# Independent geometry re-measurement for W45 ITxES proofread (own code;
# measurement primitives text_w/_font borrowed from the build's svglib,
# the same PIL/FreeType library the canonical audit uses).
import sys, os, xml.etree.ElementTree as ET
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-it-es-build"))
from svglib import text_w, _font
NS = '{http://www.w3.org/2000/svg}'
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-es/svg")
PAGES = ["p1-prima", "p2-vita", "p3-cultura", "p4-sport", "p5-giovani",
         "p6-approfondimento", "p7-lingua", "p8-valutazione"]

def span(t):
    txt = ''.join(t.itertext())
    try:
        x = float(t.get('x')); y = float(t.get('y')); size = float(t.get('font-size'))
    except (TypeError, ValueError):
        return None
    bold = t.get('font-weight') in ('700', 'bold')
    fam = t.get('font-family', '')
    kind = 'serif' if 'Serif' in fam else 'sans'
    w = text_w(txt, kind, bold, size)
    anchor = t.get('text-anchor')
    lo, hi = (x - w / 2, x + w / 2) if anchor == 'middle' else ((x - w, x) if anchor == 'end' else (x, x + w))
    font = _font(kind, bold, int(size))
    asc, desc = font.getmetrics() if font else (size, 0)
    return (lo, hi, y - asc, y + desc, txt, y, size)

print("== 1. RIGHT-EDGE (ADVANCE) frame band [40,1910], outer frame 28 ==")
flags = 0
for p in PAGES:
    root = ET.parse(os.path.join(ED, p + ".svg")).getroot()
    for t in root.iter(NS + 'text'):
        s = span(t)
        if not s: continue
        lo, hi, _, _, txt, y, _ = s
        if lo < 28 or hi > 1910:
            print(f"  FLAG {p} y={y} [{lo:.1f},{hi:.1f}] {txt[:60]!r}"); flags += 1
print("  RIGHTEDGE flags:", flags)

print("== 2. SAME-BASELINE furniture bands (P1 top y=92, footers y=2624, P1 band y=478/522) ==")
flags = 0
for p in PAGES:
    root = ET.parse(os.path.join(ED, p + ".svg")).getroot()
    by_y = {}
    for t in root.iter(NS + 'text'):
        s = span(t)
        if not s: continue
        lo, hi, _, _, txt, y, _ = s
        if y in (92.0, 2624.0, 478.0, 522.0):
            by_y.setdefault(y, []).append((lo, hi, txt))
    for y, spans in by_y.items():
        spans.sort()
        for (l1, h1, t1), (l2, h2, t2) in zip(spans, spans[1:]):
            if h1 > l2:
                print(f"  FLAG {p} y={y} {t1[:40]!r} vs {t2[:40]!r}"); flags += 1
print("  ROW flags:", flags)

print("== 3. P1 top-band gaps ==")
root = ET.parse(os.path.join(ED, "p1-prima.svg")).getroot()
band = []
for t in root.iter(NS + 'text'):
    s = span(t)
    if s and s[5] == 92.0: band.append((s[0], s[1], s[4]))
band.sort()
for b in band: print(f"  [{b[0]:.1f},{b[1]:.1f}] {b[2][:60]!r}")
for (l1, h1, _), (l2, h2, _) in zip(band, band[1:]): print(f"  gap {l2-h1:.1f}")

print("== 4. P7 FRASI rule vs col3 ink bottom ==")
root = ET.parse(os.path.join(ED, "p7-lingua.svg")).getroot()
for el in root.iter():
    if el.tag == NS + 'line':
        try: x1, y1, x2, y2 = float(el.get('x1')), float(el.get('y1')), float(el.get('x2')), float(el.get('y2'))
        except (TypeError, ValueError): continue
        if y1 == y2 and 1600 < y1 < 1760: print(f"  line y={y1} x {x1}..{x2}")
    if el.tag == NS + 'rect':
        try: x, y, w, h = float(el.get('x')), float(el.get('y')), float(el.get('width')), float(el.get('height'))
        except (TypeError, ValueError): continue
        if 1600 < y < 1760 or 1600 < y + h < 1760: print(f"  rect x={x} y={y} w={w} h={h} fill={el.get('fill')}")
# col3 ink: text nodes with baseline y < 1724 (FRASI head) and y > 1560, in P7 clinic columns;
# report max ink bottom among all P7 text nodes with baseline < 1724, excluding footer/masthead
mx = 0; arg = None
for t in root.iter(NS + 'text'):
    s = span(t)
    if not s: continue
    lo, hi, top, bot, txt, y, size = s
    if 200 < y < 1724 and bot > mx: mx, arg = bot, (y, txt[:60], size)
print(f"  max ink bottom (baseline<1724): {mx:.1f} :: {arg}")
print("  FRASI heading y=1724; rule line to compare above")

print("== 5. P8 answer bottom ==")
root = ET.parse(os.path.join(ED, "p8-valutazione.svg")).getroot()
mx = 0; arg = None
for t in root.iter(NS + 'text'):
    s = span(t)
    if not s: continue
    lo, hi, top, bot, txt, y, size = s
    if y > 1382 and bot > mx: mx, arg = bot, (y, txt[:70], size)
print(f"  max answer-region ink bottom: {mx:.1f} :: {arg}")
print("  footer baseline 2624; footer zone starts 2580")

print("== 6. P6 chart labels vs later olive bars (baseline-anchored ink, ls) ==")
root = ET.parse(os.path.join(ED, "p6-approfondimento.svg")).getroot()
elems = []
for el in root.iter():
    if el.tag == NS + 'rect' and el.get('fill') == '#3e4c2a':
        elems.append(('rect', float(el.get('x')), float(el.get('y')), float(el.get('width')), float(el.get('height'))))
    elif el.tag == NS + 'text':
        elems.append(('text', el))
maxcov = 0.0; worst = None
for i, el in enumerate(elems):
    if el[0] != 'text': continue
    t = el[1]; txt = ''.join(t.itertext())
    if txt.strip() not in ("Torino", "Milano", "Bologna", "Roma", "Napoli", "3°", "4°", "5°", "9°", "12°"): continue
    try: x, y, size = float(t.get('x')), float(t.get('y')), float(t.get('font-size'))
    except (TypeError, ValueError): continue
    bold = t.get('font-weight') in ('700', 'bold')
    fam = t.get('font-family', ''); kind = 'serif' if 'Serif' in fam else 'sans'
    font = _font(kind, bold, int(size))
    if not font: continue
    asc, desc = font.getmetrics()
    ink = (x, y - asc, x + text_w(txt, kind, bold, size), y + desc)
    area = max(0, ink[2]-ink[0]) * max(0, ink[3]-ink[1])
    for el2 in elems[i+1:]:
        if el2[0] != 'rect': continue
        _, rx, ry, rw, rh = el2
        ox = max(0, min(ink[2], rx+rw) - max(ink[0], rx)); oy = max(0, min(ink[3], ry+rh) - max(ink[1], ry))
        cov = (ox*oy/area*100) if area else 0
        if cov > maxcov: maxcov, worst = cov, txt
print(f"  max chart-label coverage: {maxcov:.1f}% (threshold <30%) worst={worst!r}")

print("== 7. Frame-pressure spot checks: text ink vs outer frame ==")
# outer frame: any text ink with lo<40 or hi>1910 already covered in (1) via advance;
# ink-based: recompute with true ink boxes (getbbox) is the audit's job (0 flags).
# Here: P1 parola single-line note + P2 box title + P7 parola box last line
def find(p, frag):
    root = ET.parse(os.path.join(ED, p + ".svg")).getroot()
    return [(t.get('x'), t.get('y'), ''.join(t.itertext())) for t in root.iter(NS+'text') if frag in ''.join(t.itertext())]
print("  P1 parola note:", find("p1-prima", "el primer frío serio"))
print("  P2 box title:", find("p2-vita", "FRASE PER RICORDARE"))
print("  P7 parola last lines:", find("p7-lingua", "se prueba gratis"))
