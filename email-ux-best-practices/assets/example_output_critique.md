# Executive Summary
- Subject and preheader are generic and do not set accurate expectations.
- The core action is present but link wording is weak and not descriptive.
- Copy is concise but lacks reassurance and security context.
- The draft risks confusion for users who did not initiate the reset.

# Top Issues (P0/P1/P2)

## P1-1
- Problem: Generic action link text reduces clarity.
- Why it matters: Users scanning quickly may not trust or understand the action.
- Fix recommendation: Replace generic anchor text with explicit destination language.
- Exact snippet to change:
  - Problematic: "Use this link to reset your password: click here."
  - Replacement: "Reset your password securely: Reset password"

## P1-2
- Problem: Missing explicit expiration context for the reset action.
- Why it matters: Users cannot judge urgency and may attempt expired links.
- Fix recommendation: Add token expiration line and fallback support path.
- Exact snippet to change:
  - Problematic: "If you did not request this, ignore."
  - Replacement: "If you did not request this, ignore this email. This reset link expires in 30 minutes."

## P2-1
- Problem: Greeting and close are minimal and can feel abrupt.
- Why it matters: Low trust in security-sensitive communication.
- Fix recommendation: Add recognizable sender context.
- Exact snippet to change:
  - Problematic: "Hi,"
  - Replacement: "Hi,\n\nYou requested a password reset for your account."

# CTA & Link Issues
- Primary CTA text should be explicit: "Reset password".
- Avoid naked/generic links.
- Keep one clear action only; avoid extra links in this transactional email.

# Accessibility Checklist
- [ ] Subject sets expectation clearly.
- [ ] Preheader provides useful context.
- [ ] Link purpose is clear out of context.
- [ ] One primary action is obvious.
- [ ] Reading order is logical.
- [ ] No image-only critical content.
- [ ] Adequate color contrast in rendered template.
- [ ] CTA is keyboard focusable and visually apparent.
- [ ] Alt text exists for informative images.
- [ ] Decorative images have empty alt.
- [ ] Body copy remains understandable with images off.
- [ ] Heading/section markers are consistent where used.

# QA Checklist
- [ ] Reset link routes to correct secure domain.
- [ ] Link expiry time is accurate.
- [ ] Security fallback line included.
- [ ] Sender name matches brand/account context.
- [ ] Reply-to path is valid for support questions.
- [ ] Email contains no promotional add-ons.
- [ ] Copy is short and mobile-readable.
- [ ] Test in Outlook/webmail/mobile clients.
- [ ] Test with dark mode enabled.
- [ ] Test with images blocked.
- [ ] Validate plain-text fallback version.
- [ ] Validate all links and tracking params.
