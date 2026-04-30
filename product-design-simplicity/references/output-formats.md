# Product Design Simplicity Output Formats

Use these formats when structure helps the user act on the critique. Keep the response concise unless the user asks for depth.

## Fast Critique

Use for quick product/design feedback.

```text
Top simplification opportunities:
1. [Issue]
   Change: [Concrete design change]
   Why: [Burden removed]
   Guardrail: [What not to lose]
```

## Prioritized Review

Use for design audits or complex flows.

```text
Assumptions:
- [User, job, context]

P0:
- Problem: [Highest-risk complexity]
- Change: [Specific simplification]
- Why: [Impact on comprehension, decision, action, or recovery]
- Guardrail: [Trust/accessibility/control constraint]

P1:
- ...

Validation:
- [How to verify the simplified design works]
```

## Before And After

Use when the user wants concrete redesign direction.

```text
Before:
- [Current pattern or copy]

After:
- [Simpler pattern or copy]

Why this is simpler:
- [Reduced choice, clearer mapping, better feedback, fewer steps, etc.]

Do not remove:
- [Necessary capability, signal, or recovery path]
```

## Implementation Brief

Use when handing recommendations to an engineer or design agent.

```text
Goal:
[User outcome]

Scope:
[Screens, components, states, or copy to change]

Required changes:
- [Concrete behavior/UI/copy change]

States to cover:
- Default
- Empty
- Loading
- Success
- Error
- Disabled or unavailable

Guardrails:
- Preserve [accessibility, control, trust, expert path, auditability]

Verification:
- [Manual checks, usability test prompt, analytics signal, or automated test]
```
