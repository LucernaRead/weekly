# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-it-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURA (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURA · CULTURE", "La Lucerna", "A2 → B1 · Le sagre d'autunno · Les fêtes de l'automne")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-main")
f.title("Le sagre d'autunno: il tartufo bianco è il re", 37)
f.byline("Dalla redazione de La Lucerna · Livello di lettura: A2 → B1")
f.para("In autunno, l'Italia mangia fuori casa. Nei paesi e nelle città è la stagione delle sagre: feste di piazza con i prodotti della terra. Il re della stagione è il tartufo bianco, il fungo più prezioso d'Italia.")
f.para("Ad Alba, in Piemonte, la Fiera del Tartufo Bianco è aperta dal 10 ottobre al 6 dicembre: quasi due mesi di mercati, profumi e piatti speciali. La fiera è iniziata sabato 10 ottobre e chiude domenica 6 dicembre.")
f.para("Questo fine settimana, sabato 24 e domenica 25 ottobre, Montaione, in Toscana, celebra la sua festa del tartufo. E a Bagolino, in Lombardia, il weekend è del formaggio Bagòss: un formaggio di montagna dal nome difficile e dal sapore forte.")
f.para("Sempre sabato 24 ottobre apre a Volterra Volterragusto, una festa dei sapori della Toscana. E ovunque, nelle piazze, si trovano le castagne arrosto: l'autunno italiano ha il profumo della castagna calda.")
f.gloss("il tartufo = la truffe · la sagra = la fête gastronomique · il profumo = le parfum · arrosto = rôti · la pittrice = la femme peintre.")
f.head("UNA GRANDE PITTRICE A FIRENZE", 25)
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
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LE SAGRE DEL WEEKEND", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "E tu? Qual è il piatto dell'autunno nel tuo paese? Scrivi due frasi in italiano e mandale alla redazione."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Et chez toi, que mange-t-on en automne ? Écris deux phrases et envoie-les.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "E TU? · ET TOI ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Et chez toi, que mange-t-on en automne ? Écris deux phrases et envoie-les.", 20, "sans", False, GREY, CW - 44, 1.42)
ay3 = ey3 + eh + 22
image(p, "artemisia.jpg", ix, ay3, CW, 165)
acy = caption(p, ix, ay3 + 165, CW, "Artemisia Gentileschi, «Giuditta decapita Oloferne» (versione di Napoli). A Firenze, la sua mostra apre mercoledì 21 ottobre.",
              "Foto: Wikimedia Commons — dominio pubblico")
print("P3 col3 ends", acy)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · EXERCICES", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · Exercices mélangés par niveau, cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · COMPRENSIONE", 25)
e.expl("Lisez l'article page 3 et choisissez la bonne réponse.")
e.ex("A2", "单选", "B", "la fête de la truffe blanche est à Alba",
     "La Fiera del Tartufo Bianco è a... A. Bagolino · B. Alba · C. Volterra", size=20, gap=8)
e.ex("A2", "单选", "C", "la foire d'Alba ferme le 6 décembre",
     "La fiera di Alba chiude... A. il 25 ottobre · B. il 1° novembre · C. il 6 dicembre", size=20, gap=8)
e.ex("A2", "单选", "B", "à Bagolino, le week-end du fromage Bagòss",
     "A Bagolino, il weekend è del... A. tartufo · B. formaggio Bagòss · C. vino", size=20, gap=8)
e.ex("B1", "单选", "A", "l'exposition Artemisia ouvre le mercredi 21 octobre",
     "La mostra su Artemisia apre... A. mercoledì 21 ottobre · B. sabato 24 ottobre · C. domenica 25 ottobre", size=20, gap=8)
e.ex("B1", "单选", "B", "l'exposition présente aussi deux œuvres de Caravage",
     "Nella mostra ci sono anche opere di... A. Leonardo · B. Caravaggio · C. Michelangelo", size=20, gap=8)
e.head("B · LE PAROLE DEL TESTO", 25)
e.expl("Complétez avec les mots du cadre.")
e.para("tartufo · sagra · profumo · castagne · pittrice · formaggio", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "tartufo", "tartufo = la truffe",
     "Il ___ bianco è il fungo più prezioso d'Italia.", instr="Compléter", size=20, gap=8)
e.ex("A2", "完成句子", "sagra", "sagra = fête gastronomique locale",
     "Una ___ è una festa di piazza con i prodotti della terra.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "profumo", "profumo = le parfum",
     "L'autunno ha il ___ della castagna calda.", instr="Compléter", size=20, gap=8)
e.ex("A2", "完成句子", "castagne", "castagne arrosto = châtaignes grillées (pluriel)",
     "Nelle piazze si trovano le ___ arrosto.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "pittrice", "pittrice = la femme peintre",
     "Artemisia è una grande ___ del Seicento.", instr="Compléter", size=20, gap=8)
e.ex("A2", "完成句子", "formaggio", "formaggio = le fromage",
     "Il Bagòss è un ___ di montagna.", instr="Compléter", size=20, gap=8)
e.head("C · IL PASSATO PROSSIMO", 25)
e.expl("Complétez au passato prossimo, en choisissant l'auxiliaire avere ou essere.")
e.ex("B1", "完成句子", "è iniziata", "iniziare prend essere, féminin : è iniziata",
     "La fiera ___ (iniziare) il 10 ottobre.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "abbiamo visitato", "visitare prend avere : abbiamo visitato",
     "Noi ___ (visitare) la mostra di Artemisia.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "è andato", "andare prend essere : è andato",
     "Marco ___ (andare) alla sagra sabato.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "hanno aperto", "aprire prend avere : hanno aperto",
     "Le sagre ___ (aprire) il fine settimana.", instr="Compléter", size=20, gap=8)
e.head("D · COSTRUISCI LE FRASI", 25)
e.expl("Formez une phrase correcte avec ces mots.")
e.ex("B1", "造句", "La fiera è iniziata il 10 ottobre.", "sujet + essere + participe + date",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="Former une phrase", size=20, gap=8)
e.ex("A2", "造句", "A Bagolino il formaggio è il re.", "le lieu d'abord, le sujet après",
     "a Bagolino / il formaggio / è il re → ___", instr="Former une phrase", size=20, gap=8)
e.ex("B1", "造句", "La mostra resta aperta fino ad aprile.", "= reste ouverte",
     "la mostra / resta aperta / fino ad aprile → ___", instr="Former une phrase", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultura.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · SPORT", "La Lucerna", "LIVELLO B1 · La Serie A e l'Europa · La Serie A et l'Europe")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1080, tag="P4-main")
f.title("L'ottava giornata: Napoli–Roma e Inter–Fiorentina", 37)
f.byline("Dalla redazione sportiva de La Lucerna · Livello di lettura: B1")
f.para("È una settimana di grande calcio. Mercoledì sera l'Inter gioca in Champions League a San Siro contro lo Shakhtar Donetsk (21:00), e giovedì l'Atalanta è in trasferta ad Amsterdam contro l'Ajax, in Conference League. Attenzione: queste partite si giocano dopo la chiusura del giornale — qui sono una presentazione, senza risultati.")
f.para("Poi arriva l'ottava giornata di Serie A, da venerdì 23 a domenica 25 ottobre. La partita più attesa è sabato 24 ottobre alle 18:00: Napoli–Roma, la grande sfida tra il Sud e la capitale.")
f.para("Domenica 25 ottobre, alle 12:30, l'Inter incontra la Fiorentina a San Siro. È una partita speciale: è la prima della domenica con l'ora solare. Chi guarda la partita a pranzo ha già dormito un'ora in più.")
f.para("E dall'America arriva il basket: la stagione NBA comincia questa settimana, e anche in Italia si cercano notizie su Spurs–Thunder, la partita di Wembanyama (ricerca in crescita su Google Trends in Italia, istantanea di martedì).")
f.gloss("la giornata = la journée · la sfida = le choc · la presentazione = la présentation · in trasferta = à l'extérieur.")
f.end_report()

# col 3: data box + e tu? (sequential)
bx = COLX[3]
p.rect(bx, 200, CW, 436, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx + 22, 240, "LE PARTITE DA SEGNARE", 23, "sans", True, OLIVE)
p.para(bx + 22, 282, "Mercoledì 21 ottobre, 21:00 · Inter – Shakhtar Donetsk (Champions League, San Siro) — si gioca dopo la chiusura del giornale. Giovedì 22 ottobre · Ajax – Atalanta (Conference League, Amsterdam) — presentazione. Sabato 24 ottobre, 18:00 · Napoli – Roma (Serie A, 8ª giornata). Domenica 25 ottobre, 12:30 · Inter – Fiorentina (Serie A) — la prima partita con l'ora solare.", 21.5, "serif", False, INK, CW - 44, 1.42)
ey3 = 662
etvous = "E tu? Quale partita guardi questo fine settimana? Scrivi due frasi in italiano."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Quel match regardes-tu ce week-end ? Écris deux phrases en italien et envoie-les.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(bx + 22, yy3 + 26, "E TU? · ET TOI ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Quel match regardes-tu ce week-end ? Écris deux phrases en italien et envoie-les.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P4 col3 ends", ey3 + eh)

# ---- fixture table (full width) ----
ty = 1140
p.text(MX, ty, "LA SETTIMANA DEL CALCIO · LA SEMAINE DU FOOTBALL", 26, "sans", True, OLIVE)
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
    p.text(MX + 18, yy + 29, d, 20.5, "sans", True, BRICK)
    p.text(MX + 185, yy + 29, t, 20, "sans", False, GREY)
    p.text(MX + 430, yy + 29, m, 21, "serif", False, INK)
    yy += 44
tnote = "Attenzione: le partite di mercoledì e giovedì finiscono dopo la chiusura di questa edizione — per questo qui sono presentazioni, senza risultati."
p.para(MX, yy + 26, tnote, 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "ESERCIZI · EXERCICES", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · Exercices mélangés par niveau, cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · COMPRENSIONE", 25)
e.expl("Lisez l'article page 4 et choisissez la bonne réponse.")
e.ex("B1", "单选", "B", "l'Inter joue mercredi contre le Shakhtar Donetsk",
     "L'Inter gioca mercoledì contro... A. l'Ajax · B. lo Shakhtar Donetsk · C. la Roma", size=20, gap=8)
e.ex("B1", "单选", "B", "Napoli–Roma, samedi à 18:00",
     "Napoli–Roma si gioca... A. venerdì · B. sabato alle 18:00 · C. domenica a mezzanotte", size=20, gap=8)
e.ex("B1", "单选", "A", "c'est le premier match du dimanche avec l'heure d'hiver",
     "Inter–Fiorentina è speciale perché... A. è la prima partita con l'ora solare · B. è una finale · C. si gioca di notte", size=20, gap=8)
e.ex("B1", "单选", "C", "l'Atalanta joue jeudi à l'extérieur, à Amsterdam",
     "L'Atalanta gioca giovedì... A. a San Siro · B. a Roma · C. ad Amsterdam", size=20, gap=8)
e.ex("B1", "单选", "B", "présentations, sans résultats",
     "Le partite di mercoledì e giovedì, in questo giornale, sono... A. risultati finali · B. presentazioni senza risultati · C. cancellate", size=20, gap=8)
e.head("B · LE PAROLE", 25)
e.match_set("B1", "词汇配对",
            ["la giornata", "la sfida", "la trasferta", "San Siro"],
            ["lo stadio dell'Inter e del Milan, a Milano",
             "una partita importante tra due squadre forti",
             "ciascuna delle parti del campionato, una dopo l'altra",
             "la partita fuori casa, nella città degli avversari"],
            ["c", "b", "d", "a"],
            ["giornata = une journée de championnat c", "sfida = le choc entre deux grandes équipes b", "trasferta = le match à l'extérieur d", "San Siro = le stade de Milan a"],
            instr="Associer")
e.head("C · I COMPARATIVI", 25)
e.expl("Complétez avec le comparatif du mot entre parenthèses (données : le tableau des matchs).")
e.ex("B1", "完成句子", "più tardi", "18:00 est plus tard que 12:30 : più tardi",
     "Napoli–Roma comincia ___ di Inter–Fiorentina. (tardi)", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "più presto", "12:30 est plus tôt que 18:00 : più presto",
     "La partita di domenica comincia ___ di quella di sabato. (presto)", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "più bella", "più + bella : la plus belle de la semaine (avis subjectif)",
     "Per i tifosi, Napoli–Roma è la partita ___ del weekend. (bella)", instr="Compléter", size=20, gap=8)
e.ex("B2", "句型转换", "meglio", "le comparatif de bene est irrégulier : meglio",
     "L'Inter gioca bene. → L'Inter gioca ___ (bene).", instr="Compléter", size=20, gap=8)
e.head("D · IL PASSATO DELLO SPORT", 25)
e.expl("Complétez au passato prossimo.")
e.ex("B1", "完成句子", "ha vinto", "vincere : ha vinto",
     "La mia squadra ___ (vincere) la partita di ieri.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "ha pareggiato", "pareggiare : ha pareggiato",
     "La mia squadra ___ (pareggiare) 1–1.", instr="Compléter", size=20, gap=8)
e.ex("B2", "完成句子", "sono arrivati", "arrivare prend essere, pluriel : sono arrivati",
     "I tifosi ___ (arrivare) allo stadio alle cinque.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "abbiamo guardato", "guardare prend avere : abbiamo guardato",
     "Noi ___ (guardare) la partita in televisione.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "ha preso", "le participe de prendere est preso : ha preso",
     "Il portiere ___ (prendere) un gol al 90°.", instr="Compléter", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
