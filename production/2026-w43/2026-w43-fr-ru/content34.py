# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-fr-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band('CULTURE · КУЛЬТУРА', "Le Lucerna", 'NIVEAU A2 → B1 · La Toussaint · ДЕНЬ ВСЕХ СВЯТЫХ')

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P3-main")
f.title("La Toussaint : le jour des fleurs et des souvenirs", 37)
f.byline("Par la rédaction · Niveau de lecture : A2 → B1")
f.para("Le 1er novembre, la France fête la Toussaint. À l'origine, c'est la fête de tous les saints. Aujourd'hui, pour beaucoup de familles, c'est surtout le jour du souvenir : on pense aux personnes mortes qu'on a aimées.")
f.para("Ce jour-là, les cimetières se remplissent de fleurs. La fleur de la Toussaint, c'est le chrysanthème. Les Français en achètent des millions : blancs, jaunes, violets... On les pose sur les tombes, on nettoie les pierres, et on reste un moment en silence avec la famille.")
f.para("Attention, voyageurs ! En France, le chrysanthème est la fleur des cimetières. On n'offre jamais de chrysanthèmes pour un anniversaire ou pour un dîner. Pour faire plaisir, choisissez des roses ou des tulipes !")
f.para("La Toussaint arrive pendant les vacances scolaires : les familles voyagent pour se retrouver. Le 1er novembre est un jour férié : les écoles, les bureaux et beaucoup de magasins sont fermés. Dans les villages comme dans les grandes villes, c'est un jour calme, doux et un peu mélancolique — le cœur de l'automne français.")
f.gloss("un cimetière кладбище · une tombe могила · un jour férié праздник, выходной · le souvenir воспоминание · mélancolique меланхоличный · à l'origine изначально.")
f.head('À VOUS ! · ТЕПЕРЬ ВЫ!', 25)
f.expl('Верно или неверно? (Vrai / Faux)')
f.ex("A2", "阅读判断", "Faux", 'День всех святых — 1 ноября, а не 31 октября',
     "La Toussaint est le 31 octobre.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Vrai", 'в тексте: les cimetières se remplissent de fleurs',
     "Le 1er novembre, les cimetières sont pleins de fleurs.", instr="Vrai ou faux ?")
f.ex("A2", "阅读判断", "Faux", 'во Франции хризантема — кладбищенский цветок: её никогда не дарят',
     "On offre des chrysanthèmes pour un anniversaire.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Faux", '1 ноября — jour férié: школы закрыты',
     "Le 1er novembre, les écoles sont ouvertes.", instr="Vrai ou faux ?")
f.ex("B1", "阅读判断", "Faux", 'текст говорит la fête divise: мнения расходятся',
     "Tous les Français adorent Halloween.", instr="Vrai ou faux ?")
f.expl('Вставьте cimetière / tombe / déguisement / citrouille.')
f.ex("B1", "完成句子", "déguisement", 'на Хэллоуин наряжаются (déguisement)',
     "Pour Halloween, les enfants portent un ___.")
f.ex("A2", "完成句子", "tombe", 'цветы кладут на могилу',
     "On pose les fleurs sur la ___.")
f.ex("A2", "完成句子", "cimetière", '1 ноября кладбище полно цветов',
     "Le ___ est plein de fleurs le 1er novembre.")
f.ex("B1", "完成句子", "citrouille", 'тыква — символ Хэллоуина',
     "Une ___ orange est le symbole d'Halloween.")
f.expl('Перепишите предложения (с ne...jamais / ne...plus / ne...pas).')
f.ex("B1", "句型转换", "On n'offre jamais de chrysanthèmes pour un anniversaire.", 'jamais + de (без артикля)',
     "(jamais) On offre des chrysanthèmes pour un anniversaire. → ___", instr='Перепишите')
f.ex("B1", "句型转换", "Les feuilles ne sont plus vertes en automne.", 'ne...plus = больше не',
     "(plus) Les feuilles sont vertes en automne. → ___", instr='Перепишите')
f.ex("B1", "句型转换", "Le 1er novembre n'est pas un jour de travail pour tous.", "n'est pas = отрицание",
     "(pas) Le 1er novembre est un jour de travail pour tous. → ___", instr='Перепишите')
f.head("HALLOWEEN : LA FÊTE QUI DIVISE", 25)
f.para("Le 31 octobre, c'est Halloween. Les enfants se déguisent — sorcières, fantômes, super-héros — et ils frappent aux portes : « Des bonbons ou un sort ! » On leur donne des bonbons, et tout le monde rit.", 23.5)
f.para("En France, la fête vient des États-Unis. Certains l'adorent : c'est joyeux, coloré, parfait pour les enfants. D'autres disent : « Ce n'est pas notre tradition, c'est du commerce. » Mais dans les écoles et les villages, les citrouilles orange sont de plus en plus nombreuses. Cette année, Halloween tombe un samedi, pendant les vacances : les familles auront le temps de préparer la fête. Et vous, pour ou contre ?", 23.5)
f.expl('Теперь вы · Вопросы о Хэллоуине.')
f.ex("A2", "完成句子", "sort", '« Des bonbons ou un sort ! » = конфеты или жизнь',
     "« Des bonbons ou un ___ ! » crient les enfants.")
f.ex("B1", "完成句子", "déguisent", 'se déguiser = наряжаться (форма ils)',
     "Les enfants se ___ en sorcières et en fantômes.")
f.ex("A2", "完成句子", "bonbons", 'дети просят конфеты (bonbons)',
     "On frappe à la porte et on demande des ___.")
f.ex("A2", "完成句子", "États-Unis", 'Хэллоуин пришёл из США (по тексту)',
     "En France, la fête d'Halloween vient des ___.")
f.ex("B1", "单选", "B", 'diviser = мнения разделяются',
     "« La fête divise » signifie... A. tout le monde est d'accord · B. les avis sont partagés · C. personne ne vient")
f.ex("B1", "完成句子", "déguisements", 'покупать конфеты и костюмы',
     "Pour la fête, on achète des bonbons et des ___.")
f.head("LA TOUSSAINT DANS LE MONDE", 25)
f.para("Le 1er novembre n'est pas férié qu'en France : la Belgique fête aussi la Toussaint, et les familles y visitent les cimetières avec des chrysanthèmes. Le mot « Toussaint » signifie « tous les saints » : la fête honore tous les saints, connus et inconnus.", 23.5)
f.para("Le 2 novembre, au Mexique, c'est le Día de los Muertos, le Jour des Morts : les familles préparent des autels avec des photos, des fleurs orange et les plats préférés des disparus. L'ambiance est très différente : musique, couleurs et fête — mais l'idée est la même : ne pas oublier ceux qu'on aime.", 23.5)
f.para("Et le 31 octobre au soir, pendant que les enfants français demandent des bonbons, beaucoup de familles pensent déjà au lendemain : acheter les fleurs, préparer le voyage, téléphoner aux grands-parents. L'automne est la saison du souvenir — et des retrouvailles.", 23.5)
f.expl('Пояснение — un autel алтарь · un disparu ушедший близкий · les retrouvailles встреча вновь.')
f.box("LE MOT DE LA PAGE", [
    ("« chrysanthème » vient du grec : chrysos (l'or) + anthemon (la fleur) — la « fleur d'or ».", "serif", False, INK, 22, 1.42),
    ('Хризантема: цветок с золотом в названии.', "sans", False, GREY, 20, 1.4),
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
p.text(ix + 22, by3 + 40, 'LES MOTS DES FÊTES · СЛОВА', 23, "sans", True, OLIVE)
mots = [
    'un saint — святой', 'un cimetière — кладбище', 'une tombe — могила',
    'un jour férié — праздник, выходной', 'se souvenir — вспоминать',
    'un déguisement — костюм, наряд', 'une citrouille — тыква',
    'un bonbon — конфета', 'un fantôme — призрак', 'un sort — заклинание',
]
yy3 = by3 + 82
for m in mots:
    p.text(ix + 22, yy3, m, 21.5, "serif", False, INK)
    yy3 += 37
zy3 = by3 + 452 + 26
p.rect(ix, zy3, CW, 476, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, zy3 + 40, 'ZOOM · МОГИЛЫ ПИСАТЕЛЕЙ', 23, "sans", True, OLIVE)
p.para(ix + 22, zy3 + 78, "À Paris, le cimetière du Père-Lachaise est le plus visité du monde. On y trouve les tombes de Balzac, d'Oscar Wilde et de Marcel Proust. Le 1er novembre, des lecteurs y déposent des fleurs... et parfois un livre.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, zy3 + 340, 'На Пер-Лашез покоятся Бальзак, Уайльд и Пруст: в День всех святых читатели могут принести цветок к могилам писателей.', 20, "sans", False, GREY, CW - 44, 1.4)
dy3 = zy3 + 476 + 26
p.rect(ix, dy3, CW, 330, fill=BOX, stroke=LINE, sw=1.4)
p.text(ix + 22, dy3 + 40, 'DATES À RETENIR · ДАТЫ МЕСЯЦА', 23, "sans", True, OLIVE)
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
p.para(ix + 22, yy3 + 20, 'Три дня подряд: Хэллоуин, День всех святых, а потом снова уроки.', 19.5, "sans", False, GREY, CW - 44, 1.4)
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
p.band('SPORT · СПОРТ', "Le Lucerna", "NIVEAU B1 · NBA · Wembanyama")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P4-main")
f.title("Wemby : le géant français qui fait rêver la NBA", 37)
f.byline("Par la rédaction · Niveau de lecture : B1")
f.para("Il mesure 2,24 mètres. Il a de très longs bras. Et cette semaine, son équipe est dans les recherches Google de toute la France : les Spurs de San Antonio contre Oklahoma City. Le nom du phénomène : Victor Wembanyama, dit « Wemby ».")
f.para("Né au Chesnay, près de Paris, Victor commence le sport enfant : d'abord le football — il est gardien de but ! — et le judo. Puis le basket arrive, et tout change. À 19 ans, il devient le numéro un de la draft NBA : les Spurs le choisissent en premier. C'est un événement historique pour le basket français.")
f.para("Pourquoi tout le monde le regarde ? Parce qu'il joue comme personne : très grand, mais rapide et précis. Il bloque les tirs des adversaires et il marque de loin, avec facilité. Certains commentateurs l'appellent « l'extraterrestre » : sur le terrain, il semble venir d'une autre planète.")
f.para("La France a déjà eu une star en NBA : Tony Parker, quatre fois champion avec San Antonio. Aujourd'hui, Parker regarde les matchs de Wemby comme un grand frère. Entre les deux hommes, une même adresse : San Antonio, une ville devenue un peu française.")
f.para("La saison NBA commence en automne. En France, beaucoup de jeunes se lèvent la nuit pour regarder les matchs en direct. C'est dur pour le réveil du matin... mais quand Wemby joue, le spectacle vaut le voyage.")
f.gloss('un géant великан · la draft драфт (выбор в NBA) · un tir бросок · bloquer блокировать · un gardien de but вратарь · précis точный · en direct в прямом эфире.')
f.head('À VOUS ! · ТЕПЕРЬ ВЫ!', 25)
f.expl('Прочитайте статью на стр. 4 и выберите ответ.')
f.ex("B1", "单选", "B", 'в тексте: Il mesure 2,24 mètres',
     "Victor Wembanyama mesure... A. 2,04 m · B. 2,24 m · C. 2,40 m")
f.ex("B1", "单选", "A", 'в детстве — футбол и дзюдо',
     "Enfant, Victor fait aussi... A. du judo · B. du tennis · C. de la danse")
f.ex("B1", "单选", "C", 'первый выбор драфта в 19 лет',
     "Il devient numéro un de la draft à... A. 17 ans · B. 21 ans · C. 19 ans")
f.ex("B1", "单选", "C", 'Паркер выиграл четыре титула NBA',
     "Tony Parker a gagné... A. deux titres · B. trois titres · C. quatre titres")
f.ex("B1", "单选", "B", 'фанаты во Франции смотрят матчи ночью',
     "Les fans français regardent les matchs... A. au petit déjeuner · B. la nuit · C. au bureau")
f.expl('Соедините слова с их значениями.')
f.match_set("B1", "词汇配对",
            ["marquer", "bloquer", "un entraînement", "la saison"],
            ["mettre le ballon dans le panier", "arrêter le tir de l'adversaire",
             "la séance où l'on répète les gestes", "la période des matchs dans l'année"],
            ["a", "b", "c", "d"],
            ['marquer = забивать a', 'bloquer = останавливать b', 'entraînement = тренировка c', 'saison = сезон d'],
            instr='Соедините')
f.expl('Вставьте сравнительную степень (plus / moins).')
f.ex("B1", "完成句子", "plus grand", "comparatif : grand → plus grand que",
     "Wemby est ___ (grand) que la plupart des joueurs.")
f.ex("B1", "完成句子", "moins populaire", 'баскетбол во Франции менее популярен, чем в США',
     "Le basket est ___ (populaire) en France qu'aux États-Unis. (moins)")
f.ex("B1", "完成句子", "plus fatigant", 'матч, который смотришь ночью, утомляет сильнее',
     "Un match regardé la nuit est ___ (fatigant) qu'un match de jour.")
f.head("LE BASKET, SPORT FRANÇAIS ?", 25)
f.para("Le basket n'est pas né en France — il arrive des États-Unis à la fin du XIXe siècle — mais il y a trouvé une vraie maison. Des milliers de jeunes jouent en club, et l'équipe de France est l'une des meilleures d'Europe. Les matchs de l'équipe nationale remplissent les grandes salles, de Paris à Lille.", 23.5)
f.para("Avec Wembanyama, une nouvelle génération découvre le championnat américain. Les professeurs de sport le racontent : depuis l'arrivée de « Wemby » en NBA, les inscriptions des adolescents dans les clubs augmentent. Un géant de 2,24 mètres fait grandir tout un sport.", 23.5)
f.expl('Пояснение — une inscription регистрация · un championnat чемпионат, лига · une salle спортзал.')
f.para("À l'école aussi, le basket est partout : dans les cours de sport, sur les terrains des quartiers, et cette semaine dans les recherches Google des Français. La saison ne fait que commencer — la France continuera de se lever la nuit.", 23.5)
f.head("REGARDER UN MATCH EN FRANÇAIS", 25)
f.para("Pour profiter d'un match avec les commentaires français, quelques phrases suffisent. Les commentateurs parlent vite, mais ils répètent souvent les mêmes expressions : écoutez, répétez, criez avec eux !", 23.5)
f.box("LES PHRASES DU COMMENTATEUR", [
    ('« Allez ! » — Вперёд! · « Quelle action ! » — Какая атака!', "serif", False, INK, 21.5, 1.42),
    ("« Il marque ! » — Он забрасывает! · « C'est gagné ! » — Победа!", "serif", False, INK, 21.5, 1.42),
    ('« Quelle ambiance dans la salle ! » — Какая атмосфера в зале!', "serif", False, INK, 21.5, 1.42),
])
f.para("Exercice d'écoute de la rédaction : regardez dix minutes de match en français et notez trois phrases nouvelles. La semaine prochaine, comparez vos listes en classe — ou envoyez-les à la rédaction (page 8).", 23.5)
f.head("LA NUIT DES MATCHS", 25)
f.para("Il y a un rituel, les soirs de match : on prépare un thé ou un chocolat, on ouvre un carnet, et on regarde le match en famille ou entre amis, parfois très tard. Le lendemain, à l'école ou au bureau, tout le monde raconte la même action — avec les mêmes mots français.", 23.5)
f.para("C'est aussi cela, apprendre une langue : partager des émotions avec des millions de personnes, au même moment, dans la même langue. Wemby joue à San Antonio, mais ses phrases voyagent jusqu'à Paris, Lyon et Dakar.", 23.5)
f.box("LE SAVIEZ-VOUS ?", [
    ("En France, beaucoup de clubs de basket accueillent les débutants toute l'année : la licence coûte souvent moins cher qu'un abonnement de streaming.", "serif", False, INK, 21.5, 1.42),
    ('Теперь вы: следующий номер собирает тексты «Первый матч, который я смотрел с французским комментарием»: хватит 2–3 предложений (отправка: стр. 8).', "sans", False, GREY, 18.5, 1.4),
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
p.text(ix + 22, vy + 40, 'LES MOTS DU SPORT · СЛОВА', 23, "sans", True, OLIVE)
mots4 = [
    'le basket — баскетбол', 'un match — матч', 'un panier — корзина; очко',
    'un terrain — площадка, поле', 'un champion — чемпион', "s'entraîner — тренироваться",
    'un adversaire — соперник', 'un titre — титул',
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
mf.head('MICRO-DRILLS · ТРЕНИРОВКА', 24)
mf.expl('Вставьте bloque / marque / gagnent / entraînent / gagné / saison.')
mf.ex("B1", "完成句子", "bloque", 'bloquer les tirs = останавливать броски',
      "Wemby ___ le tir de l'adversaire.", size=23)
mf.ex("B1", "完成句子", "marque", 'marquer un panier = забросить в корзину',
      "Il ___ un panier de très loin !", size=23)
mf.ex("B1", "完成句子", "gagnent", "ils gagnent le match",
      "Les Spurs ___ le match 98 à 90.", size=23)
mf.ex("B1", "完成句子", "entraînent", "s'entraîner = тренироваться (форма ils)",
      "Les joueurs s'___ tous les jours.", size=23)
mf.ex("B1", "完成句子", "gagné", "passé composé : a gagné",
      "Parker a ___ quatre titres NBA.", size=23)
mf.ex("A2", "完成句子", "saison", "la saison commence en automne",
      "La ___ NBA commence en automne.", size=23)
mf.end_report()
db4 = mf.y + 6
p.rect(ix, db4, CW, 2540 - db4, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(ix + 22, db4 + 40, 'LE DÉBAT · ДЕБАТЫ', 23, "sans", True, OLIVE)
p.para(ix + 22, db4 + 78, "Se lever à 3 heures du matin pour un match : folie ou passion ? Discutez en classe : deux phrases pour, deux phrases contre.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, db4 + 196, 'Вставать в 3 часа ночи ради матча: безумие или страсть? Напишите два предложения «за» и два «против».', 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
