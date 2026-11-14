# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 青年 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JEUNESSE & ÉCRANS　JÓVENES Y PANTALLAS", "Le Lucerna", "NIVEAU B1　GTA VI　Réseaux sociaux")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P5-main")
f.title("GTA VI : le jeu que tout le monde attend", 32)
f.byline("Par la rédaction　Niveau de lecture : B1")
f.para("C'est peut-être le jeu vidéo le plus attendu de la planète. Grand Theft Auto VI — GTA VI — est encore une fois, cette semaine, dans les recherches Google en France. Les fans attendent, regardent les bandes-annonces et comptent les jours.")
f.para("La série GTA est célèbre pour ses villes immenses : on se promène librement dans un monde ouvert, en voiture ou à pied. Pour beaucoup de joueurs, c'est comme un film interactif géant — avec de l'humour, de la musique et des histoires de personnages attachants.")
f.para("En France, le jeu vidéo est un loisir de masse : des millions de personnes jouent, sur console, sur ordinateur ou sur téléphone. Les jeunes, bien sûr, mais aussi leurs parents. Et les mots du jeu vidéo sont partout : « streamer », « gamer », « spoiler »... mélangés au français de tous les jours.")
f.para("Pourquoi tant d'attente ? Parce que les grands jeux sont rares, et parce que chaque bande-annonce devient un événement mondial, regardé des centaines de millions de fois. En attendant la sortie, les fans imaginent, dessinent et discutent. L'attente, elle aussi, fait partie du jeu.")
f.gloss("un jeu vidéo un videojuego · une bande-annonce un tráiler · un monde ouvert un mundo abierto · une console una consola · la sortie el lanzamiento · un loisir un pasatiempo.")
f.head("À VOUS !　A PRACTICAR", 25)
f.expl("Lee el artículo de la página 5 y elige la respuesta correcta.")
f.ex("B1", "单选", "B", "GTA es famoso por sus enormes ciudades de mundo abierto",
     "La série GTA est célèbre pour... A. ses petites villes · B. ses mondes ouverts · C. ses jeux de cartes")
f.ex("B1", "单选", "B", "en el texto: des millions de personnes jouent",
     "En France, le jeu vidéo concerne... A. seulement les enfants · B. des millions de personnes · C. personne")
f.ex("B1", "单选", "B", "cada tráiler se convierte en un acontecimiento mundial",
     "Chaque bande-annonce devient... A. un secret · B. un événement mondial · C. un examen")
f.ex("B1", "单选", "A", "para los aficionados, la espera forma parte del juego",
     "Pour les fans, l'attente... A. fait partie du jeu · B. est interdite · C. est terminée")
f.head("LE FRANÇAIS FAIT SON SHOW", 24)
f.para("Cette semaine, sur les réseaux sociaux, le français devient une star. Des vidéos comiques transforment la langue en personnage : « le français » arrive comme une vedette difficile — il a des règles partout, des exceptions, et il refuse de se prononcer comme il s'écrit ! Les apprenants se reconnaissent et rient : oui, c'est exactement ça.", 23.5)
f.para("Autre tendance : la lecture « chic ». Des photos esthétiques montrent des lecteurs avec des livres français — un café, une bougie, un roman ouvert. Le message : lire en français, c'est beau, c'est chic. Sous les photos, les commentaires demandent : « Quel livre pour commencer ? »", 23.5)
f.para("Réponse des professeurs et des libraires : des listes de livres par niveau. A2 pour débuter doucement, B1 pour les lecteurs courageux, B2 pour les passionnés. Lire un vrai livre, même lentement, même avec un dictionnaire : c'est la méthode que ce journal défend chaque semaine.", 23.5)
f.expl("Completa con virale / partager / abonnés / commentaire.")
f.ex("B1", "完成句子", "virale", "vidéo virale = un vídeo viral",
     "Une vidéo ___ est vue par des millions de personnes.")
f.ex("B1", "完成句子", "partager", "partager = compartir",
     "Clique sur le bouton pour ___ la photo avec tes amis.")
f.ex("B1", "完成句子", "abonnés", "des abonnés = seguidores, suscriptores",
     "Elle a 10 000 ___ sur son compte.")
f.ex("B1", "完成句子", "commentaire", "un commentaire = un comentario",
     "Écris un ___ sous la vidéo !")
f.expl("Completa las frases y da tu opinión (respuestas modelo en la página 8).")
f.ex("B1", "完成句子", "ex. : amusant, parce que les enfants adorent se déguiser (respuesta modelo)", "pregunta abierta: vale cualquier respuesta bien razonada",
     "À mon avis, Halloween en France, c'est ___ parce que ___.")
f.ex("B1", "完成句子", "ex. : j'aime les histoires et les mots nouveaux (respuesta modelo)", "pregunta abierta: vale cualquier respuesta bien razonada",
     "Je lis en français parce que ___.")
f.ex("B2", "完成句子", "ex. : ce ne sont pas les résultats (respuesta modelo)", "pregunta abierta: vale cualquier respuesta bien razonada",
     "Les sondages sont utiles, mais ___.")
f.expl("A practicar · Las redes sociales.")
f.ex("B1", "完成句子", "personnage", "la lengua se convierte en un personaje",
     "Dans les vidéos comiques, le français devient un ___.")
f.ex("A2", "完成句子", "chic", "lire en français, c'est chic",
     "Lire en français, c'est ___ : c'est la tendance du moment.")
f.ex("A2", "完成句子", "niveau", "des listes par niveau = listas por nivel",
     "Les professeurs proposent des listes de livres par ___.")
f.ex("B1", "完成句子", "dictionnaire", "même avec un dictionnaire",
     "On peut lire un vrai livre, même avec un ___.")
f.ex("B2", "完成句子", "reconnaissent", "se reconnaître = verse reflejado en ellos",
     "Les apprenants se ___ dans ces vidéos : c'est exactement eux !")
f.ex("B1", "完成句子", "esthétique", "une photo esthétique = una foto con estilo",
     "Une photo ___ montre un café, une bougie, un roman ouvert.")
f.head("LIRE OU JOUER ? LES DEUX !", 24)
f.para("Faut-il choisir entre les écrans et les livres ? Pas forcément. Beaucoup de joueurs deviennent lecteurs : les jeux racontent des histoires, donnent envie de lire les romans, les bandes dessinées et les guides qui les entourent. Et beaucoup de lecteurs jouent : un livre le matin, une partie le soir.", 23.5)
f.para("La bonne question n'est donc pas « écran ou livre ? », mais « quoi, sur l'écran ? ». Un texte long, une vraie histoire, un article comme celui-ci : l'écran peut aussi être une page. C'est le pari de ce journal, que vous lisez peut-être... sur un écran.", 23.5)
f.box("PETIT LEXIQUE DU JEU", [
    ("un niveau — un nivel · sauvegarder — guardar la partida · un défi — un reto", "serif", False, INK, 21.5, 1.42),
    ("perdre / gagner une partie — perder / ganar una partida", "serif", False, INK, 21.5, 1.42),
])
f.end_report()

# col 3 boxes
ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX)
p.text(ix + 22, 240, "LES MOTS DES ÉCRANS　LÉXICO", 22, "sans", True, OLIVE)
mots5 = [
    "un écran — una pantalla", "un réseau social — una red social", "viral — viral",
    "un abonné — un seguidor", "partager — compartir", "un commentaire — un comentario",
    "en ligne — en línea", "un joueur — un jugador", "attendre — esperar",
    "une sortie — un lanzamiento",
]
yy5 = 282
for m in mots5:
    p.text(ix + 22, yy5, m, 21.5, "serif", False, INK)
    yy5 += 37
qy5 = 696
p.rect(ix, qy5, CW, 400, fill="#f0eee5")
p.text(ix + 22, qy5 + 40, "LA PHRASE QUI FAIT RÉAGIR", 23, "sans", True, OLIVE)
p.para(ix + 22, qy5 + 92, "« Lire en français, c'est chic. »", 27, "serif", True, OLIVE, CW - 44, 1.3)
p.para(ix + 22, qy5 + 168, "Sous cette phrase, des centaines de lecteurs racontent leur premier livre en français : un roman d'amour, un polar, un classique commencé trois fois. Et vous, quel est le vôtre ?", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, qy5 + 322, "¿Cuál fue tu primer libro en francés? Cuéntanoslo en los comentarios.", 20, "sans", False, GREY, CW - 44, 1.4)
dy5 = qy5 + 400 + 26
p.rect(ix, dy5, CW, 440, fill=BOX)
p.text(ix + 22, dy5 + 40, "LE DÉBAT　EL DEBATE", 23, "sans", True, OLIVE)
p.para(ix + 22, dy5 + 78, "Combien d'heures par jour devant un écran ? Pour jouer, regarder, lire... Les écrans sont-ils des ennemis des livres, ou une autre porte pour entrer dans la langue ?", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 240, "Petit test de la rédaction : ce soir, remplacez trente minutes d'écran par trente minutes de lecture — et racontez-nous la différence (page 8).", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 372, "Prueba esta noche: media hora menos de pantalla y media hora más de lectura.", 20, "sans", False, GREY, CW - 44, 1.4)
sy5 = dy5 + 440 + 26
p.text(ix, sy5 + 24, "LE SONDAGE DE LA RÉDACTION", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, sy5 + 38, OLIVE, 2)
p.para(ix, sy5 + 76, "Quel jeu attendez-vous le plus ? Quel livre français lisez-vous en ce moment ? Répondez dans les commentaires : résultats dans le prochain numéro.", 21.5, "serif", False, INK, CW, 1.42)
p.para(ix, sy5 + 210, "La encuesta de la redacción: ¿qué juego esperas? ¿Qué libro en francés estás leyendo?", 20, "sans", False, GREY, CW, 1.4)
ty5 = sy5 + 268
p.rect(ix, ty5, CW, 2560 - ty5, fill=BOX)
p.text(ix + 22, ty5 + 40, "TROIS TENDANCES À RETENIR", 23, "sans", True, OLIVE)
tend5 = [
    ("1 · LE JEU ÉVÉNEMENT", "GTA VI fait attendre la planète entière : l'attente devient un spectacle."),
    ("2 · LE FRANÇAIS PERSONNAGE", "Les vidéos comiques transforment la langue en vedette difficile mais attachante."),
    ("3 · LIRE, C'EST CHIC", "Les photos de lecteurs et les listes de livres par niveau font lire la génération des écrans."),
]
yy5 = ty5 + 82
for h, t in tend5:
    p.text(ix + 22, yy5, h, 20.5, "sans", True, OLIVE)
    yy5 = p.para(ix + 22, yy5 + 28, t, 21, "serif", False, INK, CW - 44, 1.4) + 16
p.foot(5)
p.save(f"{OUT}/p5-jeunesse.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 时事 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("POLITIQUE & CHIFFRES　ACTUALIDAD", "Le Lucerna", "NIVEAU B2　Présidentielle 2027　LA ELECCIÓN A FONDO")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1420, tag="P6-deep")
f.title("Présidentielle 2027 : comprendre l'élection et ses chiffres", 32)
f.byline("Par la rédaction　Niveau de lecture : B2")
f.para("En avril 2027, les Français éliront leur président — ou leur présidente. Le président est élu pour cinq ans, au suffrage universel direct : chaque citoyen de 18 ans et plus peut voter. L'élection se déroule en deux tours. Au premier tour, tous les candidats sont en compétition. Si personne n'obtient plus de 50 % des voix, un second tour oppose, deux semaines plus tard, les deux candidats arrivés en tête.")
f.para("À six mois du scrutin, la bataille des chiffres a commencé. Les instituts publient régulièrement des « intentions de vote » : si l'élection avait lieu dimanche, pour qui voteriez-vous ? Ces enquêtes ne prédisent pas le résultat — elles photographient l'opinion à un moment donné. Un écart de deux points peut tenir à la marge d'erreur.")
f.para("Lire un sondage, c'est déjà faire de la politique : qui devance qui ? Qui gagne des points, qui en perd ? Le vocabulaire des comparaisons envahit les titres des journaux : « X creuse l'écart », « Y passe devant », « Z stagne ». Pour les apprenants de français, c'est un terrain d'entraînement idéal : les chiffres, les pourcentages et le comparatif y sont partout.")
f.para("La campagne, elle, ne fait que commencer : les partis choisissent leurs candidats, les programmes se préparent. Une chose est sûre : jusqu'en 2027, les sondages rythmeront la vie politique française — cette semaine, ils sont la recherche numéro un du pays sur Google.")
f.gloss("un scrutin una votación, una elección · une marge d'erreur un margen de error · creuser l'écart abrir brecha · devancer adelantar, superar · rythmer marcar el ritmo.")
f.end_report()

# practice poll chart, span cols 0-1
chx, chw = MX, 896
chy = 1470
p.rect(chx, chy, chw, 470, fill=BOX)
p.text(chx + 24, chy + 42, "SONDAGE D'ENTRAÎNEMENT　ENCUESTA DE PRÁCTICA", 25, "sans", True, OLIVE)
p.text(chx + 24, chy + 74, "Données simplifiées pour l'exercice — aucun institut, aucun vrai candidat.", 19.5, "sans", False, OLIVE)
p.text(chx + 24, chy + 100, "Datos de práctica: ningún instituto ni candidato reales.", 19, "sans", False, GREY)
bars = [("Candidat A", 28, OLIVE), ("Candidate B", 24, OLIVE), ("Candidat C", 17, OLIVE),
        ("Candidat D", 11, OLIVE), ("Autres", 9, OLIVE), ("Indécis", 11, "#8a8168")]
byy = chy + 128
for lab, val, col in bars:
    p.text(chx + 24, byy + 26, lab, 22, "serif", True, INK)
    p.rect(chx + 200, byy + 6, val * 18, 26, fill=col)
    p.text(chx + 212 + val * 18, byy + 27, f"{val} %", 22, "sans", True, OLIVE)
    byy += 52

e6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 1990, 2560, tag="P6-chart-ex")
e6.head("LIRE LE GRAPHIQUE　EL GRÁFICO", 22)
e6.expl("Responde mirando la encuesta de práctica de arriba.")
e6.ex("B2", "图表读数", "Le candidat A, avec 28 %", "A va primero con el 28 %",
      "Qui est en tête du sondage ?", size=23)
e6.ex("B2", "图表读数", "4 points", "28 − 24 = 4 puntos",
      "Combien de points séparent le candidat A de la candidate B ?", size=23)
e6.ex("B2", "图表读数", "Faux", "el 17 % no es el doble del 11 %",
      "Vrai ou faux : le candidat C a deux fois plus de voix que le candidat D.", size=23)
e6.ex("B2", "图表读数", "11 %", "Indécis (indecisos) = 11 %",
      "Quel est le pourcentage des indécis ?", size=23)
e6.ex("B2", "图表读数", "La candidate B (27 % contre 26 %)", "B + 3 = 27, A − 2 = 26: B adelanta",
      "Si B gagne 3 points et A en perd 2, qui passe devant ?", size=23)
e6.ex("B2", "图表读数", "Oui, 52 %", "28 + 24 = 52 %: más de la mitad",
      "Les candidats A et B, ensemble, dépassent-ils 50 % ?", size=23)
e6.end_report()

# right half, col 2: vocab box + comparatif + vocab MCQ + headline phrases
g = Flow(p, [(COLX[2], CW)], 200, 2560, tag="P6-right2")
g.box("LES MOTS DU SCRUTIN　LÉXICO", [
    ("un sondage — una encuesta · une intention de vote — intención de voto", "serif", False, INK, 21.5, 1.42),
    ("devancer — adelantar · creuser l'écart — abrir brecha", "serif", False, INK, 21.5, 1.42),
    ("stagner — estancarse · un échantillon — una muestra", "serif", False, INK, 21.5, 1.42),
    ("un parti — un partido · se qualifier — pasar a la siguiente vuelta", "serif", False, INK, 21.5, 1.42),
], tsize=22)
g.head("LE COMPARATIF EN CAMPAGNE", 24)
g.expl("Completa con el comparativo.")
g.ex("B2", "完成句子", "plus populaire", "A 28 % > B 24 %",
     "Dans ce sondage, A est ___ (populaire) que B.", size=23)
g.ex("B2", "完成句子", "moins", "D 11 % < C 17 %: se usa moins de",
     "D obtient ___ de voix que C.", size=23)
g.ex("B2", "完成句子", "aussi", "11 % = 11 %: igualdad con aussi",
     "Les indécis sont ___ nombreux que les partisans de D.", size=23)
g.ex("B2", "完成句子", "meilleur", "el comparativo de bon es meilleur",
     "Ce sondage est ___ (bon) que le précédent : l'échantillon est plus grand.", size=23)
g.head("LES MOTS　VOCABULARIO", 25)
g.expl("Elige el significado correcto.")
g.ex("B2", "单选", "B", "devancer = superar, ir por delante",
     "« Devancer » signifie... A. arriver après · B. passer devant · C. abandonner", size=23)
g.ex("B2", "单选", "C", "un scrutin = una votación",
     "Un « scrutin » est... A. un débat · B. un parti politique · C. un vote", size=23)
g.ex("B2", "单选", "A", "el margen de error solo afecta a las cifras",
     "La « marge d'erreur » concerne... A. les chiffres du sondage · B. le prix du journal · C. l'heure du vote", size=23)
g.ex("B2", "单选", "B", "être en tête = ir primero",
     "« Être en tête » veut dire... A. réfléchir · B. être le premier · C. être fatigué", size=23)
g.box("LES PHRASES DES JOURNAUX", [
    ("« X creuse l'écart. » — X abre brecha.", "serif", False, INK, 21.5, 1.42),
    ("« Y passe devant. » — Y se pone por delante.", "serif", False, INK, 21.5, 1.42),
    ("« Z en chute libre. » — Z se desploma.", "serif", False, INK, 21.5, 1.42),
    ("« W crée la surprise. » — W da la sorpresa.", "serif", False, INK, 21.5, 1.42),
])
g.end_report()

# right half, col 3: micro-drills + history box + big number + débat
g2 = Flow(p, [(COLX[3], CW)], 200, 2560, tag="P6-right3")
g2.head("MICRO-DRILLS　A PRACTICAR", 25)
g2.expl("Completa las frases sobre la elección.")
g2.ex("B2", "完成句子", "universel", "suffrage universel = sufragio universal directo",
      "Le président est élu au suffrage ___ direct.", size=23)
g2.ex("B2", "完成句子", "second", "le second tour = la segunda vuelta",
      "Si personne n'a plus de 50 %, il y a un ___ tour.", size=23)
g2.ex("B2", "完成句子", "erreur", "la marge d'erreur = el margen de error",
      "Un petit écart peut tenir à la marge d'___.", size=23)
g2.ex("B1", "完成句子", "dix-huit", "se vota desde los 18 años",
      "En France, on vote à partir de ___ ans.", size=23)
g2.box("TROIS DATES POUR COMPRENDRE", [
    ("1962 — le président est élu directement par les citoyens.", "serif", False, INK, 21.5, 1.42),
    ("1974 — on peut voter dès 18 ans.", "serif", False, INK, 21.5, 1.42),
    ("2000 — le mandat passe de sept ans à cinq ans : c'est le quinquennat.", "serif", False, INK, 21.5, 1.42),
    ("Tres reformas que dieron forma a la elección francesa de hoy.", "sans", False, GREY, 20, 1.4),
], tsize=21)
g2.head("LE CHIFFRE DE LA SEMAINE", 25)
g2.para("5 000 +", 54, "serif", True, OLIVE, 1.1, 4)
g2.para("C'est le nombre de recherches quotidiennes, en France, pour « sondage présidentielle 2027 » — la recherche numéro un du pays cette semaine (Google Trends).", 22)
g2.head("LE DÉBAT　EL DEBATE", 25)
g2.para("Les sondages influencent-ils le vote ? Certains disent oui : on aime voter pour le gagnant. D'autres disent non : les électeurs choisissent leurs idées, pas les chiffres. Et vous, qu'en pensez-vous ? Deux phrases, en français, dans les commentaires.", 22)
g2.expl("¿Influyen las encuestas en el voto? Escribe dos frases con tu opinión.")
g2.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
