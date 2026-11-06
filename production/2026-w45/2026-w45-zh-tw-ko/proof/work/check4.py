# -*- coding: utf-8 -*-
"""Same-baseline ink scan, chart/rect diffs, match/fill counts."""
import re, os, json
import xml.etree.ElementTree as ET
from PIL import ImageFont
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE = BASE + "/files/weekly-report-w45-zhtw-core/svg"
ED = BASE + "/files/weekly-report-w45-zh-tw-ko/svg"
NS = "{http://www.w3.org/2000/svg}"
# font paths from tools/tables.json
tj = json.load(open(BASE + "/tools/tables.json"))
print("font table:", json.dumps(tj.get("fonts", tj)[:500] if isinstance(tj.get("fonts"), str) else tj.get("fonts"), ensure_ascii=False)[:600])

def elems(d,p):
    t=ET.parse(f"{d}/{p}.svg"); out=[]
    for el in t.getroot().iter(NS+"text"):
        out.append(dict(x=float(el.get("x",0)), y=float(el.get("y",0)),
                        size=float(el.get("font-size","20")), fam=el.get("font-family",""),
                        bold=el.get("font-weight") in ("700","bold"), s=el.text or ""))
    return out

# --- find TC font file: split TTCs, TC=3
import glob
cands = glob.glob("/usr/share/fonts/**/NotoSerifCJK*.ttc", recursive=True) + glob.glob("/usr/share/fonts/**/NotoSansCJK*.ttc", recursive=True)
print("font files:", cands[:10])
def load_font(fam, size, bold):
    for pat in cands:
        if ("Serif" in pat) == ("Serif" in fam) and (("Bold" in pat) == bold):
            try: return ImageFont.truetype(pat, int(round(size*4)), index=3)
            except Exception as e: print("font load fail", pat, e)
    return None

print("\n=== core P7 y~224 nodes (the claimed artifact flag) ===")
for e in elems(CORE,"p7-lang"):
    if abs(e["y"]-224) < 30 or "Games" in e["s"] or "球賽" in e["s"]:
        print(f"  x={e['x']} y={e['y']} sz={e['size']} fam={e['fam']} bold={e['bold']}: {e['s'][:120]!r}")
print("=== ed P7 B1 head ===")
for e in elems(ED,"p7-lang"):
    if "球賽與節氣" in e["s"]:
        print(f"  x={e['x']} y={e['y']} sz={e['size']} fam={e['fam']}: {e['s']!r}")
        f = load_font(e["fam"], e["size"], e["bold"])
        if f:
            # anchor ls = left-baseline: bbox bottom = descent below baseline
            bb = f.getbbox(e["s"], anchor="ls")
            print(f"  PIL 4x bbox (anchor ls): {bb} -> true width px = {(bb[2]-bb[0])/4:.2f}, ink bottom below baseline = {bb[3]/4:.2f}")
        # raw-escaped measurement (the artifact): measure with '&amp;' literal
        if f:
            raw = e["s"].replace("&","&amp;")
            bb2 = f.getbbox(raw, anchor="ls")
            print(f"  raw-escaped width px = {(bb2[2]-bb2[0])/4:.2f}")

print("\n=== same-baseline ink scan (all pages, core + ed): overlapping runs on one baseline ===")
def scan(d, label):
    bad = []
    for p in ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]:
        els = elems(d,p)
        by = {}
        for e in els:
            if not e["s"].strip(): continue
            by.setdefault(round(e["y"],1), []).append(e)
        for y, g in by.items():
            if len(g) < 2: continue
            spans = []
            for e in g:
                f = load_font(e["fam"], e["size"], e["bold"])
                if f is None: continue
                bb = f.getbbox(e["s"], anchor="ls")
                x0 = e["x"] + bb[0]/4 if e["x"] < 975 else e["x"]  # approx: middle-anchored texts need centering
                # NOTE: text-anchor middle/end not handled here; only flag start-anchored overlaps precisely
                spans.append((e, bb))
            # only compare pairs where both are start-anchored (x small col starts) - use raw x + width
            for i in range(len(g)):
                for j in range(i+1, len(g)):
                    a, b = g[i], g[j]
                    fa, fb = load_font(a["fam"], a["size"], a["bold"]), load_font(b["fam"], b["size"], b["bold"])
                    if fa is None or fb is None: continue
                    wa = (fa.getbbox(a["s"], anchor="ls")[2]-fa.getbbox(a["s"], anchor="ls")[0])/4
                    wb = (fb.getbbox(b["s"], anchor="ls")[2]-fb.getbbox(b["s"], anchor="ls")[0])/4
                    # start-anchored assumption: interval [x, x+w)
                    if a["x"] < b["x"] + wb and b["x"] < a["x"] + wa:
                        # only report if both look start-anchored (heuristic: x at col starts 65/527/989/1451 or 83/93 etc.)
                        bad.append((p, y, a["s"][:60], b["s"][:60], round(wa,1), round(wb,1)))
    print(f"  {label}: candidate same-baseline overlaps (start-anchor approx): {len(bad)}")
    for b in bad[:30]: print("   ", b)
scan(CORE, "CORE"); scan(ED, "ED")

print("\n=== chart bars + rect diffs core vs ed ===")
def rects(d,p):
    t=open(f"{d}/{p}.svg",encoding="utf-8").read()
    return re.findall(r'<rect[^>]*>', t)
for p in ["p4-sport","p6-deep"]:
    cr, er = rects(CORE,p), rects(ED,p)
    print(f"--- {p}: core rects={len(cr)} ed rects={len(er)}")
    from collections import Counter
    cc, ec = Counter(cr), Counter(er)
    for r in (cc-ec):
        print(f"  CORE-ONLY rect: {r[:200]}")
    for r in (ec-cc):
        print(f"  ED-ONLY rect: {r[:200]}")
    # chart bars: filled brick/olive rects - list all rects with width>=100 and height small? print fills
    print("  bar-like rects (w>=100):")
    for r in er:
        m = re.search(r'width="([\d.]+)"', r); h = re.search(r'height="([\d.]+)"', r)
        if m and float(m.group(1)) >= 100:
            print(f"    ED: {r[:200]}")
    for r in cr:
        m = re.search(r'width="([\d.]+)"', r)
        if m and float(m.group(1)) >= 100:
            print(f"    CORE: {r[:200]}")

print("\n=== match / fill-in rendered counts ===")
for d,label in [(CORE,"CORE"),(ED,"ED")]:
    tot_m = tot_f = 0
    for p in ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]:
        txt = "".join(e["s"] for e in elems(d,p))
        m = txt.count("단어와 뜻 짝짓기") + txt.count('instr="Match"')
        # rendered instr text: match heads appear as text nodes; count literal forms
        tot_m += txt.count("단어와 뜻 짝짓기")
        tot_f += txt.count("빈칸 채우기")
    print(f"  {label}: 단어와 뜻 짝짓기 rendered={tot_m}, 빈칸 채우기 rendered={tot_f}")
    for p in ["p1-front","p2-life","p3-culture","p4-sport","p5-youth","p6-deep","p7-lang","p8-test"]:
        txt = "".join(e["s"] for e in elems(d,p))
        print(f"    {label} {p}: match={txt.count('단어와 뜻 짝짓기')} fill={txt.count('빈칸 채우기')} MatchEN={txt.count('Match')} FillEN={txt.count('Fill in')}")
print("=== transform fill-in pair counts ===")
t = open(BASE + "/hidden_files/weekly-report-w45-zh-tw-ko-transform.py", encoding="utf-8").read()
for sec in ["C12","C34","C56","C7","C8"]:
    m = re.search(sec + r" = \[(.*?)\n\]\n", t, re.S)
    if m:
        print(f"  {sec}: Fill-in pairs ->", m.group(1).count("빈칸 채우기"), "| Match pairs ->", m.group(1).count("단어와 뜻 짝짓기"))
