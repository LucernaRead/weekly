# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Test und Lösungen", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · Der große Test dieser Woche und jeder Lösungsschlüssel")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · Richtig oder falsch", 21, OLIVE, 5)
f.ex("A2", "完形单选", "A", "Brandschutztag: 9. November.",
     "全国消防日在11月9日。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "35. Brandschutztag, nicht der 34.",
     "今年是第34个全国消防日。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "Paketwelle: drei Wellen, nicht eine.",
     "快递高峰只有一波。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "BLG im Viertelfinale, AL nicht.",
     "AL进了八强。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Viertelfinale: 06:00 Uhr Pekinger Zeit.",
     "四分之一决赛在北京时间早上6点开始。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Der Pianist: 1998, nicht 2019.",
     "《海上钢琴师》是2019年的电影。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Wiederveröffentlichung: 13. November.",
     "《海上钢琴师》11月13日重映。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Der Lesemonat begann am 1. November, nicht am 9. November.",
     "深圳读书月11月9日开幕。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · Das große Quiz", 21, OLIVE, 5)
f.ex("A2", "单选", "B", "Die Hauptverkaufszeit beginnt am 10. Nov. um 20:00 Uhr.",
     "高潮场从哪天晚上8点开始? A. 11月11日 · B. 11月10日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "单选", "A", "Feuerwehr-Notruf: 119.",
     "火警电话是多少? A. 119 · B. 110 · C. 120", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Erste Paketwelle: 20.–21. Oktober.",
     "第一波包裹高峰在哪两天? A. 10月31日 · B. 10月20日到21日 · C. 11月11日", size=13.8, gap=0)
f.ex("B1", "单选", "C", "TES–IG: 4. November.",
     "TES对IG在哪天? A. 11月6日 · B. 11月7日 · C. 11月4日", size=13.8, gap=0)
f.ex("B1", "单选", "B", "DK–BLG: 6. November.",
     "DK对BLG在哪天? A. 11月5日 · B. 11月6日 · C. 11月4日", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Die Douban-Wertung des Films ist 9,3.",
     "《海上钢琴师》豆瓣分数多少? A. 9.3分 · B. 8.3分 · C. 7.3分", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Kulturnacht: 14. November.",
     "文化馆之夜在哪天? A. 11月7日 · B. 11月14日 · C. 11月1日", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Ein kleiner Höhepunkt: etwa 1,5-mal ein normaler Tag.",
     "小高峰约是日常的几倍? A. 1.5倍 · B. 2.5倍 · C. 3.5倍", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Vorverlagerte Waren: +35 %.",
     "顺丰前置货量比去年多了多少? A. 35% · B. 20% · C. 50%", size=13.8, gap=0)
f.ex("B1", "单选", "B", "S16-Finale: 15. Nov., 03:00 Uhr Pekinger Zeit.",
     "总决赛在北京时间哪天? A. 11月14日凌晨3点 · B. 11月15日凌晨3点 · C. 11月8日早上6点", size=13.8, gap=0)
f.head("C · 完成句子 · Vervollständigen", 21, OLIVE, 5)
f.ex("A2", "完成句子", "消防", "Brandschutztag: 9. November.",
     "11月9日是全国___日。", instr="Ergänzen", size=13.8, gap=0)
f.ex("A2", "完成句子", "包裹", "bāoguǒ — ein Paket.",
     "买的东西装在___里。", instr="Ergänzen", size=13.8, gap=0)
f.ex("B1", "完成句子", "取件码", "qǔjiànmǎ — der Code, der das Fach öffnet.",
     "去快递柜拿包裹,先看___。", instr="Ergänzen", size=13.8, gap=0)
f.ex("A2", "完成句子", "高潮场", "gāocháochǎng — die Hauptverkaufszeit.",
     "11月10日晚上8点,___开始了。", instr="Ergänzen", size=13.8, gap=0)
f.ex("B1", "完成句子", "重映", "chóngyìng — einen alten Film wieder zeigen.",
     "老电影11月13日___了。", instr="Ergänzen", size=13.8, gap=0)
f.ex("B1", "完成句子", "修复", "xiūfù — die 4K-Fassung restauriert den alten Film.",
     "这一次是4K___版。", instr="Ergänzen", size=13.8, gap=0)
f.ex("B2", "完成句子", "预报", "yùbào — eine Vorhersage, noch keine Tatsache.",
     "冷空气的温度是___,还没发生。", instr="Ergänzen", size=13.8, gap=0)
f.ex("A2", "完成句子", "供暖", "gōngnuǎn — im Norden beginnt die Heizperiode.",
     "北方很多地方已经开始___了。", instr="Ergänzen", size=13.8, gap=0)
f.ex("B1", "完成句子", "疏散", "shūsàn — Übung übt den Fluchtweg.",
     "消防日那天,很多地方会做___演练。", instr="Ergänzen", size=13.8, gap=0)
f.ex("B1", "完成句子", "前置", "qiánzhì — Waren im Voraus nahe beim Käufer.",
     "包裹先___了,下单以前已经在路上。", instr="Ergänzen", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Lesen & antworten", 21, OLIVE, 5)
f.para("小林住在深圳。11月9日星期一,学校做了消防演练,小林学会了走楼梯、不坐电梯。11月11日星期三,小林在网上买的书到了,他用取件码打开快递柜,拿到了包裹。11月14日星期六晚上,小林和妈妈一起去文化馆,亲手摸了摸古籍。周日凌晨3点,他想早起看S16总决赛。", 15, lh=1.3, split=False)
f.ex("A2", "单选", "A", "Xiao Lin lebt in Shenzhen.",
     "小林住在哪里? A. 深圳 · B. 北京 · C. 广州", size=13.8, gap=0)
f.ex("A2", "单选", "A", "Am 9. November hielt die Schule eine Brandschutzübung ab.",
     "11月9日学校做了什么? A. 消防演练 · B. 期中考试 · C. 运动会", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Er kaufte ein Buch im Internet.",
     "他买了什么? A. 毛衣 · B. 书 · C. 帽子", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Er ging mit seiner Mutter ins Kulturzentrum.",
     "他和谁一起去文化馆? A. 爸爸 · B. 妈妈 · C. 老师", size=13.8, gap=0)
f.ex("B2", "单选", "A", "Reihenfolge: Übung, dann Paket, dann Kulturzentrum.",
     "这段话的顺序是什么? A. 先演练,再拿包裹,再去文化馆 · B. 先去文化馆,再演练 · C. 先拿包裹,再演练", size=13.8, gap=0)
f.ex("B1", "完成句子", "深圳", "Xiao Lin lebt in Shenzhen.",
     "小林住在___。", instr="Ergänzen", size=13.8, gap=0)
f.head("E · 情景说话 · Im Gespräch", 21, OLIVE, 5)
f.ex("B1", "完形单选", "A", "Prüfe den Abholcode, dann öffne das Fach.",
     "— 包裹到了,怎么办? — 先看___,再开柜门。(A. 取件码 · B. 电影票)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Bei einem Brand nimm die Treppe, nicht den Aufzug.",
     "— 着火了,怎么办? — 走___,不坐电梯。(A. 楼梯 · B. 电梯)", size=13.8, gap=0)
f.ex("B2", "完形单选", "A", "Die Regel von Seite 6: Daten zuerst, Werbung zuletzt.",
     "— 这条新闻说最大一波,可信吗? — 先看___,再看广告。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · Schreiben", 21, OLIVE, 5)
MODELO = ("这一周是双11那一周。星期一,学校做了消防演练,我学会了走楼梯、不坐电梯。"
          "星期二晚上8点,高潮场开始了,我买了一本书。星期三,我的包裹到了,我用取件码打开快递柜,拿到了书。"
          "星期六晚上,我和妈妈一起去文化馆,亲手摸了摸古籍,很有意思。"
          "星期日凌晨3点,我想早起看S16总决赛。这一周,又忙又开心,冬天真的来了,我要多穿衣服,不着凉。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Schreiben — keine einzige richtige Antwort. Ein Mustertext mit {NCHARS} Zeichen folgt.")
f.ex("B1", "写作", "(开放题，范文如下)", f"Offene Aufgabe — Mustertext oben in Abschnitt F ({NCHARS} Zeichen)",
     "写一写《我的双11那一周》:你买了什么?包裹到了吗?这一周,你还做了什么?写 120~180 字。", instr="Schreiben", size=13.8, gap=0)
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
