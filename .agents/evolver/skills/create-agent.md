# Skill: Create Agent

## Procedure

Placeholders: `<project_root>/.agents/evolver.agent.md` § Target Agent.

1. Ask for slug, display name, purpose, tools, and `<target-project_root>`; confirm before writing.
2. If `<target-project_root>/AGENTS.md` does not exist: ask whether to create it as a full copy of `<project_root>/AGENTS.md` or a trimmed version for this project; create it accordingly on confirmation.
3. Create the canonical file from `<project_root>/.agents/evolver/templates/agent.template.md`: `<target-project_root>/.agents/<target-slug>.agent.md`
4. Create the symlink for VS Code discovery: `mkdir -p <target-project_root>/.github/agents && ln -s ../../.agents/<target-slug>.agent.md <target-project_root>/.github/agents/<target-slug>.agent.md`
5. Create `<target-project_root>/README-<target-slug>.md` from `<project_root>/.agents/evolver/templates/README.template.md`
6. Add `<target-project_root>/.agents/<target-slug>/skills|guides|templates/INDEX.md` from `<project_root>/.agents/evolver/templates/index.template.md` once needed
