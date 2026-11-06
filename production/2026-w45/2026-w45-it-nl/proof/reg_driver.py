#!/usr/bin/env python3
"""Independent registry dump: run a build copy (repointed OUT) in ONE process,
then dump bslib4.REG. Usage: reg_driver.py <build-copy-dir> <out-json>"""
import json, os, runpy, sys
d = sys.argv[1]; out = sys.argv[2]
os.chdir(d)
sys.path.insert(0, d)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(os.path.join(d, f), run_name="__main__")
import bslib4
reg = bslib4.REG
def ser(e):
    return {k: (v if not isinstance(v, (list, dict)) else v) for k, v in e.items()}
with open(out, "w", encoding="utf-8") as fh:
    json.dump(reg, fh, ensure_ascii=False, indent=1)
print("TOTAL", len(reg))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in reg)))
print("by page", dict(sorted(Counter(e["page"] for e in reg).items())))
print("keys sample", reg[0].keys() if reg else None)
