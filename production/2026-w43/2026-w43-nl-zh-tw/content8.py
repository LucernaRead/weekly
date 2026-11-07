# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-nl-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN · 練習與答案", "De Lucerna", "第 8 版 · De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "完形單選", "B", "秋天時鐘撥回",
     "In de nacht van zaterdag op zondag gaat de klok één uur ___. (A. vooruit · B. achteruit)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "中部和南部的秋假到 10 月 25 日",
     "De herfstvakantie van Midden en Zuid duurt tot en met zondag ___ oktober. (A. 25 · B. 18)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "設計週在埃因霍溫",
     "De Dutch Design Week is in ___. (A. Eindhoven · B. Amsterdam)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "PSV 客場贏了波爾圖",
     "PSV won in de Champions League bij ___. (A. Atalanta · B. FC Porto)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "ADE 今年 30 年",
     "ADE wordt dit jaar ___ jaar. (A. 25 · B. 30)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Robinson 在 11 月開始",
     "Expeditie Robinson begint op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "最大的時鐘搜尋詞是 wintertijd",
     "De grootste zoekterm over de klok was «___». (A. wintertijd · B. klok vooruit)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "half drie = 2:30",
     "«Half drie» is ___. (A. 03:30 · B. 02:30)", size=13.8, gap=0)
f.head("B · ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "單選", "B", "冬令時凌晨 03:00 開始",
     "De wintertijd begint om... A. 02:00 uur · B. 03:00 uur · C. middernacht", size=13.8, gap=0)
f.ex("A2", "單選", "A", "北部地區 10 月 10–18 日放假",
     "Welke regio had vakantie van 10 tot en met 18 oktober? A. Noord · B. Midden · C. Zuid", size=13.8, gap=0)
f.ex("A2", "單選", "C", "學生票 € 19,50",
     "Een studentenkaartje voor de DDW kost... A. € 32,50 · B. € 25,00 · C. € 19,50", size=13.8, gap=0)
f.ex("B1", "單選", "A", "費耶諾德週三在塞維利亞",
     "Feyenoord speelt woensdag in... A. Sevilla · B. Porto · C. Eindhoven", size=13.8, gap=0)
f.ex("B1", "單選", "B", "斯巴達–阿賈克斯 16:45 開始",
     "Sparta – Ajax begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("B1", "單選", "B", "19 位參賽者是荷蘭人與佛蘭芒人",
     "De 19 kandidaten van Expeditie Robinson zijn... A. allemaal dj's · B. Nederlanders en Vlamingen · C. alleen sporters", size=13.8, gap=0)
f.ex("B2", "單選", "B", "6.600 人搜的是「前進」（問反了）",
     "De 6.600 zoekopdrachten vroegen naar... A. achteruit · B. vooruit · C. wintertijd", size=13.8, gap=0)
f.ex("B1", "單選", "A", "平台今後清楚展示全部額外費用",
     "Thuisbezorgd laat voortaan... A. alle extra kosten duidelijk zien · B. geen eten meer bezorgen · C. alleen kortingsbonnen zien", size=13.8, gap=0)
f.head("C · LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht, in de regio Midden. Zij heeft de hele week herfstvakantie. Op woensdag gaat zij met haar zus naar Eindhoven, naar de Dutch Design Week. Zaterdagavond zet zij alle klokken in huis één uur achteruit — behalve haar telefoon, die doet het zelf. Zondag slaapt zij lang uit: het is de laatste dag van de vakantie.", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Sanne 住在烏得勒支",
     "Waar woont Sanne? A. in Venlo · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "單選", "B", "她所在地區正在放秋假",
     "Waarom heeft Sanne de hele week vrij? A. Zij is ziek · B. Het is herfstvakantie in haar regio · C. Zij werkt niet", size=13.8, gap=0)
f.ex("A2", "單選", "B", "她週六晚上撥時鐘",
     "Wat doet Sanne zaterdagavond? A. Zij gaat dansen · B. Zij zet de klokken achteruit · C. Zij pakt haar koffer", size=13.8, gap=0)
f.ex("B1", "單選", "C", "手機自己改時間，不用手撥",
     "Welke klok zet Sanne NIET met de hand achteruit? A. de ovenklok · B. de wekker · C. haar telefoon", size=13.8, gap=0)
f.head("D · MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "造句", "De klok gaat één uur achteruit.", "主語 + 動詞 + 賓語 + 方向",
     "de klok / gaat / één uur / achteruit → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Wij gaan zondag naar de topper.", "主語 + 動詞 + 時間 + 地點",
     "wij / gaan / zondag / naar de topper → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Hoe laat begint de wedstrijd?", "疑問短語在句首",
     "hoe laat / begint / de wedstrijd / ? → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "PSV won met 1–0 in Porto.", "主語 + 動詞 + 比分 + 地點",
     "psv / won / met 1–0 / in porto → ___", instr="造句", size=13.8, gap=0)
f.head("E · VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻譯", "週日時鐘撥回：多睡一小時！", "對照第 1 版頭條帶",
     "Zondag gaat de klok terug: een uur langer slapen! → ___", instr="翻譯", size=13.8, gap=0)
f.ex("B1", "翻譯", "你的手機和電腦會自動更改時間。", "第 2 版原句 · veranderen 更改",
     "Je telefoon en je computer veranderen de tijd zelf. → ___", instr="翻譯", size=13.8, gap=0)
f.ex("B1", "翻譯", "De Dutch Design Week is in Eindhoven.", "注意地點短語 in Eindhoven",
     "荷蘭設計週在埃因霍溫。→ ___", instr="翻譯", size=13.8, gap=0)
f.ex("B2", "翻譯", "Zondag heb ik een uur langer geslapen.", "perfectum：heb geslapen",
     "週日我多睡了一個小時。→ ___", instr="翻譯", size=13.8, gap=0)
f.head("F · WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "詞彙配對",
            ["de klok verzetten", "het ezelsbruggetje", "eropuit gaan", "bijslapen"],
            ["extra slapen om uit te rusten",
             "het huis uit gaan voor iets leuks",
             "een hulpmiddel om iets te onthouden",
             "de tijd op een klok veranderen"],
            ["d", "c", "b", "a"],
            ["verzetten=撥時鐘 d", "ezelsbruggetje=助記口訣 c", "eropuit=出門遊玩 b", "bijslapen=補覺 a"],
            instr="把詞和釋義配對")
f.head("G · DIALOOG BIJ DE DDW", 21, OLIVE, 5)
f.ex("B1", "完形單選", "B", "kaartje = 門票",
     "— Goedemorgen! Een ___ voor de Dutch Design Week, alstublieft. (A. ezelsbruggetje · B. kaartje)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "student = 學生（票價 € 19,50）",
     "— Natuurlijk. Bent u ___? Studenten betalen € 19,50. (A. student · B. ontwerper)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "tot hoe laat = 開到幾點",
     "— Ja! Hier is mijn studentenkaart. En tot hoe ___ zijn jullie open? (A. lang · B. laat)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "veel plezier = 玩得開心",
     "— Tot 18:00 uur. Veel ___ met de ontwerpen! (A. plezier · B. slaap)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "tot ziens = 再見",
     "— Dank u wel, tot ___! (A. straks · B. ziens)", size=13.8, gap=0)
f.head("H · SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Zondag 25 oktober word ik laat wakker: het is de laatste dag van mijn herfstvakantie. "
          "Ik heb een uur langer geslapen, want vannacht ging de klok achteruit. "
          "Na het ontbijt ga ik met mijn vrienden naar het bos; de bladeren zijn geel en rood. "
          "'s Middags kijken wij thuis naar PSV tegen Feyenoord op televisie. "
          "Mijn zus gaat naar Amsterdam voor ADE, maar ik blijf liever thuis met een boek. "
          "'s Avonds pak ik mijn tas voor school: morgen begint het gewone leven weer. "
          "Wat een week!")
NWORDS = len(MODELO.split())
f.expl(f"寫作題（無唯一答案）；範本（{NWORDS} 詞）見下。")
f.ex("B1", "寫作", "（開放題，範本如下）", f"範本見本版 H 區（{NWORDS} 詞）",
     "«Jouw zondag 25 oktober» Schrijf 80–100 woorden: wat doe jij op de laatste vakantiedag, hoe laat sta jij op, en wat doe jij 's middags?", instr="寫作", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ANTWOORDEN · 全部答案與簡析（第 1–8 版）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每題附一句中文簡析 · 帶 ✓ 的為範本題", 19.5, "sans", False, GREY, anchor="end")
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
