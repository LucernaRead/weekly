# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-fr/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え · Test et réponses", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "texte à trous", "A", "La Semaine de la lecture se termine le 9 novembre (lundi)",
     "読書週間は、11月9日（___）で終わります。(A. 月よう日 · B. 日よう日)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "Le jour des Pocky, c'est le 11 novembre (mercredi)",
     "ポッキーの日は、11月11日（___）です。(A. 水よう日 · B. 金よう日)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "Le match 3 des Japan Series a eu lieu le 27 octobre (mardi)",
     "日本シリーズの第3戦は、10月27日（___）でした。(A. 火よう日 · B. 水よう日)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "Match 4 : SoftBank a gagné 4-2",
     "第4戦は、ソフトバンクが ___ 対2で勝ちました。(A. 4 · B. 2)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "B", "Shichi-Go-San se concentre le 15 novembre (dimanche)",
     "七五三の中心の日は、11月 ___ 日（日）です。(A. 9 · B. 15)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "Les feuilles du mont Takao culminent dès le 13 novembre (vendredi)",
     "高尾山の見頃は、11月 ___ 日ごろからです。(A. 13 · B. 23)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "Le jour des Pocky a commencé en 1999",
     "『ポッキー＆プリッツの日』は、___ 年に始まりました。(A. 1999 · B. 1989)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "Ni-no-tori de Tori-no-ichi, c'est le 19 novembre (jeudi)",
     "二の酉は、11月 ___ 日です。(A. 19 · B. 7)", size=13.8, gap=0)
f.head("B · 一般問題", 21, OLIVE, 5)
f.ex("A2", "choix multiple", "A", "Shichi-Go-San fête les enfants de 3, 5 et 7 ans",
     "七五三は、だれのお祝いですか。 A. 3歳・5歳・7歳の子ども · B. 大人 · C. お年寄り", size=13.8, gap=0)
f.ex("B1", "choix multiple", "B", "Les visites culminent début novembre (26 %), dit l'enquête",
     "調査では、お参りがいちばん多いのはいつですか。 A. 11月15日 · B. 11月上旬 · C. 12月", size=13.8, gap=0)
f.ex("B1", "choix multiple", "A", "Le MVP de la série est Masaki Tomoya",
     "日本シリーズのMVPはだれですか。 A. 正木選手 · B. 山川選手 · C. 筒香選手", size=13.8, gap=0)
f.ex("B1", "choix multiple", "A", "Le 13e titre de SoftBank",
     "ソフトバンクは、何度目の日本一ですか。 A. 13度目 · B. 3度目 · C. 1度目", size=13.8, gap=0)
f.ex("A2", "choix multiple", "A", "Chitose-ame est un long bonbon rouge et blanc",
     "千歳飴は、どんな飴ですか。 A. 赤と白の長い飴 · B. 黒い丸い飴 · C. 緑の四角い飴", size=13.8, gap=0)
f.ex("B2", "choix multiple", "A", "Les dates prévues marquent le début de la meilleure saison",
     "紅葉の予報の日にちは、何ですか。 A. 見頃が始まる目安 · B. いちばん美しい日 · C. 落葉の日", size=13.8, gap=0)
f.ex("B2", "choix multiple", "A", "74 % des familles font des photos en studio, dit l'enquête",
     "写真館で撮る家庭は何%ですか。 A. 74% · B. 71% · C. 26%", size=13.8, gap=0)
f.ex("A2", "choix multiple", "A", "Le slogan est 「静かだけど、冒険中。」",
     "読書週間のスローガンは？ A. 静かだけど、冒険中。 · B. 本の秋 · C. 紅葉の秋", size=13.8, gap=0)
f.head("C · 読んで答えましょう", 21, OLIVE, 5)
f.para("ユウは中学生です。今週の月よう日は、読書週間の最後の日です。ユウは図書館で借りた本を読みます。水よう日には、友達とポッキーを分けます。金よう日には、高尾山へ紅葉を見に行くつもりです。日よう日には、妹の七五三で神社へ行きます。", 15, lh=1.3, split=False)
f.ex("A2", "choix multiple", "B", "Le lundi, il lit un livre de la bibliothèque",
     "ユウは月よう日に何をしますか。 A. 神社へ行く · B. 図書館で借りた本を読む · C. ポッキーを買う", size=13.8, gap=0)
f.ex("A2", "choix multiple", "B", "Le mercredi, il partage des Pocky avec des amis",
     "水よう日に何をしますか。 A. 高尾山へ行く · B. 友達とポッキーを分ける · C. 神社へ行く", size=13.8, gap=0)
f.ex("A2", "choix multiple", "A", "Le vendredi, il va au mont Takao voir les feuilles",
     "金よう日にどこへ行きますか。 A. 高尾山 · B. 神社 · C. 図書館", size=13.8, gap=0)
f.ex("B1", "choix multiple", "B", "Le dimanche, il va au sanctuaire pour le Shichi-Go-San de sa sœur",
     "日よう日にどこへ行きますか。 A. 高尾山 · B. 神社 · C. 浅草", size=13.8, gap=0)
f.head("D · 文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "construction de phrases", "私は水よう日に友達とポッキーを分けます。", "sujet + temps + objet + verbe",
     "私は / 水よう日に / 友達とポッキーを分けます → ___", instr="Former une phrase", size=13.8, gap=0)
f.ex("A2", "construction de phrases", "七五三は子どものお祝いです。", "七五三 = une fête pour les enfants",
     "七五三は / 子どもの / お祝いです → ___", instr="Former une phrase", size=13.8, gap=0)
f.ex("B1", "construction de phrases", "神社で千歳飴をもらいます。", "「で」 pour le lieu",
     "神社で / 千歳飴を / もらいます → ___", instr="Former une phrase", size=13.8, gap=0)
f.ex("B1", "construction de phrases", "ソフトバンクは4連勝で日本一になりました。", "Quatre victoires d'affilée ont apporté le titre",
     "ソフトバンクは / 4連勝で / 日本一になりました → ___", instr="Former une phrase", size=13.8, gap=0)
f.head("E · 翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "traduction", "Shichi-Go-San, c'est le 15 novembre.", "Voir page 3",
     "七五三は11月15日です。 → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "traduction", "Le jour des Pocky a commencé en 1999.", "Voir page 2",
     "『ポッキー＆プリッツの日』は1999年に始まりました。 → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B1", "traduction", "読書週間は10月27日から始まります。", "Voir page 7",
     "La Semaine de la lecture commence le 27 octobre. → ___", instr="Traduire", size=13.8, gap=0)
f.ex("B2", "traduction", "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。", "Voir page 6 (à la poursuite de la meilleure saison)",
     "Ceux qui vont voir les feuilles peuvent courir après la meilleure saison du nord au sud. → ___", instr="Traduire", size=13.8, gap=0)
f.head("F · 今週のことば", 21, OLIVE, 5)
f.match_set("B2", "association",
            ["七五三", "千歳飴", "落葉", "見頃"],
            ["木から落ちた葉",
             "3歳・5歳・7歳の子どものお祝い",
             "紅葉がいちばん美しい時",
             "赤と白の長い飴"],
            ["b", "d", "a", "c"],
            ["七五三 = une fête pour les enfants de 3, 5 et 7 ans b", "千歳飴 = long bonbon rouge et blanc d", "落葉 = feuilles tombées a", "見頃 = le meilleur moment c"],
            instr="Associer mots et sens")
f.head("G · 神社で", 21, OLIVE, 5)
f.ex("B1", "texte à trous", "A", "お参りします = aller prier",
     "— 七五三ですね。— はい、神社へ ___ ます。(A. お参りに行き · B. お参りに行か)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "撮ります = prendre une photo",
     "— 写真を ___ か。 (A. 撮ります · B. 撮った)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "Shichi-Go-San se concentre le 15 novembre (page 3)",
     "— 七五三はいつですか。— 11月 ___ 日です。(A. 15 · B. 9)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "千歳飴 est populaire",
     "— おすすめはありますか。— 『___ 』が人気です。(A. 千歳飴 · B. ポッキー)", size=13.8, gap=0)
f.ex("B1", "texte à trous", "A", "どういたしまして = je vous en prie",
     "— ありがとうございました。— ___ 。(A. どういたしまして · B. さようなら)", size=13.8, gap=0)
f.head("H · 書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の11月の1週間は、本と秋の1週間です。"
          "月よう日は、読書週間の最後の日です。図書館で借りた本を読みます。"
          "水よう日は、友達とポッキーを分けます。1が4つ並ぶ日です。"
          "金よう日は、高尾山へ紅葉を見に行きます。"
          "日よう日は、妹の七五三です。神社へ行って、写真を撮ります。"
          "11月は短いですが、楽しいことが多い季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.bridge(f"Tâche d'écriture (pas de réponse unique) ; le texte modèle ({NCHARS} caractères) est ci-dessous.")
f.ex("B1", "rédaction", "(tâche ouverte — texte modèle ci-dessous)", f"Texte modèle dans la section H de cette page ({NCHARS} caractères)",
     "『私の11月の1週間』について、150〜200字で書いてください。読書、七五三、紅葉の中から一つ選んでください。", instr="Rédaction", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 答え =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答え · Réponses — groupées par page ; cherche juste ton numéro", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Une courte note en français avec chaque réponse · ✓ = l'exercice au texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Page {pg} —", 12.9, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "rédaction":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 12.9, lh=1.13, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-tesuto.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model chars:", NCHARS)
