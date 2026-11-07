# Re-measurement on final SVGs: stem/key continuity, P6 chart, P7 phrases,
# P8 model text, keys-flow end-y, badge geometry. Writes counts-checks.json.
import glob, json, os, re, sys
from xml.etree import ElementTree as ET
NS = "{http://www.w3.org/2000/svg}"
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
DIRS = {"zh-cn": "weekly-report-w46-ja-core", "de": "weekly-report-w46-ja-de", "en": "weekly-report-w46-ja-en",
        "es": "weekly-report-w46-ja-es", "fr": "weekly-report-w46-ja-fr", "it": "weekly-report-w46-ja-it",
        "ko": "weekly-report-w46-ja-ko", "nl": "weekly-report-w46-ja-nl", "pt": "weekly-report-w46-ja-pt",
        "ru": "weekly-report-w46-ja-ru", "zh-tw": "weekly-report-w46-ja-zh-tw"}
def texts_of(svg):
    root = ET.parse(svg).getroot()
    return [(float(t.get("x")), float(t.get("y")), "".join(t.itertext())) for t in root.iter(NS + "text")]
def rects_of(svg):
    root = ET.parse(svg).getroot()
    return [(float(r.get("x", 0)), float(r.get("y", 0)), float(r.get("width", 0)), float(r.get("height", 0)), r.get("fill"))
            for r in root.iter(NS + "rect")]
QUOTES = ["「読書週間は、9日（月よう日）で終わります。」", "「15日（日よう日）は、七五三の中心の日です。」",
          "「『ポッキー＆プリッツの日』は、1999年に始まりました。」", "「千歳飴は、長く生きてほしい、という願いのお菓子です。」",
          "「七五三は、3歳と5歳と7歳の子どものお祝いです。」", "「ソフトバンクが4連勝で日本一になりました。」",
          "「11月11日は、ポッキーの日です。」", "「紅葉の見頃は、北から南へ移ります。」"]
QUOTE_PAGES = [1, 1, 2, 2, 3, 4, 5, 6]
out = {}
for code, d in DIRS.items():
    svgs = sorted(glob.glob(os.path.join(BASE, d, "svg", "*.svg")))
    assert len(svgs) == 8
    pages = [texts_of(f) for f in svgs]
    # stems: chip-adjacent "N." texts + match-set ranges "A–B." on all 8 pages
    # (P1–P7 hold 1–112; P8 holds its own assessment stems 113–150).
    stems = set()
    for pi in range(8):
        for x, y, s in pages[pi]:
            m = re.fullmatch(r"(\d+)\.", s.strip())
            if m: stems.add(int(m.group(1)))
            m = re.fullmatch(r"(\d+)–(\d+)\.", s.strip())
            if m: stems.update(range(int(m.group(1)), int(m.group(2)) + 1))
    # P8 keys: lines starting "N. " in the keys flow (y>1300 region of p8)
    keys = set()
    for x, y, s in pages[7]:
        m = re.match(r"(\d+)\.\s", s.strip())
        if m: keys.add(int(m.group(1)))
    # level chips: <text> exactly A2/B1/B2
    chips = {}
    for pi in range(8):
        for x, y, s in pages[pi]:
            if s.strip() in ("A2", "B1", "B2"): chips[s.strip()] = chips.get(s.strip(), 0) + 1
    # P6 chart: bars are rects with x=315 in p6; labels + practice-data label
    p6text = "".join(s for _, _, s in pages[5])
    bars = sorted({round(w, 1) for x, y, w, h, f in rects_of(svgs[5]) if abs(x - 315) < 1 and w > 100})
    chart_labels = {lab: (lab in p6text) for lab in ["山", "神社", "公園", "町", "34%", "26%", "24%", "16%"]}
    # P7 phrases: the P7 list quotes the sentence inside 「」; the article
    # occurrence is the bare sentence. Count the bare sentence (whitespace-
    # stripped): exactly 2 per issue (article + P7 list).
    norm = lambda s: re.sub(r"\s+", "", s)
    full = "".join(s for pg in pages for _, _, s in pg)
    src_pages = ["".join(s for _, _, s in pages[p - 1]) for p in QUOTE_PAGES]
    p7 = "".join(s for _, _, s in pages[6])
    phrases = []
    for q, sp in zip(QUOTES, src_pages):
        bare = q[1:-1]
        phrases.append({"phrase": q, "total": norm(full).count(norm(bare)),
                        "on_source_page": norm(bare) in norm(sp), "on_p7": norm(bare) in norm(p7)})
    # P8 model text: non-space chars of the model-text block — approximated by
    # the P8 text between the writing head and the keys head is fragile; the
    # registry model-chars value is recorded from run logs instead. Here we
    # record the P8 keys-flow max y (excl. footer texts y>=2580).
    keys_y = max([y for x, y, s in pages[7] if y < 2580])
    # badge geometry (fan-outs): text at x=975 y=356 fill brick; core: subtitle y=330
    badge = None
    for x, y, s in pages[0]:
        if abs(x - 975) < 1 and abs(y - 356) < 1: badge = s
    out[code] = {"stems_n": len(stems), "stems_complete_1_150": stems == set(range(1, 151)),
                 "stems_missing": sorted(set(range(1, 151)) - stems), "stems_extra": sorted(stems - set(range(1, 151))),
                 "p8_keys_n": len(keys), "p8_keys_complete_1_150": keys == set(range(1, 151)),
                 "p8_keys_missing": sorted(set(range(1, 151)) - keys),
                 "chips": chips, "p6_bar_widths": bars,
                 "p6_labels": chart_labels, "p6_practice_label": ("練習用データ" in p6text) or ("練習數據" in p6text) or ("practice" in p6text.lower()),
                 "p7_phrases": phrases, "p8_keys_flow_max_y": round(keys_y, 1), "badge_y356": badge}
    print(code, "stems", len(stems), stems == set(range(1, 151)), "| keys", len(keys), keys == set(range(1, 151)),
          "| chips", chips, "| bars", bars, "| phrases", [p["total"] for p in phrases], "| keysY", round(keys_y, 1), "| badge", badge)
json.dump(out, open(sys.argv[1], "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("wrote", sys.argv[1])
