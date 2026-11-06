# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-de-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH / LIBRARIES (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUGEND · Jovens", "Die Lucerna", "LEVEL B1 · Ferien & Bibliotheken · Férias e bibliotecas")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P5-main")
f.title("Ferien ohne Schule: Die Stadt gehört den Lesern", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B1")
f.para("Ferien — und die Schule ist zu. Was machen die Kinder und Jugendlichen in Berlin? In dieser Woche gehört die Stadt den Leserinnen und Lesern: Die Berliner Bibliotheken machen eine ganze Aktionswoche, denn am Samstag ist der Tag der Bibliotheken.")
f.para("Es gibt Bibliotheks-Bingo, eine Wand mit Lieblingsbüchern und „Book-Blind-Dates“. Wie funktioniert ein Book-Blind-Date? Das Buch ist eingepackt, man sieht nur drei Stichworte. Man wählt ein Buch, ohne es zu kennen. Erst zu Hause packt man es aus — eine Überraschung wie ein Geschenk.")
f.para("Warum der 24. Oktober? Das Datum erinnert an Karl Preusker: Am 24. Oktober 1828 gründete er in Großenhain in Sachsen eine Bibliothek — aus ihr wurde die erste öffentliche Bibliothek Deutschlands. Seit 1995 feiert das Land am 24. Oktober den Tag der Bibliotheken; Schirmherr war damals Bundespräsident Richard von Weizsäcker. Mehr als 8 000 Bibliotheken gibt es heute in Deutschland.")
f.para("Und Halloween? Die Vorbereitungen laufen: Im Zoo Osnabrück geben Kinder ihre geschnitzten Kürbisse ab (Seite 3), und die Discounter verkaufen schon Kostüme. Wer noch ein Kostüm sucht, muss sich beeilen — am Samstag, dem 31. Oktober, ist die große Nacht.")
f.para("Für viele Familien sind die Herbstferien auch Reisezeit. Aber nicht alle fahren weg: Bibliotheken, Zoos und Erlebnisparks machen den Herbst zu Hause zum Programm. Unser Tipp für den Samstag: erst in die Bibliothek, dann einen Kürbis schnitzen!")
f.gloss("die Aktionswoche = a semana de atividades · das Stichwort = a palavra-chave · eingepackt = embrulhado · der Schirmherr = o patrono de honra · sich beeilen = apressar-se.")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Quando foi a última vez que você foi a uma biblioteca? E que livro escolheria para um «encontro às cegas»? Escreva duas frases em alemão!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "UND SIE? · E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Quando foi a última vez que você foi a uma biblioteca? E que livro escolheria para um «encontro às cegas»? Escreva duas frases em alemão!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)


# ---- Samstag-Plan wide box (cols 0-2) ----
sx, swd = span_x(0, 2)
p.rect(sx, 1120, swd, 300, fill=BOX, stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "DER SAMSTAG-PLAN DER REDAKTION · O plano de sábado da redação", 24, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "ÜBUNGEN · Exercícios da página 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · Os níveis se misturam: procure cada resposta pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · LESEVERSTEHEN", 25)
e.expl("Leia o artigo da página 5 e responda.")
e.ex("B1", "Escolha múltipla", "B", "a semana de atividades é pelo Dia das Bibliotecas",
     "Die Aktionswoche gibt es, weil... A. die Schule neu ist · B. der Tag der Bibliotheken ist · C. Halloween ausfällt", size=20, gap=8)
e.ex("B1", "Escolha múltipla", "B", "no encontro às cegas com um livro, veem-se só três palavras-chave",
     "Bei einem Book-Blind-Date sieht man nur... A. den Preis · B. drei Stichworte · C. den Autor", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "A", "o Dia das Bibliotecas é 24 de outubro",
     "Der Tag der Bibliotheken ist am... A. 24. Oktober · B. 31. Oktober · C. 19. Oktober", size=20, gap=8)
e.ex("B1", "Escolha múltipla", "B", "Preusker fundou sua biblioteca em Großenhain em 1828",
     "Karl Preusker gründete seine Bibliothek im Jahr... A. 1517 · B. 1828 · C. 1995", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "B", "31 de outubro é Halloween",
     "Am 31. Oktober ist... A. der Schulanfang · B. Halloween · C. der Bibliothekstag", size=20, gap=8)
e.head("B · WÖRTER AUS DEM TEXT", 25)
e.expl("Complete com as palavras do quadro.")
e.para("Bibliothek · Stichworte · Überraschung · eingepackt · Lieblingsbuch · leihen", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Completar frases", "Stichworten", "nach drei + dativo plural: Stichworten",
     "Man wählt ein Buch nach drei ___.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completar frases", "eingepackt", "o livro está embrulhado",
     "Das Buch ist ___ — man sieht es nicht.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completar frases", "Überraschung", "uma surpresa como um presente",
     "Ein Blind Date mit einem Buch ist eine ___.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completar frases", "Lieblingsbuch", "meu livro favorito está na parede",
     "An der Wand hängt mein ___.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completar frases", "Bibliothek", "na biblioteca emprestam-se livros",
     "In der ___ kann man Bücher leihen.", instr="Complete", size=20, gap=8)
e.ex("B1", "Completar frases", "leihen", "möchte + infinitivo no fim",
     "Ich möchte dieses Buch ___ — für drei Wochen.", instr="Complete", size=20, gap=8)
e.head("C · SÄTZE MIT «WEIL»", 25)
e.expl("Junte as frases com weil (verbo no fim).")
e.ex("B1", "Transformação de frases", "Die Kinder freuen sich, weil Ferien sind.", "com weil o verbo vai para o fim",
     "Die Kinder freuen sich. Es sind Ferien. (weil) → ___", instr="Reescreva", size=20, gap=8)
e.ex("B1", "Transformação de frases", "Die Bibliotheken machen eine Aktionswoche, weil es der Tag der Bibliotheken ist.", "ist se desloca para o fim",
     "Die Bibliotheken machen eine Aktionswoche. Es ist der Tag der Bibliotheken. (weil) → ___", instr="Reescreva", size=20, gap=8)
e.ex("B1", "Transformação de frases", "Er bleibt zu Hause, weil er ein Buch lesen will.", "will vai para o fim",
     "Er bleibt zu Hause. Er will ein Buch lesen. (weil) → ___", instr="Reescreva", size=20, gap=8)
e.ex("B1", "Transformação de frases", "Sie kauft ein Kostüm, weil Halloween am 31. Oktober ist.", "ist vai para o fim",
     "Sie kauft ein Kostüm. Halloween ist am 31. Oktober. (weil) → ___", instr="Reescreva", size=20, gap=8)
e.head("D · RICHTIG ODER FALSCH?", 25)
e.expl("Verdadeiro ou falso?")
e.ex("A2", "Verdadeiro ou falso", "Richtig", "mais de 8 000 bibliotecas na Alemanha",
     "Mehr als 8 000 Bibliotheken gibt es in Deutschland. Richtig oder falsch?", instr="V ou F", size=20, gap=8)
e.ex("B1", "Verdadeiro ou falso", "Falsch", "o Dia das Bibliotecas existe desde 1995",
     "Der Tag der Bibliotheken ist ein neuer Tag aus dem Jahr 2026. Richtig oder falsch?", instr="V ou F", size=20, gap=8)
e.ex("A2", "Verdadeiro ou falso", "Richtig", "a semana de atividades de Berlim vai até sábado",
     "Die Aktionswoche in Berlin dauert bis Samstag. Richtig oder falsch?", instr="V ou F", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jugend.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERTIEFUNG · Leitura aprofundada", "Die Lucerna", "LEVEL B2 · Die große Debatte · O grande debate")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P6-main")
f.title("Soll die Zeitumstellung abgeschafft werden?", 37)
f.byline("Von der Lucerna-Redaktion · Leseniveau: B2")
f.para("Zweimal im Jahr steht die EU vor derselben Frage: vor oder zurück? An diesem Sonntag ist es wieder so weit. Doch warum gibt es die Sommerzeit überhaupt — und warum bleibt sie, obwohl so viele Menschen sie nicht mehr wollen?")
f.para("Deutschland stellte die Uhren zum ersten Mal am 30. April 1916 um — mitten im Ersten Weltkrieg sollte Tageslicht Energie sparen. Nach dem Zweiten Weltkrieg endete die Praxis 1950. Erst am 6. April 1980 führten beide deutsche Staaten die Sommerzeit wieder ein; seitdem gilt sie ohne Unterbrechung.")
f.para("Die Argumente sind bekannt: Die Freunde der Sommerzeit lieben die hellen Abende im Sommer. Die Kritiker sagen, der Körper leide unter dem Wechsel — und der Nutzen für die Energie sei heute klein.")
f.para("Im Sommer 2018 fragte die EU-Kommission die Menschen in Europa: Soll die Zeitumstellung enden? 4,6 Millionen Antworten kamen zurück — so viele wie noch nie bei einer solchen Befragung. 84 Prozent von ihnen wollten die Umstellung abschaffen. Im März 2019 stimmte das Europäische Parlament mit 410 zu 192 Stimmen dafür, die Umstellung ab 2021 zu beenden. Aber die Regierungen der Mitgliedstaaten wurden sich nicht einig — und so blieb alles, wie es ist. Die Länder konnten sich nicht entscheiden, ob sie für immer Sommerzeit oder Winterzeit wollen.")
f.para("Und nun? An diesem Sonntag genießen wir erst einmal die geschenkte Stunde. Die Debatte kommt bestimmt wieder — spätestens im März, wenn die Uhren wieder vorgestellt werden.")
f.gloss("abschaffen = abolir · die Befragung = a pesquisa · der Mitgliedstaat = o Estado-membro (plural: die Mitgliedstaaten) · sich einig werden = entrar em acordo · leiden = sofrer.")
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
p.text(ix + 22, yy3 + 26, "DIE ZEITLINIE · A linha do tempo", 24, "sans", True, OLIVE)
yy3 += 52
for yr, t in tl:
    p.text(ix + 22, yy3 + 21, yr, 21, "sans", True, BRICK)
    yy3 = p.para(ix + 92, yy3 + 20.5, t, 20.5, "serif", False, INK, CW - 114, 1.42) + 10
hy3 = 200 + tlh + 26
health = "Die Grippezeit kommt. Die STIKO empfiehlt die Impfung besonders für Menschen ab 60 Jahren, für Schwangere ab dem zweiten Drittel, für Menschen mit chronischen Krankheiten und für alle, die in Pflege und Medizin arbeiten. Der Schutz baut sich in 10 bis 14 Tagen auf. Impfen lassen kann man sich beim Hausarzt und in Apotheken (ab 18 Jahren)."
hh = 62 + len(wrap(health, "serif", False, 21, CW - 44)) * 30 + 10 + len(wrap("A gripe vem aí: a STIKO recomenda vacinar maiores de 60, gestantes (desde o 2º terço), doentes crônicos e profissionais de saúde. Proteção: 10–14 dias.", "sans", False, 19.5, CW - 44)) * 28 + 20
p.rect(ix, hy3, CW, hh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = hy3 + 16
p.text(ix + 22, yy3 + 26, "GESUND DURCH DEN HERBST", 22.5, "sans", True, OLIVE)
yy3 += 50
yy3 = p.para(ix + 22, yy3 + 21, health, 21, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "A gripe vem aí: a STIKO recomenda vacinar maiores de 60, gestantes (desde o 2º terço), doentes crônicos e profissionais de saúde. Proteção: 10–14 dias.", 19.5, "sans", False, GREY, CW - 44, 1.42)
print("P6 col3 ends", hy3 + hh)


# ---- Pro & Contra wide box (cols 0-2) ----
sx, swd = span_x(0, 2)
p.rect(sx, 1120, swd, 252, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(sx + 24, 1162, "PRO & CONTRA · Prós e contras — die Argumente der Debatte", 24, "sans", True, OLIVE)
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
p.text(MX, cy + 28, "WAS MACHEN DIE DEUTSCHEN MIT DER EXTRA STUNDE? · O que os alemães fazem com a hora extra?", 26, "sans", True, OLIVE)
bars = [("länger schlafen", 46, "dormir mais"), ("Zeit mit der Familie", 22, "com a família"),
        ("ein Buch lesen", 18, "ler um livro"), ("Sport machen", 14, "fazer esporte")]
byy = cy + 58
for lab, v, zh in bars:
    p.text(MX, byy + 26, lab, 22, "serif", True, INK)
    p.text(MX + 330, byy + 26, zh, 20, "sans", False, GREY)
    p.rect(MX + 470, byy + 4, v * 24, 30, fill=OLIVE)
    p.text(MX + 470 + v * 24 + 16, byy + 26, f"{v} %", 22, "sans", True, BRICK)
    byy += 52
p.text(MX, byy + 22, "ÜBUNGSDATEN · DADOS DE PRÁTICA — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Dados de prática da redação, não uma pesquisa real.)", 19.5, "sans", False, GREY)

# ---- P6 exercises ----
ey = 1808
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ÜBUNGEN · Exercícios da página 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · Os níveis se misturam: procure cada resposta pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · DAS DIAGRAMM LESEN", 25, gap=9)
e.expl("Veja o gráfico de prática e responda.")
e.ex("B1", "Escolha múltipla", "B", "46% dormem mais",
     "Wie viele Prozent schlafen länger? A. 22 % · B. 46 % · C. 18 %", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "C", "segundo lugar: com a família, 22%",
     "Was ist die zweitliebste Aktivität? A. Sport · B. ein Buch lesen · C. Zeit mit der Familie", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "B", "46 + 18 = 64",
     "Länger schlafen und ein Buch lesen zusammen sind... A. 60 % · B. 64 % · C. 68 %", size=20, gap=7)
e.ex("B2", "Escolha múltipla", "B", "família + leitura = 40% > esporte 14%",
     "Welche Gruppe ist größer? A. Sport allein · B. Familie und Lesen zusammen · C. beide gleich", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "A", "esporte: 14%",
     "Wie viele Prozent machen Sport? A. 14 % · B. 18 % · C. 22 %", size=20, gap=7)
e.ex("B2", "Escolha múltipla", "B", "46+22+18+14=100",
     "Die vier Zahlen zusammen ergeben... A. 90 % · B. 100 % · C. 110 %", size=20, gap=7)
e.head("B · LESEVERSTEHEN (B2)", 25, gap=9)
e.expl("Leia o texto da página 6 e responda.")
e.ex("B2", "Escolha múltipla", "B", "a primeira vez: 30 de abril de 1916",
     "Wann stellte Deutschland die Uhren zum ersten Mal um? A. 1950 · B. 1916 · C. 1980", size=20, gap=7)
e.ex("B2", "Escolha múltipla", "C", "410 votos contra 192 a favor de abolir",
     "Wie stimmte das EU-Parlament 2019? A. 192 : 410 dagegen · B. einstimmig dafür · C. 410 : 192 dafür", size=20, gap=7)
e.ex("B2", "Escolha múltipla", "B", "os governos dos Estados-membros não entraram em acordo",
     "Warum blieb die Umstellung? A. Die Bürger wollten sie. · B. Die Regierungen wurden sich nicht einig. · C. Das Parlament sagte Nein.", size=20, gap=7)
e.ex("B1", "Escolha múltipla", "A", "4,6 milhões de respostas",
     "Wie viele Antworten kamen 2018 zurück? A. 4,6 Millionen · B. 460 000 · C. 84 Millionen", size=20, gap=7)
e.head("C · GRAMMATIK", 25, gap=9)
e.expl("Complete com a forma entre parênteses.")
e.ex("B2", "Completar frases", "werden", "passiva: werden + Partizip II",
     "Die Uhren ___ (werden) am Sonntag umgestellt.", instr="Complete", size=20, gap=7)
e.ex("B2", "Completar frases", "ob", "ob introduz uma pergunta indireta",
     "Die Länder wissen nicht, ___ sie Sommerzeit oder Winterzeit wollen.", instr="Complete", size=20, gap=7)
e.ex("B1", "Completar frases", "abschaffen", "wollen + infinitivo no fim",
     "84 Prozent wollten die Umstellung ___. (abschaffen)", instr="Complete", size=20, gap=7)
e.ex("B2", "Completar frases", "stimmte", "stimmen no passado: stimmte",
     "Im März 2019 ___ das Parlament für das Ende. (stimmen)", instr="Complete", size=20, gap=7)
e.head("D · WÖRTER DER DEBATTE", 25, gap=9)
e.expl("Complete com as palavras do quadro.")
e.para("Umstellung · Mehrheit · abschaffen · Mitgliedstaaten", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Completar frases", "Umstellung", "Umstellung duas vezes por ano",
     "Die ___ findet zweimal im Jahr statt.", instr="Complete", size=20, gap=7)
e.ex("B2", "Completar frases", "Mehrheit", "84% é uma maioria clara",
     "84 Prozent sind eine klare ___.", instr="Complete", size=20, gap=7)
e.ex("B1", "Completar frases", "abschaffen", "wollen + abschaffen",
     "Viele Menschen wollen die Umstellung ___.", instr="Complete", size=20, gap=7)
e.ex("B2", "Completar frases", "Mitgliedstaaten", "os governos dos Estados-membros não entraram em acordo",
     "Die ___ der EU konnten sich nicht einigen.", instr="Complete", size=20, gap=7)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-vertiefung.svg")
print("P6 saved, exercises so far:", len(REG))
