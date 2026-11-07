# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-cn-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Toets & antwoorden", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · De toets van deze week en alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · Waar of onwaar", 21, OLIVE, 5)
f.ex("A2", "完形单选", "A", "Nationale Branddag is op 9 november.",
     "全国消防日在11月9日。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "35e Nationale Branddag, niet de 34e.",
     "今年是第34个全国消防日。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "De pakketpiek: drie golven, niet één.",
     "快递高峰只有一波。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "BLG in de kwartfinales, AL niet.",
     "AL进了八强。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Kwartfinales: 06:00 Peking-tijd.",
     "四分之一决赛在北京时间早上6点开始。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "De pianist: 1998, niet 2019.",
     "《海上钢琴师》是2019年的电影。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Heruitgave: 13 november.",
     "《海上钢琴师》11月13日重映。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "De Leesmaand begon op 1 nov., niet op 9 nov.",
     "深圳读书月11月9日开幕。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · De grote quiz", 21, OLIVE, 5)
f.ex("A2", "单选", "B", "De piekverkoop begint 10 nov. om 20:00.",
     "高潮场从哪天晚上8点开始? A. 11月11日 · B. 11月10日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "单选", "A", "Het brandalarmnummer: 119.",
     "火警电话是多少? A. 119 · B. 110 · C. 120", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Eerste pakketgolf: 20–21 okt.",
     "第一波包裹高峰在哪两天? A. 10月31日 · B. 10月20日到21日 · C. 11月11日", size=13.8, gap=0)
f.ex("B1", "单选", "C", "TES–IG: 4 november.",
     "TES对IG在哪天? A. 11月6日 · B. 11月7日 · C. 11月4日", size=13.8, gap=0)
f.ex("B1", "单选", "B", "DK–BLG: 6 november.",
     "DK对BLG在哪天? A. 11月5日 · B. 11月6日 · C. 11月4日", size=13.8, gap=0)
f.ex("B1", "单选", "A", "De Douban-score van de film: 9,3.",
     "《海上钢琴师》豆瓣分数多少? A. 9.3分 · B. 8.3分 · C. 7.3分", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Cultuuravond: 14 november.",
     "文化馆之夜在哪天? A. 11月7日 · B. 11月14日 · C. 11月1日", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Een kleine piek: ongeveer 1,5× een normale dag.",
     "小高峰约是日常的几倍? A. 1.5倍 · B. 2.5倍 · C. 3.5倍", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Vooruitgeplaatste goederen: +35%.",
     "顺丰前置货量比去年多了多少? A. 35% · B. 20% · C. 50%", size=13.8, gap=0)
f.ex("B1", "单选", "B", "De finale begint 15 nov. om 03:00 Peking-tijd.",
     "总决赛在北京时间哪天? A. 11月14日凌晨3点 · B. 11月15日凌晨3点 · C. 11月8日早上6点", size=13.8, gap=0)
f.head("C · 完成句子 · Maak af", 21, OLIVE, 5)
f.ex("A2", "完成句子", "消防", "Nationale Branddag is op 9 november.",
     "11月9日是全国___日。", instr="Vul in", size=13.8, gap=0)
f.ex("A2", "完成句子", "包裹", "bāoguǒ — een pakket.",
     "买的东西装在___里。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "取件码", "qǔjiànmǎ — de code die het kluisje opent.",
     "去快递柜拿包裹,先看___。", instr="Vul in", size=13.8, gap=0)
f.ex("A2", "完成句子", "高潮场", "gāocháochǎng — de piekverkoopperiode.",
     "11月10日晚上8点,___开始了。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "重映", "chóngyìng — een oude film opnieuw vertonen.",
     "老电影11月13日___了。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "修复", "xiūfù — de 4K-versie herstelt de oude film.",
     "这一次是4K___版。", instr="Vul in", size=13.8, gap=0)
f.ex("B2", "完成句子", "预报", "yùbào — een voorspelling, nog geen feit.",
     "冷空气的温度是___,还没发生。", instr="Vul in", size=13.8, gap=0)
f.ex("A2", "完成句子", "供暖", "gōngnuǎn — de verwarming begint in het noorden.",
     "北方很多地方已经开始___了。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "疏散", "shūsàn — de oefening oefent de vluchtroute.",
     "消防日那天,很多地方会做___演练。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "前置", "qiánzhì — goederen van tevoren dicht bij de koper geplaatst.",
     "包裹先___了,下单以前已经在路上。", instr="Vul in", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Lees en antwoord", 21, OLIVE, 5)
f.para("小林住在深圳。11月9日星期一,学校做了消防演练,小林学会了走楼梯、不坐电梯。11月11日星期三,小林在网上买的书到了,他用取件码打开快递柜,拿到了包裹。11月14日星期六晚上,小林和妈妈一起去文化馆,亲手摸了摸古籍。周日凌晨3点,他想早起看S16总决赛。", 15, lh=1.3, split=False)
f.ex("A2", "单选", "A", "Xiao Lin woont in Shenzhen.",
     "小林住在哪里? A. 深圳 · B. 北京 · C. 广州", size=13.8, gap=0)
f.ex("A2", "单选", "A", "Op 9 november hield de school een brandoefening.",
     "11月9日学校做了什么? A. 消防演练 · B. 期中考试 · C. 运动会", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Hij kocht online een boek.",
     "他买了什么? A. 毛衣 · B. 书 · C. 帽子", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Hij ging met zijn moeder naar het cultuurcentrum.",
     "他和谁一起去文化馆? A. 爸爸 · B. 妈妈 · C. 老师", size=13.8, gap=0)
f.ex("B2", "单选", "A", "Volgorde: oefening, pakket, cultuurcentrum.",
     "这段话的顺序是什么? A. 先演练,再拿包裹,再去文化馆 · B. 先去文化馆,再演练 · C. 先拿包裹,再演练", size=13.8, gap=0)
f.ex("B1", "完成句子", "深圳", "Xiao Lin woont in Shenzhen.",
     "小林住在___。", instr="Vul in", size=13.8, gap=0)
f.head("E · 情景说话 · In gesprek", 21, OLIVE, 5)
f.ex("B1", "完形单选", "A", "Controleer de code en open het kluisje.",
     "— 包裹到了,怎么办? — 先看___,再开柜门。(A. 取件码 · B. 电影票)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Bij brand: de trap, niet de lift.",
     "— 着火了,怎么办? — 走___,不坐电梯。(A. 楼梯 · B. 电梯)", size=13.8, gap=0)
f.ex("B2", "完形单选", "A", "De regel van pagina 6: data eerst, reclame het laatst.",
     "— 这条新闻说最大一波,可信吗? — 先看___,再看广告。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · Schrijven", 21, OLIVE, 5)
MODELO = ("这一周是双11那一周。星期一,学校做了消防演练,我学会了走楼梯、不坐电梯。"
          "星期二晚上8点,高潮场开始了,我买了一本书。星期三,我的包裹到了,我用取件码打开快递柜,拿到了书。"
          "星期六晚上,我和妈妈一起去文化馆,亲手摸了摸古籍,很有意思。"
          "星期日凌晨3点,我想早起看S16总决赛。这一周,又忙又开心,冬天真的来了,我要多穿衣服,不着凉。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Schrijven — er is geen enkel juist antwoord. Hieronder volgt een voorbeeldtekst van {NCHARS} tekens.")
f.ex("B1", "写作", "(开放题，范文如下)", f"Open taak — de voorbeeldtekst staat hierboven in deel F ({NCHARS} tekens)",
     "写一写《我的双11那一周》:你买了什么?包裹到了吗?这一周,你还做了什么?写 120~180 字。", instr="Schrijven", size=13.8, gap=0)
f.para("Voorbeeldtekst: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Antwoorden — per pagina, met een toelichting bij elk antwoord", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Alle toelichting in het Nederlands · ✓ = de schrijfopdracht", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
