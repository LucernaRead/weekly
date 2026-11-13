# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/core-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　练习与答案", "La Lucerna", "第 8 版　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "拉齐奥 = Lazio",
     "La prima in classifica è la ___. (A. Roma · B. Lazio)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "第 11 轮共 24 球",
     "L'11ª giornata ha portato ___ gol. (A. 24 · B. 31)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "亚特兰大对国米在贝加莫",
     "Atalanta–Inter si gioca a ___. (A. Bergamo · B. Torino)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "牛轧糖节在周日闭幕",
     "La Festa del Torrone chiude domenica a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "巧克力节在佩鲁贾",
     "Eurochocolate chiude a ___. (A. Cremona · B. Perugia)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "圣母健康节在 11 月 21 日",
     "La Madonna della Salute si celebra il ___ novembre. (A. 20 · B. 21)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "米兰书城 11 月 23 日开幕",
     "BookCity apre lunedì ___. (A. 23 novembre · B. 22 novembre)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "都灵电影节 11 月 24 日开幕",
     "Il Torino Film Festival apre... A. il 20 novembre · B. il 24 novembre", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "榜首是拉齐奥 29 分",
     "La prima in classifica ha... A. 28 punti · B. 29 punti · C. 27 punti", size=15.5, gap=1)
f.ex("A2", "单选", "B", "国米 2–0 战胜科莫",
     "L'Inter vince 2–0 con... A. la Roma · B. il Como · C. il Milan", size=15.5, gap=1)
f.ex("A2", "单选", "A", "巧克力节是第 32 届",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 15ª edizione", size=15.5, gap=1)
f.ex("B1", "单选", "C", "乌迪内斯垫底 5 分",
     "L'ultima in classifica è... A. il Monza · B. il Venezia · C. l'Udinese", size=15.5, gap=1)
f.ex("B1", "单选", "C", "阿尔巴松露节到 12 月 6 日",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "单选", "A", "修正案截止 11 月 17 日 18 点",
     "Il termine per gli emendamenti è... A. il 17 novembre · B. il 9 novembre · C. il 31 dicembre", size=15.5, gap=1)
f.ex("B2", "单选", "B", "政府提议不等于法律",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "单选", "B", "圣母健康节源于 1630 年誓愿",
     "La festa della Salute nasce da un voto del... A. 1687 · B. 1630 · C. 1898", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Venezia: sabato 21 novembre attraversa il ponte votivo e porta una candela in basilica. Paolo vive a Cremona: domenica 22 novembre guarda il corteo del Torrone e assaggia il dolce con la sua famiglia. Domenica sera, Giulia e Paolo guardano Atalanta–Inter: è la festa del torrone, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Giulia 周六去圣母健康节",
     "Chi va alla Madonna della Salute? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Paolo 周日看牛轧糖节游行",
     "Paolo, domenica, guarda... A. il corteo del Torrone · B. il ponte votivo · C. lo stadio", size=15.5, gap=1)
f.ex("A2", "单选", "B", "蜡烛是 Giulia 带的",
     "La candela è portata da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "单选", "A", "标题概括两个城市、两个节日",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "造句", "Domenica è il 22 novembre.", "时间词在前",
     "domenica / è / il 22 novembre → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "Eurochocolate chiude a Perugia il 22 novembre.", "主语 + 动词 + 地点 + 日期",
     "Eurochocolate / chiude / a Perugia / il 22 novembre → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "A che ora gioca la Lazio?", "疑问词组在句首",
     "a che ora / gioca / la Lazio / ? → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "Il torrone si assaggia a Cremona.", "主语 + 动词 + 地点",
     "il torrone / si assaggia / a Cremona → ___", instr="造句", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "圣母健康节人们走过还愿桥。", "对照原文",
     "Per la Madonna della Salute si attraversa il ponte votivo. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B1", "翻译", "周日晚上亚特兰大对国米。", "si gioca = 进行比赛",
     "Domenica sera si gioca Atalanta–Inter. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B1", "翻译", "周六，拉齐奥在主场对莱切。", "in casa = 在主场",
     "Sabato la Lazio gioca in casa con il Lecce. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve essere chiara.", "dovere = 必须",
     "每个数字都必须清楚。→ ___", instr="翻译", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["un livello di reddito del sistema fiscale",
             "i soldi che pagano una misura",
             "la differenza tra spese ed entrate",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra = 预算法案 d", "deficit = 赤字 c", "copertura = 资金来源 b", "scaglione = 税级 a"],
            instr="把词和释义配对")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "torrone = 牛轧糖",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "mandorle = 杏仁",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "quanto costa? = 多少钱",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "pagare con carta = 刷卡",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "牛轧糖节持续到 11 月 22 日",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 22 novembre metto la sciarpa e vado a Cremona: è l'ultimo giorno della Festa del Torrone e il corteo passa in piazza del Comune. "
          "Assaggio il torrone con la mia famiglia: preferisco quello con le mandorle e il miele, a forma di Torrazzo. "
          "La sera guardiamo Atalanta–Inter, alle 20.45, e la Lazio è ancora prima con 29 punti. "
          "Sabato, a Venezia, c'era la Madonna della Salute: il ponte votivo e le candele accese. "
          "La settimana è dolce e azzurra: torrone, cioccolato e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove della settimana.")
NWORDS = len(MODELO.split())
f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")
f.ex("B1", "写作", "（开放题，范文如下）", f"范文见本版 H 区（{NWORDS} 词）",
     "«La tua domenica del 22 novembre» Scrivi 80–100 parole: una festa, una partita, cosa assaggi.", instr="写作", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()
print("P8 exercises flow ends col", f.ci, "y=", f.y)
# ---- Vermeer image under the exercises flow (measured slot, col 3) ----
if f.y + 10 + 170 + 70 <= 1332:
    image(p, "lettera.jpg", COLX[3], f.y + 10, CW, 170)
    caption(p, COLX[3], f.y + 180, CW, "Una donna scrive una lettera: la scrittura è l'ultimo esercizio della settimana.",
            "Foto: Johannes Vermeer — Wikimedia Commons, dominio pubblico")
    print("P8 lettera image placed at y=", f.y + 10)
else:
    print("  !! P8 LETTERA NOSPACE: flow ends y=", f.y)

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, OLIVE, 2)
p.text(MX, 1382, "RISPOSTE　参考答案 — 按版面分页排列，找到题号即可", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "每题附一句中文简析　带 ✓ 的为范文题", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13, lh=1.14, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
