# -*- coding: utf-8 -*-
"""JA core (VOL.2, Chinese explanations) -> JA x ES edition transform.

Re-runnable: reads the PRISTINE W45 JA core build, applies exact-literal
replacements (whole strings, never AST byte offsets, never byte slicing),
and writes the edition build into this directory. Fix rounds edit THIS
file, then re-run: transform.py -> run.py (one process) -> render.py.

Frozen: every Japanese article/stem/option/letter/figure string is copied
byte-identical. Only the explanation layer changes: Chinese notes/glosses/
headers/instructions -> Spanish, per the W43 JA x ES shipped precedent
(files/weekly-report-ja-es). Masthead geometry follows the W43 JA x ES
shipped SVG exactly (wordmark 248, edition 316, badge 356 at 19pt bold
BRICK, tagline 390, rules 406/413, dark band 424).
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
    "files/weekly-report-w45-ja-es")
CANON_SVGLIB_MD5 = "d73e23b365676c3618d7e060b835eb4d"

# (old, new) applied in order. Longer strings first where one contains another.
GLOBAL = [
    # --- output repoint ---
    ("weekly-report-w45-ja-core", "weekly-report-w45-ja-es"),
    # --- registry type names / instructions (W43 JA x ES wording) ---
    ('instr="造句"', 'instr="Forma una frase"'),
    ('instr="翻译"', 'instr="Traduce"'),
    ('instr="写作"', 'instr="Redacción"'),
    ('instr="判断"', 'instr="Verdadero/falso"'),
    ('instr="填空"', 'instr="Completa"'),
    ('instr="把词和释义配对"', 'instr="Une palabra y definición"'),
    ('instr="把活动和地点·时间配对"', 'instr="Une cada evento con su lugar y fecha"'),
    ('"完形单选"', '"Texto con huecos"'),
    ('"单选"', '"Opción múltiple"'),
    ('"完成句子"', '"Completar"'),
    ('"词汇配对"', '"Emparejar"'),
    ('"造句"', '"Formar una frase"'),
    ('"判断对错"', '"Verdadero o falso"'),
    ('"翻译"', '"Traducción"'),
    ('"写作"', '"Redacción"'),
    # --- shared furniture ---
    ('"あなたは？ · 说说你自己"', '"あなたは？ · Tu turno"'),
    ('"答案见第 8 版 · 题目可跨级混排，按题号找答案"',
     '"Respuestas en la página 8 · Niveles mezclados: busca tu número"'),
]

# Answer-note translations. One Spanish rendering per distinct core note;
# duplicates share the rendering (correct: same note -> same meaning).
NOTES = [
    ("文化日在11月3日（周二）", "El Día de la Cultura es el 3 de noviembre (martes)"),
    ("读书周到11月9日（周一）", "Semana de la Lectura hasta el 9 de noviembre (lunes)"),
    ("工艺展到11月8日", "La exposición dura hasta el 8 de noviembre"),
    ("見頃＝最佳观赏期", "見頃 = mejor época para ver las hojas"),
    ("立冬＝冬天的开始", "立冬 = el inicio del invierno"),
    ("神户灯光秀从7日（周六）开始", "La iluminación de Kobe empieza el día 7 (sábado)"),
    ("文化日全国都有文化活动", "Día de la Cultura: actividades en todo el país"),
    ("立冬在11月7日（周六）", "立冬 es el 7 de noviembre (sábado)"),
    ("灯光秀在神户开始", "La iluminación empieza en Kobe"),
    ("「ゆる」＝无理をしない", "「ゆる」 = no forzarse"),
    ("鍋の食卓は去年の1.5倍", "Las cenas de olla son 1,5 veces las del año pasado"),
    ("発表は10月21日", "El anuncio fue el 21 de octubre"),
    ("11月から1月まで気温は平年より高い",
     "De noviembre a enero, sobre la media"),
    ("服と食事の話題はnoteのまとめによるもの",
     "Los temas de ropa y comida vienen del resumen de note"),
    ("ゆる＝轻松、不勉强", "ゆる = relajado, sin forzarse"),
    ("蒸し器＝蒸笼", "蒸し器 = una vaporera"),
    ("整える＝调理、调养", "整える = poner en orden"),
    ("鍋＝一锅菜", "鍋 = un plato de olla"),
    ("鍋の材料が1か月早く並んだ", "Los ingredientes para la olla llegaron un mes antes"),
    ("気象庁の予報は10月20日", "El pronóstico de la JMA fue el 20 de octubre"),
    ("サクサクdeコパンが1,300万食を超えた",
     "サクサクdeコパン superó los 13 millones de raciones"),
    ("ゆる＝轻松 b", "ゆる = relajado b"),
    ("蒸し器＝蒸笼 a", "蒸し器 = vaporera a"),
    ("麻辣湯＝辛いスープ d", "麻辣湯 = plato de sopa picante d"),
    ("予報＝天気の予想 c", "予報 = pronóstico del tiempo c"),
    ("杉并的活动是家庭管弦乐队", "El evento de Suginami es una orquesta familiar"),
    ("传统工艺展在石川县立美术馆",
     "La exposición está en el Museo de Arte de Ishikawa"),
    ("传统工艺展到11月8日", "La exposición dura hasta el 8 de noviembre"),
    ("灯光秀在金泽城和兼六园", "Iluminación: castillo de Kanazawa y Kenrokuen"),
    ("市場＝集市", "市場 = mercado"),
    ("工芸＝工艺", "工芸 = artesanía"),
    ("陶器＝陶瓷", "陶器 = cerámica"),
    ("工艺展到11月8日（周日）", "La exposición dura hasta el 8 de noviembre (domingo)"),
    ("金箔＝金箔", "金箔 = pan de oro"),
    ("主语＋时间", "sujeto + tiempo"),
    ("地点＋で＋あります", "lugar + で + あります"),
    ("见たい＝想看", "見たい = querer ver"),
    ("和家人一起", "con la familia"),
    ("文化の日＝11月3日 b", "文化の日 = 3 de noviembre b"),
    ("工芸展＝美術館 c", "工芸展 = museo c"),
    ("オーケストラ＝杉並 d", "オーケストラ = Suginami d"),
    ("ライトアップ＝金沢城 a", "ライトアップ = castillo de Kanazawa a"),
    ("第1战软银3-1胜DeNA", "Partido 1: SoftBank ganó a DeNA por 3–1"),
    ("第2战逆转的是筒香的3分本垒打", "El jonrón de 3 carreras de Tsutsugo dio la vuelta al partido 2"),
    ("2连胜开局的是软银", "SoftBank empezó con dos victorias seguidas"),
    ("2连胜开局的夺冠率是73%", "Empezar 2–0: título el 73% de las veces"),
    ("2024年夺冠的是DeNA", "DeNA ganó el título en 2024"),
    ("第1战软银得3分", "SoftBank marcó 3 en el partido 1"),
    ("第2战软银得4分", "SoftBank marcó 4 en el partido 2"),
    ("第1战打到延长11局", "El partido 1 llegó a 11 entradas"),
    ("第2战打到延长10局", "El partido 2 llegó a 10 entradas"),
    ("夺冠率73%", "Tasa de título: 73%"),
    ("延長＝比赛延长", "延長 = el partido se alarga"),
    ("第1战观众33,388人", "Partido 1: 33.388 espectadores"),
    ("第2战观众33,432人", "Partido 2: 33.432 espectadores"),
    ("相川监督说「4场胜负之战」", "El entrenador Aikawa habló de una lucha a cuatro victorias"),
    ("第1戦は土よう日です", "El partido 1 fue el sábado"),
    ("ソフトバンクが2連勝しました", "SoftBank ganó dos seguidos"),
    ("第2戦も延長戦でした", "El partido 2 también llegó a entradas extra"),
    ("2024年はDeNAが優勝しました", "En 2024 DeNA ganó el título"),
    ("万圣节在10月31日（周六）", "Halloween fue el 31 de octubre (sábado)"),
    ("涩谷禁酒时间是18时到5时", "Shibuya: prohibido beber en la calle de 18:00 a 05:00"),
    ("乱扔垃圾罚款2,000日元", "Tirar basura cuesta una multa de 2.000 yenes"),
    ("化妆活动在池袋", "El festival de cosplay está en Ikebukuro"),
    ("横滨中区民祭在11月8日（周日）", "El festival del distrito de Naka, en Yokohama, es el 8 de noviembre (domingo)"),
    ("万圣节在10月31日", "Halloween fue el 31 de octubre"),
    ("禁酒从18时开始", "La prohibición empieza a las 18:00"),
    ("禁酒到早上5时", "La prohibición dura hasta las 05:00"),
    ("横滨祭典在11月8日", "El festival de Yokohama es el 8 de noviembre"),
    ("夜里路上不能喝酒", "De noche no se puede beber en la calle"),
    ("ゴミの罰金は今年6月からです", "La multa por basura existe desde junio de este año"),
    ("コスプレフェスは池袋です", "El festival de cosplay está en Ikebukuro"),
    ("ハロウィンは10月31日（土）", "Halloween fue el 31 de octubre (sábado)"),
    ("飲むことができません＝不能喝", "飲むことができません = no se puede beber"),
    ("守って、〜しましょう", "守って + 〜しましょう = cumplir las reglas y, ¡vamos a…!"),
    ("フェンスの中＝围栏里面", "フェンスの中 = dentro de la valla"),
    ("活动从10月30日到11月1日", "El festival fue del 30 de octubre al 1 de noviembre"),
    ("雨が多いのは太平洋側", "En el lado del Pacífico llueve más"),
    ("九州の旅の検索は去年のほぼ2倍",
     "Búsquedas de viajes a Kyushu: casi el doble"),
    ("1回の旅の予算は下がった", "El presupuesto por viaje bajó"),
    ("鳴子峡の見頃は10月31日から11月8日の週末",
     "Naruko en su pico: 31 de octubre–8 de noviembre"),
    ("图中最受欢迎的是近处的满足感", "La respuesta más popular del gráfico es la satisfacción cercana"),
    ("近场满足感38%", "Satisfacción cercana: 38%"),
    ("温泉27%", "Aguas termales: 27%"),
    ("红叶21%与美食14%之差为7", "Hojas 21% menos comida 14% es 7"),
    ("38+27=65", "38 + 27 = 65"),
    ("四项合计100%", "Los cuatro suman 100%"),
    ("立冬在11月7日", "立冬 es el 7 de noviembre"),
    ("神户灯光秀到12月28日", "La iluminación de Kobe dura hasta el 28 de diciembre"),
    ("九州旅行搜索约为去年的2倍",
     "Búsquedas de viajes a Kyushu: casi el doble"),
    ("气象厅预报在10月20日", "El pronóstico de la JMA fue el 20 de octubre"),
    ("11月は平年より暖かい予報です", "Noviembre se prevé más cálido que la media"),
    ("九州の旅の検索は増えました", "Las búsquedas de viajes a Kyushu aumentaron"),
    ("グラフは練習用データです", "El gráfico es un dato de práctica"),
    ("读书周从10月27日（周二）开始", "La Semana de la Lectura empezó el 27 de octubre (martes)"),
    ("读书周到11月9日", "La Semana de la Lectura dura hasta el 9 de noviembre"),
    ("口号是「静かだけど、冒険中。」", "El lema es 「静かだけど、冒険中。」"),
    ("图书馆活动有图书介绍", "El evento de la biblioteca es la presentación de libros"),
    ("見頃＝红叶最美的时候", "見頃 = cuando las hojas se ven más bonitas"),
    ("紅葉狩り＝去看红叶", "紅葉狩り = salir a ver las hojas"),
    ("ライトアップ＝夜里用灯光照亮", "ライトアップ = iluminar de noche"),
    ("落葉＝落叶", "落葉 = hojas caídas"),
    ("1.5倍＝比去年多50%", "1.5倍 = 50% más que el año pasado"),
    ("73%≈4人中的3人", "73% ≈ 3 de cada 4"),
    ("サクサクdeコパンが1,300万食", "サクサクdeコパン llegó a 13 millones de raciones"),
    ("日本大赛第1战在10月24日（周六）", "Partido 1 de la Serie: 24 de octubre (sábado)"),
    ("第2战软银4-3获胜", "Partido 2: SoftBank ganó por 4–3"),
    ("神户灯光秀从7日开始", "La iluminación de Kobe empieza el día 7"),
    ("2连胜开局的夺冠率73%", "Tasa de título con un inicio 2–0: 73%"),
    ("气象厅预报气温高于往年", "La JMA prevé temperaturas por encima de la media"),
    ("美香周二和家人去金泽", "El martes Mika va a Kanazawa con su familia"),
    ("在金泽看传统工艺展和灯光秀", "En Kanazawa ve la exposición de artesanía y la iluminación"),
    ("周六和朋友去神户", "El sábado va a Kobe con amigos"),
    ("读书周想借2本书", "Quiere tomar prestados 2 libros para la Semana de la Lectura"),
    ("主语＋时间＋地点＋动词", "sujeto + tiempo + lugar + verbo"),
    ("场所用「で」", "usar 「で」 para el lugar"),
    ("2连胜开局", "empezar con dos victorias seguidas"),
    ("見頃＝最佳观赏期 b", "見頃 = mejor época para ver las hojas b"),
    ("鍋＝一锅菜 d", "鍋 = plato de olla d"),
    ("落葉＝落叶 a", "落葉 = hojas caídas a"),
    ("予算＝预算 c", "予算 = presupuesto c"),
    ("見せてください＝请出示", "見せてください = por favor, enseñe"),
    ("借りられます＝能借（可能形）", "借りられます = se puede tomar prestado (forma potencial)"),
    ("读书周到11月9日（第7版）", "La Semana de la Lectura dura hasta el 9 de noviembre (página 7)"),
    ("「紅葉の本」受欢迎", "「紅葉の本」 es popular"),
    ("どういたしまして＝不客气", "どういたしまして = de nada"),
    ("对照第3版", "Ver página 3"),
    ("对照第5版", "Ver página 5"),
    ("对照第7版", "Ver página 7"),
    ("对照第6版（神户的灯光秀）", "Ver página 6 (iluminación de Kobe)"),
]

# Per-file furniture / gloss / structural replacements.
PER_FILE = {
    "bslib4.py": [
        ('("译注｜" + s,', '("Nota — " + s,'),
        ('"Lucerna · 日语周报 VOL.2 · LUCERNA JAPANESE WEEKLY"',
         '"Lucerna · SEMANARIO JAPONÉS VOL.2 · TEXTO EN JAPONÉS · EXPLICACIONES EN ESPAÑOL"'),
        ('f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"'),
    ],
    "content12.py": [
        # P1 masthead -> W43 JA x ES shipped geometry
        ('p.text(975, 262, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")',
         'p.text(975, 248, "Lucerna", 168, family="UnifrakturMaguntia", anchor="middle")'),
        ('p.text(975, 330, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")',
         'p.text(975, 316, "日本語版 · VOL.2 · 文化の日 · 紅葉 · 読書週間", 40, "serif", True, INK, anchor="middle")\n'
         'p.text(975, 356, "TEXTOS EN JAPONÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 19, "sans", True, BRICK, anchor="middle")'),
        ('p.text(975, 372, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")',
         'p.text(975, 390, "日本語を学ぶ人のための週刊新聞 — 本物の日本を、日本語で", 19, "sans", False, GREY, anchor="middle")'),
        ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
         'p.hline(MX, RIGHT, 406, INK, 3); p.hline(MX, RIGHT, 413, INK, 1.2)'),
        ('"毎週、日本語で · 每周一期 · 日本人が読んでいる日本語を読む"',
         '"毎週、日本語で · Semanal · 日本人が読んでいる日本語を読む"'),
        ('"周二是文化日"', '"El martes es el Día de la Cultura"'),
        ('"节日过后，红叶周末到来 · 详见第 3 版"',
         '"Tras la fiesta llega el fin de semana de las hojas · Ver página 3"'),
        ('"トップニュース · 头条"', '"トップニュース · Titulares"'),
        ('"祝日 节假日 · 見頃 最佳观赏期 · 暦 历法 · お届けします 为您送上。"',
         '"祝日 día festivo · 見頃 mejor época para ver las hojas · 暦 calendario · お届けします para traértelo."'),
        ('"数字で見る今週 · 数字看本周"', '"数字で見る今週 · Semana en cifras"'),
        ('"今すぐ練習 · 即学即练"', '"今すぐ練習 · Práctica inmediata"'),
        ('"这四个话题，都是本期报纸的主题。"',
         '"Estos cuatro temas son los de este número."'),
        ('"来源与日期见各篇文章，非精确统计"',
         '"Fechas en los artículos; no son exactas"'),
        ('"この号の内容 · 本期目录"', '"この号の内容 · Contenido"'),
        ('"今週のことば · 本周单词"', '"今週のことば · Palabra de la semana"'),
        ('"ゆる＝ 轻松、不勉强。"', '"ゆる = relajado, sin forzarse."'),
        ('"短いニュース · 快讯"', '"短いニュース · Breves"'),
        ('"クイズ · 闪电问答"', '"クイズ · Quiz relámpago"'),
        ('"读头版，选出正确答案 · 答案见第 8 版"',
         '"Lee la portada y elige · Respuestas en la página 8"'),
        # P2
        ('"レベル A2 · ゆる整え食と暖かい11月 · 轻松食养与暖和的11月"',
         '"レベル A2 · ゆる整え食と暖かい11月 · Comida suave y un noviembre cálido"'),
        ('"蒸す 蒸 · 並ぶ 摆上货架 · 食卓 餐桌 · 超える 超过。"',
         '"蒸す cocer al vapor · 並ぶ aparecer en las tiendas · 食卓 la mesa · 超える superar."'),
        ('"予報 预报 · 平年 往年平均 · 季節風 季风 · 話題 话题 · 値上がり 涨价。"',
         '"予報 pronóstico · 平年 un año medio · 季節風 viento estacional · 話題 tema · 値上がり subida de precios."'),
        ('"你呢？寒冷的日子想吃什么锅？写两句日语寄来。"',
         '"¿Y tú? En un día frío, ¿qué olla te gustaría comer? Escríbenos dos frases en japonés."'),
        ('"季節のことば · 季节词语"', '"季節のことば · Palabras de la estación"'),
        ('"ゆる整え食の4つの言葉 · 关于轻松食养的四个词"',
         '"ゆる整え食の4つの言葉 · Cuatro palabras para comer con calma"'),
        ('"一锅菜"', '"un plato de olla"'),
        ('"蒸笼"', '"una vaporera"'),
        ('"轻松、不勉强"', '"relajado, sin forzarse"'),
        ('"调理、调养"', '"poner el cuerpo y la mente en orden"'),
        ('"練習 · 第 2 版练习"', '"練習 · Ejercicios de la página 2"'),
    ],
    "content34.py": [
        ('"レベル A2→B1 · 文化の日と金沢 · 文化日与金泽"',
         '"レベル A2→B1 · 文化の日と金沢 · El Día de la Cultura y Kanazawa"'),
        ('"市場 市场 · 工芸 工艺 · 光 灯光 · 楽しむ 享受。"',
         '"市場 mercado · 工芸 artesanía · 光 luz · 楽しむ disfrutar."'),
        ('"陶器 陶瓷 · 漆器 漆器 · 染物 染色织物 · 金箔 金箔。"',
         '"陶器 cerámica · 漆器 laca · 染物 textiles teñidos · 金箔 pan de oro."'),
        ('"你呢？文化日想去参加什么文化活动？写两句日语寄来。"',
         '"¿Y tú? ¿A qué actividad cultural te gustaría ir el Día de la Cultura? Escríbenos dos frases en japonés."'),
        ('"練習 · 第 3 版练习"', '"練習 · Ejercicios de la página 3"'),
        ('"レベル B1 · 日本シリーズ横浜の2試合 · 日本大赛横滨两场"',
         '"レベル B1 · 日本シリーズ横浜の2試合 · La Serie de Japón: dos partidos en Yokohama"'),
        ('"延長 延长赛 · 逆転 逆转 · 同点 平分 · 優勝率 夺冠率。"',
         '"延長 entradas extra · 逆転 remontada · 同点 empate · 優勝率 tasa de título."'),
        ('"総括 总结 · 締め切り 截稿 · 確認する 核实。"',
         '"総括 resumen · 締め切り cierre · 確認する confirmar."'),
        ('"日本シリーズの日程 · 大赛日程"', '"日本シリーズの日程 · Calendario"'),
        ('"横浜の2試合の記録 · 横滨两场比赛的记录"',
         '"横浜の2試合の記録 · Los dos partidos de Yokohama, en cifras"'),
        ('"練習 · 第 4 版练习"', '"練習 · Ejercicios de la página 4"'),
    ],
    "content56.py": [
        ('"若者・エンタメ · 青年"', '"若者・エンタメ · Juventud"'),
        ('"レベル B1 · ハロウィンと秋まつり · 万圣节与秋日祭典"',
         '"レベル B1 · ハロウィンと秋まつり · Halloween y fiestas de otoño"'),
        ('"罰金 罚款 · 像 雕像 · 仮装 变装 · 守る 遵守。"',
         '"罰金 multa · 像 estatua · 仮装 disfrazarse · 守る cumplir."'),
        ('"祭り 节日 · 週末 周末 · 話題 话题。"',
         '"祭り fiesta · 週末 fin de semana · 話題 tema."'),
        ('"你呢？秋日祭典上想做什么？写两句日语寄来。"',
         '"¿Y tú? ¿Qué te gustaría hacer en una fiesta de otoño? Escríbenos dos frases en japonés."'),
        ('"練習 · 第 5 版练习"', '"練習 · Ejercicios de la página 5"'),
        ('"レベル B2 · 暖かい11月と秋の旅 · 暖和的11月与秋日旅行"',
         '"レベル B2 · 暖かい11月と秋の旅 · Un noviembre cálido y viajes de otoño"'),
        ('"予算 预算 · 満足 满足 · 観測 观测 · 追いかける 追赶。"',
         '"予算 presupuesto · 満足 satisfacción · 観測 observación · 追いかける perseguir."'),
        ('"グラフを読もう · 读图表"', '"グラフを読もう · Leer el gráfico"'),
        ('"練習用データ · 练习数据"', '"練習用データ · Datos de práctica"'),
        ('"練習 · 第 6 版练习"', '"練習 · Ejercicios de la página 6"'),
    ],
    "content7.py": [
        ('"ことば · 语言"', '"ことば · Lengua"'),
        ('"言語フォーカス · 三つのレベル、三つのテーマ · 三个级别，三个主题"',
         '"言語フォーカス · 三つのレベル、三つのテーマ · Tres niveles, tres temas"'),
        ('"読書週間 读书周 · 紹介 介绍 · 読み聞かせ 朗读。"',
         '"読書週間 Semana de la Lectura · 紹介 presentación · 読み聞かせ lectura en voz alta."'),
        ('"見頃 最佳观赏期 · 紅葉狩り 看红叶出游 · 落葉 落叶"',
         '"見頃 mejor época para ver las hojas · 紅葉狩り salir a ver las hojas · 落葉 hojas caídas"'),
        ('"〜倍 倍 · 〜% 百分之〜 · 〜万食 万份。"',
         '"〜倍 veces · 〜% por ciento · 〜万食 decenas de millar de raciones."'),
        ('"まちがい診療所 · 易错诊所"', '"まちがい診療所 · Clínica de errores"'),
        ('"有「昨日」时要用过去式。"', '"Con 「昨日」, usa el pasado."'),
        ('"动词名词化时要加「こと」。"',
         '"Añade 「こと」 para sustantivar."'),
        ('"地点用「か所」来数。"', '"Cuenta los lugares con 「か所」."'),
        ('"动作发生的场所用「で」。"',
         '"Usa 「で」 para el lugar de la acción."'),
        ('"今週のフレーム · 本周句式"', '"今週のフレーム · Frase semanal"'),
        ('"句式拆解：轻松地调理身心。"',
         '"Desglose: poner el cuerpo y la mente en orden con calma."'),
        ('"読者の手紙 · 读者园地"', '"読者の手紙 · Cartas de lectores"'),
        # Readers' corner: the Japanese disclosure line (ld) must NOT
        # serve as the operative disclosure for Spanish readers, and
        # the Chinese disclosure (lcn) is the core's reader-native
        # layer. Both are replaced by ONE Spanish disclosure stating
        # the 3 facts + an explicit invitation.
        ('ld = "※この手紙は編集部の例です。締め切りまでに、本当の読者の手紙と第8版の作文の優秀作は届きませんでした。VOL.3に載せます。"',
         'ld_es = "Ejemplo de la redacción, no una carta real. Hasta la fecha '
         'límite no habían llegado cartas reales ni los mejores textos de '
         'la página 8; ambos aparecerán en el VOL.3. ¡Envíanos tu carta en '
         'japonés! Las seleccionadas saldrán en el VOL.3."'),
        ('lcn = "编辑部示例信，非真实来信。截至截稿，未收到真实来信与第8版最佳作文；VOL.3将刊登收到的来信与佳作。"\n',
         ''),
        ('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20.5, CW - 44)) * 29 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26 + 16',
         'lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld_es, "sans", False, 20, CW - 44)) * 29 + 26 + 16'),
        ('yy3 = p.para(bx + 22, yy3 + 20, ld, 20.5, "serif", False, GREY, CW - 44, 1.42) + 10\n'
         'p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)',
         'p.para(bx + 22, yy3 + 20, ld_es, 20, "sans", False, GREY, CW - 44, 1.42)'),
        ('"今週のフレーズ · 本周金句（逐字摘自本期文章）"',
         '"今週のフレーズ · Frases de la semana (citas textuales de este número)"'),
        ('"文化日是11月3日星期二。"', '"El Día de la Cultura es el 3 de noviembre, martes."'),
        ('"这是一个慢慢地、轻松调理的日本11月。"',
         '"Es un noviembre japonés lento y relajado, en orden."'),
        ('"所谓ゆる，就是不勉强、慢慢来的意思。"',
         '"«Yuru» significa no forzarse, ir despacio."'),
        ('"火锅食材提前一个月上架了。"',
         '"Los ingredientes para la olla aparecieron en las tiendas un mes antes."'),
        ('"可以同时欣赏传统工艺、红叶与灯光。"',
         '"Se pueden disfrutar juntos la artesanía tradicional, las hojas de otoño y las luces."'),
        ('"软银以两连胜开局。"', '"SoftBank empezó con dos victorias seguidas."'),
        ('"遵守规则，过一个快乐的万圣节吧。"',
         '"Respetemos las reglas y pasemos un Halloween divertido."'),
        ('"去看红叶的人可以自北向南追赶最佳观赏期。"',
         '"Quienes van a ver las hojas pueden seguir la mejor época de norte a sur."'),
        ('"第1面"', '"Página 1"'),
        ('"第2面"', '"Página 2"'),
        ('"第3面"', '"Página 3"'),
        ('"第4面"', '"Página 4"'),
        ('"第5面"', '"Página 5"'),
        ('"第6面"', '"Página 6"'),
        ('"来週 · 下期预告 (VOL.3)"', '"来週 · Próximo número (VOL.3)"'),
    ],
    "content8.py": [
        ('"テストと答え · 练习与答案"', '"テストと答え · Test y respuestas"'),
        # E zone re-aim JA<->ZH -> JA<->ES (W43 JA x ES pattern: keys
        # 137/138 re-aim to Spanish; 139/140 keep Japanese keys, only
        # their prompt sentences are printed in Spanish)
        ('"文化日是11月3日。"', '"El Día de la Cultura es el 3 de noviembre."'),
        ('"乱扔垃圾，要罚2,000日元。"', '"Tirar basura cuesta una multa de 2.000 yenes."'),
        ('"读书周从10月27日开始。→ ___"', '"La Semana de la Lectura empieza el 27 de octubre. → ___"'),
        ('"我想去神户看红叶灯光秀。→ ___"',
         '"Quiero ir a Kobe a ver la iluminación de las hojas de otoño. → ___"'),
        ('f"写作题（无唯一答案）；范文（{NCHARS} 字）见下。"',
         'f"Ejercicio de redacción (sin respuesta única); el modelo ({NCHARS} caracteres) va a continuación."'),
        ('"（开放题，范文如下）"', '"(pregunta abierta — modelo a continuación)"'),
        ('f"范文见本版 H 区（{NCHARS} 字）"',
         'f"El modelo está en la sección H de esta página ({NCHARS} caracteres)"'),
        ('"答え · 参考答案 — 按版面分页排列，找到题号即可"',
         '"答え · Respuestas — ordenadas por página, busca el número"'),
        ('"每题附一句中文简析 · 带 ✓ 的为范文题"',
         '"Una breve explicación en español por respuesta · ✓ = ejercicio con modelo"'),
        ('f"— 第{pg}面 —"', 'f"— PÁGINA {pg} —"'),
    ],
    "render.py": [
        ('"Lucerna-VOL2.pdf"', '"Lucerna-VOL2-ES.pdf"'),
        ('"Lucerna-VOL2-web.pdf"', '"Lucerna-VOL2-ES-web.pdf"'),
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
    prefixes/substrings of frozen Japanese stems and article sentences
    (e.g. note "2024年はDeNAが優勝しました" vs stem "...ました。";
    note "グラフは練習用データです" vs the frozen chart para), and a
    global replace corrupted frozen text in round 1 of the sibling build.
    Two scoped sites:
    (a) the 4th quoted argument of any .ex(...) call;
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
    # PER_FILE after NOTES because PER_FILE owns whole lines that share
    # words with notes (e.g. the season-word tuple "一锅菜" vs note
    # "鍋＝一锅菜"); GLOBAL last because it owns the P8 writing apparatus
    # neighbours only via PER_FILE lines.
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
