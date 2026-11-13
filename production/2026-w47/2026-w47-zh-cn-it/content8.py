# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-cn-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案　Test e risposte", "Lucerna", "第8版　本周大测验 + 全部答案　Il grande test e tutte le risposte")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 194, 1300, tag="P8-ex")
f.head("A　判断对错　Vero o falso", 24, OLIVE, 5)
f.ex("A2", "完形单选", "A", "La Piccola Neve (小雪) è il 22 nov.",
     "小雪在11月22日。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("A2", "完形单选", "B", "小雪 è il 20º termine solare, non la 20ª Piccola Neve.",
     "今年是第20个小雪节气。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("A2", "完形单选", "B", "Il picco dei pacchi: tre ondate, non una.",
     "快递高峰只有一波。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "GEN è arrivato in finale, IG no.",
     "GEN进了决赛。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "Le semifinali iniziano alle ore 06:00 di Pechino.",
     "半决赛在北京时间早上6点开始。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "B", "《试探》 esce il 21 nov. 2026; è un film nuovo.",
     "《试探》是2019年的电影。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "《试探》 esce il 21 nov.",
     "《试探》11月21日上映。(A. 对 · B. 错)", size=17.5, gap=0)
f.ex("B1", "完形单选", "B", "Il Mese della Lettura è iniziato il 1º nov., non il 9.",
     "深圳读书月11月9日开幕。(A. 对 · B. 错)", size=17.5, gap=0)
f.head("B　本周大测验　Il grande quiz", 24, OLIVE, 5)
f.ex("A2", "单选", "B", "La finale inizia il 15 nov. alle 03:00 ora di Pechino.",
     "决赛在北京时间哪天？ A. 11月14日凌晨3点 · B. 11月15日凌晨3点 · C. 11月8日早上6点", size=17.5, gap=0)
f.ex("A2", "单选", "A", "BLG ha battuto T1 3-1 in semifinale.",
     "半决赛，BLG打赢了哪个队？ A. T1 · B. DK · C. IG", size=17.5, gap=0)
f.ex("B1", "单选", "B", "IG ha battuto TES 3-1 nei quarti di finale.",
     "四分之一决赛，IG打赢了哪个队？ A. GEN · B. TES · C. LYON", size=17.5, gap=0)
f.ex("B1", "单选", "B", "Il totale di 22 giorni è di 139,38 miliardi di articoli.",
     "22天快递总数是多少？ A. 7.77亿件 · B. 139.38亿件 · C. 6.34亿件", size=17.5, gap=0)
f.ex("B1", "单选", "B", "Il giorno migliore ha toccato 777 milioni di articoli.",
     "单日最高是多少？ A. 139.38亿件 · B. 7.77亿件 · C. 6.34亿件", size=17.5, gap=0)
f.ex("B1", "单选", "A", "《试探》, con Feng Shaofeng.",
     "《试探》的主演是谁？ A. 冯绍峰 · B. 刘德华 · C. 朱塞佩·托纳托雷", size=17.5, gap=0)
f.ex("B1", "单选", "B", "Notte culturale: 14 novembre.",
     "文化馆之夜在哪天？ A. 11月7日 · B. 11月14日 · C. 11月1日", size=17.5, gap=0)
f.ex("B1", "单选", "A", "小雪 è il 20º termine solare.",
     "小雪是第几个节气？ A. 第20个 · B. 第24个 · C. 第2个", size=17.5, gap=0)
f.ex("B1", "单选", "A", "La prima fase è 虹藏不见.",
     "小雪三候的第一候是什么？ A. 虹藏不见 · B. 天气上升 · C. 闭塞而成冬", size=17.5, gap=0)
f.ex("B1", "单选", "A", "La finale è BLG contro GEN.",
     "决赛的两个队是？ A. BLG和GEN · B. IG和T1 · C. TES和DK", size=17.5, gap=0)
f.head("C　完成句子　Completare", 24, OLIVE, 5)
f.ex("A2", "完成句子", "小雪", "La Piccola Neve (小雪) è il 22 nov.",
     "11月22日是___。", instr="Completa", size=17.5, gap=0)
f.ex("A2", "完成句子", "15", "La finale S16 è il 15 nov., ora di Pechino.",
     "决赛在11月___日凌晨3点。", instr="Completa", size=17.5, gap=0)
f.ex("B1", "完成句子", "T1", "BLG ha battuto T1 3-1 in semifinale.",
     "半决赛，BLG 3比1打赢了___。", instr="Completa", size=17.5, gap=0)
f.ex("A2", "完成句子", "139.38", "Il totale di 22 giorni è 139.38亿件.",
     "22天快递总数是___亿件。", instr="Completa", size=17.5, gap=0)
f.ex("B1", "完成句子", "21", "《试探》 esce il 21 nov.",
     "《试探》11月___日上映。", instr="Completa", size=17.5, gap=0)
f.ex("B1", "完成句子", "20", "小雪 è il 20º termine solare.",
     "小雪是第___个节气。", instr="Completa", size=17.5, gap=0)
f.ex("B2", "完成句子", "7.77", "Il giorno migliore ha toccato 7.77亿件.",
     "单日最高是___亿件。", instr="Completa", size=17.5, gap=0)
f.ex("A2", "完成句子", "14", "Notte culturale: 14 novembre.",
     "文化馆之夜在11月___日。", instr="Completa", size=17.5, gap=0)
f.ex("B1", "完成句子", "GEN", "La finale è BLG contro GEN.",
     "决赛是BLG对___。", instr="Completa", size=17.5, gap=0)
f.ex("B1", "完成句子", "冷", "Dopo la Piccola Neve, il tempo diventa più freddo.",
     "小雪之后，天气会更___。", instr="Completa", size=17.5, gap=0)
f.head("D　读一读，答一答　Leggi, rispondi", 24, OLIVE, 5)
f.para("小林住在深圳。11月8日星期日早上6点，小林看了半决赛，GEN 3比0打赢了IG。11月11日星期三，小林在网上买的书到了，他用取件码打开快递柜，拿到了包裹。11月14日星期六晚上，小林和妈妈一起去文化馆，亲手摸了摸古籍。11月15日星期日凌晨3点，他想早起看S16总决赛，BLG对GEN。", 19.5, lh=1.3, split=False)
f.ex("A2", "单选", "A", "Xiao Lin vive a Shenzhen.",
     "小林住在哪里？ A. 深圳 · B. 北京 · C. 广州", size=17.5, gap=0)
f.ex("A2", "单选", "A", "L'8 nov. ha guardato la semifinale.",
     "11月8日，小林看了什么？ A. 半决赛 · B. 期中考试 · C. 运动会", size=17.5, gap=0)
f.ex("B1", "单选", "B", "Ha comprato un libro online.",
     "他买了什么？ A. 毛衣 · B. 书 · C. 帽子", size=17.5, gap=0)
f.ex("B1", "单选", "B", "È andato al centro culturale con sua madre.",
     "他和谁一起去文化馆？ A. 爸爸 · B. 妈妈 · C. 老师", size=17.5, gap=0)
f.ex("B2", "单选", "A", "Ordine: semifinale, poi pacco, poi centro culturale.",
     "这段话的顺序是什么？ A. 先看半决赛，再拿包裹，再去文化馆 · B. 先去文化馆，再看半决赛 · C. 先拿包裹，再看半决赛", size=17.5, gap=0)
f.ex("B1", "完成句子", "深圳", "Xiao Lin vive a Shenzhen.",
     "小林住在___。", instr="Completa", size=17.5, gap=0)
f.head("E　情景说话　In conversazione", 24, OLIVE, 5)
f.ex("B1", "完形单选", "A", "Controlla il codice, poi apri l'armadietto.",
     "— 包裹到了，怎么办？ — 先看___，再开柜门。(A. 取件码 · B. 电影票)", size=17.5, gap=0)
f.ex("B1", "完形单选", "A", "Dopo la Piccola Neve, vestiti pesante, non prendere freddo.",
     "— 小雪之后，怎么办？ — 多穿一件，别___。(A. 着凉 · B. 熬夜)", size=17.5, gap=0)
f.ex("B2", "完形单选", "A", "La regola di pagina 6: prima i dati, la pubblicità per ultima.",
     "— 这条新闻说单日最高7.77亿件，可信吗？ — 先看___，再看广告。(A. 数据 · B. 评论)", size=17.5, gap=0)
f.head("F　写一写　Scrittura", 24, OLIVE, 5)
MODELO = ("这一周是小雪那一周。星期日凌晨3点，我想早起看S16总决赛，BLG对GEN。"
          "星期一，我的包裹到了，我用取件码打开快递柜，拿到了书。"
          "星期六，我和妈妈一起去看电影《试探》，故事很有意思。"
          "星期日是小雪，天气更冷了，我加了一件厚外套。这一周，又忙又开心，天冷了，我要多穿衣服，不着凉。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Scrittura — non c'è un'unica risposta giusta. Un modello di {NCHARS} caratteri segue.")
f.ex("B1", "写作", "(开放题，范文如下)", f"Esercizio aperto — modello sopra, sezione F ({NCHARS} caratteri).",
     "写一写《小雪那一周》：S16决赛、包裹、小雪，这一周你做了什么？写 120~180 字。", instr="Scrittura", size=17.5, gap=0)
f.para("Risposta modello: " + MODELO, 18.5, lh=1.3, split=False)
f.end_report()
print("P8 test flow ends col/y:", f.ci, round(f.y, 1))
# ---- P8 image (writing) in the free space at the bottom of col 3 ----
iy8 = f.y + 24
image(p, "writing.jpg", COLX[3], iy8, CW, 210)
cy8 = caption(p, COLX[3], iy8 + 210, CW, "写一写：先想一想，再下笔。（资料图）",
              "Foto: Tookapic — CC0 (Wikimedia Commons)")
print("P8 image ends", round(cy8, 1))

# ================= keys =================
p.hline(MX, RIGHT, 1320, OLIVE, 2)
p.text(MX, 1358, "答案　Risposte — per pagina, con una nota per ogni risposta", 25, "sans", True, OLIVE)
p.text(RIGHT, 1358, "Tutte le note in italiano　✓ = l'esercizio di scrittura", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1384, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0, split=False)
af.end_report()
print("P8 keys flow ends col/y:", af.ci, round(af.y, 1))
p.foot(8)
p.save(f"{OUT}/p8-ceyan.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
