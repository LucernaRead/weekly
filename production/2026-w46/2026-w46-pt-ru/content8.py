# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-pt-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · ТЕСТ И ОТВЕТЫ", "A Lucerna", "СТРАНИЦА 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Текст с пропусками", "A", "День 2 — 15 ноября",
     "No domingo 15, o Brasil faz ___ do Enem. (A. o segundo dia · B. o primeiro dia)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "B", "Закрытие в 13:00",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "A", "Конец в 18:30",
     "A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "A", "День Провозглашения Республики — 15 ноября",
     "A Proclamação da República é no dia ___ de novembro. (A. 15 · B. 20)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "B", "Ответный матч Васко × Палмейрас — 8-го",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "B", "Во второй день всего 90 вопросов",
     "O dia 15 tem ___ questões. (A. 45 · B. 90)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "A", "Экзамен длится 5 часов",
     "No dia 15, a prova dura ___ . (A. cinco horas · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "B", "День 1 — 8 ноября",
     "O primeiro dia do Enem foi no dia ___ . (A. 15 · B. 8)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Выбор ответа", "B", "Праздник выпадает на воскресенье, в понедельник выходного нет",
     "O feriado de 15 de novembro... A. dá folga na segunda · B. cai num domingo · C. muda o relógio", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "Карта подтверждения относится к Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "B", "Ответный матч Атлетико-МГ × Гремио — на Арене MRV",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "B", "В 35-м туре на этой неделе только один матч, 14-го",
     "A rodada 35 do Brasileirão, nesta semana... A. tem dez jogos · B. só tem Mirassol × Atlético-MG · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "B", "Провозглашение Республики было в 1889 году",
     "A Proclamação da República foi em... A. 1822 · B. 1889 · C. 1949", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "11.11 — день распродаж",
     "O 11.11 é... A. um feriado nacional · B. o dia das promoções · C. o dia do Enem", size=14.5, gap=0)
f.ex("B2", "Выбор ответа", "A", "300 — длительность экзамена в минутах",
     "O número 300 mede... A. os minutos da prova · B. os dias do feriado · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "A", "Деодору был первым президентом",
     "Deodoro da Fonseca foi... A. o primeiro presidente · B. o último imperador · C. um jogador", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Marina mora em São Paulo. No domingo 15, ela faz o segundo dia do Enem. Na segunda, 9, ela revisa Natureza um pouco por dia. Na véspera, ela separa o documento e a caneta preta e dorme cedo. No domingo, ela chega ao local às 11h30, uma hora e meia antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Марина живёт в Сан-Паулу",
     "Onde mora Marina? A. no Rio · B. em São Paulo · C. em Belo Horizonte", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "Она повторяет понемногу естественные науки каждый день",
     "O que Marina revisa na semana? A. só Matemática · B. Natureza, um pouco por dia · C. nada", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "Накануне она готовит документ и чёрную ручку и ложится рано",
     "Na véspera, Marina... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "Она приходит в экзаменационный центр в 11:30",
     "Marina chega ao local... A. às 13h30 · B. às 11h30 · C. às 18h30", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Составление предложений", "Domingo é dia de prova.", "Слово времени — впереди",
     "domingo / é / dia de prova → ___", instr="Составьте предложение", size=14.5, gap=0)
f.ex("B1", "Составление предложений", "A candidata confere o cartão no aplicativo.", "Подлежащее + глагол + дополнение + место",
     "a candidata / confere / o cartão / no aplicativo → ___", instr="Составьте предложение", size=14.5, gap=0)
f.ex("B1", "Составление предложений", "Que horas termina a prova?", "Вопросительная группа — в начале",
     "que horas / termina / a prova / ? → ___", instr="Составьте предложение", size=14.5, gap=0)
f.ex("B1", "Составление предложений", "O Brasil comemora a Proclamação da República.", "Подлежащее + глагол + дополнение",
     "o Brasil / comemora / a proclamação / da república → ___", instr="Составьте предложение", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Перевод", "Воскресенье 15 ноября — второй день Enem.", "Смотри заголовок на странице 6",
     "Domingo, 15 de novembro, é o segundo dia do Enem. → ___", instr="Переведите", size=14.5, gap=0)
f.ex("B1", "Перевод", "Проверь карту до воскресенья.", "Confira = проверь",
     "Confira o cartão antes do domingo. → ___", instr="Переведите", size=14.5, gap=0)
f.ex("B1", "Перевод", "O feriado cai num domingo.", "feriado = праздник",
     "«Праздник выпадает на воскресенье.» → ___", instr="Переведите", size=14.5, gap=0)
f.ex("B2", "Перевод", "Quando você chegar, apresente o documento com foto.", "Будущее сослагательного наклонения chegar + повелительное наклонение apresente",
     "Когда придёшь, покажи документ с фото. → ___", instr="Переведите", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Соедините слова",
            ["a proclamação", "o portão", "a república", "a segunda chamada"],
            ["a forma do Estado depois de 1889",
             "o ato de anunciar uma mudança",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["proclamação = объявить изменение (b)", "portão = вход в экзаменационный центр (d)", "república = форма государства после 1889 года (a)", "segunda chamada = повторный вход после закрытия (в Enem такого нет) (c)"],
            instr="Соедините")
f.head("G · DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Текст с пропусками", "B", "documento com foto = документ с фото",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "A", "seção = экзаменационная комната (секция)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "B", "Ворота закрываются в 13:00",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "A", "Экзамен заканчивается в 18:30",
     "— A prova termina às ___ . (A. 18h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Текст с пропусками", "B", "obrigado = спасибо",
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
f.bridge(f"Письменное задание (без единственного ответа); образец текста ({NWORDS} слов) ниже.")
f.ex("B1", "Письмо", "(открытое задание — образец ниже)", f"Образец — в разделе H этой страницы ({NWORDS} слов)",
     "«O seu domingo 15 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Напишите", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · ОТВЕТЫ — по страницам; найди свой номер", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Краткая заметка к каждому ответу · ✓ = письменное задание", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2552, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— PÁGINA {pg} —", 14, "sans", True, OLIVE, lh=1.16, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Письмо":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-avaliacao.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
