# Independent check round 3 for W45 ES x NL.
import re, html, sys, hashlib
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
def norm(s): return ' '.join(s.split())

# --- P7 quote tags, P7 section only ---
for d, label, pat in [(CORE,'CORE',r'\(Página (\d)\)'), (ED,'ED',r'\(Pagina (\d)\)')]:
    els = texts(f'{d}/p7-lengua.svg')
    gi = next(i for i,e in enumerate(els) if 'FRASES' in e['t'])
    seg = els[gi:]
    tags = []
    for e in seg:
        tags += re.findall(pat, e['t'])
        if 'PRÓXIMA' in e['t']: break
    print(f'== P7-SECTION tags {label}: {tags} Counter={dict(Counter(tags))}')
    # all pagina-mentioning elements on P7
    for e in els:
        if 'gina' in e['t']:
            print(f'   P7 {label} gina-el:', repr(e['t'][:130]))

# --- Quotes unquoted x2 ---
ed_full = norm(' '.join(e['t'] for p in PAGES for e in texts(f'{ED}/{p}.svg')))
co_full = norm(' '.join(e['t'] for p in PAGES for e in texts(f'{CORE}/{p}.svg')))
p7ed = texts(f'{ED}/p7-lengua.svg')
gi = next(i for i,e in enumerate(p7ed) if 'FRASES' in e['t'])
quotes, i = [], gi+1
while len(quotes) < 8 and i < len(p7ed):
    if p7ed[i]['t'].startswith('«'):
        q = p7ed[i]['t']; j = i+1
        while '»' not in q and j < len(p7ed):
            q += ' ' + p7ed[j]['t']; j += 1
        quotes.append(norm(q)); i = j
    else:
        i += 1
for q in quotes:
    bare = q.strip('«»')
    src_ed = [p for p in PAGES if bare in norm(' '.join(e['t'] for e in texts(f'{ED}/{p}.svg')))]
    src_co = [p for p in PAGES if bare in norm(' '.join(e['t'] for e in texts(f'{CORE}/{p}.svg')))]
    print(f'== QUOTE bare ed={ed_full.count(bare)} core={co_full.count(bare)} src_ed={src_ed} src_co={src_co} :: {bare[:80]}')

# --- (Página body refs: locate pages in ED ---
for p in PAGES:
    for e in texts(f'{ED}/{p}.svg'):
        if '(Página' in e['t'] or '(Páginas' in e['t']:
            print(f'== ED body Pagina-ref {p}:', repr(e['t'][:160]))
for p in PAGES:
    for e in texts(f'{CORE}/{p}.svg'):
        if '(Página' in e['t'] or '(Páginas' in e['t']:
            print(f'== CORE body Pagina-ref {p}:', repr(e['t'][:160]))

# --- Model text: from build code, verify in both SVGs ---
s = open('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-es-build/content8.py', encoding='utf-8').read()
m = re.search(r'MODELO\s*=\s*["\'](.*?)["\']', s, re.S)
print('== MODELO in core code found:', bool(m))
if m:
    modelo = norm(m.group(1))
    print('== MODELO words:', len(modelo.split()), '::', modelo[:200])
    print('== MODELO in core SVG:', modelo in co_full, '| in ed SVG:', modelo in ed_full)
    # also find where it sits in P8: first element containing its start
    for d, label in [(CORE,'CORE'), (ED,'ED')]:
        els = texts(f'{d}/p8-ejercicios.svg')
        hits = [i for i,e in enumerate(els) if 'Madrid' in e['t'] and 'puente' in e['t']]
        print(f'== MODEL-locating {label} hits:', hits[:5], [els[i]['t'][:100] for i in hits[:3]])

# --- Image asset hashes vs KIT claims ---
import glob, os
for b in ['weekly-report-w45-es-build', 'weekly-report-w45-es-nl-build']:
    for f in sorted(glob.glob(f'/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/{b}/assets/*')):
        data = open(f,'rb').read()
        print(f'== ASSET {b}/{os.path.basename(f)} sha256={hashlib.sha256(data).hexdigest()} bytes={len(data)}')

# --- PDF pages + KIT cross-checks ---
import subprocess
for f in ['La-Lucerna-VOL2-NL.pdf','La-Lucerna-VOL2-NL-web.pdf']:
    out = subprocess.run(['pdfinfo', f'{BASE}/weekly-report-w45-es-nl/{f}'], capture_output=True, text=True).stdout
    print(f'== PDFINFO {f}:', [l for l in out.splitlines() if l.startswith(('Pages','Title'))], 'bytes=', os.path.getsize(f'{BASE}/weekly-report-w45-es-nl/{f}'))
kit = open(f'{BASE}/weekly-report-w45-es-nl/WEEKLY-KIT.md', encoding='utf-8').read()
for p in PAGES:
    h = hashlib.sha256(open(f'{ED}/{p}.svg','rb').read()).hexdigest()
    print(f'== KIT SVG hash present {p}:', h in kit, h[:16])
for h in ['7e0398c1412ac99e0934331f8672488347e9fc1fe7373a13e788c8b725c3fbec','4130e4bef0c5d8150200307ed5fac2705929d95948edc1676408fcbc7bc7b549']:
    print('== KIT PDF hash present:', h in kit, h[:16])
ab = open(f'{BASE}/weekly-report-w45-es-nl/ABSTRACT.txt','rb').read()
print('== ABSTRACT bytes:', ab)
print('== ABSTRACT in KIT §12:', ab.decode().strip() in kit)
print('== ABSTRACT lines:', ab.decode().count('\n'), 'ascii-quote:', b'"' in ab)

# --- Same-baseline row scan (own implementation, OA ink boxes) ---
def rowscan(d, label):
    flags = []
    for p in PAGES:
        els = texts(f'{d}/{p}.svg')
        by_y = {}
        for e in els:
            by_y.setdefault(round(e['y'],1), []).append(e)
        for y, grp in by_y.items():
            if len(grp) < 2: continue
            boxes = []
            for e in grp:
                try:
                    ink = OA.ink_box(e['t'], e['fam'], e['size'], e['bold'], e['x'], e['y'], e['anchor'])
                except Exception:
                    continue
                boxes.append((ink, e))
            boxes.sort(key=lambda b: b[0][0])
            for (b1,e1),(b2,e2) in zip(boxes, boxes[1:]):
                gap = b2[0] - b1[2]
                if gap < 6.0:
                    flags.append((p, y, round(gap,2), e1['t'][:40], e2['t'][:40]))
    print(f'== ROWSCAN {label}: {len(flags)} sub-6px same-baseline gaps')
    for f in flags: print('   ', f)
    return flags
fc, fe = rowscan(CORE, 'CORE'), rowscan(ED, 'ED')
print('== ROWSCAN identical core vs ed:', fc == fe)

# --- P1 ED vs W43 element diff (furniture hunt) ---
def elset(d, p):
    return Counter((e['x'],e['y'],e['size'],e['t']) for e in texts(f'{d}/{p}.svg'))
for p in ['p1-portada','p7-lengua','p8-ejercicios']:
    cw, ce = elset(W43, p), elset(ED, p)
    only_w = list((cw - ce).elements()); only_e = list((ce - cw).elements())
    print(f'== P1/W43-diff {p}: only-W43={len(only_w)} only-ED={len(only_e)}')
    # print differing elements that look like furniture (short, Dutch, or header/footer-like)
    for e in sorted(set(only_w)):
        if len(e[3]) < 90 and ('·' in e[3] or e[3].startswith(('VOL','La ','SEMANA','Lees','Antwoorden','EJERCICIOS','RESPUESTAS','Pagina'))):
            print(f'   W43-only: {e}')
    for e in sorted(set(only_e)):
        if len(e[3]) < 90 and ('·' in e[3] or e[3].startswith(('VOL','La ','SEMANA','Lees','Antwoorden','EJERCICIOS','RESPUESTAS','Pagina'))):
            print(f'   ED-only:  {e}')
