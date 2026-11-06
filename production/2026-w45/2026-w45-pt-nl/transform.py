# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x NL fan-out transform for W45 VOL.2.

Copies nothing: run this inside the already-copied build dir. Every
replacement is an exact literal match (longest strings first where one
contains another), except three line-anchored replacements (P1 subtitle
line, P1 badge line, P2 time-box tuple). After the pass, bslib4.py +
content*.py must contain ZERO CJK chars.
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + 'Página' tags are never touched.
Furniture follows the shipped W43 PT x NL edition (files/weekly-report-
pt-nl), NOT the tools README generics and NOT the W45 PT x EN sibling:
badge y=372 19pt bold BRICK, subtitle 34pt, gloss prefix 'Uitleg — ',
P8 separator '— Pagina N —', footer 'PORTUGEES WEEKBLAD VOL.2',
top strip 'ELKE WEEK · HET PORTUGEES DAT BRAZILIË LEEST', bridges via
the W43 expl() rename carrying the 'Uitleg — ' prefix.
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
CJK = re.compile(r'[\u4e00-\u9fff]')

def load(fn):
    with open(os.path.join(HERE, fn), encoding='utf-8') as f:
        return f.read()

def save(fn, txt):
    with open(os.path.join(HERE, fn), 'w', encoding='utf-8') as f:
        f.write(txt)

def sub(txt, old, new, expect=None, fn=''):
    n = txt.count(old)
    if expect is not None:
        assert n == expect, f'{fn}: {old!r} found {n}x, expected {expect}x'
    else:
        assert n >= 1, f'{fn}: {old!r} not found'
    return txt.replace(old, new)

def line_replace(txt, anchor, newline, fn=''):
    lines = txt.split('\n')
    hits = [i for i, ln in enumerate(lines) if anchor in ln]
    assert len(hits) == 1, f'{fn}: anchor {anchor!r} hits {hits}'
    lines[hits[0]] = newline
    return '\n'.join(lines)

FILES = ['bslib4.py', 'content12.py', 'content34.py', 'content56.py',
         'content7.py', 'content8.py', 'render.py']

# ---------- 0. OUT / BASE repoint (all files) ----------
for fn in FILES:
    t = load(fn)
    if 'weekly-report-w45-pt-core' in t:
        t = sub(t, 'weekly-report-w45-pt-core', 'weekly-report-w45-pt-nl', fn=fn)
        save(fn, t)

# ---------- 1. bslib4 furniture (W43 PT x NL verbatim, VOL.2) ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.2 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · PORTUGEES WEEKBLAD VOL.2 · TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS', 1, 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} van {total}"', 1, 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Uitleg — " + s', 1, 'bslib4.py')
# W43 rename: bridge -> expl (same rendering; call strings carry 'Uitleg — ')
t = sub(t, 'def bridge(self, s', 'def expl(self, s', 1, 'bslib4.py')
save('bslib4.py', t)

# ---------- 1b. bridge -> expl call sites ----------
EXPECT_BRIDGE = {'content12.py': 4, 'content34.py': 7, 'content56.py': 6,
                 'content7.py': 3, 'content8.py': 1}
for fn, expect in EXPECT_BRIDGE.items():
    t = load(fn)
    t = sub(t, '.bridge(', '.expl(', expect, fn)
    save(fn, t)

# ---------- 2. type / instr labels (instr first, then bare typ) ----------
INSTR = [
    ('instr="造句"', 'instr="Bouw de zin"'),
    ('instr="翻译"', 'instr="Vertaal"'),
    ('instr="判断"', 'instr="Waar of onwaar?"'),
    ('instr="写作"', 'instr="Schrijven"'),
    ('instr="填空"', 'instr="Vul in"'),
    ('instr="把词和释义配对"', 'instr="Combineer"'),
]
TYP = [
    ('"完成句子"', '"Voltooi de zin"'),
    ('"词汇配对"', '"Woorden koppelen"'),
    ('"判断对错"', '"Waar of onwaar"'),
    ('"完形单选"', '"Gatentekst"'),
    ('"单选"', '"Meerkeuze"'),
    ('"造句"', '"Bouw de zin"'),
    ('"翻译"', '"Vertaal"'),
    ('"写作"', '"Schrijven"'),
]
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    for old, new in INSTR:
        if old in t:
            t = sub(t, old, new, fn=fn)
    for old, new in TYP:
        if old in t:
            t = sub(t, old, new, fn=fn)
    save(fn, t)

# ---------- 3. content replacements (longest-first within each file) ----------
R12 = [
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语',
     'TODA SEMANA EM PORTUGUÊS · ELKE WEEK · HET PORTUGEES DAT BRAZILIË LEEST'),
    ('11 月 2 日亡灵节连休 · 11 月 8 日高考第一天', '2 nov Finados-weekend · 8 nov dag 1 van het Enem'),
    ('全国高考周', 'DE WEEK VAN HET ENEM'),
    ('讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。',
     'Uitleg — feriadão = het lange feestweekend · o portão = de poort · a redação = het opstel · revisar = herhalen.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · CIJFERS'),
    ('12h — os portões abrem no domingo 8（周日 12 点开门）',
     '12h — os portões abrem no domingo 8 (zondag: de poorten openen om 12h)'),
    ('13h — os portões fecham（13 点关门，过时不入）',
     '13h — os portões fecham (13h: de poorten sluiten, wie te laat is komt er niet in)'),
    ('13h30–19h — a prova do dia 8（考试 13:30 至 19:00）',
     '13h30–19h — a prova do dia 8 (het examen van dag 8, 13:30 tot 19:00)'),
    ('5h30 — a duração da prova do dia 8（考试时长 5 小时半）',
     '5h30 — a duração da prova do dia 8 (het examen van dag 8 duurt vijf en een half uur)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · AAN DE SLAG'),
    ('feriadão = 连休长周末', 'feriadão = het lange feestweekend'),
    ('portões = 大门（考场大门）', 'portões = de poorten (van de examenlocatie)'),
    ('redação = 作文', 'redação = het opstel'),
    ('13h30 开考（巴西利亚时间）', '13h30: het examen begint (tijd van Brasília)'),
    ('19h 结束', '19h: het examen eindigt'),
    ('revisar 现在时 eles 形式：revisam', 'revisar, tegenwoordige tijd (eles): revisam'),
    ('迟到不得入内：13 点后关门', 'Wie te laat komt, komt er na 13h niet meer in.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · IN DEZE EDITIE'),
    ('“连休”：假期连着周末，一共三天。',
     '«Feriadão»: feestdag plus weekend, drie dagen.'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · KORTOM'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · BLITSQUIZ'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lees de voorpagina en kies het juiste antwoord · antwoorden op pagina 8'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · HOOFDNIEUWS'),
    ('连休从 10 月 31 日到 11 月 2 日', 'Het lange weekend loopt van 31 oktober tot 2 november'),
    ('13 点关门', 'De poorten sluiten om 13h'),
    ('第 1 天考作文、语言与人文', 'Dag 1: opstel, talen en menswetenschappen'),
    ('次回合在 7 日和 8 日', 'De returns zijn op 7 en 8 november'),
    ('VIDA · 生活', 'VIDA · LEVEN'),
    ('NÍVEL A2 · Finados e revisão: o feriadão do Brasil',
     'NÍVEL A2 · Finados e revisão: o feriadão do Brasil · Finados en revisie: het lange weekend in Brazilië'),
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · EZELSBRUG'),
    ('o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。',
     'o feriadão = het lange feestweekend · o cemitério = de begraafplaats · a vela = de kaars · o crisântemo = de chrysant · a missa = de mis · conferir = nakijken.'),
    ('在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。',
     'Is er in jouw land een dag om de doden te herdenken? Wat doen families op die dag? Schrijf twee zinnen in het Portugees en stuur ze naar de redactie: de beste verschijnen op pagina 7, «Cartas dos leitores».'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · EN JIJ?'),
    ('OS HORÁRIOS DO DOMINGO 8 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 8 · DE TIJDEN VAN ZONDAG 8'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · één land, meer klokken'),
    ('周日 12 点开门', 'Zondag open om 12h'),
    ('13:30 开考', 'Examen start 13:30'),
    ('19:00 结束', 'Examen eindigt 19h'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · OEFENINGEN'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Antwoorden op pagina 8 · niveaus gemengd: zoek op nummer'),
    ('读第 2 版文章，选出正确答案。', 'Uitleg — Lees het artikel op pagina 2 en kies het juiste antwoord.'),
    ('亡灵节家人们去墓园献花', 'Op Finados bezoeken families begraafplaatsen en brengen ze bloemen'),
    ('确认卡显示考试地点', 'De bevestigingskaart toont de examenlocatie'),
    ('巴西没有夏令时，钟表不动', 'Brazilië heeft geen zomertijd: de klokken verzetten niet'),
    ('补全动词的现在时形式。', 'Uitleg — Vul de tegenwoordige tijd van het werkwoord in.'),
    ('conferir：ele → confere', 'conferir: ele → confere'),
    ('abrir：ele → abre', 'abrir: ele → abre'),
    ('levar：nós → levamos', 'levar: nós → levamos'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('ser 现在时 ela 形式：é', 'ser, tegenwoordige tijd (ela): é'),
    ('用第 1、2 版的数字填空。', 'Uitleg — Vul de getallen van pagina 1 en 2 in.'),
    ('12 点到 13 点 = 1 小时', '12h tot 13h = 1 uur'),
    ('13:30 至 19:00 = 5 个半小时', '13:30 tot 19:00 = vijf en een half uur'),
    ('5×60 + 30 = 330 分钟', '5×60 + 30 = 330 minuten'),
    ('31 日、1 日、2 日 = 3 天', '31e, 1e, 2e = 3 dagen'),
    ('feriadão=连着周末的假期 c', 'feriadão = een feestdag vast aan het weekend (c)'),
    ('cemitério=墓碑所在的地方 b', 'cemitério = waar de graven zijn (b)'),
    ('vela=点亮纪念的物品 d', 'vela = wat je aansteekt ter nagedachtenis (d)'),
    ('crisântemo=亡灵节带去的花 a', 'crisântemo = de bloem die je op Finados meeneemt (a)'),
]
R34 = [
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · EN JIJ?'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Antwoorden op pagina 8 · niveaus gemengd: zoek op nummer'),
    ('CULTURA · 文化', 'CULTURA · CULTUUR'),
    ('A2 → B1 · Finados: o dia da memória · 亡灵节：怀念的日子',
     'A2 → B1 · Finados: o dia da memória · Finados: de dag van de herinnering'),
    ('o túmulo 墓碑 · a flor 花 · acender 点燃 · rezar 祈祷 · o silêncio 寂静 · a lembrança 怀念。',
     'o túmulo = het graf · a flor = de bloem · acender = aansteken · rezar = bidden · o silêncio = de stilte · a lembrança = de herinnering.'),
    ('在你的文化里，人们怎样怀念逝者？写两句寄来。',
     'Hoe herdenken mensen in jouw cultuur de doden? Schrijf twee zinnen en stuur ze op.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · OEFENINGEN'),
    ('读第 3 版文章，选出正确答案。', 'Uitleg — Lees het artikel op pagina 3 en kies het juiste antwoord.'),
    ('亡灵节是怀念与安静的日子', 'Finados is een dag van herinnering en stilte'),
    ('家人们带花去墓园，主要是菊花', 'Families nemen bloemen mee naar begraafplaatsen, vooral chrysanten'),
    ('教堂和墓园整天都有弥撒', 'In kerken en op begraafplaatsen zijn er de hele dag missen'),
    ('万圣节在 10 月 31 日周六', 'Halloween was op zaterdag 31 oktober'),
    ('怀念是继续亲近的方式', 'Herinneren is een manier om dichtbij te blijven'),
    ('用方框里的词填空。', 'Uitleg — Vul de woorden uit het kader in.'),
    ('túmulo = 墓碑', 'túmulo = het graf'),
    ('vela = 蜡烛', 'vela = de kaars'),
    ('crisântemo = 菊花', 'crisântemo = de chrysant'),
    ('missa = 弥撒', 'missa = de mis'),
    ('silêncio = 寂静', 'silêncio = de stilte'),
    ('lembrança = 怀念', 'lembrança = de herinnering'),
    ('用过去时（pretérito perfeito）补全。', 'Uitleg — Vul de verleden tijd (pretérito perfeito) in.'),
    ('visitar 过去时 elas 形式：visitaram', 'visitar, verleden tijd (elas): visitaram'),
    ('levar 过去时 elas 形式：levaram', 'levar, verleden tijd (elas): levaram'),
    ('ser 过去时 ele 形式：foi', 'ser, verleden tijd (ele): foi'),
    ('viver 过去时 ele 形式：viveu', 'viver, verleden tijd (ele): viveu'),
    ('把词组成正确的句子。', 'Uitleg — Zet de woorden in de juiste volgorde.'),
    ('主语 + é + 表语', 'Onderwerp + é + gezegde'),
    ('主语 + 动词 + 宾语 + 地点', 'Onderwerp + werkwoord + voorwerp + plaats'),
    ('主语 + 动词 + 宾语', 'Onderwerp + werkwoord + voorwerp'),
    ('ESPORTE · 体育', 'ESPORTE · SPORT'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'NÍVEL B1 · O futebol da semana · de voetbalweek'),
    ('a ida 首回合 · a volta 次回合 · o finalista 决赛球队 · a decisão 决战 · a rodada 轮次。',
     'a ida = de heenwedstrijd · a volta = de return · o finalista = de finalist · a decisão = de beslissing · a rodada = de speelronde.'),
    ('你在巴西杯支持哪支球队？写两句寄来。',
     'Voor welk team ben jij in de Copa do Brasil? Schrijf twee zinnen en stuur ze op.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · DE VOETBALKALENDER'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · OEFENINGEN'),
    ('读第 4 版文章，选出正确答案。', 'Uitleg — Lees het artikel op pagina 4 en kies het juiste antwoord.'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点',
     'De return Atlético-MG × Grêmio is op zaterdag 7 november om 18h'),
    ('瓦斯科 × 帕尔梅拉斯次回合在周日 8 日 17 点，圣雅努阿里奥',
     'De return Vasco × Palmeiras is op zondag 8 november om 17h, in São Januário'),
    ('首回合在 11 月 1 日周日', 'De heenwedstrijden waren op zondag 1 november'),
    ('第 34 轮周一到周五每天都有比赛', 'Speelronde 34 heeft van maandag tot vrijdag wedstrijden'),
    ('两回合总比分胜者进决赛', 'Wie over twee wedstrijden wint, bereikt de finale'),
    ('finalista=进决赛的球队 b', 'finalista = het team dat de finale bereikt (b)'),
    ('ida=对决的第一场 c', 'ida = de eerste wedstrijd van een tweeluik (c)'),
    ('volta=对决的第二场 a', 'volta = de tweede wedstrijd van een tweeluik (a)'),
    ('rodada=一轮比赛 d', 'rodada = een speelronde (d)'),
    ('用括号里正确的比较形式填空。', 'Uitleg — Vul de juiste vergrotende trap tussen haakjes in.'),
    ('次回合决定决赛名额：mais', 'De return beslist wie de finale haalt: mais'),
    ('18 > 16：mais', '18 > 16: mais'),
    ('17 < 18：mais cedo', '17 < 18: mais cedo'),
    ('第 34 轮周一到周五都有比赛：mais', 'Speelronde 34 loopt van maandag tot vrijdag: mais'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Uitleg — Maak de zinnen af in de verleden tijd (pretérito perfeito).'),
    ('ser 过去时复数：foram', 'ser, verleden tijd (meervoud): foram'),
    ('receber 过去时 ele 形式：recebeu', 'receber, verleden tijd (ele): recebeu'),
    ('começar 过去时 ela 形式：começou', 'começar, verleden tijd (ela): começou'),
    ('chegar 过去时 eles 形式：chegaram', 'chegar, verleden tijd (eles): chegaram'),
]
R56 = [
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · EN JIJ?'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Antwoorden op pagina 8 · niveaus gemengd: zoek op nummer'),
    ('JOVENS · 青年', 'JOVENS · JONGEREN'),
    ('NÍVEL B1 · A reta final dos jovens · 冲刺周：年轻人的最后一周',
     'NÍVEL B1 · A reta final dos jovens · de eindsprint van de jongeren'),
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）',
     '1. Confira o Cartão de Confirmação do Enem (controleer je bevestigingskaart van het Enem)'),
    ('2. Revise um pouco por dia, sem maratona（每天复习一点，不搞突击）',
     '2. Revise um pouco por dia, sem maratona (herhaal elke dag een beetje, geen lastminutemarathon)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）',
     '3. Durma bem na véspera da prova (slaap goed in de nacht vóór het examen)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）',
     '4. Separe documento e caneta preta no dia anterior (leg document en zwarte pen een dag eerder klaar)'),
    ('5. Domingo 8: chegue antes das 12h（周日 8 日：12 点前到达）',
     '5. Domingo 8: chegue antes das 12h (zondag 8: kom vóór 12h aan)'),
    ('a reta final 最后冲刺 · a véspera 前夕 · a maratona 突击马拉松 · separar 准备好 · a cabeça 头脑、状态。',
     'a reta final = de eindsprint · a véspera = de vooravond · a maratona = de lastminutemarathon · separar = klaarmaken · a cabeça = je hoofd, je gemoedstoestand.'),
    ('重要考试前一晚，你的计划是复习还是休息？写两句寄来。',
     'Wat is jouw plan voor de avond vóór een belangrijk examen: herhalen of rusten? Schrijf twee zinnen en stuur ze op.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · OEFENINGEN'),
    ('读第 5 版文章，选出正确答案。', 'Uitleg — Lees het artikel op pagina 5 en kies het juiste antwoord.'),
    ('冲刺周在 11 月 8 日周日结束', 'De eindsprint eindigt op zondag 8 november'),
    ('每天复习一点', 'Herhaal elke dag een beetje'),
    ('提前一天备好证件和黑笔', 'Leg document en zwarte pen een dag eerder klaar'),
    ('第 2 天考自然科学与数学', 'Dag 2: natuurwetenschappen en wiskunde'),
    ('11 月 3 日周二各州议会结束休会', 'Op dinsdag 3 november keren de deelstaatparlementen terug van reces'),
    ('用方框里的词填空。注意：有的词要变成复数。',
     'Uitleg — Vul de woorden uit het kader in. Let op: één woord moet in het meervoud.'),
    ('reta final = 最后冲刺阶段', 'reta final = de eindsprint'),
    ('inscrito 配合复数：inscritos', 'inscrito in het meervoud: inscritos'),
    ('véspera = 前夕', 'véspera = de vooravond'),
    ('maratona = 突击马拉松', 'maratona = de lastminutemarathon'),
    ('local = 地点', 'local = de locatie'),
    ('separar 祈使式：separe', 'separar, gebiedende wijs: separe'),
    ('用将来时（futuro do presente）补全。', 'Uitleg — Vul de toekomende tijd (futuro do presente) in.'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, toekomende tijd (eles, onregelmatig): farão'),
    ('mostrar 将来时：mostrará', 'mostrar, toekomende tijd: mostrará'),
    ('sair 将来时复数：sairão', 'sair, toekomende tijd (meervoud): sairão'),
    ('chegar 将来时：chegará', 'chegar, toekomende tijd: chegará'),
    ('确认卡显示考试地点', 'De bevestigingskaart toont de examenlocatie'),
    ('错：考前突击不是好计划，每天复习一点才好',
     'Fout: lastminute stampen is geen goed plan — elke dag een beetje herhalen wel'),
    ('对：13:30 至 19:00', 'Juist: 13:30 tot 19:00'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · VERDIEPING'),
    ('NÍVEL B2 · O Enem explicado · 高考详解', 'NÍVEL B2 · O Enem explicado · het Enem uitgelegd'),
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。',
     'os portões = de poorten · a segunda chamada = een tweede kans, een tweede binnenkomst · conferir = nakijken · a correria = de haast.'),
    ('O DOMINGO 8 EM NÚMEROS · 11 月 8 日的数字 (horários oficiais do Inep)',
     'O DOMINGO 8 EM NÚMEROS · DE CIJFERS VAN ZONDAG 8 (officiële tijden van het Inep)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · OEFENINGEN'),
    ('看上面两张图，选出正确答案。', 'Uitleg — Kijk naar de twee grafieken hierboven en kies het juiste antwoord.'),
    ('大门开放 60 分钟', 'De poorten blijven 60 minuten open'),
    ('关门到开考之间等 30 分钟', 'Het wachten tussen sluiten en examen is 30 minuten'),
    ('考试 330 分钟', 'Het examen duurt 330 minuten'),
    ('中午到 19 点 = 7 小时', 'Van de middag tot 19h = 7 uur'),
    ('图表数字是 Inep 官方时间', 'De cijfers in de grafiek zijn officiële tijden van het Inep'),
    ('高考分 8 日和 15 日两个周日', 'Het Enem valt op twee zondagen: 8 en 15 november'),
    ('第 1 天考作文、语言与人文', 'Dag 1: opstel, talen en menswetenschappen'),
    ('13 点后到场不得入内', 'Wie na 13h aankomt, komt er niet in'),
    ('根据句子意思，补全正确的动词形式。', 'Uitleg — Vul de juiste werkwoordsvorm bij elke zin in.'),
    ('将来时：começará', 'toekomende tijd: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + aanvoegende wijs toekomst: chegar'),
    ('现在时：fecham', 'tegenwoordige tijd: fecham'),
    ('现在时：pede', 'tegenwoordige tijd: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir',
     'Uitleg — Vul de woorden uit het kader in: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = de poorten'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = een tweede kans, een tweede binnenkomst'),
    ('local = 地点', 'local = de locatie'),
    ('祈使式：confira', 'gebiedende wijs: confira'),
]
R7 = [
    ('LÍNGUA · 语言', 'LÍNGUA · TAAL'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具',
     'Focus op taal · Três níveis, três ferramentas · drie niveaus, drie hulpmiddelen'),
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro',
     'Uitleg — Vragen: que horas (hoe laat) + werkwoord; onde fica vraagt naar een plaats; conferir is onregelmatig in de eu-vorm: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (onregelmatig)'),
    ('conferir：você → confere', 'conferir: você → confere'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('onde 问地点', 'onde vraagt naar een plaats'),
    ('讲一周的事用过去时（pretérito perfeito）；revisar 规则（revisei）；chegar/dormir 的过去时注意重音。',
     'Uitleg — Om de week te vertellen gebruiken we de pretérito perfeito; revisar is regelmatig (revisei); chegar en dormir krijgen een accent in de verleden tijd: chegou, dormiu.'),
    ('revisar 过去时：revisei', 'revisar, verleden tijd: revisei'),
    ('chegar 过去时：chegou', 'chegar, verleden tijd: chegou'),
    ('dormir 过去时：dormiu', 'dormir, verleden tijd: dormiu'),
    ('chegaram 是 chegar 的过去时复数', 'chegaram is de verleden tijd (meervoud) van chegar'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。',
     'Uitleg — Na quando, se en quem staat de toekomst in de aanvoegende wijs: tiver, for, chegar — de grammatica van zondagse hypotheses.'),
    ('quem + 虚拟式将来：tiver', 'quem + aanvoegende wijs toekomst: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + aanvoegende wijs toekomst: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + aanvoegende wijs toekomst van ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + toekomst → aanvoegende wijs toekomst for'),
    ('高考用黑笔，蓝笔不行。', 'Alleen zwarte pen, geen blauwe.'),
    ('13 点关门，13:30 到就晚了。', 'Poorten dicht om 13h: 13:30 is te laat.'),
    ('考前一夜突击没用，睡好才记得住。', 'Niet doorhalen: slaap en onthoud.'),
    ('连休是 10 月 31 日到 11 月 2 日，共三天。', '31 oktober tot 2 november: 3 dagen.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · PAS OP!'),
    ('feriadão = 连休长周末，共三天。', 'feriadão = het lange feestweekend, drie dagen.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · WOORD VAN DE WEEK'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！',
     'Voorbeeld van de redactie — geen echte brief. Stuur je brief op: de beste verschijnen op pagina 7 in VOL.3!'),
    ('编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。',
     'Opmerking van de redactie: de echte brieven en beste teksten uit VOL.1 waren nog niet binnen — het voorbeeld blijft, de belofte gaat naar VOL.3.'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）',
     'FRASES DA SEMANA · ZINNEN VAN DE WEEK (letterlijk uit deze editie)'),
    ('从连休到考试：高考周。', 'Van het lange weekend naar het examen: Enem-week.'),
    ('许多人旅行、探亲、去墓园献花。', 'Veel mensen reizen, bezoeken familie en brengen bloemen naar de begraafplaats.'),
    ('亡灵节是怀念的日子。', 'Finados is een dag van herinnering.'),
    ('怀念是继续亲近的方式。', 'Herinneren is een manier om dichtbij te blijven.'),
    ('每一分值一个名次，每一球值一个故事。', 'Elk punt is een plaats waard, elk doelpunt een verhaal.'),
    ('睡得好，记得牢。', 'Goed slapen, beter onthouden.'),
    ('先做容易的，再做难的。', 'Eerst de makkelijke, dan de moeilijke.'),
    ('核对确认卡、睡好、早到。', 'Controleer je kaart, slaap goed, kom vroeg.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'A PRÓXIMA SEMANA · VOLGENDE WEEK (VOL.3)'),
]
R8 = [
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · TOETS EN ANTWOORDEN'),
    ('第 8 版 · A grande prova da semana + todas as respostas',
     'Pagina 8 · A grande prova da semana + todas as respostas'),
    ('第 1 天在 11 月 8 日', 'Dag 1 is op 8 november'),
    ('13 点关门', 'De poorten sluiten om 13h'),
    ('13:30 开考', 'Het examen begint om 13:30'),
    ('亡灵节在 11 月 2 日', 'Finados is op 2 november'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'De return Vasco × Palmeiras is op 8 november'),
    ('连休共 3 天', 'Het lange weekend duurt 3 dagen'),
    ('考试时长 5 个半小时', 'Het examen van dag 8 duurt vijf en een half uur'),
    ('第 2 天在 11 月 15 日', 'Dag 2 is op 15 november'),
    ('连休从 10 月 31 日到 11 月 2 日', 'Het lange weekend loopt van 31 oktober tot 2 november'),
    ('确认卡是高考的文件', 'De bevestigingskaart is een document van het Enem'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', 'De return Atlético-MG × Grêmio is in de Arena MRV'),
    ('第 34 轮周一到周五都有比赛', 'Speelronde 34 heeft van maandag tot vrijdag wedstrijden'),
    ('亡灵节家人们带花', 'Op Finados brengen families bloemen mee'),
    ('万圣节在 10 月 31 日周六', 'Halloween was op zaterdag 31 oktober'),
    ('330 是考试的分钟数', '330 is de duur van het examen in minuten'),
    ('亡灵节又称诸圣灵魂日', 'Finados heet ook de Dag van de Gelovige Zielen'),
    ('卢卡斯住在贝洛奥里藏特', 'Lucas woont in Belo Horizonte'),
    ('连休里他休息并每天复习一点', 'In het lange weekend rust hij uit en herhaalt hij elke dag een beetje'),
    ('前一晚他备好证件和黑笔、早睡', 'De avond ervoor legt hij document en zwarte pen klaar en gaat hij vroeg slapen'),
    ('他 11 点到达考场', 'Hij komt om 11h aan op de examenlocatie'),
    ('时间词在前', 'Het tijdwoord staat vooraan'),
    ('主语 + 动词 + 宾语 + 地点', 'Onderwerp + werkwoord + voorwerp + plaats'),
    ('疑问词组在句首', 'De vraagwoordgroep staat vooraan'),
    ('主语 + 动词 + 宾语', 'Onderwerp + werkwoord + voorwerp'),
    ('11 月 8 日周日是高考的第一天。', 'Zondag 8 november is de eerste dag van het Enem.'),
    ('对照第 6 版标题', 'zie de kop van pagina 6'),
    ('周日前核对确认卡。', 'Controleer je kaart vóór zondag.'),
    ('Confira = 请核对', 'Confira = controleer'),
    ('“连休是 10 月 31 日到 11 月 2 日。” → ___',
     '“Het lange weekend loopt van 31 oktober tot 2 november.” → ___'),
    ('feriadão = 连休', 'feriadão = het lange weekend'),
    ('你到达时，请出示带照片的证件。 → ___', 'Als je aankomt, toon dan je document met foto. → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'aanvoegende wijs toekomst chegar + gebiedende wijs apresente'),
    ('feriadão=连着周末的假期 b', 'feriadão = een feestdag vast aan het weekend (b)'),
    ('portão=考场入口 d', 'portão = de ingang van de examenlocatie (d)'),
    ('reta final=考前最后一周 a', 'reta final = de laatste week vóór het examen (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c',
     'segunda chamada = opnieuw binnenkomen na sluiting (bij het Enem onmogelijk) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = document met foto'),
    ('seção = 考场分区（房间）', 'seção = de examenzaal (de sectie)'),
    ('大门 13 点关闭', 'De poorten sluiten om 13h'),
    ('考试 13:30 开始', 'Het examen begint om 13:30'),
    ('obrigado = 谢谢', 'obrigado = dank je'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。',
     'Uitleg — Schrijfopdracht (geen uniek antwoord); de voorbeeldtekst ({NWORDS} woorden) staat hieronder.'),
    ('（开放题，范文如下）', '(open vraag — voorbeeldtekst hieronder)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'voorbeeldtekst in deel H ({NWORDS} woorden)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可',
     'RESPOSTAS · ANTWOORDEN — per pagina geordend, zoek het nummer'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'bij elk antwoord een korte uitleg in het Nederlands · ✓ = met voorbeeldtekst'),
]

for fn, reps in [('content12.py', R12), ('content34.py', R34),
                 ('content56.py', R56), ('content7.py', R7), ('content8.py', R8)]:
    seen, ordered = set(), []
    for old, new in reps:
        if old not in seen:
            seen.add(old); ordered.append((old, new))
    reps = sorted(ordered, key=lambda r: -len(r[0]))
    t = load(fn)
    for old, new in reps:
        if old in t:
            t = sub(t, old, new, fn=fn)
        else:
            print(f'WARN {fn}: not found (skipped): {old[:60]!r}')
    save(fn, t)

# ---------- 4. line-anchored replacements ----------
t = load('content12.py')
# P2 time-box gloss: the bare '13 点关门' pass above also converts this tuple
# entry; restore the short time-box wording (W43 pattern: short gloss).
t = line_replace(t, '("13h", "os portões fecham", "De poorten sluiten om 13h")',
    '    ("13h", "os portões fecham", "Poorten sluiten 13h"),',
    'content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "PORTUGEES WEEKBLAD · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE", 34, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 19, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

t = load('content7.py')
# rename the disclosure variable (definition, height formula, draw line)
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_nl')
# ROUND 2 (measured run1 defect: quote rows overprinted the VOL.3 preview
# box because the Dutch letters stack ends ~290px lower than the core's):
# quote-row pitch 128 -> 104 (W45 PT x EN precedent), together with the
# shortened err notes / example note / disclosure above.
# ROUND 3 (measured run2 defect: last quote translation baseline 2402.17
# sat 1.8px above the preview-box top 2404, so descenders touched the box):
# pitch 104 -> 96; rows are ~76px tall, so 96 still leaves ~20px air.
t = line_replace(t, 'cyq = fy + 66',
    '    cyq = fy + 66 + (i % 4) * 96  # NL round 3: tightened from 104 so the last quote translation clears the preview box',
    'content7.py')
save('content7.py', t)

t = load('content8.py')
# W43 P8 separator form (tables.json NL column leaves this null; shipped
# W43 PT x NL SVG is the authority: '— Pagina N —')
t = sub(t, '— PÁGINA {pg} —', '— Pagina {pg} —', 1, 'content8.py')
# ROUND 2 (measured run1 defect: 5 FLOW OVERFLOW warnings, key flow ended
# y=2582 past its 2552 bottom and overprinted itself): key size 13.5 -> 13,
# line height 1.16 -> 1.12 (W45 PT x EN precedent, same measured cause).
t = line_replace(t, 'af.para(txt, 13.5',
    '        af.para(txt, 13, lh=1.12, gap=0.5, split=False)',
    'content8.py')
save('content8.py', t)

# ---------- 5. verify: zero CJK in build sources + no bridge remnants ----------
for fn in ['bslib4.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    hits = CJK.findall(t)
    assert not hits, f'{fn}: {len(hits)} CJK chars remain, e.g. {hits[:10]}'
    assert '.bridge(' not in t and 'def bridge' not in t, f'{fn}: bridge remnant'
    print(f'{fn}: CJK 0 OK, bridge 0 OK')
print('TRANSFORM COMPLETE')
