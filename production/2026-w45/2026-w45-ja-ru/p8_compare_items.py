# -*- coding: utf-8 -*-
"""Reconstruct P8 key items (number -> printed line) from core and edition
SVGs and list byte-identical items for adjudication, plus lines 37/137-140.
Reconstruction: keys region y>1328, document order; a line matching ^N.
starts an item; other lines append to the current item; separator paras
are skipped. Both SVGs are parsed identically, so wrap artefacts cancel.
"""
import os
import re
import sys

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")


def items(path):
    s = open(path, encoding="utf-8").read()
    ts = re.findall(r'<text[^>]*x="([\d.]+)"[^>]*y="([\d.]+)"[^>]*>([^<]*)</text>', s)
    out = {}
    cur = None
    for x, y, t in ts:
        if float(y) <= 1328:
            continue
        if t.startswith("— ") and t.endswith(" —"):
            continue
        m = re.match(r"^(\d+)\.\s?(.*)$", t)
        if m:
            cur = int(m.group(1))
            out[cur] = m.group(2)
        elif cur is not None:
            out[cur] += t
    return out


def main():
    co = items(os.path.join(BASE, "files/weekly-report-w45-ja-core/svg/p8-tesuto.svg"))
    ed = items(os.path.join(BASE, "files/weekly-report-w45-ja-ru/svg/p8-tesuto.svg"))
    print(f"core items: {len(co)} (numbers {min(co)}-{max(co)}, missing {[n for n in range(1, 151) if n not in co]})")
    print(f"ed items:   {len(ed)} (numbers {min(ed)}-{max(ed)}, missing {[n for n in range(1, 151) if n not in ed]})")
    identical = [n for n in range(1, 151) if co.get(n) == ed.get(n)]
    print(f"identical items ({len(identical)}): {identical}")
    for n in identical:
        print(f"  IDENTICAL #{n}: {co[n][:130]!r}")
    for n in (37, 137, 138, 139, 140):
        print(f"--- #{n} CORE: {co.get(n, '?')[:160]!r}")
        print(f"--- #{n} ED:   {ed.get(n, '?')[:160]!r}")
    diff = [n for n in range(1, 151) if co.get(n) != ed.get(n)]
    print(f" differing items: {len(diff)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
