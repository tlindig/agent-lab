# Skill: Apply Learnings

## Procedure

1. Read `LEARNINGS.md`, list open entries.
2. Process one entry at a time (not batched):
   a. **Verify currency** — check whether the problem still reproduces now (test/grep, don't assume); state the finding.
   b. **Locate the authoritative fix location** — where does the agent actually evaluate this at runtime? (see `optimize.md` redundancy principle)
   c. If multiple reasonable fixes exist, present all alternatives with a clear recommendation.
   d. **Write gate** — present what will change and why, wait for explicit approval.
   e. Apply; delete the entry from `LEARNINGS.md` immediately.
3. Repeat for the next entry.
