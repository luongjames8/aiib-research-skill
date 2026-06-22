# Testing the AIIB research skills

Verify three things, separately: **(A) does the right skill trigger**, **(B) is the output correct +
appropriately deep**, and **(C) does it stay cheap / not run away**. Skills aren't invoked every turn —
Claude reads each skill's `description` (always in context) and loads the body only when your request
matches. The three skills form a funnel: **A (sector context) → S (source companies) → B (dossier each).**

## A. Trigger / routing test

Confirm the *right* skill fires (the descriptions are tuned so these don't cross-trigger):

- **Mode A (`aiib-sector-scan`):** "Research the Indonesia renewables sector for AIIB." → should fire A.
- **Mode S (`aiib-company-sourcing`):** "Find private geothermal developers in Indonesia." → should fire S.
- **Mode B (`aiib-company-dossier`):** "Build a dossier on <company>." → should fire B.

Cross-check it does NOT misroute: "find companies in X" → S (not A); "research the X sector" → A (not S);
"profile company Y" → B (not S).

How you see it trigger: **Claude Code** shows the skill invoked and (Mode A/S) spawns Sonnet subagents;
**claude.ai** says it's using the skill (no subagents).

## B. Output test

**Mode A — sector scan:**
- [ ] **Exhaustive ENUMERATION** — all sub-sectors listed (renewables ≈ 8–9), not just the obvious 3–4.
- [ ] **Triaged depth** — every sub-sector has headline economics + an A/B/C tier; the **top ~3** carry
      the full 9-field A–I with real numbers. (Full A–I on *all* only if you asked for a deep/exhaustive scan.)
- [ ] **Negative signals** on the deep ones; **provenance tags** on every number; **mandate cited to aiib.org**.
- [ ] **Anchors** at the end (listed leaders / DFI investees / deal winners) — the hand-off to Mode S.

**Mode S — company sourcing:**
- [ ] List is **mostly PRIVATE / unlisted** operators (the point of this stage), not just listed names.
- [ ] Found via **multiple methods** (graph expansion, fund-following, value-chain, sweep), expanded in
      **rounds** (open-ended) until dry.
- [ ] **Deduped + ranked** (multi-sourced names ranked higher), each tagged how-found + provenance.

**Mode B — company dossier:**
- [ ] **All 7 sections** — background+moat · guidance+catalysts · financials · valuation & scenarios ·
      mandate+ESG · key people+management · risk.
- [ ] **Financials with numbers**, each tagged; missing figures `[not available]`, not invented; judged
      **relative to the sub-sector** baseline.
- [ ] **Mandate verdict** (sector + theme + climate + Strong/Partial/Out, citing aiib.org); fact vs.
      inference separated; a **"Verify before relying"** list.

## C. Cost / runaway test (important — Mode S especially)

The earlier failure mode was a subagent tree blowing up to thousands of calls. Confirm it can't:
- [ ] Subagents are the **purpose-built** types (`subsector-researcher` / `source-expander` /
      `company-dossier-researcher`), **never `general-purpose`** — those can't recurse (no Agent tool).
- [ ] Mode S expanded in **small batched rounds** (~3–4 workers) with a **found-set**, not one big blast,
      and **stopped when dry** / at the round cap — total subagents should be tens, not hundreds.
- [ ] Searches were bounded (WebSearch-first, WebFetch rare). A sector scan should be ~12–18 searches by
      default, not hundreds.

If you can, watch the run (Claude Code `--output-format stream-json`): grep for `"name":"Agent"` (count
should be modest) and `claude-sonnet` (workers should be Sonnet, not Opus).

## D. Provenance / web-search-floor test

Run a prompt with web search **ON** (expect mostly 🟢 `[web: …]`) and **OFF** (expect the
`⚠️ NO LIVE SOURCES THIS RUN …` banner + ⚠️ tags throughout — it must still produce full output, flagged).

## E. Both surfaces

| Surface | Skills | Subagents | Live data | Setup |
|---|---|---|---|---|
| Claude Code — terminal / web | ✓ | ✓ Sonnet fan-out | ✓ yfinance/EDGAR | clone/point at this repo |
| claude.ai chat (Pro/Max/Team/Enterprise) | ✓ | ✗ sequential | ⚠️ network-dependent | upload each `.claude/skills/<skill>/` in Settings → Skills |
| ChatGPT | rebuild as Custom GPT | ✗ | ✗ (sandbox no network) | see `ports/chatgpt-custom-gpt/` |

End-to-end: run **A → S → B** (take an anchor from A into S, a candidate from S into B) on a Claude Code
surface to confirm the funnel + subagent fan-out, and once on claude.ai to confirm the sequential fallback.
