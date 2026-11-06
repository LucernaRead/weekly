# -*- coding: utf-8 -*-
"""Repoint a W46 fan-out build dir at its edition dir, fix the bslib4 footer
VOL, install the print-only render.py (core pattern) with the family's PDF
name. Usage: finish.py <lang> <pdf-stem>  e.g. finish.py de Lucerna-VOL3"""
import os, re, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
LANG, STEM = sys.argv[1], sys.argv[2]
BUILD = os.path.join(GOAL, "hidden_files", f"weekly-report-w46-ko-{LANG}-build")
ED = os.path.join(GOAL, "files", f"weekly-report-w46-ko-{LANG}")
os.makedirs(os.path.join(ED, "svg"), exist_ok=True)

for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    p = os.path.join(BUILD, fname)
    s = open(p, encoding="utf-8").read()
    assert s.count("weekly-report-w46-ko-core") == 1, (fname, s.count("weekly-report-w46-ko-core"))
    open(p, "w", encoding="utf-8").write(s.replace("weekly-report-w46-ko-core", f"weekly-report-w46-ko-{LANG}"))
    print("repointed", fname)

# bslib4 footer VOL.2 -> VOL.3 (W45 family footer already translated)
p = os.path.join(BUILD, "bslib4.py")
s = open(p, encoding="utf-8").read()
s2 = s.replace("VOL.2", "VOL.3")
assert "VOL.3" in s2, "no VOL.3 in bslib4 footer after fix"
open(p, "w", encoding="utf-8").write(s2)
print("bslib4 footer -> VOL.3")

# print-only render.py from the core pattern
core_render = open(os.path.join(GOAL, "hidden_files", "weekly-report-w46-ko-build", "render.py"), encoding="utf-8").read()
render = core_render.replace("weekly-report-w46-ko-core", f"weekly-report-w46-ko-{LANG}")
render = render.replace("Lucerna-VOL3.pdf", f"{STEM}.pdf")
assert STEM + ".pdf" in render
open(os.path.join(BUILD, "render.py"), "w", encoding="utf-8").write(render)
print("render.py installed:", STEM + ".pdf")
