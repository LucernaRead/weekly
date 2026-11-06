# -*- coding: utf-8 -*-
"""W45 ES x FR fan-out transform: Chinese explanation layer -> French.
Applies exact-string replacements to the build copy ONLY (never the core
build dir). Each replacement asserts its expected hit count; the script
aborts on any mismatch. Order matters: longer strings before their
substrings, full bridge sentences before bare instr= values.
Type names (完成句子/单选/...) stay frozen per the W43 ES x FR precedent
(only instr= labels translate); P8 separator stays Spanish (W43 precedent).
"""
import sys, os

BASE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.join(BASE, "build")

# (filename, old, new, expected_count)
R = []
def r(f, old, new, n=1):
    R.append((f, old, new, n))

# ---------- bslib4.py: furniture ----------
r("bslib4.py",
  '"La Lucerna · 西班牙语周报 VOL.2 · LUCERNA SPANISH WEEKLY"',
  '"La Lucerna · HEBDOMADAIRE ESPAGNOL VOL.2 · TEXTE EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS"')
r("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} sur {total}"')
r("bslib4.py", '"译注｜" + s', '"Note — " + s')

# ---------- content12.py: P1 ----------
r("content12.py",
  'p.text(975, 92, "CADA SEMANA EN ESPAÑOL · 每周一期 · 读西班牙人正在读的西班牙语", 21, "sans", False, GREY, anchor="middle")',
  'p.text(975, 92, "CADA SEMANA EN ESPAÑOL · CHAQUE SEMAINE · L\'ESPAGNOL DES ESPAGNOLS", 21, "sans", False, GREY, anchor="middle")')
r("content12.py",
  'p.text(975, 330, "西 班 牙 语 周 报 · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 46, "serif", True, INK, anchor="middle")',
  'p.text(975, 330, "HEBDOMADAIRE ESPAGNOL · VOL.2 · LA VIVIENDA · EL PUENTE · EL FÚTBOL", 46, "serif", True, INK, anchor="middle")')
r("content12.py",
  'p.text(975, 372, "EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA", 19, "sans", False, GREY, anchor="middle")',
  'p.text(975, 372, "TEXTES EN ESPAGNOL · EXPLICATIONS EN FRANÇAIS — L\'ÉDITION POUR LES LECTEURS FRANCOPHONES", 20, "sans", True, BRICK, anchor="middle")')
r("content12.py", "距大选还有 27 天 · 住房决定选战", "PLUS QUE 27 JOURS AVANT LE 29-N · LE LOGEMENT DÉCIDE")
r("content12.py", "本期头条 · 详见第 2、6 版", "À LA UNE · VOIR PAGES 2 ET 6")
r("content12.py", "LA NOTICIA · 头条", "LA NOTICIA · À LA UNE")
r("content12.py",
  "讲解｜la cuenta atrás 倒计时 · disolver las Cortes 解散议会 · el decreto 法令 · la candidatura 候选人名单。",
  "Notes — la cuenta atrás = le compte à rebours · disolver las Cortes = dissoudre le Parlement · el decreto = le décret · la candidatura = la candidature.")
r("content12.py", "LA SEMANA EN CIFRAS · 数字看本周", "LA SEMANA EN CIFRAS · EN CHIFFRES")
r("content12.py", "（距 29 日大选 27 天）", "(27 jours avant le vote du 29)")
r("content12.py", "（11 月 2 日放假的自治区）", "(communautés en congé le lundi 2)")
r("content12.py", "（CIS 十月数据）", "(baromètre CIS d'octobre)")
r("content12.py", "AHORA TÚ · 即学即练", "AHORA TÚ · À TOI DE JOUER")
r("content12.py", "las listas ya están presentadas; ahora se escriben los programas", "listes déjà déposées, programmes en cours d'écriture")
r("content12.py", "大选在 11 月 29 日周日", "élections le dimanche 29 novembre")
r("content12.py", "住房是选战的决定性议题", "le logement, sujet décisif de la campagne")
r("content12.py", "周一放假的自治区有 9 个", "9 communautés en congé le lundi", 2)
r("content12.py", "马竞–巴萨周日 21:00 开球", "Atlético–Barça le dimanche à 21:00")
r("content12.py", "NFL 马德里站周日 15:30 开球", "la NFL à Madrid le dimanche à 15:30")
r("content12.py", "本周五大看点 · Para entender la semana", "Cinq clés · Pour comprendre la semaine")
r("content12.py", "五大看点，不编数字：全在本期里讲清。", "Cinq clés, sans chiffres inventés.")
r("content12.py", "EN ESTA EDICIÓN · 本期目录", "EN ESTA EDICIÓN · SOMMAIRE")
r("content12.py", "“竞选预热期”：正式竞选前的几周。", "« La précampagne » : les semaines avant la campagne officielle.")
r("content12.py", "BREVES · 快讯", "BREVES · EN BREF")
r("content12.py", "QUIZ RELÁMPAGO · 闪电问答", "QUIZ RELÁMPAGO · QUIZ ÉCLAIR")
r("content12.py", "读头版，选出正确答案 · 答案见第 8 版", "Lisez la une et choisissez la bonne réponse · Réponses page 8")
r("content12.py", "大选在 11 月 29 日", "élections le 29 novembre", 2)
r("content12.py", "NFL 马德里站周日下午", "la NFL à Madrid le dimanche après-midi")
r("content12.py", "马竞–巴萨周日 21:00", "Atlético–Barça le dimanche à 21:00")
# ---------- content12.py: P2 (full lines before substrings) ----------
r("content12.py", "VIDA · 生活", "VIDA · VIE QUOTIDIENNE")
r("content12.py", "NIVEL A2 · El puente del lunes 2 · 11 月 2 日的连休", "NIVEL A2 · El puente del lunes 2 · Le pont du lundi 2")
r("content12.py", "EL CALENDARIO · 本周日历", "EL CALENDARIO · LE CALENDRIER")
r("content12.py", "（周一九地连休；周二《官方公报》公布正式候选名单）", "(pont dans neuf communautés lundi ; listes proclamées au BOE mardi)")
r("content12.py", "（周二欧冠三场西甲球队比赛）", "(mardi : trois clubs espagnols en Ligue des champions)")
r("content12.py", "（周三皇马客场对雅典 AEK）", "(mercredi : le Real à Athènes contre l'AEK)")
r("content12.py", "（周四皇家社会欧联对里昂）", "(jeudi : la Real Sociedad contre Lyon en Ligue Europa)")
r("content12.py", "（周五联赛第 12 轮开球）", "(vendredi : ouverture de la 12e journée de Liga)")
r("content12.py", "（周六瓦伦西亚对皇马）", "(samedi : Valence contre le Real à Mestalla)")
r("content12.py", "（周日 NFL 马德里站＋马竞对巴萨）", "(dimanche : la NFL au Bernabéu et Atlético–Barça)")
r("content12.py", "festivo 放假的 · el puente 连休 · la comunidad 自治区 · anochecer 天黑 · el horario de invierno 冬令时。",
  "festivo = en congé · el puente = le pont · la comunidad = la communauté autonome · anochecer = la tombée de la nuit · el horario de invierno = l'heure d'hiver.")
r("content12.py", "¿Y TÚ? · 说说你自己", "¿Y TÚ? · ET TOI ?")
r("content12.py", "11 月 2 日你那里放假吗？连休你做什么：旅行、休息还是看球？写两句西班牙语寄给编辑部。",
  "Le lundi 2 est-il férié chez toi ? Que fais-tu du pont : voyager, te reposer ou regarder du foot ? Écris deux phrases en espagnol et envoie-les à la rédaction.", 2)
r("content12.py", "LOS DÍAS DE LA SEMANA · 这样说日期", "LOS DÍAS DE LA SEMANA · DIRE LES DATES")
r("content12.py", "lunes 2 – domingo 8 de noviembre · 11 月 2 日周一至 8 日周日", "lunes 2 – domingo 8 de noviembre · du lundi 2 au dimanche 8 novembre")
r("content12.py", "EJERCICIOS · 第 2 版练习", "EJERCICIOS · EXERCICES")
r("content12.py", "答案见第 8 版 · 题目可跨级混排，按题号找答案", "Réponses page 8 · Exercices mélangés par niveau, cherchez par numéro")
r("content12.py", "用正确的日期形式补全句子。", "Complétez avec la bonne forme de la date.")
r("content12.py", "11 月 2 日周一", "le lundi 2 novembre")
r("content12.py", "11 月 8 日周日", "le dimanche 8 novembre")
r("content12.py", "每月 1 号说 el uno", "le 1er du mois se dit el uno")
r("content12.py", "月份小写", "les mois en minuscules")
r("content12.py", "补全动词的现在时形式。", "Complétez avec le présent du verbe.")
r("content12.py", "el lunes → es（单数）", "el lunes → es (singulier)")
r("content12.py", "todos → preguntan", "todos → preguntan (pluriel)")
r("content12.py", "anochecer → anochece", "anochecer → anochece (3e personne)")
r("content12.py", "nosotros → descansamos", "nosotros → descansamos")
r("content12.py", "el fin de semana → dura", "el fin de semana → dura (singulier)")
r("content12.py", "读第 2 版文章，选出正确答案。", "Lisez l'article de la page 2 et choisissez la bonne réponse.")
r("content12.py", "九个自治区周一放假", "neuf communautés en congé le lundi")
r("content12.py", "诸圣节 11 月 1 日落在周日", "la Toussaint tombe le dimanche 1er novembre")
r("content12.py", "加泰罗尼亚周一是工作日", "en Catalogne, le lundi est un jour de travail")
r("content12.py", "冬令时第二周，天黑得早", "deuxième semaine à l'heure d'hiver, la nuit tombe tôt")
r("content12.py", "puente=三天连休 b", "puente = le pont de trois jours (b)")
r("content12.py", "festivo=放假的 a", "festivo = en congé (a)")
r("content12.py", "anochecer=天黑 c", "anochecer = la tombée de la nuit (c)")
r("content12.py", "comunidad=自治区 d", "comunidad = la communauté autonome (d)")
r("content12.py", 'instr="把词和释义配对"', 'instr="Associer"', 1)
r("content12.py", 'instr="填空"', 'instr="Compléter"', 10)

# ---------- content34.py: P3 ----------
r("content34.py", "CULTURA · 文化", "CULTURA · CULTURE")
r("content34.py", "A2 → B1 · La semana pasada: tres noches de otoño · 上周的三个秋夜",
  "A2 → B1 · La semana pasada: tres noches de otoño · La semaine dernière : trois nuits d'automne")
r("content34.py", "sobrio 克制的 · el homenaje 纪念表彰 · el disfraz 服装（化装） · el boniato 红薯 · el cementerio 墓地。",
  "sobrio = sobre · el homenaje = l'hommage · el disfraz = le déguisement · el boniato = la patate douce · el cementerio = le cimetière.")
r("content34.py", "¿Y TÚ? · 说说你自己", "¿Y TÚ? · ET TOI ?", 2)
r("content34.py", "你最喜欢哪一夜：29 日、31 日还是 1 日？31 日你吃了什么？写两句寄来。",
  "Quelle nuit préfères-tu : celle du 29, du 31 ou du 1er ? Et qu'as-tu mangé le 31 ? Écris deux phrases.", 2)
r("content34.py", "周日 21:00 你看哪一场？马竞主场谁赢？写两句西班牙语寄来。",
  "Dimanche à 21:00, que regardes-tu ? Et qui gagne au Metropolitano ? Écris deux phrases en espagnol.", 2)
r("content34.py", "EJERCICIOS · 第 3 版练习", "EJERCICIOS · EXERCICES")
r("content34.py", "EJERCICIOS · 第 4 版练习", "EJERCICIOS · EXERCICES")
r("content34.py", "答案见第 8 版 · 题目可跨级混排，按题号找答案", "Réponses page 8 · Exercices mélangés par niveau, cherchez par numéro", 2)
r("content34.py", "读第 3 版文章，判断对错。", "Lisez l'article de la page 3 et dites si c'est vrai ou faux.")
r("content34.py", "DANA 纪念活动在 10 月 29 日周四", "les actes de mémoire de la DANA ont eu lieu le jeudi 29 octobre")
r("content34.py", "Castanyada 吃烤栗子、红薯和 panellets", "à la Castanyada, on mange châtaignes grillées, patates douces et panellets")
r("content34.py", "Samaín 是加利西亚古节，不是万圣节译名", "le Samaín est une fête galicienne ancienne, pas un autre nom d'Halloween")
r("content34.py", "诸圣节在 11 月 1 日，不是 10 月 31 日", "la Toussaint, c'est le 1er novembre, pas le 31 octobre")
r("content34.py", "周日家属去墓地献花", "le dimanche, les familles portent des fleurs au cimetière")
r("content34.py", "用方框里的词填空。", "Complétez avec les mots de l'encadré.")
r("content34.py", "给逝者带花 flores", "flores = des fleurs pour les défunts")
r("content34.py", "cementerio = 墓地", "cementerio = le cimetière")
r("content34.py", "castañas asadas 烤栗子", "castañas asadas = châtaignes grillées")
r("content34.py", "disfraz = 化装服装", "disfraz = le déguisement")
r("content34.py", "actos de memoria 纪念活动", "actos de memoria = actes de mémoire")
r("content34.py", 'e.bridge("选出正确答案。")', 'e.bridge("Choisissez la bonne réponse.")')
r("content34.py", "DANA 纪念是 2024 年风暴两周年", "on a commémoré la DANA de 2024, deux ans après")
r("content34.py", "Castanyada 在加泰罗尼亚", "la Castanyada se fête en Catalogne")
r("content34.py", "Samaín 是加利西亚古老节日", "le Samaín est une très vieille fête galicienne")
r("content34.py", "三夜之后周一有人连休有人上班", "après les trois nuits, lundi : pont pour les uns, travail pour les autres")
r("content34.py", "把词组成正确的句子。", "Formez la phrase correcte avec ces mots.")
r("content34.py", "动词第二位", "le verbe en 2e position")
r("content34.py", "时间在前，动词第二", "le temps d'abord, le verbe en 2e position")
r("content34.py", "地点在前，动词第二", "le lieu d'abord, le verbe en 2e position")
r("content34.py", "间接疑问用 si", "l'interrogation indirecte emploie si")
# ---------- content34.py: P4 ----------
r("content34.py", "DEPORTE · 体育", "DEPORTE · SPORT")
r("content34.py", "NIVEL B1 · Europa primero, el domingo a las 21:00 · 欧战在先，周日晚九点",
  "NIVEL B1 · Europa primero, el domingo a las 21:00 · L'Europe d'abord, dimanche à 21:00")
r("content34.py", "la jornada 轮次 · recortar la distancia 缩小分差 · recibir 主场迎战 · visitar 客场挑战 · el Metropolitano 马竞主场。",
  "la jornada = la journée de championnat · recortar la distancia = réduire l'écart · recibir = recevoir à domicile · visitar = jouer à l'extérieur · el Metropolitano = le stade de l'Atlético.")
r("content34.py", "LA SEMANA EUROPEA Y LA JORNADA 12 · 欧战周与联赛第 12 轮",
  "LA SEMANA EUROPEA Y LA JORNADA 12 · LA SEMAINE EUROPÉENNE ET LA 12e JOURNÉE")
r("content34.py", "读第 4 版文章，选出正确答案。", "Lisez l'article de la page 4 et choisissez la bonne réponse.")
r("content34.py", "皇马 2–1 赢下国家德比", "le Real gagne le Clásico 2–1")
r("content34.py", "姆巴佩进了两球", "Mbappé marque les deux buts")
r("content34.py", "周二欧冠三场西甲球队比赛", "mardi : trois clubs espagnols en Ligue des champions")
r("content34.py", "周日 21:00 马竞–巴萨", "Atlético–Barça le dimanche à 21:00")
r("content34.py", "周日下午还有 NFL 马德里站", "dimanche après-midi : la NFL à Madrid")
r("content34.py", "jornada=轮次 b", "jornada = la journée (b)")
r("content34.py", "recibir=主场迎战 a", "recibir = recevoir à domicile (a)")
r("content34.py", "visitar=客场挑战 d", "visitar = jouer à l'extérieur (d)")
r("content34.py", "recortar=缩小分差 c", "recortar = réduire l'écart (c)")
r("content34.py", "用括号里词的比较级或 -ísimo 形式填空。", "Complétez avec le comparatif ou la forme en -ísimo du mot entre parenthèses.")
r("content34.py", "más + importante（马竞–巴萨更重要）", "más + importante (l'Atlético–Barça est plus important)")
r("content34.py", "muchísimos partidos 比赛很多", "muchísimos partidos = énormément de matches")
r("content34.py", "malo 的比较级是 peor", "le comparatif de malo est peor")
r("content34.py", "bueno 的比较级是 mejor", "le comparatif de bueno est mejor")
r("content34.py", "把句子改成过去时（pretérito indefinido）。", "Mettez la phrase au passé (pretérito indefinido).")
r("content34.py", "ganar → ganó", "ganar → ganó (passé)")
r("content34.py", "marcar → marcó", "marcar → marcó (passé)")
r("content34.py", "perder → perdió", "perder → perdió (passé)")
r("content34.py", "recortar → recortó", "recortar → recortó (passé)")
r("content34.py", "ir 的过去时是 fueron", "le passé de ir est fueron")
r("content34.py", 'instr="把词和释义配对"', 'instr="Associer"', 1)
r("content34.py", 'instr="判断"', 'instr="Vrai ou faux"', 5)
r("content34.py", 'instr="填空"', 'instr="Compléter"', 9)
r("content34.py", 'instr="造句"', 'instr="Former une phrase"', 3)
r("content34.py", 'instr="改写"', 'instr="Reformuler"', 6)

# ---------- content56.py: P5 ----------
r("content56.py", "JUVENTUD · 青年", "JUVENTUD · JEUNESSE")
r("content56.py", "NIVEL B1 · La NFL en Madrid · NFL 来到马德里", "NIVEL B1 · La NFL en Madrid · La NFL à Madrid")
r("content56.py", "EL PLAN DEL PUENTE · 连休计划", "EL PLAN DEL PUENTE · LE PLAN DU PONT")
r("content56.py", "（周一：休息陪家人；若你那里连休，就去旅行）", "(lundi : repos en famille — ou voyage, si tu fais le pont)")
r("content56.py", "（周六晚：瓦伦西亚对皇马）", "(samedi soir : Valence contre le Real)")
r("content56.py", "（周日下午：NFL 马德里站）", "(dimanche après-midi : la NFL à Madrid)")
r("content56.py", "（周日晚：马竞对巴萨）", "(dimanche soir : Atlético contre Barça)")
r("content56.py", "（返校返工；竞选 13 日开始）", "(retour en classe et au travail ; la campagne commence le 13)")
r("content56.py", "el emparrillado 美式足球场（烤架形场地） · el himno 国歌 · el touchdown 达阵得分 · la calabaza 南瓜。",
  "el emparrillado = le terrain de football américain · el himno = l'hymne · el touchdown = le touchdown · la calabaza = la citrouille.")
r("content56.py", "¿Y TÚ? · 说说你自己", "¿Y TÚ? · ET TOI ?")
r("content56.py", "你看过美式足球比赛吗？你更喜欢足球还是美式足球？写两句寄来。",
  "As-tu déjà vu un match de football américain ? Préfères-tu le foot ou le football américain ? Écris deux phrases.", 2)
r("content56.py", "EJERCICIOS · 第 5 版练习", "EJERCICIOS · EXERCICES")
r("content56.py", "EJERCICIOS · 第 6 版练习", "EJERCICIOS · EXERCICES")
r("content56.py", "答案见第 8 版 · 题目可跨级混排，按题号找答案", "Réponses page 8 · Exercices mélangés par niveau, cherchez par numéro", 2)
r("content56.py", "读第 5 版文章，选出正确答案。", "Lisez l'article de la page 5 et choisissez la bonne réponse.")
r("content56.py", "NFL 马德里站周日 15:30", "la NFL à Madrid le dimanche à 15:30")
r("content56.py", "孟加拉虎对猎鹰", "Bengals contre Falcons")
r("content56.py", "西班牙国歌由吉他手演奏", "l'hymne espagnol est joué à la guitare")
r("content56.py", "首场 NFL 伯纳乌赛在 2025 年 11 月 16 日", "le premier match NFL au Bernabéu date du 16 novembre 2025")
r("content56.py", "美式足球用手打、四次进攻", "le football américain se joue à la main, en quatre tentatives")
r("content56.py", "用方框里的词填空。注意：有的词要变位。", "Complétez avec les mots de l'encadré. Attention : certains mots doivent être conjugués.")
r("content56.py", "estadio = 体育场", "estadio = le stade")
r("content56.py", "himno = 国歌", "himno = l'hymne")
r("content56.py", "acoger 变位 → acoge", "acoger conjugué → acoge")
r("content56.py", "(原形 acoger)", "(infinitif acoger)")
r("content56.py", "touchdown = 达阵得分", "touchdown = le touchdown")
r("content56.py", "calabaza = 南瓜", "calabaza = la citrouille")
r("content56.py", "disfraz = 化装服装", "disfraz = le déguisement")
r("content56.py", "用 ir a + 原形动词改写句子，表示“将要”。", "Reformulez avec ir a + infinitif pour dire « aller ».")
r("content56.py", "vamos a + 原形", "vamos a + infinitif")
r("content56.py", "va a + 原形", "va a + infinitif")
r("content56.py", "vas a + 原形", "vas a + infinitif")
r("content56.py", "van a + 原形", "van a + infinitif")
r("content56.py", "NFL 马德里站是伯纳乌第二场 NFL 比赛", "le match NFL de dimanche est le deuxième au Bernabéu")
r("content56.py", "美国国歌由 Momsen 演唱，不是 Sáinz-Villegas", "l'hymne américain est chanté par Momsen, pas par Sáinz-Villegas")
r("content56.py", "万圣节之夜在周六 31 日", "la nuit d'Halloween tombe le samedi 31")
# ---------- content56.py: P6 ----------
r("content56.py", "A FONDO · 深读", "A FONDO · EN PROFONDEUR")
r("content56.py", "NIVEL B2 · La vivienda decide la campaña · 住房决定选战",
  "NIVEL B2 · La vivienda decide la campaña · Le logement décide de la campagne")
r("content56.py", "看上面两张图，选出正确答案。", "Regardez les deux graphiques ci-dessus et choisissez la bonne réponse.")
r("content56.py", "CIS 里 PSOE 第一（34%）", "au CIS, le PSOE est premier (34 %)")
r("content56.py", "CIS 里 PP 22,2%", "au CIS, le PP est à 22,2 %")
r("content56.py", "住房是首要问题（55,7%）", "le logement est le premier problème (55,7 %)")
r("content56.py", "调查在 10 月 1–6 日进行", "le terrain a eu lieu du 1er au 6 octobre")
r("content56.py", "本报只刊登 CIS 这一组数据并注明来源日期", "La Lucerna ne publie que la série du CIS, avec source et date")
r("content56.py", "10 月 2 日议会否决两项住房法令", "le 2 octobre, le Parlement rejette deux décrets sur le logement")
r("content56.py", "10 月 5 日解散议会并召集大选", "le 5 octobre, dissolution du Parlement et convocation des élections")
r("content56.py", "民调是带误差的具体某天的照片", "un sondage est une photo avec marge d'erreur, prise un jour précis")
r("content56.py", "竞选 11 月 13 日开始", "la campagne commence le 13 novembre")
r("content56.py", "es posible que + 虚拟式 tenga", "es posible que + subjonctif (tenga)")
r("content56.py", "es importante que + 虚拟式 sea", "es importante que + subjonctif (sea)")
r("content56.py", "para que + 虚拟式（目的）", "para que + subjonctif (but)")
r("content56.py", "Aunque 后接陈述式（已知事实）", "Aunque + indicatif (fait connu)")
r("content56.py", "用方框里的词填空：sondeo · muestra · indecisos · margen de error",
  "Complétez avec les mots de l'encadré : sondeo · muestra · indecisos · margen de error")
r("content56.py", "sondeo = 民调", "sondeo = le sondage")
r("content56.py", "muestra = 样本（5.025 人）", "muestra = l'échantillon (5 025 personnes)")
r("content56.py", "indecisos = 未决定者", "indecisos = les indécis")
r("content56.py", "margen de error = 误差范围", "margen de error = la marge d'erreur")
r("content56.py", 'instr="填空"', 'instr="Compléter"', 14)
r("content56.py", 'instr="判断"', 'instr="Vrai ou faux"', 3)
r("content56.py", 'instr="改写"', 'instr="Reformuler"', 4)

# ---------- content7.py: P7 ----------
r("content7.py", "LENGUA · 语言", "LENGUA · LANGUE")
r("content7.py", "语言聚焦 · Tres niveles, tres herramientas · 三个级别，三件工具",
  "Focus langue · Tres niveles, tres herramientas · Trois niveaux, trois outils")
r("content7.py", "日期格式：el lunes 2 de noviembre；星期、月份小写；1 号说 el uno。",
  "Le format de la date : el lunes 2 de noviembre ; jours et mois en minuscules ; le 1er se dit el uno.")
r("content7.py", "el lunes 2 de noviembre 连休", "el lunes 2 de noviembre, jour de pont")
r("content7.py", "el 1 = el uno", "le 1er = el uno")
r("content7.py", "29 日是周日", "le 29 tombe un dimanche")
r("content7.py", "月份小写：noviembre", "les mois en minuscules : noviembre")
r("content7.py", "比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。",
  "Le comparatif : más…que, tan…como ; bueno → mejor, malo → peor ; jamais más mejor.")
r("content7.py", "más + cara（房价更高）", "más + cara (le logement coûte plus cher)")
r("content7.py", "tan + alta + como（同样高）", "tan + alta + como (aussi haut)")
r("content7.py", "bueno 的比较级是 mejor（不用 más）", "le comparatif de bueno est mejor (sans más)")
r("content7.py", "más mejor 是错误说法", "más mejor est une forme fautive")
r("content7.py", "es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。",
  "es necesario que, para que, ojalá + subjonctif ; creo que + indicatif.")
r("content7.py", "es necesario que + 虚拟式 baje", "es necesario que + subjonctif (baje)")
r("content7.py", "para que + 虚拟式 sea", "para que + subjonctif (sea)")
r("content7.py", "creo que + 陈述式 es", "creo que + indicatif (es)")
r("content7.py", "ojalá + 虚拟式：baje", "ojalá + subjonctif : baje")
r("content7.py", "# 盒高 = 绘制循环精确模拟（W43 回补修法：逐项模拟，不用平均行高）", "# box height = exact simulation of the draw loop (W43 backfill fix: simulate item by item, no average line height)")
r("content7.py", "ERRORES TÍPICOS · 常见错误", "ERRORES TÍPICOS · ERREURS TYPES")
r("content7.py", "lunes 是单数，动词用 es。", "lunes est singulier : on emploie es.")
r("content7.py", "mejor 本身就是比较级，不加 más。", "mejor est déjà un comparatif : pas de más.")
r("content7.py", "gente 是单数集合名词，动词用单数。", "gente est un collectif singulier : verbe au singulier.")
r("content7.py", "creo que 表肯定，用陈述式 es。", "creo que affirme : on emploie l'indicatif (es).")
r("content7.py", "LA PALABRA · 本周生词", "LA PALABRA · MOT DE LA SEMAINE")
r("content7.py", "precampaña = 竞选预热期：正式竞选前的几周。本期就是 precampaña；竞选 13 日周五开始。",
  "precampaña = la précampagne : les semaines avant la campagne officielle. Ce numéro est en précampagne ; la campagne commence le vendredi 13.", 2)
r("content7.py", "（ejemplo, escrito por la redacción）", "(ejemplo, escrito por la redacción)")
r("content7.py", "编辑部说明：截至本期截稿，未收到真实读者来信与第 8 版最佳作文，故本期登载编辑部示例信，承诺顺延至 VOL.3。欢迎来信！",
  "Note de la rédaction : à la clôture de ce numéro, aucune lettre réelle ni aucun meilleur texte de la page 8 n'était arrivé ; nous publions donc cette lettre d'exemple et la promesse est reportée au VOL.3. Écrivez-nous !")
r("content7.py", "FRASES DE LA SEMANA · 本周金句（逐字摘自本期文章）",
  "FRASES DE LA SEMANA · PHRASES DE LA SEMAINE (MOT POUR MOT, TIRÉES DE CE NUMÉRO)")
r("content7.py", "名单已提交：现在各党开始撰写纲领。", "Les listes sont déposées : les partis écrivent maintenant leurs programmes.")
r("content7.py", "11 月 2 日周一九个自治区放假，其他地区照常上班。", "Le lundi 2 novembre est férié dans neuf communautés — et jour de travail ailleurs.")
r("content7.py", "三个节日，同一个秋夜。", "Trois fêtes, une même nuit d'automne.")
r("content7.py", "皇马在诺坎普 2–1 获胜：这是巴萨本赛季联赛首败。", "Le Real gagne 2–1 au Camp Nou : première défaite du Barça en Liga cette saison.")
r("content7.py", "伯纳乌把草皮换成烤架形球场：美式足球来到马德里。", "Le Bernabéu troque sa pelouse contre un terrain de football américain : le football américain arrive à Madrid.")
r("content7.py", "住房是 55.7% 的西班牙人的首要问题。", "Le logement est le premier problème pour 55,7 % des Espagnols.")
r("content7.py", "一次民调就是一张带误差的照片，拍于某一天。", "Un sondage est une photo avec marge d'erreur, prise un jour précis.")
r("content7.py", "11 月 8 日周日，马德里有两场约会：15:30 的 NFL 和 21:00 的马竞对巴萨。", "Le dimanche 8, Madrid a deux rendez-vous : la NFL à 15:30 et l'Atlético–Barça à 21:00.")
r("content7.py", "LA PRÓXIMA SEMANA · 下期预告 (VOL.3)", "LA PRÓXIMA SEMANA · LA SEMAINE PROCHAINE (VOL.3)")
r("content7.py", 'instr="填空"', 'instr="Compléter"', 9)

# ---------- content8.py: P8 ----------
r("content8.py", "EJERCICIOS Y RESPUESTAS · 练习与答案", "EJERCICIOS Y RESPUESTAS · EXERCICES ET RÉPONSES")
r("content8.py", "第 8 版 · La gran prueba de la semana + todas las respuestas", "Page 8 · La gran prueba de la semana + todas las respuestas")
r("content8.py", "ganó 2–1 = 以 2–1 获胜", "ganó 2–1 = gagner 2–1")
r("content8.py", "marcar dos goles = 进两球", "marcar dos goles = marquer deux buts")
r("content8.py", "primera derrota liguera = 联赛首败", "primera derrota liguera = première défaite en Liga")
r("content8.py", "recortar = 缩小分差", "recortar = réduire l'écart")
r("content8.py", "acoger = 承办（伯纳乌承办 NFL）", "acoger = accueillir (le Bernabéu accueille la NFL)")
r("content8.py", "el emparrillado = 美式足球场", "el emparrillado = le terrain de football américain")
r("content8.py", "周日上演马竞–巴萨", "dimanche : Atlético–Barça au Metropolitano")
r("content8.py", "himno = 国歌", "himno = l'hymne")
r("content8.py", "周一放假的自治区有 9 个", "9 communautés en congé le lundi")
r("content8.py", "诸圣节 11 月 1 日", "la Toussaint, le 1er novembre")
r("content8.py", "马竞–巴萨与 NFL 都在周日", "l'Atlético–Barça et la NFL ont lieu le dimanche")
r("content8.py", "Castanyada 吃 panellets", "à la Castanyada, on mange des panellets")
r("content8.py", "DANA 纪念活动在 10 月 29 日周四", "les actes de mémoire de la DANA ont eu lieu le jeudi 29 octobre")
r("content8.py", "大选在 11 月 29 日", "élections le 29 novembre")
r("content8.py", "CIS 十月调查：住房 55,7%", "au baromètre CIS d'octobre : le logement à 55,7 %")
r("content8.py", "竞选 11 月 13 日开始", "la campagne commence le 13 novembre")
r("content8.py", "马德里在放假名单里", "Madrid figure sur la liste des congés")
r("content8.py", "加泰罗尼亚周一是工作日", "en Catalogne, le lundi est un jour de travail")
r("content8.py", "Ana 只看 NFL；晚上看马竞–巴萨的是 Pablo", "Ana ne regarde que la NFL ; c'est Pablo qui voit l'Atlético–Barça le soir")
r("content8.py", "标题概括两地对比", "le titre résume le contraste entre les deux villes")
r("content8.py", "主语 + 动词 + 地点", "sujet + verbe + lieu")
r("content8.py", "时间在前", "le temps d'abord")
r("content8.py", "a las nueve = 在九点", "a las nueve = à neuf heures")
r("content8.py", "疑问词在句首", "le mot interrogatif en tête")
r("content8.py", "周一在九个自治区是假日。", "Le lundi est férié dans neuf communautés.")
r("content8.py", "周日我们看 NFL 和马竞–巴萨。", "Le dimanche, nous regardons la NFL et l'Atlético–Barça.")
r("content8.py", "对照原文", "d'après le texte", 2)
r("content8.py", "伯纳乌承办一场 NFL 比赛。→ ___", "Le Bernabéu accueille un match de la NFL. → ___")
r("content8.py", "acoger = 承办", "acoger = accueillir")
r("content8.py", "每个图表都必须标明来源。→ ___", "Chaque graphique doit indiquer sa source. → ___")
r("content8.py", "tener que = 必须", "tener que = devoir")
r("content8.py", "sondeo=民调 c", "sondeo = le sondage (c)")
r("content8.py", "muestra=样本 d", "muestra = l'échantillon (d)")
r("content8.py", "margen de error=误差范围 b", "margen de error = la marge d'erreur (b)")
r("content8.py", "junta electoral=选举委员会 a", "junta electoral = la commission électorale (a)")
r("content8.py", "alquiler = 租金", "alquiler = le loyer")
r("content8.py", "tres habitaciones = 三居室", "tres habitaciones = trois pièces")
r("content8.py", "¿cuánto cuesta? 多少钱", "¿cuánto cuesta ? = combien ça coûte ?")
r("content8.py", "firmar = 签（合同）", "firmar = signer (le contrat)")
r("content8.py", "mudanza = 搬家", "mudanza = le déménagement")
r("content8.py", "写作题（无唯一答案）；范文（84 词）见下。", "Exercice d'écriture (pas de réponse unique) ; texte modèle (84 mots) ci-dessous.")
r("content8.py", "（开放题，范文如下）", "Question ouverte — texte modèle ci-dessous sur cette page")
r("content8.py", "范文见本版 H 区（84 词）", "Texte modèle dans la section H de cette page (84 mots)")
r("content8.py", "RESPUESTAS · 参考答案 — 按版面分页排列，找到题号即可", "RESPUESTAS · CORRIGÉS — classés par page, cherchez le numéro")
r("content8.py", "每题附一句中文简析 · 带 ✓ 的为范文题", "Une courte explication en français pour chaque exercice · ✓ = exercice d'écriture")
r("content8.py", 'instr="造句"', 'instr="Former une phrase"', 4)
r("content8.py", 'instr="翻译"', 'instr="Traduire"', 4)
r("content8.py", 'instr="写作"', 'instr="Écrire"', 1)
r("content8.py", 'instr="把词和释义配对"', 'instr="Associer"', 1)

# ---------- layout fixes (W43 ES x FR / W45 ES x EN precedents, French text longer) ----------
# P6: bridge A to the W43 verbatim 1-liner; bridge D keeps its word list in
# 2 lines; exercise gap 3 -> 1 on all 18 size-19 items (W43 ES x FR §5.4).
r("content56.py", "Regardez les deux graphiques ci-dessus et choisissez la bonne réponse.", "Regardez les graphiques et choisissez.")
r("content56.py", "Complétez avec les mots de l'encadré : sondeo · muestra · indecisos · margen de error", "Complétez avec : sondeo · muestra · indecisos · margen de error")
# gap change is applied by a counted sed-like replace below (18 items).
# ---------- fit fixes (French apparatus only; appended AFTER the main R
# entries so they operate on the translated strings) ----------
r("content12.py", "« La précampagne » : les semaines avant la campagne officielle.", "La précampagne : avant la campagne officielle.")
r("content56.py", "EL PLAN DEL PUENTE · LE PLAN DU PONT", "EL PLAN DEL PUENTE · LE PLAN")
r("content7.py", '"ERRORES TÍPICOS · ERREURS TYPES", 23,', '"ERRORES TÍPICOS · ERREURS TYPES", 20,')
r("content7.py", "gente est un collectif singulier : verbe au singulier.", "gente : collectif singulier.")
r("content7.py", "creo que affirme : on emploie l'indicatif (es).", "creo que affirme : indicatif.")
r("content7.py", "precampaña = la précampagne : les semaines avant la campagne officielle. Ce numéro est en précampagne ; la campagne commence le vendredi 13.", "precampaña = la précampagne. La campagne commence le vendredi 13.", 2)
r("content7.py", "Note de la rédaction : à la clôture de ce numéro, aucune lettre réelle ni aucun meilleur texte de la page 8 n'était arrivé ; nous publions donc cette lettre d'exemple et la promesse est reportée au VOL.3. Écrivez-nous !", "Note de la rédaction : sans lettre réelle ni meilleur texte de la page 8 à la clôture, voici notre exemple ; promesse reportée au VOL.3. Écrivez-nous !")

r("content7.py", 'len(wrap("precampaña = la précampagne. La campagne commence le vendredi 13.", "sans", False, 20, CW - 44)) * 29 + 20', 'len(wrap("precampaña = la précampagne. La campagne commence le vendredi 13.", "sans", False, 20, CW - 44)) * 29 + 22')

# ---------- apply ----------
def main():
    # P6 gap 3 -> 1, exactly the 18 size-19 P6 exercise items in content56.py
    _p56 = os.path.join(BUILD, "content56.py")
    _s56 = open(_p56, encoding="utf-8").read()
    assert _s56.count("size=19, gap=3") == 18, _s56.count("size=19, gap=3")
    open(_p56, "w", encoding="utf-8").write(_s56.replace("size=19, gap=3", "size=19, gap=1"))
    # P8 answer lines 13.5/1.16 -> 13.2/1.12 + separator lh 1.16 -> 1.12 (W45 ES x EN §3.2)
    _p8 = os.path.join(BUILD, "content8.py")
    _s8 = open(_p8, encoding="utf-8").read()
    assert _s8.count('af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)') == 1
    assert _s8.count('af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)') == 1
    _s8 = _s8.replace('af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)',
                      'af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.12, gap=2, split=False)')
    _s8 = _s8.replace('af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)',
                      'af.para(txt, 13.2, lh=1.12, gap=0.5, split=False)')
    open(_p8, "w", encoding="utf-8").write(_s8)
    for fname, old, new, n in R:
        path = os.path.join(BUILD, fname)
        src = open(path, encoding="utf-8").read()
        cnt = src.count(old)
        if cnt != n:
            print(f"FAIL {fname}: expected {n} x {old[:60]!r}, found {cnt}")
            sys.exit(1)
        src = src.replace(old, new)
        open(path, "w", encoding="utf-8").write(src)
    print(f"transform OK: {len(R)} replacements applied")

    # P1 CIFRAS box title tsize 23 -> 21 (W43 ES x FR §5.1 precedent)
    _p12 = os.path.join(BUILD, "content12.py")
    _s12 = open(_p12, encoding="utf-8").read()
    _old12 = '("55,7 — % que cita la vivienda como el principal problema, según el CIS de octubre(baromètre CIS d\'octobre)", "serif", False, INK, 20.5, 1.35),\n])'
    assert _s12.count(_old12) == 1, _s12.count(_old12)
    open(_p12, "w", encoding="utf-8").write(_s12.replace(_old12, _old12[:-2] + "], tsize=21)"))
    # residual CJK check (svglib.py line 120 is a dead-code comment, allowed;
    # exercise TYPE names stay frozen per the W43 ES x FR precedent, only
    # instr= labels translate -- so strip the frozen type tokens first)
    import re
    TYPES = ["完成句子", "单选", "判断对错", "造句", "句型转换", "词汇配对", "翻译", "完形单选", "写作"]
    for fname in ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        src = open(os.path.join(BUILD, fname), encoding="utf-8").read()
        for t in sorted(TYPES, key=len, reverse=True):
            src = src.replace(t, "")
        hits = [(i + 1, l) for i, l in enumerate(src.splitlines()) if re.search(r"[\u4e00-\u9fff]", l)]
        if hits:
            print(f"RESIDUAL CJK in {fname}:")
            for ln, l in hits:
                print(f"  {ln}: {l[:120]}")
            sys.exit(1)
    print("residual CJK check: clean (content + bslib4)")

if __name__ == "__main__":
    main()
