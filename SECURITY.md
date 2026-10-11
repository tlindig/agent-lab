# Security Policy

Agent Lab is a markdown-based rule framework, not executable code. Relevant security issues are mainly about the rules themselves, for example:

- A phrasing that lets an instruction injected through processed content (e.g. a Target Agent's files) override agent behavior.
- A gap in the Behavior Invariants that allows bypassing the Write/Action gate or performing an unapproved destructive action.
- A rule conflict that silently weakens the RERULE gate or the Rule Hierarchy.

## Risk Model

An agent built with this framework acts on instructions, not on its own goals — it only does what a user or calling process asks it to do. The main risk is not autonomous misbehavior but **unintended consequences of the instructions given to it**. The Write/Action gates in `AGENTS.md` require explicit approval before any write or risky action, but that approval is a judgment call made by whoever gives it.

Use at your own risk; see [LICENSE](LICENSE) for the legal terms (provided "as is", no warranty, no liability).

## Reporting a Vulnerability

Please report security issues privately using GitHub's **Private Vulnerability Reporting**:

1. Go to the repository's **Security** tab.
2. Select **Report a vulnerability**.
3. Describe the issue and, if possible, a reproduction scenario.

Do not open a public issue for security-relevant findings until it has been reviewed.

This project is maintained on a best-effort basis; there is no guaranteed response time, but reports are reviewed as soon as possible.

## Non-Security Bugs

For anything that isn't security-relevant (e.g. unclear rule wording, broken links), please use the regular issue templates instead.
