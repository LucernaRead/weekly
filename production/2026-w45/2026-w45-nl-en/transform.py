# -*- coding: utf-8 -*-
"""One-off fan-out transform: W45 NL core (Chinese explanations) -> NL x EN.
Line-literal replacements only, each asserted. Run once from this dir.
Dutch target text, keys (except re-aimed E137/E138), facts, images: untouched.
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
R = []  # (file, old, new)

def rep(f, old, new):
    R.append((f, old, new))

def rep_opt(f, old, new):
    R.append((f, old, new, True))

# ---------- global path / furniture ----------
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep(f, "weekly-report-w45-nl-core/svg", "weekly-report-w45-nl-en/svg")
rep("render.py", "weekly-report-w45-nl-core", "weekly-report-w45-nl-en")
rep("render.py", "De-Lucerna-VOL2.pdf", "De-Lucerna-VOL2-EN.pdf")
rep("render.py", "De-Lucerna-VOL2-web.pdf", "De-Lucerna-VOL2-EN-web.pdf")
rep("render.py", "Render the IT weekly", "Render the NL x EN weekly")
rep("run.py", "Run the IT weekly", "Run the NL x EN weekly")

# ---------- bslib4: footer + gloss prefix (W43 NL x EN measured) ----------
rep("bslib4.py", "De Lucerna · 荷兰语周报 VOL.2 · LUCERNA DUTCH WEEKLY",
     "De Lucerna · VOL.2 · Dutch text · English explanations · LUCERNA DUTCH WEEKLY")
rep("bslib4.py", 'f"第 {n} 版 / 共 {total} 版"', 'f"Page {n} of {total}"')
rep("bslib4.py", "译注｜", "Note | ")

# ---------- types + instr (global; E-item instrs handled per-line below) ----------
# order: instrs FIRST (else the bare type replacement would eat instr values),
# and cloze before plain choice.
for f in ["content12.py", "content34.py", "content56.py", "content7.py", "content8.py"]:
    rep_opt(f, 'instr="填空"', 'instr="Fill in"')
    rep_opt(f, 'instr="判断"', 'instr="True or false?"')
    rep_opt(f, 'instr="造句"', 'instr="Make the sentence"')
    rep_opt(f, 'instr="写作"', 'instr="Write"')
    rep_opt(f, "完形单选", "cloze choice")
    rep_opt(f, "完成句子", "complete")
    rep_opt(f, "词汇配对", "matching")
    rep_opt(f, "判断对错", "true or false")
    rep_opt(f, "单选", "choice")
    rep_opt(f, "造句", "make sentences")
    rep_opt(f, "翻译", "translate")
    rep_opt(f, "写作", "writing")
rep("content8.py", 'if e_["type"] == "writing":', 'if e_["type"] == "writing":')
# E-item directions (per body line, after the global instr pass left instr="translate")
rep("content8.py", '"De Klimaatweek duurt zeven dagen. → ___", instr="translate"',
     '"De Klimaatweek duurt zeven dagen. → ___", instr="Translate into English"')
rep("content8.py", '"Code oranje betekent: bereid je voor. → ___", instr="translate"',
     '"Code oranje betekent: bereid je voor. → ___", instr="Translate into English"')
rep("content8.py", '"博物馆之夜从晚上 19 点到凌晨 2 点。→ ___", instr="translate"',
     '"Museum Night lasts from 19:00 to 02:00. → ___", instr="Translate into Dutch"')
rep("content8.py", '"我参加气候周。→ ___", instr="translate"',
     '"I take part in the Climate Week. → ___", instr="Translate into Dutch"')

# ---------- content12: P1 ----------
rep("content12.py", "ELKE WEEK IN HET NEDERLANDS · 每周一期 · 读荷兰人正在读的荷兰语",
     "ELKE WEEK IN HET NEDERLANDS · EVERY WEEK · REAL DUTCH")
rep("content12.py", "荷 兰 语 周 报 · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12",
     "WEEKBLAD IN HET NEDERLANDS · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12")
rep("content12.py", 'p.text(975, 372, "DE WEKELIJKSE KRANT OM NEDERLANDS TE LEREN — HET ECHTE NEDERLAND, IN HET NEDERLANDS", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 372, "TEXT IN DUTCH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS", 20, "sans", True, OLIVE, anchor="middle")')
rep("content12.py", '"气候周"', '"CLIMATE WEEK"')
rep("content12.py", '"本周全国气候周 · 详见第 2 版"', '"The whole country joins in · see page 2"')
rep("content12.py", '"HET NIEUWS · 头条"', '"HET NIEUWS · TOP STORY"')
rep("content12.py", 'f.bridge("讲解｜de Klimaatweek 气候周 · de boom planten 种树 · besparen 节约 · de waarschuwing 警告、预警。")',
     'f.bridge("Note | de Klimaatweek = Climate Week · de boom planten = to plant a tree · besparen = to save · de waarschuwing = warning.")')
rep("content12.py", '"DE WEEK IN CIJFERS · 数字看本周"', '"DE WEEK IN CIJFERS · IN NUMBERS"')
rep("content12.py", "（气候周的天数）", "(the days of the Climate Week)")
rep("content12.py", "（周六科弗登发放的树木和灌木）", "(the trees and shrubs Coevorden gives away on Saturday)")
rep("content12.py", "（博物馆之夜开放的博物馆，70 多家）", "(the museums open on Museum Night, 70+)")
rep("content12.py", "（荷甲第 12 轮的比赛场数）", "(the matches of Eredivisie matchday 12)")
rep("content12.py", '"NU JIJ · 即学即练"', '"NU JIJ · YOUR TURN"')
rep("content12.py", '"气候周 11 月 2–8 日"', '"The Climate Week runs 2–8 November"')
rep("content12.py", '"科弗登发放 200 棵树木灌木"', '"Coevorden gives away 200 trees and shrubs"')
rep("content12.py", '"博物馆之夜在 11 月 7 日周六"', '"Museum Night is on Saturday 7 November"')
rep("content12.py", '"海伦芬–费耶诺德 11:15 开球"', '"Heerenveen–Feyenoord kicks off at 11:15"')
rep("content12.py", '"特温特–阿贾克斯 13:30 开球"', '"Twente–Ajax kicks off at 13:30"')
rep("content12.py", '"veel mensen → planten"', '"Plural subject, so planten"')
rep("content12.py", '"· 本周日程"', '"· THIS WEEK"')
rep("content12.py", '"Agenda van de week · 本周大事"', '"Agenda van de week · THIS WEEK\'S EVENTS"')
rep("content12.py", '"本周日程见第 2–4 版文章"', '"See the articles on pages 2–4 for all dates and times."')
rep("content12.py", '"IN DEZE EDITIE · 本期目录"', '"IN DEZE EDITIE · IN THIS ISSUE"')
rep("content12.py", '"“气候”：我们周围长期的天气与自然。气候周讲的就是我们的气候。"',
     '"«Climate»: the weather and nature around us, over a long time. The Climate Week is about our climate."')
rep("content12.py", '"IN HET KORT · 快讯"', '"IN HET KORT · IN BRIEF"')
rep("content12.py", '"BLIKSEMQUIZ · 闪电问答"', '"BLIKSEMQUIZ · LIGHTNING QUIZ"')
rep("content12.py", '"读头版，选出正确答案 · 答案见第 8 版"', '"Read page 1, choose the right answer · answers on page 8"')
rep("content12.py", '"气候周共 7 天（11 月 2–8 日）"', '"The Climate Week lasts 7 days (2–8 November)"')
rep("content12.py", '"博物馆之夜在阿姆斯特丹"', '"Museum Night is in Amsterdam"')
rep("content12.py", '"特温特–阿贾克斯 13:30 开球"', '"Twente–Ajax kicks off at 13:30"')
# ---------- content12: P2 ----------
rep("content12.py", 'p.band("LEVEN · 生活", "De Lucerna", "NIVEAU A2 · De Klimaatweek, stap voor stap · 一步一步讲气候周")',
     'p.band("LEVEN · LIFE", "De Lucerna", "NIVEAU A2 · De Klimaatweek, stap voor stap · The Climate Week, step by step")')
rep("content12.py", '"ZO ONTHOUD JE HET · 口诀"', '"ZO ONTHOUD JE HET · REMEMBER"')
rep("content12.py", 'f.gloss("het klimaat 气候 · wortelen 生根 · besparen 节约 · de verwarming 暖气 · de waarschuwing 预警 · lokaal 当地的、本地的。")',
     'f.gloss("het klimaat = climate · wortelen = to take root · besparen = to save · de verwarming = heating · de waarschuwing = warning · lokaal = local.")')
rep("content12.py", '"气候周你做什么？种树、节约能源还是骑车。写两句荷兰语寄给编辑部。"',
     '"What do you do in the Climate Week: plant a tree, save energy or cycle? Write two sentences in Dutch and send them to the editors."')
rep("content12.py", '"EN JIJ? · 说说你自己"', '"EN JIJ? · AND YOU?"')
rep("content12.py", '"DE CODES VAN HET KNMI · 气象预警颜色"', '"DE CODES VAN HET KNMI · KNMI CODES"')
rep("content12.py", '"Wat betekent elke kleur? · 每种颜色是什么意思"', '"What does each colour mean?"')
rep("content12.py", '"天气可能危险，要当心"', '"The weather may be dangerous: take care"')
rep("content12.py", '"危险，做好准备"', '"Dangerous: be prepared"')
rep("content12.py", '"非常危险，尽量待在室内"', '"Very dangerous: stay indoors if you can"')
rep("content12.py", '"预警针对你所在的地区"', '"The warning is for your own area"')
rep("content12.py", '"OEFENINGEN · 第 2 版练习"', '"OEFENINGEN · EXERCISES ON PAGE 2"')
rep("content12.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Answers on page 8 · levels are mixed; find your number"')
rep("content12.py", 'e.bridge("读第 2 版文章，选出正确答案。")', 'e.bridge("Read the article on page 2 and choose the right answer.")')
rep("content12.py", '"气候周不做：更多开车"', '"Not a Climate Week action: driving more"')
rep("content12.py", '"红色预警：非常危险，待在室内"', '"Code red: very dangerous, stay indoors"')
rep("content12.py", '"预警针对本地，不针对整个省"', '"Warnings are local, not for a whole province"')
rep("content12.py", '"节约能源：暖气调低一度"', '"Saving energy: turning the heating down one degree"')
rep("content12.py", 'e.bridge("用第 2 版的词填空。")', 'e.bridge("Fill in with words from page 2.")')
rep("content12.py", '"气候周 11 月 2–8 日共 7 天"', '"The Climate Week, 2–8 November, lasts 7 days"')
rep("content12.py", '"wortelen = 生根（复数主语）"', '"wortelen = to take root (plural subject)"')
rep("content12.py", '"besparen = 节约"', '"besparen = to save"')
rep("content12.py", '"fiets = 自行车"', '"fiets = bicycle"')
rep("content12.py", '"发放地点在兹韦洛"', '"The giveaway place is Zweeloo"')
rep("content12.py", 'e.bridge("用颜色代码和日期填空。")', 'e.bridge("Fill in the colour codes and dates.")')
rep("content12.py", '"黄色代码：当心"', '"Code yellow: take care"')
rep("content12.py", '"橙色代码：危险"', '"Code orange: dangerous"')
rep("content12.py", '"发放从 13:00 开始"', '"The giveaway starts at 13:00"')
rep("content12.py", '"气候周 11 月 8 日周日结束"', '"The Climate Week ends on Sunday 8 November"')
rep("content12.py", '["Klimaatweek=气候周 b", "besparen=节约 d", "waarschuwing=预警 a", "lokaal=本地的 c"]',
     '["Klimaatweek = Climate Week b", "besparen = to save d", "waarschuwing = warning a", "lokaal = local c"]')
rep("content12.py", 'instr="把词和释义配对"', 'instr="Match word to meaning"')

# ---------- content34: P3 ----------
rep("content34.py", 'p.band("CULTUUR · 文化", "De Lucerna", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · 博物馆之夜、书籍与艺术")',
     'p.band("CULTUUR · CULTURE", "De Lucerna", "NIVEAU A2 → B1 · Museumnacht, boeken en kunst · Museum Night, books and art")')
rep("content34.py", 'f.gloss("het museum 博物馆 · de rondleiding 导览 · het tijdslot 时间段 · tweedehands 二手的 · de beurs 展会、集市。")',
     'f.gloss("het museum = museum · de rondleiding = guided tour · het tijdslot = time slot · tweedehands = second-hand · de beurs = fair, market.")')
rep("content34.py", '"OEFENINGEN · 第 3 版练习"', '"OEFENINGEN · EXERCISES ON PAGE 3"')
rep("content34.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Answers on page 8 · levels are mixed; find your number"')
rep("content34.py", 'e.bridge("读第 3 版文章，选出正确答案。")', 'e.bridge("Read the article on page 3 and choose the right answer.")')
rep("content34.py", '"博物馆之夜在 11 月 7 日周六"', '"Museum Night is on Saturday 7 November"')
rep("content34.py", '"博物馆开放到凌晨 2 点"', '"The museums are open until 02:00"')
rep("content34.py", '"Crossing Border 在海牙"', '"Crossing Border is in The Hague"')
rep("content34.py", '"Crossing Border 结合书籍与音乐"', '"Crossing Border combines books and music"')
rep("content34.py", '"PAN 艺术博览会到 11 月 8 日"', '"The PAN art fair runs until 8 November"')
rep("content34.py", 'e.bridge("用方框里的词填空。注意：有的词要变成复数。")',
     'e.bridge("Fill in with the words from the box. Note: some words must become plural.")')
rep("content34.py", '"museum 复数：musea"', '"museum plural: musea"')
rep("content34.py", '"rondleiding = 导览"', '"rondleiding = guided tour"')
rep("content34.py", '"tijdslot = 时间段"', '"tijdslot = time slot"')
rep("content34.py", '"tweedehands = 二手的"', '"tweedehands = second-hand"')
rep("content34.py", '"beurs = 展会、集市"', '"beurs = fair, market"')
rep("content34.py", 'e.bridge("用现在完成时补全，注意助动词 hebben/zijn。")',
     'e.bridge("Complete with the present perfect. Watch the auxiliary verbs hebben/zijn.")')
rep("content34.py", '"zijn 的 perfectum：zijn geweest"', '"zijn perfectum: zijn geweest"')
rep("content34.py", '"kopen 的 perfectum：hebben gekocht"', '"kopen perfectum: hebben gekocht"')
rep("content34.py", '"voorlezen 的 perfectum：hebben voorgelezen"', '"voorlezen perfectum: hebben voorgelezen"')
rep("content34.py", '"komen 用 zijn：zijn gekomen"', '"komen takes zijn: zijn gekomen"')
rep("content34.py", 'e.bridge("算一算：用第 3 版的数字回答。")', 'e.bridge("Work it out: answer with the numbers from page 3.")')
rep("content34.py", '"19:00 到 02:00 共 7 小时"', '"19:00 to 02:00 is 7 hours"')
rep("content34.py", '"11 月 1–8 日共 8 天"', '"1–8 November is 8 days"')
rep("content34.py", '"11 月 3–8 日共 6 天"', '"3–8 November is 6 days"')
rep("content34.py", '"250 的一半是 125"', '"Half of 250 is 125"')
# ---------- content34: P4 ----------
rep("content34.py", 'p.band("SPORT · 体育", "De Lucerna", "NIVEAU B1 · Europese week en speelronde 12 · 欧战周与第 12 轮")',
     'p.band("SPORT", "De Lucerna", "NIVEAU B1 · Europese week en speelronde 12 · European week and matchday 12")')
rep("content34.py", 'f.gloss("de balans 成绩单、总结 · gelijkspelen 打平 · de speelronde 轮次 · de topper 焦点战 · de stand 积分榜。")',
     'f.gloss("de balans = the final tally · gelijkspelen = to draw · de speelronde = matchday · de topper = the top match · de stand = the table.")')
rep("content34.py", '"OEFENINGEN · 第 4 版练习"', '"OEFENINGEN · EXERCISES ON PAGE 4"')
rep("content34.py", 'e.bridge("读第 4 版文章，选出正确答案。")', 'e.bridge("Read the article on page 4 and choose the right answer.")')
rep("content34.py", '"阿贾克斯 2–0 赢亚特兰大"', '"Ajax beat Atalanta 2–0"')
rep("content34.py", '"特温特 4–1 赢林肯红魔"', '"Twente beat Lincoln 4–1"')
rep("content34.py", '"NEC 2–4 输给萨格勒布迪纳摩"', '"NEC lost 2–4 to Dinamo Zagreb"')
rep("content34.py", '"皇家贝蒂斯 1–0 赢费耶诺德"', '"Real Betis beat Feyenoord 1–0"')
rep("content34.py", '"10 轮后费耶诺德 24 分领跑"', '"After 10 rounds Feyenoord lead with 24 points"')
rep("content34.py", 'e.bridge("用方框里的词填空。注意动词形式。")',
     'e.bridge("Fill in with the words from the box. Watch the verb forms.")')
rep("content34.py", '"balans = 成绩单、总结"', '"balans = the final tally"')
rep("content34.py", '"gelijkspelen 过去时复数：speelden gelijk"', '"gelijkspelen past tense plural: speelden gelijk"')
rep("content34.py", '"topper = 焦点战"', '"topper = the top match"')
rep("content34.py", '"stand = 积分榜"', '"stand = the table"')
rep("content34.py", '"doelpunt = 进球"', '"doelpunt = goal"')
rep("content34.py", 'e.bridge("用过去时或完成时补全。")', 'e.bridge("Complete with the past tense or the perfect tense.")')
rep("content34.py", '"winnen 过去时：won"', '"winnen past tense: won"')
rep("content34.py", '"gaan 过去时：ging"', '"gaan past tense: ging"')
rep("content34.py", '"verliezen 过去时：verloor"', '"verliezen past tense: verloor"')
rep("content34.py", '"komen 的 perfectum 用 zijn"', '"komen perfectum takes zijn"')
rep("content34.py", '"对：阿贾克斯 2–0 获胜"', '"True: Ajax won 2–0"')
rep("content34.py", '"错：NEC 2–4 输了"', '"False: NEC lost 2–4"')
rep("content34.py", '"错：特温特–阿贾克斯 13:30；11:15 是海伦芬–费耶诺德"', '"False: Twente–Ajax is at 13:30; 11:15 is Heerenveen–Feyenoord"')
rep("content34.py", '"对：10 轮后费耶诺德 24 分第一"', '"True: after 10 rounds Feyenoord lead with 24 points"')

# ---------- content56: P5 ----------
rep("content56.py", 'p.band("JONGEREN · 青年", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · 荒岛节目开播、音乐节与设计周落幕")',
     'p.band("JONGEREN · YOUNG PEOPLE", "De Lucerna", "NIVEAU B1 · Robinson is begonnen, ADE en DDW voorbij · Robinson has started, ADE and DDW are over")')
rep("content56.py", "（周日晚 20:00 在 RTL 4 收看）", "(watch on RTL 4 on Sunday at 20:00)")
rep("content56.py", "（注意比赛项目：分数在那里决出）", "(watch the trials: that is where the points are won)")
rep("content56.py", "（和朋友猜谁能留到最后）", "(guess with friends who stays longest)")
rep("content56.py", "（下周这里继续报道进展）", "(next week you read here how it went on)")
rep("content56.py", 'f.gloss("het eiland 岛 · de proef 比赛项目、考验 · stemmen 投票 · de aflevering （一）集 · voorbij 过去了、结束了。")',
     'f.gloss("het eiland = island · de proef = trial, challenge · stemmen = to vote · de aflevering = episode · voorbij = over, finished.")')
rep("content56.py", '"你看《荒岛远征》吗，还是更爱自己出门活动？写两句荷兰语寄来。"',
     '"Do you watch Expeditie Robinson, or would you rather do something outside yourself? Write two sentences in Dutch and send them in."')
rep("content56.py", '"EN JIJ? · 说说你自己"', '"EN JIJ? · AND YOU?"')
rep("content56.py", '"OEFENINGEN · 第 5 版练习"', '"OEFENINGEN · EXERCISES ON PAGE 5"')
rep("content56.py", '"答案见第 8 版 · 题目可跨级混排，按题号找答案"', '"Answers on page 8 · levels are mixed; find your number"')
rep("content56.py", 'e.bridge("读第 5 版文章，选出正确答案。")', 'e.bridge("Read the article on page 5 and choose the right answer.")')
rep("content56.py", '"Robinson 在 11 月 1 日周日开始"', '"Robinson started on Sunday 1 November"')
rep("content56.py", '"19 位参赛者"', '"19 contestants"')
rep("content56.py", '"ADE 今年 30 年"', '"ADE turned 30 this year"')
rep("content56.py", '"设计周约 2.500 位设计师"', '"The Design Week showed about 2,500 designers"')
rep("content56.py", '"ADE 与 DDW 在 10 月 25 日周日落幕"', '"ADE and DDW closed on Sunday 25 October"')
rep("content56.py", 'e.bridge("用方框里的词填空。")', 'e.bridge("Fill in with the words from the box.")')
rep("content56.py", '"eiland = 岛（het）"', '"eiland = island (het)"')
rep("content56.py", '"proef = 比赛项目、考验（de）"', '"proef = trial, challenge (de)"')
rep("content56.py", '"stemmen = 投票"', '"stemmen = to vote"')
rep("content56.py", '"aflevering = （一）集"', '"aflevering = episode"')
rep("content56.py", '"voorbij = 过去了、结束了"', '"voorbij = over, finished"')
rep("content56.py", '"kandidaat 复数：kandidaten"', '"kandidaat plural: kandidaten"')
rep("content56.py", 'e.bridge("用 gaan + 不定式说将来。")', 'e.bridge("Use gaan + infinitive to talk about the future.")')
rep("content56.py", '"gaat winnen = 会赢（只是猜测）"', '"gaat winnen = will win (just a guess)"')
rep("content56.py", '"wij → gaan + 不定式 kijken"', '"wij → gaan + infinitive kijken"')
rep("content56.py", '"hij → gaat praten"', '"hij → gaat praten"')
rep("content56.py", '"zij (复数) → gaan zoeken"', '"zij (plural) → gaan zoeken"')
rep("content56.py", '"对：11 月 1 日开始"', '"True: it started on 1 November"')
rep("content56.py", '"错：ADE 今年 30 年"', '"False: ADE turned 30 this year"')
rep("content56.py", '"错：10 月 25 日已落幕"', '"False: it already closed on 25 October"')
# ---------- content56: P6 ----------
rep("content56.py", 'p.band("VERDIEPING · 深读", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · 气象预警深度解读")',
     'p.band("VERDIEPING · IN DEPTH", "De Lucerna", "NIVEAU B2 · De codes van het KNMI · The KNMI codes")')
rep("content56.py", 'f.gloss("de meteoroloog 气象学家 · waarschuwingsmoeheid 预警疲劳 · vastzetten 固定好 · het advies 建议、忠告 · de voorstander 支持者。")',
     'f.gloss("de meteoroloog = meteorologist · waarschuwingsmoeheid = warning fatigue · vastzetten = to secure, fasten · het advies = advice · de voorstander = supporter.")')
rep("content56.py", '"练习数据：虚构数字，仅供练习，非真实调查。问题：橙色预警时你会怎么做？（100 名年轻人）"',
     '"Practice data: invented numbers for practice only, not a real survey. Question: what do you do at code orange? (100 young people)"')
rep("content56.py", '"DE GRAFIEK · 图表（练习数据）"', '"DE GRAFIEK · CHART (PRACTICE DATA)"')
rep("content56.py", '"VOOR OF TEGEN? · 正方还是反方"', '"VOOR OF TEGEN? · FOR OR AGAINST?"')
rep("content56.py", '"OEFENINGEN · 第 6 版练习"', '"OEFENINGEN · EXERCISES ON PAGE 6"')
rep("content56.py", 'e.bridge("看第 6 版图表（练习数据）回答。")', 'e.bridge("Answer from the chart on page 6 (practice data).")')
rep("content56.py", '"45 名年轻人选择待在家里"', '"45 young people choose to stay home"')
rep("content56.py", '"25 人先看预警文字"', '"25 first read the warning text"')
rep("content56.py", '"45 + 25 = 70"', '"45 + 25 = 70"')
rep("content56.py", '"10 人不知道"', '"10 do not know"')
rep("content56.py", '"图表共 100 人：45+25+20+10"', '"The chart counts 100 people: 45+25+20+10"')
rep("content56.py", 'e.bridge("读第 6 版文章，选出正确答案。")', 'e.bridge("Read the article on page 6 and choose the right answer.")')
rep("content56.py", '"以前预警针对整个省"', '"Warnings used to cover a whole province"')
rep("content56.py", '"如今预警是本地的"', '"Now warnings are local"')
rep("content56.py", '"红色：非常危险，非必要不上路"', '"Code red: very dangerous, do not go out unless you must"')
rep("content56.py", '"预警疲劳：警告太多导致不再注意"', '"Warning fatigue: too many warnings, so people stop paying attention"')
rep("content56.py", '"KNMI 说：看代码旁边的文字"', '"The KNMI says: read the text next to the code"')
rep("content56.py", '"lokaal = 本地的"', '"lokaal = local"')
rep("content56.py", '"waarschuwingsmoeheid = 预警疲劳"', '"waarschuwingsmoeheid = warning fatigue"')
rep("content56.py", '"vastzetten = 固定好"', '"vastzetten = to secure, fasten"')
rep("content56.py", '"advies = 建议（het）"', '"advies = advice (het)"')
rep("content56.py", 'e.bridge("把词组成正确的句子。")', 'e.bridge("Put the words in the right order to make sentences.")')
rep("content56.py", '"主语 + 动词 + 地点"', '"Subject + verb + place"')
rep("content56.py", '"祈使句：动词在首位"', '"Imperative: the verb comes first"')
rep("content56.py", '"weinig voor = 很少出现"', '"weinig voor = rarely occurs"')
rep("content56.py", '"raakt + 宾语 + 方式"', '"raakt + object + manner"')

# ---------- content7: P7 ----------
rep("content7.py", 'p.band("TAAL · 语言", "De Lucerna", "聚焦语言 · Drie niveaus, drie gereedschappen · 三个级别，三件工具")',
     'p.band("TAAL · LANGUAGE", "De Lucerna", "Language focus · Drie niveaus, drie gereedschappen · Three levels, three tools")')
rep("content7.py", 'a.bridge("het klimaat 气候（长期）；een boom planten 种树；besparen 节约；de waarschuwing 预警。")',
     'a.bridge("het klimaat = climate (long-term); een boom planten = to plant a tree; besparen = to save; de waarschuwing = warning.")')
rep("content7.py", '"wij → planten"', '"wij → planten"')
rep("content7.py", '"je → bespaar"', '"je → bespaar"')
rep("content7.py", '"气候是长期的天气与自然"', '"Climate is the weather and nature over a long time"')
rep("content7.py", '"rood = blijf binnen"', '"rood = stay indoors"')
rep("content7.py", 'b.bridge("meedoen 参加：ik doe mee；opruimen 收拾：wij hebben opgeruimd；vastzetten 固定：zij zette vast。")',
     'b.bridge("meedoen = to take part: ik doe mee; opruimen = to tidy up: wij hebben opgeruimd; vastzetten = to secure: zij zette vast.")')
rep("content7.py", '"ik → doe mee"', '"ik → doe mee"')
rep("content7.py", '"opruimen 的分词：opgeruimd"', '"opruimen past participle: opgeruimd"')
rep("content7.py", '"vastzetten 过去时：zette vast"', '"vastzetten past tense: zette vast"')
rep("content7.py", '"meedoen = 参加、参与"', '"meedoen = to take part"')
rep("content7.py", 'c.bridge("Ik vind dat… 我认为；Volgens mij… 依我看；Het lijkt me dat… 在我看来。")',
     'c.bridge("Ik vind dat… = I think that…; Volgens mij… = In my opinion…; Het lijkt me dat… = It seems to me that…")')
rep("content7.py", '"Volgens mij… = 依我看"', '"Volgens mij… = In my opinion…"')
rep("content7.py", '"Ik vind dat… 表达看法"', '"Ik vind dat… expresses an opinion"')
rep("content7.py", '"Het lijkt me dat… = 在我看来"', '"Het lijkt me dat… = It seems to me that…"')
rep("content7.py", '"气候是长期的天气自然，不是今天的天气。"', '"Climate is the weather and nature over a long time, not today\'s weather."')
rep("content7.py", '"Klimaatweek 是专名，首字母大写。"', '"Klimaatweek is a name, so it takes a capital letter."')
rep("content7.py", '"een 是单数：een boom；复数直接用 bomen。"', '"«Een» is singular: «een boom» or «bomen»."')
rep("content7.py", '"omdat 从句后，主句动词在第二位：blijf ik thuis。"', '"After «omdat», the main-clause verb comes second: «... blijf ik thuis»."')
rep("content7.py", '"PAS OP! · 易错诊所"', '"PAS OP! · ERROR CLINIC"')
rep("content7.py", '"meedoen = 参加、参与：气候周全荷兰都参加。"', '"meedoen = to take part: the whole of the Netherlands takes part in the Climate Week."')
rep("content7.py", '"HET WOORD · 本周生词"', '"HET WOORD · WORD OF THE WEEK"')
# readers' corner: Dutch example + Dutch disclosure stay verbatim (frozen apparatus);
# the Chinese disclosure + invitation lines become English.
rep("content7.py", 'dt_zh = "截稿时未收到真实来信或第 8 版最佳作文，刊登示例信，承诺顺延 VOL.3。"',
     'dt_en = "At press time, no real letters or best page-8 texts had arrived — so here is an example instead; the promise carries to VOL.3."')
rep("content7.py", 'len(wrap(dt_zh, "sans", False, 20, CW - 44))', 'len(wrap(dt_en, "sans", False, 20, CW - 44))')
rep("content7.py", 'p.para(bx + 22, yy3 + 20, dt_zh, 20, "sans", False, GREY, CW - 44, 1.42) + 10',
     'p.para(bx + 22, yy3 + 20, dt_en, 20, "sans", False, GREY, CW - 44, 1.42) + 10')
rep("content7.py", '"编辑部示例信，非真实来信。欢迎寄来你的真实来信和第 8 版最佳作文，VOL.3 刊登！"',
     '"Editors\' example — not a real letter. Send your real letters and your best page-8 texts to the editors: we will print them in VOL.3!"')
rep("content7.py", '"ZINNEN VAN DE WEEK · 本周金句（逐字摘自本期文章）"',
     '"ZINNEN VAN DE WEEK · PHRASES OF THE WEEK (VERBATIM FROM THIS ISSUE)"')
rep("content7.py", '"从 11 月 2 日周一到 8 日周日，荷兰是气候周。"', '"From Monday 2 to Sunday 8 November, it is Climate Week in the Netherlands."')
rep("content7.py", '"秋天是种树的最好时节。"', '"Autumn is the best time to plant."')
rep("content7.py", '"黄色意味着：当心，天气可能危险。"', '"Yellow means: take care, the weather may be dangerous."')
rep("content7.py", '"70 多家博物馆从晚上 19 点开放到凌晨 2 点。"', '"More than 70 museums are open from 19:00 in the evening to 02:00 at night."')
rep("content7.py", '"阿贾克斯 10 月 22 日周四 2–0 战胜亚特兰大。"', '"On Thursday 22 October Ajax beat Atalanta 2–0."')
rep("content7.py", '"11 月 1 日周日，《荒岛远征》在 RTL 4 开播，20 点。"', '"On Sunday 1 November Expeditie Robinson started on RTL 4, at 20:00."')
rep("content7.py", '"预警代码不是禁令，而是一条建议。"', '"A code is not a ban, but advice."')
rep("content7.py", '"天气属于我们所有人，但对每个人的影响各不相同。"', '"The weather belongs to us all, but it affects us all differently."')
rep("content7.py", '"VOLGENDE WEEK · 下期预告 (VOL.3)"', '"VOLGENDE WEEK · NEXT WEEK (VOL.3)"')
# ---------- content8: P8 ----------
rep("content8.py", 'p.band("TOETS EN ANTWOORDEN · 练习与答案", "De Lucerna", "第 8 版 · De grote toets van de week + alle antwoorden")',
     'p.band("TOETS EN ANTWOORDEN · TEST AND ANSWERS", "De Lucerna", "Page 8 · De grote toets van de week + alle antwoorden")')
rep("content8.py", '"科弗登发放 200 棵树木灌木"', '"Coevorden gives away 200 trees and shrubs"')
rep("content8.py", '"特温特–阿贾克斯 13:30 开球"', '"Twente–Ajax kicks off at 13:30"')
rep("content8.py", '"阿贾克斯 2–0 赢亚特兰大"', '"Ajax beat Atalanta 2–0"')
rep("content8.py", '"气候周到 11 月 8 日"', '"The Climate Week runs to 8 November"')
rep("content8.py", '"博物馆之夜在 11 月 7 日"', '"Museum Night is on 7 November"')
rep("content8.py", '"Robinson 在 11 月开始"', '"Robinson started in November"')
rep("content8.py", '"橙色预警：天气危险"', '"Code orange: the weather is dangerous"')
rep("content8.py", '"meedoen = 参加"', '"meedoen = to take part"')
rep("content8.py", '"气候周 11 月 2 日周一开始"', '"The Climate Week starts on Monday 2 November"')
rep("content8.py", '"发放地点在兹韦洛"', '"The giveaway place is Zweeloo"')
rep("content8.py", '"Crossing Border 在海牙"', '"Crossing Border is in The Hague"')
rep("content8.py", '"PAN 在 RAI 展览中心"', '"PAN is at the RAI"')
rep("content8.py", '"皇家贝蒂斯 1–0 赢费耶诺德"', '"Real Betis beat Feyenoord 1–0"')
rep("content8.py", '"10 轮后阿贾克斯 21 分"', '"After 10 rounds Ajax have 21 points"')
rep("content8.py", '"预警疲劳：警告太多导致不再注意"', '"Warning fatigue: too many warnings, so people stop paying attention"')
rep("content8.py", '"扎安丹旧货市场约 250 个摊位"', '"The Zaandam flea market has about 250 stalls"')
rep("content8.py", '"Daan 住在科弗登"', '"Daan lives in Coevorden"')
rep("content8.py", '"他周六领了一棵免费灌木"', '"On Saturday he picks up a free shrub"')
rep("content8.py", '"周日特温特对阿贾克斯"', '"On Sunday Twente play Ajax"')
rep("content8.py", '"气候周他每天骑车上学"', '"In the Climate Week he cycles to school every day"')
rep("content8.py", '"主语 + 动词 + 时间"', '"Subject + verb + time"')
rep("content8.py", '"主语 + 动词 + 宾语 + 地点"', '"Subject + verb + object + place"')
rep("content8.py", '"主语 + 动词 + 时间 + 对手"', '"Subject + verb + time + opponent"')
rep("content8.py", '"可分动词 mee 在句末"', '"Separable verb: mee goes last"')
rep("content8.py", '"气候周持续七天。"', '"The Climate Week lasts seven days."')
rep("content8.py", '"对照第 1 版头条"', '"Compare with the page 1 headline"')
rep("content8.py", '"橙色预警意味着：做好准备。"', '"Code orange means: be prepared."')
rep("content8.py", '"第 2 版原句 · bereid je voor 做好准备"', '"From page 2 · bereid je voor = be prepared"')
rep("content8.py", '"Museumnacht duurt van 19:00 uur tot 02:00 uur."', '"Museumnacht duurt van 19:00 uur tot 02:00 uur."')
rep("content8.py", '"注意时间表达 van...tot..."', '"Watch the time phrase van...tot..."')
rep("content8.py", '"Ik doe mee aan de Klimaatweek."', '"Ik doe mee aan de Klimaatweek."')
rep("content8.py", '"meedoen 是可分动词"', '"meedoen is a separable verb"')
rep("content8.py", '["klimaat=气候 c", "meedoen=参加 b", "waarschuwing=预警 a", "vastzetten=固定好 d"]',
     '["klimaat = climate c", "meedoen = to take part b", "waarschuwing = warning a", "vastzetten = to secure d"]')
rep("content8.py", 'instr="把词和释义配对"', 'instr="Match word to meaning"')
rep("content8.py", '"boom = 树"', '"boom = tree"')
rep("content8.py", '"struik = 灌木"', '"struik = shrub"')
rep("content8.py", '"planten = 种"', '"planten = to plant"')
rep("content8.py", '"zachte = 柔软的（土壤）"', '"zachte = soft (soil)"')
rep("content8.py", '"发放到 16:00 结束"', '"The giveaway runs until 16:00"')
rep("content8.py", 'f.bridge(f"writing题（无唯一答案）；范文（{NWORDS} 词）见下。")',
     'f.bridge(f"Writing task (no single answer); model text ({NWORDS} words) below.")')
rep("content8.py", '"（开放题，范文如下）"', '"(open task, model text below)"')
rep("content8.py", 'f"范文见本版 H 区（{NWORDS} 词）"', 'f"See the model text in section H ({NWORDS} words)"')
rep("content8.py", '"ANTWOORDEN · 参考答案 — 按版面分页排列，找到题号即可"',
     '"ANTWOORDEN · ANSWER KEY — grouped by page: find your number"')
rep("content8.py", '"每题附一句中文简析 · 带 ✓ 的为范文题"',
     '"Every answer has a short note in English · ✓ marks the writing task"')
# svglib code comment only (never rendered): keep the file CJK-free like W43 EN
rep("svglib.py", "for 重阳", "for Double Ninth")

# ---------- post-transform width fixes (measured with svglib text_w) ----------
# Subtitle: full Dutch topic line measured 1958.8 > 1820 inner width, so per the
# W43 NL x EN precedent (subtitle shortened by one theme word) MUSEUMNACHT is
# dropped; the topic stays in the headline, contents and P3 coverage.
rep("content12.py", "WEEKBLAD IN HET NEDERLANDS · VOL.2 · KLIMAATWEEK · MUSEUMNACHT · SPEELRONDE 12",
     "WEEKBLAD IN HET NEDERLANDS · VOL.2 · KLIMAATWEEK · SPEELRONDE 12")
# P6 chart title: 459.4 > 412 box inner edge; shortened (OEFENDATA label stays
# in the Dutch + English captions below the chart).
rep("content56.py", "DE GRAFIEK · CHART (PRACTICE DATA)", "DE GRAFIEK · PRACTICE DATA")

# ---------- apply ----------
def main():
    for item in R:
        f, old, new = item[0], item[1], item[2]
        opt = len(item) > 3
        path = os.path.join(HERE, f)
        txt = open(path, encoding="utf-8").read()
        n = txt.count(old)
        # all optional: duplicates (same old in ex + quiz notes) legitimately hit 0
        # on the second occurrence; the CJK=0 scan + diff review is the gate.
        txt = txt.replace(old, new)
        open(path, "w", encoding="utf-8").write(txt)
        print(f"{f}: {n}x {old[:60]!r}")
    print("TOTAL replacements:", len(R))

if __name__ == "__main__":
    main()
