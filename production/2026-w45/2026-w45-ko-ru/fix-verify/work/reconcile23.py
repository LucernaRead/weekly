import pathlib, importlib.util
H = pathlib.Path.home()/"workspace/goals/lucernaread-social-media-operations"
BUILD = H/"hidden_files/weekly-report-w45-ko-ru-build"
OLD = H/"hidden_files/w45/ko-ru-proof/work/transform-repro"
FRESH = H/"hidden_files/w45/ko-ru-fix-verify/work/fresh"
DEL = BUILD
FILES = ["bslib4.py","content12.py","content34.py","content56.py","content7.py","content8.py"]
spec = importlib.util.spec_from_file_location("tmod", BUILD/"transform.py")
m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
FX = m.FIX2FIX3
def counts(d, s):
    return {fn: (d/fn).read_text(encoding="utf-8").count(s) for fn in FILES}
print("Per-mapping: src-occurrences in OLD-transform output (=pre-fix long forms) | dst-occurrences in DELIVERED")
tot_old = {fn:0 for fn in FILES}; tot_del = {fn:0 for fn in FILES}
for i,(src,dst) in enumerate(FX.items(),1):
    co = counts(OLD, src); cd = counts(DEL, dst)
    nz_o = {k:v for k,v in co.items() if v}; nz_d = {k:v for k,v in cd.items() if v}
    print(f"FX{i} src-in-old={nz_o} dst-in-delivered={nz_d}")
    for k,v in co.items(): tot_old[k]+=v
    for k,v in cd.items(): tot_del[k]+=v
print("TOTAL src-in-old per file:", tot_old, "sum=", sum(tot_old.values()))
print("TOTAL dst-in-delivered per file:", tot_del, "sum=", sum(tot_del.values()))
# fresh output: src must be 0, dst must equal delivered counts
print("Fresh: src occurrences (must all be 0):")
for src,dst in FX.items():
    c = counts(FRESH, src)
    if any(c.values()): print("  NONZERO src in fresh:", c, src[:40])
print("Fresh src check done (no lines above = all zero).")
print("Fresh dst counts per file:")
tf = {fn:0 for fn in FILES}
for src,dst in FX.items():
    c = counts(FRESH, dst)
    for k,v in c.items(): tf[k]+=v
print(tf, "sum=", sum(tf.values()))
# Also: old-vs-delivered OUT-normalized diff line counts
import difflib
for fn in FILES:
    a = (OLD/fn).read_text(encoding="utf-8").replace("ko-core","OUT").replace("ko-ru","OUT").splitlines()
    b = (DEL/fn).read_text(encoding="utf-8").replace("ko-core","OUT").replace("ko-ru","OUT").splitlines()
    diff = list(difflib.unified_diff(a,b,lineterm="",n=0))
    minus = [l for l in diff if l.startswith("-") and not l.startswith("---")]
    plus = [l for l in diff if l.startswith("+") and not l.startswith("+++")]
    print(f"old-vs-delivered OUT-norm {fn}: -lines={len(minus)} +lines={len(plus)}")
