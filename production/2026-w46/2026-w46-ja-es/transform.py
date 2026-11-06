# -*- coding: utf-8 -*-
"""JA core (VOL.3, Chinese explanations) -> JA x ES edition transform.

Re-runnable: reads the PRISTINE W46 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets), and writes the
edition build into this directory. Fix rounds edit THIS file, then
re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> Spanish, per the W45 JA x ES shipped precedent.
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
    "files/weekly-report-w46-ja-es")
CANON_SVGLIB_MD5 = "74177544422fe677639d769cd80499fb"

GLOBAL = [
    ("weekly-report-w46-ja-core", "weekly-report-w46-ja-es"),
    ('instr="造句"', 'instr="Construye una frase"'),
    ('instr="翻译"', 'instr="Traduce"'),
    ('instr="写作"', 'instr="Redacción"'),
    ('instr="判断"', 'instr="¿Verdadero o falso?"'),
    ('instr="填空"', 'instr="Completa"'),
    ('instr="把词和释义配对"', 'instr="Une palabras y sentidos"'),
    ('"完形单选"', '"cloze"'),
    ('"单选"', '"opción múltiple"'),
    ('"完成句子"', '"completar"'),
    ('"词汇配对"', '"relacionar"'),
    ('"造句"', '"construcción de frases"'),
    ('"判断对错"', '"verdadero/falso"'),
    ('"翻译"', '"traducción"'),
    ('"写作"', '"redacción"'),
    ('"あなたは？ · 说说你自己"', '"あなたは？ · Tu turno"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Respuestas en la página 8 · Niveles mezclados: busca tu número"'),
]

NOTES = [
    ("1111中有4个1", "1111 tiene cuatro unos"),
    ("1111看起来像4根细棒", "1111 parece cuatro palitos finos"),
    ("11月中旬以后进入见赏期的地点多比往年稍晚", "Los lugares que culminan tras mediados de noviembre suelen ir con retraso"),
    ("2026年没有三の酉", "No hay San-no-tori en 2026"),
    ("3%≈100人中的3人", "3 % es unos 3 de cada 100"),
    ("34+26=60", "34 + 26 = 60"),
    ("4连胜夺冠", "Cuatro victorias seguidas dieron el título"),
    ("4连胜＝4场比赛全胜", "ganar los cuatro partidos"),
    ("71%的家庭接受祈祷", "El 71 % de las familias recibe una oración"),
    ("74%的家庭在照相馆拍照", "El 74 % de las familias se hace fotos en un estudio"),
    ("Weathernews的预报在10月29日（周四）", "El pronóstico de Weathernews era del 29 de octubre (jueves)"),
    ("「千歳飴」受欢迎", "千歳飴 es popular"),
    ("お参りします＝去参拜", "お参りします = ir a rezar"),
    ("お参り＝去神社参拜", "お参り = ir a rezar a un santuario"),
    ("どういたしまして＝不客气", "どういたしまして = de nada"),
    ("七五三是3岁5岁7岁孩子的庆祝活动", "Shichi-Go-San celebra a los niños de 3, 5 y 7 años"),
    ("七五三是3岁、5岁、7岁孩子的庆祝活动", "Shichi-Go-San celebra a los niños de 3, 5 y 7 años"),
    ("七五三的中心日在11月15日附近", "Shichi-Go-San se centra en torno al 15 de noviembre"),
    ("七五三的中心日是11月15日（周日）", "Shichi-Go-San se centra el 15 de noviembre (domingo)"),
    ("七五三的中心日是11月15日（第3版）", "Shichi-Go-San se centra el 15 de noviembre (página 3)"),
    ("七五三的孩子去神社参拜", "Los niños de Shichi-Go-San van a rezar a un santuario"),
    ("七五三的照片是全家的回忆", "Las fotos de Shichi-Go-San son un recuerdo familiar"),
    ("七五三＝孩子的庆祝活动", "七五三 = una celebración para niños"),
    ("七五三＝3岁5岁7岁孩子的庆祝 b", "七五三 = una celebración para niños de 3, 5 y 7 años b"),
    ("东京的红叶在11月29日（周日）前后", "Las hojas de Tokio culminan hacia el 29 de noviembre (domingo)"),
    ("主语＋时间＋宾语＋动词", "sujeto + tiempo + objeto + verbo"),
    ("主语＋说明", "sujeto + descripción"),
    ("九州场所在福冈国际中心举行", "El torneo de Kyushu se celebra en el Fukuoka Kokusai Center"),
    ("二の酉在11月19日（周四）", "Ni-no-tori es el 19 de noviembre (jueves)"),
    ("分ける＝分享", "分ける = compartir"),
    ("前3场比赛连续打延长赛", "Los tres primeros partidos llegaron todos a entradas extra"),
    ("前3场都是延长赛", "Los tres primeros partidos llegaron todos a entradas extra"),
    ("千岁糖寄托长寿的愿望", "Chitose-ame lleva un deseo de larga vida"),
    ("千岁糖是红白相间的长糖", "Chitose-ame es un caramelo largo rojo y blanco"),
    ("千岁糖＝红白长糖", "caramelo largo rojo y blanco"),
    ("千歳飴＝红白长糖 a", "千歳飴 = caramelo largo rojo y blanco a"),
    ("千歳飴＝红白长糖 d", "千歳飴 = caramelo largo rojo y blanco d"),
    ("口号是「静かだけど、冒険中。」", "El lema es 「静かだけど、冒険中。」"),
    ("周一读图书馆借的书", "El lunes lee un libro de la biblioteca"),
    ("周三和朋友分享波奇", "El miércoles comparte Pocky con amigos"),
    ("周五去高尾山看红叶", "El viernes va al monte Takao a ver las hojas"),
    ("周日和妹妹的七五三去神社", "El domingo va a un santuario por el Shichi-Go-San de su hermana"),
    ("四项合计100%", "Los cuatro suman 100 %"),
    ("图表中最受欢迎的是山", "La montaña encabeza el gráfico"),
    ("图表是真实调查结果", "El gráfico muestra resultados reales de una encuesta"),
    ("在酉の市买熊手", "Comprar un kumade en Tori-no-ichi"),
    ("地点＋へ＋动词", "lugar + へ + verbo"),
    ("场所用「で」", "Usa 「で」 para el lugar"),
    ("大阪的红叶在12月4日（周五）前后", "Las hojas de Osaka culminan hacia el 4 de diciembre (viernes)"),
    ("宫岛的红叶从11月21日（周六）前后进入见赏期", "Las hojas de Miyajima culminan desde el 21 de noviembre (sábado)"),
    ("宾语＋动词", "objeto + verbo"),
    ("对照第2版", "Ver página 2"),
    ("对照第3版", "Ver página 3"),
    ("对照第6版（追赶见赏期）", "Ver página 6 (tras la mejor temporada)"),
    ("对照第7版", "Ver página 7"),
    ("山34%与神社26%之差为8", "Montaña 34 % menos santuarios 26 % son 8"),
    ("山占34%", "Montaña: 34 %"),
    ("岚山的红叶从11月23日（周一）前后进入见赏期", "Las hojas de Arashiyama culminan desde el 23 de noviembre (lunes)"),
    ("平成11年11月11日有6个1", "El 11 de noviembre de Heisei 11 tenía seis unos"),
    ("思い出＝回忆", "思い出 = un recuerdo"),
    ("接戦＝比分接近的比赛", "接戦 = un partido reñido"),
    ("撮ります＝拍照", "撮ります = hacer una foto"),
    ("新小结是美ノ海", "El nuevo komusubi es Umi-no-umi"),
    ("日本大赛第3战在10月27日（周二）", "El partido 3 de las Japan Series fue el 27 de octubre (martes)"),
    ("晴れ着＝庆祝日穿的衣服", "晴れ着 = ropa de día de fiesta"),
    ("波奇日从1999年开始", "El día de Pocky empezó en 1999"),
    ("波奇日只买不分享是错的", "El día de Pocky no es solo comprar"),
    ("波奇日在11月11日", "El día de Pocky es el 11 de noviembre"),
    ("波奇日在11月11日（周三）", "El día de Pocky es el 11 de noviembre (miércoles)"),
    ("波奇日定在11月11日因为细长的零食像数字1", "Se eligió el 11 de noviembre porque los snacks finos parecen el número 1"),
    ("波奇日是11月11日", "El día de Pocky es el 11 de noviembre"),
    ("波奇日要和朋友分享零食", "El día de Pocky es compartir snacks con amigos"),
    ("波奇＝巧克力细饼干", "palito con chocolate"),
    ("ポッキー＝巧克力细饼干 d", "ポッキー = palito con chocolate d"),
    ("渡す＝递给", "渡す = entregar"),
    ("照片长大后家人还会一起看", "La familia sigue mirando las fotos cuando los niños ya son mayores"),
    ("照相馆拍照的家庭是71%", "Familias que usan un estudio: 71 %"),
    ("熊手＝祈求生意兴隆的竹耙", "熊手 = rastrillo de la suerte para los negocios"),
    ("熊手＝竹耙吉祥物 b", "熊手 = rastrillo de la suerte b"),
    ("熊手＝竹耙吉祥物 c", "熊手 = rastrillo de la suerte c"),
    ("男孩在3岁和5岁庆祝，女孩在3岁和7岁", "Los niños celebran a los 3 y 5 años, las niñas a los 3 y 7"),
    ("相扑场所到11月22日（周日）", "El torneo de sumo dura hasta el 22 de noviembre (domingo)"),
    ("神社占26%", "Santuarios: 26 %"),
    ("第3战在横滨举行", "El partido 3 se jugó en Yokohama"),
    ("第3战打到延长10局", "El partido 3 llegó a la 10.ª entrada"),
    ("第3战的再见本垒打是正木打出的", "Masaki bateó el jonrón decisivo del partido 3"),
    ("第3战软银2-1获胜", "Partido 3: SoftBank ganó 2-1"),
    ("第3战软银得2分", "SoftBank marcó 2 en el partido 3"),
    ("第4战软银4-2获胜", "Partido 4: SoftBank ganó 4-2"),
    ("第4战软银得4分", "SoftBank marcó 4 en el partido 4"),
    ("第5到第7战没有举行", "Los partidos 5 a 7 no se jugaron"),
    ("第5战也举行了", "El partido 5 también se jugó"),
    ("系列赛MVP是正木智也", "El MVP de la serie es Masaki Tomoya"),
    ("红叶见赏期从南向北移动是错的", "Que la temporada de hojas vaya de sur a norte es falso"),
    ("细长的零食把人与人连接起来", "Los snacks finos conectan a la gente"),
    ("西宫神社每年5000组以上参拜", "Más de 5.000 grupos al año visitan el santuario Nishinomiya"),
    ("見頃＝最佳观赏期", "見頃 = la mejor temporada"),
    ("見頃＝最佳观赏期 c", "見頃 = la mejor temporada c"),
    ("读书周从10月27日（周二）开始", "La Semana de la Lectura empezó el 27 de octubre (martes)"),
    ("读书周在11月9日（周一）结束", "La Semana de la Lectura termina el 9 de noviembre (lunes)"),
    ("读书周结束后阅读习惯仍继续", "El hábito de leer sigue tras la Semana de la Lectura"),
    ("调查对象是200个七五三家庭", "La encuesta abarcó 200 familias de Shichi-Go-San"),
    ("调查显示11月上旬参拜占26%", "Las visitas de principios de noviembre fueron el 26 % en la encuesta"),
    ("调查显示71%的家庭在神社接受祈祷", "El 71 % de las familias recibe una oración en el santuario, dice la encuesta"),
    ("调查显示74%的家庭在照相馆拍照", "El 74 % de las familias se hace fotos en un estudio, dice la encuesta"),
    ("调查显示参拜最多的是11月上旬（26%）", "Las visitas culminan a principios de noviembre (26 %), dice la encuesta"),
    ("软银4连胜夺冠", "Cuatro victorias seguidas para el título"),
    ("软银第13次夺冠", "El 13.º título de SoftBank"),
    ("酉の市二の酉在11月19日（周四）", "El Ni-no-tori de Tori-no-ichi es el 19 de noviembre (jueves)"),
    ("酉の市＝11月酉日集市 a", "酉の市 = una feria en los días del gallo de noviembre a"),
    ("预报日期是见赏期开始的参考标准", "Las fechas previstas marcan el inicio de la mejor temporada"),
    ("高尾山的红叶从11月13日（周五）前后进入见赏期", "Las hojas del monte Takao culminan desde el 13 de noviembre (viernes)"),
    ("高尾山的红叶从13日（周五）前后进入最佳观赏期", "Las hojas del monte Takao culminan desde el 13 (viernes)"),
    ("鸣子峡已经进入见赏期", "El desfiladero de Naruko ya está en su mejor momento"),
    ("落葉＝落叶 a", "落葉 = hojas caídas a"),
    ("プリッツ＝咸味细饼干 c", "プリッツ = galleta fina salada c"),
]

PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Nota — " + s,'),
        ('"Lucerna · 日语周报 VOL.3 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · SEMANARIO JAPONÉS VOL.3 · TEXTO EN JAPONÉS · EXPLICACIONES EN ESPAÑOL"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"'),
    ],
    "content12.py": [
        ('p.text(975, 330, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.3 · 七五三 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEXTOS EN JAPONÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Cada semana · 日本人が読んでいる日本語を読む"'),
        ('"周日是七五三"', '"El domingo es Shichi-Go-San"'),
        ('"红叶最佳观赏期向南移动 · 详见第 6 版"',
         '"La temporada de hojas va hacia el sur · Ver página 6"'),
        ('"トップニュース · 头条"', '"トップニュース · Noticia principal"'),
        ('"終わる 结束 · お参り 参拜 · 移る 移动 · 熊手 竹耙吉祥物。"',
         '"終わる terminar · お参り visitar un santuario · 移る moverse · 熊手 rastrillo de la suerte."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · La semana en cifras"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Practica ahora"'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Fechas: ver artículos; no estadísticas exactas"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · En este número"'),
        ('"全部"', '"Todos los niveles"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Palabra de la semana"'),
        ('"千歳飴＝ 七五三的红白长糖。"',
         '"千歳飴 = caramelo de Shichi-Go-San."'),
        ('"短いニュース · 快讯"', '"短いニュース · Noticias breves"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quiz rápido"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lee la primera página y elige · Respuestas en la página 8"'),
        ('"レベル A2 · ポッキーの日と千歳飴 · 波奇日与千岁糖"',
         '"レベル A2 · ポッキーの日と千歳飴 · Día de Pocky y chitose-ame"'),
        ('"細い 细长的 · 似ている 相似 · 分け合う 分享 · 塩味 咸味。"',
         '"細い fino · 似ている parecerse · 分け合う compartir · 塩味 salado."'),
        ('"願い 愿望 · 撮る 拍照 · 楽しむ 享受。"',
         '"願い un deseo · 撮る hacer una foto · 楽しむ disfrutar."'),
        ('"你呢？11月11日想和谁分享波奇？写两句日语寄来。"',
         '"¿Con quién te gustaría compartir Pocky el 11 de noviembre? Escribe dos frases en japonés y envíalas."'),
        ('"11月のことば · 11月词语"', '"11月のことば · Palabras de noviembre"'),
        ('"「1」の日と七五三の4つの言葉 · 关于“1”之日与七五三的四个词"',
         '"「1」の日と七五三の4つの言葉 · Cuatro palabras para el día de los unos y Shichi-Go-San"'),
        ('"波奇巧克力棒"', '"palito con chocolate"'),
        ('"红白长糖"', '"caramelo largo rojo y blanco"'),
        ('"祈求生意兴隆的竹耙"', '"rastrillo de la suerte para los negocios"'),
        ('"最佳观赏期"', '"la mejor temporada"'),
        ('"練習 · 第 2 版练习"', '"練習 · Ejercicios de la página 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 七五三と酉の市 · 七五三与酉之市"',
         '"レベル A2→B1 · 七五三と酉の市 · Shichi-Go-San y Tori-no-ichi"'),
        ('"成長 成长 · 元気 健康 · 願い 愿望 · 日にち 日期。"',
         '"成長 crecimiento · 元気 sano · 願い un deseo · 日にち la fecha."'),
        ('"商売繁盛 生意兴隆 · 縁起物 吉祥物 · 並ぶ 排列。"',
         '"商売繁盛 negocios prósperos · 縁起物 amuleto de la suerte · 並ぶ hacer cola."'),
        ('"你呢？七五三那天想拍什么样的照片？写两句日语寄来。"',
         '"¿Qué tipo de foto te gustaría hacer en Shichi-Go-San? Escribe dos frases en japonés y envíalas."'),
        ('"練習 · 第 3 版练习"', '"練習 · Ejercicios de la página 3"'),
        ('"レベル B1 · 日本シリーズ4連勝 · 日本大赛四连胜"',
         '"レベル B1 · 日本シリーズ4連勝 · Cuatro victorias seguidas en las Japan Series"'),
        ('"接戦 势均力敌的比赛 · サヨナラ 再见（致胜） · 連続 连续。"',
         '"接戦 partido reñido · サヨナラ jonrón decisivo (sayonara) · 連続 seguidas."'),
        ('"日本シリーズの記録 · 大赛记录"', '"日本シリーズの記録 · Serie de Japón"'),
        ('"前号 上一期 · 全部 全部。"', '"前号 el número anterior · 全部 todo."'),
        ('"大相撲九州場所が始まりました · 大相扑九州场所开幕"',
         '"大相撲九州場所が始まりました · Ha empezado el torneo de sumo de Kyushu"'),
        ('"練習 · 第 4 版练习"', '"練習 · Ejercicios de la página 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Juventud"'),
        ('"レベル B1 · 11月11日の分かち合い · 11月11日的分享"',
         '"レベル B1 · 11月11日の分かち合い · Compartir el 11 de noviembre"'),
        ('"渡す 递给 · つなぐ 连接 · 送り合う 互相发送。"',
         '"渡す entregar · つなぐ conectar · 送り合う enviarse."'),
        ('"思い出 回忆 · 大きくなる 长大。"',
         '"思い出 un recuerdo · 大きくなる crecer."'),
        ('"你呢？想把波奇递给谁？写两句日语寄来。"',
         '"¿A quién te gustaría entregar Pocky? Escribe dos frases en japonés y envíalas."'),
        ('"練習 · 第 5 版练习"', '"練習 · Ejercicios de la página 5"'),
        ('"レベル B2 · 紅葉の見頃は南へ · 红叶最佳观赏期向南移动"',
         '"レベル B2 · 紅葉の見頃は南へ · La temporada de hojas va hacia el sur"'),
        ('"目安 标准 · 色づき 变色 · 変化 变化 · 準備 准备。"',
         '"目安 una guía · 色づき coloración · 変化 cambio · 準備 preparación."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Leer el gráfico"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Datos de práctica"'),
        ('"練習 · 第 6 版练习"', '"練習 · Ejercicios de la página 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Lengua"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Tres niveles, tres temas"'),
        ('"読書週間 读书周 · 習慣 习惯 · 借りる 借。"',
         '"読書週間 Semana de la Lectura · 習慣 un hábito · 借りる tomar prestado."'),
        ('"七五三 七五三 · 千歳飴 千岁糖 · 晴れ着 盛装"',
         '"七五三 Shichi-Go-San · 千歳飴 chitose-ame · 晴れ着 ropa de fiesta"'),
        ('"〜連勝 连胜 · 〜% 百分之〜 · 〜組以上 组以上。"',
         '"〜連勝 victorias seguidas · 〜% por ciento · 〜組以上 grupos o más."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Clínica de errores"'),
        ('"有「昨日」时要用过去式。"', '"Con 「昨日」, usa el pasado."'),
        ('"动词名词化时要加「こと」。"',
         '"Añade 「こと」 para convertir un verbo en sustantivo."'),
        ('"得到东西的场所用「で」。"',
         '"Usa 「で」 para el lugar donde recibes algo."'),
        ('"看的场所用「で」。"', '"Usa 「で」 para el lugar de mirar."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Estructura semanal"'),
        ('"句式拆解：追赶最佳观赏期。"',
         '"Desglose: ir tras la mejor temporada."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Rincón de los lectores"'),
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.4に載せます。"',
         'ld_es = "Ejemplo de la redacción, no una carta real. Hasta la fecha límite '
         'no llegaron cartas ni composiciones; ambas aparecerán en el VOL.4. '
         '¡Enviadnos vuestra carta en japonés: las elegidas se publicarán '
         'en el VOL.4!"'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.4将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_es, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_es, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Frases de la semana (textuales, de este número)"'),
        ('"读书周在11月9日星期一结束。"', '"La Semana de la Lectura termina el lunes 9."'),
        ('"11月15日星期日是七五三的中心日。"',
         '"El domingo 15 es el corazón de Shichi-Go-San."'),
        ('"波奇与百力滋之日始于1999年。"', '"El día de Pocky y Pretz empezó en 1999."'),
        ('"千岁糖是寄托长寿愿望的糖果。"',
         '"Chitose-ame es el caramelo del deseo de larga vida."'),
        ('"七五三是3岁、5岁和7岁孩子的庆祝活动。"',
         '"Shichi-Go-San celebra a los niños de 3, 5 y 7 años."'),
        ('"软银以四连胜夺得日本第一。"',
         '"SoftBank se llevó el título de Japón con cuatro victorias seguidas."'),
        ('"11月11日是波奇日。"', '"El 11 de noviembre es el día de Pocky."'),
        ('"红叶的最佳观赏期从北向南移动。"',
         '"La mejor temporada de hojas va del norte al sur."'),
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
        ('"テストと答え · 练习与答案"', '"テストと答え · Test y respuestas"'),
        ('"七五三是11月15日。"', '"Shichi-Go-San es el 15 de noviembre."'),
        ('"波奇日从1999年开始。"', '"El día de Pocky empezó en 1999."'),
        ('"读书周从10月27日开始。→ ___"',
         '"La Semana de la Lectura empieza el 27 de octubre. → ___"'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。→ ___"',
         '"Quienes van a ver las hojas pueden ir tras la mejor temporada del norte al sur. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Tarea de redacción (sin una única respuesta correcta); el texto modelo ({NCHARS} caracteres) está abajo."'),
        ('"（开放题，范文如下）"', '"(tarea abierta: texto modelo abajo)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"Texto modelo en la sección H de esta página ({NCHARS} caracteres)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Respuestas: agrupadas por página; solo busca tu número"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Una breve nota en español con cada respuesta · ✓ = el ejercicio con texto modelo"'),
        ('f"— 第{pg}面 —"', 'f"— PÁGINA {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL3.pdf"', '"Lucerna-VOL3-ES.pdf"'),
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
