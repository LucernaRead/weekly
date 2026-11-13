# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bslib4 import *

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "svg")
os.makedirs(OUT, exist_ok=True)

# ================= P7 · LANGUAGE (A2→B2) =================
CURPAGE[0] = 7
p = BSPage4()
p.band("LANGUAGE IN HAND　손안의 언어", "The Lucerna", "A2 → B2　Phrases of the week　이번 주 표현")

f = Flow(p, [(COLX[i], CW) for i in range(3)], 200, 2560, tag="P7-main")

f.head("WORDS　A2　win / won", 28)
f.gloss("Win은 현재형（매번 이긴다）, won은 과거형（이미 이겼다）——이번 주 뉴스에서는 과거형이 많다.")
f.para("win = to get first place. won = the past of win.", 23.5)
f.para("A2: “The Democrats won the House.” The vote is over, so the verb is in the past: won, not win.", 23.5)
f.para("Try it: win / won — ask “Will England win the next Ashes?” about the future: the next series is in England, in June 2027. About last year: “Australia won the first Test.”", 23.5)

f.head("WORDS　B1　more than", 28)
f.gloss("comparative = 비교급: more than으로 수와 크기를 말한다.")
f.para("more than = a bigger number than. In the House, 254 is more than 218. The majority is 218 — and 254 is 36 more than the majority.", 23.5)
f.para("B1: “254 seats is more than the 218 needed.” With numbers, use more than: more people, more seats, more votes.", 23.5)
f.para("Try it: “The film is longer than the trailer.” “The book is cheaper than the film.”", 23.5)

f.head("GRAMMAR　A2　will + verb", 28)
f.gloss("will + 동사 원형: 앞으로 일어날 일. 의문문에서는 will이 앞에 온다.")
f.para("The counting will continue. The new Congress will meet in January. Will the count change? Nobody knows.", 23.5)
f.para("Rule: will + verb, no -s, no -ed. “She will win.” “They will vote.” Question: “Will they watch the jungle?”", 23.5)

f.head("GRAMMAR　B1　past simple", 28)
f.gloss("past simple = 과거형: 이미 일어난 일. 불규칙 동사는 외워야 한다.")
f.para("Use the past for the past: Collins published the novel in 2025. Haymitch won the 50th Games. England lost 4–0 in 2021–22. India beat Australia by 295 runs.", 23.5)
f.para("Irregular verbs in this issue: win → won, lose → lost, beat → beat, choose → chose, run → ran.", 23.5)

f.head("GRAMMAR　B2　headlines", 28)
f.gloss("headline present = 제목의 현재형: 신문 제목은 일어난 일을 현재형으로 쓴다.")
f.para("Newspapers use the present in headlines for what already happened: “Democrats Win the House and the Senate” — the vote was on November 3, but the headline says Win, not Won. The present makes the news feel fresh.", 23.5)

f.head("GRAMMAR　B2　whether", 28)
f.gloss("whether는 종속절을 이끈다: 결과를 모를 때 whether를 쓴다.")
f.para("Nobody knows whether the count will change. Nobody knows whether it will rain in Perth. Whether = if — for what you do not know.", 23.5)

f.head("GOLDEN SENTENCES", 28)
f.bridge("명문장 (이번 호 본문의 원문)——외워 두면 다음에 당신도 이렇게 쓸 수 있어요.")
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
f.head("THE DRILLS　연습", 28)
f.bridge("다음 단어로 빈칸을 채우세요: won / more / lost / will / published / whether / chose / win.")
f.ex("A2", "명문장 빈칸 채우기", "won", "won = win의 과거형（이미 이겼다）",
     "“The Democrats ___ the House.”", instr="빈칸 채우기")
f.ex("B1", "비교", "more", "more than = …보다 많다",
     "254 is ___ than 218.", instr="빈칸 채우기")
f.ex("B1", "과거형", "lost", "lose → lost",
     "England ___ 4–0 in 2021–22.", instr="빈칸 채우기")
f.ex("A2", "미래형", "will", "will + 동사 원형",
     "The new Congress ___ meet in January.", instr="빈칸 채우기")
f.ex("B1", "시제", "published", "publish → published",
     "Collins ___ the novel in 2025.", instr="빈칸 채우기")
f.ex("B2", "종속절", "whether", "whether = ~인지（모르는 일）",
     "Nobody knows ___ the count will change.", instr="빈칸 채우기")
f.ex("B2", "과거형", "chose", "choose → chose",
     "ITV ___ Monday for the launch.", instr="빈칸 채우기")
f.ex("A2", "문장 완성", "win", "복수 주어에는 win（제목의 현재형）",
     "“Democrats ___ the House” is a headline.", instr="빈칸 채우기")
f.head("ERROR CLINIC　오류", 28)
f.ex("A2", "오류 고치기", "Correct: The Democrats won the House.", "won / win, 시제 오류",
     "“The Democrats win the House in 2026.” (wrong tense)", instr="오류 고치기")
f.ex("A2", "오류 고치기", "Correct: The count continued after the vote.", "continue의 과거형은 continued",
     "“The count continue after the vote.” (wrong tense)", instr="오류 고치기")
f.ex("B1", "오류 고치기", "Correct: 254 is more than 218.", "more than 구문",
     "“254 is more then 218.” (wrong word)", instr="오류 고치기")
f.ex("B2", "오류 고치기", "Correct: Nobody knows whether it will change.", "whether는 종속절을 이끈다",
     "“Nobody knows if the count will change or not whether.” (wrong structure)", instr="오류 고치기")
f.end_report()

# ---- col 3: image + toolbox + drills ----
ix = COLX[3]
image(p, "johnson.jpg", ix, 200, CW, 290)
cy7 = caption(p, ix, 490, CW, "Samuel Johnson, painted by Sir Joshua Reynolds in 1772. Johnson's dictionary fixed English words — and this page fixes yours.",
              "Sir Joshua Reynolds — public domain, via Wikimedia Commons")
v7 = Flow(p, [(ix, CW)], int(cy7) + 18, 2560, tag="P7-col3")
v7.box("THE TOOLBOX　도구 상자", [
    ("A2 — “The Democrats won the House.” 민주당은 하원에서 이겼다.", "serif", False, INK, 21.5, 1.42),
    ("B1 — “254 is more than 218.” 254는 218보다 많다.", "serif", False, INK, 21.5, 1.42),
    ("B2 — “Nobody knows whether the count will change.” 개표 결과가 달라질지 아무도 모른다.", "serif", False, INK, 21.5, 1.42),
])
v7.head("READERS' CORNER　독자의 편지", 25)
v7.para("VOL.3 promised real letters from VOL.4. No letters arrived by press time. This page keeps the promise open: send your letter, your three sentences, or your five-sentence film review to the newsroom. Real letters, with your name and city only if you give them, will appear here from VOL.5.", 22)
v7.para("VOL.3에서 약속했어요. VOL.4부터 독자의 진짜 편지를 싣겠다고요. 마감 때까지 편지가 오지 않았지만 약속은 여전히 유효해요. 편지, 세 문장 연습, 다섯 문장 영화 감상을 편집부에 보내주세요. 진짜 편지는 VOL.5부터 실립니다. 이름과 도시는 당신이 동의할 때만 싣습니다.", 20, "sans", False, GREY, 1.4, 2)
v7.head("AN EXAMPLE LETTER　보기", 25)
v7.para("This letter is written by the editor, only to show the shape. It is not a reader's letter. No name and no city are given, because no real letter has arrived yet.", 20, "sans", False, GREY, 1.4, 2)
v7.para("“Dear Lucerna, I read the midterm story with my class. We counted the seats together — 254, 162, 19. My question: when will the count be final? Thank you for the numbers.” — A reader, somewhere in the world.", 22)
v7.para("이 편지는 편집부가 형식의 보기로 쓴 것입니다. 독자의 편지가 아닙니다. 진짜 편지가 아직 오지 않아서 이름과 도시가 없습니다.", 20, "sans", False, GREY, 1.4, 2)
v7.head("NEXT WEEK　VOL.5 예고", 25)
v7.para("Thanksgiving in America. The Ashes: England's rematch waits until June 2027. More certified results of the midterm election. And your letters — the first real ones.", 22)
v7.end_report()
p.foot(7)
p.save(f"{OUT}/p7-lang.svg")
print("P7 saved, exercises so far:", len(REG))
