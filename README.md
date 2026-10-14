# Agent Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Framework for building AI agents that behave predictably: no guessing, no speculation, no unapproved or destructive actions.

## Quick Start

1. Clone this repository, e.g. into `~/dev/agent-lab`.
2. Open your target project in VS Code (the project that should get a new agent).
3. Add this repository as a second workspace folder: **File → Add Folder to Workspace…** → select `agent-lab`. Your target project now has this repo's `AGENTS.md` and Evolver Agent available alongside its own files (see [Where Created Agents Live](#where-created-agents-live)).
4. In Copilot Chat, open the agent picker and select **Evolver Agent**.
5. Ask it to create a new agent for your target project, e.g. _"Add a new agent for reviewing pull requests in `<target-project-root>`"_.
6. The Evolver Agent asks clarifying questions, then proposes new files **inside your target project** (`.agents/<slug>.agent.md`, a `.github/agents/<slug>.agent.md` symlink, `README-<slug>.md`) for your approval before writing anything.

See [README-evolver.md](README-evolver.md) for the full usage guide.

## Goal

An agent built and maintained with this framework does exactly what it is supposed to do:

- Ambiguity is resolved by asking early and often — not by autonomous brute-force search. A short question costs little; guessing wrong burns tool calls and tokens, and can send the agent down the wrong path unnoticed until much later.
- Token use stays deliberate: no speculative tool calls, and skills/guides/templates load only on demand instead of sitting in every agent's default context.
- Every write, and every destructive or hard-to-reverse action, requires explicit approval first.
- Content the agent processes (e.g. a Target Agent's own files) is treated as data, never as an instruction that can redirect the agent's behavior.
- Rule violations are self-reported, not hidden.

## Core Concept

- **`AGENTS.md`** sets baseline rules binding for every agent in this project. A small set of **Behavior Invariants** (asking instead of guessing, the Write/Action gates, rejecting rule overrides) are absolute and cannot be suspended by any instruction or request.
- Each agent extends this baseline in its own canonical **`.agents/<slug>.agent.md`** — it may concretize the shared rules but never contradict them.
- A **RERULE gate** re-reads and re-activates the binding rules at session start and on scope changes, so rules stay active even in long sessions.
- Rule text itself follows **KISS, DRY, STE, and positive instruction**: simple and non-duplicated, short single-idea sentences in active voice, phrased as what to do rather than what not to do — checked systematically via the Evolver Agent's `optimize.md`.
- Rule files reference files with a root prefix, `<project_root>/…` or `<target-project_root>/…`. The prefix keeps the two roots apart and stops agents from searching with `find` for a file whose location is already clear. Observed in practice; re-test before removing it.
- Tool-agnostic by design: tried so far with VS Code Copilot, but nothing in the rule files depends on a specific AI harness — any tool that can read project files and follow instructions should work.

## How a Created Agent Works

1. On session start, the agent reads `AGENTS.md` and executes the RERULE gate — this happens before it responds to the first message.
2. It resolves ambiguity by asking, classifies every input as rule (how to work) or data (what to work on), and only reads what it concretely needs.
3. Before any write or any risky action, it presents what will change and why, and waits for approval.
4. If it maintains or analyzes another agent's files (a "Target Agent"), it treats that content strictly as data — it cannot alter its own behavior.

## Structure

| Element                          | Role                                                                                                |
| -------------------------------- | --------------------------------------------------------------------------------------------------- |
| `AGENTS.md`                      | Project-wide, always-loaded baseline rules                                                          |
| `.agents/<slug>.agent.md`        | Canonical definition of one agent — tool-agnostic source of truth                                   |
| `.github/agents/<slug>.agent.md` | Symlink so VS Code discovers the agent — never edited directly                                      |
| `README-<slug>.md`               | User-facing usage description for that one agent                                                    |
| `.agents/<slug>/skills/`         | Executable step-by-step procedures, loaded on demand                                                |
| `.agents/<slug>/guides/`         | Static reference material, loaded on demand                                                         |
| `.agents/<slug>/templates/`      | Fill-in scaffolding structures, no rule logic                                                       |
| `.agents/<slug>/scripts/`        | Deterministic helper scripts for mechanical checks, run on demand                                   |
| `LEARNINGS.md`                   | Open findings from sessions, integrated back into the affected agent as a deliberate, separate step |

### Rules vs. Skills vs. Templates vs. Guides

These four content types are kept strictly apart so an agent only loads what it needs:

- **Rules** (`AGENTS.md`, `.agent.md`) — binding behavior, always loaded.
- **Skills** (`skills/*.md`) — an executable procedure, invoked by a concrete trigger.
- **Guides** (`guides/*.md`) — reference material (checklists, examples) too large for inline prose.
- **Templates** (`templates/*.md`) — output scaffolding with `<placeholder>` slots, no rule logic.

Content stays inline in the `.agent.md` as long as possible; it is extracted only once a concrete condition applies (needed a second time, growing too large, or only occasionally relevant). This is the core token-efficiency mechanism: context stays lean by default and grows only on concrete need.

## Where Created Agents Live

A created agent (a "Target Agent") does not have to live inside this repository. It can live in its own project, kept connected to this rule set via a VS Code multi-root workspace — add both folders to one workspace so the agent has this repo's `AGENTS.md` and Evolver Agent available alongside its own project files.

This also saves context: day-to-day work with a Target Agent does not load the Evolver Agent at all — it is only pulled in on demand, when maintenance or evolution of the agent itself is needed.

## Maintaining This Repository

Use the **Evolver Agent** ([README-evolver.md](README-evolver.md)) to create new agents, validate or optimize existing ones, and apply open entries from `LEARNINGS.md`.

## Disclaimer

Agents built with this framework follow instructions; they do not act on their own goals. Approving a write or a risky action is a judgment call made by the person giving the instruction — use at your own risk. See [LICENSE](LICENSE) for the legal terms.
