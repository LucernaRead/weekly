# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w45-pt-zh-tw/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · 練習與答案", "A Lucerna", "第 8 版 · A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "完形單選", "A", "第 1 天在 11 月 8 日",
     "No domingo 8, o Brasil faz ___ do Enem. (A. o primeiro dia · B. o segundo dia)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "13 點關門",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "13:30 開考",
     "A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "亡靈節在 11 月 2 日",
     "Finados é no dia ___ de novembro. (A. 2 · B. 15)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "瓦斯科 × 帕爾梅拉斯次回合在 8 日",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "連休共 3 天",
     "O feriadão tem ___ dias. (A. dois · B. três)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "考試時長 5 個半小時",
     "No dia 8, a prova dura ___ . (A. cinco horas e meia · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "第 2 天在 11 月 15 日",
     "O segundo dia do Enem é no dia ___ . (A. 8 · B. 15)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "單選", "B", "連休從 10 月 31 日到 11 月 2 日",
     "O feriadão vai... A. de 8 a 15 · B. de 31 de outubro a 2 de novembro · C. de 2 a 5", size=14.5, gap=0)
f.ex("A2", "單選", "B", "確認卡是高考的文件",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "單選", "B", "米內羅競技 × 格雷米奧次回合在 MRV 競技場",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "單選", "B", "第 34 輪週一到週五都有比賽",
     "A rodada 34 do Brasileirão... A. é só no fim de semana · B. vai de segunda a sexta · C. já terminou", size=14.5, gap=0)
f.ex("B1", "單選", "B", "亡靈節家人們帶花",
     "Em Finados, as famílias levam... A. fogos · B. flores · C. presentes", size=14.5, gap=0)
f.ex("A2", "單選", "B", "萬聖節在 10 月 31 日週六",
     "Halloween foi... A. no domingo 8 · B. no sábado, 31 de outubro · C. na segunda 2", size=14.5, gap=0)
f.ex("B2", "單選", "A", "330 是考試的分鐘數",
     "O número 330 mede... A. os minutos da prova · B. os dias do feriadão · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "單選", "A", "亡靈節又稱諸聖靈魂日",
     "Finados, em português, também se chama... A. Dia dos Fiéis Defuntos · B. Dia da Independência · C. Dia do Trabalho", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Lucas mora em Belo Horizonte. No domingo 8, ele faz o Enem pela primeira vez. Na segunda, 2, ele descansa no feriadão e revisa um pouco por dia. Na véspera, ele separa o documento e a caneta preta e dorme cedo. No domingo, ele chega ao local às 11h, duas horas antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "單選", "B", "盧卡斯住在貝洛奧里藏特",
     "Onde mora Lucas? A. no Rio · B. em Belo Horizonte · C. em São Paulo", size=14.5, gap=0)
f.ex("A2", "單選", "B", "連休裡他休息並每天複習一點",
     "O que Lucas faz no feriadão? A. só festa · B. descansa e revisa um pouco por dia · C. viaja para a praia", size=14.5, gap=0)
f.ex("A2", "單選", "B", "前一晚他備好證件和黑筆、早睡",
     "Na véspera, Lucas... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "單選", "B", "他 11 點到達考場",
     "Lucas chega ao local... A. às 13h30 · B. às 11h · C. às 19h", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "造句", "Domingo é dia de prova.", "時間詞在前",
     "domingo / é / dia de prova → ___", instr="造句", size=14.5, gap=0)
f.ex("B1", "造句", "O candidato confere o cartão no aplicativo.", "主語 + 動詞 + 賓語 + 地點",
     "o candidato / confere / o cartão / no aplicativo → ___", instr="造句", size=14.5, gap=0)
f.ex("B1", "造句", "Que horas começa a prova?", "疑問詞組在句首",
     "que horas / começa / a prova / ? → ___", instr="造句", size=14.5, gap=0)
f.ex("B1", "造句", "O Brasil lembra os seus mortos.", "主語 + 動詞 + 賓語",
     "o Brasil / lembra / os seus mortos → ___", instr="造句", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "翻譯", "11 月 8 日週日是高考的第一天。", "對照第 6 版標題",
     "Domingo, 8 de novembro, é o primeiro dia do Enem. → ___", instr="翻譯", size=14.5, gap=0)
f.ex("B1", "翻譯", "週日前核對確認卡。", "Confira = 請核對",
     "Confira o cartão antes do domingo. → ___", instr="翻譯", size=14.5, gap=0)
f.ex("B1", "翻譯", "O feriadão é de 31 de outubro a 2 de novembro.", "feriadão = 連休",
     "「連休是 10 月 31 日到 11 月 2 日。」 → ___", instr="翻譯", size=14.5, gap=0)
f.ex("B2", "翻譯", "Quando você chegar, apresente o documento com foto.", "虛擬式將來 chegar + 祈使 apresente",
     "你到達時，請出示帶照片的證件。 → ___", instr="翻譯", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "詞彙配對",
            ["o feriadão", "o portão", "a reta final", "a segunda chamada"],
            ["a última semana antes da prova",
             "um feriado grudado no fim de semana",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["feriadão=連著週末的假期 b", "portão=考場入口 d", "reta final=考前最後一週 a", "segunda chamada=關門後的再入場（高考沒有） c"],
            instr="把詞和釋義配對")
f.head("G · DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "完形單選", "B", "documento com foto 帶照片的證件",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "seção = 考場分區（房間）",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "大門 13 點關閉",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "完形單選", "A", "考試 13:30 開始",
     "— A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "完形單選", "B", "obrigado = 謝謝",
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
f.expl(f"寫作題（無唯一答案）；範本（{NWORDS} 詞）見下。")
f.ex("B1", "寫作", "（開放題，範本如下）", f"範本見本版 H 區（{NWORDS} 詞）",
     "«O seu domingo 8 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="寫作", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · 參考答案 — 按版面分頁排列，找到題號即可", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "每題附一句中文簡析 · 帶 ✓ 的為範本題", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 第 {pg} 版 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
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
