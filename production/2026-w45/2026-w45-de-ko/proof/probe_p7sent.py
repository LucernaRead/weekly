import re, glob

def alltext(path):
    s = open(path, encoding='utf-8').read()
    return re.sub(r'<[^>]+>', ' ', s)

def rows(path):
    s = open(path, encoding='utf-8').read()
    out = []
    for m in re.finditer(r'<text[^>]*>', s):
        tag = m.group(0)
        xm = re.search(r'x="([\d.]+)"', tag); ym = re.search(r'y="([\d.]+)"', tag)
        end = s.find('</text>', m.end())
        if end < 0 or not xm or not ym:
            continue
        out.append((float(ym.group(1)), float(xm.group(1)), re.sub(r'<[^>]+>', '', s[m.end():end])))
    return sorted(out)

ed = 'files/weekly-report-w45-de-ko/svg/'
core = 'files/weekly-report-w45-de-core/svg/'

# P7 table: German quotes are lines starting with „ at y>=1597, in 4 columns
for label, d in [('KO', ed), ('CORE', core)]:
    r = rows(d + 'p7-sprache.svg')
    print(f"--- {label} P7 SÄTZE table ---")
    # group: quote lines (start with „) then continuation, then translation, then Seite label
    cols = {}
    for y, x, t in r:
        if y >= 1590 and y <= 1800:
            cols.setdefault(x, []).append((y, t))
    for x in sorted(cols):
        print(f"  col x={x}:")
        for y, t in cols[x]:
            print(f"    y={y} {t!r}")

# count occurrences of each German quote across whole edition
quotes = [
    'Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.',
    'Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.',
    'Wer 50 Liter tankt, spart rund 8,35 Euro.',
    'Die Schule hat nach den Herbstferien wieder begonnen.',
]
print("--- occurrence counts (normalized whitespace) ---")
for label, d in [('KO', ed), ('CORE', core)]:
    whole = ''
    for f in sorted(glob.glob(d + '*.svg')):
        whole += ' ' + re.sub(r'\s+', ' ', alltext(f))
    whole_n = re.sub(r'\s+', ' ', whole)
    print(f"  {label}:")
    for q in quotes:
        print(f"    {whole_n.count(q)} x {q[:60]}...")
