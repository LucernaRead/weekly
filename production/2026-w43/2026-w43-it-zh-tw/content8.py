# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　練習與答案", "La Lucerna", "第8版　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "完形單選", "B", "tornare indietro = 往回撥",
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "換時之夜有 25 小時",
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "incontrare = 迎戰/對陣",
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "那不勒斯–羅馬在週六",
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "蒙塔約內是松露節",
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "電影節週日閉幕：chiude",
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "盧卡 10 月 28 日開幕：apre",
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "10 月 28 日是週三",
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "單選", "B", "03:00 變回 02:00",
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", "單選", "B", "«meteo oggi» 是熱搜第一",
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", "單選", "A", "風暴名叫 Adam",
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", "單選", "B", "白松露節在阿爾巴",
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", "單選", "C", "阿爾泰米西婭展在佛羅倫薩",
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", "單選", "A", "DPB 於 10 月 15 日送出",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "單選", "B", "DPB 數字是預測",
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", "單選", "B", "諸聖節今年是 11 月 1 日週日",
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Giulia 去盧卡漫畫節",
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "單選", "A", "Paolo 週日去電影節",
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", "單選", "B", "cosplay 是 Giulia 的",
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "單選", "A", "標題概括兩座城、兩個節",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "造句", "Domenica dormiamo un'ora in più.", "時間詞在前",
     "domenica / dormiamo / un'ora in più → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "La fiera è iniziata il 10 ottobre.", "主語 + essere + 分詞 + 日期",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "A che ora comincia la partita?", "疑問詞組在句首",
     "a che ora / comincia / la partita / ? → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "Il voto slitta a mercoledì.", "主語 + 動詞 + 介詞短語",
     "il voto / slitta / a mercoledì → ___", instr="造句", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻譯", "週日我們多睡一個小時。", "對照原文",
     "Domenica dormiamo un'ora in più. → ___", instr="翻譯", size=15.5, gap=1)
f.ex("B1", "翻譯", "展覽一直開放到四月。", "resta aperta = 持續開放",
     "La mostra resta aperta fino ad aprile. → ___", instr="翻譯", size=15.5, gap=1)
f.ex("B1", "翻譯", "Sabato alle 18:00 si gioca Napoli–Roma.", "si gioca = 進行比賽",
     "週六 18 點，那不勒斯對羅馬。→ ___", instr="翻譯", size=15.5, gap=1)
f.ex("B2", "翻譯", "Ogni cifra deve avere una fonte.", "dovere = 必須",
     "每個數字都必須有來源。→ ___", instr="翻譯", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "詞彙配對",
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ["manovra=預算法案 b", "rinvio=遲於預定到達 c", "miliardo=十億 d", "previsione=描述未來的數字 a"],
            instr="把詞和釋義配對")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "完形單選", "B", "tartufo = 松露",
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "castagne arrosto 烤栗子",
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "quanto costa? 多少錢",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "完形單選", "A", "pagare con carta 刷卡",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "完形單選", "B", "美食節持續到週日",
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.expl(f"寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。")
f.ex("B1", "寫作", "（開放題，範文如下）", f"範文見本版 H 區（{NWORDS} 詞）",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr="寫作", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RISPOSTE　全部答案與簡析（第1–8版）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每題附一句中文簡析　帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 第 {pg} 版 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-valutazione.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
