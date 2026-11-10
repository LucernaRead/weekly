# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band("TOETS EN ANTWOORDEN　テストと解答", "De Lucerna", "8ページ　De grote toets van de week + alle antwoorden")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "気候週間は11月8日まで",
     "De Klimaatweek duurt van 2 tot en met ___ november. (A. 7 · B. 8)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "コーフェルデンは200本の木と低木を配布",
     "Coevorden deelt ___ bomen en struiken uit. (A. 100 · B. 200)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "ミュージアムナハトは11月7日",
     "Museumnacht is op zaterdag ___ november. (A. 6 · B. 7)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "トゥウェンテ–アヤックスは13:30開始",
     "Twente – Ajax begint om ___ uur. (A. 11:15 · B. 13:30)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "アヤックスはアタランタに2–0で勝利",
     "Ajax won van Atalanta met ___. (A. 2–0 · B. 4–1)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "ロビンソンは11月に開始",
     "Expeditie Robinson begon op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "オレンジ警報：危険な天気",
     "Code oranje betekent: het weer is ___. (A. veilig · B. gevaarlijk)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "meedoen = 参加する",
     "«Meedoen» betekent ___. (A. weggaan · B. deelnemen)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "選択問題", "A", "気候週間は11月2日（月）に開始",
     "De Klimaatweek begint op... A. maandag 2 november · B. dinsdag 3 november · C. zaterdag 7 november", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "配布場所はズウェーロー",
     "De bomen in Coevorden worden uitgedeeld in... A. Amsterdam · B. Zweeloo · C. Rotterdam", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "クロッシング・ボーダーはデン・ハーグで",
     "Crossing Border is in... A. Amsterdam · B. Den Haag · C. Utrecht", size=13.8, gap=0)
f.ex("B1", "選択問題", "A", "PAN は RAI で開催",
     "PAN Amsterdam is in... A. de RAI · B. het Rijksmuseum · C. de Jaarbeurs", size=13.8, gap=0)
f.ex("B1", "選択問題", "B", "レアル・ベティスはフェイエノールトに1–0で勝利",
     "Real Betis – Feyenoord eindigde... A. 0–0 · B. 1–0 · C. 0–1", size=13.8, gap=0)
f.ex("B1", "選択問題", "B", "10節後アヤックスは21点",
     "Na 10 ronden heeft Ajax ___ punten. A. 24 · B. 21 · C. 20", size=13.8, gap=0)
f.ex("B2", "選択問題", "B", "警報疲れ：警報が多すぎて注意しなくなる",
     "Waarschuwingsmoeheid betekent... A. moe van het weer · B. minder opletten door te veel waarschuwingen · C. een nieuwe code", size=13.8, gap=0)
f.ex("B1", "選択問題", "C", "ザーンダムの蚤の市は約250店",
     "De Snuffelmarkt in Zaandam heeft zo'n ___ kramen. A. 70 · B. 200 · C. 250", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Coevorden. Op zaterdag 7 november gaat hij naar de Fair Groen in Zweeloo en haalt hij een gratis struik op. 's Avonds kijkt hij naar de foto's van Museumnacht in Amsterdam — zelf gaat hij niet, want zondag speelt zijn club Twente tegen Ajax om 13:30 uur. En in de Klimaatweek fietst Daan elke dag naar school, ook als het regent.", 15, lh=1.3, split=False)
f.ex("A2", "選択問題", "B", "ダーンはコーフェルデン在住",
     "Waar woont Daan? A. in Zweeloo · B. in Coevorden · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "土曜日に無料の低木を受け取る",
     "Wat haalt Daan op zaterdag op? A. een fiets · B. een gratis struik · C. een kaartje", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "日曜日はトゥウェンテ対アヤックス",
     "Waarom gaat Daan zaterdagavond niet naar Amsterdam? A. Hij heeft geen kaartje · B. Zondag speelt Twente tegen Ajax · C. Hij houdt niet van musea", size=13.8, gap=0)
f.ex("B1", "選択問題", "B", "気候週間は毎日自転車で通学",
     "Wat doet Daan in de Klimaatweek? A. Hij rijdt elke dag met de auto · B. Hij fietst elke dag naar school · C. Hij blijft thuis", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "文を作る", "De Klimaatweek begint op maandag.", "主語 + 動詞 + 時間",
     "de klimaatweek / begint / op maandag → ___", instr="文を作る", size=13.8, gap=0)
f.ex("B1", "文を作る", "Wij planten een boom in de tuin.", "主語 + 動詞 + 目的語 + 場所",
     "wij / planten / een boom / in de tuin → ___", instr="文を作る", size=13.8, gap=0)
f.ex("B1", "文を作る", "Twente speelt zondag tegen Ajax.", "主語 + 動詞 + 時間 + 対戦相手",
     "twente / speelt / zondag / tegen ajax → ___", instr="文を作る", size=13.8, gap=0)
f.ex("B1", "文を作る", "Ik doe mee aan de Klimaatweek.", "分離動詞の mee は文末に",
     "ik / doe / mee / aan de klimaatweek → ___", instr="文を作る", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻訳", "気候週間は7日間続く。", "1ページの見出し参照",
     "De Klimaatweek duurt zeven dagen. → ___", instr="日本語に訳す", size=13.8, gap=0)
f.ex("B1", "翻訳", "オレンジ警報は「備えよ」という意味だ。", "2ページの原文 · bereid je voor 備えよ",
     "Code oranje betekent: bereid je voor. → ___", instr="日本語に訳す", size=13.8, gap=0)
f.ex("B1", "翻訳", "Museumnacht duurt van 19:00 uur tot 02:00 uur.", "時間の表現 van...tot... に注意",
     "ミュージアムナハトは19時から深夜2時までです。→ ___", instr="オランダ語に訳す", size=13.8, gap=0)
f.ex("B2", "翻訳", "Ik doe mee aan de Klimaatweek.", "meedoen は分離動詞",
     "私は気候週間に参加する。→ ___", instr="オランダ語に訳す", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "単語のペア",
            ["het klimaat", "meedoen", "de waarschuwing", "vastzetten"],
            ["een bericht over gevaarlijk weer",
             "deelnemen, erbij zijn",
             "het weer en de natuur over een lange tijd",
             "losse spullen stevig maken"],
            ["c", "b", "a", "d"],
            ["klimaat=気候 c", "meedoen=参加する b", "waarschuwing=警報 a", "vastzetten=固定する d"],
            instr="語と意味を結ぶ")
f.head("G　DIALOOG BIJ DE BOMEN", 21, OLIVE, 5)
f.ex("B1", "穴埋め選択", "A", "boom = 木",
     "— Goedemiddag! Ik kom voor een ___. (A. boom · B. fiets)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "struik = 低木",
     "— Natuurlijk. Wilt u een boom of een ___? (A. struik · B. auto)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "planten = 植える",
     "— Een struik, graag. En waar moet ik hem ___? (A. planten · B. kopen)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "zachte = 柔らかい（土）",
     "— In de tuin, in de ___ grond. (A. harde · B. zachte)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "配布は16:00まで",
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
f.expl(f"作文問題（正解は一つではない）；模範文（{NWORDS}語）は下記。")
f.ex("B1", "作文", "（自由記述 — 模範文は以下）", f"模範文はこのページの H 欄（{NWORDS}語）",
     "«Jouw week in de Klimaatweek» Schrijf 80–100 woorden: wat doe jij in de Klimaatweek, plant jij iets, fiets jij, en kijk jij naar Museumnacht of voetbal?", instr="作文", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　全解答と解説（1–8ページ）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "各問に日本語の解説つき　✓ は模範文のある問題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— {pg}ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "作文":
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
