# -*- coding: utf-8 -*-
"""Korean orphan scan restricted to Hangul-bearing blocks (README #16 full definition)."""
import re
import xml.etree.ElementTree as ET
from collections import defaultdict

G = "/home/hatch/workspace/goals/lucernaread-social-media-operations"
NS = "{http://www.w3.org/2000/svg}"
HANGUL = re.compile(r"[가-힣]")
FRAG_START = set(".!?…)]}»」』】％")
PAGES = ["p1-front", "p2-life", "p3-culture", "p4-sport", "p5-youth", "p6-deep", "p7-lang", "p8-test"]

def load(path):
    t = ET.parse(path)
    out = []
    for e in t.getroot().iter(NS + "text"):
        s = e.text or ""
        if not s.strip():
            continue
        out.append(dict(s=s, x=float(e.get("x", 0)), y=float(e.get("y", 0)),
                        size=float(e.get("font-size", "20")),
                        kind="serif" if "Serif" in e.get("font-family", "") else "sans",
                        bold=e.get("font-weight") in ("700", "bold")))
    return out

def blocks(els):
    groups = defaultdict(list)
    for e in els:
        groups[(round(e["x"]), e["size"], e["kind"], e["bold"])].append(e)
    out = []
    for k, g in groups.items():
        g.sort(key=lambda e: e["y"])
        cur = [g[0]]
        for prev, nxt in zip(g, g[1:]):
            dy = nxt["y"] - prev["y"]
            if 0 < dy <= prev["size"] * 2.05:
                cur.append(nxt)
            else:
                if len(cur) >= 2:
                    out.append(cur)
                cur = [nxt]
        if len(cur) >= 2:
            out.append(cur)
    return out

total_blocks = 0
cands = []
for p in PAGES:
    els = load(f"{G}/files/weekly-report-w45-zh-tw-ko/svg/{p}.svg")
    for blk in blocks(els):
        if not any(HANGUL.search(b["s"]) for b in blk):
            continue  # frozen Chinese/Latin blocks are not Korean-orphan scope
        total_blocks += 1
        last = blk[-1]["s"].strip()
        syll = len(HANGUL.findall(last))
        stripped = last.rstrip(".!?…)]}» 」』】％")
        ssyll = len(HANGUL.findall(stripped))
        reason = None
        if syll == 0 and HANGUL.search(blk[-2]["s"] if len(blk) > 1 else ""):
            reason = "final-line-no-hangul-after-korean"
        elif syll <= 1:
            reason = "final<=1syll"
        elif last.endswith(")") or last.endswith("）"):
            reason = "final-dangling-paren"
        elif ssyll <= 2:
            reason = "final<=2syll-tail"
        elif ssyll == 3 and len(stripped) <= 8:
            reason = "final-3syll-short"
        if reason:
            cands.append((p, round(blk[0]["y"], 1), reason, [b["s"] for b in blk][-3:]))
        for ln in blk[1:]:
            s2 = ln["s"].strip()
            if s2 and s2[0] in FRAG_START:
                cands.append((p, round(ln["y"], 1), "continuation-start-punct", [ln["s"]]))
        for ln in blk:
            s3 = ln["s"].strip()
            if s3 and s3[0] in FRAG_START and ln is blk[0]:
                cands.append((p, round(ln["y"], 1), "block-start-punct", [ln["s"]]))
print("Hangul-bearing blocks:", total_blocks)
print("candidates:", len(cands))
for c in cands:
    print(c)
