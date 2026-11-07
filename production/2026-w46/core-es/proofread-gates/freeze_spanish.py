import json, glob, re, os
G=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/es-proofread-gates")
# Spanish body vocabulary probe: removed strings that look like Spanish prose (contain Spanish words, length>=30, no CJK/Cyrillic/Hangul/Kana, not furniture)
SPAN=re.compile(r"[a-záéíóúñü]", re.I)
def is_spanish_prose(s):
    if any('\u4e00'<=c<='\u9fff' or '\u3040'<=c<='\u30ff' or '\uac00'<=c<='\ud7a3' or '\u0400'<=c<='\u04ff' for c in s): return False
    if len(s)<30: return False
    # must contain several Spanish words
    words=re.findall(r"[A-Za-zÁÉÍÓÚÑÜáéíóúñü]+", s)
    if len(words)<5: return False
    # exclude furniture-like (contains · or VOL or page markers heavily?) keep but flag
    return True
for code in ["de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    d=json.load(open(f"{G}/freeze-{code}.json"))
    print(f"\n===== es-{code}: long Spanish-looking REMOVED strings =====")
    n=0
    for pg,pdata in d["pages"].items():
        for r in pdata["removed_strings"]:
            s=r["text"]
            if is_spanish_prose(s):
                n+=1
                print(f"  P{pg} x{r['count']}: {s[:180]}")
    print(f"  total {n}")
    print(f"----- long Spanish-looking ADDED strings (should be re-wrap fragments / gloss citations only) -----")
    n=0
    for pg,pdata in d["pages"].items():
        for r in pdata["added_strings"]:
            s=r["text"]
            if is_spanish_prose(s):
                n+=1
                print(f"  P{pg} x{r['count']}: {s[:180]}")
    print(f"  total {n}")
