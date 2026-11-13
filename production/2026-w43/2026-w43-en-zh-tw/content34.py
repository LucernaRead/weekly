# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE　文化", "The Lucerna", "A2 → B1　Halloween in America　萬聖節")

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
f.box("SAY IT ON THE NIGHT　當晚這樣說", [
    ("« Trick or treat ! » — 不給糖，就搗蛋！（開玩笑的威脅，永遠換來糖果）", "serif", False, INK, 21.5, 1.42),
    ("« Happy Halloween ! » — 萬聖節快樂！ · « Thank you ! » — 謝謝！（拿到糖果一定要說）", "serif", False, INK, 21.5, 1.42),
    ("« What are you dressed as ? » — 你扮的是什麼？", "serif", False, INK, 21.5, 1.42),
], tsize=22)
f.gloss("講解｜to celebrate 慶祝 · a porch 門廊 · to carve 雕刻 · a decoration 裝飾 · a survey 調查（NRF 調查 7,889 人）。")
f.head("A　TRUE OR FALSE ?　判斷對錯", 25)
f.expl("讀第 3 版文章，判斷對錯。")
f.ex("A2", "閱讀判斷", "False", "萬聖節在週六（10 月 31 日）",
     "1. Halloween is on a Friday this year.", instr="判斷", size=23)
f.ex("A2", "閱讀判斷", "True", "NRF 預測 135 億美元",
     "2. Americans will spend about $13.5 billion on Halloween.", instr="判斷", size=23)
f.ex("B1", "閱讀判斷", "False", "最大宗是服裝 44 億，不是糖果",
     "3. Candy is the biggest part of the spending.", instr="判斷", size=23)
f.ex("A2", "閱讀判斷", "True", "47% 的人用 AI 工具找靈感",
     "4. Almost half of celebrants use AI tools for costume ideas.", instr="判斷", size=23)
f.ex("A2", "閱讀判斷", "False", "門廊熄燈 = 今年請勿打擾",
     "5. A house with no light on the porch is asking for visitors.", instr="判斷", size=23)
f.head("B　FESTIVAL WORDS　節日詞填空", 24)
f.ex("A2", "完成句子", "costume", "costume = 戲服、裝扮",
     "Children wear a ___ and go from door to door.", instr="填空", size=23)
f.ex("A2", "完成句子", "carve", "carve a pumpkin 刻南瓜",
     "You ___ a pumpkin to make a jack-o'-lantern.", instr="填空", size=23)
f.ex("A2", "完成句子", "porch", "porch = 門廊",
     "Families leave a light on the ___ to welcome children.", instr="填空", size=23)
f.ex("A2", "完成句子", "candy", "96% 的人買糖果",
     "Ninety-six percent of celebrants buy ___.", instr="填空", size=23)
f.ex("A2", "完成句子", "patch", "pumpkin patch = 南瓜田",
     "In October, families visit a pumpkin ___ to choose a pumpkin.", instr="填空", size=23)
f.head("C　CHOOSE　單選", 25)
f.ex("B1", "單選", "B", "135 億是今年預測數",
     "The $13.5 billion is... A. last year's total · B. this year's projection · C. candy money only", size=22.5)
f.ex("B1", "單選", "A", "谷歌榜名 Frightgeist",
     "Google's costume list is called... A. Frightgeist · B. Spiritgeist · C. Trendlist", size=22.5)
f.ex("B1", "單選", "B", "今年流行希臘神祇",
     "This year's costumes include... A. Roman kings · B. Greek gods · C. astronauts only", size=22.5)
f.ex("B1", "單選", "B", "20 世紀初靠明信片送祝福",
     "In the early 1900s, Halloween greetings travelled by... A. telephone · B. postcard · C. radio", size=22.5)
f.head("D　SENTENCES　句子變形", 25)
f.ex("A2", "句型轉換", "Children go door to door on October 31.", "一般現在時表習慣",
     "Children (go) door to door on October 31. → ___", instr="改寫")
f.ex("B1", "句型轉換", "She buys a Greek god costume.", "三單 buys（一般現在時）",
     "She (buy) a Greek god costume. → ___", instr="改寫")
f.ex("A2", "句型轉換", "He does not like horror films.", "三單否定 does not",
     "He (not / like) horror films. → ___", instr="改寫")
f.ex("B1", "完成句子", "will rain", "I think → will 表推測",
     "I think it ___ (rain) on Halloween night.", instr="填空", size=23)
f.end_report()

# col 3
ix = COLX[3]
image(p, "halloween1912.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "« A Halloween Wish », 1912 : in the age of postcards, Halloween greetings travelled by mail — slowly, like little paper ghosts.",
              "Halloween postcard, 1912 — public domain")
v3 = Flow(p, [(ix, CW)], int(cy3) + 18, 2560, tag="P3-col3")
v3.box("FESTIVAL WORDS　節日詞表", [
    ("trick or treat — 不給糖就搗蛋", "serif", False, INK, 21.5, 1.5),
    ("a costume — 戲服、節日裝扮", "serif", False, INK, 21.5, 1.5),
    ("a jack-o'-lantern — 南瓜燈", "serif", False, INK, 21.5, 1.5),
    ("a porch — 門廊、門前台階", "serif", False, INK, 21.5, 1.5),
    ("to carve — 雕刻、刻", "serif", False, INK, 21.5, 1.5),
    ("a decoration — 裝飾品", "serif", False, INK, 21.5, 1.5),
    ("spooky — 陰森的（好玩的那種）", "serif", False, INK, 21.5, 1.5),
    ("a patch — 一片地；（pumpkin patch 南瓜田）", "serif", False, INK, 21.5, 1.5),
])
v3.box("DATES TO REMEMBER　本月日曆", [
    ("Oct 23 — Red Ribbon Week begins", "sans", True, OLIVE, 20, 1.4),
    ("Oct 24 — Make a Difference Day · Drug Take Back Day, 10 a.m.–2 p.m.", "serif", False, INK, 20.5, 1.4),
    ("Oct 31 — Halloween (Saturday)", "sans", True, OLIVE, 20, 1.4),
    ("Nov 1 — clocks fall back · Nov 3 — Election Day", "serif", False, INK, 20.5, 1.4),
])
v3.box("THE SEASON IN NUMBERS", [
    ("3,000+ — Halloween postcard designs printed in the early 1900s", "serif", False, INK, 21, 1.45),
    ("96% — of celebrants buy candy · 47% — now use AI for ideas", "serif", False, INK, 21, 1.45),
    ("$115.14 — projected spending per person (NRF)", "serif", False, INK, 21, 1.45),
])
v3.head("FUN, OR TOO MUCH ?", 23)
v3.para("Halloween now costs America more than ever — and the robots help us dress up. Is it still a festival, or is it a shopping week with ghosts ? Write to us in English, two or three sentences : your letter may appear on page 7 of VOL.2.", 21.5)
v3.expl("萬聖節越來越貴，AI 還來幫你選裝扮：它還是節日，還是帶鬼的購物週？寫信告訴我們（見第 7 版讀者園地）。")
v3.end_report()
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　體育", "The Lucerna", "LEVEL B1　NBA　World Series　Austin F1")

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
f.box("THE WEEK'S FIXTURES　本週賽程", [
    ("Tue — NBA tip-off : 76ers at Knicks · Thunder at Spurs", "serif", False, INK, 21, 1.42),
    ("Wed — Lakers vs Warriors · Thu — Patriots at Bears", "serif", False, INK, 21, 1.42),
    ("Fri — World Series Game 1, 8 p.m. ET · Sat — Game 2", "serif", False, INK, 21, 1.42),
    ("Sun — Austin Grand Prix · El Clásico, 4 p.m. ET", "serif", False, INK, 21, 1.42),
])
f.gloss("講解｜a banner 冠軍旗幟 · to sweep 橫掃 · the defending champion 衛冕冠軍 · qualifying 排位賽 · a storyline 故事線。")
f.head("A　READING　閱讀單選", 25)
f.ex("B1", "單選", "A", "尼克上一次冠軍旗幟是 1973 年",
     "The Knicks' banner was their first since... A. 1973 · B. 1982 · C. 2003", size=22.5)
f.ex("B1", "單選", "A", "106–100，相差 6 分",
     "On opening night, Philadelphia won... A. by 6 points · B. by 16 points · C. after extra time", size=22.5)
f.ex("B1", "單選", "B", "釀酒人上次進世界大賽是 1982 年",
     "Milwaukee's last World Series before this year was in... A. 1973 · B. 1982 · C. 2020", size=22.5)
f.ex("B1", "單選", "C", "F1 正賽在週日",
     "The Grand Prix race day is... A. Friday · B. Saturday · C. Sunday", size=22.5)
f.ex("B1", "單選", "B", "來源標註 Week 7，不要寫成 Week 8",
     "The NFL games this week are in... A. Week 6 · B. Week 7 · C. Week 8", size=22.5)
f.head("B　SPORTS WORDS　體育詞配對", 25)
f.match_set("B1", "詞彙配對",
            ["tip-off", "a sweep", "the defending champion", "a banner"],
            ["the team that won last time, playing to keep the title",
             "winning every game in a series",
             "a flag in the arena that remembers a championship",
             "the start of a basketball game"],
            ["d", "b", "a", "c"],
            ["tip-off=籃球開賽 d", "sweep=贏下系列賽每一場 b", "defending champion=衛冕者 a", "banner=紀念冠軍的旗幟 c"],
            instr="把詞和釋義配對")
f.head("C　COMPARATIVES　比較級", 25)
f.ex("B1", "完成句子", "older", "World Series 歷史比 NBA 久",
     "The World Series is ___ (old) than the NBA.", instr="填空", size=22.5)
f.ex("B1", "完成句子", "hotter", "hot → hotter（重讀閉音節雙寫）",
     "Austin in October is ___ (hot) than Milwaukee.", instr="填空", size=22.5)
f.ex("B1", "完成句子", "busiest", "最高級 the busiest",
     "This is the ___ (busy) sports week of the autumn.", instr="填空", size=22.5)
f.ex("B1", "完成句子", "more", "Maxey 28 分 > Brunson 21 分",
     "Maxey scored ___ points than Brunson on Tuesday. (28 to 21)", instr="填空", size=22.5)
f.head("D　VERB FORMS　動詞過去式", 25)
f.ex("B1", "句型轉換", "The 76ers won 106–100.", "win → won（不規則）",
     "The 76ers (win) 106–100 on Tuesday. → ___", instr="改寫", size=23)
f.ex("B1", "句型轉換", "The Knicks raised their banner.", "raise → raised（規則）",
     "The Knicks (raise) their banner. → ___", instr="改寫", size=23)
f.ex("B1", "句型轉換", "Milwaukee swept the Dodgers.", "sweep → swept（不規則）",
     "Milwaukee (sweep) the Dodgers. → ___", instr="改寫", size=23)
f.ex("B1", "句型轉換", "Tampa Bay beat Cleveland on Monday.", "beat → beat（不規則）",
     "Tampa Bay (beat) Cleveland on Monday. → ___", instr="改寫", size=23)
f.ex("B1", "句型轉換", "Fans watched three games on Tuesday night.", "watch → watched（規則）",
     "Fans (watch) three games on Tuesday night. → ___", instr="改寫", size=23)
f.end_report()

# col 3
ix = COLX[3]
v4 = Flow(p, [(ix, CW)], 200, 2560, tag="P4-col3")
v4.box("THE KING'S NEW TEAM", [
    ("LeBron James begins his 24th season — a record — in a new shirt : Philadelphia. He arrived this summer, and on night one, his new team won on the champions' floor.", "serif", False, INK, 21.5, 1.45),
    ("詹姆斯第 24 季（紀錄）改穿費城球衣，首夜就在冠軍主場取勝。", "sans", False, GREY, 20.5, 1.4),
])
v4.box("SPORTS WORDS　體育詞表", [
    ("tip-off — （籃球）開賽、跳球", "serif", False, INK, 21.5, 1.5),
    ("a banner — 冠軍旗幟", "serif", False, INK, 21.5, 1.5),
    ("to sweep — 橫掃（全勝贏下系列賽）", "serif", False, INK, 21.5, 1.5),
    ("the defending champion — 衛冕冠軍", "serif", False, INK, 21.5, 1.5),
    ("qualifying — 排位賽", "serif", False, INK, 21.5, 1.5),
    ("a race — 一場比賽；（賽車）賽事", "serif", False, INK, 21.5, 1.5),
    ("overtime — 加時（extra time）", "serif", False, INK, 21.5, 1.5),
    ("a fan — 球迷、粉絲", "serif", False, INK, 21.5, 1.5),
])
v4.box("THE WEEK IN NUMBERS", [
    ("43 — games in the NBA's first six days", "serif", False, INK, 21.5, 1.45),
    ("106–100 — Philadelphia's win in New York", "serif", False, INK, 21.5, 1.45),
    ("1973 — the Knicks' previous banner · 1982 — Milwaukee's last World Series", "serif", False, INK, 21.5, 1.45),
    ("24 — LeBron James's season number, a record", "serif", False, INK, 21.5, 1.45),
])
v4.head("WATCHING A GAME IN ENGLISH", 23)
v4.para("« What a shot ! » — 好球！", 21.5, "serif", True, OLIVE)
v4.para("« They are up by six. » — 他們領先六分。", 21.5)
v4.para("« It is going down to the last minute. » — 要拚到最後一分鐘。", 21.5)
v4.para("« We were robbed ! » — 我們被裁判坑了！（球迷口頭禪，輸球時說，帶玩笑）", 21.5)
v4.box("THE DEBATE　討論", [
    ("Three finals in one week : the NBA begins, baseball ends, and the cars race in Austin. A feast for fans — or too much sport ? Tell us on page 7.", "serif", False, INK, 21.5, 1.45),
])
v4.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
