#!/usr/bin/env python3
"""Independent RUxKO W45 proof script 7: CORRECTED split scan (step window 10-45,
so P8 answer lines at step 14.69 are covered) + source-word verification."""
import re
from pathlib import Path

BASE = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/files")
ED = BASE/"weekly-report-w45-ru-ko/svg"
BUILD = Path("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-ru-ko-build")
PAGES = ["p1-pervaya","p2-zhizn","p3-kultura","p4-sport","p5-molodezh","p6-razbor","p7-yazyk","p8-test"]
HANG = re.compile(r"[\uac00-\ud7a3]")

sources = []
for f in ["content12.py","content34.py","content56.py","content7.py","content8.py","bslib4.py"]:
    sources.append((BUILD/f).read_text(encoding="utf-8"))
src_joined = "\n".join(sources)

print("source contains '나타내요':", "나타내요" in src_joined)
print("source contains '도구격':", "도구격" in src_joined)
print("source contains '호에':", "호에" in src_joined)
# find the 99 note source line
for f in ["content8.py"]:
    for line in (BUILD/f).read_text(encoding="utf-8").splitlines():
        if "나타내요" in line or "대조" in line:
            print(f"  src {f}: {line.strip()[:200]}")
for f in ["content8.py"]:
    for line in (BUILD/f).read_text(encoding="utf-8").splitlines():
        if "도구격" in line:
            print(f"  src {f}: {line.strip()[:200]}")

def elems(path):
    t = Path(path).read_text(encoding="utf-8")
    out = []
    for m in re.finditer(r'<text[^>]*x="([\d.]+)"[^>]*y="([\d.]+)"[^>]*font-size="([\d.]+)"[^>]*>([^<]*)</text>', t):
        out.append((float(m.group(1)), float(m.group(2)), float(m.group(3)), m.group(4)))
    return out

def syl(tok): return len(HANG.findall(tok))

print("\n== CORRECTED split scan (step 10-45, same x+size) ==")
for pg in PAGES:
    els = elems(ED/f"{pg}.svg")
    els_sorted = sorted(els, key=lambda e: (e[0], e[1]))
    for a, b in zip(els_sorted, els_sorted[1:]):
        if a[0] != b[0] or a[2] != b[2]:
            continue
        step = b[1] - a[1]
        if not (10 <= step <= 45):
            continue
        at, bt = a[3].strip(), b[3].strip()
        if not at or not bt or not HANG.search(at) or not HANG.search(bt):
            continue
        prev_last = at.split()[-1]
        curr_first = bt.split()[0]
        if not HANG.search(prev_last) or not HANG.search(curr_first):
            continue
        joined = (prev_last + curr_first).strip(".,!?…)]»」·;:")
        if joined and joined in src_joined and len(joined) >= 2:
            flag = "FLAG>=3" if syl(curr_first) >= 3 else "cand<3"
            print(f"  {pg} [{flag}] tail={syl(curr_first)} step={step:.2f} prev={at!r} curr={bt!r} word={joined!r}")
print("\nDone.")
