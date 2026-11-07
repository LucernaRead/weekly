# -*- coding: utf-8 -*-
"""Dump the exercise registry by running the single-process driver pattern
in this build dir only (OUT already points at the edition dir)."""
import runpy, sys, os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
from bslib4 import REG
from collections import Counter
import json
print("TOTAL:", len(REG))
print("pages:", dict(sorted(Counter(e["page"] for e in REG).items())))
print("levels:", dict(sorted(Counter(e["level"] for e in REG).items())))
print("types:", dict(sorted(Counter(e["type"] for e in REG).items())))
print("numbers continuous 1..150:", [e["n"] for e in REG] == list(range(1, 151)))
with open("reg-dump.json", "w", encoding="utf-8") as fh:
    json.dump(REG, fh, ensure_ascii=False, indent=1)
