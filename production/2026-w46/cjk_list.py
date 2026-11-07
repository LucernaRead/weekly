# -*- coding: utf-8 -*-
"""List every string literal containing CJK chars in the W46 core content
files, with file:line and enclosing call context. Workload list for fan-out
SUPP maps."""
import ast, os, re, sys

BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-ko-build")
CJK = re.compile(r"[\u4e00-\u9fff]")

for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    src = open(os.path.join(BUILD, fname), encoding="utf-8").read()
    tree = ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and CJK.search(node.value):
            line = src.split("\n")[node.lineno - 1].strip()[:110]
            print(f"{fname}:{node.lineno}: {node.value!r}")
