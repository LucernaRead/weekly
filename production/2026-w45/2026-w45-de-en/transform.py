# -*- coding: utf-8 -*-
"""DE x EN fan-out transform for W45 DE core build copy.
Rules: whole-line or exact-unique-literal replacements with count
assertions; value maps (types/instr) use bare text, never repr.
German body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Run once from the build dir copy.
"""
import os, sys

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
    rep(f, "weekly-report-w45-de-core", "weekly-report-w45-de-en", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "for Double Ninth.", 1)

# ---------- bslib4: furniture + gloss prefix (W43 DE x EN shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"Die Lucerna · 德语周报 VOL.2 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · GERMAN WEEKLY VOL.2 · German text · English explanations"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Note — " + s', 1)

# ---------- shared furniture strings ----------
SHARED = [
    ("UND SIE? · 说说你自己", "UND SIE? · And you?"),
    ("FERIENWECHSEL · 假期交接", "FERIENWECHSEL · Holiday changeover"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Answers on page 8 · Levels mix freely — find each answer by its number"),
    ("BEISPIELE · 例句", "BEISPIELE · Examples"),
]
for f in ["content12.py", "content34.py", "content56.py"]:
    for old, new in SHARED:
        # only apply where present
        p = os.path.join(BASE, f)
        if old in open(p, encoding="utf-8").read():
            rep(f, old, new)

# ================= content12 (P1 + P2) =================
C12 = [
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语",
     "WÖCHENTLICH AUF DEUTSCH · ONE ISSUE A WEEK · THE GERMAN THAT GERMANS READ"),
    ("德 语 周 报 · VOL.2 · 足 球 周 · 油 价 · 护 理",
     "GERMAN WEEKLY · VOL.2 · FOOTBALL WEEK · FUEL DISCOUNT · CARE"),
    # P1 subtitle slot -> W43 shipped badge, verbatim string, 20pt bold olive
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEXT IN GERMAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 20, "sans", True, OLIVE, anchor="middle")'),
    ("本周足球周 · 欧冠欧联德甲连轴转", "Football week"),
    ("详见第 4 版 · Seite 4", "See page 4"),
    ("DIE TOPMELDUNG · 头条", "DIE TOPMELDUNG · Top story"),
    ("讲解｜die Englische Woche 一周双赛 · der Spieltag 比赛日 · empfangen 主场迎战 · die Bundesliga 德甲。",
     "Notes — die Englische Woche = English week · der Spieltag = matchday · empfangen = to host · die Bundesliga = Bundesliga."),
    ("DIE WOCHE IN ZAHLEN · 数字看本周", "DIE WOCHE IN ZAHLEN · Numbers"),
    ("9 — Spiele hat der 9. Spieltag der Bundesliga（德甲第 9 轮共 9 场比赛）",
     "9 — Spiele hat der 9. Spieltag der Bundesliga (9 matches in Bundesliga matchday 9)"),
    ("6 — deutsche Teams spielen in Europa（6 支德国球队出战欧战）",
     "6 — deutsche Teams spielen in Europa (6 German teams play in Europe)"),
    ("14,04 — Cent pro Liter beträgt der Tankrabatt（每升油减税 14.04 欧分）",
     "14,04 — Cent pro Liter beträgt der Tankrabatt (14.04 cents less tax per litre)"),
    ("JETZT ÜBEN · 即学即练", "JETZT ÜBEN · Practise now"),
    ("一周双赛", "English week"),
    ("多特主场迎战贝蒂斯", "Dortmund host Betis"),
    ("欧联在周四", "Europa League on Thursday"),
    ("周五汉堡–门兴开轮", "Hamburg–Gladbach open on Friday"),
    ("第 9 轮共 9 场", "9 matches on matchday 9"),
    ("减税到 12 月 31 日", "discount runs to 31 December"),
    ("拜仁周二客战马竞", "Bayern away at Atlético on Tuesday"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim away at Crystal Palace in the Europa League"),
    ("本周大问题 · Die Fragen der Woche", "This week's big questions"),
    ("德国本周最热议的五个问题。", "Germany's five hot questions."),
    ("IN DIESER AUSGABE · 本期目录", "IN DIESER AUSGABE · In this issue"),
    ("油价减税（加油折扣）。详见第 2 版。", "Fuel discount. See page 2."),
    ("KURZ & GUT · 快讯", "KURZ & GUT · In brief"),
    ("BLITZQUIZ · 闪电问答", "BLITZQUIZ · Lightning quiz"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Read page 1 and choose the right answer · Answers on page 8"),
    # P2
    ("LEBEN · 生活", "LEBEN · Life"),
    ("LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · 油价、电力税与护理",
     "LEVEL A2 · Tankrabatt, Stromsteuer & Pflege · Fuel discount, electricity tax and care"),
    ("der Tankrabatt 油价减税 · die Zapfsäule 加油机 · die Energiesteuer 能源税 · die Mehrwertsteuer 增值税 · der Angehörige 亲属。",
     "der Tankrabatt = fuel discount · die Zapfsäule = petrol pump · die Energiesteuer = energy tax · die Mehrwertsteuer = VAT · der Angehörige = relative."),
    ("AN DER ZAPFSÄULE · 加油机旁", "AN DER ZAPFSÄULE · At the pump"),
    ("你开车吗？你那里的油价是多少？写两句德语寄来。",
     "Do you drive? How much is petrol at home? Write two German sentences!"),
    ("ZEW IN KÜRZE · ZEW 指数简讯", "ZEW IN KÜRZE · ZEW in brief"),
    ("RECHNEN WIR MAL · 算一算", "RECHNEN WIR MAL · Let's calculate"),
    ("Die Zahlen der Woche · 本周数字", "Die Zahlen der Woche · This week's numbers"),
    ("注意：减的是税，定价的是油站。出发前比比价。",
     "Note: the tax falls — but the petrol station sets the price. Compare prices before you fill up!"),
    ("ÜBUNGEN · 第 2 版练习", "ÜBUNGEN · Page 2 exercises"),
    ("看第 2 版文章，用数字填空。", "Read the page 2 article and fill in the numbers."),
    ("每升减税 14.04 欧分", "14.04 cents less tax per litre"),
    ("50 升省约 8.35 欧元", "about 8.35 euros saved on 50 litres"),
    ("减税到 2026 年底", "discount runs to the end of 2026"),
    ("国家少收约 25 亿欧元", "the state gives up about 2.5 billion euros"),
    ("加油机旁的实际降幅", "the cut at the pump with VAT"),
    ("改成 Perfekt 现在完成时。", "Rewrite in the Perfekt (present perfect)."),
    ("beschließen → beschlossen", "beschließen → beschlossen"),
    ("fallen 用 sein", "fallen takes sein"),
    ("tanken → getankt", "tanken → getankt"),
    ("weitergeben 可分动词", "weitergeben is separable"),
    ("ZEW 预期下降", "ZEW expectations fell"),
    ("读第 2 版文章，选出正确答案。", "Read the page 2 article and choose the right answer."),
    ("减的是能源税", "it is the energy tax that falls"),
    ("油站定价", "the petrol station sets the price"),
    ("联盟党与社民党", "Union and SPD"),
    ("家属居家护理", "relatives care at home"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = fuel discount b"),
    ("Zapfsäule=加油机 d", "Zapfsäule = petrol pump d"),
    ("Mehrwertsteuer=增值税 a", "Mehrwertsteuer = VAT a"),
    ("Angehörige=亲属 c", "Angehörige = relative c"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    ("KULTUR · 文化", "KULTUR · Culture"),
    ("A2 → B1 · Ferienwechsel & Herbst · 假期交接与秋天",
     "A2 → B1 · Ferienwechsel & Herbst · Holiday changeover and autumn"),
    ("der Ferienwechsel 假期交接 · die Schülerin 女学生 · der Ausflug 短途出游 · der Advent 将临期 · die Lesung 朗读会。",
     "der Ferienwechsel = holiday changeover · die Schülerin = schoolgirl · der Ausflug = trip · der Advent = Advent · die Lesung = reading."),
    ("der Nebel — 雾", "der Nebel — fog"),
    ("das Laub — 落叶", "das Laub — foliage"),
    ("der Kürbis — 南瓜", "der Kürbis — pumpkin"),
    ("die Kerze — 蜡烛", "die Kerze — candle"),
    ("der Spaziergang — 散步", "der Spaziergang — walk"),
    ("die Lesung — 朗读会", "die Lesung — reading"),
    ("HERBSTWÖRTER · 秋天词汇", "HERBSTWÖRTER · Autumn words"),
    ("秋天你比夏天读得多吗？你的床头现在放着哪本书？写两句德语寄来。",
     "Read more in autumn? What book is by your bed? Write two German sentences!"),
    ("DER TIPP · 编辑部建议", "DER TIPP · Editors' tip"),
    ("ÜBUNGEN · 第 3 版练习", "ÜBUNGEN · Page 3 exercises"),
    ("读第 3 版文章，判断对错。", "Read the page 3 article. Right or wrong?"),
    ("BW 周一起复课", "Baden-Württemberg back on Monday"),
    ("巴伐利亚本周仍在放假", "Bavaria still on holiday this week"),
    ("诸圣节 11 月 1 日", "All Saints' Day is 1 November"),
    ("10 月 31 日也是宗教改革日（九个州）", "31 October is also Reformation Day in nine states"),
    ("诸圣节商店关门", "shops closed on All Saints' Day"),
    ("用方框里的词填空。", "Complete with the words from the box."),
    ("假期交接", "holiday changeover"),
    ("去山区短途出游", "a trip to the mountains"),
    ("图书馆的朗读会", "a reading at the library"),
    ("将临期在 11 月筹划", "Advent planned in November"),
    ("湖面上的雾", "fog over the lake"),
    ('e.bridge("选出正确答案。")', 'e.bridge("Choose the right answer.")'),
    ("BW 假期已结束", "Baden-Württemberg holidays over"),
    ("安静的节日", "a quiet holiday"),
    ("诸圣节扫墓", "visiting graves on All Saints' Day"),
    ("白天短所以夜晚长", "short days, so long evenings"),
    ("把词组成正确的句子。", "Put the words into a correct sentence."),
    ("时间地点开头，动词第二位", "time and place first, verb second"),
    ("数量时间状语，动词第二位", "time phrase first, verb second"),
    ("主谓宾顺序", "subject–verb–object order"),
    ("bleiben + geschlossen", "bleiben + geschlossen"),
    # P4
    ("SPORT · 体育", "SPORT · Sport"),
    ("LEVEL B1 · Europapokal & Bundesliga · 欧战与德甲",
     "LEVEL B1 · Europapokal & Bundesliga · European cups and Bundesliga"),
    ("die Englische Woche 一周双赛 · auswärts 客场 · empfangen 主场迎战 · der Favorit 夺冠热门 · eröffnen 揭开序幕。",
     "die Englische Woche = English week · auswärts = away · empfangen = to host · der Favorit = favourite · eröffnen = to open."),
    ("本周你支持谁？周六焦点战谁赢？写两句德语寄给编辑部。",
     "Who do you support this week? Who wins on Saturday? Write two sentences!"),
    ("DER 9. SPIELTAG · 第 9 轮赛程", "DER 9. SPIELTAG · Matchday 9 fixtures"),
    ("ÜBUNGEN · 第 4 版练习", "ÜBUNGEN · Page 4 exercises"),
    ("读第 4 版文章，选出正确答案。", "Read the page 4 article and choose the right answer."),
    ("拜仁周二客战马竞", "Bayern away at Atlético on Tuesday"),
    ("斯图加特 18:45 开球", "Stuttgart kick off at 18:45"),
    ("多特主场迎战贝蒂斯", "Dortmund host Betis"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim away at Crystal Palace in the Europa League"),
    ("周六焦点战斯图加特–不来梅", "Saturday's big match is Stuttgart–Bremen"),
    ("Englische Woche=一周双赛 a", "Englische Woche = English week a"),
    ("auswärts=客场 b", "auswärts = away b"),
    ("Favorit=热门 c", "Favorit = favourite c"),
    ("eröffnen=揭开序幕 d", "eröffnen = to open d"),
    ("用比较级完成句子（括号里是原级）。", "Complete with the comparative (the word in brackets is the positive form)."),
    ("schwer → schwerer", "schwer → schwerer"),
    ("spät → später（19:30 最晚）", "spät → später (19:30 is latest)"),
    ("viel → mehr（球迷想要更多）", "viel → mehr (fans want more)"),
    ("früh → früher（18:45 早于 21:00）", "früh → früher (18:45 is earlier than 21:00)"),
    ("看上面的赛程表，选出正确答案。", "Look at the fixture table above and choose the right answer."),
    ("汉堡–门兴周五 20:30", "Hamburg–Gladbach on Friday at 20:30"),
    ("斯图加特–不来梅周六 18:30", "Stuttgart–Bremen on Saturday at 18:30"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke on Sunday at 19:30"),
    ("弗赖堡–柏林联周日 17:30", "Freiburg–Union on Sunday at 17:30"),
    ("欧联周四霍芬海姆 18:45", "Europa League on Thursday, Hoffenheim at 18:45"),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    ("JUGEND · 青年", "JUGEND · Youth"),
    ("LEVEL B1 · Zurück in die Schule · 重返校园",
     "LEVEL B1 · Zurück in die Schule · Back to school"),
    ("der Pausenhof 课间操场 · die Klassenarbeit 课堂测验 · das Referat 课堂报告 · ausschlafen 睡懒觉 · die Probe 排练。",
     "der Pausenhof = schoolyard · die Klassenarbeit = class test · das Referat = class talk · ausschlafen = to sleep in · die Probe = rehearsal."),
    ("der Pausenhof — 课间操场", "der Pausenhof — schoolyard"),
    ("die Klassenarbeit — 课堂测验", "die Klassenarbeit — class test"),
    ("das Referat — 课堂报告", "das Referat — class talk"),
    ("der Rucksack — 书包", "der Rucksack — backpack"),
    ("ausschlafen — 睡懒觉", "ausschlafen — to sleep in"),
    ("die Probe — 排练", "die Probe — rehearsal"),
    ("SCHULWÖRTER · 校园词汇", "SCHULWÖRTER · School words"),
    ("你的学校假期后哪天开学？第一节是什么课？写两句德语寄来。",
     "When was your first day back? What was your first lesson? Write two sentences!"),
    ("DER WOCHENPLAN DER REDAKTION · 编辑部一周计划",
     "DER WOCHENPLAN DER REDAKTION · The editors' week"),
    ("ÜBUNGEN · 第 5 版练习", "ÜBUNGEN · Page 5 exercises"),
    ("读第 5 版文章，选出正确答案。", "Read the page 5 article and choose the right answer."),
    ("BW 11 月 2 日开学", "Baden-Württemberg back on 2 November"),
    ("巴伐利亚假期未结束", "Bavaria holidays not over"),
    ("开学周有课堂测验", "class tests coming in the first week"),
    ("Referat = 课堂报告", "Referat = class talk"),
    ("巴伐利亚学生周五可去球场", "Bavarian pupils can go to the stadium on Friday"),
    ("课间操场上玩", "playing in the schoolyard"),
    ("数学课堂测验", "a maths class test"),
    ("报告要读三本书", "three books to read for the talk"),
    ("假期可以睡懒觉", "sleeping in during the holidays"),
    ("圣诞演出的第一次排练", "the first rehearsal for Christmas"),
    ("书包里有本子铅笔", "packed bag: exercise books, pens"),
    ("用 weil 连接两个句子（动词放句末）。", "Join the two sentences with weil (the verb goes to the end)."),
    ("weil 句动词置尾", "in a weil clause the verb goes to the end"),
    ("ist 置尾", "ist goes to the end"),
    ("muss 置尾", "muss goes to the end"),
    ("liegen 置尾", "liegen goes to the end"),
    ("判断对错。", "Right or wrong?"),
    ("BW 11 月 2 日复课", "Baden-Württemberg back on 2 November"),
    ("全德假期并未都结束", "holidays not over in all of Germany"),
    ("开学周有测验与报告", "tests and talks in the first week"),
    # P6
    ("VERTIEFUNG · 深读", "VERTIEFUNG · Deep read"),
    ("LEVEL B2 · Pflege & Stromsteuer · 护理与电力税",
     "LEVEL B2 · Pflege & Stromsteuer · Care and electricity tax"),
    ("der Angehörige 亲属 · die Pflegeversicherung 护理保险 · der Pflegedienst 护理服务机构 · die Stagnation 停滞 · der Aufschwung 复苏。",
     "der Angehörige = relative · die Pflegeversicherung = care insurance · der Pflegedienst = care service · die Stagnation = stagnation · der Aufschwung = upturn."),
    ("DIE ZAHLEN · 本周数字", "DIE ZAHLEN · This week's numbers"),
    ("护理：在家护理需要更多帮助——对此政界仍在争论。电力税：降多少尚未确定。两者都花钱，都关系到几乎每个家庭。",
     "Care at home needs more help — still debated. The electricity-tax cut is still open. Both cost money and affect nearly every household."),
    ("PRO & CONTRA · 正方与反方 — die Argumente der Debatte",
     "PRO & CONTRA · For and against — the arguments of the debate"),
    ("WER PFLEGT ZU HAUSE? · 谁在家护理？", "WER PFLEGT ZU HAUSE? · Who cares at home?"),
    ("家属护理", "family care"),
    ("专业上门", "care service"),
    ("住养老院", "care home"),
    ("ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）",
     "ÜBUNGSDATEN · Practice data — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (These numbers are a practice example from the editors, not a real survey.)"),
    ("ÜBUNGEN · 第 6 版练习", "ÜBUNGEN · Page 6 exercises"),
    ("看上面的练习图表，选出正确答案。", "Look at the practice chart above and choose the right answer."),
    ("care service 20% 第二", "care service 20% is second"),  # after chart-label rep
    ("68+20=88", "68 + 20 = 88"),
    ("养老院 12% 最小", "care home 12% is smallest"),
    ("养老院 12%", "care home 12%"),
    ("68+20+12=100", "68 + 20 + 12 = 100"),
    ("读第 6 版深读文章，选出正确答案。", "Read the page 6 deep-read article and choose the right answer."),
    ("10 月 26 日节目讨论居家护理", "the 26 October programme discussed care at home"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，600 多万人需要护理",
     "per the ARD programme Hart aber fair on 26 October, over six million people need care"),
    ("家属居家护理", "relatives care at home"),
    ("据 ARD《Hart aber fair》10 月 26 日节目，约 1000 万人护理亲属",
     "per the ARD programme Hart aber fair on 26 October, about ten million people care for relatives"),
    ("用括号里的形式填空。", "Fill in with the form in brackets."),
    ("被动：wird + Partizip II", "passive: wird + past participle"),
    ("ob 引导间接疑问句", "ob introduces an indirect question"),
    ("steigen → steigt", "steigen → steigt"),
    ("sagen 过去时 sagte", "sagen in the past: sagte"),
    ("用方框里的词填空。", "Complete with the words from the box."),
    ("护理保险出更多钱", "care insurance should pay more"),
    ("亲属居家护理", "relatives care at home"),
    ("走出停滞", "coming out of stagnation"),
    ("复苏尚未自我维持", "the upturn not yet self-sustaining"),
]
rep_all("content56.py", C56)

# ================= content7 (P7) =================
C7 = [
    ("SPRACHE · 语言", "SPRACHE · Language"),
    ("BEISPIELE · 例句", "BEISPIELE · Examples"),
    ("A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所",
     "A2 → B2 · Sätze der Woche & Fehlerklinik · Sentences of the week & error clinic"),
    ("本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。",
     "This page is all about language: three short lessons, the sentences of the week (all quoted word for word from this issue's articles), the error clinic and readers' letters."),
    ("被动：wird + Partizip II", "passive: wird + past participle"),
    ("复数：werden", "plural: werden"),
    ("werden + 原形表将来", "werden + infinitive for the future"),
    ("被动语态", "passive voice"),
    ("spät → später（19:30 最晚）", "spät → später (19:30 is latest)"),
    ("weil 引导原因", "weil introduces a reason"),
    ("weil 句动词置尾", "in a weil clause the verb goes to the end"),
    ("länger als = 比……更长", "länger als = longer than"),
    ("A. 比平时更长 · B. 和平时一样 · C. 比平时更短",
     "A. longer than usual · B. the same as usual · C. shorter than usual"),
    ("ob 引导间接疑问", "ob introduces an indirect question"),
    ("Es ist fraglich, ob ... = 是否还难说", "Es ist fraglich, ob ... = it is doubtful whether ..."),
    ("dass 句动词置尾", "in a dass clause the verb goes to the end"),
    ("礼貌表达观点", "a polite way to give an opinion"),
    ("14,04 Cent = 每升 14.04 欧分", "14,04 Cent = 14.04 cents per litre"),
    ("rund 8,35 Euro = 大约省 8.35 欧元", "rund 8,35 Euro = about 8.35 euros"),
    ("Es wird gespielt. = 比赛将进行（被动）", "Es wird gespielt. = It will be played (passive)"),
    ("Meiner Meinung nach ... = 在我看来……", "Meiner Meinung nach ... = In my opinion ..."),
    ("Ich finde, dass ... = 我觉得……", "Ich finde, dass ... = I think that ..."),
    ("Es ist fraglich, ob ... = 是否……还难说", "Es ist fraglich, ob ... = It is doubtful whether ..."),
    ("DER WERKZEUGKASTEN · 工具箱", "DER WERKZEUGKASTEN · Toolbox"),
    ("LESERBRIEFE · 读者来信", "LESERBRIEFE · Readers' letters"),
    ("NOCH EIN WORT · 再学一词", "NOCH EIN WORT · One more word"),
    ("«der Tankrabatt»（Seite 2）: die gesenkte Steuer auf Benzin und Diesel. 油价减税。",
     "«der Tankrabatt» (page 2): the reduced tax on petrol and diesel. Fuel discount."),
    ("SÄTZE DER WOCHE · 本周金句", "SÄTZE DER WOCHE · Sentences of the week"),
    ("原文摘录，逐字引自本期文章 · 括号内为出处", "Quoted word for word from this issue's articles"),
    ("连续四个足球之夜，然后是整周末联赛。", "Four football nights in a row, then a whole weekend of league football."),
    ("汽油和柴油的能源税每升降低 14.04 欧分。", "The energy tax on petrol and diesel falls by 14.04 cents per litre."),
    ("加 50 升油，大约省 8.35 欧元。", "If you fill up with 50 litres, you save around 8.35 euros."),
    ("秋假过后，学校又开学了。", "School has started again after the autumn holidays."),
    ("白天短，夜晚长。", "The days are short, the evenings long."),
    ("德国球队的两场艰难客场之战。", "Two difficult away matches for the German teams."),
    ("德国经济正在缓慢走出停滞，但复苏还不能自我维持。",
     "The German economy is slowly leaving stagnation, but the upturn is not self-sustaining."),
    ("缓慢向好——但不会自动变好。", "Things are slowly looking up — but not on their own."),
    ("FEHLERKLINIK · 纠错诊所", "FEHLERKLINIK · The error clinic"),
    ("学习者最常犯的四个错 · 先自己改，再看答案",
     "Four mistakes learners make most often · correct them first, then check"),
    ("动词第二位：主语不在句首时，动词仍居第二。",
     "Verb second: even if the subject is not first, the verb stays in second position."),
    ("halb acht = 七点半（acht 之前）。", "halb acht = 7.30, half an hour before eight."),
    ("Perfekt 中 Partizip II 放句末。", "In the perfect tense, the past participle goes to the end."),
    ("ob 从句动词放句末。", "In an ob-clause, the verb goes to the end."),
    ("IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.3)", "IN DER NÄCHSTEN AUSGABE · Next issue (VOL.3)"),
]
rep_all("content7.py", C7)

# P7 readers box: label + two English paras replacing the Chinese note.
# German defer / reader / invite strings are FROZEN and stay untouched.
rep("content7.py", 'label = "Ein Beispiel der Redaktion!"',
    'label = "An example from the editors!"', 1)
OLD_RH = None
p7 = open(os.path.join(BASE, "content7.py"), encoding="utf-8").read()
for line in p7.splitlines():
    if line.startswith("rh = "):
        OLD_RH = line
        break
assert OLD_RH is not None
NEW_RH = ('rh = 62 + 30 + len(wrap(label, "sans", True, 20, CW - 44)) * 29 \\\n'
          '    + len(wrap(defer, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(reader, "serif", False, 21, CW - 44)) * 30 + 8 \\\n'
          '    + len(wrap(invite, "serif", False, 20.5, CW - 44)) * 29.5 + 8 \\\n'
          '    + len(wrap(note_en, "sans", False, 19.5, CW - 44)) * 28 + 8 \\\n'
          '    + len(wrap(invite_en, "serif", False, 20.5, CW - 44)) * 29.5 + 40 + 16')
rep("content7.py", OLD_RH, NEW_RH, 1)
rep("content7.py",
    'chinese = "编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.3。请寄来您的习作，优秀者刊登于 VOL.3。"',
    'note_en = "Editors\' example, not a real letter: no real letters and no best page-8 writing had arrived by press time, so the promise carries to VOL.3."\n'
    'invite_en = "Write to us! Send us your real letters and your page-8 writing — the best real letters will be printed in VOL.3."', 1)
rep("content7.py",
    'p.para(ix + 22, yy3 + 19.5, chinese, 19.5, "sans", False, GREY, CW - 44, 1.42)',
    'yy3 = p.para(ix + 22, yy3 + 19.5, note_en, 19.5, "sans", False, GREY, CW - 44, 1.42) + 8\n'
    'p.para(ix + 22, yy3 + 20.5, invite_en, 20.5, "serif", False, INK, CW - 44, 1.42)', 1)

# ================= content8 (P8) =================
C8 = [
    ("ÜBUNGEN & ANTWORTEN · 练习与答案", "ÜBUNGEN & ANTWORTEN · Exercises & answers"),
    ("SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方",
     "SCHLUSSTEST · Final test · All the answers are at the bottom of this page"),
    ("spielt（第三人称单数）", "spielt (3rd person singular)"),
    ("beginnt（第三人称单数）", "beginnt (3rd person singular)"),
    ("kauft（第三人称单数）", "kauft (3rd person singular)"),
    ("schnitzt 雕刻南瓜", "schnitzt = to carve a pumpkin"),
    ("schläft（第三人称单数）", "schläft (3rd person singular)"),
    ("Tankrabatt 油价减税", "Tankrabatt = fuel discount"),
    ("geht（第三人称单数）", "geht (3rd person singular)"),
    ("erzählt（第三人称单数）", "erzählt (3rd person singular)"),
    ("A · LÜCKENTEXT · 完形填空", "A · LÜCKENTEXT · Cloze"),
    ("选项：", "Options:"),
    ("B · WISSENSFRAGEN · 综合问答", "B · WISSENSFRAGEN · Quiz"),
    ("减税到 2026 年 12 月 31 日", "discount runs to 31 December 2026"),
    ("拜仁周二客战马竞", "Bayern away at Atlético on Tuesday"),
    ("霍芬海姆欧联客战水晶宫", "Hoffenheim away at Crystal Palace in the Europa League"),
    ("BW 假期已结束", "Baden-Württemberg holidays over"),
    ("ZEW 预期 28.1", "ZEW expectations at 28.1"),
    ("周五汉堡–门兴开轮", "Hamburg–Gladbach open on Friday"),
    ("10 月 26 日节目讨论居家护理", "the 26 October programme discussed care at home"),
    ("诸圣节 11 月 1 日", "All Saints' Day is 1 November"),
    ("C · LESEVERSTEHEN · 阅读理解", "C · LESEVERSTEHEN · Reading"),
    ("halb acht = 7:30", "halb acht = 7:30"),
    ("周二看拜仁客战马竞", "watching Bayern away at Atlético on Tuesday"),
    ("周六买南瓜", "buying a pumpkin on Saturday"),
    ("霍芬海姆–沙尔克周日 19:30", "Hoffenheim–Schalke on Sunday at 19:30"),
    ("D · SÄTZE BAUEN · 造句", "D · SÄTZE BAUEN · Sentences"),
    ("时间状语，动词第二位", "time phrase first, verb second"),
    ("主谓宾顺序", "subject–verb–object order"),
    ("时间状语开头，动词第二位", "time phrase first, verb second"),
    ("地点开头，动词第二位", "place first, verb second"),
    ("E · ÜBERSETZEN · 翻译", "E · ÜBERSETZEN · Translation"),
    ("（译成中文）", ""),
    # E keys: DE->EN re-aimed (keys change language by definition);
    # the 140 key stays German, only its prompt/instr change (below).
    ('"油价减税持续到十二月。"', '"The fuel discount runs until December."'),
    ('"我周二看足球。"', '"I watch football on Tuesday."'),
    ('"学校又开学了。"', '"School has started again."'),
    ("laufen = 持续", "laufen = to run, to last"),
    ("schauen = 看", "schauen = to watch"),
    ("wieder begonnen = 又开始", "wieder begonnen = started again"),
    ("多睡一小时 = eine Stunde länger schlafen", "to sleep an hour longer = eine Stunde länger schlafen"),
    ("F · WÖRTER PAAREN · 词汇配对", "F · WÖRTER PAAREN · Matching"),
    ("Tankrabatt=油价减税 b", "Tankrabatt = fuel discount b"),
    ("Pflege=护理 d", "Pflege = care d"),
    ("Advent=将临期 a", "Advent = Advent a"),
    ("Pausenhof=课间操场 c", "Pausenhof = schoolyard c"),
    ("G · DIALOG · 对话补全", "G · DIALOG · Dialogue"),
    ("schaust（第二人称单数）", "schaust (2nd person singular)"),
    ("siehst（第二人称单数）", "siehst (2nd person singular)"),
    ("kochen（第一人称复数）", "kochen (1st person plural)"),
    ("machst（第二人称单数）", "machst (2nd person singular)"),
    ("gehe（第一人称单数）", "gehe (1st person singular)"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "Open task — follow the points in the writing box; the model text is in the box on this page"),
    ("按要点给分", "Marked against the points listed"),
    ("H · SCHREIBEN · 写作", "H · SCHREIBEN · Writing"),
    ("用德语写 80–100 词：《我的足球周》。写清看哪几场比赛、和谁一起、看球时吃什么，并写一句关于油价减税或护理的话。",
     "Write in German, 80–100 words: «My football week». Say which matches you watch, with whom, and what you eat during the match — and add one sentence about the fuel discount or care. The best texts will be printed in VOL.3 (page 7, «Readers' letters»)."),
    ("MUSTER · 范文（84 Wörter）", "MUSTER · Model text (84 words)"),
    ("ANTWORTEN · 全部答案与简析（第 1–8 版）", "ANTWORTEN · All answers with notes (pages 1–8)"),
]
rep_all("content8.py", C8)
# ---------- generic value maps (bare text) ----------
TYPEMAP = [("完成句子", "fill-in"), ("单选", "multiple choice"),
           ("句型转换", "transformation"), ("词汇配对", "matching"),
           ("判断对错", "true/false"), ("完形填空", "cloze"),
           ("造句", "sentence building"), ("对话补全", "dialogue completion"),
           ("翻译", "translation"), ("写作", "writing")]
INSTRMAP = [('instr="填空"', 'instr="Fill in"'),
            ('instr="改写"', 'instr="Rewrite"'),
            ('instr="判断"', 'instr="True or false?"'),
            ('instr="造句"', 'instr="Build a sentence"'),
            ('instr="翻译"', 'instr="Translate into English"'),
            ('instr="把词和释义配对"', 'instr="Match the pairs"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:  # instr tokens first: TYPEMAP would corrupt instr="翻译"
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)
# P8 section E: first three are DE->EN (already Translate into English
# via the generic map); the fourth is reader->DE, fix its instr + prompt.
# (handled in the content8-specific block below)

# E item 140: prompt becomes English, instr becomes Translate into German.
# The generic INSTRMAP already turned instr="翻译" into Translate into
# English everywhere; fix ONLY the 140 line (unique prompt literal).
rep("content8.py", '"我周日多睡一小时。（译成德语）", instr="Translate into English"',
    '"I sleep an hour longer on Sunday.", instr="Translate into German"', 1)
# P8 keys: W43 DE x EN shipped form — half-width parens, 13pt keys,
# English page separators.
rep("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— Page {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.3, 9)', 1)

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
