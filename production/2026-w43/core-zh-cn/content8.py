# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zhcn-vol1/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Test & keys", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · This week's test and every answer key")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · True or false", 21, OLIVE, 5)
f.ex("A2", "完形单选", "A", "重阳 is the 9th day of the 9th lunar month.",
     "重阳节在农历九月初九。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "B", "霜降 (Oct 23) comes AFTER 重阳 (Oct 18) this year.",
     "霜降在重阳节以前。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "A", "In a pre-sale you pay the deposit first.",
     "预售的时候先付定金。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "The S16 final is in New York; LA hosted play-ins.",
     "S16 总决赛在洛杉矶。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "完形单选", "A", "Tail payments opened Oct 20 at 20:00.",
     "付尾款的时间是10月20日晚上8点。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "The measured drop was about 25.8%, not 40%.",
     "大闸蟹的价格真的降了40%。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "China's men took bronze with 249.193 points.",
     "中国体操男队拿到铜牌。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "This was Liu Wen's 10th Victoria's Secret show.",
     "刘雯第十次走上维密的舞台。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · The big quiz", 21, OLIVE, 5)
f.ex("A2", "单选", "B", "Spot sales run until Nov 13.",
     "双11 现货一直卖到哪天? A. 11月11日 · B. 11月13日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "单选", "A", "Persimmons are the 霜降 food.",
     "霜降吃的是什么? A. 柿子 · B. 月饼 · C. 粽子", size=13.8, gap=0)
f.ex("B1", "单选", "C", "The women's final is at 01:30 on Oct 22, Beijing time.",
     "体操女团决赛在北京时间几点? A. 10月21日上午 · B. 10月22日晚上8点 · C. 10月22日凌晨1点30分", size=13.8, gap=0)
f.ex("B1", "单选", "A", "Expected Yangcheng Lake output: about 10,100 tonnes.",
     "阳澄湖大闸蟹预计总产量是多少? A. 约1.01万吨 · B. 约10.1万吨 · C. 约101万吨", size=13.8, gap=0)
f.ex("A2", "单选", "C", "霜降 is Friday, Oct 23.",
     "霜降在10月几日? A. 20日 · B. 7日 · C. 23日", size=13.8, gap=0)
f.ex("B1", "单选", "B", "AL is the LPL's No. 1 seed at S16.",
     "LPL 的四支队里,哪支是一号种子? A. BLG · B. AL · C. IG", size=13.8, gap=0)
f.ex("B2", "单选", "B", "Farm-gate prices are about level with the past 3 years.",
     "协会说出水价怎么样? A. 涨了很多 · B. 和最近三年差不多 · C. 只有去年的一半", size=13.8, gap=0)
f.ex("A2", "单选", "A", "九月圆脐 — female crabs first in the 9th lunar month.",
     "农历九月先吃什么蟹? A. 母蟹 · B. 公蟹 · C. 小蟹", size=13.8, gap=0)
f.ex("B1", "单选", "C", "LeBron debuted in a 76ers jersey.",
     "詹姆斯穿上哪支队的球衣? A. 尼克斯 · B. 凯尔特人 · C. 76人", size=13.8, gap=0)
f.ex("B2", "单选", "A", "圆脐 = the female crab's round belly flap (apron).",
     "「九月圆脐十月尖」里,「圆脐」说的是: A. 母蟹的肚脐形状 · B. 月亮的形状 · C. 蟹的大小", size=13.8, gap=0)
f.head("C · 完成句子 · Complete", 21, OLIVE, 5)
f.ex("A2", "完成句子", "尾款", "Tail-payment time: Oct 20, 20:00.",
     "10月20日晚上8点付___。", instr="Fill in", size=13.8, gap=0)
f.ex("A2", "完成句子", "定金", "Deposit first in a pre-sale, balance later.",
     "预售先付___,后付尾款。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "满减", "mǎnjiǎn — spend 300, save 50.",
     "买满300减50,这叫___。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "鹿特丹", "The gymnastics worlds were in Rotterdam.",
     "体操世锦赛在荷兰___举行。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "艾伦", "The S16 Swiss stage is in Allen, Texas.",
     "S16 瑞士轮在美国___市举行。", instr="Fill in", size=13.8, gap=0)
f.ex("A2", "完成句子", "柿子", "Persimmons at 霜降 keep lips from cracking.",
     "霜降吃___,嘴唇不会裂。", instr="Fill in", size=13.8, gap=0)
f.ex("B2", "完成句子", "滞销", "zhìxiāo — selling slowly, in a few outer areas only.",
     "少数外围产区的蟹有点___,卖得慢。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "直播", "zhíbō — the fashion show was livestreamed.",
     "维密秀在网上___,很多人在线看。", instr="Fill in", size=13.8, gap=0)
f.ex("B2", "完成句子", "声明", "shēngmíng — the association's official statement.",
     "协会发表___,说「崩盘」不是真的。", instr="Fill in", size=13.8, gap=0)
f.ex("B1", "完成句子", "通宵", "tōngxiāo — up all night for the match.",
     "比赛在凌晨,看比赛的人要___。", instr="Fill in", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Read & answer", 21, OLIVE, 5)
f.para("小林住在上海。他在网上看中了一件外套,先付了30元定金。10月20日晚上8点,他付了尾款。周五是霜降,他下班后去超市买了柿子。周六凌晨1点,他起来看 S16 的瑞士轮比赛,AL 打得很好。看完比赛,他睡了一个好觉。", 15, lh=1.3, split=False)
f.ex("A2", "单选", "B", "He paid a 30-yuan deposit.",
     "小林先付了多少钱定金? A. 20元 · B. 30元 · C. 50元", size=13.8, gap=0)
f.ex("B1", "单选", "A", "On 霜降 (Friday) he bought persimmons after work.",
     "霜降那天他做了什么? A. 下班后买柿子 · B. 陪妈妈爬山 · C. 通宵看比赛", size=13.8, gap=0)
f.ex("B1", "单选", "C", "He watched at 01:00 on Saturday.",
     "他看比赛的时间是? A. 周五晚上8点 · B. 周六上午 · C. 周六凌晨1点", size=13.8, gap=0)
f.ex("B1", "单选", "B", "He watched the S16 Swiss stage.",
     "他看的是哪个比赛? A. NBA · B. S16 瑞士轮 · C. 体操世锦赛", size=13.8, gap=0)
f.ex("B2", "单选", "A", "Order: shopping, then the solar term, then the match.",
     "这段话的顺序是什么? A. 先购物,再过节气,再看比赛 · B. 先看比赛,再购物 · C. 先过节气,再看比赛,再购物", size=13.8, gap=0)
f.ex("B2", "完成句子", "上海", "Xiao Lin lives in Shanghai.",
     "小林住在___。", instr="Fill in", size=13.8, gap=0)
f.head("E · 情景说话 · In conversation", 21, OLIVE, 5)
f.ex("B1", "完形单选", "B", "Delivery starts after the balance （尾款） is paid.",
     "— 我的包裹到了吗? — 付完___,快递就开始送了。(A. 定金 · B. 尾款)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "The saying: 补冬不如补霜降 — eat well at 霜降.",
     "— 霜降要多穿点吗? — 要。___不如补霜降,先吃点好的。(A. 补冬 · B. 补夏)", size=13.8, gap=0)
f.ex("B2", "完形单选", "A", "Page 6's rule: data first, headline last.",
     "— 这条新闻说价格崩盘,可信吗? — 先看___,再看标题。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · Writing", 21, OLIVE, 5)
MODELO = ("我的双11购物车里有三样东西:一件外套、一条围巾和一盒柿子。"
          "外套260元,围巾60元,柿子40元,一共360元。"
          "今年有满300减50的活动,实付310元。"
          "我在预售时先付了30元定金,10月20日晚上8点付尾款280元。"
          "付完尾款,我就等快递了。霜降快到了,我想穿新外套、吃甜柿子,过一个暖和的秋天。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Writing — there is no single right answer. A {NCHARS}-character model follows.")
f.ex("B1", "写作", "(开放题，范文如下)", f"Open task - the model answer is printed in section F above ({NCHARS} characters)",
     "写一写《我的双11购物车》:你想买什么?先付多少定金?尾款多少?一共多少钱?写 120~180 字。", instr="Writing", size=13.8, gap=0)
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
