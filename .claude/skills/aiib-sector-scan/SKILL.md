---
name: aiib-sector-scan
description: >-
  Mode A of AIIB-style infrastructure investment research: turn a country + sector into a sourced market map.
  Enumerate and deep-dive EVERY sub-sector (a wide net, not a pre-judged few) through a 9-field economics
  template (size, tariffs, margins, IRRs, comps, track record, risks, competitors), then tier them and
  surface mandate-fit anchor companies. Use whenever the user wants to research, map, size, or assess the investment case for a
  sector or market — especially developing/emerging-market infrastructure or development finance — e.g.
  "research Indonesia renewables", "map the Vietnam data-center landscape", "investment case for Philippine
  water". Triggers on any AIIB-mandate sector (energy, transport, water, digital infrastructure, sustainable
  cities, health), even without the words "sector scan" or "AIIB". To FIND or LIST companies in a sector, use
  Mode S (aiib-company-sourcing) instead. Stage one of the funnel; feeds Mode S then Mode B. Web-search floor;
  uses subagents when available.
---

# AIIB Sector Scan (Mode A)

Top-down funnel, stage one: **Country · Sector → sub-sector economics + anchors.** Methodology proven on
a live deal-sourcing system. Output (economics + anchors) feeds the **aiib-company-sourcing** skill
(Mode S) → which feeds the **aiib-company-dossier** skill (Mode B).

Cast a **wide net** — research **every** sub-sector, don't pre-judge which few are "most investable" and
skip the rest (that's a guess made *before* you have evidence). The whole point of this map is breadth:
the funnel downstream relies on it. Cost stays bounded not by *dropping* sub-sectors but by the **fan-out
shape** — one bounded Sonnet worker per sub-sector, **one level deep (no subagent ever spawns another)**,
in concurrency-capped waves, each on a small search budget (Step 2).

## Inputs

- **Required:** a country and a sector. The sector should map to one of AIIB's 6 (Energy, Transport,
  Sustainable Cities, Digital Infrastructure, Water, Health) — see `references/aiib-mandate.md`. Accept
  the user's phrasing and map it (e.g. "renewables" → Energy; "logistics" → Transport; "data centers" →
  Digital Infrastructure).
- **Optional:** **depth** — `full` (DEFAULT: full A–I on **every** sub-sector — the wide net) or
  `quick`/`overview` (one-line headline + tier per sub-sector, no full A–I — only if the user explicitly
  wants speed over coverage). Also: quarter/timeframe (default current), a sub-sector focus, number of anchors.

## Workflow

### Step 1 — Enumerate sub-sectors (exhaustive)
List the sector's sub-sectors as completely as possible. **First from background knowledge, then confirm
and extend via web search** for this specific country (a market may have niche sub-sectors training data
misses). Tag each sub-sector's provenance. Example — Renewables → utility-scale solar · C&I/rooftop solar
· onshore wind · offshore wind · geothermal · small hydro · BESS/storage · WtE/biomass · distributed
generation. Digital Infrastructure → data centers (colo + hyperscale) · fiber · towers · subsea cable ·
edge. Do not stop at the obvious 3–4; be exhaustive.

### Step 2 — Research EVERY sub-sector (wide net), then tier from the evidence
Do **not** pre-rank sub-sectors and skip the "lesser" ones — that judgment, made before any research, is
the thing to avoid. **Cover all of them.** Run **each** enumerated sub-sector through the 9-field A–I
template (`references/ai-template.md`: market economics · pricing/tariff · margins · revenue quality ·
valuation/comps · track record incl. blow-ups · IRR · named risks · competitive landscape). Only *after*
you have the evidence do you assign each an A/B/C investability tier and rank them.

**Cost is bounded by the fan-out SHAPE, not by dropping sub-sectors** (this is the rule you care about):
- **One bounded worker per sub-sector.** When a subagent/Task tool exists, spawn one `subsector-researcher`
  subagent per sub-sector (Sonnet — cheap). ⛔ **`subagent_type: subsector-researcher` — NEVER
  `general-purpose`** (general-purpose has the Agent tool; subsector-researcher does not).
- **ONE level deep — no subagent ever spawns another.** Orchestrator → workers, full stop. This is what
  prevents the runaway (the old blowup was subagents-spawning-subagents, ~39→174 agents), *not* a coverage limit.
- **Concurrency-capped waves.** At most **~6 workers running at once**; more sub-sectors than that →
  dispatch in **waves of ~6**. Every sub-sector still gets covered — you just don't run 12 at once.
- **Per-worker search budget.** Each worker: **~2–4 searches; WebSearch first, WebFetch only when a
  snippet won't do.**

So ~8 renewable sub-sectors → ~8 bounded Sonnet workers across ~2 waves: **wide coverage, bounded cost,
no recursion.** (Optional: if the user explicitly asks for a *quick / overview* scan, you may instead give
each sub-sector a one-line headline + tier without the full A–I — but the **default is full coverage**.)

**Structured comps are automatic** (`references/data-sources.md`): the `subsector-researcher` workers
have Bash and **run `scripts/fetch_financials.py <ticker>` themselves** for field E — it **auto-installs
yfinance on first use** and returns verified EV/EBITDA, P/E, P/B, margins (🟢). They web-eyeball comps
(⚠️) only if it returns `unavailable` (sandbox blocks pip/network). No manual setup — don't ship a scan on
guessed multiples when the script can verify them.

**No subagent tool (claude.ai chat app):** work through every sub-sector sequentially yourself, same A–I
template + per-sub-sector search budget. To guarantee the cheap parallel-Sonnet path on Claude Code, run
the session on Sonnet and/or ask for delegation in the prompt (see README "Controlling cost").

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
2. **Sub-sector deep-dives — one full A–I block per sub-sector** (every enumerated one, not a subset),
   each ending with a provenance line. (`quick`/`overview` mode: a one-line headline + tier per sub-sector instead.)
3. **Sector synthesis** — cross-sub-sector comparison table (sub-sector | IRR range | tariff | margin
   trend | cycle | tier) + which sub-sectors rank most investable **and why, from the evidence** (bear case named).
4. **AIIB mandate alignment** — sector/theme match + Strong/Partial/Out verdict.
5. **Anchors** — listed leaders / DFI investees / deal winners per high-conviction sub-sector, with
   provenance — the hand-off to **aiib-company-sourcing** (Mode S).

## Self-check before returning (depth gate — do this every run)

Stop and verify; if any answer is "no", fix it before returning:
- [ ] **Wide net?** Did I enumerate ALL sub-sectors AND run the **full A–I on every one** (not pre-rank
      and skip the "lesser" ones)? Tiering came **after** the research, from evidence — not a priori.
- [ ] **Fan-out bounded by shape, not coverage?** One `subsector-researcher` per sub-sector (never
      general-purpose), **one level deep (no subagent spawned another)**, run in waves of ~6, each ~2–4 searches?
- [ ] **Bad news?** Did I include negative signals (write-downs, stalled projects, payment delays)?
- [ ] **Provenance?** Is every numeric claim tagged 🟢/🔵/⚠️, with the no-live-sources banner if web was off?
- [ ] **Mandate?** Is alignment scored from `aiib-mandate.md` (cited), not memory?
- [ ] **Hand-off?** Are anchors (listed leaders / DFI investees / deal winners) surfaced for Mode S sourcing?
