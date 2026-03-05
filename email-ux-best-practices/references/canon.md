# Email UX Canon (Paraphrased, Actionable)

## A) Content Structure & Scanability
- Lead with the decision-relevant message in the first screenful.
- Keep one clear primary action per email unless content format explicitly requires multiple stories.
- Use short sections with informative headings.
- Break dense text into bullets when readers must compare or choose.
- Put deadlines, pricing, and policy changes in easy-to-spot lines.
- Ensure subject and preheader accurately preview the body promise.

## B) Readability & Plain Language
- Use short sentences and common words.
- Prefer active voice and direct verbs.
- Avoid internal jargon, acronyms, and vague filler.
- Make each paragraph about one idea.
- Keep reading level to standard or simpler unless domain language is required.
- Write instructions as explicit actions, not implications.

## C) Visual Hierarchy & Layout
- Use a clear reading order: headline -> context -> action -> support details.
- Keep body text comfortable (typically around 16px, line-height around 1.4-1.6).
- Keep container width email-safe (roughly 600px).
- Use whitespace to separate sections and reduce cognitive load.
- Use emphasis sparingly; avoid walls of bold or italic text.
- Do not rely on image-only text for essential meaning.

## D) Links & CTAs
- Make link text descriptive and self-explanatory out of context.
- Avoid generic anchors like "click here" unless context is unambiguous.
- Keep one primary CTA visually dominant.
- Place the primary CTA early enough to be seen without long scrolling.
- Ensure CTA destination matches the promise in subject/body.
- Use supporting links only when they reduce risk or clarify edge cases.

## E) Accessibility (Screen Readers, Contrast, Alt Text)
- Preserve semantic reading order in source so assistive technology follows the intended sequence.
- Ensure color contrast is sufficient for text and controls.
- Use live text for important content; avoid images as the only source of key information.
- Provide purposeful alt text for informative images; use empty alt for decorative images.
- Keep heading structure logical and non-skipping where possible.
- Ensure link purpose is clear without requiring surrounding visual layout.

## F) Mobile & Responsive Behavior
- Assume many recipients read on mobile first.
- Keep line lengths and paragraph lengths short for narrow screens.
- Ensure CTA controls are thumb-friendly with enough spacing.
- Avoid side-by-side blocks that collapse poorly in constrained widths.
- Keep key action and critical context above long secondary detail.
- Test zoom behavior and spacing for small screens.

## G) Trust & Compliance
- Use recognizable sender identity and coherent reply-to behavior.
- Include unsubscribe controls where required and make them discoverable.
- Include preference-center paths when ongoing subscription control matters.
- Include postal/business address when required by region or campaign type.
- Separate mandatory service messages from optional marketing language.
- Avoid manipulative urgency and misleading claims.

## H) Email-Client Constraints (Outlook, Dark Mode, Images Off)
- Expect inconsistent CSS support; favor simple table-friendly layouts.
- Use inline styles for critical rendering behavior.
- Anticipate Outlook quirks and test button rendering patterns.
- Account for dark mode color inversion and preserve readable contrast.
- Assume images may be blocked; ensure message survives without images.
- Verify rendering in major clients before send (at minimum Outlook + webmail + mobile).
