# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-ja/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · 練習と答え", "Die Lucerna", "SCHLUSSTEST · 最終テスト · Alle Antworten unten auf dieser Seite — 答えはすべてこのページの下部に")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "A", "beginnt(3人称単数)"),
    ("A2", "B", "bastelt(3人称単数)"),
    ("A2", "A", "geht(3人称単数)"),
    ("A2", "B", "singt(3人称単数)"),
    ("A2", "A", "schaut(3人称単数)"),
    ("B1", "B", "sieht(3人称単数)"),
    ("A2", "B", "erzählt(3人称単数)"),
    ("B1", "A", "beginnt(3人称単数)"),
]
cnums = [reg_ex(lv, "穴埋め", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · 穴埋め", 24)
bf.para(f"Lena freut sich auf die Novemberwoche. Am Montag ({cnums[0]})___ die Schule wieder, und Lena ({cnums[1]})___ eine Laterne aus Papier. Am Mittwoch ({cnums[2]})___ sie mit ihrer Klasse beim Laternenumzug mit und ({cnums[3]})___ Martinslieder. Am Freitagabend ({cnums[4]})___ sie Deutschland in Belgrad. Am Sonntag ({cnums[5]})___ sie die NFL in München im Fernsehen. In der Schule ({cnums[6]})___ Lena: „Die Woche war toll! Der Karneval ({cnums[7]})___ um 11.11 Uhr.“", 20.5)
bf.bridge("選択肢：")
for n, opts in zip(cnums, [
    "A. beginnt · B. beginnen · C. begann",
    "A. basteln · B. bastelt · C. bastelte",
    "A. geht · B. gehen · C. ging",
    "A. singen · B. singt · C. sang",
    "A. schaut · B. schauen · C. schaute",
    "A. sehen · B. sieht · C. sah",
    "A. erzählen · B. erzählt · C. erzählte",
    "A. beginnt · B. beginnen · C. begann",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B · WISSENSFRAGEN · クイズ", 24)
bf.ex("B1", "選択肢", "A", "カーニバルは11時11分に開幕",
      "Die Karnevalssession beginnt um... A. 11.11 Uhr · B. 15.30 Uhr · C. 20.45 Uhr", size=19.5, gap=8)
bf.ex("A2", "選択肢", "B", "金曜日にセルビアでアウェー戦",
      "Deutschland spielt am Freitag in... A. Berlin · B. Belgrad · C. München", size=19.5, gap=8)
bf.ex("A2", "選択肢", "C", "NFLは日曜15時30分",
      "Das NFL-Spiel in München beginnt um... A. 11.11 Uhr · B. 20.45 Uhr · C. 15.30 Uhr", size=19.5, gap=8)
bf.ex("B1", "選択肢", "A", "追悼の日は11月15日",
      "Der Volkstrauertag ist am... A. 15. November · B. 11. November · C. 22. November", size=19.5, gap=8)
bf.ex("B1", "選択肢", "B", "家庭の電気税は2.05セント",
      "Die Stromsteuer für Haushalte beträgt... A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=19.5, gap=8)
bf.ex("A2", "選択肢", "B", "監督は11月5日に代表を発表する",
      "Klopp nennt seinen Kader am... A. 13. November · B. 5. November · C. 9. November", size=19.5, gap=8)
bf.ex("B1", "選択肢", "A", "ZDFは13時30分から生中継",
      "Die Gedenkstunde überträgt ab 13.30 Uhr... A. das ZDF · B. RTL · C. die ARD", size=19.5, gap=8)
bf.ex("A2", "選択肢", "C", "Totensonntagは11月22日",
      "Der Totensonntag ist am... A. 15. November · B. 18. November · C. 22. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · 読解", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Mittwoch bastelt die Familie eine Laterne aus Papier. Am Freitag schaut sie Deutschland in Belgrad im Fernsehen. Am Sonntag schaut sie das NFL-Spiel um 15.30 Uhr. „Eine Woche mit Laternen und Football“, sagt Frau Berger.", 20.5)
bf.ex("B1", "選択肢", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "選択肢", "B", "水曜日にランタンを作ること",
      "Was bastelt die Familie am Mittwoch? A. ein Kostüm · B. eine Laterne · C. einen Kürbis", size=19.5, gap=8)
bf.ex("A2", "選択肢", "A", "金曜日にドイツを見ること",
      "Was schaut die Familie am Freitag? A. Deutschland in Belgrad · B. die NFL · C. den Karneval", size=19.5, gap=8)
bf.ex("B1", "選択肢", "B", "NFLは日曜15時30分",
      "Wann schaut die Familie das NFL-Spiel? A. Samstag 18.30 Uhr · B. Sonntag 15.30 Uhr · C. Freitag 20.45 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · 文作り", 24)
bf.ex("A2", "文作り", "Die Karnevalssession beginnt am Mittwoch.", "時間表現、動詞は2番目",
      "die Karnevalssession / beginnt / am Mittwoch → ___", instr="文を作る", size=19.5, gap=8)
bf.ex("A2", "文作り", "Wir basteln eine Laterne aus Papier.", "主語・動詞・目的語の順",
      "wir / basteln / eine Laterne / aus Papier → ___", instr="文を作る", size=19.5, gap=8)
bf.ex("B1", "文作り", "Die Kinder gehen am Montag wieder in die Schule.", "時間表現が先、動詞は2番目",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="文を作る", size=19.5, gap=8)
bf.ex("B1", "文作り", "Am Sonntag ist Volkstrauertag in ganz Deutschland.", "場所と時間が先、動詞は2番目",
      "am Sonntag / ist / Volkstrauertag / in ganz Deutschland → ___", instr="文を作る", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · 翻訳", 24)
bf.ex("A2", "翻訳", "カーニバルは11時11分にケルンで開幕する。", "beginnen＝始まる",
      "Der Karneval beginnt um 11.11 Uhr in Köln.（日本語に訳しましょう）", instr="翻訳", size=19.5, gap=8)
bf.ex("A2", "翻訳", "水曜日にランタンを作る。", "basteln＝作る",
      "Ich bastle am Mittwoch eine Laterne.（日本語に訳しましょう）", instr="翻訳", size=19.5, gap=8)
bf.ex("B1", "翻訳", "学校は11月9日に再開した。", "wieder begonnen＝再開した",
      "Die Schule hat am 9. November wieder begonnen.（日本語に訳しましょう）", instr="翻訳", size=19.5, gap=8)
bf.ex("B1", "翻訳", "Am Sonntag schaue ich das NFL-Spiel.", "試合を見る＝das Spiel schauen",
      "日曜日にNFLの試合を見ます。（ドイツ語に訳しましょう）", instr="ドイツ語に訳す", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · 単語ペア", 24)
bf.match_set("B1", "単語ペア",
             ["der Mantel", "die Laterne", "das Geisterspiel", "die Versöhnung"],
             ["das Licht aus Papier, das die Kinder am Abend tragen",
              "der warme Umhang, den Martin mit dem Bettler teilte",
              "die Aussöhnung nach einem Streit — Frieden zwischen Menschen",
              "ein Spiel ohne Zuschauer im Stadion"],
             ["b", "a", "d", "c"],
             ["Mantel=マント b", "Laterne=ランタン a", "Geisterspiel=無観客試合 d", "Versöhnung=和解 c"],
             instr="語と意味を結ぶ")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "singst(2人称単数)"),
    ("A2", "A", "macht(2人称複数)"),
    ("A2", "A", "essen(1人称複数)"),
    ("B1", "B", "machst(2人称単数)"),
    ("B1", "A", "schaue(1人称単数)"),
]
dnums = [reg_ex(lv, "対話の補完", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · 対話の補完", 24)
bf.para(f"— Hallo, Lena! Bastelst du eine Laterne? — Ja, für St. Martin! Am Mittwoch gehen wir mit. — ({dnums[0]})___ du auch Martinslieder? — Ja, mit meiner Klasse. — Und was ({dnums[1]})___ ihr am Abend? — Wir singen und laufen mit den Laternen. Am Sonntag ({dnums[2]})___ wir Brezeln und schauen die NFL. — Lecker! Und was ({dnums[3]})___ du am Freitag? — Ich ({dnums[4]})___ Deutschland in Belgrad im Fernsehen!", 20.5)
bf.bridge("選択肢：")
for n, opts in zip(dnums, [
    "A. singe · B. singst · C. singen",
    "A. macht · B. machen · C. machst",
    "A. essen · B. esse · C. esst",
    "A. machen · B. machst · C. macht",
    "A. schaue · B. schaust · C. schaut",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "作文", "自由課題 — 作文の枠のポイントに沿いましょう。模範文はこのページの枠の中にあります", "挙げられたポイントで採点されます")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · 作文", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Novemberwoche». Erzählen Sie: Was basteln Sie? Welche Spiele schauen Sie? Mit wem? Schreiben Sie auch einen Satz über St. Martin oder den Volkstrauertag! Die besten Texte drucken wir in VOL.4 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "ドイツ語で80～100語で書きましょう。「11月の私の1週間」。何を作るか、どの試合を誰と見るか——そして聖マルティンの日か追悼の日について1文加えましょう。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · 模範文（84 Wörter）", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche bastle ich eine Laterne. Am Mittwoch singe ich mit meiner Klasse Martinslieder und gehe beim Laternenumzug mit. Am Freitag schaue ich mit meiner Familie Deutschland in Belgrad im Fernsehen. Das Spiel ist ein Geisterspiel — ohne Zuschauer. Am Sonntag schaue ich die NFL in München im Fernsehen. Die Lions spielen gegen die Patriots. Der Karneval beginnt um 11.11 Uhr in Köln. Am Sonntag esse ich Brezeln und trinke Apfelschorle. Am Montag gehe ich wieder in die Schule. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANTWORTEN · 答えと解説（1～8ページ）", 26, "sans", True, OLIVE)
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
