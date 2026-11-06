# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Test & Lösungen", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · Der Test der Woche und alle Lösungen")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · Richtig oder falsch", 21, OLIVE, 5)
f.ex("A2", "完形单选", "A", "重阳 ist der 9. Tag des 9. Mondmonats.",
     "重阳节在农历九月初九。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "霜降 (23. Okt.) kommt dieses Jahr NACH 重阳 (18. Okt.).",
     "霜降在重阳节以前。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "A", "Im Vorverkauf zahlt man zuerst die Anzahlung.",
     "预售的时候先付定金。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Das S16-Finale ist in New York; LA trug die Play-ins aus.",
     "S16 总决赛在洛杉矶。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "A", "Die Restzahlung öffnete am 20. Okt. um 20:00 Uhr.",
     "付尾款的时间是10月20日晚上8点。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Der gemessene Rückgang war etwa 25,8 %, nicht 40 %.",
     "大闸蟹的价格真的降了40%。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Chinas Männer holten Bronze mit 249.193 Punkten.",
     "中国体操男队拿到铜牌。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Es war Liu Wens zehnte Victoria's-Secret-Show.",
     "刘雯第十次走上维密的舞台。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · Das große Quiz", 21, OLIVE, 5)
f.ex("A2", "单选", "B", "Der Lagerverkauf läuft bis zum 13. Nov.",
     "双11 现货一直卖到哪天? A. 11月11日 · B. 11月13日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "单选", "A", "Kaki sind das Essen zu 霜降.",
     "霜降吃的是什么? A. 柿子 · B. 月饼 · C. 粽子", size=13.8, gap=0)
f.ex("B1", "单选", "C", "Frauenfinale: 22. Okt., 01:30 Uhr Pekinger Zeit.",
     "体操女团决赛在北京时间几点? A. 10月21日上午 · B. 10月22日晚上8点 · C. 10月22日凌晨1点30分", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Produktion Yangcheng-See: etwa 10.100 Tonnen erwartet.",
     "阳澄湖大闸蟹预计总产量是多少? A. 约1.01万吨 · B. 约10.1万吨 · C. 约101万吨", size=13.8, gap=0)
f.ex("A2", "单选", "C", "霜降 ist Freitag, der 23. Okt.",
     "霜降在10月几日? A. 20日 · B. 7日 · C. 23日", size=13.8, gap=0)
f.ex("B1", "单选", "B", "AL ist die Nummer 1 der LPL bei S16.",
     "LPL 的四支队里,哪支是一号种子? A. BLG · B. AL · C. IG", size=13.8, gap=0)
f.ex("B2", "单选", "B", "Ab-Hof-Preise: etwa Niveau der letzten drei Jahre.",
     "协会说出水价怎么样? A. 涨了很多 · B. 和最近三年差不多 · C. 只有去年的一半", size=13.8, gap=0)
f.ex("A2", "单选", "A", "九月圆脐 — im 9. Mondmonat zuerst die Weibchen.",
     "农历九月先吃什么蟹? A. 母蟹 · B. 公蟹 · C. 小蟹", size=13.8, gap=0)
f.ex("B1", "单选", "C", "LeBron debütierte im Trikot der 76ers.",
     "詹姆斯穿上哪支队的球衣? A. 尼克斯 · B. 凯尔特人 · C. 76人", size=13.8, gap=0)
f.ex("B2", "单选", "A", "圆脐 = der runde Bauchdeckel der weiblichen Krabbe.",
     "「九月圆脐十月尖」里,「圆脐」说的是: A. 母蟹的肚脐形状 · B. 月亮的形状 · C. 蟹的大小", size=13.8, gap=0)
f.head("C · 完成句子 · Sätze vervollständigen", 21, OLIVE, 5)
f.ex("A2", "完成句子", "尾款", "Zeit der Restzahlung: 20. Okt., 20:00 Uhr.",
     "10月20日晚上8点付___。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("A2", "完成句子", "定金", "Vorverkauf: erst Anzahlung, später Restbetrag.",
     "预售先付___,后付尾款。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "满减", "mǎnjiǎn — 300 ausgeben, 50 sparen.",
     "买满300减50,这叫___。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "鹿特丹", "Die Turn-WM war in Rotterdam.",
     "体操世锦赛在荷兰___举行。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "艾伦", "Die Schweizer Runde von S16 ist in Allen, Texas.",
     "S16 瑞士轮在美国___市举行。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("A2", "完成句子", "柿子", "Kaki zu 霜降 — und die Lippen springen nicht auf.",
     "霜降吃___,嘴唇不会裂。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B2", "完成句子", "滞销", "zhìxiāo — langsamer Verkauf, nur in wenigen Randgebieten.",
     "少数外围产区的蟹有点___,卖得慢。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "直播", "zhíbō — die Modenschau wurde live gestreamt.",
     "维密秀在网上___,很多人在线看。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B2", "完成句子", "声明", "shēngmíng — offizielle Stellungnahme des Verbands.",
     "协会发表___,说「崩盘」不是真的。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "通宵", "tōngxiāo — für das Spiel die ganze Nacht wach.",
     "比赛在凌晨,看比赛的人要___。", instr="Ausfüllen", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Lesen & antworten", 21, OLIVE, 5)
f.para("小林住在上海。他在网上看中了一件外套,先付了30元定金。10月20日晚上8点,他付了尾款。周五是霜降,他下班后去超市买了柿子。周六凌晨1点,他起来看 S16 的瑞士轮比赛,AL 打得很好。看完比赛,他睡了一个好觉。", 15, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Er zahlte 30 Yuan Anzahlung.",
     "小林先付了多少钱定金? A. 20元 · B. 30元 · C. 50元", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Zu 霜降 (Freitag) kaufte er Kaki nach der Arbeit.",
     "霜降那天他做了什么? A. 下班后买柿子 · B. 陪妈妈爬山 · C. 通宵看比赛", size=13.8, gap=0)
f.ex("B1", "单选", "C", "Er schaute am Samstag um 01:00 Uhr zu.",
     "他看比赛的时间是? A. 周五晚上8点 · B. 周六上午 · C. 周六凌晨1点", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Er sah die Schweizer Runde von S16.",
     "他看的是哪个比赛? A. NBA · B. S16 瑞士轮 · C. 体操世锦赛", size=13.8, gap=0)
f.ex("B2", "单选", "A", "Reihenfolge: Einkauf, Solarterminus, Spiel.",
     "这段话的顺序是什么? A. 先购物,再过节气,再看比赛 · B. 先看比赛,再购物 · C. 先过节气,再看比赛,再购物", size=13.8, gap=0)
f.ex("B2", "完成句子", "上海", "Xiao Lin wohnt in Shanghai.",
     "小林住在___。", instr="Ausfüllen", size=13.8, gap=0)
f.head("E · 情景说话 · Im Gespräch", 21, OLIVE, 5)
f.ex("B1", "完形单选", "B", "Die Lieferung beginnt nach Zahlung des Restbetrags 尾款.",
     "— 我的包裹到了吗? — 付完___,快递就开始送了。(A. 定金 · B. 尾款)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Der Spruch: 补冬不如补霜降 — zu 霜降 gut essen.",
     "— 霜降要多穿点吗? — 要。___不如补霜降,先吃点好的。(A. 补冬 · B. 补夏)", size=13.8, gap=0)
f.ex("B2", "完形单选", "A", "Regel von Seite 6: erst Daten, dann die Schlagzeile.",
     "— 这条新闻说价格崩盘,可信吗? — 先看___,再看标题。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · Schreiben", 21, OLIVE, 5)
MODELO = ("我的双11购物车里有三样东西:一件外套、一条围巾和一盒柿子。"
          "外套260元,围巾60元,柿子40元,一共360元。"
          "今年有满300减50的活动,实付310元。"
          "我在预售时先付了30元定金,10月20日晚上8点付尾款280元。"
          "付完尾款,我就等快递了。霜降快到了,我想穿新外套、吃甜柿子,过一个暖和的秋天。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Schreiben — es gibt keine einzige richtige Antwort. Es folgt ein Mustertext mit {NCHARS} Zeichen.")
f.ex("B1", "写作", "(offene Aufgabe — Mustertext unten)", f"Offene Aufgabe — der Mustertext steht oben in Abschnitt F ({NCHARS} Zeichen)",
     "写一写《我的双11购物车》:你想买什么?先付多少定金?尾款多少?一共多少钱?写 120~180 字。", instr="Schreiben", size=13.8, gap=0)
f.para("Mustertext: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Lösungen — nach Seiten, mit einer Anmerkung zu jeder Antwort", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Alle Anmerkungen auf Deutsch · ✓ = die Schreibaufgabe", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Seite {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ceyan.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
