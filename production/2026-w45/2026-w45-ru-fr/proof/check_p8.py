import re, pathlib, html, collections, json
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def texts(p):
    s=p.read_text()
    out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        ym=re.search(r'\by="([\d.]+)"', m.group(1))
        txt=html.unescape(re.sub(r'<[^>]+>','',m.group(2))).strip()
        out.append((float(ym.group(1)) if ym else 0, txt))
    return out
def parse(path):
    # P8 answers: text elements starting with "N. " in keys area; they may wrap: a key line continues on next text element without number?
    # Strategy mirroring builder claim: split on first " — " for lines that start with number.
    # First collect all texts in document order, group: numbered line = start, following non-numbered lines are continuations until next numbered.
    ts=texts(path)
    items={}  # num -> full joined text
    cur=None
    for y,t in ts:
        m=re.match(r'^(\d+)\.\s+(.*)$', t)
        if m:
            cur=int(m.group(1)); items[cur]=m.group(2)
        elif cur is not None and t and not re.match(r'^(?:— |[A-ZÉÈ])', t) and cur>=1:
            # continuation only if previous item not yet closed? Heuristic: append if t doesn't look like a header/footer/separator
            # We'll instead only append when the line is a continuation of an answer: check y proximity is hard here; use separate approach below.
            pass
    return ts, items
for label, f in [('core','files/weekly-report-w45-ru-core/svg/p8-test.svg'),('ed','files/weekly-report-w45-ru-fr/svg/p8-test.svg')]:
    ts, items = parse(base/f)
    print('\n##',label,'total text elements',len(ts))
    # print numbered lines for keys of interest, in doc order, plus next 2 texts after each
    for i,(y,t) in enumerate(ts):
        m=re.match(r'^(83|137|138|139|140|148|150)\.\s', t)
        if m:
            print(f"  [{m.group(1)}] y={y} :: {t[:300]}")
            for y2,t2 in ts[i+1:i+3]:
                print(f"      cont y={y2} :: {t2[:200]}")
    # full-width parens in whole svg
    s=(base/f).read_text()
    print('  fullwidth paren count (（/）):', s.count('（')+s.count('）'), 'halfwidth ( in P8 texts:', sum(t.count('(') for _,t in ts))
    # keys flow: max y among numbered answer lines?
    nums=[(y,t) for y,t in ts if re.match(r'^\d+\.\s', t)]
    print('  numbered lines:', len(nums), 'max y:', max(y for y,_ in nums))
