# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN　練習與答案", "Die Lucerna", "SCHLUSSTEST　綜合評估　Alle Antworten unten auf dieser Seite 答案在本版下方")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "schnitzen 雕刻南瓜"),
    ("A2", "A", "geht in die Bibliothek 去圖書館"),
    ("A2", "A", "Uhr zurückgestellt 撥回"),
    ("A2", "C", "Winterzeit 冬令時開始"),
    ("A2", "B", "eine Stunde länger 多睡一小時"),
    ("A2", "A", "der erste Frost 初霜"),
    ("B1", "B", "gefällt mir gut 我很喜歡"),
    ("A2", "C", "ich gehe（第一人稱）"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A　LÜCKENTEXT　完形填空", 24)
bf.para(f"Jonas freut sich auf das Wochenende. Am Samstag kauft er einen Kürbis und ({cnums[0]})___ ihn zu Hause. Am Nachmittag ({cnums[1]})___ er in die Bibliothek — sie hat am Samstag ein besonderes Programm. Am Abend spielt Dortmund, und Jonas sieht das Spiel mit Freunden. In der Nacht wird die Uhr ({cnums[2]})___: Die ({cnums[3]})___ beginnt. Am Sonntag schläft Jonas eine Stunde ({cnums[4]})___. Draußen ist es kalt, der erste ({cnums[5]})___ ist da. „Ein Sonntag mit 25 Stunden“, sagt Jonas, „({cnums[6]})___ mir gut! Und am Montag ({cnums[7]})___ ich wieder in die Schule.“", 20.5)
bf.expl("選項：")
for n, opts in zip(cnums, [
    "A. kocht · B. schnitzt · C. malt",
    "A. geht · B. schläft · C. kocht",
    "A. zurückgestellt · B. vorgestellt · C. vergessen",
    "A. Sommerzeit · B. Ferienzeit · C. Winterzeit",
    "A. früh · B. länger · C. laut",
    "A. Frost · B. Sommer · C. Frühling",
    "A. geht · B. gefällt · C. macht",
    "A. gehen · B. gehst · C. gehe",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B　WISSENSFRAGEN　綜合問答", 24)
bf.ex("B1", "單選", "A", "圖書館日紀念 Preusker",
      "Der Tag der Bibliotheken erinnert an... A. Karl Preusker · B. Martin Luther · C. Lucas Cranach", size=19.5, gap=8)
bf.ex("A2", "單選", "B", "週日凌晨 3 點撥回",
      "Die Uhr wird umgestellt am... A. Freitag um 20.30 Uhr · B. Sonntag um 3.00 Uhr · C. Samstag um Mitternacht", size=19.5, gap=8)
bf.ex("A2", "單選", "A", "O bis O = 十月到復活節",
      "„Von O bis O“ heißt: Winterreifen von... A. Oktober bis Ostern · B. Oktober bis Oktober · C. Ostern bis Oktober", size=19.5, gap=8)
bf.ex("B1", "單選", "B", "國家德比在多特蒙德",
      "Am 31. Oktober spielen die Bayern... A. zu Hause · B. in Dortmund · C. in Berlin", size=19.5, gap=8)
bf.ex("B1", "單選", "B", "保護力 10–14 天形成",
      "Die Grippeimpfung schützt nach... A. 2 Tagen · B. 10 bis 14 Tagen · C. 3 Monaten", size=19.5, gap=8)
bf.ex("B1", "單選", "B", "藥房接種限 18 歲以上",
      "In Apotheken impft man Menschen... A. ab 6 Jahren · B. ab 18 Jahren · C. nur ab 60", size=19.5, gap=8)
bf.ex("A2", "單選", "B", "週六焦點戰多特–法蘭克福",
      "Das Topspiel am Samstag ist... A. Freiburg–Bayern · B. Dortmund–Frankfurt · C. Stuttgart–Gladbach", size=19.5, gap=8)
bf.ex("A2", "單選", "B", "2–3 點出現兩次",
      "Die Stunde 2.00–3.00 Uhr gibt es in der Nacht... A. einmal · B. zweimal · C. gar nicht", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C　LESEVERSTEHEN　閱讀理解", 24)
bf.para("Frau Berger arbeitet in einer Berliner Bibliothek. Am Samstag, dem 24. Oktober, beginnt sie um halb zehn mit der Arbeit. Heute ist der Tag der Bibliotheken: Um elf Uhr spielt sie mit den Kindern Bibliotheks-Bingo. Am Nachmittag hilft sie bei den Book-Blind-Dates. Um 18 Uhr schließt die Bibliothek. Frau Berger fährt nach Hause und stellt am Abend alle Uhren um — morgen darf sie eine Stunde länger schlafen.", 20.5)
bf.ex("B1", "單選", "A", "halb zehn = 9:30",
      "Wann beginnt Frau Berger mit der Arbeit? A. um 9.30 Uhr · B. um 10.30 Uhr · C. um halb elf", size=19.5, gap=8)
bf.ex("A2", "單選", "B", "11 點和孩子玩 Bingo",
      "Was spielt sie um elf Uhr mit den Kindern? A. Fußball · B. Bibliotheks-Bingo · C. Karten", size=19.5, gap=8)
bf.ex("A2", "單選", "B", "晚上回家撥鐘",
      "Was macht sie am Abend zu Hause? A. Sie schnitzt einen Kürbis. · B. Sie stellt die Uhren um. · C. Sie liest ein Buch.", size=19.5, gap=8)
bf.ex("B1", "單選", "B", "因時鐘撥回可多睡",
      "Warum darf sie am Sonntag länger schlafen? A. Die Bibliothek ist zu. · B. Die Uhr wird zurückgestellt. · C. Sie hat Urlaub.", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D　SÄTZE BAUEN　造句", 22)  # D5 fix run2
bf.ex("A2", "造句", "Die Uhr wird am Sonntag zurückgestellt.", "wird 第二位，Partizip 置尾",
      "die Uhr / wird / am Sonntag / zurückgestellt → ___", instr="造句", size=19.5, gap=8)
bf.ex("A2", "造句", "Wir schlafen eine Stunde länger.", "主謂賓順序",
      "wir / schlafen / eine Stunde / länger → ___", instr="造句", size=19.5, gap=8)
bf.ex("B1", "造句", "Die Kinder freuen sich, weil Ferien sind.", "weil 句動詞置尾",
      "die Kinder / freuen sich / weil / Ferien / sind → ___", instr="造句", size=19.5, gap=8)
bf.ex("B1", "造句", "Am Samstag ist der Tag der Bibliotheken.", "時間狀語開頭，動詞第二位",
      "am Samstag / ist / der Tag / der Bibliotheken → ___", instr="造句", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E　ÜBERSETZEN　翻譯", 24)
bf.ex("A2", "翻譯", "這一夜有 25 個小時。", "Stunden = 小時",
      "Die Nacht hat 25 Stunden.（譯成中文）", instr="翻譯", size=19.5, gap=8)
bf.ex("A2", "翻譯", "我週六晚上撥鐘。", "umstellen = 撥（鐘）",
      "Ich stelle die Uhr am Samstagabend um.（譯成中文）", instr="翻譯", size=19.5, gap=8)
bf.ex("B1", "翻譯", "Am Sonntag schlafe ich eine Stunde länger.", "多睡一小時 = eine Stunde länger schlafen",
      "我週日多睡一小時。（譯成德語）", instr="翻譯", size=19.5, gap=8)
bf.ex("B1", "翻譯", "In der Bibliothek kann man Bücher leihen.", "kann man ... leihen 可以借",
      "在圖書館可以借書。（譯成德語）", instr="翻譯", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F　WÖRTER PAAREN　詞彙配對", 24)
bf.match_set("B1", "詞彙配對",
             ["die Umstellung", "die Mitgliedstaaten", "die Mehrheit", "der Feiertag"],
             ["ein Tag, an dem man nicht arbeiten muss",
              "der Wechsel zwischen Sommer- und Winterzeit",
              "die Länder, die zu einer Union gehören",
              "mehr als die Hälfte, zum Beispiel 84 Prozent"],
             ["b", "c", "d", "a"],
             ["Umstellung=夏冬令時切換 b", "Mitgliedstaaten=成員國 c", "Mehrheit=多數 d", "Feiertag=法定假日 a"],
             instr="把詞和釋義配對")

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "Buch 本（給兒子的書）"),
    ("B1", "B", "im ersten Stock 在二樓（德語的一樓）"),
    ("A2", "C", "Bingo 圖書館賓果"),
    ("B1", "A", "Bibliotheksausweis 借書證"),
    ("B1", "B", "behalten 保留/借用"),
]
dnums = [reg_ex(lv, "對話補全", k, nt) for lv, k, nt in ddefs]
bf.head("G　DIALOG　對話補全", 24)
bf.para(f"— Guten Tag! Ich suche ein Buch für meinen Sohn. — Gern. Wie alt ist er? — Er ist neun, und er mag Tiere. — Dann ist dieses ({dnums[0]})___ perfekt: „Tiere im Herbst“. Mehr Tierbücher finden Sie im ersten ({dnums[1]})___. — Danke! Gibt es heute auch das ({dnums[2]})___? — Ja, um elf Uhr im Kinderzimmer. Bitte zeigen Sie mir noch Ihren ({dnums[3]})___. — Hier ist er. Wie lange kann ich das Buch ({dnums[4]})___? — Drei Wochen. Viel Spaß beim Lesen!", 20.5)
bf.expl("選項：")
for n, opts in zip(dnums, [
    "A. Buch · B. Bett · C. Brot",
    "A. Keller · B. Stock · C. Garten",
    "A. Fußball · B. Kino · C. Bingo",
    "A. Bibliotheksausweis · B. Bibliotheksausflug · C. Bibliotheksautor",
    "A. essen · B. behalten · C. singen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, OLIVE, 2)
reg_ex("B1", "寫作", "開放題 — 要點見寫作框，範本在第 8 版寫作框內", "按要點給分")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H　SCHREIBEN　寫作", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Mein Sonntag, der 25. Oktober». Erzählen Sie: Wie lange schlafen Sie? Was machen Sie am Morgen, am Nachmittag und am Abend? Schreiben Sie auch einen Satz über die Uhr! Die besten Texte drucken wir in VOL.2 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "用德語寫 80–100 詞：《我的 10 月 25 日星期日》。寫清睡多久、上午/下午/晚上做什麼，並寫一句關於時鐘的話。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX)
p.text(mx2 + 22, wy + 38, "MUSTER　範本（87 Wörter）", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Am Sonntag, dem 25. Oktober, schlafe ich eine Stunde länger. Dann frühstücke ich langsam mit meiner Familie. Um elf Uhr gehe ich in den Park, denn die Sonne scheint. Am Nachmittag lese ich mein neues Buch aus der Bibliothek. Am Abend koche ich eine Suppe mit Kürbis. Danach rufe ich meine Freundin an. Wir sprechen über das Fußballspiel am Samstag. Dortmund hat gewonnen, und wir freuen uns. Der Sonntag mit 25 Stunden ist mein Lieblingstag. Ich gehe früh ins Bett, denn am Montag beginnt die Arbeit wieder.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 296
p.hline(MX, RIGHT, ky - 12, OLIVE, 2)
p.text(MX, ky + 26, "ANTWORTEN　全部答案與簡析（第1–8 版）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
