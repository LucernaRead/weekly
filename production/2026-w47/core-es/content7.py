# -*- coding: utf-8 -*-
# W47 ES core (VOL.4) — P7 language focus. Fresh text; golden sentences verbatim from P1–P6.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA　语言", "La Lucerna", "语言聚焦　Tres niveles, tres herramientas　三个级别，三件工具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　LA HORA", 24)
a.para("Para decir la hora: «Es la una» en singular, «Son las dos» en plural. Para los minutos: «Son las 20:45» o «las nueve menos cuarto». Y el partido se juega «a las 21:00»: con la preposición a.", 21.5)
a.para("Y ojo con la fecha: «el lunes 16 de noviembre», con el mes en minúscula y el 1 como «el uno».", 21.5)
a.bridge("时间：es la una（单数）、son las dos（复数）；比赛在 a las 21:00 开球。")
a.ex("A2", "完成句子", "Es", "1 点用单数 Es",
     "___ la una en punto.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "Son", "多点用复数 Son",
     "___ las nueve de la noche.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "las", "a las 21:00（介词 a）",
     "El derbi es el sábado a ___ 18:30.", instr="填空", size=20.5, gap=10)
a.ex("A2", "单选", "B", "1 点说 Es la una",
     "¿Cómo se dice la 1:00? A. Son la una · B. Es la una · C. Es las una", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　COMPARATIVOS", 24)
b.para("Para comparar: más / menos + adjetivo + que; tan + adjetivo + como. Dos irregulares para recordar: bueno → mejor, malo → peor. Y nunca «más mejor»: mejor ya es comparativo.", 21.5)
b.para("El fútbol de esta semana sirve para practicar: más goles que, tan rápido como, mejor que, peor que.", 21.5)
b.bridge("比较级 más…que、tan…como；bueno→mejor、malo→peor；绝不说 más mejor。")
b.ex("B1", "完成句子", "más goles", "más + goles（进球更多）",
     "El Barça marca ___ que el año pasado. (goles)", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "tan rápido", "tan + rápido + como（同样快）",
     "El derbi es ___ como siempre. (rápido)", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "mejor", "bueno 的比较级是 mejor（不用 más）",
     "Un debate claro es ___ (bueno) que un titular.", instr="填空", size=20.5, gap=10)
b.ex("B1", "单选", "B", "más mejor 是错误说法",
     "¿Qué forma es correcta? A. más mejor · B. mejor · C. muy mejor", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　EL SUBJUNTIVO", 24)
c.para("Los debates usan el subjuntivo: «es necesario que», «para que», «ojalá» van con subjuntivo — tenga, sea, baje. Pero «creo que» afirma y va con indicativo: creo que es.", 21.5)
c.para("Es la gramática de la página 6: opinar sobre debates y programas sin afirmar más de lo que sabemos.", 21.5)
c.bridge("es necesario que、para que、ojalá 后用虚拟式；creo que 后用陈述式。")
c.ex("B2", "完成句子", "baje", "es necesario que + 虚拟式 baje",
     "Es necesario que el precio ___ (bajar).", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "sea", "para que + 虚拟式 sea",
     "Publicamos la fuente para que todo ___ (ser) claro.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "es", "creo que + 陈述式 es",
     "Creo que el debate ___ (ser) útil.", instr="填空", size=20.5, gap=10)
c.ex("B2", "单选", "B", "ojalá + 虚拟式：tenga",
     "«Ojalá que el debate...» A. tiene datos · B. tenga datos · C. tener datos", size=20.5, gap=10)
c.end_report()

# ---- col 3: manuscript image + errores + palabra + lectores ----
bx = COLX[3]
image(p, "book_hours.jpg", bx, 200, CW, 120)
cy3 = caption(p, bx, 320, CW, "Un libro de horas medieval: letras decoradas que abrían la oración.",
              "Manuscrito medieval — dominio público")
errs = [
    ("«Son la una en punto.»", "→ «Es la una.» Es singular.", "一点是单数，动词用 es。"),
    ("«El derbi es más mejor.»", "→ «Es mejor.» Sin más.", "mejor 本身就是比较级，不加 más。"),
    ("«La gente votan el 29.»", "→ «La gente vota.» Es singular.", "gente 是单数集合名词，动词用单数。"),
    ("«Creo que el debate sea útil.»", "→ «Creo que el debate es útil.»", "creo que 表肯定，用陈述式 es。"),
]
ey0 = cy3 + 24
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, ey0, CW, eh, fill=BOX)
yy3 = ey0 + 16
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS　常见错误", 23, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = ey0 + eh + 16
wt = "« el debate » es la discusión con turnos: cuatro portavoces el viernes 13; el lunes 16, un cara a cara propuesto."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("debate = 辩论：公开讨论，有轮次。本期是辩论周；大选 29 日。", "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA　本周生词", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "debate = 辩论：公开讨论，有轮次。本期是辩论周；大选 29 日。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Marta, estudio español en Pekín. El lunes 16 escucho flamenco y el sábado veo el derbi. ¡Gracias por el periódico!» — Marta （ejemplo, escrito por la redacción）"
ld = "Nota de la redacción: sin cartas reales ni mejores textos al cierre, publicamos este ejemplo; la promesa pasa al VOL.5."
ldcn = "编辑部说明：截稿时未收到真实来信与最佳作文，本期登载编辑部示例信，承诺顺延至 VOL.5。欢迎来信！"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20, CW - 44)) * 29 + 10 + len(wrap(ldcn, "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, ld, 20, "serif", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, ldcn, 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = ly + lh + 35
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA　本周金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)
quotes = [
    ("«La campaña electoral empezó el viernes 13, a las 00:00, y dura quince días: hasta el viernes 27 de noviembre.»", "竞选 13 日零点开始，持续 15 天，到 27 日。", "Página 1"),
    ("«El jueves 19 es un día clave: termina el plazo para pedir el voto por correo.»", "周四 19 日是关键日：邮寄投票申请截止。", "Página 2"),
    ("«El lunes 16 de noviembre es el Día Internacional del Flamenco, y en España suena la guitarra en todos los rincones.»", "11 月 16 日周一是国际弗拉门戈日，吉他声响遍西班牙。", "Página 3"),
    ("«No es solo un baile: es cante, toque y baile, con palmas, taconeo y compás.»", "弗拉门戈不只是舞蹈：歌、琴、舞、击掌、踏脚与节拍。", "Página 3"),
    ("«La Liga se para y vuelve: después del parón de selecciones, la jornada 13 se juega del viernes 20 al lunes 23 de noviembre.»", "联赛停摆又回归：第 13 轮 11 月 20 日周五踢到 23 日周一。", "Página 4"),
    ("«¿Votas por primera vez el 29 de noviembre? Tienes dos maneras de votar: en persona o por correo.»", "11 月 29 日你第一次投票吗？两种方式：亲自去或邮寄。", "Página 5"),
    ("«En campaña, no todo lo que se anuncia está cerrado.»", "竞选期间，不是所有宣布的事都已确定。", "Página 6"),
    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "一次民调就是一张带误差的照片，拍于某一天。", "Página 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 128
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = fy + 66 + 3 * 128 + 105 + 30
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA　下期预告 (VOL.5)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "El domingo 29, España vota: los resultados, el Black Friday y la jornada 5 de la Champions. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
