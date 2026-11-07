# -*- coding: utf-8 -*-
"""Post-transform audit: every CJK constant in the transformed build must be
a mapped new value, an adjudicated identical value, the P1 badge, or a
fragment of the two new JA f-strings. Anything else = unmapped core value.
"""
import ast
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import transform as T

CJK = re.compile(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7a3]")
allowed = set(T.MAP.values()) | T.ALLOW_IDENTICAL | {
    "英語テキスト · 日本語の解説 — 日本語読者のための版",
    " ページ（全 ", " ページ）", "— ", " ページ —",
}
bad = []
for fn in T.FILES:
    src = open(os.path.join(T.HERE, fn), encoding="utf-8").read()
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and CJK.search(node.value):
            if node.value not in allowed:
                bad.append((fn, node.lineno, node.value))
print("unmapped CJK constants:", len(bad))
for fn, ln, v in bad:
    print(f"  {fn}:{ln} {v!r}")
sys.exit(1 if bad else 0)
