# -*- coding: utf-8 -*-
"""Single-process driver + REG dump (same run order as run.py)."""
import runpy, sys, os, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
with open("reg.json", "w", encoding="utf-8") as fh:
    json.dump(bslib4.REG, fh, ensure_ascii=False, indent=1)
print("REG dumped:", len(bslib4.REG))
