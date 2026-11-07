import re
p="/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-ja-en-build/transform.py"
src=open(p,encoding="utf-8").read()
# capture second elements of ("old", "new") and ('old', 'new') pairs in GLOBAL/NOTES/PER_FILE
news=[]
for m in re.finditer(r'\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)',src):
    news.append(m.group(2))
for m in re.finditer(r"\(\s*'((?:[^'\\]|\\.)*)'\s*,\s*'((?:[^'\\]|\\.)*)'\s*\)",src):
    news.append(m.group(2))
seen=[]
for n in news:
    if n not in seen: seen.append(n)
for i,n in enumerate(seen): print(i, repr(n))
print("COUNT",len(seen))
