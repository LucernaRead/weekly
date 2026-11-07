import re, html, pathlib, collections, json
G=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
def elems(p):
    s=p.read_text(encoding="utf-8")
    out=[]
    for m in re.finditer(r'<text ([^>]*)>(.*?)</text>', s, re.S):
        txt=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        out.append(txt)
    return out
def has_cjk(t): return any('\u4e00'<=c<='\u9fff' for c in t)
for pg in range(1,9):
    fn={1:'p1-front',2:'p2-leben',3:'p3-kultur',4:'p4-sport',5:'p5-jugend',6:'p6-vertiefung',7:'p7-sprache',8:'p8-uebungen'}[pg]
    co=elems(G/f"files/weekly-report-w45-de-core/svg/{fn}.svg")
    ed=elems(G/f"files/weekly-report-w45-de-zh-tw/svg/{fn}.svg")
    cc=collections.Counter(t for t in co if not has_cjk(t))
    ec=collections.Counter(t for t in ed if not has_cjk(t))
    print(f"--- P{pg} pure-nonCJK elements core={sum(cc.values())} ed={sum(ec.values())} only-core={sum((cc-ec).values())} only-ed={sum((ec-cc).values())}")
    for t,n in (cc-ec).items(): print("  ONLY-CORE x",n,repr(t[:130]))
    for t,n in (ec-cc).items(): print("  ONLY-ED   x",n,repr(t[:130]))
