# -*- coding: utf-8 -*-
"""Own gloss counter (AST, README #21 method): gloss() call strings split
on '·'; bridge/Nota strings: strip prefix 'Nota — ' (edition) / '译注｜'
(core) before splitting; mots/mots4/mots5 list lengths. Page tracked via
CURPAGE[0] = N in file order. Read-only over build sources."""
import ast, os, re, sys, json

CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-fr-build")
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-fr-it-build")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]

def count_file(path):
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src)
    page = None
    res = {}
    for node in tree.body:
        seg = ast.get_source_segment(src, node) or ""
        m = re.search(r"CURPAGE\[0\] = (\d)", seg)
        if m:
            page = int(m.group(1))
        if page is None:
            continue
        res.setdefault(page, [0, 0, 0])
        for sub in ast.walk(node):
            if not isinstance(sub, ast.Call):
                continue
            func = sub.func
            name = func.attr if isinstance(func, ast.Attribute) else ""
            if name == "gloss" and sub.args and isinstance(sub.args[0], ast.Constant):
                s = sub.args[0].value
                res[page][0] += len([t for t in s.split("·") if t.strip().strip("。")])
            if name == "bridge" and sub.args and isinstance(sub.args[0], ast.Constant):
                s = sub.args[0].value
                if s.startswith(("译注", "HINWEIS", "Nota")):
                    s2 = re.sub(r"^(译注｜|HINWEIS · |Nota — )", "", s)
                    res[page][1] += len([t for t in s2.split("·") if t.strip()])
        if isinstance(node, ast.Assign):
            for tgt in node.targets:
                if isinstance(tgt, ast.Name) and tgt.id in ("mots", "mots4", "mots5"):
                    if isinstance(node.value, ast.List):
                        res[page][2] += len(node.value.elts)
    return res

out = {}
for label, base in [("core", CORE), ("edition", ED)]:
    per = {}
    tot = [0, 0, 0]
    for f in FILES:
        r = count_file(os.path.join(base, f))
        for pg in sorted(r):
            cur = per.setdefault(pg, [0, 0, 0])
            for i in range(3):
                cur[i] += r[pg][i]; tot[i] += r[pg][i]
    out[label] = {"per_page": {str(k): v for k, v in sorted(per.items())}, "total": tot}
    print(label, "per_page", out[label]["per_page"], "total", tot)
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
