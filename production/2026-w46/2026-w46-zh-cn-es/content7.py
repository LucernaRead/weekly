# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · El foco de la lengua", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Tres niveles, tres temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 双11与包裹 · De compras", 24)
a.para("Palabras de compras de esta semana: 高潮场 (gāocháochǎng, la venta punta), 包裹 (bāoguǒ, un paquete), 取件码 (qǔjiànmǎ, un código de recogida), 快递柜 (kuàidìguì, una taquilla de paquetes). Palabras de seguridad: 消防 (xiāofáng, prevención de incendios), 疏散 (shūsàn, evacuar), 自救 (zìjiù, autorrescate).", 21.5)
a.glossline("Los clasificadores siguen importando: 一个包裹 (un paquete), 一部电影 (una película), 一场演练 (un simulacro).")
a.ex("A2", "完成句子", "个", "包裹 lleva el clasificador 个 gè.",
     "我拿了___包裹。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "单选", "A", "高潮场 significa la venta punta.",
     "「高潮场」是什么意思? A. 最忙的卖货时间 · B. 必须先付定金 · C. 只有11月11日便宜", size=20.5, gap=10)
a.ex("A2", "完成句子", "消防", "xiāofáng — prevención; 9 nov. Día del Fuego.",
     "11月9日是全国___日。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "单选", "A", "Los paquetes llevan 个 — no 只 ni 条.",
     "哪个说法对? A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20.5, gap=10)
a.para("Una más para practicar: 「我的包裹到了吗?」 (¿Ya llegó mi paquete?) Cuando esperas un paquete, pregunta primero y luego ve a la taquilla.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Horas y fechas", 24)
b.para("El chino da las horas de mayor a menor: año, mes, día, día de la semana, momento del día, hora. Ejemplos de este número: 「11月9日星期一」 (lun. 9 nov.), 「11月10日星期二20点」 (mar. 10 nov., 20:00), 「11月15日星期日凌晨3点」 (dom. 15 nov., 3 de la mañana). La unidad mayor primero, nada fuera de orden.", 21.5)
b.glossline("Así, el inglés «Monday, Nov 9» se convierte en 11月9日星期一.")
b.ex("B1", "单选", "B", "凌晨 língchén — las horas pequeñas tras la medianoche.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "完成句子", "早上", "Las 06:00 son 早上 — no la tarde.",
     "四分之一决赛在北京时间11月4日___6点开始。(不是晚上)", instr="Completa", size=20.5, gap=10)
b.ex("B1", "单选", "A", "Orden grande → pequeño: 15 nov., domingo, 03:00.",
     "哪个顺序对? A. 11月15日星期日凌晨3点 · B. 凌晨3点星期日11月15日 · C. 星期日凌晨3点11月15日", size=20.5, gap=10)
b.ex("B1", "完成句子", "周一", "El 9 de noviembre es lunes — 周一.",
     "11月9日是星期一,也可以说___。消防日在这天。", instr="Completa", size=20.5, gap=10)
b.para("Dos palabras más: 凌晨 (língchén) son las horas pequeñas tras la medianoche, antes del amanecer; 傍晚 (bàngwǎn) es el rato corto justo antes de que oscurezca.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Leer las noticias", 24)
c.para("Cuando una historia incluye una afirmación (说法), separa tres tipos de frase: afirmaciones (说法), datos (数据) y pronósticos (预报). La página 6 es el ejemplo: 「最大的一波」 es una afirmación sobre el 11 de noviembre, los múltiplos 1,5 y 2,5 son datos reportados, y las temperaturas del aire frío son un pronóstico — predicho, aún no un hecho.", 21.5)
c.glossline("Pregunta ante cada número: ¿de quién es y cuándo se midió?")
c.ex("B2", "单选", "C", "「最大的一波」 es una afirmación, no datos medidos.",
     "「最大的一波」在第6版里是什么? A. 数据 · B. 预报 · C. 说法", size=20.5, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — números medidos, no afirmaciones.",
     "买东西以前,先看___,再看广告。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "单选", "B", "Datos y página de caja primero, titular al final.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — un pronóstico, aún no un hecho.",
     "冷空气的温度是___,还没发生。", instr="Completa", size=20.5, gap=10)
c.para("Pruébalo: en el calendario de la página 1, 「11月11日」 es una fecha — un dato. Las palabras de un anuncio son afirmaciones. ¿Puedes distinguirlas?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) marca cómo se hace una acción."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) une verbo + grado: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Orden: número + clasificador + sustantivo."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日,星期日凌晨3点。」", "Las horas van de mayor a menor: el día de la semana al final."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · Clínica de errores", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看取件码,再开柜门。」(Revisa el código y abre la taquilla.) La estructura 先…再… da el orden de las acciones."
wcn = "Estructura: 先 … 再 … — primero X, luego Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Estructura de frase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在北京。11月9日学校做了消防演练,我学会了走楼梯。双11我买了一本书,包裹两天就到了。周日凌晨,我想看S16总决赛!」"
lcn = "编辑部示例信,不是真实来信。VOL.2曾预告本期刊登真实来信和最佳作文;截至11月2日截稿,仍未收到,本期仍刊示例,继续征集。延期不是取消。Nota de redacción: VOL.2 prometió cartas reales en VOL.3; ninguna llegó al 2 de nov. El ejemplo queda. Aplazado, no cancelado."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Rincón de lectores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Frases de la semana (textuales, de los artículos de este número)", 27, "sans", True, OLIVE)
quotes = [
    ("「双11的正日子」", "El propio día del Double 11.", "Página 1"),
    ("「先看结算页,再决定买不买」", "Revisa la página de caja y decide.", "Página 2"),
    ("「提高自防自救能力」", "Reforzar la autoprotección y el autorrescate.", "Página 3"),
    ("「三支队进了八强」", "Tres equipos en cuartos.", "Página 4"),
    ("「输了就回家」", "Pierdes y te vas a casa.", "Página 4"),
    ("「老电影,新画面」", "Una película vieja, una imagen nueva.", "Página 5"),
    ("「快递的高峰分三波」", "El pico de paquetes viene en tres olas.", "Página 6"),
    ("「着火了不坐电梯」", "En un incendio, no tomes el ascensor.", "Página 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期预告 · La próxima semana (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16总决赛打完了,谁是冠军?包裹都到了吗?还有你们的来信和第8版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
