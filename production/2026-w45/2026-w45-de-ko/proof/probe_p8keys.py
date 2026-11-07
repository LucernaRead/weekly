import re, sys

def lines(path):
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

for label, path in [('CORE', 'files/weekly-report-w45-de-core/svg/p8-uebungen.svg'),
                    ('KO', 'files/weekly-report-w45-de-ko/svg/p8-uebungen.svg')]:
    rows = lines(path)
    print(f"===== {label} =====")
    for want in [137, 138, 139, 140, 150]:
        # find line starting with "N. " or containing "N. " at start (allow leading spaces)
        idx = None
        for i, (y, x, t) in enumerate(rows):
            if re.match(rf'^{want}\.\s', t.strip()):
                idx = i; break
        if idx is None:
            print(f"  {want}: NOT FOUND as line start"); continue
        # join following lines on nearby y until next numbered line
        buf = [rows[idx][2].strip()]
        j = idx + 1
        while j < len(rows):
            y, x, t = rows[j]
            if re.match(r'^\d+\.\s', t.strip()):
                break
            if y - rows[j-1][0] > 60:
                break
            buf.append(t.strip()); j += 1
        print(f"  {want}: {' '.join(buf)}")
