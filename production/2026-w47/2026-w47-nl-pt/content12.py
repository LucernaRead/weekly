# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · VOORPAGINA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL.4", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "ELKE WEEK IN HET NEDERLANDS　TODAS AS SEMANAS EM NEERLANDÊS", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "WEEK VAN 16 TOT EN MET 22 NOVEMBER 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "De Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SEMANÁRIO NEERLANDÊS　VOL.4　ORANJE　SINTERKLAAS　PAKJESAVOND", 34, "serif", True, OLIVE, anchor="middle", spacing=0)
p.text(975, 372, "DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "VANAVOND IN BERLIJN!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Oranje speelt maandag tegen Duitsland — de beslissing in groep 2.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "Hoje à noite em Berlim: Países Baixos contra a Alemanha", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Esta semana: o jogo decisivo de Oranje contra a Alemanha — ver página 4", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "HET NIEUWS　MANCHETE", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Vanavond in Berlijn: Oranje tegen Duitsland", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Van de redactie van De Lucerna　Leesniveau: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland. De wedstrijd begint om 20:45 uur in het Olympiastadion en is live te zien op NPO 3. Het is de laatste wedstrijd in de groep — en de beslissing in groep 2.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. De nummers één en twee van de groep gaan naar de kwartfinales in maart 2027.")
f.para("Vrijdag speelden Oranje en Duitsland hun vijfde wedstrijd: Oranje thuis tegen Griekenland, in de Johan Cruijff ArenA in Amsterdam, en Duitsland uit in Belgrado tegen Servië. Maandagavond in Berlijn valt de beslissing: wie wint de groep?")
f.para("Afgelopen weekend kwam Sinterklaas aan in Nederland. Zaterdag 14 november was de landelijke intocht in Grave, aan de Maas in Noord-Brabant: rond 12:00 uur meerde de stoomboot aan bij de Maaskade, live op NPO 3. Een dag later, op zondag 15 november, was de intocht in Amsterdam: de 88e editie.")
f.para("Na de intocht begint de tijd van de schoen: kinderen zetten hun schoen bij de deur, met een wortel voor het paard en een verlanglijstje erin. Pakjesavond, de avond met de grote cadeaus, is dit jaar op zaterdag 5 december — over negentien dagen.")
f.bridge("Nota — de groepswinst vitória do grupo · de kwartfinale quartos de final · de intocht chegada · het verlanglijstje lista de desejos.")
f.box("DE WEEK IN CIJFERS　NÚMEROS", [  # D5: tsize 22 — title advance 411.8px > box 404.5 at 23pt
    ("16 — november: Duitsland – Nederland in Berlijn (16 nov.: Alemanha–Países Baixos)", "serif", False, INK, 20, 1.35),
    ("20:45 — de aftrap (20:45: pontapé inicial)", "serif", False, INK, 20, 1.35),
    ("8 — punten: Nederland en Griekenland bovenaan (8 pontos: empatados)", "serif", False, INK, 20, 1.35),
    ("5 — december: pakjesavond, over 19 dagen (5 dez.: Pakjesavond, em 19 dias)", "serif", False, INK, 20, 1.35),
], tsize=22)
f.head("NU JIJ　AGORA TU", 25)
f.ex("A2", "Completa a frase", "20:45", "Alemanha–Países Baixos: pontapé inicial segunda-feira às 20:45",
     "Duitsland – Nederland begint maandag om ___ uur.", size=19.5, gap=6)
f.ex("A2", "Completa a frase", "Berlijn", "O jogo é em Berlim",
     "Oranje speelt maandag in ___ tegen Duitsland.", size=19.5, gap=6)
f.ex("A2", "Completa a frase", "8", "Os Países Baixos e a Grécia têm ambos 8 pontos",
     "Nederland en Griekenland hebben allebei ___ punten.", size=19.5, gap=6)
f.ex("A2", "Completa a frase", "15", "A chegada a Amesterdão é no domingo, 15 de novembro",
     "De intocht in Amsterdam was op zondag ___ november.", size=19.5, gap=6)
f.ex("A2", "Completa a frase", "5", "O Pakjesavond é a 5 de dezembro",
     "Pakjesavond is op zaterdag ___ december.", size=19.5, gap=6)
f.ex("B1", "Completa a frase", "maakte", "Os Países Baixos marcaram 7 golos",
     "Nederland ___ (maken) 7 doelpunten in vier wedstrijden.", size=19.5, gap=6)
f.end_report()

# ---- deze week agenda (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "DEZE WEEK", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "　ESTA SEMANA", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "Agenda van de week　OS COMPROMISSOS", 19, "sans", False, GREY)
gt = [
    ("MA 16", "Oranje – Duitsland, 20:45"),
    ("ZA 21", "Eredivisie: NEC – PSV"),
    ("ZA 21", "Feyenoord – Excelsior"),
    ("ZO 22", "Ajax – ADO Den Haag"),
    ("ZO 22", "Robinson, 20:00 uur"),
]
byy = gy + 150
for i, (lab, vol) in enumerate(gt):
    p.text(gx + 22, byy + 22, lab, 20, "serif", True, OLIVE)
    p.text(gx + 110, byy + 22, vol, 20, "serif", False, INK)
    byy += 62
p.text(gx + 22, byy + 16, "Alle data en tijden staan ook", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "in de artikelen op pagina 2–5.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Datas e horas: artigos das páginas 2 a 5.", 19, "sans", False, GREY)

# ---- inhoud (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "IN DEZE EDITIE　NESTA EDIÇÃO", 22, "sans", True, OLIVE)  # D5: 24 -> 22 — advance 421.6px > box 400.5
som = [
    ("Pag. 2", "De schoen en pakjesavond", "A2"),
    ("Pag. 3", "Sinterklaas is er!", "A2→B1"),
    ("Pag. 4", "Oranje: de beslissing", "B1"),
    ("Pag. 5", "Robinson en surprises", "B1"),
    ("Pag. 6", "Oud feest, nieuwe wensen", "B2"),
    ("Pag. 7", "Drie gereedschappen", "A2→B2"),
    ("Pag. 8", "Oefeningen en antwoorden", "alle"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- woord van de week (col 3) ----
my = 1652
p.text(gx, my + 24, "HET WOORD VAN DE WEEK", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "«de groepswinst»", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "de eerste plaats in de groep: als nummer één naar de kwartfinales.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 26, "«Vitória do grupo»: primeiro lugar do grupo, direto aos quartos de final.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1853, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "westertoren.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "De Westertoren in Amsterdam. Zondag 15 november voer Sinterklaas over de Amstel naar het Scheepvaartmuseum en reed hij daarna te paard naar het Leidseplein. (Pagina 3)",
        "Foto: Wim van Rossem / Anefo, Nationaal Archief — CC0")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-extra")
f2.head("NA DE INTOCHT: DE SCHOEN", 25)
f2.para("Na de intocht mag de schoen: kinderen zetten 's avonds hun schoen bij de deur, met een wortel voor het paard en een verlanglijstje erin. 's Nachts komt Sinterklaas met een klein cadeautje.", 22.5)
f2.para("Pakjesavond, de avond met de grote cadeaus — en met surprises en gedichten — is dit jaar op zaterdag 5 december.", 22.5)
f2.end_report()
# col 3 IN HET KORT
bx = COLX[3]
p.rect(bx, 1874, CW, 430, fill=BOX)
p.text(bx + 22, 1914, "IN HET KORT　EM RESUMO", 24, "sans", True, OLIVE)
brefs = [
    ("ORANJE · P.4", "Maandag in Berlijn tegen Duitsland, 20:45 uur, NPO 3."),
    ("SINTERKLAAS · P.3", "Zaterdag intocht in Grave; zondag de 88e intocht in Amsterdam."),
    ("EREDIVISIE · P.4", "Zaterdag 21 november: NEC – PSV en Feyenoord – Excelsior."),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz bliksem ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "BLIKSEMQUIZ　QUESTIONÁRIO RELÂMPAGO", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Lê a primeira página e escolhe a resposta certa　Respostas na página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Escolha múltipla", "B", "Alemanha–Países Baixos: pontapé inicial segunda-feira às 20:45",
      "Duitsland – Nederland begint om... A. 18:00 uur · B. 20:45 uur · C. 12:00 uur", size=21)
qf.ex("A2", "Escolha múltipla", "B", "O jogo é no Olympiastadion de Berlim",
      "Oranje speelt maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=21)
qf.ex("A2", "Escolha múltipla", "C", "Os Países Baixos e a Grécia têm ambos 8 pontos",
      "Nederland en Griekenland hebben... A. 5 punten · B. 7 punten · C. 8 punten", size=21)
qf.ex("A2", "Escolha múltipla", "B", "O Pakjesavond é no sábado, 5 de dezembro",
      "Pakjesavond is op... A. 11 november · B. 5 december · C. 15 november", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-voorpagina.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · LEVEN (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("LEVEN　VIDA", "De Lucerna", "NIVEAU A2　De schoen en pakjesavond　O sapato e Pakjesavond")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("De schoen staat klaar: aftellen naar pakjesavond", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2")
f.para("Sinterklaas is er! Afgelopen weekend kwam hij aan in Grave en in Amsterdam. Nu begint de tijd van de schoen: kinderen zetten 's avonds hun schoen bij de deur, met een wortel voor het paard en een tekening of een verlanglijstje erin. 's Nachts komt Sinterklaas met een klein cadeautje.")
f.para("De wortel is voor het paard van Sinterklaas, Ozosnel. De tekening is voor Sinterklaas zelf. En het verlanglijstje? Dat is een lijst met wensen: wat wil je het liefst hebben? Schrijf het in het Nederlands — Sinterklaas leest Nederlands.")
f.para("Vorige week woensdag was het Sint-Maarten: kinderen liepen met lampionnen zingend langs de deuren. Nu is het licht van de lampion doorgegeven aan de schoen: twee feesten van licht en geven, in twee weken.")
f.para("Op zaterdag 5 december is het pakjesavond: de avond met de grote cadeaus. Veel families maken dan een surprise: een cadeau in een gekke verpakking, met een gedicht erbij. Een gedicht is een klein versje — grappig, lief of een beetje plagend. Nog negentien dagen tot pakjesavond: tijd om te knutselen en te dichten.")
f.para("En het Sinterklaasjournaal? Dat is er elke dag om 18:00 uur op NPO Zapp. Kinderen volgen hoe Sinterklaas en zijn Pieten zich voorbereiden op pakjesavond.")
f.head("DRIE DINGEN VOOR 5 DECEMBER", 23)  # D5: 25pt -> 23pt — Newsreader SemiBold advance 451.8px > col 422.5 (HEAD TOO WIDE); 23pt = 415.6px. Text unchanged.
f.para("Eén: zet je schoen, met een wortel en een verlanglijstje. Twee: schrijf een gedicht — kort is ook goed. Drie: maak een surprise: verstop het cadeau in iets geks.")
f.box("ZO ONTHOUD JE HET　LEMBRA-TE", [  # D5: tsize 21 — title advance 437.2px > box 404.5 at 23pt
    ("«De schoen staat klaar: een wortel voor het paard, een lijstje voor de Sint.» En pakjesavond is op 5 december.", "serif", False, INK, 21.5, 1.4),
], tsize=21)
f.gloss("de schoen sapato · de wortel cenoura · het verlanglijstje lista de desejos · de surprise presente disfarçado · het gedicht poema.")
f.end_report()

# col 3: image + facts + en jij (sequential, measured)
ix = COLX[3]
image(p, "sint-oud.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Sinterklaas te paard in Amsterdam (oude foto uit het archief). Zondag 15 november reed hij na de intocht te paard door de stad naar het Leidseplein.",
              "Foto: Anefo, Nationaal Archief — CC0")
facts = ["Pakjesavond: zaterdag 5 december, over negentien dagen.",
         "De schoen: 's avonds bij de deur, met een wortel en een verlanglijstje.",
         "Een surprise is een cadeau in een gekke verpakking, met een gedicht erbij."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 40
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "WIST JE DAT?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Zet jij je schoen met een wortel en een verlanglijstje, of schrijf je liever een gedicht voor pakjesavond? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie: de mooiste komen in VOL.5 (pagina 7, «Brieven van lezers»)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Vais pôr o sapato com uma lista de desejos, ou preferes escrever um poema para o Pakjesavond? Escreve duas frases em neerlandês e envia-as à redação.", "sans", False, 20, CW - 44)) * 29 + 22
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　E TU?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Vais pôr o sapato com uma lista de desejos, ou preferes escrever um poema para o Pakjesavond? Escreve duas frases em neerlandês e envia-as à redação.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- pakjesavond row: 4 boxes ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "PAKJESAVOND IN VIER WOORDEN　PAKJESAVOND EM QUATRO PALAVRAS", 27, "sans", True, OLIVE)  # D5: 28 -> 27 — title overlapped right-anchored subtitle by 11.8px
p.text(RIGHT, dy + 28, "Wat hoort bij pakjesavond?　Que palavras pertencem ao Pakjesavond?", 20, "sans", False, GREY, anchor="end")
codes = [
    ("SCHOEN", "de schoen", "Posto à noite junto à porta, à espera de Sinterklaas"),
    ("WORTEL", "voor het paard", "A cenoura é para o cavalo de Sinterklaas"),
    ("LIJSTJE", "het verlanglijstje", "Lista de desejos: escreve o que mais desejas"),
    ("GEDICHT", "het versje", "Poeminha: engraçado, carinhoso ou um pouco brincalhão"),
]
for i, (t, lab, cn) in enumerate(codes):
    bx = COLX[i]
    p.rect(bx, dy + 52, CW, 150, fill=BOX)
    p.text(bx + 22, dy + 110, t, 32, "serif", True, OLIVE)
    lx = bx + 22 + text_w(t, "serif", True, 32) + 14
    lw = bx + CW - 22 - lx
    yy = p.para(lx, dy + 92, lab, 21.5, "serif", False, INK, lw, 1.36)
    p.para(lx, yy + 20, cn, 19, "sans", False, GREY, lw, 1.3)
p.para(MX, dy + 234, "Let op: schrijf je gedicht in het Nederlands — Sinterklaas leest Nederlands. Meer over de intocht lees je op pagina 3.", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　EXERCÍCIOS DA PÁGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　Os níveis estão misturados; procura o teu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("Lê o artigo da página 2 e escolhe a resposta certa.")
e.ex("A2", "Escolha múltipla", "B", "Sinterklaas chegou a Grave e a Amesterdão no fim de semana passado",
     "Sinterklaas kwam afgelopen weekend aan in... A. Utrecht · B. Grave en Amsterdam · C. Spanje", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "B", "A cenoura no sapato é para o cavalo",
     "De wortel in de schoen is voor... A. Sinterklaas · B. het paard · C. de Piet", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "C", "O Pakjesavond é a 5 de dezembro",
     "Pakjesavond is op... A. 11 november · B. 15 november · C. 5 december", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "A", "Um surprise é um presente disfarçado",
     "Een surprise is... A. een cadeau in een gekke verpakking · B. een liedje · C. een lampion", size=20, gap=8)
e.ex("A2", "Escolha múltipla", "B", "O noticiário de Sinterklaas é todos os dias às 18:00",
     "Het Sinterklaasjournaal is elke dag om... A. 12:00 uur · B. 18:00 uur · C. 20:00 uur", size=20, gap=8)
e.head("B　WOORDEN", 25)
e.bridge("Completa com as palavras da página 2.")
e.ex("A2", "Completa a frase", "schoen", "schoen = sapato",
     "Kinderen zetten hun ___ bij de deur.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completa a frase", "wortel", "wortel = cenoura",
     "In de schoen zit een ___ voor het paard.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completa a frase", "verlanglijstje", "verlanglijstje = lista de desejos",
     "Op het ___ staan drie wensen.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completa a frase", "gedicht", "gedicht = poema",
     "Bij de surprise hoort een ___.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completa a frase", "5", "O Pakjesavond é a 5 de dezembro",
     "Pakjesavond is op ___ december.", instr="Complete", size=20, gap=8)
e.head("C　SCHOEN EN GEDICHT", 25)
e.bridge("Completa com os números e nomes da página 2.")
e.ex("A2", "Completa a frase", "Ozosnel", "O cavalo de Sinterklaas chama-se Ozosnel",
     "Het paard van Sinterklaas heet ___.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completa a frase", "19", "De 16 de novembro a 5 de dezembro são 19 dias",
     "Van 16 november tot 5 december: ___ dagen.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completa a frase", "18:00", "O noticiário de Sinterklaas às 18:00",
     "Het Sinterklaasjournaal is om ___ uur.", instr="Complete", size=20, gap=8)
e.ex("A2", "Completa a frase", "december", "O Pakjesavond é em dezembro",
     "Pakjesavond is in ___.", instr="Complete", size=20, gap=8)
e.head("D　WOORDEN", 25)
e.match_set("A2", "Relaciona as palavras",
            ["de schoen", "de wortel", "het verlanglijstje", "het gedicht"],
            ["een lijst met wensen voor Sinterklaas",
             "een klein versje bij een cadeau",
             "eten voor Sinterklaas' paard",
             "die staat 's avonds bij de deur"],
            ["d", "c", "a", "b"],
            ["schoen = sapato d", "wortel = cenoura c", "verlanglijstje = lista de desejos a", "gedicht = poema b"],
            instr="Ligue palavra-significado")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-leven.svg")
print("P2 saved, exercises so far:", len(REG))
