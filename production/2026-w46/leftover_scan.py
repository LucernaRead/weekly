import ast, json, os, re, sys
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
H46 = os.path.join(BASE, "hidden_files/w46")
FILES = ["content12.py","content34.py","content56.py","content7.py","content8.py","bslib4.py"]
CJK = re.compile(r"[\u4e00-\u9fff]")
core_strs = set(json.load(open(os.path.join(H46, "core-cjk-strings.json"), encoding="utf-8")))
def strs_in(path):
    out = {}
    tree = ast.parse(open(path, encoding="utf-8").read())
    for node in ast.walk(tree):
        v = None
        if isinstance(node, ast.Constant) and isinstance(node.value, str):
            v = node.value
        elif isinstance(node, ast.JoinedStr):
            v = "".join(p.value if isinstance(p, ast.Constant) else "{...}" for p in node.values)
        if v and CJK.search(v):
            out[v] = out.get(v, 0) + 1
    return out
native = sys.argv[1]
dst = os.path.join(BASE, "hidden_files", f"weekly-report-w46-en-{native}-build")
left = []
for f in FILES:
    for s, n in sorted(strs_in(os.path.join(dst, f)).items()):
        if s in core_strs:
            left.append({"file": f, "count": n, "text": s})
print(f"{native}: leftover core strings {len(left)}")
json.dump(left, open(os.path.join(H46, f"leftover-{native}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for i, e in enumerate(left):
    print(f"{i+1:3d} [{e['file']}] x{e['count']} {e['text']}")
