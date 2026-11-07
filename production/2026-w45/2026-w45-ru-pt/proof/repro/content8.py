# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/ru-pt-proof/repro-svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ · Teste e respostas", "Lucerna", "PÁGINA 8 · Большой тест недели + все ответы")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A · ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "4 de novembro é feriado",
     "Выходной посреди недели — ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "3 de novembro é dia de trabalho curto",
     "Короткий день — ___ ноября. (A. 2 · B. 3)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Liquidação até 12 de novembro",
     "Распродажа 11.11 закончится ___ ноября. (A. 12 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "O jogo principal é no sábado",
     "Матч «Краснодар» — ЦСКА будет в ___. (A. субботу · B. пятницу)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Placar do dérbi: 2 a 0",
     "Дерби ЦСКА — «Спартак» закончилось со счётом ___. (A. 2:0 · B. 0:0)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "A 15.ª rodada é em 20 de novembro",
     "15-й тур будет ___ ноября. (A. 20 · B. 8)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Volta às aulas em 5 de novembro",
     "Школьники идут в школу ___ ноября. (A. 4 · B. 5)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "Um código promocional é um código de desconto",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B · ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Escolha múltipla", "B", "4 de novembro é o Dia da Unidade Nacional",
     "Когда День народного единства? A. 2 ноября · B. 4 ноября · C. 5 ноября", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Folga na quinta e na sexta: 5 dias seguidos",
     "Сколько дней отдыха подряд, если взять отпуск в четверг и в пятницу? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Escolha múltipla", "B", "Dias de folga: quarta, sábado, domingo",
     "Сколько выходных дней в неделе 2–8 ноября? A. 2 · B. 3 · C. 4", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "A liquidação começou em 22 de outubro",
     "Когда началась распродажа 11.11? A. 22 октября · B. 2 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Segundo a imprensa especializada: descontos podem diminuir",
     "Что пишет торговая пресса о скидках? A. Их будет больше · B. Их может быть меньше · C. Их не будет", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "A", "O vencedor do dérbi é o CSKA",
     "Кто победил в дерби? A. ЦСКА · B. «Спартак» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "A", "A 13.ª rodada termina na segunda-feira",
     "Когда закрывается 13-й тур? A. 2 ноября · B. 6 ноября · C. 8 ноября", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "Um código promocional é um código de desconto",
     "Что такое промокод? A. Список · B. Код со скидкой · C. Магазин", size=13.8, gap=0)
f.head("C · ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё последние дни каникул: в среду, 4 ноября, — праздник, а в четверг — снова в школу. В среду Маша пойдёт на ярмарку с семьёй. А в субботу она будет смотреть футбол: «Краснодар» играет с ЦСКА. Маша болеет за «Краснодар».", 15, lh=1.3, split=False)
f.ex("A2", "Escolha múltipla", "B", "Os últimos dias de férias de Macha",
     "Что у Маши на этой неделе? A. Экзамены · B. Последние дни каникул · C. Новая школа", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "À feira na quarta-feira",
     "Куда Маша пойдёт в среду? A. В школу · B. На ярмарку · C. На футбол", size=13.8, gap=0)
f.ex("A2", "Escolha múltipla", "B", "Volta às aulas na quinta-feira",
     "Когда Маша снова идёт в школу? A. В среду · B. В четверг · C. В субботу", size=13.8, gap=0)
f.ex("B1", "Escolha múltipla", "B", "Macha torce pelo Krasnodar",
     "За кого болеет Маша? A. За ЦСКА · B. За «Краснодар» · C. За «Спартак»", size=13.8, gap=0)
f.head("D · СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Construção de frases", "В четверг школьники идут в школу.", "O tempo primeiro, o verbo em segundo",
     "в четверг / школьники / идут в школу → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("A2", "Construção de frases", "Мы берём отпуск в четверг и в пятницу.", "Sujeito + verbo + tempo",
     "мы / берём отпуск / в четверг и в пятницу → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "Construção de frases", "В субботу будет главный матч тура.", "O tempo primeiro, o verbo em segundo",
     "в субботу / будет / главный матч тура → ___", instr="Forme a frase", size=13.8, gap=0)
f.ex("B1", "Construção de frases", "Сначала составьте список покупок.", "Imperativo + objeto",
     "сначала / составьте / список покупок → ___", instr="Forme a frase", size=13.8, gap=0)
f.head("E · ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Tradução", "Na quarta-feira, 4 de novembro, é feriado.", "Ver a página 3",
     "В среду, 4 ноября, — выходной. → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "Tradução", "Um código promocional é um código de desconto.", "Ver a página 5",
     "Промокод — это код со скидкой. → ___", instr="Traduza para o português", size=13.8, gap=0)
f.ex("B1", "Tradução", "В субботу «Краснодар» играет с ЦСКА.", "Atenção: играть + с + instrumental",
     "No sábado, o Krasnodar joga contra o CSKA. → ___", instr="Traduza para o russo", size=13.8, gap=0)
f.ex("B2", "Tradução", "Поздравляю с Днём народного единства!", "поздравляю + с + instrumental",
     "Desejo a todos um feliz Dia da Unidade Nacional! → ___", instr="Traduza para o russo", size=13.8, gap=0)
f.head("F · СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Associação de palavras",
            ["выходной", "промокод", "пауза", "ярмарка"],
            ["код со скидкой",
             "место, где продают еду и подарки",
             "перерыв в чемпионате",
             "день, когда не работают"],
            ["d", "a", "c", "b"],
            ["Dia de folga d", "Código promocional a", "Pausa c", "Feira b"],
            instr="Associe")
f.head("G · ДИАЛОГ В МАГАЗИНЕ", 21, OLIVE, 5)
f.ex("B1", "Cloze", "A", "скидка = desconto",
     "— Здравствуйте! На эту куртку есть ___? (A. скидка · B. список)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "скидка 20%",
     "— Да, сегодня ___ 20%. (A. цена · B. скидка)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "у меня есть = tenho um código promocional",
     "— А у меня есть ___! (A. промокод · B. выходной)", size=13.8, gap=0)
f.ex("B1", "Cloze", "A", "его = o código promocional (masculino)",
     "— Отлично! Введите ___ в приложении. (A. его · B. её)", size=13.8, gap=0)
f.ex("B1", "Cloze", "B", "Boas compras",
     "— Спасибо! Хороших ___! (A. скидок · B. покупок)", size=13.8, gap=0)
f.head("H · НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Моя неделя с праздником посреди недели начинается в понедельник, 2 ноября. "
          "В понедельник и во вторник я работаю, а в среду, 4 ноября, — выходной. "
          "В среду я пойду на ярмарку с семьёй: куплю еду и подарки. "
          "В четверг и в пятницу я снова работаю, но вечером смотрю футбол. "
          "В субботу, 7 ноября, «Краснодар» играет с ЦСКА, и я буду болеть за «Краснодар». "
          "В воскресенье я отдохну дома и подготовлюсь к новой неделе. "
          "Такая неделя мне нравится: праздник посреди недели — как маленький подарок!")
NWORDS = len(MODELO.split())
f.bridge(f"Tarefa de escrita (sem resposta única); texto modelo ({NWORDS} palavras) abaixo.")
f.ex("B1", "Escrita", "(pergunta aberta — texto modelo abaixo)", f"O texto modelo está na seção H desta página ({NWORDS} palavras)",
     "«Моя неделя с праздником посреди недели» Напишите 80–100 слов: что вы будете делать в среду, в выходные и куда поедете?", instr="Escreva", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, GOLD, 2)
p.text(MX, 1302, "ОТВЕТЫ · Respostas — por página: procure o seu número", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Cada resposta tem uma nota breve em português · ✓ = exercício com texto modelo", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2540, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Escrita":
            txt = f"{e_['n']}. ✓ {e_['note']}"
        af.para(txt, 13.0, lh=1.13, gap=0.5, split=False)
af.end_report()
p.foot(8)
p.save(f"{OUT}/p8-test.svg")
print("P8 saved, TOTAL exercises:", len(REG))
from collections import Counter
print("by level", dict(Counter(e["level"] for e in REG)))
print("by page", dict(sorted(Counter(e["page"] for e in REG).items())))
print("by type", dict(Counter(e["type"] for e in REG)))
print("model words:", NWORDS)
