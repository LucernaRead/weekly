# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-fr-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE · CULTURA", "Le Lucerna", "NIVEAU A2 → B1 · La Toussaint · TODOS OS SANTOS")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P3-main")
f.title("La Toussaint : le jour des fleurs et des souvenirs", 37)
f.byline("Par la rédaction · Niveau de lecture : A2 → B1")
f.para("Le 1er novembre, la France fête la Toussaint. À l'origine, c'est la fête de tous les saints. Aujourd'hui, pour beaucoup de familles, c'est surtout le jour du souvenir : on pense aux personnes mortes qu'on a aimées.")
f.para("Ce jour-là, les cimetières se remplissent de fleurs. La fleur de la Toussaint, c'est le chrysanthème. Les Français en achètent des millions : blancs, jaunes, violets... On les pose sur les tombes, on nettoie les pierres, et on reste un moment en silence avec la famille.")
f.para("Attention, voyageurs ! En France, le chrysanthème est la fleur des cimetières. On n'offre jamais de chrysanthèmes pour un anniversaire ou pour un dîner. Pour faire plaisir, choisissez des roses ou des tulipes !")
f.para("La Toussaint arrive pendant les vacances scolaires : les familles voyagent pour se retrouver. Le 1er novembre est un jour férié : les écoles, les bureaux et beaucoup de magasins sont fermés. Dans les villages comme dans les grandes villes, c'est un jour calme, doux et un peu mélancolique — le cœur de l'automne français.")
f.gloss("un cimetière um cemitério · une tombe um túmulo · un jour férié um feriado · le souvenir a lembrança · mélancolique melancólico · à l'origine na origem, no início.")
f.head("À VOUS ! · SUA VEZ", 25)
f.expl("Verdadeiro ou falso? (Vrai / Faux)")
f.ex("A2", "阅读判断", "Faux", "Todos os Santos é 1.º de novembro, não 31 de outubro",
     "La Toussaint est le 31 octobre.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Vrai", "no texto: les cimetières se remplissent de fleurs",
     "Le 1er novembre, les cimetières sont pleins de fleurs.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Faux", "na França, o crisântemo é flor de cemitério: nunca se dá de presente",
     "On offre des chrysanthèmes pour un anniversaire.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Faux", "1.º de novembro é jour férié (feriado): as escolas fecham",
     "Le 1er novembre, les écoles sont ouvertes.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Faux", "o texto diz la fête divise: as opiniões se dividem",
     "Tous les Français adorent Halloween.", instr="Vrai ou faux ?")
f.expl("Complete com cimetière / tombe / déguisement / citrouille.")
f.ex("B1", "完成句子", "déguisement", "no Halloween, as pessoas se fantasiam (déguisement)",
     "Pour Halloween, les enfants portent un ___.")
f.ex("A2", "完成句子", "tombe", "as flores vão sobre o túmulo",
     "On pose les fleurs sur la ___.")
f.ex("A2", "完成句子", "cimetière", "em 1.º de novembro, o cemitério fica cheio de flores",
     "Le ___ est plein de fleurs le 1er novembre.")
f.ex("B1", "完成句子", "citrouille", "a abóbora é o símbolo do Halloween",
     "Une ___ orange est le symbole d'Halloween.")
f.expl("Reescreva as frases (com ne...jamais / ne...plus / ne...pas).")
f.ex("B1", "句型转换", "On n'offre jamais de chrysanthèmes pour un anniversaire.", "jamais + de (sem artigo)",
     "(jamais) On offre des chrysanthèmes pour un anniversaire. → ___", instr="Reescreva")
f.ex("B1", "句型转换", "Les feuilles ne sont plus vertes en automne.", "ne...plus = não mais",
     "(plus) Les feuilles sont vertes en automne. → ___", instr="Reescreva")
f.ex("B1", "句型转换", "Le 1er novembre n'est pas un jour de travail pour tous.", "n'est pas = não é",
     "(pas) Le 1er novembre est un jour de travail pour tous. → ___", instr="Reescreva")
f.head("HALLOWEEN : LA FÊTE QUI DIVISE", 25)
f.para("Le 31 octobre, c'est Halloween. Les enfants se déguisent — sorcières, fantômes, super-héros — et ils frappent aux portes : « Des bonbons ou un sort ! » On leur donne des bonbons, et tout le monde rit.", 23.5)
f.para("En France, la fête vient des États-Unis. Certains l'adorent : c'est joyeux, coloré, parfait pour les enfants. D'autres disent : « Ce n'est pas notre tradition, c'est du commerce. » Mais dans les écoles et les villages, les citrouilles orange sont de plus en plus nombreuses. Cette année, Halloween tombe un samedi, pendant les vacances : les familles auront le temps de préparer la fête. Et vous, pour ou contre ?", 23.5)
f.expl("Sua vez · Perguntas sobre o Halloween.")
f.ex("A2", "完成句子", "sort", "« Des bonbons ou un sort ! » = doces ou travessuras",
     "« Des bonbons ou un ___ ! » crient les enfants.")
f.ex("B1", "完成句子", "déguisent", "se déguiser = fantasiar-se (forma ils)",
     "Les enfants se ___ en sorcières et en fantômes.")
f.ex("A2", "完成句子", "bonbons", "as crianças pedem balas (bonbons)",
     "On frappe à la porte et on demande des ___.")
f.ex("A2", "完成句子", "États-Unis", "o Halloween vem dos Estados Unidos (no texto)",
     "En France, la fête d'Halloween vient des ___.")
f.ex("B1", "单选", "B", "diviser = as opiniões se dividem",
     "« La fête divise » signifie... A. tout le monde est d'accord · B. les avis sont partagés · C. personne ne vient")
f.ex("B1", "完成句子", "déguisements", "comprar balas e fantasias",
     "Pour la fête, on achète des bonbons et des ___.")
f.head("LA TOUSSAINT DANS LE MONDE", 25)
f.para("Le 1er novembre n'est pas férié qu'en France : la Belgique fête aussi la Toussaint, et les familles y visitent les cimetières avec des chrysanthèmes. Le mot « Toussaint » signifie « tous les saints » : la fête honore tous les saints, connus et inconnus.", 23.5)
f.para("Le 2 novembre, au Mexique, c'est le Día de los Muertos, le Jour des Morts : les familles préparent des autels avec des photos, des fleurs orange et les plats préférés des disparus. L'ambiance est très différente : musique, couleurs et fête — mais l'idée est la même : ne pas oublier ceux qu'on aime.", 23.5)
f.para("Et le 31 octobre au soir, pendant que les enfants français demandent des bonbons, beaucoup de familles pensent déjà au lendemain : acheter les fleurs, préparer le voyage, téléphoner aux grands-parents. L'automne est la saison du souvenir — et des retrouvailles.", 23.5)
f.expl("Nota — un autel um altar · un disparu um ente querido falecido · les retrouvailles o reencontro.")
f.box("LE MOT DE LA PAGE", [
    ("« chrysanthème » vient du grec : chrysos (l'or) + anthemon (la fleur) — la « fleur d'or ».", "serif", False, INK, 22, 1.42),
    ("O crisântemo: uma flor com ouro no nome.", "sans", False, GREY, 20, 1.4),
])
f.end_report()

# col 3: image + boxes
ix = COLX[3]
image(p, "chrysanthemum-blanco.jpg", ix, 200, CW, 540)
cy3 = caption(p, ix, 740, CW,
              "Le chrysanthème, fleur du souvenir en France : on le pose sur les tombes, on ne l'offre jamais en cadeau.",
              "Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public")
by3 = cy3 + 22
p.rect(ix, by3, CW, 452, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, by3 + 40, "LES MOTS DES FÊTES · PALAVRAS", 23, "sans", True, OLIVE)
mots = [
    "un saint — um santo", "un cimetière — um cemitério", "une tombe — um túmulo",
    "un jour férié — um feriado", "se souvenir — lembrar-se",
    "un déguisement — uma fantasia", "une citrouille — uma abóbora",
    "un bonbon — uma bala", "un fantôme — um fantasma", "un sort — um feitiço",
]
yy3 = by3 + 82
for m in mots:
    p.text(ix + 22, yy3, m, 21.5, "serif", False, INK)
    yy3 += 37
zy3 = by3 + 452 + 26
p.rect(ix, zy3, CW, 476, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, zy3 + 40, "ZOOM · TÚMULOS DE ESCRITORES", 23, "sans", True, OLIVE)
p.para(ix + 22, zy3 + 78, "À Paris, le cimetière du Père-Lachaise est le plus visité du monde. On y trouve les tombes de Balzac, d'Oscar Wilde et de Marcel Proust. Le 1er novembre, des lecteurs y déposent des fleurs... et parfois un livre.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, zy3 + 340, "No Père-Lachaise repousam Balzac, Wilde e Proust: em Todos os Santos, os leitores podem levar uma flor aos escritores.", 20, "sans", False, GREY, CW - 44, 1.4)
dy3 = zy3 + 476 + 26
p.rect(ix, dy3, CW, 330, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, dy3 + 40, "DATES À RETENIR · O MÊS", 23, "sans", True, OLIVE)
dates3 = [
    ("dim. 25 oct.", "changement d'heure !"),
    ("sam. 31 oct.", "Halloween"),
    ("dim. 1er nov.", "la Toussaint (jour férié)"),
    ("lun. 2 nov.", "reprise des cours"),
]
yy3 = dy3 + 84
for d, t in dates3:
    p.text(ix + 22, yy3, d, 19.5, "sans", True, BRICK)
    p.text(ix + 168, yy3, t, 18.5, "serif", False, INK)
    yy3 += 42
p.para(ix + 22, yy3 + 20, "Três dias seguidos: Halloween, Todos os Santos e depois a volta às aulas.", 19.5, "sans", False, GREY, CW - 44, 1.4)
py3 = dy3 + 330 + 30
p.text(ix, py3 + 24, "POUR OU CONTRE ?", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, py3 + 38, GOLD, 2)
p.para(ix, py3 + 74, "Halloween en France : fête joyeuse ou commerce ? Écrivez votre avis en deux phrases (page 8).", 20.5, "serif", False, INK, CW, 1.4)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · ESPORTE", "Le Lucerna", "NIVEAU B1 · NBA · Wembanyama")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P4-main")
f.title("Wemby : le géant français qui fait rêver la NBA", 37)
f.byline("Par la rédaction · Niveau de lecture : B1")
f.para("Il mesure 2,24 mètres. Il a de très longs bras. Et cette semaine, son équipe est dans les recherches Google de toute la France : les Spurs de San Antonio contre Oklahoma City. Le nom du phénomène : Victor Wembanyama, dit « Wemby ».")
f.para("Né au Chesnay, près de Paris, Victor commence le sport enfant : d'abord le football — il est gardien de but ! — et le judo. Puis le basket arrive, et tout change. À 19 ans, il devient le numéro un de la draft NBA : les Spurs le choisissent en premier. C'est un événement historique pour le basket français.")
f.para("Pourquoi tout le monde le regarde ? Parce qu'il joue comme personne : très grand, mais rapide et précis. Il bloque les tirs des adversaires et il marque de loin, avec facilité. Certains commentateurs l'appellent « l'extraterrestre » : sur le terrain, il semble venir d'une autre planète.")
f.para("La France a déjà eu une star en NBA : Tony Parker, quatre fois champion avec San Antonio. Aujourd'hui, Parker regarde les matchs de Wemby comme un grand frère. Entre les deux hommes, une même adresse : San Antonio, une ville devenue un peu française.")
f.para("La saison NBA commence en automne. En France, beaucoup de jeunes se lèvent la nuit pour regarder les matchs en direct. C'est dur pour le réveil du matin... mais quand Wemby joue, le spectacle vaut le voyage.")
f.gloss("un géant um gigante · la draft o draft (escolhas da NBA) · un tir um arremesso · bloquer bloquear, parar · un gardien de but um goleiro · précis preciso · en direct ao vivo.")
f.head("À VOUS ! · SUA VEZ", 25)
f.expl("Leia o artigo da página 4 e escolha a resposta certa.")
f.ex("B1", "单选", "B", "no texto: Il mesure 2,24 mètres",
     "Victor Wembanyama mesure... A. 2,04 m · B. 2,24 m · C. 2,40 m")
f.ex("B1", "单选", "A", "quando criança, também praticou futebol e judô",
     "Enfant, Victor fait aussi... A. du judo · B. du tennis · C. de la danse")
f.ex("B1", "单选", "C", "primeira escolha do draft aos 19 anos",
     "Il devient numéro un de la draft à... A. 17 ans · B. 21 ans · C. 19 ans")
f.ex("B1", "单选", "C", "Parker ganhou quatro títulos da NBA",
     "Tony Parker a gagné... A. deux titres · B. trois titres · C. quatre titres")
f.ex("B1", "单选", "B", "por causa do fuso horário, os torcedores franceses assistem aos jogos à noite",
     "Les fans français regardent les matchs... A. au petit déjeuner · B. la nuit · C. au bureau")
f.expl("Associe cada palavra do esporte ao seu significado.")
f.match_set("B1", "词汇配对",
            ["marquer", "bloquer", "un entraînement", "la saison"],
            ["mettre le ballon dans le panier", "arrêter le tir de l'adversaire",
             "la séance où l'on répète les gestes", "la période des matchs dans l'année"],
            ["a", "b", "c", "d"],
            ["marquer = marcar a", "bloquer = bloquear b", "entraînement = o treino c", "saison = a temporada d"],
            instr="Associe")
f.expl("Complete com o comparativo (plus / moins).")
f.ex("B1", "完成句子", "plus grand", "comparatif : grand → plus grand que",
     "Wemby est ___ (grand) que la plupart des joueurs.")
f.ex("B1", "完成句子", "moins populaire", "o basquete é menos popular na França do que nos Estados Unidos",
     "Le basket est ___ (populaire) en France qu'aux États-Unis. (moins)")
f.ex("B1", "完成句子", "plus fatigant", "um jogo assistido à noite cansa mais",
     "Un match regardé la nuit est ___ (fatigant) qu'un match de jour.")
f.head("LE BASKET, SPORT FRANÇAIS ?", 25)
f.para("Le basket n'est pas né en France — il arrive des États-Unis à la fin du XIXe siècle — mais il y a trouvé une vraie maison. Des milliers de jeunes jouent en club, et l'équipe de France est l'une des meilleures d'Europe. Les matchs de l'équipe nationale remplissent les grandes salles, de Paris à Lille.", 23.5)
f.para("Avec Wembanyama, une nouvelle génération découvre le championnat américain. Les professeurs de sport le racontent : depuis l'arrivée de « Wemby » en NBA, les inscriptions des adolescents dans les clubs augmentent. Un géant de 2,24 mètres fait grandir tout un sport.", 23.5)
f.expl("Nota — une inscription uma inscrição · un championnat um campeonato, uma liga · une salle um ginásio esportivo.")
f.para("À l'école aussi, le basket est partout : dans les cours de sport, sur les terrains des quartiers, et cette semaine dans les recherches Google des Français. La saison ne fait que commencer — la France continuera de se lever la nuit.", 23.5)
f.head("REGARDER UN MATCH EN FRANÇAIS", 25)
f.para("Pour profiter d'un match avec les commentaires français, quelques phrases suffisent. Les commentateurs parlent vite, mais ils répètent souvent les mêmes expressions : écoutez, répétez, criez avec eux !", 23.5)
f.box("LES PHRASES DU COMMENTATEUR", [
    ("« Allez ! » — Vamos! · « Quelle action ! » — Que jogada!", "serif", False, INK, 21.5, 1.42),
    ("« Il marque ! » — Ele marca! · « C'est gagné ! » — Ganhamos!", "serif", False, INK, 21.5, 1.42),
    ("« Quelle ambiance dans la salle ! » — Que clima no ginásio!", "serif", False, INK, 21.5, 1.42),
])
f.para("Exercice d'écoute de la rédaction : regardez dix minutes de match en français et notez trois phrases nouvelles. La semaine prochaine, comparez vos listes en classe — ou envoyez-les à la rédaction (page 8).", 23.5)
f.head("LA NUIT DES MATCHS", 25)
f.para("Il y a un rituel, les soirs de match : on prépare un thé ou un chocolat, on ouvre un carnet, et on regarde le match en famille ou entre amis, parfois très tard. Le lendemain, à l'école ou au bureau, tout le monde raconte la même action — avec les mêmes mots français.", 23.5)
f.para("C'est aussi cela, apprendre une langue : partager des émotions avec des millions de personnes, au même moment, dans la même langue. Wemby joue à San Antonio, mais ses phrases voyagent jusqu'à Paris, Lyon et Dakar.", 23.5)
f.box("LE SAVIEZ-VOUS ?", [
    ("En France, beaucoup de clubs de basket accueillent les débutants toute l'année : la licence coûte souvent moins cher qu'un abonnement de streaming.", "serif", False, INK, 21.5, 1.42),
    ("Sua vez: a página de esportes do próximo número reúne «O primeiro jogo que vi com narração em francês»: bastam duas ou três frases (como enviar: página 8).", "sans", False, GREY, 18.5, 1.4),
])
f.end_report()

# col 3: Parker + vocab + stats + micro-drills
ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, 240, "TONY PARKER, LE PIONNIER", 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "Avant Wemby, il y a Tony Parker. Arrivé à San Antonio à 19 ans, il gagne quatre titres de champion NBA (2003, 2005, 2007, 2014). Aujourd'hui, il est président du club de l'ASVEL, à Villeurbanne, et il reste un modèle pour les jeunes joueurs français.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, "Cette semaine, son nom est aussi dans les recherches Google : la France du basket a la mémoire longue.", 21.5, "serif", False, INK, CW - 44, 1.42)
vy = 696
p.rect(ix, vy, CW, 416, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, vy + 40, "LES MOTS DU SPORT · PALAVRAS", 23, "sans", True, OLIVE)
mots4 = [
    "le basket — o basquete", "un match — um jogo", "un panier — uma cesta; um ponto",
    "un terrain — uma quadra", "un champion — um campeão", "s'entraîner — treinar",
    "un adversaire — um adversário", "un titre — um título",
]
yy4 = vy + 82
for m in mots4:
    p.text(ix + 22, yy4, m, 21.5, "serif", False, INK)
    yy4 += 37
sy4 = vy + 416 + 26
p.rect(ix, sy4, CW, 218, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, sy4 + 40, "WEMBY EN CHIFFRES", 23, "sans", True, OLIVE)
p.para(ix + 22, sy4 + 80, "2,24 m — sa taille · né en 2004 au Chesnay · n° 1 de la draft 2023 · son surnom : « Wemby ».", 21.5, "serif", False, INK, CW - 44, 1.42)
mf = Flow(p, [(ix, CW)], sy4 + 218 + 30, 2540, tag="P4-micro")
mf.head("MICRO-DRILLS · TREINO", 24)
mf.expl("Complete com bloque / marque / gagnent / entraînent / gagné / saison.")
mf.ex("B1", "完成句子", "bloque", "bloquer les tirs = bloquear os arremessos",
      "Wemby ___ le tir de l'adversaire.", size=23)
mf.ex("B1", "完成句子", "marque", "marquer un panier = fazer uma cesta",
      "Il ___ un panier de très loin !", size=23)
mf.ex("B1", "完成句子", "gagnent", "ils gagnent le match",
      "Les Spurs ___ le match 98 à 90.", size=23)
mf.ex("B1", "完成句子", "entraînent", "s'entraîner = treinar (forma ils)",
      "Les joueurs s'___ tous les jours.", size=23)
mf.ex("B1", "完成句子", "gagné", "passé composé : a gagné",
      "Parker a ___ quatre titres NBA.", size=23)
mf.ex("A2", "完成句子", "saison", "la saison commence en automne",
      "La ___ NBA commence en automne.", size=23)
mf.end_report()
db4 = mf.y + 6
p.rect(ix, db4, CW, 2540 - db4, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, db4 + 40, "LE DÉBAT · O DEBATE", 23, "sans", True, OLIVE)
p.para(ix + 22, db4 + 78, "Se lever à 3 heures du matin pour un match : folie ou passion ? Discutez en classe : deux phrases pour, deux phrases contre.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, db4 + 196, "Acordar às 3 da manhã por um jogo: loucura ou paixão? Escreva duas frases a favor e duas contra.", 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
