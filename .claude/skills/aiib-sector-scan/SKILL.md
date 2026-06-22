---
name: aiib-sector-scan
description: >-
  Mode A of AIIB-style investment research: turn a country + sector into an exhaustive, sourced market
  map. Given a country and a sector (e.g. "Indonesia · Renewables", "Vietnam · Digital Infrastructure",
  "Brazil · Transport"), enumerate ALL sub-sectors and run each through a 9-field A–I economics template
  (market size, tariffs, margins, IRRs, listed comps, track record, risks, competitors), then produce a
  set of mandate-fit anchor companies for sourcing. Use this whenever the user wants to research, map, size, or
  assess the investment case for a sector or market — especially in developing/emerging markets for
  infrastructure or development-finance investing. Trigger on phrasings like "research <sector> in
  <country>", "what's the investment case for <sector> in <country>", "map the <sector> landscape",
  "size the <sector> opportunity in <country>", or anything about the economics of AIIB-mandate sectors
  (energy, transport, water, digital infrastructure, sustainable cities, health) — even if the user never
  says "sector scan" or "AIIB". (To *find or list the companies* in a sector, that's Mode S —
  aiib-company-sourcing — not this skill.) Stage one of the funnel — its economics + anchors feed the aiib-company-sourcing
  skill (Mode S), which feeds the aiib-company-dossier skill (Mode B). Web-search floor; uses subagents
  when available, runs sequentially when not.
---

# AIIB Sector Scan (Mode A)

Top-down funnel, stage one: **Country · Sector → sub-sector economics + anchors.** Methodology proven on
a live deal-sourcing system. Output (economics + anchors) feeds the **aiib-company-sourcing** skill
(Mode S) → which feeds the **aiib-company-dossier** skill (Mode B).

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

**Delegation — REQUIRED when a subagent tool exists (Claude Code).** If you have a Task/subagent tool,
you **must** delegate: spawn one `subsector-researcher` subagent **per sub-sector** (they run on Sonnet —
cheap + parallel) and let *them* do the web searches and data pulls. **Do NOT run the per-sub-sector web
searches yourself in the main context** — as the orchestrator your job is only to (a) enumerate the
sub-sectors, (b) spawn one Sonnet worker per sub-sector, (c) synthesize their returns. The whole point is
to keep the expensive orchestrator model out of the token-heavy searching; doing the searches inline
defeats it. Only when **no** subagent tool exists (claude.ai chat app) do you work through the
sub-sectors sequentially yourself. Output is identical — the difference is cost and speed. **Cap the
fan-out:** at most **~6 workers concurrently** — if there are more sub-sectors, dispatch in waves of ~6.
Fan-out stays **one level deep** (workers return data, never spawn their own subagents) to avoid rate-limit storms.

### Step 3 — Mandate alignment + anchors (hand-off to sourcing)
Map the sector and its sub-sectors to AIIB's 6 sectors + 4 thematic priorities using
`references/aiib-mandate.md` (cite it). Then surface the **anchors** that the sourcing stage expands
from — the **listed sector leaders, DFI investees, and recent deal/auction winners** per
high-conviction sub-sector (name, sub-sector, why it's an anchor, provenance). You are not doing the
full private-company hunt here — that's the **aiib-company-sourcing** skill (Mode S), which graph-expands
these anchors into the ranked private-candidate list. Hand the sub-sector economics + anchors to Mode S.

## Output structure

1. **Header** — `<Country> · <Sector>` + coverage note (N sub-sectors covered) + a provenance banner
   (especially the ⚠️ no-live-sources banner if web access is unavailable — see provenance.md).
2. **Sub-sector deep-dives** — one A–I block per sub-sector, each ending with a provenance summary line.
3. **Sector synthesis** — cross-sub-sector comparison table (sub-sector | IRR range | tariff | margin
   trend | cycle | tier) + which sub-sectors are most investable and why (bear case named).
4. **AIIB mandate alignment** — sector/theme match + Strong/Partial/Out verdict.
5. **Anchors** — listed leaders / DFI investees / deal winners per high-conviction sub-sector, with
   provenance — the hand-off to **aiib-company-sourcing** (Mode S).

## Self-check before returning (depth gate — do this every run)

Stop and verify; if any answer is "no", fix it before returning:
- [ ] **Exhaustive?** Did I enumerate ALL the sector's sub-sectors (not just the obvious 3–4)?
- [ ] **Depth?** Does EVERY sub-sector have all 9 A–I fields with **actual numbers**? A one-paragraph
      sub-sector is a FAILURE — redo it.
- [ ] **Bad news?** Did I include negative signals (write-downs, stalled projects, payment delays)?
- [ ] **Provenance?** Is every numeric claim tagged 🟢/🔵/⚠️, with the no-live-sources banner if web was off?
- [ ] **Mandate?** Is alignment scored from `aiib-mandate.md` (cited), not memory?
- [ ] **Hand-off?** Are anchors (listed leaders / DFI investees / deal winners) surfaced for Mode S sourcing?
