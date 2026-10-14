# Changelog

All notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
