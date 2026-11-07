# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · 評価と解答", "A Lucerna", "8 ページ · A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "A", "初日は11月8日",
     "No domingo 8, o Brasil faz ___ do Enem. (A. o primeiro dia · B. o segundo dia)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "B", "13時閉門",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "A", "13:30 試験開始",
     "A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "A", "死者の日は11月2日",
     "Finados é no dia ___ de novembro. (A. 2 · B. 15)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "B", "ヴァスコ × パルメイラス第2戦は8日",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "B", "連休は全部で3日間",
     "O feriadão tem ___ dias. (A. dois · B. três)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "A", "試験時間は5時間半",
     "No dia 8, a prova dura ___ . (A. cinco horas e meia · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "B", "第2日は11月15日",
     "O segundo dia do Enem é no dia ___ . (A. 8 · B. 15)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "選択問題", "B", "連休は10月31日から11月2日まで",
     "O feriadão vai... A. de 8 a 15 · B. de 31 de outubro a 2 de novembro · C. de 2 a 5", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "確認カードはEnemの書類",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "選択問題", "B", "アトレチコMG × グレミオ第2戦はMRVアリーナ",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "選択問題", "B", "第34節は月曜日から金曜日まで試合がある",
     "A rodada 34 do Brasileirão... A. é só no fim de semana · B. vai de segunda a sexta · C. já terminou", size=14.5, gap=0)
f.ex("B1", "選択問題", "B", "死者の日、家族は花を持っていく",
     "Em Finados, as famílias levam... A. fogos · B. flores · C. presentes", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "ハロウィーンは10月31日土曜日",
     "Halloween foi... A. no domingo 8 · B. no sábado, 31 de outubro · C. na segunda 2", size=14.5, gap=0)
f.ex("B2", "選択問題", "A", "330は試験の分数",
     "O número 330 mede... A. os minutos da prova · B. os dias do feriadão · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "選択問題", "A", "死者の日はポルトガル語で諸聖霊魂日ともいう",
     "Finados, em português, também se chama... A. Dia dos Fiéis Defuntos · B. Dia da Independência · C. Dia do Trabalho", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Lucas mora em Belo Horizonte. No domingo 8, ele faz o Enem pela primeira vez. Na segunda, 2, ele descansa no feriadão e revisa um pouco por dia. Na véspera, ele separa o documento e a caneta preta e dorme cedo. No domingo, ele chega ao local às 11h, duas horas antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "選択問題", "B", "ルーカスはベロオリゾンテに住んでいる",
     "Onde mora Lucas? A. no Rio · B. em Belo Horizonte · C. em São Paulo", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "連休中、彼は休み、毎日少しずつ復習する",
     "O que Lucas faz no feriadão? A. só festa · B. descansa e revisa um pouco por dia · C. viaja para a praia", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "前夜、彼は身分証と黒ペンを用意し、早く寝る",
     "Na véspera, Lucas... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "彼は11時に試験会場に着く",
     "Lucas chega ao local... A. às 13h30 · B. às 11h · C. às 19h", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "文を作る", "Domingo é dia de prova.", "時を表す語が前に来る",
     "domingo / é / dia de prova → ___", instr="文を作る", size=14.5, gap=0)
f.ex("B1", "文を作る", "O candidato confere o cartão no aplicativo.", "主語 + 動詞 + 目的語 + 場所",
     "o candidato / confere / o cartão / no aplicativo → ___", instr="文を作る", size=14.5, gap=0)
f.ex("B1", "文を作る", "Que horas começa a prova?", "疑問詞句が文頭に来る",
     "que horas / começa / a prova / ? → ___", instr="文を作る", size=14.5, gap=0)
f.ex("B1", "文を作る", "O Brasil lembra os seus mortos.", "主語 + 動詞 + 目的語",
     "o Brasil / lembra / os seus mortos → ___", instr="文を作る", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "翻訳", "11月8日日曜日はEnemの初日です。", "6ページの見出しと対照",
     "Domingo, 8 de novembro, é o primeiro dia do Enem. → ___", instr="翻訳", size=14.5, gap=0)
f.ex("B1", "翻訳", "日曜日の前に確認カードを確かめよう。", "Confira = 確かめること",
     "Confira o cartão antes do domingo. → ___", instr="翻訳", size=14.5, gap=0)
f.ex("B1", "翻訳", "O feriadão é de 31 de outubro a 2 de novembro.", "feriadão = 連休",
     "「連休は10月31日から11月2日までです。」 → ___", instr="翻訳", size=14.5, gap=0)
f.ex("B2", "翻訳", "Quando você chegar, apresente o documento com foto.", "接続法未来形 chegar + 命令形 apresente",
     "「着いたら、写真付きの身分証を提示してください。」 → ___", instr="翻訳", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "語と意味を結ぶ",
            ["o feriadão", "o portão", "a reta final", "a segunda chamada"],
            ["a última semana antes da prova",
             "um feriado grudado no fim de semana",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["feriadão=週末につながった休み b", "portão=試験会場の入口 d", "reta final=試験前最後の一週間 a", "segunda chamada=閉門後の再入場（Enemにはない） c"],
            instr="語と意味を結ぶ")
f.head("G · DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "穴埋め選択", "B", "documento com foto 写真付きの身分証",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "A", "seção = 試験会場の区画（部屋）",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "B", "門は13時に閉まる",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "A", "試験は13:30に始まる",
     "— A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "穴埋め選択", "B", "obrigado = ありがとう",
     "— Boa prova! — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 8 de novembro, acordo cedo e abro o Cartão de Confirmação no celular. "
          "Confiro o meu local: a escola fica a vinte minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e a caneta preta e saio às onze. "
          "Chego antes do meio-dia, entro com calma e guardo o celular desligado. "
          "A prova começa às 13h30: primeiro a redação, depois Linguagens e Humanas. "
          "Escrevo com calma e reviso no fim. "
          "Às 19h, saio cansado e feliz: o primeiro dia acabou, e o segundo vem no domingo 15.")
NWORDS = len(MODELO.split())
f.bridge(f"作文問題（唯一の答えはない）；模範文（{NWORDS} 語）は下記。")
f.ex("B1", "作文", "（自由問題、模範文は下記）", f"模範文は本ページ H 欄（{NWORDS} 語）",
     "«O seu domingo 8 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="作文", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · 全解答と解説（1–8ページ）", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "各問に日本語の一言解説 · ✓印は模範文のある問題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— {pg} ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
