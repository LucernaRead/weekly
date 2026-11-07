# -*- coding: utf-8 -*-
# W46 zh-tw core, VOL.3: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-tw-es/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Enfoque lingüístico", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Tres niveles, tres temas")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 雙11的話 · Palabras del 11.11", 24)
a.para("El Double 11 te da cuatro palabras útiles: 清單 (lista de la compra), 實付金額 (la cantidad final que pagas), 領券 (reclamar cupones) y 鑑賞期 (el plazo de devolución). Apréndelas una vez y cada oferta tendrá sentido.", 21.5)
a.glossline("Cuatro palabras del Double 11: 清單, 實付金額, 領券, 鑑賞期.")
a.para("清單 es la lista que escribes antes de comprar. 實付金額 es lo que pagas de verdad después de los descuentos. 領券 significa reclamar un cupón antes de que se agote. 鑑賞期 son los 7 días después de la entrega en los que puedes devolver casi todo.", 21.5)
a.ex("A2", "完成句子", "清單", "Una lista de la compra es una 清單.",
     "買東西之前,先列___。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "El plazo de devolución es de 7 días.",
     "鑑賞期是幾天?", opts=["A. 7天", "B. 3天", "C. 14天"], size=20.5, gap=10)
a.ex("A2", "完成句子", "實付金額", "Compara la cantidad final que pagas de verdad.",
     "比價要比___。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Reclama los cupones antes de que se agoten.",
     "優惠券要怎麼拿?", opts=["A. 先領,領完就沒有了", "B. 不用領", "C. 過期再領"], size=20.5, gap=10)
a.para("Practica: 「我的購物清單是什麼？」 («¿Qué hay en mi lista de la compra?») — escríbela primero y luego compara precios.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 影展與鋼雕 · Cine y acero", 24)
b.para("El cine y el acero comparten los titulares de la semana. Agrupa las palabras y se quedan: cine （入圍、頒獎、星光大道） y acero （鋼雕、保險箱、勞動記憶）.", 21.5)
b.glossline("Agrupa las palabras: cine (入圍/頒獎), acero (鋼雕/保險箱).")
b.para("入圍 significa ser nominado; 頒獎 significa entregar los premios. 星光大道 es la alfombra roja antes de la ceremonia. 鋼雕 es una escultura de acero; 保險箱 es la caja fuerte que guarda los recuerdos obreros de Kaohsiung.", 21.5)
b.ex("B1", "完成句子", "入圍", "Ser nominado es 入圍.",
     "被選進最後的得獎名單,叫___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "La ceremonia empieza a las 18:30 el 22 nov.",
     "金馬獎頒獎典禮幾點開始?", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=20.5, gap=10)
b.ex("B1", "完成句子", "鋼雕", "Una escultura de acero es 鋼雕.",
     "用鋼鐵做的藝術,叫___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "El festival del acero cierra el 22 nov.",
     "鋼雕藝術節展到哪天?", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=20.5, gap=10)
b.para("Truco: aprende primero 入圍 — luego la ceremonia （頒獎）, luego el lugar donde ocurre （星光大道）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Habla local", 24)
c.para("Taiwán y Hong Kong tienen cada uno su manera de decir las cosas. Esta semana: 打卡 (registrarse con una foto), 集點 (acumular puntos), 遊行 (desfile en la calle) y 感謝祭 (festival de agradecimiento para los aficionados).", 21.5)
c.glossline("Cuatro palabras locales de este número: 打卡, 集點, 遊行, 感謝祭.")
c.para("打卡 en una feria significa publicar una foto para decir «estuve aquí». 集點 es ganar puntos cada vez que haces deporte. 遊行 es la marcha de celebración por las calles; 感謝祭 es el festival de agradecimiento del equipo para sus aficionados.", 21.5)
c.ex("B2", "單選", "A", "集點 significa acumular puntos al hacer deporte.",
     "「集點」是什麼意思?", opts=["A. 每次運動累積點數", "B. 買門票", "C. 上班簽到"], size=20.5, gap=10)
c.ex("B2", "完成句子", "遊行", "Una marcha de celebración es 遊行.",
     "大家走上街頭慶祝,叫___。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "單選", "A", "感謝祭 da las gracias a los aficionados.",
     "「感謝祭」是謝謝誰的活動?", opts=["A. 球迷", "B. 店員", "C. 記者"], size=20.5, gap=10)
c.ex("B2", "完成句子", "打卡", "Registrarse con una foto es 打卡.",
     "在嘉年華拍照分享,叫___。", instr="Completa", size=20.5, gap=10)
c.para("No necesitas muchas expresiones locales: aprende cuatro y cada salida se sentirá más cercana.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「旅展在11月9日開幕」", "→「旅展在11月9日落幕,開幕是11月6日」", "Feria abierta el 6 nov. y cerrada el 9 nov. Comprueba el sentido del tiempo."),
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎,11月15日是嘉年華」", "Ceremonia: 22 nov.; carnaval: 15 nov. (2.º día)."),
    ("「滿5,000折800,實付5,800元」", "→「滿5,000折800,實付4,200元」", "Los descuentos se restan: 5.000 − 800 = 4.200."),
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
wt = "「雙11不但有折扣,而且有免運。」 — La estructura 不但…而且… significa: no solo X, sino también Y. Crea la tuya: 旅展不但有攤位,而且有表演 (no solo casetas, sino también espectáculos)."
wcn = "Estructura: 不但…而且… — no solo X, sino también Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Estructura de la semana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:雙11我的包裹到了!我買了一本書和一件外套,都沒有超過預算。週末我想去銅鑼灣看夜光巡遊,還想去高雄看鋼雕。——台北小讀者(編輯範例)」"
lcn = "Carta de ejemplo de la redacción, no una carta real. VOL.2 prometió cartas reales y los mejores textos de la página 8 desde este número; ninguna llegó publicable antes del cierre. El ejemplo se queda, y la invitación también."
lt2 = "延期披露:VOL.2曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 40
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Rincón de los lectores", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Frases de la semana — palabra por palabra, de los artículos de este número", 27, "sans", True, OLIVE)
quotes = [
    ("「先列清單,再比價,最後才結帳」", "Primero la lista, luego los precios, luego pagar.", "p. 1"),
    ("「旅展四天,一次看完123個國家及城市」", "Cuatro días de feria, 123 países y ciudades en una visita.", "p. 1"),
    ("「早晚溫差大,外套要隨身帶」", "Grandes diferencias de temperatura día-noche: lleva una chaqueta.", "p. 2"),
    ("「金馬影展,就是一年一度的大電影課」", "El festival Golden Horse es una gran clase de cine al año.", "p. 3"),
    ("「保險箱裡,裝的是高雄的勞動記憶」", "Dentro de la caja fuerte: los recuerdos obreros de Kaohsiung.", "p. 3"),
    ("「穿上紅色衣服,一起上街為龍隊喝采」", "Viste de rojo, sal a la calle, anima a los Dragons.", "p. 4"),
    ("「嘉年華不用門票,全家人都能來玩」", "No hace falta billete: toda la familia puede venir a jugar.", "p. 5"),
    ("「回饋不是折價,實付金額才是真的」", "El cashback no es un descuento: lo que cuenta es la cantidad pagada.", "p. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 138
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 138 + 4  # fix 2026-11-03: was +18; teaser bottom crossed the footer rule (2587.86 > 2580)
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · La próxima semana (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週日11月22日,三件大事同一天:封王遊行下午2點、金馬獎晚上6點30分、鋼雕藝術節閉幕,還有小雪、你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
