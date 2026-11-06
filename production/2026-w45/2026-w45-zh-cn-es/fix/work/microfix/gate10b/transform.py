# -*- coding: utf-8 -*-
"""W45 zh-cn x es: explanation-layer EN -> ES transform for MY OWN build copy only.
Line-based whole-string replacements with an assertion after each one.
NEVER run inside the core build dir. Usage: python transform.py (cwd = this dir).
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BADGE = "TEXTOS EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES"
FOOTER = "Lucerna · SEMANARIO CHINO SIMPLIFICADO VOL.2 · TEXTO EN CHINO SIMPLIFICADO · EXPLICACIONES EN ESPAÑOL"

# (filename, old, new) — old must occur >= 1 time; replace-all within that file.
R = []
def add(f, old, new):
    R.append((f, old, new))

# ---------- bslib4: furniture ----------
add("bslib4.py",
    "Lucerna · 简体中文周报 VOL.2 · 简体中文正文 · 英语讲解 · Simplified Chinese text · English explanations",
    FOOTER)
add("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Página {n} de {total}"')
add("bslib4.py", '"Notes｜" + s', '"Nota — " + s')

# ---------- shared heads / glosslines / instr ----------
for f in ["content12.py", "content34.py", "content56.py"]:
    add(f, "Answers on page 8 · 答案见第 8 版", "Respuestas en la página 8 · 答案见第 8 版")
    add(f, "练习 · Exercises", "练习 · Ejercicios")
# Micro-fix (Gate 10 cleanup): byline levels are per-file, not shared —
# content12 has no B1 byline and content56 has no A2 byline in the core
# (both verified 0 hits), so those two loop instances were dead misses.
# content34 A2→B1 (line ~146) HELD, not deleted: its old string IS present
# in raw core (content34.py line 16), so per the task STOP rule it stays.
for f in ["content12.py", "content34.py"]:
    add(f, "Lucerna editors · Reading level A2", "Redacción Lucerna · Nivel de lectura A2")
for f in ["content34.py", "content56.py"]:
    add(f, "Lucerna editors · Reading level B1", "Redacción Lucerna · Nivel de lectura B1")
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    add(f, 'instr="Fill in"', 'instr="Completa"')
add("content12.py", 'instr="Fill in the blank"', 'instr="Completa"')
add("content12.py", "A · 读一读选一选 · Read & choose", "A · 读一读选一选 · Lee y elige")
add("content34.py", "A · 读一读选一选 · Read & choose", "A · 读一读选一选 · Lee y elige")
add("content56.py", "A · 读一读选一选 · Read & choose", "A · 读一读选一选 · Lee y elige")
for f in ["content12.py", "content34.py", "content56.py"]:
    add(f, "B · 词语填空 · Word blanks", "B · 词语填空 · Completa huecos")
    add(f, "D · 词语配对 · Matching", "D · 词语配对 · Relaciona")
    add(f, "Fill each blank with the right word.", "Completa cada hueco con la palabra adecuada.")
    add(f, 'instr="Match the words"', 'instr="Relaciona las palabras"')
add("content12.py", "Read page 2 and choose the best answer.", "Lee la página 2 y elige la mejor respuesta.")
add("content34.py", "Read page 3 and choose the best answer.", "Lee la página 3 y elige la mejor respuesta.")
add("content34.py", "Read page 4 and choose the best answer.", "Lee la página 4 y elige la mejor respuesta.")
add("content56.py", "Read page 5 and choose the best answer.", "Lee la página 5 y elige la mejor respuesta.")
add("content56.py", "Read page 6 and choose the best answer.", "Lee la página 6 y elige la mejor respuesta.")
add("content12.py", "C · 数字与日期 · Numbers", "C · 数字与日期 · Números")
add("content34.py", "C · 数字与日期 · Numbers", "C · 数字与日期 · Números")
add("content34.py", "C · 读赛程 · Schedule work", "C · 读赛程 · Lee el calendario")
add("content56.py", "C · 时间与数字 · Times & numbers", "C · 时间与数字 · Fechas y cifras")
add("content56.py", "C · 练习篮子算一算 · Basket maths", "C · 练习篮子算一算 · Cuentas")
add("content12.py", "Use the practice example on this page.", "Usa el ejemplo práctico de esta página.")
add("content34.py", "Answer with dates and numbers from page 3.", "Responde con fechas y cifras de la página 3.")
add("content34.py", "Read the schedule on page 4.", "Lee el calendario de la página 4.")
add("content56.py", "Answer with dates and numbers from page 5.", "Responde con fechas y cifras de la página 5.")
add("content56.py", "Compute from the practice baskets.", "Calcula con las cestas de práctica.")
add("content12.py", "说说你自己 · And you?", "说说你自己 · ¿Y tú?")
add("content34.py", "说说你自己 · And you?", "说说你自己 · ¿Y tú?")
add("content56.py", "说说你自己 · And you?", "说说你自己 · ¿Y tú?")

# ---------- P1 (content12) ----------
add("content12.py", "每周读中文 · Read real Chinese, every week", "每周读中文 · Lee chino de verdad, cada semana")
add("content12.py", "简体中文版 · VOL.2 · 双11 · 立冬 · S16", "SEMANARIO CHINO SIMPLIFICADO · VOL.2 · 双11 · 立冬 · S16")
add("content12.py", "给学中文的人的周报 — Read the real China, in Chinese", "给学中文的人的周报 — Lee la China real, en chino")
add("content12.py", "简体中文正文 · 英语讲解 — Simplified Chinese text · Explanations in English · the edition for English-speaking readers", BADGE)
add("content12.py", "Shopping week meets winter · see pages 2–3", "Semana de compras y de invierno · ver páginas 2–3")
add("content12.py", "头条 · Top story", "头条 · Titular")
add("content12.py", "xiànhuò 现货 — goods in stock, ready to ship · lìjiǎn 立减 — an instant discount at checkout · zhíjiàng 直降 — a direct price cut · jiéqì 节气 — the 24 solar terms that divide the year.",
    "xiànhuò 现货 — mercancía en stock, lista para enviar · lìjiǎn 立减 — un descuento instantáneo en caja · zhíjiàng 直降 — una bajada directa del precio · jiéqì 节气 — los 24 términos solares que dividen el año.")
add("content12.py", "数字看本周 · This week in numbers", "数字看本周 · La semana en cifras")
add("content12.py", "Nov 13 — the last day of the spot-sale period", "13 nov. — el último día del periodo de ventas en stock")
add("content12.py", "Nov 7, Saturday — 立冬 (Start of Winter)", "7 nov., sábado — 立冬 (Comienzo del Invierno)")
add("content12.py", "Oct 12, 20:00 — JD.com spot sales began", "12 oct., 20:00 — JD.com empezó las ventas en stock")
add("content12.py", "Nov 10, 20:00 — the peak sale (高潮场) begins next week", "10 nov., 20:00 — la venta punta (高潮场) empieza la semana que viene")
add("content12.py", "即学即练 · Try it now", "即学即练 · Practica ahora")
add("content12.py", "JD.com spot sales began on Oct 12.", "JD.com empezó las ventas en stock el 12 de octubre.")
add("content12.py", "Taobao and Tmall pre-sales began on Oct 15.", "Las preventas de Taobao y Tmall: 15 de octubre.")
add("content12.py", "Spot sales run until Nov 13.", "Las ventas en stock duran hasta el 13 de noviembre.")
add("content12.py", "Start of Winter falls on Saturday, Nov 7.", "El Comienzo del Invierno cae en sábado, 7 de noviembre.")
add("content12.py", "Start of Winter is winter's first solar term.", "El Comienzo del Invierno es el primer término del invierno.")
add("content12.py", "This year many goods are marked down directly.", "Este año muchos productos bajan directamente.")
add("content12.py", "本周日历 · This week", "本周日历 · Esta semana")
add("content12.py", "11月2日—8日 · Nov 2–8", "11月2日—8日 · 2–8 nov.")
add("content12.py", "What happens this week", "Qué pasa esta semana")
add("content12.py", "The Swiss stage ends Nov 1, so the quarter-final teams are not known at press time. Quarter-finals run Nov 4–7, the first semi-final Nov 8, all at 06:00 Beijing time.",
    "La fase suiza termina el 1 de noviembre, así que los equipos de cuartos no se conocen al cierre. Los cuartos se juegan del 4 al 7 de noviembre y la primera semifinal el 8, todos a las 06:00, hora de Pekín.")
add("content12.py", "All times Beijing time", "Todas las horas son de Pekín")
add("content12.py", "S16 teams depend on the Swiss stage", "Los equipos del S16 dependen de la fase suiza")
add("content12.py", "本期目录 · Contents", "本期目录 · Índice")
add("content12.py", "本周词 · Word of the week", "本周词 · Palabra de la semana")
add("content12.py", "「立冬」 lìdōng — Start of Winter: the first solar term of winter. 立冬到了,冬天要来了。Example: 「立冬那天,我们吃饺子。」",
    "「立冬」 lìdōng — Comienzo del Invierno: el primer término solar del invierno. 立冬到了,冬天要来了。Ejemplo: 「立冬那天,我们吃饺子。」")
add("content12.py", "Photo: Map hobby — CC0 (Wikimedia Commons)", "Foto: Map hobby — CC0 (Wikimedia Commons)")
add("content12.py", "快讯 · Briefs", "快讯 · Breves")
add("content12.py", "闪电问答 · Quick quiz", "闪电问答 · Quiz relámpago")
add("content12.py", "Read page 1 and choose · 答案见第 8 版", "Lee la página 1 y elige · 答案见第 8 版")
add("content12.py", "Start of Winter is on Saturday, Nov 7.", "El Comienzo del Invierno es el sábado 7 de noviembre.")

# ---------- P2 (content12) ----------
add("content12.py", 'p.band("生活 · Life", "Lucerna", "Level A2 · 双11购物生活 · 立冬生活 · Shopping & the first winter days")',
    'p.band("生活 · Vida", "Lucerna", "Nivel A2 · 双11购物生活 · 立冬生活 · Compras y los primeros días de invierno")')
add("content12.py", "cāngkù 仓库 — a warehouse · píngjià 评价 — a review, what buyers say · chǐmǎ 尺码 — a size · tuìhuànhuò 退换货 — returns and exchanges.",
    "cāngkù 仓库 — un almacén · píngjià 评价 — una reseña, lo que dicen los compradores · chǐmǎ 尺码 — una talla · tuìhuànhuò 退换货 — devoluciones y cambios.")
add("content12.py", "满减与直降 · Old vs new", "满减与直降 · Antes y ahora")
add("content12.py", "The old rule many shoppers knew was 「满300减50」 (spend 300 yuan, save 50). This year the common pattern is 直降 (zhíjiàng): the price itself drops, and the checkout price is what you pay. The example below uses practice numbers, not real shop prices.",
    "La vieja regla que muchos compradores conocían era 「满300减50」 (gasta 300 yuanes, ahorra 50). Este año el patrón común es 直降 (zhíjiàng): el precio mismo baja, y el precio en caja es lo que pagas. El ejemplo de abajo usa cifras de práctica, no precios reales de tienda.")
add("content12.py", "Practice example · 练习例子", "Ejemplo práctico · 练习例子")
add("content12.py", "bǔdōng 补冬 — eating well before winter · jiāozǐ 饺子 — dumplings · cíbā 糍粑 — sticky rice cakes · qīzhōng 期中 — mid-term (exams).",
    "bǔdōng 补冬 — comer bien antes del invierno · jiāozǐ 饺子 — empanadillas chinas · cíbā 糍粑 — pasteles de arroz glutinoso · qīzhōng 期中 — exámenes parciales.")
add("content12.py", "本周生活小日历 · This week's dates", "本周生活小日历 · Fechas clave")
add("content12.py", "Photo: Paul Gilmore — CC0 (Wikimedia Commons)", "Foto: Paul Gilmore — CC0 (Wikimedia Commons)")
add("content12.py", "你知道吗 · Did you know?", "你知道吗 · ¿Sabías que?")
add("content12.py", "And you? What do you want to buy this 双11? What would you eat on 立冬? Write two sentences in Chinese.",
    "¿Y tú? ¿Qué quieres comprar este 双11? ¿Qué comerías en 立冬? Escribe dos frases en chino.")
add("content12.py", "购物词语卡 · Shopping words", "购物词语卡 · Palabras de compras")
add("content12.py", "Four words you will see on every shopping app", "Cuatro palabras que verás en toda app de compras")
add("content12.py", '("现货", "xiànhuò · goods in stock", "in stock now, ready to ship")',
    '("现货", "xiànhuò · mercancía en stock", "en stock, lista para enviar")')
add("content12.py", '("直降", "zhíjiàng · a direct price cut", "the price drops directly, no maths")',
    '("直降", "zhíjiàng · bajada directa", "baja directa, sin cuentas")')
add("content12.py", '("立减", "lìjiǎn · an instant discount", "taken off at checkout")',
    '("立减", "lìjiǎn · descuento instantáneo", "descuento en caja")')
add("content12.py", '("补冬", "bǔdōng · winter nourishment", "eating well before winter")',
    '("补冬", "bǔdōng · comer bien en invierno", "comer bien antes del invierno")')
add("content12.py", "Remember the sentence: 「买现货不用等,先看结算页,再付款。」", "Recuerda la frase: 「买现货不用等,先看结算页,再付款。」")
add("content12.py", "Taobao and Tmall spot sales began on Oct 20.", "Ventas en stock de Taobao y Tmall: 20 de octubre.")
add("content12.py", "直降 means the price itself drops.", "直降 significa que el precio mismo baja.")
add("content12.py", "After 立冬 the weather gets colder day by day.", "Después de 立冬 el tiempo se enfría día a día.")
add("content12.py", "The WeChat shop event runs until Nov 15.", "El evento de la tienda WeChat termina el 15 de noviembre.")
add("content12.py", "xiànhuò — goods in stock, ready to ship.", "xiànhuò — mercancía en stock, lista para enviar.")
add("content12.py", "zhíjiàng — the price itself drops.", "zhíjiàng — el precio mismo baja.")
add("content12.py", "bǔdōng — eating well before winter.", "bǔdōng — comer bien antes del invierno.")
add("content12.py", "jiǎozǐ — northern families eat these at 立冬.", "jiǎozǐ — las familias del norte las comen en 立冬.")
add("content12.py", "qīzhōng — mid-term exams fall in early November in some schools.", "qīzhōng — los exámenes parciales caen a principios de noviembre en algunas escuelas.")
add("content12.py", "The sweater costs 240 yuan in the example.", "El suéter cuesta 240 yuanes en el ejemplo.")
add("content12.py", "240 + 80 = 320 yuan together.", "240 + 80 = 320 yuanes en total.")
add("content12.py", "320 − 50 = 270 yuan after the direct cut.", "320 − 50 = 270 yuanes tras la bajada directa.")
add("content12.py", "The WeChat shop event runs 35 days in total.", "El evento de la tienda de WeChat dura 35 días en total.")
add("content12.py", '"xiànhuò 现货 = in stock, b"', '"xiànhuò 现货 = en stock, b"')
add("content12.py", '"zhíjiàng 直降 = price drops, d"', '"zhíjiàng 直降 = el precio baja, d"')
add("content12.py", '"lìjiǎn 立减 = off at checkout, c"', '"lìjiǎn 立减 = descuento en caja, c"')
add("content12.py", '"bǔdōng 补冬 = eat well before winter, a"', '"bǔdōng 补冬 = comer bien antes del invierno, a"')

# ---------- P3 (content34) ----------
add("content34.py", 'p.band("文化 · Culture", "Lucerna", "Level A2→B1 · 立冬:冬天的第一个节气 · Start of Winter")',
    'p.band("文化 · Cultura", "Lucerna", "Nivel A2→B1 · 立冬:冬天的第一个节气 · Comienzo del Invierno")')
add("content34.py", "Lucerna editors · Reading level A2→B1", "Redacción Lucerna · Nivel de lectura A2→B1")
add("content34.py", "hòu 候 — a five-day micro-season · jiāotì 交替 — one thing giving way to another · cǎifǎng 采访 — to interview, to report from the scene.",
    "hòu 候 — una microestación de cinco días · jiāotì 交替 — una cosa que da paso a otra · cǎifǎng 采访 — entrevistar, informar desde el lugar.")
add("content34.py", "hòu yīfu 厚衣服 — warm clothes · rè fàn 热饭 — a hot meal · zháoliáng 着凉 — to catch cold.",
    "hòu yīfu 厚衣服 — ropa de abrigo · rè fàn 热饭 — una comida caliente · zháoliáng 着凉 — resfriarse.")
add("content34.py", "Photo: Gerda Arendt — CC0 (Wikimedia Commons)", "Foto: Gerda Arendt — CC0 (Wikimedia Commons)")
add("content34.py", "节日小日历 · Festival dates", "节日小日历 · Fechas festivas")
add("content34.py", "Photo: Syced — CC0 (Wikimedia Commons)", "Foto: Syced — CC0 (Wikimedia Commons)")
add("content34.py", "And you? What would you eat on 立冬? Is it cold where you live? Write two sentences in Chinese.",
    "¿Y tú? ¿Qué comerías en 立冬? ¿Hace frío donde vives? Escribe dos frases en chino.")
add("content34.py", "立冬 is the 19th of the 24 solar terms.", "立冬 es el 19.º de los 24 términos solares.")
add("content34.py", "First micro-season: water begins to freeze.", "Primera microestación: el agua empieza a helarse.")
add("content34.py", "Northern families eat dumplings at 立冬.", "Las familias del norte comen empanadillas en 立冬.")
add("content34.py", "A journalist interviews people and writes the news.", "Un periodista entrevista a la gente y escribe las noticias.")
add("content34.py", "lìdōng — Start of Winter, Nov 7.", "lìdōng — Comienzo del Invierno, 7 de noviembre.")
add("content34.py", "shuǐ shǐ bīng — water begins to freeze (1st micro-season).", "shuǐ shǐ bīng — el agua empieza a helarse (1.ª microestación).")
add("content34.py", "tāngyuán — sticky rice balls eaten in some southern places.", "tāngyuán — bolas de arroz glutinoso que se comen en algunos lugares del sur.")
add("content34.py", "jìzhě — a journalist interviews and writes news.", "jìzhě — un periodista que entrevista y escribe noticias.")
add("content34.py", "立冬 is the 19th solar term.", "立冬 es el 19.º término solar.")
add("content34.py", "Start of Winter is on Nov 7.", "El Comienzo del Invierno es el 7 de noviembre.")
add("content34.py", "The solar-term moment is 17:52.", "El momento del término solar es a las 17:52.")
add("content34.py", "Journalists' Day is on Nov 8.", "El Día del Periodista es el 8 de noviembre.")
add("content34.py", '"水始冰 = water begins to freeze, b"', '"水始冰 = el agua empieza a helarse, b"')
add("content34.py", '"地始冻 = earth begins to freeze, c"', '"地始冻 = la tierra empieza a helarse, c"')
add("content34.py", '"雉入大水为蜃 = the old pheasant story, d"', '"雉入大水为蜃 = la vieja historia del faisán, d"')
add("content34.py", '"bǔdōng 补冬 = eat well before winter, a"', '"bǔdōng 补冬 = comer bien antes del invierno, a"')

# ---------- P4 (content34) ----------
add("content34.py", 'p.band("体育 · Sport", "Lucerna", "Level B1 · S16 瑞士轮与淘汰赛 · Worlds S16: Swiss stage & knockouts")',
    'p.band("体育 · Deporte", "Lucerna", "Nivel B1 · S16 瑞士轮与淘汰赛 · Mundial S16: fase suiza y eliminatorias")')
add("content34.py", "tǎotài 淘汰 — to knock out, to eliminate · nèizhàn 内战 — a match between two teams from the same region · zhǐbù 止步 — to stop here, to go no further.",
    "tǎotài 淘汰 — eliminar, dejar fuera · nèizhàn 内战 — un partido entre dos equipos de la misma región · zhǐbù 止步 — quedarse aquí, no seguir adelante.")
add("content34.py", "S16 赛程 · S16 schedule (Beijing time)", "S16 赛程 · Calendario S16 (hora de Pekín)")
add("content34.py", "Standings as of Oct 27, 2026: GEN and DK already 3–0 and through; AL and TSW 0–3 and out. Source: Sina Sports S16 guide (Beijing times) and match reports, Oct 26–27.",
    "Clasificación a 27 de octubre de 2026: GEN y DK ya están 3–0 y clasificados; AL y TSW 0–3 y eliminados. Fuente: guía S16 de Sina Sports (horas de Pekín) y crónicas de los partidos, 26–27 de octubre.")
add("content34.py", "体育小日历 · Sports dates", "体育小日历 · Fechas deportivas")
add("content34.py", "看比赛的中文 · Match words", "看比赛的中文 · Para ver partidos")
add("content34.py", '("通宵", "tōngxiāo — to stay up all night for a match.")', '("通宵", "tōngxiāo — pasar la noche en vela por un partido.")')
add("content34.py", '("加油", "jiāyóu — come on! (what fans shout).")', '("加油", "jiāyóu — ¡vamos! (lo que gritan los aficionados).")')
add("content34.py", '("翻盘", "fānpán — a comeback win, turning a game around.")', '("翻盘", "fānpán — una remontada, dar la vuelta a un partido.")')
add("content34.py", "The Swiss stage is played in Allen, Texas.", "La fase suiza se juega en Allen, Texas.")
add("content34.py", "AL lost all three of its Swiss-stage series.", "AL perdió sus tres series de la fase suiza.")
add("content34.py", "IG beat HLE on Oct 26.", "IG venció a HLE el 26 de octubre.")
add("content34.py", "Quarter-finals start at 06:00 Beijing time.", "Los cuartos empiezan a las 06:00, hora de Pekín.")
add("content34.py", "The final starts at 03:00 Beijing time on Nov 15.", "La final es a las 03:00 del 15 de noviembre, hora de Pekín.")
add("content34.py", "Àilún — Allen, Texas, hosts the Swiss stage.", "Àilún — Allen, Texas, acoge la fase suiza.")
add("content34.py", "nèizhàn — AL lost the all-LPL match to TES.", "nèizhàn — AL perdió ante TES en el duelo de la LPL.")
add("content34.py", "táotài — three wins send a team to the knockouts.", "táotài — tres victorias clasifican a las eliminatorias.")
add("content34.py", "fānpán — TES turned the game against G2 around.", "fānpán — TES remontó el partido contra G2.")
add("content34.py", "jiāyóu — what fans shout for their team.", "jiāyóu — lo que gritan los aficionados por su equipo.")
add("content34.py", "Three wins send a team through from the Swiss stage.", "Tres victorias clasifican a un equipo desde la fase suiza.")
add("content34.py", "AL won zero series in the Swiss stage.", "AL no ganó ninguna serie en la fase suiza.")
add("content34.py", "The Swiss stage runs until Nov 1.", "La fase suiza dura hasta el 1 de noviembre.")
add("content34.py", '"瑞士轮 = the Swiss stage, d"', '"瑞士轮 = la fase suiza, d"')
add("content34.py", '"内战 = an all-region match, c"', '"内战 = un partido entre equipos de la misma región, c"')
add("content34.py", '"淘汰赛 = loser goes home, b"', '"淘汰赛 = el que pierde se va a casa, b"')
add("content34.py", '"总决赛 = the final, a"', '"总决赛 = la final, a"')

# ---------- P5 (content56) ----------
add("content56.py", 'p.band("青年 · Youth", "Lucerna", "Level B1 · AI电影 · 立冬新片 · AI films & a winter film")',
    'p.band("青年 · Juventud", "Lucerna", "Nivel B1 · AI电影 · 立冬新片 · Cine con IA y una película de invierno")')
add("content56.py", "shùzì xíngxiàng 数字形象 — a digital character · gōngyìng 公映 — a public cinema release · piàofáng 票房 — box-office takings.",
    "shùzì xíngxiàng 数字形象 — un personaje digital · gōngyìng 公映 — un estreno público en cines · piàofáng 票房 — la taquilla.")
add("content56.py", "huǒhuà 火化 — cremation · jiùshú 救赎 — redemption, saving each other · yǐhòu 以后 — later, some other day.",
    "huǒhuà 火化 — la cremación · jiùshú 救赎 — la redención, salvarse mutuamente · yǐhòu 以后 — más tarde, otro día.")
add("content56.py", "这一周的高频词 · Words of the week", "这一周的高频词 · Palabras clave")
add("content56.py", "AI电影 — a film made with AI: no live actors, digital characters only.", "AI电影 — una película hecha con IA: sin actores reales, solo personajes digitales.")
add("content56.py", "Photo: Based5290 — Public domain (Wikimedia Commons)", "Foto: Based5290 — Dominio público (Wikimedia Commons)")
add("content56.py", "电影小日历 · Film dates", "电影小日历 · Fechas de cine")
add("content56.py", "And you? Would you watch a film made by AI? Who would you watch a film with on 立冬? Write two sentences in Chinese.",
    "¿Y tú? ¿Verías una película hecha con IA? ¿Con quién verías una película en 立冬? Escribe dos frases en chino.")
add("content56.py", "The AI film has no live actors.", "La película con IA no tiene actores reales.")
add("content56.py", "The AI film runs 100 minutes.", "La película con IA dura 100 minutos.")
add("content56.py", "By noon on Oct 26, Maoyan showed about 1.192 million yuan.", "Al mediodía del 26 de octubre, Maoyan mostraba unos 1,192 millones de yuanes.")
add("content56.py", "The new film opens on Nov 7, Start of Winter.", "La nueva película se estrena en lìdōng, 7 de noviembre.")
add("content56.py", "Huang Yan is a crematory worker.", "Huang Yan es trabajadora de un crematorio.")
add("content56.py", "shùzì — the film's characters are digital images.", "shùzì — los personajes son imágenes digitales.")
add("content56.py", "piàofáng — box-office takings, about 1.192 million yuan.", "piàofáng — la taquilla, unos 1,192 millones de yuanes.")
add("content56.py", "huǒhuà — Huang Yan works at a crematory.", "huǒhuà — Huang Yan trabaja en un crematorio.")
add("content56.py", "jiùshú — the two women save each other.", "jiùshú — las dos mujeres se salvan mutuamente.")
add("content56.py", "lìdōng — the new film opens on Start of Winter.", "lìdōng — estreno de la nueva película.")
add("content56.py", "The AI film opened on Oct 23.", "La película con IA se estrenó el 23 de octubre.")
add("content56.py", "On Oct 24–25, each screening averaged 2 viewers.", "El 24 y 25 de octubre: media de 2 espectadores por sesión.")
add("content56.py", "The new film runs 114 minutes.", "La nueva película dura 114 minutos.")
add("content56.py", '"数字形象 = a digital character, b"', '"数字形象 = un personaje digital, b"')
add("content56.py", '"票房 = box-office takings, a"', '"票房 = la taquilla, a"')
add("content56.py", '"火化师 = a crematory worker, d"', '"火化师 = un trabajador del crematorio, d"')
add("content56.py", '"救赎 = saving each other, c"', '"救赎 = salvarse mutuamente, c"')

# ---------- P6 (content56) ----------
add("content56.py", 'p.band("深读 · Deep read", "Lucerna", "Level B2 · 双11深读 · Why the rules got simpler")',
    'p.band("深读 · Lectura a fondo", "Lucerna", "Nivel B2 · 双11深读 · Por qué las reglas se simplificaron")')
add("content56.py", "Lucerna editors · Reading level B2", "Redacción Lucerna · Nivel de lectura B2")
add("content56.py", "jiésuàn 结算 — checkout, settling the bill · yùnfèi 运费 — delivery cost · guǎnggào 广告 — an advertisement.",
    "jiésuàn 结算 — la caja, pagar la cuenta · yùnfèi 运费 — el coste de envío · guǎnggào 广告 — un anuncio.")
add("content56.py", "shuōfǎ 说法 — a claim, what someone says · shùjù 数据 — data, measured numbers · tuìhuànhuò 退换货 — returns and exchanges.",
    "shuōfǎ 说法 — una afirmación, lo que alguien dice · shùjù 数据 — datos, cifras medidas · tuìhuànhuò 退换货 — devoluciones y cambios.")
add("content56.py", "三个练习篮子:直降以后实付多少钱 · Practice baskets", "三个练习篮子:直降以后实付多少钱 · Cestas de práctica")
add("content56.py", "Bars are drawn from 0 (3 px = 1 yuan). Practice data only — not real shop prices. Basket maths is in the article above.",
    "Las barras parten de 0 (3 px = 1 yuan). Solo datos de práctica, no precios reales de tienda. Las cuentas de las cestas están en el artículo de arriba.")
add("content56.py", "深读要点 · Key points", "深读要点 · Puntos clave")
add("content56.py", "读新闻三问 · Three questions", "读新闻三问 · Tres preguntas")
add("content56.py", "And you? What do you check before you buy? Write two sentences in Chinese.",
    "¿Y tú? ¿Qué compruebas antes de comprar? Escribe dos frases en chino.")
add("content56.py", "This year spot sales are much bigger.", "Este año las ventas en stock son mucho mayores.")
add("content56.py", "With 直降 the checkout price is what you pay.", "Con 直降 el precio en caja es lo que pagas.")
add("content56.py", "AI helps you check prices and reviews first.", "La IA te ayuda a comprobar primero precios y reseñas.")
add("content56.py", "The WeChat shop event runs 35 days.", "El evento de la tienda de WeChat dura 35 días.")
add("content56.py", "The checkout page shows what you really pay.", "La página de caja muestra lo que realmente pagas.")
add("content56.py", "jiésuàn — the checkout page shows the real price.", "jiésuàn — la página de caja muestra el precio real.")
add("content56.py", "yùnfèi — delivery cost, check whether it is included.", "yùnfèi — el coste de envío: comprueba si está incluido.")
add("content56.py", "guǎnggào — an advertisement's 'lowest price' needs checking.", "guǎnggào — el «precio más bajo» de un anuncio hay que comprobarlo.")
add("content56.py", "240 + 80 = 320, minus 50 = 270 yuan.", "240 + 80 = 320, menos 50 = 270 yuanes.")
add("content56.py", "199 − 20 = 179 yuan.", "199 − 20 = 179 yuanes.")
add("content56.py", "120 + 40 = 160 yuan, no direct cut.", "120 + 40 = 160 yuanes, sin bajada directa.")
add("content56.py", "Basket A is cut by 50 yuan.", "La cesta A se rebaja 50 yuanes.")
add("content56.py", '"说法 = a claim, c"', '"说法 = una afirmación, c"')
add("content56.py", '"数据 = measured numbers, d"', '"数据 = cifras medidas, d"')
add("content56.py", '"结算页 = the checkout page, b"', '"结算页 = la página de caja, b"')
add("content56.py", '"运费 = delivery cost, a"', '"运费 = el coste de envío, a"')

# ---------- P7 (content7) ----------
add("content7.py", 'p.band("词语 · Language focus", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Three levels, three topics")',
    'p.band("词语 · Enfoque lingüístico", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Tres niveles, tres temas")')
add("content7.py", "A2 · 双11与冬天 · Shopping", "A2 · 双11与冬天 · Compras")
add("content7.py", "Shopping words for this week: 现货 (xiànhuò, in stock), 直降 (zhíjiàng, a direct cut), 立减 (lìjiǎn, off at checkout), 结算页 (jiésuàn yè, the checkout page). Winter words: 立冬 (lìdōng, Start of Winter), 补冬 (bǔdōng, eating well before winter), 厚衣服 (hòu yīfu, warm clothes).",
    "Palabras de compras para esta semana: 现货 (xiànhuò, en stock), 直降 (zhíjiàng, una bajada directa), 立减 (lìjiǎn, descuento en caja), 结算页 (jiésuàn yè, la página de caja). Palabras de invierno: 立冬 (lìdōng, Comienzo del Invierno), 补冬 (bǔdōng, comer bien antes del invierno), 厚衣服 (hòu yīfu, ropa de abrigo).")
add("content7.py", "Measure words still matter: 一件毛衣 (a sweater), 一条围巾 (a scarf), 一部电影 (a film).",
    "Los clasificadores siguen importando: 一件毛衣 (un suéter), 一条围巾 (una bufanda), 一部电影 (una película).")
add("content7.py", "毛衣 takes the measure word 件 jiàn.", "毛衣 lleva el clasificador 件 jiàn.")
add("content7.py", "Clothes take 件, not 个 or 条.", "La ropa lleva 件, no 个 ni 条.")
add("content7.py", "One more to practise: 「这件毛衣多少钱?」 (How much is this sweater?) When you shop, ask the price first, then pay.",
    "Una más para practicar: 「这件毛衣多少钱?」 (¿Cuánto cuesta este suéter?) Cuando compres, pregunta primero el precio y luego paga.")
add("content7.py", "B1 · 时间与日期 · Time & dates", "B1 · 时间与日期 · Tiempo y fechas")
add("content7.py", "Chinese gives times big → small: year, month, day, weekday, part of day, hour. Examples from this issue: 「11月7日星期六17点52分」 (Sat Nov 7, 17:52), 「11月10日星期二20点」 (Tue Nov 10, 20:00), 「11月15日凌晨3点」 (Nov 15, 3 a.m.). The biggest unit first, nothing out of order.",
    "El chino da las horas de mayor a menor: año, mes, día, día de semana, parte del día, hora. Ejemplos de este número: 「11月7日星期六17点52分」 (sáb. 7 de nov., 17:52), 「11月10日星期二20点」 (mar. 10 de nov., 20:00), 「11月15日凌晨3点」 (15 de nov., 3 de la madrugada). La unidad mayor primero, nada fuera de orden.")
add("content7.py", "So English «Saturday evening, Nov 7» becomes 11月7日星期六晚上.",
    "Así, «el sábado por la tarde, 7 de noviembre» se convierte en 11月7日星期六晚上.")
add("content7.py", "凌晨 língchén — the small hours after midnight.", "凌晨 língchén — las primeras horas tras medianoche.")
add("content7.py", "06:00 is 早上 (morning), not evening.", "Las 06:00 son 早上 (mañana), no tarde.")
add("content7.py", "Big → small order: Nov 7, Saturday, 17:52.", "Orden de mayor a menor: 7 de nov., sábado, 17:52.")
add("content7.py", "Nov 7 is a Saturday — 周六.", "El 7 de noviembre es sábado — 周六.")
add("content7.py", "Two more words: 凌晨 (língchén) is the small hours after midnight, before dawn; 傍晚 (bàngwǎn) is the short stretch just before dark.",
    "Dos palabras más: 凌晨 (língchén) son las horas pequeñas después de medianoche, antes del alba; 傍晚 (bàngwǎn) es el rato corto justo antes de que oscurezca.")
add("content7.py", "B2 · 读新闻 · Reading the news", "B2 · 读新闻 · Leer las noticias")
add("content7.py", "When a story involves a claim (说法), separate three kinds of sentence: claims (说法), data (数据) and advertisements (广告). Page 6 is the example: 「最低价」 is a claim, the practice baskets' 270元 is practice data, and the checkout page shows what you really pay.",
    "Cuando una historia incluye una afirmación (说法), separa tres tipos de frase: afirmaciones (说法), datos (数据) y anuncios (广告). La página 6 es el ejemplo: 「最低价」 es una afirmación, los 270元 de las cestas de práctica son datos de práctica, y la página de caja muestra lo que realmente pagas.")
add("content7.py", "Ask of every price: whose number is it, and where is it written?",
    "Ante cada precio, pregunta: ¿de quién es la cifra y dónde está escrita?")
add("content7.py", "「最低价」 is an advertising claim, not measured data.", "「最低价」 es publicidad, no un dato medido.")
# Gate 10 fix round (2026-10-28): the P7 frame text was never in transform.py,
# so the transform-alone repro left it in English. Added so transform alone
# reproduces the delivered P7 frame.
add("content7.py", "「先看评价,再下单。」(First check the reviews, then order.) The frame 先…再… gives the order of actions. More: 「先看天气,再出门。」", "「先看评价,再下单。」(Primero mira las reseñas y luego pide.) El marco 先…再… da el orden de las acciones. Más: 「先看天气,再出门。」")
add("content7.py", "shùjù — measured numbers, not claims.", "shùjù — cifras medidas, no afirmaciones.")
add("content7.py", "Data and the checkout page first; the headline last.", "Primero los datos y la página de caja; el titular al final.")
add("content7.py", "Try it yourself: in the page-1 calendar box, 「11月7日」 is a date — data. The words in an advertisement are claims. Can you tell them apart?",
    "Pruébalo tú: en el calendario de la página 1, 「11月7日」 es una fecha, un dato. Las palabras de un anuncio son afirmaciones. ¿Sabes distinguirlas?")
add("content7.py", "易错诊所 · Error clinic", "易错诊所 · Clínica de errores")
add("content7.py", "地 (de) marks how an action is done.", "地 (de): marca el modo de la acción.")
add("content7.py", "得 (de) links verb + degree: 跑得快.", "得 (de): verbo + grado: 跑得快.")
add("content7.py", "Order: number + measure word + noun. The final 个 is one too many; sweaters take 件.",
    "Orden: número + clasificador + sustantivo. El 个 final sobra; el suéter lleva 件.")
add("content7.py", "Times go big → small: weekday last.", "De mayor a menor: el día de semana al final.")
add("content7.py", "本周句式 · Sentence frame", "本周句式 · Marco de frase")
add("content7.py", "Frame: 先 … 再 … — first X, then Y.", "Marco: 先 … 再 … — primero X, luego Y.")
add("content7.py", "读者园地 · Readers' corner", "读者园地 · Rincón de lectores")
add("content7.py", "编辑部示例信,不是真实来信。编辑部说明:VOL.1曾预告本期(VOL.2)刊登真实读者来信和VOL.1第8版最佳作文;至今没有收到真实来信,也没有可刊登的投稿,所以本期仍刊登编辑部示例,并继续征集。延期不是取消。Editor's note: VOL.1 promised real letters and the best VOL.1 writing in VOL.2. None have arrived, so this corner still prints an editor's example. Deferred, not cancelled.",
    "Ejemplo de la redacción, no una carta real. VOL.1 prometió cartas reales y la mejor redacción de VOL.1 en VOL.2; no ha llegado ninguna carta real ni hay ningún texto publicable, así que este rincón sigue publicando un ejemplo de la redacción. Aplazado, no cancelado. ¡Envíanos tu carta en chino! Escribe dos frases sobre tu semana y la publicaremos aquí.")
add("content7.py", "本周金句 · Phrases of the week (verbatim, from this issue's own articles)",
    "本周金句 · Frases de la semana (textuales, de los artículos de este número)")
add("content7.py", '"No need to wait for Nov 11.", "p. 1"', '"No hay que esperar al 11 de noviembre.", "Página 1"')
add("content7.py", '"Order it and it ships.", "p. 2"', '"Lo pides y se envía.", "Página 2"')
add("content7.py", '"Check the checkout page, then pay.", "p. 2"', '"Revisa la página de caja y luego paga.", "Página 2"')
add("content7.py", '"The water begins to freeze.", "p. 3"', '"El agua empieza a helarse.", "Página 3"')
add("content7.py", '"All three series lost.", "p. 4"', '"Las tres series perdidas.", "Página 4"')
add("content7.py", '"Not a single game won.", "p. 4"', '"Ni un solo juego ganado.", "Página 4"')
add("content7.py", '"But is the story good enough?", "p. 5"', '"Pero ¿la historia es lo bastante buena?", "Página 5"')
add("content7.py", '"Not later — now.", "p. 5"', '"No después: ahora.", "Página 5"')
add("content7.py", "下期预告 · Next week (VOL.3)", "下期预告 · La semana que viene (VOL.3)")

# ---------- P8 (content8) ----------
add("content8.py", 'p.band("测验与答案 · Test & keys", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · This week\'s test and every answer key")',
    'p.band("测验与答案 · Test y claves", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · El test de la semana y todas las claves")')
add("content8.py", 'f.head("A · 判断对错 · True or false", 21, OLIVE, 5)', 'f.head("A · 判断对错 · Verdadero o falso", 21, OLIVE, 5)')
add("content8.py", 'f.head("B · 本周大测验 · The big quiz", 21, OLIVE, 5)', 'f.head("B · 本周大测验 · El gran test", 21, OLIVE, 5)')
add("content8.py", 'f.head("C · 完成句子 · Complete", 21, OLIVE, 5)', 'f.head("C · 完成句子 · Completa", 21, OLIVE, 5)')
add("content8.py", 'f.head("D · 读一读,答一答 · Read & answer", 21, OLIVE, 5)', 'f.head("D · 读一读,答一答 · Lee y responde", 21, OLIVE, 5)')
add("content8.py", 'f.head("E · 情景说话 · In conversation", 21, OLIVE, 5)', 'f.head("E · 情景说话 · En conversación", 21, OLIVE, 5)')
add("content8.py", 'f.head("F · 写一写 · Writing", 21, OLIVE, 5)', 'f.head("F · 写一写 · Escritura", 21, OLIVE, 5)')
add("content8.py", 'instr="Writing"', 'instr="Escritura"')
add("content8.py", "立冬 is the 19th solar term, not the 18th.", "立冬 es el 19.º término solar, no el 18.º.")
add("content8.py", "Spot goods ship without a deposit wait.", "La mercancía en stock se envía sin esperar un anticipo.")
add("content8.py", "The new film opens on Nov 7.", "La nueva película se estrena el 7 de noviembre.")
add("content8.py", "Journalists' Day is on Nov 8, not Nov 7.", "El Día del Periodista es el 8 de noviembre, no el 7.")
add("content8.py", "TES beat G2 on Oct 26.", "TES venció a G2 el 26 de octubre.")
add("content8.py", "Basket A pays 270 yuan after the cut.", "La cesta A paga 270 yuanes tras la rebaja.")
add("content8.py", "piàofáng — box-office takings.", "piàofáng — la taquilla.")
add("content8.py", "lìjiǎn — taken off at checkout.", "lìjiǎn — se descuenta en caja.")
add("content8.py", "Xiao Hong lives in Beijing.", "Xiao Hong vive en Pekín.")
add("content8.py", "On 立冬 she made dumplings with her mother.", "En 立冬 hizo empanadillas con su madre.")
add("content8.py", "She bought a scarf online.", "Compró una bufanda en línea.")
add("content8.py", "She phoned her grandmother on Sunday.", "Llamó a su abuela el domingo.")
add("content8.py", "Order: dumplings, then shopping, then the phone call.", "Orden: empanadillas, luego compras, luego la llamada.")
add("content8.py", "Spot goods ship right away, no pre-sale wait.", "La mercancía en stock se envía al momento, sin preventa.")
add("content8.py", "Page 6's rule: data first, advertisement last.", "Página 6: primero los datos, el anuncio al final.")
add("content8.py", 'f"Writing — there is no single right answer. A {NCHARS}-character model follows."',
    'f"Escritura — no hay una única respuesta correcta. Sigue un modelo de {NCHARS} caracteres."')
add("content8.py", '"(开放题，范文如下)"', '"(pregunta abierta — modelo a continuación)"')
add("content8.py", 'f"Open task - the model answer is printed in section F above ({NCHARS} characters)"',
    'f"Pregunta abierta — el modelo está en la sección F de esta página, {NCHARS} caracteres"')
add("content8.py", '"Model answer: " + MODELO', '"Respuesta modelo: " + MODELO')
add("content8.py", "答案 · Answer keys — by page, with a note on every answer", "答案 · Claves — por página, con una nota para cada respuesta")
add("content8.py", "All notes in English · ✓ = the writing task", "Todas las notas en español · ✓ = la tarea de escritura")
add("content8.py", 'f"— Page {pg} —"', 'f"— Página {pg} —"')
# Shared notes also present in content8 (same translations as earlier files):
for _old, _new in [
    ("Spot sales run until Nov 13.", "Las ventas en stock duran hasta el 13 de noviembre."),
    ("The solar-term moment is 17:52.", "El momento del término solar es a las 17:52."),
    ("First micro-season: water begins to freeze.", "Primera microestación: el agua empieza a helarse."),
    ("IG beat HLE on Oct 26.", "IG venció a HLE el 26 de octubre."),
    ("By noon on Oct 26, Maoyan showed about 1.192 million yuan.", "Al mediodía del 26 de octubre, Maoyan mostraba unos 1,192 millones de yuanes."),
    ("Huang Yan is a crematory worker.", "Huang Yan es trabajadora de un crematorio."),
    ("The WeChat shop event runs 35 days.", "El evento de la tienda de WeChat dura 35 días."),
    ("The final starts at 03:00 Beijing time on Nov 15.", "La final es a las 03:00 del 15 de noviembre, hora de Pekín."),
    ("Start of Winter is on Nov 7.", "El Comienzo del Invierno es el 7 de noviembre."),
    ("zhíjiàng — the price itself drops.", "zhíjiàng — el precio mismo baja."),
    ("Àilún — Allen, Texas, hosts the Swiss stage.", "Àilún — Allen, Texas, acoge la fase suiza."),
    ("jiǎozǐ — northern families eat these at 立冬.", "jiǎozǐ — las familias del norte las comen en 立冬."),
    ("shùzì — the AI film's characters are digital images.", "shùzì — personajes digitales en la película con IA."),
    ("jiésuàn — the checkout page shows the real price.", "jiésuàn — la página de caja muestra el precio real."),
    ("bǔdōng — eating well before winter.", "bǔdōng — comer bien antes del invierno."),
    ("jìzhě — a journalist interviews and writes news.", "jìzhě — un periodista que entrevista y escribe noticias."),
    ("AL lost all three of its Swiss-stage series.", "AL perdió sus tres series de la fase suiza."),
    ("Quarter-finals start at 06:00 Beijing time.", "Los cuartos empiezan a las 06:00, hora de Pekín."),
    ("The AI film has no live actors.", "La película con IA no tiene actores reales."),
    ("Northern families eat dumplings at 立冬.", "Las familias del norte comen empanadillas en 立冬."),
]:
    add("content8.py", _old, _new)

# ---------- cross-file notes missed above (same translation, other files) ----------
add("content34.py", "Start of Winter falls on Saturday, Nov 7.", "El Comienzo del Invierno cae en sábado, 7 de noviembre.")
add("content34.py", "jiǎozǐ — northern families eat these at 立冬.", "jiǎozǐ — las familias del norte las comen en 立冬.")
add("content56.py", "xiànhuò — goods in stock, ready to ship.", "xiànhuò — mercancía en stock, lista para enviar.")
add("content56.py", "zhíjiàng — the price itself drops.", "zhíjiàng — el precio mismo baja.")
add("content7.py", "直降 means the price itself drops.", "直降 significa que el precio mismo baja.")
add("content7.py", "lìdōng — Start of Winter, Nov 7.", "lìdōng — Comienzo del Invierno, 7 de noviembre.")
add("content7.py", "jiésuàn — the checkout page shows the real price.", "jiésuàn — la página de caja muestra el precio real.")

# ---------- runner ----------
def main():
    failed = []
    for f, old, new in R:
        path = os.path.join(HERE, f)
        with open(path, encoding="utf-8") as fh:
            txt = fh.read()
        n = txt.count(old)
        if n < 1:
            failed.append((f, old[:80]))
            print(f"MISS {f}: {old[:100]!r}")
            continue
        txt = txt.replace(old, new)
        with open(path, "w", encoding="utf-8") as fh:
            fh.write(txt)
        print(f"ok {f} x{n}: {old[:60]!r} -> {new[:60]!r}")
    print(f"TOTAL replacements: {len(R) - len(failed)}/{len(R)}")
    if failed:
        print("FAILED:")
        for f, o in failed:
            print(" ", f, o)
        sys.exit(1)

if __name__ == "__main__":
    main()
