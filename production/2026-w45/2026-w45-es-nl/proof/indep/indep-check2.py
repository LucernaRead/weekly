# Independent check round 2 for W45 ES x NL.
import re, html, sys, json, hashlib, base64
from collections import Counter
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/tools')
import occlusion_audit as OA

BASE = '/home/hatch/workspace/goals/lucernaread-social-media-operations/files'
CORE = BASE + '/weekly-report-w45-es-core/svg'
ED = BASE + '/weekly-report-w45-es-nl/svg'
W43 = BASE + '/weekly-report-es-nl/svg'
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

# --- per-page token lost ---
tok = re.compile(r"[a-záéíóúñü]+", re.I)
for p in PAGES:
    cc = Counter(tok.findall(' '.join(e['t'] for e in texts(f'{CORE}/{p}.svg')).lower()))
    ec = Counter(tok.findall(' '.join(e['t'] for e in texts(f'{ED}/{p}.svg')).lower()))
    lost = {t: cc[t]-ec[t] for t in cc if cc[t] > ec[t]}
    print(f'== TOKEN lost {p}:', dict(sorted(lost.items())))

# --- P8 keys for the 20 tool-keydiff numbers, dash-parse, from raw answer segments ---
def p8_segments(d):
    els = texts(f'{d}/p8-ejercicios.svg')
    start = next(i for i,e in enumerate(els) if 'RESPUESTAS' in e['t'])
    ans, cur = {}, None
    for e in els[start+1:]:
        m = re.match(r'^(\d+)\.\s*(.*)$', e['t'].strip())
        if m:
            cur = int(m.group(1)); ans[cur] = [m.group(2)]
        elif cur is not None and e['t'].strip():
            if e['t'].strip().startswith('—') or 'La Lucerna ·' in e['t'] or e['t'].strip().startswith('Pagina'):
                if 'La Lucerna ·' in e['t']: cur = None
                continue
            ans[cur].append(e['t'].strip())
    out = {}
    for n, parts in ans.items():
        j = ' '.join(parts)
        out[n] = j.split(' — ', 1)[0].strip() if ' — ' in j else j.strip()
        out['full_%d' % n] = j
    return out
ck, ek = p8_segments(CORE), p8_segments(ED)
for n in [17,18,19,20,60,61,62,63,64,72,83,85,95,96,98,107,117,137,138,148,150]:
    print(f'== P8 #{n} core-key={ck.get(n)!r} ed-key={ek.get(n)!r} EQUAL={ck.get(n)==ek.get(n)}')
print('== P8 #150 core full:', ck.get('full_150'))
print('== P8 #150 ed full:', ek.get('full_150'))
print('== P8 #72 core full:', ck.get('full_72'))
print('== P8 #72 ed full:', ek.get('full_72'))
print('== P8 #148 core full:', ck.get('full_148'))
print('== P8 #148 ed full:', ek.get('full_148'))

# --- Gloss from BUILD CODE (README #21: split gloss() call string on .) ---
import glob
def gloss_calls(build):
    calls = []
    for f in sorted(glob.glob(build + '/content*.py')):
        s = open(f, encoding='utf-8').read()
        for m in re.finditer(r'gloss\((.*?)\)\s*$', s, re.M):
            calls.append((f.split('/')[-1], m.group(1)))
        # also gloss("...") inline forms
        for m in re.finditer(r'gloss\(["\'](.*?)["\']\)', s):
            calls.append((f.split('/')[-1]+':inline', m.group(1)))
    return calls
CB = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-build'
EB = '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-nl-build'
for label, b in [('CORE', CB), ('ED', EB)]:
    print(f'== GLOSS-CODE {label}:')
    tot = 0
    for fn, call in gloss_calls(b):
        # extract string literals inside the call
        lits = re.findall(r'["\'](.*?)["\']', call)
        joined = ''.join(lits)
        items = [x.strip() for x in joined.split('·') if x.strip()]
        tot += len(items)
        heads = [re.split(r'[ （(]', x)[0].strip() for x in items]
        print(f'   {fn}: {len(items)} items heads={heads} raw={joined[:150]!r}')
    print(f'   TOTAL {label}: {tot}')

# --- Images: tag form ---
for d, label in [(CORE,'CORE'), (ED,'ED')]:
    for p in PAGES:
        s = open(f'{d}/{p}.svg', encoding='utf-8').read()
        imgs = re.findall(r'<image[^>]*>', s)
        if imgs:
            print(f'== IMAGE {label} {p}:', [i[:120] for i in imgs])
            for m in re.finditer(r'href="data:image/[^;]+;base64,([^"]+)"', s):
                print('   payload sha256:', hashlib.sha256(base64.b64decode(m.group(1))).hexdigest())

# --- P7 quotes x2 ---
def norm(s): return ' '.join(s.split())
ed_full = norm(' '.join(e['t'] for p in PAGES for e in texts(f'{ED}/{p}.svg')))
co_full = norm(' '.join(e['t'] for p in PAGES for e in texts(f'{CORE}/{p}.svg')))
p7ed = texts(f'{ED}/p7-lengua.svg')
gi = next(i for i,e in enumerate(p7ed) if 'FRASES' in e['t'])
quotes = []
i = gi+1
while len(quotes) < 8 and i < len(p7ed):
    if p7ed[i]['t'].startswith('«'):
        q = p7ed[i]['t']
        j = i+1
        while '»' not in q and j < len(p7ed):
            q += ' ' + p7ed[j]['t']; j += 1
        quotes.append(norm(q)); i = j
    else:
        i += 1
for q in quotes:
    print(f'== QUOTE ed-count={ed_full.count(q)} core-count={co_full.count(q)} :: {q[:90]}')
# quote source pages in core: find each quote's first occurrence page
for q in quotes:
    pages = [p for p in PAGES if q in norm(' '.join(e['t'] for e in texts(f'{CORE}/{p}.svg')))]
    print(f'== QUOTE source pages (core): {pages} :: {q[:60]}')
# (Pagina)/(Página) tag distributions
print('== ED (Pagina N):', Counter(re.findall(r'\(Pagina (\d)\)', ed_full)))
print('== CORE (Página N):', Counter(re.findall(r'\(Página (\d)\)', co_full)))
print('== ED (Página occurrences):', [(m.start(), ed_full[max(0,m.start()-60):m.start()+20]) for m in re.finditer(r'\(Página', ed_full)])
print('== CORE (Pagina occurrences):', [(m.start(), co_full[max(0,m.start()-60):m.start()+20]) for m in re.finditer(r'\(Pagina', co_full)])

# --- P6 chart-area rects (y<1950) ---
def rects(d):
    s = open(f'{d}/p6-afondo.svg', encoding='utf-8').read()
    out = []
    for m in re.finditer(r'<rect([^>]*)/>', s):
        a = OA.parse_attrs(m.group(1))
        out.append((OA.fnum(a,'x'), OA.fnum(a,'y'), OA.fnum(a,'width'), OA.fnum(a,'height'), a.get('fill','')))
    return out
cr = [r for r in rects(CORE) if r[1] < 1950]
er = [r for r in rects(ED) if r[1] < 1950]
print('== P6 chart-area rects identical:', cr == er, len(cr), len(er))
if cr != er:
    print('  only-core:', [r for r in Counter(cr)-Counter(er)])
    print('  only-ed:', [r for r in Counter(er)-Counter(er)])
# Inmigración graze: ink box vs later bars
lab = [e for e in texts(f'{ED}/p6-afondo.svg') if e['t']=='Inmigración'][0]
print('== Inmigración el:', lab)
ink = OA.ink_box('Inmigración', lab['fam'], lab['size'], lab['bold'], lab['x'], lab['y'], lab['anchor'])
print('== Inmigración ink box:', ink)
s = open(f'{ED}/p6-afondo.svg', encoding='utf-8').read()
# bars near label: rects with y in 1650..1800
for r in rects(ED):
    if 1600 < r[1] < 1800:
        print('   bar near label:', r)
# same for core
labc = [e for e in texts(f'{CORE}/p6-afondo.svg') if e['t']=='Inmigración'][0]
print('== CORE Inmigración ink box:', OA.ink_box('Inmigración', labc['fam'], labc['size'], labc['bold'], labc['x'], labc['y'], labc['anchor']))

# --- Furniture W43 vs ED ---
def furniture(d):
    out = {}
    p1 = texts(f'{d}/p1-portada.svg')
    out['badge'] = [(e['x'],e['y'],e['size'],e['bold'],e['fill'],e['t']) for e in p1 if 'TEKSTEN IN HET SPAANS' in e['t'] and e['y']<500]
    out['subtitle330'] = [(e['x'],e['size'],e['t']) for e in p1 if e['y']==330]
    out['top92'] = [(e['x'],e['size'],e['t']) for e in p1 if e['y']==92]
    out['gloss_prefixes'] = Counter()
    for p in PAGES:
        for e in texts(f'{d}/{p}.svg'):
            if e['t'].startswith('Uitleg'): out['gloss_prefixes']['Uitleg'] += 1
    p8 = texts(f'{d}/p8-ejercicios.svg')
    out['p8_header'] = [e['t'] for e in p8 if 'RESPUESTAS' in e['t']]
    out['p8_sub'] = [e['t'] for e in p8 if 'Antwoorden' in e['t'] or 'per pagina' in e['t']]
    out['p8_sep'] = sorted(set(re.findall(r'— Pagina \d —', ' '.join(e['t'] for e in p8))))
    out['ex_heads'] = sorted(set(e['t'] for p in PAGES for e in texts(f'{d}/{p}.svg') if e['t'].startswith('EJERCICIOS')))
    out['ans_ptr'] = sorted(set(e['t'] for p in PAGES for e in texts(f'{d}/{p}.svg') if 'Antwoorden op pagina 8' in e['t']))
    return out
fw, fe = furniture(W43), furniture(ED)
for k in fw:
    print(f'== FURN {k}: W43={fw[k]} || ED={fe[k]} || SAME={fw[k]==fe[k]}')

# --- P7 letter body + attribution ---
def letter_span(d):
    els = texts(f'{d}/p7-lengua.svg')
    s = next(i for i,e in enumerate(els) if 'CARTAS' in e['t'])
    return els[s:]
lc, le = letter_span(CORE), letter_span(ED)
# Spanish letter lines: elements after CARTAS header up to the Spanish editorial note start
def span_until(els, needle):
    out = []
    for e in els[1:]:
        if needle in e['t']: break
        out.append(e['t'])
    return out
print('== LETTER core pre-note:', span_until(lc, 'Nota de la redacción'))
print('== LETTER ed pre-note:', span_until(le, 'Opmerking'))
print('== LETTER core note lines:', [e['t'] for e in lc if 'Nota de la redacción' in e['t'] or e['t'].startswith('al cierre') or 'ejemplo' in e['t']][:6])
print('== LETTER ed note lines:', [e['t'] for e in le if 'Nota de la redacción' in e['t'] or 'al cierre' in e['t']][:6])
for d, label in [(CORE,'CORE'), (ED,'ED')]:
    for e in texts(f'{d}/p7-lengua.svg'):
        if '（' in e['t']: print(f'== FULLWIDTH-PAREN {label}:', repr(e['t']))

# --- Model text P8 section H ---
for d, label in [(CORE,'CORE'), (ED,'ED')]:
    els = texts(f'{d}/p8-ejercicios.svg')
    for i,e in enumerate(els):
        if '84' in e['t'] and ('MODELO' in e['t'] or 'Modelo' in e['t'] or 'modelo' in e['t']):
            print(f'== MODEL marker {label} idx {i}:', repr(e['t']))
    # dump last 25 elements
    print(f'== P8 tail {label}:', [e['t'][:80] for e in els[-25:]])

# --- Build-code checks ---
import subprocess
for f in ['svglib.py']:
    a = open(f'{CB}/{f}','rb').read(); b = open(f'{EB}/{f}','rb').read()
    print(f'== BUILD {f} byte-identical core-vs-ed:', a==b, hashlib.sha256(a).hexdigest()[:12], hashlib.sha256(b).hexdigest()[:12])
d = subprocess.run(['diff', f'{CB}/bslib4.py', f'{EB}/bslib4.py'], capture_output=True, text=True).stdout
print('== BUILD bslib4.py diff lines:', len(d.splitlines()))
print(d[:3000])
for pat in ['bridge', '（', 'Uitleg']:
    for label, b in [('CORE', CB), ('ED', EB)]:
        n = 0
        for f in glob.glob(b + '/*.py'):
            n += open(f, encoding='utf-8').read().count(pat)
        print(f'== BUILD-CODE {pat!r} count {label}: {n}')
