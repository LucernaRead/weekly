# -*- coding: utf-8 -*-
"""Gloss audit (README #21): split each rendered gloss() call string on
'·' itself (never on ' · ') and count items; compare core vs FR per page.
Also P7 golden sentences: each contributes point + exercise note (2x)."""
import re, sys, os
def gloss_items(builddir, fname):
    src = open(os.path.join(builddir, fname), encoding="utf-8").read()
    items = []
    for m in re.finditer(r'\.gloss\("(.*?)"\)', src, re.S):
        s = m.group(1)
        # strip the library prefix marker used in core ("讲解｜") — FR
        # strings have no prefix (the library adds "Note | ")
        s = re.sub(r"^讲解｜", "", s)
        parts = [p.strip() for p in s.split("·")]
        items.extend([p for p in parts if p])
    return items
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-en-build")
FR = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-en-fr-build")
pages = {"content12.py": "P1+P2", "content34.py": "P3+P4", "content56.py": "P5+P6", "content7.py": "P7", "content8.py": "P8"}
tot_c = tot_f = 0
for fn, pg in pages.items():
    c, f = gloss_items(CORE, fn), gloss_items(FR, fn)
    tot_c += len(c); tot_f += len(f)
    print(f"{pg} ({fn}): core {len(c)} items, FR {len(f)} items {'MATCH' if len(c)==len(f) else 'MISMATCH'}")
    if len(c) != len(f):
        print("  core:", c); print("  fr:", f)
print("TOTAL gloss items: core", tot_c, "FR", tot_f)
# P7 phrases: count point strings + note strings in content7 phrases list
for bd, name in [(CORE, "core"), (FR, "FR")]:
    src = open(os.path.join(bd, "content7.py"), encoding="utf-8").read()
    pts = re.findall(r'"(?:语法点｜|Grammaire : )', src)
    print(name, "phrase points:", len(pts))
