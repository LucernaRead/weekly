# -*- coding: utf-8 -*-
# W46 zh-tw core, VOL.3: P8 test & keys (keys generated from the registry).
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-tw-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P8 · test & keys
CURPAGE[0] = 8
p = BSPage4()
p.band("測驗與答案 · Test & antwoorden", "Lucerna", "第 8 版 · 本週大測驗 + 全部答案 · De test van deze week en alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判斷對錯 · Waar of onwaar", 21, OLIVE, 5)
f.ex("A2", "完形單選", "A", "De reisbeurs sloot maandag 9 nov.",
     "台北旅展週一(11月9日)落幕。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "Double 11 is 11 nov., niet 9 nov.",
     "雙11在11月9日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "De parade is zondag 22 nov. om 14:00.",
     "封王遊行11月22日下午2點出發。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "De ceremonie is 22 nov., niet 15 nov.",
     "金馬獎頒獎典禮在11月15日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Arts in the Park is gratis toegankelijk.",
     "藝趣嘉年華免費入場。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B2", "完形單選", "B", "Het staalfestival sluit 22 nov., niet 15 nov.",
     "鋼雕藝術節11月15日閉幕。(A. 對 · B. 錯)", size=13.8, gap=0)
f.head("B · 本週大測驗 · De grote quiz", 21, OLIVE, 5)
f.ex("A2", "單選", "B", "De beurs is aan zijn 34e editie.",
     "今年旅展是第幾屆? A. 第30屆 · B. 第34屆 · C. 第40屆", size=13.8, gap=0)
f.ex("A2", "單選", "C", "Tickets ter plaatse kosten NT$ 200.",
     "旅展現場票多少錢? A. 180元 · B. 100元 · C. 200元", size=13.8, gap=0)
f.ex("B1", "單選", "A", "De nachtoptocht start om 20:30 op 14 nov.",
     "夜光巡遊11月14日晚上幾點開始? A. 8點30分 · B. 6點 · C. 10點", size=13.8, gap=0)
f.ex("B1", "單選", "B", "De concerten van Janice Vidal zijn in het Hong Kong Coliseum.",
     "衛蘭演唱會在哪裡? A. 維多利亞公園 · B. 紅磡香港體育館 · C. 南港展覽館", size=13.8, gap=0)
f.ex("B1", "單選", "C", "De bedenktijd is 7 dagen.",
     "鑑賞期是幾天? A. 3天 · B. 14天 · C. 7天", size=13.8, gap=0)
f.ex("B1", "單選", "A", "Noordelijke minima dalen onder de 20 graden.",
     "北台灣低溫會跌破幾度? A. 20度 · B. 30度 · C. 10度", size=13.8, gap=0)
f.ex("B2", "單選", "B", "587 films ingezonden.",
     "金馬獎有幾部影片報名? A. 87部 · B. 587部 · C. 57部", size=13.8, gap=0)
f.ex("B2", "單選", "A", "Novemberbezoeken leveren elk 10 punten op.",
     "11月運動一次拿幾個U幣? A. 10個 · B. 5個 · C. 100個", size=13.8, gap=0)
f.ex("B2", "單選", "C", "3,000 − 220 = 2,780.",
     "滿3,000折220,實付多少? A. 3,000元 · B. 2,220元 · C. 2,780元", size=13.8, gap=0)
f.ex("B2", "單選", "B", "Pakketten boven NT$ 2.000 kunnen invoerrechten krijgen.",
     "跨境包裹超過多少錢要補稅? A. 200元 · B. 2,000元 · C. 20,000元", size=13.8, gap=0)
f.head("C · 完成句子 · Vul in", 21, OLIVE, 5)
f.ex("A2", "完成句子", "落幕", "De beurs sloot op 9 nov.",
     "旅展11月9日___。", instr="Vul in", size=13.8, gap=0)
f.ex("A2", "完成句子", "清單", "Schrijf eerst je boodschappenlijst op.",
     "買東西之前,先列___。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "溫差", "Het dag-nachtverschil is groot.",
     "早晚___大,外套要隨身帶。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "入圍", "Genomineerd worden is 入圍.",
     "被選進得獎名單,叫___。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "遊行", "Een feestelijke optocht is 遊行.",
     "大家走上街頭慶祝,叫___。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "集點", "Punten sparen is 集點.",
     "每次運動累積點數,叫___。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "嘉年華", "Een carnaval is 嘉年華.",
     "銅鑼灣的免費活動叫藝趣___。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "打卡", "Inchecken met een foto is 打卡.",
     "在嘉年華拍照分享,叫___。", instr="Vul in", size=13.8, gap=0)
f.ex("B2", "完成句子", "門檻", "Controleer de bestedingsdrempel.",
     "領券之前,先看___。", instr="Vul in", size=13.8, gap=0)
f.ex("B2", "完成句子", "實付金額", "Het betaalde eindbedrag telt.",
     "比價要比___。", instr="Vul in", size=13.8, gap=0)
f.head("D · 讀一讀,答一答 · Lees en antwoord", 21, OLIVE, 5)
f.para("阿玲住在台北。週一(11月9日)她去南港展覽館,看了旅展最後一天,下午2點看了吉祥物大遊行。週三是雙11,她先列好清單,買了一本書450元、一件外套1,550元,加起來正好2,000元。週六她去香港銅鑼灣,看了免費的藝趣嘉年華,晚上8點30分看了夜光巡遊。", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Zij bezoekt de beurs op de laatste dag, maandag.",
     "阿玲週一去哪裡? A. 大巨蛋 · B. 南港展覽館 · C. 駁二", size=13.8, gap=0)
f.ex("B1", "單選", "B", "De parade is om 14:00.",
     "吉祥物大遊行在週一下午幾點? A. 12:00 · B. 14:00 · C. 19:00", size=13.8, gap=0)
f.ex("B1", "單選", "A", "450 + 1.550 = 2.000 in totaal.",
     "阿玲雙11買了多少錢? A. 2,000元 · B. 1,550元 · C. 450元", size=13.8, gap=0)
f.ex("B1", "單選", "A", "De nachtoptocht start om 20:30.",
     "夜光巡遊晚上幾點開始? A. 8點30分 · B. 6點 · C. 10點", size=13.8, gap=0)
f.ex("B2", "單選", "A", "Volgorde: beurs, dan winkelen, dan het carnaval.",
     "這三天她的順序是? A. 先看旅展,再買東西,再看嘉年華 · B. 先看嘉年華,再看旅展 · C. 先買東西,再看旅展,再看嘉年華", size=13.8, gap=0)
f.head("E · 情景說話 · Zeg het in context", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "De beurs sloot maandag 9 nov.",
     "— 旅展哪天落幕? — 週一___落幕。(A. 11月9日 · B. 11月6日)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "Double 11 is woensdag 11 nov.",
     "— 雙11是星期幾? — ___(A. 週一 · B. 週三)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "De bedenktijd is 7 dagen.",
     "— 鑑賞期是幾天? — ___(A. 7天 · B. 3天)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "De ceremonie is 22 nov.",
     "— 金馬獎哪天頒獎? — ___(A. 11月15日 · B. 11月22日)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "De parade start bij het Tianmu-stadion.",
     "— 封王遊行從哪裡出發? — ___(A. 天母棒球場 · B. 台北大巨蛋)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "Niet alleen korting, maar ook gratis verzending: 不但…而且….",
     "— 雙11有什麼好處? — 不但有___,而且有免運。(A. 折扣 · B. 門票)", size=13.8, gap=0)
f.head("F · 寫一寫 · Schrijven", 21, OLIVE, 5)
MODELO = ("雙11之前,我先列好購物清單:一本書450元,一件外套1,550元,加起來2,000元,正好是我的預算。"
          "我先領好優惠券,再比實付金額,最後才結帳。"
          "收到包裹7天內是鑑賞期,不合用可以退貨,但是吊牌不能拆。"
          "我沒有亂買,因為折扣大不等於便宜,實付金額才是真的。"
          "下週日我想去看封王遊行,穿紅色衣服為龍隊喝采。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Schrijven — er is niet één juist antwoord. Er volgt een model van {NCHARS} tekens.")
f.ex("B2", "寫作", "(開放題,範文如下)", f"Open opdracht — het modelantwoord staat hierboven in deel F ({NCHARS} tekens)",
     "寫一寫《我的雙11購物清單》:你想買什麼?預算多少?怎麼比價?收到包裹要注意什麼?寫 120~180 字。", instr="Schrijven", size=13.8, gap=0)
f.para("Modelantwoord: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= keys =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答案 · Antwoordsleutel — in paginavolgorde, met een korte Nederlandse noot bij elk item", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Alle noten in het Nederlands · ✓ = het modelantwoord", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Pagina {pg} —", 12.8, "sans", True, OLIVE, lh=1.12, gap=1, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 12.8, "sans", False, INK, lh=1.12, gap=1, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, exercises total:", len(REG))
