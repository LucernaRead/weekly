# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　練習與答案", "De Lucerna", "第8版　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "完形單選", "B", "氣候週到 11 月 8 日",
     "De Klimaatweek duurt van 2 tot en met ___ november. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "科弗登發放 200 棵樹木灌木",
     "Coevorden deelt ___ bomen en struiken uit. (A. 100 · B. 200)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "博物館之夜在 11 月 7 日",
     "Museumnacht is op zaterdag ___ november. (A. 6 · B. 7)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "特溫特–阿賈克斯 13:30 開球",
     "Twente – Ajax begint om ___ uur. (A. 11:15 · B. 13:30)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "阿賈克斯 2–0 贏亞特蘭大",
     "Ajax won van Atalanta met ___. (A. 2–0 · B. 4–1)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "Robinson 在 11 月開始",
     "Expeditie Robinson begon op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "橙色預警：天氣危險",
     "Code oranje betekent: het weer is ___. (A. veilig · B. gevaarlijk)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "meedoen = 參加",
     "«Meedoen» betekent ___. (A. weggaan · B. deelnemen)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "單選", "A", "氣候週 11 月 2 日週一開始",
     "De Klimaatweek begint op... A. maandag 2 november · B. dinsdag 3 november · C. zaterdag 7 november", size=13.8, gap=0)
f.ex("A2", "單選", "B", "發放地點在茲韋洛",
     "De bomen in Coevorden worden uitgedeeld in... A. Amsterdam · B. Zweeloo · C. Rotterdam", size=13.8, gap=0)
f.ex("A2", "單選", "B", "Crossing Border 在海牙",
     "Crossing Border is in... A. Amsterdam · B. Den Haag · C. Utrecht", size=13.8, gap=0)
f.ex("B1", "單選", "A", "PAN 在 RAI 展覽中心",
     "PAN Amsterdam is in... A. de RAI · B. het Rijksmuseum · C. de Jaarbeurs", size=13.8, gap=0)
f.ex("B1", "單選", "B", "皇家貝蒂斯 1–0 贏費耶諾德",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=13.8, gap=0)
f.ex("B1", "單選", "B", "10 輪後阿賈克斯 21 分",
     "Na 10 ronden heeft Ajax ___ punten. A. 24 · B. 21 · C. 20", size=13.8, gap=0)
f.ex("B2", "單選", "B", "預警疲勞：警告太多導致不再注意",
     "Waarschuwingsmoeheid betekent... A. moe van het weer · B. minder opletten door te veel waarschuwingen · C. een nieuwe code", size=13.8, gap=0)
f.ex("B1", "單選", "C", "扎安丹舊貨市場約 250 個攤位",
     "De Snuffelmarkt in Zaandam heeft zo'n ___ kramen. A. 70 · B. 200 · C. 250", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Coevorden. Op zaterdag 7 november gaat hij naar de Fair Groen in Zweeloo en haalt hij een gratis struik op. 's Avonds kijkt hij naar de foto's van Museumnacht in Amsterdam — zelf gaat hij niet, want zondag speelt zijn club Twente tegen Ajax om 13:30 uur. En in de Klimaatweek fietst Daan elke dag naar school, ook als het regent.", 15, lh=1.3, split=False)
f.ex("A2", "單選", "B", "Daan 住在科弗登",
     "Waar woont Daan? A. in Zweeloo · B. in Coevorden · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "單選", "B", "他週六領了一棵免費灌木",
     "Wat haalt Daan op zaterdag op? A. een fiets · B. een gratis struik · C. een kaartje", size=13.8, gap=0)
f.ex("A2", "單選", "B", "週日特溫特對阿賈克斯",
     "Waarom gaat Daan zaterdagavond niet naar Amsterdam? A. Hij heeft geen kaartje · B. Zondag speelt Twente tegen Ajax · C. Hij houdt niet van musea", size=13.8, gap=0)
f.ex("B1", "單選", "B", "氣候週他每天騎車上學",
     "Wat doet Daan in de Klimaatweek? A. Hij rijdt elke dag met de auto · B. Hij fietst elke dag naar school · C. Hij blijft thuis", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "造句", "De Klimaatweek begint op maandag.", "主語 + 動詞 + 時間",
     "de klimaatweek / begint / op maandag → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Wij planten een boom in de tuin.", "主語 + 動詞 + 賓語 + 地點",
     "wij / planten / een boom / in de tuin → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Twente speelt zondag tegen Ajax.", "主語 + 動詞 + 時間 + 對手",
     "twente / speelt / zondag / tegen ajax → ___", instr="造句", size=13.8, gap=0)
f.ex("B1", "造句", "Ik doe mee aan de Klimaatweek.", "可分動詞 mee 在句末",
     "ik / doe / mee / aan de klimaatweek → ___", instr="造句", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻譯", "氣候週持續七天。", "對照第 1 版頭條",
     "De Klimaatweek duurt zeven dagen. → ___", instr="翻譯", size=13.8, gap=0)
f.ex("B1", "翻譯", "橙色預警意味著：做好準備。", "第 2 版原句 · bereid je voor 做好準備",
     "Code oranje betekent: bereid je voor. → ___", instr="翻譯", size=13.8, gap=0)
f.ex("B1", "翻譯", "Museumnacht duurt van 19:00 uur tot 02:00 uur.", "注意時間表達 van...tot...",
     "博物館之夜從晚上 19 點到凌晨 2 點。→ ___", instr="翻譯", size=13.8, gap=0)
f.ex("B2", "翻譯", "Ik doe mee aan de Klimaatweek.", "meedoen 是可分動詞",
     "我參加氣候週。→ ___", instr="翻譯", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "詞彙配對",
            ["het klimaat", "meedoen", "de waarschuwing", "vastzetten"],
            ["een bericht over gevaarlijk weer",
             "deelnemen, erbij zijn",
             "het weer en de natuur over een lange tijd",
             "losse spullen stevig maken"],
            ["c", "b", "a", "d"],
            ["klimaat=氣候 c", "meedoen=參加 b", "waarschuwing=預警 a", "vastzetten=固定好 d"],
            instr="把詞和釋義配對")
f.head("G　DIALOOG BIJ DE BOMEN", 21, OLIVE, 5)
f.ex("B1", "完形單選", "A", "boom = 樹",
     "— Goedemiddag! Ik kom voor een ___. (A. boom · B. fiets)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "struik = 灌木",
     "— Natuurlijk. Wilt u een boom of een ___? (A. struik · B. auto)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "planten = 種",
     "— Een struik, graag. En waar moet ik hem ___? (A. planten · B. kopen)", size=13.8, gap=0)
f.ex("B1", "完形單選", "B", "zachte = 柔軟的（土壤）",
     "— In de tuin, in de ___ grond. (A. harde · B. zachte)", size=13.8, gap=0)
f.ex("B1", "完形單選", "A", "發放到 16:00 結束",
     "— De uitdeling duurt tot ___ uur. (A. 16:00 · B. 20:00)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Maandag 2 november begint de Klimaatweek in Nederland. "
          "Ik doe mee: ik fiets elke dag naar school en ik zet de verwarming één graad lager. "
          "Op zaterdag 7 november ga ik met mijn vader naar Coevorden, want daar deelt de gemeente gratis bomen uit. "
          "Wij nemen een struik mee voor onze tuin. "
          "'s Avonds kijken wij op televisie naar de foto's van Museumnacht in Amsterdam. "
          "Zondag kijken wij naar Twente tegen Ajax. "
          "Mijn zus plant ook een boom op haar balkon. "
          "Wat een week voor het klimaat!")
NWORDS = len(MODELO.split())
f.expl(f"寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。")
f.ex("B1", "寫作", "（開放題，範文如下）", f"範文見本版 H 區（{NWORDS} 詞）",
     "«Jouw week in de Klimaatweek» Schrijf 80–100 woorden: wat doe jij in de Klimaatweek, plant jij iets, fiets jij, en kijk jij naar Museumnacht of voetbal?", instr="寫作", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　全部答案與簡析（第1–8版）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每題附一句中文簡析　帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 第{pg}版 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
