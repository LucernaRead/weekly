# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-pt-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · Упражнения и ответы", "A Lucerna", "Страница 8 · A grande prova da semana + todas as respostas")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Выбор в пропуске", "B", "voltar às urnas = идти голосовать",
     "No domingo, o Brasil volta ___ para o segundo turno. (A. às escolas · B. às urnas)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "4.352 участка сменили адрес",
     "O TSE mudou o endereço de ___ seções. (A. 4.352 · B. 982)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "Последние дебаты — в пятницу, 23-го",
     "O último debate é na ___, 23 de outubro. (A. sexta-feira · B. terça-feira)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "«Васко» выбыл из турнира",
     "Na Sul-Americana, o Vasco está ___. (A. na final · B. eliminado)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "Запросы «гитара» с 2021 года выросли на 53%",
     "Desde 2021, as buscas por guitarra já subiram ___. (A. 53% · B. 74%)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "Экзамены Enem — в ноябре",
     "As provas do Enem são em ___. (A. outubro · B. novembro)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "Побеждает набравший больше голосов: votos válidos",
     "No segundo turno, vence quem tiver mais ___ válidos. (A. votos · B. debates)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "В Бразилии нет летнего времени, часы не переводят",
     "No Brasil, o relógio de domingo ___. (A. volta uma hora · B. não muda)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Выбор ответа", "B", "Голосование 8h–17h, время Бразилиа",
     "A votação de domingo é... A. das 6h às 15h · B. das 8h às 17h, hora de Brasília · C. das 8h às 20h", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "982 — в штате Сан-Паулу",
     "As 982 seções com endereço novo ficam em... A. Minas Gerais · B. São Paulo · C. Bahia", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "A", "Ведущий дебатов — César Tralli",
     "O mediador do debate da Globo é... A. César Tralli · B. Anderson Daronco · C. Davi Lacerda", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "C", "Davi Lacerda судит «Гремио» × «Атлетико-MG»",
     "Davi Lacerda apita... A. Palmeiras × Vasco · B. Vasco × Boca · C. Grêmio × Atlético-MG", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "B", "Prova do Fazendeiro — в среду",
     "A Prova do Fazendeiro é na... A. sexta-feira · B. quarta-feira · C. segunda-feira", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "A", "Карточка подтверждения — документ Enem",
     "O Cartão de Confirmação é um documento... A. do Enem · B. da eleição · C. da Copa do Brasil", size=14.5, gap=0)
f.ex("B2", "Выбор ответа", "B", "+900% — данные поискового интереса",
     "O número +900% mede... A. intenção de voto · B. interesse de busca · C. votos válidos", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "B", "Finados — 2 ноября",
     "Finados, feriado nacional, é no dia... A. 31 de outubro · B. 2 de novembro · C. 15 de novembro", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No primeiro turno, ela votou numa escola perto de casa. Nesta semana, abriu o e-Título e viu uma surpresa: a seção dela é uma das 982 que mudaram de endereço em São Paulo. Domingo, ela acorda cedo, leva o documento com foto e vota na escola nova.", 15.5, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Marina живёт в Сан-Паулу",
     "Onde mora Marina? A. no Rio de Janeiro · B. em São Paulo · C. na Bahia", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "A", "Её участок сменил адрес",
     "O que mudou para Marina? A. o endereço da seção dela · B. o horário da votação · C. o nome da escola", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "Изменение она увидела в e-Título",
     "Marina viu a mudança... A. na televisão · B. no aplicativo e-Título · C. no jornal de papel", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "A", "Заголовок должен охватывать весь текст",
     "O melhor título é... A. «A seção nova de Marina» · B. «O debate final» · C. «A volta da guitarra»", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Составьте предложение", "Domingo é dia de decisão.", "Слово времени — в начале",
     "domingo / é / dia de decisão → ___", instr="Составьте", size=14.5, gap=0)
f.ex("B1", "Составьте предложение", "O eleitor confere o local no aplicativo.", "Подлежащее + глагол + дополнение + место",
     "o eleitor / confere / o local / no aplicativo → ___", instr="Составьте", size=14.5, gap=0)
f.ex("B1", "Составьте предложение", "Que horas começa a votação?", "Вопрос — в начале",
     "que horas / começa / a votação / ? → ___", instr="Составьте", size=14.5, gap=0)
f.ex("B1", "Составьте предложение", "O Vasco perdeu por 3 a 1.", "Подлежащее + глагол + счёт",
     "o Vasco / perdeu / por 3 a 1 → ___", instr="Составьте", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Перевод", "В воскресенье Бразилия — снова к урнам.", "См. заголовок стр. 1",
     "Domingo, o Brasil volta às urnas. → ___", instr="Переведите", size=14.5, gap=0)
f.ex("B1", "Перевод", "Перед выходом проверьте место голосования.", "Confira = проверьте",
     "Confira o seu local antes de sair de casa. → ___", instr="Переведите", size=14.5, gap=0)
f.ex("B1", "Перевод", "As buscas por guitarra cresceram 53%.", "cresceram = выросли",
     "Запросы «гитара» выросли на 53%. → ___", instr="Переведите", size=14.5, gap=0)
f.ex("B2", "Перевод", "Quando você chegar, confira a seção.", "Будущее сослагательное chegar + повелительное confira",
     "Когда вы придёте, проверьте свой участок. → ___", instr="Переведите", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA ELEIÇÃO", 22, OLIVE, 5)
f.match_set("B2", "Сопоставление",
            ["o segundo turno", "a seção eleitoral", "justificar", "a maioria absoluta"],
            ["explicar por que você não votou",
             "a disputa final entre os dois mais votados",
             "mais da metade dos votos válidos",
             "o lugar exato onde você vota"],
            ["b", "d", "a", "c"],
            ["segundo turno = финал двух лидеров b", "seção = точное место голосования d", "justificar = объяснить, почему не голосовали a", "maioria absoluta = больше половины действительных голосов c"],
            instr="Соедините пары")
f.head("G · DIÁLOGO NO DIA DA VOTAÇÃO", 22, OLIVE, 5)
f.ex("B1", "Выбор в пропуске", "B", "documento com foto = документ с фото",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "seção — конкретный участок (комната)",
     "— A sua ___ é a 042, na sala 3. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "В электронной урне — digita (ввод номера)",
     "— Agora você ___ o número do candidato. (A. escreve · B. digita)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "Зелёная клавиша = confirma (подтвердить)",
     "— Para terminar, você ___ o voto na tecla verde. (A. confirma · B. apaga)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "obrigado = спасибо",
     "— Pronto, você já votou. — Muito ___! (A. tarde · B. obrigado)", size=14.5, gap=0)
f.head("H · ESCREVA VOCÊ", 22, OLIVE, 5)
MODELO = ("Domingo, 25 de outubro, acordo cedo e abro o aplicativo e-Título no celular. "
          "Confiro a minha seção: ela mudou de endereço, e a escola nova fica a dez minutos de casa. "
          "Tomo café com a minha família, pego o documento com foto e saio às nove. "
          "Na seção, a fila anda rápido: apresento o documento, digito o número do candidato e confirmo o voto. "
          "Depois, almoço com os amigos e assisto aos resultados à noite. "
          "Para mim, o domingo de eleição é um dia de dever — e de festa da democracia.")
NWORDS = len(MODELO.split())
WFORM = ('слово' if NWORDS % 10 == 1 and NWORDS % 100 != 11 else
         'слова' if NWORDS % 10 in (2, 3, 4) and not 12 <= NWORDS % 100 <= 14 else 'слов')
f.expl(f"Письменное задание (единственного ответа нет); образец ({NWORDS} {WFORM}) — ниже.")
f.ex("B1", "Письмо", "(открытый вопрос — образец ниже)", f"Образец — в разделе H этой страницы ({NWORDS} {WFORM})",
     "«O seu domingo 25 de outubro» Escreva 80–100 palavras: onde você vota, o que confere antes de sair, e o seu domingo de decisão.", instr="Напишите", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · Ответы — по страницам: ищите по номеру задания", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "К каждому ответу — короткое пояснение · ✓ — задание с образцом", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Письмо":
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
