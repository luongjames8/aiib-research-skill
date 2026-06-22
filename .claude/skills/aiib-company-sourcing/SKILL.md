---
name: aiib-company-sourcing
description: >-
  Mode S of AIIB-style investment research: source the companies. Given a sub-sector (ideally with its
  economics from an aiib-sector-scan run) or a country·sector, generate a RANKED LIST of mostly-PRIVATE,
  mandate-fit companies to investigate — by graph-expanding from known anchors (a company's competitors,
  suppliers, customers, JV partners, co-investors, and the fund-siblings of its PE/DFI backers), following
  DFI/PE fund portfolios, decomposing the value chain, and sweeping deal trackers, PPP pipelines,
  credit-rating lists, and local-language sources. Use this whenever the user wants to find, discover,
  source, or build a pipeline/longlist/shortlist of companies or deal targets — "what companies should I
  look at in <sector> <country>", "find private developers/operators/players in <sector>", "who competes
  with <company>", "expand from <company> to its peers", origination/deal-sourcing — even if they never
  say "sourcing". Sits between aiib-sector-scan (Mode A — context) and aiib-company-dossier (Mode B —
  deep-dive); its output feeds Mode B. Web-search floor; uses subagents when available, sequential when not.
---

# AIIB Company Sourcing (Mode S)

The middle stage of the funnel: **sub-sector economics → ranked private-company candidates.** You find
private operators by starting from known **anchors** and walking outward — not by screening tickers. Output
feeds the **aiib-company-dossier** skill (Mode B). Full method detail: `references/sourcing-methods.md`.

## Inputs
- **Required:** a sub-sector (e.g. "Indonesia · offshore wind") or a country·sector.
- **Optional:** the sub-sector economics from a Mode-A scan (tariffs, IRRs, risks, listed comps — used to
  rank and to seed anchors), specific anchor companies, target count.

## Workflow

### Step 1 — Establish anchors + context
Gather the sub-sector economics (from Mode A if available, else a quick sketch) and the **anchors**:
listed sector leaders, DFI investees, and recent deal/auction winners. Anchors are launch points — the
goal is the **private adjacents** around them, not the anchors themselves.

### Step 2 — Expand to candidates (the methods)
Apply the toolkit in `references/sourcing-methods.md`: **graph expansion** from each anchor (competitors,
suppliers, customers, JV partners, **PE/DFI fund-siblings**), **fund-following** (enumerate the portfolios
of funds/DFIs active here), **value-chain decomposition** (a player per link), the **source sweep** (deal
trackers, PPP pipelines, credit-rating lists), and **local-language mining** (the biggest private-tail
unlock). Cast several nets — overlap between methods is a quality signal.

**Delegation — REQUIRED when a subagent tool exists (Claude Code).** You **must** delegate: spawn one
`source-expander` subagent (Sonnet — cheap + parallel) **per anchor / per fund / per value-chain link**,
each carrying the sub-sector context, and let *them* do the web searches. **Do NOT run the expansion
searches yourself in the main context** — as orchestrator you only set the anchors, spawn the Sonnet
workers, and merge/dedup their returns. Only when **no** subagent tool exists (claude.ai chat app) do you
expand sequentially yourself.

### Step 3 — Dedup, screen, rank
Dedup across methods (a name found multiple ways is strong). Apply a **light** mandate-fit gate
(`references/aiib-mandate.md` — drop clearly out-of-mandate names; full scoring is the dossier's job).
**Bias to PRIVATE / unlisted** operators. Rank by mandate fit + the economic attractiveness of the
sub-sector + signs of scale/fundability (rated, DFI-backed, recent raise).

## Output structure
A **ranked candidate table**, plus a provenance banner. Each row:
`Company · sub-sector · listed/PRIVATE · how-found (method + anchor) · one-line why (mandate + economics) · provenance`.
Lead with the private names. This list is the input to **aiib-company-dossier** (Mode B) — note the top
few worth dossiering first.

## Self-check before returning
- [ ] Did I expand from anchors via **multiple** methods (graph + funds + value-chain + sweep), not one?
- [ ] Is the list **mostly PRIVATE / unlisted** operators (the point of this stage)?
- [ ] Deduped, light-mandate-screened, and **ranked** (not a raw dump)?
- [ ] Every candidate tagged with how-found + provenance (🟢/🔵/⚠️)?
- [ ] Flagged the top few to dossier first (hand-off to Mode B)?
