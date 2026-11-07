# Independent gloss audit (own implementation, scratch inputs only)
import ast, glob, os, re, sys
SCR = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ko-ru-proof/work/scratch")
CORE_SVG, ED_SVG = f"{SCR}/core/svg", f"{SCR}/edition/svg"
CORE_BUILD, ED_BUILD = f"{SCR}/corebuild", f"{SCR}/build"

def texts_of(path):
    s = open(path, encoding="utf-8").read()
    return [(float(x), float(y), t) for x, y, t in re.findall(r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>', s)]

def boxes(svgdir, prefix):
    out = {}
    for path in sorted(glob.glob(os.path.join(svgdir, "*.svg"))):
        nodes = texts_of(path)
        cur = None; res = []
        for x, y, t in nodes:
            if t.startswith(prefix):
                if cur: res.append(cur)
                cur = {"x": x, "y": y, "txt": t}
            elif cur is not None and abs(x - cur["x"]) < 0.01 and 20 <= y - cur["y"] <= 40:
                cur["y"] = y; cur["txt"] += t
            else:
                if cur: res.append(cur)
                cur = None
        if cur: res.append(cur)
        items = []
        for b in res:
            body = b["txt"][len(prefix):]
            items.append([s.strip() for s in body.split("·") if s.strip()])
        out[os.path.basename(path)] = items
    return out

cb = boxes(CORE_SVG, "译注｜"); eb = boxes(ED_SVG, "Пояснение — ")
print("== rendered gloss boxes (items per box) ==")
tot_c = tot_e = 0
for pg in sorted(cb):
    print(f"{pg}: core {[len(v) for v in cb[pg]]} sum={sum(len(v) for v in cb[pg])} | ed {[len(v) for v in eb[pg]]} sum={sum(len(v) for v in eb[pg])} equal={cb[pg] and [len(v) for v in cb[pg]]==[len(v) for v in eb[pg]]}")
    tot_c += sum(len(v) for v in cb[pg]); tot_e += sum(len(v) for v in eb[pg])
print(f"TOTAL gloss items core={tot_c} ed={tot_e}")
print("== headword check: Korean headword before '=' in each gloss item, core vs ed ==")
bad = 0
for pg in sorted(cb):
    for bi, (ci, ei) in enumerate(zip(cb[pg], eb[pg])):
        for j, (cseg, eseg) in enumerate(zip(ci, ei)):
            ch = cseg.split("=")[0].strip() if "=" in cseg else cseg.split("＝")[0].strip()
            eh = eseg.split("=")[0].strip() if "=" in eseg else eseg
            if ch != eh:
                print(f"  HEADWORD DIFF {pg} box{bi} item{j}: core={ch!r} ed={eh!r}"); bad += 1
print("headword diffs:", bad)

def call_stats(builddir):
    per = {}; calls = {}
    for fn in ["content12.py","content34.py","content56.py","content7.py","content8.py"]:
        tree = ast.parse(open(os.path.join(builddir, fn), encoding="utf-8").read())
        g = gl = 0; gl_args = []; nonconst = 0
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call): continue
            attr = getattr(node.func, "attr", None)
            if attr not in ("gloss","glossline") or not node.args: continue
            arg = node.args[0]
            if not isinstance(arg, ast.Constant) or not isinstance(arg.value, str):
                nonconst += 1; continue
            segs = [s for s in arg.value.split("·") if s.strip()]
            if attr == "gloss": g += len(segs)
            else: gl += len(segs); gl_args.append(arg.value)
        per[fn] = (g, gl); calls[fn] = gl_args
    return per, calls, nonconst

for label, bd in [("CORE", CORE_BUILD), ("ED", ED_BUILD)]:
    per, calls, nc = call_stats(bd)
    print(f"== call-string {label} (gloss segs, glossline segs) ==")
    for fn,(g,gl) in per.items(): print(f"  {fn}: gloss={g} glossline={gl} sum={g+gl}")
    print(f"  TOTAL gloss={sum(v[0] for v in per.values())} gloss+glossline={sum(v[0]+v[1] for v in per.values())} nonconst_calls={nc}")
    print(f"  glossline calls: content12={len(calls['content12.py'])} content34={len(calls['content34.py'])} content56={len(calls['content56.py'])} content7={len(calls['content7.py'])} content8={len(calls['content8.py'])}")

# rendered presence of every ED glossline arg: search joined page texts
print("== ED glossline rendered presence (per content file, page found) ==")
_, ed_calls, _ = call_stats(ED_BUILD)
page_text = {}
for path in sorted(glob.glob(os.path.join(ED_SVG, "*.svg"))):
    txt = " ".join(t for _,_,t in texts_of(path))
    page_text[os.path.basename(path)] = re.sub(r"\s+", " ", txt)
file_pages = {"content12.py": ["p1-pyoji.svg","p2-saenghwal.svg"], "content34.py": ["p3-munhwa.svg","p4-seupocheu.svg"],
              "content56.py": ["p5-cheongnyeon.svg","p6-gipi.svg"], "content7.py": ["p7-mal.svg"], "content8.py": ["p8-siheom.svg"]}
for fn, args in ed_calls.items():
    for a in args:
        norm = re.sub(r"\s+", " ", a).strip()
        found = [pg for pg in file_pages[fn] if norm in page_text[pg]]
        # fallback: first 40 chars
        found2 = [] if found else [pg for pg in file_pages[fn] if norm[:40] in page_text[pg]]
        print(f"  {fn} :: {norm[:90]!r} -> pages={found or found2 or 'NOT-FOUND'}")
