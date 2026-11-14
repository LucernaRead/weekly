# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LINGUA (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LINGUA　語言", "La Lucerna", "聚焦語言　Tre livelli, tre strumenti　三個級別，三件工具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　DIRE L'ORA E IL PRESENTE", 24)
a.para("Per dire l'ora: «È l'una», ma «Sono le due, le tre…». «E mezza» è +30 minuti (2:30); «meno un quarto», −15 (2:45).", 21.5)
a.para("E dormire è regolare: dormo, dormi, dorme, dormiamo. Svegliarsi è riflessivo: mi sveglio, si sveglia.", 21.5)
a.expl("報時只有「一點」用 è；dormire 是規則變位；svegliarsi 是反身動詞。")
a.ex("A2", "完成句子", "Sono", "十點用 Sono（只有 l'una 用 È）",
     "___ le dieci di sera. Comincia il film.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "dorme", "dormire：lui → dorme",
     "Mio fratello ___ (dormire) fino alle undici domenica.", instr="填空", size=20.5, gap=10)
a.ex("A2", "完成句子", "si sveglia", "svegliarsi：lei → si sveglia",
     "Lei ___ (svegliarsi) alle otto.", instr="填空", size=20.5, gap=10)
a.ex("A2", "單選", "B", "e mezza = 30 分鐘",
     "«Sono le due e mezza» sono le... A. 2:15 · B. 2:30 · C. 2:45", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　IL PASSATO PROSSIMO", 24)
b.para("Per raccontare il weekend usiamo il passato prossimo: ausiliare + participio. Con avere: ho visitato, abbiamo guardato.", 21.5)
b.para("Con essere — per verbi di movimento come andare e arrivare — il participio cambia con la persona: sono andato / sono andata, è iniziata (la fiera).", 21.5)
b.expl("講週末用近過去時：avere + 分詞；andare/arrivare 等移動動詞用 essere，分詞要配合性數。")
b.ex("B1", "完成句子", "è iniziata", "iniziare 用 essere，陰性 è iniziata",
     "La fiera ___ (iniziare) il 10 ottobre.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "abbiamo visitato", "visitare 用 avere",
     "Noi ___ (visitare) la mostra mercoledì.", instr="填空", size=20.5, gap=10)
b.ex("B1", "完成句子", "è andato", "andare 用 essere：è andato",
     "Marco ___ (andare) alla sagra con gli amici.", instr="填空", size=20.5, gap=10)
b.ex("B1", "單選", "B", "arrivare 用 essere + 複數配合",
     "I tifosi ___ allo stadio. A. hanno arrivato · B. sono arrivati · C. è arrivati", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　IL CONGIUNTIVO", 24)
c.para("Con «è possibile che», «bisogna che» e «è importante che» usiamo il congiuntivo: slitti (slittare), sia (essere), abbia (avere).", 21.5)
c.para("Ma dopo «so che» e «i giornali scrivono che» resta l'indicativo: il Consiglio si riunisce, la Festa chiude. È la grammatica della pagina 6: opinioni sì, fatti con l'indicativo.", 21.5)
c.expl("è possibile che / bisogna che / è importante che 後用虛擬式；so che、scrivono che 後用陳述式。")
c.ex("B2", "完成句子", "slitti", "è possibile che + 虛擬式 slitti",
     "È possibile che il voto ___ (slittare) ancora.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "abbia", "bisogna che + 虛擬式 abbia",
     "Bisogna che ogni cifra ___ (avere) una fonte.", instr="填空", size=20.5, gap=10)
c.ex("B2", "完成句子", "chiude", "so che + 陳述式 chiude",
     "So che la Festa ___ (chiudere) domenica.", instr="填空", size=20.5, gap=10)
c.ex("B2", "單選", "B", "è importante che + 虛擬式 sia",
     "«È importante che il grafico...» A. è chiaro · B. sia chiaro · C. essere chiaro", size=20.5, gap=10)
c.end_report()

# ---- col 3: errori tipici + parola + lettori ----
bx = COLX[3]
errs = [
    ("«Sono le una.»", "→ «È l'una.» Solo l'ora 1:00 usa è; le altre ore usano sono.", "只有 1 點用 è，其餘鐘點用 sono。"),
    ("«Ho andato a Lucca.»", "→ «Sono andato a Lucca.» Andare vuole l'ausiliare essere, non avere.", "andare 的助動詞是 essere，不是 avere。"),
    ("«Vado a il cinema.»", "→ «Vado al cinema.» A + il si uniscono: al. Anche: del, nel, sul, dal.", "a+il 合成 al；同理 del、nel、sul、dal。"),
    ("«La gente sono contenti.»", "→ «La gente è contenta.» Gente è singolare, come un solo gruppo.", "gente 是單數，動詞形容詞用單數陰性。"),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 194
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "ERRORI TIPICI　常見錯誤", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 26
wt = "« l'anteprima » è la prima volta che il pubblico vede un film. Questa settimana la parola vive a pagina 5: alla Festa del Cinema, molte proiezioni sono anteprime."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("anteprima = 首映。本週見第 5 版：電影節上許多場次都是首映。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "LA PAROLA　本週生詞", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "anteprima = 首映。本週見第 5 版：電影節上許多場次都是首映。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 26
lt = "«Ciao! Sono Li e studio italiano a Pechino. Domenica dormo un'ora in più e poi guardo Inter–Fiorentina. Grazie per il giornale!» — Li (lettera di esempio, scritta dalla redazione)"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("這是示例信，不是真實讀者來信。VOL.2 將刊登真實來信——寫信來吧！", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "LETTERE DEI LETTORI", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "這是示例信，不是真實讀者來信。VOL.2 將刊登真實來信——寫信來吧！", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- frasi della settimana (verbatim from this issue) ----
fy = 1700
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "FRASI DELLA SETTIMANA　本週金句（逐字摘自本期文章）", 27, "sans", True, OLIVE)
quotes = [
    ("«alle 03:00 l'orologio torna indietro di un'ora»", "03:00，時鐘往回撥一小時。", "Pagina 1"),
    ("«È la ricerca numero uno in Italia»", "這是義大利搜尋量第一的詞。", "Pagina 1"),
    ("«L'ora tra le 02:00 e le 03:00 arriva due volte nella stessa notte.»", "02:00 到 03:00 這一小時，在同一夜裡出現兩次。", "Pagina 2"),
    ("«In primavera avanti, in autunno indietro.»", "春天往前撥，秋天往回撥。", "Pagina 2"),
    ("«Il re della stagione è il tartufo bianco»", "這個季節的王是白松露。", "Pagina 3"),
    ("«È una partita speciale: è la prima della domenica con l'ora solare.»", "這場比賽很特別：它是週日第一場冬令時間比賽。", "Pagina 4"),
    ("«Molte sono anteprime: film che il pubblico vede per la prima volta.»", "許多是首映：觀眾第一次看到的電影。", "Pagina 5"),
    ("«Un voto previsto non è un voto fatto»", "「預定」的表決不等於已經表決。", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 158
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- prossima settimana ----
py = 2404
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "LA PROSSIMA SETTIMANA　下期預告 (VOL.2)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Mercoledì 28 ottobre: il voto sulla manovra a Roma. Dal 28 ottobre al 1° novembre: Lucca Comics & Games, la 60ª edizione. Domenica 1° novembre: Ognissanti — quest'anno cade di domenica, niente ponte. E poi: le vostre lettere e i testi migliori della pagina 8. A lunedì!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-lingua.svg")
print("P7 saved, exercises so far:", len(REG))
