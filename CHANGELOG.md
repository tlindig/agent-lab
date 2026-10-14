# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Skills `create-agent.md` (extracted from `evolver.agent.md`) and `rename-agent.md`.
- `scripts/validate.py`: runs the mechanical `validate.md` checks read-only; `scripts/` added to the repository structure in `AGENTS.md` and `README.md`.
- `validate.md`: checks INDEX coverage and Trigger form.
- `AGENTS.md` VS Code Tool Notes: "File writes" — use the editor tools, not shell writes, so the VS Code diff and undo stay intact.
- `README.md`: rationale for root-prefixed paths.

### Changed

- Evolver role: creates, analyzes, and optimizes a Target Agent that usually lives in another project (`evolver.agent.md`, `README-evolver.md`).
- Validation Discipline: every proposal is checked before presentation against `validate.md` and KISS+DRY+STE, using freshly read files; mechanical checks run after writing.
- `validate.md`: checks grouped into mechanical and review; Language covers all agent files and honors a user-requested language; one Folder roles check replaces the INDEX, Guides, and Templates role checks.
- `optimize.md`: Pass 5 runs only when changes were applied and ends with `validate.md`.
- `apply-learnings.md`: processes only entries for the Target Agent's slug.
- `index.template.md`: the first column is Condition, Topic, or Output by type; `agent.template.md` has no intro sentence.
- `evolver.agent.md`: full root-prefixed paths; "Switching TargetAgent" replaces "one Target Agent per run".

### Removed

- `validate.md` checks Skill file structure (`## Procedure`), Duplication, Explicit invocation, and Placeholder conventions; their purpose is covered by the DRY check, `optimize.md`, and Trigger form.
- Redundant sections in `evolver.agent.md`: Syncing AGENTS.md, Applying Learnings, Show-to-user check, Verify before reporting.

## [0.2.0] - 2026-10-14

### Added

- RERULE rule-violation trigger now offers a choice (RERULE / root-cause analysis + log / handoff prompt) instead of always executing RERULE.
- Numeric-value invariant: determine by calculation or tool, confirm quality indicators with a second independent method.
- VS Code Tool Notes: "Verify after write" guidance.
- `evolver.agent.md`: "Creating a New Agent" now creates a missing `<target-project_root>/AGENTS.md` (full copy or trimmed, by confirmation) from this repo's baseline.
- New "Syncing AGENTS.md Across Target Projects" section and `sync-agents-md.md` skill: align a Target Agent's `AGENTS.md` with this repo's baseline while preserving deliberate deviations via a `## Project Deviations` registry.
- `validate.md`: Completeness check for `<target-project_root>/AGENTS.md` existence.

### Changed

- Options gate: alternatives must be a numbered/lettered list, each with a recommendation, closed with the option identifier as the expected answer.
- Action gate: requires stating the action and reason as visible chat text (tool `explanation`/`goal` parameters are not shown to the user).

### Fixed

- `validate.md` Language and Session Start checks referenced a bare, ambiguous `AGENTS.md`; both now reference `<target-project_root>/AGENTS.md`. Session Start also accepts a faithful translation per that project's Communication rule.

## [0.1.0] - 2026-10-12

### Added

- Open-source project files: `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`, issue/PR templates, `.gitignore`.
- Quick Start section in `README.md`.
