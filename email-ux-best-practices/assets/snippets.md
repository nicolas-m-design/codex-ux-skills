# Email UX Snippets

## Bulletproof Button (Outlook-friendly VML + standard anchor)
```html
<!--[if mso]>
<v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="https://example.com" style="height:44px;v-text-anchor:middle;width:220px;" arcsize="8%" strokecolor="#0b5fff" fillcolor="#0b5fff">
  <w:anchorlock/>
  <center style="color:#ffffff;font-family:Arial,sans-serif;font-size:16px;font-weight:bold;">Primary action</center>
</v:roundrect>
<![endif]-->
<!--[if !mso]><!-- -->
<a href="https://example.com" style="display:inline-block;background:#0b5fff;color:#ffffff;text-decoration:none;padding:12px 18px;border-radius:4px;font-size:16px;font-weight:700;">Primary action</a>
<!--<![endif]-->
```

## Spacer Pattern
```html
<tr><td height="16" style="font-size:16px;line-height:16px;">&nbsp;</td></tr>
```

## Divider Pattern
```html
<tr>
  <td style="padding:16px 0;">
    <hr style="border:none;border-top:1px solid #d9dde3;margin:0;" />
  </td>
</tr>
```

## Hidden Preheader Pattern
```html
<div style="display:none!important;visibility:hidden;opacity:0;color:transparent;height:0;width:0;overflow:hidden;mso-hide:all;">
  Short preheader text that supports the subject line.
</div>
```

## Dark Mode Notes
### Do
- Use strong foreground/background contrast by default.
- Prefer transparent PNGs for logos if brand palette allows.
- Validate CTA contrast in dark mode previews.
- Keep critical message in live text, not image text.

### Do Not
- Depend on subtle gray-on-gray combinations.
- Assume client dark-mode behavior is consistent.
- Use background images for critical content blocks.
- Hide essential context inside decorative images.
