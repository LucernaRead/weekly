# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-core/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · 练习与答案", "De Lucerna", "第 8 版 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "完形单选", "B", "圣诞老人新闻 11 月 9 日开播",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "全国入城式在赫拉弗",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "阿姆斯特丹入城式是第 88 届",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "荷兰–希腊 20:45 开球",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "完形单选", "A", "圣马丁节在 11 月 11 日",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "Robinson 在 RTL 4 播出",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "圣马丁节是分享的节日",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "完形单选", "B", "schoen zetten = 放鞋子",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "单选", "A", "圣诞老人新闻每天 18:00 播出",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "单选", "B", "赫拉弗在马斯河畔",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "单选", "B", "圣诞老人在海事博物馆接受城市钥匙",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "单选", "A", "《晚餐》2009 年出版",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "单选", "B", "荷兰与希腊同积 8 分",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "单选", "B", "德国–荷兰周一在柏林",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "单选", "B", "传统靠人们继续庆祝而活着",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "单选", "C", "收礼夜在 12 月 5 日周六",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "单选", "B", "Sanne 住在乌得勒支",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "单选", "B", "她周三参加圣马丁游行",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "单选", "B", "她在鞋里放胡萝卜和愿望单",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "单选", "B", "她每天 18:00 看圣诞老人新闻",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "造句", "Het Sinterklaasjournaal begint op maandag.", "主语 + 动词 + 时间",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Wij zetten onze schoen bij de deur.", "主语 + 动词 + 宾语 + 地点",
     "wij / zetten / onze schoen / bij de deur → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Oranje speelt vrijdag tegen Griekenland.", "主语 + 动词 + 时间 + 对手",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Ik loop met een lampion langs de deuren.", "主语 + 动词 + 方式 + 地点",
     "ik / loop / met een lampion / langs de deuren → ___", instr="造句", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻译", "圣诞老人新闻每天 18:00 播出。", "对照第 3 版文章",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="翻译", size=13.8, gap=0)
f.ex("B1", "翻译", "圣马丁节是分享的节日。", "第 2 版原句 · delen 分享",
     "Sint-Maarten is het feest van het delen. → ___", instr="翻译", size=13.8, gap=0)
f.ex("B1", "翻译", "De intocht in Amsterdam is de 88e editie.", "注意序数词 88e",
     "阿姆斯特丹的入城式是第 88 届。→ ___", instr="翻译", size=13.8, gap=0)
f.ex("B2", "翻译", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten 是固定搭配",
     "我放好鞋子，里面放一张愿望单。→ ___", instr="翻译", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "词汇配对",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal=新闻节目 b", "intocht=入城式 d", "lampion=灯笼 a", "delen=分享 c"],
            instr="把词和释义配对")
f.head("G · DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
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
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 9 november begint het Sinterklaasjournaal. "
          "Ik kijk elke dag om 18:00 uur naar NPO Zapp. "
          "Op woensdag 11 november loop ik met een lampion langs de deuren en zing ik een liedje. "
          "Vrijdag kijk ik naar Oranje tegen Griekenland. "
          "Zaterdag kijk ik naar de intocht in Grave op televisie. "
          "Zondag vaart Sinterklaas in Amsterdam. "
          "Daarna zet ik mijn schoen met een wortel en een verlanglijstje. "
          "Ik hoop op een boek. "
          "Maandag 16 november speelt Oranje in Berlijn tegen Duitsland. "
          "Ik kijk ook dan. "
          "Wat een week vol licht!")
NWORDS = len(MODELO.split())
f.bridge(f"写作题（无唯一答案）；范文（{NWORDS} 词）见下。")
f.ex("B1", "写作", "（开放题，范文如下）", f"范文见本版 H 区（{NWORDS} 词）",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="写作", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · 参考答案 — 按版面分页排列，找到题号即可", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每题附一句中文简析 · 带 ✓ 的为范文题", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
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
