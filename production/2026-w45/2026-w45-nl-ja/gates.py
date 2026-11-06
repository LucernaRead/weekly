# -*- coding: utf-8 -*-
"""NL x JA W45 gate scans (builder-run, rendered SVGs + build code)."""
import re, os, sys
BASE = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files")
ED = os.path.join(BASE, "weekly-report-w45-nl-ja/svg")
CORE = os.path.join(BASE, "weekly-report-w45-nl-core/svg")
BUILD = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-nl-ja-build")

def texts(path):
    t = open(path, encoding="utf-8").read()
    return re.findall(r'<text[^>]*>([^<]*)</text>', t)

def joined(path, sep=" "):
    return sep.join(texts(path))

# ---- 1. gloss counts: split rendered gloss() strings on '·' in build code ----
print("== GLOSS (build code gloss strings, split on '·') ==")
for f, pg in [("content12.py", "P2"), ("content34.py", "P3/P4"),
               ("content56.py", "P5/P6")]:
    t = open(os.path.join(BUILD, f), encoding="utf-8").read()
    for m in re.finditer(r'\.gloss\("([^"]+)"\)', t):
        s = m.group(1)
        items = [x for x in s.split("·")]
        print(f"  {pg}: {len(items)} items :: {s[:70]}")
print("  P1 expl items:", len('de Klimaatweek 気候週間 · de boom planten 植樹 · besparen 節約する · de waarschuwing 警報。'.split("·")))

# ---- 2. golden sentences: 2x each + page tags + presence on tagged page ----
print("== GOLDEN SENTENCES ==")
quotes = [
    ("«Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland»", "Pagina 1", "p1-voorpagina.svg"),
    ("«De herfst is de beste tijd om te planten»", "Pagina 1", "p1-voorpagina.svg"),
    ("«Geel betekent: let op, het weer kan gevaarlijk zijn»", "Pagina 2", "p2-leven.svg"),
    ("«Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts»", "Pagina 3", "p3-cultuur.svg"),
    ("«Ajax won donderdag 22 oktober met 2–0 van Atalanta»", "Pagina 4", "p4-sport.svg"),
    ("«Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur»", "Pagina 5", "p5-jongeren.svg"),
    ("«Een code is geen verbod, maar een advies»", "Pagina 6", "p6-verdieping.svg"),
    ("«Het weer is van ons allemaal, maar het raakt ons allemaal anders»", "Pagina 6", "p6-verdieping.svg"),
]
p7 = joined(os.path.join(ED, "p7-taal.svg"))
for q, pg, src in quotes:
    q_inner = q.strip("«»")
    cnt = 0
    for f in sorted(os.listdir(ED)):
        j = joined(os.path.join(ED, f))
        # line-joined: Dutch lines join with space; count occurrences of inner text
        cnt += j.count(q_inner)
    onpage = q_inner in joined(os.path.join(ED, src))
    # P7 tag: translation + (Pagina N) — check tag text exists on P7
    tag_on_p7 = ("(" + pg + ")") in p7
    print(f"  {pg} src={src} total_occ={cnt} on_tagged_page={onpage} tag_on_P7={tag_on_p7} :: {q_inner[:50]}")

# ---- 3. readers' corner ----
print("== READERS CORNER (P7) ==")
p7j = joined(os.path.join(ED, "p7-taal.svg"), "")
checks = {
    "NL disclosure verbatim": "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3." in p7j,
    "JA disclosure (3 facts)": "締切時に本物の手紙と8ページの優秀作文はなく、編集部の例文を掲載。約束はVOL.3へ。" in p7j,
    "JA invitation imperative+promise": "あなたの本物の手紙と8ページの優秀作文を送ってください。VOL.3に掲載します！" in p7j,
    "example labeled editors": "編集部の例文を掲載" in p7j,
    "NL example signature kept": "Li (voorbeeldbrief van de redactie)" in " ".join(texts(os.path.join(ED, "p7-taal.svg"))),
}
for k, v in checks.items():
    print(f"  {k}: {v}")

# ---- 4. JA line-start orphan scan (rendered SVGs): NO_START closers + small kana ----
print("== JA ORPHAN SCAN (line-start closers / small kana, all 8 SVGs) ==")
NO_START = set("。、，．！？：；）」』】ー…‥・")
SMALL = set("ぁぃぅぇぉゃゅょっァィゥェォャュョッ")
hits = []
for f in sorted(os.listdir(ED)):
    for i, s in enumerate(texts(os.path.join(ED, f))):
        if s and (s[0] in NO_START or s[0] in SMALL):
            hits.append((f, i, s[:40]))
print(f"  hits: {len(hits)}")
for h in hits[:20]:
    print("   ", h)

# ---- 5. banned / residue scans ----
print("== BANNED + RESIDUE (all 8 SVGs, joined) ==")
allj = ""
for f in sorted(os.listdir(ED)):
    allj += joined(os.path.join(ED, f), "") + "\n"
for label, pat in [
    ("桥接", "桥接"), ("译注", "译注"), ("讲解", "讲解"),
    ("简体家具 练习与答案", "练习与答案"), ("简体 参考答案", "参考答案"),
    ("简体 中文简析", "中文简析"), ("简体 本周", "本周"), ("简体 第 8 版", "第 8 版"),
    ("Cyrillic", r"[\u0400-\u04FF]"),
    ("Hangul", r"[\uAC00-\uD7A3]"),
    ("DE furniture ERKLÄRUNGEN", "ERKLÄRUNGEN"),
    ("EN furniture EXPLANATIONS IN", "EXPLANATIONS IN ENGLISH"),
    ("PT furniture EXPLICAÇÕES", "EXPLICAÇÕES"),
    ("FR furniture EXPLICATIONS", "EXPLICATIONS EN FRAN"),
    ("double prefix 解説 — 解説", "解説 — 解説"),
]:
    n = len(re.findall(pat, allj))
    print(f"  {label}: {n}")
# P8 notes: full-width paren count vs half-width paren in P8 answer lines
p8 = texts(os.path.join(ED, "p8-toets.svg"))
ans = [s for s in p8 if re.match(r"\d+\.", s)]
fw = sum(s.count("（") for s in ans)
hw = sum(s.count("(") for s in ans)
print(f"  P8 answer lines: {len(ans)}, full-width parens （: {fw}, half-width (: {hw}")
print(f"  P8 half-width paren lines (should be only Dutch bodies, e.g. options):")
for s in ans:
    if "(" in s:
        print("    ", s[:100])

# ---- 6. images + credits ----
print("== IMAGES + CREDITS ==")
credits = {"p1-voorpagina.svg": "Foto: Vovogov90 — CC0",
           "p2-leven.svg": "Foto: Nationaal Archief — CC0",
           "p3-cultuur.svg": "Foto: W. Punt / Anefo, Nationaal Archief — CC0",
           "p4-sport.svg": "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein"}
for f in sorted(os.listdir(ED)):
    raw = open(os.path.join(ED, f), encoding="utf-8").read()
    n_img = len(re.findall(r"<image ", raw))
    cr = credits.get(f)
    print(f"  {f}: <image> x{n_img}" + (f" credit present={cr in raw}" if cr else " (no photo page)"))

# ---- 7. furniture ----
print("== FURNITURE ==")
for f in sorted(os.listdir(ED)):
    j = joined(os.path.join(ED, f), "")
    foot = "De Lucerna · オランダ語週刊 VOL.2 · 本文はオランダ語 · 解説は日本語" in j
    print(f"  {f}: footer={foot}")
p1 = joined(os.path.join(ED, "p1-voorpagina.svg"), "")
print("  badge:", "オランダ語テキスト · 日本語の解説 — 日本語読者のための版" in p1)
print("  topstrip:", "ELKE WEEK IN HET NEDERLANDS · 毎週一号 · オランダ人が読んでいるオランダ語を読む" in p1)
print("  flower:", "オ ラ ン ダ 語 週 刊 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12" in p1)
for n in range(1, 9):
    pg = ["p1-voorpagina.svg", "p2-leven.svg", "p3-cultuur.svg", "p4-sport.svg",
          "p5-jongeren.svg", "p6-verdieping.svg", "p7-taal.svg", "p8-toets.svg"][n - 1]
    j = joined(os.path.join(ED, pg), "")
    print(f"  page line {n}: {f'{n} ページ（全 8 ページ）' in j}")
p8j = joined(os.path.join(ED, "p8-toets.svg"), "")
print("  P8 head:", "ANTWOORDEN · 全解答と解説（1–8ページ）" in p8j)
for n in range(1, 9):
    print(f"  P8 separator {n}: {f'— {n} ページ —' in p8j}")
print("  P8 band:", "TOETS EN ANTWOORDEN · テストと解答" in p8j)
