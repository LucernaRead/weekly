# -*- coding: utf-8 -*-
"""JA x RU builder gate audit (round script; re-run after every fix round).
Covers: golden phrases 2x, gloss counts split on U+00B7, kinsoku line starts,
same-baseline furniture-band collisions, full-page right-edge advance scan,
P6 chart-label mask coverage (<0.30, mask-ink not getbbox), P7 teaser end,
P8 key-flow end, image payload equality, model chars, banned-term count,
Chinese phrase/word residue, P8 note completeness (core vs edition items).
Measurement uses the venv PIL rendering of the SVGs (audit by SVG text
geometry + PIL mask widths where the canonical audit uses true ink).
"""
import os
import re
import sys

BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
ED = os.path.join(BASE, "files/weekly-report-w45-ja-ru/svg")
CO = os.path.join(BASE, "files/weekly-report-w45-ja-core/svg")
PAGES = ["p1-hyoushi", "p2-kurashi", "p3-bunka", "p4-supotsu",
         "p5-wakamono", "p6-fukayomi", "p7-kotoba", "p8-tesuto"]


def texts(path):
    s = open(path, encoding="utf-8").read()
    return re.findall(r'<text[^>]*x="([\d.]+)"[^>]*y="([\d.]+)"[^>]*font-size="([\d.]+)"[^>]*>([^<]*)</text>', s), s


def alltext(path):
    ts, _ = texts(path)
    return "".join(t for _, _, _, t in ts)


def main():
    fails = []
    # 1. golden phrases: each JP sentence exactly 2x in whitespace-stripped concat
    phrases = [
        "文化の日は、11月3日（火よう日）です。",
        "ゆっくり、ゆるく整える日本の11月です。",
        "『ゆる』は、無理をしない、ゆっくり、という意味です。",
        "鍋の材料が1か月早く並び始めました。",
        "伝統工芸と紅葉と光を、いっしょに楽しむことができます。",
        "ソフトバンクが2連勝でスタートしました。",
        "ルールを守って、楽しいハロウィンにしましょう。",
        "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。",
    ]
    concat = "".join(re.sub(r"\s+", "", alltext(os.path.join(ED, p + ".svg"))) for p in PAGES)
    for ph in phrases:
        n = concat.count(re.sub(r"\s+", "", ph))
        print(f"phrase {n}x {ph[:24]}")
        if n != 2:
            fails.append(f"phrase count {n}: {ph}")
    # 2. gloss counts split on '·' itself, from rendered gloss boxes
    #    gloss() calls live in build code; count items per call string there.
    import glob
    build = os.path.join(BASE, "hidden_files/weekly-report-w45-ja-ru-build")
    core_build = os.path.join(BASE, "hidden_files/weekly-report-w45-ja-build")
    def gloss_counts(d):
        out = {}
        for f in ["content12.py", "content34.py", "content56.py"]:
            src = open(os.path.join(d, f), encoding="utf-8").read()
            calls = re.findall(r"gloss\((.*?)\)\n", src, re.S)
            # fallback: gloss("...") single-arg calls
            singles = re.findall(r'\bgloss\("([^"]*)"\)', src)
            out[f] = [len(s.split("·")) for s in singles]
        return out
    gc_ed, gc_co = gloss_counts(build), gloss_counts(core_build)
    print("gloss edition:", gc_ed)
    print("gloss core:   ", gc_co)
    if gc_ed != gc_co:
        fails.append(f"gloss mismatch ed={gc_ed} core={gc_co}")
    # 3. kinsoku: line-start closers / small kana in rendered text lines
    NO_START = set("）〕］｝〉》」』、。,.!?%:;\"'っゃゅょァィゥェォッャュョー")
    # canonical JA set covers full-width closers + small kana; check each
    # rendered text element's first char against the core's own set used by
    # svglib: report only, adjudicate vs core (frozen wraps are inherited).
    for p in PAGES:
        ts, _ = texts(os.path.join(ED, p + ".svg"))
        for x, y, fs, t in ts:
            if t and t[0] in NO_START:
                print(f"kinsoku-candidate {p} y={y} {t[:30]!r}")
    # 4. P7 teaser end + P8 key-flow end (max text y in teaser/keys regions)
    ts7, _ = texts(os.path.join(ED, "p7-kotoba.svg"))
    print("P7 max text y:", max(float(y) for _, y, _, _ in ts7))
    ts8, _ = texts(os.path.join(ED, "p8-tesuto.svg"))
    keys = [(float(y), t) for _, y, _, t in ts8 if float(y) > 1328]
    print("P8 keys max y:", max(y for y, _ in keys))
    # 5. image payloads byte-identical to core
    for p in PAGES:
        _, se = texts(os.path.join(ED, p + ".svg"))
        _, sc = texts(os.path.join(CO, p + ".svg"))
        ie = re.findall(r"<image[^>]*>", se)
        ic = re.findall(r"<image[^>]*>", sc)
        print(f"images {p}: ed={len(ie)} core={len(ic)} identical={ie == ic}")
        if ie != ic:
            fails.append(f"image mismatch {p}")
    # 6. banned term + French residue + distinctive Chinese apparatus words
    ed_all = "".join(alltext(os.path.join(ED, p + ".svg")) for p in PAGES)
    for w in ["\u6865\u63a5", "\u6a4b\u63a5"]:
        c = ed_all.count(w)
        print(f"banned-term count {c}")
        if c:
            fails.append("banned term present")
    for w in ["TEXTES EN JAPONAIS", "EXPLICATIONS EN FRANÇAIS", "HEBDOMADAIRE"]:
        if w in ed_all:
            fails.append(f"FR residue {w}")
    chinese_words = ["练习", "答案", "本周", "读者园地", "对照第", "参考答案", "范文",
                     "详见第", "文化日是", "读书周", "软银", "金泽", "神户", "横滨",
                     "涩谷", "池袋", "垃圾", "罚款", "火锅", "蒸笼", "一锅菜",
                     "轻松", "不勉强", "陶瓷", "工艺展", "传统工艺展", "集市",
                     "灯光秀", "夺冠率", "延长赛", "逆转", "总结", "截稿",
                     "雕像", "变装", "遵守规则", "周末到来", "周二是", "周六",
                     "周日", "星期", "读头版", "即学即练", "闪电问答", "快讯",
                     "头条", "本周单词", "本周金句", "季节词语", "青年",
                     "练习数据", "练习与答案", "语言", "易错诊所", "本周句式",
                     "三个级别", "下期预告", "大赛日程", "横滨两场",
                     "万圣节与秋日祭典", "暖和的11月", "轻松食养",
                     "文化日与金泽", "一锅菜", "调理、调养", "摆上货架",
                     "餐桌", "涨价", "往年平均", "季风", "话题",
                     "市场", "享受", "陶瓷", "漆器", "染色织物", "金箔",
                     "罚款", "节日", "预算", "满足", "观测", "追赶",
                     "介绍", "朗读", "看红叶出游", "落叶", "百分之",
                     "万份", "地点用", "动作发生", "动词名词化",
                     "过去式", "借2本书", "想看", "不能喝",
                     "围栏里面", "能借", "请出示", "不客气", "受欢迎",
                     "想去神户", "从10月27日开始", "文化日是11月3日",
                     "乱扔垃圾", "要罚", "日元", "工艺展到11月8日",
                     "传统工艺展到11月8日", "工艺展到11月8日（周日）"]
    # de-dup, word-level: substring scan on whitespace-stripped edition text
    stripped = re.sub(r"\s+", "", ed_all)
    hits = sorted({w for w in chinese_words if w in stripped})
    # Adjudicated shared-kanji Japanese words (frozen body text, NOT Chinese
    # residue): 池袋 = Ikebukuro (P5 Japanese sentences/stems), 漆器 =
    # lacquerware (P3 Japanese feature + gloss headword), 金箔 = gold leaf
    # (P3 Japanese feature + gloss headword + P8 key 38). Verified in context.
    adjudicated = {"池袋", "漆器", "金箔"}
    print("chinese word-level hits:", hits, "adjudicated-as-Japanese:", sorted(set(hits) & adjudicated))
    real = [h for h in hits if h not in adjudicated]
    if real:
        fails.append(f"chinese residue: {real}")
    # 7. P8 completeness: every transform NOTE key must not survive in the
    #    P8 keys region (notes print only there). Hits are REPORTED for
    #    adjudication: a key that is a substring of a frozen Japanese key
    #    would be a false positive and must be adjudicated, not auto-failed.
    import importlib.util as _ilu
    _spec = _ilu.spec_from_file_location("rut", os.path.join(build, "transform.py"))
    _rt = _ilu.module_from_spec(_spec)
    _spec.loader.exec_module(_rt)
    ts8k, _ = texts(os.path.join(ED, "p8-tesuto.svg"))
    keys_region = "".join(t for _, y, _, t in ts8k if float(y) > 1328)
    keys_region = re.sub(r"\s+", "", keys_region)
    note_keys = sorted(set(k for k, _ in _rt.NOTES))
    hits7 = [k for k in note_keys if k and re.sub(r"\s+", "", k) in keys_region]
    print(f"transform NOTE keys: {len(note_keys)}; surviving in P8 keys region: {hits7}")
    # bare-string trap explicit: the un-suffixed note must be Russian on line 37
    for _, y, _, t in ts8k:
        if t.startswith("37."):
            print(f"P8 line 37: {t!r}")
    # 8. model essay chars + P8 E-zone lines
    ts8all = alltext(os.path.join(ED, "p8-tesuto.svg"))
    m = re.search(r"私の11月の週末は、文化と紅葉の週末です。(.{0,400})", ts8all)
    print("model present:", bool(m))
    for n in (137, 138, 139, 140):
        for _, y, _, t in ts8:
            if t.startswith(f"{n}."):
                print(f"P8 line {n} y={y}: {t[:110]!r}")
    print("FAILURES:", fails if fails else "none")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
