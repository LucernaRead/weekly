# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-it/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · 测验与答案 =================
CURPAGE[0] = 8
p = BSPage4()
p.band("测验与答案 · Test e soluzioni", "Lucerna", "第 8 版 · 本周大测验 + 全部答案 · Il test di questa settimana e tutte le soluzioni")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判断对错 · Vero o falso", 21, OLIVE, 5)
f.ex("A2", "Scelta in contesto", "A", "Chóngyáng è il giorno 9 del 9º mese lunare.",
     "重阳节在农历九月初九。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "Scelta in contesto", "B", "Shuāngjiàng (23 ott) viene DOPO Chóngyáng (18 ott) quest'anno.",
     "霜降在重阳节以前。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "Scelta in contesto", "A", "In una prevendita paghi prima l'acconto.",
     "预售的时候先付定金。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Scelta in contesto", "B", "La finale dell'S16 è a New York; LA ha ospitato i play-in.",
     "S16 总决赛在洛杉矶。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("A2", "Scelta in contesto", "A", "I saldi si sono aperti il 20 ottobre alle 20:00.",
     "付尾款的时间是10月20日晚上8点。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Scelta in contesto", "B", "Il calo misurato è stato circa il 25,8%, non il 40%.",
     "大闸蟹的价格真的降了40%。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Scelta in contesto", "A", "La squadra maschile cinese: bronzo con 249.193 punti.",
     "中国体操男队拿到铜牌。(A. 对 · B. 错)", size=13.8, gap=0)
f.ex("B1", "Scelta in contesto", "A", "È stata la decima sfilata di Victoria's Secret per Liu Wen.",
     "刘雯第十次走上维密的舞台。(A. 对 · B. 错)", size=13.8, gap=0)
f.head("B · 本周大测验 · Il grande quiz", 21, OLIVE, 5)
f.ex("A2", "Scelta multipla", "B", "Le vendite immediate durano fino al 13 novembre.",
     "双11 现货一直卖到哪天? A. 11月11日 · B. 11月13日 · C. 10月31日", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "A", "I cachi sono il cibo di Shuāngjiàng.",
     "霜降吃的是什么? A. 柿子 · B. 月饼 · C. 粽子", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "C", "La finale femminile è alle 01:30 del 22 ottobre, ora di Pechino.",
     "体操女团决赛在北京时间几点? A. 10月21日上午 · B. 10月22日晚上8点 · C. 10月22日凌晨1点30分", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "Produzione prevista del lago Yangcheng: circa 10.100 tonnellate.",
     "阳澄湖大闸蟹预计总产量是多少? A. 约1.01万吨 · B. 约10.1万吨 · C. 约101万吨", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "C", "Shuāngjiàng è venerdì 23 ottobre.",
     "霜降在10月几日? A. 20日 · B. 7日 · C. 23日", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "AL è la testa di serie n. 1 della LPL all'S16.",
     "LPL 的四支队里,哪支是一号种子? A. BLG · B. AL · C. IG", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "B", "I prezzi alla produzione sono in linea con gli ultimi 3 anni.",
     "协会说出水价怎么样? A. 涨了很多 · B. 和最近三年差不多 · C. 只有去年的一半", size=13.8, gap=0)
f.ex("A2", "Scelta multipla", "A", "jiǔyuè yuánqí — prima le femmine nel 9º mese lunare.",
     "农历九月先吃什么蟹? A. 母蟹 · B. 公蟹 · C. 小蟹", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "C", "LeBron ha debuttato con la maglia dei 76ers.",
     "詹姆斯穿上哪支队的球衣? A. 尼克斯 · B. 凯尔特人 · C. 76人", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "A", "yuánqí = la piastra ventrale rotonda della femmina.",
     "「九月圆脐十月尖」里,「圆脐」说的是: A. 母蟹的肚脐形状 · B. 月亮的形状 · C. 蟹的大小", size=13.8, gap=0)
f.head("C · 完成句子 · Completa le frasi", 21, OLIVE, 5)
f.ex("A2", "Completa la frase", "尾款", "Ora del saldo: 20 ottobre, 20:00.",
     "10月20日晚上8点付___。", instr="Completa", size=13.8, gap=0)
f.ex("A2", "Completa la frase", "定金", "Prima l'acconto in prevendita, il saldo dopo.",
     "预售先付___,后付尾款。", instr="Completa", size=13.8, gap=0)
f.ex("B1", "Completa la frase", "满减", "mǎnjiǎn — spendi 300, risparmi 50.",
     "买满300减50,这叫___。", instr="Completa", size=13.8, gap=0)
f.ex("B1", "Completa la frase", "鹿特丹", "I Mondiali di ginnastica erano a Rotterdam.",
     "体操世锦赛在荷兰___举行。", instr="Completa", size=13.8, gap=0)
f.ex("B1", "Completa la frase", "艾伦", "La fase svizzera dell'S16 è ad Allen, in Texas.",
     "S16 瑞士轮在美国___市举行。", instr="Completa", size=13.8, gap=0)
f.ex("A2", "Completa la frase", "柿子", "I cachi a Shuāngjiàng impediscono alle labbra di screpolarsi.",
     "霜降吃___,嘴唇不会裂。", instr="Completa", size=13.8, gap=0)
f.ex("B2", "Completa la frase", "滞销", "zhìxiāo — vendite lente, solo in poche zone periferiche.",
     "少数外围产区的蟹有点___,卖得慢。", instr="Completa", size=13.8, gap=0)
f.ex("B1", "Completa la frase", "直播", "zhíbō — la sfilata è andata in diretta.",
     "维密秀在网上___,很多人在线看。", instr="Completa", size=13.8, gap=0)
f.ex("B2", "Completa la frase", "声明", "shēngmíng — la dichiarazione ufficiale dell'associazione.",
     "协会发表___,说「崩盘」不是真的。", instr="Completa", size=13.8, gap=0)
f.ex("B1", "Completa la frase", "通宵", "tōngxiāo — svegli tutta la notte per la partita.",
     "比赛在凌晨,看比赛的人要___。", instr="Completa", size=13.8, gap=0)
f.head("D · 读一读,答一答 · Leggi e rispondi", 21, OLIVE, 5)
f.para("小林住在上海。他在网上看中了一件外套,先付了30元定金。10月20日晚上8点,他付了尾款。周五是霜降,他下班后去超市买了柿子。周六凌晨1点,他起来看 S16 的瑞士轮比赛,AL 打得很好。看完比赛,他睡了一个好觉。", 15, lh=1.3, split=False)
f.ex("A2", "Scelta multipla", "B", "Ha pagato un acconto di 30 yuan.",
     "小林先付了多少钱定金? A. 20元 · B. 30元 · C. 50元", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "A", "A Shuāngjiàng (venerdì) ha comprato cachi dopo il lavoro.",
     "霜降那天他做了什么? A. 下班后买柿子 · B. 陪妈妈爬山 · C. 通宵看比赛", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "C", "Ha guardato la partita all'01:00 di sabato.",
     "他看比赛的时间是? A. 周五晚上8点 · B. 周六上午 · C. 周六凌晨1点", size=13.8, gap=0)
f.ex("B1", "Scelta multipla", "B", "Ha guardato la fase svizzera dell'S16.",
     "他看的是哪个比赛? A. NBA · B. S16 瑞士轮 · C. 体操世锦赛", size=13.8, gap=0)
f.ex("B2", "Scelta multipla", "A", "Ordine: shopping, poi il termine solare, poi la partita.",
     "这段话的顺序是什么? A. 先购物,再过节气,再看比赛 · B. 先看比赛,再购物 · C. 先过节气,再看比赛,再购物", size=13.8, gap=0)
f.ex("B2", "Completa la frase", "上海", "Xiao Lin vive a Shanghai.",
     "小林住在___。", instr="Completa", size=13.8, gap=0)
f.head("E · 情景说话 · In conversazione", 21, OLIVE, 5)
f.ex("B1", "Scelta in contesto", "B", "La consegna parte dopo il pagamento del saldo, wěikuǎn.",
     "— 我的包裹到了吗? — 付完___,快递就开始送了。(A. 定金 · B. 尾款)", size=13.8, gap=0)
f.ex("B1", "Scelta in contesto", "A", "Il detto bǔdōng bùrú bǔ shuāngjiàng: mangiare bene a Shuāngjiàng.",
     "— 霜降要多穿点吗? — 要。___不如补霜降,先吃点好的。(A. 补冬 · B. 补夏)", size=13.8, gap=0)
f.ex("B2", "Scelta in contesto", "A", "La regola di pagina 6: prima i dati, il titolo per ultimo.",
     "— 这条新闻说价格崩盘,可信吗? — 先看___,再看标题。(A. 数据 · B. 评论)", size=13.8, gap=0)
f.head("F · 写一写 · Scrittura", 21, OLIVE, 5)
MODELO = ("我的双11购物车里有三样东西:一件外套、一条围巾和一盒柿子。"
          "外套260元,围巾60元,柿子40元,一共360元。"
          "今年有满300减50的活动,实付310元。"
          "我在预售时先付了30元定金,10月20日晚上8点付尾款280元。"
          "付完尾款,我就等快递了。霜降快到了,我想穿新外套、吃甜柿子,过一个暖和的秋天。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Scrittura — non c'è un'unica risposta giusta. Segue un modello di {NCHARS} caratteri.")
f.ex("B1", "Scrittura", "(domanda aperta — modello qui sotto)", f"Domanda aperta — il modello è nella sezione F di questa pagina, {NCHARS} caratteri",
     "写一写《我的双11购物车》:你想买什么?先付多少定金?尾款多少?一共多少钱?写 120~180 字。", instr="Scrivi", size=13.8, gap=0)
f.para("Risposta modello: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Soluzioni — per pagina, con una nota per ogni risposta", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Tutte le note in italiano · ✓ = il compito di scrittura", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} ({e_['note']})"
        if e_["type"] == "Scrittura":
            txt = f"{e_['n']}. ✓ ({e_['note']})"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-ceyan.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
