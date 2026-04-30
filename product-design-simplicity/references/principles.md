# Product Design Simplicity Principles

These principles distill practical ideas from product design, usability, human factors, and design thinking literature. Do not quote or summarize books; use the ideas operationally.

## Core Principles

1. Purpose before polish
   - Know the user goal before changing the surface.
   - Remove anything that does not help the user understand, decide, act, or recover.

2. Obvious over clever
   - Make the primary action, current state, and next step visible.
   - Prefer familiar patterns when novelty does not improve the task.

3. Recognition over recall
   - Keep important choices, constraints, and consequences visible at the point of decision.
   - Avoid making users remember rules, previous steps, hidden modes, or jargon.

4. Good mapping
   - Place controls near the thing they affect.
   - Make relationships between labels, controls, outcomes, and status explicit.

5. Useful constraints
   - Prevent invalid actions where possible.
   - Narrow choices to what is relevant in the current context.

6. Feedback and recovery
   - Show what happened, what is happening, and what the user can do next.
   - Preserve undo, cancel, back, edit, retry, and graceful error handling for consequential tasks.

7. Progressive disclosure
   - Keep the common path direct.
   - Reveal advanced options when intent, expertise, or task context makes them useful.

8. Plain language
   - Use user-facing terms, not implementation terms.
   - Prefer specific verbs and concrete nouns over vague labels.

9. Defaults with agency
   - Choose helpful defaults that reduce setup and decision load.
   - Let users inspect and change consequential defaults.

10. Simplicity with trust
   - Do not hide pricing, privacy, risk, destructive consequences, or irreversible changes.
   - Do not simplify by removing accessibility, transparency, or necessary control.

## Reduction Ladder

Use this sequence when simplifying a feature or screen:

1. Can it be removed?
2. Can it be merged with an existing concept?
3. Can it be moved later in the flow?
4. Can a sensible default handle it?
5. Can the system infer it safely?
6. Can it appear only after user intent is clear?
7. Can better wording make it unnecessary?
8. Is explanation still required?

## Common Failure Modes

- Minimalism: fewer visible elements, but more hidden work.
- Over-disclosure: every option shown because every option exists.
- Over-automation: fewer steps, but less control, transparency, or trust.
- False consistency: identical patterns used for tasks with different risks.
- Decorative clarity: polished layout that does not clarify decisions.
- Expert bias: optimizing for internal teams or power users while making first use harder.
