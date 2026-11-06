#!/usr/bin/env python3
# Rerun edition + core builds in scratch (repointed outputs only) and dump REG.
import json, os, re, runpy, shutil, sys, hashlib
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
OUT = os.path.join(BASE, "hidden_files/w45/en-de-proof")
FILES = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]

def rerun(src, tag):
    dest = os.path.join(OUT, "scratch", tag)
    if os.path.exists(dest):
        shutil.rmtree(dest)
    shutil.copytree(src, dest, ignore=shutil.ignore_patterns("__pycache__"))
    svg_out = os.path.join(dest, "svg")
    os.makedirs(svg_out, exist_ok=True)
    pat = re.compile(r"([\"'])(?:~|/home/hatch)?/?workspace/goals/lucernaread-social-media-operations/files/[^\"']*\1")
    for fn in FILES:
        p = os.path.join(dest, fn)
        s = open(p, encoding="utf-8").read()
        s2 = pat.sub(lambda m: f"{m.group(1)}{svg_out}{m.group(1)}", s)
        assert s2 != s, f"no repoint in {fn}"
        assert "files/weekly-report" not in s2
        open(p, "w", encoding="utf-8").write(s2)
    sys.path.insert(0, dest)
    os.chdir(dest)
    log = []
    import io, contextlib
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        for f in FILES:
            runpy.run_path(os.path.join(dest, f), run_name="__main__")
    log = buf.getvalue()
    open(os.path.join(OUT, f"registry-{tag}-log.txt"), "w", encoding="utf-8").write(log)
    import bslib4
    reg = list(bslib4.REG)
    json.dump(reg, open(os.path.join(OUT, f"registry-{tag}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # hash produced svgs
    h = {}
    for fn in sorted(os.listdir(svg_out)):
        if fn.endswith(".svg"):
            h[fn] = hashlib.sha256(open(os.path.join(svg_out, fn), "rb").read()).hexdigest()
    json.dump(h, open(os.path.join(OUT, f"registry-{tag}-hashes.json"), "w"), indent=1)
    print(tag, "REG total:", len(reg), "produced:", sorted(h))
    # reset for next tree: remove bslib4 + content modules
    for mod in [m for m in list(sys.modules) if m in ("bslib4", "svglib") or m.startswith("content")]:
        del sys.modules[mod]
    sys.path.remove(dest)
    return reg, h

ed_reg, ed_h = rerun(os.path.join(BASE, "hidden_files/weekly-report-w45-en-de-build"), "edition")
co_reg, co_h = rerun(os.path.join(BASE, "hidden_files/weekly-report-w45-en-build"), "core")
from collections import Counter
def summ(reg):
    return {"total": len(reg),
            "per_page": dict(sorted(Counter(e["page"] for e in reg).items())),
            "levels": dict(sorted(Counter(e["level"] for e in reg).items())),
            "types": dict(sorted(Counter(e["type"] for e in reg).items()))}
print("EDITION:", json.dumps(summ(ed_reg), ensure_ascii=False))
print("CORE:", json.dumps(summ(co_reg), ensure_ascii=False))
mismatch = []
for a, b in zip(ed_reg, co_reg):
    diffs = []
    if a["page"] != b["page"]: diffs.append("page")
    if a["level"] != b["level"]: diffs.append("level")
    if a["type"] != b["type"]: diffs.append("type")
    if a["key"] != b["key"]: diffs.append("key")
    if diffs: mismatch.append((a["n"], diffs, b["key"], a["key"]))
print("registry mismatches:", len(mismatch))
for m in mismatch: print(" ", m)
# P8 notes German-only check on edition REG notes
import re as _re
cjk = _re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af\uff00-\uffef]")
bad = [(e["n"], e["note"]) for e in ed_reg if cjk.search(e["note"] or "")]
print("edition REG notes with CJK:", bad)
print("edition REG notes empty count:", sum(1 for e in ed_reg if not e["note"]))
print("core REG notes empty count:", sum(1 for e in co_reg if not e["note"]))
