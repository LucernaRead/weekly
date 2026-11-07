# -*- coding: utf-8 -*-
# W46 zh-tw core, VOL.3: P5 youth, P6 deep read.
# P5: Hong Kong Arts in the Park (Nov 14-15) + concerts + Double 11 draw.
# P6: Double 11 deep read — real amount paid, coupons, returns; chart of
# published coupon thresholds (sourced Nov 2 roundups; terms per platform).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-tw-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P5 · youth
CURPAGE[0] = 5
p = BSPage4()
p.band("青年 · Juventude", "Lucerna", "第 5 版 · 藝趣嘉年華、演唱會、抽機票 · Arts in the Park, shows e o sorteio de passagens")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P5-main")
f.title("銅鑼灣嘉年華:免費入場,兩天都好玩", 34)
f.para("週末去香港銅鑼灣,有免費的嘉年華可以玩。渣打藝趣嘉年華2026在11月14日(週六)、15日(週日)兩天,在銅鑼灣維多利亞公園中央草坪舉行,上午10點到下午5點,全場免費入場,不用門票。今年的主題是「百年童話世界」,有17個互動藝術攤位、900多件學生裝置藝術,還有4米高的木偶巡遊。")
f.para("最特別的是夜光巡遊:11月14日晚上8點30分,5隻巨型燈籠偶、18套嘉年華服飾,從利園一期正門出發,一路走到啟超道。嘉年華不用門票,全家人都能來玩,年輕人最喜歡拍照打卡,記得早一點到,才有好位置。")
f.gloss("O Standard Chartered Arts in the Park 2026 acontece sáb.-dom., 14-15 nov., no Victoria Park, Causeway Bay, das 10:00 às 17:00, entrada gratuita. Tema: um século de contos de fadas, com 17 barracas de arte interativas, mais de 900 instalações de estudantes e bonecos de 4 metros. O desfile noturno começa às 20:30 em 14 nov., a partir de Lee Gardens.")
f.title("演唱會、舞台劇,香港11月很熱鬧", 34)
f.para("香港11月也很熱鬧:衛蘭出道20週年演唱會在11月14、15、17日,地點在紅磡香港體育館。喜歡舞台劇的人,香港首部港漫改編的餐廳劇場《送書人》,11月14、15日也在灣仔上演,舞台就在餐廳裡,邊吃晚餐邊看戲。")
f.para("喜歡寶可夢的人,九龍塘又一城從11月11日開始,有寶可夢30週年活動:巨型皮卡丘氣球、10米高的精靈球燈光裝飾,還有官方快閃店。打卡之前,先看清楚活動時間,不要白跑一趟。")
f.gloss("O novembro de Hong Kong é movimentado: os shows de 20.º aniversário de Janice Vidal no Hong Kong Coliseum em 14, 15 e 17 nov.; o teatro-restaurante baseado em quadrinhos The Celestial Bookhouse em Wan Chai em 14-15 nov.; e uma mostra Pokémon de 30.º aniversário no Festival Walk a partir de 11 nov.")
f.title("雙11抽機票,年輕人最愛", 34)
f.para("雙11不只買東西,還可以抽獎。蝦皮和長榮航空的抽獎,11月11日當天抽出洛杉磯來回機票兩張,11月12、13日再抽東京、首爾來回機票。抽獎不用消費,只要完成登記,就有機會。記得:中獎是運氣,購物清單還是要先列好。")
f.box("練習例子 · Exemplo de prática", [
    ("阿傑登記了抽獎,也列好購物清單:一本書450元、一件外套1,550元,加起來2,000元,正好是他的預算。他沒有中獎,但是買到了需要的東西,沒有亂花錢。", "serif", False, INK, 22, 1.4),
    ("Números de prática: NT$ 450 + NT$ 1.550 = NT$ 2.000, exatamente o orçamento.", "sans", False, GREY, 19.5, 1.35),
])
f.head("讀懂了嗎? · Entendeu?", 28)
f.ex("B1", "單選", "B", "O Arts in the Park acontece em 14-15 nov.",
     "渣打藝趣嘉年華在哪兩天舉行?", opts=["A. 11月9、10日", "B. 11月14、15日", "C. 11月21、22日"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "A entrada é gratuita, sem ingresso.",
     "藝趣嘉年華要不要門票?", opts=["A. 不用,免費入場", "B. 要200元", "C. 要180元"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "O desfile noturno começa às 20:30 em 14 nov.",
     "夜光巡遊在11月14日晚上幾點開始?", opts=["A. 晚上6點", "B. 晚上7點", "C. 晚上8點30分"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Janice Vidal canta no Hong Kong Coliseum.",
     "衛蘭演唱會在哪裡舉行?", opts=["A. 維多利亞公園", "B. 紅磡香港體育館", "C. 灣仔餐廳"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "A mostra Pokémon abre em 11 nov.",
     "寶可夢30週年活動從哪天開始?", opts=["A. 11月11日", "B. 11月22日", "C. 11月6日"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Em 11 nov. são sorteadas duas passagens de ida e volta para Los Angeles.",
     "11月11日抽出哪裡的來回機票?", opts=["A. 東京", "B. 洛杉磯", "C. 首爾"], size=22.5, gap=8)
f.head("填一填 · Complete", 28)
f.ex("B1", "完成句子", "童話", "O tema deste ano é um século de contos de fadas.",
     "藝趣嘉年華今年的主題是「百年___世界」。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "木偶", "Bonecos de 4 metros desfilam pelo carnaval.",
     "嘉年華有4米高的___巡遊。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "打卡", "Os jovens adoram tirar fotos para o check-in.",
     "嘉年華最適合拍照___。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "登記", "Inscreva-se para participar do sorteio de passagens.",
     "抽機票只要完成___就有機會。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "預算", "As compras dele somam exatamente o orçamento.",
     "阿傑的購物清單正好是他的___。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "皮卡丘", "Um balão Pikachu gigante marca o evento Pokémon.",
     "寶可夢活動有巨型___氣球。", instr="Complete", size=22.5, gap=8)
f.head("算一算 · Calcule", 28)
f.ex("B1", "單選", "B", "450 + 1.550 = 2.000, exatamente o orçamento.",
     "練習:書450元加外套1,550元,一共多少?", opts=["A. 1,000元", "B. 2,000元", "C. 3,000元"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Fechamento às 17:00 menos abertura às 10:00 = 7 horas.",
     "嘉年華上午10點到下午5點,開放幾小時?", opts=["A. 7小時", "B. 5小時", "C. 10小時"], size=22.5, gap=8)
f.match_set("B1", "配對",
            ["嘉年華", "巡遊", "打卡", "登記"],
            ["大家一起玩的大型戶外活動", "隊伍沿著街道走給大家看", "拍照標記地點、分享到社群", "填寫資料報名參加活動"],
            ["a", "b", "c", "d"],
            ["Jiāniánhuá — um carnaval.",
             "Xúnyóu — um desfile pelas ruas.",
             "Dǎkǎ — fazer check-in com foto nas redes sociais.",
             "Dēngjì — inscrever-se num evento."],
            instr="Combine")
f.end_report()

rx = COLX[3]
by = 208
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "嘉年華小檔 · Ficha do carnaval", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日期:11月14日(六)、15日(日)",
    "時間:上午10點到下午5點",
    "地點:銅鑼灣維多利亞公園中央草坪",
    "門票:全場免費,不用門票",
    "主題:百年童話世界;17個藝術攤位",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 250, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢? · E você?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你去過嘉年華嗎?最想看夜光巡遊還是演唱會?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Você já foi a um carnaval? Prefere ver o desfile noturno ou um show?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 250 + 18
p.rect(rx, by3, CW, 450, fill=BOX, stroke=LINE, sw=1.4)
yy = by3 + 18
p.text(rx + 22, yy + 26, "香港11月節目 · Hong Kong", 25, "sans", True, OLIVE); yy += 56
for t in [
    "衛蘭演唱會:11月14、15、17日,紅磡體育館",
    "《送書人》餐廳劇場:11月14、15日,灣仔",
    "寶可夢30週年:11月11日起,又一城",
    "圓方體能競技場:11月13到15日",
    "迪士尼聖誕活動:11月17日開始(預告)",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by4 = by3 + 468
p.rect(rx, by4, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
yy = by4 + 18
p.text(rx + 22, yy + 26, "抽機票時間表 · Sorteio", 25, "sans", True, OLIVE); yy += 56
for t in [
    "10月26日到11月13日:連續19天抽獎",
    "11月11日:洛杉磯來回機票兩張",
    "11月12日:東京來回機票兩張",
    "11月13日:首爾來回機票兩張",
    "抽獎結果隔天下午6點前公布",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(5)
p.save(f"{OUT}/p5-youth.svg")
print("P5 saved, exercises so far:", len(REG))

# ============================================================ P6 · deep read
CURPAGE[0] = 6
p = BSPage4()
p.band("深讀 · Leitura a fundo", "Lucerna", "第 6 版 · 雙11深讀 + 讀圖表 · O Duplo 11 a fundo e como ler um gráfico")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 860, tag="P6-main")
f.title("雙11深讀:折扣大,不等於便宜", 34)
f.byline("Reportagem da redação · Fonte: páginas de atividades das plataformas, compiladas em 2 nov.; condições variam")
f.para("雙11的折扣數字看起來很大,但是,折扣大,不等於便宜。第一,要看門檻:滿3,000元折220元,和滿5,000元折800元,哪一個比較划算?要看你本來要買多少。第二,要看名額:很多優惠券是限量的,先領先用,領完就沒有了。第三,要看回饋是馬上折價,還是事後點數:事後點數不是馬上省錢,下次消費才能用。")
f.para("回饋不是折價,實付金額才是真的。買東西之前,先算三個數字:原價多少?折扣和回饋扣掉多少?最後真正付出去多少?三個數字算清楚,再決定要不要買。跨境購物還要多想一步:包裹2,000元以下免稅,超過要補稅,退貨也比較麻煩,先想好再下單。")
f.gloss("Grandes descontos nem sempre significam barato. Confira três coisas: o limite de gasto, a cota (muitos cupons são limitados e valem por ordem de chegada) e se a recompensa é um desconto imediato ou pontos posteriores. Cashback não é desconto — conta o valor final que você paga. Encomendas internacionais abaixo de NT$ 2.000 são isentas de imposto; acima disso, há imposto.")
f.end_report()

# ---- chart: published coupon thresholds (Nov 2 roundups) ----
chy = 900
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, GOLD, 2)
p.text(MX, chy + 28, "雙11優惠券怎麼比 · Limites dos cupons — barras em proporção ao desconto", 27, "sans", True, OLIVE)
BX = MX + 340
SCALE = 1.0
rows = [("蝦皮 滿3,000", 220), ("蝦皮11/11 滿4,800", 400), ("酷澎 滿5,000", 300), ("momo 滿5,000", 800)]
ry = chy + 62
for label, val in rows:
    p.text(MX + 20, ry + 26, label, 22, "serif", False, INK)
    p.text(BX - 14, ry + 26, "折" + str(val), 22, "serif", True, INK, anchor="end")
    p.rect(BX, ry, val * SCALE, 34, fill="#3e4c2a")
    ry += 52
chart_end = ry + 10
p.text(MX, chart_end + 24, "門檻和折扣都不同,先領券、看清楚條件再用。數字取自11月2日整理的各平台活動頁,實際辦法以各平台官方公告為準。", 21, "serif", False, GREY)
p.text(MX, chart_end + 56, "Fonte: páginas de atividades das plataformas, compiladas em 2 nov. Limites e descontos diferem; confira as condições de cada plataforma.", 20, "sans", False, GREY)

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 96, 2540, tag="P6-ex")
e.head("看圖答題 · Leia o gráfico", 28)
e.ex("B2", "單選", "A", "O cupom momo desconta NT$ 800, a maior barra.",
     "圖表裡折扣金額最大的是哪一張券?", opts=["A. momo滿5,000折800", "B. 蝦皮滿3,000折220", "C. 酷澎滿5,000折300"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "3.000 − 220 = 2.780 pagos de fato.",
     "滿3,000折220,實付金額是多少?", opts=["A. 3,000元", "B. 2,780元", "C. 2,220元"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "5.000 − 800 = 4.200 pagos de fato.",
     "滿5,000折800,實付金額是多少?", opts=["A. 5,800元", "B. 800元", "C. 4,200元"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "800 é mais que 400, mas os limites diferem: compare o que você realmente compra.",
     "折扣800元的券,一定比折扣400元的券划算嗎?", opts=["A. 不一定,要看門檻和自己要買多少", "B. 一定,數字大就划算", "C. 一定,門檻不重要"], size=22.5, gap=8)
e.head("深讀測驗 · Quiz de leitura", 28)
e.ex("B2", "單選", "B", "Muitos cupons são limitados: por ordem de chegada.",
     "很多雙11優惠券為什麼要先領?", opts=["A. 領了比較好看", "B. 限量,先領先用", "C. 不用領也可以用"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "Os pontos posteriores não são desconto imediato.",
     "事後點數回饋和馬上折價有什麼不同?", opts=["A. 點數下次才能用,不是馬上省錢", "B. 點數就是現金", "C. 沒有不同"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "Encomendas acima de NT$ 2.000 podem pagar imposto.",
     "跨境包裹超過多少錢要補稅?", opts=["A. 200元", "B. 20,000元", "C. 2,000元"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "Compare o valor final que você realmente paga.",
     "雙11比價,最重要是比什麼?", opts=["A. 折扣數字大小", "B. 實付金額", "C. 廣告好不好看"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "O sorteio Shopee-EVA vai de 26 out. a 13 nov.",
     "蝦皮抽機票活動到哪天?", opts=["A. 11月13日", "B. 11月9日", "C. 11月22日"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "A feira ITF: 123 países e cidades, 1.600 estandes.",
     "旅展集結幾個國家及城市?", opts=["A. 23個", "B. 1,600個", "C. 123個"], size=22.5, gap=8)
e.head("填一填 · Complete", 28)
e.ex("B2", "完成句子", "門檻", "Confira primeiro o limite de gasto.",
     "領券之前,先看___和名額。", instr="Complete", size=22.5, gap=8)
e.ex("B2", "完成句子", "名額", "As cotas limitadas acabam.",
     "優惠券是限量的,___用完就沒有了。", instr="Complete", size=22.5, gap=8)
e.ex("B2", "完成句子", "點數", "Os pontos posteriores são usados na próxima compra.",
     "事後回饋的___下次消費才能用。", instr="Complete", size=22.5, gap=8)
e.ex("B2", "完成句子", "實付金額", "Conta o valor final pago.",
     "比價要比___。", instr="Complete", size=22.5, gap=8)
e.ex("B2", "完成句子", "補稅", "O imposto se aplica acima de NT$ 2.000.",
     "跨境包裹超過2,000元要___。", instr="Complete", size=22.5, gap=8)
e.ex("B2", "完成句子", "原價", "Comece pelo preço original.",
     "算帳先看___多少。", instr="Complete", size=22.5, gap=8)
e.ex("B2", "完成句子", "2,780", "3,000 − 220 = 2,780.",
     "滿3,000折220,實付___元。", instr="Complete", size=22.5, gap=8)
e.ex("B2", "完成句子", "4,200", "5,000 − 800 = 4,200.",
     "滿5,000折800,實付___元。", instr="Complete", size=22.5, gap=8)
e.end_report()

rx = COLX[3]
by = 208
p.rect(rx, by, CW, 620, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "數字一覽 · Em números", 25, "sans", True, OLIVE); yy += 56
for t in [
    "旅展:123個國家及城市、1,600個攤位",
    "抽機票:23張、19天、3座城市",
    "雙11:11月11日(週三),全年最大檔",
    "鑑賞期:7天,例外先看清楚",
    "跨境免稅:2,000元以下",
    "嘉年華:17個攤位、900多件學生作品",
    "金馬報名:587部影片",
    "U幣:11月一次10個,滿100個可換儲值金",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by2 = by + 620 + 18
p.rect(rx, by2, CW, 504, fill=BOX, stroke=LINE, sw=1.4)
yy = by2 + 18
p.text(rx + 22, yy + 26, "比價三問 · Três perguntas", 25, "sans", True, OLIVE); yy += 56
yy = p.para(rx + 22, yy + 24, "第一,門檻多少?第二,名額還有嗎?第三,實付金額多少?三個問題問完,再結帳。回饋點數不是馬上折價,下次才能用。", 22, "serif", False, INK, CW - 44, 1.36) + 6
p.para(rx + 22, yy + 21, "Três perguntas antes de pagar: qual é o limite? Ainda há cota? Qual é o valor final? Os pontos vêm depois — não são desconto imediato.", 19.5, "sans", False, GREY, CW - 44, 1.35)
p.foot(6)
p.save(f"{OUT}/p6-deep.svg")
print("P6 saved, exercises so far:", len(REG))
