import re, ast, xml.etree.ElementTree as ET
BASE="/home/hatch/workspace/goals/lucernaread-social-media-operations"
def texts(path):
    tree=ET.parse(path); return [''.join(el.itertext()) for el in tree.iter() if el.tag.endswith('text')]
pages=["p1-pyoji","p2-saenghwal","p3-munhwa","p4-seupocheu","p5-cheongnyeon","p6-gipi","p7-mal","p8-siheom"]
ed=[]
for p in pages: ed+=texts(f"{BASE}/files/weekly-report-w45-ko-ja/svg/{p}.svg")
edjoined="\n".join(ed)
# parse transform.py REPL dict: find dict literal assignments? print structure first
src=open(f"{BASE}/hidden_files/weekly-report-w45-ko-ja-build/transform.py", encoding='utf-8').read()
# REPL dict is a large dict literal; extract all string literals that are keys? Use AST: find Dict nodes
tree=ast.parse(src)
dicts=[n for n in ast.walk(tree) if isinstance(n, ast.Dict)]
print(f"dict literals: {len(dicts)}")
for d in dicts:
    print(f"  dict with {len(d.keys)} entries")
# take largest dict as REPL
repl=max(dicts, key=lambda d: len(d.keys))
keys=[]
for k,v in zip(repl.keys, repl.values):
    try: keys.append((ast.literal_eval(k), ast.literal_eval(v)))
    except Exception: pass
print(f"REPL entries parsed: {len(keys)}")
HAN=re.compile(r'[\u4E00-\u9FFF]+')
residue=[]
for k,v in keys:
    # verbatim key in edition?
    if k in edjoined: residue.append(("VERBATIM",k))
    # Han runs of key present as standalone node text? check each Han run >=2 chars appearing in edition nodes as substring but not in value
    for run in set(HAN.findall(k)):
        if len(run)>=2 and run in edjoined and run not in v:
            # only flag if run is not a shared/Japanese word: check if run appears in a kana-containing node
            ctx=[t for t in ed if run in t]
            kana_ctx=any(any('\u3040'<=c<='\u30FF' for c in t) for t in ctx)
            if not kana_ctx:
                residue.append(("HANRUN-NOKANA",run,k,ctx[:1]))
print(f"residue candidates: {len(residue)}")
for r in residue[:40]: print(r)
# Also: REPL keys containing Hangul? (should be none except? ) and values
print("keys with Hangul:", sum(1 for k,v in keys if any('\uAC00'<=c<='\uD7A4' for c in k)))
print("sample keys:", keys[:3])
