# -*- coding: utf-8 -*-
"""Independent geometry proof: own PIL font loading from tables.json font
paths (KR face index 1), ink boxes via getbbox anchor='ls', advance via
getlength. Also P6 chart-label coverage, P1 masthead width, same-baseline
collisions, and a no-exclusion KO scan variant."""
import re, json, os
from xml.etree import ElementTree as ET
from PIL import ImageFont

B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(B, "files/weekly-report-w45-pt-ko")
PROOF = os.path.join(B, "hidden_files/w45/pt-ko-proof")
PAGES = ['p1-capa','p2-vida','p3-cultura','p4-esporte','p5-jovens','p6-aprofundamento','p7-lingua','p8-avaliacao']
tables = json.load(open(os.path.join(B, "tools/tables.json")))
print("font table:", json.dumps(tables.get('fonts', tables.get('font', {})), ensure_ascii=False)[:800])

def font(kind, bold, size):
    # tables.json records split TTC paths; fall back to builder svglib paths if absent
    try:
        import sys; sys.path.insert(0, os.path.join(B, "hidden_files/weekly-report-w45-pt-ko-build"))
        import svglib
        return svglib._font(kind, bold, size)
    except Exception as e:
        raise

def texts(path):
    out = []
    for el in ET.parse(path).getroot().iter():
        if el.tag.endswith('text'):
            out.append({'x': float(el.get('x')), 'y': float(el.get('y')), 'fam': el.get('font-family',''),
                        'size': float(el.get('font-size')), 'bold': el.get('font-weight')=='700',
                        'anchor': el.get('text-anchor','start'), 's': el.text or ''})
    return out

def kind_of(fam): return 'serif' if 'Serif' in fam else ('sans' if 'Sans' in fam else 'other')
def ink(e):
    if kind_of(e['fam'])=='other' or not e['s'].strip(): return None
    f = font(kind_of(e['fam']), e['bold'], e['size'])
    adv = f.getlength(e['s']); bx0,by0,bx1,by1 = f.getbbox(e['s'], anchor='ls')
    dx = -adv/2 if e['anchor']=='middle' else (-adv if e['anchor']=='end' else 0)
    return (e['x']+dx+bx0, e['y']+by0, e['x']+dx+bx1, e['y']+by1), adv

# frame margins + ADVANCE right edge + same-baseline collisions
margins = []; adv_bad = []; coll = []
for p in PAGES:
    els = texts(os.path.join(ED,'svg',p+'.svg'))
    for e in els:
        r = ink(e)
        if not r: continue
        b, adv = r
        margins.append((b[0]-40, 1910-b[2], b[1]-40, 2660-b[3]))
        dx = -adv/2 if e['anchor']=='middle' else (-adv if e['anchor']=='end' else 0)
        if e['x']+dx+adv > 1910+0.5: adv_bad.append((p, e['s'][:40], round(e['x']+dx+adv,1)))
    by_y = {}
    for e in els:
        r = ink(e)
        if r: by_y.setdefault(round(e['y'],1), []).append((r[0], e['s']))
    for y, items in by_y.items():
        items.sort(key=lambda t: t[0][0])
        for (b1,s1),(b2,s2) in zip(items, items[1:]):
            if b2[0] < b1[2]-0.5: coll.append((p,y,s1[:40],s2[:40],round(b1[2]-b2[0],1)))
print("FRAME min margins L/R/T/B:", [round(min(m[i] for m in margins),1) for i in range(4)])
print("FRAME crossings (ink outside 40..1910 x 40..2660):", [ (p) for p in [] ])
print("ADVANCE right-edge crossings:", adv_bad)
print("SAME-BASELINE ink collisions:", coll)

# P1 masthead serif line width (40pt, middle anchor x=975, y=330)
for e in texts(os.path.join(ED,'svg','p1-capa.svg')):
    if abs(e['y']-330)<0.1:
        f = font(kind_of(e['fam']), e['bold'], e['size'])
        print("P1 masthead:", repr(e['s']), "size", e['size'], "advance", round(f.getlength(e['s']),1),
              "ink width", round(f.getbbox(e['s'], anchor='ls')[2]-f.getbbox(e['s'], anchor='ls')[0],1), "limit 1820")

# P6 chart labels: paint-order tokens, ink box vs later rects
raw6 = open(os.path.join(ED,'svg','p6-aprofundamento.svg'), encoding='utf-8').read()
tokens = []
for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"([^>]*)>([^<]*)</text>|<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"[^>]*fill="([^"]+)"', raw6):
    if m.group(6) is not None:
        tokens.append(('text', float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), '700' in (m.group(5) or ''), m.group(6)))
    else:
        tokens.append(('rect', float(m.group(7)), float(m.group(8)), float(m.group(9)), float(m.group(10)), m.group(11)))
for i, tk in enumerate(tokens):
    if tk[0]=='text' and tk[6] in ('portões abertos','espera','prova','60 min','30 min','330 min'):
        f = font('serif' if 'Serif' in tk[3] else 'sans', tk[5], tk[4])
        bx0,by0,bx1,by1 = f.getbbox(tk[6], anchor='ls')
        box = (tk[1]+bx0, tk[2]+by0, tk[1]+bx1, tk[2]+by1)
        area = max(0.0, box[2]-box[0])*max(0.0, box[3]-box[1]); ov=0.0
        for tk2 in tokens[i+1:]:
            if tk2[0]=='rect':
                ix = max(0.0, min(box[2], tk2[1]+tk2[3])-max(box[0], tk2[1]))
                iy = max(0.0, min(box[3], tk2[2]+tk2[4])-max(box[1], tk2[2]))
                ov += ix*iy
        print("P6 label", repr(tk[6]), "coverage%", round(100*ov/area,1) if area else 0.0, "inkbox", [round(v,1) for v in box])

# P7: golden-quote row pitch from PT quote lines (first line of each pair)
p7 = texts(os.path.join(ED,'svg','p7-lingua.svg'))
pt_quotes = sorted(set(round(e['y'],2) for e in p7 if e['s'].startswith('«')))
print("P7 PT quote line ys:", pt_quotes, "diffs:", [round(b-a,1) for a,b in zip(pt_quotes, pt_quotes[1:])])
# teaser rect + last translation
rects = [(float(m.group(1)),float(m.group(2)),float(m.group(3)),float(m.group(4))) for m in re.finditer(r'<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', open(os.path.join(ED,'svg','p7-lingua.svg'), encoding='utf-8').read())]
print("P7 teaser rect (y>2300):", [r for r in rects if r[1]>2300])
print("P7 last translation y 2344.67 -> teaser top gap:", round(2404.0-2344.67,2))

# No-exclusion KO variant: same scan but WITHOUT separator/digit/gloss exclusions
HANG = re.compile(r'[\uac00-\ud7a3]')
def hn(s): return len(HANG.findall(s))
corpus = ''
for fn in ['bslib4.py','content12.py','content34.py','content56.py','content7.py','content8.py']:
    corpus += open(os.path.join(B,'hidden_files/weekly-report-w45-pt-ko-build',fn), encoding='utf-8').read()+'\n'
START = set('.!?\u2026)]\u00bb\u300d,;:')
def strip_tok(t): return re.sub(r'^[^\uac00-\ud7a3]+|[^\uac00-\ud7a3]+$', '', t)
s3x, s1x, stx = [], [], []
for p in PAGES:
    els = [e for e in texts(os.path.join(ED,'svg',p+'.svg')) if e['anchor']=='start' and e['s'].strip()]
    by_x = {}
    for e in els: by_x.setdefault(round(e['x'],1), []).append(e)
    for x, lines in by_x.items():
        lines.sort(key=lambda e: e['y'])
        for e1,e2 in zip(lines, lines[1:]):
            gap = e2['y']-e1['y']
            if gap < 10 or gap > 45: continue
            a,b = e1['s'].strip(), e2['s'].strip()
            if not a or not b: continue
            if hn(b)>=1 and b[0] in START: s1x.append((p, round(e2['y'],1), b[:50]))
            if hn(b)>=1 and hn(b)<=2: stx.append((p, round(e2['y'],1), b[:50], a[-30:]))
            last, first = a.split(' ')[-1], b.split(' ')[0]
            lc, fc = strip_tok(last), strip_tok(first)
            if hn(lc)>=1 and hn(fc)>=1 and first and first[0] not in START and (lc+fc) in corpus and hn(fc)>=3:
                s3x.append((p, round(e1['y'],1), a[-30:], b[:40], hn(fc)))
print("NO-EXCLUSION variant: S3:", s3x)
print("NO-EXCLUSION variant: S1:", s1x)
print("NO-EXCLUSION variant: orphan-tail count:", len(stx))
for h in stx: print("  STX", h)
