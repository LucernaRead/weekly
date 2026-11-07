import re, sys, xml.etree.ElementTree as ET
def texts(path):
    t = open(path, encoding='utf-8').read()
    # SVG text elements: extract in document order, decode entities via ET on text nodes
    # Simpler: use regex on <text ...>...</text> and unescape
    import html
    out=[]
    for m in re.finditer(r'<text[^>]*>(.*?)</text>', t, re.S):
        s = re.sub(r'<[^>]+>', '', m.group(1))
        out.append(html.unescape(s))
    return out
for label, path in [('CORE','files/weekly-report-w45-pt-core/svg/p8-avaliacao.svg'),('ED','files/weekly-report-w45-pt-fr/svg/p8-avaliacao.svg')]:
    ts = texts(path)
    print(f"===== {label} total text nodes {len(ts)}")
    # join consecutive? P8 answers are separate lines; print any node starting with target numbers
    for n in (2,4,101,137,138,139,140,146,150):
        hits=[s for s in ts if re.match(rf'^{n}[.\s]', s.strip()) or s.strip().startswith(f'{n}.') or s.strip().startswith(f'{n} ')]
        print(f"-- {n}: {hits}")
