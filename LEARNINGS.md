# Agent Learnings

<!-- Entry format:
## [YYYY-MM-DD] / [<slug>] — [Short title]

**Observed:** [What happened — concrete situation or mistake.]
**Expected:** [What the correct behavior is and why.]
**Improvement:** [Specific rule or procedure change to apply.]
-->

## 2026-11-16 / evolver — State that editor tools cannot delete files

**Observed:** A target project's `AGENTS.md` adds "No editor tool deletes files." to its `File writes` note. The reference `AGENTS.md` lacks it. Without it, an agent can search for a delete tool or fall back to a shell delete.
**Expected:** The tool note states the capability limit. Deleting stays with the user, as the Action gate defines.
**Improvement:** Append "No editor tool deletes files." to the `File writes` bullet in `## VS Code Tool Notes` of `<project_root>/AGENTS.md`. Do not repeat the trash rule there; the Action gate defines it.

## 2026-11-16 / evolver — Add a fallback for `fetch_webpage` without usable content

**Observed:** A target project's `AGENTS.md` has a `VS Code Tool Notes` bullet for `fetch_webpage` returning no usable content. The reference `AGENTS.md` lacks it. Without it, an agent can stop at the empty result or guess the page content.
**Expected:** The agent follows a fixed fallback order. It states the Action gate, opens the URL in the integrated browser, and filters the saved snapshot with a read-only terminal command. It asks the user to read the page externally only if the integrated browser is rejected.
**Improvement:** Add a bullet `**`fetch_webpage` without usable content:**` to `## VS Code Tool Notes` of `<project_root>/AGENTS.md`. Use the target project's wording: "State the Action gate and open the URL in the integrated browser, then filter the saved snapshot with a read-only terminal command (`grep_search` does not see files outside the workspace). Ask the user to read the page in an external browser only if the site rejects the integrated browser." Verify first that the snapshot mechanism applies in the current harness.


## 2026-10-20 / evolver — Shared project-knowledge skill concept

**Observed:** Project information is distributed across topic notes, decisions, ticket lists, glossaries, and operational references. Maintenance is inconsistent and the recorded status is not reliably current.
**Expected:** Agents and team members can find source-backed project knowledge, distinguish approved decisions from assumptions, and recognize stale or conflicting information without creating a competing authority for live Jira or runtime state.
**Improvement:** Use [the shared project-knowledge skill concept](topics/project-knowledge/skill-concept.md) as the implementation brief for a dedicated Evolver run. It documents explicit activation, policy and approval requirements, source provenance, maintenance workflows, acceptance scenarios, and external sources including Agent Skills and the LLM Wiki concept. Resolve its open decisions before implementation; this entry does not authorize skill creation, rule changes, tooling installation, or content migration.

## 2026-11-17 / evolver — After a tool or MCP update, document only current behavior

**Observed:** After an MCP server update (mcp-atlassian v0.23.1 → v0.24.6), the draft for the Target Agent's rules corrected old statements and kept notes on earlier versions and earlier workarounds. The user had to ask twice to cut them.
**Expected:** The rules describe only the current, unexpected behavior of the tool and, where needed, a workaround that avoids the error. A statement for an older version, and a workaround for an earlier workaround, are deleted without replacement and without a note on the earlier state.
**Improvement:** In `<project_root>/.agents/evolver/skills/apply-learnings.md`, Step 4.2 (Independent analysis), add: "For an entry about a tool or MCP update, keep only the current unexpected behavior and a workaround that avoids the error. Delete statements for older versions and earlier workarounds without replacement." Via Evolver run.

## 2026-11-17 / evolver — "Shared use" check flags a file that `AGENTS.md` references

**Observed:** A guide and two scripts below `.agents/shared/` were referenced only from the Target project's `AGENTS.md`. The "Shared use" check reported a Warning, because it counts only `.agent.md` files and `.agents/<slug>/` files. `AGENTS.md` binds every agent, so the location was correct. The Warning was wrong.
**Expected:** A file that `AGENTS.md` references counts as referenced by every agent. A file with such a reference belongs in `.agents/shared/`. The check reports no Warning for it.
**Improvement:** In `<project_root>/.agents/evolver/skills/validate.md`, check "Shared use": add "A reference in `<target-project_root>/AGENTS.md` counts as a reference by every agent." Via Evolver run.

