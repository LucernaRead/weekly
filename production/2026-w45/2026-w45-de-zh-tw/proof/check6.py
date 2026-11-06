import re, pathlib
G=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
def gloss_calls(d):
    out={}
    for f in sorted(pathlib.Path(d).glob("content*.py")):
        src=f.read_text(encoding="utf-8")
        # gloss( ... ) calls: find balanced-ish by regex non-greedy across lines until '")' ? Use ast-free: find 'gloss(' then scan string literals
        for m in re.finditer(r'gloss\((.*?)\)', src, re.S):
            arg=m.group(1)
            # extract string literal contents
            lits=re.findall(r'"([^"]*)"|"((?:[^"\\]|\\.)*)"', arg)
            s="".join(a or b for a,b in lits)
            out.setdefault(f.name,[]).append(s)
    return out
co=gloss_calls(G/"hidden_files/w45/de-zh-tw-proof/baseline2-build")
ed=gloss_calls(G/"hidden_files/weekly-report-w45-de-zh-tw-build")
for f in sorted(set(co)|set(ed)):
    print(f, "core calls:",len(co.get(f,[])), "ed calls:",len(ed.get(f,[])))
    for a,b in zip(co.get(f,[]),ed.get(f,[])):
        ca=a.split("·"); cb=b.split("·")
        # headwords: German tokens before CJK? print counts + first tokens
        print(f"  core n={len(ca)} ed n={len(cb)} match={len(ca)==len(cb)}")
        if len(ca)!=len(cb):
            print("   CORE:",a[:200]); print("   ED  :",b[:200])
        else:
            # compare German headword sequence: strip CJK from each item
            def heads(s): return [re.sub(r'[\u4e00-\u9fff]+','',x).strip() for x in s]
            if heads(a)!=heads(b): print("   HEADWORD DIFF core:",heads(a)," ed:",heads(b))
# P1 expl line: find content12 expl string with die Englische Woche
for name,d in [("CORE",G/"hidden_files/w45/de-zh-tw-proof/baseline2-build"),("ED",G/"hidden_files/weekly-report-w45-de-zh-tw-build")]:
    src=(pathlib.Path(d)/"content12.py").read_text(encoding="utf-8")
    for m in re.finditer(r'.*Englische Woche.*', src):
        print(name, m.group(0)[:220], " -> split· =", len(m.group(0).split("·")))
