# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/de-ko-proof/baseline-rerun/svg")
os.makedirs(OUT, exist_ok=True)

CURPAGE[0] = 8
p = BSPage4()
p.band("ÜBUNGEN & ANTWORTEN · 练习与答案", "Die Lucerna", "SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方")

bf = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1505, tag="P8-battery")

# ---- A. cloze (register first for marker numbers) ----
cloze_defs = [
    ("A2", "B", "spielt（第三人称单数）"),
    ("A2", "A", "beginnt（第三人称单数）"),
    ("A2", "B", "kauft（第三人称单数）"),
    ("A2", "C", "schnitzt 雕刻南瓜"),
    ("A2", "B", "schläft（第三人称单数）"),
    ("B1", "B", "Tankrabatt 油价减税"),
    ("A2", "A", "geht（第三人称单数）"),
    ("B1", "B", "erzählt（第三人称单数）"),
]
cnums = [reg_ex(lv, "完形填空", k, nt) for lv, k, nt in cloze_defs]
bf.head("A · LÜCKENTEXT · 完形填空", 24)
bf.para(f"Lena freut sich auf die Fußballwoche. Am Dienstag sieht sie Bayern bei Atlético Madrid, am Mittwoch Dortmund gegen Real Betis. Am Donnerstag ({cnums[0]})___ Hoffenheim bei Crystal Palace, und am Freitag ({cnums[1]})___ die Bundesliga mit Hamburg gegen Gladbach. Am Samstag ({cnums[2]})___ Lena einen Kürbis und ({cnums[3]})___ ihn zu Hause. Am Sonntag ({cnums[4]})___ sie lange, denn die Woche war anstrengend. In der Schule erzählt sie: „Die Fußballwoche war toll! Und der ({cnums[5]})___ läuft noch bis Dezember.“ Am Montag ({cnums[6]})___ Lena wieder in die Schule und ({cnums[7]})___ von den Spielen.", 20.5)
bf.bridge("选项：")
for n, opts in zip(cnums, [
    "A. spielen · B. spielt · C. spieltet",
    "A. beginnt · B. beginnen · C. begann",
    "A. kaufen · B. kauft · C. kaufte",
    "A. malt · B. kocht · C. schnitzt",
    "A. schlafen · B. schläft · C. schlief",
    "A. Spieltag · B. Tankrabatt · C. Advent",
    "A. geht · B. gehen · C. ging",
    "A. erzählen · B. erzählt · C. erzählte",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)

# ---- B. general MC ----
bf.head("B · WISSENSFRAGEN · 综合问答", 24)
bf.ex("B1", "单选", "A", "减税到 2026 年 12 月 31 日",
      "Der Tankrabatt läuft bis... A. 31. Dezember 2026 · B. 1. November · C. 31. Oktober", size=19.5, gap=8)
bf.ex("A2", "单选", "B", "拜仁周二客战马竞",
      "Bayern spielt am Dienstag bei... A. Galatasaray · B. Atlético Madrid · C. Real Betis", size=19.5, gap=8)
bf.ex("A2", "单选", "A", "霍芬海姆欧联客战水晶宫",
      "Hoffenheim spielt in der Europa League bei... A. Crystal Palace · B. Marseille · C. Manchester City", size=19.5, gap=8)
bf.ex("B1", "单选", "B", "BW 假期已结束",
      "In welchem Bundesland sind die Ferien schon vorbei? A. Bayern · B. Baden-Württemberg · C. Berlin", size=19.5, gap=8)
bf.ex("B1", "单选", "B", "ZEW 预期 28.1",
      "Der ZEW-Index: Die Erwartungen fielen im Oktober auf... A. 34,7 · B. 28,1 · C. 47,1", size=19.5, gap=8)
bf.ex("A2", "单选", "A", "周五汉堡–门兴开轮",
      "Der 9. Spieltag beginnt am Freitag mit... A. Hamburg–Gladbach · B. Stuttgart–Bremen · C. Köln–Leverkusen", size=19.5, gap=8)
bf.ex("B1", "单选", "B", "10 月 26 日节目讨论居家护理",
      "„Hart aber fair“ diskutierte in der Sendung am 26. Oktober... A. die Stromsteuer · B. die Pflege zu Hause · C. den Tankrabatt", size=19.5, gap=8)
bf.ex("A2", "单选", "B", "诸圣节 11 月 1 日",
      "Allerheiligen ist am... A. 31. Oktober · B. 1. November · C. 2. November", size=19.5, gap=8)

# ---- C. reading ----
bf.head("C · LESEVERSTEHEN · 阅读理解", 24)
bf.para("Familie Berger aus Stuttgart hat am Montag wieder Schule: Die Kinder gehen um halb acht aus dem Haus. Am Dienstagabend schaut die Familie Bayern bei Atlético im Fernsehen. Am Samstag fährt sie zum Markt und kauft einen Kürbis. Am Sonntag schaut sie Hoffenheim gegen Schalke um 19.30 Uhr. „Eine Woche mit Fußball und Kürbis“, sagt Frau Berger.", 20.5)
bf.ex("B1", "单选", "A", "halb acht = 7:30",
      "Wann gehen die Kinder aus dem Haus? A. um halb acht · B. um acht · C. um halb neun", size=19.5, gap=8)
bf.ex("A2", "单选", "B", "周二看拜仁客战马竞",
      "Was schaut die Familie am Dienstag? A. Dortmund–Betis · B. Bayern bei Atlético · C. Hoffenheim–Schalke", size=19.5, gap=8)
bf.ex("A2", "单选", "A", "周六买南瓜",
      "Was kauft die Familie am Samstag? A. einen Kürbis · B. ein Buch · C. ein Kostüm", size=19.5, gap=8)
bf.ex("B1", "单选", "B", "霍芬海姆–沙尔克周日 19:30",
      "Wann spielt Hoffenheim gegen Schalke? A. Samstag 18.30 Uhr · B. Sonntag 19.30 Uhr · C. Freitag 20.30 Uhr", size=19.5, gap=8)

# ---- D. sentence building ----
bf.head("D · SÄTZE BAUEN · 造句", 24)
bf.ex("A2", "造句", "Die Bundesliga beginnt am Freitag.", "时间状语，动词第二位",
      "die Bundesliga / beginnt / am Freitag → ___", instr="造句", size=19.5, gap=8)
bf.ex("A2", "造句", "Wir schauen Bayern bei Atlético.", "主谓宾顺序",
      "wir / schauen / Bayern / bei Atlético → ___", instr="造句", size=19.5, gap=8)
bf.ex("B1", "造句", "Die Kinder gehen am Montag wieder in die Schule.", "时间状语开头，动词第二位",
      "die Kinder / gehen / am Montag / wieder in die Schule → ___", instr="造句", size=19.5, gap=8)
bf.ex("B1", "造句", "In Bayern dauern die Ferien noch an.", "地点开头，动词第二位",
      "in Bayern / dauern / die Ferien / noch an → ___", instr="造句", size=19.5, gap=8)

# ---- E. translation ----
bf.head("E · ÜBERSETZEN · 翻译", 24)
bf.ex("A2", "翻译", "油价减税持续到十二月。", "laufen = 持续",
      "Der Tankrabatt läuft bis Dezember.（译成中文）", instr="翻译", size=19.5, gap=8)
bf.ex("A2", "翻译", "我周二看足球。", "schauen = 看",
      "Ich schaue am Dienstag Fußball.（译成中文）", instr="翻译", size=19.5, gap=8)
bf.ex("B1", "翻译", "学校又开学了。", "wieder begonnen = 又开始",
      "Die Schule hat wieder begonnen.（译成中文）", instr="翻译", size=19.5, gap=8)
bf.ex("B1", "翻译", "Am Sonntag schlafe ich eine Stunde länger.", "多睡一小时 = eine Stunde länger schlafen",
      "我周日多睡一小时。（译成德语）", instr="翻译", size=19.5, gap=8)

# ---- F. matching ----
bf.head("F · WÖRTER PAAREN · 词汇配对", 24)
bf.match_set("B1", "词汇配对",
             ["der Tankrabatt", "die Pflege", "der Advent", "der Pausenhof"],
             ["die Zeit vor Weihnachten, in der man plant und bastelt",
              "die Ermäßigung auf die Energiesteuer beim Tanken",
              "der Hof der Schule, auf dem die Kinder in der Pause spielen",
              "die Hilfe für Menschen, die nicht mehr allein leben können"],
             ["b", "d", "a", "c"],
             ["Tankrabatt=油价减税 b", "Pflege=护理 d", "Advent=将临期 a", "Pausenhof=课间操场 c"],
             instr="把词和释义配对")

# ---- G. dialogue ----
ddefs = [
    ("A2", "B", "schaust（第二人称单数）"),
    ("A2", "A", "siehst（第二人称单数）"),
    ("A2", "A", "kochen（第一人称复数）"),
    ("B1", "B", "machst（第二人称单数）"),
    ("B1", "A", "gehe（第一人称单数）"),
]
dnums = [reg_ex(lv, "对话补全", k, nt) for lv, k, nt in ddefs]
bf.head("G · DIALOG · 对话补全", 24)
bf.para(f"— Hallo, Lena! Schaust du am Dienstag Fußball? — Ja, Bayern bei Atlético! Um 21.00 Uhr. — Und am Mittwoch? — Dortmund gegen Betis. Ich bin für Dortmund. — ({dnums[0]})___ du am Sonntag auch Fußball? — Ja, Hoffenheim gegen Schalke um 19.30 Uhr. — Mit wem ({dnums[1]})___ du das Spiel? — Mit meiner Familie, zu Hause. Wir ({dnums[2]})___ Kürbissuppe. — Lecker! Und was ({dnums[3]})___ du am Montag? — Ich ({dnums[4]})___ wieder in die Schule. Die Ferien sind vorbei!", 20.5)
bf.bridge("选项：")
for n, opts in zip(dnums, [
    "A. schaut · B. schaust · C. schauen",
    "A. siehst · B. sehen · C. sieht",
    "A. kochen · B. koche · C. kocht",
    "A. machen · B. machst · C. macht",
    "A. gehe · B. geht · C. gehen",
]):
    bf.para(f"{n}. {opts}", 18.5, "sans", False, INK, 1.32, 2)
bf.end_report()

# ---- writing strip ----
wy = 1520
p.hline(MX, RIGHT, wy - 14, GOLD, 2)
reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")
wx, ww = span_x(0, 2)
p.text(wx, wy + 26, "H · SCHREIBEN · 写作", 25, "sans", True, OLIVE)
p.para(wx, wy + 62, "Schreiben Sie einen kurzen Text (80 bis 100 Wörter): «Meine Fußballwoche». Erzählen Sie: Welche Spiele schauen Sie? Mit wem? Was essen Sie beim Spiel? Schreiben Sie auch einen Satz über den Tankrabatt oder die Pflege! Die besten Texte drucken wir in VOL.3 (Seite 7, «Leserbriefe»).", 21.5, "serif", False, INK, ww, 1.45)
p.para(wx, wy + 196, "用德语写 80–100 词：《我的足球周》。写清看哪几场比赛、和谁一起、看球时吃什么，并写一句关于油价减税或护理的话。", 20, "sans", False, GREY, ww, 1.4)
mx2, mw2 = span_x(2, 2)
p.rect(mx2, wy, mw2, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(mx2 + 22, wy + 38, "MUSTER · 范文（84 Wörter）", 23, "sans", True, OLIVE)
p.para(mx2 + 22, wy + 74, "In dieser Woche schaue ich viel Fußball. Am Dienstag sehe ich Bayern bei Atlético, am Mittwoch Dortmund gegen Betis. Am Donnerstag spielt Hoffenheim bei Crystal Palace. Am Freitag sehe ich Hamburg gegen Gladbach mit meinem Bruder. Wir essen Brezeln und trinken Apfelschorle. Am Sonntag schauen wir Hoffenheim gegen Schalke. Der Tankrabatt freut mich sehr: Ich tanke 50 Liter und spare rund 8,35 Euro. Am Samstag kaufe ich einen Kürbis und schnitze ihn mit Lena. Am Montag gehe ich zur Arbeit. Die Woche macht Spaß!", 21, "serif", False, INK, mw2 - 44, 1.42)

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
    kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)
kf.end_report()
p.foot(8)
p.save(f"{OUT}/p8-uebungen.svg")
print("P8 saved, TOTAL exercises:", len(REG))
