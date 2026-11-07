# -*- coding: utf-8 -*-
"""Verify Round-1 fixes in the re-rendered SVGs (text layer only)."""
import glob, html, os, re, sys

GOAL = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations")
FILES = os.path.join(GOAL, "files")
CODES = ["core", "de", "en", "es", "fr", "ja", "ko", "nl", "pt", "ru", "zh-tw"]
FW = "\uff1a"

def page_text(eddir, fname):
    p = os.path.join(eddir, "svg", fname)
    s = open(p, encoding="utf-8").read()
    parts = []
    for m in re.finditer(r"<text[^>]*>(.*?)</text>", s, re.S):
        t = html.unescape(re.sub(r"<[^>]+>", "", m.group(1))).strip()
        if t:
            parts.append(t)
    return " ".join(parts)

def check(cond, label):
    print(("PASS " if cond else "FAIL ") + label)
    return cond

fails = 0
for code in CODES:
    ed = os.path.join(FILES, f"weekly-report-w46-it-{code}")
    p1 = page_text(ed, "p1-prima.svg")
    p2 = page_text(ed, "p2-vita.svg")
    p4 = page_text(ed, "p4-sport.svg")
    p7 = page_text(ed, "p7-lingua.svg")
    p8 = page_text(ed, "p8-valutazione.svg")
    all_t = " ".join(page_text(ed, f) for f in sorted(os.listdir(os.path.join(ed, "svg"))))
    print(f"--- {code} ---")
    ok = True
    ok &= check("86 film a Firenze. (Pagina 2)" in p1, "D1 Pagina 2")
    ok &= check("86 film a Firenze. (Pagina 5)" not in p1, "D1 old gone")
    ok &= check("si è chiuso il Forum Cultura" in p2, "D3 chiuso sg")
    ok &= check("si sono aperte la finale del Panettone" in p2, "D3 aperte fem-pl")
    ok &= check("si sono chiusi il Forum" not in p2 and "si sono aperti la finale" not in p2, "D3 old gone")
    ok &= check(p4.count("NON cominciano") == 2, "D2 NON stems x2")
    ok &= check("cominciano ___ di quelle" not in p4.replace("NON cominciano", ""), "D2 old stems gone")
    ok &= check("la finale è a Perugia" not in all_t, "Q1 old gone everywhere")
    ok &= check("la Festa del Torrone è a Cremona" in p7, "Q1 new fact in P7")
    ok &= check("20.45" in p8, "P8 has 20.45")
    if code in ("de", "en", "es", "fr", "ko", "nl", "pt", "ru"):
        ok &= check(FW not in all_t, f"F1 no U+FF1A in {code} SVGs")
    if code == "ko":
        ok &= check("ンチ" not in all_t and "スクリ토리ンチ타" not in all_t, "KO no katakana")
        ok &= check(all_t.count("스크리토린치타") == 6, "KO correct name x6")
        ok &= check("채우세요。" not in all_t and "완성하세요。" not in all_t, "KO no U+3002 stops")
    if code == "zh-tw":
        ok &= check("未來時" not in all_t, "ZHTW no 未來時")
        ok &= check(all_t.count("將來時") == 10, "ZHTW 將來時 x10 (P5+P7 bridges + P8 76-79,101-104)")
    if not ok:
        fails += 1

# edition-specific P8 checks
def p8of(code):
    return page_text(os.path.join(FILES, f"weekly-report-w46-it-{code}"), "p8-valutazione.svg")
print("--- edition-specific ---")
en8 = p8of("en")
fails += 0 if check("THE ITALIAN THAT ITALIANS ARE READING" in page_text(os.path.join(FILES, "weekly-report-w46-it-en"), "p1-prima.svg"), "EN strapline") else 1
fails += 0 if check("two cities, two festivals" in en8, "EN 132") else 1
fails += 0 if check(en8.count("Subject + essere + place + date") == 2, "EN 44/134 +date x2") else 1
es8 = p8of("es")
fails += 0 if check("dos ciudades, dos fiestas" in es8, "ES 132") else 1
fails += 0 if check("continúa en Cremona" in es8, "ES 117") else 1
fr8 = p8of("fr")
fails += 0 if check("deux villes, deux fêtes" in fr8, "FR 132") else 1
nl8 = p8of("nl")
fails += 0 if check("dura (zij)" in nl8, "NL 20 zij") else 1
fails += 0 if check("mandorle = amandelen" in nl8, "NL 146 =") else 1
pt8 = p8of("pt")
fails += 0 if check("duas cidades e duas festas" in pt8, "PT 132") else 1
pt7 = page_text(os.path.join(FILES, "weekly-report-w46-it-pt"), "p7-lingua.svg")
fails += 0 if check("escreve à redação" in pt7 and "escrevam" not in pt7, "PT disclosure tu") else 1
ru7 = page_text(os.path.join(FILES, "weekly-report-w46-it-ru"), "p7-lingua.svg")
fails += 0 if check("К моменту сдачи номера" in ru7, "RU disclosure qualifier") else 1
ru8 = p8of("ru")
fails += 0 if check("миндаль (мн. ч.)" not in ru8 and "mandorle = миндаль" in ru8, "RU 38 marker") else 1
core8 = p8of("core")
fails += 0 if check("mandorle = 杏仁" in core8 and "quanto costa? = 多少钱" in core8 and "pagare con carta = 刷卡" in core8, "D5 core =") else 1
ko8 = p8of("ko")
fails += 0 if check("mandorle = 아몬드" in ko8, "D5 ko 146") else 1
zt8 = p8of("zh-tw")
fails += 0 if check("mandorle = 杏仁" in zt8 and "quanto costa? = 多少錢" in zt8 and "pagare con carta = 刷卡" in zt8, "D5 zh-tw =") else 1
print("FAILURES:", fails)
sys.exit(1 if fails else 0)
