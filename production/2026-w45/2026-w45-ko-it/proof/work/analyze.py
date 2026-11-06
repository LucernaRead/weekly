#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Independent KOxIT proof analysis — reads ONLY shipped SVGs (+ own rerun logs).
Writes JSON + text summaries into work/. Never writes to delivery/core/build trees."""
import base64, hashlib, html, io, json, re, sys
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
from occlusion_audit import ink_box, get_font

BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations'
WORK = BASE + '/hidden_files/w45/ko-it-proof/work'
ED = BASE + '/files/weekly-report-w45-ko-it'
CORE = BASE + '/files/weekly-report-w45-ko-core'
W43 = BASE + '/files/weekly-report-ko-it'
PAGES = ['p1-pyoji', 'p2-saenghwal', 'p3-munhwa', 'p4-seupocheu',
         'p5-cheongnyeon', 'p6-gipi', 'p7-mal', 'p8-siheom']
NS = '{http://www.w3.org/2000/svg}'
HANGUL = re.compile(r'[\uac00-\ud7a3]')
HAN = re.compile(r'[\u4e00-\u9fff\u3400-\u4dbf\uf900-\ufaff]')
LATIN = re.compile(r'[A-Za-z]')

def texts(ed, pg):
    root = ET.parse(f'{ed}/svg/{pg}.svg').getroot()
    out = []
    for el in root.iter(NS + 'text'):
        out.append({'x': float(el.get('x')), 'y': float(el.get('y')),
                    'size': float(el.get('font-size')), 'fam': el.get('font-family'),
                    'fill': el.get('fill'), 'bold': el.get('font-weight') in ('700', 'bold'),
                    'anchor': el.get('text-anchor', 'start'), 't': ''.join(el.itertext())})
    return out

def shapes(ed, pg):
    root = ET.parse(f'{ed}/svg/{pg}.svg').getroot()
    out = []
    for el in root.iter():
        tag = el.tag.replace(NS, '')
        if tag in ('rect', 'line', 'image', 'circle', 'path'):
            out.append({'tag': tag, **{k: el.get(k) for k in
                       ('x', 'y', 'width', 'height', 'x1', 'y1', 'x2', 'y2', 'href')}})
    return out

def adv(t):
    f = get_font(t['fam'], t['size'], t['bold'])
    from occlusion_audit import SCALE
    a = f.getlength(t['t']) / SCALE
    if t['anchor'] == 'middle': return t['x'] - a / 2, t['x'] + a / 2
    if t['anchor'] == 'end': return t['x'] - a, t['x']
    return t['x'], t['x'] + a

R = {}

# ---- 1. Han inventory + banned terms + pure-Korean freeze classification ----
han_inv = {}
banned = {}
for pg in PAGES:
    ts = texts(ED, pg)
    chars = Counter()
    for t in ts:
        for ch in t['t']:
            if HAN.match(ch): chars[ch] += 1
    han_inv[pg] = dict(chars)
    hits = []
    for term in ['桥接', 'bridge', 'Bridge', 'intermediario', 'intermediazione',
                 'intermediary', '中介', '橋接']:
        for t in ts:
            if term in t['t']: hits.append((term, t['t']))
    banned[pg] = hits
R['han_inventory_edition'] = han_inv
R['han_total_edition'] = sum(sum(v.values()) for v in han_inv.values())
R['banned_hits_edition'] = banned
# core Han inventory for contrast
han_core = {}
for pg in PAGES:
    c = Counter()
    for t in texts(CORE, pg):
        for ch in t['t']:
            if HAN.match(ch): c[ch] += 1
    han_core[pg] = dict(c)
R['han_total_core'] = sum(sum(v.values()) for v in han_core.values())

# freeze-diff classification: pure-Hangul added/removed strings
fd = json.load(open(WORK + '/freeze-diff.json'))
pure_add, pure_rem, mixed_add = [], [], []
for pg, d in fd['pages'].items():
    for s in d['added_strings']:
        txt = s['text']
        if HANGUL.search(txt) and not LATIN.search(txt) and not HAN.search(txt):
            pure_add.append((pg, txt))
        elif HANGUL.search(txt):
            mixed_add.append((pg, txt))
    for s in d['removed_strings']:
        txt = s['text']
        if HANGUL.search(txt) and not LATIN.search(txt) and not HAN.search(txt):
            pure_rem.append((pg, txt))
R['freeze_pure_hangul_added'] = pure_add
R['freeze_pure_hangul_removed'] = pure_rem
R['freeze_mixed_hangul_added_count'] = len(mixed_add)
R['freeze_mixed_hangul_added'] = mixed_add

# ---- 2. P8 printed lines ----
def p8_lines(ed):
    out = []
    for t in texts(ed, 'p8-siheom'):
        m = re.match(r'^(\d+)\.\s(.*)$', t['t'])
        if m: out.append((int(m.group(1)), t['x'], t['y'], t['t']))
    return out
ed_p8, co_p8 = p8_lines(ED), p8_lines(CORE)
R['p8_keys_edition'] = {str(n): txt for n, x, y, txt in ed_p8}
for n in (104, 137, 138, 139, 140, 150):
    R[f'p8_{n}_edition'] = [txt for nn, x, y, txt in ed_p8 if nn == n]
    R[f'p8_{n}_core'] = [txt for nn, x, y, txt in co_p8 if nn == n]
R['p8_separators_edition'] = [t['t'] for t in texts(ED, 'p8-siheom') if t['t'].startswith('— ')]
R['p8_separators_core'] = [t['t'] for t in texts(CORE, 'p8-siheom') if t['t'].startswith('— ')]
# P8 notes pure-Italian check: P8 text nodes containing Han
R['p8_han_edition'] = [t['t'] for t in texts(ED, 'p8-siheom') if HAN.search(t['t'])]
# P8 keys region geometry (y>=1341 separators/keys area)
keys = [t for t in texts(ED, 'p8-siheom') if t['y'] >= 1341 and t['size'] == 13.3]
cols = defaultdict(list)
for t in keys: cols[t['x']].append(t)
colstat = {}
for x, ts in sorted(cols.items()):
    last = max(ts, key=lambda z: z['y'])
    box = ink_box(last['t'], last['fam'], last['size'], last['bold'], last['x'], last['y'], last['anchor'])
    colstat[str(x)] = {'count': len(ts), 'last_baseline': last['y'],
                        'last_text': last['t'], 'last_ink_bottom': box[3]}
R['p8_keys_columns'] = colstat
R['p8_keys_max_baseline'] = max(t['y'] for t in keys)
R['p8_keys_max_ink_bottom'] = max(ink_box(t['t'], t['fam'], t['size'], t['bold'], t['x'], t['y'], t['anchor'])[3] for t in keys)

# ---- 3. P7 letters box + golden rule line + disclosure ----
for label, ed in (('edition', ED), ('core', CORE)):
    rects = [s for s in shapes(ed, 'p7-mal') if s['tag'] == 'rect' and s.get('x') == '1451' and s.get('y') == '1230.44']
    box = rects[0] if rects else None
    bottom = float(box['y']) + float(box['height']) if box else None
    ts = texts(ed, 'p7-mal')
    disc = [t for t in ts if t['x'] == 1473.0 and 1700 <= t['y'] <= 1780]
    rule = [s for s in shapes(ed, 'p7-mal') if s['tag'] == 'line' and s.get('y1') and 1740 <= float(s['y1']) <= 1800]
    R[f'p7_letter_box_{label}'] = {'rect': box, 'bottom': bottom,
        'disclosure_lines': [(t['y'], t['t']) for t in disc],
        'rule_lines': rule}
    if label == 'edition' and disc:
        last = disc[-1]
        box2 = ink_box(last['t'], last['fam'], last['size'], last['bold'], last['x'], last['y'], last['anchor'])
        R['p7_letter_last_ink'] = {'baseline': last['y'], 'ink_bottom': box2[3],
            'box_bottom': bottom, 'margin_to_box': bottom - box2[3],
            'rule_y': float(rule[0]['y1']) if rule else None,
            'gap_to_rule': (float(rule[0]['y1']) - box2[3]) if rule else None}
        disc_txt = ' '.join(t['t'] for t in disc)
        R['p7_disclosure_joined'] = disc_txt
        R['p7_disclosure_char_count'] = len(disc_txt)
        R['p7_disclosure_char_count_nospace'] = len(disc_txt.replace(' ', ''))
    if label == 'core' and disc:
        last = disc[-1]
        box2 = ink_box(last['t'], last['fam'], last['size'], last['bold'], last['x'], last['y'], last['anchor'])
        R['p7_core_last_ink'] = {'baseline': last['y'], 'ink_bottom': box2[3],
            'box_bottom': bottom, 'overshoot': box2[3] - bottom,
            'rule_y': float(rule[0]['y1']) if rule else None}

# P7 phrases + frequencies
def phrases(ed):
    ts = texts(ed, 'p7-mal')
    out = []
    for i, t in enumerate(ts):
        if t['t'].startswith('「') and t['t'].endswith('」') and t['size'] == 21.5 and t['y'] > 1800:
            # next GREY line is translation + page tag
            nxt = ts[i + 1] if i + 1 < len(ts) else None
            out.append({'ko': t['t'][1:-1], 'trans': nxt['t'] if nxt else None, 'y': t['y']})
    return out
R['phrases_edition'] = phrases(ED)
R['phrases_core'] = phrases(CORE)
# frequency: normalized (space-stripped) substring count over all pages' joined lines
def page_norm(ed, pg):
    return ''.join(t['t'] for t in texts(ed, pg)).replace(' ', '').replace('·', '')
freq_ed, freq_co = [], []
for ph in R['phrases_edition']:
    norm = ph['ko'].replace(' ', '')
    freq_ed.append(sum(page_norm(ED, pg).count(norm) for pg in PAGES))
    freq_co.append(sum(page_norm(CORE, pg).count(norm) for pg in PAGES))
R['phrase_freq_edition'] = freq_ed
R['phrase_freq_core'] = freq_co
# per-phrase tagged-page presence (article pages only, P7 excluded from search? tagged pages are 1..6)
tagmap = []
for ph in R['phrases_edition']:
    m = re.search(r'\((\d)면\)', ph['trans'] or '')
    tag = int(m.group(1)) if m else None
    pg = PAGES[tag - 1] if tag else None
    present = norm_present = None
    if pg:
        present = ph['ko'].replace(' ', '') in page_norm(ED, pg)
    tagmap.append({'phrase': ph['ko'], 'tag': tag, 'on_tagged_page': present})
R['phrase_tag_check'] = tagmap

# ---- 4. Model essay ----
# The model essay is the '예:' example in the H stem, P8 col 4 (x=1451), 14.5pt lines.
def essay(ed):
    ts = [t for t in texts(ed, 'p8-siheom') if t['x'] == 1451.0 and abs(t['size'] - 14.5) < 0.01]
    ts.sort(key=lambda z: z['y'])
    lines = []
    started = False
    for t in ts:
        if t['t'].startswith('예: '):
            started = True
            lines.append(t['t'][3:])
        elif started:
            lines.append(t['t'])
    joined = ''.join(lines)
    nospace = joined.replace(' ', '')
    return {'lines': lines, 'joined': joined, 'nospace_len': len(nospace),
            'first_sentence': joined.split('.')[0] + '.' if '.' in joined else joined[:40]}
R['essay_edition'] = essay(ED)
R['essay_core'] = essay(CORE)
R['essay_equal'] = essay(ED)['joined'] == essay(CORE)['joined']
# P7 word-box definition sentences frozen?
p7ed = texts(ED, 'p7-mal'); p7co = texts(CORE, 'p7-mal')
R['p7_frame_def_edition'] = [(t['y'], t['t']) for t in p7ed if t['x'] == 1473.0 and t['y'] in (1086.5, 1117.03)]
R['p7_frame_def_core'] = [(t['y'], t['t']) for t in p7co if t['x'] == 1473.0 and t['y'] in (1086.5, 1117.03)]
R['p7_frame_expl_edition'] = [(t['y'], t['t']) for t in p7ed if t['x'] == 1473.0 and t['y'] in (1177.56, 1205.96)]
R['p7_frame_expl_core'] = [(t['y'], t['t']) for t in p7co if t['x'] == 1473.0 and t['y'] in (1177.56, 1205.96)]

# ---- 5. Gloss: two calibers from rendered SVG ----
def gloss_groups(ed, pg):
    """Chain GREY 20.5 lines in DOCUMENT order: same x + pitch 20-35px
    (20.5pt * 1.45 = 29.725) continues a group, else a new group starts.
    A group is a GLOSS group if its joined text carries a headword-gloss pair
    (Italian ' = ' / '=' or a ' · ' list or a 'Nota — '/'译注｜' prefix);
    otherwise it is an INSTRUCTION segment (glossline() exercise instruction).
    P8 is excluded from both calibers (content8 H f-string line is not a
    gloss item, per ko-pt precedent)."""
    ts = [t for t in texts(ed, pg) if t['fill'] == '#57523f' and abs(t['size'] - 20.5) < 0.01]
    groups = []
    for t in ts:
        if groups and abs(t['x'] - groups[-1][-1]['x']) < 1 and 20 <= t['y'] - groups[-1][-1]['y'] <= 35:
            groups[-1].append(t)
        else:
            groups.append([t])
    return groups

HEADWORD_IT = re.compile(r'[\uac00-\ud7a3]+(?: [\uac00-\ud7a3]+)*\s*=')

def gloss_calibers(ed, pg):
    if pg == 'p8-siheom':
        return {'groups': [], 'v_items': 0, 'instr_segments': 0, 'rendered_lines': 0}
    v, instr, lines, det = 0, 0, 0, []
    for g in gloss_groups(ed, pg):
        s = ''.join(x['t'] for x in g)
        is_gloss = ('=' in s and HANGUL.search(s)) or (' · ' in s) or s.startswith('Nota — ') or s.startswith('译注｜')
        if is_gloss:
            lines += len(g)
            if '=' in s and not s.startswith('译注｜'):
                n = len(HEADWORD_IT.findall(s))
            else:
                # Chinese: split on '·' regardless of surrounding spaces — wraps
                # strip the space before '·' (e.g. '围裙 ·목록' is two items).
                n = len([p for p in s.split('·') if p.strip()])
            v += n; det.append(('GLOSS', n, s))
        else:
            instr += 1; det.append(('INSTR', 1, s))
    return {'groups': det, 'v_items': v, 'instr_segments': instr, 'rendered_lines': lines}
for label, ed in (('edition', ED), ('core', CORE)):
    per_page_v, per_page_f, per_page_lines, detail = [], [], [], {}
    for pg in PAGES:
        c = gloss_calibers(ed, pg)
        per_page_v.append(c['v_items'])
        per_page_f.append(c['v_items'] + c['instr_segments'])
        per_page_lines.append(c['rendered_lines'])
        detail[pg] = c['groups']
    R[f'gloss_V_{label}'] = per_page_v
    R[f'gloss_F_{label}'] = per_page_f
    R[f'gloss_rendered_lines_{label}'] = per_page_lines
    R[f'gloss_strings_{label}'] = detail

# ---- 6. Images ----
def images(ed, pg):
    root = ET.parse(f'{ed}/svg/{pg}.svg').getroot()
    out = []
    for el in root.iter(NS + 'image'):
        href = el.get('href') or ''
        payload = href.split(',', 1)[1] if ',' in href else ''
        raw = base64.b64decode(payload) if payload else b''
        try:
            from PIL import Image as PILImage
            im = PILImage.open(io.BytesIO(raw)); wh = im.size; fmt = im.format
        except Exception as e:
            wh, fmt = None, str(e)
        out.append({'b64_sha': hashlib.sha256(payload.encode()).hexdigest(),
                    'jpeg_sha': hashlib.sha256(raw).hexdigest(),
                    'size': wh, 'format': fmt, 'bytes': len(raw)})
    return out
for label, ed in (('edition', ED), ('core', CORE)):
    R[f'images_{label}'] = {pg: images(ed, pg) for pg in PAGES}
# credit lines
for label, ed in (('edition', ED), ('core', CORE), ('w43', W43)):
    cr = {}
    for pg in PAGES:
        cr[pg] = [t['t'] for t in texts(ed, pg) if '사진:' in t['t'] or '사진' in t['t'] and ('CC0' in t['t'] or 'Public domain' in t['t'] or 'Commons' in t['t'])]
    R[f'credits_{label}'] = cr

# ---- 7. Furniture ----
def find(ed, pg, pred):
    return [t for t in texts(ed, pg) if pred(t)]
for label, ed in (('edition', ED), ('core', CORE), ('w43', W43)):
    p1 = texts(ed, 'p1-pyoji')
    badge = [t for t in p1 if t['y'] == 394.0]
    R[f'badge_{label}'] = [(t['t'], t['size'], t['bold'], t['fill'], adv(t)) for t in badge]
    mast = [t for t in p1 if t['t'] == 'Lucerna']
    R[f'masthead_{label}'] = [(t['x'], t['y'], t['size']) for t in mast]
    foot, pageline = [], []
    for pg in PAGES:
        for t in texts(ed, pg):
            if t['y'] == 2624.0 and t['anchor'] == 'start': foot.append((pg, t['t'], adv(t)))
            if t['y'] == 2624.0 and t['anchor'] == 'end': pageline.append((pg, t['t'], adv(t)))
    R[f'footer_{label}'] = foot
    R[f'pageline_{label}'] = pageline
    # subtitle: P1 text at y=366 (edition/W43) or 372 (core), size 40 bold? find by y
    sub = [t for t in p1 if t['y'] in (366.0, 372.0) and t['size'] == 40.0]
    R[f'subtitle_{label}'] = [(t['t'], t['y'], adv(t)) for t in sub]
    gloss_pref = sorted(set(t['t'][:7] for pg in PAGES for t in texts(ed, pg) if t['t'].startswith('Nota — ') or t['t'].startswith('译注｜')))
    R[f'gloss_prefix_{label}'] = gloss_pref

# ---- 8. Right-edge ADVANCE scan + frame scan + same-baseline ink collisions ----
for label, ed in (('edition', ED), ('core', CORE)):
    mx, frame_bad = {}, []
    for pg in PAGES:
        best = (0, None)
        for t in texts(ed, pg):
            l, r = adv(t)
            if r > best[0]: best = (r, t['t'])
        mx[pg] = best
        for s in shapes(ed, pg):
            try:
                if s['tag'] == 'rect':
                    x, y, w, h = float(s['x']), float(s['y']), float(s['width']), float(s['height'])
                    if x < 0 or y < 0 or x + w > 1950 or y + h > 2700: frame_bad.append((pg, s))
                if s['tag'] == 'line':
                    for xx, yy in ((float(s['x1']), float(s['y1'])), (float(s['x2']), float(s['y2']))):
                        if not (0 <= xx <= 1950 and 0 <= yy <= 2700): frame_bad.append((pg, s))
            except (TypeError, ValueError):
                pass
    R[f'adv_max_{label}'] = mx
    R[f'frame_bad_{label}'] = frame_bad
# same-baseline ink overlap (0.6px tolerance grouping, edition only + core)
def baseline_collisions(ed):
    hits = []
    for pg in PAGES:
        ts = texts(ed, pg)
        groups = defaultdict(list)
        for t in ts: groups[round(t['y'] / 0.6)].append(t)
        for k, g in groups.items():
            if len(g) < 2: continue
            boxes = []
            for t in g:
                b = ink_box(t['t'], t['fam'], t['size'], t['bold'], t['x'], t['y'], t['anchor'])
                if b: boxes.append((t['t'], b))
            for i in range(len(boxes)):
                for j in range(i + 1, len(boxes)):
                    a, b = boxes[i][1], boxes[j][1]
                    if a[0] < b[2] and b[0] < a[2] and a[1] < b[3] and b[1] < a[3]:
                        hits.append((pg, k, boxes[i][0], boxes[j][0]))
    return hits
R['baseline_collisions_edition'] = baseline_collisions(ED)
R['baseline_collisions_core'] = baseline_collisions(CORE)
# P6 later-rect coverage (baseline-anchored ink boxes)
def p6_coverage(ed):
    root = ET.parse(f'{ed}/svg/p6-gipi.svg').getroot()
    elems = []
    for el in root.iter():
        tag = el.tag.replace(NS, '')
        if tag == 'text':
            elems.append(('text', ''.join(el.itertext()), float(el.get('x')), float(el.get('y')),
                          el.get('font-family'), float(el.get('font-size')),
                          el.get('font-weight') in ('700', 'bold'), el.get('text-anchor', 'start')))
        elif tag == 'rect':
            elems.append(('rect', float(el.get('x') or 0), float(el.get('y') or 0),
                          float(el.get('width') or 0), float(el.get('height') or 0)))
    worst_later, worst_any = (0, None), (0, None)
    for i, e in enumerate(elems):
        if e[0] != 'text': continue
        b = ink_box(e[1], e[4], e[5], e[6], e[2], e[3], e[7])
        if not b or b[2] <= b[0] or b[3] <= b[1]: continue
        area = (b[2] - b[0]) * (b[3] - b[1])
        for kind, rects in (('later', elems[i + 1:]), ('any', elems)):
            cov = 0.0
            for r in rects:
                if r[0] != 'rect': continue
                rx, ry, rw, rh = r[1], r[2], r[3], r[4]
                ix = max(0, min(b[2], rx + rw) - max(b[0], rx))
                iy = max(0, min(b[3], ry + rh) - max(b[1], ry))
                cov = max(cov, ix * iy / area)
            if kind == 'later' and cov > worst_later[0]: worst_later = (cov, e[1])
            if kind == 'any' and cov > worst_any[0]: worst_any = (cov, e[1])
    return {'worst_later': worst_later, 'worst_any': worst_any}
R['p6_coverage_edition'] = p6_coverage(ED)
R['p6_coverage_core'] = p6_coverage(CORE)

# ---- 9. Exercise number sequence from SVG ----
seq = {}
for pg in PAGES:
    nums = []
    for t in texts(ED, pg):
        m = re.match(r'^(\d+)[\.–—]', t['t'])
        # section headers like "101." chips: text exactly "101." handled by same regex
        if m and t['size'] in (24.0,):
            nums.append(int(m.group(1)))
    seq[pg] = nums
R['svg_exercise_labels_edition'] = seq

# ---- 10. P1 calendar clearance ----
p1 = texts(ED, 'p1-pyoji')
cal = [t for t in p1 if 'Cinque date' in t['t']]
src = [t for t in p1 if t['t'].startswith('자료:')]
if cal and src:
    cb = ink_box(cal[0]['t'], cal[0]['fam'], cal[0]['size'], cal[0]['bold'], cal[0]['x'], cal[0]['y'], cal[0]['anchor'])
    sb = ink_box(src[0]['t'], src[0]['fam'], src[0]['size'], src[0]['bold'], src[0]['x'], src[0]['y'], src[0]['anchor'])
    R['p1_calendar'] = {'cal': (cal[0]['y'], cal[0]['t'], cb), 'src': (src[0]['y'], src[0]['t'], sb),
                        'baseline_gap': src[0]['y'] - cal[0]['y'], 'ink_gap': sb[1] - cb[3]}

json.dump(R, open(WORK + '/analyze.json', 'w'), ensure_ascii=False, indent=1)
print('OK keys:', sorted(R.keys()))
print('han_total_edition', R['han_total_edition'], 'han_total_core', R['han_total_core'])
print('banned', {k: v for k, v in banned.items() if v})
print('pure_add', pure_add)
print('pure_rem', pure_rem)
print('gloss_V_ed', R['gloss_V_edition'], 'sum', sum(R['gloss_V_edition']))
print('gloss_V_co', R['gloss_V_core'], 'sum', sum(R['gloss_V_core']))
print('gloss_F_ed', R['gloss_F_edition'], 'sum', sum(R['gloss_F_edition']))
print('gloss_F_co', R['gloss_F_core'], 'sum', sum(R['gloss_F_core']))
print('gloss_lines_ed', R['gloss_rendered_lines_edition'])
print('gloss_lines_co', R['gloss_rendered_lines_core'])
print('phrases', [(p['ko'], p['trans']) for p in R['phrases_edition']])
print('freq_ed', freq_ed, 'freq_co', freq_co)
print('tag_check', tagmap)
print('p8 cols', colstat)
print('letter', R.get('p7_letter_last_ink'), 'core', R.get('p7_core_last_ink'))
print('adv_ed', R['adv_max_edition'])
print('frame_bad_ed', R['frame_bad_edition'])
print('base_coll_ed', R['baseline_collisions_edition'][:10], 'count', len(R['baseline_collisions_edition']))
print('p6cov', R['p6_coverage_edition'], R['p6_coverage_core'])
print('essay_ed', R['essay_edition'])
print('essay_co', R['essay_core'], 'equal', R['essay_equal'])
print('p8_104_ed', R['p8_104_edition'], 'co', R['p8_104_core'])
print('p8_137_ed', R['p8_137_edition'], 'co', R['p8_137_core'])
print('p8_138_ed', R['p8_138_edition'], 'co', R['p8_138_core'])
print('p8_139_ed', R['p8_139_edition'], 'co', R['p8_139_core'])
print('p8_140_ed', R['p8_140_edition'], 'co', R['p8_140_core'])
print('p8_150_ed', R['p8_150_edition'], 'co', R['p8_150_core'])
print('p8_sep_ed', R['p8_separators_edition'])
print('p8_sep_co', R['p8_separators_core'])
print('p8_han_ed', R['p8_han_edition'])
print('badge_ed', R['badge_edition'], 'badge_w43', R['badge_w43'])
print('subtitle_ed', R['subtitle_edition'], 'subtitle_w43', R['subtitle_w43'], 'subtitle_co', R['subtitle_core'])
print('footer_ed', R['footer_edition'])
print('pageline_ed', R['pageline_edition'])
print('gloss_prefix', R['gloss_prefix_edition'], R['gloss_prefix_w43'])
print('credits_ed', R['credits_edition'])
print('credits_w43', R['credits_w43'])
print('images_ed', {k: [(i['b64_sha'][:12], i['jpeg_sha'][:12], i['size']) for i in v] for k, v in R['images_edition'].items()})
print('images_co', {k: [(i['b64_sha'][:12], i['jpeg_sha'][:12], i['size']) for i in v] for k, v in R['images_core'].items()})
print('masthead', R['masthead_edition'], R['masthead_w43'], R['masthead_core'])
print('frame_def_equal', R['p7_frame_def_edition'] == R['p7_frame_def_core'], R['p7_frame_def_edition'])
print('svg_labels', R['svg_exercise_labels_edition'])
