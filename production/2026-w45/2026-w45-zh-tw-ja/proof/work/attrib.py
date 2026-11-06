#!/usr/bin/env python3
# Own attribution: every added/removed rendered string must be explained by
# the transform (new/old strings), furniture instantiation, gloss/P8 prefixes,
# or core strings themselves. Pure-Hanzi added strings get a separate verdict.
import ast, json, os, re
from collections import Counter
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
W = os.path.join(GOAL, "hidden_files/w45/zh-tw-ja-reproof/work")
EDB = os.path.join(GOAL, "hidden_files/weekly-report-w45-zh-tw-ja-build")
COREB = os.path.join(GOAL, "hidden_files/weekly-report-w45-zhtw-build")
CORE_SVG = os.path.join(GOAL, "files/weekly-report-w45-zhtw-core/svg")
ED_SVG = os.path.join(GOAL, "files/weekly-report-w45-zh-tw-ja/svg")
import xml.etree.ElementTree as ET
def texts(d):
    out={}
    for fn in sorted(os.listdir(d)):
        if fn.endswith('.svg'):
            t=ET.parse(os.path.join(d,fn))
            out[fn]=[''.join(e.itertext()) for e in t.getroot().iter() if e.tag.endswith('text')]
    return out
core_txt, ed_txt = texts(CORE_SVG), texts(ED_SVG)
core_all = "".join(t for v in core_txt.values() for t in v)

# transform rep pairs via AST
tree = ast.parse(open(os.path.join(EDB,'transform.py'), encoding='utf-8').read())
olds, news = [], []
for node in ast.walk(tree):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id=='rep' and len(node.args)>=3:
        a=node.args
        if all(isinstance(x, ast.Constant) and isinstance(x.value,str) for x in a[:3]):
            olds.append(a[1].value); news.append(a[2].value)
print(f"transform rep pairs: {len(olds)} (first proof counted 280 rep + 6 repoints = 286 log lines)")
# conversion-logic check
tsrc = open(os.path.join(EDB,'transform.py'), encoding='utf-8').read()
for pat in ['OpenCC','opencc','s2t','t2s','mapping','convert(']:
    print(f"  conversion token {pat!r}: {'FOUND' if pat in tsrc else 'absent'}")
print(f"  'opencc' case-insensitive: {'opencc' in tsrc.lower()}")

def norm(s):
    table = str.maketrans({"？":"?","！":"!","：":":","；":";","，":",","。":".","、":",","（":"(","）":")","＋":"+","～":"~","－":"-","／":"/","「":"","」":"","『":"","』":"","・":".","…":"..."})
    return re.sub(r"\s+","", s.translate(table).replace("{NCHARS}","138"))
new_all_ns = norm("".join(news)); core_all_n = norm(core_all)
inst_new = "".join(f"{n}ページ(全8ページ)" for n in range(1,9)) + "".join(f"—{n}ページ—" for n in range(1,9))
inst_old = "".join(f"第{n}版/共8版" for n in range(1,9)) + "".join(f"—Page{n}—" for n in range(1,9))
old_all_ns = norm("".join(olds))

fd = json.load(open(os.path.join(W,'freeze-diff-fix.json')))
bad_added, bad_removed = [], []
for pg, d in fd['pages'].items():
    for s in d['added_strings']:
        st = s['text']; nst = norm(st)
        nst2 = re.sub(r"^解説—","",nst)
        nst2 = re.sub(r"^\d+\.\s*(✓\s*|.*?—\s*)","",nst2)
        nst2 = re.sub(r"^モデル解答:","",nst2)
        nst2 = re.sub(r"\s*\(p\.\s*\d\)$","",nst2)
        if nst in new_all_ns or nst2 in new_all_ns or nst in core_all_n or nst in inst_new or nst2 in core_all_n:
            continue
        # wrapped fragments: a rendered line may be a substring of a new string
        if nst2 and (nst2 in new_all_ns or nst in new_all_ns):
            continue
        bad_added.append((pg, st[:80]))
    for s in d['removed_strings']:
        st = s['text']; nst = norm(st)
        nst2 = re.sub(r"^Notes｜","",nst)
        nst2 = re.sub(r"^\d+\.\s*(✓\s*|.*?—\s*)","",nst2)
        nst2 = re.sub(r"\s*\(p\.\s*\d\)$","",nst2)
        if nst in old_all_ns or nst2 in old_all_ns or nst in core_all_n or nst in inst_old or nst2 in core_all_n:
            continue
        bad_removed.append((pg, st[:80]))
print(f"B1 unattributed ADDED: {len(bad_added)} {bad_added[:10]}")
print(f"B2 unattributed REMOVED: {len(bad_removed)} {bad_removed[:10]}")

# Pure-Hanzi added strings: added string with Hanzi but no kana/Latin -> must be in core or furniture
KANA = re.compile(r"[\u3040-\u30ff]"); LAT = re.compile(r"[A-Za-z]"); HAN = re.compile(r"[\u4e00-\u9fff]")
susp=[]
for pg, d in fd['pages'].items():
    for s in d['added_strings']:
        st=s['text']
        if HAN.search(st) and not KANA.search(st) and not LAT.search(st):
            if norm(st) not in core_all_n and norm(st) not in new_all_ns:
                susp.append((pg, st[:80]))
print(f"PURE-HANZI added strings unattributed: {len(susp)} {susp[:10]}")
# also: any added Hanzi char not in core set? (per-char, for the record)
core_han = set(c for c in core_all if HAN.match(c))
new_han_chars = set()
for pg, d in fd['pages'].items():
    for s in d['added_strings']:
        new_han_chars |= set(c for c in s['text'] if HAN.match(c))
print(f"added-Hanzi chars outside core Hanzi set: {sorted(new_han_chars - core_han)}")

# A1/A2 source-level (own, simplified): olds absent from edition build sources; core literals kept
def literals(d, files):
    out={}
    for fn in files:
        src=open(os.path.join(d,fn),encoding='utf-8').read(); tree=ast.parse(src)
        out[fn]=[n.value for n in ast.walk(tree) if isinstance(n, ast.Constant) and isinstance(n.value,str)]
    return out
FILES=["content12.py","content34.py","content56.py","content7.py","content8.py"]
core_lit=literals(COREB,FILES)
ed_src={fn: open(os.path.join(EDB,fn),encoding='utf-8').read() for fn in FILES+["bslib4.py"]}
miss=[(fn,s[:60]) for fn in set() for s in []]
# A1: each old string must NOT remain in its file (need file per rep: re-derive)
tree2 = ast.parse(tsrc); pairs=[]
for node in ast.walk(tree2):
    if isinstance(node, ast.Call) and isinstance(node.func, ast.Name) and node.func.id=='rep' and len(node.args)>=3:
        a=node.args
        if all(isinstance(x, ast.Constant) and isinstance(x.value,str) for x in a[:3]):
            pairs.append((a[0].value, a[1].value))
a1=[(fn,s[:60]) for fn,s in pairs if s in ed_src.get(fn,'')]
print(f"A1 olds still present: {len(a1)} {a1[:5]}")
ed_lit=literals(EDB,FILES+["bslib4.py"]); oldmap={}
for fn,s in pairs: oldmap.setdefault(fn,[]).append(s)
kept=[]
for fn, lst in core_lit.items():
    cc, ec = Counter(lst), Counter(ed_lit.get(fn,[]))
    for s in lst:
        if not s.strip(): continue
        if any(s==o or o in s or s in o for o in oldmap.get(fn,[])): continue
        if s in ("serif","sans","middle","end") or s.startswith("~") or s.startswith("#"): continue
        if ec[s] < cc[s]: kept.append((fn,s[:70])); ec[s]+=1
print(f"A2 core literals lost: {len(kept)} {kept[:5]}")
