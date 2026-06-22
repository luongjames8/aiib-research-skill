# Provenance Tagging

Every factual claim in output MUST carry a provenance tag. This is non-negotiable for an investment
research tool: a stale or invented financial figure presented as fact is dangerous. Tags make the
source of each claim visible so the reader knows what to trust and what to verify.

## The three tags

- 🟢 **`[web: <source>, <date>]`** — retrieved live this run from a web search or fetched page. Name
  the source (publication / org / filing) and its date. Strongest.
- 🔵 **`[connector: <name>]`** — from a connected data source / MCP connector / uploaded file the user
  provided this session. Name it.
- ⚠️ **`[training — unverified]`** — from model background knowledge, NOT checked against a live source
  this run. May be **stale (cutoff)**, **approximate**, or **wrong**. The reader MUST verify before
  relying. Use this honestly and often — never dress a training-memory figure as if it were sourced.

## Rules

1. **Default to ⚠️ when unsure.** If you can't point to a 🟢/🔵 source for a specific number, it is ⚠️.
2. **Numbers especially.** Every quantitative claim (capacity, IRR, tariff, revenue, multiple, headcount)
   gets a tag. Unsourced numbers in an investment dossier are the failure mode this tool exists to prevent.
3. **No web access this run?** (claude.ai network is settings-dependent and may be off.) Still produce
   the full output — but tag essentially everything ⚠️ and add a top banner:
   `⚠️ NO LIVE SOURCES THIS RUN — all claims are from model training and must be independently verified.`
4. **Section provenance summary.** End each major section with a one-line mix, e.g.
   `Provenance: 6 web · 0 connector · 3 training-unverified.` so the reader sees the ratio at a glance.
5. **Recency flag.** When a 🟢 source predates the current quarter, note it: `[web: IEA, 2024 — may be stale]`.
