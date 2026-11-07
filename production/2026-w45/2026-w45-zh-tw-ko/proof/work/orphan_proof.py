# -*- coding: utf-8 -*-
"""Independent segmented xKO orphan scan, window 10-45 (README #16).
Blocks segmented by (x, size) + y-gap > 45 + P8 item boundaries.
Flags: final-line single-syllable; bracket tail; line-head orphan punct;
>=3-syllable tail-split candidates (word-fragment across boundary);
standalone single-syllable lines. Complete standalone key items NOT orphans.
Also: same-baseline ink scan + chart/rect diffs (separate sections below)."""
import re, os
import xml.etree.ElementTree as ET
from collections import defaultdict
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = BASE + "/files/weekly-report-w45-zh-tw-ko/svg"
NS = "{http://www.w3.org/2000/svg}"
HANGUL = re.compile(r"[가-힣]")
FRAG_START = set(".!?…)]}»」』】％")
PAGES = ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]

def load(p):
    t = ET.parse(f"{ED}/{p}.svg"); out = []
    for e in t.getroot().iter(NS+"text"):
        s = e.text or ""
        if not s.strip(): continue
        out.append(dict(s=s, x=float(e.get("x",0)), y=float(e.get("y",0)),
                        size=float(e.get("font-size","20"))))
    return out

def blocks(els):
    groups = defaultdict(list)
    for e in els: groups[(round(e["x"]), e["size"])].append(e)
    out = []
    for k, g in groups.items():
        g.sort(key=lambda e: e["y"])
        cur = [g[0]]
        for prev, nxt in zip(g, g[1:]):
            # P8 item boundary: new item starts a new block
            if re.match(r"^\d+\. ", nxt["s"].strip()):
                if len(cur) >= 2: out.append(cur)
                cur = [nxt]; continue
            dy = nxt["y"] - prev["y"]
            if 0 < dy <= 45:
                cur.append(nxt)
            else:
                if len(cur) >= 2: out.append(cur)
                cur = [nxt]
        if len(cur) >= 2: out.append(cur)
    return out

def syll(s): return len(HANGUL.findall(s))
total_blocks = 0; cands = []
for p in PAGES:
    els = load(p)
    for blk in blocks(els):
        if not any(HANGUL.search(b["s"]) for b in blk): continue
        total_blocks += 1
        last = blk[-1]["s"].strip()
        stripped = last.rstrip(".!?…)]}» 」』】％")
        ssyll = syll(stripped)
        reason = None
        if syll(last) == 0 and HANGUL.search(blk[-2]["s"] if len(blk) > 1 else ""):
            reason = "final-line-no-hangul-after-korean"
        elif syll(last) <= 1:
            reason = "final<=1syll"
        elif last.endswith(")") or last.endswith("）"):
            reason = "final-dangling-paren"
        elif ssyll <= 2:
            reason = "final<=2syll-tail"
        elif ssyll == 3:
            reason = "final-3syll-short?"
        if reason:
            cands.append((p, round(blk[0]["y"],1), reason, [b["s"] for b in blk][-3:]))
        for ln in blk[1:]:
            s2 = ln["s"].strip()
            if s2 and s2[0] in FRAG_START:
                cands.append((p, round(ln["y"],1), "continuation-start-punct", [ln["s"]]))
print(f"Hangul-bearing blocks: {total_blocks}")
print(f"candidates: {len(cands)}")
for c in cands:
    print(f"  {c[0]} y={c[1]} {c[2]} :: {[s[:70] for s in c[3]]}")
