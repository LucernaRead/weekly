import re, html, pathlib
G=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
def elems(p):
    s=p.read_text(encoding="utf-8"); out=[]
    for m in re.finditer(r'<text ([^>]*)>(.*?)</text>', s, re.S):
        attrs=m.group(1); txt=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        xm=re.search(r'x="([\d.]+)"',attrs); ym=re.search(r'y="([\d.]+)"',attrs)
        out.append((float(xm.group(1)),float(ym.group(1)),txt))
    return out
for name,path in [("CORE",G/"files/weekly-report-w45-de-core/svg/p7-sprache.svg"),("ED",G/"files/weekly-report-w45-de-zh-tw/svg/p7-sprache.svg")]:
    els=elems(path)
    print(f"===== {name} P7 from idx 142 =====")
    for j in range(142,len(els)):
        print(j,els[j][0],els[j][1],repr(els[j][2][:160]))
    print(f"===== {name} LESERBRIEFE region =====")
    for j,(x,y,t) in enumerate(els):
        if "LESER" in t or "Beispiel der Redaktion" in t or "Redaktionsschluss" in t:
            print("anchor",j,x,y,repr(t))
            for k in range(max(0,j-3),min(len(els),j+25)):
                print("  ",k,els[k][0],els[k][1],repr(els[k][2][:160]))
            break
