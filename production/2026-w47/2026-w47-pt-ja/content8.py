# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　練習と解答", "A Lucerna", "8ページ　今週の大テスト + すべての解答")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "空所補充", "A", "11月20日金曜日は全国の祝日です",
     "Sexta, 20 de novembro, é ___ no Brasil. (A. feriado nacional · B. dia útil)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "祝日はズンビ・ドス・パルマレスを記念します",
     "O feriado lembra a morte de ___ . (A. Zumbi dos Palmares · B. Deodoro da Fonseca)", size=14.5, gap=0)
f.ex("B1", "空所補充", "B", "2026年の祝日は金曜日に当たります",
     "Em 2026, o feriado cai numa ___ . (A. segunda · B. sexta)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "コパ・ド・ブラジルの決勝は12月6日です",
     "A final da Copa do Brasil é no dia ___ de dezembro. (A. 6 · B. 15)", size=14.5, gap=0)
f.ex("B1", "空所補充", "B", "決勝：グレミオ × パルメイラス",
     "Na final, jogam Grêmio e ___ . (A. Vasco · B. Palmeiras)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "公式の解答は11月末までに発表されます",
     "O gabarito oficial sai até o ___ de novembro. (A. fim · B. dia 8)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "Enemの2日目は11月15日です",
     "O segundo dia do Enem foi no domingo ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.ex("B1", "空所補充", "B", "2日目の試験は5時間です",
     "No dia 15, a prova dura ___ horas. (A. três · B. cinco)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "1つ選ぼう", "B", "2023年の法律で11月20日が全国の祝日になりました",
     "A Lei nº 14.759, de 2023... A. criou o dia 20 · B. fez do dia 20 feriado nacional · C. acabou com o feriado", size=14.5, gap=0)
f.ex("B1", "1つ選ぼう", "A", "グレミオは合計3–1で勝ち進みました",
     "O Grêmio passou à final com... A. 3 a 1 no total · B. 2 a 2 no total · C. 1 a 0 no total", size=14.5, gap=0)
f.ex("B1", "1つ選ぼう", "B", "PK戦5–4：パルメイラスが勝ち進みました",
     "Nos pênaltis, o Palmeiras venceu por... A. 4 a 3 · B. 5 a 4 · C. 6 a 5", size=14.5, gap=0)
f.ex("B1", "1つ選ぼう", "B", "ノリスがサンパウロGPで優勝しました",
     "O Grande Prêmio de São Paulo foi vencido por... A. Verstappen · B. Norris · C. Hadjar", size=14.5, gap=0)
f.ex("B1", "1つ選ぼう", "A", "第36節：パルメイラス × フラメンゴは土曜日21日",
     "A rodada 36 tem Palmeiras × Flamengo no... A. sábado 21 · B. domingo 22 · C. dia 15", size=14.5, gap=0)
f.ex("A2", "1つ選ぼう", "B", "カポエイラはアフロブラジル人の格闘技と音楽の芸術です",
     "A capoeira é... A. um jogo de cartas · B. uma arte afro-brasileira de luta e música · C. um prato típico", size=14.5, gap=0)
f.ex("B2", "1つ選ぼう", "A", "10 公式の解答までの平日の日数です",
     "O número 10, na página 6, mede... A. os dias úteis até o gabarito · B. os gols da final · C. os feriados", size=14.5, gap=0)
f.ex("B1", "1つ選ぼう", "A", "パルマレスはアラゴアス州にありました",
     "O Quilombo dos Palmares ficava... A. em Alagoas · B. no Rio · C. em São Paulo", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Rafael mora em Salvador. Na sexta, 20, ele não trabalha: é feriado nacional. De manhã, ele vai a uma roda de capoeira no Pelourinho. À tarde, ele lê sobre Zumbi e Palmares e escreve duas frases em português. No sábado, 21, ele assiste a Palmeiras × Flamengo na televisão. No domingo, 22, ele descansa e prepara a semana: na segunda, ele volta ao trabalho e confere o gabarito extraoficial do Enem.", 15.5, lh=1.3, split=False)
f.ex("A2", "1つ選ぼう", "B", "ラファエルはサルヴァドールに住んでいます",
     "Onde mora Rafael? A. no Rio · B. em Salvador · C. em Brasília", size=14.5, gap=0)
f.ex("A2", "1つ選ぼう", "B", "金曜日、彼はカポエイラの集まりに行きます",
     "Na sexta, 20, Rafael... A. trabalha · B. vai a uma roda de capoeira · C. faz o Enem", size=14.5, gap=0)
f.ex("A2", "1つ選ぼう", "A", "土曜日、彼はパルメイラスを見ます × フラメンゴ",
     "No sábado, 21, Rafael assiste... A. a Palmeiras × Flamengo · B. ao Enem · C. a uma aula", size=14.5, gap=0)
f.ex("A2", "1つ選ぼう", "B", "月曜日、彼は非公式の解答を確かめます",
     "Na segunda, Rafael confere... A. o gabarito oficial · B. o gabarito extraoficial · C. a nota final", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "文を作ろう", "Sexta é feriado nacional.", "時間のことばが先に来ます",
     "sexta / é / feriado nacional → ___", instr="文を作ろう", size=14.5, gap=0)
f.ex("B1", "文を作ろう", "O Grêmio empatou por 1 a 1.", "主語 + 動詞 + 方法",
     "o grêmio / empatou / por 1 a 1 → ___", instr="文を作ろう", size=14.5, gap=0)
f.ex("B1", "文を作ろう", "Quando sair o gabarito, confira as respostas.", "時の従属節 + 主節",
     "quando / sair / o gabarito / confira / as respostas → ___", instr="文を作ろう", size=14.5, gap=0)
f.ex("B1", "文を作ろう", "O Brasil lembra Zumbi em 20 de novembro.", "主語 + 動詞 + 目的語 + 時間",
     "o brasil / lembra / zumbi / em 20 de novembro → ___", instr="文を作ろう", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "訳", "11月20日金曜日は全国の祝日です。", "1ページの見出しを見よう",
     "Sexta, 20 de novembro, é feriado nacional. → ___", instr="訳", size=14.5, gap=0)
f.ex("B1", "訳", "パルメイラスはPK戦で5–4で勝ちました。", "nos pênaltis = PK戦で",
     "O Palmeiras venceu nos pênaltis por 5 a 4. → ___", instr="訳", size=14.5, gap=0)
f.ex("B1", "訳", "O gabarito oficial sai até o fim de novembro.", "oficial = 公式の",
     "“公式の解答は11月末までに発表されます。” → ___", instr="訳", size=14.5, gap=0)
f.ex("B2", "訳", "Anote as suas respostas e confira quando sair o gabarito oficial.", "命令形 anote/confira + quando 従属節",
     "“自分の答えを書き留めて、公式の解答が出たら確かめよう。” → ___", instr="訳", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "語彙の組み合わせ",
            ["a consciência", "o gabarito", "o feriadão", "o agregado"],
            ["o placar dos dois jogos somados",
             "um fim de semana de três dias com feriado",
             "o saber e a memória de uma história",
             "as respostas oficiais das questões objetivas"],
            ["c", "d", "b", "a"],
            ["consciência=知ることと覚えること c", "gabarito=選択問題の公式の解答 d", "feriadão=祝日を含む3日間の週末 b", "agregado=2試合の合計スコア a"],
            instr="ペアを作ろう")
f.head("G　DIÁLOGO NA BILHETERIA", 22, OLIVE, 5)
f.ex("B1", "空所補充", "A", "マネ・ガリンシャ競技場",
     "— O jogo é no ___ Garrincha. (A. Mané · B. Maracanã)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "グレミオは6度目の優勝をねらいます",
     "— O Grêmio busca o ___ título. (A. sexto · B. primeiro)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "パルメイラスは5度目の優勝をねらいます",
     "— E o Palmeiras busca o ___ . (A. quinto · B. décimo)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "チケットはネットで売っています",
     "— Os ingressos estão à venda ___ internet. (A. na · B. no)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "obrigado = ありがとう",
     "— Boa final! — Muito ___! (A. obrigado · B. tarde)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Sexta, 20 de novembro, acordo sem despertador: é feriado nacional. "
          "De manhã, leio sobre Zumbi e Palmares e escrevo duas frases em português. "
          "À tarde, vou a uma roda de capoeira no bairro e ouço histórias de resistência. "
          "No sábado, assisto a Palmeiras × Flamengo na televisão, com a família. "
          "No domingo, descanso, preparo a semana e confiro o gabarito extraoficial do Enem. "
          "Na segunda, volto ao trabalho com calma: o feriadão foi curto, mas a memória fica. "
          "O dia 20 lembra a luta e a cultura afro-brasileiras.")
NWORDS = len(MODELO.split())
f.bridge(f"作文の課題（正解は1つではありません）。模範文（{NWORDS}語）は下です。")
f.ex("B1", "作文", "（自由課題 — 模範文は下です）", f"模範文はこのページのHの部分にあります（{NWORDS}語）",
     "«O seu feriadão de 20 a 22 de novembro» Escreva 80–100 palavras: o que você faz na sexta, no sábado e no domingo, e o que a data de 20 de novembro lembra.", instr="作文", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False, max_w=395)  # fix1 D7 (2026-11-11): wrap at 395, not the full 422.5 column — Cairo renders Newsreader ~3% wider than PIL measures, so two lines crossed the column edge 1862 (+2/+14px). Words, size (15) and 88-word count unchanged; worst line PIL 387.0, predicted rendered ink right ~1841.
f.end_report()
print("P8 exercises end y:", f.y, "col:", f.ci)

# ---- P8 image: the final stadium (col 3, below the exercises flow) ----
# The exercise flow fills cols 0-2 to the bottom; only its last column has
# free space below f.y, so the image goes there, positioned dynamically.
iy8 = (f.y + 12) if f.ci == 3 else 190
img_h = min(250, 1150 - iy8)
assert img_h >= 150, f"P8 image has no room: f.y={f.y} ci={f.ci}"
image(p, "garrincha.jpg", COLX[3], iy8, CW, img_h)
cap_end = caption(p, COLX[3], iy8 + img_h, CW,
        "O estádio Mané Garrincha, em Brasília: a final é no dia 6 de dezembro.",
        "Foto: Luis Dantas — Domínio público")
print("P8 image ends ~", cap_end)

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　解答 — ページごとに並んでいます。番号を探そう", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "答えごとに短い解説があります　✓ は模範文です", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "作文":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.5, lh=1.16, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-avaliacao.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
