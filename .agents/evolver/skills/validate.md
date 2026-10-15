# Skill: Validate

## Procedure

Placeholders: `<project_root>/.agents/evolver.agent.md` § Target Agent.

### Step 1 — Build the File Map

Table `File | Load condition | Present`:

- `<target-project_root>/AGENTS.md` — always
- `<target-project_root>/.agents/<target-slug>.agent.md` — always
- `<target-project_root>/.github/agents/<target-slug>.agent.md` — always (symlink)
- `<target-project_root>/README-<target-slug>.md` — always
- `<target-project_root>/LEARNINGS.md` — always
- `<target-project_root>/.agents/<target-slug>/skills/INDEX.md`, `skills/<skill>.md` — if present
- `<target-project_root>/.agents/<target-slug>/guides/INDEX.md`, `guides/<guide>.md` — if present
- `<target-project_root>/.agents/<target-slug>/templates/INDEX.md`, `templates/<template>.md` — if present

### Step 2 — Check Rules

Each check is a pass/fail against an existing rule — not an improvement idea; severity marks how serious a failure is. Improvements to things that already pass → `optimize.md`.

**Mechanical checks** — the result follows from the file contents alone. Count and compare; do not estimate:

- **Completeness** (Error): `<target-project_root>/.agents/<target-slug>.agent.md`, `<target-project_root>/.github/agents/<target-slug>.agent.md`, `<target-project_root>/README-<target-slug>.md`, `<target-project_root>/AGENTS.md`, and `<target-project_root>/LEARNINGS.md` exist
- **Session Start** (Error, only if `<target-project_root>/AGENTS.md` defines a RERULE gate): the Target Agent's `.agent.md` contains a "Session Start (mandatory)" section. Its first step executes that RERULE gate and blocks until the user confirms. The wording is free.
- **INDEX coverage** (Error, if the folder exists): every file in `<target-project_root>/.agents/<target-slug>/skills/`, `guides/`, and `templates/` is listed in that folder's `INDEX.md`, and every `INDEX.md` row names an existing file
- **Skill index form** (Warning): every skill in `<target-project_root>/.agents/<target-slug>/skills/INDEX.md` has a one-line purpose. A skill that only other skills or rules invoke is marked "Internal". A skill that deletes or overwrites files is not marked "Internal". The INDEX states once when to run a skill. Skill files hold no activation conditions.
- **Path resolution** (Error): every file path in backticks uses the literal `<target-project_root>/` or `<project_root>/` prefix where it points into a project root; flag a bare reference (e.g. a bare AGENTS.md) without its prefix (see `<project_root>/.agents/evolver.agent.md` § General Rules → Full path references). Exempt: the "Session Start (mandatory)" block, `<target-project_root>/README-<target-slug>.md` (user-facing), a skill or template file name listed in a Skill Map or Template Map, and a generic file name that points to no specific file (identifiers, not paths)

**Review checks** — the result needs the agent's judgment:

- **Language** (Warning): `<target-project_root>/.agents/<target-slug>.agent.md`, `<target-project_root>/README-<target-slug>.md`, and every file below `<target-project_root>/.agents/<target-slug>/` are English, per `<target-project_root>/AGENTS.md` § Communication, unless the user requested another language for that file
- **README scope** (Warning): `<target-project_root>/README-<target-slug>.md` stays user-facing — purpose and usage only; no internal rules, decision logic, or process steps
- **Folder roles** (Warning, per existing folder): `INDEX.md` has a routing table and no rule logic; skills hold executable steps, not reference material; guides hold reference material only — no activation logic, procedure steps, or behavioral rules; templates use `<...>` placeholders and no rule logic

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
