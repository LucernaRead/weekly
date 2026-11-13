# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("YOUTH　Молодёжь", "The Lucerna", "LEVEL B1　Break the silence　Нарушь молчание")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P5-main")
f.title("Break the Silence: Odd Socks and Loud Voices", 32)
f.byline("By The Lucerna newsroom　Reading level: B1")
f.para("On Monday, November 16, schools across Britain do something strange: children and teachers wear odd socks. One red sock, one blue sock — on purpose. It is Odd Socks Day, the first day of Anti-Bullying Week, and this year is its tenth birthday.")
f.para("Anti-Bullying Week runs from Monday, November 16, to Friday, November 20. It is organised by the Anti-Bullying Alliance, and this year's theme is “Break the Silence”. The idea is simple: bullying is hardest to stop when nobody speaks about it. So the week asks children — and adults — to start conversations, to speak up, to listen, and to take action together.")
f.para("The numbers are big: the campaign reaches about eight million children and young people, and more than 80% of schools in England, Wales and Northern Ireland take part. The theme was chosen with more than 200 children and young people, who said that speaking up was the hardest part.")
f.para("Friday, November 20, is also World Children's Day — a day for children's rights around the world, led by UNICEF. This year's theme is “My day. My rights. My future.” The date marks the day in 1989 when the United Nations adopted the Convention on the Rights of the Child.")
f.para("What can one child do? Tell a teacher. Tell a parent. Tell a friend. And if you see someone alone at lunch, sit with them. A small act is not small to the person it helps — and a loud voice starts with one sentence.")
f.box("ODD SOCKS, IN NUMBERS　Цифры", [
    ("10 — years of Odd Socks Day. 8 million — children reached by the week. 200 — children who helped choose this year's theme.", "serif", False, INK, 21.5, 1.4),
], tsize=21)  # boxtitle fix2 2026-11-12: 23pt over +24.3px right; 22pt still over (-6px), 21pt fits (~+13px margin)
f.para("If you want to practise Monday-morning English, try this: wear odd socks, and explain them in English. “I wear odd socks for Anti-Bullying Week. Different is good.” Three sentences — and a whole week of practice.", 23.5)
f.gloss("bullying = травля · to speak up = говорить открыто · a right = право · silence = молчание")
f.head("A　COMPREHENSION", 25)
f.bridge("Прочитай статью стр. 5 и выбери ответ.")
f.ex("B1", "Выбрать ответ", "B", "Неделя против травли, 16–20 ноября",
     "Anti-Bullying Week runs from... A. November 9 to 13 · B. Monday, November 16, to Friday, November 20 · C. November 20 to 26", size=22)
f.ex("B1", "Выбрать ответ", "A", "Тема этого года — «Нарушь молчание»",
     "This year's theme is... A. “Break the Silence” · B. “Challenge Yourself” · C. “My day. My rights.”", size=22)
f.ex("B1", "Выбрать ответ", "C", "Дню разных носков исполняется десять лет",
     "Odd Socks Day is... A. new this year · B. five years old · C. ten years old", size=22)
f.ex("B1", "Выбрать ответ", "B", "Кампания охватывает около восьми миллионов детей",
     "The campaign reaches about... A. 200 children · B. eight million children · C. 80 children", size=22)
f.ex("B1", "Выбрать ответ", "A", "Всемирный день ребёнка — пятница, 20 ноября",
     "World Children's Day is on... A. Friday, November 20 · B. Monday, November 16 · C. Thursday, November 26", size=22)
f.ex("B1", "Выбрать ответ", "C", "Конвенция о правах ребёнка принята в 1989 году",
     "The Convention on the Rights of the Child was adopted in... A. 1910 · B. 1969 · C. 1989", size=22)
f.head("B　SENTENCES", 25)
f.bridge("Дополни предложения данными словами.")
f.ex("B1", "Дополнить предложения", "silence", "silence = молчание",
     "Break the ___: speak up about bullying.", instr="Заполни")
f.ex("B1", "Дополнить предложения", "socks", "sock = носок",
     "On Monday, children wear odd ___.", instr="Заполни")
f.ex("A2", "Дополнить предложения", "rights", "right = право",
     "Every child has ___.", instr="Заполни")
f.ex("A2", "Дополнить предложения", "up", "speak up = говорить открыто",
     "Speak ___: tell a teacher.", instr="Заполни")
f.head("C　THE WORDS", 25)
f.match_set("B1", "Подобрать пары",
            ["bullying", "to speak up", "a right", "silence"],
            ["saying what you think, loudly and clearly",
             "something every child has, by law",
             "saying nothing at all",
             "hurting or frightening someone again and again"],
            ["d", "a", "b", "c"],
            ["bullying = травля d", "speak up = говорить открыто a", "right = право b", "silence = молчание c"],
            instr="Подбери пары")
f.head("D　PRESENT CONTINUOUS", 25)
f.bridge("Перепиши в настоящем продолженном времени (то, что происходит сейчас).")
f.ex("B1", "Преобразовать предложения", "Schools are wearing odd socks today.", "wear → are wearing",
     "Schools (wear) odd socks today. → ___", instr="Перепиши")
f.ex("B1", "Преобразовать предложения", "Children are speaking up this week.", "speak → are speaking",
     "Children (speak) up this week. → ___", instr="Перепиши")
f.ex("B1", "Преобразовать предложения", "We are listening to every child.", "listen → are listening",
     "We (listen) to every child. → ___", instr="Перепиши")
f.ex("B1", "Преобразовать предложения", "She is sitting with a new friend.", "sit → is sitting",
     "She (sit) with a new friend. → ___", instr="Перепиши")
f.end_report()

# col 3: image + side flow
ix = COLX[3]
image(p, "children.jpg", ix, 200, CW, 440)
cy5 = caption(p, ix, 640, CW, "Children from Lawrence, Massachusetts, marching in New York on February 19, 1912, during the textile strike. They asked for bread — and the world listened. Children have always had a voice.",
              "Bain News Service — public domain, via Library of Congress")
v5 = Flow(p, [(ix, CW)], int(cy5) + 18, 2560, tag="P5-col3")
v5.box("SPEAK UP　Говори громко", [
    ("“Break the silence.” “Different is good.” “Sit with me.” — three sentences for one week. Learn them, and Monday morning in English is yours.", "serif", False, INK, 21.5, 1.42),
])
v5.head("FRIDAY'S WORDS", 25)
v5.para("“My day. My rights. My future.” — the words of World Children's Day, Friday, November 20. Three short sentences, one big idea: children have a voice, and the world should listen.", 22)
v5.para("“Every child has rights” means: every child, everywhere, has the right to be safe, to learn, and to be heard. After that sentence, the listening begins.", 22)
v5.bridge("У каждого ребёнка есть права | Every child has rights = У каждого ребёнка есть права.")
v5.head("THE JUNGLE, TOO", 25)
v5.para("After Friday, the weekend keeps going: the jungle is on every night, and the football is back on Saturday. The week ends with sport — and starts again with school on Monday.", 22)
v5.end_report()
p.foot(5)
p.save(f"{OUT}/p5-youth.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("DEEP READ　Подробнее", "The Lucerna", "LEVEL B2　The map after November 3　Карта после 3 ноября")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P6-main")
f.title("The Map After November 3: Reading the Results", 32)
f.byline("By The Lucerna newsroom　Reading level: B2")
f.para("The vote is counted. The map is still being drawn. On Tuesday, November 3, Americans voted for the House, for a third of the Senate, and for governor in 36 states. By the Sunday after the vote, November 8, the Associated Press had called the big question: the Democrats had won both houses of Congress.")
f.para("Here is the map, as called on Sunday, November 8. In the House, the Democrats won 254 seats, the Republicans 162, and 19 races were still uncalled. In the Senate, the Democrats won 20 of the 33 races called and the Republicans 13, with Alaska and Mississippi still uncalled. Seven Senate seats changed hands, and all seven went to the Democrats: Iowa, Kansas, Maine, North Carolina, Ohio, South Carolina and Texas.")
f.para("What does “called” mean? A call is a news organisation's judgement: the maths is clear, and the candidate behind cannot catch up. It is not the official result. The official result comes when each state certifies its count — between November 10 and December 18, with no fixed date in some states. In Georgia, a Senate race with no majority winner goes to a runoff on December 1 — but this time Jon Ossoff won reelection with about 59% of the vote, so there was no runoff. Mississippi has no runoff in a regular election: the candidate with the most votes wins.")
f.para("What changes? In January 2027, the new Congress meets, with a Democratic House and a Democratic Senate. The two parties choose their leaders first: the House Republicans on November 10, the House Democrats on November 18 and 19. The Speaker — the leader of the House — is chosen when the new Congress meets in January. The Speaker, Mike Johnson, has said he will not run to lead the Republicans in the new Congress.")
f.para("What does not change? The President stays the same, and so does the White House. A midterm changes Congress, not the President. That is the American system: the voters speak in the middle of a President's term, and the two sides must then work — or argue — together. The map is drawn. The work starts in January.")
f.box("A PRACTICE BALLOT　Бюллетень", [
    ("For Governor: ☐ Candidate A · ☐ Candidate B. For the House: ☐ Candidate C · ☐ Candidate D. Names are codes here — this ballot teaches how to mark, not whom to choose.", "serif", False, INK, 21.5, 1.4),
], tsize=22)  # boxtitle fix2 2026-11-12: 23pt over +11.4px right; 22pt fits (~+6.6px margin)
f.para("A note on numbers in this issue: this paper prints the calls of Sunday, November 8, and says so. The calls can still move a little as the count goes on — and this paper will not guess the final numbers. When the certified results are in, VOL.5 will report them.")
f.gloss("to call a race = объявить результат · to certify = официально утвердить · a runoff = второй тур · a map = политическая карта.")
# practice chart
f.head("READ THE CHART　График", 25)
f.para("How big was the change? The chart is the calls of Sunday, November 8 — not the certified results, and not a prediction.", 22)
for lab in ["House called: 254 Democrats, 162 Republicans, 19 uncalled (Nov 8)",
            "Senate called: 20 Democrats, 13 Republicans, 2 uncalled (Nov 8)",
            "Senate flips: 7, all to the Democrats",
            "Governors flipped: 5, all to the Democrats",
            "States certify: November 10 to December 18",
            "Runoff, if needed: December 1 (Georgia only)"]:
    f.para(lab, 22, "serif", True, OLIVE, 1.3, 2)
f.head("A　CHART READING", 25)
f.bridge("Прочитай график с объявленными цифрами выше и выбери правильный ответ.")
f.ex("B2", "Чтение графиков", "B", "Объявлено 8 ноября: у демократов 254 мандата в Палате представителей",
     "In the House, as called on November 8, the Democrats won... A. 218 seats · B. 254 seats · C. 162 seats", size=22)
f.ex("B2", "Чтение графиков", "C", "В Палате представителей 19 мандатов ещё не объявлены",
     "In the House, races still uncalled: ... A. 2 · B. 13 · C. 19", size=22)
f.ex("B2", "Чтение графиков", "A", "В Сенате объявлены 33 мандата из 35",
     "In the Senate, races called: ... A. 33 of 35 · B. 20 of 35 · C. 35 of 35", size=22)
f.ex("B2", "Чтение графиков", "B", "Семь мест в Сенате перешли к другой партии — все к демократам",
     "Senate seats that changed hands: ... A. 5 · B. 7 · C. 22", size=22)
f.ex("B2", "Чтение графиков", "A", "Пять губернаторских постов перешли к другой партии — все к демократам",
     "Governors' offices that changed hands: ... A. 5 · B. 7 · C. 2", size=22)
f.ex("B2", "Чтение графиков", "C", "254 + 162 + 19 = 435 (всего мест в Палате представителей)",
     "The House numbers add up to... A. 218 · B. 413 · C. 435", size=22)
f.head("B　COMPREHENSION", 25)
f.bridge("Прочитай статью стр. 6 и выбери ответ.")
f.ex("B2", "Выбрать ответ", "B", "«Объявить результат» — это ещё не официальный итог",
     "A “call” is... A. the official result · B. a news organisation's judgement · C. a vote in Congress", size=22)
f.ex("B2", "Выбрать ответ", "A", "Официальный результат — после утверждения штатами",
     "The official result comes when... A. the state certifies its count · B. TV calls the race · C. the first votes arrive", size=22)
f.ex("B2", "Выбрать ответ", "C", "Два мандата в Сенате ещё не определены: Аляска и Миссисипи",
     "The two Senate races still uncalled are in... A. Georgia and Texas · B. Iowa and Ohio · C. Alaska and Mississippi", size=22)
f.ex("B2", "Выбрать ответ", "B", "Республиканцы Палаты выбирают лидера 10 ноября",
     "The House Republicans choose their leader on... A. November 8 · B. November 10 · C. November 18", size=22)
f.ex("B2", "Выбрать ответ", "A", "Промежуточные выборы меняют Конгресс, а не президента",
     "A midterm changes... A. Congress, not the President · B. the President, not Congress · C. the courts", size=22)
f.ex("B2", "Выбрать ответ", "C", "VOL.5 сообщит утверждённые окончательные итоги",
     "The certified results will be reported in... A. VOL.3 · B. this issue · C. VOL.5", size=22)
f.head("C　SENTENCES", 25)
f.bridge("Дополни предложения данными словами.")
f.ex("B2", "Дополнить предложения", "certify", "certify = утвердить официально",
     "Each state must ___ its count.", instr="Заполни")
f.ex("B2", "Дополнить предложения", "call", "call a race = объявить итоги выборов",
     "News organisations ___ a race when the maths is clear.", instr="Заполни")
f.ex("B2", "Дополнить предложения", "changed", "change hands = перейти к другой партии",
     "Seven Senate seats ___ hands on election night.", instr="Заполни")
f.ex("B1", "Дополнить предложения", "takes", "take time = занимать время",
     "Counting ___ time in every state.", instr="Заполни")
f.ex("B1", "Дополнить предложения", "differs", "differ, 3-е лицо ед. ч.: differs",
     "The rule ___ from state to state.", instr="Заполни")
f.ex("B1", "Дополнить предложения", "official", "official = официальный",
     "A call is not the ___ result.", instr="Заполни")
f.end_report()

# col 3: image + terms box
ix = COLX[3]
image(p, "voting.jpg", ix, 200, CW, 300)
cy6 = caption(p, ix, 500, CW, "A voting booth in the Old State House, Hartford, Connecticut: one voter, one ballot, one private moment. On Tuesday, November 3, millions of Americans did the same.",
              "Kenneth C. Zirkel — CC0, via Wikimedia Commons")
v6 = Flow(p, [(ix, CW)], int(cy6) + 18, 2560, tag="P6-col3")
v6.box("HOW LONG?　Срок полномочий", [
    ("House: 2 years, all 435 seats each midterm. Senate: 6 years, about a third each election. President: 4 years. Governor: usually 4 years.", "serif", False, INK, 21.5, 1.42),
])
v6.head("FIFTY ELECTIONS", 25)
v6.para("One country, fifty systems: that is why American election night is a map, not a single number. Learn the map, and the night makes sense.", 22)
v6.bridge("Одна карта: пятьдесят штатов — пятьдесят правил; поэтому в ночь выборов смотрят на карту, а не на одно число.")
v6.end_report()
p.foot(6)
p.save(f"{OUT}/p6-deep.svg")
print("P6 saved, exercises so far:", len(REG))
