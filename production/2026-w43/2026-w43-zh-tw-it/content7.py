# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-it/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Focus sulla lingua", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Tre livelli, tre temi")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 天氣的話 · Parole del meteo", 24)
a.para("La settimana del tifone riempie le notizie di parole del meteo: impara le sei che vedrai di più: 海上颱風警報 (avviso marittimo), 陸上颱風警報 (avviso terrestre), 共伴效應 (effetto congiunto), 外圍環流 (circolazione esterna), 豪雨 (pioggia torrenziale), 停班停課 (lavoro e scuola sospesi).", 21.5)
a.glossline("Sei parole del meteo ricorrono nelle notizie della settimana: imparale una volta e leggi tutta la settimana.")
a.para("Gli avvisi sono di due tipi: prima l'海上警報 (avviso marittimo), mentre il tifone è ancora in mare; poi l'陸上警報 (avviso terrestre), quando si avvicina alla terraferma. Una pioggia più forte di 大雨 è 豪雨 (pioggia torrenziale).", 21.5)
a.ex("A2", "完成句子", "海上", "Prima arriva l'avviso marittimo, mentre il tifone è ancora in mare.",
     "颱風還在海上,先發佈___颱風警報。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Tíng bān tíng kè significa lavoro e scuola sospesi.",
     "「停班停課」是什麼意思?", opts=["A. 不上班、不上課", "B. 提早一小時下班", "C. 換到別天上班"], size=20.5, gap=10)
a.ex("A2", "完成句子", "豪", "Háo yǔ è più forte di dà yǔ.",
     "比大雨還大的雨,叫___雨。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "單選", "A", "La circolazione esterna del tifone (wàiwéi huánliú) porta la pioggia.",
     "颱風的外圍___會帶來雨。", opts=["A. 環流", "B. 警報", "C. 假期"], size=20.5, gap=10)
a.para("Esercitati: «明天會停班停課嗎？» («Domani lavoro e scuola saranno sospesi?») — controlla l'annuncio della tua città.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 日子與節日 · Giorni e feste", 24)
b.para("I giorni di questa settimana sono speciali. Raggruppa le parole e restano in mente: giorni liberi （連假、補假）, viaggi （疏運） e divertimento festivo （登高、討糖、星光大道）.", 21.5)
b.glossline("Raggruppa le parole: riposo (連假/補假), viaggi (疏運), divertimento (登高/討糖/星光大道).")
b.para("連假 è una serie di giorni liberi uno dopo l'altro; quando una festa cade nel fine settimana e in cambio si libera un giorno feriale, quel giorno extra è un 補假； e i treni e gli autobus extra che portano tutti fuori e a casa sono gli 疏運.", 21.5)
b.ex("B1", "完成句子", "補假", "Un giorno di recupero: bǔjià.",
     "假日逢週日,週一多放一天,叫___。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Shūyùn = trasporti extra per gli spostamenti delle feste.",
     "「疏運」是連假時做什麼?", opts=["A. 加開班次載客", "B. 賣紀念票", "C. 修馬路"], size=20.5, gap=10)
b.ex("B1", "完成句子", "討糖", "Tǎotáng è il modo taiwanese di dire «dolcetto o scherzetto».",
     "萬聖節,小朋友去店家___(要糖果)。", instr="Completa", size=20.5, gap=10)
b.ex("B1", "單選", "A", "La parte del tappeto rosso di una serata di premi è la xīngguāng dàdào.",
     "頒獎典禮走紅毯的部分叫?", opts=["A. 星光大道", "B. 人氣獎", "C. 疏運大道"], size=20.5, gap=10)
b.para("Trucco di memoria: impara prima 連假, poi la folla che muove （疏運） e il giorno che aggiunge （補假）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 在地說法 · Modi di dire locali", 24)
c.para("Taiwan e Hong Kong hanno ciascuno il proprio modo di dire le cose. A Taiwan, Threads è soprannominato «脆»; un bel post si salva con «留友看» — «tenerlo da far vedere agli amici»; e un complimento valutato con i simboli zhuyin è un «ㄅ級分».", 21.5)
c.glossline("Tre espressioni di internet taiwanesi — tutte da una rassegna PopDaily di maggio 2026 sui meme dell'anno, non dalle notizie di questa settimana.")
c.para("A Hong Kong, Halloween è «哈囉喂»; l'hot pot è «打邊爐»; economico e gustoso è «抵食»; i granchi si pesano in «両», e i gettoni del festival gastronomico sono le «品味券».", 21.5)
c.ex("B2", "單選", "A", "A Taiwan, Threads è soprannominato cuì (croccante).",
     "台灣人把 Threads 暱稱作什麼?", opts=["A. 脆", "B. 脆餅", "C. 推特兒"], size=20.5, gap=10)
c.ex("B2", "完成句子", "留友", "Liú yǒu kàn — salvalo, così lo leggono anche gli amici.",
     "看到好文,先存起來「___看」。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "單選", "A", "Hāluō wèi è l'Halloween di Hong Kong.",
     "「哈囉喂」是香港人怎麼說哪個節日?", opts=["A. 萬聖節", "B. 聖誕節", "C. 重陽節"], size=20.5, gap=10)
c.ex("B2", "完成句子", "品味", "I coupon del festival sono le pǐnwèi quàn (biglietti di degustazione).",
     "美酒佳餚巡禮換飲品小食的券,叫___券。", instr="Completa", size=20.5, gap=10)
c.para("Non servono molte espressioni locali: imparane cinque e ogni conversazione sembrerà più vicina.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「台風來了」", "→「颱風來了」", "Taiwan scrive 颱風; 台風 è la grafia kanji giapponese."),
    ("「我買了四兩的蟹」", "→「我買了四両的蟹」", "I granchi si pesano in 両 (tael); 兩 è il «due» di tutti i giorni, come in 兩隻蟹 (due granchi)."),
    ("「天氣慢慢的變涼」", "→「天氣慢慢地變涼」", "地 (de) indica come avviene un'azione, prima del verbo."),
    ("「我明天放四天假去玩」", "→「我請了四天假去玩」", "請假 = chiedere ferie di persona; 放假 = la vacanza è data a tutti."),
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
wt = "«先看警報，再決定出不出門。» — la struttura 先…再… dà l'ordine di due azioni: prima X, poi Y. È fatta per la settimana del tifone: 先查公告，再改行程 (prima controlla gli avvisi, poi cambia i programmi)."
wcn = "Struttura: 先…再… — prima X, poi Y. Prova a scrivere una frase tua."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Struttura settimanale", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:重陽節我跟阿公去登高,他走得比我還快!晚上我們吃大閘蟹,蟹黃真的好多。下週我想去看台灣大賽。——台北小讀者(編輯範例)」"
lcn = "Una lettera di esempio della redazione — non una vera. Il VOL.2 pubblicherà lettere vere dei lettori e la migliore scrittura di pagina 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · L'angolo dei lettori", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Frasi della settimana — parola per parola dagli articoli di questo numero", 27, "sans", True, OLIVE)
quotes = [
    ("「路徑還有變數,會不會登陸,還沒有人知道」", "La traiettoria può ancora cambiare; nessuno sa ancora se toccherà terra.", "p. 1"),
    ("「請四天假,換九天連假」", "Quattro giorni di ferie, nove giorni liberi.", "p. 2"),
    ("「登高望遠,人也精神了」", "Sali in alto, guarda lontano — e sentiti rinnovato.", "p. 3"),
    ("「農曆九月吃蟹乸,農曆十月吃蟹公」", "Femmine nel nono mese lunare, maschi nel decimo.", "p. 3"),
    ("「先贏四場的隊伍,就是今年的總冠軍」", "La prima squadra a quattro vittorie è la campionessa di quest'anno.", "p. 4"),
    ("「颱風改了日期,卻改不了大家過節的心情」", "Il tifone ha cambiato la data, non l'umore festivo.", "p. 5"),
    ("「三百四十多個攤位,把世界搬到海邊」", "Più di 340 stand portano il mondo sul porto.", "p. 6"),
    ("「星期五、六的晚上,今年第一次開到凌晨一時」", "Le sere di venerdì e sabato arrivano fino all'1 per la prima volta.", "p. 6"),
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
p.text(MX + 28, py + 44, "下期預告 · La prossima settimana (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "台灣大賽冠軍出爐!美酒佳餚巡禮開幕直擊,天母搞什麼鬼主活動、福隆沙雕最後一天,還有你們的來信和第 8 版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
