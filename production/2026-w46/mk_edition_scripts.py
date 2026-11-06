# -*- coding: utf-8 -*-
"""Derive render.py + verify.py for a W46 DE fan-out from the EN versions.
Usage: mk_edition_scripts.py <code>
Config lives in EDITION_CONFIGS below (one entry per reader language).
"""
import json, os, re, sys

CODE = sys.argv[1]
G = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")

CONFIGS = {
"es": dict(
    suffix="ES", footer="Die Lucerna · SEMANARIO ALEMÁN VOL.3 · TEXTO EN ALEMÁN · EXPLICACIONES EN ESPAÑOL",
    pageline_re=r"Página \d de 8", badge="TEXTOS EN ALEMÁN · EXPLICACIONES EN ESPAÑOL",
    topstrip="WÖCHENTLICH AUF DEUTSCH · CADA SEMANA · EL ALEMÁN QUE LEEN LOS ALEMANES",
    chart=["fútbol", "fiestas", "memoria"], muster_re=r"MUSTER · Texto modelo \((\d+) palabras\)",
    paren_check="(3.ª pers. sing.)", separator_re=r"— Página \d —", cjk_scan=True),
"it": dict(
    suffix="IT", footer="Die Lucerna · SETTIMANALE TEDESCO VOL.3 · TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO",
    pageline_re=r"Pagina \d di 8", badge="TESTI IN TEDESCO · SPIEGAZIONI IN ITALIANO",
    topstrip="WÖCHENTLICH AUF DEUTSCH · OGNI SETTIMANA · IL TEDESCO CHE LEGGONO I TEDESCHI",
    chart=["calcio", "feste", "memoria"], muster_re=r"MUSTER · Testo modello \((\d+) parole\)",
    paren_check="(3ª pers. sing.)", separator_re=r"— PAGINA \d —", cjk_scan=True),
"pt": dict(
    suffix="PT", footer="Die Lucerna · SEMANÁRIO ALEMÃO VOL.3 · TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS",
    pageline_re=r"Página \d de 8", badge="TEXTOS EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS",
    topstrip="WÖCHENTLICH AUF DEUTSCH · TODA SEMANA · O ALEMÃO QUE OS ALEMÃES LEEM",
    chart=["futebol", "festas", "memória"], muster_re=r"MUSTER · Texto-modelo \((\d+) palavras\)",
    paren_check="(3.ª pessoa do singular)", separator_re=r"— Página \d —", cjk_scan=True),
"nl": dict(
    suffix="NL", footer="Die Lucerna · DUITS WEEKBLAD VOL.3 · TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS",
    pageline_re=r"Pagina \d van 8", badge="TEKSTEN IN HET DUITS · UITLEG IN HET NEDERLANDS",
    topstrip="WÖCHENTLICH AUF DEUTSCH · ELKE WEEK · HET DUITS DAT DE DUITSERS LEZEN",
    chart=["voetbal", "feesten", "herdenking"], muster_re=r"MUSTER · Voorbeeldtekst \((\d+) woorden\)",
    paren_check="(3e persoon enkelvoud)", separator_re=r"— Pagina \d —", cjk_scan=True),
"ru": dict(
    suffix="RU", footer="Die Lucerna · НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ",
    pageline_re=r"Страница \d из 8", badge="ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ",
    topstrip="WÖCHENTLICH AUF DEUTSCH · КАЖДУЮ НЕДЕЛЮ · НЕМЕЦКИЙ, КОТОРЫЙ ЧИТАЮТ НЕМЦЫ",
    chart=["футбол", "праздники", "память"], muster_re=r"MUSTER · Образец \((\d+) слова\)",
    paren_check="(3-е лицо ед. ч.)", separator_re=r"— СТРАНИЦА \d —", cjk_scan=True),
"ja": dict(
    suffix="JA", footer="Die Lucerna · ドイツ語週刊 VOL.3 · 本文はドイツ語 · 解説は日本語",
    pageline_re=r"\d ページ（全 8 ページ）", badge="ドイツ語テキスト · 日本語の解説",
    topstrip="WÖCHENTLICH AUF DEUTSCH · 毎週一号 · ドイツ人が読んでいるドイツ語を読む",
    chart=["サッカー", "祭り", "追悼"], muster_re=r"MUSTER · 模範文（84 Wörter）",
    paren_check="(3人称単数)", separator_re=r"— \d ページ —", cjk_scan=False),
"ko": dict(
    suffix="KO", footer="Die Lucerna · 독일어 주간지 VOL.3 · 텍스트는 독일어 · 해설은 한국어",
    pageline_re=r"제 \d 면 / 총 8 면", badge="독일어 텍스트 · 한국어 해설",
    topstrip="WÖCHENTLICH AUF DEUTSCH · 매주 발행 · 독일이 읽는 독일어",
    chart=["축구", "축제", "추모"], muster_re=r"MUSTER · 모범 답안 \(84단어\)",
    paren_check="(3인칭 단수)", separator_re=r"— 제 \d 면 —", cjk_scan=False),
"zh-tw": dict(
    suffix="ZH-TW", footer="Die Lucerna · 德語週報 VOL.3 · 正文德語 · 講解繁體中文",
    pageline_re=r"第 \d 版 / 共 8 版", badge="德語正文 · 繁體中文講解",
    topstrip="WÖCHENTLICH AUF DEUTSCH · 每週一期 · 讀德國人正在讀的德語",
    chart=["足球", "節日", "紀念"], muster_re=r"MUSTER · 範本（84 Wörter）",
    paren_check="(第三人稱單數)", separator_re=r"— 第 \d 版 —", cjk_scan=False),
"zh-cn": dict(
    suffix="ZH-CN", footer="Die Lucerna · 德语周报 VOL.3 · LUCERNA GERMAN WEEKLY",
    pageline_re=r"第 \d 版 / 共 8 版", badge="DIE WOCHENZEITUNG FÜR LERNENDE",
    topstrip="WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语",
    chart=["足球", "节日", "纪念"], muster_re=r"MUSTER · 范文（84 Wörter）",
    paren_check="（第三人称单数）", separator_re=r"— 第 \d 版 —", cjk_scan=False),
}

C = CONFIGS[CODE]
D = os.path.join(G, "hidden_files/w46", f"de-{CODE}")
os.makedirs(D, exist_ok=True)

# ---- render.py ----
src = open(os.path.join(G, "hidden_files/w46/de-en/render.py"), encoding="utf-8").read()
src = src.replace("weekly-report-w46-de-en", f"weekly-report-w46-de-{CODE}")
src = src.replace("Die-Lucerna-VOL3-EN.pdf", f"Die-Lucerna-VOL3-{C['suffix']}.pdf")
src = src.replace("Die-Lucerna-VOL3-EN-web.pdf", f"Die-Lucerna-VOL3-{C['suffix']}-web.pdf")
src = src.replace("DE x EN", f"DE x {CODE.upper()}")
open(os.path.join(D, "render.py"), "w", encoding="utf-8").write(src)

# ---- verify.py ----
v = open(os.path.join(G, "hidden_files/w46/de-en/verify.py"), encoding="utf-8").read()
v = v.replace("DE x EN", f"DE x {CODE.upper()}")
v = v.replace("weekly-report-w46-de-en-build", f"weekly-report-w46-de-{CODE}-build")
v = v.replace("weekly-report-w46-de-en", f"weekly-report-w46-de-{CODE}")
v = v.replace('foot = "Die Lucerna · GERMAN WEEKLY VOL.3 · German text · English explanations"',
              f'foot = {C["footer"]!r}')
v = v.replace('re.match(r"Page \\d of 8", t)', f're.match(r"{C["pageline_re"]}", t)')
v = v.replace('"TEXT IN GERMAN · EXPLANATIONS IN ENGLISH" in raw1', f'{C["badge"]!r} in raw1')
v = v.replace('"WÖCHENTLICH AUF DEUTSCH · ONE ISSUE A WEEK · THE GERMAN THAT GERMANS READ"',
              f'{C["topstrip"]!r}')
v = v.replace('["football", "festivals", "remembrance"]', repr(C["chart"]))
v = v.replace(r'MUSTER · Model text \((\d+) words\)', C["muster_re"])
v = v.replace('"(3rd person singular)" in raw8', f'{C["paren_check"]!r} in raw8')
v = v.replace('re.findall(r"— Page \\d —", raw8)', f're.findall(r"{C["separator_re"]}", raw8)')
if not C["cjk_scan"]:
    # Replace the CJK leak scan block with a leftover-SC-literal check note.
    v = v.replace('''# CJK leak scan: no CJK-range character may survive in the EN edition.
CJK = re.compile(r"[\\u2e80-\\u9fff\\u3040-\\u30ff\\uac00-\\ud7af\\uff00-\\uffef]")
for pg, ts in sorted(all_texts.items()):
    hits = [t for t in ts if CJK.search(t)]
    print(pg, "CJK texts:", len(hits), hits[:3])''',
'''# CJK-language edition: explanation layer legitimately uses CJK/Hangul/kana.
# Leak check = no Simplified-Chinese-only marker strings survive.
SC_MARKERS = ["译注", "简体", "练习", "讲解"]
for pg, ts in sorted(all_texts.items()):
    hits = [t for t in ts if any(m in t for m in SC_MARKERS)]
    print(pg, "SC-marker texts:", len(hits), hits[:3])''')
open(os.path.join(D, "verify.py"), "w", encoding="utf-8").write(v)
print("wrote", D)
