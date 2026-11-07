# -*- coding: utf-8 -*-
"""W45 EN core -> EN x ES fan-out transform.

Line/literal-based splicing only (never AST byte offsets). Every pair
asserts its occurrence count; the run aborts before writing anything if
any pair misses. Fix rounds append new pairs here and re-run from a
fresh copy of the core build (never hand-edit content files alone).
"""
import os, re, sys

BASE = os.path.dirname(os.path.abspath(__file__))
CORE_SVG = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-es-proof/baseline-ed/svg"
ED_SVG = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-es-proof/baseline-ed/svg"

# (filename, old, new, expected_count; None = replace-all, must occur >= 1)
R = [
    # ---- bslib4: footer + gloss prefix (W43 EN x ES furniture) ----
    ("bslib4.py", '"The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY"',
     '"The Lucerna · SEMANARIO INGLÉS VOL.2 · TEXTO EN INGLÉS · EXPLICACIONES EN ESPAÑOL"', 1),
    ("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de 8"', 1),
    ("bslib4.py", '("译注｜" + s, "sans", False, GREY, 20.5, 1.45)',
     '("Nota — " + s, "sans", False, GREY, 20.5, 1.45)', 1),
    # ---- type labels (registry only; never printed on the page) ----
    # Scoped with a trailing comma so bilingual section heads (which contain
    # the same word without a comma) are handled by their own full-string pairs.
    ("content12.py", '"完成句子", ', '"Completar frases", ', 11),
    ("content12.py", '"单选", ', '"Opción múltiple", ', 8),
    ("content12.py", '"句型转换", ', '"Reescribir", ', 4),
    ("content12.py", '"词汇配对",\n', '"Emparejar",\n', 1),
    ("content34.py", '"完成句子", ', '"Completar frases", ', 8),
    ("content34.py", '"单选", ', '"Opción múltiple", ', 12),
    ("content34.py", '"句型转换", ', '"Reescribir", ', 8),
    ("content34.py", '"词汇配对",\n', '"Emparejar",\n', 2),
    ("content56.py", '"完成句子", ', '"Completar frases", ', 10),
    ("content56.py", '"单选", ', '"Opción múltiple", ', 12),
    ("content56.py", '"句型转换", ', '"Reescribir", ', 4),
    ("content56.py", '"词汇配对",\n', '"Emparejar",\n', 1),
    ("content56.py", '"图表读数", ', '"Lectura de gráfico", ', 6),
    ("content7.py", '"跟练", ', '"Practicar", ', 1),
    ("content7.py", ', "改错", ', ', "Corregir", ', 4),
    ("content8.py", '"完形填空", ', '"Completar el texto", ', 1),
    ("content8.py", '"单选", ', '"Opción múltiple", ', 1),
    ("content8.py", '"阅读理解", ', '"Comprensión lectora", ', 1),
    ("content8.py", '"完成句子", ', '"Completar frases", ', 1),
    ("content8.py", '"翻译", ', '"Traducir", ', 1),
    ("content8.py", '"词汇配对",\n', '"Emparejar",\n', 1),
    ("content8.py", '"对话补全", ', '"Completar el diálogo", ', 1),
    ("content8.py", ', "写作", ', ', "Redacción", ', 1),
    # ---- instr labels (printed small grey after the number) ----
    ("content12.py", 'instr="填空"', 'instr="Completa"', None),
    ("content12.py", 'instr="改写"', 'instr="Reescribe"', None),
    ("content12.py", 'instr="把词和释义配对"', 'instr="Empareja"', None),
    ("content34.py", 'instr="填空"', 'instr="Completa"', None),
    ("content34.py", 'instr="改写"', 'instr="Reescribe"', None),
    ("content34.py", 'instr="把词和释义配对"', 'instr="Empareja"', None),
    ("content56.py", 'instr="填空"', 'instr="Completa"', None),
    ("content56.py", 'instr="改写"', 'instr="Reescribe"', None),
    ("content56.py", 'instr="把词和释义配对"', 'instr="Empareja"', None),
    ("content7.py", 'instr="改错"', 'instr="Corrige"', None),
    ("content8.py", 'instr="配对"', 'instr="Empareja"', None),
    # ---- shared instruction bridges ----
    ("content12.py", '"读第 2 版文章，选出正确答案。"', '"Lee el artículo de la página 2 y elige la respuesta correcta."', 1),
    ("content34.py", '"读第 3 版文章，选出正确答案。"', '"Lee el artículo de la página 3 y elige la respuesta correcta."', 1),
    ("content34.py", '"读第 4 版文章，选出正确答案。"', '"Lee el artículo de la página 4 y elige la respuesta correcta."', 1),
    ("content56.py", '"读第 5 版文章，选出正确答案。"', '"Lee el artículo de la página 5 y elige la respuesta correcta."', 1),
    ("content56.py", '"读第 6 版文章，选出正确答案。"', '"Lee el artículo de la página 6 y elige la respuesta correcta."', 1),
    ("content34.py", '"用所给词补全句子。"', '"Completa las frases con las palabras dadas."', 2),
    ("content56.py", '"用所给词补全句子。"', '"Completa las frases con las palabras dadas."', 2),
    ("content12.py", '"根据时间，用英语补全句子。"', '"Completa las frases en inglés según la hora."', 1),
    ("content12.py", '"用 be going to + 动词改写（计划与将要发生的事）。"', '"Reescribe con be going to + verbo (planes y cosas que van a pasar)."', 1),
    ("content34.py", '"用 be going to 改写。"', '"Reescribe con be going to."', 1),
    ("content34.py", '"用一般过去时改写（比赛已结束的说法）。"', '"Reescribe en pasado simple (los partidos ya terminaron)."', 1),
    ("content56.py", '"用现在进行时改写（正在发生的事）。"', '"Reescribe en presente continuo (lo que está pasando)."', 1),
    ("content56.py", '"读上面的教学图表，选出正确答案。"', '"Lee el gráfico didáctico de arriba y elige la respuesta correcta."', 1),
]

R += [
    # ================= P1 =================
    ("content12.py", '"WEEKLY IN ENGLISH · 每周一期 · 读美国人正在读的英语"',
     '"WEEKLY IN ENGLISH · UNA EDICIÓN CADA SEMANA · EL INGLÉS QUE LEE AMÉRICA"', 1),
    ("content12.py", '"英 语 周 报 · VOL.2 · 选 票 · 足 球 · 电 影"',
     '"SEMANARIO EN INGLÉS · VOL.2 · VOTOS · FÚTBOL · CINE"', 1),
    # badge replaces the strapline slot (W43 EN x ES geometry: y=372, 19.5pt bold brick)
    ("content12.py", 'p.text(975, 372, "THE LEARNERS\' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEXTOS EN INGLÉS · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 19.5, "sans", True, BRICK, anchor="middle")', 1),
    ("content12.py", '"周二选举日 · 周日已拨回时钟"', '"Martes electoral · Domingo con relojes atrasados"', 1),
    ("content12.py", '"11 月 3 日周二选举日 · 详见第 6 版"', '"Día de elecciones, 3 de noviembre · Página 6"', 1),
    ("content12.py", '"THE BIG STORY · 头条"', '"THE BIG STORY · Titular"', 1),
    ("content12.py", '"讲解｜a midterm 中期选举 · a ballot 选票 · a race 一场竞选 · to call a race 宣布某场竞选的结果。"',
     '"a midterm: elecciones de mitad de mandato · a ballot: papeleta · a race: una contienda · to call a race: anunciar el resultado de una contienda."', 1),
    ("content12.py", '"THE WEEK IN NUMBERS · 数字看本周"', '"THE WEEK IN NUMBERS · En cifras"', 1),
    ("content12.py", '"Nov 3 — Election Day（选举日） · 435 — seats in the House, all on the ballot（众议院全部席位改选）"',
     '"Nov 3 — Election Day (día de elecciones) · 435 — seats in the House, all on the ballot (todos los escaños de la Cámara se renuevan)"', 1),
    ("content12.py", '"Nov 6 — two films open（两部电影上映） · Nov 8 — NFL in Madrid + F1 in São Paulo（周日两场大赛）"',
     '"Nov 6 — two films open (dos estrenos) · Nov 8 — NFL in Madrid + F1 in São Paulo (dos grandes citas el domingo)"', 1),
    ("content12.py", '"TRY IT NOW · 即学即练"', '"TRY IT NOW · Practica al momento"', 1),
    ("content12.py", '"ballot = 纸选票"', '"ballot = papeleta"', 1),
    ("content12.py", '"midterm = 中期（选举）"', '"midterm = de mitad de mandato"', 1),
    ("content12.py", '"选举日 11 月 3 日（周二）"', '"día de elecciones, martes 3 de noviembre"', 1),
    ("content12.py", '"early voting = 提前投票"', '"early voting = votación anticipada"', 1),
    ("content12.py", '"race called = 宣布结果"', '"race called = resultado anunciado"', 1),
    ("content12.py", '"take time = 花时间"', '"take time = llevar tiempo"', 1),
    ("content12.py", '"本周美国热搜 · Google Trends 美国区快照"', '"Lo más buscado · Google Trends EE. UU."', 1),
    ("content12.py", '"相对热度示意，非精确搜索量。"', '"Interés relativo orientativo, no cifras exactas."', 1),
    ("content12.py", '"IN THIS ISSUE · 本期目录"', '"IN THIS ISSUE · En esta edición"', 1),
    ("content12.py", '"（任期）中期。midterm election 中期选举。"', '"A mitad de mandato: midterm election."', 1),
    ("content12.py", '"IN BRIEF · 快讯"', '"IN BRIEF · En breve"', 1),
    ("content12.py", '"LIGHTNING QUIZ · 闪电问答"', '"LIGHTNING QUIZ · Quiz relámpago"', 1),
    ("content12.py", '"读头版，选出正确答案 · 答案见第 8 版"', '"Lee la portada y elige la respuesta correcta · Respuestas en la página 8"', 1),
    ("content12.py", '"选举日 11 月 3 日周二"', '"día de elecciones, martes 3 de noviembre"', 1),
    ("content12.py", '"众议院 435 席全部改选"', '"los 435 escaños de la Cámara se renuevan"', 1),
    ("content12.py", '"美国 11 月 1 日拨回时钟"', '"EE. UU. atrasó los relojes el 1 de noviembre"', 1),
    ("content12.py", '"NFL 马德里赛 11 月 8 日周日"', '"el partido de la NFL en Madrid, domingo 8 de noviembre"', 1),
    # ================= P2 =================
    ("content12.py", 'p.band("LIFE · 生活", "The Lucerna", "LEVEL A2 · Clocks, candy & your week · 时钟、糖果与你的一周")',
     'p.band("LIFE · Vida", "The Lucerna", "LEVEL A2 · Clocks, candy & your week · Relojes, dulces y tu semana")', 1),
    ("content12.py", '"DO THE MATHS · 算一算"', '"DO THE MATHS · Calcula"', 1),
    ("content12.py", '"讲解｜to fall back （时钟）拨回 · a costume 服装、装扮 · trick or treat 不给糖就捣蛋。"',
     '"to fall back (reloj) atrasar · a costume un disfraz · trick or treat truco o trato."', 1),
    ("content12.py", '"周日你多睡了一小时吗？写两句英语寄给编辑部。"', '"¿Dormiste una hora más el domingo? Escríbenos dos frases en inglés."', 2),
    ("content12.py", '"AND YOU ? · 说说你自己"', '"AND YOU ? · ¿Y tú?"', 1),
    ("content12.py", '"TELLING THE TIME · 这样报时间"', '"TELLING THE TIME · Decir la hora"', 1),
    ("content12.py", '"The repeated hour · 本周的三个时间"', '"The repeated hour · Las tres horas de la semana"', 1),
    ("content12.py", '"= two times（两次）"', '"= two times (dos veces)"', 1),
    ("content12.py", '"= one more time（再一次）"', '"= one more time (una vez más)"', 1),
    ("content12.py", '"= to go back one hour（拨回）"', '"= to go back one hour (atrasar)"', 1),
    ("content12.py", '"= one hour more（多出一小时）"', '"= one hour more (una hora más)"', 1),
    ("content12.py", '"EXERCISES · 第 2 版练习"', '"EXERCISES · Ejercicios de la página 2"', 1),
    ("content12.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Respuestas en la página 8 · Los ejercicios mezclan niveles; busca por número"', 1),
    ("content12.py", '"1:00 = 一点整"', '"1:00 = la una en punto"', 1),
    ("content12.py", '"1:30 = 一点半"', '"1:30 = la una y media"', 1),
    ("content12.py", '"7:45 = 差一刻八点"', '"7:45 = las ocho menos cuarto"', 1),
    ("content12.py", '"两次 = twice"', '"dos veces = twice"', 1),
    ("content12.py", '"多出的 = extra"', '"de más = extra"', 1),
    ("content12.py", '"Americans 复数 → are going to"', '"Americans, plural → are going to"', 1),
    ("content12.py", '"疑问句：be 提前"', '"pregunta: be al principio"', 1),
    ("content34.py", '"疑问句：be 提前"', '"pregunta: be al principio"', 1),
    ("content12.py", '"11 月 1 日凌晨 2 点拨回 1 点"', '"el 1 de noviembre, de las 2 a la 1"', 1),
    ("content12.py", '"亚利桑那与夏威夷不拨钟"', '"Arizona y Hawái no cambian la hora"', 1),
    ("content12.py", '"万圣节 10 月 31 日周六"', '"Halloween, sábado 31 de octubre"', 1),
    ("content12.py", '"11 月 1 日夜晚有 25 小时"', '"la noche del 1 de noviembre tiene 25 horas"', 1),
    ("content12.py", '"costume=装扮 b"', '"costume=un disfraz b"', 1),
    ("content12.py", '"extra hour=多出一小时 a"', '"extra hour=una hora más a"', 1),
    ("content12.py", '"fall back=拨回 d"', '"fall back=atrasar d"', 1),
    ("content12.py", '"trick or treat=不给糖就捣蛋 c"', '"trick or treat=truco o trato c"', 1),
]

R += [
    # ================= P3 =================
    ("content34.py", 'p.band("CULTURE · 文化", "The Lucerna", "A2 → B1 · Friday at the movies · 周五看电影")',
     'p.band("CULTURE · Cultura", "The Lucerna", "A2 → B1 · Friday at the movies · El viernes, al cine")', 1),
    ("content34.py", '"AT HOME THIS WEEK · 在家看什么"', '"AT HOME THIS WEEK · En casa"', 1),
    ("content34.py", '"讲解｜to open （电影）上映 · a monster 怪物 · a catchphrase 口头禅、金句 · a series 剧集。"',
     '"to open (cine) estrenarse · a monster un monstruo · a catchphrase una frase célebre · a series una serie."', 1),
    ("content34.py", '"猫咪电影 11 月 6 日周五上映"', '"la película del Gato se estrena el viernes 6 de noviembre"', 1),
    ("content34.py", '"猫出自苏斯博士的书"', '"el Gato sale de un libro del Dr. Seuss"', 1),
    ("content34.py", '"比尔·黑德为猫配音"', '"Bill Hader pone la voz del Gato"', 1),
    ("content34.py", '"哥斯拉导演是山崎贵"', '"el director de Godzilla es Takashi Yamazaki"', 1),
    ("content34.py", '"《黑鸽》第二季 11 月 5 日上线"', '"la segunda temporada de Black Doves llega el 5 de noviembre"', 1),
    ("content34.py", '"周日重聚节目收尾"', '"el reencuentro del domingo cierra la semana"', 1),
    ("content34.py", '"open = 上映（第三人称单数加 s）"', '"open = estrenarse (tercera persona singular con s)"', 1),
    ("content34.py", '"tall → taller 比较级"', '"tall → taller, comparativo"', 1),
    ("content34.py", '"loud → louder"', '"loud → louder"', 1),
    ("content34.py", '"split = 分歧的"', '"split = dividida"', 1),
    ("content34.py", '"monster=怪物 b"', '"monster=un monstruo b"', 1),
    ("content34.py", '"catchphrase=金句 a"', '"catchphrase=una frase célebre a"', 1),
    ("content34.py", '"series=剧集 d"', '"series=una serie d"', 1),
    ("content34.py", '"open=上映 c"', '"open=estrenarse c"', 1),
    ("content34.py", '"THE CAT\'S HAT · 猫的帽子"', '"THE CAT\'S HAT · El sombrero"', 1),
    ("content34.py", '"五句影评｜who、where、发生了什么、转折、结局——五句就够。"',
     '"Cinco frases de crítica: quién, dónde, qué pasó, el giro y el final; con cinco basta."', 1),
    # ================= P4 =================
    ("content34.py", 'p.band("SPORT · 体育", "The Lucerna", "LEVEL B1 · NFL · F1 · NASCAR · WTA · Boxing")',
     'p.band("SPORT · Deportes", "The Lucerna", "LEVEL B1 · NFL · F1 · NASCAR · WTA · Boxing")', 1),
    ("content34.py", '"WHY MADRID ? · 为什么去马德里？"', '"WHY MADRID ? · ¿Por qué Madrid?"', 1),
    ("content34.py", '"讲解｜a fixture 一场比赛（赛程） · a title 冠军头衔 · to defend （卫冕）保卫头衔 · a fan 球迷。"',
     '"a fixture un partido del calendario · a title un título · to defend (campeón) defender el título · a fan un aficionado."', 1),
    ("content34.py", '"马德里赛：孟加拉虎对猎鹰"', '"Madrid: Bengals contra Falcons"', 1),
    ("content34.py", '"马德里赛场是伯纳乌"', '"el estadio de Madrid es el Bernabéu"', 1),
    ("content34.py", '"海豚对雄狮在迈阿密"', '"Dolphins contra Lions en Miami"', 1),
    ("content34.py", '"F1 圣保罗大奖赛在巴西"', '"el Gran Premio de São Paulo de F1, en Brasil"', 1),
    ("content34.py", '"WTA 年终总决赛在印第安维尔斯开赛"', '"las Finales de la WTA empiezan en Indian Wells"', 1),
    ("content34.py", '"拳击赛在阿灵顿"', '"el boxeo, en Arlington"', 1),
    ("content34.py", '"defend 三单加 s"', '"defend, tercera persona singular con s"', 1),
    ("content34.py", '"与第 4 版原文一致，复数动词"', '"como en el artículo de la página 4, verbo en plural"', 1),
    ("content34.py", '"big → bigger"', '"big → bigger"', 1),
    ("content34.py", '"fast → faster"', '"fast → faster"', 1),
    ("content34.py", '"fixture=赛程中的比赛 b"', '"fixture=un partido del calendario b"', 1),
    ("content34.py", '"title=冠军头衔 d"', '"title=un título d"', 1),
    ("content34.py", '"fan=球迷 a"', '"fan=un aficionado a"', 1),
    ("content34.py", '"defend=卫冕 c"', '"defend=defender el título c"', 1),
    ("content34.py", '"play → played"', '"play → played"', 1),
    ("content34.py", '"watch → watched"', '"watch → watched"', 1),
    ("content34.py", '"follow → followed"', '"follow → followed"', 1),
    ("content34.py", '"choose → chose"', '"choose → chose"', 1),
    ("content34.py", '"SUNDAY, NOVEMBER 8 · 周日赛程"', '"SUNDAY, NOVEMBER 8 · Domingo"', 1),
    ("content34.py", '"看球英语｜比分、谁得分、谁领先——短句就是直播英语。"',
     '"Inglés de partido: el marcador, quién marca, quién va por delante; frases cortas, como en directo."', 1),
    # ================= P5 =================
    ("content56.py", 'p.band("YOUTH · 青年", "The Lucerna", "LEVEL B1 · Election night at home · 选举之夜")',
     'p.band("YOUTH · Jóvenes", "The Lucerna", "LEVEL B1 · Election night at home · Noche electoral en casa")', 1),
    ("content56.py", '"TOO CLOSE TO CALL · 难分胜负"', '"TOO CLOSE TO CALL · Muy reñido"', 1),
    ("content56.py", '"讲解｜a map （选举）地图 · too close to call 难分胜负、无法判定 · a second screen 第二块屏幕（手机）。"',
     '"a map (elecciones) un mapa · too close to call demasiado reñido, sin decidir · a second screen una segunda pantalla (el móvil)."', 1),
    ("content56.py", '"地图随结果逐州变色"', '"el mapa cambia de color estado a estado"', 1),
    ("content56.py", '"too close to call = 尚不知晓"', '"too close to call = aún no se sabe"', 1),
    ("content56.py", '"选举夜常吃披萨"', '"en la noche electoral se suele comer pizza"', 1),
    ("content56.py", '"第二屏是手机"', '"la segunda pantalla es el móvil"', 1),
    ("content56.py", '"孩子问为什么这么久"', '"los niños preguntan por qué tarda tanto"', 1),
    ("content56.py", '"结果早上还在"', '"los resultados siguen ahí por la mañana"', 1),
    ("content56.py", '"close = 接近的"', '"close = reñido"', 1),
    ("content56.py", '"still = 仍然"', '"still = todavía"', 1),
    ("content56.py", '"与第 5 版原文一致，单数"', '"como en el artículo de la página 5, en singular"', 2),
    ("content56.py", '"map=选举地图 c"', '"map=un mapa electoral c"', 1),
    ("content56.py", '"race=一场竞选 d"', '"race=una contienda d"', 1),
    ("content56.py", '"result=结果 b"', '"result=un resultado b"', 1),
    ("content56.py", '"call=宣布胜者 a"', '"call=anunciar al ganador a"', 1),
    ("content56.py", '"change → is changing"', '"change → is changing"', 1),
    ("content56.py", '"send → are sending"', '"send → are sending"', 1),
    ("content56.py", '"watch → are watching"', '"watch → are watching"', 1),
    ("content56.py", '"wait → is waiting"', '"wait → is waiting"', 1),
    ("content56.py", '"FIVE SENTENCES · 五句话作业"', '"FIVE SENTENCES · Cinco frases"', 1),
    ("content56.py", '"投票结束｜The polls have closed = 该州投票已结束，计票开始。"',
     '"Cierre de urnas: The polls have closed = en ese estado ya se ha votado y empieza el recuento."', 1),
    # ================= P6 =================
    ("content56.py", 'p.band("DEEP READ · 时事深读", "The Lucerna", "LEVEL B2 · How America votes · 美国怎么投票")',
     'p.band("DEEP READ · Lectura a fondo", "The Lucerna", "LEVEL B2 · How America votes · Cómo vota Estados Unidos")', 1),
    ("content56.py", '"A PRACTICE BALLOT · 模拟选票"', '"A PRACTICE BALLOT · Papeleta"', 1),
    ("content56.py", '"讲解｜to register 登记（选民登记） · a governor 州长 · to shape laws 影响立法 · patience 耐心。"',
     '"to register inscribirse (registro de votantes) · a governor un gobernador · to shape laws influir en las leyes · patience paciencia."', 1),
    ("content56.py", '"READ THE CHART · 读图表"', '"READ THE CHART · Lee el gráfico"', 1),
    ("content56.py", '"38% 选“不用排队”"', '"el 38% elige «no hacer cola»"', 1),
    ("content56.py", '"工作原因 29%"', '"el trabajo, 29%"', 1),
    ("content56.py", '"四项合计 100%"', '"los cuatro suman 100%"', 1),
    ("content56.py", '"习惯最少 12%"', '"la costumbre, solo 12%"', 1),
    ("content56.py", '"不用排队比旅行多 17 个百分点"', '"«no hacer cola» supera a «viajes» por 17 puntos"', 1),
    ("content56.py", '"图表是教学数据非真实民调"', '"el gráfico es material didáctico, no una encuesta real"', 1),
    ("content56.py", '"各州自行组织选举"', '"cada estado organiza sus elecciones"', 1),
    ("content56.py", '"众议员任期两年"', '"los diputados sirven dos años"', 1),
    ("content56.py", '"参议员任期六年、每次约三分之一改选"', '"los senadores sirven seis años; cerca de un tercio se renueva cada vez"', 1),
    ("content56.py", '"邮寄选票计票需时间"', '"contar los votos por correo lleva tiempo"', 1),
    ("content56.py", '"本期不印民调与预测"', '"este número no publica encuestas ni predicciones"', 1),
    ("content56.py", '"耐心是制度的一部分"', '"la paciencia es parte del sistema"', 1),
    ("content56.py", '"shape = 影响、塑造"', '"shape = influir, dar forma"', 1),
    ("content56.py", '"register = 登记"', '"register = inscribirse"', 1),
    ("content56.py", '"patience = 耐心"', '"patience = paciencia"', 1),
    ("content56.py", '"optional = 可选的"', '"optional = opcional"', 1),
    ("content56.py", '"differ 三单 differs"', '"differ, tercera persona singular: differs"', 1),
    ("content56.py", '"private = 私密的"', '"private = en privado"', 1),
    ("content56.py", '"HOW LONG ? · 任期多长？"', '"HOW LONG ? · El mandato"', 1),
    ("content56.py", '"一张地图｜五十个州、五十套规则——所以选举夜看的是地图，不是一个数字。"',
     '"Un mapa: cincuenta estados, cincuenta reglas; por eso la noche electoral se ve en un mapa, no en un solo número."', 1),
]

R += [
    # ================= P7 =================
    ("content7.py", 'p.band("LANGUAGE IN HAND · 精讲", "The Lucerna", "A2 → B2 · Phrases of the week · 本周金句")',
     'p.band("LANGUAGE IN HAND · A fondo", "The Lucerna", "A2 → B2 · Phrases of the week · Frases de la semana")', 1),
    ("content7.py", '"LEVEL A2 · 基础"', '"LEVEL A2 · Base"', 1),
    ("content7.py", '"LEVEL B1 · 进阶"', '"LEVEL B1 · Intermedio"', 1),
    ("content7.py", '"LEVEL B2 · 挑战"', '"LEVEL B2 · Desafío"', 1),
    ("content7.py", '"THE EXAMPLE · 例句"', '"THE EXAMPLE · El ejemplo"', 3),
    # B2 example box: quoted English sentence verbatim; only the gloss localised.
    ("content7.py", '"« Patience is part of the system, not a failure of it. » — part of = 一部分 (page 6)."',
     '"« Patience is part of the system, not a failure of it. » — part of = una parte (page 6)."', 1),
    ("content7.py", '"THE TOOLBOX · 工具箱"', '"THE TOOLBOX · Herramientas"', 1),
    ("content7.py", '"工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。"',
     '"Tres frases de bolsillo, una por nivel; todas las frases de la semana salen de los artículos de este número: relee el original y resultan fáciles."', 1),
    ("content7.py", '"PHRASES OF THE WEEK · 本周金句（全部出自本期文章）"', '"PHRASES OF THE WEEK · Frases de la semana"', 1),
    ("content7.py", '"每句一个语法点 + 一道小题 · 答案见第 8 版"', '"Cada frase: un punto de gramática y una pregunta · Respuestas en la página 8"', 1),
    # phrase grammar points: W43 EN x ES phrase slot renders them with the Nota prefix
    ("content7.py", '"语法点｜is = 是；日期作主语补足语。"', '"Nota — is = es; la fecha es el atributo del sujeto."', 1),
    ("content7.py", '"语法点｜happen 的过去式是 happened，规则变化。"', '"Nota — el pasado de happen es happened, forma regular."', 1),
    ("content7.py", '"语法点｜would + 动词原形，表选择意愿。"', '"Nota — would + verbo en infinitivo, para expresar preferencia."', 1),
    ("content7.py", '"语法点｜that is = 那就是；破折号后总结。"', '"Nota — that is = es decir; resume tras la raya."', 1),
    ("content7.py", '"语法点｜will still = 仍然会；still 放在 will 之后。"', '"Nota — will still = todavía; still va después de will."', 1),
    ("content7.py", '"语法点｜part of = ……的一部分；not 表否定对照。"', '"Nota — part of = parte de; not marca el contraste."', 1),
    ("content7.py", '"语法点｜not every + 单数动词：并非每处都变。"', '"Nota — not every + verbo en singular: no todo cambia."', 1),
    ("content7.py", '"语法点｜has = 有；the week 单数用 has。"', '"Nota — has = tiene; the week, en singular, lleva has."', 1),
    ("content7.py", '"is 是"', '"is = es"', 1),
    ("content7.py", '"would + 原形"', '"would + infinitivo"', 1),
    ("content7.py", '"that is 那就是"', '"that is = es decir"', 1),
    ("content7.py", '"will still 仍然会"', '"will still = todavía"', 1),
    ("content7.py", '"is part of 一部分"', '"is part of = parte de"', 1),
    ("content7.py", '"THE ERROR CLINIC · 易错诊所"', '"THE ERROR CLINIC · Errores"', 1),
    ("content7.py", '"每句有一处错误：找出来并改正。"', '"Cada frase tiene un error: búscalo y corrígelo."', 1),
    ("content7.py", '"三单否定用 doesn\'t + 原形"', '"la negación en tercera persona usa doesn\'t + infinitivo"', 1),
    ("content7.py", '"fall 的过去式是 fell"', '"el pasado de fall es fell"', 1),
    ("content7.py", '"bigger 已含比较级，不要再加 more"', '"bigger ya es comparativo: no añadas more"', 1),
    ("content7.py", '"going to 后用动词原形"', '"después de going to va el infinitivo"', 1),
    ("content7.py", '"READERS\' CORNER · 读者园地"', '"READERS\' CORNER · Rincón de los lectores"', 1),
    # Readers' corner: the English letter paragraph is FROZEN verbatim (core's own
    # honestly-labelled example). Only the Chinese disclosure paragraph is localised:
    # it states the 3 facts (no real letters / no best VOL.1 p.8 text / example +
    # promise deferred to VOL.3) plus an explicit imperative invitation.
    ("content7.py", '"编辑说明｜VOL.1 曾承诺 VOL.2 刊登真实来信，但截至发稿编辑部未收到真实来信与 VOL.1 写作投稿，故本期如实说明、不虚构来信；请把你的来信与写作寄来，VOL.3 起刊登收到的真实来信。"',
     '"Nota de la redacción: VOL.1 prometió cartas reales en VOL.2, pero no llegó ninguna carta ni el mejor texto de la página 8 de VOL.1; no inventamos nada y el ejemplo sigue marcado. ¡Envíanos tu carta y tu texto! En VOL.3 publicaremos las cartas recibidas."', 1),
    ("content7.py", '"NEXT WEEK · VOL.3 下周预告"', '"NEXT WEEK · VOL.3 · Avance"', 1),
    ("content7.py", '"下周三退伍军人节，周日 NFL 慕尼黑赛；还有中期选举结果报道。"',
     '"El miércoles, Día de los Veteranos; el domingo, la NFL en Múnich; y los resultados de las elecciones de mitad de mandato."', 1),
    # ================= P8 =================
    ("content8.py", 'p.band("EXERCISES & ANSWERS · 练习与答案", "The Lucerna", "FINAL TEST · 综合评估 · Answers at the bottom of this page 答案在本版下方")',
     'p.band("EXERCISES & ANSWERS · Ejercicios y respuestas", "The Lucerna", "FINAL TEST · Evaluación final · Answers at the bottom of this page · Las respuestas están al final de esta página")', 1),
    ("content8.py", '"11 月 3 日是周二"', '"el 3 de noviembre es martes"', 1),
    ("content8.py", '"pizza 披萨"', '"pizza"', 1),
    ("content8.py", '"map 地图逐州变色"', '"el mapa cambia estado a estado"', 1),
    ("content8.py", '"close 接近的"', '"close = reñido"', 1),
    ("content8.py", '"sticker 贴纸"', '"sticker = pegatina"', 1),
    ("content8.py", '"will + 动词原形 know"', '"will + infinitivo: know"', 1),
    ("content8.py", '"still 仍然"', '"still = todavía"', 1),
    ("content8.py", '"选项："', '"Opciones:"', 1),
    ("content8.py", '"A · CLOZE · 完形填空"', '"A · CLOZE · Completa el texto"', 1),
    # P8 heads use the W43 EN x ES short forms (round-1 long forms tripped
    # HEAD TOO WIDE at 24pt bold in a 434px column; W43 forms fit).
    ("content8.py", '"B · MULTIPLE CHOICE · 单选"', '"B · MULTIPLE CHOICE · Opción"', 1),
    ("content8.py", '"C · READING · 阅读理解"', '"C · READING · Comprensión"', 1),
    ("content8.py", '"D · SENTENCES · 完成句子与转换"', '"D · SENTENCES · A completar"', 1),
    ("content8.py", '"E · TRANSLATION · 翻译"', '"E · TRANSLATION · Traducción"', 1),
    ("content8.py", '"F · WORDS · 词汇配对"', '"F · WORDS · Empareja"', 1),
    ("content8.py", '"G · DIALOGUE · 对话补全"', '"G · DIALOGUE · El diálogo"', 1),
    ("content8.py", '"H · WRITING · 写作 [B1]"', '"H · WRITING · Escritura [B1]"', 1),
    ("content8.py", '"we → get 原形"', '"we → get, infinitivo"', 1),
    ("content8.py", '"已发生的事用 fell"', '"lo ya ocurrido usa fell"', 1),
    ("content8.py", '"than → 比较级 bigger"', '"than → comparativo: bigger"', 1),
    ("content8.py", '"despite + 名词：尽管下雨"', '"despite + sustantivo: a pesar de la lluvia"', 1),
    ("content8.py", '"whether = 是否"', '"whether = si"', 1),
    ("content8.py", '"将来时 will + 动词原形"', '"futuro: will + infinitivo"', 1),
    ("content8.py", '"be going to + 原形 vote"', '"be going to + infinitivo: vote"', 1),
    ("content8.py", '"too close to call = 难分胜负"', '"too close to call = aún no se sabe"', 1),
    ("content8.py", '"原文：a teacher from Ohio"', '"en el texto: a teacher from Ohio"', 1),
    ("content8.py", '"周二他全天教书"', '"el martes enseña todo el día"', 1),
    ("content8.py", '"贴纸上写着 I VOTED"', '"en la pegatina pone I VOTED"', 1),
    ("content8.py", '"俄亥俄一如既往难分胜负"', '"Ohio, como siempre, demasiado reñido"', 1),
    ("content8.py", '"are going to + 原形"', '"are going to + infinitivo"', 1),
    ("content8.py", '"fall → fell（不规则变化）"', '"fall → fell, irregular"', 1),
    ("content8.py", '"tall → taller（比较级）"', '"tall → taller, comparativo"', 1),
    ("content8.py", '"whether 引导“是否”从句"', '"whether introduce una subordinada con «si»"', 1),
    # E translation items: core keys are reader-language translations of English
    # sentences; 137/140 carry an English instruction, 138/139 a native one.
    # ES mirrors that split: Translate / Traduce, keys in Spanish.
    ("content8.py", '"耐心是制度的一部分，而不是制度的失败。"', '"La paciencia es parte del sistema, no un fallo del sistema."', 1),
    ("content8.py", '"part of 一部分；not a failure 不是失败"', '"part of = parte de; not a failure = no un fallo"', 1),
    ("content8.py", '"11 月 3 日周二是美国的选举日。"', '"El martes 3 de noviembre es el día de las elecciones en Estados Unidos."', 1),
    ("content8.py", '"Election Day 选举日；on Tuesday"', '"Election Day = día de elecciones; on Tuesday"', 1),
    ("content8.py", '"翻译：Tuesday, November 3, is Election Day in the United States."',
     '"Traduce: Tuesday, November 3, is Election Day in the United States."', 1),
    ("content8.py", '"这周日，NFL 在马德里比赛。"', '"El domingo, la NFL juega en Madrid."', 1),
    ("content8.py", '"on Sunday；in Madrid"', '"on Sunday; in Madrid"', 1),
    ("content8.py", '"翻译：On Sunday, the NFL plays in Madrid."', '"Traduce: On Sunday, the NFL plays in Madrid."', 1),
    ("content8.py", '"并非每处都拨回时钟。"', '"No todos los lugares cambian."', 1),
    ("content8.py", '"not every 并非每处；change 变化"', '"not every = no todo; change = cambiar"', 1),
    ("content8.py", '"midterm = 中期选举 b"', '"midterm = elecciones de mitad de mandato b"', 1),
    ("content8.py", '"governor = 州长 c"', '"governor = gobernador c"', 1),
    ("content8.py", '"ballot = 选票 d"', '"ballot = papeleta d"', 1),
    ("content8.py", '"turnout = 投票率 a"', '"turnout = participación a"', 1),
    ("content8.py", '"投票时出示证件 ID"', '"enseña tu documento de identidad al votar"', 1),
    ("content8.py", '"line = 排队（美式英语）"', '"line = cola, inglés americano"', 1),
    ("content8.py", '"ballot = 选票"', '"ballot = papeleta"', 1),
    ("content8.py", '"sticker = 贴纸"', '"sticker = pegatina"', 1),
    ("content8.py", '"选举日是 11 月 3 日周二"', '"el día de elecciones es el martes 3 de noviembre"', 1),
    # writing item 150: key is explanation-layer text, not frozen English.
    ("content8.py", '"开放题 — 要点见写作框，范文在第 8 版写作框内"', '"Pregunta abierta: véanse los puntos en el recuadro de redacción; el modelo está en el recuadro de esta página"', 1),
    ("content8.py", '"按要点给分"', '"Se puntúa por puntos"', 1),
    ("content8.py", '"MODEL · 范文"', '"MODEL · Modelo"', 1),
    ("content8.py", '"用英语写 80–100 词：我的 11 月 3 日周二。写清你是否看了结果、吃了什么、地图显示了什么，再写一句周日夜里拨回的时钟。"',
     '"Escribe en inglés de 80 a 100 palabras: tu martes 3 de noviembre. Di si viste los resultados, qué comiste, qué mostró el mapa, y una frase sobre los relojes atrasados el domingo por la noche."', 1),
    ("content8.py", '"ANSWERS · 全部答案与简析（第 1–8 版）"', '"ANSWERS · Respuestas y notas (páginas 1–8)"', 1),
    # P8 key block: W43 EN x ES family uses half-width parens (core: full-width).
    ("content8.py", 'kf.para(f"— 第 {pg} 版 —", 17, "sans", True, OLIVE, 1.28, 3)',
     'kf.para(f"— Página {pg} —", 17, "sans", True, OLIVE, 1.28, 3)', 1),
    ("content8.py", 's += f"（{e[\'note\']}）"', 's += f" ({e[\'note\']})"', 1),
    # Printed-note set must equal the core's exactly (78). Spanish notes are
    # longer than the Chinese notes the len<=10 rule was calibrated for, so
    # the set is pinned explicitly (W43 EN x ES NOTAS_EXTRA precedent).
    ("content8.py", 'if e["note"] and (pg == 8 or len(e["note"]) <= 10 or e["type"] in ("改错", "图表读数")):',
     'NOTAS_EXTRA = {11, 12, 14, 19, 29, 30, 31, 33, 41, 44, 47, 48, 51, 58, 64, 66, 67, 68, 69, 71, 74, 82, 83, 84, 85, 86, 87, 88, 89, 91, 92, 93, 100, 102, 107, 108, 109, 110, 111}\n        if e["note"] and (pg == 8 or e["n"] in NOTAS_EXTRA):', 1),
]

R += [
    # ---- fix round 3 (geometry audit, run after the base pairs) ----
    # P2 AND YOU box: the audit measured the last line's ink 0.6px below the
    # computed box bottom; grow the box tail 20 -> 24 (box is last in col 3,
    # nothing below it before the fixed y=1570 section).
    ("content12.py", 'eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("¿Dormiste una hora más el domingo? Escríbenos dos frases en inglés.", "sans", False, 20, CW - 44)) * 29 + 20',
     'eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("¿Dormiste una hora más el domingo? Escríbenos dos frases en inglés.", "sans", False, 20, CW - 44)) * 29 + 24', 1),
    # P8 battery: "Traduce:" is longer than the core's native instruction, so
    # E item 139 wraps to 2 lines (core: 1) and pushes the Levels line onto
    # the writing-strip rule. Recover 28px by tightening the four E gaps
    # 11 -> 4 (Levels baseline 1485 -> ~1457, rule at 1486 clears).
    ("content8.py", 'bf.ex(lv, "Traducir", k, nt, body, size=20.5)',
     'bf.ex(lv, "Traducir", k, nt, body, size=20.5, gap=4)', 1),
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
