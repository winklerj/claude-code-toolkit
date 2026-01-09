#!/usr/bin/env python3
"""
UserPromptSubmit hook - outputs MANDATORY instructions for Claude to write working status.

This hook fires on every user prompt and instructs Claude to write its status
to <cwd>/.claude/status.<session_id>.md. The daemon watches these files and streams
updates to the Mimesis UI.

Exit codes:
  0 - Allow action (stdout added to Claude's context)
"""
import json
import sys
from datetime import datetime, timezone


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    cwd = input_data.get("cwd", "")
    session_id = input_data.get("session_id", "")

    if not cwd:
        sys.exit(0)

    # Determine status file path - session-specific if available, else legacy
    if session_id:
        status_file = f"{cwd}/.claude/status.{session_id}.md"
    else:
        status_file = f"{cwd}/.claude/status.md"

    # Generate current timestamp
    timestamp = datetime.now(timezone.utc).isoformat()

    # Output MANDATORY instruction for Claude to write status file
    # Using strong language to compete with user request priority
    instruction = f"""<system-reminder>
MANDATORY: You MUST write your status to {status_file} BEFORE proceeding.

This is REQUIRED for the Mimesis monitoring UI. The stop hook will BLOCK you from
stopping if this file is missing or stale. Write it NOW.

```markdown
---
status: working
updated: {timestamp}
task: <brief description of what you're working on>
---

## Summary
<1-2 sentence summary of current activity>
```

Do NOT skip this step. Update this file when:
- Starting a new subtask
- Encountering blockers
- Completing significant milestones
</system-reminder>"""

    print(instruction)
    sys.exit(0)


if __name__ == "__main__":
    main()
