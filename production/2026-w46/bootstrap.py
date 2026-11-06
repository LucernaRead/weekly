# -*- coding: utf-8 -*-
"""Bootstrap W46 fan-out builds: copy W46 core, apply W45 transform pairs that still match, report skips + remaining CJK."""
import ast, os, re, shutil, sys, json

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
W46 = os.path.join(BASE, "hidden_files/weekly-report-w46-en-build")
W45 = os.path.join(BASE, "hidden_files")
FILES = ["content12.py","content34.py","content56.py","content7.py","content8.py","bslib4.py"]

def strval(node):
    if isinstance(node, ast.Constant) and isinstance(node.value, str): return node.value
    if isinstance(node, ast.JoinedStr):
        return "".join(p.value if isinstance(p, ast.Constant) else "{...}" for p in node.values)
    return None

def extract_pairs(tree):
    """Return ordered list of (file_or_None, old, new). file from PER_FILE dict keys / rep first arg / GLOBAL (None=all)."""
    pairs = []
    # dict literals: PER_FILE = {"content12.py": [...], ...}
    for node in ast.walk(tree):
        if isinstance(node, ast.Dict):
            for k, v in zip(node.keys, node.values):
                fname = strval(k)
                if fname and isinstance(v, ast.List):
                    for el in v.elts:
                        if isinstance(el, ast.Tuple) and len(el.elts) >= 2:
                            a, b = strval(el.elts[0]), strval(el.elts[1])
                            if a is not None and b is not None: pairs.append((fname, a, b))
        if isinstance(node, ast.Assign):
            # list assigned to a name, later used in rep_all(fname, NAME)
            pass
    # rep_all(fname, LISTVAR) / rep_all(fname, [tuples]) and rep(fname, old, new)
    # collect named lists first
    named = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.List):
            for t in node.targets:
                if isinstance(t, ast.Name):
                    items = []
                    for el in node.value.elts:
                        if isinstance(el, ast.Tuple) and len(el.elts) >= 2:
                            a, b = strval(el.elts[0]), strval(el.elts[1])
                            if a is not None and b is not None: items.append((a, b))
                    named[t.id] = items
    def visit(node):
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
                        if isinstance(el, ast.Tuple) and len(el.elts) >= 2:
                            a, b = strval(el.elts[0]), strval(el.elts[1])
                            if a is not None: items.append((a, b))
                elif isinstance(lst, ast.Name):
                    items = named.get(lst.id, [])
                for a, b in items:
                    pairs.append((f, a, b))
        for ch in ast.iter_child_nodes(node):
            visit(ch)
    visit(tree)
    # GLOBAL list applied to all content files
    for lname in ("GLOBAL",):
        if lname in named:
            for f in FILES[:5]:
                for a, b in named[lname]:
                    pairs.append((f, a, b))
    # dedupe preserving order
    seen, out = set(), []
    for p in pairs:
        if p not in seen:
            seen.add(p); out.append(p)
    return out

CJK = re.compile(r"[\u4e00-\u9fff]")
def remaining_cjk(text):
    strs = set()
    for m in re.finditer(r"[^\n\"']*[\u4e00-\u9fff][^\n\"']*", text):
        strs.add(m.group(0).strip())
    return strs

for native in ["de","fr","es","it","pt","nl","ru","ja","ko","zh-tw"]:
    tp = os.path.join(W45, f"weekly-report-w45-en-{native}-build", "transform.py")
    if not os.path.exists(tp):
        print(native, "NO TRANSFORM"); continue
    tree = ast.parse(open(tp, encoding="utf-8").read())
    pairs = extract_pairs(tree)
    dst = os.path.join(BASE, "hidden_files", f"weekly-report-w46-en-{native}-build")
    if os.path.exists(dst): shutil.rmtree(dst)
    shutil.copytree(W46, dst, ignore=shutil.ignore_patterns("__pycache__"))
    applied, skipped = 0, []
    texts = {}
    for f in FILES:
        texts[f] = open(os.path.join(dst, f), encoding="utf-8").read()
    for fname, old, new in pairs:
        if fname is None: continue
        if fname not in texts: continue
        # skip OUT repoint / VOL pairs pointing at w45 (handled separately)
        if "weekly-report-w45" in old or "VOL.2" in old and "VOL.3" not in new:
            pass
        if old in texts[fname]:
            texts[fname] = texts[fname].replace(old, new)
            applied += 1
        else:
            skipped.append(old)
    for f in FILES:
        open(os.path.join(dst, f), "w", encoding="utf-8").write(texts[f])
    rem = {}
    for f in FILES:
        r = remaining_cjk(texts[f])
        if r: rem[f] = sorted(r)
    json.dump({"applied": applied, "skipped": skipped, "remaining": rem},
              open(os.path.join(BASE, "hidden_files/w46", f"bootstrap-{native}.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    nrem = sum(len(v) for v in rem.values())
    print(f"{native}: pairs={len(pairs)} applied={applied} skipped={len(skipped)} remaining-CJK-lines={nrem}")
