# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-es/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Lengua en detalle", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Tres niveles, tres temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 天氣的話 · Palabras del tiempo", 24)
a.para("La semana del tifón llena las noticias de palabras del tiempo: aprende las seis que más verás: 海上颱風警報 (aviso marítimo), 陸上颱風警報 (aviso terrestre), 共伴效應 (efecto conjunto), 外圍環流 (circulación exterior), 豪雨 (lluvia torrencial), 停班停課 (trabajo y clases suspendidos).", 21.5)
a.glossline("Seis palabras del tiempo recorren las noticias de la semana: apréndelas una vez y lee toda la semana.")
a.para("Hay dos tipos de aviso: primero el 海上警報 (aviso marítimo), mientras el tifón sigue en el mar; después el 陸上警報 (aviso terrestre), cuando se acerca a tierra. Una lluvia más fuerte que 大雨 es 豪雨 (lluvia torrencial).", 21.5)
a.ex("A2", "完成句子", "海上", "Primero va el aviso marítimo, mientras el tifón sigue en el mar.",
     "颱風還在海上,先發佈___颱風警報。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "停班停課 significa que no hay trabajo ni clases.",
     "「停班停課」是什麼意思?", opts=["A. 不上班、不上課", "B. 提早一小時下班", "C. 換到別天上班"], size=20.5, gap=10)
a.ex("A2", "完成句子", "豪", "豪雨 (háo) es más fuerte que 大雨.",
     "比大雨還大的雨,叫___雨。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "La circulación exterior del tifón (外圍環流) trae la lluvia.",
     "颱風的外圍___會帶來雨。", opts=["A. 環流", "B. 警報", "C. 假期"], size=20.5, gap=10)
a.para("A practicar: «明天會停班停課嗎？» («¿Mañana no habrá trabajo ni clases?») — consulta el anuncio de tu ciudad.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 日子與節日 · Días y fiestas", 24)
b.para("Los días de esta semana son especiales. Agrupa las palabras y se quedan: descanso （連假、補假）, viajes （疏運） y diversión de fiesta （登高、討糖、星光大道）.", 21.5)
b.glossline("Agrupa las palabras: descanso (連假/補假), viajes (疏運), diversión (登高/討糖/星光大道).")
b.para("連假 es una serie de días libres seguidos; cuando una fiesta cae en fin de semana y a cambio se libera un día entre semana, ese día extra es un 補假； y los trenes y autobuses extra que llevan a todos de ida y vuelta son el 疏運.", 21.5)
b.ex("B1", "完成句子", "補假", "Un día libre de compensación: 補假.",
     "假日逢週日,週一多放一天,叫___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "疏運 = transporte extra para los viajes de las fiestas.",
     "「疏運」是連假時做什麼?", opts=["A. 加開班次載客", "B. 賣紀念票", "C. 修馬路"], size=20.5, gap=10)
b.ex("B1", "完成句子", "討糖", "討糖 es la forma taiwanesa de decir «truco o trato».",
     "萬聖節,小朋友去店家___(要糖果)。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "La parte de alfombra roja de una noche de premios es la 星光大道.",
     "頒獎典禮走紅毯的部分叫?", opts=["A. 星光大道", "B. 人氣獎", "C. 疏運大道"], size=20.5, gap=10)
b.para("Truco de memoria: aprende primero 連假, después la gente que mueve （疏運） y el día que añade （補假）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 在地說法 · Expresiones locales", 24)
c.para("Taiwán y Hong Kong tienen cada uno su manera de decir las cosas. En Taiwán, Threads se apoda «脆»; una buena publicación se guarda con «留友看» — «guardarlo para que lo vean los amigos» —; y un cumplido puntuado con símbolos zhuyin es un «ㄅ級分».", 21.5)
c.glossline("Tres expresiones de internet de Taiwán — todas de un resumen de PopDaily de mayo de 2026 con los memes del año, no de las noticias de esta semana.")
c.para("En Hong Kong, Halloween es «哈囉喂»; el hot pot es «打邊爐»; barato y rico es «抵食»; los cangrejos se pesan en «両», y las fichas del festival gastronómico son «品味券».", 21.5)
c.ex("B2", "單選", "A", "En Taiwán, Threads se apoda 脆 («crujiente»).",
     "台灣人把 Threads 暱稱作什麼?", opts=["A. 脆", "B. 脆餅", "C. 推特兒"], size=20.5, gap=10)
c.ex("B2", "完成句子", "留友", "留友看 — guardarlo para que los amigos también lo lean.",
     "看到好文,先存起來「___看」。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "單選", "A", "哈囉喂 es el Halloween de Hong Kong.",
     "「哈囉喂」是香港人怎麼說哪個節日?", opts=["A. 萬聖節", "B. 聖誕節", "C. 重陽節"], size=20.5, gap=10)
c.ex("B2", "完成句子", "品味", "Los cupones del festival son 品味券 (fichas de degustación).",
     "美酒佳餚巡禮換飲品小食的券,叫___券。", instr="Completa", size=20.5, gap=10)
c.para("No necesitas muchas expresiones locales: aprende cinco y cada conversación se sentirá más cercana.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「台風來了」", "→「颱風來了」", "Taiwán escribe 颱風; 台風 es la grafía japonesa."),
    ("「我買了四兩的蟹」", "→「我買了四両的蟹」", "Se pesan en 両 (taels); 兩 es el «dos» común: 兩隻蟹 = dos cangrejos."),
    ("「天氣慢慢的變涼」", "→「天氣慢慢地變涼」", "地 (de) marca cómo ocurre una acción, antes del verbo."),
    ("「我明天放四天假去玩」", "→「我請了四天假去玩」", "請假 = pedir días uno mismo; 放假 = descanso para todos."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Clínica de errores", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "«先看警報，再決定出不出門。» — 先…再… ordena dos acciones: primero X, después Y. Para la semana del tifón: 先查公告，再改行程 (primero los avisos, después tus planes)."
wcn = "A practicar: escribe tu frase con 先…再…."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Estructura de la semana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:重陽節我跟阿公去登高,他走得比我還快!晚上我們吃大閘蟹,蟹黃真的好多。下週我想去看台灣大賽。——台北小讀者(編輯範例)」"
lcn = "Carta de ejemplo de la redacción. ¡El VOL.2 publicará cartas reales de lectores y la mejor redacción de la página 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · El rincón de los lectores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Frases de la semana — palabra por palabra de los artículos de este número", 27, "sans", True, OLIVE)
quotes = [
    ("「路徑還有變數,會不會登陸,還沒有人知道」", "La trayectoria aún puede cambiar; nadie sabe todavía si tocará tierra.", "p. 1"),
    ("「請四天假,換九天連假」", "Cuatro días pedidos, nueve días libres.", "p. 2"),
    ("「登高望遠,人也精神了」", "Sube alto, mira lejos — y siéntete renovado.", "p. 3"),
    ("「農曆九月吃蟹乸,農曆十月吃蟹公」", "Hembras en el mes lunar 9, machos en el 10.", "p. 3"),
    ("「先贏四場的隊伍,就是今年的總冠軍」", "El primer equipo que gane cuatro es el campeón de este año.", "p. 4"),
    ("「颱風改了日期,卻改不了大家過節的心情」", "El tifón cambió la fecha, no las ganas de fiesta.", "p. 5"),
    ("「三百四十多個攤位,把世界搬到海邊」", "Más de 340 puestos traen el mundo junto al puerto.", "p. 6"),
    ("「星期五、六的晚上,今年第一次開到凌晨一時」", "Las noches de viernes y sábado llegan hasta la 1 por primera vez.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 146
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 146 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · La semana que viene (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "台灣大賽冠軍出爐!美酒佳餚巡禮開幕直擊,天母搞什麼鬼主活動、福隆沙雕最後一天,還有你們的來信和第 8 版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
