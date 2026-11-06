# Supplementary scans reusing the canonical tool's ink_box measurement.
# 1) same-baseline text-ink collisions, all pages
# 2) chart-page graze: text ink vs LATER-drawn opaque rects (P4, P6)
# 3) P7 teaser/footer clearance + letters-box geometry
import sys, os, re
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import xml.etree.ElementTree as ET
import occlusion_audit as OA

D = '/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-it/svg/'

def parse(fn):
    tree = ET.parse(os.path.join(D, fn))
    els = []
    for el in tree.iter():
        tag = el.tag.split('}')[-1]
        if tag == 'text':
            tx = ''.join(el.itertext())
            if not tx.strip():
                continue
            els.append(('text', el, tx))
        elif tag == 'rect':
            els.append(('rect', el, None))
        elif tag == 'line':
            els.append(('line', el, None))
    return els

def ink(el, tx):
    x = float(el.get('x')); y = float(el.get('y'))
    size = float(el.get('font-size') or 20)
    fam = el.get('font-family') or ''
    bold = (el.get('font-weight') or '') in ('700', 'bold')
    anchor = el.get('text-anchor') or 'start'
    return OA.ink_box(tx, fam, size, bold, x, y, anchor)

def overlap(a, b):
    x0 = max(a[0], b[0]); y0 = max(a[1], b[1])
    x1 = min(a[2], b[2]); y1 = min(a[3], b[3])
    return max(0.0, x1 - x0), max(0.0, y1 - y0)

print('=== 1) same-baseline ink collisions ===')
tot = 0
for fn in sorted(os.listdir(D)):
    if not fn.endswith('.svg'):
        continue
    els = parse(fn)
    by_y = {}
    for kind, el, tx in els:
        if kind != 'text':
            continue
        y = float(el.get('y'))
        by_y.setdefault(y, []).append((el, tx))
    for y, nodes in by_y.items():
        if len(nodes) < 2:
            continue
        boxes = [(ink(el, tx), tx) for el, tx in nodes]
        boxes.sort(key=lambda b: b[0][0])
        for i in range(len(boxes)):
            for j in range(i + 1, len(boxes)):
                ox, oy = overlap(boxes[i][0], boxes[j][0])
                if ox > 1.0 and oy > 1.0:
                    tot += 1
                    print(fn, 'y=', y, 'overlap %.1f x %.1f' % (ox, oy),
                          repr(boxes[i][1][:60]), '||', repr(boxes[j][1][:60]))
print('same-baseline collisions:', tot)

print()
print('=== 2) chart-page graze (P4, P6): text ink vs later opaque rect ===')
for fn in ('p4-sport.svg', 'p6-deep.svg'):
    els = parse(fn)
    grazes = 0
    for idx, (kind, el, tx) in enumerate(els):
        if kind != 'text':
            continue
        box = ink(el, tx)
        for kind2, el2, _ in els[idx + 1:]:
            if kind2 != 'rect':
                continue
            fill = (el2.get('fill') or 'none').lower()
            if fill in ('none', 'transparent'):
                continue
            rx, ry = float(el2.get('x') or 0), float(el2.get('y') or 0)
            rw, rh = float(el2.get('width') or 0), float(el2.get('height') or 0)
            ox, oy = overlap(box, (rx, ry, rx + rw, ry + rh))
            if ox > 0 and oy > 0:
                grazes += 1
                print(fn, 'text', repr(tx[:70]), 'ink', [round(v, 1) for v in box],
                      'rect', (rx, ry, rw, rh), 'overlap %.1f x %.1f' % (ox, oy))
    print(fn, 'grazes:', grazes)

print()
print('=== 3) P7 teaser clearance + letters box ===')
els = parse('p7-lang.svg')
for kind, el, tx in els:
    if kind == 'text' and el.get('y') and float(el.get('y')) >= 2460:
        box = ink(el, tx)
        print('teaser node y=', el.get('y'), 'ink-bottom=%.2f' % box[3], repr(tx[:100]))
print('footer rule y=2580; clearance = 2580 - max teaser ink bottom')
print('--- P7 bordered rects (stroke set) ---')
for kind, el, tx in els:
    if kind == 'rect' and el.get('stroke'):
        print('rect x=', el.get('x'), 'y=', el.get('y'), 'w=', el.get('width'), 'h=', el.get('height'))
print('--- P7 texts y 1200-1780 (letters box region) ---')
for kind, el, tx in els:
    if kind == 'text' and el.get('y') and 1200 <= float(el.get('y')) <= 1780:
        box = ink(el, tx)
        print(' y=', el.get('y'), 'ink-bottom=%.2f' % box[3], repr(tx[:90]))
