# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x EN fan-out transform for W45 VOL.2.

Copies nothing: run this inside the already-copied build dir. Every
replacement is an exact literal match with an asserted occurrence count
(longest strings first where one contains another), except two
line-anchored replacements (P1 badge line, P7 B2 bridge line).
After the pass, bslib4.py + content*.py must contain ZERO CJK chars.
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + 'Pagina' tags are never touched.
"""
import os, re, sys

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
        t = sub(t, 'weekly-report-w45-pt-core', 'weekly-report-w45-pt-en', fn=fn)
        save(fn, t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.2 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · VOL.2 · Text in Portuguese · Explanations in English', 1, 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"', 1, 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Note | " + s', 1, 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. type / instr labels (instr first, then bare typ) ----------
INSTR = [
    ('instr="造句"', 'instr="Build the sentence"'),
    ('instr="翻译"', 'instr="Translate"'),
    ('instr="判断"', 'instr="True or false?"'),
    ('instr="写作"', 'instr="Writing"'),
    ('instr="填空"', 'instr="Fill in"'),
    ('instr="把词和释义配对"', 'instr="Match the pairs"'),
]
TYP = [
    ('"完成句子"', '"Complete the sentence"'),
    ('"词汇配对"', '"Vocabulary matching"'),
    ('"判断对错"', '"True or false"'),
    ('"完形单选"', '"Cloze"'),
    ('"单选"', '"Multiple choice"'),
    ('"造句"', '"Sentence building"'),
    ('"翻译"', '"Translation"'),
    ('"写作"', '"Writing"'),
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
     'TODA SEMANA EM PORTUGUÊS · THE PORTUGUESE BRAZIL READS, EVERY WEEK'),
    ('葡 萄 牙 语 周 报 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE',
     'PORTUGUESE WEEKLY · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE'),
    ('11 月 2 日亡灵节连休 · 11 月 8 日高考第一天', 'Nov 2 Finados weekend · Nov 8 Enem day 1'),
    ('全国高考周', 'ENEM WEEK'),
    ('讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。',
     'Key words | feriadão = the long holiday weekend · o portão = the gate · a redação = the essay · revisar = to revise.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · IN NUMBERS'),
    ('12h — os portões abrem no domingo 8（周日 12 点开门）',
     '12h — os portões abrem no domingo 8 (Sunday: gates open at 12h)'),
    ('13h — os portões fecham（13 点关门，过时不入）',
     '13h — os portões fecham (13h: gates close, latecomers do not get in)'),
    ('13h30–19h — a prova do dia 8（考试 13:30 至 19:00）',
     '13h30–19h — a prova do dia 8 (the day-8 exam, 13:30 to 19:00)'),
    ('5h30 — a duração da prova do dia 8（考试时长 5 小时半）',
     '5h30 — a duração da prova do dia 8 (the day-8 exam lasts five and a half hours)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · NOW YOU TRY'),
    ('feriadão = 连休长周末', 'feriadão = the long holiday weekend'),
    ('portões = 大门（考场大门）', 'portões = the gates (the exam venue gates)'),
    ('redação = 作文', 'redação = the essay'),
    ('13h30 开考（巴西利亚时间）', '13h30: the exam starts (Brasília time)'),
    ('19h 结束', '19h: the exam ends'),
    ('revisar 现在时 eles 形式：revisam', 'revisar, present tense, eles form: revisam'),
    ('迟到不得入内：13 点后关门', 'Latecomers do not get in after 13h.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · IN THIS ISSUE'),
    ('“连休”：假期连着周末，一共三天。',
     '“Long weekend”: a holiday plus the weekend.'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · IN BRIEF'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · LIGHTNING QUIZ'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Read the front page and choose · Answers on page 8'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · TOP STORY'),
    ('连休从 10 月 31 日到 11 月 2 日', 'The long weekend runs October 31 to November 2'),
    ('13 点关门', 'The gates close at 13h'),
    ('第 1 天考作文、语言与人文', 'Day 1 is essay, languages and humanities'),
    ('次回合在 7 日和 8 日', 'The second legs are on the 7th and 8th'),
    ('VIDA · 生活', 'VIDA · LIFE'),
    ('NÍVEL A2 · Finados e revisão: o feriadão do Brasil',
     'LEVEL A2 · Finados and revision: the long holiday weekend in Brazil'),
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · THE MANTRA'),
    ('o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。',
     'o feriadão = the long holiday weekend · o cemitério = the cemetery · a vela = the candle · o crisântemo = the chrysanthemum · a missa = Mass · conferir = to check.'),
    ('在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。',
     'In your country, is there a day for remembering the dead? What do families do on that day? Write two sentences in Portuguese and send them to us: the best will appear on page 7, «Cartas dos leitores».'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · AND YOU?'),
    ('OS HORÁRIOS DO DOMINGO 8 · 周日时间表', "OS HORÁRIOS DO DOMINGO 8 · SUNDAY'S TIMETABLE"),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · One country, several clocks'),
    ('周日 12 点开门', 'Gates open Sunday 12h'),
    ('13 点关门', 'Gates close at 13h'),
    ('13:30 开考', 'Exam starts 13:30'),
    ('19:00 结束', 'Exam ends 19:00'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · PAGE 2 EXERCISES'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Answers on page 8 · Levels are mixed — find answers by number'),
    ('读第 2 版文章，选出正确答案。', 'Read page 2 and choose the right answer.'),
    ('亡灵节家人们去墓园献花', 'On Finados, families visit cemeteries and bring flowers'),
    ('确认卡显示考试地点', 'The confirmation card shows the exam venue'),
    ('巴西没有夏令时，钟表不动', 'Brazil has no daylight saving time: the clocks do not change'),
    ('补全动词的现在时形式。', 'Fill in the present-tense form of the verb.'),
    ('conferir：ele → confere', 'conferir: ele → confere'),
    ('abrir：ele → abre', 'abrir: ele → abre'),
    ('levar：nós → levamos', 'levar: nós → levamos'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('ser 现在时 ela 形式：é', 'ser, present tense, ela form: é'),
    ('用第 1、2 版的数字填空。', 'Fill in with numbers from pages 1 and 2.'),
    ('12 点到 13 点 = 1 小时', '12h to 13h = 1 hour'),
    ('13:30 至 19:00 = 5 个半小时', '13:30 to 19:00 = five and a half hours'),
    ('5×60 + 30 = 330 分钟', '5×60 + 30 = 330 minutes'),
    ('31 日、1 日、2 日 = 3 天', '31st, 1st, 2nd = 3 days'),
    ('feriadão=连着周末的假期 c', 'feriadão = a holiday joined to the weekend (c)'),
    ('cemitério=墓碑所在的地方 b', 'cemitério = where the tombs are (b)'),
    ('vela=点亮纪念的物品 d', 'vela = the item lit in memory (d)'),
    ('crisântemo=亡灵节带去的花 a', 'crisântemo = the flower taken on Finados (a)'),
]
R34 = [
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · AND YOU?'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Answers on page 8 · Levels are mixed — find answers by number'),
    ('CULTURA · 文化', 'CULTURA · CULTURE'),
    ('A2 → B1 · Finados: o dia da memória · 亡灵节：怀念的日子',
     'A2 → B1 · Finados: the day of remembrance'),
    ('o túmulo 墓碑 · a flor 花 · acender 点燃 · rezar 祈祷 · o silêncio 寂静 · a lembrança 怀念。',
     'o túmulo = the tomb · a flor = the flower · acender = to light · rezar = to pray · o silêncio = silence · a lembrança = remembrance.'),
    ('在你的文化里，人们怎样怀念逝者？写两句寄来。',
     'In your culture, how do people remember the dead? Write two sentences in Portuguese and send them to us.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · PAGE 3 EXERCISES'),
    ('读第 3 版文章，选出正确答案。', 'Read page 3 and choose the right answer.'),
    ('亡灵节是怀念与安静的日子', 'Finados is a day of remembrance and quiet'),
    ('家人们带花去墓园，主要是菊花', 'Families take flowers to cemeteries, above all chrysanthemums'),
    ('教堂和墓园整天都有弥撒', 'In churches and cemeteries there are Masses all day'),
    ('万圣节在 10 月 31 日周六', 'Halloween was Saturday, October 31'),
    ('怀念是继续亲近的方式', 'Remembering is a way of staying close'),
    ('用方框里的词填空。', 'Fill in with the words from the box.'),
    ('túmulo = 墓碑', 'túmulo = the tomb'),
    ('vela = 蜡烛', 'vela = the candle'),
    ('crisântemo = 菊花', 'crisântemo = the chrysanthemum'),
    ('missa = 弥撒', 'missa = Mass'),
    ('silêncio = 寂静', 'silêncio = silence'),
    ('lembrança = 怀念', 'lembrança = remembrance'),
    ('用过去时（pretérito perfeito）补全。', 'Fill in with the past tense (pretérito perfeito).'),
    ('visitar 过去时 elas 形式：visitaram', 'visitar, past tense, elas form: visitaram'),
    ('levar 过去时 elas 形式：levaram', 'levar, past tense, elas form: levaram'),
    ('ser 过去时 ele 形式：foi', 'ser, past tense, ele form: foi'),
    ('viver 过去时 ele 形式：viveu', 'viver, past tense, ele form: viveu'),
    ('把词组成正确的句子。', 'Put the words in order to make sentences.'),
    ('主语 + é + 表语', 'Subject + é + complement'),
    ('主语 + 动词 + 宾语 + 地点', 'Subject + verb + object + place'),
    ('主语 + 动词 + 宾语', 'Subject + verb + object'),
    ('ESPORTE · 体育', 'ESPORTE · SPORT'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'LEVEL B1 · The football week'),
    ('a ida 首回合 · a volta 次回合 · o finalista 决赛球队 · a decisão 决战 · a rodada 轮次。',
     'a ida = the first leg · a volta = the second leg · o finalista = the finalist · a decisão = the decider · a rodada = the round.'),
    ('你在巴西杯支持哪支球队？写两句寄来。',
     'Which team do you support in the Copa do Brasil? Write two sentences in Portuguese and send them to us.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · FOOTBALL WEEK'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · PAGE 4 EXERCISES'),
    ('读第 4 版文章，选出正确答案。', 'Read page 4 and choose the right answer.'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点',
     'The Atlético-MG × Grêmio second leg is Saturday the 7th at 18h'),
    ('瓦斯科 × 帕尔梅拉斯次回合在周日 8 日 17 点，圣雅努阿里奥',
     'The Vasco × Palmeiras second leg is Sunday the 8th at 17h, at São Januário'),
    ('首回合在 11 月 1 日周日', 'The first legs were Sunday, November 1'),
    ('第 34 轮周一到周五每天都有比赛', 'Round 34 has games Monday to Friday'),
    ('两回合总比分胜者进决赛', 'Whoever wins on aggregate over the two games reaches the final'),
    ('finalista=进决赛的球队 b', 'finalista = the team that reaches the final (b)'),
    ('ida=对决的第一场 c', 'ida = the first game of a tie (c)'),
    ('volta=对决的第二场 a', 'volta = the second game of a tie (a)'),
    ('rodada=一轮比赛 d', 'rodada = a round of games (d)'),
    ('用括号里正确的比较形式填空。', 'Fill in with the correct comparative form in brackets.'),
    ('次回合决定决赛名额：mais', 'The second leg decides the finalists: mais'),
    ('18 > 16：mais', '18 > 16: mais'),
    ('17 < 18：mais cedo', '17 < 18: mais cedo'),
    ('第 34 轮周一到周五都有比赛：mais', 'Round 34 runs Monday to Friday: mais'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Complete the sentences in the past tense (pretérito perfeito).'),
    ('ser 过去时复数：foram', 'ser, past tense, plural: foram'),
    ('receber 过去时 ele 形式：recebeu', 'receber, past tense, ele form: recebeu'),
    ('começar 过去时 ela 形式：começou', 'começar, past tense, ela form: começou'),
    ('chegar 过去时 eles 形式：chegaram', 'chegar, past tense, eles form: chegaram'),
]
R56 = [
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · AND YOU?'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Answers on page 8 · Levels are mixed — find answers by number'),
    ('JOVENS · 青年', 'JOVENS · YOUTH'),
    ('NÍVEL B1 · A reta final dos jovens · 冲刺周：年轻人的最后一周',
     'LEVEL B1 · The young and the final stretch'),
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）',
     '1. Confira o Cartão de Confirmação do Enem (check your Enem confirmation card)'),
    ('2. Revise um pouco por dia, sem maratona（每天复习一点，不搞突击）',
     '2. Revise um pouco por dia, sem maratona (revise a little each day, no cramming)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）',
     '3. Durma bem na véspera da prova (sleep well the night before the exam)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）',
     '4. Separe documento e caneta preta no dia anterior (set out your document and black pen the day before)'),
    ('5. Domingo 8: chegue antes das 12h（周日 8 日：12 点前到达）',
     '5. Domingo 8: chegue antes das 12h (Sunday the 8th: arrive before 12h)'),
    ('a reta final 最后冲刺 · a véspera 前夕 · a maratona 突击马拉松 · separar 准备好 · a cabeça 头脑、状态。',
     'a reta final = the final stretch · a véspera = the eve · a maratona = the cramming marathon · separar = to set out · a cabeça = your head, your state of mind.'),
    ('重要考试前一晚，你的计划是复习还是休息？写两句寄来。',
     'The night before an important exam, is your plan to revise or to rest? Write two sentences in Portuguese.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · PAGE 5 EXERCISES'),
    ('读第 5 版文章，选出正确答案。', 'Read page 5 and choose the right answer.'),
    ('冲刺周在 11 月 8 日周日结束', 'The final stretch ends Sunday, November 8'),
    ('每天复习一点', 'Revise a little each day'),
    ('提前一天备好证件和黑笔', 'Set out your document and black pen the day before'),
    ('第 2 天考自然科学与数学', 'Day 2 is natural sciences and mathematics'),
    ('11 月 3 日周二各州议会结束休会', 'On Tuesday the 3rd, the state assemblies return from recess'),
    ('用方框里的词填空。注意：有的词要变成复数。',
     'Fill in with the words from the box. Careful: one word must become plural.'),
    ('reta final = 最后冲刺阶段', 'reta final = the final stretch'),
    ('inscrito 配合复数：inscritos', 'inscrito agrees in the plural: inscritos'),
    ('véspera = 前夕', 'véspera = the eve'),
    ('maratona = 突击马拉松', 'maratona = the cramming marathon'),
    ('local = 地点', 'local = the venue'),
    ('separar 祈使式：separe', 'separar, imperative: separe'),
    ('用将来时（futuro do presente）补全。', 'Fill in with the future tense (futuro do presente).'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, future tense, eles irregular form: farão'),
    ('mostrar 将来时：mostrará', 'mostrar, future tense: mostrará'),
    ('sair 将来时复数：sairão', 'sair, future tense, plural: sairão'),
    ('chegar 将来时：chegará', 'chegar, future tense: chegará'),
    ('确认卡显示考试地点', 'The confirmation card shows the exam venue'),
    ('错：考前突击不是好计划，每天复习一点才好',
     'Wrong: cramming the night before is not a good plan — a little revision each day is better'),
    ('对：13:30 至 19:00', 'Right: 13:30 to 19:00'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · IN DEPTH'),
    ('NÍVEL B2 · O Enem explicado · 高考详解', 'LEVEL B2 · The Enem, explained'),
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。',
     'os portões = the gates · a segunda chamada = a second sitting, a second entry · conferir = to check · a correria = the rush.'),
    ('O DOMINGO 8 EM NÚMEROS · 11 月 8 日的数字 (horários oficiais do Inep)',
     'O DOMINGO 8 EM NÚMEROS · THE NUMBERS OF SUNDAY 8 (official Inep times)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · PAGE 6 EXERCISES'),
    ('看上面两张图，选出正确答案。', 'Look at the two charts above and choose the right answer.'),
    ('大门开放 60 分钟', 'The gates stay open 60 minutes'),
    ('关门到开考之间等 30 分钟', 'The wait between closing and the exam is 30 minutes'),
    ('考试 330 分钟', 'The exam lasts 330 minutes'),
    ('中午到 19 点 = 7 小时', 'Midday to 19h = 7 hours'),
    ('图表数字是 Inep 官方时间', 'The chart figures are official Inep times'),
    ('高考分 8 日和 15 日两个周日', 'The Enem runs on two Sundays: 8 and 15'),
    ('第 1 天考作文、语言与人文', 'Day 1 is essay, languages and humanities'),
    ('13 点后到场不得入内', 'Arriving after 13h, you do not get in'),
    ('根据句子意思，补全正确的动词形式。', 'Fill in the correct verb form for each sentence.'),
    ('将来时：começará', 'future tense: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + future subjunctive: chegar'),
    ('现在时：fecham', 'present tense: fecham'),
    ('现在时：pede', 'present tense: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir',
     'Fill in with the words from the box: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = the gates'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = a second sitting, a second entry'),
    ('local = 地点', 'local = the venue'),
    ('祈使式：confira', 'imperative: confira'),
]
R7 = [
    ('LÍNGUA · 语言', 'LÍNGUA · LANGUAGE'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具',
     'Três níveis, três ferramentas · Three levels, three tools'),
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro',
     'Questions: que horas (what time) + verb; onde fica asks where a place is; conferir is irregular in the eu form: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (irregular)'),
    ('conferir：você → confere', 'conferir: você → confere'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('onde 问地点', 'onde asks about place'),
    ('讲一周的事用过去时（pretérito perfeito）；revisar 规则（revisei）；chegar/dormir 的过去时注意重音。',
     "To tell the week's story we use the pretérito perfeito; revisar is regular (revisei); chegar and dormir take an accent in the past: chegou, dormiu."),
    ('revisar 过去时：revisei', 'revisar, past tense: revisei'),
    ('chegar 过去时：chegou', 'chegar, past tense: chegou'),
    ('dormir 过去时：dormiu', 'dormir, past tense: dormiu'),
    ('chegaram 是 chegar 的过去时复数', 'chegaram is the past tense, plural, of chegar'),
    ('quem + 虚拟式将来：tiver', 'quem + future subjunctive: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + future subjunctive: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + future subjunctive of ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + future → future subjunctive for'),
    ('高考用黑笔，蓝笔不行。', 'Black pen only — blue will not do.'),
    ('13 点关门，13:30 到就晚了。', 'Gates close at 13h — 13:30 is too late.'),
    ('考前一夜突击没用，睡好才记得住。', 'No all-nighter — sleep and remember.'),
    ('连休是 10 月 31 日到 11 月 2 日，共三天。', 'October 31 to November 2 — three days.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · MISTAKES'),
    ('feriadão = 连休长周末，共三天。', 'feriadão = the long holiday weekend.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · WORD OF THE WEEK'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！',
     "Editor's example — not a real letter. Send your letters to the editors: the best will be printed in VOL.3!"),
    ('编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。',
     "Editor's note: the real letters and best texts promised in VOL.1 had not arrived by press time — the example stands, and the promise carries over to VOL.3."),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）',
     'FRASES DA SEMANA · PHRASES OF THE WEEK (verbatim from this issue)'),
    ('从连休到考试：高考周。', 'From the long weekend to the exam: Enem week.'),
    ('许多人旅行、探亲、去墓园献花。', 'Many people travel, visit family and take flowers to the cemetery.'),
    ('亡灵节是怀念的日子。', 'Finados is a day of remembrance.'),
    ('怀念是继续亲近的方式。', 'Remembering is a way of staying close.'),
    ('每一分值一个名次，每一球值一个故事。', 'Every point is worth a place, every goal a story.'),
    ('睡得好，记得牢。', 'Sleep well, remember better.'),
    ('先做容易的，再做难的。', 'The easy ones first, then the hard ones.'),
    ('核对确认卡、睡好、早到。', 'Check your card, sleep well, arrive early.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'A PRÓXIMA SEMANA · NEXT WEEK (VOL.3)'),
]
R8 = [
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · TEST AND ANSWERS'),
    ('第 8 版 · A grande prova da semana + todas as respostas',
     'PAGE 8 · The big test of the week + all the answers'),
    ('第 1 天在 11 月 8 日', 'Day 1 is on November 8'),
    ('13 点关门', 'The gates close at 13h'),
    ('13:30 开考', 'The exam starts at 13:30'),
    ('亡灵节在 11 月 2 日', 'Finados is on November 2'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'The Vasco × Palmeiras second leg is on the 8th'),
    ('连休共 3 天', 'The long weekend is 3 days'),
    ('考试时长 5 个半小时', 'The day-8 exam lasts five and a half hours'),
    ('第 2 天在 11 月 15 日', 'Day 2 is on November 15'),
    ('连休从 10 月 31 日到 11 月 2 日', 'The long weekend runs October 31 to November 2'),
    ('确认卡是高考的文件', 'The confirmation card is an Enem document'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场',
     'The Atlético-MG × Grêmio second leg is at Arena MRV'),
    ('第 34 轮周一到周五都有比赛', 'Round 34 has games Monday to Friday'),
    ('亡灵节家人们带花', 'On Finados, families bring flowers'),
    ('万圣节在 10 月 31 日周六', 'Halloween was Saturday, October 31'),
    ('330 是考试的分钟数', "330 is the exam's length in minutes"),
    ('亡灵节又称诸圣灵魂日', 'Finados is also called the Day of the Faithful Departed'),
    ('卢卡斯住在贝洛奥里藏特', 'Lucas lives in Belo Horizonte'),
    ('连休里他休息并每天复习一点', 'Over the long weekend he rests and revises a little each day'),
    ('前一晚他备好证件和黑笔、早睡',
     'The night before, he sets out his document and black pen and sleeps early'),
    ('他 11 点到达考场', 'He reaches the venue at 11h'),
    ('时间词在前', 'The time word comes first'),
    ('主语 + 动词 + 宾语 + 地点', 'Subject + verb + object + place'),
    ('疑问词组在句首', 'The question phrase comes first'),
    ('主语 + 动词 + 宾语', 'Subject + verb + object'),
    ('11 月 8 日周日是高考的第一天。', 'Sunday, November 8, is the first day of the Enem.'),
    ('对照第 6 版标题', 'See the page 6 headline'),
    ('周日前核对确认卡。', 'Check your card before Sunday.'),
    ('Confira = 请核对', 'Confira = check, confirm'),
    ('“连休是 10 月 31 日到 11 月 2 日。” → ___',
     '“The long holiday weekend runs from October 31 to November 2.” → ___'),
    ('feriadão = 连休', 'feriadão = the long holiday weekend'),
    ('你到达时，请出示带照片的证件。 → ___', 'When you arrive, show your photo ID. → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'future subjunctive chegar + imperative apresente'),
    ('feriadão=连着周末的假期 b', 'feriadão = a holiday joined to the weekend (b)'),
    ('portão=考场入口 d', 'portão = the exam venue entrance (d)'),
    ('reta final=考前最后一周 a', 'reta final = the last week before the exam (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c',
     'segunda chamada = re-entry after closing (there is none in the Enem) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = photo ID'),
    ('seção = 考场分区（房间）', 'seção = the exam room (section)'),
    ('大门 13 点关闭', 'The gates close at 13h'),
    ('考试 13:30 开始', 'The exam starts at 13:30'),
    ('obrigado = 谢谢', 'obrigado = thank you'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。',
     'Writing task (no single correct answer); the model text ({NWORDS} words) is below.'),
    ('（开放题，范文如下）', '(open task — model text below)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'See the model text in section H of this page ({NWORDS} words)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可',
     'RESPOSTAS · ANSWER KEY — grouped by page; find your number'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'One short note per answer · ✓ = the writing model'),
]

for fn, reps in [('content12.py', R12), ('content34.py', R34),
                 ('content56.py', R56), ('content7.py', R7), ('content8.py', R8)]:
    # longest-first + dedupe: a short note must never eat a substring of a longer one
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
t = line_replace(t, '("13h", "os portões fecham", "The gates close at 13h")',
    '    ("13h", "os portões fecham", "Gates close at 13h"),',
    'content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "PORTUGUESE WEEKLY · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE", 38, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "TEXT IN PORTUGUESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 19, "sans", True, OLIVE, anchor="middle")',
    'content12.py')
save('content12.py', t)

t = load('content7.py')
# P7 B2 bridge: replace whole line (avoids retyping its full-width punctuation)
t = line_replace(t, 'c.bridge(',
    'c.bridge("After quando, se and quem, the future takes the subjunctive: tiver, for, chegar — the grammar of Sunday hypotheses.")',
    'content7.py')
# rename the disclosure variable (definition, height formula, draw line)
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_en')
save('content7.py', t)

t = load('content12.py')
# numbers-box title overflows its box at 23pt (W43 precedent: tsize=20)
old_close = '    ("5h30 — a duração da prova do dia 8 (the day-8 exam lasts five and a half hours)", "serif", False, INK, 20, 1.35),\n])'
assert t.count(old_close) == 1, 'numbers box close not found'
t = t.replace(old_close, old_close[:-2] + '], tsize=20)')
save('content12.py', t)

t = load('content7.py')
# word-box bottom pad 20 -> 30 (gloss descenders pressed the border by 1.1px)
old_wh = 'len(wrap("feriadão = the long holiday weekend.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1
t = t.replace(old_wh, 'len(wrap("feriadão = the long holiday weekend.", "sans", False, 20, CW - 44)) * 29 + 30')
t = line_replace(t, 'cyq = fy + 66',
    '    cyq = fy + 66 + (i % 4) * 104  # EN: tightened from 108 to restore preview-box clearance after the word-box pad',
    'content7.py')
save('content7.py', t)

t = load('content8.py')
t = line_replace(t, 'af.para(txt, 13.5',
    '        af.para(txt, 13, lh=1.12, gap=0.5, split=False)',
    'content8.py')
save('content8.py', t)

# ---------- 5. verify: zero CJK in build sources ----------
for fn in ['bslib4.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    hits = CJK.findall(t)
    assert not hits, f'{fn}: {len(hits)} CJK chars remain, e.g. {hits[:10]}'
    print(f'{fn}: CJK 0 OK')
print('TRANSFORM COMPLETE')
