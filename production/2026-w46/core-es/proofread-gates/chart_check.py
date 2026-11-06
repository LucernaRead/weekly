import re, os, hashlib
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def shapes(fn):
    s=open(fn,encoding="utf-8").read()
    # all non-text elements: rect/line/circle/path/polygon/image
    els=re.findall(r"<(rect|line|circle|path|polygon|polyline|image)\b[^>]*>", s)
    attrs=[]
    for m in re.finditer(r"<(rect|line|circle|path|polygon|polyline|image)\b([^>]*)>", s):
        a=re.sub(r"\s+"," ",m.group(2)).strip()
        # drop image href data (huge) -> keep geometry attrs only for image
        if m.group(1)=="image":
            a=" ".join(p for p in a.split(" ") if p.startswith(("x=","y=","width=","height=")))
        attrs.append(m.group(1)+" "+a)
    return attrs
core=shapes(BASE+"/files/weekly-report-w46-es-core/svg/p6-afondo.svg")
print("core P6 shapes:", len(core))
for code in ["de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    ed=shapes(BASE+f"/files/weekly-report-w46-es-{code}/svg/p6-afondo.svg")
    print(code, "shapes:", len(ed), "identical-to-core:", ed==core, "diff-count:", sum(1 for a,b in zip(ed,core) if a!=b), "len-diff:", len(ed)-len(core))
    if ed!=core:
        for i,(a,b) in enumerate(zip(ed,core)):
            if a!=b: print("   first diff at",i,"\n    core:",b[:160],"\n    ed:  ",a[:160]); break
print("\n===== P6 chart labels vs bars (text ink vs later rects) =====")
# Find chart area: bars are rects with fill != background in P6; labels are text elements left of bars.
# Use occlusion-style approach via PIL measurement is heavy; instead compare label text elements' x/y vs bar rect x in core (gated) + verify label strings identical core vs edition (freeze already: P6 label fragments re-wrapped only in 7 editions).
# Here: list bar rects (width>50, height 18-40, y 300-1200) in core P6
s=open(BASE+"/files/weekly-report-w46-es-core/svg/p6-afondo.svg",encoding="utf-8").read()
for m in re.finditer(r'<rect x="([\d.]+)" y="([\d.]+)" width="([\d.]+)" height="([\d.]+)"[^>]*fill="([^"]*)"', s):
    x,y,w,h,f=m.groups()
    if float(w)>40 and 200<float(y)<1400:
        print(f" rect x={x} y={y} w={w} h={h} fill={f}")
