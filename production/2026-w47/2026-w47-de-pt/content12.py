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
p.text(MX, 92, "VOL. 4　VIERTE AUSGABE", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "WÖCHENTLICH AUF DEUTSCH　UM NÚMERO POR SEMANA　O ALEMÃO DOS ALEMÃES", 17, "sans", False, GREY, anchor="middle", spacing=1.7)  # F7 (2026-11-12): reader segment shortened (was O ALEMÃO QUE OS ALEMÃES LEEM); advance gap to dateline 31.9px.
p.text(RIGHT, 92, "WOCHE VOM 16. BIS 22. NOVEMBER 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Die Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SEMANAL ALEMÃO　VOL.4　VOLTA A BUNDESLIGA　SEMANA TRANQUILA", 36, "serif", True, OLIVE, anchor="middle", spacing=3.0)
p.text(975, 372, "TEXTO EM ALEMÃO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA LEITORES DE LÍNGUA PORTUGUESA", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# football band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "DIE BUNDESLIGA IST ZURÜCK — BAYERN GEGEN KÖLN!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Montag bis Sonntag: Nationalelf-Entscheidung, stille Tage, Weihnachtsmärkte — alles in einer Woche", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "VOLTA A BUNDESLIGA", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Ver página 4", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "DIE TOPMELDUNG　Em destaque", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Die Bundesliga kehrt zurück — Bayern gegen Köln", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Von der Lucerna-Redaktion　Leseniveau: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Diese Woche ist die Bundesliga zurück: Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln. Anstoß ist um 20.30 Uhr in der Allianz Arena in München. Die Bayern führen die Tabelle an — Köln ist Fünfzehnter.")
f.para("Doch zuerst die Nationalmannschaft — schon am Freitag, dem 13. November: Deutschland traf in Belgrad auf Serbien, vor fast leeren Rängen (UEFA-Strafe: nur Kinder und 50 deutsche Fans durften ins Stadion). Am Montag (20.45 Uhr) folgt das Endspiel gegen die Niederlande in Berlin. Es geht ums Viertelfinale der Nations League.")
f.para("Am Mittwoch ist in Deutschland ein stiller Tag: der Buß- und Bettag. Nur Sachsen hat an diesem Tag frei. Am Sonntag folgt der Totensonntag — der letzte Sonntag des Kirchenjahres. An diesem Tag bleiben viele Weihnachtsmärkte geschlossen.")
f.para("Und die Weihnachtsmärkte? In Köln öffnen der Markt am Dom und der Markt der Engel am Montag, dem 16. November. Die offizielle Eröffnung am Dom ist am Dienstag um 19 Uhr. Der erste Advent ist erst am 29. November — die Märkte beginnen früher als das Fest.")
f.para("Die Ergebnisse vom 3. bis 8. November stehen fest: Bayern gewann in Madrid mit 2:0, Dortmund schlug Betis Sevilla mit 2:1. In der Bundesliga fielen am 9. Spieltag 30 Tore. Mehr dazu auf Seite 4.")
f.bridge("Notas — die Bundesliga = Bundesliga · das Viertelfinale = quartos de final · der Buß- und Bettag = dia de arrependimento e oração · der Totensonntag = domingo dos mortos.")
f.box("DIE WOCHE IN ZAHLEN　Em números", [
    ("5 — Punkte hat Deutschland nach vier Spielen in der Nations League (5 pontos em 4 jogos)", "serif", False, INK, 20.5, 1.35),
    ("20.30 — Anstoß Bayern gegen Köln am Freitagabend (Bayern–Colónia, 20h30)", "serif", False, INK, 20.5, 1.35),
    ("30 — Tore fielen am 9. Spieltag der Bundesliga (30 golos, jornada 9)", "serif", False, INK, 20.5, 1.35),
], tsize=20)  # D5 (2026-11-12): the earlier boxtitle fix (23->21.5) held under CJK Sans but Newsreader SemiBold runs wider: @21.5pt still +23.2px past the box; @20pt 397.6px fits 404.5 (21pt still overflows by 13.0px). No wording change.
f.head("JETZT ÜBEN　Pratica agora", 25)
f.ex("A2", "completar", "Bundesliga", "Volta a Bundesliga",
     "Diese Woche ist die ___ zurück: Bayern spielt gegen Köln.", size=22)
f.ex("A2", "completar", "Niederlande", "Países Baixos, segunda-feira",
     "Am Montag spielt Deutschland in Berlin gegen die ___.", size=22)
f.ex("A2", "completar", "Sachsen", "Só a Saxónia",
     "Der Buß- und Bettag ist nur in ___ ein Feiertag.", size=22)
f.ex("A2", "completar", "Totensonntag", "Domingo: Totensonntag",
     "Am Sonntag ist ___: der letzte Sonntag des Kirchenjahres.", size=22)
f.ex("B1", "completar", "fünf", "5 pontos em 4 jogos",
     "Deutschland hat nach vier Spielen ___ Punkte.", size=22)
f.ex("B1", "completar", "29. November", "Primeiro Advento: 29 nov.",
     "Der erste Advent ist am ___.", size=22)
f.end_report()

# ---- questions of the week (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "FRAGEN", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DER WOCHE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "As grandes perguntas　Die Fragen der Woche", 19, "sans", False, GREY)
gt = [
    ("„Deutschland im Viertelfinale?“", 250),
    ("„Bayern gegen Köln?“", 226),
    ("„Buß- und Bettag — frei?“", 196),
    ("„Weihnachtsmarkt schon jetzt?“", 158),
    ("„Totensonntag — was ist das?“", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Die fünf Fragen, über die Deutschland", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in dieser Woche spricht.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "As cinco perguntas da semana.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN DIESER AUSGABE　Sumário", 24, "sans", True, OLIVE)
som = [
    ("S.2", "Buß- und Bettag & Alltag", "A2"),
    ("S.3", "Weihnachtsmärkte & Stille", "A2→B1"),
    ("S.4", "Ergebnisse & Rückkehr", "B1"),
    ("S.5", "Adventskalender & Kinder", "B1"),
    ("S.6", "Stille Woche & Haushalt", "B2"),
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
p.text(gx, my + 76, "« der Adventskalender »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "Ein Kalender mit 24 Türchen — jeden Tag eine Überraschung.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "Calendário do Advento (24 portas). Ver p. 5.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "fussball.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Fußball auf dem Rasen: Am Freitag kehrt die Bundesliga zurück — Bayern empfängt Köln in München. Am Montag spielt die Nationalelf in Berlin gegen die Niederlande. (Seite 4)",
        "Foto: Staff Sgt. Stephanie Jacobs, U.S. Air Force — public domain")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-fussball")
f2.head("EINE WOCHE, ZWEI STIMMUNGEN", 22)  # D5 (2026-11-12): @25pt the head is 468.0px > column 422.5px (HEAD TOO WIDE); @22pt 411.8px fits. No wording change.
f2.para("Freitagabend in München, Sonntag still im ganzen Land: Erst die Bundesliga, dann der Totensonntag — eine Woche, zwei Stimmungen.", 22.5)
f2.para("Und am Montag? Da öffnen in Köln die Weihnachtsmärkte — mitten in der stillen Woche. Der November kann beides: laut und leise.", 22.5)
f2.end_report()
# col 3 KURZ & GUT
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "KURZ & GUT　Em resumo", 24, "sans", True, OLIVE)
brefs = [
    ("FUSSBALL", "Nations League: Serbien auswärts, Niederlande zu Hause. (Seite 4)"),
    ("BUNDESLIGA", "10. Spieltag: Bayern gegen Köln am Freitag, 20.30 Uhr. (Seite 4)"),
    ("WEIHNACHTEN", "Die Märkte in Köln öffnen am 16. November, am 22. November bleiben sie zu. (Seite 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "BLITZQUIZ　Quiz-relâmpago", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lê a primeira página e escolhe a resposta　Respostas na p. 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "escolha múltipla", "B", "Países Baixos, segunda-feira",
      "Deutschland spielt am Montag in Berlin gegen... A. Serbien · B. die Niederlande · C. Griechenland", size=22)
qf.ex("A2", "escolha múltipla", "A", "Bayern–Colónia, sexta-feira 20h30",
      "Bayern gegen Köln beginnt am Freitag um... A. 20.30 Uhr · B. 15.30 Uhr · C. 18.30 Uhr", size=22)
qf.ex("A2", "escolha múltipla", "B", "Só a Saxónia",
      "Der Buß- und Bettag ist ein Feiertag nur in... A. Bayern · B. Sachsen · C. Berlin", size=22)
qf.ex("A2", "escolha múltipla", "B", "Mercados de Natal de Colónia: 16 nov.",
      "Die Weihnachtsmärkte in Köln öffnen am... A. 29. November · B. 16. November · C. 22. November", size=22)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LIFE (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEBEN　Vida", "Die Lucerna", "LEVEL A2　Der Buß- und Bettag & der Alltag　Dia de arrependimento e vida quotidiana")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Ein Mittwoch, der fast frei ist: Der Buß- und Bettag", 32)
f.byline("Von der Lucerna-Redaktion　Leseniveau: A2")
f.para("Am Mittwoch, dem 18. November, ist Buß- und Bettag. Es ist ein evangelischer Feiertag — ein Tag zum Nachdenken und Beten. Doch frei haben nur die Menschen in Sachsen: Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag.")
f.para("In Bayern ist an diesem Tag kein Unterricht: Die Schulen bleiben geschlossen. Aber die Eltern müssen arbeiten — für sie ist der Mittwoch ein normaler Arbeitstag. In den anderen Bundesländern läuft alles ganz normal.")
f.para("Warum ist der Tag nur in Sachsen frei? Früher war der Buß- und Bettag in ganz Deutschland ein Feiertag. Im Jahr 1995 wurde er fast überall abgeschafft — als Ausgleich für die Pflegeversicherung. Nur Sachsen behielt ihn. Dafür zahlen Arbeitnehmer in Sachsen einen höheren Beitrag zur Pflegeversicherung.")
f.para("Was macht man an einem stillen Tag? Viele Menschen gehen in die Kirche, andere lesen oder gehen spazieren. Tanzveranstaltungen sind in Sachsen an diesem Tag von 3 bis 24 Uhr verboten — der Tag soll ruhig bleiben.")
f.para("Und vier Tage später? Am Sonntag, dem 22. November, ist Totensonntag — der letzte Sonntag des Kirchenjahres. Auch er ist ein stiller Tag. Die Weihnachtsmärkte in Köln bleiben an diesem Sonntag geschlossen. Mehr dazu auf Seite 3.")
f.para("So sieht die Woche aus: Montag Nationalelf, Mittwoch Buß- und Bettag, Freitag Bundesliga, Sonntag Totensonntag — laut und leise, nah beieinander.")
f.gloss("der Buß- und Bettag = dia de arrependimento e oração · evangelisch = protestante · der Feiertag = feriado · die Pflegeversicherung = seguro de dependência · still = calmo.")
f.end_report()

# col 3: four boxes (hand-rolled; CORRECTED height formula — see W45 KIT §geometry)
ix = COLX[3]
zapf = ["18. November — Buß- und Bettag, ein Mittwoch.",
        "Nur in Sachsen: gesetzlicher Feiertag.",
        "In Bayern: kein Unterricht, aber kein freier Tag."]
sy3 = 200
sh = 45 + 33 * len(zapf) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in zapf)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DER BUß- UND BETTAG", 24, "sans", True, OLIVE)
yy3 += 52
for t in zapf:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box1 ends", sy3 + sh)
sav = ["1995 abgeschafft — nur Sachsen behielt den Feiertag.",
       "Elf Tage vor dem ersten Advent: immer ein Mittwoch.",
       "Tanzveranstaltungen in Sachsen von 3 bis 24 Uhr verboten."]
sy3 = sy3 + sh + 26
sh = 45 + 33 * len(sav) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in sav)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WUSSTEN SIE DAS?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box2 ends", sy3 + sh)
ey3 = sy3 + sh + 26
etvous = "Und Sie? Gibt es in Ihrem Land einen stillen Tag? Was machen die Menschen dann? Schreiben Sie zwei Sätze auf Deutsch!"
eh = 140 + 30.53 * len(wrap(etvous, "serif", False, 21.5, CW - 44)) + 29 * (len(wrap("O teu país tem um dia de silêncio? O que fazem as pessoas? Escreve duas frases em alemão!", "sans", False, 20, CW - 44)) - 1)
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE?　E tu?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "O teu país tem um dia de silêncio? O que fazem as pessoas? Escreve duas frases em alemão!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 box3 ends", ey3 + eh)
zew = ["Erster Advent — 29. November: Beginn der Adventszeit.",
       "Buß- und Bettag — 18. November: Nachdenken und Beten.",
       "Totensonntag — 22. November: Gedenken an die Verstorbenen."]
sy3 = ey3 + eh + 26
sh = 45 + 33 * len(zew) + 30.53 * sum(len(wrap(t, "serif", False, 21.5, CW - 44)) for t in zew)
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "DIE STILLE WOCHE　Tranquila", 24, "sans", True, OLIVE)
yy3 += 52
for t in zew:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P2 col3 box4 ends", sy3 + sh)

# ---- Rechnen wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "RECHNEN WIR MAL　Vamos calcular", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Die Daten der Woche　As datas da semana", 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 58
for line in [
    ("18. November + 11 Tage", "= 29. November: der erste Advent"),
    ("15. November + 7 Tage", "= 22. November: Totensonntag"),
    ("16. November + 6 Tage", "= 22. November: Totensonntag"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 360, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 36
p.para(1090, ly - 108 + 22, "Achtung: Am Totensonntag bleiben die Weihnachtsmärkte in Köln geschlossen. Wer in dieser Woche nach Köln fährt, sollte den Montag oder Dienstag nehmen: Da sind die Märkte geöffnet!", 20.5, "serif", False, INK, RIGHT - 1090, 1.42)
p.para(1090, ly - 108 + 22 + 4 * 29.1 + 10, "Nota: os mercados fecham no Totensonntag; vem na segunda ou na terça.", 20, "sans", False, GREY, RIGHT - 1090, 1.42)

# ---- P2 exercises ----
ey = dy + 240  # W47 D1: was dy+282; Rechnen note ink ends ~1778, hline at ey-12=1794 clears it
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ÜBUNGEN　Exercícios da p. 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na p. 8　Os níveis misturam-se: procura pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　WELCHES DATUM?", 25)
e.bridge("Lê o artigo da p. 2 e completa as datas.")
e.ex("A2", "completar", "18. November", "Dia de arrependimento e oração, 18 nov.",
     "Der Buß- und Bettag ist am ___.", instr="Completa", size=22, gap=6)
e.ex("A2", "completar", "22. November", "Totensonntag: 22 nov.",
     "Der Totensonntag ist am ___.", instr="Completa", size=22, gap=6)
e.ex("A2", "completar", "29. November", "Primeiro Advento: 29 nov.",
     "Der erste Advent ist am ___.", instr="Completa", size=22, gap=6)
e.ex("A2", "completar", "Mittwoch", "18 de novembro, quarta-feira",
     "Der 18. November 2026 ist ein ___.", instr="Completa", size=22, gap=6)
e.ex("A2", "completar", "Sachsen", "Só a Saxónia",
     "Nur in ___ ist der Buß- und Bettag ein Feiertag.", instr="Completa", size=22, gap=6)
e.head("B　DAS PERFEKT", 25)
e.bridge("Reescreve no Perfekt (pretérito perfeito).")
e.ex("A2", "transformação", "Der Buß- und Bettag ist fast überall abgeschafft worden.", "abschaffen → abgeschafft worden",
     "Der Buß- und Bettag (abschaffen) fast überall. → ___", instr="Reescreve", size=22, gap=6)
e.ex("A2", "transformação", "Die Schulen in Bayern sind geschlossen geblieben.", "bleiben → geblieben",
     "Die Schulen in Bayern (bleiben) geschlossen. → ___", instr="Reescreve", size=22, gap=6)
e.ex("A2", "transformação", "Viele Menschen sind in die Kirche gegangen.", "gehen → gegangen",
     "Viele Menschen (gehen) in die Kirche. → ___", instr="Reescreve", size=22, gap=6)
e.ex("B1", "transformação", "Sachsen hat den Feiertag behalten.", "behalten → behalten",
     "Sachsen (behalten) den Feiertag. → ___", instr="Reescreve", size=22, gap=6)
e.ex("B1", "transformação", "Die Märkte sind am Totensonntag geschlossen geblieben.", "bleiben → geblieben",
     "Die Märkte (bleiben) am Totensonntag geschlossen. → ___", instr="Reescreve", size=22, gap=6)
e.head("C　LESEVERSTEHEN", 25)
e.bridge("Lê a p. 2 e escolhe a resposta certa.")
e.ex("A2", "escolha múltipla", "B", "Sem aulas na Baviera",
     "Was ist in Bayern am Buß- und Bettag? A. Alle haben frei. · B. Kein Unterricht, Eltern arbeiten. · C. Die Geschäfte sind zu.", size=22, gap=6)
e.ex("A2", "escolha múltipla", "B", "Abolido em 1995",
     "Wann wurde der Buß- und Bettag fast überall abgeschafft? A. 1922 · B. 1995 · C. 2026", size=22, gap=6)
e.ex("A2", "escolha múltipla", "A", "Sem dança na Saxónia, das 3 às 24 h",
     "Was ist in Sachsen am Buß- und Bettag verboten? A. Tanzveranstaltungen von 3 bis 24 Uhr · B. Das Lesen · C. Der Schulunterricht", size=22, gap=6)
e.ex("A2", "escolha múltipla", "B", "Último domingo do ano litúrgico",
     "Was ist der Totensonntag? A. der erste Sonntag · B. der letzte Sonntag · C. ein Feiertag in ganz Deutschland", size=22, gap=6)
e.head("D　DIE WÖRTER", 25)
e.match_set("A2", "associar palavras",
            ["der Buß- und Bettag", "evangelisch", "still", "der Feiertag"],
            ["ruhig und leise, ohne Lärm",
             "der Tag, an dem man nicht arbeiten muss",
             "zur evangelischen Kirche gehörend",
             "der Tag zum Nachdenken und Beten"],
            ["d", "c", "a", "b"],
            ["Buß- und Bettag=arrependimento e oração d", "evangelisch=protestante c", "still=calmo a", "Feiertag=feriado b"],
            instr="Associa as palavras")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leben.svg")
print("P2 saved, exercises so far:", len(REG))
