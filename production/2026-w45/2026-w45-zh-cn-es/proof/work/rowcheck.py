# Independent same-baseline + chart-label ink check (own implementation, PIL true ink).
import re, sys, glob, os
from xml.etree import ElementTree as ET
from PIL import ImageFont

SS = 4
FONTS = {
    ('serif', True): ('/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc', 2),
    ('serif', False): ('/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc', 2),
    ('sans', True): ('/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', 2),
    ('sans', False): ('/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', 2),
    ('black', False): ('/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf', 0),
}
_cache = {}
def font_for(fam, size, weight):
    if 'Unifraktur' in (fam or ''):
        key = ('black', False)
    elif 'Serif' in (fam or ''):
        key = ('serif', weight == '700' or weight == 'bold')
    else:
        key = ('sans', weight == '700' or weight == 'bold')
    path, idx = FONTS[key]
    ck = (path, round(size * SS), idx)
    if ck not in _cache:
        _cache[ck] = ImageFont.truetype(path, int(round(size * SS)), index=idx)
    return _cache[ck]

def local(tag):
    return tag.split('}')[-1]

def walk(el, out):
    out.append(el)
    for c in el:
        walk(c, out)

def parse_texts(path):
    tree = ET.parse(path)
    elems = []
    walk(tree.getroot(), elems)
    texts = []  # (idx, x, y, size, text)
    rects = []  # (idx, x, y, w, h)
    for i, el in enumerate(elems):
        t = local(el.tag)
        if t == 'text':
            x = float(el.get('x', '0')); y = float(el.get('y', '0'))
            size = float(el.get('font-size', '20'))
            fam = el.get('font-family', '')
            wt = el.get('font-weight', '')
            anchor = el.get('text-anchor', 'start')
            s = ''.join(el.itertext())
            if not s.strip():
                continue
            f = font_for(fam, size, wt)
            bb = f.getbbox(s)  # at SS scale, relative to origin
            # getbbox returns (left, top, right, bottom) in font coords; ink left offset
            l, tp, r, b = [v / SS for v in bb]
            w = r - l
            if anchor == 'middle':
                x0 = x - w / 2 - l
            elif anchor == 'end':
                x0 = x - w - l
            else:
                x0 = x - l
            texts.append((i, x0, x0 + w, y, s, size))
        elif t == 'rect':
            try:
                x = float(el.get('x', '0')); y = float(el.get('y', '0'))
                w = float(el.get('width', '0')); h = float(el.get('height', '0'))
            except ValueError:
                continue
            if el.get('fill', '') == 'none':
                continue
            rects.append((i, x, y, w, h))
    return texts, rects

def main():
    d = sys.argv[1]
    total_same = 0
    for f in sorted(glob.glob(os.path.join(d, '*.svg'))):
        texts, rects = parse_texts(f)
        # same-baseline: group by y (exact float), pairs with ink gap < 2
        by_y = {}
        for rec in texts:
            by_y.setdefault(rec[3], []).append(rec)
        flags = []
        for y, group in by_y.items():
            group = sorted(group, key=lambda r: r[1])
            for a, b in zip(group, group[1:]):
                gap = b[1] - a[2]
                if gap < 2:
                    flags.append((y, a[4][:40], b[4][:40], round(gap, 2)))
        print(f"{os.path.basename(f)}: {len(texts)} texts, same-baseline flags: {len(flags)}")
        for fl in flags:
            print("  FLAG", fl)
        total_same += len(flags)
        # chart-label, proper 2D check: ink box (x-interval + conservative
        # vertical span baseline-size..baseline+0.3*size) vs each bar rect,
        # regardless of draw order (any overlap reported).
        if 'p6-' in os.path.basename(f):
            bars = [r for r in rects if 1200 <= r[2] <= 1500 and r[3] > 100]
            print(f"  P6 bar rects (y 1200-1500, w>100): {bars}")
            hits = []
            for (ti, x0, x1, y, s, size) in texts:
                top, bot = y - size, y + 0.3 * size
                for (ri, rx, ry, rw, rh) in bars:
                    if x0 < rx + rw and x1 > rx and top < ry + rh and bot > ry:
                        hits.append((round(y, 1), s[:50], round(x0, 1), round(x1, 1), (rx, ry, rw, rh)))
            print(f"  P6 text-ink vs bar-rect 2D overlaps: {len(hits)}")
            for h in hits:
                print("   OVERLAP", h)
            # value-label positions for the record
            for (ti, x0, x1, y, s, size) in texts:
                if '元' in s and 1200 <= y <= 1500:
                    print(f"   value label y={y} x0={round(x0,1)} x1={round(x1,1)} text={s!r}")
    print(f"TOTAL same-baseline flags: {total_same}")

if __name__ == '__main__':
    main()
