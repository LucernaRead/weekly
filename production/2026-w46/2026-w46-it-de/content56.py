# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · GIOVANI (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("GIOVANI · JUNGE LEUTE", "La Lucerna", "LIVELLO B1 · Leggere, guardare, giocare · Lesen, schauen, spielen")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("I giovani leggono: libri a Cuneo, cinema a Milano, calcio in festa", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: B1")
f.para("Dall'11 al 15 novembre, a Cuneo, torna Scrittorincittà: più di cento autori incontrano i lettori e presentano i libri appena usciti, con il tema di quest'anno, «Finestrini». È una festa per chi ama leggere: si entra in un libro come da un finestrino, e si guarda il mondo da un altro punto di vista.")
f.para("A Milano, dal 14 al 22 novembre, c'è il Filmmaker Festival, il festival del cinema indipendente e della sperimentazione. E fino al 15 novembre continua Piccolo Grande Cinema, con proiezioni e incontri pensati soprattutto per i giovani e le famiglie.")
f.para("E dal 12 al 15 novembre, sempre a Milano, c'è l'Offside Festival, quattro giorni di calcio e cultura: ospiti, incontri e storie del pallone, in via della Moscova e via Crespi. Un festival per chi ama il calcio anche fuori dal campo, con le parole e le immagini.")
f.para("Nel weekend, poi, la scelta è dolce e azzurra: Eurochocolate a Perugia e la Festa del Torrone a Cremona (pagina 3), e giovedì e domenica le due notti dell'Italia (pagina 4). Il consiglio della redazione: un libro in mano, un film negli occhi — e domenica sera, la Nazionale.")
f.box("IL PIANO DELLA SETTIMANA", [
    ("1. Mercoledì: Scrittorincittà apre a Cuneo (Mi: Autorenfestival beginnt in Cuneo)", "serif", False, INK, 21, 1.36),
    ("2. Giovedì: Italia–Francia in TV (Italien–Frankreich im TV)", "serif", False, INK, 21, 1.36),
    ("3. Venerdì: apre Eurochocolate (Fr: Eurochocolate beginnt)", "serif", False, INK, 21, 1.36),
    ("4. Sabato: cinema a Milano (Sa: Kino in Mailand)", "serif", False, INK, 21, 1.36),
    ("5. Domenica: Belgio–Italia e rientro (So: Belgien–Italien, dann Heimfahrt)", "serif", False, INK, 21, 1.36),
])
f.gloss("il finestrino kleines Fenster · l'autore Autor · indipendente unabhängig · la sperimentazione Experiment/Erkundung · l'ospite Gast.")
f.end_report()

# col 3: castagne image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "castagne.jpg", ix, 200, CW, 300)
cy3 = caption(p, ix, 500, CW, "Le castagne arrosto: il cibo di strada dell'autunno. Con il sole di San Martino, le piazze profumano di caldarroste — e il weekend giovane comincia così.",
              "Foto: Wikimedia Commons — CC0")
facts = ["Scrittorincittà, Cuneo: dall'11 al 15 novembre, più di 100 autori, tema «Finestrini».",
         "Filmmaker Festival, Milano: dal 14 al 22 novembre, cinema indipendente.",
         "Offside Festival, Milano: dal 12 al 15 novembre, calcio e cultura."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "I GIOVANI IN NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Preferisci un libro, un film o una partita? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Lieber Buch, Film oder Spiel? Schreib zwei Sätze und schick sie.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · Jetzt du", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Lieber Buch, Film oder Spiel? Schreib zwei Sätze und schick sie.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · ÜBUNGEN ZU SEITE 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Lösungen Seite 8 · Stufen gemischt — nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("Lesen Sie den Artikel auf Seite 5 und wählen Sie die richtige Antwort.")
e.ex("B1", "Eine Antwort", "B", "Scrittorincittà ist in Cuneo",
     "Scrittorincittà è a... A. Milano · B. Cuneo · C. Firenze", size=20, gap=8)
e.ex("B1", "Eine Antwort", "B", "Scrittorincittà: über 100 Autoren",
     "Scrittorincittà ha... A. 50 autori · B. più di 100 autori · C. 19 autori", size=20, gap=8)
e.ex("B1", "Eine Antwort", "C", "Thema: Finestrini",
     "Il tema di Scrittorincittà è... A. «Legacy» · B. «Fate dolci» · C. «Finestrini»", size=20, gap=8)
e.ex("B1", "Eine Antwort", "A", "Filmmaker-Festival in Mailand",
     "Il Filmmaker Festival è a... A. Milano · B. Cuneo · C. Perugia", size=20, gap=8)
e.ex("B1", "Eine Antwort", "A", "Offside: Fußball und Kultur",
     "L'Offside Festival parla di... A. calcio e cultura · B. solo libri · C. solo dolci", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.bridge("Ergänzen Sie die Wörter aus dem Kasten. Achtung: Einige Wörter stehen im Plural.")
e.para("finestrino · autore · indipendente · sperimentazione · ospite · castagne", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "Sätze vervollständigen", "autori", "autori = Autoren (Plural)",
     "A Cuneo arrivano più di cento ___.", instr="Lücken", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "indipendente", "indipendente = unabhängig",
     "Il Filmmaker Festival è un festival del cinema ___.", instr="Lücken", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "finestrino", "finestrino = kleines Fenster",
     "Si entra in un libro come da un ___.", instr="Lücken", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "ospiti", "ospiti = Gäste (Plural)",
     "L'Offside Festival ha tanti ___ importanti.", instr="Lücken", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "castagne", "castagne arrosto = geröstete Kastanien (Plural)",
     "Le piazze profumano di ___ arrosto.", instr="Lücken", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "sperimentazione", "sperimentazione = Experiment/Erkundung",
     "Il Filmmaker Festival è il festival della ___.", instr="Lücken", size=20, gap=8)
e.head("C · IL FUTURO", 25)
e.bridge("Ergänzen Sie mit dem Futuro (futuro semplice).")
e.ex("B1", "Sätze vervollständigen", "andremo", "andare, Futur, noi: andremo",
     "Mercoledì noi ___ (andare) a Cuneo per i libri.", instr="Lücken", size=20, gap=8)
e.ex("B2", "Sätze vervollständigen", "ci sarà", "esserci, Futur: ci sarà (es wird geben)",
     "A Milano ___ (esserci) tanto cinema giovane.", instr="Lücken", size=20, gap=8)
e.ex("B1", "Sätze vervollständigen", "guarderemo", "guardare, Futur, noi: guarderemo",
     "Giovedì noi ___ (guardare) Italia–Francia.", instr="Lücken", size=20, gap=8)
e.ex("B2", "Sätze vervollständigen", "durerà", "durare, Futur: durerà",
     "Eurochocolate ___ (durare) fino al 22 novembre.", instr="Lücken", size=20, gap=8)
e.head("D · VERO O FALSO?", 25)
e.ex("B1", "Richtig oder falsch", "Vero", "Scrittorincittà: über 100 Autoren",
     "Scrittorincittà ha più di 100 autori. Vero o falso?", instr="Richtig oder falsch", size=20, gap=8)
e.ex("B1", "Richtig oder falsch", "Vero", "Filmmaker-Festival in Mailand",
     "Il Filmmaker Festival è a Milano. Vero o falso?", instr="Richtig oder falsch", size=20, gap=8)
e.ex("B2", "Richtig oder falsch", "Falso", "Falsch: Scrittorincittà endet nicht erst am 22. November",
     "Scrittorincittà chiude il 22 novembre. Vero o falso?", instr="Richtig oder falsch", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-giovani.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · APPROFONDIMENTO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("APPROFONDIMENTO · VERTIEFUNG", "La Lucerna", "LIVELLO B2 · La manovra spiegata · Der Haushalt erklärt")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1520, tag="P6-main")
f.title("La manovra, spiegata piano: 26 miliardi, il Parlamento decide", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: B2 · La legge di bilancio e i numeri")
f.para("La manovra è la legge di bilancio: il documento che dice come lo Stato spende e dove trova i soldi. Il Documento programmatico di bilancio (DPB), mandato a Bruxelles il 15 ottobre, prevede per il 2027 una crescita del +0,8% e un deficit del 3,4% del PIL. Il 28 ottobre il Consiglio dei ministri ha approvato il disegno di legge: circa 26 miliardi di euro, secondo le ricostruzioni dei giornali.")
f.para("Attenzione, però: approvato dal governo non vuol dire già legge. Il testo deve essere discusso e votato dalle Camere entro la fine dell'anno, e ogni misura può cambiare. Chi legge i giornali trova cifre diverse per le coperture — circa 5 miliardi dal settore finanziario, banche e assicurazioni, secondo le prime ricostruzioni — perché il testo definitivo si conosce solo alla fine dell'iter.")
f.para("Tra le misure raccontate dai giornali: l'allargamento del secondo scaglione Irpef al 33%, da 50 mila a 55 mila euro, e più soldi per la sanità. Sono misure raccontate, non ancora votate: il lettore saggio distingue tra «il governo propone» e «la legge dice».")
f.para("E l'Europa? Lunedì 9 novembre c'è l'Eurogruppo, la riunione dei ministri delle Finanze: la composizione della manovra dipende anche dagli spazi di flessibilità che Bruxelles concede per difesa e sicurezza energetica. Per questo, in questa edizione, riportiamo solo le date, i numeri del DPB e le misure raccontate — senza indicare alcun esito del voto in Parlamento, che non c'è ancora stato.")
f.bridge("Bei Redaktionsschluss hatte das Parlament noch nicht abgestimmt: Diese Ausgabe nennt nur Daten, DPB-Zahlen und berichtete Maßnahmen, kein Abstimmungsergebnis.")
f.gloss("la manovra Haushaltsgesetz · il deficit Defizit · la copertura Finanzierung · lo scaglione Steuerstufe · l'iter Gesetzgebungsverfahren.")
f.end_report()

# col 3: timeline + leggere i numeri (sequential, measured)
bx = COLX[3]
p.rect(bx, 200, CW, 640, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LA STRADA DELLA MANOVRA", 22, "sans", True, OLIVE)
steps = [
    ("15 OTT.", "Il DPB parte per Bruxelles: crescita +0,8%, deficit 3,4% del PIL."),
    ("28 OTT.", "Il Consiglio dei ministri approva il disegno di legge, circa 26 miliardi."),
    ("LUN 9 NOV.", "Eurogruppo a Bruxelles: si parla di flessibilità per difesa ed energia."),
    ("FINE ANNO", "Le Camere devono discutere e votare: il testo può cambiare."),
]
sy3 = 282
for w, t in steps:
    p.text(bx + 22, sy3 + 21, w, 20, "sans", True, BRICK)
    sy3 = p.para(bx + 164, sy3 + 21, t, 21, "serif", False, INK, CW - 186, 1.4) + 16
by3 = 866
bb = ("Davanti a una cifra della manovra, fai tre domande: chi la pubblica? Quando? "
      "È una proposta del governo o una legge votata? Senza queste tre risposte, un numero dice poco.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEGGERE I NUMERI", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh)

# ---- Practice-data chart (explicitly labeled as exercise data) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, GOLD, 2)
p.text(MX, gy + 10, "LE MINIME DI ESEMPIO · BEISPIEL-TIEFSTWERTE (DATI INVENTATI PER L'ESERCIZIO)", 26, "sans", True, OLIVE)
dpb = [("Torino", 6.0),
       ("Milano", 7.0),
       ("Bologna", 8.0),
       ("Roma", 12.0),
       ("Napoli", 14.0)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx1 + 22, gy + 68, "MINIME DI ESEMPIO · gradi, dati inventati", 21, "sans", True, INK)
yy = gy + 96
for lab, v in dpb:
    p.text(bx1 + 22, yy + 24, lab, 20, "serif", True, INK)
    labw = text_w(lab, "serif", True, 20)
    p.rect(bx1 + 40 + labw, yy + 6, v * 34, 22, fill=OLIVE)
    p.text(bx1 + 58 + labw + v * 34, yy + 24, f"{v:.0f}°", 20.5, "serif", False, INK)
    yy += 38
p.para(bx1 + 22, gy + bhh - 26, "Questi numeri sono inventati per l'esercizio: servono per imparare a leggere un grafico, NON sono previsioni reali.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right box: probabilities
bx2 = COLX[2]
p.rect(bx2, gy + 28, bw_, bhh, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx2 + 22, gy + 68, "PROPOSTA ≠ LEGGE", 21, "sans", True, INK)
p.para(bx2 + 22, gy + 118, "«Il governo propone» ≠ «la legge dice»", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 158, "Una cifra raccontata ≠ una cifra votata", 23, "serif", True, INK, bw_ - 44, 1.35)
p.para(bx2 + 22, gy + 198, "Il testo definitivo si conosce solo alla fine dell'iter in Parlamento.", 19.5, "serif", False, INK, bw_ - 44, 1.4)
p.para(bx2 + 22, gy + bhh - 62, "Le cifre della manovra si aggiornano con il dibattito: controllale prima di citarle.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)

# ---- P6 exercises ----
ey = 1930
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · ÜBUNGEN ZU SEITE 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Lösungen Seite 8 · Stufen gemischt — nach Nummer suchen", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LEGGERE IL GRAFICO", 25)
e.bridge("Sehen Sie sich das Übungsdiagramm oben an und wählen Sie die richtige Antwort.")
e.ex("B2", "Eine Antwort", "B", "Kältester Ort der Beispieldaten: Turin, 6°",
     "La città più fredda del grafico è... A. Milano · B. Torino · C. Napoli", size=18, gap=2)
e.ex("B2", "Eine Antwort", "A", "Wärmster Ort der Beispieldaten: Neapel, 14°",
     "La città più calda del grafico è... A. Napoli · B. Roma · C. Bologna", size=18, gap=2)
e.ex("B2", "Eine Antwort", "B", "14 − 12 = 2",
     "La differenza tra Napoli (14°) e Roma (12°) è... A. 3° · B. 2° · C. 4°", size=18, gap=2)
e.ex("B2", "Eine Antwort", "A", "7 + 8 = 15",
     "Milano (7°) e Bologna (8°) insieme fanno... A. 15° · B. 14° · C. 16°", size=18, gap=2)
e.ex("B2", "Eine Antwort", "B", "Die Diagrammdaten sind zum Üben, keine echten Vorhersagen",
     "I numeri del grafico sono... A. previsioni reali · B. dati inventati per l'esercizio · C. temperature di ieri", size=18, gap=2)
e.ex("B2", "Eine Antwort", "A", "Ein Regierungsvorschlag ist noch kein Gesetz",
     "«Il governo propone»... A. non è ancora legge · B. è già legge · C. è un errore", size=18, gap=2)
e.head("B · COMPRENSIONE", 25)
e.ex("B2", "Eine Antwort", "B", "Das Gesetz ist das Haushaltsgesetz",
     "La manovra è... A. una festa · B. la legge di bilancio · C. un film", size=18, gap=2)
e.ex("B2", "Eine Antwort", "A", "Das Parlament muss bis Jahresende abstimmen",
     "Le Camere devono votare il testo... A. entro la fine dell'anno · B. entro il 9 novembre · C. mai", size=18, gap=2)
e.ex("B2", "Eine Antwort", "A", "Der DPB wurde am 15. Oktober nach Brüssel geschickt",
     "Il DPB è stato mandato a Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=18, gap=2)
e.ex("B2", "Eine Antwort", "B", "Wachstumsprognose 2027: +0,8 %",
     "La crescita prevista per il 2027 è... A. +3,4% · B. +0,8% · C. +5%", size=18, gap=2)
e.head("C · IL CONGIUNTIVO", 25)
e.ex("B2", "Sätze vervollständigen", "piova", "è probabile che + Konjunktiv: piova",
     "È probabile che domani ___ (piovere) in pianura.", instr="Lücken", size=18, gap=2)
e.ex("B2", "Sätze vervollständigen", "nevichi", "è possibile che + Konjunktiv: nevichi",
     "È possibile che in montagna ___ (nevicare) nel weekend.", instr="Lücken", size=18, gap=2)
e.ex("B2", "Sätze vervollständigen", "controllino", "bisogna che + Konjunktiv: controllino",
     "Bisogna che i lettori ___ (controllare) il testo più recente.", instr="Lücken", size=18, gap=2)
e.ex("B2", "Sätze vervollständigen", "sia", "è importante che + Konjunktiv: sia",
     "È importante che la cifra ___ (essere) chiara per tutti.", instr="Lücken", size=18, gap=2)
e.head("D · LE PAROLE DELLA MANOVRA", 25)
e.bridge("Mit Wörtern aus dem Kasten ergänzen: manovra · deficit · copertura · scaglione")
e.ex("B2", "Sätze vervollständigen", "manovra", "manovra = Haushaltsgesetz",
     "La ___ è la legge di bilancio.", instr="Lücken", size=18, gap=2)
e.ex("B2", "Sätze vervollständigen", "deficit", "deficit = Defizit",
     "Il ___ previsto per il 2027 è del 3,4% del PIL.", instr="Lücken", size=18, gap=2)
e.ex("B2", "Sätze vervollständigen", "copertura", "copertura = Finanzierung",
     "Ogni misura deve avere la sua ___.", instr="Lücken", size=18, gap=2)
e.ex("B2", "Sätze vervollständigen", "scaglione", "scaglione = Steuerstufe",
     "Il secondo ___ Irpef si allarga, secondo le ricostruzioni.", instr="Lücken", size=18, gap=2)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-approfondimento.svg")
print("P6 saved, exercises so far:", len(REG))
