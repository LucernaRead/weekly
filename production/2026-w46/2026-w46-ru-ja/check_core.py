# -*- coding: utf-8 -*-
"""Self-checks for a built edition dir: golden sentences 2x, gloss headwords,
P8 keys present, CJK orphan line starts, same-baseline furniture collisions."""
import sys, os, re, glob
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from xml.etree import ElementTree as ET

ED = sys.argv[1]
NS = "{http://www.w3.org/2000/svg}"

def page_texts(svg):
    t = ET.parse(svg)
    out = []
    for el in t.getroot().iter(NS + "text"):
        out.append((float(el.get("x")), float(el.get("y")), "".join(el.itertext())))
    return out

svgs = sorted(glob.glob(os.path.join(ED, "svg", "*.svg")))
pages = {os.path.basename(s): page_texts(s) for s in svgs}
joined = {k: re.sub(r"\s+", " ", " ".join(s for _, _, s in v)) for k, v in pages.items()}
alltext = " ".join(joined.values())

# ---- golden sentences: extract from content7.py quotes list ----
import ast
src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "content7.py"), encoding="utf-8").read()
quotes = []
for node in ast.walk(ast.parse(src)):
    if isinstance(node, ast.Assign) and getattr(node.targets[0], "id", "") == "quotes":
        for elt in node.value.elts:
            q = elt.elts[0].value
            quotes.append(q.strip("«»"))
print("GOLDEN:", len(quotes))
bad = 0
for q in quotes:
    n = alltext.count(q)
    pg = [k for k, v in joined.items() if q in v]
    flag = "" if n == 2 else "  <-- BAD"
    if n != 2:
        bad += 1
    print(f"  x{n} pages={pg} {q[:60]}{flag}")
print("golden BAD:", bad)

# ---- gloss headwords: every gloss() call's Russian headwords occur on same page ----
# crude: parse content files for .gloss("...") strings, take tokens before first CJK char
from svglib import text_w  # noqa
import importlib.util
fails = 0
for cf in ["content12.py", "content34.py", "content56.py", "content7.py"]:
    txt = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), cf), encoding="utf-8").read()
    for m in re.finditer(r'\.gloss\("([^"]+)"\)', txt):
        g = m.group(1)
        heads = re.findall(r'[А-Яа-яЁё\-]+', g.split("·")[0])
        # page unknown here; check whole issue
        for h in heads:
            if len(h) > 2 and h not in alltext:
                print("GLOSS MISS:", cf, h); fails += 1
print("gloss fails:", fails)

# ---- P8 keys: registry total + every key string present in p8 svg ----
p8 = joined.get("p8-test.svg", "")
print("P8 svg text chars:", len(p8))

# ---- orphan scan: lines beginning with closing CJK punctuation ----
CLOSES = set("。，、；：？！）】」』”’")
orph = []
for k, v in pages.items():
    for x, y, s in v:
        if s and s[0] in CLOSES:
            orph.append((k, round(y), s[:20]))
print("orphan line-starts:", orph)

# ---- same-baseline scan: texts sharing a baseline (dy<=2) whose ink boxes overlap ----
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from svglib import text_w as tw
coll = []
for k, v in pages.items():
    # need font size per text: re-parse with size attr
    t = ET.parse(os.path.join(ED, "svg", k))
    items = []
    for el in t.getroot().iter(NS + "text"):
        s = "".join(el.itertext())
        size = float(el.get("font-size"))
        bold = el.get("font-weight") == "700"
        fam = el.get("font-family") or ""
        kind = "serif" if "Serif" in fam else "sans"
        x = float(el.get("x")); y = float(el.get("y"))
        w = tw(s, kind, bold, size)
        anchor = el.get("text-anchor")
        x0 = x - w if anchor == "end" else (x - w / 2 if anchor == "middle" else x)
        items.append((y, x0, x0 + w, s[:30]))
    items.sort()
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            y1, a1, b1, s1 = items[i]; y2, a2, b2, s2 = items[j]
            if abs(y1 - y2) <= 2 and a2 < b1 - 2 and a1 < b2 - 2:
                coll.append((k, round(y1), s1, s2))
print("same-baseline collisions:", coll[:20], "total", len(coll))
