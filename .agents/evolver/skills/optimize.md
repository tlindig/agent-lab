# Skill: Optimize

## Procedure

Run `validate.md` first — optimize assumes the Target Agent already passes validation; fix violations there, not here.

Placeholders: `<project_root>/.agents/evolver.agent.md` § Target Agent.

Read every file for this Target Agent (see `validate.md` Step 1's File Map) before Pass 1.

Run the passes below in order. For each pass: analyze, present findings, wait for confirmation, apply confirmed changes, then proceed to the next pass so it sees the corrected state.

### Pass 1 — Structural Integrity (baseline)

- **Missing references:** a file the Target Agent needs but that is not reliably loaded. `validate.md` checks the `INDEX.md` coverage.
- **Dead content:** a file, section, or procedure step never reached under any load condition. Remove it, or relocate it to where it becomes reachable.
- **Circular references:** trace reference chains; resolve by establishing a clear dependency direction.
- **Placeholder inconsistency:** `<target-slug>`, `<target-project_root>`, `<Target Agent Name>` vs. template fill-in placeholders (`<...>` scaffolding) — keep the two placeholder systems distinct.

### Pass 2 — Correctness

- **Contradictions:** conflicting instructions between files; converge on one referenced location and apply the fix there.
- **Outdated content:** formulations no longer accurate.
- **Robustness gaps:** a known tool quirk (see `<target-project_root>/AGENTS.md` § VS Code Tool Notes) or write-operation failure mode without a verification step.

### Pass 3 — Redundancy

Redundancy can point in different directions — resolve toward the authoritative source:

- Repeated within the Target Agent's own files (`.agent.md` vs. a skill/guide) → determine the authoritative source, others reference it.
- Repeated across multiple agents → move it to `<target-project_root>/AGENTS.md`, **except** the "Session Start (mandatory)" block: it is intentionally repeated in every `.agent.md`, because passively loaded context is often not actively applied — the entry-point copy is what enforces it.
- Repeated across multiple skills of the Target Agent → extract into a guide, referenced by each skill.
- **Paraphrase duplication:** the same fact stated in different wording in two places is still a duplicate — check meaning, not just string match.
- **Structural redundancy:** a summary that fully restates an always-co-loaded artifact has no standalone value — remove it, keep the actual source.
- **Executor restating criteria:** when a skill executes checks defined elsewhere, verify each step is a pointer, not a restatement of that content.
- **Repeated fixes/rules justified as separate occurrences by surface wording alone:** write out each trigger condition explicitly; if they match, consolidate into one general rule.

### Pass 4 — Economy

- **Unnecessary verbosity** — for each passage, ask: would removing it cause a mistake? Check against `<project_root>/.agents/evolver.agent.md` § Writing Style.
- **Over-emphasis:** more than one or two emphasized rules (bold, "IMPORTANT") in one file. Keep emphasis sparse.
- **Negative phrasing** — check against `<project_root>/.agents/evolver.agent.md` § General Rules → Write rules as positive instructions.
- **Extraction candidates** per "When to Extract Skills/Guides/Templates" in `<project_root>/.agents/evolver.agent.md`.
- **Structure vs. precision trade-off:** only shorten if the Target Agent can still act correctly from the reduced form; prefer lookup tables over prose for parameter mappings.

### Pass 5 — Re-validation

Skip this pass if Passes 1–4 applied no change. Otherwise re-run Pass 1's checks — confirm Passes 2–4 did not break a reference, orphan a file, or reintroduce a placeholder inconsistency — then run `validate.md` on the Target Agent.
