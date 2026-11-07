# -*- coding: utf-8 -*-
"""JA core (VOL.2, Chinese explanations) -> JA x FR edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets, never byte slicing),
and writes the edition build into this directory. Fix rounds edit THIS
file, then re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> French, per the W43 JA x FR shipped precedent
(files/weekly-report-ja-fr). Masthead geometry follows the W43 JA x FR
shipped SVG exactly (wordmark 248, edition 316, badge 356, tagline 390,
rules 406/413, dark band 424).
"""
import hashlib
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w45-ja-build")
EDITION = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w45-ja-fr")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

# (old, new) applied in order. Longer strings first where one contains another.
GLOBAL = [
    # --- output repoint ---
    ("weekly-report-w45-ja-core", "weekly-report-w45-ja-fr"),
    # --- registry type names / instructions (W43 JA x FR wording) ---
    ('instr="造句"', 'instr="Formez la phrase"'),
    ('instr="翻译"', 'instr="Traduisez"'),
    ('instr="写作"', 'instr="Rédaction"'),
    ('instr="判断"', 'instr="Vrai ou faux ?"'),
    ('instr="填空"', 'instr="Complétez"'),
    ('instr="把词和释义配对"', 'instr="Associez mot et définition"'),
    ('instr="把活动和地点·时间配对"', 'instr="Événement, lieu et date"'),
    ('"完形单选"', '"Texte à trous"'),
    ('"单选"', '"Choix multiple"'),
    ('"完成句子"', '"Compléter"'),
    ('"词汇配对"', '"Appariement"'),
    ('"造句"', '"Former une phrase"'),
    ('"判断对错"', '"Vrai ou faux"'),
    ('"翻译"', '"Traduction"'),
    ('"写作"', '"Rédaction"'),
    # --- shared furniture ---
    ('"あなたは？ · 说说你自己"', '"あなたは？ · À vous la parole"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Réponses page 8 · niveaux mélangés, cherchez par numéro"'),
]

# Answer-note Traductions. One French rendering per distinct core note;
# duplicates share the rendering (correct: same note -> same meaning).
NOTES = [
    ("文化日在11月3日（周二）", "La Journée de la culture, c'est le 3 novembre (mardi)"),
    ("读书周到11月9日（周一）", "La Semaine de la lecture dure jusqu'au 9 novembre (lundi)"),
    ("見頃＝最佳观赏期", "見頃 = le meilleur moment"),
    ("立冬＝冬天的开始", "立冬 = le début de l'hiver"),
    ("神户灯光秀从7日（周六）开始", "Les illuminations de Kobe commencent le 7 (samedi)"),
    ("文化日全国都有文化活动", "La Journée de la culture propose des événements culturels dans tout le pays"),
    ("立冬在11月7日（周六）", "立冬, c'est le 7 novembre (samedi)"),
    ("灯光秀在神户开始", "Les illuminations commencent à Kobe"),
    ("「ゆる」＝无理をしない", "「ゆる」 = ne pas se forcer"),
    ("鍋の食卓は去年の1.5倍", "Les dîners nabe : 1,5 fois plus que l'an dernier"),
    ("発表は10月21日", "L'annonce date du 21 octobre"),
    ("11月から1月まで気温は平年より高い",
     "Les températures sont au-dessus des moyennes de novembre à janvier"),
    ("服と食事の話題はnoteのまとめによるもの",
     "Les sujets mode et cuisine viennent de la synthèse note"),
    ("ゆる＝轻松、不勉强", "ゆる = détendu, sans se forcer"),
    ("蒸し器＝蒸笼", "蒸し器 = un panier vapeur"),
    ("整える＝调理、调养", "整える = mettre en ordre"),
    ("鍋＝一锅菜", "鍋 = un plat cuisiné dans un seul pot"),
    ("鍋の材料が1か月早く並んだ", "Les ingrédients pour nabe sont apparus un mois plus tôt"),
    ("気象庁の予報は10月20日", "Les prévisions de la JMA datent du 20 octobre"),
    ("サクサクdeコパンが1,300万食を超えた",
     "サクサクdeコパン a dépassé 13 millions de portions"),
    ("ゆる＝轻松 b", "ゆる = détendu b"),
    ("蒸し器＝蒸笼 a", "蒸し器 = panier vapeur a"),
    ("麻辣湯＝辛いスープ d", "麻辣湯 = soupe épicée d"),
    ("予報＝天気の予想 c", "予報 = prévisions météo c"),
    ("杉并的活动是家庭管弦乐队", "L'événement de Suginami est un orchestre familial"),
    ("传统工艺展在石川县立美术馆",
     "L'exposition d'artisanat : musée d'art d'Ishikawa"),
    ("传统工艺展到11月8日", "L'exposition dure jusqu'au 8 novembre"),
    # 2026-10-27 follow-up trap (JA x EN / JA x DE precedent): the BARE
    # note "工艺展到11月8日" (content34 P3 fill-in, P8 key 37) is a distinct
    # note argument from the suffixed "工艺展到11月8日（周日）" — without
    # this entry it leaked through verbatim as Chinese on P8 line 37.
    ("工艺展到11月8日", "L'exposition dure jusqu'au 8 novembre"),
    ("灯光秀在金泽城和兼六园", "Les illuminations : château de Kanazawa et Kenrokuen"),
    ("市場＝集市", "市場 = marché"),
    ("工芸＝工艺", "工芸 = artisanat"),
    ("陶器＝陶瓷", "陶器 = poterie"),
    ("工艺展到11月8日（周日）", "L'exposition dure jusqu'au 8 novembre (dimanche)"),    ("金箔＝金箔", "金箔 = feuille d'or"),
    ("主语＋时间", "sujet + temps"),
    ("地点＋で＋あります", "lieu + で + あります"),
    ("见たい＝想看", "見たい = vouloir voir"),
    ("和家人一起", "en famille"),
    ("文化の日＝11月3日 b", "文化の日 = 3 novembre b"),
    ("工芸展＝美術館 c", "工芸展 = musée c"),
    ("オーケストラ＝杉並 d", "オーケストラ = Suginami d"),
    ("ライトアップ＝金沢城 a", "ライトアップ = château de Kanazawa a"),
    ("第1战软银3-1胜DeNA", "Match 1 : SoftBank bat DeNA 3–1"),
    ("第2战逆转的是筒香的3分本垒打", "Le home run de 3 points de Tsutsugo a renversé le match 2"),
    ("2连胜开局的是软银", "SoftBank a commencé par deux victoires d'affilée"),
    ("2连胜开局的夺冠率是73%", "Mener 2–0, c'est gagner le titre dans 73 % des cas"),
    ("2024年夺冠的是DeNA", "DeNA a remporté le titre en 2024"),
    ("第1战软银得3分", "SoftBank a marqué 3 points au match 1"),
    ("第2战软银得4分", "SoftBank a marqué 4 points au match 2"),
    ("第1战打到延长11局", "Le match 1 est allé jusqu'à la 11e manche"),
    ("第2战打到延长10局", "Le match 2 est allé jusqu'à la 10e manche"),
    ("夺冠率73%", "Taux de titre : 73 %"),
    ("延長＝比赛延长", "延長 = le match qui se prolonge"),
    ("第1战观众33,388人", "Public du match 1 : 33 388"),
    ("第2战观众33,432人", "Public du match 2 : 33 432"),
    ("相川监督说「4场胜负之战」", "L'entraîneur Aikawa : un combat en quatre victoires"),
    ("第1戦は土よう日です", "Le match 1 avait lieu samedi"),
    ("ソフトバンクが2連勝しました", "SoftBank a gagné deux fois d'affilée"),
    ("第2戦も延長戦でした", "Le match 2 est aussi allé en manches supplémentaires"),
    ("2024年はDeNAが優勝しました", "DeNA a gagné en 2024"),
    ("万圣节在10月31日（周六）", "Halloween, c'était le 31 octobre (samedi)"),
    ("涩谷禁酒时间是18时到5时", "L'interdiction de boire à Shibuya : de 18 h à 5 h"),
    ("乱扔垃圾罚款2,000日元", "Jeter des déchets coûte 2 000 yens d'amende"),
    ("化妆活动在池袋", "Le festival de cosplay a lieu à Ikebukuro"),
    ("工艺展到11月8日（周日）", "L'exposition dure jusqu'au 8 novembre (dimanche)"),
    ("横滨中区民祭在11月8日（周日）", "Le festival de Naka a lieu le 8 novembre (dimanche)"),
    ("万圣节在10月31日", "Halloween, c'était le 31 octobre"),
    ("禁酒从18时开始", "L'interdiction commence à 18 h"),
    ("禁酒到早上5时", "L'interdiction court jusqu'à 5 h"),
    ("横滨祭典在11月8日", "Le festival de Yokohama a lieu le 8 novembre"),
    ("夜里路上不能喝酒", "Pas d'alcool dans la rue la nuit"),
    ("ゴミの罰金は今年6月からです", "L'amende pour déchets date de juin de cette année"),
    ("コスプレフェスは池袋です", "Le festival de cosplay a lieu à Ikebukuro"),
    ("ハロウィンは10月31日（土）", "Halloween, c'était le 31 octobre (samedi)"),
    ("飲むことができません＝不能喝", "飲むことができません = ne pas pouvoir boire"),
    ("守って、〜しましょう", "守って + 〜しましょう = respectez les règles, et…"),
    ("フェンスの中＝围栏里面", "フェンスの中 = à l'intérieur de la clôture"),
    ("活动从10月30日到11月1日", "Le festival a duré du 30 octobre au 1er novembre"),
    ("11月から1月まで気温は平年より高い",
     "Les températures sont au-dessus des moyennes de novembre à janvier"),
    ("雨が多いのは太平洋側", "Le côté Pacifique reçoit plus de pluie"),
    ("九州の旅の検索は去年のほぼ2倍",
     "Voyages à Kyushu : recherches presque doublées en un an"),
    ("1回の旅の予算は下がった", "Le budget par voyage a baissé"),
    ("鳴子峡の見頃は10月31日から11月8日の週末",
     "Les gorges de Naruko sont au plus beau le week-end du 31 octobre au 8 novembre"),
    ("图中最受欢迎的是近处的满足感", "La première réponse du graphique est la satisfaction de proximité"),
    ("近场满足感38%", "Satisfaction de proximité : 38 %"),
    ("温泉27%", "Sources chaudes : 27 %"),
    ("红叶21%与美食14%之差为7", "Feuilles 21 % moins gastronomie 14 % = 7"),
    ("38+27=65", "38 + 27 = 65"),
    ("四项合计100%", "Les quatre totalisent 100 %"),
    ("立冬在11月7日", "立冬, c'est le 7 novembre"),
    ("神户灯光秀到12月28日", "Les illuminations de Kobe durent jusqu'au 28 décembre"),
    ("九州旅行搜索约为去年的2倍",
     "Voyages à Kyushu : presque deux fois plus que l'an dernier"),
    ("气象厅预报在10月20日", "Les prévisions de la JMA datent du 20 octobre"),
    ("11月は平年より暖かい予報です", "Novembre s'annonce plus chaud que la moyenne"),
    ("九州の旅の検索は増えました", "Les recherches de voyages à Kyushu ont augmenté"),
    ("グラフは練習用データです", "Le graphique présente des données d'exercice"),
    ("读书周从10月27日（周二）开始", "La Semaine de la lecture commence le 27 octobre (mardi)"),
    ("读书周到11月9日", "La Semaine de la lecture dure jusqu'au 9 novembre"),
    ("口号是「静かだけど、冒険中。」", "Le slogan est 「静かだけど、冒険中。」"),
    ("图书馆活动有图书介绍", "Bibliothèque : des présentations de livres"),
    ("見頃＝红叶最美的时候", "見頃 = quand les feuilles sont les plus belles"),
    ("紅葉狩り＝去看红叶", "紅葉狩り = sortir voir les feuilles"),
    ("ライトアップ＝夜里用灯光照亮", "ライトアップ = illuminer la nuit"),
    ("落葉＝落叶", "落葉 = feuilles tombées"),
    ("1.5倍＝比去年多50%", "1.5倍 = 50 % de plus que l'an dernier"),
    ("73%≈4人中的3人", "73 % ≈ 3 sur 4"),
    ("サクサクdeコパンが1,300万食", "サクサクdeコパン a atteint 13 millions de portions"),
    ("日本大赛第1战在10月24日（周六）", "Le match 1 des Japan Series : le 24 octobre (samedi)"),
    ("第2战软银4-3获胜", "Match 2 : SoftBank gagne 4–3"),
    ("神户灯光秀从7日开始", "Les illuminations de Kobe commencent le 7"),
    ("2连胜开局的夺冠率73%", "Taux de titre pour un départ à 2–0 : 73 %"),
    ("气象厅预报气温高于往年", "Les prévisions de la JMA : plus chaud que la moyenne"),
    ("九州旅行搜索约为去年的2倍",
     "Voyages à Kyushu : presque deux fois plus que l'an dernier"),
    ("美香周二和家人去金泽", "Mardi, Mika va à Kanazawa avec sa famille"),
    ("在金泽看传统工艺展和灯光秀",
     "À Kanazawa : l'exposition d'artisanat et les illuminations"),
    ("周六和朋友去神户", "Samedi, elle va à Kobe avec des amis"),
    ("读书周想借2本书", "Elle veut emprunter 2 livres pour la Semaine de la lecture"),
    ("主语＋时间＋地点＋动词", "sujet + temps + lieu + verbe"),
    ("场所用「で」", "employez 「で」 pour le lieu"),
    ("2连胜开局", "commencer par deux victoires d'affilée"),
    ("見頃＝最佳观赏期 b", "見頃 = le meilleur moment b"),
    ("鍋＝一锅菜 d", "鍋 = plat en pot unique d"),
    ("落葉＝落叶 a", "落葉 = feuilles tombées a"),
    ("予算＝预算 c", "予算 = budget c"),
    ("見せてください＝请出示", "見せてください = veuillez montrer"),
    ("借りられます＝能借（可能形）", "借りられます = pouvoir emprunter (forme potentielle)"),
    ("读书周到11月9日（第7版）", "La Semaine de la lecture : jusqu'au 9 novembre (page 7)"),
    ("「紅葉の本」受欢迎", "「紅葉の本」 est populaire"),
    ("どういたしまして＝不客气", "どういたしまして = je vous en prie"),
    ("对照第3版", "Voir page 3"),
    ("对照第5版", "Voir page 5"),
    ("对照第7版", "Voir page 7"),
    ("对照第6版（神户的灯光秀）", "Voir page 6"),
]

# Per-file furniture / gloss / structural replacements.
PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Note — " + s,'),
        ('"Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · HEBDOMADAIRE JAPONAIS VOL.2 · TEXTE EN JAPONAIS · EXPLICATIONS EN FRANÇAIS"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} sur {total}"'),
    ],
    "content12.py": [
        # P1 masthead -> W43 JA x FR shipped geometry
        ('p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")',
         'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")'),
        ('p.text(975, 330, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEXTES EN JAPONAIS · EXPLICATIONS EN FRANÇAIS — L\'ÉDITION POUR LES LECTEURS FRANCOPHONES", 19, "sans", True, OLIVE, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Chaque semaine · 日本人が読んでいる日本語を読む"'),
        ('"周二是文化日"', '"Mardi, c\'est la Journée de la culture"'),
        ('"节日过后，红叶周末到来 · 详见第 3 版"',
         '"Après le jour férié, le week-end des érables arrive · Voir page 3"'),
        ('"トップニュース · 头条"', '"トップニュース · À la une"'),
        ('"祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。"',
         '"祝日 jour férié · 見頃 le meilleur moment · 暦 calendrier · お届けします vous apporter."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · En chiffres"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · À vous de jouer"'),
        ('"这四个话题，都是本期报纸的主题。"',
         '"Ces quatre sujets structurent ce numéro."'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Dates dans les articles ; chiffres approximatifs"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · Dans ce numéro"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Le mot de la semaine"'),
        ('"ゆる＝ 轻松、不勉强。"', '"ゆる = détendu, sans se forcer."'),
        ('"短いニュース · 快讯"', '"短いニュース · En bref"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quiz éclair"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lisez la une et choisissez · réponses page 8"'),
        # P2
        ('"レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月"',
         '"レベル A2 · ゆる整え食と暖かい11月 · Cuisine douce et un novembre doux"'),
        ('"蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。"',
         '"蒸す cuire à la vapeur · 並ぶ apparaître en rayon · 食卓 la table du dîner · 超える dépasser."'),
        ('"予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。"',
         '"予報 prévisions · 平年 une année moyenne · 季節風 vent saisonnier · 話題 sujet · 値上がり hausses de prix."'),
        ('"你呢？寒冷的日子想吃什么锅？写两句日语寄来。"',
         '"Et vous ? Par un jour froid, quel nabe aimeriez-vous manger ? Écrivez deux phrases en japonais et envoyez-les-nous."'),
        ('"季節のことば · 季节词语"', '"季節のことば · Les mots de saison"'),
        ('"ゆる整え食の4つの言葉 · 关于轻松食养的四个词"',
         '"ゆる整え食の4つの言葉 · Quatre mots pour une cuisine douce"'),
        ('"一锅菜"', '"un plat en pot unique"'),
        ('"蒸笼"', '"un panier vapeur"'),
        ('"轻松、不勉强"', '"détendu, sans se forcer"'),
        ('"调理、调养"', '"mettre le corps et l\'esprit en ordre"'),
        ('"練習 · 第 2 版练习"', '"練習 · Exercices · page 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 文化の日と金沢 · 文化日与金泽"',
         '"レベル A2→B1 · 文化の日と金沢 · La Journée de la culture et Kanazawa"'),
        ('"市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。"',
         '"市場 marché · 工芸 artisanat · 光 lumière · 楽しむ apprécier."'),
        ('"陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。"',
         '"陶器 poterie · 漆器 laque · 染物 textiles teints · 金箔 feuille d\'or."'),
        ('"你呢？文化日想去参加什么文化活动？写两句日语寄来。"',
         '"Et vous ? À quel événement culturel aimeriez-vous aller pour la Journée de la culture ? Écrivez deux phrases en japonais et envoyez-les-nous."'),
        ('"練習 · 第 3 版练习"', '"練習 · Exercices · page 3"'),
        ('"レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场"',
         '"レベル B1 · 日本シリーズ横浜の2試合 · Les Japan Series : deux matchs à Yokohama"'),
        ('"延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。"',
         '"延長 manches supplémentaires · 逆転 retournement · 同点 égalité · 優勝率 taux de titre."'),
        ('"総括 总结 · 締め切り 截稿 · 確認する 核实。"',
         '"総括 bilan · 締め切り date limite · 確認する vérifier."'),
        ('"日本シリーズの日程 · 大赛日程"', '"日本シリーズの日程 · Calendrier"'),
        ('"横浜の2試合の記録 · 横滨两场比赛的记录"',
         '"横浜の2試合の記録 · Les deux matchs de Yokohama, en chiffres"'),
        ('"練習 · 第 4 版练习"', '"練習 · Exercices · page 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Jeunesse"'),
        ('"レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典"',
         '"レベル B1 · ハロウィンと秋まつり · Halloween et fêtes d\'automne"'),
        ('"罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。"',
         '"罰金 amende · 像 statue · 仮装 déguisement · 守る respecter."'),
        ('"祭り 节日 · 週末 周末 · 話題 话题。"',
         '"祭り fête · 週末 week-end · 話題 sujet."'),
        ('"你呢？秋日祭典上想做什么？写两句日语寄来。"',
         '"Et vous ? Que voudriez-vous faire à une fête d\'automne ? Écrivez deux phrases en japonais et envoyez-les-nous."'),
        ('"練習 · 第 5 版练习"', '"練習 · Exercices · page 5"'),
        ('"レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行"',
         '"レベル B2 · 暖かい11月と秋の旅 · Un novembre doux et les voyages d\'automne"'),
        ('"予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。"',
         '"予算 budget · 満足 satisfaction · 観測 observation · 追いかける poursuivre."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Lire le graphique"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Données d\'exercice"'),
        ('"練習 · 第 6 版练习"', '"練習 · Exercices · page 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Langue"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Trois niveaux, trois thèmes"'),
        ('"読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。"',
         '"読書週間 Semaine de la lecture · 紹介 présentation · 読み聞かせ lecture à voix haute."'),
        ('"見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶"',
         '"見頃 le meilleur moment · 紅葉狩り sorties pour voir les feuilles · 落葉 feuilles tombées"'),
        ('"〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。"',
         '"〜倍 fois · 〜% pour cent · 〜万食 dizaines de milliers de portions."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Erreurs fréquentes"'),
        ('"有「昨日」时要用过去式。"', '"Avec 「昨日」, employez le passé."'),
        ('"动词名词化时要加「こと」。"',
         '"「こと」 nominalise le verbe."'),
        ('"地点用「か所」来数。"', '"Comptez les lieux avec 「か所」."'),
        ('"动作发生的场所用「で」。"',
         '"Employez 「で」 pour le lieu de l\'action."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Modèle de phrase"'),
        ('"句式拆解：轻松地调理身心。"',
         '"Décomposition : remettre doucement le corps et l\'esprit en ordre."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Le courrier des lecteurs"'),
        # Le courrier des lecteurs: coordinator ruling — the Japanese disclosure line
        # (ld) must NOT serve as the operative disclosure for French
        # readers, and the Chinese disclosure (lcn) is the core's
        # reader-native layer. Both are replaced by ONE French
        # disclosure stating the 3 facts + an explicit invitation.
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.3に載せます。"',
         'ld_fr = "Exemple de la rédaction, pas une vraie lettre. Aucune lettre, '
         'aucun meilleur texte de la page 8 avant la date limite : les deux '
         'paraîtront dans le VOL.3. Envoyez-nous votre lettre en japonais — '
         'les lettres choisies seront publiées dans le VOL.3 !"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_fr, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_fr, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Les phrases de la semaine (extraits mot pour mot de ce numéro)"'),
        ('"文化日是11月3日星期二。"', '"La Journée de la culture, c\'est mardi 3 novembre."'),
        ('"这是一个慢慢地、轻松调理的日本11月。"',
         '"C\'est un novembre japonais lent et doux."'),
        ('"所谓ゆる，就是不勉强、慢慢来的意思。"',
         '"ゆる veut dire ne pas se forcer, prendre son temps."'),
        ('"火锅食材提前一个月上架了。"',
         '"Les ingrédients pour nabe sont apparus en magasin un mois plus tôt."'),
        ('"可以同时欣赏传统工艺、红叶与灯光。"',
         '"On peut apprécier ensemble artisanat traditionnel, feuilles d\'automne et lumières."'),
        ('"软银以两连胜开局。"', '"SoftBank a commencé par deux victoires d\'affilée."'),
        ('"遵守规则，过一个快乐的万圣节吧。"',
         '"Respectez les règles et passez un joyeux Halloween."'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。"',
         '"Ceux qui vont voir les feuilles peuvent poursuivre la plus belle période du nord au sud."'),
        ('"第1面"', '"p. 1"'),
        ('"第2面"', '"p. 2"'),
        ('"第3面"', '"p. 3"'),
        ('"第4面"', '"p. 4"'),
        ('"第5面"', '"p. 5"'),
        ('"第6面"', '"p. 6"'),
        ('"来週 · 下期预告 (VOL.3)"', '"来週 · La semaine prochaine (VOL.3)"'),
    ],
    "content8.py": [
        ('"テストと答え · 练习与答案"', '"テストと答え · Test et réponses"'),
        # E zone re-aim JA<->ZH -> JA<->EN (W43 JA x FR pattern)
        ('"文化日是11月3日。"', '"La Journée de la culture, c\'est le 3 novembre."'),
        ('"乱扔垃圾，要罚2,000日元。"', '"Jeter des déchets coûte 2 000 yens d\'amende."'),
        ('"读书周从10月27日开始。→ ___"', '"La Semaine de la lecture commence le 27 octobre. → ___"'),
        ('"我想去神户看红叶灯光秀。→ ___"',
         '"Je veux aller à Kobe voir les illuminations des érables. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Exercice d\'écriture (pas de réponse unique) ; le modèle ({NCHARS} caractères) est ci-dessous."'),
        ('"（开放题，范文如下）"', '"(question ouverte — modèle ci-dessous)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Modèle dans la section H de cette page ({NCHARS} caractères)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Réponses — classées par page, cherchez le numéro"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Une courte explication en français pour chaque réponse · ✓ = exercice avec modèle"'),
        ('f"— 第{pg}面 —"', 'f"— Page {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-FR.pdf"'),
        ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-FR-web.pdf"'),
    ],
}


def apply_pairs(text, pairs, fname):
    seen = set()
    for old, new in pairs:
        if old in seen:
            continue
        seen.add(old)
        n = text.count(old)
        assert n >= 1, f"{fname}: replacement source missing: {old!r}"
        text = text.replace(old, new)
    return text


def apply_soft(text, pairs):
    seen = set()
    for old, new in pairs:
        if old in seen:
            continue
        seen.add(old)
        text = text.replace(old, new)
    return text


def apply_notes_scoped(text, note_map):
    """Replace note strings ONLY where they are note arguments.

    Bare substring replacement is FORBIDDEN for notes: several notes are
    prefixes/substrings of frozen Japanese stems and article sentences
    (e.g. note "2024年はDeNAが優勝しました" vs stem "...ました。";
    note "グラフは練習用データです" vs the frozen chart para), and a
    global replace corrupted frozen text in round 1. Two scoped sites:
    (a) the 4th quoted argument of any .ex(...) call;
    (b) a bracket-list line whose every string is a note (match_set notes
    lists; lefts/rights/keys lines never satisfy this).
    """
    def ex_sub(m):
        note = m.group(2)
        if note in note_map:
            return m.group(1) + note_map[note] + m.group(3)
        return m.group(0)
    text = re.sub(r'(\.ex\("[^"]*",\s*"[^"]*",\s*"[^"]*",\s*")([^"]*)(")',
                  ex_sub, text)

    def list_sub(m):
        inner = m.group(2)
        strs = re.findall(r'"([^"]*)"', inner)
        if strs and all(s in note_map for s in strs):
            out = inner
            for s in strs:
                out = out.replace('"%s"' % s, '"%s"' % note_map[s], 1)
            return m.group(1) + out + m.group(3)
        return m.group(0)
    text = re.sub(r'(?m)^(\s*\[)(.*)(\],\s*)$', list_sub, text)
    return text


def quoted_strings(text):
    return set(re.findall(r'"([^"]*)"', text))


def main():
    os.makedirs(EDITION, exist_ok=True)
    os.makedirs(os.path.join(EDITION, "svg"), exist_ok=True)
    # svglib: canonical JA build, copied verbatim, md5-verified, never edited.
    src_svg = os.path.join(CORE, "svglib.py")
    data = open(src_svg, "rb").read()
    assert hashlib.md5(data).hexdigest() == CANON_SVGLIB_MD5, "svglib md5 mismatch"
    shutil.copyfile(src_svg, os.path.join(HERE, "svglib.py"))
    # run.py: verbatim copy (one-process driver).
    shutil.copyfile(os.path.join(CORE, "run.py"), os.path.join(HERE, "run.py"))
    # assets: verbatim copies (images + credits).
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(CORE, "assets")):
        shutil.copyfile(os.path.join(CORE, "assets", f),
                        os.path.join(HERE, "assets", f))
    # NOTE replacements: dict (deduped). Order: NOTES scoped FIRST (note
    # arguments only), then structural PER_FILE, then GLOBAL types/instr.
    # PER_FILE after NOTES because PER_FILE owns whole lines that share
    # words with notes (e.g. the season-word tuple "一锅菜" vs note
    # "鍋＝一锅菜"); GLOBAL last because it owns the P8 Rédaction bridge's
    # neighbours only via PER_FILE lines.
    note_map = dict(NOTES)
    fnames = ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "render.py"]
    # Pre-audit: every GLOBAL source must occur in >=1 core file, and
    # every NOTE key must occur as an EXACT quoted string (a real note
    # argument, not a substring of a frozen sentence).
    core_texts = {f: open(os.path.join(CORE, f), encoding="utf-8").read()
                  for f in fnames}
    for old, _ in GLOBAL:
        assert any(old in t for t in core_texts.values()), \
            f"transform table source never occurs in core: {old!r}"
    core_quoted = set()
    for t in core_texts.values():
        core_quoted |= quoted_strings(t)
    for old in note_map:
        assert old in core_quoted, \
            f"note key never occurs as an exact quoted string: {old!r}"
    for fname in fnames:
        text = core_texts[fname]
        text = apply_notes_scoped(text, note_map)
        text = apply_pairs(text, PER_FILE.get(fname, []), fname)
        text = apply_soft(text, GLOBAL)
        open(os.path.join(HERE, fname), "w", encoding="utf-8").write(text)
        print("transformed", fname)
    # Post-audit: no GLOBAL source may survive as a substring, and no
    # NOTE key may survive as an exact quoted string (substrings inside
    # frozen stems, e.g. "...ました。" stems, legitimately remain).
    for fname in fnames:
        out = open(os.path.join(HERE, fname), encoding="utf-8").read()
        for old, _ in GLOBAL:
            assert old not in out, f"{fname}: un-replaced source remains: {old!r}"
        out_quoted = quoted_strings(out)
        for old in note_map:
            assert old not in out_quoted, \
                f"{fname}: un-replaced note remains: {old!r}"
    print("OUT dir:", EDITION)


if __name__ == "__main__":
    main()
