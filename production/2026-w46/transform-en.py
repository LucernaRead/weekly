# -*- coding: utf-8 -*-
"""DE x EN fan-out transform for W46 DE core build copy.
Rules: whole-line or exact unique literal replacements with count
assertions; value maps (types/instr) use bare text, never repr.
German body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Run once from the build dir copy.
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
    LOG.append(f"{fname}: {n}x {old[:60]!r} -> {new[:60]!r}")
    open(p, "w", encoding="utf-8").write(s.replace(old, new))

def rep_all(fname, pairs):
    seen = set()
    for old, new in pairs:
        assert old not in seen, f"duplicate old in {fname}: {old!r}"
        seen.add(old)
    for old, new in sorted(pairs, key=lambda t: -len(t[0])):
        rep(fname, old, new)

# ---------- OUT repoint (1 per content file) ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w46-de-core", "weekly-report-w46-de-en", 1)

# ---------- svglib docstring comment only (not rendered) ----------
rep("svglib.py", "for 重阳.", "for Double Ninth.", 1)

# ---------- bslib4: furniture + gloss prefix (W45 DE x EN shipped forms, VOL.3) ----------
rep("bslib4.py",
    '"Die Lucerna · 德语周报 VOL.3 · LUCERNA GERMAN WEEKLY"',
    '"Die Lucerna · GERMAN WEEKLY VOL.3 · German text · English explanations"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Note — " + s', 1)

# ================= content12 (P1 + P2) =================
C12 = [
    ("WÖCHENTLICH AUF DEUTSCH · 每周一期 · 读德国人正在读的德语",
     "WÖCHENTLICH AUF DEUTSCH · ONE ISSUE A WEEK · THE GERMAN THAT GERMANS READ"),
    ("德 语 周 报 · VOL.3 · 国 家 队 · 圣 马 丁 · NFL",
     "GERMAN WEEKLY · VOL.3 · NATIONAL TEAM · ST MARTIN · NFL"),
    ('p.text(975, 372, "DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEXT IN GERMAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 20, "sans", True, OLIVE, anchor="middle")'),
    ("本周国家队周 · 圣马丁节与 NFL", "NATIONAL WEEK · ST MARTIN & NFL"),
    ("详见第 4 版 · Seite 4", "See page 4"),
    ("DIE TOPMELDUNG · 头条", "DIE TOPMELDUNG · Top story"),
    ("讲解｜die Länderspielpause 国家队比赛间歇期 · das Viertelfinale 四分之一决赛 · ausverkauft 售罄。",
     "Notes — die Länderspielpause = international break · das Viertelfinale = quarter-final · ausverkauft = sold out."),
    ("DIE WOCHE IN ZAHLEN · 数字看本周", "DIE WOCHE IN ZAHLEN · Numbers"),
    ("5 — Punkte hat Deutschland nach vier Spielen in der Nations League（四轮过后德国队 5 分）",
     "5 — Punkte hat Deutschland nach vier Spielen in der Nations League (Germany have 5 points after four games)"),
    ("11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln（11 点 11 分狂欢季开幕）",
     "11.11 — um 11.11 Uhr beginnt die Karnevalssession in Köln (the carnival session opens at 11.11)"),
    ("15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München（周日 15 点 30 分 NFL 开球）",
     "15.30 — um 15.30 Uhr beginnt das NFL-Spiel in München (the NFL game kicks off at 15.30 on Sunday)"),
    ("JETZT ÜBEN · 即学即练", "JETZT ÜBEN · Practise now"),
    ("国家队比赛周", "international break week"),
    ("塞尔维亚首都", "capital of Serbia"),
    ("狂欢季 11 点 11 分开幕", "carnival opens at 11.11"),
    ("NFL 在慕尼黑", "the NFL in Munich"),
    ("四轮 5 分", "5 points after four games"),
    ("周日是纪念日", "Sunday is the remembrance day"),
    ("圣马丁节 11 月 11 日", "St Martin's Day is 11 November"),
    ("11 月 11 日是星期三", "11 November is a Wednesday"),
    ("本周大问题 · Die Fragen der Woche", "Big questions · Die Fragen der Woche"),
    ("德国本周最热议的五个问题。", "Germany's five hot questions this week."),
    ("IN DIESER AUSGABE · 本期目录", "IN DIESER AUSGABE · In this issue"),
    ("空场比赛（无观众）。详见第 4 版。", "A match with no spectators. See page 4."),
    ("KURZ & GUT · 快讯", "KURZ & GUT · In brief"),
    ("BLITZQUIZ · 闪电问答", "BLITZQUIZ · Lightning quiz"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Read page 1 and choose the right answer · Answers on page 8"),
    ("周五客战塞尔维亚", "away in Serbia on Friday"),
    ("NFL 下午 3 点半开球", "NFL kick-off at 3.30 pm"),
    ("纪念日在周日", "the remembrance day is on Sunday"),
    ("LEBEN · 生活", "LEBEN · Life"),
    ("LEVEL A2 · Der 11. November & der Alltag · 11 月 11 日与日常生活",
     "LEVEL A2 · Der 11. November & der Alltag · 11 November and everyday life"),
    ("der Jeck 狂欢者（科隆方言） · die fünfte Jahreszeit 第五个季节（狂欢季） · die Laterne 灯笼 · der Weckmann 面人面包 · die Martinsgans 圣马丁鹅。",
     "der Jeck = carnival reveller (Cologne dialect) · die fünfte Jahreszeit = the fifth season (carnival) · die Laterne = lantern · der Weckmann = bread man · die Martinsgans = St Martin's goose."),
    ("DER 11. NOVEMBER · 11 月 11 日", "DER 11. NOVEMBER"),
    ("你过狂欢节还是圣马丁节？写两句德语寄来。", "Do you celebrate Karneval or St Martin? Write two German sentences!"),
    ("UND SIE? · 说说你自己", "UND SIE? · And you?"),
    ("MARTIN IN KÜRZE · 圣马丁简讯", "MARTIN IN KÜRZE · In brief"),
    ("RECHNEN WIR MAL · 算一算", "RECHNEN WIR MAL · Let's calculate"),
    ("Die Uhrzeiten der Woche · 本周时刻", "Die Uhrzeiten der Woche · This week's times"),
    ("注意：11 月 11 日是工作日。去科隆要早到：老城很挤，晚上街道属于提灯笼的孩子们。",
     "Note: 11 November is a working day. Arrive early in Cologne: the old town is crowded, and in the evening the streets belong to the children with their lanterns."),
    ("ÜBUNGEN · 第 2 版练习", "ÜBUNGEN · Page 2 exercises"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Answers on page 8 · Levels mix freely — find each answer by its number"),
    ("看第 2 版文章，用时间填空。", "Read the page 2 article and fill in the times."),
    ("WDR 10 点半直播", "WDR live from 10.30"),
    ("Weckmann 是面人面包", "a Weckmann is a bread man"),
    ("11 月 11 日不是法定假日", "11 November is not a public holiday"),
    ("圣马丁鹅配红甘蓝和丸子", "St Martin's goose with red cabbage and dumplings"),
    ("改成 Perfekt 现在完成时。", "Rewrite in the Perfekt (present perfect)."),
    ("读第 2 版文章，选出正确答案。", "Read the page 2 article and choose the right answer."),
    ("Jeck=狂欢者 c", "Jeck=carnival reveller c"),
    ("Laterne=灯笼 a", "Laterne=lantern a"),
    ("Weckmann=面人面包 b", "Weckmann=bread man b"),
    ("Martinsgans=圣马丁鹅 d", "Martinsgans=St Martin's goose d"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    ("KULTUR · 文化", "KULTUR · Culture"),
    ("A2 → B1 · St. Martin, Karneval & Rückblick · 圣马丁、狂欢节与回顾",
     "A2 → B1 · St. Martin, Karneval & Rückblick · St Martin, carnival and a look back"),
    ("der Bettler 乞丐 · der Mantel 斗篷 · das Geschnatter 鹅叫声 · der Gänsestall 鹅棚 · das Dreigestirn 狂欢节三人组。",
     "der Bettler = beggar · der Mantel = cloak · das Geschnatter = cackling · der Gänsestall = goose shed · das Dreigestirn = carnival triumvirate."),
    ("ST. MARTIN · 圣马丁", "ST. MARTIN · St Martin"),
    ("die Laterne — 灯笼", "die Laterne — lantern"),
    ("der Mantel — 斗篷", "der Mantel — cloak"),
    ("die Gans — 鹅", "die Gans — goose"),
    ("der Weckmann — 面人面包", "der Weckmann — bread man"),
    ("das Martinsfeuer — 圣马丁篝火", "das Martinsfeuer — St Martin's bonfire"),
    ("das Kostüm — 服装", "das Kostüm — costume"),
    ("MARTINSWÖRTER · 圣马丁词汇", "MARTINSWÖRTER · St Martin"),
    ("UND SIE? · 说说你自己", "UND SIE? · And you?"),
    ("你做过灯笼吗？你们国家的孩子唱什么歌？写两句德语寄来。",
     "Have you ever made a lantern? What songs do children sing in your country? Write two German sentences!"),
    ("DER TIPP · 编辑部建议", "DER TIPP · Editors' tip"),
    ("ÜBUNGEN · 第 3 版练习", "ÜBUNGEN · Page 3 exercises"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Answers on page 8 · Levels mix freely — find each answer by its number"),
    ("读第 3 版文章，判断对错。", "Read the page 3 article. Right or wrong?"),
    ("传说马丁是罗马士兵", "legend says Martin was a Roman soldier"),
    ("传说鹅叫声暴露了他", "legend says the geese gave him away"),
    ("纪念日 11 月 11 日", "memorial day is 11 November"),
    ("截稿时 11 月 3–8 日结果未知", "results of 3–8 November unknown at press time"),
    ("狂欢季 11 点 11 分开幕", "carnival opens at 11.11"),
    ("用方框里的词填空。", "Complete with the words from the box."),
    ("斗篷分给乞丐", "the cloak shared with the beggar"),
    ("纸灯笼", "a paper lantern"),
    ("圣马丁鹅", "St Martin's goose"),
    ("圣马丁鹅配红甘蓝和丸子", "St Martin's goose with red cabbage and dumplings"),
    ("狂欢节服装", "a carnival costume"),
    ("游行在篝火处结束", "the procession ends at the bonfire"),
    ("选出正确答案。", "Choose the right answer."),
    ("马丁后来成为图尔主教", "Martin later became bishop of Tours"),
    ("灯笼游行常在前后晚上举行", "lantern processions often happen on nearby evenings"),
    ("VOL.4 报道 11 月 3–8 日结果", "VOL.4 will report the 3–8 November results"),
    ("把词组成正确的句子。", "Put the words into a correct sentence."),
    ("主谓宾顺序", "subject–verb–object order"),
    ("时间状语开头，动词第二位", "time phrase first, verb second"),
    ("地点开头，动词第二位", "place first, verb second"),
    ("SPORT · 体育", "SPORT · Sport"),
    ("LEVEL B1 · Nationalelf & NFL · 国家队与 NFL",
     "LEVEL B1 · Nationalelf & NFL · National team and NFL"),
    ("das Geisterspiel 空场比赛 · das Hinspiel 首回合 · ausverkauft 售罄 · der Star 明星 · gewinnen 获胜。",
     "das Geisterspiel = ghost game · das Hinspiel = first leg · ausverkauft = sold out · der Star = star · gewinnen = to win."),
    ("你更爱看足球还是美式橄榄球？贝尔格莱德谁赢？写两句德语寄来。",
     "Football or American football? Who wins? Write two German sentences!"),
    ("DER SPIELPLAN · 本周与下周赛程", "DER SPIELPLAN · This week and next week"),
    ("ÜBUNGEN · 第 4 版练习", "ÜBUNGEN · Page 4 exercises"),
    ("读第 4 版文章，选出正确答案。", "Read the page 4 article and choose the right answer."),
    ("德国 5 分，荷兰希腊各 8 分", "Germany 5 points, Netherlands and Greece 8 each"),
    ("主教练 11 月 5 日公布名单", "the coach names the squad on 5 November"),
    ("贝尔格莱德空场", "empty stadium in Belgrade"),
    ("首回合德国 2:0 胜塞尔维亚", "Germany won the first leg 2–0 against Serbia"),
    ("NFL 慕尼黑赛售罄", "the Munich NFL game is sold out"),
    ("Geisterspiel=空场比赛 b", "Geisterspiel=ghost game b"),
    ("Hinspiel=首回合 a", "Hinspiel=first leg a"),
    ("Ausrüster=装备赞助商 c", "Ausrüster=kit supplier c"),
    ("ausverkauft=售罄 d", "ausverkauft=sold out d"),
    ("用比较级完成句子（括号里是原级）。", "Complete with the comparative (the word in brackets is the positive form)."),
    ("viel → mehr（荷兰 8 分多于德国 5 分）", "viel → mehr (the Netherlands have 8 points, more than Germany's 5)"),
    ("spät → später（15:30 晚于 11:11）", "spät → später (15.30 is later than 11.11)"),
    ("leise → leiser（空场比主场安静）", "leise → leiser (an empty stadium is quieter than a home game)"),
    ("früh → früher（11 月 5 日早于 11 月 13 日）", "früh → früher (5 November is earlier than 13 November)"),
    ("看上面的赛程表，选出正确答案。", "Look at the fixture table above and choose the right answer."),
    ("塞尔维亚–德国周五 20:45", "Serbia–Germany on Friday at 20.45"),
    ("NFL 周日 15:30", "NFL on Sunday at 15.30"),
    ("德国–荷兰周一 20:45", "Germany–Netherlands on Monday at 20.45"),
    ("拜仁–科隆周五 20:30", "Bayern–Köln on Friday at 20.30"),
    ("沙尔克–斯图加特周六 17:30", "Schalke–Stuttgart on Saturday at 17.30"),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    ("JUGEND · 青年", "JUGEND · Youth"),
    ("LEVEL B1 · Laternen, Lieder & Schule · 灯笼、歌曲与学校",
     "LEVEL B1 · Laternen, Lieder & Schule · Lanterns, songs and school"),
    ("basteln 制作 · der Pausenhof 课间操场 · sich verkleiden 乔装打扮 · die Stimmung 气氛 · der Pirat 海盗。",
     "basteln = to make, to craft · der Pausenhof = schoolyard · sich verkleiden = to dress up · die Stimmung = atmosphere · der Pirat = pirate."),
    ("SCHULWOCHE · 开学周", "SCHULWOCHE · Back to school"),
    ("die Laterne — 灯笼", "die Laterne — lantern"),
    ("basteln — 制作", "basteln — to craft"),
    ("das Lied — 歌曲", "das Lied — song"),
    ("das Kostüm — 服装", "das Kostüm — costume"),
    ("der Umzug — 游行", "der Umzug — procession"),
    ("der Stern — 星星", "der Stern — star"),
    ("MARTINSWÖRTER · 圣马丁词汇", "MARTINSWÖRTER · St Martin"),
    ("UND SIE? · 说说你自己", "UND SIE? · And you?"),
    ("你小时候做过灯笼吗？11 月你唱哪首歌？写两句德语寄来。",
     "Did you make a lantern as a child? What song do you sing in November? Write two German sentences!"),
    ("DER WOCHENPLAN DER REDAKTION · 编辑部一周计划", "DER WOCHENPLAN DER REDAKTION · The editors' week"),
    ("ÜBUNGEN · 第 5 版练习", "ÜBUNGEN · Page 5 exercises"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Answers on page 8 · Levels mix freely — find each answer by its number"),
    ("读第 5 版文章，选出正确答案。", "Read the page 5 article and choose the right answer."),
    ("11 月 9 日全德复课", "school restarts everywhere on 9 November"),
    ("孩子们做纸灯笼", "children make paper lanterns"),
    ("纸灯笼", "a paper lantern"),
    ("上午狂欢，下午圣马丁", "carnival in the morning, St Martin in the afternoon"),
    ("NFL 周日在电视上", "the NFL on TV on Sunday"),
    ("周五看国家队比赛", "watching the national team on Friday"),
    ("用方框里的词填空。", "Complete with the words from the box."),
    ("做灯笼", "making lanterns"),
    ("唱圣马丁歌曲", "singing St Martin songs"),
    ("狂欢节服装", "a carnival costume"),
    ("灯笼游行", "a lantern procession"),
    ("灯笼上的星星", "the star on the lantern"),
    ("用 weil 连接两个句子（动词放句末）。", "Join the two sentences with weil (the verb goes to the end)."),
    ("weil 句动词置尾", "in a weil clause the verb goes to the end"),
    ("ist 置尾", "ist goes to the end"),
    ("will 置尾", "will goes to the end"),
    ("beginnt 置尾", "beginnt goes to the end"),
    ("判断对错。", "Right or wrong?"),
    ("11 月 9 日巴伐利亚也复课", "Bavaria also back on 9 November"),
    ("灯笼游行在晚上", "the lantern procession is in the evening"),
    ("孩子们唱圣马丁歌曲", "children sing St Martin songs"),
    ("VERTIEFUNG · 深读", "VERTIEFUNG · Deep read"),
    ("LEVEL B2 · Volkstrauertag & Stromsteuer · 纪念日与电力税",
     "LEVEL B2 · Volkstrauertag & Stromsteuer · Remembrance day and electricity tax"),
    ("gedenken 纪念 · die Kranzniederlegung 献花圈 · der stille Tag 安静日 · die Verbundenheit 联系 · die Versöhnung 和解。",
     "gedenken = commemorate · die Kranzniederlegung = wreath-laying · der stille Tag = quiet day · Verbundenheit = bond · Versöhnung = reconciliation."),
    ("DIE ZAHLEN · 本周数字", "DIE ZAHLEN · The numbers"),
    ("纪念日：纪念需要安静——对此几乎人人赞同。电力税：降多少尚未确定。两者都关系到几乎每个家庭。",
     "Remembrance day: remembrance needs quiet — almost everyone agrees. Electricity tax: how much it falls is still open. Both affect nearly every household."),
    ("ZWEI SONNTAGE IM NOVEMBER · 十一月的两个周日", "ZWEI SONNTAGE IM NOVEMBER · Two Sundays in November"),
    ("WAS INTERESSIERT DIE LESER? · 读者最关心什么？", "WAS INTERESSIERT DIE LESER? · What interests readers?"),
    ('("Nations League und NFL", 46, "足球")', '("Nations League und NFL", 46, "football")'),
    ('("St. Martin und Karneval", 34, "节日")', '("St. Martin und Karneval", 34, "festivals")'),
    ('("Volkstrauertag und Gedenken", 20, "纪念")', '("Volkstrauertag und Gedenken", 20, "remembrance")'),
    ("ÜBUNGSDATEN · 练习数据 — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage.（本图数字为编辑部练习示例，非真实调查。）",
     "ÜBUNGSDATEN · Practice data — Diese Zahlen sind ein Übungsbeispiel der Redaktion zum Lesen von Diagrammen, keine echte Umfrage. (Practice data from the editors, not a real survey.)"),
    ("ÜBUNGEN · 第 6 版练习", "ÜBUNGEN · Page 6 exercises"),
    ("看上面的练习图表，选出正确答案。", "Use the practice chart above."),
    ("46% 足球最受关注", "football leads at 46%"),
    ("节日 34% 第二", "festivals second at 34%"),
    ("纪念 20% 最小", "remembrance smallest at 20%"),
    ("纪念 20%", "remembrance 20%"),
    ("读第 6 版深读文章，选出正确答案。", "Read the page 6 article."),
    ("11 月 15 日纪念日", "remembrance day is 15 November"),
    ("ZDF 13 点半直播纪念仪式", "ZDF live from 13.30"),
    ("家庭电力税 2.05 欧分", "household electricity tax is 2.05 cents"),
    ("2027 年预算 11 月 27 日表决", "2027 budget vote on 27 November"),
    ("用括号里的形式填空。", "Fill in with the form in brackets."),
    ("被动：wird + Partizip II", "passive: wird + past participle"),
    ("ob 引导间接疑问句", "ob introduces an indirect question"),
    ("献花圈仪式", "a wreath-laying ceremony"),
    ("为和平与和解", "for peace and reconciliation"),
    ("德奥联系", "German–Austrian connectedness"),
    ("纪念受害者", "remembering the victims"),
]
rep_all("content56.py", C56)

# ================= content7 (P7) =================
C7 = [
    ("SPRACHE · 语言", "SPRACHE · Language"),
    ("A2 → B2 · Sätze der Woche & Fehlerklinik · 本周金句与纠错诊所",
     "A2 → B2 · Sätze der Woche & Fehlerklinik · Sentences of the week & error clinic"),
    ("本版专攻语言：三节小课、本期金句（全部摘自本期文章原文）、纠错诊所和读者来信。",
     "This page is all about language: three short lessons, the sentences of the week (all quoted word for word from this issue's articles), the error clinic and readers' letters."),
    ("BEISPIELE · 例句", "BEISPIELE · Examples"),
    ("被动：wird + Partizip II", "passive: wird + past participle"),
    ("复数：werden", "plural: werden"),
    ("werden + 原形表将来", "werden + infinitive for the future"),
    ("被动语态", "passive voice"),
    ("lang → länger（夜晚比白天长）", "lang → länger (the night is longer than the day)"),
    ("weil 引导原因", "weil introduces a reason"),
    ("weil 句动词置尾", "in a weil clause the verb goes to the end"),
    ("länger als = 比……更长", "länger als = longer than"),
    ("„Länger als sonst“ heißt... A. 比平时更长 · B. 和平时一样 · C. 比平时更短",
     "„Länger als sonst“ means... A. longer than usual · B. the same as usual · C. shorter than usual"),
    ("ob 引导间接疑问", "ob introduces an indirect question"),
    ("Es ist fraglich, ob ... = 是否还难说", "Es ist fraglich, ob ... = it is doubtful whether ..."),
    ("dass 句动词置尾", "in a dass clause the verb goes to the end"),
    ("礼貌表达观点", "a polite way to give an opinion"),
    ("11.11 Uhr = 11 点 11 分", "11.11 Uhr = 11.11"),
    ("vor leeren Rängen = 空场，没有观众", "vor leeren Rängen = empty stadium"),
    ("Es wird gespielt. = 比赛将进行（被动）", "Es wird gespielt. = It will be played"),
    ("Meiner Meinung nach ... = 在我看来……", "Meiner Meinung nach = in my opinion"),
    ("Ich finde, dass ... = 我觉得……", "Ich finde, dass = I think that"),
    ("Es ist fraglich, ob ... = 是否……还难说", "Es ist fraglich, ob ... = doubtful whether"),
    ("DER WERKZEUGKASTEN · 工具箱", "DER WERKZEUGKASTEN · Toolbox"),
    ('label = "Ein Beispiel der Redaktion!"', 'label = "An example from the editors!"'),
    ("编辑部示例，非真实来信：截稿时未收到真实来信或习作，见 VOL.4。请寄来您的习作，优秀者刊登于 VOL.4。",
     "Editors' example, not a real letter: no real letters had arrived by press time. Send us yours for VOL.4!"),
    ("LESERBRIEFE · 读者来信", "LESERBRIEFE · Readers' letters"),
    ("NOCH EIN WORT · 再学一词", "NOCH EIN WORT · One more word"),
    ("«das Geisterspiel»（Seite 4）: ein Spiel ohne Zuschauer im Stadion. 空场比赛。",
     "«das Geisterspiel» (Seite 4): ein Spiel ohne Zuschauer im Stadion. A ghost game: a match with no spectators."),
    ("SÄTZE DER WOCHE · 本周金句", "SÄTZE DER WOCHE · Sentences of the week"),
    ("原文摘录，逐字引自本期文章 · 括号内为出处", "Quoted word for word from this issue's articles · source in brackets"),
    ("德甲休战——但国家队要比赛。", "The Bundesliga pauses — but the national team plays."),
    ("11 点 11 分，科隆新一季狂欢季开幕。", "At 11.11, the new carnival session begins in Cologne."),
    ("他的纪念日是 11 月 11 日。", "His memorial day is 11 November."),
    ("书包收拾好了，操场上又热闹起来。", "Bags are packed, schoolyards are loud again."),
    ("十一月黑暗，但并不安静：它歌唱、发光、庆祝。", "November is dark, but not quiet: it sings, shines and celebrates."),
    ("比赛售罄，RTL 现场直播。", "The game is sold out; RTL broadcasts live."),
    ("这里的纪念意味着：停下来、记住——并为和平与和解挺身而出。",
     "Here, remembrance means: pause, remember — and stand up for peace and reconciliation."),
    ("周日，全国一片安静。", "On Sunday, the country is quiet."),
    ("FEHLERKLINIK · 纠错诊所", "FEHLERKLINIK · The error clinic"),
    ("学习者最常犯的四个错 · 先自己改，再看答案", "Four mistakes learners make most often · correct them first, then check"),
    ("动词第二位：主语不在句首时，动词仍居第二。", "Verb second: even when the subject is not first, the verb stays second."),
    ("halb zwölf = 十一点半（zwölf 之前）。", "halb zwölf = 11.30, half an hour before zwölf."),
    ("Perfekt 中 Partizip II 放句末。", "In the Perfekt, the past participle goes to the end."),
    ("ob 从句动词放句末。", "In an ob-clause, the verb goes to the end."),
    ("IN DER NÄCHSTEN AUSGABE · 下期预告 (VOL.4)", "IN DER NÄCHSTEN AUSGABE · Next issue (VOL.4)"),
]
rep_all("content7.py", C7)

# ================= content8 (P8) =================
C8 = [
    ("ÜBUNGEN & ANTWORTEN · 练习与答案", "ÜBUNGEN & ANTWORTEN · Exercises & answers"),
    ("SCHLUSSTEST · 综合评估 · Alle Antworten unten auf dieser Seite 答案在本版下方",
     "SCHLUSSTEST · Final test · Alle Antworten unten auf dieser Seite — all answers at the bottom of this page"),
    ("beginnt（第三人称单数）", "beginnt (3rd person singular)"),
    ("bastelt（第三人称单数）", "bastelt (3rd person singular)"),
    ("geht（第三人称单数）", "geht (3rd person singular)"),
    ("singt（第三人称单数）", "singt (3rd person singular)"),
    ("schaut（第三人称单数）", "schaut (3rd person singular)"),
    ("sieht（第三人称单数）", "sieht (3rd person singular)"),
    ("erzählt（第三人称单数）", "erzählt (3rd person singular)"),
    ("A · LÜCKENTEXT · 完形填空", "A · LÜCKENTEXT · Cloze"),
    ("选项：", "Options:"),
    ("B · WISSENSFRAGEN · 综合问答", "B · WISSENSFRAGEN · Quiz"),
    ("狂欢季 11 点 11 分开幕", "carnival opens at 11.11"),
    ("周五客战塞尔维亚", "away in Serbia on Friday"),
    ("NFL 周日 15:30", "NFL on Sunday at 15.30"),
    ("纪念日 11 月 15 日", "remembrance day is 15 November"),
    ("家庭电力税 2.05 欧分", "household electricity tax is 2.05 cents"),
    ("主教练 11 月 5 日公布名单", "the coach names the squad on 5 November"),
    ("ZDF 13 点半直播纪念仪式", "ZDF live from 13.30"),
    ("亡灵主日 11 月 22 日", "Totensonntag is 22 November"),
    ("C · LESEVERSTEHEN · 阅读理解", "C · LESEVERSTEHEN · Reading"),
    ("周三做灯笼", "making a lantern on Wednesday"),
    ("周五看德国队", "watching Germany on Friday"),
    ("D · SÄTZE BAUEN · 造句", "D · SÄTZE BAUEN · Sentences"),
    ("时间状语，动词第二位", "time phrase, verb second"),
    ("主谓宾顺序", "subject–verb–object order"),
    ("时间状语开头，动词第二位", "time phrase first, verb second"),
    ("地点时间开头，动词第二位", "place and time first, verb second"),
    ("E · ÜBERSETZEN · 翻译", "E · ÜBERSETZEN · Translation"),
    ("狂欢节 11 点 11 分在科隆开幕。", "The carnival opens at 11.11 in Cologne."),
    ("beginnen = 开始", "beginnen = to begin"),
    ("Der Karneval beginnt um 11.11 Uhr in Köln.（译成中文）", "Der Karneval beginnt um 11.11 Uhr in Köln. (translate into English)"),
    ("我周三做一个灯笼。", "I make a lantern on Wednesday."),
    ("basteln = 制作", "basteln = to make, to craft"),
    ("Ich bastle am Mittwoch eine Laterne.（译成中文）", "Ich bastle am Mittwoch eine Laterne. (translate into English)"),
    ("学校 11 月 9 日又开学了。", "School started again on 9 November."),
    ("wieder begonnen = 又开始", "wieder begonnen = started again"),
    ("Die Schule hat am 9. November wieder begonnen.（译成中文）", "Die Schule hat am 9. November wieder begonnen. (translate into English)"),
    ("看比赛 = das Spiel schauen", "to watch a game = das Spiel schauen"),
    ('"我周日看 NFL 比赛。（译成德语）", instr="翻译"',
     '"I watch the NFL game on Sunday. (translate into German)", instr="Translate into German"'),
    ("F · WÖRTER PAAREN · 词汇配对", "F · WÖRTER PAAREN · Matching"),
    ("Mantel=斗篷 b", "Mantel=cloak b"),
    ("Laterne=灯笼 a", "Laterne=lantern a"),
    ("Geisterspiel=空场比赛 d", "Geisterspiel=ghost game d"),
    ("Versöhnung=和解 c", "Versöhnung=reconciliation c"),
    ("singst（第二人称单数）", "singst (2nd person singular)"),
    ("macht（第二人称复数）", "macht (2nd person plural)"),
    ("essen（第一人称复数）", "essen (1st person plural)"),
    ("machst（第二人称单数）", "machst (2nd person singular)"),
    ("schaue（第一人称单数）", "schaue (1st person singular)"),
    ("G · DIALOG · 对话补全", "G · DIALOG · Dialogue"),
    ("开放题 — 要点见写作框，范文在第 8 版写作框内",
     "Open task — follow the points in the writing box; the model text is in the box on this page"),
    ("按要点给分", "Marked against the points listed"),
    ("H · SCHREIBEN · 写作", "H · SCHREIBEN · Writing"),
    ("用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于圣马丁节或纪念日的话。",
     "Write in German, 80–100 words: «My week in November». Say what you make, which games you watch and with whom — and add one sentence about St Martin's Day or the remembrance day."),
    ("MUSTER · 范文（84 Wörter）", "MUSTER · Model text (84 words)"),
    ("ANTWORTEN · 全部答案与简析（第 1–8 版）", "ANTWORTEN · All answers with notes (pages 1–8)"),
]
rep_all("content8.py", C8)
# P8 keys: W45 DE x EN shipped form — half-width parens, 13pt keys,
# English page separators.
rep("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
    'kf.para(f"— Page {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1)
rep("content8.py", 's += f"（{e[\'note\']}）"', 's += f"({e[\'note\']})"', 1)
rep("content8.py", 'kf.para(" · ".join(parts), 14.5, "sans", False, INK, 1.3, 9)',
    'kf.para(" · ".join(parts), 13, "sans", False, INK, 1.3, 9)', 1)

# ---------- generic value maps (bare text, quoted) ----------
TYPEMAP = [('"完成句子"', '"fill-in"'), ('"单选"', '"multiple choice"'),
           ('"句型转换"', '"transformation"'), ('"词汇配对"', '"matching"'),
           ('"判断对错"', '"true/false"'), ('"完形填空"', '"cloze"'),
           ('"造句"', '"sentence building"'), ('"对话补全"', '"dialogue completion"'),
           ('"翻译"', '"translation"'), ('"写作"', '"writing"')]
INSTRMAP = [('instr="填空"', 'instr="Fill in"'),
            ('instr="改写"', 'instr="Rewrite"'),
            ('instr="判断"', 'instr="True or false?"'),
            ('instr="造句"', 'instr="Build a sentence"'),
            ('instr="翻译"', 'instr="Translate into English"'),
            ('instr="把词和释义配对"', 'instr="Match the pairs"')]
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    for old, new in INSTRMAP + TYPEMAP:
        pth = os.path.join(BASE, f)
        n = open(pth, encoding="utf-8").read().count(old)
        if n == 0:
            LOG.append(f"{f}: 0x {old!r} (absent, skipped)")
        else:
            rep(f, old, new)

# ---------- final CJK leak check ----------
import re
CJK = re.compile(r'[\u4e00-\u9fff]')
leaks = {}
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
    for i, line in enumerate(open(os.path.join(BASE, f), encoding="utf-8"), 1):
        if CJK.search(line):
            leaks.setdefault(f, []).append((i, line.strip()[:80]))
print("CJK leaks:", leaks if leaks else "NONE")
assert not leaks, "CJK strings remain after transform"

print("\n".join(LOG))
print(f"TOTAL replacements: {len(LOG)}")
