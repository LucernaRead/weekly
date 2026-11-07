import re, html, pathlib
from PIL import ImageFont
G=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
SANS="/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc"; SANSB="/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc"
SERIF="/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc"; SERIFB="/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc"
BLACK="/home/hatch/.local/share/fonts/UnifrakturMaguntia.ttf"
def font(fam,size,bold,tc):
    idx=3 if tc else 2
    if "blackletter" in fam.lower() or fam=="UnifrakturMaguntia": return ImageFont.truetype(BLACK,int(round(size)))
    if "Serif" in fam: path=SERIFB if bold else SERIF
    else: path=SANSB if bold else SANS
    try: return ImageFont.truetype(path,int(round(size)),index=idx)
    except Exception: return ImageFont.truetype(path,int(round(size)))
def parse(p):
    s=p.read_text(encoding="utf-8"); els=[]
    for m in re.finditer(r'<text ([^>]*)>(.*?)</text>', s, re.S):
        a=m.group(1); txt=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
        def g(pat,default=None):
            mm=re.search(pat,a); return mm.group(1) if mm else default
        x=float(g(r'x="([\d.]+)"')); y=float(g(r'y="([\d.]+)"')); fam=g(r'font-family="([^"]+)"'); size=float(g(r'font-size="([\d.]+)"'))
        bold='font-weight="700"' in a; anchor=g(r'text-anchor="([^"]+)"',"start")
        tc="TC" in (fam or "")
        try:
            f=font(fam or "",size,bold,tc); l,t,r,b=f.getbbox(txt)
        except Exception as e:
            continue
        w=r-l; x0=x-w if anchor=="end" else (x-w/2 if anchor=="middle" else x)
        els.append(dict(txt=txt,x0=x0+l,y0=y+t,x1=x0+r,y1=y+b,y=y,x=x))
    rects=[]
    for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', s):
        rects.append(tuple(float(v) for v in m.groups()))
    # keep draw order: need combined order of texts vs rects - redo with positions in file
    return els, rects, s
# 1) same-baseline collisions
for name,d in [("CORE",G/"files/weekly-report-w45-de-core/svg"),("ED",G/"files/weekly-report-w45-de-zh-tw/svg")]:
    tot=0; details=[]
    for f in sorted(d.glob("*.svg")):
        els,_,_=parse(f); by={}
        for e in els: by.setdefault(round(e["y"]),[]).append(e)
        for y,bs in by.items():
            bs.sort(key=lambda e:e["x0"])
            for a,b in zip(bs,bs[1:]):
                if a["x1"]>b["x0"]+0.5: tot+=1; details.append((f.name,y,a["txt"][:40],b["txt"][:40],round(a["x1"]-b["x0"],1)))
    print(name,"same-baseline collisions:",tot, details[:10])
# 2) P6 chart: labels vs later-drawn rects (draw order)
for name,d in [("ED",G/"files/weekly-report-w45-de-zh-tw/svg"),("CORE",G/"files/weekly-report-w45-de-core/svg")]:
    s=(d/"p6-vertiefung.svg").read_text(encoding="utf-8")
    tokens=list(re.finditer(r'<(text|rect)[^>]*>.*?(?:</text>)?', s, re.S))
    # simpler: iterate all elements in order
    items=[]
    for m in re.finditer(r'<text ([^>]*)>(.*?)</text>|<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"', s, re.S):
        if m.group(1) is not None:
            a=m.group(1); txt=html.unescape(re.sub(r'<[^>]+>','',m.group(2)))
            xm=re.search(r'x="([\d.]+)"',a); ym=re.search(r'y="([\d.]+)"',a); fm=re.search(r'font-family="([^"]+)"',a); sm=re.search(r'font-size="([\d.]+)"',a)
            x=float(xm.group(1)); y=float(ym.group(1)); size=float(sm.group(1)); bold='font-weight="700"' in a; anchor=re.search(r'text-anchor="([^"]+)"',a)
            anchor=anchor.group(1) if anchor else "start"; fam=fm.group(1)
            try:
                fnt=font(fam,size,bold,"TC" in fam); l,t,r,b=fnt.getbbox(txt)
            except Exception: continue
            w=r-l; x0=x-w if anchor=="end" else (x-w/2 if anchor=="middle" else x)
            items.append(("text",txt,x0+l,y+t,x0+r,y+b))
        else:
            x,y,w,h=(float(v) for v in m.groups()[2:]); items.append(("rect",None,x,y,x+w,y+h))
    print("==",name,"P6 order items:",len(items))
    for label in ["家屬護理","專業到府","住養老院"] if name=="ED" else ["家属居家护理","专业上门","住养老院"]:
        idx=[i for i,it in enumerate(items) if it[0]=="text" and it[1]==label]
        print(" label",label,"idx",idx, [(round(items[i][2],1),round(items[i][4],1)) for i in idx])
        for i in idx:
            _,_,x0,y0,x1,y1=items[i]
            hits=[(j,items[j]) for j in range(i+1,len(items)) if items[j][0]=="rect" and not (items[j][4]<x0 or items[j][2]>x1 or items[j][5]<y0 or items[j][3]>y1)]
            print("   later-rect overlaps:",len(hits), hits[:3])
            bars=[items[j] for j in range(i+1,len(items)) if items[j][0]=="rect"]
            # nearest bar x to the right on similar y band
            near=[b for b in bars if abs(b[3]-y0)<40]
            print("   bars near band:",[(round(b[2],1),round(b[3],1)) for b in near[:5]], "clearance to nearest bar x:", (min([b[2] for b in near])-x1) if near else None)
    # ÜBUNGSDATEN line
    for it in items:
        if it[0]=="text" and "BUNGSDATEN" in (it[1] or ""):
            print("  ÜBUNGSDATEN:",it[1][:80],"ink width:",round(it[4]-it[2],1),"x0",round(it[2],1),"x1",round(it[4],1))
    # chart rect multiset compare ED vs CORE done separately below
