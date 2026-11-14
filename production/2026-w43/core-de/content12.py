# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1　ERSTE AUSGABE", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "WÖCHENTLICH AUF DEUTSCH　每周一期　读德国人正在读的德语", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WOCHE VOM 19. BIS 25. OKTOBER 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Die Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "德语周报　VOL.1　时钟　假期　霜冻", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# clock band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "SONNTAG WIRD DIE UHR ZURÜCKGESTELLT — EINE STUNDE LÄNGER SCHLAFEN!", 31, "sans", True, ONCLOTH)  # D5 fix run2
p.text(MX + 30, 568, "In der Nacht von Samstag auf Sonntag endet die Sommerzeit: Um 3.00 Uhr springt die Uhr auf 2.00 Uhr zurück.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "本周日拨回时钟　多睡一小时", 21, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "25 小时之夜　详见第2 版", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "DIE TOPMELDUNG　头条", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Eine Stunde geschenkt: Deutschland stellt die Uhren zurück — und elf Länder haben Ferien", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Von der Lucerna-Redaktion　Leseniveau: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Am Sonntag ist es wieder so weit: Deutschland stellt die Uhren um. In der Nacht von Samstag auf Sonntag endet die Sommerzeit. Um 3.00 Uhr wird die Uhr eine Stunde zurückgestellt — auf 2.00 Uhr. Die Nacht hat dann 25 Stunden, und alle dürfen eine Stunde länger schlafen.")
f.para("Warum? Im Sommer ist es abends länger hell — das war die Idee: mehr Licht am Abend. Im Oktober sind die Tage schon kurz, und die Winterzeit beginnt — bis zum 28. März 2027.")
f.para("Und das ist nicht alles: Elf Bundesländer haben in dieser Woche gleichzeitig Herbstferien — der Höhepunkt in diesem Herbst. Viele Familien reisen, und die Züge und Freizeitparks sind voll.")
f.para("Auch der Sport liebt diese Woche: Am Dienstag und Mittwoch spielt die Champions League, am Freitag beginnt der 7. Spieltag der Bundesliga. Am Sonntag spielen Hoffenheim und Freiburg schon in der neuen Zeit — mehr dazu auf Seite 4.")
f.para("Das ist die erste Ausgabe von Die Lucerna auf Deutsch. Jede Woche lesen wir mit Ihnen das echte Deutschland — langsam, klar und ehrlich. Willkommen!")
f.bridge("讲解｜die Uhr umstellen 拨钟 · zurückstellen 往回拨 · die Sommerzeit 夏令时 · die Winterzeit 冬令时 · das Bundesland 联邦州。")
f.box("DIE WOCHE IN ZAHLEN　数字看本周", [
    ("25 — Stunden hat die Nacht von Samstag auf Sonntag（本周六之夜有 25 小时）", "serif", False, INK, 20.5, 1.35),
    ("11 — Bundesländer haben gleichzeitig Herbstferien（11 个州同时放秋假）", "serif", False, INK, 20.5, 1.35),
    ("8 000+ — Bibliotheken gibt es in Deutschland（德国有 8000 多家图书馆）", "serif", False, INK, 20.5, 1.35),
], tsize=21)  # D5 fix run2
f.head("JETZT ÜBEN　即学即练", 25)
f.ex("A2", "完成句子", "zurückgestellt", "zurückstellen = 往回拨",
     "Am Sonntag wird die Uhr eine Stunde ___.", size=20.5)
f.ex("A2", "完成句子", "25", "25 小时之夜",
     "Die Nacht von Samstag auf Sonntag hat ___ Stunden.", size=20.5)
f.ex("A2", "完成句子", "Herbstferien", "Herbstferien = 秋假",
     "Elf Bundesländer haben in dieser Woche ___.", size=20.5)
f.ex("A2", "完成句子", "Winterzeit", "冬令时到 2027 年 3 月 28 日",
     "Am Sonntag beginnt die ___ — sie dauert bis zum 28. März 2027.", size=20.5)
f.ex("B1", "完成句子", "länger", "eine Stunde länger schlafen 多睡一小时",
     "In der Nacht zum Sonntag dürfen alle eine Stunde ___ schlafen.", size=20.5)
f.ex("B1", "完成句子", "elf", "11 个州同时放假",
     "In dieser Woche haben ___ Bundesländer gleichzeitig Ferien.", size=20.5)
f.end_report()

# ---- questions of the week (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "FRAGEN", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DER WOCHE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "本周大问题　Die Fragen der deutschen Ratgeber", 17, "sans", False, GREY)  # D5 fix run2
gt = [
    ("„Vor oder zurück?“", 250),
    ("„Wann wird umgestellt?“", 226),
    ("„Handy: allein um?“", 196),
    ("„Warum Sommerzeit?“", 158),
    ("„Bleibt das für immer?“", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Die fünf Fragen stellen die Ratgeber", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in ganz Deutschland in dieser Woche.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "德国各地的指南本周都在答这五问。", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN DIESER AUSGABE　本期目录", 22, "sans", True, OLIVE)  # D5 fix run2
som = [
    ("S.2", "Die Uhr & der erste Frost", "A2"),
    ("S.3", "Zwei Feste, ein Tag", "A2→B1"),
    ("S.4", "Königsklasse & Liga", "B1"),
    ("S.5", "Ferien ohne Schule", "B1"),
    ("S.6", "Umstellung abschaffen?", "B2"),
    ("S.7", "Sätze der Woche", "A2→B2"),
    ("S.8", "Übungen & Lösungen", "alle"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "DAS WORT DER WOCHE", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« zurückstellen »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "Die Uhr geht eine Stunde zurück; Gegenteil: vorstellen.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "往回拨。反义：vorstellen。口诀见第 2 版。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "frost.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Raureif an den Zweigen: In der Nacht zum Dienstag kam der erste Frost des Herbstes — östlich von Weser und Werra lokal bis minus ein Grad, am Boden bis minus drei Grad. (Seite 2)",
        "Foto: Courtney Celley, U.S. Fish and Wildlife Service — public domain")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-herbst")
f2.head("DER HERBST BEGINNT RICHTIG", 22)  # D5 fix run2
f2.para("Kurze Tage, die ersten kalten Nächte, volle Bibliotheken und ein Spieltag in zwei Zeiten: Der Herbst zeigt in dieser Woche sein ganzes Programm.", 22.5)
f2.para("Sein Geschenk an alle Leser ist eine Stunde mehr Schlaf. Nehmen Sie sie — und lesen Sie weiter auf Seite 2!", 22.5)
f2.end_report()
# col 3 KURZ & GUT
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "KURZ & GUT　快讯", 24, "sans", True, OLIVE)
brefs = [
    ("UHRZEIT", "Sonntag, 3.00 Uhr: Die Uhren gehen eine Stunde zurück. (Seite 2)"),
    ("BIBLIOTHEKEN", "Samstag ist Tag der Bibliotheken — Berlin macht eine ganze Aktionswoche. (Seite 5)"),
    ("FUSSBALL", "Am Sonntag spielt die Bundesliga zum ersten Mal in der Winterzeit. (Seite 4)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "BLITZQUIZ　闪电问答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "读头版，选出正确答案　答案见第8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "单选", "B", "周日凌晨拨回一小时",
      "Die Uhren werden am Sonntag... A. eine Stunde vorgestellt · B. eine Stunde zurückgestellt · C. gar nicht umgestellt", size=21)
qf.ex("A2", "单选", "C", "11 个州同时秋假",
      "Wie viele Bundesländer haben Herbstferien? A. fünf · B. neun · C. elf", size=21)
qf.ex("A2", "单选", "A", "冬令时到 2027 年 3 月 28 日",
      "Die Winterzeit dauert bis... A. 28. März 2027 · B. 1. November · C. 31. Oktober", size=21)
qf.ex("A2", "单选", "B", "图书馆日：10 月 24 日周六",
      "Der Tag der Bibliotheken ist am... A. Freitag · B. Samstag · C. Sonntag", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEBEN　生活", "Die Lucerna", "LEVEL A2　Die Uhr, der Frost & die Reifen　时钟、霜冻与轮胎")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Eine Stunde mehr: Die längste Nacht des Jahres", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: A2")
f.para("Sie kommt nur einmal im Jahr: die Nacht mit 25 Stunden. In der Nacht von Samstag, dem 24. Oktober, auf Sonntag, den 25. Oktober, endet in Deutschland die Sommerzeit. Um 3.00 Uhr springen die Uhren auf 2.00 Uhr zurück.")
f.para("Die Stunde von 2.00 bis 3.00 Uhr gibt es in dieser Nacht zweimal. Die Physikalisch-Technische Bundesanstalt — sie wacht in Braunschweig über die genaue Zeit — nennt die erste Stunde 2A und die zweite 2B. Wer um 2.30 Uhr aufwacht, weiß also nicht: Ist es die erste oder die zweite halbe Stunde?")
f.para("Was muss ich selbst umstellen? Handy und Computer machen es allein. Die Funkuhr am Bett auch. Aber die Uhr am Backofen, die alte Wanduhr in der Küche und die Uhr im Auto brauchen Ihre Hand. Unser Tipp: Stellen Sie die Uhren schon am Samstagabend um — dann ist der Sonntagmorgen ganz entspannt.")
f.para("Und warum das alles? Die Sommerzeit kam 1980 nach Deutschland — beide deutsche Staaten begannen damals mit ihr. Die Idee: Am Abend bleibt es länger hell, und das Land braucht weniger Licht. Ob die Idee heute noch stimmt, lesen Sie auf Seite 6.")
f.box("DER MERKSATZ　口诀", [
    ("„Im Frühjahr stellt man die Gartenmöbel VOR das Haus — im Herbst stellt man sie ZURÜCK ins Haus.“ So merken sich die Deutschen die Richtung: vor im Frühjahr, zurück im Herbst.", "serif", False, INK, 21.5, 1.4),
], tsize=21)  # D5 fix run2
f.head("DER ERSTE FROST IST DA", 25)
f.para("Der Herbst begann in dieser Woche mit kalten Fingern: In der Nacht von Montag auf Dienstag (19./20. Oktober) kam der erste Frost. Die Temperaturen fielen auf 8 bis 0 Grad, östlich von Weser und Werra lokal auf minus 1 Grad; am Boden gab es bis minus 3 Grad. Die Gärtner deckten ihre Pflanzen ab, und am Morgen kratzten die ersten Autofahrer ihre Scheiben frei.", 23.5)
f.para("Ab der Nacht zum Mittwoch kommt dann Regen aus dem Westen — die Nächte werden milder. Aber der Frost ist eine Warnung: Der Winter ist nicht mehr weit.", 23.5)
f.para("Für Autofahrer heißt der Oktober: Winterreifen! Die Regel heißt „Von O bis O“ — von Oktober bis Ostern. Wichtig: Ein Gesetz mit festen Daten gibt es nicht. Winterreifen sind Pflicht, wenn es glatt ist — bei Eis, Schneematsch und Frost. Und seit Oktober 2024 reicht das alte M+S-Zeichen nicht mehr: Der Reifen braucht das Alpensymbol, einen Berg mit Schneeflocke.", 23.5)
f.gloss("die Bundesanstalt 联邦局（PTB 物理技术联邦局）· der Frost 霜冻 · der Reifen 轮胎 · glatt 滑的 · der Schneematsch 雪泥。")
f.end_report()

# col 3: image + facts (sequential, measured)
ix = COLX[3]
image(p, "atomuhr.jpg", ix, 200, CW, 430)
cy3 = caption(p, ix, 630, CW, "Die NIST-F1 in den USA: eine der genauesten Uhren der Welt. Auch Deutschlands Zeit kommt aus einer Atomuhr — die PTB in Braunschweig sendet das Funksignal.",
              "Foto: NIST — public domain")
sav = ["Die Nacht zum Sonntag hat 25 Stunden — die längste Nacht des Jahres.",
       "Die Stunde von 2.00 bis 3.00 Uhr gibt es in dieser Nacht zweimal: 2A und 2B.",
       "Unter 7 Grad greifen Winterreifen besser, sagen die Reifenexperten."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 14
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WUSSTEN SIE DAS?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.42) + 12  # D5 fix run2b
ey3 = sy3 + sh + 26
etvous = "Und Sie? Haben Sie eine Funkuhr zu Hause? Stellen Sie Ihre Uhren selbst um? Schreiben Sie zwei Sätze auf Deutsch und schicken Sie sie an die Redaktion: Die besten kommen in VOL.2 (Seite 7, «Leserbriefe»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你家有收音机时钟（Funkuhr）吗？你家的钟是自己拨吗？写两句德语寄给编辑部。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你家有收音机时钟（Funkuhr）吗？你家的钟是自己拨吗？写两句德语寄给编辑部。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Telling the time wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "DIE UHRZEIT SAGEN　这样报时", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Die Zeiten der Woche　本周的时间都用得上", 20, "sans", False, GREY, anchor="end")

def clock(cx, cy, r, hh, mm, label):
    p.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#f0eee5" stroke="{INK}" stroke-width="3"/>')
    import math
    for k in range(12):
        a = math.radians(k * 30)
        x1, y1 = cx + (r - 12) * math.sin(a), cy - (r - 12) * math.cos(a)
        x2, y2 = cx + r * math.sin(a), cy - r * math.cos(a)
        p.add(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="2.4"/>')
    ah = math.radians((hh % 12) * 30 + mm * 0.5)
    am = math.radians(mm * 6)
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.55)*math.sin(ah):.0f}" y2="{cy - (r*0.55)*math.cos(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.82)*math.sin(am):.0f}" y2="{cy - (r*0.82)*math.cos(am):.0f}" stroke="{OLIVE}" stroke-width="4" stroke-linecap="round"/>')
    p.text(cx, cy + r + 34, label, 22, "serif", True, INK, anchor="middle")

clock(240, dy + 130, 70, 8, 0, "Es ist acht Uhr.")
clock(560, dy + 130, 70, 2, 30, "Es ist halb drei (2.30 Uhr).")
clock(880, dy + 130, 70, 7, 45, "Es ist Viertel vor acht.")
lx = 1090
ly = dy + 58
for line in [
    ("halb drei", "= 2.30 Uhr!（不是 3.30）"),
    ("Viertel vor acht", "= 7.45 Uhr（差一刻八点）"),
    ("Viertel nach acht", "= 8.15 Uhr（八点一刻）"),
    ("Mittag / Mitternacht", "= 12.00 Uhr am Tag / in der Nacht"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 300, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 36
p.para(lx, ly + 22, "Wichtig: Dortmund–Frankfurt beginnt Samstag um 18.30 Uhr — noch Sommerzeit. Freiburg–Bayern am Sonntag um 17.30 Uhr — schon Winterzeit.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　第2 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8 版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　WIE SPÄT IST ES?", 25)
e.bridge("看时间，用德语补全句子。")
e.ex("A2", "完成句子", "halb", "halb drei = 2:30（半点在 drei 之前）",
     "2:30 — Es ist ___ drei.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Viertel vor", "7:45 = 差一刻八点",
     "7:45 — Es ist ___ acht.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Viertel nach", "8:15 = 八点一刻",
     "8:15 — Es ist ___ acht.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Mitternacht", "0:00 = 午夜",
     "0:00 — Es ist ___. Die Stadt schläft.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Mittag", "12:00 白天 = 正午",
     "12:00 am Tag — Es ist ___. Zeit für Suppe!", instr="填空", size=20, gap=8)
e.head("B　DAS PERFEKT", 25)
e.bridge("改成 Perfekt 现在完成时。")
e.ex("A2", "句型转换", "Deutschland hat die Uhren am Sonntag umgestellt.", "trennbar: um-ge-stellt",
     "Deutschland (umstellen) die Uhren am Sonntag. → ___", instr="改写", size=20, gap=8)
e.ex("A2", "句型转换", "Die Nacht hat 25 Stunden gehabt.", "haben → gehabt",
     "Die Nacht (haben) 25 Stunden. → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Der Frost ist in der Nacht zum Dienstag gekommen.", "kommen 用 sein",
     "Der Frost (kommen) in der Nacht zum Dienstag. → ___", instr="改写", size=20, gap=8)
e.ex("A2", "句型转换", "Wir haben eine Stunde länger geschlafen.", "schlafen → geschlafen",
     "Wir (schlafen) eine Stunde länger. → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Die Familien sind in den Ferien gereist.", "reisen 用 sein",
     "Die Familien (reisen) in den Ferien. → ___", instr="改写", size=20, gap=8)
e.head("C　LESEVERSTEHEN", 25)
e.bridge("读第 2 版文章，选出正确答案。")
e.ex("A2", "单选", "C", "2A 与 2B：这小时出现两次",
     "Die Stunde 2.00–3.00 Uhr gibt es... A. nie · B. einmal · C. zweimal", size=20, gap=8)
e.ex("A2", "单选", "C", "烤箱上的钟要手动拨",
     "Was stellt sich NICHT allein um? A. Handy · B. Computer · C. Backofen-Uhr", size=20, gap=8)
e.ex("A2", "单选", "A", "初霜在周一夜到周二",
     "Der erste Frost kam in der Nacht... A. von Montag auf Dienstag · B. von Freitag auf Samstag · C. am Sonntag", size=20, gap=8)
e.ex("A2", "单选", "B", "2024 年 10 月起须 Alpensymbol",
     "Winterreifen brauchen seit 2024... A. M+S-Zeichen · B. Alpensymbol · C. roten Punkt", size=20, gap=8)
e.head("D　DIE WÖRTER", 25)
e.match_set("A2", "词汇配对",
            ["der Frost", "der Reifen", "die Funkuhr", "glatt"],
            ["Uhr mit automatischem Zeitsignal",
             "Frost an Pflanzen und Scheiben",
             "der runde Gummiteil am Auto",
             "so rutschig wie Eis"],
            ["b", "c", "a", "d"],
            ["Frost=植物和玻璃上的冻气 b（释义为近似说法）", "Reifen=车上的橡胶圆环 c", "Funkuhr=自动接收信号的钟 a", "glatt=像冰一样滑 d"],
            instr="把词和释义配对")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leben.svg")
print("P2 saved, exercises so far:", len(REG))
