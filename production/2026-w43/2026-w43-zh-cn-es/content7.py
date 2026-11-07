# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-es/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Enfoque lingüístico", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Tres niveles, tres temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 购物与量词 · Clasificadores", 24)
a.para("Al comprar, el chino usa clasificadores (量词): 一件外套 (un abrigo), 一条围巾 (una bufanda), 一斤蟹 (medio kilo de cangrejo), 一只蟹 (un cangrejo). El patrón es: número + clasificador + sustantivo (数词 + 量词 + 名词).", 21.5)
a.glossline("El español cuenta las cosas de forma imprecisa; el chino elige un clasificador para cada tipo de cosa — sin plural.")
a.ex("A2", "Completar", "件", "wàitào lleva el clasificador jiàn.",
     "我想买一___外套。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Opción múltiple", "B", "wéijīn lleva tiáo: cosas largas y blandas.",
     "「一条」可以说什么? A. 一条外套 · B. 一条围巾 · C. 一条大闸蟹", size=20.5, gap=10)
a.ex("A2", "Completar", "斤", "jīn — medio kilo; los precios del mercado son por jīn.",
     "大闸蟹多少钱一___?", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Opción múltiple", "A", "La ropa lleva jiàn, no gè ni tiáo.",
     "哪个说法对? A. 一件衣服 · B. 一个衣服 · C. 一条衣服", size=20.5, gap=10)
a.para("Una más para practicar: 「这件外套多少钱?」 (¿Cuánto cuesta este abrigo?) Al comprar, pregunta primero el precio y paga después.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Hora y fechas", 24)
b.para("El chino da las horas de grande a pequeño: año, mes, día, día de la semana, parte del día, hora. Ejemplo: 「10月20日晚上8点」 (20 de octubre, 8 de la tarde) — primero la unidad mayor, nada fuera de orden.", 21.5)
b.glossline("Así, «la tarde del viernes 23 de octubre» se convierte en 10月23日星期五晚上.")
b.ex("B1", "Opción múltiple", "B", "língchén — las horas tras medianoche.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "Completar", "上午", "La NBA abrió por la mañana, hora de Pekín.",
     "NBA 在北京时间10月21日___开打。(不是晚上)", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Opción múltiple", "A", "Orden grande → pequeño: 20 de octubre, tarde, 8.",
     "哪个顺序对? A. 10月20日晚上8点 · B. 8点晚上10月20日 · C. 晚上8点10月20日", size=20.5, gap=10)
b.ex("B1", "Completar", "周五", "El 23 de octubre es viernes — zhōuwǔ.",
     "10月23日是星期五,也可以说___。霜降在这天。", instr="Completa", size=20.5, gap=10)
b.para("Dos palabras más: 凌晨 (língchén) son las horas pequeñas después de medianoche, antes del amanecer; 傍晚 (bàngwǎn) es el rato corto justo antes de que oscurezca.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Leer las noticias", 24)
c.para("Cuando una noticia trata de una disputa (争议), separa tres tipos de frases: afirmaciones en línea (说法), declaraciones oficiales (声明) y datos de mercado (数据). Las afirmaciones pueden exagerar; los datos deben conservar su fuente y su fecha. La página 6 es el ejemplo: 「暴跌40%」 es una afirmación, 77.5 元 y 57.5 元 son datos, 「崩盘不实」 es una declaración.", 21.5)
c.glossline("Pregunta de cada cifra: ¿quién la midió, y cuándo?") 
c.ex("B2", "Opción múltiple", "C", "«bàodiē 40 %» era una afirmación, no un dato medido.",
     "「暴跌超过40%」在第6版里是什么? A. 数据 · B. 声明 · C. 网上的说法", size=20.5, gap=10)
c.ex("B2", "Completar", "声明", "shēngmíng — la declaración de la asociación.",
     "协会10月19日发表___,说「崩盘」不是真的。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Opción múltiple", "B", "Primero los datos y la fuente; el titular al final.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和出处 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "Completar", "25.8", "La bajada real, calculada en la página 6, es del 25,8 %.",
     "第6版真正算出的数据降幅是___%。", instr="Completa", size=20.5, gap=10)
c.para("Pruébalo tú: en el cuadro de búsquedas de la página 1, 「第 8 位」 es una posición — un dato. Las palabras de un titular son afirmaciones. ¿Sabes distinguirlas?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) marca cómo se hace una acción; va antes del verbo."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) une un verbo con un complemento de grado: 跑得快."),
    ("「我买了三只大闸蟹个」", "→ 「我买了三只大闸蟹。」", "Orden: número + clasificador + sustantivo. El 个 final sobra; los cangrejos usan 只."),
    ("「霜降在星期五十月二十三日」", "→ 「霜降在10月23日,星期五。」", "Las horas van de grande a pequeño: primero mes y día, el día de la semana al final."),
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
wt = "「先付定金,后付尾款。」(Primero el anticipo, luego el saldo.) La estructura 先…后/再… da el orden de las acciones. Más: 「先看天气,再出门。」「先洗手,再吃饭。」"
wcn = "Estructura: 先 … 后/再 … — primero X, luego Y. Inventa tu propia frase."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · Estructura de la semana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在多伦多。霜降那天,我吃了柿子,也给妈妈打了电话。我的购物车里有一件外套,还在等付尾款。」"
lcn = "Una carta de ejemplo de la redacción — no es real. ¡El VOL.2 publicará cartas reales de los lectores y el mejor texto de la página 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · Rincón de los lectores", 23, "sans", True, OLIVE)
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
    ("「今年的双11来得早」", "El 双11 de este año llegó pronto.", "Página 1"),
    ("「付完尾款，快递就开始送货了」", "Pagado el saldo, empieza el envío.", "Página 1"),
    ("「付完尾款，商家就发货」", "Al pagar el saldo, el vendedor envía.", "Página 2"),
    ("「遥知兄弟登高处，遍插茱萸少一人」", "El verso famoso de Wang Wei sobre el 重阳 (poema).", "Página 3"),
    ("「两个分数只差2.735分」", "Las dos puntuaciones solo difieren en 2,735 puntos.", "Página 4"),
    ("「最大的看点是詹姆斯」", "La mayor atracción es LeBron.", "Página 4"),
    ("「看S16，要通宵了」", "Ver el S16 significa pasar la noche en vela.", "Página 5"),
    ("「先看数据，再看标题」", "Primero los datos, el titular al final (la regla de la página 6).", "Página 6"),
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
p.text(MX + 28, py + 44, "下期预告 · La semana que viene (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16 瑞士轮打完了:LPL 的四支队打得怎么样?双11 的包裹都到了吗?我们追踪报道。11月7日是立冬,冬天要来了。还有你们的来信和第 8 版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
