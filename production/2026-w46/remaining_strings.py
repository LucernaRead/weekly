# -*- coding: utf-8 -*-
import ast, re, os, json
CJK = re.compile(r"[\u4e00-\u9fff]")
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
def strs_in(path):
    out = set()
    tree = ast.parse(open(path, encoding="utf-8").read())
    for node in ast.walk(tree):
        v = None
        if isinstance(node, ast.Constant) and isinstance(node.value, str): v = node.value
        elif isinstance(node, ast.JoinedStr):
            v = "".join(p.value if isinstance(p, ast.Constant) else "{...}" for p in node.values)
        if v and CJK.search(v): out.add(v)
    return out
FILES = ["content12.py","content34.py","content56.py","content7.py","content8.py","bslib4.py"]
allsets = {}
for native in ["de","fr","es","it","pt","nl","ru","ja","ko","zh-tw"]:
    d = os.path.join(BASE, "hidden_files", f"weekly-report-w46-en-{native}-build")
    s = set()
    for f in FILES: s |= strs_in(os.path.join(d, f))
    allsets[native] = s
    print(native, len(s))
union = set().union(*allsets.values())
print("union:", len(union))
json.dump({k: sorted(v) for k, v in allsets.items()}, open(os.path.join(BASE, "hidden_files/w46/remaining-strings.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
# strings remaining in ALL latin natives (common todo)
latin = ["de","fr","es","it","pt","nl","ru"]
common = set.intersection(*[allsets[n] for n in latin])
print("common-to-all-latin:", len(common))
json.dump(sorted(common), open(os.path.join(BASE, "hidden_files/w46/todo-common-latin.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
