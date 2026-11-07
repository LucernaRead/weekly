import ast, importlib.util, sys, hashlib, pathlib
B = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ko-ru-build"
FIX = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ko-ru-fix"

def load_transform(path):
    spec = importlib.util.spec_from_file_location("tmod_"+path.stem+str(abs(hash(str(path)))%99999), path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
    return m

cur = load_transform(B/"transform.py")
old = load_transform(FIX/"transform-before.py")
print("current transform sha:", hashlib.sha256((B/"transform.py").read_bytes()).hexdigest())
print("old transform sha:", hashlib.sha256((FIX/"transform-before.py").read_bytes()).hexdigest())
print("REPL current:", len(cur.REPL), "old:", len(old.REPL))
print("REPL keys equal:", set(cur.REPL)==set(old.REPL))
diff = [(k, old.REPL.get(k), cur.REPL.get(k)) for k in set(old.REPL)|set(cur.REPL) if old.REPL.get(k)!=cur.REPL.get(k)]
print("REPL value diffs:", len(diff))
for d in diff: print("  DIFF", d)
print("FIX2FIX3 current:", len(cur.FIX2FIX3))
print("old has FIX2FIX3?", hasattr(old, "FIX2FIX3"))

def ast_dict(path, varname="FIX"):
    tree = ast.parse((path).read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id==varname for t in node.targets):
            return ast.literal_eval(node.value)
    raise SystemExit(f"no {varname} in {path}")

f2 = ast_dict(B/"fix2.py"); f3 = ast_dict(B/"fix3.py")
print("fix2 entries:", len(f2), "fix3 entries:", len(f3))
combined = dict(f2); combined.update(f3)
print("combined distinct keys:", len(combined), "overlap f2/f3 keys:", len(set(f2)&set(f3)))
fx = cur.FIX2FIX3
print("FIX2FIX3 == combined keys:", set(fx)==set(combined))
md = [(k, combined.get(k), fx.get(k)) for k in set(combined)|set(fx) if combined.get(k)!=fx.get(k)]
print("FIX2FIX3 vs fix2+fix3 value diffs:", len(md))
for d in md: print("  MISMATCH", repr(d[0]), "fix=", repr(d[1]), "transform=", repr(d[2]))
# per-entry: show src/dst short prefixes + check for mojibake/replacement chars
for i,(k,v) in enumerate(sorted(fx.items(), key=lambda kv: kv[0]),1):
    bad = "�" in k or "�" in v
    print(f"  FX{i} badchar={bad} src={k[:50]!r} dst={v[:50]!r}")
# KIT presence check
kit = (pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ko-ru/WEEKLY-KIT.md").read_text(encoding="utf-8")
for k,v in fx.items():
    print("  KIT src-present:", k[:30] in kit, "dst-present:", v[:30] in kit, "|", k[:30])
