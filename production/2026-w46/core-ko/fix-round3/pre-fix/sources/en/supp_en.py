# -*- coding: utf-8 -*-
"""W46 KO x EN supplement: GEOM (W43/W45 ko-en measured instance) + letters
rebuild (W45 en precedent: single English disclosure) + SUPP replacements
for W46-new Chinese strings. Applied AFTER filtered W45 ops. Every SUPP old
string must occur >= 1 time (asserted); GEOM-covered and letters-deleted
strings are excluded from SUPP."""
import os

HERE = os.path.dirname(os.path.abspath(__file__))

GEOM = [
    ('p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")\n'
     'p.text(975, 394, "TEXT IN KOREAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 17, "sans", True, OLIVE, anchor="middle")'),
    ("p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)",
     "p.hline(MX, RIGHT, 412, INK, 3); p.hline(MX, RIGHT, 421, INK, 1.2)"),
    ("p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)",
     "p.rect(MX, 433, RIGHT - MX, 118, fill=DARK)"),
    ('p.text(MX + 30, 478, "김장이 한창이에요 — 수능까지 일주일이 남았어요", 36, "sans", True, "#f3edda")',
     'p.text(MX + 30, 487, "김장이 한창이에요 — 수능까지 일주일이 남았어요", 36, "sans", True, "#f3edda")'),
    ('p.text(MX + 30, 522, "단풍 예보 날짜가 이번 주에 있어요. 한국시리즈 소식은 4면을 보세요.", 23, "serif", False, "#e8dfc8")',
     'p.text(MX + 30, 531, "단풍 예보 날짜가 이번 주에 있어요. 한국시리즈 소식은 4면을 보세요.", 23, "serif", False, "#e8dfc8")'),
    ('p.text(RIGHT - 30, 478, "김장", 24, "sans", True, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 487, "KIMCHI-MAKING", 24, "sans", True, "#b3a06a", anchor="end")'),
    ('p.text(RIGHT - 30, 522, "泡菜季正忙 · 高考剩一周", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 531, "Kimchi season in full swing · One week to the CSAT", 21, "sans", False, "#b3a06a", anchor="end")'),
]

NEW_LCN = ("Editor's note: this is an example letter from the editors, not a "
           "real reader's letter. No real reader letters or best page 8 writing "
           "had arrived by press time, so the example stands and last issue's "
           "promise carries to VOL.4. Send us your letter and your page 8 writing "
           "— write two sentences in Korean and send them in!")

SUPP = [
    ("한창이다 正忙 · 새우젓 腌虾酱 · 절정 最盛期、高峰 · 예보 预报 · 관측 观测。",
     "한창이다 = in full swing · 새우젓 = salted shrimp · 절정 = peak, the height · 예보 = forecast · 관측 = observation"),
    ("집계하다 统计 · 좌우하다 左右、决定 · 장바구니 菜篮子 · 대상 对象。",
     "집계하다 = to total up · 좌우하다 = to decide, to sway · 장바구니 = shopping basket · 대상 = target, object"),
    ("노고 辛劳 · 소화기 灭火器 · 막히다 堵塞。",
     "노고 = hard work · 소화기 = fire extinguisher · 막히다 = to be blocked"),
    ("절임배추 提前腌好的白菜 · 버무리다 拌 · 아끼다 节省。",
     "절임배추 = pre-salted cabbage · 버무리다 = to mix and season · 아끼다 = to save"),
    ("아삭하다 脆脆的 · 약하다 弱 · 김 蒸汽。",
     "아삭하다 = crisp · 약하다 = weak · 김 = steam"),
    ("전망 展望、预测 · 나누다 区分 · 통제하다 管制 · 순환버스 循环巴士。",
     "전망 = outlook, forecast · 나누다 = to tell apart · 통제하다 = to control · 순환버스 = shuttle bus"),
    ("겹치다 重叠 · 감사하다 感谢 · 나누다 区分、分享。",
     "겹치다 = to overlap · 감사하다 = to thank · 나누다 = to tell apart, to share"),
    ("밀리다 推迟 · 이동일 移动日 · 이어지다 延续 · 먼저 首先。",
     "밀리다 = to be pushed back · 이동일 = travel day · 이어지다 = to continue · 먼저 = first"),
    ("관리본부 管理本部 · 신고하다 申报 · 챙기다 准备好。",
     "관리본부 = management office · 신고하다 = to report · 챙기다 = to get ready"),
    ("건네다 递给 · 날씬해지다 变苗条 · 하얗다 白。",
     "건네다 = to hand over · 날씬해지다 = to get slim · 하얗다 = white"),
    ("피곤하다 疲倦 · 졸리다 犯困 · 평소 平时。",
     "피곤하다 = tired · 졸리다 = sleepy · 평소 = usually"),
    ("재다 衡量 · 규모 规模 · 섞다 混淆。",
     "재다 = to measure · 규모 = scale, size · 섞다 = to mix up"),
    ("정직하다 诚实 · 채우다 填补 · 속이다 欺骗。",
     "정직하다 = honest · 채우다 = to fill · 속이다 = to deceive"),
    ("미리 提前 · 아끼다 节省 · 들어가다 加入。",
     "미리 = in advance · 아끼다 = to save · 들어가다 = to go in"),
    ("남다 剩下 · 딱 正好、恰恰。",
     "남다 = to be left · 딱 = exactly"),
    ("기준 标准 · 나누다 区分。",
     "기준 = criterion · 나누다 = to tell apart"),
    ("한창 ＝ 正忙、最忙的时候。",
     "한창 = in full swing, the busiest time."),
    ("김장=腌过冬泡菜 a", "김장 = making kimchi for winter a"),
    ("예보=提前预报 d", "예보 = a forecast given in advance d"),
    ("관측=实际观测 c", "관측 = an actual observation c"),
    ("새우젓=涨价的虾酱 c", "새우젓 = the salted shrimp that went up c"),
    ("소방의 날=11月9日 d", "소방의 날 = Nov 9 d"),
    ("11月12日是D-7", "Nov 12 is D-7"),
    ("泡菜季正忙", "Kimchi season is in full swing"),
    ("高考在11月19日周四", "The CSAT is on Thursday, Nov 19"),
    ("11月9日是D-10", "Nov 9 is D-10"),
    ("三星3胜2负晋级", "Samsung won 3–2 to advance"),
    ("定期报名11月10日17点截止", "Regular sign-up closes Nov 10 at 17:00"),
    ("白菜降价、虾酱涨价", "Cabbage down, salted shrimp up"),
    ("11月11日有三个名字", "Nov 11 has three names"),
    ("季后赛三星3胜2负胜KIA", "Samsung beat KIA 3–2 in the playoff"),
    ("白菜一棵5,557韩元", "One cabbage: 5,557 won"),
    ("虾酱涨了32.5%", "Salted shrimp up 32.5%"),
    ("消防日是11月9日周一", "Firefighters' Day is Monday, Nov 9"),
    ("定期报名截止11月10日17点", "Regular sign-up ends Nov 10 at 17:00"),
    ("首尔折扣11月5日至11日", "Seoul discount, Nov 5–11"),
    ("调料里有辣椒粉、大蒜、生姜、虾酱", "The seasoning has chilli powder, garlic, ginger and salted shrimp"),
    ("消防日源于119", "Firefighters' Day comes from 119"),
    ("今年泡菜费由酱类左右", "This year jeot decides the kimchi bill"),
    ("虾酱1公斤20,269韩元", "Salted shrimp: 20,269 won a kilo"),
    ("定期报名截止17点", "Regular sign-up closes at 17:00"),
    ("取消名额报名11月11日至13日", "Cancelled-seat sign-up, Nov 11–13"),
    ("11 月 9 日，还剩 10 天", "Nov 9, 10 days left"),
    ("11 月 12 日，还剩 7 天", "Nov 12, 7 days left"),
    ("11 月 15 日，还剩 4 天", "Nov 15, 4 days left"),
    ("月出山林业厅预报峰值11月9日", "Wolchulsan Forestry Service forecast peak: Nov 9"),
    ("年糕条日从2006年开始", "Garaetteok Day started in 2006"),
    ("预报日期和实际观测日期不同", "Forecast dates and actual observation dates differ"),
    ("实际观测10月16日", "Actual observation: Oct 16"),
    ("11月11日是农民节", "Nov 11 is Farmers' Day"),
    ("年糕条日分享年糕", "On Garaetteok Day, share garaetteok"),
    ("杜鹃山林业厅预报11日", "Duryunsan Forestry Service forecast: the 11th"),
    ("季后赛胜队是三星", "Samsung won the playoff"),
    ("系列赛比分3胜2负", "Series score: 3 wins, 2 losses"),
    ("第5场11月1日大邱三星6比1", "Game 5, Nov 1, Daegu: Samsung 6–1"),
    ("韩国大赛11月3日水原开始", "The Korean Series starts Nov 3 in Suwon"),
    ("报纸11月2日截稿、1至5场结果未知", "Paper closed Nov 2; Games 1–5 results unknown"),
    ("三星3胜2负胜KIA", "Samsung beat KIA 3–2"),
    ("韩国大赛1、2场在水原", "Korean Series Games 1–2 in Suwon"),
    ("开幕因雨和第五场推迟一天", "The opener shifted a day for rain and Game 5"),
    ("先赢4场夺冠、剩余比赛不举行", "First to 4 wins takes the title; the rest are not played"),
    ("预备召集在11月18日周三", "The preliminary assembly is Wednesday, Nov 18"),
    ("考试日8点10分前入场完毕", "On exam day, be seated by 08:10"),
    ("巧克力棒日分享细长饼干", "On Pepero Day, share the thin sticks"),
    ("预备召集领取准考证", "Pick up your ticket at the preliminary assembly"),
    ("带照片的实体身份证", "A physical photo ID"),
    ("预备召集在11月18日", "The preliminary assembly is Nov 18"),
    ("朋友分享巧克力棒", "Friends share Pepero"),
    ("本周倒计时D-10至D-4", "This week the countdown runs D-10 to D-4"),
    ("林业厅标准是叶子50%", "The Forestry Service counts 50% of leaves"),
    ("气象厅观测标准约80%", "The weather service observes about 80%"),
    ("韩国大赛开幕推迟到11月3日", "The Korean Series opener moved to Nov 3"),
    ("日期不同因标准不同", "The dates differ because the criteria differ"),
    ("公布的日程可能改变", "An announced schedule can change"),
    ("结果要等比赛结束", "Results come only after the games"),
    ("预报日期不等于观测日期", "A forecast date is not an observation date"),
    ("不知道结果要说不知道", "If you do not know the result, say so"),
    ("消防日在11月9日周一", "Firefighters' Day is Monday, Nov 9"),
    ("三个名字的日子11月11日", "The three-name day is Nov 11"),
    ("杜鹃山林业厅预报峰值11月11日", "Duryunsan Forestry Service forecast peak: Nov 11"),
    ("季后赛首场10月26日KIA5比1", "Playoff Game 1, Oct 26: KIA 5–1"),
    ("智敏周三分享年糕条", "Jimin shares garaetteok on Wednesday"),
    ("周六帮忙腌泡菜", "On Saturday, help make kimchi"),
    ("语序：主语+时间+宾语+动词", "Word order: subject + time + object + verb"),
    ("对照第 2 版", "From page 2"),
    ("周三分享年糕条", "Sharing garaetteok on Wednesday"),
    ("레벨 A2 · 김장 가격과 겨울 준비, 한능검 · 泡菜价格与过冬准备、韩史考试",
     "레벨 A2 · 김장 가격과 겨울 준비, 한능검 · Kimchi prices, winter prep and the Korean History exam"),
    ("김장 장보기 목록 · 泡菜采购清单", "김장 장보기 목록 · Kimchi shopping list"),
    ("당신은? · 说说你自己", "당신은? · And you?"),
    ("你呢？腌泡菜时你认为最重要的材料是什么？写两句韩语寄来。",
     "And you? What is the most important ingredient when you make kimchi? Write two sentences in Korean and send them in."),
    ("你呢？11月11日想分享巧克力棒还是年糕条？写两句韩语寄来。",
     "And you? On Nov 11, would you share Pepero or garaetteok? Write two sentences in Korean and send them in."),
    ("레벨 A2→B1 · 단풍과 11월 11일의 세 이름 · 红叶与 11 月 11 日的三个名字",
     "레벨 A2→B1 · 단풍과 11월 11일의 세 이름 · Autumn leaves and the three names of Nov 11"),
    ("레벨 B1 · 플레이오프 결과와 한국시리즈 · 季后赛结果与韩国大赛",
     "레벨 B1 · 플레이오프 결과와 한국시리즈 · Playoff result and the Korean Series"),
    ("레벨 B1 · 수능 D-7 주간과 빼빼로데이 · 高考 D-7 周与巧克力棒日",
     "레벨 B1 · 수능 D-7 주간과 빼빼로데이 · The CSAT D-7 week and Pepero Day"),
    ("레벨 B2 · 예보와 발표를 읽는 법 · 预报与发布的读法",
     "레벨 B2 · 예보와 발표를 읽는 법 · How to read forecasts and announcements"),
    ("句式拆解：「在〜之前」。提问：「〜 전에 뭐 해요?」",
     "Frame: “before ~”. Ask: “〜 전에 뭐 해요?”"),
    ("提前盐腌好的白菜", "Cabbage salted in advance"),
    ("调料里有虾酱", "The seasoning has salted shrimp"),
    ("D-4＝11月15日", "D-4 = Nov 15"),
    ("D-7就是还剩一周", "D-7 means one week left"),
    ("发布和结果要区分", "Tell announcements and results apart"),
    ("「듣다」的过去式是「들었어요」。", "The past of 듣다 is 들었어요."),
    ("日期数字要留空格。", "Leave a space after date numbers."),
    ("学习场所用「에서」。", "Use 에서 for the place of study."),
    ("白菜降价了，虾酱却涨价了。", "Cabbage is down, but salted shrimp is up."),
    ("11 月 11 日是有三个名字的日子。", "Nov 11 is a day with three names."),
    ("泡菜季正忙。", "Kimchi season is in full swing."),
    ("离高考还剩 7 天，今天是 D-7。", "Seven days to the CSAT. Today is D-7."),
    ("预报日期和实际观测日期不同。", "Forecast dates and actual observation dates differ."),
    ("结果请在 KBO 官网确认。", "Check the result on the KBO website."),
    ("离高考正好剩一周。", "Exactly one week left to the CSAT."),
    ("把日期、标准和结果分开。", "Separate the date, the criterion and the result."),
    ("11月12日是D-7。", "Nov 12 is D-7."),
    ("11月11日有三个名字。→ ___", "Nov 11 has three names. → ___"),
    ("我周三和朋友分享年糕条。→ ___", "On Wednesday I share garaetteok with a friend. → ___"),
    ("Use 「에서」 for the place of an action", "Use 에서 for the place of an action"),
    ("내장산=公团预报11日 b", "내장산 = parks agency forecast, the 11th b"),
    ("월출산=林业厅预报9日 a", "월출산 = Forestry Service forecast, the 9th a"),
    ("두륜산=林业厅预报11日 d", "두륜산 = Forestry Service forecast, the 11th d"),
    ("플레이오프=三星3胜2负 d", "플레이오프 = Samsung 3–2 d"),
    ("한국시리즈=kt对三星 a", "한국시리즈 = kt vs Samsung a"),
    ("이동일=系列赛之间一天 c", "이동일 = one day between series c"),
    ("把词和说明配对", "Match the words to the notes"),
    ("系列赛之间需要一天移动日", "A travel day is needed between series"),
    ("밀리다的过去式밀렸어요", "The past of 밀리다 is 밀렸어요"),
    ("다음 주 · 下期预告 (VOL.4)", "다음 주 · Next week (VOL.4)"),
]


def apply_letters(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    out = []
    for ln in lines:
        s = ln.strip()
        if s.startswith('lcn = "'):
            out.append('lcn = "' + NEW_LCN + '"')
        elif s.startswith('lko = "') or s.startswith('lcn2 = "'):
            out.append("")
        elif s.startswith("lh = 62 + len(wrap(lt,"):
            out.append('lh = 62 + len(wrap(lt, "serif", False, 21.5, CW - 44)) * 30.5 + 12 + len(wrap(lcn, "sans", False, 20, CW - 44)) * 29 + 26')
        elif ", lko, " in ln or ", lcn2, " in ln:
            out.append("")
        else:
            out.append(ln)
    text = "\n".join(out)
    assert "lko" not in text and "lcn2" not in text, "letters leftovers"
    assert NEW_LCN in text
    open(path, "w", encoding="utf-8").write(text)
    print("  letters rebuilt (en)")


def main():
    build = HERE
    # GEOM first (whole-line, W46 lines)
    p12 = os.path.join(build, "content12.py")
    text = open(p12, encoding="utf-8").read()
    for old, new in GEOM:
        n = text.count(old)
        if n == 0 and new.split("\n")[-1] in text:
            print(f"  GEOM already-applied: {old[:50]!r}")
            continue
        assert n == 1, f"GEOM NOT FOUND (x{n}): {old[:60]!r}"
        text = text.replace(old, new)
        print(f"  GEOM x{n} {old[:50]!r}")
    open(p12, "w", encoding="utf-8").write(text)
    # letters (content7 structural)
    apply_letters(os.path.join(build, "content7.py"))
    # SUPP longest-first across content files
    files = ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]
    texts = {f: open(os.path.join(build, f), encoding="utf-8").read() for f in files}
    for old, new in sorted(SUPP, key=lambda p: -len(p[0])):
        hit = False
        for f in files:
            n = texts[f].count(old)
            if n >= 1:
                texts[f] = texts[f].replace(old, new)
                hit = True
                print(f"  SUPP {f} x{n} {old[:44]!r} -> {new[:44]!r}")
        if not hit:
            already = any(new in texts[f] for f in files)
            assert already, f"SUPP NOT FOUND (and new absent): {old[:60]!r}"
            print(f"  SUPP already-applied: {old[:44]!r}")
    for f in files:
        open(os.path.join(build, f), "w", encoding="utf-8").write(texts[f])
    print("SUPP-EN DONE")


if __name__ == "__main__":
    main()
