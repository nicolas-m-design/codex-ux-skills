# Factory Review Guidance

Use this file when the repo contains the Factory Design System artifacts or the user names Factory directly.

## Default Artifact Order

Read the Factory sources in this order:
1. `DESIGN.md`
2. `tokens/factory.tokens.json`
3. `docs/component-specs.md`
4. `docs/figma-edit-checklist.md`
5. `docs/icon-guidelines.md`
6. `tokens/factory.css`
7. `preview.html`

Treat the first four as the primary source of truth. Use the others as supporting evidence and consistency checks.

## Preserve These Likely Strengths

Do not turn these into faux findings when the current artifacts already support them:

- canonical visual language is explicit
- token taxonomy and alias handling are explicit
- semantic colors are defined with usage guidance
- typography roles and spacing scale exist
- buttons, forms, links, tabs, badges, alerts, and cards already have meaningful state or token coverage
- icon curation is already controlled rather than open-ended

Summarize these strengths briefly in `## Coverage Snapshot` instead.

## Bias Toward These Gaps

Prioritize findings in this order when the evidence supports them:

1. Layout audit gaps
- missing reusable matrix for reflow, wrap, overflow, and narrow-screen stress cases
- responsive behavior exists in prose but not as a repeated audit contract per component

2. Annotation gaps
- missing normalized rules for headings, landmarks, semantic order, and focus order
- accessibility exists at the component level but page-level structure is not yet normalized

3. Contract-shape gaps
- component specs cover states and tokens, but not yet the same repeated contract fields for every family
- anatomy, semantic intent, responsive failure modes, and implementation notes are not yet normalized across all components

## Target Artifacts for Recommended Changes

Prefer these destinations for follow-up work:

| Need | Default target artifact |
| --- | --- |
| global design-language or layout policy | `DESIGN.md` |
| repeated component contract fields | `docs/component-specs.md` |
| execution checklist for Figma or cleanup work | `docs/figma-edit-checklist.md` |
| token additions or canonical token corrections | `tokens/factory.tokens.json` |
| icon subset or alias expansion | `docs/icon-guidelines.md` |

Avoid recommending token changes when the real gap is documentation shape.

## Factory-Specific Guardrails

- Prefer additive recommendations over style resets.
- Avoid proposing a second visual language or font family.
- Keep orange/action, neutral/base, and feedback semantics intact unless the docs themselves contradict them.
- Do not ask for runtime WCAG testing unless the user explicitly broadens the scope.
- Do not require Figma. Mention Figma only when the docs already point to design-file follow-up.

## Example Finding Shape

Good:
- "Layout guidance exists globally, but tabs, badges, and cards do not share a repeated reflow and overflow contract. Add a reusable responsive-stress matrix in `docs/component-specs.md` and reflect it in `docs/figma-edit-checklist.md`."

Weak:
- "The system needs more responsive design."

Good:
- "Factory documents component-level focus visibility, but it does not yet normalize page-level heading, landmark, and focus-order annotations for screen specs. Add a page annotation section to `DESIGN.md`."

Weak:
- "Accessibility could be improved."
