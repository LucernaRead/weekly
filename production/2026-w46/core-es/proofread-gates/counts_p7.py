import re, glob, os, html, collections
BASE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def texts_of(fn):
    s=open(fn,encoding="utf-8").read()
    return [html.unescape(re.sub(r"<[^>]+>","",c)) for c in re.findall(r"<text[^>]*>(.*?)</text>", s, re.S)]
print("===== EXERCISE COUNTS: bracketed level tags =====")
for code in ["core","de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    perpage=[]; tot=collections.Counter()
    for fn in sorted(glob.glob(BASE+"/files/weekly-report-w46-es-"+code+"/svg/*.svg")):
        joined=" ".join(texts_of(fn))
        c=collections.Counter(re.findall(r"\[(A2|B1|B2)\]", joined))
        perpage.append(dict(c)); tot.update(c)
    print(code, "A2=",tot["A2"],"B1=",tot["B1"],"B2=",tot["B2"],"sum=",sum(tot.values()),"perpage=",perpage)
print("\n===== P7 long lines =====")
for code in ["core","de","en","fr","it","ja","ko","nl","pt","ru","zh-cn","zh-tw"]:
    p7=texts_of(BASE+"/files/weekly-report-w46-es-"+code+"/svg/p7-lengua.svg")
    print("\n-- "+code+" --")
    for t in p7:
        if len(t)>=55:
            print("   ", t[:170])
