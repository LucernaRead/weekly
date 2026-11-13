# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()

# ---- D5-de fix (W47 fix round 3): level chips for items that Flow.ex() never
# draws one for — the cloze option lines (Q113-120), the dialogue
# (Q145-149, one shared paragraph, no option lines) and writing (Q150).
# Copied from fr core content8.py D5 helpers, with de's own sizes
# (cloze option lines are 18.5 in de, not 19.5 as in fr).
# Both helpers DRAW ONLY: they never touch REG, so numbering is unchanged.
def badge_opt(flow, level, n, opts, size=18.5, lh=1.32, gap=2):
    """One cloze option line with its own level chip: chip at the row
    head, the option-line text shifted right by 72px.
    Under the text-export stubs (no _fit/_ph: export_text.py) this only
    records the option line, exactly as the old bf.para call did."""
    body = f"{n}. {opts}"
    if not hasattr(flow, "_fit"):
        flow.p.para(flow.x, flow.y + size, body, size, "sans", False, INK, 422.5, lh)
        return flow.y
    w = flow.w - 72
    lines = wrap(body, "sans", False, size, w)
    h = size + len(lines) * size * lh
    flow._fit(h + gap)
    x, y = flow.x, flow.y
    chip(flow.p, x, y, level)
    flow.y = flow.p.para(x + 72, y + size, body, size, "sans", False, INK, w, lh) + gap
    return flow.y

def badge_strip(flow, items, size=19.5, gap=9):
    """Row(s) of level chips, one per (level, n): chip + 'N.' per item,
    packed 3 per row. For items that share one paragraph (dialogue).
    Under the text-export stubs this draws nothing (chips carry no text
    for the export; the numbers already sit in the dialogue paragraph)."""
    if not hasattr(flow, "_fit"):
        return flow.y
    widths = [60 + 6 + text_w(f"{n}.", "sans", True, size) for _lv, n in items]
    rows, cur, curw = [], [], 0.0
    for it, w in zip(items, widths):
        if cur and curw + 14 + w > flow.w:
            rows.append(cur); cur, curw = [], 0.0
        cur.append((it, w)); curw += (14 if cur else 0) + w
    if cur:
        rows.append(cur)
    h = len(rows) * 30 + (len(rows) - 1) * 4  # fix3b: 行距 8->4 (chip 高 30，行距 34)
    flow._fit(h + gap)
    x0, y0 = flow.x, flow.y
    for ri, row in enumerate(rows):
        x = x0; y = y0 + ri * 34  # fix3b: 与上行一致
        for (lv, n), _w in row:
            chip(flow.p, x, y, lv)
            flow.p.text(x + 66, y + 22, f"{n}.", size, "sans", True, OLIVE)
            x += _w + 14
    flow.y = y0 + h + gap
    return flow.y
p.band("ÜBUNGEN & ANTWORTEN　練習與答案", "Die Lucerna", "SCHLUSSTEST　期末測驗　Alle Antworten unten auf dieser Seite 答案在本頁下方")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1555, tag="P8-battery")  # W47 D1: bottom was 1505; P8 stems at the 15.4pt concession need the extra room (writing strip moves down with wy, same 81px gap as before)

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "A", "schaut (第三人稱單數)"),
    ("A2", "B", "bastelt (第三人稱單數)"),
    ("A2", "A", "schreibt (第三人稱單數)"),
    ("A2", "B", "sieht (第三人稱單數)"),
    ("A2", "A", "beginnt (第三人稱單數)"),
    ("A2", "A", "liest (第三人稱單數)"),
    ("A2", "B", "denkt … nach (第三人稱單數)"),
    ("A2", "A", "ist (第三人稱單數)"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　完形填空", 24)
bf.para(f"Lena freut sich auf die Novemberwoche. Am Montag ({cnums[0]})___ sie die Nationalelf in Berlin. Am Mittwoch ({cnums[1]})___ sie einen Adventskalender und ({cnums[2]})___ ihren Wunschzettel. Am Freitag ({cnums[3]})___ sie Bayern gegen Köln im Fernsehen. Der Advent ({cnums[4]})___ am 29. November. Die Märkte sind am Sonntag geschlossen — Lena ({cnums[5]})___ ein Buch und ({cnums[6]})___ über den Totensonntag nach. Am Mittwoch ({cnums[7]})___ kein Unterricht in Bayern.", 19.5)
bf.bridge("選項：")
for n, (lv, _k, _nt), opts in zip(cnums, cloze_defs, [
    "A. schaut · B. schauen · C. schaute",
    "A. basteln · B. bastelt · C. bastelte",
    "A. schreibt · B. schreiben · C. schrieb",
    "A. sehen · B. sieht · C. sah",
    "A. beginnt · B. beginnen · C. begann",
    "A. liest · B. lesen · C. las",
    "A. denken · B. denkt · C. dachte",
    "A. ist · B. sind · C. war",
]):
    badge_opt(bf, lv, n, opts)

# ---- B. general MC ----
# W47 fix3b (收尾): B–E 共 20 个 ex() 的 gap 6→3 —— 上一棒 FIX-LOG 称已改，实测文件仍为 gap=6，
# 三份 build12 日志字节相同即为明证；此处才是真正落盘。省 20×3=60px，电池流 1472.44→1412.44，P8 图恢复 ~139.6px。
bf.head("B　WISSENSFRAGEN　問答", 24)
bf.ex("B1", "選擇題", "A", "德甲 11 月 20 日回歸",
      "Die Bundesliga kehrt zurück am... A. 20. November · B. 13. November · C. 29. November", size=20.5, gap=3)
bf.ex("A2", "選擇題", "B", "拜仁對科隆 20:30",
      "Bayern – Köln beginnt um... A. 15.30 Uhr · B. 20.30 Uhr · C. 17.30 Uhr", size=20.5, gap=3)
bf.ex("B1", "選擇題", "B", "對荷蘭 11 月 16 日",
      "Deutschland spielt gegen die Niederlande am... A. 13. November · B. 16. November · C. 22. November", size=20.5, gap=3)
bf.ex("B1", "選擇題", "B", "只有薩克森放假",
      "In welchem Bundesland ist der Buß- und Bettag ein Feiertag? A. Bayern · B. Sachsen · C. Nordrhein-Westfalen", size=20.5, gap=3)
bf.ex("A2", "選擇題", "B", "Totensonntag：11 月 22 日",
      "Der Totensonntag ist am... A. 18. November · B. 22. November · C. 29. November", size=20.5, gap=3)
bf.ex("A2", "選擇題", "A", "科隆市集 11 月 16 日開市",
      "Die Weihnachtsmärkte in Köln öffnen am... A. 16. November · B. 23. November · C. 29. November", size=20.5, gap=3)
bf.ex("B1", "選擇題", "B", "家庭電稅 2.05 分",
      "Die Stromsteuer für Haushalte beträgt... A. 2,50 Cent · B. 2,05 Cent · C. 0,05 Cent", size=20.5, gap=3)
bf.ex("A2", "選擇題", "B", "將臨期第一主日：11 月 29 日",
      "Der erste Advent ist am... A. 22. November · B. 29. November · C. 16. November", size=20.5, gap=3)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　閱讀理解", 24)
bf.para("Familie Berger aus Stuttgart hat eine volle Novemberwoche. Am Montag schaut die Familie Deutschland gegen die Niederlande im Fernsehen. Am Mittwoch bastelt die Familie einen Adventskalender. Am Freitag schaut sie Bayern gegen Köln. Am Sonntag ist Totensonntag: Die Familie geht auf den Friedhof und zündet Kerzen an. „Eine stille, schöne Woche“, sagt Frau Berger.", 19.5)
bf.ex("B1", "選擇題", "A", "德國對荷蘭（週一）",
      "Was schaut die Familie am Montag? A. Deutschland gegen die Niederlande · B. die Bundesliga · C. den Adventskalender", size=20.5, gap=3)
bf.ex("A2", "選擇題", "B", "將臨期日曆（週三）",
      "Was bastelt die Familie am Mittwoch? A. eine Kerze · B. einen Adventskalender · C. einen Weihnachtsbaum", size=20.5, gap=3)
bf.ex("A2", "選擇題", "B", "拜仁對科隆（週五）",
      "Was schaut die Familie am Freitag? A. Deutschland gegen die Niederlande · B. Bayern gegen Köln · C. die Weihnachtsmärkte", size=20.5, gap=3)
bf.ex("B1", "選擇題", "B", "墓地與蠟燭（週日）",
      "Was macht die Familie am Sonntag? A. Sie geht auf den Weihnachtsmarkt. · B. Sie geht auf den Friedhof und zündet Kerzen an. · C. Sie bastelt einen Adventskalender.", size=20.5, gap=3)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　造句", 24)
bf.ex("A2", "造句", "Die Bundesliga kehrt am Freitag zurück.", "時間，動詞第二",
      "die Bundesliga / kehrt / am Freitag / zurück → ___", instr="造句", size=20.5, gap=3)
bf.ex("A2", "造句", "Wir basteln im November einen Adventskalender.", "S-V-O 語序",
      "wir / basteln / einen Adventskalender / im November → ___", instr="造句", size=20.5, gap=3)
bf.ex("B1", "造句", "Am Sonntag sind die Weihnachtsmärkte geschlossen.", "時間在先，動詞第二",
      "am Sonntag / sind / die Weihnachtsmärkte / geschlossen → ___", instr="造句", size=20.5, gap=3)
bf.ex("B1", "造句", "Die Familie geht am Sonntag auf den Friedhof.", "S-V-O 語序",
      "die Familie / geht / am Sonntag / auf den Friedhof → ___", instr="造句", size=20.5, gap=3)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　翻譯", 24)
bf.ex("A2", "翻譯", "德甲週五回歸。", "kehren zurück = 回歸",
      "Die Bundesliga kehrt am Freitag zurück. (譯成繁體中文)", instr="譯成繁體中文", size=20.5, gap=3)
bf.ex("A2", "翻譯", "週日市集休息。", "geschlossen = 休息的",
      "Die Märkte sind am Sonntag geschlossen. (譯成繁體中文)", instr="譯成繁體中文", size=20.5, gap=3)
bf.ex("B1", "翻譯", "我正在做將臨期日曆。", "basteln = 手作",
      "Ich bastle einen Adventskalender. (譯成繁體中文)", instr="譯成繁體中文", size=20.5, gap=3)
bf.ex("B1", "翻譯", "Am Montag schaue ich zu Hause Deutschland gegen die Niederlande.", "看比賽 = das Spiel schauen",
      "週一我在家看德國對荷蘭。(譯成德文。)", instr="譯成德文", size=20.5, gap=3)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　詞彙配對", 24, gap=5)  # fix3b: col3 间距补偿
bf.match_set("B1", "配對",
             ["der Wunschzettel", "das Türchen", "der Glühwein", "der Friedhof"],
             ["das kleine Fenster im Adventskalender, hinter dem eine Überraschung wartet",
              "der Ort, an dem man der Verstorbenen gedenkt",
              "die Liste mit Wünschen für Weihnachten",
              "der warme, gewürzte Wein, den man auf Weihnachtsmärkten trinkt"],
             ["c", "a", "d", "b"],
             ["Wunschzettel=願望清單 c", "Türchen=小門 a", "Glühwein=熱紅酒 d", "Friedhof=墓地 b"],
             instr="配對", gap=0)  # fix3b: col3 间距补偿

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "öffne (第一人稱單數)"),
    ("A2", "B", "machst (第二人稱單數)"),
    ("A2", "A", "schaue (第一人稱單數)"),
    ("B1", "A", "schaue (第一人稱單數)"),
    ("A2", "A", "lese (第一人稱單數)"),
]
dnums = [reg_ex(lv, "對話補全", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　對話", 24, gap=5)  # fix3b: col3 间距补偿
badge_strip(bf, [(lv, n) for n, (lv, _k, _nt) in zip(dnums, ddefs)], gap=3)  # fix3b: col3 间距补偿
bf.para(f"— Hallo, Lena! Bastelst du einen Adventskalender? — Ja, für Weihnachten! Am 1. Dezember ({dnums[0]})___ ich das erste Türchen. — Und was ({dnums[1]})___ du am Freitag? — Ich ({dnums[2]})___ Bayern gegen Köln im Fernsehen. — Und am Montag? — Da ({dnums[3]})___ ich die Nationalelf gegen die Niederlande. — Und am Sonntag? — Da ({dnums[4]})___ ich ein Buch und bleibe zu Hause.", 19.5, gap=3)  # fix3b: col3 间距补偿
bf.bridge("選項：", gap=3)  # fix3b: col3 间距补偿
for n, opts in zip(dnums, [
    "A. öffne · B. öffnest · C. öffnen",
    "A. mache · B. machst · C. macht",
    "A. schaue · B. schaust · C. schaut",
    "A. schaue · B. schaust · C. schaut",
    "A. lese · B. liest · C. lesen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 0)  # fix3b: col3 间距补偿，单行选项行无需行距
bf.end_report()

# ---- P8 image: football 1905, col 3 below the battery ----
wy = 1650  # W47 D1: was 1600; battery bottom moved to 1555, strip follows (keys end ~2378, bottom 2560)
iy8 = bf.y + 12
ih8 = min(140, (wy - 14) - (iy8 + 72))
print("P8 image height", ih8)
image(p, "fussball1905.jpg", COLX[3], iy8, CW, ih8)
cy8 = caption(p, COLX[3], iy8 + ih8, CW,
              "Fußball 1905: Schweiz gegen Frankreich.",
              "Foto: unbekannter Fotograf, 1905 — public domain")
print("P8 battery ends col3", bf.y, "| image ends", cy8)

# ---- writing strip ----
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "寫作", "開放任務 — 依寫作框中的要點進行", "按所列要點評分")
wx, ww = span_x(0, 2)
chip(p, wx, wy, "B1")  # D5-de fix: writing (Q150) gets its own level chip
p.text(wx + 72, wy + 26, "H　SCHREIBEN　寫作", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Novemberwoche». Erzählen Sie: Was basteln Sie? Welche Spiele schauen Sie? Mit wem? Schreiben Sie auch einen Satz über den Buß- und Bettag oder den Totensonntag! Die besten Texte drucken wir in VOL.5 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "用德文寫 80–100 詞：「我十一月的一週」。寫你做了什麼、和誰看哪些比賽，並加一句關於 Buß- und Bettag 或 Totensonntag 的話。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　範文（84 詞）", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche bastle ich einen Adventskalender. Am Mittwoch öffne ich kein Türchen — das erste Türchen öffnet sich erst am 1. Dezember. Am Montag schaue ich mit meiner Familie die Nationalelf gegen die Niederlande. Am Freitag schaue ich Bayern gegen Köln im Fernsehen. Die Bayern führen die Tabelle an. Am Mittwoch ist Buß- und Bettag: In Bayern habe ich keinen Unterricht. Am Sonntag ist Totensonntag. Die Weihnachtsmärkte in Köln sind geschlossen. Ich lese ein Buch und bleibe zu Hause. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　全部答案與註解（第 1–8 頁）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第 {pg} 頁 —", 16, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f"（{e['note']}）"
        parts.append(s)
    kf.para(" · ".join(parts), 13.25, "sans", False, INK, 1.18, 4)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
