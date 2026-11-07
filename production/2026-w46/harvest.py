import re, os, sys, ast
W45=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files")
CORE=os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-ja-build")
core_text=""
for f in ["bslib4.py","content12.py","content34.py","content56.py","content7.py","content8.py","render.py"]:
    core_text+=open(os.path.join(CORE,f),encoding="utf-8").read()
lang=sys.argv[1]
src=open(os.path.join(W45,f"weekly-report-w45-ja-{lang}-build","transform.py"),encoding="utf-8").read()
# crude: find all ("old", "new") string pairs in PER_FILE/GLOBAL sections
pairs=re.findall(r'\(\s*"((?:[^"\\]|\\.)*)"\s*,\s*"((?:[^"\\]|\\.)*)"\s*\)',src)
seen=set()
for old,new in pairs:
    old=old.encode().decode('unicode_escape') if '\\' in old else old
    if old in seen: continue
    seen.add(old)
    if old in core_text:
        print(f"REUSE {old!r} -> {new!r}")
