# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zhtw-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P3 · culture
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · Culture", "Lucerna", "第 3 版 · 重陽節與大閘蟹 · La Fête du Double Neuf et la saison du crabe poilu")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P3-main")
f.title("重陽節:登高、敬老、吃紅龜粿", 34)
f.para("昨天(10月18日,週日)是農曆九月初九,重陽節。「九」和「久」的聲音很像,所以重陽是祝長輩長壽、健康的日子。")
f.para("重陽的老習俗很多:登高(爬山,看遠方)、插茱萸(古人說可以避邪)、賞菊、飲菊花酒。台北的碧湖步道,這個週末都是登高的人。爬上山,看看遠方——登高望遠,人也精神了。")
f.para("台灣過重陽,「敬老」的味道最濃。各縣市辦敬老活動,像高雄都會公園10月17日的重陽敬老嘉年華。家裡祭祖,會準備一整隻雞和紅龜粿:紅色的粿,祝長輩長壽又平安。")
f.gloss("La Fête du Double Neuf (9e jour du 9e mois lunaire) est tombée le dimanche 18 octobre. On monte sur les hauteurs, on admire les chrysanthèmes et on honore les aînés ; les familles taïwanaises offrent à leurs ancêtres un poulet entier et des gâteaux tortues rouges.")
f.title("香港的重陽:放假、登高、掃墓", 34)
f.para("香港把重陽節定為法定假日。今年正日是週日,所以週一(10月19日)多放一天,叫「重陽節翌日」公眾假期。香港人這一天登高,也掃墓祭祖。台灣的重陽不是假日,兩地過法,有一點不一樣。")
f.title("大閘蟹上場:九雌十雄", 34)
f.para("秋風一起,大閘蟹的季節就到了。吃蟹有句老話:「九雌十雄」。農曆九月吃蟹乸,農曆十月吃蟹公。農曆九月(大約10月)的雌蟹,蟹黃多、最肥;再過一個月,換雄蟹的蟹膏上場。")
f.para("蒸蟹要看大小:3両的蟹,蒸約12分鐘;4両的蟹,蒸約15分鐘。吃的時候配薑醋,吃完喝一杯薑茶,肚子暖暖的。")
f.para("香港的食府這個月都推蟹宴。尖沙咀「胡同」的大閘蟹菜單今天(10月19日)開始,做到11月30日,清蒸大閘蟹每隻498港幣;美利酒店的蟹宴晚宴,每位798港幣。想吃蟹,這個月最對時。")
f.gloss("La saison du crabe poilu bat son plein : les femelles (蟹乸) aux œufs riches au 9e mois lunaire, les mâles (蟹公) le mois suivant. Un crabe de 3 taels cuit environ 12 minutes à la vapeur, un crabe de 4 taels environ 15.")
f.title("短訊:臺北時裝週剛落幕", 34)
f.para("上週末(10月15日到18日),臺北時裝週 SS27 在空總舉行,剛剛落幕。看秀、看展的人很多;下一個城裡的大活動,就是本週的金鐘獎了(見第5版)。")
f.head("讀懂了嗎? · Tout compris ?", 28)
f.ex("A2", "單選", "A", "Le Double Neuf est le 9e jour du 9e mois lunaire.",
     "重陽節是農曆幾月幾日?", opts=["A. 九月初九", "B. 五月初五", "C. 八月十五"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "Cette année, il est tombé le dimanche 18 octobre.",
     "今年的重陽節是星期幾?", opts=["A. 週六", "B. 週日", "C. 週一"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "La fête tombait un dimanche, le lundi est donc devenu férié.",
     "香港的重陽假期為什麼在週一?", opts=["A. 正日逢週日,翌日補假", "B. 老闆多送一天", "C. 學校自己放假"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "Les familles offrent un poulet entier et des gâteaux tortues rouges.",
     "台灣祭祖會準備什麼?", opts=["A. 月餅和茶", "B. 粽子和湯圓", "C. 整隻雞和紅龜粿"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "Au 9e mois lunaire, ce sont les femelles qui sont au mieux.",
     "農曆九月,先吃哪種蟹?", opts=["A. 蟹公", "B. 蟹乸", "C. 小蟹"], size=22.5, gap=8)
f.head("填一填 · Complétez", 28)
f.ex("A2", "完成句子", "登高", "Monter en hauteur : la coutume classique du Double Neuf.",
     "重陽節爬山看遠方,叫作「___」。", instr="Complétez", size=22.5, gap=8)
f.ex("A2", "完成句子", "茱萸", "On portait des brins de zhuyu pour éloigner le mal.",
     "古人重陽插___,說可以避邪。", instr="Complétez", size=22.5, gap=8)
f.ex("A2", "完成句子", "菊花", "Le vin de chrysanthème se boit pendant la fête.",
     "重陽飲___酒,還要賞菊。", instr="Complétez", size=22.5, gap=8)
f.ex("A2", "完成句子", "紅龜", "Les gâteaux tortues rouges souhaitent une longue vie aux aînés.",
     "祭祖的粿是紅色的,叫___粿。", instr="Complétez", size=22.5, gap=8)
f.ex("A2", "完成句子", "敬老", "La fête honore aussi les personnes âgées.",
     "重陽節要___長輩,祝他們長壽。", instr="Complétez", size=22.5, gap=8)
f.match_set("B1", "配對",
            ["蟹乸", "蟹公", "薑茶", "両"],
            ["雌蟹,農曆九月蟹黃多、最肥", "雄蟹,農曆十月吃蟹膏", "吃蟹後喝一杯,肚子暖暖的", "計算蟹重的單位"],
            ["a", "b", "c", "d"],
            ["蟹乸 — la femelle, au mieux au 9e mois lunaire.",
             "蟹公 — le mâle, mangé pour sa pâte au 10e mois lunaire.",
             "薑茶 — un thé au gingembre après le crabe, pour réchauffer l'estomac.",
             "両 — le tael, l'unité de poids des crabes."],
            instr="Associez")
f.head("算一算 · À vos calculs", 28)
f.ex("B1", "單選", "B", "15 - 12 = 3 minutes de plus pour le plus gros crabe.",
     "4両的蟹比3両的蟹多蒸幾分鐘?", opts=["A. 2分鐘", "B. 3分鐘", "C. 5分鐘"], size=22.5, gap=8)
f.ex("B1", "完成句子", "996", "498 HK$ x 2 = 996 HK$.",
     "胡同清蒸大閘蟹每隻498港幣,兩隻一共___港幣。", instr="Complétez", size=22.5, gap=8)
f.ex("B1", "單選", "B", "798 - 498 = 300 dollars de Hong Kong de plus.",
     "美利酒店蟹宴每位798港幣,比胡同一隻蟹貴多少?", opts=["A. 200港幣", "B. 300港幣", "C. 398港幣"], size=22.5, gap=8)
f.ex("B1", "完成句子", "十", "Les mâles arrivent en saison au 10e mois lunaire.",
     "「九雌十雄」:雄蟹要等到農曆___月。", instr="Complétez", size=22.5, gap=8)
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
    "登高 — monter sur une hauteur et regarder au loin",
    "茱萸 — un brin porté sur soi pour éloigner le mal",
    "菊花酒 — le vin de chrysanthème bu pendant la fête",
    "敬老 — honorer et prendre soin des aînés",
    "蟹季 — saison du crabe : le menu crabe de Hutong commence le 19 octobre",
]
kwh = 18 + 56 + sum(24 + len(wrap("· " + t, "serif", False, 22.5, CW - 44)) * 22.5 * 1.32 + 8 for t in kw) - 8 + 16
p.rect(rx, by, CW, kwh, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "重陽關鍵詞 · Mots-clés", 25, "sans", True, OLIVE); yy += 56
for t in kw:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + kwh + 18, CW, 220, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + kwh + 18 + 18
p.text(rx + 22, yy + 26, "你呢? · À vous", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你家過節會吃什麼特別的東西?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Quel plat spécial votre famille mange-t-elle les jours de fête ?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ============================================================ P4 · sport
CURPAGE[0] = 4
p = BSPage4()
p.band("體育 · Sport", "Lucerna", "第 4 版 · 台灣大賽「龍象大戰」 · La Série de Taïwan : Dragons contre Brothers")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P4-main")
f.title("龍象大戰:總冠軍本週出爐?", 34)
f.para("中華職棒一年的總冠軍賽「台灣大賽」開打了。今年是球迷等了很久的「龍象大戰」:味全龍對中信兄弟——中職最有歷史、氣氛最緊張的對戰組合。")
f.para("兩隊怎麼來的?味全龍是上半季冠軍,全年勝率第一,直接晉級;中信兄弟先打贏了季後挑戰賽,才拿到台灣大賽的門票。賽制是七戰四勝:先贏四場的隊伍,就是今年的總冠軍。")
f.para("第一戰上週六(10月17日)在臺北大巨蛋打完:味全龍3比0完封兄弟,全場4萬人,坐得滿滿的。前兩戰在上週末打完;本週二起,第三戰開始,全部比賽都在大巨蛋舉行,緯來體育台全系列轉播。")
f.gloss("La Série de Taïwan se joue au meilleur des sept matchs : la première équipe à quatre victoires remporte le titre. Les Dragons ont blanchi les Brothers 3 à 0 lors du match 1, devant 40 000 spectateurs au Dôme de Taipei.")
f.box("本週賽程 · Les matchs de la semaine", [
    ("G1 · 10月17日(六) 味全龍 3:0 中信兄弟(已打完)", "serif", False, INK, 22.5, 1.35),
    ("G3 · 10月20日(二)", "serif", False, INK, 22.5, 1.35),
    ("G4 · 10月21日(三)", "serif", False, INK, 22.5, 1.35),
    ("G5 · 10月23日(五) 如有需要", "serif", False, INK, 22.5, 1.35),
    ("G6 · 10月24日(六) 如有需要", "serif", False, INK, 22.5, 1.35),
    ("G7 · 10月25日(日) 如有需要", "serif", False, INK, 22.5, 1.35),
    ("La première équipe à quatre victoires prend le titre — les matchs 5 à 7 ne seront peut-être pas nécessaires.", "sans", False, GREY, 20, 1.35),
])
f.title("看球先學四個詞", 34)
f.para("Quatre mots avant de regarder : « 完封 » — un blanchissage : l'équipe adverse ne marque rien de tout le match, comme le 3 à 0 du match 1. « 封王 » — décrocher le titre : gagner le match qui décide du championnat. « 滿場 » — guichets fermés : tous les billets vendus, toutes les places prises. « 如有需要 » — « si nécessaire » : si une équipe a déjà gagné quatre matchs, les suivants ne se jouent pas.")
f.title("在家看轉播,也像在球場", 34)
f.para("買不到票也沒關係:緯來體育台全系列轉播,在家也能看。第一戰大巨蛋坐了4萬人,更多人在電視和手機前面看。看轉播學中文很快:主播會一直說「安打」「三振」「全壘打」,聽幾場,棒球的詞就記住了。")
f.gloss("Pas de billet ? Toute la série passe à la télévision. Écouter les commentateurs est un moyen rapide d'apprendre les mots du baseball : 安打 (un coup sûr), 三振 (un retrait sur prises), 全壘打 (un coup de circuit).")
f.head("讀懂了嗎? · Tout compris ?", 28)
f.ex("B1", "單選", "A", "Les Dragons sont champions de la première moitié de saison, meilleur bilan global.",
     "味全龍怎麼晉級台灣大賽?", opts=["A. 上半季冠軍", "B. 抽籤抽到", "C. 去年冠軍保送"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Les Brothers ont d'abord remporté la série de qualification.",
     "中信兄弟先打贏了什麼比賽?", opts=["A. 季後挑戰賽", "B. 明星賽", "C. 熱身賽"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Tous les matchs de la série se jouent au Dôme de Taipei.",
     "台灣大賽全部在哪裡打?", opts=["A. 臺北大巨蛋", "B. 台中洲際棒球場", "C. 高雄澄清湖球場"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Match 1 : Dragons 3, Brothers 0.",
     "第一戰的比數是?", opts=["A. 味全龍3:0中信兄弟", "B. 中信兄弟3:0味全龍", "C. 味全龍4:3中信兄弟"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Un blanchissage signifie que l'adversaire marque zéro.",
     "「完封」是什麼意思?", opts=["A. 對手得0分", "B. 比賽因雨取消", "C. 打滿十局"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Videoland Sports retransmet toute la série.",
     "哪一台轉播全系列比賽?", opts=["A. 緯來體育台", "B. 迪士尼頻道", "C. 購物台"], size=22.5, gap=8)
f.head("看賽程表 · Le calendrier", 28)
f.ex("B1", "單選", "B", "Le match 4 a lieu le mercredi 21 octobre.",
     "第四戰 G4 在哪一天?", opts=["A. 10月20日(二)", "B. 10月21日(三)", "C. 10月23日(五)"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Les matchs suivants sont sautés dès qu'une équipe atteint quatre victoires.",
     "G5為什麼寫「如有需要」?", opts=["A. 可能已經有人封王", "B. 場地還沒決定", "C. 門票還沒開賣"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Seuls les matchs 3 et 4 sont certains cette semaine.",
     "本週確定要打的比賽有幾場?", opts=["A. 2場", "B. 3場", "C. 5場"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "La série peut aller jusqu'au match 7, dimanche.",
     "本週最多打到第幾戰?", opts=["A. G5", "B. G6", "C. G7"], size=22.5, gap=8)
f.head("填一填 · Complétez", 28)
f.ex("B1", "完成句子", "4", "Quatre victoires donnent le titre, au meilleur des sept.",
     "七戰四勝:先贏___場,就是總冠軍。", instr="Complétez", size=22.5, gap=8)
f.ex("B1", "完成句子", "完封", "Un blanchissage : les adversaires ne marquent rien.",
     "對手整場一分未得,叫作___。", instr="Complétez", size=22.5, gap=8)
f.ex("B1", "完成句子", "滿場", "Guichets fermés : toutes les places sont prises.",
     "票全賣完、場內坐滿人,叫作___。", instr="Complétez", size=22.5, gap=8)
f.ex("B1", "完成句子", "封王", "Décrocher le titre du championnat, c'est 封王.",
     "贏下決定冠軍的那一場,叫作___。", instr="Complétez", size=22.5, gap=8)
f.match_set("B1", "配對",
            ["味全龍", "中信兄弟", "臺北大巨蛋", "緯來體育台"],
            ["上半季冠軍、全年勝率第一", "季後挑戰賽勝出", "全部場次的球場", "全系列轉播的電視台"],
            ["a", "b", "c", "d"],
            ["味全龍 — champions de la première moitié, meilleur bilan global.",
             "中信兄弟 — passés par la série de qualification.",
             "臺北大巨蛋 — le dôme qui accueille tous les matchs.",
             "緯來體育台 — la chaîne qui retransmet toute la série."],
            instr="Associez")
f.end_report()

rx = COLX[3]
image(p, "baseball.jpg", rx, 208, CW, 620)
caption(p, rx, 208 + 620 + 6, CW, "打者全力揮棒(資料照片)。",
        "Photo: unknown author — Public domain (Wikimedia Commons)")
by = 208 + 620 + 100
wc = [
    "完封 (blanchissage) — l'adversaire ne marque rien",
    "封王 (décrocher le titre) — gagner le match décisif",
    "滿場 (guichets fermés) — toutes les places prises",
    "七戰四勝 (au meilleur des sept) — la première équipe à quatre victoires",
]
wch = 18 + 56 + sum(24 + len(wrap("· " + t, "serif", False, 22.5, CW - 44)) * 22.5 * 1.32 + 8 for t in wc) - 8 + 16
p.rect(rx, by, CW, wch, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "棒球詞卡 · Cartes de mots", 25, "sans", True, OLIVE); yy += 56
for t in wc:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + wch + 18, CW, 220, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + wch + 18 + 18
p.text(rx + 22, yy + 26, "你呢? · À vous", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你支持哪一隊?你看過現場的棒球賽嗎?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Dragons ou Brothers — quelle est votre équipe ?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
