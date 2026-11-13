# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE (A2→B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND　语言在手", "The Lucerna", "A2 → B2　Phrases of the week　本周句型")

f = Flow(p, [(COLX[i], CW) for i in range(3)], 200, 2560, tag="P7-main")

f.head("WORDS　A2　win / won", 28)
f.gloss("讲解｜Win 是现在时（每次都赢）；won 是过去时（已经赢了）——本周新闻多用过去时。")
f.para("win = to get first place. won = the past of win.", 23.5)
f.para("A2: “The Democrats won the House.” The vote is over, so the verb is in the past: won, not win.", 23.5)
f.para("Try it: win / won — ask “Will England win the next Ashes?” about the future: the next series is in England, in June 2027. About last year: “Australia won the first Test.”", 23.5)

f.head("WORDS　B1　more than", 28)
f.gloss("讲解｜comparative 比较级：用 more than 说数量和大小。")
f.para("more than = a bigger number than. In the House, 254 is more than 218. The majority is 218 — and 254 is 36 more than the majority.", 23.5)
f.para("B1: “254 seats is more than the 218 needed.” With numbers, use more than: more people, more seats, more votes.", 23.5)
f.para("Try it: “The film is longer than the trailer.” “The book is cheaper than the film.”", 23.5)

f.head("GRAMMAR　A2　will + verb", 28)
f.gloss("讲解｜will + 动词原形：说将要发生的事；疑问句 will 提前。")
f.para("The counting will continue. The new Congress will meet in January. Will the count change? Nobody knows.", 23.5)
f.para("Rule: will + verb, no -s, no -ed. “She will win.” “They will vote.” Question: “Will they watch the jungle?”", 23.5)

f.head("GRAMMAR　B1　past simple", 28)
f.gloss("讲解｜past simple 一般过去时：已经发生的事；不规则动词要记住。")
f.para("Use the past for the past: Collins published the novel in 2025. Haymitch won the 50th Games. England lost 4–0 in 2021–22. India beat Australia by 295 runs.", 23.5)
f.para("Irregular verbs in this issue: win → won, lose → lost, beat → beat, choose → chose, run → ran.", 23.5)

f.head("GRAMMAR　B2　headlines", 28)
f.gloss("讲解｜headline present 标题现在时：报纸标题用现在时说已经发生的事。")
f.para("Newspapers use the present in headlines for what already happened: “Democrats Win the House and the Senate” — the vote was on November 3, but the headline says Win, not Won. The present makes the news feel fresh.", 23.5)

f.head("GRAMMAR　B2　whether", 28)
f.gloss("讲解｜whether 引导宾语从句：不知道结果的事，用 whether。")
f.para("Nobody knows whether the count will change. Nobody knows whether it will rain in Perth. Whether = if — for what you do not know.", 23.5)

f.head("GOLDEN SENTENCES", 28)
f.bridge("金句（本期正文原句）——背下来，下次你也可以这样写。")
gold = [
    ("The vote is over. The counting is not.", "P2"),
    ("A “call” is not the official result.", "P1"),
    ("The Ashes are not a sport for early nights.", "P4"),
    ("A midterm changes Congress, not the President.", "P6"),
    ("The map is drawn. The work starts in January.", "P6"),
    ("Two jungles, one week: a painted jungle in the cinema, and a real jungle on television.", "P3"),
    ("A small act is not small to the person it helps — and a loud voice starts with one sentence.", "P5"),
    ("On Tuesday, November 3, Americans voted in the midterm election — for all 435 seats in the House of Representatives, for 35 seats in the Senate, and for governor in 36 states.", "P1"),
]
for en, src in gold:
    f.para(f"“{en}”", 23.5, "serif", False, INK, 1.42, 2)
    f.para(f"—— From page {src.replace('P', '')} of this issue.", 19, "sans", False, GREY, 1.4, 2)
f.head("THE DRILLS　本周小练", 28)
f.bridge("用下列词填空：won / more / lost / will / published / whether / chose / win。")
f.ex("A2", "金句填空", "won", "won = win 的过去时（已赢）",
     "“The Democrats ___ the House.”", instr="填空")
f.ex("B1", "比较填空", "more", "more than = 比……多",
     "254 is ___ than 218.", instr="填空")
f.ex("B1", "过去时", "lost", "lose → lost",
     "England ___ 4–0 in 2021–22.", instr="填空")
f.ex("A2", "将来时", "will", "will + 动词原形",
     "The new Congress ___ meet in January.", instr="填空")
f.ex("B1", "时态", "published", "publish → published",
     "Collins ___ the novel in 2025.", instr="填空")
f.ex("B2", "从句", "whether", "whether = 是否（不知道的事）",
     "Nobody knows ___ the count will change.", instr="填空")
f.ex("B2", "过去时", "chose", "choose → chose",
     "ITV ___ Monday for the launch.", instr="填空")
f.ex("A2", "完成句子", "win", "复数主语用 win（标题现在时）",
     "“Democrats ___ the House” is a headline.", instr="填空")
f.head("ERROR CLINIC　纠错门诊", 28)
f.ex("A2", "纠错", "Correct: The Democrats won the House.", "won / win 时态错",
     "“The Democrats win the House in 2026.” (wrong tense)", instr="纠错")
f.ex("A2", "纠错", "Correct: The count continued after the vote.", "continue 的过去时 continued",
     "“The count continue after the vote.” (wrong tense)", instr="纠错")
f.ex("B1", "纠错", "Correct: 254 is more than 218.", "more than 结构",
     "“254 is more then 218.” (wrong word)", instr="纠错")
f.ex("B2", "纠错", "Correct: Nobody knows whether it will change.", "whether 引导从句",
     "“Nobody knows if the count will change or not whether.” (wrong structure)", instr="纠错")
f.end_report()

# ---- col 3: image + toolbox + drills ----
ix = COLX[3]
image(p, "johnson.jpg", ix, 200, CW, 290)
cy7 = caption(p, ix, 490, CW, "Samuel Johnson, painted by Sir Joshua Reynolds in 1772. Johnson's dictionary fixed English words — and this page fixes yours.",
              "Sir Joshua Reynolds — public domain, via Wikimedia Commons")
v7 = Flow(p, [(ix, CW)], int(cy7) + 18, 2560, tag="P7-col3")
v7.box("THE TOOLBOX　句型工具箱", [
    ("A2 — “The Democrats won the House.” 民主党赢了众议院。", "serif", False, INK, 21.5, 1.42),
    ("B1 — “254 is more than 218.” 254 比 218 多。", "serif", False, INK, 21.5, 1.42),
    ("B2 — “Nobody knows whether the count will change.” 没人知道计票结果还会不会变。", "serif", False, INK, 21.5, 1.42),
])
v7.head("READERS' CORNER　读者来信", 25)
v7.para("VOL.3 promised real letters from VOL.4. No letters arrived by press time. This page keeps the promise open: send your letter, your three sentences, or your five-sentence film review to the newsroom. Real letters, with your name and city only if you give them, will appear here from VOL.5.", 22)
v7.para("VOL.3 曾承诺：从 VOL.4 起刊登真实读者来信。本期截稿时没有收到来信——这个承诺仍然有效：请把你的信、三句话练习或五句影评寄给编辑部。真实来信将从 VOL.5 起刊登，姓名与城市只在你同意时写出。", 20, "sans", False, GREY, 1.4, 2)
v7.head("AN EXAMPLE LETTER　示例信", 25)
v7.para("This letter is written by the editor, only to show the shape. It is not a reader's letter. No name and no city are given, because no real letter has arrived yet.", 20, "sans", False, GREY, 1.4, 2)
v7.para("“Dear Lucerna, I read the midterm story with my class. We counted the seats together — 254, 162, 19. My question: when will the count be final? Thank you for the numbers.” — A reader, somewhere in the world.", 22)
v7.para("这封信是编辑写的示例，仅供参考格式，不是读者来信。没有写姓名与城市，因为尚未收到真实来信。", 20, "sans", False, GREY, 1.4, 2)
v7.head("NEXT WEEK　VOL.5 预告", 25)
v7.para("Thanksgiving in America. The Ashes: England's rematch waits until June 2027. More certified results of the midterm election. And your letters — the first real ones.", 22)
v7.end_report()
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
