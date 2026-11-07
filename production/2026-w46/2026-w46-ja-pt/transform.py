# -*- coding: utf-8 -*-
"""JA core (VOL.3, Chinese explanations) -> JA x PT edition transform.

Re-runnable: reads the PRISTINE W46 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets), and writes the
edition build into this directory. Fix rounds edit THIS file, then
re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> Portuguese, per the W45 JA x PT shipped precedent.
Masthead geometry per the W46 task + tools/README lesson 20: wordmark
stays at the CORE position y=262, subtitle 316, badge inserted at
(975,356) 19pt BRICK, strapline 390, rules 406/413, dark band 424.
"""
import hashlib
import os
import re
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
CORE = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "hidden_files/weekly-report-w46-ja-build")
EDITION = os.path.expanduser(
    "~/workspace/goals/lucernaread-social-media-operations/"
    "files/weekly-report-w46-ja-pt")
CANON_SVGLIB_MD5 = "74177544422fe677639d769cd80499fb"

GLOBAL = [
    ("weekly-report-w46-ja-core", "weekly-report-w46-ja-pt"),
    ('instr="造句"', 'instr="Construa uma frase"'),
    ('instr="翻译"', 'instr="Traduza"'),
    ('instr="写作"', 'instr="Redação"'),
    ('instr="判断"', 'instr="Verdadeiro ou falso?"'),
    ('instr="填空"', 'instr="Complete"'),
    ('instr="把词和释义配对"', 'instr="Ligue palavra e sentido"'),
    ('"完形单选"', '"cloze"'),
    ('"单选"', '"múltipla escolha"'),
    ('"完成句子"', '"completar"'),
    ('"词汇配对"', '"associação"'),
    ('"造句"', '"construção de frases"'),
    ('"判断对错"', '"verdadeiro/falso"'),
    ('"翻译"', '"tradução"'),
    ('"写作"', '"redação"'),
    ('"あなたは？ · 说说你自己"', '"あなたは？ · A tua vez"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Respostas na página 8 · Níveis misturados: encontra o teu número"'),
]

NOTES = [
    ("1111中有4个1", "1111 tem quatro uns"),
    ("1111看起来像4根细棒", "1111 parece quatro palitos finos"),
    ("11月中旬以后进入见赏期的地点多比往年稍晚", "Os lugares que culminam após meados de novembro costumam atrasar-se"),
    ("2026年没有三の酉", "Não há San-no-tori em 2026"),
    ("3%≈100人中的3人", "3 % é cerca de 3 em 100"),
    ("34+26=60", "34 + 26 = 60"),
    ("4连胜夺冠", "Quatro vitórias seguidas trouxeram o título"),
    ("4连胜＝4场比赛全胜", "ganhar os quatro jogos"),
    ("71%的家庭接受祈祷", "71 % das famílias recebem uma oração"),
    ("74%的家庭在照相馆拍照", "74 % das famílias tiram fotos num estúdio"),
    ("Weathernews的预报在10月29日（周四）", "A previsão da Weathernews era de 29 de outubro (quinta-feira)"),
    ("「千歳飴」受欢迎", "千歳飴 é popular"),
    ("お参りします＝去参拜", "お参りします = ir rezar"),
    ("お参り＝去神社参拜", "お参り = ir rezar a um santuário"),
    ("どういたしまして＝不客气", "どういたしまして = de nada"),
    ("七五三是3岁5岁7岁孩子的庆祝活动", "O Shichi-Go-San celebra crianças de 3, 5 e 7 anos"),
    ("七五三是3岁、5岁、7岁孩子的庆祝活动", "O Shichi-Go-San celebra crianças de 3, 5 e 7 anos"),
    ("七五三的中心日在11月15日附近", "O Shichi-Go-San centra-se por volta de 15 de novembro"),
    ("七五三的中心日是11月15日（周日）", "O Shichi-Go-San centra-se a 15 de novembro (domingo)"),
    ("七五三的中心日是11月15日（第3版）", "O Shichi-Go-San centra-se a 15 de novembro (página 3)"),
    ("七五三的孩子去神社参拜", "As crianças do Shichi-Go-San vão rezar a um santuário"),
    ("七五三的照片是全家的回忆", "As fotos do Shichi-Go-San são uma memória de família"),
    ("七五三＝孩子的庆祝活动", "七五三 = uma celebração para crianças"),
    ("七五三＝3岁5岁7岁孩子的庆祝 b", "七五三 = uma celebração para crianças de 3, 5 e 7 anos b"),
    ("东京的红叶在11月29日（周日）前后", "As folhas de Tóquio culminam por volta de 29 de novembro (domingo)"),
    ("主语＋时间＋宾语＋动词", "sujeito + tempo + objeto + verbo"),
    ("主语＋说明", "sujeito + descrição"),
    ("九州场所在福冈国际中心举行", "O torneio de Kyushu realiza-se no Fukuoka Kokusai Center"),
    ("二の酉在11月19日（周四）", "Ni-no-tori é 19 de novembro (quinta-feira)"),
    ("分ける＝分享", "分ける = partilhar"),
    ("前3场比赛连续打延长赛", "Os três primeiros jogos foram todos a entradas extra"),
    ("前3场都是延长赛", "Os três primeiros jogos foram todos a entradas extra"),
    ("千岁糖寄托长寿的愿望", "Chitose-ame traz um desejo de vida longa"),
    ("千岁糖是红白相间的长糖", "Chitose-ame é um doce comprido vermelho e branco"),
    ("千岁糖＝红白长糖", "doce comprido vermelho e branco"),
    ("千歳飴＝红白长糖 a", "千歳飴 = doce comprido vermelho e branco a"),
    ("千歳飴＝红白长糖 d", "千歳飴 = doce comprido vermelho e branco d"),
    ("口号是「静かだけど、冒険中。」", "O slogan é 「静かだけど、冒険中。」"),
    ("周一读图书馆借的书", "À segunda-feira lê um livro da biblioteca"),
    ("周三和朋友分享波奇", "À quarta-feira partilha Pocky com amigos"),
    ("周五去高尾山看红叶", "À sexta-feira vai ao monte Takao ver as folhas"),
    ("周日和妹妹的七五三去神社", "Ao domingo vai a um santuário pelo Shichi-Go-San da irmã"),
    ("四项合计100%", "Os quatro somam 100 %"),
    ("图表中最受欢迎的是山", "A montanha lidera o gráfico"),
    ("图表是真实调查结果", "O gráfico mostra resultados reais de um inquérito"),
    ("在酉の市买熊手", "Comprar um kumade em Tori-no-ichi"),
    ("地点＋へ＋动词", "lugar + へ + verbo"),
    ("场所用「で」", "Usa 「で」 para o lugar"),
    ("大阪的红叶在12月4日（周五）前后", "As folhas de Osaka culminam por volta de 4 de dezembro (sexta-feira)"),
    ("宫岛的红叶从11月21日（周六）前后进入见赏期", "As folhas de Miyajima culminam a partir de 21 de novembro (sábado)"),
    ("宾语＋动词", "objeto + verbo"),
    ("对照第2版", "Ver página 2"),
    ("对照第3版", "Ver página 3"),
    ("对照第6版（追赶见赏期）", "Ver página 6 (atrás da melhor estação)"),
    ("对照第7版", "Ver página 7"),
    ("山34%与神社26%之差为8", "Montanha 34 % menos santuários 26 % são 8"),
    ("山占34%", "Montanha: 34 %"),
    ("岚山的红叶从11月23日（周一）前后进入见赏期", "As folhas de Arashiyama culminam a partir de 23 de novembro (segunda-feira)"),
    ("平成11年11月11日有6个1", "11 de novembro de Heisei 11 tinha seis uns"),
    ("思い出＝回忆", "思い出 = uma memória"),
    ("接戦＝比分接近的比赛", "接戦 = um jogo disputado"),
    ("撮ります＝拍照", "撮ります = tirar uma foto"),
    ("新小结是美ノ海", "O novo komusubi é Umi-no-umi"),
    ("日本大赛第3战在10月27日（周二）", "O jogo 3 das Japan Series foi a 27 de outubro (terça-feira)"),
    ("晴れ着＝庆祝日穿的衣服", "晴れ着 = roupa de dia de festa"),
    ("波奇日从1999年开始", "O dia do Pocky começou em 1999"),
    ("波奇日只买不分享是错的", "O dia do Pocky não é só comprar"),
    ("波奇日在11月11日", "O dia do Pocky é 11 de novembro"),
    ("波奇日在11月11日（周三）", "O dia do Pocky é 11 de novembro (quarta-feira)"),
    ("波奇日定在11月11日因为细长的零食像数字1", "Escolheu-se 11 de novembro porque os snacks finos parecem o número 1"),
    ("波奇日是11月11日", "O dia do Pocky é 11 de novembro"),
    ("波奇日要和朋友分享零食", "O dia do Pocky é partilhar snacks com amigos"),
    ("波奇＝巧克力细饼干", "palito com chocolate"),
    ("ポッキー＝巧克力细饼干 d", "ポッキー = palito com chocolate d"),
    ("渡す＝递给", "渡す = entregar"),
    ("照片长大后家人还会一起看", "A família ainda vê as fotos quando as crianças já cresceram"),
    ("照相馆拍照的家庭是71%", "Famílias que usam estúdio: 71 %"),
    ("熊手＝祈求生意兴隆的竹耙", "熊手 = ancinho da sorte para os negócios"),
    ("熊手＝竹耙吉祥物 b", "熊手 = ancinho da sorte b"),
    ("熊手＝竹耙吉祥物 c", "熊手 = ancinho da sorte c"),
    ("男孩在3岁和5岁庆祝，女孩在3岁和7岁", "Os rapazes celebram aos 3 e 5 anos, as raparigas aos 3 e 7"),
    ("相扑场所到11月22日（周日）", "O torneio de sumo dura até 22 de novembro (domingo)"),
    ("神社占26%", "Santuários: 26 %"),
    ("第3战在横滨举行", "O jogo 3 jogou-se em Yokohama"),
    ("第3战打到延长10局", "O jogo 3 chegou à 10.ª entrada"),
    ("第3战的再见本垒打是正木打出的", "Masaki bateu o home run decisivo do jogo 3"),
    ("第3战软银2-1获胜", "Jogo 3: SoftBank ganhou 2-1"),
    ("第3战软银得2分", "SoftBank marcou 2 no jogo 3"),
    ("第4战软银4-2获胜", "Jogo 4: SoftBank ganhou 4-2"),
    ("第4战软银得4分", "SoftBank marcou 4 no jogo 4"),
    ("第5到第7战没有举行", "Os jogos 5 a 7 não se jogaram"),
    ("第5战也举行了", "O jogo 5 também se jogou"),
    ("系列赛MVP是正木智也", "O MVP da série é Masaki Tomoya"),
    ("红叶见赏期从南向北移动是错的", "A estação das folhas ir de sul para norte está errado"),
    ("细长的零食把人与人连接起来", "Os snacks finos ligam as pessoas"),
    ("西宫神社每年5000组以上参拜", "Mais de 5.000 grupos por ano visitam o santuário Nishinomiya"),
    ("見頃＝最佳观赏期", "見頃 = a melhor estação"),
    ("見頃＝最佳观赏期 c", "見頃 = a melhor estação c"),
    ("读书周从10月27日（周二）开始", "A Semana da Leitura começou a 27 de outubro (terça-feira)"),
    ("读书周在11月9日（周一）结束", "A Semana da Leitura termina a 9 de novembro (segunda-feira)"),
    ("读书周结束后阅读习惯仍继续", "O hábito de ler continua após a Semana da Leitura"),
    ("调查对象是200个七五三家庭", "O inquérito abrangeu 200 famílias de Shichi-Go-San"),
    ("调查显示11月上旬参拜占26%", "As visitas do início de novembro foram 26 % no inquérito"),
    ("调查显示71%的家庭在神社接受祈祷", "71 % das famílias recebem uma oração no santuário, diz o inquérito"),
    ("调查显示74%的家庭在照相馆拍照", "74 % das famílias tiram fotos num estúdio, diz o inquérito"),
    ("调查显示参拜最多的是11月上旬（26%）", "As visitas culminam no início de novembro (26 %), diz o inquérito"),
    ("软银4连胜夺冠", "Quatro vitórias seguidas para o título"),
    ("软银第13次夺冠", "O 13.º título de SoftBank"),
    ("酉の市二の酉在11月19日（周四）", "O Ni-no-tori de Tori-no-ichi é 19 de novembro (quinta-feira)"),
    ("酉の市＝11月酉日集市 a", "酉の市 = uma feira nos dias do galo de novembro a"),
    ("预报日期是见赏期开始的参考标准", "As datas previstas marcam o início da melhor estação"),
    ("高尾山的红叶从11月13日（周五）前后进入见赏期", "As folhas do monte Takao culminam a partir de 13 de novembro (sexta-feira)"),
    ("高尾山的红叶从13日（周五）前后进入最佳观赏期", "As folhas do monte Takao culminam a partir do dia 13 (sexta-feira)"),
    ("鸣子峡已经进入见赏期", "O desfiladeiro de Naruko já está no seu melhor"),
    ("落葉＝落叶 a", "落葉 = folhas caídas a"),
    ("プリッツ＝咸味细饼干 c", "プリッツ = biscoito fino salgado c"),
]

PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Nota — " + s,'),
        ('"Lucerna · 日语周报 VOL.3 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · SEMANÁRIO JAPONÊS VOL.3 · TEXTOS EM JAPONÊS · EXPLICAÇÕES EM PORTUGUÊS"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"'),
    ],
    "content12.py": [
        ('p.text(975, 330, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEXTOS EM JAPONÊS · EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Toda semana · 日本人が読んでいる日本語を読む"'),
        ('"周日是七五三"', '"Domingo é Shichi-Go-San"'),
        ('"红叶最佳观赏期向南移动 · 详见第 6 版"',
         '"A estação das folhas vai para sul · Ver página 6"'),
        ('"トップニュース · 头条"', '"トップニュース · Manchete"'),
        ('"終わる 结束 · お参り 参拜 · 移る 移动 · 熊手 竹耙吉祥物。"',
         '"終わる terminar · お参り visitar um santuário · 移る mover-se · 熊手 ancinho da sorte."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · Números semanais"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Pratica agora"'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Datas nos artigos; não estatísticas exatas"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · Neste número"'),
        ('"全部"', '"Todos os níveis"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Palavra da semana"'),
        ('"千歳飴＝ 七五三的红白长糖。"',
         '"千歳飴 = doce do Shichi-Go-San."'),
        ('"短いニュース · 快讯"', '"短いニュース · Notícias breves"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quiz rápido"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lê a primeira página e escolhe · Respostas na página 8"'),
        ('"レベル A2 · ポッキーの日と千歳飴 · 波奇日与千岁糖"',
         '"レベル A2 · ポッキーの日と千歳飴 · Dia do Pocky e chitose-ame"'),
        ('"細い 细长的 · 似ている 相似 · 分け合う 分享 · 塩味 咸味。"',
         '"細い fino · 似ている parecer · 分け合う partilhar · 塩味 salgado."'),
        ('"願い 愿望 · 撮る 拍照 · 楽しむ 享受。"',
         '"願い um desejo · 撮る tirar uma foto · 楽しむ gostar."'),
        ('"你呢？11月11日想和谁分享波奇？写两句日语寄来。"',
         '"Com quem gostarias de partilhar Pocky a 11 de novembro? Escreve duas frases em japonês e envia-as."'),
        ('"11月のことば · 11月词语"', '"11月のことば · Palavras de novembro"'),
        ('"「1」の日と七五三の4つの言葉 · 关于“1”之日与七五三的四个词"',
         '"「1」の日と七五三の4つの言葉 · Quatro palavras para o dia dos uns e o Shichi-Go-San"'),
        ('"波奇巧克力棒"', '"palito com chocolate"'),
        ('"红白长糖"', '"doce comprido vermelho e branco"'),
        ('"祈求生意兴隆的竹耙"', '"ancinho da sorte para os negócios"'),
        ('"最佳观赏期"', '"a melhor estação"'),
        ('"練習 · 第 2 版练习"', '"練習 · Exercícios da página 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 七五三と酉の市 · 七五三与酉之市"',
         '"レベル A2→B1 · 七五三と酉の市 · Shichi-Go-San e Tori-no-ichi"'),
        ('"成長 成长 · 元気 健康 · 願い 愿望 · 日にち 日期。"',
         '"成長 crescimento · 元気 saudável · 願い um desejo · 日にち a data."'),
        ('"商売繁盛 生意兴隆 · 縁起物 吉祥物 · 並ぶ 排列。"',
         '"商売繁盛 negócios prósperos · 縁起物 amuleto da sorte · 並ぶ fazer fila."'),
        ('"你呢？七五三那天想拍什么样的照片？写两句日语寄来。"',
         '"Que tipo de foto gostarias de tirar no Shichi-Go-San? Escreve duas frases em japonês e envia-as."'),
        ('"練習 · 第 3 版练习"', '"練習 · Exercícios da página 3"'),
        ('"レベル B1 · 日本シリーズ4連勝 · 日本大赛四连胜"',
         '"レベル B1 · 日本シリーズ4連勝 · Quatro vitórias seguidas nas Japan Series"'),
        ('"接戦 势均力敌的比赛 · サヨナラ 再见（致胜） · 連続 连续。"',
         '"接戦 jogo disputado · サヨナラ home run decisivo (sayonara) · 連続 seguidas."'),
        ('"日本シリーズの記録 · 大赛记录"', '"日本シリーズの記録 · Balanço"'),
        ('"前号 上一期 · 全部 全部。"', '"前号 o número anterior · 全部 tudo."'),
        ('"大相撲九州場所が始まりました · 大相扑九州场所开幕"',
         '"大相撲九州場所が始まりました · O torneio de sumo de Kyushu começou"'),
        ('"練習 · 第 4 版练习"', '"練習 · Exercícios da página 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Juventude"'),
        ('"レベル B1 · 11月11日の分かち合い · 11月11日的分享"',
         '"レベル B1 · 11月11日の分かち合い · Partilha a 11 de novembro"'),
        ('"渡す 递给 · つなぐ 连接 · 送り合う 互相发送。"',
         '"渡す entregar · つなぐ ligar · 送り合う enviar um ao outro."'),
        ('"思い出 回忆 · 大きくなる 长大。"',
         '"思い出 uma memória · 大きくなる crescer."'),
        ('"你呢？想把波奇递给谁？写两句日语寄来。"',
         '"A quem gostarias de entregar Pocky? Escreve duas frases em japonês e envia-as."'),
        ('"練習 · 第 5 版练习"', '"練習 · Exercícios da página 5"'),
        ('"レベル B2 · 紅葉の見頃は南へ · 红叶最佳观赏期向南移动"',
         '"レベル B2 · 紅葉の見頃は南へ · A estação das folhas vai para sul"'),
        ('"目安 标准 · 色づき 变色 · 変化 变化 · 準備 准备。"',
         '"目安 uma referência · 色づき coloração · 変化 mudança · 準備 preparação."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Ler o gráfico"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Dados de prática"'),
        ('"練習 · 第 6 版练习"', '"練習 · Exercícios da página 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Língua"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Três níveis, três temas"'),
        ('"読書週間 读书周 · 習慣 习惯 · 借りる 借。"',
         '"読書週間 Semana da Leitura · 習慣 um hábito · 借りる pedir emprestado."'),
        ('"七五三 七五三 · 千歳飴 千岁糖 · 晴れ着 盛装"',
         '"七五三 Shichi-Go-San · 千歳飴 chitose-ame · 晴れ着 roupa de festa"'),
        ('"〜連勝 连胜 · 〜% 百分之〜 · 〜組以上 组以上。"',
         '"〜連勝 vitórias seguidas · 〜% por cento · 〜組以上 grupos ou mais."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Clínica de erros"'),
        ('"有「昨日」时要用过去式。"', '"Com 「昨日」, usa o passado."'),
        ('"动词名词化时要加「こと」。"',
         '"Acrescenta 「こと」 para fazer um nome de um verbo."'),
        ('"得到东西的场所用「で」。"',
         '"Usa 「で」 para o lugar onde recebes algo."'),
        ('"看的场所用「で」。"', '"Usa 「で」 para o lugar onde olhas."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Estrutura semanal"'),
        ('"句式拆解：追赶最佳观赏期。"',
         '"Análise: atrás da melhor estação."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Cantinho dos leitores"'),
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.4に載せます。"',
         'ld_pt = "Exemplo da redação, não uma carta real. Até o prazo não chegaram '
         'cartas nem composições; ambas aparecerão no VOL.4. Enviem-nos a '
         'vossa carta em japonês: as escolhidas serão publicadas '
         'no VOL.4!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.4将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_pt, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_pt, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Frases da semana (textuais, deste número)"'),
        ('"读书周在11月9日星期一结束。"', '"A Semana da Leitura termina na segunda-feira, 9 de novembro."'),
        ('"11月15日星期日是七五三的中心日。"',
         '"Domingo, 15 de novembro, é o coração do Shichi-Go-San."'),
        ('"波奇与百力滋之日始于1999年。"', '"O dia do Pocky e do Pretz começou em 1999."'),
        ('"千岁糖是寄托长寿愿望的糖果。"',
         '"Chitose-ame é o doce do desejo de vida longa."'),
        ('"七五三是3岁、5岁和7岁孩子的庆祝活动。"',
         '"O Shichi-Go-San celebra crianças de 3, 5 e 7 anos."'),
        ('"软银以四连胜夺得日本第一。"',
         '"A SoftBank conquistou o título do Japão com quatro vitórias seguidas."'),
        ('"11月11日是波奇日。"', '"11 de novembro é o dia do Pocky."'),
        ('"红叶的最佳观赏期从北向南移动。"',
         '"A melhor estação das folhas vai de norte para sul."'),
        ('"第1面"', '"pág. 1"'),
        ('"第2面"', '"pág. 2"'),
        ('"第3面"', '"pág. 3"'),
        ('"第4面"', '"pág. 4"'),
        ('"第5面"', '"pág. 5"'),
        ('"第6面"', '"pág. 6"'),
        ('"来週 · 下期预告 (VOL.4)"', '"来週 · Próximo número (VOL.4)"'),
    ],
    "content8.py": [
        ('af.para(f"— 第{pg}面 —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)', 'af.para(f"— 第{pg}面 —", 12.9, "sans", True, OLIVE, lh=1.13, gap=2, split=False)'),
        ('af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)', 'af.para(txt, 12.9, lh=1.13, gap=0.5, split=False)'),
        ('"テストと答え · 练习与答案"', '"テストと答え · Teste e respostas"'),
        ('"七五三是11月15日。"', '"O Shichi-Go-San é 15 de novembro."'),
        ('"波奇日从1999年开始。"', '"O dia do Pocky começou em 1999."'),
        ('"读书周从10月27日开始。→ ___"',
         '"A Semana da Leitura começa a 27 de outubro. → ___"'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。→ ___"',
         '"Quem vai ver as folhas pode ir atrás da melhor estação de norte para sul. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Tarefa de redação (sem uma única resposta certa); o texto modelo ({NCHARS} caracteres) está abaixo."'),
        ('"（开放题，范文如下）"', '"(tarefa aberta — texto modelo abaixo)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Texto modelo na secção H desta página ({NCHARS} caracteres)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Respostas — agrupadas por página; encontra só o teu número"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Uma breve nota em português com cada resposta · ✓ = o exercício com texto modelo"'),
        ('f"— 第{pg}面 —"', 'f"— Página {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL3.pdf"', '"Lucerna-VOL3-PT.pdf"'),
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
    src_svg = os.path.join(CORE, "svglib.py")
    data = open(src_svg, "rb").read()
    assert hashlib.md5(data).hexdigest() == CANON_SVGLIB_MD5, "svglib md5 mismatch"
    shutil.copyfile(src_svg, os.path.join(HERE, "svglib.py"))
    shutil.copyfile(os.path.join(CORE, "run.py"), os.path.join(HERE, "run.py"))
    os.makedirs(os.path.join(HERE, "assets"), exist_ok=True)
    for f in os.listdir(os.path.join(CORE, "assets")):
        shutil.copyfile(os.path.join(CORE, "assets", f),
                        os.path.join(HERE, "assets", f))
    note_map = dict(NOTES)
    fnames = ["bslib4.py", "content12.py", "content34.py", "content56.py",
              "content7.py", "content8.py", "render.py"]
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
