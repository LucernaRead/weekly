# -*- coding: utf-8 -*-
# W47 zh-tw core, VOL.4: P5 youth, P6 deep read.
# P5: Hong Kong Disneyland Christmas (Nov 17) + West Kowloon Jazz Fest.
# P6: Nov 22 deep read — four big events in one day, timeline chart.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-it/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P5 · youth
CURPAGE[0] = 5
p = BSPage4()
p.band("青年　Giovani", "Lucerna", "第5版　迪士尼聖誕　爵士音樂節　Natale a Disneyland e il festival jazz")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2560, tag="P5-main")
f.title("香港迪士尼聖誕，11月17日開始", 32)
f.para("香港迪士尼聖誕，從11月17日開始，一直放到明年1月3日，一共48天。今年魔雪奇緣世界有第一個冬日市集，可以逛市集、買聖誕禮物。11月19日起，城堡前有新的日間聖誕演出，米奇、米妮和史迪仔一起上台。晚上有聖誕樹亮燈禮，又有飄雪，又有無人機表演。")
f.para("喜歡音樂的人不要錯過：迪士尼聖誕音樂會在11月21日、22日和12月5日、6日舉行，一共4場，香港兒童合唱團和本地音樂人一起演出。香港居民有雙重暢玩限時優惠，可以任選兩天入園。")
f.gloss("Il Natale a Hong Kong Disneyland dura dal 17 nov. al 3 gen. — 48 giorni. World of Frozen ospita il suo primo mercatino invernale, un nuovo spettacolo diurno di Natale apre il 19 nov. davanti al castello (Topolino, Minnie e Stitch), e la sera c'è la cerimonia di accensione dell'albero con neve e droni. Il concerto di Natale è il 21–22 nov. e il 5–6 dic., quattro spettacoli in tutto.")
f.title("西九爵士音樂節，免費戶外舞台", 32)
f.para("第八屆國泰西九爵士音樂節是歷年最大的一次，第一次橫跨兩個週末：11月13到15日、17到22日，還有11月24日。11月13日，戴安娜·克瑞兒在戲曲中心開幕；11月15日，科里·黃和口琴手何卓彥同場；11月17日，史黛西·肯特在自由空間連開兩場；11月24日，肯尼·基在竹翠公園收尾。")
f.para("爵士音樂節不只有室內場，戶外也有免費演出：維港邊吹著海風聽爵士，草地上席地而坐，年輕人最喜歡。想去的人，先看節目表，免費場和收費場不要搞錯。")
f.gloss("L'8° Cathay West Kowloon Jazz Festival è il più grande finora e il primo su due weekend: 13–15, 17–22 e 24 nov. Diana Krall apre il 13 nov., Cory Wong suona il 15 nov., Stacey Kent il 17 nov., Kenny G chiude il 24 nov. I palchi all'aperto sul porto sono gratuiti: porta un telo da picnic e siediti sull'erba.")
f.title("寶可夢、耶誕市集，11月繼續玩", 32)
f.para("喜歡寶可夢的人，九龍塘又一城從11月11日開始，有寶可夢30週年活動：巨型皮卡丘氣球、10米高的精靈球燈光裝飾，還有官方快閃店。打卡之前，先看清楚活動時間，不要白跑一趟。")
f.para("新北耶誕城也開城了：11月13日到12月27日，德國耶誕市集在12月4日到6日登場，有異國美食和聖誕禮物。11月很熱鬧，出門之前，先列好想看的清單。")
f.gloss("La mostra per il 30° anniversario dei Pokémon a Festival Walk comincia l'11 nov.: un palloncino gigante di Pikachu, un'installazione luminosa Poké Ball alta 10 metri e un pop-up store ufficiale. New Taipei Christmasland dura dal 13 nov. al 27 dic., con il suo mercatino di Natale tedesco dal 4 al 6 dic.")
f.box("練習例子　Esempio pratico", [
    ("阿芬想去看迪士尼聖誕音樂會，音樂會在11月21日、22日和12月5日、6日舉行，一共4場。她選11月22日那場，是第2場。迪士尼聖誕從11月17日到明年1月3日，一共48天。", "serif", False, INK, 22, 1.4),
    ("Numeri per esercitarsi: 4 concerti in tutto; il 22 nov. è il 2° concerto. Dal 17 nov. al 3 gen. sono 48 giorni (14 + 31 + 3).", "sans", False, GREY, 19.5, 1.35),
])
f.head("讀懂了嗎？　Hai capito?", 25)
f.ex("B1", "單選", "B", "Il Natale Disney dura dal 17 nov. al 3 gen.",
     "香港迪士尼聖誕從哪天開始？", opts=["A. 11月11日", "B. 11月17日", "C. 11月22日"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Il mercatino invernale è a World of Frozen.",
     "魔雪奇緣世界今年有什麼新東西？", opts=["A. 第一個冬日市集", "B. 新的雲霄飛車", "C. 新的水上樂園"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "Stacey Kent suona il 17 nov. al FreeSpace.",
     "史黛西·肯特在哪天演出？", opts=["A. 11月13日", "B. 11月15日", "C. 11月17日"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Kenny G chiude il festival il 24 nov.",
     "爵士音樂節誰收尾？", opts=["A. 戴安娜·克瑞兒", "B. 肯尼·基", "C. 科里·黃"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "La mostra Pokémon apre l'11 nov.",
     "寶可夢30週年活動從哪天開始？", opts=["A. 11月11日", "B. 11月22日", "C. 11月6日"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Il concerto di Natale prevede 4 spettacoli in tutto.",
     "迪士尼聖誕音樂會一共幾場？", opts=["A. 2場", "B. 4場", "C. 6場"], size=22.5, gap=8)
f.head("填一填　Completare", 25)
f.ex("B1", "完成句子", "市集", "World of Frozen ospita il suo primo mercatino invernale.",
     "魔雪奇緣世界有第一個冬日___。", instr="Completare", size=22.5, gap=8)
f.ex("B1", "完成句子", "亮燈禮", "La cerimonia di accensione dell'albero chiude la serata.",
     "晚上有聖誕樹___。", instr="Completare", size=22.5, gap=8)
f.ex("B1", "完成句子", "爵士", "Jazz sul porto, gratis all'aperto.",
     "西九音樂節是___音樂節。", instr="Completare", size=22.5, gap=8)
f.ex("B1", "完成句子", "免費", "I palchi all'aperto sono gratuiti.",
     "戶外舞台是___的。", instr="Completare", size=22.5, gap=8)
f.ex("B1", "完成句子", "皮卡丘", "Un palloncino gigante di Pikachu segna l'evento Pokémon.",
     "寶可夢活動有巨型___氣球。", instr="Completare", size=22.5, gap=8)
f.ex("B1", "完成句子", "耶誕", "Il mercatino di Natale tedesco è dal 4 al 6 dic.",
     "新北耶誕城有德國___市集。", instr="Completare", size=22.5, gap=8)
f.head("算一算　Calcola", 25)
f.ex("B1", "單選", "B", "Dal 17 al 30 nov. sono 14 giorni, più 31 a dicembre, più 3 a gennaio = 48.",
     "迪士尼聖誕11月17日到明年1月3日，一共幾天？", opts=["A. 38天", "B. 48天", "C. 58天"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Dal 17 al 22 nov. inclusi sono 6 giorni.",
     "爵士音樂節第二週11月17日到22日，一共幾天？", opts=["A. 6天", "B. 5天", "C. 7天"], size=22.5, gap=8)
f.match_set("B1", "配對",
            ["市集", "亮燈禮", "爵士", "打卡"],
            ["賣東西、逛街的地方", "點亮聖誕樹的儀式", "一種自由的音樂", "拍照標記地點、分享到社群"],
            ["a", "b", "c", "d"],
            ["市集 — un mercato.",
             "亮燈禮 — la cerimonia di accensione dell'albero.",
             "爵士 — musica jazz.",
             "打卡 — fare check-in con una foto sui social media."],
            instr="Abbinare")
f.end_report()

rx = COLX[3]
image(p, "harbour.jpg", rx, 208, CW, 300)
by = caption(p, rx, 208 + 300 + 6, CW, "一百多年前的維多利亞港（資料照片）。香港今昔，海一樣藍。",
        "Foto: autore sconosciuto — pubblico dominio (Wikimedia Commons)") + 18
p.rect(rx, by, CW, 470, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "迪士尼聖誕小檔　Scheda Disney", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日期：11月17日到明年1月3日，一共48天",
    "冬日市集：魔雪奇緣世界，第一個",
    "新演出：11月19日起，城堡前日間演出",
    "亮燈禮：晚上，聖誕樹亮燈、飄雪、無人機",
    "音樂會：11月21、22日和12月5、6日",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 250, fill=BOX)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢？　E tu?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你最想看迪士尼聖誕，還是爵士音樂節？", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Preferiresti vedere il Natale a Disneyland o il festival jazz?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 250 + 18
p.rect(rx, by3, CW, 418, fill=BOX)
yy = by3 + 18
p.text(rx + 22, yy + 26, "香港11月節目　Hong Kong", 25, "sans", True, OLIVE); yy += 56
for t in [
    "迪士尼聖誕：11月17日起，大嶼山",
    "爵士音樂節：11月13到15日、17到22日、24日",
    "寶可夢30週年：11月11日起，又一城",
    "圓方體能競技場：11月13到15日",
    "迪士尼聖誕音樂會：11月21、22日",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by4 = by3 + 436  # fix2: HK box shrank 480->418 (one 61.7px row removed); keeps the 18px gap
p.rect(rx, by4, CW, 430, fill=BOX)
yy = by4 + 18
p.text(rx + 22, yy + 26, "爵士音樂節時間表　Date del jazz", 25, "sans", True, OLIVE); yy += 56
for t in [
    "11月13日：戴安娜·克瑞兒開幕，戲曲中心",
    "11月15日：科里·黃、何卓彥，戲曲中心",
    "11月17日：史黛西·肯特，自由空間",
    "11月24日：肯尼·基收尾，竹翠公園",
    "戶外舞台免費，室內場要買票",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(5)
p.save(f"{OUT}/p5-youth.svg")
print("P5 saved, exercises so far:", len(REG))

# ============================================================ P6 · deep read
CURPAGE[0] = 6
p = BSPage4()
p.band("深讀　Lettura approfondita", "Lucerna", "第6版　11月22日深讀　讀時間軸　Una domenica, quattro grandi eventi")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 860, tag="P6-main")
f.title("11月22日，一天四件大事", 32)
f.byline("Servizio di redazione　Fonte: annunci degli eventi, raccolti al 10 nov.")
f.para("11月22日（週日）是今年最忙的一天：下午2點，封王遊行從天母出發；下午5點，金馬獎星光大道；晚上6點30分，金馬獎頒獎典禮；晚上7點，六福村夜間遊行最後一場；同一天，高雄鋼雕藝術節閉幕，晚上8點閉館，小雪也在這一天。四件大事，同一天，一個人看不完。")
f.para("怎麼辦？先選一件，再看轉播——四件事只能取捨。遊行在街上，去現場最熱鬧；金馬獎在家看轉播，得獎名單一樣看得到；鋼雕在高雄、夜間遊行在新竹，去不了就留到下次。")
f.gloss("Domenica 22 nov. è la giornata più intensa dell'anno: la parata scudetto alle 14:00, il red carpet dei Golden Horse alle 17:00, la cerimonia alle 18:30, l'ultima parata notturna alle 19:00 — e il festival dell'acciaio chiude alle 20:00, proprio il giorno di Xiaoxue. Una persona non può vederli tutti e quattro. Scegline uno, guarda gli altri sullo schermo e controlla gli orari prima di uscire.")
f.end_report()

# ---- chart: Nov 22 timeline, 14:00-21:00 ----
chy = 900
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, OLIVE, 2)
p.text(MX, chy + 28, "11月22日時間軸　Una domenica su una linea del tempo — tutti gli orari di inizio in una riga", 27, "sans", True, OLIVE)
X0, X1 = MX + 100, COLX[0] + 3 * CW + 2 * GUT - 40
HOUR = (X1 - X0) / 7.0
AXIS = chy + 96
p.hline(X0, X1, AXIS, INK, 2)
for h in range(14, 22):
    x = X0 + (h - 14) * HOUR
    p.add(f'<line x1="{x}" y1="{AXIS - 8}" x2="{x}" y2="{AXIS + 8}" stroke="{INK}" stroke-width="2"/>')
    p.text(x, AXIS + 38, f"{h}:00", 20, "serif", False, INK, anchor="middle")
EVENTS = [(14.0, "遊行出發"), (17.0, "星光大道"), (18.5, "頒獎典禮"), (19.0, "夜間遊行"), (20.0, "鋼雕閉館")]
for t, name in EVENTS:
    x = X0 + (t - 14) * HOUR
    p.add(f'<circle cx="{x}" cy="{AXIS}" r="9" fill="{OLIVE}" stroke="{INK}" stroke-width="1.5"/>')
    p.text(x, AXIS - 22, name, 21, "serif", True, INK, anchor="middle")
chart_end = AXIS + 62
p.text(MX, chart_end + 24, "14:00遊行出發 · 17:00星光大道 · 18:30頒獎典禮 · 19:00夜間遊行 · 20:00鋼雕閉館。同一天，四件大事，先選一件。", 21, "serif", False, GREY)
p.text(MX, chart_end + 56, "Linea del tempo: parata 14:00, red carpet 17:00, cerimonia 18:30, parata notturna 19:00, chiusura del festival dell'acciaio 20:00.", 20, "sans", False, GREY)

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 96, 2560, tag="P6-ex")
e.head("看圖答題　Leggi la linea del tempo", 25)
e.ex("B2", "單選", "A", "La parata parte alle 14:00, il segnale più presto.",
     "時間軸上，最早開始的是哪一件大事？", opts=["A. 封王遊行下午2點", "B. 金馬獎頒獎典禮", "C. 夜間遊行"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "Dalle 14:00 alle 19:00 sono 5 ore.",
     "封王遊行下午2點出發，夜間遊行晚上7點，中間隔幾小時？", opts=["A. 3小時", "B. 5小時", "C. 7小時"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "Dalle 17:00 alle 18:30 sono 1,5 ore.",
     "星光大道下午5點，頒獎典禮晚上6點30分，中間隔多久？", opts=["A. 1小時", "B. 2小時", "C. 1小時30分"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "Il festival dell'acciaio chiude alle 20:00, l'ultimo segnale.",
     "時間軸上，最晚的是哪一件？", opts=["A. 鋼雕藝術節晚上8點閉館", "B. 星光大道", "C. 封王遊行"], size=22.5, gap=8)
e.head("深讀測驗　Quiz di lettura", 25)
e.ex("B2", "單選", "B", "Una persona non può vedere tutti e quattro gli eventi in un giorno.",
     "11月22日四件大事，一個人看得完嗎？", opts=["A. 看得完，都在同一個地方", "B. 看不完，要選一件", "C. 看得完，都在早上"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "Guarda la parata dal vivo, la cerimonia sullo schermo.",
     "看遊行和看金馬獎，最好的辦法是什麼？", opts=["A. 遊行去現場，金馬獎看轉播", "B. 兩件都不要看", "C. 只看夜間遊行"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "Xiaoxue è il 22 nov., lo stesso giorno.",
     "小雪在哪天？", opts=["A. 11月16日", "B. 11月17日", "C. 11月22日"], size=22.5, gap=8)
e.ex("B2", "單選", "B", "Il festival dell'acciaio chiude il 22 nov.",
     "鋼雕藝術節展到哪天？", opts=["A. 11月15日", "B. 11月22日", "C. 12月22日"], size=22.5, gap=8)
e.ex("B2", "單選", "A", "L'ultima replica della parata notturna è alle 19:00 il 22 nov.",
     "六福村夜間遊行最終場晚上幾點？", opts=["A. 晚上7點", "B. 下午2點", "C. 晚上9點"], size=22.5, gap=8)
e.ex("B2", "單選", "C", "La cerimonia è al Taipei Music Center.",
     "金馬獎頒獎典禮在哪裡舉行？", opts=["A. 天母棒球場", "B. 駁二蓬萊區", "C. 台北流行音樂中心"], size=22.5, gap=8)
e.head("填一填　Completare", 25)
e.ex("B2", "完成句子", "時間軸", "Leggi la linea del tempo per pianificare la giornata.",
     "先看___，再決定去哪一件。", instr="Completare", size=22.5, gap=8)
e.ex("B2", "完成句子", "轉播", "Guarda la cerimonia sullo schermo.",
     "金馬獎在家看___就好。", instr="Completare", size=22.5, gap=8)
e.ex("B2", "完成句子", "取捨", "Non puoi vedere tutto: scegli.",
     "四件大事同一天，要學會___。", instr="Completare", size=22.5, gap=8)
e.ex("B2", "完成句子", "星光大道", "Il red carpet inizia alle 17:00.",
     "頒獎典禮前，先走___。", instr="Completare", size=22.5, gap=8)
e.ex("B2", "完成句子", "閉館", "Il festival dell'acciaio chiude alle 20:00.",
     "鋼雕藝術節晚上8點___。", instr="Completare", size=22.5, gap=8)
e.ex("B2", "完成句子", "小雪", "Xiaoxue è il 22 nov.",
     "11月22日也是___。", instr="Completare", size=22.5, gap=8)
e.ex("B2", "完成句子", "5", "Dalle 14:00 alle 19:00 sono 5 ore.",
     "遊行下午2點，夜間遊行晚上7點，中間隔___小時。", instr="Completare", size=22.5, gap=8)
e.ex("B2", "完成句子", "4", "Quattro grandi eventi cadono la stessa domenica.",
     "11月22日一共有___件大事。", instr="Completare", size=22.5, gap=8)
e.end_report()

rx = COLX[3]
by = 208
p.rect(rx, by, CW, 760, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "數字一覽　In cifre", 25, "sans", True, OLIVE); yy += 56
for t in [
    "四件大事：遊行、金馬獎、鋼雕閉幕、夜間遊行",
    "時間：14:00、17:00、18:30、",
    "19:00、20:00",
    "金馬報名：587部影片",
    "耶誕城：11月13日到12月27日，一共45天",
    "迪士尼聖誕：11月17日到1月3日，一共48天",
    "爵士音樂節第二週：11月17日到22日，一共6天",
    "小雪：11月22日（日），二十四節氣第20個",
    "雙11包裹：先點收，7天內可退貨",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by2 = by + 760 + 18
p.rect(rx, by2, CW, 504, fill=BOX)
yy = by2 + 18
p.text(rx + 22, yy + 26, "看活動三問　Tre domande", 25, "sans", True, OLIVE); yy += 56
yy = p.para(rx + 22, yy + 24, "第一，時間幾點？第二，地點在哪裡？第三，只能選幾件？三個問題問完，再出門。同一天看不完四件大事，先選一件最想看的，其他的看轉播、留到下次。", 22, "serif", False, INK, CW - 44, 1.36) + 6
p.para(rx + 22, yy + 21, "Tre domande prima di uscire: a che ora? Dove? Quanti ne puoi vedere davvero? Scegli quello che vuoi di più; guarda gli altri sullo schermo.", 19.5, "sans", False, GREY, CW - 44, 1.35)
p.foot(6)
p.save(f"{OUT}/p6-deep.svg")
print("P6 saved, exercises so far:", len(REG))
