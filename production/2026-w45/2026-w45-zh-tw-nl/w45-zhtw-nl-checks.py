# -*- coding: utf-8 -*-
"""W45 zh-tw x nl builder self-checks: same-baseline collisions, chart-label
element check, gloss counts, P7 phrases, image payload identity,
Traditional-independence union check, residual-Latin inventory."""
import re, sys, os, hashlib, html
from collections import Counter

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-zh-tw-nl/svg")
CORE = os.path.join(BASE, "files/weekly-report-w45-zhtw-core/svg")
W43 = os.path.join(BASE, "files/weekly-report-zh-tw-nl/svg")
sys.path.insert(0, os.path.join(BASE, "tools"))
import importlib.util
spec = importlib.util.spec_from_file_location("oa", os.path.join(BASE, "tools/occlusion_audit.py"))
oa = importlib.util.module_from_spec(spec)
spec.loader.exec_module(oa)

TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)"([^>]*)>([^<]*)</text>')

def parse(path):
    s = open(path, encoding="utf-8").read()
    els = []
    for m in TEXT_RE.finditer(s):
        x, y, attrs, t = float(m.group(1)), float(m.group(2)), m.group(3), html.unescape(m.group(4))
        fm = re.search(r'font-family="([^"]+)"', attrs)
        sm = re.search(r'font-size="([\d.]+)"', attrs)
        bold = 'font-weight="700"' in attrs or 'font-weight="bold"' in attrs
        anchor = "middle" if 'text-anchor="middle"' in attrs else ("end" if 'text-anchor="end"' in attrs else "start")
        fam = fm.group(1) if fm else ""
        size = float(sm.group(1)) if sm else 20.0
        box = oa.ink_box(t, fam, size, bold, x, y, anchor, 0.0)
        els.append({"x": x, "y": y, "t": t, "box": box, "size": size})
    return s, els

print("== 1. same-baseline ink collisions (overlap = gap<0) ==")
nflag = 0
for fn in sorted(os.listdir(ED)):
    _, els = parse(os.path.join(ED, fn))
    byy = {}
    for e in els:
        byy.setdefault(e["y"], []).append(e)
    for y, group in byy.items():
        if len(group) < 2:
            continue
        group = sorted(group, key=lambda e: e["box"][0])
        for a, b in zip(group, group[1:]):
            gap = b["box"][0] - a["box"][2]
            if gap < 0:
                print(f"  COLLISION {fn} y={y}: {a['t'][:30]!r} vs {b['t'][:30]!r} gap={gap:.1f}")
                nflag += 1
print("  same-baseline collisions:", nflag)

print("== 2. chart-label element check (text ink vs later-drawn rects, P4/P6) ==")
RECT_RE = re.compile(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"')
nflag2 = 0
for fn in ["p4-sport.svg", "p6-deep.svg"]:
    s, els = parse(os.path.join(ED, fn))
    # document order: interleave texts and rects by file position
    items = []
    for m in TEXT_RE.finditer(s):
        items.append(("text", m.start(), m.group(4)))
    for m in RECT_RE.finditer(s):
        items.append(("rect", m.start(), (float(m.group(1)), float(m.group(2)), float(m.group(3)), float(m.group(4)))))
    items.sort(key=lambda z: z[1])
    # rebuild text boxes in order
    _, els2 = parse(os.path.join(ED, fn))
    titer = iter(els2)
    seq = []
    for kind, _, val in items:
        if kind == "text":
            seq.append(("text", next(titer)))
        else:
            x, y, w, h = val
            seq.append(("rect", (x, y, x + w, y + h)))
    for i, (kind, obj) in enumerate(seq):
        if kind != "text":
            continue
        l, t, r, b = obj["box"]
        for kind2, rbox in seq[i + 1:]:
            if kind2 != "rect":
                continue
            rl, rt, rr, rb = rbox
            if l < rr and r > rl and t < rb and b > rt:
                # ignore the full-page/frame rects (huge) and the chip rects? chips are 60x30 with text on top by design (level chip + level text) - skip rects that are chips (w==60,h==30) and page frames (w>1800)
                if (rr - rl) == 60.0 and (rb - rt) == 30.0:
                    continue
                if (rr - rl) > 1800:
                    continue
                print(f"  OVERLAP {fn}: text {obj['t'][:40]!r} ink {[round(v,1) for v in obj['box']]} vs later rect {[round(v,1) for v in rbox]}")
                nflag2 += 1
print("  chart-label overlaps:", nflag2)

print("== 3. gloss counts in render ==")
tot_u = tot_n = 0
for fn in sorted(os.listdir(ED)):
    s = open(os.path.join(ED, fn), encoding="utf-8").read()
    u = s.count("Uitleg — "); n = s.count("Notes")
    tot_u += u; tot_n += n
    print(f"  {fn}: Uitleg — x{u}, Notes x{n}")
print(f"  TOTAL Uitleg — = {tot_u} (core Notes boxes: 12), Notes residual = {tot_n}")

print("== 4. P7 golden sentences ==")
_, ed_els = [], None
all_ed = ""
for fn in sorted(os.listdir(ED)):
    s = open(os.path.join(ED, fn), encoding="utf-8").read()
    all_ed += "".join(m.group(4) for m in TEXT_RE.finditer(s))
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "p. 1"),
    ("「123個國家及城市、1,600個攤位」", "p. 1"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "p. 2"),
    ("「在高雄，鋼鐵也能變成舞台」", "p. 3"),
    ("「福隆的夏天，在10月26日畫下句點」", "p. 3"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "p. 4"),
    ("「250家店家一起討糖」", "p. 5"),
    ("「旅展首日中午12點才開門」", "p. 6"),
]
for q, pg in quotes:
    print(f"  {q[:20]}... count={all_ed.count(q)} tag=({pg}) present={'(' + pg + ')' in all_ed}")

print("== 5. image payloads per page, core vs edition ==")
IMG_RE = re.compile(r'<image x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*href="data:image/[^;]+;base64,([^"]+)"')
for fn in sorted(os.listdir(CORE)):
    cs = open(os.path.join(CORE, fn), encoding="utf-8").read()
    es = open(os.path.join(ED, fn), encoding="utf-8").read()
    cimgs = [(m.group(1), m.group(2), m.group(3), m.group(4), hashlib.sha256(m.group(5).encode()).hexdigest()[:16]) for m in IMG_RE.finditer(cs)]
    eimgs = [(m.group(1), m.group(2), m.group(3), m.group(4), hashlib.sha256(m.group(5).encode()).hexdigest()[:16]) for m in IMG_RE.finditer(es)]
    print(f"  {fn}: core {len(cimgs)} edition {len(eimgs)} identical={cimgs == eimgs}")
    for c, e in zip(cimgs, eimgs):
        if c != e:
            print(f"    DIFF core {c} vs ed {e}")

print("== 6. Traditional-independence union check ==")
CJK = re.compile(r"[\u3000-\u303f\u3400-\u9fff\uf900-\ufaff]")
def charset(d):
    cs = set()
    for fn in sorted(os.listdir(d)):
        s = open(os.path.join(d, fn), encoding="utf-8").read()
        for m in TEXT_RE.finditer(s):
            cs |= set(CJK.findall(m.group(4)))
    return cs
ed_cs, core_cs, w43_cs = charset(ED), charset(CORE), charset(W43)
union = core_cs | w43_cs
outside = ed_cs - union
print(f"  edition CJK chars: {len(ed_cs)}, core: {len(core_cs)}, W43: {len(w43_cs)}, union: {len(union)}")
print(f"  edition chars outside union: {len(outside)} {sorted(outside) if outside else ''}")
print(f"  edition chars not in core: {len(ed_cs - core_cs)} {sorted(ed_cs - core_cs) if ed_cs - core_cs else ''}")

print("== 7. residual Latin inventory (distinct Latin-script text nodes) ==")
latin = Counter()
for fn in sorted(os.listdir(ED)):
    s = open(os.path.join(ED, fn), encoding="utf-8").read()
    for m in TEXT_RE.finditer(s):
        t = m.group(4)
        if re.search(r"[A-Za-z]", t):
            latin[t] += 1
print(f"  distinct Latin-bearing text nodes: {len(latin)}")
for t, c in sorted(latin.items()):
    print(f"  x{c} {t[:120]}")
