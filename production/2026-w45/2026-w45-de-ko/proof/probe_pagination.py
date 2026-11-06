import re, glob

for label, path in [('KO', 'files/weekly-report-w45-de-ko/svg/p8-uebungen.svg'),
                    ('CORE', 'files/weekly-report-w45-de-core/svg/p8-uebungen.svg')]:
    s = open(path, encoding='utf-8').read()
    rows = []
    for m in re.finditer(r'<text[^>]*>', s):
        tag = m.group(0)
        xm = re.search(r'x="([\d.]+)"', tag); ym = re.search(r'y="([\d.]+)"', tag)
        fm = re.search(r'font-size="([\d.]+)"', tag)
        end = s.find('</text>', m.end())
        if end < 0 or not xm or not ym or not fm:
            continue
        rows.append((float(ym.group(1)), float(xm.group(1)), float(fm.group(1)),
                     re.sub(r'<[^>]+>', '', s[m.end():end])))
    # answer flow = 13.0pt (KO) / 14.5pt (CORE) lines + 17pt separators
    cols = {}
    for y, x, fs, t in rows:
        if fs in (13.0, 14.5, 17.0):
            cols.setdefault(x, []).append((y, fs, t))
    groups = {}  # source page -> set of answer numbers
    for x, lines in cols.items():
        lines.sort()
        cur = None
        for y, fs, t in lines:
            m = re.search(r'—\s*제\s*(\d+)\s*면\s*—', t) or re.search(r'—\s*第\s*(\d+)\s*版\s*—', t)
            if m:
                cur = int(m.group(1)); continue
            if cur is None:
                continue
            for nm in re.finditer(r'(?<![\d.])(\d{1,3})\.\s', t):
                groups.setdefault(cur, set()).add(int(nm.group(1)))
    print(f"--- {label} answer groups by source page ---")
    prev = 0
    for pg in sorted(groups):
        ns = sorted(groups[pg])
        print(f"  source p{pg}: answers {min(ns)}..{max(ns)} count={len(ns)} -> exercises on page = {max(ns)-prev} (cumulative {max(ns)})")
        prev = max(ns)
    alln = set().union(*groups.values()) if groups else set()
    print(f"  total distinct answers grouped: {len(alln)}, missing: {[n for n in range(1,151) if n not in alln]}")
