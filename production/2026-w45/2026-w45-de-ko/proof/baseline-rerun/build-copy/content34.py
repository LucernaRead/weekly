# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/de-ko-proof/baseline-rerun/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("KULTUR · 文化", "Die Lucerna", "A2 → B1 · Ferienwechsel & Herbst · 假期交接与秋天")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Ferienwechsel: Die einen kommen, die anderen gehen", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: A2 → B1")
f.para("In dieser Woche wechseln die Ferien: In Baden-Württemberg ist die Schule schon wieder losgegangen — die Herbstferien dort sind vorbei. In Bayern dagegen haben die Schülerinnen und Schüler noch frei: Dort dauern die Herbstferien in dieser Woche noch an.")
f.para("Was macht man im November? Der Herbst zeigt seine ruhige Seite: Man liest, man kocht Kürbissuppe, man geht spazieren — und man plant schon den Advent. Die Tage sind kurz, die Abende lang. Viele Familien nutzen die freie Zeit für Ausflüge in die Berge oder an einen See — bevor der Winter kommt.")
f.para("Rückblick: Am Samstag, dem 31. Oktober, war Halloween — und zugleich Reformationstag in neun Bundesländern. Ebenfalls am 31. Oktober spielte Bayern in Dortmund — der Klassiker. Einen Tag später, am Sonntag, dem 1. November, war Allerheiligen: ein Feiertag in Baden-Württemberg, Bayern, Nordrhein-Westfalen, Rheinland-Pfalz und dem Saarland. Die Geschäfte blieben geschlossen, viele Menschen besuchten die Gräber ihrer Angehörigen.")
f.para("Und die Kultur? Die Museen und Theater spielen ihr Herbstprogramm. Ein Tipp der Redaktion: Gehen Sie an einem grauen Nachmittag ins Museum — dort ist es warm, ruhig und hell. Und wer ein Buch sucht: Die Bibliotheken haben im November oft Lesungen und Büchertische zum Herbst.")
f.para("Auch der Fußball gehört zum Herbst: Am Samstag und Sonntag spielt die Bundesliga — für viele Familien der Ausflug des Wochenendes. Mehr dazu auf Seite 4.")
f.para("Für Kinder gibt es in dieser Woche noch ein Highlight: Die Laternen für St. Martin werden schon gebastelt — der 11. November kommt bald. Mehr dazu in der nächsten Ausgabe.")
f.gloss("der Ferienwechsel 假期交接 · die Schülerin 女学生 · der Ausflug 短途出游 · der Advent 将临期 · die Lesung 朗读会。")
f.end_report()

# col 3: facts + vocab + Und Sie + Tipp (hand-rolled; CORRECTED height formula — see KIT §geometry)
ix = COLX[3]
facts = ["Baden-Württemberg ist seit Montag, dem 2. November, wieder in der Schule.",
         "Bayern hat in dieser Woche noch Herbstferien — als einziges Bundesland.",
         "Allerheiligen am 1. November ist ein stiller Feiertag: Die Geschäfte bleiben zu."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "FERIENWECHSEL · 假期交接", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 facts ends", sy3 + sh)
words = ["der Nebel — 雾", "das Laub — 落叶", "der Kürbis — 南瓜",
         "die Kerze — 蜡烛", "der Spaziergang — 散步", "die Lesung — 朗读会"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "HERBSTWÖRTER · 秋天词汇", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Lesen Sie im Herbst mehr als im Sommer? Welches Buch liegt gerade auf Ihrem Nachttisch? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("秋天你比夏天读得多吗？你的床头现在放着哪本书？写两句德语寄来。", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "秋天你比夏天读得多吗？你的床头现在放着哪本书？写两句德语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 undsie ends", ey3 + eh)
tipp = "Tipp: An einem grauen Nachmittag ins Museum — dort ist es warm."
sy3 = ey3 + eh + 26
sh = 45 + 33 + 30.53 * len(wrap(tipp, "serif", False, 21.5, CW - 44))
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DER TIPP · 编辑部建议", 24, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, tipp, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 第 3 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · RICHTIG ODER FALSCH?", 25)
e.bridge("读第 3 版文章，判断对错。")
e.ex("A2", "判断对错", "Richtig", "BW 周一起复课",
     "In Baden-Württemberg sind die Herbstferien vorbei. Richtig oder falsch?", instr="判断", size=20, gap=8)
e.ex("A2", "判断对错", "Falsch", "巴伐利亚本周仍在放假",
     "Bayern hat in dieser Woche keine Ferien mehr. Richtig oder falsch?", instr="判断", size=20, gap=8)
e.ex("A2", "判断对错", "Richtig", "诸圣节 11 月 1 日",
     "Allerheiligen ist am 1. November. Richtig oder falsch?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Falsch", "10 月 31 日也是宗教改革日（九个州）",
     "Am 31. Oktober war nur Halloween, kein Feiertag. Richtig oder falsch?", instr="判断", size=20, gap=8)
e.ex("A2", "判断对错", "Falsch", "诸圣节商店关门",
     "Die Geschäfte sind an Allerheiligen geöffnet. Richtig oder falsch?", instr="判断", size=20, gap=8)
e.head("B · WÖRTER AUS DEM TEXT", 25)
e.bridge("用方框里的词填空。")
e.para("Ferienwechsel · Ausflug · Lesung · Advent · Nebel", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "Ferienwechsel", "假期交接",
     "In dieser Woche ist ___: Die einen kommen, die anderen gehen.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Ausflug", "去山区短途出游",
     "Viele Familien machen einen ___ in die Berge.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Lesung", "图书馆的朗读会",
     "In der Bibliothek gibt es eine ___ zum Herbst.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Advent", "将临期在 11 月筹划",
     "Im November plant man schon den ___.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "Nebel", "湖面上的雾",
     "Am Morgen liegt ___ über dem See.", instr="填空", size=20, gap=8)
e.head("C · LESEVERSTEHEN", 25)
e.bridge("选出正确答案。")
e.ex("A2", "单选", "B", "BW 假期已结束",
     "Wo sind die Ferien schon vorbei? A. in Bayern · B. in Baden-Württemberg · C. in Berlin", size=20, gap=8)
e.ex("A2", "单选", "B", "安静的节日",
     "Was ist Allerheiligen? A. ein lautes Fest · B. ein stiller Feiertag · C. ein Schultag", size=20, gap=8)
e.ex("A2", "单选", "A", "诸圣节扫墓",
     "Was machen viele an Allerheiligen? A. Sie besuchen Gräber. · B. Sie gehen in die Schule. · C. Sie kaufen Kostüme.", size=20, gap=8)
e.ex("B1", "单选", "A", "白天短所以夜晚长",
     "Warum sind die Abende lang? A. Die Tage sind kurz. · B. Die Uhren gehen vor. · C. Die Ferien sind lang.", size=20, gap=8)
e.head("D · SÄTZE BAUEN", 25)
e.bridge("把词组成正确的句子。")
e.ex("A2", "造句", "In Baden-Württemberg ist die Schule wieder losgegangen.", "时间地点开头，动词第二位",
     "in Baden-Württemberg / ist / die Schule / wieder losgegangen → ___", instr="造句", size=20, gap=8)
e.ex("B1", "造句", "Bayern hat in dieser Woche noch Ferien.", "数量时间状语，动词第二位",
     "Bayern / hat / in dieser Woche / noch Ferien → ___", instr="造句", size=20, gap=8)
e.ex("A2", "造句", "Viele Familien machen einen Ausflug in die Berge.", "主谓宾顺序",
     "viele Familien / machen / einen Ausflug / in die Berge → ___", instr="造句", size=20, gap=8)
e.ex("B1", "造句", "An Allerheiligen bleiben die Geschäfte geschlossen.", "bleiben + geschlossen",
     "an Allerheiligen / bleiben / die Geschäfte / geschlossen → ___", instr="造句", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · 体育", "Die Lucerna", "LEVEL B1 · Europapokal & Bundesliga · 欧战与德甲")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Englische Woche: Vier Nächte, dann der Spieltag", 37)
f.byline("Von der Lucerna-Sportredaktion · Leseniveau: B1")
f.para("Was für eine Fußballwoche! Am Dienstag und Mittwoch spielt die Champions League, am Donnerstag die Europa League — und am Freitag beginnt schon der 9. Spieltag der Bundesliga. Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.")
f.para("Am Dienstagabend wird es ernst: Bayern München spielt um 21.00 Uhr bei Atlético Madrid. Schon um 18.45 Uhr spielt der VfB Stuttgart bei Galatasaray in Istanbul. Zwei schwere Auswärtsspiele für die deutschen Teams.")
f.para("Am Mittwochabend (21.00 Uhr) geht es weiter: Borussia Dortmund empfängt Real Betis Sevilla, und RB Leipzig spielt gegen Manchester City. Für Leipzig ist es das schwerste Spiel der Woche: City ist der Favorit — aber zu Hause ist alles möglich.")
f.para("Am Donnerstagabend (18.45 Uhr) spielt die TSG Hoffenheim in der Europa League bei Crystal Palace in London. Auch Bayer Leverkusen ist in Europa dabei: Die Werkself spielt um 21.00 Uhr gegen Marseille.")
f.para("Und dann die Bundesliga: Am Freitag (20.30 Uhr) eröffnen Hamburg und Mönchengladbach den 9. Spieltag. Am Samstag folgen fünf Spiele, das Topspiel ist Stuttgart gegen Bremen (18.30 Uhr). Am Sonntag: Köln–Leverkusen (15.30 Uhr), Freiburg–Union Berlin (17.30 Uhr) und Hoffenheim–Schalke (19.30 Uhr).")
f.para("Merken Sie sich auch den nächsten Sonntag: Am 15. November spielt die NFL in München — American Football in der Allianz Arena! Mehr dazu in der nächsten Ausgabe.")
f.gloss("die Englische Woche 一周双赛 · auswärts 客场 · empfangen 主场迎战 · der Favorit 夺冠热门 · eröffnen 揭开序幕。")
f.end_report()

# col 3: kopfball image + Und Sie
bx = COLX[3]
image(p, "kopfball.jpg", bx, 200, CW, 470)
cy3 = caption(p, bx, 670, CW, "Kopfball im Spiel: So sieht ein Duell in der Luft aus — um jeden Ball wird gekämpft.",
              "Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain")
ey3 = cy3 + 26
etvous = "Und Sie? Für wen sind Sie in dieser Woche — Bayern, Dortmund, Leipzig oder Stuttgart? Und wer gewinnt am Samstag das Topspiel? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("本周你支持谁？周六焦点战谁赢？写两句德语寄给编辑部。", "sans", False, 20, CW - 44)) - 1)
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "UND SIE? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "本周你支持谁？周六焦点战谁赢？写两句德语寄给编辑部。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "DER 9. SPIELTAG · 第 9 轮赛程", 26, "sans", True, OLIVE)
rows = [
    ("Fr 6.11.", "20.30", "Hamburger SV – Borussia Mönchengladbach"),
    ("Sa 7.11.", "15.30", "Borussia Dortmund – SV Elversberg · SC Paderborn 07 – Eintracht Frankfurt"),
    ("Sa 7.11.", "15.30", "1. FSV Mainz 05 – FC Bayern München · RB Leipzig – FC Augsburg"),
    ("Sa 7.11.", "18.30", "VfB Stuttgart – Werder Bremen (Topspiel)"),
    ("Sa 7.11.", "20.30", "Hertha BSC – VfL Wolfsburg (2. Bundesliga)"),
    ("So 8.11.", "15.30", "1. FC Köln – Bayer 04 Leverkusen"),
    ("So 8.11.", "17.30", "SC Freiburg – 1. FC Union Berlin"),
    ("So 8.11.", "19.30", "TSG Hoffenheim – FC Schalke 04"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Alle Zeiten in MEZ (Mitteleuropäische Zeit). Die Europa-Spiele: Dienstag bis Donnerstag, die Liga: Freitag bis Sonntag. Die Hertha-Zeile ist 2. Bundesliga."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1640
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 第 4 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · LESEVERSTEHEN", 25)
e.bridge("读第 4 版文章，选出正确答案。")
e.ex("B1", "单选", "B", "拜仁周二客战马竞",
     "Bayern spielt am Dienstag... A. zu Hause gegen Atlético · B. bei Atlético Madrid · C. bei Galatasaray", size=20, gap=8)
e.ex("B1", "单选", "B", "斯图加特 18:45 开球",
     "Stuttgart spielt am Dienstag um... A. 21.00 Uhr · B. 18.45 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.ex("B1", "单选", "C", "多特主场迎战贝蒂斯",
     "Dortmund empfängt am Mittwoch... A. Manchester City · B. Marseille · C. Real Betis Sevilla", size=20, gap=8)
e.ex("B1", "单选", "A", "霍芬海姆欧联客战水晶宫",
     "Hoffenheim spielt in der Europa League bei... A. Crystal Palace · B. Galatasaray · C. Real Betis", size=20, gap=8)
e.ex("B1", "单选", "B", "周六焦点战斯图加特–不来梅",
     "Das Topspiel am Samstag ist... A. Hamburg–Gladbach · B. Stuttgart–Bremen · C. Köln–Leverkusen", size=20, gap=8)
e.head("B · DIE WÖRTER", 25)
e.match_set("B1", "词汇配对",
            ["die Englische Woche", "auswärts", "der Favorit", "eröffnen"],
            ["eine Woche mit Spielen unter der Woche und am Wochenende",
             "nicht zu Hause, sondern beim Gegner",
             "das Team, das wahrscheinlich gewinnt",
             "den Anfang machen, ein Spiel beginnen"],
            ["a", "b", "c", "d"],
            ["Englische Woche=一周双赛 a", "auswärts=客场 b", "Favorit=热门 c", "eröffnen=揭开序幕 d"],
            instr="把词和释义配对")
e.head("C · KOMPARATIV", 25)
e.bridge("用比较级完成句子（括号里是原级）。")
e.ex("B1", "完成句子", "schwerer", "schwer → schwerer",
     "Für Leipzig wird der Abend gegen City ___ (schwer) als normal.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "später", "spät → später（19:30 最晚）",
     "Das Sonntagsspiel Hoffenheim–Schalke beginnt ___ (spät) als die anderen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "mehr", "viel → mehr（球迷想要更多）",
     "Die Fans wollen ___ (viel) Tore sehen.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "früher", "früh → früher（18:45 早于 21:00）",
     "Stuttgart spielt schon um 18.45 Uhr — ___ (früh) als das Bayern-Spiel.", instr="填空", size=20, gap=8)
e.head("D · DIE UHRZEITEN", 25)
e.bridge("看上面的赛程表，选出正确答案。")
e.ex("B1", "单选", "A", "汉堡–门兴周五 20:30",
     "Das Spiel Hamburg–Gladbach beginnt um... A. 20.30 Uhr · B. 18.30 Uhr · C. 15.30 Uhr", size=20, gap=8)
e.ex("B1", "单选", "B", "斯图加特–不来梅周六 18:30",
     "Stuttgart–Bremen ist das Topspiel am Samstag um... A. 15.30 Uhr · B. 18.30 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.ex("B1", "单选", "C", "霍芬海姆–沙尔克周日 19:30",
     "Hoffenheim–Schalke beginnt am Sonntag um... A. 15.30 Uhr · B. 17.30 Uhr · C. 19.30 Uhr", size=20, gap=8)
e.ex("B1", "单选", "A", "弗赖堡–柏林联周日 17:30",
     "Freiburg–Union beginnt um... A. 17.30 Uhr · B. 19.30 Uhr · C. 15.30 Uhr", size=20, gap=8)
e.ex("B1", "单选", "B", "欧联周四霍芬海姆 18:45",
     "Die Europa League am Donnerstag: Hoffenheim spielt um... A. 21.00 Uhr · B. 18.45 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
