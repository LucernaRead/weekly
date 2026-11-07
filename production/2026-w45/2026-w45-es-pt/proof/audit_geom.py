import re, html, pathlib
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def els(path):
    s=path.read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        a=m.group(1); t=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        x=float(re.search(r'x="([\d.]+)"',a).group(1)); y=float(re.search(r'y="([\d.]+)"',a).group(1))
        fs=float(re.search(r'font-size="([\d.]+)"',a).group(1))
        out.append((x,y,fs,t))
    return out, s
def rects(path):
    s=path.read_text(encoding='utf-8'); out=[]
    for m in re.finditer(r'<rect\b([^>]*?)/?>', s):
        a=m.group(1)
        def g(k):
            mm=re.search(rf'{k}="([\d.]+)"',a); return float(mm.group(1)) if mm else None
        out.append((g('x'),g('y'),g('width'),g('height'),a))
    return out
print("=== P5 exercise flow: max y of exercise texts (excluding footer y>=2580 band) ===")
for label,root in [('CORE','files/weekly-report-w45-es-core/svg'),('ED','files/weekly-report-w45-es-pt/svg')]:
    ts,_=els(base/f"{root}/p5-juventud.svg")
    body=[(x,y,fs,t) for x,y,fs,t in ts if y<2580]
    print(f"  {label} max body y={max(y for x,y,fs,t in body)} :: {[t for x,y,fs,t in body if y==max(y for x2,y2,fs2,t2 in body)][0][:80]!r}")
    # last 5 body elements in doc order with y>2400
    print(f"    tail: {[(round(y,2),t[:60]) for x,y,fs,t in ts if y>2400 and y<2580][-6:]}")
print("\n=== P7 col3 tail + preview rect ===")
for label,root in [('CORE','files/weekly-report-w45-es-core/svg'),('ED','files/weekly-report-w45-es-pt/svg')]:
    ts,_=els(base/f"{root}/p7-lengua.svg")
    rs=rects(base/f"{root}/p7-lengua.svg")
    # preview box: rect near y 2440; col3: texts in third column x~? print rects with y in 2430-2450 and 1800-1830 region texts
    print(f"  {label} rects y 2435-2445: {[(x,y,w,h) for x,y,w,h,a in rs if y and 2435<=y<=2445]}")
    print(f"  {label} rects y 2550-2565 (preview bottom): {[(x,y,w,h) for x,y,w,h,a in rs if y and 2550<=y<=2565]}")
    # col3 tail: disclosure text elements - find 'Nota da redação' / core equivalent and following lines, print their y
    for i,(x,y,fs,t) in enumerate(ts):
        if 'Nota da redação' in t or '编者注' in t or 'Nota de la redacción' in t:
            print(f"    disclosure start [{i}] y={y} :: {t[:100]!r}")
            for j in range(i, min(i+6,len(ts))):
                print(f"      [{j}] y={ts[j][1]} :: {ts[j][3][:110]!r}")
            break
    # also: max y among texts with y<2400 excluding footer (preview title baseline 2484?)
    mid=[(x,y,fs,t) for x,y,fs,t in ts if y<2400]
    print(f"    max y<2400: {max(y for x,y,fs,t in mid)}")
print("\n=== P8 #137/#138 line counts (answer-section elements) ===")
for label,root in [('CORE','files/weekly-report-w45-es-core/svg'),('ED','files/weekly-report-w45-es-pt/svg')]:
    ts,_=els(base/f"{root}/p8-ejercicios.svg")
    start=[i for i,(x,y,fs,t) in enumerate(ts) if t.startswith('RESPUESTAS ·')][0]
    for n in (137,138):
        idx=[i for i in range(start,len(ts)) if ts[i][3].startswith(f"{n}.")]
        i=idx[0]
        # continuation = next elements until next numbered answer or separator
        cont=[ts[i][3]]
        j=i+1
        while j<len(ts) and not re.match(r'^\d+\.\s', ts[j][3]) and not ts[j][3].startswith('— PÁGINA') and not ts[j][3].startswith('La Lucerna'):
            cont.append(ts[j][3]); j+=1
        print(f"  {label} #{n}: lines={len(cont)} y={[ts[k][1] for k in range(i,j)]} :: {cont}")
