# A–I Sub-Sector Deep-Dive Template

The depth bar for each sub-sector. A one-paragraph "economics summary" is a FAILURE — produce all nine
fields with ACTUAL NUMBERS where available, every claim provenance-tagged (see provenance.md). Mirrors
the methodology proven on the meridian deal-sourcing claw.

For **each** sub-sector, produce:

- **A. Market economics** — market size (capacity in MW/GW, or USD revenue), growth rate, demand
  drivers (structural vs. policy-dependent). *Primary sources:* the national/sector **plan or regulator
  data** (e.g. India NEP/RUPTL, Indonesia RUPTL/PDP, Vietnam PDP8, the energy ministry / regulator site),
  not a news summary of it.
- **B. Pricing & tariff (ACTUAL NUMBERS)** — PPA / auction-clearing / FiT / regulated rates in local
  currency + USD (¢/kWh, rents $/sqm, tolls /km, $/rack, etc.), 3-year trend, regulated vs. market-set.
  *Primary sources:* the **tariff order / regulator ruling** (CERC, state ERCs, etc.) and the **actual
  auction/tender result notification** (SECI, PLN, EVN/DPPA, the relevant agency) — cite the order/auction,
  not a secondary article quoting it.
- **C. Margin structure** — actual EBITDA margins operators earn; cost structure (capex per unit, O&M,
  land, grid/connection); compressing or expanding.
- **D. Revenue quality** — % contracted vs. merchant, contract/lease tenor, offtaker identity + payment
  track record + curtailment data, counterparty credit.
- **E. Valuation & cycle** — pull the **2–3 most relevant** listed comparables (ticker, EV/EBITDA, P/E, P/B, revenue
  growth, 52-wk range) as a **comp table** + private-transaction comps; where multiples sit vs. history;
  capital-flow direction. *Primary sources:* the **`fetch_financials.py` (yfinance) pull** for the listed
  multiples (🟢, not eyeballed) and **company annual reports / investor decks** for the detail.
- **F. Track record & realized returns** — who has invested in this market/sub-sector, at what
  valuations, exits, **blow-ups / write-downs**, actual realized IRRs. **Search specifically for NEGATIVE
  signals** — do not cherry-pick. *Primary sources:* **company filings, fund/DFI disclosures, exchange
  announcements, credit-rating actions** — the document that records the write-down/exit, not a recap.
- **G. IRR estimation** — levered equity IRR for a new project (state assumptions: leverage %, cost of
  debt, hold years, exit multiple) + sensitivity to tariff/capex.
- **H. Key risks (specific, named)** — curtailment, grid bottlenecks, offtaker financial health,
  regulatory change, land/permitting — named for this market, not generic.
- **I. Competitive landscape** — top ~5 players, market share, consolidating vs. fragmenting, whether
  returns are being competed away; name parents / PE backers.

## Quality rules

- **Numbers, not adjectives.** "High margins" is a failure; "EBITDA ~75% [web: company FY24, 2025]" is the bar.
- **Prefer PRIMARY sources, and cite them.** Go to the source document — tariff order, auction-result
  notification, national plan, company filing, rating action, the `fetch_financials.py` pull — not a news
  article *about* it. Use WebFetch to read the actual order/filing when WebSearch surfaces it. A news
  recap is acceptable only as a pointer or when the primary doc isn't reachable; tag which one you used.
- **Include the bad news** (F especially) — write-downs, stalled projects, payment delays, policy reversals.
- **Tag every claim** (provenance.md). Unsourced numbers → ⚠️ training-unverified.
- **Tier each sub-sector** A/B/C on investability with a one-line reason (e.g. "Tier C — tariff below
  bankability; no PE precedent").
