import re
from pathlib import Path
H=Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files"
def gloss_counts(builddir):
    out={}
    for f in ["content12.py","content34.py","content56.py"]:
        txt=(builddir/f).read_text(encoding="utf-8")
        # gloss("...") calls; also f.gloss / bridge? gloss only
        for m in re.finditer(r'\.gloss\("((?:[^"\\]|\\.)*)"\)', txt):
            s=m.group(1)
            items=[x.strip() for x in s.split("·") if x.strip()]
            out.setdefault(f,[]).append((s[:60],len(items)))
    return out
for label, d in [("CORE",H/"weekly-report-w45-fr-build"),("ED-BUILD",H/"weekly-report-w45-fr-nl-build")]:
    print("==",label)
    tot=0
    for f, lst in gloss_counts(d).items():
        print(" ",f, [n for _,n in lst], "sum", sum(n for _,n in lst)); tot+=sum(n for _,n in lst)
    print("  TOTAL",tot)
# golden joint counts from delivery SVGs (joined, normalised apostrophe variants)
import xml.etree.ElementTree as ET
BASE=Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
def joined(d):
    alltxt=[]
    per={}
    for p in sorted(d.glob("*.svg")):
        t=ET.parse(p); ns=[]
        for el in t.iter():
            if el.tag.endswith('}text') or el.tag=='text':
                s=''.join(el.itertext())
                if s.strip(): ns.append(s)
        per[p.name]=' '.join(ns); alltxt.append(per[p.name])
    return per,' '.join(alltxt)
EDper,EDall=joined(BASE/"weekly-report-w45-fr-nl/svg")
COREper,COREall=joined(BASE/"weekly-report-w45-fr-core/svg")
def norm(s): return s.replace("’","'").replace("‘","'")
EDn,COREn=norm(EDall),norm(COREall)
gold=[
 ("#1","Le lundi 2 novembre, on reprend les cours.","p2-vie.svg"),
 ("#2","On ne connaît pas encore les finalistes.","p1-une.svg"),
 ("#3","Les cimetières se sont remplis de chrysanthèmes.","p3-culture.svg"),
 ("#4","Une finale qu'on ne connaît pas d'avance : plus excitante ou plus frustrante ?","p4-sport.svg"),
 ("#5","Le festival se promène dans Paris.","p5-jeunesse.svg"),
 ("#6","Ce calendrier peut encore bouger.","p6-politique.svg"),
 ("#7","Ce week-end, tout se joue.","p1-une.svg"),
 ("#8","Les jeunes créateurs y rencontrent leur public, en vrai.","p5-jeunesse.svg"),
]
# Note: P7 table uses '?' spacing variants: joined text may have "? »" etc; count with flexible whitespace/punct
for num,sent,src in gold:
    # flexible: collapse spaces, allow space before ? 
    pat=re.escape(norm(sent)).replace(r"\ ","\\s+")
    ed=len(re.findall(pat, EDn)); co=len(re.findall(pat, COREn))
    # source page hit: sentence words in source page joined (allow wrap)
    srcED=norm(EDper[src]); srcCORE=norm(COREper[src])
    # check first 30 chars fragment presence after normalising whitespace
    frag=re.sub(r"\s+"," ",norm(sent))[:40]
    def has(page,frag):
        pg=re.sub(r"\s+"," ",page)
        return frag in pg or frag.replace(" ?","?") in pg or frag.replace(" :"," :") in pg
    print(f"GOLD {num} ED_joint={ed} CORE_joint={co} src={src} srcED_frag={has(srcED,frag)} srcCORE_frag={has(srcCORE,frag)} sent={sent[:50]}")
    # also per-page counts
    for pn,txt in EDper.items():
        c=len(re.findall(pat, norm(txt)))
        if c: print(f"    ED {pn}: {c}")
