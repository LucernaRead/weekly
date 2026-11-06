# -*- coding: utf-8 -*-
"""Wrap-spy for the KO x PT build: run the edition build in a SCRATCH copy
with a logging wrap(). Never run in the real build dir (its OUT points at
the delivery dir). Copies the build dir to spy/, repoints OUT to spy/svg/,
patches svglib.wrap to log pre-kinsoku and post-kinsoku lines for every
call, runs run.py there, writes spy-wrap.log next to this script.
Usage: tools/venv/bin/python spy_wrap.py (from this build dir)
"""
import os, re, shutil, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCRATCH = os.path.join(HERE, "spy")
LOG = os.path.join(HERE, "spy-wrap.log")


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
        s = s.replace("files/weekly-report-w45-ko-pt/svg",
                      "hidden_files/weekly-report-w45-ko-pt-build/spy/svg")
        open(p, "w", encoding="utf-8").write(s)
    p = os.path.join(SCRATCH, "svglib.py")
    s = open(p, encoding="utf-8").read()
    assert "import os" in s and "# kinsoku shori" in s
    s = s.replace("from PIL import ImageFont",
                  "from PIL import ImageFont\nimport json as _json")
    s = s.replace("    # kinsoku shori",
                  "    _spy_pre = list(lines)\n    # kinsoku shori")
    s = s.replace("    return lines\n\ndef esc",
                  "    _log = os.environ.get('SPY_LOG', '')\n"
                  "    if _log:\n"
                  "        with open(_log, 'a', encoding='utf-8') as _fh:\n"
                  "            _fh.write(_json.dumps({'text': text, 'kind': kind, 'bold': bold, 'size': size, 'max_w': max_w, 'pre': _spy_pre, 'post': list(lines)}, ensure_ascii=False) + '\\n')\n"
                  "    return lines\n\ndef esc")
    assert "_log" in s, "wrap return patch did not apply"
    open(p, "w", encoding="utf-8").write(s)
    if os.path.exists(LOG):
        os.remove(LOG)
    env = dict(os.environ, SPY_LOG=LOG)
    venv = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/tools/venv/bin/python")
    r = subprocess.run([venv, "run.py"], cwd=SCRATCH, env=env,
                       capture_output=True, text=True)
    print(r.stdout[-1500:])
    print(r.stderr[-1500:])
    assert r.returncode == 0, "spy run failed"
    n = sum(1 for _ in open(LOG, encoding="utf-8"))
    print(f"spy log: {n} wrap calls -> {LOG}")


if __name__ == "__main__":
    main()
