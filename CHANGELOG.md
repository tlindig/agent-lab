# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.8.0] - 2026-10-28

### Added

- `optimize.md` Pass 2 checks the order and the catch-all branch of condition lists; `apply-learnings.md` and `sync-agents-md.md` follow it.
- `AGENTS.md` § Failed Attempts: after two failed attempts the agent changes the approach once, then stops and reports to the caller.
- `validate.md`: the File Map lists `.agents/<target-slug>/scripts/`.

### Changed

- `AGENTS.md` § Learnings: a finding takes the first matching branch (rule not followed → RERULE; rule ambiguous → reword; no rule → filter unexpected, preventable, relevant; otherwise analyze and ask).
- `AGENTS.md` invariant: every recommendation and warning needs a factual reason. Options gate: options use letters on the first and numbers on a nested second level; the recommended option carries `**(+)**`, each option to avoid `(-)`, and equal options stay unmarked.
- `AGENTS.md` Action gate: destructive actions are asked in a question that lists each action and nothing else; the agent does not delete files and asks to move a file to the trash with `gio trash`; the user deletes permanently.
- `validate.md`: Session Start accepts a silent RERULE for an agent with `user-invocable: false`; user-facing agents keep the blocking form.
- `optimize.md` Pass 1: dead content is relocated first and removed only if no load condition fits.

## [0.7.0] - 2026-10-20

### Added

- `validate.md`: Structure match check compares a Target Agent's files with the `## Repository Structure` table of its `AGENTS.md`.
- `validate.md`: Tool names check verifies that tools and parameters named in `AGENTS.md` § VS Code Tool Notes exist in the harness or are gated by a setting.
- `AGENTS.md` invariant: read a referenced file with a tool call before reporting it as applied or checked.

### Changed

- `AGENTS.md` Options gate: options follow the pattern `[id]. [option] — [reason]`; the recommended one starts with `**Recommended:**`.
- `AGENTS.md` § VS Code Tool Notes: `includeIgnoredFiles` needs a narrow `includePattern`; Post-write verification also checks markup structure and table line lengths; shorter `replace_string_in_file` note. The Repository Structure table no longer refers to the Evolver.
- `sync-agents-md.md` skips `## Repository Structure`; skills and `README-evolver.md` name `<project_root>/AGENTS.md` by path instead of "baseline".

## [0.6.0] - 2026-10-18

### Added

- Cross-agent `.agents/shared/` level (`guides/`, `templates/`, `scripts/`) with a criterion for when content belongs there; `extend-agent.md` asks who uses the content; `validate.md` warns about a shared file that fewer than two agents use.
- Evolver checks: skill files over 500 lines are split; `optimize.md` flags steps that list several equal alternatives without a default.
- `apply-learnings.md` routes a skill candidate to `extend-agent.md`.

### Changed

- `validate.md`: mechanical checks determine results by tool or count; Completeness verifies the discovery symlink target (`readlink -f`); a skill file holds the Action only.
- Evolver rules tightened: Action/Trigger separation names its failure mode; redundant pointers, back-references, and negations removed; Skill Map rows give a one-line purpose; the `evolver.agent.md` description and Responsibilities cover renaming, `README-<target-slug>.md`, `LEARNINGS.md`, and `shared/`.
- `sync-agents-md.md`: dropped an opening sentence that contradicted Step 5.
- `optimize.md` Pass 3 moves only repeated rules to `AGENTS.md`.
- `LEARNINGS.md`: the entry-format comment allows a source finding in `Observed`.

## [0.5.0] - 2026-10-16

### Added

- `extend-agent.md`: adds a skill, guide, or template to a Target Agent and registers it in the folder's `INDEX.md`.

### Changed

- `apply-learnings.md` clusters entries by root problem, classifies scope, and routes generic fixes to the target's `AGENTS.md`.
- `sync-agents-md.md` compares both directions; target-only improvements become baseline candidates.
- `create-agent.md` asks for domain, workflow, and external systems; adds the agent to the target's `README.md`.
- `AGENTS.md`: Write gate self-correction exception; invariant to track open self-asked questions; Options gate checks for "or"; KISS and DRY sections; "Post-write verification" with a separate read; deletion via `rm`; template notation in Placeholder Conventions.
- `validate.md` Folder roles: guides state requirements on artifacts, not instructions. `optimize.md` presents each finding as a Write-gate proposal. The reference search covers plain names and path forms.

## [0.4.0] - 2026-10-15

### Added

- `create-agent.md` creates a missing `LEARNINGS.md`; `validate.md` checks it exists.

### Changed

- `LEARNINGS.md` entry-format comment (`Observed` / `Expected` / `Improvement`); `apply-learnings.md` reads the target project's file.
- `AGENTS.md`: tool-agnostic RERULE read step; Tool Use rule (shell only when no tool applies); the Action gate requires the concrete result an action should deliver; corrected hidden-directory note.
- `validate.md`: Session Start applies only if the target's `AGENTS.md` defines a RERULE gate; Trigger form became Skill index form; Path resolution exempts template names and generic file names.
- Skill Map rows describe a skill by purpose; skills that only other skills invoke are marked Internal.
- Validation Discipline: reference search before removing or renaming a section, heading, or file. `optimize.md` Pass 4 verbosity check covers every passage.
- `.gitignore` ignores `*.code-workspace`.

### Removed

- `scripts/validate.py`: mechanical checks run by reading the files.

## [0.3.0] - 2026-10-15

### Added

- Skills `create-agent.md` (extracted from `evolver.agent.md`) and `rename-agent.md`.
- `scripts/validate.py` (removed in 0.4.0); `validate.md` checks INDEX coverage and Trigger form.
- `AGENTS.md` VS Code Tool Notes "File writes": use the editor tools so the VS Code diff and undo stay intact.
- `README.md`: rationale for root-prefixed paths.

### Changed

- Evolver role: creates, analyzes, and optimizes a Target Agent that usually lives in another project; "Switching TargetAgent" replaces "one Target Agent per run"; full root-prefixed paths.
- Validation Discipline: every proposal is checked against `validate.md` and KISS+DRY+STE before presentation, using freshly read files.
- `validate.md`: mechanical and review checks; one Folder roles check; Language honors a user-requested language.
- `optimize.md` Pass 5 runs only after changes and ends with `validate.md`. `apply-learnings.md` processes only the Target Agent's slug.

### Removed

- `validate.md` checks Skill file structure, Duplication, Explicit invocation, and Placeholder conventions (covered by the DRY check, `optimize.md`, and Trigger form).
- Redundant sections in `evolver.agent.md` (Syncing AGENTS.md, Applying Learnings, Show-to-user check, Verify before reporting).

## [0.2.0] - 2026-10-14

### Added

- RERULE violation trigger offers a choice (RERULE / root-cause analysis + log / handoff prompt).
- Invariant: numeric values by calculation or tool, quality indicators confirmed by a second method.
- VS Code Tool Notes "Verify after write".
- `sync-agents-md.md`: aligns a Target Agent's `AGENTS.md` with the baseline and keeps deliberate deviations in a `## Project Deviations` registry.
- `evolver.agent.md` creates a missing target `AGENTS.md`; `validate.md` checks it exists.

### Changed

- Options gate: numbered or lettered list, each option with a recommendation, closed with the option identifier. Action gate: action and reason as visible chat text.

### Fixed

- `validate.md` Language and Session Start checks reference `<target-project_root>/AGENTS.md`; Session Start accepts a faithful translation.

## [0.1.0] - 2026-10-12

### Added

- Open-source project files: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue/PR templates, `.gitignore`.
- Quick Start section in `README.md`.
