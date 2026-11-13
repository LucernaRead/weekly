# -*- coding: utf-8 -*-
"""Dump the W47 EN core exercise registry to JSON (one-process, same as run.py)."""
import runpy, sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
out = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-en2/fanout/fr/registry.json")
json.dump(bslib4.REG, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("registry:", len(bslib4.REG))
from collections import Counter
print("by page:", dict(sorted(Counter(e["page"] for e in bslib4.REG).items())))
print("by level:", dict(Counter(e["level"] for e in bslib4.REG)))
print("by type:", dict(Counter(e["type"] for e in bslib4.REG)))
