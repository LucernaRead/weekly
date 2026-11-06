# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-it-en/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · Culture", "La Lucerna", "A2 → B1 · Panettone, torrone e musei aperti · Sweets and open museums")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Il weekend più dolce: panettone a Milano, torrone a Cremona", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2 → B1")
f.para("Il freddo porta con sé la voglia di dolci. Sabato 7 e domenica 8 novembre, a Milano, c'è la finale della Coppa del Mondo del Panettone: pasticceri da 19 paesi si sfidano con il dolce simbolo di Milano, e il pubblico può assaggiare gratis. Due le categorie in gara: il panettone tradizionale e il panettone al cioccolato.")
f.para("Lo stesso fine settimana apre a Cremona la Festa del Torrone, che dura fino al 22 novembre: bancarelle, degustazioni e musica nella città dei violini. Il torrone è un dolce antico, di mandorle e miele — e Cremona ne è la capitale.")
f.para("E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre, con mercati e piatti speciali. Il re dell'autunno resta in tavola anche con il primo freddo.")
f.para("Per chi ama la cultura, la settimana comincia martedì 3 novembre a Milano con il Forum Cultura: più di 50 eventi e aperture straordinarie di musei e biblioteche. Si comincia con il cantiere di restauro della Sala delle Asse al Castello Sforzesco, la GAM e Palazzo Morando; nel fine settimana il Forum si sposta alla Bovisa, al sito della Goccia.")
f.gloss("il panettone Milan's Christmas cake · il torrone nougat · l'assaggio tasting · la bancarella stall · il cantiere building site")
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
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Do you prefer traditional panettone or chocolate panettone? Write two sentences and send them to us.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · Over to you", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Do you prefer traditional panettone or chocolate panettone? Write two sentences and send them to us.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · Page 3 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels are mixed — find answers by number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("Read the page 3 article and choose the right answer.")
e.ex("A2", "单选", "B", "The Panettone final is in Milan",
     "La finale della Coppa del Mondo del Panettone è a... A. Cremona · B. Milano · C. Alba", size=20, gap=8)
e.ex("A2", "单选", "C", "The Cremona torrone festival runs to 22 November",
     "La Festa del Torrone dura fino al... A. 6 dicembre · B. 8 novembre · C. 22 novembre", size=20, gap=8)
e.ex("A2", "单选", "B", "19 countries send pastry chefs to the Panettone final",
     "Alla finale del Panettone partecipano pasticceri da... A. 5 paesi · B. 19 paesi · C. 50 paesi", size=20, gap=8)
e.ex("B1", "单选", "A", "The Forum Cultura opens on Tuesday 3 November",
     "Il Forum Cultura apre... A. martedì 3 novembre · B. sabato 7 novembre · C. lunedì 2 novembre", size=20, gap=8)
e.ex("B1", "单选", "B", "The Alba truffle fair runs to 6 December",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.bridge("Fill in with the words in the box.")
e.para("panettone · torrone · assaggio · bancarella · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "panettone", "panettone = Milan's Christmas cake",
     "Il ___ è il dolce simbolo di Milano.", instr="Fill in", size=20, gap=8)
e.ex("A2", "完成句子", "torrone", "torrone = nougat",
     "A Cremona si festeggia il ___.", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "assaggio", "assaggio = tasting",
     "Alla finale del Panettone, il pubblico può fare un ___ gratis.", instr="Fill in", size=20, gap=8)
e.ex("A2", "完成句子", "bancarella", "bancarella = stall",
     "Alla festa ci sono tante ___ con i dolci.", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "mandorle", "mandorle = almonds (plural)",
     "Il torrone è fatto di ___ e miele.", instr="Fill in", size=20, gap=8)
e.ex("A2", "完成句子", "tartufo", "tartufo = truffle",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="Fill in", size=20, gap=8)
e.head("C · IL PASSATO PROSSIMO", 25)
e.bridge("Complete with the passato prossimo — watch the auxiliaries avere / essere.")
e.ex("B1", "完成句子", "è arrivato", "arrivare takes essere: è arrivato",
     "Il primo freddo ___ (arrivare) lunedì.", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "abbiamo assaggiato", "assaggiare takes avere",
     "Noi ___ (assaggiare) il panettone a Milano.", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "sono andati", "andare takes essere, plural sono andati",
     "I pasticceri ___ (andare) a Milano per la finale.", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "ha aperto", "aprire takes avere: ha aperto",
     "Cremona ___ (aprire) la Festa del Torrone sabato.", instr="Fill in", size=20, gap=8)
e.head("D · COSTRUISCI LE FRASI", 25)
e.bridge("Put the words in the right order.")
e.ex("B1", "造句", "La finale è a Milano il 7 novembre.", "Subject + essere + place",
     "la finale / è a Milano / il 7 novembre → ___", instr="Reorder", size=20, gap=8)
e.ex("A2", "造句", "A Cremona il torrone è il re.", "Place first, subject after",
     "a Cremona / il torrone / è il re → ___", instr="Reorder", size=20, gap=8)
e.ex("B1", "造句", "La fiera dura fino al 6 dicembre.", "dura fino a = lasts until",
     "la fiera / dura / fino al 6 dicembre → ___", instr="Reorder", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · Sport", "La Lucerna", "LIVELLO B1 · La Serie A e l'Europa · Serie A and Europe")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("L'undicesima giornata: Genoa–Milan, Inter–Como, Fiorentina–Juventus", 37)
f.byline("Dalla redazione sportiva de La Lucerna · Livello di lettura: B1")
f.para("È una settimana di grande calcio. Da martedì 3 a giovedì 5 novembre si gioca la quarta giornata delle coppe europee: Champions League, Europa League e Conference League. Attenzione: queste partite si giocano dopo la chiusura del giornale — qui sono una presentazione, senza risultati.")
f.para("Poi arriva l'undicesima giornata di Serie A, da venerdì 6 a domenica 8 novembre. La giornata chiude domenica 8 novembre con tre partite grandi: Genoa–Milan, Inter–Como e Fiorentina–Juventus, la sera a Firenze.")
f.para("Domenica è anche il giorno del freddo sugli spalti: chi va allo stadio mette sciarpa e guanti, come a pagina 2. Ma il calcio non si ferma per il primo freddo — anzi, con il freddo le partite della sera diventano ancora più belle, sotto le luci.")
f.para("E per chi segue i giovani: anche le squadre giovani giocano nel weekend. Il consiglio della redazione è uno solo: scegli una partita, guarda il calendario e non perderti la domenica sera a Firenze.")
f.gloss("la giornata matchday · la presentazione preview · gli spalti stands · la sera evening")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Martedì 3 – giovedì 5 novembre · Coppe europee, 4ª giornata — si giocano dopo la chiusura del giornale. Venerdì 6 – domenica 8 novembre · Serie A, 11ª giornata. Domenica 8 novembre · Genoa – Milan; Inter – Como; Fiorentina – Juventus (sera, a Firenze).", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi domenica sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Which match will you watch on Sunday evening? Write two sentences in Italian and send them to us.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU? · Over to you", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Which match will you watch on Sunday evening? Write two sentences in Italian and send them to us.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DEL CALCIO · Football week", 26, "sans", True, OLIVE)
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
p.text(MX, ey + 28, "ESERCIZI · Page 4 exercises", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Answers on page 8 · Levels are mixed — find answers by number", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIONE", 25)
e.bridge("Read the page 4 article and choose the right answer.")
e.ex("B1", "单选", "B", "Serie A matchday 11 ends on Sunday",
     "L'undicesima giornata di Serie A chiude... A. venerdì · B. domenica 8 novembre · C. lunedì", size=20, gap=8)
e.ex("B1", "单选", "B", "Fiorentina play Juventus on Sunday evening",
     "Domenica sera, a Firenze, si gioca... A. Inter–Como · B. Fiorentina–Juventus · C. Genoa–Milan", size=20, gap=8)
e.ex("B1", "单选", "A", "European matchday 4 runs 3-5 November",
     "La quarta giornata delle coppe europee si gioca... A. dal 3 al 5 novembre · B. dal 6 all'8 novembre · C. il 2 novembre", size=20, gap=8)
e.ex("B1", "单选", "C", "European matches are previews here, with no results",
     "Le partite europee, in questo giornale, sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati", size=20, gap=8)
e.ex("B1", "单选", "B", "Inter play Como at San Siro",
     "Inter–Como si gioca... A. a Firenze · B. a San Siro · C. a Genova", size=20, gap=8)
e.head("B · LE PAROLE", 25)
e.match_set("B1", "词汇配对",
            ["la giornata", "la presentazione", "gli spalti", "la sera"],
            ["il posto del pubblico allo stadio, con le gradinate",
             "il racconto prima della partita, senza risultati",
             "ciascuna delle parti del campionato, una dopo l'altra",
             "la parte del giorno dopo il tramonto, con le luci accese"],
            ["c", "b", "a", "d"],
            ["giornata = one matchday, c", "presentazione = preview, b", "spalti = stands, a", "sera = evening, d"],
            instr="Match the pairs")
e.head("C · I COMPARATIVI", 25)
e.bridge("Fill in with the comparative of the word in brackets (see the fixture table).")
e.ex("B1", "完成句子", "più tardi", "Sunday matches are later than Friday's: più tardi",
     "Le partite di domenica sera cominciano ___ di quelle di venerdì. (tardi)", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "più presto", "Friday matches are earlier than Sunday's: più presto",
     "Le partite di venerdì cominciano ___ di quelle di domenica. (presto)", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "più bella", "più + bella: Sunday evening is the finest",
     "Per i tifosi, la domenica sera è la serata ___ del weekend. (bella)", instr="Fill in", size=20, gap=8)
e.ex("B2", "句型转换", "meglio", "The comparative of bene is the irregular meglio",
     "L'Inter gioca bene. → L'Inter gioca ___ (bene).", instr="Fill in", size=20, gap=8)
e.head("D · IL PASSATO DELLO SPORT", 25)
e.bridge("Complete with the passato prossimo.")
e.ex("B1", "完成句子", "ha vinto", "vincere: ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "ha pareggiato", "pareggiare: ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="Fill in", size=20, gap=8)
e.ex("B2", "完成句子", "sono arrivati", "arrivare takes essere, plural sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "abbiamo guardato", "guardare takes avere: abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="Fill in", size=20, gap=8)
e.ex("B1", "完成句子", "ha preso", "The participle of prendere is preso: ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="Fill in", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
