# -*- coding: utf-8 -*-
"""Independent freeze-diff decomposition for W45 zh-cn x ja proofread.
Reads core + edition SVGs, computes per-page text multiset diffs,
classifies removed strings (Han-bearing listed individually) and
added strings without kana (listed individually), and checks
Han-run conservation at joined-text level."""
import re, json, glob, os
from collections import Counter
from xml.etree import ElementTree as ET

CORE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zhcn-core/svg")
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-cn-ja/svg")

def texts(path):
    t = ET.parse(path)
    out = []
    for el in t.iter():
        if el.tag.endswith('text') and el.text:
            out.append(el.text)
    return out

def pgnum(fn):
    m = re.search(r'p(\d)-', os.path.basename(fn))
    return int(m.group(1))

HAN = re.compile(r'[\u4e00-\u9fff]+')
KANA = re.compile(r'[\u3040-\u30ff]')

core, ed = {}, {}
for d, store in ((CORE, core), (ED, ed)):
    for f in sorted(glob.glob(os.path.join(d, '*.svg'))):
        store[pgnum(f)] = texts(f)

report = {}
for p in range(1, 9):
    c, e = Counter(core[p]), Counter(ed[p])
    removed = c - e
    added = e - c
    # removed strings bearing Han chars (need individual adjudication)
    rem_han = [(s, n) for s, n in sorted(removed.items()) if HAN.search(s)]
    rem_pure_en = [(s, n) for s, n in sorted(removed.items()) if not HAN.search(s)]
    # added strings with NO kana
    add_nokana = [(s, n) for s, n in sorted(added.items()) if not KANA.search(s)]
    add_kana = [(s, n) for s, n in sorted(added.items()) if KANA.search(s)]
    # Han-run conservation, joined-text level
    cjoin = ''.join(core[p])
    ejoin = ''.join(ed[p])
    cruns = Counter(HAN.findall(cjoin))
    eruns = Counter(HAN.findall(ejoin))
    missing = {r: n for r, n in cruns.items() if eruns.get(r, 0) < n}
    # edition-only runs
    only_ed = {r: n for r, n in eruns.items() if cruns.get(r, 0) < n}
    report[p] = {
        'removed_total': sum(removed.values()), 'added_total': sum(added.values()),
        'removed_han': rem_han, 'removed_pure_en_count': sum(n for _, n in rem_pure_en),
        'added_nokana': add_nokana, 'added_nokana_occ': sum(n for _, n in add_nokana),
        'added_kana_occ': sum(n for _, n in add_kana),
        'missing_runs': missing, 'edition_only_runs': only_ed,
        'core_runs_total': sum(cruns.values()), 'ed_runs_total': sum(eruns.values()),
    }
    print(f"=== P{p}: removed {sum(removed.values())} (Han-bearing {sum(n for _,n in rem_han)} occ, {len(rem_han)} unique; pure-EN {sum(n for _,n in rem_pure_en)} occ) | added {sum(added.values())} (no-kana {sum(n for _,n in add_nokana)} occ, {len(add_nokana)} unique; kana {sum(n for _,n in add_kana)} occ)")
    print(f"    Han runs: core {sum(cruns.values())} -> edition {sum(eruns.values())}; MISSING runs: {missing if missing else 'NONE'}")
    for s, n in rem_han:
        print(f"    REM-HAN x{n}: {s!r}")
    for s, n in add_nokana:
        print(f"    ADD-NOKANA x{n}: {s!r}")
json.dump({str(k): {kk: vv for kk, vv in v.items() if kk not in ('removed_han','added_nokana')} for k, v in report.items()},
          open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-ja-reproof/work/decompose-summary.json"), 'w'), ensure_ascii=False, indent=1)
# full lists to file
with open(os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-ja-reproof/work/decompose-full.txt"), 'w') as fh:
    for p in range(1, 9):
        r = report[p]
        fh.write(f"=== P{p} REM-HAN ===\n")
        for s, n in r['removed_han']: fh.write(f"x{n} {s!r}\n")
        fh.write(f"=== P{p} ADD-NOKANA ===\n")
        for s, n in r['added_nokana']: fh.write(f"x{n} {s!r}\n")
        fh.write(f"=== P{p} MISSING-RUNS ===\n{r['missing_runs']}\n")
        fh.write(f"=== P{p} EDITION-ONLY-RUNS ===\n{r['edition_only_runs']}\n")
print("written decompose-summary.json + decompose-full.txt")
