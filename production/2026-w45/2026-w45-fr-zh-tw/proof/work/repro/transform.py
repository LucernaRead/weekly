# -*- coding: utf-8 -*-
"""W45 FR x ZH-TW fan-out transform (single source of truth).

Applies to a pristine copy of hidden_files/weekly-report-w45-fr-build:
  1. OUT repoint (5 content files, core dir -> this edition dir).
  2. svglib SC face -> TC face (4 sites, W43 FRxZH-TW precedent).
  3. content8 P8 rule: core length-threshold rule -> explicit PRINT_NOTES
     set (the core's own measured 97-item noted set, via tools/p8.py
     extract --total 150) + half-width paren note style (W45 zh-tw column
     convention, cf. de-zh-tw / en-zh-tw builds).
  4. Token-exact Traditional-Chinese rewrite of the explanation layer.
     Every replacement is a whole STRING token (never a substring, never
     an AST byte offset), with a hardcoded expected token count taken
     from the pristine inventory (scratch/cjk-inventory.txt, tokenize
     based). Any count mismatch aborts before writing.
  5. Reader's corner (content7): comment para gains an explicit
     imperative solicitation covering BOTH letters and best page-8
     texts (FRxNL precedent, same slot); the editorial note renders the
     frozen French note's "aucun texte" scope explicitly (no real
     letters AND no VOL.2 p8 submissions, both deferred to VOL.4).
  6. Orphan trims (W43 precedent: shorten the Chinese line itself):
     P3 instruction -3 chars (W43 remedy verbatim), P7 phrase-1 bridge
     -2 chars (重新開始 -> 重開), P4 debate +2 chars (到底) to pull
     the ？ off the line start. All three verified by re-render.

NOT transformed (deliberately): all French target text (byte-frozen);
shared-glyph literals (see KEEP audit in checks); svglib line-120
docstring "for 重阳" (library-internal, never rendered, W43 precedent);
f-string fragments "第 {n} 版 / 共 {total} 版" and "— 第 {pg} 版 —"
(shared glyphs). No dropped-intermediary-term wording anywhere in
this file or in the edition output.
"""
import io
import os
import sys
import tokenize

HERE = os.path.dirname(os.path.abspath(__file__))
ED = "weekly-report-w45-fr-zh-tw"
CORE = "weekly-report-w45-fr-core"

# (old, new, expected_token_count) -- counts from scratch/cjk-inventory.txt
MAP = [
("VOL. 3 · 总第 3 期", "VOL. 3 · 總第 3 期", 1),
("HEBDOMADAIRE EN FRANÇAIS · 每周一期 · 读法国人正在读的法语", "HEBDOMADAIRE EN FRANÇAIS · 每週一期 · 讀法國人正在讀的法語", 1),
("法 语 周 报 · VOL.3 · 决 赛 周 末", "法 語 週 報 · VOL.3 · 決 賽 週 末", 1),
("周一开学 · 全法同步复课", "週一開學 · 全法同步復課", 1),
("大师赛开赛 · 音乐节开幕 · 详见第 2 版", "大師賽開賽 · 音樂節開幕 · 詳見第 2 版", 1),
("法语正文 · 简体中文讲解 — 给简体中文读者的版本", "法語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 1),
("SPORT · CULTURE · GASTRONOMIE · LA UNE · 决赛周末", "SPORT · CULTURE · GASTRONOMIE · LA UNE · 決賽週末", 1),
("se jouer 决出胜负、上演 · une finale 决赛 · une demi-finale 半决赛 · un quart de finale 四分之一决赛 · une nocturne 夜场活动 · un frisson 战栗、刺激感 · la coquille Saint-Jacques 扇贝。", "se jouer 決出勝負、上演 · une finale 決賽 · une demi-finale 半決賽 · un quart de finale 四分之一決賽 · une nocturne 夜場活動 · un frisson 戰慄、刺激感 · la coquille Saint-Jacques 扇貝。", 1),
("LES DATES · 决赛周末日程", "LES DATES · 決賽週末日程", 1),
("À VOUS ! · 即学即练", "À VOUS ! · 即學即練", 4),
("周日 8 日举行决赛", "週日 8 日舉行決賽", 1),
("周六 7 日晚是最后夜场", "週六 7 日晚是最後夜場", 1),
("波尔诺曼底卖扇贝", "波爾諾曼底賣扇貝", 1),
("周一 2 日全法复课", "週一 2 日全法復課", 1),
("半决赛后才知道决赛选手", "半決賽後才知道決賽選手", 1),
("三个决赛：网球、刺激、美味", "三個決賽：網球、刺激、美味", 1),
("本周日程 · 11 月 2 日至 8 日", "本週日程 · 11 月 2 日至 8 日", 1),
("周末决赛结果周六晚、周日揭晓。", "週末決賽結果週六晚、週日揭曉。", 1),
("DANS CE NUMÉRO · 本期目录", "DANS CE NUMÉRO · 本期目錄", 1),
("决出胜负；上演。本周末一切都将见分晓。", "決出勝負；上演。本週末一切都將見分曉。", 1),
("EN BREF · 快讯", "EN BREF · 快訊", 1),
("QUIZ ÉCLAIR · 闪电问答", "QUIZ ÉCLAIR · 閃電問答", 1),
("读头版，选出正确答案 · 答案见第 8 版", "讀頭版，選出正確答案 · 答案見第 8 版", 1),
("单选", "單選", 19),
("决赛在周日 8 日", "決賽在週日 8 日", 2),
("扇贝节在滨海波尔", "扇貝節在濱海波爾", 1),
("周一 2 日早上全区复课", "週一 2 日早上全區復課", 1),
("最后夜场周六 7 日", "最後夜場週六 7 日", 1),
("NIVEAU A2 · La rentrée · 开学复课", "NIVEAU A2 · La rentrée · 開學復課", 1),
("la rentrée 开学、复课 · reprendre 重新开始、复课 · un cartable 书包 · un décalage 错开、时差 · en revanche 相反、反之 · un rituel 习惯、仪式。", "la rentrée 開學、復課 · reprendre 重新開始、復課 · un cartable 書包 · un décalage 錯開、時差 · en revanche 相反、反之 · un rituel 習慣、儀式。", 1),
("译注｜une valise 行李箱 · une ambiance 气氛 · le bilan 总结、盘点。", "譯注｜une valise 行李箱 · une ambiance 氣氛 · le bilan 總結、盤點。", 1),
("说说你的开学：周一早上你在哪里？假期读了哪本书？写两句法语寄给编辑部。", "說說你的開學：週一早上你在哪裡？假期讀了哪本書？寫兩句法語寄給編輯部。", 2),
("ET VOUS ? · 说说你自己", "ET VOUS ? · 說說你自己", 1),
("DIRE LA DATE · 这样说日期", "DIRE LA DATE · 這樣說日期", 1),
("lundi 2 novembre · 注意：1 日说 le premier，其余用基数词", "lundi 2 novembre · 注意：1 日說 le premier，其餘用基數詞", 1),
("EXERCICES · 第 2 版练习", "EXERCICES · 第 2 版練習", 1),
("答案见第 8 版 · 题目可跨级混排，按题号找答案", "答案見第 8 版 · 題目可跨級混排，按題號找答案", 1),
("用法语补全日期（注意星期与数字）。", "用法語補全日期（注意星期與數字）。", 1),
("复课在星期一", "復課在星期一", 1),
("11 月 1 日说 le premier", "11 月 1 日說 le premier", 1),
("最后夜场在星期六", "最後夜場在星期六", 1),
("决赛在星期日", "決賽在星期日", 1),
("用 aller + 动词原形改写（最近将来时）。", "用 aller + 動詞原形改寫（最近將來時）。", 1),
("句型转换", "句型轉換", 7),
("改写", "改寫", 7),
("读第 2 版文章，选出正确答案。", "讀第 2 版文章，選出正確答案。", 1),
("三区同一周一早上复课", "三區同一週一早上復課", 1),
("冬令时从 10 月 25 日开始", "冬令時從 10 月 25 日開始", 1),
("词汇配对", "詞彙配對", 5),
("rentrée=开学 a", "rentrée=開學 a", 1),
("reprendre=重新开始 b", "reprendre=重新開始 b", 1),
("cartable=书包 c", "cartable=書包 c", 1),
("rituel=习惯 d", "rituel=習慣 d", 1),
("把词和释义配对", "把詞和釋義配對", 1),
("NIVEAU A2 → B1 · Halloween, Toussaint · 万圣与诸圣", "NIVEAU A2 → B1 · Halloween, Toussaint · 萬聖與諸聖", 1),
("se déguiser 变装、装扮 · un sort 魔法、恶作剧 · une ambiance 气氛 · le souvenir 回忆、纪念 · confondre 混淆 · discret 低调的、安静的。", "se déguiser 變裝、裝扮 · un sort 魔法、惡作劇 · une ambiance 氣氛 · le souvenir 回憶、紀念 · confondre 混淆 · discret 低調的、安靜的。", 1),
("判断对错（Vrai / Faux）。", "判斷對錯（Vrai / Faux）。", 1),
("万圣节在 10 月 31 日星期六", "萬聖節在 10 月 31 日星期六", 1),
("诸圣节墓园摆满菊花", "諸聖節墓園擺滿菊花", 1),
("菊花绝不能当礼物送人", "菊花絕不能當禮物送人", 1),
("11 月 2 日是 jour des morts，不是诸圣节", "11 月 2 日是 jour des morts，不是諸聖節", 1),
("万圣节穿变装服装", "萬聖節穿變裝服裝", 1),
("南瓜是万圣节的象征", "南瓜是萬聖節的象徵", 1),
("诸圣节是纪念之日", "諸聖節是紀念之日", 1),
("改写句子（用 ne...jamais / ne...plus / ne...pas）。", "改寫（ne...jamais / ne...plus / ne...pas）。", 1),
("jamais + de（无冠词变化）", "jamais + de（無冠詞變化）", 1),
("即学即练 · 公园万圣节小题。", "即學即練 · 公園萬聖節小題。", 1),
("周六 7 日是最后夜场", "週六 7 日是最後夜場", 1),
("敏感儿童有免费驱怪徽章", "敏感兒童有免費驅怪徽章", 1),
("阿斯泰里克斯公园在 Plailly", "阿斯泰里克斯公園在 Plailly", 1),
("恐惧等级用颜色区分", "恐懼等級用顏色區分", 1),
("夜场从 19 点到凌晨 1 点", "夜場從 19 點到凌晨 1 點", 1),
("LES MOTS DES FÊTES · 节日词表", "LES MOTS DES FÊTES · 節日詞表", 1),
("un saint — 圣人", "un saint — 聖人", 1),
("un cimetière — 墓园", "un cimetière — 墓園", 1),
("une tombe — 坟墓", "une tombe — 墳墓", 1),
("se souvenir — 纪念、想起", "se souvenir — 紀念、想起", 1),
("un déguisement — 变装服装", "un déguisement — 變裝服裝", 1),
("un fantôme — 幽灵", "un fantôme — 幽靈", 1),
("un sort — 魔法、诅咒", "un sort — 魔法、詛咒", 1),
("10 月 3 日至 11 月 8 日，12 场夜场；最后夜场 11 月 7 日；白天 10 点至 19 点开放。", "10 月 3 日至 11 月 8 日，12 場夜場；最後夜場 11 月 7 日；白天 10 點至 19 點開放。", 1),
("DATES À RETENIR · 本周日历", "DATES À RETENIR · 本週日曆", 1),
("注意：迪耶普扇贝集市在 11 月 14–15 日，不在本周。", "注意：迪耶普扇貝集市在 11 月 14–15 日，不在本週。", 1),
("SPORT · 体育", "SPORT · 體育", 1),
("un tournoi 锦标赛、赛事 · sur dur 硬地球场 · en salle 室内 · un tableau principal 正赛签表 · le tenant du titre 卫冕冠军 · basculer 逆转、倾斜 · les tribunes 看台。", "un tournoi 錦標賽、賽事 · sur dur 硬地球場 · en salle 室內 · un tableau principal 正賽籤表 · le tenant du titre 衛冕冠軍 · basculer 逆轉、傾斜 · les tribunes 看台。", 1),
("读第 4 版文章，选出正确答案。", "讀第 4 版文章，選出正確答案。", 1),
("大师赛在室内硬地球场举行", "大師賽在室內硬地球場舉行", 1),
("2025 年卫冕冠军是辛纳", "2025 年衛冕冠軍是辛納", 1),
("法甲第十轮大场面：朗斯–马赛", "法甲第十輪大場面：朗斯–馬賽", 1),
("周日 8 日还有轮椅单打决赛（中午）", "週日 8 日還有輪椅單打決賽（中午）", 1),
("把网球词和释义配对。", "把網球詞和釋義配對。", 1),
("tournoi=赛事 a", "tournoi=賽事 a", 2),
("tenant=卫冕者 d", "tenant=衛冕者 d", 1),
("配对", "配對", 4),
("用比较级完成句子（plus / moins）。", "用比較級完成句子（plus / moins）。", 1),
("室内球速更快", "室內球速更快", 1),
("大师赛是仅次于大满贯的级别", "大師賽是僅次於大滿貫的級別", 1),
("室内赛季比室外短", "室內賽季比室外短", 1),
("译注｜un choc 强强对决 · recevoir 迎战、接待 · familier 熟悉的。", "譯注｜un choc 強強對決 · recevoir 迎戰、接待 · familier 熟悉的。", 1),
("« Il marque ! » — 他得分了！ · « C'est gagné ! » — 赢了！", "« Il marque ! » — 他得分了！ · « C'est gagné ! » — 贏了！", 1),
("« Quel point ! » — 好球！（网球） · « Balle de match ! » — 赛点！", "« Quel point ! » — 好球！（網球） · « Balle de match ! » — 賽點！", 1),
("LES MOTS DU TENNIS · 网球词表", "LES MOTS DU TENNIS · 網球詞表", 1),
("le tennis — 网球", "le tennis — 網球", 1),
("un set — 一盘", "un set — 一盤", 1),
("un match — 比赛", "un match — 比賽", 1),
("la finale — 决赛", "la finale — 決賽", 1),
("un adversaire — 对手", "un adversaire — 對手", 1),
("un titre — 冠军头衔", "un titre — 冠軍頭銜", 1),
("MICRO-DRILLS · 即学即练", "MICRO-DRILLS · 即學即練", 2),
("四分之一决赛在周五", "四分之一決賽在週五", 1),
("半决赛在周六", "半決賽在週六", 1),
("单打决赛在周日", "單打決賽在週日", 1),
("正赛签表从周一开始", "正賽籤表從週一開始", 1),
("轮椅赛事周五至周日", "輪椅賽事週五至週日", 1),
("朗斯–马赛是周末焦点战", "朗斯–馬賽是週末焦點戰", 1),
("LE DÉBAT · 讨论", "LE DÉBAT · 討論", 3),
("事先不知道决赛选手，是更刺激还是更扫兴？写两句支持、两句反对。", "事先不知道決賽選手，到底是更刺激還是更掃興？寫兩句支持、兩句反對。", 1),
("NIVEAU B1 · Pitchfork Paris · 音乐节", "NIVEAU B1 · Pitchfork Paris · 音樂節", 1),
("un lieu 场所、场地 · une affiche 海报 · les paroles 歌词 · donner le ton 定调子 · se promener 漫步、穿梭 · pile 正好、恰好。", "un lieu 場所、場地 · une affiche 海報 · les paroles 歌詞 · donner le ton 定調子 · se promener 漫步、穿梭 · pile 正好、恰好。", 1),
("读第 5 版文章，选出正确答案。", "讀第 5 版文章，選出正確答案。", 1),
("音乐节 11 月 2–8 日，整整一周", "音樂節 11 月 2–8 日，整整一週", 1),
("15 届音乐节", "15 屆音樂節", 1),
("Avant-Garde 在巴士底各场地，周四至周六", "Avant-Garde 在巴士底各場地，週四至週六", 1),
("俱乐部之夜在周五、周六", "俱樂部之夜在週五、週六", 1),
("开幕夜：Headache、Iceage、DIIV", "開幕夜：Headache、Iceage、DIIV", 1),
("10 个场地", "10 個場地", 1),
("歌词也是法语学习材料", "歌詞也是法語學習材料", 1),
("海报上写着演出信息", "海報上寫著演出資訊", 1),
("每晚气氛各不相同", "每晚氣氛各不相同", 1),
("音乐节上人们跳舞", "音樂節上人們跳舞", 1),
("发现不认识的乐队", "發現不認識的樂隊", 1),
("把音乐词和释义配对。", "把音樂詞和釋義配對。", 1),
("concert=音乐会 a", "concert=音樂會 a", 1),
("groupe=乐队 c", "groupe=樂隊 c", 1),
("billet=门票 d", "billet=門票 d", 1),
("补全对话（音乐节门口）。", "補全對話（音樂節門口）。", 1),
("今晚演出的乐队", "今晚演出的樂隊", 1),
("买两张票", "買兩張票", 1),
("MOTS DE LA MUSIQUE · 音乐词表", "MOTS DE LA MUSIQUE · 音樂詞表", 1),
("un festival — 音乐节", "un festival — 音樂節", 1),
("un concert — 音乐会", "un concert — 音樂會", 1),
("écouter — 聆听", "écouter — 聆聽", 1),
("une salle — 演出厅", "une salle — 演出廳", 1),
("le public — 观众", "le public — 觀眾", 1),
("PARIS CREATOR WEEK · 创作者周", "PARIS CREATOR WEEK · 創作者週", 1),
("11 月 4–5 日拉维莱特：创作者周，线上创作者与观众线下见面。", "11 月 4–5 日拉維萊特：創作者週，線上創作者與觀眾線下見面。", 1),
("十个场地的音乐节，比单一大场馆更好吗？你听什么音乐学法语？", "十個場地的音樂節，比單一大場館更好嗎？你聽什麼音樂學法語？", 1),
("POLITIQUE & CHIFFRES · 时事", "POLITIQUE & CHIFFRES · 時事", 1),
("NIVEAU B2 · Budget 2027 · 预算周", "NIVEAU B2 · Budget 2027 · 預算週", 1),
("un budget 预算 · une mission （预算）分项 · un député 国民议会议员 · rejeter 否决 · à l'unanimité 一致通过/否决 · un amendement 修正案。", "un budget 預算 · une mission （預算）分項 · un député 國民議會議員 · rejeter 否決 · à l'unanimité 一致通過/否決 · un amendement 修正案。", 1),
("LE CALENDRIER PRÉVU · 计划中的投票日程（结果未出）", "LE CALENDRIER PRÉVU · 計畫中的投票日程（結果未出）", 1),
("本页日程为计划安排，结果尚未产生，下期跟进。", "本頁日程為計畫安排，結果尚未產生，下期跟進。", 1),
("LIRE LE CALENDRIER · 读日程", "LIRE LE CALENDRIER · 讀日程", 1),
("读上图日程，选出正确答案。", "讀上圖日程，選出正確答案。", 1),
("图表读数", "圖表讀數", 7),
("周二 3 日：文化与媒体", "週二 3 日：文化與媒體", 1),
("周三 4 日：农业", "週三 4 日：農業", 1),
("周四 5 日：国土协调与科研", "週四 5 日：國土協調與科研", 1),
("周五 6 日：公共财政与经济", "週五 6 日：公共財政與經濟", 1),
("10 月 23 日社保预算收入被 115–1 否决", "10 月 23 日社保預算收入被 115–1 否決", 1),
("参议院从 11 月 9 日起审议", "參議院從 11 月 9 日起審議", 1),
("LES MOTS · 词汇", "LES MOTS · 詞彙", 1),
("député=议员 a", "député=議員 a", 1),
("rejeter=否决 b", "rejeter=否決 b", 1),
("« Le texte part au Sénat. » — 法案送交参议院。", "« Le texte part au Sénat. » — 法案送交參議院。", 1),
("« Ce calendrier peut encore bouger. » — 日程仍可能变动。", "« Ce calendrier peut encore bouger. » — 日程仍可能變動。", 1),
("« Les résultats ne sont pas connus. » — 结果尚未揭晓。", "« Les résultats ne sont pas connus. » — 結果尚未揭曉。", 1),
("译注｜prévu 预定的、计划的 · réaliser 实现、完成 · distinguer 区分。", "譯注｜prévu 預定的、計畫的 · réaliser 實現、完成 · distinguer 區分。", 1),
("用比较级完成句子。", "用比較級完成句子。", 1),
("预算辩论比一场音乐会长", "預算辯論比一場音樂會長", 1),
("预算比时间表复杂", "預算比時間表複雜", 1),
("文化预算与农业预算同样重要", "文化預算與農業預算同樣重要", 1),
("国民议会审议预算", "國民議會審議預算", 1),
("议员们否决收入部分", "議員們否決收入部分", 1),
("法案送交参议院", "法案送交參議院", 1),
("日程仍可能变动", "日程仍可能變動", 1),
("结果尚未揭晓", "結果尚未揭曉", 1),
("讨论｜结果未出时，该不该先公布日程？区分 prévu（计划）与 décidé（已定）。", "討論｜結果未出時，該不該先公布日程？區分 prévu（計畫）與 décidé（已定）。", 1),
("LANGUE EN MAIN · 精讲", "LANGUE EN MAIN · 精講", 1),
("A2 → B2 · Les phrases de la semaine · 本周金句", "A2 → B2 · Les phrases de la semaine · 本週金句", 1),
("NIVEAU A2 · 基础", "NIVEAU A2 · 基礎", 1),
("NIVEAU B1 · 进阶", "NIVEAU B1 · 進階", 1),
("NIVEAU B2 · 挑战", "NIVEAU B2 · 挑戰", 1),
("工具箱｜本期三句随身句，按级各一；金句全部出自本期文章，回读原文最有效。", "工具箱｜本期三句隨身句，按級各一；金句全部出自本期文章，回讀原文最有效。", 1),
("LES PHRASES DE LA SEMAINE · 本周金句（全部出自本期文章）", "LES PHRASES DE LA SEMAINE · 本週金句（全部出自本期文章）", 1),
("每句一个语法点 + 一道小题 · 答案见第 8 版", "每句一個語法點 + 一道小題 · 答案見第 8 版", 1),
("语法点｜reprendre：复课、重新开始（pause 后）。", "語法點｜reprendre：復課、重開（pause 後）。", 1),
("语法点｜ne...pas encore：尚未、还不。", "語法點｜ne...pas encore：尚未、還不。", 1),
("语法点｜passé composé 代动词：se + être + 过去分词。", "語法點｜passé composé 代動詞：se + être + 過去分詞。", 1),
("语法点｜comparatif：plus + 形容词，ou 对举。", "語法點｜comparatif：plus + 形容詞，ou 對舉。", 1),
("plus + 形容词", "plus + 形容詞", 1),
("语法点｜se promener：代动词，漫步、穿梭。", "語法點｜se promener：代動詞，漫步、穿梭。", 1),
("语法点｜pouvoir + 动词原形：可能、可以。", "語法點｜pouvoir + 動詞原形：可能、可以。", 1),
("语法点｜se jouer：决出胜负、上演（代动词）。", "語法點｜se jouer：決出勝負、上演（代動詞）。", 1),
("语法点｜rencontrer：与观众见面；y 代指地点。", "語法點｜rencontrer：與觀眾見面；y 代指地點。", 1),
("跟练", "跟練", 1),
("CLINIQUE DES ERREURS · 易错诊所", "CLINIQUE DES ERREURS · 易錯診所", 1),
("每句有一处错误：找出来并改正。", "每句有一處錯誤：找出來並改正。", 1),
("改错", "改錯", 9),
("jamais + de：否定句中 des 变 de", "jamais + de：否定句中 des 變 de", 1),
("主谓一致：créateurs 复数 → rencontrent，不是 rencontre", "主謂一致：créateurs 複數 → rencontrent，不是 rencontre", 1),
("虚拟式：il examine，不加 s", "虛擬式：il examine，不加 s", 1),
("事实：决赛在 8 日，不是 7 日", "事實：決賽在 8 日，不是 7 日", 1),
("LE COURRIER DES LECTEURS · 读者园地", "LE COURRIER DES LECTEURS · 讀者園地", 1),
("小墨点评｜编辑部示例：周末叙事用 passé composé 很稳，分号连接两天值得学。下期读者园地将点评真实投稿。", "小墨點評｜編輯部範例：週末敘事用 passé composé 很穩，分號連接兩天值得學。下期讀者園地將點評真實投稿。請把你的來信和最棒的第 8 版作文寄給我們，VOL.4 見！", 1),
("编辑部说明：截至付印，编辑部尚未收到 VOL.2 第 8 版的投稿作文（W44 未出刊），故本期刊登标注明确的编辑部示例；VOL.4 将兑现点评真实投稿的承诺。", "編輯部說明：截至付印，編輯部尚未收到真實來信與 VOL.2 第 8 版投稿作文（W44 未出刊），故本期刊登標註明確的編輯部範例；兩者皆延至 VOL.4 點評。", 1),
("LA SEMAINE PROCHAINE · VOL.4 下周预告", "LA SEMAINE PROCHAINE · VOL.4 下週預告", 1),
("下周：参议院审议社保预算、11 月 11 日停战纪念日、迪耶普扇贝集市；还有你们的来信！", "下週：參議院審議社保預算、11 月 11 日停戰紀念日、迪耶普扇貝集市；還有你們的來信！", 1),
("EXERCICES & RÉPONSES · 练习与答案", "EXERCICES & RÉPONSES · 練習與答案", 1),
("综合评估 ÉVALUATION · 答案在本版下方", "綜合評估 ÉVALUATION · 答案在本版下方", 1),
("去南泰尔看决赛", "去南泰爾看決賽", 1),
("决赛选手周六晚才揭晓", "決賽選手週六晚才揭曉", 1),
("品尝语境（un régal）→ goûté", "品嚐語境（un régal）→ goûté", 1),
("avoir + 过去分词 goûté（不配合）", "avoir + 過去分詞 goûté（不配合）", 1),
("les finales 主语复数 → ont lieu", "les finales 主語複數 → ont lieu", 1),
("elle écrit 她写", "elle écrit 她寫", 1),
("选项：", "選項：", 1),
("B · CHOIX MULTIPLE · 单选", "B · CHOIX MULTIPLE · 單選", 1),
("7 nov. = samedi（最后夜场）", "7 nov. = samedi（最後夜場）", 1),
("si + imparfait（未完成过去时）→ conditionnel présent（条件式现在时）；j' 是 je 在元音前的省音", "si + imparfait（未完成過去時）→ conditionnel présent（條件式現在時）；j' 是 je 在母音前的省音", 1),
("主语 ce programme 三单 → semble", "主語 ce programme 第三人稱單數 → semble", 1),
("将来时 aura lieu（决赛在周日）", "將來時 aura lieu（決賽在週日）", 1),
("三区同日复课", "三區同日復課", 1),
("扇贝节在 11 月 7–8 日", "扇貝節在 11 月 7–8 日", 1),
("C · LECTURE · 阅读理解", "C · LECTURE · 閱讀理解", 1),
("夜场 19 点至凌晨 1 点", "夜場 19 點至凌晨 1 點", 1),
("小徽章给小 Léo 驱怪", "小徽章給小 Léo 驅怪", 1),
("周日先看决赛再吃扇贝", "週日先看決賽再吃扇貝", 1),
("周日晚上早睡因为周一上学", "週日晚上早睡因為週一上學", 1),
("周一是上学日（复课后正常周一）", "週一是上學日（復課後正常週一）", 1),
("阅读理解", "閱讀理解", 1),
("D · PHRASES · 完成句子与转换", "D · PHRASES · 完成句子與轉換", 1),
("si + 半过去时 venais", "si + 半過去時 venais", 1),
("passé composé : a + 过去分词", "passé composé : a + 過去分詞", 1),
("selon moi = 在我看来", "selon moi = 在我看來", 1),
("il est prévu que + 虚拟式", "il est prévu que + 虛擬式", 1),
("E · TRADUCTION · 翻译", "E · TRADUCTION · 翻譯", 1),
("读一份日程，本身就是在了解法国。", "讀一份日程，本身就是在了解法國。", 1),
("lire un programme = 读日程", "lire un programme = 讀日程", 1),
("比较级 plus vite + court", "比較級 plus vite + court", 1),
("Traduisez : 学生们自 10 月 17 日起就在放假。", "Traduisez : 學生們自 10 月 17 日起就在放假。", 1),
("Traduisez : 今晚，我们要准备书包。", "Traduisez : 今晚，我們要準備書包。", 1),
("Traduisez : 人们尚不知道决赛选手是谁。", "Traduisez : 人們尚不知道決賽選手是誰。", 1),
("翻译", "翻譯", 1),
("F · LES MOTS · 词汇配对", "F · LES MOTS · 詞彙配對", 1),
("nocturne=夜场 b", "nocturne=夜場 b", 1),
("budget=预算 c", "budget=預算 c", 1),
("coquille=扇贝 d", "coquille=扇貝 d", 1),
("festival=音乐节 e", "festival=音樂節 e", 1),
("在市场买扇贝", "在市場買扇貝", 1),
("goûter 品尝（原形）", "goûter 品嚐（原形）", 1),
("à la portaise 是一种做法", "à la portaise 是一種做法", 1),
("Bon week-end ! 周末愉快", "Bon week-end ! 週末愉快", 1),
("对话补全", "對話補全", 1),
("G · DIALOGUE · 对话补全", "G · DIALOGUE · 對話補全", 1),
("写作", "寫作", 1),
("开放题 — 要点见写作框，范文在第 8 版写作框内", "開放題 — 要點見寫作框，範本在第 8 版寫作框內", 1),
("按要点给分", "按要點給分", 1),
("H · ÉCRITURE · 写作", "H · ÉCRITURE · 寫作", 1),
("用法语写 80–100 词：我的 11 月 7–8 日周末。写清一场比赛、一个节日、一道菜。", "用法語寫 80–100 詞：我的 11 月 7–8 日週末。寫清一場比賽、一個節日、一道菜。", 1),
("MODÈLE · 范文", "MODÈLE · 範本", 1),
("RÉPONSES · 全部答案与简析（第 1–8 版）", "RÉPONSES · 全部答案與簡析（第 1–8 版）", 1),
("Le Lucerna · 法语周报 VOL.3 · 正文法语 · 讲解简体中文", "Le Lucerna · 法語週報 VOL.3 · 正文法語 · 講解繁體中文", 1),
("译注｜", "譯注｜", 1),
("阅读判断", "閱讀判斷", 5),
]

# Core's own measured P8 noted set (tools/p8.py extract --total 150 on the
# shipped core P8 SVG): 97 items, 53 bare. Explicit set replaces the
# length-threshold rule so Traditional note-length drift cannot change it.
PRINT_NOTES = {1, 3, 4, 7, 8, 10, 11, 13, 14, 17, 19, 21, 27, 28, 31, 32,
33, 34, 42, 44, 53, 55, 56, 57, 58, 59, 60, 63, 67, 68, 69, 70, 71, 72, 74,
77, 78, 79, 80, 81, 82, 83, 84, 87, 90, 92, 93, 94, 95, 96, 100, 105, 106,
107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121,
122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136,
137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150}


CONTENT_FILES = ["content12.py", "content34.py", "content56.py",
                 "content7.py", "content8.py"]


def replace_or_die(path, old, new, expected):
    src = open(path, encoding="utf-8").read()
    n = src.count(old)
    assert n == expected, f"{path}: {old!r} count {n} != {expected}"
    open(path, "w", encoding="utf-8").write(src.replace(old, new))
    return n


def main():
    # --- 1. OUT repoint (exactly 1 per content file; 0 means re-run) ---
    for fn in CONTENT_FILES:
        replace_or_die(os.path.join(HERE, fn), CORE, ED, 1)

    # --- 2. svglib SC -> TC (W43 precedent, 4 sites) ---
    svg = os.path.join(HERE, "svglib.py")
    replace_or_die(svg, "_sc_index", "_tc_index", 2)
    replace_or_die(svg, 'endswith("SC")', 'endswith("TC")', 1)
    replace_or_die(svg, '"Noto Serif CJK SC"', '"Noto Serif CJK TC"', 1)
    replace_or_die(svg, '"Noto Sans CJK SC"', '"Noto Sans CJK TC"', 1)

    # --- 3. content8 P8 rule -> explicit PRINT_NOTES + half-width parens ---
    c8 = os.path.join(HERE, "content8.py")
    old_loop = 'for pg, grp in groupby(REG, key=lambda e: e["page"]):'
    new_loop = ("PRINT_NOTES = " + repr(sorted(PRINT_NOTES)) + "\n"
                + old_loop)
    replace_or_die(c8, old_loop, new_loop, 1)
    old_rule = ('if e["note"] and (pg == 8 or len(e["note"]) <= 10 '
                'or e["type"] in ("改错", "图表读数")):')
    replace_or_die(c8, old_rule, 'if e["note"] and e["n"] in PRINT_NOTES:', 1)
    replace_or_die(c8, 's += f"（{e[\'note\']}）"', 's += f" ({e[\'note\']})"', 1)

    # --- 4. Line-based exact-literal Traditional rewrite ---
    # Each MAP old value is replaced only as a fully quoted literal
    # ("old" or 'old') within its source line, so a short value can never
    # rewrite a substring of a longer literal on the same line. Counts
    # are asserted per key (inventory counts, minus the P8 rule line's
    # one "改错" and one "图表读数" already removed in step 3).
    expected = {old: cnt for old, _, cnt in MAP}
    expected["改错"] = 8
    expected["图表读数"] = 6
    lookup = {old: new for old, new, _ in MAP}
    found = {old: 0 for old, _, _ in MAP}
    files = CONTENT_FILES + ["bslib4.py"]
    for fn in files:
        path = os.path.join(HERE, fn)
        lines = open(path, encoding="utf-8").read().split("\n")
        for i, ln in enumerate(lines):
            for old, new in lookup.items():
                for q in ('"', "'"):
                    pat, rep = q + old + q, q + new + q
                    n = ln.count(pat)
                    if n:
                        # a quoted literal must not straddle code/comments:
                        # every hit on this line is a genuine literal hit
                        # (verified by the per-key total assertion below)
                        ln = ln.replace(pat, rep)
                        found[old] += n
            lines[i] = ln
        open(path, "w", encoding="utf-8").write("\n".join(lines))
    bad = [(k, found[k], expected[k]) for k in expected if found[k] != expected[k]]
    assert not bad, f"MAP count mismatches: {bad[:10]} (total {len(bad)})"
    # post-condition: no MAP key survives as a quoted literal anywhere
    for fn in files:
        src2 = open(os.path.join(HERE, fn), encoding="utf-8").read()
        for old in lookup:
            assert ('"' + old + '"') not in src2 and ("'" + old + "'") not in src2, \
                f"{fn}: unreplaced key {old!r}"
    print(f"transform OK: {len(MAP)} map entries, {sum(found.values())} literal hits replaced")
    print(f"OUT repointed to {ED}; svglib TC; P8 PRINT_NOTES={len(PRINT_NOTES)}")


if __name__ == "__main__":
    main()
