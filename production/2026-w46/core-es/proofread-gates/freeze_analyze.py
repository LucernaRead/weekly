import json, glob, re, unicodedata, collections, os
G="/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/es-proofread-gates"
F="/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
import xml.etree.ElementTree as ET
def texts(d):
    out=[]
    for fn in sorted(glob.glob(d+"/svg/*.svg")):
        t=open(fn,encoding="utf-8").read()
        # strip tags crudely: extract <text ...>...</text> inner text incl tspans
        import re
        for m in re.finditer(r"<text[^>]*>(.*?)</text>", t, re.S):
            inner=re.sub(r"<[^>]+>","",m.group(1))
            out.append(inner)
    return out
core_texts=texts(F+"/weekly-report-w46-es-core")
core_chars=set("".join(core_texts))
core_cjk=set(c for c in core_chars if '\u4e00'<=c<='\u9fff')
print("CORE global CJK chars:", len(core_cjk))
for code in ["de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    d=json.load(open(f"{G}/freeze-{code}.json"))
    print(f"\n===== es-{code} cjk_added_total={d['cjk_added_total']} =====")
    for pg, pdata in d["pages"].items():
        added=pdata.get("cjk_added",{})
        print(f" P{pg} added-distinct={len(added)} total={sum(added.values())} coreTot={pdata.get('cjk_core_total')} edTot={pdata.get('cjk_edition_total')}")
    # global added chars not in core at all
    alladded=set()
    for pdata in d["pages"].values():
        alladded|=set(pdata.get("cjk_added",{}).keys())
    novel=alladded-core_chars
    print("  added chars NOVEL vs whole core:", sorted(novel)[:60], "count", len(novel))
    # Hangul / Hanzi / kana breakdown of edition
    ed=texts(F+f"/weekly-report-w46-es-{code}")
    edstr="".join(ed)
    hanzi=[c for c in edstr if '\u4e00'<=c<='\u9fff']
    hangul=[c for c in edstr if '\uac00'<=c<='\ud7a3']
    kana=[c for c in edstr if '\u3040'<=c<='\u30ff']
    cyr=[c for c in edstr if '\u0400'<=c<='\u04ff']
    print(f"  edition totals: Hanzi={len(hanzi)} distinct={len(set(hanzi))} Hangul={len(hangul)} Kana={len(kana)} Cyrillic={len(cyr)}")
    print(f"  Hanzi distinct in edition: {''.join(sorted(set(hanzi)))[:120]}")
