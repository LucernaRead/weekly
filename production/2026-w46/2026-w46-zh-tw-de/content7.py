# -*- coding: utf-8 -*-
# W46 zh-tw core, VOL.3: P7 language focus.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-zh-tw-de/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P7 · language focus
CURPAGE[0] = 7
p = BSPage4()
p.band("語言 · Sprachfokus", "Lucerna", "語言聚焦 · 三個級別,三個主題 · Drei Stufen, drei Themen")

# ---- A2 column ----
a = Flow(p, [(COLX[0], CW)], 200, 1560, tag="P7-a2")
a.head("A2 · 雙11的話 · Double-11-Wörter", 24)
a.para("Double 11 gibt dir vier nützliche Wörter: 清單 (Einkaufsliste), 實付金額 (der Endbetrag, den du zahlst), 領券 (Gutscheine beanspruchen) und 鑑賞期 (die Bedenkzeit). Lerne sie einmal, und jeder Sale ergibt Sinn.", 21.5)
a.glossline("Vier Double-11-Wörter: 清單, 實付金額, 領券, 鑑賞期.")
a.para("清單 ist die Liste, die du vor dem Einkaufen schreibst. 實付金額 ist das, was du nach den Rabatten wirklich zahlst. 領券 heißt, einen Gutschein zu beanspruchen, bevor er ausgeht. 鑑賞期 sind die 7 Tage nach der Lieferung, in denen du die meisten Waren zurückgeben kannst.", 21.5)
a.ex("A2", "完成句子", "清單", "Eine Einkaufsliste ist eine 清單.",
     "買東西之前,先列___。", instr="Lückentext", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Die Bedenkzeit beträgt 7 Tage.",
     "鑑賞期是幾天?", opts=["A. 7天", "B. 3天", "C. 14天"], size=20.5, gap=10)
a.ex("A2", "完成句子", "實付金額", "Vergleiche den Endbetrag, den du wirklich zahlst.",
     "比價要比___。", instr="Lückentext", size=20.5, gap=10)
a.ex("A2", "單選", "A", "Beanspruche Gutscheine, bevor sie ausgehen.",
     "優惠券要怎麼拿?", opts=["A. 先領,領完就沒有了", "B. 不用領", "C. 過期再領"], size=20.5, gap=10)
a.para("Übe: 「我的購物清單是什麼？」 („Was steht auf meiner Einkaufsliste?“) — schreibe sie zuerst, dann vergleiche die Preise.", 21.5)
a.end_report()

# ---- B1 column ----
b = Flow(p, [(COLX[1], CW)], 200, 1560, tag="P7-b1")
b.head("B1 · 影展與鋼雕 · Film und Stahl", 24)
b.para("Film und Stahl teilen sich die Schlagzeilen dieser Woche. Gruppiere die Wörter, und sie bleiben haften: Film （入圍、頒獎、星光大道） und Stahl （鋼雕、保險箱、勞動記憶）.", 21.5)
b.glossline("Gruppiere die Wörter: Film (入圍/頒獎), Stahl (鋼雕/保險箱).")
b.para("入圍 heißt nominiert sein; 頒獎 heißt Preise verleihen. 星光大道 ist der rote Teppich vor der Zeremonie. 鋼雕 ist Skulptur aus Stahl; 保險箱 ist der Safe, der Kaohsiungs Arbeitserinnerungen bewahrt.", 21.5)
b.ex("B1", "完成句子", "入圍", "Nominiert sein heißt 入圍.",
     "被選進最後的得獎名單,叫___。", instr="Lückentext", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Die Zeremonie beginnt um 18:30 Uhr am 22. Nov.",
     "金馬獎頒獎典禮幾點開始?", opts=["A. 晚上6點30分", "B. 下午2點", "C. 上午10點"], size=20.5, gap=10)
b.ex("B1", "完成句子", "鋼雕", "Skulptur aus Stahl heißt 鋼雕.",
     "用鋼鐵做的藝術,叫___。", instr="Lückentext", size=20.5, gap=10)
b.ex("B1", "單選", "A", "Das Stahlfestival endet am 22. Nov.",
     "鋼雕藝術節展到哪天?", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=20.5, gap=10)
b.para("Merktipp: Lerne zuerst 入圍 — dann die Zeremonie （頒獎）, dann den Ort, an dem sie stattfindet （星光大道）.", 21.5)
b.end_report()

# ---- B2 column ----
c = Flow(p, [(COLX[2], CW)], 200, 1560, tag="P7-b2")
c.head("B2 · 港台說法 · Lokale Wörter", 24)
c.para("Taiwan und Hongkong haben jeweils ihre eigene Art, Dinge zu sagen. Diese Woche: 打卡 (mit einem Foto einchecken), 集點 (Punkte sammeln), 遊行 (Straßenparade) und 感謝祭 (Dankesfest für Fans).", 21.5)
c.glossline("Vier lokale Wörter aus dieser Ausgabe: 打卡, 集點, 遊行, 感謝祭.")
c.para("打卡 auf einer Messe heißt, ein Foto zu posten, um zu sagen: „Ich war hier“. 集點 heißt, bei jedem Sport Punkte zu verdienen. 遊行 ist der Festzug durch die Straßen; 感謝祭 ist das Dankesfest des Teams für seine Fans.", 21.5)
c.ex("B2", "單選", "A", "集點 heißt Punkte sammeln beim Sport.",
     "「集點」是什麼意思?", opts=["A. 每次運動累積點數", "B. 買門票", "C. 上班簽到"], size=20.5, gap=10)
c.ex("B2", "完成句子", "遊行", "Ein Festzug heißt 遊行.",
     "大家走上街頭慶祝,叫___。", instr="Lückentext", size=20.5, gap=10)
c.ex("B2", "單選", "A", "感謝祭 dankt den Fans.",
     "「感謝祭」是謝謝誰的活動?", opts=["A. 球迷", "B. 店員", "C. 記者"], size=20.5, gap=10)
c.ex("B2", "完成句子", "打卡", "Mit einem Foto einchecken heißt 打卡.",
     "在嘉年華拍照分享,叫___。", instr="Lückentext", size=20.5, gap=10)
c.para("Du brauchst nicht viele lokale Redewendungen — lerne vier, und jeder Ausflug fühlt sich näher an.", 21.5)
c.end_report()

# ---- col 3: error clinic + frame + letters ----
bx = COLX[3]
errs = [
    ("「旅展在11月9日開幕」", "→「旅展在11月9日落幕,開幕是11月6日」", "Messe: 6. Nov. auf, 9. Nov. zu. Zeitrichtung prüfen."),
    ("「金馬獎11月15日頒獎」", "→「金馬獎11月22日頒獎,11月15日是嘉年華」", "Zeremonie: 22. Nov.; Karneval: 15. Nov. (2. Tag)."),
    ("「滿5,000折800,實付5,800元」", "→「滿5,000折800,實付4,200元」", "Rabatte abziehen: 5.000 − 800 = 4.200."),
]
eh = 74 + sum(72 + len(wrap(r[0], "serif", True, 21.5, CW - 44)) * 29.24 + len(wrap(r[1], "serif", False, 20.5, CW - 44)) * 27.88 + len(wrap(r[2], "sans", False, 19.5, CW - 44)) * 26.52 for r in errs)
p.rect(bx, 200, CW, eh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = 216
p.text(bx + 22, yy3 + 26, "易錯診所 · Fehlerklinik", 23, "sans", True, OLIVE)
yy3 += 54
for wrong, right, en in errs:
    yy3 = p.para(bx + 22, yy3 + 21, wrong, 21.5, "serif", True, BRICK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 21, right, 20.5, "serif", False, INK, CW - 44, 1.36)
    yy3 = p.para(bx + 22, yy3 + 20, en, 19.5, "sans", False, GREY, CW - 44, 1.36) + 10
wy = 200 + eh + 12
wt = "「雙11不但有折扣,而且有免運。」 — 不但…而且… heißt: nicht nur X, sondern auch Y. Bilde selbst: 旅展不但有攤位,而且有表演 (nicht nur Stände, sondern auch Shows)."
wcn = "Struktur: 不但…而且… — nicht nur X, sondern auch Y."
wh = 62 + len(wrap(wt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(wcn, "sans", False, 20, CW - 44)) * 29 + 28
p.rect(bx, wy, CW, wh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = wy + 16
p.text(bx + 22, yy3 + 26, "本週句式 · Satzmuster", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, wt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, wcn, 20, "sans", False, GREY, CW - 44, 1.42)
ly = wy + wh + 12
lt = "「編輯好:雙11我的包裹到了!我買了一本書和一件外套,都沒有超過預算。週末我想去銅鑼灣看夜光巡遊,還想去高雄看鋼雕。——台北小讀者(編輯範例)」"
lcn = "Beispielbrief der Redaktion — kein echter Brief. VOL.2 versprach echte Leserbriefe und beste Seite-8-Texte ab dieser Ausgabe; keiner kam bis Redaktionsschluss an. Das Beispiel bleibt, die Einladung auch."
lt2 = "延期披露:VOL.2曾預告本期起刊登真實讀者來信和第8版最佳作文;截至截稿,本報未收到可刊登的真實來信與投稿,因此本期仍刊登編輯範例,並繼續公開徵集。你的來信,下一期見。"
lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lt2, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 40
p.rect(bx, ly, CW, lh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = ly + 16
p.text(bx + 22, yy3 + 26, "讀者園地 · Leserecke", 23, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(bx + 22, yy3 + 21, lt, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
yy3 = p.para(bx + 22, yy3 + 21, lt2, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(bx + 22, yy3 + 20, lcn, 20, "sans", False, GREY, CW - 44, 1.42)
col3_end = ly + lh
print("P7 col3 ends", col3_end)

# ---- phrases of the week (verbatim from this issue) ----
fy = max(1712, col3_end + 44)
p.hline(MX, RIGHT, fy - 14, GOLD, 2)
p.text(MX, fy + 24, "本週金句 · Sätze der Woche — wörtlich aus den Artikeln dieser Ausgabe", 27, "sans", True, OLIVE)
quotes = [
    ("「先列清單,再比價,最後才結帳」", "Erst Liste schreiben, Preise vergleichen, dann zahlen.", "S. 1"),
    ("「旅展四天,一次看完123個國家及城市」", "Vier Messetage, 123 Länder und Städte auf einmal.", "S. 1"),
    ("「早晚溫差大,外套要隨身帶」", "Große Tag-Nacht-Temperaturunterschiede — behalte eine Jacke bei dir.", "S. 2"),
    ("「金馬影展,就是一年一度的大電影課」", "Das Golden-Horse-Festival ist ein großer Filmkurs pro Jahr.", "S. 3"),
    ("「保險箱裡,裝的是高雄的勞動記憶」", "Im Safe: Kaohsiungs Arbeitserinnerungen.", "S. 3"),
    ("「穿上紅色衣服,一起上街為龍隊喝采」", "Trage Rot, gehe auf die Straße, feuere die Dragons an.", "S. 4"),
    ("「嘉年華不用門票,全家人都能來玩」", "Keine Karte nötig — die ganze Familie kann kommen und spielen.", "S. 5"),
    ("「回饋不是折價,實付金額才是真的」", "Cashback ist kein Rabatt — der gezahlte Betrag zählt.", "S. 6"),
]
colw = (RIGHT - MX - GUT) // 2
for i, (q, en, pg) in enumerate(quotes):
    cx = MX + (i // 4) * (colw + GUT)
    cyq = fy + 66 + (i % 4) * 138
    yyq = p.para(cx, cyq + 21, q, 21.5, "serif", False, INK, colw, 1.38)
    p.para(cx, yyq + 20, en + " (" + pg + ")", 19.5, "sans", False, GREY, colw, 1.35)

# ---- next week ----
py = fy + 66 + 4 * 138 + 18
p.rect(MX, py, RIGHT - MX, 118, fill=DARK)
p.text(MX + 28, py + 44, "下期預告 · Nächste Woche (VOL.4)", 24, "sans", True, "#e8dfc8")
p.para(MX + 28, py + 84, "下週日11月22日,三件大事同一天:封王遊行下午2點、金馬獎晚上6點30分、鋼雕藝術節閉幕,還有小雪、你們的來信和第8版最佳作文。下週見!", 21, "serif", False, "#f3edda", RIGHT - MX - 56, 1.36)
print("P7 teaser ends", py + 118)
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
