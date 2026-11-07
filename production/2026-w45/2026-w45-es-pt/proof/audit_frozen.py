import re, html, pathlib, collections
base=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
CJK_RE=re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
def texts(p):
    s=p.read_text(encoding='utf-8')
    out=[]
    for m in re.finditer(r'<text\b[^>]*>(.*?)</text>', s, flags=re.S):
        t=html.unescape(re.sub(r'<[^>]+>','',m.group(1)))
        out.append(t)
    return out
def elems(p):
    s=p.read_text(encoding='utf-8')
    out=[]
    for m in re.finditer(r'<text\b([^>]*)>(.*?)</text>', s, flags=re.S):
        out.append((m.group(1), html.unescape(re.sub(r'<[^>]+>','',m.group(2)))))
    return out
pages={'p1-portada':'p1','p2-vida':'p2','p3-cultura':'p3','p4-deporte':'p4','p5-juventud':'p5','p6-afondo':'p6','p7-lengua':'p7','p8-ejercicios':'p8'}
print("=== 1. removed strings with NO char in freeze CJK_RE (tool definition) ===")
import json
d=json.load(open(base/"hidden_files/w45/es-pt-proof/freeze-diff.json"))
for pg,v in sorted(d['pages'].items(), key=lambda x:int(x[0])):
    for r in v['removed_strings']:
        if not CJK_RE.search(r['text']):
            print(f"  P{pg} REM x{r['count']}: {r['text']!r}")
print("\n=== 2. core long texts (>=40 chars) missing verbatim from edition ===")
for f,pg in pages.items():
    ct=texts(base/f"files/weekly-report-w45-es-core/svg/{f}.svg")
    et=collections.Counter(texts(base/f"files/weekly-report-w45-es-pt/svg/{f}.svg"))
    missing=[]
    for t in ct:
        if len(t)>=40 and et[t]==0: missing.append(t)
        elif len(t)>=40: et[t]-=1
    print(f"  {pg}: core long texts={sum(1 for t in ct if len(t)>=40)} missing={len(missing)}")
    for t in missing: print(f"    MISSING: {t!r}")
print("\n=== 3. core texts containing NO CJK at all, missing verbatim (short too) ===")
for f,pg in pages.items():
    ct=texts(base/f"files/weekly-report-w45-es-core/svg/{f}.svg")
    et=collections.Counter(texts(base/f"files/weekly-report-w45-es-pt/svg/{f}.svg"))
    missing=[]
    for t in ct:
        if not CJK_RE.search(t) and t.strip():
            if et[t]==0: missing.append(t)
            else: et[t]-=1
    print(f"  {pg}: missing-noCJK-texts={len(missing)}")
    for t in missing: print(f"    MISSING: {t!r}")
