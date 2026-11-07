# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-core/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · 练习与答案", "La Lucerna", "第 8 版 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "圣马丁 = San Martino",
     "Mercoledì 11 novembre è ___. (A. Natale · B. San Martino)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "葡萄汁变新酒",
     "A San Martino ogni mosto diventa ___. (A. vino · B. latte)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "意大利对法国在圣西罗",
     "Italia–Francia si gioca a ___. (A. San Siro · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "巧克力节在周五开幕",
     "Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "牛轧糖节在克雷莫纳",
     "La Festa del Torrone continua a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "民俗电影节 86 部影片",
     "Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "比利时对意大利在周日晚上",
     "Belgio–Italia si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "作家进城在库内奥",
     "Scrittorincittà è a ___. (A. Milano · B. Cuneo)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "圣马丁的夏天持续三天多一点",
     "L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora", size=15.5, gap=1)
f.ex("A2", "单选", "B", "斗篷是 Martino 分给乞丐的",
     "Martino divide... A. il pane · B. il mantello · C. il vino", size=15.5, gap=1)
f.ex("A2", "单选", "A", "巧克力节是第 32 届",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 67ª edizione", size=15.5, gap=1)
f.ex("B1", "单选", "B", "小组第一法国 10 分",
     "Nel girone di Nations League, la Francia ha... A. 7 punti · B. 10 punti · C. 0 punti", size=15.5, gap=1)
f.ex("B1", "单选", "C", "阿尔巴松露节到 12 月 6 日",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "单选", "A", "DPB 于 10 月 15 日送出",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "单选", "B", "政府提议不等于法律",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "单选", "B", "民俗电影节 11 月 8 日闭幕",
     "Il Festival dei Popoli si è chiuso... A. il 31 ottobre · B. l'8 novembre · C. il 15 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Cuneo: mercoledì 11 novembre va a Scrittorincittà e ascolta un autore. Paolo vive a Cremona: sabato 14 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano Belgio–Italia: è San Martino, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Giulia 周三去作家进城",
     "Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Paolo 周六去牛轧糖节",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "单选", "B", "作家是 Giulia 听的",
     "L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "单选", "A", "标题概括两个城市、两个节日",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "造句", "Mercoledì è San Martino.", "时间词在前",
     "mercoledì / è / San Martino → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "Eurochocolate è a Perugia dal 13 novembre.", "主语 + essere + 地点 + 日期",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "A che ora gioca l'Italia?", "疑问词组在句首",
     "a che ora / gioca / l'Italia / ? → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "Il vino nuovo si assaggia in cantina.", "主语 + 动词 + 地点",
     "il vino nuovo / si assaggia / in cantina → ___", instr="造句", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "圣马丁节葡萄汁变成酒。", "对照原文",
     "A San Martino ogni mosto diventa vino. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B1", "翻译", "周四晚上意大利对法国。", "si gioca = 进行比赛",
     "Giovedì sera si gioca Italia–Francia. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B1", "翻译", "周日晚上，比利时对意大利。", "si gioca = 进行比赛",
     "Domenica sera si gioca Belgio–Italia. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve essere chiara.", "dovere = 必须",
     "每个数字都必须清楚。→ ___", instr="翻译", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["la parte del sistema fiscale, un livello di reddito",
             "i soldi che pagano una misura, la sua fonte",
             "la differenza tra spese ed entrate, in rosso",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra=预算法案 d", "deficit=赤字 c", "copertura=资金来源 b", "scaglione=税级 a"],
            instr="把词和释义配对")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
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
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Mercoledì 11 novembre metto la sciarpa e vado in cantina: è San Martino e il vino nuovo si assaggia. "
          "A scuola parliamo della leggenda del mantello diviso e dell'estate di tre giorni. "
          "Sabato assaggio il torrone con la mia famiglia: preferisco quello di Cremona, con le mandorle e il miele. "
          "Giovedì sera guardiamo Italia–Francia in televisione, alle 20.45. "
          "Domenica, poi, il Belgio: due notti azzurre in una settimana. "
          "San Martino è arrivato, ma la settimana è dolce: vino nuovo, castagne e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove di San Martino.")
NWORDS = len(MODELO.split())
f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")
f.ex("B1", "写作", "（开放题，范文如下）", f"范文见本版 H 区（{NWORDS} 词）",
     "«La tua settimana di San Martino» Scrivi 80–100 parole: San Martino, cosa assaggi, un evento o una festa del tuo weekend.", instr="写作", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, GOLD, 2)
p.text(MX, 1382, "RISPOSTE · 参考答案 — 按版面分页排列，找到题号即可", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "每题附一句中文简析 · 带 ✓ 的为范文题", 19.5, "sans", False, GREY, anchor="end")
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
