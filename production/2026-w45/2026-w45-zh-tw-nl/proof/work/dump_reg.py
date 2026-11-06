# -*- coding: utf-8 -*-
"""Dump bslib4.REG from a build-dir copy (OUT already repointed there).
Usage: python dump_reg.py <build-dir> <out-json>"""
import sys, os, json, runpy
d = sys.argv[1]
out = os.path.abspath(sys.argv[2])
os.chdir(d)
sys.path.insert(0, d)
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
with open(out, "w", encoding="utf-8") as fh:
    json.dump(bslib4.REG, fh, ensure_ascii=False, indent=1)
print("dumped", len(bslib4.REG), "to", out)
