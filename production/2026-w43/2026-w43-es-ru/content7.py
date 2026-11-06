# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-es-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA · Язык", "La Lucerna", "Tres niveles, tres herramientas · Три уровня, три инструмента")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · DECIR LA HORA Y EL PRESENTE", 24)
a.para("Para decir la hora: «Es la una», pero «Son las dos, las tres…». «Y media» es +30 minutos (2:30); «menos cuarto», −15 (2:45).", 21.5)
a.para("Y ojo con dormir: el presente cambia la vocal — duermo, duermes, duerme… pero dormimos, dormís. Despertarse es reflexivo: me despierto, se despierta.", 21.5)
a.expl("Только для одного часа — es; dormir спрягается нерегулярно; despertarse — возвратный глагол.")
a.ex("A2", "Дополните предложение", "Son", "в десять часов говорят Son (Es — только для la una)",
     "___ las diez de la noche. Empieza la película.", instr="Вставьте слово", size=20.5, gap=10)
a.ex("A2", "Дополните предложение", "duerme", "dormir: él → duerme (o→ue)",
     "Mi hermano ___ (dormir) hasta las once el domingo.", instr="Вставьте слово", size=20.5, gap=10)
a.ex("A2", "Дополните предложение", "se despierta", "despertarse: ella → se despierta",
     "Ella ___ (despertarse) a las ocho.", instr="Вставьте слово", size=20.5, gap=10)
a.ex("A2", "Выбор ответа", "B", "y media = 30 минут",
     "«Son las dos y media» son las... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · COMPARATIVOS Y PASADO", 24)
b.para("Para comparar: más / menos + adjetivo + que. Dos irregulares para recordar: bueno → mejor, malo → peor.", 21.5)
b.para("Para contar el martes de Champions usamos el pretérito indefinido: ganó, marcó, perdió, cortó. Es el tiempo de los resultados y de las crónicas.", 21.5)
b.expl("Сравнительная степень: más…que; bueno→mejor и malo→peor — нерегулярные; о результатах говорят в indefinido.")
b.ex("B1", "Дополните предложение", "más importante", "más + прилагательное (сравнение)",
     "El Clásico es ___ que un partido normal. (importante)", instr="Вставьте слово", size=20.5, gap=10)
b.ex("B1", "Дополните предложение", "peor", "сравнительная степень от malo — peor",
     "Fue la ___ (malo) noche del Barça esta temporada.", instr="Вставьте слово", size=20.5, gap=10)
b.ex("B1", "Дополните предложение", "marcó", "indefinido от marcar: marcó",
     "Doué ___ (marcar) el primer gol en París.", instr="Вставьте слово", size=20.5, gap=10)
b.ex("B1", "Выбор ответа", "B", "Вильярреал проиграл 4–3",
     "El Villarreal en Liverpool... A. ganó 4–3 · B. perdió 4–3 · C. empató 0–0", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · CREO QUE… / NO CREO QUE…", 24)
c.para("Con «creo que» afirmamos: va el indicativo — «Creo que el Clásico es el domingo». Con «no creo que», con dudas y con «es importante que» va el subjuntivo: tenga (tener), sea (ser), llueva (llover).", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas sin afirmar más de lo que sabemos.", 21.5)
c.expl("После creo que — изъявительное; после no creo que и es importante que — сослагательное (tenga/sea/llueva).")
c.ex("B2", "Дополните предложение", "es", "creo que + изъявительное: es",
     "Creo que el Clásico ___ (ser) el domingo.", instr="Вставьте слово", size=20.5, gap=10)
c.ex("B2", "Дополните предложение", "sea", "no creo que + сослагательное: sea",
     "No creo que el gráfico ___ (ser) completo sin la fuente.", instr="Вставьте слово", size=20.5, gap=10)
c.ex("B2", "Дополните предложение", "tenga", "es importante que + сослагательное: tenga",
     "Es importante que cada encuesta ___ (tener) su fecha.", instr="Вставьте слово", size=20.5, gap=10)
c.ex("B2", "Выбор ответа", "B", "es posible que + сослагательное: llueva",
     "«Es posible que el domingo...» A. llueve · B. llueva · C. llover", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«Es las tres.»", "→ «Son las tres.» Solo «la una» usa es; las demás horas usan son.", "Только «la una» — с es; остальные — son."),
    ("«Hoy soy muy aburrido.»", "→ «Hoy estoy muy aburrido.» Estado de hoy: estar. Ser aburrido = ser una persona aburrida.", "Сегодня — estar; ser aburrido = скучный."),
    ("«Me gusta los libros.»", "→ «Me gustan los libros.» Gustar cambia con la cosa: gusta / gustan.", "Gustar — по вещи: gusta / gustan."),
    ("«La gente son felices.»", "→ «La gente es feliz.» Gente es singular, como un solo grupo.", "Gente — собирательное, ед. число."),
]
# 盒高 = 绘制循环精确模拟（2026-10-21 回补：原平均行高公式系统性低估 206.5，第四条被下方盒覆盖；修法与 ES×EN 版一致）
_sim = 216 + 44
for _w, _r, _n in errs:
    _sim += 17 + len(wrap(_w, "serif", True, 21.5, CW - 44)) * 21.5 * 1.36 \
          + 17 + len(wrap(_r, "serif", False, 20.5, CW - 44)) * 20.5 * 1.36 \
          + 16 + len(wrap(_n, "sans", False, 19.5, CW - 44)) * 19.5 * 1.36 + 4
eh = _sim - 200 + 12
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · Ошибки", 23, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« empatar » es terminar igual: en un partido, no ganar ni perder. Esta semana la palabra vive dos veces: el Atlético empató en Stuttgart — ¡y Alonso y Sainz llegan empatados a Austin, con los mismos puntos!"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("empatar = сыграть вничью. Дважды на неделе: «Атлетико» и Алонсо—Сайнс.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA · Слово недели", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "empatar = сыграть вничью. Дважды на неделе: «Атлетико» и Алонсо—Сайнс.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Mei y estudio español en Pekín. El domingo voy a ver el Clásico con mis amigos — y antes, a dormir una hora más. ¡Gracias por el periódico!» — Mei （carta de ejemplo, escrita por la redacción）"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Образец от редакции, не письмо читателя. В VOL.2 — ваши письма!", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Образец от редакции, не письмо читателя. В VOL.2 — ваши письма!", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA · Фразы недели (дословно из статей этого выпуска)", 27, "sans", True, OLIVE)
quotes = [
    ("«La noche tiene 25 horas y dormimos una hora más.»", "Ночь длится 25 часов, и мы спим на час дольше.", "Страница 1"),
    ("«En Canarias hay una hora menos que en la Península»", "На Канарах на час раньше, чем на полуострове.", "Страница 2"),
    ("«El sistema sigue — si la ley europea no cambia.»", "Система остаётся — если не изменится европейский закон.", "Страница 2"),
    ("«El PSG ganó 4–2 en París: fue la primera derrota azulgrana de la temporada.»", "ПСЖ выиграл в Париже 4–2: первое поражение «Барсы» в этом сезоне.", "Страница 4"),
    ("«España se divide en dos: unos hacen puente y otros, no.»", "Испания делится на две части: одна устраивает пуэнте, другая — нет.", "Страница 3"),
    ("«En Cataluña, la Castanyada: castañas asadas, boniatos y panellets, unos dulces pequeños de mazapán.»", "В Каталонии на Кастаньяду едят жареные каштаны, сладкий картофель и panellets — маленькие марципановые печенья.", "Страница 3"),
    ("«La camiseta se estrena primero con el equipo femenino, el sábado 24»", "Футболка дебютирует сначала у женской команды, в субботу 24-го.", "Страница 5"),
    ("«Publicamos las dos series con su fuente y su fecha, una junto a otra — y no las mezclamos nunca en un solo número.»", "Мы публикуем оба ряда с источником и датой рядом — и никогда не смешиваем их в одно число.", "Страница 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- próxima semana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA · На следующей неделе (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "El jueves 29: los actos de memoria de la DANA en Valencia. El sábado 31: Halloween, la Castanyada y el Samaín. El domingo 1: Todos los Santos — y el lunes 2, el puente en nueve comunidades. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
