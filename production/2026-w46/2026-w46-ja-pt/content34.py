# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · 文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化 · ぶんか", "Lucerna", "レベル A2→B1 · 七五三と酉の市 · Shichi-Go-San e Tori-no-ichi")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P3-feature")
f.title("七五三 — 着物の子どもと神社", 37)
f.byline("Lucerna編集部 · 読むレベル：A2→B1")
f.para("七五三は、3歳と5歳と7歳の子どものお祝いです。男の子は3歳と5歳、女の子は3歳と7歳でお祝いします。11月15日ごろに、神社へお参りに行きます。")
f.para("子どもは、着物やはかまを着ます。家族と写真を撮ります。神社では、千歳飴をもらいます。今の形は、江戸時代に始まったと言われています。")
f.para("兵庫県の西宮神社では、例年5,000組以上が七五三参りに来るそうです。11月15日だけではありません。いこーよの調査（10月21日までの回答、七五三の家庭200）では、お参りは「11月上旬」が26%でいちばん多く、「11月15日」は3%でした。日にちは、家族によってちがいます。")
f.para("七五三は、子どもの成長を祝う日です。元気に大きくなってほしい、という家族の願いがあります。")
f.gloss("成長 crescimento · 元気 saudável · 願い um desejo · 日にち a data.")
f.head("酉の市と熊手", 25)
f.para("酉の市は、11月の酉の日に開くお祭りです。浅草の鷲神社では、一の酉が7日（土よう日）でした。二の酉は、19日（木よう日）です。2026年は、三の酉がありません。")
f.para("酉の市では、熊手を買います。熊手は、商売繁盛の縁起物です。大きな熊手を、家族や店の人と、いっしょに買う人もいます。")
f.gloss("商売繁盛 negócios prósperos · 縁起物 amuleto da sorte · 並ぶ fazer fila.")
f.end_report()

# col 3: print + calendar + あなた
ix = COLX[3]
image(p, "hiroshige.jpg", ix, 200, CW, 222)
cy3 = caption(p, ix, 422, CW, "明治時代の行列の版画（歌川広重（三代）、1876年）。昔の日本の行列の美しさです。",
              "版画：歌川広重（三代）— パブリックドメイン（Wikimedia Commons）")
cal = ["9日（月）読書週間が終わります",
       "11日（水）ポッキーの日",
       "13日（金）ごろ 高尾山の紅葉が見頃",
       "15日（日）七五三の中心の日",
       "19日（木）酉の市・二の酉"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in cal) + 32
p.rect(ix, sy3, CW, sh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "今週の文化カレンダー", 24, "sans", True, OLIVE)
yy3 += 52
for t in cal:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "あなたは？七五三の日に、どんな写真を撮りたいですか。日本語で2文、書いて送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Que tipo de foto gostarias de tirar no Shichi-Go-San? Escreve duas frases em japonês e envia-as.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill="#f1ead6", stroke=LINE, sw=1.4)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？ · A tua vez", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Que tipo de foto gostarias de tirar no Shichi-Go-San? Escreve duas frases em japonês e envia-as.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Exercícios da página 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · Níveis misturados: encontra o teu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A · 理解", 25)
e.bridge("第3版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "múltipla escolha", "A", "O Shichi-Go-San celebra crianças de 3, 5 e 7 anos",
     "七五三は、だれのお祝いですか。 A. 3歳・5歳・7歳の子ども · B. 20歳の大人 · C. 100歳のお年寄り", size=19, gap=6)
e.ex("A2", "múltipla escolha", "B", "Os rapazes celebram aos 3 e 5 anos, as raparigas aos 3 e 7",
     "女の子は、何歳でお祝いしますか。 A. 3歳と5歳 · B. 3歳と7歳 · C. 5歳と7歳", size=19, gap=6)
e.ex("B1", "múltipla escolha", "B", "As visitas culminam no início de novembro (26 %), diz o inquérito",
     "調査では、お参りがいちばん多いのはいつですか。 A. 11月15日 · B. 11月上旬 · C. 12月", size=19, gap=6)
e.ex("B1", "múltipla escolha", "A", "O Ni-no-tori de Tori-no-ichi é 19 de novembro (quinta-feira)",
     "二の酉はいつですか。 A. 19日（木） · B. 7日（土） · C. 15日（日）", size=19, gap=6)
e.ex("A2", "múltipla escolha", "C", "Não há San-no-tori em 2026",
     "2026年の酉の市は、どうですか。 A. 三の酉まであります · B. 一の酉だけです · C. 二の酉までです", size=19, gap=6)
e.head("B · ことば", 25)
e.bridge("言葉や数字を入れてください。")
e.ex("A2", "completar", "神社", "As crianças do Shichi-Go-San vão rezar a um santuário",
     "七五三の子どもは、___ へお参りに行きます。", instr="Complete", size=19, gap=6)
e.ex("A2", "completar", "千歳飴", "doce comprido vermelho e branco",
     "神社では、___ をもらいます。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar", "熊手", "熊手 = ancinho da sorte para os negócios",
     "酉の市では、___ を買います。", instr="Complete", size=19, gap=6)
e.ex("A2", "completar", "15", "O Shichi-Go-San centra-se por volta de 15 de novembro",
     "七五三は、11月 ___ 日ごろに行います。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar", "26", "As visitas do início de novembro foram 26 % no inquérito",
     "調査では、「11月上旬」は ___ %でした。", instr="Complete", size=19, gap=6)
e.head("C · 文を作りましょう", 25)
e.bridge("言葉を並べて、正しい文を作ってください。")
e.ex("B1", "construção de frases", "七五三は子どものお祝いです。", "sujeito + descrição",
     "七五三は / 子どもの / お祝いです → ___", instr="Construa uma frase", size=19, gap=6)
e.ex("A2", "construção de frases", "神社へお参りに行きます。", "lugar + へ + verbo",
     "神社へ / お参りに / 行きます → ___", instr="Construa uma frase", size=19, gap=6)
e.ex("B1", "construção de frases", "千歳飴をもらいます。", "objeto + verbo",
     "千歳飴を / もらいます → ___", instr="Construa uma frase", size=19, gap=6)
e.ex("B1", "construção de frases", "酉の市で熊手を買います。", "Comprar um kumade em Tori-no-ichi",
     "酉の市で / 熊手を / 買います → ___", instr="Construa uma frase", size=19, gap=6)
e.head("D · ペアにしましょう", 25)
e.match_set("B1", "associação",
            ["七五三", "千歳飴", "熊手", "酉の市"],
            ["11月の酉の日に開くお祭り",
             "3歳・5歳・7歳の子どものお祝い",
             "商売繁盛の縁起物",
             "赤と白の長い飴"],
            ["b", "d", "c", "a"],
            ["七五三 = uma celebração para crianças de 3, 5 e 7 anos b", "千歳飴 = doce comprido vermelho e branco d", "熊手 = ancinho da sorte c", "酉の市 = uma feira nos dias do galo de novembro a"],
            instr="Ligue palavra e sentido")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-bunka.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · スポーツ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("スポーツ · 体育", "Lucerna", "レベル B1 · 日本シリーズ4連勝 · Quatro vitórias seguidas nas Japan Series")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P4-feature")
f.title("4連勝 — 接戦の日本シリーズ", 37)
f.byline("Lucerna編集部 · 読むレベル：B1")
f.para("日本シリーズは、10月24日（土よう日）に始まりました。福岡ソフトバンクホークスと、横浜DeNAベイスターズの対戦でした。第1戦は、ソフトバンクが3対1で勝ちました。第2戦も、ソフトバンクが4対3で勝ちました。2試合とも、延長戦でした。")
f.para("第3戦は、10月27日（火よう日）、福岡でした。ソフトバンクが2対1で勝ちました。延長10回に、正木智也選手のサヨナラホームランで決まりました。第4戦は、10月28日（水よう日）に、ソフトバンクが4対2で勝ちました。")
f.para("ソフトバンクが4連勝で日本一になりました。2年連続、13度目の日本一です。第5戦から第7戦は、行われませんでした。シリーズのMVPは、正木智也選手です。4試合とも、2点差以内の接戦でした。第1戦から第3戦まで、3試合連続の延長戦は、日本シリーズで初めてだそうです。")
f.gloss("接戦 jogo disputado · サヨナラ home run decisivo (sayonara) · 連続 seguidas.")
f.head("シリーズの記録", 25)
f.box("日本シリーズの記録 · Balanço", [
    ("第1戦 — 10月24日（土）横浜：ソフトバンク 3-1 DeNA（延長11回）", "serif", False, INK, 20, 1.35),
    ("第2戦 — 10月25日（日）横浜：ソフトバンク 4-3 DeNA（延長10回）", "serif", False, INK, 20, 1.35),
    ("第3戦 — 10月27日（火）福岡：ソフトバンク 2-1 DeNA（延長10回）", "serif", False, INK, 20, 1.35),
    ("第4戦 — 10月28日（水）福岡：ソフトバンク 4-2 DeNA", "serif", False, INK, 20, 1.35),
    ("第5戦〜第7戦 — 行われませんでした", "serif", False, GREY, 20, 1.35),
    ("MVP — 正木智也選手（ソフトバンク）", "serif", False, INK, 20, 1.35),
])
f.para("前号（VOL.2）では、第3戦からの結果が分かりませんでした。今号で、全部の結果をお知らせします。")
f.gloss("前号 o número anterior · 全部 tudo.")
f.end_report()

# col 3: stadium image + 4-win box
ix = COLX[3]
image(p, "stadium.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "横浜スタジアム。第1戦と第2戦は、ここで戦いました。",
              "写真：Syced — CC0（Wikimedia Commons）")
ot = "4連勝は、4試合とも勝つことです。2年連続の日本一は、去年も今年も優勝した、という意味です。13度目は、13回目です。"
oy = cy3 + 24
oh = 62 + len(wrap(ot, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("※記録は各試合の報道によるものです。", "serif", False, 19.5, CW - 44)) * 27 + 20 + 8
p.rect(ix, oy, CW, oh, fill=BOX, stroke=LINE, sw=1.4)
yy3 = oy + 16
p.text(ix + 22, yy3 + 26, "4連勝の意味", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, ot, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "※記録は各試合の報道によるものです。", 19.5, "serif", False, GREY, CW - 44, 1.38)
print("P4 col3 ends", oy + oh)

# ---- sumo box (full width) ----
ty = 1490
p.text(MX, ty + 26, "大相撲九州場所が始まりました · O torneio de sumo de Kyushu começou", 26, "sans", True, OLIVE)
p.hline(MX, RIGHT, ty + 40, GOLD, 2)
p.para(MX, ty + 78, "大相撲の九州場所は、8日（日よう日）に福岡国際センターで始まりました。横綱は大の里と豊昇龍です。10月26日に発表された番付では、美ノ海が新小結になりました。沖縄県の力士で初めての三役だそうです。玉鷲は、41歳11か月で再入幕しました。場所は、22日（日よう日）までです。今週の勝敗は、次号でお知らせします。", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1840
p.hline(MX, RIGHT, ey - 12, GOLD, 2)
p.text(MX, ey + 28, "練習 · Exercícios da página 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Respostas na página 8 · Níveis misturados: encontra o teu número", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A · 理解", 25)
e.bridge("第4版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "múltipla escolha", "B", "Jogo 3: SoftBank ganhou 2-1",
     "第3戦のスコアは？ A. 4-2 · B. 2-1 · C. 1-2", size=19, gap=6)
e.ex("B1", "múltipla escolha", "B", "Masaki bateu o home run decisivo do jogo 3",
     "第3戦のサヨナラホームランを打ったのは？ A. 山川選手 · B. 正木選手 · C. 川村選手", size=19, gap=6)
e.ex("B1", "múltipla escolha", "A", "Jogo 4: SoftBank ganhou 4-2",
     "第4戦のスコアは？ A. 4-2 · B. 2-4 · C. 3-1", size=19, gap=6)
e.ex("B1", "múltipla escolha", "B", "O MVP da série é Masaki Tomoya",
     "シリーズのMVPはだれですか。 A. 山川選手 · B. 正木選手 · C. 筒香選手", size=19, gap=6)
e.ex("B1", "múltipla escolha", "A", "Os jogos 5 a 7 não se jogaram",
     "第5戦から第7戦は、どうなりましたか。 A. 行われませんでした · B. 横浜で行われました · C. 福岡で行われました", size=19, gap=6)
e.head("B · 数字", 25)
e.bridge("第4版の数字を入れてください。")
e.ex("B1", "completar", "2", "SoftBank marcou 2 no jogo 3",
     "第3戦、ソフトバンクは ___ 点取りました。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar", "4", "SoftBank marcou 4 no jogo 4",
     "第4戦、ソフトバンクは ___ 点取りました。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar", "10", "O jogo 3 chegou à 10.ª entrada",
     "第3戦は延長 ___ 回で決まりました。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar", "13", "O 13.º título de SoftBank",
     "ソフトバンクは ___ 度目の日本一です。", instr="Complete", size=19, gap=6)
e.ex("B1", "completar", "3", "Os três primeiros jogos foram todos a entradas extra",
     "第1戦から第3戦まで、___ 試合連続の延長戦でした。", instr="Complete", size=19, gap=6)
e.head("C · ことばと記録", 25)
e.bridge("第4版の記事から答えてください。")
e.ex("B1", "múltipla escolha", "B", "接戦 = um jogo disputado",
     "「接戦」とは何ですか。 A. 大差の試合 · B. 点差が小さい試合 · C. 試合がないこと", size=19, gap=6)
e.ex("B1", "múltipla escolha", "A", "O torneio de Kyushu realiza-se no Fukuoka Kokusai Center",
     "九州場所はどこですか。 A. 福岡国際センター · B. 横浜スタジアム · C. 東京ドーム", size=19, gap=6)
e.ex("B1", "múltipla escolha", "B", "O novo komusubi é Umi-no-umi",
     "新小結になったのはだれですか。 A. 玉鷲 · B. 美ノ海 · C. 大の里", size=19, gap=6)
e.ex("B1", "múltipla escolha", "A", "O torneio de sumo dura até 22 de novembro (domingo)",
     "九州場所はいつまでですか。 A. 22日（日） · B. 15日（日） · C. 28日（水）", size=19, gap=6)
e.head("D · 正しい・正しくない", 25)
e.bridge("文が正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "verdadeiro/falso", "○", "Quatro vitórias seguidas para o título",
     "ソフトバンクは、4連勝しました。", instr="Verdadeiro ou falso?", size=19, gap=6)
e.ex("B1", "verdadeiro/falso", "×", "O jogo 3 jogou-se em Yokohama",
     "第3戦は横浜で行われました。", instr="Verdadeiro ou falso?", size=19, gap=6)
e.ex("B1", "verdadeiro/falso", "×", "O jogo 5 também se jogou",
     "第5戦も行われました。", instr="Verdadeiro ou falso?", size=19, gap=6)
e.ex("B1", "verdadeiro/falso", "○", "Os três primeiros jogos foram todos a entradas extra",
     "第1戦から第3戦まで、延長戦でした。", instr="Verdadeiro ou falso?", size=19, gap=6)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-supotsu.svg")
print("P4 saved, exercises so far:", len(REG))
