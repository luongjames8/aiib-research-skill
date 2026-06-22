#!/usr/bin/env python3
"""Fetch free structured financials for a ticker via yfinance.

Usage:  python fetch_financials.py <TICKER>
Example: python fetch_financials.py PGEO.JK   (Pertamina Geothermal, Jakarta)

Prints a JSON object to stdout. On success: status="ok" with the financial data.
If yfinance isn't installed or there's no network / no data, prints status="unavailable"
with a reason — the skill should then fall back to the web-search floor (see
references/data-sources.md). Never raises; always prints parseable JSON.

yfinance is Apache-2.0 and free (no API key). International tickers use exchange suffixes
(.JK Jakarta, .BK Bangkok, .NS India, .SA Sao Paulo, .SN Santiago, .IS Istanbul, .HK Hong Kong).
"""
import json
import sys


def _unavailable(reason):
    print(json.dumps({"status": "unavailable", "reason": reason}))
    sys.exit(0)


def main():
    if len(sys.argv) < 2:
        _unavailable("no ticker argument (usage: fetch_financials.py <TICKER>)")
    ticker = sys.argv[1].strip()

    try:
        import yfinance as yf
    except Exception:
        _unavailable("yfinance not installed — run `pip install yfinance` if the environment allows, "
                     "otherwise use the web-search floor")

    try:
        t = yf.Ticker(ticker)
        info = getattr(t, "info", {}) or {}
        if not info or info.get("regularMarketPrice") is None and not info.get("longName"):
            _unavailable(f"no data returned for '{ticker}' (bad ticker, no coverage, or no network)")

        def frame_to_records(df, limit_cols=4):
            # yfinance returns a DataFrame (rows=line items, cols=periods); keep most recent few.
            try:
                if df is None or getattr(df, "empty", True):
                    return None
                df = df.iloc[:, :limit_cols]
                return {str(c.date()) if hasattr(c, "date") else str(c):
                        {str(k): (None if v != v else v) for k, v in df[c].items()}
                        for c in df.columns}
            except Exception:
                return None

        out = {
            "status": "ok",
            "ticker": ticker,
            "as_of": "yfinance live pull",
            "profile": {
                k: info.get(k) for k in (
                    "longName", "country", "sector", "industry", "currency",
                    "fullTimeEmployees", "website", "marketCap", "enterpriseValue",
                )
            },
            "valuation_ratios": {
                k: info.get(k) for k in (
                    "trailingPE", "forwardPE", "priceToBook", "priceToSalesTrailing12Months",
                    "enterpriseToEbitda", "enterpriseToRevenue", "dividendYield",
                )
            },
            "margins_growth": {
                k: info.get(k) for k in (
                    "grossMargins", "ebitdaMargins", "operatingMargins", "profitMargins",
                    "revenueGrowth", "earningsGrowth", "returnOnEquity", "returnOnAssets",
                )
            },
            "balance": {
                k: info.get(k) for k in (
                    "totalRevenue", "ebitda", "totalDebt", "totalCash", "debtToEquity",
                    "freeCashflow", "operatingCashflow",
                )
            },
            "income_statement": frame_to_records(getattr(t, "financials", None)),
            "balance_sheet": frame_to_records(getattr(t, "balance_sheet", None)),
            "cash_flow": frame_to_records(getattr(t, "cashflow", None)),
        }
        print(json.dumps(out, default=str))
    except Exception as e:
        _unavailable(f"yfinance call failed for '{ticker}': {type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
