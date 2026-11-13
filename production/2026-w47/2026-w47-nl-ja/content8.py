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
f.ex("B1", "穴埋め選択", "B", "ドイツ対オランダ、月曜、ベルリン",
     "Duitsland – Nederland is op maandag in ___. (A. Amsterdam · B. Berlijn)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "オランダとギリシャはともに勝ち点8",
     "Nederland en Griekenland hebben allebei ___ punten. (A. 5 · B. 8)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "オランダは7得点した",
     "Nederland maakte ___ doelpunten in vier wedstrijden. (A. 7 · B. 5)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "Pakjesavondは12月",
     "Pakjesavond is op ___ december. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "シンタクラース・ニュース 18:00",
     "Het Sinterklaasjournaal is elke dag om ___ uur. (A. 12:00 · B. 18:00)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "ロビンソンは RTL 4 で放送",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "サプライズには詩が入っている",
     "Bij een surprise hoort een ___. (A. liedje · B. gedicht)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "groepswinst = グループ優勝",
     "«De groepswinst» betekent ___. (A. de laatste plaats · B. de eerste plaats in de groep)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "選択問題", "A", "シンタクラース・ニュースは毎日18:00に放送される",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "グラーフェはマース川沿いにある",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "アムステルダム到着は第88回",
     "De intocht in Amsterdam was de... A. 26e editie · B. 88e editie · C. 30e editie", size=13.8, gap=0)
f.ex("B1", "選択問題", "A", "『Het diner』は2009年に出版された",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "選択問題", "B", "ドイツはホームでギリシャに0–1で敗れた",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=13.8, gap=0)
f.ex("B1", "選択問題", "B", "PSV は勝ち点26でエールディヴィジ首位",
     "PSV staat bovenaan in de Eredivisie met ___ punten. A. 25 · B. 26 · C. 8", size=13.8, gap=0)
f.ex("B2", "選択問題", "B", "伝統は、人々が祝い続けると生き続ける",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "選択問題", "C", "エールディヴィジ第13節は11月21～22日",
     "Speelronde 13 is op... A. 13 en 14 november · B. 16 november · C. 21 en 22 november", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Daan woont in Rotterdam. Op maandag 16 november kijkt hij om 20:45 uur naar Duitsland – Nederland in Berlijn. Elke dag kijkt hij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag 21 november kijkt hij naar NEC – PSV. Zondag zet hij zijn schoen met een wortel en een verlanglijstje. Op zondagavond kijkt hij ook naar Expeditie Robinson.", 15, lh=1.3, split=False)
f.ex("A2", "選択問題", "B", "ダーンはロッテルダムに住んでいる",
     "Waar woont Daan? A. in Grave · B. in Rotterdam · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "彼は月曜日にドイツ–オランダを見る",
     "Wat doet Daan op maandag 16 november? A. Hij kijkt naar Robinson · B. Hij kijkt naar Duitsland – Nederland · C. Hij leest Het diner", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "彼は靴にニンジンと願い事リストを入れる",
     "Wat zit er in de schoen van Daan? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "選択問題", "B", "彼は毎日18:00にシンタクラース・ニュースを見る",
     "Wanneer kijkt Daan naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "文を作る", "Het Sinterklaasjournaal begint om 18:00 uur.", "主語＋動詞＋時間",
     "het sinterklaasjournaal / begint / om 18:00 uur → ___", instr="文を作る", size=13.8, gap=0)
f.ex("B1", "文を作る", "Wij zetten onze schoen bij de deur.", "主語＋動詞＋目的語＋場所",
     "wij / zetten / onze schoen / bij de deur → ___", instr="文を作る", size=13.8, gap=0)
f.ex("B1", "文を作る", "Oranje speelt maandag in Berlijn.", "主語＋動詞＋時間＋場所",
     "oranje / speelt / maandag / in berlijn → ___", instr="文を作る", size=13.8, gap=0)
f.ex("B1", "文を作る", "Ik zet mijn schoen met een wortel.", "主語＋動詞＋目的語＋方法",
     "ik / zet / mijn schoen / met een wortel → ___", instr="文を作る", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻訳", "シンタクラース・ニュースは毎日18:00に放送される。", "3ページの記事と比べよう",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="日本語に訳す", size=13.8, gap=0)
f.ex("B1", "翻訳", "上位2チームが準々決勝に進む。", "4ページの原文 · kwartfinale = 準々決勝",
     "De nummers één en twee gaan naar de kwartfinales. → ___", instr="日本語に訳す", size=13.8, gap=0)
f.ex("B1", "翻訳", "De intocht in Amsterdam was de 88e editie.", "序数88eに注意",
     "アムステルダム到着は第88回。→ ___", instr="オランダ語に訳す", size=13.8, gap=0)
f.ex("B2", "翻訳", "Ik maak een surprise met een kort gedicht.", "surprise は決まった言い方",
     "小さな詩つきのサプライズを作ります。→ ___", instr="オランダ語に訳す", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "対応付け",
            ["het journaal", "de groepswinst", "de schoen", "het gedicht"],
            ["een klein versje bij een cadeau",
             "een dagelijks nieuwsprogramma op televisie",
             "de eerste plaats in de groep",
             "die staat 's avonds bij de deur"],
            ["b", "c", "d", "a"],
            ["journaal = ニュース番組 b", "groepswinst=グループ優勝 c", "schoen = 靴 d", "gedicht=詩 a"],
            instr="語と意味を結ぶ")
f.head("G　DIALOOG BIJ DE SCHOEN", 21, OLIVE, 5)
f.ex("B1", "穴埋め選択", "A", "schoen = 靴",
     "— Mama, waar moet mijn ___? (A. schoen · B. boek)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "wortel = ニンジン（馬のため）",
     "— Bij de deur, met een ___ voor het paard. (A. wortel · B. lampion)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "verlanglijstje = 願い事リスト",
     "— En mijn ___ erin? (A. verlanglijstje · B. journaal)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "cadeautje = 小さな贈り物",
     "— Ja. Sinterklaas brengt 's nachts een ___. (A. mantel · B. cadeautje)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "18:00 = シンタクラース・ニュースの時間",
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
f.bridge(f"作文問題（正解は一つではない）；模範文（{NWORDS}語）は下記。")
f.ex("B1", "作文", "(自由課題、モデル文は下)", f"H のモデル文を見てください（{NWORDS}語）",
     "«Mijn week met Oranje en Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, kijk jij naar Duitsland – Nederland, en zet jij je schoen?", instr="作文", size=13.8, gap=0)
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
p.text(MX, 1302, "ANTWOORDEN　解答 — ページごとに並んでいます：番号を探そう", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "答えにはどれも日本語の短い注がある　✓ は作文問題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PAGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
