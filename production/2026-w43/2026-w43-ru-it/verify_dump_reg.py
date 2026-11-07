# -*- coding: utf-8 -*-
"""Dump the exercise registry (n, page, level, type, key, note) of a build dir
to JSON, running its content files in one process like run.py does."""
import runpy, sys, os, json

build = sys.argv[1]
out = sys.argv[2]
os.chdir(build)
sys.path.insert(0, build)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(os.path.join(build, f), run_name="__main__")
import bslib4
with open(out, "w", encoding="utf-8") as fh:
    json.dump(bslib4.REG, fh, ensure_ascii=False, indent=1)
print("dumped", len(bslib4.REG), "entries ->", out)
