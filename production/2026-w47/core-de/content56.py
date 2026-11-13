# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND　青年", "Die Lucerna", "LEVEL B1　Adventskalender, Wunschzettel & Schule　降临节日历、愿望单与学校")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Adventskalender basteln: 24 Türchen bis Weihnachten", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B1")
f.para("Am Montag, dem 16. November, öffnen in Köln zwei große Weihnachtsmärkte. Aber für Kinder beginnt die schönste Zeit erst am 1. Dezember: Dann öffnet sich das erste Türchen des Adventskalenders. Bis dahin bleibt Zeit zum Basteln.")
f.para("Was ist ein Adventskalender? Ein Kalender mit 24 Türchen — für jeden Dezembertag bis Weihnachten eines. Hinter jedem Türchen wartet eine kleine Überraschung. Das kann Schokolade, ein Bild oder ein Spruch sein. Viele Familien basteln ihren Kalender selbst: aus Papier, Pappe und viel Fantasie.")
f.para("So alt ist die Idee: Schon im Jahr 1903 gab es einen Adventskalender mit dem Titel „Im Lande des Christkinds“. Die Kinder konnten die Bilder ausschneiden und auf den Kalender kleben. Das Bild auf dieser Seite zeigt ihn — über 120 Jahre alt, und die Idee lebt noch heute.")
f.para("Und der Wunschzettel? Im November schreiben viele Kinder ihren Wunschzettel für Weihnachten. Was steht darauf? Ein Buch, ein Spiel, ein Fahrrad — oder ein Besuch auf dem Weihnachtsmarkt. Der Wunschzettel kommt ans Fenster oder geht per Post an das Christkind oder den Weihnachtsmann.")
f.para("Was macht man nach der Schule im dunklen November? Lesen, was man im Herbst begonnen hat, oder einen Adventskalender basteln. In vielen Familien brennt im Advent eine Kerze auf dem Tisch, und auf dem Kalender leuchtet ein Stern. Unser Tipp: Suchen Sie sich ein Buch für die dunklen Abende — die Bibliotheken haben im November oft neue Bücher und Lesungen. Und wer Sport mag: Am Freitag kehrt die Bundesliga zurück.")
f.para("Auch der Fußball gehört zur Woche: Am Montag spielt die Nationalmannschaft in Berlin gegen die Niederlande — viele Jugendliche schauen das Spiel im Fernsehen. Am Freitag spielt der FC Bayern gegen Köln. Mehr dazu auf Seite 4.")
f.gloss("der Adventskalender 降临节日历 · das Türchen 小门 · der Wunschzettel 愿望单 · das Christkind 圣婴 · basteln 制作。")
f.end_report()

# col 3: facts + vocab + Und Sie (hand-rolled; CORRECTED height formula — see W45 KIT §geometry)
ix = COLX[3]
facts = ["Ein Adventskalender hat 24 Türchen — bis Weihnachten.",
         "Das erste Türchen öffnet sich am 1. Dezember.",
         "Schon 1903 gab es den Kalender „Im Lande des Christkinds“."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ADVENTSKALENDER", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 facts ends", sy3 + sh)
words = ["das Türchen — 小门", "der Wunschzettel — 愿望单", "das Christkind — 圣婴",
         "die Schokolade — 巧克力", "die Kerze — 蜡烛", "der Stern — 星星"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ADVENTSWÖRTER　降临节词汇", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P5 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Basteln Sie einen Adventskalender? Was steht auf Ihrem Wunschzettel? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("你做降临节日历吗？你的愿望单上写了什么？写两句德语寄来。", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你做降临节日历吗？你的愿望单上写了什么？写两句德语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 undsie ends", ey3 + eh)

# ---- Advent calendar image (col 3, below the boxes) ----
iy5 = ey3 + eh + 26
image(p, "christkind.jpg", ix, iy5, CW, 313)
cy5 = caption(p, ix, iy5 + 313, CW,
              "Adventskalender aus dem Jahr 1903: „Im Lande des Christkinds“.",
              "Bild: Richard Ernst Kepler, 1903 — public domain")
print("P5 col3 image ends", cy5)

# ---- Wochenplan wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 300, fill=BOX)
p.text(sx + 24, 1162, "DER WOCHENPLAN DER REDAKTION　编辑部一周计划", 24, "sans", True, OLIVE)
planrows = [
    ("Mo 16.11.", "Nationalelf in Berlin: Deutschland – Niederlande (20.45 Uhr, ARD)."),
    ("Di 17.11.", "Weihnachtsmarkt am Dom: offizielle Eröffnung um 19 Uhr."),
    ("Mi 18.11.", "Buß- und Bettag: kein Unterricht in Bayern, Feiertag in Sachsen."),
    ("Do 19.11.", "Adventskalender basteln: Papier, Pappe, Schere — und Fantasie."),
    ("Fr 20.11.", "Bundesliga: Bayern – Köln (20.30 Uhr)."),
]
pyy = 1184
for t, txt in planrows:
    p.text(sx + 24, pyy + 24, t, 21, "sans", True, OLIVE)
    p.text(sx + 190, pyy + 24, txt, 21.5, "serif", False, INK)
    pyy += 45

# ---- P5 exercises ----
ey = 1756  # W47 D1: was 1780; col-3 image ends 1732.9, hline at ey-12=1744 clears it
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　第 5 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P5-ex")
e.head("A　LESEVERSTEHEN", 25)
e.bridge("读第 5 版文章，选出正确答案。")
e.ex("B1", "单选", "A", "第一扇小门 12 月 1 日打开",
     "Wann öffnet sich das erste Türchen? A. am 1. Dezember · B. am 16. November · C. am 29. November", size=22, gap=8)
e.ex("B1", "单选", "B", "日历有 24 扇小门",
     "Wie viele Türchen hat ein Adventskalender? A. 12 · B. 24 · C. 30", size=22, gap=8)
e.ex("B1", "单选", "B", "1903 年的日历叫《圣婴之国》",
     "Wie heißt der Adventskalender aus dem Jahr 1903? A. „Im Lande des Weihnachtsmanns“ · B. „Im Lande des Christkinds“ · C. „Im Lande der Engel“", size=22, gap=8)
e.ex("B1", "单选", "B", "愿望单寄给圣婴或圣诞老人",
     "Wohin geht der Wunschzettel? A. an den Osterhasen · B. an das Christkind oder den Weihnachtsmann · C. an den Nikolaus im Sommer", size=22, gap=8)
e.ex("A2", "单选", "A", "周一国家队比赛",
     "Was schauen viele Jugendliche am Montag? A. die Nationalmannschaft in Berlin · B. die Bundesliga · C. den Weihnachtsmarkt", size=22, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.bridge("用方框里的词填空。")
e.para("Türchen · Wunschzettel · Christkind · Schokolade · Kerze · Stern", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "Türchen", "小门",
     "Am 1. Dezember öffnet sich das erste ___.", instr="填空", size=22, gap=8)
e.ex("B1", "完成句子", "Wunschzettel", "愿望单",
     "Die Kinder schreiben im November ihren ___.", instr="填空", size=22, gap=8)
e.ex("B1", "完成句子", "Christkind", "圣婴",
     "Der Wunschzettel geht an das ___ oder den Weihnachtsmann.", instr="填空", size=22, gap=8)
e.ex("B1", "完成句子", "Schokolade", "巧克力",
     "Hinter einem Türchen wartet oft ___.", instr="填空", size=22, gap=8)
e.ex("A2", "完成句子", "Kerze", "蜡烛",
     "Im Advent brennt eine ___ auf dem Tisch.", instr="填空", size=22, gap=8)
e.ex("A2", "完成句子", "Stern", "星星",
     "Auf dem Adventskalender ist ein ___.", instr="填空", size=22, gap=8)
e.head("C　SÄTZE MIT «WEIL»", 25)
e.bridge("用 weil 连接两个句子（动词放句末）。")
e.ex("B1", "句型转换", "Die Kinder freuen sich, weil der Advent beginnt.", "weil 句动词置尾",
     "Die Kinder freuen sich. Der Advent beginnt. (weil) → ___", instr="改写", size=22, gap=8)
e.ex("B1", "句型转换", "Er bleibt zu Hause, weil es dunkel ist.", "ist 置尾",
     "Er bleibt zu Hause. Es ist dunkel. (weil) → ___", instr="改写", size=22, gap=8)
e.ex("B1", "句型转换", "Sie geht in die Bibliothek, weil sie ein Buch lesen will.", "will 置尾",
     "Sie geht in die Bibliothek. Sie will ein Buch lesen. (weil) → ___", instr="改写", size=22, gap=8)
e.ex("B1", "句型转换", "Köln feiert, weil die Weihnachtsmärkte öffnen.", "öffnen 置尾",
     "Köln feiert. Die Weihnachtsmärkte öffnen. (weil) → ___", instr="改写", size=22, gap=8)
e.head("D　RICHTIG ODER FALSCH?", 25)
e.bridge("判断对错。")
e.ex("A2", "判断对错", "Richtig", "11 月 16 日科隆圣诞市场开市",
     "Am 16. November öffnen der Markt am Dom und der Markt der Engel. Richtig oder falsch?", instr="判断", size=22, gap=8)
e.ex("B1", "判断对错", "Falsch", "小门后是惊喜，不是空的",
     "Hinter jedem Türchen wartet nichts. Richtig oder falsch?", instr="判断", size=22, gap=8)
e.ex("A2", "判断对错", "Richtig", "孩子们给圣婴写愿望单",
     "Die Kinder schreiben ihren Wunschzettel an das Christkind. Richtig oder falsch?", instr="判断", size=22, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG　深读", "Die Lucerna", "LEVEL B2　Stille Woche & Haushalt　安静的一周与财政预算")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Eine stille Woche: Was bedeuten Buß- und Bettag und Totensonntag?", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: B2")
f.para("Am Mittwoch, dem 18. November, ist Buß- und Bettag. Am Sonntag, dem 22. November, ist Totensonntag. Zwischen beiden Tagen liegt eine stille Woche: keine lauten Feste, keine großen Partys — dafür Zeit zum Nachdenken. Was bedeuten diese Tage?")
f.para("Der Buß- und Bettag ist ein evangelischer Feiertag. Er lädt zur Buße und zum Nachdenken ein: Was war falsch in diesem Jahr? Was kann ich besser machen? Der Tag liegt immer elf Tage vor dem ersten Advent — in diesem Jahr am 18. November. Nur Sachsen feiert ihn als gesetzlichen Feiertag.")
f.para("Der Totensonntag ist der letzte Sonntag des Kirchenjahres. Evangelische Christen gedenken an diesem Tag ihrer Verstorbenen: Sie gehen auf den Friedhof, zünden Kerzen an und legen Blumen nieder. Am nächsten Sonntag beginnt mit dem ersten Advent ein neues Kirchenjahr.")
f.para("Zweites Thema: der Bundeshaushalt 2027. Er soll am Freitag, dem 27. November, verabschiedet werden. Auch die Stromsteuer ist noch offen: Kanzler Friedrich Merz will sie für alle senken. Haushalte zahlen weiter 2,05 Cent pro Kilowattstunde. Ob eine Einigung gelingt, ist offen.")
f.para("Zwei Themen, ein Muster: Die stillen Tage und der Haushalt betreffen fast jeden. Am Sonntag ist es still im Land. Am Montag geht die Debatte weiter — und die Weihnachtsmärkte öffnen wieder.")
f.para("Und die Kirche? Der erste Advent ist am 29. November. Dann beginnt die Adventszeit — mit Kerzen, Liedern und dem ersten Türchen des Adventskalenders. Die stille Woche ist der Übergang: vom November in den Advent.")
f.gloss("die Buße 忏悔 · das Kirchenjahr 教会年 · der Verstorbene 故者 · der Friedhof 墓地 · der Haushalt 财政预算 · die Einigung 达成一致。")
f.end_report()

# col 3: numbers box + debate box (measured)
ix = COLX[3]
tl = [("18.11.", "Buß- und Bettag — elf Tage vor dem ersten Advent."),
      ("22.11.", "Totensonntag — der letzte Sonntag des Kirchenjahres."),
      ("29.11.", "Erster Advent — Beginn des neuen Kirchenjahres."),
      ("2,05", "Cent pro Kilowattstunde: Stromsteuer für Haushalte."),
      ("27.11.", "Verabschiedung des Bundeshaushalts 2027 geplant."),
      ("1995", "Seit diesem Jahr ist der Buß- und Bettag nur noch in Sachsen ein Feiertag.")]
tlh = 45 + 30.5 * len(tl) + 29.11 * sum(len(wrap(t, "serif", False, 20.5, CW - 152)) for yr, t in tl)
p.rect(ix, 200, CW, tlh, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DIE ZAHLEN　本周数字", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, OLIVE)
    yy3 = p.para(ix + 130, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 152, 1.42) + 10
print("P6 col3 numbers ends", 200 + tlh)
deb = "Stille Tage: Gedenken braucht Ruhe — darüber sind sich fast alle einig. Haushalt: Wie stark die Stromsteuer sinkt, ist noch offen. Beides betrifft fast jeden Haushalt."
hy3 = 200 + tlh + 26
hh = 140 + 29.82 * len(wrap(deb, "serif", False, 21, CW - 44)) + 27.69 * (len(wrap("安静的日子：纪念需要安宁——对此几乎人人赞同。预算：电力税降多少尚未确定。两者都关系到几乎每个家庭。", "sans", False, 19.5, CW - 44)) - 1)
p.rect(ix, hy3, CW, hh, fill="#f0eee5")
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "DIE DEBATTE IN EINEM SATZ", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, deb, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "安静的日子：纪念需要安宁——对此几乎人人赞同。预算：电力税降多少尚未确定。两者都关系到几乎每个家庭。", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)

# ---- Die stille Woche wide box (cols 0-2) ----
sx, swd = span_x(0, 3)
p.rect(sx, 1120, swd, 252, fill="#f0eee5")
p.text(sx + 24, 1162, "DIE STILLE WOCHE　安静的一周", 24, "sans", True, OLIVE)
p.text(sx + 24, 1210, "BUß- UND BETTAG — 18. NOVEMBER", 21, "sans", True, OLIVE)
p.text(sx + 24 + (swd - 48) // 2, 1210, "TOTENSONNTAG — 22. NOVEMBER", 21, "sans", True, OLIVE)
pro = ["Evangelischer Tag zum Nachdenken und Beten.",
       "Feiertag nur in Sachsen; in Bayern kein Unterricht."]
contra = ["Evangelischer Gedenktag für die Verstorbenen.",
          "Weihnachtsmärkte in Köln bleiben geschlossen; danach beginnt die Adventszeit."]
pyy = 1232
for t in pro:
    pyy2 = p.para(sx + 24, pyy + 20, "· " + t, 20.5, "serif", False, INK, (swd - 72) // 2, 1.4)
    pyy = max(pyy, pyy2) + 8
pyy = 1232
for t in contra:
    pyy2 = p.para(sx + 24 + (swd - 48) // 2, pyy + 20, "· " + t, 20.5, "serif", False, INK, (swd - 72) // 2, 1.4)
    pyy = max(pyy, pyy2) + 8

# ---- practice chart (full width) ----
cy = 1420
p.hline(MX, RIGHT, cy - 12, OLIVE, 2)
p.text(MX, cy + 28, "WAS INTERESSIERT DIE LESER?　读者最关心什么？", 26, "sans", True, OLIVE)
bars = [("Bundesliga und Nations League", 44, "足球"),
        ("Weihnachtsmärkte", 33, "市场"),
        ("Stille Tage", 23, "安静")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 360, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 17, 30, fill=OLIVE)
    p.text(MX + 470 + v * 17 + 16, byy + 26, f"{v} %", 22, "sans", True, OLIVE)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN　练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1752
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　第 6 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P6-ex")
e.head("A　DAS DIAGRAMM LESEN", 25, gap=6)
e.bridge("看上面的练习图表，选出正确答案。", gap=6)
e.ex("B1", "单选", "A", "44% 足球最受关注",
     "Was interessiert die Leser am meisten (Übungsdaten)? A. Bundesliga und Nations League · B. Weihnachtsmärkte · C. Stille Tage", size=22, gap=6)
e.ex("B1", "单选", "B", "市场 33% 第二",
     "Was ist die zweitgrößte Gruppe? A. Stille Tage · B. Weihnachtsmärkte · C. Bundesliga", size=22, gap=6)
e.ex("B1", "单选", "B", "44+33=77",
     "Fußball und Märkte zusammen sind... A. 67 % · B. 77 % · C. 100 %", size=22, gap=6)
e.ex("B2", "单选", "B", "安静 23% 最小",
     "Welche Gruppe ist kleiner? A. Märkte · B. Stille Tage · C. beide gleich", size=22, gap=6)
e.ex("B1", "单选", "A", "安静 23%",
     "Wie viele Prozent interessieren sich für die stillen Tage? A. 23 % · B. 33 % · C. 44 %", size=22, gap=6)
e.ex("B2", "单选", "B", "44+33+23=100",
     "Die drei Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=22, gap=6)
e.head("B　LESEVERSTEHEN (B2)", 25, gap=6)
e.bridge("读第 6 版深读文章，选出正确答案。", gap=6)
e.ex("B2", "单选", "B", "忏悔祈祷日 11 月 18 日",
     "Wann ist Buß- und Bettag? A. 11. November · B. 18. November · C. 22. November", size=22, gap=6)
e.ex("B2", "单选", "A", "亡灵主日是教会年最后一个周日",
     "Was ist der Totensonntag? A. der letzte Sonntag des Kirchenjahres · B. der erste Advent · C. ein Feiertag in ganz Deutschland", size=22, gap=6)
e.ex("B2", "单选", "B", "家庭电力税 2.05 欧分",
     "Wie hoch ist die Stromsteuer für Haushalte? A. 0,05 Cent · B. 2,05 Cent · C. 3,05 Cent", size=22, gap=6)
e.ex("B1", "单选", "B", "2027 年预算 11 月 27 日表决",
     "Wann soll der Bundeshaushalt 2027 verabschiedet werden? A. am 18. November · B. am 27. November · C. am 22. November", size=22, gap=6)
e.head("C　GRAMMATIK", 25, gap=6)
e.bridge("用括号里的形式填空。", gap=6)
e.ex("B2", "完成句子", "wird", "被动：wird + Partizip II",
     "Der Bundeshaushalt ___ (werden) am 27. November verabschiedet.", instr="填空", size=22, gap=6)
e.ex("B2", "完成句子", "ob", "ob 引导间接疑问句",
     "Niemand weiß, ___ die Einigung gelingt.", instr="填空", size=22, gap=6)
e.ex("B1", "完成句子", "geht", "gehen → geht",
     "Die Debatte ___ (gehen) weiter.", instr="填空", size=22, gap=6)
e.ex("B2", "完成句子", "beginnt", "beginnen → beginnt",
     "Mit dem ersten Advent ___ (beginnen) ein neues Kirchenjahr.", instr="填空", size=22, gap=6)
e.head("D　WÖRTER DER DEBATTE", 25, gap=6)
e.bridge("用方框里的词填空。", gap=6)
e.para("Buße · Kirchenjahr · Friedhof · Einigung", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "Buße", "忏悔",
     "Der Buß- und Bettag lädt zur ___ ein.", instr="填空", size=22, gap=6)
e.ex("B2", "完成句子", "Kirchenjahr", "教会年",
     "Der Totensonntag ist der letzte Sonntag des ___s.", instr="填空", size=22, gap=6)
e.ex("B2", "完成句子", "Friedhof", "墓地",
     "Die Menschen gehen auf den ___ und zünden Kerzen an.", instr="填空", size=22, gap=6)
e.ex("B1", "完成句子", "Einigung", "达成一致",
     "Ob eine ___ gelingt, ist offen.", instr="填空", size=22, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
