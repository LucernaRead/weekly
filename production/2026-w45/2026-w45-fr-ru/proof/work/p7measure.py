import re, sys, os, html
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "repro"))
import svglib
TRE = re.compile(r'<text\b([^>]*)>([^<]*)</text>')
def attr(a,k):
    m=re.search(k+r'="([^"]*)"',a); return m.group(1) if m else None
def meas(t,kind,bold,size):
    f=svglib._font(kind,bold,int(round(size*4))); bb=f.getbbox(t); return bb[3]/4.0
for label,path in [("ED",os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-fr-ru/svg/p7-langue.svg"))]:
    src=open(path,encoding="utf-8").read()
    for m in TRE.finditer(src):
        a,t=m.group(1),html.unescape(m.group(2))
        if any(k in t for k in ["Примечание редакции: настоящих","поступило (W44","На следующей неделе:","LA SEMAINE PROCHAINE","Комментарий редакции","Присылайте письма"]):
            x,y=float(attr(a,"x")),float(attr(a,"y")); fam=attr(a,"font-family"); size=float(attr(a,"font-size")); bold=attr(a,"font-weight")=="700"
            kind="serif" if "Serif" in (fam or "") else "sans"
            print(f"y={y} ink_bottom={y+meas(t,kind,bold,size):.1f} size={size} :: {t!r}")
    # rects: readers box x=989 w=896 bottom 2258; also find rect containing y 1878..2258
    for m in re.finditer(r'<rect\b([^>]*)/?>',src):
        a=m.group(1)
        if attr(a,"fill") in (None,"none"): continue
        x,y,w,h=float(attr(a,"x") or 0),float(attr(a,"y") or 0),float(attr(a,"width") or 0),float(attr(a,"height") or 0)
        if y+h==2258.0: print(f"BOX rect x={x} y={y} w={w} h={h} bottom={y+h}")
