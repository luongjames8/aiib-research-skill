---
name: aiib-sector-scan
description: >-
  Mode A of AIIB-style investment research: turn a country + sector into an exhaustive, sourced market
  map. Given a country and a sector (e.g. "Indonesia · Renewables", "Vietnam · Digital Infrastructure",
  "Brazil · Transport"), enumerate ALL sub-sectors, triage them cheaply, and run the 9-field A–I economics
  template (market size, tariffs, margins, IRRs, listed comps, track record, risks, competitors) on the
  most-investable few (or all, on request), then produce a set of mandate-fit anchor companies for sourcing. Use this whenever the user wants to research, map, size, or
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

Depth **where it counts**. This map is the foundation the funnel stands on, so it must be more than a
3-bullet summary — but it is *context*, not a research report on every niche. Be **exhaustive in
enumerating** the sub-sectors, triage them all cheaply, and spend real depth only on the **top few** that
matter (Step 2). Going full-depth on every sub-sector is what makes a scan cost a fortune for little
added signal.

## Inputs

- **Required:** a country and a sector. The sector should map to one of AIIB's 6 (Energy, Transport,
  Sustainable Cities, Digital Infrastructure, Water, Health) — see `references/aiib-mandate.md`. Accept
  the user's phrasing and map it (e.g. "renewables" → Energy; "logistics" → Transport; "data centers" →
  Digital Infrastructure).
- **Optional:** **depth** — `screening` (DEFAULT: triage all sub-sectors + full A–I on the top ~3) or
  `deep`/`exhaustive` (full A–I on every sub-sector — opt-in, much costlier). Also: quarter/timeframe
  (default current), a sub-sector focus, number of anchors. Read the user's intent for depth too — words
  like "quick / overview / just the landscape" → screening; "deep / thorough / exhaustive" → deep.

## Workflow

### Step 1 — Enumerate sub-sectors (exhaustive)
List the sector's sub-sectors as completely as possible. **First from background knowledge, then confirm
and extend via web search** for this specific country (a market may have niche sub-sectors training data
misses). Tag each sub-sector's provenance. Example — Renewables → utility-scale solar · C&I/rooftop solar
· onshore wind · offshore wind · geothermal · small hydro · BESS/storage · WtE/biomass · distributed
generation. Digital Infrastructure → data centers (colo + hyperscale) · fiber · towers · subsea cable ·
edge. Do not stop at the obvious 3–4; be exhaustive.

### Step 2 — Triage all cheaply, deep-dive only the few (DEPTH CONTROL — read this)
This scan is **context**, not a research report on every niche — so do **not** spend full depth
uniformly. That is what makes a scan cost a fortune. Two gears:

1. **Triage ALL sub-sectors — search ADAPTIVELY, not flat-one-each.** For each, capture the **headline
   economics** — market size, price/tariff, IRR range, top 1–2 risks, and an A/B/C investability tier.
   Spend searches **where your confidence is low, not uniformly**:
   - **Well-known sub-sector** (you know the rough size/tariff/IRR): **0–1 search** — a quick confirm, or
     none + ⚠️-tag the numbers as training-based.
   - **Niche / thinly-covered sub-sector** (frontier market, obscure segment): **~1–2 searches** — your
     priors are weak, so verify before tiering it.
   - **Borderline sub-sectors near the top-3 cutoff: search these the most.** Getting the *ranking* wrong
     wastes the expensive deep budget on the wrong sub-sectors, so resolve close calls before committing
     to which ~3 go deep. This is the highest-leverage place to spend a triage search.
2. **Full A–I on the top ~3 most-investable sub-sectors only** (the 9-field `references/ai-template.md`).
   The rest stay at headline depth. **Exception:** if the user explicitly asks for a *deep / exhaustive /
   thorough* scan, run full A–I on all — but that's opt-in and expensive; say so.

**Search budget — cheap, but weighted to uncertainty.** A default scan averages **~1 search per
sub-sector — front-loaded on the niche + borderline ones, ~0 on the obvious ones — plus a few per deep
one (~15–25 searches total)**, NOT 3–5 uniformly. If you're firing dozens of searches or spawning a
worker for every sub-sector, you're overspending — tighten.

**Data tiers** (`references/data-sources.md`): for the deep sub-sectors' field E (comps), pull free
listed-comp multiples with `scripts/fetch_financials.py <ticker>` (yfinance) when a code tool + network
are available; else web. Tag by provenance.

**Delegation — MANDATORY for the deep A–I dives (if a subagent/Task tool exists).** Triage runs **inline**
(cheap, headline numbers from knowledge). But the **deep 9-field A–I dives MUST be delegated** — **you,
the orchestrator, do NOT run A–I web research in your own context.** Spawn one `subsector-researcher`
subagent **per deep sub-sector (~3)** and have it do the searching; you only synthesize the returns.
**If you catch yourself web-searching tariffs / IRRs / comps yourself for a deep sub-sector, STOP and
spawn the subagent instead** — keeping the expensive orchestrator model off the heavy research is the
whole point (the workers run on Sonnet). ⛔ **`subagent_type: subsector-researcher` — NEVER
`general-purpose`** (general-purpose has the Agent tool and will recurse into a runaway tree;
subsector-researcher has only WebSearch/WebFetch/Read, so it can't). Each worker's budget: **~2–4
searches; prefer WebSearch, WebFetch
only if a snippet is insufficient.** **Cap the fan-out:** ~6 workers concurrent max. Only when no
subagent tool exists (claude.ai chat app) do the deep dives sequentially yourself.

(Reality: for a small triaged scope the model may judge inline cheaper and skip delegation — that's
acceptable and still bounded. To *guarantee* the cheap parallel-Sonnet path, the user runs the session
on Sonnet and/or asks for delegation in the prompt — see the README "Controlling cost" section.)

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
2. **Sub-sector triage + deep-dives** — headline economics + an A/B/C tier for **all** sub-sectors; a
   full A–I block for the **top ~3** most-investable (or all, in deep mode), each with a provenance line.
3. **Sector synthesis** — cross-sub-sector comparison table (sub-sector | IRR range | tariff | margin
   trend | cycle | tier) + which sub-sectors are most investable and why (bear case named).
4. **AIIB mandate alignment** — sector/theme match + Strong/Partial/Out verdict.
5. **Anchors** — listed leaders / DFI investees / deal winners per high-conviction sub-sector, with
   provenance — the hand-off to **aiib-company-sourcing** (Mode S).

## Self-check before returning (depth gate — do this every run)

Stop and verify; if any answer is "no", fix it before returning:
- [ ] **Exhaustive enumeration?** Did I *list* ALL the sector's sub-sectors (not just the obvious 3–4)?
      (Listing is cheap; this stays exhaustive.)
- [ ] **Triaged + targeted depth?** Does every sub-sector have **headline economics + a tier**, and the
      **top ~3** the full 9-field A–I with numbers? (Full A–I on *all* only if the user asked for a deep scan.)
- [ ] **Confident in the top-3 pick?** Did I search the **borderline** sub-sectors enough to trust the
      ranking — not deep-dive the wrong 3 off thin triage? (Search weighted to niche/uncertain, ~0 on obvious.)
- [ ] **Stayed in budget?** ~1 search/sub-sector on average (front-loaded on uncertainty) + a few for the
      deep ones — not dozens, and not a worker per sub-sector?
- [ ] **Bad news?** Did I include negative signals (write-downs, stalled projects, payment delays) on the deep ones?
- [ ] **Provenance?** Is every numeric claim tagged 🟢/🔵/⚠️, with the no-live-sources banner if web was off?
- [ ] **Mandate?** Is alignment scored from `aiib-mandate.md` (cited), not memory?
- [ ] **Hand-off?** Are anchors (listed leaders / DFI investees / deal winners) surfaced for Mode S sourcing?
