# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · CULTURE", "La Lucerna", "A2 → B1 · Torrone, cioccolato e tartufo · Torrone, chocolat et truffe")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Due feste dolci: il torrone a Cremona, il cioccolato a Perugia", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2 → B1")
f.para("Il secondo weekend della Festa del Torrone è a Cremona, sabato 14 e domenica 15 novembre: laboratori per i più piccoli, degustazioni e una maxi racchetta da tennis fatta di torrone, per il tennis in carrozzina. Domenica 15 novembre arriva anche il Treno Storico Arlecchino, da Milano a Cremona, e lo spettacolo delle Terre di mezzo in piazza del Comune.")
f.para("Lo stesso weekend, venerdì 13 novembre, apre a Perugia Eurochocolate, la 32ª edizione, fino al 22 novembre: il titolo è «Fate dolci», un invito a vivere il cioccolato in modo attivo e creativo, con laboratori, spettacoli e il grande Chocolate Show. La Regione ospite di quest'anno è la Calabria.")
f.para("E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre, con il Mercato Mondiale ogni sabato e domenica. Il re dell'autunno resta in tavola anche con il sole di San Martino.")
f.para("Per chi ama la storia, il torrone di Cremona racconta un matrimonio: la rievocazione è quella di Bianca Maria Visconti e Francesco Sforza, con il corteo storico che torna domenica 22 novembre, l'ultimo giorno della festa. Il tema del 2026 è «Il Confine», la soglia tra tradizione e innovazione.")
f.gloss("il torrone nougat · il cioccolato chocolat · il laboratorio atelier · la degustazione dégustation · la rievocazione reconstitution historique.")
f.head("IL TARTUFO RESTA IN TAVOLA", 25)
f.para("La Fiera di Alba è aperta dal 10 ottobre: quasi due mesi di profumi e piatti speciali. Con il sole di San Martino, il tartufo bianco diventa ancora più prezioso — e i ristoranti lo servono con pasta, uova e risotti.", 23.5)
f.end_report()

# col 3: truffle image + facts + e tu? (sequential)
ix = COLX[3]
image(p, "tartufo.jpg", ix, 200, CW, 265)
cy3 = caption(p, ix, 465, CW, "Un tartufo bianco, il fungo più prezioso d'Italia. Ad Alba la fiera dura fino al 6 dicembre; con il sole di San Martino, il tartufo è ancora più prezioso.",
              "Foto: Wikimedia Commons — dominio pubblico")
facts = ["Cremona, 14–15 novembre: secondo weekend del Torrone, laboratori e treno storico.",
         "Perugia, 13–22 novembre: Eurochocolate, 32ª edizione, «Fate dolci».",
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
etvous = "E tu? Preferisci il torrone o il cioccolato? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Tu préfères le torrone ou le chocolat ? Écris deux phrases et envoie-les.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · À TOI LA PAROLE", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Tu préfères le torrone ou le chocolat ? Écris deux phrases et envoie-les.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · Exercices page 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · Niveaux mélangés — cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("Lisez l'article page 3 et choisissez la bonne réponse.")
e.ex("A2", "Choix unique", "B", "Fête du torrone, deuxième week-end : 14–15 novembre",
     "Il secondo weekend del Torrone è... A. il 7–8 novembre · B. il 14–15 novembre · C. il 21–22 novembre", size=20, gap=8)
e.ex("A2", "Choix unique", "C", "Le festival du chocolat dure jusqu'au 22 novembre",
     "Eurochocolate dura fino al... A. 6 dicembre · B. 15 novembre · C. 22 novembre", size=20, gap=8)
e.ex("A2", "Choix unique", "B", "Le festival du chocolat en est à sa 32e édition",
     "Eurochocolate è alla sua... A. 29ª edizione · B. 32ª edizione · C. 67ª edizione", size=20, gap=8)
e.ex("B1", "Choix unique", "A", "Le thème d'Eurochocolate : « Fate dolci »",
     "Il titolo di Eurochocolate 2026 è... A. «Fate dolci» · B. «Il Confine» · C. «Legacy»", size=20, gap=8)
e.ex("B1", "Choix unique", "B", "La foire de la truffe d'Alba dure jusqu'au 6 décembre",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.bridge("Complétez avec les mots de l'encadré.")
e.para("torrone · cioccolato · laboratorio · degustazione · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Compléter les phrases", "torrone", "torrone = nougat",
     "A Cremona si festeggia il ___.", instr="Compléter", size=20, gap=8)
e.ex("A2", "Compléter les phrases", "cioccolato", "cioccolato = chocolat",
     "A Perugia si festeggia il ___.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "laboratorio", "laboratorio = atelier (ici)",
     "Per i più piccoli c'è il ___ della dolcezza.", instr="Compléter", size=20, gap=8)
e.ex("A2", "Compléter les phrases", "degustazione", "degustazione = dégustation",
     "Alla festa c'è una ___ con i dolci.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "mandorle", "mandorle = amandes (pluriel)",
     "Il torrone è fatto di ___ e miele.", instr="Compléter", size=20, gap=8)
e.ex("A2", "Compléter les phrases", "tartufo", "tartufo = truffe",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="Compléter", size=20, gap=8)
e.head("C · IL PASSATO PROSSIMO", 25)
e.bridge("Complétez avec le passato prossimo — attention aux auxiliaires avere / essere.")
e.ex("B1", "Compléter les phrases", "è arrivato", "arrivare prend essere : è arrivato",
     "Il Treno Storico ___ (arrivare) a Cremona domenica.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "abbiamo assaggiato", "assaggiare prend avere",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "sono andati", "andare prend essere, pluriel sono andati",
     "I visitatori ___ (andare) a Perugia per Eurochocolate.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "ha aperto", "aprire prend avere : ha aperto",
     "Perugia ___ (aprire) Eurochocolate venerdì.", instr="Compléter", size=20, gap=8)
e.head("D · COSTRUISCI LE FRASI", 25)
e.bridge("Remettez les mots dans le bon ordre.")
e.ex("B1", "Faire des phrases", "Eurochocolate è a Perugia dal 13 novembre.", "Sujet + essere + lieu + date",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="Former une phrase", size=20, gap=8)
e.ex("A2", "Faire des phrases", "A Cremona il torrone è il re.", "Lieu d'abord, sujet ensuite",
     "a Cremona / il torrone / è il re → ___", instr="Former une phrase", size=20, gap=8)
e.ex("B1", "Faire des phrases", "La fiera dura fino al 6 dicembre.", "dura fino a = dure jusqu'à",
     "la fiera / dura / fino al 6 dicembre → ___", instr="Former une phrase", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · SPORT", "La Lucerna", "LIVELLO B1 · Le notti azzurre e il tennis · Nuits azzurre et tennis")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("Due notti azzurre: Francia a San Siro, Belgio a Bruxelles", 37)
f.byline("Dalla redazione sportiva de La Lucerna · Livello di lettura: B1")
f.para("È una settimana di grande calcio, senza Serie A: il campionato si ferma per la sosta delle nazionali. Giovedì 12 novembre, alle 20.45, l'Italia gioca a San Siro con la Francia, nella quinta giornata di Nations League. Domenica 15 novembre, alle 20.45, gli Azzurri chiudono il girone a Bruxelles, con il Belgio.")
f.para("Nel girone 1 di Lega A, la Francia è prima con 10 punti, l'Italia è seconda con 7, il Belgio è terzo con 6 e la Turchia è a zero. Le prime due vanno ai quarti di finale, a marzo 2027. Per l'Italia, le due partite di questa settimana sono decisive: attenzione, qui sono presentazioni, senza risultati.")
f.para("Giovedì e domenica il calcio scende in campo anche per la ricerca: con «Un gol per la ricerca», le partite ricordano i Giorni della Ricerca AIRC, che durano fino al 15 novembre e raccontano il lavoro di più di 770 progetti di ricerca.")
f.para("Domenica 15 novembre comincia anche un'altra storia: a Torino, all'Inalpi Arena, iniziano le Nitto ATP Finals, con gli otto migliori giocatori e le otto migliori coppie di doppio. Giovedì 12 novembre, all'Inalpi Arena, c'è il Grand Opening Show con Achille Lauro.")
f.para("E per chi segue la Serie A: l'undicesima giornata, giocata dal 6 all'8 novembre, è appena finita — i risultati e la classifica li leggiamo nel prossimo numero. La dodicesima giornata si gioca dal 21 al 23 novembre: Como–Cagliari e Lazio–Lecce sabato, Juventus–Venezia, Bologna–Udinese, Sassuolo–Genoa e Milan–Frosinone domenica, Atalanta–Inter la sera, Monza–Fiorentina lunedì.")
f.gloss("la sosta trêve du championnat · il girone groupe · decisivo décisif · la presentazione présentation d'avant-match.")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Giovedì 12 novembre, ore 20.45 · Italia – Francia, a San Siro, Nations League. Domenica 15 novembre, ore 20.45 · Belgio – Italia, a Bruxelles. Domenica 15 novembre · ATP Finals a Torino: iniziano le gare all'Inalpi Arena.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi giovedì sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Quel match regarderas-tu jeudi soir ? Écris deux phrases en italien.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU? · À TOI LA PAROLE", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Quel match regarderas-tu jeudi soir ? Écris deux phrases en italien.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DELLO SPORT · La semaine du sport", 26, "sans", True, OLIVE)
rows = [
    ("Gio 12.11", "Nations League", "Italia – Francia — ore 20.45, a San Siro, a Milano"),
    ("Ven 13.11", "Tennis · Torino", "Blue Carpet: i campioni sfilano in piazza San Carlo"),
    ("Dom 15.11", "Nations League", "Belgio – Italia — ore 20.45, a Bruxelles"),
    ("Dom 15.11", "Tennis · Torino", "ATP Finals: iniziano le gare all'Inalpi Arena"),
    ("Dom 22.11", "Serie A · 12ª giornata", "Atalanta – Inter — la sera, a Bergamo"),
]
yy = ty + 16
for i, (d, t, m) in enumerate(rows):
    p.rect(MX, yy, RIGHT - MX, 44, fill="#f4efe0" if i % 2 == 0 else "#efe8d2")
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 470, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Attenzione: le partite dell'Italia di giovedì e domenica e le gare di tennis si giocano dopo la chiusura di questa edizione — per questo qui sono presentazioni, senza risultati. I risultati della Serie A, invece, sono nel prossimo numero."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · Exercices page 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · Niveaux mélangés — cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("Lisez l'article page 4 et choisissez la bonne réponse.")
e.ex("B1", "Choix unique", "B", "Italie–France, jeudi 12 novembre",
     "Italia–Francia si gioca... A. domenica 15 novembre · B. giovedì 12 novembre · C. lunedì 9 novembre", size=20, gap=8)
e.ex("B1", "Choix unique", "B", "Dimanche : l'Italie à Bruxelles contre la Belgique",
     "Domenica, l'Italia gioca... A. a San Siro · B. a Bruxelles · C. a Torino", size=20, gap=8)
e.ex("B1", "Choix unique", "A", "La France mène le groupe avec 10 points",
     "Nel girone, la Francia ha... A. 10 punti · B. 7 punti · C. 6 punti", size=20, gap=8)
e.ex("B1", "Choix unique", "C", "Les matches de la Nazionale sont des avant-premières, sans résultats",
     "Le partite dell'Italia, in questo giornale, sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati", size=20, gap=8)
e.ex("B1", "Choix unique", "B", "Finales ATP à Turin",
     "Le ATP Finals si giocano... A. a Milano · B. a Torino · C. a Bruxelles", size=20, gap=8)
e.head("B · LE PAROLE", 25)
e.match_set("B1", "Associer les mots",
            ["la sosta", "il girone", "decisivo", "la presentazione"],
            ["il racconto prima della partita, senza risultati",
             "che decide tutto, molto importante",
             "il gruppo di squadre che giocano tra loro",
             "la pausa del campionato, senza partite"],
            ["d", "c", "b", "a"],
            ["sosta=trêve d", "girone=groupe c", "decisivo=décisif b", "presentazione=présentation d'avant-match a"],
            instr="Associer")
e.head("C · I COMPARATIVI", 25)
e.bridge("Complétez avec le comparatif du mot entre parenthèses (voir le tableau des matchs).")
e.ex("B1", "Compléter les phrases", "più tardi", "Les deux matches commencent à 20 h 45 : le match de dimanche n'est pas plus tard que celui de jeudi : più tardi",
     "Le partite di domenica sera NON cominciano ___ di quelle di giovedì. (tardi)", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "più presto", "Les deux matches commencent à 20 h 45 : le match de jeudi n'est pas plus tôt que celui de dimanche : più presto",
     "Le partite di giovedì NON cominciano ___ di quelle di domenica. (presto)", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "più bella", "più + bella : jeudi soir le plus beau (jugement subjectif)",
     "Per i tifosi, la serata di giovedì è la serata ___ del weekend. (bella)", instr="Compléter", size=20, gap=8)
e.ex("B2", "Structures de phrase", "meglio", "Le comparatif de bene est l'irrégulier meglio",
     "L'Italia gioca bene. → L'Italia gioca ___ (bene).", instr="Compléter", size=20, gap=8)
e.head("D · IL PASSATO DELLO SPORT", 25)
e.bridge("Complétez avec le passato prossimo.")
e.ex("B1", "Compléter les phrases", "ha vinto", "vincere : ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "ha pareggiato", "pareggiare : ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="Compléter", size=20, gap=8)
e.ex("B2", "Compléter les phrases", "sono arrivati", "arrivare prend essere, pluriel sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "abbiamo guardato", "guardare prend avere : abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="Compléter", size=20, gap=8)
e.ex("B1", "Compléter les phrases", "ha preso", "Le participe de prendere est preso : ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="Compléter", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
