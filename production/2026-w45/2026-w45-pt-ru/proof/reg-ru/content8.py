# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/pt-ru-proof/out-ru/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · AVALIAÇÃO E RESPOSTAS =================
CURPAGE[0] = 8
p = BSPage4()
p.band("AVALIAÇÃO E RESPOSTAS · Тест и ответы", "A Lucerna", "СТРАНИЦА 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · COMPLETE A CRÔNICA", 22, OLIVE, 5)
f.ex("B1", "Выбор в пропуске", "A", "День 1 — 8 ноября",
     "No domingo 8, o Brasil faz ___ do Enem. (A. o primeiro dia · B. o segundo dia)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "Ворота закрываются в 13h",
     "Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "Экзамен начинается в 13:30",
     "A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "Финадос — 2 ноября",
     "Finados é no dia ___ de novembro. (A. 2 · B. 15)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "Ответный матч «Васко» × «Палмейрас» — 8-го",
     "A volta de Vasco × Palmeiras é no domingo ___ . (A. 1º · B. 8)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "Длинные выходные — всего 3 дня",
     "O feriadão tem ___ dias. (A. dois · B. três)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "Экзамен длится пять с половиной часов",
     "No dia 8, a prova dura ___ . (A. cinco horas e meia · B. sete horas)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "День 2 — 15 ноября",
     "O segundo dia do Enem é no dia ___ . (A. 8 · B. 15)", size=14.5, gap=0)
f.head("B · PERGUNTAS GERAIS", 22, OLIVE, 5)
f.ex("A2", "Выбор ответа", "B", "Длинные выходные — с 31 октября по 2 ноября",
     "O feriadão vai... A. de 8 a 15 · B. de 31 de outubro a 2 de novembro · C. de 2 a 5", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "Карточка подтверждения — документ Enem",
     "O Cartão de Confirmação é um documento... A. da Copa do Brasil · B. do Enem · C. do Halloween", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "B", "Ответный матч «Атлетико Минейро» × «Гремио» — на «Арене MRV»",
     "Atlético-MG × Grêmio, a volta, é... A. em São Januário · B. na Arena MRV · C. no Maracanã", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "B", "В 34-м туре матчи идут с понедельника по пятницу",
     "A rodada 34 do Brasileirão... A. é só no fim de semana · B. vai de segunda a sexta · C. já terminou", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "B", "На Финадос семьи несут цветы",
     "Em Finados, as famílias levam... A. fogos · B. flores · C. presentes", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "Хэллоуин был в субботу, 31 октября",
     "Halloween foi... A. no domingo 8 · B. no sábado, 31 de outubro · C. na segunda 2", size=14.5, gap=0)
f.ex("B2", "Выбор ответа", "A", "330 — это минуты экзамена",
     "O número 330 mede... A. os minutos da prova · B. os dias do feriadão · C. os inscritos", size=14.5, gap=0)
f.ex("B1", "Выбор ответа", "A", "Финадос называют также Днём усопших верных",
     "Finados, em português, também se chama... A. Dia dos Fiéis Defuntos · B. Dia da Independência · C. Dia do Trabalho", size=14.5, gap=0)
f.head("C · LEIA E RESPONDA", 22, OLIVE, 5)
f.para("Lucas mora em Belo Horizonte. No domingo 8, ele faz o Enem pela primeira vez. Na segunda, 2, ele descansa no feriadão e revisa um pouco por dia. Na véspera, ele separa o documento e a caneta preta e dorme cedo. No domingo, ele chega ao local às 11h, duas horas antes de os portões fecharem, e faz a prova com calma.", 15.5, lh=1.3, split=False)
f.ex("A2", "Выбор ответа", "B", "Лукас живёт в Белу-Оризонти",
     "Onde mora Lucas? A. no Rio · B. em Belo Horizonte · C. em São Paulo", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "В выходные он отдыхает и повторяет понемногу каждый день",
     "O que Lucas faz no feriadão? A. só festa · B. descansa e revisa um pouco por dia · C. viaja para a praia", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "Накануне он готовит документ и чёрную ручку и рано ложится",
     "Na véspera, Lucas... A. faz maratona a noite inteira · B. separa o documento e dorme cedo · C. compra a caneta azul", size=14.5, gap=0)
f.ex("A2", "Выбор ответа", "B", "Он приходит на место экзамена в 11h",
     "Lucas chega ao local... A. às 13h30 · B. às 11h · C. às 19h", size=14.5, gap=0)
f.head("D · CONSTRUA AS FRASES", 22, OLIVE, 5)
f.ex("A2", "Составьте предложение", "Domingo é dia de prova.", "Слово времени — первым",
     "domingo / é / dia de prova → ___", instr="Составьте", size=14.5, gap=0)
f.ex("B1", "Составьте предложение", "O candidato confere o cartão no aplicativo.", "Подлежащее + глагол + дополнение + место",
     "o candidato / confere / o cartão / no aplicativo → ___", instr="Составьте", size=14.5, gap=0)
f.ex("B1", "Составьте предложение", "Que horas começa a prova?", "Вопросительное словосочетание — первым",
     "que horas / começa / a prova / ? → ___", instr="Составьте", size=14.5, gap=0)
f.ex("B1", "Составьте предложение", "O Brasil lembra os seus mortos.", "Подлежащее + глагол + дополнение",
     "o Brasil / lembra / os seus mortos → ___", instr="Составьте", size=14.5, gap=0)
f.head("E · TRADUZA", 22, OLIVE, 5)
f.ex("A2", "Перевод", "Воскресенье, 8 ноября, — первый день Enem.", "См. заголовок страницы 6",
     "Domingo, 8 de novembro, é o primeiro dia do Enem. → ___", instr="Переведите", size=14.5, gap=0)
f.ex("B1", "Перевод", "Проверьте карточку подтверждения до воскресенья.", "Confira = проверьте",
     "Confira o cartão antes do domingo. → ___", instr="Переведите", size=14.5, gap=0)
f.ex("B1", "Перевод", "O feriadão é de 31 de outubro a 2 de novembro.", "feriadão = длинные выходные",
     "«Длинные выходные — с 31 октября по 2 ноября». → ___", instr="Переведите", size=14.5, gap=0)
f.ex("B2", "Перевод", "Quando você chegar, apresente o documento com foto.", "будущее сослагательное chegar + повелительное apresente",
     "Когда вы придёте, покажите документ с фотографией. → ___", instr="Переведите", size=14.5, gap=0)
f.head("F · AS PALAVRAS DA SEMANA", 22, OLIVE, 5)
f.match_set("B2", "Сопоставление",
            ["o feriadão", "o portão", "a reta final", "a segunda chamada"],
            ["a última semana antes da prova",
             "um feriado grudado no fim de semana",
             "uma nova entrada depois do fechamento — que não existe no Enem",
             "a porta de entrada do local de prova"],
            ["b", "d", "a", "c"],
            ["feriadão = праздник, слившийся с выходными (b)", "portão = вход на место экзамена (d)", "reta final = последняя неделя перед экзаменом (a)", "segunda chamada = повторный вход после закрытия (в Enem его нет) (c)"],
            instr="Соедините пары")
f.head("G · DIÁLOGO NO PORTÃO", 22, OLIVE, 5)
f.ex("B1", "Выбор в пропуске", "B", "documento com foto = документ с фотографией",
     "— Bom dia! O seu ___ com foto, por favor. (A. cartão · B. documento)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "seção = экзаменационный сектор (аудитория)",
     "— A sua ___ é a 042. (A. seção · B. zona)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "Ворота закрываются в 13h",
     "— Os portões fecham às ___ . (A. 12h · B. 13h)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "A", "Экзамен начинается в 13:30",
     "— A prova começa às ___ . (A. 13h30 · B. 19h)", size=14.5, gap=0)
f.ex("B1", "Выбор в пропуске", "B", "obrigado = спасибо",
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
f.expl(f"Задание без единственного правильного ответа; образец текста ({NWORDS} слова) — ниже.")
f.ex("B1", "Письмо", "(открытое задание — образец ниже)", f"Образец — в разделе H этой страницы ({NWORDS} слова)",
     "«O seu domingo 8 de novembro» Escreva 80–100 palavras: onde você faz a prova (ou descansa), o que confere antes de sair, e o seu plano para o dia.", instr="Напишите", size=14.5, gap=0)
f.para("Texto modelo: " + MODELO, 15, lh=1.3, split=False)
f.end_report()

# ================= RESPOSTAS =================
p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "RESPOSTAS · Ответы — по страницам: ищите по номеру задания", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "К каждому ответу — короткое пояснение · ✓ — задание с образцом текста", 19.5, "sans", False, GREY, anchor="end")
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
        af.para(txt, 13, lh=1.12, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-avaliacao.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("model words:", NWORDS)
