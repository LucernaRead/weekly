# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x RU fan-out transform for W46 VOL.3.

Run inside the already-copied build dir. Every replacement is an exact
literal match (longest strings first); missing literals warn, and the
final pass asserts ZERO CJK chars remain in the build sources.
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + page tags are never touched.
P1 subtitle (330) and badge (372) lines are replaced whole (size/color).
Subtitle size 30pt is measured (36pt overflows the page frame).
Badge uses GREY non-bold per the W45 RU precedent.
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

# ---------- 0. OUT / BASE repoint + print PDF name ----------
for fn in FILES:
    t = load(fn)
    if 'weekly-report-w46-pt-core' in t:
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-ru')
        save(fn, t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.3 · ТЕКСТЫ НА ПОРТУГАЛЬСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Страница {n} из {total}"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Пояснение — " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. P1 masthead lines (whole-line) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "ПОРТУГАЛЬСКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE", 30, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "ТЕКСТЫ НА ПОРТУГАЛЬСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 19, "sans", False, GREY, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 3. type / instr labels ----------
INSTR = [
    ('instr="造句"', 'instr="Составьте предложение"'),
    ('instr="翻译"', 'instr="Переведите"'),
    ('instr="判断"', 'instr="Верно или неверно?"'),
    ('instr="写作"', 'instr="Напишите"'),
    ('instr="填空"', 'instr="Заполните"'),
    ('instr="把词和释义配对"', 'instr="Соедините"'),
]
TYP = [
    ('"完成句子"', '"Дополните предложение"'),
    ('"词汇配对"', '"Соедините слова"'),
    ('"判断对错"', '"Верно или неверно"'),
    ('"完形单选"', '"Текст с пропусками"'),
    ('"单选"', '"Выбор ответа"'),
    ('"造句"', '"Составление предложений"'),
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
    save(fn, t)

# ---------- 4. content replacements (global table, longest-first) ----------
REPL = [
    # bands
    ('NÍVEL A2 · Prova e feriado no mesmo domingo', 'УРОВЕНЬ A2 · Экзамен и праздник в один день'),
    ('A2 → B1 · Proclamação da República: 137 anos · 共和国宣言 137 周年', 'A2 → B1 · Proclamação da República: 137 лет'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'УРОВЕНЬ B1 · Футбольная неделя'),
    ('NÍVEL B1 · A última semana dos jovens · 最后一周：年轻人的冲刺', 'УРОВЕНЬ B1 · Последняя неделя молодёжи'),
    ('NÍVEL B2 · O segundo domingo explicado · 第二个周日详解', 'УРОВЕНЬ B2 · Второе воскресенье: объяснение'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', 'Três níveis, três ferramentas · Три уровня, три инструмента'),
    ('第 8 版 · A grande prova da semana + todas as respostas', 'СТРАНИЦА 8 · Большой тест недели + все ответы'),
    # top strip / kickers
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · ТО, ЧТО ЧИТАЕТ БРАЗИЛИЯ'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · ГЛАВНАЯ НОВОСТЬ'),
    ('VIDA · 生活', 'VIDA · ЖИЗНЬ'),
    ('CULTURA · 文化', 'CULTURA · КУЛЬТУРА'),
    ('ESPORTE · 体育', 'ESPORTE · СПОРТ'),
    ('JOVENS · 青年', 'JOVENS · МОЛОДЁЖЬ'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · ПОГРУЖЕНИЕ'),
    ('LÍNGUA · 语言', 'LÍNGUA · ЯЗЫК'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · ТЕСТ И ОТВЕТЫ'),
    # P1
    ('高考第二天', 'ENEM, ДЕНЬ 2'),
    ('11 月 15 日第二场考试 · 共和国宣言日假期', '15 ноября: второй день экзамена · праздник Провозглашения Республики'),
    ('讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。', 'Ключевые слова | a proclamação = провозглашение · o feriado = праздник · a natureza = естественные науки · a matemática = математика.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · В ЦИФРАХ'),
    ('12h — os portões abrem no domingo 15（周日 12 点开门）', '12h — os portões abrem no domingo 15 (воскресенье: вход с 12:00)'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham (13:00: ворота закрываются, опоздавших не пускают)'),
    ('13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）', '13h30–18h30 — a prova do dia 15 (экзамен 15-го, с 13:30 до 18:30)'),
    ('90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）', '90 — as questões do dia 15: 45 + 45 (90 вопросов: 45 + 45)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · ТЕПЕРЬ ТЫ'),
    ('proclamação = 宣布（共和国宣言）', 'proclamação = провозглашение (Республики)'),
    ('proclamação = 宣布（共和国宣言）。', 'proclamação = провозглашение (Республики).'),
    ('feriado = 假日', 'feriado = праздник'),
    ('portões = 大门（考场大门）', 'portões = ворота (экзаменационного центра)'),
    ('18h30 结束', 'заканчивается в 18:30'),
    ('90 道题', '90 вопросов'),
    ('fazer 现在时 eles 形式：fazem', 'fazer, настоящее время, форма eles: fazem'),
    ('迟到不得入内：13 点后关门', 'После 13:00 уже не войти.'),
    # .text.md variant of the line above: the export source carries a trailing 。 which the bare entry leaves behind (F-2).
    ('迟到不得入内：13 点后关门。', 'После 13:00 уже не войти.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · В этом выпуске'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · Коротко'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · МОЛНИЕНОСНЫЙ ТЕСТ'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Прочитай первую полосу и выбери · Ответы на странице 8'),
    ('共和国宣言日在 11 月 15 日', 'День Провозглашения Республики — 15 ноября'),
    ('13 点关门', 'Закрытие в 13:00'),
    ('第 2 天考自然科学与数学', 'День 2: естественные науки и математика'),
    ('18:30 结束', 'Конец в 18:30'),
    # P2
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · ЗАПОМНИ'),
    ('a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。', 'a proclamação = провозглашение · o feriado = праздник · a natureza = естественные науки · a matemática = математика · conferir = проверить · a escala = расписание.'),
    ('在你的国家，落在周日的假日会在周一补休吗？写两句寄来。', 'В твоей стране праздник, выпавший на воскресенье, переносится на понедельник? Напиши два предложения и пришли нам.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · А ТЫ?'),
    ('OS HORÁRIOS DO DOMINGO 15 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 15 · РАСПИСАНИЕ НА ВОСКРЕСЕНЬЕ, 15-Е'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · Одна страна, несколько часовых поясов'),
    ('周日 12 点开门', 'В воскресенье вход с 12:00'),
    ('13:30 开考', 'Экзамен начинается в 13:30'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · УПРАЖНЕНИЯ, СТРАНИЦА 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Ответы на странице 8 · Уровни перемешаны — ищи по номеру'),
    ('读第 2 版文章，选出正确答案。', 'Прочитай страницу 2 и выбери правильный ответ.'),
    ('假日落在周日，周一不补休', 'Праздник выпадает на воскресенье, в понедельник выходного нет'),
    # P7-clinic/.text.md variant of the line above: the source carries a trailing 。 (F-2/F-3).
    ('假日落在周日，周一不补休。', 'Праздник выпадает на воскресенье, в понедельник выходного нет.'),
    ('确认卡显示考试地点', 'Карта подтверждения показывает место экзамена'),
    ('巴西没有夏令时，钟表不动', 'В Бразилии нет летнего времени: часы не переводят'),
    ('补全动词的现在时形式。', 'Дополни форму глагола в настоящем времени.'),
    ('用第 1、2 版的数字填空。', 'Заполни числами со страниц 1 и 2.'),
    ('12 点到 13 点 = 1 小时', 'С 12:00 до 13:00 = 1 час'),
    ('13:30 至 18:30 = 5 小时', 'С 13:30 до 18:30 = 5 часов'),
    ('5×60 = 300 分钟', '5×60 = 300 минут'),
    ('proclamação=宣布一个变化 b', 'proclamação = объявить изменение (b)'),
    ('feriado=法律规定的休息日 c', 'feriado = установленный законом выходной (c)'),
    ('natureza=生命、物理与化学的科学 d', 'natureza = наука о жизни, физике и химии (d)'),
    ('matemática=数字与图形的科学 a', 'matemática = наука о числах и фигурах (a)'),
    ('把词和释义配对', 'Соедини слова и значения'),
]
REPL += [
    # P3
    ('a monarquia 君主制 · a república 共和国 · o marechal 元帅 · o exílio 流亡 · o governo 政府 · a lei 法律。', 'a monarquia = монархия · a república = республика · o marechal = маршал · o exílio = изгнание · o governo = правительство · a lei = закон.'),
    ('在你的国家，有纪念共和国建立的假日吗？写两句寄来。', 'Есть ли в твоей стране праздник в честь основания республики? Напиши два предложения и пришли нам.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · УПРАЖНЕНИЯ, СТРАНИЦА 3'),
    ('读第 3 版文章，选出正确答案。', 'Прочитай страницу 3 и выбери правильный ответ.'),
    ('共和国宣言在 1889 年 11 月 15 日', 'Провозглашение Республики было 15 ноября 1889 года'),
    ('德奥多罗成为巴西第一任总统', 'Деодору стал первым президентом Бразилии'),
    ('全国性假日，任何城市都不能改为工作日', 'Общенациональный праздник, который ни один город не может сделать рабочим днём'),
    ('2026 年假日落在周日', 'В 2026 году праздник выпадает на воскресенье'),
    ('共和国里总统由选举产生、任期有限', 'В республике президента избирают, и власть ограничена сроком'),
    ('用方框里的词填空。', 'Заполни словами из рамки.'),
    ('monarquia = 君主制', 'monarquia = монархия'),
    ('república = 共和国', 'república = республика'),
    ('marechal = 元帅', 'marechal = маршал'),
    ('exílio = 流亡', 'exílio = изгнание'),
    ('governo = 政府', 'governo = правительство'),
    ('lei = 法律', 'lei = закон'),
    ('用过去时（pretérito perfeito）补全。', 'Дополни в прошедшем времени (pretérito perfeito).'),
    ('tomar 过去时 elas 形式：tomaram', 'tomar, прошедшее время, форма elas: tomaram'),
    ('acabar 过去时 ela 形式：acabou', 'acabar, прошедшее время, форма ela: acabou'),
    ('ser 过去时 ele 形式：foi', 'ser, прошедшее время, форма ele: foi'),
    ('assumir 过去时 ele 形式：assumiu', 'assumir, прошедшее время, форма ele: assumiu'),
    ('把词组成正确的句子。', 'Поставь слова в правильном порядке.'),
    ('主语 + é + 表语', 'Подлежащее + é + сказуемое'),
    ('主语 + 动词 + 表语', 'Подлежащее + глагол + сказуемое'),
    ('主语 + 动词 + 宾语 + 时间', 'Подлежащее + глагол + дополнение + время'),
    # P4
    ('a ida 首回合 · a volta 次回合 · o gol 进球 · o pênalti 点球 · a pausa 休整期 · o amistoso 友谊赛。', 'a ida = первый матч · a volta = ответный матч · o gol = гол · o pênalti = пенальти · a pausa = перерыв · o amistoso = товарищеский матч.'),
    ('你在巴西杯支持哪支球队？谁能进决赛？写两句寄来。', 'За какую команду ты болеешь в Кубке Бразилии, и кто выйдет в финал? Напиши два предложения и пришли нам.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · ФУТБОЛЬНАЯ НЕДЕЛЯ'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · УПРАЖНЕНИЯ, СТРАНИЦА 4'),
    ('读第 4 版文章，选出正确答案。', 'Прочитай страницу 4 и выбери правильный ответ.'),
    ('首回合格雷米奥 2 比 0 战胜米内罗竞技', 'В первом матче Гремио обыграл Атлетико-МГ со счётом 2:0'),
    ('帕尔梅拉斯 1 比 0 战胜瓦斯科，毛里西奥进球', 'Палмейрас обыграл Васко 1:0, гол забил Маурисио'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', 'Ответный матч Атлетико-МГ × Гремио — в субботу 7-го в 18:00'),
    ('决赛 12 月 6 日单场，在马内·加林查', 'Финал: один матч, 6 декабря, на стадионе Мане Гарринча'),
    ('第 35 轮本周只有一场：米拉索尔 × 米内罗竞技', 'В 35-м туре на этой неделе только один матч: Мирассол × Атлетико-МГ'),
    ('gol=射入球网的得分 b', 'gol = гол, забитый в ворота (b)'),
    ('ida=对决的第一场 d', 'ida = первый матч противостояния (d)'),
    ('volta=对决的第二场 a', 'volta = второй матч противостояния (a)'),
    ('pênalti=十一米点的罚球 c', 'pênalti = удар с одиннадцатиметровой отметки (c)'),
    ('用括号里正确的比较形式填空。', 'Заполни правильную сравнительную форму из скобок.'),
    ('5 小时 < 5.5 小时：menos', '5 часов < 5,5 часа: menos'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Дополни предложения в прошедшем времени (pretérito perfeito).'),
    ('vencer 过去时 ele 形式：venceu', 'vencer, прошедшее время, форма ele: venceu'),
    ('marcar 过去时 eles 形式：marcaram', 'marcar, прошедшее время, форма eles: marcaram'),
    ('marcar 过去时 ele 形式：marcou', 'marcar, прошедшее время, форма ele: marcou'),
    ('convocar 过去时 ele 形式：convocou', 'convocar, прошедшее время, форма ele: convocou'),
    ('ser 过去时复数：foram', 'ser, прошедшее время, множественное число: foram'),
    # P5
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem (проверь карту подтверждения Enem)'),
    ('2. Revise um pouco por dia: Natureza e Matemática（每天复习一点：自然科学与数学）', '2. Revise um pouco por dia: Natureza e Matemática (повторяй понемногу каждый день: естественные науки и математику)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova (хорошо выспись накануне экзамена)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior (приготовь документ и чёрную ручку накануне)'),
    ('5. Domingo 15: chegue antes das 12h（周日 15 日：12 点前到达）', '5. Domingo 15: chegue antes das 12h (воскресенье 15-го: приходи до 12:00)'),
    ('a natureza 自然科学 · a matemática 数学 · a maratona 突击马拉松 · a véspera 前夕 · comparar 比较价格 · a cabeça 头脑、状态。', 'a natureza = естественные науки · a matemática = математика · a maratona = марафон повторения · a véspera = канун · comparar = сравнивать цены · a cabeça = голова, состояние.'),
    ('重要考试前一晚，你是复习到很晚还是早睡？写两句寄来。', 'Накануне важного экзамена: ты повторяешь допоздна или ложишься рано? Напиши два предложения и пришли нам.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · УПРАЖНЕНИЯ, СТРАНИЦА 5'),
    ('读第 5 版文章，选出正确答案。', 'Прочитай страницу 5 и выбери правильный ответ.'),
    ('最后一周在 11 月 15 日周日结束', 'Последняя неделя заканчивается в воскресенье 15 ноября'),
    ('每天复习一点', 'Повторять понемногу каждый день'),
    ('提前一天备好证件和黑笔', 'Приготовить документ и чёрную ручку накануне'),
    ('黑五在 11 月 27 日', 'Чёрная пятница — 27 ноября'),
    ('11 月 14 日周六巴西 × 日本 7:15', 'Суббота 14-го: Бразилия × Япония в 7:15'),
    ('用方框里的词填空。注意：有的词要变成复数。', 'Заполни словами из рамки. Внимание: одно слово — во множественном числе.'),
    ('última semana = 最后一周', 'última semana = последняя неделя'),
    ('inscrito 配合复数：inscritos', 'inscrito согласуется во множественном числе: inscritos'),
    ('véspera = 前夕', 'véspera = канун'),
    ('maratona = 突击马拉松', 'maratona = марафон повторения'),
    ('local = 地点', 'local = место'),
    ('separar 祈使式：separe', 'separar, повелительное наклонение: separe'),
    ('用将来时（futuro do presente）补全。', 'Дополни в будущем времени (futuro do presente).'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, будущее время, неправильная форма eles: farão'),
    ('mostrar 将来时：mostrará', 'mostrar, будущее время: mostrará'),
    ('sair 将来时复数：sairão', 'sair, будущее время, множественное число: sairão'),
    ('chegar 将来时：chegará', 'chegar, будущее время: chegará'),
    ('错：考前突击不是好计划，每天复习一点才好', 'Неверно: зубрёжка накануне — не план, лучше понемногу каждый день'),
    ('对：13:30 至 18:30', 'Верно: с 13:30 до 18:30'),
    # P6
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões = ворота · a segunda chamada = вторая попытка, второй вход · conferir = проверить · a correria = спешка.'),
    ('O DOMINGO 15 EM NÚMEROS · 11 月 15 日的数字 (horários oficiais do Inep)', 'O DOMINGO 15 EM NÚMEROS · ЦИФРЫ 15 НОЯБРЯ (официальное время Inep)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · УПРАЖНЕНИЯ, СТРАНИЦА 6'),
    ('看上面两张图，选出正确答案。', 'Посмотри на два графика выше и выбери правильный ответ.'),
    ('大门开放 60 分钟', 'Ворота открыты 60 минут'),
    ('关门到开考之间等 30 分钟', 'Ожидание между закрытием и экзаменом — 30 минут'),
    ('考试 300 分钟', 'Экзамен длится 300 минут'),
    ('中午到 18:30 = 6 个半小时', 'От полудня до 18:30 = шесть с половиной часов'),
    ('图表数字是 Inep 官方时间', 'Цифры графика — официальное время Inep'),
    ('高考分 8 日和 15 日两个周日', 'Enem проходит в два воскресенья: 8-го и 15-го'),
    ('13 点后到场不得入内', 'После 13:00 уже не войти'),
    ('根据句子意思，补全正确的动词形式。', 'Дополни правильную форму глагола для каждого предложения.'),
    ('将来时：começará', 'Будущее время: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + будущее сослагательного наклонения: chegar'),
    ('现在时：fecham', 'Настоящее время: fecham'),
    ('现在时：pede', 'Настоящее время: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', 'Заполни словами из рамки: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = ворота'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = вторая попытка, второй вход'),
    ('祈使式：confira', 'Повелительное наклонение: confira'),
    # P7
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', 'Вопросы: que horas (во сколько) + глагол; onde fica спрашивает, где место; conferir неправилен в форме eu: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (неправильный)'),
    ('onde 问地点', 'onde спрашивает о месте'),
    ('讲一周的事用过去时（pretérito perfeito）；vencer 规则（venceu）；marcar/chegar/dormir 的过去时注意重音。', 'Чтобы рассказать о неделе, используем прошедшее время (pretérito perfeito); vencer правильный (venceu); следи за ударением в прошедшем времени marcar, chegar и dormir.'),
    ('vencer 过去时：venceu', 'vencer, прошедшее время: venceu'),
    ('marcar 过去时：marcou', 'marcar, прошедшее время: marcou'),
    ('chegar 过去时：chegou', 'chegar, прошедшее время: chegou'),
    ('venceram 是 vencer 的过去时复数', 'venceram — прошедшее время, множественное число, от vencer'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'После quando, se и quem — будущее сослагательного наклонения: tiver, for, chegar — грамматика воскресных гипотез.'),
    ('quem + 虚拟式将来：tiver', 'quem + будущее сослагательного наклонения: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + будущее сослагательного наклонения: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + будущее сослагательного наклонения от ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + будущее → будущее сослагательного наклонения for'),
    ('高考用黑笔，蓝笔不行。', 'Только чёрная ручка — синяя не подойдёт.'),
    ('13 点关门，13:30 到就晚了。', 'Закрытие в 13:00 — в 13:30 уже поздно.'),
    ('15 日考试 18:30 结束，19 点是 8 日的时间。', '15-го экзамен заканчивается в 18:30; 19:00 — это 8-е.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · Частые ошибки'),
    ('proclamação = 宣布；1889 年君主制结束、共和国开始。', 'proclamação = провозглашение; в 1889 году монархия закончилась, а республика началась.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · Слово недели'),
    ('编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。', 'Примечание: настоящих писем и лучших текстов из VOL.2 не пришло. Пример остаётся, обещание — в VOL.4.'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', 'Пример редакции — не настоящее письмо. Присылайте письма!'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · ФРАЗЫ НЕДЕЛИ (дословно из этого номера)'),
    ('两个周日、一个假日：巴西迎来高考第二天。', 'Два воскресенья, один праздник: Бразилия сдаёт второй день Enem.'),
    ('考试和假日在同一天到来。', 'Экзамен и праздник приходят в один день.'),
    ('假日不改变时钟。', 'Праздник не переводит часы.'),
    ('君主制结束了。', 'Монархия закончилась.'),
    ('谁能进巴西杯决赛？', 'Кто выйдет в финал Кубка Бразилии?'),
    ('睡得好，记得牢。', 'Хорошо спишь — лучше помнишь.'),
    ('先做容易的，再做难的。', 'Сначала лёгкие, потом трудные.'),
    ('核对确认卡、睡好、早到。', 'Проверь карту, выспись, приходи рано.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.4)', 'A PRÓXIMA SEMANA · НА СЛЕДУЮЩЕЙ НЕДЕЛЕ (VOL.4)'),
    # P8
    ('第 2 天在 11 月 15 日', 'День 2 — 15 ноября'),
    ('第 1 天在 11 月 8 日', 'День 1 — 8 ноября'),
    ('确认卡是高考的文件', 'Карта подтверждения относится к Enem'),
    ('共和国宣言日在 11 月 15 日', 'День Провозглашения Республики — 15 ноября'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'Ответный матч Васко × Палмейрас — 8-го'),
    ('第二天共 90 道题', 'Во второй день всего 90 вопросов'),
    ('考试时长 5 小时', 'Экзамен длится 5 часов'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', 'Ответный матч Атлетико-МГ × Гремио — на Арене MRV'),
    ('第 35 轮本周只有一场，在 14 日', 'В 35-м туре на этой неделе только один матч, 14-го'),
    ('共和国宣言在 1889 年', 'Провозглашение Республики было в 1889 году'),
    ('11.11 是促销日', '11.11 — день распродаж'),
    ('300 是考试的分钟数', '300 — длительность экзамена в минутах'),
    ('德奥多罗是第一任总统', 'Деодору был первым президентом'),
    ('玛丽娜住在圣保罗', 'Марина живёт в Сан-Паулу'),
    ('她每天复习一点自然科学', 'Она повторяет понемногу естественные науки каждый день'),
    ('前一晚她备好证件和黑笔、早睡', 'Накануне она готовит документ и чёрную ручку и ложится рано'),
    ('她 11:30 到达考场', 'Она приходит в экзаменационный центр в 11:30'),
    ('时间词在前', 'Слово времени — впереди'),
    ('主语 + 动词 + 宾语 + 地点', 'Подлежащее + глагол + дополнение + место'),
    ('疑问词组在句首', 'Вопросительная группа — в начале'),
    ('主语 + 动词 + 宾语', 'Подлежащее + глагол + дополнение'),
    ('11 月 15 日周日是高考的第二天。', 'Воскресенье 15 ноября — второй день Enem.'),
    ('对照第 6 版标题', 'Смотри заголовок на странице 6'),
    ('周日前核对确认卡。', 'Проверь карту до воскресенья.'),
    ('Confira = 请核对', 'Confira = проверь'),
    ('“假日落在周日。” → ___', '«Праздник выпадает на воскресенье.» → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'Будущее сослагательного наклонения chegar + повелительное наклонение apresente'),
    ('你到达时，请出示带照片的证件。 → ___', 'Когда придёшь, покажи документ с фото. → ___'),
    ('proclamação=宣布一个变化 b', 'proclamação = объявить изменение (b)'),
    ('portão=考场入口 d', 'portão = вход в экзаменационный центр (d)'),
    ('república=1889 年后的国家形式 a', 'república = форма государства после 1889 года (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada = повторный вход после закрытия (в Enem такого нет) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = документ с фото'),
    ('seção = 考场分区（房间）', 'seção = экзаменационная комната (секция)'),
    ('大门 13 点关闭', 'Ворота закрываются в 13:00'),
    ('考试 18:30 结束', 'Экзамен заканчивается в 18:30'),
    ('obrigado = 谢谢', 'obrigado = спасибо'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', 'Письменное задание (без единственного ответа); образец текста ({NWORDS} слов) ниже.'),
    ('（开放题，范文如下）', '(открытое задание — образец ниже)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'Образец — в разделе H этой страницы ({NWORDS} слов)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · ОТВЕТЫ — по страницам; найди свой номер'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'Краткая заметка к каждому ответу · ✓ = письменное задание'),
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

# ---------- 5. disclosure rename + layout tweaks (Latin/RU precedent) ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_ru')
old_wh = 'len(wrap("proclamação = провозглашение; в 1889 году монархия закончилась, а республика началась.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box pad line not found'
t = t.replace(old_wh, 'len(wrap("proclamação = провозглашение; в 1889 году монархия закончилась, а республика началась.", "sans", False, 20, CW - 44)) * 29 + 30')
assert t.count(')) * 29 + 35') == 1, 'letters-box pad line not found'
t = t.replace(')) * 29 + 35', ')) * 29 + 22')
t = line_replace(t, 'fy = max(1712,', 'fy = max(1712, ly + lh + 14)', 'content7.py')
t = line_replace(t, 'cyq = fy + 66', '    cyq = fy + 66 + (i % 4) * 88', 'content7.py')
save('content7.py', t)

t = load('content8.py')
t = line_replace(t, 'af.para(txt, 13.5',
    '        af.para(txt, 13, lh=1.12, gap=0.5, split=False)',
    'content8.py')
save('content8.py', t)

t = load('content12.py')
old_box = '    ("90 — as questões do dia 15: 45 + 45 (90 вопросов: 45 + 45)", "serif", False, INK, 20, 1.35),\n])'
assert t.count(old_box) == 1, 'numbers box close not found'
t = t.replace(old_box, old_box[:-2] + '], tsize=20)')
save('content12.py', t)

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
