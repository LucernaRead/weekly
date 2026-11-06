# Round 2 sweeps: wrong-script / untranslated residue, reader-facing labels,
# image credits, weekday/date claims. All from shipped SVG text.
import glob, os, re, json, datetime
from xml.etree import ElementTree as ET
NS = "{http://www.w3.org/2000/svg}"
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
DIRS = {"zh-cn": "weekly-report-w46-ja-core", "de": "weekly-report-w46-ja-de",
        "en": "weekly-report-w46-ja-en", "es": "weekly-report-w46-ja-es",
        "fr": "weekly-report-w46-ja-fr", "it": "weekly-report-w46-ja-it",
        "ko": "weekly-report-w46-ja-ko", "nl": "weekly-report-w46-ja-nl",
        "pt": "weekly-report-w46-ja-pt", "ru": "weekly-report-w46-ja-ru",
        "zh-tw": "weekly-report-w46-ja-zh-tw"}
def alltext(d):
    out = []
    for fn in sorted(glob.glob(os.path.join(BASE, d, "svg", "*.svg"))):
        root = ET.parse(fn).getroot()
        for t in root.iter(NS + "text"):
            out.append((os.path.basename(fn), round(float(t.get("y")), 1), "".join(t.itertext())))
    return out
def has_hangul(s): return any(0xAC00 <= ord(c) <= 0xD7A3 for c in s)
def has_cyr(s): return any(0x0400 <= ord(c) <= 0x04FF for c in s)
def has_han(s): return any(0x4E00 <= ord(c) <= 0x9FFF for c in s)
# Chinese-prose markers: multi-char runs of Han (explanation prose) — report
# per edition; Japanese text also contains Han, so restrict to strings that
# contain Chinese-only function words / simplified-only markers.
CN_MARKERS = ["的", "是", "了", "在", "和", "我们", "你们", "他们", "这", "那"]
results = {}
for code, d in DIRS.items():
    ts = alltext(d)
    full = "\n".join(s for _, _, s in ts)
    hangul_hits = [(f, y, s) for f, y, s in ts if has_hangul(s) and code != "ko"]
    cyr_hits = [(f, y, s) for f, y, s in ts if has_cyr(s) and code != "ru"]
    # English prose residue: ASCII-letter words in non-EN editions, excluding
    # known furniture (Lucerna, VOL, Wikimedia Commons credits, DeNA, SNS, Pocky
    # latin spellings inside Japanese text, URLs). Report raw count + samples.
    ascii_words = re.findall(r"[A-Za-z]{3,}", full)
    from collections import Counter
    wc = Counter(ascii_words)
    results[code] = {"hangul_outside_ko": hangul_hits, "cyr_outside_ru": cyr_hits,
                     "ascii_word_counts": dict(wc.most_common(12))}
    print(code, "hangul_hits", len(hangul_hits), "cyr_hits", len(cyr_hits))
    for h in hangul_hits[:5] + cyr_hits[:5]: print("   ", h)
    print("   top ascii:", wc.most_common(12))
# Reader-facing sweep: forbidden internal strings anywhere in SVG text.
FORBIDDEN = ["weekly-report", "github", "SOP", "proofread", "occlusion", "lint",
             "index.json", "VOL.4 制作", "cover", "COVER"]
print("== reader-facing ==")
for code, d in DIRS.items():
    ts = alltext(d)
    hits = [(f, y, s) for f, y, s in ts for b in FORBIDDEN if b.lower() in s.lower()]
    print(code, "forbidden hits:", len(hits))
    for h in hits: print("   ", h)
# Image credits: the 3 photos must be credited on-page.
print("== credits ==")
for code, d in DIRS.items():
    ts = alltext(d)
    full = " ".join(s for _, _, s in ts)
    print(code, "Poliphilo", "Poliphilo" in full, "| Hiroshige", "歌川広重" in full,
          "| Syced", "Syced" in full, "| CC0", full.count("CC0"), "| PD", "パブリックドメイン" in full or "public domain" in full.lower())
# Weekday/date verification against the real calendar.
print("== dates ==")
claims = [("2026-10-24", "土"), ("2026-10-25", "日"), ("2026-10-27", "火"),
          ("2026-10-28", "水"), ("2026-11-09", "月"), ("2026-11-11", "水"),
          ("2026-11-15", "日"), ("2026-11-13", "金"), ("2026-11-19", "木"),
          ("2026-11-21", "土"), ("2026-11-22", "日"), ("2026-11-23", "月"),
          ("2026-11-29", "日"), ("2026-12-04", "金"), ("2026-11-07", "土")]
JP = ["月", "火", "水", "木", "金", "土", "日"]
for ds, wd in claims:
    dt = datetime.date.fromisoformat(ds)
    print(ds, dt.strftime("%A"), "JP:", JP[dt.weekday()], "claim:", wd, "OK" if JP[dt.weekday()] == wd else "MISMATCH")
json.dump(results, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "sweeps-round2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
