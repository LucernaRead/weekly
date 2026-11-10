# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("KULTUR　문화", "Die Lucerna", "A2 → B1　Ferienwechsel & Herbst　방학 교체와 가을")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Ferienwechsel: Die einen kommen, die anderen gehen", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: A2 → B1")
f.para("In dieser Woche wechseln die Ferien: In Baden-Württemberg ist die Schule schon wieder losgegangen — die Herbstferien dort sind vorbei. In Bayern dagegen haben die Schülerinnen und Schüler noch frei: Dort dauern die Herbstferien in dieser Woche noch an.")
f.para("Was macht man im November? Der Herbst zeigt seine ruhige Seite: Man liest, man kocht Kürbissuppe, man geht spazieren — und man plant schon den Advent. Die Tage sind kurz, die Abende lang. Viele Familien nutzen die freie Zeit für Ausflüge in die Berge oder an einen See — bevor der Winter kommt.")
f.para("Rückblick: Am Samstag, dem 31. Oktober, war Halloween — und zugleich Reformationstag in neun Bundesländern. Ebenfalls am 31. Oktober spielte Bayern in Dortmund — der Klassiker. Einen Tag später, am Sonntag, dem 1. November, war Allerheiligen: ein Feiertag in Baden-Württemberg, Bayern, Nordrhein-Westfalen, Rheinland-Pfalz und dem Saarland. Die Geschäfte blieben geschlossen, viele Menschen besuchten die Gräber ihrer Angehörigen.")
f.para("Und die Kultur? Die Museen und Theater spielen ihr Herbstprogramm. Ein Tipp der Redaktion: Gehen Sie an einem grauen Nachmittag ins Museum — dort ist es warm, ruhig und hell. Und wer ein Buch sucht: Die Bibliotheken haben im November oft Lesungen und Büchertische zum Herbst.")
f.para("Auch der Fußball gehört zum Herbst: Am Samstag und Sonntag spielt die Bundesliga — für viele Familien der Ausflug des Wochenendes. Mehr dazu auf Seite 4.")
f.para("Für Kinder gibt es in dieser Woche noch ein Highlight: Die Laternen für St. Martin werden schon gebastelt — der 11. November kommt bald. Mehr dazu in der nächsten Ausgabe.")
f.gloss("der Ferienwechsel 방학 교체 · die Schülerin 여학생 · der Ausflug 짧은 여행 · der Advent 대림절 · die Lesung 낭독회.")
f.end_report()

# col 3: facts + vocab + Und Sie + Tipp (hand-rolled; CORRECTED height formula — see KIT §geometry)
ix = COLX[3]
facts = ["Baden-Württemberg ist seit Montag, dem 2. November, wieder in der Schule.",
         "Bayern hat in dieser Woche noch Herbstferien — als einziges Bundesland.",
         "Allerheiligen am 1. November ist ein stiller Feiertag: Die Geschäfte bleiben zu."]
sy3 = 200
sh = 45 + 33 * len(facts) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in facts)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "FERIENWECHSEL　방학 교체", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 facts ends", sy3 + sh)
words = ["der Nebel — 안개", "das Laub — 낙엽", "der Kürbis — 호박",
         "die Kerze — 양초", "der Spaziergang — 산책", "die Lesung — 낭독회"]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(words) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in words)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "HERBSTWÖRTER　가을 단어", 24, "sans", True, OLIVE)
yy3 += 52
for t in words:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 vocab ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Lesen Sie im Herbst mehr als im Sommer? Welches Buch liegt gerade auf Ihrem Nachttisch? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("가을에는 여름보다 더 읽나요? 침대 옆에는 무슨 책이 있나요? 독일어로 두 문장 보내 주세요.", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "가을에는 여름보다 더 읽나요? 침대 옆에는 무슨 책이 있나요? 독일어로 두 문장 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 undsie ends", ey3 + eh)
tipp = "Tipp: An einem grauen Nachmittag ins Museum — dort ist es warm."
sy3 = ey3 + eh + 26
sh = 45 + 33 + 30.53 * len(wrap(tipp, "serif", False, 21.5, CW - 44))
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DER TIPP　편집부 제안", 24, "sans", True, OLIVE)
yy3 += 52
p.para(ix + 22, yy3 + 21, tipp, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　3면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　번호로 정답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　RICHTIG ODER FALSCH?", 25)
e.expl("3면 기사를 읽고 맞는지 틀리는지 판단하세요.")
e.ex("A2", "참/거짓 판단", "Richtig", "바덴뷔르템베르크는 월요일부터 다시 개학해요",
     "In Baden-Württemberg sind die Herbstferien vorbei. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("A2", "참/거짓 판단", "Falsch", "이번 주도 바이에른은 방학 중이에요",
     "Bayern hat in dieser Woche keine Ferien mehr. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("A2", "참/거짓 판단", "Richtig", "모든 성인의 날 11월 1일",
     "Allerheiligen ist am 1. November. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Falsch", "10월 31일은 종교개혁기념일이기도 해요(9개 주)",
     "Am 31. Oktober war nur Halloween, kein Feiertag. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("A2", "참/거짓 판단", "Falsch", "모든 성인의 날에는 상점이 문을 닫아요",
     "Die Geschäfte sind an Allerheiligen geöffnet. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.expl("네모 안의 단어로 빈칸을 채우세요.")
e.para("Ferienwechsel · Ausflug · Lesung · Advent · Nebel", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장 완성", "Ferienwechsel", "방학 교체",
     "In dieser Woche ist ___: Die einen kommen, die anderen gehen.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Ausflug", "산으로 짧은 여행을 가요",
     "Viele Familien machen einen ___ in die Berge.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Lesung", "도서관의 낭독회",
     "In der Bibliothek gibt es eine ___ zum Herbst.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Advent", "대림절은 11월에 계획해요",
     "Im November plant man schon den ___.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Nebel", "호수 위의 안개",
     "Am Morgen liegt ___ über dem See.", instr="빈칸", size=20, gap=8)
e.head("C　LESEVERSTEHEN", 25)
e.expl("정답을 고르세요.")
e.ex("A2", "객관식", "B", "이번 주 바덴뷔르템베르크는 방학이 끝났어요",
     "Wo sind die Ferien schon vorbei? A. in Bayern · B. in Baden-Württemberg · C. in Berlin", size=20, gap=8)
e.ex("A2", "객관식", "B", "조용한 공휴일이에요",
     "Was ist Allerheiligen? A. ein lautes Fest · B. ein stiller Feiertag · C. ein Schultag", size=20, gap=8)
e.ex("A2", "객관식", "A", "모든 성인의 날에는 묘지를 찾아가요",
     "Was machen viele an Allerheiligen? A. Sie besuchen Gräber. · B. Sie gehen in die Schule. · C. Sie kaufen Kostüme.", size=20, gap=8)
e.ex("B1", "객관식", "A", "낮이 짧아서 밤이 길어요",
     "Warum sind die Abende lang? A. Die Tage sind kurz. · B. Die Uhren gehen vor. · C. Die Ferien sind lang.", size=20, gap=8)
e.head("D　SÄTZE BAUEN", 25)
e.expl("단어를 모아 올바른 문장을 만드세요.")
e.ex("A2", "문장 만들기", "In Baden-Württemberg ist die Schule wieder losgegangen.", "시간·장소가 앞에 오고 동사는 두 번째 자리에 와요",
     "in Baden-Württemberg / ist / die Schule / wieder losgegangen → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 만들기", "Bayern hat in dieser Woche noch Ferien.", "시간 부사구가 앞에 오고 동사는 두 번째 자리에 와요",
     "Bayern / hat / in dieser Woche / noch Ferien → ___", instr="문장 만들기", size=20, gap=8)
e.ex("A2", "문장 만들기", "Viele Familien machen einen Ausflug in die Berge.", "주어·동사·목적어 순서예요",
     "viele Familien / machen / einen Ausflug / in die Berge → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 만들기", "An Allerheiligen bleiben die Geschäfte geschlossen.", "bleiben + geschlossen",
     "an Allerheiligen / bleiben / die Geschäfte / geschlossen → ___", instr="문장 만들기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "Die Lucerna", "LEVEL B1　Europapokal & Bundesliga　유럽 대항전과 분데스리가")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Englische Woche: Vier Nächte, dann der Spieltag", 32)
f.byline("Von der Lucerna-Sportredaktion　Leseniveau: B1")
f.para("Was für eine Fußballwoche! Am Dienstag und Mittwoch spielt die Champions League, am Donnerstag die Europa League — und am Freitag beginnt schon der 9. Spieltag der Bundesliga. Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.")
f.para("Am Dienstagabend wird es ernst: Bayern München spielt um 21.00 Uhr bei Atlético Madrid. Schon um 18.45 Uhr spielt der VfB Stuttgart bei Galatasaray in Istanbul. Zwei schwere Auswärtsspiele für die deutschen Teams.")
f.para("Am Mittwochabend (21.00 Uhr) geht es weiter: Borussia Dortmund empfängt Real Betis Sevilla, und RB Leipzig spielt gegen Manchester City. Für Leipzig ist es das schwerste Spiel der Woche: City ist der Favorit — aber zu Hause ist alles möglich.")
f.para("Am Donnerstagabend (18.45 Uhr) spielt die TSG Hoffenheim in der Europa League bei Crystal Palace in London. Auch Bayer Leverkusen ist in Europa dabei: Die Werkself spielt um 21.00 Uhr gegen Marseille.")
f.para("Und dann die Bundesliga: Am Freitag (20.30 Uhr) eröffnen Hamburg und Mönchengladbach den 9. Spieltag. Am Samstag folgen fünf Spiele, das Topspiel ist Stuttgart gegen Bremen (18.30 Uhr). Am Sonntag: Köln–Leverkusen (15.30 Uhr), Freiburg–Union Berlin (17.30 Uhr) und Hoffenheim–Schalke (19.30 Uhr).")
f.para("Merken Sie sich auch den nächsten Sonntag: Am 15. November spielt die NFL in München — American Football in der Allianz Arena! Mehr dazu in der nächsten Ausgabe.")
f.gloss("die Englische Woche 주중과 주말 연속 경기 · auswärts 원정 · empfangen 홈에서 맞기 · der Favorit 우승 후보 · eröffnen 개막하기.")
f.end_report()

# col 3: kopfball image + Und Sie
bx = COLX[3]
image(p, "kopfball.jpg", bx, 200, CW, 470)
cy3 = caption(p, bx, 670, CW, "Kopfball im Spiel: So sieht ein Duell in der Luft aus — um jeden Ball wird gekämpft.",
              "Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain")
ey3 = cy3 + 26
etvous = "Und Sie? Für wen sind Sie in dieser Woche — Bayern, Dortmund, Leipzig oder Stuttgart? Und wer gewinnt am Samstag das Topspiel? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("이번 주 응원 팀은 어디예요? 토요일 빅매치 승자는 누구예요? 독일어로 두 문장 보내 주세요.", "sans", False, 20, CW - 44)) - 1)
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "UND SIE?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "이번 주 응원 팀은 어디예요? 토요일 빅매치 승자는 누구예요? 독일어로 두 문장 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "DER 9. SPIELTAG　9라운드 일정", 26, "sans", True, OLIVE)
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
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Alle Zeiten in MEZ (Mitteleuropäische Zeit). Die Europa-Spiele: Dienstag bis Donnerstag, die Liga: Freitag bis Sonntag. Die Hertha-Zeile ist 2. Bundesliga."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1640
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　4면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　번호로 정답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　LESEVERSTEHEN", 25)
e.expl("4면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "바이에른은 화요일에 아틀레티코 원정 경기를 해요",
     "Bayern spielt am Dienstag... A. zu Hause gegen Atlético · B. bei Atlético Madrid · C. bei Galatasaray", size=20, gap=8)
e.ex("B1", "객관식", "B", "슈투트가르트는 18:45에 시작해요",
     "Stuttgart spielt am Dienstag um... A. 21.00 Uhr · B. 18.45 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.ex("B1", "객관식", "C", "도르트문트가 베티스를 홈에서 맞아요",
     "Dortmund empfängt am Mittwoch... A. Manchester City · B. Marseille · C. Real Betis Sevilla", size=20, gap=8)
e.ex("B1", "객관식", "A", "유로파리그에서 호펜하임은 크리스털 팰리스 원정을 가요",
     "Hoffenheim spielt in der Europa League bei... A. Crystal Palace · B. Galatasaray · C. Real Betis", size=20, gap=8)
e.ex("B1", "객관식", "B", "토요일 빅매치: 슈투트가르트–브레멘전",
     "Das Topspiel am Samstag ist... A. Hamburg–Gladbach · B. Stuttgart–Bremen · C. Köln–Leverkusen", size=20, gap=8)
e.head("B　DIE WÖRTER", 25)
e.match_set("B1", "단어 짝짓기",
            ["die Englische Woche", "auswärts", "der Favorit", "eröffnen"],
            ["eine Woche mit Spielen unter der Woche und am Wochenende",
             "nicht zu Hause, sondern beim Gegner",
             "das Team, das wahrscheinlich gewinnt",
             "den Anfang machen, ein Spiel beginnen"],
            ["a", "b", "c", "d"],
            ["Englische Woche=주중과 주말 연속 경기 a", "auswärts=원정 b", "Favorit=유력 후보 c", "eröffnen=막을 열기 d"],
            instr="단어와 뜻 짝짓기")
e.head("C　KOMPARATIV", 25)
e.expl("비교급으로 문장을 완성하세요(괄호 안은 원급).")
e.ex("B1", "문장 완성", "schwerer", "schwer → schwerer",
     "Für Leipzig wird der Abend gegen City ___ (schwer) als normal.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "später", "spät → später(19:30이 가장 늦어요)",
     "Das Sonntagsspiel Hoffenheim–Schalke beginnt ___ (spät) als die anderen.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "mehr", "viel → mehr(팬들은 더 많은 골을 보고 싶어 해요)",
     "Die Fans wollen ___ (viel) Tore sehen.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "früher", "früh → früher(18:45는 21:00보다 일러요)",
     "Stuttgart spielt schon um 18.45 Uhr — ___ (früh) als das Bayern-Spiel.", instr="빈칸", size=20, gap=8)
e.head("D　DIE UHRZEITEN", 25)
e.expl("위 일정표를 보고 정답을 고르세요.")
e.ex("B1", "객관식", "A", "금요일 20:30에 함부르크–묀헨글라트바흐전이 시작해요",
     "Das Spiel Hamburg–Gladbach beginnt um... A. 20.30 Uhr · B. 18.30 Uhr · C. 15.30 Uhr", size=20, gap=8)
e.ex("B1", "객관식", "B", "슈투트가르트–브레멘전은 토요일 18:30에 열려요",
     "Stuttgart–Bremen ist das Topspiel am Samstag um... A. 15.30 Uhr · B. 18.30 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.ex("B1", "객관식", "C", "호펜하임–샬케전은 일요일 19:30에 시작해요",
     "Hoffenheim–Schalke beginnt am Sonntag um... A. 15.30 Uhr · B. 17.30 Uhr · C. 19.30 Uhr", size=20, gap=8)
e.ex("B1", "객관식", "A", "일요일 17:30 프라이부르크–우니온전",
     "Freiburg–Union beginnt um... A. 17.30 Uhr · B. 19.30 Uhr · C. 15.30 Uhr", size=20, gap=8)
e.ex("B1", "객관식", "B", "목요일 유로파리그 호펜하임전 18:45예요",
     "Die Europa League am Donnerstag: Hoffenheim spielt um... A. 21.00 Uhr · B. 18.45 Uhr · C. 20.30 Uhr", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
