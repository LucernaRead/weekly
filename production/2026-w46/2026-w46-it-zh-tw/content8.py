# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-it-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · 練習與答案", "La Lucerna", "第 8 版 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "完形單選", "B", "聖馬丁 = San Martino",
     "Mercoledì 11 novembre è ___. (A. Natale · B. San Martino)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "葡萄汁變新酒",
     "A San Martino ogni mosto diventa ___. (A. vino · B. latte)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "義大利對法國在聖西羅",
     "Italia–Francia si gioca a ___. (A. San Siro · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "巧克力節在週五開幕",
     "Eurochocolate apre venerdì a ___. (A. Perugia · B. Cuneo)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "牛軋糖節在克雷莫納",
     "La Festa del Torrone continua a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "民俗電影節 86 部影片",
     "Il Festival dei Popoli ha presentato ___ film. (A. 50 · B. 86)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "比利時對義大利在週日晚上",
     "Belgio–Italia si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "作家進城在庫內奧",
     "Scrittorincittà è a ___. (A. Milano · B. Cuneo)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "單選", "B", "聖馬丁的夏天持續三天多一點",
     "L'estate di San Martino dura... A. un mese · B. tre giorni e un pochino · C. un'ora", size=15.5, gap=1)
f.ex("A2", "單選", "B", "斗篷是 Martino 分給乞丐的",
     "Martino divide... A. il pane · B. il mantello · C. il vino", size=15.5, gap=1)
f.ex("A2", "單選", "A", "巧克力節是第 32 屆",
     "Eurochocolate è alla sua... A. 32ª edizione · B. 29ª edizione · C. 67ª edizione", size=15.5, gap=1)
f.ex("B1", "單選", "B", "小組第一法國 10 分",
     "Nel girone di Nations League, la Francia ha... A. 7 punti · B. 10 punti · C. 0 punti", size=15.5, gap=1)
f.ex("B1", "單選", "C", "阿爾巴松露節到 12 月 6 日",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "單選", "A", "DPB 於 10 月 15 日送出",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "單選", "B", "政府提議不等於法律",
     "«Il governo propone»... A. è già legge · B. non è ancora legge · C. è un errore", size=15.5, gap=1)
f.ex("B1", "單選", "B", "民俗電影節 11 月 8 日閉幕",
     "Il Festival dei Popoli si è chiuso... A. il 31 ottobre · B. l'8 novembre · C. il 15 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Cuneo: mercoledì 11 novembre va a Scrittorincittà e ascolta un autore. Paolo vive a Cremona: sabato 14 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano Belgio–Italia: è San Martino, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Giulia 週三去作家進城",
     "Chi va a Scrittorincittà? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "單選", "A", "Paolo 週六去牛軋糖節",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Cuneo · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "單選", "B", "作家是 Giulia 聽的",
     "L'autore è ascoltato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "單選", "A", "標題概括兩個城市、兩個節日",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "造句", "Mercoledì è San Martino.", "時間詞在前",
     "mercoledì / è / San Martino → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "Eurochocolate è a Perugia dal 13 novembre.", "主語 + essere + 地點 + 日期",
     "Eurochocolate / è a Perugia / dal 13 novembre → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "A che ora gioca l'Italia?", "疑問詞組在句首",
     "a che ora / gioca / l'Italia / ? → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "Il vino nuovo si assaggia in cantina.", "主語 + 動詞 + 地點",
     "il vino nuovo / si assaggia / in cantina → ___", instr="造句", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻譯", "聖馬丁節葡萄汁變成酒。", "對照原文",
     "A San Martino ogni mosto diventa vino. → ___", instr="翻譯", size=15.5, gap=1)
f.ex("B1", "翻譯", "週四晚上義大利對法國。", "si gioca = 進行比賽",
     "Giovedì sera si gioca Italia–Francia. → ___", instr="翻譯", size=15.5, gap=1)
f.ex("B1", "翻譯", "週日晚上，比利時對義大利。", "si gioca = 進行比賽",
     "Domenica sera si gioca Belgio–Italia. → ___", instr="翻譯", size=15.5, gap=1)
f.ex("B2", "翻譯", "Ogni cifra deve essere chiara.", "dovere = 必須",
     "每個數字都必須清楚。→ ___", instr="翻譯", size=15.5, gap=1)
f.head("F · LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "詞彙配對",
            ["la manovra", "il deficit", "la copertura", "lo scaglione"],
            ["la parte del sistema fiscale, un livello di reddito",
             "i soldi che pagano una misura, la sua fonte",
             "la differenza tra spese ed entrate, in rosso",
             "la legge di bilancio, il documento dello Stato"],
            ["d", "c", "b", "a"],
            ["manovra=預算法案 d", "deficit=赤字 c", "copertura=資金來源 b", "scaglione=稅級 a"],
            instr="把詞和釋義配對")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "完形單選", "B", "torrone = 牛軋糖",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "mandorle = 杏仁",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "quanto costa? = 多少錢",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "pagare con carta = 刷卡",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "牛軋糖節持續到 11 月 22 日",
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
f.bridge(f"寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。")
f.ex("B1", "寫作", "（開放題，範文如下）", f"範文見本版 H 區（{NWORDS} 詞）",
     "«La tua settimana di San Martino» Scrivi 80–100 parole: San Martino, cosa assaggi, un evento o una festa del tuo weekend.", instr="寫作", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1344, GOLD, 2)
p.text(MX, 1382, "RISPOSTE · 全部答案與簡析（第 1–8 版）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1382, "每題附一句中文簡析 · 帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1408, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.14, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
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
