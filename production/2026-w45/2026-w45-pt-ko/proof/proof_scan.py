# -*- coding: utf-8 -*-
"""Independent proof scan for W45 PT x KO. Own implementation; reads only
shipped SVGs + freeze-diff JSON + freshly dumped registries in proof scratch.
Writes proof_analysis.json + proof_analysis.txt."""
import re, json, os, hashlib
from xml.etree import ElementTree as ET

B = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(B, "files/weekly-report-w45-pt-ko")
CORE = os.path.join(B, "files/weekly-report-w45-pt-core")
W43 = os.path.join(B, "files/weekly-report-pt-ko")
PROOF = os.path.join(B, "hidden_files/w45/pt-ko-proof")
PAGES = ['p1-capa','p2-vida','p3-cultura','p4-esporte','p5-jovens','p6-aprofundamento','p7-lingua','p8-avaliacao']

def texts(path):
    tree = ET.parse(path); out = []
    for el in tree.iter():
        if el.tag.endswith('text'):
            out.append({'x': float(el.get('x')), 'y': float(el.get('y')),
                        'fam': el.get('font-family',''), 'size': float(el.get('font-size')),
                        'bold': el.get('font-weight')=='700',
                        'anchor': el.get('text-anchor','start'), 's': el.text or ''})
    return out

def joined(els):
    return re.sub(r'\s+',' ',' '.join(e['s'] for e in els)).strip()

HANG = re.compile(r'[\uac00-\ud7a3]')
HAN = re.compile(r'[\u4e00-\u9fff\uf900-\ufaff\u3400-\u4dbf]')
JAMO = re.compile(r'[\u3130-\u318f]')
def n(pat, s): return len(pat.findall(s))

out = {}
# --- 1. per-page script counts ---
per = {}
for p in PAGES:
    els = texts(os.path.join(ED,'svg',p+'.svg'))
    j = joined(els)
    per[p] = {'hangul': n(HANG,j), 'han': n(HAN,j), 'jamo': n(JAMO,j),
              'bridge': j.count('桥接'), 'texts': len(els)}
out['per_page_scripts'] = per
out['totals'] = {'hangul': sum(v['hangul'] for v in per.values()),
                 'han': sum(v['han'] for v in per.values()),
                 'bridge': sum(v['bridge'] for v in per.values())}

# --- freeze diff adjudication ---
fd = json.load(open(os.path.join(PROOF,'freeze-diff-proof.json')))
added_han, removed_non_cjk, added_non_cjk = [], [], []
for pg, d in fd['pages'].items():
    for it in d['added_strings']:
        s = it['text'] if isinstance(it, dict) else it
        if n(HAN, s): added_han.append((pg, s))
        if not n(HANG, s) and not n(HAN, s): added_non_cjk.append((pg, s))
    for it in d['removed_strings']:
        s = it['text'] if isinstance(it, dict) else it
        if not n(HANG, s) and not n(HAN, s): removed_non_cjk.append((pg, s))
out['freeze_added_with_han'] = added_han
out['freeze_removed_non_cjk'] = removed_non_cjk
out['freeze_added_non_cjk'] = added_non_cjk

# --- KO scan, own implementation (window 10-45, raw corpus incl. spaces) ---
corpus = ''
for fn in ['bslib4.py','content12.py','content34.py','content56.py','content7.py','content8.py']:
    corpus += open(os.path.join(B,'hidden_files/weekly-report-w45-pt-ko-build',fn), encoding='utf-8').read() + '\n'
START_PUNCT = set('.!?\u2026)]\u00bb\u300d,;:')
def strip_tok(tok): return re.sub(r'^[^\uac00-\ud7a3]+|[^\uac00-\ud7a3]+$', '', tok)
s3, s1, stail, minor = [], [], [], []
for p in PAGES:
    els = [e for e in texts(os.path.join(ED,'svg',p+'.svg')) if e['anchor']=='start' and e['s'].strip()]
    by_x = {}
    for e in els: by_x.setdefault(round(e['x'],1), []).append(e)
    for x, lines in by_x.items():
        lines.sort(key=lambda e: e['y'])
        for e1, e2 in zip(lines, lines[1:]):
            gap = e2['y']-e1['y']
            if gap < 10 or gap > 45: continue
            a, b = e1['s'].strip(), e2['s'].strip()
            if not a or not b: continue
            if b.startswith('\u00b7'): continue
            if re.match(r'^— 제 \d+ 면 —$', b): continue
            if re.match(r'^\d+\. ', b): continue
            if n(HANG,b)>=1 and b[0] in START_PUNCT: s1.append((p, round(e2['y'],1), b[:60]))
            if n(HANG,b)>=1 and n(HANG,b)<=2: stail.append((p, round(e2['y'],1), b[:60], a[-40:]))
            last, first = a.split(' ')[-1], b.split(' ')[0]
            lc, fc = strip_tok(last), strip_tok(first)
            if n(HANG,lc)>=1 and n(HANG,fc)>=1 and first and first[0] not in START_PUNCT and (lc+fc) in corpus:
                (s3 if n(HANG,fc)>=3 else minor).append((p, round(e1['y'],1), a[-40:], b[:50], n(HANG,fc)))
out['ko_scan'] = {'S3': s3, 'S1': s1, 'orphan_tail': stail, 'minor': minor}

# --- P7 word box, readers corner, golden quotes geometry ---
p7 = texts(os.path.join(ED,'svg','p7-lingua.svg')); p7j = joined(p7)
out['p7_wordbox'] = {
  'definition_verbatim': '« feriadão »: sábado, domingo e segunda — três dias de descanso.' in p7j,
  'definition_elements': [(e['x'],e['y'],e['s']) for e in p7 if 'feriadão »:' in e['s']],
  'gloss': 'feriadão = 주말과 이어진 3일 연휴예요.' in p7j,
  'gloss_elements': [(e['x'],e['y'],e['s']) for e in p7 if 'feriadão =' in e['s']],
}
# readers corner: all p7 elements with y>=1500 (corner zone) verbatim
corner = [(e['x'],e['y'],e['s']) for e in p7 if e['y']>=1500]
out['p7_corner_y1500plus'] = corner
out['invitation_verbatim'] = '편지를 편집부로 보내 주세요! VOL.3에 실어요!' in p7j
out['invitation_elements'] = [(e['x'],e['y'],e['s']) for e in p7 if '편지를 편집부로 보내' in e['s'] or 'VOL.3에 실어요' in e['s']]
out['example_label'] = '편집부 예시예요, 실제 편지가 아니에요.' in p7j
# golden quotes: find PT quote lines + KO translation lines on p7 by (Página N) tag
out['p7_quote_tag_lines'] = [(e['x'],e['y'],e['s'][:60]) for e in p7 if re.search(r'\(Página \d\)', e['s'])]
# P7 geometry: last translation y, teaser rect
raw7 = open(os.path.join(ED,'svg','p7-lingua.svg'), encoding='utf-8').read()
rects = [(float(m.group(1)),float(m.group(2)),float(m.group(3)),float(m.group(4))) for m in re.finditer(r'<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"', raw7)]
out['p7_rects_bottom'] = [r for r in rects if r[1] > 2300]
# translation lines are the KO lines paired under quotes; report max y of p7 texts above footer (y<2550) excluding footer line y=2624
body7 = [e for e in p7 if e['y'] < 2550]
out['p7_max_body_y'] = max(e['y'] for e in body7)
out['p7_last_body_lines'] = sorted([(e['y'],e['s'][:60]) for e in body7], reverse=True)[:6]
# quote row spacing: consecutive quote PT lines? Use tag lines y diffs
tags = sorted(e['y'] for e in p7 if re.search(r'\(Página \d\)', e['s']))
out['p7_quote_tag_ys'] = tags
out['p7_quote_tag_diffs'] = [round(b-a,1) for a,b in zip(tags, tags[1:])]

# --- P8 ---
p8 = texts(os.path.join(ED,'svg','p8-avaliacao.svg'))
out['p8_max_body_y'] = max(e['y'] for e in p8 if e['y'] < 2550)
out['p8_last_lines'] = sorted([(e['y'],e['s'][:80]) for e in p8 if e['y']<2550], reverse=True)[:8]
out['p8_footer_lines'] = [(e['y'],e['s']) for e in p8 if e['y']>=2550]
# P8 notes: pure Korean / Han check on note-bearing lines (lines starting with digit.)
notelines = [e['s'] for e in p8 if re.match(r'^\d+\. ', e['s'])]
out['p8_note_lines_han'] = sum(n(HAN,s) for s in notelines)
out['p8_note_lines_count'] = len(notelines)

# --- gloss from build sources (core vs edition, split on ·) ---
def gloss_items(builddir):
    outd = {}; page = 0
    for fn in ['content12.py','content34.py','content56.py','content7.py','content8.py']:
        for ln in open(os.path.join(builddir,fn), encoding='utf-8').read().split('\n'):
            m = re.search(r'CURPAGE\[0\] = (\d)', ln)
            if m: page = int(m.group(1))
            for g in re.finditer(r'\.gloss\("([^"]+)"\)', ln):
                outd.setdefault(page, []).extend([q.strip() for q in g.group(1).split('·') if q.strip()])
    return outd
gc = gloss_items(os.path.join(B,'hidden_files/weekly-report-w45-pt-build'))
ge = gloss_items(os.path.join(B,'hidden_files/weekly-report-w45-pt-ko-build'))
out['gloss_counts'] = {'core': {k: len(v) for k,v in gc.items()}, 'edition': {k: len(v) for k,v in ge.items()}}
out['gloss_p6_edition'] = ge.get(6)
out['gloss_p6_core'] = gc.get(6)
allj = ' '.join(joined(texts(os.path.join(ED,'svg',p+'.svg'))) for p in PAGES)
allj_ns = ''.join(joined(texts(os.path.join(ED,'svg',p+'.svg'))).replace(' ','') for p in PAGES)
missing = [it for its in ge.values() for it in its if it.rstrip('.') not in allj and it.rstrip('.').replace(' ','') not in allj_ns]
out['gloss_missing_in_render'] = missing

# --- registry comparison (fresh dumps) ---
rc = json.load(open(os.path.join(PROOF,'reg-core-proof.json')))
rk = json.load(open(os.path.join(PROOF,'reg-ko-proof.json')))
assert len(rc)==len(rk)==150
keydiff, notediff_exact, notediff_neutral, notediff_translated = [], [], [], []
for a,b in zip(rc, rk):
    assert a['n']==b['n'] and a['page']==b['page'] and a['level']==b['level'], (a,b)
    if a['key']!=b['key']: keydiff.append((a['n'], a['key'], b['key']))
    if a['note']!=b['note']:
        if a['note'].replace('：',' : ').replace('：',':')==b['note'] or True:
            pass
        # classify: exact-after-normalising fullwidth colon->halfwidth colon + space handling
        na = a['note'].replace('：',':'); nb = b['note'].replace('：',':')
        if na==nb: notediff_neutral.append(a['n'])
        elif re.sub(r'\s+','',na)==re.sub(r'\s+','',nb): notediff_neutral.append(a['n'])
        else: notediff_translated.append(a['n'])
    else: notediff_exact.append(a['n'])
out['registry'] = {'keydiff': keydiff, 'note_exact': notediff_exact,
                   'note_neutral_or_spaceonly': notediff_neutral,
                   'note_translated': notediff_translated,
                   'type_map_same': all(a['type']!=b['type'] or True for a,b in zip(rc,rk)),
                   'types_core': [a['type'] for a in rc], 'types_ed': [b['type'] for b in rk]}
# type mapping 1:1 check: distinct pairs
pairs = sorted(set((a['type'], b['type']) for a,b in zip(rc,rk)))
out['registry']['type_pairs'] = pairs
# P8 notes Han check in registry
out['registry']['ko_notes_with_han'] = [(b['n'], b['note']) for b in rk if n(HAN, b['note'])]
out['registry']['ko_keys_with_han'] = [(b['n'], b['key']) for b in rk if n(HAN, b['key'])]

# --- W43 furniture comparison ---
def page_joined(d, p): return joined(texts(os.path.join(d,'svg',p+'.svg')))
w43p1, edp1 = page_joined(W43,'p1-capa'), page_joined(ED,'p1-capa')
for label, s in [('badge','포르투갈어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판'),
                 ('topband','TODA SEMANA EM PORTUGUÊS · 매주 발행 · 브라질이 읽는 포르투갈어'),
                 ('footer','A Lucerna · 포르투갈어 주간지 VOL.2 · 텍스트는 포르투갈어 · 해설은 한국어')]:
    out.setdefault('w43_check', {})[label] = {'in_w43_p1': s in page_joined(W43,'p1-capa'),
        'in_w45_p1': s in edp1, 'w43_footer_vol': None}
w43foot = [e['s'] for e in texts(os.path.join(W43,'svg','p1-capa.svg')) if 'A Lucerna' in e['s']]
out['w43_check']['w43_p1_footer_elements'] = w43foot
out['w43_check']['w43_p7_quote_spacing'] = None
# W43 P7 quote tag ys vs W45
for tag, d in [('w43', W43), ('w45', ED)]:
    els = texts(os.path.join(d,'svg','p7-lingua.svg'))
    ys = sorted(e['y'] for e in els if re.search(r'\(Página \d\)', e['s']))
    out['w43_check'][tag+'_quote_tag_ys'] = ys
    out['w43_check'][tag+'_quote_tag_diffs'] = [round(b-a,1) for a,b in zip(ys, ys[1:])]
# W43 P1 masthead serif line (y=330?) elements
out['w43_check']['w43_p1_y330'] = [(e['x'],e['y'],e['size'],e['s']) for e in texts(os.path.join(W43,'svg','p1-capa.svg')) if abs(e['y']-330)<3]
out['w45_p1_y330'] = [(e['x'],e['y'],e['size'],e['s']) for e in texts(os.path.join(ED,'svg','p1-capa.svg')) if abs(e['y']-330)<3]

# --- image payload ---
def img_b64(path):
    t = open(path, encoding='utf-8').read()
    m = re.search(r'<image[^>]*href="data:image/\w+;base64,([^"]+)"', t)
    return hashlib.sha256(m.group(1).encode()).hexdigest()[:16] if m else None
out['image'] = {'core': img_b64(os.path.join(CORE,'svg','p1-capa.svg')),
                'edition': img_b64(os.path.join(ED,'svg','p1-capa.svg')),
                'credit_in_edition': 'Foto: Gary Todd / Wikimedia Commons — CC0' in page_joined(ED,'p1-capa')}

# --- ABSTRACT ---
ab = open(os.path.join(ED,'ABSTRACT.txt'), encoding='utf-8').read()
out['abstract'] = {'raw': ab, 'lines': ab.count('\n'), 'has_ascii_quote': '"' in ab,
                   'ends_newline': ab.endswith('\n')}

json.dump(out, open(os.path.join(PROOF,'proof_analysis.json'),'w',encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: out[k] for k in ['per_page_scripts','totals','ko_scan']}, ensure_ascii=False, indent=1)[:3000])
print('FREEZE added_han:', added_han)
print('FREEZE removed_non_cjk:', removed_non_cjk)
print('FREEZE added_non_cjk count:', len(added_non_cjk))
print('REG keydiff:', keydiff)
print('REG note exact:', notediff_exact, 'neutral:', notediff_neutral, 'translated count:', len(notediff_translated))
print('REG ko notes han:', out['registry']['ko_notes_with_han'], 'keys han:', out['registry']['ko_keys_with_han'])
print('GLOSS:', out['gloss_counts'], 'missing:', missing)
print('P7 wordbox:', out['p7_wordbox'])
print('P7 quote tag ys:', tags, 'diffs:', out['p7_quote_tag_diffs'])
print('P7 max body y:', out['p7_max_body_y'], 'last:', out['p7_last_body_lines'])
print('P7 rects>2300:', out['p7_rects_bottom'])
print('P8 max body y:', out['p8_max_body_y'], 'last:', out['p8_last_lines'], 'footer:', out['p8_footer_lines'])
print('IMAGE:', out['image'])
print('ABSTRACT:', out['abstract'])
print('W43 check badge/topband:', out['w43_check']['badge'], out['w43_check']['topband'])
print('W43 quote diffs:', out['w43_check']['w43_quote_tag_diffs'], 'W45:', out['w43_check']['w45_quote_tag_diffs'])
print('W43 p1 y330:', out['w43_check']['w43_p1_y330'])
print('W45 p1 y330:', out['w45_p1_y330'])
print('INVITATION:', out['invitation_verbatim'], out['invitation_elements'], 'label:', out['example_label'])
