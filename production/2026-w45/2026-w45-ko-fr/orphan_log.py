# -*- coding: utf-8 -*-
"""Produce a wrap-call log for the orphan scan, in a SCRATCH copy only.

Copies this build tree to orphan-scratch/, repoints OUT to the scratch
svg dir, instruments the scratch svglib wrap() to record its input string
and its pre/post-kinsoku line lists, runs run.py there, and writes
orphan-wrap.log next to this script. The real build dir and delivery dir
are never written by this script.
Usage: tools/venv/bin/python orphan_log.py
"""
import os
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.path.join(HERE, "orphan-scratch")
LOG = os.path.join(HERE, "orphan-wrap.log")


def main():
    if os.path.exists(SCRATCH):
        shutil.rmtree(SCRATCH)
    os.makedirs(os.path.join(SCRATCH, "svg"))
    for f in ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "svglib.py", "run.py"]:
        shutil.copy(os.path.join(HERE, f), os.path.join(SCRATCH, f))
    shutil.copytree(os.path.join(HERE, "assets"), os.path.join(SCRATCH, "assets"))
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(SCRATCH, f)
        s = open(p, encoding="utf-8").read()
        s = s.replace("files/weekly-report-w45-ko-fr/svg",
                      "hidden_files/weekly-report-w45-ko-fr-build/orphan-scratch/svg")
        open(p, "w", encoding="utf-8").write(s)
    p = os.path.join(SCRATCH, "svglib.py")
    s = open(p, encoding="utf-8").read()
    assert s.count("    # kinsoku shori") == 1
    assert s.count("    return lines\n\ndef esc") == 1
    s = s.replace("from PIL import ImageFont",
                  "from PIL import ImageFont\nimport json as _logjson")
    s = s.replace("    # kinsoku shori",
                  "    _pre_capture = list(lines)\n    # kinsoku shori")
    s = s.replace("    return lines\n\ndef esc",
                  "    _dest = os.environ.get('KO_FR_WRAP_LOG', '')\n"
                  "    if _dest:\n"
                  "        with open(_dest, 'a', encoding='utf-8') as _fh:\n"
                  "            _fh.write(_logjson.dumps({'text': text, 'kind': kind, 'bold': bold, 'size': size, 'max_w': max_w, 'pre': _pre_capture, 'post': list(lines)}, ensure_ascii=False) + '\\n')\n"
                  "    return lines\n\ndef esc")
    open(p, "w", encoding="utf-8").write(s)
    if os.path.exists(LOG):
        os.remove(LOG)
    env = dict(os.environ, KO_FR_WRAP_LOG=LOG)
    venv = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python")
    r = subprocess.run([venv, "run.py"], cwd=SCRATCH, env=env,
                       capture_output=True, text=True)
    print(r.stdout[-1500:])
    print(r.stderr[-1500:])
    assert r.returncode == 0, "scratch run failed"
    n = sum(1 for _ in open(LOG, encoding="utf-8"))
    print(f"wrap log: {n} calls -> {LOG}")


if __name__ == "__main__":
    main()
