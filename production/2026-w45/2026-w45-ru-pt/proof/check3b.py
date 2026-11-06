import re
def footers(path):
    raw=open(path,encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'<text[^>]*y="([^"]*)"[^>]*>(.*?)</text>', raw, re.S):
        txt=re.sub(r'<[^>]+>','',m.group(2)).strip()
        if float(m.group(1))>2550 and txt: out.append(txt)
    return out
import glob
for pg in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]:
    e=footers(f"/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-pt/svg/{pg}.svg")
    w=footers(f"/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ru-pt/svg/{pg}.svg")
    en=[s.replace("VOL.2","VOL.X") for s in e]; wn=[s.replace("VOL.1","VOL.X") for s in w]
    print(pg, "ED:", e)
    print(pg, "W43:", w, "MATCH-normalized:", en==wn)
