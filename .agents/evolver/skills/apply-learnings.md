# Skill: Apply Learnings

## Procedure

1. Read `<target-project_root>/LEARNINGS.md`. List the open entries for the Target Agent (slug in the heading). Skip other slugs. If none exist, stop.
2. Classify the scope of each entry. The heading slug names where the incident happened, not where the fix belongs. Take the first bullet that matches.
   - Skill candidate (a procedure to extract) → `extend-agent.md`.
   - Generic tool or infrastructure concern → `<target-project_root>/AGENTS.md`. Read it and `<project_root>/AGENTS.md` first. If only `<project_root>/AGENTS.md` holds the rule, the fix is a sync (`sync-agents-md.md`), not a new rule.
   - Problem specific to the Target Agent's domain → `<target-project_root>/.agents/<target-slug>.agent.md` and its skills, guides, templates.
   - Otherwise → ask the user where the fix belongs.
3. Cluster the entries by root problem and affected files. Present the clusters with rationale. Wait for confirmation.
4. For each cluster, in confirmed order:
   1. **Verify currency** — check by test or grep whether the problem still occurs. State the finding.
   2. **Independent analysis** — derive root cause and fix from `Observed` and `Expected` only. Read `Improvement` after the independent solution is settled.
      - Check the scope: only the named file, or a broader class of files?
      - Check the Target Agent's existing patterns for the same concern. Reference existing content instead of repeating it.
      - Choose the authoritative location (`optimize.md` redundancy principle).
      - If several fixes are viable, weigh pros and cons and recommend one.
      - For a fix in `<project_root>/AGENTS.md`, check that the wording is project-neutral.
      - Compare the result with `Improvement`. Note agreement or deviation.
      - If the fix needs an unstated assumption or contradicts an existing pattern, ask the user.
   3. **Reference search** — run the reference search of `<project_root>/.agents/evolver.agent.md` § Validation Discipline for every changed concept, not only for removals and renames.
   4. **Write gate** — per file, present what changes, why, the scope reasoning, the hits of the reference search, and each deviation from `Improvement`. List the entries to delete. Wait for approval.
   5. Apply the changes. Delete each integrated entry block entirely from `<target-project_root>/LEARNINGS.md`.
   6. Run the post-write steps of § Validation Discipline on the Target Agent.
   7. **Improvement for `<project_root>/AGENTS.md`** — if the fix went into `<target-project_root>/AGENTS.md`, `<target-project_root>` differs from `<project_root>`, and the rule is not specific to the target project, propose an entry as in `sync-agents-md.md` Step 5.
   8. Confirm completion. Continue with the next cluster.
