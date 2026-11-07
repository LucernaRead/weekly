# -*- coding: utf-8 -*-
"""Registry comparison core vs edition (one-process dumps, scratch only).
For each side: copy the build .py files + assets to reg-scratch-<side>,
repoint OUT to the scratch svg dir, run content modules in ONE process
via runpy (registry accumulates), dump bslib4.REG to JSON. Compare:
number/page/level/type identical; keys diff; notes diff count; stems diff.
Run from this dir with tools/venv/bin/python reg_compare.py
"""
import os, shutil, subprocess, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
VENV = os.path.join(GOAL, "tools/venv/bin/python")

DUMP = '''
import os, sys, runpy, json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    runpy.run_path(f, run_name="__main__")
import bslib4
json.dump(bslib4.REG, open("reg.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("dumped", len(bslib4.REG))
'''

def dump_side(name, srcdir, outname):
    d = os.path.join(HERE, "reg-scratch-" + name)
    if os.path.exists(d):
        shutil.rmtree(d)
    os.makedirs(os.path.join(d, "svg"))
    for f in ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "svglib.py"]:
        shutil.copy(os.path.join(srcdir, f), os.path.join(d, f))
    shutil.copytree(os.path.join(srcdir, "assets"), os.path.join(d, "assets"))
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(d, f)
        s = open(p, encoding="utf-8").read()
        old = "files/weekly-report-w45-ko-core/svg" if name == "core" else "files/weekly-report-w45-ko-nl/svg"
        assert old in s, (name, f)
        s = s.replace(old, "hidden_files/weekly-report-w45-ko-nl-build/reg-scratch-" + name + "/svg")
        open(p, "w", encoding="utf-8").write(s)
    open(os.path.join(d, "dump.py"), "w", encoding="utf-8").write(DUMP)
    r = subprocess.run([VENV, "dump.py"], cwd=d, capture_output=True, text=True)
    assert r.returncode == 0, r.stdout[-1000:] + r.stderr[-1000:]
    print(name, r.stdout.strip().splitlines()[-1])
    return json.load(open(os.path.join(d, "reg.json"), encoding="utf-8"))

core = dump_side("core", os.path.join(GOAL, "hidden_files/weekly-report-w45-ko-build"), "core")
ed = dump_side("ed", HERE, "ed")
assert len(core) == len(ed) == 150, (len(core), len(ed))
print("TOTAL core", len(core), "edition", len(ed))
meta_diff, key_diff, note_diff, stem_diff = [], [], [], 0
for c, e in zip(core, ed):
    assert c["n"] == e["n"]
    if (c["page"], c["level"], c["type"]) != (e["page"], e["level"], e["type"]):
        meta_diff.append((c["n"], (c["page"], c["level"], c["type"]), (e["page"], e["level"], e["type"])))
    if c["key"] != e["key"]:
        key_diff.append((c["n"], c["key"], e["key"]))
    if c["note"] != e["note"]:
        note_diff.append(c["n"])
    # stem/body field names vary; compare all remaining string fields
    for k in c:
        if k in ("n", "page", "level", "type", "key", "note"):
            continue
        if c[k] != e[k]:
            stem_diff += 1
            if c["n"] in (139, 140):
                print(f"  stem/body diff #{c['n']} field {k}: core={c[k]!r} edition={e[k]!r}")
print("page/level/type diffs:", meta_diff)
print("key diffs:", key_diff)
print("notes changed:", len(note_diff), "/150")
print("other-field diffs total (incl. stems 139/140):", stem_diff)
json.dump({"key_diff": key_diff, "note_diff": note_diff, "meta_diff": meta_diff},
          open(os.path.join(HERE, "reg_compare.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
