import re, glob

def parse(path):
    s = open(path, encoding='utf-8').read()
    rows = []
    for m in re.finditer(r'<text[^>]*>', s):
        tag = m.group(0)
        xm = re.search(r'x="([\d.]+)"', tag); ym = re.search(r'y="([\d.]+)"', tag)
        fm = re.search(r'font-size="([\d.]+)"', tag)
        end = s.find('</text>', m.end())
        if end < 0 or not xm or not ym:
            continue
        t = re.sub(r'<[^>]+>', '', s[m.end():end])
        rows.append({'x': float(xm.group(1)), 'y': float(ym.group(1)),
                     'fs': float(fm.group(1)) if fm else 0, 't': t})
    return rows

def syl(s):
    return sum(1 for c in s if '\uac00' <= c <= '\ud7a3')

def strip_tok(tok):
    return tok.strip(' .,!?;:()[]{}"“”‘’·%')

# token inventory: single whitespace-delimited tokens from edition build sources
BUILD = 'hidden_files/weekly-report-w45-de-ko-build/'
tokens = set()
for f in glob.glob(BUILD + 'content*.py') + glob.glob(BUILD + 'bslib4.py'):
    txt = open(f, encoding='utf-8').read()
    for tok in re.split(r'\s+', txt):
        t = strip_tok(tok)
        if t and re.search(r'[\uac00-\ud7a3]', t):
            tokens.add(t)

def scan(ed_dir):
    out = {}
    for path in sorted(glob.glob(ed_dir + '*.svg')):
        pg = path.split('/')[-1]
        rows = parse(path)
        groups = {}
        for r in rows:
            groups.setdefault((round(r['x']), round(r['fs'], 1)), []).append(r)
        splits, lsp, lsd, lsparen = [], [], [], []
        for key, g in groups.items():
            g.sort(key=lambda r: r['y'])
            for i, r in enumerate(g):
                t = r['t'].strip()
                if t:
                    first = t[0]
                    if first == '·':
                        lsd.append((pg, key, r['y'], r['t']))
                    elif first in '.,!?;:)%]}”':
                        lsp.append((pg, key, r['y'], r['t']))
                    elif first == '(':
                        lsparen.append((pg, key, r['y'], r['t']))
                if i + 1 >= len(g):
                    continue
                nxt = g[i + 1]
                gap = nxt['y'] - r['y']
                if not (10 <= gap <= 45):
                    continue
                up = r['t'].strip().split(); dn = nxt['t'].strip().split()
                if not up or not dn:
                    continue
                F, T = strip_tok(up[-1]), strip_tok(dn[0])
                if not F or not T:
                    continue
                if not re.search(r'[\uac00-\ud7a3]', F) or not re.search(r'[\uac00-\ud7a3]', T):
                    continue
                if (F + T) in tokens:
                    splits.append((pg, r['y'], f"{F}|{T}", syl(T)))
        out[pg] = (splits, lsp, lsd, lsparen)
    return out

for label, d in [('EDITION', 'files/weekly-report-w45-de-ko/svg/'),
                 ('CORE', 'files/weekly-report-w45-de-core/svg/')]:
    res = scan(d)
    print(f"##### {label} #####")
    tot = 0; s3 = 0
    for pg, (splits, lsp, lsd, lsparen) in res.items():
        print(f"== {pg}: splits={len(splits)} S3={sum(1 for s in splits if s[3]>=3)} LSP={len(lsp)} LSDOT={len(lsd)} LPAREN={len(lsparen)}")
        for s in splits:
            print(f"   SPLIT y={s[1]} {s[2]} cont={s[3]}")
        for x in lsp:
            print(f"   LSP x={x[1]} y={x[2]} {x[3]!r}")
        for x in lsd:
            print(f"   LSDOT x={x[1]} y={x[2]} {x[3]!r}")
        for x in lsparen:
            print(f"   LPAREN x={x[1]} y={x[2]} {x[3]!r}")
        tot += len(splits); s3 += sum(1 for s in splits if s[3] >= 3)
    print(f"{label} TOTAL splits={tot} S3={s3}")
