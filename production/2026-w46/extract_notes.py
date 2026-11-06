import re, os
D=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-ja-build")
notes={}
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
    txt=open(os.path.join(D,f),encoding="utf-8").read()
    for m in re.finditer(r'\.ex\("[^"]*",\s*"[^"]*",\s*"[^"]*",\s*"([^"]*)"',txt):
        notes.setdefault(m.group(1),[]).append(f)
    for m in re.finditer(r'(?m)^\s*\[(.*)\],\s*$',txt):
        strs=re.findall(r'"([^"]*)"',m.group(1))
        if strs and all(('=' in s or '＝' in s or '对照' in s) for s in strs):
            for s in strs: notes.setdefault(s,[]).append(f+"(list)")
for s,fs in sorted(notes.items()):
    print(f"[{','.join(sorted(set(fs)))}] {s!r},")
print("TOTAL distinct notes:",len(notes))
