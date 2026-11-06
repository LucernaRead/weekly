# -*- coding: utf-8 -*-
"""W45 zh-cn x pt fan-out transform: English explanation layer -> Portuguese.
Applies exact-literal replacements (line-based safety: whole literal matches,
assertion after each pair) to MY build copy only. Never run inside the core dir.
Order matters: longer/anchored forms first (see comments).
"""
import os, sys

BUILD = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-pt-reproof/work/repro-build")
FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]

# (old, new) applied to ALL files (counts reported; 0 hits = hard fail)
PAIRS = [
    # ---- bslib4 furniture (only present in bslib4.py; other files: 0 hits would fail,
    # so these are handled in FILE_PAIRS below, not here) ----
    # ---- global recurring labels ----
    ("Lucerna editors · Reading level A2→B1", "Redação Lucerna · Nível de leitura A2→B1"),
    ("Lucerna editors · Reading level A2", "Redação Lucerna · Nível de leitura A2"),
    ("Lucerna editors · Reading level B1", "Redação Lucerna · Nível de leitura B1"),
    ("Lucerna editors · Reading level B2", "Redação Lucerna · Nível de leitura B2"),
    ("Answers on page 8 · 答案见第 8 版", "Respostas na página 8 · 答案见第 8 版"),
    ("练习 · Exercises", "练习 · Exercícios"),
    ("A · 读一读选一选 · Read & choose", "A · 读一读选一选 · Leia e escolha"),
    ("B · 词语填空 · Word blanks", "B · 词语填空 · Complete"),
    ("D · 词语配对 · Matching", "D · 词语配对 · Associação"),
    ("说说你自己 · And you?", "说说你自己 · E você?"),
    ("Fill each blank with the right word.", "Complete cada espaço com a palavra certa."),
    ("Photo: ", "Foto: "),
    ('instr="Fill in the blank"', 'instr="Complete"'),
    ('instr="Fill in"', 'instr="Complete"'),
    ('instr="Match the words"', 'instr="Associe as palavras"'),
    # ---- shared exercise notes (same meaning everywhere they occur) ----
    ("JD.com spot sales began on Oct 12.", "Vendas imediatas da JD.com: 12 de outubro."),
    ("Spot sales run until Nov 13.", "As vendas imediatas vão até 13 de novembro."),
    ("This year many goods are marked down directly.", "Este ano, muitas mercadorias têm corte direto no preço."),
    ("Start of Winter is on Saturday, Nov 7.", "O Início do Inverno é no sábado, 7 de novembro."),
    ("Start of Winter falls on Saturday, Nov 7.", "O Início do Inverno cai no sábado, 7 de novembro."),
    ("直降 means the price itself drops.", "直降 significa que o preço em si cai."),
    ("jiǎozǐ — northern families eat these at 立冬.", "jiǎozǐ — as famílias do norte comem estes no 立冬."),
    ("lìdōng — Start of Winter, Nov 7.", "lìdōng — Início do Inverno, 7 de nov."),
    ("Quarter-finals start at 06:00 Beijing time.", "As quartas de final começam às 06:00, hora de Pequim."),
    ("The AI film runs 100 minutes.", "O filme de IA dura 100 minutos."),
    ("xiànhuò — goods in stock, ready to ship.", "xiànhuò — mercadoria em estoque, pronta para envio."),
    ("zhíjiàng — the price itself drops.", "zhíjiàng — o preço em si cai."),
    ("jiésuàn — the checkout page shows the real price.", "jiésuàn — a página de checkout mostra o preço real."),
]

# (filename, old, new) — file-specific pairs
FILE_PAIRS = [
    ("bslib4.py",
     "Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations",
     "Lucerna · SEMANÁRIO CHINÊS SIMPLIFICADO VOL.2 · TEXTOS EM CHINÊS SIMPLIFICADO · EXPLICAÇÕES EM PORTUGUÊS"),
    ("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"'),
    ("bslib4.py", '"Notes｜" + s', '"Nota — " + s'),
    # ---- P1 ----
    ("content12.py", "每周读中文 · Read real Chinese, every week", "每周读中文 · Leia chinês de verdade, toda semana"),
    ("content12.py", "简体中文版 · VOL.2 · 双11 · 立冬 · S16", "SEMANÁRIO CHINÊS SIMPLIFICADO · VOL.2 · 双11 · 立冬 · S16"),
    ("content12.py", "给学中文的人的周报 — Read the real China, in Chinese", "给学中文的人的周报 — Leia a China de verdade, em chinês"),
    ("content12.py", "简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers",
     "TEXTOS EM CHINÊS SIMPLIFICADO · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA"),
    ("content12.py", "Shopping week meets winter · see pages 2–3", "Semana de compras encontra o inverno · ver páginas 2–3"),
    ("content12.py", "头条 · Top story", "头条 · Manchete"),
    ("content12.py", "xiànhuò 现货 — goods in stock, ready to ship · lìjiǎn 立减 — an instant discount at checkout · zhíjiàng 直降 — a direct price cut · jiéqì 节气 — the 24 solar terms that divide the year.",
     "xiànhuò 现货 — mercadoria em estoque, pronta para envio · lìjiǎn 立减 — um desconto imediato no checkout · zhíjiàng 直降 — um corte direto no preço · jiéqì 节气 — os 24 termos solares que dividem o ano."),
    ("content12.py", "数字看本周 · This week in numbers", "数字看本周 · A semana em números"),
    ("content12.py", "Nov 13 — the last day of the spot-sale period", "13 de nov. — o último dia do período de vendas imediatas"),
    ("content12.py", "Nov 7, Saturday — 立冬 (Start of Winter)", "7 de nov., sábado — 立冬 (Início do Inverno)"),
    ("content12.py", "Oct 12, 20:00 — JD.com spot sales began", "12 de out., 20:00 — começaram as vendas imediatas da JD.com"),
    ("content12.py", "Nov 10, 20:00 — the peak sale (高潮场) begins next week", "10 de nov., 20:00 — a venda de pico (高潮场) começa na próxima semana"),
    ("content12.py", "即学即练 · Try it now", "即学即练 · Pratique já"),
    ("content12.py", "Taobao and Tmall pre-sales began on Oct 15.", "Pré-vendas do Taobao e do Tmall: 15 de outubro."),
    ("content12.py", "Start of Winter is winter's first solar term.", "O Início do Inverno é o primeiro termo solar do inverno."),
    ("content12.py", "本周日历 · This week", "本周日历 · Esta semana"),
    ("content12.py", "11月2日—8日 · Nov 2–8", "11月2日—8日 · 2–8 de nov."),
    ("content12.py", "What happens this week", "O que acontece esta semana"),
    ("content12.py", "The Swiss stage ends Nov 1, so the quarter-final teams are not known at press time. Quarter-finals run Nov 4–7, the first semi-final Nov 8, all at 06:00 Beijing time.",
     "A fase suíça termina em 1º de novembro, por isso as equipes das quartas de final ainda não são conhecidas no fechamento. As quartas de final vão de 4 a 7 de novembro, a primeira semifinal é em 8 de novembro, todas às 06:00, hora de Pequim."),
    ("content12.py", "All times Beijing time", "Todos os horários são de Pequim"),
    ("content12.py", "S16 teams depend on the Swiss stage", "As equipes do S16 dependem da fase suíça"),
    ("content12.py", "本期目录 · Contents", "本期目录 · Nesta edição"),
    ("content12.py", "本周词 · Word of the week", "本周词 · Palavra da semana"),
    ("content12.py", "「立冬」 lìdōng — Start of Winter: the first solar term of winter. 立冬到了,冬天要来了。Example: 「立冬那天,我们吃饺子。」",
     "「立冬」 lìdōng — Início do Inverno: o primeiro termo solar do inverno. 立冬到了,冬天要来了。Exemplo: 「立冬那天,我们吃饺子。」"),
    ("content12.py", "快讯 · Briefs", "快讯 · Em resumo"),
    ("content12.py", "闪电问答 · Quick quiz", "闪电问答 · Quiz-relâmpago"),
    ("content12.py", "Read page 1 and choose · 答案见第 8 版", "Leia a página 1 e escolha · 答案见第 8 版"),
    # ---- P2 ----
    ("content12.py", "Level A2 · 双11购物生活 · 立冬生活 · Shopping & the first winter days", "Nível A2 · 双11购物生活 · 立冬生活 · Compras e os primeiros dias de inverno"),
    ("content12.py", "cāngkù 仓库 — a warehouse · píngjià 评价 — a review, what buyers say · chǐmǎ 尺码 — a size · tuìhuànhuò 退换货 — returns and exchanges.",
     "cāngkù 仓库 — um armazém · píngjià 评价 — uma avaliação, o que os compradores dizem · chǐmǎ 尺码 — um tamanho · tuìhuànhuò 退换货 — devoluções e trocas."),
    ("content12.py", "满减与直降 · Old vs new", "满减与直降 · Antigo vs. novo"),
    ("content12.py", "The old rule many shoppers knew was 「满300减50」 (spend 300 yuan, save 50). This year the common pattern is 直降 (zhíjiàng): the price itself drops, and the checkout price is what you pay. The example below uses practice numbers, not real shop prices.",
     "A regra antiga que muitos compradores conheciam era 「满300减50」 (gastar 300 yuan, economizar 50). Este ano, o padrão comum é o 直降 (zhíjiàng): o preço em si cai, e o preço do checkout é o que você paga. O exemplo abaixo usa números de prática, não preços reais de loja."),
    ("content12.py", "Practice example · 练习例子", "Exemplo prático · 练习例子"),
    ("content12.py", "bǔdōng 补冬 — eating well before winter · jiāozǐ 饺子 — dumplings · cíbā 糍粑 — sticky rice cakes · qīzhōng 期中 — mid-term (exams).",
     "bǔdōng 补冬 — comer bem antes do inverno · jiāozǐ 饺子 — bolinhos recheados · cíbā 糍粑 — bolos de arroz glutinoso · qīzhōng 期中 — provas de meio de período."),
    ("content12.py", "本周生活小日历 · This week's dates", "本周生活小日历 · Datas da semana"),
    ("content12.py", "你知道吗 · Did you know?", "你知道吗 · Você sabia?"),
    ("content12.py", "And you? What do you want to buy this 双11? What would you eat on 立冬? Write two sentences in Chinese.",
     "E você? O que você quer comprar neste 双11? O que você comeria no 立冬? Escreva duas frases em chinês."),
    ("content12.py", "购物词语卡 · Shopping words", "购物词语卡 · Palavras de compras"),
    ("content12.py", "Four words you will see on every shopping app", "Quatro palavras que você verá em todo aplicativo de compras"),
    ("content12.py", '("现货", "xiànhuò · goods in stock", "in stock now, ready to ship")', '("现货", "xiànhuò · mercadoria em estoque", "em estoque agora, pronta para envio")'),
    ("content12.py", '("直降", "zhíjiàng · a direct price cut", "the price drops directly, no maths")', '("直降", "zhíjiàng · um corte direto no preço", "o preço cai diretamente, sem contas")'),
    ("content12.py", '("立减", "lìjiǎn · an instant discount", "taken off at checkout")', '("立减", "lìjiǎn · um desconto imediato", "descontado no checkout")'),
    ("content12.py", '("补冬", "bǔdōng · winter nourishment", "eating well before winter")', '("补冬", "bǔdōng · reforço para o inverno", "comer bem antes do inverno")'),
    ("content12.py", "Remember the sentence: 「买现货不用等,先看结算页,再付款。」", "Lembre-se da frase: 「买现货不用等,先看结算页,再付款。」"),
    ("content12.py", "Read page 2 and choose the best answer.", "Leia a página 2 e escolha a melhor resposta."),
    ("content12.py", "Taobao and Tmall spot sales began on Oct 20.", "Vendas imediatas do Taobao e do Tmall: 20 de outubro."),
    ("content12.py", "After 立冬 the weather gets colder day by day.", "O tempo fica mais frio dia a dia depois do 立冬."),
    ("content12.py", "The WeChat shop event runs until Nov 15.", "O evento da loja do WeChat vai até 15 de novembro."),
    ("content12.py", "qīzhōng — mid-term exams fall in early November in some schools.", "qīzhōng — as provas de meio de período caem no início de novembro em algumas escolas."),
    ("content12.py", "Use the practice example on this page.", "Use o exemplo prático desta página."),
    ("content12.py", "The sweater costs 240 yuan in the example.", "O suéter custa 240 yuan no exemplo."),
    ("content12.py", "240 + 80 = 320 yuan together.", "240 + 80 = 320 yuan juntos."),
    ("content12.py", "320 − 50 = 270 yuan after the direct cut.", "320 − 50 = 270 yuan depois do corte direto."),
    ("content12.py", "The WeChat shop event runs 35 days in total.", "O evento da loja do WeChat dura 35 dias no total."),
    ("content12.py", '["xiànhuò 现货 = in stock, b", "zhíjiàng 直降 = price drops, d", "lìjiǎn 立减 = off at checkout, c", "bǔdōng 补冬 = eat well before winter, a"]',
     '["xiànhuò 现货 = em estoque, b", "zhíjiàng 直降 = o preço cai, d", "lìjiǎn 立减 = desconto no checkout, c", "bǔdōng 补冬 = comer bem antes do inverno, a"]'),
]

FILE_PAIRS += [
    # ---- P3 ----
    ("content34.py", "Level A2→B1 · 立冬:冬天的第一个节气 · Start of Winter", "Nível A2→B1 · 立冬:冬天的第一个节气 · Início do Inverno"),
    ("content34.py", "hòu 候 — a five-day micro-season · jiāotì 交替 — one thing giving way to another · cǎifǎng 采访 — to interview, to report from the scene.",
     "hòu 候 — uma microestação de cinco dias · jiāotì 交替 — uma coisa dando lugar a outra · cǎifǎng 采访 — entrevistar, reportar do local."),
    ("content34.py", "hòu yīfu 厚衣服 — warm clothes · rè fàn 热饭 — a hot meal · zháoliáng 着凉 — to catch cold.",
     "hòu yīfu 厚衣服 — roupas quentes · rè fàn 热饭 — uma refeição quente · zháoliáng 着凉 — pegar um resfriado."),
    ("content34.py", "节日小日历 · Festival dates", "节日小日历 · Datas das festas"),
    ("content34.py", "And you? What would you eat on 立冬? Is it cold where you live? Write two sentences in Chinese.",
     "E você? O que você comeria no 立冬? Faz frio onde você mora? Escreva duas frases em chinês."),
    ("content34.py", "Read page 3 and choose the best answer.", "Leia a página 3 e escolha a melhor resposta."),
    ("content34.py", "立冬 is the 19th of the 24 solar terms.", "立冬 é o 19º dos 24 termos solares."),
    ("content34.py", "First micro-season: water begins to freeze.", "Primeira microestação: a água começa a congelar."),
    ("content34.py", "Northern families eat dumplings at 立冬.", "As famílias do norte comem bolinhos no 立冬."),
    ("content34.py", "A journalist interviews people and writes the news.", "Um jornalista entrevista pessoas e escreve as notícias."),
    ("content34.py", "shuǐ shǐ bīng — water begins to freeze (1st micro-season).", "shuǐ shǐ bīng — a água começa a congelar (1ª microestação)."),
    ("content34.py", "tāngyuán — sticky rice balls eaten in some southern places.", "tāngyuán — bolinhos de arroz glutinoso comidos em alguns lugares do sul."),
    ("content34.py", "jìzhě — a journalist interviews and writes news.", "jìzhě — um jornalista entrevista e escreve notícias."),
    ("content34.py", "Answer with dates and numbers from page 3.", "Responda com datas e números da página 3."),
    ("content34.py", "立冬 is the 19th solar term.", "立冬 é o 19º termo solar."),
    ("content34.py", "Start of Winter is on Nov 7.", "O Início do Inverno é em 7 de novembro."),
    ("content34.py", "The solar-term moment is 17:52.", "O momento do termo solar é às 17h52."),
    ("content34.py", "Journalists' Day is on Nov 8.", "O Dia dos Jornalistas é em 8 de novembro."),
    ("content34.py", '["水始冰 = water begins to freeze, b", "地始冻 = earth begins to freeze, c", "雉入大水为蜃 = the old pheasant story, d", "bǔdōng 补冬 = eat well before winter, a"]',
     '["水始冰 = a água começa a congelar, b", "地始冻 = a terra começa a congelar, c", "雉入大水为蜃 = a velha história do faisão, d", "bǔdōng 补冬 = comer bem antes do inverno, a"]'),
    # ---- P4 ----
    ("content34.py", "Level B1 · S16 瑞士轮与淘汰赛 · Worlds S16: Swiss stage & knockouts", "Nível B1 · S16 瑞士轮与淘汰赛 · Mundial S16: fase suíça e mata-mata"),
    ("content34.py", "S16 赛程 · S16 schedule (Beijing time)", "S16 赛程 · Calendário do S16 (horário de Pequim)"),
    ("content34.py", "Standings as of Oct 27, 2026: GEN and DK already 3–0 and through; AL and TSW 0–3 and out. Source: Sina Sports S16 guide (Beijing times) and match reports, Oct 26–27.",
     "Classificação em 27 de outubro de 2026: GEN e DK já estão 3–0 e classificados; AL e TSW 0–3 e eliminados. Fonte: guia S16 do Sina Sports (horários de Pequim) e reportagens de jogos, 26–27 de outubro."),
    ("content34.py", "体育小日历 · Sports dates", "体育小日历 · Datas do esporte"),
    ("content34.py", '("通宵", "tōngxiāo — to stay up all night for a match.")', '("通宵", "tōngxiāo — ficar acordado a noite toda por um jogo.")'),
    ("content34.py", '("加油", "jiāyóu — come on! (what fans shout).")', '("加油", "jiāyóu — vamos! (o que os torcedores gritam).")'),
    ("content34.py", '("翻盘", "fānpán — a comeback win, turning a game around.")', '("翻盘", "fānpán — uma virada, virar um jogo.")'),
    ("content34.py", "看比赛的中文 · Match words", "看比赛的中文 · Palavras do jogo"),
    ("content34.py", "Read page 4 and choose the best answer.", "Leia a página 4 e escolha a melhor resposta."),
    ("content34.py", "The Swiss stage is played in Allen, Texas.", "A fase suíça é jogada em Allen, no Texas."),
    ("content34.py", "AL lost all three of its Swiss-stage series.", "A AL perdeu as três séries da fase suíça."),
    ("content34.py", "IG beat HLE on Oct 26.", "A IG venceu a HLE em 26 de outubro."),
    ("content34.py", "The final starts at 03:00 Beijing time on Nov 15.", "A final: 15 de novembro, 03:00, hora de Pequim."),
    ("content34.py", "Àilún — Allen, Texas, hosts the Swiss stage.", "Àilún — Allen, no Texas, sedia a fase suíça."),
    ("content34.py", "nèizhàn — AL lost the all-LPL match to TES.", "nèizhàn — a AL perdeu o jogo interno da LPL para a TES."),
    ("content34.py", "táotài — three wins send a team to the knockouts.", "táotài — três vitórias levam um time ao mata-mata."),
    ("content34.py", "fānpán — TES turned the game against G2 around.", "fānpán — a TES virou o jogo contra a G2."),
    ("content34.py", "jiāyóu — what fans shout for their team.", "jiāyóu — o que os torcedores gritam pelo seu time."),
    ("content34.py", "Read the schedule on page 4.", "Leia o calendário da página 4."),
    ("content34.py", "Three wins send a team through from the Swiss stage.", "Três vitórias levam um time adiante na fase suíça."),
    ("content34.py", "AL won zero series in the Swiss stage.", "A AL não venceu nenhuma série na fase suíça."),
    ("content34.py", "The Swiss stage runs until Nov 1.", "A fase suíça vai até 1º de novembro."),
    ("content34.py", '["瑞士轮 = the Swiss stage, d", "内战 = an all-region match, c", "淘汰赛 = loser goes home, b", "总决赛 = the final, a"]',
     '["瑞士轮 = a fase suíça, d", "内战 = um jogo interno da região, c", "淘汰赛 = quem perde vai para casa, b", "总决赛 = a final, a"]'),
    # ---- P5 ----
    ("content56.py", "Level B1 · AI电影 · 立冬新片 · AI films & a winter film", "Nível B1 · AI电影 · 立冬新片 · Filmes de IA e um filme de inverno"),
    ("content56.py", "shùzì xíngxiàng 数字形象 — a digital character · gōngyìng 公映 — a public cinema release · piàofáng 票房 — box-office takings.",
     "shùzì xíngxiàng 数字形象 — um personagem digital · gōngyìng 公映 — um lançamento público no cinema · piàofáng 票房 — a bilheteria."),
    ("content56.py", "huǒhuà 火化 — cremation · jiùshú 救赎 — redemption, saving each other · yǐhòu 以后 — later, some other day.",
     "huǒhuà 火化 — cremação · jiùshú 救赎 — redenção, salvar um ao outro · yǐhòu 以后 — depois, um outro dia."),
    ("content56.py", "这一周的高频词 · Words of the week", "这一周的高频词 · Palavras-chave"),
    ("content56.py", "AI电影 — a film made with AI: no live actors, digital characters only.", "AI电影 — um filme feito com IA: sem atores reais, só personagens digitais."),
    ("content56.py", "电影小日历 · Film dates", "电影小日历 · Datas dos filmes"),
    ("content56.py", "And you? Would you watch a film made by AI? Who would you watch a film with on 立冬? Write two sentences in Chinese.",
     "E você? Você assistiria a um filme feito por IA? Com quem você assistiria a um filme no 立冬? Escreva duas frases em chinês."),
    ("content56.py", "Read page 5 and choose the best answer.", "Leia a página 5 e escolha a melhor resposta."),
    ("content56.py", "The AI film has no live actors.", "O filme de IA não tem atores reais."),
    ("content56.py", "By noon on Oct 26, Maoyan showed about 1.192 million yuan.", "Ao meio-dia de 26 de outubro, o Maoyan mostrava cerca de 1,192 milhão de yuan."),
    ("content56.py", "The new film opens on Nov 7, Start of Winter.", "O novo filme estreia em 7 de novembro, Início do Inverno."),
    ("content56.py", "Huang Yan is a crematory worker.", "Huang Yan é funcionária de crematório."),
    ("content56.py", "shùzì — the film's characters are digital images.", "shùzì — os personagens do filme são imagens digitais."),
    ("content56.py", "piàofáng — box-office takings, about 1.192 million yuan.", "piàofáng — a bilheteria, cerca de 1,192 milhão de yuan."),
    ("content56.py", "huǒhuà — Huang Yan works at a crematory.", "huǒhuà — Huang Yan trabalha num crematório."),
    ("content56.py", "jiùshú — the two women save each other.", "jiùshú — as duas mulheres salvam uma à outra."),
    ("content56.py", "lìdōng — the new film opens on Start of Winter.", "lìdōng — o novo filme estreia no Início do Inverno."),
    ("content56.py", "Answer with dates and numbers from page 5.", "Responda com datas e números da página 5."),
    ("content56.py", "The AI film opened on Oct 23.", "O filme de IA estreou em 23 de outubro."),
    ("content56.py", "On Oct 24–25, each screening averaged 2 viewers.", "24–25 de outubro: média de 2 espectadores por sessão."),
    ("content56.py", "The new film runs 114 minutes.", "O novo filme dura 114 minutos."),
    ("content56.py", '["数字形象 = a digital character, b", "票房 = box-office takings, a", "火化师 = a crematory worker, d", "救赎 = saving each other, c"]',
     '["数字形象 = um personagem digital, b", "票房 = a bilheteria, a", "火化师 = uma funcionária de crematório, d", "救赎 = salvar um ao outro, c"]'),
    # ---- P6 ----
    ("content56.py", "Level B2 · 双11深读 · Why the rules got simpler", "Nível B2 · 双11深读 · Por que as regras ficaram mais simples"),
    ("content56.py", "jiésuàn 结算 — checkout, settling the bill · yùnfèi 运费 — delivery cost · guǎnggào 广告 — an advertisement.",
     "jiésuàn 结算 — checkout, o acerto da conta · yùnfèi 运费 — custo de entrega · guǎnggào 广告 — uma propaganda."),
    ("content56.py", "shuōfǎ 说法 — a claim, what someone says · shùjù 数据 — data, measured numbers · tuìhuànhuò 退换货 — returns and exchanges.",
     "shuōfǎ 说法 — uma afirmação, o que alguém diz · shùjù 数据 — dados, números medidos · tuìhuànhuò 退换货 — devoluções e trocas."),
    ("content56.py", "三个练习篮子:直降以后实付多少钱 · Practice baskets", "三个练习篮子:直降以后实付多少钱 · Cestas de prática"),
    ("content56.py", "Bars are drawn from 0 (3 px = 1 yuan). Practice data only — not real shop prices. Basket maths is in the article above.",
     "As barras partem de 0 (3 px = 1 yuan). Apenas dados de prática — não são preços reais de loja. As contas das cestas estão no artigo acima."),
    ("content56.py", "深读要点 · Key points", "深读要点 · Pontos-chave"),
    ("content56.py", "读新闻三问 · Three questions", "读新闻三问 · Três perguntas"),
    ("content56.py", "And you? What do you check before you buy? Write two sentences in Chinese.",
     "E você? O que você verifica antes de comprar? Escreva duas frases em chinês."),
    ("content56.py", "Read page 6 and choose the best answer.", "Leia a página 6 e escolha a melhor resposta."),
    ("content56.py", "This year spot sales are much bigger.", "Este ano, as vendas imediatas são bem maiores."),
    ("content56.py", "With 直降 the checkout price is what you pay.", "Com o 直降 o preço do checkout é o que você paga."),
    ("content56.py", "AI helps you check prices and reviews first.", "A IA ajuda você a verificar preços e avaliações primeiro."),
    ("content56.py", "The WeChat shop event runs 35 days.", "O evento da loja do WeChat dura 35 dias."),
    ("content56.py", "The checkout page shows what you really pay.", "A página de checkout mostra o que você realmente paga."),
    ("content56.py", "yùnfèi — delivery cost, check whether it is included.", "yùnfèi — custo de entrega, verifique se está incluído."),
    ("content56.py", "guǎnggào — an advertisement's 'lowest price' needs checking.", "guǎnggào — o 'preço mais baixo' de uma propaganda precisa ser verificado."),
    ("content56.py", "Compute from the practice baskets.", "Calcule a partir das cestas de prática."),
    ("content56.py", "240 + 80 = 320, minus 50 = 270 yuan.", "240 + 80 = 320, menos 50 = 270 yuan."),
    ("content56.py", "199 − 20 = 179 yuan.", "199 − 20 = 179 yuan."),
    ("content56.py", "120 + 40 = 160 yuan, no direct cut.", "120 + 40 = 160 yuan, sem corte direto."),
    ("content56.py", "Basket A is cut by 50 yuan.", "A cesta A tem corte de 50 yuan."),
    ("content56.py", '["说法 = a claim, c", "数据 = measured numbers, d", "结算页 = the checkout page, b", "运费 = delivery cost, a"]',
     '["说法 = uma afirmação, c", "数据 = números medidos, d", "结算页 = a página de checkout, b", "运费 = custo de entrega, a"]'),
]

# second global batch (appended after audit of part 1)
PAIRS2 = [
    ("bǔdōng — eating well before winter.", "bǔdōng — comer bem antes do inverno."),
    ("C · 数字与日期 · Numbers", "C · 数字与日期 · Números e datas"),
]

FILE_PAIRS += [
    # ---- P2/P3/P4/P5/P6 band titles + C heads (missed in part 1/2) ----
    ("content12.py", "生活 · Life", "生活 · Vida"),
    ("content34.py", "文化 · Culture", "文化 · Cultura"),
    ("content34.py", "体育 · Sport", "体育 · Esporte"),
    ("content34.py", "C · 读赛程 · Schedule work", "C · 读赛程 · Leia o calendário"),
    # Fix-round consolidation (Gate 10 B-1): P4 feature gloss was fixed
    # afterwards in the PT build copy and never folded back; it belongs
    # here as a transform pair, not a build-copy one-off.
    ("content34.py", "tǎotài 淘汰 — to knock out, to eliminate · nèizhàn 内战 — a match between two teams from the same region · zhǐbù 止步 — to stop here, to go no further.",
     "tǎotài 淘汰 — eliminar, tirar do torneio · nèizhàn 内战 — um jogo entre dois times da mesma região · zhǐbù 止步 — parar aqui, não ir adiante."),
    ("content56.py", "青年 · Youth", "青年 · Juventude"),
    ("content56.py", "深读 · Deep read", "深读 · Leitura profunda"),
    ("content56.py", "C · 时间与数字 · Times & numbers", "C · 时间与数字 · Datas e horas"),
    # Fix-round consolidation (Gate 10 B-1): leftover-English sweep caught
    # the P5 photo credit in the PT build copy; folded back here. The old
    # side is the post-global form (global "Photo: " -> "Foto: " runs first).
    ("content56.py", "Foto: Based5290 — Public domain (Wikimedia Commons)", "Foto: Based5290 — Domínio público (Wikimedia Commons)"),
    ("content56.py", "C · 练习篮子算一算 · Basket maths", "C · 练习篮子算一算 · Cálculos"),
    # ---- P7 ----
    ("content7.py", "词语 · Language focus", "词语 · Foco na língua"),
    ("content7.py", "语言聚焦 · 三个级别,三个主题 · Three levels, three topics", "语言聚焦 · 三个级别,三个主题 · Três níveis, três temas"),
    ("content7.py", "A2 · 双11与冬天 · Shopping", "A2 · 双11与冬天 · Compras"),
    ("content7.py", "Shopping words for this week: 现货 (xiànhuò, in stock), 直降 (zhíjiàng, a direct cut), 立减 (lìjiǎn, off at checkout), 结算页 (jiésuàn yè, the checkout page). Winter words: 立冬 (lìdōng, Start of Winter), 补冬 (bǔdōng, eating well before winter), 厚衣服 (hòu yīfu, warm clothes).",
     "Palavras de compras desta semana: 现货 (xiànhuò, em estoque), 直降 (zhíjiàng, um corte direto), 立减 (lìjiǎn, desconto no checkout), 结算页 (jiésuàn yè, a página de checkout). Palavras de inverno: 立冬 (lìdōng, Início do Inverno), 补冬 (bǔdōng, comer bem antes do inverno), 厚衣服 (hòu yīfu, roupas quentes)."),
    ("content7.py", "Measure words still matter: 一件毛衣 (a sweater), 一条围巾 (a scarf), 一部电影 (a film).",
     "Os classificadores ainda importam: 一件毛衣 (um suéter), 一条围巾 (um cachecol), 一部电影 (um filme)."),
    ("content7.py", "毛衣 takes the measure word 件 jiàn.", "毛衣 usa o classificador 件 jiàn."),
    ("content7.py", "Clothes take 件, not 个 or 条.", "Roupas usam 件, não 个 nem 条."),
    ("content7.py", "One more to practise: 「这件毛衣多少钱?」 (How much is this sweater?) When you shop, ask the price first, then pay.",
     "Mais um para praticar: 「这件毛衣多少钱?」 (Quanto custa este suéter?) Quando fizer compras, pergunte o preço primeiro e só depois pague."),
    ("content7.py", "B1 · 时间与日期 · Time & dates", "B1 · 时间与日期 · Hora e datas"),
    ("content7.py", "Chinese gives times big → small: year, month, day, weekday, part of day, hour. Examples from this issue: 「11月7日星期六17点52分」 (Sat Nov 7, 17:52), 「11月10日星期二20点」 (Tue Nov 10, 20:00), 「11月15日凌晨3点」 (Nov 15, 3 a.m.). The biggest unit first, nothing out of order.",
     "O chinês dá os horários do maior para o menor: ano, mês, dia, dia da semana, parte do dia, hora. Exemplos desta edição: 「11月7日星期六17点52分」 (sáb. 7 de nov., 17h52), 「11月10日星期二20点」 (ter. 10 de nov., 20h), 「11月15日凌晨3点」 (15 de nov., 3h da manhã). A maior unidade primeiro, nada fora de ordem."),
    ("content7.py", "So English «Saturday evening, Nov 7» becomes 11月7日星期六晚上.", "Assim, «sábado à noite, 7 de novembro» vira 11月7日星期六晚上."),
    ("content7.py", "凌晨 língchén — the small hours after midnight.", "凌晨 língchén — as horas pequenas depois da meia-noite."),
    ("content7.py", "06:00 is 早上 (morning), not evening.", "06:00 é 早上 (manhã), não noite."),
    ("content7.py", "Big → small order: Nov 7, Saturday, 17:52.", "Ordem do maior para o menor: 7 de nov., sábado, 17h52."),
    ("content7.py", "Nov 7 is a Saturday — 周六.", "7 de novembro é sábado — 周六."),
    ("content7.py", "Two more words: 凌晨 (língchén) is the small hours after midnight, before dawn; 傍晚 (bàngwǎn) is the short stretch just before dark.",
     "Mais duas palavras: 凌晨 (língchén) são as horas pequenas depois da meia-noite, antes do amanhecer; 傍晚 (bàngwǎn) é o trechinho logo antes de escurecer."),
    ("content7.py", "B2 · 读新闻 · Reading the news", "B2 · 读新闻 · Lendo as notícias"),
    ("content7.py", "When a story involves a claim (说法), separate three kinds of sentence: claims (说法), data (数据) and advertisements (广告). Page 6 is the example: 「最低价」 is a claim, the practice baskets' 270元 is practice data, and the checkout page shows what you really pay.",
     "Quando uma notícia envolve uma afirmação (说法), separe três tipos de frase: afirmações (说法), dados (数据) e propagandas (广告). A página 6 é o exemplo: 「最低价」 é uma afirmação, os 270元 das cestas de prática são dados de prática, e a página de checkout mostra o que você realmente paga."),
    ("content7.py", "Ask of every price: whose number is it, and where is it written?", "Pergunte de cada preço: de quem é o número, e onde ele está escrito?"),
    ("content7.py", "「最低价」 is an advertising claim, not measured data.", "「最低价」 é propaganda, não dado medido."),
    ("content7.py", "shùjù — measured numbers, not claims.", "shùjù — números medidos, não afirmações."),
    ("content7.py", "Data and the checkout page first; the headline last.", "Dados e checkout primeiro; a manchete por último."),
    ("content7.py", "Try it yourself: in the page-1 calendar box, 「11月7日」 is a date — data. The words in an advertisement are claims. Can you tell them apart?",
     "Tente você: na caixa de calendário da página 1, 「11月7日」 é uma data — um dado. As palavras de uma propaganda são afirmações. Você sabe distingui-las?"),
    ("content7.py", "易错诊所 · Error clinic", "易错诊所 · Clínica de erros"),
    ("content7.py", "地 (de) marks how an action is done.", "地 (de) marca como uma ação é feita."),
    ("content7.py", "得 (de) links verb + degree: 跑得快.", "得 (de) liga verbo + grau: 跑得快."),
    ("content7.py", "Order: number + measure word + noun. The final 个 is one too many; sweaters take 件.", "Ordem: número + classificador + substantivo. O 个 final é um a mais; suéteres usam 件."),
    ("content7.py", "Times go big → small: weekday last.", "Maior → menor: dia da semana por último."),
    ("content7.py", "本周句式 · Sentence frame", "本周句式 · Estrutura da semana"),
    ("content7.py", "「先看评价,再下单。」(First check the reviews, then order.) The frame 先…再… gives the order of actions. More: 「先看天气,再出门。」",
     "「先看评价,再下单。」(Primeiro veja as avaliações, depois faça o pedido.) A estrutura 先…再… dá a ordem das ações. Mais: 「先看天气,再出门。」"),
    ("content7.py", "Frame: 先 … 再 … — first X, then Y.", "先 … 再 … — primeiro X, depois Y."),
    ("content7.py", "读者园地 · Readers' corner", "读者园地 · Cantinho dos leitores"),
    # Readers' corner disclosure: core's bilingual (Chinese + English) disclosure is
    # INHERITED in content and rendered in Portuguese only — the PT text below is
    # self-contained (label + VOL.1 promise + none arrived + deferred-not-cancelled
    # + EXPLICIT invitation). Measured at exactly 10 wrapped lines, same as the
    # core's lcn, so P7 col3/teaser geometry is unchanged.
    ("content7.py", "编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。Editor's note: VOL.1 promised real letters and the best VOL.1 writing in VOL.2. None have arrived, so this corner still prints an editor's example. Deferred, not cancelled.",
     "Exemplo da redação — não é uma carta de verdade. O VOL.1 prometeu cartas verdadeiras dos leitores e o melhor texto do VOL.1 neste VOL.2; até agora nenhuma carta chegou e não há texto publicável, por isso este cantinho ainda traz um exemplo da redação. Adiado, não cancelado. Escreva-nos! Envie a sua carta em chinês — duas frases já bastam — e ela pode sair no próximo número."),
    ("content7.py", "本周金句 · Phrases of the week (verbatim, from this issue's own articles)", "本周金句 · Frases da semana (textuais, dos artigos desta edição)"),
    ("content7.py", '("「不用等11月11日」", "No need to wait for Nov 11.", "p. 1")', '("「不用等11月11日」", "Não é preciso esperar até 11 de novembro.", "Página 1")'),
    ("content7.py", '("「下单就能发货」", "Order it and it ships.", "p. 2")', '("「下单就能发货」", "Fez o pedido e já despacha.", "Página 2")'),
    ("content7.py", '("「先看结算页,再付款」", "Check the checkout page, then pay.", "p. 2")', '("「先看结算页,再付款」", "Veja a página de checkout e só depois pague.", "Página 2")'),
    ("content7.py", '("「水开始结冰」", "The water begins to freeze.", "p. 3")', '("「水开始结冰」", "A água começa a congelar.", "Página 3")'),
    ("content7.py", '("「三场都输了」", "All three series lost.", "p. 4")', '("「三场都输了」", "As três séries perdidas.", "Página 4")'),
    ("content7.py", '("「小局一场没赢」", "Not a single game won.", "p. 4")', '("「小局一场没赢」", "Nenhum jogo ganho.", "Página 4")'),
    ("content7.py", '("「故事够不够好」", "But is the story good enough?", "p. 5")', '("「故事够不够好」", "Mas a história é boa o bastante?", "Página 5")'),
    ("content7.py", '("「别以后,就现在」", "Not later — now.", "p. 5")', '("「别以后,就现在」", "Não depois — agora.", "Página 5")'),
    ("content7.py", "下期预告 · Next week (VOL.3)", "下期预告 · Na próxima semana (VOL.3)"),
    # ---- P8 ----
    ("content8.py", "测验与答案 · Test & keys", "测验与答案 · Teste e gabarito"),
    ("content8.py", "第 8 版 · 本周大测验 + 全部答案 · This week's test and every answer key", "第 8 版 · 本周大测验 + 全部答案 · O teste da semana e todas as respostas"),
    ("content8.py", "A · 判断对错 · True or false", "A · 判断对错 · Verdadeiro ou falso"),
    ("content8.py", "立冬 is the 19th solar term, not the 18th.", "立冬 é o 19º termo solar, não o 18º."),
    ("content8.py", "Spot goods ship without a deposit wait.", "Mercadorias imediatas: sem espera de sinal."),
    ("content8.py", "AL lost all three of its Swiss-stage series.", "A AL perdeu as três séries da fase suíça."),
    ("content8.py", "The AI film has no live actors.", "O filme de IA não tem atores reais."),
    ("content8.py", "The new film opens on Nov 7.", "O novo filme estreia em 7 de novembro."),
    ("content8.py", "Journalists' Day is on Nov 8, not Nov 7.", "Dia dos Jornalistas: 8 de novembro, não 7."),
    ("content8.py", "B · 本周大测验 · The big quiz", "B · 本周大测验 · O grande quiz"),
    ("content8.py", "The solar-term moment is 17:52.", "O momento do termo solar é às 17h52."),
    ("content8.py", "First micro-season: water begins to freeze.", "Primeira microestação: a água começa a congelar."),
    ("content8.py", "IG beat HLE on Oct 26.", "A IG venceu a HLE em 26 de outubro."),
    ("content8.py", "TES beat G2 on Oct 26.", "A TES venceu a G2 em 26 de outubro."),
    ("content8.py", "By noon on Oct 26, Maoyan showed about 1.192 million yuan.", "Ao meio-dia de 26 de outubro, o Maoyan mostrava cerca de 1,192 milhão de yuan."),
    ("content8.py", "Huang Yan is a crematory worker.", "Huang Yan é funcionária de crematório."),
    ("content8.py", "The WeChat shop event runs 35 days.", "O evento da loja do WeChat dura 35 dias."),
    ("content8.py", "Basket A pays 270 yuan after the cut.", "A cesta A paga 270 yuan depois do corte."),
    ("content8.py", "The final starts at 03:00 Beijing time on Nov 15.", "A final: 15 de novembro, 03:00, hora de Pequim."),
    ("content8.py", "C · 完成句子 · Complete", "C · 完成句子 · Complete as frases"),
    ("content8.py", "Start of Winter is on Nov 7.", "O Início do Inverno é em 7 de novembro."),
    ("content8.py", "Àilún — Allen, Texas, hosts the Swiss stage.", "Àilún — Allen, no Texas, sedia a fase suíça."),
    ("content8.py", "shùzì — the AI film's characters are digital images.", "shùzì — personagens digitais no filme de IA."),
    ("content8.py", "piàofáng — box-office takings.", "piàofáng — a bilheteria."),
    ("content8.py", "jìzhě — a journalist interviews and writes news.", "jìzhě — um jornalista entrevista e escreve notícias."),
    ("content8.py", "lìjiǎn — taken off at checkout.", "lìjiǎn — desconto no checkout."),
    ("content8.py", "D · 读一读,答一答 · Read & answer", "D · 读一读,答一答 · Leia e responda"),
    ("content8.py", "Xiao Hong lives in Beijing.", "Xiao Hong mora em Pequim."),
    ("content8.py", "On 立冬 she made dumplings with her mother.", "No 立冬 ela fez bolinhos com a mãe."),
    ("content8.py", "She bought a scarf online.", "Ela comprou um cachecol on-line."),
    ("content8.py", "She phoned her grandmother on Sunday.", "Ela telefonou para a avó no domingo."),
    ("content8.py", "Order: dumplings, then shopping, then the phone call.", "Ordem: bolinhos, depois compras, depois o telefonema."),
    ("content8.py", "E · 情景说话 · In conversation", "E · 情景说话 · Em conversa"),
    ("content8.py", "Spot goods ship right away, no pre-sale wait.", "Mercadorias imediatas: despacham na hora."),
    ("content8.py", "Northern families eat dumplings at 立冬.", "As famílias do norte comem bolinhos no 立冬."),
    ("content8.py", "Page 6's rule: data first, advertisement last.", "Regra da página 6: dados primeiro."),
    ("content8.py", "F · 写一写 · Writing", "F · 写一写 · Escrita"),
    ("content8.py", "Writing — there is no single right answer. A ", "Escrita — não há uma única resposta certa. Segue um texto-modelo de "),
    ("content8.py", "-character model follows.", " caracteres."),
    ("content8.py", 'instr="Writing"', 'instr="Escreva"'),
    ("content8.py", "Open task - the model answer is printed in section F above (", "Pergunta aberta — o modelo está na seção F acima ("),
    ("content8.py", " characters)", " caracteres)"),
    ("content8.py", "Model answer: ", "Texto-modelo: "),
    ("content8.py", "答案 · Answer keys — by page, with a note on every answer", "答案 · Gabarito — por página, com uma nota em cada resposta"),
    ("content8.py", "All notes in English · ✓ = the writing task", "Todas as notas em português · ✓ = a tarefa de escrita"),
    ("content8.py", 'f"— Page {pg} —"', 'f"— Página {pg} —"'),
    # P8 key format is DASH style in this core family (content8.py code path:
    # f"{n}. {key} — {note}" / writing f"{n}. ✓ {note}") — KEPT byte-identical.
    ("content8.py", 'e_["type"] == "写作"', 'e_["type"] == "Escrita"'),
]

# Exercise-type names: registry-only (never printed on pages except via the
# P8 writing-type check above). Localised per the shipped VOL.1 PT column:
# Complete a frase 68 / Escolha múltipla 50 / Associação 20 /
# Escolha no contexto 11 / Escrita 1. Anchored 2nd-arg form so bilingual
# heads (which contain the Chinese words with " · " separators) are untouched.
TYPE_PAIRS = [
    (', "完形单选", ', ', "Escolha no contexto", '),
    (', "完成句子", ', ', "Complete a frase", '),
    (', "词汇配对",', ', "Associação",'),
    (', "单选", ', ', "Escolha múltipla", '),
    (', "写作", ', ', "Escrita", '),
]

def apply_pairs():
    texts = {}
    for fn in FILES:
        with open(os.path.join(BUILD, fn), encoding="utf-8") as fh:
            texts[fn] = fh.read()
    total = 0
    for old, new in PAIRS + PAIRS2:
        hits = 0
        for fn in FILES:
            c = texts[fn].count(old)
            if c:
                texts[fn] = texts[fn].replace(old, new)
                hits += c
        print(f"global {hits:3d} :: {old[:70]!r}")
        assert hits >= 1, f"ZERO HITS (global): {old!r}"
        total += hits
    for fn, old, new in FILE_PAIRS:
        c = texts[fn].count(old)
        print(f"{fn} {c:3d} :: {old[:70]!r}")
        assert c >= 1, f"ZERO HITS ({fn}): {old!r}"
        texts[fn] = texts[fn].replace(old, new)
        total += c
    for old, new in TYPE_PAIRS:
        hits = 0
        for fn in FILES:
            c = texts[fn].count(old)
            if c:
                texts[fn] = texts[fn].replace(old, new)
                hits += c
        print(f"type   {hits:3d} :: {old!r} -> {new!r}")
        assert hits >= 1, f"ZERO HITS (type): {old!r}"
        total += hits
    for fn in FILES:
        with open(os.path.join(BUILD, fn), "w", encoding="utf-8") as fh:
            fh.write(texts[fn])
    print("TOTAL replacements:", total)

if __name__ == "__main__":
    apply_pairs()
