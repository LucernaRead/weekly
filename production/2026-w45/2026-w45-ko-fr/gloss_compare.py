# -*- coding: utf-8 -*-
"""Gloss item counts (README #21): split each rendered gloss()/glossline()
call string on '·' itself, per content file, core vs edition. Read-only
AST walk for counting only (no source editing).
Usage: tools/venv/bin/python gloss_compare.py
"""
import ast
import os

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ko-build")


def count_file(path):
    tree = ast.parse(open(path, encoding="utf-8").read())
    per = {}
    total = 0
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        fn = node.func
        name = getattr(fn, "attr", None)
        if name not in ("gloss", "glossline") or not node.args:
            continue
        arg = node.args[0]
        if not isinstance(arg, ast.Constant) or not isinstance(arg.value, str):
            continue
        items = [seg.strip() for seg in arg.value.split("·") if seg.strip()]
        per.setdefault(name, []).append((len(items), arg.value[:40]))
        total += len(items)
    return total, per


def main():
    grand_c = grand_e = 0
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        tc, _ = count_file(os.path.join(CORE, fn))
        te, _ = count_file(os.path.join(HERE, fn))
        grand_c += tc
        grand_e += te
        print(f"{fn}: core {tc} edition {te} {'OK' if tc == te else 'MISMATCH'}")
    print(f"TOTAL: core {grand_c} edition {grand_e}")


if __name__ == "__main__":
    main()
