# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-de-ja/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · 練習と答え", "Die Lucerna", "SCHLUSSTEST · 総合テスト · Alle Antworten unten auf dieser Seite — 答えはこのページの下にあります")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "schnitzen かぼちゃを彫る"),
    ("A2", "A", "geht in die Bibliothek 図書館へ行く"),
    ("A2", "A", "Uhr zurückgestellt 時計を戻した"),
    ("A2", "C", "Winterzeit 冬時間が始まる"),
    ("A2", "B", "eine Stunde länger 1時間長く"),
    ("A2", "A", "der erste Frost 初霜"),
    ("B1", "B", "gefällt mir gut とても気に入る"),
    ("A2", "C", "ich gehe (一人称)"),
]
cnums = [reg_ex(lv, "穴埋め", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · 穴埋め", 24)
bf.para(f"Jonas freut sich auf das Wochenende. Am Samstag kauft er einen Kürbis und ({cnums[0]})___ ihn zu Hause. Am Nachmittag ({cnums[1]})___ er in die Bibliothek — sie hat am Samstag ein besonderes Programm. Am Abend spielt Dortmund, und Jonas sieht das Spiel mit Freunden. In der Nacht wird die Uhr ({cnums[2]})___: Die ({cnums[3]})___ beginnt. Am Sonntag schläft Jonas eine Stunde ({cnums[4]})___. Draußen ist es kalt, der erste ({cnums[5]})___ ist da. „Ein Sonntag mit 25 Stunden“, sagt Jonas, „({cnums[6]})___ mir gut! Und am Montag ({cnums[7]})___ ich wieder in die Schule.“", 20.5)
bf.expl("選択肢：")
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
bf.head("B · WISSENSFRAGEN · 総合問題", 24)
bf.ex("B1", "選択問題", "A", "図書館の日は Preusker を記念する",
      "Der Tag der Bibliotheken erinnert an... A. Karl Preusker · B. Martin Luther · C. Lucas Cranach", size=19.5, gap=8)
bf.ex("A2", "選択問題", "B", "日曜の午前3時に戻す",
      "Die Uhr wird umgestellt am... A. Freitag um 20.30 Uhr · B. Sonntag um 3.00 Uhr · C. Samstag um Mitternacht", size=19.5, gap=8)
bf.ex("A2", "選択問題", "A", "O bis O = 10月からイースターまで",
      "„Von O bis O“ heißt: Winterreifen von... A. Oktober bis Ostern · B. Oktober bis Oktober · C. Ostern bis Oktober", size=19.5, gap=8)
bf.ex("B1", "選択問題", "B", "ダービーはドルトムントで",
      "Am 31. Oktober spielen die Bayern... A. zu Hause · B. in Dortmund · C. in Berlin", size=19.5, gap=8)
bf.ex("B1", "選択問題", "B", "効果は10–14日で現れる",
      "Die Grippeimpfung schützt nach... A. 2 Tagen · B. 10 bis 14 Tagen · C. 3 Monaten", size=19.5, gap=8)
bf.ex("B1", "選択問題", "B", "薬局での接種は18歳以上",
      "In Apotheken impft man Menschen... A. ab 6 Jahren · B. ab 18 Jahren · C. nur ab 60", size=19.5, gap=8)
bf.ex("A2", "選択問題", "B", "土曜の注目試合はドルトムント–フランクフルト",
      "Das Topspiel am Samstag ist... A. Freiburg–Bayern · B. Dortmund–Frankfurt · C. Stuttgart–Gladbach", size=19.5, gap=8)
bf.ex("A2", "選択問題", "B", "2–3時は2回現れる",
      "Die Stunde 2.00–3.00 Uhr gibt es in der Nacht... A. einmal · B. zweimal · C. gar nicht", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · 読解", 24)
bf.para("Frau Berger arbeitet in einer Berliner Bibliothek. Am Samstag, dem 24. Oktober, beginnt sie um halb zehn mit der Arbeit. Heute ist der Tag der Bibliotheken: Um elf Uhr spielt sie mit den Kindern Bibliotheks-Bingo. Am Nachmittag hilft sie bei den Book-Blind-Dates. Um 18 Uhr schließt die Bibliothek. Frau Berger fährt nach Hause und stellt am Abend alle Uhren um — morgen darf sie eine Stunde länger schlafen.", 20.5)
bf.ex("B1", "選択問題", "A", "halb zehn = 9:30",
      "Wann beginnt Frau Berger mit der Arbeit? A. um 9.30 Uhr · B. um 10.30 Uhr · C. um halb elf", size=19.5, gap=8)
bf.ex("A2", "選択問題", "B", "11時に子どもと Bingo",
      "Was spielt sie um elf Uhr mit den Kindern? A. Fußball · B. Bibliotheks-Bingo · C. Karten", size=19.5, gap=8)
bf.ex("A2", "選択問題", "B", "夜に家で時計を合わせる",
      "Was macht sie am Abend zu Hause? A. Sie schnitzt einen Kürbis. · B. Sie stellt die Uhren um. · C. Sie liest ein Buch.", size=19.5, gap=8)
bf.ex("B1", "選択問題", "B", "時計を戻すので長く眠れる",
      "Warum darf sie am Sonntag länger schlafen? A. Die Bibliothek ist zu. · B. Die Uhr wird zurückgestellt. · C. Sie hat Urlaub.", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · 文作り", 24)
bf.ex("A2", "文を作る", "Die Uhr wird am Sonntag zurückgestellt.", "wird は2番目、Partizip は文末",
      "die Uhr / wird / am Sonntag / zurückgestellt → ___", instr="文を作る", size=19.5, gap=8)
bf.ex("A2", "文を作る", "Wir schlafen eine Stunde länger.", "主語・動詞・目的語の順",
      "wir / schlafen / eine Stunde / länger → ___", instr="文を作る", size=19.5, gap=8)
bf.ex("B1", "文を作る", "Die Kinder freuen sich, weil Ferien sind.", "weil 文では動詞は文末",
      "die Kinder / freuen sich / weil / Ferien / sind → ___", instr="文を作る", size=19.5, gap=8)
bf.ex("B1", "文を作る", "Am Samstag ist der Tag der Bibliotheken.", "時間の言葉で始め、動詞は2番目",
      "am Samstag / ist / der Tag / der Bibliotheken → ___", instr="文を作る", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · 翻訳", 24)
bf.ex("A2", "翻訳", "この夜は25時間あります。", "Stunden = 時間",
      "Die Nacht hat 25 Stunden.（日本語訳）", instr="翻訳", size=19.5, gap=8)
bf.ex("A2", "翻訳", "私は土曜の夜に時計を合わせます。", "umstellen = 時計を調整する",
      "Ich stelle die Uhr am Samstagabend um.（日本語訳）", instr="翻訳", size=19.5, gap=8)
bf.ex("B1", "翻訳", "Am Sonntag schlafe ich eine Stunde länger.", "1時間長く寝る = eine Stunde länger schlafen",
      "日曜は1時間長く寝ます。（ドイツ語訳）", instr="翻訳", size=19.5, gap=8)
bf.ex("B1", "翻訳", "In der Bibliothek kann man Bücher leihen.", "kann man ... leihen = 借りることができる",
      "図書館では本が借りられます。（ドイツ語訳）", instr="翻訳", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · 単語ペア", 24)
bf.match_set("B1", "単語のペア",
             ["die Umstellung", "die Mitgliedstaaten", "die Mehrheit", "der Feiertag"],
             ["ein Tag, an dem man nicht arbeiten muss",
              "der Wechsel zwischen Sommer- und Winterzeit",
              "die Länder, die zu einer Union gehören",
              "mehr als die Hälfte, zum Beispiel 84 Prozent"],
             ["b", "c", "d", "a"],
             ["Umstellung=夏時間と冬時間の切替 b", "Mitgliedstaaten=加盟国 c", "Mehrheit=過半数 d", "Feiertag=祝日 a"],
             instr="語と意味を結ぶ")

# ---- G. dialogue ----
ddefs = [
    ("A2", "A", "Buch 本 (息子への本)"),
    ("B1", "B", "im ersten Stock 2階 (ドイツでは1階)"),
    ("A2", "C", "Bingo 図書館ビンゴ"),
    ("B1", "A", "Bibliotheksausweis 図書館カード"),
    ("B1", "B", "behalten 手元に置く／借りる"),
]
dnums = [reg_ex(lv, "対話の補完", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · 対話の補完", 24)
bf.para(f"— Guten Tag! Ich suche ein Buch für meinen Sohn. — Gern. Wie alt ist er? — Er ist neun, und er mag Tiere. — Dann ist dieses ({dnums[0]})___ perfekt: „Tiere im Herbst“. Mehr Tierbücher finden Sie im ersten ({dnums[1]})___. — Danke! Gibt es heute auch das ({dnums[2]})___? — Ja, um elf Uhr im Kinderzimmer. Bitte zeigen Sie mir noch Ihren ({dnums[3]})___. — Hier ist er. Wie lange kann ich das Buch ({dnums[4]})___? — Drei Wochen. Viel Spaß beim Lesen!", 20.5)
bf.expl("選択肢：")
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
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "作文", "自由作文 — ポイントは作文の枠、模範はこのページの作文枠の中", "ポイントごとに採点")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · 作文", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Mein Sonntag, der 25. Oktober». Erzählen Sie: Wie lange schlafen Sie? Was machen Sie am Morgen, am Nachmittag und am Abend? Schreiben Sie auch einen Satz über die Uhr! Die besten Texte drucken wir in VOL.2 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "ドイツ語で80–100語で書いてください：《私の10月25日（日曜日）》。どれだけ寝るか、午前・午後・夜に何をするかを書き、時計についても一文入れてください。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 276, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · 模範文（87 Wörter）", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "Am Sonntag, dem 25. Oktober, schlafe ich eine Stunde länger. Dann frühstücke ich langsam mit meiner Familie. Um elf Uhr gehe ich in den Park, denn die Sonne scheint. Am Nachmittag lese ich mein neues Buch aus der Bibliothek. Am Abend koche ich eine Suppe mit Kürbis. Danach rufe ich meine Freundin an. Wir sprechen über das Fußballspiel am Samstag. Dortmund hat gewonnen, und wir freuen uns. Der Sonntag mit 25 Stunden ist mein Lieblingstag. Ich gehe früh ins Bett, denn am Montag beginnt die Arbeit wieder.", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 296
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANTWORTEN · 全解答と解説（1–8ページ）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— {pg} ページ —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13.0, "sans", False, INK, 1.16, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
