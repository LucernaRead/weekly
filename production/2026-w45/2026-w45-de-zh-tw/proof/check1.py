import re, html, pathlib, json, collections
G=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
ED=G/"files/weekly-report-w45-de-zh-tw/svg"; CO=G/"files/weekly-report-w45-de-core/svg"; W43=G/"files/weekly-report-de-zh-tw/svg"
def elems(p):
    s=p.read_text(encoding="utf-8")
    out=[]
    for m in re.finditer(r'<text ([^>]*)>(.*?)</text>', s, re.S):
        attrs, raw = m.group(1), m.group(2)
        txt=html.unescape(re.sub(r'<[^>]+>','',raw))
        xm=re.search(r'x="([\d.]+)"',attrs); ym=re.search(r'y="([\d.]+)"',attrs)
        fm=re.search(r'font-family="([^"]+)"',attrs); sm=re.search(r'font-size="([\d.]+)"',attrs)
        wm=re.search(r'font-weight="([^"]+)"',attrs); fm2=re.search(r'fill="([^"]+)"',attrs); am=re.search(r'text-anchor="([^"]+)"',attrs)
        out.append(dict(x=float(xm.group(1)) if xm else None,y=float(ym.group(1)) if ym else None,fam=fm.group(1) if fm else None,size=float(sm.group(1)) if sm else None,weight=wm.group(1) if wm else None,fill=fm2.group(1) if fm2 else None,anchor=am.group(1) if am else "start",text=txt,raw=attrs))
    return out
def alltext(d):
    return {f.name:" ".join(e["text"] for e in elems(f)) for f in sorted(d.glob("*.svg"))}
ed={f.name:elems(f) for f in sorted(ED.glob("*.svg"))}; co={f.name:elems(f) for f in sorted(CO.glob("*.svg"))}
# 1 forbidden term + simplified prefix
for name,d in [("ED",ed),("CO",co)]:
    full=" ".join(e["text"] for v in d.values() for e in v)
    print(name,"桥接 count:",full.count("桥接"),"译注 Simplified-prefix 译注｜ count ED only:",full.count("译注"))
    print(name,"ASCII double-quote count:",full.count('"'))
# freeze diff non-CJK removed/added per page from freeze-diff.json
fd=json.loads(pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/de-zh-tw-proof/freeze-diff.json").read_text())
print(json.dumps(fd,ensure_ascii=False)[:3000])
