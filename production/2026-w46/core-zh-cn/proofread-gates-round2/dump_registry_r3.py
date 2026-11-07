import ast, json, sys
build = sys.argv[1]
files = ["content12.py","content34.py","content56.py","content7.py","content8.py"]
out=[]
for fn in files:
    src=open(f"{build}/{fn}",encoding="utf-8").read()
    tree=ast.parse(src)
    for node in ast.walk(tree):
        if isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            f=node.value.func
            name = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else "?")
            args=node.value.args
            def lit(a):
                try: return ast.literal_eval(a)
                except Exception: return "<expr>"
            if name=="ex":
                # ex(level, kind, key, note, stem, instr=..., ...)
                out.append({"file":fn,"type":"ex","level":lit(args[0]),"kind":lit(args[1]),"key":lit(args[2]),"note":lit(args[3]),"stem":lit(args[4])})
            elif name=="match_set":
                out.append({"file":fn,"type":"match","level":lit(args[0]),"kind":lit(args[1]),"lefts":lit(args[2]),"rights":lit(args[3]),"keys":lit(args[4]),"notes":lit(args[5])})
            elif name in ("choice","choose","mc","qa"):
                out.append({"file":fn,"type":name,"raw":[lit(a) for a in args]})
print(f"entries={len(out)} ex={sum(1 for e in out if e['type']=='ex')} match={sum(1 for e in out if e['type']=='match')} other={[e['type'] for e in out if e['type'] not in ('ex','match')]}", file=sys.stderr)
json.dump(out, open(sys.argv[2],"w",encoding="utf-8"), ensure_ascii=False, indent=1)
