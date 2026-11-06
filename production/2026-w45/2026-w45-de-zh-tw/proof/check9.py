import re, html, pathlib, collections
G=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
def elems(p):
    s=p.read_text(encoding="utf-8"); out=[]
    for m in re.finditer(r'<text ([^>]*)>(.*?)</text>', s, re.S):
        a=m.group(1); txt=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        xm=re.search(r'x="([\d.]+)"',a); ym=re.search(r'y="([\d.]+)"',a)
        out.append((float(xm.group(1)),float(ym.group(1)),txt))
    return out
def has_cjk(t): return any('\u4e00'<=c<='\u9fff' for c in t)
for pg,fn in [(1,'p1-front'),(2,'p2-leben'),(3,'p3-kultur'),(4,'p4-sport'),(5,'p5-jugend'),(6,'p6-vertiefung'),(7,'p7-sprache'),(8,'p8-uebungen')]:
    co=[e for e in elems(G/f"files/weekly-report-w45-de-core/svg/{fn}.svg") if not has_cjk(e[2])]
    ed=[e for e in elems(G/f"files/weekly-report-w45-de-zh-tw/svg/{fn}.svg") if not has_cjk(e[2])]
    cc,ec=collections.Counter(co),collections.Counter(ed)
    print(f"P{pg} frozen (x,y,text) only-core={sum((cc-ec).values())} only-ed={sum((ec-cc).values())}")
    for t,n in list((cc-ec).items())[:8]: print("  ONLY-CORE",t)
    for t,n in list((ec-cc).items())[:8]: print("  ONLY-ED  ",t)
