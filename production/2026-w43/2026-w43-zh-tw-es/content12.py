# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-es/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P1 · front
CURPAGE[0] = 1
p = BSPage4()
p.text(975, 218, "Lucerna", 168, "serif", True, INK, anchor="middle", family="UnifrakturMaguntia")
p.hline(MX, RIGHT, 268, INK, 3)
p.text(975, 316, "繁體中文版 · VOL.1 · 2026年10月19日(一)至10月25日(日) · 台灣 / 香港", 27, "sans", False, GREY, anchor="middle")
p.hline(MX, RIGHT, 340, GOLD, 2)
p.text(975, 378, "TEXTOS EN CHINO TRADICIONAL · EXPLICACIONES EN ESPAÑOL — LA EDICIÓN PARA LOS LECTORES HISPANOHABLANTES", 21, "sans", True, BRICK, anchor="middle")
p.text(975, 410, "颱風 · 連假 · 金鐘獎 · 台灣大賽——本週最忙的一週", 30, "sans", True, BRICK, anchor="middle")
hl = "強颱薔琵壓境!週五、週六風雨最大"
p.text(975, 518, hl, 96, "serif", True, INK, anchor="middle")
if text_w(hl, "serif", True, 96) > RIGHT - MX:
    print("  !! P1 HEADLINE TOO WIDE", text_w(hl, "serif", True, 96))
p.text(975, 572, "海上警報最快週三晚間發佈 · 北台灣先轉涼 · 光復節連假週六開始", 27, "serif", False, GREY, anchor="middle")

f = Flow(p, [(COLX[0], 3 * CW + 2 * GUT)], 640, 1935, tag="P1-lead")
f.title("薔琵走到哪裡了?", 40)
f.byline("Reportaje de la redacción · Fuente: Administración Meteorológica Central (según los medios) · Noche del 20 de octubre")
f.para("強烈颱風「薔琵」正朝台灣東邊的海面走來。10月20日(二)晚上,颱風中心在鵝鑾鼻東南東方約1,390公里,近中心最大風速約每秒60公尺,暴風半徑280公里,是個又大又強的颱風。")
f.para("更麻煩的是東北季風。颱風的外圍環流加上季風,叫作「共伴效應」,雨會下得更大、更久。中央氣象署說,海上颱風警報最快週三(10月21日)晚間發佈;陸上颱風警報可能在週五(10月23日)發佈。週五、週六(10月23、24日)颱風最接近台灣,風雨最大,北部、東北部和東部要防大雨或豪雨。")
f.para("數字也會說話:未來120小時的暴風侵襲機率,以基隆72%、宜蘭71%最高。意思是:北邊和東北邊的縣市,最要小心。")
f.para("颱風還沒到,北台灣先變天。週三起東北季風增強,白天高溫約29度,清晨只有20到21度,早晚溫差大,出門記得帶一件外套。很多人關心:會不會放颱風假?要看風雨,各縣市會再宣佈停班停課。")
f.para("氣象署提醒,這幾天的雨量要看颱風走得多快。路徑還有變數,會不會登陸,還沒有人知道。出門前,先看最新的警報和預報,再決定行程。")
f.para("颱風也改了這一週的日程:天母的萬聖節踩街改到週日晚上(見第5版);金鐘獎主辦單位也說,正密切注意颱風,兩晚典禮照常準備(見第5版)。")
f.gloss("El tifón Jangmi se acerca al mar al este de Taiwán. Junto con el monzón del noreste (el «efecto conjunto»), la lluvia será más intensa y durará más. El aviso marítimo podría emitirse el miércoles por la noche; el viernes y el sábado serán los días de más viento y lluvia.")
f.end_report()

rx = COLX[3]
image(p, "typhoon.jpg", rx, 640, CW, 300)
caption(p, rx, 640 + 300 + 6, CW, "颱風的「眼睛」:從國際太空站拍到的颱風(資料照片,非本週的薔琵)。",
        "Photo: NASA Johnson Space Center — Public domain (Wikimedia Commons)")
by = 640 + 300 + 128
p.rect(rx, by, CW, 560, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "本週大事 · Esta semana", 25, "sans", True, OLIVE); yy += 58
for t in [
    "週一 10/19 香港重陽節翌日公眾假期",
    "週二 10/20 台灣大賽 G3(臺北大巨蛋)",
    "週三 10/21 海上警報可能發佈;G4",
    "週四 10/22 天母店週年慶開跑",
    "週五 10/23 金鐘獎節目類;疏運開始",
    "週六 10/24 金鐘獎戲劇類;連假開始",
    "週日 10/25 天母百鬼夜行踩街 19:00",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.3) + 9
p.rect(rx, by + 578, CW, 218, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 578 + 18
p.text(rx + 22, yy + 26, "本週一詞 · Palabra de la semana", 25, "sans", True, OLIVE); yy += 56
p.para(rx + 22, yy + 21, "「颱風假」 — un «día de tifón»: cuando el viento y la lluvia alcanzan el nivel establecido, las ciudades y los condados pueden anunciar un día sin trabajo ni clases.", 20, "sans", False, GREY, CW - 44, 1.35)

q = Flow(p, [(COLX[i], CW) for i in range(4)], 2035, 2540, tag="P1-quiz")
q.head("快速測驗 · Quiz rápido", 26)
q.ex("A2", "單選", "B", "Jangmi es un tifón fuerte (severo).",
     "薔琵現在是什麼等級?", opts=["A. 輕度颱風", "B. 強烈颱風", "C. 熱帶低壓"], size=22.5, gap=8)
q.ex("A2", "單選", "B", "El aviso marítimo podría llegar el miércoles por la noche.",
     "海上颱風警報最快什麼時候發佈?", opts=["A. 週一晚上", "B. 週三晚間", "C. 週六早上"], size=22.5, gap=8)
q.ex("A2", "單選", "B", "Viernes y sábado: máxima cercanía, el peor tiempo.",
     "風雨最大的兩天是?", opts=["A. 週二、週三", "B. 週五、週六", "C. 週日、週一"], size=22.5, gap=8)
q.ex("A2", "單選", "A", "Keelung tiene la mayor probabilidad de impacto: 72%.",
     "基隆的暴風侵襲機率是多少?", opts=["A. 72%", "B. 60%", "C. 28%"], size=22.5, gap=8)
q.head("標題填空 · Palabras de titulares", 26)
q.ex("A2", "完成句子", "東南", "El centro estaba al sureste de Eluanbi.",
     "颱風中心在鵝鑾鼻___東方約1,390公里。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "共伴", "Tifón + monzón = el «efecto conjunto».",
     "颱風加東北季風,叫作「___效應」。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "60", "Vientos máximos cerca del centro: unos 60 m/s.",
     "近中心最大風速約每秒___公尺。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "280", "El radio de la tormenta es de 280 km.",
     "薔琵的暴風半徑是___公里。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "71", "La probabilidad de impacto de Yilan es del 71%.",
     "宜蘭的暴風侵襲機率是___%。", instr="Completa", size=22.5, gap=8)
q.ex("A2", "完成句子", "陸上", "El aviso terrestre podría seguir el viernes.",
     "週五可能發佈的是___颱風警報。", instr="Completa", size=22.5, gap=8)
q.end_report()
p.foot(1)
p.save(f"{OUT}/p1-front.svg")
print("P1 saved, exercises so far:", len(REG))

# ============================================================ P2 · life
CURPAGE[0] = 2
p = BSPage4()
p.band("生活 · Vida cotidiana", "Lucerna", "第 2 版 · 天氣、假期與週年慶 · Tiempo, vacaciones y la venta aniversario")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P2-main")
f.title("颱風天,出門前先做三件事", 34)
f.para("第一,看警報。颱風還在海上,先發佈海上颱風警報;颱風靠近陸地,再發佈陸上颱風警報。警報一出,海邊和山區都不要去。")
f.para("第二,看宣佈。你住的縣市有沒有停班停課?各縣市會看風雨決定,前一晚或當天早上公佈。第三,帶雨具、穿外套。週四(10月22日)起,薔琵的外圍環流讓雨勢擴大,北台灣一整週都容易下雨。")
f.gloss("Tres cosas antes de salir: mira los avisos, mira el anuncio de tu ciudad sobre trabajo y clases, y lleva impermeable y una chaqueta.")
f.title("香港的九天長假,怎麼來的?", 34)
f.para("香港週一(10月19日)是重陽節翌日公眾假期。旅遊網站教大家一個方法:請四天假,換九天連假。請的是10月20日到23日(二到五)四天;前後接上週末,再加上週一的假期,10月17日到25日,一共放九天。")
f.para("九天怎麼算?週末兩天,加假期一天,加請假四天,再加週末兩天:2+1+4+2=9。很多人用這九天去旅行,也有人留港休息、登高、吃大閘蟹。")
f.gloss("El truco de Hong Kong: pide 4 días (de martes a viernes) entre una fiesta en lunes y dos fines de semana, y tendrás 9 días libres: 2+1+4+2 = 9.")
f.title("連假出門:疏運五天,活動收官", 34)
f.para("台灣這邊,光復節連假從週六(10月24日)到下週一(10月26日):週日是光復節,週一補假,一共三天。台鐵、高鐵的連假疏運期從週五(10月23日)到週二(10月27日),一共五天,會加開班次載大家回家、出遊。")
f.para("連假也是秋季活動的收官週末:臺中爵士音樂節(10月16日到25日)最後一個週末;池上秋收稻穗藝術節在10月24、25日兩天,在金黃的稻田邊看表演。福隆沙雕季到10月26日結束,下期再報。")
f.gloss("El fin de semana largo de Taiwán va de sábado a lunes (24-26 de octubre). Los trenes circulan 5 días en operativo especial con más servicios, y los festivales de otoño llegan a su último fin de semana.")
f.title("週年慶購物攻略:先看日期,再看回饋", 34)
f.para("台灣百貨公司一年一度的大檔期「週年慶」正在最高峰。新光三越首波六店(台北南西、桃園站前、台中中港、嘉義垂楊、台南小北門、高雄三多)從10月1日到10月25日;台北天母店週四(10月22日)開跑;台中中港店、桃園站前店週日(10月25日)是最後一天,要買要快。信義新天地則到11月8日。")
f.para("La oferta más común es «滿千送百» («por cada 1.000, 100 de regalo»): por cada 1.000 NT$ que gastes, la tienda te devuelve 100 NT$ en vales o puntos. Haz las cuentas antes de comprar: un reembolso solo ahorra si de verdad lo usas.")
f.box("練習例子 · Ejemplo práctico", [
    ("阿May買了一個包包3,200元、一雙鞋1,800元,一共5,000元。滿千送百:5,000 ÷ 1,000 = 5,她可以拿到 5 × 100 = 500 元回饋。", "serif", False, INK, 22, 1.4),
    ("Cifras del ejemplo: 3.200 NT$ + 1.800 NT$ = 5.000 NT$, así que la regla «por cada 1.000, 100» devuelve 500 NT$.", "sans", False, GREY, 19.5, 1.35),
])
f.head("讀懂了嗎? · ¿Entendido?", 28)
f.ex("A2", "單選", "A", "Las ciudades y los condados anuncian las suspensiones de trabajo y clases.",
     "停班停課是誰宣佈的?", opts=["A. 各縣市", "B. 百貨公司", "C. 氣象署"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "Los días pedidos son del 20 al 23 de octubre (de martes a viernes).",
     "香港人「請4放9」請的是哪四天?", opts=["A. 10月20日到23日", "B. 10月19日到22日", "C. 10月23日到26日"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "Los 9 días van del 17 al 25 de octubre.",
     "九天長假從哪天到哪天?", opts=["A. 10月17日到25日", "B. 10月19日到27日", "C. 10月20日到28日"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "El fin de semana largo dura 3 días: de sábado a lunes.",
     "光復節連假一共幾天?", opts=["A. 2天", "B. 3天", "C. 4天"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "El descanso empieza el sábado 24 de octubre.",
     "連假第一天是星期幾?", opts=["A. 週五", "B. 週六", "C. 週日"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "El último día de la venta en Zhonggang, Taichung, es el domingo 25 de octubre.",
     "台中中港店週年慶最後一天是?", opts=["A. 週四", "B. 週六", "C. 週日(10月25日)"], size=22.5, gap=8)
f.head("填一填 · Completa", 28)
f.ex("A2", "完成句子", "警報", "Consulta primero el último aviso y el pronóstico.",
     "出門前,先看最新的___和預報。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "補假", "La fiesta del domingo se compensa el lunes.",
     "週日是光復節,週一___,所以連放三天。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "4", "Cuatro días pedidos hacen el descanso de 9 días.",
     "「請4放9」要請___天假。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "外圍", "La circulación exterior del tifón trae la lluvia.",
     "颱風的___環流加上季風,雨會更大。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "送百", "Por cada 1.000, te devuelven 100: 滿千送百.",
     "每滿1,000元送100元,叫作「滿千___」。", instr="Completa", size=22.5, gap=8)
f.head("算一算 · A calcular", 28)
f.ex("A2", "單選", "B", "5.000 / 1.000 = 5 tramos, por 100 = 500 de vuelta.",
     "練習:買5,000元的東西,滿千送百可拿回多少?", opts=["A. 100元", "B. 500元", "C. 1,000元"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "9 días en total menos 4 pedidos = 5 días ya libres.",
     "九天長假裡,不用請假的日子有幾天?", opts=["A. 4天", "B. 5天", "C. 6天"], size=22.5, gap=8)
f.ex("A2", "完成句子", "5", "Del 23 al 27 de octubre, inclusive: 5 días de operativo de transporte.",
     "疏運期10月23日到27日,一共___天。", instr="Completa", size=22.5, gap=8)
f.match_set("A2", "配對",
            ["連假", "補假", "疏運", "回饋"],
            ["連著放假的好幾天", "假日逢週末,平日多放一天", "連假時加開班次,載大家出門回家", "買東西送的券或點數"],
            ["a", "b", "c", "d"],
            ["連假 — una serie de días libres seguidos.",
             "補假 — un día libre de compensación cuando la fiesta cae en fin de semana.",
             "疏運 — el transporte extra organizado para los viajes de las fiestas.",
             "回饋 — los vales o puntos que devuelve una tienda."],
            instr="Une palabra y definición")
f.end_report()

rx = COLX[3]
image(p, "rain.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "雨天出門,傘要帶牢(資料照片)。",
        "Photo: CorraleH — CC0 (Wikimedia Commons)")
by = 208 + 300 + 96
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "事實框 · Los datos de la semana", 24, "sans", True, OLIVE); yy += 56
for t in [
    "週三起:北台灣轉涼,白天約29度、清晨20到21度",
    "週四起:外圍環流到,雨勢擴大",
    "週五、週六:風雨最大,防大雨或豪雨",
    "連假:10月24日(六)到26日(一)",
    "疏運:10月23日到27日,共五天",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 230, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢? · Ahora tú", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你住的地方這週會下雨嗎?連假你想去哪裡?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "¿Lloverá esta semana donde vives? ¿Adónde irías en un puente de 3 días?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 230 + 18
p.rect(rx, by3, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
yy = by3 + 18
p.text(rx + 22, yy + 26, "收官活動 · Últimos eventos", 25, "sans", True, OLIVE); yy += 56
for t in [
    "臺中爵士音樂節:最後週末,10月25日閉幕",
    "池上秋收稻穗藝術節:10月24、25日",
    "清境火把節:10月24、25日",
    "福隆國際沙雕藝術季:展到10月26日",
    "颱風週注意:活動可能再改期,出門先查公告",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(2)
p.save(f"{OUT}/p2-life.svg")
print("P2 saved, exercises so far:", len(REG))
