# -*- coding: utf-8 -*-
"""EN x DE fan-out transform for W45 EN core build copy.

Rules (same as sibling W45 fan-outs): whole-line or exact-unique-literal
replacements with count assertions; value maps use bare text, never repr.
English body text is NEVER touched: every `old` below is a Chinese
explanation-layer string, a bilingual furniture string, or a generic
type/instr token. Furniture follows the SHIPPED W43 EN x DE edition
(files/weekly-report-en-de/), which wins over any generic rule:
badge replaces the P1 subtitle slot at y=372, 19.5pt bold olive;
footer is the English-form exception with VOL.2; gloss prefix is
"Anmerkung | "; P8 prints ALL notes at 13.5pt with half-width parens
and "--- Seite N ---" separators. Run once from the build dir copy.
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
    rep(f, "weekly-report-w45-en-core", "weekly-report-w45-en-de", 1)

# ---------- bslib4: furniture + gloss prefix (W43 shipped forms, VOL.2) ----------
rep("bslib4.py",
    '"The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY"',
    '"The Lucerna · ENGLISH WEEKLY VOL.2 · Englischer Text · Deutsche Erklärungen"', 1)
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"', 1)
rep("bslib4.py", '"译注｜" + s', '"Anmerkung | " + s', 1)

# ---------- shared type tokens (registry only, never rendered as prose) ----------
# NOTE: applied LAST (see bottom of file), after all per-page mappings:
# several heads/titles contain a type word, and replacing types first
# would corrupt those heads' `old` strings.
TYPE_MAP = [
    ("完成句子", "Satzergänzung"),
    ("单选", "Multiple Choice"),
    ("句型转换", "Umformung"),
    ("词汇配对", "Zuordnung"),
    ("跟练", "Anwendungsübung"),
    ("改错", "Fehlerkorrektur"),
    ("完形填空", "Lückentext"),
    ("阅读理解", "Leseverstehen"),
    ("对话补全", "Dialogergänzung"),
    ("写作", "Schreiben"),
    ("图表读数", "Diagrammlesen"),
]
INSTR_MAP = [
    ('instr="填空"', 'instr="Ergänze"'),
    ('instr="改写"', 'instr="Schreibe um"'),
    ('instr="把词和释义配对"', 'instr="Ordne zu"'),
    ('instr="配对"', 'instr="Ordne zu"'),
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
     "WEEKLY IN ENGLISH · Jede Woche neu · Englisch, wie Amerika es liest"),
    ("英 语 周 报 · VOL.2 · 选 票 · 足 球 · 电 影",
     "ENGLISCHES WOCHENBLATT · VOL.2 · WAHLEN · FUSSBALL · FILME"),
    # P1 subtitle slot -> W43 shipped badge, verbatim string, 19.5pt bold olive
    ('p.text(975, 372, "THE LEARNERS\' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "ENGLISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 19.5, "sans", True, OLIVE, anchor="middle")'),
    ("周二选举日 · 周日已拨回时钟", "DIENSTAG WAHLTAG · SONNTAG ZURÜCKGESTELLT"),
    ("11 月 3 日周二选举日 · 详见第 6 版", "Dienstag, 3. November, Wahltag · Siehe Seite 6"),
    ("THE BIG STORY · 头条", "THE BIG STORY · Schlagzeile"),
    ("讲解｜a midterm 中期选举 · a ballot 选票 · a race 一场竞选 · to call a race 宣布某场竞选的结果。",
     "Erklärung | a midterm = Zwischenwahl · a ballot = Stimmzettel · a race = Wahlkampf, Rennen · to call a race = ein Rennen entscheiden."),
    ("THE WEEK IN NUMBERS · 数字看本周", "THE WEEK IN NUMBERS · Zahlen der Woche"),
    ("Nov 3 — Election Day（选举日） · 435 — seats in the House, all on the ballot（众议院全部席位改选）",
     "Nov 3 — Election Day (Wahltag) · 435 — seats in the House, all on the ballot (alle Sitze im Repräsentantenhaus neu zu wählen)"),
    ("Nov 6 — two films open（两部电影上映） · Nov 8 — NFL in Madrid + F1 in São Paulo（周日两场大赛）",
     "Nov 6 — two films open (zwei Filme starten) · Nov 8 — NFL in Madrid + F1 in São Paulo (zwei große Spiele am Sonntag)"),
    ("TRY IT NOW · 即学即练", "TRY IT NOW · Jetzt üben"),
    ("ballot = 纸选票", "ballot = Stimmzettel"),
    ("midterm = 中期（选举）", "midterm = Zwischenwahl"),
    ("选举日 11 月 3 日（周二）", "Wahltag: Dienstag, 3. November"),
    ("early voting = 提前投票", "early voting = vorzeitige Stimmabgabe"),
    ("race called = 宣布结果", "race called = Rennen entschieden"),
    ("take time = 花时间", "take time = Zeit brauchen"),
    ("本周美国热搜 · Google Trends 美国区快照", "Diese Woche in den USA gesucht · Google-Trends-Schnappschuss USA"),
    ("相对热度示意，非精确搜索量。", "Relative Beliebtheit, keine exakten Suchzahlen."),
    ("IN THIS ISSUE · 本期目录", "IN THIS ISSUE · Inhalt"),
    ("（任期）中期。midterm election 中期选举。", "Mitte (einer Amtszeit). midterm election = Zwischenwahl."),
    ("IN BRIEF · 快讯", "IN BRIEF · Kurz gemeldet"),
    ("LIGHTNING QUIZ · 闪电问答", "LIGHTNING QUIZ · Blitzquiz"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Lies Seite 1, wähle die richtige Antwort · Lösungen auf Seite 8"),
    ("选举日 11 月 3 日周二", "Wahltag: Dienstag, 3. November"),
    ("众议院 435 席全部改选", "Alle 435 Sitze im Repräsentantenhaus neu zu wählen"),
    ("美国 11 月 1 日拨回时钟", "Die USA stellten am 1. November zurück"),
    ("NFL 马德里赛 11 月 8 日周日", "NFL-Spiel in Madrid am Sonntag, 8. November"),
    # P2
    ("LIFE · 生活", "LIFE · Leben"),
    ("LEVEL A2 · Clocks, candy & your week · 时钟、糖果与你的一周",
     "LEVEL A2 · Clocks, candy & your week · Uhren, Süßes und deine Woche"),
    ("DO THE MATHS · 算一算", "DO THE MATHS · Rechne mit"),
    ("讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。",
     "to fall back = (Uhren) zurückstellen · a costume = Kostüm, Verkleidung · trick or treat = Süßes oder Saures."),
    ("周日你多睡了一小时吗？写两句英语寄给编辑部。",
     "Hast du am Sonntag eine Stunde länger geschlafen? Schreibe zwei englische Sätze an die Redaktion!"),
    ("AND YOU ? · 说说你自己", "AND YOU ? · Und du ?"),
    ("TELLING THE TIME · 这样报时间", "TELLING THE TIME · So sagt man die Uhrzeit"),
    ("The repeated hour · 本周的三个时间", "The repeated hour · Die drei Uhrzeiten der Woche"),
    ("= two times（两次）", "= two times (zweimal)"),
    ("= one more time（再一次）", "= one more time (noch einmal)"),
    ("= to go back one hour（拨回）", "= to go back one hour (Uhren zurückstellen)"),
    ("= one hour more（多出一小时）", "= one hour more (eine Stunde mehr)"),
    ("EXERCISES · 第 2 版练习", "EXERCISES · Übungen zu Seite 2"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案", "Antworten auf Seite 8 · Nach Nummern suchen"),
    ("根据时间，用英语补全句子。", "Ergänze die Sätze auf Englisch nach der Uhrzeit."),
    ("1:00 = 一点整", "1:00 = ein Uhr"),
    ("1:30 = 一点半", "1:30 = halb zwei"),
    ("7:45 = 差一刻八点", "7:45 = Viertel vor acht"),
    ("两次 = twice", "zweimal = twice"),
    ("多出的 = extra", "extra = zusätzlich"),
    ("用 be going to + 动词改写（计划与将要发生的事）。", "Schreibe mit be going to um (Pläne und was geschehen wird)."),
    ("Americans 复数 → are going to", "Americans (Plural) → are going to"),
    ("疑问句：be 提前", "Fragesatz: be steht vorn"),
    ("读第 2 版文章，选出正确答案。", "Lies Seite 2, wähle die richtige Antwort."),
    ("11 月 1 日凌晨 2 点拨回 1 点", "Am 1. November um 2 Uhr nachts auf 1 Uhr zurückgestellt"),
    ("亚利桑那与夏威夷不拨钟", "Arizona und Hawaii stellen nicht um"),
    ("万圣节 10 月 31 日周六", "Halloween war Samstag, der 31. Oktober"),
    ("11 月 1 日夜晚有 25 小时", "Die Nacht des 1. November hat 25 Stunden"),
    ("costume=装扮 b", "costume = Kostüm b"),
    ("extra hour=多出一小时 a", "extra hour = eine Stunde mehr a"),
    ("fall back=拨回 d", "fall back = Uhren zurückstellen d"),
    ("trick or treat=不给糖就捣蛋 c", "trick or treat = Süßes oder Saures c"),
]
rep_all("content12.py", C12)

# ================= content34 (P3 + P4) =================
C34 = [
    ("CULTURE · 文化", "CULTURE · Kultur"),
    ("A2 → B1 · Friday at the movies · 周五看电影", "A2 → B1 · Friday at the movies · Freitag im Kino"),
    ("AT HOME THIS WEEK · 在家看什么", "AT HOME THIS WEEK · Diese Woche zu Hause"),
    ("讲解｜to open （电影）上映 · a monster 怪物 · a catchphrase 口头禅、金句 · a series 剧集。",
     "to open = (Film) anlaufen, starten · a monster = Monster · a catchphrase = Spruch · a series = Serie."),
    ("读第 3 版文章，选出正确答案。", "Lies Seite 3, wähle die richtige Antwort."),
    ("猫咪电影 11 月 6 日周五上映", "Der Katzenfilm startet Freitag, den 6. November"),
    ("猫出自苏斯博士的书", "Die Katze stammt aus einem Buch von Dr. Seuss"),
    ("比尔·黑德为猫配音", "Bill Hader spricht die Katze"),
    ("哥斯拉导演是山崎贵", "Godzilla-Regisseur ist Takashi Yamazaki"),
    ("《黑鸽》第二季 11 月 5 日上线", "« Black Doves » Staffel 2 startet am 5. November"),
    ("周日重聚节目收尾", "Am Sonntag schließt die Reunion-Sendung die Woche"),
    ("用所给词补全句子。", "Ergänze die Sätze mit den Wörtern."),
    ("open = 上映（第三人称单数加 s）", "open = anlaufen (3. Person Singular mit -s)"),
    ("tall → taller 比较级", "tall → taller (Komparativ)"),
    ("split = 分歧的", "split = uneins, geteilt"),
    ("monster=怪物 b", "monster = Monster b"),
    ("catchphrase=金句 a", "catchphrase = Spruch a"),
    ("series=剧集 d", "series = Serie d"),
    ("open=上映 c", "open = anlaufen c"),
    ("用 be going to 改写。", "Schreibe mit be going to um."),
    ("疑问句：be 提前", "Fragesatz: be steht vorn"),
    ("THE CAT'S HAT · 猫的帽子", "THE CAT'S HAT · Der Hut der Katze"),
    ("五句影评｜who、where、发生了什么、转折、结局——五句就够。",
     "Fünf Sätze | who, where, was geschah, die Wende, das Ende — fünf Sätze genügen."),
    # P4
    ("SPORT · 体育", "SPORT · Sport"),
    ("WHY MADRID ? · 为什么去马德里？", "WHY MADRID ? · Warum Madrid?"),
    ("讲解｜a fixture 一场比赛（赛程） · a title 冠军头衔 · to defend （卫冕）保卫头衔 · a fan 球迷。",
     "a fixture = Spiel (im Spielplan) · a title = Titel · to defend = (Titel) verteidigen · a fan = Fan."),
    ("读第 4 版文章，选出正确答案。", "Lies Seite 4, wähle die richtige Antwort."),
    ("马德里赛：孟加拉虎对猎鹰", "Madrid-Spiel: Bengals gegen Falcons"),
    ("马德里赛场是伯纳乌", "Das Madrid-Spiel ist im Bernabéu"),
    ("海豚对雄狮在迈阿密", "Dolphins gegen Lions in Miami"),
    ("F1 圣保罗大奖赛在巴西", "Der São-Paulo-Grand-Prix ist in Brasilien"),
    ("WTA 年终总决赛在印第安维尔斯开赛", "Die WTA Finals beginnen in Indian Wells"),
    ("拳击赛在阿灵顿", "Der Boxkampf ist in Arlington"),
    ("defend 三单加 s", "defend, 3. Person Singular mit -s"),
    ("与第 4 版原文一致，复数动词", "Wie im Text auf Seite 4, Verb im Plural"),
    ("fixture=赛程中的比赛 b", "fixture = Spiel im Spielplan b"),
    ("title=冠军头衔 d", "title = Titel d"),
    ("fan=球迷 a", "fan = Fan a"),
    ("defend=卫冕 c", "defend = Titel verteidigen c"),
    ("用一般过去时改写（比赛已结束的说法）。", "Schreibe im Past Simple um (für beendete Spiele)."),
    ("SUNDAY, NOVEMBER 8 · 周日赛程", "SUNDAY, NOVEMBER 8 · Spiele am Sonntag"),
    ("看球英语｜比分、谁得分、谁领先——短句就是直播英语。",
     "Fußball-Englisch | Spielstand, wer traf, wer führt — kurze Sätze sind Live-Englisch."),
]
rep_all("content34.py", C34)

# ================= content56 (P5 + P6) =================
C56 = [
    ("YOUTH · 青年", "YOUTH · Jugend"),
    ("LEVEL B1 · Election night at home · 选举之夜", "LEVEL B1 · Election night at home · Wahlnacht zu Hause"),
    ("TOO CLOSE TO CALL · 难分胜负", "TOO CLOSE TO CALL · Zu knapp, um es zu entscheiden"),
    ("讲解｜a map （选举）地图 · too close to call 难分胜负、无法判定 · a second screen 第二块屏幕（手机）。",
     "a map = (Wahl)karte · too close to call = zu knapp, um es zu entscheiden · a second screen = zweiter Bildschirm (Handy)."),
    ("读第 5 版文章，选出正确答案。", "Lies Seite 5, wähle die richtige Antwort."),
    ("地图随结果逐州变色", "Die Karte färbt sich mit den Ergebnissen Bundesstaat für Bundesstaat"),
    ("too close to call = 尚不知晓", "too close to call = man weiß es noch nicht"),
    ("选举夜常吃披萨", "Am Wahlabend gibt es oft Pizza"),
    ("第二屏是手机", "Der zweite Bildschirm ist das Handy"),
    ("孩子问为什么这么久", "Kinder fragen, warum es so lange dauert"),
    ("结果早上还在", "Die Ergebnisse sind am Morgen noch da"),
    ("用所给词补全句子。", "Ergänze die Sätze mit den Wörtern."),
    ("close = 接近的", "close = knapp"),
    ("still = 仍然", "still = weiterhin"),
    ("与第 5 版原文一致，单数", "Wie im Text auf Seite 5, Singular"),
    ("map=选举地图 c", "map = Wahlkarte c"),
    ("race=一场竞选 d", "race = Wahlkampf d"),
    ("result=结果 b", "result = Ergebnis b"),
    ("call=宣布胜者 a", "call = Sieger verkünden a"),
    ("用现在进行时改写（正在发生的事）。", "Schreibe im Present Continuous um (was gerade geschieht)."),
    ("FIVE SENTENCES · 五句话作业", "FIVE SENTENCES · Fünf Sätze als Aufgabe"),
    ("投票结束｜The polls have closed = 该州投票已结束，计票开始。",
     "Wahlschluss | The polls have closed = In diesem Bundesstaat ist die Wahl beendet, das Zählen beginnt."),
    # P6
    ("DEEP READ · 时事深读", "DEEP READ · Vertiefung"),
    ("LEVEL B2 · How America votes · 美国怎么投票", "LEVEL B2 · How America votes · Wie Amerika wählt"),
    ("A PRACTICE BALLOT · 模拟选票", "A PRACTICE BALLOT · Musterstimmzettel"),
    ("讲解｜to register 登记（选民登记） · a governor 州长 · to shape laws 影响立法 · patience 耐心。",
     "to register = sich (als Wähler) registrieren · a governor = Gouverneur · to shape laws = Gesetze prägen · patience = Geduld."),
    ("READ THE CHART · 读图表", "READ THE CHART · Diagramm lesen"),
    ("读上面的教学图表，选出正确答案。", "Lies das Übungsdiagramm oben, wähle die richtige Antwort."),
    ("38% 选“不用排队”", "38 % wählten «keine Schlangen»"),
    ("工作原因 29%", "Grund «Arbeit am Dienstag»: 29 %"),
    ("四项合计 100%", "Alle vier zusammen: 100 %"),
    ("习惯最少 12%", "Am wenigsten: Gewohnheit mit 12 %"),
    ("不用排队比旅行多 17 个百分点", "«Keine Schlangen» liegt 17 Punkte vor «Reisepläne»"),
    ("图表是教学数据非真实民调", "Das Diagramm sind Übungsdaten, keine echte Umfrage"),
    ("读第 6 版文章，选出正确答案。", "Lies Seite 6, wähle die richtige Antwort."),
    ("各州自行组织选举", "Die Bundesstaaten organisieren die Wahlen selbst"),
    ("众议员任期两年", "Abgeordnete dienen zwei Jahre"),
    ("参议员任期六年、每次约三分之一改选", "Senatoren dienen sechs Jahre, etwa ein Drittel wird jeweils neu gewählt"),
    ("邮寄选票计票需时间", "Briefwahlstimmen brauchen Zeit zum Öffnen und Prüfen"),
    ("本期不印民调与预测", "Diese Ausgabe druckt keine Umfragen und Prognosen"),
    ("耐心是制度的一部分", "Geduld ist Teil des Systems"),
    ("shape = 影响、塑造", "shape = prägen, formen"),
    ("register = 登记", "register = sich registrieren"),
    ("patience = 耐心", "patience = Geduld"),
    ("optional = 可选的", "optional = freiwillig"),
    ("differ 三单 differs", "differ, 3. Person Singular: differs"),
    ("private = 私密的", "private = privat"),
    ("HOW LONG ? · 任期多长？", "HOW LONG ? · Wie lange im Amt?"),
    ("一张地图｜五十个州、五十套规则——所以选举夜看的是地图，不是一个数字。",
     "Eine Karte | Fünfzig Bundesstaaten, fünfzig Regeln — deshalb schaut man am Wahlabend auf eine Karte, nicht auf eine Zahl."),
]
rep_all("content56.py", C56)

# ================= content7 (P7) =================
# P7 structure (measured from the core, not copied from any other family):
# top: 4 columns A2 (FALLING BACK + GOING TO + EXAMPLE) / B1 (COMPARATIVES
# + PAST SIMPLE + EXAMPLE) / B2 (HEADLINE PRESENT + WHETHER + EXAMPLE) /
# TOOLBOX (3 pocket sentences + bridge); middle: PHRASES OF THE WEEK, 8
# sentences verbatim + grammar point + follow-up exercise each; bottom:
# ERROR CLINIC (2 cols, 4 items) + READERS' CORNER box + NEXT WEEK teaser.
# Golden sentences and column English teaching paragraphs stay verbatim;
# only grammar points, notes, heads, bridges and the disclosure are German.
C7 = [
    ("LANGUAGE IN HAND · 精讲", "LANGUAGE IN HAND · Sprachwerkstatt"),
    ("A2 → B2 · Phrases of the week · 本周金句", "A2 → B2 · Phrases of the week · Sätze der Woche"),
    ("LEVEL A2 · 基础", "LEVEL A2 · Grundlagen"),
    ("LEVEL B1 · 进阶", "LEVEL B1 · Aufbau"),
    ("LEVEL B2 · 挑战", "LEVEL B2 · Herausforderung"),
    ("THE EXAMPLE · 例句", "THE EXAMPLE · Beispiel"),
    ("« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6).",
     "« Patience is part of the system, not a failure of it. » — part of = ein Teil von (page 6)."),
    ("THE TOOLBOX · 工具箱", "THE TOOLBOX · Werkzeugkiste"),
    ("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。",
     "Werkzeugkiste | Drei Sätze zum Mitnehmen, einer pro Niveau; alle Sätze der Woche stammen aus dieser Ausgabe — lies den Artikel dazu, dann sitzen sie."),
    ("PHRASES OF THE WEEK · 本周金句（全部出自本期文章）",
     "PHRASES OF THE WEEK · Sätze der Woche (alle aus dieser Ausgabe)"),
    ("每句一个语法点 + 一道小题 · 答案见第 8 版",
     "Jeder Satz: ein Grammatikpunkt + eine Übung · Antworten auf Seite 8"),
    # phrase grammar points + notes (sentences themselves untouched)
    ("语法点｜is = 是；日期作主语补足语。", "Grammatik | is = ist; das Datum als Subjekt."),
    ("is 是", "is = ist"),
    ("语法点｜happen 的过去式是 happened，规则变化。",
     "Grammatik | Vergangenheit von happen ist happened, regelmäßig."),
    ("语法点｜would + 动词原形，表选择意愿。",
     "Grammatik | would + Grundform, für einen Wunsch bei der Wahl."),
    ("would + 原形", "would + Grundform"),
    ("语法点｜that is = 那就是；破折号后总结。",
     "Grammatik | that is = das ist; nach dem Gedankenstrich die Zusammenfassung."),
    ("that is 那就是", "that is = das ist"),
    ("语法点｜will still = 仍然会；still 放在 will 之后。",
     "Grammatik | will still = wird weiterhin; still steht nach will."),
    ("will still 仍然会", "will still = wird weiterhin"),
    ("语法点｜part of = ……的一部分；not 表否定对照。",
     "Grammatik | part of = ein Teil von; not als Gegensatz."),
    ("is part of 一部分", "is part of = ein Teil von"),
    ("语法点｜not every + 单数动词：并非每处都变。",
     "Grammatik | not every + Verb im Singular: nicht jeder Ort ändert sich."),
    ("语法点｜has = 有；the week 单数用 has。",
     "Grammatik | has = hat; the week im Singular braucht has."),
    # clinic
    ("THE ERROR CLINIC · 易错诊所", "THE ERROR CLINIC · Fehlerklinik"),
    ("每句有一处错误：找出来并改正。", "Jeder Satz enthält einen Fehler: Finde ihn und korrigiere den Satz."),
    ("三单否定用 doesn't + 原形", "3. Person: doesn't + Grundform"),
    ("fall 的过去式是 fell", "Vergangenheit von fall: fell"),
    ("bigger 已含比较级，不要再加 more", "bigger ist schon der Komparativ — kein more davor"),
    ("going to 后用动词原形", "Nach going to steht die Grundform"),
    # readers' corner: box head German; the English example letter paragraph
    # stays VERBATIM (core English element); only the disclosure below is
    # rewritten in German. No new English disclosure sentence is invented.
    ("READERS' CORNER · 读者园地", "READERS' CORNER · Leserecke"),
    ("编辑说明｜VOL.1 曾承诺 VOL.2 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.1 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.3 起刊登收到的真实来信。",
     "Anmerkung der Redaktion | Bis Redaktionsschluss sind keine echten Leserbriefe eingetroffen, und es gibt keinen besten VOL.1-Schreibtext zu besprechen. Das Beispiel oben bleibt daher ehrlich gekennzeichnet stehen; echte Briefe erscheinen ab VOL.3. Schicke uns deinen Brief und deinen Text — wir drucken sie in VOL.3!"),
    # teaser: English paragraph stays verbatim; German line localised
    ("NEXT WEEK · VOL.3 下周预告", "NEXT WEEK · VOL.3 · Vorschau"),
    ("下周三退伍军人节，周日 NFL 慕尼黑赛；还有中期选举结果报道。",
     "Mittwoch: Veterans Day. Sonntag: die NFL in München. Dazu die Ergebnisse der Zwischenwahlen."),
]
rep_all("content7.py", C7)

# ================= content8 (P8) =================
# E-item redirection (core keys 137-140 all Chinese; edition is EN<->DE):
# 137 EN->DE (key German), 138 DE->EN (key English = core body sentence),
# 139 DE->EN (key English = core body sentence), 140 EN->DE (key German).
# 150 writing registry key -> German (W43 form). All other keys byte-equal.
C8 = [
    ("EXERCISES & ANSWERS · 练习与答案", "EXERCISES & ANSWERS · Übungen & Antworten"),
    ("FINAL TEST · 综合评估 · Answers at the bottom of this page 答案在本版下方",
     "FINAL TEST · Abschlusstest · Answers at the bottom of this page"),
    ("A · CLOZE · 完形填空", "A · CLOZE · Lückentext"),
    ("选项：", "Optionen:"),
    ("11 月 3 日是周二", "Der 3. November ist ein Dienstag"),
    ("pizza 披萨", "pizza = Pizza"),
    ("map 地图逐州变色", "map = Karte, die sich Bundesstaat für Bundesstaat färbt"),
    ("close 接近的", "close = knapp"),
    ("sticker 贴纸", "sticker = Aufkleber"),
    ("will + 动词原形 know", "will + Grundform know"),
    ("still 仍然", "still = weiterhin"),
    ("B · MULTIPLE CHOICE · 单选", "B · MULTIPLE CHOICE · Auswahl"),
    ("we → get 原形", "we → get (Grundform)"),
    ("已发生的事用 fell", "Vergangenes: fell"),
    ("than → 比较级 bigger", "than → Komparativ bigger"),
    ("despite + 名词：尽管下雨", "despite + Substantiv: trotz Regen"),
    ("whether = 是否", "whether = ob"),
    ("将来时 will + 动词原形", "Futur: will + Grundform"),
    ("be going to + 原形 vote", "be going to + Grundform vote"),
    ("too close to call = 难分胜负", "too close to call = zu knapp, um es zu entscheiden"),
    ("C · READING · 阅读理解", "C · READING · Leseverstehen"),
    ("原文：a teacher from Ohio", "Im Text: a teacher from Ohio"),
    ("周二他全天教书", "Am Dienstag unterrichtet er den ganzen Tag"),
    ("贴纸上写着 I VOTED", "Auf dem Aufkleber steht I VOTED"),
    ("俄亥俄一如既往难分胜负", "Ohio ist wie immer zu knapp, um es zu entscheiden"),
    ("D · SENTENCES · 完成句子与转换", "D · SENTENCES · Sätze bilden und umformen"),
    ("are going to + 原形", "are going to + Grundform"),
    ("fall → fell（不规则变化）", "fall → fell (unregelmäßig)"),
    ("tall → taller（比较级）", "tall → taller (Komparativ)"),
    ("whether 引导“是否”从句", "whether leitet einen Ob-Satz ein"),
    ("E · TRANSLATION · 翻译", "E · TRANSLATION · Übersetzung"),
    # 137 EN->DE
    ('("B2", "耐心是制度的一部分，而不是制度的失败。", "part of 一部分；not a failure 不是失败",',
     '("B2", "Geduld ist Teil des Systems, nicht ein Versagen des Systems.", "part of = ein Teil von; not a failure = kein Versagen",'),
    # 138 DE->EN (body German, key = core body English sentence)
    ('("A2", "11 月 3 日周二是美国的选举日。", "Election Day 选举日；on Tuesday",\n     "翻译：Tuesday, November 3, is Election Day in the United States."),',
     '("A2", "Tuesday, November 3, is Election Day in the United States.", "Wahltag = Election Day; am Dienstag = on Tuesday",\n     "Übersetze: Dienstag, der 3. November, ist Wahltag in den Vereinigten Staaten."),'),
    # 139 DE->EN
    ('("B1", "这周日，NFL 在马德里比赛。", "on Sunday；in Madrid",\n     "翻译：On Sunday, the NFL plays in Madrid."),',
     '("B1", "On Sunday, the NFL plays in Madrid.", "an diesem Sonntag = on Sunday; in Madrid = in Madrid",\n     "Übersetze: An diesem Sonntag spielt die NFL in Madrid."),'),
    # 140 EN->DE
    ('("B1", "并非每处都拨回时钟。", "not every 并非每处；change 变化",',
     '("B1", "Nicht jeder Ort stellt die Uhren zurück.", "not every = nicht jeder; changes = stellt zurück",'),
    ("F · WORDS · 词汇配对", "F · WORDS · Zuordnung"),
    ("midterm = 中期选举 b", "midterm = Zwischenwahl b"),
    ("governor = 州长 c", "governor = Gouverneur c"),
    ("ballot = 选票 d", "ballot = Stimmzettel d"),
    ("turnout = 投票率 a", "turnout = Wahlbeteiligung a"),
    ("G · DIALOGUE · 对话补全", "G · DIALOGUE · Dialog"),
    ("投票时出示证件 ID", "Beim Wählen den Ausweis (ID) zeigen"),
    ("line = 排队（美式英语）", "line = Schlange (amerikanisches Englisch)"),
    ("ballot = 选票", "ballot = Stimmzettel"),
    ("sticker = 贴纸", "sticker = Aufkleber"),
    ("选举日是 11 月 3 日周二", "Wahltag ist Dienstag, der 3. November"),
    ('reg_ex("B1", "写作", "开放题 — 要点见写作框，范文在第 8 版写作框内", "按要点给分")',
     'reg_ex("B1", "Schreiben", "Offene Aufgabe — Stichpunkte im Schreibkasten; Mustertext im Kasten auf Seite 8", "Bewertung nach Stichpunkten")'),
    ("H · WRITING · 写作 [B1]", "H · WRITING · Schreiben [B1]"),
    ("用英语写 80–100 词：我的 11 月 3 日周二。写清你是否看了结果、吃了什么、地图显示了什么，再写一句周日夜里拨回的时钟。",
     "Schreibe auf Englisch (80–100 Wörter): « Mein Dienstag, der 3. November ». Beschreibe, ob du die Ergebnisse verfolgt hast, was du gegessen hast, was die Karte gezeigt hat — und einen Satz über die Uhren, die in der Sonntagnacht zurückgestellt wurden."),
    ("MODEL · 范文", "MODEL · Mustertext"),
    ("ANSWERS · 全部答案与简析（第 1–8 版）", "ANSWERS · Alle Antworten mit Anmerkungen (Seiten 1–8)"),
    # P8 key rendering: W43 EN x DE form — print ALL notes, 13.5pt,
    # half-width parens, "--- Seite N ---" separators, bottom 2530.
    ('kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2545, tag="P8-keys")',
     'kf = Flow(p, [(COLX[i], CW) for i in range(4)], ky + 48, 2530, tag="P8-keys")'),
    ('    kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
     '    kf.para(f"— Seite {pg} —", 16, "sans", True, OLIVE, 1.26, 3)'),
    ('        if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):\n            s += f"（{e[\'note\']}）"',
     '        if e["note"]:\n            s += f" ({e[\'note\']})"'),
    ('    kf.para(" · ".join(parts), 15.5, "sans", False, INK, 1.3, 9)',
     '    kf.para(" · ".join(parts), 13.5, "sans", False, INK, 1.26, 9)'),
]
rep_all("content8.py", C8)
# shared maps LAST (see note at top): remaining type/instr tokens only
apply_shared()
# now the type token "翻译" remains only as the E-section type (bodies done)
rep("content8.py", '"翻译"', '"Übersetzung"', 1)

# ================= ROUND 2 (layout fixes from build round 1) =================
# All `old` strings below are the ROUND-1 German outputs (transform.py is
# re-run from a fresh core copy each round, so round 2 edits apply on top).
# R2-1 P1: box line 1 wrapped to 4 lines (core: 3) and pushed the last
#   TRY IT NOW exercise past the headline flow bottom (1828). Shorten the
#   parenthetical so it wraps to 3 lines again (-1 line, -27.7px).
rep("content12.py",
    "Nov 3 — Election Day (Wahltag) · 435 — seats in the House, all on the ballot (alle Sitze im Repräsentantenhaus neu zu wählen)",
    "Nov 3 — Election Day (Wahltag) · 435 — seats in the House, all on the ballot (alle 435 Sitze neu zu wählen)", 1)
# R2-2 P2 exercises: German bridges wrapped to 2 lines (core: 1) and the
#   D match_set (362px) started at y=2307, 107px past its fit. Save lines
#   plus spacing (precedent: W43 EN x DE P2 tightening):
#   bridges to 1 line (-59.4), 4 section-head gaps 13->8 (-20),
#   3 bridge gaps 9->5 (-12), 13 exercise gaps 11->9 (-26),
#   match_set gap 14->6 (-8 inside D).
rep("content12.py", "Ergänze die Sätze auf Englisch nach der Uhrzeit.",
    "Ergänze die Sätze nach der Uhrzeit.", 1)
rep("content12.py", "Schreibe mit be going to um (Pläne und was geschehen wird).",
    "Schreibe mit be going to um.", 1)
rep("content12.py", 'e.head("A · WHAT TIME IS IT ?", 25)',
    'e.head("A · WHAT TIME IS IT ?", 25, gap=8)', 1)
rep("content12.py", 'e.head("B · GOING TO", 25)',
    'e.head("B · GOING TO", 25, gap=8)', 1)
rep("content12.py", 'e.head("C · COMPREHENSION", 25)',
    'e.head("C · COMPREHENSION", 25, gap=8)', 1)
rep("content12.py", 'e.head("D · THE WORDS", 25)',
    'e.head("D · THE WORDS", 25, gap=8)', 1)
rep("content12.py", 'e.bridge("Ergänze die Sätze nach der Uhrzeit.")',
    'e.bridge("Ergänze die Sätze nach der Uhrzeit.", gap=5)', 1)
rep("content12.py", 'e.bridge("Schreibe mit be going to um.")',
    'e.bridge("Schreibe mit be going to um.", gap=5)', 1)
rep("content12.py", 'e.bridge("Lies Seite 2, wähle die richtige Antwort.")',
    'e.bridge("Lies Seite 2, wähle die richtige Antwort.", gap=5)', 1)
rep("content12.py", 'instr="Ergänze", size=22)',
    'instr="Ergänze", size=22, gap=9)', 5)
rep("content12.py", ', size=22)',
    ', size=22, gap=9)', 4)
rep("content12.py", 'instr="Schreibe um")',
    'instr="Schreibe um", gap=9)', 4)
# match_set D call in content12: add gap=6 (call ends with instr="Ordne zu")
rep("content12.py", 'instr="Ordne zu")',
    'instr="Ordne zu", gap=6)', 1)
# R2-3 P6 chart head too wide (446.7 > 434): shorten German second part.
rep("content56.py", "READ THE CHART · Diagramm lesen",
    "READ THE CHART · Diagramm", 1)
# R2-4 P8 battery ended 1513 vs bottom 1485 (+28): the DE->EN body of item
#   139 wraps to 2 lines (core: 1) and cannot shrink to 1 line without
#   dropping the date, so save spacing instead: B/C/D loop gaps 11->8
#   (-27/-12/-12 = -51). E items already pass gap=8.
rep("content8.py", 'bf.ex(lv, "Multiple Choice", k, nt, body, size=20.5)',
    'bf.ex(lv, "Multiple Choice", k, nt, body, size=20.5, gap=8)', 1)
rep("content8.py", 'bf.ex(lv, "Leseverstehen", k, nt, body, size=20.5)',
    'bf.ex(lv, "Leseverstehen", k, nt, body, size=20.5, gap=8)', 1)
rep("content8.py", 'bf.ex(lv, "Satzergänzung", k, nt, body, size=20.5)',
    'bf.ex(lv, "Satzergänzung", k, nt, body, size=20.5, gap=8)', 1)
# R2-5 P8 D head too wide (555.2 > 434): W43 form "Sätze formen".
rep("content8.py", "D · SENTENCES · Sätze bilden und umformen",
    "D · SENTENCES · Sätze formen", 1)

print("transform done, replacements:", len(LOG))
for line in LOG:
    print(" ", line)

# ================= ROUND 3 (occlusion-audit flags from build round 2) =================
# Root cause in every case: a German furniture/box title drawn unwrapped
# (p.text / Flow.box title) that outgrew its box or the page. All fixes
# shorten the title only; box heights are measured from body paras, so no
# flow shifts. Pre-fix baseline: run2-baseline.sha256.
# R3-1 P1 searches subtitle ran off the page (ink to 2100.8).
rep("content12.py", "Diese Woche in den USA gesucht · Google-Trends-Schnappschuss USA",
    "Diese Woche gesucht · Google Trends USA", 1)
# R3-2 P1 word-of-week German line wrapped to 2 lines and the 2nd line was
#   struck by the row-B rule at y=1844. One-line form (wrap-verified).
rep("content12.py", "Mitte (einer Amtszeit). midterm election = Zwischenwahl.",
    "Mitte der Amtszeit: midterm = Zwischenwahl.", 1)
# R3-3 P1 numbers box title past its column box (ink 1507.2 > border 1423).
rep("content12.py", "THE WEEK IN NUMBERS · Zahlen der Woche",
    "THE WEEK IN NUMBERS · Zahlen", 1)
# R3-4 P3 home box title past its column box (ink 596.5 > border 499).
rep("content34.py", "AT HOME THIS WEEK · Diese Woche zu Hause",
    "AT HOME THIS WEEK · Zu Hause", 1)
# R3-5 P4 Sunday box title off the page (ink 1963 > 1922) and past its box.
rep("content34.py", "SUNDAY, NOVEMBER 8 · Spiele am Sonntag",
    "SUNDAY, NOVEMBER 8 · Spiele", 1)
# R3-6 P5 TOO CLOSE box title past its box (ink 703 > border 499) and into
#   the next column, where it collided with the C head (TEXTX).
rep("content56.py", "TOO CLOSE TO CALL · Zu knapp, um es zu entscheiden",
    "TOO CLOSE TO CALL · Zu knapp", 1)
# R3-7 P5 col3 box title past its box (ink 1945.5 > border 1885).
rep("content56.py", "FIVE SENTENCES · Fünf Sätze als Aufgabe",
    "FIVE SENTENCES · Fünf Sätze", 1)
# R3-8 P6 ballot box title past its box (ink 1015.5 > border 961) and into
#   the next column, where it grazed a B2 chip (TEXTX 8.6x3.8).
rep("content56.py", "A PRACTICE BALLOT · Musterstimmzettel",
    "A PRACTICE BALLOT · Stimmzettel", 1)

print("transform done, replacements:", len(LOG))
for line in LOG:
    print(" ", line)

# ================= ROUND 4 (visual QA: P1 dark-band collision) =================
# Card review found the dark-band line 1 left English line and the German
# right line touching ("BACK !DIENSTAG"): PIL advance gap is only 4.9px
# and CairoSVG's bold metrics run slightly wider, so the eye sees a join
# that ink-box measurement calls clean. Shorten the right line to a
# grammatical, banner-style form (gap becomes 64.8px by advance measure).
# Pre-fix baseline: run3-baseline.sha256.
rep("content12.py", "DIENSTAG WAHLTAG · SONNTAG ZURÜCKGESTELLT",
    "DIENSTAG WAHLTAG · SONNTAG UMGESTELLT", 1)

print("transform done, replacements:", len(LOG))
for line in LOG:
    print(" ", line)
