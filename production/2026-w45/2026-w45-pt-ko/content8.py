# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS　평가와 정답", "A Lucerna", "제8면　A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "빈칸 객관식", "A", "첫날은 11월 8일이에요",
     "No domingo 8, o Brasil faz ___ do Enem. (A. o primeiro dia · B. o segundo dia)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "B", "13시에 문이 닫혀요",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "A", "13:30에 시작해요",
     "A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "A", "위령절은 11월 2일이에요",
     "Finados é no dia ___ de novembro. (A. 2 · B. 15)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "B", "바스쿠 × 파우메이라스 2차전은 8일에 있어요",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "B", "연휴는 모두 3일이에요",
     "O feriadão tem ___ dias. (A. dois · B. três)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "A", "시험 시간은 5시간 반이에요",
     "No dia 8, a prova dura ___ . (A. cinco horas e meia · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "B", "둘째 날은 11월 15일이에요",
     "O segundo dia do Enem é no dia ___ . (A. 8 · B. 15)", size=14.5, gap=0)
f.head("B　PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "객관식", "B", "연휴는 10월 31일부터 11월 2일까지예요",
     "O feriadão vai... A. de 8 a 15 · B. de 31 de outubro a 2 de novembro · C. de 2 a 5", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "확인 카드는 엔엠 서류예요",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "객관식", "B", "아틀레치쿠 미네이루 × 그레미우 2차전은 MRV에서 있어요",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "객관식", "B", "34라운드는 월요일부터 금요일까지 경기가 있어요",
     "A rodada 34 do Brasileirão... A. é só no fim de semana · B. vai de segunda a sexta · C. já terminou", size=14.5, gap=0)
f.ex("B1", "객관식", "B", "위령절에 가족들은 꽃을 가져가요",
     "Em Finados, as famílias levam... A. fogos · B. flores · C. presentes", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "핼러윈은 10월 31일 토요일이었어요",
     "Halloween foi... A. no domingo 8 · B. no sábado, 31 de outubro · C. na segunda 2", size=14.5, gap=0)
f.ex("B2", "객관식", "A", "330은 시험 분 수예요",
     "O número 330 mede... A. os minutos da prova · B. os dias do feriadão · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "객관식", "A", "위령절은 모든 충실한 영혼의 날이라고도 불러요",
     "Finados, em português, também se chama... A. Dia dos Fiéis Defuntos · B. Dia da Independência · C. Dia do Trabalho", size=14.5, gap=0)
f.head("C　LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Lucas mora em Belo Horizonte. No domingo 8, ele faz o Enem pela primeira vez. Na segunda, 2, ele descansa no feriadão e revisa um pouco por dia. Na véspera, ele separa o documento e a caneta preta e dorme cedo. No domingo, ele chega ao local às 11h, duas horas antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "객관식", "B", "루카스는 벨루오리존치에 살아요",
     "Onde mora Lucas? A. no Rio · B. em Belo Horizonte · C. em São Paulo", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "연휴 동안 그는 쉬고 매일 조금씩 복습해요",
     "O que Lucas faz no feriadão? A. só festa · B. descansa e revisa um pouco por dia · C. viaja para a praia", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "전날 밤 그는 신분증과 검은 펜을 챙기고 일찍 자요",
     "Na véspera, Lucas... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "객관식", "B", "그는 11시에 시험장에 도착해요",
     "Lucas chega ao local... A. às 13h30 · B. às 11h · C. às 19h", size=14.5, gap=0)
f.head("D　CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "문장 만들기", "Domingo é dia de prova.", "시간 단어가 앞에 와요",
     "domingo / é / dia de prova → ___", instr="문장 만들기", size=14.5, gap=0)
f.ex("B1", "문장 만들기", "O candidato confere o cartão no aplicativo.", "주어 + 동사 + 목적어 + 장소",
     "o candidato / confere / o cartão / no aplicativo → ___", instr="문장 만들기", size=14.5, gap=0)
f.ex("B1", "문장 만들기", "Que horas começa a prova?", "의문사구가 문장 앞에 와요",
     "que horas / começa / a prova / ? → ___", instr="문장 만들기", size=14.5, gap=0)
f.ex("B1", "문장 만들기", "O Brasil lembra os seus mortos.", "주어 + 동사 + 목적어",
     "o Brasil / lembra / os seus mortos → ___", instr="문장 만들기", size=14.5, gap=0)
f.head("E　TRADUZA", 22, OLIVE, 5)
f.ex("A2", "번역", "11월 8일 일요일은 엔엠 첫날이에요.", "6면 제목을 보세요",
     "Domingo, 8 de novembro, é o primeiro dia do Enem. → ___", instr="번역", size=14.5, gap=0)
f.ex("B1", "번역", "일요일 전에 확인 카드를 확인하세요.", "Confira = 확인하세요",
     "Confira o cartão antes do domingo. → ___", instr="번역", size=14.5, gap=0)
f.ex("B1", "번역", "O feriadão é de 31 de outubro a 2 de novembro.", "feriadão = 연휴예요",
     "“연휴는 10월 31일부터 11월 2일까지예요.” → ___", instr="번역", size=14.5, gap=0)
f.ex("B2", "번역", "Quando você chegar, apresente o documento com foto.", "접속법 미래 chegar + 명령형 apresente",
     "도착하면 사진이 있는 신분증을 보여 주세요. → ___", instr="번역", size=14.5, gap=0)
f.head("F　AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "단어 짝짓기",
            ["o feriadão", "o portão", "a reta final", "a segunda chamada"],
            ["a última semana antes da prova",
             "um feriado grudado no fim de semana",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["feriadão=주말과 이어진 연휴 b", "portão=시험장 입구 d", "reta final=시험 전 마지막 한 주 a", "segunda chamada=문이 닫힌 뒤의 재입장 (엔엠에는 없어요) c"],
            instr="단어와 뜻 짝짓기")
f.head("G　DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "빈칸 객관식", "B", "documento com foto 사진이 있는 신분증",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "A", "seção = 시험장 구역 (교실)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "B", "문은 13시에 닫혀요",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "A", "시험은 13:30에 시작해요",
     "— A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "빈칸 객관식", "B", "obrigado = 고마워요",
     "— Boa prova! — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H　ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 8 de novembro, acordo cedo e abro o Cartão de Confirmação no celular. "
          "Confiro o meu local: a escola fica a vinte minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e a caneta preta e saio às onze. "
          "Chego antes do meio-dia, entro com calma e guardo o celular desligado. "
          "A prova começa às 13h30: primeiro a redação, depois Linguagens e Humanas. "
          "Escrevo com calma e reviso no fim. "
          "Às 19h, saio cansado e feliz: o primeiro dia acabou, e o segundo vem no domingo 15.")
NWORDS = len(MODELO.split())
f.bridge(f"쓰기 문제예요 (하나의 정답은 없어요); 모범 답안은 아래에 있어요 ({NWORDS} 단어).")
f.ex("B1", "쓰기", "(열린 문제 — 모범 답안은 아래에 있어요)", f"모범 답안은 이 면 H 칸에 있어요 ({NWORDS} 단어)",
     "«O seu domingo 8 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="쓰기", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "RESPOSTAS　정답 — 면마다 나눠 실었어요, 번호로 찾으세요", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "각 답마다 짧은 해설이 있어요　✓는 모범 답안 문제예요", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제 {pg} 면 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "쓰기":
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
