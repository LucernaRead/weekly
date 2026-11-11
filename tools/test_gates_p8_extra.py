#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Minimal regression test for the gates.py p8 `extra` key bug.

Bug (run-log L1896/L3206): the zh-tw refanout gates.py built its p8 summary
with `"extra": comp.get("extra_count", "?")`. tools/p8.py compare writes
`extra` (a list) into p8-compare.json; `extra_count` appears only in p8.py's
stdout line ("extra_count=0"), never in the JSON. The lookup therefore
always fell through to the "?" default, and every gates.json reported
`"extra": "?"` even when the compare was CLEAN with extra=[].

This test:
  1. reproduces the original bug (old expression -> "?" on real-shaped input),
  2. extracts the `"extra": ...` expression from the gates.py under test and
     evaluates it against fixture p8-compare dicts, asserting it returns the
     real `extra` list,
  3. asserts the buggy `extra_count` lookup is gone from the file.

Usage: python3 test_gates_p8_extra.py [path/to/gates.py]
Exit 0 = pass, 1 = fail. Plain python3, no venv needed.
"""
import json
import re
import sys

import os
# Default target: the sibling gates-zh-tw.py promoted into tools/ with this
# test (the live driver is the goals-side scratch-refanout-zh-tw/gates.py;
# pass its path as argv[1] to test that copy instead).
_HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT = os.path.join(_HERE, "gates-zh-tw.py")
PATH = sys.argv[1] if len(sys.argv) > 1 else DEFAULT

# Fixture p8-compare dicts, same schema tools/p8.py compare writes.
CLEAN = {"status": "CLEAN", "total": 150, "missing": [], "extra": [],
         "uncertain": [], "keydiff": []}
WITH_EXTRA = {"status": "EXTRA_ONLY", "total": 150, "missing": [],
              "extra": [150], "uncertain": [], "keydiff": [137, 138]}
MULTI_EXTRA = {"status": "EXTRA_ONLY", "total": 150, "missing": [],
               "extra": [137, 140], "uncertain": [], "keydiff": []}


def old_expr(comp):
    """Verbatim buggy expression (kept only to reproduce the bug)."""
    return comp.get("extra_count", "?")


def main():
    fails = []

    # 1. reproduce the original bug on the fixtures.
    for name, comp in (("CLEAN", CLEAN), ("WITH_EXTRA", WITH_EXTRA)):
        got = old_expr(comp)
        print(f"old expr on {name}: {got!r} (expected '?' — the bug)")
        if got != "?":
            fails.append(f"old expr did not reproduce the bug on {name}")

    # 2. the gates.py under test must no longer LOOK UP extra_count.
    # (The word may still appear in a comment explaining the bug.)
    src = open(PATH, encoding="utf-8").read()
    if re.search(r'\.get\(\s*["\']extra_count["\']', src):
        fails.append(f"{PATH} still looks up 'extra_count'")
    else:
        print(f"{PATH}: no 'extra_count' lookup — OK")

    # 3. extract the live `"extra": <expr>` from the file and eval it.
    m = re.search(r'"extra":\s*(comp\.get\([^)]*\))', src)
    if not m:
        print("FAIL: no '\"extra\": comp.get(...)' expression found in file")
        return 1
    print(f"live expression in file: {m.group(1)}")
    for name, comp, want in (("CLEAN", CLEAN, []),
                             ("WITH_EXTRA", WITH_EXTRA, [150]),
                             ("MULTI_EXTRA", MULTI_EXTRA, [137, 140])):
        got = eval(m.group(1), {}, {"comp": comp})
        print(f"live expr on {name}: {got!r} (expected {want!r})")
        if got != want:
            fails.append(f"live expr on {name}: got {got!r}, want {want!r}")

    if fails:
        print("FAIL:")
        for f in fails:
            print(" -", f)
        return 1
    print("PASS: gates.py p8 extra key regression test")
    return 0


if __name__ == "__main__":
    sys.exit(main())
