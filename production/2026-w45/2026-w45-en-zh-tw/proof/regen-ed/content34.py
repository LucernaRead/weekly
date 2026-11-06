# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = "/home/hatch/workspace/goals/lucernaread-social-media-operations/hidden_files/w45/en-zh-tw-proof/regen-ed/svg"
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE · 文化", "The Lucerna", "A2 → B1 · Friday at the movies · 週五看電影")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P3-main")
f.title("Friday Night at the Movies : A Cat and a Monster", 37)
f.byline("By The Lucerna newsroom · Reading level : A2 → B1")
f.para("On Friday, November 6, two very different films open in cinemas across America. One is for children and families. The other is for monster fans. Both give you a reason to go out on a dark autumn evening.")
f.para("The first is « The Cat in the Hat », from the famous children's book by Dr. Seuss. The Cat — tall, funny, and always in trouble — comes to life on the big screen, with Bill Hader as the voice of the Cat. If you know the book, you know the hat : red and white, and much too tall.")
f.para("The second is « Godzilla Minus Zero », the new film from Japanese director Takashi Yamazaki. Godzilla is the giant monster who has walked through Japanese films for more than seventy years. This time, the monster returns to the cinema — bigger, darker, and louder than ever.")
f.para("Which film would you choose ? A talking cat in a striped hat, or a giant monster in a city ? In our newsroom, the vote is split — half for the cat, half for the monster. Tell us your choice on page 7.")
f.box("AT HOME THIS WEEK · 在家看什麼", [
    ("Wed Nov 4 — « A Dog's Perfect Christmas » and « Taken : Natalee Holloway » arrive on Netflix.", "serif", False, INK, 21.5, 1.4),
    ("Thu Nov 5 — « Black Doves » Season 2 begins. Fri Nov 6 — « Under Siege » Season 1 and « Unprotected : Murder in Galicia ».", "serif", False, INK, 21.5, 1.4),
    ("Sun Nov 8 — « Love Is Blind : The Reunion » closes the week. One week, one screen, many stories.", "serif", False, INK, 21.5, 1.4),
])
f.para("A film is not only a story — it is also English practice. Listen for three things : the catchphrase (the line everybody repeats), the joke (why does the room laugh ?), and the ending (happy, sad, or open ?). After the film, try to tell the story in five English sentences.")
f.para("And if you stay at home, the same rule works for a series : one episode, five sentences, in English. The best five-sentence reviews will be printed in VOL.3 — send yours to the newsroom.")
f.gloss("講解｜to open （電影）上映 · a monster 怪物 · a catchphrase 口頭禪、金句 · a series 劇集。")
f.head("A · COMPREHENSION", 25)
f.expl("讀第 3 版文章，選出正確答案。")
f.ex("A2", "單選", "B", "貓咪電影 11 月 6 日週五上映",
     "« The Cat in the Hat » opens on... A. November 3 · B. Friday, November 6 · C. November 8", size=22)
f.ex("A2", "單選", "A", "貓出自蘇斯博士的書",
     "The Cat comes from a book by... A. Dr. Seuss · B. Takashi Yamazaki · C. Bill Hader", size=22)
f.ex("A2", "單選", "C", "比爾·哈德為貓配音",
     "The voice of the Cat is... A. the director · B. Godzilla · C. Bill Hader", size=22)
f.ex("B1", "單選", "B", "哥斯拉導演是山崎貴",
     "« Godzilla Minus Zero » is directed by... A. Dr. Seuss · B. Takashi Yamazaki · C. Bill Hader", size=22)
f.ex("B1", "單選", "A", "《黑鴿》第二季 11 月 5 日上線",
     "« Black Doves » Season 2 begins on... A. Thursday, November 5 · B. Friday, November 6 · C. Sunday, November 8", size=22)
f.ex("B1", "單選", "C", "週日重聚節目收尾",
     "The week closes with... A. a film · B. a monster · C. « Love Is Blind : The Reunion »", size=22)
f.head("B · SENTENCES", 25)
f.expl("用所給詞補全句子。")
f.ex("A2", "完成句子", "opens", "open = 上映（第三人稱單數加 s）",
     "The film ___ on Friday, November 6.", instr="填空")
f.ex("A2", "完成句子", "taller", "tall → taller 比較級",
     "The hat is ___ than the Cat himself !", instr="填空")
f.ex("B1", "完成句子", "louder", "loud → louder",
     "Godzilla is bigger, darker, and ___ than ever this time.", instr="填空")
f.ex("B1", "完成句子", "split", "split = 分歧的",
     "In our newsroom, the vote is ___ : half cat, half monster.", instr="填空")
f.head("C · THE WORDS", 25)
f.match_set("A2", "詞彙配對",
            ["a monster", "a catchphrase", "a series", "to open"],
            ["a line everybody repeats",
             "a giant frightening creature",
             "a film's first day in cinemas",
             "a story told in many episodes"],
            ["b", "a", "d", "c"],
            ["monster=怪物 b", "catchphrase=金句 a", "series=劇集 d", "open=上映 c"],
            instr="把詞和釋義配對")
f.head("D · GOING TO", 25)
f.expl("用 be going to 改寫。")
f.ex("A2", "句型轉換", "We are going to watch the cat film on Friday.", "we → are going to",
     "We (watch) the cat film on Friday. → ___", instr="改寫")
f.ex("A2", "句型轉換", "She is going to tell the story in five sentences.", "she → is going to",
     "She (tell) the story in five sentences. → ___", instr="改寫")
f.ex("B1", "句型轉換", "Are you going to choose the monster ?", "疑問句：be 提前",
     "You (choose) the monster ? → ___", instr="改寫")
f.ex("B1", "句型轉換", "They are going to send their reviews to the newsroom.", "they → are going to",
     "They (send) their reviews to the newsroom. → ___", instr="改寫")
f.end_report()

# col 3: image + side flow
ix = COLX[3]
image(p, "catmanet.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "A cat in art : « Cat and Flowers », an illustration by Édouard Manet for « The Cats » by Champfleury. Not film art — but this week, every cat is a star.",
              "Édouard Manet — CC0, via Wikimedia Commons")
v3 = Flow(p, [(ix, CW)], int(cy3) + 18, 2540, tag="P3-col3")
v3.box("THE CAT'S HAT · 貓的帽子", [
    ("Red and white stripes, much too tall — the most famous hat in children's books. In the film, the hat is back, and so is the trouble.", "serif", False, INK, 21.5, 1.42),
])
v3.head("FIVE SENTENCES", 25)
v3.para("After any film or episode, tell the story in five English sentences : who, where, what happened, the surprise, the ending. Five sentences are enough — and they are excellent practice.", 22)
v3.para("Example : « A cat comes to a house. Two children are bored. The cat plays games. The house is a mess. Then the cat cleans it all up. » Now it is your turn.", 22)
v3.expl("五句影評｜who、where、發生了什麼、轉折、結局——五句就夠。")
v3.end_report()
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · 體育", "The Lucerna", "LEVEL B1 · NFL · F1 · NASCAR · WTA · Boxing")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P4-main")
f.title("Sunday in Madrid, São Paulo and Miami", 37)
f.byline("By The Lucerna newsroom · Reading level : B1")
f.para("Sunday, November 8, is the biggest sports day of the autumn. Three countries, five sports, one Sunday — and American football in a Spanish football stadium.")
f.para("In Madrid, the NFL plays its international game at the Santiago Bernabéu : the Cincinnati Bengals against the Atlanta Falcons. American football in the home of Real Madrid — a strange and wonderful mix. The game is part of NFL Week 9, and it is the week's most talked-about fixture.")
f.para("Back in the United States, Week 9 continues the same day : the Miami Dolphins play the Detroit Lions at Hard Rock Stadium in Miami Gardens. Two games, two continents, one league — that is the modern NFL.")
f.para("In Brazil, Formula 1 races the São Paulo Grand Prix, the second race after the United States Grand Prix in Austin. Fast cars, a famous track, and a championship still to decide — the perfect Sunday afternoon for racing fans.")
f.para("And there is more : NASCAR races at Homestead-Miami, the WTA Finals begin at Indian Wells, and in Arlington, Texas, Alycia Baumgardner defends her women's lightweight title against Elif Nur Turhan. One Sunday is not enough — good thing the week has seven days.")
f.box("WHY MADRID ? · 為什麼去馬德里？", [
    ("The NFL plays games outside the United States every year, so new fans can see the sport live. Madrid joins London, Munich and São Paulo on the international map.", "serif", False, INK, 21.5, 1.4),
])
f.para("How do you follow five sports in one day ? Choose one game to watch fully, and follow the others on your phone. That is the modern fan : one screen for the game, one screen for the scores.")
f.para("On Saturday, November 7, the warm-up is already on : Major League Soccer plays its late-season fixtures, including Charlotte against Inter Miami and Atlanta against the New York Red Bulls. The weekend starts on Saturday — and it does not stop.")
f.gloss("講解｜a fixture 一場比賽（賽程） · a title 冠軍頭銜 · to defend （衛冕）保衛頭銜 · a fan 球迷。")
f.head("A · COMPREHENSION", 25)
f.expl("讀第 4 版文章，選出正確答案。")
f.ex("B1", "單選", "A", "馬德里賽：孟加拉虎對獵鷹",
     "In Madrid, the Bengals play... A. the Falcons · B. the Lions · C. Real Madrid", size=22)
f.ex("B1", "單選", "C", "馬德里賽場是伯納烏",
     "The Madrid game is at... A. Hard Rock Stadium · B. Wembley · C. the Santiago Bernabéu", size=22)
f.ex("B1", "單選", "B", "海豚對雄獅在邁阿密",
     "The Dolphins play the Lions in... A. Madrid · B. Miami · C. São Paulo", size=22)
f.ex("B1", "單選", "A", "F1 聖保羅大獎賽在巴西",
     "The São Paulo Grand Prix is in... A. Brazil · B. Spain · C. Texas", size=22)
f.ex("B1", "單選", "C", "WTA 年終總決賽在印地安泉開賽",
     "The WTA Finals begin at... A. Miami · B. Madrid · C. Indian Wells", size=22)
f.ex("B1", "單選", "B", "拳擊賽在阿靈頓",
     "The Baumgardner fight is in... A. Miami · B. Arlington, Texas · C. Madrid", size=22)
f.head("B · SENTENCES", 25)
f.expl("用所給詞補全句子。")
f.ex("B1", "完成句子", "defends", "defend 三單加 s",
     "Baumgardner ___ her title on Sunday.", instr="填空")
f.ex("B1", "完成句子", "begin", "與第 4 版原文一致，複數動詞",
     "The WTA Finals ___ on Sunday.", instr="填空")
f.ex("A2", "完成句子", "bigger", "big → bigger",
     "The Bernabéu is ___ than most NFL stadiums.", instr="填空")
f.ex("A2", "完成句子", "faster", "fast → faster",
     "Formula 1 cars are ___ than NASCAR cars on a road course.", instr="填空")
f.head("C · THE WORDS", 25)
f.match_set("B1", "詞彙配對",
            ["a fixture", "a title", "a fan", "to defend"],
            ["a person who loves a team or sport",
             "a game in a season's schedule",
             "to keep a championship you already hold",
             "the honour of being champion"],
            ["b", "d", "a", "c"],
            ["fixture=賽程中的比賽 b", "title=冠軍頭銜 d", "fan=球迷 a", "defend=衛冕 c"],
            instr="把詞和釋義配對")
f.head("D · PAST SIMPLE", 25)
f.expl("用一般過去時改寫（比賽已結束的說法）。")
f.ex("B1", "句型轉換", "The Bengals played in Madrid on Sunday.", "play → played",
     "The Bengals (play) in Madrid on Sunday. → ___", instr="改寫")
f.ex("B1", "句型轉換", "She watched the race in São Paulo.", "watch → watched",
     "She (watch) the race in São Paulo. → ___", instr="改寫")
f.ex("B1", "句型轉換", "They followed the scores on their phones.", "follow → followed",
     "They (follow) the scores on their phones. → ___", instr="改寫")
f.ex("B1", "句型轉換", "He chose one game to watch fully.", "choose → chose",
     "He (choose) one game to watch fully. → ___", instr="改寫")
f.end_report()

# col 3: image + fixtures
ix = COLX[3]
image(p, "football1910.jpg", ix, 200, CW, 470)
cy4 = caption(p, ix, 670, CW, "American football in 1910 : Miami against Wittenberg. The helmets were leather, the fields were mud — but the game was already America's game.",
              "Frank R. Snyder — public domain, via Wikimedia Commons")
v4 = Flow(p, [(ix, CW)], int(cy4) + 18, 2540, tag="P4-col3")
v4.box("SUNDAY, NOVEMBER 8 · 週日賽程", [
    ("NFL : Bengals–Falcons, Madrid (Bernabéu) ; Dolphins–Lions, Miami.", "serif", False, INK, 21.5, 1.42),
    ("F1 : São Paulo Grand Prix, Brazil. NASCAR : Homestead-Miami.", "serif", False, INK, 21.5, 1.42),
    ("WTA Finals begin, Indian Wells. Boxing : Baumgardner–Turhan, Arlington.", "serif", False, INK, 21.5, 1.42),
    ("SATURDAY, NOVEMBER 7 : MLS — Charlotte–Inter Miami ; Atlanta–New York Red Bulls.", "serif", False, INK, 21.5, 1.42),
])
v4.head("ONE SCREEN, TWO SCREENS", 25)
v4.para("The modern fan watches one game fully and follows the others on a phone. Try it in English : « The score is 14–10. » « Who scored ? » « Madrid is winning ! » — short sentences, live English.", 22)
v4.expl("看球英語｜比數、誰得分、誰領先——短句就是直播英語。")
v4.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
