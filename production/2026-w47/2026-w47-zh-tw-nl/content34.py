# -*- coding: utf-8 -*-
# W47 zh-tw core, VOL.4: P3 culture, P4 sport.
# P3: Golden Horse Awards (Nov 22) + steel festival closing (Nov 22).
# P4: Dragons championship parade (Nov 22) + U-Sport November points.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-nl/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P3 · culture
CURPAGE[0] = 3
p = BSPage4()
p.band("文化　Cultuur", "Lucerna", "第3版　金馬獎　鋼雕閉幕　De Golden Horse Awards en de laatste dag van de staalkunst")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2560, tag="P3-main")
f.title("金馬獎本週日頒獎，誰會得獎？", 32)
f.para("2026台北金馬影展從11月6日放到11月22日，入圍影片都在影展放映。今年有587部影片報名，入圍名單在10月1日公布，《狂忘警探》入圍11項，是入圍最多的影片。頒獎典禮在本週日（11月22日）舉行，地點在台北流行音樂中心，下午5點先走星光大道，頒獎典禮晚上6點30分開始。今年的主題是「再見江湖」，主持人是香港演員柯煒林，第一次主持金馬獎。得獎名單要到典禮當天才揭曉，現在誰也不知道誰會得獎。")
f.para("金馬獎，就是一年一度的大電影課：看片、聽影人分享、學電影怎麼拍。影展最後一天就是頒獎典禮，想看入圍電影的人，要把握最後一週。")
f.gloss("Het Taipei Golden Horse Film Festival 2026 loopt van 6 tot 22 nov.: 587 inzendingen, nominaties bekendgemaakt op 1 okt., één film aan kop met 11 nominaties. De 63e Golden Horse Awards volgen op zondag 22 nov. in het Taipei Music Center — rode loper om 17:00, ceremonie om 18:30, gepresenteerd door Will Or (Ko Wai-lam). Geen winnaar is bekend tot die avond zelf.")
f.title("鋼雕藝術節：最後一週，快去看", 32)
f.para("2026高雄國際鋼雕藝術節展到11月22日，主題是 SUPER STAGE，地點在駁二蓬萊區B3倉庫、哈瑪星鐵道園區、鹽埕街區。最後一個週末是11月21日、22日，想去的人，先查主辦單位的最新公告。平日上午10點到下午6點；週五、週末和假期，開到晚上8點。")
f.para("主題展「安全第一 SUPER SAFE」把蓬萊B3倉庫變成一座「保險箱」：保險箱裡，裝的是高雄的勞動記憶。85歲素人藝術家林洪玉秀用金屬紗網編出永不凋謝的花，作品叫《萬年吉祥花》，是本屆最動人的亮點之一。她年輕時在鹽埕學裁縫，為新娘縫婚紗，如今把人生經歷編進金屬花裡。")
f.gloss("Het Internationale Steel Sculpture Festival van Kaohsiung (23 okt.–22 nov., SUPER STAGE) bereikt het laatste weekend, 21–22 nov., in het Penglai B3-pakhuis, Hamasen en Yancheng. De themashow SUPER SAFE verandert het pakhuis in een stalen kluis met de arbeidsherinneringen van Kaohsiung — waaronder de eeuwige metalen bloemen van de 85-jarige Lin Hung Yu-hsiu.")
f.title("電影小課：1902年的月球之旅", 32)
f.para("一百多年前，電影還是黑白默片：沒有聲音，也沒有顏色。法國導演梅里愛在1902年拍了《月球之旅》，講一群人坐大砲做的太空船飛上月球，是最早的科幻電影之一。今天看金馬獎，也要記得：電影從黑白默片走到今天，走了一百多年。")
f.gloss("Ruim een eeuw geleden waren films zwart-wit en stil. A Trip to the Moon (1902) van de Franse regisseur Georges Méliès — een bemanning die in een als kanon gebouwd ruimteschip naar de maan wordt geschoten — is een van de vroegste sciencefictionfilms. De Golden Horse Awards vieren een eeuw van die reis.")
f.head("讀懂了嗎？　Begrepen?", 25)
f.ex("A2", "單選", "A", "Het filmfestival loopt van 6 tot 22 nov.",
     "金馬影展放到哪天？", opts=["A. 11月22日", "B. 11月15日", "C. 11月9日"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "587 films ingezonden dit jaar.",
     "今年金馬獎有幾部影片報名？", opts=["A. 87部", "B. 587部", "C. 57部"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "De ceremonie is op zondag 22 nov.",
     "第63屆金馬獎頒獎典禮在哪天？", opts=["A. 11月15日", "B. 11月9日", "C. 11月22日"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "De ceremonie begint om 18:30.",
     "金馬獎頒獎典禮晚上幾點開始？", opts=["A. 6點30分", "B. 5點", "C. 8點"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Het staalfestival sluit op 22 nov.",
     "高雄鋼雕藝術節展到哪天？", opts=["A. 11月15日", "B. 11月22日", "C. 12月22日"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "A Trip to the Moon is gemaakt in 1902.",
     "《月球之旅》是哪一年拍的？", opts=["A. 2026年", "B. 1920年", "C. 1902年"], size=22.5, gap=8)
f.head("填一填　Invullen", 25)
f.ex("A2", "完成句子", "入圍", "De nominatielijst werd op 1 okt. bekendgemaakt.",
     "金馬獎___名單在10月1日公布。", instr="Invullen", size=22.5, gap=8)
f.ex("A2", "完成句子", "星光大道", "De rode loper begint om 17:00.",
     "頒獎典禮前，先走___。", instr="Invullen", size=22.5, gap=8)
f.ex("B1", "完成句子", "保險箱", "Het pakhuis wordt een stalen kluis.",
     "主題展把倉庫變成一座___。", instr="Invullen", size=22.5, gap=8)
f.ex("B1", "完成句子", "鹽埕", "Yancheng is een van de festivalwijken.",
     "鋼雕藝術節的地點包括駁二、哈瑪星和___街區。", instr="Invullen", size=22.5, gap=8)
f.ex("B1", "完成句子", "默片", "Vroege films waren zwart-wit en stil.",
     "一百多年前的電影是黑白___。", instr="Invullen", size=22.5, gap=8)
f.ex("B1", "完成句子", "柯煒林", "Will Or presenteert de ceremonie van dit jaar.",
     "今年金馬獎主持人是___。", instr="Invullen", size=22.5, gap=8)
f.head("算一算　Reken uit", 25)
f.ex("B1", "單選", "C", "6 tot 22 nov. inclusief is 17 dagen.",
     "金馬影展11月6日到11月22日，一共幾天？", opts=["A. 15天", "B. 16天", "C. 17天"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Van 17:00 tot 18:30 is 1,5 uur.",
     "星光大道下午5點開始，典禮晚上6點30分開始，中間隔多久？", opts=["A. 1小時", "B. 1小時30分", "C. 2小時"], size=22.5, gap=8)
f.match_set("B1", "配對",
            ["入圍", "頒獎", "鋼雕", "默片"],
            ["被選進最後的得獎名單", "把獎頒給得獎的人", "用鋼鐵做的藝術", "沒有聲音的早期電影"],
            ["a", "b", "c", "d"],
            ["入圍 — genomineerd zijn.",
             "頒獎 — prijzen uitreiken.",
             "鋼雕 — sculptuur van staal.",
             "默片 — een stomme film."],
            instr="Combineren")
f.end_report()

rx = COLX[3]
image(p, "moon.jpg", rx, 208, CW, 300)
by = caption(p, rx, 208 + 300 + 6, CW, "1902年電影《月球之旅》劇照（資料照片）。電影從黑白默片走到今天的金馬獎。",
        "Foto: Georges Méliès — publiek domein (Wikimedia Commons)") + 18
p.rect(rx, by, CW, 470, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "金馬小表　Golden-Horse-fiche", 25, "sans", True, OLIVE); yy += 56
for t in [
    "影展：11月6日到11月22日",
    "報名：587部影片，入圍10月1日公布",
    "頒獎：11月22日（日），台北流行音樂中心",
    "星光大道：下午5點；典禮：晚上6點30分",
    "主題：再見江湖；主持人：柯煒林",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 250, fill=BOX)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢？　En jij?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你最想看哪一部入圍電影？你去過駁二看展嗎？", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Welke genomineerde film zou je het liefst zien? Ben je weleens naar een tentoonstelling in Pier-2 geweest?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 250 + 18
p.rect(rx, by3, CW, 450, fill=BOX)
yy = by3 + 18
p.text(rx + 22, yy + 26, "鋼雕閉幕行程　Laatste weekend", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日期：10月23日到11月22日",
    "地點：駁二蓬萊區B3倉庫、哈瑪星鐵道園區、鹽埕街區",
    "最後週末：11月21日（六）、22日（日）",
    "平日10點到18點；週五、週末、假期到20點",
    "閉幕當天也是小雪，小雪是11月22日",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
by4 = by3 + 468
p.rect(rx, by4, CW, 430, fill=BOX)
yy = by4 + 18
p.text(rx + 22, yy + 26, "電影小檔　Bioscoopfiche", 25, "sans", True, OLIVE); yy += 56
for t in [
    "影展放映：11月6日到11月22日",
    "地點：威秀影城台北信義、MUVIE CINEMAS",
    "《月球之旅》：1902年，法國，梅里愛",
    "最早的科幻電影之一，黑白默片",
    "金馬獎：一年一度的大電影課",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ============================================================ P4 · sport
CURPAGE[0] = 4
p = BSPage4()
p.band("體育　Sport", "Lucerna", "第4版　封王遊行　運動集點　De kampioensparade en de sportpunten")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 1020, tag="P4-main")
f.title("本週日，封王遊行天母出發！", 32)
f.byline("Redactierapport　Bron: TSNA-sportnieuws en gemeentebestuur van Taipei, 30–31 okt.")
f.para("味全龍拿下隊史第6座總冠軍，封王遊行訂在本週日（11月22日）下午2點，從天母棒球場出發，終點是台北大巨蛋松菸大道。球團在11月21日、22日兩天，在天母棒球場辦球迷感謝祭：21日有草地音樂會，球迷可以在草坪上搭帳篷過夜；22日有球員互動、拍照和簽名，還有投打棒球教室。")
f.para("台北市政府也一起慶祝：11月整個月，市民到267間運動場館運動，U幣集點翻倍送。平常運動一次拿5個U幣，11月拿10個，滿100個U幣可以換成悠遊卡儲值金。穿上紅色衣服，一起上街為龍隊喝采，也順便養成運動習慣。")
f.gloss("De kampioensparade van de Wei Chuan Dragons is gepland op zondag 22 nov. om 14:00, van het Tianmu Baseball Stadium naar de Taipei Dome. Een tweedaags dankfeest voor fans is er op 21–22 nov. in Tianmu: grasconcert en overnachten op het gras op de 21e, spelersactiviteiten op de 22e. De stad Taipei verdubbelt in heel november de U-Sport-punten: 10 punten per bezoek in plaats van 5, op 267 locaties.")
f.title("棒球詞卡　Honkbalwoorden", 32)
f.para("遊行：大家走上街頭慶祝，叫遊行。感謝祭：球隊謝謝球迷的活動，叫感謝祭。集點：每次運動累積點數，叫集點。封王：拿下總冠軍，叫封王——上週本報已經教過這個詞了。")
f.gloss("Vier woorden: 遊行 (parade), 感謝祭 (dankfeest voor fans), 集點 (punten verzamelen), 封王 (de titel pakken).")
f.end_report()

# ---- chart: U-Sport points in November (10 points per visit, 100 to convert) ----
chy = 1070
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, OLIVE, 2)
p.text(MX, chy + 28, "U幣集點怎麼算　U-Sport-punten — balken in verhouding tot de punten", 27, "sans", True, OLIVE)
BX = MX + 215
SCALE = 9.0
rows = [("運動1次", 10), ("運動5次", 50), ("運動10次", 100)]
ry = chy + 54
for label, val in rows:
    p.text(MX + 20, ry + 22, label, 22, "serif", False, INK)
    p.text(BX - 14, ry + 22, str(val), 22, "serif", True, INK, anchor="end")
    if val > 0:
        p.rect(BX, ry, val * SCALE, 28, fill=OLIVE)
    ry += 40
chart_end = ry + 10
p.text(MX, chart_end + 24, "11月運動一次拿10個U幣，5次50個，10次100個，滿100個可以換成悠遊卡儲值金。平常一次只有5個U幣。", 21, "serif", False, GREY)
p.text(MX, chart_end + 56, "Opmerking: bezoeken in november leveren elk 10 punten op (normaal 5). 10 bezoeken × 10 = 100 punten, de omwisselgrens.", 20, "sans", False, GREY)

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 64, 2560, tag="P4-ex")
e.head("讀懂了嗎？　Begrepen?", 25)
e.ex("B1", "單選", "B", "De parade is op zondag 22 nov. om 14:00.",
     "封王遊行在哪天下午2點出發？", opts=["A. 11月15日", "B. 11月22日", "C. 11月9日"], size=22, gap=6)
e.ex("B1", "單選", "C", "De parade start bij het Tianmu Baseball Stadium.",
     "封王遊行從哪裡出發？", opts=["A. 台北大巨蛋", "B. 南港展覽館", "C. 天母棒球場"], size=22, gap=6)
e.ex("B1", "單選", "A", "Het festival is op 21–22 nov. in Tianmu.",
     "球迷感謝祭在哪兩天舉行？", opts=["A. 11月21、22日", "B. 11月14、15日", "C. 11月6、7日"], size=22, gap=6)
e.ex("B1", "單選", "B", "Bezoeken in november leveren elk 10 punten op.",
     "11月運動一次拿幾個U幣？", opts=["A. 5個", "B. 10個", "C. 100個"], size=22, gap=6)
e.ex("B1", "單選", "A", "100 punten worden omgezet in EasyCard-tegoed.",
     "滿幾個U幣可以換成悠遊卡儲值金？", opts=["A. 100個", "B. 50個", "C. 10個"], size=22, gap=6)
e.ex("B1", "單選", "C", "267 locaties doen mee.",
     "U幣集點有幾間運動場館參加？", opts=["A. 67間", "B. 167間", "C. 267間"], size=22, gap=6)
e.head("填一填　Invullen", 25)
e.ex("B1", "完成句子", "大巨蛋", "De parade eindigt bij de Taipei Dome.",
     "封王遊行終點是台北___松菸大道。", instr="Invullen", size=22, gap=6)
e.ex("B1", "完成句子", "遊行", "Een parade: iedereen gaat de straat op om te vieren.",
     "大家走上街頭慶祝，叫___。", instr="Invullen", size=22, gap=6)
e.ex("B1", "完成句子", "感謝祭", "Het dankfeest bedankt de fans.",
     "球隊謝謝球迷的活動，叫___。", instr="Invullen", size=22, gap=6)
e.ex("B1", "完成句子", "集點", "Punten verzamelen elke keer dat je sport.",
     "每次運動累積點數，叫___。", instr="Invullen", size=22, gap=6)
e.ex("B1", "完成句子", "帳篷", "Fans kamperen 's nachts op het gras.",
     "球迷可以在草坪上搭___過夜。", instr="Invullen", size=22, gap=6)
e.ex("B1", "完成句子", "紅色", "Draag rood voor de Dragons.",
     "看遊行要穿___衣服，為龍隊喝采。", instr="Invullen", size=22, gap=6)
e.head("看圖答題　Lees de grafiek", 25)
e.ex("B1", "單選", "B", "5 bezoeken × 10 punten = 50 punten.",
     "運動5次，一共幾個U幣？", opts=["A. 10個", "B. 50個", "C. 100個"], size=22, gap=6)
e.ex("B1", "單選", "C", "7 bezoeken × 10 = 70 punten; nog 30 tot 100.",
     "運動7次，一共70個U幣，還差幾個滿100個？", opts=["A. 10個", "B. 20個", "C. 30個"], size=22, gap=6)
e.match_set("B1", "配對",
            ["遊行", "感謝祭", "集點", "封王"],
            ["走上街頭慶祝", "球隊謝謝球迷的活動", "每次運動累積點數", "拿下總冠軍"],
            ["a", "b", "c", "d"],
            ["遊行 — een parade door de straten.",
             "感謝祭 — een dankfeest voor fans.",
             "集點 — punten verzamelen.",
             "封王 — de titel pakken."],
            instr="Combineren")
e.end_report()

rx = COLX[3]
image(p, "baseball.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "棒球舊照（資料照片）。本週日，龍隊封王遊行從天母出發。",
        "Foto: Bain News Service — publiek domein (Wikimedia Commons)")
by = 208 + 300 + 132
p.rect(rx, by, CW, 470, fill=BOX)
yy = by + 18
p.text(rx + 22, yy + 26, "遊行小檔　Paradefiche", 25, "sans", True, OLIVE); yy += 56
for t in [
    "遊行：11月22日（日）下午2點出發",
    "起點：天母棒球場；終點：台北大巨蛋松菸大道",
    "感謝祭：11月21、22日，天母棒球場",
    "21日：草地音樂會、草坪搭帳篷過夜",
    "22日：球員互動、拍照、簽名、棒球教室",
]:
    yy = p.para(rx + 22, yy + 24, t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 244, fill=BOX)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢？　En jij?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你會去看封王遊行嗎？你一週運動幾次？", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Ga je naar de kampioensparade kijken? Hoe vaak per week sport jij?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
