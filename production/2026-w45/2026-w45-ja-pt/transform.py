# -*- coding: utf-8 -*-
"""JA core (VOL.2, Chinese explanations) -> JA x PT edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets, never byte slicing),
and writes the edition build into this directory. Fix rounds edit THIS
file, then re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> Portuguese, per the W43 JA x PT shipped precedent
(files/weekly-report-ja-pt). Masthead geometry follows the W43 JA x PT
shipped SVG exactly (wordmark 248, edition 316, badge 356, tagline 390,
rules 406/413, dark band 424). The README #20 JA-target note (wordmark
stays at 262) is NOT followed: the same-pairing W43 JA x PT geometry
(wordmark 248) governs, as do all W45 JA siblings.

P7 rule: Japanese definition sentences are byte-frozen; only glosses
are localized. P8 E zone is re-aimed JA<->ZH -> JA<->PT: #137/#138 keys
become Portuguese bodies (Japanese prompts frozen), #139/#140 bodies
become Portuguese prompts (Japanese keys byte-identical).
"""
import hashlib
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w45-ja-build")
EDITION = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w45-ja-pt")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

# (old, new) applied in order. Longer strings first where one contains another.
GLOBAL = [
    # --- output repoint ---
    ("weekly-report-w45-ja-core", "weekly-report-w45-ja-pt"),
    # --- registry type names / instructions (W43 JA x PT wording pattern) ---
    ('instr="造句"', 'instr="Construa uma frase"'),
    ('instr="翻译"', 'instr="Traduza"'),
    ('instr="写作"', 'instr="Redação"'),
    ('instr="判断"', 'instr="Verdadeiro ou falso?"'),
    ('instr="填空"', 'instr="Complete"'),
    ('instr="把词和释义配对"', 'instr="Ligue palavras e sentidos"'),
    ('instr="把活动和地点·时间配对"', 'instr="Ligue os eventos aos lugares e às datas"'),
    ('"完形单选"', '"cloze"'),
    ('"单选"', '"múltipla escolha"'),
    ('"完成句子"', '"complete a frase"'),
    ('"词汇配对"', '"associação de palavras"'),
    ('"造句"', '"construção de frases"'),
    ('"判断对错"', '"verdadeiro/falso"'),
    ('"翻译"', '"tradução"'),
    ('"写作"', '"redação"'),
    # --- shared furniture ---
    ('"あなたは？ · 说说你自己"', '"あなたは？ · A sua vez"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Respostas na página 8 · Níveis mistos: procure o seu número"'),
]

# Answer-note translations. One Portuguese rendering per distinct core note;
# duplicates share the rendering (correct: same note -> same meaning).
NOTES = [
    ("文化日在11月3日（周二）", "O Dia da Cultura é 3 de novembro (terça-feira)"),
    ("读书周到11月9日（周一）", "A Semana da Leitura vai até 9 de novembro (segunda-feira)"),
    ("見頃＝最佳观赏期", "見頃 = a melhor época para ver"),
    ("立冬＝冬天的开始", "立冬 = o início do inverno"),
    ("神户灯光秀从7日（周六）开始", "As luzes de Kobe começam no dia 7 (sábado)"),
    ("文化日全国都有文化活动", "No Dia da Cultura há eventos culturais em todo o país"),
    ("立冬在11月7日（周六）", "立冬 é 7 de novembro (sábado)"),
    ("灯光秀在神户开始", "As luzes começam em Kobe"),
    ("「ゆる」＝无理をしない", "「ゆる」 = sem forçar"),
    ("鍋の食卓は去年の1.5倍", "Os jantares de nabe são 1,5 vez os do ano passado"),
    ("発表は10月21日", "O anúncio foi em 21 de outubro"),
    ("11月から1月まで気温は平年より高い",
     "Temperaturas acima da média de novembro a janeiro"),
    ("服と食事の話題はnoteのまとめによるもの",
     "Os temas de roupa e comida vêm da coletânea de notas"),
    ("ゆる＝轻松、不勉强", "ゆる = relaxado, sem forçar"),
    ("蒸し器＝蒸笼", "蒸し器 = uma cesta de vapor"),
    ("整える＝调理、调养", "整える = pôr em ordem"),
    ("鍋＝一锅菜", "鍋 = um cozido de panela"),
    ("鍋の材料が1か月早く並んだ", "Ingredientes de nabe um mês mais cedo nas lojas"),
    ("気象庁の予報は10月20日", "A previsão da Agência Meteorológica foi em 20 de outubro"),
    ("サクサクdeコパンが1,300万食を超えた",
     "サクサクdeコパン passou de 13 milhões de porções"),
    ("ゆる＝轻松 b", "ゆる = relaxado b"),
    ("蒸し器＝蒸笼 a", "蒸し器 = cesta de vapor a"),
    ("麻辣湯＝辛いスープ d", "麻辣湯 = sopa apimentada d"),
    ("予報＝天気の予想 c", "予報 = previsão do tempo c"),
    ("杉并的活动是家庭管弦乐队", "O evento de Suginami é uma orquestra familiar"),
    ("传统工艺展在石川县立美术馆",
     "A exposição é no Museu de Arte da Prefeitura de Ishikawa"),
    ("传统工艺展到11月8日", "A exposição vai até 8 de novembro"),
    ("灯光秀在金泽城和兼六园", "As luzes ficam no Castelo de Kanazawa e no Kenrokuen"),
    ("市場＝集市", "市場 = mercado"),
    ("工芸＝工艺", "工芸 = artesanato"),
    ("陶器＝陶瓷", "陶器 = cerâmica"),
    ("工艺展到11月8日（周日）", "A exposição vai até 8 de novembro (domingo)"),
    ("金箔＝金箔", "金箔 = folha de ouro"),
    # P8 #37 bare note (P3 exercise, key 8) — distinct from #32's
    # (Sunday) note above and from the 传统… note. Fact check: the P3
    # stem is 展覧会は11月 ___ 日（日）までです。 and 2026-11-08 is a
    # Sunday, so the Portuguese note matches the stem fact.
    ("工艺展到11月8日", "A exposição vai até 8 de novembro"),
    ("主语＋时间", "sujeito + tempo"),
    ("地点＋で＋あります", "lugar + で + あります"),
    ("见たい＝想看", "見たい = querer ver"),
    ("和家人一起", "com a família"),
    ("文化の日＝11月3日 b", "文化の日 = 3 de novembro b"),
    ("工芸展＝美術館 c", "工芸展 = museu c"),
    ("オーケストラ＝杉並 d", "オーケストラ = Suginami d"),
    ("ライトアップ＝金沢城 a", "ライトアップ = Castelo de Kanazawa a"),
    ("第1战软银3-1胜DeNA", "Jogo 1: SoftBank venceu DeNA por 3–1"),
    ("第2战逆转的是筒香的3分本垒打", "O home run de 3 pontos de Tsutsugo virou o jogo 2"),
    ("2连胜开局的是软银", "SoftBank começou com duas vitórias seguidas"),
    ("2连胜开局的夺冠率是73%", "Quem começa com 2–0 vence o título em 73% dos casos"),
    ("2024年夺冠的是DeNA", "DeNA venceu o título em 2024"),
    ("第1战软银得3分", "SoftBank marcou 3 no jogo 1"),
    ("第2战软银得4分", "SoftBank marcou 4 no jogo 2"),
    ("第1战打到延长11局", "O jogo 1 foi a 11 entradas"),
    ("第2战打到延长10局", "O jogo 2 foi a 10 entradas"),
    ("夺冠率73%", "Taxa de título: 73%"),
    ("延長＝比赛延长", "延長 = o jogo se prolongar"),
    ("第1战观众33,388人", "Público do jogo 1: 33.388"),
    ("第2战观众33,432人", "Público do jogo 2: 33.432"),
    ("相川监督说「4场胜负之战」", "O técnico Aikawa falou de uma luta de quatro vitórias"),
    ("第1戦は土よう日です", "O jogo 1 foi no sábado"),
    ("ソフトバンクが2連勝しました", "SoftBank venceu duas seguidas"),
    ("第2戦も延長戦でした", "O jogo 2 também foi a entradas extras"),
    ("2024年はDeNAが優勝しました", "DeNA venceu em 2024"),
    ("万圣节在10月31日（周六）", "O Halloween foi em 31 de outubro (sábado)"),
    ("涩谷禁酒时间是18时到5时", "A proibição de beber em Shibuya vai das 18h às 5h"),
    ("乱扔垃圾罚款2,000日元", "Jogar lixo na rua custa 2.000 ienes de multa"),
    ("化妆活动在池袋", "O festival de cosplay fica em Ikebukuro"),
    ("横滨中区民祭在11月8日（周日）", "Festival de Naka, em Yokohama: 8 de novembro (domingo)"),
    ("万圣节在10月31日", "O Halloween foi em 31 de outubro"),
    ("禁酒从18时开始", "A proibição começa às 18h"),
    ("禁酒到早上5时", "A proibição vai até as 5h"),
    ("横滨祭典在11月8日", "O festival de Yokohama é em 8 de novembro"),
    ("夜里路上不能喝酒", "Não se pode beber na rua à noite"),
    ("ゴミの罰金は今年6月からです", "A multa por lixo vale desde junho deste ano"),
    ("コスプレフェスは池袋です", "O festival de cosplay é em Ikebukuro"),
    ("ハロウィンは10月31日（土）", "O Halloween foi em 31 de outubro (sábado)"),
    ("飲むことができません＝不能喝", "飲むことができません = não se pode beber"),
    ("守って、〜しましょう", "守って + 〜しましょう = siga as regras e vamos…"),
    ("フェンスの中＝围栏里面", "フェンスの中 = dentro da cerca"),
    ("活动从10月30日到11月1日", "O festival foi de 30 de outubro a 1º de novembro"),
    ("雨が多いのは太平洋側", "O lado do Pacífico tem mais chuva"),
    ("九州の旅の検索は去年のほぼ2倍",
     "Buscas de viagens a Kyushu quase dobraram"),
    ("1回の旅の予算は下がった", "O orçamento por viagem caiu"),
    ("鳴子峡の見頃は10月31日から11月8日の週末",
     "Pico de Naruko Gorge: 31 de outubro a 8 de novembro"),
    ("图中最受欢迎的是近处的满足感", "O topo do gráfico é a satisfação por perto"),
    ("近场满足感38%", "Satisfação por perto: 38%"),
    ("温泉27%", "Fontes termais: 27%"),
    ("红叶21%与美食14%之差为7", "Folhas 21% menos comida 14% é 7"),
    ("38+27=65", "38 + 27 = 65"),
    ("四项合计100%", "Os quatro somam 100%"),
    ("立冬在11月7日", "立冬 é 7 de novembro"),
    ("神户灯光秀到12月28日", "As luzes de Kobe vão até 28 de dezembro"),
    ("九州旅行搜索约为去年的2倍",
     "Buscas por Kyushu: quase o dobro do ano passado"),
    ("气象厅预报在10月20日", "A previsão da Agência Meteorológica foi em 20 de outubro"),
    ("11月は平年より暖かい予報です", "Novembro deve ser mais quente que a média"),
    ("九州の旅の検索は増えました", "As buscas por viagens a Kyushu aumentaram"),
    ("グラフは練習用データです", "O gráfico é dado de prática"),
    ("读书周从10月27日（周二）开始", "Semana da Leitura começou em 27 de outubro (terça)"),
    ("读书周到11月9日", "A Semana da Leitura vai até 9 de novembro"),
    ("口号是「静かだけど、冒険中。」", "O lema é 「静かだけど、冒険中。」"),
    ("图书馆活动有图书介绍", "O evento da biblioteca é a apresentação de livros"),
    ("見頃＝红叶最美的时候", "見頃 = quando as folhas estão mais bonitas"),
    ("紅葉狩り＝去看红叶", "紅葉狩り = sair para ver as folhas"),
    ("ライトアップ＝夜里用灯光照亮", "ライトアップ = iluminar à noite"),
    ("落葉＝落叶", "落葉 = folhas caídas"),
    ("1.5倍＝比去年多50%", "1.5倍 = 50% a mais que no ano passado"),
    ("73%≈4人中的3人", "73% ≈ 3 em cada 4"),
    ("サクサクdeコパンが1,300万食", "サクサクdeコパン chegou a 13 milhões de porções"),
    ("日本大赛第1战在10月24日（周六）", "O jogo 1 das Japan Series foi em 24 de outubro (sábado)"),
    ("第2战软银4-3获胜", "Jogo 2: SoftBank venceu por 4–3"),
    ("神户灯光秀从7日开始", "As luzes de Kobe começam no dia 7"),
    ("2连胜开局的夺冠率73%", "Taxa de título para quem começa com 2–0: 73%"),
    ("气象厅预报气温高于往年", "Previsão da Agência Meteorológica: acima da média"),
    ("美香周二和家人去金泽", "Na terça-feira Mika vai a Kanazawa com a família"),
    ("在金泽看传统工艺展和灯光秀",
     "Em Kanazawa ela vê a exposição de artesanato e as luzes"),
    ("周六和朋友去神户", "No sábado ela vai a Kobe com amigos"),
    ("读书周想借2本书", "Quer 2 livros emprestados para a Semana da Leitura"),
    ("主语＋时间＋地点＋动词", "sujeito, tempo, lugar, verbo"),
    ("场所用「で」", "use 「で」 para o lugar"),
    ("2连胜开局", "2 vitórias seguidas"),
    ("見頃＝最佳观赏期 b", "見頃 = a melhor época para ver b"),
    ("鍋＝一锅菜 d", "鍋 = um cozido de panela d"),
    ("落葉＝落叶 a", "落葉 = folhas caídas a"),
    ("予算＝预算 c", "予算 = orçamento c"),
    ("見せてください＝请出示", "見せてください = por favor, mostre"),
    ("借りられます＝能借（可能形）", "借りられます = pode pegar emprestado (forma potencial)"),
    ("读书周到11月9日（第7版）", "A Semana da Leitura vai até 9 de novembro (página 7)"),
    ("「紅葉の本」受欢迎", "「紅葉の本」 é popular"),
    ("どういたしまして＝不客气", "どういたしまして = por nada"),
    ("对照第3版", "Veja a página 3"),
    ("对照第5版", "Veja a página 5"),
    ("对照第7版", "Veja a página 7"),
    ("对照第6版（神户的灯光秀）", "Veja a página 6"),
]

# Per-file furniture / gloss / structural replacements.
PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Nota — " + s,'),
        ('"Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · SEMANÁRIO JAPONÊS VOL.2 · TEXTOS EM JAPONÊS · EXPLICAÇÕES EM PORTUGUÊS"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"'),
    ],
    "content12.py": [
        # P1 masthead -> W43 JA x PT shipped geometry
        ('p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")',
         'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")'),
        ('p.text(975, 330, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEXTOS EM JAPONÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 19, "sans", True, OLIVE, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Toda semana · 日本人が読んでいる日本語を読む"'),
        ('"周二是文化日"', '"Terça-feira é o Dia da Cultura"'),
        ('"节日过后，红叶周末到来 · 详见第 3 版"',
         '"Depois do feriado, chega o fim de semana das folhas · Veja a página 3"'),
        ('"トップニュース · 头条"', '"トップニュース · Em destaque"'),
        ('"祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。"',
         '"祝日 feriado · 見頃 a melhor época para ver · 暦 calendário · お届けします entregamos a você."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · Em números"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Pratique agora"'),
        ('"这四个话题，都是本期报纸的主题。"',
         '"Estes quatro temas dão forma a este número."'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Datas nos artigos; não são estatísticas exatas"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · Neste número"'),
        ('"今週のことば · 本周单词"', '"今週のことば · A palavra da semana"'),
        ('"ゆる＝ 轻松、不勉强。"', '"ゆる = relaxado, sem forçar."'),
        ('"短いニュース · 快讯"', '"短いニュース · Notícias breves"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quiz-relâmpago"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Leia a primeira página e escolha · Respostas na página 8"'),
        # P2
        ('"レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月"',
         '"レベル A2 · ゆる整え食と暖かい11月 · Comida leve e um novembro ameno"'),
        ('"蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。"',
         '"蒸す cozinhar no vapor · 並ぶ chegar às prateleiras · 食卓 a mesa de jantar · 超える passar de."'),
        ('"予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。"',
         '"予報 previsão · 平年 um ano médio · 季節風 vento sazonal · 話題 tema · 値上がり alta de preços."'),
        ('"你呢？寒冷的日子想吃什么锅？写两句日语寄来。"',
         '"E você? Num dia frio, que nabe gostaria de comer? Escreva duas frases em japonês e envie."'),
        ('"季節のことば · 季节词语"', '"季節のことば · Palavras da estação"'),
        ('"ゆる整え食の4つの言葉 · 关于轻松食养的四个词"',
         '"ゆる整え食の4つの言葉 · Quatro palavras para comer com leveza"'),
        ('"一锅菜"', '"um cozido de panela"'),
        ('"蒸笼"', '"uma cesta de vapor"'),
        ('"轻松、不勉强"', '"relaxado, sem forçar"'),
        ('"调理、调养"', '"pôr o corpo e a mente em ordem"'),
        ('"練習 · 第 2 版练习"', '"練習 · Exercícios da página 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 文化の日と金沢 · 文化日与金泽"',
         '"レベル A2→B1 · 文化の日と金沢 · Dia da Cultura e Kanazawa"'),
        ('"市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。"',
         '"市場 mercado · 工芸 artesanato · 光 luz · 楽しむ aproveitar."'),
        ('"陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。"',
         '"陶器 cerâmica · 漆器 laca · 染物 tecidos tingidos · 金箔 folha de ouro."'),
        ('"你呢？文化日想去参加什么文化活动？写两句日语寄来。"',
         '"E você? A que evento cultural gostaria de ir no Dia da Cultura? Escreva duas frases em japonês e envie."'),
        ('"練習 · 第 3 版练习"', '"練習 · Exercícios da página 3"'),
        ('"レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场"',
         '"レベル B1 · 日本シリーズ横浜の2試合 · As Japan Series: dois jogos em Yokohama"'),
        ('"延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。"',
         '"延長 entradas extras · 逆転 virada · 同点 empate · 優勝率 taxa de título."'),
        ('"総括 总结 · 締め切り 截稿 · 確認する 核实。"',
         '"総括 balanço · 締め切り fechamento · 確認する confirmar."'),
        ('"日本シリーズの日程 · 大赛日程"', '"日本シリーズの日程 · Calendário"'),
        ('"横浜の2試合の記録 · 横滨两场比赛的记录"',
         '"横浜の2試合の記録 · Os dois jogos de Yokohama, registrados"'),
        ('"練習 · 第 4 版练习"', '"練習 · Exercícios da página 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Jovens"'),
        ('"レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典"',
         '"レベル B1 · ハロウィンと秋まつり · Halloween e festivais de outono"'),
        ('"罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。"',
         '"罰金 multa · 像 estátua · 仮装 fantasiar-se · 守る respeitar."'),
        ('"祭り 节日 · 週末 周末 · 話題 话题。"',
         '"祭り festival · 週末 fim de semana · 話題 tema."'),
        ('"你呢？秋日祭典上想做什么？写两句日语寄来。"',
         '"E você? O que gostaria de fazer num festival de outono? Escreva duas frases em japonês e envie."'),
        ('"練習 · 第 5 版练习"', '"練習 · Exercícios da página 5"'),
        ('"レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行"',
         '"レベル B2 · 暖かい11月と秋の旅 · Um novembro ameno e viagens de outono"'),
        ('"予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。"',
         '"予算 orçamento · 満足 satisfação · 観測 observação · 追いかける perseguir."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Vamos ler o gráfico"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Dados de prática"'),
        ('"練習 · 第 6 版练习"', '"練習 · Exercícios da página 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Língua"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Três níveis, três temas"'),
        ('"読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。"',
         '"読書週間 Semana da Leitura · 紹介 apresentação · 読み聞かせ leitura em voz alta."'),
        ('"見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶"',
         '"見頃 a melhor época para ver · 紅葉狩り passeios para ver as folhas · 落葉 folhas caídas"'),
        ('"〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。"',
         '"〜倍 vezes · 〜% por cento · 〜万食 dezenas de milhares de porções."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Clínica dos erros"'),
        ('"有「昨日」时要用过去式。"', '"Com 「昨日」, use o passado."'),
        ('"动词名词化时要加「こと」。"',
         '"Acrescente 「こと」 para transformar um verbo em substantivo."'),
        ('"地点用「か所」来数。"', '"Conte lugares com 「か所」."'),
        ('"动作发生的场所用「で」。"',
         '"Use 「で」 para o lugar onde a ação acontece."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · A frase modelo"'),
        ('"句式拆解：轻松地调理身心。"',
         '"Análise: pôr o corpo e a mente em ordem com leveza."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Cantinho dos leitores"'),
        # Readers' corner: coordinator ruling — the Japanese disclosure line
        # (ld) must NOT serve as the operative disclosure for Portuguese
        # readers, and the Chinese disclosure (lcn) is the core's
        # reader-native layer. Both are replaced by ONE Portuguese
        # disclosure stating the 3 facts + an explicit invitation.
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.3に載せます。"',
         'ld_pt = "Exemplo da redação, não é carta de verdade. Até o '
         'fechamento, não chegaram cartas nem as melhores redações '
         'da página 8; ambas sairão no VOL.3. Envie a sua carta em japonês!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_pt, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_pt, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Frases da semana (textuais, deste número)"'),
        ('"文化日是11月3日星期二。"', '"O Dia da Cultura é terça-feira, 3 de novembro."'),
        ('"这是一个慢慢地、轻松调理的日本11月。"',
         '"É um novembro japonês lento, posto em ordem com leveza."'),
        ('"所谓ゆる，就是不勉强、慢慢来的意思。"',
         '"ゆる quer dizer não forçar, ir devagar."'),
        ('"火锅食材提前一个月上架了。"',
         '"Os ingredientes de nabe chegaram às lojas um mês mais cedo."'),
        ('"可以同时欣赏传统工艺、红叶与灯光。"',
         '"Dá para apreciar juntos artesanato tradicional, folhas de outono e luzes."'),
        ('"软银以两连胜开局。"', '"SoftBank começou com duas vitórias seguidas."'),
        ('"遵守规则，过一个快乐的万圣节吧。"',
         '"Respeite as regras e tenha um Halloween feliz."'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。"',
         '"Quem vai ver as folhas pode perseguir a melhor época do norte ao sul."'),
        ('"第1面"', '"p.1"'),
        ('"第2面"', '"p.2"'),
        ('"第3面"', '"p.3"'),
        ('"第4面"', '"p.4"'),
        ('"第5面"', '"p.5"'),
        ('"第6面"', '"p.6"'),
        ('"来週 · 下期预告 (VOL.3)"', '"来週 · Na próxima semana (VOL.3)"'),
    ],
    "content8.py": [
        ('"テストと答え · 练习与答案"', '"テストと答え · Teste e respostas"'),
        ('"第 8 面 · 週の大きなテスト + 全ての答え"',
         '"Página 8 · 週の大きなテスト + 全ての答え"'),
        # E zone re-aim JA<->ZH -> JA<->PT (W43 JA x PT pattern):
        # #137/#138 keys become Portuguese bodies (Japanese prompts frozen);
        # #139/#140 bodies become Portuguese prompts (Japanese keys frozen).
        ('"文化日是11月3日。"', '"O Dia da Cultura é 3 de novembro."'),
        ('"乱扔垃圾，要罚2,000日元。"', '"Se jogar lixo na rua, a multa é de 2.000 ienes."'),
        ('"读书周从10月27日开始。→ ___"',
         '"A Semana da Leitura começa em 27 de outubro. → ___"'),
        ('"我想去神户看红叶灯光秀。→ ___"',
         '"Quero ir a Kobe ver as luzes das folhas de outono. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Redação (sem resposta única); o texto-modelo ({NCHARS} caracteres) está abaixo."'),
        ('"（开放题，范文如下）"', '"(tarefa aberta — texto-modelo abaixo)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Texto-modelo na seção H desta página ({NCHARS} caracteres)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Respostas — agrupadas por página: basta procurar o seu número"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Uma nota breve em português para cada resposta · ✓ = a pergunta com o texto-modelo"'),
        ('f"— 第{pg}面 —"', 'f"— Página {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-PT.pdf"'),
        ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-PT-web.pdf"'),
    ],
}


def apply_pairs(text, pairs, fname):
    seen = set()
    for old, new in pairs:
        if old in seen:
            continue
        seen.add(old)
        n = text.count(old)
        assert n >= 1, f"{fname}: replacement source missing: {old!r}"
        text = text.replace(old, new)
    return text


def apply_soft(text, pairs):
    seen = set()
    for old, new in pairs:
        if old in seen:
            continue
        seen.add(old)
        text = text.replace(old, new)
    return text


def apply_notes_scoped(text, note_map):
    """Replace note strings ONLY where they are note arguments.

    Bare substring replacement is FORBIDDEN for notes: several notes are
    prefixes/substrings of frozen Japanese stems and article sentences,
    and a global replace corrupted frozen text in the JA x EN round 1.
    Two scoped sites: (a) the 4th quoted argument of any .ex(...) call;
    (b) a bracket-list line whose every string is a note (match_set notes
    lists; lefts/rights/keys lines never satisfy this).
    """
    def ex_sub(m):
        note = m.group(2)
        if note in note_map:
            return m.group(1) + note_map[note] + m.group(3)
        return m.group(0)
    text = re.sub(r'(\.ex\("[^"]*",\s*"[^"]*",\s*"[^"]*",\s*")([^"]*)(")',
                  ex_sub, text)

    def list_sub(m):
        inner = m.group(2)
        strs = re.findall(r'"([^"]*)"', inner)
        if strs and all(s in note_map for s in strs):
            out = inner
            for s in strs:
                out = out.replace('"%s"' % s, '"%s"' % note_map[s], 1)
            return m.group(1) + out + m.group(3)
        return m.group(0)
    text = re.sub(r'(?m)^(\s*\[)(.*)(\],\s*)$', list_sub, text)
    return text


def quoted_strings(text):
    return set(re.findall(r'"([^"]*)"', text))


def main():
    os.makedirs(EDITION, exist_ok=True)
    os.makedirs(os.path.join(EDITION, "svg"), exist_ok=True)
    # svglib: canonical JA build, copied verbatim, md5-verified, never edited.
    src_svg = os.path.join(CORE, "svglib.py")
    data = open(src_svg, "rb").read()
    assert hashlib.md5(data).hexdigest() == CANON_SVGLIB_MD5, "svglib md5 mismatch"
    shutil.copyfile(src_svg, os.path.join(HERE, "svglib.py"))
    # run.py: verbatim copy (one-process driver).
    shutil.copyfile(os.path.join(CORE, "run.py"), os.path.join(HERE, "run.py"))
    # assets: verbatim copies (images + credits).
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(CORE, "assets")):
        shutil.copyfile(os.path.join(CORE, "assets", f),
                        os.path.join(HERE, "assets", f))
    # NOTE replacements: dict (deduped). Order: NOTES scoped FIRST (note
    # arguments only), then structural PER_FILE, then GLOBAL types/instr.
    note_map = dict(NOTES)
    fnames = ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "render.py"]
    # Pre-audit: every GLOBAL source must occur in >=1 core file, and
    # every NOTE key must occur as an EXACT quoted string (a real note
    # argument, not a substring of a frozen sentence).
    core_texts = {f: open(os.path.join(CORE, f), encoding="utf-8").read()
                  for f in fnames}
    for old, _ in GLOBAL:
        assert any(old in t for t in core_texts.values()), \
            f"transform table source never occurs in core: {old!r}"
    core_quoted = set()
    for t in core_texts.values():
        core_quoted |= quoted_strings(t)
    for old in note_map:
        assert old in core_quoted, \
            f"note key never occurs as an exact quoted string: {old!r}"
    for fname in fnames:
        text = core_texts[fname]
        text = apply_notes_scoped(text, note_map)
        text = apply_pairs(text, PER_FILE.get(fname, []), fname)
        text = apply_soft(text, GLOBAL)
        open(os.path.join(HERE, fname), "w", encoding="utf-8").write(text)
        print("transformed", fname)
    # Post-audit: no GLOBAL source may survive as a substring, and no
    # NOTE key may survive as an exact quoted string (substrings inside
    # frozen stems, e.g. "...ました。" stems, legitimately remain).
    for fname in fnames:
        out = open(os.path.join(HERE, fname), encoding="utf-8").read()
        for old, _ in GLOBAL:
            assert old not in out, f"{fname}: un-replaced source remains: {old!r}"
        out_quoted = quoted_strings(out)
        for old in note_map:
            assert old not in out_quoted, \
                f"{fname}: un-replaced note remains: {old!r}"
    print("OUT dir:", EDITION)


if __name__ == "__main__":
    main()
