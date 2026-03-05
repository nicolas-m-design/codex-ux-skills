---
name: email-ux-best-practices
description: Opinionated email UX and accessibility workflow for marketing, product, lifecycle, transactional, and internal emails. Use when reviewing or rewriting email drafts to improve readability, scanability, accessibility, mobile performance, CTA clarity, and sender trust, or when generating subject/preheader/CTA variants and HTML-lite email output.
metadata:
  tags:
    - email-ux
    - accessibility
    - copywriting
    - lifecycle
    - transactional
  inputs:
    - Email draft in plain text or HTML
    - Optional parameters: mode, email_type, audience, intent, tone, length, reading_level, primary_cta, constraints
  outputs:
    - Critique report schema
    - Rewrite schema (plain text + optional HTML-lite)
    - Variants schema
    - HTML-lite schema
  safety_notes:
    - Do not generate spammy, deceptive, or black-hat content.
    - Do not promise deliverability guarantees.
    - Keep legal/compliance reminders and required sender identity elements.
---

# Email UX Best Practices

## Operating Defaults
- Run in text-first mode by default.
- Use `mode="rewrite"` when mode is not provided.
- Keep one primary CTA by default. Allow multiple CTAs only when the user explicitly asks (for example, multi-story newsletters).
- Default to short, scannable writing with headings, bullets, and short paragraphs.
- Prefer plain language over jargon.

## When To Use
- Improve a draft email before sending.
- Review email UX/accessibility quality without rewriting full copy.
- Generate variant sets for subject lines, preheaders, openers, and CTA text.
- Convert email copy into minimal email-client-safe HTML with plain-text fallback.

## When Not To Use
- Deliverability engineering (IP warmup, list hygiene, inbox placement guarantees).
- Spammy growth hacks or deceptive copy.
- Long-form legal drafting beyond email UX and structure.

## Parameters
- `mode`: `critique | rewrite | variants | html-lite` (default `rewrite`)
- `email_type`: `transactional | lifecycle | marketing | internal` (infer if omitted)
- `audience`: optional string
- `intent`: required only if not inferable from draft/context
- `tone`: `friendly | neutral | formal | enthusiastic | brand-voice` (default `neutral`)
- `length`: `short | medium | long` (default `medium`)
- `reading_level`: `simple | standard` (default `standard`)
- `primary_cta`: optional string; infer if missing
- `constraints`: optional list of required elements (for example: legal line, postal address, pricing terms)

## Intake Protocol (Ask Only If Essentials Are Missing)
Ask at most 5 questions, only when essentials are missing:
1. What is the `email_type`?
2. Who is the audience, and what should they do after reading (intent)?
3. Which constraints are mandatory (brand voice, max length, legal lines, address, pricing terms)?
4. Which output format is needed (plain text only or include HTML-lite)?
5. What is the single primary CTA? (If user insists, allow multi-CTA.)

If enough information is present, infer missing fields and proceed.

## Deterministic Review Workflow (Use In All Modes)
1. Subject + preheader checks: verify clarity, specificity, and expectation-setting.
2. Above-the-fold checks: ensure first 2-4 lines communicate value and action.
3. Scanability checks: headings, bullets, chunking, and short paragraphs.
4. Readability checks: sentence length, active voice, jargon removal, plain-language clarity.
5. CTA + link checks: descriptive link text, one primary action, adequate visual spacing.
6. Accessibility checks:
   - Remind about contrast, image-off behavior, and live text preference.
   - Apply alt text rules: decorative vs informative images, concise purpose-first alt text.
   - Preserve logical reading order and semantic structure.
7. Mobile checks: thumb-friendly CTA size/spacing, line length, breathing room.
8. Trust/compliance checks: sender identity, reply-to clarity, unsubscribe/preference controls, business address when required.
9. Formatting checks:
   - Body text 14-18px (target 16px), line-height 1.4-1.6.
   - Button/body spacing at least 12-16px vertically.
   - Email container max-width about 600px.
   - Use bold for emphasis sparingly; avoid long italics.
10. Email-client reality checks: Outlook rendering, dark mode inversion, blocked images.

## Output Schemas (Fixed By Mode)

### Mode: `critique`
Output only diagnosis. Do not provide a full rewritten email.
1. Executive Summary (2-4 bullets)
2. Top Issues (P0/P1/P2), each with:
   - Problem
   - Why it matters
   - Fix recommendation
   - Exact snippet to change: quote problematic line + propose replacement
3. CTA & Link Issues
4. Accessibility Checklist (10-20 items)
5. QA Checklist (10-20 items)

### Mode: `rewrite` (default)
1. Executive Summary
2. Top Issues (P0/P1/P2) with brief rationale
3. Revised Email
   - Plain text version (always required)
   - HTML-lite version (optional; include when user asks or source is HTML)
4. Subject + preheader (3 options each)
5. CTA spec
   - Primary CTA
   - Secondary links (if any)
   - Expected landing behavior
6. Accessibility checklist
7. QA / send checklist

### Mode: `variants`
Output variants only. Do not output a full rewritten email.
1. Subject lines (10)
2. Preheaders (10)
3. Openers (5) (first 1-2 lines)
4. CTA button text variants (10)
5. CTA supporting lines (5)
6. Optional microcopy variants (3) for one key detail (pricing, deadline, policy)

### Mode: `html-lite`
1. Minimal HTML email body
   - Table-friendly structure
   - Inline styles
   - Max-width container
   - Bulletproof button pattern
2. Plain-text fallback (always)
3. Notes
   - Test in Outlook
   - Test in dark mode
   - Test with images off
   - Accessibility notes: alt text, live text, descriptive links

If input is plain text, convert to HTML-lite safely without inventing unsupported layout complexity.

## Prioritization Rubric
- P0: legal/compliance risk, inaccessible critical path, or severely misleading copy.
- P1: high confusion risk, weak action clarity, significant scanability/readability problems.
- P2: polish improvements that increase speed, confidence, and consistency.

## Reference Loading
- Load `references/canon.md` only when you need principle-level guidance or tie-breakers.
- Prefer the deterministic workflow above for execution.

## Optional Static Audit Script
Use `scripts/email_audit.py` to perform deterministic static checks on HTML email files.

```bash
python3 scripts/email_audit.py /path/to/email.html
python3 scripts/email_audit.py /path/to/email.html --text /path/to/fallback.txt
python3 scripts/email_audit.py /path/to/email.html --json
```

Script flags:
- Missing or generic alt text
- Weak/generic link text
- Raw URL link text
- Duplicate link text mapping to different URLs
- Missing plain-text fallback heuristic
- Low-contrast inline-style risks (heuristic)
- Missing structure/chunking (heuristic)
