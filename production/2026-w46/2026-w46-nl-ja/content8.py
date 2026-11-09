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
f.ex("B1", "穴埋め選択", "B", "シンタクラース・ニュースは11月9日に始まる",
     "Het Sinterklaasjournaal begint op 9 ___. (A. oktober · B. november)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "全国到着はグラーフェ",
     "De landelijke intocht is in ___. (A. Amsterdam · B. Grave)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "アムステルダム到着は第88回",
     "De intocht in Amsterdam is de ___ editie. (A. 26e · B. 88e)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "オランダ対ギリシャ、20:45キックオフ",
     "Oranje – Griekenland begint om ___ uur. (A. 18:00 · B. 20:45)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "A", "聖マルティン祭は11月11日",
     "Sint-Maarten is op 11 ___. (A. november · B. december)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "ロビンソンはRTL 4で放送される",
     "Expeditie Robinson is te zien op ___. (A. NPO 3 · B. RTL 4)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "聖マルティン祭は分け合いの祭り",
     "Sint-Maarten is het feest van het ___. (A. griezelen · B. delen)", size=13.8, gap=0)
f.ex("B1", "穴埋め選択", "B", "schoen zetten = 靴を出す",
     "«De schoen zetten» betekent ___. (A. schoenen kopen · B. je schoen neerzetten)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", "選択問題", "A", "シンタクラース・ニュースは毎日18:00に放送される",
     "Het Sinterklaasjournaal is elke dag om... A. 18:00 uur · B. 12:00 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "グラーフェはマース川沿いにある",
     "Grave ligt aan... A. de Amstel · B. de Maas · C. de Rijn", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "シンタクラースは海事博物館で市の鍵を受け取る",
     "In Amsterdam krijgt Sinterklaas de sleutel bij... A. de Stopera · B. het Scheepvaartmuseum · C. het Leidseplein", size=13.8, gap=0)
f.ex("B1", "選択問題", "A", "『Het diner』は2009年に出版された",
     "Het diner van Herman Koch is uit... A. 2009 · B. 2026 · C. 2017", size=13.8, gap=0)
f.ex("B1", "選択問題", "B", "オランダとギリシャはともに勝ち点8",
     "Na vier wedstrijden hebben Nederland en Griekenland ___ punten. A. 5 · B. 8 · C. 0", size=13.8, gap=0)
f.ex("B1", "選択問題", "B", "ドイツ対オランダ、月曜、ベルリン",
     "Duitsland – Nederland is op maandag in... A. Amsterdam · B. Berlijn · C. Zeist", size=13.8, gap=0)
f.ex("B2", "選択問題", "B", "伝統は、人々が祝い続けると生き続ける",
     "Een traditie leeft als... A. ze oud is · B. mensen haar blijven vieren · C. ze op televisie is", size=13.8, gap=0)
f.ex("B1", "選択問題", "C", "パッケスアーフォントは12月5日（土）",
     "Pakjesavond is op... A. 11 november · B. 14 november · C. 5 december", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht. Op woensdag 11 november loopt zij met een lampion mee in de Sint Maarten Parade en zingt zij bij elke deur. Elke dag kijkt zij om 18:00 uur naar het Sinterklaasjournaal. Zaterdag kijkt zij op televisie naar de intocht in Grave. Zondag zet zij haar schoen met een wortel en een verlanglijstje. Vrijdag kijkt zij naar Oranje tegen Griekenland.", 15, lh=1.3, split=False)
f.ex("A2", "選択問題", "B", "サンネはユトレヒトに住んでいる",
     "Waar woont Sanne? A. in Grave · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "水曜日、彼女は聖マルティンのパレードに参加する",
     "Wat doet Sanne op woensdag 11 november? A. Ze kijkt naar Oranje · B. Ze loopt mee in de Sint Maarten Parade · C. Ze leest Het diner", size=13.8, gap=0)
f.ex("A2", "選択問題", "B", "彼女は靴にニンジンと願い事リストを入れる",
     "Wat zit er in de schoen van Sanne? A. een boek · B. een wortel en een verlanglijstje · C. een lampion", size=13.8, gap=0)
f.ex("B1", "選択問題", "B", "彼女は毎日18:00にシンタクラース・ニュースを見る",
     "Wanneer kijkt Sanne naar het Sinterklaasjournaal? A. om 12:00 uur · B. om 18:00 uur · C. om 20:00 uur", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", "文を作る", "Het Sinterklaasjournaal begint op maandag.", "主語＋動詞＋時間",
     "het sinterklaasjournaal / begint / op maandag → ___", instr="文を作る", size=13.8, gap=0)
f.ex("B1", "文を作る", "Wij zetten onze schoen bij de deur.", "主語＋動詞＋目的語＋場所",
     "wij / zetten / onze schoen / bij de deur → ___", instr="文を作る", size=13.8, gap=0)
f.ex("B1", "文を作る", "Oranje speelt vrijdag tegen Griekenland.", "主語＋動詞＋時間＋相手",
     "oranje / speelt / vrijdag / tegen griekenland → ___", instr="文を作る", size=13.8, gap=0)
f.ex("B1", "文を作る", "Ik loop met een lampion langs de deuren.", "主語＋動詞＋様態＋場所",
     "ik / loop / met een lampion / langs de deuren → ___", instr="文を作る", size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", "翻訳", "シンタクラース・ニュースは毎日18:00に放送される。", "3ページの記事と比べよう",
     "Het Sinterklaasjournaal is elke dag om 18:00 uur te zien. → ___", instr="日本語に訳す", size=13.8, gap=0)
f.ex("B1", "翻訳", "聖マルティン祭は分け合いの祭り。", "2ページの原文 · delen = 分け合う",
     "Sint-Maarten is het feest van het delen. → ___", instr="日本語に訳す", size=13.8, gap=0)
f.ex("B1", "翻訳", "De intocht in Amsterdam is de 88e editie.", "序数88eに注意",
     "アムステルダム到着は第88回。→ ___", instr="オランダ語に訳す", size=13.8, gap=0)
f.ex("B2", "翻訳", "Ik zet mijn schoen met een verlanglijstje.", "schoen zettenは決まり文句",
     "靴を出す、中に願い事リストを入れて。→ ___", instr="オランダ語に訳す", size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", "対応付け",
            ["het journaal", "de intocht", "de lampion", "delen"],
            ["een papieren lichtje voor 11 november",
             "een dagelijks nieuwsprogramma op televisie",
             "licht en eten geven aan anderen",
             "de feestelijke aankomst van Sinterklaas"],
            ["b", "d", "a", "c"],
            ["journaal = ニュース番組 b", "intocht = 祝祭の到着 d", "lampion = ランタン a", "delen = 分け合う c"],
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
f.expl(f"作文問題（正解は一つではない）；模範文（{NWORDS}語）は下記。")
f.ex("B1", "作文", "（自由課題、模範文は下記）", f"模範文はHセクション参照（{NWORDS}語）",
     "«Mijn week met Sinterklaas» Schrijf 80–100 woorden: wat doe jij deze week, loop jij met een lampion, kijk jij naar het Sinterklaasjournaal, en zet jij je schoen?", instr="作文", size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ANTWOORDEN　解答一覧 — ページごとに探そう", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "すべての答えに日本語の短い解説つき　✓は作文問題", 19.5, "sans", False, GREY, anchor="end")
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
