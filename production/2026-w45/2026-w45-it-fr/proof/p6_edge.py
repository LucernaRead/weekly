import glob, re
import xml.etree.ElementTree as ET
from PIL import ImageFont
G = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
FD = '/usr/share/fonts/opentype/noto/'
FACES = {('serif', False): 'NotoSerifCJK-Regular.ttc', ('serif', True): 'NotoSerifCJK-Bold.ttc',
         ('sans', False): 'NotoSansCJK-Regular.ttc', ('sans', True): 'NotoSansCJK-Bold.ttc'}
def font_of(el):
    fam = el.get('font-family', '')
    kind = 'serif' if 'Serif' in fam else 'sans'
    bold = el.get('font-weight') in ('700', 'bold')
    size = float(el.get('font-size', 20))
    return ImageFont.truetype(FD + FACES[(kind, bold)], int(round(size)), index=2), size
def items_of(path):
    root = ET.parse(path).getroot(); items = []
    for el in root.iter():
        tag = el.tag.split('}')[-1]
        if tag == 'text' and (el.text or '').strip():
            f, size = font_of(el); t = el.text; adv = f.getlength(t)
            anchor = el.get('text-anchor', 'start'); x = float(el.get('x', 0)); y = float(el.get('y', 0))
            x0 = x - adv if anchor == 'end' else x - adv/2 if anchor == 'middle' else x
            asc, desc = f.getmetrics()
            l, tp, r, b = f.getbbox(t, anchor='ls')
            items.append({'kind': 'text', 'text': t, 'x0': x0, 'y': y,
                          'gm_box': (x0, y - asc, x0 + adv, y + desc),
                          'gb_box': (x0 + l, y + tp, x0 + r, y + b)})
        elif tag == 'rect':
            try: items.append({'kind': 'rect', 'x': float(el.get('x', 0)), 'y': float(el.get('y', 0)),
                               'w': float(el.get('width', 0)), 'h': float(el.get('height', 0)),
                               'fill': el.get('fill', '')})
            except ValueError: pass
    return items
def ov(a0, a1, b0, b1): return max(0.0, min(a1, b1) - max(a0, b0))
def cov(box, rect):
    ox = ov(box[0], box[2], rect['x'], rect['x'] + rect['w'])
    oy = ov(box[1], box[3], rect['y'], rect['y'] + rect['h'])
    area = max(0.0, (box[2]-box[0]) * (box[3]-box[1]))
    return ox*oy/area if area else 0.0
# --- P6 coverage, both methods ---
items = items_of(G + '/files/weekly-report-w45-it-fr/svg/p6-approfondimento.svg')
print("P6 nodes with degree sign or city names:")
for it in items:
    if it['kind'] == 'text' and ('°' in it['text'] or any(c in it['text'] for c in ['Torino', 'Milano', 'Bologna', 'Roma', 'Napoli'])):
        print('  ', round(it['y'], 1), repr(it['text']), 'gm_box=', [round(v,1) for v in it['gm_box']], 'gb_box=', [round(v,1) for v in it['gb_box']])
print("\nP6 ALL-text max coverage, getmetrics method:")
worst_gm, worst_gb = [], []
for i, it in enumerate(items):
    if it['kind'] != 'text': continue
    for later in items[i+1:]:
        if later['kind'] != 'rect' or later['fill'] in ('none', ''): continue
        c1 = cov(it['gm_box'], later); c2 = cov(it['gb_box'], later)
        if c1 > 0: worst_gm.append((round(c1*100, 2), it['text'][:50]))
        if c2 > 0: worst_gb.append((round(c2*100, 2), it['text'][:50]))
worst_gm.sort(reverse=True); worst_gb.sort(reverse=True)
print('  getmetrics max =', worst_gm[0] if worst_gm else 0, ' n>0:', len(worst_gm))
for w in worst_gm[:10]: print('   ', w)
print('  getbbox    max =', worst_gb[0] if worst_gb else 0, ' n>0:', len(worst_gb))
for w in worst_gb[:10]: print('   ', w)
print("\nP6 chart-label-only max coverage:")
labels = [it for it in items if it['kind'] == 'text' and ('°' in it['text'] or any(c in it['text'] for c in ['Torino', 'Milano', 'Bologna', 'Roma', 'Napoli']))]
for it in labels:
    i = items.index(it); mg = max([cov(it['gm_box'], l) for l in items[i+1:] if l['kind'] == 'rect' and l['fill'] not in ('none', '')] or [0])
    mb = max([cov(it['gb_box'], l) for l in items[i+1:] if l['kind'] == 'rect' and l['fill'] not in ('none', '')] or [0])
    print(f"  {it['text']!r} getmetrics={mg*100:.2f}% getbbox={mb*100:.2f}%")
# --- right-edge ADVANCE scan, edition + core ---
for lbl, pat in [('ED', G+'/files/weekly-report-w45-it-fr/svg/*.svg'), ('CORE', G+'/files/weekly-report-w45-it-core/svg/*.svg')]:
    print(f"\n{lbl} right-edge ADVANCE flags (>1885):")
    for f in sorted(glob.glob(pat)):
        its = items_of(f)
        for it in its:
            if it['kind'] == 'text':
                # advance right edge: x0 + adv; adv = gm_box width
                right = it['gm_box'][2]
                if right > 1885:
                    print(f"  {f.split('/')[-1]} y={it['y']} right={right:.1f} {it['text'][:60]!r}")
    # same-baseline furniture row check
    print(f"{lbl} same-baseline furniture flags (gap<2, y<600 or y>2550):")
    nflags = 0
    for f in sorted(glob.glob(pat)):
        its = [it for it in items_of(f) if it['kind'] == 'text']
        by_y = {}
        for it in its:
            if it['y'] < 600 or it['y'] > 2550:
                by_y.setdefault(round(it['y'], 1), []).append(it)
        for y, grp in by_y.items():
            grp.sort(key=lambda z: z['x0'])
            for a, b in zip(grp, grp[1:]):
                gap = b['x0'] - a['gm_box'][2]
                if gap < 2:
                    print(f"  {f.split('/')[-1]} y={y} gap={gap:.1f} {a['text'][:30]!r} | {b['text'][:30]!r}"); nflags += 1
    print(f"  total row flags: {nflags}")
