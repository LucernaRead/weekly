# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　練習與答案", "A Lucerna", "第8版　A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "完形單選", "A", "第 2 天在 11 月 15 日",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "13 點關門",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "18:30 結束",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "共和國宣言日在 11 月 15 日",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "瓦斯科 × 帕爾梅拉斯次回合在 8 日",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "第二天共 90 道題",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "考試時長 5 小時",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "第 1 天在 11 月 8 日",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "單選", "B", "假日落在週日，週一不補休",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "單選", "B", "確認卡是高考的文件",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "單選", "B", "米內羅競技 × 格雷米奧次回合在 MRV 競技場",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "單選", "B", "第 35 輪本週只有一場，在 14 日",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "單選", "B", "共和國宣言在 1889 年",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "單選", "B", "11.11 是促銷日",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "單選", "A", "300 是考試的分鐘數",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "單選", "A", "德奧多羅是第一任總統",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "單選", "B", "瑪麗娜住在聖保羅",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "單選", "B", "她每天複習一點自然科學",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "單選", "B", "前一晚她備好證件和黑筆、早睡",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "單選", "B", "她 11:30 到達考場",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "Domingo é dia de prova.", "時間詞在前",
     "domingo / é / dia de prova → ___", instr="造句", size=14.5, gap=0)
f.ex("B1", "造句", "A candidata confere o cartão no aplicativo.", "主語 + 動詞 + 賓語 + 地點",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="造句", size=14.5, gap=0)
f.ex("B1", "造句", "Que horas termina a prova?", "疑問詞組在句首",
     "que horas / termina / a prova / ? → ___", instr="造句", size=14.5, gap=0)
f.ex("B1", "造句", "O Brasil comemora a Proclamação da República.", "主語 + 動詞 + 賓語",
     "o Brasil / comemora / a proclamação / da república → ___", instr="造句", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "翻譯", "11 月 15 日週日是高考的第二天。", "對照第 6 版標題",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="翻譯", size=14.5, gap=0)
f.ex("B1", "翻譯", "週日前核對確認卡。", "Confira = 請核對",
     "Confira o cartão antes do domingo. → ___", instr="翻譯", size=14.5, gap=0)
f.ex("B1", "翻譯", "O feriado cai num domingo.", "feriado = 假日",
     "“假日落在週日。” → ___", instr="翻譯", size=14.5, gap=0)
f.ex("B2", "翻譯", "Quando você chegar, apresente o documento com foto.", "虛擬式將來 chegar + 祈使 apresente",
     "你到達時，請出示帶照片的證件。 → ___", instr="翻譯", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "詞彙配對",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação=宣佈一個變化 b", "portão=考場入口 d", "república=1889 年後的國家形式 a", "segunda chamada=關門後的再入場（高考沒有） c"],
            instr="把詞和釋義配對")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "完形單選", "B", "documento com foto 帶照片的證件",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "考場分區（房間）",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "大門 13 點關閉",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "考試 18:30 結束",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "obrigado = 謝謝",
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
f.bridge(f"寫作題（無唯一答案）；範文（{NWORDS} 詞）見下。")
f.ex("B1", "寫作", "（開放題，範文如下）", f"範文見本版 H 區（{NWORDS} 詞）",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="寫作", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　參考答案 — 按版面分頁排列，找到題號即可", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每題附一句中文簡析　帶 ✓ 的為範文題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "寫作":
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
