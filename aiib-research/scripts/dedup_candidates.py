#!/usr/bin/env python3
"""Deterministic dedup + rank for sourcing candidates (Claude Code).

The orchestrator collects every source-expander worker's candidate list into one JSON
array and pipes it here. This script normalizes names, collapses duplicates across
workers/methods, treats multi-sourcing as a strength signal, and returns a ranked list —
so dedup is deterministic instead of eyeballed.

Usage:
  cat all_candidates.json | python dedup_candidates.py
  python dedup_candidates.py all_candidates.json

Input: a JSON array of objects. Only "name" is required; any of these are merged if present:
  {"name","anchor","method","private"(bool),"why","provenance","sub_sector"}

Output (stdout): JSON array, one entry per distinct company, sorted by source_count desc
(multi-sourced first), each with the merged anchors/methods/provenance and source_count.
"""
import json
import re
import sys
from collections import OrderedDict

# Legal / suffix noise stripped before comparing names.
_SUFFIXES = {
    "pt", "tbk", "persero", "bhd", "berhad", "plc", "ltd", "limited", "pvt", "private",
    "co", "inc", "corp", "corporation", "group", "holdings", "holding", "sa", "sas",
    "ag", "nv", "spa", "as", "asa", "jsc", "pjsc", "llc", "llp", "company", "the",
}


def normalize(name):
    s = (name or "").lower()
    s = re.sub(r"[.,/&()'\"]+", " ", s)          # drop punctuation
    s = re.sub(r"[^a-z0-9 ]+", " ", s)            # drop non-ascii/diacritic remnants
    toks = [t for t in s.split() if t and t not in _SUFFIXES]
    return " ".join(toks).strip()


def main():
    raw = (open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()).strip()
    if not raw:
        print("[]")
        return
    try:
        items = json.loads(raw)
    except Exception as e:
        print(json.dumps({"error": f"bad JSON input: {e}"}))
        sys.exit(1)
    if isinstance(items, dict):                   # tolerate {"candidates":[...]}
        items = items.get("candidates") or items.get("results") or []

    merged = OrderedDict()
    for it in items:
        if not isinstance(it, dict) or not it.get("name"):
            continue
        key = normalize(it["name"])
        if not key:
            continue
        if key not in merged:
            merged[key] = {
                "name": it["name"].strip(),
                "sub_sector": it.get("sub_sector"),
                "private": it.get("private"),
                "anchors": [], "methods": [], "provenance": [], "why": [],
                "source_count": 0,
            }
        m = merged[key]
        m["source_count"] += 1
        for fld, dst in (("anchor", "anchors"), ("method", "methods"),
                         ("provenance", "provenance"), ("why", "why")):
            v = it.get(fld)
            if v and v not in m[dst]:
                m[dst].append(v)
        if m.get("private") is None and it.get("private") is not None:
            m["private"] = it.get("private")
        if not m.get("sub_sector") and it.get("sub_sector"):
            m["sub_sector"] = it["sub_sector"]

    # Multi-sourced names rank first (overlap = strength signal); then private over listed.
    out = sorted(
        merged.values(),
        key=lambda c: (-c["source_count"], c.get("private") is not True),
    )
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
