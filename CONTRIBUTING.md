# Contributing

Thanks for considering a contribution to Agent Lab. This project is a rule framework, not application code — most contributions touch `AGENTS.md`, `.agents/<slug>.agent.md` definitions, their skills/guides/templates, or documentation.

## Before You Start

- For small fixes (typos, broken links, clarifications), open a pull request directly.
- For new agents, new skills/guides/templates, or rule changes, open an issue first using the **Feature Request** template so the approach can be discussed before you invest time.

## Workflow

1. Fork the repository and create a branch from `main`.
2. Make your change.
3. If you modify an agent's rules (`AGENTS.md` or any `.agent.md`), run it through the **Evolver Agent**'s `validate` and `optimize` skills (see [README-evolver.md](README-evolver.md)) before opening the PR, and mention the result in the PR description.
4. Open a pull request using the PR template checklist.

## Conventions

- File content (rules, docs, commit messages) is written in English, as defined in `AGENTS.md`.
- Rule text follows KISS, DRY, short single-idea sentences, active voice, and positive instruction (what to do, not what to avoid) — the same standard the Evolver Agent checks for.
- Commit messages use a short `type: summary` prefix (`feat:`, `fix:`, `refactor:`, `docs:`), consistent with the existing history.
- Classify your own change as RULE (how an agent should work) or DATA (project content) in the PR description if it isn't obvious — this mirrors the classification agents are required to do for user input.

## Reporting Process Gaps

If you hit a missing rule, unexpected tool behavior, or a process gap while contributing, add an entry to `LEARNINGS.md` using the format described there instead of fixing it ad hoc — learnings are applied as a deliberate, separate step.

## Code of Conduct

Participation in this project is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
