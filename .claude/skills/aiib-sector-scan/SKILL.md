---
name: aiib-sector-scan
description: >-
  Mode A of AIIB-style investment research: turn a country + sector into an exhaustive, sourced market
  map. Given a country and a sector (e.g. "Indonesia · Renewables", "Vietnam · Digital Infrastructure",
  "Brazil · Transport"), enumerate ALL sub-sectors and run each through a 9-field A–I economics template
  (market size, tariffs, margins, IRRs, listed comps, track record, risks, competitors), then produce a
  ranked, mandate-fit company shortlist. Use this whenever the user wants to research, map, size, or
  assess the investment case for a sector or market — especially in developing/emerging markets for
  infrastructure or development-finance investing. Trigger on phrasings like "research <sector> in
  <country>", "what's the investment case for <sector> in <country>", "map the <sector> landscape",
  "which companies operate in <country> <sector>", or anything about AIIB-mandate sectors (energy,
  transport, water, digital infrastructure, sustainable cities, health) — even if the user never says
  "sector scan" or "AIIB". Pairs with the aiib-company-dossier skill (Mode B) for the shortlisted
  companies. Web-search floor; uses subagents when available, runs sequentially when not.
---

# AIIB Sector Scan (Mode A)

Top-down funnel, stage one: **Country · Sector → sub-sector economics → company shortlist.** Methodology
proven on a live deal-sourcing system. Output feeds the **aiib-company-dossier** skill (Mode B).

Depth is the whole point. This map is the foundation the rest of the funnel stands on — a shallow,
3-bullet "economics summary" produces false signals that every downstream company screen inherits. So
the bar is exhaustive sub-sector coverage and real numbers, not a tidy paragraph.

## Inputs

- **Required:** a country and a sector. The sector should map to one of AIIB's 6 (Energy, Transport,
  Sustainable Cities, Digital Infrastructure, Water, Health) — see `references/aiib-mandate.md`. Accept
  the user's phrasing and map it (e.g. "renewables" → Energy; "logistics" → Transport; "data centers" →
  Digital Infrastructure).
- **Optional:** quarter/timeframe (default: current), a sub-sector focus, number of shortlist names.

## Workflow

### Step 1 — Enumerate sub-sectors (exhaustive)
List the sector's sub-sectors as completely as possible. **First from background knowledge, then confirm
and extend via web search** for this specific country (a market may have niche sub-sectors training data
misses). Tag each sub-sector's provenance. Example — Renewables → utility-scale solar · C&I/rooftop solar
· onshore wind · offshore wind · geothermal · small hydro · BESS/storage · WtE/biomass · distributed
generation. Digital Infrastructure → data centers (colo + hyperscale) · fiber · towers · subsea cable ·
edge. Do not stop at the obvious 3–4; be exhaustive.

### Step 2 — Deep-dive each sub-sector (the A–I template)
Run **every** enumerated sub-sector through the 9-field A–I template in `references/ai-template.md`
(market economics · pricing/tariff · margins · revenue quality · valuation/comps · track record incl.
blow-ups · IRR estimate · named risks · competitive landscape). Numbers, not adjectives. Include the
bad news. Tier each A/B/C on investability.

**Data tiers** (`references/data-sources.md`): for field E (valuation & comps), pull free listed-comp
multiples with `scripts/fetch_financials.py <ticker>` (yfinance — international tickers via exchange
suffixes) when a code tool + network are available; else gather comps from web search. Tag by provenance.

**Delegation (the portability rule):** If you have a Task/subagent tool available (Claude Code), spawn
one `subsector-researcher` subagent **per sub-sector** and run them in parallel, then synthesize. If you
do not (claude.ai chat app), work through the sub-sectors **sequentially** in this context. The output
is identical either way — subagents are an optimization, never a requirement.

### Step 3 — Mandate alignment + company shortlist
Map the sector and its sub-sectors to AIIB's 6 sectors + 4 thematic priorities using
`references/aiib-mandate.md` (cite it). Then surface a **ranked shortlist of companies** operating in
the highest-conviction sub-sectors — for each: name, sub-sector, one-line why (mandate fit + economics),
and provenance. These are the inputs the user feeds to the aiib-company-dossier skill.

## Output structure

1. **Header** — `<Country> · <Sector>` + coverage note (N sub-sectors covered) + a provenance banner
   (especially the ⚠️ no-live-sources banner if web access is unavailable — see provenance.md).
2. **Sub-sector deep-dives** — one A–I block per sub-sector, each ending with a provenance summary line.
3. **Sector synthesis** — cross-sub-sector comparison table (sub-sector | IRR range | tariff | margin
   trend | cycle | tier) + which sub-sectors are most investable and why (bear case named).
4. **AIIB mandate alignment** — sector/theme match + Strong/Partial/Out verdict.
5. **Company shortlist** — ranked, mandate-fit, with provenance — the hand-off to Mode B.

## Self-check before returning (depth gate — do this every run)

Stop and verify; if any answer is "no", fix it before returning:
- [ ] **Exhaustive?** Did I enumerate ALL the sector's sub-sectors (not just the obvious 3–4)?
- [ ] **Depth?** Does EVERY sub-sector have all 9 A–I fields with **actual numbers**? A one-paragraph
      sub-sector is a FAILURE — redo it.
- [ ] **Bad news?** Did I include negative signals (write-downs, stalled projects, payment delays)?
- [ ] **Provenance?** Is every numeric claim tagged 🟢/🔵/⚠️, with the no-live-sources banner if web was off?
- [ ] **Mandate?** Is alignment scored from `aiib-mandate.md` (cited), not memory?
- [ ] **Hand-off?** Is there a ranked, mandate-fit company shortlist for Mode B?
