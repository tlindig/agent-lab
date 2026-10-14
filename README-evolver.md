# Evolver Agent

Creates, analyzes, and optimizes agents. The agent to work on (the Target Agent) usually lives in another project; the Evolver Agent joins that project via a multi-root workspace (see [README.md](README.md#where-created-agents-live)). It maintains the Target Agent's `AGENTS.md`, `.agents/` definition, and its skills/guides/templates.

The agent is tool-agnostic: the rules live in `.agents/evolver.agent.md` and work with any AI tool that supports file context.

---

## Using the Agent

**VS Code Copilot:** Select **Evolver Agent** from the agent picker.

**Typical inputs:**

- _"Add a new agent for X"_ — scaffolds a canonical `.agents/<slug>.agent.md`, a discovery symlink, and a `README-<slug>.md`
- _"Check the ollama agent's files for rule violations"_ — validates a Target Agent against fixed structural rules (completeness, language, required sections)
- _"Rename the coding agent to review"_ — renames its files, symlink, headings, and references to the new slug
- _"Apply the open LEARNINGS.md entries"_ — integrates open learnings into the affected agent files
- _"Align the AGENTS.md of the ollama project with the baseline"_ — compares it with this repo's baseline and applies confirmed differences, keeping deliberate deviations
- _"Review/optimize the coding agent"_ — analyzes an agent's files for redundancy, contradictions, or missing structure
