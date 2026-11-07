# -*- coding: utf-8 -*-
"""JA x PT round-2 supplementary audits (venv PIL measurements).

Covers what the canonical occlusion audit does not: same-baseline ink
collisions, ADVANCE right-edge scan, full-page frame-line scan (rect
borders / lines drawn AFTER a text element crossing its ink), P6 chart
label coverage (baseline-anchored ink vs later bars), kinsoku line
starts, gloss counts, phrase 2x, image payloads, P8 note completeness
(byte-identical P8 lines vs core), word-level residue, keydiff detail.
"""
import re, sys, hashlib
from collections import Counter
from PIL import ImageFont

G = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
ED = G + '/files/weekly-report-w45-ja-pt/svg/'
CO = G + '/files/weekly-report-w45-ja-core/svg/'
EB = G + '/hidden_files/weekly-report-w45-ja-pt-build/'
PAGES = ['p1-hyoushi', 'p2-kurashi', 'p3-bunka', 'p4-supotsu',
         'p5-wakamono', 'p6-fukayomi', 'p7-kotoba', 'p8-tesuto']

import importlib.util as _ilu
_spec = _ilu.spec_from_file_location('occ', G + '/tools/occlusion_audit.py')
_occ = _ilu.module_from_spec(_spec); _spec.loader.exec_module(_occ)
ink_box = _occ.ink_box

def parse(svgpath):
    svg = open(svgpath, encoding='utf-8').read()
    els = []
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"(?: font-weight="(\d+)")?[^>]*?(?: text-anchor="(\w+)")?>([^<]*)</text>', svg):
        x, y = float(m.group(1)), float(m.group(2))
        fam = 'serif' if 'Serif' in m.group(3) else 'sans'
        size = float(m.group(4)); bold = m.group(5) == '700'
        anchor = m.group(6) or 'start'; txt = m.group(7)
        ib = ink_box(txt, fam, size, bold, x, y, anchor)
        adv = _occ.get_font(fam, size, bold).getlength(txt) / _occ.SCALE
        els.append(dict(x=x, y=y, size=size, txt=txt, anchor=anchor,
                        ink=ib, adv=adv))
    return els, None, svg

print('=== 1. same-baseline ink collisions (all pages) ===')
tot = 0
for pg in PAGES:
    els, _, _ = parse(ED + pg + '.svg')
    by = {}
    for e in els:
        by.setdefault(round(e['y'], 2), []).append(e)
    for y, grp in by.items():
        grp = sorted(grp, key=lambda e: e['ink'][0])
        for a, b in zip(grp, grp[1:]):
            if a['ink'][2] > b['ink'][0] + 0.5 and a['txt'].strip() and b['txt'].strip():
                # ignore identical-position duplicates (none expected)
                print(f'  {pg} y={y}: {a["txt"][:40]!r} OVERLAPS {b["txt"][:40]!r}')
                tot += 1
print('same-baseline collisions:', tot)

print('=== 2. ADVANCE right-edge scan (limit 1885.5) ===')
viol = 0
for pg in PAGES:
    els, _, _ = parse(ED + pg + '.svg')
    for e in els:
        if e['ink'] is None: continue
        if e['anchor'] == 'start': r = e['x'] + e['adv']
        elif e['anchor'] == 'middle': r = e['x'] + e['adv'] / 2
        else: r = e['x']
        if r > 1885.5:
            print(f'  {pg}: {e["txt"][:60]!r} adv_right={r:.1f} ink_right={e["ink"][2]:.1f}'); viol += 1
print('advance violations:', viol)

print('=== 3. frame-line scan: later-drawn rect borders/lines vs text ink ===')
# document-order aware: re-parse with positions
def parse_ordered(svgpath):
    svg = open(svgpath, encoding='utf-8').read()
    items = []  # (pos, kind, data)
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"(?: font-weight="(\d+)")?[^>]*?(?: text-anchor="(\w+)")?>([^<]*)</text>', svg):
        items.append((m.start(), 'text', m))
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*?(?:stroke-width="([\d.]+)")?[^>]*>', svg):
        items.append((m.start(), 'rect', m))
    for m in re.finditer(r'<line x1="([\d.]+)" y1="([\d.]+)" x2="([\d.]+)" y2="([\d.]+)"[^>]*stroke-width="([\d.]+)"', svg):
        items.append((m.start(), 'line', m))
    return sorted(items)
hits = 0
for pg in PAGES:
    svg = open(ED + pg + '.svg', encoding='utf-8').read()
    texts = []
    shapes = []
    for pos, kind, m in parse_ordered(ED + pg + '.svg'):
        if kind == 'text':
            x, y = float(m.group(1)), float(m.group(2))
            fam = 'serif' if 'Serif' in m.group(3) else 'sans'
            size = float(m.group(4)); bold = m.group(5) == '700'
            anchor = m.group(6) or 'start'; txt = m.group(7)
            ib = ink_box(txt, fam, size, bold, x, y, anchor)
            if ib is not None:
                texts.append((pos, ib, txt))
        elif kind == 'rect':
            rx, ry, rw, rh = map(float, m.groups()[:4])
            sw = float(m.group(5)) if m.group(5) else 0
            shapes.append((pos, ('rect', rx, ry, rw, rh, sw)))
        else:
            x1, y1, x2, y2, sw = map(float, m.groups())
            shapes.append((pos, ('line', x1, y1, x2, y2, sw)))
    for pos, ink, txt in texts:
        if not txt.strip():
            continue
        for spos, sh in shapes:
            if spos < pos:
                continue
            bad = False
            if sh[0] == 'rect':
                _, rx, ry, rw, rh, sw = sh; h = sw / 2
                # border segments vs ink box
                for (ex0, ey0, ex1, ey1) in [(rx, ry, rx + rw, ry), (rx, ry + rh, rx + rw, ry + rh),
                                             (rx, ry, rx, ry + rh), (rx + rw, ry, rx + rw, ry + rh)]:
                    if not (ex1 < ink[0] or ex0 > ink[2] or ey1 < ink[1] or ey0 > ink[3]):
                        # horizontal border crossing ink vertical span, or vertical crossing horizontal span
                        if (ey0 == ey1 and ink[1] <= ey0 <= ink[3] and ex0 < ink[2] and ex1 > ink[0]) or \
                           (ex0 == ex1 and ink[0] <= ex0 <= ink[2] and ey0 < ink[3] and ey1 > ink[1]):
                            bad = True
            else:
                _, x1, y1, x2, y2, sw = sh; h = sw / 2
                if y1 == y2 and ink[1] - h <= y1 <= ink[3] + h and x1 < ink[2] and x2 > ink[0]:
                    bad = True
                if x1 == x2 and ink[0] - h <= x1 <= ink[2] + h and y1 < ink[3] and y2 > ink[1]:
                    bad = True
            if bad:
                print(f'  {pg}: shape after text crosses ink of {txt[:50]!r}'); hits += 1
                break
print('frame-line hits:', hits)

print('=== 4. P6 chart labels vs later bars (coverage <30%) ===')
els, _, svg6 = parse(ED + 'p6-fukayomi.svg')
# bars: rects on P6 in chart area; use document order from raw svg
import re as _re
order = []
for m in _re.finditer(r'<(text|rect)[^>]*>', svg6):
    order.append(m.group(0)[:80])
# simpler: reuse parse_ordered approach for P6 only
texts6 = []
bars6 = []
for pos, kind, m in parse_ordered(ED + 'p6-fukayomi.svg'):
    if kind == 'text':
        x, y = float(m.group(1)), float(m.group(2))
        fam = 'serif' if 'Serif' in m.group(3) else 'sans'
        size = float(m.group(4)); bold = m.group(5) == '700'
        anchor = m.group(6) or 'start'; txt = m.group(7)
        ib = ink_box(txt, fam, size, bold, x, y, anchor)
        if ib is not None:
            texts6.append((pos, ib, txt))
    else:
        rx, ry, rw, rh = map(float, m.groups()[:4])
        bars6.append((pos, (rx, ry, rx + rw, ry + rh)))
maxcov = 0.0; worst = None
for pos, ink, txt in texts6:
    ia = max(0.0, ink[2] - ink[0]) * max(0.0, ink[3] - ink[1])
    if ia <= 0:
        continue
    for bpos, b in bars6:
        if bpos < pos:
            continue
        ix = max(0.0, min(ink[2], b[2]) - max(ink[0], b[0]))
        iy = max(0.0, min(ink[3], b[3]) - max(ink[1], b[1]))
        cov = ix * iy / ia
        if cov > maxcov:
            maxcov, worst = cov, txt
print(f'P6 max chart-label coverage: {maxcov:.3f} worst={worst!r}')

print('=== 5. kinsoku line starts ===')
NO_START = set('\u3002\u3001\uff0c\uff0e\uff01\uff1f\uff1a\uff1b\uff09\u300d\u300f\u3011\u30fc\u2026\u2025\u30fb')
print('NO_START size:', len(NO_START))
for pg in PAGES:
    for base, tag in [(ED, 'ed'), (CO, 'core')]:
        els, _, _ = parse(base + pg + '.svg')
        bad = [e['txt'] for e in els if e['txt'] and e['txt'][0] in NO_START]
        print(f'  {pg} {tag}: {len(bad)}', bad[:3])

print('=== 6. P8 keys flow end / P7 teaser ===')
els8, _, _ = parse(ED + 'p8-tesuto.svg')
ks = [e for e in els8 if e['y'] > 1328 and e['y'] < 2600]
print('P8 last keys baseline:', max(e['y'] for e in ks), 'count:', len(ks))

print('=== 7. gloss counts (split on U+00B7) ===')
def gloss_items(path, pat):
    src = open(path, encoding='utf-8').read()
    return [s for s in _re.findall(pat, src)]
for pg, f in [('p1', 'content12'), ('p2', 'content12'), ('p3', 'content34'),
              ('p4', 'content34'), ('p5', 'content56'), ('p6', 'content56')]:
    pass
# count gloss-box strings: lines containing the gloss separator inside .box/.gloss calls is fragile;
# instead count from rendered SVGs: gloss boxes carry prefix 'Nota — ' on feature pages.
for pg in PAGES[:6]:
    els, _, _ = parse(ED + pg + '.svg')
    cnt = 0
    for e in els:
        if e['txt'].startswith('Nota — '):
            cnt += len(e['txt'].split('·'))
    elsC, _, _ = parse(CO + pg + '.svg')
    cntC = 0
    for e in elsC:
        if '｜' in e['txt']:
            cntC += len(e['txt'].split('·'))
    print(f'  {pg}: edition gloss items={cnt} core={cntC}')
# P7 bridges from build code
for base, tag in [(EB, 'ed'), (G + '/hidden_files/weekly-report-w45-ja-build/', 'core')]:
    src = ''
    for f in ['content7.py']:
        src += open(base + f, encoding='utf-8').read()
    items = []
    for m in _re.finditer(r'\.bridge\("([^"]*)"\)', src):
        items += [s for s in m.group(1).split('·')]
    print(f'  P7 bridge items {tag}: {len(items)}')

print('=== 8. phrases 2x (blank-stripped) ===')
alltxt = ''
for pg in PAGES:
    els, _, _ = parse(ED + pg + '.svg')
    alltxt += ''.join(e['txt'] for e in els)
flat = _re.sub(r'\s+', '', alltxt)
quotes = ['文化の日は、11月3日（火よう日）です。', 'ゆっくり、ゆるく整える日本の11月です。',
          '『ゆる』は、無理をしない、ゆっくり、という意味です。', '鍋の材料が1か月早く並び始めました。',
          '伝統工芸と紅葉と光を、いっしょに楽しむことができます。', 'ソフトバンクが2連勝でスタートしました。',
          'ルールを守って、楽しいハロウィンにしましょう。', '紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。']
for q in quotes:
    print(f'  {flat.count(q)}x :: {q[:30]}')

print('=== 9. image payloads core vs edition ===')
for pg in PAGES:
    for base, tag in [(ED, 'ed'), (CO, 'core')]:
        svg = open(base + pg + '.svg', encoding='utf-8').read()
        imgs = _re.findall(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', svg)
        hs = [hashlib.sha256(i.encode()).hexdigest()[:12] for i in imgs]
        print(f'  {pg} {tag}: {len(imgs)} images {hs}')
        break
    svgE = open(ED + pg + '.svg', encoding='utf-8').read()
    svgC = open(CO + pg + '.svg', encoding='utf-8').read()
    iE = [hashlib.sha256(i.encode()).hexdigest()[:12] for i in _re.findall(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', svgE)]
    iC = [hashlib.sha256(i.encode()).hexdigest()[:12] for i in _re.findall(r'data:image/[^;]+;base64,([A-Za-z0-9+/=]+)', svgC)]
    print(f'  {pg} payload match: {iE == iC}')

print('=== 10. P8 note completeness: byte-identical keys-region lines ===')
def keys_lines(base):
    els, _, _ = parse(base + 'p8-tesuto.svg')
    return sorted(e['txt'] for e in els if e['y'] > 1328 and e['y'] < 2600)
ke, kc = keys_lines(ED), keys_lines(CO)
same = sorted(set(ke) & set(kc))
print('byte-identical P8 keys lines:', len(same))
for s in same:
    print('  IDENTICAL:', repr(s[:110]))
print('edition keys lines:', len(ke), 'core:', len(kc))
print('numbers edition:', len([s for s in ke if s[0].isdigit() or s.startswith('—')]))

print('=== 11. keydiff detail (extracted keys) ===')
sys.path.insert(0, G + '/tools')
import importlib.util
spec = importlib.util.spec_from_file_location('p8mod', G + '/tools/p8.py')
p8mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(p8mod)
ce, _ = p8mod.extract(ED + 'p8-tesuto.svg', 150)
cc, _ = p8mod.extract(CO + 'p8-tesuto.svg', 150)
for n in [1, 2, 5, 7, 8, 9, 29, 32, 65, 69, 78, 101, 113, 115, 117, 118, 137, 138, 140, 146, 147]:
    print(f'  #{n} core={cc.get(n)!r} ed={ce.get(n)!r}')
