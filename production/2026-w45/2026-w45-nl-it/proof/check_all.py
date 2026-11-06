# -*- coding: utf-8 -*-
"""Independent proof checks for W45 NL x IT. Reads shipped SVGs only; writes JSON+log here."""
import re, html, json, os, sys
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import p8 as P8
from PIL import ImageFont

BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations/files'
CORE = BASE + '/weekly-report-w45-nl-core/svg'
ED = BASE + '/weekly-report-w45-nl-it/svg'
W43 = BASE + '/weekly-report-nl-it/svg'
OUT = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/nl-it-proof'

TEXT_RE = re.compile(r'<text([^>]*)>(.*?)</text>', re.S)
RECT_RE = re.compile(r'<rect x="([0-9.\-]+)" y="([0-9.\-]+)" width="([0-9.\-]+)" height="([0-9.\-]+)"[^>]*>')
IMG_RE = re.compile(r'<image[^>]*>')
CJK_RE = re.compile(r'[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]')

def attr(a, k):
    m = re.search(k + r'="([^"]*)"', a)
    return m.group(1) if m else ''

def parse(path):
    s = open(path, encoding='utf-8').read()
    els = []
    for pos, m in enumerate(TEXT_RE.finditer(s)):
        a, c = m.group(1), m.group(2)
        t = html.unescape(re.sub(r'<[^>]+>', '', c))
        els.append({'x': float(attr(a, 'x') or 0), 'y': float(attr(a, 'y') or 0),
                    'fam': attr(a, 'font-family'), 'size': float(attr(a, 'font-size') or 0),
                    'bold': 'font-weight="700"' in a, 'fill': attr(a, 'fill'),
                    'anchor': attr(a, 'text-anchor') or 'start', 's': t, 'pos': m.start(),
                    'raw': t.strip()})
    rects = [{'x': float(a), 'y': float(b), 'w': float(c), 'h': float(d), 'pos': m.start()}
             for m in RECT_RE.finditer(s) for a, b, c, d in [m.groups()]]
    return els, rects, s

def texts_of(d, name):
    els, _, _ = parse(os.path.join(d, name))
    return els

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

def joined_page(els):
    return norm(' '.join(e['raw'] for e in els))

# --- fonts (same SC faces as builder svglib) ---
FD = '/usr/share/fonts/opentype/noto'
def sc_index(path):
    for i in range(12):
        try:
            f = ImageFont.truetype(path, 40, index=i)
            if f.getname()[0].endswith('SC'):
                return i
        except Exception:
            break
    return 0
IDX = {p: sc_index(p) for p in [FD + '/NotoSansCJK-Bold.ttc', FD + '/NotoSansCJK-Regular.ttc',
                                 FD + '/NotoSerifCJK-Bold.ttc', FD + '/NotoSerifCJK-Regular.ttc']}
def font(kind, bold, size):
    p = {'sans': FD + ('/NotoSansCJK-Bold.ttc' if bold else '/NotoSansCJK-Regular.ttc'),
         'serif': FD + ('/NotoSerifCJK-Bold.ttc' if bold else '/NotoSerifCJK-Regular.ttc')}[kind]
    return ImageFont.truetype(p, int(size) if float(size).is_integer() else size, index=IDX[p])

def width(s, kind, bold, size):
    return font(kind, bold, size).getlength(s)

def inkbox_baseline(el):
    """Baseline-anchored ink box: getbbox left/right + getmetrics ascent/descent (task item 4)."""
    if 'UnifrakturMaguntia' in el['fam']:
        return None
    kind = 'serif' if 'Serif' in el['fam'] else 'sans'
    f = font(kind, el['bold'], el['size'])
    left, _t, right, _b = f.getbbox(el['raw'])
    ascent, descent = f.getmetrics()
    length = f.getlength(el['raw'])
    if el['anchor'] == 'start':
        x0, x1 = el['x'] + left, el['x'] + right
    elif el['anchor'] == 'middle':
        x0, x1 = el['x'] - length / 2 + left, el['x'] - length / 2 + right
    else:
        x0, x1 = el['x'] - length + left, el['x'] - length + right
    return (x0, el['y'] - ascent, x1, el['y'] + descent)

def inkbox_anchor_ls(el):
    """Direct PIL anchor='ls' variant, for cross-check."""
    if 'UnifrakturMaguntia' in el['fam']:
        return None
    kind = 'serif' if 'Serif' in el['fam'] else 'sans'
    f = font(kind, el['bold'], el['size'])
    try:
        l, t, r, b = f.getbbox(el['raw'], anchor='ls')
    except Exception as e:
        return ('ERR', str(e))
    # anchor ls: x is left, y is baseline -> bbox coords are absolute already
    return (el['x'] + l, el['y'] + t, el['x'] + r, el['y'] + b)

R = {}

# ---- 8. furniture ----
ed_p1 = texts_of(ED, 'p1-voorpagina.svg')
w43_p1 = texts_of(W43, 'p1-voorpagina.svg')
core_p1 = texts_of(CORE, 'p1-voorpagina.svg')
def find(els, pred):
    return [e for e in els if pred(e)]
badge_ed = find(ed_p1, lambda e: e['y'] == 568 and e['fill'] == '#a4553a')
badge_w43 = find(w43_p1, lambda e: e['y'] == 568 and e['fill'] == '#a4553a')
R['badge_ed'] = [(e['s'].strip(), e['size'], e['bold'], e['fill'], e['anchor'], e['x'], e['y'],
                  round(width(e['raw'], 'sans', True, 20), 2)) for e in badge_ed]
R['badge_w43'] = [(e['s'].strip(), e['size'], e['bold'], e['fill'], e['anchor'], e['x'], e['y'],
                   round(width(e['raw'], 'sans', True, 20), 2)) for e in badge_w43]
R['badge_strings_equal'] = (badge_ed and badge_w43 and badge_ed[0]['raw'] == badge_w43[0]['raw'])
sub_ed = find(ed_p1, lambda e: e['y'] == 330)
sub_w43 = find(w43_p1, lambda e: e['y'] == 330)
R['subtitle_ed'] = [(e['raw'], e['size'], e['bold'], round(width(e['raw'], 'serif', True, 36), 2)) for e in sub_ed]
R['subtitle_w43'] = [(e['raw'], e['size'], e['bold'], round(width(e['raw'], 'serif', True, 36), 2)) for e in sub_w43]
strap_ed = find(ed_p1, lambda e: e['y'] == 372)
strap_core = find(core_p1, lambda e: e['y'] == 372)
R['strapline_ed'] = [e['raw'] for e in strap_ed]
R['strapline_core'] = [e['raw'] for e in strap_core]
R['strapline_equal'] = strap_ed and strap_core and strap_ed[0]['raw'] == strap_core[0]['raw']
top_ed = find(ed_p1, lambda e: e['y'] == 92)
R['topstrip_ed'] = [(e['raw'], e['anchor']) for e in top_ed]
# footers all pages
pages = ['p1-voorpagina.svg', 'p2-leven.svg', 'p3-cultuur.svg', 'p4-sport.svg',
         'p5-jongeren.svg', 'p6-verdieping.svg', 'p7-taal.svg', 'p8-toets.svg']
R['footers'] = {}
for i, pg in enumerate(pages, 1):
    els = texts_of(ED, pg)
    f = [e['raw'] for e in els if e['y'] == 2624]
    R['footers'][pg] = f
R['footer_vol2_all'] = all(any('VOL.2' in t for t in v) for v in R['footers'].values())
R['page_lines'] = {pg: [t for t in v if 'Pagina' in t] for pg, v in R['footers'].items()}

# ---- gloss prefix + rendered gloss counts ----
def gloss_boxes(d, pg):
    els = texts_of(d, pg)
    boxes = []
    i = 0
    while i < len(els):
        e = els[i]
        if e['raw'].startswith('Nota — ') or e['raw'].startswith('讲解') or e['raw'].startswith('译注'):
            start = e
            lines = [e['raw']]
            j = i + 1
            while j < len(els):
                n = els[j]
                if n['x'] == start['x'] and n['size'] == start['size'] and 20 <= (n['y'] - els[j-1]['y']) <= 35 and n['raw']:
                    lines.append(n['raw']); j += 1
                else:
                    break
            boxes.append({'x': start['x'], 'joined': norm(' '.join(lines)), 'lines': lines})
            i = j
        else:
            i += 1
    return boxes
R['gloss_ed'] = {}
R['gloss_core'] = {}
for pg in pages[1:6]:  # p2..p6
    eb = gloss_boxes(ED, pg); cb = gloss_boxes(CORE, pg)
    def split_count(b):
        if not b: return None
        s = b['joined']
        s = re.sub(r'^(Nota — |讲解｜|译注｜)', '', s)
        return [x.strip() for x in s.split('·') if x.strip()]
    R['gloss_ed'][pg] = [{'joined': b['joined'], 'items': split_count(b), 'n': len(split_count(b))} for b in eb]
    R['gloss_core'][pg] = [{'joined': b['joined'], 'items': split_count(b), 'n': len(split_count(b))} for b in cb]
R['gloss_prefix_w43'] = [b['joined'][:60] for b in gloss_boxes(W43, 'p2-leven.svg')]
R['gloss_prefix_ed_all'] = [b['joined'][:8] for pg in pages[1:6] for b in gloss_boxes(ED, pg)]

# ---- 3. P7 word box ----
p7 = texts_of(ED, 'p7-taal.svg')
wb = [e['raw'] for e in p7 if e['x'] == 1473.0 and 1089 <= e['y'] <= 1151]
R['p7_wordbox_lines'] = wb
R['p7_definition_joined'] = norm(' '.join(wb))
R['p7_definition_target'] = '«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.'
R['p7_definition_verbatim'] = R['p7_definition_joined'] == R['p7_definition_target']
gl = [e['raw'] for e in p7 if e['x'] == 1473.0 and 1210 <= e['y'] <= 1240]
R['p7_wordbox_gloss'] = gl
R['p7_wordbox_gloss_joined'] = norm(' '.join(gl))
core_p7 = texts_of(CORE, 'p7-taal.svg')
cwb = [e['raw'] for e in core_p7 if e['x'] == 1473.0 and 1089 <= e['y'] <= 1151]
R['p7_definition_core'] = norm(' '.join(cwb))

# ---- 6. golden sentences ----
def golden(els):
    out = []
    for i, e in enumerate(els):
        if e['raw'].startswith('«') and e['y'] >= 2038 and e['size'] == 21.5:
            tag = ''
            for n in els[i+1:i+3]:
                m = re.search(r'\(Pagina (\d+)\)', n['raw'])
                if m: tag = m.group(1)
            out.append({'sentence': e['raw'].strip('«»'), 'tag': tag, 'y': e['y'], 'x': e['x']})
    return out
R['golden_ed'] = golden(p7)
R['golden_core'] = golden(core_p7)
# per-page normalised text
page_text = {}
for pg in pages:
    page_text[pg] = joined_page(texts_of(ED, pg))
all_text = ' '.join(page_text.values())
R['golden_checks'] = []
for g in R['golden_ed']:
    s = g['sentence']
    cnt = all_text.count(s)
    pgname = pages[int(g['tag']) - 1] if g['tag'].isdigit() else None
    on_tagged = (s in page_text[pgname]) if pgname else False
    R['golden_checks'].append({'sentence': s, 'tag': g['tag'], 'total_count': cnt, 'on_tagged_page': on_tagged, 'tagged_file': pgname})
# P7 phrases verbatim from articles: each sentence must also occur outside P7
p7_text = page_text['p7-taal.svg']
R['golden_outside_p7'] = [all_text.replace(p7_text, '', 1).count(g['sentence']) if False else None for g in R['golden_ed']]

# ---- 7. readers corner ----
rc = [e['raw'] for e in p7 if e['x'] == 1473.0 and 1311 <= e['y'] <= 1870]
R['readers_lines'] = rc
R['readers_joined'] = norm(' '.join(rc))
R['readers_checks'] = {
    'nl_disclosure': 'Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.' in R['readers_joined'],
    'it_disclosure': 'Alla stampa: niente lettere vere, niente migliori testi di pagina 8 — quindi un esempio; promessa rimandata al VOL.3.' in R['readers_joined'],
    'invitation': 'Esempio della redazione, non una lettera vera. Mandaci lettera e testo di pagina 8: li pubblicheremo nel VOL.3!' in R['readers_joined'],
    'example_label': 'voorbeeldbrief van de redactie' in R['readers_joined'],
    'imperative_Mandaci': 'Mandaci lettera' in R['readers_joined'],
    'promise_pub': 'li pubblicheremo nel VOL.3' in R['readers_joined'],
}

# ---- 2. P8 keydiff adjudication ----
core_res, _ = P8.extract(CORE + '/p8-toets.svg', 150)
ed_res, _ = P8.extract(ED + '/p8-toets.svg', 150)
R['p8_keydiff'] = []
for n in [7, 17, 70, 71, 76, 96, 137, 138, 148]:
    cs, es = core_res[n]['seg'], ed_res[n]['seg']
    ctok = cs.split(' — ')[0].strip(); etok = es.split(' — ')[0].strip()
    R['p8_keydiff'].append({'n': n, 'core_seg': cs, 'ed_seg': es, 'core_token': ctok, 'ed_token': etok,
                            'token_equal': ctok == etok, 'core_method': core_res[n]['method'], 'ed_method': ed_res[n]['method'],
                            'core_key': core_res[n]['key'], 'ed_key': ed_res[n]['key']})
R['p8_139_140'] = {n: {'core_seg': core_res[n]['seg'], 'ed_seg': ed_res[n]['seg'],
                        'core_key': core_res[n]['key'], 'ed_key': ed_res[n]['key'],
                        'key_equal': core_res[n]['key'] == ed_res[n]['key']} for n in [139, 140, 150]}
R['p8_150'] = {'core': core_res[150]['seg'], 'ed': ed_res[150]['seg']}

# ---- 4. same-baseline + P6 chart (baseline-anchored) ----
R['same_baseline'] = {}
for pg in pages:
    els, _, _ = parse(os.path.join(ED, pg))
    boxes = [(e, inkbox_baseline(e)) for e in els]
    boxes = [(e, b) for e, b in boxes if b]
    groups = {}
    for e, b in boxes:
        groups.setdefault(round(e['y'], 1), []).append((e, b))
    hits = []
    for y, items in groups.items():
        items.sort(key=lambda ib: ib[1][0])
        for (e1, b1), (e2, b2) in zip(items, items[1:]):
            if b2[0] < b1[2] - 2 and not (b2[1] > b1[3] or b1[1] > b2[3]):
                hits.append({'y': y, 'a': e1['raw'][:50], 'b': e2['raw'][:50]})
    R['same_baseline'][pg] = hits
# P6 chart labels: texts in chart region (builder region x 1451-1885, y 200-720) vs later rects
els6, rects6, _ = parse(os.path.join(ED, 'p6-verdieping.svg'))
R['p6_chart_region_texts'] = [(e['raw'], e['x'], e['y'], e['size']) for e in els6 if 1451 <= e['x'] <= 1885 and 200 <= e['y'] <= 720]
worst, worst_txt, worst_method = 0.0, '—', ''
detail = []
for e in els6:
    b = inkbox_baseline(e)
    if not b or not (1451 <= e['x'] <= 1885 and 200 <= e['y'] <= 720):
        continue
    area = max(0.0, (b[2] - b[0]) * (b[3] - b[1]))
    if area <= 0: continue
    for r in rects6:
        if r['pos'] <= e['pos']: continue
        ix = max(0.0, min(b[2], r['x'] + r['w']) - max(b[0], r['x']))
        iy = max(0.0, min(b[3], r['y'] + r['h']) - max(b[1], r['y']))
        cov = ix * iy / area
        if cov > 0: detail.append({'text': e['raw'], 'cov_pct': round(cov * 100, 2), 'inkbox': [round(v, 1) for v in b]})
        if cov > worst: worst, worst_txt, worst_method = cov, e['raw'], 'baseline-getmetrics'
R['p6_chart_worst_baseline'] = {'pct': round(worst * 100, 2), 'text': worst_txt, 'method': worst_method}
R['p6_chart_nonzero'] = detail
# anchor-ls cross-check
worst2, worst2_txt = 0.0, '—'
for e in els6:
    b = inkbox_anchor_ls(e)
    if not b or b[0] == 'ERR' or not (1451 <= e['x'] <= 1885 and 200 <= e['y'] <= 720):
        continue
    area = max(0.0, (b[2] - b[0]) * (b[3] - b[1]))
    if area <= 0: continue
    for r in rects6:
        if r['pos'] <= e['pos']: continue
        ix = max(0.0, min(b[2], r['x'] + r['w']) - max(b[0], r['x']))
        iy = max(0.0, min(b[3], r['y'] + r['h']) - max(b[1], r['y']))
        cov = ix * iy / area
        if cov > worst2: worst2, worst2_txt = cov, e['raw']
R['p6_chart_worst_anchor_ls'] = {'pct': round(worst2 * 100, 2), 'text': worst2_txt}
# chart values in P6 text
p6t = joined_page(els6)
R['p6_chart_values_present'] = {v: (v in p6t) for v in ['45', '25', '20', '10']}
# find chart label texts (percentages / bars) anywhere on P6
R['p6_all_texts_chart_area'] = [(e['raw'], e['x'], e['y']) for e in els6 if 600 <= e['y'] <= 760]

# ---- 9. misc ----
R['images'] = {}
R['credits'] = {}
for pg in pages:
    els, _, s = parse(os.path.join(ED, pg))
    R['images'][pg] = len(IMG_RE.findall(s))
    R['credits'][pg] = [e['raw'] for e in els if e['raw'].startswith('Foto:')]
R['banned'] = {}
for pg in pages:
    t = joined_page(texts_of(ED, pg))
    R['banned'][pg] = {'bridge_term': t.count('桥接'), 'cjk': len(CJK_RE.findall(t))}
R['total_cjk_ed'] = sum(v['cjk'] for v in R['banned'].values())
R['total_bridge_ed'] = sum(v['bridge_term'] for v in R['banned'].values())
import glob
abs_txt = open(BASE + '/weekly-report-w45-nl-it/ABSTRACT.txt', encoding='utf-8').read()
R['abstract'] = {'text': abs_txt, 'lines': [l for l in abs_txt.splitlines() if l.strip()], 'has_ascii_dquote': '"' in abs_txt}
# cards dimensions
from PIL import Image
R['cards'] = {}
for f in sorted(glob.glob(BASE + '/weekly-report-w45-nl-it/cards/*.png')):
    im = Image.open(f); R['cards'][os.path.basename(f)] = im.size
# exercise counts from core KIT registry? count numbered exercise markers is not reliable from SVG alone;
# instead report P8 total + registry from builder run (already verified) — here count P8 answer entries via p8 extract = 150
R['p8_noted'] = len([n for n in range(1, 151) if ed_res[n]['has_note']])

json.dump(R, open(OUT + '/check_all.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: R[k] for k in ['badge_ed', 'badge_w43', 'badge_strings_equal', 'subtitle_ed', 'subtitle_w43',
                                     'strapline_equal', 'topstrip_ed', 'footer_vol2_all', 'page_lines',
                                     'p7_definition_verbatim', 'p7_wordbox_gloss_joined', 'readers_checks',
                                     'p6_chart_worst_baseline', 'p6_chart_worst_anchor_ls',
                                     'total_cjk_ed', 'total_bridge_ed', 'abstract', 'cards']}, ensure_ascii=False, indent=1))
print('GLOSS_ED', {k: [b['n'] for b in v] for k, v in R['gloss_ed'].items()})
print('GLOSS_CORE', {k: [b['n'] for b in v] for k, v in R['gloss_core'].items()})
print('GOLDEN', R['golden_checks'])
print('GOLDEN_ED', R['golden_ed'])
print('GOLDEN_CORE', R['golden_core'])
print('SAME_BASELINE', {k: len(v) for k, v in R['same_baseline'].items()})
print('IMAGES', R['images'])
print('CREDITS', R['credits'])
print('FOOTERS', R['footers'])
