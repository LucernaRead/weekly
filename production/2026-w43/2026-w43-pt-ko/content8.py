# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-pt-ko/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band('AVALIAÇÃO E RESPOSTAS · 평가와 정답', "A Lucerna", '제8면 · A grande prova da semana + todas as respostas')

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", '빈칸 객관식', "B", 'voltar às urnas = 투표하러 가다',
     "No domingo, o Brasil volta ___ para o segundo turno. (A. às escolas · B. às urnas)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "A", '투표소 4.352곳이 주소를 바꿨어요',
     "O TSE mudou o endereço de ___ seções. (A. 4.352 · B. 982)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "A", '마지막 토론은 금요일 23일이에요',
     "O último debate é na ___, 23 de outubro. (A. sexta-feira · B. terça-feira)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "B", '바스쿠가 탈락했어요',
     "Na Sul-Americana, o Vasco está ___. (A. na final · B. eliminado)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "A", '기타 검색이 2021년부터 53% 늘었어요',
     "Desde 2021, as buscas por guitarra já subiram ___. (A. 53% · B. 74%)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "B", 'Enem 시험은 11월이에요',
     "As provas do Enem são em ___. (A. outubro · B. novembro)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "A", '표를 더 얻은 사람이 이겨요: votos válidos',
     "No segundo turno, vence quem tiver mais ___ válidos. (A. votos · B. debates)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "B", '브라질에는 서머타임이 없어 시계가 안 바뀌어요',
     "No Brasil, o relógio de domingo ___. (A. volta uma hora · B. não muda)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", '객관식', "B", '투표 8h–17h, 브라질리아 시간',
     "A votação de domingo é... A. das 6h às 15h · B. das 8h às 17h, hora de Brasília · C. das 8h às 20h", size=14.5, gap=0)
f.ex("A2", '객관식', "B", '982곳은 상파울루주에 있어요',
     "As 982 seções com endereço novo ficam em... A. Minas Gerais · B. São Paulo · C. Bahia", size=14.5, gap=0)
f.ex("A2", '객관식', "A", '토론 진행자는 César Tralli예요',
     "O mediador do debate da Globo é... A. César Tralli · B. Anderson Daronco · C. Davi Lacerda", size=14.5, gap=0)
f.ex("B1", '객관식', "C", 'Davi Lacerda가 Grêmio × Atlético-MG를 맡아요',
     "Davi Lacerda apita... A. Palmeiras × Vasco · B. Vasco × Boca · C. Grêmio × Atlético-MG", size=14.5, gap=0)
f.ex("B1", '객관식', "B", 'Prova do Fazendeiro는 수요일이에요',
     "A Prova do Fazendeiro é na... A. sexta-feira · B. quarta-feira · C. segunda-feira", size=14.5, gap=0)
f.ex("B1", '객관식', "A", '확인 카드는 Enem 문서예요',
     "O Cartão de Confirmação é um documento... A. do Enem · B. da eleição · C. da Copa do Brasil", size=14.5, gap=0)
f.ex("B2", '객관식', "B", '+900%는 검색 관심도 자료예요',
     "O número +900% mede... A. intenção de voto · B. interesse de busca · C. votos válidos", size=14.5, gap=0)
f.ex("B1", '객관식', "B", 'Finados는 11월 2일이에요',
     "Finados, feriado nacional, é no dia... A. 31 de outubro · B. 2 de novembro · C. 15 de novembro", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No primeiro turno, ela votou numa escola perto de casa. Nesta semana, abriu o e-Título e viu uma surpresa: a seção dela é uma das 982 que mudaram de endereço em São Paulo. Domingo, ela acorda cedo, leva o documento com foto e vota na escola nova.", 15.5, lh=1.3, split=False)
f.ex("A2", '객관식', "B", 'Marina는 상파울루에 살아요',
     "Onde mora Marina? A. no Rio de Janeiro · B. em São Paulo · C. na Bahia", size=14.5, gap=0)
f.ex("A2", '객관식', "A", '그녀의 투표소가 주소를 바꿨어요',
     "O que mudou para Marina? A. o endereço da seção dela · B. o horário da votação · C. o nome da escola", size=14.5, gap=0)
f.ex("A2", '객관식', "B", '그녀는 e-Título에서 변화를 봤어요',
     "Marina viu a mudança... A. na televisão · B. no aplicativo e-Título · C. no jornal de papel", size=14.5, gap=0)
f.ex("A2", '객관식', "A", '제목은 글 전체를 요약해야 해요',
     "O melhor título é... A. «A seção nova de Marina» · B. «O debate final» · C. «A volta da guitarra»", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", '문장 만들기', "Domingo é dia de decisão.", '시간 말이 앞에 와요',
     "domingo / é / dia de decisão → ___", instr='문장 만들기', size=14.5, gap=0)
f.ex("B1", '문장 만들기', "O eleitor confere o local no aplicativo.", 'S + V + O + 장소',
     "o eleitor / confere / o local / no aplicativo → ___", instr='문장 만들기', size=14.5, gap=0)
f.ex("B1", '문장 만들기', "Que horas começa a votação?", '의문사구가 문장 처음에 와요',
     "que horas / começa / a votação / ? → ___", instr='문장 만들기', size=14.5, gap=0)
f.ex("B1", '문장 만들기', "O Vasco perdeu por 3 a 1.", '주어 + 동사 + 스코어',
     "o Vasco / perdeu / por 3 a 1 → ___", instr='문장 만들기', size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", '번역', '일요일, 브라질이 다시 투표소로 가요.', '1면 제목과 대조해 보세요',
     "Domingo, o Brasil volta às urnas. → ___", instr='번역', size=14.5, gap=0)
f.ex("B1", '번역', '집에서 나가기 전에 투표 장소를 확인하세요.', 'Confira = 확인해요',
     "Confira o seu local antes de sair de casa. → ___", instr='번역', size=14.5, gap=0)
f.ex("B1", '번역', "As buscas por guitarra cresceram 53%.", 'cresceram = 늘었다는 뜻이에요',
     '"기타" 검색량이 53% 늘었어요. → ___', instr='번역', size=14.5, gap=0)
f.ex("B2", '번역', "Quando você chegar, confira a seção.", '미래 가정법 chegar + 명령형 confira',
     '도착하면 투표소를 확인하세요. → ___', instr='번역', size=14.5, gap=0)
f.head("F · AS PALAVRAS DA ELEIÇÃO", 22, OLIVE, 5)
f.match_set("B2", '단어 짝짓기',
            ["o segundo turno", "a seção eleitoral", "justificar", "a maioria absoluta"],
            ["explicar por que você não votou",
             "a disputa final entre os dois mais votados",
             "mais da metade dos votos válidos",
             "o lugar exato onde você vota"],
            ["b", "d", "a", "c"],
            ['segundo turno=두 사람의 결선 b', 'seção=실제로 투표하는 장소 d', 'justificar=투표하지 못한 이유 설명 a', 'maioria absoluta=유효표 과반 c'],
            instr='단어와 뜻 짝짓기')
f.head("G · DIÁLOGO NO DIA DA VOTAÇÃO", 22, OLIVE, 5)
f.ex("B1", '빈칸 객관식', "B", 'documento com foto 사진이 있는 신분증',
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "A", 'seção은 구체적인 투표 장소(방)예요',
     "— A sua ___ é a 042, na sala 3. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "B", '전자 투표기에서 digita (숫자 입력)',
     "— Agora você ___ o número do candidato. (A. escreve · B. digita)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "A", '초록 버튼 = confirma (확인)',
     "— Para terminar, você ___ o voto na tecla verde. (A. confirma · B. apaga)", size=14.5, gap=0)
f.ex("B1", '빈칸 객관식', "B", 'obrigado = 고마워요',
     "— Pronto, você já votou. — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 25 de outubro, acordo cedo e abro o aplicativo e-Título no celular. "
          "Confiro a minha seção: ela mudou de endereço, e a escola nova fica a dez minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e saio às nove. "
          "Na seção, a fila anda rápido: apresento o documento, digito o número do candidato e confirmo o voto. "
          "Depois, almoço com os amigos e assisto aos resultados à noite. "
          "Para mim, o domingo de eleição é um dia de dever — e de festa da democracia.")
NWORDS = len(MODELO.split())
f.expl(f"쓰기 문제예요 (하나의 정답은 없어요); 모범 답안은 아래에 있어요 ({NWORDS} 단어).")
f.ex("B1", '쓰기', '(열린 문제 — 모범 답안은 아래에 있어요)', f"모범 답안은 이 면 H 칸에 있어요 ({NWORDS} 단어)",
     "«O seu domingo 25 de outubro» Escreva 80–100 palavras: onde você vota, o que confere antes de sair, e o seu domingo de decisão.", instr='쓰기', size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, 'RESPOSTAS · 정답 — 면별로 정리했어요', 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, '문제마다 한국어 해설 한 줄 · ✓는 모범 답안이 있는 문제예요', 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— 제 {pg} 면 —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == '쓰기':
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
