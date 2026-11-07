# -*- coding: utf-8 -*-
"""For each W45 EN fan-out transform, report pair coverage against W46 core build files."""
import ast, os, json, re
W46 = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-en-build")
W45 = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files")
CORE_FILES = ["content12.py","content34.py","content56.py","content7.py","content8.py","bslib4.py"]
core = {f: open(os.path.join(W46,f), encoding="utf-8").read() for f in CORE_FILES}

def strval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str): return node.value
    if isinstance(node, ast.JoinedStr):
        return "".join(p.value if isinstance(p, ast.Constant) else "{...}" for p in node.values)
    return None

def collect_pairs(tree):
    """Return list of (file, old, new) from rep/rep_all/TYPE_MAP/INSTR_MAP usage + bslib reps."""
    pairs = []  # (file, old, new)
    # name -> list of (old,new) for module-level list assignments
    lists = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.List):
            for t in node.targets:
                if isinstance(t, ast.Name) and t.id.isupper():
                    items = []
                    for el in node.value.elts:
                        if isinstance(el, ast.Tuple) and len(el.elts) == 2:
                            a, b = strval(el.elts[0]), strval(el.elts[1])
                            if a is not None and b is not None: items.append((a, b))
                    lists[t.id] = items
    # walk statements in order
    def visit(node, curfile=None):
        if isinstance(node, ast.Call):
            fn = node.func
            name = fn.attr if isinstance(fn, ast.Attribute) else (fn.id if isinstance(fn, ast.Name) else "")
            if name == "rep" and len(node.args) >= 3:
                f, o, n = strval(node.args[0]), strval(node.args[1]), strval(node.args[2])
                if f and o is not None: pairs.append((f, o, n))
            elif name == "rep_all" and len(node.args) >= 2:
                f = strval(node.args[0])
                lst = node.args[1]
                items = []
                if isinstance(lst, ast.List):
                    for el in lst.elts:
                        if isinstance(el, ast.Tuple) and len(el.elts) == 2:
                            a, b = strval(el.elts[0]), strval(el.elts[1])
                            if a is not None: items.append((a, b))
                elif isinstance(lst, ast.Name):
                    items = lists.get(lst.id, [])
                for a, b in items:
                    pairs.append((f, a, b))
            elif name == "apply_shared" or (name in ("rep",) ):
                pass
        for ch in ast.iter_child_nodes(node):
            visit(ch, curfile)
    visit(tree)
    # TYPE_MAP/INSTR_MAP applied to all content files (apply_shared pattern)
    for lname in ("TYPE_MAP", "INSTR_MAP"):
        if lname in lists:
            for f in CORE_FILES[:5]:
                for a, b in lists[lname]:
                    pairs.append((f, a, b))
    return pairs

report = {}
for native in ["de","fr","es","it","pt","nl","ru","ja","ko","zh-tw"]:
    tp = os.path.join(W45, f"weekly-report-w45-en-{native}-build", "transform.py")
    if not os.path.exists(tp):
        report[native] = {"error": "no transform.py"}; continue
    tree = ast.parse(open(tp, encoding="utf-8").read())
    pairs = collect_pairs(tree)
    kept, missing = [], []
    for f, o, n in pairs:
        content = core.get(f, "")
        if o in content: kept.append((f, o, n))
        else: missing.append((f, o, n))
    report[native] = {"pairs": len(pairs), "kept": len(kept), "missing": len(missing),
                      "missing_olds": [o for _, o, _ in missing][:999]}
    print(f"{native}: pairs={len(pairs)} kept={len(kept)} missing={len(missing)}")
json.dump(report, open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/transform-coverage.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
