#!/usr/bin/env python3
"""Round 2: STATIC key registry (ast only, never executes build code).
Ordered events sorted by source line within each file, files in run order.
.ex(level,typ,key,note,body); match_set(level,typ,lefts,rights,keys,notes);
reg_ex(level,typ,key,note); [reg_ex(lv,typ,k,nt) for lv,k,nt in DEFS]."""
import ast, pathlib, json, sys
BASE = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w46-de-build"
FILES = ["content12.py","content34.py","content56.py","content7.py","content8.py"]
def S(n):
    if isinstance(n, ast.Constant) and isinstance(n.value, str): return n.value
    return None
events=[]  # (file_order, lineno, seq, dict)
for fo, fn in enumerate(FILES):
    tree = ast.parse((BASE/fn).read_text(encoding="utf-8"))
    defs={}
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign) and len(node.targets)==1 and isinstance(node.targets[0], ast.Name) and isinstance(node.value, ast.List):
            rows=[]
            for elt in node.value.elts:
                if isinstance(elt, ast.Tuple) and len(elt.elts)>=3:
                    rows.append((S(elt.elts[0]),S(elt.elts[1]),S(elt.elts[2])))
            if rows and all(all(r) for r in rows): defs[node.targets[0].id]=rows
    seq=[0]
    def add(lineno, rec):
        seq[0]+=1; events.append((fo,lineno,seq[0],rec))
    for node in ast.walk(tree):
        if isinstance(node, ast.ListComp):
            call=node.elt
            if isinstance(call, ast.Call) and isinstance(call.func, ast.Name) and call.func.id=="reg_ex":
                for gen in node.generators:
                    if isinstance(gen.iter, ast.Name) and gen.iter.id in defs:
                        for (lv,k,nt) in defs[gen.iter.id]:
                            add(node.lineno, {"key":k,"note":nt,"stem":"CLOZE/DIALOGUE option set","file":fn,"line":node.lineno,"kind":"comprehension:"+gen.iter.id,"level":lv})
        elif isinstance(node, ast.Call):
            # skip calls that are the elt of a ListComp (handled above)
            f=node.func; name=f.attr if isinstance(f, ast.Attribute) else (f.id if isinstance(f, ast.Name) else None)
            if name=="ex" and len(node.args)>=4 and S(node.args[0]):
                add(node.lineno, {"key":S(node.args[2]),"note":S(node.args[3]),"stem":S(node.args[4]) if len(node.args)>4 else None,"file":fn,"line":node.lineno,"kind":"ex","level":S(node.args[0])})
            elif name=="match_set" and len(node.args)>=6 and S(node.args[0]):
                keys=node.args[4]; notes=node.args[5]; lefts=node.args[2]; rights=node.args[3]
                kl=[S(e) for e in keys.elts] if isinstance(keys, ast.List) else []
                nl=[S(e) for e in notes.elts] if isinstance(notes, ast.List) else []
                ll=[S(e) for e in lefts.elts] if isinstance(lefts, ast.List) else []
                rl=[S(e) for e in rights.elts] if isinstance(rights, ast.List) else []
                for k,nt,lf in zip(kl,nl,ll):
                    add(node.lineno, {"key":k,"note":nt,"stem":"MATCH left="+str(lf)+" | rights="+str(rl),"file":fn,"line":node.lineno,"kind":"match_set","level":S(node.args[0])})
            elif name=="reg_ex" and len(node.args)>=3 and S(node.args[0]):
                add(node.lineno, {"key":S(node.args[2]),"note":S(node.args[3]) if len(node.args)>3 else "","stem":None,"file":fn,"line":node.lineno,"kind":"reg_ex","level":S(node.args[0])})
events.sort(key=lambda e:(e[0],e[1],e[2]))
regs=[]
for i,(fo,ln,sq,rec) in enumerate(events,1):
    rec["n"]=i; regs.append(rec)
print("total:", len(regs), file=sys.stderr)
from collections import Counter
print(Counter(r["level"] for r in regs), file=sys.stderr)
json.dump(regs, open(sys.argv[1],"w",encoding="utf-8"), indent=1, ensure_ascii=False)
for r in regs: print(r["n"], r["level"], r["key"], "|", r["note"], "|", (r["stem"] or "")[:80])
