import re, glob

def rows(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'<text[^>]*>', s):
        tag = m.group(0)
        xm = re.search(r'x="([\d.]+)"', tag); ym = re.search(r'y="([\d.]+)"', tag)
        fm = re.search(r'font-size="([\d.]+)"', tag)
        end = s.find('</text>', m.end())
        if end < 0 or not xm or not ym:
            continue
        out.append((float(ym.group(1)), float(xm.group(1)), float(fm.group(1)) if fm else 0,
                    re.sub(r'<[^>]+>', '', s[m.end():end])))
    return sorted(out)

for label, d, prefix in [('KO', 'files/weekly-report-w45-de-ko/svg/', '해설'),
                         ('CORE', 'files/weekly-report-w45-de-core/svg/', None)]:
    print(f"--- {label} ---")
    tot = 0
    for f in sorted(glob.glob(d + 'p[2-6]*.svg')):
        r = rows(f)
        # find gloss start: line containing '해설' (KO) or '讲解' (core)
        starts = [x for x in r if ('해설' in x[3] and x[3].strip().startswith('해설')) or ('译注' in x[3] and x[3].strip().startswith('译注'))]
        if not starts:
            print(f"  {f.split('/')[-1]}: NO gloss start found"); continue
        y0, x0, fs0, t0 = starts[0]
        # collect consecutive lines same x, gap ~29.7 (20.5pt*1.45) or 29.725
        block = [t0]
        cur = y0
        for (y, x, fs, t) in r:
            if x == x0 and 20 < y - cur < 40:
                block.append(t); cur = y
        full = ' '.join(b.strip() for b in block)
        # strip prefix up to first German word: prefix is '해설 — ' or '讲解｜'
        full2 = re.sub(r'^(해설\s*—\s*|译注\s*｜\s*)', '', full)
        items = [i.strip() for i in full2.split('·')]
        items = [i for i in items if i]
        tot += len(items)
        print(f"  {f.split('/')[-1]}: lines={len(block)} items={len(items)}")
        for i in items:
            print(f"      - {i}")
    print(f"  TOTAL {tot}")
