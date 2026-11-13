# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3　文化 (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("文化　ぶんか", "Lucerna", "レベル A2→B1　ボジョレーと秋の味　Beaujolais e sapori d'autunno")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1500, tag="P3-feature")
f.title("新酒の夜 — 19日の0時", 37)
f.byline("Lucerna編集部　読むレベル：A2→B1")
f.para("ボジョレー・ヌーヴォーは、フランスのボジョレー地方の新酒です。9月ごろに収穫したぶどうで、短い時間で作ります。解禁日は、毎年11月の第3木曜日、午前0時です。今年は、11月19日（木よう日）です。")
f.para("日本は、時差の関係で、世界でいちばん早く新酒を飲むことができる国だそうです。百貨店では、11月19日から新酒を売ります。阪神梅田本店では、約40種類の新酒を売るそうです。")
f.para("ボジョレー・ヌーヴォーは、秋の収穫を祝うワインです。フレッシュで、果実の香りがします。今年の出来栄えを確かめながら、季節の味覚といっしょに楽しみます。")
f.gloss("収穫 il raccolto　解禁日 il giorno dell'uscita　出来栄え la qualità di quest'anno　味覚 il gusto.")
f.head("酉の市の屋台", 25)
f.para("酉の市の楽しみは、熊手だけではありません。会場のまわりには、屋台も並びます。昔ながらの祭りの食べ物を、食べながら歩く人もいます。夜の浅草は、明るくにぎやかです。")
f.para("11月19日は、夜の浅草と新酒のワイン、両方の楽しみがある日です。秋の味覚を、味わいましょう。")
f.gloss("屋台 le bancarelle　にぎやか animato　味わう gustare.")
f.end_report()

# col 3: vineyard image + calendar + あなた
ix = COLX[3]
image(p, "beaujolais.jpg", ix, 200, CW, 290)
cy3 = caption(p, ix, 490, CW, "フランス・ボジョレー地方のぶどう畑。秋色の畑です。",
              "Foto: Alainauzas — dominio pubblico (Wikimedia Commons)")
cal = ["16日（月）今週の始まり",
       "19日（木）酉の市・二の酉と新酒の解禁",
       "22日（日）相撲の千秋楽と小雪",
       "23日（月）勤労感謝の日と嵐山の見頃",
       "12月1日（火）流行語のトップテン発表"]
sy3 = cy3 + 24
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in cal) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "今週の文化カレンダー", 24, "sans", True, OLIVE)
yy3 += 52
for t in cal:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ey3 = sy3 + sh + 26
etvous = "あなたは？新酒と秋の味覚で、何を楽しみたいですか。日本語で2文、書いて送ってください。"
eh = 62 + len(wrap(etvous, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("Cosa ti piacerebbe gustare, del vino nuovo o dei sapori d'autunno? Scrivi due frasi in giapponese e inviacele.", "sans", False, 20, CW - 44)) * 29 + 20
p.rect(ix, ey3, CW, eh, fill=BOX)
yy3 = ey3 + 16
p.text(ix + 22, yy3 + 26, "あなたは？　Ora tocca a te", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, etvous, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "Cosa ti piacerebbe gustare, del vino nuovo o dei sapori d'autunno? Scrivi due frasi in giapponese e inviacele.", 20, "sans", False, GREY, CW - 44, 1.42)
print("P3 col3 ends", ey3 + eh)

# ---- P3 exercises ----
ey = 1580
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "練習　Esercizi pagina 3", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli sono mescolati — trova il tuo numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P3-ex")
e.head("A　理解", 25)
e.bridge("第3版の文章を読んで、正しい答えを選んでください。")
e.ex("A2", "scelta multipla", "A", "Il Beaujolais Nouveau è un vino nuovo francese",
     "ボジョレー・ヌーヴォーは、何ですか。 A. フランスの新酒　B. 日本のお茶　C. 韓国のお酒", size=19, gap=6)
e.ex("A2", "scelta multipla", "B", "Il giorno dell'uscita è il terzo giovedì di novembre",
     "解禁日は、いつですか。 A. 11月の第1木曜日　B. 11月の第3木曜日　C. 12月の第3木曜日", size=19, gap=6)
e.ex("B1", "scelta multipla", "A", "Le uve del vino nuovo si raccolgono verso settembre",
     "新酒のぶどうは、いつ収穫しますか。 A. 9月ごろ　B. 11月ごろ　C. 12月ごろ", size=19, gap=6)
e.ex("B1", "scelta multipla", "A", "Il Giappone beve il vino nuovo per primo, per il fuso orario",
     "日本が新酒をいちばん早く飲めるのは、どうしてですか。 A. 時差の関係で　B. 飛行機が速いから　C. ぶどうが日本で取れるから", size=19, gap=6)
e.ex("A2", "scelta multipla", "B", "Hanshin Umeda vende circa 40 tipi di vino nuovo",
     "阪神梅田本店では、新酒を何種類売りますか。 A. 約4種類　B. 約40種類　C. 約400種類", size=19, gap=6)
e.head("B　ことば", 25)
e.bridge("言葉や数字を入れてください。")
e.ex("A2", "completamento", "解禁", "解禁 = il giorno in cui iniziano le vendite",
     "新酒を売り始める日を「___」と言います。", instr="Completa", size=19, gap=6)
e.ex("A2", "completamento", "収穫", "収穫 = il raccolto",
     "ぶどうを取ることを「___」と言います。", instr="Completa", size=19, gap=6)
e.ex("B1", "completamento", "19", "L'uscita, quest'anno: giovedì 19 novembre",
     "今年の解禁日は11月 ___ 日（木）です。", instr="Completa", size=19, gap=6)
e.ex("B1", "completamento", "40", "Hanshin Umeda vende circa 40 tipi di vino nuovo",
     "阪神梅田本店では、約 ___ 種類売ります。", instr="Completa", size=19, gap=6)
e.ex("A2", "completamento", "0", "L'uscita inizia a mezzanotte",
     "解禁日は、午前 ___ 時からです。", instr="Completa", size=19, gap=6)
e.head("C　文を作りましょう", 25)
e.bridge("言葉を並べて、正しい文を作ってください。")
e.ex("B1", "costruzione di frasi", "ボジョレー・ヌーヴォーはフランスの新酒です。", "soggetto + descrizione",
     "ボジョレー・ヌーヴォーは / フランスの / 新酒です → ___", instr="Costruisci una frase", size=19, gap=6)
e.ex("A2", "costruzione di frasi", "新酒は11月19日から売られます。", "tempo + verbo",
     "新酒は / 11月19日から / 売られます → ___", instr="Costruisci una frase", size=19, gap=6)
e.ex("B1", "costruzione di frasi", "屋台で食べ物を買います。", "luogo + oggetto + verbo",
     "屋台で / 食べ物を / 買います → ___", instr="Costruisci una frase", size=19, gap=6)
e.ex("B1", "costruzione di frasi", "秋の味覚を味わいます。", "oggetto + verbo",
     "秋の味覚を / 味わいます → ___", instr="Costruisci una frase", size=19, gap=6)
e.head("D　ペアにしましょう", 25)
e.match_set("B1", "abbinamento",
            ["ボジョレー・ヌーヴォー", "解禁", "収穫", "屋台"],
            ["ぶどうを取ること",
             "フランスの新酒",
             "祭りの食べ物を売る店",
             "新酒を売り始める日"],
            ["b", "d", "a", "c"],
            ["ボジョレー・ヌーヴォー = vino nuovo francese b", "解禁 = il giorno in cui iniziano le vendite d", "収穫 = il raccolto a", "屋台 = una bancarella che vende cibo c"],
            instr="Abbinare")
e.end_report()
p.foot(3)
p.save(f"{OUT}/p3-bunka.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4　スポーツ (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("スポーツ　体育", "Lucerna", "レベル B1　相撲3日目まで　Sumo: i primi tre giorni")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 1440, tag="P4-feature")
f.title("波乱の3日間 — 九州場所", 37)
f.byline("Lucerna編集部　読むレベル：B1")
f.para("大相撲の九州場所は、8日（日よう日）に福岡国際センターで始まりました。今年最後の本場所です。横綱は大の里と豊昇龍です。場所は、22日（日よう日）の千秋楽まで続きます。")
f.para("初日は、波乱でした。2場所連続優勝をねらう大の里が、小結の義ノ富士に突き落としで敗れました。3場所連続休場明けの豊昇龍は、新小結の美ノ海を押し出して勝ちました。大関は、3人のうち2人が敗れました。")
f.para("2日目は、両横綱と3人の大関が、みんな勝ちました。大の里は、藤凌駕を寄り切って初白星をあげました。豊昇龍と霧島は、2連勝です。")
f.para("3日目は、また波乱でした。豊昇龍が、藤凌駕に押し倒されて、初黒星になりました。藤凌駕の金星です。初土俵から11場所での金星は、年6場所になってから7番目の速さだそうです。大の里は、2勝目をあげました。")
f.para("3日目まで、大の里も豊昇龍も2勝1敗です。優勝は、まだ決まっていません。千秋楽の結果は、次号（VOL.5）でお知らせします。")
f.gloss("波乱 una sorpresa　ねらう puntare a　金星 una vittoria su uno yokozuna　初土俵 un debutto.")
f.head("3日目までの星取", 25)
f.box("九州場所の記録　3日目まで", [
    ("初日（8日）— 大の里 ●、豊昇龍 ○、霧島 ○、琴櫻 ●、安青錦 ●", "serif", False, INK, 20, 1.35),
    ("2日目（9日）— 両横綱と3大関がみんな勝ちました", "serif", False, INK, 20, 1.35),
    ("3日目（10日）— 豊昇龍 ●、大の里 ○、藤凌駕が金星", "serif", False, INK, 20, 1.35),
    ("3日目まで — 大の里 2勝1敗、豊昇龍 2勝1敗", "serif", False, INK, 20, 1.35),
    ("千秋楽 — 22日（日）、優勝はまだ決まっていません", "serif", False, GREY, 20, 1.35),
])
f.para("前号（VOL.3）では、場所の始まりだけをお知らせしました。今号で、3日目までの結果をお知らせします。")
f.gloss("前号 l'ultimo numero　星取 il bilancio di vittorie e sconfitte.")
f.end_report()

# col 3: yokozuna box + words box
ix = COLX[3]
ys = ["大の里 — 初日 ●、2日目 ○、3日目 ○",
      "豊昇龍 — 初日 ○、2日目 ○、3日目 ●",
      "2人とも、3日目まで2勝1敗です"]
sy3 = 200
sh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in ys) + 32
p.rect(ix, sy3, CW, sh, fill=BOX)
yy3 = sy3 + 16
p.text(ix + 22, yy3 + 26, "横綱の3日間", 24, "sans", True, OLIVE)
yy3 += 52
for t in ys:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ws = ["金星 — 前頭の力士が横綱に勝つこと",
      "千秋楽 — 場所の最後の日",
      "星取表 — 勝敗の表"]
wy3 = sy3 + sh + 26
wh = 62 + sum(len(wrap(t, "serif", False, 21.5, CW - 44)) * 30.5 + 33 for t in ws) + 32
p.rect(ix, wy3, CW, wh, fill=BOX)
yy3 = wy3 + 16
p.text(ix + 22, yy3 + 26, "相撲のことば", 24, "sans", True, OLIVE)
yy3 += 52
for t in ws:
    yy3 = p.para(ix + 22, yy3 + 21, t, 21.5, "serif", False, INK, CW - 44, 1.42) + 12
ot = "●は負け、○は勝ちです。金星は、前頭の力士が横綱に勝った時に言います。"
oy = wy3 + wh + 26
oh = 62 + len(wrap(ot, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap("※記録は各日の報道によるものです。3日目までの結果です。", "serif", False, 19.5, CW - 44)) * 27 + 20 + 8
p.rect(ix, oy, CW, oh, fill=BOX)
yy3 = oy + 16
p.text(ix + 22, yy3 + 26, "●と○の意味", 24, "sans", True, OLIVE)
yy3 += 52
yy3 = p.para(ix + 22, yy3 + 21, ot, 21.5, "serif", False, INK, CW - 44, 1.42) + 10
p.para(ix + 22, yy3 + 20, "※記録は各日の報道によるものです。3日目までの結果です。", 19.5, "serif", False, GREY, CW - 44, 1.38)
print("P4 col3 ends", oy + oh)

# ---- closing strip (full width) ----
ty = 1490
p.text(MX, ty + 26, "千秋楽は22日（日） — 優勝はまだ決まっていません", 26, "sans", True, OLIVE)
p.hline(MX, RIGHT, ty + 40, OLIVE, 2)
p.para(MX, ty + 78, "両横綱は2勝1敗で、まだ優勝の行方は分かりません。千秋楽は22日（日よう日）です。最後まで、だれが勝つか分からない場所です。最終結果は、次号（VOL.5）でお知らせします。", 20.5, "serif", False, INK, RIGHT - MX, 1.42)

# ---- P4 exercises ----
ey = 1840
p.hline(MX, RIGHT, ey - 12, OLIVE, 2)
p.text(MX, ey + 28, "練習　Esercizi pagina 4", 28, "sans", True, OLIVE)
p.text(RIGHT, ey + 28, "Risposte a pagina 8　I livelli sono mescolati — trova il tuo numero", 20, "sans", False, GREY, anchor="end")
e = Flow(p, [(COLX[i], CW) for i in range(4)], ey + 56, 2580, tag="P4-ex")
e.head("A　理解", 25)
e.bridge("第4版の文章を読んで、正しい答えを選んでください。")
e.ex("B1", "scelta multipla", "A", "Yoshinofuji ha battuto Ōnosato il giorno 1",
     "初日に大の里に勝ったのはだれですか。 A. 義ノ富士　B. 美ノ海　C. 藤凌駕", size=19, gap=6)
e.ex("B1", "scelta multipla", "B", "Chura-no-umi ha perso contro Hōshōryū il giorno 1",
     "初日に豊昇龍に敗れたのはだれですか。 A. 義ノ富士　B. 美ノ海　C. 宇良", size=19, gap=6)
e.ex("B1", "scelta multipla", "A", "Fujiryōga ha battuto Hōshōryū il giorno 3",
     "3日目に豊昇龍に勝ったのはだれですか。 A. 藤凌駕　B. 大の里　C. 霧島", size=19, gap=6)
e.ex("B1", "scelta multipla", "B", "I due yokozuna sono 2–1 dopo il giorno 3",
     "3日目まで、両横綱は何勝何敗ですか。 A. 3勝0敗　B. 2勝1敗　C. 1勝2敗", size=19, gap=6)
e.ex("B1", "scelta multipla", "C", "L'ultimo giorno è il 22 novembre (domenica)",
     "千秋楽はいつですか。 A. 15日（日）　B. 19日（木）　C. 22日（日）", size=19, gap=6)
e.head("B　数字", 25)
e.bridge("第4版の数字を入れてください。")
e.ex("B1", "completamento", "2", "Ōnosato ha vinto 2 incontri dopo il giorno 3",
     "大の里は3日目まで ___ 勝しています。", instr="Completa", size=19, gap=6)
e.ex("B1", "completamento", "2", "Anche Hōshōryū ha vinto 2 incontri dopo il giorno 3",
     "豊昇龍も3日目まで ___ 勝しています。", instr="Completa", size=19, gap=6)
e.ex("B1", "completamento", "11", "Kinboshi di Fujiryōga: 11° torneo dal debutto",
     "藤凌駕の金星は、初土俵から ___ 場所目でした。", instr="Completa", size=19, gap=6)
e.ex("B1", "completamento", "7", "7.º kinboshi più veloce dall'era dei sei tornei",
     "金星の速さは、年6場所制で ___ 番目です。", instr="Completa", size=19, gap=6)
e.ex("B1", "completamento", "8", "Il torneo di Kyushu è iniziato l'8 novembre (domenica)",
     "九州場所は11月 ___ 日（日）に始まりました。", instr="Completa", size=19, gap=6)
e.head("C　ことばと記録", 25)
e.bridge("第4版の記事から答えてください。")
e.ex("B1", "scelta multipla", "A", "金星 = un lottatore di basso rango batte uno yokozuna",
     "「金星」とは何ですか。 A. 前頭が横綱に勝つ　B. 横綱が大関に勝つこと　C. 優勝", size=19, gap=6)
e.ex("B1", "scelta multipla", "B", "千秋楽 = l'ultimo giorno del torneo",
     "「千秋楽」とは何ですか。 A. 場所の最初の日　B. 場所の最後の日　C. 休みの日", size=19, gap=6)
e.ex("B1", "scelta multipla", "A", "Il torneo di Kyushu è al Fukuoka Kokusai Center",
     "九州場所はどこですか。 A. 福岡国際センター　B. 横浜スタジアム　C. 東京ドーム", size=19, gap=6)
e.ex("B1", "scelta multipla", "B", "Hōshōryū torna dopo tre tornei di assenza",
     "3場所連続休場明けの横綱はだれですか。 A. 大の里　B. 豊昇龍　C. 霧島", size=19, gap=6)
e.head("D　正しい・正しくない", 25)
e.bridge("文が正しければ○、正しくなければ×を書いてください。")
e.ex("B1", "vero o falso", "×", "Ōnosato ha perso il giorno 1",
     "大の里は、初日に勝ちました。", instr="Vero o falso?", size=19, gap=6)
e.ex("B1", "vero o falso", "○", "Hōshōryū ha vinto i giorni 1 e 2",
     "豊昇龍は、初日と2日目に勝ちました。", instr="Vero o falso?", size=19, gap=6)
e.ex("B1", "vero o falso", "○", "Fujiryōga ha vinto un kinboshi il giorno 3",
     "藤凌駕は、3日目に金星をあげました。", instr="Vero o falso?", size=19, gap=6)
e.ex("B1", "vero o falso", "×", "Il campione non è ancora deciso",
     "優勝は、もう決まっています。", instr="Vero o falso?", size=19, gap=6)
e.end_report()
p.foot(4)
p.save(f"{OUT}/p4-supotsu.svg")
print("P4 saved, exercises so far:", len(REG))
