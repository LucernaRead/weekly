# Round 2 independent re-measurement: stems/keys continuity, level-split pairing,
# P6 chart, P7 phrases, keys-flow end-y, badge/footer geometry, model text.
import glob, json, os, re
from xml.etree import ElementTree as ET
NS = "{http://www.w3.org/2000/svg}"
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
DIRS = {"zh-cn": "weekly-report-w46-ja-core", "de": "weekly-report-w46-ja-de",
        "en": "weekly-report-w46-ja-en", "es": "weekly-report-w46-ja-es",
        "fr": "weekly-report-w46-ja-fr", "it": "weekly-report-w46-ja-it",
        "ko": "weekly-report-w46-ja-ko", "nl": "weekly-report-w46-ja-nl",
        "pt": "weekly-report-w46-ja-pt", "ru": "weekly-report-w46-ja-ru",
        "zh-tw": "weekly-report-w46-ja-zh-tw"}
def texts_of(svg):
    root = ET.parse(svg).getroot()
    return [(float(t.get("x")), float(t.get("y")), "".join(t.itertext())) for t in root.iter(NS + "text")]
def rects_of(svg):
    root = ET.parse(svg).getroot()
    return [(float(r.get("x", 0)), float(r.get("y", 0)), float(r.get("width", 0)), float(r.get("height", 0)))
            for r in root.iter(NS + "rect")]
QUOTES = ["「読書週間は、9日（月よう日）で終わります。」", "「15日（日よう日）は、七五三の中心の日です。」",
          "「『ポッキー＆プリッツの日』は、1999年に始まりました。」", "「千歳飴は、長く生きてほしい、という願いのお菓子です。」",
          "「七五三は、3歳と5歳と7歳の子どものお祝いです。」", "「ソフトバンクが4連勝で日本一になりました。」",
          "「11月11日は、ポッキーの日です。」", "「紅葉の見頃は、北から南へ移ります。」"]
QUOTE_PAGES = [1, 1, 2, 2, 3, 4, 5, 6]
out = {}
for code, d in DIRS.items():
    svgs = sorted(glob.glob(os.path.join(BASE, d, "svg", "*.svg")))
    pages = [texts_of(f) for f in svgs]
    stems = set()
    for pi in range(8):
        for x, y, s in pages[pi]:
            m = re.fullmatch(r"(\d+)\.", s.strip())
            if m: stems.add(int(m.group(1)))
            m = re.fullmatch(r"(\d+)–(\d+)\.", s.strip())
            if m: stems.update(range(int(m.group(1)), int(m.group(2)) + 1))
    keys = set()
    for x, y, s in pages[7]:
        m = re.match(r"(\d+)\.\s", s.strip())
        if m: keys.add(int(m.group(1)))
    chips = {}
    for pi in range(8):
        for x, y, s in pages[pi]:
            if s.strip() in ("A2", "B1", "B2"): chips[s.strip()] = chips.get(s.strip(), 0) + 1
    # Level pairing: each stem-number element takes the level of the nearest
    # level-badge element in the same column (x within 120) at or above it on
    # the same page; group/range headers (e.g. "141–144.") inherit likewise.
    # Column pitch is 462 (x origins 65/527/989/1451); use half-pitch window.
    split = {"A2": 0, "B1": 0, "B2": 0}
    unpaired = []
    for pi in range(8):
        badges = [(x, y, s.strip()) for x, y, s in pages[pi] if s.strip() in ("A2", "B1", "B2")]
        nums = []
        for x, y, s in pages[pi]:
            m = re.fullmatch(r"(\d+)\.", s.strip())
            if m: nums.append((x, y, int(m.group(1)), int(m.group(1))))
            m = re.fullmatch(r"(\d+)–(\d+)\.", s.strip())
            if m: nums.append((x, y, int(m.group(1)), int(m.group(2))))
        for x, y, lo, hi in nums:
            cands = [(by, bs) for bx, by, bs in badges if abs(bx - x) < 231 and by <= y + 1]
            if not cands:
                unpaired.append((pi + 1, lo, hi)); continue
            lvl = max(cands)[1]
            for n in range(lo, hi + 1): split[lvl] += 1
    p6text = "".join(s for _, _, s in pages[5])
    bars = sorted({round(w, 1) for x, y, w, h in rects_of(svgs[5]) if abs(x - 315) < 1 and w > 100})
    chart_labels = {lab: (lab in p6text) for lab in ["山", "神社", "公園", "町", "34%", "26%", "24%", "16%"]}
    norm = lambda s: re.sub(r"\s+", "", s)
    full = "".join(s for pg in pages for _, _, s in pg)
    src_pages = ["".join(s for _, _, s in pages[p - 1]) for p in QUOTE_PAGES]
    p7 = "".join(s for _, _, s in pages[6])
    phrases = []
    for q, sp in zip(QUOTES, src_pages):
        bare = q[1:-1]
        phrases.append({"phrase": q, "total": norm(full).count(norm(bare)),
                        "on_source_page": norm(bare) in norm(sp), "on_p7": norm(bare) in norm(p7)})
    keys_y = max([y for x, y, s in pages[7] if y < 2580])
    badge = None
    for x, y, s in pages[0]:
        if abs(x - 975) < 1 and abs(y - 356) < 1: badge = s
    # core subtitle geometry + fan-out subtitle/strapline/wordmark
    p1 = pages[0]
    wordmark = [s for x, y, s in p1 if abs(y - 262) < 1]
    subtitle = [(round(x,1), round(y,1), s) for x, y, s in p1 if abs(y - 316) < 1 or abs(y - 330) < 1]
    strapline = [(round(x,1), round(y,1), s) for x, y, s in p1 if abs(y - 390) < 1 or abs(y - 372) < 1]
    footer = [s for x, y, s in pages[0] if abs(y - 2624) < 1]
    out[code] = {"stems_complete": stems == set(range(1, 151)), "stems_n": len(stems),
                 "stems_missing": sorted(set(range(1, 151)) - stems),
                 "p8_keys_complete": keys == set(range(1, 151)), "p8_keys_n": len(keys),
                 "chips": chips, "level_split_pairing": split, "unpaired": unpaired,
                 "p6_bar_widths": bars, "p6_labels": chart_labels,
                 "p6_practice_label": ("練習用データ" in p6text) or ("練習數據" in p6text) or ("practice" in p6text.lower()),
                 "p7_phrases": phrases, "p8_keys_flow_max_y": round(keys_y, 1),
                 "badge_y356": badge, "wordmark_y262": wordmark,
                 "subtitle": subtitle, "strapline": strapline, "footer_p1": footer}
    print(code, "stems", len(stems), stems == set(range(1, 151)), "| keys", len(keys), keys == set(range(1, 151)),
          "| chips", chips, "| split", split, "unpaired", unpaired, "| bars", bars,
          "| phrases", [p["total"] for p in phrases], "| keysY", round(keys_y, 1), "| badge", badge)
json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "counts-round2.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote counts-round2.json")
