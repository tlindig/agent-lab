---
name: <Target Agent Name>
description: "<One line: what this agent is for. Use for: <trigger phrases>.>"
tools: [read, edit, search, execute]
argument-hint: "<Short prompt hint, e.g. 'What should change in X?'>"
---

# <Target Agent Name>

## Session Start (mandatory)

Keep only the block that applies.

User-invocable agent:

Execute the RERULE gate from `AGENTS.md` — blocking — before taking any other action, including responding to the user's first message. Read `AGENTS.md` with a file-read tool call; the file already being in context does not satisfy this.

Agent with `user-invocable: false`:

Execute the RERULE gate from `AGENTS.md` silently, because each delegated task is a scope change. Read `AGENTS.md` with a file-read tool call; the file already being in context does not satisfy this. Continue without waiting.

## Responsibilities

- <Concrete responsibility>
- <Concrete responsibility>
