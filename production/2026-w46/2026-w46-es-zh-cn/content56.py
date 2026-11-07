# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P5 youth / P6 deep read. Fresh text, structure mirrors W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-zh-cn/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JUVENTUD (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JUVENTUD · 青年", "La Lucerna", "NIVEL B1 · Votar desde casa · 在家投票")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Votar desde casa: el voto por correo", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: B1")
f.para("No hace falta ir al colegio electoral para votar: el voto por correo llega a casa.")
f.para("El voto por correo se pide desde la convocatoria y hasta el jueves 19 de noviembre, en cualquier oficina de Correos o por internet, en la web de Correos. La Oficina del Censo Electoral envía la documentación a la dirección indicada a partir del lunes 9 de noviembre. Después, votas en casa, con calma, y envías el sobre.")
f.para("Y si prefieres votar en persona, el domingo 29 los colegios electorales abren de 9:00 a 20:00, con tu documento de identidad. El sábado 28, jornada de reflexión, no hay propaganda ni actos de campaña: un día de silencio antes de votar.")
f.para("Y el viernes 13, la otra cita de la semana joven: llega a HBO Max «Infamia», un thriller español de seis episodios con Susana Abaitua, que adapta la novela de la escritora gallega Ledicia Costas. La serie tuvo su estreno mundial en el festival de series de Cádiz.")
f.box("EL PLAN DE LA SEMANA · 本周计划", [
    ("1. El lunes 9: llega la documentación del voto por correo a casa（周一：邮寄选票材料开始寄出）", "serif", False, INK, 21, 1.36),
    ("2. El miércoles 11: huelga general de 24 horas（周三：24 小时大罢工）", "serif", False, INK, 21, 1.36),
    ("3. El jueves 12: Chequia–España, 20:45, en Praga（周四晚：捷克对西班牙）", "serif", False, INK, 21, 1.36),
    ("4. El viernes 13: empieza la campaña; se estrena «Infamia»（周五：竞选开始；《Infamia》上线）", "serif", False, INK, 21, 1.36),
    ("5. Y el domingo 15: España–Inglaterra, 20:45, en el Metropolitano（周日：西班牙对英格兰）", "serif", False, INK, 21, 1.36),
])
f.gloss("el sobre 信封 · la papeleta 选票 · el censo 选民名册 · la jornada de reflexión 投票前静默日。")
f.end_report()

# col 3: typographic plate + facts + ¿Y tú?
ix = COLX[3]
p.rect(ix, 200, CW, 290, fill=DARK, stroke=LINE, sw=1.4)
p.text(ix + CW / 2, 300, "INFAMIA", 54, "sans", True, "#f3edda", anchor="middle")
p.text(ix + CW / 2, 352, "VIERNES 13 · HBO MAX", 24, "sans", True, "#b3a06a", anchor="middle")
p.text(ix + CW / 2, 404, "Seis episodios · Susana Abaitua", 21, "serif", False, "#e8dfc8", anchor="middle")
p.text(ix + CW / 2, 444, "Novela de Ledicia Costas", 21, "serif", False, "#e8dfc8", anchor="middle")
cy3 = caption(p, ix, 490, CW, "«Infamia», el thriller español del viernes 13: una abogada obsesionada con una desaparición de hace veinte años. El domingo 15, la otra pantalla: la Roja contra Inglaterra.",
              "Placa tipográfica: La Lucerna")
facts = ["El voto por correo se pide hasta el jueves 19: en Correos o por internet.",
         "La documentación llega a casa a partir del lunes 9 de noviembre.",
         "«Infamia» se estrena el viernes 13: seis episodios, en HBO Max."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "VOTAR DESDE CASA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Votarías por correo o en persona? ¿Qué serie ves esta semana: «Infamia» o el fútbol? Escribe dos frases en español."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你会邮寄投票还是亲自去投票？这周你看什么：《Infamia》还是足球？写两句寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ? · 说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你会邮寄投票还是亲自去投票？这周你看什么：《Infamia》还是足球？写两句寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · 第 5 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · COMPRENSIÓN", 25)
e.bridge("读第 5 版文章，选出正确答案。")
e.ex("B1", "单选", "B", "邮寄投票须在 19 日前申请",
     "El voto por correo se pide hasta... A. el lunes 9 · B. el jueves 19 · C. el domingo 29", size=20, gap=8)
e.ex("B1", "单选", "A", "材料从 11 月 9 日起寄出",
     "La documentación del voto por correo llega desde... A. el lunes 9 · B. el viernes 13 · C. el sábado 28", size=20, gap=8)
e.ex("B1", "单选", "C", "投票站 9:00–20:00 开放",
     "El domingo 29, los colegios abren... A. todo el día · B. de noche · C. de 9:00 a 20:00", size=20, gap=8)
e.ex("B1", "单选", "B", "Infamia 有 6 集",
     "«Infamia» tiene... A. dos episodios · B. seis episodios · C. veinte episodios", size=20, gap=8)
e.ex("B1", "单选", "A", "静默日没有宣传活动",
     "El sábado 28, jornada de reflexión, no hay... A. propaganda ni actos · B. fútbol · C. series", size=20, gap=8)
e.head("B · PALABRAS DEL TEXTO", 25)
e.bridge("用方框里的词填空。注意：有的词要变位。")
e.para("sobre · papeleta · censo · identidad · reflexión · correo", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "correo", "correo = 邮局/邮寄",
     "Pido el voto por ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "papeleta", "papeleta = 选票",
     "En casa, relleno la ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "envío", "enviar 变位 → envío",
     "Después ___ (原形 enviar) el sobre.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "identidad", "documento de identidad 身份证件",
     "Para votar en persona llevo mi documento de ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "censo", "censo = 选民名册",
     "La Oficina del ___ envía la documentación.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "reflexión", "jornada de reflexión 静默日",
     "El sábado 28 es la jornada de ___.", instr="填空", size=20, gap=8)
e.head("C · IR A + INFINITIVO", 25)
e.bridge("用 ir a + 原形动词改写句子，表示“将要”。")
e.ex("B1", "句型转换", "Voy a pedir el voto por correo.", "voy a + 原形",
     "Pido el voto por correo. → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Va a estrenarse «Infamia».", "va a + 原形",
     "Se estrena «Infamia». → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Vas a ver el España–Inglaterra.", "vas a + 原形",
     "Ves el España–Inglaterra. → ___", instr="改写", size=20, gap=8)
e.ex("B1", "句型转换", "Van a votar el domingo 29.", "van a + 原形",
     "Votan el domingo 29. → ___", instr="改写", size=20, gap=8)
e.head("D · ¿VERDADERO O FALSO?", 25)
e.ex("B1", "判断对错", "Verdadero", "邮寄投票可在 Correos 申请",
     "El voto por correo se pide en una oficina de Correos. ¿Verdadero o falso?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Falso", "静默日是周六 28 日，不是周日",
     "La jornada de reflexión es el domingo 29. ¿Verdadero o falso?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Verdadero", "Infamia 改编自 Ledicia Costas 的小说",
     "«Infamia» adapta una novela de Ledicia Costas. ¿Verdadero o falso?", instr="判断", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-juventud.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · A FONDO (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("A FONDO · 深读", "La Lucerna", "NIVEL B2 · La vivienda decide la campaña · 住房决定选战")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P6-main")
f.title("La vivienda decide la campaña", 37)
f.byline("De la redacción de La Lucerna · Nivel de lectura: B2 · La política nacional española")
f.para("La vivienda preocupa al 86,9 % de los españoles.")
f.para("Ese dato es del Barómetro de Vivienda 2026 del CIS, el instituto público de encuestas: estudio número 3532, con 6.019 entrevistas, un margen de error de ±1,3 puntos, publicado el 8 de octubre. Es la primera vez que el CIS dedica un estudio monográfico a la vivienda.")
f.para("El barómetro pregunta por soluciones, y las respuestas son claras: el 91,4 % cree que las administraciones deberían construir más vivienda pública, y el 76,3 % defiende que el Estado intervenga en el mercado «tanto como sea necesario». El 79 % quiere que la vivienda se trate como un derecho constitucional, frente al 13,5 % que la ve como un bien de mercado.")
f.para("Una encuesta es una foto con margen de error, tomada en un día concreto.")
f.para("Y mientras tanto, la campaña ya tiene su calendario: el miércoles 11, huelga general; el viernes 13 empieza la campaña; el jueves 19 termina el plazo del voto por correo; el viernes 27 termina la campaña; y el domingo 29, la única encuesta que no admite error: la votación, con papeletas de verdad.")
f.para("El 28 de octubre, un grave accidente ferroviario en Urda (Toledo) detuvo la precampaña unos días. La investigación sigue abierta: esta página no adelanta conclusiones.")
f.end_report()

# col 3: timeline + poll-reading box (sequential, measured)
bx = COLX[3]
steps = [
    "2 OCT. — El Congreso rechaza dos decretos de vivienda.",
    "5 OCT. — Sánchez disuelve las Cortes; elecciones el 29-N.",
    "6 OCT. — El decreto de convocatoria sale en el BOE.",
    "21–26 OCT. — Se presentan las candidaturas.",
    "28 OCT. — Grave accidente en Urda: la precampaña se detiene.",
    "3 NOV. — El BOE difunde las candidaturas proclamadas.",
    "9 NOV. — La documentación del voto por correo llega a casa.",
    "11 NOV. — Huelga general de 24 horas.",
    "13 NOV. — Empieza la campaña electoral.",
    "19 NOV. — Termina el plazo para pedir el voto por correo.",
    "27 NOV. — Termina la campaña; el 29, España vota.",
]
tl_h = 68 + sum(len(wrap(t, "serif", False, 19, CW - 44)) * 19 * 1.35 + 29 for t in steps) + 20
p.rect(bx, 200, CW, tl_h, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 200 + 16
p.text(bx + 22, yy3 + 26, "EL CAMINO AL 29N", 24, "sans", True, OLIVE)
yy3 += 52
for t in steps:
    yy3 = p.para(bx + 22, yy3 + 19, t, 19, "serif", False, INK, CW - 44, 1.35) + 10
tl_end = 200 + tl_h
by3 = tl_end + 26
bb = ("Para leer cualquier encuesta, pregunta tres cosas: ¿quién la publica? "
      "¿Cuándo se hizo el trabajo de campo? ¿Qué margen de error tiene? "
      "Sin esas tres respuestas, un porcentaje no dice casi nada.")
bh = 62 + len(wrap(bb, "serif", False, 21.5, CW - 44)) * 30.5 + 16
p.rect(bx, by3, CW, bh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = by3 + 16
p.text(bx + 22, yy3 + 26, "LEER UNA ENCUESTA", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, bb, 21.5, "serif", False, INK, CW - 44, 1.42)
print("P6 col3 ends", by3 + bh, "timeline box height", tl_h)

# ---- bar charts (CIS Barómetro de Vivienda 2026, honestly captioned) ----
gy = 1566
p.hline(MX, RIGHT, gy - 18, GOLD, 2)
p.text(MX, gy + 10, "EL BARÓMETRO DE VIVIENDA DEL CIS · % que apoya cada medida", 26, "sans", True, OLIVE)
cis = [("1ª vivienda: menos impuestos", 95.4), ("Más vivienda pública", 91.4), ("Empresa pública de vivienda", 76.3), ("Limitar pisos turísticos", 75.6), ("Congelar alquileres 2 años", 70.6)]
bx1, bw_, bhh = MX, 2 * CW + GUT, 322
p.rect(bx1, gy + 28, bw_, bhh, fill=BOX, stroke=LINE, sw=1.4)
p.text(bx1 + 22, gy + 68, "BARÓMETRO DE VIVIENDA (CIS) · apoyo a cada medida, %", 21, "sans", True, INK)
yy = gy + 96
for lab, v in cis:
    p.text(bx1 + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(bx1 + 430, yy + 6, v * 3.2, 22, fill=OLIVE)
    p.text(bx1 + 448 + v * 3.2, yy + 24, f"{v:.1f}".replace(".", ",") + " %", 20.5, "serif", False, INK)
    yy += 31
p.para(bx1 + 22, gy + bhh - 30, "CIS, instituto público · estudio 3532 · 6.019 entrevistas · margen ±1,3 puntos · publicado el 8 de octubre. Solo se publica esta serie, con su fuente y su fecha.", 17.5, "sans", False, GREY, bw_ - 44, 1.3)
# right column: housing as a right
rx = COLX[2]
p.rect(rx, gy + 28, 2 * CW + GUT, bhh, fill="#f1ead6", stroke=LINE, sw=1.4)
p.text(rx + 22, gy + 68, "LA VIVIENDA: ¿DERECHO O MERCADO?", 21, "sans", True, INK)
yy = gy + 96
for lab, v in [("Preocupados por la vivienda", 86.9), ("Derecho constitucional", 79.0), ("Bien de mercado", 13.5)]:
    p.text(rx + 22, yy + 24, lab, 21, "serif", True, INK)
    p.rect(rx + 430, yy + 6, v * 3.2, 22, fill=BRICK)
    p.text(rx + 448 + v * 3.2, yy + 24, f"{v:.1f}".replace(".", ",") + " %", 20.5, "serif", False, INK)
    yy += 31
p.para(rx + 22, gy + bhh - 30, "Según el mismo barómetro: el 86,9 % está preocupado por la vivienda; el 79 % la ve como un derecho constitucional y solo el 13,5 % como un bien de mercado.", 17.5, "sans", False, GREY, 2 * CW + GUT - 44, 1.3)

# ---- P6 exercises ----
ey = 1940
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "EJERCICIOS · 第 6 版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第 8 版 · 题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · LEER LOS GRÁFICOS", 25)
e.bridge("看上面两张图，选出正确答案。")
e.ex("B2", "单选", "A", "减税支持率最高（95,4%）",
     "La medida con más apoyo es... A. bajar impuestos a la 1ª vivienda · B. limitar pisos turísticos · C. congelar alquileres", size=19, gap=3)
e.ex("B2", "单选", "B", "更多公屋支持率 91,4%",
     "Construir más vivienda pública lo apoya el... A. 76,3 % · B. 91,4 % · C. 70,6 %", size=19, gap=3)
e.ex("B2", "单选", "C", "担心住房者 86,9%",
     "Está preocupado por la vivienda el... A. 13,5 % · B. 79 % · C. 86,9 %", size=19, gap=3)
e.ex("B2", "单选", "A", "调查 6.019 人次，误差 ±1,3",
     "El barómetro se hizo con... A. 6.019 entrevistas · B. 5.025 entrevistas · C. 3532 entrevistas", size=19, gap=3)
e.ex("B2", "单选", "B", "95,4 − 91,4 = 4,0",
     "Entre la medida más apoyada y la segunda hay... A. 19,1 puntos · B. 4,0 puntos · C. 24,8 puntos", size=19, gap=3)
e.ex("B2", "单选", "C", "本报只刊登 CIS 住房晴雨表这一组数据并注明来源日期",
     "La Lucerna publica aquí... A. una media mezclada · B. todos los sondeos · C. solo la serie del CIS, con fuente y fecha", size=19, gap=3)
e.head("B · COMPRENSIÓN", 25)
e.ex("B2", "单选", "B", "10 月 2 日议会否决两项住房法令",
     "El 2 de octubre, el Congreso... A. aprobó dos decretos · B. rechazó dos decretos de vivienda · C. disolvió las Cortes", size=19, gap=3)
e.ex("B2", "单选", "A", "10 月 5 日解散议会并召集大选",
     "El 5 de octubre, Sánchez... A. disolvió las Cortes y convocó elecciones · B. publicó las listas · C. empezó la campaña", size=19, gap=3)
e.ex("B2", "单选", "C", "民调是带误差的具体某天的照片",
     "Según el texto, una encuesta es... A. un resultado final · B. una promesa · C. una foto con margen de error", size=19, gap=3)
e.ex("B2", "单选", "B", "竞选 11 月 13 日开始",
     "La campaña electoral empieza el... A. 3 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=19, gap=3)
e.head("C · EL SUBJUNTIVO", 25)
e.ex("B2", "完成句子", "tenga", "es posible que + 虚拟式 tenga",
     "Es posible que el CIS ___ (tener) otro método.", instr="填空", size=19, gap=3)
e.ex("B2", "完成句子", "sea", "es importante que + 虚拟式 sea",
     "Es importante que cada gráfico ___ (ser) claro.", instr="填空", size=19, gap=3)
e.ex("B2", "完成句子", "para que", "para que + 虚拟式（目的）",
     "Publicamos la fuente ___ todos puedan comprobarla.", instr="填空", size=19, gap=3)
e.ex("B2", "完成句子", "Aunque", "Aunque 后接陈述式（已知事实）",
     "___ las encuestas difieren, ninguna miente.", instr="填空", size=19, gap=3)
e.head("D · PALABRAS DEL DEBATE", 25)
e.bridge("用方框里的词填空：sondeo · muestra · indecisos · margen de error")
e.ex("B2", "完成句子", "sondeo", "sondeo = 民调",
     "Un ___ pregunta a una muestra de ciudadanos.", instr="填空", size=19, gap=3)
e.ex("B2", "完成句子", "muestra", "muestra = 样本（6.019 人）",
     "El CIS entrevistó a una ___ de 6.019 personas.", instr="填空", size=19, gap=3)
e.ex("B2", "完成句子", "indecisos", "indecisos = 未决定者",
     "Los ___ todavía no saben a quién votar.", instr="填空", size=19, gap=3)
e.ex("B2", "完成句子", "margen de error", "margen de error = 误差范围",
     "Toda encuesta tiene un ___.", instr="填空", size=19, gap=3)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-afondo.svg")
print("P6 saved, exercises so far:", len(REG))
