# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · CULTUUR", "La Lucerna", "A2 → B1 · Panettone, torrone e musei aperti · Zoetigheid en open musea")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Il weekend più dolce: panettone a Milano, torrone a Cremona", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2 → B1")
f.para("Il freddo porta con sé la voglia di dolci. Sabato 7 e domenica 8 novembre, a Milano, c'è la finale della Coppa del Mondo del Panettone: pasticceri da 19 paesi si sfidano con il dolce simbolo di Milano, e il pubblico può assaggiare gratis. Due le categorie in gara: il panettone tradizionale e il panettone al cioccolato.")
f.para("Lo stesso fine settimana apre a Cremona la Festa del Torrone, che dura fino al 22 novembre: bancarelle, degustazioni e musica nella città dei violini. Il torrone è un dolce antico, di mandorle e miele — e Cremona ne è la capitale.")
f.para("E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre, con mercati e piatti speciali. Il re dell'autunno resta in tavola anche con il primo freddo.")
f.para("Per chi ama la cultura, la settimana comincia martedì 3 novembre a Milano con il Forum Cultura: più di 50 eventi e aperture straordinarie di musei e biblioteche. Si comincia con il cantiere di restauro della Sala delle Asse al Castello Sforzesco, la GAM e Palazzo Morando; nel fine settimana il Forum si sposta alla Bovisa, al sito della Goccia.")
f.gloss("il panettone = zoet Milanees kerstbrood · il torrone = noga · l'assaggio = proeven · la bancarella = kraam · il cantiere = bouwplaats/restauratie.")
f.head("IL TARTUFO RESTA IN TAVOLA", 25)
f.para("La Fiera di Alba è aperta dal 10 ottobre: quasi due mesi di profumi e piatti speciali. Con il freddo, il tartufo bianco diventa ancora più prezioso — e i ristoranti lo servono con pasta, uova e risotti.", 23.5)
f.end_report()

# col 3: truffle image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "tartufo.jpg", ix, 200, CW, 265)
cy3 = caption(p, ix, 465, CW, "Un tartufo bianco, il fungo più prezioso d'Italia. Ad Alba la fiera dura fino al 6 dicembre; con il primo freddo, il tartufo è ancora più prezioso.",
              "Foto: Wikimedia Commons — dominio pubblico")
facts = ["Milano, 7–8 novembre: finale della Coppa del Mondo del Panettone, degustazioni gratuite.",
         "Cremona, 7–22 novembre: Festa del Torrone, bancarelle e musica.",
         "Alba: la Fiera del Tartufo Bianco continua fino al 6 dicembre."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "IL WEEKEND DOLCE", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Preferisci il panettone tradizionale o quello al cioccolato? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Panettone tradizionale of met chocolade? Schrijf twee zinnen en stuur ze op.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Panettone tradizionale of met chocolade? Schrijf twee zinnen en stuur ze op.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · OEFENINGEN VAN PAGINA 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus staan door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("Lees het artikel op pagina 3 en kies het juiste antwoord.")
e.ex("A2", "Meerkeuze", "B", "De Panettone-finale is in Milaan",
     "La finale della Coppa del Mondo del Panettone è a... A. Cremona · B. Milano · C. Alba", size=20, gap=8)
e.ex("A2", "Meerkeuze", "C", "Festa del Torrone duurt tot 22 november",
     "La Festa del Torrone dura fino al... A. 6 dicembre · B. 8 novembre · C. 22 novembre", size=20, gap=8)
e.ex("A2", "Meerkeuze", "B", "19 landen doen mee aan de Panettone-finale",
     "Alla finale del Panettone partecipano pasticceri da... A. 5 paesi · B. 19 paesi · C. 50 paesi", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Forum Cultura opent op dinsdag 3 november",
     "Il Forum Cultura apre... A. martedì 3 novembre · B. sabato 7 novembre · C. lunedì 2 novembre", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Truffelbeurs Alba sluit op 6 december",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.bridge("Vul in met de woorden uit het kader.")
e.para("panettone · torrone · assaggio · bancarella · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Voltooi de zin", "panettone", "panettone = zoet Milanees kerstbrood",
     "Il ___ è il dolce simbolo di Milano.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "torrone", "torrone = noga",
     "A Cremona si festeggia il ___.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "assaggio", "assaggio = proeven",
     "Alla finale del Panettone, il pubblico può fare un ___ gratis.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "bancarella", "bancarella = kraam",
     "Alla festa ci sono tante ___ con i dolci.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "mandorle", "mandorle = amandelen (meervoud)",
     "Il torrone è fatto di ___ e miele.", instr="Vul in", size=20, gap=8)
e.ex("A2", "Voltooi de zin", "tartufo", "tartufo = truffel",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="Vul in", size=20, gap=8)
e.head("C · IL PASSATO PROSSIMO", 25)
e.bridge("Vul aan met de passato prossimo (voltooid tegenwoordige tijd); let op avere / essere.")
e.ex("B1", "Voltooi de zin", "è arrivato", "arrivare gebruikt essere: è arrivato",
     "Il primo freddo ___ (arrivare) lunedì.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "abbiamo assaggiato", "assaggiare gebruikt avere",
     "Noi ___ (assaggiare) il panettone a Milano.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "sono andati", "andare gebruikt essere, meervoud: sono andati",
     "I pasticceri ___ (andare) a Milano per la finale.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "ha aperto", "aprire gebruikt avere: ha aperto",
     "Cremona ___ (aprire) la Festa del Torrone sabato.", instr="Vul in", size=20, gap=8)
e.head("D · COSTRUISCI LE FRASI", 25)
e.bridge("Maak van de woorden correcte zinnen.")
e.ex("B1", "Zinnen bouwen", "La finale è a Milano il 7 novembre.", "onderwerp + essere + plaats + datum",
     "la finale / è a Milano / il 7 novembre → ___", instr="Bouw de zin", size=20, gap=8)
e.ex("A2", "Zinnen bouwen", "A Cremona il torrone è il re.", "plaats vooraan, onderwerp erna",
     "a Cremona / il torrone / è il re → ___", instr="Bouw de zin", size=20, gap=8)
e.ex("B1", "Zinnen bouwen", "La fiera dura fino al 6 dicembre.", "dura fino a = duurt tot",
     "la fiera / dura / fino al 6 dicembre → ___", instr="Bouw de zin", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · SPORT", "La Lucerna", "LIVELLO B1 · La Serie A e l'Europa · Serie A en Europa")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("L'undicesima giornata: Genoa–Milan, Inter–Como, Fiorentina–Juventus", 37)
f.byline("Dalla redazione sportiva de La Lucerna · Livello di lettura: B1")
f.para("È una settimana di grande calcio. Da martedì 3 a giovedì 5 novembre si gioca la quarta giornata delle coppe europee: Champions League, Europa League e Conference League. Attenzione: queste partite si giocano dopo la chiusura del giornale — qui sono una presentazione, senza risultati.")
f.para("Poi arriva l'undicesima giornata di Serie A, da venerdì 6 a domenica 8 novembre. La giornata chiude domenica 8 novembre con tre partite grandi: Genoa–Milan, Inter–Como e Fiorentina–Juventus, la sera a Firenze.")
f.para("Domenica è anche il giorno del freddo sugli spalti: chi va allo stadio mette sciarpa e guanti, come a pagina 2. Ma il calcio non si ferma per il primo freddo — anzi, con il freddo le partite della sera diventano ancora più belle, sotto le luci.")
f.para("E per chi segue i giovani: anche le squadre giovani giocano nel weekend. Il consiglio della redazione è uno solo: scegli una partita, guarda il calendario e non perderti la domenica sera a Firenze.")
f.gloss("la giornata = speelronde · la presentazione = voorbeschouwing · gli spalti = tribunes · la sera = avond.")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Martedì 3 – giovedì 5 novembre · Coppe europee, 4ª giornata — si giocano dopo la chiusura del giornale. Venerdì 6 – domenica 8 novembre · Serie A, 11ª giornata. Domenica 8 novembre · Genoa – Milan; Inter – Como; Fiorentina – Juventus (sera, a Firenze).", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi domenica sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Welke wedstrijd kijk jij zondagavond? Schrijf twee zinnen in het Italiaans.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU? · EN JIJ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Welke wedstrijd kijk jij zondagavond? Schrijf twee zinnen in het Italiaans.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DEL CALCIO · VOETBALWEEK", 26, "sans", True, OLIVE)
rows = [
    ("Mar–Gio", "Coppe europee · 4ª giornata", "Champions, Europa e Conference League: presentazione, senza risultati"),
    ("Ven–Dom", "Serie A · 11ª giornata", "L'undicesima giornata si gioca da venerdì 6 a domenica 8 novembre"),
    ("Dom 8.11", "Serie A", "Genoa – Milan — domenica, a Genova"),
    ("Dom 8.11", "Serie A", "Inter – Como — a San Siro, a Milano"),
    ("Dom 8.11", "Serie A · sera", "Fiorentina – Juventus — la sera, a Firenze"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 470, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Attenzione: le partite europee di martedì–giovedì e le partite di Serie A del weekend si giocano dopo la chiusura di questa edizione — per questo qui sono presentazioni, senza risultati."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · OEFENINGEN VAN PAGINA 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antwoorden op pagina 8 · Niveaus staan door elkaar: zoek op nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("Lees het artikel op pagina 4 en kies het juiste antwoord.")
e.ex("B1", "Meerkeuze", "B", "Speelronde 11 sluit op zondag",
     "L'undicesima giornata di Serie A chiude... A. venerdì · B. domenica 8 novembre · C. lunedì", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Zondagavond: Fiorentina–Juventus",
     "Domenica sera, a Firenze, si gioca... A. Inter–Como · B. Fiorentina–Juventus · C. Genoa–Milan", size=20, gap=8)
e.ex("B1", "Meerkeuze", "A", "Europese speelronde 4: 3–5 november",
     "La quarta giornata delle coppe europee si gioca... A. dal 3 al 5 novembre · B. dal 6 all'8 novembre · C. il 2 novembre", size=20, gap=8)
e.ex("B1", "Meerkeuze", "C", "Europese wedstrijden: alleen voorbeschouwing",
     "Le partite europee, in questo giornale, sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati", size=20, gap=8)
e.ex("B1", "Meerkeuze", "B", "Inter–Como in San Siro",
     "Inter–Como si gioca... A. a Firenze · B. a San Siro · C. a Genova", size=20, gap=8)
e.head("B · LE PAROLE", 25)
e.match_set("B1", "Woorden koppelen",
            ["la giornata", "la presentazione", "gli spalti", "la sera"],
            ["il posto del pubblico allo stadio, con le gradinate",
             "il racconto prima della partita, senza risultati",
             "ciascuna delle parti del campionato, una dopo l'altra",
             "la parte del giorno dopo il tramonto, con le luci accese"],
            ["c", "b", "a", "d"],
            ["giornata = speelronde c", "presentazione = voorbeschouwing b", "spalti = tribunes a", "sera = avond d"],
            instr="Koppel woord en betekenis")
e.head("C · I COMPARATIVI", 25)
e.bridge("Vul de vergrotende trap van het woord tussen haakjes in (zie het speelschema).")
e.ex("B1", "Voltooi de zin", "più tardi", "Zondagavond later dan vrijdag: più tardi",
     "Le partite di domenica sera cominciano ___ di quelle di venerdì. (tardi)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "più presto", "Vrijdag eerder dan zondag: più presto",
     "Le partite di venerdì cominciano ___ di quelle di domenica. (presto)", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "più bella", "più + bella: zondagavond is het mooist (mening)",
     "Per i tifosi, la domenica sera è la serata ___ del weekend. (bella)", instr="Vul in", size=20, gap=8)
e.ex("B2", "Zin ombouwen", "meglio", "vergrotende trap van bene is onregelmatig: meglio",
     "L'Inter gioca bene. → L'Inter gioca ___ (bene).", instr="Vul in", size=20, gap=8)
e.head("D · IL PASSATO DELLO SPORT", 25)
e.bridge("Vul aan met de passato prossimo.")
e.ex("B1", "Voltooi de zin", "ha vinto", "vincere: ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "ha pareggiato", "pareggiare: ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="Vul in", size=20, gap=8)
e.ex("B2", "Voltooi de zin", "sono arrivati", "arrivare gebruikt essere, meervoud: sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "abbiamo guardato", "guardare gebruikt avere: abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="Vul in", size=20, gap=8)
e.ex("B1", "Voltooi de zin", "ha preso", "voltooid deelwoord van prendere is preso: ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="Vul in", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
