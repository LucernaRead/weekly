# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE　练习与答案", "La Lucerna", "第8版　La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "tornare indietro = 往回拨",
     "Domenica l'orologio torna ___ di un'ora. (A. avanti · B. indietro)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "换时之夜有 25 小时",
     "La notte tra sabato e domenica dura ___ ore. (A. 25 · B. 23)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "incontrare = 迎战/对阵",
     "Alle 12:30 l'Inter ___ la Fiorentina a San Siro. (A. incontra · B. visita)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "那不勒斯–罗马在周六",
     "Napoli–Roma si gioca ___ alle 18:00. (A. sabato · B. domenica)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "蒙塔约内是松露节",
     "A Montaione è la festa del ___. (A. tartufo · B. cinema)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "电影节周日闭幕：chiude",
     "La Festa del Cinema di Roma ___ domenica 25. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "卢卡 10 月 28 日开幕：apre",
     "Lucca Comics ___ il 28 ottobre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "10 月 28 日是周三",
     "Il voto sulla manovra è atteso per ___ 28 ottobre. (A. lunedì · B. mercoledì)", size=15.5, gap=1)
f.head("B　DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "03:00 变回 02:00",
     "Il cambio dell'ora: alle 03:00 → ... A. 04:00 · B. 02:00 · C. 01:00", size=15.5, gap=1)
f.ex("A2", "单选", "B", "«meteo oggi» 是热搜第一",
     "«Meteo oggi» è... A. un film · B. la ricerca numero uno · C. una festa", size=15.5, gap=1)
f.ex("A2", "单选", "A", "风暴名叫 Adam",
     "La tempesta della settimana si chiama... A. Adam · B. Legacy · C. Bagòss", size=15.5, gap=1)
f.ex("B1", "单选", "B", "白松露节在阿尔巴",
     "La Fiera del Tartufo Bianco è a... A. Volterra · B. Alba · C. Bagolino", size=15.5, gap=1)
f.ex("B1", "单选", "C", "阿尔泰米西娅展在佛罗伦萨",
     "La mostra su Artemisia è a... A. Roma · B. Lucca · C. Firenze", size=15.5, gap=1)
f.ex("B1", "单选", "A", "DPB 于 10 月 15 日送出",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "单选", "B", "DPB 数字是预测",
     "Le cifre del DPB sono... A. risultati · B. previsioni · C. voti", size=15.5, gap=1)
f.ex("B1", "单选", "B", "诸圣节今年是 11 月 1 日周日",
     "Ognissanti, quest'anno, è... A. lunedì 2 novembre · B. domenica 1° novembre · C. sabato 31 ottobre", size=15.5, gap=1)
f.head("C　LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Lucca: mercoledì 28 ottobre va a Lucca Comics con il suo cosplay. Paolo vive a Roma: domenica 25 va all'Auditorium per l'ultimo giorno della Festa del Cinema. Sabato, Giulia e Paolo dormono un'ora in più: domenica comincia l'ora solare.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Giulia 去卢卡漫画节",
     "Chi va a Lucca Comics? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Paolo 周日去电影节",
     "Paolo, domenica, va... A. alla Festa del Cinema · B. a Lucca · C. a una sagra", size=15.5, gap=1)
f.ex("A2", "单选", "B", "cosplay 是 Giulia 的",
     "Il cosplay è di... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "单选", "A", "标题概括两座城、两个节",
     "Il titolo migliore è... A. «Due città, due feste» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D　COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "造句", "Domenica dormiamo un'ora in più.", "时间词在前",
     "domenica / dormiamo / un'ora in più → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "La fiera è iniziata il 10 ottobre.", "主语 + essere + 分词 + 日期",
     "la fiera / è iniziata / il 10 ottobre → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "A che ora comincia la partita?", "疑问词组在句首",
     "a che ora / comincia / la partita / ? → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "Il voto slitta a mercoledì.", "主语 + 动词 + 介词短语",
     "il voto / slitta / a mercoledì → ___", instr="造句", size=15.5, gap=1)
f.head("E　TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "周日我们多睡一个小时。", "对照原文",
     "Domenica dormiamo un'ora in più. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B1", "翻译", "展览一直开放到四月。", "resta aperta = 持续开放",
     "La mostra resta aperta fino ad aprile. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B1", "翻译", "Sabato alle 18:00 si gioca Napoli–Roma.", "si gioca = 进行比赛",
     "周六 18 点，那不勒斯对罗马。→ ___", instr="翻译", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni cifra deve avere una fonte.", "dovere = 必须",
     "每个数字都必须有来源。→ ___", instr="翻译", size=15.5, gap=1)
f.head("F　LE PAROLE DELLA MANOVRA", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["la manovra", "il rinvio", "il miliardo", "la previsione"],
            ["un numero che descrive il futuro",
             "la legge di bilancio dello Stato",
             "quando una cosa arriva più tardi del previsto",
             "mille milioni"],
            ["b", "c", "d", "a"],
            ["manovra=预算法案 b", "rinvio=迟于预定到达 c", "miliardo=十亿 d", "previsione=描述未来的数字 a"],
            instr="把词和释义配对")
f.head("G　DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "tartufo = 松露",
     "— Cerco il ___ bianco famoso. (A. biglietto · B. tartufo)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "castagne arrosto 烤栗子",
     "— Vuole anche le castagne ___? (A. arrosto · B. mute)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "quanto costa? 多少钱",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "pagare con carta 刷卡",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "美食节持续到周日",
     "— La sagra è in piazza fino a ___. (A. aprile · B. domenica)", size=15.5, gap=1)
f.head("H　SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Domenica 25 ottobre mi sveglio tardi: nella notte l'orologio è tornato indietro e ho dormito un'ora in più. "
          "Sabato sera ho cambiato gli orologi di casa: quello del forno e quello vecchio in cucina. "
          "Faccio colazione con calma e vado al mercato con mia sorella. A pranzo guardiamo Inter–Fiorentina: "
          "è la prima partita con l'ora solare. Nel pomeriggio leggo un libro e preparo la settimana. "
          "La sera è già buio presto, ma non mi dispiace: l'autunno è la mia stagione preferita, "
          "con le sagre, il tartufo e le castagne calde.")
NWORDS = len(MODELO.split())
f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")
f.ex("B1", "写作", "（开放题，范文如下）", f"范文见本版 H 区（{NWORDS} 词）",
     "«La tua domenica 25 ottobre» Scrivi 80–100 parole: il cambio dell'ora, cosa fai con l'ora in più, una partita o una festa del tuo weekend.", instr="写作", size=15.5, gap=1)
f.para("Testo modello: " + MODELO, 16, lh=1.3, split=False)
f.end_report()

# ================= RISPOSTE =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RISPOSTE　参考答案 — 按版面分页排列，找到题号即可", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每题附一句中文简析　带 ✓ 的为范文题", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
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
