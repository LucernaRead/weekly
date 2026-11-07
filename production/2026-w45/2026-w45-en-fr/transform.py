# -*- coding: utf-8 -*-
"""Transform the W45 EN core build into the EN x FR fan-out build.

Source of truth: hidden_files/weekly-report-w45-en-build (W45 EN core,
VOL.2). Output: hidden_files/weekly-report-w45-en-fr-build (this tree's
siblings) whose OUT points at files/weekly-report-w45-en-fr/svg.

Rules applied here (every later fix round edits THIS file, never the
generated content files directly, then re-runs it + run.py + render.py):
- English body text is copied byte-identical; only the explanation layer
  (Chinese glosses, notes, instructions, section-head French halves,
  footers, page lines, P8 answer notes) is replaced by French.
- The banned intermediary term never appears: the library method
  bridge() is renamed instrline() (W43 ENxFR precedent) and every
  "讲解｜" gloss/instruction prefix becomes "Note | " (gloss boxes via
  the library prefix; instruction lines carry it explicitly).
- Same-pairing furniture follows the shipped W43 ENxFR SVGs
  (files/weekly-report-en-fr/svg), NOT the tables.json generalisations:
  badge "TEXTE EN ANGLAIS ...", footer "HEBDOMADAIRE ANGLAIS VOL.2 ...",
  page line "Page N sur 8", gloss prefix "Note | ", P1 badge in the
  y=372 slot at 19.5pt BRICK, P1 edition line at y=330.
- P8 keys print ALL notes in half-width parens at 13.5pt/1.26, separators
  "— Page N —", keys flow bottom 2530 (W43 ENxFR pattern).
- P7 word boxes / golden sentences: English definition sentences and
  golden-sentence originals stay verbatim; only glosses/notes localise.
- Readers' corner: the core's English example quote stays verbatim; the
  Chinese disclosure paragraph becomes the French disclosure (3 facts +
  imperative invitation + VOL.3 promise). No reader, letter, name or
  quotation is invented.
- P8 translation items 137-140: the core's four prompts are all English
  sentences with Chinese keys (EN->ZH in this core; items 138/139 merely
  use the Chinese instruction word). The FR edition renders all four as
  EN->FR with French keys (see REPL content8.py).
"""
import os
import shutil
import sys

CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w45-en-build")
DST = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w45-en-fr-build")
EDITION = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w45-en-fr/svg")

# (old, new) — applied in order; each must occur exactly once unless
# the entry is a (old, new, count) triple.
BSLIB = [
    ("The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY",
     "The Lucerna · HEBDOMADAIRE ANGLAIS VOL.2 · TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS"),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} sur {total}"'),
    ('("译注｜" + s', '("Note | " + s'),
    ("def bridge(self, s", "def instrline(self, s"),
]

CONTENT12 = [
    ("WEEKLY IN ENGLISH · 每周一期 · 读美国人正在读的英语",
     "WEEKLY IN ENGLISH · Chaque semaine · L’anglais que lit l’Amérique"),
    ("英 语 周 报 · VOL.2 · 选 票 · 足 球 · 电 影",
     "HEBDOMADAIRE EN ANGLAIS · VOL.2 · ÉLECTIONS · FOOTBALL · CINÉMA"),
    # P1 badge replaces the y=372 strapline slot (W43 ENxFR geometry).
    ('"THE LEARNERS\' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA", 19, "sans", False, GREY, anchor="middle"',
     '"TEXTE EN ANGLAIS · EXPLICATIONS EN FRANÇAIS — L’ÉDITION POUR LES LECTEURS FRANCOPHONES", 19.5, "sans", True, BRICK, anchor="middle"'),
    ("周二选举日 · 周日已拨回时钟", "ÉLECTIONS MARDI · HORLOGES RECULÉES"),
    ("11 月 3 日周二选举日 · 详见第 6 版", "Mardi 3 novembre, jour des élections · page 6"),
    ("THE BIG STORY · 头条", "THE BIG STORY · À la une"),
    ("讲解｜a midterm 中期选举 · a ballot 选票 · a race 一场竞选 · to call a race 宣布某场竞选的结果。",
     "Note | a midterm = mi-mandat · a ballot = bulletin de vote · a race = course électorale · to call a race = annoncer le résultat."),
    ("THE WEEK IN NUMBERS · 数字看本周", "THE WEEK IN NUMBERS · Chiffres"),
    ("Nov 3 — Election Day（选举日） · 435 — seats in the House, all on the ballot（众议院全部席位改选）",
     "Nov 3 — Election Day (jour des élections) · 435 — seats in the House, all on the ballot (tous les sièges en jeu)"),
    ("Nov 6 — two films open（两部电影上映） · Nov 8 — NFL in Madrid + F1 in São Paulo（周日两场大赛）",
     "Nov 6 — two films open (deux films) · Nov 8 — NFL in Madrid + F1 in São Paulo (deux rendez-vous dimanche)"),
    ("TRY IT NOW · 即学即练", "TRY IT NOW · À vous de jouer"),
    ("ballot = 纸选票", "ballot = le bulletin de vote"),
    ("midterm = 中期（选举）", "midterm = une élection de mi-mandat"),
    ("选举日 11 月 3 日（周二）", "Le jour des élections, mardi 3 novembre"),
    ("early voting = 提前投票", "early voting = le vote anticipé"),
    ("race called = 宣布结果", "race called = résultat annoncé"),
    ("take time = 花时间", "take time = prendre du temps"),
    ("本周美国热搜 · Google Trends 美国区快照", "Recherches de la semaine · Google Trends"),
    ("相对热度示意，非精确搜索量。", "Intérêt relatif, pas des volumes exacts."),
    ("IN THIS ISSUE · 本期目录", "IN THIS ISSUE · Sommaire"),
    # One-line French gloss on purpose: keeps the core geometry
    # (gloss baseline my+168, row-B rule 1844) untouched.
    ("（任期）中期。midterm election 中期选举。", "midterm election = une élection de mi-mandat."),
    ("IN BRIEF · 快讯", "IN BRIEF · En bref"),
    ("LIGHTNING QUIZ · 闪电问答", "LIGHTNING QUIZ · Quiz éclair"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Lisez la une, choisissez la bonne réponse · Réponses page 8"),
    ("选举日 11 月 3 日周二", "Le jour des élections : mardi 3 novembre"),
    ("众议院 435 席全部改选", "Les 435 sièges de la Chambre sont en jeu"),
    ("美国 11 月 1 日拨回时钟", "L’Amérique a reculé ses horloges le 1er novembre"),
    ("NFL 马德里赛 11 月 8 日周日", "Le match NFL à Madrid : dimanche 8 novembre"),
    ("LIFE · 生活", "LIFE · La vie"),
    ("LEVEL A2 · Clocks, candy & your week · 时钟、糖果与你的一周",
     "LEVEL A2 · Clocks, candy & your week · Les horloges, les bonbons et votre semaine"),
    ("DO THE MATHS · 算一算", "DO THE MATHS · À vous de calculer"),
    ("讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。",
     "to fall back = reculer (les horloges) · a costume = un déguisement · trick or treat = des bonbons ou un sort."),
    ("周日你多睡了一小时吗？写两句英语寄给编辑部。",
     "Avez-vous dormi une heure de plus dimanche ? Écrivez deux phrases en anglais pour la rédaction.", 2),
    ("AND YOU ? · 说说你自己", "AND YOU ? · Et vous ?"),
    ("TELLING THE TIME · 这样报时间", "TELLING THE TIME · Dire l’heure"),
    ("The repeated hour · 本周的三个时间", "The repeated hour · Les trois heures de la semaine"),
    ("= two times（两次）", "= two times (deux fois)"),
    ("= one more time（再一次）", "= one more time (une fois de plus)"),
    ("= to go back one hour（拨回）", "= to go back one hour (reculer d’une heure)"),
    ("= one hour more（多出一小时）", "= one hour more (une heure de plus)"),
    ("EXERCISES · 第 2 版练习", "EXERCISES · Exercices"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案", "Réponses page 8 · Retrouvez chaque réponse par son numéro"),
    ("根据时间，用英语补全句子。", "D’après l’heure, complétez en anglais."),
    ("1:00 = 一点整", "1:00 = une heure pile"),
    ("1:30 = 一点半", "1:30 = une heure et demie"),
    ("7:45 = 差一刻八点", "7:45 = huit heures moins le quart"),
    ("两次 = twice", "deux fois = twice"),
    ("多出的 = extra", "en plus = extra"),
    ("用 be going to + 动词改写（计划与将要发生的事）。",
     "Réécrivez avec be going to + verbe (un projet, un événement à venir)."),
    ("Americans 复数 → are going to", "Americans, pluriel → are going to"),
    ("疑问句：be 提前", "Question : be en tête"),
    ("读第 2 版文章，选出正确答案。", "Lisez la page 2 et choisissez."),
    ("11 月 1 日凌晨 2 点拨回 1 点", "Le 1er novembre, à 2 h, on recule à 1 h"),
    ("亚利桑那与夏威夷不拨钟", "L’Arizona et Hawaï ne changent pas d’heure"),
    ("万圣节 10 月 31 日周六", "Halloween : samedi 31 octobre"),
    ("11 月 1 日夜晚有 25 小时", "La nuit du 1er novembre compte 25 heures"),
    ("costume=装扮 b", "costume = un déguisement b"),
    ("extra hour=多出一小时 a", "extra hour = une heure de plus a"),
    ("fall back=拨回 d", "fall back = reculer d"),
    ("trick or treat=不给糖就捣蛋 c", "trick or treat = des bonbons ou un sort c"),
]

CONTENT34 = [
    ("CULTURE · 文化", "CULTURE · Culture"),
    ("A2 → B1 · Friday at the movies · 周五看电影", "A2 → B1 · Friday at the movies · Vendredi au cinéma"),
    ("AT HOME THIS WEEK · 在家看什么", "AT HOME THIS WEEK · À la maison"),
    ("讲解｜to open （电影）上映 · a monster 怪物 · a catchphrase 口头禅、金句 · a series 剧集。",
     "to open = sortir (au cinéma) · a monster = un monstre · a catchphrase = une phrase culte · a series = une série."),
    ("读第 3 版文章，选出正确答案。", "Lisez l’article de la page 3 et choisissez la bonne réponse."),
    ("猫咪电影 11 月 6 日周五上映", "Le film du chat sort vendredi 6 novembre"),
    ("猫出自苏斯博士的书", "Le chat vient d’un livre du Dr Seuss"),
    ("比尔·黑德为猫配音", "Bill Hader est la voix du chat"),
    ("哥斯拉导演是山崎贵", "Le réalisateur de Godzilla est Takashi Yamazaki"),
    ("《黑鸽》第二季 11 月 5 日上线", "La saison 2 de « Black Doves » commence jeudi 5 novembre"),
    ("周日重聚节目收尾", "L’émission de retrouvailles clôt la semaine"),
    ("用所给词补全句子。", "Complétez la phrase avec le mot donné.", 2),
    ("open = 上映（第三人称单数加 s）", "open = sortir ; à la 3e personne, opens"),
    ("tall → taller 比较级", "tall → taller (comparatif)"),
    ("split = 分歧的", "split = partagé"),
    ("monster=怪物 b", "monster = un monstre b"),
    ("catchphrase=金句 a", "catchphrase = une phrase culte a"),
    ("series=剧集 d", "series = une série d"),
    ("open=上映 c", "open = sortir (au cinéma) c"),
    ("用 be going to 改写。", "Réécrivez avec be going to."),
    ("疑问句：be 提前", "Question : be en tête"),
    ("THE CAT'S HAT · 猫的帽子", "THE CAT'S HAT · Le chapeau"),
    ("五句影评｜who、where、发生了什么、转折、结局——五句就够。",
     "Cinq phrases : qui, où, ce qui s’est passé, le rebondissement, la fin — cinq phrases suffisent."),
    ("SPORT · 体育", "SPORT · Sport"),
    ("WHY MADRID ? · 为什么去马德里？", "WHY MADRID ? · Pourquoi Madrid ?"),
    ("讲解｜a fixture 一场比赛（赛程） · a title 冠军头衔 · to defend （卫冕）保卫头衔 · a fan 球迷。",
     "a fixture = un match au calendrier · a title = le titre de champion · to defend = défendre son titre · a fan = un supporter."),
    ("读第 4 版文章，选出正确答案。", "Lisez l’article de la page 4 et choisissez la bonne réponse."),
    ("马德里赛：孟加拉虎对猎鹰", "À Madrid : les Bengals contre les Falcons"),
    ("马德里赛场是伯纳乌", "Le match de Madrid a lieu au Bernabéu"),
    ("海豚对雄狮在迈阿密", "Les Dolphins contre les Lions à Miami"),
    ("F1 圣保罗大奖赛在巴西", "Le Grand Prix de São Paulo a lieu au Brésil"),
    ("WTA 年终总决赛在印第安维尔斯开赛", "Les WTA Finals commencent à Indian Wells"),
    ("拳击赛在阿灵顿", "Le combat de boxe a lieu à Arlington"),
    ("defend 三单加 s", "defend → defends, 3e personne"),
    ("与第 4 版原文一致，复数动词", "Comme dans le texte de la page 4 : verbe au pluriel"),
    ("fixture=赛程中的比赛 b", "fixture = un match au calendrier b"),
    ("title=冠军头衔 d", "title = le titre de champion d"),
    ("fan=球迷 a", "fan = un supporter a"),
    ("defend=卫冕 c", "defend = défendre son titre c"),
    ("用一般过去时改写（比赛已结束的说法）。", "Réécrivez au prétérit (pour parler d’un match terminé)."),
    ("SUNDAY, NOVEMBER 8 · 周日赛程", "SUNDAY, NOVEMBER 8 · Agenda"),
    ("看球英语｜比分、谁得分、谁领先——短句就是直播英语。",
     "Anglais du match : le score, qui a marqué, qui mène — des phrases courtes, c’est l’anglais en direct."),
]

CONTENT56 = [
    ("YOUTH · 青年", "YOUTH · Jeunesse"),
    ("LEVEL B1 · Election night at home · 选举之夜", "LEVEL B1 · Election night at home · Soirée électorale à la maison"),
    ("TOO CLOSE TO CALL · 难分胜负", "TOO CLOSE TO CALL · Trop serré"),
    ("讲解｜a map （选举）地图 · too close to call 难分胜负、无法判定 · a second screen 第二块屏幕（手机）。",
     "a map = la carte électorale · too close to call = trop serré pour trancher · a second screen = le deuxième écran (le téléphone)."),
    ("读第 5 版文章，选出正确答案。", "Lisez l’article de la page 5 et choisissez la bonne réponse."),
    ("地图随结果逐州变色", "La carte change État par État, au fil des résultats"),
    ("too close to call = 尚不知晓", "too close to call = on ne sait pas encore"),
    ("选举夜常吃披萨", "Le soir des élections, on mange souvent de la pizza"),
    ("第二屏是手机", "Le deuxième écran, c’est le téléphone"),
    ("孩子问为什么这么久", "Les enfants demandent pourquoi c’est si long"),
    ("结果早上还在", "Les résultats seront toujours là le matin"),
    ("close = 接近的", "close = serré"),
    ("still = 仍然", "still = toujours"),
    ("与第 5 版原文一致，单数", "Comme dans le texte de la page 5 : singulier", 2),
    ("map=选举地图 c", "map = la carte électorale c"),
    ("race=一场竞选 d", "race = une course électorale d"),
    ("result=结果 b", "result = le résultat b"),
    ("call=宣布胜者 a", "call = annoncer le vainqueur a"),
    ("用现在进行时改写（正在发生的事）。", "Réécrivez au présent continu (une action en cours)."),
    ("用所给词补全句子。", "Complétez la phrase avec le mot donné.", 2),
    ("FIVE SENTENCES · 五句话作业", "FIVE SENTENCES · Cinq phrases"),
    ("投票结束｜The polls have closed = 该州投票已结束，计票开始。",
     "Fin du vote : The polls have closed = le vote est terminé dans cet État, le dépouillement commence."),
    ("DEEP READ · 时事深读", "DEEP READ · En profondeur"),
    ("LEVEL B2 · How America votes · 美国怎么投票", "LEVEL B2 · How America votes · Comment l’Amérique vote"),
    ("A PRACTICE BALLOT · 模拟选票", "A PRACTICE BALLOT · Bulletin test"),
    ("讲解｜to register 登记（选民登记） · a governor 州长 · to shape laws 影响立法 · patience 耐心。",
     "to register = s’inscrire (sur les listes électorales) · a governor = le gouverneur · to shape laws = influencer les lois · patience = la patience."),
    ("READ THE CHART · 读图表", "READ THE CHART · Graphique"),
    ("读上面的教学图表，选出正确答案。", "Lisez le graphique pédagogique ci-dessus et choisissez la bonne réponse."),
    ("38% 选“不用排队”", "38 % ont choisi « pas de file »"),
    ("工作原因 29%", "Raison « travail » : 29 %"),
    ("四项合计 100%", "Les quatre totalisent 100 %"),
    ("习惯最少 12%", "L’habitude, la plus petite : 12 %"),
    ("不用排队比旅行多 17 个百分点", "« Pas de file » dépasse « voyage » de 17 points"),
    ("图表是教学数据非真实民调", "Le graphique est pédagogique, pas un vrai sondage"),
    ("读第 6 版文章，选出正确答案。", "Lisez l’article de la page 6 et choisissez la bonne réponse."),
    ("各州自行组织选举", "Les élections sont organisées par les États"),
    ("众议员任期两年", "Les députés siègent deux ans"),
    ("参议员任期六年、每次约三分之一改选", "Les sénateurs siègent six ans, un tiers renouvelé à chaque élection"),
    ("邮寄选票计票需时间", "Les bulletins par courrier prennent du temps à dépouiller"),
    ("本期不印民调与预测", "Ce numéro ne publie ni sondage ni prévision"),
    ("耐心是制度的一部分", "La patience fait partie du système"),
    ("shape = 影响、塑造", "shape = influencer, façonner"),
    ("register = 登记", "register = s’inscrire"),
    ("patience = 耐心", "patience = la patience"),
    ("optional = 可选的", "optional = facultatif"),
    ("differ 三单 differs", "differ → differs, 3e personne"),
    ("private = 私密的", "private = privé"),
    ("HOW LONG ? · 任期多长？", "HOW LONG ? · Quelle durée ?"),
    ("一张地图｜五十个州、五十套规则——所以选举夜看的是地图，不是一个数字。",
     "Une carte : cinquante États, cinquante règles — c’est pourquoi, le soir des élections, on regarde une carte, pas un seul chiffre."),
]

CONTENT7 = [
    ("LANGUAGE IN HAND · 精讲", "LANGUAGE IN HAND · La langue en main"),
    ("A2 → B2 · Phrases of the week · 本周金句", "A2 → B2 · Phrases of the week · Les phrases de la semaine"),
    ("LEVEL A2 · 基础", "LEVEL A2 · Les bases"),
    ("THE EXAMPLE · 例句", "THE EXAMPLE · L’exemple", 3),
    ("LEVEL B1 · 进阶", "LEVEL B1 · Plus loin"),
    ("LEVEL B2 · 挑战", "LEVEL B2 · Le défi"),
    ("« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6).",
     "« Patience is part of the system, not a failure of it. » — part of = une partie (page 6)."),
    ("THE TOOLBOX · 工具箱", "THE TOOLBOX · Boîte à outils"),
    ("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。",
     "Boîte à outils : trois phrases de poche, une par niveau ; toutes les phrases de la semaine viennent des articles de ce numéro — relisez l’article, et la phrase devient facile."),
    ("PHRASES OF THE WEEK · 本周金句（全部出自本期文章）",
     "PHRASES OF THE WEEK · Phrases de la semaine (de ce numéro)"),
    ("每句一个语法点 + 一道小题 · 答案见第 8 版",
     "Chaque phrase : un point de grammaire + un petit exercice · Réponses page 8"),
    ("语法点｜is = 是；日期作主语补足语。", "Grammaire : is = est ; la date est sujet."),
    ("is 是", "is = est"),
    ("语法点｜happen 的过去式是 happened，规则变化。", "Grammaire : le prétérit de happen est happened, verbe régulier."),
    ("语法点｜would + 动词原形，表选择意愿。", "Grammaire : would + verbe de base, pour exprimer un choix."),
    ("would + 原形", "would + verbe de base"),
    ("语法点｜that is = 那就是；破折号后总结。", "Grammaire : that is = c’est ; le tiret introduit une conclusion."),
    ("that is 那就是", "that is = c’est"),
    ("语法点｜will still = 仍然会；still 放在 will 之后。", "Grammaire : will still = continuera ; still se place après will."),
    ("will still 仍然会", "will still = continuera"),
    ("语法点｜part of = ……的一部分；not 表否定对照。", "Grammaire : part of = une partie de ; not marque le contraste."),
    ("is part of 一部分", "is part of = une partie de"),
    ("语法点｜not every + 单数动词：并非每处都变。", "Grammaire : not every + verbe au singulier : tous les lieux ne changent pas."),
    ("语法点｜has = 有；the week 单数用 has。", "Grammaire : has = a ; the week, singulier, prend has."),
    ("THE ERROR CLINIC · 易错诊所", "THE ERROR CLINIC · Les erreurs"),
    ("每句有一处错误：找出来并改正。", "Chaque phrase contient une erreur : trouvez-la et corrigez-la."),
    ("三单否定用 doesn't + 原形", "À la 3e personne, doesn’t + verbe de base"),
    ("fall 的过去式是 fell", "Le prétérit de fall est fell"),
    ("bigger 已含比较级，不要再加 more", "bigger est déjà un comparatif : pas de more en plus"),
    ("going to 后用动词原形", "Après going to, le verbe de base"),
    ("READERS' CORNER · 读者园地", "READERS' CORNER · Courrier des lecteurs"),
    # Disclosure in French, per the coordinator ruling: 3 facts (no real
    # letters arrived; no best page-8 writing arrived; the labelled
    # example stays and the promise moves to VOL.3) + an explicit
    # imperative invitation with a VOL.3 publication promise. The core's
    # English example quote above it is kept verbatim; no reader, letter,
    # name or quotation is invented, and no new English disclosure
    # sentence is written (the core has none).
    ("编辑说明｜VOL.1 曾承诺 VOL.2 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.1 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.3 起刊登收到的真实来信。",
     "Note : le VOL.1 avait promis de vraies lettres pour le VOL.2, mais aucune lettre ni aucun texte de la page 8 du VOL.1 n’est arrivé. L’exemple reste, honnêtement signalé, et la promesse passe au VOL.3. Envoyez vos lettres : les meilleures paraîtront dans le VOL.3 !"),
    ("NEXT WEEK · VOL.3 下周预告", "NEXT WEEK · VOL.3 La semaine prochaine"),
    ("下周三退伍军人节，周日 NFL 慕尼黑赛；还有中期选举结果报道。",
     "Mercredi 11 novembre, jour des anciens combattants ; dimanche 15 novembre, la NFL à Munich ; et les résultats des élections de mi-mandat."),
]

CONTENT8 = [
    ("EXERCISES & ANSWERS · 练习与答案", "EXERCISES & ANSWERS · Exercices et réponses"),
    ("FINAL TEST · 综合评估 · Answers at the bottom of this page 答案在本版下方",
     "FINAL TEST · Test final · Answers at the bottom of this page"),
    ("11 月 3 日是周二", "Le 3 novembre, c’est mardi"),
    ("pizza 披萨", "pizza = la pizza"),
    ("map 地图逐州变色", "map = la carte qui change État par État"),
    ("close 接近的", "close = serré"),
    ("sticker 贴纸", "sticker = l’autocollant"),
    ("will + 动词原形 know", "will + verbe de base : know"),
    ("still 仍然", "still = toujours"),
    ("A · CLOZE · 完形填空", "A · CLOZE · Texte à trous"),
    ("选项：", "Les choix :"),
    ("B · MULTIPLE CHOICE · 单选", "B · MULTIPLE CHOICE · QCM"),
    ("we → get 原形", "we → get, verbe de base"),
    ("已发生的事用 fell", "Pour le passé, fell"),
    ("than → 比较级 bigger", "than → comparatif bigger"),
    ("despite + 名词：尽管下雨", "despite + nom : malgré la pluie"),
    ("whether = 是否", "whether = si"),
    ("将来时 will + 动词原形", "Futur : will + verbe de base"),
    ("be going to + 原形 vote", "be going to + verbe de base : vote"),
    ("too close to call = 难分胜负", "too close to call = trop serré pour trancher"),
    ("C · READING · 阅读理解", "C · READING · Compréhension"),
    ("原文：a teacher from Ohio", "Dans le texte : a teacher from Ohio"),
    ("周二他全天教书", "Mardi, il enseigne toute la journée"),
    ("贴纸上写着 I VOTED", "Sur l’autocollant : I VOTED"),
    ("俄亥俄一如既往难分胜负", "L’Ohio, comme toujours, trop serré pour trancher"),
    ("D · SENTENCES · 完成句子与转换", "D · SENTENCES · Phrases à former"),
    ("are going to + 原形", "are going to + verbe de base"),
    ("fall → fell（不规则变化）", "fall → fell (verbe irrégulier)"),
    ("tall → taller（比较级）", "tall → taller (comparatif)"),
    ("whether 引导“是否”从句", "whether introduit une subordonnée en « si »"),
    ("E · TRANSLATION · 翻译", "E · TRANSLATION · Traduction"),
    # Translation keys, EN->FR (core: all four prompts are English
    # sentences, keys Chinese; items 138/139 only differ in that their
    # instruction word is the Chinese one, replaced by "Translate : ").
    ("耐心是制度的一部分，而不是制度的失败。", "La patience fait partie du système, et non un échec de celui-ci."),
    ("part of 一部分；not a failure 不是失败", "part of = une partie de ; not a failure = pas un échec"),
    ("11 月 3 日周二是美国的选举日。", "Le mardi 3 novembre est le jour des élections aux États-Unis."),
    ("Election Day 选举日；on Tuesday", "Election Day = le jour des élections ; on Tuesday"),
    ("翻译：Tuesday, November 3, is Election Day in the United States.",
     "Translate : Tuesday, November 3, is Election Day in the United States."),
    ("这周日，NFL 在马德里比赛。", "Dimanche, la NFL joue à Madrid."),
    ("on Sunday；in Madrid", "on Sunday ; in Madrid"),
    ("翻译：On Sunday, the NFL plays in Madrid.", "Translate : On Sunday, the NFL plays in Madrid."),
    ("并非每处都拨回时钟。", "Tous les endroits ne changent pas."),
    ("not every 并非每处；change 变化", "not every = pas tous ; change = changer"),
    ("F · WORDS · 词汇配对", "F · WORDS · Mots à associer"),
    ("midterm = 中期选举 b", "midterm = une élection de mi-mandat b"),
    ("governor = 州长 c", "governor = le gouverneur c"),
    ("ballot = 选票 d", "ballot = le bulletin de vote d"),
    ("turnout = 投票率 a", "turnout = la participation a"),
    ("投票时出示证件 ID", "Au vote, on montre sa pièce d’identité"),
    ("line = 排队（美式英语）", "line = la file d’attente (anglais américain)"),
    ("ballot = 选票", "ballot = le bulletin de vote"),
    ("sticker = 贴纸", "sticker = l’autocollant"),
    ("选举日是 11 月 3 日周二", "Le jour des élections : mardi 3 novembre"),
    ("G · DIALOGUE · 对话补全", "G · DIALOGUE · À compléter"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "Tâche ouverte — points dans le cadre d’écriture ; texte modèle dans le cadre de cette page"),
    ("按要点给分", "Noté sur les points"),
    ("H · WRITING · 写作 [B1]", "H · WRITING · Écriture [B1]"),
    ("用英语写 80–100 词：我的 11 月 3 日周二。写清你是否看了结果、吃了什么、地图显示了什么，再写一句周日夜里拨回的时钟。",
     "Écrivez en anglais (80 à 100 mots) : « Mon mardi 3 novembre ». Racontez si vous avez suivi les résultats, ce que vous avez mangé, ce que la carte a montré — et une phrase sur les horloges reculées dimanche soir."),
    ("MODEL · 范文", "MODEL · Texte modèle"),
    ("ANSWERS · 全部答案与简析（第 1–8 版）", "ANSWERS · Toutes les réponses commentées (pages 1 à 8)"),
]

# P8 keys block: W43 ENxFR pattern (all notes, half-width parens,
# 13.5pt/1.26, "— Page N —" separators, keys flow bottom 2530).
# KEYS_OLD is the POST-global-replacement form: the global type renames
# have already turned "改错" into "Correction", while "图表读数" survives
# (it is followed by ")" in the condition, not by the token's comma).
# KEYS_NEW replaces the whole block, so the final file has no Chinese.
KEYS_OLD = '''kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("Correction", "图表读数")):
            s += f"（{e['note']}）"
        parts.append(s)
    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)'''
KEYS_NEW = '''kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2530, tag="P8-keys")
from itertools import groupby
for pg, grp in groupby(REG, key=lambda e: e["page"]):
    kf.para(f"— Page {pg} —", 16, "sans", True, OLIVE, 1.26, 3)
    parts = []
    for e in grp:
        s = f"{e['n']}. {e['key']}"
        if e["note"]:
            s += f" ({e['note']})"
        parts.append(s)
    kf.para(" · ".join(parts), 13.5, "sans", False, INK, 1.26, 9)'''

# Global token replacements applied to every content file (exercise type
# and instruction words; registry-only strings except where printed).
GLOBAL = [
    (".bridge(", ".instrline("),
    # Instruction words FIRST: the "改错" instruction value would otherwise
    # be swallowed by the same-spelled exercise-type token below.
    ('instr="填空"', 'instr="Complétez"'),
    ('instr="改写"', 'instr="Réécrivez"'),
    ('instr="改错"', 'instr="Corrigez"'),
    ('instr="把词和释义配对"', 'instr="Associez"'),
    ('instr="配对"', 'instr="Associez"'),
    ('"完成句子",', '"Compléter",'),
    ('"单选",', '"Choix multiple",'),
    ('"句型转换",', '"Transformation",'),
    ('"词汇配对",', '"Appariement",'),
    ('"图表读数",', '"Lecture de graphique",'),
    ('"跟练",', '"À vous",'),
    ('"改错",', '"Correction",'),
    ('"阅读理解",', '"Compréhension écrite",'),
    ('"完形填空",', '"Texte à trous",'),
    ('"对话补全",', '"Dialogue à compléter",'),
    ('"写作",', '"Écriture",'),
    ('"翻译",', '"Traduction",'),
    ("files/weekly-report-w45-en-core/svg", "files/weekly-report-w45-en-fr/svg"),
]

# Post-global structural tweaks for content8 (applied after GLOBAL).
# The battery runs one ex-body line long because E139's English prompt
# wraps to 2 lines under the wider "Translate : " instruction (core: 1
# line under "翻译："). These two gap tweaks recover 14px so the Levels
# line clears the writing-strip rule at y=1486; the F gap=8 is also the
# W43 ENxFR match_set convention.
POST_GLOBAL_CONTENT8 = [
    ('Have a good day.", 21.5)', 'Have a good day.", 21.5, "serif", False, INK, 1.52, 2)'),
    ('instr="Associez")', 'instr="Associez", gap=8)'),
]

PER_FILE = {
    "bslib4.py": BSLIB,
    "content12.py": CONTENT12,
    "content34.py": CONTENT34,
    "content56.py": CONTENT56,
    "content7.py": CONTENT7,
    "content8.py": CONTENT8,
}

RUN_PY = '''# -*- coding: utf-8 -*-
"""Single-process driver: imports the content modules in registry order.
Never import a content module standalone — the shared exercise registry
accumulates numbering across modules in this one process."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content12, content34, content56, content7, content8
print("driver done")
'''

RENDER_PY = '''# -*- coding: utf-8 -*-
"""Render cards + print PDF + web PDF for the EN x FR edition.
Run ONLY with tools/venv/bin/python (system python3 has no cairosvg)."""
import glob, os
import cairosvg
from pypdf import PdfWriter
from PIL import Image

base = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-fr")
w = PdfWriter()
for f in sorted(glob.glob(base + "/svg/*.svg")):
    cairosvg.svg2png(url=f, write_to=f.replace("/svg/", "/cards/").replace(".svg", ".png"), output_width=1950)
    cairosvg.svg2pdf(url=f, write_to="/tmp/en45frpage.pdf")
    w.append("/tmp/en45frpage.pdf")
w.write(open(base + "/The-Lucerna-VOL2-FR-print.pdf", "wb"))
imgs = [Image.open(f).convert("RGB") for f in sorted(glob.glob(base + "/cards/*.png"))]
for im in imgs:
    im.thumbnail((1400, 1938))
imgs[0].save(base + "/The-Lucerna-VOL2-FR-web.pdf", save_all=True, append_images=imgs[1:], quality=85)
print("render done")
'''


def apply_repls(text, repls, fname):
    for entry in repls:
        old, new = entry[0], entry[1]
        want = entry[2] if len(entry) > 2 else 1
        n = text.count(old)
        if n != want:
            raise SystemExit(f"REPL FAIL {fname}: count {n} != {want} for {old!r}")
        text = text.replace(old, new)
    return text


def main():
    os.makedirs(DST, exist_ok=True)
    os.makedirs(EDITION, exist_ok=True)
    os.makedirs(os.path.join(EDITION, "..", "cards"), exist_ok=True)
    # svglib.py: byte-identical copy (W43 ENxFR precedent).
    shutil.copyfile(os.path.join(CORE, "svglib.py"), os.path.join(DST, "svglib.py"))
    # assets: byte-identical copy (5 public-domain images + CREDITS.md).
    src_assets = os.path.join(CORE, "assets")
    dst_assets = os.path.join(DST, "assets")
    if os.path.isdir(dst_assets):
        shutil.rmtree(dst_assets)
    shutil.copytree(src_assets, dst_assets)
    for fname, repls in PER_FILE.items():
        text = open(os.path.join(CORE, fname), encoding="utf-8").read()
        text = apply_repls(text, repls, fname)
        if fname.startswith("content"):
            # OUT must repoint exactly once — never write into the core dir.
            if text.count("files/weekly-report-w45-en-core/svg") != 1:
                raise SystemExit(f"REPOINT FAIL {fname}")
            # Plain replace-all: counts are pre-empted by interacting
            # entries (instr "改错" vs type "改错"); the post-check below
            # (no CJK, no bridge) is the real guard for leftovers.
            for (o, n) in GLOBAL:
                text = text.replace(o, n)
        if fname == "content8.py":
            text = apply_repls(text, POST_GLOBAL_CONTENT8, fname)
        open(os.path.join(DST, fname), "w", encoding="utf-8").write(text)
    # P8 keys block (content8 only).
    p8 = os.path.join(DST, "content8.py")
    text = open(p8, encoding="utf-8").read()
    if text.count(KEYS_OLD) != 1:
        raise SystemExit("REPL FAIL content8.py: KEYS_OLD count != 1")
    open(p8, "w", encoding="utf-8").write(text.replace(KEYS_OLD, KEYS_NEW))
    open(os.path.join(DST, "run.py"), "w", encoding="utf-8").write(RUN_PY)
    open(os.path.join(DST, "render.py"), "w", encoding="utf-8").write(RENDER_PY)
    # Post-conditions: no CJK, no banned term, no leftover method/type.
    import re
    bad = []
    for fname in PER_FILE:
        t = open(os.path.join(DST, fname), encoding="utf-8").read()
        if re.search(r"[\u4e00-\u9fff]", t):
            bad.append(f"{fname}: CJK remains")
        if "桥接" in t:
            bad.append(f"{fname}: banned term remains")
        if ".bridge(" in t or "def bridge" in t:
            bad.append(f"{fname}: bridge method remains")
    if bad:
        raise SystemExit("POST FAIL: " + "; ".join(bad))
    print("transform done ->", DST)


if __name__ == "__main__":
    main()
