# -*- coding: utf-8 -*-
"""Registry comparison core vs edition, via scratch copies only.

Each build tree is copied to reg-scratch-<tag>/, OUT repointed to the
scratch svg dir, and a driver process runs the content modules in one
process (the build's own run.py order) and dumps REG as JSON. The real
build dirs and delivery dirs are never written by this script.
Usage: tools/venv/bin/python reg_compare.py
"""
import json
import os
import shutil
import subprocess
import sys

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.join(BASE, "hidden_files/weekly-report-w45-ko-build")
DRIVER = ("import runpy, sys, os, json\n"
          "os.chdir(os.path.dirname(os.path.abspath('run.py')))\n"
          "for f in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:\n"
          "    runpy.run_path(f, run_name='__main__')\n"
          "import bslib4\n"
          "print(json.dumps(bslib4.REG, ensure_ascii=False))\n")


def dump(build_dir, tag, edition_slug):
    scratch = os.path.join(HERE, f"reg-scratch-{tag}")
    if os.path.exists(scratch):
        shutil.rmtree(scratch)
    os.makedirs(os.path.join(scratch, "svg"))
    for f in ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "svglib.py", "run.py"]:
        shutil.copy(os.path.join(build_dir, f), os.path.join(scratch, f))
    shutil.copytree(os.path.join(build_dir, "assets"), os.path.join(scratch, "assets"))
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(scratch, f)
        s = open(p, encoding="utf-8").read()
        s = s.replace(f"files/{edition_slug}/svg",
                      f"hidden_files/weekly-report-w45-ko-fr-build/reg-scratch-{tag}/svg")
        open(p, "w", encoding="utf-8").write(s)
    venv = os.path.join(BASE, "tools/venv/bin/python")
    r = subprocess.run([venv, "-c", DRIVER], cwd=scratch,
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr[-2000:]
    lines = [ln for ln in r.stdout.splitlines() if ln.startswith("[")]
    assert len(lines) == 1, r.stdout[-500:]
    return json.loads(lines[0])


def main():
    core = dump(CORE, "core", "weekly-report-w45-ko-core")
    ed = dump(HERE, "ed", "weekly-report-w45-ko-fr")
    assert len(core) == len(ed) == 150, (len(core), len(ed))
    bad = [e for c, e in zip(core, ed)
           if (c["n"], c["page"], c["level"]) != (e["n"], e["page"], e["level"])]
    print(f"n/page/level identical: {len(bad) == 0} (mismatches {len(bad)})")
    keydiff = [e["n"] for c, e in zip(core, ed) if c["key"] != e["key"]]
    print(f"keydiff: {keydiff}")
    for c, e in zip(core, ed):
        if c["key"] != e["key"]:
            print(f"  #{c['n']}: core {c['key']!r} -> ed {e['key']!r} (note ed {e['note']!r})")
    notediff = sum(1 for c, e in zip(core, ed) if c["note"] != e["note"])
    print(f"notes changed: {notediff}/150")
    from collections import Counter
    print("edition by level:", dict(Counter(e["level"] for e in ed)))
    print("edition by page:", dict(sorted(Counter(e["page"] for e in ed).items())))
    print("edition by type:", dict(Counter(e["type"] for e in ed)))
    # E-zone detail
    for e in ed:
        if e["page"] == 8 and e["n"] in (137, 138, 139, 140, 150):
            print(f"  P8 #{e['n']} type={e['type']} key={e['key']!r} note={e['note']!r}")


if __name__ == "__main__":
    main()
