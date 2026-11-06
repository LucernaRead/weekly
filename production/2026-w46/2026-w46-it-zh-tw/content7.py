# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA · 語言", "La Lucerna", "聚焦語言 · Tre livelli, tre strumenti · 三個級別，三件工具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · IL FUTURO", 24)
a.para("Per i piani della settimana usiamo il futuro semplice: andremo a Cuneo, assaggeremo il vino nuovo, guarderemo Italia–Francia. Le forme sono regolari: andare → andrò, assaggiare → assaggerò, guardare → guarderò.", 21.5)
a.para("E per il tempo: ci sarà il sole di San Martino, durerà tre giorni. Il verbo è durare, regolare.", 21.5)
a.bridge("用將來時說計畫：andremo、assaggeremo、guarderemo。")
a.ex("A2", "完成句子", "andremo", "andare 將來時 noi：andremo",
     "Mercoledì noi ___ (andare) a Cuneo.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "assaggeremo", "assaggiare 將來時 noi：assaggeremo",
     "Noi ___ (assaggiare) il vino nuovo.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "guarderemo", "guardare 將來時 noi：guarderemo",
     "Giovedì noi ___ (guardare) Italia–Francia.", instr="填空", size=20.5, gap=10)
a.ex("A2", "單選", "B", "durerà 是 durare 的將來時",
     "L'estate di San Martino... A. dura tre giorni · B. durerà tre giorni · C. durava tre giorni", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il weekend usiamo il passato prossimo: ausiliare + participio. Con essere — per verbi come arrivare e andare — il participio cambia con la persona: è arrivato (il treno), sono andati (i visitatori).", 21.5)
b.para("Con avere: abbiamo assaggiato, ha aperto. Il participio con avere non cambia.", 21.5)
b.bridge("講過去用近過去時：arrivare/andare 等用 essere，分詞配合性數；avere 的分詞不變。")
b.ex("B1", "完成句子", "è arrivato", "arrivare 用 essere：è arrivato",
     "Il Treno Storico ___ (arrivare) a Cremona.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "abbiamo assaggiato", "assaggiare 用 avere",
     "Noi ___ (assaggiare) il torrone a Cremona.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "sono andati", "andare 用 essere，複數 sono andati",
     "I visitatori ___ (andare) a Perugia.", instr="填空", size=20.5, gap=10)
b.ex("B1", "單選", "B", "aprire 用 avere + 不變分詞",
     "Perugia ___ Eurochocolate. A. è aperta · B. ha aperto · C. sono aperti", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · IL CONGIUNTIVO", 24)
c.para("Con «è probabile che», «è possibile che» e «bisogna che» usiamo il congiuntivo: piova (piovere), nevichi (nevicare), sia (essere). È la grammatica della probabilità, la stessa di pagina 6.", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il sole torna, la Festa del Torrone è a Cremona. Opinioni sì, fatti con l'indicativo.", 21.5)
c.bridge("è probabile che / è possibile che / bisogna che 後用虛擬式；so che、scrivono che 後用陳述式。")
c.ex("B2", "完成句子", "piova", "è probabile che + 虛擬式 piova",
     "È probabile che domani ___ (piovere) in pianura.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "nevichi", "è possibile che + 虛擬式 nevichi",
     "È possibile che in montagna ___ (nevicare) nel weekend.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "sia", "bisogna che + 虛擬式 sia",
     "Bisogna che la cifra ___ (essere) chiara per tutti.", instr="填空", size=20.5, gap=10)
c.ex("B2", "單選", "B", "so che + 陳述式 torna",
     "«So che il sole...» A. torni · B. torna · C. tornare", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Fa freddi.»", "→ «Fa freddo.» Dopo fa, freddo non cambia mai: è invariabile.", "fa 後面的 freddo 永遠不變"),
    ("«È probabile che piove.»", "→ «È probabile che piova.» Dopo è probabile che serve il congiuntivo.", "è probabile che 後用虛擬式"),
    ("«Ieri ho andato a Cremona.»", "→ «Ieri sono andato a Cremona.» Andare vuole essere, non avere.", "andare 用 essere 作助動詞"),
    ("«Il mosto diventano vino.»", "→ «Il mosto diventa vino.» Mosto è singolare, il verbo è singolare.", "mosto 是單數，動詞用單數"),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI · 常見錯誤", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« il mosto » è il succo d'uva prima che diventi vino. Questa settimana vive a pagina 2, a San Martino."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("mosto = 葡萄汁／新酒。本週見第 2 版：聖馬丁節葡萄汁變新酒。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA · 本週生詞", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "mosto = 葡萄汁／新酒。本週見第 2 版：聖馬丁節葡萄汁變新酒。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Questa settimana la redazione assaggia il vino nuovo e le castagne, e guarda Italia–Francia in televisione. E voi? Scriveteci!» — esempio della redazione"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("這是編輯部示例，非真實來信。截稿時未收到真實來信與第 8 版最佳作文，承諾順延 VOL.4，請寄信給編輯部。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "這是編輯部示例，非真實來信。截稿時未收到真實來信與第 8 版最佳作文，承諾順延 VOL.4，請寄信給編輯部。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA · 本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)
quotes = [
    ("«tre giorni di sole dopo il primo freddo»", "初寒之後三天晴。", "Pagina 1"),
    ("«il sole tornò a splendere»", "太陽重新照耀。", "Pagina 1"),
    ("«Il cinema che sceglie da che parte stare»", "選擇立場的電影。", "Pagina 2"),
    ("«Due notti azzurre, alle 20.45»", "兩個藍色之夜，20 點 45 分。", "Pagina 1"),
    ("«arriva anche il Treno Storico Arlecchino»", "歷史列車阿萊基諾也來了。", "Pagina 3"),
    ("«le due partite di questa settimana sono decisive»", "本週兩場比賽至關重要。", "Pagina 4"),
    ("«un libro in mano, un film negli occhi»", "手裡一本書，眼裡一部電影。", "Pagina 5"),
    ("«approvato dal governo non vuol dire già legge»", "政府批准不等於已經是法律。", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- prossima settimana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA · 下期預告 (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "Domenica 22 novembre: chiude la Festa del Torrone a Cremona. La Serie A torna il 21–23 novembre, con i risultati dell'11ª giornata. E poi: le vostre lettere vere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
