import re, html, pathlib, collections
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
def chart_elements(path):
    s=path.read_text(encoding='utf-8')
    items=[]
    # texts: keep (x,y,size,weight,text) if inside chart boxes
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        a=m.group(1); t=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        x=float(re.search(r'x="([\d.]+)"',a).group(1)); y=float(re.search(r'y="([\d.]+)"',a).group(1))
        if (65<=x<=960 and 1620<=y<=1905) or (990<=x<=1900 and 1620<=y<=1905):
            items.append(('text', a.strip(), t))
    for m in re.finditer(r'<rect\b([^>]*?)/?>', s):
        a=m.group(1)
        xm=re.search(r'x="([\d.]+)"',a); ym=re.search(r'y="([\d.]+)"',a)
        if xm and ym:
            x=float(xm.group(1)); y=float(ym.group(1))
            if (65<=x<=960 and 1620<=y<=1905) or (990<=x<=1900 and 1620<=y<=1905):
                items.append(('rect', a.strip(), ''))
    return items
core=chart_elements(base/"files/weekly-report-w45-es-core/svg/p6-afondo.svg")
ed=chart_elements(base/"files/weekly-report-w45-es-pt/svg/p6-afondo.svg")
print("core chart-region elements:", len(core), "edition:", len(ed))
cc, ce = collections.Counter(core), collections.Counter(ed)
print("in core not edition:", list((cc-ce).items()))
print("in edition not core:", list((ce-cc).items()))
print("\n--- core chart texts ---")
for k,a,t in core:
    if k=='text': print(f"  {t!r} :: {a}")
print("\n--- core chart rects ---")
for k,a,t in core:
    if k=='rect': print(f"  {a}")
