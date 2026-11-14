# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("KULTUR　문화", "Die Lucerna", "A2 → B1　Zwei Feste an einem Tag　같은 날 두 축제")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Zwei Feste an einem Tag: Halloween trifft den Reformationstag", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: A2 → B1")
f.para("Am Samstag, dem 31. Oktober, ist in Deutschland viel los: Zwei Feste fallen auf denselben Tag. Die Kinder feiern Halloween — und neun Bundesländer haben einen Feiertag: den Reformationstag.")
f.para("Was ist Halloween? Kinder ziehen Kostüme an und gehen am Abend von Haus zu Haus. Sie rufen: „Süßes oder Saures!“ und bekommen Süßigkeiten. In den Fenstern leuchten Kürbisse mit Gesichtern, und in vielen Straßen stehen Kerzen und kleine Lichter. Die Geschäfte sind schon bereit: Die Discounter verkaufen seit dem 12. Oktober Kostüme und Dekoration.")
f.para("Und der Reformationstag? An diesem Tag im Jahr 1517 soll Martin Luther seine 95 Thesen an die Tür der Schlosskirche in Wittenberg genagelt haben. Damit begann die Reformation — die Kirche teilte sich, und Europa veränderte sich. Heute ist der Tag ein gesetzlicher Feiertag in Brandenburg, Bremen, Hamburg, Mecklenburg-Vorpommern, Niedersachsen, Sachsen, Sachsen-Anhalt, Schleswig-Holstein und Thüringen.")
f.para("In diesem Jahr fällt der 31. Oktober auf einen Samstag — ein Extra-Freitag entsteht so nicht. Einen Tag später, am Sonntag, dem 1. November, ist Allerheiligen: ein Feiertag in Baden-Württemberg, Bayern, Nordrhein-Westfalen, Rheinland-Pfalz und dem Saarland. Dort bleiben die Geschäfte auch am Sonntag geschlossen — wie jeden Sonntag.")
f.para("Halloween im Zoo? In Osnabrück gibt es in diesem Jahr eine schöne Aktion: Wer vom 26. bis 29. Oktober einen geschnitzten Kürbis abgibt, bekommt für den 31. Oktober ein Freiticket für ein Kind. Die Kürbisse werden Dekoration rund um den Unterirdischen Zoo. Im Erlebnispark Funny-World in Kappel-Grafenhausen leuchten am 30. und 31. Oktober mehr als 600 Kürbisse.")
f.para("Zwei Feste, ein Tag — und eine Frage für unsere Leser: Feiern die Deutschen am 31. Oktober lieber leise oder lieber laut? Schreiben Sie uns! Die Redaktion sammelt die Antworten für die nächste Ausgabe.")
f.gloss("das Kostüm 의상 · der Kürbis 호박 · der Feiertag 공휴일 · die These 명제 · gesetzlich 법으로 정해진 · das Freiticket 무료표 · schnitzen 조각하다.")
f.end_report()

# col 3: Luther image + facts (sequential)
ix = COLX[3]
image(p, "luther.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "Martin Luther (1483–1546), gemalt von Lucas Cranach dem Älteren, 1528. Seine 95 Thesen von 1517 veränderten Europa.",
              "Gemälde: Lucas Cranach d. Ä., 1528 (Veste Coburg) — public domain")
facts = ["Der 31. Oktober ist in neun Bundesländern ein Feiertag — 2026 fällt er auf einen Samstag.",
         "Allerheiligen am 1. November ist ein stiller Feiertag: keine lauten Feste, die Geschäfte bleiben zu.",
         "Mehr als 600 geschnitzte Kürbisse leuchten in Funny-World (Kappel-Grafenhausen)."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 34  # D5 fix run2
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ZWEI FESTE, EIN TAG", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "Und Sie? Verkleiden Sie sich an Halloween? Oder ist der 31. Oktober für Sie ein ruhiger Tag? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("할로윈에 분장을 하나요? 아니면 조용히 보내는 날인가요? 독일어로 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "할로윈에 분장을 하나요? 아니면 조용히 보내는 날인가요? 독일어로 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　3면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　문제는 수준이 섞여 있어요　번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　RICHTIG ODER FALSCH?", 25)
e.expl("3면 기사를 읽고 맞는지 틀린지 판단하세요.")
e.ex("A2", "참/거짓 판단", "Richtig", "아홉 개 주에 종교개혁일 공휴일",
     "Der Reformationstag ist in neun Bundesländern ein Feiertag. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("A2", "참/거짓 판단", "Falsch", "Luther는 1517년, 1715년이 아니에요",
     "Martin Luther nagelte seine Thesen im Jahr 1715 an die Tür. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("A2", "참/거짓 판단", "Richtig", "10월 26–29일 호박을 내면 31일 어린이 무료표",
     "Im Zoo Osnabrück gibt es für einen Kürbis ein Freiticket für ein Kind. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Falsch", "올해 10월 31일은 토요일이라 평일 휴일이 생기지 않아요",
     "Der 31. Oktober gibt den Menschen in diesem Jahr einen freien Freitag. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("A2", "참/거짓 판단", "Richtig", "Funny-World에 호박 600개 넘게",
     "In Funny-World leuchten mehr als 600 Kürbisse. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.head("B　WÖRTER AUS DEM TEXT", 25)
e.expl("상자 속 단어로 빈칸을 채우세요.")
e.para("Kostüm · Kürbis · Feiertag · Süßes · Kerze", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "문장 완성", "Kostüm", "아이들은 Kostüm을 입어요",
     "Die Kinder ziehen ein ___ an und gehen von Haus zu Haus.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Kürbis", "호박등 Kürbis",
     "Im Fenster leuchtet ein ___ mit einem Gesicht.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Feiertag", "Feiertag = 공휴일",
     "Der Reformationstag ist ein gesetzlicher ___.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Süßes", "Süßes oder Saures!",
     "Die Kinder rufen an der Tür: „___ oder Saures!“", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Kerzen", "Kerzen (양초의 복수)",
     "In vielen Straßen stehen ___ und kleine Lichter.", instr="빈칸", size=20, gap=8)
e.head("C　LESEVERSTEHEN", 25)
e.expl("정답을 고르세요.")
e.ex("A2", "객관식", "B", "아이들은 저녁에 집집마다 다녀요",
     "Wann gehen die Kinder von Haus zu Haus? A. am Morgen · B. am Abend · C. in der Nacht um drei", size=20, gap=8)
e.ex("A2", "객관식", "A", "1517년 성 교회 문",
     "Luthers Thesen hingen 1517 an der Tür... A. der Schlosskirche · B. des Rathauses · C. der Schule", size=20, gap=8)
e.ex("B1", "객관식", "B", "모든 성인의 날은 11월 1일",
     "Allerheiligen ist am... A. 31. Oktober · B. 1. November · C. 2. November", size=20, gap=8)
e.ex("B1", "객관식", "B", "호박은 지하 동물원 둘레에 장식으로",
     "Wo stehen die Kürbisse dann im Zoo? A. Im Restaurant. · B. Rund um den Unterirdischen Zoo. · C. Am Eingang.", size=20, gap=8)
e.head("D　SÄTZE BAUEN", 25)
e.expl("단어를 바른 문장으로 만드세요.")
e.ex("A2", "문장 만들기", "Die Kinder rufen an der Tür: Süßes oder Saures!", "주어 + 동사는 두 번째 자리",
     "die Kinder / rufen / an der Tür / Süßes oder Saures → ___", instr="문장 만들기", size=20, gap=8)
e.ex("B1", "문장 만들기", "Neun Bundesländer haben am 31. Oktober einen Feiertag.", "수량사로 시작, 동사는 두 번째",
     "neun Bundesländer / haben / am 31. Oktober / einen Feiertag → ___", instr="문장 만들기", size=20, gap=8)
e.ex("A2", "문장 완성", "bekommen die Kinder Süßigkeiten", "bekommen = 사탕을 받다",
     "Die Kinder bekommen an Halloween Süßigkeiten. → An Halloween ___.", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 만들기", "Die Geschäfte bleiben am Sonntag geschlossen.", "bleiben + geschlossen",
     "die Geschäfte / bleiben / am Sonntag / geschlossen → ___", instr="문장 만들기", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-kultur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "Die Lucerna", "LEVEL B1　Champions League & Bundesliga　챔피언스리그와 분데스리가")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Königsklasse in der Woche der zwei Zeiten", 32)
f.byline("Von der Lucerna-Sportredaktion　Leseniveau: B1")
f.para("Was für eine Fußballwoche! Am Dienstag und Mittwoch spielt die Champions League ihren 3. Spieltag, am Freitag beginnt die Bundesliga — und am Sonntag wechselt mittendrin die Zeit: Die Liga spielt zum ersten Mal in dieser Saison in der Winterzeit.")
f.para("Der Dienstag brachte zwei deutsche Spiele. Borussia Dortmund gewann am Dienstagabend 2:1 bei Sabah FK in Baku. Der BVB nahm die drei Punkte mit nach Hause. Der VfB Stuttgart spielte zu Hause 1:1 gegen Atlético Madrid: Julián Álvarez machte den Ausgleich für die Spanier — ein Punkt für den VfB.")
f.para("Heute Abend (Anstoß 21.00 Uhr) wird es noch größer: Der FC Bayern empfängt den FC Arsenal, und RB Leipzig spielt bei Real Madrid. Für Leipzig ist es ein schwerer Abend: Am Wochenende verlor die Mannschaft in der Liga 1:6 bei den Bayern. In Madrid muss Leipzig mutiger spielen. Ob das gegen Real reicht? Die Antwort gibt es heute Nacht.")
f.para("Am Freitag um 20.30 Uhr beginnt der 7. Spieltag der Bundesliga: Stuttgart spielt gegen Mönchengladbach — noch in der Sommerzeit (MESZ). Am Samstag folgen fünf Spiele am Nachmittag; das Topspiel am Abend ist Borussia Dortmund gegen Eintracht Frankfurt um 18.30 Uhr. Und am Sonntag spielt die Liga dann in der neuen Zeit (MEZ): Hoffenheim gegen Leverkusen um 15.30 Uhr, Freiburg gegen die Bayern um 17.30 Uhr.")
f.para("Merken Sie sich auch den nächsten Samstag: Am 31. Oktober spielen die Bayern in Dortmund — der Klassiker! Mehr dazu in der nächsten Ausgabe.")
f.gloss("die Königsklasse 최상위 리그 (챔피언스리그의 별명) · der Spieltag 경기 라운드 · der Anstoß 킥오프 · der Ausgleich 동점골 · empfangen 홈에서 맞이하다 · mutig 용감한.")
f.end_report()

# col 3: Klassiker box + Und Sie (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 330, fill=BOX)
p.text(bx + 22, 240, "DER KLASSIKER RUFT", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Am Samstag, dem 31. Oktober, spielen die Bayern bei Borussia Dortmund — das größte Spiel der Hinrunde. Halloween, Feiertag und der Klassiker an einem Tag: Die nächste Ausgabe wird voll! (Seite 7)", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 556
etvous = "Und Sie? Für wen sind Sie am Wochenende — Bayern, Dortmund oder Leipzig? Und wer gewinnt den Klassiker am 31. Oktober? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("주말에 누구를 응원하나요? 데어 클라시커는 누가 이길까요? 독일어로 두 문장을 써서 편집부에 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "UND SIE?　여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "주말에 누구를 응원하나요? 데어 클라시커는 누가 이길까요? 독일어로 두 문장을 써서 편집부에 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "DER 7. SPIELTAG　7라운드 일정", 26, "sans", True, OLIVE)
rows = [
    ("Fr 23.10.", "20.30 (MESZ)", "VfB Stuttgart – Borussia Mönchengladbach"),
    ("Sa 24.10.", "18.30 (MESZ)", "Borussia Dortmund – Eintracht Frankfurt (Topspiel)"),
    ("Sa 24.10.", "nachmittags", "1. FC Köln – FC Schalke 04 · FC Augsburg – 1. FC Union Berlin"),
    ("Sa 24.10.", "nachmittags", "1. FSV Mainz 05 – Werder Bremen · RB Leipzig – SV Elversberg"),
    ("Sa 24.10.", "nachmittags", "SC Paderborn 07 – Hamburger SV"),
    ("So 25.10.", "15.30 (MEZ)", "TSG Hoffenheim – Bayer 04 Leverkusen"),
    ("So 25.10.", "17.30 (MEZ)", "SC Freiburg – FC Bayern München"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Achtung, Zeit-Fans: Am Freitag und Samstag gilt noch die Sommerzeit (MESZ), am Sonntag schon die Winterzeit (MEZ) — die Uhren wurden in der Nacht umgestellt."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　4면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에　문제는 수준이 섞여 있어요　번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　LESEVERSTEHEN", 25)
e.expl("4면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "A", "도르트문트 2:1 원정 승 (상대 Sabah)",
     "Dortmund spielte am Dienstag... A. 2:1 in Baku · B. 1:1 zu Hause · C. 0:2 in Madrid", size=20, gap=8)
e.ex("B1", "객관식", "B", "Álvarez가 아틀레티코 동점골",
     "Wer traf für Atlético zum Ausgleich? A. ein Stuttgarter · B. Julián Álvarez · C. ein Torwart", size=20, gap=8)
e.ex("B1", "객관식", "C", "라이프치히, 리그에서 바이에른에 1:6 패배",
     "Leipzig verlor am Wochenende... A. 0:1 · B. 2:2 · C. 1:6 bei den Bayern", size=20, gap=8)
e.ex("B1", "객관식", "A", "금요일 20:30 슈투트가르트–묀헨글라트바흐로 시작",
     "Der Spieltag beginnt am Freitag mit... A. Stuttgart–Gladbach · B. Dortmund–Frankfurt · C. Freiburg–Bayern", size=20, gap=8)
e.ex("B1", "객관식", "B", "일요일은 이미 표준시 MEZ",
     "Am Sonntag gilt schon die... A. Sommerzeit · B. Winterzeit · C. Frühlingszeit", size=20, gap=8)
e.head("B　DIE WÖRTER", 25)
e.match_set("B1", "단어 짝짓기",
            ["der Ausgleich", "der Spieltag", "der Anstoß", "die Königsklasse"],
            ["der Moment, in dem ein Spiel beginnt",
             "das Tor zum gleichen Stand, zum Beispiel 1:1",
             "ein Tag, an dem alle Teams spielen",
             "der Spitzname der Champions League"],
            ["b", "c", "a", "d"],
            ["Ausgleich = 동점골 b", "Spieltag = 경기 라운드 c", "Anstoß = 킥오프 a", "Königsklasse = 챔피언스리그 별명 d"],
            instr="단어와 뜻 짝짓기")
e.head("C　KOMPARATIV", 25)
e.expl("비교급으로 문장을 완성하세요 (괄호 안은 원급이에요).")
e.ex("B1", "문장 완성", "größer", "groß → größer (이번 주 가장 큰 밤)",
     "Der Mittwoch ist noch ___ (groß) als der Dienstag: Bayern gegen Arsenal!", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "schwerer", "schwer → schwerer",
     "Für Leipzig wird der Abend in Madrid ___ (schwer) als normal.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "später", "spät → später (금요일 20:30 킥오프가 가장 늦어요)",
     "Das Freitagsspiel beginnt ___ (spät) als die Sonntagsspiele.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "mehr", "viel → mehr (팬들은 더 많이 원해요)",
     "Die Fans wollen ___ (viel) Tore sehen.", instr="빈칸", size=20, gap=8)
e.head("D　DAS PRÄTERITUM", 25)
e.expl("문장을 Präteritum (과거형)으로 바꾸세요.")
e.ex("B1", "문장 전환", "Dortmund gewann 2:1 in Baku.", "gewinnen → gewann",
     "Dortmund gewinnt 2:1 in Baku. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Álvarez machte den Ausgleich.", "machen → machte",
     "Álvarez macht den Ausgleich. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Stuttgart spielte 1:1 gegen Atlético.", "spielen → spielte",
     "Stuttgart spielt 1:1 gegen Atlético. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Leipzig verlor 1:6 bei den Bayern.", "verlieren → verlor",
     "Leipzig verliert 1:6 bei den Bayern. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Die Fans waren nervös.", "sein → waren (복수)",
     "Die Fans sind nervös. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
