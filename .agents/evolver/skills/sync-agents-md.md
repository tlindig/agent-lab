# Skill: Sync AGENTS.md

## Procedure

Compare `<target-project_root>/AGENTS.md` with this repo's baseline, `<project_root>/AGENTS.md`, in both directions, while preserving deliberate deviations. Write only to the target. Placeholders: `<project_root>/.agents/evolver.agent.md` § Target Agent.

### Step 1 — Diff

Compare the two files section by section (same heading). Check wording, not just structure — a paraphrase of the same rule is not a difference (see `optimize.md` Pass 3, paraphrase check).

### Step 2 — Check the registry

Read the target's `## Project Deviations` section, if present (table: `Section | Reason`). A diff whose section is listed there is a preserved deviation — skip it.

### Step 3 — Classify remaining differences

For each remaining diff:

- Baseline-only content, or baseline wording newer than the target's: propose adopting the baseline version.
- Target-only content, or target wording with no registry entry: suggest one of two classifications from context: improvement (baseline candidate) or deliberate deviation (registry row), e.g. project-specific contact data or an existing language choice. Confirm the suggestion with the user before applying it.

### Step 4 — Report

Table: `# | Section | Baseline | Target | Classification | Proposed Action`.

### Step 5 — Apply

Write gate. For a confirmed propagation: update the target section with the baseline wording. For a confirmed deviation: add or keep a row in `## Project Deviations` with the confirmed reason. For a confirmed improvement: propose an entry for `<project_root>/LEARNINGS.md` (slug `evolver`, standard entry format) with project-neutral wording.
