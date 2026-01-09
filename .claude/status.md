---
status: completed
updated: 2026-01-09T17:05:00+00:00
task: Fix stop hook bug and enhance hooks documentation
---

## Summary
Fixed the stop-validator.py logic bug where the compliance checklist was never shown (status check happened before stop_hook_active escape hatch). Updated both installed and repo versions with correct two-phase flow. Synced session-aware status file support to repo. Enhanced docs/concepts/hooks.md with session-aware patterns, JSON input schemas, change-type detection table, and two-phase stop flow documentation.
