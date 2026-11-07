# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/zh-cn-ru-reproof/work/freeze-baseline/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Test & keys", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · This week's test and every answer key")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · True or false", 21, OLIVE, 5)
f.ex("A2", "完形单选", "A", "Start of Winter is on Nov 7.",
     "立冬在11月7日。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "立冬 is the 19th solar term, not the 18th.",
     "立冬是第18个节气。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "Spot goods ship without a deposit wait.",
     "现货要先付定金才能买。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "AL lost all three of its Swiss-stage series.",
     "AL赢了三场比赛。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Quarter-finals start at 06:00 Beijing time.",
     "四分之一决赛在北京时间早上6点开始。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "The AI film has no live actors.",
     "《三星堆》电影里有真人演员。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "The new film opens on Nov 7.",
     "新片《我们仅有一次的人生》11月7日上映。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Journalists' Day is on Nov 8, not Nov 7.",
     "中国记者节在11月7日。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · The big quiz", 21, OLIVE, 5)
f.ex("A2", "单选", "B", "Spot sales run until Nov 13.",
     "双11 现货一直卖到哪天? A. 11月11日 · B. 11月13日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "单选", "A", "The solar-term moment is 17:52.",
     "立冬交节在几点? A. 17点52分 · B. 18点52分 · C. 7点52分", size=13.8, gap=0)
f.ex("B1", "单选", "B", "First micro-season: water begins to freeze.",
     "立冬三候第一候是什么? A. 地始冻 · B. 水始冰 · C. 雉入大水为蜃", size=13.8, gap=0)
f.ex("B1", "单选", "C", "IG beat HLE on Oct 26.",
     "IG打赢了哪个队? A. G2 · B. KC · C. HLE", size=13.8, gap=0)
f.ex("B1", "单选", "B", "TES beat G2 on Oct 26.",
     "TES打赢了哪个队? A. HLE · B. G2 · C. TL", size=13.8, gap=0)
f.ex("B1", "单选", "A", "By noon on Oct 26, Maoyan showed about 1.192 million yuan.",
     "AI电影票房约多少? A. 119.2万元 · B. 1192万元 · C. 11.92万元", size=13.8, gap=0)
f.ex("B1", "单选", "B", "Huang Yan is a crematory worker.",
     "新片里黄燕是什么职业? A. 记者 · B. 火化师 · C. 老师", size=13.8, gap=0)
f.ex("B1", "单选", "A", "The WeChat shop event runs 35 days.",
     "微信小店活动多少天? A. 35天 · B. 13天 · C. 18天", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Basket A pays 270 yuan after the cut.",
     "篮子A实付多少钱? A. 270元 · B. 320元 · C. 240元", size=13.8, gap=0)
f.ex("B1", "单选", "B", "The final starts at 03:00 Beijing time on Nov 15.",
     "总决赛在北京时间哪天? A. 11月14日凌晨3点 · B. 11月15日凌晨3点 · C. 11月8日早上6点", size=13.8, gap=0)
f.head("C · 完成句子 · Complete", 21, OLIVE, 5)
f.ex("A2", "完成句子", "立冬", "Start of Winter is on Nov 7.",
     "11月7日是___。", instr="Fill in", size=13.8, gap=0)
f.ex("A2", "完成句子", "直降", "zhíjiàng — the price itself drops.",
     "价格直接变低,这叫___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "艾伦", "Àilún — Allen, Texas, hosts the Swiss stage.",
     "瑞士轮在美国___市举行。", instr="Fill in", size=13.8, gap=0)
f.ex("A2", "完成句子", "饺子", "jiǎozǐ — northern families eat these at 立冬.",
     "北方立冬吃___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "数字", "shùzì — the AI film's characters are digital images.",
     "AI电影的角色是___形象。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "票房", "piàofáng — box-office takings.",
     "电影卖票的钱叫___。", instr="Fill in", size=13.8, gap=0)
f.ex("B2", "完成句子", "结算", "jiésuàn — the checkout page shows the real price.",
     "真正要付的钱,看___页。", instr="Fill in", size=13.8, gap=0)
f.ex("A2", "完成句子", "补冬", "bǔdōng — eating well before winter.",
     "冬天以前吃点好的,这叫___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "记者", "jìzhě — a journalist interviews and writes news.",
     "采访和写新闻的人,叫___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "立减", "lìjiǎn — taken off at checkout.",
     "结算时直接减掉的钱叫___。", instr="Fill in", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Read & answer", 21, OLIVE, 5)
f.para("小红住在北京。11月7日星期六是立冬,她早上和妈妈一起包饺子,中午吃了热热的饺子。下午,她在网上买了一条围巾,现货第二天就到了。11月8日星期日,她给奶奶打了电话,问奶奶冷不冷。奶奶说,家里很暖和,让她多穿衣服。", 15, lh=1.3, split=False)
f.ex("A2", "单选", "A", "Xiao Hong lives in Beijing.",
     "小红住在哪里? A. 北京 · B. 上海 · C. 广州", size=13.8, gap=0)
f.ex("A2", "单选", "A", "On 立冬 she made dumplings with her mother.",
     "立冬那天她做了什么? A. 包饺子 · B. 看比赛 · C. 买毛衣", size=13.8, gap=0)
f.ex("B1", "单选", "B", "She bought a scarf online.",
     "她买了什么? A. 毛衣 · B. 围巾 · C. 帽子", size=13.8, gap=0)
f.ex("B1", "单选", "B", "She phoned her grandmother on Sunday.",
     "她给谁打了电话? A. 妈妈 · B. 奶奶 · C. 老师", size=13.8, gap=0)
f.ex("B2", "单选", "A", "Order: dumplings, then shopping, then the phone call.",
     "这段话的顺序是什么? A. 先包饺子,再买围巾,再打电话 · B. 先打电话,再包饺子 · C. 先买围巾,再包饺子", size=13.8, gap=0)
f.ex("B1", "完成句子", "北京", "Xiao Hong lives in Beijing.",
     "小红住在___。", instr="Fill in", size=13.8, gap=0)
f.head("E · 情景说话 · In conversation", 21, OLIVE, 5)
f.ex("B1", "完形单选", "A", "Spot goods ship right away, no pre-sale wait.",
     "— 现货几天能到? — 买了就能___,不用等预售。(A. 发货 · B. 退货)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "Northern families eat dumplings at 立冬.",
     "— 立冬吃什么? — 北方吃___,南方吃法各不同。(A. 饺子 · B. 月饼)", size=13.8, gap=0)
f.ex("B2", "完形单选", "A", "Page 6's rule: data first, advertisement last.",
     "— 这条新闻说最低价,可信吗? — 先看___,再看广告。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · Writing", 21, OLIVE, 5)
MODELO = ("这个周末是立冬。星期六早上,我和妈妈一起包饺子,吃了热热的饺子,身体很暖和。"
          "下午,我去买了一件毛衣,现货第二天就到了。星期日,我给奶奶打了电话,问她冷不冷。"
          "冬天来了,我想多陪陪家人,过一个暖和的冬天。"
          "晚上,我看了S16的比赛,早上6点开始,很好看。双11还没结束,我又买了一条围巾,直降以后便宜了不少。"
          "这个冬天,我要早点睡觉,多穿衣服,不着凉。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Writing — there is no single right answer. A {NCHARS}-character model follows.")
f.ex("B1", "写作", "(开放题，范文如下)", f"Open task - the model answer is printed in section F above ({NCHARS} characters)",
     "写一写《我的立冬周末》:立冬那天你做了什么?买了什么?冬天来了,你想做什么?写 120~180 字。", instr="Writing", size=13.8, gap=0)
f.para("Model answer: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Answer keys — by page, with a note on every answer", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "All notes in English · ✓ = the writing task", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Page {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
