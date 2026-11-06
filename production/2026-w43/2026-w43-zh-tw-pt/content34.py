# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P3 · culture
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · Cultura", "Lucerna", "第 3 版 · 重陽節與大閘蟹 · O Duplo Nove e a temporada do caranguejo-peludo")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P3-main")
f.title("重陽節:登高、敬老、吃紅龜粿", 34)
f.para("昨天(10月18日,週日)是農曆九月初九,重陽節。「九」和「久」的聲音很像,所以重陽是祝長輩長壽、健康的日子。")
f.para("重陽的老習俗很多:登高(爬山,看遠方)、插茱萸(古人說可以避邪)、賞菊、飲菊花酒。台北的碧湖步道,這個週末都是登高的人。爬上山,看看遠方——登高望遠,人也精神了。")
f.para("台灣過重陽,「敬老」的味道最濃。各縣市辦敬老活動,像高雄都會公園10月17日的重陽敬老嘉年華。家裡祭祖,會準備一整隻雞和紅龜粿:紅色的粿,祝長輩長壽又平安。")
f.gloss("O Duplo Nove (dia 9 do 9.º mês lunar) caiu no domingo, 18 de outubro. As pessoas sobem colinas, admiram crisântemos e honram os mais velhos; as famílias taiwanesas oferecem aos antepassados um frango inteiro e bolos vermelhos em forma de tartaruga.")
f.title("香港的重陽:放假、登高、掃墓", 34)
f.para("香港把重陽節定為法定假日。今年正日是週日,所以週一(10月19日)多放一天,叫「重陽節翌日」公眾假期。香港人這一天登高,也掃墓祭祖。台灣的重陽不是假日,兩地過法,有一點不一樣。")
f.title("大閘蟹上場:九雌十雄", 34)
f.para("秋風一起,大閘蟹的季節就到了。吃蟹有句老話:「九雌十雄」。農曆九月吃蟹乸,農曆十月吃蟹公。農曆九月(大約10月)的雌蟹,蟹黃多、最肥;再過一個月,換雄蟹的蟹膏上場。")
f.para("蒸蟹要看大小:3両的蟹,蒸約12分鐘;4両的蟹,蒸約15分鐘。吃的時候配薑醋,吃完喝一杯薑茶,肚子暖暖的。")
f.para("香港的食府這個月都推蟹宴。尖沙咀「胡同」的大閘蟹菜單今天(10月19日)開始,做到11月30日,清蒸大閘蟹每隻498港幣;美利酒店的蟹宴晚宴,每位798港幣。想吃蟹,這個月最對時。")
f.gloss("A temporada do caranguejo-peludo está no auge: as fêmeas (蟹乸), ricas em ovas, no 9.º mês lunar; os machos (蟹公) no mês seguinte. Um caranguejo de 3 taéis cozinha no vapor por cerca de 12 minutos; um de 4 taéis, cerca de 15.")
f.title("短訊:臺北時裝週剛落幕", 34)
f.para("上週末(10月15日到18日),臺北時裝週 SS27 在空總舉行,剛剛落幕。看秀、看展的人很多;下一個城裡的大活動,就是本週的金鐘獎了(見第5版)。")
f.head("讀懂了嗎? · Entendeu?", 28)
f.ex("A2", "單選", "A", "O Duplo Nove é o dia 9 do 9.º mês lunar.",
     "重陽節是農曆幾月幾日?", opts=["A. 九月初九", "B. 五月初五", "C. 八月十五"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "Este ano caiu no domingo, 18 de outubro.",
     "今年的重陽節是星期幾?", opts=["A. 週六", "B. 週日", "C. 週一"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "A festa caiu no domingo, então a segunda virou feriado.",
     "香港的重陽假期為什麼在週一?", opts=["A. 正日逢週日,翌日補假", "B. 老闆多送一天", "C. 學校自己放假"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "As famílias oferecem um frango inteiro e bolos vermelhos de tartaruga.",
     "台灣祭祖會準備什麼?", opts=["A. 月餅和茶", "B. 粽子和湯圓", "C. 整隻雞和紅龜粿"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "No 9.º mês lunar, as fêmeas do caranguejo estão no melhor momento.",
     "農曆九月,先吃哪種蟹?", opts=["A. 蟹公", "B. 蟹乸", "C. 小蟹"], size=22.5, gap=8)
f.head("填一填 · Complete", 28)
f.ex("A2", "完成句子", "登高", "Subir bem alto é o costume clássico do Duplo Nove.",
     "重陽節爬山看遠方,叫作「___」。", instr="Complete", size=22.5, gap=8)
f.ex("A2", "完成句子", "茱萸", "Usavam-se raminhos de zhūyú para afastar o mal.",
     "古人重陽插___,說可以避邪。", instr="Complete", size=22.5, gap=8)
f.ex("A2", "完成句子", "菊花", "Na festa bebe-se vinho de crisântemo.",
     "重陽飲___酒,還要賞菊。", instr="Complete", size=22.5, gap=8)
f.ex("A2", "完成句子", "紅龜", "Os bolos vermelhos de tartaruga desejam vida longa aos mais velhos.",
     "祭祖的粿是紅色的,叫___粿。", instr="Complete", size=22.5, gap=8)
f.ex("A2", "完成句子", "敬老", "A festa também é sobre respeitar os mais velhos.",
     "重陽節要___長輩,祝他們長壽。", instr="Complete", size=22.5, gap=8)
f.match_set("B1", "配對",
            ["蟹乸", "蟹公", "薑茶", "両"],
            ["雌蟹,農曆九月蟹黃多、最肥", "雄蟹,農曆十月吃蟹膏", "吃蟹後喝一杯,肚子暖暖的", "計算蟹重的單位"],
            ["a", "b", "c", "d"],
            ["Xiè nǎ — a fêmea do caranguejo, no melhor momento no 9.º mês lunar.",
             "Xiè gōng — o macho, comido pela sua pasta no 10.º mês lunar.",
             "Jiāng chá — chá de gengibre depois do caranguejo, para aquecer o estômago.",
             "Liǎng — o tael, a unidade em que se pesam os caranguejos."],
            instr="Associe palavra e definição")
f.head("算一算 · Faça as contas", 28)
f.ex("B1", "單選", "B", "15 - 12 = 3 minutos a mais para o caranguejo maior.",
     "4両的蟹比3両的蟹多蒸幾分鐘?", opts=["A. 2分鐘", "B. 3分鐘", "C. 5分鐘"], size=22.5, gap=8)
f.ex("B1", "完成句子", "996", "HK$ 498 × 2 = HK$ 996.",
     "胡同清蒸大閘蟹每隻498港幣,兩隻一共___港幣。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "單選", "B", "798 - 498 = 300 dólares de Hong Kong a mais.",
     "美利酒店蟹宴每位798港幣,比胡同一隻蟹貴多少?", opts=["A. 200港幣", "B. 300港幣", "C. 398港幣"], size=22.5, gap=8)
f.ex("B1", "完成句子", "十", "Os machos entram na temporada no 10.º mês lunar.",
     "「九雌十雄」:雄蟹要等到農曆___月。", instr="Complete", size=22.5, gap=8)
f.end_report()

rx = COLX[3]
image(p, "chrysanthemum.jpg", rx, 208, CW, 300)
cy = caption(p, rx, 208 + 300 + 6, CW, "重陽賞菊:菊花是長壽的花。",
             "Photo: Masaki Ikeda (池田正樹) — Public domain (Wikimedia Commons)")
iy2 = int(cy) + 18
image(p, "crab.jpg", rx, iy2, CW, 300)
cy2 = caption(p, rx, iy2 + 300 + 6, CW, "切開的大閘蟹:看,金黃色的蟹黃。",
              "Photo: Fumikas Sagisavas — CC0 (Wikimedia Commons)")
by = int(cy2) + 18
kw = [
    "登高 — subir uma colina e olhar longe",
    "茱萸 — um raminho usado no corpo para afastar o mal",
    "菊花酒 — o vinho de crisântemo bebido na festa",
    "敬老 — honrar e cuidar dos mais velhos",
    "蟹季 — temporada do caranguejo: o menu de caranguejo do Hutong começa em 19 de outubro",
]
kwh = 18 + 56 + sum(24 + len(wrap("· " + t, "serif", False, 22.5, CW - 44)) * 22.5 * 1.32 + 8 for t in kw) - 8 + 16
p.rect(rx, by, CW, kwh, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "重陽關鍵詞 · Palavras-chave", 25, "sans", True, OLIVE); yy += 56
for t in kw:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + kwh + 18, CW, 220, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + kwh + 18 + 18
p.text(rx + 22, yy + 26, "你呢? · E você?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你家過節會吃什麼特別的東西?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Que comida especial a sua família come nos dias de festa?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ============================================================ P4 · sport
CURPAGE[0] = 4
p = BSPage4()
p.band("體育 · Sport", "Lucerna", "第 4 版 · 台灣大賽「龍象大戰」 · A Série de Taiwan: Dragons contra Brothers")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P4-main")
f.title("龍象大戰:總冠軍本週出爐?", 34)
f.para("中華職棒一年的總冠軍賽「台灣大賽」開打了。今年是球迷等了很久的「龍象大戰」:味全龍對中信兄弟——中職最有歷史、氣氛最緊張的對戰組合。")
f.para("兩隊怎麼來的?味全龍是上半季冠軍,全年勝率第一,直接晉級;中信兄弟先打贏了季後挑戰賽,才拿到台灣大賽的門票。賽制是七戰四勝:先贏四場的隊伍,就是今年的總冠軍。")
f.para("第一戰上週六(10月17日)在臺北大巨蛋打完:味全龍3比0完封兄弟,全場4萬人,坐得滿滿的。前兩戰在上週末打完;本週二起,第三戰開始,全部比賽都在大巨蛋舉行,緯來體育台全系列轉播。")
f.gloss("A Série de Taiwan é uma melhor de sete: o primeiro time a somar quatro vitórias fica com o título. Os Dragons venceram os Brothers por 3 a 0 no Jogo 1, diante de 40.000 torcedores no Taipei Dome.")
f.box("本週賽程 · Jogos", [
    ("G1 · 10月17日(六) 味全龍 3:0 中信兄弟(已打完)", "serif", False, INK, 22.5, 1.35),
    ("G3 · 10月20日(二)", "serif", False, INK, 22.5, 1.35),
    ("G4 · 10月21日(三)", "serif", False, INK, 22.5, 1.35),
    ("G5 · 10月23日(五) 如有需要", "serif", False, INK, 22.5, 1.35),
    ("G6 · 10月24日(六) 如有需要", "serif", False, INK, 22.5, 1.35),
    ("G7 · 10月25日(日) 如有需要", "serif", False, INK, 22.5, 1.35),
    ("Quem chegar primeiro a quatro vitórias fica com o título — os Jogos 5 a 7 podem nem ser necessários.", "sans", False, GREY, 20, 1.35),
])
f.title("看球先學四個詞", 34)
f.para("Quatro palavras antes de assistir: «完封» — um shutout: o outro time não marca nada o jogo todo, como o 3 a 0 do Jogo 1. «封王» — conquistar o título: vencer o jogo que decide o campeonato. «滿場» — casa cheia: todos os ingressos vendidos, todos os lugares ocupados. «如有需要» — «se necessário»: se um time já venceu quatro, os jogos seguintes não acontecem.")
f.title("在家看轉播,也像在球場", 34)
f.para("買不到票也沒關係:緯來體育台全系列轉播,在家也能看。第一戰大巨蛋坐了4萬人,更多人在電視和手機前面看。看轉播學中文很快:主播會一直說「安打」「三振」「全壘打」,聽幾場,棒球的詞就記住了。")
f.gloss("Sem ingresso? A série inteira passa na TV. Ouvir os comentaristas é um jeito rápido de aprender palavras de beisebol: 安打 (uma rebatida), 三振 (um strikeout), 全壘打 (um home run).")
f.head("讀懂了嗎? · Entendeu?", 28)
f.ex("B1", "單選", "A", "Os Dragons são os campeões do primeiro turno, melhor campanha geral.",
     "味全龍怎麼晉級台灣大賽?", opts=["A. 上半季冠軍", "B. 抽籤抽到", "C. 去年冠軍保送"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Os Brothers passaram antes pela Série de Desafio.",
     "中信兄弟先打贏了什麼比賽?", opts=["A. 季後挑戰賽", "B. 明星賽", "C. 熱身賽"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Todos os jogos da série são no Taipei Dome.",
     "台灣大賽全部在哪裡打?", opts=["A. 臺北大巨蛋", "B. 台中洲際棒球場", "C. 高雄澄清湖球場"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Jogo 1: Dragons 3, Brothers 0.",
     "第一戰的比數是?", opts=["A. 味全龍3:0中信兄弟", "B. 中信兄弟3:0味全龍", "C. 味全龍4:3中信兄弟"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Um shutout significa que o outro time marca zero.",
     "「完封」是什麼意思?", opts=["A. 對手得0分", "B. 比賽因雨取消", "C. 打滿十局"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "A Videoland Sports transmite a série inteira.",
     "哪一台轉播全系列比賽?", opts=["A. 緯來體育台", "B. 迪士尼頻道", "C. 購物台"], size=22.5, gap=8)
f.head("看賽程表 · A tabela", 28)
f.ex("B1", "單選", "B", "O Jogo 4 é na quarta-feira, 21 de outubro.",
     "第四戰 G4 在哪一天?", opts=["A. 10月20日(二)", "B. 10月21日(三)", "C. 10月23日(五)"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Os jogos seguintes são cancelados quando um time chega a quatro vitórias.",
     "G5為什麼寫「如有需要」?", opts=["A. 可能已經有人封王", "B. 場地還沒決定", "C. 門票還沒開賣"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Esta semana, só G3 e G4 são certos.",
     "本週確定要打的比賽有幾場?", opts=["A. 2場", "B. 3場", "C. 5場"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "A série pode ir até o Jogo 7, no domingo.",
     "本週最多打到第幾戰?", opts=["A. G5", "B. G6", "C. G7"], size=22.5, gap=8)
f.head("填一填 · Complete", 28)
f.ex("B1", "完成句子", "4", "Quatro vitórias dão o título numa melhor de sete.",
     "七戰四勝:先贏___場,就是總冠軍。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "完封", "Um shutout: os adversários não marcam nada.",
     "對手整場一分未得,叫作___。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "滿場", "Casa cheia: todos os lugares ocupados.",
     "票全賣完、場內坐滿人,叫作___。", instr="Complete", size=22.5, gap=8)
f.ex("B1", "完成句子", "封王", "Conquistar o título é fēng wáng.",
     "贏下決定冠軍的那一場,叫作___。", instr="Complete", size=22.5, gap=8)
f.match_set("B1", "配對",
            ["味全龍", "中信兄弟", "臺北大巨蛋", "緯來體育台"],
            ["上半季冠軍、全年勝率第一", "季後挑戰賽勝出", "全部場次的球場", "全系列轉播的電視台"],
            ["a", "b", "c", "d"],
            ["Wèiquán Lóng — campeões do primeiro turno, melhor campanha do ano.",
             "Zhōngxìn Xiōngdì — passaram pela Série de Desafio.",
             "Táiběi Dàjùdàn — o domo que recebe todos os jogos.",
             "Wěilái Tǐyù Tái — o canal que transmite a série inteira."],
            instr="Associe nome e informação")
f.end_report()

rx = COLX[3]
image(p, "baseball.jpg", rx, 208, CW, 620)
caption(p, rx, 208 + 620 + 6, CW, "打者全力揮棒(資料照片)。",
        "Photo: unknown author — Public domain (Wikimedia Commons)")
by = 208 + 620 + 100
wc = [
    "完封 (shutout) — o adversário não marca nada",
    "封王 (conquistar o título) — vencer o jogo decisivo",
    "滿場 (casa cheia) — todos os lugares ocupados",
    "七戰四勝 (melhor de sete) — quem chegar primeiro a quatro vence",
]
wch = 18 + 56 + sum(24 + len(wrap("· " + t, "serif", False, 22.5, CW - 44)) * 22.5 * 1.32 + 8 for t in wc) - 8 + 16
p.rect(rx, by, CW, wch, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "棒球詞卡 · Cartões de palavras", 25, "sans", True, OLIVE); yy += 56
for t in wc:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + wch + 18, CW, 220, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + wch + 18 + 18
p.text(rx + 22, yy + 26, "你呢? · E você?", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你支持哪一隊?你看過現場的棒球賽嗎?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Dragons ou Brothers — para qual time você torce?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
