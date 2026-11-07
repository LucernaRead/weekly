import ast, json, sys
build=sys.argv[1]
files=["content12.py","content34.py","content56.py","content7.py","content8.py"]
entries=[]
for fn in files:
    src=open(f"{build}/{fn}",encoding="utf-8").read()
    tree=ast.parse(src)
    for stmt in tree.body:
        for node in ast.walk(stmt):
            if isinstance(node, ast.Call):
                f=node.func
                name=f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else "?")
                if name in ("ex","match_set"):
                    args=node.args
                    def lit(a):
                        try: return ast.literal_eval(a)
                        except Exception: return "<expr>"
                    entries.append({"file":fn,"lineno":node.lineno,"name":name,
                        "level":lit(args[0]),"kind":lit(args[1]),
                        "key":lit(args[2]) if name=="ex" else None,
                        "note":lit(args[3]) if name=="ex" else None,
                        "stem":lit(args[4]) if name=="ex" else None,
                        "lefts":lit(args[2]) if name=="match_set" else None,
                        "rights":lit(args[3]) if name=="match_set" else None,
                        "keys":lit(args[4]) if name=="match_set" else None,
                        "notes":lit(args[5]) if name=="match_set" else None})
entries.sort(key=lambda e:(files.index(e["file"]), e["lineno"]))
n=0; lines=[]; levels={}
for e in entries:
    if e["name"]=="ex":
        n+=1; e["n"]=n; levels[e["level"]]=levels.get(e["level"],0)+1
        lines.append(f"{n}. [{e['level']} {e['kind']}] key={e['key']!r} note={e['note']!r} stem={e['stem']!r} ({e['file']}:{e['lineno']})")
    else:
        nums=list(range(n+1,n+5)); e["nums"]=nums
        for k,lf,nt in zip(e["keys"],e["lefts"],e["notes"]): levels[e["level"]]=levels.get(e["level"],0)+1
        lines.append(f"{nums[0]}-{nums[-1]}. [{e['level']} {e['kind']}] lefts={e['lefts']} rights={e['rights']} keys={e['keys']} notes={e['notes']} ({e['file']}:{e['lineno']})")
        n+=4
open(sys.argv[2],"w",encoding="utf-8").write("\n".join(lines)+f"\nTOTAL={n} levels={levels} calls={len(entries)}\n")
print(f"TOTAL={n} levels={levels} calls={len(entries)}")
json.dump(entries, open(sys.argv[3],"w",encoding="utf-8"), ensure_ascii=False, indent=1)
