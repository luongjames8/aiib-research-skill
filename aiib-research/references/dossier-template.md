# Company Dossier Template

The dossier structure: the **5 core sections** plus **2 analytical sections** (Valuation & scenarios,
Risk) adapted from institutional equity-research practice for AIIB-style direct/PE infrastructure
investing. Produce every section; tag every claim by provenance (`provenance.md`); pull hard numbers
from Tier-1 free data when available (`data-sources.md` + `aiib-research/scripts/fetch_financials.py`), else web search.
This is an investment-screening artifact: missing data is flagged, never fabricated.

**Judge the company relative to its sub-sector.** Numbers are only meaningful against the sub-sector
baseline from the sector scan (or your quick sketch): a 60% EBITDA margin is strong in one sub-sector and
weak in another. Throughout — Financials, Valuation, Risk — state where the company sits **vs. its
sub-sector norm** (above/below margin, cheap/dear vs. comps, exposed/insulated to the sub-sector's key
risks). That relative read is what makes the dossier decision-useful.

**Adapted, not copied:** the public-equity *trading* apparatus (technical analysis, options flow, a
12-month BUY/SELL/HOLD price target) is intentionally **omitted** — AIIB makes conviction-based direct
investments, not trades. Keep the conviction + mandate-fit framing, not a trading rating.

**Private / unlisted companies are the norm here — research them deliberately.** Most AIIB targets have
no ticker and no Yahoo/EDGAR feed, so `fetch_financials.py` returns nothing — that is expected, not a
dead end. Pull what *does* exist, each tagged:
- **Credit-rating reports & bond prospectuses** (Pefindo / CRISIL / ICRA / Fitch / Moody's) — these
  routinely publish financials, leverage, and business detail for *private* infra issuers. Best single
  source of hard numbers on an unlisted operator.
- **DFI disclosure** (IFC project portal, ADB, FMO, etc.) — project summaries give deal size, sponsors,
  and sometimes returns/financials for companies these banks have backed.
- **Company website / press / investor decks**, **regulatory & PPP filings**, **company-registry
  filings** (annual accounts in many jurisdictions), **news & deal trackers** (DealStreetAsia, IJGlobal).
- **Key people** — LinkedIn, Crunchbase, company "about"/leadership pages, news.
- **User-uploaded data** — if the user attaches accounts/a deck, use it (🔵 `[uploaded: file]`).
Listed *peers* still anchor the valuation (comps) even when the target itself is private. Mark genuinely
absent figures `[not available]` — a thin but honest private dossier is the correct output.

## 1. Background

What the company is and does. Founding / ownership (listed? PE-backed? state-owned? family?),
parent/group, geographies, core business lines, scale (employees, asset base), and **position in the
value chain**. Then a **competitive-positioning / moat** read: market share, durable advantages
(scale, concession rights, network, cost), and whether the moat is widening or eroding.

## 2. Forward guidance & catalysts

The forward-looking picture: management guidance, stated strategy & expansion pipeline, capex plans,
target markets/sub-sectors, **analyst consensus** (revenue/EPS where covered), and **capital-allocation
priorities** (dividends, buybacks, capex, M&A). Then **catalysts**: near-term (0–6 mo — earnings,
contract/auction wins, financial close) and medium-term (6–24 mo — pipeline conversion, policy
changes). Distinguish **company-stated** (cite source/date) from **your inference**; if no guidance
exists, say so — don't invent targets.

## 3. Financials

Real numbers, each tagged; prefer the Tier-1 yfinance pull (`aiib-research/scripts/fetch_financials.py <ticker>`)
for listed names, else filings/web. Cover:
- **Performance** — revenue growth (YoY/QoQ), margins (gross / operating / EBITDA / net) **with
  historical trend**, net income, **earnings quality** (GAAP vs. adjusted, one-time items).
- **Balance sheet & cash** — leverage (net debt / EBITDA), debt maturity profile, liquidity, free cash
  flow, capital intensity (capex / revenue).
- **Funding** — recent rounds / bond issuance / credit ratings (Pefindo, CRISIL, Fitch, etc.).
- **Peer-comparison multiples** — vs. sector median: P/E (trailing + forward), EV/EBITDA, P/S, P/B, and
  sector-specific metrics. Present as a small comp table.
Note reporting period + currency. **Private / project companies: expect gaps — mark `[not available]`,
never guess.**

## 4. Valuation & scenarios

Where data supports it: **comparable-company** (peer multiples applied), **precedent-transaction**
(sector M&A multiples), and **DCF** (FCF projection + WACC + terminal value, with the key assumptions
stated). Then **scenario analysis** — bull / base / bear with **probability weights** (e.g. 25/55/20),
each naming its growth/margin/execution assumptions. For private or infra-project targets, express the
output as **investment conviction** (High / Medium / Low) anchored to a value range and IRR, **not** a
12-month share-price target. State explicitly when data is too thin for a real valuation.

## 5. AIIB-mandate alignment (incl. ESG)

Score against the mandate using `aiib-mandate.md` (cite `[ref: aiib-mandate.md]`):
- **Sector match** — which of AIIB's 6 sectors (or "other productive sectors") + why.
- **Theme match** — which of the 4 thematic priorities + the specific reason.
- **ESG** — Environmental (carbon/transition + physical climate risk; **Paris alignment**, given AIIB's
  >50% climate target), Social (community/stakeholder, safeguards), Governance (covered in §6).
- **Verdict** — `Strong fit` / `Partial fit` / `Out of mandate`, with the bear case (why AIIB might pass).

## 6. Key people & management quality

Founders, CEO, CFO, chair, notable board, major shareholders — name, role, one-line background (prior
firms, track record, red flags). Then a **management-quality** read: execution track record,
**capital-allocation discipline**, compensation alignment, and **governance / board effectiveness**
(independence, related-party exposure, PE-sponsor control). If names can't be verified live, tag ⚠️.

## 7. Risk assessment

- **Company-specific** — operational (execution, key-person, technology/obsolescence, supply chain),
  financial (leverage, refinancing, liquidity, FX/commodity exposure), regulatory/legal (licensing,
  litigation, IP, tariff/offtaker risk).
- **Macro** — for the company's markets: economic cycle, interest-rate sensitivity, currency, commodity,
  policy. Name the specific transmission, not generic risk words.

## Quality rules

- **Every section ends with a provenance summary line** (provenance.md rule 4).
- **Never fabricate** financials, guidance, valuation, or people. Missing = `[not available]` / ⚠️.
- **Separate fact from inference** — label analytical judgments distinctly from sourced claims.
- **Adapt to the company** — a thinly-covered private infra firm yields a short dossier honestly; a
  listed operator yields a full one. Don't pad, don't invent.
