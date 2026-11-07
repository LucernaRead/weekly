# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x RU fan-out transform for W45 VOL.2.

Run inside the already-copied build dir (copy of weekly-report-w45-pt-build).
Every replacement is an exact literal match with an asserted occurrence
count (longest strings first within each file). Furniture follows the W43
PTxRU shipped edition (files/weekly-report-pt-ru), which governs over the
README #20 generalisations: RU badge/footer/page line/gloss prefix/P8
separator/bilingual heads, bridge() renamed expl() (W43 RU-column rule),
half-width parens + space for Russian bracket notes (W43 D7).
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote Portuguese strings are never touched; P7 page
tags follow W43 RU: «Страница N».
After the pass, bslib4.py + content*.py must contain ZERO CJK chars.
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

# ---------- 0. OUT / BASE repoint ----------
for fn in FILES:
    t = load(fn)
    if 'weekly-report-w45-pt-core' in t:
        t = sub(t, 'weekly-report-w45-pt-core', 'weekly-report-w45-pt-ru', fn=fn)
        save(fn, t)

# ---------- 1. bslib4 furniture (W43 RU column) ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.2 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА ПОРТУГАЛЬСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ', 1, 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из {total}"', 1, 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Пояснение — " + s', 1, 'bslib4.py')
t = sub(t, 'def bridge(self', 'def expl(self', 1, 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. type / instr labels (instr first, then bare typ) ----------
INSTR = [
    ('instr="造句"', 'instr="Составьте"'),
    ('instr="翻译"', 'instr="Переведите"'),
    ('instr="判断"', 'instr="Верно или нет?"'),
    ('instr="写作"', 'instr="Напишите"'),
    ('instr="填空"', 'instr="Вставьте"'),
    ('instr="把词和释义配对"', 'instr="Соедините пары"'),
]
TYP = [
    ('"完形单选"', '"Выбор в пропуске"'),
    ('"完成句子"', '"Вставьте слово"'),
    ('"词汇配对"', '"Сопоставление"'),
    ('"判断对错"', '"Верно или нет"'),
    ('"单选"', '"Выбор ответа"'),
    ('"造句"', '"Составьте предложение"'),
    ('"翻译"', '"Перевод"'),
    ('"写作"', '"Письмо"'),
]
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    for old, new in INSTR:
        if old in t:
            t = sub(t, old, new, fn=fn)
    for old, new in TYP:
        if old in t:
            t = sub(t, old, new, fn=fn)
    # bridge -> expl calls (W43 RU-column rule; 21 calls total)
    if '.bridge(' in t:
        t = t.replace('.bridge(', '.expl(')
    save(fn, t)
_n = 0
for fn in ['content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    _n += load(fn).count('.expl(')
assert _n == 21, f'expl calls {_n}, expected 21'
print('expl calls 21 OK')

# ---------- 3. content replacements (longest-first within each file) ----------
R12 = [
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语',
     'TODA SEMANA EM PORTUGUÊS · КАЖДУЮ НЕДЕЛЮ · ПОРТУГАЛЬСКИЙ БРАЗИЛИИ'),
    ('葡 萄 牙 语 周 报 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE',
     'ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE'),
    ('O JORNAL SEMANAL PARA APRENDER — O BRASIL DE VERDADE, EM PORTUGUÊS, DO BRASIL',
     'ТЕКСТЫ НА ПОРТУГАЛЬСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ'),
    ('11 月 2 日亡灵节连休 · 11 月 8 日高考第一天', '2 ноября — выходные на Финадос · 8 ноября — первый день Enem'),
    ('全国高考周', 'НЕДЕЛЯ ENEM'),
    ('讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。',
     'Пояснение — feriadão = длинные праздничные выходные · o portão = ворота · a redação = сочинение · revisar = повторять.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · Цифры'),
    ('12h — os portões abrem no domingo 8（周日 12 点开门）',
     '12h — os portões abrem no domingo 8 (воскресенье 8-го: ворота открываются в 12h)'),
    ('13h — os portões fecham（13 点关门，过时不入）',
     '13h — os portões fecham (в 13h ворота закрываются, опоздавших не пускают)'),
    ('13h30–19h — a prova do dia 8（考试 13:30 至 19:00）',
     '13h30–19h — a prova do dia 8 (экзамен дня 8: с 13:30 до 19:00)'),
    ('5h30 — a duração da prova do dia 8（考试时长 5 小时半）',
     '5h30 — a duração da prova do dia 8 (экзамен дня 8 длится пять с половиной часов)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · Теперь вы'),
    ('feriadão = 连休长周末', 'feriadão = длинные праздничные выходные'),
    ('portões = 大门（考场大门）', 'portões = ворота (ворота экзаменационного центра)'),
    ('redação = 作文', 'redação = сочинение'),
    ('13h30 开考（巴西利亚时间）', '13h30: экзамен начинается (время Бразилиа)'),
    ('19h 结束', '19h: экзамен заканчивается'),
    ('revisar 现在时 eles 形式：revisam', 'revisar, настоящее время, форма eles: revisam'),
    ('迟到不得入内：13 点后关门', 'Опоздавших не пускают после 13h'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · В этом выпуске'),
    ('“连休”：假期连着周末，一共三天。',
     '«Длинные выходные»: праздник и уик-энд.'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · Коротко'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · Блиц-опрос'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Прочитайте первую полосу и выберите ответ · Ответы — страница 8'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · Главная новость'),
    ('连休从 10 月 31 日到 11 月 2 日', 'Длинные выходные — с 31 октября по 2 ноября'),
    ('13 点关门', 'Ворота закрываются в 13h'),
    ('第 1 天考作文、语言与人文', 'День 1: сочинение, языки и гуманитарные науки'),
    ('次回合在 7 日和 8 日', 'Ответные матчи — 7-го и 8-го'),
    ('VIDA · 生活', 'VIDA · Жизнь'),
    ('NÍVEL A2 · Finados e revisão: o feriadão do Brasil',
     'NÍVEL A2 · Finados e revisão: o feriadão do Brasil · Финадос и повторение: длинные выходные Бразилии'),
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · Памятка'),
    ('o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。',
     'o feriadão = длинные праздничные выходные · o cemitério = кладбище · a vela = свеча · o crisântemo = хризантема · a missa = месса · conferir = проверять.'),
    ('在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。',
     'В вашей стране есть день памяти умерших? Что делают семьи в этот день? Напишите две фразы по-португальски и пришлите в редакцию: лучшие появятся на странице 7.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · А вы?'),
    ('OS HORÁRIOS DO DOMINGO 8 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 8 · Расписание воскресенья 8-го'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · Одна страна, несколько часовых поясов'),
    ('周日 12 点开门', 'Ворота открываются в 12h'),
    ('13:30 开考', 'Экзамен начинается в 13:30'),
    ('19:00 结束', 'Экзамен заканчивается в 19:00'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · Упражнения страницы 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Ответы на странице 8 · Уровни перемешаны — ищите по номеру задания'),
    ('读第 2 版文章，选出正确答案。', 'Прочитайте статью на странице 2 и выберите правильный ответ.'),
    ('亡灵节家人们去墓园献花', 'На Финадос семьи идут на кладбище с цветами'),
    ('确认卡显示考试地点', 'Карточка подтверждения показывает место экзамена'),
    ('巴西没有夏令时，钟表不动', 'В Бразилии нет летнего времени: часы не переводят'),
    ('补全动词的现在时形式。', 'Вставьте глаголы в настоящем времени.'),
    ('conferir：ele → confere', 'conferir: ele → confere'),
    ('abrir：ele → abre', 'abrir: ele → abre'),
    ('levar：nós → levamos', 'levar: nós → levamos'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('ser 现在时 ela 形式：é', 'ser, настоящее время, форма ela: é'),
    ('用第 1、2 版的数字填空。', 'Заполните пропуски цифрами со страниц 1 и 2.'),
    ('12 点到 13 点 = 1 小时', 'С 12h до 13h = 1 час'),
    ('13:30 至 19:00 = 5 个半小时', 'С 13:30 до 19:00 = пять с половиной часов'),
    ('5×60 + 30 = 330 分钟', '5×60 + 30 = 330 минут'),
    ('31 日、1 日、2 日 = 3 天', '31-е, 1-е, 2-е = 3 дня'),
    ('feriadão=连着周末的假期 c', 'feriadão = праздник, слившийся с выходными (c)'),
    ('cemitério=墓碑所在的地方 b', 'cemitério = место, где стоят надгробия (b)'),
    ('vela=点亮纪念的物品 d', 'vela = то, что зажигают в память (d)'),
    ('crisântemo=亡灵节带去的花 a', 'crisântemo = цветок, который несут на Финадос (a)'),
]
R34 = [
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · А вы?'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Ответы на странице 8 · Уровни перемешаны — ищите по номеру задания'),
    ('CULTURA · 文化', 'CULTURA · Культура'),
    ('A2 → B1 · Finados: o dia da memória · 亡灵节：怀念的日子',
     'A2 → B1 · Finados: o dia da memória · День памяти'),
    ('o túmulo 墓碑 · a flor 花 · acender 点燃 · rezar 祈祷 · o silêncio 寂静 · a lembrança 怀念。',
     'o túmulo = надгробие · a flor = цветок · acender = зажигать · rezar = молиться · o silêncio = тишина · a lembrança = воспоминание.'),
    ('在你的文化里，人们怎样怀念逝者？写两句寄来。',
     'В вашей культуре как поминают умерших? Напишите две фразы по-португальски и пришлите нам.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · Упражнения страницы 3'),
    ('读第 3 版文章，选出正确答案。', 'Прочитайте статью на странице 3 и выберите правильный ответ.'),
    ('亡灵节是怀念与安静的日子', 'Финадос — день воспоминаний и тишины'),
    ('家人们带花去墓园，主要是菊花', 'Семьи несут цветы на кладбище, прежде всего хризантемы'),
    ('教堂和墓园整天都有弥撒', 'В церквях и на кладбищах мессы идут весь день'),
    ('万圣节在 10 月 31 日周六', 'Хэллоуин был в субботу, 31 октября'),
    ('怀念是继续亲近的方式', 'Воспоминание — способ оставаться рядом'),
    ('用方框里的词填空。', 'Заполните пропуски словами из рамки.'),
    ('túmulo = 墓碑', 'túmulo = надгробие'),
    ('vela = 蜡烛', 'vela = свеча'),
    ('crisântemo = 菊花', 'crisântemo = хризантема'),
    ('missa = 弥撒', 'missa = месса'),
    ('silêncio = 寂静', 'silêncio = тишина'),
    ('lembrança = 怀念', 'lembrança = воспоминание'),
    ('用过去时（pretérito perfeito）补全。', 'Дополните в прошедшем времени (pretérito perfeito).'),
    ('visitar 过去时 elas 形式：visitaram', 'visitar, прошлое время, форма elas: visitaram'),
    ('levar 过去时 elas 形式：levaram', 'levar, прошлое время, форма elas: levaram'),
    ('ser 过去时 ele 形式：foi', 'ser, прошлое время, форма ele: foi'),
    ('viver 过去时 ele 形式：viveu', 'viver, прошлое время, форма ele: viveu'),
    ('把词组成正确的句子。', 'Составьте из слов правильные предложения.'),
    ('主语 + é + 表语', 'Подлежащее + é + сказуемое'),
    ('主语 + 动词 + 宾语 + 地点', 'Подлежащее + глагол + дополнение + место'),
    ('主语 + 动词 + 宾语', 'Подлежащее + глагол + дополнение'),
    ('ESPORTE · 体育', 'ESPORTE · Спорт'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'NÍVEL B1 · O futebol da semana · Неделя футбола'),
    ('a ida 首回合 · a volta 次回合 · o finalista 决赛球队 · a decisão 决战 · a rodada 轮次。',
     'a ida = первый матч · a volta = ответный матч · o finalista = финалист · a decisão = решающий матч · a rodada = тур.'),
    ('你在巴西杯支持哪支球队？写两句寄来。',
     'За какую команду вы болеете в Кубке Бразилии? Напишите две фразы по-португальски и пришлите нам.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · Футбольная неделя'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · Упражнения страницы 4'),
    ('读第 4 版文章，选出正确答案。', 'Прочитайте статью на странице 4 и выберите правильный ответ.'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点',
     'Ответный матч «Атлетико Минейро» × «Гремио» — в субботу 7-го в 18h'),
    ('瓦斯科 × 帕尔梅拉斯次回合在周日 8 日 17 点，圣雅努阿里奥',
     'Ответный матч «Васко» × «Палмейрас» — в воскресенье 8-го в 17h, на «Сан-Жануарио»'),
    ('首回合在 11 月 1 日周日', 'Первые матчи были в воскресенье, 1 ноября'),
    ('第 34 轮周一到周五每天都有比赛', 'В 34-м туре матчи идут с понедельника по пятницу'),
    ('两回合总比分胜者进决赛', 'Победитель по сумме двух матчей выходит в финал'),
    ('finalista=进决赛的球队 b', 'finalista = команда, вышедшая в финал (b)'),
    ('ida=对决的第一场 c', 'ida = первый матч противостояния (c)'),
    ('volta=对决的第二场 a', 'volta = второй матч противостояния (a)'),
    ('rodada=一轮比赛 d', 'rodada = тур матчей (d)'),
    ('用括号里正确的比较形式填空。', 'Вставьте правильную сравнительную форму из скобок.'),
    ('次回合决定决赛名额：mais', 'Ответный матч решает финалистов: mais'),
    ('18 > 16：mais', '18 > 16: mais'),
    ('17 < 18：mais cedo', '17 < 18: mais cedo'),
    ('第 34 轮周一到周五都有比赛：mais', '34-й тур идёт с понедельника по пятницу: mais'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Дополните предложения в прошедшем времени (pretérito perfeito).'),
    ('ser 过去时复数：foram', 'ser, прошлое время, множественное число: foram'),
    ('receber 过去时 ele 形式：recebeu', 'receber, прошлое время, форма ele: recebeu'),
    ('começar 过去时 ela 形式：começou', 'começar, прошлое время, форма ela: começou'),
    ('chegar 过去时 eles 形式：chegaram', 'chegar, прошлое время, форма eles: chegaram'),
]

R56 = [
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · А вы?'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Ответы на странице 8 · Уровни перемешаны — ищите по номеру задания'),
    ('JOVENS · 青年', 'JOVENS · Молодёжь'),
    ('NÍVEL B1 · A reta final dos jovens · 冲刺周：年轻人的最后一周',
     'NÍVEL B1 · A reta final dos jovens · Последний рывок молодёжи'),
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）',
     '1. Confira o Cartão de Confirmação do Enem (проверьте карточку подтверждения Enem)'),
    ('2. Revise um pouco por dia, sem maratona（每天复习一点，不搞突击）',
     '2. Revise um pouco por dia, sem maratona (повторяйте понемногу каждый день, без зубрёжки)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）',
     '3. Durma bem na véspera da prova (хорошо выспитесь накануне экзамена)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）',
     '4. Separe documento e caneta preta no dia anterior (заранее приготовьте документ и чёрную ручку)'),
    ('5. Domingo 8: chegue antes das 12h（周日 8 日：12 点前到达）',
     '5. Domingo 8: chegue antes das 12h (в воскресенье 8-го: приходите до 12h)'),
    ('a reta final 最后冲刺 · a véspera 前夕 · a maratona 突击马拉松 · separar 准备好 · a cabeça 头脑、状态。',
     'a reta final = последний рывок · a véspera = канун · a maratona = ночная зубрёжка · separar = приготовить · a cabeça = голова, состояние.'),
    ('重要考试前一晚，你的计划是复习还是休息？写两句寄来。',
     'Накануне важного экзамена ваш план — повторять или отдыхать? Напишите две фразы по-португальски и пришлите нам.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · Упражнения страницы 5'),
    ('读第 5 版文章，选出正确答案。', 'Прочитайте статью на странице 5 и выберите правильный ответ.'),
    ('冲刺周在 11 月 8 日周日结束', 'Последний рывок заканчивается в воскресенье, 8 ноября'),
    ('每天复习一点', 'Повторяйте понемногу каждый день'),
    ('提前一天备好证件和黑笔', 'Заранее приготовьте документ и чёрную ручку'),
    ('第 2 天考自然科学与数学', 'День 2: естественные науки и математика'),
    ('11 月 3 日周二各州议会结束休会', 'Во вторник 3-го собрания штатов возвращаются с каникул'),
    ('用方框里的词填空。注意：有的词要变成复数。',
     'Заполните пропуски словами из рамки. Внимание: одно слово нужно поставить во множественное число.'),
    ('reta final = 最后冲刺阶段', 'reta final = последний рывок'),
    ('inscrito 配合复数：inscritos', 'inscrito во множественном числе: inscritos'),
    ('véspera = 前夕', 'véspera = канун'),
    ('maratona = 突击马拉松', 'maratona = ночная зубрёжка'),
    ('local = 地点', 'local = место'),
    ('separar 祈使式：separe', 'separar, повелительное наклонение: separe'),
    ('用将来时（futuro do presente）补全。', 'Дополните в будущем времени (futuro do presente).'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, будущее время, неправильная форма eles: farão'),
    ('mostrar 将来时：mostrará', 'mostrar, будущее время: mostrará'),
    ('sair 将来时复数：sairão', 'sair, будущее время, множественное число: sairão'),
    ('chegar 将来时：chegará', 'chegar, будущее время: chegará'),
    ('确认卡显示考试地点', 'Карточка подтверждения показывает место экзамена'),
    ('错：考前突击不是好计划，每天复习一点才好',
     'Неверно: зубрёжка накануне — плохой план, лучше повторять понемногу каждый день'),
    ('对：13:30 至 19:00', 'Верно: с 13:30 до 19:00'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · Разбор'),
    ('NÍVEL B2 · O Enem explicado · 高考详解', 'NÍVEL B2 · O Enem explicado · Enem: объяснение'),
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。',
     'os portões = ворота · a segunda chamada = пересдача, повторный вход · conferir = проверять · a correria = спешка.'),
    ('O DOMINGO 8 EM NÚMEROS · 11 月 8 日的数字 (horários oficiais do Inep)',
     'O DOMINGO 8 EM NÚMEROS · Цифры воскресенья 8-го (официальное время Inep)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · Упражнения страницы 6'),
    ('看上面两张图，选出正确答案。', 'Посмотрите на две диаграммы выше и выберите правильный ответ.'),
    ('大门开放 60 分钟', 'Ворота открыты 60 минут'),
    ('关门到开考之间等 30 分钟', 'Между закрытием и началом экзамена — 30 минут ожидания'),
    ('考试 330 分钟', 'Экзамен длится 330 минут'),
    ('中午到 19 点 = 7 小时', 'С полудня до 19h = 7 часов'),
    ('图表数字是 Inep 官方时间', 'Цифры диаграммы — официальное время Inep'),
    ('高考分 8 日和 15 日两个周日', 'Enem проходит в два воскресенья: 8-го и 15-го'),
    ('第 1 天考作文、语言与人文', 'День 1: сочинение, языки и гуманитарные науки'),
    ('13 点后到场不得入内', 'Пришедших после 13h не пускают'),
    ('根据句子意思，补全正确的动词形式。', 'Вставьте правильную форму глагола по смыслу предложения.'),
    ('将来时：começará', 'будущее время: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + будущее сослагательное: chegar'),
    ('现在时：fecham', 'настоящее время: fecham'),
    ('现在时：pede', 'настоящее время: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir',
     'Заполните пропуски словами из рамки: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = ворота'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = пересдача, повторный вход'),
    ('local = 地点', 'local = место'),
    ('祈使式：confira', 'повелительное наклонение: confira'),
]
R7 = [
    ('LÍNGUA · 语言', 'LÍNGUA · Язык'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具',
     'Três níveis, três ferramentas · Три уровня, три инструмента'),
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro',
     'Вопросы: que horas (который час) + глагол; onde fica спрашивает о месте; conferir неправилен в форме eu: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (неправильная форма)'),
    ('conferir：você → confere', 'conferir: você → confere'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('onde 问地点', 'onde спрашивает о месте'),
    ('讲一周的事用过去时（pretérito perfeito）；revisar 规则（revisei）；chegar/dormir 的过去时注意重音。',
     'Неделю рассказываем в pretérito perfeito; revisar правильный (revisei); chegar и dormir в прошлом времени — с ударением.'),
    ('revisar 过去时：revisei', 'revisar, прошлое время: revisei'),
    ('chegar 过去时：chegou', 'chegar, прошлое время: chegou'),
    ('dormir 过去时：dormiu', 'dormir, прошлое время: dormiu'),
    ('chegaram 是 chegar 的过去时复数', 'chegaram — прошлое время, множественное число, от chegar'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。',
     'После quando, se и quem будущее требует сослагательного наклонения: tiver, for, chegar (гипотезы о воскресенье).'),
    ('quem + 虚拟式将来：tiver', 'quem + будущее сослагательное: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + будущее сослагательное: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + будущее сослагательное от ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + будущее → будущее сослагательное for'),
    ('高考用黑笔，蓝笔不行。', 'Только чёрная ручка, синяя — нет.'),
    ('13 点关门，13:30 到就晚了。', 'В 13h ворота закрыты — поздно.'),
    ('考前一夜突击没用，睡好才记得住。', 'Без ночной зубрёжки — выспитесь.'),
    ('连休是 10 月 31 日到 11 月 2 日，共三天。', 'С 31 октября по 2 ноября — три дня.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · Частые ошибки'),
    ('feriadão = 连休长周末，共三天。', 'feriadão = длинные выходные, три дня.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · Слово недели'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！',
     'Пример редакции — не письмо. Присылайте письма: лучшие в VOL.3!'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）',
     'FRASES DA SEMANA · Фразы недели (дословно из статей номера)'),
    ('从连休到考试：高考周。', 'От длинных выходных — к экзамену: неделя Enem.'),
    ('许多人旅行、探亲、去墓园献花。', 'Многие путешествуют, навещают семью и несут цветы на кладбище.'),
    ('亡灵节是怀念的日子。', 'Финадос — день памяти.'),
    ('怀念是继续亲近的方式。', 'Помнить — значит оставаться рядом.'),
    ('每一分值一个名次，每一球值一个故事。', 'Каждое очко — место в таблице, каждый гол — история.'),
    ('睡得好，记得牢。', 'Хорошо выспишься — лучше запомнишь.'),
    ('先做容易的，再做难的。', 'Сначала лёгкие, потом трудные.'),
    ('核对确认卡、睡好、早到。', 'Проверьте карточку, выспитесь, приходите рано.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'A PRÓXIMA SEMANA · На следующей неделе (VOL.3)'),
]
R8 = [
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · Тест и ответы'),
    ('第 8 版 · A grande prova da semana + todas as respostas',
     'СТРАНИЦА 8 · Большой тест недели + все ответы'),
    ('第 1 天在 11 月 8 日', 'День 1 — 8 ноября'),
    ('13 点关门', 'Ворота закрываются в 13h'),
    ('13:30 开考', 'Экзамен начинается в 13:30'),
    ('亡灵节在 11 月 2 日', 'Финадос — 2 ноября'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'Ответный матч «Васко» × «Палмейрас» — 8-го'),
    ('连休共 3 天', 'Длинные выходные — всего 3 дня'),
    ('考试时长 5 个半小时', 'Экзамен длится пять с половиной часов'),
    ('第 2 天在 11 月 15 日', 'День 2 — 15 ноября'),
    ('连休从 10 月 31 日到 11 月 2 日', 'Длинные выходные — с 31 октября по 2 ноября'),
    ('确认卡是高考的文件', 'Карточка подтверждения — документ Enem'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场',
     'Ответный матч «Атлетико Минейро» × «Гремио» — на «Арене MRV»'),
    ('第 34 轮周一到周五都有比赛', 'В 34-м туре матчи идут с понедельника по пятницу'),
    ('亡灵节家人们带花', 'На Финадос семьи несут цветы'),
    ('万圣节在 10 月 31 日周六', 'Хэллоуин был в субботу, 31 октября'),
    ('330 是考试的分钟数', '330 — это минуты экзамена'),
    ('亡灵节又称诸圣灵魂日', 'Финадос называют также Днём усопших верных'),
    ('卢卡斯住在贝洛奥里藏特', 'Лукас живёт в Белу-Оризонти'),
    ('连休里他休息并每天复习一点', 'В выходные он отдыхает и повторяет понемногу каждый день'),
    ('前一晚他备好证件和黑笔、早睡', 'Накануне он готовит документ и чёрную ручку и рано ложится'),
    ('他 11 点到达考场', 'Он приходит на место экзамена в 11h'),
    ('时间词在前', 'Слово времени — первым'),
    ('主语 + 动词 + 宾语 + 地点', 'Подлежащее + глагол + дополнение + место'),
    ('疑问词组在句首', 'Вопросительное словосочетание — первым'),
    ('主语 + 动词 + 宾语', 'Подлежащее + глагол + дополнение'),
    ('11 月 8 日周日是高考的第一天。', 'Воскресенье, 8 ноября, — первый день Enem.'),
    ('对照第 6 版标题', 'См. заголовок страницы 6'),
    ('周日前核对确认卡。', 'Проверьте карточку подтверждения до воскресенья.'),
    ('Confira = 请核对', 'Confira = проверьте'),
    ('“连休是 10 月 31 日到 11 月 2 日。” → ___',
     '«Длинные выходные — с 31 октября по 2 ноября». → ___'),
    ('feriadão = 连休', 'feriadão = длинные выходные'),
    ('你到达时，请出示带照片的证件。 → ___', 'Когда вы придёте, покажите документ с фотографией. → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'будущее сослагательное chegar + повелительное apresente'),
    ('feriadão=连着周末的假期 b', 'feriadão = праздник, слившийся с выходными (b)'),
    ('portão=考场入口 d', 'portão = вход на место экзамена (d)'),
    ('reta final=考前最后一周 a', 'reta final = последняя неделя перед экзаменом (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c',
     'segunda chamada = повторный вход после закрытия (в Enem его нет) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = документ с фотографией'),
    ('seção = 考场分区（房间）', 'seção = экзаменационный сектор (аудитория)'),
    ('大门 13 点关闭', 'Ворота закрываются в 13h'),
    ('考试 13:30 开始', 'Экзамен начинается в 13:30'),
    ('obrigado = 谢谢', 'obrigado = спасибо'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。',
     'Задание без единственного правильного ответа; образец текста ({NWORDS} слова) — ниже.'),
    ('（开放题，范文如下）', '(открытое задание — образец ниже)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'Образец — в разделе H этой страницы ({NWORDS} слова)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可',
     'RESPOSTAS · Ответы — по страницам: ищите по номеру задания'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'К каждому ответу — короткое пояснение · ✓ — задание с образцом текста'),
    ('— PÁGINA {pg} —', '— СТРАНИЦА {pg} —'),
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

# ---------- 4. line-anchored: disc_cn -> disc_ru ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_ru')
t = sub(t, '编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。',
        'Примечание: настоящих писем и лучших текстов из VOL.1 нет. Пример остаётся, обещание — в VOL.3.', 1, 'content7.py')
save('content7.py', t)

# P7 page tags: core «Página N» -> W43 RU «Страница N» (furniture, 8 items)
t = load('content7.py')
assert t.count('"Página ') == 8, f"Página tags {t.count(chr(34)+'Página ')}"
t = t.replace('"Página ', '"Страница ')
save('content7.py', t)

# ---------- 4b. ROUND-2 geometry (measured round-1 overflow) ----------
# P7 col3 stack was 2056 -> quotes ran into the preview box (2404). Fixes:
# errs notes -> 1 line each (done in R7 above), word gloss -> 1 line (R7),
# label -> 2 lines, disc_ru -> 3 lines (both above), plus box pads + quote
# spacing below. All wrap()-verified before committing.
t = load('content7.py')
lines = t.split('\n')
for i, ln in enumerate(lines):
    if ln.startswith('wh = 62'):
        assert ln.rstrip().endswith('* 29 + 20'), ln
        lines[i] = ln.replace('* 29 + 20', '* 29 + 30')
    if ln.startswith('lh = 62'):
        assert ln.rstrip().endswith('* 29 + 35'), ln
        lines[i] = ln.replace('* 29 + 35', '* 29 + 25')
    if 'cyq = fy + 66' in ln:
        assert '* 128' in ln, ln
        lines[i] = ln.replace('* 128', '* 100')
t = '\n'.join(lines)
save('content7.py', t)

# P1 serif line: RU text at 40pt overflows the page (2055px) -> 36pt (1849px,
# ink 50..1900, clear of the inner frame at 40); full text kept, EN used 38pt
# for its shorter English line.
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE", 36, "serif", True, INK, anchor="middle")',
    'content12.py')
save('content12.py', t)

# P8 keys overflowed past bottom 2552 (RU notes longer) -> 13pt/1.12 (EN precedent)
t = load('content8.py')
t = sub(t, 'af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)',
        'af.para(txt, 13, lh=1.12, gap=0.5, split=False)', 1, 'content8.py')
save('content8.py', t)

# ---------- 5. verify: zero CJK in build sources ----------
for fn in ['bslib4.py', 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py']:
    t = load(fn)
    hits = CJK.findall(t)
    assert not hits, f'{fn}: {len(hits)} CJK chars remain, e.g. {hits[:10]}'
    print(f'{fn}: CJK 0 OK')
print('TRANSFORM COMPLETE')
