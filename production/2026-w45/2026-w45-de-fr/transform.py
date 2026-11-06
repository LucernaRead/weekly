# -*- coding: utf-8 -*-
"""DE x FR fan-out transform for W45 DE core build copy.
Rules: whole-line or exact-unique-literal replacements with count
assertions; value maps (types/instr) use bare text, never repr.
German body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Furniture strings are verbatim from the shipped
W43 DE x FR edition (VOL.1 -> VOL.2 here). Run once from the build dir copy.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))
LOG = []

def rep(fname, old, new, expect=None):
    p = os.path.join(BASE, fname)
    s = open(p, encoding="utf-8").read()
    n = s.count(old)
    if expect is not None:
        assert n == expect, f"{fname}: {old!r} count {n} != {expect}"
    else:
        assert n >= 1, f"{fname}: {old!r} not found"
    LOG.append(f"{fname}: {n}x {old!r} -> {new!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))

def rep_all(fname, pairs):
    for old, new in pairs:
        rep(fname, old, new)

# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-de-core", "weekly-report-w45-de-fr", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "for la fête du Double Neuf.", 1)

# ---------- bslib4: furniture + gloss prefix (W43 DE x FR shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · HEBDOMADAIRE ALLEMAND VOL.2 · TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} sur {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Note — " + s', 1)

# ---------- shared furniture strings ----------
SHARED = [
    ("UND SIE? · 说说你自己", "UND SIE? · Et vous ?"),
    ("FERIENWECHSEL · 假期交接", "FERIENWECHSEL · Vacances"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Réponses page 8 · Les niveaux se mélangent — retrouvez chaque réponse par son numéro"),
    ("BEISPIELE · 例句", "BEISPIELE · Exemples"),
]
for f in ["content12.py", "content34.py", "content56.py"]:
    for old, new in SHARED:
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)

# ================= content12 (P1 + P2) =================
C12 = [
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语",
     "WÖCHENTLICH AUF DEUTSCH · CHAQUE SEMAINE · L'ALLEMAND QUE LISENT LES ALLEMANDS"),
    ("德 语 周 报 · VOL.2 · 足 球 周 · 油 价 · 护 理",
     "JOURNAL ALLEMAND · VOL.2 · FOOTBALL · CARBURANT · SOINS"),
    # P1 subtitle slot -> W43 shipped badge, verbatim string, 20pt bold brick
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEXTE EN ALLEMAND · EXPLICATIONS EN FRANÇAIS — L\'ÉDITION POUR LES LECTEURS FRANCOPHONES", 20, "sans", True, BRICK, anchor="middle")'),
    ("本周足球周 · 欧冠欧联德甲连轴转", "Semaine de football"),
    ("详见第 4 版 · Seite 4", "Voir page 4"),
    ("DIE TOPMELDUNG · 头条", "DIE TOPMELDUNG · À la une"),
    ("讲解｜die Englische Woche 一周双赛 · der Spieltag 比赛日 · empfangen 主场迎战 · die Bundesliga 德甲。",
     "Notes — die Englische Woche = semaine anglaise · der Spieltag = journée de championnat · empfangen = recevoir."),
    ("DIE WOCHE IN ZAHLEN · 数字看本周", "DIE WOCHE IN ZAHLEN · Chiffres"),
    ("9 — Spiele hat der 9. Spieltag der Bundesliga（德甲第 9 轮共 9 场比赛）",
     "9 — Spiele hat der 9. Spieltag der Bundesliga (9 matches de la 9e journée)"),
    ("6 — deutsche Teams spielen in Europa（6 支德国球队出战欧战）",
     "6 — deutsche Teams spielen in Europa (6 équipes allemandes en Europe)"),
    ("14,04 — Cent pro Liter beträgt der Tankrabatt（每升油减税 14.04 欧分）",
     "14,04 — Cent pro Liter beträgt der Tankrabatt (taxe en moins par litre)"),
    ("JETZT ÜBEN · 即学即练", "JETZT ÜBEN · Entraînez-vous"),
    ("一周双赛", "semaine anglaise"),
    ("多特主场迎战贝蒂斯", "Dortmund reçoit le Betis"),
    ("欧联在周四", "Ligue Europa jeudi"),
    ("周五汉堡–门兴开轮", "Hambourg–Gladbach ouvrent vendredi"),
    ("第 9 轮共 9 场", "9 matches pour la 9e journée"),
    ("减税到 12 月 31 日", "réduction jusqu'au 31 décembre"),
    ("拜仁周二客战马竞", "Bayern à l'Atlético mardi"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim à Crystal Palace en Ligue Europa"),
    ("本周大问题 · Die Fragen der Woche", "Les grandes questions de la semaine"),
    ("德国本周最热议的五个问题。", "Les cinq questions qui agitent l'Allemagne."),
    ("IN DIESER AUSGABE · 本期目录", "IN DIESER AUSGABE · Sommaire"),
    ("油价减税（加油折扣）。详见第 2 版。", "Réduction du carburant. Voir page 2."),
    ("KURZ & GUT · 快讯", "KURZ & GUT · En bref"),
    ("BLITZQUIZ · 闪电问答", "BLITZQUIZ · Quiz éclair"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Lisez la page 1 et choisissez la bonne réponse · Réponses page 8"),
    # P2
    ("LEBEN · 生活", "LEBEN · Vie"),
    ("LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 油价、电力税与护理",
     "LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · Carburant, taxe sur l'électricité et soins"),
    ("der Tankrabatt 油价减税 · die Zapfsäule 加油机 · die Energiesteuer 能源税 · die Mehrwertsteuer 增值税 · der Angehörige 亲属。",
     "der Tankrabatt = réduction du carburant · die Zapfsäule = pompe à essence · die Energiesteuer = taxe sur l'énergie · die Mehrwertsteuer = TVA · der Angehörige = proche."),
    ("AN DER ZAPFSÄULE · 加油机旁", "AN DER ZAPFSÄULE · À la pompe"),
    ("你开车吗？你那里的油价是多少？写两句德语寄来。",
     "Vous conduisez ? Le prix de l'essence chez vous ? Écrivez deux phrases en allemand !"),
    ("ZEW IN KÜRZE · ZEW 指数简讯", "ZEW IN KÜRZE · ZEW en bref"),
    ("RECHNEN WIR MAL · 算一算", "RECHNEN WIR MAL · Calculons"),
    ("Die Zahlen der Woche · 本周数字", "Die Zahlen der Woche · Chiffres de la semaine"),
    ("注意：减的是税，定价的是油站。出发前比比价。",
     "Attention : c'est la taxe qui baisse — mais c'est la station-service qui fixe le prix. Comparez les prix avant de faire le plein !"),
    ("ÜBUNGEN · 第 2 版练习", "ÜBUNGEN · Exercices de la page 2"),
    ("看第 2 版文章，用数字填空。", "Lisez l'article de la page 2 et complétez avec les chiffres."),
    ("每升减税 14.04 欧分", "14,04 centimes de moins par litre"),
    ("50 升省约 8.35 欧元", "environ 8,35 euros économisés pour 50 litres"),
    ("减税到 2026 年底", "réduction jusqu'à fin 2026"),
    ("国家少收约 25 亿欧元", "l'État renonce à environ 2,5 milliards d'euros"),
    ("加油机旁的实际降幅", "la baisse réelle à la pompe, TVA comprise"),
    ("改成 Perfekt 现在完成时。", "Mettez au Perfekt (passé composé)."),
    ("fallen 用 sein", "fallen se conjugue avec sein"),
    ("weitergeben 可分动词", "weitergeben est séparable"),
    ("ZEW 预期下降", "les prévisions ZEW ont baissé"),
    ("读第 2 版文章，选出正确答案。", "Lisez l'article de la page 2 et choisissez la bonne réponse."),
    ("减的是能源税", "c'est la taxe sur l'énergie qui baisse"),
    ("油站定价", "la station-service fixe le prix"),
    ("联盟党与社民党", "Union et SPD"),
    ("家属居家护理", "les proches soignent à domicile"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = réduction du carburant b"),
    ("Zapfsäule=加油机 d", "Zapfsäule = pompe à essence d"),
    ("Mehrwertsteuer=增值税 a", "Mehrwertsteuer = TVA a"),
    ("Angehörige=亲属 c", "Angehörige = proche c"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    ("KULTUR · 文化", "KULTUR · Culture"),
    ("A2 → B1 · Ferienwechsel & Herbst · 假期交接与秋天",
     "A2 → B1 · Ferienwechsel & Herbst · Changement de vacances et automne"),
    ("der Ferienwechsel 假期交接 · die Schülerin 女学生 · der Ausflug 短途出游 · der Advent 将临期 · die Lesung 朗读会。",
     "der Ferienwechsel = changement de vacances · die Schülerin = élève · der Ausflug = excursion · der Advent = Avent · die Lesung = lecture."),
    ("der Nebel — 雾", "der Nebel — brouillard"),
    ("das Laub — 落叶", "das Laub — feuillage"),
    ("der Kürbis — 南瓜", "der Kürbis — citrouille"),
    ("die Kerze — 蜡烛", "die Kerze — bougie"),
    ("der Spaziergang — 散步", "der Spaziergang — promenade"),
    ("die Lesung — 朗读会", "die Lesung — lecture"),
    ("HERBSTWÖRTER · 秋天词汇", "HERBSTWÖRTER · Automne"),
    ("秋天你比夏天读得多吗？你的床头现在放着哪本书？写两句德语寄来。",
     "Lisez-vous plus en automne ? Votre livre de chevet ? Écrivez en allemand !"),
    ("DER TIPP · 编辑部建议", "DER TIPP · Conseil de la rédaction"),
    ("ÜBUNGEN · 第 3 版练习", "ÜBUNGEN · Exercices de la page 3"),
    ("读第 3 版文章，判断对错。", "Lisez l'article de la page 3. Vrai ou faux ?"),
    ("BW 周一起复课", "Bade-Wurtemberg reprend lundi"),
    ("巴伐利亚本周仍在放假", "la Bavière est encore en vacances cette semaine"),
    ("诸圣节 11 月 1 日", "Toussaint le 1er novembre"),
    ("10 月 31 日也是宗教改革日（九个州）", "le 31 octobre est aussi le jour de la Réforme (neuf Länder)"),
    ("诸圣节商店关门", "magasins fermés à la Toussaint"),
    ("用方框里的词填空。", "Complétez avec les mots de l'encadré."),
    ("假期交接", "changement de vacances"),
    ("去山区短途出游", "une excursion à la montagne"),
    ("图书馆的朗读会", "une lecture à la bibliothèque"),
    ("将临期在 11 月筹划", "l'Avent préparé en novembre"),
    ("湖面上的雾", "brouillard sur le lac"),
    ('e.bridge("选出正确答案。")', 'e.bridge("Choisissez la bonne réponse.")'),
    ("BW 假期已结束", "vacances finies en Bade-Wurtemberg"),
    ("安静的节日", "une fête calme"),
    ("诸圣节扫墓", "visite des tombes à la Toussaint"),
    ("白天短所以夜晚长", "jours courts, donc longues soirées"),
    ("把词组成正确的句子。", "Mettez les mots dans le bon ordre."),
    ("时间地点开头，动词第二位", "temps et lieu en tête, verbe en deuxième position"),
    ("数量时间状语，动词第二位", "complément de temps en tête, verbe en deuxième position"),
    ("主谓宾顺序", "ordre sujet–verbe–complément"),
    # P4
    ("SPORT · 体育", "SPORT · Sport"),
    ("LEVEL B1 · Europapokal & Bundesliga · 欧战与德甲",
     "LEVEL B1 · Europapokal & Bundesliga · Coupes d'Europe et Bundesliga"),
    ("die Englische Woche 一周双赛 · auswärts 客场 · empfangen 主场迎战 · der Favorit 夺冠热门 · eröffnen 揭开序幕。",
     "die Englische Woche = semaine anglaise · auswärts = à l'extérieur · empfangen = recevoir · der Favorit = favori · eröffnen = ouvrir."),
    ("本周你支持谁？周六焦点战谁赢？写两句德语寄给编辑部。",
     "Qui soutenez-vous ? Qui gagne samedi ? Écrivez deux phrases en allemand !"),
    ("DER 9. SPIELTAG · 第 9 轮赛程", "DER 9. SPIELTAG · Les matches de la 9e journée"),
    ("ÜBUNGEN · 第 4 版练习", "ÜBUNGEN · Exercices de la page 4"),
    ("读第 4 版文章，选出正确答案。", "Lisez l'article de la page 4 et choisissez la bonne réponse."),
    ("拜仁周二客战马竞", "Bayern à l'Atlético mardi"),
    ("斯图加特 18:45 开球", "Stuttgart : coup d'envoi à 18 h 45"),
    ("多特主场迎战贝蒂斯", "Dortmund reçoit le Betis"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim à Crystal Palace en Ligue Europa"),
    ("周六焦点战斯图加特–不来梅", "le grand match de samedi : Stuttgart–Brême"),
    ("Englische Woche=一周双赛 a", "Englische Woche = semaine anglaise a"),
    ("auswärts=客场 b", "auswärts = à l'extérieur b"),
    ("Favorit=热门 c", "Favorit = favori c"),
    ("eröffnen=揭开序幕 d", "eröffnen = ouvrir d"),
    ("用比较级完成句子（括号里是原级）。", "Complétez au comparatif (le mot entre parenthèses est au positif)."),
    ("spät → später（19:30 最晚）", "spät → später (19 h 30, le plus tard)"),
    ("viel → mehr（球迷想要更多）", "viel → mehr (les supporters en veulent plus)"),
    ("früh → früher（18:45 早于 21:00）", "früh → früher (18 h 45, c'est plus tôt que 21 h 00)"),
    ("看上面的赛程表，选出正确答案。", "Regardez le tableau des matches ci-dessus et choisissez la bonne réponse."),
    ("汉堡–门兴周五 20:30", "Hambourg–Gladbach vendredi 20 h 30"),
    ("斯图加特–不来梅周六 18:30", "Stuttgart–Brême samedi 18 h 30"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke dimanche 19 h 30"),
    ("弗赖堡–柏林联周日 17:30", "Fribourg–Union dimanche 17 h 30"),
    ("欧联周四霍芬海姆 18:45", "Ligue Europa jeudi, Hoffenheim à 18 h 45"),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    ("JUGEND · 青年", "JUGEND · Jeunesse"),
    ("LEVEL B1 · Zurück in die Schule · 重返校园",
     "LEVEL B1 · Zurück in die Schule · Retour à l'école"),
    ("der Pausenhof 课间操场 · die Klassenarbeit 课堂测验 · das Referat 课堂报告 · ausschlafen 睡懒觉 · die Probe 排练。",
     "der Pausenhof = cour de récréation · die Klassenarbeit = devoir sur table · das Referat = exposé · ausschlafen = faire la grasse matinée · die Probe = répétition."),
    ("der Pausenhof — 课间操场", "der Pausenhof — cour de récréation"),
    ("die Klassenarbeit — 课堂测验", "die Klassenarbeit — devoir sur table"),
    ("das Referat — 课堂报告", "das Referat — exposé"),
    ("der Rucksack — 书包", "der Rucksack — sac à dos"),
    ("ausschlafen — 睡懒觉", "ausschlafen — faire la grasse matinée"),
    ("die Probe — 排练", "die Probe — répétition"),
    ("SCHULWÖRTER · 校园词汇", "SCHULWÖRTER · Mots de l'école"),
    ("你的学校假期后哪天开学？第一节是什么课？写两句德语寄来。",
     "Quand avez-vous repris après les vacances ? Quel était votre premier cours ? Écrivez deux phrases en allemand !"),
    ("DER WOCHENPLAN DER REDAKTION · 编辑部一周计划",
     "DER WOCHENPLAN DER REDAKTION · Le programme de la rédaction"),
    ("ÜBUNGEN · 第 5 版练习", "ÜBUNGEN · Exercices de la page 5"),
    ("读第 5 版文章，选出正确答案。", "Lisez l'article de la page 5 et choisissez la bonne réponse."),
    ("BW 11 月 2 日开学", "Bade-Wurtemberg : rentrée le 2 novembre"),
    ("巴伐利亚假期未结束", "vacances pas finies en Bavière"),
    ("开学周有课堂测验", "devoirs sur table dès la première semaine"),
    ("Referat = 课堂报告", "Referat = exposé"),
    ("巴伐利亚学生周五可去球场", "les élèves bavarois peuvent aller au stade vendredi"),
    ("课间操场上玩", "jouer dans la cour de récréation"),
    ("数学课堂测验", "devoir de maths"),
    ("报告要读三本书", "trois livres à lire pour l'exposé"),
    ("假期可以睡懒觉", "faire la grasse matinée pendant les vacances"),
    ("圣诞演出的第一次排练", "première répétition du spectacle de Noël"),
    ("书包里有本子铅笔", "dans le sac : cahiers et stylos"),
    ("用 weil 连接两个句子（动词放句末）。", "Reliez les deux phrases avec weil (le verbe va à la fin)."),
    ("weil 句动词置尾", "dans une proposition en weil, le verbe va à la fin"),
    ("ist 置尾", "ist va à la fin"),
    ("muss 置尾", "muss va à la fin"),
    ("liegen 置尾", "liegen va à la fin"),
    ("判断对错。", "Vrai ou faux ?"),
    ("BW 11 月 2 日复课", "Bade-Wurtemberg : rentrée le 2 novembre"),
    ("全德假期并未都结束", "les vacances ne sont pas finies partout en Allemagne"),
    ("开学周有测验与报告", "devoirs et exposés dès la première semaine"),
    # P6
    ("VERTIEFUNG · 深读", "VERTIEFUNG · Approfondissement"),
    ("LEVEL B2 · Pflege & Stromsteuer · 护理与电力税",
     "LEVEL B2 · Pflege & Stromsteuer · Soins et taxe sur l'électricité"),
    ("der Angehörige 亲属 · die Pflegeversicherung 护理保险 · der Pflegedienst 护理服务机构 · die Stagnation 停滞 · der Aufschwung 复苏。",
     "der Angehörige = proche · die Pflegeversicherung = assurance dépendance · der Pflegedienst = service de soins · die Stagnation = stagnation · der Aufschwung = reprise."),
    ("DIE ZAHLEN · 本周数字", "DIE ZAHLEN · Chiffres"),
    ("护理：在家护理需要更多帮助——对此政界仍在争论。电力税：降多少尚未确定。两者都花钱，都关系到几乎每个家庭。",
     "Soins à domicile : il faut plus d'aide — le débat politique continue. Taxe sur l'électricité : la baisse reste à décider. Les deux coûtent cher et touchent presque chaque famille."),
    ("PRO & CONTRA · 正方与反方 — die Argumente der Debatte",
     "PRO & CONTRA · Pour et contre — les arguments du débat"),
    ("WER PFLEGT ZU HAUSE? · 谁在家护理？", "WER PFLEGT ZU HAUSE? · Qui soigne à domicile ?"),
    ("家属护理", "soins à domicile"),
    ("专业上门", "service de soins"),
    ("住养老院", "maison de retraite"),
    ("ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）",
     "ÜBUNGSDATEN · Données d'exercice — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Exemple d'exercice, pas une vraie enquête.)"),
    ("ÜBUNGEN · 第 6 版练习", "ÜBUNGEN · Exercices de la page 6"),
    ("看上面的练习图表，选出正确答案。", "Regardez le graphique d'exercice ci-dessus et choisissez la bonne réponse."),
    # residual mixed notes AFTER the chart-label reps above (order matters)
    ("service de soins 20% 第二", "service de soins 20 %, deuxième"),
    ("养老院 12% 最小", "maison de retraite 12 %, la plus petite"),
    ("养老院 12%", "maison de retraite 12 %"),
    ("读第 6 版深读文章，选出正确答案。", "Lisez l'article d'approfondissement de la page 6 et choisissez la bonne réponse."),
    ("10 月 26 日节目讨论居家护理", "l'émission du 26 octobre sur les soins à domicile"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，600 多万人需要护理",
     "selon l'émission ARD « Hart aber fair » du 26 octobre, plus de six millions de personnes ont besoin de soins"),
    ("家属居家护理", "les proches soignent à domicile"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，约 1000 万人护理亲属",
     "selon l'émission ARD « Hart aber fair » du 26 octobre, environ dix millions de personnes soignent un proche"),
    ("用括号里的形式填空。", "Complétez avec la forme entre parenthèses."),
    ("被动：wird + Partizip II", "passif : wird + Partizip II"),
    ("ob 引导间接疑问句", "ob introduit une question indirecte"),
    ("sagen 过去时 sagte", "sagen au passé : sagte"),
    ("用方框里的词填空。", "Complétez avec les mots de l'encadré."),
    ("护理保险出更多钱", "l'assurance dépendance doit payer davantage"),
    ("亲属居家护理", "les proches soignent à domicile"),
    ("走出停滞", "sortir de la stagnation"),
    ("复苏尚未自我维持", "la reprise ne se porte pas encore toute seule"),
]
rep_all("content56.py", C56)
# P6 chart labels: the bars sit at MX+470, so the label at MX+360 must end
# before x=535 (110 px at 20pt). The long note forms above would be grazed
# by the bars (35%/27%/21% coverage — one over, two under the audit's 30%
# COVER threshold, README #12 blind spot); the bars lines alone take short
# labels, while exercise notes keep the full forms.
rep("content56.py", '("pflegen Angehörige zu Hause", 68, "soins à domicile")', '("pflegen Angehörige zu Hause", 68, "domicile")')
rep("content56.py", '("nutzen einen Pflegedienst", 20, "service de soins")', '("nutzen einen Pflegedienst", 20, "service")')
rep("content56.py", '("leben im Pflegeheim", 12, "maison de retraite")', '("leben im Pflegeheim", 12, "retraite")')

# ================= content7 (P7) =================
C7 = [
    ("SPRACHE · 语言", "SPRACHE · Langue"),
    ("BEISPIELE · 例句", "BEISPIELE · Exemples"),
    ("A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所",
     "A2 → B2 · Sätze der Woche & Fehlerklinik · Phrases de la semaine et clinique des erreurs"),
    ("本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。",
     "Cette page est consacrée à la langue : trois mini-leçons, les phrases de la semaine (toutes citées mot pour mot dans les articles de ce numéro), la clinique des erreurs et le courrier des lecteurs."),
    ("被动：wird + Partizip II", "passif : wird + Partizip II"),
    ("复数：werden", "pluriel : werden"),
    ("werden + 原形表将来", "werden + infinitif pour le futur"),
    ("被动语态", "voix passive"),
    ("spät → später（19:30 最晚）", "spät → später (19 h 30, le plus tard)"),
    ("weil 引导原因", "weil introduit une cause"),
    ("weil 句动词置尾", "dans une proposition en weil, le verbe va à la fin"),
    ("länger als = 比……更长", "länger als = plus long que"),
    ("A. 比平时更长 · B. 和平时一样 · C. 比平时更短",
     "A. plus long que d'habitude · B. comme d'habitude · C. plus court que d'habitude"),
    ("ob 引导间接疑问", "ob introduit une question indirecte"),
    ("Es ist fraglich, ob ... = 是否还难说", "Es ist fraglich, ob ... = il est douteux que ..."),
    ("dass 句动词置尾", "dans une proposition en dass, le verbe va à la fin"),
    ("礼貌表达观点", "exprimer poliment une opinion"),
    ("14,04 Cent = 每升 14.04 欧分", "14,04 Cent = 14,04 centimes par litre"),
    ("rund 8,35 Euro = 大约省 8.35 欧元", "rund 8,35 Euro = environ 8,35 euros"),
    ("Es wird gespielt. = 比赛将进行（被动）", "Es wird gespielt. = On jouera (passif)"),
    ("Meiner Meinung nach ... = 在我看来……", "Meiner Meinung nach = À mon avis"),
    ("Ich finde, dass ... = 我觉得……", "Ich finde, dass ... = Je trouve que ..."),
    ("Es ist fraglich, ob ... = 是否……还难说", "Es ist fraglich, ob = Il est douteux que"),
    ("DER WERKZEUGKASTEN · 工具箱", "DER WERKZEUGKASTEN · Outils"),
    ("LESERBRIEFE · 读者来信", "LESERBRIEFE · Vos lettres"),
    ("NOCH EIN WORT · 再学一词", "NOCH EIN WORT · Un mot de plus"),
    ("«der Tankrabatt»（Seite 2）: die gesenkte Steuer auf Benzin und Diesel. 油价减税。",
     "«der Tankrabatt» (page 2) : la taxe réduite sur l'essence et le diesel. Réduction du carburant."),
    ("SÄTZE DER WOCHE · 本周金句", "SÄTZE DER WOCHE · Phrases de la semaine"),
    ("原文摘录，逐字引自本期文章 · 括号内为出处", "Citées mot pour mot dans les articles de ce numéro"),
    ("连续四个足球之夜，然后是整周末联赛。", "Quatre nuits de football d'affilée, puis tout un week-end de championnat."),
    ("汽油和柴油的能源税每升降低 14.04 欧分。", "La taxe sur l'énergie pour l'essence et le diesel baisse de 14,04 centimes par litre."),
    ("加 50 升油，大约省 8.35 欧元。", "Pour 50 litres, on économise environ 8,35 euros."),
    ("秋假过后，学校又开学了。", "L'école a repris après les vacances d'automne."),
    ("白天短，夜晚长。", "Les jours sont courts, les soirs longs."),
    ("德国球队的两场艰难客场之战。", "Deux difficiles matches à l'extérieur pour les équipes allemandes."),
    ("德国经济正在缓慢走出停滞，但复苏还不能自我维持。",
     "L'économie allemande sort lentement de la stagnation ; la reprise ne se porte pas seule."),
    ("缓慢向好——但不会自动变好。", "Ça remonte lentement — mais pas tout seul."),
    ("FEHLERKLINIK · 纠错诊所", "FEHLERKLINIK · La clinique des erreurs"),
    ("学习者最常犯的四个错 · 先自己改，再看答案",
     "Les quatre erreurs les plus fréquentes · corrigez d'abord, puis vérifiez"),
    ("动词第二位：主语不在句首时，动词仍居第二。",
     "Verbe en deuxième position : même si le sujet n'est pas en tête, le verbe reste deuxième."),
    ("halb acht = 七点半（acht 之前）。", "halb acht = 7 h 30, une demi-heure avant huit heures."),
    ("Perfekt 中 Partizip II 放句末。", "Au Perfekt, le Partizip II va à la fin."),
    ("ob 从句动词放句末。", "Dans une subordonnée en ob, le verbe va à la fin."),
    ("IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.3)", "IN DER NÄCHSTEN AUSGABE · Au prochain numéro (VOL.3)"),
]
rep_all("content7.py", C7)

# P7 readers box: label + two French paras replacing the Chinese note.
# German defer / reader / invite strings are FROZEN and stay untouched.
rep("content7.py", 'label = "Ein Beispiel der Redaktion!"',
    'label = "Un exemple de la rédaction !"', 1)
# NOTE: the core rh formula spans 5 lines (first line + 4 continuations);
# a first-line-only replacement leaves dangling continuations behind, so
# replace the WHOLE block. (The DE x EN transform had the same trap and
# was hand-fixed afterwards; this version does it in one step.)
p7 = open(os.path.join(BASE, "content7.py"), encoding="utf-8").read()
_lines = p7.splitlines()
_i = next(i for i, ln in enumerate(_lines) if ln.startswith("rh = "))
OLD_RH = "\n".join(_lines[_i:_i + 5])
assert OLD_RH.count("wrap(chinese") == 1, OLD_RH
NEW_RH = ('rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \\\n'
          '    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \\\n'
          '    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(note_fr, "sans", False, 19.5, CW - 44)) * 28 + 8 \\\n'
          '    + len(wrap(invite_fr, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 32')
rep("content7.py", OLD_RH, NEW_RH, 1)
rep("content7.py",
    'chinese = "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。"',
    'note_fr = "Aucune vraie lettre ni aucun meilleur texte de page 8 reçu ; suite en VOL.3."\n'
    'invite_fr = "Écrivez-nous vos vraies lettres — les meilleures paraîtront dans VOL.3."', 1)
rep("content7.py",
    'p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)',
    'yy3 = p.para(ix + 22, yy3 + 19.5, note_fr, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8\n'
    'p.para(ix + 22, yy3 + 20.5, invite_fr, 20.5, "serif", False, INK, CW - 44, 1.42)', 1)

# ================= content8 (P8) =================
C8 = [
    ("ÜBUNGEN & ANTWORTEN · 练习与答案", "ÜBUNGEN & ANTWORTEN · Exercices et réponses"),
    ("SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方",
     "SCHLUSSTEST · Test final · Toutes les réponses sont en bas de cette page"),
    ("spielt（第三人称单数）", "spielt (3e personne du singulier)"),
    ("beginnt（第三人称单数）", "beginnt (3e personne du singulier)"),
    ("kauft（第三人称单数）", "kauft (3e personne du singulier)"),
    ("schnitzt 雕刻南瓜", "schnitzt = sculpter une citrouille"),
    ("schläft（第三人称单数）", "schläft (3e personne du singulier)"),
    ("Tankrabatt 油价减税", "Tankrabatt = réduction du carburant"),
    ("geht（第三人称单数）", "geht (3e personne du singulier)"),
    ("erzählt（第三人称单数）", "erzählt (3e personne du singulier)"),
    ("A · LÜCKENTEXT · 完形填空", "A · LÜCKENTEXT · Texte à trous"),
    ("选项：", "Options :"),
    ("B · WISSENSFRAGEN · 综合问答", "B · WISSENSFRAGEN · Quiz"),
    ("减税到 2026 年 12 月 31 日", "réduction jusqu'au 31 décembre 2026"),
    ("拜仁周二客战马竞", "Bayern à l'Atlético mardi"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim à Crystal Palace en Ligue Europa"),
    ("BW 假期已结束", "vacances finies en Bade-Wurtemberg"),
    ("ZEW 预期 28.1", "prévisions ZEW à 28,1"),
    ("周五汉堡–门兴开轮", "Hambourg–Gladbach ouvrent vendredi"),
    ("10 月 26 日节目讨论居家护理", "l'émission du 26 octobre sur les soins à domicile"),
    ("诸圣节 11 月 1 日", "Toussaint le 1er novembre"),
    ("C · LESEVERSTEHEN · 阅读理解", "C · LESEVERSTEHEN · Lecture"),
    ("周二看拜仁客战马竞", "Bayern à l'Atlético mardi soir"),
    ("周六买南瓜", "acheter une citrouille samedi"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke dimanche 19 h 30"),
    ("D · SÄTZE BAUEN · 造句", "D · SÄTZE BAUEN · Phrases"),
    ("时间状语，动词第二位", "complément de temps en tête, verbe en deuxième position"),
    ("主谓宾顺序", "ordre sujet–verbe–complément"),
    ("时间状语开头，动词第二位", "complément de temps en tête, verbe en deuxième position"),
    ("地点开头，动词第二位", "lieu en tête, verbe en deuxième position"),
    ("E · ÜBERSETZEN · 翻译", "E · ÜBERSETZEN · Traduction"),
    ("（译成中文）", ""),
    # E keys: DE->FR re-aimed (keys change language by definition);
    # the 140 key stays German, only its prompt/instr change (below).
    ('"油价减税持续到十二月。"', '"La réduction du carburant dure jusqu\'en décembre."'),
    ('"我周二看足球。"', '"Je regarde le football mardi."'),
    ('"学校又开学了。"', '"L\'école a repris."'),
    ("laufen = 持续", "laufen = durer"),
    ("schauen = 看", "schauen = regarder"),
    ("wieder begonnen = 又开始", "wieder begonnen = avoir repris"),
    ("多睡一小时 = eine Stunde länger schlafen", "dormir une heure de plus = eine Stunde länger schlafen"),
    ("F · WÖRTER PAAREN · 词汇配对", "F · WÖRTER PAAREN · Les paires"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = réduction du carburant b"),
    ("Pflege=护理 d", "Pflege = soins d"),
    ("Advent=将临期 a", "Advent = Avent a"),
    ("Pausenhof=课间操场 c", "Pausenhof = cour de récréation c"),
    ("G · DIALOG · 对话补全", "G · DIALOG · Dialogue"),
    ("schaust（第二人称单数）", "schaust (2e personne du singulier)"),
    ("siehst（第二人称单数）", "siehst (2e personne du singulier)"),
    ("kochen（第一人称复数）", "kochen (1re personne du pluriel)"),
    ("machst（第二人称单数）", "machst (2e personne du singulier)"),
    ("gehe（第一人称单数）", "gehe (1re personne du singulier)"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "Tâche ouverte — suivez les points du cadre d'écriture ; le texte modèle est dans le cadre de cette page"),
    ("按要点给分", "Noté selon les points listés"),
    ("H · SCHREIBEN · 写作", "H · SCHREIBEN · Rédaction"),
    ("用德语写 80–100 词：《我的足球周》。写清看哪几场比赛、和谁一起、看球时吃什么，并写一句关于油价减税或护理的话。",
     "Écrivez en allemand, 80–100 mots : « Ma semaine de football ». Dites quels matches vous regardez, avec qui, et ce que vous mangez pendant le match — et ajoutez une phrase sur la réduction du carburant ou les soins. Les meilleurs textes seront publiés dans VOL.3 (page 7, « Vos lettres »)."),
    ("MUSTER · 范文（84 Wörter）", "MUSTER · Texte modèle (84 mots)"),
    ("ANTWORTEN · 全部答案与简析（第 1–8 版）", "ANTWORTEN · Toutes les réponses commentées (pages 1 à 8)"),
]
rep_all("content8.py", C8)
# ---------- generic value maps (bare text, W43 DE x FR vocabulary) ----------
TYPEMAP = [("完成句子", "à compléter"), ("单选", "QCM"),
           ("句型转换", "transformation"), ("词汇配对", "appariement"),
           ("判断对错", "vrai/faux"), ("完形填空", "texte à trous"),
           ("造句", "construction de phrase"), ("对话补全", "dialogue à compléter"),
           ("翻译", "traduction"), ("写作", "rédaction")]
INSTRMAP = [('instr="填空"', 'instr="Compléter"'),
            ('instr="改写"', 'instr="Réécrire"'),
            ('instr="判断"', 'instr="Vrai ou faux ?"'),
            ('instr="造句"', 'instr="Former une phrase"'),
            ('instr="翻译"', 'instr="Traduire en français"'),
            ('instr="把词和释义配对"', 'instr="Relier les paires"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:  # instr tokens first: TYPEMAP would corrupt instr="翻译"
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)
# E item 140: prompt becomes French, instr becomes Traduire en allemand.
# The generic INSTRMAP already turned instr="翻译" into Traduire en français
# everywhere; fix ONLY the 140 line (unique prompt literal).
rep("content8.py", '"我周日多睡一小时。（译成德语）", instr="Traduire en français"',
    '"Je dors une heure de plus le dimanche.", instr="Traduire en allemand"', 1)
# P8 keys: W43 DE x FR shipped form — half-width parens, 13pt keys,
# French page separators.
rep("content8.py", '— 第 {pg} 版 —', '— Page {pg} —', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.26, 9)', 1)

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
