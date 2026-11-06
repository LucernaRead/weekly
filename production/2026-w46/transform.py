#!/usr/bin/env python3
"""Apply an exact-string translation mapping to a fan-out build copy.

Usage: transform.py <build-dir> <mapping.json>
- Applies to content12.py, content34.py, content56.py, content7.py,
  content8.py, bslib4.py. Longest keys first. Every key must occur at
  least once across the six files, else exit 1 with the missing keys.
- Prints per-key occurrence counts. Never touches Chinese core text:
  keys are full English explanation strings only.
"""
import json, sys, os, re

FILES = ["content12.py", "content34.py", "content56.py", "content7.py",
         "content8.py", "bslib4.py"]

def apply_pair(src, old, new):
    """Plain replace, or template replace when old contains {placeholders}:
    literal segments are replaced pairwise (e.g. {NCHARS}, {n}, {pg})."""
    if "{" not in old:
        return src.replace(old, new), src.count(old)
    old_segs = re.split(r"\{[^}]+\}", old)
    new_segs = re.split(r"\{[^}]+\}", new)
    assert len(old_segs) == len(new_segs), (old, new)
    seg_counts = [src.count(o) for o, n in zip(old_segs, new_segs) if o]
    if not seg_counts or seg_counts[0] == 0:
        # the template's opening segment is absent: this file does not
        # contain the template (later segments may be generic substrings)
        return src, 0
    # all literal segments of one template must occur the same number of
    # times; a partial match would corrupt the source
    assert len(set(seg_counts)) == 1, (old, seg_counts)
    for o, n in zip(old_segs, new_segs):
        if o:
            src = src.replace(o, n)
    return src, seg_counts[0]

def main():
    build, map_path = sys.argv[1], sys.argv[2]
    mapping = json.load(open(map_path, encoding="utf-8"))
    items = sorted(mapping.items(), key=lambda kv: -len(kv[0]))
    missing = []
    counts = {}
    for fname in FILES:
        path = os.path.join(build, fname)
        src = open(path, encoding="utf-8").read()
        for old, new in items:
            src, n = apply_pair(src, old, new)
            counts[old] = counts.get(old, 0) + n
        open(path, "w", encoding="utf-8").write(src)
    # verify: no old literal segment remains
    for old, new in items:
        if counts.get(old, 0) == 0:
            print(f"MISSING (0 occurrences): {old[:60]!r}")
            missing.append(old)
        else:
            print(f"ok {counts[old]}x: {old[:50]!r} -> {new[:40]!r}")
    if missing:
        print(f"FAIL: {len(missing)} keys still present (or unreplaced)")
        sys.exit(1)
    print("transform OK:", len(items), "keys")

if __name__ == "__main__":
    main()
