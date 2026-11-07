import re, glob, sys
from PIL import ImageFont

SERIF = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc'
SERIFB = '/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc'
SANS = '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc'
SANSB = '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc'

def font_for(fam, size, weight):
    bold = weight and '700' in weight
    if 'Serif' in fam:
        path = SERIFB if bold else SERIF
    else:
        path = SANSB if bold else SANS
    # SC face index 2 for rendered SVG font-family "CJK SC"
    return ImageFont.truetype(path, int(round(size * 4)), index=2)

def scan(d):
    print(f"##### {d} #####")
    total_bad = 0
    for path in sorted(glob.glob(d + '*.svg')):
        s = open(path, encoding='utf-8').read()
        rows = []
        for m in re.finditer(r'<text[^>]*>', s):
            tag = m.group(0)
            xm = re.search(r'x="([\d.]+)"', tag); ym = re.search(r'y="([\d.]+)"', tag)
            fm = re.search(r'font-size="([\d.]+)"', tag)
            fam = re.search(r'font-family="([^"]+)"', tag)
            wm = re.search(r'font-weight="([^"]+)"', tag)
            anch = re.search(r'text-anchor="([^"]+)"', tag)
            end = s.find('</text>', m.end())
            if end < 0 or not xm or not ym or not fm:
                continue
            t = re.sub(r'<[^>]+>', '', s[m.end():end])
            if not t.strip():
                continue
            x, y, fs = float(xm.group(1)), float(ym.group(1)), float(fm.group(1))
            f = font_for(fam.group(1) if fam else '', fs, wm.group(1) if wm else '')
            bb = f.getbbox(t)
            # ink box in page coords (4x supersample -> /4); anchor handling
            w = (bb[2] - bb[0]) / 4
            a = anch.group(1) if anch else 'start'
            if a == 'middle':
                left, right = x - w / 2, x + w / 2
            elif a == 'end':
                left, right = x - w, x
            else:
                left, right = x + bb[0] / 4, x + bb[2] / 4
            rows.append((y, left, right, t))
        # group by exact y
        by_y = {}
        for y, l, r, t in rows:
            by_y.setdefault(y, []).append((l, r, t))
        bad = []
        for y, items in by_y.items():
            items.sort()
            for (l1, r1, t1), (l2, r2, t2) in zip(items, items[1:]):
                gap = l2 - r1
                if gap < 2:
                    bad.append((y, gap, t1, t2))
        print(f"  {path.split('/')[-1]}: same-baseline pairs<2px: {len(bad)}")
        for b in bad:
            print(f"    y={b[0]} gap={b[1]:.2f} {b[2]!r} | {b[3]!r}")
        total_bad += len(bad)
    print(f"  TOTAL bad={total_bad}")

scan('files/weekly-report-w45-de-ko/svg/')
scan('files/weekly-report-w45-de-core/svg/')
