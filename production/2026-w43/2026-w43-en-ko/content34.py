# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE　문화", "The Lucerna", "A2 → B1　Halloween in America　할로윈")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P3-main")
f.title("Halloween in America : a $13.5 Billion Night of Candy", 32)
f.byline("By The Lucerna newsroom　Reading level : A2 → B1")
f.para("On Saturday, October 31, America will put on its costumes. Halloween is not an official holiday — nobody gets the day off — but it is one of the biggest nights of the American year. This year, the National Retail Federation (NRF) projects record spending of 13.5 billion dollars, up 3.82% from 2025. That is about $115.14 for every person who celebrates.")
f.para("Where does the money go ? Costumes come first : $4.4 billion. Decorations are second, at $4.3 billion — gardens full of skeletons, lights and giant spiders. Candy takes $4.1 billion, and almost everybody buys it : 96% of celebrants plan to buy sweets for the big night.")
f.para("How does trick-or-treating work ? In the early evening, children in costumes walk from door to door in their neighbourhood. They ring the bell and shout : « Trick or treat ! » — a joke threat, always answered with candy. One rule matters : a light on the porch means « welcome, knock here ». A dark house means « please, not this year » — and children respect it.")
f.para("The pumpkin is the symbol of the season. In October, families drive to pumpkin patches — fields where you choose your own pumpkin — and carve faces into them at home. A candle inside makes a jack-o'-lantern, and on October 31, thousands of orange faces glow on American porches.")
f.para("What will America wear this year ? Google published its Frightgeist costume list on October 14, and the shop Spirit Halloween published its own : characters from KPop Demon Hunters and Toy Story 5, superheroes, and Greek gods. One number tells the story of 2026 : 47% of celebrants now use AI tools to plan a costume or a decoration. The robot helps you become a ghost.")
f.para("Halloween was a national festival long before it was a shopping season. In the early 1900s, when telephones were still rare, Americans sent Halloween postcards — more than 3,000 designs were printed. The card on this page is from 1912. The greetings travelled slowly, by mail, and arrived like little paper ghosts.")
f.para("This year, the calendar is kind : Halloween falls on a Saturday. No school the next morning, no work for most parents — the party can begin in the afternoon and the last jack-o'-lantern can burn late. Shops know it, too : the last full shopping week of the season is this one, and the costume shelves empty fast.")
f.para("One object waits by every door : the candy bowl. Families fill it in the afternoon — chocolate, sweets, sometimes small toys — and children empty it, street by street, all evening. Economists study the $13.5 billion. Children study something simpler : which house gives the biggest chocolate ?")
f.box("SAY IT ON THE NIGHT　그날 밤 표현", [
    ("« Trick or treat ! » — 사탕 안 주면 장난칠 거예요! (장난스러운 협박, 늘 사탕을 받아요)", "serif", False, INK, 21.5, 1.42),
    ("« Happy Halloween ! » — 해피 할로윈! · « Thank you ! » — 감사합니다! (사탕을 받으면 꼭 말하세요)", "serif", False, INK, 21.5, 1.42),
    ("« What are you dressed as ? » — 무엇으로 분장했어요?", "serif", False, INK, 21.5, 1.42),
], tsize=22)
f.gloss("to celebrate 축하하다 · a porch 현관 앞 공간 · to carve 파다, 조각하다 · a decoration 장식품 · a survey 조사 (NRF가 7,889명을 조사했어요).")
f.head("A　TRUE OR FALSE ?　참 / 거짓", 25)
f.expl("3면 기사를 읽고 참인지 거짓인지 판단하세요.")
f.ex("A2", "읽기 판단", "False", "할로윈은 토요일 (10월 31일)",
     "1. Halloween is on a Friday this year.", instr="참 / 거짓", size=23)
f.ex("A2", "읽기 판단", "True", "NRF 전망은 135억 달러",
     "2. Americans will spend about $13.5 billion on Halloween.", instr="참 / 거짓", size=23)
f.ex("B1", "읽기 판단", "False", "가장 큰 지출은 의상 44억 달러, 사탕이 아니에요",
     "3. Candy is the biggest part of the spending.", instr="참 / 거짓", size=23)
f.ex("A2", "읽기 판단", "True", "47%가 AI 도구로 아이디어를 찾아요",
     "4. Almost half of celebrants use AI tools for costume ideas.", instr="참 / 거짓", size=23)
f.ex("A2", "읽기 판단", "False", "현관 불이 꺼져 있으면 = 올해는 오지 말라는 뜻",
     "5. A house with no light on the porch is asking for visitors.", instr="참 / 거짓", size=23)
f.head("B　FESTIVAL WORDS　축제 단어", 25)
f.ex("A2", "문장 완성", "costume", "costume = 의상, 분장",
     "Children wear a ___ and go from door to door.", instr="빈칸 채우기", size=23)
f.ex("A2", "문장 완성", "carve", "carve a pumpkin: 호박을 파요",
     "You ___ a pumpkin to make a jack-o'-lantern.", instr="빈칸 채우기", size=23)
f.ex("A2", "문장 완성", "porch", "porch = 현관 앞 공간",
     "Families leave a light on the ___ to welcome children.", instr="빈칸 채우기", size=23)
f.ex("A2", "문장 완성", "candy", "96%가 사탕을 사요",
     "Ninety-six percent of celebrants buy ___.", instr="빈칸 채우기", size=23)
f.ex("A2", "문장 완성", "patch", "pumpkin patch = 호박밭",
     "In October, families visit a pumpkin ___ to choose a pumpkin.", instr="빈칸 채우기", size=23)
f.head("C　CHOOSE　객관식", 25)
f.ex("B1", "객관식", "B", "135억 달러는 올해 전망치",
     "The $13.5 billion is... A. last year's total · B. this year's projection · C. candy money only", size=22.5)
f.ex("B1", "객관식", "A", "구글 순위의 이름은 Frightgeist",
     "Google's costume list is called... A. Frightgeist · B. Spiritgeist · C. Trendlist", size=22.5)
f.ex("B1", "객관식", "B", "올해는 그리스 신들이 유행",
     "This year's costumes include... A. Roman kings · B. Greek gods · C. astronauts only", size=22.5)
f.ex("B1", "객관식", "B", "20세기 초에는 엽서로 인사를 전했어요",
     "In the early 1900s, Halloween greetings travelled by... A. telephone · B. postcard · C. radio", size=22.5)
f.head("D　SENTENCES　문장 바꾸기", 25)
f.ex("A2", "문장 바꾸기", "Children go door to door on October 31.", "현재 시제는 습관을 말해요",
     "Children (go) door to door on October 31. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 바꾸기", "She buys a Greek god costume.", "3인칭 단수 buys (현재 시제)",
     "She (buy) a Greek god costume. → ___", instr="바꿔 쓰기")
f.ex("A2", "문장 바꾸기", "He does not like horror films.", "3인칭 단수 부정은 does not",
     "He (not / like) horror films. → ___", instr="바꿔 쓰기")
f.ex("B1", "문장 완성", "will rain", "I think → will은 추측",
     "I think it ___ (rain) on Halloween night.", instr="빈칸 채우기", size=23)
f.end_report()

# col 3
ix = COLX[3]
image(p, "halloween1912.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "« A Halloween Wish », 1912 : in the age of postcards, Halloween greetings travelled by mail — slowly, like little paper ghosts.",
              "Halloween postcard, 1912 — public domain")
v3 = Flow(p, [(ix, CW)], int(cy3) + 18, 2560, tag="P3-col3")
v3.box("FESTIVAL WORDS　축제 단어장", [
    ("trick or treat — 사탕 안 주면 장난쳐요", "serif", False, INK, 21.5, 1.5),
    ("a costume — 의상, 축제 분장", "serif", False, INK, 21.5, 1.5),
    ("a jack-o'-lantern — 호박 등", "serif", False, INK, 21.5, 1.5),
    ("a porch — 현관 앞 공간, 현관 계단", "serif", False, INK, 21.5, 1.5),
    ("to carve — 파다, 조각하다", "serif", False, INK, 21.5, 1.5),
    ("a decoration — 장식품", "serif", False, INK, 21.5, 1.5),
    ("spooky — 오싹한 (재미있는 쪽으로)", "serif", False, INK, 21.5, 1.5),
    ("a patch — 작은 땅 한 조각; (pumpkin patch 호박밭)", "serif", False, INK, 21.5, 1.5),
])
v3.box("DATES TO REMEMBER　이달의 날짜", [
    ("Oct 23 — Red Ribbon Week begins", "sans", True, OLIVE, 20, 1.4),
    ("Oct 24 — Make a Difference Day · Drug Take Back Day, 10 a.m.–2 p.m.", "serif", False, INK, 20.5, 1.4),
    ("Oct 31 — Halloween (Saturday)", "sans", True, OLIVE, 20, 1.4),
    ("Nov 1 — clocks fall back · Nov 3 — Election Day", "serif", False, INK, 20.5, 1.4),
], tsize=22)
v3.box("THE SEASON IN NUMBERS", [
    ("3,000+ — Halloween postcard designs printed in the early 1900s", "serif", False, INK, 21, 1.45),
    ("96% — of celebrants buy candy · 47% — now use AI for ideas", "serif", False, INK, 21, 1.45),
    ("$115.14 — projected spending per person (NRF)", "serif", False, INK, 21, 1.45),
])
v3.head("FUN, OR TOO MUCH ?", 23)
v3.para("Halloween now costs America more than ever — and the robots help us dress up. Is it still a festival, or is it a shopping week with ghosts ? Write to us in English, two or three sentences : your letter may appear on page 7 of VOL.2.", 21.5)
v3.expl("할로윈은 점점 비싸지고, AI까지 분장 고르기를 도와줘요. 할로윈은 아직 축제일까요, 유령이 붙은 쇼핑 주간일까요? 편지로 알려 주세요 (7면 독자 코너 참조).")
v3.end_report()
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　스포츠", "The Lucerna", "LEVEL B1　NBA　World Series　Austin F1")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P4-main")
f.title("The Biggest Sports Week of the Autumn", 32)
f.byline("By The Lucerna newsroom　Reading level : B1")
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
f.box("THE WEEK'S FIXTURES　이번 주 일정", [
    ("Tue — NBA tip-off : 76ers at Knicks · Thunder at Spurs", "serif", False, INK, 21, 1.42),
    ("Wed — Lakers vs Warriors · Thu — Patriots at Bears", "serif", False, INK, 21, 1.42),
    ("Fri — World Series Game 1, 8 p.m. ET · Sat — Game 2", "serif", False, INK, 21, 1.42),
    ("Sun — Austin Grand Prix · El Clásico, 4 p.m. ET", "serif", False, INK, 21, 1.42),
], tsize=21)
f.gloss("a banner 우승 깃발 · to sweep 전승하다 · the defending champion 디펜딩 챔프 · qualifying 예선 · a storyline 이야기 흐름.")
f.head("A　READING　읽기 객관식", 25)
f.ex("B1", "객관식", "A", "닉스의 지난 우승 배너는 1973년",
     "The Knicks' banner was their first since... A. 1973 · B. 1982 · C. 2003", size=22.5)
f.ex("B1", "객관식", "A", "106–100, 6점 차",
     "On opening night, Philadelphia won... A. by 6 points · B. by 16 points · C. after extra time", size=22.5)
f.ex("B1", "객관식", "B", "브루어스의 지난 월드시리즈는 1982년",
     "Milwaukee's last World Series before this year was in... A. 1973 · B. 1982 · C. 2020", size=22.5)
f.ex("B1", "객관식", "C", "F1 본경기는 일요일",
     "The Grand Prix race day is... A. Friday · B. Saturday · C. Sunday", size=22.5)
f.ex("B1", "객관식", "B", "출처 표기는 Week 7, Week 8이 아니에요",
     "The NFL games this week are in... A. Week 6 · B. Week 7 · C. Week 8", size=22.5)
f.head("B　SPORTS WORDS　단어 짝짓기", 25)
f.match_set("B1", "단어 짝짓기",
            ["tip-off", "a sweep", "the defending champion", "a banner"],
            ["the team that won last time, playing to keep the title",
             "winning every game in a series",
             "a flag in the arena that remembers a championship",
             "the start of a basketball game"],
            ["d", "b", "a", "c"],
            ["tip-off = 농구 경기 시작, d", "sweep = 시리즈 전 경기 승리, b", "defending champion = 디펜딩 챔프, a", "banner = 우승을 기념하는 깃발, c"],
            instr="단어와 뜻 짝짓기")
f.head("C　COMPARATIVES　비교급", 25)
f.ex("B1", "문장 완성", "older", "월드시리즈가 NBA보다 역사가 길어요",
     "The World Series is ___ (old) than the NBA.", instr="빈칸 채우기", size=22.5)
f.ex("B1", "문장 완성", "hotter", "hot → hotter (자음을 겹쳐 써요)",
     "Austin in October is ___ (hot) than Milwaukee.", instr="빈칸 채우기", size=22.5)
f.ex("B1", "문장 완성", "busiest", "최상급 the busiest",
     "This is the ___ (busy) sports week of the autumn.", instr="빈칸 채우기", size=22.5)
f.ex("B1", "문장 완성", "more", "Maxey 28점 > Brunson 21점",
     "Maxey scored ___ points than Brunson on Tuesday. (28 to 21)", instr="빈칸 채우기", size=22.5)
f.head("D　VERB FORMS　동사 과거형", 25)
f.ex("B1", "문장 바꾸기", "The 76ers won 106–100.", "win → won (불규칙)",
     "The 76ers (win) 106–100 on Tuesday. → ___", instr="바꿔 쓰기", size=23)
f.ex("B1", "문장 바꾸기", "The Knicks raised their banner.", "raise → raised (규칙)",
     "The Knicks (raise) their banner. → ___", instr="바꿔 쓰기", size=23)
f.ex("B1", "문장 바꾸기", "Milwaukee swept the Dodgers.", "sweep → swept (불규칙)",
     "Milwaukee (sweep) the Dodgers. → ___", instr="바꿔 쓰기", size=23)
f.ex("B1", "문장 바꾸기", "Tampa Bay beat Cleveland on Monday.", "beat → beat (불규칙)",
     "Tampa Bay (beat) Cleveland on Monday. → ___", instr="바꿔 쓰기", size=23)
f.ex("B1", "문장 바꾸기", "Fans watched three games on Tuesday night.", "watch → watched (규칙)",
     "Fans (watch) three games on Tuesday night. → ___", instr="바꿔 쓰기", size=23)
f.end_report()

# col 3
ix = COLX[3]
v4 = Flow(p, [(ix, CW)], 200, 2560, tag="P4-col3")
v4.box("THE KING'S NEW TEAM", [
    ("LeBron James begins his 24th season — a record — in a new shirt : Philadelphia. He arrived this summer, and on night one, his new team won on the champions' floor.", "serif", False, INK, 21.5, 1.45),
    ("제임스는 24번째 시즌(기록)을 필라델피아 유니폼으로 시작했고, 첫날 밤 챔피언의 홈에서 이겼어요.", "sans", False, GREY, 20.5, 1.4),
])
v4.box("SPORTS WORDS　스포츠 단어장", [
    ("tip-off — (농구) 경기 시작, 점프볼", "serif", False, INK, 21.5, 1.5),
    ("a banner — 우승 깃발", "serif", False, INK, 21.5, 1.5),
    ("to sweep — 전승하다 (시리즈 전 경기 승리)", "serif", False, INK, 21.5, 1.5),
    ("the defending champion — 디펜딩 챔프", "serif", False, INK, 21.5, 1.5),
    ("qualifying — 예선", "serif", False, INK, 21.5, 1.5),
    ("a race — 경기 한 번; (자동차) 레이스", "serif", False, INK, 21.5, 1.5),
    ("overtime — 연장전 (extra time)", "serif", False, INK, 21.5, 1.5),
    ("a fan — 팬", "serif", False, INK, 21.5, 1.5),
])
v4.box("THE WEEK IN NUMBERS", [
    ("43 — games in the NBA's first six days", "serif", False, INK, 21.5, 1.45),
    ("106–100 — Philadelphia's win in New York", "serif", False, INK, 21.5, 1.45),
    ("1973 — the Knicks' previous banner · 1982 — Milwaukee's last World Series", "serif", False, INK, 21.5, 1.45),
    ("24 — LeBron James's season number, a record", "serif", False, INK, 21.5, 1.45),
])
v4.head("WATCHING A GAME IN ENGLISH", 23)
v4.para("« What a shot ! » — 좋은 슛이에요!", 21.5, "serif", True, OLIVE)
v4.para("« They are up by six. » — 여섯 점 앞섰어요.", 21.5)
v4.para("« It is going down to the last minute. » — 마지막 1분까지 가요.", 21.5)
v4.para("« We were robbed ! » — 심판한테 당했어요! (졌을 때 장난으로 하는 팬들의 단골 말)", 21.5)
v4.box("THE DEBATE　토론", [
    ("Three finals in one week : the NBA begins, baseball ends, and the cars race in Austin. A feast for fans — or too much sport ? Tell us on page 7.", "serif", False, INK, 21.5, 1.45),
])
v4.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
