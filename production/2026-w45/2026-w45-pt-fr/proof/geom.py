import os, sys, re, html
sys.path.insert(0, 'tools')
import occlusion_audit as OA
from PIL import ImageFont
def parse(path):
    els, _, _ = OA.parse_svg(open(path, encoding='utf-8').read())
    return els
# --- P7 clearance: preview band rect top + max ink bottom of texts above it
els = parse('files/weekly-report-w45-pt-fr/svg/p7-lingua.svg')
bands = [(e.box, e.attrs) for e in els if e.kind=='rect' and e.box and abs(e.box[1]-2404)<1]
print("P7 rects with top~2404:", [(b, a.get('fill')) for b,a in bands][:5])
# anchored boxes for texts: use true ink box from OA (el.box) for texts with baseline<2404
texts_above = [(e.baseline, e.box, e.text) for e in els if e.kind=='text' and e.box and e.baseline < 2404]
texts_above.sort(key=lambda z: z[1][3])
print("P7 top-5 ink-bottoms below band:")
for b, box, t in texts_above[-5:]:
    print(f"  baseline={b} ink-bottom={box[3]:.1f} {t[:60]!r}")
print("P7 max ink bottom above 2404:", max(box[3] for _,box,_ in texts_above), "clearance to 2404:", 2404-max(box[3] for _,box,_ in texts_above))
# quote region: texts in last quote rows y 2250-2404
print("P7 texts baseline 2250..2404:")
for b, box, t in texts_above:
    if 2250 <= b < 2404: print(f"  baseline={b} ink-bottom={box[3]:.1f} {t[:70]!r}")
# --- P2 1897.2 line ED vs CORE (true ink)
for label, path in [('ED','files/weekly-report-w45-pt-fr/svg/p2-vida.svg'),('CORE','files/weekly-report-w45-pt-core/svg/p2-vida.svg')]:
    els2 = parse(path)
    hits = [(e.baseline, e.box, e.text) for e in els2 if e.kind=='text' and e.box and 'objeto que dá luz' in e.text]
    print(label, "P2 match line:", [(b, [round(v,1) for v in box], t) for b,box,t in hits])
    mx = max(e.box[2] for e in els2 if e.kind=='text' and e.box)
    print(label, "P2 max ink-right all texts:", round(mx,1), "inner frame 1910 margin:", round(1910-mx,1))
# --- right-edge ADVANCE scan all pages: advance width (not ink) vs inner frame 1910
for pg in ["p1-capa","p2-vida","p3-cultura","p4-esporte","p5-jovens","p6-aprofundamento","p7-lingua","p8-avaliacao"]:
    els3 = parse(f'files/weekly-report-w45-pt-fr/svg/{pg}.svg')
    worst = []
    for e in els3:
        if e.kind!='text' or not e.text.strip(): continue
        a = e.attrs; size = OA.fnum(a, "font-size", 20.0); bold = a.get("font-weight","") in ("700","bold")
        f = OA.get_font(a.get("font-family",""), size, bold)
        adv = f.getlength(e.text)/OA.SCALE
        x = OA.fnum(a, "x"); anchor = a.get("text-anchor","start")
        left = x - adv/2 if anchor=='middle' else (x-adv if anchor=='end' else x)
        right = left + adv
        if right > 1910:
            worst.append((round(right,1), round(right-1910,1), e.text[:50], e.baseline))
    worst.sort(reverse=True)
    print(pg, "ADVANCE right>1910:", worst[:5])
