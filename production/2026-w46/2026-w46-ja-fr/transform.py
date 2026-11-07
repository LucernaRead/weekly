# -*- coding: utf-8 -*-
"""JA core (VOL.3, Chinese explanations) -> JA x FR edition transform.

Re-runnable: reads the PRISTINE W46 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets), and writes the
edition build into this directory. Fix rounds edit THIS file, then
re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> French, per the W45 JA x FR shipped precedent.
Masthead geometry per the W46 task + tools/README lesson 20: wordmark
stays at the CORE position y=262, subtitle 316, badge inserted at
(975,356) 19pt BRICK, strapline 390, rules 406/413, dark band 424.
"""
import hashlib
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w46-ja-build")
EDITION = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w46-ja-fr")
CANON_SVGLIB_MD5 = "74177544422fe677639d769cd80499fb"

GLOBAL = [
    ("weekly-report-w46-ja-core", "weekly-report-w46-ja-fr"),
    ('instr="造句"', 'instr="Former une phrase"'),
    ('instr="翻译"', 'instr="Traduire"'),
    ('instr="写作"', 'instr="Rédaction"'),
    ('instr="判断"', 'instr="Vrai ou faux ?"'),
    ('instr="填空"', 'instr="Compléter"'),
    ('instr="把词和释义配对"', 'instr="Associer mots et sens"'),
    ('"完形单选"', '"texte à trous"'),
    ('"单选"', '"choix multiple"'),
    ('"完成句子"', '"à compléter"'),
    ('"词汇配对"', '"association"'),
    ('"造句"', '"construction de phrases"'),
    ('"判断对错"', '"vrai/faux"'),
    ('"翻译"', '"traduction"'),
    ('"写作"', '"rédaction"'),
    ('"あなたは？ · 说说你自己"', '"あなたは？ · À toi !"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Réponses page 8 · Niveaux mélangés — cherche ton numéro"'),
]

NOTES = [
    ("1111中有4个1", "1111 compte quatre 1"),
    ("1111看起来像4根细棒", "1111 ressemble à quatre bâtonnets fins"),
    ("11月中旬以后进入见赏期的地点多比往年稍晚", "Les lieux qui culminent après la mi-novembre sont le plus souvent en retard"),
    ("2026年没有三の酉", "Il n\'y a pas de San-no-tori en 2026"),
    ("3%≈100人中的3人", "3 %, c\'est environ 3 sur 100"),
    ("34+26=60", "34 + 26 = 60"),
    ("4连胜夺冠", "Quatre victoires d\'affilée ont apporté le titre"),
    ("4连胜＝4场比赛全胜", "gagner les quatre matchs"),
    ("71%的家庭接受祈祷", "71 % des familles reçoivent une prière"),
    ("74%的家庭在照相馆拍照", "74 % des familles font des photos en studio"),
    ("Weathernews的预报在10月29日（周四）", "La prévision Weathernews datait du 29 octobre (jeudi)"),
    ("「千歳飴」受欢迎", "千歳飴 est populaire"),
    ("お参りします＝去参拜", "お参りします = aller prier"),
    ("お参り＝去神社参拜", "お参り = aller prier au sanctuaire"),
    ("どういたしまして＝不客气", "どういたしまして = je vous en prie"),
    ("七五三是3岁5岁7岁孩子的庆祝活动", "Shichi-Go-San fête les enfants de 3, 5 et 7 ans"),
    ("七五三是3岁、5岁、7岁孩子的庆祝活动", "Shichi-Go-San fête les enfants de 3, 5 et 7 ans"),
    ("七五三的中心日在11月15日附近", "Shichi-Go-San se concentre autour du 15 novembre"),
    ("七五三的中心日是11月15日（周日）", "Shichi-Go-San se concentre le 15 novembre (dimanche)"),
    ("七五三的中心日是11月15日（第3版）", "Shichi-Go-San se concentre le 15 novembre (page 3)"),
    ("七五三的孩子去神社参拜", "Les enfants de Shichi-Go-San vont prier au sanctuaire"),
    ("七五三的照片是全家的回忆", "Les photos de Shichi-Go-San sont un souvenir de famille"),
    ("七五三＝孩子的庆祝活动", "七五三 = une fête pour les enfants"),
    ("七五三＝3岁5岁7岁孩子的庆祝 b", "七五三 = une fête pour les enfants de 3, 5 et 7 ans b"),
    ("东京的红叶在11月29日（周日）前后", "Les feuilles de Tokyo culminent vers le 29 novembre (dimanche)"),
    ("主语＋时间＋宾语＋动词", "sujet + temps + objet + verbe"),
    ("主语＋说明", "sujet + description"),
    ("九州场所在福冈国际中心举行", "Le tournoi de Kyushu a lieu au Fukuoka Kokusai Center"),
    ("二の酉在11月19日（周四）", "Ni-no-tori, c\'est le 19 novembre (jeudi)"),
    ("分ける＝分享", "分ける = partager"),
    ("前3场比赛连续打延长赛", "Les trois premiers matchs sont tous allés en prolongation"),
    ("前3场都是延长赛", "Les trois premiers matchs sont tous allés en prolongation"),
    ("千岁糖寄托长寿的愿望", "Chitose-ame porte un vœu de longue vie"),
    ("千岁糖是红白相间的长糖", "Chitose-ame est un long bonbon rouge et blanc"),
    ("千岁糖＝红白长糖", "long bonbon rouge et blanc"),
    ("千歳飴＝红白长糖 a", "千歳飴 = long bonbon rouge et blanc a"),
    ("千歳飴＝红白长糖 d", "千歳飴 = long bonbon rouge et blanc d"),
    ("口号是「静かだけど、冒険中。」", "Le slogan est 「静かだけど、冒険中。」"),
    ("周一读图书馆借的书", "Le lundi, il lit un livre de la bibliothèque"),
    ("周三和朋友分享波奇", "Le mercredi, il partage des Pocky avec des amis"),
    ("周五去高尾山看红叶", "Le vendredi, il va au mont Takao voir les feuilles"),
    ("周日和妹妹的七五三去神社", "Le dimanche, il va au sanctuaire pour le Shichi-Go-San de sa sœur"),
    ("四项合计100%", "Les quatre totalisent 100 %"),
    ("图表中最受欢迎的是山", "La montagne arrive en tête du graphique"),
    ("图表是真实调查结果", "Le graphique montre de vrais résultats d\'enquête"),
    ("在酉の市买熊手", "Acheter un kumade à Tori-no-ichi"),
    ("地点＋へ＋动词", "lieu + へ + verbe"),
    ("场所用「で」", "「で」 pour le lieu"),
    ("大阪的红叶在12月4日（周五）前后", "Les feuilles d\'Osaka culminent vers le 4 décembre (vendredi)"),
    ("宫岛的红叶从11月21日（周六）前后进入见赏期", "Les feuilles de Miyajima culminent à partir du 21 novembre (samedi)"),
    ("宾语＋动词", "objet + verbe"),
    ("对照第2版", "Voir page 2"),
    ("对照第3版", "Voir page 3"),
    ("对照第6版（追赶见赏期）", "Voir page 6 (à la poursuite de la meilleure saison)"),
    ("对照第7版", "Voir page 7"),
    ("山34%与神社26%之差为8", "Montagne 34 % moins sanctuaires 26 %, cela fait 8"),
    ("山占34%", "Montagne : 34 %"),
    ("岚山的红叶从11月23日（周一）前后进入见赏期", "Les feuilles d\'Arashiyama culminent à partir du 23 novembre (lundi)"),
    ("平成11年11月11日有6个1", "Le 11 novembre de l\'an Heisei 11 comptait six 1"),
    ("思い出＝回忆", "思い出 = un souvenir"),
    ("接戦＝比分接近的比赛", "接戦 = un match serré"),
    ("撮ります＝拍照", "撮ります = prendre une photo"),
    ("新小结是美ノ海", "Le nouveau komusubi est Umi-no-umi"),
    ("日本大赛第3战在10月27日（周二）", "Le match 3 des Japan Series a eu lieu le 27 octobre (mardi)"),
    ("晴れ着＝庆祝日穿的衣服", "晴れ着 = tenue de fête"),
    ("波奇日从1999年开始", "Le jour des Pocky a commencé en 1999"),
    ("波奇日只买不分享是错的", "Le jour des Pocky, ce n\'est pas que des achats"),
    ("波奇日在11月11日", "Le jour des Pocky, c\'est le 11 novembre"),
    ("波奇日在11月11日（周三）", "Le jour des Pocky, c\'est le 11 novembre (mercredi)"),
    ("波奇日定在11月11日因为细长的零食像数字1", "Le 11 novembre a été choisi car les snacks fins ressemblent au chiffre 1"),
    ("波奇日是11月11日", "Le jour des Pocky, c\'est le 11 novembre"),
    ("波奇日要和朋友分享零食", "Le jour des Pocky, on partage des snacks avec des amis"),
    ("波奇＝巧克力细饼干", "bâtonnet au chocolat"),
    ("ポッキー＝巧克力细饼干 d", "ポッキー = bâtonnet au chocolat d"),
    ("渡す＝递给", "渡す = tendre, donner"),
    ("照片长大后家人还会一起看", "La famille regarde encore les photos une fois les enfants grands"),
    ("照相馆拍照的家庭是71%", "Familles en studio photo : 71 %"),
    ("熊手＝祈求生意兴隆的竹耙", "熊手 = râteau porte-bonheur pour les affaires"),
    ("熊手＝竹耙吉祥物 b", "熊手 = râteau porte-bonheur b"),
    ("熊手＝竹耙吉祥物 c", "熊手 = râteau porte-bonheur c"),
    ("男孩在3岁和5岁庆祝，女孩在3岁和7岁", "Les garçons fêtent à 3 et 5 ans, les filles à 3 et 7 ans"),
    ("相扑场所到11月22日（周日）", "Le tournoi de sumo dure jusqu\'au 22 novembre (dimanche)"),
    ("神社占26%", "Sanctuaires : 26 %"),
    ("第3战在横滨举行", "Le match 3 s\'est joué à Yokohama"),
    ("第3战打到延长10局", "Le match 3 est allé jusqu\'à la 10e manche"),
    ("第3战的再见本垒打是正木打出的", "Masaki a frappé le coup de circuit décisif du match 3"),
    ("第3战软银2-1获胜", "Match 3 : SoftBank a gagné 2-1"),
    ("第3战软银得2分", "SoftBank a marqué 2 points au match 3"),
    ("第4战软银4-2获胜", "Match 4 : SoftBank a gagné 4-2"),
    ("第4战软银得4分", "SoftBank a marqué 4 points au match 4"),
    ("第5到第7战没有举行", "Les matchs 5 à 7 n\'ont pas eu lieu"),
    ("第5战也举行了", "Le match 5 a aussi eu lieu"),
    ("系列赛MVP是正木智也", "Le MVP de la série est Masaki Tomoya"),
    ("红叶见赏期从南向北移动是错的", "La saison des feuilles allant du sud au nord, c\'est faux"),
    ("细长的零食把人与人连接起来", "Les snacks fins relient les gens"),
    ("西宫神社每年5000组以上参拜", "Plus de 5 000 groupes par an visitent le sanctuaire Nishinomiya"),
    ("見頃＝最佳观赏期", "見頃 = le meilleur moment"),
    ("見頃＝最佳观赏期 c", "見頃 = le meilleur moment c"),
    ("读书周从10月27日（周二）开始", "La Semaine de la lecture a commencé le 27 octobre (mardi)"),
    ("读书周在11月9日（周一）结束", "La Semaine de la lecture se termine le 9 novembre (lundi)"),
    ("读书周结束后阅读习惯仍继续", "L\'habitude de lire continue après la Semaine de la lecture"),
    ("调查对象是200个七五三家庭", "L\'enquête couvrait 200 familles de Shichi-Go-San"),
    ("调查显示11月上旬参拜占26%", "Les visites début novembre étaient de 26 % dans l\'enquête"),
    ("调查显示71%的家庭在神社接受祈祷", "71 % des familles reçoivent une prière au sanctuaire, dit l\'enquête"),
    ("调查显示74%的家庭在照相馆拍照", "74 % des familles font des photos en studio, dit l\'enquête"),
    ("调查显示参拜最多的是11月上旬（26%）", "Les visites culminent début novembre (26 %), dit l\'enquête"),
    ("软银4连胜夺冠", "Quatre victoires d\'affilée pour le titre"),
    ("软银第13次夺冠", "Le 13e titre de SoftBank"),
    ("酉の市二の酉在11月19日（周四）", "Ni-no-tori de Tori-no-ichi, c\'est le 19 novembre (jeudi)"),
    ("酉の市＝11月酉日集市 a", "酉の市 = une foire les jours du coq en novembre a"),
    ("预报日期是见赏期开始的参考标准", "Les dates prévues marquent le début de la meilleure saison"),
    ("高尾山的红叶从11月13日（周五）前后进入见赏期", "Les feuilles du mont Takao culminent dès le 13 novembre (vendredi)"),
    ("高尾山的红叶从13日（周五）前后进入最佳观赏期", "Les feuilles du mont Takao culminent dès le 13 (vendredi)"),
    ("鸣子峡已经进入见赏期", "La gorge de Naruko est déjà à son meilleur"),
    ("落葉＝落叶 a", "落葉 = feuilles tombées a"),
    ("プリッツ＝咸味细饼干 c", "プリッツ = biscuit fin salé c"),
]

PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Note — " + s,'),
        ('"Lucerna · 日语周报 VOL.3 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · HEBDOMADAIRE JAPONAIS VOL.3 · TEXTE EN JAPONAIS · EXPLICATIONS EN FRANÇAIS"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} sur {total}"'),
    ],
    "content12.py": [
        ('p.text(975, 330, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEXTES EN JAPONAIS · EXPLICATIONS EN FRANÇAIS — L\'ÉDITION POUR LES LECTEURS FRANCOPHONES", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Chaque semaine · 日本人が読んでいる日本語を読む"'),
        ('"周日是七五三"', '"Dimanche, c\'est Shichi-Go-San"'),
        ('"红叶最佳观赏期向南移动 · 详见第 6 版"',
         '"La saison des feuilles va vers le sud · Voir page 6"'),
        ('"トップニュース · 头条"', '"トップニュース · À la une"'),
        ('"終わる 结束 · お参り 参拜 · 移る 移动 · 熊手 竹耙吉祥物。"',
         '"終わる se terminer · お参り aller prier au sanctuaire · 移る se déplacer · 熊手 râteau porte-bonheur."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · Semaine en chiffres"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Entraîne-toi"'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Voir les articles ; statistiques non exactes"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · Dans ce numéro"'),
        ('"全部"', '"Tous niveaux"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Mot de la semaine"'),
        ('"千歳飴＝ 七五三的红白长糖。"',
         '"千歳飴 = bonbon de Shichi-Go-San."'),
        ('"短いニュース · 快讯"', '"短いニュース · En bref"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quiz éclair"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lis la première page et choisis · Réponses page 8"'),
        ('"レベル A2 · ポッキーの日と千歳飴 · 波奇日与千岁糖"',
         '"レベル A2 · ポッキーの日と千歳飴 · Jour des Pocky et chitose-ame"'),
        ('"細い 细长的 · 似ている 相似 · 分け合う 分享 · 塩味 咸味。"',
         '"細い fin · 似ている ressembler · 分け合う partager · 塩味 salé."'),
        ('"願い 愿望 · 撮る 拍照 · 楽しむ 享受。"',
         '"願い un vœu · 撮る prendre une photo · 楽しむ apprécier."'),
        ('"你呢？11月11日想和谁分享波奇？写两句日语寄来。"',
         '"Avec qui aimerais-tu partager des Pocky le 11 novembre ? Écris deux phrases en japonais et envoie-les."'),
        ('"11月のことば · 11月词语"', '"11月のことば · Mots de novembre"'),
        ('"「1」の日と七五三の4つの言葉 · 关于“1”之日与七五三的四个词"',
         '"「1」の日と七五三の4つの言葉 · Quatre mots pour le jour des 1 et Shichi-Go-San"'),
        ('"波奇巧克力棒"', '"bâtonnet au chocolat"'),
        ('"红白长糖"', '"long bonbon rouge et blanc"'),
        ('"祈求生意兴隆的竹耙"', '"râteau porte-bonheur pour les affaires"'),
        ('"最佳观赏期"', '"le meilleur moment"'),
        ('"練習 · 第 2 版练习"', '"練習 · Exercices page 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 七五三と酉の市 · 七五三与酉之市"',
         '"レベル A2→B1 · 七五三と酉の市 · Shichi-Go-San et Tori-no-ichi"'),
        ('"成長 成长 · 元気 健康 · 願い 愿望 · 日にち 日期。"',
         '"成長 croissance · 元気 en bonne santé · 願い un vœu · 日にち la date."'),
        ('"商売繁盛 生意兴隆 · 縁起物 吉祥物 · 並ぶ 排列。"',
         '"商売繁盛 affaires florissantes · 縁起物 porte-bonheur · 並ぶ faire la queue."'),
        ('"你呢？七五三那天想拍什么样的照片？写两句日语寄来。"',
         '"Quelle photo aimerais-tu prendre pour Shichi-Go-San ? Écris deux phrases en japonais et envoie-les."'),
        ('"練習 · 第 3 版练习"', '"練習 · Exercices page 3"'),
        ('"レベル B1 · 日本シリーズ4連勝 · 日本大赛四连胜"',
         '"レベル B1 · 日本シリーズ4連勝 · Quatre victoires d\'affilée aux Japan Series"'),
        ('"接戦 势均力敌的比赛 · サヨナラ 再见（致胜） · 連続 连续。"',
         '"接戦 match serré · サヨナラ coup décisif (sayonara) · 連続 d\'affilée."'),
        ('"日本シリーズの記録 · 大赛记录"', '"日本シリーズの記録 · Bilan"'),
        ('"前号 上一期 · 全部 全部。"', '"前号 le numéro précédent · 全部 tout."'),
        ('"大相撲九州場所が始まりました · 大相扑九州场所开幕"',
         '"大相撲九州場所が始まりました · Le tournoi de sumo de Kyushu a commencé"'),
        ('"練習 · 第 4 版练习"', '"練習 · Exercices page 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Jeunesse"'),
        ('"レベル B1 · 11月11日の分かち合い · 11月11日的分享"',
         '"レベル B1 · 11月11日の分かち合い · Partage le 11 novembre"'),
        ('"渡す 递给 · つなぐ 连接 · 送り合う 互相发送。"',
         '"渡す tendre · つなぐ relier · 送り合う s\'envoyer."'),
        ('"思い出 回忆 · 大きくなる 长大。"',
         '"思い出 un souvenir · 大きくなる grandir."'),
        ('"你呢？想把波奇递给谁？写两句日语寄来。"',
         '"À qui aimerais-tu tendre des Pocky ? Écris deux phrases en japonais et envoie-les."'),
        ('"練習 · 第 5 版练习"', '"練習 · Exercices page 5"'),
        ('"レベル B2 · 紅葉の見頃は南へ · 红叶最佳观赏期向南移动"',
         '"レベル B2 · 紅葉の見頃は南へ · La saison des feuilles va vers le sud"'),
        ('"目安 标准 · 色づき 变色 · 変化 变化 · 準備 准备。"',
         '"目安 un repère · 色づき coloration · 変化 changement · 準備 préparation."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Lire le graphique"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Données d\'exercice"'),
        ('"練習 · 第 6 版练习"', '"練習 · Exercices page 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Langue"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Trois niveaux, trois thèmes"'),
        ('"読書週間 读书周 · 習慣 习惯 · 借りる 借。"',
         '"読書週間 Semaine de la lecture · 習慣 une habitude · 借りる emprunter."'),
        ('"七五三 七五三 · 千歳飴 千岁糖 · 晴れ着 盛装"',
         '"七五三 Shichi-Go-San · 千歳飴 chitose-ame · 晴れ着 tenue de fête"'),
        ('"〜連勝 连胜 · 〜% 百分之〜 · 〜組以上 组以上。"',
         '"〜連勝 victoires d\'affilée · 〜% pour cent · 〜組以上 groupes ou plus."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Clinique des erreurs"'),
        ('"有「昨日」时要用过去式。"', '"Avec 「昨日」, emploie le passé."'),
        ('"动词名词化时要加「こと」。"',
         '"Ajoute 「こと」 pour faire un nom d\'un verbe."'),
        ('"得到东西的场所用「で」。"',
         '"「で」 pour le lieu où l\'on reçoit."'),
        ('"看的场所用「で」。"', '"「で」 pour le lieu où l\'on regarde."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Structure hebdo"'),
        ('"句式拆解：追赶最佳观赏期。"',
         '"Décomposition : courir après le meilleur moment."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Courrier des lecteurs"'),
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.4に載せます。"',
         'ld_fr = "Exemple de la rédaction, pas une vraie lettre. À la date limite, '
         'aucune lettre ni composition n\'était arrivée ; les deux paraîtront '
         'dans le VOL.4. Envoyez-nous votre lettre en japonais — les lettres '
         'choisies seront publiées dans le VOL.4 !"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.4将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_fr, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_fr, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Phrases de la semaine (mot pour mot, de ce numéro)"'),
        ('"读书周在11月9日星期一结束。"', '"La Semaine de la lecture se termine le lundi 9 novembre."'),
        ('"11月15日星期日是七五三的中心日。"',
         '"Le dimanche 15 novembre est le cœur de Shichi-Go-San."'),
        ('"波奇与百力滋之日始于1999年。"', '"Le jour des Pocky et Pretz a commencé en 1999."'),
        ('"千岁糖是寄托长寿愿望的糖果。"',
         '"Chitose-ame est le bonbon du vœu de longue vie."'),
        ('"七五三是3岁、5岁和7岁孩子的庆祝活动。"',
         '"Shichi-Go-San fête les enfants de 3, 5 et 7 ans."'),
        ('"软银以四连胜夺得日本第一。"',
         '"SoftBank a pris le titre du Japon avec quatre victoires d\'affilée."'),
        ('"11月11日是波奇日。"', '"Le 11 novembre, c\'est le jour des Pocky."'),
        ('"红叶的最佳观赏期从北向南移动。"',
         '"La meilleure saison des feuilles va du nord au sud."'),
        ('"第1面"', '"p. 1"'),
        ('"第2面"', '"p. 2"'),
        ('"第3面"', '"p. 3"'),
        ('"第4面"', '"p. 4"'),
        ('"第5面"', '"p. 5"'),
        ('"第6面"', '"p. 6"'),
        ('"来週 · 下期预告 (VOL.4)"', '"来週 · Prochain numéro (VOL.4)"'),
    ],
    "content8.py": [
        ('af.para(f"— 第{pg}面 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)', 'af.para(f"— 第{pg}面 —", 12.9, "sans", True, OLIVE, lh=1.13, gap=2, split=False)'),
        ('af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)', 'af.para(txt, 12.9, lh=1.13, gap=0.5, split=False)'),
        ('"テストと答え · 练习与答案"', '"テストと答え · Test et réponses"'),
        ('"七五三是11月15日。"', '"Shichi-Go-San, c\'est le 15 novembre."'),
        ('"波奇日从1999年开始。"', '"Le jour des Pocky a commencé en 1999."'),
        ('"读书周从10月27日开始。→ ___"',
         '"La Semaine de la lecture commence le 27 octobre. → ___"'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。→ ___"',
         '"Ceux qui vont voir les feuilles peuvent courir après la meilleure saison du nord au sud. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Tâche d\'écriture (pas de réponse unique) ; le texte modèle ({NCHARS} caractères) est ci-dessous."'),
        ('"（开放题，范文如下）"', '"(tâche ouverte — texte modèle ci-dessous)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Texte modèle dans la section H de cette page ({NCHARS} caractères)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Réponses — groupées par page ; cherche juste ton numéro"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Une courte note en français avec chaque réponse · ✓ = l\'exercice au texte modèle"'),
        ('f"— 第{pg}面 —"', 'f"— Page {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL3.pdf"', '"Lucerna-VOL3-FR.pdf"'),
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
    src_svg = os.path.join(CORE, "svglib.py")
    data = open(src_svg, "rb").read()
    assert hashlib.md5(data).hexdigest() == CANON_SVGLIB_MD5, "svglib md5 mismatch"
    shutil.copyfile(src_svg, os.path.join(HERE, "svglib.py"))
    shutil.copyfile(os.path.join(CORE, "run.py"), os.path.join(HERE, "run.py"))
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(CORE, "assets")):
        shutil.copyfile(os.path.join(CORE, "assets", f),
                        os.path.join(HERE, "assets", f))
    note_map = dict(NOTES)
    fnames = ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "render.py"]
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
