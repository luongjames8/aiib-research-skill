<!--
Example output — aiib-company-sourcing (Mode S), run live 2026-06-23 in a clean Claude Code session.
Seeded with the India-renewables anchors from the Mode-A example. Stats: 121 unique companies (96
private / 25 listed) over 3 iterative rounds (stopped when dry) · 5 methods · 13 source-expander
workers (zero general-purpose — no recursion) · 151 web searches · deterministic dedup via
dedup_candidates.py + LLM judgment-merge pass. Provenance: 31 🟢 / 7 ⚠️. Reproduce: see ../TESTING.md.
Point-in-time snapshot for illustration — not investment advice (see ../README.md).
-->

121 unique companies (96 private, 25 listed) across 3 rounds and 5 methods. Round 3 was effectively dry for the institutional private-developer tier — only a handful of new scale names. Stopping here. Below is the deduped, mandate-screened, **ranked** candidate list.

---

# India Solar (C&I/Rooftop + Utility) — AIIB Private-Candidate Pipeline (Mode S)

**Provenance banner:** 121 deduped companies sourced over 3 iterative rounds via 5 methods (graph expansion · fund-following · value-chain · auction/DFI sweep · local-language), 13 `source-expander` workers. Anchors excluded from ranking (launch points, not discoveries). Tags: 🟢 = multiple/primary sources (DFI press, Mercom league tables, company filings) · 🔵 = single solid source · ⚠️ = thin, verify before dossier. Dedup deterministic via `dedup_candidates.py`; judgment-pass merges noted.

> **Judgment-pass merges** (script left apart, same company): *AmpIn Energy Transition* = *Amp Energy India* (rebrand) · *AM Green* = *AM Green Energy* (one platform; backer attribution conflicting — Greenko-founders/ORIX/GIC confirmed) · *Virescent Infrastructure* = *Virescent Renewable Energy Trust* (KKR InvIT, now IndiGrid) · *Hexa Climate* = *Hexa Climate Solutions*.
> **De-prioritized — no longer independently investable:** O2 Power (→JSW), Ayana (→ONGC-NTPC PSU), Sprng (→Shell), Virescent (→IndiGrid).

---

## TIER 1 — Lead private developers, scale + mandate-fit (dossier these first)

| # | Company | Segment | Status | How-found (method · anchor) | Why (mandate + economics) | Prov |
|---|---------|---------|--------|------------------------------|---------------------------|------|
| 1 | **Sunsure Energy** | C&I / open-access | PRIVATE | graph · CleanMax/FP | Partners Group $400M; 600MWp op, 7.1GWp pipeline; pure C&I offtake — bull's-eye on the priority segment | 🟢 |
| 2 | **Radiance Renewables** | C&I / BTM | PRIVATE | graph · CleanMax/FP | Eversource-promoted pure-play C&I/BTM; FMO+IFU ~$100M equity (Feb '26); ~95% IG offtakers | 🟢 |
| 3 | **AmpIn Energy Transition** | C&I + utility | PRIVATE | graph + fund (Actis/CIP/Sumitomo) | $600M+ raised incl. AIIB, OeEB, FMO; Actis-backed; 3GWp, 17 states; C&I + utility | 🟢 |
| 4 | **Continuum Green Energy** | C&I + utility | PRIVATE | graph · CleanMax/FP | MS Infrastructure; 4.7GWp; 170+ C&I PPAs; DRHP filed (not yet listed) | 🟢 |
| 5 | **Aditya Birla Renewables** | utility + C&I + floating | PRIVATE | fund · GIP/BlackRock | 4.3GW platform; GIP/BlackRock ~$335M minority (Dec '25); Grasim parent — strong sponsor | 🟢 |
| 6 | **Serentica Renewables** | firm/RTC RE for industry | PRIVATE | graph · Adani/ReNew | KKR $650M; dispatchable RE for hard-to-abate; bought Statkraft India 1.4GWp; Sterlite promoters | 🟢 |
| 7 | **Avaada Energy** | utility + group-captive | PRIVATE | graph · multi | 6–7GWp; Brookfield/GPSC-backed; 30GWp 2030 target; one of largest private IPPs | 🟢 |
| 8 | **Juniper Green Energy** | utility + hybrid | PRIVATE | graph · Adani/ReNew | ~10GWp, 48 projects; AT Capital; $350M raised; DRHP filed; ICRA-rated | 🟢 |
| 9 | **Hero Future Energies** | C&I + utility | PRIVATE | graph + fund (IFC/KKR) | KKR $450M + IFC; ~7GW solar+wind; C&I open-access + rooftop | 🟢 |
| 10 | **BrightNight** | utility + hybrid | PRIVATE | sweep · Goldman/ACEN | Goldman Sachs Alt $440M + ACEN $250M; 5.4GW India pipeline; Rajasthan 2GW | 🟢 |
| 11 | **Zelestra (ex-Solarpack)** | utility + C&I | PRIVATE | sweep + fund · EQT | EQT-backed; 5.4GW India pipeline; €132M Rajasthan 435MWdc; C&I in TN | 🟢 |
| 12 | **AM Green** | utility + green-NH₃ | PRIVATE | graph + fund · Greenko-founders/GIC/ORIX | #1 open-access developer 2024; ORIX $730M; GIC/ADIA co-invest; 2.4GWp + green ammonia (large, complex) | 🟢 |
| 13 | **Evren** | utility + hybrid + BESS | PRIVATE | fund · Brookfield | Brookfield + Axis Energy 50:50 JV; 11GW pipeline; $100M ALTERRA+Brookfield ('25) | 🟢 |
| 14 | **Gentari India** | C&I / open-access | PRIVATE | graph + fund · Petronas | Petronas arm (absorbed Amplus); #1 open-access 2025; 3.5GW; **seeking partial stake sale** — live entry point | 🟢 |
| 15 | **Apraava Energy (ex-CLP India)** | utility + C&I | PRIVATE | graph + sweep | CLP + CDPQ owned; ~2GW; BII financing '25; 600MW solar pipeline | 🟢 |

## TIER 2 — Private C&I/rooftop pure-plays (the priority segment; mid-scale, DFI-friendly)

| # | Company | Segment | Status | How-found | Why | Prov |
|---|---------|---------|--------|-----------|-----|------|
| 16 | **Cleantech Solar** | C&I rooftop/open-access | PRIVATE | graph · C&I | SG-HQ, major India C&I; $240M raised; Shell-linked; corporate PPAs | 🟢 |
| 17 | **Vibrant Energy** | C&I open-access | PRIVATE | graph · Adani/ReNew | INOXGFL subsidiary; 1.9GW+ AUM; Amazon/Coca-Cola/UltraTech offtakers | 🔵 |
| 18 | **Roofsol Energy** | C&I rooftop | PRIVATE | sweep · C&I | #2 rooftop installer '24; Rs2.1bn from Aseem Infra Finance ('25); industrial C&I | 🟢 |
| 19 | **Orb Energy** | C&I + SME rooftop | PRIVATE | DFI · C&I | FMO/DEG/DFC/Shell-backed; $48M Series D ('24); rooftop + SME solar finance | 🟢 |
| 20 | **Candi Solar** | C&I / BTM rooftop | PRIVATE | graph + fund · IFC/Norfund | IFC-led $58.5M debt; Norfund $20M; top-3 rooftop; India + South Africa | 🟢 |
| 21 | **SolarSquare** | residential + C&I rooftop | PRIVATE | sweep · M&A | Lightspeed/B Capital; ~$450–500M val; raising $60M ('26); fast-growing | 🟢 |
| 22 | **Statkraft BLP Solar Solutions** | C&I rooftop + ground | PRIVATE | fund · Statkraft | Statkraft+BLP JV; Statkraft divesting India RE — **M&A target** | 🔵 |
| 23 | **Bharat Light & Power (BLP)** | solar + wind | PRIVATE | fund · Statkraft/Shell | Bangalore IPP (2010); standalone behind Statkraft-BLP JV | ⚠️ |
| 24 | **Mahindra Susten** | C&I + utility EPC/IPP | PRIVATE | sweep · NTPC/GUVNL | Mahindra arm; 1.55GWp+ IPP; 560MWp commissioned '25; Rs14.5bn debt | 🟢 |
| 25 | **Enerparc India** | C&I rooftop EPC/IPP | PRIVATE | graph · C&I | Enerparc AG (Germany) India arm; OPEX/CAPEX models; parent-funded | 🔵 |
| 26 | **Kalpa Power** | C&I rooftop/open-access | PRIVATE | sweep · C&I | Top rooftop installer rankings '24; C&I PPA specialist | ⚠️ |

## TIER 3 — Niche segments (floating · agrivoltaic · green-H₂ captive solar)

| # | Company | Segment | Status | How-found | Why | Prov |
|---|---------|---------|--------|-----------|-----|------|
| 27 | **Floatex Solar** | floating solar | PRIVATE | segment | India floating pure-play; 1GW+ executed; NTPC Ramagundam 130MWp | 🟢 |
| 28 | **Ciel & Terre India** | floating solar | PRIVATE | segment | French leader's India arm; 259MW+; 120MWp Omkareshwar (SJVN); local float mfg | 🟢 |
| 29 | **Hygenco Green Energies** | green-H₂ + captive solar | PRIVATE | segment | First commercial green-H₂; 1,125MW captive RE Odisha; Tata Steel SEZ JV | 🟢 |
| 30 | **TrueRE / Oriana (green ammonia)** | green-NH₃ + captive solar | PRIVATE | segment | SIGHT award; Rs3,135Cr SECI ammonia offtake; 1GW solar + 800MWh BESS | 🔵 |
| 31 | **Megha Engineering (MEIL)** | canal-top / KUSUM solar | PRIVATE | segment | World's first canal-top solar; 618MW BESCOM PPA; 76 PM-KUSUM plants | 🔵 |
| 32 | **Shapoorji Pallonji Infra Capital** | floating + utility solar | PRIVATE | segment | SP Group; won India's first large floating solar (Rihand) | 🔵 |

## TIER 4 — Private long-tail (recent auction/tender winners; smaller, regional)

Onix Renewable 🟢 (NHPC L1 @₹3.09, 7GW park pipeline) · Jindal Renewables 🟢 (~3GW, SJVN 300MW) · Hindustan Power 🔵 (UPPCL 435MW) · OMC Power 🟢 (UP minigrids; Kansai T&D 10% '26) · Sunbridge Solar 🔵 (MPUVNL 471MW) · Kosol Energie 🔵 (AP rooftop 291MW) · Sadbhav Futuretech 🔵 (AP rooftop; solar pumps) · Onward Solar 🔵 (TNGECL BESS) · Eagle Infra 🔵 (TNGECL BESS) · Diwakar Renewable 🔵 (RVUNL BESS) · Mecpower 🔵 (RVUNL BESS) · Purvah Green 🔵 (CESC subsidiary) · Hexa Climate 🔵 (NTPC FDRE) · Hinduja Renewables 🔵 · Eden Renewables (TotalEnergies/GreenYellow JV) 🔵 · UPC Renewables India 🔵 · Vena Energy India (GIP) 🔵 · Vector Green (→Sembcorp) 🔵 · Solairedirect India (ENGIE) 🔵 · Solarcraft 🔵 · Rays Power Infra 🔵 · SunSource Energy (→SHV) 🔵 · Freyr/Oorjan/MYSUN/ZunRoof/SunEdison Infra India (residential/rooftop micro) 🔵 · Oorja/Claro (agri-solar micro) 🔵 · Pahal Solar 🔵 · EDF Renewables India ⚠️ · Navayuga Renewable ⚠️ · H2e Power ⚠️.

## TIER 5 — Value-chain / suppliers (mandate-adjacent; fundable but not core AIIB equity)

- **EPC / O&M:** Hartek Solar 🟢 (top-5 EPC + top-3 rooftop) · Inspire Clean Energy 🟢 (top-4 O&M) · Mahindra Teqo 🔵 (O&M) · Amara Raja Infra 🔵 *(listed parent)*
- **Modules / cells (PLI):** *PRIVATE* — Goldi Solar 🔵 · Saatvik Green (DRHP) 🔵 · Rayzon (DRHP) 🔵 · Gautam Solar 🔵 · RenewSys (integrated) 🔵 · Navitas 🔵 · Indosol (Brookfield eyeing) 🔵 · Pahal. *LISTED* — Waaree, Vikram, Premier, Emmvee, Insolation.
- **Trackers / BESS / inverters:** Sunchaser Structures 🟢 · Strolar 🔵 · NewEnergie 🔵 · Statcon Energiaa 🔵 · Cygni Energy 🔵 · SunGarner 🔵

## Reference — Listed (de-prioritized per private-bias; benchmarks/context only)
Adani Green · ReNew · Acme Solar · Tata Power Renewable · NTPC Green · Torrent Power · KPI Green · Refex Energy · JSW Neo Energy · Reliance NU Suntech/Energies · Sterling & Wilson · Sembcorp Green Infra · Bondada Engineering · OPG Power · Ceigall India · Dilip Buildcon · Waaree Renewable · Oriana Power (SME) · Zodiac Energy (SME) · Azure Power (CDPQ, delisted — distressed, ⚠️).

---

### Hand-off to Mode B (aiib-company-dossier) — dossier these first

The five best **private, scale, mandate-fit, and segment-priority** picks:

1. **Sunsure Energy** — purest C&I play at scale, fresh Partners Group capital.
2. **Radiance Renewables** — pure C&I/BTM, just DFI-funded (FMO/IFU); textbook AIIB co-invest.
3. **Aditya Birla Renewables** — newest large platform, GIP/BlackRock validation, strong sponsor.
4. **Serentica Renewables** — firm/dispatchable RE for industry (the structural growth story), KKR-backed.
5. **Gentari India** — **actively seeking a partial stake sale right now**, #1 open-access 2025 — a live entry point.

Runners-up worth early dossiers: **AmpIn**, **Continuum**, **BrightNight**, **Zelestra**, **Avaada**.

**Method note:** rounds went 42 → +53 → +26 new names; Round 3's net-new was dominated by micro long-tail and listed infra (only ABREN, BLP, Floatex, Hygenco added at the institutional-private tier), so I stopped at the round cap with the relevant tier dry. Raw artifacts in `/tmp/aiib-sourcing-india-solar/` (`round{1,2,3}.json`, `dedup_all.json`).

Want me to kick off Mode B dossiers on the top 5 (parallel `company-dossier-researcher` subagents), or expand any tier further?
