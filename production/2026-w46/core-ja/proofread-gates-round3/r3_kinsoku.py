# Round 3 independent kinsoku + orphan scan (own implementation; definitions per
# SOP/check_edition.py as recorded in the Round 1 verdict: line-START set,
# line-END opening-bracket set, orphan runs window 10-45).
import glob, json, os
from xml.etree import ElementTree as ET

NS = "{http://www.w3.org/2000/svg}"
NO_START = set("。、，．！？：；）」』】ー…‥・") | set("］｝〉》％") | set(")]}.,!?%:;\"")
NO_END = set("（「『〔【《〈([")
ORPHAN_START = set(")]}〉》.,!?%:;」』】")

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
DIRS = {"zh-cn": "weekly-report-w46-ja-core", "de": "weekly-report-w46-ja-de",
        "en": "weekly-report-w46-ja-en", "es": "weekly-report-w46-ja-es",
        "fr": "weekly-report-w46-ja-fr", "it": "weekly-report-w46-ja-it",
        "ko": "weekly-report-w46-ja-ko", "nl": "weekly-report-w46-ja-nl",
        "pt": "weekly-report-w46-ja-pt", "ru": "weekly-report-w46-ja-ru",
        "zh-tw": "weekly-report-w46-ja-zh-tw"}

def page_texts(path):
    root = ET.parse(path).getroot()
    return [(float(t.get("x")), float(t.get("y")), "".join(t.itertext()))
            for t in root.iter(NS + "text")]

def is_hangul(ch):
    return 0xAC00 <= ord(ch) <= 0xD7A3

def scan(svgdir):
    start_hits, end_hits, orphans = [], [], []
    for pi, fn in enumerate(sorted(glob.glob(os.path.join(svgdir, "*.svg"))), 1):
        texts = page_texts(fn)
        for x, y, s in texts:
            st = s.strip()
            if st and st[0] in NO_START:
                start_hits.append([pi, round(y, 1), st[:60]])
            if st and st[-1] in NO_END:
                end_hits.append([pi, round(y, 1), st[-60:]])
        ordered = sorted(texts, key=lambda t: (t[1], t[0]))
        runs = []
        for x, y, s in ordered:
            if runs and abs(x - runs[-1][-1][0]) < 3 and 10 <= y - runs[-1][-1][1] <= 45 and len(runs[-1]) < 30:
                runs[-1].append((x, y, s))
            else:
                runs.append([(x, y, s)])
        for run in runs:
            if len(run) < 2:
                continue
            last = run[-1][2].strip()
            if last.endswith(")") or last.endswith("」") or last.startswith("("):
                seg = last.split()[-1] if last.split() else last
                if sum(1 for ch in seg if is_hangul(ch)) >= 3:
                    orphans.append([pi, "PAREN-FRAG", round(run[-1][1], 1), last[:60]])
            first = run[1][2].strip()
            if first and first[0] in ORPHAN_START:
                orphans.append([pi, "START-PUNCT", round(run[1][1], 1), first[:60]])
            prev = run[-2][2].strip()
            if len(last) <= 6 and sum(1 for ch in last if is_hangul(ch)) >= 3 and len(prev) >= 14:
                if last.endswith(("요.", "요", "예요.", "예요", "어요.", "어요")) or ")" in last:
                    orphans.append([pi, "SHORT-TAIL", round(run[-1][1], 1), last[:60]])
    return {"kinsoku_start": start_hits, "kinsoku_end": end_hits, "orphan": orphans}

out = {}
for code, d in DIRS.items():
    r = scan(os.path.join(BASE, d, "svg"))
    out[code] = r
    print(code, "start", len(r["kinsoku_start"]), "end", len(r["kinsoku_end"]),
          "orphan", len(r["orphan"]))
    for h in r["kinsoku_start"] + r["kinsoku_end"] + r["orphan"]:
        print("  ", h)

here = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(here, "kinsoku-orphan-round3.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
print("wrote kinsoku-orphan-round3.json")
