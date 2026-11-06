# -*- coding: utf-8 -*-
"""Extract kept-pair translations (old in W46 core strings) per native -> JSON tables."""
import ast, os, json, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
# reuse extract() from bootstrap2 by importing its functions without running main: copy minimal logic
import importlib.util
spec = importlib.util.spec_from_file_location("b2", os.path.join(os.path.dirname(os.path.abspath(__file__)), "bootstrap2.py"))
# bootstrap2 runs its loop at import; avoid by re-implementing extract inline here
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
W46 = os.path.join(BASE, "hidden_files/weekly-report-w46-en-build")
W45 = os.path.join(BASE, "hidden_files")
FILES = ["content12.py","content34.py","content56.py","content7.py","content8.py","bslib4.py"]
def strval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str): return node.value
    if isinstance(node, ast.JoinedStr):
        return "".join(p.value if isinstance(p, ast.Constant) else "{...}" for p in node.values)
    return None
def tuples_of(node):
    out = []
    if isinstance(node, ast.List):
        for el in node.elts:
            if isinstance(el, ast.Tuple) and len(el.elts) >= 2:
                a, b = strval(el.elts[0]), strval(el.elts[1])
                if a is not None and b is not None: out.append((a, b))
    return out
def extract(tree):
    env = {}; pairs = []
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if not isinstance(t, ast.Name): continue
                if isinstance(node.value, ast.List): env[t.id] = tuples_of(node.value)
                elif isinstance(node.value, ast.Dict):
                    d = {}
                    for k, v in zip(node.value.keys, node.value.values):
                        kk = strval(k)
                        if isinstance(v, ast.List): vv = tuples_of(v)
                        elif isinstance(v, ast.Name): vv = ("REF", v.id)
                        elif isinstance(v, ast.Dict): vv = {strval(k2): strval(v2) for k2, v2 in zip(v.keys, v.values) if strval(k2) is not None and strval(v2) is not None}
                        else: vv = strval(v)
                        if kk is not None: d[kk] = vv
                    env[t.id] = d
    for node in ast.walk(tree):
        if isinstance(node, ast.AugAssign) and isinstance(node.value, ast.List):
            for el in node.value.elts:
                if isinstance(el, ast.Tuple) and len(el.elts) >= 3:
                    f, a, b = strval(el.elts[0]), strval(el.elts[1]), strval(el.elts[2])
                    if f in FILES and a is not None and b is not None: pairs.append((f, a, b))
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.List):
            for el in node.value.elts:
                if isinstance(el, ast.Tuple) and len(el.elts) >= 3:
                    f, a, b = strval(el.elts[0]), strval(el.elts[1]), strval(el.elts[2])
                    if f in FILES and a is not None and b is not None: pairs.append((f, a, b))
    for name, val in env.items():
        if isinstance(val, dict):
            for k, v in val.items():
                if isinstance(v, str):
                    for f in FILES: pairs.append((f, k, v))
                elif isinstance(v, tuple) and len(v) == 2 and v[0] == "REF":
                    v = env.get(v[1], [])
                    if isinstance(v, list) and k in FILES:
                        for a, b in v: pairs.append((k, a, b))
                elif isinstance(v, list) and k in FILES:
                    for a, b in v: pairs.append((k, a, b))
    named_lists = {k: v for k, v in env.items() if isinstance(v, list)}
    def visit(node):
        if isinstance(node, ast.Call):
            fn = node.func
            nm = fn.attr if isinstance(fn, ast.Attribute) else (fn.id if isinstance(fn, ast.Name) else "")
            if nm == "rep" and len(node.args) >= 3:
                f, o, n = strval(node.args[0]), strval(node.args[1]), strval(node.args[2])
                if f and o is not None: pairs.append((f, o, n))
            elif nm == "rep_all" and len(node.args) >= 2:
                f = strval(node.args[0]); lst = node.args[1]
                items = tuples_of(lst) if isinstance(lst, ast.List) else (named_lists.get(lst.id, []) if isinstance(lst, ast.Name) else [])
                for a, b in items: pairs.append((f, a, b))
        for ch in ast.iter_child_nodes(node): visit(ch)
    visit(tree)
    for gname in ("GLOBAL",):
        if gname in named_lists:
            for f in FILES[:5]:
                for a, b in named_lists[gname]: pairs.append((f, a, b))
    seen, out = set(), []
    for p in pairs:
        if p not in seen: seen.add(p); out.append(p)
    return out

core_strs = set(json.load(open(os.path.join(BASE, "hidden_files/w46/core-cjk-strings.json"), encoding="utf-8")))
core_texts = {f: open(os.path.join(W46, f), encoding="utf-8").read() for f in FILES}
for native in ["de","fr","es","it","pt","nl","ru","ja","ko","zh-tw"]:
    tp = os.path.join(W45, f"weekly-report-w45-en-{native}-build", "transform.py")
    pairs = extract(ast.parse(open(tp, encoding="utf-8").read()))
    table = {}
    for fname, old, new in pairs:
        if old in core_texts.get(fname, "") and old in core_strs:
            # avoid conflicting translations for same old
            if old in table and table[old] != new:
                print(f"CONFLICT {native}: {old!r} -> {table[old]!r} vs {new!r}")
            table[old] = new
    json.dump(table, open(os.path.join(BASE, "hidden_files/w46", f"kept-{native}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(native, "kept translations:", len(table), "| core strings still missing:", len(core_strs - set(table)))
