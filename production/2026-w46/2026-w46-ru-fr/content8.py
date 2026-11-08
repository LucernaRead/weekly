# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P8 · ТЕСТ И ОТВЕТЫ =================
CURPAGE[0] = 8
p = BSPage4()
p.band("ТЕСТ И ОТВЕТЫ　TEST ET RÉPONSES", "Lucerna", "PAGE 8　Le grand test de la semaine + toutes les réponses")

f = Flow(p, [(COLX[i], CW) for i in range(4)], 180, 1252, tag="P8-ex")
f.head("A　ХРОНИКА НЕДЕЛИ", 21, OLIVE, 5)
f.ex("B1", "Choix", "A", "Lundi 9 novembre",
     "Обычная неделя начинается ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "10 novembre — Jour de la police",
     "День полиции — ___ ноября. (A. 9 · B. 10)", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Jour des soldes : 11 novembre",
     "День распродажи 11.11 — ___ ноября. (A. 11 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Jeudi contre l’Ouzbékistan",
     "Сборная России играет с ___. (A. Узбекистаном · B. Венесуэлой)", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Résultats de la 14e journée inconnus à la mise sous presse",
     "Итоги 14-го тура на момент сдачи номера ___. (A. неизвестны · B. известны)", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "15e journée le 20 novembre",
     "15-й тур будет ___ ноября. (A. 20 · B. 15)", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Lilia sort le 12 novembre",
     "Фильм «Лиля» выходит ___ ноября. (A. 13 · B. 12)", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Un code promo est un code de réduction.",
     "Промокод — это код со ___. (A. скидкой · B. списком)", size=13.8, gap=0)
f.head("B　ОБЩИЕ ВОПРОСЫ", 21, OLIVE, 5)
f.ex("A2", "Choix", "B", "10 novembre — Jour de la police",
     "Когда День полиции? A. 9 ноября · B. 10 ноября · C. 11 ноября", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "5 jours de travail dans la semaine",
     "Сколько рабочих дней на этой неделе? A. 3 · B. 5 · C. 7", size=13.8, gap=0)
f.ex("B2", "Choix", "B", "10 jours de repos en novembre",
     "Сколько выходных и праздничных дней в ноябре? A. 20 · B. 10 · C. 5", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Les soldes ont commencé le 22 octobre",
     "Когда началась распродажа 11.11 на Ozon? A. 22 октября · B. 9 ноября · C. 12 ноября", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Météorologues : neige mouillée possible",
     "Что обещают синоптики? A. Жаркое лето · B. Первый мокрый снег · C. Устойчивый снег", size=13.8, gap=0)
f.ex("A2", "Choix", "A", "Le Spartak a battu le Lokomotiv 4-0",
     "Кто победил в матче «Спартак» — «Локомотив»? A. «Спартак» 4:0 · B. «Локомотив» · C. Ничья", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "13e journée : CSKA 0-0 Orenbourg",
     "Как сыграли ЦСКА и «Оренбург»? A. 0:0 · B. 4:0 · C. 1:2", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "Un colis doit être suivi, retiré, vérifié",
     "Что надо сделать с посылкой? A. Выбросить · B. Отследить, получить и проверить · C. Вернуть в кино", size=13.8, gap=0)
f.head("C　ЧИТАЙТЕ И ОТВЕЧАЙТЕ", 21, OLIVE, 5)
f.para("Маша учится в школе в Москве. На этой неделе у неё обычная неделя: пять учебных дней и никаких праздников. В среду, 11 ноября, Маша заказывает книгу на распродаже 11.11. В четверг она получает посылку в пункте выдачи и проверяет книгу. А в субботу Маша идёт в кино с друзьями: они смотрят фильм «Лиля».", 15, lh=1.3, split=False)
f.ex("A2", "Choix", "B", "La semaine de Macha est une semaine ordinaire",
     "Какая неделя у Маши? A. Каникулы · B. Обычная неделя · C. Экзамены", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "Mercredi, elle commande un livre",
     "Что Маша заказывает в среду? A. Билет в кино · B. Книгу · C. Промокод", size=13.8, gap=0)
f.ex("A2", "Choix", "B", "Jeudi, elle retire un colis au point relais",
     "Где Маша получает посылку? A. В кино · B. В пункте выдачи · C. В школе", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Samedi, elle voit Lilia avec une amie",
     "Куда Маша идёт в субботу? A. В школу · B. В кино с друзьями · C. На ярмарку", size=13.8, gap=0)
f.head("D　СОБЕРИТЕ ПРЕДЛОЖЕНИЯ", 21, OLIVE, 5)
f.ex("A2", "Phrases", "В среду Маша заказывает книгу.", "Sujet + verbe + objet",
     "в среду / Маша / заказывает книгу → ___", instr="Phrases", size=13.8, gap=0)
f.ex("A2", "Phrases", "В четверг она получает посылку.", "Sujet + verbe + objet",
     "в четверг / она / получает посылку → ___", instr="Phrases", size=13.8, gap=0)
f.ex("B1", "Phrases", "В субботу Маша идёт в кино.", "Le temps d’abord, le verbe en deuxième",
     "в субботу / Маша / идёт в кино → ___", instr="Phrases", size=13.8, gap=0)
f.ex("B1", "Phrases", "Сначала составьте список покупок.", "Impératif + objet",
     "сначала / составьте / список покупок → ___", instr="Phrases", size=13.8, gap=0)
f.head("E　ПЕРЕВЕДИТЕ", 21, OLIVE, 5)
f.ex("A2", "Traduction", "Mardi 10 novembre — Jour de la police.", "Comparer page 2",
     "Во вторник, 10 ноября, — День полиции. → ___", instr="Traduire en français", size=13.8, gap=0)
f.ex("B1", "Traduction", "Un colis doit être suivi, retiré et vérifié.", "Comparer page 5",
     "Посылку нужно отследить, получить и проверить. → ___", instr="Traduire en français", size=13.8, gap=0)
f.ex("B1", "Traduction", "Jeudi, la Russie joue contre l’Ouzbékistan.", "Attention : играть + с + instrumental",
     "В четверг сборная России играет с Узбекистаном. → ___", instr="Traduire en français", size=13.8, gap=0)
f.ex("B2", "Traduction", "Bon Jour de la police à toutes et à tous !", "поздравляю + с + instrumental",
     "Поздравляю с Днём полиции! → ___", instr="Traduire en français", size=13.8, gap=0)
f.head("F　СЛОВА НЕДЕЛИ", 21, OLIVE, 5)
f.match_set("B2", "Appariement",
            ["предзимье", "посылка", "пик", "гололедица"],
            ["самое большое число заказов",
             "лёд на дороге",
             "время между осенью и зимой",
             "товар, который прислали по почте"],
            ["c", "d", "a", "b"],
            ["avant-hiver c", "colis d", "pic a", "le verglas b"],
            instr="Associer")
f.head("G　ДИАЛОГ В ПУНКТЕ ВЫДАЧИ", 21, OLIVE, 5)
f.ex("B1", "Choix", "A", "Retirer un colis : номер заказа",
     "— Здравствуйте! Я пришла за посылкой. Вот ___ заказа. (A. номер · B. пик)", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Le colis est arrivé",
     "— Да, ваша посылка уже ___. (A. ушла · B. пришла)", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Veuillez vérifier le colis",
     "— Проверьте ___, пожалуйста. (A. посылку · B. промокод)", size=13.8, gap=0)
f.ex("B1", "Choix", "A", "Tout va bien",
     "— Всё в порядке, спасибо! Книга ___. (A. целая · B. мокрая)", size=13.8, gap=0)
f.ex("B1", "Choix", "B", "Bon shopping",
     "— Спасибо! Хороших ___! (A. скидок · B. покупок)", size=13.8, gap=0)
f.head("H　НАПИШИТЕ САМИ", 21, OLIVE, 5)
MODELO = ("Моя обычная неделя в ноябре начинается в понедельник, 9 ноября. "
          "В понедельник и во вторник я работаю, а вечером читаю книгу. "
          "Во вторник, 10 ноября, я поздравляю знакомого полицейского с Днём полиции. "
          "В среду, 11 ноября, — день распродажи 11.11: я заказываю книгу и проверяю промокод. "
          "В четверг я получаю посылку и проверяю покупку. "
          "В пятницу вечером я иду в кино с друзьями. "
          "В субботу я высыпаюсь и гуляю в парке, а в воскресенье готовлюсь к новой неделе. "
          "Обычная неделя мне нравится: ровный ритм — это хорошо!")
NWORDS = len(MODELO.split())
f.bridge(f"Rédaction (pas de réponse unique) ; texte modèle ({NWORDS} mots) ci-dessous.")
f.ex("B1", "Rédaction", "(Question ouverte, texte modèle ci-dessous)", f"Voir le texte modèle dans la section H de cette page ({NWORDS} mots)",
     "«Моя обычная неделя в ноябре» Напишите 80–100 слов: что вы будете делать каждый день недели?", instr="Rédaction", size=13.8, gap=0)
f.para("Пример: " + MODELO, 14.5, lh=1.3, split=False)
f.end_report()

p.hline(MX, RIGHT, 1264, OLIVE, 2)
p.text(MX, 1302, "ОТВЕТЫ　CORRIGÉ — CLASSÉ PAR PAGE ; TROUVEZ LE NUMÉRO D’EXERCICE", 25, "sans", True, OLIVE)
p.text(RIGHT, 1302, "Chaque réponse avec une courte note en français　✓ = texte modèle", 19.5, "sans", False, GREY, anchor="end")
by_page = {}
for e_ in REG:
    by_page.setdefault(e_["page"], []).append(e_)
af = Flow(p, [(COLX[i], CW) for i in range(4)], 1328, 2560, tag="P8-keys")
for pg in sorted(by_page):
    af.para(f"— СТРАНИЦА {pg} —", 13.3, "sans", True, OLIVE, lh=1.13, gap=2, split=False)
    for e_ in by_page[pg]:
        txt = f"{e_['n']}. {e_['key']} — {e_['note']}"
        if e_["type"] == "Rédaction":
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
