#!/usr/bin/env python3
"""Round 2: STATIC registry parse (ast only, never executes build code).
Counts reg_ex/.ex/.match_set registrations in run order content12,34,56,7,8.
Expands *_defs list literals used in comprehensions. Prints numbered levels."""
import ast, pathlib, json, sys
BASE = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-de-build"
FILES = ["content12.py","content34.py","content56.py","content7.py","content8.py"]
regs = []  # (level, file, lineno, kind)

def const_str(n):
    return n.value if isinstance(n, ast.Constant) and isinstance(n.value, str) else None

for fn in FILES:
    src = (BASE/fn).read_text(encoding="utf-8")
    tree = ast.parse(src)
    # collect *_defs list literals: name -> list of tuple first-elements
    defs = {}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0], ast.Name):
            if isinstance(node.value, ast.List):
                rows=[]
                for elt in node.value.elts:
                    if isinstance(elt, ast.Tuple) and elt.elts:
                        rows.append(const_str(elt.elts[0]))
                if rows and all(rows):
                    defs[node.targets[0].id]=rows
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            f=node.func
            name = f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else None)
            if name=="ex" and node.args:
                lv=const_str(node.args[0])
                if lv: regs.append((lv,fn,node.lineno,"ex"))
            elif name=="match_set" and node.args:
                lv=const_str(node.args[0])
                # keys arg: find List arg (3rd positional after lefts/rights?) - signature (level,typ,lefts,rights,keys,notes)
                nkeys=None
                for a in node.args:
                    pass
                if len(node.args)>=5 and isinstance(node.args[4], ast.List):
                    nkeys=len(node.args[4].elts)
                if lv and nkeys: regs.extend([(lv,fn,node.lineno,"match_set")]*nkeys)
            elif name=="reg_ex" and node.args:
                lv=const_str(node.args[0])
                if lv:
                    regs.append((lv,fn,node.lineno,"reg_ex"))
                else:
                    # comprehension variable: handled below via ListComp walk; skip bare
                    pass
        if isinstance(node, ast.ListComp):
            # [reg_ex(lv, ...) for lv,k,nt in <defs>]
            call=node.elt
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id=="reg_ex":
                for gen in node.generators:
                    if isinstance(gen.iter, ast.Name) and gen.iter.id in defs:
                        for lv in defs[gen.iter.id]:
                            regs.append((lv,fn,node.lineno,"comprehension:"+gen.iter.id))
print("total registrations:", len(regs))
from collections import Counter
print(Counter(l for l,_,_,_ in regs))
for i,(lv,fn,ln,kind) in enumerate(regs,1):
    print(i, lv, fn, ln, kind)
pathlib.Path(sys.argv[1]).write_text(json.dumps([{"n":i,"level":lv,"file":fn,"line":ln,"kind":kind} for i,(lv,fn,ln,kind) in enumerate(regs,1)],indent=1,ensure_ascii=False),encoding="utf-8")
