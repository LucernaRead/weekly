# -*- coding: utf-8 -*-
"""EN x NL fan-out transform for the W45 EN core build copy.

Rules (same as sibling W45 fan-outs): whole-line or exact-unique-literal
replacements with count assertions; value maps use bare text, never repr.
English body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Furniture follows the SHIPPED W43 EN x NL edition
(files/weekly-report-en-nl/), which wins over any generic rule:
badge replaces the P1 subtitle slot at y=372, 19.5pt bold olive;
footer is the NL form with VOL.2; gloss prefix is "Uitleg — ";
P8 prints ALL notes at 13.5pt with half-width parens and
"— Pagina N —" separators. Run once from the build dir copy.
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
    rep(f, "weekly-report-w45-en-core", "weekly-report-w45-en-nl", 1)

# ---------- bslib4: furniture + gloss prefix (W43 shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY"',
    '"The Lucerna · ENGELS WEEKBLAD VOL.2 · TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} van {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Uitleg — " + s', 1)

# ---------- shared type tokens (registry only, never rendered as prose) ----------
# NOTE: applied LAST (see bottom of file), after all per-page mappings:
# several heads/titles contain a type word, and replacing types first
# would corrupt those heads' `old` strings.
TYPE_MAP = [
    ("完成句子", "Zinnen aanvullen"),
    ("单选", "Meerkeuze"),
    ("句型转换", "Zinnen omvormen"),
    ("词汇配对", "Woorden combineren"),
    ("跟练", "Meedoen"),
    ("改错", "Fouten verbeteren"),
    ("完形填空", "Gatentekst"),
    ("阅读理解", "Leestekst"),
    ("对话补全", "Dialoog aanvullen"),
    ("写作", "Schrijven"),
    ("图表读数", "Grafiek lezen"),
    ("翻译", "Vertalen"),
]
INSTR_MAP = [
    ('instr="填空"', 'instr="Vul in"'),
    ('instr="改写"', 'instr="Herschrijf"'),
    ('instr="把词和释义配对"', 'instr="Combineer"'),
    ('instr="配对"', 'instr="Combineer"'),
]

def apply_shared():
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        for old, new in TYPE_MAP:
            p = os.path.join(BASE, f)
            if old in open(p, encoding="utf-8").read():
                rep(f, old, new)
        for old, new in INSTR_MAP:
            p = os.path.join(BASE, f)
            if old in open(p, encoding="utf-8").read():
                rep(f, old, new)

# ================= content12 (P1 + P2) =================
C12 = [
    ("WEEKLY IN ENGLISH · 每周一期 · 读美国人正在读的英语",
     "WEEKLY IN ENGLISH · ELKE WEEK EEN NUMMER · HET ENGELS DAT AMERIKA LEEST"),
    ("英 语 周 报 · VOL.2 · 选 票 · 足 球 · 电 影",
     "ENGELS WEEKBLAD · VOL.2 · STEMMEN · VOETBAL · FILMS"),
    # P1 subtitle slot -> W43 shipped badge, verbatim string, 19.5pt bold olive
    ('p.text(975, 372, "THE LEARNERS\' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEKSTEN IN HET ENGELS · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 19.5, "sans", True, OLIVE, anchor="middle")'),
    ("周二选举日 · 周日已拨回时钟", "DINSDAG VERKIEZINGSDAG · KLOK TERUG"),
    ("11 月 3 日周二选举日 · 详见第 6 版", "Dinsdag 3 november verkiezingsdag · Zie pagina 6"),
    ("THE BIG STORY · 头条", "THE BIG STORY · Hoofdverhaal"),
    ("讲解｜a midterm 中期选举 · a ballot 选票 · a race 一场竞选 · to call a race 宣布某场竞选的结果。",
     "Uitleg — midterm = tussentijdse verkiezing · ballot = stembiljet · race = verkiezingsstrijd · to call a race = uitslag bekendmaken."),
    ("THE WEEK IN NUMBERS · 数字看本周", "THE WEEK IN NUMBERS · Cijfers"),
    ("Nov 3 — Election Day（选举日） · 435 — seats in the House, all on the ballot（众议院全部席位改选）",
     "Nov 3 — Election Day (verkiezingsdag) · 435 — seats in the House, all on the ballot (alle zetels in het Huis verkiesbaar)"),
    ("Nov 6 — two films open（两部电影上映） · Nov 8 — NFL in Madrid + F1 in São Paulo（周日两场大赛）",
     "Nov 6 — two films open (twee films) · Nov 8 — NFL in Madrid + F1 in São Paulo (twee topwedstrijden op zondag)"),
    ("TRY IT NOW · 即学即练", "TRY IT NOW · Oefen nu"),
    ("ballot = 纸选票", "ballot = stembiljet"),
    ("midterm = 中期（选举）", "midterm = tussentijds (verkiezing)"),
    ("选举日 11 月 3 日（周二）", "Verkiezingsdag: dinsdag 3 november"),
    ("early voting = 提前投票", "early voting = vervroegd stemmen"),
    ("race called = 宣布结果", "race called = uitslag bekend"),
    ("take time = 花时间", "take time = tijd kosten"),
    ("本周美国热搜 · Google Trends 美国区快照", "Deze week gezocht · Google Trends VS"),
    ("相对热度示意，非精确搜索量。", "Relatieve populariteit, geen exacte zoekcijfers."),
    ("IN THIS ISSUE · 本期目录", "IN THIS ISSUE · Inhoud"),
    ("（任期）中期。midterm election 中期选举。", "Midden van een termijn: tussentijdse verkiezing."),
    ("IN BRIEF · 快讯", "IN BRIEF · Kort nieuws"),
    ("LIGHTNING QUIZ · 闪电问答", "LIGHTNING QUIZ · Bliksemquiz"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Lees pagina 1, kies het juiste antwoord · Antwoorden op pagina 8"),
    ("选举日 11 月 3 日周二", "Verkiezingsdag: dinsdag 3 november"),
    ("众议院 435 席全部改选", "Alle 435 zetels in het Huis verkiesbaar"),
    ("美国 11 月 1 日拨回时钟", "Amerika zette op 1 november de klok terug"),
    ("NFL 马德里赛 11 月 8 日周日", "NFL-wedstrijd in Madrid op zondag 8 november"),
    # P2
    ("LIFE · 生活", "LIFE · Leven"),
    ("LEVEL A2 · Clocks, candy & your week · 时钟、糖果与你的一周",
     "LEVEL A2 · Clocks, candy & your week · Klokken, snoep en jouw week"),
    ("DO THE MATHS · 算一算", "DO THE MATHS · Reken mee"),
    ("讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。",
     "to fall back = de klok terugzetten · a costume = kostuum, verkleding · trick or treat = snoep of je leven."),
    ("周日你多睡了一小时吗？写两句英语寄给编辑部。",
     "Heb jij zondag een uur langer geslapen? Schrijf twee Engelse zinnen voor de redactie."),
    ("AND YOU ? · 说说你自己", "AND YOU ? · Vertel over jezelf"),
    ("TELLING THE TIME · 这样报时间", "TELLING THE TIME · Zo zeg je de tijd"),
    ("The repeated hour · 本周的三个时间", "The repeated hour · De drie tijden van deze week"),
    ("= two times（两次）", "= two times (twee keer)"),
    ("= one more time（再一次）", "= one more time (nog een keer)"),
    ("= to go back one hour（拨回）", "= to go back one hour (de klok terugzetten)"),
    ("= one hour more（多出一小时）", "= one hour more (een uur extra)"),
    ("EXERCISES · 第 2 版练习", "EXERCISES · Oefeningen pagina 2"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案", "Antwoorden op pagina 8 · Opgaven kunnen niveaus mixen, zoek op nummer"),
    ("根据时间，用英语补全句子。", "Vul de zinnen aan volgens de klok."),
    ("1:00 = 一点整", "1:00 = één uur precies"),
    ("1:30 = 一点半", "1:30 = half twee"),
    ("7:45 = 差一刻八点", "7:45 = kwart voor acht"),
    ("两次 = twice", "twee keer = twice"),
    ("多出的 = extra", "een extra uur = extra"),
    ("用 be going to + 动词改写（计划与将要发生的事）。", "Herschrijf met be going to + werkwoord (plannen en wat er gaat gebeuren)."),
    ("Americans 复数 → are going to", "Americans meervoud → are going to"),
    ("疑问句：be 提前", "Vraagzin: be vooraan"),
    ("读第 2 版文章，选出正确答案。", "Lees het artikel op pagina 2 en kies het juiste antwoord."),
    ("11 月 1 日凌晨 2 点拨回 1 点", "Op 1 november om 2 uur 's nachts terug naar 1 uur"),
    ("亚利桑那与夏威夷不拨钟", "Arizona en Hawaï zetten de klok niet terug"),
    ("万圣节 10 月 31 日周六", "Halloween op zaterdag 31 oktober"),
    ("11 月 1 日夜晚有 25 小时", "De nacht van 1 november duurt 25 uur"),
    ("costume=装扮 b", "costume = verkleding b"),
    ("extra hour=多出一小时 a", "extra hour = een uur extra a"),
    ("fall back=拨回 d", "fall back = de klok terugzetten d"),
    ("trick or treat=不给糖就捣蛋 c", "trick or treat = snoep of je leven c"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    # P3
    ("CULTURE · 文化", "CULTURE · Cultuur"),
    ("A2 → B1 · Friday at the movies · 周五看电影",
     "A2 → B1 · Friday at the movies · Vrijdag naar de film"),
    ("AT HOME THIS WEEK · 在家看什么", "AT HOME THIS WEEK · Thuis kijken"),
    ("讲解｜to open （电影）上映 · a monster 怪物 · a catchphrase 口头禅、金句 · a series 剧集。",
     "to open = (film) in première gaan · a monster = monster · a catchphrase = slogan, gevleugelde zin · a series = serie."),
    ("读第 3 版文章，选出正确答案。", "Lees het artikel op pagina 3 en kies het juiste antwoord."),
    ("猫咪电影 11 月 6 日周五上映", "De kattenfilm gaat op vrijdag 6 november in première"),
    ("猫出自苏斯博士的书", "De kat komt uit een boek van Dr. Seuss"),
    ("比尔·黑德为猫配音", "Bill Hader is de stem van de kat"),
    ("哥斯拉导演是山崎贵", "De regisseur van Godzilla is Takashi Yamazaki"),
    ("《黑鸽》第二季 11 月 5 日上线", "« Black Doves » seizoen 2 begint op 5 november"),
    ("周日重聚节目收尾", "De week sluit af met het reünieprogramma op zondag"),
    ("用所给词补全句子。", "Vul de zinnen aan met de gegeven woorden."),
    ("open = 上映（第三人称单数加 s）", "open = in première gaan (3e persoon enkelvoud + s)"),
    ("tall → taller 比较级", "tall → taller (vergrotende trap)"),
    ("split = 分歧的", "split = verdeeld"),
    ("monster=怪物 b", "monster = monster b"),
    ("catchphrase=金句 a", "catchphrase = slogan a"),
    ("series=剧集 d", "series = serie d"),
    ("open=上映 c", "open = in première gaan c"),
    ("用 be going to 改写。", "Herschrijf met be going to."),
    ("疑问句：be 提前", "Vraagzin: be vooraan"),
    ("THE CAT'S HAT · 猫的帽子", "THE CAT'S HAT · De hoed van de kat"),
    ("五句影评｜who、where、发生了什么、转折、结局——五句就够。",
     "Vijf zinnen | who, where, wat er gebeurde, de wending, het einde — vijf zinnen zijn genoeg."),
    # P4
    ("SPORT · 体育", "SPORT · Sport"),
    ("WHY MADRID ? · 为什么去马德里？", "WHY MADRID ? · Waarom Madrid?"),
    ("讲解｜a fixture 一场比赛（赛程） · a title 冠军头衔 · to defend （卫冕）保卫头衔 · a fan 球迷。",
     "a fixture = wedstrijd (in het speelschema) · a title = kampioenstitel · to defend = (titel) verdedigen · a fan = fan."),
    ("读第 4 版文章，选出正确答案。", "Lees het artikel op pagina 4 en kies het juiste antwoord."),
    ("马德里赛：孟加拉虎对猎鹰", "In Madrid: Bengals tegen Falcons"),
    ("马德里赛场是伯纳乌", "Het stadion in Madrid is het Bernabéu"),
    ("海豚对雄狮在迈阿密", "Dolphins tegen Lions in Miami"),
    ("F1 圣保罗大奖赛在巴西", "De Grand Prix van São Paulo is in Brazilië"),
    ("WTA 年终总决赛在印第安维尔斯开赛", "De WTA Finals beginnen in Indian Wells"),
    ("拳击赛在阿灵顿", "De bokswedstrijd is in Arlington"),
    ("defend 三单加 s", "defend + s in de 3e persoon enkelvoud"),
    ("与第 4 版原文一致，复数动词", "Zoals in het artikel op pagina 4, meervoud"),
    ("fixture=赛程中的比赛 b", "fixture = wedstrijd in het speelschema b"),
    ("title=冠军头衔 d", "title = kampioenstitel d"),
    ("fan=球迷 a", "fan = fan a"),
    ("defend=卫冕 c", "defend = titel verdedigen c"),
    ("用一般过去时改写（比赛已结束的说法）。", "Herschrijf in de verleden tijd (voor afgelopen wedstrijden)."),
    ("SUNDAY, NOVEMBER 8 · 周日赛程", "SUNDAY, NOVEMBER 8 · Zondag"),
    ("看球英语｜比分、谁得分、谁领先——短句就是直播英语。",
     "Voetbalengels | Stand, wie scoorde, wie leidt — korte zinnen zijn live Engels."),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    # P5
    ("YOUTH · 青年", "YOUTH · Jeugd"),
    ("LEVEL B1 · Election night at home · 选举之夜",
     "LEVEL B1 · Election night at home · Verkiezingsnacht"),
    ("TOO CLOSE TO CALL · 难分胜负", "TOO CLOSE TO CALL · Onbeslist"),
    ("讲解｜a map （选举）地图 · too close to call 难分胜负、无法判定 · a second screen 第二块屏幕（手机）。",
     "a map = (verkiezings)kaart · too close to call = nog niet te beslissen · a second screen = tweede scherm (telefoon)."),
    ("读第 5 版文章，选出正确答案。", "Lees het artikel op pagina 5 en kies het juiste antwoord."),
    ("用所给词补全句子。", "Vul de zinnen aan met de gegeven woorden."),
    ("地图随结果逐州变色", "De kaart kleurt mee met de resultaten, staat per staat"),
    ("too close to call = 尚不知晓", "too close to call = we weten het nog niet"),
    ("选举夜常吃披萨", "Op verkiezingsnacht eet men vaak pizza"),
    ("第二屏是手机", "Het tweede scherm is de telefoon"),
    ("孩子问为什么这么久", "Kinderen vragen waarom het zo lang duurt"),
    ("结果早上还在", "De resultaten zijn er 's ochtends nog"),
    ("close = 接近的", "close = dichtbij, spannend"),
    ("still = 仍然", "still = nog steeds"),
    ("与第 5 版原文一致，单数", "Zoals in het artikel op pagina 5, enkelvoud"),
    ("map=选举地图 c", "map = verkiezingskaart c"),
    ("race=一场竞选 d", "race = verkiezingsstrijd d"),
    ("result=结果 b", "result = uitslag b"),
    ("call=宣布胜者 a", "call = winnaar bekendmaken a"),
    ("用现在进行时改写（正在发生的事）。", "Herschrijf met de continuous-vorm (wat er nu gebeurt)."),
    ("FIVE SENTENCES · 五句话作业", "FIVE SENTENCES · Vijf zinnen"),
    ("投票结束｜The polls have closed = 该州投票已结束，计票开始。",
     "Stemmen gesloten | The polls have closed = in die staat is het stemmen voorbij, het tellen begint."),
    # P6
    ("DEEP READ · 时事深读", "DEEP READ · Verdieping"),
    ("LEVEL B2 · How America votes · 美国怎么投票",
     "LEVEL B2 · How America votes · Hoe Amerika stemt"),
    ("A PRACTICE BALLOT · 模拟选票", "A PRACTICE BALLOT · Stembiljet"),
    ("讲解｜to register 登记（选民登记） · a governor 州长 · to shape laws 影响立法 · patience 耐心。",
     "to register = je registreren (als kiezer) · a governor = gouverneur · to shape laws = wetten vormgeven · patience = geduld."),
    ("READ THE CHART · 读图表", "READ THE CHART · Grafiek"),
    ("读上面的教学图表，选出正确答案。", "Lees de oefengrafiek hierboven en kies het juiste antwoord."),
    ("38% 选“不用排队”", "38% koos « geen rijen »"),
    ("工作原因 29%", "Werk als reden: 29%"),
    ("四项合计 100%", "De vier samen: 100%"),
    ("习惯最少 12%", "Gewoonte het minst: 12%"),
    ("不用排队比旅行多 17 个百分点", "Geen rijen 17 punten meer dan reizen"),
    ("图表是教学数据非真实民调", "De grafiek is oefenmateriaal, geen echte peiling"),
    ("读第 6 版文章，选出正确答案。", "Lees het artikel op pagina 6 en kies het juiste antwoord."),
    ("各州自行组织选举", "De staten organiseren zelf de verkiezingen"),
    ("众议员任期两年", "Leden van het Huis dienen twee jaar"),
    ("参议员任期六年、每次约三分之一改选", "Senatoren dienen zes jaar, telkens ongeveer een derde verkiesbaar"),
    ("邮寄选票计票需时间", "Poststemmen tellen kost tijd"),
    ("本期不印民调与预测", "Dit nummer drukt geen peilingen of voorspellingen"),
    ("耐心是制度的一部分", "Geduld is een deel van het systeem"),
    ("shape = 影响、塑造", "shape = beïnvloeden, vormgeven"),
    ("register = 登记", "register = je registreren"),
    ("patience = 耐心", "patience = geduld"),
    ("optional = 可选的", "optional = optioneel"),
    ("differ 三单 differs", "differ → differs in de 3e persoon enkelvoud"),
    ("private = 私密的", "private = privé"),
    ("HOW LONG ? · 任期多长？", "HOW LONG ? · Hoe lang?"),
    ("一张地图｜五十个州、五十套规则——所以选举夜看的是地图，不是一个数字。",
     "Eén kaart | Vijftig staten, vijftig regels — daarom kijk je op verkiezingsnacht naar een kaart, niet naar één getal."),
]
rep_all("content56.py", C56)

# ================= content7 (P7) =================
C7 = [
    ("LANGUAGE IN HAND · 精讲", "LANGUAGE IN HAND · Taal in handen"),
    ("A2 → B2 · Phrases of the week · 本周金句",
     "A2 → B2 · Phrases of the week · Zinnen van de week"),
    ("LEVEL A2 · 基础", "LEVEL A2 · Basis"),
    ("LEVEL B1 · 进阶", "LEVEL B1 · Verder"),
    ("LEVEL B2 · 挑战", "LEVEL B2 · Uitdaging"),
    ("THE EXAMPLE · 例句", "THE EXAMPLE · Voorbeeld"),
    # B2 example box: English sentence FROZEN verbatim; only its gloss localises
    ("« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6).",
     "« Patience is part of the system, not a failure of it. » — part of = een deel (page 6)."),
    ("THE TOOLBOX · 工具箱", "THE TOOLBOX · Gereedschap"),
    ("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。",
     "Gereedschap | Drie zinnen om mee te nemen, één per niveau; alle zinnen van de week komen uit de artikelen van dit nummer — lees het artikel erbij en ze blijven hangen."),
    ("PHRASES OF THE WEEK · 本周金句（全部出自本期文章）",
     "PHRASES OF THE WEEK · Zinnen van de week (allemaal uit dit nummer)"),
    ("每句一个语法点 + 一道小题 · 答案见第 8 版",
     "Elke zin: één grammaticapunt + één opgave · Antwoorden op pagina 8"),
    # golden sentences: English originals FROZEN; only grammar points + notes localise
    ("语法点｜is = 是；日期作主语补足语。", "Grammatica | is = is; de datum als onderwerp."),
    ("语法点｜happen 的过去式是 happened，规则变化。",
     "Grammatica | verleden tijd van happen is happened, regelmatig."),
    ("语法点｜would + 动词原形，表选择意愿。", "Grammatica | would + infinitief, voor een keuze."),
    ("语法点｜that is = 那就是；破折号后总结。", "Grammatica | that is = dat is; na het streepje de samenvatting."),
    ("语法点｜will still = 仍然会；still 放在 will 之后。", "Grammatica | will still = zal nog steeds; still staat na will."),
    ("语法点｜part of = ……的一部分；not 表否定对照。", "Grammatica | part of = een deel van; not als tegenstelling."),
    ("语法点｜not every + 单数动词：并非每处都变。",
     "Grammatica | not every + werkwoord in het enkelvoud: niet elke plaats verandert."),
    ("语法点｜has = 有；the week 单数用 has。", "Grammatica | has = heeft; the week in het enkelvoud krijgt has."),
    ('"is", "is 是"', '"is", "is = zijn"'),
    ('"would", "would + 原形"', '"would", "would + infinitief"'),
    ('"is", "that is 那就是"', '"is", "that is = dat is"'),
    ('"will", "will still 仍然会"', '"will", "will still = nog steeds"'),
    ('"is", "is part of 一部分"', '"is", "is part of = een deel"'),
    # clinic
    ("THE ERROR CLINIC · 易错诊所", "THE ERROR CLINIC · Fouten"),
    ("每句有一处错误：找出来并改正。", "Elke zin bevat één fout: vind hem en verbeter de zin."),
    ("三单否定用 doesn't + 原形", "Ontkenning in de 3e persoon enkelvoud: doesn't + infinitief"),
    ("fall 的过去式是 fell", "Verleden tijd van fall is fell"),
    ("bigger 已含比较级，不要再加 more", "bigger bevat al de vergrotende trap, geen more erbij"),
    ("going to 后用动词原形", "Na going to volgt de infinitief"),
    # readers' corner: English letter FROZEN verbatim; disclosure in Dutch with
    # the 3 facts (no real letters, no best VOL.1 writing, example + promise
    # deferred to VOL.3) + an explicit imperative invitation with VOL.3 promise.
    ("READERS' CORNER · 读者园地", "READERS' CORNER · Lezershoek"),
    ("编辑说明｜VOL.1 曾承诺 VOL.2 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.1 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.3 起刊登收到的真实来信。",
     "Toelichting | VOL.1 beloofde echte brieven in VOL.2, maar er kwamen geen echte brieven en geen VOL.1-schrijfwerk binnen. We verzinnen niets: het voorbeeld blijft, eerlijk gemarkeerd. Stuur je brief in — in VOL.3 publiceren we de brieven die we ontvangen!"),
    # teaser: English paragraph FROZEN; Dutch paragraph localises
    ("NEXT WEEK · VOL.3 下周预告", "NEXT WEEK · VOL.3 Volgende week"),
    ("下周三退伍军人节，周日 NFL 慕尼黑赛；还有中期选举结果报道。",
     "Woensdag Veteranendag, zondag de NFL in München; plus verslag van de midtermresultaten."),
]
rep_all("content7.py", C7)

# ================= content8 (P8) =================
C8 = [
    ("EXERCISES & ANSWERS · 练习与答案", "EXERCISES & ANSWERS · Oefeningen en antwoorden"),
    ("FINAL TEST · 综合评估 · Answers at the bottom of this page 答案在本版下方",
     "FINAL TEST · Eindtoets · Answers at the bottom of this page · Antwoorden onderaan deze pagina"),
    ("11 月 3 日是周二", "3 november is een dinsdag"),
    ("pizza 披萨", "pizza = pizza"),
    ("map 地图逐州变色", "map = kaart die per staat kleurt"),
    ("close 接近的", "close = spannend, dichtbij"),
    ("sticker 贴纸", "sticker = sticker"),
    ("will + 动词原形 know", "will + infinitief know"),
    ("still 仍然", "still = nog steeds"),
    ("A · CLOZE · 完形填空", "A · CLOZE · Gatentekst"),
    ("选项：", "Opties:"),
    ("B · MULTIPLE CHOICE · 单选", "B · MULTIPLE CHOICE · Meerkeuze"),
    ("we → get 原形", "we → get (infinitief)"),
    ("已发生的事用 fell", "Voor iets gebeurds: fell"),
    ("than → 比较级 bigger", "than → vergrotende trap bigger"),
    ("despite + 名词：尽管下雨", "despite + zelfstandig naamwoord: ondanks de regen"),
    ("whether = 是否", "whether = of"),
    ("将来时 will + 动词原形", "Toekomst: will + infinitief"),
    ("be going to + 原形 vote", "be going to + infinitief vote"),
    ("too close to call = 难分胜负", "too close to call = nog niet te beslissen"),
    ("C · READING · 阅读理解", "C · READING · Leestekst"),
    ("原文：a teacher from Ohio", "In de tekst: a teacher from Ohio"),
    ("周二他全天教书", "Op dinsdag geeft hij de hele dag les"),
    ("贴纸上写着 I VOTED", "Op de sticker staat I VOTED"),
    ("俄亥俄一如既往难分胜负", "Ohio is als altijd nog niet beslist"),
    ("D · SENTENCES · 完成句子与转换", "D · SENTENCES · Zinnen vormen"),
    ("are going to + 原形", "are going to + infinitief"),
    ("fall → fell（不规则变化）", "fall → fell (onregelmatig)"),
    ("tall → taller（比较级）", "tall → taller (vergrotende trap)"),
    ("whether 引导“是否”从句", "whether leidt een of-zin in"),
    ("E · TRANSLATION · 翻译", "E · TRANSLATION · Vertalen"),
    # translation items: stems re-aimed EN->NL, keys re-aimed to Dutch
    ('("B2", "耐心是制度的一部分，而不是制度的失败。", "part of 一部分；not a failure 不是失败",',
     '("B2", "Geduld is een deel van het systeem, geen falen van het systeem.", "part of = een deel; not a failure = geen falen",'),
    ('"Translate : « Patience is part of the system, not a failure of it. »"',
     '"Vertaal: « Patience is part of the system, not a failure of it. »"'),
    ('("A2", "11 月 3 日周二是美国的选举日。", "Election Day 选举日；on Tuesday",',
     '("A2", "Dinsdag 3 november is verkiezingsdag in de Verenigde Staten.", "Election Day = verkiezingsdag; on Tuesday",'),
    ('"翻译：Tuesday, November 3, is Election Day in the United States."',
     '"Vertaal: Tuesday, November 3, is Election Day in the United States."'),
    ('("B1", "这周日，NFL 在马德里比赛。", "on Sunday；in Madrid",',
     '("B1", "Deze zondag speelt de NFL in Madrid.", "on Sunday = op zondag; in Madrid",'),
    ('"翻译：On Sunday, the NFL plays in Madrid."',
     '"Vertaal: On Sunday, the NFL plays in Madrid."'),
    ('("B1", "并非每处都拨回时钟。", "not every 并非每处；change 变化",',
     '("B1", "Niet elke plaats zet de klok terug.", "not every = niet elke; change = veranderen",'),
    ('"Translate : « Not every place changes. »"',
     '"Vertaal: « Not every place changes. »"'),
    ("F · WORDS · 词汇配对", "F · WORDS · Woorden combineren"),
    ("midterm = 中期选举 b", "midterm = tussentijdse verkiezing b"),
    ("governor = 州长 c", "governor = gouverneur c"),
    ("ballot = 选票 d", "ballot = stembiljet d"),
    ("turnout = 投票率 a", "turnout = opkomst a"),
    ("G · DIALOGUE · 对话补全", "G · DIALOGUE · Dialoog aanvullen"),
    ("投票时出示证件 ID", "Toon je identiteitsbewijs bij het stemmen"),
    ("line = 排队（美式英语）", "line = rij (Amerikaans Engels)"),
    ("ballot = 选票", "ballot = stembiljet"),
    ("sticker = 贴纸", "sticker = sticker"),
    ("选举日是 11 月 3 日周二", "Verkiezingsdag is dinsdag 3 november"),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")',
     'reg_ex("B1", "Schrijven", "Open vraag — punten in het schrijfblok; voorbeeldtekst in het kader op pagina 8", "Beoordeel op punten")'),
    ("H · WRITING · 写作 [B1]", "H · WRITING · Schrijven [B1]"),
    ("用英语写 80–100 词：我的 11 月 3 日周二。写清你是否看了结果、吃了什么、地图显示了什么，再写一句周日夜里拨回的时钟。",
     "Schrijf in het Engels (80–100 woorden): « Mijn dinsdag, 3 november ». Vertel of je de resultaten hebt gevolgd, wat je hebt gegeten, wat de kaart liet zien — en één zin over de klokken die op zondagnacht zijn teruggezet."),
    ("MODEL · 范文", "MODEL · Voorbeeldtekst"),
    ("ANSWERS · 全部答案与简析（第 1–8 版）", "ANSWERS · Alle antwoorden met toelichting (pagina 1–8)"),
    # P8 keys layout: all notes print, half-width parens, 13.5pt/1.26 (sibling form)
    ('kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")',
     'kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2530, tag="P8-keys")'),
    ('    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
     '    kf.para(f"— Pagina {pg} —", 16, "sans", True, OLIVE, 1.26, 3)'),
    ('        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):\n            s += f"（{e[\'note\']}）"',
     '        if e["note"]:\n            s += f" ({e[\'note\']})"'),
    ('    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)',
     '    kf.para(" · ".join(parts), 13.5, "sans", False, INK, 1.26, 9)'),
]
rep_all("content8.py", C8)

# ---------- shared tokens LAST ----------
apply_shared()

# P8 battery gaps B/C/D 11->8 (DE-sibling precedent; absorbs the E-stem +1
# line so the "Levels :" line clears the writing-strip rule). Applied AFTER
# apply_shared because the type names only exist post-mapping.
for _old, _new in [
    ('bf.ex(lv, "Meerkeuze", k, nt, body, size=20.5)', 'bf.ex(lv, "Meerkeuze", k, nt, body, size=20.5, gap=8)'),
    ('bf.ex(lv, "Leestekst", k, nt, body, size=20.5)', 'bf.ex(lv, "Leestekst", k, nt, body, size=20.5, gap=8)'),
    ('bf.ex(lv, "Zinnen aanvullen", k, nt, body, size=20.5)', 'bf.ex(lv, "Zinnen aanvullen", k, nt, body, size=20.5, gap=8)'),
]:
    rep("content8.py", _old, _new)

open(os.path.join(BASE, "transform-log.txt"), "w", encoding="utf-8").write("\n".join(LOG) + "\n")
print(f"transform done: {len(LOG)} replacements")
