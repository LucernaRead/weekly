# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/de-es-proof/baseline-core/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · ZWEITE AUSGABE", 23, "sans", True, OLIVE)
p.text(975, 92, "WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WOCHE VOM 2. BIS 8. NOVEMBER 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Die Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "德 语 周 报 · VOL.2 · 足 球 周 · 油 价 · 护 理", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# football band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ENGLISCHE WOCHE — DANN DER 9. SPIELTAG!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Dienstag bis Sonntag: Champions League, Europa League, Bundesliga — alles in einer Woche", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "本周足球周 · 欧冠欧联德甲连轴转", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "详见第 4 版 · Seite 4", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "DIE TOPMELDUNG · 头条", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Englische Woche in Deutschland: Vier Nächte Fußball, dann der 9. Spieltag", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Von der Lucerna-Redaktion · Leseniveau: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Diese Woche ist eine Fußballwoche: Am Dienstag und Mittwoch spielt die Champions League, am Donnerstag die Europa League, und am Freitag beginnt der 9. Spieltag der Bundesliga. Vier Nächte Fußball, dann ein ganzes Wochenende Liga.")
f.para("Am Dienstag (21.00 Uhr) spielt Bayern bei Atlético Madrid, und Stuttgart spielt schon um 18.45 Uhr bei Galatasaray. Am Mittwoch (21.00 Uhr) empfängt Dortmund Real Betis Sevilla, und Leipzig spielt gegen Manchester City.")
f.para("Am Donnerstagabend (18.45 Uhr) spielt Hoffenheim bei Crystal Palace in London. Am Freitag (20.30 Uhr) beginnt die Bundesliga: Hamburg gegen Mönchengladbach.")
f.para("Am Samstag folgen fünf Spiele, am Sonntag drei: Köln–Leverkusen (15.30 Uhr), Freiburg–Union Berlin (17.30 Uhr), Hoffenheim–Schalke (19.30 Uhr). Das Topspiel am Samstagabend: Stuttgart gegen Bremen (18.30 Uhr).")
f.para("Aber diese Woche ist mehr als Fußball: Der Tankrabatt läuft bis zum 31. Dezember, die Pflege wird debattiert, und in Bayern sind noch Ferien — in Baden-Württemberg geht die Schule schon wieder los. Lesen Sie weiter!")
f.bridge("讲解｜die Englische Woche 一周双赛 · der Spieltag 比赛日 · empfangen 主场迎战 · die Bundesliga 德甲。")
f.box("DIE WOCHE IN ZAHLEN · 数字看本周", [
    ("9 — Spiele hat der 9. Spieltag der Bundesliga（德甲第 9 轮共 9 场比赛）", "serif", False, INK, 20.5, 1.35),
    ("6 — deutsche Teams spielen in Europa（6 支德国球队出战欧战）", "serif", False, INK, 20.5, 1.35),
    ("14,04 — Cent pro Liter beträgt der Tankrabatt（每升油减税 14.04 欧分）", "serif", False, INK, 20.5, 1.35),
])
f.head("JETZT ÜBEN · 即学即练", 25)
f.ex("A2", "完成句子", "Englische", "一周双赛",
     "Diese Woche ist eine ___ Woche: viele Spiele in wenigen Tagen.", size=20.5)
f.ex("A2", "完成句子", "Dortmund", "多特主场迎战贝蒂斯",
     "Am Mittwoch empfängt ___ Real Betis Sevilla.", size=20.5)
f.ex("A2", "完成句子", "Donnerstag", "欧联在周四",
     "Die Europa League spielt am ___: Hoffenheim bei Crystal Palace.", size=20.5)
f.ex("A2", "完成句子", "Hamburg", "周五汉堡–门兴开轮",
     "Die Bundesliga beginnt am Freitag mit ___ gegen Mönchengladbach.", size=20.5)
f.ex("B1", "完成句子", "neun", "第 9 轮共 9 场",
     "Der 9. Spieltag hat ___ Spiele.", size=20.5)
f.ex("B1", "完成句子", "Tankrabatt", "减税到 12 月 31 日",
     "Der ___ läuft bis zum 31. Dezember.", size=20.5)
f.end_report()

# ---- questions of the week (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "FRAGEN", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DER WOCHE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "本周大问题 · Die Fragen der Woche", 19, "sans", False, GREY)
gt = [
    ("„Wer gewinnt in Madrid?“", 250),
    ("„Schafft Leipzig City?“", 226),
    ("„Tankrabatt: kommt er an?“", 196),
    ("„Pflege: wer hilft zu Hause?“", 158),
    ("„Ferien: wer ist noch frei?“", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE if i == 0 else GOLD)
    byy += 92
p.text(gx + 22, byy + 16, "Die fünf Fragen, über die Deutschland", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in dieser Woche spricht.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "德国本周最热议的五个问题。", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN DIESER AUSGABE · 本期目录", 24, "sans", True, OLIVE)
som = [
    ("S.2", "Tankrabatt & Pflege", "A2"),
    ("S.3", "Ferienwechsel & Herbst", "A2→B1"),
    ("S.4", "Europapokal & Liga", "B1"),
    ("S.5", "Zurück in die Schule", "B1"),
    ("S.6", "Pflege & Stromsteuer", "B2"),
    ("S.7", "Sätze der Woche", "A2→B2"),
    ("S.8", "Übungen & Lösungen", "alle"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, BRICK)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "DAS WORT DER WOCHE", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, GOLD, 2)
p.para(gx, my + 76, "« der Tankrabatt » : Die Steuer auf Benzin sinkt — Tanken wird billiger.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, my + 152, "油价减税（加油折扣）。详见第 2 版。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "fussball.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Fußball auf dem Rasen: In dieser Woche spielen sechs deutsche Teams in Europa — und am Wochenende der 9. Spieltag der Bundesliga. (Seite 4)",
        "Foto: Staff Sgt. Stephanie Jacobs, U.S. Air Force — public domain")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2290, tag="P1-fussball")
f2.head("EINE WOCHE, VIER NÄCHTE", 25)
f2.para("Dienstag, Mittwoch, Donnerstag, Freitag: Vier Abende Fußball hintereinander — und dann der Spieltag.", 22.5)
f2.para("Wer diese Woche liebt, braucht keinen Wecker: Der Fußball weckt ihn schon. Und am Montag? Da geht es überall wieder los — die Ferien sind dann vorbei.", 22.5)
f2.end_report()
# col 3 KURZ & GUT
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 1914, "KURZ & GUT · 快讯", 24, "sans", True, OLIVE)
brefs = [
    ("FUSSBALL", "Champions League, Europa League, Bundesliga: alles in einer Woche. (Seite 4)"),
    ("TANKRABATT", "14,04 Cent pro Liter weniger Steuer — bis zum 31. Dezember. (Seite 2)"),
    ("FERIEN", "Baden-Württemberg ist zurück in der Schule, Bayern hat noch Ferien. (Seite 5)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, BRICK)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, GOLD, 2)
p.text(MX, qy + 36, "BLITZQUIZ · 闪电问答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "读头版，选出正确答案 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "单选", "B", "拜仁周二客战马竞",
      "Bayern spielt am Dienstag bei... A. Real Madrid · B. Atlético Madrid · C. Galatasaray", size=21)
qf.ex("A2", "单选", "C", "霍芬海姆欧联客战水晶宫",
      "Hoffenheim spielt in der Europa League bei... A. Marseille · B. Manchester City · C. Crystal Palace", size=21)
qf.ex("A2", "单选", "A", "减税到 12 月 31 日",
      "Der Tankrabatt läuft bis... A. 31. Dezember · B. 1. November · C. 31. Oktober", size=21)
qf.ex("A2", "单选", "A", "周五汉堡–门兴开轮",
      "Der 9. Spieltag beginnt am Freitag mit... A. Hamburg–Gladbach · B. Dortmund–Elversberg · C. Stuttgart–Bremen", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEBEN · 生活", "Die Lucerna", "LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 油价、电力税与护理")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Tanken für weniger: Der Tankrabatt läuft bis Silvester", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: A2")
f.para("Gute Nachricht für alle, die Auto fahren: Seit dem 1. Oktober ist das Tanken in Deutschland billiger. Der Bundestag und der Bundesrat haben am 25. September beschlossen: Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter. Das gilt bis zum 31. Dezember 2026. Mit der Mehrwertsteuer sind es an der Zapfsäule rund 16,7 Cent pro Liter.")
f.para("Was heißt das für eine Tankfüllung? Wer 50 Liter tankt, spart rund 8,35 Euro. Der Staat verzichtet dafür auf rund 2,5 Milliarden Euro an Steuern — Bund und Länder teilen sich die Kosten etwa zur Hälfte.")
f.para("Aber Achtung: Die Tankstellen müssen den Rabatt nicht eins zu eins weitergeben. Das Gesetz senkt nur die Steuer — den Preis macht die Tankstelle. Am Morgen des 1. Oktober fielen die Preise um 14 bis 15 Cent, mittags stiegen sie schon wieder: Der ADAC berichtet, dass ein Teil des Rabatts im Preis „verschwindet“.")
f.para("Zweites Thema der Woche: die Stromsteuer. Union und SPD streiten noch, wie stark sie sinken soll. Viele Haushalte hoffen auf billigeren Strom — vor allem, weil die Energiepreise die Einkommen drücken. Auch der ZEW-Index zeigt es: Die Erwartungen der Finanzexperten fielen im Oktober um 6,6 Punkte auf 28,1.")
f.para("Drittes Thema: die Pflege. Nach Angaben der ARD-Sendung „Hart aber fair“ (26. Oktober) brauchen in Deutschland mehr als sechs Millionen Menschen Pflege. Die meisten von ihnen werden zu Hause gepflegt — von rund zehn Millionen Angehörigen. Am Montag, dem 26. Oktober, diskutierte die ARD-Sendung „Hart aber fair“ (21.00 Uhr): „Pflege zu Hause — Lässt die Politik Angehörige allein?“ Mehr dazu auf Seite 6.")
f.gloss("der Tankrabatt 油价减税 · die Zapfsäule 加油机 · die Energiesteuer 能源税 · die Mehrwertsteuer 增值税 · der Angehörige 亲属。")
f.end_report()

# col 3: four boxes (hand-rolled; CORRECTED height formula — see KIT §geometry:
# content bottom = 30.47 + 33k + 30.53*sum(lines); 45 used as the constant for ~14px slack)
ix = COLX[3]
zapf = ["14,04 Cent pro Liter — so viel Steuer weniger seit dem 1. Oktober.",
        "16,7 Cent pro Liter an der Zapfsäule (mit Mehrwertsteuer).",
        "Rund 8,35 Euro — so viel spart, wer 50 Liter tankt."]
sy3 = 200
sh = 45 + 33 * len(zapf) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in zapf)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "AN DER ZAPFSÄULE · 加油机旁", 24, "sans", True, OLIVE)
yy3 += 52
for t in zapf:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box1 ends", sy3 + sh)
sav = ["Der Tankrabatt gilt nur bis zum 31. Dezember 2026 — danach ist Schluss.",
       "Die Tankstelle muss den Rabatt nicht voll weitergeben — der Preis ist frei.",
       "Mehr als sechs Millionen Menschen in Deutschland brauchen Pflege (ARD „Hart aber fair“, 26. Oktober)."]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(sav) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in sav)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WUSSTEN SIE DAS?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box2 ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Fahren Sie Auto? Was kostet ein Liter Benzin in Ihrem Land? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("你开车吗？你那里的油价是多少？写两句德语寄来。", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你开车吗？你那里的油价是多少？写两句德语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 box3 ends", ey3 + eh)
zew = ["Erwartungen: 28,1 Punkte (minus 6,6 im Oktober).",
       "Lage: minus 35,9 Punkte (plus 11,2).",
       "Prognose: Die Wirtschaft wächst langsam, aber nicht von allein."]
sy3 = ey3 + eh + 26
sh = 45 + 33 * len(zew) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in zew)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ZEW IN KÜRZE · ZEW 指数简讯", 24, "sans", True, OLIVE)
yy3 += 52
for t in zew:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box4 ends", sy3 + sh)

# ---- Rechnen wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "RECHNEN WIR MAL · 算一算", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Die Zahlen der Woche · 本周数字", 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 58
for line in [
    ("50 Liter × 14,04 Cent", "= 7,02 € Steuer weniger"),
    ("mit Mehrwertsteuer", "= rund 8,35 € gespart"),
    ("Staat: rund 2,5 Milliarden €", "= weniger Einnahmen"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 360, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 36
p.para(1090, ly - 108 + 22, "Achtung: Die Steuer sinkt — aber den Preis macht die Tankstelle. Der ADAC berichtet, dass ein Teil des Rabatts im Preis „verschwindet“. Vergleichen Sie die Preise, bevor Sie tanken!", 20.5, "serif", False, INK, RIGHT - 1090, 1.42)
p.para(1090, ly - 108 + 22 + 4 * 29.1 + 10, "注意：减的是税，定价的是油站。出发前比比价。", 20, "sans", False, GREY, RIGHT - 1090, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 第 2 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · WIE VIEL SPAREN?", 25)
e.bridge("看第 2 版文章，用数字填空。")
e.ex("A2", "完成句子", "14,04", "每升减税 14.04 欧分",
     "Die Steuer sinkt um ___ Cent pro Liter.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "8,35", "50 升省约 8.35 欧元",
     "Wer 50 Liter tankt, spart rund ___ Euro.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "31. Dezember", "减税到 2026 年底",
     "Der Tankrabatt läuft bis zum ___ 2026.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "2,5 Milliarden", "国家少收约 25 亿欧元",
     "Der Staat verzichtet auf rund ___ Euro.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Zapfsäule", "加油机旁的实际降幅",
     "Mit Mehrwertsteuer sind es an der ___ rund 16,7 Cent weniger.", instr="填空", size=20, gap=8)
e.head("B · DAS PERFEKT", 25)
e.bridge("改成 Perfekt 现在完成时。")
e.ex("A2", "句型转换", "Der Bundestag hat den Tankrabatt beschlossen.", "beschließen → beschlossen",
     "Der Bundestag (beschließen) den Tankrabatt. → ___", instr="改写", size=20, gap=8)
e.ex("A2", "句型转换", "Die Preise sind am Morgen gefallen.", "fallen 用 sein",
     "Die Preise (fallen) am Morgen. → ___", instr="改写", size=20, gap=8)
e.ex("A2", "句型转换", "Wir haben 50 Liter getankt.", "tanken → getankt",
     "Wir (tanken) 50 Liter. → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Die Tankstellen haben den Rabatt nicht voll weitergegeben.", "weitergeben 可分动词",
     "Die Tankstellen (weitergeben) den Rabatt nicht voll. → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Die Erwartungen sind im Oktober gefallen.", "ZEW 预期下降",
     "Die Erwartungen (fallen) im Oktober. → ___", instr="改写", size=20, gap=8)
e.head("C · LESEVERSTEHEN", 25)
e.bridge("读第 2 版文章，选出正确答案。")
e.ex("A2", "单选", "B", "减的是能源税",
     "Was sinkt beim Tankrabatt? A. der Preis direkt · B. die Steuer · C. die Mehrwertsteuer allein", size=20, gap=8)
e.ex("A2", "单选", "B", "油站定价",
     "Wer bestimmt den Preis? A. der Staat · B. die Tankstelle · C. der ADAC", size=20, gap=8)
e.ex("A2", "单选", "A", "联盟党与社民党",
     "In der Stromsteuer-Debatte streiten... A. Union und SPD · B. Bayern und Dortmund · C. ADAC und ZEW", size=20, gap=8)
e.ex("A2", "单选", "B", "家属居家护理",
     "Wer pflegt zu Hause? A. die Ärzte · B. die Angehörigen · C. die Tankstellen", size=20, gap=8)
e.head("D · DIE WÖRTER", 25)
e.match_set("A2", "词汇配对",
            ["der Tankrabatt", "die Zapfsäule", "die Mehrwertsteuer", "der Angehörige"],
            ["die Steuer, die beim Kauf dazu kommt",
             "die Ermäßigung auf die Energiesteuer",
             "ein Familienmitglied, das pflegt",
             "die Säule an der Tankstelle, aus der Benzin kommt"],
            ["b", "d", "a", "c"],
            ["Tankrabatt=油价减税 b", "Zapfsäule=加油机 d", "Mehrwertsteuer=增值税 a", "Angehörige=亲属 c"],
            instr="把词和释义配对")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leben.svg")
print("P2 saved, exercises so far:", len(REG))
