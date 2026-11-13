# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语　Foco de lengua", "Lucerna", "语言聚焦　三个级别，三个主题　Tres niveles, tres temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　决赛与包裹　Final y paquetes", 24)
a.para("Palabras de la semana: 决赛 (juésài, la final), 冠军 (guànjūn, el campeón), 半决赛 (bànjuésài, la semifinal), 到货 (dàohuò, llegado), 退换货 (tuìhuànhuò, devoluciones y cambios), 价保 (jiàbǎo, protección de precio).", 21.5)
a.glossline("Los clasificadores siguen importando: 一个包裹 (un paquete), 一部电影 (una película), 一场演练 (un simulacro).")
a.ex("A2", "完成句子", "个", "包裹 lleva el clasificador 个 gè.",
     "我拿了___包裹。", instr="Completa", size=20, gap=10)
a.ex("A2", "单选", "A", "决赛 significa la final, el último partido.",
     "「决赛」是什么意思？ A. 最后一场比赛 · B. 第一场比赛 · C. 练习赛", size=20, gap=10)
a.ex("A2", "完成句子", "决赛", "juésài — la final; BLG contra GEN el 15 nov.",
     "11月15日凌晨3点，BLG和GEN打___。", instr="Completa", size=20, gap=10)
a.ex("A2", "单选", "A", "Los paquetes llevan 个 — no 只 ni 条.",
     "哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20, gap=10)
a.para("Uno más para practicar: 「我的包裹到了吗？」 (¿Ha llegado mi paquete?) Cuando esperes un paquete, pregunta primero y luego ve a la taquilla.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　时间与日期　Hora y fechas", 24)
b.para("El chino ordena el tiempo de mayor a menor: año, mes, día, día de la semana, parte del día, hora. Ejemplos de este número: 「11月15日星期日凌晨3点」 (dom. 15 nov., 3 de la madrugada), 「11月22日星期日」 (dom. 22 nov.), 「11月21日星期六」 (sáb. 21 nov.). La unidad mayor primero, nada fuera de orden.", 21.5)
b.glossline("Así, «Sunday, Nov 22» en inglés se convierte en 11月22日星期日.")
b.ex("B1", "单选", "B", "凌晨 língchén — las horas pequeñas tras la medianoche.",
     "「凌晨3点」是什么时候？ A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20, gap=10)
b.ex("B1", "完成句子", "早上", "Las 06:00 son 早上 — no por la noche.",
     "半决赛在北京时间11月8日___6点开始。（不是晚上）", instr="Completa", size=20, gap=10)
b.ex("B1", "单选", "A", "Orden de mayor a menor: 22 nov., domingo.",
     "哪个顺序对？ A. 11月22日星期日 · B. 星期日11月22日 · C. 星期日小雪11月22日", size=20, gap=10)
b.ex("B1", "完成句子", "周日", "El 22 nov. es domingo — 周日.",
     "11月22日是星期日，也可以说___。小雪在这天。", instr="Completa", size=20, gap=10)
b.para("Dos palabras más: 凌晨 (língchén) son las horas pequeñas tras la medianoche, antes del amanecer; 傍晚 (bàngwǎn) es el rato corto justo antes de que oscurezca.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　读新闻　Leer las noticias", 24)
c.para("Cuando una historia incluye una afirmación (说法), separa tres tipos de oraciones: afirmaciones (说法), datos (数据) y previsiones (预报). La página 6 es el ejemplo: « 没有爆掉 » es una afirmación sobre los paquetes de este año, el total 139.38亿件 son datos publicados — ya contados, no una suposición — y « 第三波是最高峰 » es una previsión de 中通云仓: esperada, aún no contada.", 21.5)
c.glossline("Pregunta ante cada número: ¿de quién es y cuándo se midió?")
c.ex("B2", "单选", "A", "« 139.38亿件 »: recuento final de Correos, ya contado.",
     "「139.38亿件」在第6版里是什么？ A. 已经数完的事实 · B. 邮政局的预计 · C. 广告词", size=20, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — números medidos, no afirmaciones.",
     "买东西以前，先看___，再看广告。", instr="Completa", size=20, gap=10)
c.ex("B2", "单选", "B", "Datos y página de caja primero, titular al final.",
     "读新闻时，哪个做法最好？ A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — un pronóstico, aún no un hecho.",
     "「第三波是最高峰」是___，还没发生。", instr="Completa", size=20, gap=10)
c.para("Pruébalo tú: en el recuadro del calendario de la página 1, « 11月22日 » es una fecha — un dato. Las palabras de un anuncio son afirmaciones. ¿Puedes distinguirlas?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters + image ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) marca cómo se hace una acción."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) une verbo + grado: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Orden: número + clasificador + sustantivo."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日，星期日凌晨3点。」", "Las horas van de mayor a menor: el día de la semana al final."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所　Clínica de errores", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看预报，再决定穿什么。」La estructura 先…再… da el orden de las acciones."
wcn = "Estructura: 先 … 再 … — primero X, luego Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式　Estructura de frase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好！我住在上海。11月9日半决赛，我看了BLG打T1，3比1，真好看！双11我买了一件外套，包裹两天就到了。你们呢？」"
lcn = "编辑部示例信，不是真实来信。VOL.3曾预告本期刊登真实来信和最佳作文；截至11月10日截稿，仍未收到，继续征集。延期不是取消。Nota de la redacción: VOL.3 prometió cartas reales; ninguna llegó al 10 nov. Aplazado, no cancelado."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地　Rincón de lectores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- P7 image (brush) below the letters box ----
iy7 = col3_end + 12
image(p, "brush.jpg", bx, iy7, CW, 130)
cy7 = caption(p, bx, iy7 + 130, CW, "毛笔（资料图）。写中文，先从一笔一画开始。",
              "Foto: Mx. Granger — CC0 (Wikimedia Commons)")
img_end = cy7
print("P7 image ends", img_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, img_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本周金句　Frases de la semana (textuales, de los artículos de este número)", 27, "sans", True, OLIVE)
quotes = [
    ("「决赛对阵GEN」", "La final: BLG contra GEN.", "Página 1"),
    ("「包裹都到了吗」", "¿Han llegado todos los paquetes?", "Página 2"),
    ("「小雪气寒而将雪矣」", "Nieve Menor: el aire se enfría, llega la nieve.", "Página 3"),
    ("「两支中国队进了四强」", "Dos equipos chinos llegaron a las semifinales.", "Página 4"),
    ("「先看简介，再决定」", "Lee primero la sinopsis y luego decide.", "Página 5"),
    ("「无高峰，全高峰」", "Ningún pico único — cada día es un pico.", "Página 6"),
    ("「先打开看一看，再确认收货」", "Abre y revisa primero, luego confirma la recepción.", "Página 6"),
    ("「悦读深圳」", "Leer con alegría en Shenzhen — el tema del Mes de la Lectura de Shenzhen.", "Página 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 120
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 120 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期预告　La semana que viene (VOL.5)", 24, "sans", True, GOOSE)
p.para(MX + 28, py + 84, "S16总决赛打完了，谁是冠军？小雪之后，冬天怎么过？还有你们的来信和第8版最佳作文。下周见！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
