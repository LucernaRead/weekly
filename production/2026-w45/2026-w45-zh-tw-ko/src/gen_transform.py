# -*- coding: utf-8 -*-
"""Generate the self-contained transform.py from es_pairs.json (verbatim
core OLD strings) + ko_map.py (Korean NEW strings). This avoids
hand-transcribing OLD strings, which must match core sources
character-for-character (the transform's own rep() assertions verify
every count at apply time). Output lives OUTSIDE the build dir, per
sibling convention, because fresh_copy() wipes the build dir.
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from ko_map import KO, EXTRA_C7

es = json.load(open(os.path.join(HERE, "es_pairs.json"), encoding="utf-8"))
SKIP = {("C12", 52), ("C34", 58), ("C56", 62), ("C56", 63),
         ("C7", 49), ("C7", 50), ("C7", 51), ("C7", 52),
         # C8[45] writing key "(開放題,範文如下)": identity per W43 zh-tw-ko
         # shipped code — never printed (writing keys render "150. ✓ note").
         ("C8", 45)}
used = set()
sections = {}
for sec in ("BSLIB", "C12", "C34", "C56", "C7", "C8"):
    pairs = []
    for i, (old, _es_new, count) in enumerate(es[sec]):
        key = (sec, i)
        if key in SKIP:
            continue
        assert key in KO, f"missing KO mapping for {key}: {old[:80]!r}"
        used.add(key)
        pairs.append((old, KO[key], count))
    sections[sec] = pairs
# C34 match: single W43-column form for both sets (es used two ordered
# Spanish forms; the KO column precedent is one form, cf. W43 KO x5).
sections["C34"].append(('instr="Match"', 'instr="단어와 뜻 짝짓기"', 2))
sections["C7"].extend(EXTRA_C7)
extra_keys = set(KO) - used - {("C34", "MATCH")}
assert not extra_keys, f"unused KO keys: {extra_keys}"

def fmt(pairs):
    lines = ["["]
    for old, new, count in pairs:
        lines.append(f"    ({old!r}, {new!r}, {count}),")
    lines.append("]")
    return "\n".join(lines)

HEADER = open(os.path.join(HERE, "transform_header.py"), encoding="utf-8").read()
FOOTER = open(os.path.join(HERE, "transform_footer.py"), encoding="utf-8").read()

out = [HEADER]
for sec, fname in (("BSLIB", "bslib4.py"), ("C12", "content12.py"),
                   ("C34", "content34.py"), ("C56", "content56.py"),
                   ("C7", "content7.py"), ("C8", "content8.py")):
    out.append(f"# ---------------------------------------------------------------- {fname}\n{sec} = {fmt(sections[sec])}\n")
out.append(FOOTER)
dest = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-zh-tw-ko-transform.py")
open(dest, "w", encoding="utf-8").write("\n".join(out))
print("pairs:", {s: len(sections[s]) for s in sections}, "total:", sum(len(v) for v in sections.values()))
print("wrote", dest)
