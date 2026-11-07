# -*- coding: utf-8 -*-
"""v2: resolve named lists/dicts (R, MAP, PER_FILE, CONTENT12...) for all W45 EN transforms."""
import ast, os, re, shutil, json

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
    env = {}  # name -> list[(old,new)] or dict{old:new} or dict{fname: list}
    pairs = []  # (fname_or_None, old, new)
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for t in node.targets:
                if not isinstance(t, ast.Name): continue
                if isinstance(node.value, ast.List):
                    env[t.id] = tuples_of(node.value)
                elif isinstance(node.value, ast.Dict):
                    d = {}
                    for k, v in zip(node.value.keys, node.value.values):
                        kk, vv = strval(k), None
                        if isinstance(v, ast.List): vv = tuples_of(v)
                        elif isinstance(v, ast.Name): vv = ("REF", v.id)
                        elif isinstance(v, ast.Dict):
                            vv = {strval(k2): strval(v2) for k2, v2 in zip(v.keys, v.values) if strval(k2) is not None and strval(v2) is not None}
                        else: vv = strval(v)
                        if kk is not None: d[kk] = vv
                    env[t.id] = d
    # R-style: (fname, old, new, exp) tuples in a list named R (or any list with 4-tuples)
    for name, val in env.items():
        pass
    # find R list directly from AST (4-tuples), incl. R += [...]
    for node in ast.walk(tree):
        if isinstance(node, ast.AugAssign) and isinstance(node.value, ast.List):
            for el in node.value.elts:
                if isinstance(el, ast.Tuple) and len(el.elts) >= 3:
                    f, a, b = strval(el.elts[0]), strval(el.elts[1]), strval(el.elts[2])
                    if f in FILES and a is not None and b is not None:
                        pairs.append((f, a, b))
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.List):
            for el in node.value.elts:
                if isinstance(el, ast.Tuple) and len(el.elts) >= 3:
                    f, a, b = strval(el.elts[0]), strval(el.elts[1]), strval(el.elts[2])
                    if f in FILES and a is not None and b is not None:
                        pairs.append((f, a, b))
    # MAP dicts: apply to all files
    for name, val in env.items():
        if isinstance(val, dict):
            for k, v in val.items():
                if isinstance(v, str):
                    for f in FILES: pairs.append((f, k, v))
                elif isinstance(v, list):
                    for a, b in v: pairs.append((k, a, b))
    # PER_FILE-like dicts mapping fname -> list (resolve REF names)
    for name, val in env.items():
        if isinstance(val, dict):
            for k, v in val.items():
                if isinstance(v, tuple) and len(v) == 2 and v[0] == "REF":
                    v = env.get(v[1], [])
                if isinstance(v, list) and k in FILES:
                    for a, b in v: pairs.append((k, a, b))
    # rep()/rep_all() calls
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
    # GLOBAL lists -> all content files
    for gname in ("GLOBAL",):
        if gname in named_lists:
            for f in FILES[:5]:
                for a, b in named_lists[gname]: pairs.append((f, a, b))
    seen, out = set(), []
    for p in pairs:
        if p not in seen: seen.add(p); out.append(p)
    return out

CJK = re.compile(r"[\u4e00-\u9fff]")
def remaining_cjk(text):
    out = set()
    for m in re.finditer(r"[^\n\"']*[\u4e00-\u9fff][^\n\"']*", text):
        out.add(m.group(0).strip())
    return out

for native in ["de","fr","es","it","pt","nl","ru","ja","ko","zh-tw"]:
    tp = os.path.join(W45, f"weekly-report-w45-en-{native}-build", "transform.py")
    tree = ast.parse(open(tp, encoding="utf-8").read())
    pairs = extract(tree)
    dst = os.path.join(BASE, "hidden_files", f"weekly-report-w46-en-{native}-build")
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(W46, dst, ignore=shutil.ignore_patterns("__pycache__"))
    texts = {f: open(os.path.join(dst, f), encoding="utf-8").read() for f in FILES}
    applied, skipped = 0, []
    for fname, old, new in pairs:
        if fname not in texts: continue
        if old in texts[fname]:
            texts[fname] = texts[fname].replace(old, new); applied += 1
        else: skipped.append((fname, old))
    for f in FILES:
        open(os.path.join(dst, f), "w", encoding="utf-8").write(texts[f])
    rem = {}
    for f in FILES:
        r = remaining_cjk(texts[f])
        if r: rem[f] = sorted(r)
    json.dump({"applied": applied, "skipped": skipped, "remaining": rem},
              open(os.path.join(BASE, "hidden_files/w46", f"bootstrap-{native}.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(f"{native}: pairs={len(pairs)} applied={applied} skipped={len(skipped)} rem-lines={sum(len(v) for v in rem.values())}")
