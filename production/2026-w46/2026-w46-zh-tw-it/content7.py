# -*- coding: utf-8 -*-
# W46 zh-tw core, VOL.3: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-tw-it/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Focus lingua", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Tre livelli, tre temi")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 雙11的話 · Parole del 11.11", 24)
a.para("Il Double 11 ti dà quattro parole utili: 清單 (lista della spesa), 實付金額 (l'importo finale che paghi), 領券 (richiedere coupon) e 鑑賞期 (il periodo di ripensamento). Imparale una volta e ogni saldo avrà senso.", 21.5)
a.glossline("Quattro parole del Double 11: 清單, 實付金額, 領券, 鑑賞期.")
a.para("清單 è la lista che scrivi prima di comprare. 實付金額 è ciò che paghi davvero dopo gli sconti. 領券 significa richiedere un coupon prima che finisca. 鑑賞期 sono i 7 giorni dopo la consegna in cui puoi restituire quasi tutto.", 21.5)
a.ex("A2", "完成句子", "清單", "Una lista della spesa è qīngdān.",
     "買東西之前,先列___。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Il periodo di ripensamento è di 7 giorni.",
     "鑑賞期是幾天?", opts=["A. 7天", "B. 3天", "C. 14天"], size=20.5, gap=10)
a.ex("A2", "完成句子", "實付金額", "Confronta l'importo finale che paghi davvero.",
     "比價要比___。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Richiedi i coupon prima che finiscano.",
     "優惠券要怎麼拿?", opts=["A. 先領,領完就沒有了", "B. 不用領", "C. 過期再領"], size=20.5, gap=10)
a.para("Esercitati: 「我的購物清單是什麼？」 («Che cosa c'è nella mia lista della spesa?») — scrivila prima, poi confronta i prezzi.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 影展與鋼雕 · Film e acciaio", 24)
b.para("Film e acciaio condividono i titoli della settimana. Raggruppa le parole e restano: film （入圍、頒獎、星光大道） e acciaio （鋼雕、保險箱、勞動記憶）.", 21.5)
b.glossline("Raggruppa le parole: film (入圍/頒獎), acciaio (鋼雕/保險箱).")
b.para("入圍 significa essere nominato; 頒獎 significa consegnare i premi. 星光大道 è il tappeto rosso prima della cerimonia. 鋼雕 è una scultura d'acciaio; 保險箱 è la cassaforte che custodisce i ricordi del lavoro di Kaohsiung.", 21.5)
b.ex("B1", "完成句子", "入圍", "Essere nominato è rùwéi.",
     "被選進最後的得獎名單,叫___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "La cerimonia inizia alle 18:30 il 22 nov.",
     "金馬獎頒獎典禮幾點開始?", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=20.5, gap=10)
b.ex("B1", "完成句子", "鋼雕", "Una scultura d'acciaio è gāngdiāo.",
     "用鋼鐵做的藝術,叫___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Il festival dell'acciaio chiude il 22 nov.",
     "鋼雕藝術節展到哪天?", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=20.5, gap=10)
b.para("Trucco: impara prima 入圍 — poi la cerimonia （頒獎）, poi il luogo dove avviene （星光大道）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Modi di dire locali", 24)
c.para("Taiwan e Hong Kong hanno ciascuno il proprio modo di dire le cose. Questa settimana: 打卡 (fare check-in con una foto), 集點 (raccogliere punti), 遊行 (parata in strada) e 感謝祭 (festival di ringraziamento per i tifosi).", 21.5)
c.glossline("Quattro parole locali di questo numero: 打卡, 集點, 遊行, 感謝祭.")
c.para("打卡 a una fiera significa pubblicare una foto per dire «ero qui». 集點 è guadagnare punti ogni volta che fai sport. 遊行 è la marcia di festa per le strade; 感謝祭 è il festival di ringraziamento della squadra per i suoi tifosi.", 21.5)
c.ex("B2", "單選", "A", "Jídiǎn significa raccogliere punti quando fai sport.",
     "「集點」是什麼意思?", opts=["A. 每次運動累積點數", "B. 買門票", "C. 上班簽到"], size=20.5, gap=10)
c.ex("B2", "完成句子", "遊行", "Una marcia di festa è yóuxíng.",
     "大家走上街頭慶祝,叫___。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "單選", "A", "Gǎnxièjì ringrazia i tifosi.",
     "「感謝祭」是謝謝誰的活動?", opts=["A. 球迷", "B. 店員", "C. 記者"], size=20.5, gap=10)
c.ex("B2", "完成句子", "打卡", "Fare check-in con una foto è dǎkǎ.",
     "在嘉年華拍照分享,叫___。", instr="Completa", size=20.5, gap=10)
c.para("Non servono molti modi di dire locali: imparane quattro e ogni uscita sembrerà più vicina.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「旅展在11月9日開幕」", "→「旅展在11月9日落幕,開幕是11月6日」", "Fiera aperta il 6 nov., chiusa il 9 nov. Controlla il senso del tempo."),
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎,11月15日是嘉年華」", "Cerimonia: 22 nov.; carnevale: 15 nov. (2º giorno)."),
    ("「滿5,000折800,實付5,800元」", "→「滿5,000折800,實付4,200元」", "Gli sconti si sottraggono: 5.000 − 800 = 4.200."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Clinica degli errori", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「雙11不但有折扣,而且有免運。」 — La struttura 不但…而且… significa: non solo X, ma anche Y. Crea la tua: 旅展不但有攤位,而且有表演 (non solo stand, ma anche spettacoli)."
wcn = "Struttura: 不但…而且… — non solo X, ma anche Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Struttura della settimana", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:雙11我的包裹到了!我買了一本書和一件外套,都沒有超過預算。週末我想去銅鑼灣看夜光巡遊,還想去高雄看鋼雕。——台北小讀者(編輯範例)」"
lcn = "Lettera di esempio della redazione, non una lettera vera. VOL.2 prometteva lettere vere e i migliori testi di pagina 8 da questo numero; nessuna pubblicabile era arrivata alla chiusura. L'esempio resta, e resta anche l'invito."
lt2 = "延期披露:VOL.2曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 40
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · L'angolo dei lettori", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Frasi della settimana — parola per parola dagli articoli di questo numero", 27, "sans", True, OLIVE)
quotes = [
    ("「先列清單,再比價,最後才結帳」", "Prima la lista, poi i prezzi, poi pagare.", "p. 1"),
    ("「旅展四天,一次看完123個國家及城市」", "Quattro giorni di fiera, 123 paesi e città in una visita.", "p. 1"),
    ("「早晚溫差大,外套要隨身帶」", "Grandi sbalzi giorno-notte: tieni una giacca con te.", "p. 2"),
    ("「金馬影展,就是一年一度的大電影課」", "Il festival Golden Horse è una grande lezione di cinema all'anno.", "p. 3"),
    ("「保險箱裡,裝的是高雄的勞動記憶」", "Dentro la cassaforte: i ricordi del lavoro di Kaohsiung.", "p. 3"),
    ("「穿上紅色衣服,一起上街為龍隊喝采」", "Vesti di rosso, scendi in strada, tifa per i Dragons.", "p. 4"),
    ("「嘉年華不用門票,全家人都能來玩」", "Nessun biglietto: tutta la famiglia può venire a giocare.", "p. 5"),
    ("「回饋不是折價,實付金額才是真的」", "Il cashback non è uno sconto: conta l'importo pagato.", "p. 6"),
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
p.text(MX + 28, py + 44, "下期預告 · La prossima settimana (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週日11月22日,三件大事同一天:封王遊行下午2點、金馬獎晚上6點30分、鋼雕藝術節閉幕,還有小雪、你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
