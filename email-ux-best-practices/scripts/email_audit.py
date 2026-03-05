#!/usr/bin/env python3
"""Static audit for HTML email UX/accessibility issues."""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from html.parser import HTMLParser
from pathlib import Path
from typing import Dict, List, Optional, Tuple

GENERIC_ALT_TERMS = {
    "image",
    "photo",
    "graphic",
    "picture",
    "img",
    "banner",
    "logo",
}

GENERIC_LINK_TERMS = {
    "click here",
    "learn more",
    "read more",
    "more",
    "here",
    "this link",
    "go here",
}

RAW_URL_RE = re.compile(r"^(https?://|www\.)", re.IGNORECASE)

NAMED_COLORS = {
    "black": (0, 0, 0),
    "white": (255, 255, 255),
    "gray": (128, 128, 128),
    "grey": (128, 128, 128),
    "red": (255, 0, 0),
    "green": (0, 128, 0),
    "blue": (0, 0, 255),
    "navy": (0, 0, 128),
    "teal": (0, 128, 128),
    "maroon": (128, 0, 0),
    "purple": (128, 0, 128),
    "yellow": (255, 255, 0),
    "silver": (192, 192, 192),
}

SEVERITY_ORDER = {"P0": 0, "P1": 1, "P2": 2}


@dataclass
class Issue:
    severity: str
    code: str
    line: int
    col: int
    message: str
    hint: str

    def format(self) -> str:
        return f"{self.severity} {self.code} {self.line}:{self.col} - {self.message} ({self.hint})"


@dataclass
class LinkRecord:
    href: str
    text: str
    line: int
    col: int


@dataclass
class ImageRecord:
    src: str
    alt: Optional[str]
    line: int
    col: int


@dataclass
class ContrastRecord:
    line: int
    col: int
    ratio: float
    color: str
    background: str


class EmailHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.links: List[LinkRecord] = []
        self.images: List[ImageRecord] = []
        self.contrast_records: List[ContrastRecord] = []
        self.heading_count = 0
        self.section_count = 0
        self.total_text_len = 0
        self.block_lengths: List[int] = []

        self._open_links: List[Dict[str, object]] = []
        self._open_blocks: List[Dict[str, object]] = []

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        t = tag.lower()
        attr_map = {k.lower(): (v or "") for k, v in attrs if k}
        line, col = self.getpos()
        col += 1

        if t in {"h1", "h2", "h3", "h4", "h5", "h6"}:
            self.heading_count += 1
            self.section_count += 1

        if t in {"p", "li", "section", "article", "td"}:
            self.section_count += 1

        if t in {"p", "li", "td", "div"}:
            self._open_blocks.append({"tag": t, "line": line, "col": col, "text": ""})

        if t == "a":
            self._open_links.append(
                {"href": attr_map.get("href", "").strip(), "line": line, "col": col, "text": ""}
            )

        if t == "img":
            src = attr_map.get("src", "").strip()
            alt = attr_map.get("alt")
            self.images.append(ImageRecord(src=src, alt=alt, line=line, col=col))

        style = attr_map.get("style", "")
        if style:
            style_map = parse_style(style)
            if "color" in style_map and "background-color" in style_map:
                fg = parse_color(style_map["color"])
                bg = parse_color(style_map["background-color"])
                if fg and bg:
                    ratio = contrast_ratio(fg, bg)
                    self.contrast_records.append(
                        ContrastRecord(
                            line=line,
                            col=col,
                            ratio=ratio,
                            color=style_map["color"],
                            background=style_map["background-color"],
                        )
                    )

    def handle_endtag(self, tag: str) -> None:
        t = tag.lower()

        if t == "a" and self._open_links:
            link = self._open_links.pop()
            self.links.append(
                LinkRecord(
                    href=str(link.get("href", "")).strip(),
                    text=normalize_space(str(link.get("text", ""))),
                    line=int(link.get("line", 1)),
                    col=int(link.get("col", 1)),
                )
            )

        if t in {"p", "li", "td", "div"} and self._open_blocks:
            # Close the nearest matching block from the end.
            idx = -1
            for i in range(len(self._open_blocks) - 1, -1, -1):
                if self._open_blocks[i].get("tag") == t:
                    idx = i
                    break
            if idx != -1:
                block = self._open_blocks.pop(idx)
                text_len = len(normalize_space(str(block.get("text", ""))))
                if text_len > 0:
                    self.block_lengths.append(text_len)

    def handle_data(self, data: str) -> None:
        if not data:
            return
        clean = normalize_space(data)
        if not clean:
            return

        self.total_text_len += len(clean)

        if self._open_links:
            self._open_links[-1]["text"] = f"{self._open_links[-1].get('text', '')} {clean}".strip()

        if self._open_blocks:
            self._open_blocks[-1]["text"] = f"{self._open_blocks[-1].get('text', '')} {clean}".strip()


def normalize_space(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def parse_style(style_text: str) -> Dict[str, str]:
    out: Dict[str, str] = {}
    for decl in style_text.split(";"):
        if ":" not in decl:
            continue
        key, val = decl.split(":", 1)
        key = key.strip().lower()
        val = val.strip().lower()
        if key and val:
            out[key] = val
    return out


def parse_color(raw: str) -> Optional[Tuple[int, int, int]]:
    value = raw.strip().lower()
    if value in NAMED_COLORS:
        return NAMED_COLORS[value]

    hex_match = re.fullmatch(r"#([0-9a-f]{3}|[0-9a-f]{6})", value)
    if hex_match:
        h = hex_match.group(1)
        if len(h) == 3:
            return tuple(int(ch * 2, 16) for ch in h)  # type: ignore[return-value]
        return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))

    rgb_match = re.fullmatch(
        r"rgb\(\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*,\s*([0-9]{1,3})\s*\)",
        value,
    )
    if rgb_match:
        r, g, b = (int(rgb_match.group(i)) for i in range(1, 4))
        if r <= 255 and g <= 255 and b <= 255:
            return (r, g, b)

    return None


def relative_luminance(rgb: Tuple[int, int, int]) -> float:
    def channel(c: int) -> float:
        c_lin = c / 255.0
        return c_lin / 12.92 if c_lin <= 0.03928 else ((c_lin + 0.055) / 1.055) ** 2.4

    r, g, b = rgb
    return 0.2126 * channel(r) + 0.7152 * channel(g) + 0.0722 * channel(b)


def contrast_ratio(fg: Tuple[int, int, int], bg: Tuple[int, int, int]) -> float:
    l1 = relative_luminance(fg)
    l2 = relative_luminance(bg)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)


def is_generic_alt(alt: str) -> bool:
    cleaned = normalize_space(alt).lower().strip(".:-_")
    if not cleaned:
        return False
    if cleaned in GENERIC_ALT_TERMS:
        return True
    return cleaned.startswith("image of") or cleaned.startswith("photo of")


def is_generic_link_text(text: str) -> bool:
    cleaned = normalize_space(text).lower().strip(".:-_")
    return cleaned in GENERIC_LINK_TERMS


def run_audit(html_path: Path, text_path: Optional[Path]) -> List[Issue]:
    parser = EmailHTMLParser()
    html = html_path.read_text(encoding="utf-8", errors="replace")
    parser.feed(html)

    issues: List[Issue] = []

    # Image alt checks.
    for img in parser.images:
        if img.alt is None:
            issues.append(
                Issue(
                    severity="P1",
                    code="IMG_ALT_MISSING",
                    line=img.line,
                    col=img.col,
                    message="Image is missing alt attribute",
                    hint=img.src or "<img>",
                )
            )
            continue
        if is_generic_alt(img.alt):
            issues.append(
                Issue(
                    severity="P2",
                    code="IMG_ALT_GENERIC",
                    line=img.line,
                    col=img.col,
                    message="Image alt text is too generic",
                    hint=f'alt="{normalize_space(img.alt)}"',
                )
            )

    # Link checks.
    text_to_hrefs: Dict[str, set] = {}
    for link in parser.links:
        link_text = normalize_space(link.text)
        lower_text = link_text.lower()
        text_to_hrefs.setdefault(lower_text, set()).add(link.href)

        if link_text and is_generic_link_text(link_text):
            issues.append(
                Issue(
                    severity="P1",
                    code="LINK_TEXT_GENERIC",
                    line=link.line,
                    col=link.col,
                    message="Link text is generic and lacks context",
                    hint=f'text="{link_text}" href="{link.href}"',
                )
            )

        if link_text and RAW_URL_RE.match(link_text):
            issues.append(
                Issue(
                    severity="P2",
                    code="LINK_TEXT_RAW_URL",
                    line=link.line,
                    col=link.col,
                    message="Link text is a raw URL",
                    hint=f'text="{link_text}"',
                )
            )

    for text_value, hrefs in text_to_hrefs.items():
        if text_value and len(hrefs) > 1:
            issues.append(
                Issue(
                    severity="P1",
                    code="LINK_TEXT_DUPLICATE_DIFF_URL",
                    line=1,
                    col=1,
                    message="Same link text points to multiple destinations",
                    hint=f'text="{text_value}" urls={sorted(hrefs)}',
                )
            )

    # Contrast heuristic.
    for rec in parser.contrast_records:
        if rec.ratio < 4.5:
            issues.append(
                Issue(
                    severity="P1",
                    code="LOW_CONTRAST_INLINE_STYLE",
                    line=rec.line,
                    col=rec.col,
                    message=f"Low contrast ratio detected ({rec.ratio:.2f}:1)",
                    hint=f"color={rec.color} background-color={rec.background}",
                )
            )

    # Structure heuristic.
    long_blocks = [n for n in parser.block_lengths if n >= 320]
    if parser.heading_count == 0 and parser.total_text_len >= 300:
        if long_blocks and parser.section_count < 4:
            issues.append(
                Issue(
                    severity="P1",
                    code="STRUCTURE_MISSING",
                    line=1,
                    col=1,
                    message="No headings and long unchunked content detected",
                    hint="Add headings and split long paragraphs/bullets",
                )
            )
        else:
            issues.append(
                Issue(
                    severity="P2",
                    code="STRUCTURE_WEAK",
                    line=1,
                    col=1,
                    message="Email lacks clear section structure",
                    hint="Add headings and scannable chunks",
                )
            )

    # Plain-text fallback heuristic.
    fallback_ok = False
    if text_path is not None:
        fallback_ok = text_path.exists()
        if not fallback_ok:
            issues.append(
                Issue(
                    severity="P1",
                    code="PLAINTEXT_FILE_MISSING",
                    line=1,
                    col=1,
                    message="Provided plain-text fallback file path does not exist",
                    hint=str(text_path),
                )
            )
    else:
        sibling = html_path.with_suffix(".txt")
        fallback_ok = sibling.exists()

    if not fallback_ok:
        issues.append(
            Issue(
                severity="P2",
                code="PLAINTEXT_FALLBACK_NOT_FOUND",
                line=1,
                col=1,
                message="Plain-text fallback not found (heuristic)",
                hint="Provide --text fallback.txt or create sibling .txt file",
            )
        )

    issues.sort(key=lambda i: (SEVERITY_ORDER.get(i.severity, 9), i.line, i.col, i.code))
    return issues


def has_high_severity(issues: List[Issue]) -> bool:
    return any(i.severity in {"P0", "P1"} for i in issues)


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Audit an HTML email for common UX/accessibility issues.")
    parser.add_argument("html_file", help="Path to HTML email file")
    parser.add_argument("--text", dest="text_file", help="Path to plain-text fallback file")
    parser.add_argument("--json", action="store_true", help="Output JSON")
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()

    html_path = Path(args.html_file)
    if not html_path.exists():
        print(f"File not found: {html_path}", file=sys.stderr)
        return 2

    text_path = Path(args.text_file) if args.text_file else None

    issues = run_audit(html_path, text_path)

    if args.json:
        payload = {
            "file": str(html_path),
            "issue_count": len(issues),
            "issues": [asdict(i) for i in issues],
        }
        print(json.dumps(payload, indent=2))
    else:
        if not issues:
            print("No issues found.")
        else:
            for issue in issues:
                print(issue.format())
            p1_or_higher = sum(1 for i in issues if i.severity in {"P0", "P1"})
            p2 = sum(1 for i in issues if i.severity == "P2")
            print(f"Summary: {p1_or_higher} high-priority issue(s), {p2} lower-priority issue(s)")

    return 1 if has_high_severity(issues) else 0


if __name__ == "__main__":
    sys.exit(main())
