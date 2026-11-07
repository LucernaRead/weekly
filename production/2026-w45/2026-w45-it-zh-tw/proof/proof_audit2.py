#!/usr/bin/env python3
"""Independent proof audit part 2 for W45 IT x ZH-TW. Read-only, static
parsing only; never imports content modules."""
import re, sys, html, hashlib, glob
from collections import Counter
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as OA
import p8 as P8

BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
CORE = BASE + '/files/weekly-report-w45-it-core/svg'
ED = BASE + '/files/weekly-report-w45-it-zh-tw/svg'
W43ED = BASE + '/files/weekly-report-it-zh-tw/svg'
COREBUILD = BASE + '/hidden_files/weekly-report-w45-it-build'
EDBUILD = BASE + '/hidden_files/weekly-report-w45-it-zh-tw-build'
PAGES = ['p1-prima','p2-vita','p3-cultura','p4-sport','p5-giovani','p6-approfondimento','p7-lingua','p8-valutazione']

def texts(path):
    s = open(path, encoding='utf-8').read()
    return [html.unescape(re.sub(r'<[^>]+>', '', c)) for c in re.findall(r'<text\b[^>]*>(.*?)</text>', s, re.S)], s

def text_elems(path):
    """(attrs, text) in document order, attrs parsed properly."""
    s = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>', s, re.S):
        attrs = dict(re.findall(r'([\w-]+)="([^"]*)"', m.group(1)))
        out.append((attrs, html.unescape(re.sub(r'<[^>]+>', '', m.group(2)))))
    return out, s

print('=== A. badge geometry (own attrs, edition vs W43) ===')
for d, label in [(W43ED,'W43'),(ED,'W45')]:
    els, _ = text_elems(f'{d}/p1-prima.svg')
    for a, t in els:
        if '義大利語正文' in t:
            print(f'  {label}: x={a.get("x")} y={a.get("y")} font={a.get("font-family")} size={a.get("font-size")} weight={a.get("font-weight")} fill={a.get("fill")} anchor={a.get("text-anchor")} text={t!r}')

print('=== B. disclosure: all 3 rendered lines + box containment ===')
els, s7 = text_elems(f'{ED}/p7-lingua.svg')
idx = [i for i,(a,t) in enumerate(els) if '這是編輯部示例信' in t]
print('  disclosure start index:', idx)
for i in range(idx[0], idx[0]+3):
    a, t = els[i]
    print(f'  line{i-idx[0]}: x={a.get("x")} y={a.get("y")} size={a.get("font-size")} font={a.get("font-family")} text={t!r}')
joined_disc = ''.join(t for _, t in els[idx[0]:idx[0]+3])
print('  joined disclosure:', repr(joined_disc))
print('  target sentence:', repr('這是編輯部示例信，非真實來信；本期無最佳第 8 版作文。請寄來信，VOL.3 刊登真實來信與最佳作文！'))
print('  verbatim match:', joined_disc == '這是編輯部示例信，非真實來信；本期無最佳第 8 版作文。請寄來信，VOL.3 刊登真實來信與最佳作文！')
# reader-garden box: rects on P7 whose y-range contains disclosure lines
rects = re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*>', s7)
ys = [float(els[i][0]['y']) for i in range(idx[0], idx[0]+3)]
print('  disclosure y range:', min(ys), max(ys))
for r in rects:
    x, y, w, h = map(float, r)
    if y <= min(ys) and max(ys) <= y + h and w > 300:
        print(f'  containing rect: x={x} y={y} w={w} h={h}')
# disclosure ink bottom vs garden box bottom 1673.0 (OA true ink)
for i in range(idx[0], idx[0]+3):
    a, t = els[i]
    box = OA.ink_box(t, a.get('font-family',''), float(a.get('font-size','20')), a.get('font-weight')=='700', float(a.get('x',0)), float(a.get('y',0)), a.get('text-anchor','start'))
    print(f'  disclosure line{i-idx[0]} ink box: {box} bottom margin to 1673.0 = {1673.0 - box[3]:.2f}')
# letter Italian text: P7 letter lines in core vs edition (Italian-only strings)
tc, _ = texts(f'{CORE}/p7-lingua.svg'); te, _ = texts(f'{ED}/p7-lingua.svg')
print('  letter lt in core P7:', [t for t in tc if 'Sono Li' in t])
print('  letter lt in edition P7:', [t for t in te if 'Sono Li' in t])
print('  letter tag core:', '(esempio della redazione)' in tc, 'edition:', '(esempio della redazione)' in te)

print('=== C. P8 full key compare (p8.py extract, all 150) ===')
cres, _ = P8.extract(f'{CORE}/p8-valutazione.svg', 150)
eres, _ = P8.extract(f'{ED}/p8-valutazione.svg', 150)
ckeys = {n: v['key'] for n, v in cres.items() if isinstance(n, int)}
ekeys = {n: v['key'] for n, v in eres.items() if isinstance(n, int)}
cnoted = sorted(n for n, v in cres.items() if isinstance(n, int) and v['has_note'])
enoted = sorted(n for n, v in eres.items() if isinstance(n, int) and v['has_note'])
print(f'  core noted set size={len(cnoted)} edition noted set size={len(enoted)} sets equal={cnoted==enoted}')
print(f'  keys dict sizes: core={len(ckeys)} edition={len(ekeys)}')
diffs = [n for n in range(1, 151) if P8.norm(ckeys[n]) != P8.norm(ekeys[n])]
print(f'  full keydiff (all 150 compared, norm): {diffs}')
for n in diffs:
    print(f'    #{n}: core key={ckeys[n]!r} edition key={ekeys[n]!r} core seg={cres[n]["seg"]!r} edition seg={eres[n]["seg"]!r}')
    print(f'      edition seg first-seg before " — " == core key? {eres[n]["seg"].split(" — ")[0].strip() == ckeys[n]}')
p8els, _ = text_elems(f'{ED}/p8-valutazione.svg')
for n in diffs:
    hits = [t for _, t in p8els if re.match(rf'^{n}\.', t.strip())]
    print(f'    printed raw line #{n} (edition): {hits}')
for n in [140, 150]:
    print(f'    control #{n}: core key={ckeys.get(n)!r} edition key={ekeys.get(n)!r} equal={ckeys.get(n)==ekeys.get(n)}')
from opencc import OpenCC
conv = OpenCC('s2twp')
bad = []
for n in range(1, 151):
    seg = eres[n]['seg']
    if ' — ' in seg:
        note = seg.split(' — ', 1)[1]
        for ch in note:
            if '\u4e00' <= ch <= '\u9fff' and conv.convert(ch) != ch and ch not in ('里','栗'):
                bad.append((n, ch, note))
print(f'  P8 printed-note simplified-variant chars (excl 里/栗): count={len(bad)} {bad[:20]}')
# P8 change-line closure: every P8 text string that differs core vs edition must be in registered classes
tc8, _ = texts(f'{CORE}/p8-valutazione.svg'); te8, _ = texts(f'{ED}/p8-valutazione.svg')
dc8, de8 = Counter(tc8), Counter(te8)
print(f'  P8 string multiset: core-only {len(list((dc8-de8).elements()))} edition-only {len(list((de8-dc8).elements()))}')
for t in sorted(set((dc8-de8).elements()) | set((de8-dc8).elements())):
    print(f'    diff-string: {t!r}')

print('=== D. gold sentences 2x ===')
# gold block in content7 source: quotes list with (q, cn, pg)
for label, d in [('core', COREBUILD), ('edition', EDBUILD)]:
    s = open(f'{d}/content7.py', encoding='utf-8').read()
    m = re.search(r'quotes\s*=\s*\[(.*?)\]\s*\n', s, re.S)
    print(f'  {label} quotes block found: {bool(m)}')
    if m:
        qs = re.findall(r'\(\s*"([^"]+)"', m.group(1))
        print(f'  {label} gold quotes: {len(qs)}')
        for q in qs: print(f'    {q!r}')
# count in whole-book SVG text (whitespace-normalised)
def book_text(d):
    out = []
    for p in PAGES:
        t, _ = texts(f'{d}/{p}.svg'); out.extend(t)
    return ' '.join(' '.join(out).split())
for d, label in [(CORE,'core'),(ED,'edition')]:
    bt = book_text(d)
    print(f'  {label} book text len: {len(bt)}')
    s = open(f'{EDBUILD}/content7.py', encoding='utf-8').read()
    m = re.search(r'quotes\s*=\s*\[(.*?)\]\s*\n', s, re.S)
    qs = re.findall(r'\(\s*"([^"]+)"', m.group(1)) if m else []
    for q in qs:
        inner = q.strip('«»')
        print(f'    {label} gold inner {inner[:40]!r}... quoted occurrences={bt.count(" ".join(q.split()))} inner occurrences={bt.count(" ".join(inner.split()))}')

print('=== E. static exercise expansion (no import, no build log) ===')
tot = Counter(); bypage = {}; bytype = Counter()
for f in ['content12.py','content34.py','content56.py','content7.py','content8.py']:
    s = open(f'{EDBUILD}/{f}', encoding='utf-8').read()
    cur = None
    # walk lines in order, tracking CURPAGE assignments
    for line in s.splitlines():
        mm = re.search(r'CURPAGE\[0\]\s*=\s*(\d+)', line)
        if mm: cur = int(mm.group(1))
        for lv, typ in re.findall(r'\.ex\(\s*"(A2|B1|B2)",\s*"([^"]+)"', line):
            tot[lv] += 1; bypage.setdefault(cur, Counter())[lv] += 1; bytype[typ] += 1
        for lv in re.findall(r'\.match_set\(\s*"(A2|B1|B2)"', line):
            pass
    # match_set items: count keys list length per call (static: keys arg is 3rd list; use the notes list count via keys [...] pattern in source order)
    for m in re.finditer(r'\.match_set\(\s*"(A2|B1|B2)",\s*"([^"]+)",\s*\[(.*?)\],\s*\[(.*?)\],\s*\[(.*?)\]', s, re.S):
        lv, typ, lefts, rights, keys = m.groups()
        n = keys.count('"') // 2
        tot[lv] += n; bytype[typ] += n
        # page for match_set: find nearest preceding CURPAGE in source
        pos = m.start()
        curs = re.findall(r'CURPAGE\[0\]\s*=\s*(\d+)', s[:pos])
        pg = int(curs[-1]) if curs else None
        bypage.setdefault(pg, Counter())[lv] += n
print(f'  total={sum(tot.values())} levels={dict(tot)}')
print(f'  by page: { {k: dict(v) for k, v in sorted(bypage.items())} }')
print(f'  page totals: { {k: sum(v.values()) for k, v in sorted(bypage.items())} }')
print(f'  by type: {dict(bytype)}')
# MODELO word count + core/edition equality
for d, label in [(COREBUILD,'core'),(EDBUILD,'edition')]:
    s = open(f'{d}/content8.py', encoding='utf-8').read()
    m = re.search(r'MODELO\s*=\s*\((.*?)\)\s*\nNWORDS', s, re.S)
    parts = re.findall(r'"([^"]*)"', m.group(1)) if m else []
    modelo = ' '.join(parts)
    print(f'  {label} MODELO words={len(modelo.split())} text={modelo!r}')
    print(f'  {label} MODELO == edition MODELO check stored')

print('=== F. gloss headwords: source equality + rendered presence ===')
def gloss_calls(path):
    s = open(path, encoding='utf-8').read()
    return [m.group(1) for m in re.finditer(r'gloss\(\s*"((?:[^"\\]|\\.)*)"', s)]
pagemap = {'content12.py': 2, 'content34.py': (3, 4), 'content56.py': (5, 6)}
for f in ['content12.py','content34.py','content56.py']:
    c = gloss_calls(f'{COREBUILD}/{f}'); e = gloss_calls(f'{EDBUILD}/{f}')
    for ci, (a, b) in enumerate(zip(c, e)):
        ca, cb = a.split('·'), b.split('·')
        heads_c = [it.strip().split(' ')[0] for it in ca]
        heads_e = [it.strip().split(' ')[0] for it in cb]
        # headword = Italian token(s) before first CJK char
        def head(it):
            mm = re.search(r'[\u4e00-\u9fff]', it)
            return it[:mm.start()].strip() if mm else it.strip()
        hc = [head(it) for it in ca]; he = [head(it) for it in cb]
        pg = pagemap[f] if not isinstance(pagemap[f], tuple) else pagemap[f][ci]
        rendered, _ = texts(f'{ED}/{PAGES[pg-1]}.svg')
        rendered_joined = ' '.join(rendered)
        present = [h for h in he if h in rendered_joined]
        print(f'  {f} call{ci} (P{pg}): core items={len(ca)} edition items={len(cb)} headwords equal={hc==he} rendered present={len(present)}/{len(he)}')
        if hc != he: print(f'    CORE heads={hc} ED heads={he}')

print('=== G. independent geometry ===')
# same-baseline ink overlap (README #10): parse with OA, group texts by (page, y) with ink boxes
for d, label in [(ED,'edition')]:
    total = 0
    for p in PAGES:
        els, W, H = OA.parse_svg(open(f'{d}/{p}.svg', encoding='utf-8').read())
        texts_els = [e for e in els if e.kind == 'text']
        by_y = {}
        for e in texts_els:
            box = OA.ink_box(e.text, e.attrs.get('font-family',''), float(e.attrs.get('font-size', 25)), e.attrs.get('font-weight')=='700', float(e.attrs.get('x',0)), float(e.attrs.get('y',0)), e.attrs.get('text-anchor','start'))
            by_y.setdefault(round(float(e.attrs.get('y',0)),2), []).append((e.text, box))
        for y, items in by_y.items():
            items.sort(key=lambda t: t[1][0])
            for (t1, b1), (t2, b2) in zip(items, items[1:]):
                if b2[0] < b1[2] - 0.5:
                    print(f'  SAME-BASELINE OVERLAP {p} y={y}: {t1!r} vs {t2!r}'); total += 1
    print(f'  same-baseline overlaps total: {total}')
# right-edge ADVANCE scan + footer band + box-frame pressure, PIL getlength
from PIL import ImageFont
import os
FONTDIR = '/usr/share/fonts/opentype/noto'
def font_for(fam, size, bold):
    base = 'NotoSerifCJK-Bold.ttc' if ('Serif' in fam and bold) else 'NotoSerifCJK-Regular.ttc' if 'Serif' in fam else 'NotoSansCJK-Bold.ttc' if bold else 'NotoSansCJK-Regular.ttc'
    idx = 3 if 'TC' in fam else 2
    try: return ImageFont.truetype(os.path.join(FONTDIR, base), int(float(size)), index=idx)
    except Exception: return ImageFont.truetype(os.path.join(FONTDIR, base), int(float(size)))
for d, label in [(ED,'edition')]:
    over = footer = 0
    for p in PAGES:
        els, _ = text_elems(f'{d}/{p}.svg')
        for a, t in els:
            if not t.strip(): continue
            f = font_for(a.get('font-family',''), a.get('font-size','25'), a.get('font-weight')=='700')
            adv = f.getlength(t)
            x = float(a.get('x', 0)); y = float(a.get('y', 0))
            anchor = a.get('text-anchor','start')
            right = x + adv if anchor == 'start' else x + adv/2 if anchor == 'middle' else x
            left = x if anchor == 'start' else x - adv/2 if anchor == 'middle' else x - adv
            if right > 1950 or left < 0:
                print(f'  RIGHT/LEFT EDGE {p}: {t[:40]!r} left={left:.1f} right={right:.1f}'); over += 1
            if y > 2580:
                # footer lines exempt? report all, then classify
                print(f'  BELOW-2580 {p}: y={y} {t[:40]!r}'); footer += 1
    print(f'  edge overflows: {over}; texts with y>2580: {footer} (footer band lines expected: check manually)')
# P6 chart: rect multiset core vs edition + label coverage via OA ink vs later rects
def rects(d, p):
    s = open(f'{d}/{p}.svg', encoding='utf-8').read()
    return Counter(re.findall(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', s))
rc, re_ = rects(CORE, 'p6-approfondimento'), rects(ED, 'p6-approfondimento')
print(f'  P6 rect multiset: core distinct={len(rc)} total={sum(rc.values())}; edition distinct={len(re_)} total={sum(re_.values())}; equal={rc==re_}')
if rc != re_:
    print(f'    core-only: {list((rc-re_).items())[:10]}'); print(f'    ed-only: {list((re_-rc).items())[:10]}')
for lab in ['Torino 3°','Milano 4°','Bologna 5°','Roma 9°','Napoli 12°',"DATI INVENTATI"]:
    t6, _ = texts(f'{ED}/p6-approfondimento.svg')
    print(f'  P6 label {lab!r} present: {any(lab in x for x in t6)}')
# P6 text ink vs later rects (OA parse order)
els, W, H = OA.parse_svg(open(f'{ED}/p6-approfondimento.svg', encoding='utf-8').read())
maxcov = 0; hits = 0
for i, e in enumerate(els):
    if e.kind != 'text': continue
    box = OA.ink_box(e.text, e.attrs.get('font-family',''), float(e.attrs.get('font-size',25)), e.attrs.get('font-weight')=='700', float(e.attrs.get('x',0)), float(e.attrs.get('y',0)), e.attrs.get('text-anchor','start'))
    for later in els[i+1:]:
        if later.kind == 'rect':
            rb = OA.shape_box(later)
            if rb:
                ox = max(0, min(box[2], rb[2]) - max(box[0], rb[0])); oy = max(0, min(box[3], rb[3]) - max(box[1], rb[1]))
                area = (box[2]-box[0])*(box[3]-box[1])
                cov = (ox*oy/area) if area else 0
                if cov > 0:
                    hits += 1; maxcov = max(maxcov, cov)
                    if cov >= 0.3: print(f'  P6 rect-cover >=30%: {e.text[:40]!r} cov={cov:.2f}')
print(f'  P6 text-vs-later-rect overlaps: {hits} sites, max coverage={maxcov:.3f} (gate <0.30)')

print('=== H. residue in shipped SVGs ===')
for pat in ['重阳','练习','�','意大利语','简体']:
    hits = []
    for p in PAGES:
        t, _ = texts(f'{ED}/{p}.svg')
        for x in t:
            if pat in x: hits.append((p, x))
    print(f'  pattern {pat!r}: {len(hits)} hits {hits[:3]}')
t4, _ = texts(f'{ED}/p4-sport.svg')
print('  P4 header strings:', [x for x in t4 if '第 4 版' in x or 'ESERCIZI' in x][:5])
print('=== I. flow terminal values in round-0 build log (no re-render) ===')
log = open(f'{EDBUILD}/build-log-r0.txt', encoding='utf-8').read()
for key in ['P1-headline', 'P7 col3', 'P6-ex', 'P8-keys']:
    print(f'  {key}: {[l for l in log.splitlines() if key in l]}')
print('=== J. W43 furniture geometry vs edition (footer/page-line/gloss) ===')
for d, label in [(W43ED,'W43'),(ED,'W45')]:
    els, _ = text_elems(f'{d}/p2-vita.svg')
    for a, t in els:
        if '週報 VOL' in t or '譯注' in t:
            print(f'  {label} P2: size={a.get("font-size")} font={a.get("font-family")} text={t[:60]!r}')
