# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-ja-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え · Teste e respostas", "Lucerna", "第 8 面 · 週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "A Semana da Leitura termina a 9 de novembro (segunda-feira)",
     "読書週間は、11月9日（___）で終わります。(A. 月よう日 · B. 日よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "O dia do Pocky é 11 de novembro (quarta-feira)",
     "ポッキーの日は、11月11日（___）です。(A. 水よう日 · B. 金よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "O jogo 3 das Japan Series foi a 27 de outubro (terça-feira)",
     "日本シリーズの第3戦は、10月27日（___）でした。(A. 火よう日 · B. 水よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "Jogo 4: SoftBank ganhou 4-2",
     "第4戦は、ソフトバンクが ___ 対2で勝ちました。(A. 4 · B. 2)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "O Shichi-Go-San centra-se a 15 de novembro (domingo)",
     "七五三の中心の日は、11月 ___ 日（日）です。(A. 9 · B. 15)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "As folhas do monte Takao culminam a partir de 13 de novembro (sexta-feira)",
     "高尾山の見頃は、11月 ___ 日ごろからです。(A. 13 · B. 23)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "O dia do Pocky começou em 1999",
     "『ポッキー＆プリッツの日』は、___ 年に始まりました。(A. 1999 · B. 1989)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "O Ni-no-tori de Tori-no-ichi é 19 de novembro (quinta-feira)",
     "二の酉は、11月 ___ 日です。(A. 19 · B. 7)", size=13.8, gap=0)
f.head("B · 一般問題", 21, OLIVE, 5)
f.ex("A2", "múltipla escolha", "A", "O Shichi-Go-San celebra crianças de 3, 5 e 7 anos",
     "七五三は、だれのお祝いですか。 A. 3歳・5歳・7歳の子ども · B. 大人 · C. お年寄り", size=13.8, gap=0)
f.ex("B1", "múltipla escolha", "B", "As visitas culminam no início de novembro (26 %), diz o inquérito",
     "調査では、お参りがいちばん多いのはいつですか。 A. 11月15日 · B. 11月上旬 · C. 12月", size=13.8, gap=0)
f.ex("B1", "múltipla escolha", "A", "O MVP da série é Masaki Tomoya",
     "日本シリーズのMVPはだれですか。 A. 正木選手 · B. 山川選手 · C. 筒香選手", size=13.8, gap=0)
f.ex("B1", "múltipla escolha", "A", "O 13.º título de SoftBank",
     "ソフトバンクは、何度目の日本一ですか。 A. 13度目 · B. 3度目 · C. 1度目", size=13.8, gap=0)
f.ex("A2", "múltipla escolha", "A", "Chitose-ame é um doce comprido vermelho e branco",
     "千歳飴は、どんな飴ですか。 A. 赤と白の長い飴 · B. 黒い丸い飴 · C. 緑の四角い飴", size=13.8, gap=0)
f.ex("B2", "múltipla escolha", "A", "As datas previstas marcam o início da melhor estação",
     "紅葉の予報の日にちは、何ですか。 A. 見頃が始まる目安 · B. いちばん美しい日 · C. 落葉の日", size=13.8, gap=0)
f.ex("B2", "múltipla escolha", "A", "74 % das famílias tiram fotos num estúdio, diz o inquérito",
     "写真館で撮る家庭は何%ですか。 A. 74% · B. 71% · C. 26%", size=13.8, gap=0)
f.ex("A2", "múltipla escolha", "A", "O slogan é 「静かだけど、冒険中。」",
     "読書週間のスローガンは？ A. 静かだけど、冒険中。 · B. 本の秋 · C. 紅葉の秋", size=13.8, gap=0)
f.head("C · 読んで答えましょう", 21, OLIVE, 5)
f.para("ユウは中学生です。今週の月よう日は、読書週間の最後の日です。ユウは図書館で借りた本を読みます。水よう日には、友達とポッキーを分けます。金よう日には、高尾山へ紅葉を見に行くつもりです。日よう日には、妹の七五三で神社へ行きます。", 15, lh=1.3, split=False)
f.ex("A2", "múltipla escolha", "B", "À segunda-feira lê um livro da biblioteca",
     "ユウは月よう日に何をしますか。 A. 神社へ行く · B. 図書館で借りた本を読む · C. ポッキーを買う", size=13.8, gap=0)
f.ex("A2", "múltipla escolha", "B", "À quarta-feira partilha Pocky com amigos",
     "水よう日に何をしますか。 A. 高尾山へ行く · B. 友達とポッキーを分ける · C. 神社へ行く", size=13.8, gap=0)
f.ex("A2", "múltipla escolha", "A", "À sexta-feira vai ao monte Takao ver as folhas",
     "金よう日にどこへ行きますか。 A. 高尾山 · B. 神社 · C. 図書館", size=13.8, gap=0)
f.ex("B1", "múltipla escolha", "B", "Ao domingo vai a um santuário pelo Shichi-Go-San da irmã",
     "日よう日にどこへ行きますか。 A. 高尾山 · B. 神社 · C. 浅草", size=13.8, gap=0)
f.head("D · 文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "construção de frases", "私は水よう日に友達とポッキーを分けます。", "sujeito + tempo + objeto + verbo",
     "私は / 水よう日に / 友達とポッキーを分けます → ___", instr="Construa uma frase", size=13.8, gap=0)
f.ex("A2", "construção de frases", "七五三は子どものお祝いです。", "七五三 = uma celebração para crianças",
     "七五三は / 子どもの / お祝いです → ___", instr="Construa uma frase", size=13.8, gap=0)
f.ex("B1", "construção de frases", "神社で千歳飴をもらいます。", "Usa 「で」 para o lugar",
     "神社で / 千歳飴を / もらいます → ___", instr="Construa uma frase", size=13.8, gap=0)
f.ex("B1", "construção de frases", "ソフトバンクは4連勝で日本一になりました。", "Quatro vitórias seguidas trouxeram o título",
     "ソフトバンクは / 4連勝で / 日本一になりました → ___", instr="Construa uma frase", size=13.8, gap=0)
f.head("E · 翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "tradução", "O Shichi-Go-San é 15 de novembro.", "Ver página 3",
     "七五三は11月15日です。 → ___", instr="Traduza", size=13.8, gap=0)
f.ex("B1", "tradução", "O dia do Pocky começou em 1999.", "Ver página 2",
     "『ポッキー＆プリッツの日』は1999年に始まりました。 → ___", instr="Traduza", size=13.8, gap=0)
f.ex("B1", "tradução", "読書週間は10月27日から始まります。", "Ver página 7",
     "A Semana da Leitura começa a 27 de outubro. → ___", instr="Traduza", size=13.8, gap=0)
f.ex("B2", "tradução", "紅葉を見に行く人は、北から南へ、見頃を追いかけることができます。", "Ver página 6 (atrás da melhor estação)",
     "Quem vai ver as folhas pode ir atrás da melhor estação de norte para sul. → ___", instr="Traduza", size=13.8, gap=0)
f.head("F · 今週のことば", 21, OLIVE, 5)
f.match_set("B2", "associação",
            ["七五三", "千歳飴", "落葉", "見頃"],
            ["木から落ちた葉",
             "3歳・5歳・7歳の子どものお祝い",
             "紅葉がいちばん美しい時",
             "赤と白の長い飴"],
            ["b", "d", "a", "c"],
            ["七五三 = uma celebração para crianças de 3, 5 e 7 anos b", "千歳飴 = doce comprido vermelho e branco d", "落葉 = folhas caídas a", "見頃 = a melhor estação c"],
            instr="Ligue palavra e sentido")
f.head("G · 神社で", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "お参りします = ir rezar",
     "— 七五三ですね。— はい、神社へ ___ ます。(A. お参りに行き · B. お参りに行か)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "撮ります = tirar uma foto",
     "— 写真を ___ か。 (A. 撮ります · B. 撮った)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "O Shichi-Go-San centra-se a 15 de novembro (página 3)",
     "— 七五三はいつですか。— 11月 ___ 日です。(A. 15 · B. 9)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "千歳飴 é popular",
     "— おすすめはありますか。— 『___ 』が人気です。(A. 千歳飴 · B. ポッキー)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "どういたしまして = de nada",
     "— ありがとうございました。— ___ 。(A. どういたしまして · B. さようなら)", size=13.8, gap=0)
f.head("H · 書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の11月の1週間は、本と秋の1週間です。"
          "月よう日は、読書週間の最後の日です。図書館で借りた本を読みます。"
          "水よう日は、友達とポッキーを分けます。1が4つ並ぶ日です。"
          "金よう日は、高尾山へ紅葉を見に行きます。"
          "日よう日は、妹の七五三です。神社へ行って、写真を撮ります。"
          "11月は短いですが、楽しいことが多い季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.bridge(f"Tarefa de redação (sem uma única resposta certa); o texto modelo ({NCHARS} caracteres) está abaixo.")
f.ex("B1", "redação", "(tarefa aberta — texto modelo abaixo)", f"Texto modelo na secção H desta página ({NCHARS} caracteres)",
     "『私の11月の1週間』について、150〜200字で書いてください。読書、七五三、紅葉の中から一つ選んでください。", instr="Redação", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 答え =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答え · Respostas — agrupadas por página; encontra só o teu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Uma breve nota em português com cada resposta · ✓ = o exercício com texto modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Página {pg} —", 12.9, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "redação":
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
