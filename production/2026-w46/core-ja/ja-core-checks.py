import re, html, glob, os, json
from collections import Counter
from PIL import ImageFont
D=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-core/svg")
def texts(p):
    s=open(p,encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>","",c)) for c in re.findall(r"<text[^>]*>(.*?)</text>",s,re.S)]
alltext=[]
for f in sorted(glob.glob(D+"/*.svg")):
    ts=texts(f); alltext+=ts
    print(f.split("/")[-1], len(ts), "texts")
blob="".join(t.replace(" ","").replace("\u3000","") for t in alltext)
quotes=["「読書週間は、9日（月よう日）で終わります。」","「15日（日よう日）は、七五三の中心の日です。」","「『ポッキー＆プリッツの日』は、1999年に始まりました。」","「千歳飴は、長く生きてほしい、という願いのお菓子です。」","「七五三は、3歳と5歳と7歳の子どものお祝いです。」","「ソフトバンクが4連勝で日本一になりました。」","「11月11日は、ポッキーの日です。」","「紅葉の見頃は、北から南へ移ります。」"]
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
print("P6 chart rects:", re.findall(r'<rect x="315" y="(\d+)" width="(\d+)"', s)[:6])
# dump full text
with open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ja-core-text.txt"),"w",encoding="utf-8") as fh:
    for f in sorted(glob.glob(D+"/*.svg")):
        fh.write("\n===== %s =====\n"%os.path.basename(f))
        for t in texts(f): fh.write(t+"\n")
print("dumped")
