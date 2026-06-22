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
  look at in <sector> <country>", "which companies operate in <country> <sector>", "find private
  developers/operators/players in <sector>", "who competes with <company>", "list/expand from <company> to
  its peers", origination/deal-sourcing — even if they never say "sourcing". Use this for the MANY-company
  discovery step (a list); to deep-dive ONE named company use aiib-company-dossier (Mode B) instead. Sits
  between aiib-sector-scan (Mode A — context) and aiib-company-dossier (Mode B — deep-dive); output feeds Mode B. Web-search floor; uses subagents when available, sequential when not.
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

### Step 1 — Establish + DEDUP anchors, load context
Gather the sub-sector economics (from Mode A if available, else a quick sketch) and the **anchors**:
listed sector leaders, DFI investees, and recent deal/auction winners. Anchors are launch points — the
goal is the **private adjacents** around them, not the anchors themselves.

**Dedup the anchors BEFORE you spawn anything** (this is what stops three workers all chasing Star
Energy / Salak). Normalize each name — strip legal/suffix noise (`PT`, `Tbk`, `Group`, `Bhd`, `PLC`,
`Pvt`, `Ltd`, `Holdings`), lowercase, and merge obvious variants ("Star Energy", "PT Star Energy
Geothermal", "Star Energy Group" → one). Then assign **one worker per DISTINCT anchor** with a
non-overlapping brief. (You can't share state across parallel workers, so the lever is non-overlapping
assignment up front + dedup on the way out — Step 3 — not preventing every redundant search.)

### Step 2 — Expand to candidates (the methods)
Apply the toolkit in `references/sourcing-methods.md`: **graph expansion** from each anchor (competitors,
suppliers, customers, JV partners, **PE/DFI fund-siblings**), **fund-following** (enumerate the portfolios
of funds/DFIs active here), **value-chain decomposition** (a player per link), the **source sweep** (deal
trackers, PPP pipelines, credit-rating lists), and **local-language mining** (the biggest private-tail
unlock). Cast several nets — overlap between methods is a quality signal.

**Delegation — REQUIRED when a subagent tool exists (Claude Code).**

⛔ **Use `subagent_type: source-expander` — NEVER `general-purpose`.** This is the single most important
rule in this skill. `general-purpose` has the **Agent tool**, so those workers **re-delegate and spawn
their own children**, which spawn more — a runaway tree (one real run hit ~2,800 calls / 174 agents).
`source-expander` ships with tools **WebSearch/WebFetch/Read only — no Agent tool — so it physically
cannot recurse.** Always pass `subagent_type: "source-expander"`.

**Dedup anchors BEFORE spawning, then one worker per anchor.** Collapse overlapping anchors first (don't
spawn three workers that all chase Star Energy / Salak). Spawn **one `source-expander` per distinct
anchor — aim for ~8–12 total, hard cap ~15.** Do **not** spawn per micro value-chain link (links ×
players explodes); fold value-chain coverage into the per-anchor workers' briefs instead.

**Per-worker search budget (put it in each worker's prompt):** "**max ~10 searches; prefer WebSearch;
only WebFetch a page when a search snippet is insufficient.**" (WebFetch is the expensive call and often
403s — keep it rare.)

**Fan-out width + waves:** at most **~6 workers concurrent**; more anchors than that → dispatch in waves
of ~6. As orchestrator you only set/dedup anchors, spawn the source-expander workers, and merge their
returns — never run the expansion searches yourself. Only when **no** subagent tool exists (claude.ai
chat app) do you expand sequentially yourself, within the same search budget.

### Step 3 — Merge, DEDUP, screen, rank
As workers return, merge all candidate lists and **dedup by normalized name** (same suffix-stripping +
lowercase + variant-merge rule as Step 1). A name surfaced by **multiple** anchors/methods collapses to
**ONE entry** — but record that it was multi-sourced: that overlap is a **strength signal** (rank it
higher), not a duplicate to discard. Then apply a **light** mandate-fit gate (`references/aiib-mandate.md`
— drop clearly out-of-mandate names; full scoring is the dossier's job). **Bias to PRIVATE / unlisted**
operators. Rank by mandate fit + multi-source overlap + sub-sector attractiveness + signs of
scale/fundability (rated, DFI-backed, recent raise).

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
