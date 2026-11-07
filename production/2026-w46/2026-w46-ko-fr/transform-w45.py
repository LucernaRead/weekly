# -*- coding: utf-8 -*-
"""KO x FR (W45) fan-out transform — SINGLE source of truth for all edits.

Method (tools README #17/#18): exact unique literal replacements, applied
longest-first so a short string never corrupts a longer string containing
it; every replacement asserted (count >= 1 across the build files, and the
source literal must be absent afterwards). No AST byte-offset splicing, no
repr literals into f-strings. Korean target text is never touched: only
the Chinese explanation layer + bilingual furniture second elements +
masthead geometry change. Run from this directory; re-runnable (idempotent
only in the sense that a second run aborts: sources are already gone).
"""
import glob
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py", "render.py"]

# ---- Chinese explanation layer -> French (longest applied first) ----
REPL = {
    # bslib4 furniture
    "Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY":
        "Lucerna · HEBDOMADAIRE CORÉEN VOL.2 · TEXTE EN CORÉEN · EXPLICATIONS EN FRANÇAIS",
    "제 {n} 면 / 총 {total} 면": "Page {n} sur {total}",
    "译注｜": "Note — ",
    # exercise types / instruction labels
    "完成句子": "Compléter",
    "完形单选": "Texte à trous",
    "词汇配对": "Appariement",
    "句型转换": "Transformation",
    "把词和说明配对": "Associer",
    "把山和说明配对": "Associer",
    "把词和释义配对": "Associer",
    "单选": "Choix multiple",
    "造句": "Former une phrase",
    "判断": "Vrai ou faux",
    "翻译": "Traduction",
    "写作": "Rédaction",
    "填空": "Complétez",
    "改写": "Réécrire",
    # P1 furniture
    "매주 한국어로 · 每周一期 · 한국 사람이 읽는 한국어를 읽어요":
        "매주 한국어로 · Chaque semaine · 한국 사람이 읽는 한국어를 읽어요",
    "한국어판 · VOL.2 · 입동 · 단풍 · 김장":
        "HEBDOMADAIRE CORÉEN · VOL.2 · 입동 · 단풍 · 김장",
    "立冬在 11 月 7 日周六 · 泡菜季开始":
        "L'Ipdong, le samedi 7 novembre · Début du kimjang",
    "立冬": "IPDONG",
    "톱 뉴스 · 头条": "톱 뉴스 · À la une",
    "입동 立冬、冬季开始 · 절정 最盛期、高峰 · 김장 腌过冬泡菜 · 상륙하다 登陆 · 온대저기압 温带气旋。":
        "입동 = Ipdong · 절정 = apogée · 김장 = kimjang · 상륙하다 = toucher terre · 온대저기압 = cyclone extratropical.",
    "숫자로 보는 이번 주 · 数字看本周": "숫자로 보는 이번 주 · En chiffres",
    "지금 바로 연습 · 即学即练": "지금 바로 연습 · Exercices immédiats",
    "这五个日期，是本期报纸的骨架。": "Ces cinq dates font ce numéro.",
    "이번 호의 내용 · 本期目录": "이번 호의 내용 · Sommaire",
    "全部": "Tous",
    "이번 주의 말 · 本周词语": "이번 주의 말 · Le mot de la semaine",
    "입동 ＝ 立冬、冬季开始的节气。": "입동 = Ipdong, le début de l'hiver.",
    "짧은 소식 · 快讯": "짧은 소식 · En bref",
    "퀴즈 · 闪电问答": "퀴즈 · Quiz éclair",
    "读头版，选出正确答案 · 答案见第 8 版":
        "Lisez la une, choisissez la bonne réponse · Réponses page 8",
    # P1/P2 band + heads
    "생활 · 生活": "생활 · Vie quotidienne",
    "레벨 A2 · 김장과 겨울 준비, 한능검 · 泡菜季与过冬准备、韩史考试报名":
        "레벨 A2 · 김장과 겨울 준비, 한능검 · Kimjang et préparatifs d'hiver, examen d'histoire de Corée",
    "절이다 用盐腌 · 버무리다 拌 · 난방 供暖 · 식탁 餐桌。":
        "절이다 = saler · 버무리다 = mélanger, assaisonner · 난방 = chauffage · 식탁 = table à manger.",
    "산불 山火 · 벌금 罚款 · 불씨 火星。":
        "산불 = feu de forêt · 벌금 = amende · 불씨 = étincelle.",
    "한능검 접수 · 韩史考试报名": "한능검 접수 · Inscriptions",
    "아삭하다 脆脆的 · 김 蒸汽 · 깊어지다 变深。":
        "아삭하다 = croquant · 김 = vapeur · 깊어지다 = s'approfondir.",
    "물려주다 传给 · 낡다 旧 · 두렵다 害怕。":
        "물려주다 = transmettre · 낡다 = usé · 두렵다 = craindre.",
    "겨울 준비 목록 · 过冬清单": "겨울 준비 목록 · Liste d'hiver",
    "묵직하다 沉甸甸的 · 앞치마 围裙 · 목록 清单。":
        "묵직하다 = lourd, bien dense · 앞치마 = tablier · 목록 = liste.",
    "당신은? · 说说你自己": "당신은? · À vous",
    "你呢？为过冬做的第一件事是什么？写两句韩语寄来。":
        "Et vous ? Pour préparer l'hiver, que faites-vous en premier ? Écrivez deux phrases en coréen et envoyez-les-nous.",
    "날짜 세는 말 · 数日子的说法": "날짜 세는 말 · Compter les jours",
    "수능까지 남은 날로 날짜를 세는 네 가지 말 · 用高考倒计时数日子的四个说法":
        "Quatre façons de compter avec le compte à rebours du Suneung",
    "11 月 2 日，还剩 17 天": "Le 2 novembre, il reste 17 jours",
    "11 月 7 日，还剩 12 天": "Le 7 novembre, il reste 12 jours",
    "11 月 18 日，就是明天": "Le 18 novembre, c'est demain",
    "11 月 19 日，就是今天": "Le 19 novembre, c'est aujourd'hui",
    "연습 · 第 2 版练习": "연습 · Exercices page 2",
    "연습 · 第 3 版练习": "연습 · Exercices page 3",
    "연습 · 第 4 版练习": "연습 · Exercices page 4",
    "연습 · 第 5 版练习": "연습 · Exercices page 5",
    "연습 · 第 6 版练习": "연습 · Exercices page 6",
    "答案见第 8 版 · 题目可跨级混排，按题号找答案":
        "Réponses page 8 · Les niveaux sont mélangés, cherchez le numéro",
    # P2 notes
    "泡菜季＝腌过冬泡菜": "Kimjang = le kimchi de l'hiver",
    "山火注意期从11月1日开始": "La vigilance feux de forêt commence le 1er novembre",
    "带火进山最高罚30万韩元": "Apporter du feu en montagne : jusqu'à 300 000 wons d'amende",
    "韩史考试在11月28日周六": "L'examen d'histoire a lieu le samedi 28 novembre",
    "首尔报名10点至12点": "Inscriptions à Séoul de 10 h à 12 h",
    "白菜用盐腌": "Le chou est salé",
    "加入萝卜和调料拌匀": "On ajoute radis et assaisonnement, on mélange",
    "过冬准备＝为冬天做准备": "Préparer l'hiver = se préparer pour l'hiver",
    "进山要小心火": "En montagne, attention au feu",
    "11月3日起开始报名": "Les inscriptions commencent le 3 novembre",
    "山火注意期到12月15日": "La vigilance dure jusqu'au 15 décembre",
    "最高罚款30万韩元": "Amende maximale : 300 000 wons",
    "深化考试费27,000韩元": "Frais d'examen (niveau avancé) : 27 000 wons",
    "11月6日13点起全国报名剩余名额":
        "Le 6 novembre dès 13 h, inscriptions nationales pour les places restantes",
    "김장=腌过冬泡菜 a": "김장=le kimchi de l'hiver a",
    "월동 준비=准备过冬 c": "월동 준비=préparer l'hiver c",
    "산불조심=进山小心火 d": "산불조심=attention au feu en montagne d",
    "한능검=韩国史考试简称 b": "한능검=examen d'histoire de Corée b",
    # P3
    "문화 · 文化": "문화 · Culture",
    "레벨 A2→B1 · 단풍 마지막 주말 · 红叶最后一周":
        "레벨 A2→B1 · 단풍 마지막 주말 · Dernier week-end des feuillages",
    "기관 机构 · 기준 标准 · 관측 观测 · 구간별 按路段。":
        "기관 = organisme · 기준 = critère · 관측 = observation · 구간별 = par tronçon.",
    "현장 现场 · 유명하다 有名 · 맛보다 品尝。":
        "현장 = sur place · 유명하다 = célèbre · 맛보다 = goûter.",
    "이용하다 利用 · 막히다 堵塞 · 예의 礼仪。":
        "이용하다 = utiliser · 막히다 = être bouché · 예의 = politesse.",
    "겹쳐 입다 叠穿 · 미끄러지다 打滑 · 돌 石头。":
        "겹쳐 입다 = superposer · 미끄러지다 = glisser · 돌 = pierre.",
    "단풍 구경 준비물 · 红叶观赏准备": "단풍 구경 준비물 · À emporter",
    "你呢？想去看红叶的山是哪座？写两句韩语寄来。":
        "Et vous ? Quelle montagne voulez-vous voir en feuillages ? Écrivez deux phrases en coréen et envoyez-les-nous.",
    "内藏山林业厅预报峰值11月4日": "Pic de Naejangsan selon le Service des forêts : 4 novembre",
    "内藏山公园公团预报峰值11月11日": "Pic de Naejangsan selon l'Office des parcs : 11 novembre",
    "雪岳山实际观测峰值10月16日": "Pic observé à Seoraksan : 16 octobre",
    "青松现场庆典11月4日至8日": "Fête de Cheongsong sur place, du 4 au 8 novembre",
    "没有官方的路段数值": "Aucune valeur officielle par tronçon",
    "红叶最美的时候叫절정": "Le plus beau moment des feuillages s'appelle 절정",
    "日期不同因为标准不同": "Les dates diffèrent car les critères diffèrent",
    "实际观测比预报早": "L'observation réelle devance la prévision",
    "现场庆典11月4日起": "La fête sur place commence le 4 novembre",
    "青松以苹果闻名": "Cheongsong est célèbre pour ses pommes",
    "内藏山林业厅预报4日": "Prévision du Service des forêts pour Naejangsan : le 4",
    "内藏山公团预报11日": "Prévision de l'Office des parcs pour Naejangsan : le 11",
    "月出山林业厅预报9日": "Prévision du Service des forêts pour Wolchulsan : le 9",
    "雪岳山实际观测16日": "Observation réelle à Seoraksan : le 16",
    "내장산=两个预报之间 b": "내장산=entre les deux prévisions b",
    "월출산=11月9日前夕 a": "월출산=à la veille du 9 novembre a",
    "북한산=11月4日之后、低路更晚 d": "북한산=après le 4 novembre, sentiers bas plus tardifs d",
    "설악산=实际观测10月16日 c": "설악산=observation réelle le 16 octobre c",
    # P4
    "스포츠 · 体育": "스포츠 · Sports",
    "레벨 B1 · 가을야구 소식 · 秋季棒球消息":
        "레벨 B1 · 가을야구 소식 · Nouvelles du baseball d'automne",
    "연승 连胜 · 만루홈런 满垒本垒打 · 미뤄지다 推迟 · 마감하다 截稿。":
        "연승 = victoires d'affilée · 만루홈런 = grand chelem · 미뤄지다 = être reporté · 마감하다 = boucler.",
    "흔들다 挥动 · 하나가 되다 融为一体。":
        "흔들다 = agiter · 하나가 되다 = ne faire qu'un.",
    "예상 预测。": "예상 = prévision.",
    "한국시리즈까지의 길 · 通往韩国大赛之路":
        "한국시리즈까지의 길 · La route vers les Korean Series",
    "半决赛胜队是KIA": "Le vainqueur de la demi-finale est KIA",
    "第3场比分13比1": "Le 3e match : 13 à 1",
    "第3场在蚕室举行": "Le 3e match a eu lieu à Jamsil",
    "季后赛首场因雨推迟": "Le 1er match des play-offs reporté pour cause de pluie",
    "公布的韩国大赛开始日11月2日": "Début annoncé des Korean Series : 2 novembre",
    "三连胜晋级": "Trois victoires d'affilée",
    "首场比赛因雨推迟": "Le 1er match reporté pour cause de pluie",
    "10月26日变为温带气旋": "Devenu cyclone extratropical le 26 octobre",
    "kt在韩国大赛等候": "kt attend en Korean Series",
    "이기다的过去式이겼어요": "Passé de 이기다 : 이겼어요",
    "열리다的过去式열렸어요": "Passé de 열리다 : 열렸어요",
    "미뤄지다的过去式미뤄졌어요": "Passé de 미뤄지다 : 미뤄졌어요",
    "바뀌다的过去式바뀌었어요": "Passé de 바뀌다 : 바뀌었어요",
    "준플레이오프=KIA三连胜 b": "준플레이오프=KIA, trois victoires d'affilée b",
    "플레이오프=KIA对三星 d": "플레이오프=KIA contre Samsung d",
    "한국시리즈=kt在等候 a": "한국시리즈=kt attend a",
    "온대저기압=台风10月26日变化 c": "온대저기압=le typhon devenu cyclone le 26 octobre c",
    # P5
    "청년 · 青年": "청년 · Jeunesse",
    "레벨 B1 · 수능 카운트다운과 할로윈 · 高考倒计时与万圣节":
        "레벨 B1 · 수능 카운트다운과 할로윈 · Compte à rebours du Suneung et Halloween",
    "정리 整理、复习 · 끈끈하다 粘粘的 · 합격 合格。":
        "정리 = rangement, révision · 끈끈하다 = collant · 합격 = réussite.",
    "중점 重点 · 배치하다 部署 · 통제하다 管制。":
        "중점 = prioritaire · 배치하다 = déployer · 통제하다 = contrôler.",
    "이번 주 청년 숫자 · 本周青年数字": "이번 주 청년 숫자 · Chiffres jeunes",
    "챙기다 准备好 · 졸리다 犯困 · 평소 平时。":
        "챙기다 = préparer · 졸리다 = avoir sommeil · 평소 = d'habitude.",
    "비다 祈愿 · 피하다 避开 · 미끄럽다 滑。":
        "비다 = souhaiter · 피하다 = éviter · 미끄럽다 = glissant.",
    "你呢？想对考生说的一句加油是什么？写两句韩语寄来。":
        "Et vous ? Quel mot d'encouragement voulez-vous dire aux candidats ? Écrivez deux phrases en coréen et envoyez-les-nous.",
    "11月7日是D-12": "Le 7 novembre, c'est D-12",
    "高考在11月19日周四": "Le Suneung a lieu le jeudi 19 novembre",
    "听力时段飞机不起降": "Pendant l'écoute, aucun avion ne décolle ni n'atterrit",
    "首尔万圣节安全人员3,271人": "Séoul : 3 271 agents pour Halloween",
    "梨泰院路10月31日管制": "La rue d'Itaewon fermée le 31 octobre",
    "全国为考生加油": "Tout le pays encourage les candidats",
    "倒计时仍在继续": "Le compte à rebours continue",
    "怀着祈愿合格的心意赠送糯米糕、饴糖":
        "On offre tteok de riz gluant et yeot en souhaitant la réussite",
    "首尔安全人员3,271人": "Séoul : 3 271 agents de sécurité",
    "今年考生551,864人": "Candidats cette année : 551 864",
    "考场全国1,312处": "Centres d'examen dans tout le pays : 1 312",
    "考试日机关10点上班": "Le jour de l'examen, les bureaux ouvrent à 10 h",
    "梨泰院部署1,620人": "Itaewon : 1 620 agents déployés",
    "语序：主语+副词+动词": "Ordre : sujet + adverbe + verbe",
    "主语+宾语+动词的语序": "Ordre : sujet + objet + verbe",
    "首尔管理14个地点": "Séoul gère 14 lieux",
    # P6
    "깊이 읽기 · 深读": "깊이 읽기 · Lecture approfondie",
    "레벨 B2 · 수능 카운트다운을 읽는 법 · 高考倒计时读法":
        "레벨 B2 · 수능 카운트다운을 읽는 법 · Comment lire le compte à rebours du Suneung",
    "짙어지다 变浓 · 규모 规模 · 섞다 混淆。":
        "짙어지다 = s'intensifier · 규모 = ampleur · 섞다 = confondre.",
    "겁이 나다 害怕 · 중요하다 重要。":
        "겁이 나다 = avoir peur · 중요하다 = important.",
    "예정 预定 · 확정 确定 · 믿다 相信。":
        "예정 = prévu · 확정 = confirmé · 믿다 = croire.",
    "이번 주와 시험 날, 한눈에 보기 · 本周与考试日一表看清":
        "이번 주와 시험 날, 한눈에 보기 · Cette semaine et le jour de l'examen, en un coup d'œil",
    "本周倒计时D-17至D-12": "Cette semaine : compte à rebours D-17 à D-12",
    "考试日有特别措施": "Le jour de l'examen, il y a des mesures spéciales",
    "本周没有特别措施": "Cette semaine, pas de mesures spéciales",
    "考试日就是D-day": "Le jour de l'examen, c'est le D-day",
    "本周氛围是倒计时": "Cette semaine, l'ambiance est au compte à rebours",
    "氛围在现在、本周": "L'ambiance est là, maintenant, cette semaine",
    "措施只适用于11月19日": "Les mesures ne s'appliquent que le 19 novembre",
    "听力时段13:10～13:35": "Écoute : 13 h 10–13 h 35",
    "倒计时氛围在本周": "Le compte à rebours, c'est l'ambiance de cette semaine",
    "特别措施只适用于考试日": "Les mesures spéciales ne valent que le jour de l'examen",
    "从D-17到D-12的一周": "La semaine qui va de D-17 à D-12",
    "大数字显示全国规模": "Les grands chiffres montrent l'ampleur nationale",
    "特别措施只适用于11月19日": "Les mesures spéciales ne s'appliquent que le 19 novembre",
    "听力时段飞机受管制": "Pendant l'écoute, les avions sont réglementés",
    "本周是倒计时氛围": "Cette semaine, c'est l'ambiance du compte à rebours",
    # P7
    "말 공부 · 语言": "말 공부 · Langue",
    "언어 포커스 · 세 가지 레벨, 세 가지 주제 · 三个级别，三个主题":
        "언어 포커스 · 세 가지 레벨, 세 가지 주제 · Trois niveaux, trois sujets",
    "본격적 正式、全面 · 나다 度过。":
        "본격적 = vraiment, pleinement · 나다 = passer, traverser.",
    "남다 剩下 · 바로 正是、恰恰。": "남다 = rester · 바로 = exactement.",
    "짐작하다 推测 · 나누다 区分。": "짐작하다 = deviner · 나누다 = distinguer.",
    "节气＝一年24个时节": "절기 = les 24 divisions de l'année",
    "D-1＝明天": "D-1 = demain",
    "D-day就是当天": "Le D-day, c'est le jour même",
    "日期不同因标准不同（3版）": "Les dates diffèrent car les critères diffèrent (page 3)",
    "林业厅标准是叶子50%": "Le critère du Service des forêts : 50 % des feuilles",
    "实际观测10月16日": "Observation réelle : 16 octobre",
    "预报要标准日期一起看": "Pour une prévision, regarder critère et date ensemble",
    "실수 병원 · 易错诊所": "실수 병원 · Le cabinet des erreurs",
    "去某地用「에」，不用「를」。": "« 에 » pour la destination, pas « 를 ».",
    "「담그다」的过去式是「담갔어요」。": "Passé de « 담그다 » : « 담갔어요 ».",
    "数字与前面要留空格。": "Un espace avant le chiffre.",
    "助词只用一个。": "Une seule particule.",
    "이번 주의 틀 · 本周句式": "이번 주의 틀 · Modèle de phrase",
    "句式拆解：「从〜到〜」。提问：「〜부터 〜까지예요?」":
        "Structure « de 〜 à 〜 » ; question : « 〜부터 〜까지예요? »",
    "독자의 편지 · 读者园地": "독자의 편지 · Le courrier des lecteurs",
    "编辑部示例信，非真实来信。": "Exemple de la rédaction, pas une vraie lettre.",
    "郑重说明：截至截稿时，未收到真实读者来信与第 8 版优秀作文，因此仍刊示例，上期承诺顺延至 VOL.3。":
        "Aucune vraie lettre ni meilleur texte de page 8 à la mise sous presse : l'exemple reste, la promesse passe au VOL.3. Envoyez-nous votre lettre et votre texte de page 8 !",
    "이번 주의 문장 · 本周金句（逐字摘自本期文章）":
        "이번 주의 문장 · Phrases de la semaine (verbatim, tirées de ce numéro)",
    "11 月 7 日是立冬。": "Le 7 novembre, c'est l'Ipdong.",
    "只能说是接近峰值的周末。": "On peut seulement parler d'un week-end proche du pic.",
    "泡菜季就是腌过冬泡菜。": "Le kimjang, c'est préparer le kimchi de tout l'hiver.",
    "离高考还剩 17 天，今天是 D-17。": "Il reste 17 jours avant le Suneung. Aujourd'hui, c'est D-17.",
    "低处的路红得更晚。": "Les sentiers bas rougissent plus tard.",
    "KIA 虎三连胜战胜 LG 双子。": "Les KIA Tigers ont battu les LG Twins trois fois d'affilée.",
    "全国都在为考生加油。": "Tout le pays encourage les candidats.",
    "先看日期。": "Regardez d'abord la date.",
    "다음 주 · 下期预告 (VOL.3)": "다음 주 · La semaine prochaine (VOL.3)",
    # P8
    "시험과 답 · 测验与答案": "시험과 답 · Test et réponses",
    "立冬在11月7日周六": "L'Ipdong tombe le samedi 7 novembre",
    "青松现场庆典11月4日起": "La fête de Cheongsong sur place commence le 4 novembre",
    "KIA三连胜晋级": "Trois victoires d'affilée",
    "汉拿山三角峰降雨415.5毫米": "Pluie au Samgakbong du Hallasan : 415,5 mm",
    "月出山林业厅预报峰值11月9日": "Pic de Wolchulsan selon le Service des forêts : 9 novembre",
    # P8 short variants, distinct from the longer P3 forms (ko-de round-1 trap)
    "内藏山公团预报峰值11月11日": "Pic de Naejangsan selon l'Office des parcs : 11 novembre",
    "首尔报名窗口10点至12点": "Inscriptions à Séoul de 10 h à 12 h",
    "日期不同因标准不同": "Les dates diffèrent car les critères diffèrent",
    "智敏周六去内藏山": "Jimin va à Naejangsan samedi",
    "周日帮忙腌泡菜": "Dimanche, elle aide au kimjang",
    "下周准备韩史考试": "La semaine prochaine, elle prépare l'examen d'histoire",
    "智敏喜欢韩国史": "Jimin aime l'histoire de Corée",
    "语序：主语+时间+场所+动词": "Ordre : sujet + temps + lieu + verbe",
    "보러 가요 = 去看": "보러 가요 = aller voir",
    "动作场所用「에서」": "Le lieu de l'action prend « 에서 »",
    "11月7日是立冬。": "Le 7 novembre, c'est l'Ipdong.",
    "对照第 1 版": "Voir page 1",
    "离高考还剩 12 天。": "Il reste 12 jours avant le Suneung.",
    "对照第 5 版": "Voir page 5",
    "特别措施只适用于11月19日。→ ___": "Les mesures spéciales ne s'appliquent que le 19 novembre. → ___",
    "对照第 6 版": "Voir page 6",
    "我周六去内藏山看红叶。→ ___": "Samedi, je vais à Naejangsan voir les feuillages. → ___",
    "对照第 3 版": "Voir page 3",
    "입동=冬季开始的节气 a": "입동=le début de l'hiver a",
    "절정=最佳时期 b": "절정=le plus beau moment b",
    "김장=腌过冬泡菜 c": "김장=le kimchi de l'hiver c",
    "온대저기압=台风10月26日变化 d": "온대저기압=le typhon devenu cyclone le 26 octobre d",
    "周六去内藏山": "Aller à Naejangsan samedi",
    "首尔报名10点开始": "Les inscriptions à Séoul commencent à 10 h",
    "(开放题，范文如下)": "(question ouverte — modèle ci-dessous)",
    "范文见本版 H 区（{NCHARS} 字）": "Modèle dans la section H de cette page ({NCHARS} caractères)",
    "답 · 参考答案 — 按版面分页排列，找到题号即可":
        "답 · Réponses — classées par page, cherchez le numéro",
    "每题附一句中文简析 · 带 ✓ 的为范文题":
        "Chaque réponse avec une courte note en français · ✓ = exercice à texte modèle",
    # P1 drill notes not covered above (distinct strings)
    "首尔报名窗口11月6日10–12点": "Inscriptions à Séoul le 6 novembre, 10 h–12 h",
    "台风没有在韩国本土登陆": "Le typhon n'a pas touché la Corée",
    "11月2日是D-17": "Le 2 novembre, c'est D-17",
    "立冬＝冬季开始的节气": "Ipdong = le début de l'hiver",
    "内藏山两个预报：11月4日与11月11日": "Naejangsan : deux prévisions, 4 et 11 novembre",
    "10月25日首场比赛因雨推迟": "Le 1er match reporté pour cause de pluie, le 25 octobre",
}

# ---- whole-line geometry edits (content12 masthead, W43 ko-fr geometry) ----
LINE_EDITS = [
    ("content12.py",
     'p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")\n'
     'p.text(975, 394, "TEXTES EN CORÉEN · EXPLICATIONS EN FRANÇAIS — L\'ÉDITION POUR LES LECTEURS FRANCOPHONES", 20, "sans", True, BRICK, anchor="middle")'),
    ("content12.py",
     "p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)",
     "p.hline(MX, RIGHT, 412, INK, 3); p.hline(MX, RIGHT, 421, INK, 1.2)"),
    ("content12.py",
     "p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)",
     "p.rect(MX, 433, RIGHT - MX, 118, fill=DARK)"),
    ("content12.py",
     'p.text(MX + 30, 478, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")',
     'p.text(MX + 30, 487, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")'),
    ("content12.py",
     'p.text(MX + 30, 522, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")',
     'p.text(MX + 30, 531, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")'),
    ("content12.py",
     'p.text(RIGHT - 30, 478, "IPDONG", 24, "sans", True, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 487, "IPDONG", 24, "sans", True, "#b3a06a", anchor="end")'),
    ("content12.py",
     'p.text(RIGHT - 30, 522, "L\'Ipdong, le samedi 7 novembre · Début du kimjang", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 531, "L\'Ipdong, le samedi 7 novembre · Début du kimjang", 21, "sans", False, "#b3a06a", anchor="end")'),
    # P7 phrases pitch 132 -> 102 (French readers-corner growth compensation;
    # row content needs ~76px, pitch 102 keeps ~26px inter-row air)
    ("content7.py", "(i % 4) * 132", "(i % 4) * 102"),
    ("content7.py", "py = fy + 66 + 4 * 132 + 18", "py = fy + 66 + 4 * 102 + 18"),
    # P7 readers-box slack +40: the lh formula undercounts drawn height by
    # ~29px (measured on both core and edition: drawn last ink bottom sits
    # ~29px below the formula box bottom; core's own last line hangs below
    # its box). +40 puts the edition's last line ~11px inside the box.
    ("content7.py",
     'wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 26',
     'wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 66'),
    # render PDF names (W43 ko-fr pattern: VOLn-FR)
    ("render.py", "Lucerna-VOL2-web.pdf", "Lucerna-VOL2-FR-web.pdf"),
    ("render.py", "Lucerna-VOL2.pdf", "Lucerna-VOL2-FR.pdf"),
]


# Type/instr collisions: 翻译 and 写作 serve as BOTH a type name and an
# instr label with different French forms — pre-replace the instr form first.
PRE_REPL = {
    'instr="翻译"': 'instr="Traduire"',
    'instr="写作"': 'instr="Écrire"',
}


def main():
    texts = {}
    for fn in FILES:
        with open(os.path.join(HERE, fn), encoding="utf-8") as fh:
            texts[fn] = fh.read()
    for src, dst in PRE_REPL.items():
        total = sum(t.count(src) for t in texts.values())
        assert total >= 1, f"PRE_REPL source not found: {src!r}"
        for fn in FILES:
            texts[fn] = texts[fn].replace(src, dst)
        print(f"pre-replaced {total}x: {src!r} -> {dst!r}")
    # literal replacements, longest source first
    for src, dst in sorted(REPL.items(), key=lambda kv: -len(kv[0])):
        total = sum(t.count(src) for t in texts.values())
        assert total >= 1, f"REPL source not found: {src!r}"
        for fn in FILES:
            texts[fn] = texts[fn].replace(src, dst)
        assert all(src not in t for t in texts.values()), f"REPL source remains: {src!r}"
        print(f"replaced {total}x: {src[:40]!r} -> {dst[:40]!r}")
    for fn, old, new in LINE_EDITS:
        assert texts[fn].count(old) == 1, f"LINE_EDIT not unique in {fn}: {old[:60]!r} (count {texts[fn].count(old)})"
        texts[fn] = texts[fn].replace(old, new)
        print(f"line edit {fn}: {old[:50]!r}")
    for fn in FILES:
        with open(os.path.join(HERE, fn), "w", encoding="utf-8") as fh:
            fh.write(texts[fn])
    print("transform OK")


if __name__ == "__main__":
    main()
