# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P5 · YOUTH (B1) =================
CURPAGE[0] = 5
p = BSPage4()
p.band("YOUTH　若者", "The Lucerna", "LEVEL B1　Break the silence　沈黙を破れ")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P5-main")
f.title("Break the Silence: Odd Socks and Loud Voices", 32)
f.byline("By The Lucerna newsroom　Reading level: B1")
f.para("On Monday, November 16, schools across Britain do something strange: children and teachers wear odd socks. One red sock, one blue sock — on purpose. It is Odd Socks Day, the first day of Anti-Bullying Week, and this year is its tenth birthday.")
f.para("Anti-Bullying Week runs from Monday, November 16, to Friday, November 20. It is organised by the Anti-Bullying Alliance, and this year's theme is “Break the Silence”. The idea is simple: bullying is hardest to stop when nobody speaks about it. So the week asks children — and adults — to start conversations, to speak up, to listen, and to take action together.")
f.para("The numbers are big: the campaign reaches about eight million children and young people, and more than 80% of schools in England, Wales and Northern Ireland take part. The theme was chosen with more than 200 children and young people, who said that speaking up was the hardest part.")
f.para("Friday, November 20, is also World Children's Day — a day for children's rights around the world, led by UNICEF. This year's theme is “My day. My rights. My future.” The date marks the day in 1989 when the United Nations adopted the Convention on the Rights of the Child.")
f.para("What can one child do? Tell a teacher. Tell a parent. Tell a friend. And if you see someone alone at lunch, sit with them. A small act is not small to the person it helps — and a loud voice starts with one sentence.")
f.box("ODD SOCKS, IN NUMBERS　数字で", [  # D5: tsize 23->22, +6.3px over
    ("10 — years of Odd Socks Day. 8 million — children reached by the week. 200 — children who helped choose this year's theme.", "serif", False, INK, 21.5, 1.4),
], tsize=22)
f.para("If you want to practise Monday-morning English, try this: wear odd socks, and explain them in English. “I wear odd socks for Anti-Bullying Week. Different is good.” Three sentences — and a whole week of practice.", 23.5)
f.gloss("bullying = いじめ · to speak up = 声を上げる · a right = 権利 · silence = 沈黙")
f.head("A　COMPREHENSION", 25)
f.bridge("5ページの記事を読んで、正しい答えを選びなさい。")
f.ex("B1", "選択", "B", "いじめ防止週間は11月16–20日",
     "Anti-Bullying Week runs from... A. November 9 to 13 · B. Monday, November 16, to Friday, November 20 · C. November 20 to 26", size=22)
f.ex("B1", "選択", "A", "今年のテーマは「沈黙を破れ」",
     "This year's theme is... A. “Break the Silence” · B. “Challenge Yourself” · C. “My day. My rights.”", size=22)
f.ex("B1", "選択", "C", "ちぐはぐソックスの日は10周年",
     "Odd Socks Day is... A. new this year · B. five years old · C. ten years old", size=22)
f.ex("B1", "選択", "B", "この活動は約800万人の子どもに届く",
     "The campaign reaches about... A. 200 children · B. eight million children · C. 80 children", size=22)
f.ex("B1", "選択", "A", "世界子どもの日は11月20日金曜日",
     "World Children's Day is on... A. Friday, November 20 · B. Monday, November 16 · C. Thursday, November 26", size=22)
f.ex("B1", "選択", "C", "「子どもの権利条約」は1989年に採択された",
     "The Convention on the Rights of the Child was adopted in... A. 1910 · B. 1969 · C. 1989", size=22)
f.head("B　SENTENCES", 25)
f.bridge("与えられた語で文を完成させなさい。")
f.ex("B1", "文の完成", "silence", "silence = 沈黙",
     "Break the ___: speak up about bullying.", instr="空所補充")
f.ex("B1", "文の完成", "socks", "sock = 靴下",
     "On Monday, children wear odd ___.", instr="空所補充")
f.ex("A2", "文の完成", "rights", "right = 権利",
     "Every child has ___.", instr="空所補充")
f.ex("A2", "文の完成", "up", "speak up = 声を上げる",
     "Speak ___: tell a teacher.", instr="空所補充")
f.head("C　THE WORDS", 25)
f.match_set("B1", "語彙マッチング",
            ["bullying", "to speak up", "a right", "silence"],
            ["saying what you think, loudly and clearly",
             "something every child has, by law",
             "saying nothing at all",
             "hurting or frightening someone again and again"],
            ["d", "a", "b", "c"],
            ["bullying = いじめ d", "speak up = 声を上げる a", "right = 権利 b", "silence = 沈黙 c"],
            instr="語と意味を結ぶ")
f.head("D　PRESENT CONTINUOUS", 25)
f.bridge("現在進行形で書きかえよう。")
f.ex("B1", "文型変換", "Schools are wearing odd socks today.", "wear → are wearing",
     "Schools (wear) odd socks today. → ___", instr="書きかえ")
f.ex("B1", "文型変換", "Children are speaking up this week.", "speak → are speaking",
     "Children (speak) up this week. → ___", instr="書きかえ")
f.ex("B1", "文型変換", "We are listening to every child.", "listen → are listening",
     "We (listen) to every child. → ___", instr="書きかえ")
f.ex("B1", "文型変換", "She is sitting with a new friend.", "sit → is sitting",
     "She (sit) with a new friend. → ___", instr="書きかえ")
f.end_report()

# col 3: image + side flow
ix = COLX[3]
image(p, "children.jpg", ix, 200, CW, 440)
cy5 = caption(p, ix, 640, CW, "Children from Lawrence, Massachusetts, marching in New York on February 19, 1912, during the textile strike. They asked for bread — and the world listened. Children have always had a voice.",
              "Bain News Service — public domain, via Library of Congress")
v5 = Flow(p, [(ix, CW)], int(cy5) + 18, 2560, tag="P5-col3")
v5.box("SPEAK UP　声を上げよう", [
    ("“Break the silence.” “Different is good.” “Sit with me.” — three sentences for one week. Learn them, and Monday morning in English is yours.", "serif", False, INK, 21.5, 1.42),
])
v5.head("FRIDAY'S WORDS", 25)
v5.para("“My day. My rights. My future.” — the words of World Children's Day, Friday, November 20. Three short sentences, one big idea: children have a voice, and the world should listen.", 22)
v5.para("“Every child has rights” means: every child, everywhere, has the right to be safe, to learn, and to be heard. After that sentence, the listening begins.", 22)
v5.bridge("すべての子どもに権利がある | Every child has rights = すべての子どもに権利がある。")
v5.head("THE JUNGLE, TOO", 25)
v5.para("After Friday, the weekend keeps going: the jungle is on every night, and the football is back on Saturday. The week ends with sport — and starts again with school on Monday.", 22)
v5.end_report()
p.foot(5)
p.save(f"{OUT}/p5-youth.svg")
print("P5 saved, exercises so far:", len(REG))

# ================= P6 · DEEP READ (B2) =================
CURPAGE[0] = 6
p = BSPage4()
p.band("DEEP READ　深読み", "The Lucerna", "LEVEL B2　The map after November 3　11月3日後の地図")

f = Flow(p, [(COLX[0], CW), (COLX[1], CW), (COLX[2], CW)], 200, 2560, tag="P6-main")
f.title("The Map After November 3: Reading the Results", 32)
f.byline("By The Lucerna newsroom　Reading level: B2")
f.para("The vote is counted. The map is still being drawn. On Tuesday, November 3, Americans voted for the House, for a third of the Senate, and for governor in 36 states. By the Sunday after the vote, November 8, the Associated Press had called the big question: the Democrats had won both houses of Congress.")
f.para("Here is the map, as called on Sunday, November 8. In the House, the Democrats won 254 seats, the Republicans 162, and 19 races were still uncalled. In the Senate, the Democrats won 20 of the 33 races called and the Republicans 13, with Alaska and Mississippi still uncalled. Seven Senate seats changed hands, and all seven went to the Democrats: Iowa, Kansas, Maine, North Carolina, Ohio, South Carolina and Texas.")
f.para("What does “called” mean? A call is a news organisation's judgement: the maths is clear, and the candidate behind cannot catch up. It is not the official result. The official result comes when each state certifies its count — between November 10 and December 18, with no fixed date in some states. In Georgia, a Senate race with no majority winner goes to a runoff on December 1 — but this time Jon Ossoff won reelection with about 59% of the vote, so there was no runoff. Mississippi has no runoff in a regular election: the candidate with the most votes wins.")
f.para("What changes? In January 2027, the new Congress meets, with a Democratic House and a Democratic Senate. The two parties choose their leaders first: the House Republicans on November 10, the House Democrats on November 18 and 19. The Speaker — the leader of the House — is chosen when the new Congress meets in January. The Speaker, Mike Johnson, has said he will not run to lead the Republicans in the new Congress.")
f.para("What does not change? The President stays the same, and so does the White House. A midterm changes Congress, not the President. That is the American system: the voters speak in the middle of a President's term, and the two sides must then work — or argue — together. The map is drawn. The work starts in January.")
f.box("A PRACTICE BALLOT　投票用紙", [
    ("For Governor: ☐ Candidate A · ☐ Candidate B. For the House: ☐ Candidate C · ☐ Candidate D. Names are codes here — this ballot teaches how to mark, not whom to choose.", "serif", False, INK, 21.5, 1.4),
])
f.para("A note on numbers in this issue: this paper prints the calls of Sunday, November 8, and says so. The calls can still move a little as the count goes on — and this paper will not guess the final numbers. When the certified results are in, VOL.5 will report them.")
f.gloss("to call a race = 当確を出す · to certify = 正式に認証する · a runoff = 決選投票 · a map = 政治地図。")
# practice chart
f.head("READ THE CHART　グラフを読む", 25)
f.para("How big was the change? The chart is the calls of Sunday, November 8 — not the certified results, and not a prediction.", 22)
for lab in ["House called: 254 Democrats, 162 Republicans, 19 uncalled (Nov 8)",
            "Senate called: 20 Democrats, 13 Republicans, 2 uncalled (Nov 8)",
            "Senate flips: 7, all to the Democrats",
            "Governors flipped: 5, all to the Democrats",
            "States certify: November 10 to December 18",
            "Runoff, if needed: December 1 (Georgia only)"]:
    f.para(lab, 22, "serif", True, OLIVE, 1.3, 2)
f.head("A　CHART READING", 25)
f.bridge("上の発表数のグラフを読んで正しい答えを選びなさい。")
f.ex("B2", "グラフの読み取り", "B", "11月8日発表：民主党は下院で254議席",
     "In the House, as called on November 8, the Democrats won... A. 218 seats · B. 254 seats · C. 162 seats", size=22)
f.ex("B2", "グラフの読み取り", "C", "下院の19議席は未発表",
     "In the House, races still uncalled: ... A. 2 · B. 13 · C. 19", size=22)
f.ex("B2", "グラフの読み取り", "A", "上院は35議席中33議席が発表済み",
     "In the Senate, races called: ... A. 33 of 35 · B. 20 of 35 · C. 35 of 35", size=22)
f.ex("B2", "グラフの読み取り", "B", "上院の7議席が政党を変え、すべて民主党へ",
     "Senate seats that changed hands: ... A. 5 · B. 7 · C. 22", size=22)
f.ex("B2", "グラフの読み取り", "A", "5つの知事職が政党を変え、すべて民主党へ",
     "Governors' offices that changed hands: ... A. 5 · B. 7 · C. 2", size=22)
f.ex("B2", "グラフの読み取り", "C", "254 + 162 + 19 = 435（下院の議席総数）",
     "The House numbers add up to... A. 218 · B. 413 · C. 435", size=22)
f.head("B　COMPREHENSION", 25)
f.bridge("6ページの記事を読んで、正しい答えを選びなさい。")
f.ex("B2", "選択", "B", "「当確を出す」ことは正式な結果ではない",
     "A “call” is... A. the official result · B. a news organisation's judgement · C. a vote in Congress", size=22)
f.ex("B2", "選択", "A", "正式な結果は各州の認証による",
     "The official result comes when... A. the state certifies its count · B. TV calls the race · C. the first votes arrive", size=22)
f.ex("B2", "選択", "C", "上院の2議席は未確定：アラスカとミシシッピ",
     "The two Senate races still uncalled are in... A. Georgia and Texas · B. Iowa and Ohio · C. Alaska and Mississippi", size=22)
f.ex("B2", "選択", "B", "下院の共和党は11月10日に党首を選ぶ",
     "The House Republicans choose their leader on... A. November 8 · B. November 10 · C. November 18", size=22)
f.ex("B2", "選択", "A", "中間選挙は議会を変え、大統領は変わらない",
     "A midterm changes... A. Congress, not the President · B. the President, not Congress · C. the courts", size=22)
f.ex("B2", "選択", "C", "VOL.5では認証後の最終結果を報じます",
     "The certified results will be reported in... A. VOL.3 · B. this issue · C. VOL.5", size=22)
f.head("C　SENTENCES", 25)
f.bridge("与えられた語で文を完成させなさい。")
f.ex("B2", "文の完成", "certify", "certify = 正式に認証する",
     "Each state must ___ its count.", instr="空所補充")
f.ex("B2", "文の完成", "call", "call a race = 選挙結果を発表すること",
     "News organisations ___ a race when the maths is clear.", instr="空所補充")
f.ex("B2", "文の完成", "changed", "change hands = 政党が変わる",
     "Seven Senate seats ___ hands on election night.", instr="空所補充")
f.ex("B1", "文の完成", "takes", "take time = 時間がかかる",
     "Counting ___ time in every state.", instr="空所補充")
f.ex("B1", "文の完成", "differs", "differ の三人称単数 differs",
     "The rule ___ from state to state.", instr="空所補充")
f.ex("B1", "文の完成", "official", "official = 公式の",
     "A call is not the ___ result.", instr="空所補充")
f.end_report()

# col 3: image + terms box
ix = COLX[3]
image(p, "voting.jpg", ix, 200, CW, 300)
cy6 = caption(p, ix, 500, CW, "A voting booth in the Old State House, Hartford, Connecticut: one voter, one ballot, one private moment. On Tuesday, November 3, millions of Americans did the same.",
              "Kenneth C. Zirkel — CC0, via Wikimedia Commons")
v6 = Flow(p, [(ix, CW)], int(cy6) + 18, 2560, tag="P6-col3")
v6.box("HOW LONG?　任期の長さ", [
    ("House: 2 years, all 435 seats each midterm. Senate: 6 years, about a third each election. President: 4 years. Governor: usually 4 years.", "serif", False, INK, 21.5, 1.42),
])
v6.head("FIFTY ELECTIONS", 25)
v6.para("One country, fifty systems: that is why American election night is a map, not a single number. Learn the map, and the night makes sense.", 22)
v6.bridge("一枚の地図｜50の州、50通りのルール——だから選挙の夜に見るのは地図であって、1つの数字ではない。")
v6.end_report()
p.foot(6)
p.save(f"{OUT}/p6-deep.svg")
print("P6 saved, exercises so far:", len(REG))
