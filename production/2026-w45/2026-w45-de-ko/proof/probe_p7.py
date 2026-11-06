import re, sys

def texts(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'<text[^>]*>', s):
        tag = m.group(0)
        xm = re.search(r'x="([\d.]+)"', tag); ym = re.search(r'y="([\d.]+)"', tag)
        end = s.find('</text>', m.end())
        if end < 0 or not xm or not ym:
            continue
        t = re.sub(r'<[^>]+>', '', s[m.end():end])
        out.append((float(ym.group(1)), float(xm.group(1)), t))
    return sorted(out)

for label, path in [('CORE', 'files/weekly-report-w45-de-core/svg/p7-sprache.svg'),
                    ('KO', 'files/weekly-report-w45-de-ko/svg/p7-sprache.svg'),
                    ('EN', 'files/weekly-report-de-en/svg/p7-sprache.svg')]:
    try:
        rows = texts(path)
    except Exception as e:
        print(label, 'ERR', e); continue
    print(f"===== {label} =====")
    for y, x, t in rows:
        if 'NOCH' in t or 'WORT' in t:
            print(f"  y={y} x={x} {t!r}")
    noch = [(y, x, t) for y, x, t in rows if 'NOCH' in t]
    if noch:
        y0 = noch[0][0]
        print(f"  --- rows y in [{y0}, {y0+400}] (box region) ---")
        for y, x, t in rows:
            if y0 - 5 <= y <= y0 + 400:
                print(f"  y={y} x={x} {t!r}")
