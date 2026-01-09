# Documentation Index

> Template for projects using the docs-navigator skill. Copy this to `docs/index.md` and customize for your project.

## How to Use This Index

1. Scan the **Keywords** column for terms matching your task
2. Read the **Summary** to confirm relevance
3. Read ONLY the docs that match - don't read everything

## Documentation Map

| Doc | Keywords | Summary |
|-----|----------|---------|
| [architecture.md](architecture.md) | system design, components, data flow, infrastructure | High-level system architecture and component relationships |
| [api/endpoints.md](api/endpoints.md) | REST, routes, handlers, authentication, requests | API endpoint specifications and request/response formats |
| [api/errors.md](api/errors.md) | error codes, exceptions, error handling, validation | Error response formats and handling patterns |
| [operations/deployment.md](operations/deployment.md) | deploy, CI/CD, docker, kubernetes, environments | Deployment procedures and environment configuration |
| [operations/monitoring.md](operations/monitoring.md) | logs, metrics, alerts, observability, debugging | Monitoring setup and debugging procedures |
| [guides/authentication.md](guides/authentication.md) | auth, login, JWT, sessions, OAuth, permissions | Authentication flows and security patterns |
| [guides/testing.md](guides/testing.md) | tests, pytest, mocking, fixtures, coverage | Testing patterns and test execution |

## Quick Reference

- **Adding a feature?** → Read architecture.md first
- **Fixing a bug?** → Check api/errors.md and operations/monitoring.md
- **Deploying changes?** → Read operations/deployment.md
- **Auth issues?** → Read guides/authentication.md
- **Writing tests?** → Read guides/testing.md

---

## Template Instructions

### Required Structure

Your `docs/index.md` must have:

1. **Documentation Map table** with columns:
   - `Doc` - Link to the documentation file
   - `Keywords` - Comma-separated terms for matching
   - `Summary` - One-line description

2. **Quick Reference section** - Common tasks mapped to docs

### Keyword Guidelines

Good keywords are:
- **Specific** - "JWT", "pytest", "docker" (not "code", "file", "thing")
- **Action-oriented** - "deploy", "test", "authenticate"
- **Domain terms** - Words your team uses to describe features

### Keeping It Updated

Update this index when you:
- Add new documentation
- Rename or reorganize docs
- Add major features that need documentation
