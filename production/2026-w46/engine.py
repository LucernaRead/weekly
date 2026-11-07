# -*- coding: utf-8 -*-
"""W46 ES fan-out transform engine.

Usage from a fan-out build dir's transform script:
    from engine import apply_pairs
    apply_pairs(BUILD, PAIRS, FILES)
PAIRS: list of (old, new) applied longest-first across FILES (default
content12/34/56/7/8.py + bslib4.py + svglib.py + render.py when listed).
Every pair must hit at least once; counts are logged. Pairs whose old
string was fully consumed by a longer pair hit 0 and are reported as
CONSUMED (not an error) when allow_zero=True.
After all pairs, a residue scan reports remaining CJK / simplified /
traditional characters per file; the caller adjudicates the allowlist.
"""
import os, re, sys

CJK = re.compile(r"[\u2e80-\u9fff\u3040-\u30ff\uac00-\ud7af]")
DEFAULT_FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
                 "content7.py", "content8.py", "svglib.py", "render.py"]

def apply_pairs(builddir, pairs, files=None, allow_zero=()):
    files = files or DEFAULT_FILES
    texts = {}
    for f in files:
        p = os.path.join(builddir, f)
        if os.path.exists(p):
            texts[f] = open(p, encoding="utf-8").read()
    log = []
    # longest first, stable
    ordered = sorted(pairs, key=lambda t: -len(t[0]))
    for item in ordered:
        old, new = item[0], item[1]
        flist = item[2] if len(item) > 2 and item[2] else files
        total = 0
        for f in flist:
            if f in texts:
                n = texts[f].count(old)
                if n:
                    texts[f] = texts[f].replace(old, new)
                    total += n
        if total == 0 and old not in allow_zero:
            raise SystemExit(f"PAIR MISS (0 hits): {old!r}")
        log.append((total, old, new))
    for f, t in texts.items():
        open(os.path.join(builddir, f), "w", encoding="utf-8").write(t)
    for total, old, new in log:
        print(f"{total:4d}  {old[:60]!r} -> {new[:60]!r}")
    return log

def residue_scan(builddir, files=None):
    files = files or DEFAULT_FILES
    out = {}
    for f in files:
        p = os.path.join(builddir, f)
        if os.path.exists(p):
            t = open(p, encoding="utf-8").read()
            chars = sorted(set(CJK.findall(t)))
            out[f] = chars
            print(f, "CJK distinct:", len(chars), "".join(chars)[:80])
    return out
