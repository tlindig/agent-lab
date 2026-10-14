# Skill: Validate

## Procedure

Validate one Target Agent (`<target-slug>`) per run, per `evolver.agent.md` § Target Agent.

### Step 1 — Build the File Map

Table `File | Load condition | Present`:

- `<target-project_root>/AGENTS.md` — always
- `<target-project_root>/.agents/<target-slug>.agent.md` — always
- `<target-project_root>/.github/agents/<target-slug>.agent.md` — always (symlink)
- `<target-project_root>/README-<target-slug>.md` — always
- `<target-project_root>/.agents/<target-slug>/skills/INDEX.md`, `skills/<skill>.md` — if present
- `<target-project_root>/.agents/<target-slug>/guides/INDEX.md`, `guides/<guide>.md` — if present
- `<target-project_root>/.agents/<target-slug>/templates/INDEX.md`, `templates/<template>.md` — if present

### Step 2 — Check Rules

Each check is a binary pass/fail against an existing rule — not a quality judgment; severity marks how serious a failure is. Improvements to things that already pass → `optimize.md`.

- **Completeness** (Error): `<target-project_root>/.agents/<target-slug>.agent.md` exists; `<target-project_root>/.github/agents/<target-slug>.agent.md` is a symlink to `../../.agents/<target-slug>.agent.md` (no content of its own); `<target-project_root>/README-<target-slug>.md` exists; `<target-project_root>/AGENTS.md` exists, required by the Session Start block (see Session Start check), which reads it via `read_file(AGENTS.md)`
- **Language** (Warning): `<target-project_root>/.agents/<target-slug>.agent.md` and `<target-project_root>/README-<target-slug>.md` are English throughout, per `<target-project_root>/AGENTS.md` § Communication
- **Session Start** (Error): the Target Agent's `.agent.md` contains the "Session Start (mandatory)" section, matching the template verbatim, or a faithful translation per `<target-project_root>/AGENTS.md` § Communication
- **README scope** (Warning): `<target-project_root>/README-<target-slug>.md` stays user-facing — purpose and usage only; no internal rules, decision logic, or process steps
- **INDEX.md role** (Warning, if the folder exists): has a routing table, no rule logic
- **Guides role** (Warning, if `guides/` exists): reference material only — no activation logic, procedure steps, or behavioral rules
- **Templates role** (Warning, if the folder exists): scaffolding templates use `<...>` placeholders; no rule logic permitted
- **Skill file structure** (Error): each skill file has a `## Procedure` section
- **Duplication** (Warning): rules defined in `<target-slug>.agent.md` are referenced from skills/guides, not restated; a principle already in `AGENTS.md` is referenced, not copied
- **Explicit invocation** (Warning): a skill that deletes or overwrites files as part of its own procedure has an unambiguous, direct-request condition in `skills/INDEX.md` — not inferable from loosely related phrasing
- **Placeholder conventions** (Warning): `<target-slug>`, `<Target Agent Name>`, `<target-project_root>`, `<project_root>` used correctly per `AGENTS.md` § Placeholder Conventions and `evolver.agent.md` § Target Agent
- **Path resolution** (Error): every file path in backticks uses the literal `<target-project_root>/` or `<project_root>/` prefix where it points into a project root; flag a bare reference (e.g. plain `AGENTS.md`) without its prefix (see `evolver.agent.md` § General Rules → Full path references)

### Step 3 — Report

```
### Errors (must fix)
| # | Check | File | Issue |
|---|-------|------|-------|

### Warnings (should fix)
| # | Check | File | Issue |
|---|-------|------|-------|
```

If none: state "All checks passed." Propose a concrete fix per violation. Apply changes only after approval (Write gate).
