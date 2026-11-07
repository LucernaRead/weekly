# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x EN fan-out transform for W46 VOL.3.

Run inside the already-copied build dir. Every replacement is an exact
literal match (longest strings first); missing literals warn, and the
final pass asserts ZERO CJK chars remain in the build sources.
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + page tags are never touched.
P1 subtitle (330) and badge (372) lines are replaced whole (size/color).
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

def sub(txt, old, new, fn=''):
    n = txt.count(old)
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

# ---------- 0. OUT / BASE repoint ----------
for fn in FILES:
    t = load(fn)
    if 'weekly-report-w46-pt-core' in t:
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-en')
        save(fn, t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · VOL.3 · Text in Portuguese · Explanations in English', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Note | " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. P1 masthead lines (whole-line) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "PORTUGUESE WEEKLY · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE", 35, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "TEXT IN PORTUGUESE · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 19, "sans", True, OLIVE, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 3. type / instr labels ----------
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

# ---------- 4. content replacements (global table, longest-first) ----------
REPL = [
    # bands (reader-language descriptors, W45 precedent)
    ('NÍVEL A2 · Prova e feriado no mesmo domingo', 'LEVEL A2 · Exam and holiday on the same Sunday'),
    ('A2 → B1 · Proclamação da República: 137 anos · 共和国宣言 137 周年', 'A2 → B1 · Proclamação da República: 137 years'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'LEVEL B1 · The football week'),
    ('NÍVEL B1 · A última semana dos jovens · 最后一周：年轻人的冲刺', 'LEVEL B1 · The final week for young people'),
    ('NÍVEL B2 · O segundo domingo explicado · 第二个周日详解', 'LEVEL B2 · The second Sunday, explained'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', 'Três níveis, três ferramentas · Three levels, three tools'),
    ('第 8 版 · A grande prova da semana + todas as respostas', 'PAGE 8 · The big test of the week + all the answers'),
    # top strip / kickers
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · THE PORTUGUESE BRAZIL READS, EVERY WEEK'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · TOP STORY'),
    ('VIDA · 生活', 'VIDA · LIFE'),
    ('CULTURA · 文化', 'CULTURA · CULTURE'),
    ('ESPORTE · 体育', 'ESPORTE · SPORT'),
    ('JOVENS · 青年', 'JOVENS · YOUTH'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · IN DEPTH'),
    ('LÍNGUA · 语言', 'LÍNGUA · LANGUAGE'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · TEST AND ANSWERS'),
    # P1
    ('高考第二天', 'ENEM, DAY 2'),
    ('11 月 15 日第二场考试 · 共和国宣言日假期', 'Nov 15: second exam day · Proclamation of the Republic holiday'),
    ('讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。', 'Key words | a proclamação = proclamation · o feriado = holiday · a natureza = natural sciences · a matemática = mathematics.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · IN NUMBERS'),
    ('12h — os portões abrem no domingo 15（周日 12 点开门）', '12h — os portões abrem no domingo 15 (Sunday: gates open at 12h)'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham (13h: gates close, latecomers do not get in)'),
    ('13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）', '13h30–18h30 — a prova do dia 15 (the day-15 exam, 13:30 to 18:30)'),
    ('90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）', '90 — as questões do dia 15: 45 + 45 (90 questions: 45 + 45)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · NOW YOU TRY'),
    ('proclamação = 宣布（共和国宣言）', 'proclamação = proclamation (of the Republic)'),
    ('proclamação = 宣布（共和国宣言）。', 'proclamação = proclamation (of the Republic).'),
    ('feriado = 假日', 'feriado = holiday'),
    ('portões = 大门（考场大门）', 'portões = the gates (the exam venue gates)'),
    ('18h30 结束', 'ends at 18h30'),
    ('90 道题', '90 questions'),
    ('fazer 现在时 eles 形式：fazem', 'fazer, present tense, eles form: fazem'),
    ('迟到不得入内：13 点后关门', 'Latecomers do not get in after 13h.'),
    # .text.md variant of the line above: the export source carries a trailing 。 which the bare entry leaves behind (F-2).
    ('迟到不得入内：13 点后关门。', 'Latecomers do not get in after 13h.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · IN THIS ISSUE'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · IN BRIEF'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · LIGHTNING QUIZ'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Read the front page and choose · Answers on page 8'),
    ('共和国宣言日在 11 月 15 日', 'The Proclamation of the Republic is on November 15'),
    ('13 点关门', 'The gates close at 13h'),
    ('第 2 天考自然科学与数学', 'Day 2 is natural sciences and mathematics'),
    ('18:30 结束', 'ends at 18:30'),
    # P2
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · THE MANTRA'),
    ('a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。', 'a proclamação = proclamation · o feriado = holiday · a natureza = natural sciences · a matemática = mathematics · conferir = to check · a escala = the rota.'),
    ('在你的国家，落在周日的假日会在周一补休吗？写两句寄来。', 'In your country, does a holiday that falls on a Sunday give you Monday off? Write two sentences and send them in.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · AND YOU?'),
    ('OS HORÁRIOS DO DOMINGO 15 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 15 · SUNDAY TIMETABLE'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · One country, several time zones'),
    ('周日 12 点开门', 'Gates open Sunday 12h'),
    ('13:30 开考', 'Exam starts 13:30'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · PAGE 2 EXERCISES'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Answers on page 8 · Levels are mixed — find answers by number'),
    ('读第 2 版文章，选出正确答案。', 'Read page 2 and choose the right answer.'),
    ('假日落在周日，周一不补休', 'The holiday falls on a Sunday, with no Monday off'),
    # P7-clinic/.text.md variant of the line above: the source carries a trailing 。 (F-2/F-3).
    ('假日落在周日，周一不补休。', 'The holiday falls on a Sunday, with no Monday off.'),
    ('确认卡显示考试地点', 'The confirmation card shows the exam venue'),
    ('巴西没有夏令时，钟表不动', 'Brazil has no daylight saving time: the clocks do not change'),
    ('补全动词的现在时形式。', 'Fill in the present-tense form of the verb.'),
    ('用第 1、2 版的数字填空。', 'Fill in with numbers from pages 1 and 2.'),
    ('12 点到 13 点 = 1 小时', '12h to 13h = 1 hour'),
    ('13:30 至 18:30 = 5 小时', '13:30 to 18:30 = 5 hours'),
    ('5×60 = 300 分钟', '5×60 = 300 minutes'),
    ('proclamação=宣布一个变化 b', 'proclamação = announcing a change (b)'),
    ('feriado=法律规定的休息日 c', 'feriado = a rest day fixed by law (c)'),
    ('natureza=生命、物理与化学的科学 d', 'natureza = the science of life, physics and chemistry (d)'),
    ('matemática=数字与图形的科学 a', 'matemática = the science of numbers and shapes (a)'),
    ('把词和释义配对', 'Match the words to their meanings'),
]
REPL += [
    # P3
    ('a monarquia 君主制 · a república 共和国 · o marechal 元帅 · o exílio 流亡 · o governo 政府 · a lei 法律。', 'a monarquia = monarchy · a república = republic · o marechal = marshal · o exílio = exile · o governo = government · a lei = law.'),
    ('在你的国家，有纪念共和国建立的假日吗？写两句寄来。', 'In your country, is there a holiday that marks the start of the republic? Write two sentences and send them in.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · PAGE 3 EXERCISES'),
    ('读第 3 版文章，选出正确答案。', 'Read page 3 and choose the right answer.'),
    ('共和国宣言在 1889 年 11 月 15 日', 'The Proclamation of the Republic was on November 15, 1889'),
    ('德奥多罗成为巴西第一任总统', 'Deodoro became the first president of Brazil'),
    ('全国性假日，任何城市都不能改为工作日', 'A national holiday no city may turn into a working day'),
    ('2026 年假日落在周日', 'In 2026 the holiday falls on a Sunday'),
    ('共和国里总统由选举产生、任期有限', 'In a republic the president is elected and power has a time limit'),
    ('用方框里的词填空。', 'Fill in with the words from the box.'),
    ('monarquia = 君主制', 'monarquia = monarchy'),
    ('república = 共和国', 'república = republic'),
    ('marechal = 元帅', 'marechal = marshal'),
    ('exílio = 流亡', 'exílio = exile'),
    ('governo = 政府', 'governo = government'),
    ('lei = 法律', 'lei = law'),
    ('用过去时（pretérito perfeito）补全。', 'Fill in with the past tense (pretérito perfeito).'),
    ('tomar 过去时 elas 形式：tomaram', 'tomar, past tense, elas form: tomaram'),
    ('acabar 过去时 ela 形式：acabou', 'acabar, past tense, ela form: acabou'),
    ('ser 过去时 ele 形式：foi', 'ser, past tense, ele form: foi'),
    ('assumir 过去时 ele 形式：assumiu', 'assumir, past tense, ele form: assumiu'),
    ('把词组成正确的句子。', 'Put the words in order to make sentences.'),
    ('主语 + é + 表语', 'Subject + é + complement'),
    ('主语 + 动词 + 表语', 'Subject + verb + complement'),
    ('主语 + 动词 + 宾语 + 时间', 'Subject + verb + object + time'),
    # P4
    ('a ida 首回合 · a volta 次回合 · o gol 进球 · o pênalti 点球 · a pausa 休整期 · o amistoso 友谊赛。', 'a ida = the first leg · a volta = the second leg · o gol = the goal · o pênalti = the penalty · a pausa = the break · o amistoso = the friendly.'),
    ('你在巴西杯支持哪支球队？谁能进决赛？写两句寄来。', 'Which team do you support in the Copa do Brasil — and who reaches the final? Write two sentences and send them in.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · FOOTBALL WEEK'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · PAGE 4 EXERCISES'),
    ('读第 4 版文章，选出正确答案。', 'Read page 4 and choose the right answer.'),
    ('首回合格雷米奥 2 比 0 战胜米内罗竞技', 'In the first leg Grêmio beat Atlético-MG 2–0'),
    ('帕尔梅拉斯 1 比 0 战胜瓦斯科，毛里西奥进球', 'Palmeiras beat Vasco 1–0, with a goal by Maurício'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', 'The Atlético-MG × Grêmio second leg is Saturday the 7th at 18h'),
    ('决赛 12 月 6 日单场，在马内·加林查', 'The final is a single game on December 6, at the Mané Garrincha'),
    ('第 35 轮本周只有一场：米拉索尔 × 米内罗竞技', 'Round 35 has only one game this week: Mirassol × Atlético-MG'),
    ('gol=射入球网的得分 b', 'gol = the point scored in the net (b)'),
    ('ida=对决的第一场 d', 'ida = the first game of a tie (d)'),
    ('volta=对决的第二场 a', 'volta = the second game of a tie (a)'),
    ('pênalti=十一米点的罚球 c', 'pênalti = the kick from the eleven-metre mark (c)'),
    ('用括号里正确的比较形式填空。', 'Fill in with the correct comparative form in brackets.'),
    ('5 小时 < 5.5 小时：menos', '5 hours < 5.5 hours: menos'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Complete the sentences in the past tense (pretérito perfeito).'),
    ('vencer 过去时 ele 形式：venceu', 'vencer, past tense, ele form: venceu'),
    ('marcar 过去时 eles 形式：marcaram', 'marcar, past tense, eles form: marcaram'),
    ('marcar 过去时 ele 形式：marcou', 'marcar, past tense, ele form: marcou'),
    ('convocar 过去时 ele 形式：convocou', 'convocar, past tense, ele form: convocou'),
    ('ser 过去时复数：foram', 'ser, past tense, plural: foram'),
    # P5
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem (check your Enem confirmation card)'),
    ('2. Revise um pouco por dia: Natureza e Matemática（每天复习一点：自然科学与数学）', '2. Revise um pouco por dia: Natureza e Matemática (revise a little each day: natural sciences and mathematics)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova (sleep well the night before the exam)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior (set out your document and black pen the day before)'),
    ('5. Domingo 15: chegue antes das 12h（周日 15 日：12 点前到达）', '5. Domingo 15: chegue antes das 12h (Sunday the 15th: arrive before 12h)'),
    ('a natureza 自然科学 · a matemática 数学 · a maratona 突击马拉松 · a véspera 前夕 · comparar 比较价格 · a cabeça 头脑、状态。', 'a natureza = natural sciences · a matemática = mathematics · a maratona = the cramming marathon · a véspera = the eve · comparar = to compare prices · a cabeça = your head, your state of mind.'),
    ('重要考试前一晚，你是复习到很晚还是早睡？写两句寄来。', 'The night before an important exam, do you revise late or sleep early? Write two sentences and send them in.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · PAGE 5 EXERCISES'),
    ('读第 5 版文章，选出正确答案。', 'Read page 5 and choose the right answer.'),
    ('最后一周在 11 月 15 日周日结束', 'The last week ends Sunday, November 15'),
    ('每天复习一点', 'Revise a little each day'),
    ('提前一天备好证件和黑笔', 'Set out your document and black pen the day before'),
    ('黑五在 11 月 27 日', 'Black Friday is on November 27'),
    ('11 月 14 日周六巴西 × 日本 7:15', 'On Saturday the 14th, Brazil × Japan at 7:15'),
    ('用方框里的词填空。注意：有的词要变成复数。', 'Fill in with the words from the box. Careful: one word must become plural.'),
    ('última semana = 最后一周', 'última semana = the last week'),
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
    ('错：考前突击不是好计划，每天复习一点才好', 'Wrong: cramming the night before is not a good plan — a little revision each day is better'),
    ('对：13:30 至 18:30', 'Right: 13:30 to 18:30'),
    # P6
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões = the gates · a segunda chamada = a second sitting, a second entry · conferir = to check · a correria = the rush.'),
    ('O DOMINGO 15 EM NÚMEROS · 11 月 15 日的数字 (horários oficiais do Inep)', 'O DOMINGO 15 EM NÚMEROS · THE NUMBERS OF SUNDAY 15 (official Inep times)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · PAGE 6 EXERCISES'),
    ('看上面两张图，选出正确答案。', 'Look at the two charts above and choose the right answer.'),
    ('大门开放 60 分钟', 'The gates stay open 60 minutes'),
    ('关门到开考之间等 30 分钟', 'The wait between closing and the exam is 30 minutes'),
    ('考试 300 分钟', 'The exam lasts 300 minutes'),
    ('中午到 18:30 = 6 个半小时', 'Midday to 18:30 = six and a half hours'),
    ('图表数字是 Inep 官方时间', 'The chart figures are official Inep times'),
    ('高考分 8 日和 15 日两个周日', 'The Enem runs on two Sundays: 8 and 15'),
    ('13 点后到场不得入内', 'Arriving after 13h, you do not get in'),
    ('根据句子意思，补全正确的动词形式。', 'Fill in the correct verb form for each sentence.'),
    ('将来时：começará', 'future tense: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + future subjunctive: chegar'),
    ('现在时：fecham', 'present tense: fecham'),
    ('现在时：pede', 'present tense: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', 'Fill in with the words from the box: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = the gates'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = a second sitting, a second entry'),
    ('祈使式：confira', 'imperative: confira'),
    # P7
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', 'Questions: que horas (what time) + verb; onde fica asks where a place is; conferir is irregular in the eu form: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (irregular)'),
    ('onde 问地点', 'onde asks about place'),
    ('讲一周的事用过去时（pretérito perfeito）；vencer 规则（venceu）；marcar/chegar/dormir 的过去时注意重音。', "To tell the week's story we use the pretérito perfeito; vencer is regular (venceu); watch the stress in the past of marcar, chegar and dormir."),
    ('vencer 过去时：venceu', 'vencer, past tense: venceu'),
    ('marcar 过去时：marcou', 'marcar, past tense: marcou'),
    ('chegar 过去时：chegou', 'chegar, past tense: chegou'),
    ('venceram 是 vencer 的过去时复数', 'venceram is the past tense, plural, of vencer'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'After quando, se and quem, the future takes the subjunctive: tiver, for, chegar — the grammar of Sunday hypotheses.'),
    ('quem + 虚拟式将来：tiver', 'quem + future subjunctive: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + future subjunctive: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + future subjunctive of ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + future → future subjunctive for'),
    ('高考用黑笔，蓝笔不行。', 'Black pen only — blue will not do.'),
    ('13 点关门，13:30 到就晚了。', 'Gates close at 13h — 13:30 is too late.'),
    ('15 日考试 18:30 结束，19 点是 8 日的时间。', 'On the 15th the exam ends at 18:30; 19h belongs to the 8th.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · MISTAKES'),
    ('proclamação = 宣布；1889 年君主制结束、共和国开始。', 'proclamação = proclamation; in 1889 the monarchy ended and the Republic began.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · WORD OF THE WEEK'),
    ('编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。', "Editor's note: the real letters and best texts promised in VOL.2 had not arrived by press time — the example stands, and the promise carries over to VOL.4."),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', "Editor's example — not a real letter. Send your letters to the editors!"),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · PHRASES OF THE WEEK (verbatim from this issue)'),
    ('两个周日、一个假日：巴西迎来高考第二天。', 'Two Sundays, one holiday: Brazil sits the second day of the Enem.'),
    ('考试和假日在同一天到来。', 'The exam and the holiday arrive on the same day.'),
    ('假日不改变时钟。', 'The holiday does not change the clock.'),
    ('君主制结束了。', 'The monarchy ended.'),
    ('谁能进巴西杯决赛？', 'Who reaches the Copa do Brasil final?'),
    ('睡得好，记得牢。', 'Sleep well, remember better.'),
    ('先做容易的，再做难的。', 'The easy ones first, then the hard ones.'),
    ('核对确认卡、睡好、早到。', 'Check your card, sleep well, arrive early.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.4)', 'A PRÓXIMA SEMANA · NEXT WEEK (VOL.4)'),
    # P8
    ('第 1 天在 11 月 8 日', 'Day 1 is on November 8'),
    ('第 2 天在 11 月 15 日', 'Day 2 is on November 15'),
    ('确认卡是高考的文件', 'The confirmation card is an Enem document'),
    ('共和国宣言日在 11 月 15 日', 'The Proclamation of the Republic is on November 15'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'The Vasco × Palmeiras second leg is on the 8th'),
    ('第二天共 90 道题', 'Day 2 has 90 questions in total'),
    ('考试时长 5 小时', 'The exam lasts 5 hours'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', 'The Atlético-MG × Grêmio second leg is at Arena MRV'),
    ('第 35 轮本周只有一场，在 14 日', 'Round 35 has only one game this week, on the 14th'),
    ('共和国宣言在 1889 年', 'The Proclamation of the Republic was in 1889'),
    ('11.11 是促销日', '11.11 is the day of promotions'),
    ('300 是考试的分钟数', '300 is the exam length in minutes'),
    ('德奥多罗是第一任总统', 'Deodoro was the first president'),
    ('玛丽娜住在圣保罗', 'Marina lives in São Paulo'),
    ('她每天复习一点自然科学', 'She revises a little natural science each day'),
    ('前一晚她备好证件和黑笔、早睡', 'The night before, she sets out her document and black pen and sleeps early'),
    ('她 11:30 到达考场', 'She reaches the venue at 11:30'),
    ('时间词在前', 'The time word comes first'),
    ('主语 + 动词 + 宾语 + 地点', 'Subject + verb + object + place'),
    ('疑问词组在句首', 'The question phrase comes first'),
    ('主语 + 动词 + 宾语', 'Subject + verb + object'),
    ('11 月 15 日周日是高考的第二天。', 'Sunday, November 15, is the second day of the Enem.'),
    ('对照第 6 版标题', 'See the page 6 headline'),
    ('周日前核对确认卡。', 'Check your card before Sunday.'),
    ('Confira = 请核对', 'Confira = check, confirm'),
    ('“假日落在周日。” → ___', '“The holiday falls on a Sunday.” → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'future subjunctive chegar + imperative apresente'),
    ('你到达时，请出示带照片的证件。 → ___', 'When you arrive, show your photo ID. → ___'),
    ('proclamação=宣布一个变化 b', 'proclamação = announcing a change (b)'),
    ('portão=考场入口 d', 'portão = the exam venue entrance (d)'),
    ('república=1889 年后的国家形式 a', 'república = the form of the State after 1889 (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada = re-entry after closing (there is none in the Enem) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = photo ID'),
    ('seção = 考场分区（房间）', 'seção = the exam room (section)'),
    ('大门 13 点关闭', 'The gates close at 13h'),
    ('考试 18:30 结束', 'The exam ends at 18:30'),
    ('obrigado = 谢谢', 'obrigado = thank you'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', 'Writing task (no single correct answer); the model text ({NWORDS} words) is below.'),
    ('（开放题，范文如下）', '(open task — model text below)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'See the model text in section H of this page ({NWORDS} words)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · ANSWER KEY — grouped by page; find your number'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'One short note per answer · ✓ = the writing model'),
]

for fn, reps in [('content12.py', REPL), ('content34.py', REPL),
                 ('content56.py', REPL), ('content7.py', REPL), ('content8.py', REPL)]:
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

# ---------- 5. disclosure rename + layout tweaks (W45 EN precedent) ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_en')
old_wh = 'len(wrap("proclamação = proclamation; in 1889 the monarchy ended and the Republic began.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box pad line not found'
t = t.replace(old_wh, 'len(wrap("proclamação = proclamation; in 1889 the monarchy ended and the Republic began.", "sans", False, 20, CW - 44)) * 29 + 30')
save('content7.py', t)

t = load('content8.py')
t = line_replace(t, 'af.para(txt, 13.5',
    '        af.para(txt, 13, lh=1.12, gap=0.5, split=False)',
    'content8.py')
save('content8.py', t)

# ---------- 5b. EN layout fixes (gates round 1) ----------
t = load('content12.py')
old_box = '    ("90 — as questões do dia 15: 45 + 45 (90 questions: 45 + 45)", "serif", False, INK, 20, 1.35),\n])'
assert t.count(old_box) == 1, 'numbers box close not found'
t = t.replace(old_box, old_box[:-2] + '], tsize=20)')
save('content12.py', t)

t = load('content7.py')
old_label = "Editor's example — not a real letter. Send your letters to the editors: the best will be printed in VOL.4!"
new_label = "Editor's example — not a real letter. Send your letters to the editors!"
# FIX (Round 1 rebuild): the REPL entry above already emits the SHORT label,
# so the long form never occurs in a fresh derivation (count 0). The §5b
# shortening is a no-op here; the geometry edits below are the live part.
assert t.count(old_label) in (0, 2), f'label count {t.count(old_label)}'
t = t.replace(old_label, new_label)
assert t.count(')) * 29 + 35') == 1, 'letters-box pad line not found'
t = t.replace(')) * 29 + 35', ')) * 29 + 22')
t = line_replace(t, 'fy = max(1712,', 'fy = max(1712, ly + lh + 30)', 'content7.py')
t = line_replace(t, 'cyq = fy + 66', '    cyq = fy + 66 + (i % 4) * 94', 'content7.py')
save('content7.py', t)

# ---------- 5c. FIX F-1 (Round 1 proofread): fullwidth colon in P8 notes ----------
# The 10 note strings below are pure Portuguese (no CJK gloss) inherited from
# the core register with U+FF1A (：). In Latin-script editions they must use
# an ASCII colon, matching neighbouring notes (e.g. item 101). CJK editions
# (ja/zh-cn/zh-tw) legitimately keep ： inside CJK glosses, so this block is
# present ONLY in the 8 Latin-script transforms. Runs after the REPL loop.
for _fn, _old, _new in [
    ("content12.py", "conferir：ele → confere", "conferir: ele → confere"),
    ("content12.py", "abrir：ele → abre", "abrir: ele → abre"),
    ("content12.py", "levar：nós → levamos", "levar: nós → levamos"),
    ("content12.py", "começar：ela → começa", "começar: ela → começa"),
    ("content12.py", "terminar：ela → termina", "terminar: ela → termina"),
    ("content34.py", "2 > 0：mais", "2 > 0: mais"),
    ("content34.py", "3 > 2：mais", "3 > 2: mais"),
    ("content34.py", "17 < 18：mais cedo", "17 < 18: mais cedo"),
    ("content7.py", "conferir：você → confere", "conferir: você → confere"),
    ("content7.py", "terminar：ela → termina", "terminar: ela → termina"),
]:
    _t = load(_fn)
    _t = sub(_t, _old, _new, _fn)
    save(_fn, _t)

# ---------- 6. verify: zero CJK in build sources ----------
for fn in ['bslib4.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    hits = CJK.findall(t)
    assert not hits, f'{fn}: {len(hits)} CJK chars remain, e.g. {hits[:10]}'
    print(f'{fn}: CJK 0 OK')
print('TRANSFORM COMPLETE')
