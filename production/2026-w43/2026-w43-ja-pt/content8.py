# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-ja-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · テストと答え =================
CURPAGE[0] = 8
p = BSPage4()
p.band("テストと答え · Teste e respostas", "Lucerna", "Página 8 · 週の大きなテスト + 全ての答え")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · 週のクロニクル", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "O jogo 1 é no sábado, 24 de outubro",
     "日本シリーズの第1戦は、10月24日（___）です。(A. 土よう日 · B. 日よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "O último dia dos Jogos Para-Asiáticos também é 24",
     "アジアパラ競技大会の最終日も、___ 日です。(A. 24 · B. 25)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "O Jidai Matsuri foi na quinta, 22 de outubro",
     "時代祭は、10月 ___ 日（木）でした。(A. 22 · B. 24)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Venda geral: dia 22, às 12h",
     "日本シリーズのチケットの一般発売は、___ 日12時でした。(A. 20 · B. 22)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "O Irohazaka tem o auge a partir de sexta, dia 23",
     "日光のいろは坂の見頃は、___ 日（金）からです。(A. 23 · B. 15)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "O total dos Geraldon: 1.342 pontos",
     "ジェラードンの合計点は、___ 点でした。(A. 671 · B. 1,342)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "A Semana da Leitura começa na terça, 27 de outubro",
     "読書週間は、10月 ___ 日（火）からです。(A. 27 · B. 31)", size=13.8, gap=0)
f.ex("B1", "cloze", "B", "Halloween é no sábado, 31 de outubro",
     "ハロウィンは、10月 ___ 日（土）です。(A. 30 · B. 31)", size=13.8, gap=0)
f.head("B · 一般問題", 21, OLIVE, 5)
f.ex("A2", "escolha múltipla", "B", "Participaram 45 países e regiões",
     "アジアパラ競技大会に参加した国と地域は？ A. 18 · B. 45 · C. 282", size=13.8, gap=0)
f.ex("A2", "escolha múltipla", "A", "Atletas japoneses: 282",
     "日本の選手は何人でしたか。 A. 282人 · B. 120人 · C. 17人", size=13.8, gap=0)
f.ex("B1", "escolha múltipla", "A", "O tempo da Toyo: 10h31min30s",
     "予選会で1位の東洋大学のタイムは？ A. 10時間31分30秒 · B. 1分46秒 · C. 9時間31分", size=13.8, gap=0)
f.ex("B1", "escolha múltipla", "B", "1min46s = 106 segundos",
     "法政大学は国士舘大学より何秒速かったですか。 A. 33秒 · B. 106秒 · C. 46秒", size=13.8, gap=0)
f.ex("A2", "escolha múltipla", "C", "As avaliações de mochi: +168%",
     "『餅』の口コミは何%増えましたか。 A. 82% · B. 84% · C. 168%", size=13.8, gap=0)
f.ex("B1", "escolha múltipla", "A", "Multa por lixo: 2.000 ienes",
     "渋谷でゴミを捨てた時の罰金は？ A. 2,000円 · B. 1,000万円 · C. 900円", size=13.8, gap=0)
f.ex("A2", "escolha múltipla", "B", "A exposição do Shosoin vai até 9 de novembro",
     "正倉院展はいつまでですか。 A. 11月1日 · B. 11月9日 · C. 10月31日", size=13.8, gap=0)
f.ex("B1", "escolha múltipla", "C", "SoftBank: 91 vitórias na temporada",
     "ソフトバンクのレギュラーシーズンの勝ち数は？ A. 71 · B. 49 · C. 91", size=13.8, gap=0)
f.head("C · 読んで答えましょう", 21, OLIVE, 5)
f.para("ケンは大学生です。今週の土よう日、横浜スタジアムで日本シリーズの第1戦があります。ケンはチケットを買うことができませんでしたから、テレビで応援します。日よう日は、奈良の正倉院展へ行くつもりです。来週の読書週間には、図書館で本を3冊借りたいと思っています。", 15, lh=1.3, split=False)
f.ex("A2", "escolha múltipla", "B", "No sábado, Ken torce pela TV",
     "ケンは土よう日に何をしますか。 A. スタジアムへ行く · B. テレビで応援する · C. 奈良へ行く", size=13.8, gap=0)
f.ex("A2", "escolha múltipla", "B", "Porque não conseguiu comprar ingresso",
     "ケンはなぜスタジアムへ行きませんか。 A. 時間がない · B. チケットが買えなかった · C. 雨だった", size=13.8, gap=0)
f.ex("A2", "escolha múltipla", "A", "No domingo, a exposição do Shosoin",
     "日よう日の予定は？ A. 正倉院展 · B. 図書館 · C. ハロウィン", size=13.8, gap=0)
f.ex("B1", "escolha múltipla", "B", "Na Semana da Leitura, quer pegar 3 livros",
     "読書週間に借りたい本は？ A. 2冊 · B. 3冊 · C. 9冊", size=13.8, gap=0)
f.head("D · 文を作りましょう", 21, OLIVE, 5)
f.ex("A2", "construção de frases", "私は土よう日に試合を見ます。", "Sujeito + tempo + objeto + verbo",
     "私は / 土よう日に / 試合を見ます → ___", instr="Construa a frase", size=13.8, gap=0)
f.ex("A2", "construção de frases", "紅葉は今週末が見頃です。", "見頃 = o período de maior beleza",
     "紅葉は / 今週末が / 見頃です → ___", instr="Construa a frase", size=13.8, gap=0)
f.ex("B1", "construção de frases", "図書館で本を借ります。", "O lugar da ação leva «で»",
     "図書館で / 本を / 借ります → ___", instr="Construa a frase", size=13.8, gap=0)
f.ex("B1", "construção de frases", "ジェラードンは1,342点で優勝しました。", "Pontos + で + 優勝 (vencer)",
     "ジェラードンは / 1,342点で / 優勝しました → ___", instr="Construa a frase", size=13.8, gap=0)
f.head("E · 翻訳しましょう", 21, OLIVE, 5)
f.ex("A2", "tradução", "O cortejo parte do Kyoto Gyoen às 12.", "Veja a página 3",
     "行列は京都御苑を12時に出発します。 → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "tradução", "Se jogar lixo, a multa é de 2.000 ienes.", "Veja a página 5",
     "ゴミを捨てると、2,000円の罰金です。 → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "tradução", "読書週間は来週の火よう日から始まります。", "Veja a página 7",
     "A Semana da Leitura começa na próxima terça-feira. → ___", instr="Traduza para o japonês", size=13.8, gap=0)
f.ex("B2", "tradução", "私は池袋のハロウィンのイベントに行きたいです。", "Veja a página 5 (o evento de Ikebukuro)",
     "Quero ir ao evento de Halloween de Ikebukuro. → ___", instr="Traduza para o japonês", size=13.8, gap=0)
f.head("F · 今週のことば", 21, OLIVE, 5)
f.match_set("B2", "associação",
            ["見頃", "福袋", "行列", "勝率"],
            ["勝った割合（.650など）",
             "花や紅葉がいちばん美しい時",
             "中身が見えない本のセット",
             "昔の服を着た人の列"],
            ["b", "c", "d", "a"],
            ["見頃 = o período de maior beleza (b)", "福袋 = um pacote-surpresa de livros (c)", "行列 = um cortejo (d)", "勝率 = porcentagem de vitórias (a)"],
            instr="Associe as palavras")
f.head("G · 図書館で", 21, OLIVE, 5)
f.ex("B1", "cloze", "A", "見せてください = mostre, por favor",
     "— 本を借りたいです。— はい、カードを ___ ください。(A. 見せて · B. 見て)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "借りられます = pode pegar (forma potencial)",
     "— 3冊、___ か。 (A. 借りられます · B. 借りますた)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "A Semana da Leitura começa na terça (página 7)",
     "— いつ返しますか。— 読書週間が始まる ___ に返します。(A. 火よう日 · B. 土よう日)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "A «fukubukuro de livros» é o sucesso da biblioteca",
     "— おすすめはありますか。— 『本の ___ 』が人気です。(A. 福袋 · B. 行列)", size=13.8, gap=0)
f.ex("B1", "cloze", "A", "どういたしまして = de nada",
     "— ありがとうございました。— ___ 。(A. どういたしまして · B. さようなら)", size=13.8, gap=0)
f.head("H · 書いてみましょう", 21, OLIVE, 5)
MODELO = ("私の秋の週末は、スポーツと読書の週末です。"
          "土よう日は、友達と家で日本シリーズを見ます。私はDeNAを応援します。"
          "試合の後は、近くの公園へ紅葉を見に行きます。"
          "日よう日は、図書館で借りた本を読みます。"
          "読書週間も始まりますから、静かな場所で大きな冒険をしたいです。"
          "秋は短いですが、楽しいことが多い季節です。")
NCHARS = len(MODELO.replace(" ", ""))
f.expl(f"Tarefa de escrita (sem uma única resposta certa); o texto-modelo ({NCHARS} caracteres) está abaixo.")
f.ex("B1", "escrita", "(tarefa aberta — texto-modelo abaixo)", f"Texto-modelo na seção H desta página ({NCHARS} caracteres)",
     "『私の秋の週末』について、150〜200字で書いてください。スポーツ、紅葉、読書の中から一つ選んでください。", instr="Escreva", size=13.8, gap=0)
f.para("例： " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

# ================= 答え =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "答え · Respostas — agrupadas por página: basta procurar o seu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Uma nota breve em português para cada resposta · ✓ = a pergunta com o texto-modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— Página {pg} —", 13.3, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "escrita":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.3, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-tesuto.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model chars:", NCHARS)
