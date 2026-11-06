# -*- coding: utf-8 -*-
"""Supplementary audits for W45 KO x NL (round 2+), beyond canonical
tools/occlusion_audit.py: ADVANCE right-edge scan, frame-line scan,
same-baseline ink overlap, P6 chart-label coverage (baseline-anchored
true ink), rendered-line window scan (10-45px), P8 three-caliber end,
P7 letters-box geometry, gloss two calibers, phrase frequencies,
image payload hashes, web-PDF vs card comparison.
Run from this dir with tools/venv/bin/python audit_nl.py
"""
import os, re, sys, io, hashlib, json
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w45-ko-nl")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ko-core")
SVG = lambda d: sorted(os.path.join(d, "svg", f) for f in os.listdir(os.path.join(d, "svg")) if f.endswith(".svg"))

def els_of(path):
    return OA.parse_svg(open(path, encoding="utf-8").read())[0]

def adv_of(el):
    """(left, right) advance interval for a text el."""
    a = el.attrs
    f = OA.get_font(a.get("font-family", ""), OA.fnum(a, "font-size", 20.0),
                    a.get("font-weight", "") in ("700", "bold"))
    adv = f.getlength(el.text) / OA.SCALE
    sp = OA.fnum(a, "letter-spacing", 0.0)
    if sp:
        adv += sp * (len(el.text) - 1)
    x = OA.fnum(a, "x")
    anchor = a.get("text-anchor", "start")
    if anchor == "middle":
        return x - adv / 2, x + adv / 2
    if anchor == "end":
        return x - adv, x
    return x, x + adv

print("=== 1. ADVANCE right-edge scan (limit 1910) ===")
worst = 0.0; flags = []
for p in SVG(ED):
    for el in els_of(p):
        if el.kind != "text" or not el.text.strip():
            continue
        l, r = adv_of(el)
        worst = max(worst, r)
        if r > 1910 or l < 40:
            flags.append((os.path.basename(p), el.text[:40], round(l, 1), round(r, 1)))
print("worst advance right:", round(worst, 1), "flags:", len(flags))
for f in flags:
    print("  FLAG", f)

print("=== 2. Frame-line scan (text ink vs rect borders / lines; footer rule y=2580 exempt) ===")
fflags = []
for p in SVG(ED):
    els = els_of(p)
    for i, el in enumerate(els):
        if el.kind != "text" or not el.box:
            continue
        for j, o in enumerate(els):
            if j <= i or o.kind not in ("rect", "line") or not o.box:
                continue
            if o.kind == "line" and abs(OA.fnum(o.attrs, "y1") - 2580) < 1:
                continue
            # rect border: ink strictly inside rect is fine; straddle = defect
            if o.kind == "rect":
                bl, bt, br, bb = o.box
                il, it, ir, ib = el.box
                sw = OA.fnum(o.attrs, "stroke-width", 0.0) / 2 + 0.5
                # a border straddle needs BOTH: ink crosses the edge line
                # AND ink overlaps the edge segment on the other axis
                vcross = ((il < bl + sw < ir) or (il < br - sw < ir)) and not (ib < bt or it > bb)
                hcross = ((it < bt + sw < ib) or (it < bb - sw < ib)) and not (ir < bl or il > br)
                if vcross or hcross:
                    fflags.append((os.path.basename(p), el.text[:30], o.kind, [round(v, 1) for v in o.box]))
            else:
                l, t, r, b = o.box
                il, it, ir, ib = el.box
                if l == r:  # vertical line
                    if il < l < ir and not (ib < t or it > b):
                        fflags.append((os.path.basename(p), el.text[:30], "vline", round(l, 1)))
                elif t == b:  # horizontal line
                    if it < t < ib and not (ir < l or il > r):
                        fflags.append((os.path.basename(p), el.text[:30], "hline", round(t, 1)))
print("frame flags:", len(fflags))
for f in fflags[:20]:
    print("  FLAG", f)

print("=== 3. Same-baseline ink overlap (0.6px tolerance) ===")
sflags = []
for p in SVG(ED):
    els = [e for e in els_of(p) if e.kind == "text" and e.box]
    groups = {}
    for e in els:
        groups.setdefault(round(e.baseline / 0.6), []).append(e)
    for g in groups.values():
        g.sort(key=lambda e: e.box[0])
        for a, b in zip(g, g[1:]):
            if b.box[0] < a.box[2] - 0.6:
                sflags.append((os.path.basename(p), round(a.baseline, 1), a.text[:30], b.text[:30]))
print("same-baseline flags:", len(sflags))
for f in sflags[:20]:
    print("  FLAG", f)

print("=== 4. P6 chart-label coverage (true ink vs later rects, gate <30%) ===")
p6 = os.path.join(ED, "svg", "p6-gipi.svg")
els = els_of(p6)
labs = []
for i, el in enumerate(els):
    if el.kind != "text" or not el.box:
        continue
    worst_cov = 0.0
    for o in els[i + 1:]:
        if o.kind == "rect" and o.box and OA.is_opaque(o):
            area, _ = OA.overlap(el.box, o.box)
            ink_area = (el.box[2] - el.box[0]) * (el.box[3] - el.box[1])
            if ink_area > 0:
                worst_cov = max(worst_cov, area / ink_area)
    if worst_cov > 0:
        labs.append((el.text[:40], round(worst_cov * 100, 1)))
print("labels with coverage>0:", len(labs), "worst:", max([c for _, c in labs], default=0.0))
for l in labs[:20]:
    print("  ", l)

print("=== 5. Rendered-line window scan (dy 10-45, same x) ===")
NO_START = set(")]}〉》.,!?%:;\"'」』）】〕、。")
# KO svglib ASCII closer set + full-width closers
NO_START |= set(")]}〉》.,!?%:;\"")
wflags = []
for p in SVG(ED):
    els = [e for e in els_of(p) if e.kind == "text" and e.text.strip()]
    byx = {}
    for e in els:
        byx.setdefault(OA.fnum(e.attrs, "x"), []).append(e)
    for x, g in byx.items():
        g.sort(key=lambda e: e.baseline)
        for a, b in zip(g, g[1:]):
            dy = b.baseline - a.baseline
            if 10 <= dy <= 45:
                first = b.text.strip()[:1]
                if first in NO_START:
                    wflags.append((os.path.basename(p), round(x, 1), round(a.baseline, 1), round(b.baseline, 1), repr(a.text[-20:]), repr(b.text[:20])))
print("line-start NO_START flags:", len(wflags))
for f in wflags:
    print("  FLAG", f)

print("=== 6. P8 three calibers ===")
import subprocess
log = open(os.path.join(HERE, "round3-run.log"), encoding="utf-8").read()
m = re.search(r"flow\[P8-keys\] ended col \d+/\d+ y=([\d.]+)", log)
cursor = float(m.group(1)) if m else None
p8 = els_of(os.path.join(ED, "svg", "p8-siheom.svg"))
keys = [e for e in p8 if e.kind == "text" and e.baseline > 1330 and e.baseline < 2600]
maxbase = max(e.baseline for e in keys)
inkbot = max(e.box[3] for e in keys if e.box)
print(f"flow cursor={cursor} max baseline={maxbase:.2f} ink bottom={inkbot:.2f} (limit 2540)")

print("=== 7. P7 letters-box geometry ===")
p7 = els_of(os.path.join(ED, "svg", "p7-mal.svg"))
rects = [e for e in p7 if e.kind == "rect"]
for e in rects:
    x, y = OA.fnum(e.attrs, "x"), OA.fnum(e.attrs, "y")
    w, h = OA.fnum(e.attrs, "width"), OA.fnum(e.attrs, "height")
    if abs(x - 1451) < 1 and 1300 < y < 1900:
        print(f"  letters rect? x={x} y={y} w={w} h={h} bottom={y + h}")
letters_texts = [e for e in p7 if e.kind == "text" and abs(OA.fnum(e.attrs, "x") - 1473) < 1 and 1350 < e.baseline < 1900]
if letters_texts:
    last = max(letters_texts, key=lambda e: e.baseline)
    print(f"  last letters text baseline={last.baseline:.2f} ink bottom={last.box[3]:.2f} text={last.text[:60]!r}")
    print(f"  all letters baselines: {[round(e.baseline, 1) for e in letters_texts]}")
lines = [e for e in p7 if e.kind == "line"]
for e in lines:
    y1 = OA.fnum(e.attrs, "y1")
    if 1850 < y1 < 1950:
        print(f"  phrases rule line y={y1}")
teaser = [e for e in p7 if e.kind == "rect" and OA.fnum(e.attrs, "height") == 118 and OA.fnum(e.attrs, "y") > 2400]
for e in teaser:
    print(f"  teaser rect y={OA.fnum(e.attrs, 'y')} bottom={OA.fnum(e.attrs, 'y') + 118}")

print("=== 8. Gloss calibers ===")
import ast as _ast
def call_gloss(path):
    src = open(path, encoding="utf-8").read()
    total = 0; per = []
    for mm in re.finditer(r"\.(?:gloss|glossline)\(\s*([^)]*)\)", src):
        arg = mm.group(1)
        # string literal(s): take first quoted literal
        sm = re.search(r'"([^"]*)"', arg)
        if not sm:
            # f-string or concatenated: skip (counted via render instead)
            continue
        s = sm.group(1)
        # strip a leading Korean headword? No: count items split on '·'
        items = [t for t in s.split("·")]
        per.append((s[:30], len(items)))
        total += len(items)
    return total, per
for d, label in [(os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-build"), "core"),
                 (HERE, "edition")]:
    tot = 0
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        t, _ = call_gloss(os.path.join(d, f))
        print(f"  call-string {label} {f}: {t}")
        tot += t
    print(f"  call-string {label} TOTAL: {tot}")
print("  rendered caliber (sans 20.5 grey texts, units split on '·'):")
def rendered_gloss(d):
    out = {}
    for p in SVG(d):
        els = [e for e in els_of(p) if e.kind == "text" and e.text.strip()]
        sel = []
        for e in els:
            a = e.attrs
            if (a.get("font-family", "").startswith("Noto Sans") or "Sans" in a.get("font-family", "")) \
               and abs(OA.fnum(a, "font-size") - 20.5) < 0.1 and a.get("fill", "") == "#57523f":
                sel.append(e)
        # group by x, consecutive dy<=45
        sel.sort(key=lambda e: (OA.fnum(e.attrs, "x"), e.baseline))
        units = []
        cur = []
        for e in sel:
            if cur and (OA.fnum(e.attrs, "x") != OA.fnum(cur[-1].attrs, "x") or e.baseline - cur[-1].baseline > 45):
                units.append(cur); cur = []
            cur.append(e)
        if cur:
            units.append(cur)
        items = 0
        for u in units:
            joined = "".join(t.text for t in u)
            items += len(joined.split("·"))
        out[os.path.basename(p)] = (len(units), items)
    return out
rc, re_ = rendered_gloss(CORE), rendered_gloss(ED)
for k in sorted(rc):
    print(f"  {k}: core units={rc[k][0]} items={rc[k][1]} | edition units={re_[k][0]} items={re_[k][1]}")

print("=== 9. Phrase frequencies (space-stripped, whole issue) ===")
PHRASES = ["11월 7일은 입동이에요", "절정에 가까운 주말이라고만 말할 수 있어요",
           "김장은 겨울 내내 먹는 김치를 담그는 일이에요", "수능까지 17일 남았어요. 오늘이 D-17예요",
           "낮은 길은 더 늦게 물들어요", "KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요",
           "온 나라가 수험생을 응원해요", "날짜를 먼저 보세요"]
TAGS = ["1면", "2면", "3면", "4면", "5면", "6면"]
def page_texts(d):
    out = {}
    for p in SVG(d):
        txt = "".join(e.text for e in els_of(p) if e.kind == "text")
        out[os.path.basename(p)] = re.sub(r"\s+", "", txt)
    return out
cp, ep = page_texts(CORE), page_texts(ED)
for ph, tag in zip(PHRASES, ["1면", "1면", "1면", "2면", "3면", "4면", "5면", "6면"]):
    key = re.sub(r"\s+", "", ph)
    cc = sum(v.count(key) for v in cp.values())
    ec = sum(v.count(key) for v in ep.values())
    # tagged page: find which page file holds the tag (p1..p6 order)
    print(f"  {ph[:22]}... tag {tag}: core={cc} edition={ec}")

print("=== 10. Image payloads + credits ===")
def images(d):
    out = {}
    for p in SVG(d):
        s = open(p, encoding="utf-8").read()
        arr = []
        for mm in re.finditer(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', s):
            b64 = mm.group(1)
            raw = __import__("base64").b64decode(b64)
            arr.append((hashlib.sha256(b64.encode()).hexdigest()[:12],
                        hashlib.sha256(raw).hexdigest()[:12]))
        out[os.path.basename(p)] = arr
    return out
ic, ie = images(CORE), images(ED)
for k in sorted(ic):
    print(f"  {k}: core={ic[k]} edition={ie[k]} equal={ic[k] == ie[k]}")
for p in SVG(ED):
    s = open(p, encoding="utf-8").read()
    texts = re.findall(r"<text[^>]*>([^<]*)</text>", s)
    creds = [t for t in texts if any(a in t for a in ["lumoplank", "wizdata", "Udonhan1992", "Cézanne", "Bain", "Gary Todd", "사진:"])]
    if creds:
        print(" ", os.path.basename(p), creds)

print("=== 11. Web PDF vs cards ===")
from pypdf import PdfReader
for pdf, label in [(os.path.join(ED, "Lucerna-VOL2-NL-web.pdf"), "web"),
                   (os.path.join(ED, "Lucerna-VOL2-NL.pdf"), "print")]:
    r = PdfReader(pdf)
    print(f"  {label} PDF pages: {len(r.pages)} size: {os.path.getsize(pdf)}")
try:
    from pypdf import PdfReader as PR
    r = PR(os.path.join(ED, "Lucerna-VOL2-NL-web.pdf"))
    cards = sorted(os.path.join(ED, "cards", f) for f in os.listdir(os.path.join(ED, "cards")) if f.endswith(".png"))
    for i, page in enumerate(r.pages):
        imgs = list(page.images)
        if not imgs:
            print(f"  web p{i+1}: NO embedded image!")
            continue
        data = imgs[0].data
        im = Image.open(io.BytesIO(data)).convert("RGB")
        card = Image.open(cards[i]).convert("RGB").resize(im.size, Image.LANCZOS)
        from PIL import ImageChops, ImageStat
        diff = ImageStat.Stat(ImageChops.difference(im, card)).mean
        print(f"  web p{i+1}: {im.size} mean|diff| per channel = {[round(v, 2) for v in diff]}")
except Exception as ex:
    print("  web-vs-card failed:", repr(ex))
print("AUDIT DONE")
