# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/it-zh-tw-proof/baseline-w45-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · VALUTAZIONE E RISPOSTE =================
CURPAGE[0] = 8
p = BSPage4()
p.band("VALUTAZIONE E RISPOSTE · 练习与答案", "La Lucerna", "第 8 版 · La grande prova della settimana + tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1332, tag="P8-ex")
f.head("A · COMPLETA LA CRONACA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "primo freddo = 第一场寒冷",
     "Lunedì 2 novembre arriva il primo ___ della stagione. (A. caldo · B. freddo)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "追思日在 11 月 2 日",
     "Il 2 novembre è la Commemorazione dei ___. (A. defunti · B. santi)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "文化论坛在米兰开幕",
     "Il Forum Cultura apre martedì a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "潘妮托尼决赛在周六日",
     "La finale del Panettone è sabato e ___ a Milano. (A. domenica · B. lunedì)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "牛轧糖节在克雷莫纳",
     "La Festa del Torrone apre a ___. (A. Milano · B. Cremona)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "意甲第 11 轮周日收官：chiude",
     "L'undicesima giornata ___ domenica 8 novembre. (A. apre · B. chiude)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "佛罗伦萨对尤文图斯在周日晚上",
     "Fiorentina–Juventus si gioca domenica ___. (A. sera · B. mattina)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "民俗电影节在佛罗伦萨",
     "Il Festival dei Popoli è a ___. (A. Milano · B. Firenze)", size=15.5, gap=1)
f.head("B · DOMANDE GENERALI", 22, OLIVE, 5)
f.ex("A2", "单选", "B", "初雪在 1300–1500 米左右",
     "La prima neve leggera può cadere intorno ai... A. 500 m · B. 1.300–1.500 m · C. 3.000 m", size=15.5, gap=1)
f.ex("A2", "单选", "B", "追思日的花是菊花",
     "Il fiore del 2 novembre è... A. la rosa · B. il crisantemo · C. il tulipano", size=15.5, gap=1)
f.ex("A2", "单选", "A", "潘妮托尼决赛有 19 国糕点师",
     "Alla finale del Panettone partecipano pasticceri da... A. 19 paesi · B. 5 paesi · C. 50 paesi", size=15.5, gap=1)
f.ex("B1", "单选", "B", "文化论坛有 50 多场活动",
     "Il Forum Cultura ha... A. 5 eventi · B. più di 50 eventi · C. 19 eventi", size=15.5, gap=1)
f.ex("B1", "单选", "C", "阿尔巴松露节到 12 月 6 日",
     "La Fiera del Tartufo Bianco di Alba chiude... A. il 22 novembre · B. l'8 novembre · C. il 6 dicembre", size=15.5, gap=1)
f.ex("B1", "单选", "A", "DPB 于 10 月 15 日送出",
     "Il DPB è partito per Bruxelles... A. il 15 ottobre · B. il 19 ottobre · C. il 28 ottobre", size=15.5, gap=1)
f.ex("B2", "单选", "B", "概率不等于确定",
     "Una probabilità alta... A. è una certezza · B. non è una certezza · C. è un errore", size=15.5, gap=1)
f.ex("B1", "单选", "B", "卢卡漫画节 11 月 1 日闭幕",
     "Lucca Comics si è chiusa... A. il 28 ottobre · B. il 1° novembre · C. l'8 novembre", size=15.5, gap=1)
f.head("C · LEGGI E RISPONDI", 22, OLIVE, 5)
f.para("Giulia vive a Milano: sabato 7 novembre va alla finale del Panettone e assaggia il panettone tradizionale. Paolo vive a Cremona: sabato 7 novembre va alla Festa del Torrone. Domenica, Giulia e Paolo guardano la Serie A: fa freddo, ma il calcio non si ferma.", 16.5, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Giulia 去米兰潘妮托尼决赛",
     "Chi va alla finale del Panettone? A. Paolo · B. Giulia · C. i due", size=15.5, gap=1)
f.ex("A2", "单选", "A", "Paolo 周六去牛轧糖节",
     "Paolo, sabato, va... A. alla Festa del Torrone · B. a Milano · C. allo stadio", size=15.5, gap=1)
f.ex("A2", "单选", "B", "传统潘妮托尼是 Giulia 品尝的",
     "Il panettone tradizionale è assaggiato da... A. Paolo · B. Giulia · C. nessuno", size=15.5, gap=1)
f.ex("A2", "单选", "A", "标题概括两个城市、两个节日",
     "Il titolo migliore è... A. «Due città, due dolci» · B. «La manovra» · C. «Il meteo»", size=15.5, gap=1)
f.head("D · COSTRUISCI LE FRASI", 22, OLIVE, 5)
f.ex("A2", "造句", "Lunedì arriva il primo freddo.", "时间词在前",
     "lunedì / arriva / il primo freddo → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "La finale è a Milano il 7 novembre.", "主语 + essere + 地点 + 日期",
     "la finale / è a Milano / il 7 novembre → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "A che ora apre il Forum Cultura?", "疑问词组在句首",
     "a che ora / apre / il Forum Cultura / ? → ___", instr="造句", size=15.5, gap=1)
f.ex("B1", "造句", "Il freddo arriva lunedì.", "主语 + 动词 + 时间",
     "il freddo / arriva / lunedì → ___", instr="造句", size=15.5, gap=1)
f.head("E · TRADUCI", 22, OLIVE, 5)
f.ex("A2", "翻译", "周一第一场寒冷来了。", "对照原文",
     "Lunedì arriva il primo freddo. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B1", "翻译", "观众可以免费品尝。", "assaggiare gratis = 免费品尝",
     "Il pubblico può assaggiare gratis. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B1", "翻译", "周日晚上，佛罗伦萨对尤文图斯。", "si gioca = 进行比赛",
     "Domenica sera si gioca Fiorentina–Juventus. → ___", instr="翻译", size=15.5, gap=1)
f.ex("B2", "翻译", "Ogni previsione deve essere chiara.", "dovere = 必须",
     "每个预报都必须清楚。→ ___", instr="翻译", size=15.5, gap=1)
f.head("F · LE PAROLE DEL METEO", 22, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["la probabilità", "la media", "il bollettino", "il modello"],
            ["il valore medio, tra tanti valori",
             "il documento con le previsioni più recenti",
             "il calcolo che prevede il tempo, come l'ECMWF",
             "quanto è possibile che una cosa succeda"],
            ["d", "a", "b", "c"],
            ["probabilità=可能性 d", "media=平均值 a", "bollettino=预报公报 b", "modello=预报模型 c"],
            instr="把词和释义配对")
f.head("G · DIALOGO ALLA SAGRA", 22, OLIVE, 5)
f.ex("B1", "完形单选", "B", "torrone = 牛轧糖",
     "— Cerco il ___ di Cremona. (A. biglietto · B. torrone)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "mandorle 杏仁",
     "— È fatto di ___ e miele. (A. mandorle · B. patate)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "quanto costa? 多少钱",
     "— Quanto ___ tutto? (A. dorme · B. costa)", size=15.5, gap=1)
f.ex("B1", "完形单选", "A", "pagare con carta 刷卡",
     "— Pago con ___. (A. carta · B. cosplay)", size=15.5, gap=1)
f.ex("B1", "完形单选", "B", "牛轧糖节持续到 11 月 22 日",
     "— La festa dura fino al ___. (A. 6 dicembre · B. 22 novembre)", size=15.5, gap=1)
f.head("H · SCRIVI TU", 22, OLIVE, 5)
MODELO = ("Lunedì 2 novembre metto il cappotto e la sciarpa: arriva il primo freddo e la mattina è pungente. "
          "A scuola parliamo del Forum Cultura di Milano e del Festival dei Popoli di Firenze. "
          "Sabato assaggio il panettone con la mia famiglia: preferisco quello tradizionale, con i canditi. "
          "Domenica sera guardiamo Fiorentina–Juventus in televisione. "
          "Il freddo è arrivato, ma la settimana è dolce: cultura, dolci e calcio, come nel giornale. "
          "Lunedì prossimo racconto tutto alla classe, con le parole nuove del freddo.")
NWORDS = len(MODELO.split())
f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")
f.ex("B1", "写作", "（开放题，范文如下）", f"范文见本版 H 区（{NWORDS} 词）",
     "«La tua settimana del primo freddo» Scrivi 80–100 parole: il freddo, cosa metti, un evento o una festa del tuo weekend.", instr="写作", size=15.5, gap=1)
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
