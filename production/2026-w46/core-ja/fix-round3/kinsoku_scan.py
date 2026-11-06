# Standalone read-only scan replicating hidden_files/w46/check_edition.py
# orphan/kinsoku definitions (window 10-45, >=3-syllable tails, paren frags,
# line-start orphan punctuation) + svglib NO_START/NO_END sets.
import glob, os, re, sys, json
from xml.etree import ElementTree as ET
NS="{http://www.w3.org/2000/svg}"
NO_START=set("。、，．！？：；）」』】ー…‥・") | set("］｝〉》％") | set(")]}.,!?%:;\"")
NO_END=set("（「『〔【《〈([")
def page_texts(svg):
    root=ET.parse(svg).getroot()
    return [(float(t.get("x")), float(t.get("y")), "".join(t.itertext())) for t in root.iter(NS+"text")]
def scan(svgdir):
    svgs=sorted(glob.glob(os.path.join(svgdir,"*.svg")))
    kin=[]; kinend=[]; orph=[]
    ORPHAN_START=set(")]}〉》.,!?%:;」』】")
    hangul=lambda ch: 0xAC00<=ord(ch)<=0xD7A3
    def syll(s): return sum(1 for ch in s if hangul(ch))
    for pi,fn in enumerate(svgs,1):
        texts=page_texts(fn)
        for x,y,s in texts:
            st=s.strip()
            if st and st[0] in NO_START: kin.append((pi,round(y,1),st[:50]))
            if st and st[-1] in NO_END: kinend.append((pi,round(y,1),st[-50:]))
        # orphan runs (sorted by y,x as in check_edition.py)
        ts=sorted(texts,key=lambda t:(t[1],t[0])); runs=[]
        for x,y,s in ts:
            if runs and abs(x-runs[-1][-1][0])<3 and 10<=y-runs[-1][-1][1]<=45 and len(runs[-1])<30:
                runs[-1].append((x,y,s))
            else: runs.append([(x,y,s)])
        for run in runs:
            if len(run)<2: continue
            last=run[-1][2].strip()
            if last.endswith(")") or last.endswith("」") or last.startswith("("):
                seg=last.split()[-1] if last.split() else last
                if syll(seg)>=3: orph.append((pi,"PAREN-FRAG",round(run[-1][1],1),last[:60]))
            first=run[1][2].strip()
            if first and first[0] in ORPHAN_START: orph.append((pi,"START-PUNCT",round(run[1][1],1),first[:60]))
            prev=run[-2][2].strip()
            if len(last)<=6 and syll(last)>=3 and len(prev)>=14:
                if last.endswith(("요.","요","예요.","예요","어요.","어요")) or ")" in last:
                    orph.append((pi,"SHORT-TAIL",round(run[-1][1],1),last[:60]))
    return {"kinsoku_start":kin,"kinsoku_end":kinend,"orphan":orph}
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
dirs={"zh-cn":"weekly-report-w46-ja-core","de":"weekly-report-w46-ja-de","en":"weekly-report-w46-ja-en","es":"weekly-report-w46-ja-es","fr":"weekly-report-w46-ja-fr","it":"weekly-report-w46-ja-it","ko":"weekly-report-w46-ja-ko","nl":"weekly-report-w46-ja-nl","pt":"weekly-report-w46-ja-pt","ru":"weekly-report-w46-ja-ru","zh-tw":"weekly-report-w46-ja-zh-tw"}
out={}
for code,d in dirs.items():
    r=scan(os.path.join(BASE,d,"svg")); out[code]=r
    print(code,"kinsoku_start",len(r["kinsoku_start"]),"kinsoku_end",len(r["kinsoku_end"]),"orphan",len(r["orphan"]))
    for k in r["kinsoku_start"][:8]: print("  KS:",k)
    for k in r["kinsoku_end"][:8]: print("  KE:",k)
    for k in r["orphan"][:8]: print("  OR:",k)
json.dump(out,open(sys.argv[1],"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("wrote", sys.argv[1])
