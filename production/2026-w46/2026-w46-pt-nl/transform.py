# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x NL fan-out transform for W46 VOL.3.

Run inside the already-copied build dir. Every replacement is an exact
literal match (longest strings first); missing literals warn, and the
final pass asserts ZERO CJK chars remain in the build sources.
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + page tags are never touched.
P1 subtitle (330) and badge (372) lines are replaced whole (size/color).
Subtitle size 34pt is measured (fits at 1763px).
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
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-nl')
        save(fn, t)
t = load('render.py')
t = sub(t, 'A-Lucerna-VOL3.pdf', 'A-Lucerna-VOL3.pdf', 'render.py')
save('render.py', t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · PORTUGEES WEEKBLAD VOL.3 · TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Pagina {n} van {total}"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("Uitleg — " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. P1 masthead lines (whole-line) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "PORTUGEES WEEKBLAD · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE", 34, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "TEKSTEN IN HET PORTUGEES · UITLEG IN HET NEDERLANDS — DE EDITIE VOOR NEDERLANDSTALIGE LEZERS", 19, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 3. type / instr labels ----------
INSTR = [
    ('instr="造句"', 'instr="Maak een zin"'),
    ('instr="翻译"', 'instr="Vertaal"'),
    ('instr="判断"', 'instr="Waar of niet waar?"'),
    ('instr="写作"', 'instr="Schrijf"'),
    ('instr="填空"', 'instr="Vul in"'),
    ('instr="把词和释义配对"', 'instr="Koppel"'),
]
TYP = [
    ('"完成句子"', '"Zin afmaken"'),
    ('"词汇配对"', '"Woordenschat koppelen"'),
    ('"判断对错"', '"Waar of niet waar"'),
    ('"完形单选"', '"Gatentekst"'),
    ('"单选"', '"Meerkeuze"'),
    ('"造句"', '"Zinnen maken"'),
    ('"翻译"', '"Vertaling"'),
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

# ---------- 4. content replacements (global table, longest-first) ----------
REPL = [
    # bands
    ('NÍVEL A2 · Prova e feriado no mesmo domingo', 'NIVEAU A2 · Examen en feestdag op dezelfde zondag'),
    ('A2 → B1 · Proclamação da República: 137 anos · 共和国宣言 137 周年', 'A2 → B1 · Proclamação da República: 137 jaar'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'NIVEAU B1 · De voetbalweek'),
    ('NÍVEL B1 · A última semana dos jovens · 最后一周：年轻人的冲刺', 'NIVEAU B1 · De laatste week van de jongeren'),
    ('NÍVEL B2 · O segundo domingo explicado · 第二个周日详解', 'NIVEAU B2 · De tweede zondag, uitgelegd'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', 'Três níveis, três ferramentas · Drie niveaus, drie instrumenten'),
    ('第 8 版 · A grande prova da semana + todas as respostas', 'PAGINA 8 · De grote toets van de week + alle antwoorden'),
    # top strip / kickers
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · HET PORTUGEES DAT BRAZILIË LEEST, ELKE WEEK'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · HOOFDVERHAAL'),
    ('VIDA · 生活', 'VIDA · LEVEN'),
    ('CULTURA · 文化', 'CULTURA · CULTUUR'),
    ('ESPORTE · 体育', 'ESPORTE · SPORT'),
    ('JOVENS · 青年', 'JOVENS · JONGEREN'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · VERDIEPING'),
    ('LÍNGUA · 语言', 'LÍNGUA · TAAL'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · TOETS EN ANTWOORDEN'),
    # P1
    ('高考第二天', 'ENEM, DAG 2'),
    ('11 月 15 日第二场考试 · 共和国宣言日假期', '15 nov.: tweede examendag · feestdag van de Proclamatie van de Republiek'),
    ('讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。', 'Kernwoorden | a proclamação = proclamatie · o feriado = feestdag · a natureza = natuurwetenschappen · a matemática = wiskunde.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · IN CIJFERS'),
    ('12h — os portões abrem no domingo 15（周日 12 点开门）', '12h — os portões abrem no domingo 15 (zondag: open vanaf 12 uur)'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham (13 uur: dicht, te laat is te laat)'),
    ('13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）', '13h30–18h30 — a prova do dia 15 (het examen van de 15e, 13:30 tot 18:30)'),
    ('90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）', '90 — as questões do dia 15: 45 + 45 (90 vragen: 45 + 45)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · NU JIJ'),
    ('proclamação = 宣布（共和国宣言）', 'proclamação = proclamatie (van de Republiek)'),
    ('proclamação = 宣布（共和国宣言）。', 'proclamação = proclamatie (van de Republiek).'),
    ('feriado = 假日', 'feriado = feestdag'),
    ('portões = 大门（考场大门）', 'portões = de poorten (van het examencentrum)'),
    ('18h30 结束', 'eindigt om 18:30'),
    ('90 道题', '90 vragen'),
    ('fazer 现在时 eles 形式：fazem', 'fazer, tegenwoordige tijd, eles-vorm: fazem'),
    ('迟到不得入内：13 点后关门', 'Na 13 uur kom je er niet meer in.'),
    # .text.md variant of the line above: the export source carries a trailing 。 which the bare entry leaves behind (F-2).
    ('迟到不得入内：13 点后关门。', 'Na 13 uur kom je er niet meer in.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · IN DEZE EDITIE'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · KORTOM'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · BLIKSEMQUIZ'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lees de voorpagina en kies · Antwoorden op pagina 8'),
    ('共和国宣言日在 11 月 15 日', 'De Proclamatie van de Republiek is op 15 november'),
    ('13 点关门', 'Sluiting om 13 uur'),
    ('第 2 天考自然科学与数学', 'Dag 2: natuurwetenschappen en wiskunde'),
    ('18:30 结束', 'Einde om 18:30'),
    # P2
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · EZELSBRUG'),
    ('a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。', 'a proclamação = proclamatie · o feriado = feestdag · a natureza = natuurwetenschappen · a matemática = wiskunde · conferir = controleren · a escala = het rooster.'),
    ('在你的国家，落在周日的假日会在周一补休吗？写两句寄来。', 'Wordt in jouw land een feestdag op zondag op maandag ingehaald? Schrijf twee zinnen en stuur ze op.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · EN JIJ?'),
    ('OS HORÁRIOS DO DOMINGO 15 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 15 · TIJDEN OP ZONDAG 15'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · Eén land, meerdere klokken'),
    ('周日 12 点开门', 'Open op zondag vanaf 12 uur'),
    ('13:30 开考', 'Examen begint om 13:30'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · OEFENINGEN PAGINA 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Antwoorden op pagina 8 · Niveaus door elkaar: zoek op nummer'),
    ('读第 2 版文章，选出正确答案。', 'Lees pagina 2 en kies het juiste antwoord.'),
    ('假日落在周日，周一不补休', 'De feestdag valt op zondag, maandag geen inhaal'),
    # P7-clinic/.text.md variant of the line above: the source carries a trailing 。 (F-2/F-3).
    ('假日落在周日，周一不补休。', 'De feestdag valt op zondag, maandag geen inhaal.'),
    ('确认卡显示考试地点', 'De bevestigingskaart toont de examenlocatie'),
    ('巴西没有夏令时，钟表不动', 'Brazilië heeft geen zomertijd: de klokken blijven staan'),
    ('补全动词的现在时形式。', 'Vul de tegenwoordige tijd van het werkwoord in.'),
    ('用第 1、2 版的数字填空。', 'Vul in met de cijfers van pagina 1 en 2.'),
    ('12 点到 13 点 = 1 小时', 'Van 12 tot 13 uur = 1 uur'),
    ('13:30 至 18:30 = 5 小时', 'Van 13:30 tot 18:30 = 5 uur'),
    ('5×60 = 300 分钟', '5×60 = 300 minuten'),
    ('proclamação=宣布一个变化 b', 'proclamação = een verandering aankondigen (b)'),
    ('feriado=法律规定的休息日 c', 'feriado = een wettelijk vastgelegde rustdag (c)'),
    ('natureza=生命、物理与化学的科学 d', 'natureza = de wetenschap van leven, natuurkunde en scheikunde (d)'),
    ('matemática=数字与图形的科学 a', 'matemática = de wetenschap van getallen en figuren (a)'),
    ('把词和释义配对', 'Koppel de woorden aan de betekenissen'),
]
REPL += [
    # P3
    ('a monarquia 君主制 · a república 共和国 · o marechal 元帅 · o exílio 流亡 · o governo 政府 · a lei 法律。', 'a monarquia = monarchie · a república = republiek · o marechal = maarschalk · o exílio = ballingschap · o governo = regering · a lei = wet.'),
    ('在你的国家，有纪念共和国建立的假日吗？写两句寄来。', 'Heeft jouw land een feestdag voor de stichting van de republiek? Schrijf twee zinnen en stuur ze op.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · OEFENINGEN PAGINA 3'),
    ('读第 3 版文章，选出正确答案。', 'Lees pagina 3 en kies het juiste antwoord.'),
    ('共和国宣言在 1889 年 11 月 15 日', 'De Proclamatie van de Republiek was op 15 november 1889'),
    ('德奥多罗成为巴西第一任总统', 'Deodoro werd de eerste president van Brazilië'),
    ('全国性假日，任何城市都不能改为工作日', 'Een landelijke feestdag die geen stad tot werkdag mag maken'),
    ('2026 年假日落在周日', 'In 2026 valt de feestdag op een zondag'),
    ('共和国里总统由选举产生、任期有限', 'In een republiek wordt de president gekozen en is de macht beperkt in tijd'),
    ('用方框里的词填空。', 'Vul in met de woorden uit het kader.'),
    ('monarquia = 君主制', 'monarquia = monarchie'),
    ('república = 共和国', 'república = republiek'),
    ('marechal = 元帅', 'marechal = maarschalk'),
    ('exílio = 流亡', 'exílio = ballingschap'),
    ('governo = 政府', 'governo = regering'),
    ('lei = 法律', 'lei = wet'),
    ('用过去时（pretérito perfeito）补全。', 'Vul in in de verleden tijd (pretérito perfeito).'),
    ('tomar 过去时 elas 形式：tomaram', 'tomar, verleden tijd, eles-vorm: tomaram'),
    ('acabar 过去时 ela 形式：acabou', 'acabar, verleden tijd, ela-vorm: acabou'),
    ('ser 过去时 ele 形式：foi', 'ser, verleden tijd, ele-vorm: foi'),
    ('assumir 过去时 ele 形式：assumiu', 'assumir, verleden tijd, ele-vorm: assumiu'),
    ('把词组成正确的句子。', 'Zet de woorden in de juiste volgorde.'),
    ('主语 + é + 表语', 'Onderwerp + é + gezegde'),
    ('主语 + 动词 + 表语', 'Onderwerp + werkwoord + gezegde'),
    ('主语 + 动词 + 宾语 + 时间', 'Onderwerp + werkwoord + lijdend voorwerp + tijd'),
    # P4
    ('a ida 首回合 · a volta 次回合 · o gol 进球 · o pênalti 点球 · a pausa 休整期 · o amistoso 友谊赛。', 'a ida = de heenwedstrijd · a volta = de terugwedstrijd · o gol = de goal · o pênalti = de penalty · a pausa = de pauze · o amistoso = de vriendschappelijke wedstrijd.'),
    ('你在巴西杯支持哪支球队？谁能进决赛？写两句寄来。', 'Welk team steun jij in de Copa do Brasil, en wie haalt de finale? Schrijf twee zinnen en stuur ze op.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · DE VOETBALWEEK'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · OEFENINGEN PAGINA 4'),
    ('读第 4 版文章，选出正确答案。', 'Lees pagina 4 en kies het juiste antwoord.'),
    ('首回合格雷米奥 2 比 0 战胜米内罗竞技', 'In de heenwedstrijd won Grêmio met 2-0 van Atlético-MG'),
    ('帕尔梅拉斯 1 比 0 战胜瓦斯科，毛里西奥进球', 'Palmeiras won met 1-0 van Vasco, doelpunt van Maurício'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', 'De terugwedstrijd Atlético-MG × Grêmio is zaterdag 7 om 18 uur'),
    ('决赛 12 月 6 日单场，在马内·加林查', 'De finale: één wedstrijd, op 6 december, in het Mané Garrincha'),
    ('第 35 轮本周只有一场：米拉索尔 × 米内罗竞技', 'Speelronde 35 heeft deze week maar één wedstrijd: Mirassol × Atlético-MG'),
    ('gol=射入球网的得分 b', 'gol = de treffer in het net (b)'),
    ('ida=对决的第一场 d', 'ida = de eerste wedstrijd van een tweeluik (d)'),
    ('volta=对决的第二场 a', 'volta = de tweede wedstrijd van een tweeluik (a)'),
    ('pênalti=十一米点的罚球 c', 'pênalti = de strafschop vanaf elf meter (c)'),
    ('用括号里正确的比较形式填空。', 'Vul de juiste vergelijkingsvorm tussen haakjes in.'),
    ('5 小时 < 5.5 小时：menos', '5 uur < 5,5 uur: menos'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Maak de zinnen af in de verleden tijd (pretérito perfeito).'),
    ('vencer 过去时 ele 形式：venceu', 'vencer, verleden tijd, ele-vorm: venceu'),
    ('marcar 过去时 eles 形式：marcaram', 'marcar, verleden tijd, eles-vorm: marcaram'),
    ('marcar 过去时 ele 形式：marcou', 'marcar, verleden tijd, ele-vorm: marcou'),
    ('convocar 过去时 ele 形式：convocou', 'convocar, verleden tijd, ele-vorm: convocou'),
    ('ser 过去时复数：foram', 'ser, verleden tijd, meervoud: foram'),
    # P5
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem (controleer je Enem-bevestigingskaart)'),
    ('2. Revise um pouco por dia: Natureza e Matemática（每天复习一点：自然科学与数学）', '2. Revise um pouco por dia: Natureza e Matemática (herhaal elke dag een beetje: natuurwetenschappen en wiskunde)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova (slaap goed in de nacht voor het examen)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior (leg document en zwarte pen de dag ervoor klaar)'),
    ('5. Domingo 15: chegue antes das 12h（周日 15 日：12 点前到达）', '5. Domingo 15: chegue antes das 12h (zondag 15: kom vóór 12 uur)'),
    ('a natureza 自然科学 · a matemática 数学 · a maratona 突击马拉松 · a véspera 前夕 · comparar 比较价格 · a cabeça 头脑、状态。', 'a natureza = natuurwetenschappen · a matemática = wiskunde · a maratona = de herhaalmarathon · a véspera = de avond ervoor · comparar = prijzen vergelijken · a cabeça = het hoofd, de vorm.'),
    ('重要考试前一晚，你是复习到很晚还是早睡？写两句寄来。', 'De avond voor een belangrijk examen: studeer je tot laat of ga je vroeg slapen? Schrijf twee zinnen en stuur ze op.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · OEFENINGEN PAGINA 5'),
    ('读第 5 版文章，选出正确答案。', 'Lees pagina 5 en kies het juiste antwoord.'),
    ('最后一周在 11 月 15 日周日结束', 'De laatste week eindigt op zondag 15 november'),
    ('每天复习一点', 'Elke dag een beetje herhalen'),
    ('提前一天备好证件和黑笔', 'Document en zwarte pen de dag ervoor klaarleggen'),
    ('黑五在 11 月 27 日', 'Black Friday is op 27 november'),
    ('11 月 14 日周六巴西 × 日本 7:15', 'Zaterdag 14: Brazilië × Japan om 7:15'),
    ('用方框里的词填空。注意：有的词要变成复数。', 'Vul in met de woorden uit het kader. Let op: één woord moet in het meervoud.'),
    ('última semana = 最后一周', 'última semana = de laatste week'),
    ('inscrito 配合复数：inscritos', 'inscrito staat in het meervoud: inscritos'),
    ('véspera = 前夕', 'véspera = de avond ervoor'),
    ('maratona = 突击马拉松', 'maratona = de herhaalmarathon'),
    ('local = 地点', 'local = de plaats'),
    ('separar 祈使式：separe', 'separar, gebiedende wijs: separe'),
    ('用将来时（futuro do presente）补全。', 'Vul in in de toekomende tijd (futuro do presente).'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, toekomende tijd, onregelmatige eles-vorm: farão'),
    ('mostrar 将来时：mostrará', 'mostrar, toekomende tijd: mostrará'),
    ('sair 将来时复数：sairão', 'sair, toekomende tijd, meervoud: sairão'),
    ('chegar 将来时：chegará', 'chegar, toekomende tijd: chegará'),
    ('错：考前突击不是好计划，每天复习一点才好', 'Niet waar: stampen op de avond ervoor is geen goed plan — elke dag een beetje is beter'),
    ('对：13:30 至 18:30', 'Waar: van 13:30 tot 18:30'),
    # P6
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões = de poorten · a segunda chamada = een tweede zitting, een tweede toegang · conferir = controleren · a correria = de haast.'),
    ('O DOMINGO 15 EM NÚMEROS · 11 月 15 日的数字 (horários oficiais do Inep)', 'O DOMINGO 15 EM NÚMEROS · DE CIJFERS VAN 15 NOVEMBER (officiële Inep-tijden)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · OEFENINGEN PAGINA 6'),
    ('看上面两张图，选出正确答案。', 'Kijk naar de twee grafieken hierboven en kies het juiste antwoord.'),
    ('大门开放 60 分钟', 'De poorten blijven 60 minuten open'),
    ('关门到开考之间等 30 分钟', 'De wachttijd tussen sluiting en examen is 30 minuten'),
    ('考试 300 分钟', 'Het examen duurt 300 minuten'),
    ('中午到 18:30 = 6 个半小时', 'Middag tot 18:30 = zeseneenhalf uur'),
    ('图表数字是 Inep 官方时间', 'De cijfers in de grafiek zijn officiële Inep-tijden'),
    ('高考分 8 日和 15 日两个周日', 'De Enem valt op twee zondagen: de 8e en de 15e'),
    ('13 点后到场不得入内', 'Na 13 uur kom je er niet meer in'),
    ('根据句子意思，补全正确的动词形式。', 'Vul de juiste werkwoordsvorm in voor elke zin.'),
    ('将来时：começará', 'Toekomende tijd: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + futuro van de aanvoegende wijs: chegar'),
    ('现在时：fecham', 'Tegenwoordige tijd: fecham'),
    ('现在时：pede', 'Tegenwoordige tijd: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', 'Vul in met de woorden uit het kader: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = de poorten'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = een tweede zitting, een tweede toegang'),
    ('祈使式：confira', 'Gebiedende wijs: confira'),
    # P7
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', 'Vragen: que horas (hoe laat) + werkwoord; onde fica vraagt waar een plaats is; conferir is onregelmatig in de eu-vorm: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (onregelmatig)'),
    ('onde 问地点', 'onde vraagt naar de plaats'),
    ('讲一周的事用过去时（pretérito perfeito）；vencer 规则（venceu）；marcar/chegar/dormir 的过去时注意重音。', 'Om de week te vertellen gebruiken we de verleden tijd (pretérito perfeito); vencer is regelmatig (venceu); let op de klemtoon in de verleden tijd van marcar, chegar en dormir.'),
    ('vencer 过去时：venceu', 'vencer, verleden tijd: venceu'),
    ('marcar 过去时：marcou', 'marcar, verleden tijd: marcou'),
    ('chegar 过去时：chegou', 'chegar, verleden tijd: chegou'),
    ('venceram 是 vencer 的过去时复数', 'venceram is de verleden tijd, meervoud, van vencer'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'Na quando, se en quem komt de futuro van de aanvoegende wijs: tiver, for, chegar — de grammatica van de zondagshypothesen.'),
    ('quem + 虚拟式将来：tiver', 'quem + futuro van de aanvoegende wijs: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + futuro van de aanvoegende wijs: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + futuro van de aanvoegende wijs van ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + toekomst → futuro van de aanvoegende wijs for'),
    ('高考用黑笔，蓝笔不行。', 'Alleen zwarte pen — blauw mag niet.'),
    ('13 点关门，13:30 到就晚了。', 'Sluiting om 13 uur — 13:30 is te laat.'),
    ('15 日考试 18:30 结束，19 点是 8 日的时间。', 'Op de 15e eindigt het examen om 18:30; 19 uur hoort bij de 8e.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · PAS OP!'),
    ('proclamação = 宣布；1889 年君主制结束、共和国开始。', 'proclamação = proclamatie; in 1889 eindigde de monarchie en begon de republiek.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · WOORD VAN DE WEEK'),
    ('编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。', 'Opmerking van de redactie: de echte brieven en beste teksten uit VOL.2 waren nog niet binnen — het voorbeeld blijft, de belofte gaat naar VOL.4.'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', 'Voorbeeld van de redactie — geen echte brief. Stuur je brief op!'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · ZINNEN VAN DE WEEK (letterlijk uit dit nummer)'),
    ('两个周日、一个假日：巴西迎来高考第二天。', 'Twee zondagen, één feestdag: Brazilië maakt de tweede dag van de Enem.'),
    ('考试和假日在同一天到来。', 'Het examen en de feestdag komen op dezelfde dag.'),
    ('假日不改变时钟。', 'De feestdag verandert de klok niet.'),
    ('君主制结束了。', 'De monarchie is voorbij.'),
    ('谁能进巴西杯决赛？', 'Wie haalt de finale van de Copa do Brasil?'),
    ('睡得好，记得牢。', 'Goed slapen, beter onthouden.'),
    ('先做容易的，再做难的。', 'Eerst de makkelijke, dan de moeilijke.'),
    ('核对确认卡、睡好、早到。', 'Controleer je kaart, slaap goed, kom vroeg.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.4)', 'A PRÓXIMA SEMANA · VOLGENDE WEEK (VOL.4)'),
    # P8
    ('第 2 天在 11 月 15 日', 'Dag 2 is op 15 november'),
    ('第 1 天在 11 月 8 日', 'Dag 1 is op 8 november'),
    ('确认卡是高考的文件', 'De bevestigingskaart hoort bij de Enem'),
    ('共和国宣言日在 11 月 15 日', 'De Proclamatie van de Republiek is op 15 november'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'De terugwedstrijd Vasco × Palmeiras is op de 8e'),
    ('第二天共 90 道题', 'Dag 2 heeft in totaal 90 vragen'),
    ('考试时长 5 小时', 'Het examen duurt 5 uur'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', 'De terugwedstrijd Atlético-MG × Grêmio is in de Arena MRV'),
    ('第 35 轮本周只有一场，在 14 日', 'Speelronde 35 heeft deze week maar één wedstrijd, op de 14e'),
    ('共和国宣言在 1889 年', 'De Proclamatie van de Republiek was in 1889'),
    ('11.11 是促销日', '11.11 is de dag van de aanbiedingen'),
    ('300 是考试的分钟数', '300 is de examenduur in minuten'),
    ('德奥多罗是第一任总统', 'Deodoro was de eerste president'),
    ('玛丽娜住在圣保罗', 'Marina woont in São Paulo'),
    ('她每天复习一点自然科学', 'Ze herhaalt elke dag een beetje natuurwetenschappen'),
    ('前一晚她备好证件和黑笔、早睡', 'De avond ervoor legt ze document en zwarte pen klaar en gaat vroeg slapen'),
    ('她 11:30 到达考场', 'Ze komt om 11:30 aan bij het examencentrum'),
    ('时间词在前', 'Het tijdwoord staat vooraan'),
    ('主语 + 动词 + 宾语 + 地点', 'Onderwerp + werkwoord + lijdend voorwerp + plaats'),
    ('疑问词组在句首', 'De vraagzin staat vooraan'),
    ('主语 + 动词 + 宾语', 'Onderwerp + werkwoord + lijdend voorwerp'),
    ('11 月 15 日周日是高考的第二天。', 'Zondag 15 november is de tweede dag van de Enem.'),
    ('对照第 6 版标题', 'Zie de titel van pagina 6'),
    ('周日前核对确认卡。', 'Controleer de kaart vóór zondag.'),
    ('Confira = 请核对', 'Confira = controleer'),
    ('“假日落在周日。” → ___', '“De feestdag valt op een zondag.” → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'Futuro van de aanvoegende wijs chegar + gebiedende wijs apresente'),
    ('你到达时，请出示带照片的证件。 → ___', 'Laat bij aankomst je document met foto zien. → ___'),
    ('proclamação=宣布一个变化 b', 'proclamação = een verandering aankondigen (b)'),
    ('portão=考场入口 d', 'portão = de ingang van het examencentrum (d)'),
    ('república=1889 年后的国家形式 a', 'república = de staatsvorm na 1889 (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada = opnieuw binnen na sluiting (bestaat niet bij de Enem) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = document met foto'),
    ('seção = 考场分区（房间）', 'seção = de examenruimte (de sectie)'),
    ('大门 13 点关闭', 'De poorten sluiten om 13 uur'),
    ('考试 18:30 结束', 'Het examen eindigt om 18:30'),
    ('obrigado = 谢谢', 'obrigado = dank je'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', 'Schrijfopdracht (geen enkel juist antwoord); de modeltekst ({NWORDS} woorden) staat hieronder.'),
    ('（开放题，范文如下）', '(open opdracht — modeltekst hieronder)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'Zie de modeltekst in deel H van deze pagina ({NWORDS} woorden)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · ANTWOORDEN — per pagina geordend; zoek je nummer'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'Een korte toelichting per antwoord · ✓ = de schrijfopdracht'),
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

# ---------- 5. disclosure rename + layout tweaks (EN/DE/FR/ES/IT precedent) ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_nl')
old_wh = 'len(wrap("proclamação = proclamatie; in 1889 eindigde de monarchie en begon de republiek.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box pad line not found'
t = t.replace(old_wh, 'len(wrap("proclamação = proclamatie; in 1889 eindigde de monarchie en begon de republiek.", "sans", False, 20, CW - 44)) * 29 + 30')
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
old_box = '    ("90 — as questões do dia 15: 45 + 45 (90 vragen: 45 + 45)", "serif", False, INK, 20, 1.35),\n])'
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
