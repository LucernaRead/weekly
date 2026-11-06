# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.expanduser("~/workspace/goals/lucernaread-social-media-operations/files/weekly-report-w46-en-ja/svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE · カルチャー", "The Lucerna", "A2 → B1 · Friday at the movies · 金曜日の映画")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P3-main")
f.title("Friday Night at the Movies : Scrooge Comes Early", 37)
f.byline("By The Lucerna newsroom · Reading level : A2 → B1")
f.para("On Friday, November 13, a ghost comes to the cinema — early. « Ebenezer » is a dark new telling of Charles Dickens's « A Christmas Carol », with Johnny Depp as Ebenezer Scrooge, the miser who hates Christmas. Christmas is still six weeks away. The film does not wait.")
f.para("Dickens wrote the story in 1843, in London. Scrooge is visited in one night by three ghosts : the Ghost of Christmas Past, the Ghost of Christmas Present, and the Ghost of Christmas Yet to Come. By morning, the cold old man is warm again. The book made Christmas what it is in Britain — and the films keep remaking it.")
f.para("The second film of the week is very different. « How to Rob a Bank » is a heist comedy : bank robbers who film their crimes and post them online. The police follow the likes. It is fast, funny and very 2026 — crime as content.")
f.para("Which film would you choose ? A ghost story in Dickens's London, or a bank story on today's internet ? In our newsroom, the vote is split again — half for the ghost, half for the bank. Tell us your choice on page 7.")
f.box("COMING SOON · 近日公開", [
    ("Fri Nov 20 — « The Hunger Games : Sunrise on the Reaping » opens in cinemas. Fri Nov 27 — Disney's « Hexed » arrives.", "serif", False, INK, 21.5, 1.4),
    ("Sun Nov 15 — the ATP Finals begin in Turin. Fri Nov 13 — Children in Need, live from Salford.", "serif", False, INK, 21.5, 1.4),
    ("One week, one screen, many stories — and Christmas is coming, one film at a time.", "serif", False, INK, 21.5, 1.4),
])
f.para("A film is not only a story — it is also English practice. Listen for three things : the catchphrase (the line everybody repeats), the joke (why does the room laugh ?), and the ending (happy, sad, or open ?). After the film, try to tell the story in five English sentences.", 23.5)
f.para("And if you stay at home, the same rule works for a series : one episode, five sentences, in English. The best five-sentence reviews will be printed in VOL.4 — send yours to the newsroom.", 23.5)
f.gloss("a miser けちん坊 · a ghost 幽霊 · a heist 強盗事件 · yet to come まだ来ていない。")
f.head("A · COMPREHENSION", 25)
f.bridge("3ページの記事を読んで、正しい答えを選びなさい。")
f.ex("A2", "選択", "B", "『Ebenezer』11月13日金曜日公開",
     "« Ebenezer » opens on... A. November 11 · B. Friday, November 13 · C. November 15", size=22)
f.ex("A2", "選択", "A", "ジョニー・デップがスクルージを演じる",
     "Scrooge is played by... A. Johnny Depp · B. Charles Dickens · C. John Leech", size=22)
f.ex("A2", "選択", "C", "物語は1843年に書かれた",
     "Dickens wrote the story in... A. 1918 · B. 1920 · C. 1843", size=22)
f.ex("B1", "選択", "B", "3人の幽霊が一夜のうちに訪れる",
     "Scrooge is visited by... A. one ghost · B. three ghosts · C. five ghosts", size=22)
f.ex("B1", "選択", "A", "強盗たちは犯行をネットに投稿する",
     "In « How to Rob a Bank », the robbers... A. post their crimes online · B. rob a ghost · C. hate Christmas", size=22)
f.ex("B1", "選択", "C", "『ハンガー・ゲーム』新作、11月20日公開",
     "« The Hunger Games : Sunrise on the Reaping » opens on... A. November 13 · B. November 15 · C. November 20", size=22)
f.head("B · SENTENCES", 25)
f.bridge("与えられた語で文を完成させなさい。")
f.ex("A2", "文の完成", "opens", "open = 公開される（三人称単数 + s）",
     "The film ___ on Friday, November 13.", instr="空所補充")
f.ex("A2", "文の完成", "miser", "miser = けちん坊",
     "Scrooge is a ___ who hates Christmas.", instr="空所補充")
f.ex("B1", "文の完成", "split", "split = 分かれた",
     "In our newsroom, the vote is ___ : half ghost, half bank.", instr="空所補充")
f.ex("B1", "文の完成", "ghost", "ghost = 幽霊",
     "Marley's ___ visits Scrooge at night.", instr="空所補充")
f.head("C · THE WORDS", 25)
f.match_set("A2", "語彙マッチング",
            ["a miser", "a ghost", "a heist", "a catchphrase"],
            ["a line everybody repeats",
             "a person who loves money and hates spending it",
             "the spirit of a dead person",
             "a robbery, usually of a bank"],
            ["b", "c", "d", "a"],
            ["miser = けちん坊 b", "ghost = 幽霊 c", "heist = 強盗事件 d", "catchphrase = 決めぜりふ a"],
            instr="語と意味を結ぶ")
f.head("D · PAST SIMPLE", 25)
f.bridge("過去形で書きかえよう（起きたこと）。")
f.ex("A2", "文型変換", "Dickens wrote the story in 1843.", "write → wrote",
     "Dickens (write) the story in 1843. → ___", instr="書きかえ")
f.ex("A2", "文型変換", "The ghosts visited Scrooge in one night.", "visit → visited",
     "The ghosts (visit) Scrooge in one night. → ___", instr="書きかえ")
f.ex("B1", "文型変換", "Scrooge became warm again by morning.", "become → became",
     "Scrooge (become) warm again by morning. → ___", instr="書きかえ")
f.ex("B1", "文型変換", "She chose the ghost story.", "choose → chose",
     "She (choose) the ghost story. → ___", instr="書きかえ")
f.end_report()

# col 3: image + side flow
ix = COLX[3]
image(p, "marley.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "A ghost in art : Marley's Ghost visits Scrooge, in John Leech's illustration for Dickens's « A Christmas Carol » (1843). Not film art — but this week, every ghost is a star.",
              "John Leech — public domain, via Wikimedia Commons")
v3 = Flow(p, [(ix, CW)], int(cy3) + 18, 2540, tag="P3-col3")
v3.box("SCROOGE'S NIGHT · スクルージの夜", [
    ("Three ghosts, one night : Past, Present, and Yet to Come. By morning, Scrooge is a new man — and Christmas is saved, six weeks early.", "serif", False, INK, 21.5, 1.42),
])
v3.head("FIVE SENTENCES", 25)
v3.para("After any film or episode, tell the story in five English sentences : who, where, what happened, the surprise, the ending. Five sentences are enough — and they are excellent practice.", 22)
v3.para("Example : « A ghost comes to a house. A miser is cold and alone. Three ghosts visit him. He sees his past, his present and his future. Then he is warm again. » Now it is your turn.", 22)
v3.bridge("5文レビュー｜who、where、何が起きたか、転換、結末——5文で十分。")
v3.end_report()
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT · スポーツ", "The Lucerna", "LEVEL B1 · NFL · ATP · Nations League")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2540, tag="P4-main")
f.title("Sunday in Munich, Turin and Madrid", 37)
f.byline("By The Lucerna newsroom · Reading level : B1")
f.para("Sunday, November 15, is the biggest sports day of the autumn. Three cities, three sports, one Sunday — and American football in the home of Bayern Munich.")
f.para("In Munich, the NFL plays at the Allianz Arena : the Detroit Lions, the home team, against the New England Patriots. The game starts at 3:30 p.m. local time — 9:30 a.m. in New York. It is the Lions' first game in Germany, and a special game for their German-American star, Amon-Ra St. Brown, whose mother is German. The game is part of NFL Week 10, and it is the week's most talked-about fixture.")
f.para("Back in the United States, Week 10 continues the same day : the Chiefs play the Falcons in Atlanta, the Vikings play the Packers at Lambeau Field, and the 49ers play the Cowboys in Arlington. The week began on Thursday, November 12, with the Commanders at the Giants, and ends on Monday, November 16, with the Chargers at the Ravens.")
f.para("In Turin, Italy, tennis begins its season finale : the ATP Finals, from Sunday, November 15, to Sunday, November 22. The eight best singles players of the year play in two groups of four, and the final is on November 22. The field was settled on Monday, November 9, after the Paris Masters.")
f.para("And in Madrid, football takes the stage : Spain play England in the Nations League on Sunday night, three days after England play Croatia at Wembley on Thursday, November 12. Scotland play North Macedonia at Hampden Park on Friday, November 13. One Sunday is not enough — good thing the week has seven days.")
f.box("WHY MUNICH ? · なぜミュンヘンか", [
    ("The NFL plays games outside the United States every year, so new fans can see the sport live. Munich hosted NFL games in 2022 and 2024, and will host again in 2028. This year there are nine international games in all — a record.", "serif", False, INK, 21.5, 1.4),
])
f.para("How do you follow three sports in one day ? Choose one game to watch fully, and follow the others on your phone. That is the modern fan : one screen for the game, one screen for the scores.", 23.5)
f.para("The Allianz Arena holds 70,000 people — bigger than most NFL stadiums. And next week ? The Ashes begin : Australia against England in the first Test in Perth, from Saturday, November 21. Cricket's oldest rivalry, back in Australia. The weekend starts on Sunday — and it does not stop.", 23.5)
f.gloss("a fixture 1試合（日程） · a group グループ · a finale 決勝・最終戦 · a star スター選手。")
f.head("A · COMPREHENSION", 25)
f.bridge("4ページの記事を読んで、正しい答えを選びなさい。")
f.ex("B1", "選択", "A", "ミュンヘン戦：ペイトリオッツ対ライオンズ",
     "In Munich, the Lions play... A. the Patriots · B. the Falcons · C. Bayern Munich", size=22)
f.ex("B1", "選択", "C", "ミュンヘンのキックオフは現地時間15:30",
     "The Munich game starts at... A. 9:30 a.m. Munich time · B. 7:45 p.m. · C. 3:30 p.m. local time", size=22)
f.ex("B1", "選択", "B", "ATPファイナルズはトリノで開催",
     "The ATP Finals are in... A. Paris · B. Turin · C. Madrid", size=22)
f.ex("B1", "選択", "A", "イングランド対クロアチア、11月12日木曜日",
     "England play Croatia on... A. Thursday, November 12 · B. Friday, November 13 · C. Sunday, November 15", size=22)
f.ex("B1", "選択", "C", "スコットランド対北マケドニア",
     "Scotland play... A. Spain · B. Croatia · C. North Macedonia", size=22)
f.ex("B1", "選択", "B", "第10週のマンデーナイト：チャージャーズ対レイブンズ",
     "Week 10 ends with... A. Commanders at Giants · B. Chargers at Ravens · C. 49ers at Cowboys", size=22)
f.head("B · SENTENCES", 25)
f.bridge("与えられた語で文を完成させなさい。")
f.ex("B1", "文の完成", "hosts", "host の三人称単数 hosts",
     "The Allianz Arena ___ the NFL on Sunday.", instr="空所補充")
f.ex("B1", "文の完成", "begin", "4ページの本文と同じ、動詞は複数形",
     "The ATP Finals ___ on Sunday, November 15.", instr="空所補充")
f.ex("A2", "文の完成", "bigger", "big → bigger",
     "The Allianz Arena is ___ than most NFL stadiums.", instr="空所補充")
f.ex("A2", "文の完成", "eight", "8人 = eight",
     "___ singles players play in Turin.", instr="空所補充")
f.head("C · THE WORDS", 25)
f.match_set("B1", "語彙マッチング",
            ["a fixture", "a group", "a finale", "a star"],
            ["a famous player, loved by the fans",
             "a game in a season's schedule",
             "the last event of a season",
             "a small set of players who play each other"],
            ["b", "d", "c", "a"],
            ["fixture = 日程の1試合 b", "group = グループ d", "finale = 最終戦 c", "star = スター選手 a"],
            instr="語と意味を結ぶ")
f.head("D · PAST SIMPLE", 25)
f.bridge("過去形で書きかえよう（試合は終わった）。")
f.ex("B1", "文型変換", "The Lions played in Munich on Sunday.", "play → played",
     "The Lions (play) in Munich on Sunday. → ___", instr="書きかえ")
f.ex("B1", "文型変換", "She watched the tennis in Turin.", "watch → watched",
     "She (watch) the tennis in Turin. → ___", instr="書きかえ")
f.ex("B1", "文型変換", "They followed the scores on their phones.", "follow → followed",
     "They (follow) the scores on their phones. → ___", instr="書きかえ")
f.ex("B1", "文型変換", "He chose one game to watch fully.", "choose → chose",
     "He (choose) one game to watch fully. → ___", instr="書きかえ")
f.end_report()

# col 3: image + fixtures
ix = COLX[3]
image(p, "football1910.jpg", ix, 200, CW, 470)
cy4 = caption(p, ix, 670, CW, "American football in 1910 : Miami against Wittenberg. The helmets were leather, the fields were mud — but the game was already America's game. This week, the game goes to Munich.",
              "Frank R. Snyder — public domain, via Wikimedia Commons")
v4 = Flow(p, [(ix, CW)], int(cy4) + 18, 2540, tag="P4-col3")
v4.box("SUNDAY, NOVEMBER 15 · 日曜の試合", [
    ("NFL : Patriots–Lions, Munich (Allianz Arena), 3:30 p.m. local time.", "serif", False, INK, 21.5, 1.42),
    ("ATP Finals begin, Turin. Nations League : Spain–England, Madrid, 7:45 p.m.", "serif", False, INK, 21.5, 1.42),
    ("THURSDAY, NOVEMBER 12 : England–Croatia, Wembley. FRIDAY, NOVEMBER 13 : Scotland–North Macedonia, Hampden.", "serif", False, INK, 21.5, 1.42),
    ("MONDAY, NOVEMBER 16 : Chargers–Ravens close NFL Week 10.", "serif", False, INK, 21.5, 1.42),
])
v4.head("ONE SCREEN, TWO SCREENS", 25)
v4.para("The modern fan watches one game fully and follows the others on a phone. Try it in English : « The score is 14–10. » « Who scored ? » « Munich is winning ! » — short sentences, live English.", 22)
v4.bridge("観戦英語｜スコア、誰が得点したか、誰がリードしているか——短い文こそ実況英語。")
v4.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
