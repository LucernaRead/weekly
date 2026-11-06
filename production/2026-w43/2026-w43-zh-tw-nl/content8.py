# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P8 · test & keys
CURPAGE[0] = 8
p = BSPage4()
p.band("測驗與答案 · Toets en antwoorden", "Lucerna", "第 8 版 · 本週大測驗 + 全部答案 · De grote toets van deze week en alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 判斷對錯 · Waar of onwaar", 21, OLIVE, 5)
f.ex("A2", "完形單選", "A", "Het Dubbelnegenfeest is maan 9/9.",
     "重陽節在農曆九月初九。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "De Hongkongse feestdag was ma 19 okt, niet 20 okt.",
     "香港重陽節翌日假期在10月20日。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "A", "Vrijdag en zaterdag zijn de dagen van dichtste nadering.",
     "颱風薔琵週五、週六最接近台灣。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "De Draken wonnen wedstrijd 1 met 3-0 — niet de Broers.",
     "台灣大賽第一戰,中信兄弟3比0贏味全龍。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "De dramaprijzen zijn op zaterdag; vrijdag zijn de programmaprijzen.",
     "金鐘獎戲劇類在週五頒獎。(A. 對 · B. 錯)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "400 - 258 = 142 bespaard met de proefpas.",
     "品味證比逐樣買便宜142港幣。(A. 對 · B. 錯)", size=13.8, gap=0)
f.head("B · 本週大測驗 · De grote quiz", 21, OLIVE, 5)
f.ex("A2", "單選", "B", "De zeewaarschuwing kan woensdagavond komen.",
     "海上颱風警報最快哪晚發佈? A. 週一 · B. 週三 · C. 週五", size=13.8, gap=0)
f.ex("A2", "單選", "B", "Neem 4 dagen verlof, krijg 9 dagen vrij.",
     "「請4放9」一共放幾天? A. 4天 · B. 9天 · C. 13天", size=13.8, gap=0)
f.ex("A2", "單選", "A", "Vrouwtjes (xiènǎi) zijn het best in de 9e maanmaand.",
     "農曆九月先吃什麼蟹? A. 蟹乸 · B. 蟹公 · C. 蟹仔", size=13.8, gap=0)
f.ex("A2", "單選", "B", "De uitverkoop van Tianmu begint donderdag 22 okt.",
     "天母店週年慶哪天開跑? A. 週二 · B. 週四 · C. 週六", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Best of seven: wie het eerst 4 wint.",
     "台灣大賽要先贏幾場才封王? A. 3場 · B. 4場 · C. 7場", size=13.8, gap=0)
f.ex("B1", "單選", "B", "De uitslag komt zaterdag tijdens de ceremonie.",
     "人氣獎結果何時公佈? A. 投票截止時 · B. 週六典禮當晚 · C. 週日早上", size=13.8, gap=0)
f.ex("B1", "單選", "C", "Meer dan 340 kraampjes doen mee.",
     "美酒佳餚巡禮有幾個攤位? A. 約140個 · B. 約240個 · C. 逾340個", size=13.8, gap=0)
f.ex("B1", "單選", "B", "De Halloweenstad van Taoyuan opent za 24 okt.",
     "桃園萬聖城哪天開城? A. 10月23日 · B. 10月24日 · C. 10月25日", size=13.8, gap=0)
f.ex("B2", "單選", "B", "De premiumpas bundelt voor HK$900 aan posten.",
     "尊尚品酒證的內容總值是? A. 558港幣 · B. 900港幣 · C. 400港幣", size=13.8, gap=0)
f.ex("B2", "單選", "A", "Cuì is de bijnaam van Taiwan voor Threads.",
     "哪個說法對? A. 「脆」是台灣對 Threads 的暱稱 · B. 「脆」是一種餅乾 · C. 「脆」是香港用法", size=13.8, gap=0)
f.head("C · 完成句子 · Vul in", 21, OLIVE, 5)
f.ex("A2", "完成句子", "共伴", "Tyfoon plus moesson: het gezamenlijke effect.",
     "颱風加東北季風,叫___效應。", instr="Vul in", size=13.8, gap=0)
f.ex("A2", "完成句子", "登高", "Hoog klimmen is het Dubbelnegengebruik.",
     "重陽節爬山,叫作___。", instr="Vul in", size=13.8, gap=0)
f.ex("A2", "完成句子", "疏運", "Shūyùn — de vakantievervoersoperatie.",
     "連假人多,台鐵、高鐵加開班次,這叫___。", instr="Vul in", size=13.8, gap=0)
f.ex("A2", "完成句子", "送百", "Besteed 1.000, krijg 100: mǎnqiān sòngbǎi.",
     "每滿一千送一百,叫滿千___。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "完封", "Een shutout: de tegenstander scoort nul.",
     "棒球比賽對手得0分,叫___。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "星光", "De rode loper is de xīngguāng dàdào.",
     "頒獎典禮走紅毯的部分,叫___大道。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "哈囉", "Hāluōwèi — Halloween in Hongkong.",
     "海洋公園的萬聖節,香港人叫___喂。", instr="Vul in", size=13.8, gap=0)
f.ex("B1", "完成句子", "12", "Een krab van 3 tael stoomt circa 12 minuten.",
     "蒸一隻3両的大閘蟹,約___分鐘。", instr="Vul in", size=13.8, gap=0)
f.ex("B2", "完成句子", "品味", "De bonnen zijn pǐnwèiquàn (proefmunten).",
     "美酒佳餚巡禮的券,叫___券。", instr="Vul in", size=13.8, gap=0)
f.ex("B2", "完成句子", "留友", "Liúyǒu kàn — bewaar het voor vrienden.",
     "看到好文存起來給朋友,叫「___看」。", instr="Vul in", size=13.8, gap=0)
f.head("D · 讀一讀,答一答 · Lees en antwoord", 21, OLIVE, 5)
f.para("阿哲住在台北。光復節連假,他週六晚上在家看台灣大賽第六戰(如果有需要)。週日晚上七點,他去天母看百鬼夜行踩街,還拿到一個南瓜桶。週一是補假,他睡到自然醒,下午去信義新天地逛週年慶,買了一雙鞋:2,600元,滿千送百,他拿到200元回饋券。三天連假,他過得很開心。", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Hij kijkt zaterdagavond naar de Taiwan Series.",
     "阿哲週六晚上看什麼? A. 金鐘獎 · B. 台灣大賽 · C. 電影", size=13.8, gap=0)
f.ex("B1", "單選", "B", "De optocht is zondag om 19:00.",
     "踩街在週日幾點? A. 17:00 · B. 19:00 · C. 21:00", size=13.8, gap=0)
f.ex("B1", "單選", "B", "Hij winkelt op de maandagfeestdag in Xinyi.",
     "他週一去哪裡逛週年慶? A. 天母店 · B. 信義新天地 · C. 台中中港店", size=13.8, gap=0)
f.ex("B1", "單選", "B", "2.600 = twee volle duizenden, dus 2 x 100 = 200 terug.",
     "鞋子2,600元,他拿到多少回饋券? A. 100元 · B. 200元 · C. 260元", size=13.8, gap=0)
f.ex("B2", "單選", "A", "Volgorde: honkbal, dan de optocht, dan winkelen.",
     "這三天他的順序是? A. 先看球,再踩街,再逛街 · B. 先逛街,再看球 · C. 先踩街,再逛街,再看球", size=13.8, gap=0)
f.head("E · 情景說話 · Zeg het in context", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "Controleer de waarschuwing voor je naar buiten gaat.",
     "— 明天會下雨嗎? — 颱風來了,先看___再出門。(A. 警報 · B. 菜單)", size=13.8, gap=0)
f.ex("A2", "完形單選", "B", "2.000 = twee duizenden, dus 200 aan vouchers.",
     "— 這件外套多少錢? — 2,000元,滿千送百,可以拿___元券。 A. 100 · B. 200", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Klimmen (dēnggāo) hoort bij het Dubbelnegenfeest.",
     "— 你重陽節做什麼? — 我去___,還吃了紅龜粿。(A. 登高 · B. 討糖)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "Wedstrijd 4 is op woensdag 21 okt.",
     "— G4 是哪天? — 週___,10月21日。(A. 二 · B. 三)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "De uitslag komt tijdens de ceremonie van zaterdag.",
     "— 人氣獎結果何時知道? — 週六___公佈。(A. 典禮當晚 · B. 下週一)", size=13.8, gap=0)
f.ex("B2", "完形單選", "A", "Liúyǒu kàn — bewaar de post voor vrienden.",
     "— 這篇文不錯。 — 我先存起來,___看。(A. 留友 · B. 哈囉)", size=13.8, gap=0)
f.head("F · 寫一寫 · Schrijven", 21, OLIVE, 5)
MODELO = ("光復節連假有三天。第一天,我在家看台灣大賽,如果打到第六戰,我一定準時打開電視。"
          "第二天晚上七點,我去天母看百鬼夜行,順便討糖。"
          "第三天是補假,我想睡晚一點,下午去信義新天地逛週年慶。"
          "下週四美酒佳餚巡禮開幕,我先買了兩張品味證,一共516元,準備帶媽媽去中環看海、吃好料。")
NCHARS = len(MODELO.replace(" ", ""))
f.glossline(f"Schrijven — er is geen enkel juist antwoord. Hieronder volgt een model van {NCHARS} tekens.")
f.ex("B2", "寫作", "(開放題,範文如下)", f"(Open opdracht — het modelantwoord staat hierboven in deel F ({NCHARS} tekens))",
     "寫一寫《我的連假計畫》:三天連假你想做什麼?哪天看什麼活動?要買什麼票?寫 120~180 字。", instr="Schrijf", size=13.8, gap=0)
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
    af.para(f"— Pagina {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, exercises total:", len(REG))
from collections import Counter
print("levels:", Counter(e_["level"] for e_ in REG))
print("writing model chars:", NCHARS)
