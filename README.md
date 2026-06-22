# AIIB Investment Research Skills

Two portable [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) for
AIIB-style developing-markets infrastructure investment research, usable in **claude.ai** (web + desktop)
and **Claude Code** (terminal + web). A top-down funnel in two modes:

- **Mode A — `aiib-sector-scan`** — input `Country · Sector` (e.g. "Indonesia · Renewables") → exhaustive
  sub-sector deep-dive (9-field A–I economics per sub-sector) + a ranked, mandate-fit **company shortlist**.
- **Mode B — `aiib-company-dossier`** — input a company (or a Mode-A shortlist row) → a structured
  **5-section dossier**: background · forward guidance · financials · AIIB-mandate alignment · key people.

### Design principles

- **Provenance-tagged.** Every claim is marked 🟢 web-sourced / 🔵 connector / ⚠️ training-unverified, so
  unverified figures are visible. Built for a **web-search floor**: with no network it still runs, fully
  ⚠️-tagged under a "no live sources" banner.
- **Mandate-anchored.** Each skill bundles `references/aiib-mandate.md` — AIIB's 6 sectors + 4 thematic
  priorities + 2030 targets, sourced from aiib.org — so mandate fit is cited, not hallucinated.
- **Subagents where available, never required.** On Claude Code the skills delegate each sub-sector /
  company to a parallel subagent (`.claude/agents/`); on the claude.ai chat app (no subagents) they run
  sequentially. Same output either way.

## Install

### claude.ai (web / desktop) — Pro, Max, Team, Enterprise (code execution enabled)
Each skill folder is self-contained. In **Settings → Capabilities → Skills**, upload each of:
- `.claude/skills/aiib-sector-scan/`
- `.claude/skills/aiib-company-dossier/`

(Subagents in `.claude/agents/` are not used on claude.ai; the skills detect this and run sequentially.)

### Claude Code (terminal or web)
Clone this repo and open it (or point a Claude Code web session at it). The skills in `.claude/skills/`
and subagents in `.claude/agents/` are picked up automatically — subagent fan-out works here.

## Usage

```
Mode A:  "Research Indonesia · Renewables for AIIB."  →  sub-sector deep-dive + company shortlist
Mode B:  "Build a dossier on <company>."              →  5-section investment dossier
```

Typical flow: run Mode A on a country·sector, then run Mode B on each shortlisted company.

## Disclaimer

- **Not affiliated with AIIB.** This is an independent, unofficial tool. It is **not** affiliated with,
  endorsed by, sponsored by, or sanctioned by the Asian Infrastructure Investment Bank (AIIB). "AIIB" and
  related names and marks are the property of their respective owner and are used here only for
  descriptive reference (nominative fair use).
- **Source of mandate data.** The AIIB sector and thematic-priority information in
  `references/aiib-mandate.md` was sourced from AIIB's public website (**aiib.org**) as of 2026-06-22 and
  may be incomplete or out of date. Consult **aiib.org** for authoritative, current information.
- **Not investment advice.** Output is AI-generated research for informational purposes only. It may
  contain errors, omissions, or fabricated figures — that is exactly why every claim is provenance-tagged
  (🟢 web / 🔵 connector / ⚠️ training-unverified). It does **not** constitute investment, financial,
  legal, or tax advice. Verify every figure independently and do your own due diligence before relying on
  anything here.
- **No warranty.** Provided "as is", without warranty of any kind. Use at your own risk; the authors
  accept no liability for any decision made on the basis of this tool's output.
