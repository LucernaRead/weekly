# -*- coding: utf-8 -*-
"""W45 IT core -> IT x PT fan-out transform for the BUILD COPY ONLY.

Literal replacements only (tools README #17): each rep() fails loudly if
its old string is absent or its count differs, so a typo can never
silently skip a translation. Italian target-language text is never a
replacement target, EXCEPT the approved furniture/disclosure items
recorded below (P8 separators PAGINA -> PÁGINA, band-title PT tails,
P7 letter-box Italian disclosure line, P8 answer-format dash -> paren
following the shipped W43 IT x PT precedent). Registry exercise-type
names stay in Chinese (never printed anywhere, W43/W45 IT x EN
precedent) so the registry stays byte-comparable with the core.
Furniture strings are verbatim from the shipped W43 IT x PT SVGs
(files/weekly-report-it-pt/svg/): badge, footer, band titles, gloss
prefix "Nota — ", page line, P8 keys head and separators. Badge
geometry: W43 IT x PT puts the badge in the y=372 slot, but the W45
core's y=372 is FROZEN Italian strapline, so the badge is INSERTED at
y=574, 22pt BRICK, following the W45 IT-family insertion precedent
(W45 IT x EN, same core) — replacing the strapline would delete
frozen Italian text. P7 word-box: the Italian definition sentence is
FROZEN verbatim; only the gloss line is localised into Portuguese.
P7 letter: Italian letter text frozen verbatim incl. "(esempio della
redazione)". COORDINATOR RULING 2026-10-27 (reader-corner disclosure,
IT family): the core carries NO Italian disclosure sentence (its
disclosure is in the core reader language), so NO new Italian
disclosure sentence is written here — the frozen Italian elements
(letter, label, VOL.3 preview promise) are retained, and the
Portuguese note itself states all three disclosure facts plus an
imperative invitation with a VOL.3 publication promise. (IT x EN
proofread blocking item B1 was ruled non-blocking on this ground.)
No parentheses are used inside any Portuguese P8 note (paren-format
P8 lines must parse unambiguously in tools/p8.py).
"""
import pathlib, sys

B = pathlib.Path('/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/weekly-report-w45-it-pt-build')
C12, C34, C56, C7, C8, BS, SV = 'content12.py', 'content34.py', 'content56.py', 'content7.py', 'content8.py', 'bslib4.py', 'svglib.py'
ALL = [C12, C34, C56, C7, C8]

def rep(files, old, new, expect=None):
    total = 0
    for fn in files:
        p = B / fn
        t = p.read_text(encoding='utf-8')
        c = t.count(old)
        total += c
        if c:
            p.write_text(t.replace(old, new), encoding='utf-8')
    if expect is not None and total != expect:
        print(f'COUNT MISMATCH: {old!r} found {total}, expected {expect}'); sys.exit(1)
    if total == 0:
        print(f'NOT FOUND: {old!r}'); sys.exit(1)
    return total

# ---------- repoint OUT + render names (copy only; core untouched) ----------
rep(ALL, 'weekly-report-w45-it-core', 'weekly-report-w45-it-pt', 5)
rep(['render.py'], 'weekly-report-w45-it-core', 'weekly-report-w45-it-pt', 1)
rep(['render.py'], 'La-Lucerna-VOL2-web.pdf', 'La-Lucerna-VOL2-PT-web.pdf', 1)
rep(['render.py'], 'La-Lucerna-VOL2.pdf', 'La-Lucerna-VOL2-PT.pdf', 1)
rep(['render.py'], 'Render the IT weekly', 'Render the IT x PT edition', 1)

# ---------- bslib4 furniture (shipped W43 IT x PT strings, VOL.2) ----------
rep([BS], '"La Lucerna · 意大利语周报 VOL.2 · LUCERNA ITALIAN WEEKLY"',
    '"La Lucerna · SEMANÁRIO ITALIANO VOL.2 · TEXTOS EM ITALIANO · EXPLICAÇÕES EM PORTUGUÊS"', 1)
rep([BS], 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"', 1)
rep([BS], '"译注｜" + s', '"Nota — " + s', 1)

# ---------- P1 masthead + pairing badge (W43 IT x PT string; W45 insertion y=574, 22pt) ----------
rep([C12], '"OGNI SETTIMANA IN ITALIANO · 每周一期 · 读意大利人正在读的意大利语"',
    '"OGNI SETTIMANA IN ITALIANO · TODA SEMANA · O ITALIANO QUE OS ITALIANOS LEEM"', 1)
rep([C12], '"意 大 利 语 周 报 · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"',
    '"SEMANÁRIO ITALIANO · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"', 1)
rep([C12], 'p.text(RIGHT - 30, 522, "初寒之周 · 详见第 2 版", 21, "sans", False, "#b3a06a", anchor="end")',
    'p.text(RIGHT - 30, 522, "A semana do primeiro frio · ver página 2", 21, "sans", False, "#b3a06a", anchor="end")\np.text(975, 574, "TEXTOS EM ITALIANO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 22, "sans", True, BRICK, anchor="middle")', 1)
rep([C12], 'p.text(RIGHT - 30, 478, "本周迎来第一场寒冷", 24, "sans", True, "#b3a06a", anchor="end")',
    'p.text(RIGHT - 30, 478, "A SEMANA DO PRIMEIRO FRIO", 24, "sans", True, "#b3a06a", anchor="end")', 1)
rep([C12], '"LA NOTIZIA · 头条"', '"LA NOTIZIA · A MANCHETE"', 1)
rep([C12], '"讲解｜il primo freddo 第一场寒冷 · il versante adriatico 亚得里亚海一侧 · la previsione 预报 · assaggi 品尝。"',
    '"Notas: il primo freddo, o primeiro frio · il versante adriatico, o lado adriático · la previsione, previsão · assaggi, provas."', 1)
rep([C12], '"LA SETTIMANA IN CIFRE · 数字看本周"', '"LA SETTIMANA IN CIFRE · EM NÚMEROS"', 1)
rep([C12], '（可能下初雪的海拔）', '(altitude da primeira neve fraca)', 1)
rep([C12], '（米兰文化论坛 50 多场活动）', '(mais de 50 eventos do Forum Cultura em Milão)', 1)
rep([C12], '（参加米兰潘妮托尼决赛的国家数）', '(países na final do Panettone em Milão)', 1)
rep([C12], '（本周末意甲第 11 轮）', '(a jornada da Serie A deste fim de semana)', 1)
rep([C12], '("11ª — la giornata di Serie A del fine settimana(a jornada da Serie A deste fim de semana)", "serif", False, INK, 20.5, 1.35),\n])',
    '("11ª — la giornata di Serie A del fine settimana(a jornada da Serie A deste fim de semana)", "serif", False, INK, 20.5, 1.35),\n], tsize=20)', 1)
rep([C12], '"ADESSO TU · 即学即练"', '"ADESSO TU · Agora tu"', 1)
rep([C12], '"本周日程 · Cosa succede, giorno per giorno"', '"ESTA SEMANA · Cosa succede, giorno per giorno"', 1)
rep([C12], '"日程以各活动日历为准，时间可能有变。"', '"Datas segundo os calendários dos eventos; os horários podem mudar."', 1)
rep([C12], '"IN QUESTO NUMERO · 本期目录"', '"IN QUESTO NUMERO · NESTE NÚMERO"', 1)
rep([C12], '"“第一场寒冷”：温和秋天后的第一波寒冷。"', '"«O primeiro frio»: o primeiro frio sério depois de um outono ameno."', 1)
rep([C12], '"IN BREVE · 快讯"', '"IN BREVE · EM RESUMO"', 1)
rep([C12], '"QUIZ LAMPO · 闪电问答"', '"QUIZ LAMPO · QUIZ RELÂMPAGO"', 1)
rep([C12], '"读头版，选出正确答案 · 答案见第 8 版"', '"Leia a primeira página e escolha a resposta certa · Respostas na página 8"', 1)

# ---------- band titles / subs (W43 IT x PT band titles verbatim) ----------
rep([C12], '"VITA · 生活"', '"VITA · VIDA COTIDIANA"', 1)
rep([C12], '"LIVELLO A2 · Il primo freddo e il 2 novembre · 初寒与追思日"',
    '"LIVELLO A2 · Il primo freddo e il 2 novembre · O primeiro frio e o 2 de novembro"', 1)
rep([C34], '"CULTURA · 文化"', '"CULTURA · CULTURA"', 1)
rep([C34], '"A2 → B1 · Panettone, torrone e musei aperti · 甜点与博物馆"',
    '"A2 → B1 · Panettone, torrone e musei aperti · Doces e museus abertos"', 1)
rep([C34], '"SPORT · 体育"', '"SPORT · ESPORTES"', 1)
rep([C34], '"LIVELLO B1 · La Serie A e l\'Europa · 意甲与欧战"',
    '"LIVELLO B1 · La Serie A e l\'Europa · A Serie A e a Europa"', 1)
rep([C56], '"GIOVANI · 青年"', '"GIOVANI · JOVENS"', 1)
rep([C56], '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · 卢卡之后"',
    '"LIVELLO B1 · Dopo Lucca: cultura, cinema e weekend · Depois de Lucca"', 1)
rep([C56], '"APPROFONDIMENTO · 深读"', '"APPROFONDIMENTO · APROFUNDAMENTO"', 1)
rep([C56], '"LIVELLO B2 · Leggere le previsioni · 怎样读天气预报"',
    '"LIVELLO B2 · Leggere le previsioni · Como ler uma previsão"', 1)
rep([C7], '"LINGUA · 语言"', '"LINGUA · LÍNGUA"', 1)
rep([C7], '"聚焦语言 · Tre livelli, tre strumenti · 三个级别，三件工具"',
    '"Em foco: a língua · Tre livelli, tre strumenti · Três níveis, três ferramentas"', 1)
rep([C8], '"VALUTAZIONE E RISPOSTE · 练习与答案"', '"VALUTAZIONE E RISPOSTE · AVALIAÇÃO E RESPOSTAS"', 1)
rep([C8], '"第 8 版 · La grande prova della settimana + tutte le risposte"',
    '"Página 8 · La grande prova della settimana + tutte le risposte"', 1)

# ---------- section heads / shared apparatus ----------
rep(ALL, '"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
    '"Respostas na página 8 · Os níveis misturam-se — procure pelo número"')
rep(ALL, '"E TU? · 说说你自己"', '"E TU? · E tu?"')
rep([C12], '"ESERCIZI · 第 2 版练习"', '"ESERCIZI · Exercícios da página 2"', 1)
rep([C34], '"ESERCIZI · 第 3 版练习"', '"ESERCIZI · Exercícios da página 3"', 1)
rep([C34], '"ESERCIZI · 第 4 版练习"', '"ESERCIZI · Exercícios da página 4"', 1)
rep([C56], '"ESERCIZI · 第 5 版练习"', '"ESERCIZI · Exercícios da página 5"', 1)
rep([C56], '"ESERCIZI · 第 6 版练习"', '"ESERCIZI · Exercícios da página 6"', 1)
rep([C12], '"IL 2 NOVEMBRE · 追思日"', '"IL 2 NOVEMBRE · Dia de Finados"', 1)
rep([C34], '"LA SETTIMANA DEL CALCIO · 足球周"', '"LA SETTIMANA DEL CALCIO · Semana do futebol"', 1)
rep([C56], '"LE MINIME DI ESEMPIO · 练习用示例最低温 (DATI INVENTATI PER L\'ESERCIZIO)"',
    '"LE MINIME DI ESEMPIO · Mínimas de exemplo (DATI INVENTATI PER L\'ESERCIZIO)"', 1)
rep([C56], '"PROBABILITÀ · 概率"', '"PROBABILITÀ · Probabilidade"', 1)

# ---------- bridges (printed grey sans) ----------
rep([C12], '"发稿时表决结果尚未确认，详见第 6 版。"',
    '"À hora de fecho, o resultado da votação ainda não estava confirmado — ver página 6."', 1)
rep([C12], '"用意大利语补全句子。"', '"Complete as frases em italiano."', 1)
rep([C12], '"补全动词的现在时形式。"', '"Complete com o presente do indicativo."', 1)
rep([C12], '"读第 2 版文章，选出正确答案。"', '"Leia o artigo da página 2 e escolha a resposta certa."', 1)
rep([C34], '"读第 3 版文章，选出正确答案。"', '"Leia o artigo da página 3 e escolha a resposta certa."', 1)
rep([C34], '"用方框里的词填空。"', '"Preencha com as palavras do quadro."', 1)
rep([C34], '"用 passato prossimo（近过去时）补全，注意助动词 avere / essere。"',
    '"Complete com o passato prossimo — atenção aos auxiliares avere e essere."', 1)
rep([C34], '"把词组成正确的句子。"', '"Ponha as palavras na ordem certa."', 1)
rep([C34], '"读第 4 版文章，选出正确答案。"', '"Leia o artigo da página 4 e escolha a resposta certa."', 1)
rep([C34], '"用括号里词的比较级填空（数据看赛程表）。"',
    '"Preencha com o comparativo da palavra entre parênteses — ver a tabela de jogos."', 1)
rep([C34], '"用 passato prossimo 补全。"', '"Complete com o passato prossimo."', 1)
rep([C56], '"读第 5 版文章，选出正确答案。"', '"Leia o artigo da página 5 e escolha a resposta certa."', 1)
rep([C56], '"用方框里的词填空。注意：有的词要变成复数。"',
    '"Preencha com as palavras do quadro. Atenção: algumas vão para o plural."', 1)
rep([C56], '"用将来时（futuro semplice）补全。"', '"Complete com o futuro semplice."', 1)
rep([C56], '"发稿时 10 月 28 日表决结果尚未确认：本期只写预期日期、争议点和 DPB 数字，不写结果。"',
    '"À hora de fecho, o resultado da votação de 28 de outubro ainda não estava confirmado: este número dá só a data prevista, o ponto em disputa e os números do DPB, sem resultado."', 1)
rep([C56], '"看上面的练习图表，选出正确答案。"', '"Veja o gráfico de treino acima e escolha a resposta certa."', 1)
rep([C56], '"用方框里的词填空：probabilità · media · bollettino · modello"',
    '"Preencha com as palavras do quadro: probabilità · media · bollettino · modello"', 1)
rep([C7], '"天气用无人称动词（第三人称单数）；“我冷”说 ho freddo，“外面冷”说 fa freddo。"',
    '"O tempo usa verbos impessoais, na terceira pessoa do singular: «tenho frio» é ho freddo, «está frio lá fora» é fa freddo."', 1)
rep([C7], '"讲过去用近过去时：arrivare/andare 等用 essere，分词配合性数；avere 的分词不变。"',
    '"Para o passado usa-se o passato prossimo: arrivare e andare levam essere e o particípio concorda; com avere, nunca muda."', 1)
rep([C7], '"è probabile che / è possibile che / bisogna che 后用虚拟式；so che、scrivono che 后用陈述式。"',
    '"Depois de è probabile che, è possibile che e bisogna che usa-se o conjuntivo; depois de so che e scrivono che fica o indicativo."', 1)

# ---------- gloss() argument strings (counts must stay 1:1 with the core) ----------
rep([C12], '"il cappotto 大衣 · la sciarpa 围巾 · i guanti 手套 · a strati 分层穿衣 · il termosifone 暖气片 · il crisantemo 菊花"',
    '"il cappotto casaco · la sciarpa cachecol · i guanti luvas · a strati em camadas · il termosifone aquecedor · il crisantemo crisântemo"', 1)
rep([C34], '"il panettone 米兰圣诞面包 · il torrone 牛轧糖 · l\'assaggio 品尝 · la bancarella 摊位 · il cantiere 施工现场/修复工地。"',
    '"il panettone bolo de Natal de Milão · il torrone torrão · l\'assaggio prova · la bancarella banca · il cantiere estaleiro"', 1)
rep([C34], '"la giornata 轮次 · la presentazione 赛前介绍 · gli spalti 看台 · la sera 晚上。"',
    '"la giornata jornada · la presentazione antevisão · gli spalti bancadas · la sera noite"', 1)
rep([C56], '"il cosplay 角色扮演服装 · gratuito 免费的 · il documentario 纪录片 · lo schermo 银幕。"',
    '"il cosplay fato de cosplay · gratuito gratuito · il documentario documentário · lo schermo ecrã"', 1)
rep([C56], '"la probabilità 概率 · la media 平均值 · il modello 模型/预报模式 · il bollettino 公报/预报 · aggiornare 更新。"',
    '"la probabilità probabilidade · la media média · il modello modelo de previsão · il bollettino boletim · aggiornare atualizar"', 1)

# ---------- P1/P2/P3/P4/P5 box parentheticals + E TU notes ----------
rep([C56], '（周二：米兰文化论坛开幕）', '(terça-feira: abertura do Forum Cultura em Milão)', 1)
rep([C56], '（周三至周四：欧战直播）', '(quarta e quinta: taças europeias na TV)', 1)
rep([C56], '（周五准备周末）', '(sexta: preparar o fim de semana)', 1)
rep([C56], '（周六：米兰或克雷莫纳品尝）', '(sábado: provas em Milão ou Cremona)', 1)
rep([C56], '（周日：意甲与返程）', '(domingo: Serie A e regresso)', 1)
rep([C12], '"初寒来了你穿什么：大衣、围巾还是手套？写两句意大利语寄给编辑部。"',
    '"Quando chega o primeiro frio, o que vestes: casaco, cachecol ou luvas? Escreve duas frases em italiano e envia-as à redação."', 2)
rep([C34], '"你更喜欢传统潘妮托尼还是巧克力味的？写两句寄来。"',
    '"Preferes o panettone tradicional ou o de chocolate? Escreve duas frases e envia-as."', 2)
rep([C34], '"周日晚上你看哪场比赛？写两句意大利语寄来。"',
    '"Que jogo vais ver no domingo à noite? Escreve duas frases em italiano e envia-as."', 2)
rep([C56], '"卢卡之后你去哪：文化论坛、电影还是美食节？写两句寄来。"',
    '"Depois de Lucca, para onde vais: Forum Cultura, cinema ou festa? Escreve duas frases e envia-as."', 2)

# ---------- P2 FRASE box: W43 IT x PT title + tsize 20 ----------
rep([C12], 'f.box("LA FRASE PER RICORDARE · 口诀", [\n    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n])',
    'f.box("LA FRASE PER RICORDARE · MACETE", [\n    ("«Fa freddo, copriti bene!» Così dicono le nonne italiane: quando arriva il primo freddo, il consiglio è uno solo — vestirsi bene, a strati.", "serif", False, INK, 21.5, 1.4),\n], tsize=20)', 1)

# ---------- P7: errori notes (kept to ONE wrapped line each, core col3 geometry) ----------
rep([C7], '"fa 后面的 freddo 永远不变。"', '"Depois de fa, freddo nunca muda."', 1)
rep([C7], '"nevicare 只用第三人称单数。"', '"Nevicare só usa a terceira pessoa do singular."', 1)
rep([C7], '"预报给的是概率，不是确定性。"', '"Previsões dão probabilidades, não certezas."', 1)
rep([C7], '"gente 是单数，动词形容词用单数阴性。"', '"Gente é singular feminino."', 1)
rep([C7], '"ERRORI TIPICI · 常见错误"', '"ERRORI TIPICI · Erros comuns"', 1)
# P7 parola: Italian definition sentence FROZEN verbatim; only the gloss
# line below it is localised. Gloss kept to ONE line so col3 keeps room
# for the letter-box Italian disclosure line added below.
rep([C7], '"LA PAROLA · 本周生词"', '"LA PAROLA · A PALAVRA DA SEMANA"', 1)
rep([C7], '"assaggio = 品尝。本周见第 3 版：潘妮托尼决赛上观众可以免费品尝。"',
    '"assaggio = prova de um alimento, ver página 3."', 2)
# P7 letters: Italian letter text frozen verbatim, including its
# "(esempio della redazione)" label. The box gains a short one-line
# Italian disclosure sentence (its own grey line, height added to the
# lh formula) and the Portuguese note states all three disclosure
# facts (no real letters yet, no best page-8 essay yet, the sample
# stands in and both are promised for VOL.3) plus an explicit
# imperative invitation with a VOL.3 publication promise.
rep([C7], 'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！", "sans", False, 20, CW - 44)) * 29 + 20',
    'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Esempio della redazione: non è ancora una lettera vera.", "sans", False, 20, CW - 44)) * 29 + 12 + len(wrap("Exemplo da redação, não uma carta real: ainda não há cartas reais nem o melhor texto da página 8 — ambos prometidos para o VOL.3. Escrevam à redação!", "sans", False, 20, CW - 44)) * 29 + 20', 1)
rep([C7], 'yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10\np.para(bx + 22, yy3 + 20, "这是编辑部示例信，非真实来信。来信请寄编辑部，VOL.3 刊登真实来信与第 8 版最佳作文！", 20, "sans", False, GREY, CW - 44, 1.42)',
    'yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10\nyy3 = p.para(bx + 22, yy3 + 20, "Esempio della redazione: non è ancora una lettera vera.", 20, "sans", False, GREY, CW - 44, 1.42) + 10\np.para(bx + 22, yy3 + 20, "Exemplo da redação, não uma carta real: ainda não há cartas reais nem o melhor texto da página 8 — ambos prometidos para o VOL.3. Escrevam à redação!", 20, "sans", False, GREY, CW - 44, 1.42)', 1)
rep([C7], '"FRASI DELLA SETTIMANA · 本周金句（逐字摘自本期文章）"', '"FRASI DELLA SETTIMANA · FRASES DA SEMANA"', 1)
rep([C7], '"第一场真正的寒冷到来了。"', '"Chega o primeiro frio a sério da estação."', 1)
rep([C7], '"这不是确定性，而是概率。"', '"Não é uma certeza, é uma probabilidade."', 1)
rep([C7], '"11 月 2 日是追思日。"', '"O dia 2 de novembro é o Dia de Finados."', 1)
rep([C7], '"天冷，穿暖和点！"', '"Está frio, agasalha-te bem!"', 1)
rep([C7], '"观众可以免费品尝。"', '"O público pode provar de graça."', 1)
rep([C7], '"足球不会因为第一场寒冷而停下。"', '"O futebol não para por causa do primeiro frio."', 1)
rep([C7], '"文化继续。"', '"A cultura continua."', 1)
rep([C7], '"高概率不等于确定性。"', '"Uma probabilidade alta não é uma certeza."', 1)
rep([C7], '"LA PROSSIMA SETTIMANA · 下期预告 (VOL.3)"', '"LA PROSSIMA SETTIMANA · NA PRÓXIMA SEMANA (VOL.3)"', 1)

# ---------- printed instructions (instr= values sit beside exercise numbers) ----------
rep(ALL, 'instr="填空"', 'instr="Completar"')
rep(ALL, 'instr="造句"', 'instr="Formar frases"')
rep(ALL, 'instr="判断"', 'instr="Verdadeiro ou falso"')
rep(ALL, 'instr="把词和释义配对"', 'instr="Combinar"')
rep(ALL, 'instr="写作"', 'instr="Escrever"')
# P8 E-section instructions, per item direction (W43 IT x PT ruling:
# keys re-aimed at Portuguese for 137-138, stems re-aimed for 139-140)
rep([C8], 'f.ex("A2", "翻译", "周一第一场寒冷来了。", "对照原文",\n     "Lunedì arriva il primo freddo. → ___", instr="翻译"',
    'f.ex("A2", "翻译", "Na segunda-feira chega o primeiro frio.", "Ver o texto original.",\n     "Lunedì arriva il primo freddo. → ___", instr="Traduzir para português"', 1)
rep([C8], 'f.ex("B1", "翻译", "观众可以免费品尝。", "assaggiare gratis = 免费品尝",\n     "Il pubblico può assaggiare gratis. → ___", instr="翻译"',
    'f.ex("B1", "翻译", "O público pode provar de graça.", "assaggiare gratis = provar de graça",\n     "Il pubblico può assaggiare gratis. → ___", instr="Traduzir para português"', 1)
rep([C8], 'f.ex("B1", "翻译", "周日晚上，佛罗伦萨对尤文图斯。", "si gioca = 进行比赛",\n     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="翻译"',
    'f.ex("B1", "翻译", "No domingo à noite, joga-se Fiorentina–Juventus.", "si gioca = joga-se",\n     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="Traduzir para português"', 1)
rep([C8], 'f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = 必须",\n     "每个预报都必须清楚。→ ___", instr="翻译"',
    'f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = dever",\n     "Cada previsão deve ser clara. → ___", instr="Traduzir para italiano"', 1)

# ---------- exercise notes, pages 1-2 (printed on P8) ----------
rep([C12], '"il primo freddo = 第一场寒冷"', '"il primo freddo = o primeiro frio"', 1)
rep([C12], '"la prima neve leggera = 初雪"', '"la prima neve leggera = a primeira neve fraca"', 1)
rep([C12], '"文化论坛与潘妮托尼决赛都在米兰"', '"Forum Cultura e final do Panettone: ambos em Milão"', 1)
rep([C12], '"克雷莫纳的节日叫 Festa del Torrone"', '"A festa de Cremona é a Festa del Torrone"', 1)
rep([C12], '"previsioni = 预报（复数）"', '"previsioni = previsões, plural"', 1)
rep([C12], '"第一场寒冷在周一 11 月 2 日到来"', '"O primeiro frio chega na segunda-feira, 2 de novembro"', 1)
rep([C12], '"初雪在 1300–1500 米左右"', '"A primeira neve cai por volta de 1.300–1.500 metros"', 1)
rep([C12], '"潘妮托尼决赛在米兰"', '"A final do Panettone é em Milão"', 1)
rep([C12], '"意甲第 11 轮周日收官"', '"A jornada 11 da Serie A fecha no domingo"', 2)
rep([C12], '"cappotto = 大衣"', '"cappotto = casaco"', 1)
rep([C12], '"sciarpa = 围巾"', '"sciarpa = cachecol"', 1)
rep([C12], '"guanti = 手套（复数）"', '"guanti = luvas, plural"', 1)
rep([C12], '"crisantemi = 菊花（复数）"', '"crisantemi = crisântemos, plural"', 1)
rep([C12], '"termosifoni = 暖气片（复数）"', '"termosifoni = aquecedores, plural"', 1)
rep([C12], '"fare freddo：fa freddo（天气）"', '"fare freddo: fa freddo, o tempo"', 1)
rep([C12], '"mettere：io → metto"', '"mettere: io dá metto"', 1)
rep([C12], '"portare：loro → portano"', '"portare: loro dá portano"', 1)
rep([C12], '"guardare：loro → guardano"', '"guardare: loro dá guardano"', 1)
rep([C12], '"restare：la scuola → resta（lei）"', '"restare: la scuola dá resta, lei"', 1)
rep([C12], '"11 月 2 日是追思日"', '"O dia 2 de novembro é o Dia de Finados"', 1)
rep([C12], '"追思日的花是菊花"', '"A flor do dia 2 de novembro é o crisântemo"', 1)
rep([C12], '"分层穿衣：a strati"', '"Vestir em camadas: a strati"', 1)
rep([C12], '"诸圣节今年是周日、无连休"', '"O Dia de Todos os Santos cai num domingo este ano, sem ponte"', 1)
rep([C12], '"cappotto=御寒大衣 c"', '"cappotto = casaco quente de inverno, c"', 1)
rep([C12], '"sciarpa=围巾 d"', '"sciarpa = cachecol, d"', 1)
rep([C12], '"crisantemo=十一月的花 a"', '"crisantemo = flor de novembro, a"', 1)
rep([C12], '"termosifone=暖气片 b"', '"termosifone = aquecedor, b"', 1)

# ---------- exercise notes, pages 3-4 ----------
rep([C34], '"潘妮托尼决赛在米兰"', '"A final do Panettone é em Milão"', 1)
rep([C34], '"克雷莫纳牛轧糖节到 11 月 22 日"', '"A Festa del Torrone vai até 22 de novembro"', 1)
rep([C34], '"潘妮托尼决赛有 19 国糕点师"', '"19 países enviam pasteleiros à final do Panettone"', 1)
rep([C34], '"文化论坛 11 月 3 日周二开幕"', '"O Forum Cultura abre na terça-feira, 3 de novembro"', 1)
rep([C34], '"阿尔巴松露节到 12 月 6 日"', '"A feira da trufa de Alba vai até 6 de dezembro"', 1)
rep([C34], '"panettone = 米兰圣诞面包"', '"panettone = bolo de Natal de Milão"', 1)
rep([C34], '"torrone = 牛轧糖"', '"torrone = torrão"', 1)
rep([C34], '"assaggio = 品尝"', '"assaggio = prova"', 1)
rep([C34], '"bancarella = 摊位"', '"bancarella = banca"', 1)
rep([C34], '"mandorle = 杏仁（复数）"', '"mandorle = amêndoas, plural"', 1)
rep([C34], '"tartufo = 松露"', '"tartufo = trufa"', 1)
rep([C34], '"arrivare 用 essere：è arrivato"', '"arrivare leva essere: è arrivato"', 1)
rep([C34], '"assaggiare 用 avere：abbiamo assaggiato"', '"assaggiare leva avere: abbiamo assaggiato"', 1)
rep([C34], '"andare 用 essere，复数 sono andati"', '"andare leva essere, plural sono andati"', 1)
rep([C34], '"aprire 用 avere：ha aperto"', '"aprire leva avere: ha aperto"', 1)
rep([C34], '"主语 + essere + 地点 + 日期"', '"Sujeito + essere + lugar + data"', 1)
rep([C34], '"地点在前，主语在后"', '"Lugar primeiro, sujeito depois"', 1)
rep([C34], '"dura fino a = 持续到"', '"dura fino a = dura até"', 1)
rep([C34], '"意甲第 11 轮周日收官"', '"A jornada 11 da Serie A fecha no domingo"', 1)
rep([C34], '"周日晚上佛罗伦萨对尤文图斯"', '"No domingo à noite joga-se Fiorentina–Juventus"', 1)
rep([C34], '"欧战第 4 轮在 11 月 3–5 日"', '"A jornada 4 das taças europeias é de 3 a 5 de novembro"', 1)
rep([C34], '"欧战比赛只作前瞻、无结果"', '"Os jogos europeus são antevisões, sem resultados"', 1)
rep([C34], '"国米对科莫在圣西罗"', '"Inter–Como joga-se em San Siro"', 1)
rep([C34], '"giornata=联赛的一轮 c"', '"giornata = uma jornada do campeonato, c"', 1)
rep([C34], '"presentazione=赛前介绍 b"', '"presentazione = antevisão, b"', 1)
rep([C34], '"spalti=看台 a"', '"spalti = bancadas, a"', 1)
rep([C34], '"sera=晚上 d"', '"sera = noite, d"', 1)
rep([C34], '"周日晚上的比赛晚于周五的：più tardi"', '"Os jogos de domingo à noite são mais tarde que os de sexta: più tardi"', 1)
rep([C34], '"周五的比赛早于周日的：più presto"', '"Os jogos de sexta são mais cedo que os de domingo: più presto"', 1)
rep([C34], '"più + bella 周日晚最美（主观评价）"', '"più + bella: a noite de domingo é a mais bela, na opinião dos adeptos"', 1)
rep([C34], '"bene 的比较级是不规则的 meglio"', '"O comparativo de bene é o irregular meglio"', 1)
rep([C34], '"vincere：ha vinto"', '"vincere: ha vinto"', 1)
rep([C34], '"pareggiare：ha pareggiato"', '"pareggiare: ha pareggiato"', 1)
rep([C34], '"arrivare 用 essere，复数 sono arrivati"', '"arrivare leva essere, plural sono arrivati"', 1)
rep([C34], '"guardare 用 avere：abbiamo guardato"', '"guardare leva avere: abbiamo guardato"', 1)
rep([C34], '"prendere 的分词是 preso：ha preso"', '"O particípio de prendere é preso: ha preso"', 1)

# ---------- exercise notes, pages 5-6 ----------
rep([C56], '"卢卡漫画节是第 60 届"', '"A Lucca Comics vai na 60ª edição"', 1)
rep([C56], '"文化论坛 11 月 3 日开幕"', '"O Forum Cultura abre a 3 de novembro"', 1)
rep([C56], '"民俗电影节在佛罗伦萨"', '"O Festival dei Popoli é em Florença"', 2)
rep([C56], '"文化论坛有 50 多场活动"', '"O Forum Cultura tem mais de 50 eventos"', 2)
rep([C56], '"卢卡漫画节主题是 Legacy"', '"O tema da Lucca Comics é Legacy"', 1)
rep([C56], '"armadio = 衣柜"', '"armadio = guarda-roupa"', 1)
rep([C56], '"gratuiti = 免费的（阳性复数）"', '"gratuiti = gratuitos, masculino plural"', 1)
rep([C56], '"documentario = 纪录片"', '"documentario = documentário"', 1)
rep([C56], '"schermo = 银幕"', '"schermo = ecrã"', 1)
rep([C56], '"castagne arrosto 烤栗子（复数）"', '"castagne arrosto = castanhas assadas, plural"', 1)
rep([C56], '"cosplay = 角色扮演服装"', '"cosplay = fato de cosplay"', 1)
rep([C56], '"andare 将来时 noi：andremo"', '"andare, futuro nós: andremo"', 1)
rep([C56], '"esserci 将来时：ci sarà（将有）"', '"esserci, futuro: ci sarà, haverá"', 1)
rep([C56], '"guardare 将来时 noi：guarderemo"', '"guardare, futuro nós: guarderemo"', 1)
rep([C56], '"durare 将来时：durerà"', '"durare, futuro: durerà"', 1)
rep([C56], '"卢卡漫画节到 11 月 8 日才结束是错的"', '"A Lucca Comics acabar a 8 de novembro é falso"', 1)
rep([C56], '"示例数据中最冷的是都灵 3°"', '"A cidade mais fria dos dados de exemplo é Turim, 3°"', 1)
rep([C56], '"示例数据中最暖的是那不勒斯 12°"', '"A cidade mais quente dos dados de exemplo é Nápoles, 12°"', 1)
rep([C56], '"12 − 9 = 3"', '"12 menos 9 = 3"', 1)
rep([C56], '"4 + 5 = 9"', '"4 mais 5 = 9"', 1)
rep([C56], '"图表数据是练习用的、不是真实预报"', '"Os números do gráfico são dados de treino, não previsões reais"', 1)
rep([C56], '"高概率不等于确定"', '"Uma probabilidade alta não é uma certeza"', 1)
rep([C56], '"预报基于 ECMWF 等模型"', '"As previsões assentam em modelos como o ECMWF"', 1)
rep([C56], '"预报会变，因为大气变化快"', '"As previsões mudam porque a atmosfera muda depressa"', 1)
rep([C56], '"DPB 于 10 月 15 日送布鲁塞尔"', '"O DPB seguiu para Bruxelas a 15 de outubro"', 1)
rep([C56], '"2027 增长预测 +0,8%"', '"Crescimento previsto para 2027: +0,8%"', 1)
rep([C56], '"è probabile che + 虚拟式 piova"', '"è probabile che + conjuntivo piova"', 1)
rep([C56], '"è possibile che + 虚拟式 nevichi"', '"è possibile che + conjuntivo nevichi"', 1)
rep([C56], '"bisogna che + 虚拟式 controllino"', '"bisogna che + conjuntivo controllino"', 1)
rep([C56], '"è importante che + 虚拟式 sia"', '"è importante che + conjuntivo sia"', 1)
rep([C56], '"probabilità = 概率"', '"probabilità = probabilidade"', 1)
rep([C56], '"media = 平均值"', '"media = média"', 1)
rep([C56], '"bollettino = 预报公报"', '"bollettino = boletim de previsão"', 1)
rep([C56], '"modello = 预报模型"', '"modello = modelo de previsão"', 1)

# ---------- exercise notes, page 7 ----------
rep([C7], '"piovere 天气动词：piove"', '"piovere, verbo do tempo: piove"', 1)
rep([C7], '"fa freddo = 天气冷"', '"fa freddo = está frio"', 1)
rep([C7], '"nevicare：nevica"', '"nevicare: nevica"', 1)
rep([C7], '"“我冷”说 ho freddo"', '"«Tenho frio» é ho freddo"', 1)
rep([C7], '"arrivare 用 essere：è arrivato"', '"arrivare leva essere: è arrivato"', 1)
rep([C7], '"assaggiare 用 avere"', '"assaggiare leva avere"', 1)
rep([C7], '"andare 用 essere，复数 sono andati"', '"andare leva essere, plural sono andati"', 1)
rep([C7], '"aprire 用 avere + 不变分词"', '"aprire leva avere + particípio invariável"', 1)
rep([C7], '"è probabile che + 虚拟式 piova"', '"è probabile che + conjuntivo piova"', 1)
rep([C7], '"è possibile che + 虚拟式 nevichi"', '"è possibile che + conjuntivo nevichi"', 1)
rep([C7], '"bisogna che + 虚拟式 sia"', '"bisogna che + conjuntivo sia"', 1)
rep([C7], '"so che + 陈述式 arriva"', '"so che + indicativo arriva"', 1)

# ---------- exercise notes, page 8 ----------
rep([C8], '"primo freddo = 第一场寒冷"', '"primo freddo = o primeiro frio"', 1)
rep([C8], '"追思日在 11 月 2 日"', '"O Dia de Finados é a 2 de novembro"', 1)
rep([C8], '"文化论坛在米兰开幕"', '"O Forum Cultura abre em Milão"', 1)
rep([C8], '"潘妮托尼决赛在周六日"', '"A final do Panettone é no sábado e no domingo"', 1)
rep([C8], '"牛轧糖节在克雷莫纳"', '"A Festa del Torrone é em Cremona"', 1)
rep([C8], '"意甲第 11 轮周日收官：chiude"', '"A jornada 11 da Serie A fecha no domingo: chiude"', 1)
rep([C8], '"佛罗伦萨对尤文图斯在周日晚上"', '"Fiorentina–Juventus joga-se no domingo à noite"', 1)
rep([C8], '"民俗电影节在佛罗伦萨"', '"O Festival dei Popoli é em Florença"', 1)
rep([C8], '"初雪在 1300–1500 米左右"', '"A primeira neve cai por volta de 1.300–1.500 metros"', 1)
rep([C8], '"追思日的花是菊花"', '"A flor do dia 2 de novembro é o crisântemo"', 1)
rep([C8], '"潘妮托尼决赛有 19 国糕点师"', '"19 países enviam pasteleiros à final do Panettone"', 1)
rep([C8], '"文化论坛有 50 多场活动"', '"O Forum Cultura tem mais de 50 eventos"', 1)
rep([C8], '"阿尔巴松露节到 12 月 6 日"', '"A feira da trufa de Alba vai até 6 de dezembro"', 1)
rep([C8], '"DPB 于 10 月 15 日送出"', '"O DPB seguiu a 15 de outubro"', 1)
rep([C8], '"概率不等于确定"', '"Uma probabilidade não é uma certeza"', 1)
rep([C8], '"卢卡漫画节 11 月 1 日闭幕"', '"A Lucca Comics fechou a 1 de novembro"', 1)
rep([C8], '"Giulia 去米兰潘妮托尼决赛"', '"Giulia vai à final do Panettone em Milão"', 1)
rep([C8], '"Paolo 周六去牛轧糖节"', '"Paolo vai à Festa del Torrone no sábado"', 1)
rep([C8], '"传统潘妮托尼是 Giulia 品尝的"', '"O panettone tradicional é provado por Giulia"', 1)
rep([C8], '"标题概括两个城市、两个节日"', '"O título resume duas cidades e dois doces"', 1)
rep([C8], '"时间词在前"', '"Palavra de tempo primeiro"', 1)
rep([C8], '"主语 + essere + 地点 + 日期"', '"Sujeito + essere + lugar + data"', 1)
rep([C8], '"疑问词组在句首"', '"Expressão interrogativa primeiro"', 1)
rep([C8], '"主语 + 动词 + 时间"', '"Sujeito + verbo + tempo"', 1)
rep([C8], '"probabilità=可能性 d"', '"probabilità = possibilidade, d"', 1)
rep([C8], '"media=平均值 a"', '"media = média, a"', 1)
rep([C8], '"bollettino=预报公报 b"', '"bollettino = boletim de previsão, b"', 1)
rep([C8], '"modello=预报模型 c"', '"modello = modelo de previsão, c"', 1)
rep([C8], '"torrone = 牛轧糖"', '"torrone = torrão"', 1)
rep([C8], '"mandorle 杏仁"', '"mandorle = amêndoas"', 1)
rep([C8], '"quanto costa? 多少钱"', '"quanto costa? = quanto custa?"', 1)
rep([C8], '"pagare con carta 刷卡"', '"pagare con carta = pagar com cartão"', 1)
rep([C8], '"牛轧糖节持续到 11 月 22 日"', '"A Festa del Torrone vai até 22 de novembro"', 1)
# P8 H writing bridge + writing item (key is not printed for writing items;
# the note is printed as "150. ✓ <note>").
rep([C8], 'f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")',
    'f.bridge(f"Tarefa de escrita, sem resposta única; o texto modelo, {NWORDS} palavras, segue abaixo.")', 1)
rep([C8], '"（开放题，范文如下）"', '"(tarefa aberta — texto modelo abaixo)"', 1)
rep([C8], 'f"范文见本版 H 区（{NWORDS} 词）"', 'f"O texto modelo está na seção H desta página, {NWORDS} palavras"', 1)
# P8 answer-key titles + separators (W43 IT x PT shipped strings;
# answer lines switch from the core dash form to the W43 paren form)
rep([C8], '"RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可"',
    '"RISPOSTE · RESPOSTAS — organizadas por página: busque pelo número do exercício"', 1)
rep([C8], '"每题附一句中文简析 · 带 ✓ 的为范文题"',
    '"Uma nota breve em português para cada exercício · ✓ = exercício de escrita"', 1)
rep([C8], 'f"— PAGINA {pg} —"', 'f"— PÁGINA {pg} —"', 1)
rep([C8], 'txt = f"{e_[\'n\']}. {e_[\'key\']} — {e_[\'note\']}"',
    'txt = f"{e_[\'n\']}. {e_[\'key\']} ({e_[\'note\']})"', 1)
print("TRANSFORM DONE")

# ---------- FIX ROUND 1 (round-1 render defects) ----------
# (a) P7 col3 ended y=1831, past the FRASI rule at 1686 (core: 1673).
# Measured with the build's own wrap(): errori notes 2 and 3 wrapped
# to 2 lines each (core: 1), parola gloss 2 lines (core: 2, kept),
# letter Italian disclosure 2 lines, Portuguese note 4 lines (core
# Chinese note: 3). Shortenings below save 2+2+1+1+2 = 8 wrapped
# lines in col3 (wording only, no layout parameter change).
rep([C7], '"Nevicare só usa a terceira pessoa do singular."', '"Nevicare: só a terceira pessoa."', 1)
rep([C7], '"Previsões dão probabilidades, não certezas."', '"Probabilidades, não certezas."', 1)
rep([C7], '"assaggio = prova de um alimento, ver página 3."', '"assaggio = prova, página 3."', 2)
rep([C7], 'len(wrap("Esempio della redazione: non è ancora una lettera vera.", "sans", False, 20, CW - 44))',
    'len(wrap("Non è una lettera vera, è un esempio.", "sans", False, 20, CW - 44))', 1)
rep([C7], 'len(wrap("Exemplo da redação, não uma carta real: ainda não há cartas reais nem o melhor texto da página 8 — ambos prometidos para o VOL.3. Escrevam à redação!", "sans", False, 20, CW - 44))',
    'len(wrap("Sem cartas reais nem o melhor texto da página 8: escrevam para o VOL.3!", "sans", False, 20, CW - 44))', 1)
rep([C7], '"Esempio della redazione: non è ancora una lettera vera."',
    '"Non è una lettera vera, è un esempio."', 1)
rep([C7], '"Exemplo da redação, não uma carta real: ainda não há cartas reais nem o melhor texto da página 8 — ambos prometidos para o VOL.3. Escrevam à redação!"',
    '"Sem cartas reais nem o melhor texto da página 8: escrevam para o VOL.3!"', 1)
# (b) P8 keys flow overflowed (items 148-150 clamped past the footer
# zone): Portuguese notes wrapped to 2 lines on 8 items. Wording-only
# trims below, each verified 1 line at 13pt serif in width 434 with
# the build's own wrap(); no layout parameter changes. The #44/#134
# note string is shared by the P3 and P8 items (count 2).
rep([C34], '"Os jogos de domingo à noite são mais tarde que os de sexta: più tardi"', '"Domingo à noite é mais tarde que sexta: più tardi"', 1)
rep([C34], '"Os jogos de sexta são mais cedo que os de domingo: più presto"', '"Sexta é mais cedo que domingo: più presto"', 1)
rep([C34], '"più + bella: a noite de domingo é a mais bela, na opinião dos adeptos"', '"più + bella: a mais bela, segundo os adeptos"', 1)
rep([C56], '"Os números do gráfico são dados de treino, não previsões reais"', '"Dados de treino, não previsões reais"', 1)
rep([C12], '"O Dia de Todos os Santos cai num domingo este ano, sem ponte"', '"Todos os Santos cai num domingo, sem ponte"', 1)
rep([C34, C8], '"Sujeito + essere + lugar + data"', '"Sujeito, essere, lugar, data"', 2)
rep([C8], '"Expressão interrogativa primeiro"', '"Interrogativa primeiro"', 1)
print("TRANSFORM + FIX ROUND 1 DONE")

# ---------- FIX ROUND 2 (occlusion audit, round-2 render: 7 NEW flags, core 0) ----------
# All five are Portuguese text running longer than the Chinese original
# in a fixed-width, unwrapped slot (wording-only fixes, no layout
# parameter change except the day-note call, which gains the same
# max_w wrap every other note call already carries, and +4 box padding
# on the parola box whose height formula grazed its own ink by 1.1px).
# (a) P1 day-box subtitle overran the box right border (ink 1906.5).
rep([C12], '"ESTA SEMANA · Cosa succede, giorno per giorno"', '"ESTA SEMANA · Cosa succede"', 1)
# (b) P1 day-box note was printed with p.text (no wrapping at all),
# so the Portuguese sentence ran past the page edge (ink 2007.5) and
# its box border; print it with p.para wrapped at the box inner width
# like every other note (first baseline unchanged).
rep([C12], 'p.text(gx + 22, byy + 76, "Datas segundo os calendários dos eventos; os horários podem mudar.", 16.5, "sans", False, GREY)',
    'p.para(gx + 22, byy + 76, "Datas segundo os calendários dos eventos; os horários podem mudar.", 16.5, "sans", False, GREY, CW - 44, 1.35)', 1)
# (c) P1 sommario title overran the box right border (ink 1937.5).
rep([C12], '"IN QUESTO NUMERO · NESTE NÚMERO"', '"IN QUESTO NUMERO · ÍNDICE"', 1)
# (d) P1 parola translation wrapped to 2 lines and its second line
# struck the row-B rule at y=1864 (core Chinese: 1 line); shorten to
# one line (the Italian definition above already carries the detail).
rep([C12], '"«O primeiro frio»: o primeiro frio sério depois de um outono ameno."', '"«O primeiro frio» após um outono ameno."', 1)
# (e) P7 parola box title overran its box border by 1.8px.
rep([C7], '"LA PAROLA · A PALAVRA DA SEMANA"', '"LA PAROLA · A PALAVRA"', 1)
# (f) P7 parola box bottom ink grazed its own border by 1.1px
# (height-formula rounding); +4 padding, col3 still ends 1660.
rep([C7], 'wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("assaggio = prova, página 3.", "sans", False, 20, CW - 44)) * 29 + 20',
    'wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("assaggio = prova, página 3.", "sans", False, 20, CW - 44)) * 29 + 24', 1)
print("TRANSFORM + FIX ROUNDS 1-2 DONE")

# ---------- FIX ROUND 3 (coordinator ruling + P1 subtitle frame overflow) ----------
# (a) COORDINATOR RULING 2026-10-27: remove the Italian disclosure
# line added in fix round 1 — the core has no Italian disclosure
# sentence to retain, and none may be newly written. The Portuguese
# note is rewritten to carry the "exemplo" fact explicitly as well
# (example + no real letters + no best page-8 text + imperative
# invitation + VOL.3 publication promise), at 3 wrapped lines; col3
# still ends 1650 (rule at 1686).
rep([C7], 'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Non è una lettera vera, è un esempio.", "sans", False, 20, CW - 44)) * 29 + 12 + len(wrap("Sem cartas reais nem o melhor texto da página 8: escrevam para o VOL.3!", "sans", False, 20, CW - 44)) * 29 + 20',
    'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Exemplo da redação: sem cartas reais nem o melhor texto da página 8. Escrevam, saem no VOL.3!", "sans", False, 20, CW - 44)) * 29 + 20', 1)
rep([C7], 'yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10\nyy3 = p.para(bx + 22, yy3 + 20, "Non è una lettera vera, è un esempio.", 20, "sans", False, GREY, CW - 44, 1.42) + 10\np.para(bx + 22, yy3 + 20, "Sem cartas reais nem o melhor texto da página 8: escrevam para o VOL.3!", 20, "sans", False, GREY, CW - 44, 1.42)',
    'yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10\np.para(bx + 22, yy3 + 20, "Exemplo da redação: sem cartas reais nem o melhor texto da página 8. Escrevam, saem no VOL.3!", 20, "sans", False, GREY, CW - 44, 1.42)', 1)
# (b) P1 subtitle: the Portuguese strap line at 46pt serif bold has
# TRUE ink to x=1925, crossing both page-frame rects (1910/1922) —
# a real NEW overflow, not an advance artifact (core Chinese strap
# fits). Shorten by dropping the articles (strap-line topic tags).
rep([C12], '"SEMANÁRIO ITALIANO · VOL.2 · IL PRIMO FREDDO · IL PANETTONE · LA SERIE A"',
    '"SEMANÁRIO ITALIANO · VOL.2 · PRIMO FREDDO · PANETTONE · SERIE A"', 1)
print("TRANSFORM + FIX ROUNDS 1-3 DONE")
