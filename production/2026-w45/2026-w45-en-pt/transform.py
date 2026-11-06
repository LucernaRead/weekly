# -*- coding: utf-8 -*-
"""W45 EN core -> EN x PT fan-out transform.

Line/literal-based splicing only (never AST byte offsets). Every pair
asserts its occurrence count; the run aborts before writing anything if
any pair misses. Fix rounds append new pairs here and re-run from a
fresh copy of the core build (never hand-edit content files alone).

Provenance: the core build sources in this directory were reconstructed
by reverse-es.py (reversing the EN x ES transform) and PROVEN by
tools/freeze.py baseline 8/8 byte-identical to the shipped core SVGs
(see core-baseline-proof record in hidden_files/weekly-report-w45-en-pt-coreproof).

Furniture follows the SHIPPED W43 EN x PT edition
(files/weekly-report-en-pt/), which wins over any generic rule:
badge replaces the P1 subtitle slot at y=372, 19.5pt bold brick;
footer "The Lucerna · SEMANÁRIO INGLÊS VOL.2 · TEXTOS EM INGLÊS ·
EXPLICAÇÕES EM PORTUGUÊS"; page line "Página N de 8"; gloss prefix
"Nota — " with comma-style gloss items; P7 phrase points use the
W43 PT "Gramática — " prefix; P8 heads use the W43 PT short forms;
P8 prints notes with half-width parens and "— Página N —" separators;
P8 printed-note set pinned explicitly (NOTAS_EXTRA = the core's
printed pg<8 set, verified identical to the EN x ES pin).
Brazilian Portuguese throughout (the W43 column's variety).
"""
import os
import re
import sys

BASE = os.path.dirname(os.path.abspath(__file__))
CORE_SVG = "~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-core/svg"
ED_SVG = "~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-en-pt/svg"

# (filename, old, new, expected_count; None = replace-all, must occur >= 1)
R = [
    # ---- bslib4: footer + gloss prefix (W43 EN x PT furniture) ----
    ("bslib4.py", '"The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY"',
     '"The Lucerna · SEMANÁRIO INGLÊS VOL.2 · TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS"', 1),
    ("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de 8"', 1),
    ("bslib4.py", '("译注｜" + s, "sans", False, GREY, 20.5, 1.45)',
     '("Nota — " + s, "sans", False, GREY, 20.5, 1.45)', 1),
    # ---- type labels (registry only; never printed on the page) ----
    ("content12.py", '"完成句子", ', '"Completar frases", ', 11),
    ("content12.py", '"单选", ', '"Múltipla escolha", ', 8),
    ("content12.py", '"句型转换", ', '"Reescrever", ', 4),
    ("content12.py", '"词汇配对",\n', '"Combinar",\n', 1),
    ("content34.py", '"完成句子", ', '"Completar frases", ', 8),
    ("content34.py", '"单选", ', '"Múltipla escolha", ', 12),
    ("content34.py", '"句型转换", ', '"Reescrever", ', 8),
    ("content34.py", '"词汇配对",\n', '"Combinar",\n', 2),
    ("content56.py", '"完成句子", ', '"Completar frases", ', 10),
    ("content56.py", '"单选", ', '"Múltipla escolha", ', 12),
    ("content56.py", '"句型转换", ', '"Reescrever", ', 4),
    ("content56.py", '"词汇配对",\n', '"Combinar",\n', 1),
    ("content56.py", '"图表读数", ', '"Leitura de gráfico", ', 6),
    ("content7.py", '"跟练", ', '"Praticar", ', 1),
    ("content7.py", ', "改错", ', ', "Corrigir", ', 4),
    ("content8.py", '"完形填空", ', '"Completar o texto", ', 1),
    ("content8.py", '"单选", ', '"Múltipla escolha", ', 1),
    ("content8.py", '"阅读理解", ', '"Compreensão de leitura", ', 1),
    ("content8.py", '"完成句子", ', '"Completar frases", ', 1),
    ("content8.py", '"翻译", ', '"Traduzir", ', 1),
    ("content8.py", '"词汇配对",\n', '"Combinar",\n', 1),
    ("content8.py", '"对话补全", ', '"Completar o diálogo", ', 1),
    ("content8.py", ', "写作", ', ', "Redação", ', 1),
    # ---- instr labels (printed small grey after the number) ----
    ("content12.py", 'instr="填空"', 'instr="Complete"', None),
    ("content12.py", 'instr="改写"', 'instr="Reescreva"', None),
    ("content12.py", 'instr="把词和释义配对"', 'instr="Combine"', None),
    ("content34.py", 'instr="填空"', 'instr="Complete"', None),
    ("content34.py", 'instr="改写"', 'instr="Reescreva"', None),
    ("content34.py", 'instr="把词和释义配对"', 'instr="Combine"', None),
    ("content56.py", 'instr="填空"', 'instr="Complete"', None),
    ("content56.py", 'instr="改写"', 'instr="Reescreva"', None),
    ("content56.py", 'instr="把词和释义配对"', 'instr="Combine"', None),
    ("content7.py", 'instr="改错"', 'instr="Corrija"', None),
    ("content8.py", 'instr="配对"', 'instr="Combine"', None),
    # ---- shared instruction bridges ----
    ("content12.py", '"读第 2 版文章，选出正确答案。"', '"Leia o artigo da página 2 e escolha a resposta certa."', 1),
    ("content34.py", '"读第 3 版文章，选出正确答案。"', '"Leia o artigo da página 3 e escolha a resposta certa."', 1),
    ("content34.py", '"读第 4 版文章，选出正确答案。"', '"Leia o artigo da página 4 e escolha a resposta certa."', 1),
    ("content56.py", '"读第 5 版文章，选出正确答案。"', '"Leia o artigo da página 5 e escolha a resposta certa."', 1),
    ("content56.py", '"读第 6 版文章，选出正确答案。"', '"Leia o artigo da página 6 e escolha a resposta certa."', 1),
    ("content34.py", '"用所给词补全句子。"', '"Complete as frases com as palavras dadas."', 2),
    ("content56.py", '"用所给词补全句子。"', '"Complete as frases com as palavras dadas."', 2),
    ("content12.py", '"根据时间，用英语补全句子。"', '"Complete as frases em inglês conforme o horário."', 1),
    ("content12.py", '"用 be going to + 动词改写（计划与将要发生的事）。"', '"Reescreva com be going to + verbo (planos e coisas que vão acontecer)."', 1),
    ("content34.py", '"用 be going to 改写。"', '"Reescreva com be going to."', 1),
    ("content34.py", '"用一般过去时改写（比赛已结束的说法）。"', '"Reescreva no passado simples (os jogos já terminaram)."', 1),
    ("content56.py", '"用现在进行时改写（正在发生的事）。"', '"Reescreva no presente contínuo (o que está acontecendo)."', 1),
    ("content56.py", '"读上面的教学图表，选出正确答案。"', '"Leia o gráfico didático acima e escolha a resposta certa."', 1),
]

R += [
    # ================= P1 =================
    ("content12.py", '"WEEKLY IN ENGLISH · 每周一期 · 读美国人正在读的英语"',
     '"WEEKLY IN ENGLISH · UM NÚMERO POR SEMANA · O INGLÊS QUE A AMÉRICA LÊ"', 1),
    ("content12.py", '"英 语 周 报 · VOL.2 · 选 票 · 足 球 · 电 影"',
     '"SEMANÁRIO EM INGLÊS · VOL.2 · VOTOS · FUTEBOL · CINEMA"', 1),
    # badge replaces the strapline slot (W43 EN x PT geometry: y=372, 19.5pt bold brick)
    ("content12.py", 'p.text(975, 372, "THE LEARNERS\' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEXTOS EM INGLÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 19.5, "sans", True, BRICK, anchor="middle")', 1),
    ("content12.py", '"周二选举日 · 周日已拨回时钟"', '"Terça-feira de eleições · Domingo com relógios atrasados"', 1),
    ("content12.py", '"11 月 3 日周二选举日 · 详见第 6 版"', '"Dia de eleições, terça-feira, 3 de novembro · Página 6"', 1),
    ("content12.py", '"THE BIG STORY · 头条"', '"THE BIG STORY · Manchete"', 1),
    ("content12.py", '"讲解｜a midterm 中期选举 · a ballot 选票 · a race 一场竞选 · to call a race 宣布某场竞选的结果。"',
     '"a midterm, eleição de meio de mandato · a ballot, cédula · a race, uma disputa · to call a race, anunciar o resultado de uma disputa."', 1),
    ("content12.py", '"THE WEEK IN NUMBERS · 数字看本周"', '"THE WEEK IN NUMBERS · Em números"', 1),
    ("content12.py", '"Nov 3 — Election Day（选举日） · 435 — seats in the House, all on the ballot（众议院全部席位改选）"',
     '"Nov 3 — Election Day (dia das eleições) · 435 — seats in the House, all on the ballot (todos os assentos da Câmara em disputa)"', 1),
    ("content12.py", '"Nov 6 — two films open（两部电影上映） · Nov 8 — NFL in Madrid + F1 in São Paulo（周日两场大赛）"',
     '"Nov 6 — two films open (dois filmes estreiam) · Nov 8 — NFL in Madrid + F1 in São Paulo (dois grandes eventos no domingo)"', 1),
    ("content12.py", '"TRY IT NOW · 即学即练"', '"TRY IT NOW · Pratique agora"', 1),
    ("content12.py", '"ballot = 纸选票"', '"ballot = cédula"', 1),
    ("content12.py", '"midterm = 中期（选举）"', '"midterm = de meio de mandato"', 1),
    ("content12.py", '"选举日 11 月 3 日（周二）"', '"dia das eleições, terça-feira, 3 de novembro"', 1),
    ("content12.py", '"early voting = 提前投票"', '"early voting = votação antecipada"', 1),
    ("content12.py", '"race called = 宣布结果"', '"race called = resultado anunciado"', 1),
    ("content12.py", '"take time = 花时间"', '"take time = levar tempo"', 1),
    ("content12.py", '"本周美国热搜 · Google Trends 美国区快照"', '"As mais buscadas · Google Trends EUA"', 1),
    ("content12.py", '"相对热度示意，非精确搜索量。"', '"Interesse relativo aproximado, não números exatos."', 1),
    ("content12.py", '"IN THIS ISSUE · 本期目录"', '"IN THIS ISSUE · Nesta edição"', 1),
    ("content12.py", '"（任期）中期。midterm election 中期选举。"', '"A meio do mandato: midterm election."', 1),
    ("content12.py", '"IN BRIEF · 快讯"', '"IN BRIEF · Em resumo"', 1),
    ("content12.py", '"LIGHTNING QUIZ · 闪电问答"', '"LIGHTNING QUIZ · Quiz-relâmpago"', 1),
    ("content12.py", '"读头版，选出正确答案 · 答案见第 8 版"', '"Leia a capa e escolha a resposta certa · Respostas na página 8"', 1),
    ("content12.py", '"选举日 11 月 3 日周二"', '"dia das eleições, terça-feira, 3 de novembro"', 1),
    ("content12.py", '"众议院 435 席全部改选"', '"todos os 435 assentos da Câmara em disputa"', 1),
    ("content12.py", '"美国 11 月 1 日拨回时钟"', '"os EUA atrasaram os relógios em 1º de novembro"', 1),
    ("content12.py", '"NFL 马德里赛 11 月 8 日周日"', '"o jogo da NFL em Madri, domingo, 8 de novembro"', 1),
    # ================= P2 =================
    ("content12.py", 'p.band("LIFE · 生活", "The Lucerna", "LEVEL A2 · Clocks, candy & your week · 时钟、糖果与你的一周")',
     'p.band("LIFE · Vida", "The Lucerna", "LEVEL A2 · Clocks, candy & your week · Relógios, doces e a sua semana")', 1),
    ("content12.py", '"DO THE MATHS · 算一算"', '"DO THE MATHS · Faça as contas"', 1),
    ("content12.py", '"讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。"',
     '"to fall back (relógio), atrasar · a costume, uma fantasia · trick or treat, doces ou travessuras."', 1),
    ("content12.py", '"周日你多睡了一小时吗？写两句英语寄给编辑部。"', '"Dormiu uma hora a mais no domingo? Envie duas frases em inglês à redação."', 2),
    ("content12.py", '"AND YOU ? · 说说你自己"', '"AND YOU ? · E você?"', 1),
    ("content12.py", '"TELLING THE TIME · 这样报时间"', '"TELLING THE TIME · Como dizer as horas"', 1),
    ("content12.py", '"The repeated hour · 本周的三个时间"', '"The repeated hour · As três horas da semana"', 1),
    ("content12.py", '"= two times（两次）"', '"= two times (duas vezes)"', 1),
    ("content12.py", '"= one more time（再一次）"', '"= one more time (mais uma vez)"', 1),
    ("content12.py", '"= to go back one hour（拨回）"', '"= to go back one hour (atrasar)"', 1),
    ("content12.py", '"= one hour more（多出一小时）"', '"= one hour more (uma hora a mais)"', 1),
    ("content12.py", '"EXERCISES · 第 2 版练习"', '"EXERCISES · Exercícios da página 2"', 1),
    ("content12.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Respostas na página 8 · Os exercícios misturam níveis; procure pelo número"', 1),
    ("content12.py", '"1:00 = 一点整"', '"1:00 = uma hora em ponto"', 1),
    ("content12.py", '"1:30 = 一点半"', '"1:30 = uma e meia"', 1),
    ("content12.py", '"7:45 = 差一刻八点"', '"7:45 = quinze para as oito"', 1),
    ("content12.py", '"两次 = twice"', '"duas vezes = twice"', 1),
    ("content12.py", '"多出的 = extra"', '"a mais = extra"', 1),
    ("content12.py", '"Americans 复数 → are going to"', '"Americans, plural → are going to"', 1),
    ("content12.py", '"疑问句：be 提前"', '"pergunta: be no início"', 1),
    ("content34.py", '"疑问句：be 提前"', '"pergunta: be no início"', 1),
    ("content12.py", '"11 月 1 日凌晨 2 点拨回 1 点"', '"em 1º de novembro, das 2h para 1h"', 1),
    ("content12.py", '"亚利桑那与夏威夷不拨钟"', '"Arizona e Havaí não mudam a hora"', 1),
    ("content12.py", '"万圣节 10 月 31 日周六"', '"Halloween, sábado, 31 de outubro"', 1),
    ("content12.py", '"11 月 1 日夜晚有 25 小时"', '"a noite de 1º de novembro tem 25 horas"', 1),
    ("content12.py", '"costume=装扮 b"', '"costume=uma fantasia b"', 1),
    ("content12.py", '"extra hour=多出一小时 a"', '"extra hour=uma hora a mais a"', 1),
    ("content12.py", '"fall back=拨回 d"', '"fall back=atrasar d"', 1),
    ("content12.py", '"trick or treat=不给糖就捣蛋 c"', '"trick or treat=doces ou travessuras c"', 1),
]

R += [
    # ================= P3 =================
    ("content34.py", 'p.band("CULTURE · 文化", "The Lucerna", "A2 → B1 · Friday at the movies · 周五看电影")',
     'p.band("CULTURE · Cultura", "The Lucerna", "A2 → B1 · Friday at the movies · Sexta-feira no cinema")', 1),
    ("content34.py", '"AT HOME THIS WEEK · 在家看什么"', '"AT HOME THIS WEEK · Em casa"', 1),
    ("content34.py", '"讲解｜to open （电影）上映 · a monster 怪物 · a catchphrase 口头禅、金句 · a series 剧集。"',
     '"to open (cinema), estrear · a monster, um monstro · a catchphrase, uma frase famosa · a series, uma série."', 1),
    ("content34.py", '"猫咪电影 11 月 6 日周五上映"', '"o filme do Gato estreia na sexta-feira, 6 de novembro"', 1),
    ("content34.py", '"猫出自苏斯博士的书"', '"o Gato sai de um livro do Dr. Seuss"', 1),
    ("content34.py", '"比尔·黑德为猫配音"', '"Bill Hader dubla o Gato"', 1),
    ("content34.py", '"哥斯拉导演是山崎贵"', '"o diretor de Godzilla é Takashi Yamazaki"', 1),
    ("content34.py", '"《黑鸽》第二季 11 月 5 日上线"', '"a segunda temporada de Black Doves chega em 5 de novembro"', 1),
    ("content34.py", '"周日重聚节目收尾"', '"o reencontro de domingo fecha a semana"', 1),
    ("content34.py", '"open = 上映（第三人称单数加 s）"', '"open = estrear (terceira pessoa do singular com s)"', 1),
    ("content34.py", '"tall → taller 比较级"', '"tall → taller, comparativo"', 1),
    ("content34.py", '"loud → louder"', '"loud → louder"', 1),
    ("content34.py", '"split = 分歧的"', '"split = dividida"', 1),
    ("content34.py", '"monster=怪物 b"', '"monster=um monstro b"', 1),
    ("content34.py", '"catchphrase=金句 a"', '"catchphrase=uma frase famosa a"', 1),
    ("content34.py", '"series=剧集 d"', '"series=uma série d"', 1),
    ("content34.py", '"open=上映 c"', '"open=estrear c"', 1),
    ("content34.py", '"THE CAT\'S HAT · 猫的帽子"', '"THE CAT\'S HAT · O chapéu"', 1),
    ("content34.py", '"五句影评｜who、where、发生了什么、转折、结局——五句就够。"',
     '"Cinco frases de crítica: quem, onde, o que aconteceu, a reviravolta e o final; cinco bastam."', 1),
    # ================= P4 =================
    ("content34.py", 'p.band("SPORT · 体育", "The Lucerna", "LEVEL B1 · NFL · F1 · NASCAR · WTA · Boxing")',
     'p.band("SPORT · Esporte", "The Lucerna", "LEVEL B1 · NFL · F1 · NASCAR · WTA · Boxing")', 1),
    ("content34.py", '"WHY MADRID ? · 为什么去马德里？"', '"WHY MADRID ? · Por que Madri?"', 1),
    ("content34.py", '"讲解｜a fixture 一场比赛（赛程） · a title 冠军头衔 · to defend （卫冕）保卫头衔 · a fan 球迷。"',
     '"a fixture, um jogo da tabela · a title, um título · to defend (campeão), defender o título · a fan, um torcedor."', 1),
    ("content34.py", '"马德里赛：孟加拉虎对猎鹰"', '"Madri: Bengals contra Falcons"', 1),
    ("content34.py", '"马德里赛场是伯纳乌"', '"o estádio de Madri é o Bernabéu"', 1),
    ("content34.py", '"海豚对雄狮在迈阿密"', '"Dolphins contra Lions em Miami"', 1),
    ("content34.py", '"F1 圣保罗大奖赛在巴西"', '"o Grande Prêmio de São Paulo de F1, no Brasil"', 1),
    ("content34.py", '"WTA 年终总决赛在印第安维尔斯开赛"', '"as Finais da WTA começam em Indian Wells"', 1),
    ("content34.py", '"拳击赛在阿灵顿"', '"o boxe, em Arlington"', 1),
    ("content34.py", '"defend 三单加 s"', '"defend, terceira pessoa do singular com s"', 1),
    ("content34.py", '"与第 4 版原文一致，复数动词"', '"como no artigo da página 4, verbo no plural"', 1),
    ("content34.py", '"big → bigger"', '"big → bigger"', 1),
    ("content34.py", '"fast → faster"', '"fast → faster"', 1),
    ("content34.py", '"fixture=赛程中的比赛 b"', '"fixture=um jogo da tabela b"', 1),
    ("content34.py", '"title=冠军头衔 d"', '"title=um título d"', 1),
    ("content34.py", '"fan=球迷 a"', '"fan=um torcedor a"', 1),
    ("content34.py", '"defend=卫冕 c"', '"defend=defender o título c"', 1),
    ("content34.py", '"play → played"', '"play → played"', 1),
    ("content34.py", '"watch → watched"', '"watch → watched"', 1),
    ("content34.py", '"follow → followed"', '"follow → followed"', 1),
    ("content34.py", '"choose → chose"', '"choose → chose"', 1),
    ("content34.py", '"SUNDAY, NOVEMBER 8 · 周日赛程"', '"SUNDAY, NOVEMBER 8 · Domingo"', 1),
    ("content34.py", '"看球英语｜比分、谁得分、谁领先——短句就是直播英语。"',
     '"Inglês de jogo: o placar, quem marcou, quem está na frente; frases curtas, como ao vivo."', 1),
    # ================= P5 =================
    ("content56.py", 'p.band("YOUTH · 青年", "The Lucerna", "LEVEL B1 · Election night at home · 选举之夜")',
     'p.band("YOUTH · Jovens", "The Lucerna", "LEVEL B1 · Election night at home · Noite de eleições em casa")', 1),
    ("content56.py", '"TOO CLOSE TO CALL · 难分胜负"', '"TOO CLOSE TO CALL · Muito disputado"', 1),
    ("content56.py", '"讲解｜a map （选举）地图 · too close to call 难分胜负、无法判定 · a second screen 第二块屏幕（手机）。"',
     '"a map (eleições), um mapa · too close to call, muito disputado, sem definição · a second screen, uma segunda tela (o celular)."', 1),
    ("content56.py", '"地图随结果逐州变色"', '"o mapa muda de cor estado por estado"', 1),
    ("content56.py", '"too close to call = 尚不知晓"', '"too close to call = ainda não se sabe"', 1),
    ("content56.py", '"选举夜常吃披萨"', '"na noite de eleições, costuma-se comer pizza"', 1),
    ("content56.py", '"第二屏是手机"', '"a segunda tela é o celular"', 1),
    ("content56.py", '"孩子问为什么这么久"', '"as crianças perguntam por que demora tanto"', 1),
    ("content56.py", '"结果早上还在"', '"os resultados continuam lá de manhã"', 1),
    ("content56.py", '"close = 接近的"', '"close = disputado"', 1),
    ("content56.py", '"still = 仍然"', '"still = ainda"', 1),
    ("content56.py", '"与第 5 版原文一致，单数"', '"como no artigo da página 5, no singular"', 2),
    ("content56.py", '"map=选举地图 c"', '"map=um mapa eleitoral c"', 1),
    ("content56.py", '"race=一场竞选 d"', '"race=uma disputa d"', 1),
    ("content56.py", '"result=结果 b"', '"result=um resultado b"', 1),
    ("content56.py", '"call=宣布胜者 a"', '"call=anunciar o vencedor a"', 1),
    ("content56.py", '"change → is changing"', '"change → is changing"', 1),
    ("content56.py", '"send → are sending"', '"send → are sending"', 1),
    ("content56.py", '"watch → are watching"', '"watch → are watching"', 1),
    ("content56.py", '"wait → is waiting"', '"wait → is waiting"', 1),
    ("content56.py", '"FIVE SENTENCES · 五句话作业"', '"FIVE SENTENCES · Cinco frases"', 1),
    ("content56.py", '"投票结束｜The polls have closed = 该州投票已结束，计票开始。"',
     '"Fim da votação: The polls have closed = nesse estado a votação já terminou e a apuração começa."', 1),
    # ================= P6 =================
    ("content56.py", 'p.band("DEEP READ · 时事深读", "The Lucerna", "LEVEL B2 · How America votes · 美国怎么投票")',
     'p.band("DEEP READ · Leitura profunda", "The Lucerna", "LEVEL B2 · How America votes · Como a América vota")', 1),
    ("content56.py", '"A PRACTICE BALLOT · 模拟选票"', '"A PRACTICE BALLOT · Cédula de treino"', 1),
    ("content56.py", '"讲解｜to register 登记（选民登记） · a governor 州长 · to shape laws 影响立法 · patience 耐心。"',
     '"to register, inscrever-se (cadastro de eleitores) · a governor, um governador · to shape laws, influenciar as leis · patience, paciência."', 1),
    ("content56.py", '"READ THE CHART · 读图表"', '"READ THE CHART · Leia o gráfico"', 1),
    ("content56.py", '"38% 选“不用排队”"', '"38% escolhem «não enfrentar fila»"', 1),
    ("content56.py", '"工作原因 29%"', '"o trabalho, 29%"', 1),
    ("content56.py", '"四项合计 100%"', '"os quatro somam 100%"', 1),
    ("content56.py", '"习惯最少 12%"', '"o hábito, só 12%"', 1),
    ("content56.py", '"不用排队比旅行多 17 个百分点"', '"«não enfrentar fila» supera «viagens» por 17 pontos"', 1),
    ("content56.py", '"图表是教学数据非真实民调"', '"o gráfico é material didático, não uma pesquisa real"', 1),
    ("content56.py", '"各州自行组织选举"', '"cada estado organiza suas eleições"', 1),
    ("content56.py", '"众议员任期两年"', '"os deputados têm mandato de dois anos"', 1),
    ("content56.py", '"参议员任期六年、每次约三分之一改选"', '"os senadores têm mandato de seis anos; cerca de um terço se renova de cada vez"', 1),
    ("content56.py", '"邮寄选票计票需时间"', '"contar os votos pelo correio leva tempo"', 1),
    ("content56.py", '"本期不印民调与预测"', '"esta edição não publica pesquisas nem previsões"', 1),
    ("content56.py", '"耐心是制度的一部分"', '"a paciência faz parte do sistema"', 1),
    ("content56.py", '"shape = 影响、塑造"', '"shape = influenciar, moldar"', 1),
    ("content56.py", '"register = 登记"', '"register = inscrever-se"', 1),
    ("content56.py", '"patience = 耐心"', '"patience = paciência"', 1),
    ("content56.py", '"optional = 可选的"', '"optional = opcional"', 1),
    ("content56.py", '"differ 三单 differs"', '"differ, terceira pessoa do singular: differs"', 1),
    ("content56.py", '"private = 私密的"', '"private = em particular"', 1),
    ("content56.py", '"HOW LONG ? · 任期多长？"', '"HOW LONG ? · O mandato"', 1),
    ("content56.py", '"一张地图｜五十个州、五十套规则——所以选举夜看的是地图，不是一个数字。"',
     '"Um mapa: cinquenta estados, cinquenta regras; por isso a noite de eleições se vê num mapa, não num só número."', 1),
]

R += [
    # ================= P7 =================
    ("content7.py", 'p.band("LANGUAGE IN HAND · 精讲", "The Lucerna", "A2 → B2 · Phrases of the week · 本周金句")',
     'p.band("LANGUAGE IN HAND · A língua na mão", "The Lucerna", "A2 → B2 · Phrases of the week · Frases da semana")', 1),
    ("content7.py", '"LEVEL A2 · 基础"', '"LEVEL A2 · Base"', 1),
    ("content7.py", '"LEVEL B1 · 进阶"', '"LEVEL B1 · Avançando"', 1),
    ("content7.py", '"LEVEL B2 · 挑战"', '"LEVEL B2 · Desafio"', 1),
    ("content7.py", '"THE EXAMPLE · 例句"', '"THE EXAMPLE · O exemplo"', 3),
    # B2 example box: quoted English sentence verbatim; only the gloss localised.
    ("content7.py", '"« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6)."',
     '"« Patience is part of the system, not a failure of it. » — part of = uma parte (page 6)."', 1),
    ("content7.py", '"THE TOOLBOX · 工具箱"', '"THE TOOLBOX · Ferramentas"', 1),
    ("content7.py", '"工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。"',
     '"Caixa de ferramentas — Três frases de bolso, uma por nível; todas as frases da semana saem dos textos desta edição: releia o original e fica fácil."', 1),
    ("content7.py", '"PHRASES OF THE WEEK · 本周金句（全部出自本期文章）"', '"PHRASES OF THE WEEK · Frases da semana (todas dos textos desta edição)"', 1),
    ("content7.py", '"每句一个语法点 + 一道小题 · 答案见第 8 版"', '"Um ponto de gramática e um exercício por frase · Respostas na página 8"', 1),
    # phrase grammar points: W43 EN x PT phrase slot renders them with the
    # "Gramática — " prefix (not "Nota — ").
    ("content7.py", '"语法点｜is = 是；日期作主语补足语。"', '"Gramática — is = é; a data é o complemento do sujeito."', 1),
    ("content7.py", '"语法点｜happen 的过去式是 happened，规则变化。"', '"Gramática — o passado de happen é happened, forma regular."', 1),
    ("content7.py", '"语法点｜would + 动词原形，表选择意愿。"', '"Gramática — would + verbo no infinitivo, para expressar preferência."', 1),
    ("content7.py", '"语法点｜that is = 那就是；破折号后总结。"', '"Gramática — that is = ou seja; resume depois do travessão."', 1),
    ("content7.py", '"语法点｜will still = 仍然会；still 放在 will 之后。"', '"Gramática — will still = ainda; still vai depois de will."', 1),
    ("content7.py", '"语法点｜part of = ……的一部分；not 表否定对照。"', '"Gramática — part of = parte de; not marca o contraste."', 1),
    ("content7.py", '"语法点｜not every + 单数动词：并非每处都变。"', '"Gramática — not every + verbo no singular: nem tudo muda."', 1),
    ("content7.py", '"语法点｜has = 有；the week 单数用 has。"', '"Gramática — has = tem; the week, no singular, leva has."', 1),
    ("content7.py", '"is 是"', '"is = é"', 1),
    ("content7.py", '"would + 原形"', '"would + infinitivo"', 1),
    ("content7.py", '"that is 那就是"', '"that is = ou seja"', 1),
    ("content7.py", '"will still 仍然会"', '"will still = ainda"', 1),
    ("content7.py", '"is part of 一部分"', '"is part of = parte de"', 1),
    ("content7.py", '"THE ERROR CLINIC · 易错诊所"', '"THE ERROR CLINIC · Clínica"', 1),
    ("content7.py", '"每句有一处错误：找出来并改正。"', '"Cada frase tem um erro: encontre e corrija."', 1),
    ("content7.py", '"三单否定用 doesn\'t + 原形"', '"a negação na terceira pessoa usa doesn\'t + infinitivo"', 1),
    ("content7.py", '"fall 的过去式是 fell"', '"o passado de fall é fell"', 1),
    ("content7.py", '"bigger 已含比较级，不要再加 more"', '"bigger já é comparativo: não acrescente more"', 1),
    ("content7.py", '"going to 后用动词原形"', '"depois de going to vai o infinitivo"', 1),
    ("content7.py", '"READERS\' CORNER · 读者园地"', '"READERS\' CORNER · Cantinho dos leitores"', 1),
    # Readers' corner: the English letter paragraph is FROZEN verbatim (core's own
    # honestly-labelled example, incl. its own English disclosure clause).
    # Only the Chinese disclosure paragraph is localised: it states the 3
    # facts (no real letters / no best VOL.1 p.8 text / example + promise
    # deferred to VOL.3) plus an explicit imperative invitation.
    ("content7.py", '"编辑说明｜VOL.1 曾承诺 VOL.2 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.1 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.3 起刊登收到的真实来信。"',
     '"Nota da redação: a VOL.1 prometeu cartas reais na VOL.2, mas não chegou nenhuma carta real nem o melhor texto da página 8 da VOL.1; não inventamos nada e o exemplo segue marcado. Envie sua carta e seu texto! Na VOL.3 publicaremos as cartas recebidas."', 1),
    ("content7.py", '"NEXT WEEK · VOL.3 下周预告"', '"NEXT WEEK · Na próxima semana, o VOL.3"', 1),
    ("content7.py", '"下周三退伍军人节，周日 NFL 慕尼黑赛；还有中期选举结果报道。"',
     '"Na quarta-feira, Dia dos Veteranos; no domingo, a NFL em Munique; e os resultados das eleições de meio de mandato."', 1),
    # ================= P8 =================
    ("content8.py", 'p.band("EXERCISES & ANSWERS · 练习与答案", "The Lucerna", "FINAL TEST · 综合评估 · Answers at the bottom of this page 答案在本版下方")',
     'p.band("EXERCISES & ANSWERS · Exercícios e respostas", "The Lucerna", "FINAL TEST · Avaliação final · Answers at the bottom of this page · As respostas estão no final desta página")', 1),
    ("content8.py", '"11 月 3 日是周二"', '"o dia 3 de novembro é terça-feira"', 1),
    ("content8.py", '"pizza 披萨"', '"pizza"', 1),
    ("content8.py", '"map 地图逐州变色"', '"o mapa muda estado por estado"', 1),
    ("content8.py", '"close 接近的"', '"close = disputado"', 1),
    ("content8.py", '"sticker 贴纸"', '"sticker = adesivo"', 1),
    ("content8.py", '"will + 动词原形 know"', '"will + infinitivo: know"', 1),
    ("content8.py", '"still 仍然"', '"still = ainda"', 1),
    ("content8.py", '"选项："', '"Opções:"', 1),
    ("content8.py", '"A · CLOZE · 完形填空"', '"A · CLOZE · Complete o texto"', 1),
    # P8 heads use the W43 EN x PT short forms (round-1 long forms tripped
    # HEAD TOO WIDE at 24pt bold in a 434px column in the ES sibling).
    ("content8.py", '"B · MULTIPLE CHOICE · 单选"', '"B · MULTIPLE CHOICE · Escolha"', 1),
    ("content8.py", '"C · READING · 阅读理解"', '"C · READING · Compreensão"', 1),
    ("content8.py", '"D · SENTENCES · 完成句子与转换"', '"D · SENTENCES · Frases"', 1),
    ("content8.py", '"E · TRANSLATION · 翻译"', '"E · TRANSLATION · Tradução"', 1),
    ("content8.py", '"F · WORDS · 词汇配对"', '"F · WORDS · Associação"', 1),
    ("content8.py", '"G · DIALOGUE · 对话补全"', '"G · DIALOGUE · Diálogo"', 1),
    ("content8.py", '"H · WRITING · 写作 [B1]"', '"H · WRITING · Escrita [B1]"', 1),
    ("content8.py", '"we → get 原形"', '"we → get, infinitivo"', 1),
    ("content8.py", '"已发生的事用 fell"', '"o que já aconteceu usa fell"', 1),
    ("content8.py", '"than → 比较级 bigger"', '"than → comparativo: bigger"', 1),
    ("content8.py", '"despite + 名词：尽管下雨"', '"despite + substantivo: apesar da chuva"', 1),
    ("content8.py", '"whether = 是否"', '"whether = se"', 1),
    ("content8.py", '"将来时 will + 动词原形"', '"futuro: will + infinitivo"', 1),
    ("content8.py", '"be going to + 原形 vote"', '"be going to + infinitivo: vote"', 1),
    ("content8.py", '"too close to call = 难分胜负"', '"too close to call = ainda não se sabe"', 1),
    ("content8.py", '"原文：a teacher from Ohio"', '"no texto: a teacher from Ohio"', 1),
    ("content8.py", '"周二他全天教书"', '"na terça-feira ele ensina o dia todo"', 1),
    ("content8.py", '"贴纸上写着 I VOTED"', '"no adesivo está escrito I VOTED"', 1),
    ("content8.py", '"俄亥俄一如既往难分胜负"', '"Ohio, como sempre, muito disputado"', 1),
    ("content8.py", '"are going to + 原形"', '"are going to + infinitivo"', 1),
    ("content8.py", '"fall → fell（不规则变化）"', '"fall → fell, irregular"', 1),
    ("content8.py", '"tall → taller（比较级）"', '"tall → taller, comparativo"', 1),
    ("content8.py", '"whether 引导“是否”从句"', '"whether introduz uma subordinada com «se»"', 1),
    # E translation items: core keys are reader-language translations of English
    # sentences; 137/140 carry an English instruction, 138/139 a native one.
    # PT mirrors that split: Translate / Traduza, keys in Portuguese.
    ("content8.py", '"耐心是制度的一部分，而不是制度的失败。"', '"A paciência faz parte do sistema, não é uma falha do sistema."', 1),
    ("content8.py", '"part of 一部分；not a failure 不是失败"', '"part of = parte de; not a failure = não uma falha"', 1),
    ("content8.py", '"11 月 3 日周二是美国的选举日。"', '"Terça-feira, 3 de novembro, é o dia das eleições nos Estados Unidos."', 1),
    ("content8.py", '"Election Day 选举日；on Tuesday"', '"Election Day = dia das eleições; on Tuesday"', 1),
    ("content8.py", '"翻译：Tuesday, November 3, is Election Day in the United States."',
     '"Traduza: Tuesday, November 3, is Election Day in the United States."', 1),
    ("content8.py", '"这周日，NFL 在马德里比赛。"', '"Neste domingo, a NFL joga em Madri."', 1),
    ("content8.py", '"on Sunday；in Madrid"', '"on Sunday; in Madrid"', 1),
    ("content8.py", '"翻译：On Sunday, the NFL plays in Madrid."', '"Traduza: On Sunday, the NFL plays in Madrid."', 1),
    ("content8.py", '"并非每处都拨回时钟。"', '"Nem todos os lugares mudam."', 1),
    ("content8.py", '"not every 并非每处；change 变化"', '"not every = nem todo; change = mudar"', 1),
    ("content8.py", '"midterm = 中期选举 b"', '"midterm = eleição de meio de mandato b"', 1),
    ("content8.py", '"governor = 州长 c"', '"governor = governador c"', 1),
    ("content8.py", '"ballot = 选票 d"', '"ballot = cédula d"', 1),
    ("content8.py", '"turnout = 投票率 a"', '"turnout = participação a"', 1),
    ("content8.py", '"投票时出示证件 ID"', '"mostre seu documento de identidade ao votar"', 1),
    ("content8.py", '"line = 排队（美式英语）"', '"line = fila, inglês americano"', 1),
    ("content8.py", '"ballot = 选票"', '"ballot = cédula"', 1),
    ("content8.py", '"sticker = 贴纸"', '"sticker = adesivo"', 1),
    ("content8.py", '"选举日是 11 月 3 日周二"', '"o dia das eleições é terça-feira, 3 de novembro"', 1),
    # writing item 150: key is explanation-layer text, not frozen English.
    ("content8.py", '"开放题 — 要点见写作框，范文在第 8 版写作框内"', '"Questão aberta: veja os pontos no quadro de redação; o modelo está no quadro desta página"', 1),
    ("content8.py", '"按要点给分"', '"Pontua-se por pontos"', 1),
    ("content8.py", '"MODEL · 范文"', '"MODEL · Modelo"', 1),
    ("content8.py", '"用英语写 80–100 词：我的 11 月 3 日周二。写清你是否看了结果、吃了什么、地图显示了什么，再写一句周日夜里拨回的时钟。"',
     '"Escreva em inglês de 80 a 100 palavras: sua terça-feira, 3 de novembro. Diga se viu os resultados, o que comeu, o que o mapa mostrou, e uma frase sobre os relógios atrasados na noite de domingo."', 1),
    ("content8.py", '"ANSWERS · 全部答案与简析（第 1–8 版）"', '"ANSWERS · Respostas e notas (páginas 1–8)"', 1),
    # P8 key block: W43 EN x PT family uses half-width parens (core: full-width).
    ("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
     'kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1),
    ("content8.py", 's += f"（{e[\'note\']}）"', 's += f" ({e[\'note\']})"', 1),
    # Printed-note set must equal the core's exactly (78). Portuguese notes are
    # longer than the Chinese notes the len<=10 rule was calibrated for, so
    # the set is pinned explicitly (same pin as EN x ES, verified against
    # the core's printed set: pg<8 part identical).
    ("content8.py", 'if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):',
     'NOTAS_EXTRA = {11, 12, 14, 19, 29, 30, 31, 33, 41, 44, 47, 48, 51, 58, 64, 66, 67, 68, 69, 71, 74, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 100, 102, 107, 108, 109, 110, 111}\n        if e["note"] and (pg == 8 or e["n"] in NOTAS_EXTRA):', 1),
]

R += [
    # ---- fix round 1 (geometry, carried from the ES sibling where the
    # same mechanism applies; verified by this edition's own audit) ----
    # P2 AND YOU box: the ES audit measured the last line's ink 0.6px below
    # the computed box bottom; grow the box tail 20 -> 24 (box is last in
    # col 3, nothing below it before the fixed y=1570 section). PT wraps
    # to the same 2 lines at the same size/width, so the same tail applies.
    ("content12.py", 'eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Dormiu uma hora a mais no domingo? Envie duas frases em inglês à redação.", "sans", False, 20, CW - 44)) * 29 + 20',
     'eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Dormiu uma hora a mais no domingo? Envie duas frases em inglês à redação.", "sans", False, 20, CW - 44)) * 29 + 24', 1),
    # P8 battery: "Traduza:" is longer than the core's native instruction, so
    # E item 139 wraps to 2 lines (core: 1) and pushes the Levels line onto
    # the writing-strip rule. Recover 28px by tightening the four E gaps
    # 11 -> 4 (Levels baseline 1485 -> ~1457, rule at 1486 clears).
    # Same instruction length as the ES sibling's "Traduce:" (8 chars).
    ("content8.py", 'bf.ex(lv, "Traduzir", k, nt, body, size=20.5)',
     'bf.ex(lv, "Traduzir", k, nt, body, size=20.5, gap=4)', 1),
]

R += [
    # ---- fix round 2 (FLOW OVERFLOW cascade, measured) ----
    # P1 headline flow: the PT numbers box measured 4+4 lines vs the core's
    # 3+3, so the box no longer fit col1's remainder and bumped to col2,
    # cascading TRY IT NOW past the flow bottom (ended 1921 vs 1828).
    # Shorten both parentheticals to restore 3+3 lines (wrap-verified).
    ("content12.py", '"Nov 3 — Election Day (dia das eleições) · 435 — seats in the House, all on the ballot (todos os assentos da Câmara em disputa)"',
     '"Nov 3 — Election Day (dia das eleições) · 435 — seats in the House, all on the ballot (todos em disputa)"', 1),
    ("content12.py", '"Nov 6 — two films open (dois filmes estreiam) · Nov 8 — NFL in Madrid + F1 in São Paulo (dois grandes eventos no domingo)"',
     '"Nov 6 — two films open (dois filmes estreiam) · Nov 8 — NFL in Madrid + F1 in São Paulo (dois eventos no domingo)"', 1),
    # P2 exercises flow: PT bridges A and C measured 2 lines vs the core's 1,
    # each bump cascading one exercise across a column break until the D
    # match_set overflowed the last column (ended 2948 vs bottom 2562).
    # Shorten both bridges to 1 line (wrap-verified); B stays 2 lines like
    # the core's own B bridge.
    ("content12.py", '"Complete as frases em inglês conforme o horário."',
     '"Complete em inglês conforme o horário."', 1),
    ("content12.py", '"Leia o artigo da página 2 e escolha a resposta certa."',
     '"Leia o artigo da página 2 e responda."', 1),
]

R += [
    # ---- fix round 3 (occlusion audit + supplemental scans, measured) ----
    # P1 dark band line 1: PT right text overprinted the EN headline
    # (rowcheck gap -70.3, visible on the card). Shortened so its ink
    # starts at 1398.1 vs the EN ink end 1243.8 (gap 154.4, PIL-measured).
    ("content12.py", '"Terça-feira de eleições · Domingo com relógios atrasados"',
     '"Terça de eleições · Relógios atrasados"', 1),
    # P1 numbers box title: ink crossed the box border by 24.5px
    # (985.5 vs 961). Shortened suffix: ink right 946.2, margin 14.8.
    ("content12.py", '"THE WEEK IN NUMBERS · Em números"',
     '"THE WEEK IN NUMBERS · Números"', 1),
    # P1 searches footnote: ink/advance right 1929.5 past the page frame
    # (1885) and the box edge. Shortened: ink right 1818.0, inside the
    # box padding (1863).
    ("content12.py", '"Interesse relativo aproximado, não números exatos."',
     '"Interesse relativo, não números exatos."', 1),
    # P5 box title: ink crossed the box border by 28.5px (527.5 vs 499).
    # Shortened suffix: ink right 459.0, margin 40.0.
    ("content56.py", '"TOO CLOSE TO CALL · Muito disputado"',
     '"TOO CLOSE TO CALL · Disputado"', 1),
    # P6 box title: ink crossed the box border by 27.8px (988.8 vs 961).
    # Shortened suffix: ink right 881.0, margin 80.0.
    ("content56.py", '"A PRACTICE BALLOT · Cédula de treino"',
     '"A PRACTICE BALLOT · Cédula"', 1),
    # P1 wordmark/subtitle TEXTX flag (6.2px PIL-bbox overlap): the rendered
    # PNG already shows a fully-empty ink row (y=294) between wordmark ink
    # (ends y=293) and subtitle ink (starts y=295) — no glyph touches, so
    # this is a PIL-bbox vs Cairo-rasterization artifact. The task gate
    # nevertheless requires literal NEW=0, so the PT subtitle (furniture,
    # not frozen text) shifts 330 -> 338 (+8px): PIL clearance becomes
    # ~1.8px, the badge gap stays ~8px, wordmark/rules/badge untouched.
    ("content12.py", 'p.text(975, 330, "SEMANÁRIO EM INGLÊS · VOL.2 · VOTOS · FUTEBOL · CINEMA", 46, "serif", True, INK, anchor="middle")',
     'p.text(975, 338, "SEMANÁRIO EM INGLÊS · VOL.2 · VOTOS · FUTEBOL · CINEMA", 46, "serif", True, INK, anchor="middle")', 1),
]

CJK = re.compile(r"[\u4e00-\u9fff]")


def main():
    cache = {}
    for fname, old, new, exp in R:
        p = os.path.join(BASE, fname)
        if p not in cache:
            cache[p] = open(p, encoding="utf-8").read()
        s = cache[p]
        n = s.count(old)
        if exp is None:
            assert n >= 1, f"NOT FOUND {fname}: {old[:70]}"
        else:
            assert n == exp, f"COUNT {fname}: {old[:70]} found {n} expected {exp}"
        cache[p] = s.replace(old, new)
    # repoint OUT paths to the edition dir
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(BASE, fname)
        s = cache[p]
        assert CORE_SVG in s, f"OUT not found in {fname}"
        cache[p] = s.replace(CORE_SVG, ED_SVG)
    for p, s in cache.items():
        open(p, "w", encoding="utf-8").write(s)
        print("wrote", os.path.basename(p))
    # post-conditions on transformed sources
    for fname in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py", "bslib4.py"]:
        s = open(os.path.join(BASE, fname), encoding="utf-8").read()
        assert not CJK.search(s), f"CJK remains in {fname}"
        assert "｜" not in s, f"fullwidth bar remains in {fname}"
    print("transform OK: no CJK, no fullwidth bar in transformed sources")


if __name__ == "__main__":
    main()
