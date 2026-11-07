# -*- coding: utf-8 -*-
"""IT x ZH-TW W45 recovery audit (r1). Read-only: never imports content modules,
never writes into files/ dirs. Uses tools venv (PIL + occlusion_audit ink boxes)."""
import re, sys, json, hashlib, unicodedata
from collections import Counter
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as OA

BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
CORE = BASE + '/files/weekly-report-w45-it-core/svg'
ED = BASE + '/files/weekly-report-w45-it-zh-tw/svg'
W43ED = BASE + '/files/weekly-report-it-zh-tw/svg'
ZHTWCORE = BASE + '/files/weekly-report-zh-tw-it/svg'
PAGES = ['p1-prima','p2-vita','p3-cultura','p4-sport','p5-giovani','p6-approfondimento','p7-lingua','p8-valutazione']
CJK = re.compile(r'[\u4e00-\u9fff]')

def texts(path):
    s = open(path, encoding='utf-8').read()
    return re.findall(r'<text\b[^>]*>(.*?)</text>', s, re.S), s

def strip_cjk(t):
    return CJK.sub('', t)

print('=== A. stripped (non-CJK) multiset diff per page ===')
for p in PAGES:
    tc, _ = texts(f'{CORE}/{p}.svg'); te, _ = texts(f'{ED}/{p}.svg')
    dc = Counter(strip_cjk(t) for t in tc); de = Counter(strip_cjk(t) for t in te)
    only_c = list((dc - de).elements()); only_e = list((de - dc).elements())
    print(f'-- {p}: core-only {len(only_c)} edition-only {len(only_e)}')
    for t in only_c: print('   CORE-only:', repr(t))
    for t in only_e: print('   ED-only  :', repr(t))

print('=== B. 桥接 scan (edition SVGs + build content files) ===')
import glob
for path in sorted(glob.glob(ED + '/*.svg')) + sorted(glob.glob(BASE + '/hidden_files/weekly-report-w45-it-zh-tw-build/content*.py')):
    s = open(path, encoding='utf-8').read()
    print(f'  {path.split("/")[-1]}: 桥接={s.count("桥接")} 桥={s.count("桥")}')

print('=== C. quote counts per page core vs edition ===')
for p in PAGES:
    _, sc = texts(f'{CORE}/{p}.svg'); _, se = texts(f'{ED}/{p}.svg')
    row = {}
    for ch, name in [('“','ldquo'),('”','rdquo'),('‘','lsquo'),('’','rsquo'),('「','lcorner'),('」','rcorner'),('«','laquo'),('»','raquo'),('"','ascii-dquote')]:
        row[name] = (sc.count(ch), se.count(ch))
    print(f'  {p}: ' + ' '.join(f'{k}={v[0]}->{v[1]}' for k, v in row.items() if v[0] or v[1]))

print('=== D1. union-charset check: edition chars NOT in (W43 ITxZHTW ∪ W43 ZHTWxIT) ===')
union = set()
for d in (W43ED, ZHTWCORE):
    for p in glob.glob(d + '/*.svg'):
        union |= set(CJK.findall(open(p, encoding='utf-8').read()))
print(f'  union size: {len(union)}')
edchars = Counter()
for p in PAGES:
    t, _ = texts(f'{ED}/{p}.svg')
    for x in t: edchars.update(CJK.findall(x))
novel = sorted(set(edchars) - union)
print(f'  edition distinct CJK: {len(edchars)}; NOT in union: {len(novel)} -> {novel}')
for ch in novel:
    ctxs = []
    for p in PAGES:
        t, _ = texts(f'{ED}/{p}.svg')
        for x in t:
            if ch in x: ctxs.append(f'{p}:{x[:80]}')
    for c in ctxs[:4]: print(f'    {ch}: {c}')

print('=== D2. s2twp-variant scan: edition chars where s2twp(c)!=c ===')
from opencc import OpenCC
conv = OpenCC('s2twp')
sus = {}
for ch in edchars:
    if conv.convert(ch) != ch: sus[ch] = conv.convert(ch)
print(f'  variant chars in edition: {sus}')
for ch in sus:
    ctxs = []
    for p in PAGES:
        t, _ = texts(f'{ED}/{p}.svg')
        for x in t:
            if ch in x: ctxs.append(f'{p}:{x[:90]}')
    for c in ctxs[:6]: print(f'    {ch}-> {sus[ch]}: {c}')

print('=== D3. mainland-vocab scan (simplified forms must be 0; TW forms noted) ===')
all_ed = ''
for p in PAGES:
    t, _ = texts(f'{ED}/{p}.svg'); all_ed += ''.join(t)
pairs = [('代码','代碼'),('比赛项目','比賽項目'),('报道','報導'),('集市','市集'),('片语','詞組'),('片語','詞組'),
         ('软件','軟體'),('视频','影片'),('打印机','印表機'),('网络','網路'),('信息','資訊'),('数据','數據'),
         ('周报','週報'),('意大利语','義大利語'),('意大利','義大利')]
for sc, tc in pairs:
    print(f'  {sc}={all_ed.count(sc)} {tc}={all_ed.count(tc)}')

print('=== E. P7 gold sentences 2x + labels (joined, whitespace-normalised) ===')
def joined(d):
    out = []
    for p in PAGES:
        t, _ = texts(f'{d}/{p}.svg'); out.append(' '.join(t))
    return re.sub(r'\s+', ' ', ' '.join(out))
je = joined(ED); jc = joined(CORE)
quotes = ['arriva il primo freddo vero della stagione','Non è una certezza, è una probabilità',
          'il 2 novembre è la Commemorazione dei defunti','Fa freddo, copriti bene!',
          'il pubblico può assaggiare gratis','il calcio non si ferma per il primo freddo',
          'la cultura continua','Una probabilità alta non è una certezza']
labels = ['Pagina 1','Pagina 1','Pagina 2','Pagina 2','Pagina 3','Pagina 4','Pagina 5','Pagina 6']
for q, lb in zip(quotes, labels):
    print(f'  {q[:50]!r}: core={jc.count(q)} ed={je.count(q)} label {lb}: core={jc.count(lb)} (P7 gold label counts checked on P7 below)')
t7, _ = texts(f'{ED}/p7-lingua.svg'); j7 = re.sub(r'\s+', ' ', ' '.join(t7))
t7c, _ = texts(f'{CORE}/p7-lingua.svg'); j7c = re.sub(r'\s+', ' ', ' '.join(t7c))
for q, lb in zip(quotes, labels):
    print(f'    P7-only {q[:40]!r}: core={j7c.count(q)} ed={j7.count(q)}; ({lb}) on P7: core={j7c.count(lb)} ed={j7.count(lb)}')

print('=== F. gloss counts (source gloss() strings split on ·) ===')
for label, d in [('core-build', BASE + '/hidden_files/weekly-report-w45-it-build'),
                 ('ed-build', BASE + '/hidden_files/weekly-report-w45-it-zh-tw-build')]:
    tot = 0
    for f, pg in [('content12.py','P2'),('content34.py','P3'),('content34.py','P4'),('content56.py','P5'),('content56.py','P6')]:
        s = open(f'{d}/{f}', encoding='utf-8').read()
        for m in re.finditer(r'\.gloss\("([^"]*)"\)', s):
            items = [x for x in m.group(1).split('·')]
            print(f'  {label} {pg}: {len(items)} items: {[x.strip()[:28] for x in items]}')
            tot += len(items)
    print(f'  {label} TOTAL: {tot}')

print('=== G. P6 chart-label coverage (true ink vs later rects) + rect multiset ===')
def parse_els(svg_text):
    els = []
    for m in OA.TAG_RE.finditer(svg_text):
        if m.group('tcontent') is not None:
            a = OA.parse_attrs(m.group('tattrs')); els.append(('text', a, m.group('tcontent')))
        else:
            a = OA.parse_attrs(m.group('attrs')); els.append((m.group('tag'), a, None))
    return els
for d, name in [(CORE, 'core'), (ED, 'ed')]:
    s = open(f'{d}/p6-approfondimento.svg', encoding='utf-8').read()
    els = parse_els(s)
    rects = []
    worst = []
    for i, (tag, a, t) in enumerate(els):
        if tag == 'rect':
            try: rects.append((float(a.get('x', 0)), float(a.get('y', 0)), float(a.get('width', 0)), float(a.get('height', 0))))
            except ValueError: pass
        if tag == 'text' and t and t.strip():
            try:
                x = float(a.get('x', 0)); y = float(a.get('y', 0)); size = float(a.get('font-size', 20))
                bold = a.get('font-weight', '') in ('bold', '700')
                ib = OA.ink_box(t, a.get('font-family', ''), size, bold, x, y, a.get('text-anchor', 'start'))
            except Exception as e:
                continue
            if not ib: continue
            for (rx, ry, rw, rh) in rects:
                # only later-drawn rects: rects list holds rects seen BEFORE this text; need later ones -> handled below
                pass
    # second pass: later rects
    allrects = []
    for i, (tag, a, t) in enumerate(els):
        if tag == 'rect':
            try: allrects.append((i, float(a.get('x', 0)), float(a.get('y', 0)), float(a.get('width', 0)), float(a.get('height', 0))))
            except ValueError: pass
    for i, (tag, a, t) in enumerate(els):
        if tag == 'text' and t and t.strip():
            try:
                x = float(a.get('x', 0)); y = float(a.get('y', 0)); size = float(a.get('font-size', 20))
                bold = a.get('font-weight', '') in ('bold', '700')
                ib = OA.ink_box(t, a.get('font-family', ''), size, bold, x, y, a.get('text-anchor', 'start'))
            except Exception:
                continue
            if not ib: continue
            ia = max(0.0, (ib[2]-ib[0]) * (ib[3]-ib[1]))
            for (j, rx, ry, rw, rh) in allrects:
                if j <= i: continue
                ox = max(0.0, min(ib[2], rx+rw) - max(ib[0], rx)); oy = max(0.0, min(ib[3], ry+rh) - max(ib[1], ry))
                if ox > 0 and oy > 0 and ia > 0:
                    cov = ox*oy/ia
                    worst.append((cov, t[:60], (rx, ry, rw, rh)))
    worst.sort(reverse=True)
    print(f'  P6 {name}: texts-vs-later-rects overlaps: {len(worst)}; max coverage: {worst[0][0]:.3f} {worst[0][1]!r}' if worst else f'  P6 {name}: 0 overlaps')
    for cov, t, r in worst[:5]: print(f'    cov={cov:.3f} {t!r} rect={r}')
    # rect geometry multiset
    print(f'  P6 {name} rect multiset size: {len(allrects)}')
    if name == 'core': core_rects = Counter(allrects)
    else:
        print(f'  P6 rect multiset equal core: {Counter(allrects) == core_rects}')

print('=== H. same-baseline ink collisions (all pages, edition) ===')
for p in PAGES:
    s = open(f'{ED}/{p}.svg', encoding='utf-8').read()
    els = parse_els(s)
    by_y = {}
    for tag, a, t in els:
        if tag == 'text' and t and t.strip():
            try:
                x = float(a.get('x', 0)); y = float(a.get('y', 0)); size = float(a.get('font-size', 20))
                bold = a.get('font-weight', '') in ('bold', '700')
                ib = OA.ink_box(t, a.get('font-family', ''), size, bold, x, y, a.get('text-anchor', 'start'))
            except Exception:
                continue
            if ib: by_y.setdefault(round(y, 2), []).append((ib, t[:50]))
    hits = 0
    for y, items in by_y.items():
        items.sort(key=lambda z: z[0][0])
        for (b1, t1), (b2, t2) in zip(items, items[1:]):
            if b2[0] < b1[2] and not (b1[3] < b2[1] or b2[3] < b1[1]):
                print(f'  {p} y={y}: OVERLAP {t1!r} vs {t2!r}'); hits += 1
    print(f'  {p}: same-baseline collisions: {hits}')

print('=== I. ADVANCE right-edge + frame-pressure scan (edition) ===')
for p in PAGES:
    s = open(f'{ED}/{p}.svg', encoding='utf-8').read()
    els = parse_els(s)
    boxes = []
    for tag, a, t in els:
        if tag == 'rect':
            try: boxes.append((float(a.get('x', 0)), float(a.get('y', 0)), float(a.get('width', 0)), float(a.get('height', 0))))
            except ValueError: pass
    edge = 0; press = 0
    for tag, a, t in els:
        if tag == 'text' and t and t.strip():
            try:
                x = float(a.get('x', 0)); y = float(a.get('y', 0)); size = float(a.get('font-size', 20))
                bold = a.get('font-weight', '') in ('bold', '700')
                f = OA.get_font(a.get('font-family', ''), size, bold)
                adv = f.getlength(t) / OA.SCALE
                anchor = a.get('text-anchor', 'start')
                left = x - adv/2 if anchor == 'middle' else (x - adv if anchor == 'end' else x)
                right = left + adv
            except Exception:
                continue
            if right > 1950:
                print(f'  {p} PAGE-EDGE advance-right={right:.1f} {t[:60]!r}'); edge += 1
            for (rx, ry, rw, rh) in boxes:
                if ry <= y <= ry + rh and left < rx + rw < right:
                    print(f'  {p} PRESS right-border x={rx+rw:.0f} adv-right={right:.1f} {t[:60]!r}'); press += 1
                if ry <= y <= ry + rh and left < rx < right and left > rx:
                    pass
    print(f'  {p}: page-edge={edge} right-border-press={press}')

print('=== J. image payloads + credits ===')
for p in PAGES:
    _, sc = texts(f'{CORE}/{p}.svg'); _, se = texts(f'{ED}/{p}.svg')
    def imgs(s):
        return sorted(hashlib.sha256(x.encode()).hexdigest()[:12] for x in re.findall(r'xlink:href="data:image/[^;]+;base64,([^"]+)"', s))
    ic, ie = imgs(open(f'{CORE}/{p}.svg', encoding='utf-8').read()), imgs(open(f'{ED}/{p}.svg', encoding='utf-8').read())
    print(f'  {p}: core imgs {ic} ed imgs {ie} equal={ic == ie}')
for p in PAGES:
    t, _ = texts(f'{ED}/{p}.svg'); jt = ' '.join(t)
    for cred in ['Foto:', 'Wikimedia', 'dominio pubblico', 'CC0', 'Disegno della redazione']:
        if cred in jt: print(f'  credit {p}: {cred!r} present')
print('=== K. readers corner (edition P7 joined note) ===')
t7, _ = texts(f'{ED}/p7-lingua.svg')
note = '這是編輯部示例信，非真實來信；本期無最佳第 8 版作文。請寄來信，VOL.3 刊登真實來信與最佳作文！'
print('  joined-with-"":', note in ''.join(t7))
print('  joined-with-space normalised:', note in re.sub(r'\s+', '', ' '.join(t7)))
print('  (esempio della redazione) core:', '(esempio della redazione)' in ' '.join(texts(f'{CORE}/p7-lingua.svg')[0]), 'ed:', '(esempio della redazione)' in ' '.join(t7))
print('=== L. CJK added recount (multiset core vs edition) ===')
tot = 0
for p in PAGES:
    tc, _ = texts(f'{CORE}/{p}.svg'); te, _ = texts(f'{ED}/{p}.svg')
    cc = Counter(); ce = Counter()
    for x in tc: cc.update(CJK.findall(x))
    for x in te: ce.update(CJK.findall(x))
    added = sum((ce - cc).values()); tot += added
    print(f'  {p}: core {sum(cc.values())} ed {sum(ce.values())} added {added}')
print(f'  TOTAL added: {tot}')
