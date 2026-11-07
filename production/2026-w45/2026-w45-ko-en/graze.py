# -*- coding: utf-8 -*-
"""Paint-order graze check: for every text element, test its anchor-aware
PIL advance box against every LATER-drawn rect/image box (stroke-expanded).
Advance boxes are a superset of true ink, so a zero result proves zero
ink coverage without relying on getbbox; any hit is a candidate for
pixel adjudication on the card PNG. Covers the canonical audit's
sub-30% blind spot (chart/table labels) and the later-rect graze class.
Usage: venv python graze.py <svg-dir>"""
import re, sys, os, glob

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import svglib

EL_RE = re.compile(r'<(rect|image|text|line|path)([^>]*?)(/?)>')
ATTR = lambda a, n: (re.search(r'%s="([^"]+)"' % n, a).group(1)
                     if re.search(r'%s="([^"]+)"' % n, a) else None)


def elements(path):
    s = open(path, encoding='utf-8').read()
    els = []
    for m in EL_RE.finditer(s):
        kind, attrs = m.group(1), m.group(2)
        if kind in ('line', 'path'):
            continue  # strokes: covered by the canonical audit's LINEX
        if kind == 'text':
            # text content is between this tag and </text>; find it
            end = s.find('</text>', m.end())
            txt = s[m.end():end]
            x = float(ATTR(attrs, 'x')); y = float(ATTR(attrs, 'y'))
            fs = float(ATTR(attrs, 'font-size'))
            fam = ATTR(attrs, 'font-family') or ''
            bold = ATTR(attrs, 'font-weight') == '700'
            anchor = ATTR(attrs, 'text-anchor') or 'start'
            w = svglib.text_w(txt, 'serif' if 'Serif' in fam else 'sans', bold, fs)
            # advance box: baseline y, approx top y-fs*0.85, bottom y+fs*0.25
            if anchor == 'middle':
                l, r = x - w / 2, x + w / 2
            elif anchor == 'end':
                l, r = x - w, x
            else:
                l, r = x, x + w
            els.append(('text', (l, y - fs * 0.85, r, y + fs * 0.25), txt[:50]))
        elif kind in ('rect', 'image'):
            x = float(ATTR(attrs, 'x') or 0); y = float(ATTR(attrs, 'y') or 0)
            w = float(ATTR(attrs, 'width')); h = float(ATTR(attrs, 'height'))
            sw = float(ATTR(attrs, 'stroke-width') or 0)
            els.append((kind, (x - sw / 2 - 1, y - sw / 2 - 1,
                               x + w + sw / 2 + 1, y + h + sw / 2 + 1), ''))
    return els


def main():
    d = sys.argv[1]
    total_hits = 0
    for f in sorted(glob.glob(os.path.join(d, '*.svg'))):
        els = elements(f)
        hits = []
        for i, (kind, box, txt) in enumerate(els):
            if kind != 'text':
                continue
            l1, t1, r1, b1 = box
            for kind2, box2, _ in els[i + 1:]:
                if kind2 not in ('rect', 'image'):
                    continue
                l2, t2, r2, b2 = box2
                ix = max(0, min(r1, r2) - max(l1, l2))
                iy = max(0, min(b1, b2) - max(t1, t2))
                if ix > 0 and iy > 0:
                    hits.append((txt, kind2, round(ix, 1), round(iy, 1)))
        print(f"{os.path.basename(f)}: later-rect/image advance-box hits = {len(hits)}")
        for h in hits:
            print('   ', h)
        total_hits += len(hits)
    print('TOTAL hits:', total_hits)


if __name__ == '__main__':
    main()
