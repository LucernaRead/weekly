# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 青年 (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band('JEUNESSE & ÉCRANS　청소년', "Le Lucerna", "NIVEAU B1　GTA VI　Réseaux sociaux")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P5-main")
f.title("GTA VI : le jeu que tout le monde attend", 32)
f.byline("Par la rédaction　Niveau de lecture : B1")
f.para("C'est peut-être le jeu vidéo le plus attendu de la planète. Grand Theft Auto VI — GTA VI — est encore une fois, cette semaine, dans les recherches Google en France. Les fans attendent, regardent les bandes-annonces et comptent les jours.")
f.para("La série GTA est célèbre pour ses villes immenses : on se promène librement dans un monde ouvert, en voiture ou à pied. Pour beaucoup de joueurs, c'est comme un film interactif géant — avec de l'humour, de la musique et des histoires de personnages attachants.")
f.para("En France, le jeu vidéo est un loisir de masse : des millions de personnes jouent, sur console, sur ordinateur ou sur téléphone. Les jeunes, bien sûr, mais aussi leurs parents. Et les mots du jeu vidéo sont partout : « streamer », « gamer », « spoiler »... mélangés au français de tous les jours.")
f.para("Pourquoi tant d'attente ? Parce que les grands jeux sont rares, et parce que chaque bande-annonce devient un événement mondial, regardé des centaines de millions de fois. En attendant la sortie, les fans imaginent, dessinent et discutent. L'attente, elle aussi, fait partie du jeu.")
f.gloss('un jeu vidéo 비디오 게임 · une bande-annonce 예고편 · un monde ouvert 오픈 월드 · une console 게임기 · la sortie (게임) 출시 · un loisir 여가.')
f.head('À VOUS !　바로 연습', 25)
f.expl('5면 기사를 읽고 정답을 고르세요.')
f.ex("B1", '객관식', "B", 'GTA는 거대한 오픈 월드 도시로 유명해요',
     "La série GTA est célèbre pour... A. ses petites villes · B. ses mondes ouverts · C. ses jeux de cartes")
f.ex("B1", '객관식', "B", '본문: des millions de personnes jouent',
     "En France, le jeu vidéo concerne... A. seulement les enfants · B. des millions de personnes · C. personne")
f.ex("B1", '객관식', "B", '예고편은 세계적 이벤트예요',
     "Chaque bande-annonce devient... A. un secret · B. un événement mondial · C. un examen")
f.ex("B1", '객관식', "A", '기다림 자체도 게임의 일부예요',
     "Pour les fans, l'attente... A. fait partie du jeu · B. est interdite · C. est terminée")
f.head("LE FRANÇAIS FAIT SON SHOW", 24)
f.para("Cette semaine, sur les réseaux sociaux, le français devient une star. Des vidéos comiques transforment la langue en personnage : « le français » arrive comme une vedette difficile — il a des règles partout, des exceptions, et il refuse de se prononcer comme il s'écrit ! Les apprenants se reconnaissent et rient : oui, c'est exactement ça.", 23.5)
f.para("Autre tendance : la lecture « chic ». Des photos esthétiques montrent des lecteurs avec des livres français — un café, une bougie, un roman ouvert. Le message : lire en français, c'est beau, c'est chic. Sous les photos, les commentaires demandent : « Quel livre pour commencer ? »", 23.5)
f.para("Réponse des professeurs et des libraires : des listes de livres par niveau. A2 pour débuter doucement, B1 pour les lecteurs courageux, B2 pour les passionnés. Lire un vrai livre, même lentement, même avec un dictionnaire : c'est la méthode que ce journal défend chaque semaine.", 23.5)
f.expl('virale / partager / abonnés / commentaire로 빈칸을 채우세요.')
f.ex("B1", '문장 완성', "virale", 'vidéo virale 입소문 영상',
     "Une vidéo ___ est vue par des millions de personnes.")
f.ex("B1", '문장 완성', "partager", 'partager = 공유하다',
     "Clique sur le bouton pour ___ la photo avec tes amis.")
f.ex("B1", '문장 완성', "abonnés", 'des abonnés 구독자, 팔로워',
     "Elle a 10 000 ___ sur son compte.")
f.ex("B1", '문장 완성', "commentaire", 'un commentaire 댓글 하나',
     "Écris un ___ sous la vidéo !")
f.expl('문장을 완성하며 내 생각을 표현하세요 (예시 답안은 8면).')
f.ex("B1", '문장 완성', 'ex. : amusant, parce que les enfants adorent se déguiser (예시 답안)', '열린 문제, 말이 되면 돼요',
     "À mon avis, Halloween en France, c'est ___ parce que ___.")
f.ex("B1", '문장 완성', "ex. : j'aime les histoires et les mots nouveaux (예시 답안)", '열린 문제, 말이 되면 돼요',
     "Je lis en français parce que ___.")
f.ex("B2", '문장 완성', 'ex. : ce ne sont pas les résultats (예시 답안)', '열린 문제, 말이 되면 돼요',
     "Les sondages sont utiles, mais ___.")
f.expl('바로 연습 · 소셜 화제 작은 문제.')
f.ex("B1", '문장 완성', "personnage", '언어가 하나의 인물이 돼요',
     "Dans les vidéos comiques, le français devient un ___.")
f.ex("A2", '문장 완성', "chic", "lire en français, c'est chic",
     "Lire en français, c'est ___ : c'est la tendance du moment.")
f.ex("A2", '문장 완성', "niveau", 'des listes par niveau 수준별 목록',
     "Les professeurs proposent des listes de livres par ___.")
f.ex("B1", '문장 완성', "dictionnaire", "même avec un dictionnaire",
     "On peut lire un vrai livre, même avec un ___.")
f.ex("B2", '문장 완성', "reconnaissent", 'se reconnaître 그 속에서 자신을 보다',
     "Les apprenants se ___ dans ces vidéos : c'est exactement eux !")
f.ex("B1", '문장 완성', "esthétique", 'une photo esthétique 감성 사진',
     "Une photo ___ montre un café, une bougie, un roman ouvert.")
f.head("LIRE OU JOUER ? LES DEUX !", 24)
f.para("Faut-il choisir entre les écrans et les livres ? Pas forcément. Beaucoup de joueurs deviennent lecteurs : les jeux racontent des histoires, donnent envie de lire les romans, les bandes dessinées et les guides qui les entourent. Et beaucoup de lecteurs jouent : un livre le matin, une partie le soir.", 23.5)
f.para("La bonne question n'est donc pas « écran ou livre ? », mais « quoi, sur l'écran ? ». Un texte long, une vraie histoire, un article comme celui-ci : l'écran peut aussi être une page. C'est le pari de ce journal, que vous lisez peut-être... sur un écran.", 23.5)
f.box("PETIT LEXIQUE DU JEU", [
    ('un niveau — 레벨, 단계 · sauvegarder — 저장하다 · un défi — 도전', "serif", False, INK, 21.5, 1.42),
    ('perdre / gagner une partie — 한 판 지다 / 이기다', "serif", False, INK, 21.5, 1.42),
])
f.end_report()

# col 3 boxes
ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX)
p.text(ix + 22, 240, 'LES MOTS DES ÉCRANS　화면 단어장', 23, "sans", True, OLIVE)
mots5 = [
    'un écran — 화면', 'un réseau social — 소셜 네트워크', 'viral — 입소문이 난',
    'un abonné — 구독자, 팔로워', 'partager — 공유하다', 'un commentaire — 댓글',
    'en ligne — 온라인', 'un joueur — 플레이어', 'attendre — 기다리다',
    'une sortie — 출시, 개봉',
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
p.para(ix + 22, qy5 + 322, '여러분이 처음 읽은 프랑스어 책은 무엇인가요? 댓글로 알려 주세요.', 20, "sans", False, GREY, CW - 44, 1.4)
dy5 = qy5 + 400 + 26
p.rect(ix, dy5, CW, 440, fill=BOX)
p.text(ix + 22, dy5 + 40, 'LE DÉBAT　화면 시간', 23, "sans", True, OLIVE)
p.para(ix + 22, dy5 + 78, "Combien d'heures par jour devant un écran ? Pour jouer, regarder, lire... Les écrans sont-ils des ennemis des livres, ou une autre porte pour entrer dans la langue ?", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 240, "Petit test de la rédaction : ce soir, remplacez trente minutes d'écran par trente minutes de lecture — et racontez-nous la différence (page 8).", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, dy5 + 372, '오늘 밤 이렇게 해 보세요: 화면은 30분 줄이고 책은 30분 더 읽기.', 20, "sans", False, GREY, CW - 44, 1.4)
sy5 = dy5 + 440 + 26
p.text(ix, sy5 + 24, "LE SONDAGE DE LA RÉDACTION", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, sy5 + 38, OLIVE, 2)
p.para(ix, sy5 + 76, "Quel jeu attendez-vous le plus ? Quel livre français lisez-vous en ce moment ? Répondez dans les commentaires : résultats dans le prochain numéro.", 21.5, "serif", False, INK, CW, 1.42)
p.para(ix, sy5 + 210, '편집부 작은 설문: 어떤 게임을 기다리나요? 어떤 프랑스어 책을 읽고 있나요?', 20, "sans", False, GREY, CW, 1.4)
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
p.band('POLITIQUE & CHIFFRES　시사', "Le Lucerna", 'NIVEAU B2　Présidentielle 2027　대선 심층 읽기')

f = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1420, tag="P6-deep")
f.title("Présidentielle 2027 : comprendre l'élection et ses chiffres", 32)
f.byline("Par la rédaction　Niveau de lecture : B2")
f.para("En avril 2027, les Français éliront leur président — ou leur présidente. Le président est élu pour cinq ans, au suffrage universel direct : chaque citoyen de 18 ans et plus peut voter. L'élection se déroule en deux tours. Au premier tour, tous les candidats sont en compétition. Si personne n'obtient plus de 50 % des voix, un second tour oppose, deux semaines plus tard, les deux candidats arrivés en tête.")
f.para("À six mois du scrutin, la bataille des chiffres a commencé. Les instituts publient régulièrement des « intentions de vote » : si l'élection avait lieu dimanche, pour qui voteriez-vous ? Ces enquêtes ne prédisent pas le résultat — elles photographient l'opinion à un moment donné. Un écart de deux points peut tenir à la marge d'erreur.")
f.para("Lire un sondage, c'est déjà faire de la politique : qui devance qui ? Qui gagne des points, qui en perd ? Le vocabulaire des comparaisons envahit les titres des journaux : « X creuse l'écart », « Y passe devant », « Z stagne ». Pour les apprenants de français, c'est un terrain d'entraînement idéal : les chiffres, les pourcentages et le comparatif y sont partout.")
f.para("La campagne, elle, ne fait que commencer : les partis choisissent leurs candidats, les programmes se préparent. Une chose est sûre : jusqu'en 2027, les sondages rythmeront la vie politique française — cette semaine, ils sont la recherche numéro un du pays sur Google.")
f.gloss("un scrutin 투표, 선거 · une marge d'erreur 오차 범위 · creuser l'écart 격차를 벌리다 · devancer 추월하다 · rythmer 리듬을 정하다.")
f.end_report()

# practice poll chart, span cols 0-1
chx, chw = MX, 896
chy = 1470
p.rect(chx, chy, chw, 470, fill=BOX)
p.text(chx + 24, chy + 42, "SONDAGE D'ENTRAÎNEMENT　연습 여론조사 도표", 25, "sans", True, OLIVE)
p.text(chx + 24, chy + 74, "Données simplifiées pour l'exercice — aucun institut, aucun vrai candidat.", 19.5, "sans", False, OLIVE)
p.text(chx + 24, chy + 100, '이 도표는 연습용 자료로, 실제 여론조사 기관이나 후보자와 관계없어요.', 19, "sans", False, GREY)
bars = [("Candidat A", 28, OLIVE), ("Candidate B", 24, OLIVE), ("Candidat C", 17, OLIVE),
        ("Candidat D", 11, OLIVE), ("Autres", 9, OLIVE), ("Indécis", 11, "#8a8168")]
byy = chy + 128
for lab, val, col in bars:
    p.text(chx + 24, byy + 26, lab, 22, "serif", True, INK)
    p.rect(chx + 200, byy + 6, val * 18, 26, fill=col)
    p.text(chx + 212 + val * 18, byy + 27, f"{val} %", 22, "sans", True, OLIVE)
    byy += 52

e6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 1990, 2560, tag="P6-chart-ex")
e6.head('LIRE LE GRAPHIQUE　도표 읽기', 25)
e6.expl('위 연습 여론조사 도표를 보고 답하세요.')
e6.ex("B2", '도표 읽기', "Le candidat A, avec 28 %", 'A가 28%로 선두',
      "Qui est en tête du sondage ?", size=23)
e6.ex("B2", '도표 읽기', "4 points", '28 − 24 = 4%포인트',
      "Combien de points séparent le candidat A de la candidate B ?", size=23)
e6.ex("B2", '도표 읽기', "Faux", '17%는 11%의 두 배가 아니에요',
      "Vrai ou faux : le candidat C a deux fois plus de voix que le candidat D.", size=23)
e6.ex("B2", '도표 읽기', "11 %", 'Indécis (미결정) = 11 %',
      "Quel est le pourcentage des indécis ?", size=23)
e6.ex("B2", '도표 읽기', "La candidate B (27 % contre 26 %)", 'B+3=27, A−2=26이라 B가 추월해요',
      "Si B gagne 3 points et A en perd 2, qui passe devant ?", size=23)
e6.ex("B2", '도표 읽기', "Oui, 52 %", '28 + 24 = 52%로 과반을 넘어요',
      "Les candidats A et B, ensemble, dépassent-ils 50 % ?", size=23)
e6.end_report()

# right half, col 2: vocab box + comparatif + vocab MCQ + headline phrases
g = Flow(p, [(COLX[2], CW)], 200, 2560, tag="P6-right2")
g.box('LES MOTS DU SCRUTIN　선거 단어장', [
    ('un sondage — 여론조사 · une intention de vote — 투표 의향', "serif", False, INK, 21.5, 1.42),
    ("devancer — 추월하다 · creuser l'écart — 격차를 벌리다", "serif", False, INK, 21.5, 1.42),
    ('stagner — 정체하다 · un échantillon — 표본', "serif", False, INK, 21.5, 1.42),
    ('un parti — 정당 · se qualifier — 다음 단계에 진출하다', "serif", False, INK, 21.5, 1.42),
])
g.head("LE COMPARATIF EN CAMPAGNE", 25)
g.expl('비교급으로 문장을 완성하세요.')
g.ex("B2", '문장 완성', "plus populaire", "A 28 % > B 24 %",
     "Dans ce sondage, A est ___ (populaire) que B.", size=23)
g.ex("B2", '문장 완성', "moins", 'D 11% < C 17%라 moins de를 써요',
     "D obtient ___ de voix que C.", size=23)
g.ex("B2", '문장 완성', "aussi", '11% = 11%로 같으니 aussi를 써요',
     "Les indécis sont ___ nombreux que les partisans de D.", size=23)
g.ex("B2", '문장 완성', "meilleur", 'bon의 비교급은 meilleur예요',
     "Ce sondage est ___ (bon) que le précédent : l'échantillon est plus grand.", size=23)
g.head('LES MOTS　단어', 25)
g.expl('올바른 뜻을 고르세요.')
g.ex("B2", '객관식', "B", 'devancer = 앞서다, 추월하다',
     "« Devancer » signifie... A. arriver après · B. passer devant · C. abandonner", size=23)
g.ex("B2", '객관식', "C", 'un scrutin = 투표 한 번',
     "Un « scrutin » est... A. un débat · B. un parti politique · C. un vote", size=23)
g.ex("B2", '객관식', "A", '오차 범위는 숫자에만 관계해요',
     "La « marge d'erreur » concerne... A. les chiffres du sondage · B. le prix du journal · C. l'heure du vote", size=23)
g.ex("B2", '객관식', "B", 'être en tête = 1위에 있다',
     "« Être en tête » veut dire... A. réfléchir · B. être le premier · C. être fatigué", size=23)
g.box("LES PHRASES DES JOURNAUX", [
    ("« X creuse l'écart. » — X가 격차를 벌려요.", "serif", False, INK, 21.5, 1.42),
    ('« Y passe devant. » — Y가 앞으로 치고 나가요.', "serif", False, INK, 21.5, 1.42),
    ('« Z en chute libre. » — Z의 지지율이 곤두박질쳐요.', "serif", False, INK, 21.5, 1.42),
    ('« W crée la surprise. » — W가 이변을 만들어요.', "serif", False, INK, 21.5, 1.42),
])
g.end_report()

# right half, col 3: micro-drills + history box + big number + débat
g2 = Flow(p, [(COLX[3], CW)], 200, 2560, tag="P6-right3")
g2.head('MICRO-DRILLS　바로 연습', 25)
g2.expl('선거 상식 표현을 완성하세요.')
g2.ex("B2", '문장 완성', "universel", 'suffrage universel 보통 직접 선거',
      "Le président est élu au suffrage ___ direct.", size=23)
g2.ex("B2", '문장 완성', "second", 'le second tour 결선 투표',
      "Si personne n'a plus de 50 %, il y a un ___ tour.", size=23)
g2.ex("B2", '문장 완성', "erreur", "la marge d'erreur 오차 범위",
      "Un petit écart peut tenir à la marge d'___.", size=23)
g2.ex("B1", '문장 완성', "dix-huit", '18세부터 투표할 수 있어요',
      "En France, on vote à partir de ___ ans.", size=23)
g2.box("TROIS DATES POUR COMPRENDRE", [
    ("1962 — le président est élu directement par les citoyens.", "serif", False, INK, 21.5, 1.42),
    ("1974 — on peut voter dès 18 ans.", "serif", False, INK, 21.5, 1.42),
    ("2000 — le mandat passe de sept ans à cinq ans : c'est le quinquennat.", "serif", False, INK, 21.5, 1.42),
    ('세 번의 개혁이 오늘의 프랑스 대선을 만들었어요.', "sans", False, GREY, 20, 1.4),
])
g2.head("LE CHIFFRE DE LA SEMAINE", 25)
g2.para("5 000 +", 54, "serif", True, OLIVE, 1.1, 4)
g2.para("C'est le nombre de recherches quotidiennes, en France, pour « sondage présidentielle 2027 » — la recherche numéro un du pays cette semaine (Google Trends).", 22)
g2.head('LE DÉBAT　토론', 25)
g2.para("Les sondages influencent-ils le vote ? Certains disent oui : on aime voter pour le gagnant. D'autres disent non : les électeurs choisissent leurs idées, pas les chiffres. Et vous, qu'en pensez-vous ? Deux phrases, en français, dans les commentaires.", 22)
g2.expl('여론조사가 투표에 영향을 줄까요? 내 생각을 두 문장으로 써 보세요.')
g2.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
