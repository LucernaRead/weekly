import re, glob, sys

ED = 'files/weekly-report-w45-de-ko/svg/'
BUILD = 'hidden_files/weekly-report-w45-de-ko-build/'

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

# source inventory: all text from edition build content modules (raw file text)
src = ''
for f in glob.glob(BUILD + 'content*.py'):
    src += open(f, encoding='utf-8').read() + '\n'
src_nospace = re.sub(r'\s+', '', src)

def strip_tok(tok):
    return tok.strip(' .,!?;:()[]{}"“”‘’·%')

pages = {}
for path in sorted(glob.glob(ED + '*.svg')):
    pg = path.split('/')[-1]
    rows = parse(path)
    # group by (x, fs) within tolerance: x rounded to int, fs rounded
    groups = {}
    for r in rows:
        groups.setdefault((round(r['x']), round(r['fs'], 1)), []).append(r)
    splits = []
    line_start_punct = []
    line_start_dot = []
    block_final_short = []
    for key, g in groups.items():
        g.sort(key=lambda r: r['y'])
        for i, r in enumerate(g):
            t = r['t']
            if not t.strip():
                continue
            first = t.strip()[0]
            if first == '·':
                line_start_dot.append((pg, key, r['y'], t))
            elif first in '.,!?;:)%]}”':
                line_start_punct.append((pg, key, r['y'], t))
            # block final: next line gap >45 or none
            nxt = g[i+1] if i+1 < len(g) else None
            if nxt is None or not (10 <= nxt['y'] - r['y'] <= 45):
                # only consider lines containing Hangul and short
                if syl(t) <= 2 and re.search(r'[\uac00-\ud7a3]', t):
                    block_final_short.append((pg, key, r['y'], t, syl(t)))
            if nxt is None:
                continue
            gap = nxt['y'] - r['y']
            if not (10 <= gap <= 45):
                continue
            up = r['t'].strip().split()
            dn = nxt['t'].strip().split()
            if not up or not dn:
                continue
            F, T = strip_tok(up[-1]), strip_tok(dn[0])
            if not F or not T:
                continue
            if not re.search(r'[\uac00-\ud7a3]', F) or not re.search(r'[\uac00-\ud7a3]', T):
                continue
            # true split if F+T occurs contiguously in source (word or word+particle)
            if (F + T) in src_nospace:
                splits.append((pg, key, r['y'], f"{F}|{T}", syl(T), r['t'], nxt['t']))
    pages[pg] = (splits, line_start_punct, line_start_dot, block_final_short)

all_splits = []
for pg, (splits, lsp, lsd, bfs) in pages.items():
    print(f"== {pg}: splits={len(splits)} line-start-punct={len(lsp)} line-start-dot={len(lsd)} blockfinal<=2syl={len(bfs)}")
    for s in splits:
        print(f"   SPLIT {s[0]} y={s[2]} {s[3]} cont={s[4]} | up={s[5]!r} dn={s[6]!r}")
        all_splits.append(s)
    for x in lsp:
        print(f"   LSP {x[0]} x={x[1]} y={x[2]} {x[3]!r}")
    for x in lsd:
        print(f"   LSDOT {x[0]} x={x[1]} y={x[2]} {x[3]!r}")
    for x in bfs:
        print(f"   BLOCKFINAL {x[0]} x={x[1]} y={x[2]} syl={x[4]} {x[3]!r}")
s3 = [s for s in all_splits if s[4] >= 3]
print(f"TOTAL splits={len(all_splits)} S3(>=3)={len(s3)}")
for s in s3:
    print("  S3:", s)
