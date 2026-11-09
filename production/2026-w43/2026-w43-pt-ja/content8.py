# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　評価と解答", "A Lucerna", "8ページ　A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", '穴埋め選択', "B", 'voltar às urnas = 投票に行く',
     "No domingo, o Brasil volta ___ para o segundo turno. (A. às escolas · B. às urnas)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "A", '4.352 か所の投票所が移転',
     "O TSE mudou o endereço de ___ seções. (A. 4.352 · B. 982)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "A", '最後の討論は金曜23日',
     "O último debate é na ___, 23 de outubro. (A. sexta-feira · B. terça-feira)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "B", 'ヴァスコは敗退した',
     "Na Sul-Americana, o Vasco está ___. (A. na final · B. eliminado)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "A", 'ギター検索は2021年以来53%増',
     "Desde 2021, as buscas por guitarra já subiram ___. (A. 53% · B. 74%)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "B", 'Enem の試験は11月',
     "As provas do Enem são em ___. (A. outubro · B. novembro)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "A", '得票の多い者が勝つ：votos válidos',
     "No segundo turno, vence quem tiver mais ___ válidos. (A. votos · B. debates)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "B", 'ブラジルに夏時間はなく、時計は動かない',
     "No Brasil, o relógio de domingo ___. (A. volta uma hora · B. não muda)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", '選択問題', "B", '投票は8–17時、ブラジリア時間',
     "A votação de domingo é... A. das 6h às 15h · B. das 8h às 17h, hora de Brasília · C. das 8h às 20h", size=14.5, gap=0)
f.ex("A2", '選択問題', "B", '982 か所はサンパウロ州',
     "As 982 seções com endereço novo ficam em... A. Minas Gerais · B. São Paulo · C. Bahia", size=14.5, gap=0)
f.ex("A2", '選択問題', "A", '討論の司会は César Tralli',
     "O mediador do debate da Globo é... A. César Tralli · B. Anderson Daronco · C. Davi Lacerda", size=14.5, gap=0)
f.ex("B1", '選択問題', "C", 'Davi Lacerda が Grêmio × Atlético-MG の審判',
     "Davi Lacerda apita... A. Palmeiras × Vasco · B. Vasco × Boca · C. Grêmio × Atlético-MG", size=14.5, gap=0)
f.ex("B1", '選択問題', "B", 'Prova do Fazendeiro は水曜日',
     "A Prova do Fazendeiro é na... A. sexta-feira · B. quarta-feira · C. segunda-feira", size=14.5, gap=0)
f.ex("B1", '選択問題', "A", '確認カードは Enem の書類',
     "O Cartão de Confirmação é um documento... A. do Enem · B. da eleição · C. da Copa do Brasil", size=14.5, gap=0)
f.ex("B2", '選択問題', "B", '+900% は検索の関心のデータ',
     "O número +900% mede... A. intenção de voto · B. interesse de busca · C. votos válidos", size=14.5, gap=0)
f.ex("B1", '選択問題', "B", 'Finados は11月2日',
     "Finados, feriado nacional, é no dia... A. 31 de outubro · B. 2 de novembro · C. 15 de novembro", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No primeiro turno, ela votou numa escola perto de casa. Nesta semana, abriu o e-Título e viu uma surpresa: a seção dela é uma das 982 que mudaram de endereço em São Paulo. Domingo, ela acorda cedo, leva o documento com foto e vota na escola nova.", 15.5, lh=1.3, split=False)
f.ex("A2", '選択問題', "B", 'Marina はサンパウロ在住',
     "Onde mora Marina? A. no Rio de Janeiro · B. em São Paulo · C. na Bahia", size=14.5, gap=0)
f.ex("A2", '選択問題', "A", '彼女の投票所は住所が変わった',
     "O que mudou para Marina? A. o endereço da seção dela · B. o horário da votação · C. o nome da escola", size=14.5, gap=0)
f.ex("A2", '選択問題', "B", '彼女は e-Título で変化を見た',
     "Marina viu a mudança... A. na televisão · B. no aplicativo e-Título · C. no jornal de papel", size=14.5, gap=0)
f.ex("A2", '選択問題', "A", 'タイトルは全体を要約するもの',
     "O melhor título é... A. «A seção nova de Marina» · B. «O debate final» · C. «A volta da guitarra»", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", '文を作る', "Domingo é dia de decisão.", '時の語が前に来る',
     "domingo / é / dia de decisão → ___", instr='文を作る', size=14.5, gap=0)
f.ex("B1", '文を作る', "O eleitor confere o local no aplicativo.", '主語 + 動詞 + 目的語 + 場所',
     "o eleitor / confere / o local / no aplicativo → ___", instr='文を作る', size=14.5, gap=0)
f.ex("B1", '文を作る', "Que horas começa a votação?", '疑問詞句が文頭に来る',
     "que horas / começa / a votação / ? → ___", instr='文を作る', size=14.5, gap=0)
f.ex("B1", '文を作る', "O Vasco perdeu por 3 a 1.", '主語 + 動詞 + スコア',
     "o Vasco / perdeu / por 3 a 1 → ___", instr='文を作る', size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", '翻訳', '日曜日、ブラジルは再び投票に行く。', '1ページの見出しと対照',
     "Domingo, o Brasil volta às urnas. → ___", instr='翻訳', size=14.5, gap=0)
f.ex("B1", '翻訳', '家を出る前に、投票場所を確認しなさい。', 'Confira = 確認しなさい',
     "Confira o seu local antes de sair de casa. → ___", instr='翻訳', size=14.5, gap=0)
f.ex("B1", '翻訳', "As buscas por guitarra cresceram 53%.", 'cresceram = 増えた',
     '「ギター」の検索量は53%増えた。→ ___', instr='翻訳', size=14.5, gap=0)
f.ex("B2", '翻訳', "Quando você chegar, confira a seção.", '接続法未来 chegar + 命令形 confira',
     '着いたら、投票所を確認してください。→ ___', instr='翻訳', size=14.5, gap=0)
f.head("F　AS PALAVRAS DA ELEIÇÃO", 22, OLIVE, 5)
f.match_set("B2", '語と意味を結ぶ',
            ["o segundo turno", "a seção eleitoral", "justificar", "a maioria absoluta"],
            ["explicar por que você não votou",
             "a disputa final entre os dois mais votados",
             "mais da metade dos votos válidos",
             "o lugar exato onde você vota"],
            ["b", "d", "a", "c"],
            ['segundo turno=二人の決選 b', 'seção=投票の正確な場所 d', 'justificar=投票しなかった理由を説明する a', 'maioria absoluta=有効票の過半数 c'],
            instr='語と意味を結ぶ')
f.head("G　DIÁLOGO NO DIA DA VOTAÇÃO", 22, OLIVE, 5)
f.ex("B1", '穴埋め選択', "B", 'documento com foto 写真付き身分証',
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "A", 'seção は具体的な投票場所（部屋）',
     "— A sua ___ é a 042, na sala 3. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "B", '電子投票機で digita（数字を入力する）',
     "— Agora você ___ o número do candidato. (A. escreve · B. digita)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "A", '緑のキー = confirma（確認）',
     "— Para terminar, você ___ o voto na tecla verde. (A. confirma · B. apaga)", size=14.5, gap=0)
f.ex("B1", '穴埋め選択', "B", 'obrigado = ありがとう',
     "— Pronto, você já votou. — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 25 de outubro, acordo cedo e abro o aplicativo e-Título no celular. "
          "Confiro a minha seção: ela mudou de endereço, e a escola nova fica a dez minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e saio às nove. "
          "Na seção, a fila anda rápido: apresento o documento, digito o número do candidato e confirmo o voto. "
          "Depois, almoço com os amigos e assisto aos resultados à noite. "
          "Para mim, o domingo de eleição é um dia de dever — e de festa da democracia.")
NWORDS = len(MODELO.split())
f.expl(f"作文の問題（唯一の答えはない）；模範文（{NWORDS} 語）を次に示す。")
f.ex("B1", '作文', '（自由作文、模範文は次のとおり）', f"模範文はこの版の H 欄（{NWORDS} 語）",
     "«O seu domingo 25 de outubro» Escreva 80–100 palavras: onde você vota, o que confere antes de sair, e o seu domingo de decisão.", instr='作文', size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　全解答と解説（1–8ページ）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "各問に日本語の一言解説　✓印は模範文のある問題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— {pg}ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == '作文':
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
