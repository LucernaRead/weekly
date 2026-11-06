# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/w45/zh-tw-es-proof/work/reg-ed/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Enfoque lingüístico", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Tres niveles, tres temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 展會的話 · Palabras de feria", 24)
a.para("Las ferias de esta semana te dan cuatro palabras útiles: 旅展 (feria de viajes), 攤位 (caseta), 集章 (coleccionar sellos) y 吉祥物大遊行 (desfile de mascotas). Apréndelas una vez y toda la feria de viajes cobrará sentido.", 21.5)
a.glossline("Cuatro palabras de feria: 旅展, 攤位, 集章, 吉祥物大遊行.")
a.para("旅展 es la forma corta de 旅行展覽會 (exposición de viajes). Una 攤位 es un puesto dentro de la feria; la feria de Taipéi tiene 1.600. 集章 significa coleccionar sellos en puntos establecidos: colecciona los seis sellos de las Vías Verdes y ganarás un premio.", 21.5)
a.ex("A2", "完成句子", "攤位", "Un puesto dentro de la feria es una 攤位.",
     "旅展裡的一個小展位,叫___。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "El desfile de mascotas se celebra a diario a las 14:00.",
     "吉祥物大遊行每天幾點?", opts=["A. 下午2點", "B. 中午12點", "C. 晚上7點"], size=20.5, gap=10)
a.ex("A2", "完成句子", "集章", "Coleccionar sellos en puntos establecidos es 集章.",
     "在6大綠道蓋章收集,叫___。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "La feria de viajes está en el Centro de Exposiciones de Nangang.",
     "台北旅展在哪裡?", opts=["A. 南港展覽館一館", "B. 台北大巨蛋", "C. 高雄駁二"], size=20.5, gap=10)
a.para("Practica: 「旅展幾點開門？」 («¿A qué hora abre la feria?») — el viernes abre al mediodía y los demás días a las 10:00.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 球賽與節氣 · Juegos y estación", 24)
b.para("El deporte y las estaciones comparten los titulares de esta semana. Agrupa las palabras y se quedan: ganar （封王、完封） e invierno （立冬、進補）.", 21.5)
b.glossline("Agrupa las palabras: ganar (封王/完封), invierno (立冬/進補).")
b.para("封王 significa conquistar el campeonato; 完封 significa dejar al rival sin anotar, 0 carreras. 立冬 es el término solar que inicia el invierno; 進補 es comer alimentos calientes y nutritivos antes de los meses fríos.", 21.5)
b.ex("B1", "完成句子", "封王", "Conquistar el título es 封王.",
     "拿下總冠軍,叫___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "完封 significa que el rival anota cero.",
     "「完封」是什麼意思?", opts=["A. 對手得0分", "B. 大勝10分", "C. 打滿9局"], size=20.5, gap=10)
b.ex("B1", "完成句子", "立冬", "Lidong inicia el invierno.",
     "冬天第一個節氣是___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "El pato con jengibre es un plato de Lidong.",
     "立冬常吃的鍋是哪一種?", opts=["A. 薑母鴨", "B. 冰品", "C. 生魚片"], size=20.5, gap=10)
b.para("Truco de memoria: aprende primero 封王 y después la manera en que se ganó （完封） y después la estación en que ocurrió （立冬）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Habla local", 24)
c.para("Taiwán y Hong Kong tienen cada uno su manera de decir las cosas. Esta semana: 打卡 (registrarse con una foto), 討糖 (pedir dulces en Halloween), 踩街 (desfile callejero disfrazado) y 泡湯 (bañarse en aguas termales).", 21.5)
c.glossline("Cuatro palabras locales de este número: 打卡, 討糖, 踩街, 泡湯.")
c.para("打卡 empezó como fichar al entrar al trabajo, pero en una feria o un festival significa publicar una foto para decir «estuve aquí». 討糖 es lo que los niños dicen en las tiendas en Halloween; 踩街 es el propio desfile disfrazado; 泡湯 es el placer otoñal de un baño termal.", 21.5)
c.ex("B2", "單選", "A", "En un festival, 打卡 significa publicar una foto para decir que estuviste allí.",
     "在旅展、節慶場合,「打卡」是什麼意思?", opts=["A. 拍照分享,說自己來過", "B. 上班簽到", "C. 買門票"], size=20.5, gap=10)
c.ex("B2", "完成句子", "討糖", "Pedir dulces en Halloween es 討糖.",
     "萬聖節小朋友去店家___。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "單選", "A", "踩街 es un desfile callejero disfrazado.",
     "「踩街」是什麼?", opts=["A. 穿裝扮上街遊行", "B. 在街上跑步", "C. 逛夜市"], size=20.5, gap=10)
c.ex("B2", "完成句子", "泡湯", "Bañarse en aguas termales es 泡湯.",
     "秋冬去溫泉洗澡、放鬆,叫___。", instr="Completa", size=20.5, gap=10)
c.para("No necesitas muchos dichos locales: aprende cuatro y cada salida se sentirá más cercana.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「龍隊完勝兄弟6比0」", "→「龍隊完封兄弟6比0」", "完勝 significa ganar por mucho; 完封 significa que el rival anotó cero."),
    ("「立冬就是冬至」", "→「立冬是冬天開始,冬至是白天最短的一天」", "Lidong inicia el invierno; el Solsticio es el día más corto. Términos distintos."),
    ("「金融科技週在台北開幕」", "→「金融科技週在香港開幕」", "Comprueba la ciudad: la Semana FinTech abre en Hong Kong, no en Taipéi."),
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
wt = "「先去集章，再去看表演。」 — la estructura 先…再… ordena dos acciones: primero X y después Y. Crea la tuya: 先比價，再結帳."
wcn = "Estructura: 先…再… — primero X y después Y. Crea tu propia frase con ella."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Estructura de la semana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:上週我去天母討糖,拿到一顆很大的糖果!這週我想去旅展看吉祥物大遊行,還想集滿6大綠道的章。——台北小讀者(編輯範例)」"
lcn = "Carta de ejemplo de la redacción, no una carta real. Aviso: el VOL.1 prometió cartas reales y la mejor redacción de la página 8 desde este número; al cierre no había ninguna publicable, así que el ejemplo se mantiene y la invitación sigue abierta."
lt2 = "延期披露:VOL.1曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 46
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Rincón del lector", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Frases de la semana — palabra por palabra de los artículos de este número", 27, "sans", True, OLIVE)
quotes = [
    ("「用手機轉帳、掃碼付款、網上買保險，都是金融科技」", "Pagar con el móvil, escanear para pagar, comprar un seguro en línea: eso es la tecnología financiera.", "p. 1"),
    ("「123個國家及城市、1,600個攤位」", "123 países y ciudades, 1.600 casetas.", "p. 1"),
    ("「需要才買，不要為了折扣買一堆用不到的東西」", "Compra lo que necesites; no compres un montón de cosas que no usarás solo por un descuento.", "p. 2"),
    ("「在高雄，鋼鐵也能變成舞台」", "En Kaohsiung, hasta el acero puede convertirse en escenario.", "p. 3"),
    ("「福隆的夏天，在10月26日畫下句點」", "El verano de Fulong llegó a su fin el 26 de octubre.", "p. 3"),
    ("「6比0完封兄弟，龍隊拋下紅色彩帶」", "Un 6-0 sin carreras en contra ante los Brothers, y los Dragons lanzaron las cintas rojas.", "p. 4"),
    ("「250家店家一起討糖」", "250 tiendas repartiendo dulces juntas.", "p. 5"),
    ("「旅展首日中午12點才開門」", "El primer día de la feria las puertas abren solo al mediodía.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 138
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 138 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · La próxima semana (VOL.3)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週三雙11,你買了什麼?下週一旅展最後一天直擊,高雄鋼雕藝術節展到11月22日,還有你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
