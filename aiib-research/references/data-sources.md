# Data Sources — tiered strategy

This tool has a **web-search floor** and an **optional structured-data layer**. Use the richest tier
available in the current environment; always fall back gracefully; tag every figure by provenance
(see `provenance.md`).

## Tier 1 — free structured data (preferred, when a code tool + network are available)

When you have a **code-execution tool with network access** (Claude Code; or claude.ai if its sandbox
has network), pull hard numbers directly from these **free, no-API-key** sources instead of eyeballing
them from web pages. Tag the result 🟢 with the source + as-of date.

- **yfinance** (Yahoo Finance) — financials, fundamentals, prices, key ratios, comparables. Free, no
  key. Broad **international** coverage via exchange suffixes — ideal for AIIB markets:
  `.JK` Jakarta · `.BK`/`.BKK` Bangkok · `.NS`/`.BO` India · `.SA` São Paulo · `.SN` Santiago ·
  `.IS` Istanbul · `.VN`/`.HM` Vietnam (coverage varies) · `.HK` Hong Kong. A bundled helper script,
  `aiib-research/scripts/fetch_financials.py`, wraps this — prefer it over re-writing yfinance calls each run.
- **SEC EDGAR** — US filings (10-K/10-Q/8-K) + the `data.sec.gov` company-facts JSON API. Free, no key.
  Use for any **US-listed** company or comp; limited for the many non-US AIIB targets.
- **stooq** — free historical prices with decent international coverage; a good cross-check / fallback
  when a ticker is thin on Yahoo (`https://stooq.com/q/d/l/?s=<ticker>&i=d`).
- **OpenBB** (`pip install openbb`) — aggregates many **free** providers (yfinance, SEC, etc.) behind one
  Python API (`from openbb import obb; obb.equity.fundamental.metrics("AAPL")`). Optional convenience
  layer. **License note:** OpenBB is **AGPL-3.0** — it is NOT bundled in this repo; only invoked at
  runtime if the user already has it installed. yfinance + EDGAR cover the same free ground without the
  copyleft consideration, so prefer them unless OpenBB is already present.
- **FRED** (macro: rates, FX, inflation) — free but needs a free API key; use only if the user provides one.

How to use Tier 1: run `python aiib-research/scripts/fetch_financials.py <TICKER>` (one or more tickers), parse the JSON, and build
the Financials + peer-comparison + valuation inputs from real numbers. **The script auto-installs yfinance
on first use** (a one-time quiet `pip install`), so no setup is needed — just run it. The subagents that
need this (`subsector-researcher`, `company-dossier-researcher`) have the Bash tool for exactly this; they
do NOT have the Agent/Task tool, so they still can't spawn subagents (Bash is for this script only). Only
if the script prints `unavailable` (sandbox blocks pip/network, e.g. claude.ai) drop to Tier 0 (web).

## Tier 0 — web-search floor (always available as fallback)

When no code tool or no network: gather everything from **web search** — company filings, earnings
releases, investor presentations, analyst coverage, news. Cite each source 🟢 `[web: source, date]`.
This is the methodology's baseline and works on every surface.

## Tier −1 — no live access at all

If neither web nor code/data is available this run, still produce the full output **from model
training**, tag every claim ⚠️ `[training — unverified]`, and lead with the no-live-sources banner
(`provenance.md`). Never present an untagged training-memory number as if it were sourced.

## Reality check for AIIB markets

Many AIIB targets are **private, project-level, or thinly-covered emerging-market** companies with no
structured feed. Expect Tier 1 to return little for them — that is normal. Fall to web search +
primary filings, and mark genuinely missing figures `[not available]` rather than inventing them.

## Attribution

The fundamental + qualitative analysis framework adapts the open-source, MIT-licensed
**claude-equity-research** project (https://github.com/quant-sentiment-ai/claude-equity-research),
reframed for AIIB-style direct/PE infrastructure investing (the public-equity trading apparatus —
technicals, options flow, 12-month price targets — is intentionally omitted as out of scope).
