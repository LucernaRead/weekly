import re, html, glob, os, json
from collections import Counter
from PIL import ImageFont
D=os.path.expanduser("~/workspace/weekly-git/production/2026-w47/core-ja/svg")
def texts(p):
    s=open(p,encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>","",c)) for c in re.findall(r"<text[^>]*>(.*?)</text>",s,re.S)]
alltext=[]
for f in sorted(glob.glob(D+"/*.svg")):
    ts=texts(f); alltext+=ts
    print(f.split("/")[-1], len(ts), "texts")
blob="".join(t.replace(" ","").replace("\u3000","") for t in alltext)
quotes=["「19日（木よう日）は、酉の市・二の酉です。」","「同じ19日（木よう日）は、ボジョレー・ヌーヴォーの解禁日です。」","「熊手は、商売繁盛の縁起物です。」","「ボジョレー・ヌーヴォーは、フランスのボジョレー地方の新酒です。」","「3日目まで、大の里も豊昇龍も2勝1敗です。」","「『りくりゅう』は、フィギュアスケートのペアです。」","「紅葉の見頃は、京都へ移っています。」","「酉の市は、11月の酉の日に開くお祭りです。」"]
for q in quotes:
    print("PHRASE", blob.count(q.replace(" ","")), q)
# kinsoku: line starts
NO_START="。、，．！？：；）」』】ー…‥・"
bad=[]
for f in sorted(glob.glob(D+"/*.svg")):
    for t in texts(f):
        if t and t[0] in NO_START: bad.append((f.split("/")[-1],t))
print("KINSOKU line-start hits:", bad)
# chart graze: P6 labels vs bars
s=open(D+"/p6-fukayomi.svg",encoding="utf-8").read()
print("P6 chart rects:", re.findall(r'<rect x="338" y="(\d+)" width="(\d+)"', s)[:6])
# dump full text
with open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja/ja-core-text.txt"),"w",encoding="utf-8") as fh:
    for f in sorted(glob.glob(D+"/*.svg")):
        fh.write("\n===== %s =====\n"%os.path.basename(f))
        for t in texts(f): fh.write(t+"\n")
print("dumped")
