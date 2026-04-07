# External Best Practices

Use this file for rationale and tie-breakers. Prefer official and system-doc sources over practitioner commentary.

## Source Priority

Use this priority order when reconciling guidance:
1. W3C and WAI normative guidance
2. mature design-system documentation with explicit checklists
3. practitioner articles and annotation write-ups

## Distilled Rules

### 1. Keep a markdown-first system narrative

Source:
- VoltAgent Lovable `DESIGN.md`

Working rule:
- Maintain one concise narrative document that explains canonical visual language, token philosophy, and system intent in plain language before diving into component specifics.

Why it matters:
- A system becomes easier to audit when high-level language, principles, and constraints are stated once and referenced everywhere else.

### 2. Treat component specs as implementation contracts

Source:
- Carbon component checklist

Working rule:
- A component spec is incomplete if it stops at variants and screenshots. The contract should cover anatomy, states, behavior, content rules, accessibility, and edge conditions.

Why it matters:
- The hardest design-system failures usually come from undocumented states and behaviors, not missing colors.

### 3. Annotate behavior and semantics, not just visuals

Sources:
- Primer designer checklist
- Primer annotation toolkit
- GitHub annotation articles
- Stephanie Walter on documenting accessibility interactions

Working rule:
- Document keyboard interaction, focus movement, landmarks, headings, semantic order, live or status messaging intent, and other non-visual behaviors directly in the spec or handoff layer.

Why it matters:
- A polished component library still produces inaccessible products when semantics and interaction rules are omitted from the handoff.

### 4. Use W3C as the normative floor

Sources:
- WAI Tabs Authoring Practices
- WCAG 2.2 Understanding docs for Focus Appearance, Target Size Minimum, and Non-text Contrast

Working rule:
- For interaction widgets and visible accessibility requirements, prefer explicit references to normative behavior over taste-based recommendations.

Practical implications for spec review:
- tabs should not be considered complete without keyboard interaction and active-state semantics
- focus indicators need explicit visibility guidance, not just color styling
- target size or spacing expectations should be stated for tap-first contexts
- non-text contrast matters for control boundaries, icons, and focus indicators

### 5. Review failure modes, not just ideal states

Cross-source synthesis:
- mature systems document overflow, wrapping, small-screen behavior, dense content, long labels, and error conditions

Working rule:
- Count layout or component behavior as complete only when the doc explains what happens under stress, not only the happy path.

## What Not to Import Into This Skill

- Do not turn external examples into brand or visual mandates.
- Do not require live browsing at runtime.
- Do not import social-media opinion as a normative requirement.
- Do not broaden the skill into runtime conformance testing.

## Suggested Citation Style In Reviews

When you need to justify a recommendation, keep it short:
- "This follows the existing WAI Tabs interaction pattern."
- "This closes a common handoff gap called out by Primer and GitHub's annotation guidance."
- "This change aligns the spec with the same contract shape used by mature design systems such as Carbon."
