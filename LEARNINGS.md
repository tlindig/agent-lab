# Agent Learnings

<!-- Entry format:
## [YYYY-MM-DD] / [<slug>] — [Short title]

**Observed:** [What happened — concrete situation or mistake.]
**Expected:** [What the correct behavior is and why.]
**Improvement:** [Specific rule or procedure change to apply.]
-->

## [2026-10-25] / [evolver] — Shell commands drafted inside Markdown table cells

**Observed:** A Mission Contract draft listed gate commands in a table and escaped `|` as `\|`. A copied command would run `grep -E 'a\|b'` (literal pipe) and a broken `node -e`. The post-write check found it and the table was replaced by a list.
**Expected:** A command that an agent copies and runs stays free of Markdown escapes.
**Improvement:** Apply once a guide or template for the Mission Contract exists in the Orchestrator's project (`Dev/ai-agents`): it requires each command in a list item or code block, never in a table cell. Until then, keep this entry open. Do not add the rule to `<project_root>/.agents/evolver.agent.md` or `<project_root>/.agents/evolver/skills/validate.md`: one incident, post-write verification caught it, and `missions/` is outside the validate File Map.
