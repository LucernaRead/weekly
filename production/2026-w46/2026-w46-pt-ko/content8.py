# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-pt-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · 평가와 정답", "A Lucerna", "8면 · 이번 주의 큰 시험 + 모든 정답")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "A", "둘째 날은 11월 15일",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "B", "13시 폐문",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "A", "18:30 종료",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "A", "공화국 선포의 날은 11월 15일",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "B", "바스쿠 × 파우메이라스 2차전은 8일",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "B", "둘째 날은 모두 90문제",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "A", "시험 시간은 5시간",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "B", "첫째 날은 11월 8일",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "객관식", "B", "공휴일이 일요일에 겹쳐도 월요일에 쉬지 않아요",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "확인 카드는 Enem 서류예요",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "객관식", "B", "아틀레치쿠 MG × 그레미우 2차전은 MRV 아레나",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "객관식", "B", "35라운드는 이번 주 한 경기뿐, 14일",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "객관식", "B", "공화국 선포는 1889년",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "11.11은 세일의 날",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "객관식", "A", "300은 시험의 분 단위 시간",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "객관식", "A", "데오도루는 초대 대통령",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "마리나는 상파울루에 살아요",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "그녀는 매일 조금씩 자연과학을 복습해요",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "전날 밤, 신분증과 검은 펜을 준비하고 일찍 자요",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "그녀는 11:30에 시험장에 도착해요",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "Domingo é dia de prova.", "시간 말이 앞에 와요",
     "domingo / é / dia de prova → ___", instr="문장 만들기", size=14.5, gap=0)
f.ex("B1", "문장 만들기", "A candidata confere o cartão no aplicativo.", "주어 + 동사 + 목적어 + 장소",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="문장 만들기", size=14.5, gap=0)
f.ex("B1", "문장 만들기", "Que horas termina a prova?", "의문 어구가 문장 맨 앞에 와요",
     "que horas / termina / a prova / ? → ___", instr="문장 만들기", size=14.5, gap=0)
f.ex("B1", "문장 만들기", "O Brasil comemora a Proclamação da República.", "주어 + 동사 + 목적어",
     "o Brasil / comemora / a proclamação / da república → ___", instr="문장 만들기", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "번역", "11월 15일 일요일은 Enem 둘째 날이에요.", "6면 제목과 대조하세요",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="번역하기", size=14.5, gap=0)
f.ex("B1", "번역", "일요일 전에 확인 카드를 확인하세요.", "Confira = 확인하세요",
     "Confira o cartão antes do domingo. → ___", instr="번역하기", size=14.5, gap=0)
f.ex("B1", "번역", "O feriado cai num domingo.", "feriado = 공휴일",
     "“공휴일이 일요일에 겹쳐요.” → ___", instr="번역하기", size=14.5, gap=0)
f.ex("B2", "번역", "Quando você chegar, apresente o documento com foto.", "미래 접속법 chegar + 명령형 apresente",
     "도착하면 사진이 있는 신분증을 보여 주세요. → ___", instr="번역하기", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "어휘 연결하기",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação = 변화를 선포하는 것 (b)", "portão = 시험장 입구 (d)", "república = 1889년 이후의 국가 형태 (a)", "segunda chamada = 폐문 후 재입장(Enem에는 없어요) (c)"],
            instr="단어와 뜻 연결하기")
f.head("G · DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "빈칸 채우기", "B", "documento com foto = 사진이 있는 신분증",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "A", "seção = 시험실(구역)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "B", "정문은 13시에 닫혀요",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "A", "시험은 18:30에 끝나요",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "빈칸 채우기", "B", "obrigado = 고마워요",
     "— Boa prova! — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 15 de novembro, acordo cedo e abro o Cartão de Confirmação no celular. "
          "Confiro o meu local: a escola fica a vinte minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e a caneta preta e saio às onze. "
          "Chego antes do meio-dia, entro com calma e guardo o celular desligado. "
          "A prova começa às 13h30: primeiro Natureza, depois Matemática. "
          "Resolvo com calma e reviso no fim. "
          "Às 18h30, saio cansada e feliz: o Enem acabou, e o feriado continua em casa.")
NWORDS = len(MODELO.split())
f.bridge(f"작문 문제(유일한 정답 없음). 모범 답안({NWORDS}단어)은 아래에 있어요.")
f.ex("B1", "작문", "(열린 문제, 모범 답안은 아래)", f"모범 답안은 이 면 H란({NWORDS}단어)",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="쓰기", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · 정답 — 면별로 배열했어요. 번호를 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "각 문제에 한 줄 해설 · ✓는 작문 문제", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "작문":
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
