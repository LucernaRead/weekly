# Independent proofread checks for W45 ES x NL. Reads SHIPPED SVGs only.
import re, html, sys, json, hashlib, base64
from collections import Counter
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as OA

BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations/files'
CORE = BASE + '/weekly-report-w45-es-core/svg'
ED = BASE + '/weekly-report-w45-es-nl/svg'
W43 = BASE + '/weekly-report-es-nl/svg'
OUT = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/es-nl-proof/indep/'
PAGES = ['p1-portada','p2-vida','p3-cultura','p4-deporte','p5-juventud','p6-afondo','p7-lengua','p8-ejercicios']

def texts(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>', s, re.S):
        a = OA.parse_attrs(m.group(1))
        t = html.unescape(re.sub(r'<[^>]+>', '', m.group(2)))
        out.append({'x': OA.fnum(a,'x'), 'y': OA.fnum(a,'y'),
                    'size': OA.fnum(a,'font-size'), 'bold': a.get('font-weight')=='700',
                    'fam': a.get('font-family',''), 'anchor': a.get('text-anchor','start'),
                    'fill': a.get('fill',''), 't': t})
    return out

def fulltext(d):
    return '\n'.join(e['t'] for p in PAGES for e in texts(f'{d}/{p}.svg'))

# ---------- 1. Spanish token multiset diff ----------
tok = re.compile(r"[a-záéíóúñü]+", re.I)
cc, ec = Counter(), Counter()
for p in PAGES:
    cc.update(tok.findall(' '.join(e['t'] for e in texts(f'{CORE}/{p}.svg')).lower()))
    ec.update(tok.findall(' '.join(e['t'] for e in texts(f'{ED}/{p}.svg')).lower()))
lost = {t: cc[t]-ec[t] for t in cc if cc[t] > ec[t]}
gained = {t: ec[t]-cc[t] for t in ec if ec[t] > cc[t]}
print('== TOKEN DIFF lost:', dict(sorted(lost.items())))
print('== TOKEN DIFF gained (sample, Dutch + kept-Spanish):', dict(sorted(gained.items())[:60]), '... total gained types:', len(gained))

# ---------- 2. P8 dash-parse key verification ----------
def p8_answers(d):
    els = texts(f'{d}/p8-ejercicios.svg')
    ans, cur = {}, None
    for e in els:
        m = re.match(r'^(\d+)\.\s*(.*)$', e['t'].strip())
        if m and int(m.group(1)) <= 150 and (cur is None or int(m.group(1)) != cur):
            # only accept as new answer if it is in the ANSWERS section (y large) or first occurrence;
            # answers section starts after the RESPUESTAS header; track by order: numbers seen twice
            # (test items 1..38 on p8 top, then answers 1..150). Keep LAST occurrence block.
            cur = int(m.group(1)); ans.setdefault(cur, [])
            ans[cur].append(m.group(2))
        elif cur is not None and e['t'].strip():
            # continuation only if this element is not a new section header / separator
            if not re.match(r'^(RESPUESTAS|EJERCICIOS|— |MODELO|H\b)', e['t'].strip()):
                ans[cur].append(e['t'].strip())
    # The above keeps FIRST block (test items). Re-do: answers block = text after RESPUESTAS header.
    els2 = els
    start = next((i for i,e in enumerate(els2) if 'RESPUESTAS' in e['t']), None)
    ans, cur = {}, None
    for e in els2[start+1:]:
        m = re.match(r'^(\d+)\.\s*(.*)$', e['t'].strip())
        if m:
            cur = int(m.group(1)); ans[cur] = [m.group(2)]
        elif cur is not None and e['t'].strip() and not e['t'].strip().startswith('—'):
            # stop appending once we hit the MODELO section header text
            if 'MODELO' in e['t'] or e['t'].strip().startswith('H.'):
                cur = None
            else:
                ans[cur].append(e['t'].strip())
    keys = {}
    for n, parts in ans.items():
        joined = ' '.join(parts)
        if ' — ' in joined:
            keys[n] = joined.split(' — ', 1)[0].strip()
        else:
            keys[n] = joined.strip()
    return keys
ck, ek = p8_answers(CORE), p8_answers(ED)
print('== P8 dash-parse: core answers:', len(ck), 'edition answers:', len(ek))
diffs = {n: (ck.get(n), ek.get(n)) for n in sorted(set(ck)|set(ek)) if ck.get(n) != ek.get(n)}
for n,(a,b) in diffs.items():
    print(f'   KEYDIFF #{n}: core={a!r} edition={b!r}')
print('== P8 dash-parse diff count:', len(diffs))

# ---------- 3. Gloss split on · ----------
def gloss_boxes(d, prefixes):
    boxes = []
    for p in PAGES:
        for e in texts(f'{d}/{p}.svg'):
            for pre in prefixes:
                if e['t'].startswith(pre):
                    boxes.append((p, e['t'][len(pre):]))
    return boxes
cb = gloss_boxes(CORE, ['译注｜','讲解｜'])
eb = gloss_boxes(ED, ['Uitleg — '])
print('== GLOSS core boxes:', len(cb), 'edition boxes:', len(eb))
for (p, c), (_, e) in zip(cb, eb):
    ci, ei = [x.strip() for x in c.split('·')], [x.strip() for x in e.split('·')]
    ch = [re.split(r'[ （(]', x)[0].strip() for x in ci]
    eh = [re.split(r'[ （(]', x)[0].strip() for x in ei]
    print(f'   {p}: core {len(ci)} {ch} | ed {len(ei)} {eh} | headwords-equal={ch==eh}')
print('== GLOSS totals core:', sum(len(c.split('·')) for _,c in cb), 'edition:', sum(len(e.split('·')) for _,e in eb))

# ---------- 4. Image payloads ----------
def images(d):
    out = {}
    for p in PAGES:
        s = open(f'{d}/{p}.svg', encoding='utf-8').read()
        hs = []
        for m in re.finditer(r'xlink:href="data:image/[^;]+;base64,([^"]+)"', s):
            hs.append(hashlib.sha256(base64.b64decode(m.group(1))).hexdigest())
        if hs: out[p] = hs
    return out
ci, ei = images(CORE), images(ED)
print('== IMAGES core==edition payloads:', ci == ei, json.dumps(ci, indent=0), json.dumps(ei, indent=0))

# ---------- 5. P7 golden sentences x2 ----------
ed_full = ' '.join(fulltext(ED).split())
co_full = ' '.join(fulltext(CORE).split())
p7ed = texts(f'{ED}/p7-lengua.svg')
# golden section: text elements after the FRASES header element
gi = next((i for i,e in enumerate(p7ed) if 'FRASES' in e['t']), None)
print('== P7 FRASES header idx:', gi, p7ed[gi]['t'] if gi is not None else None)
# print surrounding elements for manual identification
for e in p7ed[gi:gi+40]:
    print('   P7ED:', repr(e['t'][:120]))

# ---------- 6. P6 chart ----------
def rects(d):
    s = open(f'{d}/p6-afondo.svg', encoding='utf-8').read()
    return sorted(re.findall(r'<rect[^>]*>', s))
cr, er = rects(CORE), rects(ED)
print('== P6 rects identical:', cr == er, 'core', len(cr), 'ed', len(er))
if cr != er:
    print('   only-core:', [r for r in Counter(cr)-Counter(er)])
    print('   only-ed:', [r for r in Counter(er)-Counter(cr)])
ct = [(e['x'],e['y'],e['t']) for e in texts(f'{CORE}/p6-afondo.svg') if e['y'] < 1950]
et = [(e['x'],e['y'],e['t']) for e in texts(f'{ED}/p6-afondo.svg') if e['y'] < 1950]
print('== P6 y<1950 texts core', len(ct), 'ed', len(et), 'identical:', ct == et)
if ct != et:
    for a,b in zip(ct, et):
        if a != b: print('   DIFF:', a, '||', b)

# ---------- 7. Furniture ----------
def find(d, p, needle):
    return [e for e in texts(f'{d}/{p}.svg') if needle in e['t']]
for label, d in [('ED', ED), ('W43', W43)]:
    b = find(d, 'p1-portada', 'TEKSTEN IN HET SPAANS')
    print(f'== {label} badge:', [(e['x'],e['y'],e['size'],e['bold'],e['fill'],e['t']) for e in b])
    sub = [e for e in texts(f'{d}/p1-portada.svg') if e['y']==330]
    print(f'== {label} y=330:', [(e['x'],e['size'],e['t']) for e in sub])
    top = [e for e in texts(f'{d}/p1-portada.svg') if e['y']==92]
    print(f'== {label} y=92:', [(e['x'],e['size'],e['t']) for e in top])
for p in PAGES:
    ef = [e['t'] for e in texts(f'{ED}/{p}.svg') if e['y']==2624]
    print(f'== ED footer {p}:', ef)

# ---------- 8. Bans / pins ----------
han = re.compile(r'[\u4e00-\u9fff]')
for p in PAGES:
    s = open(f'{ED}/{p}.svg', encoding='utf-8').read()
    hs = han.findall(s)
    fw = s.count('（') + s.count('）')
    print(f'== {p}: Han chars={len(hs)} {hs[:10]} fullwidth-parens={fw}')
ed_all = fulltext(ED)
for needle in ['桥接', 'bridge', '12 de noviembre', '12 november', '(Página', 'PÁGINA']:
    print(f'== ED contains {needle!r}:', ed_all.count(needle))
print('== ED Pagina tags:', re.findall(r'\(Pagina \d\)', ed_all), 'count', len(re.findall(r'\(Pagina \d\)', ed_all)))
print('== ED P8 separators:', re.findall(r'— Pagina \d —', ed_all))
print('== ED Pagina-footer lines:', re.findall(r'Pagina \d van 8', ed_all))
print('== ED 12-nov check raw:', '12 de noviembre' in ed_all)

# ---------- 9. Readers letters P7 ----------
p7c = ' '.join(e['t'] for e in texts(f'{CORE}/p7-lengua.svg'))
p7e = ' '.join(e['t'] for e in texts(f'{ED}/p7-lengua.svg'))
for frag in ['CARTAS DE LOS LECTORES', 'Nota de la redacción', 'VOL.3']:
    print(f'== P7 frag {frag!r}: core={frag in p7c} ed={frag in p7e}')
i = p7e.find('Opmerking')
print('== ED Dutch disclosure:', p7e[i:i+220] if i>=0 else 'NOT FOUND')
i = p7c.find('Nota de la redacción')
print('== CORE Spanish note:', p7c[i:i+220] if i>=0 else 'NOT FOUND')
# Spanish letter: compare letter body - elements between CARTAS header and disclosure in core vs ed
def letter_block(d):
    els = texts(f'{d}/p7-lengua.svg')
    s = next(i for i,e in enumerate(els) if 'CARTAS' in e['t'])
    return [e['t'] for e in els[s:s+30]]
lc, le = letter_block(CORE), letter_block(ED)
print('== P7 letter-block core vs ed equal:', lc == le)
if lc != le:
    for a,b in zip(lc, le):
        if a != b: print('   LETTER DIFF:', repr(a), '||', repr(b))

# ---------- 10. Model text P8 H ----------
def model(d):
    els = texts(f'{d}/p8-ejercicios.svg')
    s = next((i for i,e in enumerate(els) if e['t'].strip() == 'H' or 'MODELO' in e['t']), None)
    return s, [e['t'] for e in els[s:s+15]] if s is not None else []
print('== MODEL core:', model(CORE))
print('== MODEL ed:', model(ED))
