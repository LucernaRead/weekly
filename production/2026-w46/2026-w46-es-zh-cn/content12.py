# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — fresh text, week 9–15 Nov 2026. Structure/counts mirror W45.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P1 · PORTADA (A2) =================
CURPAGE[0] = 1
p = BSPage4()

# top strip
p.text(MX, 92, "VOL. 3　TERCERA EDICIÓN", 17, "sans", True, OLIVE, spacing=1.7)
p.text(975, 92, "CADA SEMANA EN ESPAÑOL　每周一期　读西班牙人正在读的西班牙语", 17, "sans", False, GREY, anchor="middle", spacing=1.7)
p.text(RIGHT, 92, "SEMANA DEL 9 AL 15 DE NOVIEMBRE DE 2026", 17, "sans", False, GREY, anchor="end", spacing=1.7)
p.text(975, 262, "La Lucerna", 196, family="UnifrakturMaguntia", anchor="middle")
p.text(975, 330, "西班牙语周报　VOL.3　LA HUELGA　LA CAMPAÑA　LA ROJA", 36, "serif", True, OLIVE, anchor="middle", spacing=11.5)
p.text(975, 372, "西班牙语正文　简体中文讲解 — 给简体中文读者的版本", 16, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 420, OLIVE, 2)
moth(p, 975, 420)

# band
p.rect(MX, 470, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 30, 524, "¡EL VIERNES 13 EMPIEZA LA CAMPAÑA!", 46, "sans", True, ONCLOTH)
p.text(MX + 30, 568, "Faltan 20 días para el 29-N: el miércoles 11, huelga general de 24 horas.", 25, "serif", False, "#cac8ba")
p.text(RIGHT - 30, 524, "周五13日竞选开始　周三11日大罢工", 27, "sans", True, GOOSE, anchor="end")
p.text(RIGHT - 30, 568, "本期头条　详见第2、6版", 18, "sans", False, GOOSE, anchor="end")

# ---- headline (span cols 0-2) ----
hy = 590
p.text(MX, hy + 26, "LA NOTICIA　头条", 17, "sans", True, OLIVE)
hy = p.para(MX, hy + 92, "Del 11-N a la campaña: España vota en 20 días", 53, "serif", True, INK, 1323, 1.06)
p.text(MX, hy + 28, "De la redacción de La Lucerna　Nivel de lectura: A2", 17, "sans", False, GREY)
hy += 48
f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], hy, 1828, tag="P1-headline")
f.para("España entra en su semana más intensa antes de las elecciones. El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral.")
f.para("El domingo 29 de noviembre, España vota en elecciones generales. La campaña dura quince días: del viernes 13 al viernes 27 de noviembre. El sábado 28 es la jornada de reflexión, sin actos de campaña.")
f.para("¿Por qué esta semana decide tanto? Porque la vivienda sigue siendo el primer problema del país: según el Barómetro de Vivienda del CIS, el 91,4 % pide más vivienda pública (página 6).")
f.para("Y el que quiera votar por correo tiene que pedirlo antes del jueves 19: la documentación llega a casa desde el lunes 9 (página 2).")
f.para("El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45.")
f.para("Esta es la tercera edición de La Lucerna en español: cada semana, la España real contigo. ¡Bienvenidos!")
f.bridge("讲解｜la huelga general 大罢工 · la campaña electoral 竞选活动 · el voto por correo 邮寄投票 · la jornada de reflexión 投票前静默日。")
f.box("LA SEMANA EN CIFRAS　数字看本周", [
    ("20 — días faltan el lunes 9 para las elecciones del domingo 29（距 29 日大选 20 天）", "serif", False, INK, 20.5, 1.35),
    ("24 — horas dura la huelga general del miércoles 11 de noviembre（11 月 11 日大罢工持续 24 小时）", "serif", False, INK, 20.5, 1.35),
    ("91,4 — % que pide más vivienda pública, según el CIS de octubre（CIS 住房晴雨表数据）", "serif", False, INK, 20.5, 1.35),
])
f.head("AHORA TÚ　即学即练", 25)
f.ex("A2", "完成句子", "13", "竞选 11 月 13 日周五开始",
     "La campaña electoral empieza el viernes ___ de noviembre.", size=20.5)
f.ex("A2", "完成句子", "11", "大罢工在 11 月 11 日周三",
     "La huelga general es el miércoles ___ de noviembre.", size=20.5)
f.ex("A2", "完成句子", "29", "大选在 11 月 29 日周日",
     "España vota en elecciones generales el domingo ___ de noviembre.", size=20.5)
f.ex("A2", "完成句子", "19", "邮寄投票须在 19 日前申请",
     "El voto por correo se pide antes del jueves ___ de noviembre.", size=20.5)
f.ex("B1", "完成句子", "20:45", "西班牙–英格兰周日 20:45 开球",
     "El España–Inglaterra del domingo se juega a las ___.", size=20.5)
f.ex("B1", "完成句子", "15", "竞选持续 15 天",
     "La campaña electoral dura ___ días.", size=20.5)
f.end_report()

# ---- claves de la semana (col 3) ----
gx, gw = COLX[3], CW
gy = 588
p.rect(gx, gy, gw, 700, fill=BOX)
p.text(gx + 22, gy + 40, "CINCO", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 76, "CLAVES", 27, "sans", True, OLIVE)
p.text(gx + 22, gy + 106, "本周五大看点　Para entender la semana", 19, "sans", False, GREY)
gt = [
    ("La huelga del 11-N", 250),
    ("La campaña del 13", 226),
    ("El voto por correo", 196),
    ("La Roja: Praga e Inglaterra", 158),
    ("San Martín y el veranillo", 122),
]
byy = gy + 150
for i, (lab, bw) in enumerate(gt):
    p.text(gx + 22, byy + 22, f"{i+1}. {lab}", 21.5, "serif", True, INK)
    p.rect(gx + 22, byy + 34, bw, 22, fill=OLIVE)
    byy += 92
p.text(gx + 22, byy + 16, "Cinco claves, sin números", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 42, "inventados: todo está explicado", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 68, "en esta edición.", 18.5, "sans", False, GREY)
p.text(gx + 22, byy + 102, "五大看点，不编数字：全在本期里讲清。", 19, "sans", False, GREY)

# ---- sommaire (col 3) ----
sy = 1312
p.rect(gx, sy, gw, 340, fill="#f0eee5")
p.text(gx + 22, sy + 40, "EN ESTA EDICIÓN　本期目录", 24, "sans", True, OLIVE)
som = [
    ("Pág. 2", "El miércoles 11, huelga", "A2"),
    ("Pág. 3", "San Martín y el otoño", "A2→B1"),
    ("Pág. 4", "Praga y el domingo", "B1"),
    ("Pág. 5", "Votar desde casa", "B1"),
    ("Pág. 6", "La vivienda decide", "B2"),
    ("Pág. 7", "Fechas y promesas", "A2→B2"),
    ("Pág. 8", "Ejercicios y respuestas", "todos"),
]
yy = sy + 84
for pg, t, lv in som:
    p.text(gx + 22, yy, pg, 21, "sans", True, OLIVE)
    p.text(gx + 88, yy, t, 20, "serif", False, INK)
    p.text(gx + gw - 22, yy, lv, 18, "sans", True, OLIVE, anchor="end")
    yy += 40

# ---- word of the week (col 3) ----
my = 1652
p.text(gx, my + 24, "LA PALABRA DE LA SEMANA", 22, "sans", True, OLIVE)
p.hline(gx, gx + gw, my + 38, OLIVE, 2)
p.text(gx, my + 76, "« la huelga general »", 21.5, "serif", False, INK, italic=True)
wy = p.para(gx, my + 108, "todos paran a la vez, un día entero.", 21.5, "serif", False, INK, gw, 1.4)
p.para(gx, wy + 10, "“大罢工”：全体劳动者同一天停工 24 小时。", 19, "sans", False, GREY, gw, 1.35)

# ---- row B ----
p.hline(MX, RIGHT, 1844, LINE, 1.2)
iy = 1874
ix, iw = span_x(0, 2)
p.rect(ix, iy, iw, 320, fill=BOX)
illus_voto(p, ix + 240, iy + 30, s=1.7)
caption(p, ix, iy + 320, iw,
        "La urna y el sobre: votar por correo o en persona, el 29 de noviembre España decide. En la página 2, cómo pedir el voto por correo antes del jueves 19, y en la página 6, los datos del CIS sobre la vivienda. (Ilustración de la redacción, no una fotografía)",
        "Ilustración: La Lucerna")
# col 2 mini feature
f2 = Flow(p, [(COLX[2], CW)], 1874, 2300, tag="P1-otono")
f2.head("UNA SEMANA, DOS ESPAÑAS", 25)
f2.para("El miércoles, la calle en huelga; el viernes, la campaña en marcha. El domingo, el Metropolitano con la Roja. Entre medias, San Martín y su veranillo: esta semana España vive a la vez su protesta y su fiesta.", 22.5)
f2.para("Nuestro consejo para esta semana: lee el programa, no solo el titular. En la página 6 te enseñamos cómo.", 22.5)
f2.end_report()
# col 3 BREVES
bx = COLX[3]
p.rect(bx, 1874, CW, 416, fill=BOX)
p.text(bx + 22, 1914, "BREVES　快讯", 24, "sans", True, OLIVE)
brefs = [
    ("LA HUELGA", "El miércoles 11, huelga de 24 horas en todo el país. (Página 2)"),
    ("LA ROJA", "Jueves: Chequia–España. Domingo: España–Inglaterra. (Página 4)"),
    ("SAN MARTÍN", "El miércoles 11 es San Martín: castañas y veranillo. (Página 3)"),
]
byy = 1944
for h, b in brefs:
    p.text(bx + 22, byy + 22, h, 20, "sans", True, OLIVE)
    byy = p.para(bx + 22, byy + 50, b, 20, "serif", False, INK, CW - 44, 1.36) + 8

# ---- lightning quiz ----
qy = 2312
p.hline(MX, RIGHT, qy, OLIVE, 2)
p.text(MX, qy + 36, "QUIZ RELÁMPAGO　闪电问答", 26, "sans", True, OLIVE)
p.text(RIGHT, qy + 36, "读头版，选出正确答案　答案见第8版", 20, "sans", False, GREY, anchor="end")
qf = Flow(p, [(COLX[i], CW) for i in range(4)], qy + 54, 2560, tag="P1-quiz")
qf.ex("A2", "单选", "C", "大选在 11 月 29 日",
      "Las elecciones generales son el... A. 11 de noviembre · B. 13 de noviembre · C. 29 de noviembre", size=21)
qf.ex("A2", "单选", "B", "大罢工持续 24 小时",
      "La huelga general del miércoles dura... A. una hora · B. 24 horas · C. una semana", size=21)
qf.ex("A2", "单选", "A", "竞选 11 月 13 日开始",
      "La campaña electoral empieza el... A. viernes 13 · B. lunes 9 · C. domingo 15", size=21)
qf.ex("A2", "单选", "B", "西班牙–英格兰周日 20:45",
      "El España–Inglaterra se juega el domingo a las... A. 15:30 · B. 20:45 · C. 18:30", size=21)
qf.end_report()
p.foot(1)
p.save(f"{OUT}/p1-portada.svg")
print("P1 saved, exercises so far:", len(REG))

# ================= P2 · VIDA (A2) =================
CURPAGE[0] = 2
p = BSPage4()
p.band("VIDA　生活", "La Lucerna", "NIVEL A2　El miércoles 11, huelga general　11月11日周三大罢工")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P2-feature")
f.title("El miércoles 11: huelga general de 24 horas", 32)
f.byline("De la redacción de La Lucerna　Nivel de lectura: A2")
f.para("El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos.")
f.para("La convocan Comisiones Obreras (CCOO) y la Unión General de Trabajadores (UGT), junto con la Confederación General del Trabajo (CGT), la Confederación Nacional del Trabajo (CNT) y la Confederación de Sindicatos de Inquilinas, entre otras organizaciones. El lema es «Salarios, vivienda y precios».")
f.para("¿Qué piden? Subir los salarios, bajar el precio de la vivienda, regular el alquiler y frenar la subida de los precios. La huelga llega dos días antes de que empiece la campaña electoral, el viernes 13.")
f.para("En un día de huelga, no todo se para igual: hay servicios mínimos en el transporte y en la sanidad. Los servicios mínimos de esta huelga se anuncian antes del miércoles: consulta los avisos de tu ciudad y de tu empresa.")
f.box("EL CALENDARIO　本周日历", [
    ("Lunes 9 — la selección se concentra en Las Rozas; la documentación del voto por correo empieza a llegar a casa（周一国家队集结；邮寄选票材料开始寄出）", "serif", False, INK, 21, 1.36),
    ("Martes 10 — último día de calma antes de la huelga: los sindicatos ultiman los servicios mínimos（周二罢工前最后准备日）", "serif", False, INK, 21, 1.36),
    ("Miércoles 11 — huelga general de 24 horas; San Martín, castañas y vino nuevo（周三大罢工；圣马丁节）", "serif", False, INK, 21, 1.36),
    ("Jueves 12 — Liga de Naciones: Chequia–España, 20:45, en Praga（周四欧国联：捷克对西班牙）", "serif", False, INK, 21, 1.36),
    ("Viernes 13 — a las 00:00 empieza la campaña electoral del 29-N（周五零点竞选正式开始）", "serif", False, INK, 21, 1.36),
    ("Sábado 14 — final de la Copa Federación en Sestao, 19:00（周六联邦杯决赛在塞斯陶）", "serif", False, INK, 21, 1.36),
    ("Domingo 15 — Liga de Naciones: España–Inglaterra, 20:45, en el Metropolitano（周日欧国联：西班牙对英格兰）", "serif", False, INK, 21, 1.36),
])
f.head("DECIR LA FECHA", 25)
f.para("En español, la fecha se dice así: «el miércoles 11 de noviembre». Primero el día de la semana, luego el número y luego el mes. Los días y los meses van en minúscula: miércoles, noviembre. Y ojo: el primero del mes no es «el primero», es «el uno»: el 1 de noviembre.", 23)
f.gloss("la huelga 罢工 · el sindicato 工会 · el salario 工资 · el alquiler 租金 · los servicios mínimos 最低服务保障。")
f.end_report()

# col 3: facts + ¿Y tú? (sequential, measured)
ix = COLX[3]
facts = ["La huelga del miércoles 11 dura 24 horas y llega a todo el país.",
         "La convocan CCOO, UGT, CGT, CNT y los sindicatos de inquilinas.",
         "El lema es «Salarios, vivienda y precios»: tres palabras, tres problemas."]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "¿SABÍAS QUE…?", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "¿Y tú? ¿Qué harías el miércoles 11: vas a la huelga, trabajas o te quedas en casa? ¿Qué te preocupa más: el salario, la vivienda o los precios? Escribe dos frases en español y envíalas a la redacción: las mejores salen en la página 7, «Cartas de los lectores»."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("11 月 11 日周三你做什么：罢工、上班还是待在家里？你最担心什么：工资、住房还是物价？写两句西班牙语寄给编辑部。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "¿Y TÚ?　说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "11 月 11 日周三你做什么：罢工、上班还是待在家里？你最担心什么：工资、住房还是物价？写两句西班牙语寄给编辑部。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P2 col3 ends", ey3 + eh)

# ---- Decir la fecha wide box ----
dy = 1566
p.hline(MX, RIGHT, dy - 12, OLIVE, 2)
p.text(MX, dy + 28, "LOS DÍAS DE LA SEMANA　这样说日期", 28, "sans", True, OLIVE)
p.text(RIGHT, dy + 28, "lunes 9 – domingo 15 de noviembre　11月9日周一至15日周日", 20, "sans", False, GREY, anchor="end")
lx = MX
ly = dy + 58
for d, t in [
    ("lunes 9", "el lunes 9 — la Roja se concentra en Las Rozas"),
    ("martes 10", "el martes 10 — antes de la huelga"),
    ("miércoles 11", "el miércoles 11 — huelga general, 24 horas"),
    ("jueves 12", "el jueves 12 — Chequia–España, 20:45"),
]:
    p.text(lx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(lx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
ly = dy + 58
rx = MX + 910
for d, t in [
    ("viernes 13", "el viernes 13 — empieza la campaña, 00:00"),
    ("sábado 14", "el sábado 14 — Copa Federación, 19:00"),
    ("domingo 15", "el domingo 15 — España–Inglaterra, 20:45"),
]:
    p.text(rx, ly + 24, d, 24, "serif", True, OLIVE)
    p.text(rx + 240, ly + 24, t, 21, "sans", False, GREY)
    ly += 36
p.para(lx, dy + 226, "Ojo: los días de la semana y los meses van en minúscula en español — miércoles, noviembre — y el 1 del mes es «el uno», no «el primero».", 20.5, "serif", False, INK, RIGHT - lx, 1.42)

# ---- P2 exercises ----
ey = dy + 282
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "EJERCICIOS　第2版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P2-ex")
e.head("A　LAS FECHAS", 25)
e.bridge("用正确的日期形式补全句子。")
e.ex("A2", "完成句子", "11", "11 月 11 日周三",
     "La huelga general es el miércoles ___ de noviembre.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "15", "11 月 15 日周日",
     "El España–Inglaterra se juega el domingo ___ de noviembre.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "29", "大选在 11 月 29 日",
     "Las elecciones generales son el ___ de noviembre.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "uno", "每月 1 号说 el uno",
     "El Día de Todos los Santos fue el ___ de noviembre.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "noviembre", "月份小写",
     "El miércoles 11 de ___ hay huelga general.", instr="填空", size=20, gap=8)
e.head("B　EL PRESENTE", 25)
e.bridge("补全动词的现在时形式。")
e.ex("A2", "完成句子", "piden", "los sindicatos → piden",
     "Los sindicatos ___ subir los salarios.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "dura", "la huelga → dura",
     "La huelga ___ 24 horas.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "empieza", "la campaña → empieza",
     "La campaña ___ el viernes 13.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "convocan", "CCOO y UGT → convocan",
     "CCOO y UGT ___ la huelga general.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "llega", "la documentación → llega",
     "La documentación del voto por correo ___ desde el lunes 9.", instr="填空", size=20, gap=8)
e.head("C　COMPRENSIÓN", 25)
e.bridge("读第 2 版文章，选出正确答案。")
e.ex("A2", "单选", "B", "大罢工在 11 月 11 日周三",
     "¿Cuándo es la huelga general? A. el lunes 9 · B. el miércoles 11 · C. el viernes 13", size=20, gap=8)
e.ex("A2", "单选", "A", "罢工口号是工资、住房、物价",
     "El lema de la huelga es... A. «Salarios, vivienda y precios» · B. «Fútbol y fiesta» · C. «Cine y series»", size=20, gap=8)
e.ex("A2", "单选", "C", "罢工后两天竞选开始",
     "La campaña empieza... A. antes de la huelga · B. el mismo día · C. dos días después de la huelga", size=20, gap=8)
e.ex("B1", "单选", "B", "罢工日有最低服务保障",
     "En un día de huelga hay... A. fiesta total · B. servicios mínimos · C. vacaciones", size=20, gap=8)
e.head("D　LAS PALABRAS", 25)
e.match_set("A2", "词汇配对",
            ["la huelga", "el sindicato", "el salario", "el alquiler"],
            ["lo que se paga por trabajar",
             "una organización de trabajadores",
             "un paro de todos los trabajadores",
             "lo que se paga por vivir en un piso"],
            ["c", "b", "a", "d"],
            ["huelga=罢工 c", "sindicato=工会 b", "salario=工资 a", "alquiler=租金 d"],
            instr="把词和释义配对")
e.end_report()
p.foot(2)
p.save(f"{OUT}/p2-vida.svg")
print("P2 saved, exercises so far:", len(REG))
