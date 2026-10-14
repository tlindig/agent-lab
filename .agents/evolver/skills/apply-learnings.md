# Skill: Apply Learnings

## Procedure

1. Read `<project_root>/LEARNINGS.md`, list open entries for the Target Agent (slug in the heading); skip other slugs.
2. Process one entry at a time (not batched):
   a. **Verify currency** — check whether the problem still reproduces now (test/grep, don't assume); state the finding.
   b. **Independent analysis** — reason out the root cause and a candidate fix (including its authoritative location, see `optimize.md` redundancy principle) before treating the entry's own `Improvement` text as the answer; then compare the two and reconcile differences.
   c. If multiple reasonable fixes exist, present all alternatives with a clear recommendation.
   d. **Write gate** — present what will change and why, wait for explicit approval.
   e. Apply; delete the entry from `<project_root>/LEARNINGS.md` immediately.
3. Repeat for the next entry.
