# -*- coding: utf-8 -*-
"""Own AST-literal freeze check: collect string constants from CORE build
sources, keep those with no Han char, test presence (exact substring) in
EDITION build sources. Read-only."""
import ast, os, sys, json

CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-fr-build")
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-fr-it-build")

def has_han(s):
    return any("\u4e00" <= c <= "\u9fff" for c in s)

def collect(d, files):
    out = []  # (file, lineno, value)
    for f in files:
        src = open(os.path.join(d, f), encoding="utf-8").read()
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str):
                out.append((f, node.lineno, node.value))
    return out

def run(files, label):
    core = collect(CORE, files)
    ed_text = ""
    for f in files:
        ed_text += open(os.path.join(ED, f), encoding="utf-8").read() + "\n"
    ed_text_all = ed_text
    nohan = [(f, ln, v) for f, ln, v in core if not has_han(v)]
    # dedupe by value for missing analysis, keep first occurrence
    seen = {}
    for f, ln, v in nohan:
        seen.setdefault(v, (f, ln))
    missing = [(v, seen[v]) for v in seen if v not in ed_text_all]
    # edition source Han literals count
    ed_lits = collect(ED, files)
    ed_han = [(f, ln, v) for f, ln, v in ed_lits if has_han(v)]
    print(f"== {label} files={files}")
    print(f" core literals total={len(core)} no-Han unique={len(seen)} missing={len(missing)}")
    for v, (f, ln) in missing:
        print(f"  MISSING [{f}:{ln}] {v!r}")
    print(f" edition literals with Han={len(ed_han)}")
    for f, ln, v in ed_han[:20]:
        print(f"  ED-HAN [{f}:{ln}] {v!r}")
    return {"files": files, "core_total": len(core), "nohan_unique": len(seen),
            "missing": [{"value": v, "core_file": f, "core_line": ln} for v, (f, ln) in missing],
            "ed_han_count": len(ed_han),
            "ed_han_sample": [{"file": f, "line": ln, "value": v} for f, ln, v in ed_han[:20]]}

res = {}
res["content_only"] = run(["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"], "content-only")
res["content_plus_bslib"] = run(["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"], "content+bslib")
json.dump(res, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", sys.argv[1])
