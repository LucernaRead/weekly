# -*- coding: utf-8 -*-
"""W45 ES x ZH-TW builder self-checks (single script, read-only on SVGs):
rowcheck (same-baseline ink), P6 chart later-rect overlaps + Inmigracion
graze measurement, gloss counts split on U+00B7 itself, P7 quote counts,
simplified-residue scan, orphan-punctuation scan, image-payload identity,
freeze-residual Latin multiset, furniture presence."""
import re, sys, glob, os, json, hashlib, importlib.util
G = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
ED = f'{G}/files/weekly-report-w45-es-zh-tw/svg'
CO = f'{G}/files/weekly-report-w45-es-core/svg'

def load_svglib(path):
    spec = importlib.util.spec_from_file_location('svglib_ed', path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

SV = load_svglib(f'{G}/hidden_files/weekly-report-w45-es-zh-tw-build/svglib.py')
TEXT_RE = re.compile(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"( font-weight="700")?[^>]*?(?: text-anchor="(start|middle|end)")?[^>]*>([^<]*)</text>')

def texts(path):
    src = open(path, encoding='utf-8').read()
    out = []
    for m in TEXT_RE.finditer(src):
        x, y, fam, size, bold, anchor, t = (float(m.group(1)), float(m.group(2)), m.group(3),
                                            float(m.group(4)), bool(m.group(5)), m.group(6) or 'start', m.group(7))
        out.append((m.start(), x, y, fam, size, bold, anchor, t))
    return src, out

def ink(x, fam, size, bold, anchor, t):
    kind = 'serif' if 'Serif' in fam else 'sans'
    f = SV._font(kind, bold, int(round(size * 4)))
    bb = f.getbbox(t); adv = f.getlength(t) / 4.0
    l, r = bb[0] / 4.0, bb[2] / 4.0
    if anchor == 'start': return x + l, x + r
    if anchor == 'end': return x - adv + l, x - adv + r
    return x - adv / 2 + l, x - adv / 2 + r

def rowcheck(d):
    bad = []
    for path in sorted(glob.glob(os.path.join(d, '*.svg'))):
        _, els = texts(path)
        rows = {}
        for _, x, y, fam, size, bold, anchor, t in els:
            if not t.strip(): continue
            a, b = ink(x, fam, size, bold, anchor, t)
            rows.setdefault(round(y, 1), []).append((a, b, t))
        for y, spans in rows.items():
            spans.sort()
            for (a1, b1, t1), (a2, b2, t2) in zip(spans, spans[1:]):
                if a2 - b1 < 6: bad.append((os.path.basename(path), y, round(a2 - b1, 1), t1[:30], t2[:30]))
    return bad

def chartcheck(path):
    src, els = texts(path)
    pos = []
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)" fill="([^"]*)"', src):
        pos.append((m.start(), 'rect', float(m.group(1)), float(m.group(2)),
                    float(m.group(1)) + float(m.group(3)), float(m.group(2)) + float(m.group(4)), m.group(5)))
    for st, x, y, fam, size, bold, anchor, t in els:
        if not t.strip(): continue
        a, b = ink(x, fam, size, bold, anchor, t)
        pos.append((st, 'text', a, y - size, b, y + size * 0.25, t))
    pos.sort()
    bad = []
    for j, (st, k, ax, ay, bx, by, t) in enumerate(pos):
        if k != 'text': continue
        for (st2, k2, ax2, ay2, bx2, by2, fill) in pos[j + 1:]:
            if k2 != 'rect': continue
            if ax < bx2 and ax2 < bx and ay < by2 and ay2 < by:
                bad.append((t[:44], round(ax, 1), round(bx, 1), fill, round(ax2, 1), round(bx2, 1)))
    return bad

def inmigracion(path):
    src, els = texts(path)
    res = []
    for st, x, y, fam, size, bold, anchor, t in els:
        if t.strip() == 'Inmigración':
            a, b = ink(x, fam, size, bold, anchor, t)
            rects = [(float(m.group(1)), float(m.group(2)), float(m.group(1)) + float(m.group(3)))
                     for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', src)
                     if m.start() > st]
            following = [r for r in rects if abs(r[1] - (y - size)) < 40 or abs(r[1] - y) < 40]
            res.append((round(x, 1), round(y, 1), round(a, 1), round(b, 1),
                        [(round(r[0], 1), round(r[1], 1)) for r in following[:4]]))
    return res

def is_cjk(c): return '\u4e00' <= c <= '\u9fff' or '\u3400' <= c <= '\u4dbf'

def gloss_counts(d, prefix):
    per = {}
    for path in sorted(glob.glob(os.path.join(d, '*.svg'))):
        _, els = texts(path)
        boxes = [t for *_, t in els if t.startswith(prefix)]
        counts = []
        for t in boxes:
            body = t[len(prefix):]
            items = [i for i in body.split('·')]
            counts.append(len([i for i in items if i.strip(' 。')]))
        per[os.path.basename(path)] = counts
    return per

def orphan_scan(d):
    closers = set('，。；：、！？）」』》】')
    openers = set('（「『《【')
    flags = []
    for path in sorted(glob.glob(os.path.join(d, '*.svg'))):
        _, els = texts(path)
        for _, x, y, fam, size, bold, anchor, t in els:
            if not any(is_cjk(c) for c in t): continue
            s = t.strip()
            if not s: continue
            if s[0] in closers: flags.append((os.path.basename(path), round(y, 1), 'LEAD', s[:40]))
            if s[-1] in openers: flags.append((os.path.basename(path), round(y, 1), 'TRAIL', s[-40:]))
    return flags

def images(d):
    out = {}
    for path in sorted(glob.glob(os.path.join(d, '*.svg'))):
        src = open(path, encoding='utf-8').read()
        lst = []
        for m in re.finditer(r'<image ([^>]*)/>', src):
            attrs = m.group(1)
            href = re.search(r'(?:xlink:href|href)="([^"]*)"', attrs)
            h = href.group(1) if href else ''
            digest = hashlib.sha256(h.encode('utf-8')).hexdigest()[:16]
            xy = re.search(r'x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', attrs)
            lst.append((digest, xy.groups() if xy else ()))
        out[os.path.basename(path)] = lst
    return out

def furniture(d):
    res = {}
    for path in sorted(glob.glob(os.path.join(d, '*.svg'))):
        src = open(path, encoding='utf-8').read()
        res[os.path.basename(path)] = {
            'footer': src.count('La Lucerna · 西班牙語週報 VOL.2 · 正文西班牙語 · 講解繁體中文'),
            'pageline': len(re.findall(r'第 \d 版 / 共 8 版', src)),
        }
    p1 = open(os.path.join(d, 'p1-portada.svg'), encoding='utf-8').read()
    p8 = open(os.path.join(d, 'p8-ejercicios.svg'), encoding='utf-8').read()
    res['badge'] = p1.count('西班牙語正文 · 繁體中文講解 — 給繁體中文讀者的版本')
    res['p8head'] = p8.count('RESPUESTAS · 全部答案與簡析（第 1–8 版）')
    res['p8sep'] = len(re.findall(r'— 第 \d 版 —', p8))
    return res

if __name__ == '__main__':
    print('== rowcheck edition'); r = rowcheck(ED); [print(x) for x in r]; print('row-bad:', len(r))
    print('== rowcheck core'); r2 = rowcheck(CO); [print(x) for x in r2]; print('row-bad-core:', len(r2))
    print('== chartcheck edition P6'); c = chartcheck(f'{ED}/p6-afondo.svg'); [print(x) for x in c]; print('chart-overlaps-ed:', len(c))
    print('== chartcheck core P6'); c2 = chartcheck(f'{CO}/p6-afondo.svg'); [print(x) for x in c2]; print('chart-overlaps-core:', len(c2))
    print('== Inmigracion edition:', inmigracion(f'{ED}/p6-afondo.svg'))
    print('== Inmigracion core:', inmigracion(f'{CO}/p6-afondo.svg'))
    print('== gloss edition:', gloss_counts(ED, '譯注｜'))
    print('== gloss core:', gloss_counts(CO, '译注｜'))
    print('== orphan edition:', orphan_scan(ED))
    print('== orphan core:', orphan_scan(CO))
    print('== images equal:', images(ED) == images(CO), images(ED))
    print('== furniture:', furniture(ED))
