# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P5 youth, P6 deep read.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-es/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P5 · youth
CURPAGE[0] = 5
p = BSPage4()
p.band("青年 · Juventud", "Lucerna", "第 5 版 · 天母萬聖節回顧、旅展攻略 · Repaso de Halloween en Tianmu y plan para la feria de viajes")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P5-main")
f.title("天母萬聖節回顧:討糖、踩街、南瓜桶", 34)
f.para("上週的天母很熱鬧。第18屆「天母搞什麼鬼」原訂10月24日辦主活動,受到颱風影響,改成兩天:10月25日(週日)晚上7點,百鬼夜行討糖踩街從新光三越台北天母店出發,沿著忠誠路二段走到大葉高島屋;10月26日(週一)下午1點到晚上8點,主活動在天母運動公園登場。")
f.para("討糖是重點:250家店家一起討糖,三大百貨在10月26日下午1點同步發放4,500個限量南瓜桶。今年還跟日本人氣角色塔麻歌子30週年合作,很多大小朋友穿上萬聖裝扮,到店家喊一聲 Trick or Treat,就能拿到糖果。")
f.gloss("El Halloween de Tianmu (25-26 de octubre, aplazado del 24 de octubre por el tifón): el desfile nocturno del 25 de octubre marchó desde Shin Kong Mitsukoshi Tianmu por la calle Zhongcheng hasta Dayeh Takashimaya, y el evento principal del 26 de octubre duró de 13:00 a 20:00 en el parque deportivo de Tianmu, con 250 tiendas repartiendo dulces y 4.500 cubos de calabaza de tres grandes almacenes.")
f.title("旅展青年攻略:先看表演,再比價", 34)
f.para("週五旅展開幕,年輕人怎麼逛?先看表演:大會舞台有多國文化展演,包括日本山形花笠舞、韓國觀光公社帶來的跆拳道與喜劇武術表演《JUMP》;每日下午2點,吉祥物大遊行準時出發,還能參加粉絲見面會。")
f.para("再比價:機票優惠要看清楚。廉航最低票價通常不含託運行李,加上行李費,價差可能縮小,甚至反轉。報導整理的例子:國泰航空東京來回含稅13,433元起,購票到11月13日。所有價格都以實際訂票結果為準,不同日期價格不同。")
f.gloss("Plan para la feria de viajes: mira primero los espectáculos (danza del sombrero de flores de Yamagata, espectáculo JUMP de taekwondo y comedia de Corea, desfile diario de mascotas a las 14:00) y después compara precios: las tarifas económicas a menudo excluyen el equipaje facturado, así que suma ese coste antes de decidir.")
f.title("雙11:購物車先列好", 34)
f.para("下週三就是雙11。聰明的做法是:這週先把購物車列好,刪掉不需要的,留下真正要買的;設好預算,超過預算的東西,先放一邊。折扣會過去,帳單會留下來。")
f.box("練習例子 · Ejemplo práctico", [
    ("小林的購物車一共6,200元,預算只有5,000元。他刪掉一件1,200元的外套,購物車變成5,000元,正好符合預算。", "serif", False, INK, 22, 1.4),
    ("Cifras del ejemplo: 6.200 NT$ − 1.200 NT$ = 5.000 NT$, justo su presupuesto.", "sans", False, GREY, 19.5, 1.35),
])
f.head("讀懂了嗎? · ¿Entendido?", 28)
f.ex("B1", "單選", "B", "El desfile nocturno marchó el domingo 25 de octubre a las 19:00.",
     "百鬼夜行討糖踩街在哪天晚上?", opts=["A. 週六晚上", "B. 週日(10月25日)晚上7點", "C. 週一晚上"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "El evento principal duró de 13:00 a 20:00 en el parque deportivo de Tianmu.",
     "天母主活動在哪裡、幾點到幾點?", opts=["A. 天母運動公園,下午1點到晚上8點", "B. 大葉高島屋,早上9點到下午5點", "C. 新光三越,晚上7點到9點"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "250 tiendas repartieron dulces.",
     "天母商圈有幾家店家一起討糖?", opts=["A. 25家", "B. 150家", "C. 250家"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Se repartieron 4.500 cubos de calabaza.",
     "三大百貨發放幾個限量南瓜桶?", opts=["A. 450個", "B. 4,500個", "C. 45,000個"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "El desfile de mascotas se celebra a diario a las 14:00.",
     "旅展吉祥物大遊行每天幾點?", opts=["A. 下午2點", "B. 中午12點", "C. 晚上7點"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Las tarifas económicas a menudo excluyen el equipaje facturado.",
     "廉航最低票價通常不含什麼?", opts=["A. 機上餐點", "B. 託運行李", "C. 登機證"], size=22.5, gap=8)
f.head("填一填 · Completa", 28)
f.ex("B1", "完成句子", "忠誠路", "El desfile marchó por la calle Zhongcheng.",
     "百鬼夜行沿著___二段走。", instr="Completa", size=22.5, gap=8)
f.ex("B1", "完成句子", "塔麻歌子", "La colaboración del 30.º aniversario de Tamagotchi.",
     "今年天母萬聖節跟___30週年合作。", instr="Completa", size=22.5, gap=8)
f.ex("B1", "完成句子", "花笠舞", "La danza del sombrero de flores de Yamagata actúa en el escenario.",
     "旅展舞台有日本山形___。", instr="Completa", size=22.5, gap=8)
f.ex("B1", "完成句子", "預算", "Fija un presupuesto antes del Doble 11.",
     "雙11之前,先設好___。", instr="Completa", size=22.5, gap=8)
f.ex("B1", "完成句子", "行李費", "Suma las tasas de equipaje antes de comparar tarifas.",
     "比機票價錢,要先加上___再比較。", instr="Completa", size=22.5, gap=8)
f.ex("B1", "完成句子", "購物車", "Haz primero la lista de tu carrito y después borra lo que no necesites.",
     "雙11之前,先把___列好。", instr="Completa", size=22.5, gap=8)
f.head("算一算 · Calcula", 28)
f.ex("B1", "單選", "B", "6.200 − 1.200 = 5.000, justo el presupuesto.",
     "練習:購物車6,200元,刪掉1,200元外套,剩下多少?", opts=["A. 4,000元", "B. 5,000元", "C. 7,400元"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "El desfile empieza a las 19:00; el evento principal, al día siguiente a las 13:00.",
     "踩街晚上7點出發,主活動隔天下午幾點開始?", opts=["A. 下午1點", "B. 上午10點", "C. 晚上7點"], size=22.5, gap=8)
f.match_set("B1", "配對",
            ["討糖", "踩街", "南瓜桶", "打卡"],
            ["萬聖節向店家要糖果", "穿上裝扮上街遊行", "裝糖果的萬聖節桶子", "拍照標記地點、分享到社群"],
            ["a", "b", "c", "d"],
            ["討糖 — pedir dulces en Halloween.",
             "踩街 — desfilar por las calles disfrazado.",
             "南瓜桶 — un cubo de calabaza para dulces.",
             "打卡 — registrarse con una foto en redes sociales."],
            instr="Une evento y dato")
f.end_report()

rx = COLX[3]
image(p, "pumpkin.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "雕刻好的南瓜燈(資料照片)。天母萬聖節,南瓜桶是小朋友的最愛。",
        "Photo: Benjamin Balazs — CC0 (Wikimedia Commons)")
by = 208 + 300 + 96
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "天母時間表 · Horario de Tianmu", 25, "sans", True, OLIVE); yy += 56
for t in [
    "原訂:10月24日主活動,因颱風延期",
    "10月25日(日)19:00:百鬼夜行踩街",
    "起點:新光三越台北天母店",
    "終點:大葉高島屋,沿忠誠路二段",
    "10月26日(一)13:00-20:00:主活動,天母運動公園",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 250, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢? · ¿Y tú?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你扮過萬聖節裝扮嗎?最想扮什麼角色?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "¿Te has disfrazado alguna vez en Halloween? ¿Qué personaje te gustaría más ser?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 250 + 18
p.rect(rx, by3, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
yy = by3 + 18
p.text(rx + 22, yy + 26, "旅展表演 · Espectáculos", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日本山形花笠舞",
    "韓國跆拳道與喜劇武術《JUMP》",
    "吉祥物大遊行:每日下午2點",
    "粉絲見面會:遊行之後",
    "旅遊產品說明會:西班牙朝聖之路、日本自由行",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(5)
p.save(f"{OUT}/p5-youth.svg")
print("P5 saved, exercises so far:", len(REG))

# ============================================================ P6 · deep read
CURPAGE[0] = 6
p = BSPage4()
p.band("深讀 · Lectura a fondo", "Lucerna", "第 6 版 · 金融科技週深讀 + 讀圖表 · FinTech a fondo y lectura de gráficos")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 860, tag="P6-main")
f.title("金融科技週深讀:三個加號", 34)
f.byline("Reportaje de la redacción · Fuente: comunicado de prensa de los organizadores (23 de octubre) y preguntas frecuentes del evento")
f.para("金融科技週的三大方向,名字裡都有一個「＋」。第一個是金融＋:金融業本來就有錢、有客戶,加上科技,就能把服務做得更快、更方便。第二個是人工智慧＋:人工智慧走進銀行、投資、保險,幫忙看數據、抓風險、回客戶問題。第三個是全球擴張:一家香港的新創公司,能不能把產品賣到東南亞、歐洲、北美?金融科技週就是幫大家牽線的地方。")
f.para("數字會說話:預計逾45,000人、120多個經濟體、逾1,000位講者、逾800家參展商和新創公司、逾30個代表團、100多場社區活動。這些數字不是比賽誰大,而是告訴你:金融科技已經不是少數人的話題,而是整個城市、整個區域都在談的事。")
f.para("對學中文的人,金融科技週也是一堂課。展區裡的產品介紹、論壇上的演講題目,用的都是今天的中文:支付、數位資產、財富科技、保險科技。聽不懂沒關係,先記住四個詞,下次再聽,就聽得懂一半了。")
f.gloss("Tres signos más: Finanzas+ (finanzas más tecnología), IA+ (inteligencia artificial dentro de bancos, inversiones y seguros) y expansión global (ayudar a las empresas emergentes a vender en todo el mundo). La escala — más de 45.000 personas, más de 120 economías, más de 1.000 ponentes, más de 800 expositores y empresas emergentes, más de 30 delegaciones, más de 100 eventos comunitarios — muestra que la tecnología financiera ya es un tema de toda la ciudad.")
f.end_report()

# ---- chart: ITF opening hours per day ----
chy = 900
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, GOLD, 2)
p.text(MX, chy + 28, "旅展每日開放時數 · Horas de apertura de la ITF por día — barras proporcionales a las horas", 27, "sans", True, OLIVE)
BX = MX + 215
SCALE = 100.0
hours = [("11/6(五)", 6), ("11/7(六)", 8), ("11/8(日)", 8), ("11/9(一)", 8)]
ry = chy + 62
for label, val in hours:
    p.text(MX + 20, ry + 26, label, 22, "serif", False, INK)
    p.text(BX - 14, ry + 26, str(val), 22, "serif", True, INK, anchor="end")
    p.rect(BX, ry, val * SCALE, 34, fill="#3e4c2a")
    ry += 52
chart_end = ry + 10
p.text(MX, chart_end + 24, "旅展首日中午12點才開門,開放6小時;11月7到9日每天上午10點到下午6點,各8小時。展期共4天,總開放時數 6 + 8 + 8 + 8 = 30 小時。", 21, "serif", False, GREY)
p.text(MX, chart_end + 56, "Fuente: horarios publicados de la feria (6 nov.: 12:00-18:00; 7-9 nov.: 10:00-18:00). Total: 30 horas.", 20, "sans", False, GREY)

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 96, 2540, tag="P6-ex")
e.head("看圖答題 · Lee el gráfico", 28)
e.ex("B2", "單選", "A", "El 6 de noviembre es el día más corto: 6 horas.",
     "旅展哪一天開放時間最短?", opts=["A. 11月6日(6小時)", "B. 11月7日", "C. 11月9日"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "El 8 de noviembre dura de 10:00 a 18:00: 8 horas.",
     "11月8日開放幾小時?", opts=["A. 6小時", "B. 8小時", "C. 10小時"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "6 + 8 + 8 + 8 = 30 horas en total.",
     "展期4天,總開放時數是多少?", opts=["A. 24小時", "B. 28小時", "C. 30小時"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "El 6 de noviembre abre al mediodía, no a las 10:00.",
     "旅展首日幾點開門?", opts=["A. 中午12點", "B. 上午10點", "C. 下午2點"], size=22.5, gap=8)
e.head("深讀測驗 · Preguntas a fondo", 28)
e.ex("B2", "單選", "B", "Finanzas+ significa finanzas más tecnología.",
     "「金融＋」是什麼意思?", opts=["A. 金融業加薪", "B. 金融加上科技", "C. 金融業加班"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "La IA ayuda a leer datos, detectar riesgos y responder a los clientes.",
     "人工智慧在金融業幫忙做什麼?", opts=["A. 看數據、抓風險、回客戶問題", "B. 印鈔票", "C. 蓋銀行大樓"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "La expansión global significa vender productos en todo el mundo.",
     "「全球擴張」是幫新創公司做什麼?", opts=["A. 在香港開分店", "B. 請更多員工", "C. 把產品賣到世界各地"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "Participan más de 1.000 ponentes.",
     "金融科技週有幾位以上講者?", opts=["A. 100位", "B. 1,000位", "C. 10,000位"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "La conferencia principal dura los días 2 y 3 de noviembre.",
     "金融科技週主會議是哪兩天?", opts=["A. 11月2、3日", "B. 11月5、6日", "C. 11月7、8日"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "Los eventos comunitarios son más de 100 durante la semana.",
     "金融科技週整週有多少場以上社區活動?", opts=["A. 10場", "B. 50場", "C. 100場"], size=22.5, gap=8)
e.head("填一填 · Completa", 28)
e.ex("B2", "完成句子", "支付", "Los pagos son uno de los temas de la conferencia principal.",
     "主會議主題包括___、數位資產、財富科技、保險科技。", instr="Completa", size=22.5, gap=8)
e.ex("B2", "完成句子", "數位資產", "Los activos digitales son un tema de la conferencia principal.",
     "主會議主題包括支付、___、財富科技、保險科技。", instr="Completa", size=22.5, gap=8)
e.ex("B2", "完成句子", "保險科技", "La tecnología de seguros es un tema de la conferencia principal.",
     "主會議主題包括支付、數位資產、財富科技、___。", instr="Completa", size=22.5, gap=8)
e.ex("B2", "完成句子", "牽線", "La semana conecta a las empresas emergentes con el mundo.",
     "金融科技週幫新創公司___、走向世界。", instr="Completa", size=22.5, gap=8)
e.ex("B2", "完成句子", "30", "Horas totales de apertura: 30.",
     "旅展4天總開放時數是___小時。", instr="Completa", size=22.5, gap=8)
e.ex("B2", "完成句子", "12", "El 6 de noviembre abre al mediodía (12:00).",
     "旅展首日中午___點才開門。", instr="Completa", size=22.5, gap=8)
e.ex("B2", "完成句子", "1,600", "La feria de viajes tiene 1.600 casetas.",
     "台北旅展有___個攤位。", instr="Completa", size=22.5, gap=8)
e.ex("B2", "完成句子", "45,000", "Se esperan más de 45.000 personas.",
     "金融科技週預計逾___人參加。", instr="Completa", size=22.5, gap=8)
e.end_report()

rx = COLX[3]
by = 208
p.rect(rx, by, CW, 620, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "數字一覽 · Las cifras", 25, "sans", True, OLIVE); yy += 56
for t in [
    "參加人數:逾45,000人",
    "經濟體:120多個",
    "講者:逾1,000人",
    "參展商和新創:逾800家",
    "代表團:逾30個",
    "社區活動:100多場",
    "主會議:11月2、3日,香港會議展覽中心",
    "專題論壇:10個",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by2 = by + 620 + 18
p.rect(rx, by2, CW, 504, fill=BOX, stroke=LINE, sw=1.4)
yy = by2 + 18
p.text(rx + 22, yy + 26, "比價提醒 · Compara con cuidado", 25, "sans", True, OLIVE); yy += 56
yy = p.para(rx + 22, yy + 24, "報導整理的例子:國泰航空東京來回含稅13,433元起,購票到11月13日。廉航最低票價通常不含託運行李,加上行李費再比較。", 22, "serif", False, INK, CW - 44, 1.36) + 6
p.para(rx + 22, yy + 21, "Ejemplo de notas de prensa (20 de octubre): vuelo de ida y vuelta Taipéi-Tokio con Cathay Pacific desde 13.433 NT$ con impuestos incluidos, reserva hasta el 13 de noviembre. Compara siempre sumando las tasas de equipaje, y comprueba el resultado de la reserva en directo, ya que los precios varían según la fecha.", 19.5, "sans", False, GREY, CW - 44, 1.35)
p.foot(6)
p.save(f"{OUT}/p6-deep.svg")
print("P6 saved, exercises so far:", len(REG))
