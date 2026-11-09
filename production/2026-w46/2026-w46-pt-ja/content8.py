# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　評価と解答", "A Lucerna", "8ページ　今週の大テスト + すべての解答")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "空所補充", "A", "第 2 日は 11 月 15 日",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "空所補充", "B", "13 時に閉門",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "18:30 終了",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "共和国宣言の日は 11 月 15 日",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "空所補充", "B", "ヴァスコ × パルメイラスの第 2 戦は 8 日",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "空所補充", "B", "第 2 日は全部で 90 問",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "試験時間は 5 時間",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "空所補充", "B", "第 1 日は 11 月 8 日",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "選択問題", "B", "祝日が日曜日に重なり、月曜の振替なし",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "確認カードは Enem の書類",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "選択問題", "B", "アトレチコ MG × グレミオの第 2 戦は MRV アリーナ",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "選択問題", "B", "第 35 節は今週 1 試合だけ、14 日",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "選択問題", "B", "共和国宣言は 1889 年",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "11.11 はセールの日",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "選択問題", "A", "300 は試験の分数",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "選択問題", "A", "デオドロは初代大統領",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "選択問題", "B", "マリーナはサンパウロに住んでいる",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "彼女は毎日少し自然科学を復習する",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "前夜、身分証と黒ペンを用意し、早く寝る",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "選択問題", "B", "彼女は 11:30 に試験会場に着く",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "文を作る", "Domingo é dia de prova.", "時間の言葉が前に来る",
     "domingo / é / dia de prova → ___", instr="文を作る", size=14.5, gap=0)
f.ex("B1", "文を作る", "A candidata confere o cartão no aplicativo.", "主語 + 動詞 + 目的語 + 場所",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="文を作る", size=14.5, gap=0)
f.ex("B1", "文を作る", "Que horas termina a prova?", "疑問の語句が文頭に来る",
     "que horas / termina / a prova / ? → ___", instr="文を作る", size=14.5, gap=0)
f.ex("B1", "文を作る", "O Brasil comemora a Proclamação da República.", "主語 + 動詞 + 目的語",
     "o Brasil / comemora / a proclamação / da república → ___", instr="文を作る", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "翻訳", "11 月 15 日（日）は Enem の第 2 日です。", "6 ページの見出しと対照",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="訳す", size=14.5, gap=0)
f.ex("B1", "翻訳", "日曜日の前に確認カードを確かめよう。", "Confira = 確認しよう",
     "Confira o cartão antes do domingo. → ___", instr="訳す", size=14.5, gap=0)
f.ex("B1", "翻訳", "O feriado cai num domingo.", "feriado = 祝日",
     "「祝日は日曜日に重なる。」→ ___", instr="訳す", size=14.5, gap=0)
f.ex("B2", "翻訳", "Quando você chegar, apresente o documento com foto.", "未来接続法 chegar + 命令形 apresente",
     "着いたら、写真付きの身分証を提示してください。→ ___", instr="訳す", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "語彙のマッチング",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação = 変化を宣言すること (b)", "portão = 試験会場の入口 (d)", "república = 1889 年以後の国家形態 (a)", "segunda chamada = 閉門後の再入場（Enem にはない）(c)"],
            instr="言葉と意味を結ぶ")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "空所補充", "B", "documento com foto = 写真付き身分証",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "seção = 試験室（区画）",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "空所補充", "B", "門は 13 時に閉まる",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "空所補充", "A", "試験は 18:30 に終わる",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "空所補充", "B", "obrigado = ありがとう",
     "— Boa prova! — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 15 de novembro, acordo cedo e abro o Cartão de Confirmação no celular. "
          "Confiro o meu local: a escola fica a vinte minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e a caneta preta e saio às onze. "
          "Chego antes do meio-dia, entro com calma e guardo o celular desligado. "
          "A prova começa às 13h30: primeiro Natureza, depois Matemática. "
          "Resolvo com calma e reviso no fim. "
          "Às 18h30, saio cansada e feliz: o Enem acabou, e o feriado continua em casa.")
NWORDS = len(MODELO.split())
f.bridge(f"作文問題（唯一の答えなし）。模範文（{NWORDS} 語）は下記。")
f.ex("B1", "作文", "（自由問題、模範文は下記）", f"模範文は本ページ H 欄（{NWORDS} 語）",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="書く", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　解答 — ページごとに配列。番号を探そう", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "各問に一言の解説付き　✓ は作文問題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— {pg}ページ —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
