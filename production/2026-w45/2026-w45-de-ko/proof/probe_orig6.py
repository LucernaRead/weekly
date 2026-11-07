import re
def rows(path):
    s=open(path,encoding='utf-8').read(); out=[]
    for m in re.finditer(r'<text[^>]*>',s):
        tag=m.group(0); xm=re.search(r'x="([\d.]+)"',tag); ym=re.search(r'y="([\d.]+)"',tag); fm=re.search(r'font-size="([\d.]+)"',tag)
        end=s.find('</text>',m.end())
        if end<0 or not xm or not ym: continue
        out.append((float(xm.group(1)),float(ym.group(1)),float(fm.group(1)) if fm else 0,re.sub(r'<[^>]+>','',s[m.end():end])))
    return out
for label,path in [('CURRENT','files/weekly-report-w45-de-ko/svg/p8-uebungen.svg')]:
    r=[x for x in rows(path) if x[2]==13.0]
    for col in (65,527,989):
        g=sorted([x for x in r if x[0]==col],key=lambda z:z[1])
        print(f"--- col x={col} ({len(g)} lines) ---")
        for x,y,fs,t in g:
            print(f"  y={y:.2f} {t!r}")
