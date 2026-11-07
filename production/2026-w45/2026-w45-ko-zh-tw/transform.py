# -*- coding: utf-8 -*-
"""W45 KO x ZH-TW fan-out transform. Single source of edits.

Copies of the W45 KO core build files are transformed in place:
  * explanation layer (Simplified Chinese) -> Traditional Chinese written
    natively for Taiwan/Hong Kong readers (NOT a codepage conversion of
    the simplified text: every target string below was authored directly
    in Traditional usage; Taiwan/Hong Kong vocabulary decisions are noted
    in the KIT, e.g. 準季後賽 for 준플레이오프, 漢拏山 for 한라산).
  * Korean target text is NEVER touched: every MAP source is an
    explanation-layer literal; frozen Korean strings contain no MAP
    source as a substring (verified by the post-transform freeze audit).
  * furniture follows the W43 ko-zh-tw shipped SVGs (badge/footer/page
    line/P8 head/separators/gloss prefix), VOL.1 -> VOL.2.
  * svglib face change KR -> TC follows the W43 ko-zh-tw precedent.

Usage: run from this directory AFTER a fresh copy of the core build tree.
  python3 transform.py
Refuses to run twice (badge already present -> abort).
Every MAP/STRUCT source must occur >= 1 time before replacement and be
absent afterwards (longest-source-first order).
"""
import os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["content12.py", "content34.py", "content56.py", "content7.py",
         "content8.py", "bslib4.py", "svglib.py", "render.py"]

# ---- explanation-layer map: Simplified source -> Traditional target ----
MAP = [
    # type / instruction names
    ("完形单选", "完形單選"),
    ("单选", "單選"),
    ("词汇配对", "詞彙配對"),
    ("句型转换", "句型轉換"),
    ("翻译", "翻譯"),
    ("改写", "改寫"),
    ("判断", "判斷"),
    ("写作", "寫作"),
    ("译注｜", "譯注｜"),
    ("练习", "練習"),
    # furniture / band titles
    ("体育", "體育"),
    ("深读", "深讀"),
    ("语言", "語言"),
    ("测验与答案", "測驗與答案"),
    ("每周一期", "每週一期"),
    ("头条", "頭條"),
    ("快讯", "快訊"),
    ("闪电问答", "閃電問答"),
    ("数字看本周", "數字看本週"),
    ("即学即练", "即學即練"),
    ("本期目录", "本期目錄"),
    ("本周词语", "本週詞語"),
    ("读者园地", "讀者園地"),
    ("本周金句（逐字摘自本期文章）", "本週金句（逐字摘自本期文章）"),
    ("本周句式", "本週句式"),
    ("易错诊所", "易錯診所"),
    ("下期预告", "下期預告"),
    ("过冬清单", "過冬清單"),
    ("红叶观赏准备", "紅葉觀賞準備"),
    ("红叶最后一周", "紅葉最後一週"),
    ("本周青年数字", "本週青年數字"),
    ("高考倒计时与万圣节", "高考倒數計時與萬聖節"),
    ("高考倒计时读法", "高考倒數計時讀法"),
    ("本周与考试日一表看清", "本週與考試日一表看清"),
    ("三个级别，三个主题", "三個級別，三個主題"),
    ("数日子的说法", "數日子的說法"),
    ("用高考倒计时数日子的四个说法", "用高考倒數計時數日子的四個說法"),
    ("说说你自己", "說說你自己"),
    ("韩史考试报名", "韓史考試報名"),
    ("泡菜季与过冬准备、韩史考试报名", "泡菜季與過冬準備、韓史考試報名"),
    ("立冬在 11 月 7 日周六 · 泡菜季开始", "立冬在 11 月 7 日週六 · 泡菜季開始"),
    # P8 head / apparatus (W43 ko-zh-tw forms)
    ("답 · 参考答案 — 按版面分页排列，找到题号即可", "답 · 全部答案與簡析（第 1–8 版）"),
    ("每题附一句中文简析 · 带 ✓ 的为范文题", "每題附一句中文簡析 · 帶 ✓ 的為範本題"),
    ("(开放题，范文如下)", "（開放題，範本如下）"),
    ("范文见本版 H 区（{NCHARS} 字）", "範本見本版 H 區（{NCHARS} 字）"),
    ("Lucerna · 韩语周报 VOL.2 · LUCERNA KOREAN WEEKLY",
     "Lucerna · 韓語週報 VOL.2 · 正文韓語 · 講解繁體中文"),
    # gloss lines (full literals)
    ("입동 立冬、冬季开始 · 절정 最盛期、高峰 · 김장 腌过冬泡菜 · 상륙하다 登陆 · 온대저기압 温带气旋。",
     "입동 立冬、冬季開始 · 절정 最盛期、高峰 · 김장 醃過冬泡菜 · 상륙하다 登陸 · 온대저기압 溫帶氣旋。"),
    ("입동 ＝ 立冬、冬季开始的节气。", "입동 ＝ 立冬、冬季開始的節氣。"),
    ("절이다 用盐腌 · 버무리다 拌 · 난방 供暖 · 식탁 餐桌。",
     "절이다 用鹽醃 · 버무리다 拌 · 난방 供暖 · 식탁 餐桌。"),
    ("산불 山火 · 벌금 罚款 · 불씨 火星。", "산불 山火 · 벌금 罰款 · 불씨 火星。"),
    ("아삭하다 脆脆的 · 김 蒸汽 · 깊어지다 变深。", "아삭하다 脆脆的 · 김 蒸汽 · 깊어지다 變深。"),
    ("물려주다 传给 · 낡다 旧 · 두렵다 害怕。", "물려주다 傳給 · 낡다 舊 · 두렵다 害怕。"),
    ("묵직하다 沉甸甸的 · 앞치마 围裙 · 목록 清单。",
     "묵직하다 沉甸甸的 · 앞치마 圍裙 · 목록 清單。"),
    ("기관 机构 · 기준 标准 · 관측 观测 · 구간별 按路段。",
     "기관 機構 · 기준 標準 · 관측 觀測 · 구간별 按路段。"),
    ("현장 现场 · 유명하다 有名 · 맛보다 品尝。", "현장 現場 · 유명하다 有名 · 맛보다 品嚐。"),
    ("이용하다 利用 · 막히다 堵塞 · 예의 礼仪。", "이용하다 利用 · 막히다 堵塞 · 예의 禮儀。"),
    ("겹쳐 입다 叠穿 · 미끄러지다 打滑 · 돌 石头。",
     "겹쳐 입다 疊穿 · 미끄러지다 打滑 · 돌 石頭。"),
    ("연승 连胜 · 만루홈런 满垒本垒打 · 미뤄지다 推迟 · 마감하다 截稿。",
     "연승 連勝 · 만루홈런 滿壘本壘打 · 미뤄지다 推遲 · 마감하다 截稿。"),
    ("흔들다 挥动 · 하나가 되다 融为一体。", "흔들다 揮動 · 하나가 되다 融為一體。"),
    ("예상 预测。", "예상 預測。"),
    ("정리 整理、复习 · 끈끈하다 粘粘的 · 합격 合格。",
     "정리 整理、複習 · 끈끈하다 粘粘的 · 합격 合格。"),
    ("중점 重点 · 배치하다 部署 · 통제하다 管制。", "중점 重點 · 배치하다 部署 · 통제하다 管制。"),
    ("챙기다 准备好 · 졸리다 犯困 · 평소 平时。", "챙기다 準備好 · 졸리다 犯睏 · 평소 平時。"),
    ("비다 祈愿 · 피하다 避开 · 미끄럽다 滑。", "비다 祈願 · 피하다 避開 · 미끄럽다 滑。"),
    ("짙어지다 变浓 · 규모 规模 · 섞다 混淆。", "짙어지다 變濃 · 규모 規模 · 섞다 混淆。"),
    ("예정 预定 · 확정 确定 · 믿다 相信。", "예정 預定 · 확정 確定 · 믿다 相信。"),
    ("본격적 正式、全面 · 나다 度过。", "본격적 正式、全面 · 나다 度過。"),
    ("짐작하다 推测 · 나누다 区分。", "짐작하다 推測 · 나누다 區分。"),
    # notes / keys / prompts
    ("立冬在11月7日周六", "立冬在11月7日週六"),
    ("泡菜季＝腌过冬泡菜", "泡菜季＝醃過冬泡菜"),
    ("高考在11月19日周四", "高考在11月19日週四"),
    ("台风没有在韩国本土登陆", "颱風沒有在韓國本土登陸"),
    ("首尔报名窗口11月6日10–12点", "首爾報名窗口11月6日10–12點"),
    ("立冬＝冬季开始的节气", "立冬＝冬季開始的節氣"),
    ("内藏山两个预报：11月4日与11月11日", "內藏山兩個預報：11月4日與11月11日"),
    ("10月25日首场比赛因雨推迟", "10月25日首場比賽因雨推遲"),
    ("答案见第 8 版 · 题目可跨级混排，按题号找答案", "答案見第 8 版 · 題目可跨級混排，按題號找答案"),
    ("读头版，选出正确答案 · 答案见第 8 版", "讀頭版，選出正確答案 · 答案見第 8 版"),
    ("这五个日期，是本期报纸的骨架。", "這五個日期，是本期報紙的骨架。"),
    ("你呢？为过冬做的第一件事是什么？写两句韩语寄来。",
     "你呢？為過冬做的第一件事是什麼？寫兩句韓語寄來。"),
    ("你呢？想去看红叶的山是哪座？写两句韩语寄来。",
     "你呢？想去看紅葉的山是哪座？寫兩句韓語寄來。"),
    ("你呢？想对考生说的一句加油是什么？写两句韩语寄来。",
     "你呢？想對考生說的一句加油是什麼？寫兩句韓語寄來。"),
    ("韩史考试在11月28日周六", "韓史考試在11月28日週六"),
    ("过冬准备＝为冬天做准备", "過冬準備＝為冬天做準備"),
    ("把词和说明配对", "把詞和說明配對"),
    ("把词和释义配对", "把詞和釋義配對"),
    ("把山和说明配对", "把山和說明配對"),
    ("考场全国1,312处", "考場全國1,312處"),
    ("内藏山林业厅预报峰值11月4日", "內藏山林業廳預報峰值11月4日"),
    ("雪岳山实际观测峰值10月16日", "雪嶽山實際觀測峰值10月16日"),
    ("第3场在蚕室举行", "第3場在蠶室舉行"),
    ("季后赛首场因雨推迟", "季後賽首場因雨推遲"),
    ("听力时段飞机不起降", "聽力時段飛機不起降"),
    ("首尔万圣节安全人员3,271人", "首爾萬聖節安全人員3,271人"),
    ("主语+宾语+动词的语序", "主語+賓語+動詞的語序"),
    ("语序：主语+副词+动词", "語序：主語+副詞+動詞"),
    ("语序：主语+时间+场所+动词", "語序：主語+時間+場所+動詞"),
    ("措施只适用于11月19日", "措施只適用於11月19日"),
    ("特别措施只适用于11月19日", "特別措施只適用於11月19日"),
    ("特别措施只适用于考试日", "特別措施只適用於考試日"),
    ("山火注意期从11月1日开始", "山火注意期從11月1日開始"),
    ("带火进山最高罚30万韩元", "帶火進山最高罰30萬韓元"),
    ("首尔报名10点至12点", "首爾報名10點至12點"),
    ("白菜用盐腌", "白菜用鹽醃"),
    ("加入萝卜和调料拌匀", "加入蘿蔔和調料拌勻"),
    ("进山要小心火", "進山要小心火"),
    ("11月3日起开始报名", "11月3日起開始報名"),
    ("最高罚款30万韩元", "最高罰款30萬韓元"),
    ("深化考试费27,000韩元", "深化考試費27,000韓元"),
    ("11月6日13点起全国报名剩余名额", "11月6日13點起全國報名剩餘名額"),
    ("김장=腌过冬泡菜 a", "김장=醃過冬泡菜 a"),
    ("월동 준비=准备过冬 c", "월동 준비=準備過冬 c"),
    ("산불조심=进山小心火 d", "산불조심=進山小心火 d"),
    ("한능검=韩国史考试简称 b", "한능검=韓國史考試簡稱 b"),
    ("内藏山公园公团预报峰值11月11日", "內藏山公園公團預報峰值11月11日"),
    ("青松现场庆典11月4日至8日", "青松現場慶典11月4日至8日"),
    ("没有官方的路段数值", "沒有官方的路段數值"),
    ("红叶最美的时候叫절정", "紅葉最美的時候叫절정"),
    ("日期不同因为标准不同", "日期不同因為標準不同"),
    ("日期不同因标准不同（3版）", "日期不同因標準不同（3版）"),
    ("日期不同因标准不同", "日期不同因標準不同"),
    ("实际观测比预报早", "實際觀測比預報早"),
    ("现场庆典11月4日起", "現場慶典11月4日起"),
    ("青松以苹果闻名", "青松以蘋果聞名"),
    ("内藏山林业厅预报4日", "內藏山林業廳預報4日"),
    ("内藏山公团预报11日", "內藏山公團預報11日"),
    ("月出山林业厅预报9日", "月出山林業廳預報9日"),
    ("雪岳山实际观测16日", "雪嶽山實際觀測16日"),
    ("내장산=两个预报之间 b", "내장산=兩個預報之間 b"),
    ("북한산=11月4日之后、低路更晚 d", "북한산=11月4日之後、低路更晚 d"),
    ("설악산=实际观测10月16日 c", "설악산=實際觀測10月16日 c"),
    ("半决赛胜队是KIA", "準季後賽勝隊是KIA"),
    ("第3场比分13比1", "第3場比分13比1"),
    ("公布的韩国大赛开始日11月2日", "公佈的韓國大賽開始日11月2日"),
    ("三连胜晋级", "三連勝晉級"),
    ("首场比赛因雨推迟", "首場比賽因雨推遲"),
    ("10月26日变为温带气旋", "10月26日變為溫帶氣旋"),
    ("kt在韩国大赛等候", "kt在韓國大賽等候"),
    ("이기다的过去式이겼어요", "이기다的過去式이겼어요"),
    ("열리다的过去式열렸어요", "열리다的過去式열렸어요"),
    ("미뤄지다的过去式미뤄졌어요", "미뤄지다的過去式미뤄졌어요"),
    ("바뀌다的过去式바뀌었어요", "바뀌다的過去式바뀌었어요"),
    ("준플레이오프=KIA三连胜 b", "준플레이오프=KIA三連勝 b"),
    ("플레이오프=KIA对三星 d", "플레이오프=KIA對三星 d"),
    ("온대저기압=台风10月26日变化 c", "온대저기압=颱風10月26日變化 c"),
    ("全国为考生加油", "全國為考生加油"),
    ("倒计时仍在继续", "倒數計時仍在繼續"),
    ("怀着祈愿合格的心意赠送糯米糕、饴糖", "懷著祈願合格的心意贈送糯米糕、飴糖"),
    ("首尔安全人员3,271人", "首爾安全人員3,271人"),
    ("考试日机关10点上班", "考試日機關10點上班"),
    ("首尔管理14个地点", "首爾管理14個地點"),
    ("本周倒计时D-17至D-12", "本週倒數計時D-17至D-12"),
    ("考试日就是D-day", "考試日就是D-day"),
    ("考试日有特别措施", "考試日有特別措施"),
    ("本周没有特别措施", "本週沒有特別措施"),
    ("本周氛围是倒计时", "本週氛圍是倒數計時"),
    ("氛围在现在、本周", "氛圍在現在、本週"),
    ("听力时段13:10～13:35", "聽力時段13:10～13:35"),
    ("倒计时氛围在本周", "倒數計時氛圍在本週"),
    ("从D-17到D-12的一周", "從D-17到D-12的一週"),
    ("大数字显示全国规模", "大數字顯示全國規模"),
    ("听力时段飞机受管制", "聽力時段飛機受管制"),
    ("本周是倒计时氛围", "本週是倒數計時氛圍"),
    ("节气＝一年24个时节", "節氣＝一年24個時節"),
    ("D-day就是当天", "D-day就是當天"),
    ("林业厅标准是叶子50%", "林業廳標準是葉子50%"),
    ("实际观测10月16日", "實際觀測10月16日"),
    ("预报要标准日期一起看", "預報要標準日期一起看"),
    ("「담그다」的过去式是「담갔어요」。", "「담그다」的過去式是「담갔어요」。"),
    ("数字与前面要留空格。", "數字與前面要留空格。"),
    ("助词只用一个。", "助詞只用一個。"),
    ("句式拆解：「从〜到〜」。提问：「〜부터 〜까지예요?」",
     "句式拆解：「從〜到〜」。提問：「〜부터 〜까지예요?」"),
    ("编辑部示例信，非真实来信。", "編輯部範例信，非真實來信。"),
    ("郑重说明：截至截稿时，未收到真实读者来信与第 8 版优秀作文，因此仍刊示例，上期承诺顺延至 VOL.3。",
     "鄭重說明：截至截稿時，未收到真實讀者來信與第 8 版優秀作文，因此仍刊範例，上期承諾順延至 VOL.3。請把你的來信和第 8 版作文寄給我們！"),
    ("只能说是接近峰值的周末。", "只能說是接近峰值的週末。"),
    ("泡菜季就是腌过冬泡菜。", "泡菜季就是醃過冬泡菜。"),
    ("离高考还剩 17 天，今天是 D-17。", "離高考還剩 17 天，今天是 D-17。"),
    ("低处的路红得更晚。", "低處的路紅得更晚。"),
    ("KIA 虎三连胜战胜 LG 双子。", "KIA 虎三連勝戰勝 LG 雙子。"),
    ("全国都在为考生加油。", "全國都在為考生加油。"),
    ("KIA三连胜晋级", "KIA三連勝晉級"),
    ("汉拿山三角峰降雨415.5毫米", "漢拏山三角峰降雨415.5毫米"),
    ("内藏山公团预报峰值11月11日", "內藏山公園公團預報峰值11月11日"),
    ("月出山林业厅预报峰值11月9日", "月出山林業廳預報峰值11月9日"),
    ("首尔报名窗口10点至12点", "首爾報名窗口10點至12點"),
    ("智敏周六去内藏山", "智敏週六去內藏山"),
    ("周日帮忙腌泡菜", "週日幫忙醃泡菜"),
    ("下周准备韩史考试", "下週準備韓史考試"),
    ("智敏喜欢韩国史", "智敏喜歡韓國史"),
    ("动作场所用「에서」", "動作場所用「에서」"),
    ("对照第 1 版", "對照第 1 版"),
    ("离高考还剩 12 天。", "離高考還剩 12 天。"),
    ("对照第 5 版", "對照第 5 版"),
    ("对照第 6 版", "對照第 6 版"),
    ("特别措施只适用于11月19日。→ ___", "特別措施只適用於11月19日。→ ___"),
    ("对照第 3 版", "對照第 3 版"),
    ("我周六去内藏山看红叶。→ ___", "我週六去內藏山看紅葉。→ ___"),
    ("입동=冬季开始的节气 a", "입동=冬季開始的節氣 a"),
    ("절정=最佳时期 b", "절정=最佳時期 b"),
    ("김장=腌过冬泡菜 c", "김장=醃過冬泡菜 c"),
    ("온대저기압=台风10月26日变化 d", "온대저기압=颱風10月26日變化 d"),
    ("周六去内藏山", "週六去內藏山"),
    ("首尔报名10点开始", "首爾報名10點開始"),
    ("11 月 2 日，还剩 17 天", "11 月 2 日，還剩 17 天"),
    ("11 月 7 日，还剩 12 天", "11 月 7 日，還剩 12 天"),
    # band sub-lines (full literals, Korean + Chinese)
    ("레벨 A2 · 김장과 겨울 준비, 한능검 · 泡菜季与过冬准备、韩史考试报名",
     "레벨 A2 · 김장과 겨울 준비, 한능검 · 泡菜季與過冬準備、韓史考試報名"),
    ("레벨 A2→B1 · 단풍 마지막 주말 · 红叶最后一周",
     "레벨 A2→B1 · 단풍 마지막 주말 · 紅葉最後一週"),
    ("레벨 B1 · 수능 카운트다운과 할로윈 · 高考倒计时与万圣节",
     "레벨 B1 · 수능 카운트다운과 할로윈 · 高考倒數計時與萬聖節"),
    ("레벨 B2 · 수능 카운트다운을 읽는 법 · 高考倒计时读法",
     "레벨 B2 · 수능 카운트다운을 읽는 법 · 高考倒數計時讀法"),
    ("언어 포커스 · 세 가지 레벨, 세 가지 주제 · 三个级别，三个主题",
     "언어 포커스 · 세 가지 레벨, 세 가지 주제 · 三個級別，三個主題"),
    ("수능까지 남은 날로 날짜를 세는 네 가지 말 · 用高考倒计时数日子的四个说法",
     "수능까지 남은 날로 날짜를 세는 네 가지 말 · 用高考倒數計時數日子的四個說法"),
    ("날짜 세는 말 · 数日子的说法", "날짜 세는 말 · 數日子的說法"),
    ("겨울 준비 목록 · 过冬清单", "겨울 준비 목록 · 過冬清單"),
    ("단풍 구경 준비물 · 红叶观赏准备", "단풍 구경 준비물 · 紅葉觀賞準備"),
    ("한국시리즈까지의 길 · 通往韩国大赛之路", "한국시리즈까지의 길 · 通往韓國大賽之路"),
    ("이번 주 청년 숫자 · 本周青年数字", "이번 주 청년 숫자 · 本週青年數字"),
    ("이번 주와 시험 날, 한눈에 보기 · 本周与考试日一表看清",
     "이번 주와 시험 날, 한눈에 보기 · 本週與考試日一表看清"),
    ("실수 병원 · 易错诊所", "실수 병원 · 易錯診所"),
    ("이번 주의 틀 · 本周句式", "이번 주의 틀 · 本週句式"),
    ("독자의 편지 · 读者园地", "독자의 편지 · 讀者園地"),
    ("이번 주의 문장 · 本周金句（逐字摘自本期文章）",
     "이번 주의 문장 · 本週金句（逐字摘自本期文章）"),
    ("다음 주 · 下期预告 (VOL.3)", "다음 주 · 下期預告 (VOL.3)"),
    ("시험과 답 · 测验与答案", "시험과 답 · 測驗與答案"),
    ("말 공부 · 语言", "말 공부 · 語言"),
    ("깊이 읽기 · 深读", "깊이 읽기 · 深讀"),
    ("스포츠 · 体育", "스포츠 · 體育"),
    ("짧은 소식 · 快讯", "짧은 소식 · 快訊"),
    ("퀴즈 · 闪电问答", "퀴즈 · 閃電問答"),
    ("지금 바로 연습 · 即学即练", "지금 바로 연습 · 即學即練"),
    ("숫자로 보는 이번 주 · 数字看本周", "숫자로 보는 이번 주 · 數字看本週"),
    ("이번 호의 내용 · 本期目录", "이번 호의 내용 · 本期目錄"),
    ("이번 주의 말 · 本周词语", "이번 주의 말 · 本週詞語"),
    ("톱 뉴스 · 头条", "톱 뉴스 · 頭條"),
    ("한능검 접수 · 韩史考试报名", "한능검 접수 · 韓史考試報名"),
    ("당신은? · 说说你自己", "당신은? · 說說你自己"),
    ("연습 · 第 2 版练习", "연습 · 第 2 版練習"),
    ("연습 · 第 3 版练习", "연습 · 第 3 版練習"),
    ("연습 · 第 4 版练习", "연습 · 第 4 版練習"),
    ("연습 · 第 5 版练习", "연습 · 第 5 版練習"),
    ("연습 · 第 6 版练习", "연습 · 第 6 版練習"),
    # svglib docstring example (W43 precedent)
    ("Mountains, sun, two stick climbers, chrysanthemums — for 重阳.",
     "Mountains, sun, two stick climbers, chrysanthemums — for 重陽."),
]

# ---- structural / code edits (exact strings, with expected counts) ----
STRUCT = [
    # output paths -> this edition
    ("weekly-report-w45-ko-core", "weekly-report-w45-ko-zh-tw"),
    ("Lucerna-VOL2.pdf", "Lucerna-VOL2-ZHTW.pdf"),
    ("Lucerna-VOL2-web.pdf", "Lucerna-VOL2-ZHTW-web.pdf"),
    # svglib KR -> TC face (W43 precedent)
    ("def _sc_index(path):", "def _tc_index(path):"),
    ('if f.getname()[0].endswith("KR"):', 'if f.getname()[0].endswith("TC"):'),
    ("_IDX = {p: _sc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}",
     "_IDX = {p: _tc_index(p) for p in (_SERIF, _SERIF_B, _SANS, _SANS_B)}"),
    ('"Noto Serif CJK KR"', '"Noto Serif CJK TC"'),
    ('"Noto Sans CJK KR"', '"Noto Sans CJK TC"'),
    # bslib4 footer + page line (W43 ko-zh-tw forms, VOL.2)
    ('f"제 {n} 면 / 총 {total} 면"', 'f"第 {n} 版 / 共 {total} 版"'),
    # P8 separators (W43 ko-zh-tw form)
    ('f"— 제{pg}면 —"', 'f"— 第 {pg} 版 —"'),
    # P1 masthead furniture (W43 geometry: subtitle 372->366, badge y=394,
    # rules +20, band +9)
    ('p.text(975, 372, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")',
     'p.text(975, 366, "한국어를 배우는 사람을 위한 주간 신문 — 진짜 한국을, 한국어로", 19, "sans", False, GREY, anchor="middle")\n'
     'p.text(975, 394, "韓語正文 · 繁體中文講解 — 給繁體中文讀者的版本", 20, "sans", True, BRICK, anchor="middle")'),
    ("p.hline(MX, RIGHT, 392, INK, 3); p.hline(MX, RIGHT, 401, INK, 1.2)",
     "p.hline(MX, RIGHT, 412, INK, 3); p.hline(MX, RIGHT, 421, INK, 1.2)"),
    ("p.rect(MX, 424, RIGHT - MX, 118, fill=DARK)",
     "p.rect(MX, 433, RIGHT - MX, 118, fill=DARK)"),
    ('p.text(MX + 30, 478, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")',
     'p.text(MX + 30, 487, "11월 7일은 입동이에요 — 겨울의 시작, 단풍의 끝", 36, "sans", True, "#f3edda")'),
    ('p.text(MX + 30, 522, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")',
     'p.text(MX + 30, 531, "김장철이 열리고, 수능까지 12일이 남아요. 이번 주의 달력은 오른쪽을 보세요.", 23, "serif", False, "#e8dfc8")'),
    ('p.text(RIGHT - 30, 478, "立冬", 24, "sans", True, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 487, "立冬", 24, "sans", True, "#b3a06a", anchor="end")'),
    ('p.text(RIGHT - 30, 522, "立冬在 11 月 7 日週六 · 泡菜季開始", 21, "sans", False, "#b3a06a", anchor="end")',
     'p.text(RIGHT - 30, 531, "立冬在 11 月 7 日週六 · 泡菜季開始", 21, "sans", False, "#b3a06a", anchor="end")'),
    # P7 readers-box slack: core formula undercounts ~26-29px (core P7 last
    # line spills below its box); +40 slack follows ko-fr (+40) precedent.
    ('len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 26',
     'len(wrap(lcn2, "sans", False, 20, CW - 44)) * 29 + 66'),
    # P7 phrases pitch 132 -> 102 (ko-fr precedent): the longer Traditional
    # readers box pushes fy down; pitch 102 keeps the teaser end < 2540
    # while rows still carry ~26px inter-row air (row content ~76px).
    ("cyq = fy + 66 + (i % 4) * 132", "cyq = fy + 66 + (i % 4) * 102"),
    ("py = fy + 66 + 4 * 132 + 18", "py = fy + 66 + 4 * 102 + 18"),
]


def main():
    texts = {}
    for f in FILES:
        texts[f] = open(os.path.join(HERE, f), encoding="utf-8").read()
    if "韓語正文 · 繁體中文講解" in texts["content12.py"]:
        print("ABORT: transform already applied (badge present)")
        sys.exit(2)
    combined = "\n".join(texts.values())
    # MAP: pre-counts on ORIGINAL text (a short source may live only inside
    # a longer source, which longest-first replacement consumes first).
    for src, dst in MAP:
        n = combined.count(src)
        if n < 1:
            print(f"ABORT: MAP source missing in original (0x): {src!r}")
            sys.exit(1)
        print(f"MAP {n:3d}x {src!r} -> {dst!r}")
    for src, dst in sorted(MAP, key=lambda kv: -len(kv[0])):
        combined = combined.replace(src, dst)
    for src, dst in MAP:
        assert src not in combined, f"MAP residue {src!r}"
    # STRUCT: pre-counts on POST-MAP text (one entry matches MAP output).
    for src, dst in STRUCT:
        n = combined.count(src)
        if n < 1:
            print(f"ABORT: STRUCT source missing post-MAP (0x): {src!r}")
            sys.exit(1)
        print(f"STRUCT {n:3d}x {src[:60]!r} ...")
    for src, dst in STRUCT:
        combined = combined.replace(src, dst)
    for src, dst in STRUCT:
        assert src not in combined, f"STRUCT residue {src!r}"
    # split back: files were joined with "\n" - recover by re-splitting is
    # unsafe; instead re-apply per file. (Combined pass above was for
    # counting/assertion only; do the real per-file pass now.)
    for f in FILES:
        t = open(os.path.join(HERE, f), encoding="utf-8").read()
        for src, dst in sorted(MAP, key=lambda kv: -len(kv[0])):
            t = t.replace(src, dst)
        for src, dst in STRUCT:
            t = t.replace(src, dst)
        open(os.path.join(HERE, f), "w", encoding="utf-8").write(t)
    # post-assertions on written files
    after = ""
    for f in FILES:
        after += open(os.path.join(HERE, f), encoding="utf-8").read()
    for src, dst in MAP:
        assert src not in after, f"residue MAP {src!r}"
    for src, dst in STRUCT:
        if src != dst:
            assert src not in after, f"residue STRUCT {src!r}"
    assert "韓語正文 · 繁體中文講解" in after
    print("TRANSFORM OK: all assertions passed")


if __name__ == "__main__":
    main()
