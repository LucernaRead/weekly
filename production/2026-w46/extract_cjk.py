import re, glob, os, json
D=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-ja-build")
CJK=re.compile(r'[\u4e00-\u9fff]')
out={}
for f in ["bslib4.py","content12.py","content34.py","content56.py","content7.py","content8.py","render.py"]:
    txt=open(os.path.join(D,f),encoding="utf-8").read()
    for m in re.finditer(r'"([^"\n]*)"',txt):
        s=m.group(1)
        if CJK.search(s):
            out.setdefault(s,[]).append(f)
for s,fs in sorted(out.items()):
    print(f"{len(fs)}x [{','.join(sorted(set(fs)))}] {s}")
print("TOTAL distinct:",len(out))
