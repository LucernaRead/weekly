# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("YOUTH　Jeugd", "The Lucerna", "LEVEL B1　Election night at home　Verkiezingsnacht")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P5-main")
f.title("Election Night at Home : Maps, Phones and Pizza", 32)
f.byline("By The Lucerna newsroom　Reading level : B1")
f.para("Last issue, we asked you a question : what do Americans read, watch and eat while they wait for the results ? On Tuesday night, November 3, here is the answer — from living rooms across the country.")
f.para("First, they watch the maps. On television, the map of the United States slowly changes colour, state by state, as results come in. Every channel has its own map, its own experts, and its own way of saying the same sentence : « Too close to call. » That means : we do not know yet.")
f.para("Second, they eat. Election night is pizza night in many homes — easy food, no cooking, hands free for the phone. Popcorn, chips and soda join the pizza on the table. Nobody cooks a big dinner on a night when the news never stops.")
f.para("Third, they read — on their phones. Friends send messages : « Did you see Ohio ? » « Florida is close ! » « Go to bed, we will know tomorrow. » The second screen is part of the night : the television for the map, the phone for the friends.")
f.para("And the children ? They watch too, from the sofa, and they ask the best questions : « Why is that state red ? » « Why does it take so long ? » « Can we stay up until the end ? » The answer to the last question is usually : no. The results will still be there in the morning.")
f.box("TOO CLOSE TO CALL　Onbeslist", [
    ("When a race is very close, channels do not call a winner. They wait. « Too close to call » is the most honest sentence on election night — and the most repeated.", "serif", False, INK, 21.5, 1.4),
])
f.para("If you want to practise election-night English, try this : watch ten minutes of results coverage in English, and write down five sentences you hear. « Too close to call » will certainly be one of them. The other four are your homework.")
f.gloss("a map = (verkiezings)kaart · too close to call = nog niet te beslissen · a second screen = tweede scherm (telefoon).")
f.head("A　COMPREHENSION", 25)
f.bridge("Lees het artikel op pagina 5 en kies het juiste antwoord.")
f.ex("B1", "Meerkeuze", "B", "De kaart kleurt mee met de resultaten, staat per staat",
     "On election night, the TV map changes... A. every hour · B. state by state · C. only at midnight", size=22)
f.ex("B1", "Meerkeuze", "A", "too close to call = we weten het nog niet",
     "« Too close to call » means... A. we do not know yet · B. the winner is clear · C. the night is over", size=22)
f.ex("B1", "Meerkeuze", "C", "Op verkiezingsnacht eet men vaak pizza",
     "Election night is often... A. cooking night · B. reading night · C. pizza night", size=22)
f.ex("B1", "Meerkeuze", "B", "Het tweede scherm is de telefoon",
     "The second screen is... A. a second TV · B. the phone · C. a computer game", size=22)
f.ex("B1", "Meerkeuze", "A", "Kinderen vragen waarom het zo lang duurt",
     "Children ask... A. why it takes so long · B. where pizza comes from · C. who won in Ohio", size=22)
f.ex("B1", "Meerkeuze", "C", "De resultaten zijn er 's ochtends nog",
     "If you go to bed, the results... A. disappear · B. change · C. will still be there in the morning", size=22)
f.head("B　SENTENCES", 25)
f.bridge("Vul de zinnen aan met de gegeven woorden.")
f.ex("B1", "Zinnen aanvullen", "close", "close = dichtbij, spannend",
     "Florida is very ___ tonight.", instr="Vul in")
f.ex("B1", "Zinnen aanvullen", "still", "still = nog steeds",
     "The results will ___ be there in the morning.", instr="Vul in")
f.ex("A2", "Zinnen aanvullen", "map", "Zoals in het artikel op pagina 5, enkelvoud",
     "Every channel has its own ___.", instr="Vul in")
f.ex("A2", "Zinnen aanvullen", "phone", "Zoals in het artikel op pagina 5, enkelvoud",
     "Hands free for the ___.", instr="Vul in")
f.head("C　THE WORDS", 25)
f.match_set("B1", "Woorden combineren",
            ["a map", "a race", "a result", "to call"],
            ["to announce the winner of an election",
             "the final numbers of a vote",
             "a picture of the states, coloured by results",
             "one contest for one office"],
            ["c", "d", "b", "a"],
            ["map = verkiezingskaart c", "race = verkiezingsstrijd d", "result = uitslag b", "call = winnaar bekendmaken a"],
            instr="Combineer")
f.head("D　PRESENT CONTINUOUS", 25)
f.bridge("Herschrijf met de continuous-vorm (wat er nu gebeurt).")
f.ex("B1", "Zinnen omvormen", "The map is changing colour now.", "change → is changing",
     "The map (change) colour now. → ___", instr="Herschrijf")
f.ex("B1", "Zinnen omvormen", "Friends are sending messages tonight.", "send → are sending",
     "Friends (send) messages tonight. → ___", instr="Herschrijf")
f.ex("B1", "Zinnen omvormen", "We are watching the results at home.", "watch → are watching",
     "We (watch) the results at home. → ___", instr="Herschrijf")
f.ex("B1", "Zinnen omvormen", "She is waiting for Ohio's result.", "wait → is waiting",
     "She (wait) for Ohio's result. → ___", instr="Herschrijf")
f.end_report()

# col 3: side flow
ix = COLX[3]
v5 = Flow(p, [(ix, CW)], 200, 2560, tag="P5-col3")
v5.box("FIVE SENTENCES　Vijf zinnen", [
    ("Watch ten minutes of results coverage in English. Write down five sentences you hear. « Too close to call » will be one of them.", "serif", False, INK, 21.5, 1.42),
])
v5.head("ELECTION-NIGHT PHRASES", 25)
v5.para("« Too close to call. » « The polls have closed. » « We will know tomorrow. » « Go to bed ! » — four sentences for one night. Learn them, and election night in English is yours.", 22)
v5.para("« The polls have closed » means : voting is finished in that state. After that sentence, the counting begins — and the waiting too.", 22)
v5.bridge("Stemmen gesloten | The polls have closed = in die staat is het stemmen voorbij, het tellen begint.")
v5.head("SATURDAY SPORT", 25)
v5.para("After Tuesday, the weekend keeps going : MLS fixtures on Saturday, November 7, including Charlotte against Inter Miami and Atlanta against the New York Red Bulls. The weekend warms up for Sunday's games.", 22)
v5.end_report()
p.foot(5)
p.save(f"{OUT}/p5-jeunesse.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("DEEP READ　Verdieping", "The Lucerna", "LEVEL B2　How America votes　Hoe Amerika stemt")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P6-main")
f.title("How America Votes : One Country, Fifty Elections", 32)
f.byline("By The Lucerna newsroom　Reading level : B2")
f.para("There is no single American election. There are fifty — one in every state — run by the states themselves, under rules that differ from state to state. That is why Election Day looks different in Texas, in Florida and in Ohio, and why the results arrive at different speeds.")
f.para("The House of Representatives has 435 members, each serving two years. Every midterm, all 435 seats are on the ballot. The Senate has 100 members, each serving six years, and only about a third of them face the voters in any one election. Governors, who lead the states, are also on the ballot in many states.")
f.para("Why does a midterm matter ? Because the party that holds the House and the Senate can shape the laws of the next two years. A midterm can change who controls Congress — or confirm the voters' choice of two years before. Nothing is decided in advance ; that is the point of the vote.")
f.para("How does a voter vote ? First, register — in most states, before Election Day. Then, choose : vote early in person, vote by mail where the state allows it, or vote in person on Tuesday. At the voting place, show your ID where the state asks for it, mark your ballot in private, and put it in the box. The sticker — « I VOTED » — is optional, but almost everybody takes one.")
f.para("And after Tuesday ? Counting continues. Mail ballots take time to open and check. Close races take longer. Channels call a race only when the maths is clear — and when it is not clear, they say the honest sentence : too close to call. Patience is part of the system, not a failure of it.")
f.box("A PRACTICE BALLOT　Stembiljet", [
    ("For Governor : ☐ Candidate A · ☐ Candidate B. For the House : ☐ Candidate C · ☐ Candidate D. Names are codes here — this ballot teaches how to mark, not whom to choose.", "serif", False, INK, 21.5, 1.4),
])
f.para("A note on numbers in this issue : this paper prints no poll figures and no predictions. Polls change, and a learner's paper should teach the system, not guess the result. On Wednesday morning, the results will speak for themselves — and next week's issue will report them.")
f.gloss("to register = je registreren (als kiezer) · a governor = gouverneur · to shape laws = wetten vormgeven · patience = geduld.")
# practice chart
f.head("READ THE CHART　Grafiek", 25)
f.para("Why do voters vote early ? A practice survey of 100 early voters gives four reasons. The chart is teaching data, not a real poll.", 22)
# chart bars drawn via flow-adjacent page calls is complex; use text bars in flow
for lab, pct, bw in [("No lines", 38, 280), ("Work on Tuesday", 29, 214), ("Travel plans", 21, 155), ("Habit", 12, 88)]:
    f.para(f"{lab} : {pct}%", 22, "serif", True, OLIVE, 1.3, 2)
f.head("A　CHART READING", 25)
f.bridge("Lees de oefengrafiek hierboven en kies het juiste antwoord.")
f.ex("B2", "Grafiek lezen", "B", "38% koos « geen rijen »",
     "The biggest reason is... A. Habit · B. No lines (38%) · C. Travel plans", size=22)
f.ex("B2", "Grafiek lezen", "C", "Werk als reden: 29%",
     "« Work on Tuesday » is... A. 38% · B. 21% · C. 29%", size=22)
f.ex("B2", "Grafiek lezen", "A", "De vier samen: 100%",
     "38 + 29 + 21 + 12 = ... A. 100 · B. 99 · C. 101", size=22)
f.ex("B2", "Grafiek lezen", "B", "Gewoonte het minst: 12%",
     "The smallest reason is... A. Travel plans · B. Habit (12%) · C. No lines", size=22)
f.ex("B2", "Grafiek lezen", "A", "Geen rijen 17 punten meer dan reizen",
     "No lines beats Travel plans by... A. 17 points · B. 9 points · C. 26 points", size=22)
f.ex("B2", "Grafiek lezen", "C", "De grafiek is oefenmateriaal, geen echte peiling",
     "This chart is... A. a real poll · B. a prediction · C. practice data", size=22)
f.head("B　COMPREHENSION", 25)
f.bridge("Lees het artikel op pagina 6 en kies het juiste antwoord.")
f.ex("B2", "Meerkeuze", "B", "De staten organiseren zelf de verkiezingen",
     "American elections are run by... A. one office · B. the states · C. the TV channels", size=22)
f.ex("B2", "Meerkeuze", "A", "Leden van het Huis dienen twee jaar",
     "House members serve... A. two years · B. four years · C. six years", size=22)
f.ex("B2", "Meerkeuze", "C", "Senatoren dienen zes jaar, telkens ongeveer een derde verkiesbaar",
     "Senators serve... A. two years · B. four years · C. six years", size=22)
f.ex("B2", "Meerkeuze", "B", "Poststemmen tellen kost tijd",
     "Counting takes time because... A. TV is slow · B. mail ballots must be opened and checked · C. voters are late", size=22)
f.ex("B2", "Meerkeuze", "A", "Dit nummer drukt geen peilingen of voorspellingen",
     "This issue prints... A. no polls or predictions · B. one poll · C. three predictions", size=22)
f.ex("B2", "Meerkeuze", "C", "Geduld is een deel van het systeem",
     "Waiting for results is... A. a failure · B. unusual · C. part of the system", size=22)
f.head("C　SENTENCES", 25)
f.bridge("Vul de zinnen aan met de gegeven woorden.")
f.ex("B2", "Zinnen aanvullen", "shape", "shape = beïnvloeden, vormgeven",
     "A midterm can ___ the laws of two years.", instr="Vul in")
f.ex("B2", "Zinnen aanvullen", "register", "register = je registreren",
     "First, you must ___ before Election Day.", instr="Vul in")
f.ex("B2", "Zinnen aanvullen", "patience", "patience = geduld",
     "___ is part of the system.", instr="Vul in")
f.ex("B1", "Zinnen aanvullen", "optional", "optional = optioneel",
     "The « I VOTED » sticker is ___ , but everybody takes one.", instr="Vul in")
f.ex("B1", "Zinnen aanvullen", "differs", "differ → differs in de 3e persoon enkelvoud",
     "The rule ___ from state to state.", instr="Vul in")
f.ex("B1", "Zinnen aanvullen", "private", "private = privé",
     "Mark your ballot in ___.", instr="Vul in")
f.end_report()

# col 3: image + terms box
ix = COLX[3]
image(p, "capitol.jpg", ix, 200, CW, 300)
cy6 = caption(p, ix, 500, CW, "The United States Capitol, Washington : the House and the Senate meet here. On Tuesday, voters decide who sits inside.",
              "Public domain, via Wikimedia Commons")
v6 = Flow(p, [(ix, CW)], int(cy6) + 18, 2560, tag="P6-col3")
v6.box("HOW LONG ?　Hoe lang?", [
    ("House : 2 years, all 435 seats each midterm. Senate : 6 years, about a third each election. President : 4 years. Governor : usually 4 years.", "serif", False, INK, 21.5, 1.42),
])
v6.head("FIFTY ELECTIONS", 25)
v6.para("One country, fifty systems : that is why American election night is a map, not a single number. Learn the map, and the night makes sense.", 22)
v6.bridge("Eén kaart | Vijftig staten, vijftig regels — daarom kijk je op verkiezingsnacht naar een kaart, niet naar één getal.")
v6.end_report()
p.foot(6)
p.save(f"{OUT}/p6-politique.svg")
print("P6 saved, exercises so far:", len(REG))
