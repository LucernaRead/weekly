#!/usr/bin/env python3
"""Rerun edition + core builds in proof scratch (repointed outputs only), dump REG, compare.
Also: transform-only reproduction: core build copy + transform.py -> run -> compare to delivered SVGs
and to build-dir content files."""
import json, os, re, runpy, shutil, sys, hashlib
from collections import Counter
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
OUT = os.path.join(BASE, "hidden_files/w45/en-nl-proof")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]
def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()
def rerun(src, tag, extra_files=None):
    dest = os.path.join(OUT, "scratch", tag)
    if os.path.exists(dest): shutil.rmtree(dest)
    shutil.copytree(src, dest, ignore=shutil.ignore_patterns("__pycache__"))
    svg_out = os.path.join(dest, "svg"); os.makedirs(svg_out, exist_ok=True)
    pat = re.compile(r"([\"'])(?:~|/home/hatch)?/?workspace/goals/lucernaread-social-media-operations/files/[^\"']*\1")
    for fn in FILES:
        p = os.path.join(dest, fn); s = open(p, encoding="utf-8").read()
        s2 = pat.sub(lambda m: f"{m.group(1)}{svg_out}{m.group(1)}", s)
        assert s2 != s, f"no repoint in {fn}"
        assert "files/weekly-report" not in s2
        open(p, "w", encoding="utf-8").write(s2)
    sys.path.insert(0, dest); os.chdir(dest)
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        for f in FILES: runpy.run_path(os.path.join(dest, f), run_name="__main__")
    open(os.path.join(OUT, f"registry-{tag}-log.txt"), "w", encoding="utf-8").write(buf.getvalue())
    import bslib4
    reg = list(bslib4.REG)
    json.dump(reg, open(os.path.join(OUT, f"registry-{tag}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    h = {fn: sha(os.path.join(svg_out, fn)) for fn in sorted(os.listdir(svg_out)) if fn.endswith(".svg")}
    json.dump(h, open(os.path.join(OUT, f"registry-{tag}-hashes.json"), "w"), indent=1)
    print(tag, "REG total:", len(reg), "hashes:", h)
    for mod in [m for m in list(sys.modules) if m in ("bslib4", "svglib") or m.startswith("content")]: del sys.modules[mod]
    sys.path.remove(dest)
    return reg, h, dest
ed_reg, ed_h, _ = rerun(os.path.join(BASE, "hidden_files/weekly-report-w45-en-nl-build"), "edition")
co_reg, co_h, _ = rerun(os.path.join(BASE, "hidden_files/weekly-report-w45-en-build"), "core")
def summ(reg):
    return {"total": len(reg), "nums_continuous": [e["n"] for e in reg] == list(range(1, len(reg)+1)),
            "per_page": dict(sorted(Counter(e["page"] for e in reg).items())),
            "levels": dict(sorted(Counter(e["level"] for e in reg).items())),
            "types": dict(sorted(Counter(e["type"] for e in reg).items()))}
print("EDITION:", json.dumps(summ(ed_reg), ensure_ascii=False))
print("CORE:", json.dumps(summ(co_reg), ensure_ascii=False))
mismatch = []
for a, b in zip(ed_reg, co_reg):
    diffs = [k for k in ("page","level","type","key") if a[k] != b[k]]
    if diffs: mismatch.append((a["n"], diffs, b, a))
print("registry mismatches (ed vs core):", len(mismatch))
for n, diffs, b, a in mismatch: print(" ", n, diffs, "core:", {k: b[k] for k in diffs}, "ed:", {k: a[k] for k in diffs})
cjk = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af]")
print("edition REG notes with CJK:", [(e["n"], e["note"]) for e in ed_reg if cjk.search(e["note"] or "")])
print("edition REG notes empty:", sum(1 for e in ed_reg if not e["note"]), "core empty:", sum(1 for e in co_reg if not e["note"]))
print("edition REG types set:", sorted(set(e["type"] for e in ed_reg)))
print("core REG types set:", sorted(set(e["type"] for e in co_reg)))
# delivered SVG hashes vs rerun hashes
delivered = {fn: sha(os.path.join(BASE, "files/weekly-report-w45-en-nl/svg", fn)) for fn in sorted(os.listdir(os.path.join(BASE, "files/weekly-report-w45-en-nl/svg"))) if fn.endswith(".svg")}
print("delivered:", delivered)
print("run.py-rerun == delivered:", ed_h == delivered)
for fn in sorted(delivered): print(f"  {fn} rerun==delivered: {ed_h.get(fn)==delivered[fn]}")
# --- transform-only reproduction ---
print("\n== TRANSFORM-ONLY ==")
src = os.path.join(BASE, "hidden_files/weekly-report-w45-en-build")
dest = os.path.join(OUT, "scratch", "transform")
if os.path.exists(dest): shutil.rmtree(dest)
shutil.copytree(src, dest, ignore=shutil.ignore_patterns("__pycache__"))
shutil.copy(os.path.join(BASE, "hidden_files/weekly-report-w45-en-nl-build/transform.py"), os.path.join(dest, "transform.py"))
# transform.py BASE = its own dir; run it there (it writes transform-log.txt into dest, harmless)
os.chdir(dest)
import subprocess
r = subprocess.run([sys.executable, "transform.py"], cwd=dest, capture_output=True, text=True)
print("transform stdout:", r.stdout[-2000:]); print("transform stderr:", r.stderr[-2000:]); print("transform rc:", r.returncode)
# diff content files vs NL build content files (excluding OUT? transform repoints OUT to en-nl, same as NL build)
for fn in FILES + ["bslib4.py"]:
    a = open(os.path.join(dest, fn), encoding="utf-8").read()
    b = open(os.path.join(BASE, "hidden_files/weekly-report-w45-en-nl-build", fn), encoding="utf-8").read()
    print(f"  content diff {fn}: identical={a==b} len {len(a)} vs {len(b)}")
    if a != b:
        import difflib
        d = list(difflib.unified_diff(b.splitlines(), a.splitlines(), lineterm="", n=1))
        print("    diff lines:", len(d))
        for line in d[:40]: print("    ", line)
# now run transformed copy (repoint OUT to scratch svg) and compare SVGs
svg_out = os.path.join(dest, "svg"); os.makedirs(svg_out, exist_ok=True)
pat = re.compile(r"([\"'])(?:~|/home/hatch)?/?workspace/goals/lucernaread-social-media-operations/files/[^\"']*\1")
for fn in FILES:
    p = os.path.join(dest, fn); s = open(p, encoding="utf-8").read()
    s2 = pat.sub(lambda m: f"{m.group(1)}{svg_out}{m.group(1)}", s)
    open(p, "w", encoding="utf-8").write(s2)
sys.path.insert(0, dest)
import io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    for f in FILES: runpy.run_path(os.path.join(dest, f), run_name="__main__")
open(os.path.join(OUT, "transform-run-log.txt"), "w", encoding="utf-8").write(buf.getvalue())
th = {fn: sha(os.path.join(svg_out, fn)) for fn in sorted(os.listdir(svg_out)) if fn.endswith(".svg")}
print("transform-run hashes:", th)
print("transform-run == delivered:", th == delivered)
for fn in sorted(delivered): print(f"  {fn} transform==delivered: {th.get(fn)==delivered[fn]}")
print("transform-run log tail:", buf.getvalue()[-500:])
