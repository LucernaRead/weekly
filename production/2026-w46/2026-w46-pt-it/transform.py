# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x IT fan-out transform for W46 VOL.3.

Run inside the already-copied build dir. Every replacement is an exact
literal match (longest strings first); missing literals warn, and the
final pass asserts ZERO CJK chars remain in the build sources.
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + page tags are never touched.
P1 subtitle (330) and badge (372) lines are replaced whole (size/color).
Subtitle size 33pt is measured (36pt overflows the page frame).
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
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-it')
        save(fn, t)
t = load('render.py')
t = sub(t, 'A-Lucerna-VOL3.pdf', 'A-Lucerna-VOL3-IT.pdf', 'render.py')
save('render.py', t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · SETTIMANALE PORTOGHESE VOL.3 · TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} di {total}"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Nota — " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. P1 masthead lines (whole-line) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "SETTIMANALE PORTOGHESE · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE", 33, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "TESTI IN PORTOGHESE · SPIEGAZIONI IN ITALIANO — L\u2019EDIZIONE PER I LETTORI ITALIANI", 19, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 3. type / instr labels ----------
INSTR = [
    ('instr="造句"', 'instr="Forma una frase"'),
    ('instr="翻译"', 'instr="Traduci"'),
    ('instr="判断"', 'instr="Vero o falso?"'),
    ('instr="写作"', 'instr="Scrivi"'),
    ('instr="填空"', 'instr="Completa"'),
    ('instr="把词和释义配对"', 'instr="Abbina"'),
]
TYP = [
    ('"完成句子"', '"Completare la frase"'),
    ('"词汇配对"', '"Abbinare il lessico"'),
    ('"判断对错"', '"Vero o falso"'),
    ('"完形单选"', '"Testo con buchi"'),
    ('"单选"', '"Scelta multipla"'),
    ('"造句"', '"Formare frasi"'),
    ('"翻译"', '"Traduzione"'),
    ('"写作"', '"Scrittura"'),
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
    ('NÍVEL A2 · Prova e feriado no mesmo domingo', 'LIVELLO A2 · Esame e festa lo stesso giorno'),
    ('A2 → B1 · Proclamação da República: 137 anos · 共和国宣言 137 周年', 'A2 → B1 · Proclamação da República: 137 anni'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'LIVELLO B1 · La settimana del calcio'),
    ('NÍVEL B1 · A última semana dos jovens · 最后一周：年轻人的冲刺', 'LIVELLO B1 · L\u2019ultima settimana dei giovani'),
    ('NÍVEL B2 · O segundo domingo explicado · 第二个周日详解', 'LIVELLO B2 · La seconda domenica, spiegata'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', 'Três níveis, três ferramentas · Tre livelli, tre strumenti'),
    ('第 8 版 · A grande prova da semana + todas as respostas', 'PAGINA 8 · La grande prova della settimana + tutte le risposte'),
    # top strip / kickers
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · IL PORTOGHESE CHE LEGGE IL BRASILE, OGNI SETTIMANA'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · IN PRIMA PAGINA'),
    ('VIDA · 生活', 'VIDA · LA VITA'),
    ('CULTURA · 文化', 'CULTURA · CULTURA'),
    ('ESPORTE · 体育', 'ESPORTE · SPORT'),
    ('JOVENS · 青年', 'JOVENS · I GIOVANI'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · APPROFONDIMENTO'),
    ('LÍNGUA · 语言', 'LÍNGUA · LINGUA'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · PROVA E RISPOSTE'),
    # P1
    ('高考第二天', 'ENEM, GIORNO 2'),
    ('11 月 15 日第二场考试 · 共和国宣言日假期', '15 nov.: secondo giorno d\u2019esame · festa della Proclamazione della Repubblica'),
    ('讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。', 'Parole chiave | a proclamação = proclamazione · o feriado = festa · a natureza = scienze della natura · a matemática = matematica.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · IN CIFRE'),
    ('12h — os portões abrem no domingo 15（周日 12 点开门）', '12h — os portões abrem no domingo 15 (domenica: apertura alle 12)'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham (13: chiusura, chi arriva tardi non entra)'),
    ('13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）', '13h30–18h30 — a prova do dia 15 (la prova del 15, dalle 13:30 alle 18:30)'),
    ('90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）', '90 — as questões do dia 15: 45 + 45 (90 domande: 45 + 45)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · ORA TOCCA A TE'),
    ('proclamação = 宣布（共和国宣言）', 'proclamação = proclamazione (della Repubblica)'),
    ('proclamação = 宣布（共和国宣言）。', 'proclamação = proclamazione (della Repubblica).'),
    ('feriado = 假日', 'feriado = festa'),
    ('portões = 大门（考场大门）', 'portões = i cancelli (del centro d\u2019esame)'),
    ('18h30 结束', 'finisce alle 18:30'),
    ('90 道题', '90 domande'),
    ('fazer 现在时 eles 形式：fazem', 'fazer, presente, forma eles: fazem'),
    ('迟到不得入内：13 点后关门', 'Dopo le 13 non si entra più.'),
    # .text.md variant of the line above: the export source carries a trailing 。 which the bare entry leaves behind (F-2).
    ('迟到不得入内：13 点后关门。', 'Dopo le 13 non si entra più.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · SOMMARIO'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · IN BREVE'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · QUIZ LAMPO'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Leggi la prima pagina e scegli · Risposte a pagina 8'),
    ('共和国宣言日在 11 月 15 日', 'La Proclamazione della Repubblica è il 15 novembre'),
    ('13 点关门', 'Chiusura alle 13'),
    ('第 2 天考自然科学与数学', 'Giorno 2: scienze della natura e matematica'),
    ('18:30 结束', 'Finisce alle 18:30'),
    # P2
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · IL TRUCCO'),
    ('a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。', 'a proclamação = proclamazione · o feriado = festa · a natureza = scienze della natura · a matemática = matematica · conferir = controllare · a escala = il turno.'),
    ('在你的国家，落在周日的假日会在周一补休吗？写两句寄来。', 'Nel tuo paese, una festa che cade di domenica si recupera il lunedì? Scrivi due frasi e mandacele.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · E TU?'),
    ('OS HORÁRIOS DO DOMINGO 15 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 15 · GLI ORARI DI DOMENICA 15'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · Un paese, più orologi'),
    ('周日 12 点开门', 'Apertura domenica alle 12'),
    ('13:30 开考', 'La prova inizia alle 13:30'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · ESERCIZI PAGINA 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Risposte a pagina 8 · Livelli mescolati: cerca per numero'),
    ('读第 2 版文章，选出正确答案。', 'Leggi pagina 2 e scegli la risposta giusta.'),
    ('假日落在周日，周一不补休', 'La festa cade di domenica, il lunedì non si recupera'),
    # P7-clinic/.text.md variant of the line above: the source carries a trailing 。 (F-2/F-3).
    ('假日落在周日，周一不补休。', 'La festa cade di domenica, il lunedì non si recupera.'),
    ('确认卡显示考试地点', 'La carta di conferma mostra il luogo d\u2019esame'),
    ('巴西没有夏令时，钟表不动', 'Il Brasile non ha l\u2019ora legale: gli orologi non si spostano'),
    ('补全动词的现在时形式。', 'Completa con la forma al presente del verbo.'),
    ('用第 1、2 版的数字填空。', 'Completa con i numeri delle pagine 1 e 2.'),
    ('12 点到 13 点 = 1 小时', 'Dalle 12 alle 13 = 1 ora'),
    ('13:30 至 18:30 = 5 小时', 'Dalle 13:30 alle 18:30 = 5 ore'),
    ('5×60 = 300 分钟', '5×60 = 300 minuti'),
    ('proclamação=宣布一个变化 b', 'proclamação = annunciare un cambiamento (b)'),
    ('feriado=法律规定的休息日 c', 'feriado = un giorno di riposo fissato per legge (c)'),
    ('natureza=生命、物理与化学的科学 d', 'natureza = la scienza della vita, della fisica e della chimica (d)'),
    ('matemática=数字与图形的科学 a', 'matemática = la scienza dei numeri e delle figure (a)'),
    ('把词和释义配对', 'Abbina le parole e le definizioni'),
]
REPL += [
    # P3
    ('a monarquia 君主制 · a república 共和国 · o marechal 元帅 · o exílio 流亡 · o governo 政府 · a lei 法律。', 'a monarquia = monarchia · a república = repubblica · o marechal = maresciallo · o exílio = esilio · o governo = governo · a lei = legge.'),
    ('在你的国家，有纪念共和国建立的假日吗？写两句寄来。', 'Nel tuo paese c\u2019è una festa per la fondazione della repubblica? Scrivi due frasi e mandacele.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · ESERCIZI PAGINA 3'),
    ('读第 3 版文章，选出正确答案。', 'Leggi pagina 3 e scegli la risposta giusta.'),
    ('共和国宣言在 1889 年 11 月 15 日', 'La Proclamazione della Repubblica è avvenuta il 15 novembre 1889'),
    ('德奥多罗成为巴西第一任总统', 'Deodoro è diventato il primo presidente del Brasile'),
    ('全国性假日，任何城市都不能改为工作日', 'Una festa nazionale che nessuna città può trasformare in giorno lavorativo'),
    ('2026 年假日落在周日', 'Nel 2026 la festa cade di domenica'),
    ('共和国里总统由选举产生、任期有限', 'In repubblica il presidente è eletto e il potere ha un limite di tempo'),
    ('用方框里的词填空。', 'Completa con le parole del riquadro.'),
    ('monarquia = 君主制', 'monarquia = monarchia'),
    ('república = 共和国', 'república = repubblica'),
    ('marechal = 元帅', 'marechal = maresciallo'),
    ('exílio = 流亡', 'exílio = esilio'),
    ('governo = 政府', 'governo = governo'),
    ('lei = 法律', 'lei = legge'),
    ('用过去时（pretérito perfeito）补全。', 'Completa al passato (pretérito perfeito).'),
    ('tomar 过去时 elas 形式：tomaram', 'tomar, passato, forma elas: tomaram'),
    ('acabar 过去时 ela 形式：acabou', 'acabar, passato, forma ela: acabou'),
    ('ser 过去时 ele 形式：foi', 'ser, passato, forma ele: foi'),
    ('assumir 过去时 ele 形式：assumiu', 'assumir, passato, forma ele: assumiu'),
    ('把词组成正确的句子。', 'Metti le parole nell\u2019ordine giusto.'),
    ('主语 + é + 表语', 'Soggetto + é + predicato'),
    ('主语 + 动词 + 表语', 'Soggetto + verbo + predicato'),
    ('主语 + 动词 + 宾语 + 时间', 'Soggetto + verbo + oggetto + tempo'),
    # P4
    ('a ida 首回合 · a volta 次回合 · o gol 进球 · o pênalti 点球 · a pausa 休整期 · o amistoso 友谊赛。', 'a ida = la gara d\u2019andata · a volta = la gara di ritorno · o gol = il gol · o pênalti = il rigore · a pausa = la pausa · o amistoso = l\u2019amichevole.'),
    ('你在巴西杯支持哪支球队？谁能进决赛？写两句寄来。', 'Quale squadra tifi nella Copa do Brasil, e chi andrà in finale? Scrivi due frasi e mandacele.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · LA SETTIMANA DEL CALCIO'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · ESERCIZI PAGINA 4'),
    ('读第 4 版文章，选出正确答案。', 'Leggi pagina 4 e scegli la risposta giusta.'),
    ('首回合格雷米奥 2 比 0 战胜米内罗竞技', 'All\u2019andata il Grêmio ha battuto l\u2019Atlético-MG 2 a 0'),
    ('帕尔梅拉斯 1 比 0 战胜瓦斯科，毛里西奥进球', 'Il Palmeiras ha battuto il Vasco 1 a 0, gol di Maurício'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', 'Il ritorno Atlético-MG × Grêmio è sabato 7 alle 18'),
    ('决赛 12 月 6 日单场，在马内·加林查', 'La finale: una sola partita, il 6 dicembre, al Mané Garrincha'),
    ('第 35 轮本周只有一场：米拉索尔 × 米内罗竞技', 'La 35ª giornata ha una sola partita questa settimana: Mirassol × Atlético-MG'),
    ('gol=射入球网的得分 b', 'gol = il punto segnato nella rete (b)'),
    ('ida=对决的第一场 d', 'ida = la prima partita di uno scontro (d)'),
    ('volta=对决的第二场 a', 'volta = la seconda partita di uno scontro (a)'),
    ('pênalti=十一米点的罚球 c', 'pênalti = il tiro dal dischetto (c)'),
    ('用括号里正确的比较形式填空。', 'Completa con la forma comparativa giusta tra parentesi.'),
    ('5 小时 < 5.5 小时：menos', '5 ore < 5,5 ore: menos'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Completa le frasi al passato (pretérito perfeito).'),
    ('vencer 过去时 ele 形式：venceu', 'vencer, passato, forma ele: venceu'),
    ('marcar 过去时 eles 形式：marcaram', 'marcar, passato, forma eles: marcaram'),
    ('marcar 过去时 ele 形式：marcou', 'marcar, passato, forma ele: marcou'),
    ('convocar 过去时 ele 形式：convocou', 'convocar, passato, forma ele: convocou'),
    ('ser 过去时复数：foram', 'ser, passato, plurale: foram'),
    # P5
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem (controlla la tua carta di conferma dell\u2019Enem)'),
    ('2. Revise um pouco por dia: Natureza e Matemática（每天复习一点：自然科学与数学）', '2. Revise um pouco por dia: Natureza e Matemática (ripassa un po\u2019 ogni giorno: scienze della natura e matematica)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova (dormi bene la vigilia della prova)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior (prepara documento e penna nera il giorno prima)'),
    ('5. Domingo 15: chegue antes das 12h（周日 15 日：12 点前到达）', '5. Domingo 15: chegue antes das 12h (domenica 15: arriva prima delle 12)'),
    ('a natureza 自然科学 · a matemática 数学 · a maratona 突击马拉松 · a véspera 前夕 · comparar 比较价格 · a cabeça 头脑、状态。', 'a natureza = scienze della natura · a matemática = matematica · a maratona = la maratona di ripasso · a véspera = la vigilia · comparar = confrontare i prezzi · a cabeça = la testa, la forma.'),
    ('重要考试前一晚，你是复习到很晚还是早睡？写两句寄来。', 'La sera prima di un esame importante: ripassi fino a tardi o vai a letto presto? Scrivi due frasi e mandacele.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · ESERCIZI PAGINA 5'),
    ('读第 5 版文章，选出正确答案。', 'Leggi pagina 5 e scegli la risposta giusta.'),
    ('最后一周在 11 月 15 日周日结束', 'L\u2019ultima settimana finisce domenica 15 novembre'),
    ('每天复习一点', 'Ripassare un po\u2019 ogni giorno'),
    ('提前一天备好证件和黑笔', 'Preparare documento e penna nera il giorno prima'),
    ('黑五在 11 月 27 日', 'Il Black Friday è il 27 novembre'),
    ('11 月 14 日周六巴西 × 日本 7:15', 'Sabato 14: Brasile × Giappone alle 7:15'),
    ('用方框里的词填空。注意：有的词要变成复数。', 'Completa con le parole del riquadro. Attenzione: una parola va al plurale.'),
    ('última semana = 最后一周', 'última semana = l\u2019ultima settimana'),
    ('inscrito 配合复数：inscritos', 'inscrito concorda al plurale: inscritos'),
    ('véspera = 前夕', 'véspera = la vigilia'),
    ('maratona = 突击马拉松', 'maratona = la maratona di ripasso'),
    ('local = 地点', 'local = il luogo'),
    ('separar 祈使式：separe', 'separar, imperativo: separe'),
    ('用将来时（futuro do presente）补全。', 'Completa al futuro (futuro do presente).'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, futuro, forma eles irregolare: farão'),
    ('mostrar 将来时：mostrará', 'mostrar, futuro: mostrará'),
    ('sair 将来时复数：sairão', 'sair, futuro, plurale: sairão'),
    ('chegar 将来时：chegará', 'chegar, futuro: chegará'),
    ('错：考前突击不是好计划，每天复习一点才好', 'Falso: sgobbare la vigilia non è un buon piano — un po\u2019 ogni giorno è meglio'),
    ('对：13:30 至 18:30', 'Vero: dalle 13:30 alle 18:30'),
    # P6
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões = i cancelli · a segunda chamada = una seconda sessione, un secondo accesso · conferir = controllare · a correria = la fretta.'),
    ('O DOMINGO 15 EM NÚMEROS · 11 月 15 日的数字 (horários oficiais do Inep)', 'O DOMINGO 15 EM NÚMEROS · I NUMERI DEL 15 NOVEMBRE (orari ufficiali Inep)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · ESERCIZI PAGINA 6'),
    ('看上面两张图，选出正确答案。', 'Guarda i due grafici qui sopra e scegli la risposta giusta.'),
    ('大门开放 60 分钟', 'I cancelli restano aperti 60 minuti'),
    ('关门到开考之间等 30 分钟', 'L\u2019attesa tra la chiusura e la prova è di 30 minuti'),
    ('考试 300 分钟', 'La prova dura 300 minuti'),
    ('中午到 18:30 = 6 个半小时', 'Da mezzogiorno alle 18:30 = sei ore e mezza'),
    ('图表数字是 Inep 官方时间', 'I numeri del grafico sono gli orari ufficiali Inep'),
    ('高考分 8 日和 15 日两个周日', 'L\u2019Enem si svolge in due domeniche: l\u20198 e il 15'),
    ('13 点后到场不得入内', 'Dopo le 13 non si entra più'),
    ('根据句子意思，补全正确的动词形式。', 'Completa con la forma verbale giusta per ogni frase.'),
    ('将来时：começará', 'Futuro: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + futuro del congiuntivo: chegar'),
    ('现在时：fecham', 'Presente: fecham'),
    ('现在时：pede', 'Presente: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', 'Completa con le parole del riquadro: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = i cancelli'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = una seconda sessione, un secondo accesso'),
    ('祈使式：confira', 'Imperativo: confira'),
    # P7
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', 'Domande: que horas (a che ora) + verbo; onde fica chiede dove si trova un luogo; conferir è irregolare nella forma eu: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (irregolare)'),
    ('onde 问地点', 'onde chiede il luogo'),
    ('讲一周的事用过去时（pretérito perfeito）；vencer 规则（venceu）；marcar/chegar/dormir 的过去时注意重音。', 'Per raccontare la settimana usiamo il passato (pretérito perfeito); vencer è regolare (venceu); attenzione all\u2019accento al passato di marcar, chegar e dormir.'),
    ('vencer 过去时：venceu', 'vencer, passato: venceu'),
    ('marcar 过去时：marcou', 'marcar, passato: marcou'),
    ('chegar 过去时：chegou', 'chegar, passato: chegou'),
    ('venceram 是 vencer 的过去时复数', 'venceram è il passato, plurale, di vencer'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'Dopo quando, se e quem va il futuro del congiuntivo: tiver, for, chegar — la grammatica delle ipotesi della domenica.'),
    ('quem + 虚拟式将来：tiver', 'quem + futuro del congiuntivo: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + futuro del congiuntivo: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + futuro del congiuntivo di ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + futuro → futuro del congiuntivo for'),
    ('高考用黑笔，蓝笔不行。', 'Solo penna nera: la blu non va bene.'),
    ('13 点关门，13:30 到就晚了。', 'Chiusura alle 13: arrivare alle 13:30 è tardi.'),
    ('15 日考试 18:30 结束，19 点是 8 日的时间。', 'Il 15 la prova finisce alle 18:30; le 19 sono del giorno 8.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · ERRORI'),
    ('proclamação = 宣布；1889 年君主制结束、共和国开始。', 'proclamação = proclamazione; nel 1889 finisce la monarchia e inizia la repubblica.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · LA PAROLA'),
    ('编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。', 'Nota della redazione: le lettere vere e i migliori testi promessi nel VOL.2 non erano arrivati alla chiusura — resta l\u2019esempio e la promessa passa al VOL.4.'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', 'Esempio della redazione — non è una lettera vera. Mandateci le vostre lettere!'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · FRASI DELLA SETTIMANA (citate parola per parola in questo numero)'),
    ('两个周日、一个假日：巴西迎来高考第二天。', 'Due domeniche, una festa: il Brasile affronta il secondo giorno dell\u2019Enem.'),
    ('考试和假日在同一天到来。', 'L\u2019esame e la festa arrivano lo stesso giorno.'),
    ('假日不改变时钟。', 'La festa non cambia l\u2019orologio.'),
    ('君主制结束了。', 'La monarchia è finita.'),
    ('谁能进巴西杯决赛？', 'Chi andrà in finale di Copa do Brasil?'),
    ('睡得好，记得牢。', 'Dormire bene, ricordare meglio.'),
    ('先做容易的，再做难的。', 'Prima le facili, poi le difficili.'),
    ('核对确认卡、睡好、早到。', 'Controlla la carta, dormi bene, arriva presto.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.4)', 'A PRÓXIMA SEMANA · LA PROSSIMA SETTIMANA (VOL.4)'),
    # P8
    ('第 2 天在 11 月 15 日', 'Il giorno 2 è il 15 novembre'),
    ('第 1 天在 11 月 8 日', 'Il giorno 1 è l\u20198 novembre'),
    ('确认卡是高考的文件', 'La carta di conferma appartiene all\u2019Enem'),
    ('共和国宣言日在 11 月 15 日', 'La Proclamazione della Repubblica è il 15 novembre'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'Il ritorno Vasco × Palmeiras è il giorno 8'),
    ('第二天共 90 道题', 'Il giorno 2 ha 90 domande in tutto'),
    ('考试时长 5 小时', 'La prova dura 5 ore'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', 'Il ritorno Atlético-MG × Grêmio è all\u2019Arena MRV'),
    ('第 35 轮本周只有一场，在 14 日', 'La 35ª giornata ha una sola partita questa settimana, il 14'),
    ('共和国宣言在 1889 年', 'La Proclamazione della Repubblica è del 1889'),
    ('11.11 是促销日', 'L\u201911.11 è il giorno delle offerte'),
    ('300 是考试的分钟数', '300 è la durata della prova in minuti'),
    ('德奥多罗是第一任总统', 'Deodoro è stato il primo presidente'),
    ('玛丽娜住在圣保罗', 'Marina abita a São Paulo'),
    ('她每天复习一点自然科学', 'Ripassa un po\u2019 di scienze della natura ogni giorno'),
    ('前一晚她备好证件和黑笔、早睡', 'La vigilia prepara documento e penna nera e va a letto presto'),
    ('她 11:30 到达考场', 'Arriva al centro d\u2019esame alle 11:30'),
    ('时间词在前', 'La parola del tempo sta davanti'),
    ('主语 + 动词 + 宾语 + 地点', 'Soggetto + verbo + oggetto + luogo'),
    ('疑问词组在句首', 'Il gruppo interrogativo sta all\u2019inizio'),
    ('主语 + 动词 + 宾语', 'Soggetto + verbo + oggetto'),
    ('11 月 15 日周日是高考的第二天。', 'Domenica 15 novembre è il secondo giorno dell\u2019Enem.'),
    ('对照第 6 版标题', 'Vedi il titolo di pagina 6'),
    ('周日前核对确认卡。', 'Controlla la carta prima di domenica.'),
    ('Confira = 请核对', 'Confira = controlla'),
    ('“假日落在周日。” → ___', '«La festa cade di domenica.» → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'Futuro del congiuntivo chegar + imperativo apresente'),
    ('你到达时，请出示带照片的证件。 → ___', 'Quando arrivi, mostra il documento con foto. → ___'),
    ('proclamação=宣布一个变化 b', 'proclamação = annunciare un cambiamento (b)'),
    ('portão=考场入口 d', 'portão = l\u2019ingresso del centro d\u2019esame (d)'),
    ('república=1889 年后的国家形式 a', 'república = la forma di Stato dopo il 1889 (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada = rientro dopo la chiusura (non esiste all\u2019Enem) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = documento con foto'),
    ('seção = 考场分区（房间）', 'seção = l\u2019aula d\u2019esame (il settore)'),
    ('大门 13 点关闭', 'I cancelli chiudono alle 13'),
    ('考试 18:30 结束', 'La prova finisce alle 18:30'),
    ('obrigado = 谢谢', 'obrigado = grazie'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', 'Esercizio di scrittura (senza risposta unica); il testo modello ({NWORDS} parole) è qui sotto.'),
    ('（开放题，范文如下）', '(esercizio aperto — testo modello qui sotto)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'Vedi il testo modello nella parte H di questa pagina ({NWORDS} parole)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · RISPOSTE — ordinate per pagina; trova il tuo numero'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'Una breve nota per risposta · ✓ = l\u2019esercizio di scrittura'),
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

# ---------- 5. disclosure rename + layout tweaks (EN/DE/FR/ES precedent) ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_it')
old_wh = 'len(wrap("proclamação = proclamazione; nel 1889 finisce la monarchia e inizia la repubblica.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box pad line not found'
t = t.replace(old_wh, 'len(wrap("proclamação = proclamazione; nel 1889 finisce la monarchia e inizia la repubblica.", "sans", False, 20, CW - 44)) * 29 + 30')
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
old_box = '    ("90 — as questões do dia 15: 45 + 45 (90 domande: 45 + 45)", "serif", False, INK, 20, 1.35),\n])'
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
