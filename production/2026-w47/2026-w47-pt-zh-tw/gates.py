# -*- coding: utf-8 -*-
"""Builder self-check for W47 PT core (zh-cn explanations). Adapted from the
W46 PT x EN gates.py: ink boxes via PIL getbbox anchor='ls'."""
import os, re, sys, html
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib

BUILD = os.path.dirname(os.path.abspath(__file__))
ED = BUILD
fails = []

def check(name, ok, detail=""):
    print(f"[{'PASS' if ok else 'FAIL'}] {name} :: {detail}")
    if not ok:
        fails.append(name)

def svg_texts_full(path):
    t = open(path, encoding='utf-8').read()
    els = []
    for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"([^>]*)>([^<]*)</text>', t):
        x, y, fam, size, rest, s = float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), m.group(5), html.unescape(m.group(6))
        bold = '700' in rest
        # Newsreader is the serif face (its name carries neither 'Serif'
        # nor 'Sans'); UnifrakturMaguntia (the P1 wordmark) stays 'other'
        # and is skipped by the ink checks, as in the W46 gates.
        kind = 'serif' if ('Serif' in fam or 'Newsreader' in fam) else ('sans' if 'Sans' in fam else 'other')
        anch = 'end' if 'text-anchor="end"' in rest else ('middle' if 'text-anchor="middle"' in rest else 'start')
        els.append({'x': x, 'y': y, 'fam': fam, 'size': size, 'bold': bold, 'kind': kind, 's': s, 'anchor': anch})
    return els, t

def text_bbox(x, y, s, kind, bold, size, anchor='start'):
    """Real ink bbox of a text element, via svglib's per-run PIL fonts
    (svglib._font was removed in the current toolkit; _pil + _runs is the
    supported path). Anchor 'ls': x is the left edge, y the baseline."""
    adv = svglib.text_w(s, kind, bold, size)
    dx = -adv / 2 if anchor == 'middle' else (-adv if anchor == 'end' else 0)
    boxes, cx = [], x + dx
    for t, cls in svglib._runs(s, kind, bold):
        f = svglib._pil(kind, bold, cls, size)
        bx0, by0, bx1, by1 = f.getbbox(t, anchor='ls')
        boxes.append((cx + bx0, y + by0, cx + bx1, y + by1))
        cx += f.getlength(t)
    return (min(b[0] for b in boxes), min(b[1] for b in boxes),
            max(b[2] for b in boxes), max(b[3] for b in boxes))

def ink_full(el):
    if el['kind'] == 'other' or not el['s'].strip():
        return None
    return text_bbox(el['x'], el['y'], el['s'], el['kind'], el['bold'], el['size'], el['anchor'])

def joined(path):
    els, _ = svg_texts_full(path)
    return re.sub(r'\s+', ' ', ' '.join(e['s'] for e in els)).strip()

def squashed(s):
    """Whitespace-insensitive form for substring checks. D5 splits one
    source string into several <text> runs (Latin/digits -> Newsreader,
    CJK stays), so joined() inserts a space where the source had none
    ('第 1 版' for '第1版', '2 比 2' for '2比2'). The characters and
    their order are unchanged (pdftotext still extracts '第1版／共8版');
    only the check comparison must ignore the split-induced spaces.
    Used ONLY for the two checks whose targets contain CJK+digit mixes;
    the other checks keep the strict joined() form (e.g. the VOL.3
    residue check must not match across a real 'VOL.3' citation)."""
    return re.sub(r'\s+', '', s)

PAGES = ['p1-capa', 'p2-vida', 'p3-cultura', 'p4-esporte', 'p5-jovens', 'p6-aprofundamento', 'p7-lingua', 'p8-avaliacao']
EDSVG = {p: os.path.join(ED, 'svg', p + '.svg') for p in PAGES}
for p in PAGES:
    assert os.path.exists(EDSVG[p]), p

p1 = joined(EDSVG['p1-capa'])
check('P1 VOL.4 + week dates', 'VOL. 4' in p1 and 'SEMANA DE 16 A 22 DE NOVEMBRO DE 2026' in p1, 'top strip')
check('P1 subtitle topics', 'CONSCIÊNCIA NEGRA' in p1 and 'GABARITO DO ENEM' in p1 and 'A FINAL DA COPA' in p1, 'subtitle line')
foot_ok = True
for i, p in enumerate(PAGES, 1):
    j = squashed(joined(EDSVG[p]))
    if squashed('A Lucerna 葡萄牙語週報 VOL.4 正文葡萄牙語 講解繁體中文') not in j or squashed(f'第{i}版／共8版') not in j:
        foot_ok = False
check('footer+page line 8/8', foot_ok, 'VOL.4 ZH-TW footer + page line on all pages')
allj = ' '.join(joined(EDSVG[p]) for p in PAGES)
check('no VOL.3 edition label residue', 'VOL. 3' not in allj and 'VOL. 2' not in allj and 'VOL.2' not in allj, 'VOL.3 may appear only as the cited promising issue in the P7 disclosure')
check('press-time note + final named', 'fechou em 10 de novembro' in allj and 'dia 6 de dezembro' in allj, 'P4 press-time note present; final date named')

# subtitle / strapline widths on P1
els1, _ = svg_texts_full(EDSVG['p1-capa'])
widths = {}
for e in els1:
    if abs(e['y'] - 330) < 0.5 or abs(e['y'] - 372) < 0.5:
        widths[round(e['y'])] = svglib.text_w(e['s'], e['kind'], e['bold'], e['size'])
check('P1 masthead lines fit 1820', all(w <= 1820 for w in widths.values()), str({k: round(v, 1) for k, v in widths.items()}))

# same-baseline collisions. Threshold 2.0px: PIL getbbox returns INTEGER
# pixel bounds, so every element's ink box rounds up to ~1px past its float
# advance on each edge — overlaps <= ~1.5px are rounding noise, not layout
# defects (a real defect in this build, P2 day-box labels, was ~18px).
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
            if b2[0] < b1[2] - 2.0:
                coll.append((p, y, s1[:40], s2[:40], round(b1[2] - b2[0], 1)))
check('same-baseline ink collisions = 0', not coll, f'{len(coll)} collisions' + (f' e.g. {coll[:3]}' if coll else ''))

# page-frame ink crossings
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

# P6 chart-label GRAZE coverage
t6 = open(EDSVG['p6-aprofundamento'], encoding='utf-8').read()
tokens = []
for m in re.finditer(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"([^>]*)>([^<]*)</text>|<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"[^>]*fill="([^"]+)"', t6):
    if m.group(6) is not None:
        tokens.append(('text', float(m.group(1)), float(m.group(2)), m.group(3), float(m.group(4)), '700' in (m.group(5) or ''), html.unescape(m.group(6))))
    else:
        tokens.append(('rect', float(m.group(7)), float(m.group(8)), float(m.group(9)), float(m.group(10)), m.group(11)))
cov = []
for i, tk in enumerate(tokens):
    if tk[0] == 'text' and tk[6] in ('dias úteis', 'fins de semana e feriado', '10 dias', '5 dias'):
        kind = 'serif' if ('Serif' in tk[3] or 'Newsreader' in tk[3]) else 'sans'
        box = text_bbox(tk[1], tk[2], tk[6], kind, tk[5], tk[4])
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

# gloss counts: split on '·' itself (lesson 21)
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
gc = {}
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    for pg, it in gloss_items(BUILD, fn).items():
        gc.setdefault(pg, []).extend(it)
gc_n = {p: len(v) for p, v in gc.items()}
check('gloss items enumerated', sum(gc_n.values()) > 0, f'{gc_n} total {sum(gc_n.values())}')
missing = [it.split()[0] for pg, its in gc.items() for it in its if it.split()[0].rstrip('.') not in allj]
check('gloss headwords survive in render', not missing, f'{len(missing)} missing' + (f' {missing[:3]}' if missing else ''))

# P7 quotes
t7src = open(os.path.join(BUILD, 'content7.py'), encoding='utf-8').read()
quotes = re.findall(r'\("«([^»]+)»", "([^"]+)", "(Página \d)"\)', t7src)
qok, qdet = True, []
for q, cn, pg in quotes:
    n = squashed(allj).count(squashed(q))
    pgn = {'Página 1': 'p1-capa', 'Página 2': 'p2-vida', 'Página 3': 'p3-cultura', 'Página 4': 'p4-esporte', 'Página 5': 'p5-jovens', 'Página 6': 'p6-aprofundamento'}[pg]
    onpage = squashed(q) in squashed(joined(EDSVG[pgn]))
    onp7 = squashed(cn + ' (' + pg + ')') in squashed(joined(EDSVG['p7-lingua']))
    if not (n == 2 and onpage and onp7):
        qok = False
    qdet.append((q[:30], n, onpage, onp7))
check('P7 quotes 2x + page tag + ZH-TW on P7', qok, f'{len(quotes)} quotes; ' + str(qdet))

# readers corner
p7j = joined(EDSVG['p7-lingua'])
lt = '«Vou aproveitar o feriadão para ler sobre Zumbi. Bom feriado!» — EXEMPLO DA REDAÇÃO'
disc_pt = 'Nota da redação: as cartas reais e os melhores textos do VOL.3 não chegaram até o fechamento — fica o exemplo, e a promessa passa para o VOL.5.'
disc_zh_tw = "編輯部說明：上期（VOL.3）承諾的真實來信與最佳作文截稿時未收到，本期仍刊示例，順延至下期（VOL.5）。"
p7nospace = re.sub(r'\s+', '', p7j)
checks = {
    'PT example verbatim': lt in p7j,
    'PT disclosure verbatim': disc_pt in p7j,
    'ZH-TW disclosure verbatim': re.sub(r'\s+', '', disc_zh_tw) in p7nospace,
    'ZH-TW example label': "編輯部示例，非真實來信" in p7nospace,
    'VOL.5 carry': 'VOL.5' in p7j,
}
check('readers corner disclosure', all(checks.values()), str(checks))

# images + credits on all 5 photo pages
p1t = open(EDSVG['p1-capa'], encoding='utf-8').read()
p3t = open(EDSVG['p3-cultura'], encoding='utf-8').read()
p5t = open(EDSVG['p5-jovens'], encoding='utf-8').read()
p7t = open(EDSVG['p7-lingua'], encoding='utf-8').read()
p8t = open(EDSVG['p8-avaliacao'], encoding='utf-8').read()
img_checks = {
    'P1 capoeira + credit': '<image' in p1t and 'Gravura: Johann Moritz Rugendas / Wikimedia Commons — Domínio público' in p1,
    'P3 zumbi + credit': '<image' in p3t and 'Pintura: Antônio Parreiras / Wikimedia Commons — Domínio público' in joined(EDSVG['p3-cultura']),
    'P5 estudo + credit': '<image' in p5t and 'Foto: Gary Todd / Wikimedia Commons — CC0' in joined(EDSVG['p5-jovens']),
    'P7 lusiadas + credit': '<image' in p7t and 'Domínio público / Wikimedia Commons' in joined(EDSVG['p7-lingua']),
    'P8 garrincha + credit': '<image' in p8t and 'Foto: Luis Dantas — Domínio público' in joined(EDSVG['p8-avaliacao']),
}
check('images embedded + credits 5/5', all(img_checks.values()), str(img_checks))

# P7 quotes vs preview box: last quote translation baseline must be < 2404
els7, _ = svg_texts_full(EDSVG['p7-lingua'])
qmax = max(e['y'] for e in els7 if e['y'] < 2404 and e['y'] > 1700)
check('P7 quotes clear of preview box', qmax < 2404, f'max quote-region baseline {qmax}')

# P1 headline length vs cover.mjs LIMITS.headline (other = 56, whitespace removed)
head = 'Consciência Negra: sexta é feriado em todo o país'
check('P1 headline <= 56 non-space chars', len(re.sub(r'\s+', '', head)) <= 56,
      f'{len(re.sub(chr(92)+"s+", "", head))} chars')

print('FAILURES:', fails if fails else 'none')
sys.exit(1 if fails else 0)
