# Design System Audit Rubric

Use this rubric to turn design-system docs into a deterministic review. Default to evidence quality over volume: a rule is `documented` only when a developer could implement it without guessing.

## Evidence States

Use these states exactly:

- `documented`: explicit, unambiguous, and implementation-ready
- `partial`: mentioned or implied, but still leaves meaningful decisions open
- `missing`: not specified in the reviewed artifacts
- `contradictory`: two or more artifacts disagree on the canonical rule

Escalation rules:
- Prefer `partial` when the intent exists but the behavior contract is incomplete.
- Use `contradictory` whenever the same component or token rule is expressed differently across files.
- Treat screenshots, specimen pages, or preview markup alone as supporting evidence, not as a complete contract.

## Severity Rules

Use these severities exactly:

- `high`: likely to cause inaccessible or inconsistent implementation
- `medium`: incomplete contract that will create ambiguity, rework, or uneven quality
- `low`: polish, clarity, or future-proofing gap

Escalate toward `high` when the missing contract affects keyboard behavior, focus treatment, target size, labels and errors, responsive failure modes, or semantic roles.

## Foundations Review

Review each foundation area against these checks:

| Area | Count as `documented` only when the artifacts explicitly define | Escalate when missing |
| --- | --- | --- |
| Token taxonomy | canonical naming rules, alias handling, semantic vs primitive guidance, source of truth | implementers could bind raw values inconsistently |
| Semantic usage | which semantic tokens power actions, feedback, surfaces, text, borders, icons | components could bypass semantics or misuse feedback colors |
| Typography roles | named text styles, size/line-height/weight, usage guidance | teams could invent parallel type roles |
| Spacing scale | approved spacing steps and guidance against ad hoc values | layout rhythm will drift |
| Radius and borders | radius policy, border widths, indicator thickness, focus treatment widths | controls and states will vary arbitrarily |
| Elevation | explicit rule for flat, outlined, or overlay surfaces | overlays and cards will diverge visually |
| Icon policy | approved subset, sizing, color roles, and growth rules | icon usage will sprawl without control |

## Layout Review

Review layout guidance across page-level docs and component docs. Mark gaps when these are absent or only implied:

- container width rules
- grid or alignment rules
- spacing behavior between sections and inside components
- wrap behavior for long labels, chips, actions, and metadata
- overflow behavior for horizontal lists, tables, or tab rows
- zoom and reflow expectations
- small-screen and orientation behavior
- explicit avoidance of unnecessary two-dimensional scrolling

Count layout as `documented` only when the failure mode is named, not just the ideal layout.

## Component Contract Review

For every documented component family, check whether the same contract shape is present. A component is fully `documented` only when these fields are explicit:

- anatomy
- variants
- sizes
- full state matrix
- behavior notes
- content rules
- placement rules
- semantic intent
- implementation notes
- responsive failure modes
- accessibility notes

Interpretation rules:
- If a component has strong state coverage but no anatomy or semantic intent, mark `partial`.
- If behavior is implied by a Figma checklist but absent from the canonical spec doc, mark `partial`.
- If token bindings disagree with narrative guidance, mark `contradictory`.

## Accessibility Review

Review the design-system docs for design-time accessibility coverage, not runtime conformance testing. Check whether the system explicitly documents:

- text contrast expectations
- non-text contrast for boundaries, icons, and focus indicators
- visible focus treatment
- target size or spacing expectations for tap-first contexts
- keyboard interaction for composite widgets
- focus order or focus movement where interaction changes context
- landmarks and heading structure where page-level templates or layouts exist
- labels, helper text, error text, and non-color signaling for forms
- announcement or semantic intent guidance for alerts, status, and urgent messaging

Use official guidance as the tie-breaker for normative requirements. If the docs imply accessibility through aesthetics only, mark `partial` or `missing`.

## Handoff Clarity Test

After reviewing foundations, layout, components, and accessibility, ask:

- Could a developer implement the component without inventing hidden behavior?
- Could a designer extend the system without guessing naming, placement, or state rules?
- Could QA verify the contract from the docs alone?

If the answer is no, create a `Handoff Clarity` finding even when the visual direction is strong.

## Recommended Review Order

Use this order unless the user requests otherwise:
1. foundations
2. layout
3. component contracts
4. accessibility
5. handoff clarity

## Generic vs Factory-First Use

For generic systems:
- apply the rubric without assuming Factory terminology
- keep examples neutral unless the user asks for Factory comparisons

For Factory-first reviews:
- use this rubric, then apply the repo-specific bias in `references/factory-review-guidance.md`
