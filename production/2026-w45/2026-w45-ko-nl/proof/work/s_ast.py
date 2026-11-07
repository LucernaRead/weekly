# -*- coding: utf-8 -*-
"""Independent AST gloss count for W45 KO core (orig) vs KO x NL (build).
Rule: every .gloss()/.glossline() call's first argument string value;
items = number of '·'-separated segments (a string with no '·' = 1 item).
f-strings: join constant parts (placeholders contribute no '·').
Parenthesised strings are transparent to AST (this is where regex undercounts)."""
import ast, os, sys
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
B = os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-nl-build")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]

def str_value(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts = []
        for v in node.values:
            if isinstance(v, ast.Constant): parts.append(str(v.value))
            elif isinstance(v, ast.FormattedValue): parts.append("\x00")
        return "".join(parts)
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        a, b = str_value(node.left), str_value(node.right)
        return None if a is None or b is None else a + b
    return None

def count_file(path):
    tree = ast.parse(open(path, encoding="utf-8").read())
    per_call = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute) \
                and node.func.attr in ("gloss", "glossline") and node.args:
            v = str_value(node.args[0])
            if v is None:
                per_call.append((node.lineno, node.func.attr, None, None))
            else:
                per_call.append((node.lineno, node.func.attr, v, len(v.split("·"))))
    per_call.sort()
    return per_call

for side, d in [("core-orig", os.path.join(B, "orig")), ("edition", B)]:
    print(f"== AST gloss {side} ==")
    tot = 0
    for f in FILES:
        calls = count_file(os.path.join(d, f))
        s = sum(c[3] for c in calls if c[3] is not None)
        tot += s
        print(f"   {f}: calls={len(calls)} items={s} unparsed={[c for c in calls if c[3] is None]}")
        for ln, attr, v, n in calls:
            # flag the two regex-miss shapes: paren inside string, f-string
            if v is not None and ("(" in v or "\x00" in v):
                print(f"      line {ln} .{attr} items={n} value={v[:110]!r}")
    print(f"   TOTAL {side} = {tot}")
