# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-de-reproof/work/t10b/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Test & Lösungen", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · Der Test der Woche und alle Lösungen")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · Richtig oder falsch", 21, OLIVE, 5)
f.ex("A2", "完形单选", "A", "Winteranfang ist am 7. Nov.",
     "立冬在11月7日。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "立冬 ist der 19. Solarterm, nicht der 18.",
     "立冬是第18个节气。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "Spot-Ware wird ohne Anzahlungswartezeit versandt.",
     "现货要先付定金才能买。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "AL verlor alle drei Swiss-Runden-Serien.",
     "AL赢了三场比赛。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Die Viertelfinale beginnen um 06:00 Uhr Pekinger Zeit.",
     "四分之一决赛在北京时间早上6点开始。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Der KI-Film hat keine echten Schauspieler.",
     "《三星堆》电影里有真人演员。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Der neue Film startet am 7. Nov.",
     "新片《我们仅有一次的人生》11月7日上映。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Der Journalistentag ist am 8. Nov., nicht am 7.",
     "中国记者节在11月7日。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · Das große Quiz", 21, OLIVE, 5)
f.ex("A2", "单选", "B", "Die Spot-Verkäufe laufen bis zum 13. Nov.",
     "双11 现货一直卖到哪天? A. 11月11日 · B. 11月13日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "单选", "A", "Der Solarterm-Moment ist 17:52 Uhr.",
     "立冬交节在几点? A. 17点52分 · B. 18点52分 · C. 7点52分", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Erste Mikro-Jahreszeit: Das Wasser beginnt zu gefrieren.",
     "立冬三候第一候是什么? A. 地始冻 · B. 水始冰 · C. 雉入大水为蜃", size=13.8, gap=0)
f.ex("B1", "单选", "C", "IG schlug HLE am 26. Okt.",
     "IG打赢了哪个队? A. G2 · B. KC · C. HLE", size=13.8, gap=0)
f.ex("B1", "单选", "B", "TES schlug G2 am 26. Okt.",
     "TES打赢了哪个队? A. HLE · B. G2 · C. TL", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Bis Mittag am 26. Okt. zeigte Maoyan etwa 1,192 Mio. Yuan.",
     "AI电影票房约多少? A. 119.2万元 · B. 1192万元 · C. 11.92万元", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Huang Yan arbeitet in einem Krematorium.",
     "新片里黄燕是什么职业? A. 记者 · B. 火化师 · C. 老师", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Die WeChat-Shop-Aktion läuft 35 Tage.",
     "微信小店活动多少天? A. 35天 · B. 13天 · C. 18天", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Korb A zahlt nach dem Abzug 270 Yuan.",
     "篮子A实付多少钱? A. 270元 · B. 320元 · C. 240元", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Finale: 15. Nov., 03:00 Uhr Pekinger Zeit.",
     "总决赛在北京时间哪天? A. 11月14日凌晨3点 · B. 11月15日凌晨3点 · C. 11月8日早上6点", size=13.8, gap=0)
f.head("C · 完成句子 · Sätze vervollständigen", 21, OLIVE, 5)
f.ex("A2", "完成句子", "立冬", "Winteranfang ist am 7. Nov.",
     "11月7日是___。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("A2", "完成句子", "直降", "zhíjiàng — der Preis selbst sinkt.",
     "价格直接变低,这叫___。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "艾伦", "Àilún — Allen, Texas, Austragungsort der Swiss-Runde.",
     "瑞士轮在美国___市举行。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("A2", "完成句子", "饺子", "jiǎozǐ — nordchinesische Familien essen sie an 立冬.",
     "北方立冬吃___。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "数字", "shùzì — die Figuren des KI-Films sind digitale Bilder.",
     "AI电影的角色是___形象。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "票房", "piàofáng — Einnahmen aus dem Kartenverkauf.",
     "电影卖票的钱叫___。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B2", "完成句子", "结算", "jiésuàn — die Kassenseite zeigt den echten Preis.",
     "真正要付的钱,看___页。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("A2", "完成句子", "补冬", "bǔdōng — vor dem Winter gut essen.",
     "冬天以前吃点好的,这叫___。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "记者", "jìzhě — Journalist: interviewt, schreibt Nachrichten.",
     "采访和写新闻的人,叫___。", instr="Ausfüllen", size=13.8, gap=0)
f.ex("B1", "完成句子", "立减", "lìjiǎn — wird an der Kasse abgezogen.",
     "结算时直接减掉的钱叫___。", instr="Ausfüllen", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Lesen & antworten", 21, OLIVE, 5)
f.para("小红住在北京。11月7日星期六是立冬,她早上和妈妈一起包饺子,中午吃了热热的饺子。下午,她在网上买了一条围巾,现货第二天就到了。11月8日星期日,她给奶奶打了电话,问奶奶冷不冷。奶奶说,家里很暖和,让她多穿衣服。", 15, lh=1.3, split=False)
f.ex("A2", "单选", "A", "Xiao Hong wohnt in Peking.",
     "小红住在哪里? A. 北京 · B. 上海 · C. 广州", size=13.8, gap=0)
f.ex("A2", "单选", "A", "An 立冬 machte sie mit ihrer Mutter Teigtaschen.",
     "立冬那天她做了什么? A. 包饺子 · B. 看比赛 · C. 买毛衣", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Sie kaufte online einen Schal.",
     "她买了什么? A. 毛衣 · B. 围巾 · C. 帽子", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Am Sonntag rief sie ihre Großmutter an.",
     "她给谁打了电话? A. 妈妈 · B. 奶奶 · C. 老师", size=13.8, gap=0)
f.ex("B2", "单选", "A", "Reihenfolge: Teigtaschen, dann Einkaufen, dann Anruf.",
     "这段话的顺序是什么? A. 先包饺子,再买围巾,再打电话 · B. 先打电话,再包饺子 · C. 先买围巾,再包饺子", size=13.8, gap=0)
f.ex("B1", "完成句子", "北京", "Xiao Hong wohnt in Peking.",
     "小红住在___。", instr="Ausfüllen", size=13.8, gap=0)
f.head("E · 情景说话 · Im Gespräch", 21, OLIVE, 5)
f.ex("B1", "完形单选", "A", "Spot-Ware: sofort versandt, keine Vorverkaufswartezeit.",
     "— 现货几天能到? — 买了就能___,不用等预售。(A. 发货 · B. 退货)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Nordchinesische Familien essen an 立冬 Teigtaschen.",
     "— 立冬吃什么? — 北方吃___,南方吃法各不同。(A. 饺子 · B. 月饼)", size=13.8, gap=0)
f.ex("B2", "完形单选", "A", "Regel von Seite 6: erst Daten, dann Werbung.",
     "— 这条新闻说最低价,可信吗? — 先看___,再看广告。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · Schreiben", 21, OLIVE, 5)
MODELO = ("这个周末是立冬。星期六早上,我和妈妈一起包饺子,吃了热热的饺子,身体很暖和。"
          "下午,我去买了一件毛衣,现货第二天就到了。星期日,我给奶奶打了电话,问她冷不冷。"
          "冬天来了,我想多陪陪家人,过一个暖和的冬天。"
          "晚上,我看了S16的比赛,早上6点开始,很好看。双11还没结束,我又买了一条围巾,直降以后便宜了不少。"
          "这个冬天,我要早点睡觉,多穿衣服,不着凉。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Schreiben — keine einzige richtige Antwort. Ein Mustertext mit {NCHARS} Zeichen folgt.")
f.ex("B1", "写作", "(offene Aufgabe — Mustertext unten)", f"Offene Aufgabe — der Mustertext steht unten in Abschnitt F ({NCHARS} Zeichen)",
     "写一写《我的立冬周末》:立冬那天你做了什么?买了什么?冬天来了,你想做什么?写 120~180 字。", instr="Schreiben", size=13.8, gap=0)
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
