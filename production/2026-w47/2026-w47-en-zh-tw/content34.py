# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P3 · CULTURE (A2→B1) =================
CURPAGE[0] = 3
p = BSPage4()
p.band("CULTURE　文化", "The Lucerna", "A2 → B1　Friday at the movies　週五看電影")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P3-main")
f.title("Friday at the Movies: Haymitch Goes Back to the Arena", 32)
f.byline("By The Lucerna newsroom　Reading level: A2 → B1")
f.para("On Friday, November 20, a familiar name returns to the cinema: Haymitch Abernathy. “The Hunger Games: Sunrise on the Reaping” tells the story of the young Haymitch — sixteen years old, from District 12 — in the 50th Hunger Games, the Second Quarter Quell, when twice as many young people were sent into the arena.")
f.para("The film is based on the novel by Suzanne Collins, published in 2025. Joseph Zada plays the young Haymitch. McKenna Grace plays Maysilee Donner, his fellow tribute from District 12. Ralph Fiennes plays the young President Snow. Francis Lawrence, who directed the earlier Hunger Games films, directs this one too.")
f.para("Fans of the first films will know what happens next: Haymitch wins the 50th Games — and becomes the tired, funny, clever mentor of the later stories, played in the first films by Woody Harrelson. This film shows how he got there: a boy from District 12, in the cruellest Games of all.")
f.para("And on the small screen? On Monday, November 16, at 9 p.m., “I'm a Celebrity... Get Me Out of Here!” returns to ITV1 and ITVX. Ant and Dec are back in the Australian jungle, near Murwillumbah in New South Wales. The launch is a day later than usual — because England play Spain in the Nations League on Sunday, November 15. ITV has not confirmed the campmates yet: the names will come a few days before the launch.")
f.para("Two jungles, one week: a painted jungle in the cinema, and a real jungle on television. In one, the prize is survival. In the other, the prize is the public's vote — and the title of King or Queen of the Jungle.")
f.box("COMING SOON　即將上映", [
    ("Fri Nov 20 — “The Hunger Games: Sunrise on the Reaping” opens in cinemas. The album of songs from the film arrives a week earlier, on Nov 13.", "serif", False, INK, 21.5, 1.4),
    ("Mon Nov 16 — “I'm a Celebrity” opens on ITV1, 9 p.m. “Unpacked”, the companion show, is on ITV2.", "serif", False, INK, 21.5, 1.4),
    ("Sun Nov 15 — “How to Survive the Jungle”, a one-off special, before the launch.", "serif", False, INK, 21.5, 1.4),
])
f.para("A film is not only a story — it is also English practice. Listen for three things: the catchphrase (the line everybody repeats), the joke (why does the room laugh?), and the ending (happy, sad, or open?). After the film, try to tell the story in five English sentences.", 23.5)
f.para("And if you stay at home, the same rule works for a series: one episode, five sentences, in English. The best five-sentence reviews will be printed in VOL.5 — send yours to the newsroom.", 23.5)
f.gloss("a tribute = 被選中的參賽者 · a mentor = 導師 · the arena = 競技場 · a campmate = 營地成員。")
f.head("A　COMPREHENSION", 25)
f.bridge("讀第 3 版文章，選出正確答案。")
f.ex("A2", "單選", "B", "《飢餓遊戲》新片11月20日週五上映",
     "“Sunrise on the Reaping” opens on... A. November 16 · B. Friday, November 20 · C. November 22", size=22)
f.ex("A2", "單選", "A", "約瑟夫·扎達飾演年輕的海米奇",
     "The young Haymitch is played by... A. Joseph Zada · B. Woody Harrelson · C. Ralph Fiennes", size=22)
f.ex("A2", "單選", "C", "第50屆飢餓遊戲，參賽人數翻倍",
     "The 50th Games, the Second Quarter Quell, sent... A. half as many tributes · B. the same number · C. twice as many young people", size=22)
f.ex("B1", "單選", "B", "拉爾夫·費因斯飾演年輕的斯諾總統",
     "The young President Snow is played by... A. Francis Lawrence · B. Ralph Fiennes · C. McKenna Grace", size=22)
f.ex("B1", "單選", "A", "叢林節目11月16日週一晚9點開播",
     "“I'm a Celebrity” returns on... A. Monday, November 16, at 9 p.m. · B. Sunday, November 15 · C. Friday, November 20", size=22)
f.ex("B1", "單選", "C", "開播推遲一天是因為英格蘭對西班牙的比賽",
     "The launch is a day late because... A. of the rain · B. of the film · C. England play Spain on Sunday, November 15", size=22)
f.head("B　SENTENCES", 25)
f.bridge("用所給詞補全句子。")
f.ex("A2", "完成句子", "opens", "open = 上映（第三人稱單數加 s）",
     "The film ___ on Friday, November 20.", instr="填空")
f.ex("A2", "完成句子", "mentor", "mentor = 導師",
     "Haymitch becomes the ___ of the later stories.", instr="填空")
f.ex("B1", "完成句子", "twice", "twice = 兩倍",
     "The 50th Games sent ___ as many young people.", instr="填空")
f.ex("B1", "完成句子", "jungle", "jungle = 叢林",
     "Ant and Dec are back in the Australian ___.", instr="填空")
f.head("C　THE WORDS", 25)
f.match_set("A2", "詞彙配對",
            ["a tribute", "a mentor", "the arena", "a campmate"],
            ["a person who teaches and guides you",
             "a person chosen to take part in the Games",
             "a person who lives with you in the jungle camp",
             "the place where the Games are fought"],
            ["b", "a", "d", "c"],
            ["tribute=參賽者 b", "mentor = 導師 a", "arena=競技場 d", "campmate=營地成員 c"],
            instr="把詞和釋義配對")
f.head("D　PAST SIMPLE", 25)
f.bridge("用一般過去時改寫（已經發生的事）。")
f.ex("A2", "句型轉換", "Collins published the novel in 2025.", "publish → published",
     "Collins (publish) the novel in 2025. → ___", instr="改寫")
f.ex("A2", "句型轉換", "Haymitch won the 50th Games.", "win → won",
     "Haymitch (win) the 50th Games. → ___", instr="改寫")
f.ex("B1", "句型轉換", "Rousseau painted jungles he never saw.", "paint → painted",
     "Rousseau (paint) jungles he never saw. → ___", instr="改寫")
f.ex("B1", "句型轉換", "ITV chose Monday for the launch.", "choose → chose",
     "ITV (choose) Monday for the launch. → ___", instr="改寫")
f.end_report()

# col 3: image + side flow
ix = COLX[3]
image(p, "tiger.jpg", ix, 200, CW, 470)
cy3 = caption(p, ix, 670, CW, "A tiger in a painted jungle: Henri Rousseau's “Surprised!” (1891). Rousseau never left France — he painted his jungles from books and the botanical garden in Paris.",
              "Henri Rousseau — public domain, via Wikimedia Commons")
v3 = Flow(p, [(ix, CW)], int(cy3) + 18, 2560, tag="P3-col3")
v3.box("HAYMITCH'S GAMES　海米奇的比賽", [  # D5: tsize 23->21, +17.8px over
    ("The 50th Games: twice as many tributes as usual — four from each district, not two. The winner: a sixteen-year-old boy from District 12.", "serif", False, INK, 21.5, 1.42),
], tsize=21)
v3.head("FIVE SENTENCES", 25)
v3.para("After any film or episode, tell the story in five English sentences: who, where, what happened, the surprise, the ending. Five sentences are enough — and they are excellent practice.", 22)
v3.para("Example: “A boy goes to the arena. The Games are cruel and long. He makes a friend and loses her. He wins with a trick, not with force. Then he goes home — changed.” Now it is your turn.", 22)
v3.bridge("五句影評｜who、where、發生了什麼、轉折、結局——五句就夠。")
v3.end_report()
p.foot(3)
p.save(f"{OUT}/p3-culture.svg")
print("P3 saved, exercises so far:", len(REG))

# ================= P4 · SPORT (B1) =================
CURPAGE[0] = 4
p = BSPage4()
p.band("SPORT　體育", "The Lucerna", "LEVEL B1　Ashes　Premier League　ATP")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P4-main")
f.title("Perth, One Year On: How Australia Kept the Ashes", 32)
f.byline("By The Lucerna newsroom　Reading level: B1")
f.para("A year ago, the Ashes came to Perth. On Friday, November 21, 2025, Australia played England in the first Test at Perth Stadium — the first Ashes Test at the ground. Australia won in two days, by eight wickets. It was the shortest Ashes Test, by balls bowled, since 1888.")
f.para("The series ran from November 21, 2025, to January 8, 2026. Australia won the first three Tests — in Perth, in Brisbane and in Adelaide — and kept the Ashes after the third Test. England won the fourth Test, in Melbourne, by four wickets: their first Test win in Australia for almost fifteen years. Australia won the fifth Test, in Sydney, by five wickets. The final score was 4–1.")
f.para("Australia had problems before the first Test. Their captain, Pat Cummins, was out with a back injury, and the fast bowler Josh Hazlewood was out with a hamstring injury. Steve Smith led the side instead. Scott Boland played, and the young fast bowler Brendan Doggett played his first Test.")
f.para("England's team was more settled. Ben Stokes was the captain. Joe Root, the batter England needed most, was in the team, with Jofra Archer and Mark Wood to bowl fast. England had not won a Test series in Australia since 2010–11 — they lost 4–0 on their last two tours, in 2017–18 and 2021–22. The last series, in England in 2023, was drawn.")
f.para("One Test lasts up to five days — but two Tests in this series lasted only two. The first Test in Perth ended in two days, and so did the fourth Test in Melbourne. The Ashes are not a sport for early nights.")
f.para("Back home, football returns too. The Premier League is back on Saturday, November 21, after the international break: Manchester City play Fulham at 12:30, and Newcastle play Arsenal at 5:30. On Sunday, November 22, Liverpool play Manchester United at 4:30 — and the ATP Finals end in Turin, with the singles final not before 6 p.m. local time.")
f.para("And American football? Week 11 opens on Thursday, November 19, with the Colts at the Texans. On Sunday, November 22, the Vikings play the 49ers in Mexico City, at 8:20 p.m. Eastern. The Patriots, after Munich, have the week off.")
f.box("WHY PERTH?　為什麼去珀斯？", [
    ("Perth Stadium hosted its first Ashes Test in November 2025. The city was not in the 2021–22 tour at all. Australia lost their first Test at the ground in November 2024, by 295 runs to India — and won their first Ashes Test there in two days, a year later.", "serif", False, INK, 21.5, 1.4),
])
f.para("How do you follow three sports in one day? Choose one game to watch fully, and follow the others on your phone. That is the modern fan: one screen for the game, one screen for the scores.", 23.5)
f.para("The ATP Finals in Turin run from Sunday, November 15, to Sunday, November 22. The eight best singles players of the year play in two groups of four: Alexander Zverev, Carlos Alcaraz, Ben Shelton, Daniil Medvedev, Flavio Cobolli, Arthur Fils, Frances Tiafoe and Rafael Jodar. The champion of the last two years, Jannik Sinner, is out with a knee injury.", 23.5)
f.gloss("a Test = 五日板球賽 · a tour = 巡迴賽 · an injury = 傷病 · a break = 間歇期。")
f.head("A　COMPREHENSION", 25)
f.bridge("讀第 4 版文章，選出正確答案。")
f.ex("B1", "單選", "A", "2025–26灰燼盃首戰2025年11月21日週五在珀斯",
     "The 2025–26 Ashes began on... A. Friday, November 21, 2025, in Perth · B. Saturday, November 21, 2026, in Perth · C. Thursday, November 19, in Houston", size=22)
f.ex("B1", "單選", "C", "澳大利亞隊長卡明斯因背傷缺陣",
     "Australia's captain, Pat Cummins, is out with... A. a knee injury · B. a hamstring injury · C. a back injury", size=22)
f.ex("B1", "單選", "B", "史蒂夫·史密斯代任隊長",
     "Steve Smith... A. is out with an injury · B. leads the side instead · C. plays for England", size=22)
f.ex("B1", "單選", "A", "英格蘭上次在澳大利亞贏系列賽是2010–11賽季",
     "England last won a Test series in Australia in... A. 2010–11 · B. 2017–18 · C. 2021–22", size=22)
f.ex("B1", "單選", "C", "英超回歸：曼城對富勒姆12:30開球",
     "On Saturday, November 21, Manchester City play Fulham at... A. 10:20 a.m. · B. 4:30 p.m. · C. 12:30 p.m.", size=22)
f.ex("B1", "單選", "B", "ATP總決賽在都靈，辛納因膝傷缺席",
     "The ATP Finals champion of the last two years, Jannik Sinner, is out with... A. a back injury · B. a knee injury · C. a hamstring injury", size=22)
f.head("B　SENTENCES", 25)
f.bridge("用所給詞補全句子。")
f.ex("B1", "完成句子", "hosted", "host → hosted（過去式）",
     "Perth Stadium ___ its first Ashes Test in November 2025.", instr="填空")
f.ex("B1", "完成句子", "lasts", "last三單lasts",
     "One Test ___ up to five days.", instr="填空")
f.ex("A2", "完成句子", "eight", "八位 = eight",
     "___ singles players play in Turin.", instr="填空")
f.ex("A2", "完成句子", "won", "win → won（過去式）",
     "Australia ___ the first Test by eight wickets.", instr="填空")
f.head("C　THE WORDS", 25)
f.match_set("B1", "詞彙配對",
            ["a Test", "a tour", "an injury", "a break"],
            ["a pause between parts of a season",
             "a five-day cricket match",
             "a series of games away from home",
             "damage to the body that stops you playing"],
            ["b", "c", "d", "a"],
            ["Test=五日板球賽 b", "tour=巡迴賽 c", "injury=傷病 d", "break=間歇期 a"],
            instr="把詞和釋義配對")
f.head("D　PAST SIMPLE", 25)
f.bridge("用一般過去時改寫（比賽已結束的說法）。")
f.ex("B1", "句型轉換", "England lost 4–0 in 2021–22.", "lose → lost",
     "England (lose) 4–0 in 2021–22. → ___", instr="改寫")
f.ex("B1", "句型轉換", "Australia lost their first Test at the ground.", "lose → lost",
     "Australia (lose) their first Test at the ground. → ___", instr="改寫")
f.ex("B1", "句型轉換", "The last series ended in a draw in 2023.", "end → ended",
     "The last series (end) in a draw in 2023. → ___", instr="改寫")
f.ex("B1", "句型轉換", "India beat Australia by 295 runs.", "beat → beat（不規則變化）",
     "India (beat) Australia by 295 runs in November 2024. → ___", instr="改寫")
f.end_report()

# col 3: image + fixtures
ix = COLX[3]
image(p, "grace.jpg", ix, 200, CW, 470)
cy4 = caption(p, ix, 670, CW, "W. G. Grace, cricket's first great star, in a photograph from the late 1880s. The Ashes began in 1882, in his time — and the urn is still the prize.",
              "Herbert Rose Barraud — public domain, via Wikimedia Commons")
v4 = Flow(p, [(ix, CW)], int(cy4) + 18, 2560, tag="P4-col3")
v4.box("SATURDAY, NOV 21　週六賽程", [
    ("Premier League: Man City–Fulham 12:30, Newcastle–Arsenal 17:30.", "serif", False, INK, 21.5, 1.42),
    ("ATP Finals semi-finals, Turin. SUNDAY, NOVEMBER 22: Liverpool–Man Utd 16:30, ATP finals day.", "serif", False, INK, 21.5, 1.42),
    ("NFL WEEK 11: Thu Nov 19, Colts–Texans. Sun Nov 22, Vikings–49ers in Mexico City.", "serif", False, INK, 21.5, 1.42),
])
v4.head("ONE SCREEN, TWO SCREENS", 25)
v4.para("The modern fan watches one game fully and follows the others on a phone. Try it in English: “The score is 14–10.” “Who scored?” “Arsenal are winning!” — short sentences, live English.", 22)
v4.bridge("看球英語｜比數、誰得分、誰領先——短句就是直播英語。")
v4.end_report()
p.foot(4)
p.save(f"{OUT}/p4-sport.svg")
print("P4 saved, exercises so far:", len(REG))
