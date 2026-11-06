# -*- coding: utf-8 -*-
"""Gloss gate (README #21): rendered-page gloss() box counts vs core.
Rendered method: a gloss box starts at a text node beginning with the
gloss prefix ("Пояснение — " RU / "译注｜" core); continuation lines share
the same x with ~29.7 pitch. Joined box text is split on "·" itself
(never on " · "), segments stripped and counted. Compared per page,
per box, in document order. Call-string counts are reported separately
by gloss_call.py. Usage: tools/venv/bin/python gloss_render.py
"""
import ast
import glob
import os
import re

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
CORE_SVG = os.path.join(BASE, "files/weekly-report-w45-ko-core/svg")
ED_SVG = os.path.join(BASE, "files/weekly-report-w45-ko-ru/svg")
CORE_BUILD = os.path.join(BASE, "hidden_files/weekly-report-w45-ko-build")
ED_BUILD = os.path.join(BASE, "hidden_files/weekly-report-w45-ko-ru-build")
PREFIX = {"core": "译注｜", "ru": "Пояснение — "}


def rendered_boxes(svgdir, prefix):
    out = {}
    for path in sorted(glob.glob(os.path.join(svgdir, "*.svg"))):
        src = open(path, encoding="utf-8").read()
        nodes = [(float(x), float(y), t)
                 for x, y, t in re.findall(
                     r'<text x="([\d.]+)" y="([\d.]+)"[^>]*>([^<]*)</text>', src)]
        boxes = []
        cur = None
        for x, y, t in nodes:
            if t.startswith(prefix):
                if cur:
                    boxes.append(cur)
                cur = [x, y, t]
            elif cur and x == cur[0] and 26 <= y - cur[1] <= 34:
                cur[1] = y
                cur[2] += t
            else:
                if cur:
                    boxes.append(cur)
                cur = None
        if cur:
            boxes.append(cur)
        items = []
        for _, _, txt in boxes:
            body = txt[len(prefix):]
            segs = [s.strip() for s in body.split("·") if s.strip()]
            items.append(len(segs))
        out[os.path.basename(path)] = items
    return out


def call_counts(builddir, names):
    total = 0
    per = {}
    for fn in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        tree = ast.parse(open(os.path.join(builddir, fn), encoding="utf-8").read())
        n = 0
        for node in ast.walk(tree):
            if not isinstance(node, ast.Call):
                continue
            if getattr(node.func, "attr", None) not in names or not node.args:
                continue
            arg = node.args[0]
            if not isinstance(arg, ast.Constant) or not isinstance(arg.value, str):
                continue
            n += len([s for s in arg.value.split("·") if s.strip()])
        per[fn] = n
        total += n
    return total, per


def main():
    rc = rendered_boxes(CORE_SVG, PREFIX["core"])
    re_ = rendered_boxes(ED_SVG, PREFIX["ru"])
    ok = True
    for pg in sorted(rc):
        match = rc[pg] == re_[pg]
        ok &= match
        print(f"{pg}: core boxes {rc[pg]} (total {sum(rc[pg])}) | ru boxes {re_[pg]} (total {sum(re_[pg])}) {'OK' if match else 'MISMATCH'}")
    print("rendered-page gloss() totals:", sum(sum(v) for v in rc.values()),
          "vs", sum(sum(v) for v in re_.values()), "ALL-BOXES-EQUAL" if ok else "MISMATCH")
    for label, names in [("gloss() only", ("gloss",)), ("gloss()+glossline()", ("gloss", "glossline"))]:
        tc, pc = call_counts(CORE_BUILD, names)
        te, pe = call_counts(ED_BUILD, names)
        print(f"call-string {label}: core {tc} {pc} | ru {te} {pe} {'OK' if tc == te else 'MISMATCH'}")


if __name__ == "__main__":
    main()
