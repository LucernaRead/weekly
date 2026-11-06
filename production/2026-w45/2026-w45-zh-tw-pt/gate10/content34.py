# -*- coding: utf-8 -*-
# W45 zh-tw core, VOL.2: P3 culture, P4 sport.
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45-zh-tw-pt-gate10/svg"
os.makedirs(OUT, exist_ok=True)

# ============================================================ P3 · culture
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · Cultura", "Lucerna", "第 3 版 · 立冬、鋼雕與沙雕落幕 · Lidong, arte em aço e o fim do festival de areia")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P3-main")
f.title("立冬:冬天開始的日子", 34)
f.para("二十四節氣是古人看天氣、安排農事的方法。立冬是冬天第一個節氣,意思是冬天開始了。立冬一到,天氣會越來越冷,日夜溫差也越來越大,大家要開始注意保暖。")
f.para("立冬吃什麼?台灣人常在立冬吃薑母鴨、羊肉爐、麻油雞,用熱鍋幫身體補一補。老一輩的人說,立冬補冬,補嘴空:意思是冬天之前,先把身體養好。吃補也要適量,不要一餐吃太多,也不要天天大魚大肉。")
f.gloss("Lidong é o primeiro termo solar do inverno: o inverno começa. As pessoas marcam a data com pratos de panela quente como pato com gengibre, panela de carneiro e frango com gergelim — comida que aquece antes dos meses frios.")
f.title("高雄鋼雕藝術節:鋼鐵變舞台", 34)
f.para("在高雄,鋼鐵也能變成舞台。2026高雄國際鋼雕藝術節從10月23日到11月22日,主題是 SUPER STAGE,地點在駁二蓬萊區B3倉庫、哈瑪星鐵道園區、鹽埕街區。倉庫、工廠、港口、街區,都變成看作品的地方。")
f.para("高雄是工業起家的城市,鋼鐵是它的材料,也是它的記憶。藝術節請來台灣、日本、英國、法國的設計師和產業講者,辦國際論壇「剛質潮汐 SOLID TIDES」,聊製造、設計,聊藝術怎麼走進日常生活。展期到11月22日,本週去看,正是最好的時候。")
f.para("開放時間:週一到週四上午10點到下午6點;週五、週末和國定假期上午10點到晚上8點。出門前,先查主辦單位的最新公告。")
f.gloss("O Festival Internacional de Escultura em Aço de Kaohsiung (23 de outubro a 22 de novembro) transforma armazéns, fábricas, o porto e as ruas em um palco — SUPER STAGE — com um fórum internacional sobre fazer, design e arte na vida cotidiana.")
f.title("上週回顧:福隆沙雕落幕", 34)
f.para("福隆的夏天,在10月26日畫下句點。2026福隆國際沙雕藝術季從5月29日開展,到10月26日結束,是第19屆,主題是「全球夏日沙雕派對」。15位以上國內外藝術家,用福隆的金色沙子,做出40座以上沙雕,還找來侏羅紀世界、史瑞克、功夫熊貓、回到未來這些大家熟悉的電影角色。")
f.para("沙雕最怕什麼?怕雨,也怕風。一個夏天過去,沙雕陪大家過完暑假,最後回到大海。下一個夏天,福隆還會有新的沙雕等你。")
f.gloss("O Festival Internacional de Escultura em Areia de Fulong encerrou em 26 de outubro após sua 19.ª temporada (29 de maio a 26 de outubro): mais de 40 esculturas de mais de 15 artistas, construídas com a areia dourada de Fulong em torno de personagens de cinema de Jurassic World, Shrek, Kung Fu Panda e De Volta para o Futuro.")
f.head("讀懂了嗎? · Entendeu?", 28)
f.ex("A2", "單選", "A", "Lidong significa que o inverno começa.",
     "立冬是什麼意思?", opts=["A. 冬天開始", "B. 冬天結束", "C. 春天開始"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "Pato com gengibre é um prato típico do Lidong.",
     "立冬常吃什麼?", opts=["A. 冰品", "B. 薑母鴨", "C. 生魚片"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "O festival do aço vai de 23 de outubro a 22 de novembro.",
     "高雄鋼雕藝術節展到哪天?", opts=["A. 11月2日", "B. 11月7日", "C. 11月22日"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Entre as sedes está o armazém B3 de Penglai, no Pier-2.",
     "鋼雕藝術節的地點之一是?", opts=["A. 駁二蓬萊區B3倉庫", "B. 台北大巨蛋", "C. 南港展覽館"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "O festival de areia encerrou em 26 de outubro.",
     "福隆沙雕藝術季哪天結束?", opts=["A. 10月19日", "B. 10月26日", "C. 11月1日"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "O festival de areia fez mais de 40 esculturas.",
     "福隆沙雕有幾座以上?", opts=["A. 10座", "B. 20座", "C. 40座"], size=22.5, gap=8)
f.head("填一填 · Complete", 28)
f.ex("A2", "完成句子", "節氣", "Lidong é um termo solar (jiéqì).",
     "立冬是二十四___之一。", instr="Complete", size=22.5, gap=8)
f.ex("A2", "完成句子", "麻油雞", "Frango com gergelim é um prato do Lidong.",
     "立冬常吃薑母鴨、羊肉爐、___。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "鋼鐵", "O aço é o material e a memória de Kaohsiung.",
     "高雄用___做藝術,辦鋼雕藝術節。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "哈瑪星", "O Parque Ferroviário de Hamasen é uma sede.",
     "鋼雕藝術節的地點包括___鐵道園區。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "金色", "A areia de Fulong é dourada.",
     "福隆的沙子是___的沙子。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "侏羅紀世界", "Jurassic World é um dos personagens de cinema.",
     "福隆沙雕有___、史瑞克這些電影角色。", instr="Complete", size=22.5, gap=8)
f.head("算一算 · Faça as contas", 28)
f.ex("B1", "單選", "C", "29 a 31 de maio (3) + 30 de junho + 31 de julho + 31 de agosto + 30 de setembro + 26 de outubro = 151 dias.",
     "福隆沙雕展期5月29日到10月26日,一共幾天?", opts=["A. 120天", "B. 140天", "C. 151天"], size=22.5, gap=8)
f.ex("B1", "單選", "B", "23 a 31 de outubro (9) + 22 de novembro = 31 dias.",
     "鋼雕藝術節10月23日到11月22日,一共幾天?", opts=["A. 22天", "B. 31天", "C. 40天"], size=22.5, gap=8)
f.match_set("B1", "配對",
            ["立冬", "進補", "鋼雕", "沙雕"],
            ["冬天第一個節氣", "冬天前吃熱的養身體", "用鋼鐵做的藝術", "用沙子堆出來的雕塑"],
            ["a", "b", "c", "d"],
            ["lìdōng — o primeiro termo solar do inverno.",
             "jìnbǔ — comida nutritiva antes do inverno.",
             "gāngdiāo — escultura feita de aço.",
             "shādiāo — escultura construída com areia."],
            instr="Associe palavra e definição")
f.end_report()

rx = COLX[3]
by = 208
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "節氣小表 · Termos solares", 25, "sans", True, OLIVE); yy += 56
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
p.text(rx + 22, yy + 26, "你呢? · E você?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你去過福隆看沙雕嗎?最想看哪一部電影的沙雕?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Você já viu as esculturas de areia de Fulong? Que personagem de cinema você mais gostaria de ver em areia?", 20, "sans", False, GREY, CW - 44, 1.3)
by3 = by + 488 + 260 + 18
p.rect(rx, by3, CW, 430, fill=BOX, stroke=LINE, sw=1.4)
yy = by3 + 18
p.text(rx + 22, yy + 26, "鋼雕行程 · Planeje sua visita", 25, "sans", True, OLIVE); yy += 56
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
p.band("體育 · Esporte", "Lucerna", "第 4 版 · 台灣大賽封王 · A Série de Taiwan está decidida")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 1020, tag="P4-main")
f.title("味全龍封王!6比0完封兄弟", 34)
f.byline("Reportagem da redação · Fonte: notícias esportivas da TSNA, 26 de outubro")
f.para("台灣大賽有結果了!10月26日(週一)第六戰,味全龍在台北大巨蛋6比0完封中信兄弟,系列賽4勝2敗,拿下中華職棒2026年度總冠軍。這是中職史上第一場「龍象大戰」,也是味全龍隊史第6座總冠軍。")
f.para("第六戰的英雄是先發投手梅賽鍶。他先發8局,只被敲出2支安打,送出6次三振,沒有失分。3局下,張政禹擊出安打,先幫龍隊拿下1分。8局下,郭天信、張政禹、劉基鴻、朱育賢連續安打,加上蔣少宏的兩分全壘打,龍隊單局拿下5分,比賽就此底定。6比0完封兄弟，龍隊拋下紅色彩帶。")
f.para("梅賽鍶獲選台灣大賽最有價值球員:他在台灣大賽2場先發,14局只掉1分,完全封鎖對手。更厲害的是,龍隊在這個系列賽3度完封對手,是單一台灣大賽史上第一次。")
f.gloss("Os Wei Chuan Dragons venceram os CTBC Brothers por 6 a 0 no 6.º jogo (26 de outubro, Domo de Taipé) e conquistaram a Série de Taiwan 2026 por 4 a 2 — a primeira final Dragons–Brothers da história e o 6.º título dos Dragons. O arremessador titular C.C. Mercedes lançou 8 entradas sem sofrer pontos e foi eleito o MVP da série.")
f.title("棒球詞卡 · Palavras", 34)
f.para("完封:對手得0分,叫完封。封王:拿下總冠軍,叫封王。全壘打:一棒打出場外,叫全壘打。最有價值球員:系列賽表現最好的人,英文叫 MVP。")
f.gloss("Quatro palavras: 完封 (jogo sem sofrer pontos), 封王 (conquistar o título), 全壘打 (home run), MVP (jogador mais valioso).")
f.end_report()

# ---- chart: Game 6 runs by inning (innings 1-8; bottom 9th not played) ----
chy = 1070
p.hline(MX, COLX[0] + 3 * CW + 2 * GUT, chy - 18, GOLD, 2)
p.text(MX, chy + 28, "第六戰得分走勢 · Pontos do 6.º jogo por entrada — barras proporcionais aos pontos", 27, "sans", True, OLIVE)
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
p.text(MX, chart_end + 56, "Nota: os Dragons não rebateram na parte baixa da 9.ª entrada — vencendo por 6 a 0 após a parte alta da 9.ª, o jogo estava encerrado. 1 + 5 = 6.", 20, "sans", False, GREY)

e = Flow(p, [(COLX[i], CW) for i in range(3)], int(chart_end) + 64, 2540, tag="P4-ex")
e.head("讀懂了嗎? · Entendeu?", 26)
e.ex("B1", "單選", "B", "Os Dragons venceram o 6.º jogo por 6 a 0.",
     "台灣大賽第六戰,比數是多少?", opts=["A. 3比0", "B. 6比0", "C. 6比3"], size=21.5, gap=6)
e.ex("B1", "單選", "C", "A série terminou 4 a 2 para os Dragons.",
     "系列賽最後是幾勝幾敗?", opts=["A. 4勝0敗", "B. 4勝1敗", "C. 4勝2敗"], size=21.5, gap=6)
e.ex("B1", "單選", "A", "Mercedes lançou 8 entradas sem sofrer pontos.",
     "梅賽鍶先發幾局、失幾分?", opts=["A. 8局、0分", "B. 7局、1分", "C. 9局、2分"], size=21.5, gap=6)
e.ex("B1", "單選", "B", "Mercedes foi eleito o MVP da série.",
     "台灣大賽最有價值球員是誰?", opts=["A. 蔣少宏", "B. 梅賽鍶", "C. 張政禹"], size=21.5, gap=6)
e.ex("B1", "單選", "A", "O 6.º título dos Dragons na história do time.",
     "這是味全龍隊史第幾座總冠軍?", opts=["A. 第6座", "B. 第4座", "C. 第3座"], size=21.5, gap=6)
e.ex("B1", "單選", "C", "Três jogos sem sofrer pontos em uma mesma série é algo inédito.",
     "龍隊在系列賽幾度完封對手?", opts=["A. 1度", "B. 2度", "C. 3度"], size=21.5, gap=6)
e.head("填一填 · Complete", 28)
e.ex("B1", "完成句子", "大巨蛋", "O 6.º jogo foi disputado no Domo de Taipé.",
     "第六戰在台北___舉行。", instr="Complete", size=21.5, gap=6)
e.ex("B1", "完成句子", "完封", "Um jogo sem sofrer pontos: o adversário marca zero.",
     "對手得0分,叫___。", instr="Complete", size=21.5, gap=6)
e.ex("B1", "完成句子", "封王", "Conquistar o título é fēng wáng.",
     "拿下總冠軍,叫___。", instr="Complete", size=21.5, gap=6)
e.ex("B1", "完成句子", "全壘打", "Uma bola rebatida para fora do campo é um home run.",
     "蔣少宏擊出兩分___。", instr="Complete", size=21.5, gap=6)
e.ex("B1", "完成句子", "14", "Mercedes cedeu 1 ponto em 14 entradas.",
     "梅賽鍶2場先發,___局只掉1分。", instr="Complete", size=21.5, gap=6)
e.ex("B1", "完成句子", "5", "Os Dragons marcaram 5 pontos na 8.ª entrada.",
     "龍隊8局下拿下___分。", instr="Complete", size=21.5, gap=6)
e.head("看圖答題 · Leia o gráfico", 28)
e.ex("B1", "單選", "B", "A 8.ª entrada: 5 pontos, a maior barra.",
     "龍隊哪一局得分最多?", opts=["A. 3局下", "B. 8局下", "C. 9局下"], size=21.5, gap=6)
e.ex("B1", "單選", "A", "1 + 5 = 6 pontos no total.",
     "3局下和8局下加起來是幾分?", opts=["A. 6分", "B. 5分", "C. 8分"], size=21.5, gap=6)
e.match_set("B1", "配對",
            ["完封", "封王", "全壘打", "安打"],
            ["對手得0分", "拿下總冠軍", "一棒打出場外", "打者把球打到場內形成上壘"],
            ["a", "b", "c", "d"],
            ["wánfēng — jogo sem sofrer pontos: o adversário marca zero.",
             "fēng wáng — conquistar o campeonato.",
             "quánlěidǎ — um home run.",
             "āndǎ — uma rebatida."],
            instr="Associe nome e informação")
e.end_report()

rx = COLX[3]
image(p, "baseball.jpg", rx, 208, CW, 300)
caption(p, rx, 208 + 300 + 6, CW, "棒球舊照(資料照片)。第六戰,龍隊8局下連續安打,奠定勝基。",
        "Photo: Bain News Service — Public domain (Wikimedia Commons)")
by = 208 + 300 + 132
p.rect(rx, by, CW, 470, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "系列賽小檔 · Ficha da série", 25, "sans", True, OLIVE); yy += 56
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
p.text(rx + 22, yy + 26, "你呢? · E você?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你支持哪一隊?你看過現場棒球賽嗎?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Para que time você torce? Você já assistiu a um jogo de beisebol ao vivo?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
