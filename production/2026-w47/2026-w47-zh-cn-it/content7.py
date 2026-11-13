# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语　Focus linguistico", "Lucerna", "语言聚焦　三个级别，三个主题　Tre livelli, tre temi")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　决赛与包裹　Finale e pacchi", 24)
a.para("Parole della settimana: 决赛 (juésài, la finale), 冠军 (guànjūn, il campione), 半决赛 (bànjuésài, la semifinale), 到货 (dàohuò, arrivato), 退换货 (tuìhuànhuò, resi e cambi), 价保 (jiàbǎo, protezione del prezzo).", 21.5)
a.glossline("I classificatori contano ancora: 一个包裹 (un pacco), 一部电影 (un film), 一场演练 (un'esercitazione).")
a.ex("A2", "完成句子", "个", "包裹 prende il classificatore 个 gè.",
     "我拿了___包裹。", instr="Completa", size=20, gap=10)
a.ex("A2", "单选", "A", "决赛 vuol dire la finale, l'ultima partita.",
     "「决赛」是什么意思？ A. 最后一场比赛 · B. 第一场比赛 · C. 练习赛", size=20, gap=10)
a.ex("A2", "完成句子", "决赛", "juésài — la finale; BLG contro GEN il 15 nov.",
     "11月15日凌晨3点，BLG和GEN打___。", instr="Completa", size=20, gap=10)
a.ex("A2", "单选", "A", "I pacchi prendono 个 — non 只 o 条.",
     "哪个说法对？ A. 一个包裹 · B. 一只包裹 · C. 一条包裹", size=20, gap=10)
a.para("Ancora uno da esercitare: 「我的包裹到了吗？」 (Il mio pacco è arrivato?) Quando aspetti un pacco, chiedi prima e poi vai all'armadietto.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　时间与日期　Ora e date", 24)
b.para("Il cinese mette i tempi dal grande al piccolo: anno, mese, giorno, giorno della settimana, momento del giorno, ora. Esempi da questo numero: 「11月15日星期日凌晨3点」 (dom. 15 nov., ore 3 di notte), 「11月22日星期日」 (dom. 22 nov.), 「11月21日星期六」 (sab. 21 nov.). L'unità più grande prima, niente fuori ordine.", 21.5)
b.glossline("Così l'inglese «Sunday, Nov 22» diventa 11月22日星期日.")
b.ex("B1", "单选", "B", "凌晨 língchén — le piccole ore dopo mezzanotte.",
     "「凌晨3点」是什么时候？ A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20, gap=10)
b.ex("B1", "完成句子", "早上", "Le 06:00 sono 早上 — non sera.",
     "半决赛在北京时间11月8日___6点开始。（不是晚上）", instr="Completa", size=20, gap=10)
b.ex("B1", "单选", "A", "Ordine dal grande al piccolo: 22 nov., domenica.",
     "哪个顺序对？ A. 11月22日星期日 · B. 星期日11月22日 · C. 星期日小雪11月22日", size=20, gap=10)
b.ex("B1", "完成句子", "周日", "Il 22 nov. è domenica — 周日.",
     "11月22日是星期日，也可以说___。小雪在这天。", instr="Completa", size=20, gap=10)
b.para("Altre due parole: 凌晨 (língchén) sono le piccole ore dopo mezzanotte, prima dell'alba; 傍晚 (bàngwǎn) è il breve tratto appena prima del buio.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　读新闻　Leggere le notizie", 24)
c.para("Quando una storia contiene un'affermazione (说法), separa tre tipi di frasi: affermazioni (说法), dati (数据) e previsioni (预报). Pagina 6 è l'esempio: 「没有爆掉」 è un'affermazione sui pacchi di quest'anno, il totale 139.38亿件 sono dati riportati — già contati, non un'ipotesi — e 「第三波是最高峰」 è una previsione di 中通云仓: attesa, non ancora contata.", 21.5)
c.glossline("Chiedi per ogni numero: di chi è e quando è stato misurato?")
c.ex("B2", "单选", "A", "「139.38亿件」: conteggio finale delle Poste, già contato.",
     "「139.38亿件」在第6版里是什么？ A. 已经数完的事实 · B. 邮政局的预计 · C. 广告词", size=20, gap=10)
c.ex("B2", "完成句子", "数据", "shùjù — numeri misurati, non affermazioni.",
     "买东西以前，先看___，再看广告。", instr="Completa", size=20, gap=10)
c.ex("B2", "单选", "B", "Dati e pagina di pagamento prima, titolo per ultimo.",
     "读新闻时，哪个做法最好？ A. 只看标题 · B. 先看数据和结算页 · C. 只看评论", size=20, gap=10)
c.ex("B2", "完成句子", "预报", "yùbào — una previsione, non ancora un fatto.",
     "「第三波是最高峰」是___，还没发生。", instr="Completa", size=20, gap=10)
c.para("Prova tu stesso: nel riquadro del calendario a pagina 1, 「11月22日」 è una data — un dato. Le parole in una pubblicità sono affermazioni. Sai distinguerle?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters + image ----
bx = COLX[3]
errs = [
    ("「他开心的去拿包裹」", "→ 「他开心地去拿包裹。」", "地 (de) indica come si fa un'azione."),
    ("「包裹来的很快」", "→ 「包裹来得很快。」", "得 (de) collega verbo + grado: 来得快."),
    ("「我拿了两个包裹个」", "→ 「我拿了两个包裹。」", "Ordine: numero + classificatore + nome."),
    ("「总决赛在星期日11月15日凌晨3点」", "→ 「总决赛在11月15日，星期日凌晨3点。」", "Gli orari vanno dal grande al piccolo: il giorno della settimana per ultimo."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所　Clinica degli errori", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先看预报，再决定穿什么。」La struttura 先…再… dà l'ordine delle azioni."
wcn = "Struttura: 先 … 再 … — prima X, poi Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill=BOX)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式　Struttura di frase", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好！我住在上海。11月9日半决赛，我看了BLG打T1，3比1，真好看！双11我买了一件外套，包裹两天就到了。你们呢？」"
lcn = "编辑部示例信，不是真实来信。VOL.3曾预告本期刊登真实来信和最佳作文；截至11月10日截稿，仍未收到，继续征集。延期不是取消。Nota della redazione: VOL.3 aveva promesso lettere vere in VOL.4; nessuna è arrivata entro il 10 nov. Rimandato, non cancellato."
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地　Angolo dei lettori", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- P7 image (brush) below the letters box ----
iy7 = col3_end + 12
image(p, "brush.jpg", bx, iy7, CW, 130)
cy7 = caption(p, bx, iy7 + 130, CW, "毛笔（资料图）。写中文，先从一笔一画开始。",
              "Foto: Mx. Granger — CC0 (Wikimedia Commons)")
img_end = cy7
print("P7 image ends", img_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, img_end + 44)
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "本周金句　Frasi della settimana (alla lettera, dagli articoli di questo numero)", 27, "sans", True, OLIVE)
quotes = [
    ("「决赛对阵GEN」", "La finale: BLG contro GEN.", "Pagina 1"),
    ("「包裹都到了吗」", "Sono arrivati tutti i pacchi?", "Pagina 2"),
    ("「小雪气寒而将雪矣」", "Piccola Neve: l'aria si fa fredda, arriva la neve.", "Pagina 3"),
    ("「两支中国队进了四强」", "Due squadre cinesi sono arrivate in semifinale.", "Pagina 4"),
    ("「先看简介，再决定」", "Leggi prima la trama, poi decidi.", "Pagina 5"),
    ("「无高峰，全高峰」", "Nessun picco unico — ogni giorno è un picco.", "Pagina 6"),
    ("「先打开看一看，再确认收货」", "Apri e controlla prima, poi conferma la ricezione.", "Pagina 6"),
    ("「悦读深圳」", "Leggere con gioia a Shenzhen — il tema del Mese della Lettura di Shenzhen.", "Pagina 3"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 120
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 120 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "下期预告　La prossima settimana (VOL.5)", 24, "sans", True, GOOSE)
p.para(MX + 28, py + 84, "S16总决赛打完了，谁是冠军？小雪之后，冬天怎么过？还有你们的来信和第8版最佳作文。下周见！", 21, "serif", False, ONCLOTH, RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
