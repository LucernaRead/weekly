#!/usr/bin/env python3
import re, os, json, html, collections
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w46/zh-cn-proofread-gates")
PAGES = ["p1-touiban.svg","p2-shenghuo.svg","p3-wenhua.svg","p4-tiyu.svg","p5-qingnian.svg","p6-shendu.svg","p7-ciyu.svg","p8-ceyan.svg"]
EDITIONS = {"zh-cn-en":"weekly-report-w46-zh-cn-core","zh-cn-de":"weekly-report-w46-zh-cn-de","zh-cn-es":"weekly-report-w46-zh-cn-es","zh-cn-fr":"weekly-report-w46-zh-cn-fr","zh-cn-it":"weekly-report-w46-zh-cn-it","zh-cn-ja":"weekly-report-w46-zh-cn-ja","zh-cn-ko":"weekly-report-w46-zh-cn-ko","zh-cn-nl":"weekly-report-w46-zh-cn-nl","zh-cn-pt":"weekly-report-w46-zh-cn-pt","zh-cn-ru":"weekly-report-w46-zh-cn-ru"}
def texts_of(path):
    s = open(path, encoding="utf-8").read()
    out = []
    for m in re.finditer(r"<text\b([^>]*)>(.*?)</text>", s, re.S):
        txt = html.unescape(re.sub(r"<[^>]+>", "", m.group(2)))
        out.append((m.group(1), txt))
    return out, s
def all_texts(slug):
    d = os.path.join(BASE, EDITIONS[slug], "svg")
    return {p: texts_of(os.path.join(d, p)) for p in PAGES}
def level_counts(slug):
    tot = collections.Counter(); chips = []; perpage = {}
    for p, (tl, raw) in all_texts(slug).items():
        c = collections.Counter(); pc = []
        for attrs, txt in tl:
            t = txt.strip()
            if t in ("A2", "B1", "B2"):
                c[t] += 1
            m = re.fullmatch(r"(\d+)\.", t)
            if m:
                pc.append(int(m.group(1)))
        perpage[p] = (dict(c), sorted(pc))
        tot.update(c); chips += pc
    cs = sorted(chips)
    return {"levels": dict(tot), "total_level_tags": sum(tot.values()), "chips_count": len(cs),
            "chips_dupes": [k for k, v in collections.Counter(cs).items() if v > 1],
            "chips_missing": [n for n in range(1, 151) if n not in cs],
            "chips_extra": [n for n in cs if n < 1 or n > 150], "perpage": perpage}
PHRASES = ["双11的正日子","先看结算页，再决定买不买","提高自防自救能力","三支队进了八强","输了就回家","老电影，新画面","快递的高峰分三波","着火了不坐电梯"]
def phrase_counts(slug):
    joined = ""
    for p, (tl, raw) in all_texts(slug).items():
        joined += "".join(t for _, t in tl) + "\n"
    return {ph: joined.count(ph) for ph in PHRASES}
def chart_rects(slug):
    s = open(os.path.join(BASE, EDITIONS[slug], "svg", "p6-shendu.svg"), encoding="utf-8").read()
    out = []
    for r in re.findall(r"<rect[^>]*>", s):
        def g(k):
            m = re.search(k + r'="([\d.]+)"', r)
            return float(m.group(1)) if m else None
        f = re.search(r'fill="([^"]+)"', r)
        out.append((g("x"), g("y"), g("width"), g("height"), f.group(1) if f else ""))
    return out
def badge_footer(slug):
    tl, raw = all_texts(slug)["p1-touiban.svg"]
    badge = None; mast = {}
    for attrs, txt in tl:
        if 'y="434"' in attrs:
            badge = txt
        for y in ("92", "262", "330", "372", "434"):
            if 'y="%s"' % y in attrs:
                mast[y] = txt
    footers = {}
    for p, (tl3, _) in all_texts(slug).items():
        for attrs, txt in tl3:
            if 'y="2624"' in attrs:
                footers[p] = txt
    s = open(os.path.join(BASE, EDITIONS[slug], "svg", "p1-touiban.svg"), encoding="utf-8").read()
    m = re.search(r'<text[^>]*y="434"[^>]*>', s)
    return {"badge": badge, "badge_elem": m.group(0) if m else None, "footers": footers, "masthead": mast}
def script_scan(slug):
    res = {}
    for p, (tl, _) in all_texts(slug).items():
        joined = "".join(t for _, t in tl)
        res[p] = {"hangul": sum(1 for ch in joined if "\uAC00" <= ch <= "\uD7A4"),
                  "cyrillic": sum(1 for ch in joined if "\u0400" <= ch <= "\u04FF"),
                  "hiragana": sum(1 for ch in joined if "\u3040" <= ch <= "\u309F"),
                  "katakana": sum(1 for ch in joined if "\u30A0" <= ch <= "\u30FF"),
                  "hanzi": sum(1 for ch in joined if "\u4E00" <= ch <= "\u9FFF")}
    return res
TRAD_ONLY = set(list("麼魚體學讀週雙讓還過為與來東長門問間開關後發對說話語國時現見親觀歡難灣臺認議論權機歲處張帳場陽陰雲電靈龍龜點麵乾亂爭從倉側偵傳傷億儀儘僅廣廠廢彈歸當徹徑復徵德忍志忘忙忠快怎怒怕思急恆悅悉惠惡惱想愁愈愉意愛感慈態慣慘慮慶憂憑憲憶懶懷懸戀"))
def trad_scan(slug):
    hits = {}
    for p, (tl, _) in all_texts(slug).items():
        joined = "".join(t for _, t in tl)
        hits[p] = dict(collections.Counter(ch for ch in joined if ch in TRAD_ONLY))
    return hits
POLITICS = ["战争","地缘","外交","政治","选举","民调","政党","政府","领导人","主席","总理","人大","政协","台独","六四"]
def politics_scan(slug):
    hits = {}
    for p, (tl, _) in all_texts(slug).items():
        joined = "".join(t for _, t in tl)
        for w in POLITICS:
            if w in joined:
                hits.setdefault(p, []).append((w, joined.count(w)))
    return hits
READER_FACING = ["W46", "w46", "zh-cn", "2026-w46", "SOP", "proofread", "occlusion", "audit", "GitHub", "github", "insert.py", "freeze", "lint"]
def reader_scan(slug):
    hits = {}
    for p, (tl, _) in all_texts(slug).items():
        for attrs, txt in tl:
            for w in READER_FACING:
                if w in txt:
                    hits.setdefault(p, []).append((w, txt[:140]))
    return hits
NO_START = set("，。、；：？！）］｝》」』】ぁぃぅぇぉゃゅょゎっァィゥェォャュョヮッ")
NO_END = set("（［｛《「『【")
def kinsoku_scan(slug):
    flags = []
    for p, (tl, _) in all_texts(slug).items():
        for attrs, txt in tl:
            if txt and txt[0] in NO_START:
                flags.append((p, "START", txt[:70]))
            if txt and txt[-1] in NO_END:
                flags.append((p, "END", txt[:70]))
    return flags
def freeze_detail(slug):
    core = all_texts("zh-cn-en"); ed = all_texts(slug)
    out = {}
    for p in PAGES:
        c = collections.Counter(t for _, t in core[p][0]); e = collections.Counter(t for _, t in ed[p][0])
        added = e - c; removed = c - e
        added_chars = collections.Counter()
        for s, n in added.items():
            for ch in s:
                if "\u4E00" <= ch <= "\u9FFF" or "\u3040" <= ch <= "\u30FF" or "\uAC00" <= ch <= "\uD7A4" or ch in "，。、；：？！「」『』《》〈〉【】（）—…·":
                    added_chars[ch] += n
        hanzi_added = sum(n for s, n in added.items() for ch in s if "\u4E00" <= ch <= "\u9FFF")
        out[p] = {"added_strings": dict(added), "removed_strings": dict(removed),
                  "added_cjk_total": sum(added_chars.values()), "added_hanzi_total": hanzi_added,
                  "added_cjk_chars": dict(added_chars)}
    return out
if __name__ == "__main__":
    report = {}
    for slug in EDITIONS:
        report[slug] = {"levels": level_counts(slug), "phrases": phrase_counts(slug),
                        "chart": chart_rects(slug), "badge_footer": badge_footer(slug),
                        "scripts": script_scan(slug), "trad": trad_scan(slug),
                        "politics": politics_scan(slug), "reader": reader_scan(slug),
                        "kinsoku": kinsoku_scan(slug), "freeze": freeze_detail(slug)}
        lv = report[slug]["levels"]
        print(slug, "levels", lv["levels"], "chips", lv["chips_count"], "missing", lv["chips_missing"], "dupes", lv["chips_dupes"], "phrases", report[slug]["phrases"], "kinsoku", len(report[slug]["kinsoku"]))
    json.dump(report, open(os.path.join(OUT, "text-analysis.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("WROTE text-analysis.json")
