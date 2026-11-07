import sys, os, re
sys.path.insert(0, '/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ja-it-build')
from svglib import _font
ED='/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ja-it'
TEXT_RE = re.compile(r'<text x="([^"]+)" y="([^"]+)" font-family="([^"]+)" font-size="([^"]+)"([^>]*)>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([^"]+)" y="([^"]+)" width="([^"]+)" height="([^"]+)"[^>]*>')
LINE_RE = re.compile(r'<line x1="([^"]+)" y1="([^"]+)" x2="([^"]+)" y2="([^"]+)"[^>]*stroke-width="([^"]+)"')
def fam_kind(fam): return "serif" if "Serif" in fam else "sans"
def texts_of(path):
    s=open(path,encoding='utf-8').read(); out=[]
    for m in TEXT_RE.finditer(s):
        x,y,fam,size,rest,t=float(m.group(1)),float(m.group(2)),m.group(3),float(m.group(4)),m.group(5),m.group(6)
        anchor="middle" if 'text-anchor="middle"' in rest else ("end" if 'text-anchor="end"' in rest else "start")
        bold='font-weight="700"' in rest
        out.append({"x":x,"y":y,"size":size,"kind":fam_kind(fam),"bold":bold,"anchor":anchor,"t":t})
    return out
def ink_box(el):
    f=_font(el["kind"],el["bold"],el["size"])
    try: bb=f.getbbox(el["t"],anchor="ls")
    except Exception: bb=f.getbbox(el["t"])
    w=bb[2]-bb[0]
    x0=el["x"]-w/2-bb[0] if el["anchor"]=="middle" else el["x"]-w-bb[0] if el["anchor"]=="end" else el["x"]-bb[0]
    return (x0, el["y"]+bb[1], x0+w, el["y"]+bb[3])
def adv_right(el):
    f=_font(el["kind"],el["bold"],el["size"]); w=f.getlength(el["t"])
    return el["x"]+w/2 if el["anchor"]=="middle" else el["x"] if el["anchor"]=="end" else el["x"]+w
PAGES=["p1-hyoushi","p2-kurashi","p3-bunka","p4-supotsu","p5-wakamono","p6-fukayomi","p7-kotoba","p8-tesuto"]
viol=[]
for pg in PAGES:
    for el in texts_of(f'{ED}/svg/{pg}.svg'):
        r=adv_right(el)
        if r>1885.5: viol.append((pg,round(r,1),el["t"][:50]))
print('ADVANCE violations:', len(viol), viol[:10])
for pg in PAGES:
    for el in texts_of(f'{ED}/svg/{pg}.svg'):
        if 'Abbina' in el["t"]: print('P2 Abbina advance end:', round(adv_right(el),2), repr(el["t"]))
# frame scan
hits=[]
for pg in PAGES:
    path=f'{ED}/svg/{pg}.svg'; s=open(path,encoding='utf-8').read()
    rects=[(float(a),float(b),float(c),float(d)) for a,b,c,d in RECT_RE.findall(s)]
    lines=[(float(a),float(b),float(c),float(d),float(e)) for a,b,c,d,e in LINE_RE.findall(s)]
    for el in texts_of(path):
        x0,y0,x1,y1=ink_box(el)
        for rx,ry,rw,rh in rects:
            for bx in (rx,rx+rw):
                if x0<bx<x1 and y0<ry+rh and y1>ry: hits.append((pg,'rect-v',round(bx,1),el["t"][:30]))
            for by in (ry,ry+rh):
                if y0<by<y1 and x0<rx+rw and x1>rx: hits.append((pg,'rect-h',round(by,1),el["t"][:30]))
        for x1l,y1l,x2l,y2l,sw in lines:
            if y1l==y2l and y0-sw/2<y1l<y1+sw/2 and x0<max(x1l,x2l) and x1>min(x1l,x2l): hits.append((pg,'line-h',round(y1l,1),el["t"][:30]))
            if x1l==x2l and x0-sw/2<x1l<x1+sw/2 and y0<max(y1l,y2l) and y1>min(y1l,y2l): hits.append((pg,'line-v',round(x1l,1),el["t"][:30]))
print('FRAME hits:', len(hits), hits[:10])
# P6 chart coverage (baseline-anchored, later-drawn rects only)
p6=open(f'{ED}/svg/p6-fukayomi.svg',encoding='utf-8').read()
texts6=texts_of(f'{ED}/svg/p6-fukayomi.svg')
cats=["満足","温泉","紅葉","グルメ"]
labels=[el for el in texts6 if any(c in el["t"] for c in cats) or "%" in el["t"]]
rect_list=[(m.start(),float(m.group(1)),float(m.group(2)),float(m.group(3)),float(m.group(4))) for m in RECT_RE.finditer(p6)]
maxcov=0.0
for el in labels:
    x0,y0,x1,y1=ink_box(el); area=max(0.0,(x1-x0)*(y1-y0))
    if area==0: continue
    pos=p6.find(">"+el["t"]+"<"); ov=0.0
    for rp,rx,ry,rw,rh in rect_list:
        if rp>pos:
            ov+=max(0.0,min(x1,rx+rw)-max(x0,rx))*max(0.0,min(y1,ry+rh)-max(y0,ry))
    cov=ov/area; maxcov=max(maxcov,cov)
    if cov>0: print('P6 label coverage>0:', repr(el["t"][:30]), round(cov,4))
print('P6 max coverage:', round(maxcov,4), 'labels:', len(labels))
# kinsoku
NO_START=set("。、，．！？：；）」』】ー…‥・")
ks=[]
for pg in PAGES:
    for el in texts_of(f'{ED}/svg/{pg}.svg'):
        if el["t"] and el["t"][0] in NO_START: ks.append((pg,el["t"][:20]))
print('KINSOKU hits:', len(ks), ks[:10])
