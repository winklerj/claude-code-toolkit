#!/usr/bin/env python3
"""
UserPromptSubmit hook - triggers documentation reading when user says "read the docs".
"""
import json
import sys


def main():
    try:
        input_data = json.load(sys.stdin)
    except json.JSONDecodeError:
        sys.exit(0)

    message = input_data.get("message", "").lower()

    # Only fire when user explicitly requests doc reading
    if "read the docs" not in message:
        sys.exit(0)

    reminder = """Use ultrathink to thoroughly understand the documentation.

Before starting this task, you MUST:

1. Read docs/index.md to understand the documentation structure
2. Use the docs-navigator skill pattern to identify relevant docs
3. Match your task keywords to the index keywords
4. Read ONLY the 1-3 most relevant docs (not all)
5. Apply the patterns and conventions documented there

Do NOT skip this step. Do NOT read all docs. Read smart, not everything."""

    print(reminder)
    sys.exit(0)


if __name__ == "__main__":
    main()
