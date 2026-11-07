# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x ES fan-out transform for W45 VOL.2.

Copies nothing: run this inside the already-copied build dir. Every
replacement is an exact literal match with an asserted occurrence count
(longest strings first where one contains another), except line-anchored
replacements (P1 edition/badge lines, P7 B2 bridge line, numbers-box
tsize, P8 key size). After the pass, bslib4.py + content*.py must contain
ZERO CJK chars. Frozen Portuguese text, the P7 example letter (lt), the
PT disclosure (disc_pt) and the P7 quote strings + 'Página' tags are
never touched. Furniture follows the shipped W43 PT x ES edition
(files/weekly-report-pt-es + its build): badge BRICK 19pt bold in the
strapline slot, footer SEMANARIO PORTUGUÉS VOL.2, page line
'Página N de 8', gloss prefix 'Nota — '. P8 keeps the W45 core's dash
style (same as the W45 PT x EN sibling); the W43 paren style belonged to
the W43 core's apparatus and is NOT carried over.
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
        t = sub(t, 'weekly-report-w45-pt-core', 'weekly-report-w45-pt-es', fn=fn)
        save(fn, t)

# render.py PDF names: W43 pattern Lucerna-VOLn-ES
t = load('render.py')
t = sub(t, 'A-Lucerna-VOL2.pdf', 'Lucerna-VOL2-ES.pdf', 1, 'render.py')
t = sub(t, 'A-Lucerna-VOL2-web.pdf', 'Lucerna-VOL2-ES-web.pdf', 1, 'render.py')
save('render.py', t)

# ---------- 1. bslib4 furniture (W43 PT x ES, VOL.2) ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.2 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · SEMANARIO PORTUGUÉS VOL.2 · TEXTO EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL', 1, 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"', 1, 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Nota — " + s', 1, 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. type / instr labels (instr first, then bare typ) ----------
INSTR = [
    ('instr="造句"', 'instr="Forma la frase"'),
    ('instr="翻译"', 'instr="Traduce"'),
    ('instr="判断"', 'instr="¿Verdadero o falso?"'),
    ('instr="写作"', 'instr="Escribe"'),
    ('instr="填空"', 'instr="Completa"'),
    ('instr="把词和释义配对"', 'instr="Relaciona"'),
]
TYP = [
    ('"完成句子"', '"Completa la frase"'),
    ('"词汇配对"', '"Emparejar vocabulario"'),
    ('"判断对错"', '"Verdadero o falso"'),
    ('"完形单选"', '"Cloze"'),
    ('"单选"', '"Opción múltiple"'),
    ('"造句"', '"Construir frases"'),
    ('"翻译"', '"Traducción"'),
    ('"写作"', '"Escritura"'),
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
     'TODA SEMANA EM PORTUGUÊS · CADA SEMANA · EL PORTUGUÉS QUE LEE BRASIL'),
    ('葡 萄 牙 语 周 报 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE',
     'SEMANARIO EN PORTUGUÉS · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE'),
    ('11 月 2 日亡灵节连休 · 11 月 8 日高考第一天', '2 nov: puente de Finados · 8 nov: día 1 del Enem'),
    ('全国高考周', 'SEMANA DEL ENEM'),
    ('讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。',
     'Palabras clave | feriadão = el puente festivo · o portão = la puerta · a redação = la redacción · revisar = repasar.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · EN CIFRAS'),
    ('12h — os portões abrem no domingo 8（周日 12 点开门）',
     '12h — os portões abrem no domingo 8 (el domingo, apertura a las 12h)'),
    ('13h — os portões fecham（13 点关门，过时不入）',
     '13h — os portões fecham (a las 13h cierran; quien llegue tarde no entra)'),
    ('13h30–19h — a prova do dia 8（考试 13:30 至 19:00）',
     '13h30–19h — a prova do dia 8 (el examen, de 13:30 a 19:00)'),
    ('5h30 — a duração da prova do dia 8（考试时长 5 小时半）',
     '5h30 — a duração da prova do dia 8 (el examen dura cinco horas y media)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · AHORA TÚ'),
    ('feriadão = 连休长周末', 'feriadão = el puente festivo'),
    ('portões = 大门（考场大门）', 'portões = las puertas (las del lugar del examen)'),
    ('redação = 作文', 'redação = la redacción'),
    ('13h30 开考（巴西利亚时间）', '13h30: el examen empieza (hora de Brasilia)'),
    ('19h 结束', '19h: termina'),
    ('revisar 现在时 eles 形式：revisam', 'revisar, presente, forma eles: revisam'),
    ('迟到不得入内：13 点后关门', 'Quien llegue tarde no entra'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · EN ESTA EDICIÓN'),
    ('“连休”：假期连着周末，一共三天。', '«Feriadão»: un festivo junto al fin de semana.'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · BREVE'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · QUIZ RÁPIDO'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lee la portada y elige la correcta · Respuestas en la página 8'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · TITULAR'),
    ('连休从 10 月 31 日到 11 月 2 日', 'El puente festivo va del 31 de octubre al 2 de noviembre'),
    ('13 点关门', 'Cierre a las 13h'),
    ('第 1 天考作文、语言与人文', 'El día 1 es redacción, lenguas y humanidades'),
    ('次回合在 7 日和 8 日', 'Los partidos de vuelta son el 7 y el 8'),
    ('VIDA · 生活', 'VIDA · VIDA DIARIA'),
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · LA REGLA'),
    ('o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。',
     'o feriadão = el puente festivo · o cemitério = el cementerio · a vela = la vela · o crisântemo = el crisantemo · a missa = la misa · conferir = comprobar.'),
    ('在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。',
     '¿En tu país hay un día para recordar a los difuntos? ¿Qué hacen las familias ese día? Escribe dos frases en portugués y envíanoslas.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · CUÉNTANOS'),
    ('OS HORÁRIOS DO DOMINGO 8 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 8 · HORARIOS DEL DOMINGO 8'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · Un país, varios relojes'),
    ('周日 12 点开门', 'Domingo, apertura a las 12h'),
    ('13:30 开考', 'Empieza a las 13:30'),
    ('19:00 结束', 'Termina a las 19:00'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · EJERCICIOS DE LA PÁGINA 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respuestas en la página 8 · Los niveles se mezclan: busca por número'),
    ('读第 2 版文章，选出正确答案。', 'Lee el artículo de la página 2 y elige la respuesta correcta.'),
    ('亡灵节家人们去墓园献花', 'En Finados, las familias van al cementerio a llevar flores'),
    ('确认卡显示考试地点', 'La tarjeta de confirmación muestra el lugar del examen'),
    ('巴西没有夏令时，钟表不动', 'Brasil no tiene horario de verano: los relojes no cambian'),
    ('补全动词的现在时形式。', 'Completa con la forma del presente del verbo.'),
    ('conferir：ele → confere', 'conferir: ele → confere'),
    ('abrir：ele → abre', 'abrir: ele → abre'),
    ('levar：nós → levamos', 'levar: nós → levamos'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('ser 现在时 ela 形式：é', 'ser, presente, forma ela: é'),
    ('用第 1、2 版的数字填空。', 'Completa con los números de las páginas 1 y 2.'),
    ('12 点到 13 点 = 1 小时', 'De 12h a 13h = 1 hora'),
    ('13:30 至 19:00 = 5 个半小时', 'De 13:30 a 19:00 = cinco horas y media'),
    ('5×60 + 30 = 330 分钟', '5×60 + 30 = 330 minutos'),
    ('31 日、1 日、2 日 = 3 天', '31, 1 y 2 = 3 días'),
    ('feriadão=连着周末的假期 c', 'feriadão = un festivo junto al fin de semana: c'),
    ('cemitério=墓碑所在的地方 b', 'cemitério = donde están las tumbas: b'),
    ('vela=点亮纪念的物品 d', 'vela = el objeto que se enciende en memoria: d'),
    ('crisântemo=亡灵节带去的花 a', 'crisântemo = la flor que se lleva en Finados: a'),
]
R34 = [
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · CUÉNTANOS'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respuestas en la página 8 · Los niveles se mezclan: busca por número'),
    ('CULTURA · 文化', 'CULTURA · CULTURA'),
    ('A2 → B1 · Finados: o dia da memória · 亡灵节：怀念的日子',
     'A2 → B1 · Finados: o dia da memória · Finados: el día de la memoria'),
    ('o túmulo 墓碑 · a flor 花 · acender 点燃 · rezar 祈祷 · o silêncio 寂静 · a lembrança 怀念。',
     'o túmulo = la tumba · a flor = la flor · acender = encender · rezar = rezar · o silêncio = el silencio · a lembrança = el recuerdo.'),
    ('在你的文化里，人们怎样怀念逝者？写两句寄来。',
     'En tu cultura, ¿cómo se recuerda a los difuntos? Escribe dos frases en portugués y envíanoslas.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · EJERCICIOS DE LA PÁGINA 3'),
    ('读第 3 版文章，选出正确答案。', 'Lee el artículo de la página 3 y elige la respuesta correcta.'),
    ('亡灵节是怀念与安静的日子', 'Finados es un día de recuerdo y silencio'),
    ('家人们带花去墓园，主要是菊花', 'Las familias llevan flores al cementerio, sobre todo crisantemos'),
    ('教堂和墓园整天都有弥撒', 'En las iglesias y en los cementerios hay misas todo el día'),
    ('万圣节在 10 月 31 日周六', 'Halloween fue el sábado 31 de octubre'),
    ('怀念是继续亲近的方式', 'Recordar es una forma de seguir cerca'),
    ('用方框里的词填空。', 'Completa con las palabras del recuadro.'),
    ('túmulo = 墓碑', 'túmulo = la tumba'),
    ('vela = 蜡烛', 'vela = la vela'),
    ('crisântemo = 菊花', 'crisântemo = el crisantemo'),
    ('missa = 弥撒', 'missa = la misa'),
    ('silêncio = 寂静', 'silêncio = el silencio'),
    ('lembrança = 怀念', 'lembrança = el recuerdo'),
    ('用过去时（pretérito perfeito）补全。', 'Completa con el pretérito perfeito.'),
    ('visitar 过去时 elas 形式：visitaram', 'visitar, pretérito perfeito, forma elas: visitaram'),
    ('levar 过去时 elas 形式：levaram', 'levar, pretérito perfeito, forma elas: levaram'),
    ('ser 过去时 ele 形式：foi', 'ser, pretérito perfeito, forma ele: foi'),
    ('viver 过去时 ele 形式：viveu', 'viver, pretérito perfeito, forma ele: viveu'),
    ('把词组成正确的句子。', 'Ordena las palabras para formar frases.'),
    ('主语 + é + 表语', 'Sujeto + é + atributo'),
    ('主语 + 动词 + 宾语 + 地点', 'Sujeto + verbo + objeto + lugar'),
    ('主语 + 动词 + 宾语', 'Sujeto + verbo + objeto'),
    ('ESPORTE · 体育', 'ESPORTE · DEPORTE'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'NÍVEL B1 · O futebol da semana · El fútbol de la semana'),
    ('a ida 首回合 · a volta 次回合 · o finalista 决赛球队 · a decisão 决战 · a rodada 轮次。',
     'a ida = el partido de ida · a volta = el partido de vuelta · o finalista = el finalista · a decisão = la decisión · a rodada = la jornada.'),
    ('你在巴西杯支持哪支球队？写两句寄来。',
     '¿A qué equipo apoyas en la Copa do Brasil? Escribe dos frases en portugués y envíanoslas.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · LA SEMANA DEL FÚTBOL'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · EJERCICIOS DE LA PÁGINA 4'),
    ('读第 4 版文章，选出正确答案。', 'Lee el artículo de la página 4 y elige la respuesta correcta.'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点',
     'El partido de vuelta Atlético-MG × Grêmio es el sábado 7 a las 18h'),
    ('瓦斯科 × 帕尔梅拉斯次回合在周日 8 日 17 点，圣雅努阿里奥',
     'El partido de vuelta Vasco × Palmeiras es el domingo 8 a las 17h, en São Januário'),
    ('首回合在 11 月 1 日周日', 'Los partidos de ida fueron el domingo 1 de noviembre'),
    ('第 34 轮周一到周五每天都有比赛', 'La jornada 34 tiene partidos de lunes a viernes'),
    ('两回合总比分胜者进决赛', 'Quien gane en el total de los dos partidos llega a la final'),
    ('finalista=进决赛的球队 b', 'finalista = el equipo que llega a la final: b'),
    ('ida=对决的第一场 c', 'ida = el primer partido de una eliminatoria: c'),
    ('volta=对决的第二场 a', 'volta = el segundo partido de una eliminatoria: a'),
    ('rodada=一轮比赛 d', 'rodada = una jornada de partidos: d'),
    ('用括号里正确的比较形式填空。', 'Completa con la forma comparativa correcta del paréntesis.'),
    ('次回合决定决赛名额：mais', 'La vuelta decide a los finalistas: mais'),
    ('18 > 16：mais', '18 > 16: mais'),
    ('17 < 18：mais cedo', '17 < 18: mais cedo'),
    ('第 34 轮周一到周五都有比赛：mais', 'La jornada 34 va de lunes a viernes: mais'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Completa las frases en pretérito perfeito.'),
    ('ser 过去时复数：foram', 'ser, pretérito perfeito, plural: foram'),
    ('receber 过去时 ele 形式：recebeu', 'receber, pretérito perfeito, forma ele: recebeu'),
    ('começar 过去时 ela 形式：começou', 'começar, pretérito perfeito, forma ela: começou'),
    ('chegar 过去时 eles 形式：chegaram', 'chegar, pretérito perfeito, forma eles: chegaram'),
]
R56 = [
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · CUÉNTANOS'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Respuestas en la página 8 · Los niveles se mezclan: busca por número'),
    ('JOVENS · 青年', 'JOVENS · JÓVENES'),
    ('NÍVEL B1 · A reta final dos jovens · 冲刺周：年轻人的最后一周',
     'NÍVEL B1 · A reta final dos jovens · La recta final de los jóvenes'),
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）',
     '1. Confira o Cartão de Confirmação do Enem (comprueba tu tarjeta de confirmación del Enem)'),
    ('2. Revise um pouco por dia, sem maratona（每天复习一点，不搞突击）',
     '2. Revise um pouco por dia, sem maratona (repasa un poco cada día, sin atracón)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）',
     '3. Durma bem na véspera da prova (duerme bien la noche antes del examen)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）',
     '4. Separe documento e caneta preta no dia anterior (prepara tu documento y tu bolígrafo negro el día anterior)'),
    ('5. Domingo 8: chegue antes das 12h（周日 8 日：12 点前到达）',
     '5. Domingo 8: chegue antes das 12h (domingo 8: llega antes de las 12h)'),
    ('a reta final 最后冲刺 · a véspera 前夕 · a maratona 突击马拉松 · separar 准备好 · a cabeça 头脑、状态。',
     'a reta final = la recta final · a véspera = la víspera · a maratona = el atracón · separar = preparar · a cabeça = la cabeza, el ánimo.'),
    ('重要考试前一晚，你的计划是复习还是休息？写两句寄来。',
     'La noche antes de un examen importante, ¿tu plan es repasar o descansar? Escribe dos frases en portugués y envíanoslas.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · EJERCICIOS DE LA PÁGINA 5'),
    ('读第 5 版文章，选出正确答案。', 'Lee el artículo de la página 5 y elige la respuesta correcta.'),
    ('冲刺周在 11 月 8 日周日结束', 'La recta final termina el domingo 8 de noviembre'),
    ('每天复习一点', 'Repasa un poco cada día'),
    ('提前一天备好证件和黑笔', 'Prepara tu documento y tu bolígrafo negro el día anterior'),
    ('第 2 天考自然科学与数学', 'El día 2 es ciencias naturales y matemáticas'),
    ('11 月 3 日周二各州议会结束休会', 'El martes 3, las asambleas estatales vuelven del receso'),
    ('用方框里的词填空。注意：有的词要变成复数。',
     'Completa con las palabras del recuadro. Atención: una palabra debe ir en plural.'),
    ('reta final = 最后冲刺阶段', 'reta final = la recta final'),
    ('inscrito 配合复数：inscritos', 'inscrito concuerda en plural: inscritos'),
    ('véspera = 前夕', 'véspera = la víspera'),
    ('maratona = 突击马拉松', 'maratona = el atracón'),
    ('local = 地点', 'local = el lugar'),
    ('separar 祈使式：separe', 'separar, imperativo: separe'),
    ('用将来时（futuro do presente）补全。', 'Completa con el futuro (futuro do presente).'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, futuro, forma eles, irregular: farão'),
    ('mostrar 将来时：mostrará', 'mostrar, futuro: mostrará'),
    ('sair 将来时复数：sairão', 'sair, futuro, plural: sairão'),
    ('chegar 将来时：chegará', 'chegar, futuro: chegará'),
    ('确认卡显示考试地点', 'La tarjeta de confirmación muestra el lugar del examen'),
    ('错：考前突击不是好计划，每天复习一点才好',
     'Falso: el atracón de la víspera no es un buen plan; mejor repasar un poco cada día'),
    ('对：13:30 至 19:00', 'Verdadero: de 13:30 a 19:00'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · EN PROFUNDIDAD'),
    ('NÍVEL B2 · O Enem explicado · 高考详解', 'NÍVEL B2 · O Enem explicado · El Enem, explicado'),
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。',
     'os portões = las puertas · a segunda chamada = una segunda convocatoria, una segunda entrada · conferir = comprobar · a correria = las prisas.'),
    ('O DOMINGO 8 EM NÚMEROS · 11 月 8 日的数字 (horários oficiais do Inep)',
     'O DOMINGO 8 EM NÚMEROS · LOS NÚMEROS DEL DOMINGO 8 (horarios oficiales del Inep)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · EJERCICIOS DE LA PÁGINA 6'),
    ('看上面两张图，选出正确答案。', 'Mira los dos gráficos de arriba y elige la respuesta correcta.'),
    ('大门开放 60 分钟', 'Las puertas están abiertas 60 minutos'),
    ('关门到开考之间等 30 分钟', 'La espera entre el cierre y el examen es de 30 minutos'),
    ('考试 330 分钟', 'El examen dura 330 minutos'),
    ('中午到 19 点 = 7 小时', 'Del mediodía a las 19h = 7 horas'),
    ('图表数字是 Inep 官方时间', 'Las cifras del gráfico son horarios oficiales del Inep'),
    ('高考分 8 日和 15 日两个周日', 'El Enem se celebra dos domingos: 8 y 15'),
    ('第 1 天考作文、语言与人文', 'El día 1 es redacción, lenguas y humanidades'),
    ('13 点后到场不得入内', 'Quien llegue después de las 13h no entra'),
    ('根据句子意思，补全正确的动词形式。', 'Completa con la forma verbal correcta para cada frase.'),
    ('将来时：começará', 'futuro: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + futuro de subjuntivo: chegar'),
    ('现在时：fecham', 'presente: fecham'),
    ('现在时：pede', 'presente: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir',
     'Completa con las palabras del recuadro: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = las puertas'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = una segunda convocatoria, una segunda entrada'),
    ('祈使式：confira', 'imperativo: confira'),
]
R7 = [
    ('LÍNGUA · 语言', 'LÍNGUA · LENGUA'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具',
     'Enfoque en la lengua · Três níveis, três ferramentas · Tres niveles, tres herramientas'),
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro',
     'Preguntas: que horas (¿a qué hora?) + verbo; onde fica pregunta por el lugar; conferir es irregular en la forma eu: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (irregular)'),
    ('conferir：você → confere', 'conferir: você → confere'),
    ('começar：ela → começa', 'começar: ela → começa'),
    ('onde 问地点', 'onde pregunta por el lugar'),
    ('讲一周的事用过去时（pretérito perfeito）；revisar 规则（revisei）；chegar/dormir 的过去时注意重音。',
     'Para contar la semana usamos el pretérito perfeito; revisar es regular (revisei); chegar y dormir llevan acento en el pasado: chegou, dormiu.'),
    ('revisar 过去时：revisei', 'revisar, pretérito perfeito: revisei'),
    ('chegar 过去时：chegou', 'chegar, pretérito perfeito: chegou'),
    ('dormir 过去时：dormiu', 'dormir, pretérito perfeito: dormiu'),
    ('chegaram 是 chegar 的过去时复数', 'chegaram es el pretérito perfeito, plural, de chegar'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。',
     'Después de quando, se y quem, el futuro pide el subjuntivo: tiver, for, chegar (las hipótesis del domingo).'),
    ('quem + 虚拟式将来：tiver', 'quem + futuro de subjuntivo: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + futuro de subjuntivo: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + futuro de subjuntivo de ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + futuro → futuro de subjuntivo for'),
    ('高考用黑笔，蓝笔不行。', 'Bolígrafo negro; el azul no vale.'),
    ('13 点关门，13:30 到就晚了。', 'Cierran a las 13h; a las 13:30 es tarde.'),
    ('考前一夜突击没用，睡好才记得住。', 'Sin atracón: durmiendo se recuerda.'),
    ('连休是 10 月 31 日到 11 月 2 日，共三天。', 'Del 31 de octubre al 2 de noviembre.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · ERRORES'),
    ('feriadão = 连休长周末，共三天。', 'feriadão = el puente festivo.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · LA PALABRA'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！',
     'Ejemplo de la redacción, no una carta real. ¡Envíanos tu carta! Las mejores se publicarán en el VOL.3.'),
    ('编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。',
     'Nota de la redacción: las cartas reales y los mejores textos prometidos en el VOL.1 no habían llegado al cierre — queda el ejemplo y la promesa pasa al VOL.3.'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）',
     'FRASES DA SEMANA · FRASES DE LA SEMANA (textuales, de esta edición)'),
    ('从连休到考试：高考周。', 'Del puente festivo al examen: la semana del Enem.'),
    ('许多人旅行、探亲、去墓园献花。', 'Mucha gente viaja, visita a su familia y va al cementerio a llevar flores.'),
    ('亡灵节是怀念的日子。', 'Finados es el día de la memoria.'),
    ('怀念是继续亲近的方式。', 'Recordar es una forma de seguir cerca.'),
    ('每一分值一个名次，每一球值一个故事。', 'Cada punto vale una posición, cada gol vale una historia.'),
    ('睡得好，记得牢。', 'Quien duerme bien recuerda mejor.'),
    ('先做容易的，再做难的。', 'Primero las fáciles, después las difíciles.'),
    ('核对确认卡、睡好、早到。', 'Comprueba tu tarjeta, duerme bien, llega temprano.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.3)', 'A PRÓXIMA SEMANA · LA SEMANA QUE VIENE (VOL.3)'),
]
R8 = [
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · EVALUACIÓN Y RESPUESTAS'),
    ('第 8 版 · A grande prova da semana + todas as respostas',
     'Página 8 · A grande prova da semana + todas as respostas'),
    ('第 1 天在 11 月 8 日', 'El día 1 es el 8 de noviembre'),
    ('13 点关门', 'Cierre a las 13h'),
    ('13:30 开考', 'Empieza a las 13:30'),
    ('亡灵节在 11 月 2 日', 'Finados es el 2 de noviembre'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'El partido de vuelta Vasco × Palmeiras es el día 8'),
    ('连休共 3 天', 'El puente festivo dura 3 días'),
    ('考试时长 5 个半小时', 'El examen del día 8 dura cinco horas y media'),
    ('第 2 天在 11 月 15 日', 'El día 2 es el 15 de noviembre'),
    ('连休从 10 月 31 日到 11 月 2 日', 'El puente festivo va del 31 de octubre al 2 de noviembre'),
    ('确认卡是高考的文件', 'La tarjeta de confirmación es un documento del Enem'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场',
     'El partido de vuelta Atlético-MG × Grêmio es en la Arena MRV'),
    ('第 34 轮周一到周五都有比赛', 'La jornada 34 tiene partidos de lunes a viernes'),
    ('亡灵节家人们带花', 'En Finados, las familias llevan flores'),
    ('万圣节在 10 月 31 日周六', 'Halloween fue el sábado 31 de octubre'),
    ('330 是考试的分钟数', '330 son los minutos del examen'),
    ('亡灵节又称诸圣灵魂日', 'Finados también se llama el Día de los Fieles Difuntos'),
    ('卢卡斯住在贝洛奥里藏特', 'Lucas vive en Belo Horizonte'),
    ('连休里他休息并每天复习一点', 'Durante el puente festivo descansa y repasa un poco cada día'),
    ('前一晚他备好证件和黑笔、早睡',
     'La noche anterior prepara su documento y su bolígrafo negro y se acuesta temprano'),
    ('他 11 点到达考场', 'Llega al lugar del examen a las 11h'),
    ('时间词在前', 'La palabra de tiempo va primero'),
    ('主语 + 动词 + 宾语 + 地点', 'Sujeto + verbo + objeto + lugar'),
    ('疑问词组在句首', 'La expresión interrogativa va al inicio'),
    ('主语 + 动词 + 宾语', 'Sujeto + verbo + objeto'),
    ('11 月 8 日周日是高考的第一天。', 'El domingo 8 de noviembre es el primer día del Enem.'),
    ('对照第 6 版标题', 'Véase el titular de la página 6'),
    ('周日前核对确认卡。', 'Comprueba tu tarjeta antes del domingo.'),
    ('Confira = 请核对', 'Confira = comprueba'),
    ('“连休是 10 月 31 日到 11 月 2 日。” → ___',
     '“El puente festivo va del 31 de octubre al 2 de noviembre.” → ___'),
    ('feriadão = 连休', 'feriadão = el puente festivo'),
    ('你到达时，请出示带照片的证件。 → ___', 'Cuando llegues, presenta tu documento con foto. → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'futuro de subjuntivo chegar + imperativo apresente'),
    ('feriadão=连着周末的假期 b', 'feriadão = un festivo junto al fin de semana: b'),
    ('portão=考场入口 d', 'portão = la entrada del lugar del examen: d'),
    ('reta final=考前最后一周 a', 'reta final = la última semana antes del examen: a'),
    ('segunda chamada=关门后的再入场（高考没有） c',
     'segunda chamada = una nueva entrada tras el cierre (que no existe en el Enem): c'),
    ('documento com foto 带照片的证件', 'documento com foto = documento con foto'),
    ('seção = 考场分区（房间）', 'sección = la zona del examen (la sala)'),
    ('大门 13 点关闭', 'Las puertas cierran a las 13h'),
    ('考试 13:30 开始', 'El examen empieza a las 13:30'),
    ('obrigado = 谢谢', 'obrigado = gracias'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。',
     'Ejercicio de escritura (sin respuesta única); el texto modelo ({NWORDS} palabras) está abajo.'),
    ('（开放题，范文如下）', '(pregunta abierta)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'el texto modelo está en la sección H: {NWORDS} palabras'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可',
     'RESPOSTAS · RESPUESTAS — ordenadas por página, busca el número'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'Una nota breve en español para cada respuesta · ✓ = el texto modelo'),
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
# P1 edition line: 40pt measures 1876px > 1820; 38pt measures 1782px (EN precedent)
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "SEMANARIO EN PORTUGUÉS · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE", 38, "serif", True, INK, anchor="middle")',
    'content12.py')
# P1 badge: W43 PT x ES verbatim, BRICK 19pt bold, strapline slot
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "TEXTOS EN PORTUGUÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 19, "sans", True, BRICK, anchor="middle")',
    'content12.py')
# numbers-box title overflows its box at 23pt (425.8px > CW-36); tsize=20 (EN precedent)
old_close = '    ("5h30 — a duração da prova do dia 8 (el examen dura cinco horas y media)", "serif", False, INK, 20, 1.35),\n])'
assert t.count(old_close) == 1, 'numbers box close not found'
t = t.replace(old_close, old_close[:-2] + '], tsize=20)')
save('content12.py', t)

t = load('content7.py')
# P7 B2 bridge: replace whole line (avoids retyping its full-width punctuation)
t = line_replace(t, 'c.bridge(',
    'c.bridge("Después de quando, se y quem, el futuro pide el subjuntivo: tiver, for, chegar (las hipótesis del domingo).")',
    'content7.py')
# rename the disclosure variable (definition, height formula, draw line)
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_es')
# quote spacing 128 -> 104 (EN precedent): col3 stack ends ~1880, fy ~1924,
# last translation baseline ~2370, clear of the preview box at 2404
t = line_replace(t, 'cyq = fy + 66',
    '    cyq = fy + 66 + (i % 4) * 104  # ES: tightened from 128 to clear the preview box',
    'content7.py')
# word-box bottom pad 20 -> 30 (EN precedent): gloss descender pressed the
# border by 0.6px (BOXTITLE 1283.1 > 1282.5)
old_wh = 'len(wrap("feriadão = el puente festivo.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box wh line not found'
t = t.replace(old_wh, 'len(wrap("feriadão = el puente festivo.", "sans", False, 20, CW - 44)) * 29 + 30')
save('content7.py', t)

t = load('content8.py')
# P8 key paras 13.5pt/1.16 -> 13pt/1.12 (EN precedent: ES notes run longer than zh)
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
