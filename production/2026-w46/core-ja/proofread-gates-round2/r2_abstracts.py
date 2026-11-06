# Round 2 independent ABSTRACT verification: format + practice framing +
# rest-verbatim vs the BEFORE texts recorded in ja-fix/abstracts-before-after.txt.
import os, re, json

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
FIX = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/ja-fix")
DIRS = {"zh-cn": "weekly-report-w46-ja-core", "de": "weekly-report-w46-ja-de",
        "en": "weekly-report-w46-ja-en", "es": "weekly-report-w46-ja-es",
        "fr": "weekly-report-w46-ja-fr", "it": "weekly-report-w46-ja-it",
        "ko": "weekly-report-w46-ja-ko", "nl": "weekly-report-w46-ja-nl",
        "pt": "weekly-report-w46-ja-pt", "ru": "weekly-report-w46-ja-ru",
        "zh-tw": "weekly-report-w46-ja-zh-tw"}

# Parse the before/after record file.
rec = open(os.path.join(FIX, "abstracts-before-after.txt"), encoding="utf-8").read()
pairs = {}
for m in re.finditer(r"=== (\S+) \(.*?\) ===\nBEFORE: (.*?)\nAFTER:  (.*?)\n", rec, re.S):
    pairs[m.group(1)] = (m.group(2).strip(), m.group(3).strip())
print("record pairs parsed:", sorted(pairs))

BANNED = ["通过读日语新闻学日语", "透過真實日本新聞學日語",
          "learning Japanese through real Japanese news",
          "Japanisch durch echte japanische Nachrichten lernen",
          "aprender japonés con noticias japonesas reales",
          "apprendre le japonais à travers de vraies nouvelles japonaises",
          "imparare il giapponese con vere notizie giapponesi",
          "실제 일본 뉴스로 일본어를 배웁니다",
          "Japans te leren met echt Japans nieuws",
          "aprender japonês com notícias japonesas reais",
          "изучающих японский по настоящим японским новостям",
          "读日语新闻学日语", "读新闻学", "以新闻学", "用报纸学",
          "learn Japanese through", "through real Japanese news"]

out = {}
for code, d in DIRS.items():
    raw = open(os.path.join(BASE, d, "ABSTRACT.txt"), "rb").read()
    text = raw.decode("utf-8")
    before, after = pairs[code]
    checks = {
        "single_line_plus_trailing_newline": raw.endswith(b"\n") and text.count("\n") == 1,
        "no_ascii_dquote": '"' not in text,
        "has_150": "150" in text,
        "has_A2": "A2" in text,
        "has_B2": "B2" in text,
        "matches_after_record": text.rstrip("\n") == after,
        "banned_tail_present": [b for b in BANNED if b in text],
        "prefix_preserved_vs_before": text.rstrip("\n").startswith(before[:40]),
    }
    # Stronger verbatim check: AFTER record must share its full prefix with
    # BEFORE up to the tail divergence; report the common prefix length.
    i = 0
    while i < min(len(before), len(after)) and before[i] == after[i]:
        i += 1
    checks["common_prefix_len_before_after"] = i
    checks["before_len"] = len(before)
    checks["after_len"] = len(after)
    checks["current_equals_after"] = text.rstrip("\n") == after
    out[code] = checks
    print(code, checks)

json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "abstracts-round2.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
