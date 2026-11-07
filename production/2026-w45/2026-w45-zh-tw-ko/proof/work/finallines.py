# -*- coding: utf-8 -*-
"""Print last 2 lines of every Hangul-bearing block for fragment-split reading."""
import re, os
import xml.etree.ElementTree as ET
from collections import defaultdict
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = BASE + "/files/weekly-report-w45-zh-tw-ko/svg"
NS = "{http://www.w3.org/2000/svg}"
HANGUL = re.compile(r"[가-힣]")
PAGES = ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]
def load(p):
    t = ET.parse(f"{ED}/{p}.svg"); out = []
    for e in t.getroot().iter(NS+"text"):
        s = e.text or ""
        if not s.strip(): continue
        out.append(dict(s=s, x=float(e.get("x",0)), y=float(e.get("y",0)), size=float(e.get("font-size","20"))))
    return out
def blocks(els):
    groups = defaultdict(list)
    for e in els: groups[(round(e["x"]), e["size"])].append(e)
    out = []
    for k, g in groups.items():
        g.sort(key=lambda e: e["y"])
        cur = [g[0]]
        for prev, nxt in zip(g, g[1:]):
            if re.match(r"^\d+\. ", nxt["s"].strip()):
                if len(cur) >= 2: out.append(cur)
                cur = [nxt]; continue
            dy = nxt["y"] - prev["y"]
            if 0 < dy <= 45: cur.append(nxt)
            else:
                if len(cur) >= 2: out.append(cur)
                cur = [nxt]
        if len(cur) >= 2: out.append(cur)
    return out
for p in PAGES:
    for blk in blocks(load(p)):
        if not any(HANGUL.search(b["s"]) for b in blk): continue
        print(f"{p} y0={blk[0]['y']:.1f} :: PREV={blk[-2]['s'].strip()[:90]!r} || LAST={blk[-1]['s'].strip()[:90]!r}")
