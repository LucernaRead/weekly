# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ja-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · 若者・エンタメ (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("若者・エンタメ · Jovens", "Lucerna", "レベル B1 · コントとハロウィン · Comédia e Halloween")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P5-feature")
f.title("ジェラードンが優勝！キングオブコント2026", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("10月17日（土）、東京・赤坂のTBSで『キングオブコント2026』の決勝がありました。優勝は、コントのグループ『ジェラードン』です。第19代の王者で、賞金は1,000万円です。")
f.para("点数は、671点と671点で、合計1,342点でした。2位の『かえる亭』とは、33点の差でした。今年は、負けたチームがもう一度戦う『敗者復活』がありました。審査員も、5人から7人に増えました。")
f.para("決勝の後も、話は終わりません。『キングオブコント2026』は、20日（火）のトレンドでも1位でした。テレビの前で笑った人も多い週末でした。")
f.gloss("決勝 a final · 王者 os campeões · 敗者復活 a repescagem · 審査員 os jurados.")
f.head("ハロウィンと渋谷のルール", 25)
f.para("今年のハロウィンは、10月31日（土）です。仮装の準備をする人が増えています。でも、渋谷にはルールがあります。駅の近くでは、一年中、夜18時から朝5時まで、道でお酒を飲むことができません。")
f.para("ゴミを捨てると、その場で2,000円の罰金です。今年の6月から始まったルールです。ハチ公の像は、10月30日から11月1日までフェンスの中にあります。ハロウィンの夜は、お店にお酒を売らないよう、お願いも出ています。")
f.para("コスプレの大きなイベントは池袋です。『池袋ハロウィンコスプレフェス』は、10月30日から11月1日まであります。ルールを守って、楽しいハロウィンにしましょう。")
f.gloss("罰金 uma multa · 像 uma estátua · 仮装 uma fantasia · 守る respeitar (as regras).")
f.end_report()

# col 3: pumpkin image + comedy words + あなた
ix = COLX[3]
image(p, "pumpkin.jpg", ix, 200, CW, 262)
cy3 = caption(p, ix, 462, CW, "ハロウィンのかぼちゃ。渋谷では、ルールを守ることが大切です。",
              "写真：Petr Kratochvil — パブリックドメイン（Wikimedia Commons）")
words5 = ["ボケ — わざと変なことを言う人",
          "ツッコミ — ボケに答える人",
          "ネタ — コントの話の内容"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in words5) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "コントのことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in words5:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "あなたは？ハロウィンに、どんな仮装をしたいですか。日本語で2文、書いて、送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("E você? De que você quer se fantasiar no Halloween? Escreva duas frases em japonês e envie para nós.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · E você?", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "E você? De que você quer se fantasiar no Halloween? Escreva duas frases em japonês e envie para nós.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P5 col3 ends", ey3 + eh)

# ---- P5 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Exercícios da página 5", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · Níveis mistos: procure o seu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P5-ex")
e.head("A · 理解", 25)
e.expl("コントの記事を読んで、正しい答えを選んでください。")
e.ex("B1", "escolha múltipla", "A", "A final foi no sábado, 17 de outubro",
     "キングオブコントの決勝は何日でしたか。 A. 17日（土） · B. 20日（火） · C. 31日（土）", size=19, gap=6)
e.ex("B1", "escolha múltipla", "B", "Os campeões são os Geraldon",
     "優勝したのは？ A. かえる亭 · B. ジェラードン · C. ハチ公", size=19, gap=6)
e.ex("B1", "escolha múltipla", "B", "O prêmio é de 10 milhões de ienes",
     "賞金はいくらですか。 A. 100万円 · B. 1,000万円 · C. 2,000円", size=19, gap=6)
e.ex("B1", "escolha múltipla", "B", "O total é de 1.342 pontos",
     "ジェラードンの合計点は？ A. 671点 · B. 1,342点 · C. 33点", size=19, gap=6)
e.ex("B1", "escolha múltipla", "B", "Os jurados subiram para sete",
     "審査員は何人に増えましたか。 A. 5人 · B. 7人 · C. 19人", size=19, gap=6)
e.head("B · 数字", 25)
e.expl("第5版の数字を入れてください。")
e.ex("B1", "completar frases", "19", "Os campeões número 19",
     "ジェラードンは第 ___ 代の王者です。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar frases", "671", "As duas rodadas: 671 pontos",
     "点数は671点と ___ 点でした。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar frases", "33", "33 pontos à frente do segundo",
     "2位との差は ___ 点でした。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar frases", "2,000", "Multa por lixo: 2.000 ienes",
     "ゴミを捨てると、罰金は ___ 円です。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar frases", "1", "O Hachiko fica cercado até 1.º de novembro",
     "ハチ公の像がフェンスの中にあるのは、11月 ___ 日までです。", instr="Complete", size=19, gap=6)
e.head("C · 正しい・正しくない", 25)
e.expl("渋谷のルールについて、正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "verdadeiro ou falso", "×", "Não se pode beber álcool na rua",
     "渋谷では、夜、道でお酒を飲むことができます。", instr="V ou F", size=19, gap=6)
e.ex("B1", "verdadeiro ou falso", "○", "A multa por lixo vale desde junho deste ano",
     "ゴミの罰金は、今年の6月からです。", instr="V ou F", size=19, gap=6)
e.ex("B1", "verdadeiro ou falso", "×", "O festival de cosplay é em Ikebukuro",
     "コスプレフェスは渋谷であります。", instr="V ou F", size=19, gap=6)
e.ex("B1", "verdadeiro ou falso", "○", "Halloween é no sábado, 31 de outubro",
     "ハロウィンは10月31日（土）です。", instr="V ou F", size=19, gap=6)
e.head("D · 文を完成しましょう", 25)
e.expl("第5版の文を完成してください。")
e.ex("B1", "completar frases", "飲む", "飲むことができません = não se pode beber",
     "駅の近くでは、道でお酒を ___ ことができません。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar frases", "守って", "守って + ましょう: vamos respeitar",
     "ルールを ___ 、楽しいハロウィンにしましょう。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar frases", "中", "フェンスの中 = dentro da cerca",
     "ハチ公の像は、フェンスの ___ にあります。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar frases", "10月30日", "Acontece de 30 de outubro a 1.º de novembro",
     "コスプレフェスは ___ から11月1日までです。", instr="Complete", size=19, gap=6)
e.end_report()
p.foot(5)
p.save(f"{OUT}/p5-wakamono.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · 深読み (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("深読み · ふかよみ", "Lucerna", "レベル B2 · アジアパラ競技大会 · Os Jogos Para-Asiáticos em profundidade")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P6-feature")
f.title("日本で初めてのアジアパラ競技大会", 37)
f.byline("Lucerna編集部 · 読むレベル：B2")
f.para("『第5回アジアパラ競技大会 愛知・名古屋2026』は、10月18日（日）に始まりました。最終日は24日（土）です。アジアパラ競技大会が日本で開かれるのは、今回が初めてです。")
f.para("参加した国と地域は45で、過去最多でした。競技は18あります。日本の選手団は282人です。そのうち120人は初めての出場で、17人は2024年のパリ・パラリンピックの金メダリストです。")
f.para("この大会は、2028年のロサンゼルス・パラリンピックへの道でもあります。たとえば車いすテニスでは、優勝した選手がロサンゼルス大会への出場権を直接得ることができます。（アジアデイリーの報道による）")
f.para("大会の意味は、スポーツだけではありません。会場のバリアフリー、街の人たちの応援、そして障害のある人もない人も、同じ場所で同じ試合を見ます。その風景こそ、この大会がいちばん伝えたいことです。")
f.para("愛知・名古屋の次は、2028年のロサンゼルスです。この大会で経験を積んだ選手たちが、2年後の世界の舞台を目指します。日本の282人のうち120人は、初めての出場でした。若い選手たちの経験も、この大会の大きな成果です。")
f.gloss("選手団 uma delegação · 出場権 uma vaga na competição · 障害 a deficiência · 風景 uma cena · 成果 um resultado.")
f.end_report()

# col 3: para swim image + facts
ix = COLX[3]
image(p, "paraswim.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "パラ水泳も人気の競技です。（写真はアメリカ国防総省の大会のもので、本大会の写真ではありません）",
              "写真：EJ Hersom／米国防総省 — パブリックドメイン（Wikimedia Commons）")
facts6 = ["45 — 参加した国と地域（過去最多）",
          "18 — 競技の数",
          "282 — 日本の選手の数",
          "120 — 初めて出場する日本の選手"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in facts6) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "大会の数字", 24, "sans", True, OLIVE)
yy3 += 52
for t in facts6:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
print("P6 col3 ends", sy3 + sh)

# ---- practice chart (full width) ----
chy = 1500
p.text(MX, chy + 26, "グラフを読もう · Vamos ler o gráfico", 26, "sans", True, OLIVE)
p.text(RIGHT, chy + 26, "練習用データ · Dados de prática", 21, "sans", True, BRICK, anchor="end")
p.hline(MX, RIGHT, chy + 40, GOLD, 2)
p.text(MX, chy + 78, "会場で聞いた「見たい競技」（練習用データ — 実際の調査ではありません）", 22, "serif", True, INK)
chart = [("車いすテニス", 34), ("水泳", 28), ("陸上", 22), ("その他", 16)]
byy = chy + 104
for name, val in chart:
    p.text(MX, byy + 26, name, 22, "serif", False, INK)
    p.rect(MX + 250, byy, val * 30, 34, fill=OLIVE)
    p.text(MX + 250 + val * 30 + 16, byy + 26, f"{val}%", 22, "sans", True, INK)
    byy += 56
p.para(MX, byy + 22, "このグラフは練習用データです。数字は全部で100%になります。", 19.5, "serif", False, GREY, RIGHT - MX, 1.4)

# ---- P6 exercises ----
ey = 1900
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Exercícios da página 6", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · Níveis mistos: procure o seu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P6-ex")
e.head("A · 理解", 25)
e.expl("第6版の文章を読んで、正しい答えを選んでください。")
e.ex("B2", "escolha múltipla", "B", "Primeira vez no Japão (os Jogos estão na 5.ª edição)",
     "アジアパラ競技大会が日本で開かれるのは？ A. 2回目 · B. 初めて · C. 毎年", size=19, gap=6)
e.ex("B2", "escolha múltipla", "B", "Participaram 45 países e regiões",
     "参加した国と地域は？ A. 18 · B. 45 · C. 282", size=19, gap=6)
e.ex("B2", "escolha múltipla", "C", "A equipe japonesa: 282 atletas",
     "日本の選手は何人ですか。 A. 120人 · B. 17人 · C. 282人", size=19, gap=6)
e.ex("B2", "escolha múltipla", "A", "120 atletas japoneses são estreantes",
     "初めて出場する日本の選手は？ A. 120人 · B. 282人 · C. 17人", size=19, gap=6)
e.ex("B2", "escolha múltipla", "B", "Os vencedores do tênis em cadeira de rodas vão direto a Los Angeles",
     "車いすテニスの優勝者は、どこへの出場権を直接得ますか。 A. パリ大会 · B. ロサンゼルス大会 · C. 名古屋大会", size=19, gap=6)
e.head("B · グラフ", 25)
e.expl("練習用データのグラフを見て答えてください。")
e.ex("B2", "completar frases", "車いすテニス", "No topo do gráfico: o tênis em cadeira de rodas",
     "「見たい競技」で1位は ___ です。", instr="Complete", size=19, gap=6)
e.ex("B2", "completar frases", "34", "Tênis em cadeira de rodas: 34%",
     "車いすテニスと答えた人は ___ %です。", instr="Complete", size=19, gap=6)
e.ex("B2", "completar frases", "28", "Natação: 28%",
     "水泳は ___ %です。", instr="Complete", size=19, gap=6)
e.ex("B2", "completar frases", "6", "22% menos 16% = 6 pontos",
     "陸上と「その他」の差は ___ %です。", instr="Complete", size=19, gap=6)
e.ex("B2", "completar frases", "62", "34 + 28 = 62",
     "車いすテニスと水泳を合わせると ___ %です。", instr="Complete", size=19, gap=6)
e.ex("B2", "completar frases", "100", "Os quatro itens somam 100%",
     "4つの数字を全部足すと ___ %になります。", instr="Complete", size=19, gap=6)
e.head("C · 数字と事実", 25)
e.expl("第6版の数字を入れてください。")
e.ex("B2", "completar frases", "17", "17 são ouros de Paris 2024",
     "日本の選手282人のうち、金メダリストは ___ 人です。", instr="Complete", size=19, gap=6)
e.ex("B2", "completar frases", "24", "O último dia é sábado, 24 de outubro",
     "大会の最終日は10月 ___ 日（土）です。", instr="Complete", size=19, gap=6)
e.ex("B2", "completar frases", "5", "É a 5.ª edição dos Jogos Para-Asiáticos",
     "この大会は第 ___ 回のアジアパラ競技大会です。", instr="Complete", size=19, gap=6)
e.ex("B2", "completar frases", "2028", "As Paralimpíadas de Los Angeles são em 2028",
     "ロサンゼルスのパラリンピックは ___ 年です。", instr="Complete", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.expl("正しければ○、正しくなければ×を書いてください。")
e.ex("B2", "verdadeiro ou falso", "×", "É a primeira vez no Japão",
     "この大会は、日本で2回目です。", instr="V ou F", size=19, gap=6)
e.ex("B2", "verdadeiro ou falso", "○", "Países e regiões participantes: um recorde",
     "参加した国と地域は、過去最多でした。", instr="V ou F", size=19, gap=6)
e.ex("B2", "verdadeiro ou falso", "×", "O gráfico usa dados de prática",
     "グラフの数字は、本当の調査の結果です。", instr="V ou F", size=19, gap=6)
e.end_report()
p.foot(6)
p.save(f"{OUT}/p6-fukayomi.svg")
print("P6 saved, exercises so far:", len(REG))
