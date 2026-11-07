# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-nl-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · 練習與答案", "De Lucerna", "第 8 版 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "完形單選", "B", "辛特克拉斯新聞從 11 月 9 日開始",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "全國進城在赫拉弗舉行",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "阿姆斯特丹進城是第 88 屆",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "荷蘭—希臘之戰 20:45 開踢",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "聖馬丁節在 11 月 11 日",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "《魯濱遜遠征》在 RTL 4 播出",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "聖馬丁節是分享的節日",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "schoen zetten = 擺鞋子",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "單選", "A", "辛特克拉斯新聞每天 18:00 播出",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "單選", "B", "赫拉弗位於馬斯河畔",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "單選", "B", "辛特克拉斯在海事博物館接過城市鑰匙",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "單選", "A", "《晚餐》出版於 2009 年",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "單選", "B", "荷蘭和希臘都是 8 分",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "單選", "B", "德國—荷蘭，週一，柏林",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "單選", "B", "傳統會一直活下去，只要人們繼續慶祝它",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "單選", "C", "禮物之夜在 12 月 5 日週六",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "珊恩住在烏特勒支",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "單選", "B", "週三她參加聖馬丁遊行",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "單選", "B", "她在鞋子裡放一根胡蘿蔔和一份願望清單",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "單選", "B", "她每天 18:00 看辛特克拉斯新聞",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "造句", "Het Sinterklaasjournaal begint op maandag.", "主詞 + 動詞 + 時間",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Wij zetten onze schoen bij de deur.", "主詞 + 動詞 + 受詞 + 地點",
     "wij / zetten / onze schoen / bij de deur → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Oranje speelt vrijdag tegen Griekenland.", "主詞 + 動詞 + 時間 + 對手",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Ik loop met een lampion langs de deuren.", "主詞 + 動詞 + 方式 + 地點",
     "ik / loop / met een lampion / langs de deuren → ___", instr="造句", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻譯", "辛特克拉斯新聞每天 18:00 播出。", "對照第 3 版文章",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="翻譯", size=13.8, gap=0)
f.ex("B1", "翻譯", "聖馬丁節是分享的節日。", "第 2 版原句 · delen = 分享",
     "Sint-Maarten is het feest van het delen. → ___", instr="翻譯", size=13.8, gap=0)
f.ex("B1", "翻譯", "De intocht in Amsterdam is de 88e editie.", "注意序數 88e",
     "阿姆斯特丹進城是第 88 屆。→ ___", instr="翻譯", size=13.8, gap=0)
f.ex("B2", "翻譯", "Ik zet mijn schoen met een verlanglijstje.", "schoen zetten 是固定說法",
     "我擺出鞋子，裡面放著願望清單。→ ___", instr="翻譯", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "詞彙配對",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal = 新聞節目 b", "intocht = 慶典進城 d", "lampion = 燈籠 a", "delen = 分享 c"],
            instr="把詞和釋義配對")
f.head("G · DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "schoen = 鞋子",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "wortel = 胡蘿蔔（給馬的）",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "verlanglijstje = 願望清單",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "cadeautje = 小禮物",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "18:00 = 辛特克拉斯新聞時間",
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
f.expl(f"寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。")
f.ex("B1", "寫作", "（開放題，範文見下）", f"範文見 H 部分（{NWORDS} 詞）",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="寫作", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · 全部答案與簡析（第 1–8 版）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每題附一句繁體中文簡析 · 帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 第 {pg} 版 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
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
