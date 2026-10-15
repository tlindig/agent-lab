---
name: <Target Agent Name>
description: "<One line: what this agent is for. Use for: <trigger phrases>.>"
tools: [read, edit, search, execute]
argument-hint: "<Short prompt hint, e.g. 'What should change in X?'>"
---

# <Target Agent Name>

## Session Start (mandatory)

Execute the RERULE gate from `AGENTS.md` — blocking — before taking any other action, including responding to the user's first message. Read `AGENTS.md` with a file-read tool call; the file already being in context does not satisfy this.

## Responsibilities

- <Concrete responsibility>
- <Concrete responsibility>
