# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-zh-cn-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · Cultura", "Lucerna", "Nível A2→B1 · 重阳刚过 · 霜降要来 · Uma festa que acabou de passar, um termo a caminho")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1560, tag="P3-feature")
f.title("重阳刚过,霜降要来", 37)
f.byline("Redação Lucerna · Nível de leitura A2→B1")
f.para("上周日,10月18日,是重阳节。重阳节在农历九月初九。「九」是阳数,两个九在一起,所以叫「重阳」。")
f.para("重阳节要登高。人们爬上山,看秋天的风景。还要赏菊花、佩茱萸、吃重阳糕。")
f.para("王维写过一首有名的诗:「遥知兄弟登高处,遍插茱萸少一人。」这首诗写的就是重阳节想念家人的心情。")
f.para("重阳糕是重阳节的点心。吃糕有「步步高」的好意头,因为「糕」和「高」同音。山上还有菊花:人们一边爬山,一边赏菊,菊花茶也是重阳的味道。")
f.para("现在,重阳节也是敬老节。这一天,年轻人陪老人爬山、吃饭,给老人送祝福。")
f.gloss("nónglì 农历 — o calendário lunar tradicional · dēnggāo 登高 — subir a um lugar alto · zhūyú 茱萸 — uma planta perfumada usada para sorte e saúde.")
f.head("霜降:秋天的最后一个节气", 25)
f.para("本周五,10月23日,是霜降。霜降是秋天的第六个节气,也是最后一个。霜降有三候:一候豺乃祭兽,二候草木黄落,三候蛰虫咸俯。")
f.para("简单说:动物开始准备过冬,树叶变黄、落下,小虫子躲进洞里。天气真的冷了。")
f.para("霜降吃柿子。老话说:「霜降吃柿子,嘴唇不会裂。」还有一句话:「补冬不如补霜降。」这个周末,去山上看红叶,回家吃一个柿子,秋天就圆满了。")
f.para("霜降前后,柿子最甜,山上的枫叶也红了、银杏也黄了。公园里都是拍照的人——这就是深秋的样子。")
f.gloss("hòu 候 — uma microestação de cinco dias · huángluò 黄落 — as folhas amarelam e caem · zhéchóng 蛰虫 — insetos em hibernação, escondidos para o inverno.")
f.end_report()

# col 3: chrysanthemum + facts + frost + 你呢
ix = COLX[3]
image(p, "chrysanthemum.jpg", ix, 200, CW, 185)
cy3 = caption(p, ix, 385, CW, "重阳赏菊。菊花是秋天的花,也是长寿的花。",
              "Foto: PushpaKhan — CC0 (Wikimedia Commons)")
facts = ["上周日 10月18日 — 重阳节(农历九月初九)",
         "本周五 10月23日 — 霜降,秋天最后一个节气",
         "11月7日 — 立冬,冬天开始"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "节日小日历 · Datas das festas", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
image(p, "frost.jpg", ix, ay3, CW, 200)
cy4 = caption(p, ix, ay3 + 200, CW, "带霜的红叶。霜降到了,早上能看见白白的霜。",
              "Foto: Gerda Arendt — CC0 (Wikimedia Commons)")
ey3 = cy4 + 18
etvous = "你呢?重阳节,你想陪谁去爬山?霜降的时候,你想吃什么?写两句中文寄来。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("E você? Com quem você subiria uma colina? O que você comeria no Shuāngjiàng? Escreva duas frases em chinês.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "说说你自己 · E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E você? Com quem você subiria uma colina? O que você comeria no Shuāngjiàng? Escreva duas frases em chinês.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1620
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Exercícios", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 读一读选一选 · Leia e escolha", 25)
e.glossline("Leia a página 3 e escolha a melhor resposta.")
e.ex("A2", "Escolha múltipla", "A", "Chóngyáng cai no dia 9 do 9º mês lunar.",
     "重阳节在农历几月几日? A. 九月初九 · B. 八月十五 · C. 正月初一", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "B", "Subir a um lugar alto é a atividade clássica do Chóngyáng.",
     "重阳节人们做什么? A. 游泳 · B. 登高 · C. 放鞭炮", size=19, gap=6)
e.ex("B1", "Escolha múltipla", "C", "Quem falta no poema de Wang Wei é o próprio poeta.",
     "王维的诗里,登高的人少了谁? A. 一位朋友 · B. 一位兄弟 · C. 作者自己", size=19, gap=6)
e.ex("A2", "Escolha múltipla", "B", "Shuāngjiàng é o último termo solar do outono.",
     "霜降是秋天的哪个节气? A. 第一个 · B. 最后一个 · C. 第三个", size=19, gap=6)
e.ex("B1", "Escolha múltipla", "B", "Segunda microestação: as folhas amarelam e caem.",
     "霜降二候,树叶怎么样? A. 变绿 · B. 变黄落下 · C. 开花", size=19, gap=6)
e.head("B · 词语填空 · Complete", 25)
e.glossline("Complete cada espaço com a palavra certa.")
e.ex("A2", "Complete a frase", "重阳", "A festa do jiǔyuè chūjiǔ é o Chóngyáng.",
     "九月初九是___节。", instr="Complete", size=19, gap=6)
e.ex("A2", "Complete a frase", "登高", "dēnggāo — subir a um lugar alto no Chóngyáng.",
     "重阳节要爬山,这叫___。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "茱萸", "zhūyú — a planta perfumada que as pessoas usam.",
     "人们把___佩在身上,保佑平安。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "黄落", "cǎomù huángluò — as folhas amarelam e caem (2ª microestação).",
     "霜降二候是草木___。", instr="Complete", size=19, gap=6)
e.ex("A2", "Complete a frase", "柿子", "Comer caquis no Shuāngjiàng é o costume.",
     "霜降吃___,嘴唇不会裂。", instr="Complete", size=19, gap=6)
e.head("C · 数字与日期 · Números e datas", 25)
e.glossline("Responda com datas e números da página 3.")
e.ex("A2", "Complete a frase", "18", "Este ano, o Chóngyáng foi em 18 de outubro (domingo).",
     "今年重阳节在10月___日。", instr="Complete", size=19, gap=6)
e.ex("A2", "Complete a frase", "23", "Shuāngjiàng cai na sexta-feira, 23 de outubro.",
     "霜降在10月___日。", instr="Complete", size=19, gap=6)
e.ex("A2", "Complete a frase", "7", "Este ano, Lìdōng é em 7 de novembro.",
     "立冬在11月___日。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "一", "biàn chā zhūyú shǎo yì rén — falta uma pessoa.",
     "王维的诗里说「遍插茱萸少___人」。", instr="Complete", size=19, gap=6)
e.head("D · 词语配对 · Associação", 25)
e.match_set("A2", "Associação",
            ["登高", "茱萸", "重阳糕", "霜"],
            ["早上草地上的白色小冰晶",
             "重阳节吃的一种糕",
             "爬上高处看风景",
             "佩在身上的香草"],
            ["c", "d", "b", "a"],
            ["dēnggāo = subir alto, c", "zhūyú = a planta que se usa, d", "chóngyáng gāo = o bolo da festa, b", "shuāng = geada, a"],
            instr="Associe as palavras")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-wenhua.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · 体育 (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("体育 · Esporte", "Lucerna", "Nível B1 · 体操世锦赛 · NBA 新赛季 · Mundial de ginástica e abertura da NBA")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1180, tag="P4-feature")
f.title("体操男团摘铜,NBA 新赛季开打", 37)
f.byline("Redação Lucerna · Nível de leitura B1")
f.para("北京时间10月21日凌晨,2026年体操世锦赛在荷兰鹿特丹举行男子团体决赛。日本队拿到251.928分,得到冠军。")
f.para("中国队有邹敬园、兰星宇、杨皓楠、田昊和李鸿颜,拿到249.193分,得到铜牌。两个分数只差2.735分。")
f.para("比赛前三名的队,都拿到了2028年洛杉矶奥运会的团体参赛资格。女子团体决赛在北京时间10月22日凌晨1点30分举行。")
f.para("体操有很多项目:自由操、鞍马、吊环、跳马、双杠、单杠。中国队里,邹敬园的双杠很有名。")
f.gloss("tuántǐ 团体 — a prova por equipes · juésài 决赛 — a final · zīgé 资格 — uma vaga na classificação · diàohuán 吊环 — as argolas.")
f.para("篮球也有大消息。NBA新赛季在北美时间10月20日开始;换成北京时间,是10月21日上午。")
f.para("揭幕日有三场比赛:凯尔特人对活塞、76人对尼克斯、雷霆对马刺。尼克斯是上个赛季的冠军,是卫冕冠军。")
f.para("最大的看点是詹姆斯。他穿上76人的球衣,开始他的第24个赛季。马刺队也在揭幕日出场,年轻球员文班亚马会和队友一起上场。")
f.gloss("jiēmù 揭幕 — abrir a temporada · wèimiǎn 卫冕 — defender um título · kàndiǎn 看点 — o que vale a pena ver.")
f.end_report()

# ---- score chart (cols 0-2), bars exactly proportional from zero ----
ly = 1210
p.text(MX, ly + 26, "男团决赛：只差 2.735 分 · A final por equipes masculina", 26, "sans", True, OLIVE)
p.hline(MX, COLX[2] + CW, ly + 40, GOLD, 2)
rows = [("日本队", 251.928), ("中国队", 249.193)]
SCALE = 2.2
by0 = ly + 66
for i, (name, val) in enumerate(rows):
    yy = by0 + i * 64
    p.text(MX, yy + 34, name, 24, "sans", True, INK)
    bw_ = val * SCALE
    p.rect(MX + 120, yy + 6, bw_, 34, fill=OLIVE if i == 0 else GOLD)
    p.text(MX + 120 + bw_ + 16, yy + 34, f"{val:.3f} 分", 24, "serif", True, INK)
p.para(MX, by0 + 2 * 64 + 22, "As barras são desenhadas a partir de 0, em proporção exata às pontuações: 251.928 − 249.193 = 2.735. Fonte: 京报网 (The Beijing News), 21/10/2026.", 20.5, "serif", False, GREY, 1388, 1.4)

# col 3: basketball + facts + 1896 gymnastics
ix = COLX[3]
image(p, "basketball.jpg", ix, 200, CW, 240)
cy3 = caption(p, ix, 440, CW, "篮球进筐!NBA 新赛季,北京时间 10 月 21 日上午开打。",
              "Foto: noahsilliman — CC0 (Wikimedia Commons)")
facts = ["10月21日凌晨 — 体操男团决赛(已结束)",
         "10月22日 01:30 — 体操女团决赛",
         "10月21日上午 — NBA 新赛季第一天"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "体育小日历 · Datas do esporte", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ay3 = sy3 + sh + 26
image(p, "gymnastics1896.jpg", ix, ay3, CW, 200)
caption(p, ix, ay3 + 200, CW, "一百多年前的体操比赛:1896 年的雅典。今天的项目名字,很多还是那时的。",
        "Foto: autor desconhecido, 1896 — Domínio público (Wikimedia Commons)")
print("P4 col3 ends", ay3 + 300)

# ---- P4 exercises ----
ey = 1560
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "练习 · Exercícios", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · 答案见第 8 版", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 读一读选一选 · Leia e escolha", 25)
e.glossline("Leia a página 4 e escolha a melhor resposta.")
e.ex("B1", "Escolha múltipla", "A", "O Mundial foi em Roterdã, na Holanda.",
     "体操世锦赛在哪个城市? A. 鹿特丹 · B. 北京 · C. 洛杉矶", size=19, gap=6)
e.ex("B1", "Escolha múltipla", "B", "O Japão venceu o título masculino por equipes.",
     "男团冠军是哪个队? A. 中国队 · B. 日本队 · C. 美国队", size=19, gap=6)
e.ex("B1", "Escolha múltipla", "B", "A China fez 249.193 pontos.",
     "中国队拿到多少分? A. 251.928 · B. 249.193 · C. 240.193", size=19, gap=6)
e.ex("B1", "Escolha múltipla", "B", "As três primeiras equipes ganharam as vagas olímpicas para LA 2028.",
     "前三名的队拿到了什么? A. 奖金 · B. 奥运团体资格 · C. 新球衣", size=19, gap=6)
e.ex("B1", "Escolha múltipla", "C", "No dia da abertura, os 76ers jogaram contra os Knicks.",
     "NBA 揭幕日,76 人对哪个队? A. 凯尔特人 · B. 马刺 · C. 尼克斯", size=19, gap=6)
e.head("B · 词语填空 · Complete", 25)
e.glossline("Complete cada espaço com a palavra certa.")
e.ex("B1", "Complete a frase", "团体", "tuántǐ — a final masculina por equipes.",
     "男子___决赛在鹿特丹举行。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "铜", "A China ficou com a medalha de bronze.",
     "中国队得到___牌。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "体操", "Argolas e barras são provas da ginástica.",
     "吊环、双杠、单杠都是___项目。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "卫冕", "wèimiǎn — os Knicks são os atuais campeões.",
     "尼克斯是上个赛季的冠军,是___冠军。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "24", "É a 24ª temporada de LeBron.",
     "詹姆斯开始他的第___个赛季。", instr="Complete", size=19, gap=6)
e.head("C · 读图与换算 · Leia o gráfico", 25)
e.glossline("Leia o gráfico e os horários da página 4.")
e.ex("B2", "Complete a frase", "2.735", "251.928 − 249.193 = 2.735 pontos.",
     "两个分数差___分。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "1", "A final feminina por equipes é à 01:30, hora de Pequim.",
     "女团决赛在北京时间10月22日凌晨___点30分。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "21", "20/out na América do Norte é 21/out em Pequim.",
     "NBA 在北美时间10月20日开赛,北京时间是10月___日。", instr="Complete", size=19, gap=6)
e.ex("B1", "Complete a frase", "一", "Os campeões ficam em primeiro.",
     "拿到冠军的队排第___。", instr="Complete", size=19, gap=6)
e.head("D · 词语配对 · Associação", 25)
e.match_set("B1", "Associação",
            ["吊环", "双杠", "单杠", "自由操"],
            ["在地上做动作,不用器械",
             "两根一样高的杠",
             "一根高高的杠",
             "两个吊在空中的环"],
            ["d", "b", "c", "a"],
            ["diàohuán = duas argolas penduradas, d", "shuānggàng = duas barras na mesma altura, b", "dāngàng = uma barra alta, c", "zìyóucāo = solo, a"],
            instr="Associe as palavras")
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-tiyu.svg")
print("P4 saved, exercises so far:", len(REG))
