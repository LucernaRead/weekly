# -*- coding: utf-8 -*-
"""JA x NL supplementary audits (round 3 artifacts). Writes audit-suppl.txt."""
import base64
import hashlib
import re
import sys

sys.path.insert(0, '.')
from svglib import wrap  # noqa: F401  (ensures font config loads)
from PIL import ImageFont
import os

ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-nl")
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-core")
BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ja-nl-build")
OUT = []
def log(s=""):
    OUT.append(s)
    print(s)

# ---- font helpers (same faces as svglib) ----
import svglib as SV
def font(family, bold, size):
    return SV.font_for(family, bold, size) if hasattr(SV, 'font_for') else None

# svglib exposes its font loader; fall back to direct paths from tables
def load_font(family, bold, size):
    try:
        return SV.get_font(family, bold, size)
    except Exception:
        pass
    # inspect svglib source for the font table
    import glob
    cands = glob.glob('/usr/share/fonts/**/NotoSansCJK-Regular.ttc', recursive=True) + \
            glob.glob('/usr/share/fonts/**/NotoSerifCJK-Regular.ttc', recursive=True)
    return None

# Instead of guessing svglib internals, parse its module for a text-width
# helper (bslib4 uses text_w). bslib4.text_w exists.
sys.path.insert(0, BUILD)
import bslib4
text_w = bslib4.text_w
log("text_w probe: " + str(text_w("Pagina 8 van 8", "sans", False, 20)))

def parse_svg(path):
    s = open(path, encoding='utf-8').read()
    texts = []
    for m in re.finditer(r'<text\s+([^>]*)>([^<]*)</text>', s):
        attrs, t = m.group(1), m.group(2)
        def a(name, default=None):
            mm = re.search(name + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else default
        texts.append({
            'x': float(a('x', 0)), 'y': float(a('y', 0)),
            'size': float(a('font-size', 20)),
            'family': a('font-family', ''),
            'weight': a('font-weight', ''),
            'anchor': a('text-anchor', 'start'),
            'text': t,
        })
    rects = []
    for m in re.finditer(r'<rect\s+([^>]*)/?>', s):
        attrs = m.group(1)
        def a(name, default=None):
            mm = re.search(name + r'="([^"]*)"', attrs)
            return mm.group(1) if mm else default
        try:
            rects.append({'x': float(a('x', 0)), 'y': float(a('y', 0)),
                          'w': float(a('width', 0)), 'h': float(a('height', 0)),
                          'sw': float(a('stroke-width', 0) or 0),
                          'fill': a('fill', '')})
        except (TypeError, ValueError):
            pass
    imgs = re.findall(r'xlink:href="data:image/[^;]+;base64,([^"]+)"', s)
    return s, texts, rects, imgs

import glob
ed_pages = sorted(glob.glob(ED + '/svg/*.svg'))
co_pages = sorted(glob.glob(CORE + '/svg/*.svg'))
assert len(ed_pages) == 8 and len(co_pages) == 8

# 1. Right-edge ADVANCE scan (limit 1885.5, ja-en method)
log("\n== RIGHT-EDGE ADVANCE SCAN (limit 1885.5) ==")
viol = 0
for p in ed_pages:
    _, texts, _, _ = parse_svg(p)
    for t in texts:
        fam = 'sans' if 'Sans' in t['family'] else 'serif'
        if 'Unifraktur' in t['family']:
            continue
        bold = t['weight'] in ('700', 'bold')
        try:
            adv = text_w(t['text'], fam, bold, t['size'])
        except Exception:
            continue
        if t['anchor'] == 'start':
            right = t['x'] + adv
        elif t['anchor'] == 'middle':
            right = t['x'] + adv / 2
        else:
            right = t['x']
        if right > 1885.5:
            viol += 1
            log(f"  VIOL {os.path.basename(p)} y={t['y']} right={right:.1f} {t['text'][:60]!r}")
log(f"  violations: {viol}")

# 2. Same-baseline P1 top band (y=92)
log("\n== P1 TOP BAND (y=92) ink spacing ==")
_, texts, _, _ = parse_svg(ed_pages[0])
band = [t for t in texts if abs(t['y'] - 92) < 1]
for t in band:
    fam = 'sans' if 'Sans' in t['family'] else 'serif'
    bold = t['weight'] in ('700', 'bold')
    adv = text_w(t['text'], fam, bold, t['size'])
    if t['anchor'] == 'start':
        l, r = t['x'], t['x'] + adv
    elif t['anchor'] == 'middle':
        l, r = t['x'] - adv / 2, t['x'] + adv / 2
    else:
        l, r = t['x'] - adv, t['x']
    log(f"  {l:.0f}–{r:.0f} {t['text'][:70]!r}")

# 3. Kinsoku line-start scan (NO_START set from canonical svglib)
log("\n== KINSOKU LINE-START SCAN ==")
src = open(os.path.join(BUILD, 'svglib.py'), encoding='utf-8').read()
m = re.search(r'NO_START\s*=\s*"([^"]*)"', src)
nostart = set()
if m:
    nostart = set(m.group(1))
log(f"  NO_START set size: {len(nostart)}")
COLXS = {65, 527, 989, 1451}
hits = 0
for p in ed_pages:
    _, texts, _, _ = parse_svg(p)
    for t in texts:
        if not t['text']:
            continue
        # candidate line starts: text anchored start near a column/inset x
        if t['anchor'] == 'start' and any(abs(t['x'] - cx) < 60 for cx in list(COLXS) + [87, 93, 95, 117]):
            if t['text'][0] in nostart:
                hits += 1
                log(f"  HIT {os.path.basename(p)} y={t['y']} {t['text'][:40]!r}")
log(f"  kinsoku hits: {hits}")

# 4. P6 chart-label coverage: PIL true-ink boxes (occlusion module) vs
# LATER-drawn opaque rects; report every text with any such overlap.
log("\n== P6 CHART-LABEL COVERAGE (true ink vs later rects) ==")
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
p6path = [p for p in ed_pages if 'p6-' in p][0]
els6, _, _ = OA.parse_svg(open(p6path, encoding='utf-8').read())
maxcov = 0.0
for i, el in enumerate(els6):
    if el.kind != 'text':
        continue
    ib = el.box
    if ib is None:
        continue
    iarea = max(0.0, (ib[2] - ib[0]) * (ib[3] - ib[1]))
    if iarea <= 0:
        continue
    for later in els6[i + 1:]:
        if later.kind not in ('rect', 'path', 'image'):
            continue
        if not OA.is_opaque(later):
            continue
        lb = OA.shape_box(later)
        if lb is None:
            continue
        ox = max(0.0, min(ib[2], lb[2]) - max(ib[0], lb[0]))
        oy = max(0.0, min(ib[3], lb[3]) - max(ib[1], lb[1]))
        cov = (ox * oy) / iarea
        if cov > 0:
            maxcov = max(maxcov, cov)
            log(f"  cov={cov:.3f} text={el.text[:60]!r} ink={tuple(round(v,1) for v in ib)} rect={tuple(round(v,1) for v in lb)}")
log(f"  MAX chart-page later-rect ink coverage: {maxcov:.3f} (gate <0.30)")

# 4b. Full-page frame scan: every text ink box vs every rect border line.
log("\n== FULL-PAGE FRAME SCAN (ink crossing a rect border) ==")
frame_hits = 0
for p in ed_pages:
    els, _, _ = OA.parse_svg(open(p, encoding='utf-8').read())
    for el in els:
        if el.kind != 'text':
            continue
        ib = el.box
        if ib is None:
            continue
        for r in els:
            if r.kind != 'rect':
                continue
            rb = OA.shape_box(r)
            if rb is None:
                continue
            sw = 0.0
            try:
                sw = float(r.attrs.get('stroke-width', 0) or 0)
            except (TypeError, ValueError):
                sw = 0.0
            tol = sw / 2.0 + 0.5
            x0, y0, x1, y1 = rb
            # skip page-size background rects
            if x0 <= 0 and y0 <= 0 and x1 >= 1950 and y1 >= 2700:
                continue
            crossed = []
            # vertical borders
            for bx in (x0, x1):
                if ib[0] < bx - tol and ib[2] > bx + tol and ib[1] < y1 and ib[3] > y0:
                    crossed.append(f"v-border x={bx:.0f}")
            for by in (y0, y1):
                if ib[1] < by - tol and ib[3] > by + tol and ib[0] < x1 and ib[2] > x0:
                    crossed.append(f"h-border y={by:.0f}")
            if crossed:
                frame_hits += 1
                log(f"  {os.path.basename(p)} {crossed} text={el.text[:60]!r} ink={tuple(round(v,1) for v in ib)} rect={tuple(round(v,1) for v in rb)}")
log(f"  frame-scan hits: {frame_hits}")

# 5. Gloss counts (code-level gloss() strings, split on the separator)
log("\n== GLOSS COUNTS (split on separator) ==")
def gloss_counts(builddir):
    total = {}
    for fn in ('content12.py', 'content34.py', 'content56.py'):
        txt = open(os.path.join(builddir, fn), encoding='utf-8').read()
        # gloss calls: .gloss("...") in bslib4? find gloss( " strings
        calls = re.findall(r'\.gloss\(\s*"([^"]*)"', txt)
        # also box gloss lists: gloss strings appear as ("...") args; count
        # via the rendered prefix instead (see SVG section below)
        total[fn] = calls
    return total
for bdir, label in [(CORE.replace('files/weekly-report-w45-ja-core', 'hidden_files/weekly-report-w45-ja-build'), 'core'),
                    (BUILD, 'edition')]:
    gc = gloss_counts(bdir)
    for fn, calls in gc.items():
        log(f"  {label} {fn}: {len(calls)} gloss calls")
# SVG-level: count Uitleg prefix boxes + per-page gloss item check via code strings
for p in ed_pages:
    _, texts, _, _ = parse_svg(p)
    n = sum(1 for t in texts if t['text'].startswith('Uitleg'))
    log(f"  {os.path.basename(p)}: Uitleg-prefixed text runs: {n}")

# 6. Phrases 2x + tags
log("\n== P7 PHRASES ==")
alltext = ''
for p in ed_pages:
    _, texts, _, _ = parse_svg(p)
    alltext += ''.join(t['text'] for t in texts)
blank = re.sub(r'\s+', '', alltext)
quotes = [
    "「文化の日は、11月3日（火よう日）です。」",
    "「ゆっくり、ゆるく整える日本の11月です。」",
    "「『ゆる』は、無理をしない、ゆっくり、という意味です。」",
    "「鍋の材料が1か月早く並び始めました。」",
    "「伝統工芸と紅葉と光を、いっしょに楽しむことができます。」",
    "「ソフトバンクが2連勝でスタートしました。」",
    "「ルールを守って、楽しいハロウィンにしましょう。」",
    "「紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。」",
]
for q in quotes:
    log(f"  count={blank.count(re.sub(chr(32), '', q))} {q[:30]}")
for tag in ['(Pagina 1)', '(Pagina 2)', '(Pagina 3)', '(Pagina 4)', '(Pagina 5)', '(Pagina 6)']:
    log(f"  tag {tag}: {alltext.count(tag)}")

# 7. Images + credits
log("\n== IMAGES + CREDITS ==")
for ep, cp in zip(ed_pages, co_pages):
    _, _, _, ei = parse_svg(ep)
    _, _, _, ci = parse_svg(cp)
    eh = [hashlib.sha256(base64.b64decode(x)).hexdigest()[:12] for x in ei]
    ch = [hashlib.sha256(base64.b64decode(x)).hexdigest()[:12] for x in ci]
    log(f"  {os.path.basename(ep)}: edition {eh} core {ch} equal={eh == ch}")
# credit lines: small grey texts containing known author markers
for ep, cp in zip(ed_pages, co_pages):
    def credits(p):
        _, texts, _, _ = parse_svg(p)
        return [t['text'] for t in texts if any(k in t['text'] for k in ['Poliphilo', 'Hiroshige', 'Syced', 'Kratochvil', 'CC0', 'Public', 'パブリック', '出典'])]
    log(f"  {os.path.basename(ep)} credits equal={credits(ep) == credits(cp)} ed={credits(ep)}")

# 8. P8 integrity: identical lines core vs edition + E-zone + #37
log("\n== P8 INTEGRITY ==")
def lines(p):
    _, texts, _, _ = parse_svg(p)
    return [t['text'] for t in texts]
co_p8 = [p for p in co_pages if 'p8-' in p][0]
ed_p8 = [p for p in ed_pages if 'p8-' in p][0]
cl, el = lines(co_p8), lines(ed_p8)
cs, es = set(cl), set(el)
ident = sorted(cs & es)
log(f"  core lines {len(cl)}, edition lines {len(el)}, identical distinct lines: {len(ident)}")
for t in ident:
    log(f"    IDENTICAL: {t[:110]!r}")
for n in ('137.', '138.', '139.', '140.', '37.'):
    for t in el:
        if t.startswith(n + ' ') or t.startswith(n):
            log(f"  ED {t[:130]!r}")
            break
for n in ('137.', '138.', '139.', '140.'):
    for t in cl:
        if t.startswith(n + ' '):
            log(f"  CORE {t[:130]!r}")
            break
# directional instrs on P8
for t in el:
    if 'Vertaal naar' in t:
        log(f"  ED instr: {t!r}")

# 9. Word-level CJK residue: edition CJK runs not occurring in core text
log("\n== WORD-LEVEL CJK RESIDUE (edition runs absent from core text) ==")
core_all = ''
for p in co_pages:
    _, texts, _, _ = parse_svg(p)
    core_all += ''.join(t['text'] for t in texts)
core_runs = set(re.findall(r'[\u4e00-\u9fff\u3040-\u30ff]+', core_all))
for p in ed_pages:
    _, texts, _, _ = parse_svg(p)
    for t in texts:
        for run in re.findall(r'[\u4e00-\u9fff\u3040-\u30ff]+', t['text']):
            if len(run) >= 2 and run not in core_all:
                log(f"  {os.path.basename(p)} y={t['y']} run={run!r} ctx={t['text'][:80]!r}")

# 10. Furniture counts
log("\n== FURNITURE COUNTS ==")
p1 = parse_svg(ed_pages[0])[1]
badge = [t for t in p1 if 'TEKSTEN IN HET JAPANS' in t['text']]
log(f"  badge P1: {len(badge)} {badge[0]['text'] if badge else ''} y={badge[0]['y'] if badge else ''} size={badge[0]['size'] if badge else ''}")
foot = 0; pageline = 0; sep = 0; gloss_prefix = 0
for p in ed_pages:
    _, texts, _, _ = parse_svg(p)
    foot += sum(1 for t in texts if t['text'].startswith('Lucerna · JAPANS WEEKBLAD VOL.2'))
    pageline += sum(1 for t in texts if re.match(r'Pagina \d van 8', t['text']))
    sep += sum(1 for t in texts if re.match(r'— Pagina \d —', t['text']))
    gloss_prefix += sum(1 for t in texts if t['text'].startswith('Uitleg —'))
log(f"  footers: {foot}, page lines: {pageline}, P8 separators: {sep}, gloss-prefix runs: {gloss_prefix}")

# 11. Banned intermediary term (written as escapes, never literally)
log("\n== BANNED-TERM SCAN ==")
term = chr(0x6865) + chr(0x63a5)
hits = 0
for p in ed_pages:
    s = open(p, encoding='utf-8').read()
    if term in s:
        hits += 1
        log(f"  HIT in {p}")
for f in ('transform.py', 'gen_nl.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py', 'render.py', 'run.py'):
    s = open(os.path.join(BUILD, f), encoding='utf-8').read()
    if term in s:
        hits += 1
        log(f"  HIT in build {f}")
log(f"  banned-term hits in SVG+build code: {hits} (ABSTRACT/KIT checked separately)")

open(os.path.join(BUILD, 'audit-suppl.txt'), 'w', encoding='utf-8').write('\n'.join(OUT) + '\n')
log("\nWROTE audit-suppl.txt")
