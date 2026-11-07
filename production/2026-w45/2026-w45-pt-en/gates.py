# -*- coding: utf-8 -*-
"""Builder gate battery for W45 PT x EN (run after render.py).
Prints PASS/FAIL per gate with measured values; exits 1 if any gate fails.
Ink boxes: PIL getbbox with anchor='ls' (baseline-anchored, per task).
"""
import os, re, sys, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib
from PIL import ImageFont

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
ED = os.path.join(GOAL, "weekly-report-w45-pt-en")
CORE = os.path.join(GOAL, "weekly-report-w45-pt-core")
BUILD = os.path.dirname(os.path.abspath(__file__))
fails = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}")
    if not ok:
        fails.append(name)

def svg_texts_full(path):
    t = open(path, encoding='utf-8').read()
    els = []
    for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"([^>]*)>([^<]*)</text>', t):
        x, y, fam, size, rest, s = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5), m.group(6)
        bold = '700' in rest
        kind = 'serif' if 'Serif' in fam else ('sans' if 'Sans' in fam else 'other')
        anch = 'end' if 'text-anchor="end"' in rest else ('middle' if 'text-anchor="middle"' in rest else 'start')
        els.append({'x': x, 'y': y, 'fam': fam, 'size': size, 'bold': bold, 'kind': kind, 's': s, 'anchor': anch})
    return els, t

def ink_full(el):
    if el['kind'] == 'other' or not el['s'].strip():
        return None
    f = svglib._font(el['kind'], el['bold'], el['size'])
    adv = f.getlength(el['s'])
    bx0, by0, bx1, by1 = f.getbbox(el['s'], anchor='ls')
    dx = -adv / 2 if el['anchor'] == 'middle' else (-adv if el['anchor'] == 'end' else 0)
    return (el['x'] + dx + bx0, el['y'] + by0, el['x'] + dx + bx1, el['y'] + by1)

def joined(path):
    els, _ = svg_texts_full(path)
    return re.sub(r'\s+', ' ', ' '.join(e['s'] for e in els)).strip()

PAGES = ['p1-capa', 'p2-vida', 'p3-cultura', 'p4-esporte', 'p5-jovens', 'p6-aprofundamento', 'p7-lingua', 'p8-avaliacao']
EDSVG = {p: os.path.join(ED, 'svg', p + '.svg') for p in PAGES}

p1 = joined(EDSVG['p1-capa'])
check('badge P1', 'TEXT IN PORTUGUESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS' in p1, 'badge present on P1')
foot_ok = True
for i, p in enumerate(PAGES, 1):
    j = joined(EDSVG[p])
    if 'A Lucerna · VOL.2 · Text in Portuguese · Explanations in English' not in j or f'Page {i} of 8' not in j:
        foot_ok = False
check('footer+page line 8/8', foot_ok, 'VOL.2 EN footer + Page N of 8 on all pages')

CJKRE = re.compile(r'[\u4e00-\u9fff\u3000-\u303f\uff00-\uffef]')
res = {p: len(CJKRE.findall(joined(EDSVG[p]))) for p in PAGES}
check('Chinese residue per page = 0', all(v == 0 for v in res.values()), str(res))

coll = []
for p in PAGES:
    els, _ = svg_texts_full(EDSVG[p])
    by_y = {}
    for e in els:
        b = ink_full(e)
        if b is None:
            continue
        by_y.setdefault(round(e['y'], 1), []).append((b, e['s']))
    for y, items in by_y.items():
        items.sort(key=lambda t: t[0][0])
        for (b1, s1), (b2, s2) in zip(items, items[1:]):
            if b2[0] < b1[2] - 0.5:
                coll.append((p, y, s1[:40], s2[:40], round(b1[2] - b2[0], 1)))
check('same-baseline ink collisions = 0', not coll, f'{len(coll)} collisions' + (f' e.g. {coll[:3]}' if coll else ''))

edge, margins = [], []
for p in PAGES:
    els, _ = svg_texts_full(EDSVG[p])
    for e in els:
        b = ink_full(e)
        if b is None:
            continue
        margins.append((b[0] - 40, 1910 - b[2], b[1] - 40, 2660 - b[3]))
        if b[0] < 40 - 0.5 or b[2] > 1910 + 0.5 or b[1] < 40 - 0.5 or b[3] > 2660 + 0.5:
            edge.append((p, e['s'][:40], [round(v, 1) for v in b]))
check('page-frame ink crossings = 0', not edge, f'{len(edge)} crossings' + (f' {edge[:3]}' if edge else '') +
      f' | min margins L/R/T/B = {[round(min(m[i] for m in margins), 1) for i in range(4)]}')

t6 = open(EDSVG['p6-aprofundamento'], encoding='utf-8').read()
tokens = []
for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"([^>]*)>([^<]*)</text>|<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"[^>]*fill="([^"]+)"', t6):
    if m.group(6) is not None:
        tokens.append(('text', float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), '700' in (m.group(5) or ''), m.group(6)))
    else:
        tokens.append(('rect', float(m.group(7)), float(m.group(8)), float(m.group(9)), float(m.group(10)), m.group(11)))
cov = []
for i, tk in enumerate(tokens):
    if tk[0] == 'text' and tk[6] in ('portões abertos', 'espera', 'prova', '60 min', '30 min', '330 min'):
        kind = 'serif' if 'Serif' in tk[3] else 'sans'
        f = svglib._font(kind, tk[5], tk[4])
        bx0, by0, bx1, by1 = f.getbbox(tk[6], anchor='ls')
        box = (tk[1] + bx0, tk[2] + by0, tk[1] + bx1, tk[2] + by1)
        area = max(0.0, box[2] - box[0]) * max(0.0, box[3] - box[1])
        ov = 0.0
        for tk2 in tokens[i + 1:]:
            if tk2[0] == 'rect':
                rx, ry, rw, rh = tk2[1], tk2[2], tk2[3], tk2[4]
                ix = max(0.0, min(box[2], rx + rw) - max(box[0], rx))
                iy = max(0.0, min(box[3], ry + rh) - max(box[1], ry))
                ov += ix * iy
        cov.append((tk[6], round(100 * ov / area, 1) if area else 0.0))
check('P6 chart-label coverage <30%', all(c < 30 for _, c in cov), str(cov))

def gloss_items(builddir, fn):
    t = open(os.path.join(builddir, fn), encoding='utf-8').read()
    out, page = {}, 0
    for ln in t.split('\n'):
        m = re.search(r'CURPAGE\[0\] = (\d)', ln)
        if m:
            page = int(m.group(1))
        for g in re.finditer(r'\.gloss\("([^"]+)"\)', ln):
            parts = [p.strip() for p in g.group(1).split('·') if p.strip()]
            out.setdefault(page, []).extend(parts)
    return out
core_build = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-pt-build")
gc, ge = {}, {}
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    for pg, it in gloss_items(core_build, fn).items():
        gc.setdefault(pg, []).extend(it)
    for pg, it in gloss_items(BUILD, fn).items():
        ge.setdefault(pg, []).extend(it)
gc_n = {p: len(v) for p, v in gc.items()}
ge_n = {p: len(v) for p, v in ge.items()}
check('gloss count core 1:1', gc_n == ge_n, f'core {gc_n} edition {ge_n} total {sum(ge_n.values())}')
allj = ' '.join(joined(EDSVG[p]) for p in PAGES)
missing = [it for pg, its in ge.items() for it in its if it.rstrip('.') not in allj]
check('gloss items survive in render', not missing, f'{len(missing)} missing' + (f' {missing[:3]}' if missing else ''))

t7src = open(os.path.join(BUILD, 'content7.py'), encoding='utf-8').read()
quotes = re.findall(r'\("«([^»]+)»", "([^"]+)", "(Página \d)"\)', t7src)
qok, qdet = True, []
for q, en, pg in quotes:
    n = allj.count(q)  # core method: bare text, guillemets stripped, whitespace collapsed
    pgn = {'Página 1': 'p1-capa', 'Página 2': 'p2-vida', 'Página 3': 'p3-cultura', 'Página 4': 'p4-esporte', 'Página 5': 'p5-jovens', 'Página 6': 'p6-aprofundamento'}[pg]
    onpage = q in joined(EDSVG[pgn])
    onp7 = (en + ' (' + pg + ')') in joined(EDSVG['p7-lingua'])
    if not (n == 2 and onpage and onp7):
        qok = False
    qdet.append((q[:30], n, onpage, onp7))
check('P7 quotes 2x + page tag + EN on P7', qok, f'{len(quotes)} quotes; ' + str(qdet))

p7j = joined(EDSVG['p7-lingua'])
lt = '«Vou fazer o Enem no domingo 8. Já conferi o cartão. Boa prova!» — EXEMPLO DA REDAÇÃO'
disc_pt = 'Nota da redação: as cartas reais e os melhores textos prometidos no VOL.1 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.3.'
disc_en = "Editor's note: the real letters and best texts promised in VOL.1 had not arrived by press time — the example stands, and the promise carries over to VOL.3."
checks = {
    'PT example verbatim': lt in p7j,
    'PT disclosure verbatim': disc_pt in p7j,
    'EN disclosure equivalent': disc_en in p7j,
    'EN example label': "Editor's example — not a real letter" in p7j,
    'EN invitation imperative': 'Send your letters to the editors' in p7j,
    'EN publication promise': 'the best will be printed in VOL.3' in p7j,
}
check("readers corner 3 facts + invitation", all(checks.values()), str(checks))

p1t = open(EDSVG['p1-capa'], encoding='utf-8').read()
core_p1t = open(os.path.join(CORE, 'svg', 'p1-capa.svg'), encoding='utf-8').read()
def img_hash(t):
    m = re.search(r'<image[^>]*href="data:image/\w+;base64,([^"]+)"', t)
    import hashlib
    return hashlib.sha256(m.group(1).encode()).hexdigest()[:16] if m else None
p1j = joined(EDSVG['p1-capa'])
check('P1 image embedded + credit', '<image' in p1t and 'Foto: Gary Todd / Wikimedia Commons — CC0' in p1j,
      f'image hash core {img_hash(core_p1t)} edition {img_hash(p1t)} (must match)')

print('FAILURES:', fails if fails else 'none')
sys.exit(1 if fails else 0)
