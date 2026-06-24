#!/usr/bin/env python3
"""Fetch free structured financials for one or more tickers via yfinance.

Usage:  python fetch_financials.py <TICKER> [<TICKER> ...]
Example: python fetch_financials.py PGEO.JK ADANIGREEN.NS

Prints JSON to stdout. One ticker → a single JSON object; multiple tickers → a JSON array,
one object per ticker (in argv order). Each object is status="ok" with the financial data, or
status="unavailable" with a reason — the skill should then fall back to the web-search floor
(see references/data-sources.md). Never raises; always prints parseable JSON.

yfinance is Apache-2.0 and free (no API key). International tickers use exchange suffixes
(.JK Jakarta, .BK Bangkok, .NS India, .SA Sao Paulo, .SN Santiago, .IS Istanbul, .HK Hong Kong).
"""
import json
import sys


def _unavailable(reason, ticker=None):
    d = {"status": "unavailable", "reason": reason}
    if ticker is not None:
        d["ticker"] = ticker
    return d


def fetch_one(yf, ticker):
    try:
        t = yf.Ticker(ticker)
        info = getattr(t, "info", {}) or {}
        if not info or (info.get("regularMarketPrice") is None and not info.get("longName")):
            return _unavailable(f"no data returned for '{ticker}' (bad ticker, no coverage, or no network)", ticker)

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

        return {
            "status": "ok",
            "ticker": ticker,
            "as_of": "yfinance live pull",
            "profile": {k: info.get(k) for k in (
                "longName", "country", "sector", "industry", "currency",
                "fullTimeEmployees", "website", "marketCap", "enterpriseValue")},
            "valuation_ratios": {k: info.get(k) for k in (
                "trailingPE", "forwardPE", "priceToBook", "priceToSalesTrailing12Months",
                "enterpriseToEbitda", "enterpriseToRevenue", "dividendYield")},
            "margins_growth": {k: info.get(k) for k in (
                "grossMargins", "ebitdaMargins", "operatingMargins", "profitMargins",
                "revenueGrowth", "earningsGrowth", "returnOnEquity", "returnOnAssets")},
            "balance": {k: info.get(k) for k in (
                "totalRevenue", "ebitda", "totalDebt", "totalCash", "debtToEquity",
                "freeCashflow", "operatingCashflow")},
            "income_statement": frame_to_records(getattr(t, "financials", None)),
            "balance_sheet": frame_to_records(getattr(t, "balance_sheet", None)),
            "cash_flow": frame_to_records(getattr(t, "cashflow", None)),
        }
    except Exception as e:
        return _unavailable(f"yfinance call failed for '{ticker}': {type(e).__name__}: {e}", ticker)


def main():
    tickers = [a.strip() for a in sys.argv[1:] if a.strip()]
    if not tickers:
        print(json.dumps(_unavailable("no ticker argument (usage: fetch_financials.py <TICKER> [<TICKER> ...])")))
        return

    try:
        import yfinance as yf
    except Exception:
        # Self-heal: try a one-time quiet install, then re-import. Graceful fallback if blocked.
        import subprocess
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "--quiet", "--disable-pip-version-check", "yfinance"],
                           check=True, timeout=240, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            import yfinance as yf
        except Exception as e:
            print(json.dumps(_unavailable(f"yfinance unavailable and auto-install failed ({type(e).__name__}) — "
                                          "the sandbox likely blocks pip/network; use the web-search floor")))
            return

    results = [fetch_one(yf, t) for t in tickers]
    print(json.dumps(results[0] if len(results) == 1 else results, default=str))


if __name__ == "__main__":
    main()
