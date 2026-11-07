# -*- coding: utf-8 -*-
"""Dump the exercise registry (REG) from a build copy: run the content
modules in ONE process via the build's own driver pattern, then write
REG as JSON. Run ONLY inside a build copy whose OUT paths point at its
own (scratch/delivery) svg dir — never inside the core build dir."""
import json, os, runpy, sys

d = sys.argv[1]
out = sys.argv[2]
os.chdir(d)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
json.dump(bslib4.REG, open(out, "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print(f"dumped {len(bslib4.REG)} entries to {out}")
