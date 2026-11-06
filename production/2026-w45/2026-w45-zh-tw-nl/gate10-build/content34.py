# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P3 culture, P4 sport.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-zh-tw-nl-gate10-out/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P3 · culture
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · Cultuur", "Lucerna", "第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, staalkunst en de zandfestivalfinale")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P3-main")
f.title("立冬:冬天開始的日子", 34)
f.para("二十四節氣是古人看天氣、安排農事的方法。立冬是冬天第一個節氣,意思是冬天開始了。立冬一到,天氣會越來越冷,日夜溫差也越來越大,大家要開始注意保暖。")
f.para("立冬吃什麼?台灣人常在立冬吃薑母鴨、羊肉爐、麻油雞,用熱鍋幫身體補一補。老一輩的人說,立冬補冬,補嘴空:意思是冬天之前,先把身體養好。吃補也要適量,不要一餐吃太多,也不要天天大魚大肉。")
f.gloss("Lidong is de eerste zonneterm van de winter: de winter begint. Mensen vieren dat met hotpotgerechten zoals gember-eend, lamshotpot en sesamkip — verwarmend eten vóór de koude maanden.")
f.title("高雄鋼雕藝術節:鋼鐵變舞台", 34)
f.para("在高雄,鋼鐵也能變成舞台。2026高雄國際鋼雕藝術節從10月23日到11月22日,主題是 SUPER STAGE,地點在駁二蓬萊區B3倉庫、哈瑪星鐵道園區、鹽埕街區。倉庫、工廠、港口、街區,都變成看作品的地方。")
f.para("高雄是工業起家的城市,鋼鐵是它的材料,也是它的記憶。藝術節請來台灣、日本、英國、法國的設計師和產業講者,辦國際論壇「剛質潮汐 SOLID TIDES」,聊製造、設計,聊藝術怎麼走進日常生活。展期到11月22日,本週去看,正是最好的時候。")
f.para("開放時間:週一到週四上午10點到下午6點;週五、週末和國定假期上午10點到晚上8點。出門前,先查主辦單位的最新公告。")
f.gloss("Het Internationale Staalsculptuurfestival van Kaohsiung (23 okt-22 nov) maakt van pakhuizen, fabrieken, de haven en straten een podium — SUPER STAGE — met een internationaal forum over maken, design en kunst in het dagelijks leven.")
f.title("上週回顧:福隆沙雕落幕", 34)
f.para("福隆的夏天,在10月26日畫下句點。2026福隆國際沙雕藝術季從5月29日開展,到10月26日結束,是第19屆,主題是「全球夏日沙雕派對」。15位以上國內外藝術家,用福隆的金色沙子,做出40座以上沙雕,還找來侏羅紀世界、史瑞克、功夫熊貓、回到未來這些大家熟悉的電影角色。")
f.para("沙雕最怕什麼?怕雨,也怕風。一個夏天過去,沙雕陪大家過完暑假,最後回到大海。下一個夏天,福隆還會有新的沙雕等你。")
f.gloss("Het Internationale Zandsculptuurfestival van Fulong sloot op 26 okt na zijn 19e seizoen (29 mei-26 okt): 40+ sculpturen van 15+ kunstenaars, gebouwd uit het gouden zand van Fulong rond filmfiguren uit Jurassic World, Shrek, Kung Fu Panda en Back to the Future.")
f.head("讀懂了嗎? · Begrepen?", 28)
f.ex("A2", "單選", "A", "Lidong betekent dat de winter begint.",
     "立冬是什麼意思?", opts=["A. 冬天開始", "B. 冬天結束", "C. 春天開始"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "Gember-eend is een typisch Lidong-gerecht.",
     "立冬常吃什麼?", opts=["A. 冰品", "B. 薑母鴨", "C. 生魚片"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "Het staalfestival loopt van 23 okt tot 22 nov.",
     "高雄鋼雕藝術節展到哪天?", opts=["A. 11月2日", "B. 11月7日", "C. 11月22日"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "De locaties omvatten het Penglai B3-pakhuis van Pier-2.",
     "鋼雕藝術節的地點之一是?", opts=["A. 駁二蓬萊區B3倉庫", "B. 台北大巨蛋", "C. 南港展覽館"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "Het zandfestival sloot op 26 okt.",
     "福隆沙雕藝術季哪天結束?", opts=["A. 10月19日", "B. 10月26日", "C. 11月1日"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "Het zandfestival maakte 40+ sculpturen.",
     "福隆沙雕有幾座以上?", opts=["A. 10座", "B. 20座", "C. 40座"], size=22.5, gap=8)
f.head("填一填 · Vul in", 28)
f.ex("A2", "完成句子", "節氣", "Lidong is een zonneterm (節氣).",
     "立冬是二十四___之一。", instr="Vul in", size=22.5, gap=8)
f.ex("A2", "完成句子", "麻油雞", "Sesamkip is een Lidong-gerecht.",
     "立冬常吃薑母鴨、羊肉爐、___。", instr="Vul in", size=22.5, gap=8)
f.ex("B1", "完成句子", "鋼鐵", "Staal is het materiaal en het geheugen van Kaohsiung.",
     "高雄用___做藝術,辦鋼雕藝術節。", instr="Vul in", size=22.5, gap=8)
f.ex("B1", "完成句子", "哈瑪星", "Het Hamasen-spoorwegpark is een locatie.",
     "鋼雕藝術節的地點包括___鐵道園區。", instr="Vul in", size=22.5, gap=8)
f.ex("B1", "完成句子", "金色", "Het zand van Fulong is goudkleurig.",
     "福隆的沙子是___的沙子。", instr="Vul in", size=22.5, gap=8)
f.ex("B1", "完成句子", "侏羅紀世界", "Jurassic World is een van de filmfiguren.",
     "福隆沙雕有___、史瑞克這些電影角色。", instr="Vul in", size=22.5, gap=8)
f.head("算一算 · Reken uit", 28)
f.ex("B1", "單選", "C", "29-31 mei (3) + 30 juni + 31 juli + 31 aug + 30 sept + 26 okt = 151 dagen.",
     "福隆沙雕展期5月29日到10月26日,一共幾天?", opts=["A. 120天", "B. 140天", "C. 151天"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "23-31 okt (9) + 22 nov = 31 dagen.",
     "鋼雕藝術節10月23日到11月22日,一共幾天?", opts=["A. 22天", "B. 31天", "C. 40天"], size=22.5, gap=8)
f.match_set("B1", "配對",
            ["立冬", "進補", "鋼雕", "沙雕"],
            ["冬天第一個節氣", "冬天前吃熱的養身體", "用鋼鐵做的藝術", "用沙子堆出來的雕塑"],
            ["a", "b", "c", "d"],
            ["立冬 — de eerste zonneterm van de winter.",
             "進補 — voedzaam eten vóór de winter.",
             "鋼雕 — sculptuur gemaakt van staal.",
             "沙雕 — sculptuur gebouwd uit zand."],
            instr="Koppel")
f.end_report()

rx = COLX[3]
by = 208
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "節氣小表 · Zonnetermen", 25, "sans", True, OLIVE); yy += 56
for t in [
    "立冬:11月7日(六),冬天開始",
    "小雪:11月22日(日),下一個節氣",
    "立冬吃鍋:薑母鴨、羊肉爐、麻油雞",
    "提醒:吃補適量,腸胃不好先問醫生",
    "立冬不是假期,照常上班上課",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 260, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢? · Nu jij", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你去過福隆看沙雕嗎?最想看哪一部電影的沙雕?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Heb je de zandsculpturen van Fulong gezien? Welk filmfiguur zou je het liefst in zand willen zien?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 260 + 18
p.rect(rx, by3, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
yy = by3 + 18
p.text(rx + 22, yy + 26, "鋼雕行程 · Plan je bezoek", 25, "sans", True, OLIVE); yy += 56
for t in [
    "日期:10月23日到11月22日",
    "地點:駁二蓬萊區B3倉庫、哈瑪星鐵道園區、鹽埕街區",
    "平日:上午10點到下午6點",
    "週五、週末、假期:上午10點到晚上8點",
    "論壇:剛質潮汐 SOLID TIDES",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ============================================================ P4 · sport
CURPAGE[0] = 4
p = BSPage4()
p.band("體育 · Sport", "Lucerna", "第 4 版 · 台灣大賽封王 · De Taiwan Series is beslist")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 1020, tag="P4-main")
f.title("味全龍封王!6比0完封兄弟", 34)
f.byline("Redactieverslag · Bron: TSNA-sportnieuws, 26 okt")
f.para("台灣大賽有結果了!10月26日(週一)第六戰,味全龍在台北大巨蛋6比0完封中信兄弟,系列賽4勝2敗,拿下中華職棒2026年度總冠軍。這是中職史上第一場「龍象大戰」,也是味全龍隊史第6座總冠軍。")
f.para("第六戰的英雄是先發投手梅賽鍶。他先發8局,只被敲出2支安打,送出6次三振,沒有失分。3局下,張政禹擊出安打,先幫龍隊拿下1分。8局下,郭天信、張政禹、劉基鴻、朱育賢連續安打,加上蔣少宏的兩分全壘打,龍隊單局拿下5分,比賽就此底定。6比0完封兄弟，龍隊拋下紅色彩帶。")
f.para("梅賽鍶獲選台灣大賽最有價值球員:他在台灣大賽2場先發,14局只掉1分,完全封鎖對手。更厲害的是,龍隊在這個系列賽3度完封對手,是單一台灣大賽史上第一次。")
f.gloss("De Wei Chuan Dragons versloegen de CTBC Brothers met 6-0 in wedstrijd 6 (26 okt, Taipei Dome) en wonnen de Taiwan Series 2026 met 4-2 — de allereerste Dragons-Brothers-finale en de 6e titel van de Dragons. Starter C.C. Mercedes gooide 8 shutout-innings en werd uitgeroepen tot MVP van de Series.")
f.title("棒球詞卡 · Honkbaltaal", 34)
f.para("完封:對手得0分,叫完封。封王:拿下總冠軍,叫封王。全壘打:一棒打出場外,叫全壘打。最有價值球員:系列賽表現最好的人,英文叫 MVP。")
f.gloss("Vier woorden: 完封 (shutout), 封王 (de titel pakken), 全壘打 (homerun), MVP (meest waardevolle speler).")
f.end_report()

# ---- chart: Game 6 runs by inning (innings 1-8; bottom 9th not played) ----
chy = 1070
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, GOLD, 2)
p.text(MX, chy + 28, "第六戰得分走勢 · Wedstrijd 6: punten per inning — balken in verhouding tot de punten", 27, "sans", True, OLIVE)
BX = MX + 215
SCALE = 120.0
runs = [("第1局", 0), ("第2局", 0), ("第3局", 1), ("第4局", 0), ("第5局", 0), ("第6局", 0), ("第7局", 0), ("第8局", 5)]
ry = chy + 54
for label, val in runs:
    p.text(MX + 20, ry + 22, label, 22, "serif", False, INK)
    p.text(BX - 14, ry + 22, str(val), 22, "serif", True, INK, anchor="end")
    if val > 0:
        p.rect(BX, ry, val * SCALE, 28, fill="#a4553a")
    ry += 40
chart_end = ry + 10
p.text(MX, chart_end + 24, "龍隊後攻,得分都在局下半。龍隊9局下不用打:9局上結束,龍隊6比0領先,比賽結束。3局下1分、8局下5分,合計6分。", 21, "serif", False, GREY)
p.text(MX, chart_end + 56, "Opmerking: de Dragons sloegen niet in de tweede helft van de 9e inning — met 6-0 voor na de eerste helft van de 9e inning was de wedstrijd voorbij. 1 + 5 = 6.", 20, "sans", False, GREY)

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 64, 2540, tag="P4-ex")
e.head("讀懂了嗎? · Begrepen?", 26)
e.ex("B1", "單選", "B", "De Dragons wonnen wedstrijd 6 met 6-0.",
     "台灣大賽第六戰,比數是多少?", opts=["A. 3比0", "B. 6比0", "C. 6比3"], size=21.5, gap=6)
e.ex("B1", "單選", "C", "De Series eindigde in 4-2 voor de Dragons.",
     "系列賽最後是幾勝幾敗?", opts=["A. 4勝0敗", "B. 4勝1敗", "C. 4勝2敗"], size=21.5, gap=6)
e.ex("B1", "單選", "A", "Mercedes gooide 8 shutout-innings.",
     "梅賽鍶先發幾局、失幾分?", opts=["A. 8局、0分", "B. 7局、1分", "C. 9局、2分"], size=21.5, gap=6)
e.ex("B1", "單選", "B", "Mercedes werd uitgeroepen tot MVP van de Series.",
     "台灣大賽最有價值球員是誰?", opts=["A. 蔣少宏", "B. 梅賽鍶", "C. 張政禹"], size=21.5, gap=6)
e.ex("B1", "單選", "A", "De 6e titel in de clubgeschiedenis van de Dragons.",
     "這是味全龍隊史第幾座總冠軍?", opts=["A. 第6座", "B. 第4座", "C. 第3座"], size=21.5, gap=6)
e.ex("B1", "單選", "C", "Drie shutouts in één Series is een primeur.",
     "龍隊在系列賽幾度完封對手?", opts=["A. 1度", "B. 2度", "C. 3度"], size=21.5, gap=6)
e.head("填一填 · Vul in", 28)
e.ex("B1", "完成句子", "大巨蛋", "Wedstrijd 6 werd gespeeld in de Taipei Dome.",
     "第六戰在台北___舉行。", instr="Vul in", size=21.5, gap=6)
e.ex("B1", "完成句子", "完封", "Een shutout: de andere ploeg scoort nul.",
     "對手得0分,叫___。", instr="Vul in", size=21.5, gap=6)
e.ex("B1", "完成句子", "封王", "De titel winnen is 封王.",
     "拿下總冠軍,叫___。", instr="Vul in", size=21.5, gap=6)
e.ex("B1", "完成句子", "全壘打", "Een bal die het park uit wordt geslagen is een homerun.",
     "蔣少宏擊出兩分___。", instr="Vul in", size=21.5, gap=6)
e.ex("B1", "完成句子", "14", "Mercedes stond 1 punt toe in 14 innings.",
     "梅賽鍶2場先發,___局只掉1分。", instr="Vul in", size=21.5, gap=6)
e.ex("B1", "完成句子", "5", "De Dragons scoorden 5 punten in de 8e inning.",
     "龍隊8局下拿下___分。", instr="Vul in", size=21.5, gap=6)
e.head("看圖答題 · Lees de grafiek", 28)
e.ex("B1", "單選", "B", "De 8e inning: 5 punten, de grootste balk.",
     "龍隊哪一局得分最多?", opts=["A. 3局下", "B. 8局下", "C. 9局下"], size=21.5, gap=6)
e.ex("B1", "單選", "A", "1 + 5 = 6 punten in totaal.",
     "3局下和8局下加起來是幾分?", opts=["A. 6分", "B. 5分", "C. 8分"], size=21.5, gap=6)
e.match_set("B1", "配對",
            ["完封", "封王", "全壘打", "安打"],
            ["對手得0分", "拿下總冠軍", "一棒打出場外", "打者把球打到場內形成上壘"],
            ["a", "b", "c", "d"],
            ["完封 — een shutout: de andere ploeg scoort nul.",
             "封王 — het kampioenschap pakken.",
             "全壘打 — een homerun.",
             "安打 — een honkslag."],
            instr="Koppel")
e.end_report()

rx = COLX[3]
image(p, "baseball.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "棒球舊照(資料照片)。第六戰,龍隊8局下連續安打,奠定勝基。",
        "Photo: Bain News Service — Public domain (Wikimedia Commons)")
by = 208 + 300 + 132
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "系列賽小檔 · Seriedossier", 25, "sans", True, OLIVE); yy += 56
for t in [
    "第六戰:10月26日(一),台北大巨蛋",
    "比數:味全龍 6比0 中信兄弟",
    "系列賽:龍隊 4勝2敗封王",
    "隊史:第6座總冠軍",
    "紀錄:史上首場龍象大戰;單一系列3度完封史上第一次",
]:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + 488, CW, 230, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + 488 + 18
p.text(rx + 22, yy + 26, "你呢? · Nu jij", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你支持哪一隊?你看過現場棒球賽嗎?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Welke ploeg steun jij? Heb je ooit een honkbalwedstrijd live gezien?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
