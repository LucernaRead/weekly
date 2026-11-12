#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""head_check.py — standing gate: run.py HEAD TOO WIDE is a defect.

`run.py` (via bslib4 `head()`) prints `  !! HEAD TOO WIDE [<tag>]: <text>`
whenever a column/battery heading's advance width exceeds its column.
That is a real overflow: the D5 pilot (2026-11-11, en-fr) proved all 8
other gates miss it — occlusion, edge scan, creambox, boxtitle and spill
all stayed green while a P7 heading ran 8.6 px past its column and past
the page content edge (RIGHT=1862). A P8 battery heading over by 1.2 px
is also a defect, even when the ink stops short of the next column: the
warning itself is the gate, not the visual severity.

Usage:
  tools/venv/bin/python tools/head_check.py <run.log> [<run.log> ...]
      [--json out.json] [--selftest]
Exit 0 iff no HEAD TOO WIDE in any log; exit 1 if any found (each one
listed with file, line number, tag and text); exit 2 on usage error or
a missing log file. Read-only wrt the logs; writes only --json + stdout.

--selftest runs synthetic dirty/clean logs under tools/scratch/ and
asserts the dirty log reports exactly its planted findings and the
clean log passes. Run it after any change to this file.
"""
import argparse
import json
import os
import re
import sys
import tempfile

LINE_RE = re.compile(r"HEAD TOO WIDE \[(?P<tag>[^\]]+)\]: (?P<text>.*)$")


def check_logs(paths):
    """Return (findings, missing). findings: list of dicts."""
    findings, missing = [], []
    for path in paths:
        if not os.path.isfile(path):
            missing.append(path)
            continue
        with open(path, encoding="utf-8", errors="replace") as f:
            for n, line in enumerate(f, 1):
                m = LINE_RE.search(line)
                if m:
                    findings.append({"log": path, "line": n,
                                     "tag": m.group("tag"),
                                     "text": m.group("text").strip()})
    return findings, missing


def selftest():
    scratch = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "scratch", "head-check-selftest")
    os.makedirs(scratch, exist_ok=True)
    dirty = os.path.join(scratch, "dirty.log")
    clean = os.path.join(scratch, "clean.log")
    with open(dirty, "w", encoding="utf-8") as f:
        f.write("TOTAL 150\n")
        f.write("  !! HEAD TOO WIDE [P7-col3]: AN EXAMPLE LETTER\u3000Exemple\n")
        f.write("  !! HEAD TOO WIDE [P8-battery]: D\u3000SENTENCES\u3000Phrases \u00e0 former\n")
        f.write("ALL DONE\n")
    with open(clean, "w", encoding="utf-8") as f:
        f.write("TOTAL 150\nALL DONE\n")
    fails = []
    found, missing = check_logs([dirty])
    if missing:
        fails.append(f"selftest: dirty log reported missing: {missing}")
    if len(found) != 2:
        fails.append(f"selftest: dirty log: expected 2 findings, got {len(found)}")
    elif found[0]["tag"] != "P7-col3" or found[1]["tag"] != "P8-battery":
        fails.append(f"selftest: dirty log: wrong tags: {found}")
    found_c, _ = check_logs([clean])
    if found_c:
        fails.append(f"selftest: clean log: expected 0 findings, got {len(found_c)}")
    _, missing2 = check_logs([os.path.join(scratch, "no-such.log")])
    if len(missing2) != 1:
        fails.append("selftest: missing file not reported")
    if fails:
        print("SELFTEST FAILED")
        for x in fails:
            print(" -", x)
        return 1
    print("SELFTEST OK: dirty log -> 2 findings (P7-col3, P8-battery); "
          "clean log -> 0; missing file reported")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description="HEAD TOO WIDE hard gate")
    ap.add_argument("logs", nargs="*", help="run.py output log(s) to scan")
    ap.add_argument("--json", dest="json_out", default=None)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.logs:
        ap.error("at least one run.log is required")
    findings, missing = check_logs(args.logs)
    if missing:
        for p in missing:
            print(f"BLOCKED: no such log: {p}")
        return 2
    for f in findings:
        print(f"DEFECT {f['log']}:{f['line']} HEAD TOO WIDE "
              f"[{f['tag']}]: {f['text']}")
    if args.json_out:
        json.dump({"findings": findings},
                  open(args.json_out, "w", encoding="utf-8"),
                  ensure_ascii=False, indent=1)
    print(f"HEAD CHECK {'FAIL ' + str(len(findings)) + ' defects' if findings else 'PASS 0 defects'}")
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
