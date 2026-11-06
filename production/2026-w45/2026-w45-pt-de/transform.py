# -*- coding: utf-8 -*-
"""PT x DE fan-out transform for W45 (VOL.2).

Run ONCE on a fresh copy of hidden_files/weekly-report-w45-pt-build:
  1. cp -r weekly-report-w45-pt-build -> weekly-report-w45-pt-de-build
     (excluding __pycache__)
  2. python3 transform.py   (repoints OUT/BASE/PDF names + rewrites ONLY
     the explanation layer from Chinese into German; Portuguese text is
     never touched — every replacement below is a Chinese-containing
     literal, a bilingual furniture line, or a P8 translation re-aim)
  3. <tools/venv>/python run.py && <tools/venv>/python render.py

Rules baked in (W43 PT x DE shipped precedent):
  - gloss prefix "HINWEIS · " (tables.json DE column, W43 SVG-verified)
  - badge replaces the P1 strapline in place at y=372, 19pt bold BRICK
  - edition line 40pt -> 34pt (German line is longer)
  - footers: tables.json DE column with VOL.2
  - P8 separator stays "— PÁGINA {pg} —" (W43 shipped SVG precedent,
    NOT the tables.json SEITE form — deviation documented in WEEKLY-KIT.md)
  - exercise `typ` registry strings (e.g. "单选") are NEVER rendered
    (bslib4 ex() prints only level/number/instr/body; P8 prints key/note
    and checks type == "写作" for the writing item) — left untouched
    exactly as in the W43 PT x DE build
  - P8 notes carry NO parentheses at all (avoids the p8.py paren-branch
    extraction artifact seen with trailing ASCII paren groups in NL x DE)
  - space before every parenthesis in visible German text (W43 rule)
  - P8 translation re-aims (W43 KIT §4 pattern): 137/138 PT->DE keys;
    139/140 stems DE->PT with Portuguese keys byte-identical; 150
    writing apparatus in German, model text untouched
  - P7 readers' corner: Portuguese disclosure sentence verbatim (frozen);
    Chinese notes -> German; the German note carries the EXPLICIT
    invitation (imperative + publication promise in VOL.3)
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (old, new) — applied to every .py file listed in FILES unless noted.
# All `old` strings contain Chinese or are bilingual furniture lines;
# no Portuguese-only literal appears here (frozen layer untouched).
REPLACEMENTS = [
    # ---- bslib4 furniture ----
    ("A Lucerna · 葡萄牙语周报 VOL.2 · LUCERNA PORTUGUESE WEEKLY",
     "A Lucerna · PORTUGIESISCHE WOCHENZEITUNG VOL.2 · TEXT AUF PORTUGIESISCH · ERKLÄRUNGEN AUF DEUTSCH"),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"Seite {n} von {total}"'),
    ('("译注｜" + s', '("HINWEIS · " + s'),
    # ---- P1 top furniture ----
    ("TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语",
     "TODA SEMANA EM PORTUGUÊS · DAS PORTUGIESISCH, DAS BRASILIEN LIEST"),
    ('p.text(975, 330, "葡 萄 牙 语 周 报 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE", 40,',
     'p.text(975, 330, "PORTUGIESISCHE WOCHENZEITUNG · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE", 34,'),
    ('p.text(975, 372, "O JORNAL SEMANAL PARA APRENDER — O BRASIL DE VERDADE, EM PORTUGUÊS, DO BRASIL", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "PORTUGIESISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER", 19, "sans", True, BRICK, anchor="middle")'),
    ("全国高考周", "DIE ENEM-WOCHE"),
    ("11 月 2 日亡灵节连休 · 11 月 8 日高考第一天",
     "2. Nov.: Finados und langes Wochenende · 8. Nov.: erster Prüfungstag"),
    ("A NOTÍCIA · 头条", "A NOTÍCIA · SCHLAGZEILE"),
    ("讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。",
     "HINWEIS · feriadão = langes Feiertagswochenende · o portão = Eingangstor · a redação = Aufsatz · revisar = wiederholen."),
    ("A SEMANA EM NÚMEROS · 数字", "A SEMANA EM NÚMEROS · ZAHLEN"),
    ("12h — os portões abrem no domingo 8（周日 12 点开门）",
     "12h — os portões abrem no domingo 8 (Sonntag, 12 Uhr öffnen die Tore)"),
    ("13h — os portões fecham（13 点关门，过时不入）",
     "13h — os portões fecham (13 Uhr: nachher kein Einlass mehr)"),
    ("13h30–19h — a prova do dia 8（考试 13:30 至 19:00）",
     "13h30–19h — a prova do dia 8 (Prüfung 13:30 bis 19:00 Uhr)"),
    ("5h30 — a duração da prova do dia 8（考试时长 5 小时半）",
     "5h30 — a duração da prova do dia 8 (Prüfungsdauer: fünfeinhalb Stunden)"),
    ("AGORA VOCÊ · 即学即练", "AGORA VOCÊ · SIE SIND DRAN"),
    ("feriadão = 连休长周末", "feriadão = langes Feiertagswochenende"),
    ("portões = 大门（考场大门）", "portões = Eingangstore am Prüfungsort"),
    ("redação = 作文", "redação = Aufsatz"),
    ("13h30 开考（巴西利亚时间）", "13h30: Prüfungsbeginn, Brasília-Zeit"),
    ("19h 结束", "19h: Prüfungsende"),
    ("revisar 现在时 eles 形式：revisam", "revisar, Präsens eles: revisam"),
    ("迟到不得入内：13 点后关门", "Zu spät: kein Einlass nach 13 Uhr"),
    ("NESTA EDIÇÃO · 本期目录", "NESTA EDIÇÃO · INHALT"),
    ("“连休”：假期连着周末，一共三天。", "„Feriadão“ = langes Wochenende, drei Tage."),
    ("EM POUCAS PALAVRAS · 快讯", "EM POUCAS PALAVRAS · IN KÜRZE"),
    ("QUIZ RELÂMPAGO · 闪电问答", "QUIZ RELÂMPAGO · BLITZQUIZ"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Titelseite lesen, richtig antworten · Lösungen auf Seite 8"),
    ("次回合在 7 日和 8 日", "Die Rückspiele sind am 7. und 8. November"),
    ("PARA NÃO ERRAR · 口诀", "PARA NÃO ERRAR · MERKSATZ"),
    # ---- shared exercise furniture (all pages) ----
    ("EXERCÍCIOS · 第 2 版练习", "EXERCÍCIOS · ÜBUNGEN · SEITE 2"),
    ("EXERCÍCIOS · 第 3 版练习", "EXERCÍCIOS · ÜBUNGEN · SEITE 3"),
    ("EXERCÍCIOS · 第 4 版练习", "EXERCÍCIOS · ÜBUNGEN · SEITE 4"),
    ("EXERCÍCIOS · 第 5 版练习", "EXERCÍCIOS · ÜBUNGEN · SEITE 5"),
    ("EXERCÍCIOS · 第 6 版练习", "EXERCÍCIOS · ÜBUNGEN · SEITE 6"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案", "Lösungen auf Seite 8 · gemischte Stufen — nach Nummern suchen"),
    ('instr="填空"', 'instr="Ausfüllen"'),
    ('instr="造句"', 'instr="Sätze bilden"'),
    ('instr="翻译"', 'instr="Übersetzen"'),
    ('instr="写作"', 'instr="Schreiben"'),
    ('instr="判断"', 'instr="Wahr oder falsch?"'),
    ('instr="把词和释义配对"', 'instr="Zuordnen"'),
    # ---- P2 ----
    ("VIDA · 生活", "VIDA · LEBEN"),
    ("NÍVEL A2 · Finados e revisão: o feriadão do Brasil",
     "NÍVEL A2 · Finados e revisão: o feriadão do Brasil · Finados und Wiederholung: das lange Wochenende in Brasilien"),
    ("o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。",
     "o feriadão = langes Feiertagswochenende · o cemitério = Friedhof · a vela = Kerze · o crisântemo = Chrysantheme · a missa = Messe · conferir = prüfen, nachsehen."),
    ("E VOCÊ? · 说说你自己", "E VOCÊ? · UND SIE?"),
    ("在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。",
     "Gibt es in Ihrem Land einen Tag, an dem man der Toten gedenkt? Was tun die Familien an diesem Tag? Schreiben Sie zwei Sätze."),
    ("OS HORÁRIOS DO DOMINGO 8 · 周日时间表", "OS HORÁRIOS DO DOMINGO 8 · DIE ZEITEN AM SONNTAG"),
    ("Um país, vários relógios · 一个国家，几个时区", "Um país, vários relógios · Ein Land, viele Uhren"),
    ("周日 12 点开门", "Sonntag 12 Uhr: öffnen"),
    ("13 点关门", "Die Tore schließen um 13 Uhr"),
    ("13:30 开考", "13:30 Uhr: Beginn"),
    ("19:00 结束", "19 Uhr: Ende"),
    ("读第 2 版文章，选出正确答案。", "Lesen Sie Seite 2 und wählen Sie die richtige Antwort."),
    ("连休从 10 月 31 日到 11 月 2 日", "Feriadão: 31. Oktober bis 2. November"),
    ("亡灵节家人们去墓园献花", "An Finados besuchen die Familien die Friedhöfe und bringen Blumen"),
    ("确认卡显示考试地点", "Die Bestätigungskarte zeigt den Prüfungsort"),
    ("巴西没有夏令时，钟表不动", "Brasilien hat keine Sommerzeit: Die Uhr bleibt"),
    ("补全动词的现在时形式。", "Ergänzen Sie die Verben im Präsens."),
    ("conferir：ele → confere", "conferir: ele confere"),
    ("abrir：ele → abre", "abrir: ele abre"),
    ("levar：nós → levamos", "levar: nós levamos"),
    ("começar：ela → começa", "começar: ela começa"),
    ("ser 现在时 ela 形式：é", "ser, Präsens ela: é"),
    ("用第 1、2 版的数字填空。", "Ergänzen Sie die Zahlen von Seite 1 und 2."),
    ("12 点到 13 点 = 1 小时", "12 bis 13 Uhr = 1 Stunde"),
    ("13:30 至 19:00 = 5 个半小时", "13:30 bis 19:00 Uhr = fünfeinhalb Stunden"),
    ("5×60 + 30 = 330 分钟", "5 × 60 + 30 = 330 Minuten"),
    ("31 日、1 日、2 日 = 3 天", "31., 1. und 2. = 3 Tage"),
    ("feriadão=连着周末的假期 c", "feriadão = Feiertag am Wochenende: c"),
    ("cemitério=墓碑所在的地方 b", "cemitério = Ort der Gräber: b"),
    ("vela=点亮纪念的物品 d", "vela = Gegenstand, der in Erinnerung angezündet wird: d"),
    ("crisântemo=亡灵节带去的花 a", "crisântemo = Blume, die man an Finados mitbringt: a"),
    # ---- P3 ----
    ("CULTURA · 文化", "CULTURA · KULTUR"),
    ("A2 → B1 · Finados: o dia da memória · 亡灵节：怀念的日子",
     "A2 → B1 · Finados: o dia da memória · Finados: der Tag der Erinnerung"),
    ("o túmulo 墓碑 · a flor 花 · acender 点燃 · rezar 祈祷 · o silêncio 寂静 · a lembrança 怀念。",
     "o túmulo = Grab · a flor = Blume · acender = anzünden · rezar = beten · o silêncio = Stille · a lembrança = Erinnerung."),
    ("在你的文化里，人们怎样怀念逝者？写两句寄来。",
     "Wie gedenkt man in Ihrer Kultur der Toten? Schreiben Sie zwei Sätze."),
    ("读第 3 版文章，选出正确答案。", "Lesen Sie Seite 3 und wählen Sie die richtige Antwort."),
    ("亡灵节是怀念与安静的日子", "Finados ist der Tag der Erinnerung und der Stille"),
    ("家人们带花去墓园，主要是菊花", "Die Familien bringen Blumen auf die Friedhöfe, vor allem Chrysanthemen"),
    ("教堂和墓园整天都有弥撒", "In Kirchen und auf Friedhöfen gibt es den ganzen Tag Messen"),
    ("万圣节在 10 月 31 日周六", "Halloween war am Samstag, dem 31. Oktober"),
    ("怀念是继续亲近的方式", "Erinnern heißt, weiterhin nahe zu bleiben"),
    ("用方框里的词填空。", "Setzen Sie die Wörter aus dem Kasten ein."),
    ("túmulo = 墓碑", "túmulo = Grab"),
    ("vela = 蜡烛", "vela = Kerze"),
    ("crisântemo = 菊花", "crisântemo = Chrysantheme"),
    ("missa = 弥撒", "missa = Messe"),
    ("silêncio = 寂静", "silêncio = Stille"),
    ("lembrança = 怀念", "lembrança = Erinnerung"),
    ("用过去时（pretérito perfeito）补全。", "Ergänzen Sie im Pretérito Perfeito."),
    ("visitar 过去时 elas 形式：visitaram", "visitar, Vergangenheit elas: visitaram"),
    ("levar 过去时 elas 形式：levaram", "levar, Vergangenheit elas: levaram"),
    ("ser 过去时 ele 形式：foi", "ser, Vergangenheit ele: foi"),
    ("viver 过去时 ele 形式：viveu", "viver, Vergangenheit ele: viveu"),
    ("把词组成正确的句子。", "Bilden Sie aus den Wörtern Sätze."),
    ("主语 + é + 表语", "Subjekt + é + Prädikat"),
    ("主语 + 动词 + 宾语 + 地点", "Subjekt + Verb + Objekt + Ort"),
    ("主语 + 动词 + 宾语", "Subjekt + Verb + Objekt"),
    # ---- P4 ----
    ("ESPORTE · 体育", "ESPORTE · SPORT"),
    ("NÍVEL B1 · O futebol da semana · 足球之周", "NÍVEL B1 · O futebol da semana · Die Fußballwoche"),
    ("a ida 首回合 · a volta 次回合 · o finalista 决赛球队 · a decisão 决战 · a rodada 轮次。",
     "a ida = Hinspiel · a volta = Rückspiel · o finalista = Finalist · a decisão = Entscheidung · a rodada = Spieltag, Runde."),
    ("你在巴西杯支持哪支球队？写两句寄来。", "Für welches Team sind Sie in der Copa do Brasil? Schreiben Sie zwei Sätze."),
    ("A SEMANA DO FUTEBOL · 足球周历", "A SEMANA DO FUTEBOL · DIE FUSSBALLWOCHE"),
    ("读第 4 版文章，选出正确答案。", "Lesen Sie Seite 4 und wählen Sie die richtige Antwort."),
    ("次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点", "Rückspiel Atlético-MG × Grêmio: Samstag, 7., 18 Uhr"),
    ("瓦斯科 × 帕尔梅拉斯次回合在周日 8 日 17 点，圣雅努阿里奥",
     "Rückspiel Vasco × Palmeiras: Sonntag, 8., 17 Uhr, São Januário"),
    ("首回合在 11 月 1 日周日", "Die Hinspiele waren am Sonntag, dem 1. November"),
    ("第 34 轮周一到周五每天都有比赛", "Die 34. Runde hat von Montag bis Freitag jeden Tag ein Spiel"),
    ("两回合总比分胜者进决赛", "Ins Finale kommt, wer beide Spiele zusammen gewinnt"),
    ("finalista=进决赛的球队 b", "finalista = Finalist: b"),
    ("ida=对决的第一场 c", "ida = erstes Spiel eines Duells: c"),
    ("volta=对决的第二场 a", "volta = zweites Spiel eines Duells: a"),
    ("rodada=一轮比赛 d", "rodada = Spieltag einer Meisterschaft: d"),
    ("用括号里正确的比较形式填空。", "Setzen Sie die richtige Vergleichsform ein."),
    ("次回合决定决赛名额：mais", "Die Volta entscheidet über das Finale: mais"),
    ("18 > 16：mais", "18 > 16: mais"),
    ("17 < 18：mais cedo", "17 < 18: mais cedo"),
    ("第 34 轮周一到周五都有比赛：mais", "Die 34. Runde geht von Montag bis Freitag: mais"),
    ("把句子补全成过去时（pretérito perfeito）。", "Vervollständigen Sie im Pretérito Perfeito."),
    ("ser 过去时复数：foram", "ser, Vergangenheit Plural: foram"),
    ("receber 过去时 ele 形式：recebeu", "receber, Vergangenheit ele: recebeu"),
    ("começar 过去时 ela 形式：começou", "começar, Vergangenheit ela: começou"),
    ("chegar 过去时 eles 形式：chegaram", "chegar, Vergangenheit eles: chegaram"),
    # ---- P5 ----
    ("JOVENS · 青年", "JOVENS · JUGEND"),
    ("NÍVEL B1 · A reta final dos jovens · 冲刺周：年轻人的最后一周",
     "NÍVEL B1 · A reta final dos jovens · Der Endspurt der Jugend"),
    ("1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）",
     "1. Confira o Cartão de Confirmação do Enem (Enem-Bestätigungskarte prüfen)"),
    ("2. Revise um pouco por dia, sem maratona（每天复习一点，不搞突击）",
     "2. Revise um pouco por dia, sem maratona (jeden Tag etwas wiederholen, kein Marathon)"),
    ("3. Durma bem na véspera da prova（考前一晚睡好）",
     "3. Durma bem na véspera da prova (am Vorabend gut schlafen)"),
    ("4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）",
     "4. Separe documento e caneta preta no dia anterior (Ausweis und schwarzen Stift am Vortag bereitlegen)"),
    ("5. Domingo 8: chegue antes das 12h（周日 8 日：12 点前到达）",
     "5. Domingo 8: chegue antes das 12h (Sonntag, 8.: vor 12 Uhr da sein)"),
    ("a reta final 最后冲刺 · a véspera 前夕 · a maratona 突击马拉松 · separar 准备好 · a cabeça 头脑、状态。",
     "a reta final = Endspurt · a véspera = Vorabend · a maratona = Marathon, hier: pauken ohne Pause · separar = bereitlegen · a cabeça = Kopf, Verfassung."),
    ("重要考试前一晚，你的计划是复习还是休息？写两句寄来。",
     "Was ist Ihr Plan am Vorabend einer wichtigen Prüfung: wiederholen oder ausruhen? Schreiben Sie zwei Sätze."),
    ("读第 5 版文章，选出正确答案。", "Lesen Sie Seite 5 und wählen Sie die richtige Antwort."),
    ("冲刺周在 11 月 8 日周日结束", "Der Endspurt endet am Sonntag, dem 8. November"),
    ("每天复习一点", "Jeden Tag etwas wiederholen"),
    ("提前一天备好证件和黑笔", "Am Vortag Ausweis und schwarzen Stift bereitlegen"),
    ("第 2 天考自然科学与数学", "Tag 2: Naturwissenschaften und Mathematik"),
    ("11 月 3 日周二各州议会结束休会", "Dienstag, 3.: Die Landesparlamente kehren aus der Pause zurück"),
    ("用方框里的词填空。注意：有的词要变成复数。",
     "Setzen Sie die Wörter aus dem Kasten ein. Achtung: Einige müssen in den Plural."),
    ("reta final = 最后冲刺阶段", "reta final = Endspurt"),
    ("inscrito 配合复数：inscritos", "inscrito im Plural: inscritos"),
    ("véspera = 前夕", "véspera = Vorabend"),
    ("maratona = 突击马拉松", "maratona = pauken ohne Pause"),
    ("local = 地点", "local = Ort"),
    ("separar 祈使式：separe", "separar, Imperativ: separe"),
    ("用将来时（futuro do presente）补全。", "Ergänzen Sie im Futuro do Presente."),
    ("fazer 将来时 eles 不规则形式：farão", "fazer, Zukunft eles, unregelmäßig: farão"),
    ("mostrar 将来时：mostrará", "mostrar, Zukunft: mostrará"),
    ("sair 将来时复数：sairão", "sair, Zukunft Plural: sairão"),
    ("chegar 将来时：chegará", "chegar, Zukunft: chegará"),
    ("错：考前突击不是好计划，每天复习一点才好",
     "Falsch: Pauken am Vorabend ist kein guter Plan — lieber jeden Tag etwas"),
    ("对：13:30 至 19:00", "Richtig: 13:30 bis 19:00 Uhr"),
    # ---- P6 ----
    ("APROFUNDAMENTO · 深读", "APROFUNDAMENTO · VERTIEFUNG"),
    ("NÍVEL B2 · O Enem explicado · 高考详解", "NÍVEL B2 · O Enem explicado · Das Enem erklärt"),
    ("os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。",
     "os portões = Eingangstore · a segunda chamada = Nachprüfung, zweiter Einlass — beim Enem gibt es keinen · conferir = prüfen, nachsehen · a correria = Hetze, Eile."),
    ("O DOMINGO 8 EM NÚMEROS · 11 月 8 日的数字 (horários oficiais do Inep)",
     "O DOMINGO 8 EM NÚMEROS · DIE ZAHLEN DES 8. NOVEMBER (horários oficiais do Inep)"),
    ("看上面两张图，选出正确答案。", "Antworten zu den Grafiken oben — wählen Sie die richtige."),
    ("大门开放 60 分钟", "Die Tore sind 60 Minuten geöffnet"),
    ("关门到开考之间等 30 分钟", "Zwischen Schließung und Beginn: 30 Minuten Wartezeit"),
    ("考试 330 分钟", "Die Prüfung dauert 330 Minuten"),
    ("60 + 30 + 330 = 420", "60 + 30 + 330 = 420"),
    ("中午到 19 点 = 7 小时", "Von mittags bis 19 Uhr = 7 Stunden"),
    ("图表数字是 Inep 官方时间", "Die Zahlen im Diagramm sind offizielle Inep-Zeiten"),
    ("高考分 8 日和 15 日两个周日", "Das Enem hat zwei Sonntage: 8. und 15."),
    ("第 1 天考作文、语言与人文", "Tag 1: Aufsatz, Sprachen und Humanwissenschaften"),
    ("13 点后到场不得入内", "Wer nach 13 Uhr kommt, kommt nicht hinein"),
    ("根据句子意思，补全正确的动词形式。", "Ergänzen Sie die passende Verbform."),
    ("将来时：começará", "Zukunft: começará"),
    ("quem + 虚拟式将来：chegar", "quem + Futuro do Subjuntivo: chegar"),
    ("现在时：fecham", "Präsens: fecham"),
    ("现在时：pede", "Präsens: pede"),
    ("用方框里的词填空：portões · segunda chamada · local · conferir",
     "Setzen Sie die Wörter aus dem Kasten ein: portões · segunda chamada · local · conferir"),
    ("portões = 大门", "portões = Eingangstore"),
    ("segunda chamada = 补考、第二次入场", "segunda chamada = Nachprüfung, zweiter Einlass"),
    ("祈使式：confira", "Imperativ: confira"),
    # ---- P7 ----
    ("LÍNGUA · 语言", "LÍNGUA · SPRACHE"),
    ("聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具",
     "Im Fokus: Sprache · Três níveis, três ferramentas · Drei Stufen, drei Werkzeuge"),
    ("提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro",
     "Fragen bilden: que horas (wie viel Uhr) + Verb; onde fica fragt nach dem Ort. Conferir ist bei eu unregelmäßig: confiro."),
    ("conferir：eu → confiro（不规则）", "conferir: eu confiro, unregelmäßig"),
    ("conferir：você → confere", "conferir: você confere"),
    ("onde 问地点", "onde fragt nach dem Ort"),
    ("讲一周的事用过去时（pretérito perfeito）；revisar 规则（revisei）；chegar/dormir 的过去时注意重音。",
     "Die Woche erzählt man im Pretérito Perfeito; revisar ist regelmäßig (revisei); bei chegar und dormir auf den Akzent achten: chegou, dormiu."),
    ("revisar 过去时：revisei", "revisar, Vergangenheit: revisei"),
    ("chegar 过去时：chegou", "chegar, Vergangenheit: chegou"),
    ("dormir 过去时：dormiu", "dormir, Vergangenheit: dormiu"),
    ("chegaram 是 chegar 的过去时复数", "chegaram = Vergangenheit Plural von chegar"),
    ("quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。",
     "Nach quando, se und quem steht das Futuro do Subjuntivo: tiver, for, chegar — Hypothesen zum Sonntag."),
    ("quem + 虚拟式将来：tiver", "quem + Futuro do Subjuntivo: tiver"),
    ("quando + 虚拟式将来：chegar", "quando + Futuro do Subjuntivo: chegar"),
    ("se + ser 的虚拟式将来：for", "se + Futuro do Subjuntivo von ser: for"),
    ("quando + 未来 → 虚拟式将来 for", "quando + Zukunft → Futuro do Subjuntivo: for"),
    ("ERROS COMUNS · 常见错误", "ERROS COMUNS · HÄUFIGE FEHLER"),
    ("高考用黑笔，蓝笔不行。", "Nur schwarzer Stift — blau gilt nicht."),
    ("13 点关门，13:30 到就晚了。", "13 Uhr Schluss — 13:30 Uhr ist zu spät."),
    ("考前一夜突击没用，睡好才记得住。", "Kein Pauken nachts — Schlaf hilft mehr."),
    ("连休是 10 月 31 日到 11 月 2 日，共三天。", "Feriadão: 31. Oktober bis 2. November."),
    ("A PALAVRA · 本周生词", "A PALAVRA · WORT DER WOCHE"),
    ("feriadão = 连休长周末，共三天。", "feriadão = langes Feiertagswochenende."),
    ("编辑部示例，非真实来信。真实来信请寄编辑部，下期见！",
     "Beispiel der Redaktion. Schreiben Sie uns! Beste Briefe erscheinen in VOL.3."),
    ("编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。",
     "Anmerkung: Echte Briefe und beste Texte kamen bis Redaktionsschluss nicht an — Beispiel bleibt, Versprechen gilt für VOL.3."),
    ("FRASES DA SEMANA · 本周金句（逐字摘自本期文章）",
     "FRASES DA SEMANA · SÄTZE DER WOCHE (wörtlich aus dieser Ausgabe)"),
    ("从连休到考试：高考周。", "Vom langen Wochenende zur Prüfung: die Enem-Woche."),
    ("许多人旅行、探亲、去墓园献花。", "Viele reisen, besuchen die Familie und bringen Blumen auf den Friedhof."),
    ("亡灵节是怀念的日子。", "Finados ist der Tag der Erinnerung."),
    ("怀念是继续亲近的方式。", "Erinnern heißt, weiterhin nahe zu bleiben."),
    ("每一分值一个名次，每一球值一个故事。", "Jeder Punkt ist ein Platz wert, jedes Tor eine Geschichte."),
    ("睡得好，记得牢。", "Wer gut schläft, behält mehr."),
    ("先做容易的，再做难的。", "Zuerst die leichten Aufgaben, dann die schweren."),
    ("核对确认卡、睡好、早到。", "Karte prüfen, gut schlafen, früh da sein."),
    ("A PRÓXIMA SEMANA · 下期预告 (VOL.3)", "A PRÓXIMA SEMANA · NÄCHSTE AUSGABE (VOL.3)"),
    # ---- P8 ----
    ("AVALIAÇÃO E RESPOSTAS · 练习与答案", "AVALIAÇÃO E RESPOSTAS · TEST UND LÖSUNGEN"),
    ("第 8 版 · A grande prova da semana + todas as respostas",
     "SEITE 8 · A grande prova da semana + todas as respostas"),
    ("第 1 天在 11 月 8 日", "Tag 1 ist am 8. November"),
    # NOTE: the P8-A note "13:30 开考" shares its literal with the P2
    # time-box label and is translated by that earlier entry
    # ("13:30 Uhr: Beginn") — no separate P8 entry (it would MISS).
    ("亡灵节在 11 月 2 日", "Finados ist am 2. November"),
    ("瓦斯科 × 帕尔梅拉斯次回合在 8 日", "Rückspiel Vasco × Palmeiras am Sonntag, 8."),
    ("连休共 3 天", "Der Feriadão dauert 3 Tage"),
    ("考试时长 5 个半小时", "Die Prüfung am Tag 8 dauert fünfeinhalb Stunden"),
    ("第 2 天在 11 月 15 日", "Tag 2 ist am 15. November"),
    ("确认卡是高考的文件", "Die Bestätigungskarte gehört zum Enem"),
    ("米内罗竞技 × 格雷米奥次回合在 MRV 竞技场", "Rückspiel Atlético-MG × Grêmio in der Arena MRV"),
    ("第 34 轮周一到周五都有比赛", "Die 34. Runde geht von Montag bis Freitag"),
    ("亡灵节家人们带花", "An Finados bringen die Familien Blumen"),
    ("330 是考试的分钟数", "330 sind die Minuten der Prüfung"),
    ("亡灵节又称诸圣灵魂日", "Finados heißt auch Dia dos Fiéis Defuntos"),
    ("卢卡斯住在贝洛奥里藏特", "Lucas wohnt in Belo Horizonte"),
    ("连休里他休息并每天复习一点", "Im Feriadão ruht er aus, wiederholt täglich etwas"),
    ("前一晚他备好证件和黑笔、早睡", "Am Vorabend: Ausweis und Stift bereit, früh schlafen"),
    ("他 11 点到达考场", "Er kommt um 11 Uhr am Prüfungsort an"),
    ("时间词在前", "Zeitangabe zuerst"),
    ("疑问词组在句首", "Fragewort am Anfang"),
    # P8-E re-aims: 137/138 keys PT->DE; 139/140 stems DE->PT (keys frozen)
    ("11 月 8 日周日是高考的第一天。", "Sonntag, 8. November ist Tag 1 des Enem."),
    ("对照第 6 版标题", "vgl. Seite 6"),
    ("周日前核对确认卡。", "Prüfen Sie die Karte vor dem Sonntag."),
    ("Confira = 请核对", "confira = prüfen Sie"),
    ("“连休是 10 月 31 日到 11 月 2 日。” → ___",
     "„Der Feriadão geht vom 31. Oktober bis zum 2. November.“ → ___"),
    ("feriadão = 连休", "feriadão = langes Feiertagswochenende"),
    ("你到达时，请出示带照片的证件。 → ___",
     "„Wenn Sie ankommen, zeigen Sie bitte Ihren Ausweis mit Foto vor.“ → ___"),
    ("虚拟式将来 chegar + 祈使 apresente", "Futuro do Subjuntivo chegar + Imperativ apresente"),
    ("feriadão=连着周末的假期 b", "feriadão = Feiertag am Wochenende: b"),
    ("portão=考场入口 d", "portão = Eingang zum Prüfungsort: d"),
    ("reta final=考前最后一周 a", "reta final = letzte Woche vor der Prüfung: a"),
    ("segunda chamada=关门后的再入场（高考没有） c",
     "segunda chamada = kein Einlass nach Schluss: c"),
    ("documento com foto 带照片的证件", "documento com foto = Ausweis mit Foto"),
    ("seção = 考场分区（房间）", "seção = Prüfungsraum, Sektion"),
    ("大门 13 点关闭", "Die Tore schließen um 13 Uhr"),
    ("考试 13:30 开始", "Die Prüfung beginnt um 13:30 Uhr"),
    ("obrigado = 谢谢", "obrigado = danke"),
    ("写作题（无唯一答案）；范文（{NWORDS} 词）见下。", "Schreibaufgabe (offen); Mustertext ({NWORDS} Wörter) unten."),
    ("（开放题，范文如下）", "(offene Aufgabe — Mustertext unten)"),
    ("范文见本版 H 区（{NWORDS} 词）", "Mustertext in Bereich H auf dieser Seite ({NWORDS} Wörter)"),
    ("RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可",
     "RESPOSTAS · LÖSUNGEN — nach Seiten geordnet, nach Nummer suchen"),
    ("每题附一句中文简析 · 带 ✓ 的为范文题", "Jede Nummer mit kurzer deutscher Erklärung · ✓ = Aufgabe mit Mustertext"),
]

FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py"]


def main():
    # 0. idempotency guard: several new strings contain their old string
    #    as a prefix (P2 band appends the German half to the Portuguese
    #    sub) — a second run would duplicate them. Refuse if already done.
    for fn in FILES:
        s = open(os.path.join(HERE, fn), encoding="utf-8").read()
        if "PORTUGIESISCHE WOCHENZEITUNG" in s or "HINWEIS · " in s:
            print(f"ABORT: {fn} already transformed — start from a fresh core copy")
            return 2
    # 1. repoint outputs
    for fn in FILES + ["render.py"]:
        p = os.path.join(HERE, fn)
        s = open(p, encoding="utf-8").read()
        s2 = s.replace("weekly-report-w45-pt-core", "weekly-report-w45-pt-de")
        if fn == "render.py":
            s2 = s2.replace('"A-Lucerna-VOL2.pdf"', '"A-Lucerna-VOL2-DE.pdf"')
            s2 = s2.replace('"A-Lucerna-VOL2-web.pdf"', '"A-Lucerna-VOL2-DE-web.pdf"')
        if s2 != s:
            open(p, "w", encoding="utf-8").write(s2)
            print(f"repointed {fn}")
    # 2. explanation-layer replacements (exact literals, counted).
    #    Longest old literal first: several short literals are prefixes
    #    of longer ones (e.g. "13 点关门" inside the P7 error-clinic
    #    sentence; "feriadão = 连休" inside the P1/P7 notes).
    failed = []
    for old, new in sorted(REPLACEMENTS, key=lambda t: -len(t[0])):
        total = 0
        for fn in FILES:
            p = os.path.join(HERE, fn)
            s = open(p, encoding="utf-8").read()
            n = s.count(old)
            if n:
                open(p, "w", encoding="utf-8").write(s.replace(old, new))
                total += n
        status = "OK " if total else "MISS"
        if not total:
            failed.append(old)
        print(f"{status} x{total} :: {old[:64]!r}")
    # 2b. file-specific post-pass (round-2 length trims whose old literal
    #     also occurs elsewhere and must NOT be changed there):
    #     P8 #134's note is abbreviated to one printed line, but the P3
    #     body note with the identical wording keeps its full form.
    for fn, old, new in [
        ("content8.py", "Subjekt + Verb + Objekt + Ort", "S + V + O + Ort"),
        # P7 word box: the core height formula leaves the Latin note's
        # descenders 1.1px past the box border (audit BOXTITLE); +8 bottom
        # pad, compensated by -8 in the gap to the letters box, so the
        # column bottom (and hence the quotes block) does not move.
        ("content7.py", 'wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("feriadão = langes Feiertagswochenende.", "sans", False, 20, CW - 44)) * 29 + 20',
         'wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("feriadão = langes Feiertagswochenende.", "sans", False, 20, CW - 44)) * 29 + 28'),
        ("content7.py", "ly = wy + wh + 22", "ly = wy + wh + 14"),
    ]:
        p = os.path.join(HERE, fn)
        s = open(p, encoding="utf-8").read()
        n = s.count(old)
        if n != 1:
            failed.append(f"{fn}:{old}")
            print(f"MISS x{n} (file-specific) :: {old[:64]!r}")
        else:
            open(p, "w", encoding="utf-8").write(s.replace(old, new))
            print(f"OK  x1 (file-specific {fn}) :: {old[:64]!r}")
    # 3. residual CJK scan over build sources (transform.py itself excluded:
    #    it legitimately holds the old literals as mapping data)
    import re
    cjk = re.compile(r"[\u2e80-\u9fff]")
    # typ registry strings are never rendered (see module docstring) and
    # the P8 writing-type check ("写作") is code, not text — exclude them.
    typ_re = re.compile(r'"(单选|完成句子|完形单选|造句|翻译|词汇配对|判断对错|写作)"')
    leftovers = []
    for fn in FILES:
        s = open(os.path.join(HERE, fn), encoding="utf-8").read()
        for i, line in enumerate(s.splitlines(), 1):
            if cjk.search(typ_re.sub('""', line)):
                leftovers.append((fn, i, line.strip()[:100]))
    print(f"residual CJK lines in build sources: {len(leftovers)}")
    for fn, i, line in leftovers:
        print(f"  {fn}:{i}: {line}")
    if failed or leftovers:
        print(f"TRANSFORM FAILED: {len(failed)} missed literals, {len(leftovers)} CJK lines left")
        return 1
    print("TRANSFORM OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
