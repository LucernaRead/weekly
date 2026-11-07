#!/usr/bin/env python3
"""Supplementary re-gate measurements for the W46 zh-cn D3/D4 fix.
- Per-page exercise-number counts from SVG text nodes (bare chips + range headers expanded).
- P7 phrase counts (joined SVG text, per edition): each of the 8 phrases exactly 2x.
- P6 chart rects: x/widths/heights/ys/fills.
- Kinsoku scan: line-start NO_START / line-end NO_END characters at text-node edges.
- P8 corrected-key lines: first text-node fragment starting with '25. '/'26. '/'27. '/'99. '/'100. '.
Writes counts-phrases-chart.json + kinsoku.log + p8-corrected-keys.txt under gates/.
"""
import json, os, re, sys, html

ROOT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
G = os.path.join(ROOT, "hidden_files/w46/zh-cn-fix-keys/gates")
os.makedirs(G, exist_ok=True)
LANGS = ["en", "de", "es", "fr", "it", "ja", "ko", "nl", "pt", "ru"]
PAGES = ["p1-touiban", "p2-shenghuo", "p3-wenhua", "p4-tiyu", "p5-qingnian",
         "p6-shendu", "p7-ciyu", "p8-ceyan"]
PHRASES = ["双11的正日子", "先看结算页，再决定买不买", "提高自防自救能力",
           "三支队进了八强", "输了就回家", "老电影，新画面",
           "快递的高峰分三波", "着火了不坐电梯"]
TEXT_RE = re.compile(r'<text [^>]*>([^<]*)</text>')
RECT_RE = re.compile(r'<rect x="([0-9.]+)" y="([0-9.]+)" width="([0-9.]+)" height="([0-9.]+)"[^>]*fill="([^"]+)"')

def ed_dir(lang):
    return os.path.join(ROOT, "files/weekly-report-w46-zh-cn-core" if lang == "en"
                        else f"files/weekly-report-w46-zh-cn-{lang}")

def texts_of(path):
    raw = open(path, encoding="utf-8").read()
    return [html.unescape(m.group(1)) for m in TEXT_RE.finditer(raw)], raw

result = {}
for lang in LANGS:
    ed = ed_dir(lang)
    per_page = {}
    all_text = []
    for pg in PAGES:
        ts, _ = texts_of(os.path.join(ed, "svg", pg + ".svg"))
        all_text.extend(ts)
        nums = set()
        for t in ts:
            s = t.strip()
            m = re.fullmatch(r"(\d+)–(\d+)\.", s)
            if m:
                nums.update(range(int(m.group(1)), int(m.group(2)) + 1))
                continue
            m = re.fullmatch(r"(\d+)\.", s)
            if m:
                nums.add(int(m.group(1)))
        per_page[pg] = sorted(nums)
    joined = "".join(all_text)
    phrases = {p: joined.count(p) for p in PHRASES}
    # P6 chart
    _, raw6 = texts_of(os.path.join(ed, "svg", "p6-shendu.svg"))
    rects = [(float(x), float(y), float(w), float(h), f)
             for x, y, w, h, f in RECT_RE.findall(raw6)]
    bars = [r for r in rects if r[3] == 30 and r[0] == 325]
    # P8 corrected keys: first fragment per number
    ts8, _ = texts_of(os.path.join(ed, "svg", "p8-ceyan.svg"))
    keys = {}
    for want in (25, 26, 27, 99, 100):
        for t in ts8:
            if t.startswith(f"{want}. "):
                keys[want] = t
                break
    result[lang] = {
        "per_page_counts": {k: len(v) for k, v in per_page.items()},
        "per_page_numbers": per_page,
        "total_unique": len(set().union(*[set(v) for v in per_page.values()])),
        "phrases": phrases,
        "p6_bars": bars,
        "p8_corrected_key_fragments": keys,
    }
    print(lang, "counts", result[lang]["per_page_counts"],
          "total", result[lang]["total_unique"],
          "phrases", phrases, "bars", bars)
    print(lang, "P8 corrected:", keys)

json.dump(result, open(os.path.join(G, "counts-phrases-chart.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

# --- kinsoku ---
NO_START = set("、，。．,.)）]」』〕〉》】％!！?？:：;；ぁぃぅぇぉっゃゅょゎァィゥェォッャュョヮ")
NO_END = set("（(「『〔〈《【")
kin_lines = []
for lang in LANGS:
    ed = ed_dir(lang)
    flags = []
    for pg in PAGES:
        ts, _ = texts_of(os.path.join(ed, "svg", pg + ".svg"))
        for t in ts:
            s = t.strip()
            if not s:
                continue
            if s[0] in NO_START:
                flags.append(f"{pg}: START {s[:30]!r}")
            if s[-1] in NO_END:
                flags.append(f"{pg}: END {s[:30]!r}")
    kin_lines.append(f"{lang}: {len(flags)} flags")
    kin_lines.extend("  " + f for f in flags)
    print(lang, "kinsoku flags:", len(flags))
open(os.path.join(G, "kinsoku.log"), "w", encoding="utf-8").write("\n".join(kin_lines) + "\n")

# --- P8 corrected keys flat file ---
lines = []
for lang in LANGS:
    for n in (25, 26, 27, 99, 100):
        lines.append(f"{lang} {n}. {result[lang]['p8_corrected_key_fragments'].get(n, 'MISSING')}")
open(os.path.join(G, "p8-corrected-keys.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
print("DONE")
