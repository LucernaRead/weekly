# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-es-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LENGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LENGUA · LANGUE", "La Lucerna", "Focus langue · Tres niveles, tres herramientas · Trois niveaux, trois outils")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · DECIR LA HORA Y EL PRESENTE", 24)
a.para("Para decir la hora: «Es la una», pero «Son las dos, las tres…». «Y media» es +30 minutos (2:30); «menos cuarto», −15 (2:45).", 21.5)
a.para("Y ojo con dormir: el presente cambia la vocal — duermo, duermes, duerme… pero dormimos, dormís. Despertarse es reflexivo: me despierto, se despierta.", 21.5)
a.expl("Seule « la una » prend es ; dormir change de radical ; despertarse est un verbe pronominal.")
a.ex("A2", "完成句子", "Son", "pour dix heures, Son (Es seulement avec la una)",
     "___ las diez de la noche. Empieza la película.", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "完成句子", "duerme", "dormir : él → duerme (o → ue)",
     "Mi hermano ___ (dormir) hasta las once el domingo.", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "完成句子", "se despierta", "despertarse: ella → se despierta",
     "Ella ___ (despertarse) a las ocho.", instr="Compléter", size=20.5, gap=10)
a.ex("A2", "单选", "B", "y media = 30 minutes",
     "«Son las dos y media» son las... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · COMPARATIVOS Y PASADO", 24)
b.para("Para comparar: más / menos + adjetivo + que. Dos irregulares para recordar: bueno → mejor, malo → peor.", 21.5)
b.para("Para contar el martes de Champions usamos el pretérito indefinido: ganó, marcó, perdió, cortó. Es el tiempo de los resultados y de las crónicas.", 21.5)
b.expl("Comparatif avec más … que ; bueno → mejor et malo → peor sont irréguliers ; les résultats se racontent au pretérito indefinido.")
b.ex("B1", "完成句子", "más importante", "más + adjectif (comparaison)",
     "El Clásico es ___ que un partido normal. (importante)", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "完成句子", "peor", "le comparatif de malo est peor",
     "Fue la ___ (malo) noche del Barça esta temporada.", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "完成句子", "marcó", "marcar au indefinido : marcó",
     "Doué ___ (marcar) el primer gol en París.", instr="Compléter", size=20.5, gap=10)
b.ex("B1", "单选", "B", "Villarreal a perdu 4–3",
     "El Villarreal en Liverpool... A. ganó 4–3 · B. perdió 4–3 · C. empató 0–0", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · CREO QUE… / NO CREO QUE…", 24)
c.para("Con «creo que» afirmamos: va el indicativo — «Creo que el Clásico es el domingo». Con «no creo que», con dudas y con «es importante que» va el subjuntivo: tenga (tener), sea (ser), llueva (llover).", 21.5)
c.para("Es la gramática de la página 6: opinar sobre encuestas sin afirmar más de lo que sabemos.", 21.5)
c.expl("Après creo que, l'indicatif ; après no creo que et es importante que, le subjonctif (tenga, sea, llueva).")
c.ex("B2", "完成句子", "es", "creo que + indicatif : es",
     "Creo que el Clásico ___ (ser) el domingo.", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "完成句子", "sea", "no creo que + subjonctif : sea",
     "No creo que el gráfico ___ (ser) completo sin la fuente.", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "完成句子", "tenga", "es importante que + subjonctif : tenga",
     "Es importante que cada encuesta ___ (tener) su fecha.", instr="Compléter", size=20.5, gap=10)
c.ex("B2", "单选", "B", "es posible que + subjonctif : llueva",
     "«Es posible que el domingo...» A. llueve · B. llueva · C. llover", size=20.5, gap=10)
c.end_report()

# ---- col 3: errores típicos + palabra + lectores ----
bx = COLX[3]
errs = [
    ("«Es las tres.»", "→ «Son las tres.» Solo «la una» usa es; las demás horas usan son.", "Seule la una prend es ; le reste, son."),
    ("«Hoy soy muy aburrido.»", "→ «Hoy estoy muy aburrido.» Estado de hoy: estar. Ser aburrido = ser una persona aburrida.", "État du jour : estar. Ser = ennuyeux."),
    ("«Me gusta los libros.»", "→ «Me gustan los libros.» Gustar cambia con la cosa: gusta / gustan.", "Gustar suit la chose : gusta / gustan."),
    ("«La gente son felices.»", "→ «La gente es feliz.» Gente es singular, como un solo grupo.", "gente : collectif, verbe au singulier."),
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
p.text(bx + 22, yy3 + 26, "ERRORES TÍPICOS · ERREURS TYPES", 20, "sans", True, OLIVE)
yy3 += 44
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 17, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 17, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 16, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 4
wy = 200 + eh + 16
wt = "« empatar » es terminar igual: en un partido, no ganar ni perder. Esta semana la palabra vive dos veces: el Atlético empató en Stuttgart — ¡y Alonso y Sainz llegan empatados a Austin, con los mismos puntos!"
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("empatar = faire match nul. Deux fois cette semaine : Stuttgart et Austin.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PALABRA · MOT DE LA SEMAINE", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "empatar = faire match nul. Deux fois cette semaine : Stuttgart et Austin.", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 16
lt = "«¡Hola! Soy Mei y estudio español en Pekín. El domingo voy a ver el Clásico con mis amigos — y antes, a dormir una hora más. ¡Gracias por el periódico!» — Mei (carta de ejemplo, escrita por la redacción)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Lettre d'exemple. VOL.2 : vraies lettres et meilleurs textes — écris-nous !", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "CARTAS DE LOS LECTORES", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "Lettre d'exemple. VOL.2 : vraies lettres et meilleurs textes — écris-nous !", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frases de la semana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASES DE LA SEMANA · PHRASES DE LA SEMAINE (MOT POUR MOT, TIRÉES DE CE NUMÉRO)", 27, "sans", True, OLIVE)
quotes = [
    ("«La noche tiene 25 horas y dormimos una hora más.»", "La nuit dure 25 heures, et nous dormons une heure de plus.", "Página 1"),
    ("«En Canarias hay una hora menos que en la Península»", "Aux Canaries, il est une heure plus tôt que sur la Péninsule.", "Página 2"),
    ("«El sistema sigue — si la ley europea no cambia.»", "Le système continue — sauf si la loi européenne change.", "Página 2"),
    ("«El PSG ganó 4–2 en París: fue la primera derrota azulgrana de la temporada.»", "Le PSG a gagné 4–2 à Paris : première défaite de la saison pour le Barça.", "Página 4"),
    ("«España se divide en dos: unos hacen puente y otros, no.»", "L'Espagne se divise en deux : les uns font le pont, les autres non.", "Página 3"),
    ("«En Cataluña, la Castanyada: castañas asadas, boniatos y panellets, unos dulces pequeños de mazapán.»", "En Catalogne, la Castanyada : châtaignes grillées, patates douces et panellets — de petits gâteaux à la pâte d'amandes.", "Página 3"),
    ("«La camiseta se estrena primero con el equipo femenino, el sábado 24»", "Le maillot est porté d'abord par l'équipe féminine, le samedi 24.", "Página 5"),
    ("«Publicamos las dos series con su fuente y su fecha, una junto a otra — y no las mezclamos nunca en un solo número.»", "Nous publions les deux séries côte à côte, avec source et date — sans jamais les fondre en un seul chiffre.", "Página 6"),
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
p.text(MX + 28, py + 44, "LA PRÓXIMA SEMANA · LA SEMAINE PROCHAINE (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "El jueves 29: los actos de memoria de la DANA en Valencia. El sábado 31: Halloween, la Castanyada y el Samaín. El domingo 1: Todos los Santos — y el lunes 2, el puente en nueve comunidades. Además: tus cartas y los mejores textos de la página 8. ¡Hasta el lunes!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lengua.svg")
print("P7 saved, exercises so far:", len(REG))
