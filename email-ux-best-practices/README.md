# email-ux-best-practices

`email-ux-best-practices` is a Codex skill for writing, reviewing, and shipping emails that are readable, scannable, accessible, and effective across devices and email clients.

Supported modes:
- `critique`
- `rewrite` (default)
- `variants`
- `html-lite`

## Example Invocations

```text
Use $email-ux-best-practices mode=critique on this transactional reset email and give prioritized issues only.
```

```text
Use $email-ux-best-practices mode=rewrite email_type=lifecycle tone=friendly length=short on this draft.
```

```text
Use $email-ux-best-practices mode=variants tone=friendly length=short for this winback campaign.
```

```text
Use $email-ux-best-practices mode=html-lite on this plain text and include a plain-text fallback.
```

## Install via `$skill-installer` (GitHub Directory URL)

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --url https://github.com/<owner>/<repo>/tree/main/email-ux-best-practices
```

Restart Codex to pick up new skills.

## Optional: OpenAI Skills API Upload

```bash
cd /path/to/repo-root
zip -r email-ux-best-practices.zip email-ux-best-practices

curl https://api.openai.com/v1/skills \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -F "file=@email-ux-best-practices.zip"
```
