---
name: review-design-system-specs
description: Factory-first audit workflow for design-system documentation, token files, component specs, and handoff checklists. Use when reviewing a design system, auditing component specs, checking layout or accessibility coverage, finding gaps in tokens/docs, improving handoff quality, or reviewing the Factory Design System. Default to audit plus remediation plan; do not use for runtime WCAG implementation testing, visual redesigns, or file rewrites unless explicitly requested.
---

# Review Design System Specs

## Operating Mode

- Audit text artifacts first.
- Treat current design-system docs and tokens as the baseline source of truth.
- Prefer additive recommendations over resets or redesigns.
- Keep the review text-driven. Do not require Figma or live web research at runtime.
- Do not rewrite files by default. Produce findings, a prioritized remediation plan, and acceptance criteria.

## Default Inputs

Look for these artifacts in order:
- `DESIGN.md`
- `docs/component-specs.md`
- `docs/figma-edit-checklist.md`
- `tokens/factory.tokens.json`
- `docs/icon-guidelines.md`
- `tokens/*.css`
- `preview.html`

If some artifacts are missing:
- Continue.
- Label the review as partial.
- Separate high-confidence conclusions from assumption-driven conclusions.

## Reference Loading

Load references in this order:
1. `references/design-system-audit-rubric.md` for the review matrix and evidence rules.
2. `references/factory-review-guidance.md` when the user names Factory or the repo contains the default Factory files listed above.
3. `references/external-best-practices.md` when you need rationale, tie-breakers, or source-backed justification.

Load templates every time:
- `templates/audit-report-template.md`
- `templates/remediation-backlog-template.md`

## Deterministic Workflow

1. Inventory sources. List found and missing artifacts. Decide whether the review is `Factory-first` or `generic`.
2. Build the coverage snapshot. Score foundations and each documented component with the evidence states `documented`, `partial`, `missing`, or `contradictory`.
3. Identify only concrete gaps. Prefer gaps that would cause implementation guessing, inconsistent layout behavior, or accessibility regression.
4. Group findings by:
   - `Layout`
   - `Spec Completeness`
   - `Accessibility`
   - `Handoff Clarity`
5. Prioritize with these severities only:
   - `high`: likely to cause inaccessible or inconsistent implementation
   - `medium`: incomplete contract that will cause ambiguity or rework
   - `low`: polish, clarity, or future-proofing gap
6. Build the remediation plan from `templates/remediation-backlog-template.md`.
7. Finish with explicit acceptance criteria tied to the affected docs.

## Output Contract

Always render output in this exact order:
1. `## Scope & Assumptions`
2. `## Coverage Snapshot`
3. `## Findings`
4. `## Prioritized Remediation Plan`
5. `## Acceptance Criteria`

Additional rules:
- Use the evidence states exactly as written.
- Do not dump findings file by file.
- Summarize existing strengths briefly in `## Coverage Snapshot`; do not convert strengths into faux findings.
- Cite the artifact path for every finding.
- Name the target artifact and the contract to add or clarify for every remediation item.

## Factory-First Bias

When reviewing the Factory Design System:
- Read the current docs first and treat them as the baseline, not as something to replace wholesale.
- Preserve existing strengths around token taxonomy, visual language, semantic color usage, component states, and icon curation when they are already explicit.
- Bias recommendations toward the highest-value gaps already likely in this repo:
  - missing reusable layout stress rules for reflow, wrap, overflow, and narrow-screen behavior
  - missing normalized page-level annotation rules for headings, landmarks, semantic order, and focus order
  - missing repeated component contract fields for anatomy, semantics, responsive failure modes, and implementation annotations
- Prefer doc additions, table expansions, and checklist normalization over redesign language.

## Boundaries

- Do not turn this into a runtime accessibility conformance audit.
- Do not prescribe visual redesigns unless the user explicitly asks.
- Do not invent missing implementation details as facts; label them as recommendations.
- Do not leak Factory-specific terminology into generic audits unless the user is reviewing Factory.
- If the user explicitly asks for rewrites, produce them only after the audit and keep them scoped to the named artifacts.

## Quick Trigger Examples

- "Review our design system and find spec gaps."
- "Audit these component specs for layout and accessibility coverage."
- "Check our tokens and docs for missing handoff details."
- "Review Factory Design System and propose the next documentation fixes."
