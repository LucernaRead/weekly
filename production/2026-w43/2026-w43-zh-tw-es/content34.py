# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-tw-es/svg")
os.makedirs(OUT, exist_ok=True)

# ============================================================ P3 · culture
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · Cultura", "Lucerna", "第 3 版 · 重陽節與大閘蟹 · El Doble Nueve y la temporada del cangrejo peludo")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P3-main")
f.title("重陽節:登高、敬老、吃紅龜粿", 34)
f.para("昨天(10月18日,週日)是農曆九月初九,重陽節。「九」和「久」的聲音很像,所以重陽是祝長輩長壽、健康的日子。")
f.para("重陽的老習俗很多:登高(爬山,看遠方)、插茱萸(古人說可以避邪)、賞菊、飲菊花酒。台北的碧湖步道,這個週末都是登高的人。爬上山,看看遠方——登高望遠,人也精神了。")
f.para("台灣過重陽,「敬老」的味道最濃。各縣市辦敬老活動,像高雄都會公園10月17日的重陽敬老嘉年華。家裡祭祖,會準備一整隻雞和紅龜粿:紅色的粿,祝長輩長壽又平安。")
f.gloss("El Doble Nueve (día 9 del mes lunar 9) cayó el domingo 18 de octubre. La gente sube a los montes, admira los crisantemos y honra a sus mayores; las familias taiwanesas ofrecen a los antepasados un pollo entero y pasteles rojos de tortuga.")
f.title("香港的重陽:放假、登高、掃墓", 34)
f.para("香港把重陽節定為法定假日。今年正日是週日,所以週一(10月19日)多放一天,叫「重陽節翌日」公眾假期。香港人這一天登高,也掃墓祭祖。台灣的重陽不是假日,兩地過法,有一點不一樣。")
f.title("大閘蟹上場:九雌十雄", 34)
f.para("秋風一起,大閘蟹的季節就到了。吃蟹有句老話:「九雌十雄」。農曆九月吃蟹乸,農曆十月吃蟹公。農曆九月(大約10月)的雌蟹,蟹黃多、最肥;再過一個月,換雄蟹的蟹膏上場。")
f.para("蒸蟹要看大小:3両的蟹,蒸約12分鐘;4両的蟹,蒸約15分鐘。吃的時候配薑醋,吃完喝一杯薑茶,肚子暖暖的。")
f.para("香港的食府這個月都推蟹宴。尖沙咀「胡同」的大閘蟹菜單今天(10月19日)開始,做到11月30日,清蒸大閘蟹每隻498港幣;美利酒店的蟹宴晚宴,每位798港幣。想吃蟹,這個月最對時。")
f.gloss("La temporada del cangrejo peludo está en su cima: las hembras (蟹乸) con las huevas ricas en el mes lunar 9, los machos (蟹公) el mes que viene. Un cangrejo de 3 taels se cuece al vapor unos 12 minutos; uno de 4 taels, unos 15.")
f.title("短訊:臺北時裝週剛落幕", 34)
f.para("上週末(10月15日到18日),臺北時裝週 SS27 在空總舉行,剛剛落幕。看秀、看展的人很多;下一個城裡的大活動,就是本週的金鐘獎了(見第5版)。")
f.head("讀懂了嗎? · ¿Entendido?", 28)
f.ex("A2", "單選", "A", "El Doble Nueve es el día 9 del mes lunar 9.",
     "重陽節是農曆幾月幾日?", opts=["A. 九月初九", "B. 五月初五", "C. 八月十五"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "Este año cayó el domingo 18 de octubre.",
     "今年的重陽節是星期幾?", opts=["A. 週六", "B. 週日", "C. 週一"], size=22.5, gap=8)
f.ex("A2", "單選", "A", "La fiesta cayó en domingo, así que el lunes fue el día libre.",
     "香港的重陽假期為什麼在週一?", opts=["A. 正日逢週日,翌日補假", "B. 老闆多送一天", "C. 學校自己放假"], size=22.5, gap=8)
f.ex("A2", "單選", "C", "Las familias ofrecen un pollo entero y pasteles rojos de tortuga.",
     "台灣祭祖會準備什麼?", opts=["A. 月餅和茶", "B. 粽子和湯圓", "C. 整隻雞和紅龜粿"], size=22.5, gap=8)
f.ex("A2", "單選", "B", "En el mes lunar 9, las hembras están en su mejor momento.",
     "農曆九月,先吃哪種蟹?", opts=["A. 蟹公", "B. 蟹乸", "C. 小蟹"], size=22.5, gap=8)
f.head("填一填 · Completa", 28)
f.ex("A2", "完成句子", "登高", "Subir a lo alto es la costumbre clásica del Doble Nueve.",
     "重陽節爬山看遠方,叫作「___」。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "茱萸", "La gente llevaba ramitas de zhuyu para alejar el mal.",
     "古人重陽插___,說可以避邪。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "菊花", "En la fiesta se bebe vino de crisantemo.",
     "重陽飲___酒,還要賞菊。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "紅龜", "Los pasteles rojos de tortuga desean larga vida a los mayores.",
     "祭祖的粿是紅色的,叫___粿。", instr="Completa", size=22.5, gap=8)
f.ex("A2", "完成句子", "敬老", "La fiesta también honra a los mayores.",
     "重陽節要___長輩,祝他們長壽。", instr="Completa", size=22.5, gap=8)
f.match_set("B1", "配對",
            ["蟹乸", "蟹公", "薑茶", "両"],
            ["雌蟹,農曆九月蟹黃多、最肥", "雄蟹,農曆十月吃蟹膏", "吃蟹後喝一杯,肚子暖暖的", "計算蟹重的單位"],
            ["a", "b", "c", "d"],
            ["蟹乸 — la hembra, en su mejor momento en el mes lunar 9.",
             "蟹公 — el macho, que se come por su pasta en el mes lunar 10.",
             "薑茶 — té de jengibre tras el cangrejo, para calentar el estómago.",
             "両 — el tael, la unidad con que se pesan los cangrejos."],
            instr="Une palabra y definición")
f.head("算一算 · A calcular", 28)
f.ex("B1", "單選", "B", "15 - 12 = 3 minutos más para el cangrejo grande.",
     "4両的蟹比3両的蟹多蒸幾分鐘?", opts=["A. 2分鐘", "B. 3分鐘", "C. 5分鐘"], size=22.5, gap=8)
f.ex("B1", "完成句子", "996", "498 HK$ × 2 = 996 HK$.",
     "胡同清蒸大閘蟹每隻498港幣,兩隻一共___港幣。", instr="Completa", size=22.5, gap=8)
f.ex("B1", "單選", "B", "798 - 498 = 300 dólares de Hong Kong más.",
     "美利酒店蟹宴每位798港幣,比胡同一隻蟹貴多少?", opts=["A. 200港幣", "B. 300港幣", "C. 398港幣"], size=22.5, gap=8)
f.ex("B1", "完成句子", "十", "Los machos entran en temporada en el mes lunar 10.",
     "「九雌十雄」:雄蟹要等到農曆___月。", instr="Completa", size=22.5, gap=8)
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
    "登高 — subir a un monte y mirar a lo lejos",
    "茱萸 — una ramita que se lleva encima para alejar el mal",
    "菊花酒 — el vino de crisantemo que se bebe en la fiesta",
    "敬老 — honrar y cuidar a los mayores",
    "蟹季 — temporada del cangrejo: el menú de Hutong empieza el 19 de octubre",
]
kwh = 18 + 56 + sum(24 + len(wrap("· " + t, "serif", False, 22.5, CW - 44)) * 22.5 * 1.32 + 8 for t in kw) - 8 + 16
p.rect(rx, by, CW, kwh, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "重陽關鍵詞 · Palabras clave", 25, "sans", True, OLIVE); yy += 56
for t in kw:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + kwh + 18, CW, 220, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + kwh + 18 + 18
p.text(rx + 22, yy + 26, "你呢? · Ahora tú", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你家過節會吃什麼特別的東西?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "¿Qué comida especial come tu familia en los días de fiesta?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ============================================================ P4 · sport
CURPAGE[0] = 4
p = BSPage4()
p.band("體育 · Deportes", "Lucerna", "第 4 版 · 台灣大賽「龍象大戰」 · La Serie de Taiwán: Dragones contra Hermanos")
f = Flow(p, [(COLX[i], CW) for i in range(3)], 208, 2540, tag="P4-main")
f.title("龍象大戰:總冠軍本週出爐?", 34)
f.para("中華職棒一年的總冠軍賽「台灣大賽」開打了。今年是球迷等了很久的「龍象大戰」:味全龍對中信兄弟——中職最有歷史、氣氛最緊張的對戰組合。")
f.para("兩隊怎麼來的?味全龍是上半季冠軍,全年勝率第一,直接晉級;中信兄弟先打贏了季後挑戰賽,才拿到台灣大賽的門票。賽制是七戰四勝:先贏四場的隊伍,就是今年的總冠軍。")
f.para("第一戰上週六(10月17日)在臺北大巨蛋打完:味全龍3比0完封兄弟,全場4萬人,坐得滿滿的。前兩戰在上週末打完;本週二起,第三戰開始,全部比賽都在大巨蛋舉行,緯來體育台全系列轉播。")
f.gloss("La Serie de Taiwán es al mejor de siete: el primer equipo que gane cuatro partidos se lleva el título. Los Dragones dejaron en blanco a los Hermanos (3-0) en el partido 1, ante un lleno de 40.000 personas en el Domo de Taipéi.")
f.box("本週賽程 · Partidos", [
    ("G1 · 10月17日(六) 味全龍 3:0 中信兄弟(已打完)", "serif", False, INK, 22.5, 1.35),
    ("G3 · 10月20日(二)", "serif", False, INK, 22.5, 1.35),
    ("G4 · 10月21日(三)", "serif", False, INK, 22.5, 1.35),
    ("G5 · 10月23日(五) 如有需要", "serif", False, INK, 22.5, 1.35),
    ("G6 · 10月24日(六) 如有需要", "serif", False, INK, 22.5, 1.35),
    ("G7 · 10月25日(日) 如有需要", "serif", False, INK, 22.5, 1.35),
    ("El primero que llegue a cuatro victorias se lleva el título: quizá no hagan falta los partidos 5 a 7.", "sans", False, GREY, 20, 1.35),
])
f.title("看球先學四個詞", 34)
f.para("Cuatro palabras antes de verlo: «完封» — dejar en blanco: el otro equipo no anota en todo el partido, como el 3-0 del partido 1. «封王» — asegurarse el título: ganar el partido que decide el campeonato. «滿場» — lleno total: todos los boletos vendidos, todos los asientos ocupados. «如有需要» — «si es necesario»: si un equipo ya ganó cuatro, los partidos siguientes no se juegan.")
f.title("在家看轉播,也像在球場", 34)
f.para("買不到票也沒關係:緯來體育台全系列轉播,在家也能看。第一戰大巨蛋坐了4萬人,更多人在電視和手機前面看。看轉播學中文很快:主播會一直說「安打」「三振」「全壘打」,聽幾場,棒球的詞就記住了。")
f.gloss("¿Sin boleto? Toda la serie está en la tele. Escuchar a los comentaristas es una forma rápida de aprender palabras de béisbol: 安打 (un hit), 三振 (un ponche), 全壘打 (un jonrón).")
f.head("讀懂了嗎? · ¿Entendido?", 28)
f.ex("B1", "單選", "A", "Los Dragones son campeones de la primera mitad, el mejor registro del año.",
     "味全龍怎麼晉級台灣大賽?", opts=["A. 上半季冠軍", "B. 抽籤抽到", "C. 去年冠軍保送"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Los Hermanos llegaron tras ganar la Serie de Desafío.",
     "中信兄弟先打贏了什麼比賽?", opts=["A. 季後挑戰賽", "B. 明星賽", "C. 熱身賽"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Todos los partidos de la serie son en el Domo de Taipéi.",
     "台灣大賽全部在哪裡打?", opts=["A. 臺北大巨蛋", "B. 台中洲際棒球場", "C. 高雄澄清湖球場"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Partido 1: Dragones 3, Hermanos 0.",
     "第一戰的比數是?", opts=["A. 味全龍3:0中信兄弟", "B. 中信兄弟3:0味全龍", "C. 味全龍4:3中信兄弟"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Dejar en blanco significa que el rival anota cero.",
     "「完封」是什麼意思?", opts=["A. 對手得0分", "B. 比賽因雨取消", "C. 打滿十局"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Videoland Sports transmite toda la serie.",
     "哪一台轉播全系列比賽?", opts=["A. 緯來體育台", "B. 迪士尼頻道", "C. 購物台"], size=22.5, gap=8)
f.head("看賽程表 · El calendario", 28)
f.ex("B1", "單選", "B", "El partido 4 es el miércoles 21 de octubre.",
     "第四戰 G4 在哪一天?", opts=["A. 10月20日(二)", "B. 10月21日(三)", "C. 10月23日(五)"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Los partidos siguientes se cancelan cuando un equipo llega a cuatro victorias.",
     "G5為什麼寫「如有需要」?", opts=["A. 可能已經有人封王", "B. 場地還沒決定", "C. 門票還沒開賣"], size=22.5, gap=8)
f.ex("B1", "單選", "A", "Esta semana solo son seguros el G3 y el G4.",
     "本週確定要打的比賽有幾場?", opts=["A. 2場", "B. 3場", "C. 5場"], size=22.5, gap=8)
f.ex("B1", "單選", "C", "La serie puede llegar a un partido 7 el domingo.",
     "本週最多打到第幾戰?", opts=["A. G5", "B. G6", "C. G7"], size=22.5, gap=8)
f.head("填一填 · Completa", 28)
f.ex("B1", "完成句子", "4", "Cuatro victorias dan el título al mejor de siete.",
     "七戰四勝:先贏___場,就是總冠軍。", instr="Completa", size=22.5, gap=8)
f.ex("B1", "完成句子", "完封", "Dejar en blanco: los rivales no anotan nada.",
     "對手整場一分未得,叫作___。", instr="Completa", size=22.5, gap=8)
f.ex("B1", "完成句子", "滿場", "Lleno total: todos los asientos ocupados.",
     "票全賣完、場內坐滿人,叫作___。", instr="Completa", size=22.5, gap=8)
f.ex("B1", "完成句子", "封王", "Asegurarse el campeonato es 封王.",
     "贏下決定冠軍的那一場,叫作___。", instr="Completa", size=22.5, gap=8)
f.match_set("B1", "配對",
            ["味全龍", "中信兄弟", "臺北大巨蛋", "緯來體育台"],
            ["上半季冠軍、全年勝率第一", "季後挑戰賽勝出", "全部場次的球場", "全系列轉播的電視台"],
            ["a", "b", "c", "d"],
            ["味全龍 — campeones de la primera mitad, mejor registro del año.",
             "中信兄弟 — llegaron por la Serie de Desafío.",
             "臺北大巨蛋 — el domo que acoge todos los partidos.",
             "緯來體育台 — el canal que transmite toda la serie."],
            instr="Une nombre y dato")
f.end_report()

rx = COLX[3]
image(p, "baseball.jpg", rx, 208, CW, 620)
caption(p, rx, 208 + 620 + 6, CW, "打者全力揮棒(資料照片)。",
        "Photo: unknown author — Public domain (Wikimedia Commons)")
by = 208 + 620 + 100
wc = [
    "完封 (dejar en blanco) — el rival no anota nada",
    "封王 (asegurarse el título) — ganar el partido decisivo",
    "滿場 (lleno total) — todos los asientos ocupados",
    "七戰四勝 (al mejor de siete) — gana el primero que llegue a cuatro",
]
wch = 18 + 56 + sum(24 + len(wrap("· " + t, "serif", False, 22.5, CW - 44)) * 22.5 * 1.32 + 8 for t in wc) - 8 + 16
p.rect(rx, by, CW, wch, fill=BOX, stroke=LINE, sw=1.4)
yy = by + 18
p.text(rx + 22, yy + 26, "棒球詞卡 · Tarjetas de palabras", 25, "sans", True, OLIVE); yy += 56
for t in wc:
    yy = p.para(rx + 22, yy + 24, "· " + t, 22.5, "serif", False, INK, CW - 44, 1.32) + 8
p.rect(rx, by + wch + 18, CW, 220, fill="#f1ead6", stroke=LINE, sw=1.4)
yy = by + wch + 18 + 18
p.text(rx + 22, yy + 26, "你呢? · Ahora tú", 25, "sans", True, OLIVE); yy += 54
yy = p.para(rx + 22, yy + 24, "你支持哪一隊?你看過現場的棒球賽嗎?", 22.5, "serif", False, INK, CW - 44, 1.36) + 4
p.para(rx + 22, yy + 21, "Dragones o Hermanos: ¿a qué equipo apoyas?", 20, "sans", False, GREY, CW - 44, 1.3)
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
