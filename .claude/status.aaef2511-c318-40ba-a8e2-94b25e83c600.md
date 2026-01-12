---
status: completed
updated: 2026-01-12T15:35:00+00:00
task: Remove auto-switch module completely
---

## Summary
Completely removed the claude-auto-switch module:

- Deleted ~/.claude/scripts/claude-auto-switch/ (active installation)
- Deleted prompts/config/scripts/claude-auto-switch/ and docs/guides/auto-switch.md
- Deleted mimesis/docs/claude-code/.../claude-auto-switch/ and auto-switch.md
- Removed alias from ~/.zshrc
- Cleaned MEMORIES.md and README references

Verified: `which claude` now returns `/opt/homebrew/bin/claude`

Commits:
- prompts: `a15c061`
- mimesis: `67cd15d`
