# -*- coding: utf-8 -*-
"""PT core (zh explanations) -> PT x DE fan-out transform for W46 VOL.3.

Run inside the already-copied build dir. Every replacement is an exact
literal match (longest strings first); missing literals warn, and the
final pass asserts ZERO CJK chars remain in the build sources.
Frozen Portuguese text, the P7 example letter (lt), the PT disclosure
(disc_pt) and the P7 quote strings + page tags are never touched.
P1 subtitle (330) and badge (372) lines are replaced whole (size/color).
Subtitle size 30pt is measured (34pt overflows the page frame).
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
        t = t.replace('weekly-report-w46-pt-core', 'weekly-report-w46-pt-de')
        save(fn, t)
t = load('render.py')
t = sub(t, 'A-Lucerna-VOL3.pdf', 'A-Lucerna-VOL3-DE.pdf', 'render.py')
save('render.py', t)

# ---------- 1. bslib4 furniture ----------
t = load('bslib4.py')
t = sub(t, 'A Lucerna · 葡萄牙语周报 VOL.3 · LUCERNA PORTUGUESE WEEKLY',
        'A Lucerna · PORTUGIESISCHE WOCHENZEITUNG VOL.3 · TEXT AUF PORTUGIESISCH · ERKLÄRUNGEN AUF DEUTSCH', 'bslib4.py')
t = sub(t, 'f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"', 'bslib4.py')
t = sub(t, '("译注｜" + s', '("HINWEIS · " + s', 'bslib4.py')
save('bslib4.py', t)

# ---------- 2. P1 masthead lines (whole-line) ----------
t = load('content12.py')
t = line_replace(t, 'p.text(975, 330,',
    'p.text(975, 330, "PORTUGIESISCHE WOCHENZEITUNG · VOL.3 · ENEM, DIA 2 · PROCLAMAÇÃO DA REPÚBLICA · O FUTEBOL DECIDE", 30, "serif", True, INK, anchor="middle")',
    'content12.py')
t = line_replace(t, 'p.text(975, 372,',
    'p.text(975, 372, "PORTUGIESISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 19, "sans", True, BRICK, anchor="middle")',
    'content12.py')
save('content12.py', t)

# ---------- 3. type / instr labels ----------
INSTR = [
    ('instr="造句"', 'instr="Satz bilden"'),
    ('instr="翻译"', 'instr="Übersetzen"'),
    ('instr="判断"', 'instr="Richtig oder falsch?"'),
    ('instr="写作"', 'instr="Schreiben"'),
    ('instr="填空"', 'instr="Ergänzen"'),
    ('instr="把词和释义配对"', 'instr="Paare zuordnen"'),
]
TYP = [
    ('"完成句子"', '"Satz vervollständigen"'),
    ('"词汇配对"', '"Wortschatz zuordnen"'),
    ('"判断对错"', '"Richtig oder falsch"'),
    ('"完形单选"', '"Lückentext"'),
    ('"单选"', '"Multiple Choice"'),
    ('"造句"', '"Satzbau"'),
    ('"翻译"', '"Übersetzung"'),
    ('"写作"', '"Schreiben"'),
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
    ('NÍVEL A2 · Prova e feriado no mesmo domingo', 'NIVEAU A2 · Prüfung und Feiertag am selben Sonntag'),
    ('A2 → B1 · Proclamação da República: 137 anos · 共和国宣言 137 周年', 'A2 → B1 · Proclamação da República: 137 Jahre'),
    ('NÍVEL B1 · O futebol da semana · 足球之周', 'NIVEAU B1 · Die Fußballwoche'),
    ('NÍVEL B1 · A última semana dos jovens · 最后一周：年轻人的冲刺', 'NIVEAU B1 · Die letzte Woche der Jugendlichen'),
    ('NÍVEL B2 · O segundo domingo explicado · 第二个周日详解', 'NIVEAU B2 · Der zweite Sonntag, erklärt'),
    ('聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具', 'Três níveis, três ferramentas · Drei Niveaus, drei Werkzeuge'),
    ('第 8 版 · A grande prova da semana + todas as respostas', 'SEITE 8 · Die große Prüfung der Woche + alle Antworten'),
    # top strip / kickers
    ('TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语', 'TODA SEMANA EM PORTUGUÊS · DAS PORTUGIESISCH, DAS BRASILIEN LIEST, JEDE WOCHE'),
    ('A NOTÍCIA · 头条', 'A NOTÍCIA · TITELTHEMA'),
    ('VIDA · 生活', 'VIDA · LEBEN'),
    ('CULTURA · 文化', 'CULTURA · KULTUR'),
    ('ESPORTE · 体育', 'ESPORTE · SPORT'),
    ('JOVENS · 青年', 'JOVENS · JUGEND'),
    ('APROFUNDAMENTO · 深读', 'APROFUNDAMENTO · VERTIEFUNG'),
    ('LÍNGUA · 语言', 'LÍNGUA · SPRACHE'),
    ('AVALIAÇÃO E RESPOSTAS · 练习与答案', 'AVALIAÇÃO E RESPOSTAS · TEST UND ANTWORTEN'),
    # P1
    ('高考第二天', 'ENEM, TAG 2'),
    ('11 月 15 日第二场考试 · 共和国宣言日假期', '15. Nov.: zweiter Prüfungstag · Feiertag der Ausrufung der Republik'),
    ('讲解｜a proclamação 宣布、宣告 · o feriado 假日 · a natureza 自然科学 · a matemática 数学。', 'Stichwörter | a proclamação = Ausrufung · o feriado = Feiertag · a natureza = Naturwissenschaften · a matemática = Mathematik.'),
    ('A SEMANA EM NÚMEROS · 数字', 'A SEMANA EM NÚMEROS · IN ZAHLEN'),
    ('12h — os portões abrem no domingo 15（周日 12 点开门）', '12h — os portões abrem no domingo 15 (Sonntag: Einlass ab 12 Uhr)'),
    ('13h — os portões fecham（13 点关门，过时不入）', '13h — os portões fecham (13 Uhr: Tore schließen, zu spät ist zu spät)'),
    ('13h30–18h30 — a prova do dia 15（考试 13:30 至 18:30）', '13h30–18h30 — a prova do dia 15 (Prüfung am 15., 13:30 bis 18:30 Uhr)'),
    ('90 — as questões do dia 15: 45 + 45（90 道题：45 + 45）', '90 — as questões do dia 15: 45 + 45 (90 Fragen: 45 + 45)'),
    ('AGORA VOCÊ · 即学即练', 'AGORA VOCÊ · JETZT DU'),
    ('proclamação = 宣布（共和国宣言）', 'proclamação = Ausrufung (der Republik)'),
    ('proclamação = 宣布（共和国宣言）。', 'proclamação = Ausrufung (der Republik).'),
    ('feriado = 假日', 'feriado = Feiertag'),
    ('portões = 大门（考场大门）', 'portões = die Tore (des Prüfungsortes)'),
    ('18h30 结束', 'Ende um 18:30 Uhr'),
    ('90 道题', '90 Fragen'),
    ('fazer 现在时 eles 形式：fazem', 'fazer, Präsens, eles-Form: fazem'),
    ('迟到不得入内：13 点后关门', 'Wer nach 13 Uhr kommt, bleibt draußen.'),
    # .text.md variant of the line above: the export source carries a trailing 。 which the bare entry leaves behind (F-2).
    ('迟到不得入内：13 点后关门。', 'Wer nach 13 Uhr kommt, bleibt draußen.'),
    ('NESTA EDIÇÃO · 本期目录', 'NESTA EDIÇÃO · INHALT'),
    ('EM POUCAS PALAVRAS · 快讯', 'EM POUCAS PALAVRAS · IN KÜRZE'),
    ('QUIZ RELÂMPAGO · 闪电问答', 'QUIZ RELÂMPAGO · BLITZQUIZ'),
    ('读头版，选出正确答案 · 答案见第 8 版', 'Lies die Titelseite und wähle · Antworten auf Seite 8'),
    ('共和国宣言日在 11 月 15 日', 'Der Tag der Ausrufung der Republik ist am 15. November'),
    ('13 点关门', 'Die Tore schließen um 13 Uhr'),
    ('第 2 天考自然科学与数学', 'Am 2. Tag: Naturwissenschaften und Mathematik'),
    ('18:30 结束', 'Ende um 18:30 Uhr'),
    # P2
    ('PARA NÃO ERRAR · 口诀', 'PARA NÃO ERRAR · DIE MERKREGEL'),
    ('a proclamação 宣布 · o feriado 假日 · a natureza 自然科学 · a matemática 数学 · conferir 核对 · a escala 排班。', 'a proclamação = Ausrufung · o feriado = Feiertag · a natureza = Naturwissenschaften · a matemática = Mathematik · conferir = prüfen · a escala = der Dienstplan.'),
    ('在你的国家，落在周日的假日会在周一补休吗？写两句寄来。', 'Gibt es in deinem Land für einen Feiertag, der auf einen Sonntag fällt, am Montag frei? Schreib zwei Sätze und schick sie ein.'),
    ('E VOCÊ? · 说说你自己', 'E VOCÊ? · UND DU?'),
    ('OS HORÁRIOS DO DOMINGO 15 · 周日时间表', 'OS HORÁRIOS DO DOMINGO 15 · ZEITPLAN FÜR SONNTAG, DEN 15.'),
    ('Um país, vários relógios · 一个国家，几个时区', 'Um país, vários relógios · Ein Land, mehrere Zeitzonen'),
    ('周日 12 点开门', 'Einlass sonntags ab 12 Uhr'),
    ('13:30 开考', 'Prüfungsbeginn 13:30 Uhr'),
    ('EXERCÍCIOS · 第 2 版练习', 'EXERCÍCIOS · ÜBUNGEN SEITE 2'),
    ('答案见第 8 版 · 题目可跨级混排，按题号找答案', 'Antworten auf Seite 8 · Niveaus gemischt — Antworten nach Nummer suchen'),
    ('读第 2 版文章，选出正确答案。', 'Lies Seite 2 und wähle die richtige Antwort.'),
    ('假日落在周日，周一不补休', 'Der Feiertag fällt auf einen Sonntag, montags gibt es keinen Ausgleich'),
    # P7-clinic/.text.md variant of the line above: the source carries a trailing 。 (F-2/F-3).
    ('假日落在周日，周一不补休。', 'Der Feiertag fällt auf einen Sonntag, montags gibt es keinen Ausgleich.'),
    ('确认卡显示考试地点', 'Die Bestätigungskarte zeigt den Prüfungsort'),
    ('巴西没有夏令时，钟表不动', 'Brasilien hat keine Sommerzeit: Die Uhren werden nicht umgestellt'),
    ('补全动词的现在时形式。', 'Ergänze die Präsensform des Verbs.'),
    ('用第 1、2 版的数字填空。', 'Ergänze mit den Zahlen von Seite 1 und 2.'),
    ('12 点到 13 点 = 1 小时', '12 bis 13 Uhr = 1 Stunde'),
    ('13:30 至 18:30 = 5 小时', '13:30 bis 18:30 Uhr = 5 Stunden'),
    ('5×60 = 300 分钟', '5×60 = 300 Minuten'),
    ('proclamação=宣布一个变化 b', 'proclamação = eine Veränderung ankündigen (b)'),
    ('feriado=法律规定的休息日 c', 'feriado = ein gesetzlich festgelegter Ruhetag (c)'),
    ('natureza=生命、物理与化学的科学 d', 'natureza = die Wissenschaft von Leben, Physik und Chemie (d)'),
    ('matemática=数字与图形的科学 a', 'matemática = die Wissenschaft von Zahlen und Formen (a)'),
    ('把词和释义配对', 'Ordne die Wörter den Bedeutungen zu'),
]
REPL += [
    # P3
    ('a monarquia 君主制 · a república 共和国 · o marechal 元帅 · o exílio 流亡 · o governo 政府 · a lei 法律。', 'a monarquia = Monarchie · a república = Republik · o marechal = Marschall · o exílio = Exil · o governo = Regierung · a lei = Gesetz.'),
    ('在你的国家，有纪念共和国建立的假日吗？写两句寄来。', 'Gibt es in deinem Land einen Feiertag, der an die Gründung der Republik erinnert? Schreib zwei Sätze und schick sie ein.'),
    ('EXERCÍCIOS · 第 3 版练习', 'EXERCÍCIOS · ÜBUNGEN SEITE 3'),
    ('读第 3 版文章，选出正确答案。', 'Lies Seite 3 und wähle die richtige Antwort.'),
    ('共和国宣言在 1889 年 11 月 15 日', 'Die Ausrufung der Republik war am 15. November 1889'),
    ('德奥多罗成为巴西第一任总统', 'Deodoro wurde der erste Präsident Brasiliens'),
    ('全国性假日，任何城市都不能改为工作日', 'Ein Feiertag für das ganze Land, den keine Stadt zum Arbeitstag machen darf'),
    ('2026 年假日落在周日', '2026 fällt der Feiertag auf einen Sonntag'),
    ('共和国里总统由选举产生、任期有限', 'In der Republik wird der Präsident gewählt und die Macht ist befristet'),
    ('用方框里的词填空。', 'Ergänze mit den Wörtern aus dem Kasten.'),
    ('monarquia = 君主制', 'monarquia = Monarchie'),
    ('república = 共和国', 'república = Republik'),
    ('marechal = 元帅', 'marechal = Marschall'),
    ('exílio = 流亡', 'exílio = Exil'),
    ('governo = 政府', 'governo = Regierung'),
    ('lei = 法律', 'lei = Gesetz'),
    ('用过去时（pretérito perfeito）补全。', 'Ergänze im Perfekt (pretérito perfeito).'),
    ('tomar 过去时 elas 形式：tomaram', 'tomar, Perfekt, elas-Form: tomaram'),
    ('acabar 过去时 ela 形式：acabou', 'acabar, Perfekt, ela-Form: acabou'),
    ('ser 过去时 ele 形式：foi', 'ser, Perfekt, ele-Form: foi'),
    ('assumir 过去时 ele 形式：assumiu', 'assumir, Perfekt, ele-Form: assumiu'),
    ('把词组成正确的句子。', 'Bring die Wörter in die richtige Reihenfolge.'),
    ('主语 + é + 表语', 'Subjekt + é + Ergänzung'),
    ('主语 + 动词 + 表语', 'Subjekt + Verb + Ergänzung'),
    ('主语 + 动词 + 宾语 + 时间', 'Subjekt + Verb + Objekt + Zeit'),
    # P4
    ('a ida 首回合 · a volta 次回合 · o gol 进球 · o pênalti 点球 · a pausa 休整期 · o amistoso 友谊赛。', 'a ida = das Hinspiel · a volta = das Rückspiel · o gol = das Tor · o pênalti = der Elfmeter · a pausa = die Pause · o amistoso = das Freundschaftsspiel.'),
    ('你在巴西杯支持哪支球队？谁能进决赛？写两句寄来。', 'Für welches Team bist du in der Copa do Brasil — und wer kommt ins Finale? Schreib zwei Sätze und schick sie ein.'),
    ('A SEMANA DO FUTEBOL · 足球周历', 'A SEMANA DO FUTEBOL · FUSSBALLWOCHE'),
    ('EXERCÍCIOS · 第 4 版练习', 'EXERCÍCIOS · ÜBUNGEN SEITE 4'),
    ('读第 4 版文章，选出正确答案。', 'Lies Seite 4 und wähle die richtige Antwort.'),
    ('首回合格雷米奥 2 比 0 战胜米内罗竞技', 'Im Hinspiel schlug Grêmio Atlético-MG mit 2:0'),
    ('帕尔梅拉斯 1 比 0 战胜瓦斯科，毛里西奥进球', 'Palmeiras schlug Vasco mit 1:0, Tor durch Maurício'),
    ('次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点', 'Das Rückspiel Atlético-MG × Grêmio ist am Samstag, den 7., um 18 Uhr'),
    ('决赛 12 月 6 日单场，在马内·加林查', 'Das Finale ist ein einziges Spiel am 6. Dezember, im Mané Garrincha'),
    ('第 35 轮本周只有一场：米拉索尔 × 米内罗竞技', 'Der 35. Spieltag hat diese Woche nur ein Spiel: Mirassol × Atlético-MG'),
    ('gol=射入球网的得分 b', 'gol = der Treffer ins Netz (b)'),
    ('ida=对决的第一场 d', 'ida = das erste Spiel eines Duells (d)'),
    ('volta=对决的第二场 a', 'volta = das zweite Spiel eines Duells (a)'),
    ('pênalti=十一米点的罚球 c', 'pênalti = der Schuss vom Elfmeterpunkt (c)'),
    ('用括号里正确的比较形式填空。', 'Ergänze die richtige Vergleichsform aus der Klammer.'),
    ('5 小时 < 5.5 小时：menos', '5 Stunden < 5,5 Stunden: menos'),
    ('把句子补全成过去时（pretérito perfeito）。', 'Vervollständige die Sätze im Perfekt (pretérito perfeito).'),
    ('vencer 过去时 ele 形式：venceu', 'vencer, Perfekt, ele-Form: venceu'),
    ('marcar 过去时 eles 形式：marcaram', 'marcar, Perfekt, eles-Form: marcaram'),
    ('marcar 过去时 ele 形式：marcou', 'marcar, Perfekt, ele-Form: marcou'),
    ('convocar 过去时 ele 形式：convocou', 'convocar, Perfekt, ele-Form: convocou'),
    ('ser 过去时复数：foram', 'ser, Perfekt, Plural: foram'),
    # P5
    ('1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）', '1. Confira o Cartão de Confirmação do Enem (prüfe deine Enem-Bestätigungskarte)'),
    ('2. Revise um pouco por dia: Natureza e Matemática（每天复习一点：自然科学与数学）', '2. Revise um pouco por dia: Natureza e Matemática (wiederhole jeden Tag ein bisschen: Naturwissenschaften und Mathematik)'),
    ('3. Durma bem na véspera da prova（考前一晚睡好）', '3. Durma bem na véspera da prova (schlaf in der Nacht vor der Prüfung gut)'),
    ('4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）', '4. Separe documento e caneta preta no dia anterior (lege Ausweis und schwarzen Stift am Vortag bereit)'),
    ('5. Domingo 15: chegue antes das 12h（周日 15 日：12 点前到达）', '5. Domingo 15: chegue antes das 12h (Sonntag, den 15.: komm vor 12 Uhr)'),
    ('a natureza 自然科学 · a matemática 数学 · a maratona 突击马拉松 · a véspera 前夕 · comparar 比较价格 · a cabeça 头脑、状态。', 'a natureza = Naturwissenschaften · a matemática = Mathematik · a maratona = der Lernmarathon · a véspera = der Vorabend · comparar = Preise vergleichen · a cabeça = der Kopf, die Verfassung.'),
    ('重要考试前一晚，你是复习到很晚还是早睡？写两句寄来。', 'Am Abend vor einer wichtigen Prüfung: lernst du bis spät oder gehst du früh schlafen? Schreib zwei Sätze und schick sie ein.'),
    ('EXERCÍCIOS · 第 5 版练习', 'EXERCÍCIOS · ÜBUNGEN SEITE 5'),
    ('读第 5 版文章，选出正确答案。', 'Lies Seite 5 und wähle die richtige Antwort.'),
    ('最后一周在 11 月 15 日周日结束', 'Die letzte Woche endet am Sonntag, den 15. November'),
    ('每天复习一点', 'Jeden Tag ein bisschen wiederholen'),
    ('提前一天备好证件和黑笔', 'Ausweis und schwarzen Stift am Vortag bereitlegen'),
    ('黑五在 11 月 27 日', 'Black Friday ist am 27. November'),
    ('11 月 14 日周六巴西 × 日本 7:15', 'Am Samstag, den 14., Brasilien × Japan um 7:15 Uhr'),
    ('用方框里的词填空。注意：有的词要变成复数。', 'Ergänze mit den Wörtern aus dem Kasten. Achtung: Ein Wort muss in den Plural.'),
    ('última semana = 最后一周', 'última semana = die letzte Woche'),
    ('inscrito 配合复数：inscritos', 'inscrito steht im Plural: inscritos'),
    ('véspera = 前夕', 'véspera = der Vorabend'),
    ('maratona = 突击马拉松', 'maratona = der Lernmarathon'),
    ('local = 地点', 'local = der Ort'),
    ('separar 祈使式：separe', 'separar, Imperativ: separe'),
    ('用将来时（futuro do presente）补全。', 'Ergänze im Futur (futuro do presente).'),
    ('fazer 将来时 eles 不规则形式：farão', 'fazer, Futur, unregelmäßige eles-Form: farão'),
    ('mostrar 将来时：mostrará', 'mostrar, Futur: mostrará'),
    ('sair 将来时复数：sairão', 'sair, Futur, Plural: sairão'),
    ('chegar 将来时：chegará', 'chegar, Futur: chegará'),
    ('错：考前突击不是好计划，每天复习一点才好', 'Falsch: Pauken am Vorabend ist kein guter Plan — jeden Tag ein bisschen ist besser'),
    ('对：13:30 至 18:30', 'Richtig: 13:30 bis 18:30 Uhr'),
    # P6
    ('os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。', 'os portões = die Tore · a segunda chamada = ein zweiter Termin, ein zweiter Einlass · conferir = prüfen · a correria = die Hektik.'),
    ('O DOMINGO 15 EM NÚMEROS · 11 月 15 日的数字 (horários oficiais do Inep)', 'O DOMINGO 15 EM NÚMEROS · DIE ZAHLEN DES 15. NOVEMBER (offizielle Inep-Zeiten)'),
    ('EXERCÍCIOS · 第 6 版练习', 'EXERCÍCIOS · ÜBUNGEN SEITE 6'),
    ('看上面两张图，选出正确答案。', 'Schau dir die zwei Grafiken oben an und wähle die richtige Antwort.'),
    ('大门开放 60 分钟', 'Die Tore bleiben 60 Minuten offen'),
    ('关门到开考之间等 30 分钟', 'Die Wartezeit zwischen Schließung und Prüfung beträgt 30 Minuten'),
    ('考试 300 分钟', 'Die Prüfung dauert 300 Minuten'),
    ('中午到 18:30 = 6 个半小时', 'Mittag bis 18:30 Uhr = sechseinhalb Stunden'),
    ('图表数字是 Inep 官方时间', 'Die Zahlen der Grafik sind offizielle Inep-Zeiten'),
    ('高考分 8 日和 15 日两个周日', 'Der Enem läuft an zwei Sonntagen: am 8. und am 15.'),
    ('13 点后到场不得入内', 'Wer nach 13 Uhr kommt, kommt nicht hinein'),
    ('根据句子意思，补全正确的动词形式。', 'Ergänze die richtige Verbform für jeden Satz.'),
    ('将来时：começará', 'Futur: começará'),
    ('quem + 虚拟式将来：chegar', 'quem + Futur des Konjunktivs: chegar'),
    ('现在时：fecham', 'Präsens: fecham'),
    ('现在时：pede', 'Präsens: pede'),
    ('用方框里的词填空：portões · segunda chamada · local · conferir', 'Ergänze mit den Wörtern aus dem Kasten: portões · segunda chamada · local · conferir'),
    ('portões = 大门', 'portões = die Tore'),
    ('segunda chamada = 补考、第二次入场', 'segunda chamada = ein zweiter Termin, ein zweiter Einlass'),
    ('祈使式：confira', 'Imperativ: confira'),
    # P7
    ('提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro', 'Fragen: que horas (wie spät) + Verb; onde fica fragt nach dem Ort; conferir ist in der eu-Form unregelmäßig: confiro.'),
    ('conferir：eu → confiro（不规则）', 'conferir: eu → confiro (unregelmäßig)'),
    ('onde 问地点', 'onde fragt nach dem Ort'),
    ('讲一周的事用过去时（pretérito perfeito）；vencer 规则（venceu）；marcar/chegar/dormir 的过去时注意重音。', 'Um die Woche zu erzählen, benutzen wir das Perfekt (pretérito perfeito); vencer ist regelmäßig (venceu); achte auf die Betonung im Perfekt von marcar, chegar und dormir.'),
    ('vencer 过去时：venceu', 'vencer, Perfekt: venceu'),
    ('marcar 过去时：marcou', 'marcar, Perfekt: marcou'),
    ('chegar 过去时：chegou', 'chegar, Perfekt: chegou'),
    ('venceram 是 vencer 的过去时复数', 'venceram ist das Perfekt, Plural, von vencer'),
    ('quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。', 'Nach quando, se und quem steht der Futur des Konjunktivs: tiver, for, chegar — die Grammatik der Sonntagshypothesen.'),
    ('quem + 虚拟式将来：tiver', 'quem + Futur des Konjunktivs: tiver'),
    ('quando + 虚拟式将来：chegar', 'quando + Futur des Konjunktivs: chegar'),
    ('se + ser 的虚拟式将来：for', 'se + Futur des Konjunktivs von ser: for'),
    ('quando + 未来 → 虚拟式将来 for', 'quando + Zukunft → Futur des Konjunktivs for'),
    ('高考用黑笔，蓝笔不行。', 'Nur schwarzer Stift — blau geht nicht.'),
    ('13 点关门，13:30 到就晚了。', 'Die Tore schließen um 13 Uhr — 13:30 Uhr ist zu spät.'),
    ('15 日考试 18:30 结束，19 点是 8 日的时间。', 'Am 15. endet die Prüfung um 18:30 Uhr; 19 Uhr gehört zum 8.'),
    ('ERROS COMUNS · 常见错误', 'ERROS COMUNS · FEHLER'),
    ('proclamação = 宣布；1889 年君主制结束、共和国开始。', 'proclamação = Ausrufung; 1889 endete die Monarchie und die Republik begann.'),
    ('A PALAVRA · 本周生词', 'A PALAVRA · WORT DER WOCHE'),
    ('编辑部说明：上期（VOL.2）承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期（VOL.4）。', 'Anmerkung: Die versprochenen Briefe und Texte kamen nicht an – das Beispiel bleibt, das Versprechen geht an VOL.4 weiter.'),
    ('编辑部示例，非真实来信。真实来信请寄编辑部，下期见！', 'Redaktionsbeispiel – kein echter Brief.'),
    ('FRASES DA SEMANA · 本周金句（逐字摘自本期文章）', 'FRASES DA SEMANA · SÄTZE DER WOCHE (wörtlich aus dieser Ausgabe)'),
    ('两个周日、一个假日：巴西迎来高考第二天。', 'Zwei Sonntage, ein Feiertag: Brasilien schreibt den zweiten Enem-Tag.'),
    ('考试和假日在同一天到来。', 'Prüfung und Feiertag kommen am selben Tag.'),
    ('假日不改变时钟。', 'Der Feiertag stellt die Uhr nicht um.'),
    ('君主制结束了。', 'Die Monarchie ist zu Ende.'),
    ('谁能进巴西杯决赛？', 'Wer kommt ins Finale der Copa do Brasil?'),
    ('睡得好，记得牢。', 'Wer gut schläft, erinnert sich besser.'),
    ('先做容易的，再做难的。', 'Erst die leichten, dann die schweren.'),
    ('核对确认卡、睡好、早到。', 'Karte prüfen, gut schlafen, früh kommen.'),
    ('A PRÓXIMA SEMANA · 下期预告 (VOL.4)', 'A PRÓXIMA SEMANA · NÄCHSTE WOCHE (VOL.4)'),
    # P8
    ('第 2 天在 11 月 15 日', 'Tag 2 ist am 15. November'),
    ('第 1 天在 11 月 8 日', 'Tag 1 ist am 8. November'),
    ('确认卡是高考的文件', 'Die Bestätigungskarte gehört zum Enem'),
    ('共和国宣言日在 11 月 15 日', 'Der Tag der Ausrufung der Republik ist am 15. November'),
    ('瓦斯科 × 帕尔梅拉斯次回合在 8 日', 'Das Rückspiel Vasco × Palmeiras ist am 8.'),
    ('第二天共 90 道题', 'Tag 2 hat insgesamt 90 Fragen'),
    ('考试时长 5 小时', 'Die Prüfung dauert 5 Stunden'),
    ('米内罗竞技 × 格雷米奥次回合在 MRV 竞技场', 'Das Rückspiel Atlético-MG × Grêmio ist in der Arena MRV'),
    ('第 35 轮本周只有一场，在 14 日', 'Der 35. Spieltag hat diese Woche nur ein Spiel, am 14.'),
    ('共和国宣言在 1889 年', 'Die Ausrufung der Republik war 1889'),
    ('11.11 是促销日', 'Der 11.11. ist der Tag der Aktionen'),
    ('300 是考试的分钟数', '300 ist die Prüfungsdauer in Minuten'),
    ('德奥多罗是第一任总统', 'Deodoro war der erste Präsident'),
    ('玛丽娜住在圣保罗', 'Marina wohnt in São Paulo'),
    ('她每天复习一点自然科学', 'Sie wiederholt jeden Tag ein bisschen Naturwissenschaften'),
    ('前一晚她备好证件和黑笔、早睡', 'Am Vorabend legt sie Ausweis und schwarzen Stift bereit und geht früh schlafen'),
    ('她 11:30 到达考场', 'Sie kommt um 11:30 Uhr am Prüfungsort an'),
    ('时间词在前', 'Das Zeitwort steht vorn'),
    ('主语 + 动词 + 宾语 + 地点', 'Subjekt + Verb + Objekt + Ort'),
    ('疑问词组在句首', 'Die Fragephrase steht am Satzanfang'),
    ('主语 + 动词 + 宾语', 'Subjekt + Verb + Objekt'),
    ('11 月 15 日周日是高考的第二天。', 'Sonntag, der 15. November, ist der zweite Tag des Enem.'),
    ('对照第 6 版标题', 'Siehe die Überschrift auf Seite 6'),
    ('周日前核对确认卡。', 'Prüfe die Karte vor Sonntag.'),
    ('Confira = 请核对', 'Confira = prüfen, bestätigen'),
    ('“假日落在周日。” → ___', '„Der Feiertag fällt auf einen Sonntag.“ → ___'),
    ('虚拟式将来 chegar + 祈使 apresente', 'Futur des Konjunktivs chegar + Imperativ apresente'),
    ('你到达时，请出示带照片的证件。 → ___', 'Wenn du ankommst, zeig bitte deinen Ausweis mit Foto. → ___'),
    ('proclamação=宣布一个变化 b', 'proclamação = eine Veränderung ankündigen (b)'),
    ('portão=考场入口 d', 'portão = der Eingang zum Prüfungsort (d)'),
    ('república=1889 年后的国家形式 a', 'república = die Staatsform nach 1889 (a)'),
    ('segunda chamada=关门后的再入场（高考没有） c', 'segunda chamada = Wiedereinlass nach Schließung (gibt es beim Enem nicht) (c)'),
    ('documento com foto 带照片的证件', 'documento com foto = Ausweis mit Foto'),
    ('seção = 考场分区（房间）', 'seção = der Prüfungsraum (Abschnitt)'),
    ('大门 13 点关闭', 'Die Tore schließen um 13 Uhr'),
    ('考试 18:30 结束', 'Die Prüfung endet um 18:30 Uhr'),
    ('obrigado = 谢谢', 'obrigado = danke'),
    ('写作题（无唯一答案）；范文（{NWORDS} 词）见下。', 'Schreibaufgabe (keine einzige richtige Antwort); der Mustertext ({NWORDS} Wörter) steht unten.'),
    ('（开放题，范文如下）', '(offene Aufgabe — Mustertext unten)'),
    ('范文见本版 H 区（{NWORDS} 词）', 'Siehe den Mustertext in Abschnitt H dieser Seite ({NWORDS} Wörter)'),
    ('RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可', 'RESPOSTAS · LÖSUNGEN — nach Seiten geordnet; such deine Nummer'),
    ('每题附一句中文简析 · 带 ✓ 的为范文题', 'Eine kurze Notiz pro Antwort · ✓ = die Schreibaufgabe'),
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

# ---------- 5. disclosure rename + layout tweaks (EN precedent) ----------
t = load('content7.py')
assert t.count('disc_cn') == 3, f"content7.py disc_cn count {t.count('disc_cn')}"
t = t.replace('disc_cn', 'disc_de')
old_wh = 'len(wrap("proclamação = Ausrufung; 1889 endete die Monarchie und die Republik begann.", "sans", False, 20, CW - 44)) * 29 + 20'
assert t.count(old_wh) == 1, 'word-box pad line not found'
t = t.replace(old_wh, 'len(wrap("proclamação = Ausrufung; 1889 endete die Monarchie und die Republik begann.", "sans", False, 20, CW - 44)) * 29 + 30')
assert t.count(')) * 29 + 35') == 1, 'letters-box pad line not found'
t = t.replace(')) * 29 + 35', ')) * 29 + 22')
t = line_replace(t, 'fy = max(1712,', 'fy = max(1712, ly + lh + 30)', 'content7.py')
t = line_replace(t, 'cyq = fy + 66', '    cyq = fy + 66 + (i % 4) * 94', 'content7.py')
save('content7.py', t)

t = load('content8.py')
t = line_replace(t, 'af.para(txt, 13.5',
    '        af.para(txt, 13, lh=1.12, gap=0.5, split=False)',
    'content8.py')
save('content8.py', t)

t = load('content12.py')
old_box = '    ("90 — as questões do dia 15: 45 + 45 (90 Fragen: 45 + 45)", "serif", False, INK, 20, 1.35),\n])'
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
