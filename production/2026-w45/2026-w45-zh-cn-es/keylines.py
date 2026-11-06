# -*- coding: utf-8 -*-
"""Compare per-key wrapped line counts in P8 keys area: core vs edition SVG.
Usage: keylines.py <core_p8.svg> <edition_p8.svg>
Keys-area text nodes have y >= 1320 (flow starts 1328) and font-size 13.3.
A key's first line matches ^N. ; continuation lines don't. Headers start with —.
"""
import sys, re
from xml.etree import ElementTree as ET

def keylines(path):
    t = ET.parse(path)
    nodes = []
    for el in t.iter():
        if el.tag.endswith("text"):
            y = float(el.get("y"))
            fs = el.get("font-size")
            if y >= 1320 and fs == "13.3":
                nodes.append((y, "".join(el.itertext())))
    # document order IS flow order (col 0, then 1, 2, 3); do NOT sort by y.
    keys = {}
    cur = None
    for y, s in nodes:
        if s.startswith("—"):
            cur = None
            continue
        m = re.match(r"^(\d+)\. ", s)
        if m:
            cur = int(m.group(1))
            keys[cur] = [s]
        elif cur is not None:
            keys[cur].append(s)
    return keys

core = keylines(sys.argv[1])
ed = keylines(sys.argv[2])
print(f"keys core={len(core)} ed={len(ed)}")
worse = []
for n in sorted(core):
    c, e = len(core[n]), len(ed.get(n, []))
    if e > c:
        worse.append((n, c, e, " ".join(ed[n])))
print(f"keys with MORE lines in edition: {len(worse)}; total extra lines: {sum(e-c for _,c,e,_ in worse)}")
for n, c, e, txt in worse:
    print(f"  key {n}: core {c} -> ed {e}: {txt[:160]}")
# also final y
for label, d in [("core", core), ("ed", ed)]:
    pass
