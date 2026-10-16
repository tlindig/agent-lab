# Skill: Create Agent

## Procedure

Placeholders: `<project_root>/.agents/evolver.agent.md` § Target Agent.

1. Ask for slug, display name, purpose, domain and workflow, tools, `<target-project_root>`, and external systems the agent needs (Jira, Git, APIs, web search) with their MCP tools or workspace setup. Clarify open questions before confirming; confirm before writing.
2. If `<target-project_root>/AGENTS.md` does not exist: ask whether to create it as a full copy of `<project_root>/AGENTS.md` or a trimmed version for this project; create it accordingly on confirmation.
3. If `<target-project_root>/LEARNINGS.md` does not exist: create it from `<project_root>/LEARNINGS.md`. Copy only the title and the entry-format comment (through `-->`), never entries.
4. Create the canonical file from `<project_root>/.agents/evolver/templates/agent.template.md`: `<target-project_root>/.agents/<target-slug>.agent.md`
5. Create the symlink for VS Code discovery: `mkdir -p <target-project_root>/.github/agents && ln -s ../../.agents/<target-slug>.agent.md <target-project_root>/.github/agents/<target-slug>.agent.md`
6. Create `<target-project_root>/README-<target-slug>.md` from `<project_root>/.agents/evolver/templates/README.template.md`
7. Add skills, guides, and templates with `extend-agent.md` once needed
8. If `<target-project_root>/README.md` lists agents, add the new agent to its agent table and project structure.
