#!/usr/bin/env python3
"""
Rebuild index.html by injecting the canonical persona data into the template.

The app is a single self-contained HTML file with the data embedded inline
(browsers block fetch() of local JSON when you open a file directly), so any
time you edit data/prospect-intelligence.json, run this to regenerate index.html.

Usage:
    python3 build/build.py
"""
import json, pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
data = json.loads((ROOT / "data" / "prospect-intelligence.json").read_text(encoding="utf-8"))
template = (ROOT / "build" / "template.html").read_text(encoding="utf-8")

out = template.replace("__SEED__", json.dumps(data, ensure_ascii=False))
assert "__SEED__" not in out, "placeholder not replaced — check template.html"

(ROOT / "index.html").write_text(out, encoding="utf-8")
print(f"Built index.html with {len(data['personas'])} personas "
      f"({sum(len(p['quiz']['flashcards']) for p in data['personas'])} flashcards).")
