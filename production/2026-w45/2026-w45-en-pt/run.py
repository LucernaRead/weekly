# -*- coding: utf-8 -*-
"""Run the PT weekly build files in ONE process so the exercise registry
(REG in bslib4) accumulates across pages: content12 -> 34 -> 56 -> 7 -> 8."""
import runpy, sys, os
from collections import Counter

os.chdir(os.path.dirname(os.path.abspath(__file__)))
files = sys.argv[1:] or ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]
for f in files:
    print("=" * 24, f)
    runpy.run_path(f, run_name="__main__")
import bslib4
print("=" * 24, "REGISTRY STATS")
print("TOTAL", len(bslib4.REG))
print("by level", dict(Counter(e["level"] for e in bslib4.REG)))
print("by page", dict(sorted(Counter(e["page"] for e in bslib4.REG).items())))
print("by type", dict(Counter(e["type"] for e in bslib4.REG)))
print("ALL DONE")
