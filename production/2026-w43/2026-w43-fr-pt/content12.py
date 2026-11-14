# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · 头版 (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 1　Nº 1", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "HEBDOMADAIRE EN FRANÇAIS　TODA SEMANA　O FRANCÊS QUE OS FRANCESES LEEM", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMAINE DU 19 AU 25 OCTOBRE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "Le Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "SEMANÁRIO EM FRANCÊS　VOL.1　OUTONO E FESTAS", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "LE JOURNAL DES APPRENANTS DE FRANÇAIS — LIRE LA VRAIE VIE, EN FRANÇAIS", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# countdown band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "DIMANCHE, ON RECULE D'UNE HEURE !", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Changement d'heure : dans la nuit de samedi à dimanche, à 3 h, il sera 2 h. On gagne une heure de sommeil !", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "NESTE DOMINGO　HORÁRIO DE INVERNO", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "Relógios atrasam uma hora　ver página 2", 18, "sans", False, GOOSE, anchor="end")

# pairing badge (this edition: French text, Italian explanations)
p.text(975, 612, "TEXTOS EM FRANCÊS　EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 16, "sans", False, GREY, anchor="middle")

# ---- headline (span cols 0-2) ----
hy = 610
p.text(MX, hy + 26, "POLITIQUE　LA UNE　POLÍTICA INTERNA", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Présidentielle 2027 : les Français regardent déjà les sondages", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "Par la rédaction du Lucerna　Niveau de lecture : A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1812, tag="P1-headline")
f.para("L'élection présidentielle est en 2027, mais les Français en parlent déjà. Cette semaine, sur Google, la recherche numéro un en France est : « sondage présidentielle 2027 ». Des milliers de personnes cherchent ces mots chaque jour.")
f.para("Un sondage, c'est une grande question posée à beaucoup de personnes : « Pour qui voulez-vous voter ? » Les réponses donnent des chiffres : un candidat a 28 %, un autre a 24 %... Les journaux publient ces chiffres, et tout le monde les commente.")
f.para("Pourquoi si tôt ? Parce que la campagne commence doucement. Les candidats préparent leurs idées et leurs affiches. Pour les Français, c'est aussi un jeu : qui monte, qui descend ? Dans les cafés, on compare les chiffres comme un classement de football.")
f.para("Attention : un sondage n'est pas un résultat. C'est une photo du moment. En avril 2027, les Français voteront pour de vrai, en deux tours.")
f.para("En attendant, les chiffres font parler le pays — et ils sont parfaits pour apprendre le français des nombres et des opinions. Dossier complet en page 6.")
f.gloss("sondage pesquisa · en tête na liderança · un tour um turno · voter votar · un candidat um candidato.")
f.box("EN CHIFFRES　OS NÚMEROS", [
    ("18 ans — l'âge pour voter (vota-se aos 18) · 5 ans — la durée du mandat (dura 5 anos)", "serif", False, INK, 21.5, 1.4),
    ("2 tours — deux votes pour élire (dois turnos) · 50 % + 1 — pour gagner dès le premier tour (vencer já no 1.º turno)", "serif", False, INK, 21.5, 1.4),
])
f.head("À VOUS !　SUA VEZ", 25)
f.ex("A2", "完成句子", "sondage", "palavra-chave da manchete",
     "Un ___ pose des questions à beaucoup de personnes.", size=21.5)
f.ex("A2", "完成句子", "tête", "être en tête = estar na liderança",
     "Le candidat qui a le plus de voix est en ___.", size=21.5)
f.ex("A2", "完成句子", "pour cent", "28 % = vingt-huit pour cent",
     "28 % se lit : « vingt-huit ___ ».", size=21.5)
f.ex("A2", "完成句子", "cinq", "o mandato presidencial dura cinco anos",
     "Le président reste ___ ans au pouvoir.", size=21.5)
f.ex("B1", "完成句子", "monte", "monter / descendre: quem sobe e quem desce nas pesquisas",
     "Dans les sondages, qui ___ ? Qui descend ?", size=21.5)
f.ex("B1", "完成句子", "photo", "sondage = photo du moment",
     "Un sondage est une ___ du moment, pas un résultat.", size=21.5)
f.end_report()

# ---- GT chart (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 668, fill=BOX)
p.text(gx + 22, gy + 40, "LES RECHERCHES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "DE LA SEMAINE", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "As buscas da semana　Google Trends", 19, "sans", False, GREY)
gt = [
    ("sondage présidentielle 2027", "5 000 +", 250),
    ("knicks – 76ers (NBA)", "2 000 +", 196),
    ("spurs – thunder (NBA)", "1 000 +", 152),
    ("grand theft auto vi", "500 +", 104),
    ("tony parker", "200 +", 62),
]
byy = gy + 150
for i, (lab, val, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    p.text(gx + 30 + bw, byy + 53, val, 20, "sans", True, OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Source : Google Trends, France,", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "recherches du jour, cette semaine.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 76, "A mais buscada: a presidencial de 2027.", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1280
p.rect(gx, sy, gw, 372, fill="#f0eee5")
p.text(gx + 22, sy + 40, "DANS CE NUMÉRO　SUMÁRIO", 24, "sans", True, OLIVE)
som = [
    ("p.2", "L'heure d'hiver arrive", "A2"),
    ("p.3", "La Toussaint des fleurs", "A2→B1"),
    ("p.4", "Wemby, le géant de la NBA", "B1"),
    ("p.5", "GTA VI et les réseaux", "B1"),
    ("p.6", "L'élection en chiffres", "B2"),
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
p.text(gx, my + 76, "« reculer »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "aller en arrière. Dimanche, les horloges reculent d'une heure.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "Andar para trás; atrasar o relógio.", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
image(p, "hiroshige-maple.jpg", ix, iy, iw, 320)
caption(p, ix, iy + 320, iw,
        "L'automne à Mama, près d'Edo : les érables deviennent rouges, les lecteurs ouvrent leurs livres.",
        "Utagawa Hiroshige (1797-1858), estampe, domaine public · LACMA")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-automne")
f2.head("L'AUTOMNE, SAISON DES LIVRES", 23)
f2.para("En France, l'automne est la saison des livres : c'est la « rentrée littéraire », des centaines de romans nouveaux arrivent en librairie.", 22.5)
f2.para("Ce numéro suit le rythme de la saison : les vacances, la Toussaint, le basket de la nuit, les chiffres de la politique. Bonne lecture !", 22.5)

f2.end_report()
# col 3 EN BREF
bx = COLX[3]
p.rect(bx, 1874, CW, 434, fill=BOX)
p.text(bx + 22, 1914, "EN BREF　EM RESUMO", 24, "sans", True, OLIVE)
brefs = [
    ("VACANCES", "Les vacances de la Toussaint ont commencé samedi 17. Les cours reprennent le lundi 2 novembre."),
    ("NBA", "La saison de basket commence : la France regarde les Spurs de Wembanyama. (page 4)"),
    ("HALLOWEEN", "Le 31 octobre, les enfants se déguisent. La fête divise. (page 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- quiz éclair (4 columns, one item each) ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ ÉCLAIR　QUIZ RELÂMPAGO", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "Leia a primeira página e escolha a resposta certa　Respostas na página 8", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "单选", "B", "a manchete: a busca número um na França nesta semana",
      "Quelle est la recherche numéro un en France cette semaine ? A. le football · B. « sondage présidentielle 2027 » · C. la météo", size=21)
qf.ex("A2", "单选", "B", "neste domingo, às 3 h serão 2 h",
      "Dimanche, à trois heures du matin, il sera... A. quatre heures · B. deux heures · C. trois heures", size=21)
qf.ex("A2", "单选", "C", "férias de 17 de outubro a 2 de novembro",
      "Les vacances de la Toussaint finissent... A. le 25 octobre · B. le 1er novembre · C. le 2 novembre", size=21)
qf.ex("A2", "单选", "B", "Wembanyama joga no Spurs de San Antonio",
      "Victor Wembanyama joue... A. à Paris · B. à San Antonio · C. à New York", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-une.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · 生活 (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIE QUOTIDIENNE　VIDA COTIDIANA", "Le Lucerna", "NIVEAU A2　Changement d'heure　A MUDANÇA DE HORA")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("Changement d'heure : dimanche, la France recule d'une heure", 32)
f.byline("Par la rédaction　Niveau de lecture : A2")
f.para("Dans la nuit de samedi à dimanche, la France passe à l'heure d'hiver. À trois heures du matin, les horloges reculent : il est deux heures. Résultat : on dort une heure de plus !")
f.para("Pourquoi ce changement ? L'histoire commence en 1976. Après le choc pétrolier de 1973, l'énergie est très chère. L'idée est simple : utiliser la lumière du jour pour économiser l'électricité. Depuis, deux fois par an, les Français changent d'heure : au printemps, le dernier dimanche de mars, on avance d'une heure ; en automne, le dernier dimanche d'octobre, on recule.")
f.para("Pour ne pas se tromper, les Français répètent une petite phrase : « En octobre, on recule. » Le même jour, toute l'Union européenne change d'heure. Les téléphones et les ordinateurs changent tout seuls. Mais attention aux montres, aux fours et aux vieux réveils : eux, il faut les régler à la main !")
f.para("Bien dormir, c'est important. Le corps aime les habitudes. Le matin du changement, la lumière arrive plus tôt ; le soir, la nuit tombe plus vite. Les médecins conseillent : profitez de la lumière du matin, et gardez des heures de repas régulières.")
f.para("Et les animaux ? Les vaches, les chiens et les chats ne regardent pas l'heure... mais ils aiment leurs habitudes, eux aussi. Alors les fermiers changent les heures de repas petit à petit, jour après jour.")
f.para("Une heure de plus : qu'en faire ? Dormir, bien sûr. Mais aussi : préparer un bon petit déjeuner, téléphoner à ses grands-parents, ou lire un roman. Une heure gagnée, c'est vingt pages de lecture !")
f.para("Le dimanche matin, tout est calme : les boulangeries ouvrent, les marchés s'installent. Un café, un croissant, un bon livre : c'est le programme préféré des lecteurs.")
f.gloss("reculer recuar, atrasar (o relógio) · avancer adiantar (o relógio) · régler ajustar · le choc pétrolier o choque do petróleo · économiser economizar · un réveil um despertador · la lumière du jour a luz do dia.")
f.head("LES VACANCES DE LA TOUSSAINT", 23)
f.para("Depuis samedi 17 octobre, les élèves français sont en vacances. Les cours reprennent le lundi 2 novembre, au matin. C'est la première pause de l'année scolaire : deux semaines pour se reposer.", 23.5)
f.para("Dans les gares, les trains sont pleins : les familles partent chez les grands-parents, à la campagne ou au bord de la mer. Les valises sont pleines de livres : pendant les vacances, on lit pour le plaisir. La fête de la Toussaint arrive au milieu des vacances — rendez-vous en page 3.", 23.5)
f.para("Petit conseil de la rédaction : réservez vos billets de train tôt, et gardez un livre pour le voyage — le train est la plus belle salle de lecture du monde.", 23.5)
f.expl("Nota — une pause uma pausa · une gare uma estação · une valise uma mala · la reprise a volta às aulas.")
f.end_report()

# col 3: image + facts (sequential, measured)
ix = COLX[3]
image(p, "atget-paris.jpg", ix, 200, CW, 480)
cy3 = caption(p, ix, 680, CW, "Paris, un matin d'automne : la ville se réveille doucement.",
              "Eugène Atget (1857-1927), photographie, domaine public")
sav = ["Le changement d'heure existe en France depuis 1976, après le choc pétrolier de 1973.",
       "Dans toute l'Union européenne, on change d'heure le même week-end.",
       "Dimanche matin, vous gagnez une heure de sommeil. Profitez-en pour lire !"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in sav) + 30
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "LE SAVIEZ-VOUS ?", 24, "sans", True, OLIVE)
yy3 += 52
for t in sav:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 10
etvous = "Dans votre pays, change-t-on d'heure ? Le dimanche, à quelle heure vous levez-vous ? Écrivez deux phrases en français et envoyez-les à la rédaction : les meilleures paraîtront dans le prochain numéro (page 7, « Le courrier des lecteurs »)."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("O seu país muda a hora? A que horas você acorda no domingo? Escreva-nos.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "ET VOUS ?　E VOCÊ?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "O seu país muda a hora? A que horas você acorda no domingo? Escreva-nos.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Dire l'heure wide box ----
dy = 1570
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "DIRE L'HEURE　DIZER AS HORAS", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "Il est + heure　Atenção: para dizer as horas, usa-se « Il est », não « C'est »", 20, "sans", False, GREY, anchor="end")

def clock(cx, cy, r, hh, mm, label):
    p.add(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="#fdfaf0" stroke="{INK}" stroke-width="3"/>')
    import math
    for k in range(12):
        a = math.radians(k * 30)
        x1, y1 = cx + (r - 12) * math.sin(a), cy - (r - 12) * math.cos(a)
        x2, y2 = cx + r * math.sin(a), cy - r * math.cos(a)
        p.add(f'<line x1="{x1:.0f}" y1="{y1:.0f}" x2="{x2:.0f}" y2="{y2:.0f}" stroke="{INK}" stroke-width="2.4"/>')
    ah = math.radians((hh % 12) * 30 + mm * 0.5)
    am = math.radians(mm * 6)
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.55)*math.sin(ah):.0f}" y2="{cy - (r*0.55)*math.cos(ah):.0f}" stroke="{INK}" stroke-width="6" stroke-linecap="round"/>')
    p.add(f'<line x1="{cx}" y1="{cy}" x2="{cx + (r*0.82)*math.sin(am):.0f}" y2="{cy - (r*0.82)*math.cos(am):.0f}" stroke="{OLIVE}" stroke-width="4" stroke-linecap="round"/>')
    p.text(cx, cy + r + 34, label, 22, "serif", True, INK, anchor="middle")

clock(240, dy + 140, 74, 3, 0, "Il est trois heures.")
clock(560, dy + 140, 74, 7, 30, "Il est sept heures et demie.")
clock(880, dy + 140, 74, 10, 15, "Il est dix heures et quart.")
lx = 1090
ly = dy + 66
for line in [
    ("et quart", "= + 15 minutes (mais um quarto)"),
    ("et demie", "= + 30 minutes (mais meia hora)"),
    ("moins le quart", "= − 15 minutes (menos um quarto)"),
    ("midi / minuit", "= 12 h 00 le jour / la nuit (meio-dia / meia-noite)"),
]:
    p.text(lx, ly + 24, line[0], 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, line[1], 21, "sans", False, GREY)
    ly += 40
p.para(lx, ly + 24, "Exemples : 8 h 45 = Il est neuf heures moins le quart. · 23 h 30 = Il est onze heures et demie du soir.", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 340
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EXERCICES　EXERCÍCIOS DA PÁGINA 2", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8　Os exercícios podem misturar os níveis: procure pelo número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2560, tag="P2-ex")
e.head("A　QUELLE HEURE EST-IL ?", 25)
e.expl("Complete as frases conforme a hora.")
e.ex("A2", "完成句子", "demie", "14 h 30 = duas e meia da tarde",
     "14 h 30 : Il est deux heures et ___ .", instr="Complete", size=23)
e.ex("A2", "完成句子", "et quart", "8 h 15 = oito e um quarto",
     "8 h 15 : Il est huit heures ___ .", instr="Complete", size=23)
e.ex("A2", "完成句子", "moins le quart", "11 h 45 = meio-dia menos um quarto",
     "11 h 45 : Il est midi ___ .", instr="Complete", size=23)
e.ex("A2", "完成句子", "midi", "12 h 00 = meio-dia",
     "12 h 00 : Il est ___ . On déjeune !", instr="Complete", size=23)
e.ex("A2", "完成句子", "minuit et demi", "0 h 30 = meia-noite e meia (minuit é masculino: demi sem -e)",
     "0 h 30 : Il est ___ . Bonne nuit !", instr="Complete", size=23)
e.head("B　LE FUTUR PROCHE", 25)
e.expl("Reescreva no futur proche (aller + inf.).")
e.ex("A2", "句型转换", "Nous allons changer les horloges.", "nous → allons",
     "Ce soir, nous (changer) les horloges. → ___", instr="Reescreva")
e.ex("A2", "句型转换", "Tu vas dormir une heure de plus.", "tu → vas",
     "Dimanche, tu (dormir) une heure de plus. → ___", instr="Reescreva")
e.ex("A2", "句型转换", "Les élèves vont reprendre les cours le 2 novembre.", "ils/elles → vont",
     "Les élèves (reprendre) les cours le 2 novembre. → ___", instr="Reescreva")
e.ex("B1", "句型转换", "Vous allez partir en vacances ?", "vous → allez",
     "Vous (partir) en vacances cette semaine ? → ___", instr="Reescreva")
e.head("C　COMPRÉHENSION", 25)
e.expl("Leia o artigo da página 2 e escolha.")
e.ex("A2", "单选", "B", "existe desde 1976 (depois do choque do petróleo)",
     "Le changement d'heure existe depuis... A. 1916 · B. 1976 · C. 2020", size=23.5)
e.ex("A2", "单选", "B", "na primavera, adianta-se (avancer)",
     "Au printemps, on... A. recule d'une heure · B. avance d'une heure · C. ne change rien", size=23.5)
e.ex("A2", "单选", "C", "celulares e computadores se atualizam sozinhos",
     "Quels appareils changent d'heure tout seuls ? A. les fours · B. les montres · C. les téléphones", size=23.5)
e.head("D　LES MOTS", 25)
e.match_set("A2", "词汇配对",
            ["reculer", "régler", "économiser", "la lumière du jour"],
            ["mettre une montre à l'heure", "aller en arrière",
             "utiliser moins d'énergie", "elle vient du soleil"],
            ["b", "a", "c", "d"],
            ["reculer = andar para trás b", "régler = acertar o relógio a", "économiser = gastar menos c", "a luz do dia vem do sol d"],
            instr="Associe a palavra ao sentido")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vie.svg")
print("P2 saved, exercises so far:", len(REG))
