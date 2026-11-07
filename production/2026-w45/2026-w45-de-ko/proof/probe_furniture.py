import re
def rows(path):
    s=open(path,encoding='utf-8').read(); out=[]
    for m in re.finditer(r'<text[^>]*>',s):
        tag=m.group(0); xm=re.search(r'x="([\d.]+)"',tag); ym=re.search(r'y="([\d.]+)"',tag); fm=re.search(r'font-size="([\d.]+)"',tag); anch=re.search(r'text-anchor="([^"]+)"',tag)
        end=s.find('</text>',m.end())
        if end<0 or not xm or not ym: continue
        out.append((float(xm.group(1)),float(ym.group(1)),float(fm.group(1)) if fm else 0,anch.group(1) if anch else '',re.sub(r'<[^>]+>','',s[m.end():end])))
    return out
for label,path in [('W43','files/weekly-report-de-ko/svg/p1-front.svg'),('W45KO','files/weekly-report-w45-de-ko/svg/p1-front.svg'),('W45CORE','files/weekly-report-w45-de-core/svg/p1-front.svg')]:
    r=rows(path); print('=====',label)
    for y in (92,262,330,372,478,522):
        for x,yy,fs,a,t in sorted(r):
            if abs(yy-y)<1: print(f"  y={yy} x={x} fs={fs} anch={a} {t!r}")
    # badge slots
    slot=[t for x,yy,fs,a,t in r if 380<=yy<=420 or 560<=yy<=600]
    print('  badge-slot rows (380-420,560-600):',slot)
