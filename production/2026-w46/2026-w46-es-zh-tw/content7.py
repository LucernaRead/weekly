# -*- coding: utf-8 -*-
# W46 ES core (VOL.3) — P7 language focus. Fresh text; golden sentences verbatim from P1–P6.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-es-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA · 語言", "La Lucerna", "語言聚焦 · Tres niveles, tres herramientas · 三個級別，三件工具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · LAS FECHAS", 24)
a.para("Para decir la fecha: «el miércoles 11 de noviembre». Primero el día, luego el número y luego el mes. Los días y los meses van en minúscula: miércoles, noviembre.", 21.5)
a.para("Y ojo con el 1: el primer día del mes es «el uno», no «el primero»: el 1 de noviembre, el Día de Todos los Santos.", 21.5)
a.expl("日期格式：el miércoles 11 de noviembre；星期、月份小寫；1 號說 el uno。")
a.ex("A2", "完成句子", "11", "el miércoles 11 de noviembre 大罷工",
     "La huelga general es el miércoles ___ de noviembre.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "uno", "el 1 = el uno",
     "Todos los Santos es el ___ de noviembre.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "domingo", "15 日是週日",
     "El España–Inglaterra es el ___ 15 de noviembre.", instr="填空", size=20.5, gap=10)
a.ex("A2", "單選", "B", "月份小寫：noviembre",
     "¿Cómo se escribe el mes? A. Noviembre · B. noviembre · C. NOVIEMBRE", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · COMPARATIVOS", 24)
b.para("Para comparar: más / menos + adjetivo + que; tan + adjetivo + como. Dos irregulares para recordar: bueno → mejor, malo → peor. Y nunca «más mejor»: mejor ya es comparativo.", 21.5)
b.para("La vivienda de esta semana sirve para practicar: más cara que, tan alta como, mejor que, peor que.", 21.5)
b.expl("比較級 más…que、tan…como；bueno→mejor、malo→peor；絕不說 más mejor。")
b.ex("B1", "完成句子", "más cara", "más + cara（房價更高）",
     "La vivienda es ___ que hace un año. (cara)", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "tan alta", "tan + alta + como（同樣高）",
     "La preocupación es ___ como en octubre. (alta)", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "mejor", "bueno 的比較級是 mejor（不用 más）",
     "Un programa claro es ___ (bueno) que un titular.", instr="填空", size=20.5, gap=10)
b.ex("B1", "單選", "B", "más mejor 是錯誤說法",
     "¿Qué forma es correcta? A. más mejor · B. mejor · C. muy mejor", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · EL SUBJUNTIVO", 24)
c.para("Las promesas usan el subjuntivo: «es necesario que», «para que», «ojalá» van con subjuntivo — tenga, sea, baje. Pero «creo que» afirma y va con indicativo: creo que es.", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas y programas sin afirmar más de lo que sabemos.", 21.5)
c.expl("es necesario que、para que、ojalá 後用虛擬式；creo que 後用陳述式。")
c.ex("B2", "完成句子", "baje", "es necesario que + 虛擬式 baje",
     "Es necesario que el precio ___ (bajar).", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "sea", "para que + 虛擬式 sea",
     "Publicamos la fuente para que todo ___ (ser) claro.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "es", "creo que + 陳述式 es",
     "Creo que la vivienda ___ (ser) el tema del 29-N.", instr="填空", size=20.5, gap=10)
c.ex("B2", "單選", "B", "ojalá + 虛擬式：baje",
     "«Ojalá que el precio...» A. baja · B. baje · C. bajar", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«El domingo 15 son el partido.»", "→ «El domingo 15 es el partido.» El domingo es singular: es, no son.", "domingo 是單數，動詞用 es。"),
    ("«La vivienda es más mejor.»", "→ «La vivienda es mejor.» Mejor ya es comparativo: sin más.", "mejor 本身就是比較級，不加 más。"),
    ("«La gente votan el 29.»", "→ «La gente vota el 29.» Gente es singular, como un solo grupo.", "gente 是單數集合名詞，動詞用單數。"),
    ("«Creo que la vivienda sea el tema.»", "→ «Creo que la vivienda es el tema.» Creo que afirma: indicativo.", "creo que 表肯定，用陳述式 es。"),
]
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · 常見錯誤", 23, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« la huelga general » es el paro de todos a la vez, un día entero: el miércoles 11, por los salarios, la vivienda y los precios."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("huelga general = 大罷工：全體勞動者同一天停工。本期就是罷工週；競選 13 日週五開始。", "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA · 本週生詞", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "huelga general = 大罷工：全體勞動者同一天停工。本期就是罷工週；競選 13 日週五開始。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Ana, estudio español en Shanghái. El miércoles 11 sigo la huelga en las noticias y el domingo veo el España–Inglaterra con mis amigos. ¡Gracias por el periódico!» — Ana （ejemplo, escrito por la redacción）"
ld = "Nota de la redacción: al cierre no había cartas reales ni los mejores textos de la página 8; publicamos este ejemplo y la promesa pasa al VOL.4."
ldcn = "編輯部說明：截至本期截稿，未收到真實讀者來信與第 8 版最佳作文，故本期登載編輯部示例信，承諾順延至 VOL.4。歡迎來信！"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(ld, "serif", False, 20, CW - 44)) * 29 + 10 + len(wrap(ldcn, "sans", False, 20, CW - 44)) * 29 + 42
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, ld, 20, "serif", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, ldcn, 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = ly + lh + 35
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA · 本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)
quotes = [
    ("«El miércoles 11 hay huelga general y el viernes 13, a las 00:00, empieza la campaña electoral.»", "週三 11 日有大罷工，週五 13 日零點競選開始。", "Página 1"),
    ("«El miércoles 11 de noviembre hay huelga general en toda España: un paro de 24 horas, convocado por los sindicatos.»", "11 月 11 日週三全西班牙大罷工：工會召集的 24 小時停工。", "Página 2"),
    ("«Cuenta la leyenda que Martín, soldado romano, partió su capa en dos con la espada para cubrir a un mendigo que moría de frío.»", "傳說羅馬士兵馬丁用劍把斗篷分成兩半，蓋住快凍死的乞丐。", "Página 3"),
    ("«España, vigente campeona del mundo y de Europa, juega en el grupo A3 con Croacia, Inglaterra y la República Checa.»", "現任世界冠軍和歐洲冠軍西班牙，與克羅地亞、英格蘭和捷克同在 A3 組。", "Página 4"),
    ("«No hace falta ir al colegio electoral para votar: el voto por correo llega a casa.»", "投票不必去投票站：郵寄選票送到家裡。", "Página 5"),
    ("«La vivienda preocupa al 86,9 % de los españoles.»", "住房讓 86.9% 的西班牙人擔心。", "Página 6"),
    ("«Una encuesta es una foto con margen de error, tomada en un día concreto.»", "一次民調就是一張帶誤差的照片，拍於某一天。", "Página 6"),
    ("«El domingo 15, la selección cierra la fase de grupos de la Liga de Naciones contra Inglaterra, en el Metropolitano, a las 20:45.»", "11 月 15 日週日，國家隊在大都會球場 20:45 對英格蘭，收官小組賽。", "Página 1"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 128
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = fy + 66 + 3 * 128 + 105 + 30
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA · 下期預告 (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "La primera semana de campaña, la jornada 13 de Liga y la vuelta de la Champions. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
