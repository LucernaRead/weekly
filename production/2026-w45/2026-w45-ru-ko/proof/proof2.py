#!/usr/bin/env python3
"""Independent RUxKO W45 proof script 2: geometry, gloss, images, badge, footers, totals."""
import re, json, hashlib, collections
from pathlib import Path

BASE = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/files")
CORE = BASE/"weekly-report-w45-ru-core/svg"
ED = BASE/"weekly-report-w45-ru-ko/svg"
W43 = BASE/"weekly-report-ru-ko/svg"
PAGES = ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]
BUILD = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-ko-build")
CBUILD = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-build")

def elems(path):
    t = Path(path).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<text([^>]*)>([^<]*)</text>', t):
        attrs = m.group(1); s = m.group(2)
        def g(k):
            mm = re.search(rf'{k}="([^"]*)"', attrs); return mm.group(1) if mm else ""
        out.append({"x": float(g("x") or 0), "y": float(g("y") or 0),
                    "size": float(g("font-size") or 0), "weight": g("font-weight"),
                    "fill": g("fill"), "anchor": g("text-anchor"), "fam": g("font-family"), "s": s})
    return out

def rects(path):
    t = Path(path).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<rect([^>]*)/>', t):
        attrs = m.group(1)
        def g(k):
            mm = re.search(rf'{k}="([^"]*)"', attrs); return mm.group(1) if mm else ""
        out.append((g("x"), g("y"), g("width"), g("height"), g("fill"), g("stroke")))
    return out

print("== B. Rect multiset core vs edition (exact tuples) ==")
for p in PAGES:
    cr, er = collections.Counter(rects(CORE/f"{p}.svg")), collections.Counter(rects(ED/f"{p}.svg"))
    print(f"{p}: core={sum(cr.values())} ed={sum(er.values())} core-only={dict(cr-er)} ed-only={dict(er-cr)}")

print("\n== C. P7 readers corner: disclosure lines + box bottom ==")
for label, d in (("core", CORE), ("edition", ED)):
    els = elems(d/"p7-yazyk.svg")
    print(f"--- {label} ---")
    for e in els:
        if "пример от редакции" in e["s"] or "실제 편지" in e["s"] or "письм" in e["s"] and "редакц" in e["s"]:
            print(f"  y={e['y']} size={e['size']} {e['s']!r}")
    # disclosure: lines containing 'VOL.3' promise or 'не пришли' / Korean disclosure
    for e in els:
        if "VOL.3" in e["s"] or "오지 않았어요" in e["s"] or "пришли" in e["s"]:
            print(f"  DISC y={e['y']} {e['s']!r}")
    # letters box: rects near y 1500-1750, find max bottom among rects with y<1727.58+1 and height large
    rs = rects(d/"p7-yazyk.svg")
    cand = []
    for x,y,w,h,f,st in rs:
        try: yy, hh = float(y), float(h)
        except: continue
        if 1500 < yy < 1730 and hh > 50: cand.append((yy, hh, yy+hh, x, w))
    print("  big rects y1500-1730:", sorted(cand, key=lambda c: -c[2])[:4])

print("\n== D. P6 chart bars + % labels ==")
for label, d in (("core", CORE), ("edition", ED)):
    els = elems(d/"p6-razbor.svg"); rs = rects(d/"p6-razbor.svg")
    bars = sorted([(float(w), float(h), float(x), float(y)) for x,y,w,h,f,st in rs if float(h) in (600,494,388,282) and float(w) > 50], key=lambda b: -b[1])
    print(f"--- {label} bars (w,h,x,y): {bars}")
    for e in els:
        if e["s"].strip().endswith("%"):
            print(f"  label {e['s']!r} x={e['x']} y={e['y']} size={e['size']}")

print("\n== F. Gloss counts: split gloss() call strings on · (build sources) ==")
import ast
def gloss_counts(builddir):
    total = 0; per = {}
    for f in ["content12.py","content34.py","content56.py"]:
        src = (builddir/f).read_text(encoding="utf-8")
        tree = ast.parse(src)
        counts = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) and node.func.attr == "gloss":
                if node.args and isinstance(node.args[0], ast.Constant):
                    s = node.args[0].value
                    counts.append(len(s.split("·")))
        per[f] = counts; total += sum(counts)
    return per, total
print("edition build:", gloss_counts(BUILD))
print("core build:   ", gloss_counts(CBUILD))
# rendered gloss lines: lines starting with '해설 — ' in edition vs core '注释'? just print edition gloss lines
for p in ["p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor"]:
    for e in elems(ED/f"{p}.svg"):
        if e["s"].startswith("해설"):
            print(f"  {p} gloss-render y={e['y']}: {e['s']!r}")

print("\n== G. Image payload SHA-256 (data URIs) ==")
def img_hashes(d):
    out = {}
    for p in PAGES:
        t = (d/f"{p}.svg").read_text(encoding="utf-8")
        hs = []
        for m in re.finditer(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', t):
            import base64
            hs.append(hashlib.sha256(base64.b64decode(m.group(1))).hexdigest()[:16])
        out[p] = hs
    return out
ci, ei = img_hashes(CORE), img_hashes(ED)
for p in PAGES:
    print(f"{p}: core={ci[p]} ed={ei[p]} match={ci[p]==ei[p]}")

print("\n== H. Badge three-way ==")
for label, d in (("edition", ED), ("W43", W43), ("core", CORE)):
    els = elems(d/"p1-pervaya.svg")
    for e in els:
        if "한국어 해설" in e["s"] or "한국어 독자" in e["s"] or "러시아어 텍스트" in e["s"]:
            print(f"  {label}: x={e['x']} y={e['y']} size={e['size']} w={e['weight']} fill={e['fill']} anchor={e['anchor']} {e['s']!r}")
    for e in els:
        if e["y"] == 372 or (370 <= e["y"] <= 374):
            print(f"  {label} y~372: x={e['x']} y={e['y']} size={e['size']} {e['s']!r}")

print("\n== I. Footers every page (edition) ==")
for p in PAGES:
    els = elems(ED/f"{p}.svg")
    left = [e["s"] for e in els if e["y"] == 2624 and e["anchor"] == "start"]
    right = [e["s"] for e in els if e["y"] == 2624 and e["anchor"] == "end"]
    print(f"{p}: left={left} right={right}")

print("\n== N. Exercise numbering + level chips from rendered SVGs ==")
allnums = []
for p in PAGES:
    els = elems(ED/f"{p}.svg")
    nums = []
    for e in els:
        m = re.match(r"^(\d+)\.$", e["s"].strip())
        if m: nums.append(int(m.group(1)))
    nums.sort()
    print(f"{p}: n={len(nums)} range={nums[0] if nums else None}-{nums[-1] if nums else None}")
    allnums += nums
print(f"TOTAL numbered labels={len(allnums)} unique={len(set(allnums))} min={min(allnums)} max={max(allnums)} missing={sorted(set(range(1,151))-set(allnums))} dupes={[n for n,c in collections.Counter(allnums).items() if c>1]}")
chips = collections.Counter()
for p in PAGES:
    for e in elems(ED/f"{p}.svg"):
        if e["s"].strip() in ("A2","B1","B2") and e["size"] == 19:
            chips[e["s"].strip()] += 1
print("level chips size19:", dict(chips), "total:", sum(chips.values()))

print("\n== L1. P2 reader-call Korean para ==")
for e in elems(ED/"p2-zhizn.svg"):
    if "11월 4일 수요일은 뭐 할 거예요" in e["s"] or "여러분은요?" in e["s"]:
        print(f"  y={e['y']} x={e['x']} size={e['size']} {e['s']!r}")
print("== L2. P5 gloss word-boundary ==")
for e in elems(ED/"p5-molodezh.svg"):
    if "만들었어요" in e["s"] or "составили" in e["s"]:
        print(f"  y={e['y']} x={e['x']} {e['s']!r}")
print("== L3. P3 gloss 산책 ==")
for e in elems(ED/"p3-kultura.svg"):
    if "산책" in e["s"]:
        print(f"  y={e['y']} x={e['x']} {e['s']!r}")
print("== L4. P6 gloss 집에서 ==")
for e in elems(ED/"p6-razbor.svg"):
    if "집에서" in e["s"]:
        print(f"  y={e['y']} x={e['x']} {e['s']!r}")
print("== K. P2 gloss3 지난 호 / 에. ==")
for e in elems(ED/"p2-zhizn.svg"):
    if "지난 호" in e["s"] or e["s"].strip() == "에.":
        print(f"  y={e['y']} x={e['x']} size={e['size']} {e['s']!r}")
