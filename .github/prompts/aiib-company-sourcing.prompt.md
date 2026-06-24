---
agent: AIIB Company Sourcing
description: "Mode S — graph-expand sourcing anchors into a ranked longlist of mostly-private, mandate-fit companies."
---

Run **Mode S: Company Sourcing** for AIIB investment research.

Anchors / sub-sector: $ARGUMENTS

Execute the full Mode S methodology as defined in the **AIIB Company Sourcing** agent — iterative
graph-expansion **rounds carrying a found-set** (NOT one parallel per-anchor blast), small batches of
**Source Expander** workers per round, dedup via `dedup_candidates.py`, and a light mandate-fit ranking
biased toward private/unlisted operators. Do not abbreviate or reorder the agent's method here.
