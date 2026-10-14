# Skill: Validate

## Procedure

Placeholders: `<project_root>/.agents/evolver.agent.md` § Target Agent.

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

Each check is a pass/fail against an existing rule — not an improvement idea; severity marks how serious a failure is. Improvements to things that already pass → `optimize.md`.

**Mechanical checks** — the result follows from the file contents alone. Run them with `python <project_root>/.agents/evolver/scripts/validate.py --root <target-project_root> --slug <target-slug>` (read-only; prints the Step 3 report for these checks):

- **Completeness** (Error): `<target-project_root>/.agents/<target-slug>.agent.md` exists; `<target-project_root>/.github/agents/<target-slug>.agent.md` is a symlink to `../../.agents/<target-slug>.agent.md` (no content of its own); `<target-project_root>/README-<target-slug>.md` exists; `<target-project_root>/AGENTS.md` exists
- **Session Start** (Error): the Target Agent's `.agent.md` contains the "Session Start (mandatory)" section, matching the template verbatim, or a faithful translation per `<target-project_root>/AGENTS.md` § Communication
- **INDEX coverage** (Error, if the folder exists): every file in `<target-project_root>/.agents/<target-slug>/skills/`, `guides/`, and `templates/` is listed in that folder's `INDEX.md`, and every `INDEX.md` row names an existing file
- **Trigger form** (Warning): every row of the Skill Map in `<target-project_root>/.agents/<target-slug>/skills/INDEX.md` starts with "User asks to" or "After"; a skill that deletes or overwrites files has a "User asks to" row
- **Path resolution** (Error): every file path in backticks uses the literal `<target-project_root>/` or `<project_root>/` prefix where it points into a project root; flag a bare reference (e.g. a bare AGENTS.md) without its prefix (see `<project_root>/.agents/evolver.agent.md` § General Rules → Full path references). Exempt: the verbatim "Session Start (mandatory)" block, `<target-project_root>/README-<target-slug>.md` (user-facing), and a skill file name listed in a Skill Map (an identifier, not a path)

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
