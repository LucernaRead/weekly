# -*- coding: utf-8 -*-
"""Independent exercise inventory from shipped SVGs only (body markers, P8 keys excluded).
Marker = standalone 'N.' (or 'N-M.') text at exercise-column x (137/599/1061/1523);
level = the immediately preceding standalone A2/B1/B2 label. Run with tools venv python."""
import re, html, os
from collections import Counter
BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations/files'
PAGES = ['p1-voorpagina.svg', 'p2-leven.svg', 'p3-cultuur.svg', 'p4-sport.svg',
         'p5-jongeren.svg', 'p6-verdieping.svg', 'p7-taal.svg', 'p8-toets.svg']

def texts(d, pg):
    s = open(os.path.join(d, pg), encoding='utf-8').read()
    out = []
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>", s, re.S):
        a = m.group(1)
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()
        mm = re.search(r'x="([^"]*)"', a)
        out.append((float(mm.group(1)) if mm else 0, t))
    return out

def inventory(d):
    perpage, lvl = {}, {}
    for pg in PAGES:
        ts = texts(d, pg)
        hdr = next((i for i, (x, t) in enumerate(ts) if re.match(r'^—\s*PAGINA \d+\s*—$', t)), None)
        body = ts[:hdr] if hdr is not None else ts
        nums, pending = [], None
        for x, t in body:
            if t in ('A2', 'B1', 'B2'):
                pending = t
                continue
            if x not in (137.0, 599.0, 1061.0, 1523.0):
                continue
            if re.match(r'^\d{1,3}\.$', t):
                n = int(t[:-1]); nums.append(n); lvl[n] = pending; pending = None
            elif re.match(r'^\d{1,3}–\d{1,3}\.$', t):
                a, b = t[:-1].split('–')
                for n in range(int(a), int(b) + 1):
                    nums.append(n); lvl[n] = pending
                pending = None
        perpage[pg] = sorted(set(nums))
    alln = sorted({n for ns in perpage.values() for n in ns})
    return perpage, alln, Counter(lvl.values())

if __name__ == '__main__':
    for label, d in [('CORE', BASE + '/weekly-report-w45-nl-core/svg'),
                     ('ED', BASE + '/weekly-report-w45-nl-it/svg')]:
        pp, alln, cnt = inventory(d)
        print(label, 'total', len(alln), 'missing', sorted(set(range(1, 151)) - set(alln)), 'levels', dict(cnt))
        for pg, ns in pp.items():
            print(' ', pg, len(ns))
