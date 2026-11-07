import os, re, glob
import xml.etree.ElementTree as ET
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
NS="{http://www.w3.org/2000/svg}"
SYL=re.compile(r"[\uac00-\ud7a3]")
ORPHAN_START=set(".,;:!?%)]}、。·…~–—")
def load(fn):
    els=[]
    for t in ET.parse(fn).getroot().iter(NS+"text"):
        txt="".join(t.itertext())
        els.append({"x":float(t.get("x")),"y":float(t.get("y")),"size":float(t.get("font-size","20")),"w":t.get("font-weight","") or "","text":txt})
    return els
for code in ["ko"]:
    print("=====",code,"independent orphan scan (window 10-45, >=3-syllable tail) =====")
    flags=[]
    for fn in sorted(glob.glob(BASE+f"/files/weekly-report-w46-es-{code}/svg/*.svg")):
        els=load(fn)
        # group by (x,size) preserving document order, then sort each group by y
        from collections import defaultdict
        groups=defaultdict(list)
        for e in els: groups[(round(e["x"],1),e["size"])].append(e)
        for key, g in groups.items():
            g=sorted(g,key=lambda e:e["y"])
            for a,b in zip(g,g[1:]):
                dy=b["y"]-a["y"]
                if not (10<=dy<=45): continue
                bt=b["text"].strip(); at=a["text"].rstrip()
                if not bt or not at: continue
                if not SYL.search(bt): continue
                # S1: continuation starts with orphan punctuation
                if bt[0] in ORPHAN_START:
                    flags.append((os.path.basename(fn),"S1-PUNCT",a["y"],b["y"],at[-40:],bt[:60])); continue
                # tail criterion: prev ends with Hangul (no trailing space/punct), continuation starts with Hangul
                if SYL.search(at[-1]) and SYL.search(bt[0]):
                    # first token of continuation (up to space or punctuation)
                    m=re.match(r"^[\uac00-\ud7a3]+", bt)
                    if m:
                        tail=m.group(0)
                        # only flag if prev line's last token also Hangul-continuation (i.e., combined word): prev last token
                        prevtok=re.search(r"[\uac00-\ud7a3]+$", at)
                        if prevtok and len(SYL.findall(tail))>=3:
                            # exclude cases where tail is a standalone word that happens to follow a Hangul-ending line with a space in source? 
                            # Source lines have no trailing spaces in SVG text; a wrap break inside a word shows as prev ending mid-word.
                            # Heuristic: flag only if prev line does NOT end with a particle boundary? Can't know. Flag all >=3 for adjudication.
                            flags.append((os.path.basename(fn),"TAIL>=3",a["y"],b["y"],at[-40:],bt[:60]))
    print("flags:", len(flags))
    for f in flags: print(" ", f)
