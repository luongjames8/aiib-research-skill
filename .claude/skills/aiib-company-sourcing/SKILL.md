---
name: aiib-company-sourcing
description: >-
  Mode S of AIIB-style investment research: source the companies. Given a sub-sector (with its economics) or a
  country and sector, produce a ranked list of mostly-PRIVATE, mandate-fit companies — by graph-expanding from
  anchors (a company's competitors, suppliers, customers, JV partners, PE/DFI fund-siblings), following DFI/PE
  fund portfolios, decomposing the value chain, and sweeping deal trackers, PPP pipelines, credit-rating lists,
  and local-language sources. Use whenever the user wants to find, discover, source, or build a pipeline or
  longlist of companies or deal targets — e.g. "what companies should I look at in Vietnam offshore wind", "find
  private solar developers in Indonesia", "who competes with this company", origination or deal-sourcing — even
  without the word "sourcing". This is the MANY-company discovery step; to deep-dive ONE named company use Mode
  B (aiib-company-dossier). Sits between Mode A and Mode B. Uses subagents when available.
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

**Dedup the anchors BEFORE Step 2** (this is what stops successive rounds re-chasing Star Energy / Salak).
Normalize each name — strip legal/suffix noise (`PT`, `Tbk`, `Group`, `Bhd`, `PLC`, `Pvt`, `Ltd`,
`Holdings`), lowercase, and merge obvious variants ("Star Energy", "PT Star Energy Geothermal", "Star
Energy Group" → one). These dedup'd anchors are the **launch points for Step 2's first round** — from
there the iterative **found-set** (Step 2) is the shared state that keeps later rounds from re-searching
names already discovered.

### Step 2 — Expand ITERATIVELY, in rounds, until dry
Sourcing is **open-ended** — you don't know how many companies exist — so expand in **rounds** carrying a
running **found-set**, NOT one big parallel blast. Each round finds names the previous rounds missed and
is told what's already found, so **no search is wasted re-discovering known names**. The methods
(`references/sourcing-methods.md`): graph expansion (competitors, suppliers, customers, JV partners,
PE/DFI fund-siblings), fund-following, value-chain decomposition, source sweep, local-language mining.

**The loop — the orchestrator owns it (this is the safe place for the recursion):**
1. **Seed.** `found = {}` (the deduped anchors from Step 1 are your round-1 launch points).
2. **Round.** Spawn a **small batch (~3–4)** of `source-expander` workers, each given: one anchor/method
   to expand **and the current `found` list**, with the instruction *"return only companies NOT already
   in this list."*
3. **Dedup** the round's returns into `found` (`scripts/dedup_candidates.py`).
4. **Decide.** If the round added **≥ ~3 new names**, run another round — expand from the most promising
   **new** names + any method/value-chain link not yet worked. If it added **< ~3 (dry)** or you've hit
   the budget, **stop.**

⛔ **`subagent_type: source-expander` ONLY — NEVER `general-purpose`.** general-purpose has the Agent tool
and workers re-delegate into a runaway tree (one real run hit ~2,800 calls / 174 agents); source-expander
has **WebSearch/WebFetch/Read only — no Agent tool — so it can't recurse.** The ORCHESTRATOR loops; the
workers never do.

**Bounds (keep it safe):** small batch per round (~3–4 concurrent, not all anchors at once) · per-worker
budget "**max ~10 searches; WebSearch first; WebFetch only when a snippet won't do**" (WebFetch is
expensive + often 403s) · **round cap ~4–5** even if not fully dry. On **claude.ai** (no subagents) run
the same rounds sequentially yourself, within the budget.

### Step 3 — Final DEDUP, screen, rank
After the rounds, your **found-set** holds the accumulated candidates (already deduped between rounds).
Give it a **final dedup by normalized name** + judgment pass. A name surfaced by **multiple**
anchors/methods/rounds collapses to **ONE entry** — record that it was multi-sourced: that overlap is a
**strength signal** (rank it higher), not a duplicate to discard.

**In Claude Code, dedup deterministically — don't eyeball it.** Have each worker return its candidates
as a JSON array (`{"name","anchor","method","private","provenance"}`), concatenate all workers' arrays
into one file, and run `scripts/dedup_candidates.py` (`cat all.json | python scripts/dedup_candidates.py`).
It normalizes names (strips `PT`/`Tbk`/`Group`/`Ltd`/… noise, lowercases), merges duplicates across
workers, ranks multi-sourced names first, and emits one entry per company. It is **conservative** — it
will NOT merge `X` with `X Geothermal` (possible parent/subsidiary), so do a quick **judgment pass** to
combine the obvious same-company near-dupes it left apart (e.g. acronyms — `BREN` = `Barito Renewables`).
On **claude.ai** (no filesystem/subagents), do the dedup by hand with the Step-1 normalization rule. Then apply a **light** mandate-fit gate (`references/aiib-mandate.md`
— drop clearly out-of-mandate names; full scoring is the dossier's job). **Bias to PRIVATE / unlisted**
operators. Rank by mandate fit + multi-source overlap + sub-sector attractiveness + signs of
scale/fundability (rated, DFI-backed, recent raise).

## Output structure
A **ranked candidate table**, plus a provenance banner. Each row:
`Company · sub-sector · listed/PRIVATE · how-found (method + anchor) · one-line why (mandate + economics) · provenance`.
Lead with the private names. This list is the input to **aiib-company-dossier** (Mode B) — note the top
few worth dossiering first.

## Self-check before returning
- [ ] Did I expand in **rounds with a found-set** (each round told what's already found), not one blast —
      and stop when a round went **dry** (or at the round cap)?
- [ ] Did I expand via **multiple** methods (graph + funds + value-chain + sweep), not one?
- [ ] Workers were `source-expander` (NEVER general-purpose), small batch per round?
- [ ] Is the list **mostly PRIVATE / unlisted** operators (the point of this stage)?
- [ ] Deduped, light-mandate-screened, and **ranked** (not a raw dump)?
- [ ] Every candidate tagged with how-found + provenance (🟢/🔵/⚠️)?
- [ ] Flagged the top few to dossier first (hand-off to Mode B)?
