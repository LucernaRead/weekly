# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band('CULTURE　문화', "Le Lucerna", 'NIVEAU A2 → B1　La Toussaint　모든 성인의 날')

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P3-main")
f.title("La Toussaint : le jour des fleurs et des souvenirs", 32)
f.byline("Par la rédaction　Niveau de lecture : A2 → B1")
f.para("Le 1er novembre, la France fête la Toussaint. À l'origine, c'est la fête de tous les saints. Aujourd'hui, pour beaucoup de familles, c'est surtout le jour du souvenir : on pense aux personnes mortes qu'on a aimées.")
f.para("Ce jour-là, les cimetières se remplissent de fleurs. La fleur de la Toussaint, c'est le chrysanthème. Les Français en achètent des millions : blancs, jaunes, violets... On les pose sur les tombes, on nettoie les pierres, et on reste un moment en silence avec la famille.")
f.para("Attention, voyageurs ! En France, le chrysanthème est la fleur des cimetières. On n'offre jamais de chrysanthèmes pour un anniversaire ou pour un dîner. Pour faire plaisir, choisissez des roses ou des tulipes !")
f.para("La Toussaint arrive pendant les vacances scolaires : les familles voyagent pour se retrouver. Le 1er novembre est un jour férié : les écoles, les bureaux et beaucoup de magasins sont fermés. Dans les villages comme dans les grandes villes, c'est un jour calme, doux et un peu mélancolique — le cœur de l'automne français.")
f.gloss("un cimetière 묘지 · une tombe 무덤 · un jour férié 공휴일 · le souvenir 추억, 기념 · mélancolique 우울한 · à l'origine 원래, 처음에는.")
f.head('À VOUS !　바로 연습', 25)
f.expl('맞는지 틀리는지 판단하세요 (Vrai / Faux).')
f.ex("A2", '읽기 판단', "Faux", '모든 성인의 날은 11월 1일, 10월 31일이 아니에요',
     "La Toussaint est le 31 octobre.", instr="Vrai ou faux ?")
f.ex("A2", '읽기 판단', "Vrai", '본문: les cimetières se remplissent de fleurs',
     "Le 1er novembre, les cimetières sont pleins de fleurs.", instr="Vrai ou faux ?")
f.ex("A2", '읽기 판단', "Faux", '국화는 프랑스에서 성묘용 꽃이라 선물하면 안 돼요',
     "On offre des chrysanthèmes pour un anniversaire.", instr="Vrai ou faux ?")
f.ex("B1", '읽기 판단', "Faux", '11월 1일은 jour férié라 학교가 쉬어요',
     "Le 1er novembre, les écoles sont ouvertes.", instr="Vrai ou faux ?")
f.ex("B1", '읽기 판단', "Faux", '본문의 la fête divise처럼 의견이 갈려요',
     "Tous les Français adorent Halloween.", instr="Vrai ou faux ?")
f.expl('cimetière / tombe / déguisement / citrouille로 빈칸을 채우세요.')
f.ex("B1", '문장 완성', "déguisement", 'Halloween에는 분장 의상을 입어요',
     "Pour Halloween, les enfants portent un ___.")
f.ex("A2", '문장 완성', "tombe", '꽃은 묘비 위에 올려요',
     "On pose les fleurs sur la ___.")
f.ex("A2", '문장 완성', "cimetière", '11월 1일 묘지는 꽃으로 가득해요',
     "Le ___ est plein de fleurs le 1er novembre.")
f.ex("B1", '문장 완성', "citrouille", '호박은 Halloween의 상징',
     "Une ___ orange est le symbole d'Halloween.")
f.expl('ne...jamais / ne...plus / ne...pas를 써서 문장을 바꿔 쓰세요.')
f.ex("B1", '문장 바꾸기', "On n'offre jamais de chrysanthèmes pour un anniversaire.", 'jamais + de (관사 변화 없음)',
     "(jamais) On offre des chrysanthèmes pour un anniversaire. → ___", instr='바꿔 쓰기')
f.ex("B1", '문장 바꾸기', "Les feuilles ne sont plus vertes en automne.", 'ne...plus = 더 이상 ~않다',
     "(plus) Les feuilles sont vertes en automne. → ___", instr='바꿔 쓰기')
f.ex("B1", '문장 바꾸기', "Le 1er novembre n'est pas un jour de travail pour tous.", "n'est pas = ~가 아니다",
     "(pas) Le 1er novembre est un jour de travail pour tous. → ___", instr='바꿔 쓰기')
f.head("HALLOWEEN : LA FÊTE QUI DIVISE", 25)
f.para("Le 31 octobre, c'est Halloween. Les enfants se déguisent — sorcières, fantômes, super-héros — et ils frappent aux portes : « Des bonbons ou un sort ! » On leur donne des bonbons, et tout le monde rit.", 23.5)
f.para("En France, la fête vient des États-Unis. Certains l'adorent : c'est joyeux, coloré, parfait pour les enfants. D'autres disent : « Ce n'est pas notre tradition, c'est du commerce. » Mais dans les écoles et les villages, les citrouilles orange sont de plus en plus nombreuses. Cette année, Halloween tombe un samedi, pendant les vacances : les familles auront le temps de préparer la fête. Et vous, pour ou contre ?", 23.5)
f.expl('바로 연습 · Halloween 작은 문제.')
f.ex("A2", '문장 완성', "sort", '« Des bonbons ou un sort ! » 사탕을 안 주면 장난칠 거예요',
     "« Des bonbons ou un ___ ! » crient les enfants.")
f.ex("B1", '문장 완성', "déguisent", 'se déguiser 분장하다, ils형',
     "Les enfants se ___ en sorcières et en fantômes.")
f.ex("A2", '문장 완성', "bonbons", '아이들이 달라는 것은 사탕',
     "On frappe à la porte et on demande des ___.")
f.ex("A2", '문장 완성', "États-Unis", 'Halloween은 미국에서 왔어요 (본문)',
     "En France, la fête d'Halloween vient des ___.")
f.ex("B1", '객관식', "B", 'diviser = 의견이 갈리다',
     "« La fête divise » signifie... A. tout le monde est d'accord · B. les avis sont partagés · C. personne ne vient")
f.ex("B1", '문장 완성', "déguisements", '사탕과 분장 의상을 사요',
     "Pour la fête, on achète des bonbons et des ___.")
f.head("LA TOUSSAINT DANS LE MONDE", 25)
f.para("Le 1er novembre n'est pas férié qu'en France : la Belgique fête aussi la Toussaint, et les familles y visitent les cimetières avec des chrysanthèmes. Le mot « Toussaint » signifie « tous les saints » : la fête honore tous les saints, connus et inconnus.", 23.5)
f.para("Le 2 novembre, au Mexique, c'est le Día de los Muertos, le Jour des Morts : les familles préparent des autels avec des photos, des fleurs orange et les plats préférés des disparus. L'ambiance est très différente : musique, couleurs et fête — mais l'idée est la même : ne pas oublier ceux qu'on aime.", 23.5)
f.para("Et le 31 octobre au soir, pendant que les enfants français demandent des bonbons, beaucoup de familles pensent déjà au lendemain : acheter les fleurs, préparer le voyage, téléphoner aux grands-parents. L'automne est la saison du souvenir — et des retrouvailles.", 23.5)
f.expl('해설 — un autel 제단 · un disparu 고인 · les retrouvailles 재회.')
f.box("LE MOT DE LA PAGE", [
    ("« chrysanthème » vient du grec : chrysos (l'or) + anthemon (la fleur) — la « fleur d'or ».", "serif", False, INK, 22, 1.42),
    ('국화: 이름 속에 금을 품은 꽃.', "sans", False, GREY, 20, 1.4),
])
f.end_report()

# col 3: image + boxes
ix = COLX[3]
image(p, "chrysanthemum-blanco.jpg", ix, 200, CW, 540)
cy3 = caption(p, ix, 740, CW,
              "Le chrysanthème, fleur du souvenir en France : on le pose sur les tombes, on ne l'offre jamais en cadeau.",
              "Planche botanique, Flora de Filipinas (Blanco), XIXe siècle, domaine public")
by3 = cy3 + 22
p.rect(ix, by3, CW, 452, fill=BOX)
p.text(ix + 22, by3 + 40, 'LES MOTS DES FÊTES　축제 단어장', 23, "sans", True, OLIVE)
mots = [
    'un saint — 성인', 'un cimetière — 묘지', 'une tombe — 무덤',
    'un jour férié — 공휴일', 'se souvenir — 기억하다, 추억하다',
    'un déguisement — 분장 의상', 'une citrouille — 호박',
    'un bonbon — 사탕', 'un fantôme — 유령', 'un sort — 마법, 저주',
]
yy3 = by3 + 82
for m in mots:
    p.text(ix + 22, yy3, m, 21.5, "serif", False, INK)
    yy3 += 37
zy3 = by3 + 452 + 26
p.rect(ix, zy3, CW, 476, fill="#f0eee5")
p.text(ix + 22, zy3 + 40, 'ZOOM　작가들의 묘지', 23, "sans", True, OLIVE)
p.para(ix + 22, zy3 + 78, "À Paris, le cimetière du Père-Lachaise est le plus visité du monde. On y trouve les tombes de Balzac, d'Oscar Wilde et de Marcel Proust. Le 1er novembre, des lecteurs y déposent des fleurs... et parfois un livre.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, zy3 + 340, '페르 라셰즈 묘지에는 발자크, 오스카 와일드, 프루스트가 잠들어 있어요. 책을 좋아하는 사람의 모든 성인의 날에는 작가에게 꽃 한 송이를 바치러 가 보세요.', 20, "sans", False, GREY, CW - 44, 1.4)
dy3 = zy3 + 476 + 26
p.rect(ix, dy3, CW, 330, fill=BOX)
p.text(ix + 22, dy3 + 40, 'DATES À RETENIR　이달의 일정', 23, "sans", True, OLIVE)
dates3 = [
    ("dim. 25 oct.", "changement d'heure !"),
    ("sam. 31 oct.", "Halloween"),
    ("dim. 1er nov.", "la Toussaint (jour férié)"),
    ("lun. 2 nov.", "reprise des cours"),
]
yy3 = dy3 + 84
for d, t in dates3:
    p.text(ix + 22, yy3, d, 19.5, "sans", True, OLIVE)
    p.text(ix + 168, yy3, t, 18.5, "serif", False, INK)
    yy3 += 42
p.para(ix + 22, yy3 + 20, '사흘의 일정이 이어져요: Halloween, 모든 성인의 날, 그리고 개학.', 19.5, "sans", False, GREY, CW - 44, 1.4)
py3 = dy3 + 330 + 30
p.text(ix, py3 + 24, "POUR OU CONTRE ?", 23, "sans", True, OLIVE)
p.hline(ix, ix + CW, py3 + 38, OLIVE, 2)
p.para(ix, py3 + 74, "Halloween en France : fête joyeuse ou commerce ? Écrivez votre avis en deux phrases (page 8).", 20.5, "serif", False, INK, CW, 1.4)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band('SPORT　스포츠', "Le Lucerna", "NIVEAU B1　NBA　Wembanyama")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P4-main")
f.title("Wemby : le géant français qui fait rêver la NBA", 32)
f.byline("Par la rédaction　Niveau de lecture : B1")
f.para("Il mesure 2,24 mètres. Il a de très longs bras. Et cette semaine, son équipe est dans les recherches Google de toute la France : les Spurs de San Antonio contre Oklahoma City. Le nom du phénomène : Victor Wembanyama, dit « Wemby ».")
f.para("Né au Chesnay, près de Paris, Victor commence le sport enfant : d'abord le football — il est gardien de but ! — et le judo. Puis le basket arrive, et tout change. À 19 ans, il devient le numéro un de la draft NBA : les Spurs le choisissent en premier. C'est un événement historique pour le basket français.")
f.para("Pourquoi tout le monde le regarde ? Parce qu'il joue comme personne : très grand, mais rapide et précis. Il bloque les tirs des adversaires et il marque de loin, avec facilité. Certains commentateurs l'appellent « l'extraterrestre » : sur le terrain, il semble venir d'une autre planète.")
f.para("La France a déjà eu une star en NBA : Tony Parker, quatre fois champion avec San Antonio. Aujourd'hui, Parker regarde les matchs de Wemby comme un grand frère. Entre les deux hommes, une même adresse : San Antonio, une ville devenue un peu française.")
f.para("La saison NBA commence en automne. En France, beaucoup de jeunes se lèvent la nuit pour regarder les matchs en direct. C'est dur pour le réveil du matin... mais quand Wemby joue, le spectacle vaut le voyage.")
f.gloss('un géant 거인 · la draft (NBA) 드래프트 · un tir 슛 · bloquer 블록하다 · un gardien de but 골키퍼 · précis 정확한 · en direct 생중계.')
f.head('À VOUS !　바로 연습', 25)
f.expl('4면 기사를 읽고 정답을 고르세요.')
f.ex("B1", '객관식', "B", '본문: Il mesure 2,24 mètres',
     "Victor Wembanyama mesure... A. 2,04 m · B. 2,24 m · C. 2,40 m")
f.ex("B1", '객관식', "A", '어릴 때 축구와 유도를 했어요',
     "Enfant, Victor fait aussi... A. du judo · B. du tennis · C. de la danse")
f.ex("B1", '객관식', "C", '19세에 드래프트 1순위가 됐어요',
     "Il devient numéro un de la draft à... A. 17 ans · B. 21 ans · C. 19 ans")
f.ex("B1", '객관식', "C", 'Parker는 NBA 우승 4회',
     "Tony Parker a gagné... A. deux titres · B. trois titres · C. quatre titres")
f.ex("B1", '객관식', "B", '시차 때문에 프랑스 팬은 한밤중에 일어나 생중계를 봐요',
     "Les fans français regardent les matchs... A. au petit déjeuner · B. la nuit · C. au bureau")
f.expl('스포츠 단어와 뜻을 짝지으세요.')
f.match_set("B1", '단어 짝짓기',
            ["marquer", "bloquer", "un entraînement", "la saison"],
            ["mettre le ballon dans le panier", "arrêter le tir de l'adversaire",
             "la séance où l'on répète les gestes", "la période des matchs dans l'année"],
            ["a", "b", "c", "d"],
            ['marquer=득점 a', 'bloquer=블록 b', 'entraînement=훈련 c', 'saison=시즌 d'],
            instr='짝짓기')
f.expl('비교급으로 문장을 완성하세요 (plus / moins).')
f.ex("B1", '문장 완성', "plus grand", "comparatif : grand → plus grand que",
     "Wemby est ___ (grand) que la plupart des joueurs.")
f.ex("B1", '문장 완성', "moins populaire", '프랑스 농구는 미국만큼 인기 있지 않아요',
     "Le basket est ___ (populaire) en France qu'aux États-Unis. (moins)")
f.ex("B1", '문장 완성', "plus fatigant", '한밤중에 경기를 보면 더 피곤해요',
     "Un match regardé la nuit est ___ (fatigant) qu'un match de jour.")
f.head("LE BASKET, SPORT FRANÇAIS ?", 25)
f.para("Le basket n'est pas né en France — il arrive des États-Unis à la fin du XIXe siècle — mais il y a trouvé une vraie maison. Des milliers de jeunes jouent en club, et l'équipe de France est l'une des meilleures d'Europe. Les matchs de l'équipe nationale remplissent les grandes salles, de Paris à Lille.", 23.5)
f.para("Avec Wembanyama, une nouvelle génération découvre le championnat américain. Les professeurs de sport le racontent : depuis l'arrivée de « Wemby » en NBA, les inscriptions des adolescents dans les clubs augmentent. Un géant de 2,24 mètres fait grandir tout un sport.", 23.5)
f.expl('해설 — une inscription 등록, 신청 · un championnat 선수권 대회, 리그 · une salle (스포츠) 체육관.')
f.para("À l'école aussi, le basket est partout : dans les cours de sport, sur les terrains des quartiers, et cette semaine dans les recherches Google des Français. La saison ne fait que commencer — la France continuera de se lever la nuit.", 23.5)
f.head("VOIR UN MATCH EN FRANÇAIS", 25)
f.para("Pour profiter d'un match avec les commentaires français, quelques phrases suffisent. Les commentateurs parlent vite, mais ils répètent souvent les mêmes expressions : écoutez, répétez, criez avec eux !", 23.5)
f.box("LES PHRASES DU COMMENTATEUR", [
    ('« Allez ! » — 힘내라! · « Quelle action ! » — 멋진 플레이!', "serif", False, INK, 21.5, 1.42),
    ("« Il marque ! » — 골을 넣었어요! · « C'est gagné ! » — 이겼어요!", "serif", False, INK, 21.5, 1.42),
    ('« Quelle ambiance dans la salle ! » — 경기장 분위기가 뜨거워요!', "serif", False, INK, 21.5, 1.42),
])
f.para("Exercice d'écoute de la rédaction : regardez dix minutes de match en français et notez trois phrases nouvelles. La semaine prochaine, comparez vos listes en classe — ou envoyez-les à la rédaction (page 8).", 23.5)
f.head("LA NUIT DES MATCHS", 25)
f.para("Il y a un rituel, les soirs de match : on prépare un thé ou un chocolat, on ouvre un carnet, et on regarde le match en famille ou entre amis, parfois très tard. Le lendemain, à l'école ou au bureau, tout le monde raconte la même action — avec les mêmes mots français.", 23.5)
f.para("C'est aussi cela, apprendre une langue : partager des émotions avec des millions de personnes, au même moment, dans la même langue. Wemby joue à San Antonio, mais ses phrases voyagent jusqu'à Paris, Lyon et Dakar.", 23.5)
f.box("LE SAVIEZ-VOUS ?", [
    ("En France, beaucoup de clubs de basket accueillent les débutants toute l'année : la licence coûte souvent moins cher qu'un abonnement de streaming.", "serif", False, INK, 21.5, 1.42),
    ('다음 호 스포츠 면 예고: «내가 처음 본 프랑스어 해설 경기» 글을 모집해요. 두세 문장이면 돼요 (투고 방법은 8면).', "sans", False, GREY, 18.5, 1.4),
])
f.end_report()

# col 3: Parker + vocab + stats + micro-drills
ix = COLX[3]
p.rect(ix, 200, CW, 470, fill=BOX)
p.text(ix + 22, 240, "TONY PARKER, LE PIONNIER", 23, "sans", True, OLIVE)
p.para(ix + 22, 278, "Avant Wemby, il y a Tony Parker. Arrivé à San Antonio à 19 ans, il gagne quatre titres de champion NBA (2003, 2005, 2007, 2014). Aujourd'hui, il est président du club de l'ASVEL, à Villeurbanne, et il reste un modèle pour les jeunes joueurs français.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, 520, "Cette semaine, son nom est aussi dans les recherches Google : la France du basket a la mémoire longue.", 21.5, "serif", False, INK, CW - 44, 1.42)
vy = 696
p.rect(ix, vy, CW, 416, fill="#f0eee5")
p.text(ix + 22, vy + 40, 'LES MOTS DU SPORT　스포츠 단어장', 23, "sans", True, OLIVE)
mots4 = [
    'le basket — 농구', 'un match — 경기', 'un panier — 골대; 골',
    'un terrain — 경기장', 'un champion — 챔피언', "s'entraîner — 훈련하다",
    'un adversaire — 상대', 'un titre — 우승 타이틀',
]
yy4 = vy + 82
for m in mots4:
    p.text(ix + 22, yy4, m, 21.5, "serif", False, INK)
    yy4 += 37
sy4 = vy + 416 + 26
p.rect(ix, sy4, CW, 218, fill=BOX)
p.text(ix + 22, sy4 + 40, "WEMBY EN CHIFFRES", 23, "sans", True, OLIVE)
p.para(ix + 22, sy4 + 80, "2,24 m — sa taille · né en 2004 au Chesnay · n° 1 de la draft 2023 · son surnom : « Wemby ».", 21.5, "serif", False, INK, CW - 44, 1.42)
mf = Flow(p, [(ix, CW)], sy4 + 218 + 30, 2560, tag="P4-micro")
mf.head('MICRO-DRILLS　바로 연습', 24)
mf.expl('bloque / marque / gagnent / entraînent / gagné / saison으로 빈칸을 채우세요.')
mf.ex("B1", '문장 완성', "bloque", 'bloquer les tirs 슛을 막다',
      "Wemby ___ le tir de l'adversaire.", size=23)
mf.ex("B1", '문장 완성', "marque", 'marquer un panier 골을 넣다',
      "Il ___ un panier de très loin !", size=23)
mf.ex("B1", '문장 완성', "gagnent", "ils gagnent le match",
      "Les Spurs ___ le match 98 à 90.", size=23)
mf.ex("B1", '문장 완성', "entraînent", "s'entraîner 훈련하다 (ils형)",
      "Les joueurs s'___ tous les jours.", size=23)
mf.ex("B1", '문장 완성', "gagné", "passé composé : a gagné",
      "Parker a ___ quatre titres NBA.", size=23)
mf.ex("A2", '문장 완성', "saison", "la saison commence en automne",
      "La ___ NBA commence en automne.", size=23)
mf.end_report()
db4 = mf.y + 6
p.rect(ix, db4, CW, 2560 - db4, fill="#f0eee5")
p.text(ix + 22, db4 + 40, 'LE DÉBAT　토론', 23, "sans", True, OLIVE)
p.para(ix + 22, db4 + 78, "Se lever à 3 heures du matin pour un match : folie ou passion ? Discutez en classe : deux phrases pour, deux phrases contre.", 21.5, "serif", False, INK, CW - 44, 1.42)
p.para(ix + 22, db4 + 196, '새벽 세 시에 일어나 경기를 보는 것, 열정일까요 무리일까요? 찬성 두 문장, 반대 두 문장을 써 보세요.', 20, "sans", False, GREY, CW - 44, 1.4)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
