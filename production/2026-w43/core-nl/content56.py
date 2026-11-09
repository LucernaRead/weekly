# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · JONGEREN (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("JONGEREN　青年", "De Lucerna", "NIVEAU B1　ADE wordt 30, De Hanslers en Robinson　音乐节、真人秀与荒岛节目")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P5-main")
f.title("Dertig jaar dansen: ADE neemt Amsterdam over", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Amsterdam danst weer. Het Amsterdam Dance Event (ADE) is van woensdag 21 tot en met zondag 25 oktober in Amsterdam. Het festival wordt dertig jaar. Er komen meer dan 3.000 artiesten naar meer dan 200 locaties in de stad.")
f.para("De eerste namen kwamen al in juni: meer dan 250 artiesten, met onder anderen Armin van Buuren, Amelie Lens, Adam Beyer en Skepta. Na de tweede ronde zijn er meer dan 1.500 namen zeker. De krant NRC schreef op 19 oktober over dertig jaar ADE: feesten en netwerken horen bij elkaar op dit festival.")
f.para("Overdag is ADE meer dan dansen: er is ook een conferentie, waar dj's, makers en bedrijven praten over muziek en werk. Feesten én netwerken — precies zoals NRC het beschreef.")
f.para("Thuis op de bank is er ook spanning. De realityserie De Hanslers op SBS6 zorgt voor gesprekken in heel het land: de ruzie tussen Monique en Mike was dinsdag de meest gezochte zoekopdracht van Nederland, met meer dan 10.000 zoekopdrachten.")
f.para("En na ADE begint een ander avontuur: Expeditie Robinson. De 19 kandidaten zijn bekend — onder hen Maxime Meiland, Boaz Kok van de band Goldband en oud-shorttracker Sjinkie Knegt. Het programma begint op zondag 1 november om 20:00 uur op RTL 4.")
f.para("Het eilandprogramma is zwaar: de kandidaten slapen buiten, maken zelf vuur en zoeken hun eigen eten. Wie een proef verliest, kan naar huis worden gestemd; wie het langst blijft, wint. De kandidaten komen uit Nederland en Vlaanderen.")
f.box("ZO PLAN JE ADE　音乐节小贴士", [
    ("1. Kies twee of drie locaties per avond（每晚选两三个场地）", "serif", False, INK, 21, 1.36),
    ("2. Reis met de trein of de fiets（坐火车或骑车去）", "serif", False, INK, 21, 1.36),
    ("3. Drink water tussen het dansen door（跳舞间隙记得喝水）", "serif", False, INK, 21, 1.36),
    ("4. Spreek een plek af als je je vrienden kwijtraakt（约好走散集合点）", "serif", False, INK, 21, 1.36),
])
f.gloss("de artiest 艺人 · de locatie 场地 · de ruzie 争吵 · de kandidaat 参赛者 · het avontuur 冒险。")
f.end_report()

# col 3: image + facts + en jij (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 272)
cy3 = caption(p, ix, 472, CW, "Een boot in een Amsterdamse gracht. Tijdens ADE is de hele stad een podium: meer dan 200 locaties.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["Meer dan 3.000 artiesten op ADE, op meer dan 200 locaties.",
         "«de hanslers ruzie»: meer dan 10.000 zoekopdrachten op dinsdag.",
         "Expeditie Robinson: 19 kandidaten; start zondag 1 november, 20:00 uur."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "JONGEREN IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "En jij? Dans je graag, of kijk je liever naar een serie thuis? Schrijf twee zinnen in het Nederlands en stuur ze naar de redactie."
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("你喜欢跳舞，还是更爱在家看剧？写两句荷兰语寄来。", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f0eee5")
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "EN JIJ?　说说你自己", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "你喜欢跳舞，还是更爱在家看剧？写两句荷兰语寄来。", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　第5版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("读第 5 版文章，选出正确答案。")
e.ex("B1", "单选", "B", "ADE 从 10 月 21 日到 25 日",
     "ADE duurt van... A. 17 tot en met 25 oktober · B. 21 tot en met 25 oktober · C. 1 tot en met 5 november", size=20, gap=8)
e.ex("B1", "单选", "C", "艺人总数超过 3.000（250 只是第一批名单）",
     "Er komen meer dan ___ artiesten naar ADE. A. 250 · B. 1.500 · C. 3.000", size=20, gap=8)
e.ex("B1", "单选", "B", "周二最大的搜索是 Hanslers 争吵",
     "De meest gezochte zoekopdracht van dinsdag was... A. «ade» · B. «de hanslers ruzie» · C. «uitslagen»", size=20, gap=8)
e.ex("B1", "单选", "B", "Robinson 在 11 月 1 日周日开始",
     "Expeditie Robinson begint op... A. zondag 25 oktober · B. zondag 1 november · C. woensdag 21 oktober", size=20, gap=8)
e.ex("B1", "单选", "C", "Sjinkie Knegt 是前短道速滑选手",
     "Sjinkie Knegt was vroeger... A. een dj · B. een ontwerper · C. een shorttracker", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("用方框里的词填空。")
e.para("artiesten · locaties · ruzie · kandidaten · avontuur · netwerken", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "artiesten", "artiesten = 艺人（复数）",
     "Meer dan 3.000 ___ komen naar Amsterdam.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "locaties", "locaties = 场地（复数）",
     "Het festival heeft meer dan 200 ___ in de stad.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "ruzie", "ruzie = 争吵",
     "De ___ tussen Monique en Mike is groot nieuws.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "kandidaten", "kandidaten = 参赛者（复数）",
     "Expeditie Robinson heeft 19 ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "avontuur", "avontuur = 冒险（het）",
     "Robinson is een ___ op een eiland.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "netwerken", "netwerken = 社交、结识人脉",
     "Op ADE horen feesten en ___ bij elkaar.", instr="填空", size=20, gap=8)
e.head("C　DE TOEKOMST MET GAAN", 25)
e.bridge("用 gaan + 不定式说将来。")
e.ex("B1", "完成句子", "gaat beginnen", "gaat beginnen = 将要开始",
     "Expeditie Robinson ___ (beginnen) op 1 november.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaan dansen", "wij → gaan + 不定式 dansen",
     "Wij ___ (dansen) op ADE in Amsterdam.", instr="填空", size=20, gap=8)
e.ex("B2", "完成句子", "gaat winnen", "gaat winnen = 会赢（只是猜测）",
     "Wie ___ (winnen) Expeditie Robinson, denk je?", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "gaat kijken", "hij → gaat kijken",
     "Hij ___ (kijken) vanavond naar de serie.", instr="填空", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "判断对错", "Waar", "对：ADE 30 周年",
     "ADE wordt dit jaar dertig jaar. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Niet waar", "错：11 月 1 日才开始",
     "Expeditie Robinson begint op 25 oktober. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B2", "判断对错", "Waar", "对：超过 10.000 次搜索（周二快照）",
     "De zoekopdracht «de hanslers ruzie» had meer dan 10.000 zoekopdrachten. Waar of niet waar?", instr="判断", size=20, gap=8)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jongeren.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · VERDIEPING (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("VERDIEPING　深读", "De Lucerna", "NIVEAU B2　Waarom googelt Nederland de klok?　荷兰人为什么狂搜时钟")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P6-main")
f.title("Waarom googelt Nederland de klok?", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B2")
f.para("Twee keer per jaar stelt heel Nederland dezelfde vraag: gaat de klok vooruit of achteruit? Een onderzoek van Wristler, gepubliceerd op dinsdag 20 oktober, telt de zoekopdrachten van oktober vorig jaar. Het resultaat is verrassend: ongeveer 750.000 keer zochten Nederlanders naar de klokverandering.")
f.para("De twee grootste zoektermen waren «wintertijd» (301.000 keer) en «klok verzetten» (246.000 keer). Samen zijn dat 547.000 zoekopdrachten. De rest — ongeveer 203.000 — waren andere vragen en woorden over de klok.")
f.para("Het mooiste cijfer gaat over de richting. 60.500 mensen vroegen: «wanneer gaat de klok achteruit?» — het goede antwoord. Maar 6.600 mensen vroegen het omgekeerde: «wanneer gaat de klok vooruit?» Ruim negen keer zoveel mensen vragen het goed als fout.")
f.para("Nederland staat niet alleen. Van de 16 landen in het onderzoek zoekt alleen Italië per inwoner nog meer naar de klok. Nederlanders zijn dus kampioen twijfelen — op één land na.")
f.para("Waarom is het zo moeilijk? De regel lijkt simpel, maar het gevoel is anders. Het ezelsbruggetje helpt: in het voorjaar vooruit, in het najaar achteruit. En toch googelt iedereen het elk jaar opnieuw. Misschien is dat de echte traditie: niet de klok, maar de vraag.")
f.head("AFSCHAFFEN OF NIET?", 25)
f.para("Elk jaar komt ook de discussie terug: moeten we de klok nog wel verzetten? Sommigen willen één vaste tijd voor het hele jaar; anderen houden van het lange licht op zomeravonden. Een besluit is er niet — de klok gaat voorlopig twee keer per jaar heen en weer.")
f.para("En dus komt de vraag elk jaar twee keer terug: in oktober voor de wintertijd en in het voorjaar voor de zomertijd. En twee keer per jaar zoekt Nederland weer massaal naar hetzelfde antwoord.")
f.gloss("de zoekopdracht 搜索（词/次）· tellen 数、统计 · het omgekeerde 相反的 · per inwoner 人均 · twijfelen 犹豫、拿不准。")
f.end_report()

# col 3: chart with exactly proportional bars + pro/contra box (sequential, measured)
ix = COLX[3]
rows = [
    ("«wintertijd»", "301.000", 250),
    ("«klok verzetten»", "246.000", 204),
    ("«...klok achteruit?»", "60.500", 50),
    ("«...klok vooruit?»", "6.600", 5),
]
cap = "Zoekopdrachten in oktober vorig jaar. Bron: onderzoek van Wristler, gepubliceerd op 20 oktober 2026."
capcn = "来源：Wristler 研究，2026年10月20日发布；数据为去年10月的搜索次数"
ch = 62 + len(rows) * 58 + 14 + len(wrap(cap, "serif", False, 19, CW - 44)) * 27 + 6 + len(wrap(capcn, "sans", False, 18.5, CW - 44)) * 26 + 18
p.rect(ix, 200, CW, ch, fill=BOX)
yy3 = 216
p.text(ix + 22, yy3 + 26, "DE CIJFERS　数字图", 24, "sans", True, OLIVE)
yy3 += 58
for lab, val, bw in rows:
    p.text(ix + 22, yy3 + 20, lab, 19.5, "serif", True, INK)
    p.text(ix + CW - 22, yy3 + 20, val, 19.5, "sans", True, OLIVE, anchor="end")
    p.rect(ix + 22, yy3 + 30, bw, 18, fill=OLIVE)
    yy3 += 58
yy3 += 14
yy3 = p.para(ix + 22, yy3 + 19, cap, 19, "serif", False, GREY, CW - 44, 1.36)
yy3 = p.para(ix + 22, yy3 + 18.5, capcn, 18.5, "sans", False, GREY, CW - 44, 1.32) + 6
print("P6 chart ends", 200 + ch, "content to", yy3)
by6 = 200 + ch + 26
bt = [
    ("Stoppen met verzetten: één vaste tijd voor het hele jaar is rustiger voor lichaam en planning.", "serif", False, INK, 21, 1.4),
    ("Doorgaan: zo houden we de lange, lichte avonden in de zomer.", "serif", False, INK, 21, 1.4),
    ("De krant kiest niet: wij tellen alleen de zoekopdrachten. En jij?", "serif", False, INK, 21, 1.4),
]
bh = 62 + sum(len(wrap(t, "serif", False, 21, CW - 44)) * 29.5 + 8 for t, *_ in bt) + 16 + 30
p.rect(ix, by6, CW, bh, fill="#f0eee5")
yy3 = by6 + 16
p.text(ix + 22, yy3 + 26, "AFSCHAFFEN OF NIET?　废除还是保留", 21, "sans", True, OLIVE)
yy3 += 52
for t, k, b, fl, s, lh in bt:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21, "serif", False, INK, CW - 44, 1.4) + 8
print("P6 col3 ends", by6 + bh)

# ---- P6 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　第6版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A　LEES DE GRAFIEK", 25)
e.bridge("看第 6 版图表（Wristler 数据）回答。")
e.ex("B2", "完成句子", "301.000", "«wintertijd» 被搜 301.000 次（最多）",
     "De meest gezochte term was «wintertijd»: ___ keer.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "547.000", "301.000 + 246.000 = 547.000",
     "«wintertijd» en «klok verzetten» samen: ___ zoekopdrachten.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "203.000", "750.000 − 547.000 ≈ 203.000（约数）",
     "Van de ±750.000 zoekopdrachten waren er ongeveer ___ voor andere vragen.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "6.600", "只有 6.600 人问反了方向",
     "Slechts ___ mensen vroegen «vooruit» in plaats van «achteruit».", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "9", "60.500 ÷ 6.600 ≈ 9 倍多",
     "«Achteruit» is ruim ___ keer zo vaak gezocht als «vooruit».", instr="填空", size=21.5, gap=9)
e.ex("B2", "单选", "B", "统计的是去年 10 月的搜索",
     "Het onderzoek telt zoekopdrachten uit... A. oktober 2026 · B. oktober vorig jaar · C. de zomer van 2026", size=21.5, gap=9)
e.head("B　BEGRIJPEN", 25)
e.bridge("读第 6 版文章，选出正确答案。")
e.ex("B2", "单选", "B", "只有意大利人均搜索更多",
     "Alleen welk land zoekt per inwoner méér naar de klok? A. Duitsland · B. Italië · C. Frankrijk", size=21.5, gap=9)
e.ex("B2", "单选", "B", "研究覆盖 16 个国家",
     "Hoeveel landen deden mee aan het onderzoek? A. 10 · B. 16 · C. 27", size=21.5, gap=9)
e.ex("B2", "单选", "A", "方向难以记住，所以年年都搜",
     "Waarom googelen mensen de klok elk jaar weer? A. De richting is moeilijk te onthouden · B. De klok verandert nooit · C. Er is geen ezelsbruggetje", size=21.5, gap=9)
e.ex("B2", "单选", "B", "一部分人想要全年固定一个时间",
     "Wat wil een deel van de mensen? A. Twee keer per jaar verzetten, voor altijd · B. Eén vaste tijd voor het hele jaar · C. Nooit meer klokken", size=21.5, gap=9)
e.ex("B1", "单选", "B", "口诀：秋天拨回",
     "Het ezelsbruggetje zegt: in het najaar gaat de klok... A. vooruit · B. achteruit · C. niet", size=21.5, gap=9)
e.head("C　WOORDEN", 25)
e.bridge("用方框里的词填空。")
e.para("zoekopdracht · per inwoner · het omgekeerde · tellen", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B2", "完成句子", "zoekopdracht", "zoekopdracht = 搜索（词）",
     "«wintertijd» was de grootste ___ van oktober.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "per inwoner", "per inwoner = 人均",
     "Italië zoekt ___ nog meer dan Nederland.", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "het omgekeerde", "het omgekeerde = 相反的",
     "«Vooruit» is ___ van «achteruit».", instr="填空", size=21.5, gap=9)
e.ex("B2", "完成句子", "telt", "tellen：het onderzoek → telt",
     "Het onderzoek ___ (tellen) alle zoekopdrachten.", instr="填空", size=21.5, gap=9)
e.head("D　MAAK DE ZINNEN", 25)
e.bridge("把词组成正确的句子。")
e.ex("B2", "造句", "Nederlanders zoeken elk jaar naar de klok.", "动词 zoeken 第二位",
     "nederlanders / zoeken / elk jaar / naar de klok → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "Alleen Italië zoekt per inwoner meer.", "alleen + 国家名在前",
     "alleen Italië / zoekt / per inwoner / meer → ___", instr="造句", size=21.5, gap=9)
e.ex("B2", "造句", "De discussie komt elk jaar terug.", "terug 是可分前缀，回到句末",
     "de discussie / komt / elk jaar / terug → ___", instr="造句", size=21.5, gap=9)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-verdieping.svg")
print("P6 saved, exercises so far:", len(REG))
