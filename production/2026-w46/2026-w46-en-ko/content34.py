# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE　문화", "The Lucerna", "A2 → B1　Friday at the movies　금요일 영화")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P3-main")
f.title("Friday Night at the Movies : Scrooge Comes Early", 32)
f.byline("By The Lucerna newsroom　Reading level : A2 → B1")
f.para("On Friday, November 13, a ghost comes to the cinema — early. « Ebenezer » is a dark new telling of Charles Dickens's « A Christmas Carol », with Johnny Depp as Ebenezer Scrooge, the miser who hates Christmas. Christmas is still six weeks away. The film does not wait.")
f.para("Dickens wrote the story in 1843, in London. Scrooge is visited in one night by three ghosts : the Ghost of Christmas Past, the Ghost of Christmas Present, and the Ghost of Christmas Yet to Come. By morning, the cold old man is warm again. The book made Christmas what it is in Britain — and the films keep remaking it.")
f.para("The second film of the week is very different. « How to Rob a Bank » is a heist comedy : bank robbers who film their crimes and post them online. The police follow the likes. It is fast, funny and very 2026 — crime as content.")
f.para("Which film would you choose ? A ghost story in Dickens's London, or a bank story on today's internet ? In our newsroom, the vote is split again — half for the ghost, half for the bank. Tell us your choice on page 7.")
f.box("COMING SOON　곧 개봉", [
    ("Fri Nov 20 — « The Hunger Games : Sunrise on the Reaping » opens in cinemas. Fri Nov 27 — Disney's « Hexed » arrives.", "serif", False, INK, 21.5, 1.4),
    ("Sun Nov 15 — the ATP Finals begin in Turin. Fri Nov 13 — Children in Need, live from Salford.", "serif", False, INK, 21.5, 1.4),
    ("One week, one screen, many stories — and Christmas is coming, one film at a time.", "serif", False, INK, 21.5, 1.4),
])
f.para("A film is not only a story — it is also English practice. Listen for three things : the catchphrase (the line everybody repeats), the joke (why does the room laugh ?), and the ending (happy, sad, or open ?). After the film, try to tell the story in five English sentences.", 23.5)
f.para("And if you stay at home, the same rule works for a series : one episode, five sentences, in English. The best five-sentence reviews will be printed in VOL.4 — send yours to the newsroom.", 23.5)
f.gloss("a miser 구두쇠 · a ghost 유령 · a heist 강도 사건 · yet to come 아직 오지 않은 것.")
f.head("A　COMPREHENSION", 25)
f.bridge("3면 기사를 읽고 정답을 고르세요.")
f.ex("A2", "객관식", "B", "《Ebenezer》 11월 13일 금요일 개봉",
     "« Ebenezer » opens on... A. November 11 · B. Friday, November 13 · C. November 15", size=22)
f.ex("A2", "객관식", "A", "조니 뎁이 스크루지를 연기해요",
     "Scrooge is played by... A. Johnny Depp · B. Charles Dickens · C. John Leech", size=22)
f.ex("A2", "객관식", "C", "이야기는 1843년에 쓰였어요",
     "Dickens wrote the story in... A. 1918 · B. 1920 · C. 1843", size=22)
f.ex("B1", "객관식", "B", "세 유령이 하룻밤에 찾아와요",
     "Scrooge is visited by... A. one ghost · B. three ghosts · C. five ghosts", size=22)
f.ex("B1", "객관식", "A", "강도들이 범행을 인터넷에 올려요",
     "In « How to Rob a Bank », the robbers... A. post their crimes online · B. rob a ghost · C. hate Christmas", size=22)
f.ex("B1", "객관식", "C", "《헝거 게임》 신작 11월 20일 개봉",
     "« The Hunger Games : Sunrise on the Reaping » opens on... A. November 13 · B. November 15 · C. November 20", size=22)
f.head("B　SENTENCES", 25)
f.bridge("주어진 단어로 문장을 완성하세요.")
f.ex("A2", "문장 완성", "opens", "open = 개봉하다(3인칭 단수는 s 추가)",
     "The film ___ on Friday, November 13.", instr="빈칸 채우기")
f.ex("A2", "문장 완성", "miser", "miser = 구두쇠",
     "Scrooge is a ___ who hates Christmas.", instr="빈칸 채우기")
f.ex("B1", "문장 완성", "split", "split = 의견이 갈린",
     "In our newsroom, the vote is ___ : half ghost, half bank.", instr="빈칸 채우기")
f.ex("B1", "문장 완성", "ghost", "ghost = 유령",
     "Marley's ___ visits Scrooge at night.", instr="빈칸 채우기")
f.head("C　THE WORDS", 25)
f.match_set("A2", "단어 짝짓기",
            ["a miser", "a ghost", "a heist", "a catchphrase"],
            ["a line everybody repeats",
             "a person who loves money and hates spending it",
             "the spirit of a dead person",
             "a robbery, usually of a bank"],
            ["b", "c", "d", "a"],
            ["miser = 구두쇠 b", "ghost = 유령 c", "heist = 강도 사건 d", "catchphrase = 명대사 a"],
            instr="단어와 뜻 짝짓기")
f.head("D　PAST SIMPLE", 25)
f.bridge("일반 과거형으로 바꿔 쓰세요(이미 일어난 일).")
f.ex("A2", "문장 바꾸기", "Dickens wrote the story in 1843.", "write → wrote",
     "Dickens (write) the story in 1843. → ___", instr="바꿔 쓰기")
f.ex("A2", "문장 바꾸기", "The ghosts visited Scrooge in one night.", "visit → visited",
     "The ghosts (visit) Scrooge in one night. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "Scrooge became warm again by morning.", "become → became",
     "Scrooge (become) warm again by morning. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "She chose the ghost story.", "choose → chose",
     "She (choose) the ghost story. → ___", instr="바꿔 쓰기")
f.end_report()

# col 3: image + side flow
ix = COLX[3]
image(p, "marley.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "A ghost in art : Marley's Ghost visits Scrooge, in John Leech's illustration for Dickens's « A Christmas Carol » (1843). Not film art — but this week, every ghost is a star.",
              "John Leech — public domain, via Wikimedia Commons")
v3 = Flow(p, [(ix, CW)], int(cy3) + 18, 2560, tag="P3-col3")
v3.box("SCROOGE'S NIGHT　스크루지의 밤", [
    ("Three ghosts, one night : Past, Present, and Yet to Come. By morning, Scrooge is a new man — and Christmas is saved, six weeks early.", "serif", False, INK, 21.5, 1.42),
])
v3.head("FIVE SENTENCES", 25)
v3.para("After any film or episode, tell the story in five English sentences : who, where, what happened, the surprise, the ending. Five sentences are enough — and they are excellent practice.", 22)
v3.para("Example : « A ghost comes to a house. A miser is cold and alone. Three ghosts visit him. He sees his past, his present and his future. Then he is warm again. » Now it is your turn.", 22)
v3.bridge("다섯 문장 평｜who, where, 무슨 일, 반전, 결말 — 다섯 문장이면 돼요.")
v3.end_report()
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "The Lucerna", "LEVEL B1　NFL　ATP　Nations League")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P4-main")
f.title("Sunday in Munich, Turin and Madrid", 32)
f.byline("By The Lucerna newsroom　Reading level : B1")
f.para("Sunday, November 15, is the biggest sports day of the autumn. Three cities, three sports, one Sunday — and American football in the home of Bayern Munich.")
f.para("In Munich, the NFL plays at the Allianz Arena : the Detroit Lions, the home team, against the New England Patriots. The game starts at 3:30 p.m. local time — 9:30 a.m. in New York. It is the Lions' first game in Germany, and a special game for their German-American star, Amon-Ra St. Brown, whose mother is German. The game is part of NFL Week 10, and it is the week's most talked-about fixture.")
f.para("Back in the United States, Week 10 continues the same day : the Chiefs play the Falcons in Atlanta, the Vikings play the Packers at Lambeau Field, and the 49ers play the Cowboys in Arlington. The week began on Thursday, November 12, with the Commanders at the Giants, and ends on Monday, November 16, with the Chargers at the Ravens.")
f.para("In Turin, Italy, tennis begins its season finale : the ATP Finals, from Sunday, November 15, to Sunday, November 22. The eight best singles players of the year play in two groups of four, and the final is on November 22. The field was settled on Monday, November 9, after the Paris Masters.")
f.para("And in Madrid, football takes the stage : Spain play England in the Nations League on Sunday night, three days after England play Croatia at Wembley on Thursday, November 12. Scotland play North Macedonia at Hampden Park on Friday, November 13. One Sunday is not enough — good thing the week has seven days.")
f.box("WHY MUNICH ?　왜 뮌헨일까요?", [
    ("The NFL plays games outside the United States every year, so new fans can see the sport live. Munich hosted NFL games in 2022 and 2024, and will host again in 2028. This year there are nine international games in all — a record.", "serif", False, INK, 21.5, 1.4),
])
f.para("How do you follow three sports in one day ? Choose one game to watch fully, and follow the others on your phone. That is the modern fan : one screen for the game, one screen for the scores.", 23.5)
f.para("The Allianz Arena holds 70,000 people — bigger than most NFL stadiums. And next week ? The Ashes begin : Australia against England in the first Test in Perth, from Saturday, November 21. Cricket's oldest rivalry, back in Australia. The weekend starts on Sunday — and it does not stop.", 23.5)
f.gloss("a fixture 경기 일정 · a group 조 · a finale 결승전, 마지막 경기 · a star 스타선수.")
f.head("A　COMPREHENSION", 25)
f.bridge("4면 기사를 읽고 정답을 고르세요.")
f.ex("B1", "객관식", "A", "뮌헨 경기: 패트리어츠 대 라이언스",
     "In Munich, the Lions play... A. the Patriots · B. the Falcons · C. Bayern Munich", size=22)
f.ex("B1", "객관식", "C", "뮌헨 킥오프는 현지 시간 오후 3시 30분이에요",
     "The Munich game starts at... A. 9:30 a.m. Munich time · B. 7:45 p.m. · C. 3:30 p.m. local time", size=22)
f.ex("B1", "객관식", "B", "ATP 파이널스는 토리노에서 열려요",
     "The ATP Finals are in... A. Paris · B. Turin · C. Madrid", size=22)
f.ex("B1", "객관식", "A", "잉글랜드 대 크로아티아 11월 12일 목요일",
     "England play Croatia on... A. Thursday, November 12 · B. Friday, November 13 · C. Sunday, November 15", size=22)
f.ex("B1", "객관식", "C", "스코틀랜드 대 북마케도니아",
     "Scotland play... A. Spain · B. Croatia · C. North Macedonia", size=22)
f.ex("B1", "객관식", "B", "10주차 월요일 밤 경기: 차저스 대 레이븐스",
     "Week 10 ends with... A. Commanders at Giants · B. Chargers at Ravens · C. 49ers at Cowboys", size=22)
f.head("B　SENTENCES", 25)
f.bridge("주어진 단어로 문장을 완성하세요.")
f.ex("B1", "문장 완성", "hosts", "host 3인칭 단수 hosts",
     "The Allianz Arena ___ the NFL on Sunday.", instr="빈칸 채우기")
f.ex("B1", "문장 완성", "begin", "4면 원문과 같아요, 복수 동사",
     "The ATP Finals ___ on Sunday, November 15.", instr="빈칸 채우기")
f.ex("A2", "문장 완성", "bigger", "big → bigger",
     "The Allianz Arena is ___ than most NFL stadiums.", instr="빈칸 채우기")
f.ex("A2", "문장 완성", "eight", "여덟 명 = eight",
     "___ singles players play in Turin.", instr="빈칸 채우기")
f.head("C　THE WORDS", 25)
f.match_set("B1", "단어 짝짓기",
            ["a fixture", "a group", "a finale", "a star"],
            ["a famous player, loved by the fans",
             "a game in a season's schedule",
             "the last event of a season",
             "a small set of players who play each other"],
            ["b", "d", "c", "a"],
            ["fixture = 일정 속 경기 b", "group = 조 d", "finale = 마지막 경기 c", "star = 스타 선수 a"],
            instr="단어와 뜻 짝짓기")
f.head("D　PAST SIMPLE", 25)
f.bridge("일반 과거형으로 바꿔 쓰세요(끝난 경기 말하기).")
f.ex("B1", "문장 바꾸기", "The Lions played in Munich on Sunday.", "play → played",
     "The Lions (play) in Munich on Sunday. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "She watched the tennis in Turin.", "watch → watched",
     "She (watch) the tennis in Turin. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "They followed the scores on their phones.", "follow → followed",
     "They (follow) the scores on their phones. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "He chose one game to watch fully.", "choose → chose",
     "He (choose) one game to watch fully. → ___", instr="바꿔 쓰기")
f.end_report()

# col 3: image + fixtures
ix = COLX[3]
image(p, "football1910.jpg", ix, 200, CW, 470)
cy4 = caption(p, ix, 670, CW, "American football in 1910 : Miami against Wittenberg. The helmets were leather, the fields were mud — but the game was already America's game. This week, the game goes to Munich.",
              "Frank R. Snyder — public domain, via Wikimedia Commons")
v4 = Flow(p, [(ix, CW)], int(cy4) + 18, 2560, tag="P4-col3")
v4.box("SUNDAY, NOVEMBER 15　일요일 일정", [
    ("NFL : Patriots–Lions, Munich (Allianz Arena), 3:30 p.m. local time.", "serif", False, INK, 21.5, 1.42),
    ("ATP Finals begin, Turin. Nations League : Spain–England, Madrid, 7:45 p.m.", "serif", False, INK, 21.5, 1.42),
    ("THURSDAY, NOVEMBER 12 : England–Croatia, Wembley. FRIDAY, NOVEMBER 13 : Scotland–North Macedonia, Hampden.", "serif", False, INK, 21.5, 1.42),
    ("MONDAY, NOVEMBER 16 : Chargers–Ravens close NFL Week 10.", "serif", False, INK, 21.5, 1.42),
])
v4.head("ONE SCREEN, TWO SCREENS", 25)
v4.para("The modern fan watches one game fully and follows the others on a phone. Try it in English : « The score is 14–10. » « Who scored ? » « Munich is winning ! » — short sentences, live English.", 22)
v4.bridge("경기 영어｜점수, 누가 득점했는지, 누가 앞서는지 — 짧은 문장이 생중계 영어예요.")
v4.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
