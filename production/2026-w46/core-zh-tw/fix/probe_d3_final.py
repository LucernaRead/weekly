import sys, os, re, ast
sys.path.insert(0, os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-zh-tw-fr-build"))
from svglib import wrap, text_w, _fw
src = open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-zh-tw-fr-build/content34.py"), encoding="utf-8").read()
tree = ast.parse(src)
gloss = None
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and getattr(node.func, "attr", "") == "gloss" and node.args:
        v = node.args[0]
        if isinstance(v, ast.Constant) and "Wei Chuan Dragons est prévu" in str(v.value):
            gloss = v.value
assert gloss, "gloss not found"
print("GLOSS:", gloss)
lines = wrap("Note — " + gloss, "sans", False, 20.5, 398)
t = _fw("Note — " + gloss); words = set(t.split(" "))
splits = []
for i in range(len(lines)-1):
    a = lines[i].split(" ")[-1]; b = lines[i+1].split(" ")[0]
    balpha = re.match(r"[A-Za-zÀ-ÿ]+", b)
    if a and balpha and a[-1].isalpha() and (a + balpha.group(0)) in words:
        splits.append((i, a, b))
print(f"lines={len(lines)} splits={splits}")
for ln in lines: print(f"  [{text_w(ln,'sans',False,20.5):6.1f}] {ln!r}")
assert not splits and len(lines) == 11, "D3 probe FAILED"
print("D3 PROBE OK")
