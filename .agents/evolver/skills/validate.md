# Skill: Validate

## Procedure

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
- `<target-project_root>/.agents/<target-slug>/scripts/<script>` — if present
- `<target-project_root>/.agents/shared/guides/`, `templates/`, `scripts/` (`INDEX.md` in guides and templates) — if present

### Step 2 — Check Rules

Each check is a pass/fail against an existing rule; severity marks how serious a failure is. Improvements to things that already pass → `optimize.md`.

**Mechanical checks** — the result follows from the file contents alone. Determine each result by tool or count, then compare:

- **Completeness** (Error): `<target-project_root>/.agents/<target-slug>.agent.md`, `<target-project_root>/README-<target-slug>.md`, `<target-project_root>/AGENTS.md`, and `<target-project_root>/LEARNINGS.md` exist; `<target-project_root>/.github/agents/<target-slug>.agent.md` is a symlink that `readlink -f` resolves to `<target-project_root>/.agents/<target-slug>.agent.md`
- **Session Start** (Error, only if `<target-project_root>/AGENTS.md` defines a RERULE gate): the Target Agent's `.agent.md` contains a "Session Start (mandatory)" section. Its first step executes that RERULE gate. For a user-facing agent, the step blocks until the user confirms. For an agent with `user-invocable: false`, the step runs the gate silently as a scope change and does not wait. The wording is free.
- **INDEX coverage** (Error, if the folder exists): every file in `<target-project_root>/.agents/<target-slug>/skills/`, `guides/`, and `templates/`, and in `<target-project_root>/.agents/shared/guides/` and `templates/`, is listed in that folder's `INDEX.md`, and every `INDEX.md` row names an existing file
- **Shared use** (Warning, if `<target-project_root>/.agents/shared/` exists): every file below it is referenced by two or more agents. Count the agents whose `<target-project_root>/.agents/<slug>.agent.md` or files below `<target-project_root>/.agents/<slug>/` contain the file name (`grep`).
- **Skill index form** (Warning): every skill in `<target-project_root>/.agents/<target-slug>/skills/INDEX.md` follows `<project_root>/.agents/evolver.agent.md` § Skills. A skill file holds the Action only (see `<project_root>/.agents/evolver.agent.md` § General Rules → Action/Trigger separation).
- **Path resolution** (Error): every file path in backticks uses the literal `<target-project_root>/` or `<project_root>/` prefix where it points into a project root; flag a bare reference (e.g. a bare AGENTS.md) without its prefix (see `<project_root>/.agents/evolver.agent.md` § General Rules → Full path references). Exempt: the "Session Start (mandatory)" block, `<target-project_root>/README-<target-slug>.md` (user-facing), a skill or template file name listed in a Skill Map or Template Map, and a generic file name that points to no specific file (identifiers, not paths)

**Review checks** — the result needs the agent's judgment:

- **Language** (Warning): `<target-project_root>/.agents/<target-slug>.agent.md`, `<target-project_root>/README-<target-slug>.md`, and every file below `<target-project_root>/.agents/<target-slug>/` are English, per `<target-project_root>/AGENTS.md` § Communication, unless the user requested another language for that file
- **README scope** (Warning): `<target-project_root>/README-<target-slug>.md` stays user-facing — purpose and usage only; no internal rules, decision logic, or process steps
- **Folder roles** (Warning, per existing folder, also below `<target-project_root>/.agents/shared/`): `INDEX.md` has a routing table and no rule logic; skills hold executable steps, not reference material; guides hold reference material — they may state requirements on artifacts (what an output must contain) but hold no instructions to the agent (when to act, whom to ask, which step follows); templates follow the placeholder notation of `<target-project_root>/AGENTS.md` § Placeholder Conventions and hold no rule logic
- **Structure match** (Warning, only if `<target-project_root>/AGENTS.md` has a `## Repository Structure` table): every file and folder from the File Map that is present matches a row path, reading `<slug>` as `<target-slug>` and `<project_root>` as `<target-project_root>`
- **Tool names** (Warning, only if `<target-project_root>/AGENTS.md` has a `## VS Code Tool Notes` section): every tool or parameter that section names exists in the current harness or is gated by a named setting. Before you report a name as wrong or unverified, check the tool schema, the settings that add parameters, and the installed VS Code bundle.

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
