# Agent Lab

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Agent Lab is the meta level for AI agents. Its Evolver Agent creates, validates, and optimizes agents and lets them evolve over time.

The agents it builds are tool-agnostic by design, use few tokens, ask instead of guessing, and change nothing without approval. They improve iteratively: session findings flow back into the agents, one approved step at a time.

## Quick Start

1. Clone this repository, e.g. into `~/dev/agent-lab`.
2. Open your target project in VS Code (the project that should get a new agent).
3. Add this repository as a second workspace folder (**File → Add Folder to Workspace…**). Your project then has this repo's `AGENTS.md` and the Evolver Agent next to its own files (see [Where Created Agents Live](#where-created-agents-live)).
4. In Copilot Chat, open the agent picker and select **Evolver Agent**.
5. Ask it to create a new agent for your target project, e.g. _"Add a new agent for reviewing pull requests in `<target-project_root>`"_.
6. The Evolver Agent asks clarifying questions, then proposes new files in your target project for approval before writing anything: `.agents/<slug>.agent.md`, a `.github/agents/<slug>.agent.md` symlink, and `README-<slug>.md`, plus an entry in the project's `README.md` if it lists agents.

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
- Rule files reference files with a root prefix (`<project_root>/…`, `<target-project_root>/…`). It keeps the two roots apart and stops agents from searching for files whose location is already clear. Observed in practice; re-test before removing it.
- Tool-agnostic by design: tried so far with VS Code Copilot, but nothing in the rule files depends on a specific AI harness — any tool that can read project files and follow instructions should work.
- **Learning loop:** Agents log findings in `LEARNINGS.md` and propose improvements themselves. The Evolver Agent applies them in a separate step, cluster by cluster. Each change needs approval first. This improves agents iteratively, the Evolver Agent itself included.

## Structure

```text
<project_root>/
├── AGENTS.md                         # baseline rules, always loaded
├── LEARNINGS.md                      # open findings, applied in a separate step
├── README-<slug>.md                  # user-facing description of one agent
├── .agents/
│   ├── shared/                       # resources used by two or more agents: guides/, templates/, scripts/
│   ├── <slug>.agent.md               # canonical agent definition, tool-agnostic source of truth
│   └── <slug>/
│       ├── skills/                   # step-by-step procedures, on demand
│       ├── guides/                   # reference material, on demand
│       ├── templates/                # fill-in scaffolding, no rule logic
│       └── scripts/                  # deterministic checks, on demand
└── .github/agents/
    └── <slug>.agent.md               # symlink for VS Code discovery, never edited
```

### Keeping Context Lean

Content stays inline in the `.agent.md` as long as possible; it is extracted only once a concrete condition applies (needed a second time, growing too large, or only occasionally relevant). This is the core token-efficiency mechanism: context stays lean by default and grows only on concrete need.

## Relation to Open Standards

- **AGENTS.md:** The baseline rules use the [AGENTS.md](https://agents.md/) format, a plain-Markdown convention that many coding agents read.
- **Agent Skills:** Skills, guides, and templates are inspired by [Agent Skills](https://agentskills.io/). Both load detail only when a task needs it. Agent Lab does not follow the format and differs on purpose:
  - By default, a skill belongs to one agent. An agent is a role and a skill is one of its abilities. The same ability can differ by role: "update ticket" reads a GitHub issue for one agent and a Jira ticket for another. Separate skills avoid a switch inside one shared skill and keep each agent's context small.
  - Overlap between agents is not solved by sharing the skill. Knowledge that several agents need is shared in `.agents/shared/`. A capability that belongs to another agent's role is delegated to that agent, not copied.
  - The agent loads a skill through its `INDEX.md`. A client does not discover it from frontmatter. A skill is of no use without its agent, so automatic loading is not wanted.
  - Activation conditions stand only in `INDEX.md`. A skill that another procedure calls runs even if its own conditions would not cover the case.
  - As a result, clients that scan for `SKILL.md` files do not find these skills.

## Where Created Agents Live

A created agent (a "Target Agent") does not have to live inside this repository. It can live in its own project, kept connected to this rule set via a VS Code multi-root workspace — add both folders to one workspace so the agent has this repo's `AGENTS.md` and Evolver Agent available alongside its own project files.

This also saves context: day-to-day work with a Target Agent does not load the Evolver Agent at all — it is only pulled in on demand, when maintenance or evolution of the agent itself is needed.

## Maintaining This Repository

Use the **Evolver Agent** ([README-evolver.md](README-evolver.md)) to create new agents, validate or optimize existing ones, and apply open entries from `LEARNINGS.md`.

## Disclaimer

Agents built with this framework follow instructions and can still make mistakes. Approving a write or a risky action is a judgment call made by whoever approves it, whether a person or another agent — use at your own risk. See [LICENSE](LICENSE) for the legal terms.
