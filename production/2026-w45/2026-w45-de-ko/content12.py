# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-de-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · FRONT PAGE (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 2 · ZWEITE AUSGABE", 23, "sans", True, OLIVE)
p.text(975, 92, "WÖCHENTLICH AUF DEUTSCH · 매주 발행 · 독일이 읽는 독일어", 21, "sans", False, GREY, anchor="middle")
p.text(RIGHT, 92, "WOCHE VOM 2. BIS 8. NOVEMBER 2026", 23, "sans", False, GREY, anchor="end")
p.hline(MX, RIGHT, 112, GOLD, 1.6)
p.text(975, 262, "Die Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "독일어 주간지 · VOL.2 · 축구 주간 · 유가 · 돌봄", 46, "serif", True, INK, anchor="middle")
p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)

# football band
p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)
p.text(MX + 30, 478, "ENGLISCHE WOCHE — DANN DER 9. SPIELTAG!", 36, "sans", True, "#f3edda")
p.text(MX + 30, 522, "Dienstag bis Sonntag: Champions League, Europa League, Bundesliga — alles in einer Woche", 23, "serif", False, "#e8dfc8")
p.text(RIGHT - 30, 478, "이번 주 축구 주간 · 유럽 대항전과 분데스리가 연속", 24, "sans", True, "#b3a06a", anchor="end")
p.text(RIGHT - 30, 522, "자세한 내용은 4면 · Seite 4", 21, "sans", False, "#b3a06a", anchor="end")

# ---- headline (span cols 0-2) ----
hy = 580
p.text(MX, hy + 26, "DIE TOPMELDUNG · 헤드라인", 22, "sans", True, BRICK)
hy = p.para(MX, hy + 92, "Englische Woche in Deutschland: Vier Nächte Fußball, dann der 9. Spieltag", 44, "serif", True, INK, 1388, 1.2)
p.text(MX, hy + 28, "Von der Lucerna-Redaktion · Leseniveau: A2", 20, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Diese Woche ist eine Fußballwoche: Am Dienstag und Mittwoch spielt die Champions League, am Donnerstag die Europa League, und am Freitag beginnt der 9. Spieltag der Bundesliga. Vier Nächte Fußball, dann ein ganzes Wochenende Liga.")
f.para("Am Dienstag (21.00 Uhr) spielt Bayern bei Atlético Madrid, und Stuttgart spielt schon um 18.45 Uhr bei Galatasaray. Am Mittwoch (21.00 Uhr) empfängt Dortmund Real Betis Sevilla, und Leipzig spielt gegen Manchester City.")
f.para("Am Donnerstagabend (18.45 Uhr) spielt Hoffenheim bei Crystal Palace in London. Am Freitag (20.30 Uhr) beginnt die Bundesliga: Hamburg gegen Mönchengladbach.")
f.para("Am Samstag folgen fünf Spiele, am Sonntag drei: Köln–Leverkusen (15.30 Uhr), Freiburg–Union Berlin (17.30 Uhr), Hoffenheim–Schalke (19.30 Uhr). Das Topspiel am Samstagabend: Stuttgart gegen Bremen (18.30 Uhr).")
f.para("Aber diese Woche ist mehr als Fußball: Der Tankrabatt läuft bis zum 31. Dezember, die Pflege wird debattiert, und in Bayern sind noch Ferien — in Baden-Württemberg geht die Schule schon wieder los. Lesen Sie weiter!")
f.expl("해설 — die Englische Woche 주중과 주말 연속 경기 · der Spieltag 경기일 · empfangen 홈에서 맞기 · die Bundesliga 분데스리가.")
f.box("DIE WOCHE IN ZAHLEN · 숫자로 보기", [
    ("9 — Spiele hat der 9. Spieltag der Bundesliga (분데스리가 9라운드는 총 9경기)", "serif", False, INK, 20.5, 1.35),
    ("6 — deutsche Teams spielen in Europa (6개 독일 팀이 유럽 대항전에 나서요)", "serif", False, INK, 20.5, 1.35),
    ("14,04 — Cent pro Liter beträgt der Tankrabatt (리터당 14.04센트 세금 인하)", "serif", False, INK, 20.5, 1.35),
])
f.head("JETZT ÜBEN · 바로 연습", 25)
f.ex("A2", "문장 완성", "Englische", "주중과 주말 연속 경기",
     "Diese Woche ist eine ___ Woche: viele Spiele in wenigen Tagen.", size=20.5)
f.ex("A2", "문장 완성", "Dortmund", "도르트문트가 베티스를 홈에서 맞아요",
     "Am Mittwoch empfängt ___ Real Betis Sevilla.", size=20.5)
f.ex("A2", "문장 완성", "Donnerstag", "유로파리그는 목요일에 해요",
     "Die Europa League spielt am ___: Hoffenheim bei Crystal Palace.", size=20.5)
f.ex("A2", "문장 완성", "Hamburg", "금요일 함부르크–묀헨글라트바흐전으로 개막해요",
     "Die Bundesliga beginnt am Freitag mit ___ gegen Mönchengladbach.", size=20.5)
f.ex("B1", "문장 완성", "neun", "이번 9라운드는 9경기예요",
     "Der 9. Spieltag hat ___ Spiele.", size=20.5)
f.ex("B1", "문장 완성", "Tankrabatt", "세금이 12월 31일까지 내려가요",
     "Der ___ läuft bis zum 31. Dezember.", size=20.5)
f.end_report()

# ---- questions of the week (col 3) ----
gx, gw = COLX[3], CW
gy = 580
p.rect(gx, gy, gw, 700, fill=BOX, stroke=LINE, sw=1.4)
p.text(gx + 22, gy + 40, "FRAGEN", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DER WOCHE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "이번 주의 큰 질문 · Die Fragen der Woche", 19, "sans", False, GREY)
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
p.text(gx + 22, byy + 76, "독일에서 이번 주 화제가 된 다섯 가지 질문이에요.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(gx + 22, sy + 40, "IN DIESER AUSGABE · 이번 호 목차", 24, "sans", True, OLIVE)
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
p.para(gx, my + 152, "유가 할인(주유 할인)이에요. 자세한 내용은 2면에 있어요.", 19, "sans", False, GREY, gw, 1.35)

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
p.text(bx + 22, 1914, "KURZ & GUT · 짧은 소식", 24, "sans", True, OLIVE)
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
p.text(MX, qy + 36, "BLITZQUIZ · 번개 퀴즈", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "1면을 읽고 정답을 고르세요 · 정답은 8면에", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2540, tag="P1-quiz")
qf.ex("A2", "객관식", "B", "바이에른은 화요일에 아틀레티코 원정 경기를 해요",
      "Bayern spielt am Dienstag bei... A. Real Madrid · B. Atlético Madrid · C. Galatasaray", size=21)
qf.ex("A2", "객관식", "C", "유로파리그에서 호펜하임은 크리스털 팰리스 원정을 가요",
      "Hoffenheim spielt in der Europa League bei... A. Marseille · B. Manchester City · C. Crystal Palace", size=21)
qf.ex("A2", "객관식", "A", "세금이 12월 31일까지 내려가요",
      "Der Tankrabatt läuft bis... A. 31. Dezember · B. 1. November · C. 31. Oktober", size=21)
qf.ex("A2", "객관식", "A", "금요일 함부르크–묀헨글라트바흐전으로 개막해요",
      "Der 9. Spieltag beginnt am Freitag mit... A. Hamburg–Gladbach · B. Dortmund–Elversberg · C. Stuttgart–Bremen", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEBEN · 생활", "Die Lucerna", "LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 유가, 전기세와 돌봄")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Tanken für weniger: Der Tankrabatt läuft bis Silvester", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: A2")
f.para("Gute Nachricht für alle, die Auto fahren: Seit dem 1. Oktober ist das Tanken in Deutschland billiger. Der Bundestag und der Bundesrat haben am 25. September beschlossen: Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter. Das gilt bis zum 31. Dezember 2026. Mit der Mehrwertsteuer sind es an der Zapfsäule rund 16,7 Cent pro Liter.")
f.para("Was heißt das für eine Tankfüllung? Wer 50 Liter tankt, spart rund 8,35 Euro. Der Staat verzichtet dafür auf rund 2,5 Milliarden Euro an Steuern — Bund und Länder teilen sich die Kosten etwa zur Hälfte.")
f.para("Aber Achtung: Die Tankstellen müssen den Rabatt nicht eins zu eins weitergeben. Das Gesetz senkt nur die Steuer — den Preis macht die Tankstelle. Am Morgen des 1. Oktober fielen die Preise um 14 bis 15 Cent, mittags stiegen sie schon wieder: Der ADAC berichtet, dass ein Teil des Rabatts im Preis „verschwindet“.")
f.para("Zweites Thema der Woche: die Stromsteuer. Union und SPD streiten noch, wie stark sie sinken soll. Viele Haushalte hoffen auf billigeren Strom — vor allem, weil die Energiepreise die Einkommen drücken. Auch der ZEW-Index zeigt es: Die Erwartungen der Finanzexperten fielen im Oktober um 6,6 Punkte auf 28,1.")
f.para("Drittes Thema: die Pflege. Nach Angaben der ARD-Sendung „Hart aber fair“ (26. Oktober) brauchen in Deutschland mehr als sechs Millionen Menschen Pflege. Die meisten von ihnen werden zu Hause gepflegt — von rund zehn Millionen Angehörigen. Am Montag, dem 26. Oktober, diskutierte die ARD-Sendung „Hart aber fair“ (21.00 Uhr): „Pflege zu Hause — Lässt die Politik Angehörige allein?“ Mehr dazu auf Seite 6.")
f.gloss("der Tankrabatt 유가 할인 · die Zapfsäule 주유기 · die Energiesteuer 에너지세 · die Mehrwertsteuer 부가가치세 · der Angehörige 가족.")
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
p.text(ix + 22, yy3 + 26, "AN DER ZAPFSÄULE · 주유소 옆", 24, "sans", True, OLIVE)
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
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("운전하세요? 여러분 나라 기름값은 얼마예요? 독일어로 두 문장 보내 주세요.", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · 여러분은요?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "운전하세요? 여러분 나라 기름값은 얼마예요? 독일어로 두 문장 보내 주세요.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 box3 ends", ey3 + eh)
zew = ["Erwartungen: 28,1 Punkte (minus 6,6 im Oktober).",
       "Lage: minus 35,9 Punkte (plus 11,2).",
       "Prognose: Die Wirtschaft wächst langsam, aber nicht von allein."]
sy3 = ey3 + eh + 26
sh = 45 + 33 * len(zew) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in zew)
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "ZEW IN KÜRZE · ZEW 지수 소식", 24, "sans", True, OLIVE)
yy3 += 52
for t in zew:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box4 ends", sy3 + sh)

# ---- Rechnen wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, GOLD, 2)
p.text(MX, dy + 28, "RECHNEN WIR MAL · 계산해 봐요", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Die Zahlen der Woche · 이번 주 숫자", 20, "sans", False, GREY, anchor="end")
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
p.para(1090, ly - 108 + 22 + 4 * 29.1 + 10, "주의: 내려가는 것은 세금이고, 가격은 주유소가 정해요. 주유하기 전에 가격을 비교하세요.", 20, "sans", False, GREY, RIGHT - 1090, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · 2면 연습", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "정답은 8면에 · 번호로 정답을 찾으세요", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A · WIE VIEL SPAREN?", 25)
e.expl("2면 기사를 보고 숫자로 빈칸을 채우세요.")
e.ex("A2", "문장 완성", "14,04", "리터당 14.04센트 세금이 내려가요",
     "Die Steuer sinkt um ___ Cent pro Liter.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "8,35", "50리터를 넣으면 약 8.35유로를 아껴요",
     "Wer 50 Liter tankt, spart rund ___ Euro.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "31. Dezember", "2026년 말까지 세금이 내려가요",
     "Der Tankrabatt läuft bis zum ___ 2026.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "2,5 Milliarden", "국가는 약 25억 유로 세금을 덜 거둬요",
     "Der Staat verzichtet auf rund ___ Euro.", instr="빈칸", size=20, gap=8)
e.ex("A2", "문장 완성", "Zapfsäule", "주유기에서는 실제로 약 16.7센트 내려가요",
     "Mit Mehrwertsteuer sind es an der ___ rund 16,7 Cent weniger.", instr="빈칸", size=20, gap=8)
e.head("B · DAS PERFEKT", 25)
e.expl("Perfekt(현재완료)로 바꾸세요.")
e.ex("A2", "문장 전환", "Der Bundestag hat den Tankrabatt beschlossen.", "beschließen → beschlossen",
     "Der Bundestag (beschließen) den Tankrabatt. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("A2", "문장 전환", "Die Preise sind am Morgen gefallen.", "fallen은 sein과 함께 써요",
     "Die Preise (fallen) am Morgen. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("A2", "문장 전환", "Wir haben 50 Liter getankt.", "tanken → getankt",
     "Wir (tanken) 50 Liter. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Die Tankstellen haben den Rabatt nicht voll weitergegeben.", "weitergeben은 분리 동사예요",
     "Die Tankstellen (weitergeben) den Rabatt nicht voll. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.ex("B1", "문장 전환", "Die Erwartungen sind im Oktober gefallen.", "ZEW 전망이 떨어졌어요",
     "Die Erwartungen (fallen) im Oktober. → ___", instr="바꿔 쓰기", size=20, gap=8)
e.head("C · LESEVERSTEHEN", 25)
e.expl("2면 기사를 읽고 정답을 고르세요.")
e.ex("A2", "객관식", "B", "내려가는 것은 에너지세예요",
     "Was sinkt beim Tankrabatt? A. der Preis direkt · B. die Steuer · C. die Mehrwertsteuer allein", size=20, gap=8)
e.ex("A2", "객관식", "B", "주유소가 가격을 정해요",
     "Wer bestimmt den Preis? A. der Staat · B. die Tankstelle · C. der ADAC", size=20, gap=8)
e.ex("A2", "객관식", "A", "기민·기사연합과 사민당이에요",
     "In der Stromsteuer-Debatte streiten... A. Union und SPD · B. Bayern und Dortmund · C. ADAC und ZEW", size=20, gap=8)
e.ex("A2", "객관식", "B", "가족이 집에서 돌봐요",
     "Wer pflegt zu Hause? A. die Ärzte · B. die Angehörigen · C. die Tankstellen", size=20, gap=8)
e.head("D · DIE WÖRTER", 25)
e.match_set("A2", "단어 짝짓기",
            ["der Tankrabatt", "die Zapfsäule", "die Mehrwertsteuer", "der Angehörige"],
            ["die Steuer, die beim Kauf dazu kommt",
             "die Ermäßigung auf die Energiesteuer",
             "ein Familienmitglied, das pflegt",
             "die Säule an der Tankstelle, aus der Benzin kommt"],
            ["b", "d", "a", "c"],
            ["Tankrabatt=유가 할인 b", "Zapfsäule=주유기 d", "Mehrwertsteuer=부가가치세 a", "Angehörige=가족 c"],
            instr="단어와 뜻 짝짓기")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leben.svg")
print("P2 saved, exercises so far:", len(REG))
