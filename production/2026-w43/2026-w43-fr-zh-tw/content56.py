# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 青年 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JEUNESSE & ÉCRANS　青年", "Le Lucerna", "NIVEAU B1　GTA VI　Réseaux sociaux")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P5-main")
f.title("GTA VI : le jeu que tout le monde attend", 32)
f.byline("Par la rédaction　Niveau de lecture : B1")
f.para("C'est peut-être le jeu vidéo le plus attendu de la planète. Grand Theft Auto VI — GTA VI — est encore une fois, cette semaine, dans les recherches Google en France. Les fans attendent, regardent les bandes-annonces et comptent les jours.")
f.para("La série GTA est célèbre pour ses villes immenses : on se promène librement dans un monde ouvert, en voiture ou à pied. Pour beaucoup de joueurs, c'est comme un film interactif géant — avec de l'humour, de la musique et des histoires de personnages attachants.")
f.para("En France, le jeu vidéo est un loisir de masse : des millions de personnes jouent, sur console, sur ordinateur ou sur téléphone. Les jeunes, bien sûr, mais aussi leurs parents. Et les mots du jeu vidéo sont partout : « streamer », « gamer », « spoiler »... mélangés au français de tous les jours.")
f.para("Pourquoi tant d'attente ? Parce que les grands jeux sont rares, et parce que chaque bande-annonce devient un événement mondial, regardé des centaines de millions de fois. En attendant la sortie, les fans imaginent, dessinent et discutent. L'attente, elle aussi, fait partie du jeu.")
f.gloss("un jeu vidéo 電子遊戲 · une bande-annonce 預告片 · un monde ouvert 開放世界 · une console 遊戲主機 · la sortie （遊戲）發售 · un loisir 休閒娛樂。")
f.head("À VOUS !　即學即練", 25)
f.expl("讀第 5 版文章，選出正確答案。")
f.ex("B1", "單選", "B", "GTA 以巨大的開放世界城市聞名",
     "La série GTA est célèbre pour... A. ses petites villes · B. ses mondes ouverts · C. ses jeux de cartes")
f.ex("B1", "單選", "B", "文中：des millions de personnes jouent",
     "En France, le jeu vidéo concerne... A. seulement les enfants · B. des millions de personnes · C. personne")
f.ex("B1", "單選", "B", "預告片是世界級事件",
     "Chaque bande-annonce devient... A. un secret · B. un événement mondial · C. un examen")
f.ex("B1", "單選", "A", "等待本身也是遊戲的一部分",
     "Pour les fans, l'attente... A. fait partie du jeu · B. est interdite · C. est terminée")
f.head("LE FRANÇAIS FAIT SON SHOW", 24)
f.para("Cette semaine, sur les réseaux sociaux, le français devient une star. Des vidéos comiques transforment la langue en personnage : « le français » arrive comme une vedette difficile — il a des règles partout, des exceptions, et il refuse de se prononcer comme il s'écrit ! Les apprenants se reconnaissent et rient : oui, c'est exactement ça.", 23.5)
f.para("Autre tendance : la lecture « chic ». Des photos esthétiques montrent des lecteurs avec des livres français — un café, une bougie, un roman ouvert. Le message : lire en français, c'est beau, c'est chic. Sous les photos, les commentaires demandent : « Quel livre pour commencer ? »", 23.5)
f.para("Réponse des professeurs et des libraires : des listes de livres par niveau. A2 pour débuter doucement, B1 pour les lecteurs courageux, B2 pour les passionnés. Lire un vrai livre, même lentement, même avec un dictionnaire : c'est la méthode que ce journal défend chaque semaine.", 23.5)
f.expl("用 virale / partager / abonnés / commentaire 填空。")
f.ex("B1", "完成句子", "virale", "vidéo virale 爆紅影片",
     "Une vidéo ___ est vue par des millions de personnes.")
f.ex("B1", "完成句子", "partager", "partager = 分享",
     "Clique sur le bouton pour ___ la photo avec tes amis.")
f.ex("B1", "完成句子", "abonnés", "des abonnés 粉絲、訂閱者",
     "Elle a 10 000 ___ sur son compte.")
f.ex("B1", "完成句子", "commentaire", "un commentaire 一則評論",
     "Écris un ___ sous la vidéo !")
f.expl("完成句子，表達看法（參考答案見第 8 版）。")
f.ex("B1", "完成句子", "ex. : amusant, parce que les enfants adorent se déguiser（參考答案）", "開放題，言之成理即可",
     "À mon avis, Halloween en France, c'est ___ parce que ___.")
f.ex("B1", "完成句子", "ex. : j'aime les histoires et les mots nouveaux（參考答案）", "開放題，言之成理即可",
     "Je lis en français parce que ___.")
f.ex("B2", "完成句子", "ex. : ce ne sont pas les résultats（參考答案）", "開放題，言之成理即可",
     "Les sondages sont utiles, mais ___.")
f.expl("即學即練 · 社交熱議小題。")
f.ex("B1", "完成句子", "personnage", "語言變成一個角色",
     "Dans les vidéos comiques, le français devient un ___.")
f.ex("A2", "完成句子", "chic", "lire en français, c'est chic",
     "Lire en français, c'est ___ : c'est la tendance du moment.")
f.ex("A2", "完成句子", "niveau", "des listes par niveau 按級別",
     "Les professeurs proposent des listes de livres par ___.")
f.ex("B1", "完成句子", "dictionnaire", "même avec un dictionnaire",
     "On peut lire un vrai livre, même avec un ___.")
f.ex("B2", "完成句子", "reconnaissent", "se reconnaître 在其中看到自己",
     "Les apprenants se ___ dans ces vidéos : c'est exactement eux !")
f.ex("B1", "完成句子", "esthétique", "une photo esthétique 氛圍感照片",
     "Une photo ___ montre un café, une bougie, un roman ouvert.")
f.head("LIRE OU JOUER ? LES DEUX !", 24)
f.para("Faut-il choisir entre les écrans et les livres ? Pas forcément. Beaucoup de joueurs deviennent lecteurs : les jeux racontent des histoires, donnent envie de lire les romans, les bandes dessinées et les guides qui les entourent. Et beaucoup de lecteurs jouent : un livre le matin, une partie le soir.", 23.5)
f.para("La bonne question n'est donc pas « écran ou livre ? », mais « quoi, sur l'écran ? ». Un texte long, une vraie histoire, un article comme celui-ci : l'écran peut aussi être une page. C'est le pari de ce journal, que vous lisez peut-être... sur un écran.", 23.5)
f.box("PETIT LEXIQUE DU JEU", [
    ("un niveau — 關卡 · sauvegarder — 存檔 · un défi — 挑戰", "serif", False, INK, 21.5, 1.42),
    ("perdre / gagner une partie — 輸掉/贏下一局", "serif", False, INK, 21.5, 1.42),
])
f.end_report()

# col 3 boxes
ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX)
p.text(ix + 22, 240, "LES MOTS DES ÉCRANS　螢幕詞表", 22, "sans", True, OLIVE)
mots5 = [
    "un écran — 螢幕", "un réseau social — 社交網路", "viral — 爆紅的",
    "un abonné — 粉絲、訂閱者", "partager — 分享", "un commentaire — 評論",
    "en ligne — 線上", "un joueur — 玩家", "attendre — 等待",
    "une sortie — 發售、上映",
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
p.para(ix + 22, qy5 + 322, "你讀的第一本法語書是什麼？在評論區告訴我們。", 20, "sans", False, GREY, CW - 44, 1.4)
dy5 = qy5 + 400 + 26
p.rect(ix, dy5, CW, 440, fill=BOX)
p.text(ix + 22, dy5 + 40, "LE DÉBAT　螢幕時間", 23, "sans", True, OLIVE)
p.para(ix + 22, dy5 + 78, "Combien d'heures par jour devant un écran ? Pour jouer, regarder, lire... Les écrans sont-ils des ennemis des livres, ou une autre porte pour entrer dans la langue ?", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 240, "Petit test de la rédaction : ce soir, remplacez trente minutes d'écran par trente minutes de lecture — et racontez-nous la différence (page 8).", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 372, "今晚試一次：少看半小時螢幕，多讀半小時書。", 20, "sans", False, GREY, CW - 44, 1.4)
sy5 = dy5 + 440 + 26
p.text(ix, sy5 + 24, "LE SONDAGE DE LA RÉDACTION", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, sy5 + 38, OLIVE, 2)
p.para(ix, sy5 + 76, "Quel jeu attendez-vous le plus ? Quel livre français lisez-vous en ce moment ? Répondez dans les commentaires : résultats dans le prochain numéro.", 21.5, "serif", False, INK, CW, 1.42)
p.para(ix, sy5 + 210, "編輯部小調查：你在等哪款遊戲？在讀哪本法語書？", 20, "sans", False, GREY, CW, 1.4)
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

# ================= P6 · 時事 (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("POLITIQUE & CHIFFRES　時事", "Le Lucerna", "NIVEAU B2　Présidentielle 2027　大選深讀")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1420, tag="P6-deep")
f.title("Présidentielle 2027 : comprendre l'élection et ses chiffres", 32)
f.byline("Par la rédaction　Niveau de lecture : B2")
f.para("En avril 2027, les Français éliront leur président — ou leur présidente. Le président est élu pour cinq ans, au suffrage universel direct : chaque citoyen de 18 ans et plus peut voter. L'élection se déroule en deux tours. Au premier tour, tous les candidats sont en compétition. Si personne n'obtient plus de 50 % des voix, un second tour oppose, deux semaines plus tard, les deux candidats arrivés en tête.")
f.para("À six mois du scrutin, la bataille des chiffres a commencé. Les instituts publient régulièrement des « intentions de vote » : si l'élection avait lieu dimanche, pour qui voteriez-vous ? Ces enquêtes ne prédisent pas le résultat — elles photographient l'opinion à un moment donné. Un écart de deux points peut tenir à la marge d'erreur.")
f.para("Lire un sondage, c'est déjà faire de la politique : qui devance qui ? Qui gagne des points, qui en perd ? Le vocabulaire des comparaisons envahit les titres des journaux : « X creuse l'écart », « Y passe devant », « Z stagne ». Pour les apprenants de français, c'est un terrain d'entraînement idéal : les chiffres, les pourcentages et le comparatif y sont partout.")
f.para("La campagne, elle, ne fait que commencer : les partis choisissent leurs candidats, les programmes se préparent. Une chose est sûre : jusqu'en 2027, les sondages rythmeront la vie politique française — cette semaine, ils sont la recherche numéro un du pays sur Google.")
f.gloss("un scrutin 投票、選舉 · une marge d'erreur 誤差範圍 · creuser l'écart 拉開差距 · devancer 反超 · rythmer 為……定下節奏。")
f.end_report()

# practice poll chart, span cols 0-1
chx, chw = MX, 896
chy = 1470
p.rect(chx, chy, chw, 470, fill=BOX)
p.text(chx + 24, chy + 42, "SONDAGE D'ENTRAÎNEMENT　練習民調圖", 25, "sans", True, OLIVE)
p.text(chx + 24, chy + 74, "Données simplifiées pour l'exercice — aucun institut, aucun vrai candidat.", 19.5, "sans", False, OLIVE)
p.text(chx + 24, chy + 100, "本圖為教學練習數據，不對應任何真實民調機構或候選人。", 19, "sans", False, GREY)
bars = [("Candidat A", 28, OLIVE), ("Candidate B", 24, OLIVE), ("Candidat C", 17, OLIVE),
        ("Candidat D", 11, OLIVE), ("Autres", 9, OLIVE), ("Indécis", 11, "#8a8168")]
byy = chy + 128
for lab, val, col in bars:
    p.text(chx + 24, byy + 26, lab, 22, "serif", True, INK)
    p.rect(chx + 200, byy + 6, val * 18, 26, fill=col)
    p.text(chx + 212 + val * 18, byy + 27, f"{val} %", 22, "sans", True, OLIVE)
    byy += 52

e6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 1990, 2560, tag="P6-chart-ex")
e6.head("LIRE LE GRAPHIQUE　讀圖", 25)
e6.expl("看上面的練習民調圖回答問題。")
e6.ex("B2", "圖表讀數", "Le candidat A, avec 28 %", "A 以 28 % 居首",
      "Qui est en tête du sondage ?", size=23)
e6.ex("B2", "圖表讀數", "4 points", "28 − 24 = 4 個百分點",
      "Combien de points séparent le candidat A de la candidate B ?", size=23)
e6.ex("B2", "圖表讀數", "Faux", "17 % 並非 11 % 的兩倍",
      "Vrai ou faux : le candidat C a deux fois plus de voix que le candidat D.", size=23)
e6.ex("B2", "圖表讀數", "11 %", "Indécis（未決定）= 11 %",
      "Quel est le pourcentage des indécis ?", size=23)
e6.ex("B2", "圖表讀數", "La candidate B (27 % contre 26 %)", "B+3=27，A−2=26，B 反超",
      "Si B gagne 3 points et A en perd 2, qui passe devant ?", size=23)
e6.ex("B2", "圖表讀數", "Oui, 52 %", "28 + 24 = 52 %，超過半數",
      "Les candidats A et B, ensemble, dépassent-ils 50 % ?", size=23)
e6.end_report()

# right half, col 2: vocab box + comparatif + vocab MCQ + headline phrases
g = Flow(p, [(COLX[2], CW)], 200, 2560, tag="P6-right2")
g.box("LES MOTS DU SCRUTIN　選舉詞表", [
    ("un sondage — 民意調查 · une intention de vote — 投票意向", "serif", False, INK, 21.5, 1.42),
    ("devancer — 反超 · creuser l'écart — 拉開差距", "serif", False, INK, 21.5, 1.42),
    ("stagner — 停滯 · un échantillon — 抽樣樣本", "serif", False, INK, 21.5, 1.42),
    ("un parti — 政黨 · se qualifier — 晉級下一輪", "serif", False, INK, 21.5, 1.42),
])
g.head("LE COMPARATIF EN CAMPAGNE", 24)
g.expl("用比較級完成句子。")
g.ex("B2", "完成句子", "plus populaire", "A 28 % > B 24 %",
     "Dans ce sondage, A est ___ (populaire) que B.", size=23)
g.ex("B2", "完成句子", "moins", "D 11 % < C 17 %，用 moins de",
     "D obtient ___ de voix que C.", size=23)
g.ex("B2", "完成句子", "aussi", "11 % = 11 %，一樣多用 aussi",
     "Les indécis sont ___ nombreux que les partisans de D.", size=23)
g.ex("B2", "完成句子", "meilleur", "bon 的比較級是 meilleur",
     "Ce sondage est ___ (bon) que le précédent : l'échantillon est plus grand.", size=23)
g.head("LES MOTS　詞彙", 25)
g.expl("選出正確釋義。")
g.ex("B2", "單選", "B", "devancer = 超過、走在前面",
     "« Devancer » signifie... A. arriver après · B. passer devant · C. abandonner", size=23)
g.ex("B2", "單選", "C", "un scrutin = 一次投票",
     "Un « scrutin » est... A. un débat · B. un parti politique · C. un vote", size=23)
g.ex("B2", "單選", "A", "誤差範圍只關乎數字",
     "La « marge d'erreur » concerne... A. les chiffres du sondage · B. le prix du journal · C. l'heure du vote", size=23)
g.ex("B2", "單選", "B", "être en tête = 排第一",
     "« Être en tête » veut dire... A. réfléchir · B. être le premier · C. être fatigué", size=23)
g.box("LES PHRASES DES JOURNAUX", [
    ("« X creuse l'écart. » — X 拉開差距。", "serif", False, INK, 21.5, 1.42),
    ("« Y passe devant. » — Y 反超到前面。", "serif", False, INK, 21.5, 1.42),
    ("« Z en chute libre. » — Z 支持率暴跌。", "serif", False, INK, 21.5, 1.42),
    ("« W crée la surprise. » — W 爆冷、製造驚喜。", "serif", False, INK, 21.5, 1.42),
])
g.end_report()

# right half, col 3: micro-drills + history box + big number + débat
g2 = Flow(p, [(COLX[3], CW)], 200, 2560, tag="P6-right3")
g2.head("MICRO-DRILLS　即學即練", 25)
g2.expl("補全選舉常識短語。")
g2.ex("B2", "完成句子", "universel", "suffrage universel 直接普選",
      "Le président est élu au suffrage ___ direct.", size=23)
g2.ex("B2", "完成句子", "second", "le second tour 第二輪",
      "Si personne n'a plus de 50 %, il y a un ___ tour.", size=23)
g2.ex("B2", "完成句子", "erreur", "la marge d'erreur 誤差範圍",
      "Un petit écart peut tenir à la marge d'___.", size=23)
g2.ex("B1", "完成句子", "dix-huit", "18 歲起可投票",
      "En France, on vote à partir de ___ ans.", size=23)
g2.box("TROIS DATES POUR COMPRENDRE", [
    ("1962 — le président est élu directement par les citoyens.", "serif", False, INK, 21.5, 1.42),
    ("1974 — on peut voter dès 18 ans.", "serif", False, INK, 21.5, 1.42),
    ("2000 — le mandat passe de sept ans à cinq ans : c'est le quinquennat.", "serif", False, INK, 21.5, 1.42),
    ("三場改革定型了今天的法國大選。", "sans", False, GREY, 20, 1.4),
], tsize=21)
g2.head("LE CHIFFRE DE LA SEMAINE", 25)
g2.para("5 000 +", 54, "serif", True, OLIVE, 1.1, 4)
g2.para("C'est le nombre de recherches quotidiennes, en France, pour « sondage présidentielle 2027 » — la recherche numéro un du pays cette semaine (Google Trends).", 22)
g2.head("LE DÉBAT　討論", 25)
g2.para("Les sondages influencent-ils le vote ? Certains disent oui : on aime voter pour le gagnant. D'autres disent non : les électeurs choisissent leurs idées, pas les chiffres. Et vous, qu'en pensez-vous ? Deux phrases, en français, dans les commentaires.", 22)
g2.expl("民調會影響投票嗎？寫兩句你的看法。")
g2.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
