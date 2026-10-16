# Skill: Extend Agent

## Procedure

Placeholders: `<project_root>/.agents/evolver.agent.md` § Target Agent.

1. Ask for `<target-slug>`, `<target-project_root>`, and the content to add or extract. Choose the type per § When to Extract Skills/Guides/Templates in `<project_root>/.agents/evolver.agent.md`: skill, guide, or template. For a skill, ask whether only other skills or rules invoke it.
2. If `<target-project_root>/.agents/<target-slug>/<skills|guides|templates>/INDEX.md` does not exist, create it from `<project_root>/.agents/evolver/templates/index.template.md`.
3. Draft the file in that folder. Follow the folder's role in `validate.md` → Folder roles. Start a skill with `# Skill: <Name>` and `## Procedure`.
4. Add one row to that folder's `INDEX.md`: file name and one-line purpose. Mark a skill "Internal" per § Skills in `<project_root>/.agents/evolver.agent.md`.
5. If the content moved out of an existing file, replace it there with a reference to the new file.
