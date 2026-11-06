import re, json, hashlib, base64, unicodedata
from xml.etree import ElementTree as ET
from collections import Counter
import glob, os
CORE="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-core/svg"
ED="/home/hatch/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ru-pt/svg"
def texts(path):
    t=open(path,encoding='utf-8').read()
    # text elements content
    return re.findall(r'<text[^>]*>(.*?)</text>', t, re.S)
def clean(s):
    return re.sub(r'<[^>]+>','',s)
CYR=re.compile(r'[А-Яа-яЁё]+')
def cyrtoks(path):
    c=Counter()
    for s in texts(path):
        for tok in CYR.findall(clean(s)): c[tok]+=1
    return c
for i,page in enumerate(["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"],1):
    cc=cyrtoks(f"{CORE}/{page}.svg"); ec=cyrtoks(f"{ED}/{page}.svg")
    diff_c = cc-ec; diff_e = ec-cc
    print(f"P{i} core_total={sum(cc.values())} ed_total={sum(ec.values())} removed={dict(diff_c)} added={dict(diff_e)}")
print("--- fullwidth parens ---")
for page in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]:
    raw=open(f"{ED}/{page}.svg",encoding='utf-8').read()
    print(page, "FF ( =", raw.count('（'), "FF ) =", raw.count('）'), "CJK chars:", sum(1 for ch in raw if '\u4e00'<=ch<='\u9fff' or '\u3040'<=ch<='\u30ff'))
print("--- images ---")
def imgs(path):
    raw=open(path,encoding='utf-8').read()
    out=[]
    for m in re.finditer(r'xlink:href="data:image/[^;]+;base64,([^"]+)"', raw):
        out.append(hashlib.sha256(base64.b64decode(m.group(1))).hexdigest()[:16])
    # also href without xlink
    for m in re.finditer(r'(?<!xlink:)href="data:image/[^;]+;base64,([^"]+)"', raw):
        out.append(hashlib.sha256(base64.b64decode(m.group(1))).hexdigest()[:16])
    return out
for page in ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]:
    print(page, "core", imgs(f"{CORE}/{page}.svg"), "ed", imgs(f"{ED}/{page}.svg"), "EQUAL" if imgs(f"{CORE}/{page}.svg")==imgs(f"{ED}/{page}.svg") else "DIFF")
