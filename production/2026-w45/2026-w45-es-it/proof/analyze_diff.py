import json, re, unicodedata
from xml.etree import ElementTree as ET
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
d=json.load(open(f"{BASE}/hidden_files/w45/es-it-proof/freeze-diff.json"))
NS="{http://www.w3.org/2000/svg}"
def texts(path):
    t=ET.parse(path); out=[]
    for e in t.iter():
        if e.tag.endswith('text') and e.text:
            out.append(e.text)
    return out
def norm(s):
    s=s.replace("\n"," ").replace("—"," ").replace("–"," ")
    s=re.sub(r"\s+"," ",s)
    return s
def tokens(s):
    # Latin-script word tokens (letters incl accents), length>=2, exclude pure numbers
    toks=re.findall(r"[A-Za-zÀ-ÿ]+(?:['’][A-Za-zÀ-ÿ]+)?", s)
    return [t for t in toks if len(t)>=2]
import glob, os
pages={}
for p in sorted(glob.glob(f"{BASE}/files/weekly-report-w45-es-core/svg/*.svg")):
    n=os.path.basename(p)[1]
    pages.setdefault(n,{})['core']=norm(" ".join(texts(p)))
for p in sorted(glob.glob(f"{BASE}/files/weekly-report-w45-es-it/svg/*.svg")):
    n=os.path.basename(p)[1]
    pages.setdefault(n,{})['ed']=norm(" ".join(texts(p)))
def has_cjk(s): return any('\u4e00'<=c<='\u9fff' for c in s)
print("=== REMOVED-STRING TOKEN SURVIVAL (per page): tokens in removed strings NOT found in edition page full text ===")
for pg in sorted(d['pages'], key=int):
    ed=pages[pg]['ed']; edlow=ed.lower()
    missing={}
    for item in d['pages'][pg]['removed_strings']:
        txt=item['text']
        for tok in tokens(txt):
            if tok.lower() not in edlow:
                missing.setdefault(tok,[]).append(txt)
    print(f"--- p{pg}: {len(missing)} distinct missing tokens ---")
    for tok, exs in sorted(missing.items()):
        print(f"  {tok!r}  e.g. {exs[0][:110]!r} (in {len(exs)} removed strings)")
print()
print("=== ADDED-STRING tokens NOT in core page text (candidates for new Spanish/Italian) ===")
for pg in sorted(d['pages'], key=int):
    core=pages[pg]['core']; corelow=core.lower()
    newt={}
    for item in d['pages'][pg]['added_strings']:
        txt=item['text']
        for tok in tokens(txt):
            if tok.lower() not in corelow:
                newt.setdefault(tok,[]).append(txt)
    print(f"--- p{pg}: {len(newt)} distinct new tokens ---")
    print("   ", ", ".join(sorted(newt.keys())))
