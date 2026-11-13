# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　练习与答案", "De Lucerna", "第8版　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "完形单选", "B", "德国–荷兰周一在柏林",
     "Duitsland – Nederland is op maandag in ___. (A. Amsterdam · B. Berlijn)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "荷兰与希腊同积 8 分",
     "Nederland en Griekenland hebben allebei ___ punten. (A. 5 · B. 8)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "荷兰进球 7 个",
     "Nederland maakte ___ doelpunten in vier wedstrijden. (A. 7 · B. 5)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "收礼夜在 12 月",
     "Pakjesavond is op ___ december. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "圣诞老人新闻 18:00",
     "Het Sinterklaasjournaal is elke dag om ___ uur. (A. 12:00 · B. 18:00)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Robinson 在 RTL 4",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "surprise 里有诗",
     "Bij een surprise hoort een ___. (A. liedje · B. gedicht)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "groepswinst = 小组头名",
     "«De groepswinst» betekent ___. (A. de laatste plaats · B. de eerste plaats in de groep)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "单选", "A", "圣诞老人新闻每天 18:00 播出",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "单选", "B", "赫拉弗在马斯河畔",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "单选", "B", "阿姆斯特丹入城式是第 88 届",
     "De intocht in Amsterdam was de... A. 26e editie · B. 88e editie · C. 30e editie", size=13.8, gap=0)
f.ex("B1", "单选", "A", "《晚餐》2009 年出版",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "单选", "B", "德国主场 0–1 输给希腊",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=13.8, gap=0)
f.ex("B1", "单选", "B", "PSV 以 26 分领跑荷甲",
     "PSV staat bovenaan in de Eredivisie met ___ punten. A. 25 · B. 26 · C. 8", size=13.8, gap=0)
f.ex("B2", "单选", "B", "传统靠人们继续庆祝而活着",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "单选", "C", "荷甲第 13 轮在 11 月 21–22 日",
     "Speelronde 13 is op... A. 13 en 14 november · B. 16 november · C. 21 en 22 november", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Rotterdam. Op maandag 16 november kijkt hij om 20:45 uur naar Duitsland – Nederland in Berlijn. Elke dag kijkt hij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag 21 november kijkt hij naar NEC – PSV. Zondag zet hij zijn schoen met een wortel en een verlanglijstje. Op zondagavond kijkt hij ook naar Expeditie Robinson.", 15, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Daan 住在鹿特丹",
     "Waar woont Daan? A. in Grave · B. in Rotterdam · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "单选", "B", "他周一看德国–荷兰",
     "Wat doet Daan op maandag 16 november? A. Hij kijkt naar Robinson · B. Hij kijkt naar Duitsland – Nederland · C. Hij leest Het diner", size=13.8, gap=0)
f.ex("A2", "单选", "B", "他鞋里放胡萝卜和愿望单",
     "Wat zit er in de schoen van Daan? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "单选", "B", "他每天 18:00 看圣诞老人新闻",
     "Wanneer kijkt Daan naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "造句", "Het Sinterklaasjournaal begint om 18:00 uur.", "主语 + 动词 + 时间",
     "het sinterklaasjournaal / begint / om 18:00 uur → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Wij zetten onze schoen bij de deur.", "主语 + 动词 + 宾语 + 地点",
     "wij / zetten / onze schoen / bij de deur → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Oranje speelt maandag in Berlijn.", "主语 + 动词 + 时间 + 地点",
     "oranje / speelt / maandag / in berlijn → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Ik zet mijn schoen met een wortel.", "主语 + 动词 + 宾语 + 方式",
     "ik / zet / mijn schoen / met een wortel → ___", instr="造句", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻译", "圣诞老人新闻每天 18:00 播出。", "对照第 3 版文章",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="翻译", size=13.8, gap=0)
f.ex("B1", "翻译", "前两名晋级四分之一决赛。", "第 4 版原句 · kwartfinale 四分之一决赛",
     "De nummers één en twee gaan naar de kwartfinales. → ___", instr="翻译", size=13.8, gap=0)
f.ex("B1", "翻译", "De intocht in Amsterdam was de 88e editie.", "注意序数词 88e",
     "阿姆斯特丹的入城式是第 88 届。→ ___", instr="翻译", size=13.8, gap=0)
f.ex("B2", "翻译", "Ik maak een surprise met een kort gedicht.", "surprise 是固定搭配",
     "我做一个带小诗的伪装礼物。→ ___", instr="翻译", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["het journaal", "de groepswinst", "de schoen", "het gedicht"],
            ["een klein versje bij een cadeau",
             "een dagelijks nieuwsprogramma op televisie",
             "de eerste plaats in de groep",
             "die staat 's avonds bij de deur"],
            ["b", "c", "d", "a"],
            ["journaal=新闻节目 b", "groepswinst=小组头名 c", "schoen=鞋子 d", "gedicht=诗 a"],
            instr="把词和释义配对")
f.head("G　DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "完形单选", "A", "schoen = 鞋",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "wortel = 胡萝卜（给马）",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "verlanglijstje = 愿望单",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "cadeautje = 小礼物",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "18:00 = 圣诞老人新闻时间",
     "— Eerst kijken we om ___ uur naar het Sinterklaasjournaal. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 16 november speelt Oranje in Berlijn tegen Duitsland. "
          "Ik kijk om 20:45 uur naar NPO 3. "
          "Elke dag kijk ik om 18:00 uur naar het Sinterklaasjournaal. "
          "Op woensdag schrijf ik een gedicht voor mijn surprise. "
          "Zaterdag kijk ik naar NEC – PSV. "
          "Zondag zet ik mijn schoen met een wortel en een verlanglijstje. "
          "Zondagavond kijk ik naar Expeditie Robinson. "
          "Daarna is het bijna pakjesavond, op zaterdag 5 december. "
          "Ik hoop op een boek. "
          "Wat een week vol voetbal en licht!")
NWORDS = len(MODELO.split())
f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")
f.ex("B1", "写作", "（开放题，范文如下）", f"范文见本版 H 区（{NWORDS} 词）",
     "«Mijn week met Oranje en Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, kijk jij naar Duitsland – Nederland, en zet jij je schoen?", instr="写作", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()
print("P8-ex flow ended col", f.ci, "y", round(f.y, 1), "(bottom 1252)")

# ---- P8 photo (W47: every page carries a public-domain image) ----
# Placed in the final exercise column, below the flow, only if it fits
# above the answers rule at y=1264 (image + caption must end by 1252).
if f.ci == 3 and f.y + 16 + 200 + 78 <= 1252:
    _px = COLX[f.ci]
    _py = f.y + 16
    image(p, "pen.jpg", _px, _py, CW, 200)
    _cy = caption(p, _px, _py + 200, CW, "Een vulpen op een schrift. Schrijf je opstel eerst met de hand — dan in het net.",
                  "Foto: Aaron Burden / Unsplash — CC0")
    print("P8 photo placed at", _px, _py, "ends", _cy)
else:
    print("!! P8 photo NOT placed: flow ended col", f.ci, "y", round(f.y, 1))

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　参考答案 — 按版面分页排列，找到题号即可", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每题附一句中文简析　带 ✓ 的为范文题", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "写作":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-toets.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
