import os, glob, subprocess, re, json
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
codes=["de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]
def run(cmd):
    r=subprocess.run(cmd,capture_output=True)
    return r.stdout
print("===== PDF CHECKS (web + print) =====")
for code in ["core"]+codes:
    d=f"{BASE}/files/weekly-report-w46-es-{code}"
    for f in sorted(glob.glob(d+"/*.pdf")):
        sz=os.path.getsize(f)
        txt=run(["pdftotext",f,"-"])
        info=run(["pdfinfo",f]).decode(errors="replace")
        pages=[l for l in info.splitlines() if l.startswith("Pages:")]
        print(f"{code} {os.path.basename(f)} size={sz} ({sz/1048576:.2f}MB) pdftotext_bytes={len(txt)} {pages}")
    print("---")
print("\n===== ABSTRACT.txt =====")
for code in ["core"]+codes:
    p=f"{BASE}/files/weekly-report-w46-es-{code}/ABSTRACT.txt"
    raw=open(p,encoding="utf-8").read()
    lines=raw.splitlines()
    print(f"{code}: lines={len(lines)} chars={len(raw)} has_ascii_quote={'\"' in raw} ends_newline={raw.endswith(chr(10))}")
    print("  ", lines[0][:220] if lines else "(empty)")
print("\n===== READER-FACING SWEEP: forbidden internal terms in SVG text =====")
FORB=["w46","W46","2026-w46","2026-W46","es-de","es-en","es-fr","es-it","es-ja","es-ko","es-nl","es-pt","es-ru","zh-cn","zh-tw","github","discord","SOP","proofread","audit","lint","freeze","occlusion","insert.py","KIT","http://","https://",".md","weekly-git","hidden_files","TODO","FIXME","Lorem"]
import html
def texts(d):
    out=[]
    for fn in sorted(glob.glob(d+"/svg/*.svg")):
        s=open(fn,encoding="utf-8").read()
        for m in re.finditer(r"<text[^>]*>(.*?)</text>", s, re.S):
            out.append((os.path.basename(fn), html.unescape(re.sub(r"<[^>]+>","",m.group(1)))))
    return out
for code in codes:
    hits=[]
    for fn,t in texts(f"{BASE}/files/weekly-report-w46-es-{code}"):
        for f in FORB:
            if f in t: hits.append((fn,f,t[:130]))
    print(f"{code}: {len(hits)} hits")
    for h in hits: print("   ",h)
print("\n===== '12 de noviembre' occurrences (decree-date check) =====")
for code in ["core"]+codes:
    for fn,t in texts(f"{BASE}/files/weekly-report-w46-es-{code}"):
        if "12 de noviembre" in t or "12 noviembre" in t.lower():
            print(f"{code} {fn}: {t[:200]}")
print("\n===== image credit strings =====")
for code in ["core"]+codes:
    found=set()
    for fn,t in texts(f"{BASE}/files/weekly-report-w46-es-{code}"):
        for kw in ["Commons","CC0","Wikimedia","Sugar-roasted","chestnut","castaña","Ilustración","ilustración","Infamia"]:
            if kw.lower() in t.lower(): found.add(kw)
    print(code, sorted(found))
