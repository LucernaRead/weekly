import re,glob,os,json,collections
from fontTools.ttLib import TTCollection, TTFont
BASE='/usr/share/fonts/opentype/noto'
def load(ttc, idx):
    return TTCollection(os.path.join(BASE,ttc)).fonts[idx].getBestCmap()
SERIF_R=load('NotoSerifCJK-Regular.ttc',2); SERIF_B=load('NotoSerifCJK-Bold.ttc',2)
SANS_R=load('NotoSansCJK-Regular.ttc',2); SANS_B=load('NotoSansCJK-Bold.ttc',2)
UNI=TTFont(os.path.expanduser('~/.local/share/fonts/UnifrakturMaguntia.ttf')).getBestCmap()
MAP={('Noto Serif CJK SC','700'):SERIF_B,('Noto Serif CJK SC','400'):SERIF_R,('Noto Serif CJK SC',None):SERIF_R,
     ('Noto Sans CJK SC','700'):SANS_B,('Noto Sans CJK SC','400'):SANS_R,('Noto Sans CJK SC',None):SANS_R,
     ('UnifrakturMaguntia',None):UNI,('UnifrakturMaguntia','400'):UNI}
missing=collections.Counter(); distinct=set(); pernode=0
for f in sorted(glob.glob(os.path.expanduser('~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ru-it/svg/*.svg'))):
    t=open(f,encoding='utf-8').read()
    for m in re.finditer(r'<text([^>]*)>(.*?)</text>',t,re.S):
        a,s=m.group(1),m.group(2)
        fam=re.search(r'font-family="([^"]+)"',a).group(1)
        w=re.search(r'font-weight="(\d+)"',a); w=w.group(1) if w else None
        cmap=MAP.get((fam,w)) or MAP.get((fam,None))
        assert cmap is not None,(fam,w)
        pernode+=1
        for ch in s:
            if ch.isspace(): continue
            distinct.add(ch)
            if ord(ch) not in cmap: missing[ch]+=1
print("nodes checked:",pernode,"distinct chars (excl ws):",len(distinct))
print("MISSING:",dict(missing),"total missing occurrences:",sum(missing.values()))
print("control š U+0161 in Serif cmap:",0x161 in SERIF_R or 0x161 in SERIF_B,"in Sans cmap:",0x161 in SANS_R or 0x161 in SANS_B)
print("control š in SerifR:",0x161 in SERIF_R,"SerifB:",0x161 in SERIF_B,"SansR:",0x161 in SANS_R,"SansB:",0x161 in SANS_B)
print("cmap sizes serifR/B sansR/B:",len(SERIF_R),len(SERIF_B),len(SANS_R),len(SANS_B))
json.dump({"distinct":len(distinct),"missing":{hex(ord(k)):v for k,v in missing.items()},"control_serif":0x161 in SERIF_R or 0x161 in SERIF_B,"control_sans":0x161 in SANS_R or 0x161 in SANS_B},open(os.path.expanduser('~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ru-proofread-gates-round3/gates/font-coverage.json'),'w'))
