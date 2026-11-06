import re, html
def texts(path):
    t = open(path, encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'<text[^>]*>(.*?)</text>', t, re.S):
        s = re.sub(r'<[^>]+>', '', m.group(1))
        out.append(html.unescape(s))
    return out
for label, path in [('CORE','files/weekly-report-w45-pt-core/svg/p8-avaliacao.svg'),('ED','files/weekly-report-w45-pt-fr/svg/p8-avaliacao.svg')]:
    ts = texts(path)
    print(f"===== {label}")
    for i,s in enumerate(ts):
        if s.strip() in ('137.','138.','139.','140.') or re.match(r'^(137|138|139|140)\.', s.strip()):
            print(f"[{i}] {s!r}  NEXT: {ts[i+1:i+3]!r}")
    # CJK scan
    import unicodedata
    cjk = [s for s in ts if any('\u4e00' <= c <= '\u9fff' for c in s)]
    print("CJK text nodes:", len(cjk), cjk[:5])
