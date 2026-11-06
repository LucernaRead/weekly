from PIL import Image
import pathlib
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-de"
im=Image.open(BASE/"cards"/"p1-portada.png").convert("RGB")
px=im.load()
bg=(247,241,226)
def is_ink(p):
    return abs(p[0]-bg[0])>40 or abs(p[1]-bg[1])>40 or abs(p[2]-bg[2])>40
bad=[]
W,H=im.size
for y in range(0,26):
    for x in range(W):
        if is_ink(px[x,y]): bad.append((x,y))
for y in range(H-26,H):
    for x in range(W):
        if is_ink(px[x,y]): bad.append((x,y))
for x in list(range(0,26))+list(range(W-26,W)):
    for y in range(H):
        if is_ink(px[x,y]): bad.append((x,y))
print("outer-26px non-cream pixels:", len(bad), bad[:10])
# wordmark: band y 155..275, x 500..1450, dark ink (near-black #28251d-ish)
xs=[]; ys=[]
for y in range(155,275):
    for x in range(500,1450):
        p=px[x,y]
        if p[0]<90 and p[1]<90 and p[2]<90:
            xs.append(x); ys.append(y)
print("wordmark dark-ink bbox: x", min(xs),"..",max(xs)," y",min(ys),"..",max(ys),"| clearance inside content area 65..1885: L",min(xs)-65,"R",1885-max(xs))
# top strip gaps via SVG ink boxes (already have wordmark); compute strip text ink boxes
import sys
sys.path.insert(0, str(pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA, xml.etree.ElementTree as ET
NS="{http://www.w3.org/2000/svg}"
t=ET.parse(BASE/"svg"/"p1-portada.svg")
for el in t.iter(NS+"text"):
    if float(el.get("y"))==92:
        box=OA.ink_box(el.text or "", el.get("font-family",""), float(el.get("font-size")), False, float(el.get("x")), float(el.get("y")), el.get("text-anchor","start"))
        print("strip:", repr(el.text), "ink x", round(box[0],1),"..",round(box[2],1))
# badge/tagline clearance: tagline y=372 vs badge y=574 vs wordmark bottom 267
for el in t.iter(NS+"text"):
    if el.get("y") in ("372","574"):
        box=OA.ink_box(el.text or "", el.get("font-family",""), float(el.get("font-size")), el.get("font-weight") in ("700","bold"), float(el.get("x")), float(el.get("y")), el.get("text-anchor","start"))
        print("y="+el.get("y"), repr(el.text)[:60], "ink y", round(box[1],1),"..",round(box[3],1), "ink x", round(box[0],1),"..",round(box[2],1))
