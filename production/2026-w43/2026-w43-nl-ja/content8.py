# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · TOETS EN ANTWOORDEN =================
CURPAGE[0] = 8
p = BSPage4()
p.band('TOETS EN ANTWOORDEN　テストと解答', "De Lucerna", '8ページ　De grote toets van de week + alle antwoorden')

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　VUL DE KRONIEK IN", 21, OLIVE, 5)
f.ex("B1", '穴埋め選択', "B", '秋は時計を戻す',
     "In de nacht van zaterdag op zondag gaat de klok één uur ___. (A. vooruit · B. achteruit)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "A", '中部と南部の秋休みは10月25日まで',
     "De herfstvakantie van Midden en Zuid duurt tot en met zondag ___ oktober. (A. 25 · B. 18)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "A", 'デザインウィークはアイントホーフェン',
     "De Dutch Design Week is in ___. (A. Eindhoven · B. Amsterdam)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "B", 'PSV はアウェーでポルトに勝利',
     "PSV won in de Champions League bij ___. (A. Atalanta · B. FC Porto)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "B", 'ADE は今年30年',
     "ADE wordt dit jaar ___ jaar. (A. 25 · B. 30)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "A", 'Robinson は11月に開始',
     "Expeditie Robinson begint op 1 ___. (A. november · B. oktober)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "A", '最大の時計検索語は wintertijd',
     "De grootste zoekterm over de klok was «___». (A. wintertijd · B. klok vooruit)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "B", "half drie = 2:30",
     "«Half drie» is ___. (A. 03:30 · B. 02:30)", size=13.8, gap=0)
f.head("B　ALGEMENE VRAGEN", 21, OLIVE, 5)
f.ex("A2", '選択問題', "B", '冬時間は午前03:00に開始',
     "De wintertijd begint om... A. 02:00 uur · B. 03:00 uur · C. middernacht", size=13.8, gap=0)
f.ex("A2", '選択問題', "A", '北部地域は10月10–18日が休暇',
     "Welke regio had vakantie van 10 tot en met 18 oktober? A. Noord · B. Midden · C. Zuid", size=13.8, gap=0)
f.ex("A2", '選択問題', "C", '学生券 € 19,50',
     "Een studentenkaartje voor de DDW kost... A. € 32,50 · B. € 25,00 · C. € 19,50", size=13.8, gap=0)
f.ex("B1", '選択問題', "A", 'フェイエノールトは水曜にセビージャ',
     "Feyenoord speelt woensdag in... A. Sevilla · B. Porto · C. Eindhoven", size=13.8, gap=0)
f.ex("B1", '選択問題', "B", 'スパルタ–アヤックスは16:45開始',
     "Sparta – Ajax begint zondag om... A. 14:30 uur · B. 16:45 uur · C. 20:00 uur", size=13.8, gap=0)
f.ex("B1", '選択問題', "B", '19人の候補者はオランダ人とフラマン人',
     "De 19 kandidaten van Expeditie Robinson zijn... A. allemaal dj's · B. Nederlanders en Vlamingen · C. alleen sporters", size=13.8, gap=0)
f.ex("B2", '選択問題', "B", '6.600人は「進める」を検索（逆を聞いた）',
     "De 6.600 zoekopdrachten vroegen naar... A. achteruit · B. vooruit · C. wintertijd", size=13.8, gap=0)
f.ex("B1", '選択問題', "A", 'プラットフォームは今後、追加費用を全て明示',
     "Thuisbezorgd laat voortaan... A. alle extra kosten duidelijk zien · B. geen eten meer bezorgen · C. alleen kortingsbonnen zien", size=13.8, gap=0)
f.head("C　LEES EN ANTWOORD", 21, OLIVE, 5)
f.para("Sanne woont in Utrecht, in de regio Midden. Zij heeft de hele week herfstvakantie. Op woensdag gaat zij met haar zus naar Eindhoven, naar de Dutch Design Week. Zaterdagavond zet zij alle klokken in huis één uur achteruit — behalve haar telefoon, die doet het zelf. Zondag slaapt zij lang uit: het is de laatste dag van de vakantie.", 15, lh=1.3, split=False)
f.ex("A2", '選択問題', "B", 'Sanne はユトレヒト在住',
     "Waar woont Sanne? A. in Venlo · B. in Utrecht · C. in Amsterdam", size=13.8, gap=0)
f.ex("A2", '選択問題', "B", '彼女の地域は秋休み中',
     "Waarom heeft Sanne de hele week vrij? A. Zij is ziek · B. Het is herfstvakantie in haar regio · C. Zij werkt niet", size=13.8, gap=0)
f.ex("A2", '選択問題', "B", '彼女は土曜の夜に時計を直す',
     "Wat doet Sanne zaterdagavond? A. Zij gaat dansen · B. Zij zet de klokken achteruit · C. Zij pakt haar koffer", size=13.8, gap=0)
f.ex("B1", '選択問題', "C", 'スマホは自動で変わり、手で直さない',
     "Welke klok zet Sanne NIET met de hand achteruit? A. de ovenklok · B. de wekker · C. haar telefoon", size=13.8, gap=0)
f.head("D　MAAK DE ZINNEN", 21, OLIVE, 5)
f.ex("A2", '文を作る', "De klok gaat één uur achteruit.", '主語 + 動詞 + 目的語 + 方向',
     "de klok / gaat / één uur / achteruit → ___", instr='文を作る', size=13.8, gap=0)
f.ex("B1", '文を作る', "Wij gaan zondag naar de topper.", '主語 + 動詞 + 時刻 + 場所',
     "wij / gaan / zondag / naar de topper → ___", instr='文を作る', size=13.8, gap=0)
f.ex("B1", '文を作る', "Hoe laat begint de wedstrijd?", '疑問句は文頭',
     "hoe laat / begint / de wedstrijd / ? → ___", instr='文を作る', size=13.8, gap=0)
f.ex("B1", '文を作る', "PSV won met 1–0 in Porto.", '主語 + 動詞 + スコア + 場所',
     "psv / won / met 1–0 / in porto → ___", instr='文を作る', size=13.8, gap=0)
f.head("E　VERTAAL", 21, OLIVE, 5)
f.ex("A2", '翻訳', '日曜日は時計を戻す：1時間長く眠れる！', '1ページのトップ帯と対照',
     "Zondag gaat de klok terug: een uur langer slapen! → ___", instr='翻訳', size=13.8, gap=0)
f.ex("B1", '翻訳', 'あなたの電話とコンピュータは時刻を自分で変える。', '2ページの原文 · veranderen 変える',
     "Je telefoon en je computer veranderen de tijd zelf. → ___", instr='翻訳', size=13.8, gap=0)
f.ex("B1", '翻訳', "De Dutch Design Week is in Eindhoven.", '場所の句 in Eindhoven に注意',
     'オランダ・デザインウィークはアイントホーフェンで開かれる。→ ___', instr='翻訳', size=13.8, gap=0)
f.ex("B2", '翻訳', "Zondag heb ik een uur langer geslapen.", "perfectum：heb geslapen",
     '日曜日、私は1時間長く眠った。→ ___', instr='翻訳', size=13.8, gap=0)
f.head("F　WOORDEN VAN DE WEEK", 21, OLIVE, 5)
f.match_set("B2", '単語のペア',
            ["de klok verzetten", "het ezelsbruggetje", "eropuit gaan", "bijslapen"],
            ["extra slapen om uit te rusten",
             "het huis uit gaan voor iets leuks",
             "een hulpmiddel om iets te onthouden",
             "de tijd op een klok veranderen"],
            ["d", "c", "b", "a"],
            ['verzetten=時計を動かす d', 'ezelsbruggetje=語呂合わせ c', 'eropuit=お出かけ b', 'bijslapen=寝だめ a'],
            instr='語と意味を結ぶ')
f.head("G　DIALOOG BIJ DE DDW", 21, OLIVE, 5)
f.ex("B1", '穴埋め選択', "B", 'kaartje = チケット',
     "— Goedemorgen! Een ___ voor de Dutch Design Week, alstublieft. (A. ezelsbruggetje · B. kaartje)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "A", 'student = 学生（料金 € 19,50）',
     "— Natuurlijk. Bent u ___? Studenten betalen € 19,50. (A. student · B. ontwerper)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "B", 'tot hoe laat = 何時まで開いているか',
     "— Ja! Hier is mijn studentenkaart. En tot hoe ___ zijn jullie open? (A. lang · B. laat)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "A", 'veel plezier = 楽しんで',
     "— Tot 18:00 uur. Veel ___ met de ontwerpen! (A. plezier · B. slaap)", size=13.8, gap=0)
f.ex("B1", '穴埋め選択', "B", 'tot ziens = さようなら',
     "— Dank u wel, tot ___! (A. straks · B. ziens)", size=13.8, gap=0)
f.head("H　SCHRIJF ZELF", 21, OLIVE, 5)
MODELO = ("Zondag 25 oktober word ik laat wakker: het is de laatste dag van mijn herfstvakantie. "
          "Ik heb een uur langer geslapen, want vannacht ging de klok achteruit. "
          "Na het ontbijt ga ik met mijn vrienden naar het bos; de bladeren zijn geel en rood. "
          "'s Middags kijken wij thuis naar PSV tegen Feyenoord op televisie. "
          "Mijn zus gaat naar Amsterdam voor ADE, maar ik blijf liever thuis met een boek. "
          "'s Avonds pak ik mijn tas voor school: morgen begint het gewone leven weer. "
          "Wat een week!")
NWORDS = len(MODELO.split())
f.expl(f"作文問題（決まった答えはありません）。模範文（{NWORDS}語）は以下です。")
f.ex("B1", '作文', '（自由記述 — 模範文は以下）', f"模範文はこのページの H 欄（{NWORDS}語）",
     "«Jouw zondag 25 oktober» Schrijf 80–100 woorden: wat doe jij op de laatste vakantiedag, hoe laat sta jij op, en wat doe jij 's middags?", instr='作文', size=13.8, gap=0)
f.para("Tekstmodel: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= ANTWOORDEN =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, 'ANTWOORDEN　全解答と解説（1–8ページ）', 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, '各問に日本語の解説つき　✓ は模範文のある問題', 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— {pg}ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == '作文':
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
