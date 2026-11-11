# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTUUR (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTUUR　文化", "De Lucerna", "NIVEAU A2 → B1　Sinterklaas is er!　圣诞老人来了！")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1540, tag="P3-feature")
f.title("Sinterklaas is er: Grave, Amsterdam en het journaal", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: A2 → B1")
f.para("Op zaterdag 14 november kwam Sinterklaas officieel aan in Nederland. De landelijke intocht was dit jaar in Grave, een vestingstad aan de Maas in Noord-Brabant. Rond 12:00 uur meerde de stoomboot aan bij de Maaskade. Burgemeester Marieke Moorman ontving Sinterklaas. Het programma duurde van 12:00 tot 16:00 uur en was live te zien op NPO 3.")
f.para("Een dag later voer Sinterklaas in Amsterdam: de boot vertrok om 10:15 uur bij De Omval en voer over de Amstel naar het Scheepvaartmuseum, waar hij rond 11:30 uur aankwam. Daar kreeg hij de sleutel van de stad. Om 13:00 uur begon de stoet te paard bij de Stopera, via het Rembrandtplein en de Utrechtsestraat naar het Leidseplein. Het was de 88e editie van de Amsterdamse intocht.")
f.para("Het Sinterklaasjournaal is er elke dag om 18:00 uur op NPO Zapp. Presentatrice Merel Westrik vertelt hoe de voorbereidingen gaan: de schoen, de verlanglijstjes en — over negentien dagen — pakjesavond op zaterdag 5 december.")
f.para("November is ook de maand van Heel Nederland Leest: heel Nederland leest dit jaar Het diner van Herman Koch, uit 2009. Het boek is gratis af te halen in de bibliotheek, ook als je geen lid bent. Er is ook een grootletterboek, een Makkelijk Lezen-editie, een e-book en een luisterboek. In bibliotheken zijn er leeskringen — ook voor mensen die Nederlands leren.")
f.head("LEZEN EN KIJKEN", 25)
f.para("Twee dingen in november: 's avonds om 18:00 uur het Sinterklaasjournaal kijken, en overdag een boek lezen. Neem Het diner mee naar huis en praat erover met vrienden: samen lezen is leuker dan alleen lezen.")
f.para("En wie zijn schoen zet, kan er een verlanglijstje in doen — of een tekening. Sinterklaas leest alles.")
f.gloss("de vestingstad 要塞城市 · ontvangen 迎接 · de sleutel 钥匙 · de editie 届 · de leeskring 读书会。")
f.end_report()

# col 3: image + facts box (sequential, measured)
ix = COLX[3]
image(p, "gracht.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Een boot in een Amsterdamse gracht. Zondag voer de stoomboot van Sinterklaas over de Amstel naar het Scheepvaartmuseum.",
              "Foto: W. Punt / Anefo, Nationaal Archief — CC0")
facts = ["Landelijke intocht: zaterdag 14 november, Grave, Maaskade, vanaf 12:00 uur op tv.",
         "Amsterdam: zondag 15 november, boot 10:15 uur, stoet 13:00 uur, 88e editie.",
         "Sinterklaasjournaal: elke dag 18:00 uur, NPO Zapp, met Merel Westrik.",
         "Heel Nederland Leest: Het diner, gratis in de bibliotheek, heel november."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 64
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "SINTERKLAAS IN CIJFERS", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P3 col3 ends", sy3 + sh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　第3版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("读第 3 版文章，选出正确答案。")
e.ex("A2", "单选", "B", "全国入城式在赫拉弗",
     "De landelijke intocht was in... A. Amsterdam · B. Grave · C. Utrecht", size=20, gap=8)
e.ex("A2", "单选", "B", "船 12:00 左右在 Maaskade 靠岸",
     "De stoomboot meerde aan om... A. 18:00 uur · B. 12:00 uur · C. 20:45 uur", size=20, gap=8)
e.ex("A2", "单选", "C", "阿姆斯特丹的船 10:15 从 Omval 出发",
     "De boot in Amsterdam vertrok om... A. 12:00 uur · B. 13:00 uur · C. 10:15 uur", size=20, gap=8)
e.ex("A2", "单选", "A", "阿姆斯特丹入城式是第 88 届",
     "De intocht in Amsterdam was de... A. 88e editie · B. 26e editie · C. 30e editie", size=20, gap=8)
e.ex("A2", "单选", "B", "《晚餐》在图书馆免费领取",
     "Het diner is gratis af te halen in... A. de boekwinkel · B. de bibliotheek · C. het museum", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("用方框里的词填空。")
e.para("vestingstad · ontvangen · sleutel · editie · leeskring", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("A2", "完成句子", "vestingstad", "vestingstad = 要塞城市",
     "Grave is een oude ___ aan de Maas.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "ontving", "ontvangen 的过去时：ontving",
     "Burgemeester Moorman ___ Sinterklaas in Grave.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "sleutel", "sleutel = 钥匙",
     "Sinterklaas kreeg de ___ van de stad.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "editie", "editie = 届",
     "Het was de 88e ___ van de Amsterdamse intocht.", instr="填空", size=20, gap=8)
e.ex("A2", "完成句子", "leeskring", "leeskring = 读书会",
     "In de bibliotheek is er een ___ over Het diner.", instr="填空", size=20, gap=8)
e.head("C　HET PERFECTUM", 25)
e.bridge("用现在完成时补全，注意助动词 hebben/zijn。", w=CW - 40)  # fix3 D6: 窄 40px 使句末 。 回上一行（原断行 。 独占一行）
e.ex("B1", "完成句子", "is aangekomen", "aankomen 用 zijn：is aangekomen",
     "Sinterklaas ___ (aankomen) in Grave.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "heeft ontvangen", "ontvangen 的 perfectum：heeft ontvangen",
     "De burgemeester ___ (ontvangen) Sinterklaas.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "is gevaren", "varen 用 zijn：is gevaren",
     "De boot ___ (varen) van De Omval naar het Scheepvaartmuseum.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "hebben gelezen", "lezen 的 perfectum：hebben gelezen",
     "Veel mensen ___ (lezen) Het diner in november.", instr="填空", size=20, gap=8)
e.head("D　REKENEN", 25)
e.bridge("算一算：用第 3 版的数字回答。")
e.ex("B1", "完成句子", "1", "11 月 14 日到 15 日相隔 1 天",
     "Van zaterdag 14 tot zondag 15 november: ___ dag.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "4", "赫拉弗活动 12:00–16:00 共 4 小时",
     "Het programma in Grave duurde van 12:00 tot 16:00 uur: ___ uur.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "19", "11 月 16 日到 12 月 5 日相隔 19 天",
     "Van 16 november tot 5 december: ___ dagen.", instr="填空", size=20, gap=8)
e.ex("B2", "完成句子", "17", "《晚餐》2009 年出版，到 2026 年 17 年",
     "Het diner is uit 2009; in 2026 is dat ___ jaar geleden.", instr="填空", size=20, gap=8)
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-cultuur.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　体育", "De Lucerna", "NIVEAU B1　Oranje en de Nations League　橙衣军团与国家联赛")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P4-feature")
f.title("Oranje: de beslissing in Berlijn", 32)
f.byline("Van de redactie van De Lucerna　Leesniveau: B1")
f.para("Op maandag 16 november speelt Oranje in Berlijn tegen Duitsland. De wedstrijd begint om 20:45 uur in het Olympiastadion en is live te zien op NPO 3. Het is de zesde en laatste wedstrijd in de groepsfase van de Nations League — en de beslissing in groep 2: de nummers één en twee gaan naar de kwartfinales in maart 2027.")
f.para("Na vier wedstrijden staan Nederland en Griekenland samen bovenaan met 8 punten. Duitsland heeft 5 punten, Servië heeft 0 punten. Nederland staat eerste, omdat het meer doelpunten maakte: 7 tegen 5. Oranje is nog ongeslagen: 1–1 thuis tegen Duitsland, 2–1 uit bij Servië, 2–2 uit bij Griekenland en 2–1 thuis tegen Servië.")
f.para("Duitsland moet winnen in Berlijn. De Duitsers verloren thuis met 0–1 van Griekenland, wonnen met 2–0 van Servië en speelden met 0–0 gelijk in Griekenland. Vrijdag speelde Duitsland in Belgrado tegen Servië; Oranje speelde vrijdag thuis tegen Griekenland. Maandagavond in Berlijn valt de beslissing.")
f.para("De Eredivisie begint zaterdag weer: speelronde 13 is op 21 en 22 november. Zaterdag speelt PSV om 16:30 uur uit bij NEC en speelt Feyenoord om 18:45 uur thuis tegen Excelsior. Zondag speelt Ajax om 14:30 uur thuis tegen ADO Den Haag en speelt FC Twente om 12:15 uur thuis tegen Willem II. Vóór de interlandperiode won PSV met 2–5 van Cambuur en werd het 5–3 bij Heerenveen – Feyenoord.")
f.head("DE STAND IN GROEP 2", 25)
f.para("Nederland 8 punten, Griekenland 8, Duitsland 5, Servië 0. Twee landen gaan door. Maandag in Berlijn is dus bijna een finale — de laatste wedstrijd van de groep.")
f.gloss("de groepswinst 小组头名 · de kwartfinale 四分之一决赛 · ongeslagen 未尝败绩 · de interland 国家队比赛 · de stand 积分榜。")
f.end_report()

# col 3: image + programme box (sequential, measured)
ix = COLX[3]
image(p, "elftal1912.jpg", ix, 200, CW, 250)
cy3 = caption(p, ix, 450, CW, "Het Nederlands elftal in 1912. Oranje speelt al meer dan honderd jaar in het oranje.",
              "Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein")
facts = ["Maandag 16 november, 20:45 uur: Duitsland – Nederland, Berlijn, NPO 3.",
         "Stand na 4 wedstrijden: Nederland 8, Griekenland 8, Duitsland 5, Servië 0 punten.",
         "Speelronde 12: Heerenveen – Feyenoord 5–3; Cambuur – PSV 2–5; Twente – Ajax 2–2.",
         "Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.",
         "Speelronde 13: zaterdag NEC – PSV 16:30 uur; Feyenoord – Excelsior 18:45 uur."]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 12 for t in facts) + 32 + 30
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "HET PROGRAMMA", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P4 col3 ends", sy3 + sh)

# ---- P4 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "OEFENINGEN　第4版练习", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "答案见第8版　题目可跨级混排，按题号找答案", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　BEGRIJPEN", 25)
e.bridge("读第 4 版文章，选出正确答案。")
e.ex("B1", "单选", "C", "德国–荷兰周一在柏林",
     "Duitsland – Nederland is op... A. vrijdag 13 november · B. zaterdag 14 november · C. maandag 16 november", size=20, gap=8)
e.ex("B1", "单选", "B", "荷兰与希腊同积 8 分",
     "Na vier wedstrijden hebben Nederland en Griekenland... A. 5 punten · B. 8 punten · C. 0 punten", size=20, gap=8)
e.ex("B1", "单选", "B", "德国主场 0–1 输给了希腊",
     "Duitsland verloor thuis met 0–1 van... A. Servië · B. Griekenland · C. Nederland", size=20, gap=8)
e.ex("B1", "单选", "B", "荷甲第 13 轮在 11 月 21–22 日",
     "Speelronde 13 is op... A. 13 en 14 november · B. 21 en 22 november · C. 9 en 10 november", size=20, gap=8)
e.ex("B1", "单选", "B", "PSV 2–5 赢了 Cambuur",
     "PSV won met 2–5 van... A. Feyenoord · B. Cambuur · C. Ajax", size=20, gap=8)
e.head("B　WOORDEN UIT DE TEKST", 25)
e.bridge("用方框里的词填空。注意动词形式。")
e.para("groepswinst · kwartfinale · ongeslagen · interland · stand", 20, "sans", True, OLIVE, 1.35, 6)
e.ex("B1", "完成句子", "groepswinst", "groepswinst = 小组头名",
     "Maandag valt de beslissing om de ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "kwartfinales", "kwartfinale 复数：kwartfinales",
     "De nummers één en twee gaan naar de ___.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "ongeslagen", "ongeslagen = 未尝败绩",
     "Oranje is nog ___ na vier wedstrijden.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "stand", "stand = 积分榜",
     "Op de ___ staat Servië onderaan met 0 punten.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "interland", "interland = 国家队比赛",
     "Na maandag is er geen ___ meer tot maart.", instr="填空", size=20, gap=8)
e.head("C　VERLEDEN TIJD", 25)
e.bridge("用过去时或完成时补全。")
e.ex("B1", "完成句子", "speelde", "spelen 过去时：speelde",
     "Oranje ___ (spelen) 1–1 tegen Duitsland.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "won", "winnen 过去时：won",
     "PSV ___ (winnen) met 2–5 van Cambuur.", instr="填空", size=20, gap=8)
e.ex("B1", "完成句子", "verloor", "verliezen 过去时：verloor",
     "Feyenoord ___ (verliezen) met 5–3 bij Heerenveen.", instr="填空", size=20, gap=8)
e.ex("B2", "完成句子", "speelden", "spelen 过去时复数：speelden",
     "Twente en Ajax ___ (spelen) 2–2 gelijk.", instr="填空", size=20, gap=8)
e.head("D　WAAR OF NIET WAAR?", 25)
e.ex("B1", "判断对错", "Waar", "对：德国–荷兰周一 20:45",
     "Duitsland – Nederland begint maandag om 20:45 uur. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Niet waar", "错：塞尔维亚 0 分垫底",
     "Servië heeft 8 punten in groep 2. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Niet waar", "错：PSV 26 分领跑荷甲",
     "PSV staat onderaan in de Eredivisie. Waar of niet waar?", instr="判断", size=20, gap=8)
e.ex("B1", "判断对错", "Waar", "对：海伦芬 5–3 赢费耶诺德",
     "Heerenveen won met 5–3 van Feyenoord. Waar of niet waar?", instr="判断", size=20, gap=8)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
