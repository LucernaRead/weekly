import re, html, pathlib
G=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
def elems(p):
    s=p.read_text(encoding="utf-8")
    out=[]
    for m in re.finditer(r'<text ([^>]*)>(.*?)</text>', s, re.S):
        attrs=m.group(1); txt=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        xm=re.search(r'x="([\d.]+)"',attrs); ym=re.search(r'y="([\d.]+)"',attrs)
        out.append((float(xm.group(1)),float(ym.group(1)),txt))
    return out
for name,path in [("CORE",G/"files/weekly-report-w45-de-core/svg/p7-sprache.svg"),("ED",G/"files/weekly-report-w45-de-zh-tw/svg/p7-sprache.svg"),("DE-EN",G/"files/weekly-report-w45-de-en/svg/p7-sprache.svg")]:
    els=elems(path)
    print(f"===== {name} =====")
    for i,(x,y,t) in enumerate(els):
        if "NOCH EIN WORT" in t or "WORT" in t and "NOCH" in t:
            print("BOX HEAD at",i,x,y,repr(t))
            for j in range(max(0,i-2),min(len(els),i+30)):
                print("   ",j,els[j][0],els[j][1],repr(els[j][2][:150]))
            break
