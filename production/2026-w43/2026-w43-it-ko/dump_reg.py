# -*- coding: utf-8 -*-
"""One-process registry dump: run all content modules in run.py order, then
dump bslib4.REG (level, type, key, note) to scratch/registry.json."""
import sys, os, runpy, json
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
for m in ["content12", "content34", "content56", "content7", "content8"]:
    runpy.run_module(m, run_name="__main__")
import bslib4
rows = []
from collections import Counter
lv, tp = Counter(), Counter()
for e in bslib4.REG:
    rows.append({"n": e["n"], "page": e["page"], "level": e["level"],
                 "type": e["type"], "key": e["key"], "note": e["note"]})
    lv[e["level"]] += 1
    tp[e["type"]] += 1
out = os.path.join(HERE, "scratch", "registry.json")
with open(out, "w", encoding="utf-8") as fh:
    json.dump(rows, fh, ensure_ascii=False, indent=1)
print("registry:", len(rows), dict(lv), dict(tp))
print("dumped:", out)
