#!/usr/bin/env python3
"""Reproof R2: independent 10-45 orphan / mid-word-split scan, all 8 pages."""
import re, pathlib
BASE=pathlib.Path("/home/hatch/workspace/goals/lucernaread-social-media-operations")
ED=BASE/"files/weekly-report-w45-ru-ko/svg"; BUILD=BASE/"hidden_files/weekly-report-w45-ru-ko-build"
PAGES=["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]
HANG=re.compile(r"[\uac00-\ud7a3]"); PUNCT=set(".!?…)]»」")
def parse(path):
    t=path.read_text(encoding="utf-8"); out=[]
    for m in re.finditer(r"<text([^>]*)>(.*?)</text>",t,re.S):
        a=m.group(1)
        def g(k):
            mm=re.search(k+r'="([^"]*)"',a); return mm.group(1) if mm else ""
        if not g("x") or not g("y"): continue
        out.append((float(g("x")),float(g("y")),float(g("font-size")) if g("font-size") else 0,m.group(2)))
    return out
# inventory: every whitespace token in rendered lines + build sources
inv=set()
for p in PAGES:
    for x,y,s,t in parse(ED/f"{p}.svg"): inv.update(t.split())
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py","bslib4.py"]:
    inv.update((BUILD/f).read_text(encoding="utf-8").split())
inv_stripped={w.strip(".,!?…)]»」·;:\"'()") for w in inv}
flagged=[]; cands=[]
for p in PAGES:
    els=parse(ED/f"{p}.svg")
    for x,y,s,t in els:
        st=t.strip()
        if not st: continue
        toks=st.split()
        if toks and all(ch in PUNCT for ch in toks[-1]): print(f"{p} END-PUNCT-ONLY x={x} y={y} {t!r}")
        if st[0] in PUNCT: print(f"{p} START-PUNCT x={x} y={y} {t!r}")
    els.sort(key=lambda e:(e[0],e[1]))
    for a,b in zip(els,els[1:]):
        if a[0]!=b[0] or a[2]!=b[2]: continue
        step=b[1]-a[1]
        if not (10<=step<=45): continue
        at,bt=a[3].strip(),b[3].strip()
        if not at or not bt or not HANG.search(at) or not HANG.search(bt): continue
        pl,cf=at.split()[-1],bt.split()[0]
        if not HANG.search(pl) or not HANG.search(cf): continue
        joined=(pl+cf).strip(".,!?…)]»」·;:")
        if joined and joined in inv_stripped and len(joined)>=2:
            tail=len(HANG.findall(cf))
            rec=(p,a[0],a[1],b[1],tail,at,bt,joined)
            (flagged if tail>=3 else cands).append(rec)
            print(f"{p} SPLIT tail={tail} x={a[0]} y={a[1]}->{b[1]} prev={at!r} curr={bt!r} word={joined!r}")
print(f"FLAGGED(>=3): {len(flagged)}")
for r in flagged: print(" FLAG:",r)
print(f"CANDIDATES(<3): {len(cands)}")
for r in cands: print(" CAND:",r)
