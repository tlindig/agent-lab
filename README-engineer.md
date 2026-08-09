# Engineer Agent

Maintains and evolves the agent infrastructure of this project (`Dev/ai-agent`): `AGENTS.md`, the `.agents/` agent definitions, and their skills/guides/templates.

The agent is tool-agnostic: the rules live in `.agents/engineer.agent.md` and work with any AI tool that supports file context.

---

## Using the Agent

**VS Code Copilot:** Select **Engineer** from the agent picker.

**Typical inputs:**

- _"Add a new agent for X"_ — scaffolds a canonical `.agents/<slug>.agent.md`, a discovery symlink, and a `README-<slug>.md`
- _"Check the ollama agent's files for rule violations"_ — validates a Target Agent against fixed structural rules (completeness, language, required sections)
- _"Apply the open LEARNINGS.md entries"_ — integrates open learnings into the affected agent files
- _"Review/optimize the coding agent"_ — analyzes an agent's files for redundancy, contradictions, or missing structure
