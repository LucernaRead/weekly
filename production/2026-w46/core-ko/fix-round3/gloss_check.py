import glob, os, re
from xml.etree import ElementTree as ET

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
NS = "{http://www.w3.org/2000/svg}"
EDITIONS = {"zh-cn": "weekly-report-w46-ko-core", "de": "weekly-report-w46-ko-de",
            "en": "weekly-report-w46-ko-en", "es": "weekly-report-w46-ko-es",
            "fr": "weekly-report-w46-ko-fr", "it": "weekly-report-w46-ko-it",
            "ja": "weekly-report-w46-ko-ja", "nl": "weekly-report-w46-ko-nl",
            "pt": "weekly-report-w46-ko-pt", "ru": "weekly-report-w46-ko-ru",
            "zh-tw": "weekly-report-w46-ko-zh-tw"}
EXPECTED = {
 "zh-cn": "译注｜겹치다 重叠 · 가늘다 细 · 감사하다 感谢 · 나누다 区分、分享。",
 "de": "HINWEIS · 겹치다 = sich überschneiden · 가늘다 = dünn · 감사하다 = danken · 나누다 = unterscheiden, teilen",
 "en": "Note — 겹치다 = to overlap · 가늘다 = thin · 감사하다 = to thank · 나누다 = to tell apart, to share",
 "es": "Nota — 겹치다 = coincidir, solaparse · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, compartir",
 "fr": "Note — 겹치다 = se chevaucher · 가늘다 = fin · 감사하다 = remercier · 나누다 = distinguer, partager",
 "it": "Nota — 겹치다 = sovrapporsi · 가늘다 = sottile · 감사하다 = ringraziare · 나누다 = distinguere, condividere",
 "ja": "解説 — 겹치다 = 重なる · 가늘다 = 細い · 감사하다 = 感謝する · 나누다 = 区別する、分かち合う",
 "nl": "Uitleg — 겹치다 = samenvallen · 가늘다 = dun · 감사하다 = bedanken · 나누다 = onderscheiden, delen",
 "pt": "Nota — 겹치다 = sobrepor-se · 가늘다 = fino · 감사하다 = agradecer · 나누다 = distinguir, partilhar",
 "ru": "Пояснение — 겹치다 = совпадать · 가늘다 = тонкий · 감사하다 = благодарить · 나누다 = различать, делиться",
 "zh-tw": "譯注｜겹치다 重疊 · 가늘다 細 · 감사하다 感謝 · 나누다 區分、分享。",
}

for code, edir in EDITIONS.items():
    path = os.path.join(GOAL, "files", edir, "svg", "p3-munhwa.svg")
    root = ET.parse(path).getroot()
    els = [(float(t.get("x")), float(t.get("y")), "".join(t.itertext()))
           for t in root.iter(NS + "text")]
    # gloss anchor: node containing 겹치다
    anchor = [e for e in els if "겹치다" in e[2]][0]
    ax, ay = anchor[0], anchor[1]
    # gloss lines: nodes starting at the anchor x, from anchor y downward
    # in steps of the gloss line pitch (~29.7), while the text continues the
    # gloss (contains one of the gloss headwords or is a pure continuation
    # of the same wrapped line: take nodes with same x and y in [ay, ay+90]
    # whose text, joined, reconstructs the expected string).
    lines = sorted([e for e in els if abs(e[0] - ax) < 6 and ay - 1 <= e[1] <= ay + 90],
                   key=lambda e: e[1])
    joined = " ".join(e[2] for e in lines)
    print(code, "MATCH" if joined == EXPECTED[code] else "MISMATCH")
    print("  lines:", [e[2] for e in lines])
    if joined != EXPECTED[code]:
        print("  joined:  ", repr(joined))
        print("  expected:", repr(EXPECTED[code]))
