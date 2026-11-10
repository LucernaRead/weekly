# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · TAAL (A2/B1/B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("TAAL　言語", "De Lucerna", "言語に注目　Drie niveaus, drie gereedschappen　3レベル、3つの道具")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2　KLIMAATWOORDEN", 24)
a.para("De woorden van deze week horen bij de Klimaatweek: het klimaat, de boom planten, besparen en de waarschuwing. Het klimaat is het weer en de natuur over een lange tijd — niet het weer van vandaag.", 21.5)
a.para("En de codes: geel is let op, oranje is gevaarlijk, rood is blijf binnen. Onthoud ook: een waarschuwing geldt voor jouw eigen omgeving.", 21.5)
a.expl("het klimaat 気候（長期）；een boom planten 植樹；besparen 節約する；de waarschuwing 警報。")
a.ex("A2", "文の完成", "planten", "wij → planten",
     "In de Klimaatweek ___ (planten) wij een boom.", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "文の完成", "bespaar", "je → bespaar",
     "Met de fiets ___ (besparen) je energie.", instr="空所補充", size=20.5, gap=10)
a.ex("A2", "選択問題", "B", "気候とは長期的な天気と自然のこと",
     "«Het klimaat» is... A. het weer van vandaag · B. het weer en de natuur over een lange tijd · C. een museum", size=20.5, gap=10)
a.ex("A2", "文の完成", "blijf", "rood = 屋内にいよう",
     "Code rood betekent: ___ binnen.", instr="空所補充", size=20.5, gap=10)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1　SCHEIDBARE WERKWOORDEN", 24)
b.para("Deze week doen we iets met scheidbare werkwoorden: meedoen (deed mee, meegedaan), opruimen (ruimde op, opgeruimd) en vastzetten (zette vast, vastgezet). Het eerste deel gaat in de zin naar het einde.", 21.5)
b.para("Voorbeeld: «Ik doe mee aan de Klimaatweek.» «Wij hebben de tuin opgeruimd.» «Zij zette de losse spullen vast.» Let op de volgorde: het deel staat achteraan.", 21.5)
b.expl("meedoen 参加する：ik doe mee；opruimen 片付ける：wij hebben opgeruimd；vastzetten 固定する：zij zette vast。")
b.ex("B1", "文の完成", "doe mee", "ik → doe mee",
     "Ik ___ (meedoen) aan de Klimaatweek.", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "文の完成", "opgeruimd", "opruimen の過去分詞：opgeruimd",
     "Wij hebben de tuin ___ (opruimen).", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "文の完成", "zette vast", "vastzetten の過去形：zette vast",
     "Zij ___ (vastzetten) de losse spullen.", instr="空所補充", size=20.5, gap=10)
b.ex("B1", "選択問題", "B", "meedoen = 参加する",
     "«Meedoen» betekent... A. meekijken · B. deelnemen, erbij zijn · C. weggaan", size=20.5, gap=10)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2　EEN MENING GEVEN", 24)
c.para("Over het klimaat heeft iedereen een mening. Beleefd geef je die zo: «Ik vind dat ...», «Volgens mij ...» of «Het lijkt me dat ...» Zo praat je mee over de Klimaatweek én over de codes van het KNMI.", 21.5)
c.para("Voorbeeld: «Volgens mij moet iedereen meedoen.» «Het lijkt me dat lokaal waarschuwen beter is.» Een mening is geen feit — zeg er dus bij dat het jouw mening is.", 21.5)
c.expl("Ik vind dat… ～だと思う；Volgens mij… 私見では；Het lijkt me dat… 私には～のように思える。")
c.ex("B2", "文の完成", "Volgens", "Volgens mij… = 私見では",
     "___ mij moet iedereen meedoen aan de Klimaatweek.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "選択問題", "B", "Ik vind dat… は意見を表す",
     "«Ik vind dat iedereen moet meedoen» is... A. een bevel · B. een mening · C. een vraag", size=20.5, gap=10)
c.ex("B2", "文の完成", "lijkt", "Het lijkt me dat… = 私には～のように思える",
     "Het ___ me dat lokaal waarschuwen beter is.", instr="空所補充", size=20.5, gap=10)
c.ex("B2", "文の完成", "mij", "Volgens mij… = 私見では",
     "Volgens ___ is fietsen beter dan autorijden.", instr="空所補充", size=20.5, gap=10)
c.end_report()

# ---- col 3: pas op + het woord + brieven ----
bx = COLX[3]
errs = [
    ("«Het klimaat is slecht weer.»", "→ Fout: het klimaat is het weer over een lange tijd.", "気候とは長期的な天気と自然のことで、今日の天気ではない。"),
    ("«Ik doe mee aan de klimaatweek.»", "→ «Klimaatweek» krijgt een hoofdletter: het is een naam.", "Klimaatweek は固有名詞だから大文字。"),
    ("«Ik plant een bomen.»", "→ «Een» is enkelvoud: «een boom» of «bomen».", "een は単数、複数は bomen。"),
    ("«Omdat het regent, ik blijf thuis.»", "→ Na «omdat» staat het werkwoord op plaats 2: «... blijf ik thuis.»", "omdat の従属節の後では、主節の動詞は2番目：blijf ik thuis。"),
]
eh = 62 + sum((len(wrap(r[0], "serif", True, 21.5, CW - 44)) + len(wrap(r[1], "serif", False, 20.5, CW - 44)) + len(wrap(r[2], "sans", False, 19.5, CW - 44))) * 29.5 + 10 for r in errs) + 16 + 192
p.rect(bx, 200, CW, eh, fill=BOX)
yy3 = 216
p.text(bx + 22, yy3 + 26, "PAS OP!　間違いクリニック", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, cn in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, OLIVE, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, cn, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 8
wt = "«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("meedoen = 参加する：気候週間にはオランダ中が参加する。", "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f0eee5")
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "HET WOORD　今週の単語", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "meedoen = 参加する：気候週間にはオランダ中が参加する。", 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 8
lt = "«Hallo! Ik ben Li en ik leer Nederlands in Shanghai. In de Klimaatweek plant ik een boom op mijn balkon!» — Li (voorbeeldbrief van de redactie)"
# Fix-1 disclosure (independent proof Problem 2): on-page, Dutch + matching Japanese.
# No real letters/best P8 texts had arrived by press time, so the labeled example
# stands and the promise carries to VOL.3. Existing labeling/invitation kept verbatim.
dt_nl = "Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3."
dt_ja = "締切時に本物の手紙と8ページの優秀作文はなく、編集部の例文を掲載。約束はVOL.3へ。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(dt_nl, "serif", False, 21.5, CW - 44)) * 30.5 + 10 + len(wrap(dt_ja, "sans", False, 20, CW - 44)) * 29 + 10 + len(wrap("あなたの本物の手紙と8ページの優秀作文を送ってください。VOL.3に掲載します！", "sans", False, 20, CW - 44)) * 29 + 34 + 50
# +50 measured correction: rendered inter-paragraph spacing runs ~20px above the
# formula per added paragraph (verified on the rendered SVG: last baseline sat
# 21px below the box edge before this correction).
p.rect(bx, ly, CW, lh, fill=BOX)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "BRIEVEN VAN LEZERS", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, dt_nl, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 20, dt_ja, 20, "sans", False, GREY, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, "あなたの本物の手紙と8ページの優秀作文を送ってください。VOL.3に掲載します！", 20, "sans", False, GREY, CW - 44, 1.42)
print("P7 col3 ends", ly + lh)

# ---- zinnen van de week (verbatim from this issue) ----
# Fix-1 layout only: fy moved down for the taller BRIEVEN box; row pitch
# 158 -> 90 (rows have ~77px of content from quote top to Chinese descender,
# so 90px still leaves a clear gap); no quote text changed.
fy = 1951
p.hline(MX, RIGHT, fy - 14, OLIVE, 2)
p.text(MX, fy + 24, "ZINNEN VAN DE WEEK　今週の名文（本号の記事から逐語引用）", 27, "sans", True, OLIVE)
quotes = [
    ("«Van maandag 2 tot en met zondag 8 november is het Klimaatweek in Nederland»", "11月2日（月）から8日（日）まで、オランダは気候週間だ。", "Pagina 1"),
    ("«De herfst is de beste tijd om te planten»", "秋は植樹に最適の季節だ。", "Pagina 1"),
    ("«Geel betekent: let op, het weer kan gevaarlijk zijn»", "黄色は「注意、危険な天気になるおそれ」という意味だ。", "Pagina 2"),
    ("«Meer dan 70 musea zijn open van 19:00 uur 's avonds tot 02:00 uur 's nachts»", "70を超える美術館・博物館が夜19時から深夜2時まで開いている。", "Pagina 3"),
    ("«Ajax won donderdag 22 oktober met 2–0 van Atalanta»", "アヤックスは10月22日（木）にアタランタに2–0で勝った。", "Pagina 4"),
    ("«Zondag 1 november begon Expeditie Robinson op RTL 4, om 20:00 uur»", "11月1日（日）、『エクスペディティ・ロビンソン』がRTL 4で20時に始まった。", "Pagina 5"),
    ("«Een code is geen verbod, maar een advies»", "警報コードは禁止ではなく助言だ。", "Pagina 6"),
    ("«Het weer is van ons allemaal, maar het raakt ons allemaal anders»", "天気は私たちみんなのものだが、影響は人それぞれ違う。", "Pagina 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, cn, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 90
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, cn + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- volgende week ----
# Fix-1 layout only: py moved down (fy shift minus pitch saving); text unchanged.
py = 2439
p.rect(MX, py, RIGHT - MX, 118, fill=CLOTH)
p.text(MX + 28, py + 44, "VOLGENDE WEEK　来週の予告 (VOL.3)", 24, "sans", True, ONCLOTH)
p.para(MX + 28, py + 84, "Zondag 15 november komt Sinterklaas aan in Amsterdam. En woensdag 11 november is het Sint-Maarten: kinderen gaan met lampionnen langs de deuren. Verder: jullie brieven en de beste teksten van pagina 8. Tot maandag!", 21, "serif", False, "#cac8ba", RIGHT - MX - 56, 1.36)
p.foot(7)
p.save(f"{OUT}/p7-taal.svg")
print("P7 saved, exercises so far:", len(REG))
