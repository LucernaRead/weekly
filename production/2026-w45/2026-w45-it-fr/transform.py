# -*- coding: utf-8 -*-
"""W45 IT core -> IT x FR fan-out transform for the BUILD COPY ONLY.

Literal replacements only (tools README #17): each rep() fails loudly if
its old string is absent, so a typo can never silently skip a translation.
Italian target-language text is never a replacement target; only the
explanation layer (Chinese notes/bridges/titles/furniture) and the P8
E-section re-aiming change. Registry exercise-type names stay in Chinese
(never printed anywhere, W43 IT x FR precedent) so the registry stays
byte-comparable with the core. Furniture follows the shipped W43 IT x FR
SVGs (badge TEXTES EN ITALIEN ...; footer HEBDOMADAIRE ITALIEN; gloss
prefix "Note — "; P8 separators stay Italian "— PAGINA n —"), with VOL.1
-> VOL.2, which outrank the generic rules in tools README #20. Badge
geometry follows the W45 IT x EN precedent (inserted y=574, 22pt BRICK):
the W45 core's y=372 slot is frozen Italian strapline, unlike the W43
core's tagline slot.
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-it-fr-build')
C12, C34, C56, C7, C8, BS, SV = 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py', 'svglib.py'
ALL = [C12, C34, C56, C7, C8]

def rep(files, old, new, expect=None):
    total = 0
    for fn in files:
        p = B / fn
        t = p.read_text(encoding='utf-8')
        c = t.count(old)
        total += c
        if c:
            p.write_text(t.replace(old, new), encoding='utf-8')
    if expect is not None and total != expect:
        print(f'COUNT MISMATCH: {old!r} found {total}, expected {expect}'); sys.exit(1)
    if total == 0:
        print(f'NOT FOUND: {old!r}'); sys.exit(1)
    return total

# ---------- repoint OUT + render names (copy only; core untouched) ----------
rep(ALL, 'weekly-report-w45-it-core', 'weekly-report-w45-it-fr', 5)
rep(['render.py'], 'weekly-report-w45-it-core', 'weekly-report-w45-it-fr', 1)
rep(['render.py'], 'La-Lucerna-VOL2-web.pdf', 'La-Lucerna-VOL2-FR-web.pdf', 1)
rep(['render.py'], 'La-Lucerna-VOL2.pdf', 'La-Lucerna-VOL2-FR.pdf', 1)
rep(['render.py'], 'Render the IT weekly', 'Render the IT x FR edition', 1)

# ---------- bslib4 furniture (W43 IT x FR shipped strings, VOL.2) ----------
rep([BS], '"La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY"',
    '"La Lucerna · HEBDOMADAIRE ITALIEN VOL.2 · TEXTE EN ITALIEN · EXPLICATIONS EN FRANÇAIS"', 1)
rep([BS], 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} sur {total}"', 1)
rep([BS], '"译注｜" + s', '"Note — " + s', 1)
# svglib: one CJK docstring in an unused illustration helper; prints nothing.
rep([SV], 'for 重阳.', 'for Double Ninth Festival.', 1)

# ---------- P1 masthead + pairing badge (W45 insert geometry: y=574, 22pt BRICK) ----------
rep([C12], '"OGNI SETTIMANA IN ITALIANO · 每周一期 · 读意大利人正在读的意大利语"',
    '"OGNI SETTIMANA IN ITALIANO · L’ITALIEN QUE LISENT LES ITALIENS"', 1)
rep([C12], '"意 大 利 语 周 报 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"',
    '"JOURNAL ITALIEN · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"', 1)
rep([C12], 'p.text(RIGHT - 30, 522, "初寒之周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
    'p.text(RIGHT - 30, 522, "La semaine du premier froid · Voir page 2", 21, "sans", False, "#b3a06a", anchor="end")\np.text(975, 574, "TEXTES EN ITALIEN · EXPLICATIONS EN FRANÇAIS — L’ÉDITION POUR LES LECTEURS FRANCOPHONES", 22, "sans", True, BRICK, anchor="middle")', 1)
rep([C12], '"本周迎来第一场寒冷"', '"LE PREMIER FROID ARRIVE CETTE SEMAINE"', 1)
rep([C12], '"LA NOTIZIA · 头条"', '"LA NOTIZIA · À LA UNE"', 1)
rep([C12], '"讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。"',
    '"Notes : il primo freddo, le premier froid · il versante adriatico, le versant adriatique · la previsione, prévision · assaggi, dégustations."', 1)
rep([C12], '"LA SETTIMANA IN CIFRE · 数字看本周"', '"LA SETTIMANA IN CIFRE · EN CHIFFRES"', 1)
rep([C12], '（可能下初雪的海拔）', '(altitude des premières neiges légères)', 1)
rep([C12], '（米兰文化论坛 50 多场活动）', '(plus de 50 événements du Forum Cultura à Milan, du 3 au 8 novembre)', 1)
rep([C12], '（参加米兰潘妮托尼决赛的国家数）', '(pays représentés à la finale du Panettone à Milan)', 1)
rep([C12], '（本周末意甲第 11 轮）', '(11e journée de Serie A ce week-end)', 1)
rep([C12], '"ADESSO TU · 即学即练"', '"ADESSO TU · À TOI DE JOUER"', 1)
rep([C12], '"本周日程 · Cosa succede, giorno per giorno"', '"Cette semaine · Cosa succede, giorno per giorno"', 1)
rep([C12], '"日程以各活动日历为准，时间可能有变。"', '"Dates selon les calendriers des événements ; les horaires peuvent changer."', 1)
rep([C12], '"IN QUESTO NUMERO · 本期目录"', '"IN QUESTO NUMERO · SOMMAIRE"', 1)
rep([C12], '"“第一场寒冷”：温和秋天后的第一波寒冷。"', '"« Il primo freddo » : le froid après un automne doux."', 1)
rep([C12], '"IN BREVE · 快讯"', '"IN BREVE · EN BREF"', 1)
rep([C12], '"QUIZ LAMPO · 闪电问答"', '"QUIZ LAMPO · QUIZ ÉCLAIR"', 1)
rep([C12], '"读头版，选出正确答案 · 答案见第 8 版"', '"Lisez la une, choisissez la bonne réponse · Réponses page 8"', 1)

# ---------- band titles / subs ----------
rep([C12], '"VITA · 生活"', '"VITA · VIE QUOTIDIENNE"', 1)
rep([C12], '"LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒与追思日"',
    '"LIVELLO A2 · Il primo freddo e il 2 novembre · Premier froid et 2 novembre"', 1)
rep([C34], '"CULTURA · 文化"', '"CULTURA · CULTURE"', 1)
rep([C34], '"A2 → B1 · Panettone, torrone e musei aperti · 甜点与博物馆"',
    '"A2 → B1 · Panettone, torrone e musei aperti · Douceurs et musées ouverts"', 1)
rep([C34], '"SPORT · 体育"', '"SPORT · SPORT"', 1)
rep([C34], '"LIVELLO B1 · La Serie A e l\'Europa · 意甲与欧战"',
    '"LIVELLO B1 · La Serie A e l\'Europa · Serie A et Europe"', 1)
rep([C56], '"GIOVANI · 青年"', '"GIOVANI · JEUNESSE"', 1)
rep([C56], '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 卢卡之后"',
    '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · Après Lucca"', 1)
rep([C56], '"APPROFONDIMENTO · 深读"', '"APPROFONDIMENTO · EN PROFONDEUR"', 1)
rep([C56], '"LIVELLO B2 · Leggere le previsioni · 怎样读天气预报"',
    '"LIVELLO B2 · Leggere le previsioni · Comment lire une prévision"', 1)
rep([C7], '"LINGUA · 语言"', '"LINGUA · LANGUE"', 1)
rep([C7], '"聚焦语言 · Tre livelli, tre strumenti · 三个级别，三件工具"',
    '"Gros plan sur la langue · Tre livelli, tre strumenti · Trois niveaux, trois outils"', 1)
rep([C8], '"VALUTAZIONE E RISPOSTE · 练习与答案"', '"VALUTAZIONE E RISPOSTE · EXERCICES ET RÉPONSES"', 1)
rep([C8], '"第 8 版 · La grande prova della settimana + tutte le risposte"',
    '"Page 8 · La grande prova della settimana + tutte le risposte"', 1)

# ---------- section heads / shared apparatus ----------
rep(ALL, '"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
    '"Réponses page 8 · Niveaux mélangés — cherchez par numéro"', 5)
rep(ALL, '"E TU? · 说说你自己"', '"E TU? · À TOI LA PAROLE"')
rep([C12], '"ESERCIZI · 第 2 版练习"', '"ESERCIZI · Exercices page 2"', 1)
rep([C34], '"ESERCIZI · 第 3 版练习"', '"ESERCIZI · Exercices page 3"', 1)
rep([C34], '"ESERCIZI · 第 4 版练习"', '"ESERCIZI · Exercices page 4"', 1)
rep([C56], '"ESERCIZI · 第 5 版练习"', '"ESERCIZI · Exercices page 5"', 1)
rep([C56], '"ESERCIZI · 第 6 版练习"', '"ESERCIZI · Exercices page 6"', 1)
rep([C12], '"IL 2 NOVEMBRE · 追思日"', '"IL 2 NOVEMBRE · COMMÉMORATION DES DÉFUNTS"', 1)
rep([C34], '"LA SETTIMANA DEL CALCIO · 足球周"', '"LA SETTIMANA DEL CALCIO · SEMAINE DE FOOTBALL"', 1)
rep([C56], '"LE MINIME DI ESEMPIO · 练习用示例最低温 (DATI INVENTATI PER L\'ESERCIZIO)"',
    '"LE MINIME DI ESEMPIO · Minima d’exemple (DATI INVENTATI PER L\'ESERCIZIO)"', 1)
rep([C56], '"PROBABILITÀ · 概率"', '"PROBABILITÀ · PROBABILITÉ"', 1)

# ---------- bridges (printed grey sans) ----------
rep([C12], '"发稿时表决结果尚未确认，详见第 6 版。"',
    '"Au moment de mettre sous presse, le résultat du vote n’était pas encore confirmé — voir page 6."', 1)
rep([C12], '"用意大利语补全句子。"', '"Complétez les phrases en italien."', 1)
rep([C12], '"补全动词的现在时形式。"', '"Complétez avec le présent."', 1)
rep([C12], '"读第 2 版文章，选出正确答案。"', '"Lisez l’article page 2 et choisissez la bonne réponse."', 1)
rep([C34], '"读第 3 版文章，选出正确答案。"', '"Lisez l’article page 3 et choisissez la bonne réponse."', 1)
rep([C34], '"用方框里的词填空。"', '"Complétez avec les mots de l’encadré."', 1)
rep([C34], '"用 passato prossimo（近过去时）补全，注意助动词 avere / essere。"',
    '"Complétez avec le passato prossimo — attention aux auxiliaires avere / essere."', 1)
rep([C34], '"把词组成正确的句子。"', '"Remettez les mots dans le bon ordre."', 1)
rep([C34], '"读第 4 版文章，选出正确答案。"', '"Lisez l’article page 4 et choisissez la bonne réponse."', 1)
rep([C34], '"用括号里词的比较级填空（数据看赛程表）。"',
    '"Complétez avec le comparatif du mot entre parenthèses (voir le tableau des matchs)."', 1)
rep([C34], '"用 passato prossimo 补全。"', '"Complétez avec le passato prossimo."', 1)
rep([C56], '"读第 5 版文章，选出正确答案。"', '"Lisez l’article page 5 et choisissez la bonne réponse."', 1)
rep([C56], '"用方框里的词填空。注意：有的词要变成复数。"',
    '"Complétez avec les mots de l’encadré. Attention : certains mots doivent passer au pluriel."', 1)
rep([C56], '"用将来时（futuro semplice）补全。"', '"Complétez avec le futuro semplice."', 1)
rep([C56], '"发稿时 10 月 28 日表决结果尚未确认：本期只写预期日期、争议点和 DPB 数字，不写结果。"',
    '"Au moment de mettre sous presse, le résultat du vote du 28 octobre n’était pas encore confirmé : ce numéro donne seulement la date prévue, le point contesté et les chiffres du DPB, pas le résultat."', 1)
rep([C56], '"看上面的练习图表，选出正确答案。"',
    '"Regardez le graphique d’exercice ci-dessus et choisissez la bonne réponse."', 1)
rep([C56], '"用方框里的词填空：probabilità · media · bollettino · modello"',
    '"Complétez avec les mots de l’encadré : probabilità · media · bollettino · modello"', 1)
rep([C7], '"天气用无人称动词（第三人称单数）；“我冷”说 ho freddo，“外面冷”说 fa freddo。"',
    '"La météo emploie des verbes impersonnels (3e personne du singulier) : « j’ai froid » se dit ho freddo, « il fait froid dehors » se dit fa freddo."', 1)
rep([C7], '"讲过去用近过去时：arrivare/andare 等用 essere，分词配合性数；avere 的分词不变。"',
    '"Pour le passé, employez le passato prossimo : arrivare/andare prennent essere et le participe s’accorde ; avec avere, il ne change jamais."', 1)
rep([C7], '"è probabile che / è possibile che / bisogna che 后用虚拟式；so che、scrivono che 后用陈述式。"',
    '"Après è probabile che / è possibile che / bisogna che, employez le subjonctif ; après so che / scrivono che, l’indicatif."', 1)

# ---------- gloss() argument strings (counts must stay 1:1 with the core) ----------
rep([C12], '"il cappotto 大衣 · la sciarpa 围巾 · i guanti 手套 · a strati 分层穿衣 · il termosifone 暖气片 · il crisantemo 菊花"',
    '"il cappotto manteau · la sciarpa écharpe · i guanti gants · a strati en couches superposées · il termosifone radiateur · il crisantemo chrysanthème"', 1)
rep([C34], '"il panettone 米兰圣诞面包 · il torrone 牛轧糖 · l\'assaggio 品尝 · la bancarella 摊位 · il cantiere 施工现场/修复工地。"',
    '"il panettone gâteau de Noël milanais · il torrone nougat · l\'assaggio dégustation · la bancarella étal · il cantiere chantier."', 1)
rep([C34], '"la giornata 轮次 · la presentazione 赛前介绍 · gli spalti 看台 · la sera 晚上。"',
    '"la giornata journée de championnat · la presentazione présentation d’avant-match · gli spalti tribunes · la sera soir."', 1)
rep([C56], '"il cosplay 角色扮演服装 · gratuito 免费的 · il documentario 纪录片 · lo schermo 银幕。"',
    '"il cosplay costume de cosplay · gratuito gratuit · il documentario documentaire · lo schermo écran."', 1)
rep([C56], '"la probabilità 概率 · la media 平均值 · il modello 模型/预报模式 · il bollettino 公报/预报 · aggiornare 更新。"',
    '"la probabilità probabilité · la media moyenne · il modello modèle de prévision · il bollettino bulletin · aggiornare mettre à jour."', 1)

# ---------- P1/P2/P3/P4/P5 box parentheticals + E TU notes ----------
rep([C56], '（周二：米兰文化论坛开幕）', '(mardi : ouverture du Forum Cultura à Milan)', 1)
rep([C56], '（周三至周四：欧战直播）', '(mercredi-jeudi : coupes d’Europe à la télévision)', 1)
rep([C56], '（周五准备周末）', '(vendredi : préparer le week-end)', 1)
rep([C56], '（周六：米兰或克雷莫纳品尝）', '(samedi : dégustations à Milan ou à Crémone)', 1)
rep([C56], '（周日：意甲与返程）', '(dimanche : Serie A et retour)', 1)
rep([C12], '"初寒来了你穿什么：大衣、围巾还是手套？写两句意大利语寄给编辑部。"',
    '"Quand le premier froid arrive, que portez-vous : manteau, écharpe ou gants ? Écrivez deux phrases en italien et envoyez-les-nous."', 2)
rep([C34], '"你更喜欢传统潘妮托尼还是巧克力味的？写两句寄来。"',
    '"Préférez-vous le panettone traditionnel ou celui au chocolat ? Écrivez deux phrases et envoyez-les-nous."', 2)
rep([C34], '"周日晚上你看哪场比赛？写两句意大利语寄来。"',
    '"Quel match regarderez-vous dimanche soir ? Écrivez deux phrases en italien et envoyez-les-nous."', 2)
rep([C56], '"卢卡之后你去哪：文化论坛、电影还是美食节？写两句寄来。"',
    '"Après Lucca, où allez-vous : Forum Cultura, cinéma ou fête gourmande ? Écrivez deux phrases et envoyez-les-nous."', 2)

# ---------- P2 FRASE box: title at tsize=20 (W43 IT x FR precedent) ----------
rep([C12], 'f.box("LA FRASE PER RICORDARE · 口诀", [\n    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n])',
    'f.box("LA FRASE PER RICORDARE · À RETENIR", [\n    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n], tsize=20)', 1)

# ---------- P7: errori notes (kept to ONE wrapped line at 19.5pt, core col3 geometry) ----------
rep([C7], '"fa 后面的 freddo 永远不变。"', '"Après fa, freddo ne change jamais."', 1)
rep([C7], '"nevicare 只用第三人称单数。"', '"Nevicare : 3e personne du singulier seulement."', 1)
rep([C7], '"预报给的是概率，不是确定性。"', '"Probabilités, pas certitudes."', 1)
rep([C7], '"gente 是单数，动词形容词用单数阴性。"', '"Gente est singulier féminin."', 1)
rep([C7], '"ERRORI TIPICI · 常见错误"', '"ERRORI TIPICI · ERREURS TYPES"', 1)
# P7 parola: Italian definition sentence is FROZEN verbatim; only the gloss
# line below it is localised into French.
rep([C7], '"LA PAROLA · 本周生词"', '"LA PAROLA · MOT DE LA SEMAINE"', 1)
rep([C7], '"assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。"',
    '"assaggio = dégustation. Voir page 3 : dégustation gratuite à la finale du Panettone."', 2)
# P7 letters: Italian letter text frozen verbatim, including its
# "(esempio della redazione)" label. The French note states all three
# disclosure facts (no real letters yet, no best page-8 essay yet, the
# sample stands in and both are promised for VOL.3) plus an explicit
# imperative invitation with a VOL.3 publication promise.
rep([C7], '"这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！"',
    '"Exemple de la rédaction, pas une vraie lettre : pas encore de vraies lettres, pas encore de meilleur texte de la page 8 — les deux sont promis pour le VOL.3. Écrivez-nous !"', 2)
rep([C7], '"FRASI DELLA SETTIMANA · 本周金句（逐字摘自本期文章）"',
    '"FRASI DELLA SETTIMANA · PHRASES DE LA SEMAINE (verbatim de ce numéro)"', 1)
rep([C7], '"第一场真正的寒冷到来了。"', '"Le premier vrai froid de la saison est arrivé."', 1)
rep([C7], '"这不是确定性，而是概率。"', '"Ce n’est pas une certitude, c’est une probabilité."', 1)
rep([C7], '"11 月 2 日是追思日。"', '"Le 2 novembre est la commémoration des défunts."', 1)
rep([C7], '"天冷，穿暖和点！"', '"Il fait froid, couvrez-vous bien !"', 1)
rep([C7], '"观众可以免费品尝。"', '"Le public peut déguster gratuitement."', 1)
rep([C7], '"足球不会因为第一场寒冷而停下。"', '"Le football ne s’arrête pas pour le premier froid."', 1)
rep([C7], '"文化继续。"', '"La culture continue."', 1)
rep([C7], '"高概率不等于确定性。"', '"Une forte probabilité n’est pas une certitude."', 1)
rep([C7], '"LA PROSSIMA SETTIMANA · 下期预告 (VOL.3)"', '"LA PROSSIMA SETTIMANA · LA SEMAINE PROCHAINE (VOL.3)"', 1)

# ---------- printed instructions (instr= values sit beside exercise numbers) ----------
rep(ALL, 'instr="填空"', 'instr="Compléter"')
rep(ALL, 'instr="造句"', 'instr="Former une phrase"')
rep(ALL, 'instr="判断"', 'instr="Vrai ou faux"')
rep(ALL, 'instr="把词和释义配对"', 'instr="Associer"')
rep(ALL, 'instr="写作"', 'instr="Écrire"')
# P8 E-section re-aiming (W43 IT x FR ruling): items 1-3 are IT->FR
# (French keys, Italian bodies unchanged); item 4 is FR->IT (French body,
# Italian key byte-identical).
rep([C8], 'f.ex("A2", "翻译", "周一第一场寒冷来了。", "对照原文",\n     "Lunedì arriva il primo freddo. → ___", instr="翻译"',
    'f.ex("A2", "翻译", "Lundi, le premier froid arrive.", "Comparer avec l’original.",\n     "Lunedì arriva il primo freddo. → ___", instr="Traduire en français"', 1)
rep([C8], 'f.ex("B1", "翻译", "观众可以免费品尝。", "assaggiare gratis = 免费品尝",\n     "Il pubblico può assaggiare gratis. → ___", instr="翻译"',
    'f.ex("B1", "翻译", "Le public peut déguster gratuitement.", "assaggiare gratis = déguster gratuitement",\n     "Il pubblico può assaggiare gratis. → ___", instr="Traduire en français"', 1)
rep([C8], 'f.ex("B1", "翻译", "周日晚上，佛罗伦萨对尤文图斯。", "si gioca = 进行比赛",\n     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="翻译"',
    'f.ex("B1", "翻译", "Dimanche soir, on joue Fiorentina–Juventus.", "si gioca = on joue",\n     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="Traduire en français"', 1)
rep([C8], 'f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = 必须",\n     "每个预报都必须清楚。→ ___", instr="翻译"',
    'f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = devoir",\n     "Chaque prévision doit être claire. → ___", instr="Traduire en italien"', 1)

# ---------- exercise notes, pages 1-2 (printed on P8) ----------
rep([C12], '"il primo freddo = 第一场寒冷"', '"il primo freddo = le premier froid"', 1)
rep([C12], '"la prima neve leggera = 初雪"', '"la prima neve leggera = les premières neiges légères"', 1)
rep([C12], '"文化论坛与潘妮托尼决赛都在米兰"', '"Le Forum Cultura et la finale du Panettone sont tous deux à Milan"', 1)
rep([C12], '"克雷莫纳的节日叫 Festa del Torrone"', '"La fête de Crémone est la Festa del Torrone"', 1)
rep([C12], '"previsioni = 预报（复数）"', '"previsioni = prévisions (pluriel)"', 1)
rep([C12], '"第一场寒冷在周一 11 月 2 日到来"', '"Le premier froid arrive lundi 2 novembre"', 1)
rep([C12], '"初雪在 1300–1500 米左右"', '"Les premières neiges tombent vers 1 300-1 500 mètres"', 1)
rep([C12], '"潘妮托尼决赛在米兰"', '"La finale du Panettone est à Milan"', 1)
rep([C12], '"意甲第 11 轮周日收官"', '"La 11e journée de Serie A se termine dimanche"', 2)
rep([C12], '"cappotto = 大衣"', '"cappotto = manteau"', 1)
rep([C12], '"sciarpa = 围巾"', '"sciarpa = écharpe"', 1)
rep([C12], '"guanti = 手套（复数）"', '"guanti = gants (pluriel)"', 1)
rep([C12], '"crisantemi = 菊花（复数）"', '"crisantemi = chrysanthèmes (pluriel)"', 1)
rep([C12], '"termosifoni = 暖气片（复数）"', '"termosifoni = radiateurs (pluriel)"', 1)
rep([C12], '"fare freddo：fa freddo（天气）"', '"fare freddo : fa freddo (météo)"', 1)
rep([C12], '"mettere：io → metto"', '"mettere : io donne metto"', 1)
rep([C12], '"portare：loro → portano"', '"portare : loro donne portano"', 1)
rep([C12], '"guardare：loro → guardano"', '"guardare : loro donne guardano"', 1)
rep([C12], '"restare：la scuola → resta（lei）"', '"restare : la scuola donne resta (lei)"', 1)
rep([C12], '"11 月 2 日是追思日"', '"Le 2 novembre est la commémoration des défunts"', 1)
rep([C12], '"追思日的花是菊花"', '"La fleur de la commémoration des défunts est le chrysanthème"', 1)
rep([C12], '"分层穿衣：a strati"', '"S’habiller en couches superposées : a strati"', 1)
rep([C12], '"诸圣节今年是周日、无连休"', '"La Toussaint tombe un dimanche cette année, donc pas de long week-end"', 1)
rep([C12], '"cappotto=御寒大衣 c"', '"cappotto = manteau chaud d’hiver, c"', 1)
rep([C12], '"sciarpa=围巾 d"', '"sciarpa = écharpe, d"', 1)
rep([C12], '"crisantemo=十一月的花 a"', '"crisantemo = fleur de novembre, a"', 1)
rep([C12], '"termosifone=暖气片 b"', '"termosifone = radiateur, b"', 1)

# ---------- exercise notes, pages 3-4 ----------
rep([C34], '"潘妮托尼决赛在米兰"', '"La finale du Panettone est à Milan"', 1)
rep([C34], '"克雷莫纳牛轧糖节到 11 月 22 日"', '"La fête du torrone de Crémone dure jusqu’au 22 novembre"', 1)
rep([C34], '"潘妮托尼决赛有 19 国糕点师"', '"19 pays envoient des pâtissiers à la finale du Panettone"', 1)
rep([C34], '"文化论坛 11 月 3 日周二开幕"', '"Le Forum Cultura ouvre mardi 3 novembre"', 1)
rep([C34], '"阿尔巴松露节到 12 月 6 日"', '"La foire de la truffe d’Alba dure jusqu’au 6 décembre"', 1)
rep([C34], '"panettone = 米兰圣诞面包"', '"panettone = gâteau de Noël milanais"', 1)
rep([C34], '"torrone = 牛轧糖"', '"torrone = nougat"', 1)
rep([C34], '"assaggio = 品尝"', '"assaggio = dégustation"', 1)
rep([C34], '"bancarella = 摊位"', '"bancarella = étal"', 1)
rep([C34], '"mandorle = 杏仁（复数）"', '"mandorle = amandes (pluriel)"', 1)
rep([C34], '"tartufo = 松露"', '"tartufo = truffe"', 1)
rep([C34], '"arrivare 用 essere：è arrivato"', '"arrivare prend essere : è arrivato"', 1)
rep([C34], '"assaggiare 用 avere：abbiamo assaggiato"', '"assaggiare prend avere : abbiamo assaggiato"', 1)
rep([C34], '"andare 用 essere，复数 sono andati"', '"andare prend essere, pluriel sono andati"', 1)
rep([C34], '"aprire 用 avere：ha aperto"', '"aprire prend avere : ha aperto"', 1)
rep([C34], '"主语 + essere + 地点 + 日期"', '"Sujet + essere + lieu + date"', 1)
rep([C34], '"地点在前，主语在后"', '"Lieu d’abord, sujet ensuite"', 1)
rep([C34], '"dura fino a = 持续到"', '"dura fino a = dure jusqu’à"', 1)
rep([C34], '"意甲第 11 轮周日收官"', '"La 11e journée de Serie A se termine dimanche"', 1)
rep([C34], '"周日晚上佛罗伦萨对尤文图斯"', '"Fiorentina joue contre Juventus dimanche soir"', 1)
rep([C34], '"欧战第 4 轮在 11 月 3–5 日"', '"La 4e journée européenne a lieu du 3 au 5 novembre"', 1)
rep([C34], '"欧战比赛只作前瞻、无结果"', '"Les matchs européens ne sont ici que des avant-premières, sans résultats"', 1)
rep([C34], '"国米对科莫在圣西罗"', '"Inter joue contre Como à San Siro"', 1)
rep([C34], '"giornata=联赛的一轮 c"', '"giornata = une journée de championnat, c"', 1)
rep([C34], '"presentazione=赛前介绍 b"', '"presentazione = présentation d’avant-match, b"', 1)
rep([C34], '"spalti=看台 a"', '"spalti = tribunes, a"', 1)
rep([C34], '"sera=晚上 d"', '"sera = soir, d"', 1)
rep([C34], '"周日晚上的比赛晚于周五的：più tardi"', '"Les matchs du dimanche soir sont plus tardifs que ceux du vendredi : più tardi"', 1)
rep([C34], '"周五的比赛早于周日的：più presto"', '"Les matchs du vendredi sont plus précoces que ceux du dimanche : più presto"', 1)
rep([C34], '"più + bella 周日晚最美（主观评价）"', '"più + bella : le dimanche soir est le plus beau (un jugement)"', 1)
rep([C34], '"bene 的比较级是不规则的 meglio"', '"Le comparatif de bene est l’irrégulier meglio"', 1)
rep([C34], '"vincere：ha vinto"', '"vincere : ha vinto"', 1)
rep([C34], '"pareggiare：ha pareggiato"', '"pareggiare : ha pareggiato"', 1)
rep([C34], '"arrivare 用 essere，复数 sono arrivati"', '"arrivare prend essere, pluriel sono arrivati"', 1)
rep([C34], '"guardare 用 avere：abbiamo guardato"', '"guardare prend avere : abbiamo guardato"', 1)
rep([C34], '"prendere 的分词是 preso：ha preso"', '"Le participe de prendere est preso : ha preso"', 1)

# ---------- exercise notes, pages 5-6 ----------
rep([C56], '"卢卡漫画节是第 60 届"', '"Lucca Comics en est à sa 60e édition"', 1)
rep([C56], '"文化论坛 11 月 3 日开幕"', '"Le Forum Cultura ouvre le 3 novembre"', 1)
rep([C56], '"民俗电影节在佛罗伦萨"', '"Le Festival dei Popoli est à Florence"', 2)
rep([C56], '"文化论坛有 50 多场活动"', '"Le Forum Cultura propose plus de 50 événements"', 2)
rep([C56], '"卢卡漫画节主题是 Legacy"', '"Le thème de Lucca Comics est Legacy"', 1)
rep([C56], '"armadio = 衣柜"', '"armadio = armoire"', 1)
rep([C56], '"gratuiti = 免费的（阳性复数）"', '"gratuiti = gratuits (masculin pluriel)"', 1)
rep([C56], '"documentario = 纪录片"', '"documentario = documentaire"', 1)
rep([C56], '"schermo = 银幕"', '"schermo = écran"', 1)
rep([C56], '"castagne arrosto 烤栗子（复数）"', '"castagne arrosto = marrons grillés (pluriel)"', 1)
rep([C56], '"cosplay = 角色扮演服装"', '"cosplay = costume de cosplay"', 1)
rep([C56], '"andare 将来时 noi：andremo"', '"andare, futur noi : andremo"', 1)
rep([C56], '"esserci 将来时：ci sarà（将有）"', '"esserci, futur : ci sarà (il y aura)"', 1)
rep([C56], '"guardare 将来时 noi：guarderemo"', '"guardare, futur noi : guarderemo"', 1)
rep([C56], '"durare 将来时：durerà"', '"durare, futur : durerà"', 1)
rep([C56], '"卢卡漫画节到 11 月 8 日才结束是错的"', '"Lucca Comics se terminant le 8 novembre est faux"', 1)
rep([C56], '"示例数据中最冷的是都灵 3°"', '"La ville la plus froide des données d’exemple est Turin, avec 3°"', 1)
rep([C56], '"示例数据中最暖的是那不勒斯 12°"', '"La ville la plus chaude des données d’exemple est Naples, avec 12°"', 1)
rep([C56], '"12 − 9 = 3"', '"12 moins 9 = 3"', 1)
rep([C56], '"4 + 5 = 9"', '"4 plus 5 = 9"', 1)
rep([C56], '"图表数据是练习用的、不是真实预报"', '"Les chiffres du graphique sont des données d’exercice, pas de vraies prévisions"', 1)
rep([C56], '"高概率不等于确定"', '"Une forte probabilité n’est pas une certitude"', 1)
rep([C56], '"预报基于 ECMWF 等模型"', '"Les prévisions reposent sur des modèles comme l’ECMWF"', 1)
rep([C56], '"预报会变，因为大气变化快"', '"Les prévisions changent parce que l’atmosphère change vite"', 1)
rep([C56], '"DPB 于 10 月 15 日送布鲁塞尔"', '"Le DPB est parti pour Bruxelles le 15 octobre"', 1)
rep([C56], '"2027 增长预测 +0,8%"', '"Prévision de croissance pour 2027 : +0,8 %"', 1)
rep([C56], '"è probabile che + 虚拟式 piova"', '"è probabile che + subjonctif piova"', 1)
rep([C56], '"è possibile che + 虚拟式 nevichi"', '"è possibile che + subjonctif nevichi"', 1)
rep([C56], '"bisogna che + 虚拟式 controllino"', '"bisogna che + subjonctif controllino"', 1)
rep([C56], '"è importante che + 虚拟式 sia"', '"è importante che + subjonctif sia"', 1)
rep([C56], '"probabilità = 概率"', '"probabilità = probabilité"', 1)
rep([C56], '"media = 平均值"', '"media = moyenne"', 1)
rep([C56], '"bollettino = 预报公报"', '"bollettino = bulletin de prévision"', 1)
rep([C56], '"modello = 预报模型"', '"modello = modèle de prévision"', 1)

# ---------- exercise notes, page 7 ----------
rep([C7], '"piovere 天气动词：piove"', '"piovere, verbe météorologique : piove"', 1)
rep([C7], '"fa freddo = 天气冷"', '"fa freddo = il fait froid"', 1)
rep([C7], '"nevicare：nevica"', '"nevicare : nevica"', 1)
rep([C7], '"“我冷”说 ho freddo"', '"« J’ai froid » se dit ho freddo"', 1)
rep([C7], '"arrivare 用 essere：è arrivato"', '"arrivare prend essere : è arrivato"', 1)
rep([C7], '"assaggiare 用 avere"', '"assaggiare prend avere"', 1)
rep([C7], '"andare 用 essere，复数 sono andati"', '"andare prend essere, pluriel sono andati"', 1)
rep([C7], '"aprire 用 avere + 不变分词"', '"aprire prend avere + participe invariable"', 1)
rep([C7], '"è probabile che + 虚拟式 piova"', '"è probabile che + subjonctif piova"', 1)
rep([C7], '"è possibile che + 虚拟式 nevichi"', '"è possibile che + subjonctif nevichi"', 1)
rep([C7], '"bisogna che + 虚拟式 sia"', '"bisogna che + subjonctif sia"', 1)
rep([C7], '"so che + 陈述式 arriva"', '"so che + indicatif arriva"', 1)

# ---------- exercise notes, page 8 ----------
rep([C8], '"primo freddo = 第一场寒冷"', '"primo freddo = le premier froid"', 1)
rep([C8], '"追思日在 11 月 2 日"', '"La commémoration des défunts a lieu le 2 novembre"', 1)
rep([C8], '"文化论坛在米兰开幕"', '"Le Forum Cultura ouvre à Milan"', 1)
rep([C8], '"潘妮托尼决赛在周六日"', '"La finale du Panettone a lieu samedi et dimanche"', 1)
rep([C8], '"牛轧糖节在克雷莫纳"', '"La fête du torrone est à Crémone"', 1)
rep([C8], '"意甲第 11 轮周日收官：chiude"', '"La 11e journée de Serie A se termine dimanche : chiude"', 1)
rep([C8], '"佛罗伦萨对尤文图斯在周日晚上"', '"Fiorentina joue contre Juventus dimanche soir"', 1)
rep([C8], '"民俗电影节在佛罗伦萨"', '"Le Festival dei Popoli est à Florence"', 1)
rep([C8], '"初雪在 1300–1500 米左右"', '"Les premières neiges tombent vers 1 300-1 500 mètres"', 1)
rep([C8], '"追思日的花是菊花"', '"La fleur de la commémoration des défunts est le chrysanthème"', 1)
rep([C8], '"潘妮托尼决赛有 19 国糕点师"', '"19 pays envoient des pâtissiers à la finale du Panettone"', 1)
rep([C8], '"文化论坛有 50 多场活动"', '"Le Forum Cultura propose plus de 50 événements"', 1)
rep([C8], '"阿尔巴松露节到 12 月 6 日"', '"La foire de la truffe d’Alba dure jusqu’au 6 décembre"', 1)
rep([C8], '"DPB 于 10 月 15 日送出"', '"Le DPB est parti le 15 octobre"', 1)
rep([C8], '"概率不等于确定"', '"Une probabilité n’est pas une certitude"', 1)
rep([C8], '"卢卡漫画节 11 月 1 日闭幕"', '"Lucca Comics a fermé le 1er novembre"', 1)
rep([C8], '"Giulia 去米兰潘妮托尼决赛"', '"Giulia va à la finale du Panettone à Milan"', 1)
rep([C8], '"Paolo 周六去牛轧糖节"', '"Paolo va à la fête du torrone samedi"', 1)
rep([C8], '"传统潘妮托尼是 Giulia 品尝的"', '"Le panettone traditionnel est dégusté par Giulia"', 1)
rep([C8], '"标题概括两个城市、两个节日"', '"Le titre résume deux villes, deux douceurs"', 1)
rep([C8], '"时间词在前"', '"Le mot de temps d’abord"', 1)
rep([C8], '"主语 + essere + 地点 + 日期"', '"Sujet + essere + lieu + date"', 1)
rep([C8], '"疑问词组在句首"', '"Le groupe interrogatif d’abord"', 1)
rep([C8], '"主语 + 动词 + 时间"', '"Sujet + verbe + temps"', 1)
rep([C8], '"probabilità=可能性 d"', '"probabilità = possibilité, d"', 1)
rep([C8], '"media=平均值 a"', '"media = moyenne, a"', 1)
rep([C8], '"bollettino=预报公报 b"', '"bollettino = bulletin de prévision, b"', 1)
rep([C8], '"modello=预报模型 c"', '"modello = modèle de prévision, c"', 1)
rep([C8], '"torrone = 牛轧糖"', '"torrone = nougat"', 1)
rep([C8], '"mandorle 杏仁"', '"mandorle = amandes"', 1)
rep([C8], '"quanto costa? 多少钱"', '"quanto costa ? = combien ça coûte ?"', 1)
rep([C8], '"pagare con carta 刷卡"', '"pagare con carta = payer par carte"', 1)
rep([C8], '"牛轧糖节持续到 11 月 22 日"', '"La fête du torrone dure jusqu’au 22 novembre"', 1)
# P8 H writing bridge + writing item (key is not printed for writing items;
# the note is printed as "150. ✓ <note>").
rep([C8], 'f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")',
    'f.bridge(f"Exercice d’écriture (pas de réponse unique) ; le texte modèle ({NWORDS} mots) suit.")', 1)
rep([C8], '"（开放题，范文如下）"', '"(exercice ouvert — texte modèle ci-dessous)"', 1)
rep([C8], 'f"范文见本版 H 区（{NWORDS} 词）"', 'f"Texte modèle dans la section H ci-dessous ({NWORDS} mots)"', 1)
# P8 answer-key titles (W43 IT x FR shipped strings; separators stay Italian)
rep([C8], '"RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可"',
    '"RISPOSTE · CORRIGÉS — classés par page, cherchez le numéro"', 1)
rep([C8], '"每题附一句中文简析 · 带 ✓ 的为范文题"',
    '"Chaque réponse est accompagnée d’une note d’une ligne en français · ✓ = exercice du texte modèle"', 1)

print('TRANSFORM COMPLETE')

# ---------- FIX ROUND 1 (round-1 render: P1-headline overflow, P7 col3 1789.5, box-title crossings) ----------
# All trims are wording-only, verified with the build's own wrap() to
# restore the CORE's line counts exactly (no layout parameter changes
# except the two tsize notes, both W43 IT x FR precedents).
# (a) P1 bridge 4 lines -> 3 (core 3): drop "la" before previsione and
# gloss assaggi with the generic singular "dégustation".
rep([C12], '"Notes : il primo freddo, le premier froid · il versante adriatico, le versant adriatique · la previsione, prévision · assaggi, dégustations."',
    '"Notes : il primo freddo, le premier froid · il versante adriatico, versant adriatique · previsione, prévision · assaggi, dégustation."', 1)
# (b) P1 cifre #2 4 lines -> 3 (core 3); #4 3 lines -> 2 (core 2).
rep([C12], '(plus de 50 événements du Forum Cultura à Milan, du 3 au 8 novembre)', '(50+ événements à Milan du 3 au 8 novembre)', 1)
# (c) CIFRE box title ink 446.8px > 416px slot at tsize 23 -> tsize=20
# (W43 IT x FR precedent for this exact title), ink ~388px.
rep([C12], '("11ª — la giornata di Serie A del fine settimana(11e journée de Serie A ce week-end)", "serif", False, INK, 20.5, 1.35),\n])',
    '("11ª — la giornata di Serie A del fine settimana(11e journée de Serie A)", "serif", False, INK, 20.5, 1.35),\n], tsize=20)', 1)
# (d) LA SETTIMANA diary subtitle ink 436.2px > 412px box slot ->
# "Semaine · ..." (387.8px, 24px margin).
rep([C12], '"Cette semaine · Cosa succede, giorno per giorno"', '"Semaine · Cosa succede, giorno per giorno"', 1)
# (e) LA SETTIMANA French footer note is a single p.text line: ink
# 569.0px > 412px slot -> 377.5px version.
rep([C12], '"Dates selon les calendriers des événements ; les horaires peuvent changer."',
    '"Dates selon les calendriers ; horaires modifiables."', 1)
# (f) P1 parola gloss 2 lines -> 1: the 2-line gloss's second line would
# be struck by the row-B rule at y=1864 (IT x EN fix-round-2 precedent).
rep([C12], '"« Il primo freddo » : le froid après un automne doux."',
    '"« Il primo freddo » : froid après un automne doux."', 1)
# (g) P7 errori #2 2 lines -> 1 (core 1).
rep([C7], '"Nevicare : 3e personne du singulier seulement."', '"Nevicare : 3e personne seulement."', 1)
# (h) P7 parola gloss 3 lines -> 2 (core 2).
rep([C7], '"assaggio = dégustation. Voir page 3 : dégustation gratuite à la finale du Panettone."',
    '"assaggio = dégustation. Voir page 3 : dégustation gratuite au Panettone."', 2)
# (i) P7 letter note 5 lines -> 3 (core 3), keeping all three disclosure
# facts (editor's sample, no real letters yet, no best page-8 essay yet,
# both promised for VOL.3) + the imperative invitation.
rep([C7], '"Exemple de la rédaction, pas une vraie lettre : pas encore de vraies lettres, pas encore de meilleur texte de la page 8 — les deux sont promis pour le VOL.3. Écrivez-nous !"',
    '"Exemple de rédaction, pas une vraie lettre : pas encore de lettres ni de meilleur texte page 8, promis au VOL.3. Écrivez-nous !"', 2)

print('TRANSFORM COMPLETE (WITH FIX ROUND 1)')

# ---------- FIX ROUND 2 (P8-keys overflow: 7 items past the footer) ----------
# Wording-only trims of P8 answer notes, each verified with the build's
# own wrap() to drop its answer from 2 lines to 1 (13pt serif, width 434,
# saving 14.82px each). 14 cuts = ~207px against a ~193px excess; items
# 138/139 (re-aimed translation keys) stay 2 lines — their keys and
# notes are already minimal and must not be distorted.
rep([C12], '"Le Forum Cultura et la finale du Panettone sont tous deux à Milan"',
    '"Forum Cultura et Panettone : tous deux à Milan"', 1)
rep([C12, C8], '"La fleur de la commémoration des défunts est le chrysanthème"',
    '"Fleur de la commémoration des défunts : le chrysanthème"', 2)
rep([C12], '"La Toussaint tombe un dimanche cette année, donc pas de long week-end"',
    '"Toussaint 2026 : un dimanche, pas de long week-end"', 1)
rep([C34], '"assaggiare prend avere : abbiamo assaggiato"', '"assaggiare prend avere"', 1)
rep([C34], '"Les matchs européens ne sont ici que des avant-premières, sans résultats"',
    '"Matchs européens : avant-premières ici, sans résultats"', 1)
rep([C34], '"Les matchs du dimanche soir sont plus tardifs que ceux du vendredi : più tardi"',
    '"Matchs du dimanche soir, plus tardifs : più tardi"', 1)
rep([C34], '"Les matchs du vendredi sont plus précoces que ceux du dimanche : più presto"',
    '"Matchs du vendredi, plus précoces : più presto"', 1)
rep([C34], '"più + bella : le dimanche soir est le plus beau (un jugement)"',
    '"più + bella : le dimanche soir est le plus beau"', 1)
rep([C56], '"La ville la plus froide des données d’exemple est Turin, avec 3°"',
    '"Ville la plus froide des données d’exemple : Turin, 3°"', 1)
rep([C56], '"La ville la plus chaude des données d’exemple est Naples, avec 12°"',
    '"Ville la plus chaude des données d’exemple : Naples, 12°"', 1)
rep([C56], '"Les chiffres du graphique sont des données d’exercice, pas de vraies prévisions"',
    '"Graphique : données d’exercice, pas de vraies prévisions"', 1)
rep([C56], '"Les prévisions changent parce que l’atmosphère change vite"',
    '"Les prévisions changent, l’atmosphère change vite"', 1)
rep([C8], '"Le groupe interrogatif d’abord"', '"Interrogatif d’abord"', 1)

print('TRANSFORM COMPLETE (WITH FIX ROUNDS 1-2)')

# ---------- FIX ROUND 3 (occlusion audit: 1 NEW BOXTITLE, P7 parola) ----------
# The 2-line parola gloss's second line ended in Latin descenders
# ("gratuite", "Panettone") whose ink bottom (1314.0) grazed 0.5px past
# the box border (1313.5) — pixel-confirmed on the P7 card (border line
# through the descender tails). The core's 2-line Chinese gloss passes
# only because CJK ink has no Latin descenders. Fix: reword the gloss
# so its verified wrap puts a descender-free line 2 ("du Panettone.")
# under the same 2-line geometry — col3 still ends exactly 1673.0.
rep([C7], '"assaggio = dégustation. Voir page 3 : dégustation gratuite au Panettone."',
    '"assaggio = dégustation. Voir page 3, finale du Panettone."', 2)

print('TRANSFORM COMPLETE (WITH FIX ROUNDS 1-3)')

# ---------- FIX ROUND 4 (W43 furniture byte-fidelity: badge apostrophe) ----------
# The shipped W43 IT x FR badge uses an ASCII apostrophe in L'ÉDITION;
# round 1 used U+2019. Furniture strings follow the shipped SVG byte
# for byte, so switch to ASCII '. Width impact ~1px; geometry unchanged.
rep([C12], "L’ÉDITION POUR LES LECTEURS FRANCOPHONES", "L'ÉDITION POUR LES LECTEURS FRANCOPHONES", 1)

print('TRANSFORM COMPLETE (WITH FIX ROUNDS 1-4)')
