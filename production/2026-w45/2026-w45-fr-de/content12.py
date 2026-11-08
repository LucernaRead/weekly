# -*- coding: utf-8 -*-
"""W45 FR core VOL.2 — P1 + P2. Issue week Mon 2 – Sun 8 Nov 2026."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

p.text(MX, 92, "VOL. 2　AUSGABE NR. 2", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "HEBDOMADAIRE EN FRANÇAIS　JEDE WOCHE　FRANZÖSISCH, WIE FRANKREICH ES LIEST", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMAINE DU 2 AU 8 NOVEMBRE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Le Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "FRANZÖSISCHE WOCHENZEITUNG　VOL.2　FINALWOCHENENDE", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "LE JOURNAL DES APPRENANTS DE FRANÇAIS — LIRE LA VRAIE VIE, EN FRANÇAIS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# rentrée band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "LUNDI 2 NOVEMBRE : LA FRANCE REPREND !", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Ce matin, les élèves reprennent les cours. Le Masters commence, Pitchfork ouvre.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "MONTAG SCHULBEGINN　IN GANZ FRANKREICH", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "MASTERS-BEGINN　FESTIVAL-ERÖFFNUNG　SIEHE SEITE 2", 18, "sans", False, GOOSE, anchor="end")

# pairing badge — FR-family shipped precedent (FR×ZH-TW): inserted at y=574, 22pt BRICK, centred, reader-language form
p.text(975, 612, "FRANZÖSISCHER TEXT　DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 16, "sans", False, GREY, anchor="middle")

# ---- headline (span cols 0-2) ----
hy = 610
p.text(MX, hy + 26, "SPORT　CULTURE　GASTRONOMIE　LA UNE　FINALWOCHENENDE", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Paris, Plailly, Port-en-Bessin : le week-end où tout se joue", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Par la rédaction du Lucerna　Niveau de lecture : A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1812, tag="P1-headline")
f.para("Lundi 2 novembre, la France reprend : les vacances de la Toussaint sont finies, les élèves retournent à l'école, et une grande semaine commence. Elle se terminera en beauté, le week-end du 7 et 8 novembre, avec trois finales en même temps.", 24, "serif", False, INK, 1.45)
f.para("À Nanterre, dimanche 8 novembre, on joue les finales du Rolex Paris Masters, le dernier grand tournoi de tennis de la saison. Les quarts de finale ont lieu vendredi 6, les demi-finales samedi 7. Attention : au moment où nous écrivons, on ne connaît pas encore les finalistes — ils seront connus samedi soir, après les demi-finales.", 24, "serif", False, INK, 1.45)
f.para("À Plailly, dans l'Oise, c'est la dernière semaine de « Peur sur le Parc » : la dernière soirée nocturne a lieu samedi 7 novembre, de 19 heures à 1 heure du matin, et le parc ferme dimanche 8 novembre. Les enfants sensibles ont un badge gratuit contre les monstres.", 24, "serif", False, INK, 1.45)
f.para("À Port-en-Bessin, en Normandie, on fête la coquille Saint-Jacques : « Le Goût du Large », samedi 7 et dimanche 8 novembre, 22e édition. On y vend des coquilles et on goûte des recettes au bord de la mer.", 24, "serif", False, INK, 1.45)
f.para("Trois villes, trois finales, un seul week-end : Paris pour le tennis, Plailly pour les frissons, Port-en-Bessin pour les saveurs. Suite en pages 3 et 4.", 24, "serif", False, INK, 1.45)
f.gloss("se jouer entscheiden · une finale Finale · une demi-finale Halbfinale · un quart de finale Viertelfinale · une nocturne Nachtevent · un frisson Nervenkitzel · la coquille Saint-Jacques Jakobsmuschel.")
f.box("LES DATES　FINALWOCHENENDE", [
    ("sam. 7 nov. — demis + nocturne + Goût du Large", "serif", False, INK, 21.5, 1.4),
    ("dim. 8 nov. — finales + fermeture du parc + Goût du Large", "serif", False, INK, 21.5, 1.4),
])
f.head("À VOUS !　SIE SIND DRAN", 25)
f.ex("A2", "Satzergänzung", "finales", "Finale am Sonntag, 8. Nov.",
     "Dimanche 8 novembre, on joue les ___ du Masters de Paris.", size=21.5)
f.ex("A2", "Satzergänzung", "nocturne", "Letzte Nachtveranstaltung am Samstag, 7. Nov.",
     "Samedi 7 novembre, c'est la dernière ___ de Peur sur le Parc.", size=21.5)
f.ex("A2", "Satzergänzung", "coquilles", "In Port-en-Bessin gibt es Jakobsmuscheln",
     "À Port-en-Bessin, on vend des ___ Saint-Jacques.", size=21.5)
f.ex("B1", "Satzergänzung", "reprend", "Schulbeginn am Montag, 2. Nov., in ganz Frankreich",
     "Lundi 2 novembre, la France ___ les cours.", size=21.5)
f.ex("B1", "Satzergänzung", "samedi soir", "Finalisten erst nach den Halbfinals bekannt",
     "On connaîtra les finalistes ___ , après les demi-finales.", size=21.5)
f.ex("B1", "Satzergänzung", "saveurs", "Drei Finals: Tennis, Nervenkitzel, Genuss",
     "Plailly pour les frissons, Port-en-Bessin pour les ___.", size=21.5)
f.end_report()

# ---- agenda (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 668, fill=BOX)
p.text(gx + 22, gy + 40, "CETTE SEMAINE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "JOUR PAR JOUR", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "WOCHENPLAN　2. BIS 8. NOVEMBER", 19, "sans", False, GREY)
agenda = [
    ("lun. 2", "rentrée · Masters · Pitchfork"),
    ("mar. 3", "Assemblée : Culture, Médias"),
    ("mer. 4", "sorties cinéma · Créateurs"),
    ("jeu. 5", "Pitchfork Avant-Garde"),
    ("ven. 6", "quarts du Masters · Ligue 1"),
    ("sam. 7", "demis · nocturne · Goût"),
    ("dim. 8", "finales · Lens – Marseille"),
]
byy = gy + 150
for d, t in agenda:
    p.text(gx + 22, byy + 22, d, 21, "sans", True, OLIVE)
    p.text(gx + 118, byy + 22, t, 20, "serif", False, INK)
    byy += 62
p.text(gx + 22, byy + 16, "Les résultats du week-end final", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "seront connus samedi soir et dimanche.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "Finalergebnisse: Sa.-Abend und So.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f0eee5")
p.text(gx + 22, sy + 40, "DANS CE NUMÉRO　INHALT", 24, "sans", True, OLIVE)
som = [
    ("p.2", "La rentrée et les lectures", "A2"),
    ("p.3", "Halloween, Toussaint, Parc", "A2→B1"),
    ("p.4", "Masters de Paris, Ligue 1", "B1"),
    ("p.5", "Pitchfork à Paris", "B1"),
    ("p.6", "Le budget 2027 à l'Assemblée", "B2"),
    ("p.7", "Les phrases de la semaine", "A2→B2"),
    ("p.8", "Exercices et réponses", "tous"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 72, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- mot de la semaine (col 3) ----
my = 1652
p.text(gx, my + 24, "LE MOT DE LA SEMAINE", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« se jouer »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "se décider. Ce week-end, tout se joue : les finales, la fête, la saison.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "Sich entscheiden; sich abspielen.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "atget-paris.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "Paris, un matin de novembre : la ville reprend, les salles se remplissent, la semaine des finales commence.",
        "Eugène Atget (1857-1927), photographie, domaine public")
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-hiver")
f2.head("DEUXIÈME SEMAINE D'HIVER", 25)
f2.para("La France est passée à l'heure d'hiver dimanche 25 octobre. Cette semaine est donc la deuxième semaine à l'heure d'hiver : la nuit tombe tôt, les soirées sont longues.", 22.5)
f2.para("Que lit-on quand il fait nuit tôt ? La rédaction répond en page 2 : des romans courts, des nouvelles, et un bon chocolat chaud.", 22.5)
f2.end_report()
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "EN BREF　KURZ GEMELDET", 24, "sans", True, OLIVE)
brefs = [
    ("HALLOWEEN", "Samedi 31 octobre, les enfants se sont déguisés. Bilan en page 3."),
    ("TOUSSAINT", "Dimanche 1er novembre, les cimetières se sont remplis de fleurs. (page 3)"),
    ("JOUR DES MORTS", "Lundi 2 novembre : un jour de souvenir en famille, différent de la Toussaint. (page 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz éclair ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ ÉCLAIR　BLITZQUIZ", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Titelseite lesen, richtig antworten　Antworten auf Seite 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "Multiple Choice", "C", "Finale am Sonntag, 8. November",
      "Les finales du Masters ont lieu... A. vendredi 6 · B. samedi 7 · C. dimanche 8", size=21)
qf.ex("A2", "Multiple Choice", "A", "Muschelfest in Port-en-Bessin",
      "Le Goût du Large a lieu à... A. Port-en-Bessin · B. Dieppe · C. Courseulles", size=21)
qf.ex("A2", "Multiple Choice", "B", "Schulbeginn am Montagmorgen, 2. November",
      "La rentrée a lieu... A. dimanche 1er · B. lundi 2 au matin · C. mardi 3", size=21)
qf.ex("A2", "Multiple Choice", "A", "Letzte Nachtveranstaltung am Samstag, 7. November",
      "La dernière nocturne de Peur sur le Parc, c'est... A. samedi 7 · B. dimanche 8 · C. vendredi 6", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-une.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIE QUOTIDIENNE　LEBEN", "Le Lucerna", "NIVEAU A2　La rentrée　SCHULBEGINN")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("La rentrée : lundi, toute la France reprend", 32)
f.byline("Par la rédaction　Niveau de lecture : A2")
f.para("Lundi 2 novembre, au matin, les élèves français reprennent les cours. Pour les vacances de la Toussaint, il n'y a pas de décalage entre les zones : les zones A, B et C reprennent ensemble, le même lundi matin.")
f.para("Les vacances ont commencé samedi 17 octobre, après les cours. Deux semaines pour se reposer, voir ses grands-parents, lire pour le plaisir. Lundi matin, les gares et les cours d'école se remplissent de nouveau : cartables, copains, professeurs — et les histoires des vacances à raconter.")
f.para("Cette semaine est aussi la deuxième semaine à l'heure d'hiver. Depuis dimanche 25 octobre, la nuit tombe plus tôt : le soir, la nuit tombe tôt. Le matin, en revanche, la lumière arrive plus tôt — parfait pour se lever sans se tromper d'heure.")
f.para("Que lit-on quand il fait nuit tôt ? C'est la question de la rédaction pour cette semaine d'automne. Réponse : des textes courts, qu'on peut finir en une soirée. Une nouvelle, un chapitre, vingt pages — et on dort avec une belle phrase dans la tête.")
f.para("Autre conseil de saison : préparez vos affaires le soir. Le cartable prêt, les vêtements choisis, le livre dans le sac : le matin de la rentrée devient facile. Et pour les lecteurs de français, un rituel simple : dix minutes de lecture chaque soir, avant de dormir.")
f.para("Bonne rentrée à tous ! Que vous soyez élève, étudiant ou lecteur du soir, cette semaine recommence avec vous — et elle se terminera en beauté, dimanche 8 novembre.")
f.gloss("la rentrée Schulbeginn, Wiederbeginn · reprendre wieder beginnen, wieder aufnehmen · un cartable Schultasche · un décalage Verschiebung, Zeitunterschied · en revanche dagegen, andererseits · un rituel Gewohnheit, Ritual.")
f.head("LES VACANCES, EN CHIFFRES", 25)
f.para("Du samedi 17 octobre au lundi 2 novembre : les vacances de la Toussaint, trois zones ensemble, un seul lundi de reprise. Les familles sont parties chez les grands-parents, à la campagne ou au bord de la mer — et les valises sont revenues pleines de livres.", 23.5)
f.para("Pendant les vacances, les Français ont fêté Halloween, samedi 31 octobre, puis la Toussaint, dimanche 1er novembre. Deux fêtes, deux ambiances : les bonbons d'abord, les fleurs ensuite. Bilan en page 3.", 23.5)
f.bridge("HINWEIS · une valise Koffer · une ambiance Stimmung · le bilan Bilanz, Rückblick.")
f.end_report()

ix = COLX[3]
image(p, "hiroshige-maple.jpg", ix, 200, CW, 480)
cy3 = caption(p, ix, 680, CW, "L'automne à Mama, près d'Edo : les feuilles rouges annoncent les soirées de lecture.",
              "Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA")
sav = ["Les vacances de la Toussaint : du samedi 17 octobre au lundi 2 novembre.",
       "Reprise le lundi 2 novembre au matin, zones A, B et C ensemble.",
       "Deuxième semaine à l'heure d'hiver : la nuit tombe tôt, lisez le soir !"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 14
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LE SAVIEZ-VOUS ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "Et vous ? Racontez votre rentrée en deux phrases en français : où étiez-vous lundi matin, et quel livre avez-vous lu pendant les vacances ? Les meilleurs textes paraîtront dans le VOL.4 (page 7, « Le courrier des lecteurs »)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Montagmorgen: Wo waren Sie, welches Buch? Zwei Sätze an die Redaktion!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "ET VOUS ?　UND SIE?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Montagmorgen: Wo waren Sie, welches Buch? Zwei Sätze an die Redaktion!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Dire la date wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "DIRE LA DATE　SO SAGT MAN DAS DATUM", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "lundi 2 novembre　Achtung: Am 1. sagt man le premier, sonst Grundzahlen", 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 66
for line in [
    ("lundi 2 novembre", "Montag, 2. November · la rentrée"),
    ("mardi 3 novembre", "Dienstag, 3. November · votes à l'Assemblée"),
    ("mercredi 4 novembre", "Mittwoch, 4. November · sorties cinéma"),
    ("samedi 7 novembre", "Samstag, 7. November · nocturne et demis"),
    ("dimanche 8 novembre", "Sonntag, 8. November · les finales"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 330, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "Exemples : Le 1er novembre, c'est la Toussaint. · Le lundi 2 novembre, on reprend les cours. · Le dimanche 8 novembre, on joue les finales.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 320
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCICES　ÜBUNGEN SEITE 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Antworten auf Seite 8　Niveaugemischt; suchen Sie nach der Nummer", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　QUELLE DATE ?", 25)
e.bridge("Ergänzen Sie das Datum auf Französisch (Wochentag und Zahl beachten).")
e.ex("A2", "Satzergänzung", "lundi", "Schulbeginn am Montag",
     "La rentrée a lieu ___ 2 novembre.", instr="Ausfüllen", size=23)
e.ex("A2", "Satzergänzung", "1er", "Am 1. November sagt man le premier",
     "La Toussaint, c'est le ___ novembre.", instr="Ausfüllen", size=23)
e.ex("A2", "Satzergänzung", "samedi", "Letzte Nachtveranstaltung am Samstag",
     "La dernière nocturne a lieu ___ 7 novembre.", instr="Ausfüllen", size=23)
e.ex("A2", "Satzergänzung", "dimanche", "Finale am Sonntag",
     "Les finales ont lieu ___ 8 novembre.", instr="Ausfüllen", size=23)
e.head("B　LE FUTUR PROCHE", 25)
e.bridge("Schreiben Sie mit aller + Infinitiv um (futur proche).")
e.ex("A2", "Umformung", "Les élèves vont reprendre les cours lundi.", "ils/elles → vont",
     "Les élèves (reprendre) les cours lundi. → ___", instr="Umformen", size=21.5)
e.ex("A2", "Umformung", "Nous allons lire vingt pages ce soir.", "nous → allons",
     "Ce soir, nous (lire) vingt pages. → ___", instr="Umformen", size=21.5)
e.ex("A2", "Umformung", "Tu vas préparer ton cartable ce soir.", "tu → vas",
     "Ce soir, tu (préparer) ton cartable. → ___", instr="Umformen", size=21.5)
e.ex("B1", "Umformung", "Vous allez raconter vos vacances lundi.", "vous → allez",
     "Lundi, vous (raconter) vos vacances. → ___", instr="Umformen", size=21.5)
e.head("C　COMPRÉHENSION", 25)
e.bridge("Lesen Sie den Artikel auf Seite 2 und wählen Sie die richtige Antwort.")
e.ex("A2", "Multiple Choice", "C", "Alle drei Zonen beginnen am Montagmorgen",
     "Les zones reprennent... A. séparément · B. en décembre · C. ensemble lundi", size=22)
e.ex("A2", "Multiple Choice", "B", "Winterzeit seit dem 25. Oktober",
     "L'heure d'hiver, c'est depuis... A. le 2 nov. · B. le 25 oct. · C. le 31 oct.", size=22)
e.ex("A2", "Multiple Choice", "A", "Im November wird es abends früh dunkel",
     "Le soir, en novembre... A. la nuit tombe tôt · B. il fait jour · C. il neige", size=22)
e.head("D　LES MOTS", 25)
e.match_set("A2", "Zuordnung",
            ["la rentrée", "reprendre", "un cartable", "un rituel"],
            ["le retour à l'école après les vacances", "recommencer une activité",
             "le sac des élèves", "une habitude qu'on répète"],
            ["a", "b", "c", "d"],
            ["rentrée=Schulbeginn a", "reprendre=wieder beginnen b", "cartable=Schultasche c", "rituel=Gewohnheit d"],
            instr="Zuordnen")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vie.svg")
print("P2 saved, exercises so far:", len(REG))
