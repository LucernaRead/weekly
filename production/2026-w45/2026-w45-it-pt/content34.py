# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA　CULTURA", "La Lucerna", "A2 → B1　Panettone, torrone e musei aperti　Doces e museus abertos")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Il weekend più dolce: panettone a Milano, torrone a Cremona", 32)
f.byline("Dalla redazione de La Lucerna　Livello di lettura: A2 → B1")
f.para("Il freddo porta con sé la voglia di dolci. Sabato 7 e domenica 8 novembre, a Milano, c'è la finale della Coppa del Mondo del Panettone: pasticceri da 19 paesi si sfidano con il dolce simbolo di Milano, e il pubblico può assaggiare gratis. Due le categorie in gara: il panettone tradizionale e il panettone al cioccolato.")
f.para("Lo stesso fine settimana apre a Cremona la Festa del Torrone, che dura fino al 22 novembre: bancarelle, degustazioni e musica nella città dei violini. Il torrone è un dolce antico, di mandorle e miele — e Cremona ne è la capitale.")
f.para("E il tartufo bianco non va in vacanza: ad Alba, in Piemonte, la Fiera del Tartufo Bianco continua fino al 6 dicembre, con mercati e piatti speciali. Il re dell'autunno resta in tavola anche con il primo freddo.")
f.para("Per chi ama la cultura, la settimana comincia martedì 3 novembre a Milano con il Forum Cultura: più di 50 eventi e aperture straordinarie di musei e biblioteche. Si comincia con il cantiere di restauro della Sala delle Asse al Castello Sforzesco, la GAM e Palazzo Morando; nel fine settimana il Forum si sposta alla Bovisa, al sito della Goccia.")
f.gloss("il panettone bolo de Natal de Milão · il torrone torrão · l'assaggio prova · la bancarella banca · il cantiere estaleiro")
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
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "IL WEEKEND DOLCE", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Preferisci il panettone tradizionale o quello al cioccolato? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Preferes o panettone tradicional ou o de chocolate? Escreve duas frases e envia-as.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU?　E tu?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Preferes o panettone tradicional ou o de chocolate? Escreve duas frases e envia-as.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　Exercícios da página 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　Os níveis misturam-se — procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P3-ex")
e.head("A　COMPRENSIONE", 25)
e.bridge("Leia o artigo da página 3 e escolha a resposta certa.")
e.ex("A2", "Uma opção", "B", "A final do Panettone é em Milão",
     "La finale della Coppa del Mondo del Panettone è a... A. Cremona · B. Milano · C. Alba", size=20, gap=8)
e.ex("A2", "Uma opção", "C", "A Festa del Torrone vai até 22 de novembro",
     "La Festa del Torrone dura fino al... A. 6 dicembre · B. 8 novembre · C. 22 novembre", size=20, gap=8)
e.ex("A2", "Uma opção", "B", "19 países enviam pasteleiros à final do Panettone",
     "Alla finale del Panettone partecipano pasticceri da... A. 5 paesi · B. 19 paesi · C. 50 paesi", size=20, gap=8)
e.ex("B1", "Uma opção", "A", "O Forum Cultura abre na terça-feira, 3 de novembro",
     "Il Forum Cultura apre... A. martedì 3 novembre · B. sabato 7 novembre · C. lunedì 2 novembre", size=20, gap=8)
e.ex("B1", "Uma opção", "B", "A feira da trufa de Alba vai até 6 de dezembro",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. il 6 dicembre · C. l'8 novembre", size=20, gap=8)
e.head("B　LE PAROLE DEL TESTO", 25)
e.bridge("Preencha com as palavras do quadro.")
e.para("panettone · torrone · assaggio · bancarella · tartufo · mandorle", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "Completar as frases", "panettone", "panettone = bolo de Natal de Milão",
     "Il ___ è il dolce simbolo di Milano.", instr="Completar", size=20, gap=8)
e.ex("A2", "Completar as frases", "torrone", "torrone = torrão",
     "A Cremona si festeggia il ___.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "assaggio", "assaggio = prova",
     "Alla finale del Panettone, il pubblico può fare un ___ gratis.", instr="Completar", size=20, gap=8)
e.ex("A2", "Completar as frases", "bancarella", "bancarella = banca",
     "Alla festa ci sono tante ___ con i dolci.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "mandorle", "mandorle = amêndoas, plural",
     "Il torrone è fatto di ___ e miele.", instr="Completar", size=20, gap=8)
e.ex("A2", "Completar as frases", "tartufo", "tartufo = trufa",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="Completar", size=20, gap=8)
e.head("C　IL PASSATO PROSSIMO", 25)
e.bridge("Complete com o passato prossimo — atenção aos auxiliares avere e essere.")
e.ex("B1", "Completar as frases", "è arrivato", "arrivare leva essere: è arrivato",
     "Il primo freddo ___ (arrivare) lunedì.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "abbiamo assaggiato", "assaggiare leva avere: abbiamo assaggiato",
     "Noi ___ (assaggiare) il panettone a Milano.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "sono andati", "andare leva essere, plural sono andati",
     "I pasticceri ___ (andare) a Milano per la finale.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "ha aperto", "aprire leva avere: ha aperto",
     "Cremona ___ (aprire) la Festa del Torrone sabato.", instr="Completar", size=20, gap=8)
e.head("D　COSTRUISCI LE FRASI", 25)
e.bridge("Ponha as palavras na ordem certa.")
e.ex("B1", "Formar frases", "La finale è a Milano il 7 novembre.", "Sujeito, essere, lugar, data",
     "la finale / è a Milano / il 7 novembre → ___", instr="Formar frases", size=20, gap=8)
e.ex("A2", "Formar frases", "A Cremona il torrone è il re.", "Lugar primeiro, sujeito depois",
     "a Cremona / il torrone / è il re → ___", instr="Formar frases", size=20, gap=8)
e.ex("B1", "Formar frases", "La fiera dura fino al 6 dicembre.", "dura fino a = dura até",
     "la fiera / dura / fino al 6 dicembre → ___", instr="Formar frases", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　ESPORTES", "La Lucerna", "LIVELLO B1　La Serie A e l'Europa　A Serie A e a Europa")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("L'undicesima giornata: Genoa–Milan, Inter–Como, Fiorentina–Juventus", 32)
f.byline("Dalla redazione sportiva de La Lucerna　Livello di lettura: B1")
f.para("È una settimana di grande calcio. Da martedì 3 a giovedì 5 novembre si gioca la quarta giornata delle coppe europee: Champions League, Europa League e Conference League. Attenzione: queste partite si giocano dopo la chiusura del giornale — qui sono una presentazione, senza risultati.")
f.para("Poi arriva l'undicesima giornata di Serie A, da venerdì 6 a domenica 8 novembre. La giornata chiude domenica 8 novembre con tre partite grandi: Genoa–Milan, Inter–Como e Fiorentina–Juventus, la sera a Firenze.")
f.para("Domenica è anche il giorno del freddo sugli spalti: chi va allo stadio mette sciarpa e guanti, come a pagina 2. Ma il calcio non si ferma per il primo freddo — anzi, con il freddo le partite della sera diventano ancora più belle, sotto le luci.")
f.para("E per chi segue i giovani: anche le squadre giovani giocano nel weekend. Il consiglio della redazione è uno solo: scegli una partita, guarda il calendario e non perderti la domenica sera a Firenze.")
f.gloss("la giornata jornada · la presentazione antevisão · gli spalti bancadas · la sera noite")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Martedì 3 – giovedì 5 novembre · Coppe europee, 4ª giornata — si giocano dopo la chiusura del giornale. Venerdì 6 – domenica 8 novembre · Serie A, 11ª giornata. Domenica 8 novembre · Genoa – Milan; Inter – Como; Fiorentina – Juventus (sera, a Firenze).", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi domenica sera? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Que jogo vais ver no domingo à noite? Escreve duas frases em italiano e envia-as.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU?　E tu?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Que jogo vais ver no domingo à noite? Escreve duas frases em italiano e envia-as.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DEL CALCIO　Semana do futebol", 26, "sans", True, OLIVE)
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
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, OLIVE)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 470, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Attenzione: le partite europee di martedì–giovedì e le partite di Serie A del weekend si giocano dopo la chiusura di questa edizione — per questo qui sono presentazioni, senza risultati."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "ESERCIZI　Exercícios da página 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　Os níveis misturam-se — procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P4-ex")
e.head("A　COMPRENSIONE", 25)
e.bridge("Leia o artigo da página 4 e escolha a resposta certa.")
e.ex("B1", "Uma opção", "B", "A jornada 11 da Serie A fecha no domingo",
     "L'undicesima giornata di Serie A chiude... A. venerdì · B. domenica 8 novembre · C. lunedì", size=20, gap=8)
e.ex("B1", "Uma opção", "B", "No domingo à noite joga-se Fiorentina–Juventus",
     "Domenica sera, a Firenze, si gioca... A. Inter–Como · B. Fiorentina–Juventus · C. Genoa–Milan", size=20, gap=8)
e.ex("B1", "Uma opção", "A", "A jornada 4 das taças europeias é de 3 a 5 de novembro",
     "La quarta giornata delle coppe europee si gioca... A. dal 3 al 5 novembre · B. dal 6 all'8 novembre · C. il 2 novembre", size=20, gap=8)
e.ex("B1", "Uma opção", "C", "Os jogos europeus são antevisões, sem resultados",
     "Le partite europee, in questo giornale, sono... A. risultati finali · B. cancellate · C. presentazioni senza risultati", size=20, gap=8)
e.ex("B1", "Uma opção", "B", "Inter–Como joga-se em San Siro",
     "Inter–Como si gioca... A. a Firenze · B. a San Siro · C. a Genova", size=20, gap=8)
e.head("B　LE PAROLE", 25)
e.match_set("B1", "Ligar palavras",
            ["la giornata", "la presentazione", "gli spalti", "la sera"],
            ["il posto del pubblico allo stadio, con le gradinate",
             "il racconto prima della partita, senza risultati",
             "ciascuna delle parti del campionato, una dopo l'altra",
             "la parte del giorno dopo il tramonto, con le luci accese"],
            ["c", "b", "a", "d"],
            ["giornata = uma jornada do campeonato, c", "presentazione = antevisão, b", "spalti = bancadas, a", "sera = noite, d"],
            instr="Combinar")
e.head("C　I COMPARATIVI", 25)
e.bridge("Preencha com o comparativo da palavra entre parênteses — ver a tabela de jogos.")
e.ex("B1", "Completar as frases", "più tardi", "Domingo à noite é mais tarde que sexta: più tardi",
     "Le partite di domenica sera cominciano ___ di quelle di venerdì. (tardi)", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "più presto", "Sexta é mais cedo que domingo: più presto",
     "Le partite di venerdì cominciano ___ di quelle di domenica. (presto)", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "più bella", "più + bella: a mais bela, segundo os adeptos",
     "Per i tifosi, la domenica sera è la serata ___ del weekend. (bella)", instr="Completar", size=20, gap=8)
e.ex("B2", "Padrões de frase", "meglio", "O comparativo de bene é o irregular meglio",
     "L'Inter gioca bene. → L'Inter gioca ___ (bene).", instr="Completar", size=20, gap=8)
e.head("D　IL PASSATO DELLO SPORT", 25)
e.bridge("Complete com o passato prossimo.")
e.ex("B1", "Completar as frases", "ha vinto", "vincere: ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "ha pareggiato", "pareggiare: ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="Completar", size=20, gap=8)
e.ex("B2", "Completar as frases", "sono arrivati", "arrivare leva essere, plural sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "abbiamo guardato", "guardare leva avere: abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="Completar", size=20, gap=8)
e.ex("B1", "Completar as frases", "ha preso", "O particípio de prendere é preso: ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="Completar", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
