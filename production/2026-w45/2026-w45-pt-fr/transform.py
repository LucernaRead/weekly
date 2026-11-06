# -*- coding: utf-8 -*-
"""PT x FR fan-out transform for W45 (VOL.2).

Run ONCE on a fresh copy of hidden_files/weekly-report-w45-pt-build:
  1. cp -r weekly-report-w45-pt-build -> weekly-report-w45-pt-fr-build
     (excluding __pycache__)
  2. python3 transform.py   (repoints OUT/BASE/PDF names + rewrites ONLY
     the explanation layer from Chinese into French; Portuguese text is
     never touched — every replacement below is a Chinese-containing
     literal, a bilingual furniture line, or a P8 translation re-aim)
  3. <tools/venv>/python run.py && <tools/venv>/python render.py

Rules baked in (W43 PT x FR shipped precedent + W45 PT x DE sibling):
  - gloss prefix "Note — " (tables.json FR column, W43 SVG-verified)
  - badge replaces the P1 strapline in place at y=372, 19pt bold BRICK
  - edition line KEPT at 40pt (unlike W43 FR's 36pt): the W45 French line
    measures 1732.1px <= 1820 at 40pt, so no reduction is needed; the
    core geometry is preserved and the measurement is recorded in the KIT
  - footers: tables.json FR column with VOL.2 substituted for the
    tables.json VOL.1 (W45 core is VOL.2)
  - P8 separator stays "— PÁGINA {pg} —" (W43 PT x FR shipped SVG
    precedent, NOT the tables.json "— Page {n} —" form — deviation
    documented in WEEKLY-KIT.md; same call as PT x DE)
  - exercise `typ` registry strings (e.g. "单选") are NEVER rendered
    (bslib4 ex() prints only level/number/instr/body; P8 prints key/note
    and checks type == "写作" for the writing item) — left untouched
    exactly as in the W43 PT x FR build
  - P8 notes carry NO parentheses (avoids the p8.py paren-branch
    extraction artifact; W43 FR's "(titre page 1)" style note is
    reworded with "cf." instead)
  - space before ? ! : in visible French text (W43 FR rule, e.g.
    "ET VOUS ?"); French times written "13 h" in the French layer,
    while frozen Portuguese text keeps "13h"
  - P8 translation re-aims (W43 KIT pattern): 137/138 PT->FR keys;
    139/140 stems FR->PT with Portuguese keys byte-identical; 150
    writing apparatus in French, model text untouched
  - P7 word box: the Portuguese definition sentence is FROZEN verbatim;
    only the gloss line is localised into French (blocking gate)
  - P7 readers' corner: Portuguese disclosure sentence verbatim (frozen);
    Chinese notes -> French; the French example note carries the EXPLICIT
    invitation (imperative "Écrivez-nous votre lettre !" + publication
    promise "paraîtront dans le VOL.3"); the French disclosure states
    all three facts (no real letters, no best P8 texts, example + VOL.3
    promise)
  - ERROS COMUNS title shortened to "ERROS COMUNS · ERREURS" (W43 FR
    precedent): the full "ERREURS FRÉQUENTES" form measures 480.8px at
    23pt > 390px box inner width and would overflow the box
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
     "A Lucerna · HEBDOMADAIRE PORTUGAIS VOL.2 · TEXTE EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS"),
    ('f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} sur {total}"'),
    ('("译注｜" + s', '("Note — " + s'),
    # ---- P1 top furniture ----
    ("TODA SEMANA EM PORTUGUÊS · 每周一期 · 读巴西人正在读的葡萄牙语",
     "TODA SEMANA EM PORTUGUÊS · CHAQUE SEMAINE · LE PORTUGAIS QUE LIT LE BRÉSIL"),
    ("葡 萄 牙 语 周 报 · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE",
     "JOURNAL PORTUGAIS · VOL.2 · A SEMANA DO ENEM · FINADOS · O FUTEBOL DECIDE"),
    ('p.text(975, 372, "O JORNAL SEMANAL PARA APRENDER — O BRASIL DE VERDADE, EM PORTUGUÊS, DO BRASIL", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEXTES EN PORTUGAIS · EXPLICATIONS EN FRANÇAIS — L\u2019ÉDITION POUR LES LECTEURS FRANCOPHONES", 19, "sans", True, BRICK, anchor="middle")'),
    ("全国高考周", "SEMAINE DE L\u2019ENEM"),
    ("11 月 2 日亡灵节连休 · 11 月 8 日高考第一天",
     "2 nov. : Finados et pont · 8 nov. : premier jour d\u2019examen"),
    ("A NOTÍCIA · 头条", "A NOTÍCIA · À LA UNE"),
    ("讲解｜feriadão 连休长周末 · o portão 大门 · a redação 作文 · revisar 复习。",
     "Notes — feriadão = long week-end de pont · o portão = porte d\u2019entrée · a redação = dissertation · revisar = réviser."),
    ("A SEMANA EM NÚMEROS · 数字", "A SEMANA EM NÚMEROS · CHIFFRES"),
    ("12h — os portões abrem no domingo 8（周日 12 点开门）",
     "12h — os portões abrem no domingo 8 (dimanche 8, ouverture à 12 h)"),
    ("13h — os portões fecham（13 点关门，过时不入）",
     "13h — os portões fecham (13 h : après, plus d\u2019entrée)"),
    ("13h30–19h — a prova do dia 8（考试 13:30 至 19:00）",
     "13h30–19h — a prova do dia 8 (examen de 13 h 30 à 19 h)"),
    ("5h30 — a duração da prova do dia 8（考试时长 5 小时半）",
     "5h30 — a duração da prova do dia 8 (durée : cinq heures et demie)"),
    ("AGORA VOCÊ · 即学即练", "AGORA VOCÊ · À VOUS"),
    ("feriadão = 连休长周末，共三天。", "feriadão = pont de trois jours."),
    ("feriadão = 连休长周末", "feriadão = long week-end de pont"),
    ("portões = 大门（考场大门）", "portões = portes d\u2019entrée du lieu d\u2019examen"),
    ("redação = 作文", "redação = dissertation"),
    ("13h30 开考（巴西利亚时间）", "13h30 : début, heure de Brasília"),
    ("19h 结束", "19h : fin"),
    ("revisar 现在时 eles 形式：revisam", "revisar, présent eles : revisam"),
    ("迟到不得入内：13 点后关门", "En retard : plus d\u2019entrée après 13 h"),
    ("NESTA EDIÇÃO · 本期目录", "NESTA EDIÇÃO · SOMMAIRE"),
    ("“连休”：假期连着周末，一共三天。", "« Feriadão » : trois jours de pont."),
    ("EM POUCAS PALAVRAS · 快讯", "EM POUCAS PALAVRAS · EN BREF"),
    ("QUIZ RELÂMPAGO · 闪电问答", "QUIZ RELÂMPAGO · QUIZ ÉCLAIR"),
    ("读头版，选出正确答案 · 答案见第 8 版", "Lisez la une, choisissez la bonne réponse · réponses page 8"),
    ("次回合在 7 日和 8 日", "Les matches retour ont lieu les 7 et 8"),
    ("PARA NÃO ERRAR · 口诀", "PARA NÃO ERRAR · À RETENIR"),
    # ---- shared exercise furniture (all pages) ----
    ("EXERCÍCIOS · 第 2 版练习", "EXERCÍCIOS · EXERCICES · PAGE 2"),
    ("EXERCÍCIOS · 第 3 版练习", "EXERCÍCIOS · EXERCICES · PAGE 3"),
    ("EXERCÍCIOS · 第 4 版练习", "EXERCÍCIOS · EXERCICES · PAGE 4"),
    ("EXERCÍCIOS · 第 5 版练习", "EXERCÍCIOS · EXERCICES · PAGE 5"),
    ("EXERCÍCIOS · 第 6 版练习", "EXERCÍCIOS · EXERCICES · PAGE 6"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案", "Réponses page 8 · niveaux mélangés — cherchez par numéro"),
    ('instr="填空"', 'instr="Compléter"'),
    ('instr="造句"', 'instr="Former une phrase"'),
    ('instr="翻译"', 'instr="Traduire"'),
    ('instr="写作"', 'instr="Écrire"'),
    ('instr="判断"', 'instr="Vrai ou faux ?"'),
    ('instr="把词和释义配对"', 'instr="Associer"'),
    # ---- P2 ----
    ("VIDA · 生活", "VIDA · LA VIE"),
    ("NÍVEL A2 · Finados e revisão: o feriadão do Brasil",
     "NÍVEL A2 · Finados e revisão: o feriadão do Brasil · Finados et révision : le pont au Brésil"),
    ("o feriadão 连休长周末 · o cemitério 墓园 · a vela 蜡烛 · o crisântemo 菊花 · a missa 弥撒 · conferir 核对。",
     "o feriadão = long week-end de pont · o cemitério = cimetière · a vela = bougie · o crisântemo = chrysanthème · a missa = messe · conferir = vérifier."),
    ("E VOCÊ? · 说说你自己", "E VOCÊ? · ET VOUS ?"),
    ("在你的国家，有纪念逝者的日子吗？那天家人们做什么？写两句寄来。",
     "Dans votre pays, y a-t-il un jour pour se souvenir des morts ? Que font les familles ce jour-là ? Écrivez deux phrases et envoyez-les-nous."),
    ("OS HORÁRIOS DO DOMINGO 8 · 周日时间表", "OS HORÁRIOS DO DOMINGO 8 · LES HORAIRES DU DIMANCHE 8"),
    ("Um país, vários relógios · 一个国家，几个时区", "Um país, vários relógios · Un pays, plusieurs fuseaux horaires"),
    ("周日 12 点开门", "Dimanche 12 h : ouverture"),
    ("13 点关门", "Fermeture à 13 h"),
    ("13:30 开考", "Début à 13 h 30"),
    ("19:00 结束", "19 h : fin"),
    ("读第 2 版文章，选出正确答案。", "Lisez la page 2 et choisissez la bonne réponse."),
    ("连休从 10 月 31 日到 11 月 2 日", "Le pont va du 31 octobre au 2 novembre"),
    ("亡灵节家人们去墓园献花", "À Finados, les familles vont fleurir les cimetières"),
    ("确认卡显示考试地点", "La carte indique le lieu de l\u2019examen"),
    ("巴西没有夏令时，钟表不动", "Pas de changement d\u2019heure au Brésil"),
    ("补全动词的现在时形式。", "Complétez les verbes au présent."),
    ("conferir：ele → confere", "conferir : ele confere"),
    ("abrir：ele → abre", "abrir : ele abre"),
    ("levar：nós → levamos", "levar : nós levamos"),
    ("começar：ela → começa", "começar : ela começa"),
    ("ser 现在时 ela 形式：é", "ser, présent ela : é"),
    ("用第 1、2 版的数字填空。", "Complétez avec les chiffres des pages 1 et 2."),
    ("12 点到 13 点 = 1 小时", "De 12 h à 13 h = 1 heure"),
    ("13:30 至 19:00 = 5 个半小时", "De 13 h 30 à 19 h = cinq heures et demie"),
    ("5×60 + 30 = 330 分钟", "5 × 60 + 30 = 330 minutes"),
    ("31 日、1 日、2 日 = 3 天", "31, 1er et 2 = 3 jours"),
    ("feriadão=连着周末的假期 c", "feriadão = vacances collées au week-end : c"),
    ("cemitério=墓碑所在的地方 b", "cemitério = lieu des tombes : b"),
    ("vela=点亮纪念的物品 d", "vela = objet qu\u2019on allume en souvenir : d"),
    ("crisântemo=亡灵节带去的花 a", "crisântemo = fleur apportée à Finados : a"),
    # ---- P3 ----
    ("CULTURA · 文化", "CULTURA · CULTURE"),
    ("A2 → B1 · Finados: o dia da memória · 亡灵节：怀念的日子",
     "A2 → B1 · Finados: o dia da memória · Finados : le jour du souvenir"),
    ("o túmulo 墓碑 · a flor 花 · acender 点燃 · rezar 祈祷 · o silêncio 寂静 · a lembrança 怀念。",
     "o túmulo = tombe · a flor = fleur · acender = allumer · rezar = prier · o silêncio = silence · a lembrança = souvenir."),
    ("在你的文化里，人们怎样怀念逝者？写两句寄来。",
     "Dans votre culture, comment se souvient-on des morts ? Écrivez deux phrases et envoyez-les-nous."),
    ("读第 3 版文章，选出正确答案。", "Lisez la page 3 et choisissez la bonne réponse."),
    ("亡灵节是怀念与安静的日子", "Finados est le jour du souvenir et du silence"),
    ("家人们带花去墓园，主要是菊花", "Fleurs aux cimetières, surtout des chrysanthèmes"),
    ("教堂和墓园整天都有弥撒", "Messes toute la journée, églises et cimetières"),
    ("万圣节在 10 月 31 日周六", "Halloween, c\u2019était le samedi 31 octobre"),
    ("怀念是继续亲近的方式", "Se souvenir, c\u2019est rester proche"),
    ("用方框里的词填空。", "Complétez avec les mots de l\u2019encadré."),
    ("túmulo = 墓碑", "túmulo = tombe"),
    ("vela = 蜡烛", "vela = bougie"),
    ("crisântemo = 菊花", "crisântemo = chrysanthème"),
    ("missa = 弥撒", "missa = messe"),
    ("silêncio = 寂静", "silêncio = silence"),
    ("lembrança = 怀念", "lembrança = souvenir"),
    ("用过去时（pretérito perfeito）补全。", "Complétez au pretérito perfeito."),
    ("visitar 过去时 elas 形式：visitaram", "visitar, passé elas : visitaram"),
    ("levar 过去时 elas 形式：levaram", "levar, passé elas : levaram"),
    ("ser 过去时 ele 形式：foi", "ser, passé ele : foi"),
    ("viver 过去时 ele 形式：viveu", "viver, passé ele : viveu"),
    ("把词组成正确的句子。", "Formez des phrases avec les mots donnés."),
    ("主语 + é + 表语", "Sujet + é + attribut"),
    ("主语 + 动词 + 宾语 + 地点", "Sujet + verbe + complément + lieu"),
    ("主语 + 动词 + 宾语", "Sujet + verbe + complément"),
    # ---- P4 ----
    ("ESPORTE · 体育", "ESPORTE · SPORT"),
    ("NÍVEL B1 · O futebol da semana · 足球之周", "NÍVEL B1 · O futebol da semana · La semaine du football"),
    ("a ida 首回合 · a volta 次回合 · o finalista 决赛球队 · a decisão 决战 · a rodada 轮次。",
     "a ida = match aller · a volta = match retour · o finalista = finaliste · a decisão = match décisif · a rodada = journée de championnat."),
    ("你在巴西杯支持哪支球队？写两句寄来。", "Quelle équipe soutenez-vous en Copa do Brasil ? Écrivez deux phrases et envoyez-les-nous."),
    ("A SEMANA DO FUTEBOL · 足球周历", "A SEMANA DO FUTEBOL · LA SEMAINE DU FOOTBALL"),
    ("读第 4 版文章，选出正确答案。", "Lisez la page 4 et choisissez la bonne réponse."),
    ("次回合米内罗竞技 × 格雷米奥在周六 7 日 18 点", "Retour Atlético-MG × Grêmio : samedi 7, 18 h"),
    ("瓦斯科 × 帕尔梅拉斯次回合在周日 8 日 17 点，圣雅努阿里奥",
     "Retour Vasco × Palmeiras, dimanche 8"),
    ("首回合在 11 月 1 日周日", "Les matches aller ont eu lieu le dimanche 1er novembre"),
    ("第 34 轮周一到周五每天都有比赛", "La 34e journée a un match du lundi au vendredi"),
    ("两回合总比分胜者进决赛", "Va en finale qui gagne sur l\u2019ensemble des deux matches"),
    ("finalista=进决赛的球队 b", "finalista = équipe qui atteint la finale : b"),
    ("ida=对决的第一场 c", "ida = premier match d\u2019une confrontation : c"),
    ("volta=对决的第二场 a", "volta = deuxième match d\u2019une confrontation : a"),
    ("rodada=一轮比赛 d", "rodada = journée d\u2019un championnat : d"),
    ("用括号里正确的比较形式填空。", "Complétez avec la bonne forme comparative entre parenthèses."),
    ("次回合决定决赛名额：mais", "Le retour décide de la finale : mais"),
    ("18 > 16：mais", "18 > 16 : mais"),
    ("17 < 18：mais cedo", "17 < 18 : mais cedo"),
    ("第 34 轮周一到周五都有比赛：mais", "La 34e journée va du lundi au vendredi : mais"),
    ("把句子补全成过去时（pretérito perfeito）。", "Complétez les phrases au pretérito perfeito."),
    ("ser 过去时复数：foram", "ser, passé pluriel : foram"),
    ("receber 过去时 ele 形式：recebeu", "receber, passé ele : recebeu"),
    ("começar 过去时 ela 形式：começou", "começar, passé ela : começou"),
    ("chegar 过去时 eles 形式：chegaram", "chegar, passé eles : chegaram"),
    # ---- P5 ----
    ("JOVENS · 青年", "JOVENS · JEUNES"),
    ("NÍVEL B1 · A reta final dos jovens · 冲刺周：年轻人的最后一周",
     "NÍVEL B1 · A reta final dos jovens · Le sprint final des jeunes"),
    ("1. Confira o Cartão de Confirmação do Enem（核对高考确认卡）",
     "1. Confira o Cartão de Confirmação do Enem (vérifier la carte de confirmation de l\u2019Enem)"),
    ("2. Revise um pouco por dia, sem maratona（每天复习一点，不搞突击）",
     "2. Revise um pouco por dia, sem maratona (réviser un peu chaque jour, sans bachotage)"),
    ("3. Durma bem na véspera da prova（考前一晚睡好）",
     "3. Durma bem na véspera da prova (bien dormir la veille de l\u2019examen)"),
    ("4. Separe documento e caneta preta no dia anterior（提前一天备好证件和黑笔）",
     "4. Separe documento e caneta preta no dia anterior (préparer la veille pièce d\u2019identité et stylo noir)"),
    ("5. Domingo 8: chegue antes das 12h（周日 8 日：12 点前到达）",
     "5. Domingo 8: chegue antes das 12h (dimanche 8 : arriver avant 12 h)"),
    ("a reta final 最后冲刺 · a véspera 前夕 · a maratona 突击马拉松 · separar 准备好 · a cabeça 头脑、状态。",
     "a reta final = sprint final · a véspera = veille · a maratona = bachotage de dernière minute · separar = préparer · a cabeça = tête, forme."),
    ("重要考试前一晚，你的计划是复习还是休息？写两句寄来。",
     "La veille d\u2019un examen important, votre plan, c\u2019est réviser ou vous reposer ? Écrivez deux phrases et envoyez-les-nous."),
    ("读第 5 版文章，选出正确答案。", "Lisez la page 5 et choisissez la bonne réponse."),
    ("冲刺周在 11 月 8 日周日结束", "Le sprint final se termine le dimanche 8 novembre"),
    ("每天复习一点", "Réviser un peu chaque jour"),
    ("提前一天备好证件和黑笔", "Préparer la veille pièce d\u2019identité et stylo noir"),
    ("第 2 天考自然科学与数学", "Le jour 2 : sciences de la nature et mathématiques"),
    ("11 月 3 日周二各州议会结束休会", "Mardi 3 : reprise des assemblées des États"),
    ("用方框里的词填空。注意：有的词要变成复数。",
     "Complétez avec les mots de l\u2019encadré. Attention : certains doivent passer au pluriel."),
    ("reta final = 最后冲刺阶段", "reta final = sprint final"),
    ("inscrito 配合复数：inscritos", "inscrito au pluriel : inscritos"),
    ("véspera = 前夕", "véspera = veille"),
    ("maratona = 突击马拉松", "maratona = bachotage de dernière minute"),
    ("local = 地点", "local = lieu"),
    ("separar 祈使式：separe", "separar, impératif : separe"),
    ("用将来时（futuro do presente）补全。", "Complétez au futuro do presente."),
    ("fazer 将来时 eles 不规则形式：farão", "fazer, futur eles, irrégulier : farão"),
    ("mostrar 将来时：mostrará", "mostrar, futur : mostrará"),
    ("sair 将来时复数：sairão", "sair, futur pluriel : sairão"),
    ("chegar 将来时：chegará", "chegar, futur : chegará"),
    ("错：考前突击不是好计划，每天复习一点才好",
     "Faux : mieux vaut réviser un peu chaque jour"),
    ("对：13:30 至 19:00", "Vrai : de 13 h 30 à 19 h"),
    # ---- P6 ----
    ("APROFUNDAMENTO · 深读", "APROFUNDAMENTO · APPROFONDISSEMENT"),
    ("NÍVEL B2 · O Enem explicado · 高考详解", "NÍVEL B2 · O Enem explicado · L\u2019Enem expliqué"),
    ("os portões 大门 · a segunda chamada 补考、第二次入场 · conferir 核对 · a correria 匆忙。",
     "os portões = portes d\u2019entrée · a segunda chamada = rattrapage, deuxième entrée — inexistante à l\u2019Enem · conferir = vérifier · a correria = précipitation."),
    ("O DOMINGO 8 EM NÚMEROS · 11 月 8 日的数字 (horários oficiais do Inep)",
     "O DOMINGO 8 EM NÚMEROS · LES CHIFFRES DU 8 NOVEMBRE (horários oficiais do Inep)"),
    ("看上面两张图，选出正确答案。", "Regardez les deux graphiques ci-dessus et choisissez la bonne réponse."),
    ("大门开放 60 分钟", "Les portes restent ouvertes 60 minutes"),
    ("关门到开考之间等 30 分钟", "Entre la fermeture et le début : 30 minutes d\u2019attente"),
    ("考试 330 分钟", "L\u2019examen dure 330 minutes"),
    ("60 + 30 + 330 = 420", "60 + 30 + 330 = 420"),
    ("中午到 19 点 = 7 小时", "De midi à 19 h = 7 heures"),
    ("图表数字是 Inep 官方时间", "Chiffres officiels de l\u2019Inep"),
    ("高考分 8 日和 15 日两个周日", "L\u2019Enem a deux dimanches : le 8 et le 15"),
    ("第 1 天考作文、语言与人文", "Le jour 1 : dissertation, langues et sciences humaines"),
    ("13 点后到场不得入内", "Qui arrive après 13 h n\u2019entre pas"),
    ("根据句子意思，补全正确的动词形式。", "Complétez avec la bonne forme verbale selon le sens de la phrase."),
    ("将来时：começará", "Futur : começará"),
    ("quem + 虚拟式将来：chegar", "quem + futur du subjonctif : chegar"),
    ("现在时：fecham", "Présent : fecham"),
    ("现在时：pede", "Présent : pede"),
    ("用方框里的词填空：portões · segunda chamada · local · conferir",
     "Complétez avec les mots de l\u2019encadré : portões · segunda chamada · local · conferir"),
    ("portões = 大门", "portões = portes d\u2019entrée"),
    ("segunda chamada = 补考、第二次入场", "segunda chamada = rattrapage, 2e entrée"),
    ("祈使式：confira", "Impératif : confira"),
    # ---- P7 ----
    ("LÍNGUA · 语言", "LÍNGUA · LANGUE"),
    ("聚焦语言 · Três níveis, três ferramentas · 三个级别，三件工具",
     "Gros plan sur la langue · Três níveis, três ferramentas · Trois niveaux, trois outils"),
    ("提问句：que horas（几点）+ 动词；onde fica 问地点；conferir 的 eu 形式不规则：confiro",
     "Poser une question : que horas (à quelle heure) + verbe ; onde fica demande le lieu ; conferir est irrégulier à eu : confiro."),
    ("conferir：eu → confiro（不规则）", "conferir : eu confiro, irrégulier"),
    ("conferir：você → confere", "conferir : você confere"),
    ("onde 问地点", "onde demande le lieu"),
    ("讲一周的事用过去时（pretérito perfeito）；revisar 规则（revisei）；chegar/dormir 的过去时注意重音。",
     "Pour raconter la semaine, on emploie le pretérito perfeito ; revisar est régulier (revisei) ; pour chegar et dormir, attention à l\u2019accent : chegou, dormiu."),
    ("revisar 过去时：revisei", "revisar, passé : revisei"),
    ("chegar 过去时：chegou", "chegar, passé : chegou"),
    ("dormir 过去时：dormiu", "dormir, passé : dormiu"),
    ("chegaram 是 chegar 的过去时复数", "chegaram = passé pluriel de chegar"),
    ("quando、se、quem 后用虚拟式将来：tiver、for、chegar（周日假设）。",
     "Après quando, se et quem, on emploie le futur du subjonctif : tiver, for, chegar — des hypothèses sur le dimanche."),
    ("quem + 虚拟式将来：tiver", "quem + futur du subjonctif : tiver"),
    ("quando + 虚拟式将来：chegar", "quando + futur du subjonctif : chegar"),
    ("se + ser 的虚拟式将来：for", "se + futur du subjonctif de ser : for"),
    ("quando + 未来 → 虚拟式将来 for", "quando + futur → futur du subjonctif : for"),
    ("ERROS COMUNS · 常见错误", "ERROS COMUNS · ERREURS"),
    ("高考用黑笔，蓝笔不行。", "Stylo noir à l\u2019Enem, pas de bleu."),
    ("13 点关门，13:30 到就晚了。", "Fermeture à 13 h : trop tard à 13 h 30."),
    ("考前一夜突击没用，睡好才记得住。", "Dormez bien, ne bachotez pas."),
    ("连休是 10 月 31 日到 11 月 2 日，共三天。", "Pont du 31 octobre au 2 novembre."),
    ("A PALAVRA · 本周生词", "A PALAVRA · MOT DE LA SEMAINE"),
    ("编辑部示例，非真实来信。真实来信请寄编辑部，下期见！",
     "Exemple de la rédaction. Écrivez-nous ! Les meilleures paraîtront au VOL.3."),
    ("编辑部说明：上期承诺的真实来信与最佳作文截稿时未收到，本期仍刊示例，顺延至下期。",
     "Note de la rédaction : ni lettres ni meilleurs textes du VOL.1 avant le bouclage — l\u2019exemple reste, promesse au VOL.3."),
    ("FRASES DA SEMANA · 本周金句（逐字摘自本期文章）",
     "FRASES DA SEMANA · PHRASES DE LA SEMAINE (citées mot à mot dans ce numéro)"),
    ("从连休到考试：高考周。", "Du pont à l\u2019examen : la semaine de l\u2019Enem."),
    ("许多人旅行、探亲、去墓园献花。", "Beaucoup voyagent, voient leur famille et vont fleurir le cimetière."),
    ("亡灵节是怀念的日子。", "Finados est le jour du souvenir."),
    ("怀念是继续亲近的方式。", "Se souvenir, c\u2019est rester proche."),
    ("每一分值一个名次，每一球值一个故事。", "Chaque point vaut une place, chaque but vaut une histoire."),
    ("睡得好，记得牢。", "Bien dormir, mieux retenir."),
    ("先做容易的，再做难的。", "D\u2019abord les faciles, ensuite les difficiles."),
    ("核对确认卡、睡好、早到。", "Vérifier la carte, bien dormir, arriver tôt."),
    ("A PRÓXIMA SEMANA · 下期预告 (VOL.3)", "A PRÓXIMA SEMANA · LA SEMAINE PROCHAINE (VOL.3)"),
    # ---- P8 ----
    ("AVALIAÇÃO E RESPOSTAS · 练习与答案", "AVALIAÇÃO E RESPOSTAS · EXERCICES ET RÉPONSES"),
    ("第 8 版 · A grande prova da semana + todas as respostas",
     "Page 8 · A grande prova da semana + todas as respostas"),
    ("第 1 天在 11 月 8 日", "Le jour 1, c\u2019est le 8 novembre"),
    ("亡灵节在 11 月 2 日", "Finados, c\u2019est le 2 novembre"),
    ("瓦斯科 × 帕尔梅拉斯次回合在 8 日", "Retour Vasco × Palmeiras le dimanche 8"),
    ("连休共 3 天", "Le pont dure 3 jours"),
    ("考试时长 5 个半小时", "L\u2019examen du jour 8 dure cinq heures et demie"),
    ("第 2 天在 11 月 15 日", "Le jour 2, c\u2019est le 15 novembre"),
    ("确认卡是高考的文件", "La carte de confirmation appartient à l\u2019Enem"),
    ("米内罗竞技 × 格雷米奥次回合在 MRV 竞技场", "Retour Atlético-MG × Grêmio à l\u2019Arena MRV"),
    ("第 34 轮周一到周五都有比赛", "La 34e journée va du lundi au vendredi"),
    ("亡灵节家人们带花", "À Finados, les familles apportent des fleurs"),
    ("330 是考试的分钟数", "330, ce sont les minutes de l\u2019examen"),
    ("亡灵节又称诸圣灵魂日", "Finados s\u2019appelle aussi Dia dos Fiéis Defuntos"),
    ("卢卡斯住在贝洛奥里藏特", "Lucas habite à Belo Horizonte"),
    ("连休里他休息并每天复习一点", "Pendant le pont, il se repose et révise un peu chaque jour"),
    ("前一晚他备好证件和黑笔、早睡", "La veille : document, stylo noir, il se couche tôt"),
    ("他 11 点到达考场", "Il arrive sur place à 11 h"),
    ("时间词在前", "Le mot de temps d\u2019abord"),
    ("疑问词组在句首", "Le mot interrogatif en tête"),
    # P8-E re-aims: 137/138 keys PT->FR; 139/140 stems FR->PT (keys frozen)
    ("11 月 8 日周日是高考的第一天。", "Dimanche 8 novembre, c\u2019est le premier jour de l\u2019Enem."),
    ("对照第 6 版标题", "cf. le titre de la page 6"),
    ("周日前核对确认卡。", "Vérifiez la carte avant dimanche."),
    ("Confira = 请核对", "confira = vérifiez"),
    ("“连休是 10 月 31 日到 11 月 2 日。” → ___",
     "« Le feriadão va du 31 octobre au 2 novembre. » → ___"),
    ("feriadão = 连休", "feriadão = long week-end de pont"),
    ("你到达时，请出示带照片的证件。 → ___",
     "« Quand vous arriverez, présentez la pièce d\u2019identité avec photo. » → ___"),
    ("虚拟式将来 chegar + 祈使 apresente", "futur du subjonctif chegar + impératif apresente"),
    ("feriadão=连着周末的假期 b", "feriadão = vacances collées au week-end : b"),
    ("portão=考场入口 d", "portão = entrée du lieu d\u2019examen : d"),
    ("reta final=考前最后一周 a", "reta final = dernière semaine avant l\u2019examen : a"),
    ("segunda chamada=关门后的再入场（高考没有） c",
     "segunda chamada = réentrée impossible à l\u2019Enem : c"),
    ("documento com foto 带照片的证件", "documento com foto = pièce d\u2019identité avec photo"),
    ("seção = 考场分区（房间）", "seção = salle d\u2019examen"),
    ("大门 13 点关闭", "Les portes ferment à 13 h"),
    ("考试 13:30 开始", "L\u2019examen commence à 13 h 30"),
    ("obrigado = 谢谢", "obrigado = merci"),
    ("写作题（无唯一答案）；范文（{NWORDS} 词）见下。", "Exercice d\u2019écriture (sans réponse unique) ; le texte modèle ({NWORDS} mots) est ci-dessous."),
    ("（开放题，范文如下）", "Question ouverte — texte modèle ci-dessous sur cette page"),
    ("范文见本版 H 区（{NWORDS} 词）", "Texte modèle dans la section H de cette page ({NWORDS} mots)"),
    ("RESPOSTAS · 参考答案 — 按版面分页排列，找到题号即可",
     "RESPOSTAS · RÉPONSES — classées par page, cherchez le numéro"),
    ("每题附一句中文简析 · 带 ✓ 的为范文题", "Une courte note en français pour chaque réponse · ✓ = exercice avec texte modèle"),
]

FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py"]


def main():
    # 0. idempotency guard: refuse if already transformed.
    for fn in FILES:
        s = open(os.path.join(HERE, fn), encoding="utf-8").read()
        if "HEBDOMADAIRE PORTUGAIS" in s or "Note — " in s:
            print(f"ABORT: {fn} already transformed — start from a fresh core copy")
            return 2
    # 1. repoint outputs
    for fn in FILES + ["render.py"]:
        p = os.path.join(HERE, fn)
        s = open(p, encoding="utf-8").read()
        s2 = s.replace("weekly-report-w45-pt-core", "weekly-report-w45-pt-fr")
        if fn == "render.py":
            s2 = s2.replace('"A-Lucerna-VOL2.pdf"', '"A-Lucerna-VOL2-FR.pdf"')
            s2 = s2.replace('"A-Lucerna-VOL2-web.pdf"', '"A-Lucerna-VOL2-FR-web.pdf"')
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
    # 2.5 post-pass: P1 numbers-box title must render at 21pt, not 23pt:
    # at 23pt its ink (419.5px) crosses the box border (961.0); at 21pt it
    # measures 383.1px and clears it (W43 PT x FR precedent, same box).
    p12 = os.path.join(HERE, "content12.py")
    s12 = open(p12, encoding="utf-8").read()
    marker = 'f.box("A SEMANA EM NÚMEROS · CHIFFRES", ['
    assert s12.count(marker) == 1, "numbers box call not found"
    head, rest = s12.split(marker, 1)
    lines = rest.splitlines(keepends=True)
    for i, ln in enumerate(lines):
        if ln.rstrip() == "])":
            lines[i] = ln.replace("])", "], tsize=21)", 1)
            break
    else:
        raise AssertionError("numbers box closing not found")
    open(p12, "w", encoding="utf-8").write(head + marker + "".join(lines))
    print("post-pass: numbers box title tsize=21 applied")
    # P7 palavra-box height compensation (+4px): the French gloss line
    # carries Latin descenders (p/j) whose true ink bottom sits 0.8px
    # below the box border computed for the CJK gloss (no descenders);
    # the core's own FIX1 history uses the same box-height compensation
    # remedy for a 1px box-bottom press. +4px clears the audit while
    # leaving the quotes section clear of the preview band.
    p7 = os.path.join(HERE, "content7.py")
    s7 = open(p7, encoding="utf-8").read()
    lines7 = s7.splitlines(keepends=True)
    hit = [i for i, ln in enumerate(lines7) if ln.startswith("wh = 62 + len(wrap(wt,")]
    assert len(hit) == 1, hit
    i = hit[0]
    assert lines7[i].rstrip().endswith("+ 20"), lines7[i]
    lines7[i] = lines7[i].replace("+ 20", "+ 24", 1)
    open(p7, "w", encoding="utf-8").write("".join(lines7))
    print("post-pass: palavra box height +4 applied")
    print("TRANSFORM OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
