# Skill: Rename Agent

## Procedure

`<target-slug>` and `<Target Agent Name>` are the old identifiers; `<new-slug>` and `<New Agent Name>` are the new ones.

1. Ask for `<new-slug>` and `<New Agent Name>`; confirm `<target-project_root>`.
2. Find every occurrence of the old slug and display name: `grep -rniI --exclude-dir=.git -e "<target-slug>" -e "<Target Agent Name>" <target-project_root>`. Review each hit — a word that is also an ordinary word needs a judgment.
3. Present the change set (Write gate):
   - Move `<target-project_root>/.agents/<target-slug>.agent.md`, `<target-project_root>/.agents/<target-slug>/`, and `<target-project_root>/README-<target-slug>.md` to the new slug.
   - Recreate the symlink `<target-project_root>/.github/agents/<target-slug>.agent.md` for the new slug.
   - Set `name` in the frontmatter and the `#` heading of the agent file, the `#` heading of the README, and the `<Target Agent Name>` in the `INDEX.md` headings to `<New Agent Name>`.
   - Update path references and prose mentions of the agent in the Target Agent's files, in `<target-project_root>/README.md`, and in `<target-project_root>/AGENTS.md`, and the slug in `<target-project_root>/LEARNINGS.md` headings.
4. After approval, move the files with `git -C <target-project_root> mv <old> <new>`, using paths relative to `<target-project_root>`. Use plain `mv` if `git -C <target-project_root> rev-parse --is-inside-work-tree` fails. Replace the symlink: `ln -s ../../.agents/<new-slug>.agent.md <target-project_root>/.github/agents/<new-slug>.agent.md`, then remove the old one. Edit file contents with the editor tools.
5. Verify: `grep` finds no leftover old slug in the confirmed places, `readlink` shows the new symlink target, and the mechanical checks of `<project_root>/.agents/evolver/skills/validate.md` pass for `<new-slug>`.
