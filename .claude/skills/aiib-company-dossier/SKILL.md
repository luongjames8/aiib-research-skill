---
name: aiib-company-dossier
description: >-
  Mode B of AIIB-style investment research: turn a company into a structured, sourced investment dossier.
  Given a company (optionally with sub-sector context, or a candidate from the aiib-company-sourcing list),
  produce a structured dossier — background + competitive moat, forward guidance & catalysts, financials
  (margins, earnings quality, peer multiples), valuation & bull/base/bear scenarios, AIIB-mandate
  alignment incl. ESG (vs. the 6 sectors + 4 thematic priorities), key people & management quality, and
  risk assessment — pulling free structured financial data (yfinance / SEC EDGAR) when a code tool is
  available and falling back to web search otherwise, with every claim provenance-tagged so unverified
  figures are visible. Use this whenever the user wants a company deep-dive,
  investment dossier, due-diligence brief, company profile, or to assess a company as an investment —
  especially for infrastructure / development-finance / emerging-market investing, or when they hand over
  a candidate from the aiib-company-sourcing skill (Mode S). Trigger even if they never say "dossier" or
  "AIIB" — e.g. "is <company> a good investment", "research <company> for me", "profile <company>",
  "what's the investment case for <company>". This skill is ONE named company at a time; for a SECTOR use
  Mode A (aiib-sector-scan) and for a LIST of companies to look at use Mode S (aiib-company-sourcing).
  Web-search floor; uses subagents when available, runs sequentially when not.
---

# AIIB Company Dossier (Mode B)

Top-down funnel, final stage: **company → structured investment dossier.** Consumes candidates from the
**aiib-company-sourcing** skill (Mode S) and uses the sub-sector economics from **aiib-sector-scan**
(Mode A) as screening context — or runs standalone on any named company.

Integrity is the whole point. This dossier feeds an investment decision, so a confidently-stated wrong
number is worse than an honest gap. A private company with thin public data yields a thin dossier — that
is the correct output, never a reason to invent. Mark missing figures `[not available]`, tag every claim
by source, and keep your own inferences visibly separate from sourced facts.

## Inputs

- **Required:** a company name.
- **Optional:** country / sector / sub-sector context (improves disambiguation and mandate scoring),
  or a candidate from Mode S sourcing. Multiple companies → produce one dossier each.

## Workflow

### Step 1 — Resolve the company + load sector context + pull data
Confirm which entity (disambiguate by country/sector; identify parent/group and listing status).
**Load the sub-sector context.** A company is only judged *relative to its sub-sector* — its margins,
IRR, tariffs, and risks mean nothing without the sub-sector baseline. If a Mode-A (aiib-sector-scan)
result exists for this company's sub-sector, carry its economics in (tariff range, typical EBITDA/IRR,
cycle, key risks, listed comps, competitive landscape). If not, do a **quick sub-sector economics
sketch first** (a few searches: tariffs, typical margins/IRR, main risks) so you have a yardstick.
**Get the best data tier available** (`references/data-sources.md`): if you have a code tool with
network, pull free structured financials with `scripts/fetch_financials.py <ticker>` (yfinance — works
for international tickers via exchange suffixes, e.g. `PGEO.JK`); if it returns `unavailable`, or for
private/unlisted names, fall back to web search of filings/earnings. Tag everything by provenance.

### Step 2 — Produce the dossier
Follow `references/dossier-template.md` — the **5 core sections + 2 analytical sections** (Valuation &
scenarios, Risk), adapted from institutional equity research for AIIB direct/PE investing:
1. **Background** (+ competitive moat) · 2. **Forward guidance & catalysts** · 3. **Financials** (margins
with history, earnings quality, cash flow, peer-comparison multiples) · 4. **Valuation & scenarios**
(comps / precedent / DCF + bull-base-bear, expressed as conviction not a price target) · 5. **AIIB-mandate
alignment incl. ESG** (cite `references/aiib-mandate.md`) · 6. **Key people & management quality** ·
7. **Risk assessment** (company-specific + macro). The template has the full spec for each.

**Delegation — REQUIRED when a subagent tool exists (Claude Code).** If you have a Task/subagent tool,
you **must** delegate: spawn one `company-dossier-researcher` subagent **per company** (they run on
Sonnet — cheap + parallel) and let *them* do the web searches and data pulls; then assemble. **Pass each
worker the sub-sector economics as context** (from Step 1 — tariff range, typical EBITDA/IRR, cycle, key
risks, comps) so it screens the company *within* its sector reality, not in a vacuum. **Do NOT run the
research yourself in the main context** — as the orchestrator you only resolve the company(ies), load the
sector context, spawn one Sonnet worker each (with that context), and assemble their returns, so the
expensive orchestrator model stays out of the token-heavy searching. For a single company you may still delegate the whole dossier to one
worker. Only when **no** subagent tool exists (claude.ai chat app) do you produce the dossier(s)
sequentially in this context. Identical output — the difference is cost and speed. **Cap the fan-out:**
at most **~6 workers concurrently** — more companies than that, dispatch in waves. Fan-out stays **one
level deep** (workers return data, never spawn their own subagents) to avoid rate-limit storms.

### Step 3 — Verify & flag
Re-read the dossier for any untagged numbers (→ ⚠️) and any fabricated-looking specifics. Add the
section provenance summaries. Surface the biggest open verification items at the end.

## Output structure

Per company: a header (name + one-line identity + provenance banner) then the **seven sections in order**,
each ending with a provenance summary line, then a short **"Verify before relying"** list of the
highest-risk unsourced claims.

## Self-check before returning (depth gate — do this every run)

Stop and verify; if any answer is "no", fix it before returning:
- [ ] **All 7 sections** present (background+moat · guidance+catalysts · financials · valuation & scenarios · mandate+ESG · people+mgmt quality · risk)?
- [ ] **Best data tier used?** Tried `fetch_financials.py` (or filings) before settling for web/training?
- [ ] **Financials with numbers**, each tagged — and every missing figure marked `[not available]`, not invented?
- [ ] **Mandate** scored from `aiib-mandate.md` (cited): sector + theme + climate + Strong/Partial/Out verdict?
- [ ] **Provenance** on every claim (🟢/🔵/⚠️), with the no-live-sources banner if web was off?
- [ ] **Fact vs inference** separated; a "Verify before relying" list of the riskiest unsourced claims included?
