# Simplified-only scan for zh-tw, AFTER the fix (adjudicated version).
# NOTE: an earlier draft defined SC-only as "s2t-differing AND absent from the
# core repertoire". That definition is INVALID: the core IS the zh-cn edition,
# so its repertoire contains Simplified explanation characters too, and the
# draft reported 0 candidates while residue was present. It was discarded.
# This version enumerates the full universe (every char in the zh-tw SVGs
# whose OpenCC s2t form differs) and adjudicates it against the BEFORE
# enumeration (sc-occurrences-BEFORE.txt): 21 of the 27 such chars are
# legitimate Japanese shinjitai / deliberate keeps
# (会内写参号国学寝届峡当数来横浅温点画祷里静); 6 occur ONLY in residue
# strings (东买场欢没结). After the fix, the residue chars must be absent
# entirely, the 8 residue source strings must be absent, and their
# Traditional forms must be present.
import glob, json, sys
from xml.etree import ElementTree as ET
from opencc import OpenCC
NS = "{http://www.w3.org/2000/svg}"
BASE = "/home/hatch/workspace/goals/lucernaread-social-media-operations/files"
def texts(d):
    out = []
    for f in sorted(glob.glob(d + "/svg/*.svg")):
        root = ET.parse(f).getroot()
        for t in root.iter(NS + "text"):
            out.append((f.split("/")[-1], round(float(t.get("y")), 1), "".join(t.itertext())))
    return out
cc = OpenCC("s2t")
tw = texts(BASE + "/weekly-report-w46-ja-zh-tw")
diff_chars = sorted({c for _, _, s in tw for c in s if cc.convert(c) != c})
RESIDUE_CHARS = set("东买场欢没结")
hits = [(fn, y, s, sorted(set(s) & RESIDUE_CHARS)) for fn, y, s in tw if set(s) & RESIDUE_CHARS]
RESIDUE_STRINGS = ["得到东西的场所用「で」。", "看的场所用「で」。", "场所用「で」",
                   "在酉の市买熊手", "2026年没有三の酉", "新小结是美ノ海",
                   "「千歳飴」受欢迎", "口号是「静かだけど、冒険中。」"]
TC_FORMS = ["得到東西的場所用「で」。", "看的場所用「で」。", "場所用「で」",
            "在酉の市買熊手", "2026年沒有三の酉", "新小結是美ノ海",
            "「千歳飴」受歡迎", "口號是「静かだけど、冒険中。」"]
full = "\n".join(s for _, _, s in tw)
res = {"diff_chars": diff_chars, "residue_char_hits": hits,
       "residue_strings_present": [s for s in RESIDUE_STRINGS if s in full],
       "tc_forms_present": {s: (s in full) for s in TC_FORMS}}
print("s2t-differing chars remaining:", len(diff_chars), "".join(diff_chars))
print("residue-char hits:", len(hits))
for h in hits: print("  HIT:", h)
print("residue strings present:", res["residue_strings_present"])
print("TC forms present:", res["tc_forms_present"])
print("VERDICT:", "0 Simplified-only characters remain" if not hits and not res["residue_strings_present"] and all(res["tc_forms_present"].values()) else "RESIDUE REMAINS")
json.dump(res, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", sys.argv[1])
