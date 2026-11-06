# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-de-zh-cn/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · 练习与答案", "Die Lucerna", "SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "A", "beginnt（第三人称单数）"),
    ("A2", "B", "bastelt（第三人称单数）"),
    ("A2", "A", "geht（第三人称单数）"),
    ("A2", "B", "singt（第三人称单数）"),
    ("A2", "A", "schaut（第三人称单数）"),
    ("B1", "B", "sieht（第三人称单数）"),
    ("A2", "B", "erzählt（第三人称单数）"),
    ("B1", "A", "beginnt（第三人称单数）"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · 完形填空", 24)
bf.para(f"Lena freut sich auf die Novemberwoche. Am Montag ({cnums[0]})___ die Schule wieder, und Lena ({cnums[1]})___ eine Laterne aus Papier. Am Mittwoch ({cnums[2]})___ sie mit ihrer Klasse beim Laternenumzug mit und ({cnums[3]})___ Martinslieder. Am Freitagabend ({cnums[4]})___ sie Deutschland in Belgrad. Am Sonntag ({cnums[5]})___ sie die NFL in München im Fernsehen. In der Schule ({cnums[6]})___ Lena: „Die Woche war toll! Der Karneval ({cnums[7]})___ um 11.11 Uhr.“", 20.5)
bf.bridge("选项：")
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
bf.head("B · WISSENSFRAGEN · 综合问答", 24)
bf.ex("B1", "单选", "A", "狂欢季 11 点 11 分开幕",
      "Die Karnevalssession beginnt um... A. 11.11 Uhr · B. 15.30 Uhr · C. 20.45 Uhr", size=19.5, gap=8)
bf.ex("A2", "单选", "B", "周五客战塞尔维亚",
      "Deutschland spielt am Freitag in... A. Berlin · B. Belgrad · C. München", size=19.5, gap=8)
bf.ex("A2", "单选", "C", "NFL 周日 15:30",
      "Das NFL-Spiel in München beginnt um... A. 11.11 Uhr · B. 20.45 Uhr · C. 15.30 Uhr", size=19.5, gap=8)
bf.ex("B1", "单选", "A", "纪念日 11 月 15 日",
      "Der Volkstrauertag ist am... A. 15. November · B. 11. November · C. 22. November", size=19.5, gap=8)
bf.ex("B1", "单选", "B", "家庭电力税 2.05 欧分",
      "Die Stromsteuer für Haushalte beträgt... A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=19.5, gap=8)
bf.ex("A2", "单选", "B", "主教练 11 月 5 日公布名单",
      "Klopp nennt seinen Kader am... A. 13. November · B. 5. November · C. 9. November", size=19.5, gap=8)
bf.ex("B1", "单选", "A", "ZDF 13 点半直播纪念仪式",
      "Die Gedenkstunde überträgt ab 13.30 Uhr... A. das ZDF · B. RTL · C. die ARD", size=19.5, gap=8)
bf.ex("A2", "单选", "C", "亡灵主日 11 月 22 日",
      "Der Totensonntag ist am... A. 15. November · B. 18. November · C. 22. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · 阅读理解", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Mittwoch bastelt die Familie eine Laterne aus Papier. Am Freitag schaut sie Deutschland in Belgrad im Fernsehen. Am Sonntag schaut sie das NFL-Spiel um 15.30 Uhr. „Eine Woche mit Laternen und Football“, sagt Frau Berger.", 20.5)
bf.ex("B1", "单选", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "单选", "B", "周三做灯笼",
      "Was bastelt die Familie am Mittwoch? A. ein Kostüm · B. eine Laterne · C. einen Kürbis", size=19.5, gap=8)
bf.ex("A2", "单选", "A", "周五看德国队",
      "Was schaut die Familie am Freitag? A. Deutschland in Belgrad · B. die NFL · C. den Karneval", size=19.5, gap=8)
bf.ex("B1", "单选", "B", "NFL 周日 15:30",
      "Wann schaut die Familie das NFL-Spiel? A. Samstag 18.30 Uhr · B. Sonntag 15.30 Uhr · C. Freitag 20.45 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · 造句", 24)
bf.ex("A2", "造句", "Die Karnevalssession beginnt am Mittwoch.", "时间状语，动词第二位",
      "die Karnevalssession / beginnt / am Mittwoch → ___", instr="造句", size=19.5, gap=8)
bf.ex("A2", "造句", "Wir basteln eine Laterne aus Papier.", "主谓宾顺序",
      "wir / basteln / eine Laterne / aus Papier → ___", instr="造句", size=19.5, gap=8)
bf.ex("B1", "造句", "Die Kinder gehen am Montag wieder in die Schule.", "时间状语开头，动词第二位",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="造句", size=19.5, gap=8)
bf.ex("B1", "造句", "Am Sonntag ist Volkstrauertag in ganz Deutschland.", "地点时间开头，动词第二位",
      "am Sonntag / ist / Volkstrauertag / in ganz Deutschland → ___", instr="造句", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · 翻译", 24)
bf.ex("A2", "翻译", "狂欢节 11 点 11 分在科隆开幕。", "beginnen = 开始",
      "Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）", instr="翻译", size=19.5, gap=8)
bf.ex("A2", "翻译", "我周三做一个灯笼。", "basteln = 制作",
      "Ich bastle am Mittwoch eine Laterne.（译成中文）", instr="翻译", size=19.5, gap=8)
bf.ex("B1", "翻译", "学校 11 月 9 日又开学了。", "wieder begonnen = 又开始",
      "Die Schule hat am 9. November wieder begonnen.（译成中文）", instr="翻译", size=19.5, gap=8)
bf.ex("B1", "翻译", "Am Sonntag schaue ich das NFL-Spiel.", "看比赛 = das Spiel schauen",
      "我周日看 NFL 比赛。（译成德语）", instr="翻译", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · 词汇配对", 24)
bf.match_set("B1", "词汇配对",
             ["der Mantel", "die Laterne", "das Geisterspiel", "die Versöhnung"],
             ["das Licht aus Papier, das die Kinder am Abend tragen",
              "der warme Umhang, den Martin mit dem Bettler teilte",
              "die Aussöhnung nach einem Streit — Frieden zwischen Menschen",
              "ein Spiel ohne Zuschauer im Stadion"],
             ["b", "a", "d", "c"],
             ["Mantel=斗篷 b", "Laterne=灯笼 a", "Geisterspiel=空场比赛 d", "Versöhnung=和解 c"],
             instr="把词和释义配对")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "singst（第二人称单数）"),
    ("A2", "A", "macht（第二人称复数）"),
    ("A2", "A", "essen（第一人称复数）"),
    ("B1", "B", "machst（第二人称单数）"),
    ("B1", "A", "schaue（第一人称单数）"),
]
dnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · 对话补全", 24)
bf.para(f"— Hallo, Lena! Bastelst du eine Laterne? — Ja, für St. Martin! Am Mittwoch gehen wir mit. — ({dnums[0]})___ du auch Martinslieder? — Ja, mit meiner Klasse. — Und was ({dnums[1]})___ ihr am Abend? — Wir singen und laufen mit den Laternen. Am Sonntag ({dnums[2]})___ wir Brezeln und schauen die NFL. — Lecker! Und was ({dnums[3]})___ du am Freitag? — Ich ({dnums[4]})___ Deutschland in Belgrad im Fernsehen!", 20.5)
bf.bridge("选项：")
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
reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · 写作", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Novemberwoche». Erzählen Sie: Was basteln Sie? Welche Spiele schauen Sie? Mit wem? Schreiben Sie auch einen Satz über St. Martin oder den Volkstrauertag! Die besten Texte drucken wir in VOL.4 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · 范文（84 Wörter）", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche bastle ich eine Laterne. Am Mittwoch singe ich mit meiner Klasse Martinslieder und gehe beim Laternenumzug mit. Am Freitag schaue ich mit meiner Familie Deutschland in Belgrad im Fernsehen. Das Spiel ist ein Geisterspiel — ohne Zuschauer. Am Sonntag schaue ich die NFL in München im Fernsehen. Die Lions spielen gegen die Patriots. Der Karneval beginnt um 11.11 Uhr in Köln. Am Sonntag esse ich Brezeln und trinke Apfelschorle. Am Montag gehe ich wieder in die Schule. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

# ---- keys ----
ky = wy + 320
p.hline(MX, RIGHT, ky - 12, GOLD, 2)
p.text(MX, ky + 26, "ANTWORTEN · 全部答案与简析（第 1–8 版）", 26, "sans", True, OLIVE)
kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2560, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f"（{e['note']}）"
        parts.append(s)
    kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9, strict=True)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
