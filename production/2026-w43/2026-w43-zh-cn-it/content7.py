# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · 词语精讲 =================
CURPAGE[0] = 7
p = BSPage4()
p.band("词语 · Focus sulla lingua", "Lucerna", "语言聚焦 · 三个级别,三个主题 · Tre livelli, tre temi")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 购物与量词 · I classificatori", 24)
a.para("Quando fai acquisti, il cinese usa i classificatori (量词): 一件外套 (un cappotto), 一条围巾 (una sciarpa), 一斤蟹 (mezzo chilo di granchi), 一只蟹 (un granchio). Lo schema è: numero + classificatore + nome (数词 + 量词 + 名词).", 21.5)
a.glossline("L'italiano conta le cose in modo libero; il cinese sceglie un classificatore per ogni tipo di cosa — niente plurale.")
a.ex("A2", "Completa la frase", "件", "wàitào prende il classificatore jiàn.",
     "我想买一___外套。", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Scelta multipla", "B", "wéijīn prende tiáo: cose lunghe e morbide.",
     "「一条」可以说什么? A. 一条外套 · B. 一条围巾 · C. 一条大闸蟹", size=20.5, gap=10)
a.ex("A2", "Completa la frase", "斤", "jīn — mezzo chilo; i prezzi del mercato sono al jīn.",
     "大闸蟹多少钱一___?", instr="Completa", size=20.5, gap=10)
a.ex("A2", "Scelta multipla", "A", "Per i vestiti si usa jiàn, non gè né tiáo.",
     "哪个说法对? A. 一件衣服 · B. 一个衣服 · C. 一条衣服", size=20.5, gap=10)
a.para("Un altro esempio per esercitarti: 「这件外套多少钱?」 (Quanto costa questo cappotto?) Quando fai acquisti, chiedi prima il prezzo, poi paga.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 时间与日期 · Ora e date", 24)
b.para("Il cinese dà gli orari dal grande al piccolo: anno, mese, giorno, giorno della settimana, parte del giorno, ora. Esempio: 「10月20日晚上8点」 (20 ottobre, ore 20) — prima l'unità più grande, niente fuori ordine.", 21.5)
b.glossline("Così «venerdì sera, 23 ottobre» diventa 10月23日星期五晚上.")
b.ex("B1", "Scelta multipla", "B", "língchén — le ore piccole dopo mezzanotte.",
     "「凌晨3点」是什么时候? A. 下午3点 · B. 半夜3点 · C. 中午12点", size=20.5, gap=10)
b.ex("B1", "Completa la frase", "上午", "La NBA è iniziata di mattina, ora di Pechino.",
     "NBA 在北京时间10月21日___开打。(不是晚上)", instr="Completa", size=20.5, gap=10)
b.ex("B1", "Scelta multipla", "A", "Ordine dal grande al piccolo: 20 ottobre, sera, ore 8.",
     "哪个顺序对? A. 10月20日晚上8点 · B. 8点晚上10月20日 · C. 晚上8点10月20日", size=20.5, gap=10)
b.ex("B1", "Completa la frase", "周五", "Il 23 ottobre è venerdì — zhōuwǔ.",
     "10月23日是星期五,也可以说___。霜降在这天。", instr="Completa", size=20.5, gap=10)
b.para("Due parole in più: 凌晨 (língchén) sono le ore piccole dopo mezzanotte, prima dell'alba; 傍晚 (bàngwǎn) è il breve tratto appena prima del buio.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 读新闻 · Leggere le notizie", 24)
c.para("Quando una notizia riguarda una disputa (争议), distingui tre tipi di frase: le affermazioni online (说法), le dichiarazioni ufficiali (声明) e i dati di mercato (数据). Le affermazioni possono esagerare; i dati devono conservare fonte e data. La pagina 6 è l'esempio: 「暴跌40%」 è un'affermazione, 77,5 元 e 57,5 元 sono dati, 「崩盘不实」 è una dichiarazione.", 21.5)
c.glossline("Chiediti di ogni numero: chi l'ha misurato, e quando?") 
c.ex("B2", "Scelta multipla", "C", "«bàodiē 40%» era un'affermazione online, non un dato misurato.",
     "「暴跌超过40%」在第6版里是什么? A. 数据 · B. 声明 · C. 网上的说法", size=20.5, gap=10)
c.ex("B2", "Completa la frase", "声明", "shēngmíng — la dichiarazione ufficiale dell'associazione.",
     "协会10月19日发表___,说「崩盘」不是真的。", instr="Completa", size=20.5, gap=10)
c.ex("B2", "Scelta multipla", "B", "Prima i dati e la fonte; il titolo per ultimo.",
     "读新闻时,哪个做法最好? A. 只看标题 · B. 先看数据和出处 · C. 只看评论", size=20.5, gap=10)
c.ex("B2", "Completa la frase", "25.8", "Il calo reale, calcolato a pagina 6, è del 25,8%.",
     "第6版真正算出的数据降幅是___%。", instr="Completa", size=20.5, gap=10)
c.para("Prova tu: nel riquadro delle ricerche di pagina 1, 「第 8 位」 è una posizione in classifica — un dato. Le parole di un titolo sono affermazioni. Sai distinguerle?", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「他高兴的跳起来」", "→ 「他高兴地跳起来。」", "地 (de) indica come si compie un'azione; va prima del verbo."),
    ("「他跑的很快」", "→ 「他跑得很快。」", "得 (de) lega un verbo a un complemento di grado: 跑得快."),
    ("「我买了三只大闸蟹个」", "→ 「我买了三只大闸蟹。」", "Ordine: numero + classificatore + nome. Il 个 finale è di troppo; per i granchi si usa 只."),
    ("「霜降在星期五十月二十三日」", "→ 「霜降在10月23日,星期五。」", "Gli orari vanno dal grande al piccolo: prima mese e giorno, il giorno della settimana per ultimo."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易错诊所 · Errori frequenti", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「先付定金,后付尾款。」(Prima l'acconto, poi il saldo.) La struttura 先…后/再… dà l'ordine delle azioni. Altri esempi: 「先看天气,再出门。」「先洗手,再吃饭。」"
wcn = "Struttura: 先 … 后/再 … — prima X, poi Y. Inventa una frase tua."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本周句式 · La struttura settimanale", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「你好!我住在多伦多。霜降那天,我吃了柿子,也给妈妈打了电话。我的购物车里有一件外套,还在等付尾款。」"
lcn = "Una lettera di esempio della redazione — non è una lettera vera. Il VOL.2 pubblicherà le lettere vere dei lettori e il miglior testo di pagina 8!"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "读者园地 · L'angolo dei lettori", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本周金句 · Frasi della settimana (testuali, dagli articoli di questo numero)", 27, "sans", True, OLIVE)
quotes = [
    ("「今年的双11来得早」", "Il 双11 di quest'anno è arrivato presto.", "Pagina 1"),
    ("「付完尾款，快递就开始送货了」", "Pagato il saldo, la consegna parte.", "Pagina 1"),
    ("「付完尾款，商家就发货」", "Appena paghi il saldo, il venditore spedisce.", "Pagina 2"),
    ("「遥知兄弟登高处，遍插茱萸少一人」", "Il celebre verso di Wang Wei sul 重阳 (poesia).", "Pagina 3"),
    ("「两个分数只差2.735分」", "I due punteggi differiscono di soli 2.735 punti.", "Pagina 4"),
    ("「最大的看点是詹姆斯」", "L'attrazione più grande è LeBron.", "Pagina 4"),
    ("「看S16，要通宵了」", "Guardare l'S16 significa stare svegli tutta la notte.", "Pagina 5"),
    ("「先看数据，再看标题」", "Prima i dati, il titolo per ultimo (la regola di pagina 6).", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 150
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 150 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期预告 · La prossima settimana (VOL.2)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "S16 瑞士轮打完了:LPL 的四支队打得怎么样?双11 的包裹都到了吗?我们追踪报道。11月7日是立冬,冬天要来了。还有你们的来信和第 8 版最佳作文。下周见!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-ciyu.svg")
print("P7 saved, exercises so far:", len(REG))
