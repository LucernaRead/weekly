# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-de-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH / LIBRARIES (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND · 청소년", "Die Lucerna", "LEVEL B1 · Ferien & Bibliotheken · 방학과 도서관")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Ferien ohne Schule: Die Stadt gehört den Lesern", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B1")
f.para("Ferien — und die Schule ist zu. Was machen die Kinder und Jugendlichen in Berlin? In dieser Woche gehört die Stadt den Leserinnen und Lesern: Die Berliner Bibliotheken machen eine ganze Aktionswoche, denn am Samstag ist der Tag der Bibliotheken.")
f.para("Es gibt Bibliotheks-Bingo, eine Wand mit Lieblingsbüchern und „Book-Blind-Dates“. Wie funktioniert ein Book-Blind-Date? Das Buch ist eingepackt, man sieht nur drei Stichworte. Man wählt ein Buch, ohne es zu kennen. Erst zu Hause packt man es aus — eine Überraschung wie ein Geschenk.")
f.para("Warum der 24. Oktober? Das Datum erinnert an Karl Preusker: Am 24. Oktober 1828 gründete er in Großenhain in Sachsen eine Bibliothek — aus ihr wurde die erste öffentliche Bibliothek Deutschlands. Seit 1995 feiert das Land am 24. Oktober den Tag der Bibliotheken; Schirmherr war damals Bundespräsident Richard von Weizsäcker. Mehr als 8 000 Bibliotheken gibt es heute in Deutschland.")
f.para("Und Halloween? Die Vorbereitungen laufen: Im Zoo Osnabrück geben Kinder ihre geschnitzten Kürbisse ab (Seite 3), und die Discounter verkaufen schon Kostüme. Wer noch ein Kostüm sucht, muss sich beeilen — am Samstag, dem 31. Oktober, ist die große Nacht.")
f.para("Für viele Familien sind die Herbstferien auch Reisezeit. Aber nicht alle fahren weg: Bibliotheken, Zoos und Erlebnisparks machen den Herbst zu Hause zum Programm. Unser Tipp für den Samstag: erst in die Bibliothek, dann einen Kürbis schnitzen!")
f.gloss("die Aktionswoche 행사 주간 · das Stichwort 키워드 · eingepackt 포장된 · der Schirmherr 명예 후원자 · sich beeilen 서두르다.")
f.end_report()

# col 3: pumpkin image + facts + Und Sie
ix = COLX[3]
image(p, "kuerbis.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Kürbisse auf einem Markt in den USA: Auch in Deutschland ist im Oktober Kürbiszeit — zum Schnitzen, Kochen und Dekorieren. (Seite 3)",
              "Foto: U.S. Department of Agriculture — public domain")
facts = ["11 Bundesländer haben gleichzeitig Herbstferien — der Höhepunkt ist in dieser Woche.",
         "Mehr als 8 000 Bibliotheken gibt es in Deutschland.",
         "Am Montag (26. Oktober) gehen sechs Länder zurück in die Schule — Baden-Württemberg startet dann in die Ferien."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 14
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "FERIEN IN ZAHLEN", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "Und Sie? Wann waren Sie das letzte Mal in einer Bibliothek? Und welches Buch würden Sie als Blind Date wählen? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("마지막으로 도서관에 간 것은 언제인가요? 블라인드 데이트로 어떤 책을 고를까요? 독일어로 두 문장을 써서 보내 주세요.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · 여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "마지막으로 도서관에 간 것은 언제인가요? 블라인드 데이트로 어떤 책을 고를까요? 독일어로 두 문장을 써서 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)


# ---- Samstag-Plan wide box (cols 0-2) ----
sx, swd = span_x(0, 2)
p.rect(sx, 1120, swd, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "DER SAMSTAG-PLAN DER REDAKTION · 편집부의 토요일 계획", 24, "sans", True, OLIVE)
planrows = [
    ("9.30 Uhr", "In die Bibliothek: Bingo spielen und ein Book-Blind-Date wählen."),
    ("12.00 Uhr", "Auf dem Markt einen schönen Kürbis kaufen."),
    ("15.00 Uhr", "Zu Hause den Kürbis schnitzen — Ideen auf Seite 3."),
    ("18.30 Uhr", "Fußball: Dortmund gegen Frankfurt, das Topspiel (Seite 4)."),
    ("danach", "Die Uhren umstellen nicht vergessen! (Seite 2)"),
]
pyy = 1184
for t, txt in planrows:
    p.text(sx + 24, pyy + 24, t, 21, "sans", True, BRICK)
    p.text(sx + 190, pyy + 24, txt, 21.5, "serif", False, INK)
    pyy += 45

# ---- P5 exercises ----
ey = 1500
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 5면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에 · 문제는 수준이 섞여 있어요 · 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · LESEVERSTEHEN", 25)
e.expl("5면 기사를 읽고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "도서관의 날이라 행사 주간이에요",
     "Die Aktionswoche gibt es, weil... A. die Schule neu ist · B. der Tag der Bibliotheken ist · C. Halloween ausfällt", size=20, gap=8)
e.ex("B1", "객관식", "B", "블라인드 데이트 책은 키워드 세 개만 보여요",
     "Bei einem Book-Blind-Date sieht man nur... A. den Preis · B. drei Stichworte · C. den Autor", size=20, gap=8)
e.ex("A2", "객관식", "A", "도서관의 날은 10월 24일",
     "Der Tag der Bibliotheken ist am... A. 24. Oktober · B. 31. Oktober · C. 19. Oktober", size=20, gap=8)
e.ex("B1", "객관식", "B", "Preusker는 1828년 Großenhain에서",
     "Karl Preusker gründete seine Bibliothek im Jahr... A. 1517 · B. 1828 · C. 1995", size=20, gap=8)
e.ex("A2", "객관식", "B", "10월 31일은 할로윈",
     "Am 31. Oktober ist... A. der Schulanfang · B. Halloween · C. der Bibliothekstag", size=20, gap=8)
e.head("B · WÖRTER AUS DEM TEXT", 25)
e.expl("상자 속 단어로 빈칸을 채우세요.")
e.para("Bibliothek · Stichworte · Überraschung · eingepackt · Lieblingsbuch · leihen", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "Stichworten", "nach drei + 3격 복수 Stichworten",
     "Man wählt ein Buch nach drei ___.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "eingepackt", "책이 포장되어 있어요",
     "Das Buch ist ___ — man sieht es nicht.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Überraschung", "선물 같은 놀라움",
     "Ein Blind Date mit einem Buch ist eine ___.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Lieblingsbuch", "가장 좋아하는 책이 벽에",
     "An der Wand hängt mein ___.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Bibliothek", "도서관에서 책을 빌려요",
     "In der ___ kann man Bücher leihen.", instr="빈칸", size=20, gap=8)
e.ex("B1", "문장 완성", "leihen", "möchte + 원형은 문장 끝에",
     "Ich möchte dieses Buch ___ — für drei Wochen.", instr="빈칸", size=20, gap=8)
e.head("C · SÄTZE MIT «WEIL»", 25)
e.expl("weil로 두 문장을 연결하세요 (동사는 문장 끝에).")
e.ex("B1", "문장 전환", "Die Kinder freuen sich, weil Ferien sind.", "weil 문장은 동사가 끝에",
     "Die Kinder freuen sich. Es sind Ferien. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Die Bibliotheken machen eine Aktionswoche, weil es der Tag der Bibliotheken ist.", "ist가 문장 끝으로",
     "Die Bibliotheken machen eine Aktionswoche. Es ist der Tag der Bibliotheken. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Er bleibt zu Hause, weil er ein Buch lesen will.", "will이 끝에",
     "Er bleibt zu Hause. Er will ein Buch lesen. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Sie kauft ein Kostüm, weil Halloween am 31. Oktober ist.", "ist가 끝에",
     "Sie kauft ein Kostüm. Halloween ist am 31. Oktober. (weil) → ___", instr="바꿔 쓰기", size=20, gap=8)
e.head("D · RICHTIG ODER FALSCH?", 25)
e.expl("맞는지 틀린지 판단하세요.")
e.ex("A2", "참/거짓 판단", "Richtig", "독일에 도서관 8,000곳 넘어",
     "Mehr als 8 000 Bibliotheken gibt es in Deutschland. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("B1", "참/거짓 판단", "Falsch", "도서관의 날은 1995년부터",
     "Der Tag der Bibliotheken ist ein neuer Tag aus dem Jahr 2026. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.ex("A2", "참/거짓 판단", "Richtig", "베를린 행사 주간은 토요일까지",
     "Die Aktionswoche in Berlin dauert bis Samstag. Richtig oder falsch?", instr="판단", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG · 심층 읽기", "Die Lucerna", "LEVEL B2 · Die große Debatte · 큰 토론")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Soll die Zeitumstellung abgeschafft werden?", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B2")
f.para("Zweimal im Jahr steht die EU vor derselben Frage: vor oder zurück? An diesem Sonntag ist es wieder so weit. Doch warum gibt es die Sommerzeit überhaupt — und warum bleibt sie, obwohl so viele Menschen sie nicht mehr wollen?")
f.para("Deutschland stellte die Uhren zum ersten Mal am 30. April 1916 um — mitten im Ersten Weltkrieg sollte Tageslicht Energie sparen. Nach dem Zweiten Weltkrieg endete die Praxis 1950. Erst am 6. April 1980 führten beide deutsche Staaten die Sommerzeit wieder ein; seitdem gilt sie ohne Unterbrechung.")
f.para("Die Argumente sind bekannt: Die Freunde der Sommerzeit lieben die hellen Abende im Sommer. Die Kritiker sagen, der Körper leide unter dem Wechsel — und der Nutzen für die Energie sei heute klein.")
f.para("Im Sommer 2018 fragte die EU-Kommission die Menschen in Europa: Soll die Zeitumstellung enden? 4,6 Millionen Antworten kamen zurück — so viele wie noch nie bei einer solchen Befragung. 84 Prozent von ihnen wollten die Umstellung abschaffen. Im März 2019 stimmte das Europäische Parlament mit 410 zu 192 Stimmen dafür, die Umstellung ab 2021 zu beenden. Aber die Regierungen der Mitgliedstaaten wurden sich nicht einig — und so blieb alles, wie es ist. Die Länder konnten sich nicht entscheiden, ob sie für immer Sommerzeit oder Winterzeit wollen.")
f.para("Und nun? An diesem Sonntag genießen wir erst einmal die geschenkte Stunde. Die Debatte kommt bestimmt wieder — spätestens im März, wenn die Uhren wieder vorgestellt werden.")
f.gloss("abschaffen 폐지하다 · die Befragung 설문조사 · der Mitgliedstaat 회원국 (복수 die Mitgliedstaaten) · sich einig werden 합의하다 · leiden 고통받다.")
f.end_report()

# col 3: timeline + health + Und Sie (sequential, measured)
ix = COLX[3]
tl = [("1916", "Deutschland stellt zum ersten Mal um (30. April)."),
      ("1950", "Die Praxis endet nach dem Zweiten Weltkrieg."),
      ("1980", "Beide deutsche Staaten führen die Sommerzeit wieder ein (6. April)."),
      ("2018", "EU-Befragung: 4,6 Millionen Antworten, 84 % für ein Ende."),
      ("2019", "Das EU-Parlament stimmt 410 : 192 für das Ende ab 2021."),
      ("2026", "Die Regierungen sind sich weiter nicht einig — umgestellt wird wie immer.")]
tlh = 52
for yr, t in tl:
    tlh += 30 + len(wrap(t, "serif", False, 20.5, CW - 44)) * 29 + 10
p.rect(ix, 200, CW, tlh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DIE ZEITLINIE · 타임라인", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, BRICK)
    yy3 = p.para(ix + 92, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 114, 1.42) + 10
hy3 = 200 + tlh + 26
health = "Die Grippezeit kommt. Die STIKO empfiehlt die Impfung besonders für Menschen ab 60 Jahren, für Schwangere ab dem zweiten Drittel, für Menschen mit chronischen Krankheiten und für alle, die in Pflege und Medizin arbeiten. Der Schutz baut sich in 10 bis 14 Tagen auf. Impfen lassen kann man sich beim Hausarzt und in Apotheken (ab 18 Jahren)."
hh = 62 + len(wrap(health, "serif", False, 21, CW - 44)) * 30 + 10 + len(wrap("독감 철이 와요: STIKO는 60세 이상, 임산부 (중기부터), 만성질환자와 의료·돌봄 종사자에게 접종을 권해요. 면역은 10–14일에 생겨요.", "sans", False, 19.5, CW - 44)) * 28 + 20
p.rect(ix, hy3, CW, hh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "GESUND DURCH DEN HERBST", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, health, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "독감 철이 와요: STIKO는 60세 이상, 임산부 (중기부터), 만성질환자와 의료·돌봄 종사자에게 접종을 권해요. 면역은 10–14일에 생겨요.", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)


# ---- Pro & Contra wide box (cols 0-2) ----
sx, swd = span_x(0, 2)
p.rect(sx, 1120, swd, 252, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "PRO & CONTRA · 찬성과 반대 — die Argumente der Debatte", 24, "sans", True, OLIVE)
p.text(sx + 24, 1210, "PRO SOMMERZEIT", 21, "sans", True, BRICK)
p.text(sx + 24 + (swd - 48) // 2, 1210, "CONTRA — GEGEN DIE UMSTELLUNG", 21, "sans", True, BRICK)
pro = ["Helle Abende im Sommer: mehr Zeit draußen, im Café und beim Sport.",
       "Feste und Märkte am Abend leben vom langen Licht."]
contra = ["Der Körper leidet unter dem Wechsel, sagen die Kritiker.",
          "Energie wird heute kaum noch gespart — und 84 Prozent wollten 2018 ein Ende."]
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
p.hline(MX, RIGHT, cy - 12, GOLD, 2)
p.text(MX, cy + 28, "WAS MACHEN DIE DEUTSCHEN MIT DER EXTRA STUNDE? · 늘어난 한 시간으로 무엇을 할까요?", 26, "sans", True, OLIVE)
bars = [("länger schlafen", 46, "더 자기"), ("Zeit mit der Familie", 22, "가족과 함께"),
        ("ein Buch lesen", 18, "책 읽기"), ("Sport machen", 14, "운동")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 330, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 24, 30, fill=OLIVE)
    p.text(MX + 470 + v * 24 + 16, byy + 26, f"{v} %", 22, "sans", True, BRICK)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN · 연습 데이터 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (이 숫자는 편집부의 연습 예시이며 실제 설문조사가 아니에요.)", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1808
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 6면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에 · 문제는 수준이 섞여 있어요 · 번호로 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · DAS DIAGRAMM LESEN", 25, gap=9)
e.expl("위의 연습 차트를 보고 정답을 고르세요.")
e.ex("B1", "객관식", "B", "46%가 더 자요",
     "Wie viele Prozent schlafen länger? A. 22 % · B. 46 % · C. 18 %", size=20, gap=7)
e.ex("B1", "객관식", "C", "2위는 가족과 함께 22%",
     "Was ist die zweitliebste Aktivität? A. Sport · B. ein Buch lesen · C. Zeit mit der Familie", size=20, gap=7)
e.ex("B1", "객관식", "B", "46 + 18 = 64",
     "Länger schlafen und ein Buch lesen zusammen sind... A. 60 % · B. 64 % · C. 68 %", size=20, gap=7)
e.ex("B2", "객관식", "B", "가족+독서 = 40% > 운동 14%",
     "Welche Gruppe ist größer? A. Sport allein · B. Familie und Lesen zusammen · C. beide gleich", size=20, gap=7)
e.ex("B1", "객관식", "A", "운동 14%",
     "Wie viele Prozent machen Sport? A. 14 % · B. 18 % · C. 22 %", size=20, gap=7)
e.ex("B2", "객관식", "B", "46+22+18+14=100",
     "Die vier Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=7)
e.head("B · LESEVERSTEHEN (B2)", 25, gap=9)
e.expl("6면 심층 기사를 읽고 정답을 고르세요.")
e.ex("B2", "객관식", "B", "1916년 4월 30일 처음",
     "Wann stellte Deutschland die Uhren zum ersten Mal um? A. 1950 · B. 1916 · C. 1980", size=20, gap=7)
e.ex("B2", "객관식", "C", "410 대 192로 폐지 찬성",
     "Wie stimmte das EU-Parlament 2019? A. 192 : 410 dagegen · B. einstimmig dafür · C. 410 : 192 dafür", size=20, gap=7)
e.ex("B2", "객관식", "B", "회원국 정부들이 합의하지 못했어요",
     "Warum blieb die Umstellung? A. Die Bürger wollten sie. · B. Die Regierungen wurden sich nicht einig. · C. Das Parlament sagte Nein.", size=20, gap=7)
e.ex("B1", "객관식", "A", "답변 460만 건",
     "Wie viele Antworten kamen 2018 zurück? A. 4,6 Millionen · B. 460 000 · C. 84 Millionen", size=20, gap=7)
e.head("C · GRAMMATIK", 25, gap=9)
e.expl("괄호 속 형태로 빈칸을 채우세요.")
e.ex("B2", "문장 완성", "werden", "수동태: werden + Partizip II",
     "Die Uhren ___ (werden) am Sonntag umgestellt.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "ob", "ob가 이끄는 간접 의문문",
     "Die Länder wissen nicht, ___ sie Sommerzeit oder Winterzeit wollen.", instr="빈칸", size=20, gap=7)
e.ex("B1", "문장 완성", "abschaffen", "wollen + 원형은 문장 끝에",
     "84 Prozent wollten die Umstellung ___. (abschaffen)", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "stimmte", "stimmen의 과거형 stimmte",
     "Im März 2019 ___ das Parlament für das Ende. (stimmen)", instr="빈칸", size=20, gap=7)
e.head("D · WÖRTER DER DEBATTE", 25, gap=9)
e.expl("상자 속 단어로 빈칸을 채우세요.")
e.para("Umstellung · Mehrheit · abschaffen · Mitgliedstaaten", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "문장 완성", "Umstellung", "Umstellung은 해마다 두 번",
     "Die ___ findet zweimal im Jahr statt.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "Mehrheit", "84%는 확실한 다수",
     "84 Prozent sind eine klare ___.", instr="빈칸", size=20, gap=7)
e.ex("B1", "문장 완성", "abschaffen", "wollen + abschaffen",
     "Viele Menschen wollen die Umstellung ___.", instr="빈칸", size=20, gap=7)
e.ex("B2", "문장 완성", "Mitgliedstaaten", "회원국 정부들이 합의하지 못했어요",
     "Die ___ der EU konnten sich nicht einigen.", instr="빈칸", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
