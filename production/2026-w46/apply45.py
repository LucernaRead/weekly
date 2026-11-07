# -*- coding: utf-8 -*-
"""Apply harvested W45 ops (filtered: old must occur; VOL.2->VOL.3 in new
strings; geometry/render ops excluded — handled separately) to a W46
fan-out build dir, then report residual CJK literals identical to core
literals (untranslated explanation strings)."""
import ast, json, os, re, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HF = os.path.join(GOAL, "hidden_files")
CORE_BUILD = os.path.join(HF, "weekly-report-w46-ko-build")
CJK = re.compile(r"[\u4e00-\u9fff]")

GEOM_PATTERNS = ("p.text(975, 372", "p.hline(MX, RIGHT, 392", "p.rect(MX, 424",
                 "p.text(MX + 30, 478", "p.text(MX + 30, 522",
                 "p.text(RIGHT - 30, 478", "p.text(RIGHT - 30, 522",
                 "p.text(975, 366", "p.hline(MX, RIGHT, 412",
                 "p.text(975, 394")

def is_geom(op):
    return any(p in op["old"] for p in GEOM_PATTERNS)

def load_ops(lang):
    h = json.load(open(f"/tmp/w46-harvest/{lang}-ops.json", encoding="utf-8"))
    return h["ops"]

def bump(new):
    return new.replace("VOL.2", "VOL.3")

def apply_ops(lang, ops, log):
    build = os.path.join(HF, f"weekly-report-w46-ko-{lang}-build")
    files = {}
    for fname in ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        files[fname] = open(os.path.join(build, fname), encoding="utf-8").read()
    # file-scoped ops first (harvest order), then flat ops longest-first
    file_ops = [o for o in ops if o["scope"] == "file" and not is_geom(o) and o["file"] not in ("render.py", "svglib.py", "run.py")]
    flat_ops = [o for o in ops if o["scope"] == "flat" and not is_geom(o)]
    flat_ops.sort(key=lambda o: -len(o["old"]))
    applied, skipped = 0, 0
    for o in file_ops:
        fname = o["file"]
        if fname not in files:
            skipped += 1
            continue
        n = files[fname].count(o["old"])
        if n >= 1:
            files[fname] = files[fname].replace(o["old"], bump(o["new"]))
            applied += 1
            log.append(f"  FILE {fname} x{n} {o['old'][:50]!r} -> {bump(o['new'])[:50]!r}")
        else:
            skipped += 1
    for o in flat_ops:
        hit = False
        for fname, text in files.items():
            n = text.count(o["old"])
            if n >= 1:
                files[fname] = text.replace(o["old"], bump(o["new"]))
                applied += 1
                hit = True
                log.append(f"  FLAT {fname} x{n} {o['old'][:50]!r} -> {bump(o['new'])[:50]!r}")
        if not hit:
            skipped += 1
    for fname, text in files.items():
        open(os.path.join(build, fname), "w", encoding="utf-8").write(text)
    return applied, skipped

def core_cjk_literals():
    out = set()
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        tree = ast.parse(open(os.path.join(CORE_BUILD, fname), encoding="utf-8").read())
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and CJK.search(node.value):
                out.add(node.value)
    return out

def residual(lang):
    core = core_cjk_literals()
    build = os.path.join(HF, f"weekly-report-w46-ko-{lang}-build")
    res = []
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        src = open(os.path.join(build, fname), encoding="utf-8").read()
        tree = ast.parse(src)
        for node in ast.walk(tree):
            if isinstance(node, ast.Constant) and isinstance(node.value, str) and CJK.search(node.value):
                if node.value in core:
                    res.append((fname, node.lineno, node.value))
    # dedupe preserving order
    seen, uniq = set(), []
    for r in res:
        if r[2] not in seen:
            seen.add(r[2])
            uniq.append(r)
    return uniq

if __name__ == "__main__":
    lang = sys.argv[1]
    ops = load_ops(lang)
    log = []
    a, s = apply_ops(lang, ops, log)
    print(f"{lang}: applied {a}, skipped {s} (of {len(ops)})")
    open(f"/tmp/w46-harvest/{lang}-apply45.log", "w", encoding="utf-8").write("\n".join(log))
    res = residual(lang)
    print(f"{lang}: residual untranslated CJK literals: {len(res)}")
    for fname, ln, v in res:
        print(f"  {fname}:{ln}: {v!r}")
    json.dump([[f, l, v] for f, l, v in res],
              open(f"/tmp/w46-harvest/{lang}-residual.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
