# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2, issue week Mon 2026-11-02 to Sun 2026-11-08.
# All target text written natively for the Taiwan / Hong Kong ecosystem.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-es/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P1 · front
CURPAGE[0] = 1
p = BSPage4()
p.text(975, 218, "Lucerna", 168, "serif", True, INK, anchor="middle", family="UnifrakturMaguntia")
p.hline(MX, RIGHT, 268, INK, 3)
p.text(975, 316, "繁體中文版 · VOL.2 · 2026年11月2日(一)至11月8日(日) · 台灣 / 香港", 27, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 340, GOLD, 2)
p.text(975, 378, "TEXTOS EN CHINO TRADICIONAL · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 21, "sans", True, BRICK, anchor="middle")
p.text(975, 410, "金融科技週 · 台北旅展 · 味全龍封王——本週台港最熱的三件事", 30, "sans", True, BRICK, anchor="middle")
hl = "金融科技週開幕!香港迎四萬五千人"
p.text(975, 518, hl, 96, "serif", True, INK, anchor="middle")
if text_w(hl, "serif", True, 96) > RIGHT - MX:
    print("  !! P1 HEADLINE TOO WIDE", text_w(hl, "serif", True, 96))
p.text(975, 572, "主會議在灣仔會展中心 · 逾千講者、八百參展商 · 週五台北旅展接棒", 27, "serif", False, GREY, anchor="middle")

f = Flow(p, [(COLX[0], 3 * CW + 2 * GUT)], 640, 1935, tag="P1-lead")
f.title("香港金融科技週,週一開幕", 40)
f.byline("Reportaje de la redacción · Fuente: comunicado de prensa de los organizadores (23 de octubre) y preguntas frecuentes del evento")
f.para("香港金融科技週 x StartmeupHK 2026,週一(11月2日)在香港開幕,一連五天到週五(11月6日)。主會議和展覽在香港會議展覽中心,11月2、3日兩天;整週還有100多場社區活動,遍佈香港多個場地。")
f.para("規模很大:預計逾45,000人參加,來自120多個經濟體,講者逾1,000人,參展商和新創公司逾800家,代表團逾30個。今年的主題是 Fintech Nexus: Bridging the World, Building the Future,三大方向是金融＋、人工智慧＋、全球擴張。")
f.para("什麼是金融科技?用手機轉帳、掃碼付款、網上買保險,都是金融科技。人工智慧讓銀行、投資、保險跑得更快、更聰明;「全球擴張」是幫新創公司把生意做到世界各地。對學中文的你來說,這三個詞很好用:金融科技、人工智慧、全球擴張。")
f.para("主會議有10個專題論壇,主題包括支付、數位資產、財富科技、保險科技。想入門的人不用怕:先聽一場主題演講,再去展區看一家新創公司怎麼做產品,一天就很有收穫。")
f.gloss("La Semana FinTech de Hong Kong x StartmeupHK 2026 abre el lunes (2 de noviembre) y dura hasta el viernes (6 de noviembre). La conferencia principal y la exposición se celebran en el Centro de Convenciones y Exposiciones de Hong Kong los días 2 y 3 de noviembre, con más de 100 eventos comunitarios durante la semana. Se esperan más de 45.000 personas de más de 120 economías, más de 1.000 ponentes y más de 800 expositores y empresas emergentes.")
f.title("週五,台北旅展也開幕", 40)
f.para("週五(11月6日)中午12點,2026 ITF 台灣國際旅展在台北南港展覽館一館開幕,展到下週一(11月9日)。123個國家及城市、1,600個攤位,從年末聚餐、親子出遊、冬季泡湯,到山林慢旅,一次看完。")
f.para("旅展不只賣票:大會舞台有多國文化展演,每日下午2點有吉祥物大遊行,還有旅遊產品說明會,主題包括西班牙朝聖之路、日本自由行、極光與南北極探險。想學中文的人,逛旅展也是練聽力:每個攤位都是一堂生活中文課。")
f.gloss("La Feria Internacional de Viajes de Taipéi (ITF) abre el viernes (6 de noviembre) al mediodía en el Centro de Exposiciones de Nangang y dura hasta el lunes (9 de noviembre): 123 países y ciudades, 1.600 casetas, un desfile diario de mascotas a las 14:00 y charlas de viajes.")
f.end_report()

rx = COLX[3]
image(p, "harbour.jpg", rx, 640, CW, 300)
caption(p, rx, 640 + 300 + 6, CW, "香港維港的天際線(資料照片)。金融科技週的主會議就在灣仔的會展中心。",
        "Photo: Wilfredor — CC0 (Wikimedia Commons)")
by = 640 + 300 + 128
p.rect(rx, by, CW, 560, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "本週大事 · Esta semana", 25, "sans", True, OLIVE); yy += 58
for t in [
    "週一 11/2 香港金融科技週開幕",
    "週二 11/3 金融科技週主會議第二天",
    "週五 11/6 台北國際旅展開幕 12:00",
    "週六 11/7 立冬,冬天要來了",
    "週日 11/8 旅展第三天;吉祥物大遊行 14:00",
    "上週回顧:10/26 味全龍封王;福隆沙雕落幕",
    "上週回顧:美酒佳餚巡禮 11/1 落幕",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.3) + 9
p.rect(rx, by + 578, CW, 218, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 578 + 18
p.text(rx + 22, yy + 26, "本週一詞 · Palabra de la semana", 25, "sans", True, OLIVE); yy += 56
p.para(rx + 22, yy + 21, "「金融科技」 — fintech: usar la tecnología para gestionar servicios financieros, como pagar con el móvil o escanear un código para pagar.", 20, "sans", False, GREY, CW - 44, 1.35)

q = Flow(p, [(COLX[i], CW) for i in range(4)], 2035, 2540, tag="P1-quiz")
q.head("快速測驗 · Cuestionario rápido", 26)
q.ex("A2", "單選", "B", "La Semana FinTech abre el lunes 2 de noviembre.",
     "香港金融科技週哪天開幕?", opts=["A. 週五", "B. 週一(11月2日)", "C. 週六"], size=22.5, gap=8)
q.ex("A2", "單選", "A", "La conferencia principal se celebra en el Centro de Convenciones y Exposiciones de Hong Kong.",
     "主會議和展覽在哪裡?", opts=["A. 香港會議展覽中心", "B. 台北南港展覽館", "C. 高雄駁二"], size=22.5, gap=8)
q.ex("A2", "單選", "C", "Se esperan más de 45.000 personas.",
     "金融科技週預計有多少人參加?", opts=["A. 約5,000人", "B. 約15,000人", "C. 逾45,000人"], size=22.5, gap=8)
q.ex("A2", "單選", "B", "La feria de viajes abre el viernes 6 de noviembre al mediodía.",
     "台北國際旅展哪天開幕?", opts=["A. 週一", "B. 週五(11月6日)中午12點", "C. 週日"], size=22.5, gap=8)
q.head("標題填空 · Palabras de titulares", 26)
q.ex("A2", "完成句子", "120", "Los participantes vienen de más de 120 economías.",
     "金融科技週的參加者來自___多個經濟體。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "800", "Participan más de 800 expositores y empresas emergentes.",
     "參展商和新創公司逾___家。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "123", "La feria de viajes reúne a 123 países y ciudades.",
     "台北旅展集結___個國家及城市。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "1,600", "La feria de viajes tiene 1.600 casetas.",
     "台北旅展有___個攤位。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "立冬", "El sábado 7 de noviembre es el término solar del Inicio del Invierno.",
     "週六(11月7日)是___。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "11月9日", "La feria de viajes dura hasta el lunes 9 de noviembre.",
     "台北旅展展到下週一___。", instr="Completa", size=22.5, gap=8)
q.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ============================================================ P2 · life
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · Vida cotidiana", "Lucerna", "第 2 版 · 天氣、泡湯、旅展與雙11 · Tiempo, aguas termales, la feria de viajes y el 11.11")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P2-main")
f.title("天氣轉涼,立冬要來了", 34)
f.para("東北季風一波一波來,北台灣早晚轉涼,出門記得多帶一件外套。週六(11月7日)是立冬,二十四節氣裡冬天開始的日子。立冬不是假期,但很多人會在這一天吃一頓熱的,幫身體「進補」。")
f.para("立冬吃什麼?台灣人常吃薑母鴨、羊肉爐、麻油雞,都是熱呼呼的鍋。吃鍋要適量:太油、太鹹都不好,腸胃不好的人,先問醫生再進補。")
f.gloss("El monzón del noreste enfría el norte de Taiwán, y el sábado (7 de noviembre) es Lidong, el Inicio del Invierno: el día en que empieza el invierno en los 24 términos solares. Mucha gente lo celebra con una comida caliente y nutritiva en olla.")
f.title("秋冬怎麼玩?泡湯、登山、集章", 34)
f.para("秋冬是泡湯的好季節。北投、宜蘭都有溫泉,旅展現場也有溫泉住宿券,先比價再下手。登山也不錯:觀光署在旅展打造國家形象館,現場收錄56條精選路線的「步道大百科」,教你從海岸、淺山走到森林、雲海。")
f.para("喜歡集章的人,主辦單位推出「來台灣走走!6大綠道集章挑戰」,6處集章點是淡蘭古道、樟之細路、山海圳、百年大圳、原民古道、糖鐵國家綠道。集滿6個章,可以拿到限定貼紙,還能參加抽獎。")
f.gloss("El otoño y el invierno son para las aguas termales y el senderismo. La enciclopedia de senderos de la feria reúne 56 rutas, y el reto de sellos de las 6 Vías Verdes cubre los senderos Tamsui-Kavalan, Raknus Selu, de la Montaña al Mar, del Centenario, Indígena y del Ferrocarril Azucarero.")
f.title("雙11快到了,先想好再買", 34)
f.para("下週三(11月11日)是雙11,電商早就開始暖身。買東西之前,先列清單、設預算:需要才買,不要為了折扣買一堆用不到的東西。比價也要看清楚:含稅嗎?運費多少?能不能退貨?三個問題問完,再結帳。")
f.box("練習例子 · Ejemplo práctico", [
    ("小安的預算有4,000元。她看中一件外套2,400元、一雙鞋1,600元,加起來正好4,000元,沒有超過預算,可以買。", "serif", False, INK, 22, 1.4),
    ("Cifras del ejemplo: 2.400 NT$ + 1.600 NT$ = 4.000 NT$, justo su presupuesto; así que puede comprar las dos cosas.", "sans", False, GREY, 19.5, 1.35),
])
f.head("讀懂了嗎? · ¿Entendido?", 28)
f.ex("A2", "單選", "A", "Lidong, el Inicio del Invierno, es el sábado 7 de noviembre.",
     "立冬是哪一天?", opts=["A. 週六(11月7日)", "B. 週五(11月6日)", "C. 週日(11月8日)"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "El monzón del noreste enfría el norte de Taiwán.",
     "北台灣轉涼,主要是哪個風的影響?", opts=["A. 西南風", "B. 東北季風", "C. 颱風"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "La enciclopedia de senderos reúne 56 rutas.",
     "「步道大百科」收錄幾條路線?", opts=["A. 56條", "B. 16條", "C. 6條"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "El reto de sellos tiene 6 Vías Verdes.",
     "6大綠道集章挑戰有幾個集章點?", opts=["A. 4個", "B. 6個", "C. 9個"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "El Doble 11 cae el miércoles 11 de noviembre.",
     "雙11是下週星期幾?", opts=["A. 週一", "B. 週二", "C. 週三(11月11日)"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "Antes de pagar, comprueba los impuestos, el envío y las devoluciones.",
     "結帳前要問清楚哪三件事?", opts=["A. 含稅嗎?運費多少?能不能退貨?", "B. 顏色好看嗎?包裝大嗎?", "C. 店員親切嗎?"], size=22.5, gap=8)
f.head("填一填 · Completa", 28)
f.ex("A2", "完成句子", "進補", "Una comida caliente en olla celebra Lidong: 進補.",
     "立冬吃一頓熱的,叫作___。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "外套", "Recuerda la chaqueta: las mañanas y las noches refrescan.",
     "早晚轉涼,出門記得帶一件___。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "泡湯", "El otoño y el invierno son buenos para las aguas termales.",
     "秋冬是___的好季節。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "集章", "Colecciona sellos en las 6 Vías Verdes.",
     "6大綠道可以玩___挑戰。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "預算", "Fija un presupuesto antes de comprar en el Doble 11.",
     "買東西之前,先列清單、設___。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "淡蘭古道", "El sendero Tamsui-Kavalan es una de las 6 Vías Verdes.",
     "6大綠道之一是___。", instr="Completa", size=22.5, gap=8)
f.head("算一算 · Calcula", 28)
f.ex("A2", "單選", "B", "2.400 + 1.600 = 4.000, justo el presupuesto.",
     "練習:外套2,400元加鞋1,600元,一共多少?", opts=["A. 3,000元", "B. 4,000元", "C. 5,000元"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "El presupuesto es 4.000 y el total es 4.000: nada por encima.",
     "小安有沒有超過預算?", opts=["A. 沒有,正好4,000元", "B. 超過1,000元", "C. 超過4,000元"], size=22.5, gap=8)
f.match_set("A2", "配對",
            ["立冬", "進補", "泡湯", "集章"],
            ["冬天開始的節氣", "吃熱的補身體", "去溫泉洗澡、放鬆", "在指定地點蓋章收集"],
            ["a", "b", "c", "d"],
            ["立冬 — el término solar del Inicio del Invierno.",
             "進補 — comer alimentos calientes y nutritivos para el invierno.",
             "泡湯 — bañarse en aguas termales.",
             "集章 — coleccionar sellos en puntos establecidos."],
            instr="Une palabra y definición")
f.end_report()

rx = COLX[3]
image(p, "rain.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "秋雨綿綿,出門記得帶傘(資料照片)。",
        "Photo: CorraleH — CC0 (Wikimedia Commons)")
by = 208 + 300 + 96
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "事實框 · Datos de la semana", 24, "sans", True, OLIVE); yy += 56
for t in [
    "週六 11/7:立冬,冬天開始",
    "旅展:11/6(五)到11/9(一),南港展覽館一館",
    "金融科技週:11/2(一)到11/6(五),香港",
    "雙11:下週三 11/11,先列清單再買",
    "6大綠道:集滿章,拿貼紙、參加抽獎",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 230, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢? · ¿Y tú?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "立冬你想吃什麼鍋?雙11你的購物車裡有什麼?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "¿Qué olla caliente comerías en Lidong? ¿Qué hay en tu carrito del Doble 11?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 230 + 18
p.rect(rx, by3, CW, 460, fill=BOX, stroke=LINE, sw=1.4)
yy = by3 + 18
p.text(rx + 22, yy + 26, "封王優惠 · Ofertas de campeón", 25, "sans", True, OLIVE); yy += 56
for t in [
    "味全龍封王後,合作品牌推出慶祝優惠",
    "全家便利商店:指定貝納頌商品買一送一",
    "優惠期間:10月29日到11月4日",
    "實際辦法與品項,以各品牌官方公告為準",
    "把握時間,不要為了優惠亂買",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
