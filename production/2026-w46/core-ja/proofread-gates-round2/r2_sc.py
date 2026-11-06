# Round 2 independent Simplified-only scan for zh-tw (CORRECT method):
# enumerate EVERY char in the zh-tw SVGs whose OpenCC s2t form differs, dump
# every occurrence (file/y/string), then adjudicate each char. The discarded
# definition (s2t-differing AND absent from core repertoire) is NOT used.
import glob, json, os
from collections import Counter, defaultdict
from xml.etree import ElementTree as ET
from opencc import OpenCC

NS = "{http://www.w3.org/2000/svg}"
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
TW = os.path.join(BASE, "weekly-report-w46-ja-zh-tw", "svg")

cc = OpenCC("s2t")

occ = defaultdict(list)  # char -> [(file, y, string)]
for fn in sorted(glob.glob(os.path.join(TW, "*.svg"))):
    root = ET.parse(fn).getroot()
    for t in root.iter(NS + "text"):
        s = "".join(t.itertext())
        y = round(float(t.get("y")), 1)
        for ch in set(s):
            if cc.convert(ch) != ch:
                occ[ch].append((os.path.basename(fn), y, s))

counts = Counter()
for ch, lst in occ.items():
    for _, _, s in lst:
        counts[ch] += s.count(ch)

print("distinct s2t-differing chars:", len(occ), "".join(sorted(occ)))
print("total instances:", sum(counts.values()))
for ch in sorted(occ):
    print(f"CHAR {ch} (s2t {cc.convert(ch)}) instances={counts[ch]} elements={len(occ[ch])}")

RESIDUE_STRINGS = ["得到东西的场所用「で」。", "看的场所用「で」。", "场所用「で」",
                   "在酉の市买熊手", "2026年没有三の酉", "新小结是美ノ海",
                   "「千歳飴」受欢迎", "口号是「静かだけど、冒険中。」"]
TC_FORMS = ["得到東西的場所用「で」。", "看的場所用「で」。", "場所用「で」",
            "在酉の市買熊手", "2026年沒有三の酉", "新小結是美ノ海",
            "「千歳飴」受歡迎", "口號是「静かだけど、冒険中。」"]
full = ""
for fn in sorted(glob.glob(os.path.join(TW, "*.svg"))):
    root = ET.parse(fn).getroot()
    for t in root.iter(NS + "text"):
        full += "".join(t.itertext()) + "\n"

# Per-TC-form occurrence contexts (file/y) for quoting in the verdict.
contexts = {}
for form in TC_FORMS:
    hits = []
    for fn in sorted(glob.glob(os.path.join(TW, "*.svg"))):
        root = ET.parse(fn).getroot()
        for t in root.iter(NS + "text"):
            s = "".join(t.itertext())
            if form in s:
                hits.append((os.path.basename(fn), round(float(t.get("y")), 1), s))
    contexts[form] = hits
    print("TC", repr(form), "occurrences:", len(hits))
    for h in hits:
        print("   ", h)

res = {
    "diff_chars": sorted(occ),
    "diff_chars_str": "".join(sorted(occ)),
    "counts": {ch: counts[ch] for ch in sorted(occ)},
    "occurrences": {ch: occ[ch] for ch in sorted(occ)},
    "residue_strings_present": [s for s in RESIDUE_STRINGS if s in full],
    "tc_form_contexts": contexts,
    "residue_chars_present": [ch for ch in "东买场欢没结" if ch in occ],
}
print("residue strings present:", res["residue_strings_present"])
print("residue chars present:", res["residue_chars_present"])
json.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "sc-scan-round2.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote sc-scan-round2.json")
