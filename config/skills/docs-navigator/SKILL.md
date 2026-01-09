---
name: docs-navigator
description: Navigate project documentation efficiently. Use when asked to "read the docs", "check documentation", or before starting unfamiliar tasks. Triggers on read docs, check docs, documentation, unfamiliar codebase.
---

# Documentation Navigator

Efficiently read project documentation without bloating context.

## When to Use

- User explicitly says "read the docs"
- Starting work in unfamiliar area of codebase
- Need to understand patterns/conventions before implementing

## Workflow

### Step 1: Read the Index

Always start with `docs/index.md`:
- Contains keywords and summaries for all docs
- Enables smart routing to relevant docs only

### Step 2: Match Task to Keywords

Look at the **Keywords** column in the index:
- Identify 1-3 docs that match your current task
- Don't read docs that don't match

Example matching:
- Task: "Fix authentication bug" → Match: auth, login, error handling
- Task: "Add new API endpoint" → Match: REST, routes, architecture
- Task: "Deploy to production" → Match: deploy, CI/CD, environments

### Step 3: Read Only Relevant Docs

- Read the 1-3 matched docs fully
- Apply patterns and conventions found there
- Skip unrelated docs to preserve context

### Step 4: Apply What You Learned

- Follow documented patterns exactly
- Don't deviate from established conventions
- Reference specific docs in your reasoning

## Anti-Patterns

| Don't Do This | Do This Instead |
|---------------|-----------------|
| Read all docs in index | Read only task-relevant docs |
| Skim docs superficially | Read relevant docs thoroughly |
| Ignore index, guess from memory | Always check index first |
| Read docs once and forget | Re-read when switching tasks |

## Expected docs/index.md Format

Projects using this skill should have a `docs/index.md` with this structure:

```markdown
# Documentation Index

## How to Use This Index

1. Scan the **Keywords** column for terms matching your task
2. Read the **Summary** to confirm relevance
3. Read ONLY the docs that match - don't read everything

## Documentation Map

| Doc | Keywords | Summary |
|-----|----------|---------|
| [architecture.md](architecture.md) | system design, components, data flow | High-level system architecture |
| [api/endpoints.md](api/endpoints.md) | REST, routes, handlers, requests | API endpoint specifications |
| [guides/testing.md](guides/testing.md) | tests, pytest, mocking, fixtures | Testing patterns |

## Quick Reference

- **Adding a feature?** → Read architecture.md first
- **Fixing a bug?** → Check api/errors.md and operations/monitoring.md
```

## Integration with Hooks

This skill complements the hooks:
- **SessionStart**: Reminds to read docs/index.md
- **read-docs-trigger**: When user says "read the docs", this skill guides the process
- **Stop**: Validates work against documented standards

## Example Session

```
User: Read the docs before we add a new payment endpoint

Claude: [Reads docs/index.md]

I found these relevant docs based on keywords:
- architecture.md (system design, components)
- api/endpoints.md (REST, routes, handlers)
- guides/authentication.md (auth, permissions)

[Reads those 3 docs]

Based on the documentation:
- New endpoints go in src/api/routes/
- Must follow RESTful conventions from api/endpoints.md
- Payment endpoints require auth middleware per guides/authentication.md
- Error responses must match format in api/errors.md

Ready to implement the payment endpoint following these patterns.
```

## Context Efficiency

This approach optimizes context usage:

| Approach | Context Cost | Effectiveness |
|----------|--------------|---------------|
| Read all docs | High (10k+ tokens) | Unfocused |
| Read index only | Low (500 tokens) | Incomplete |
| **Index + matched docs** | Medium (2-4k tokens) | **Targeted** |

By matching keywords before reading, you get the right context without bloat.
