# -*- coding: utf-8 -*-
"""Dump every string literal containing CJK chars in the core build files,
with file + line, so fan-out translation maps cover the whole explanation layer."""
import ast, sys, os
CJK = lambda ch: "\u2e80" <= ch <= "\u9fff" or "\uac00" <= ch <= "\ud7a3" or "\u3040" <= ch <= "\u30ff"
d = sys.argv[1]
for fn in ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    path = os.path.join(d, fn)
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    seen = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and any(CJK(c) for c in node.value):
            if node.value in seen:
                continue
            seen.add(node.value)
            print(f"{fn}:{node.lineno}: {node.value!r}")
