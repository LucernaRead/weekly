# -*- coding: utf-8 -*-
"""Independent geometry re-measurement for W45 KO x NL (own code, OA parser only)."""
import os, re, sys
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(GOAL, "files/weekly-report-w45-ko-nl")
CORE = os.path.join(GOAL, "files/weekly-report-w45-ko-core")
PAGES = ["p1-pyoji.svg", "p2-saenghwal.svg", "p3-munhwa.svg", "p4-seupocheu.svg",
         "p5-cheongnyeon.svg", "p6-gipi.svg", "p7-mal.svg", "p8-siheom.svg"]
def els(d, pg): return OA.parse_svg(open(os.path.join(d, "svg", pg), encoding="utf-8").read())[0]

def adv(el):
    a = el.attrs
    f = OA.get_font(a.get("font-family", ""), OA.fnum(a, "font-size", 20.0), a.get("font-weight", "") in ("700", "bold"))
    adv = f.getlength(el.text) / OA.SCALE
    sp = OA.fnum(a, "letter-spacing", 0.0)
    if sp: adv += sp * (len(el.text) - 1)
    x = OA.fnum(a, "x"); anchor = a.get("text-anchor", "start")
    if anchor == "middle": return x - adv / 2, x + adv / 2
    if anchor == "end": return x - adv, x
    return x, x + adv

print("== 1. ADVANCE right-edge scan (limit 1910, left>=40) ==")
worst, flags = 0.0, []
for pg in PAGES:
    for e in els(ED, pg):
        if e.kind != "text" or not e.text.strip(): continue
        l, r = adv(e); worst = max(worst, r)
        if r > 1910 or l < 40: flags.append((pg, e.text[:40], round(l, 1), round(r, 1)))
print(f"   worst advance right={worst:.1f} flags={len(flags)} {flags}")

print("== 2. frame-line scan (text ink vs later rect borders/lines; footer rule 2580 exempt) ==")
ff = []
for pg in PAGES:
    es = els(ED, pg)
    for i, el in enumerate(es):
        if el.kind != "text" or not el.box: continue
        for o in es[i + 1:]:
            if o.kind not in ("rect", "line") or not o.box: continue
            if o.kind == "line" and abs(OA.fnum(o.attrs, "y1") - 2580) < 1: continue
            il, it, ir, ib = el.box
            if o.kind == "rect":
                bl, bt, br, bb = o.box
                sw = OA.fnum(o.attrs, "stroke-width", 0.0) / 2 + 0.5
                vc = ((il < bl + sw < ir) or (il < br - sw < ir)) and not (ib < bt or it > bb)
                hc = ((it < bt + sw < ib) or (it < bb - sw < ib)) and not (ir < bl or il > br)
                if vc or hc: ff.append((pg, el.text[:30], "rect", [round(v, 1) for v in o.box]))
            else:
                l, t, r, b = o.box
                if l == r:
                    if il < l < ir and not (ib < t or it > b): ff.append((pg, el.text[:30], "vline", round(l, 1)))
                elif t == b:
                    if it < t < ib and not (ir < l or il > r): ff.append((pg, el.text[:30], "hline", round(t, 1)))
print(f"   frame flags={len(ff)} {ff[:10]}")

print("== 3. same-baseline ink overlap (0.6px tolerance) ==")
sf = []
for pg in PAGES:
    es = [e for e in els(ED, pg) if e.kind == "text" and e.box]
    groups = {}
    for e in es: groups.setdefault(round(e.baseline / 0.6), []).append(e)
    for g in groups.values():
        g.sort(key=lambda e: e.box[0])
        for a, b in zip(g, g[1:]):
            if b.box[0] < a.box[2] - 0.6: sf.append((pg, round(a.baseline, 1), a.text[:30], b.text[:30]))
print(f"   same-baseline flags={len(sf)} {sf[:10]}")

print("== 4. P6 chart-label coverage (ink box vs later opaque rects) ==")
es = els(ED, "p6-gipi.svg")
labs = []
for i, el in enumerate(es):
    if el.kind != "text" or not el.box: continue
    worst_cov = 0.0
    for o in es[i + 1:]:
        if o.kind == "rect" and o.box and OA.is_opaque(o):
            area, _ = OA.overlap(el.box, o.box)
            ink = (el.box[2] - el.box[0]) * (el.box[3] - el.box[1])
            if ink > 0: worst_cov = max(worst_cov, area / ink)
    if worst_cov > 0: labs.append((el.text[:40], round(worst_cov * 100, 1)))
print(f"   labels coverage>0: {len(labs)} worst: {max([c for _, c in labs], default=0.0)} {labs[:10]}")

print("== 5. P8 three calibers (cursor from MY repro log, limit 2540) ==")
log = open(os.path.join(GOAL, "hidden_files/w45/ko-nl-proof/work/ed-repro.log"), encoding="utf-8").read()
m = re.search(r"flow\[P8-keys\] ended col \d+/\d+ y=([\d.]+)", log)
cursor = float(m.group(1)) if m else None
p8 = els(ED, "p8-siheom.svg")
keys = [e for e in p8 if e.kind == "text" and e.baseline and 1330 < e.baseline < 2600]
maxbase = max(e.baseline for e in keys); inkbot = max(e.box[3] for e in keys if e.box)
print(f"   flow cursor={cursor} max baseline={maxbase:.2f} ink bottom={inkbot:.2f} (limit 2540)")

print("== 6. P7 geometry (edition, own extraction) ==")
p7 = els(ED, "p7-mal.svg")
rects = [e for e in p7 if e.kind == "rect"]
for e in rects:
    x, y = OA.fnum(e.attrs, "x"), OA.fnum(e.attrs, "y")
    w, h = OA.fnum(e.attrs, "width"), OA.fnum(e.attrs, "height")
    if abs(x - 1451) < 1 and 1200 < y < 1900:
        print(f"   letters rect x={x} y={y} w={w} h={h} bottom={y + h}")
lets = [e for e in p7 if e.kind == "text" and abs(OA.fnum(e.attrs, "x") - 1473) < 1 and 1350 < e.baseline < 1900]
last = max(lets, key=lambda e: e.baseline)
print(f"   last letters baseline={last.baseline:.2f} ink bottom={last.box[3]:.2f} text={last.text!r}")
print(f"   box bottom - ink bottom = {1230.44 + 635.5 - last.box[3]:.2f}")
for e in p7:
    if e.kind == "line" and 1850 < OA.fnum(e.attrs, "y1") < 1950:
        print(f"   phrases rule line y={OA.fnum(e.attrs, 'y1')} gap vs ink bottom={OA.fnum(e.attrs, 'y1') - last.box[3]:.2f}")
for e in rects:
    if OA.fnum(e.attrs, "height") == 118 and OA.fnum(e.attrs, "y") > 2400:
        print(f"   teaser rect y={OA.fnum(e.attrs, 'y')} bottom={OA.fnum(e.attrs, 'y') + 118}")
print("== 7. P7 preview/core-overflow (report only, core not reopened) ==")
for d, nm in [(CORE, "core")]:
    es = els(d, "p7-mal.svg")
    rr = [(OA.fnum(e.attrs, "y"), OA.fnum(e.attrs, "height")) for e in es if e.kind == "rect" and abs(OA.fnum(e.attrs, "x") - 1451) < 1 and 1200 < OA.fnum(e.attrs, "y") < 1900]
    ll = [e for e in es if e.kind == "text" and abs(OA.fnum(e.attrs, "x") - 1473) < 1 and 1350 < e.baseline < 1900]
    lastc = max(ll, key=lambda e: e.baseline)
    print(f"   {nm}: box y={rr[0][0]} h={rr[0][1]} bottom={rr[0][0] + rr[0][1]} last ink={lastc.box[3]:.2f} overflow={lastc.box[3] - (rr[0][0] + rr[0][1]):.2f}")
