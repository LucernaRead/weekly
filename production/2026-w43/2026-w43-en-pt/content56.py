# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-en-pt/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("YOUTH · Jovens", "The Lucerna", "LEVEL B1 · Screens, streams & new machines")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P5-main")
f.title("Opening Week Lives on Your Phone", 37)
f.byline("By The Lucerna newsroom · Reading level : B1")
f.head("THE GAME COMES TO YOU", 26)
f.para("For fifty years, a big game meant a television in the living room. This week, the NBA opened its season in a new way : opening night was built as a tripleheader for NBC — and for its streaming service, Peacock. Three games, one night, every screen in the house.")
f.para("Young fans do not always watch a whole game. Many meet the game first as a clip : forty seconds of the best moment, sent by a friend, watched on the bus. The full game comes later — or never. On Wednesday morning, one of the top trending searches in America was « lakers roster » : before watching the team, fans wanted the list of names. Who plays for the Lakers this year ?")
f.head("AI PLANS YOUR COSTUME", 26)
f.para("Halloween is the other screen story of the week. The NRF counts a new habit : 47% of celebrants now use AI tools to plan a costume or a decoration. You describe an idea — « a Greek god, but funny » — and the machine offers ten versions. Then the group chat votes.")
f.para("The costume itself is content now. A good costume is not finished when you put it on ; it is finished when the photo is posted. Google's Frightgeist list and the Spirit Halloween list agree on the stars of 2026 : KPop Demon Hunters, Toy Story 5, superheroes and Greek gods. This year, the gods have good lighting.")
f.head("EARNINGS, IN PLAIN ENGLISH", 26)
f.para("On Wednesday, after the markets close, two giants publish their numbers : Tesla and Meta. Netflix and SpaceX did the same on Tuesday. « Earnings » is a company's report card : how much money came in, how much went out, and what is left — the profit.")
f.para("For a few hours, every feed is green arrows and red arrows. One warning from our business desk : before the report, different experts give different numbers — nobody knows. After the close, everybody knows at the same time. That is the game, and this week, America is watching it live.")
f.head("THE SECOND SCREEN", 26)
f.para("Watch a game with young fans and you will see two games at once. On the television, the match. On the phone, the second match : live statistics, polls — « Who wins tonight ? » — and the group chat, where every goal, every basket, produces twenty messages in ten seconds. The phone does not kill the game. For this generation, the phone IS part of the game.")
f.para("The same phone plans the weekend. It holds the costume ideas, the AI pictures, the party address and the money for the pizza. One small glass rectangle runs the whole autumn : sport, money, festivals and friends. The Lucerna's advice ? Enjoy it — and sometimes, look up. The real game is also beautiful.")
f.gloss("to stream, transmitir on-line · a highlight, os melhores momentos · earnings, o balanço (lucros) · a feed, o feed de notícias · a roster, a lista de jogadores.")
f.head("A · CHOOSE · Escolha", 25)
f.ex("B1", "Escolha múltipla", "A", "a rodada tripla de abertura passou na NBC e no Peacock",
     "The opening tripleheader was shown on... A. NBC and Peacock · B. FOX only · C. ESPN only", size=22.5)
f.ex("B1", "Escolha múltipla", "A", "um dos retratos de buscas da manhã de quarta",
     "On Wednesday morning, a top search was... A. lakers roster · B. world series tickets · C. tesla stock", size=22.5)
f.ex("B1", "Escolha múltipla", "B", "47% usam IA para planejar fantasias e enfeites",
     "47% of celebrants use AI to plan... A. their votes · B. costumes and decorations · C. their homework", size=22.5)
f.ex("B1", "Escolha múltipla", "B", "Tesla e Meta divulgam resultados na quarta, após o fechamento",
     "Tesla and Meta report their results... A. Monday morning · B. Wednesday after the close · C. Sunday night", size=22.5)
f.ex("B1", "Escolha múltipla", "C", "antes do balanço, os números dos especialistas são todos diferentes",
     "Before a report, the experts' numbers... A. are all the same · B. are secret · C. differ from expert to expert", size=22.5)
f.head("B · SCREEN WORDS · Da tela", 25)
f.ex("A2", "Completar frases", "stream", "stream = assistir on-line",
     "You can ___ the game live on your phone.", instr="Complete", size=23)
f.ex("B1", "Completar frases", "highlights", "highlights = melhores momentos",
     "No time for the full game ? Watch the ___ : three minutes of the best moments.", instr="Complete", size=23)
f.ex("B1", "Completar frases", "viral", "go viral = viralizar",
     "Her costume photo went ___ : a million people saw it in one day.", instr="Complete", size=23)
f.ex("B1", "Completar frases", "roster", "roster = lista do time",
     "Before the season, fans study the ___ : who plays for the Lakers this year ?", instr="Complete", size=23)
f.ex("B1", "Completar frases", "earnings", "earnings = balanço",
     "Wednesday is ___ day for Tesla and Meta : the companies publish their numbers.", instr="Complete", size=23)
f.ex("A2", "Completar frases", "feed", "feed = o feed de notícias",
     "His ___ is full of game clips and costume photos.", instr="Complete", size=23)
f.head("C · THIS WEEK, LIVE · Presente", 25)
f.expl("Reescreva no presente contínuo: o que está acontecendo esta semana.")
f.ex("B1", "Transformação de frases", "Tesla is reporting its results tonight.", "terceira pessoa: is + -ing",
     "Tesla (report) its results tonight. → ___", instr="Reescreva")
f.ex("B1", "Transformação de frases", "The teams are playing 43 games this week.", "plural: are + -ing",
     "The teams (play) 43 games this week. → ___", instr="Reescreva")
f.ex("B1", "Transformação de frases", "Fans are watching the tripleheader on their phones.", "fans → are watching",
     "Fans (watch) the tripleheader on their phones. → ___", instr="Reescreva")
f.ex("B1", "Transformação de frases", "Milwaukee is preparing for Game 1.", "prepare → is preparing",
     "Milwaukee (prepare) for Game 1. → ___", instr="Reescreva")
f.head("D · TRUE OR FALSE ? · V ou F", 25)
f.ex("B1", "Leitura: V ou F", "True", "no texto: muitos jovens veem primeiro um clipe",
     "1. Many young fans meet a game first as a short clip.", instr="V ou F", size=23)
f.ex("B1", "Leitura: V ou F", "False", "antes da divulgação, ninguém sabe os números",
     "2. Everybody knows Tesla's numbers before Wednesday's report.", instr="V ou F", size=23)
f.ex("B1", "Leitura: V ou F", "False", "as listas vêm do Frightgeist (Google) e das lojas",
     "3. The costume lists come only from shops.", instr="V ou F", size=23)
f.end_report()

# col 3
ix = COLX[3]
v5 = Flow(p, [(ix, CW)], 200, 2540, tag="P5-col3")
v5.box("WORDS OF THE SCREEN · Da tela", [
    ("to stream — transmitir on-line", "serif", False, INK, 21.5, 1.5),
    ("a highlight — os melhores momentos", "serif", False, INK, 21.5, 1.5),
    ("a clip — um vídeo curto", "serif", False, INK, 21.5, 1.5),
    ("a feed — o feed de notícias", "serif", False, INK, 21.5, 1.5),
    ("viral — que viraliza (go viral)", "serif", False, INK, 21.5, 1.5),
    ("a roster — a lista, o elenco", "serif", False, INK, 21.5, 1.5),
    ("earnings — o balanço, os lucros", "serif", False, INK, 21.5, 1.5),
    ("to post — postar, publicar", "serif", False, INK, 21.5, 1.5),
])
v5.box("SAY IT ONLINE · Diga on-line", [
    ("« What a game ! » — Que jogo!", "serif", False, INK, 21.5, 1.45),
    ("« Send me the highlights. » — Me manda os melhores momentos.", "serif", False, INK, 21.5, 1.45),
    ("« This costume wins Halloween. » — Essa fantasia ganhou o Halloween.", "serif", False, INK, 21.5, 1.45),
])
v5.box("THE WORLD GAME AT 4 P.M.", [
    ("On Sunday at 4 p.m. Eastern, American screens turn to Spain : Barcelona vs Real Madrid, on ESPN. In one Wednesday snapshot, it was America's number one search. The world's game needs no translation.", "serif", False, INK, 21.5, 1.45),
    ("Domingo, 16h (leste): o clássico espanhol na ESPN. Na quarta, foi a busca nº 1 dos EUA.", "sans", False, GREY, 20.5, 1.4),
])
v5.box("PLAN YOUR STREAMING WEEK", [
    ("Tue — the NBA tripleheader, on Peacock", "serif", False, INK, 21.5, 1.45),
    ("Wed — Tesla & Meta numbers, after the close", "serif", False, INK, 21.5, 1.45),
    ("Fri — World Series Game 1 · Sat — Game 2", "serif", False, INK, 21.5, 1.45),
    ("Sun — Austin Grand Prix · El Clásico, 4 p.m. ET", "serif", False, INK, 21.5, 1.45),
])
v5.box("NEXT WEEK ON YOUR SCREENS", [
    ("Mon–Tue — the Series moves to Tampa · Sat Oct 31 — Halloween night · Sun Nov 1 — the clocks fall back · Tue Nov 3 — election night. The autumn does not slow down.", "serif", False, INK, 21.5, 1.45),
])
v5.box("THE DEBATE · O debate", [
    ("Is a forty-second clip really « watching the game » ? Or is the full game a thing of the past ? Two sentences, in English, to the newsroom — the best answers appear on page 7 of VOL.2.", "serif", False, INK, 21.5, 1.45),
])
v5.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jeunesse.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("IN DEPTH · Leitura profunda", "The Lucerna", "LEVEL B2 · The 2026 midterms · As eleições de meio de mandato")

a6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], 200, 1420, tag="P6-article")
a6.title("The Midterms : Why America Votes Early", 37)
a6.byline("By The Lucerna newsroom · Reading level : B2")
a6.para("On Tuesday, November 3, Americans vote in the midterm elections — the elections that fall in the middle of a president's term. There is no presidential race this year. Instead, voters choose the whole House of Representatives, part of the Senate, and most state governors. It is a smaller election than 2024, but in Washington, it changes everything.", 24)
a6.para("The stakes fit in one line of numbers : the House today stands at 218 Republicans to 214 Democrats, according to Reuters — a margin of four seats. A handful of districts will decide who controls Congress for the next two years. That is why the advertising never stops : spending on election ads had already reached a record 3.8 billion dollars by October 12, the analytics firm AdImpact reported.", 24)
a6.para("The newest fact of American elections is the calendar. Voting is no longer a day ; it is a season. Nurses, drivers, soldiers and parents often cannot queue for hours on a Tuesday, so states let them vote early, in person, with the same ballot. This year's wave opened on Monday, October 19, in Texas — early voting there runs to October 30 — and in Alaska, Arkansas, Connecticut and Colorado.", 24)
a6.para("Louisiana and Missouri followed on Tuesday, Delaware and Maryland on Thursday, and Michigan and Florida's mandatory period begins on Saturday, October 24. Fifty states, fifty calendars : in the United States, elections are run by the states, not by Washington, and every state keeps its own doors and its own hours.", 24)
a6.para("Early voting changes the campaign, too. Parties no longer aim everything at one Tuesday ; they aim at October. But one rule protects the suspense : early votes are counted under state rules, and the results, as always, arrive on election night. Voting early does not mean knowing early.", 24)
a6.gloss("midterm, eleição de meio de mandato · House, a Câmara · turnout, a participação · incumbent, o titular.")
a6.end_report()

# col 2 rail
r6rail = Flow(p, [(COLX[2], CW)], 200, 1420, tag="P6-rail")
r6rail.box("THE EARLY-VOTING WEEK", [
    ("Mon, Oct 19 — Texas, Alaska, Arkansas, Connecticut and Colorado open", "serif", False, INK, 21.5, 1.48),
    ("Tue, Oct 20 — Louisiana and Missouri follow", "serif", False, INK, 21.5, 1.48),
    ("Thu, Oct 22 — Delaware and Maryland open", "serif", False, INK, 21.5, 1.48),
    ("Sat, Oct 24 — Michigan opens ; Florida's mandatory period begins", "serif", False, INK, 21.5, 1.48),
    ("Fri, Oct 30 — early voting closes in Texas", "serif", False, INK, 21.5, 1.48),
    ("Tue, Nov 3 — ELECTION DAY", "serif", True, INK, 21.5, 1.48),
])
r6rail.box("HOW TO FOLLOW IT · Como seguir", [
    ("Watch three numbers, not three hundred opinions : the turnout (how many vote), the House margin (218–214 today) and the ad money ($3.8 billion and counting). The rest is noise.", "serif", False, INK, 21.5, 1.45),
    ("Para acompanhar a eleição, olhe três números: a participação, a margem na Câmara e o dinheiro de anúncios. O resto é ruído.", "sans", False, GREY, 20.5, 1.4),
])
r6rail.end_report()

# col 3 sidebar
ix = COLX[3]
image(p, "capitol.jpg", ix, 200, CW, 186)
cy6 = caption(p, ix, 386, CW, "The Capitol in Washington : control of Congress is the prize on November 3.",
              "United States Capitol — public domain")
s6 = Flow(p, [(ix, CW)], int(cy6) + 16, 1420, tag="P6-side")
s6.box("ELECTION WORDS · Da eleição", [
    ("a midterm — a eleição de meio de mandato", "serif", False, INK, 21.5, 1.5),
    ("an incumbent — quem ocupa o cargo", "serif", False, INK, 21.5, 1.5),
    ("a margin — a margem (de votos/cadeiras)", "serif", False, INK, 21.5, 1.5),
    ("turnout — a participação dos eleitores", "serif", False, INK, 21.5, 1.5),
    ("a campaign — a campanha", "serif", False, INK, 21.5, 1.5),
    ("a district — o distrito eleitoral", "serif", False, INK, 21.5, 1.5),
])
s6.box("HEADLINE LANGUAGE · Manchete", [
    ("« Early voting opens » — começa a votação antecipada", "serif", False, INK, 21, 1.45),
    ("« voters head to the polls » — eleitores vão às urnas", "serif", False, INK, 21, 1.45),
    ("« too close to call » — perto demais para anunciar um vencedor", "serif", False, INK, 21, 1.45),
])
s6.end_report()

# ---- practice chart (span cols 0-1) ----
chy = 1456
p.hline(MX, RIGHT, chy - 12, GOLD, 2)
chx, chw = COLX[0], 2 * CW + GUT
p.text(chx, chy + 28, "WHY DO VOTERS VOTE EARLY ? · Gráfico de prática", 26, "sans", True, OLIVE)
p.text(chx, chy + 58, "PRACTICE DATA — simplified and invented for this exercise ; not a real survey. Dados de prática fictícios.", 18.5, "sans", False, BRICK)
p.rect(chx, chy + 76, chw, 356, fill=BOX, stroke=LINE, sw=1.4)
rows = [
    ("To avoid the long lines", 34, OLIVE),
    ("I work on Election Day", 27, GOLD),
    ("I want it done early", 23, OLIVE),
    ("I will travel on Nov 3", 16, GOLD),
]
byy = chy + 116
for lab, val, col in rows:
    p.text(chx + 24, byy + 24, lab, 22, "serif", True, INK)
    p.rect(chx + 24, byy + 36, val * 11, 24, fill=col)
    p.text(chx + 34 + val * 11, byy + 56, f"{val}%", 21, "sans", True, BRICK)
    byy += 82
p.text(chx + 24, byy + 8, "Four answers, 100 voters. Quatro respostas, 100 eleitores no total.", 19, "sans", False, GREY)

# ---- chart questions (cols 0-1) ----
q6 = Flow(p, [(COLX[0], CW), (COLX[1], CW)], chy + 470, 2540, tag="P6-chart-ex")
q6.head("READING THE CHART · O gráfico", 24)
q6.ex("B2", "Leitura de gráfico", "C", "o maior motivo é evitar as filas: 34%",
     "The biggest reason is... A. travel · B. work · C. avoiding long lines", size=22)
q6.ex("B2", "Leitura de gráfico", "27", "trabalham no dia da eleição: 27 pessoas",
     "Out of 100 voters, how many work on Election Day ?", size=22)
q6.ex("B1", "Leitura de gráfico", "61%", "34 + 27 = 61",
     "The top two reasons together make ___ of the voters.", size=22)
q6.ex("B2", "Leitura de gráfico", "False", "27 + 16 = 43, menos da metade",
     "True or false : more than half vote early because of work or travel.", size=22)
q6.ex("B1", "Leitura de gráfico", "18 points", "34 − 16 = 18 pontos percentuais",
     "The difference between « lines » and « travel » is ___.", size=22)
q6.ex("B1", "Leitura de gráfico", "100%", "as quatro respostas somam 100%",
     "All four answers together make ___ of the voters.", size=22)
q6.box("KEY SENTENCE · Frase-chave", [
    ("« Voting is no longer a day ; it is a season. »", "serif", False, INK, 21.5, 1.45),
    ("Votar não é mais um dia; é uma estação. — A frase central da leitura profunda desta página.", "sans", False, GREY, 20.5, 1.4),
])
q6.end_report()

# ---- right exercises (cols 2-3) ----
r6 = Flow(p, [(COLX[2], CW), (COLX[3], CW)], chy + 14, 2540, tag="P6-ex")
r6.head("READING · Leitura", 24)
r6.ex("B2", "Escolha múltipla", "B", "as eleições de meio de mandato decidem o controle do Congresso",
     "The midterms decide... A. the president · B. control of Congress · C. the Supreme Court", size=22)
r6.ex("B2", "Escolha múltipla", "B", "nos EUA, as eleições são organizadas pelos estados",
     "Elections in the US are run by... A. the White House · B. the states · C. the parties", size=22)
r6.ex("B2", "Escolha múltipla", "B", "os US$ 3,8 bilhões são os gastos com anúncios até 12 de outubro",
     "The $3.8 billion is... A. the cost of voting machines · B. ad spending by Oct 12 · C. the price of ballots", size=22)
r6.ex("B2", "Escolha múltipla", "C", "o período obrigatório da Flórida começa no sábado, 24 de outubro",
     "Florida's mandatory early voting starts... A. Oct 19 · B. Oct 22 · C. Oct 24", size=22)
r6.head("COMPARATIVES · Comparativos", 24)
r6.ex("B2", "Completar frases", "more convenient", "convenient usa more",
     "Early voting is ___ (convenient) than voting on one day only.", instr="Complete", size=22)
r6.ex("B1", "Completar frases", "highest", "record = o maior de todos os tempos",
     "Ad spending this year is the ___ (high) ever.", instr="Complete", size=22)
r6.ex("B1", "Completar frases", "earlier", "o Texas começa em 19 de outubro, antes da Flórida (24)",
     "Texas starts ___ (early) than Florida.", instr="Complete", size=22)
r6.ex("B2", "Completar frases", "smaller", "218 − 214 = 4 < 10",
     "The House margin (218–214) is ___ (small) than ten seats.", instr="Complete", size=22)
r6.head("ELECTION WORDS · Da eleição", 24)
r6.ex("B2", "Completar frases", "incumbent", "incumbent = quem ocupa o cargo",
     "The ___ is the person who holds the job now and wants to keep it.", instr="Complete", size=22)
r6.ex("B2", "Completar frases", "margin", "margin = margem",
     "218 to 214 is a ___ of four seats.", instr="Complete", size=22)
r6.ex("B2", "Completar frases", "turnout", "turnout = participação",
     "A high ___ means many people vote.", instr="Complete", size=22)
r6.ex("B2", "Completar frases", "campaign", "campaign = campanha",
     "A ___ is the long season of work before an election.", instr="Complete", size=22)
r6.box("SAY IT LIKE A HEADLINE", [
    ("« Early voters ___ to the polls in Texas. » (head)", "serif", False, INK, 21, 1.45),
    ("« The race is too ___ to call. » (close)", "serif", False, INK, 21, 1.45),
    ("« Turnout is ___ this year. » (up)", "serif", False, INK, 21, 1.45),
    ("Três manchetes de jornal: complete e diga em voz alta — as respostas estão no uso diário.", "sans", False, GREY, 20.5, 1.4),
])
r6.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
