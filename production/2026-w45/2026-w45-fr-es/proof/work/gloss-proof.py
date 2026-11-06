# -*- coding: utf-8 -*-
"""Gloss counts, core vs edition, from build sources (README #21:
split the rendered gloss() call string on '·' itself).
Categories per page:
  (a) gloss() call strings, items = split on '·' (drop empties, strip
      trailing '。' handling: items counted as split parts, non-empty)
  (b) Nota/HINWEIS/译注 bridge strings, same split
  (c) word-list boxes: mots/mots4/mots5 list literals (AST), items = list len
Page assignment: content12 -> P1,P2 (split by CURPAGE assignment in file
order); content34 -> P3,P4; content56 -> P5,P6; content7 -> P7;
content8 -> P8 (no gloss apparatus there).
Simpler robust approach: process each file's top-level statements in
order, tracking the current CURPAGE[0] = N assignment, and attribute
gloss/bridge/mots counts to that page.
"""
import ast, os, re, sys

CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-fr-build")
ED = os.path.dirname(os.path.abspath(__file__))


def count_file(path):
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    page = None
    res = {}  # page -> [gloss_items, bridge_items, mots_items]
    for node in tree.body:
        # CURPAGE[0] = N
        if isinstance(node, ast.Assign):
            pass
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Subscript):
            try:
                v = node.value
                if isinstance(v.value, ast.Subscript):
                    pass
            except Exception:
                pass
        # detect CURPAGE[0] = N via source segment regex on the node
        seg = ast.get_source_segment(src, node) or ""
        m = re.search(r"CURPAGE\[0\] = (\d)", seg)
        if m:
            page = int(m.group(1))
        if page is None:
            continue
        res.setdefault(page, [0, 0, 0])
        # walk calls in this statement
        for sub in ast.walk(node):
            if not isinstance(sub, ast.Call):
                continue
            func = sub.func
            name = ""
            if isinstance(func, ast.Attribute):
                name = func.attr
            if name == "gloss" and sub.args and isinstance(sub.args[0], ast.Constant):
                s = sub.args[0].value
                items = [t.strip() for t in s.split("·") if t.strip().strip("。")]
                res[page][0] += len(items)
            if name == "bridge" and sub.args and isinstance(sub.args[0], ast.Constant):
                s = sub.args[0].value
                if s.startswith(("译注", "HINWEIS", "Nota")):
                    # strip the prefix itself ("译注｜" / "HINWEIS · ")
                    # before splitting, or the German prefix adds a phantom item
                    s2 = re.sub(r"^(译注｜|HINWEIS · |Nota — )", "", s)
                    items = [t for t in s2.split("·")]
                    res[page][1] += len([t for t in items if t.strip()])
        # mots list literals
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in ("mots", "mots4", "mots5"):
                    if isinstance(node.value, ast.List):
                        res[page][2] += len(node.value.elts)
    return res


for label, base in [("core", CORE), ("edition", ED)]:
    total = [0, 0, 0]
    print("==", label)
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        r = count_file(os.path.join(base, f))
        for pg in sorted(r):
            print(f"  P{pg}: gloss={r[pg][0]} bridge-hinweis={r[pg][1]} mots={r[pg][2]}")
            for i in range(3):
                total[i] += r[pg][i]
    print("  TOTAL gloss/bridge/mots:", total)
