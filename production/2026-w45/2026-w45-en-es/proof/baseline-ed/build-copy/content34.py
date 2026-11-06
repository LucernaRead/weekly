# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-es-proof/baseline-ed/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE · Cultura", "The Lucerna", "A2 → B1 · Friday at the movies · El viernes, al cine")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P3-main")
f.title("Friday Night at the Movies : A Cat and a Monster", 37)
f.byline("By The Lucerna newsroom · Reading level : A2 → B1")
f.para("On Friday, November 6, two very different films open in cinemas across America. One is for children and families. The other is for monster fans. Both give you a reason to go out on a dark autumn evening.")
f.para("The first is « The Cat in the Hat », from the famous children's book by Dr. Seuss. The Cat — tall, funny, and always in trouble — comes to life on the big screen, with Bill Hader as the voice of the Cat. If you know the book, you know the hat : red and white, and much too tall.")
f.para("The second is « Godzilla Minus Zero », the new film from Japanese director Takashi Yamazaki. Godzilla is the giant monster who has walked through Japanese films for more than seventy years. This time, the monster returns to the cinema — bigger, darker, and louder than ever.")
f.para("Which film would you choose ? A talking cat in a striped hat, or a giant monster in a city ? In our newsroom, the vote is split — half for the cat, half for the monster. Tell us your choice on page 7.")
f.box("AT HOME THIS WEEK · En casa", [
    ("Wed Nov 4 — « A Dog's Perfect Christmas » and « Taken : Natalee Holloway » arrive on Netflix.", "serif", False, INK, 21.5, 1.4),
    ("Thu Nov 5 — « Black Doves » Season 2 begins. Fri Nov 6 — « Under Siege » Season 1 and « Unprotected : Murder in Galicia ».", "serif", False, INK, 21.5, 1.4),
    ("Sun Nov 8 — « Love Is Blind : The Reunion » closes the week. One week, one screen, many stories.", "serif", False, INK, 21.5, 1.4),
])
f.para("A film is not only a story — it is also English practice. Listen for three things : the catchphrase (the line everybody repeats), the joke (why does the room laugh ?), and the ending (happy, sad, or open ?). After the film, try to tell the story in five English sentences.")
f.para("And if you stay at home, the same rule works for a series : one episode, five sentences, in English. The best five-sentence reviews will be printed in VOL.3 — send yours to the newsroom.")
f.gloss("to open (cine) estrenarse · a monster un monstruo · a catchphrase una frase célebre · a series una serie.")
f.head("A · COMPREHENSION", 25)
f.bridge("Lee el artículo de la página 3 y elige la respuesta correcta.")
f.ex("A2", "Opción múltiple", "B", "la película del Gato se estrena el viernes 6 de noviembre",
     "« The Cat in the Hat » opens on... A. November 3 · B. Friday, November 6 · C. November 8", size=22)
f.ex("A2", "Opción múltiple", "A", "el Gato sale de un libro del Dr. Seuss",
     "The Cat comes from a book by... A. Dr. Seuss · B. Takashi Yamazaki · C. Bill Hader", size=22)
f.ex("A2", "Opción múltiple", "C", "Bill Hader pone la voz del Gato",
     "The voice of the Cat is... A. the director · B. Godzilla · C. Bill Hader", size=22)
f.ex("B1", "Opción múltiple", "B", "el director de Godzilla es Takashi Yamazaki",
     "« Godzilla Minus Zero » is directed by... A. Dr. Seuss · B. Takashi Yamazaki · C. Bill Hader", size=22)
f.ex("B1", "Opción múltiple", "A", "la segunda temporada de Black Doves llega el 5 de noviembre",
     "« Black Doves » Season 2 begins on... A. Thursday, November 5 · B. Friday, November 6 · C. Sunday, November 8", size=22)
f.ex("B1", "Opción múltiple", "C", "el reencuentro del domingo cierra la semana",
     "The week closes with... A. a film · B. a monster · C. « Love Is Blind : The Reunion »", size=22)
f.head("B · SENTENCES", 25)
f.bridge("Completa las frases con las palabras dadas.")
f.ex("A2", "Completar frases", "opens", "open = estrenarse (tercera persona singular con s)",
     "The film ___ on Friday, November 6.", instr="Completa")
f.ex("A2", "Completar frases", "taller", "tall → taller, comparativo",
     "The hat is ___ than the Cat himself !", instr="Completa")
f.ex("B1", "Completar frases", "louder", "loud → louder",
     "Godzilla is bigger, darker, and ___ than ever this time.", instr="Completa")
f.ex("B1", "Completar frases", "split", "split = dividida",
     "In our newsroom, the vote is ___ : half cat, half monster.", instr="Completa")
f.head("C · THE WORDS", 25)
f.match_set("A2", "Emparejar",
            ["a monster", "a catchphrase", "a series", "to open"],
            ["a line everybody repeats",
             "a giant frightening creature",
             "a film's first day in cinemas",
             "a story told in many episodes"],
            ["b", "a", "d", "c"],
            ["monster=un monstruo b", "catchphrase=una frase célebre a", "series=una serie d", "open=estrenarse c"],
            instr="Empareja")
f.head("D · GOING TO", 25)
f.bridge("Reescribe con be going to.")
f.ex("A2", "Reescribir", "We are going to watch the cat film on Friday.", "we → are going to",
     "We (watch) the cat film on Friday. → ___", instr="Reescribe")
f.ex("A2", "Reescribir", "She is going to tell the story in five sentences.", "she → is going to",
     "She (tell) the story in five sentences. → ___", instr="Reescribe")
f.ex("B1", "Reescribir", "Are you going to choose the monster ?", "pregunta: be al principio",
     "You (choose) the monster ? → ___", instr="Reescribe")
f.ex("B1", "Reescribir", "They are going to send their reviews to the newsroom.", "they → are going to",
     "They (send) their reviews to the newsroom. → ___", instr="Reescribe")
f.end_report()

# col 3: image + side flow
ix = COLX[3]
image(p, "catmanet.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "A cat in art : « Cat and Flowers », an illustration by Édouard Manet for « The Cats » by Champfleury. Not film art — but this week, every cat is a star.",
              "Édouard Manet — CC0, via Wikimedia Commons")
v3 = Flow(p, [(ix, CW)], int(cy3) + 18, 2540, tag="P3-col3")
v3.box("THE CAT'S HAT · El sombrero", [
    ("Red and white stripes, much too tall — the most famous hat in children's books. In the film, the hat is back, and so is the trouble.", "serif", False, INK, 21.5, 1.42),
])
v3.head("FIVE SENTENCES", 25)
v3.para("After any film or episode, tell the story in five English sentences : who, where, what happened, the surprise, the ending. Five sentences are enough — and they are excellent practice.", 22)
v3.para("Example : « A cat comes to a house. Two children are bored. The cat plays games. The house is a mess. Then the cat cleans it all up. » Now it is your turn.", 22)
v3.bridge("Cinco frases de crítica: quién, dónde, qué pasó, el giro y el final; con cinco basta.")
v3.end_report()
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · Deportes", "The Lucerna", "LEVEL B1 · NFL · F1 · NASCAR · WTA · Boxing")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P4-main")
f.title("Sunday in Madrid, São Paulo and Miami", 37)
f.byline("By The Lucerna newsroom · Reading level : B1")
f.para("Sunday, November 8, is the biggest sports day of the autumn. Three countries, five sports, one Sunday — and American football in a Spanish football stadium.")
f.para("In Madrid, the NFL plays its international game at the Santiago Bernabéu : the Cincinnati Bengals against the Atlanta Falcons. American football in the home of Real Madrid — a strange and wonderful mix. The game is part of NFL Week 9, and it is the week's most talked-about fixture.")
f.para("Back in the United States, Week 9 continues the same day : the Miami Dolphins play the Detroit Lions at Hard Rock Stadium in Miami Gardens. Two games, two continents, one league — that is the modern NFL.")
f.para("In Brazil, Formula 1 races the São Paulo Grand Prix, the second race after the United States Grand Prix in Austin. Fast cars, a famous track, and a championship still to decide — the perfect Sunday afternoon for racing fans.")
f.para("And there is more : NASCAR races at Homestead-Miami, the WTA Finals begin at Indian Wells, and in Arlington, Texas, Alycia Baumgardner defends her women's lightweight title against Elif Nur Turhan. One Sunday is not enough — good thing the week has seven days.")
f.box("WHY MADRID ? · ¿Por qué Madrid?", [
    ("The NFL plays games outside the United States every year, so new fans can see the sport live. Madrid joins London, Munich and São Paulo on the international map.", "serif", False, INK, 21.5, 1.4),
])
f.para("How do you follow five sports in one day ? Choose one game to watch fully, and follow the others on your phone. That is the modern fan : one screen for the game, one screen for the scores.")
f.para("On Saturday, November 7, the warm-up is already on : Major League Soccer plays its late-season fixtures, including Charlotte against Inter Miami and Atlanta against the New York Red Bulls. The weekend starts on Saturday — and it does not stop.")
f.gloss("a fixture un partido del calendario · a title un título · to defend (campeón) defender el título · a fan un aficionado.")
f.head("A · COMPREHENSION", 25)
f.bridge("Lee el artículo de la página 4 y elige la respuesta correcta.")
f.ex("B1", "Opción múltiple", "A", "Madrid: Bengals contra Falcons",
     "In Madrid, the Bengals play... A. the Falcons · B. the Lions · C. Real Madrid", size=22)
f.ex("B1", "Opción múltiple", "C", "el estadio de Madrid es el Bernabéu",
     "The Madrid game is at... A. Hard Rock Stadium · B. Wembley · C. the Santiago Bernabéu", size=22)
f.ex("B1", "Opción múltiple", "B", "Dolphins contra Lions en Miami",
     "The Dolphins play the Lions in... A. Madrid · B. Miami · C. São Paulo", size=22)
f.ex("B1", "Opción múltiple", "A", "el Gran Premio de São Paulo de F1, en Brasil",
     "The São Paulo Grand Prix is in... A. Brazil · B. Spain · C. Texas", size=22)
f.ex("B1", "Opción múltiple", "C", "las Finales de la WTA empiezan en Indian Wells",
     "The WTA Finals begin at... A. Miami · B. Madrid · C. Indian Wells", size=22)
f.ex("B1", "Opción múltiple", "B", "el boxeo, en Arlington",
     "The Baumgardner fight is in... A. Miami · B. Arlington, Texas · C. Madrid", size=22)
f.head("B · SENTENCES", 25)
f.bridge("Completa las frases con las palabras dadas.")
f.ex("B1", "Completar frases", "defends", "defend, tercera persona singular con s",
     "Baumgardner ___ her title on Sunday.", instr="Completa")
f.ex("B1", "Completar frases", "begin", "como en el artículo de la página 4, verbo en plural",
     "The WTA Finals ___ on Sunday.", instr="Completa")
f.ex("A2", "Completar frases", "bigger", "big → bigger",
     "The Bernabéu is ___ than most NFL stadiums.", instr="Completa")
f.ex("A2", "Completar frases", "faster", "fast → faster",
     "Formula 1 cars are ___ than NASCAR cars on a road course.", instr="Completa")
f.head("C · THE WORDS", 25)
f.match_set("B1", "Emparejar",
            ["a fixture", "a title", "a fan", "to defend"],
            ["a person who loves a team or sport",
             "a game in a season's schedule",
             "to keep a championship you already hold",
             "the honour of being champion"],
            ["b", "d", "a", "c"],
            ["fixture=un partido del calendario b", "title=un título d", "fan=un aficionado a", "defend=defender el título c"],
            instr="Empareja")
f.head("D · PAST SIMPLE", 25)
f.bridge("Reescribe en pasado simple (los partidos ya terminaron).")
f.ex("B1", "Reescribir", "The Bengals played in Madrid on Sunday.", "play → played",
     "The Bengals (play) in Madrid on Sunday. → ___", instr="Reescribe")
f.ex("B1", "Reescribir", "She watched the race in São Paulo.", "watch → watched",
     "She (watch) the race in São Paulo. → ___", instr="Reescribe")
f.ex("B1", "Reescribir", "They followed the scores on their phones.", "follow → followed",
     "They (follow) the scores on their phones. → ___", instr="Reescribe")
f.ex("B1", "Reescribir", "He chose one game to watch fully.", "choose → chose",
     "He (choose) one game to watch fully. → ___", instr="Reescribe")
f.end_report()

# col 3: image + fixtures
ix = COLX[3]
image(p, "football1910.jpg", ix, 200, CW, 470)
cy4 = caption(p, ix, 670, CW, "American football in 1910 : Miami against Wittenberg. The helmets were leather, the fields were mud — but the game was already America's game.",
              "Frank R. Snyder — public domain, via Wikimedia Commons")
v4 = Flow(p, [(ix, CW)], int(cy4) + 18, 2540, tag="P4-col3")
v4.box("SUNDAY, NOVEMBER 8 · Domingo", [
    ("NFL : Bengals–Falcons, Madrid (Bernabéu) ; Dolphins–Lions, Miami.", "serif", False, INK, 21.5, 1.42),
    ("F1 : São Paulo Grand Prix, Brazil. NASCAR : Homestead-Miami.", "serif", False, INK, 21.5, 1.42),
    ("WTA Finals begin, Indian Wells. Boxing : Baumgardner–Turhan, Arlington.", "serif", False, INK, 21.5, 1.42),
    ("SATURDAY, NOVEMBER 7 : MLS — Charlotte–Inter Miami ; Atlanta–New York Red Bulls.", "serif", False, INK, 21.5, 1.42),
])
v4.head("ONE SCREEN, TWO SCREENS", 25)
v4.para("The modern fan watches one game fully and follows the others on a phone. Try it in English : « The score is 14–10. » « Who scored ? » « Madrid is winning ! » — short sentences, live English.", 22)
v4.bridge("Inglés de partido: el marcador, quién marca, quién va por delante; frases cortas, como en directo.")
v4.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
