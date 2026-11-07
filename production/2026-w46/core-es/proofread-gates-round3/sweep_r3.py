import xml.etree.ElementTree as ET, pathlib, re, collections
BASE=pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files"
ED=BASE/"weekly-report-w46-es-de"; CORE=BASE/"weekly-report-w46-es-core"
NS="{http://www.w3.org/2000/svg}"
names=["p1-portada.svg","p2-vida.svg","p3-cultura.svg","p4-deporte.svg","p5-juventud.svg","p6-afondo.svg","p7-lengua.svg","p8-ejercicios.svg"]
def alltext(d):
    out=[]
    for nm in names:
        t=ET.parse(d/"svg"/nm)
        for el in t.iter(NS+"text"): out.append((nm,el.text or ""))
    return out
# reader-facing sweep
forbidden=["w46","W46","github","discord","SOP","proofread","audit","lint","freeze","occlusion","KIT","http",".md","frontmatter","insert.py","webpdf","slug","W45","VOL.1"]
print("=== reader-facing sweep DE ===")
for term in forbidden:
    hits=[(nm,s) for nm,s in alltext(ED) if term in s]
    print(term, len(hits), hits[:3])
print("=== credits ===")
for k in ["CC0","Wikimedia","Ilustración","Infamia","castaña","Commons"]:
    hits=[(nm,s) for nm,s in alltext(ED) if k in s]
    print(k, len(hits), hits[:2])
print("=== CJK scan DE (all chars >= U+2E80) ===")
cjk=collections.Counter()
for nm,s in alltext(ED):
    for ch in s:
        if ord(ch)>=0x2E80: cjk[ch]+=1
print("CJK total:", sum(cjk.values()), dict(cjk))
print("=== Hanzi/Hangul/kana probe ===")
joined="".join(s for _,s in alltext(ED))
print("Hangul:", sum(1 for c in joined if 0xAC00<=ord(c)<=0xD7A3), "Hanzi(CJK ext range):", sum(1 for c in joined if 0x4E00<=ord(c)<=0x9FFF), "hiragana:", sum(1 for c in joined if 0x3040<=ord(c)<=0x309F), "katakana:", sum(1 for c in joined if 0x30A0<=ord(c)<=0x30FF))
print("=== gloss boxes: HINWEIS lines ===")
for nm,s in alltext(ED):
    if s.startswith("HINWEIS") or "HINWEIS" in s: print(nm, repr(s))
print("=== P1 expl line ===")
for nm,s in alltext(ED):
    if nm=="p1-portada.svg" and s.startswith("Hinweis"): print(repr(s))
