# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　CULTUUR", "La Lucerna", "A2 → B1　Le sagre d'autunno　De herfst-eetfeesten")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Le sagre d'autunno: il tartufo bianco è il re", 32)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: A2 → B1")
f.para("In autunno, l'Italia mangia fuori casa. Nei paesi e nelle città è la stagione delle sagre: feste di piazza con i prodotti della terra. Il re della stagione è il tartufo bianco, il fungo più prezioso d'Italia.")
f.para("Ad Alba, in Piemonte, la Fiera del Tartufo Bianco è aperta dal 10 ottobre al 6 dicembre: quasi due mesi di mercati, profumi e piatti speciali. La fiera è iniziata sabato 10 ottobre e chiude domenica 6 dicembre.")
f.para("Questo fine settimana, sabato 24 e domenica 25 ottobre, Montaione, in Toscana, celebra la sua festa del tartufo. E a Bagolino, in Lombardia, il weekend è del formaggio Bagòss: un formaggio di montagna dal nome difficile e dal sapore forte.")
f.para("Sempre sabato 24 ottobre apre a Volterra Volterragusto, una festa dei sapori della Toscana. E ovunque, nelle piazze, si trovano le castagne arrosto: l'autunno italiano ha il profumo della castagna calda.")
f.gloss("il tartufo = truffel · la sagra = plaatselijk eetfeest · il profumo = geur · arrosto = geroosterd · la pittrice = schilderes.")
f.head("UNA GRANDE PITTRICE A FIRENZE", 22)
f.para("Mercoledì 21 ottobre apre a Firenze, al Museo degli Innocenti, la mostra «Artemisia Gentileschi a Firenze». Artemisia (1593–1656 circa) è una delle pittrici più famose del Seicento: le sue donne sono forti, coraggiose e vive.")
f.para("La mostra resta aperta fino al 4 aprile 2027 e presenta anche due opere di Caravaggio, il grande maestro della luce e dell'ombra. La pittura antica diventa notizia di questa settimana perché la mostra apre proprio mercoledì.")
f.end_report()

# col 3: truffle image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "tartufo.jpg", ix, 200, CW, 265)
cy3 = caption(p, ix, 465, CW, "Un tartufo bianco, il fungo più prezioso d'Italia. Ad Alba la fiera dura dal 10 ottobre al 6 dicembre; questo weekend, festa del tartufo anche a Montaione.",
              "Foto: Wikimedia Commons — dominio pubblico")
facts = ["Alba: la Fiera del Tartufo Bianco dura dal 10 ottobre al 6 dicembre.",
         "Montaione (Toscana): festa del tartufo, sabato 24 e domenica 25 ottobre.",
         "Bagolino (Lombardia): weekend del formaggio Bagòss, il 24 e 25 ottobre."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LE SAGRE DEL WEEKEND", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Qual è il piatto dell'autunno nel tuo paese? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Wat eten jullie in de herfst in jouw streek? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Wat eten jullie in de herfst in jouw streek? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
ay3 = ey3 + eh + 22
image(p, "artemisia.jpg", ix, ay3, CW, 165)
acy = caption(p, ix, ay3 + 165, CW, "Artemisia Gentileschi, «Giuditta decapita Oloferne» (versione di Napoli). A Firenze, la sua mostra apre mercoledì 21 ottobre.",
              "Foto: Wikimedia Commons — dominio pubblico")
print("P3 col3 ends", acy)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　OEFENINGEN VAN PAGINA 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus staan door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　COMPRENSIONE", 25)
e.expl("Lees het artikel op pagina 3 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "het witte-truffelfeest is in Alba",
     "La Fiera del Tartufo Bianco è a... A. Bagolino · B. Alba · C. Volterra", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "de truffelbeurs van Alba sluit op 6 december",
     "La fiera di Alba chiude... A. il 25 ottobre · B. il 1° novembre · C. il 6 dicembre", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "in Bagolino is het weekend van de Bagòss-kaas",
     "A Bagolino, il weekend è del... A. tartufo · B. formaggio Bagòss · C. vino", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Artemisia opent op woensdag 21 oktober",
     "La mostra su Artemisia apre... A. mercoledì 21 ottobre · B. sabato 24 ottobre · C. domenica 25 ottobre", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "de tentoonstelling heeft ook twee werken van Caravaggio",
     "Nella mostra ci sono anche opere di... A. Leonardo · B. Caravaggio · C. Michelangelo", size=20, gap=8)
e.head("B　LE PAROLE DEL TESTO", 25)
e.expl("Vul de woorden uit het kader in.")
e.para("tartufo · sagra · profumo · castagne · pittrice · formaggio", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Voltooi de zin", "tartufo", "tartufo = truffel",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "sagra", "sagra = plaatselijk eetfeest",
     "Una ___ è una festa di piazza con i prodotti della terra.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "profumo", "profumo = geur",
     "L'autunno ha il ___ della castagna calda.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "castagne", "castagne arrosto = geroosterde kastanjes",
     "Nelle piazze si trovano le ___ arrosto.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "pittrice", "pittrice = schilderes",
     "Artemisia è una grande ___ del Seicento.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "formaggio", "formaggio = kaas",
     "Il Bagòss è un ___ di montagna.", instr="Vul in", size=20, gap=8)
e.head("C　IL PASSATO PROSSIMO", 25)
e.expl("Vul aan met de passato prossimo; let op het hulpwerkwoord avere / essere.")
e.ex("B1", "Voltooi de zin", "è iniziata", "iniziare neemt essere; vrouwelijk: è iniziata",
     "La fiera ___ (iniziare) il 10 ottobre.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "abbiamo visitato", "visitare gebruikt avere: abbiamo visitato",
     "Noi ___ (visitare) la mostra di Artemisia.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "è andato", "andare gebruikt essere: è andato",
     "Marco ___ (andare) alla sagra sabato.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "hanno aperto", "aprire gebruikt avere: hanno aperto",
     "Le sagre ___ (aprire) il fine settimana.", instr="Vul in", size=20, gap=8)
e.head("D　COSTRUISCI LE FRASI", 25)
e.expl("Maak van de woorden correcte zinnen.")
e.ex("B1", "Zinnen bouwen", "La fiera è iniziata il 10 ottobre.", "essere + deelwoord + datum",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="Bouw de zin", size=20, gap=8)
e.ex("A2", "Zinnen bouwen", "A Bagolino il formaggio è il re.", "eerst plaats, dan onderwerp",
     "a Bagolino / il formaggio / è il re → ___", instr="Bouw de zin", size=20, gap=8)
e.ex("B1", "Zinnen bouwen", "La mostra resta aperta fino ad aprile.", "resta aperta blijft open",
     "la mostra / resta aperta / fino ad aprile → ___", instr="Bouw de zin", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　SPORT", "La Lucerna", "LIVELLO B1　La Serie A e l'Europa　De Serie A en Europa")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("L'ottava giornata: Napoli–Roma e Inter–Fiorentina", 32)
f.byline("Dalla redazione sportiva de La Lucerna　Livello di lettura: B1")
f.para("È una settimana di grande calcio. Mercoledì sera l'Inter gioca in Champions League a San Siro contro lo Shakhtar Donetsk (21:00), e giovedì l'Atalanta è in trasferta ad Amsterdam contro l'Ajax, in Conference League. Attenzione: queste partite si giocano dopo la chiusura del giornale — qui sono una presentazione, senza risultati.")
f.para("Poi arriva l'ottava giornata di Serie A, da venerdì 23 a domenica 25 ottobre. La partita più attesa è sabato 24 ottobre alle 18:00: Napoli–Roma, la grande sfida tra il Sud e la capitale.")
f.para("Domenica 25 ottobre, alle 12:30, l'Inter incontra la Fiorentina a San Siro. È una partita speciale: è la prima della domenica con l'ora solare. Chi guarda la partita a pranzo ha già dormito un'ora in più.")
f.para("E dall'America arriva il basket: la stagione NBA comincia questa settimana, e anche in Italia si cercano notizie su Spurs–Thunder, la partita di Wembanyama (ricerca in crescita su Google Trends in Italia, istantanea di martedì).")
f.gloss("la giornata = speelronde · la sfida = topper · la presentazione = voorbeschouwing · in trasferta = uitwedstrijd.")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Mercoledì 21 ottobre, 21:00 · Inter – Shakhtar Donetsk (Champions League, San Siro) — si gioca dopo la chiusura del giornale. Giovedì 22 ottobre · Ajax – Atalanta (Conference League, Amsterdam) — presentazione. Sabato 24 ottobre, 18:00 · Napoli – Roma (Serie A, 8ª giornata). Domenica 25 ottobre, 12:30 · Inter – Fiorentina (Serie A) — la prima partita con l'ora solare.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi questo fine settimana? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Welke wedstrijd kijk jij dit weekend? Schrijf twee zinnen Italiaans en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU?　EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Welke wedstrijd kijk jij dit weekend? Schrijf twee zinnen Italiaans en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DEL CALCIO　DE VOETBALWEEK", 26, "sans", True, OLIVE)
rows = [
    ("Mer 21.10", "21:00 · Champions", "Inter – Shakhtar Donetsk (San Siro) — partita della sera, dopo la chiusura del giornale"),
    ("Gio 22.10", "Conference League", "Ajax – Atalanta (Amsterdam) — presentazione, senza risultato"),
    ("Ven–Dom", "Serie A · 8ª giornata", "L'ottava giornata si gioca da venerdì 23 a domenica 25 ottobre"),
    ("Sab 24.10", "18:00 · Serie A", "Napoli – Roma — la partita più attesa del weekend"),
    ("Dom 25.10", "12:30 · Serie A", "Inter – Fiorentina — prima partita con l'ora solare"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Attenzione: le partite di mercoledì e giovedì finiscono dopo la chiusura di questa edizione — per questo qui sono presentazioni, senza risultati."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　OEFENINGEN VAN PAGINA 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8　Niveaus staan door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　COMPRENSIONE", 25)
e.expl("Lees het artikel op pagina 4 en kies het juiste antwoord.")
e.ex("B1", "Meerkeuze", "B", "Inter speelt woensdag tegen Shakhtar Donetsk",
     "L'Inter gioca mercoledì contro... A. l'Ajax · B. lo Shakhtar Donetsk · C. la Roma", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Napoli–Roma is zaterdag om 18:00",
     "Napoli–Roma si gioca... A. venerdì · B. sabato alle 18:00 · C. domenica a mezzanotte", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "dit is de eerste wedstrijd van de zondag met wintertijd",
     "Inter–Fiorentina è speciale perché... A. è la prima partita con l'ora solare · B. è una finale · C. si gioca di notte", size=20, gap=8)
e.ex("B1", "Meerkeuze", "C", "Atalanta speelt donderdag uit in Amsterdam",
     "L'Atalanta gioca giovedì... A. a San Siro · B. a Roma · C. ad Amsterdam", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "midweek: alleen voorbeschouwing, geen uitslag",
     "Le partite di mercoledì e giovedì, in questo giornale, sono... A. risultati finali · B. presentazioni senza risultati · C. cancellate", size=20, gap=8)
e.head("B　LE PAROLE", 25)
e.match_set("B1", "Woorden koppelen",
            ["la giornata", "la sfida", "la trasferta", "San Siro"],
            ["lo stadio dell'Inter e del Milan, a Milano",
             "una partita importante tra due squadre forti",
             "ciascuna delle parti del campionato, una dopo l'altra",
             "la partita fuori casa, nella città degli avversari"],
            ["c", "b", "d", "a"],
            ["giornata = een speelronde van de competitie c", "sfida = topper tussen twee sterke ploegen b", "trasferta = uitwedstrijd d", "San Siro = het stadion van Milaan a"],
            instr="Koppel woord en betekenis")
e.head("C　I COMPARATIVI", 25)
e.expl("Vul de vergrotende trap van het woord tussen haakjes in (gegevens: zie het speelschema).")
e.ex("B1", "Voltooi de zin", "più tardi", "18:00 is later dan 12:30: più tardi",
     "Napoli–Roma comincia ___ di Inter–Fiorentina. (tardi)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "più presto", "12:30 is vroeger dan 18:00: più presto",
     "La partita di domenica comincia ___ di quella di sabato. (presto)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "più bella", "più + bella = de mooiste van de week (subjectief)",
     "Per i tifosi, Napoli–Roma è la partita ___ del weekend. (bella)", instr="Vul in", size=20, gap=8)
e.ex("B2", "Zinsomvorming", "meglio", "bene → meglio (onregelmatig)",
     "L'Inter gioca bene. → L'Inter gioca ___ (bene).", instr="Vul in", size=20, gap=8)
e.head("D　IL PASSATO DELLO SPORT", 25)
e.expl("Vul aan met de passato prossimo.")
e.ex("B1", "Voltooi de zin", "ha vinto", "vincere: ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "ha pareggiato", "pareggiare: ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "sono arrivati", "arrivare neemt essere (meervoud)",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "abbiamo guardato", "guardare neemt avere",
     "Noi ___ (guardare) la partita in televisione.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "ha preso", "het deelwoord van prendere is preso: ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="Vul in", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
