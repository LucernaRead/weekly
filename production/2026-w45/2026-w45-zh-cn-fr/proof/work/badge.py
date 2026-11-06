import re, glob
def find(p, needles):
    s=open(p,encoding="utf-8").read()
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>", s, re.S):
        c=re.sub(r"<[^>]+>","",m.group(2))
        for n in needles:
            if n in c:
                print(p.split("/")[-2], "|", m.group(1)[:220], "|", c[:120])
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-fr/svg/p1-touiban.svg"
CO="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg/p1-touiban.svg"
W43="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-fr/svg/p1-touiban.svg"
for p in [ED,CO,W43]:
    print("=====",p)
    find(p, ["TEXTES EN CHINOIS","简体中文正文 · 英语讲解","给学中文的人的周报","HEBDOMADAIRE CHINOIS"])
