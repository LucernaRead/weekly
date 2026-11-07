import sys, pathlib
sys.path.insert(0, str(pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as OA
from PIL import Image
import xml.etree.ElementTree as ET
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-de"
NS="{http://www.w3.org/2000/svg}"
t=ET.parse(BASE/"svg"/"p1-portada.svg")
for el in t.iter(NS+"text"):
    txt=el.text or ""
    if txt.strip() in ("La Lucerna",) and float(el.get("y"))<300:
        box=OA.ink_box(txt, el.get("font-family",""), float(el.get("font-size")), False, float(el.get("x")), float(el.get("y")), el.get("text-anchor","start"))
        print("wordmark ink box:", [round(v,1) for v in box], repr(txt))
    if float(el.get("y"))<170:
        print("top-band text:", el.get("x"), el.get("y"), el.get("font-size"), repr(txt))
# pixel checks on P1 card
im=Image.open(BASE/"cards"/"p1-portada.png").convert("RGB")
print("card size:", im.size)
px=im.load()
# background cream sampled at (100,300)
bg=px[100,300]
print("bg sample:", bg)
def is_ink(p):
    # ink = far from cream bg in any channel
    return abs(p[0]-bg[0])>30 or abs(p[1]-bg[1])>30 or abs(p[2]-bg[2])>30
# outer 26px border scan (excluding frame rects at 28/40 which are intentional): report ink pixels with x<26 or y<26 or x>=1924 or y>=2674
bad=[]
for y in range(0,26):
    for x in range(im.size[0]):
        if is_ink(px[x,y]): bad.append((x,y))
for y in range(im.size[1]-26, im.size[1]):
    for x in range(im.size[0]):
        if is_ink(px[x,y]): bad.append((x,y))
for x in list(range(0,26))+list(range(im.size[0]-26, im.size[0])):
    for y in range(im.size[1]):
        if is_ink(px[x,y]): bad.append((x,y))
print("outer-26px ink pixels:", len(bad), bad[:10])
# wordmark pixel bbox in band y 150..300, dark ink only (near-black)
xs=[]; ys=[]
for y in range(150,300):
    for x in range(im.size[0]):
        p=px[x,y]
        if p[0]<80 and p[1]<80 and p[2]<80:
            xs.append(x); ys.append(y)
print("wordmark dark-ink pixel bbox: x", min(xs), "..", max(xs), " y", min(ys), "..", max(ys), " clearance L:", min(xs)-65, "R:", 1885-max(xs))
# top strip: band y 52..150 is dark; find gold-ish text columns: pixels with high R, mid G, low B inside band, excluding band edges
cols=set()
for y in range(56,146):
    for x in range(im.size[0]):
        p=px[x,y]
        if p[0]>140 and 100<p[1]<190 and p[2]<140:
            cols.add(x)
if cols:
    # clusters
    cs=sorted(cols); clusters=[]; s=cs[0]; prev=cs[0]
    for c in cs[1:]:
        if c-prev>10: clusters.append((s,prev)); s=c
        prev=c
    clusters.append((s,prev))
    print("top-strip gold-ink clusters:", clusters)
    if len(clusters)>=2:
        print("gaps between clusters:", [clusters[i+1][0]-clusters[i][1] for i in range(len(clusters)-1)])
