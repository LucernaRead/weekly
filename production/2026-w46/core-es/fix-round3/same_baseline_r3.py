import sys, os, re, glob, html
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools"))
import occlusion_audit as oa
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def parse(fn):
    s=open(fn,encoding="utf-8").read()
    out=[]
    for m in re.finditer(r'<text x="([\d.]+)" y="([\d.]+)" font-family="([^"]+)" font-size="([\d.]+)"([^>]*)>(.*?)</text>', s, re.S):
        attrs=m.group(5)
        bold='700' in attrs
        anchor=re.search(r'text-anchor="([^"]+)"', attrs)
        out.append({"x":float(m.group(1)),"y":float(m.group(2)),"fam":m.group(3),"size":float(m.group(4)),"bold":bold,"anchor":anchor.group(1) if anchor else "start","text":html.unescape(re.sub(r"<[^>]+>","",m.group(6)))})
    return out
for code in ["de"]:
    print(f"===== es-{code} same-baseline: gaps < 2px or overlap (ink boxes, exact-y groups) =====")
    nrep=0
    for fn in sorted(glob.glob(BASE+f"/files/weekly-report-w46-es-{code}/svg/*.svg")):
        els=parse(fn)
        from collections import defaultdict
        groups=defaultdict(list)
        for e in els: groups[round(e["y"],2)].append(e)
        for y,g in groups.items():
            if len(g)<2: continue
            boxes=[]
            for e in g:
                try: box=oa.ink_box(e["text"],e["fam"],e["size"],e["bold"],e["x"],e["y"],anchor=e["anchor"])
                except Exception as ex: continue
                boxes.append((box[0],box[2],e))
            boxes.sort()
            for (l1,r1,e1),(l2,r2,e2) in zip(boxes,boxes[1:]):
                gap=l2-r1
                if gap<2.0:
                    nrep+=1
                    print(f"  {os.path.basename(fn)} y={y} gap={gap:.1f} :: [{e1['text'][:50]}] || [{e2['text'][:50]}]")
    print(f"  reports: {nrep}")
