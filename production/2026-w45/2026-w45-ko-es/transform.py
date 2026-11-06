# -*- coding: utf-8 -*-
"""KOxES W45 fan-out transform — SINGLE SOURCE for all fixes.

Regenerates the working build files from orig/ (pristine W45 KO core
copies), repoints OUT/BASE to the ko-es edition dir, renames the PDFs
to Lucerna-VOL2-ES.pdf / Lucerna-VOL2-ES-web.pdf, and rewrites ONLY
the explanation layer (Chinese -> Spanish). Korean target text, keys
(except the E-zone re-aim), stems, options, images and geometry are
untouched. Replacements are exact unique literals (never AST byte
offsets, tools README #17) and bare text for f-string parts (#18);
each replacement asserts its occurrence count. Run from this dir:
    tools/venv/bin/python transform.py && tools/venv/bin/python run.py
"""
import os, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ORIG = os.path.join(HERE, "orig")
ED = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-ko-es")
CORE_ED = "weekly-report-w45-ko-core"
NEW_ED = "weekly-report-w45-ko-es"

FILES = ["bslib4.py", "content12.py", "content34.py", "content56.py",
         "content7.py", "content8.py", "svglib.py", "run.py", "render.py"]

# ---- ordered replacements: (old, new, min_expected_total) ----
# Long forms BEFORE their substrings (substring-order hazards, cf. ko-de KIT §11).
MAP = [
    # instr labels first (before the same words as exercise types)
    ('instr="造句"', 'instr="Forma la frase"', 1),
    ('instr="翻译"', 'instr="Traduce"', 1),
    ('instr="写作"', 'instr="Escribe"', 1),
    ('instr="改写"', 'instr="Reescribe"', 1),
    ('instr="填空"', 'instr="Completa"', 1),
    ('instr="把词和说明配对"', 'instr="Relaciona"', 1),
    ('instr="把词和释义配对"', 'instr="Relaciona"', 1),
    ('instr="把山和说明配对"', 'instr="Relaciona"', 1),
    # exercise types (registry `type` args stay as rendered labels; W43 ES pattern)
    ("完形单选", "Texto con huecos", 1),
    ("完成句子", "Completar", 1),
    ("词汇配对", "Emparejar", 1),
    ("句型转换", "Transformación", 1),
    ("单选", "Opción múltiple", 1),
    ("造句", "Formar una frase", 1),
    ("判断", "Verdadero o falso", 1),
    ("翻译", "Traducción", 1),
    ("写作", "Redacción", 1),
    # bslib4 furniture
    ("Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY",
     "Lucerna · SEMANARIO COREANO VOL.2 · TEXTO EN COREANO · EXPLICACIONES EN ESPAÑOL", 1),
    ("제 {n} 면 / 총 {total} 면", "Página {n} de {total}", 1),
    ("译注｜", "Nota — ", 1),
    # P1 furniture
    ("매주 한국어로 · 每周一期 · 한국 사람이 읽는 한국어를 읽어요",
     "매주 한국어로 · Cada semana · 한국 사람이 읽는 한국어를 읽어요", 1),
    ("한국어판 · VOL.2 · 입동 · 단풍 · 김장",
     "SEMANARIO COREANO · VOL.2 · 입동 · 단풍 · 김장", 1),
    ("톱 뉴스 · 头条", "톱 뉴스 · Titular", 1),
    ('p.text(RIGHT - 30, 478, "立冬"', 'p.text(RIGHT - 30, 487, "IPDONG"', 1),
    ("立冬在 11 月 7 日周六 · 泡菜季开始",
     "Ipdong, el 7 de noviembre · comienza la temporada de kimjang", 1),
    ("입동 立冬、冬季开始 · 절정 最盛期、高峰 · 김장 腌过冬泡菜 · 상륙하다 登陆 · 온대저기압 温带气旋。",
     "입동 = ipdong · 절정 = apogeo · 김장 = kimchi invernal · 상륙하다 = tocar tierra · 온대저기압 = ciclón extratropical", 1),
    ("숫자로 보는 이번 주 · 数字看本周", "숫자로 보는 이번 주 · En cifras", 1),
    ("지금 바로 연습 · 即学即练", "지금 바로 연습 · Práctica inmediata", 1),
    ("这五个日期，是本期报纸的骨架。", "Estas cinco fechas articulan este número.", 1),
    ("이번 호의 내용 · 本期目录", "이번 호의 내용 · Índice", 1),
    ("全部", "Todos", 1),
    ("이번 주의 말 · 本周词语", "이번 주의 말 · Palabra de la semana", 1),
    ("입동 ＝ 立冬、冬季开始的节气。", "입동 = ipdong, el comienzo del invierno.", 1),
    ("짧은 소식 · 快讯", "짧은 소식 · Noticias breves", 1),
    ("퀴즈 · 闪电问答", "퀴즈 · Quiz relámpago", 1),
    ("读头版，选出正确答案 · 答案见第 8 版",
     "Lee la portada y elige la respuesta correcta · Respuestas en la pág. 8", 1),
    # P1 + P2 notes
    ("立冬在11月7日周六", "Ipdong es el 7 de noviembre, sábado", 1),
    ("泡菜季＝腌过冬泡菜", "La temporada de kimjang es hacer kimchi de invierno", 1),
    ("高考在11月19日周四", "El examen es el jueves 19 de noviembre", 1),
    ("11月2日是D-17", "El 2 de noviembre es D-17", 1),
    ("台风没有在韩国本土登陆", "El tifón no tocó tierra en la península de Corea", 1),
    ("首尔报名窗口11月6日10–12点", "La inscripción de Seúl, el 6 de noviembre de 10 a 12", 1),
    ("立冬＝冬季开始的节气", "Ipdong = el comienzo del invierno", 1),
    ("内藏山两个预报：11月4日与11月11日", "Las dos previsiones de Naejangsan: 4 y 11 de noviembre", 1),
    ("10月25日首场比赛因雨推迟", "El primer partido, el 25 de octubre, se aplazó por la lluvia", 1),
    # P2 bands / glosses / boxes
    ("생활 · 生活", "생활 · Vida cotidiana", 1),
    ("레벨 A2 · 김장과 겨울 준비, 한능검 · 泡菜季与过冬准备、韩史考试报名",
     "레벨 A2 · 김장과 겨울 준비, 한능검 · Kimjang, preparar el invierno y el examen de historia", 1),
    ("절이다 用盐腌 · 버무리다 拌 · 난방 供暖 · 식탁 餐桌。",
     "절이다 = salar en salmuera · 버무리다 = mezclar · 난방 = calefacción · 식탁 = mesa", 1),
    ("산불 山火 · 벌금 罚款 · 불씨 火星。",
     "산불 = incendio forestal · 벌금 = multa · 불씨 = chispa", 1),
    ("한능검 접수 · 韩史考试报名", "한능검 접수 · Examen de historia", 1),
    ("아삭하다 脆脆的 · 김 蒸汽 · 깊어지다 变深。",
     "아삭하다 = crujiente · 김 = vapor · 깊어지다 = hacerse más profundo", 1),
    ("물려주다 传给 · 낡다 旧 · 두렵다 害怕。",
     "물려주다 = pasar a otro · 낡다 = viejo, gastado · 두렵다 = tener miedo", 1),
    ("겨울 준비 목록 · 过冬清单", "겨울 준비 목록 · Lista de invierno", 1),
    ("묵직하다 沉甸甸的 · 앞치마 围裙 · 목록 清单。",
     "묵직하다 = pesado · 앞치마 = delantal · 목록 = lista", 1),
    ("你呢？为过冬做的第一件事是什么？写两句韩语寄来。",
     "¿Y tú? Para preparar el invierno, ¿qué haces primero? Escribe dos frases en coreano; envíalas.", 1),
    ("당신은? · 说说你自己", "당신은? · ¿Y tú?", 1),
    ("날짜 세는 말 · 数日子的说法", "날짜 세는 말 · Contar los días", 1),
    ("수능까지 남은 날로 날짜를 세는 네 가지 말 · 用高考倒计时数日子的四个说法",
     "수능까지 남은 날로 날짜를 세는 네 가지 말 · Cuatro formas de contar con la cuenta atrás", 1),
    ("11 月 2 日，还剩 17 天", "2 de noviembre, quedan 17 días", 1),
    ("11 月 7 日，还剩 12 天", "7 de noviembre, quedan 12 días", 1),
    ("11 月 18 日，就是明天", "18 de noviembre, mañana", 1),
    ("11 月 19 日，就是今天", "19 de noviembre, hoy", 1),
    ("연습 · 第 2 版练习", "연습 · Ejercicios pág. 2", 1),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案",
     "Respuestas en la pág. 8 · Los ejercicios mezclan niveles: busca por número", 1),
    ("2면의 글을 읽고 맞는 답을 고르세요.",
     "Lee los textos de la pág. 2 y elige la respuesta correcta.", 1),
    ("빈칸에 알맞은 말을 넣으세요.", "Pon la palabra adecuada en el hueco.", 1),
    ("1면과 2면의 숫자와 날짜로 답하세요.",
     "Responde con las cifras y las fechas de las págs. 1 y 2.", 1),
    ("山火注意期从11月1日开始", "La prevención de incendios empieza el 1 de noviembre", 1),
    ("带火进山最高罚30万韩元", "Llevar fuego al monte: multa de hasta 300.000 wones", 1),
    ("韩史考试在11月28日周六", "El examen de historia es el sábado 28 de noviembre", 1),
    ("首尔报名10点至12点", "La inscripción de Seúl es de 10 a 12", 1),
    ("白菜用盐腌", "La col se sala en salmuera", 1),
    ("加入萝卜和调料拌匀", "Se añaden rábano y condimentos y se mezclan", 1),
    ("过冬准备＝为冬天做准备", "Preparar el invierno = prepararse para el invierno", 1),
    ("进山要小心火", "En el monte, cuidado con el fuego", 1),
    ("11月3日起开始报名", "La inscripción empieza el 3 de noviembre", 1),
    ("山火注意期到12月15日", "El periodo de prevención dura hasta el 15 de diciembre", 1),
    ("最高罚款30万韩元", "La multa máxima es de 300.000 wones", 1),
    ("深化考试费27,000韩元", "La tasa del nivel avanzado es de 27.000 wones", 1),
    ("11月6日13点起全国报名剩余名额",
     "Desde las 13:00 del 6 de noviembre, plazas restantes", 1),
    ("김장=腌过冬泡菜 a", "김장 = kimchi de invierno (a)", 1),
    ("월동 준비=准备过冬 c", "월동 준비 = preparar el invierno (c)", 1),
    ("산불조심=进山小心火 d", "산불조심 = cuidado con el fuego en el monte (d)", 1),
    ("한능검=韩国史考试简称 b", "한능검 = abreviatura del examen de historia (b)", 1),
]

MAP += [
    # P3
    ("문화 · 文化", "문화 · Cultura", 1),
    ("레벨 A2→B1 · 단풍 마지막 주말 · 红叶最后一周",
     "레벨 A2→B1 · 단풍 마지막 주말 · Último fin de semana del follaje", 1),
    ("기관 机构 · 기준 标准 · 관측 观测 · 구간별 按路段。",
     "기관 = organismo · 기준 = criterio · 관측 = observación · 구간별 = por tramos", 1),
    ("현장 现场 · 유명하다 有名 · 맛보다 品尝。",
     "현장 = in situ · 유명하다 = famoso · 맛보다 = probar", 1),
    ("이용하다 利用 · 막히다 堵塞 · 예의 礼仪。",
     "이용하다 = utilizar · 막히다 = atascarse · 예의 = cortesía", 1),
    ("겹쳐 입다 叠穿 · 미끄러지다 打滑 · 돌 石头。",
     "겹쳐 입다 = vestirse por capas · 미끄러지다 = resbalar · 돌 = piedra", 1),
    ("단풍 구경 준비물 · 红叶观赏准备", "단풍 구경 준비물 · Qué llevar", 1),
    ("你呢？想去看红叶的山是哪座？写两句韩语寄来。",
     "¿Y tú? ¿A qué montaña quieres ir a ver el follaje? Escribe dos frases en coreano; envíalas.", 1),
    ("연습 · 第 3 版练习", "연습 · Ejercicios pág. 3", 1),
    ("3면의 글을 읽고 맞는 답을 고르세요.",
     "Lee los textos de la pág. 3 y elige la respuesta correcta.", 1),
    ("3면의 숫자와 날짜로 답하세요.", "Responde con las cifras y las fechas de la pág. 3.", 1),
    ("内藏山林业厅预报峰值11月4日", "Pico de Naejangsan (Agencia Forestal): 4 de noviembre", 1),
    ("内藏山公园公团预报峰值11月11日", "Pico de Naejangsan (Parques Nacionales): 11 de noviembre", 1),
    ("雪岳山实际观测峰值10月16日", "El pico observado de Seoraksan: 16 de octubre", 1),
    ("青松现场庆典11月4日至8日", "Fiesta presencial de Cheongsong, 4-8 de noviembre", 1),
    ("没有官方的路段数值", "No hay valores oficiales por tramos", 1),
    ("红叶最美的时候叫절정", "El momento más bonito del follaje se llama 절정", 1),
    ("日期不同因为标准不同", "Las fechas difieren porque los criterios difieren", 1),
    ("实际观测比预报早", "La observación real fue anterior al pronóstico", 1),
    ('"现场庆典11月4日起"', '"La fiesta presencial empieza el 4 de noviembre"', 1),
    ("青松以苹果闻名", "Cheongsong es famoso por sus manzanas", 1),
    ("内藏山林业厅预报4日", "La Agencia Forestal prevé el día 4 para Naejangsan", 1),
    ("内藏山公团预报11日", "Parques Nacionales prevé el día 11 para Naejangsan", 1),
    ("月出山林业厅预报9日", "La Agencia Forestal prevé el día 9 para Wolchulsan", 1),
    ("雪岳山实际观测16日", "La observación real de Seoraksan fue el día 16", 1),
    ("내장산=两个预报之间 b", "내장산 = entre las dos previsiones (b)", 1),
    ("월출산=11月9日前夕 a", "월출산 = víspera del 9 de noviembre (a)", 1),
    ("북한산=11月4日之后、低路更晚 d", "북한산 = tras el 4 de noviembre; caminos bajos tarde (d)", 1),
    ("설악산=实际观测10月16日 c", "설악산 = observación real del 16 de octubre (c)", 1),
    # P4
    ("스포츠 · 体育", "스포츠 · Deportes", 1),
    ("레벨 B1 · 가을야구 소식 · 秋季棒球消息",
     "레벨 B1 · 가을야구 소식 · Noticias del béisbol de otoño", 1),
    ("연승 连胜 · 만루홈런 满垒本垒打 · 미뤄지다 推迟 · 마감하다 截稿。",
     "연승 = victorias seguidas · 만루홈런 = grand slam · 미뤄지다 = aplazarse · 마감하다 = cerrar la edición", 1),
    ("흔들다 挥动 · 하나가 되다 融为一体。",
     "흔들다 = agitar · 하나가 되다 = hacerse uno", 1),
    ("예상 预测。", "예상 = previsión", 1),
    ("한국시리즈까지의 길 · 通往韩国大赛之路", "한국시리즈까지의 길 · El camino a la Serie Coreana", 1),
    ("연습 · 第 4 版练习", "연습 · Ejercicios pág. 4", 1),
    ("4면의 글을 읽고 맞는 답을 고르세요.",
     "Lee los textos de la pág. 4 y elige la respuesta correcta.", 1),
    ("문장을 과거형으로 바꾸세요. (바꾼 문장은 모두 이 신문에 나온 일이에요.)",
     "Pasa las frases al pasado. (Todas son hechos de este número.)", 1),
    ("半决赛胜队是KIA", "KIA ganó la semifinal", 1),
    ("第3场比分13比1", "El tercer partido: 13 a 1", 1),
    ("第3场在蚕室举行", "El tercer partido se jugó en Jamsil", 1),
    ("季后赛首场因雨推迟", "El primer partido del playoff se aplazó por la lluvia", 1),
    ("公布的韩国大赛开始日11月2日", "La Serie Coreana anunciada empieza el 2 de noviembre", 1),
    ("首场比赛因雨推迟", "El primer partido se aplazó por la lluvia", 1),
    ("10月26日变为温带气旋", "El 26 de octubre, ciclón extratropical", 1),
    ("kt在韩国大赛等候", "kt espera en la Serie Coreana", 1),
    ("이기다的过去式이겼어요", "Pasado de 이기다: 이겼어요", 1),
    ("열리다的过去式열렸어요", "Pasado de 열리다: 열렸어요", 1),
    ("미뤄지다的过去式미뤄졌어요", "Pasado de 미뤄지다: 미뤄졌어요", 1),
    ("바뀌다的过去式바뀌었어요", "Pasado de 바뀌다: 바뀌었어요", 1),
    ("준플레이오프=KIA三连胜 b", "준플레이오프 = KIA, tres victorias seguidas (b)", 1),
    ("플레이오프=KIA对三星 d", "플레이오프 = KIA contra Samsung (d)", 1),
    ("한국시리즈=kt在等候 a", "한국시리즈 = kt espera (a)", 1),
    ("온대저기압=台风10月26日变化 c", "온대저기압 = el tifón cambió el 26 de octubre (c)", 1),
    # P5
    ("청년 · 青年", "청년 · Juventud", 1),
    ("레벨 B1 · 수능 카운트다운과 할로윈 · 高考倒计时与万圣节",
     "레벨 B1 · 수능 카운트다운과 할로윈 · Cuenta atrás del examen y Halloween", 1),
    ("정리 整理、复习 · 끈끈하다 粘粘的 · 합격 合格。",
     "정리 = repaso, orden · 끈끈하다 = pegajoso · 합격 = aprobado", 1),
    ("중점 重点 · 배치하다 部署 · 통제하다 管制。",
     "중점 = prioritario · 배치하다 = desplegar · 통제하다 = controlar", 1),
    ("이번 주 청년 숫자 · 本周青年数字", "이번 주 청년 숫자 · Cifras de la semana", 1),
    ("챙기다 准备好 · 졸리다 犯困 · 평소 平时。",
     "챙기다 = preparar · 졸리다 = tener sueño · 평소 = habitualmente", 1),
    ("비다 祈愿 · 피하다 避开 · 미끄럽다 滑。",
     "비다 = desear, rogar · 피하다 = evitar · 미끄럽다 = resbaladizo", 1),
    ("你呢？想对考生说的一句加油是什么？写两句韩语寄来。",
     "¿Y tú? ¿Qué ánimo quieres dar a un candidato? Escribe dos frases en coreano; envíalas.", 1),
    ("연습 · 第 5 版练习", "연습 · Ejercicios pág. 5", 1),
    ("5면의 글을 읽고 맞는 답을 고르세요.",
     "Lee los textos de la pág. 5 y elige la respuesta correcta.", 1),
    ("5면의 숫자로 답하세요.", "Responde con las cifras de la pág. 5.", 1),
    ("말을 바른 순서로 놓아 문장을 만드세요.", "Ordena las palabras y forma la frase.", 1),
    ("11月7日是D-12", "El 7 de noviembre es D-12", 1),
    ("听力时段飞机不起降", "Sin vuelos durante la escucha", 1),
    ("首尔万圣节安全人员3,271人", "Seguridad de Halloween en Seúl: 3.271 personas", 1),
    ("梨泰院路10月31日管制", "La calle de Itaewon se cierra el 31 de octubre", 1),
    ("全国为考生加油", "Todo el país anima a los candidatos", 1),
    ("倒计时仍在继续", "La cuenta atrás continúa", 1),
    ("怀着祈愿合格的心意赠送糯米糕、饴糖",
     "Regalo de tteok y caramelo para aprobar", 1),
    ("首尔安全人员3,271人", "El personal de seguridad de Seúl: 3.271 personas", 1),
    ("今年考生551,864人", "Este año hay 551.864 candidatos", 1),
    ("考场全国1,312处", "Hay 1.312 centros de examen en todo el país", 1),
    ("考试日机关10点上班", "El día del examen, las oficinas abren a las 10", 1),
    ("梨泰院部署1,620人", "En Itaewon se despliegan 1.620 personas", 1),
    ("语序：主语+副词+动词", "Orden: sujeto + adverbio + verbo", 1),
    ("主语+宾语+动词的语序", "Orden: sujeto + objeto + verbo", 1),
    ("首尔管理14个地点", "Seúl gestiona 14 lugares", 1),
    # P6
    ("깊이 읽기 · 深读", "깊이 읽기 · Lectura profunda", 1),
    ("레벨 B2 · 수능 카운트다운을 읽는 법 · 高考倒计时读法",
     "레벨 B2 · 수능 카운트다운을 읽는 법 · Cómo leer la cuenta atrás del examen", 1),
    ("짙어지다 变浓 · 규모 规模 · 섞다 混淆。",
     "짙어지다 = intensificarse · 규모 = escala · 섞다 = mezclar", 1),
    ("겁이 나다 害怕 · 중요하다 重要。",
     "겁이 나다 = tener miedo · 중요하다 = importante", 1),
    ("예정 预定 · 확정 确定 · 믿다 相信。",
     "예정 = previsto · 확정 = confirmado · 믿다 = creer", 1),
    ("이번 주와 시험 날, 한눈에 보기 · 本周与考试日一表看清",
     "이번 주와 시험 날, 한눈에 보기 · Esta semana y el día del examen, de un vistazo", 1),
    ("연습 · 第 6 版练习", "연습 · Ejercicios pág. 6", 1),
    ("6면의 표를 보고 맞는 답을 고르세요.",
     "Lee la tabla de la pág. 6 y elige la respuesta correcta.", 1),
    ("6면의 글을 읽고 맞는 답을 고르세요.",
     "Lee los textos de la pág. 6 y elige la respuesta correcta.", 1),
    ("문장이 맞으면 맞다, 틀리면 틀리다를 고르세요.",
     "Elige «verdadero» si la frase es correcta y «falso» si no lo es.", 1),
    ("本周倒计时D-17至D-12", "Esta semana, la cuenta atrás va de D-17 a D-12", 1),
    ("考试日有特别措施", "El día del examen hay medidas especiales", 1),
    ("本周没有特别措施", "Esta semana no hay medidas especiales", 1),
    ("考试日就是D-day", "El día del examen es el día D", 1),
    ("本周氛围是倒计时", "El ambiente de esta semana es la cuenta atrás", 1),
    ("氛围在现在、本周", "El ambiente está ahora, esta semana", 1),
    ("听力时段13:10～13:35", "La comprensión auditiva es de 13:10 a 13:35", 1),
    ("倒计时氛围在本周", "La cuenta atrás es el ambiente de esta semana", 1),
    ("特别措施只适用于考试日", "Las medidas especiales solo se aplican el día del examen", 1),
    ("从D-17到D-12的一周", "La semana que va de D-17 a D-12", 1),
    ("大数字显示全国规模", "Las cifras grandes muestran la escala nacional", 1),
    ("听力时段飞机受管制", "Aviones restringidos durante la comprensión auditiva", 1),
    ("本周是倒计时氛围", "Esta semana es ambiente de cuenta atrás", 1),
]

MAP += [
    # P7 (long parenthesised form BEFORE the bare form used on P8)
    ("말 공부 · 语言", "말 공부 · Lengua", 1),
    ("언어 포커스 · 세 가지 레벨, 세 가지 주제 · 三个级别，三个主题",
     "언어 포커스 · 세 가지 레벨, 세 가지 주제 · Tres niveles, tres temas", 1),
    ("본격적 正式、全面 · 나다 度过。",
     "본격적 = en serio, de lleno · 나다 = pasar (el invierno)", 1),
    ("남다 剩下 · 바로 正是、恰恰。",
     "남다 = quedar · 바로 = justo, precisamente", 1),
    ("짐작하다 推测 · 나누다 区分。",
     "짐작하다 = suponer · 나누다 = distinguir", 1),
    ("节气＝一年24个时节", "절기 = las 24 divisiones del año", 1),
    ("D-1＝明天", "D-1 = mañana", 1),
    ("D-day就是当天", "El día D es el mismo día", 1),
    ("日期不同因标准不同（3版）",
     "Las fechas difieren porque los criterios difieren (pág. 3)", 1),
    ("林业厅标准是叶子50%", "El criterio de la Agencia Forestal es el 50% de las hojas", 1),
    ("实际观测10月16日", "La observación real fue el 16 de octubre", 1),
    ("预报要标准日期一起看", "En un pronóstico hay que mirar criterio y fecha juntos", 1),
    ("去某地用「에」，不用「를」。", "Para ir a un lugar se usa «에», no «를».", 1),
    ("「담그다」的过去式是「담갔어요」。", "El pasado de «담그다» es «담갔어요».", 1),
    ("数字与前面要留空格。", "El número va separado.", 1),
    ("助词只用一个。", "Se usa una sola partícula.", 1),
    ("실수 병원 · 易错诊所", "실수 병원 · La clínica de errores", 1),
    ("이번 주의 틀 · 本周句式", "이번 주의 틀 · La frase modelo", 1),
    ("句式拆解：「从〜到〜」。提问：「〜부터 〜까지예요?」",
     "«desde ~ hasta ~»: «〜부터 〜까지예요?»", 1),
    ("编辑部示例信，非真实来信。", "Ejemplo editorial, no una carta real.", 1),
    ("郑重说明：截至截稿时，未收到真实读者来信与第 8 版优秀作文，因此仍刊示例，上期承诺顺延至 VOL.3。",
     "Sin cartas reales ni mejores textos de la pág. 8, la promesa pasa al VOL.3. ¡Envíanos tu carta · tu texto destacado!", 1),
    ("독자의 편지 · 读者园地", "독자의 편지 · Cartas de los lectores", 1),
    ("이번 주의 문장 · 本周金句（逐字摘自本期文章）",
     "이번 주의 문장 · Frases de la semana (textuales, de este número)", 1),
    ("11 月 7 日是立冬。", "El 7 de noviembre es Ipdong.", 1),
    ("只能说是接近峰值的周末。", "Solo puede decirse: un fin de semana cercano al apogeo.", 1),
    ("泡菜季就是腌过冬泡菜。", "Kimjang es hacer el kimchi de todo el invierno.", 1),
    ("离高考还剩 17 天，今天是 D-17。", "Quedan 17 días para el examen; hoy es D-17.", 1),
    ("低处的路红得更晚。", "Los caminos bajos se tiñen más tarde.", 1),
    ("KIA 虎三连胜战胜 LG 双子。", "KIA Tigers venció a LG Twins por tres victorias seguidas.", 1),
    ("全国都在为考生加油。", "Todo el país anima a los candidatos.", 1),
    ("先看日期。", "Mira primero la fecha.", 1),
    ("다음 주 · 下期预告 (VOL.3)", "다음 주 · La semana que viene (VOL.3)", 1),
    # P8 (long forms first)
    ("시험과 답 · 测验与答案", "시험과 답 · Test y respuestas", 1),
    ("青松现场庆典11月4日起", "La fiesta presencial de Cheongsong empieza el 4", 1),
    ("内藏山公团预报峰值11月11日", "Pico de Naejangsan (Parques Nacionales): 11 de noviembre", 1),
    ("月出山林业厅预报峰值11月9日", "Pico de Wolchulsan (Agencia Forestal): 9 de noviembre", 1),
    ("首尔报名窗口10点至12点", "La inscripción de Seúl es de 10 a 12", 1),
    ("KIA三连胜晋级", "KIA ganó por tres victorias seguidas", 1),
    ("三连胜晋级", "Tres victorias seguidas", 1),
    ("汉拿山三角峰降雨415.5毫米", "En el pico Samgakbong de Hallasan cayeron 415,5 mm", 1),
    ("智敏周六去内藏山", "Jimin va a Naejangsan el sábado", 1),
    ("周日帮忙腌泡菜", "El domingo ayuda a hacer kimchi", 1),
    ("下周准备韩史考试", "La semana que viene prepara el examen de historia", 1),
    ("智敏喜欢韩国史", "A Jimin le gusta la historia de Corea", 1),
    ("语序：主语+时间+场所+动词", "Sujeto + tiempo + lugar + verbo", 1),
    ("보러 가요 = 去看", "보러 가요 = ir a ver", 1),
    ("动作场所用「에서」", "Lugar de la acción: «에서»", 1),
    # E-zone re-aim (core KO<->ZH -> KO<->ES); keys 137/138 + stems 139/140 only
    ("11月7日是立冬。", "El 7 de noviembre es Ipdong.", 1),
    ("离高考还剩 12 天。", "Quedan 12 días para el examen.", 1),
    ("特别措施只适用于11月19日。→ ___",
     "Las medidas especiales: solo el 19 de noviembre. → ___", 1),
    ("我周六去内藏山看红叶。→ ___",
     "El sábado voy a Naejangsan a ver el follaje. → ___", 1),
    ("对照第 1 版", "Compara con la pág. 1", 1),
    ("对照第 5 版", "Compara con la pág. 5", 1),
    ("对照第 6 版", "Compara con la pág. 6", 1),
    ("对照第 3 版", "Compara con la pág. 3", 1),
    ("特别措施只适用于11月19日", "Las medidas especiales: solo el 19 de noviembre", 1),
    # restore the E stem to its full sentence form (the note shortening
    # above must not shorten the translation stem itself)
    ("Las medidas especiales: solo el 19 de noviembre. → ___",
     "Las medidas especiales solo se aplican el 19 de noviembre. → ___", 1),
    ("措施只适用于11月19日", "Las medidas solo se aplican el 19 de noviembre", 1),
    ("日期不同因标准不同", "Las fechas difieren porque los criterios difieren", 1),
    ("입동=冬季开始的节气 a", "입동 = el comienzo del invierno (a)", 1),
    ("절정=最佳时期 b", "절정 = el mejor momento (b)", 1),
    ("김장=腌过冬泡菜 c", "김장 = kimchi de invierno (c)", 1),
    ("온대저기압=台风10月26日变化 d", "온대저기압 = el tifón cambió el 26 de octubre (d)", 1),
    ("周六去内藏山", "Ir a Naejangsan el sábado", 1),
    ("首尔报名10点开始", "La inscripción de Seúl empieza a las 10", 1),
    ("쓰기 문제예요 (정답은 하나가 아니에요). 아래에 {NCHARS}자의 예가 있어요.",
     "Ejercicio de escritura (sin respuesta única); el modelo ({NCHARS} caracteres) está debajo.", 1),
    ("(开放题，范文如下)", "(pregunta abierta — modelo a continuación)", 1),
    ("范文见本版 H 区（{NCHARS} 字）",
     "El modelo está en la sección H ({NCHARS} caracteres)", 1),
    ("답 · 参考答案 — 按版面分页排列，找到题号即可",
     "답 · Respuestas — ordenadas por página, busca el número", 1),
    ("每题附一句中文简析 · 带 ✓ 的为范文题",
     "Cada respuesta con una nota breve en español · ✓ = ejercicio con modelo", 1),
]

# ---- structural line edits (exact lines, asserted) ----
STRUCT = [
    # P1 masthead geometry: W43 ko-es measured — subtitle 372->366,
    # badge INSERTED y=394 20pt BRICK, rules +20, dark band +9.
    ('p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")\n'
     'p.text(975, 394, "TEXTOS EN COREANO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 20, "sans", True, BRICK, anchor="middle")'),
    ('p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)',
     'p.hline(MX, RIGHT, 412, INK, 3); p.hline(MX, RIGHT, 421, INK, 1.2)'),
    ('p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)',
     'p.rect(MX, 433, RIGHT - MX, 118, fill=DARK)'),
    ('p.text(MX + 30, 478, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")',
     'p.text(MX + 30, 487, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")'),
    ('p.text(MX + 30, 522, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")',
     'p.text(MX + 30, 531, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")'),
    ('p.text(RIGHT - 30, 522, "Ipdong, el 7 de noviembre · comienza la temporada de kimjang", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 531, "Ipdong, el 7 de noviembre · comienza la temporada de kimjang", 21, "sans", False, "#b3a06a", anchor="end")'),
]

def main():
    os.makedirs(ED, exist_ok=True)
    os.makedirs(os.path.join(ED, "svg"), exist_ok=True)
    os.makedirs(os.path.join(ED, "cards"), exist_ok=True)
    for f in FILES:
        shutil.copyfile(os.path.join(ORIG, f), os.path.join(HERE, f))
    # repoint OUT / BASE + PDF names (before MAP, so MAP counts are unaffected)
    for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
        p = os.path.join(HERE, f)
        s = open(p, encoding="utf-8").read()
        old = f"files/{CORE_ED}/svg"
        assert s.count(old) == 1, (f, s.count(old))
        s = s.replace(old, f"files/{NEW_ED}/svg")
        open(p, "w", encoding="utf-8").write(s)
    rp = os.path.join(HERE, "render.py")
    s = open(rp, encoding="utf-8").read()
    assert s.count(f"files/{CORE_ED}") == 1
    s = s.replace(f"files/{CORE_ED}", f"files/{NEW_ED}")
    assert s.count("Lucerna-VOL2.pdf") == 1 and s.count("Lucerna-VOL2-web.pdf") == 1
    s = s.replace("Lucerna-VOL2.pdf", "Lucerna-VOL2-ES.pdf")
    s = s.replace("Lucerna-VOL2-web.pdf", "Lucerna-VOL2-ES-web.pdf")
    open(rp, "w", encoding="utf-8").write(s)
    # MAP across all working files
    totals = {}
    for f in FILES:
        p = os.path.join(HERE, f)
        s = open(p, encoding="utf-8").read()
        for old, new, _mn in MAP:
            n = s.count(old)
            if n:
                totals[old] = totals.get(old, 0) + n
                s = s.replace(old, new)
        open(p, "w", encoding="utf-8").write(s)
    # structural edit (content7 letters box): +29 slack (KIT section 7)
    p7 = os.path.join(HERE, "content7.py")
    s7 = open(p7, encoding="utf-8").read()
    _anchor = 'len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 26'
    assert s7.count(_anchor) == 1, s7.count(_anchor)
    s7 = s7.replace(_anchor, 'len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 65  # +39 total slack: last-line ink (incl. inverted ! depth 4.3px) clears border by 8.9px')
    open(p7, "w", encoding="utf-8").write(s7)
    # structural edits (content12 only)
    p = os.path.join(HERE, "content12.py")
    s = open(p, encoding="utf-8").read()
    for old, new in STRUCT:
        assert s.count(old) == 1, ("STRUCT miss", old[:60], s.count(old))
        s = s.replace(old, new)
    open(p, "w", encoding="utf-8").write(s)
    missing = [(o, n) for (o, n, _m) in MAP if totals.get(o, 0) == 0]
    print("MAP entries:", len(MAP), "| applied with count>0:", len(MAP) - len(missing))
    if missing:
        print("MISSING (count 0):")
        for o, n in missing:
            print("  !!", o)
        sys.exit(1)
    # post-checks: no Han left in working code, no stray ASCII double-quote leaks
    import re
    # svglib.py is the shared library: its 2 Han chars live in a code
    # comment (never rendered) and the file stays byte-identical to core.
    for f in [x for x in FILES if x != "svglib.py"]:
        s = open(os.path.join(HERE, f), encoding="utf-8").read()
        hans = re.findall(r"[\u4e00-\u9fff]", s)
        print(f, "Han chars left:", len(hans), hans[:10])
        assert not hans, f
    print("transform OK -> edition dir:", ED)

if __name__ == "__main__":
    main()
