---
agent: AIIB Company Dossier
description: "Mode B — build a 7-section investment dossier on one company, screened within its sub-sector economics."
---

Run **Mode B: Company Dossier** for AIIB investment research.

Company: ${input:company:e.g. Sunsure Energy · India · C&I solar}

Execute the full Mode B methodology as defined in the **AIIB Company Dossier** agent — load the sub-sector
context, spawn **one Company Dossier Researcher worker per company** (each produces all 7 sections;
multiple companies → workers in parallel), assemble per `dossier-template.md`, and close with the
"Verify before relying" list. Do not abbreviate or reorder the agent's method here.
