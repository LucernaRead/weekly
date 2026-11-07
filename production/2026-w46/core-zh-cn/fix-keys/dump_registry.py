#!/usr/bin/env python3
"""Static registry dump for W46 zh-cn core: parse content*.py with AST (no import),
number exercises in build order, print key/note/stem/options for semantic verification."""
import ast, os, sys

BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-zhcn-build")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]

def ev(node):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.List):
        return [ev(e) for e in node.elts]
    if isinstance(node, ast.Tuple):
        return [ev(e) for e in node.elts]
    if isinstance(node, ast.BinOp) and isinstance(node.op, ast.Add):
        a, b = ev(node.left), ev(node.right)
        if isinstance(a, str) and isinstance(b, str):
            return a + b
        return f"<binop {a!r} + {b!r}>"
    if isinstance(node, ast.JoinedStr):
        parts = []
        for v in node.values:
            if isinstance(v, ast.Constant):
                parts.append(str(v.value))
            elif isinstance(v, ast.FormattedValue):
                parts.append("{...}")
            else:
                parts.append("<fmt>")
        return "".join(parts)
    if isinstance(node, ast.Name):
        return f"<name:{node.id}>"
    return f"<{type(node).__name__}>"

n = 0
out = []
for fname in FILES:
    tree = ast.parse(open(os.path.join(BUILD, fname), encoding="utf-8").read())
    # page tracking: CURPAGE assignments
    page = None
    for node in ast.walk(tree):
        pass
    # walk in source order: iterate top-level statements in order, tracking CURPAGE
    for stmt in tree.body:
        # find CURPAGE assignments and calls recursively in source order via ast.walk sorted by lineno is messy;
        # instead walk all nodes of this statement sorted by lineno
        nodes = [nd for nd in ast.walk(stmt)]
        nodes.sort(key=lambda nd: (getattr(nd, "lineno", 0), getattr(nd, "col_offset", 0)))
        for nd in nodes:
            if isinstance(nd, ast.Assign):
                # CURPAGE[0] = N  -> Subscript
                try:
                    if isinstance(nd.targets[0], ast.Subscript) and isinstance(nd.targets[0].value, ast.Name) and nd.targets[0].value.id == "CURPAGE":
                        page = ev(nd.value)
                except Exception:
                    pass
            if isinstance(nd, ast.Call) and isinstance(nd.func, ast.Attribute) and nd.func.attr in ("ex", "match_set"):
                if nd.func.attr == "ex":
                    args = [ev(a) for a in nd.args]
                    level, typ, key, note, body = args[0], args[1], args[2], args[3], args[4] if len(args) > 4 else ""
                    opts = None
                    for kw in nd.keywords:
                        if kw.arg == "instr":
                            opts = ev(kw.value)
                    n += 1
                    out.append(f"{n}. [{fname}:{nd.lineno} p{page} {level} {typ}] KEY={key!r} NOTE={note!r} STEM={body!r} opts={opts}")
                    if len(args) > 5:
                        out.append(f"    OPTS-ARG={args[5]!r}")
                else:
                    args = [ev(a) for a in nd.args]
                    level, typ, lefts, rights, keys, notes = args[0], args[1], args[2], args[3], args[4], args[5]
                    for l, k, nt in zip(lefts, keys, notes):
                        n += 1
                        out.append(f"{n}. [{fname}:{nd.lineno} p{page} {level} {typ}/matching] KEY={k!r} NOTE={nt!r} LEFT={l!r}")
                    out.append(f"    RIGHTS(a-d)={rights!r} LEFTS={lefts!r} KEYS={keys!r}")
    print(f"# {fname} done, cumulative n={n}", file=sys.stderr)
print(f"TOTAL={n}")
for line in out:
    print(line)
