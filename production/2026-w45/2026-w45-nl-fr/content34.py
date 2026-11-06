# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-nl-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · Nuit des musées, livres et art")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Amsterdam blijft wakker: de Museumnacht", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: A2 → B1")
f.para("Zaterdagavond 7 november blijft Amsterdam wakker: het is Museumnacht, de 26e editie. Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts, met muziek, workshops en rondleidingen. Eén kaartje geeft toegang tot alle deelnemende musea.")
f.para("Let op: de Museumkaart geldt deze avond niet — je hebt een apart kaartje nodig. Populaire musea werken met tijdsloten: reserveer op tijd, anders sta je in de rij. Veel bezoekers gaan op de fiets van museum naar museum; er rijden ook extra nachtbussen.")
f.para("In Den Haag is het deze week Crossing Border Festival, van dinsdag tot en met zondag: schrijvers en muzikanten delen het podium. Literatuur en muziek horen bij elkaar, zeggen de organisatoren — een boek kan klinken als een lied, en een lied kan lezen als een verhaal.")
f.para("En de kunstbeurs PAN Amsterdam in de RAI loopt nog tot en met zondag 8 november: kunst, antiek en design uit alle eeuwen, van oud porselein tot nieuwe meubels.")
f.head("TWEEDEHANDS IS OOK CULTUUR", 25)
f.para("In Zaandam is op 7 en 8 november de Mega Snuffelmarkt, met zo'n 250 kramen vol tweedehands spullen: boeken, platen, kleding en speelgoed. Tweedehands kopen is ook klimaatvriendelijk: wat al bestaat, hoeft niet opnieuw gemaakt te worden.")
f.para("En wie na de markt nog energie heeft, fietst 's avonds naar Amsterdam: daar begint om 19:00 uur de Museumnacht.")
f.gloss("het museum : le musée · de rondleiding : la visite guidée · het tijdslot : le créneau horaire · tweedehands : d'occasion · de beurs : la foire, le salon.")
f.end_report()

# col 3: image + facts box (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Een boot in een Amsterdamse gracht. Tijdens Museumnacht fietst en vaart de stad de hele nacht door.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["26e editie van Museumnacht, zaterdag 7 november, 19:00–02:00 uur.",
         "Meer dan 70 musea doen mee; de Museumkaart geldt niet.",
         "PAN Amsterdam in de RAI, tot en met zondag 8 november."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "MUSEUMNACHT IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · EXERCICES", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · exercices mélangés par niveau, cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · BEGRIJPEN", 25)
e.bridge("Lisez l'article de la page 3 et choisissez la bonne réponse.")
e.ex("A2", "单选", "B", "La Nuit des musées : samedi 7 novembre",
     "Museumnacht is op... A. vrijdag 6 november · B. zaterdag 7 november · C. zondag 8 november", size=20, gap=8)
e.ex("A2", "单选", "B", "Les musées sont ouverts jusqu'à 2 heures du matin",
     "De musea zijn open tot... A. 24:00 uur · B. 02:00 uur · C. 19:00 uur", size=20, gap=8)
e.ex("A2", "单选", "C", "Crossing Border a lieu à La Haye",
     "Crossing Border is in... A. Amsterdam · B. Rotterdam · C. Den Haag", size=20, gap=8)
e.ex("A2", "单选", "A", "Crossing Border combine livres et musique",
     "Crossing Border combineert... A. boeken en muziek · B. voetbal en dans · C. film en eten", size=20, gap=8)
e.ex("A2", "单选", "B", "La foire PAN dure jusqu'au 8 novembre",
     "PAN Amsterdam loopt tot en met... A. zaterdag 7 november · B. zondag 8 november · C. maandag 9 november", size=20, gap=8)
e.head("B · WOORDEN UIT DE TEKST", 25)
e.bridge("Complétez avec les mots de l'encadré. Attention : certains mots passent au pluriel.")
e.para("museum · rondleiding · tijdslot · tweedehands · beurs", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "musea", "museum au pluriel : musea",
     "Op Museumnacht zijn meer dan 70 ___ open.", instr="Compléter", size=20, gap=8)
e.ex("A2", "完成句子", "rondleiding", "rondleiding = visite guidée",
     "Een ___ laat je de mooiste zalen zien.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "tijdslot", "tijdslot = créneau horaire",
     "Reserveer een ___ voor populaire musea.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "tweedehands", "tweedehands = d'occasion",
     "Op de Snuffelmarkt koop je ___ spullen.", instr="Compléter", size=20, gap=8)
e.ex("A2", "完成句子", "beurs", "beurs = foire, salon",
     "PAN is een ___ voor kunst en antiek.", instr="Compléter", size=20, gap=8)
e.head("C · HET PERFECTUM", 25)
e.bridge("Complétez au parfait, avec l'auxiliaire hebben ou zijn.")
e.ex("B1", "完成句子", "zijn geweest", "parfait de zijn : zijn geweest",
     "De musea ___ (zijn) tot 02:00 uur open.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "hebben gekocht", "parfait de kopen : hebben gekocht",
     "Wij ___ (kopen) één kaartje voor alle musea.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "hebben voorgelezen", "parfait de voorlezen : hebben voorgelezen",
     "De schrijvers ___ (voorlezen) hun werk op het podium.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "zijn gekomen", "komen se conjugue avec zijn : zijn gekomen",
     "Veel bezoekers ___ (komen) met de fiets.", instr="Compléter", size=20, gap=8)
e.head("D · REKENEN", 25)
e.bridge("Calculez avec les chiffres de la page 3.")
e.ex("B1", "完成句子", "7", "De 19 h à 2 h : 7 heures",
     "Museumnacht duurt van 19:00 tot 02:00 uur: ___ uur.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "8", "Du 1er au 8 novembre : 8 jours",
     "PAN Amsterdam loopt van 1 tot en met 8 november: ___ dagen.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "6", "Du mardi 3 au dimanche 8 novembre : 6 jours",
     "Crossing Border duurt van dinsdag 3 tot en met zondag 8 november: ___ dagen.", instr="Compléter", size=20, gap=8)
e.ex("B2", "完成句子", "125", "La moitié de 250 est 125",
     "De Snuffelmarkt heeft zo'n 250 kramen; de helft is ___.", instr="Compléter", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · SPORT", "De Lucerna", "NIVEAU B1 · Europese week en speelronde 12 · Semaine européenne et 12e journée")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Europa: drie keer feest, twee keer verlies", 37)
f.byline("Van de redactie van De Lucerna · Leesniveau: B1")
f.para("De Europese week is voorbij — en de balans is drie keer feest, twee keer verlies. Ajax won donderdag 22 oktober met 2–0 van Atalanta in de Conference League. Twente won met 4–1 bij Lincoln Red Imps in Gibraltar. AZ won met 4–0 van Ararat-Armenia. NEC verloor: 2–4 bij Dinamo Zagreb.")
f.para("En woensdag 21 oktober verloor Feyenoord in de Champions League: Real Betis won met 1–0 in Sevilla, door een doelpunt van Isco in de 59e minuut. Feyenoord had wel meer balbezit, maar schoot te weinig op doel.")
f.para("In de Eredivisie was het zondag 25 oktober ook spannend: PSV en Feyenoord speelden 1–1 gelijk. Ajax won met 2–1 bij Sparta. En Twente won met 2–0 bij AZ. Na 10 ronden staat Feyenoord bovenaan met 24 punten, Ajax heeft 21, en PSV, Twente en AZ hebben elk 20 punten.")
f.para("Nu speelronde 12. Vrijdagavond: Willem II tegen PEC Zwolle (19:00 uur). Zaterdag: Fortuna tegen Telstar (15:30), ADO tegen Sparta (17:45) en Excelsior tegen Go Ahead Eagles (20:00). Zondag de topper: Heerenveen tegen Feyenoord (11:15) en Twente tegen Ajax (13:30), plus Cambuur tegen PSV, AZ tegen Groningen (15:45) en Utrecht tegen NEC (19:00).")
f.head("DE STAND NA 10 RONDEN", 25)
f.para("Feyenoord 24 punten, Ajax 21, PSV 20, Twente 20, AZ 20. Onderaan staan ADO en Telstar met 6 punten en Willem II met 2 punten. Maar er zijn nog 24 ronden te gaan: alles kan nog veranderen.")
f.gloss("de balans : le bilan · gelijkspelen : faire match nul · de speelronde : la journée · de topper : le grand match · de stand : le classement.")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Voetbal is al meer dan honderd jaar de sport van Nederland.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Donderdag 22 oktober: Ajax – Atalanta 2–0; Twente – Lincoln 4–1; AZ – Ararat 4–0; Dinamo – NEC 4–2.",
         "Woensdag 21 oktober: Real Betis – Feyenoord 1–0.",
         "Zondag 25 oktober: PSV – Feyenoord 1–1; Sparta – Ajax 1–2; AZ – Twente 0–2.",
         "Speelronde 12: vrijdag Willem II – PEC; zondag Heerenveen – Feyenoord (11:15) en Twente – Ajax (13:30)."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "HET PROGRAMMA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy3 + sh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "OEFENINGEN · EXERCICES", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Réponses page 8 · exercices mélangés par niveau, cherchez par numéro", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · BEGRIJPEN", 25)
e.bridge("Lisez l'article de la page 4 et choisissez la bonne réponse.")
e.ex("B1", "单选", "B", "L'Ajax bat l'Atalanta 2–0",
     "Ajax won donderdag met... A. 1–0 · B. 2–0 · C. 4–1", size=20, gap=8)
e.ex("B1", "单选", "C", "Twente bat Lincoln 4–1",
     "Twente won bij Lincoln met... A. 2–0 · B. 4–0 · C. 4–1", size=20, gap=8)
e.ex("B1", "单选", "A", "NEC perd 2–4 contre le Dinamo Zagreb",
     "NEC verloor met... A. 2–4 · B. 4–2 · C. 1–0", size=20, gap=8)
e.ex("B1", "单选", "B", "Le Real Betis bat Feyenoord 1–0",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=20, gap=8)
e.ex("B1", "单选", "B", "Après 10 journées, Feyenoord mène avec 24 points",
     "Na 10 ronden staat Feyenoord... A. tweede · B. eerste met 24 punten · C. derde", size=20, gap=8)
e.head("B · WOORDEN UIT DE TEKST", 25)
e.bridge("Complétez avec les mots de l'encadré. Attention à la forme du verbe.")
e.para("balans · gelijkspelen · topper · stand · doelpunt", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "balans", "balans = bilan",
     "De ___ van de Europese week is: drie keer feest, twee keer verlies.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "speelden gelijk", "gelijkspelen au passé, pluriel : speelden gelijk",
     "PSV en Feyenoord ___ (gelijkspelen): 1–1.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "topper", "topper = grand match",
     "Heerenveen – Feyenoord is de ___ van zondag.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "stand", "stand = classement",
     "Op de ___ staat Feyenoord bovenaan.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "doelpunt", "doelpunt = but",
     "Isco maakte het enige ___ van Betis – Feyenoord.", instr="Compléter", size=20, gap=8)
e.head("C · VERLEDEN TIJD", 25)
e.bridge("Complétez au passé ou au parfait.")
e.ex("B1", "完成句子", "won", "winnen au passé : won",
     "Ajax ___ (winnen) donderdag met 2–0.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "ging", "gaan au passé : ging",
     "De bal ___ (gaan) in het doel: 1–0 voor Betis.", instr="Compléter", size=20, gap=8)
e.ex("B1", "完成句子", "verloor", "verliezen au passé : verloor",
     "Feyenoord ___ (verliezen) met 1–0 in Sevilla.", instr="Compléter", size=20, gap=8)
e.ex("B2", "完成句子", "zijn gekomen", "parfait de komen, avec zijn",
     "Veel supporters ___ (komen) naar het stadion.", instr="Compléter", size=20, gap=8)
e.head("D · WAAR OF NIET WAAR?", 25)
e.ex("B1", "判断对错", "Waar", "Vrai : l'Ajax gagne 2–0",
     "Ajax won donderdag met 2–0 van Atalanta. Waar of niet waar?", instr="Vrai ou faux", size=20, gap=8)
e.ex("B1", "判断对错", "Niet waar", "Faux : NEC perd 2–4",
     "NEC won met 4–2 bij Dinamo Zagreb. Waar of niet waar?", instr="Vrai ou faux", size=20, gap=8)
e.ex("B1", "判断对错", "Niet waar", "Faux : Twente – Ajax joue à 13 h 30 ; 11 h 15, c'est Heerenveen – Feyenoord",
     "Twente – Ajax is zondag om 11:15 uur. Waar of niet waar?", instr="Vrai ou faux", size=20, gap=8)
e.ex("B1", "判断对错", "Waar", "Vrai : après 10 journées, Feyenoord est premier avec 24 points",
     "Feyenoord staat na 10 ronden bovenaan met 24 punten. Waar of niet waar?", instr="Vrai ou faux", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
