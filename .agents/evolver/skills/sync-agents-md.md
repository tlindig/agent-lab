# Skill: Sync AGENTS.md

## Procedure

Compare `<target-project_root>/AGENTS.md` with `<project_root>/AGENTS.md` (the reference AGENTS.md), in both directions, while preserving deliberate deviations.

### Step 1 — Diff

Compare the two files section by section (same heading). Skip `## Repository Structure`: it describes each project's own layout, and `validate.md` checks it. Check wording, not just structure — a paraphrase of the same rule is not a difference (see `optimize.md` Pass 3, paraphrase check).

### Step 2 — Check the registry

Read the target's `## Project Deviations` section, if present (table: `Section | Reason`). A diff whose section is listed there is a preserved deviation — skip it.

### Step 3 — Classify remaining differences

For each remaining diff:

- Reference-only content, or reference wording newer than the target's: propose adopting the reference version.
- Target-only content, or target wording with no registry entry: suggest one of two classifications from context: improvement (candidate for the reference) or deliberate deviation (registry row), e.g. project-specific contact data or an existing language choice. Confirm the suggestion with the user before applying it.
- Both sides differ and neither is clearly newer: ask the user which wording applies.

### Step 4 — Report

Table: `# | Section | Reference | Target | Classification | Proposed Action`.

### Step 5 — Apply

Write gate. Add the KISS+DRY+STE check line to each proposal (see `<project_root>/.agents/evolver.agent.md` § General Rules). For a confirmed propagation: update the target section with the reference wording. For a confirmed deviation: add or keep a row in `## Project Deviations` with the confirmed reason. For a confirmed improvement: propose an entry for `<project_root>/LEARNINGS.md` (slug `evolver`, standard entry format) with project-neutral wording.
