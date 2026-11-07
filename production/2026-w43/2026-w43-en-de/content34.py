# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-en-de/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE · Kultur", "The Lucerna", "A2 → B1 · Halloween in America · Halloween in Amerika")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P3-main")
f.title("Halloween in America : a $13.5 Billion Night of Candy", 37)
f.byline("By The Lucerna newsroom · Reading level : A2 → B1")
f.para("On Saturday, October 31, America will put on its costumes. Halloween is not an official holiday — nobody gets the day off — but it is one of the biggest nights of the American year. This year, the National Retail Federation (NRF) projects record spending of 13.5 billion dollars, up 3.82% from 2025. That is about $115.14 for every person who celebrates.")
f.para("Where does the money go ? Costumes come first : $4.4 billion. Decorations are second, at $4.3 billion — gardens full of skeletons, lights and giant spiders. Candy takes $4.1 billion, and almost everybody buys it : 96% of celebrants plan to buy sweets for the big night.")
f.para("How does trick-or-treating work ? In the early evening, children in costumes walk from door to door in their neighbourhood. They ring the bell and shout : « Trick or treat ! » — a joke threat, always answered with candy. One rule matters : a light on the porch means « welcome, knock here ». A dark house means « please, not this year » — and children respect it.")
f.para("The pumpkin is the symbol of the season. In October, families drive to pumpkin patches — fields where you choose your own pumpkin — and carve faces into them at home. A candle inside makes a jack-o'-lantern, and on October 31, thousands of orange faces glow on American porches.")
f.para("What will America wear this year ? Google published its Frightgeist costume list on October 14, and the shop Spirit Halloween published its own : characters from KPop Demon Hunters and Toy Story 5, superheroes, and Greek gods. One number tells the story of 2026 : 47% of celebrants now use AI tools to plan a costume or a decoration. The robot helps you become a ghost.")
f.para("Halloween was a national festival long before it was a shopping season. In the early 1900s, when telephones were still rare, Americans sent Halloween postcards — more than 3,000 designs were printed. The card on this page is from 1912. The greetings travelled slowly, by mail, and arrived like little paper ghosts.")
f.para("This year, the calendar is kind : Halloween falls on a Saturday. No school the next morning, no work for most parents — the party can begin in the afternoon and the last jack-o'-lantern can burn late. Shops know it, too : the last full shopping week of the season is this one, and the costume shelves empty fast.")
f.para("One object waits by every door : the candy bowl. Families fill it in the afternoon — chocolate, sweets, sometimes small toys — and children empty it, street by street, all evening. Economists study the $13.5 billion. Children study something simpler : which house gives the biggest chocolate ?")
f.box("SAY IT ON THE NIGHT · Sag es so", [
    ("« Trick or treat ! » — „Süßes oder Saures!“ (Scherzdrohung — es gibt immer Süßigkeiten)", "serif", False, INK, 21.5, 1.42),
    ("« Happy Halloween ! » — Frohes Halloween! · « Thank you ! » — Danke! (unbedingt sagen, wenn es etwas gibt)", "serif", False, INK, 21.5, 1.42),
    ("« What are you dressed as ? » — Als was bist du verkleidet?", "serif", False, INK, 21.5, 1.42),
])
f.gloss("to celebrate = feiern · a porch = Veranda, Türstufen · to carve = schnitzen · a decoration = Schmuck, Deko · a survey = eine Umfrage (die NRF befragte 7.889 Personen).")
f.head("A · WAHR ODER FALSCH ?", 25)
f.bridge("Lies Seite 3 und entscheide: richtig oder falsch.")
f.ex("A2", "Richtig/Falsch", "False", "Halloween ist am Samstag (31. Oktober)",
     "1. Halloween is on a Friday this year.", instr="Richtig oder falsch?", size=23)
f.ex("A2", "Richtig/Falsch", "True", "NRF-Prognose: 13,5 Milliarden Dollar",
     "2. Americans will spend about $13.5 billion on Halloween.", instr="Richtig oder falsch?", size=23)
f.ex("B1", "Richtig/Falsch", "False", "Größter Posten: Kostüme (4,4 Mrd.), nicht Süßes",
     "3. Candy is the biggest part of the spending.", instr="Richtig oder falsch?", size=23)
f.ex("A2", "Richtig/Falsch", "True", "47 % nutzen KI für Ideen",
     "4. Almost half of celebrants use AI tools for costume ideas.", instr="Richtig oder falsch?", size=23)
f.ex("A2", "Richtig/Falsch", "False", "Kein Licht an der Tür = bitte nicht stören",
     "5. A house with no light on the porch is asking for visitors.", instr="Richtig oder falsch?", size=23)
f.head("B · FESTWÖRTER", 25)
f.ex("A2", "Satzergänzung", "costume", "costume = Kostüm, Verkleidung",
     "Children wear a ___ and go from door to door.", instr="Ergänze", size=23)
f.ex("A2", "Satzergänzung", "carve", "carve a pumpkin = einen Kürbis schnitzen",
     "You ___ a pumpkin to make a jack-o'-lantern.", instr="Ergänze", size=23)
f.ex("A2", "Satzergänzung", "porch", "porch = Veranda",
     "Families leave a light on the ___ to welcome children.", instr="Ergänze", size=23)
f.ex("A2", "Satzergänzung", "candy", "96 % kaufen Süßigkeiten",
     "Ninety-six percent of celebrants buy ___.", instr="Ergänze", size=23)
f.ex("A2", "Satzergänzung", "patch", "pumpkin patch = Kürbisfeld",
     "In October, families visit a pumpkin ___ to choose a pumpkin.", instr="Ergänze", size=23)
f.head("C · CHOOSE · Auswahl", 25)
f.ex("B1", "Multiple Choice", "B", "13,5 Mrd. = Prognose für dieses Jahr",
     "The $13.5 billion is... A. last year's total · B. this year's projection · C. candy money only", size=22.5)
f.ex("B1", "Multiple Choice", "A", "Googles Liste heißt Frightgeist",
     "Google's costume list is called... A. Frightgeist · B. Spiritgeist · C. Trendlist", size=22.5)
f.ex("B1", "Multiple Choice", "B", "Im Trend: griechische Götter",
     "This year's costumes include... A. Roman kings · B. Greek gods · C. astronauts only", size=22.5)
f.ex("B1", "Multiple Choice", "B", "Anfang des 20. Jh.: Grüße per Postkarte",
     "In the early 1900s, Halloween greetings travelled by... A. telephone · B. postcard · C. radio", size=22.5)
f.head("D · SENTENCES · Umformen", 25)
f.ex("A2", "Umformung", "Children go door to door on October 31.", "Present Simple für Gewohnheiten",
     "Children (go) door to door on October 31. → ___", instr="Schreibe um")
f.ex("B1", "Umformung", "She buys a Greek god costume.", "3. Person Singular: buys",
     "She (buy) a Greek god costume. → ___", instr="Schreibe um")
f.ex("A2", "Umformung", "He does not like horror films.", "Verneinung, 3. Person: does not",
     "He (not / like) horror films. → ___", instr="Schreibe um")
f.ex("B1", "Satzergänzung", "will rain", "I think → will für Vermutungen",
     "I think it ___ (rain) on Halloween night.", instr="Ergänze", size=23)
f.end_report()

# col 3
ix = COLX[3]
image(p, "halloween1912.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "« A Halloween Wish », 1912 : in the age of postcards, Halloween greetings travelled by mail — slowly, like little paper ghosts.",
              "Halloween postcard, 1912 — public domain")
v3 = Flow(p, [(ix, CW)], int(cy3) + 18, 2540, tag="P3-col3")
v3.box("FESTIVAL WORDS · Wortliste", [
    ("trick or treat — Süßes oder Saures", "serif", False, INK, 21.5, 1.5),
    ("a costume — ein Kostüm", "serif", False, INK, 21.5, 1.5),
    ("a jack-o'-lantern — Kürbislaterne", "serif", False, INK, 21.5, 1.5),
    ("a porch — Veranda, Türstufen", "serif", False, INK, 21.5, 1.5),
    ("to carve — schnitzen", "serif", False, INK, 21.5, 1.5),
    ("a decoration — Deko, Schmuck", "serif", False, INK, 21.5, 1.5),
    ("spooky — gruselig (lustig gemeint)", "serif", False, INK, 21.5, 1.5),
    ("a patch — ein Stück Land (pumpkin patch = Kürbisfeld)", "serif", False, INK, 21.5, 1.5),
])
v3.box("DATES TO REMEMBER · Termine", [
    ("Oct 23 — Red Ribbon Week begins", "sans", True, BRICK, 20, 1.4),
    ("Oct 24 — Make a Difference Day · Drug Take Back Day, 10 a.m.–2 p.m.", "serif", False, INK, 20.5, 1.4),
    ("Oct 31 — Halloween (Saturday)", "sans", True, BRICK, 20, 1.4),
    ("Nov 1 — clocks fall back · Nov 3 — Election Day", "serif", False, INK, 20.5, 1.4),
])
v3.box("THE SEASON IN NUMBERS", [
    ("3,000+ — Halloween postcard designs printed in the early 1900s", "serif", False, INK, 21, 1.45),
    ("96% — of celebrants buy candy · 47% — now use AI for ideas", "serif", False, INK, 21, 1.45),
    ("$115.14 — projected spending per person (NRF)", "serif", False, INK, 21, 1.45),
])
v3.head("FUN, OR TOO MUCH ?", 23)
v3.para("Halloween now costs America more than ever — and the robots help us dress up. Is it still a festival, or is it a shopping week with ghosts ? Write to us in English, two or three sentences : your letter may appear on page 7 of VOL.2.", 21.5)
v3.bridge("Halloween wird immer teurer, und die KI hilft beim Kostüm: noch ein Fest — oder eine Einkaufswoche mit Geistern? Schreib uns (Leserecke auf Seite 7).")
v3.end_report()
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · Sport", "The Lucerna", "LEVEL B1 · NBA · World Series · Austin F1")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P4-main")
f.title("The Biggest Sports Week of the Autumn", 37)
f.byline("By The Lucerna newsroom · Reading level : B1")
f.head("TIP-OFF TUESDAY", 26)
f.para("The NBA is back. On Tuesday, October 20, the 2026–27 season opened with something new : a tripleheader — three big games in one night — on NBC and its streaming service Peacock. Boston played at Detroit, Oklahoma City at San Antonio, and in New York, the champions received their rings.")
f.para("Before the game at Madison Square Garden, the New York Knicks raised their championship banner — the club's first since 1973. Then the Philadelphia 76ers spoiled the party. Philadelphia won 106–100, with 28 points from Tyrese Maxey. LeBron James, now a 76er, began a record 24th NBA season. The season continues all week : 43 games from Tuesday to Sunday, including the Lakers against the Warriors on Wednesday.")
f.head("A FIRST-TIME CHAMPION", 26)
f.para("Baseball offers the week's most beautiful storyline. In the National League final, Milwaukee swept the Los Angeles Dodgers — the champions of the last two years are out. It is the Brewers' first World Series since 1982. In the American League, Tampa Bay beat Cleveland in Game 6 on Monday night.")
f.para("So the World Series is Milwaukee against Tampa Bay. Game 1 is Friday, October 23, in Milwaukee (8 p.m. Eastern, on FOX), and Game 2 follows on Saturday. Here is the magic number : zero. Neither club has ever won the World Series — so for the first time in years, a first-time champion is guaranteed.")
f.head("SPEED IN AUSTIN", 26)
f.para("On Sunday, the week ends at full speed : the United States Grand Prix at the Circuit of The Americas in Austin, Texas. Practice is on Friday, qualifying on Saturday, and the race on Sunday afternoon. The weekend is also a music festival : Maroon 5 on Friday, Post Malone on Saturday, Alesso on Sunday. A special « Grand PrixView » day opens the circuit to fans on Thursday.")
f.para("One more name to watch : Victor Wembanyama, the French star of San Antonio, meets Oklahoma City in the third game of the tripleheader. In France, they will watch at breakfast time ; in Texas, it is prime time.")
f.head("THE FOOTBALL WEEKEND", 26)
f.para("And football ? It never stops. Week 7 of the NFL season brings the Patriots at the Bears on Thursday night, then, on Sunday, the Packers at the Lions and the Chiefs at the Seahawks in the night game. College football fills Saturday : LSU at Auburn, Texas A&M at Alabama, Ole Miss at Texas, Indiana at Michigan.")
f.head("AND AT 4 P.M. ON SUNDAY...", 26)
f.para("...the world game joins the party. Barcelona play Real Madrid in El Clásico on Sunday — 4 p.m. Eastern on ESPN in the United States. On Wednesday morning, « barca vs real madrid » was the number one trending search in the US in one snapshot.")
f.box("THE WEEK'S FIXTURES · Spielplan", [
    ("Tue — NBA tip-off : 76ers at Knicks · Thunder at Spurs", "serif", False, INK, 21, 1.42),
    ("Wed — Lakers vs Warriors · Thu — Patriots at Bears", "serif", False, INK, 21, 1.42),
    ("Fri — World Series Game 1, 8 p.m. ET · Sat — Game 2", "serif", False, INK, 21, 1.42),
    ("Sun — Austin Grand Prix · El Clásico, 4 p.m. ET", "serif", False, INK, 21, 1.42),
])
f.gloss("a banner = Banner, Meisterfahne · to sweep = alle Spiele einer Serie gewinnen · the defending champion = der Titelverteidiger · qualifying = die Qualifikation · a storyline = der rote Faden.")
f.head("A · READING · Leseauswahl", 25)
f.ex("B1", "Multiple Choice", "A", "Letztes Knicks-Banner: 1973",
     "The Knicks' banner was their first since... A. 1973 · B. 1982 · C. 2003", size=22.5)
f.ex("B1", "Multiple Choice", "A", "106–100 = 6 Punkte Abstand",
     "On opening night, Philadelphia won... A. by 6 points · B. by 16 points · C. after extra time", size=22.5)
f.ex("B1", "Multiple Choice", "B", "Brewers zuletzt 1982 in der World Series",
     "Milwaukee's last World Series before this year was in... A. 1973 · B. 1982 · C. 2020", size=22.5)
f.ex("B1", "Multiple Choice", "C", "F1-Rennen am Sonntag",
     "The Grand Prix race day is... A. Friday · B. Saturday · C. Sunday", size=22.5)
f.ex("B1", "Multiple Choice", "B", "Laut Quelle Week 7 (nicht Week 8)",
     "The NFL games this week are in... A. Week 6 · B. Week 7 · C. Week 8", size=22.5)
f.head("B · SPORTS WORDS · Zuordnung", 25)
f.match_set("B1", "Zuordnung",
            ["tip-off", "a sweep", "the defending champion", "a banner"],
            ["the team that won last time, playing to keep the title",
             "winning every game in a series",
             "a flag in the arena that remembers a championship",
             "the start of a basketball game"],
            ["d", "b", "a", "c"],
            ["tip-off = Spielbeginn (Basketball) d", "sweep = jede Partie der Serie gewinnen b", "defending champion = Titelverteidiger a", "banner = Fahne für den Titel c"],
            instr="Ordne zu")
f.head("C · COMPARATIVES · Vergleiche", 25)
f.ex("B1", "Satzergänzung", "older", "Die World Series ist älter als die NBA",
     "The World Series is ___ (old) than the NBA.", instr="Ergänze", size=22.5)
f.ex("B1", "Satzergänzung", "hotter", "hot → hotter (Konsonant wird verdoppelt)",
     "Austin in October is ___ (hot) than Milwaukee.", instr="Ergänze", size=22.5)
f.ex("B1", "Satzergänzung", "busiest", "Superlativ: the busiest",
     "This is the ___ (busy) sports week of the autumn.", instr="Ergänze", size=22.5)
f.ex("B1", "Satzergänzung", "more", "Maxey 28 Punkte > Brunson 21",
     "Maxey scored ___ points than Brunson on Tuesday. (28 to 21)", instr="Ergänze", size=22.5)
f.head("D · VERB FORMS · Vergangenheit", 25)
f.ex("B1", "Umformung", "The 76ers won 106–100.", "win → won (unregelmäßig)",
     "The 76ers (win) 106–100 on Tuesday. → ___", instr="Schreibe um", size=23)
f.ex("B1", "Umformung", "The Knicks raised their banner.", "raise → raised (regelmäßig)",
     "The Knicks (raise) their banner. → ___", instr="Schreibe um", size=23)
f.ex("B1", "Umformung", "Milwaukee swept the Dodgers.", "sweep → swept (unregelmäßig)",
     "Milwaukee (sweep) the Dodgers. → ___", instr="Schreibe um", size=23)
f.ex("B1", "Umformung", "Tampa Bay beat Cleveland on Monday.", "beat → beat (unregelmäßig)",
     "Tampa Bay (beat) Cleveland on Monday. → ___", instr="Schreibe um", size=23)
f.ex("B1", "Umformung", "Fans watched three games on Tuesday night.", "watch → watched (regelmäßig)",
     "Fans (watch) three games on Tuesday night. → ___", instr="Schreibe um", size=23)
f.end_report()

# col 3
ix = COLX[3]
v4 = Flow(p, [(ix, CW)], 200, 2540, tag="P4-col3")
v4.box("THE KING'S NEW TEAM", [
    ("LeBron James begins his 24th season — a record — in a new shirt : Philadelphia. He arrived this summer, and on night one, his new team won on the champions' floor.", "serif", False, INK, 21.5, 1.45),
    ("James startet seine 24. Saison — ein Rekord — im Trikot von Philadelphia. Gleich in der ersten Nacht gewann sein neues Team in der Halle der Champions.", "sans", False, GREY, 20.5, 1.4),
])
v4.box("SPORTS WORDS · Wortliste", [
    ("tip-off — Spielbeginn (Basketball)", "serif", False, INK, 21.5, 1.5),
    ("a banner — Meisterfahne", "serif", False, INK, 21.5, 1.5),
    ("to sweep — alle Spiele gewinnen", "serif", False, INK, 21.5, 1.5),
    ("the defending champion — Titelverteidiger", "serif", False, INK, 21.5, 1.5),
    ("qualifying — Qualifikation", "serif", False, INK, 21.5, 1.5),
    ("a race — ein Rennen", "serif", False, INK, 21.5, 1.5),
    ("overtime — Verlängerung (extra time)", "serif", False, INK, 21.5, 1.5),
    ("a fan — ein Fan", "serif", False, INK, 21.5, 1.5),
])
v4.box("THE WEEK IN NUMBERS", [
    ("43 — games in the NBA's first six days", "serif", False, INK, 21.5, 1.45),
    ("106–100 — Philadelphia's win in New York", "serif", False, INK, 21.5, 1.45),
    ("1973 — the Knicks' previous banner · 1982 — Milwaukee's last World Series", "serif", False, INK, 21.5, 1.45),
    ("24 — LeBron James's season number, a record", "serif", False, INK, 21.5, 1.45),
])
v4.head("WATCHING A GAME IN ENGLISH", 23)
v4.para("« What a shot ! » — Was für ein Wurf!", 21.5, "serif", True, OLIVE)
v4.para("« They are up by six. » — Sie führen mit sechs.", 21.5)
v4.para("« It is going down to the last minute. » — Spannend bis zur letzten Minute.", 21.5)
v4.para("« We were robbed ! » — Wir wurden betrogen! (Fan-Spruch nach einer Niederlage, halb im Scherz)", 21.5)
v4.box("THE DEBATE · Die Debatte", [
    ("Three finals in one week : the NBA begins, baseball ends, and the cars race in Austin. A feast for fans — or too much sport ? Tell us on page 7.", "serif", False, INK, 21.5, 1.45),
])
v4.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
