# PROOF-NOTE — 2026-W47 · nl → ko（荷兰语目标语 × 韩语读者）· proof1 独立复校

- 版目录：`production/2026-w47/fanout-nl/2026-w47-nl-ko/`
- 复校员：独立复校（proof1）· 2026-11-11
- 依据：仓库根 `SOP.md`（proofread-until-zero；几何遮挡扫描必过；p8 compare 必跑；讲解/导读用读者母语；对外内容禁内部标签/周次/语言代码）

## 结论：(b) 有缺陷，不能定稿

共 **5 项缺陷**（重大 2 项：D4、D6；一般 1 项：D3；轻微 2 项：D5、D7）。
150 题答案键手验 150/150 全部通过；全部 8 页已逐页目视；机械门除下列缺陷所指处外全部通过。
修复后须按 SOP §8 循环规则**整期重渲染、从头再做一轮全量校对**，直到一整轮零问题。

> **校对中途文件被并发重写（重要）**：pinned 的 text.md（SHA `bbca93462d…`，47,383 B）在校对进行中、**2026-11-11 11:53:08 UTC 被重写**（新 SHA `702e12429b09648655760352f966574f4483c5b63413d2d22a9ebd861f26683a`，47,525 B）。新版把答案标记改为 `— 정답： `（142 处）+ `(정답 x`（8 处），「答案」残留 0 处，全文件 Han 字符 0 个。已验证：修复代理留下的 `scratch-fix-core-nl1/textmd-before/2026-w47-nl-ko.text.md` 的 SHA 就是 pinned 版 `bbca93462d…`；新旧两版做标记归一化（정답→答案、去掉冒号后空格）后**完全相同**。因此本轮通读旧版所得的全部内容结论可 1:1 平移到新版。**D4 在 pinned 版成立、在当前文件已解决**（见 D4）。仅 text.md 被改；SVG（2026-11-11 05:08–05:09）、两 PDF（05:10/05:12）、ABSTRACT.txt、WEEKLY-KIT.md、content*.py 均未动——全部 SVG/PDF 门禁与测量仍然有效。若 SVG/PDF 随后重建，需 proof2 重校新版。

## 缺陷清单

### D3（一般，预期存在）— P2 D 节选项 c「c. eten voor het paard van Sinterklaas」超出右版心约 8.5–13.1 px
- **页码/定位**：P2 练习 D「WOORDEN」选项列，基线 y=2233，23 pt Newsreader，起笔 x=1473.5；右版心 1862.0 px（=1396.5 pt）。
- **归属**：核心级旧文本（本版建于核心修复之前）。实测 nuance：现行核心 `content12.py:276` 已是短式 `"eten voor Sinterklaas' paard"`；本版 `content12.py:276` 仍为长式 `"eten voor het paard van Sinterklaas"`；核心修复代理的 `scratch-fix-core-nl1/measure_d3.py` 把短式列为候选修法。即核心侧已改短，本版用的是修复前旧文本；重 fan-out 即解决。
- **实测证据（三法一致）**：PIL 真墨水 ink right 1870.5（+8.5 px）；印 PDF span 1406.3 pt = 1875.1 px（+13.1 px）；200 dpi 像素扫描最右墨点 1874.0 px（+12.0 px）。目视：该行明显比同列 a/b/d 行探出、直抵页边（裁图 `zoom-p2-optc.png`）。
- **修复建议**：随重 fan-out 继承核心短式（或换行/缩写），使墨水右缘 ≤1862。

### D4（重大，针对 pinned 版；当前文件已修复）— text.md 全文 150 处答案标记未本地化，中文「答案：」残留
- **页码/定位**：pinned 版 `2026-w47-nl-ko.text.md`（SHA `bbca93462d…`）全文：142 处「— 答案：」+ 8 处配对题内「(答案 x · …)」型标记（#25–28、#141–144），共 150 处；除「答/案」外该文件无其他中文字符。印 PDF / 网 PDF 无此问题（pdftotext 0 处）。
- **为什么是缺陷**：text.md 是交付件（网站正文体 + SEO），韩语读者在每道题后都看到中文标记，违反「讲解层用读者母语」与对外内容语言一致要求。E 节 type 标签本身已本地化（번역等，见 GATE-LOG §9），但答案标记属于同类未本地化残留。
- **当前状态**：校对中途 11:53:08 UTC 该文件被并发重写，新版标记已本地化为 `— 정답： `（142 处，冒号后带一空格）+ `(정답 x`（8 处），「答案」残留 0 处，Han 字符 0 个；新旧两版标记归一化后完全相同。**D4 在当前文件已解决；但本轮结论针对 pinned 版，仍记为 (b) 缺陷。**
- **修复建议**：已完成的部分无需再做；重 fan-out 时确认导出模板按读者语本地化标记（韩语版：「— 정답：」；配对题「(정답 d · …)」）；修后 grep 验证 text.md 中 Han 字符为 0（U+3000 分隔符除外）。

### D5（轻微）— 网 PDF 丢失 P1 本周词斜体（nl-de D5 同类）
- **页码/定位**：P1「HET WOORD VAN DE WEEK」«de groepswinst»。
- **归属**：机制（tools/webpdf.py 字体裁切未带斜体面）。
- **实测证据**：印 PDF：该词 1 处 Newsreader Italic span（16.12 pt，bbox 1079.6–1201.8 pt）；网 PDF：全书 0 处 italic span，同词改用 LucernaNewsreader-Regular。文字层本身完好：印/网 pdftotext 归一化 diff 为空。
- **修复建议**：webpdf.py 裁切字体时带上 Newsreader Italic 面；入仓前批量重建解决；修后核查网 PDF 全书 italic span 数 = 印版数（本版：1 处）。

### D6（重大，新增，本次发现）— P4 积分榜段落丢失，fan-out-nl 全家 10 版皆无
- **页码/定位**：P4「HET PROGRAMMA」盒 facts 列表。核心 `content34.py:127` 与核心 P4 SVG（y=1054.4/1084.9）均有第 4 条：`Stand Eredivisie na 12 ronden: PSV 26, Feyenoord 25, Ajax 25 punten.`（共 5 条）。本版 `content34.py` 的 facts 列表只有 4 条（Speelronde 12 后直接 Speelronde 13），P4 SVG 与 text.md 均无此句。
- **归属**：fan-out 机制丢失。grep 验证：10 个 fan-out-nl 版的 `content34.py` 与 `svg/p4-sport.svg` 均无 `Stand Eredivisie na 12`（0 命中）。nl-de 的 P4 同样缺失（nl-de proof1 未列此项——本次为新增发现）。
- **后果**：Q63（PSV staat onderaan in de Eredivisie，答案 Niet waar，注「PSV는 26점으로 에레디비시 선두」）与 Q126（PSV staat bovenaan … met ___ punten，答案 B=26）所考事实在正文中**无出处**，仅答案注自称；读者无法从本期内容推导。P4 目视可见 HET PROGRAMMA 盒偏短、盒下大片空白。
- **外部核实**：该事实本身属实——PSV 12 战 26 分榜首、Feyenoord 25 分（PitchLab、VAVEL、Sports Mole、TuringStats 多源一致；见核实摘要）。错不在事实，在正文缺失。
- **修复建议**：把该句恢复进 fan-out facts 列表与 text.md，重渲染；fan-out-nl 全家 10 版同修（nl-de 的 P4 亦然）。

### D7（轻微，ko 特有）— P2 EN JIJ 盒韩语 gloss 末尾孤儿句号
- **页码/定位**：P2 EN JIJ 盒（y=1022.25，bottom=1445.8）。韩语 gloss 末行只剩一个孤立的 `.`（基线 y=1440.2，PIL ink-bottom 1440.2，盒内余 5.6 px，不溢出）。
- **实测证据**：Zoom 裁图 `zoom-p2-enjij.png` 目视确认：`…편집부에 보내세요` 下一行单独一个 `.`。
- **修复建议**：重排 gloss 使句号跟住 `보내세요`。

## 未决事项

无。本轮必查的外部事实（Amsterdam 入城、Feyenoord–Ajax）均已独立核实（见核实摘要）；nl-de proof1 的未决 O1（Amsterdam 细节未核实）在本版已闭合——10:15 De Omval、13:00 Stopera、「88e editie」全部属实。

## 判为非缺陷的项（摘要，详见 GATE-LOG）
- 几何遮挡审计 0 flags（自检通过）；creambox 全版扫描 372 行，仅 3 处「last baseline」负值，均为盒下相邻标题的已知假阳性（+24.0/+44.0/+32.0）；盒内行 clearance 全为正；P7 toolbox 实测 min inside clearance +12.5、min desc-clear +6.5；P3/P5 右栏奶油盒末行降部：无溢出（PIL 真墨水 + P5 像素扫描确认；任务必查项 (c) 未复现）。
- 必查项 (a)：P1/P2/P7 盒题横向均合规——P1 `IN DEZE EDITIE　이번 호 내용` PIL 1785.5 / 像素 1781.1（盒右缘 1862，余 ~81 px）；P6 `VOOR OF TEGEN?　찬성? 반대?` PIL 1764.5 / 像素 1762.9（余 ~99 px）；P2 `ZO ONTHOUD JE HET　기억해요` PIL 902.5 / 像素 901.9（盒右缘 961，余 ~59 px）。无一 R2-BOX-RIGHT 标记。
- freeze baseline 重跑后 8/8（首次 6/8 因核心 p2/p4 在 11:43 UTC 被核心重建重写，见 GATE-LOG §5）；freeze diff 新增 CJK 共 3449 字符，全为 Hangul + 每页 1 个 U+3000 分隔符；非 Hangul 新增仅 P1「」与 P8『』（合法引号）；p8 compare CLEAN，keydiff [137, 138] 为翻译题合法重定向（键本身正确）；P8 extract 150/150；P8 答案键与 text.md 键逐题比对 0 不符（keycheck-150.json，150/150）。
- P8 最小字号实测 10.12 pt（印版与网版均为 P8 `1. 20:45 —`），SOP §1.1 让步阶梯允许 ≥9.75 pt，合规。
- 引号：text.md U+201C/U+201D/U+2019/U+201E 均为 0；U+0027 ×12（`'s avonds` 等，与核心一致）。新版 text.md CJK：Han 0、U+3000 ×59、「1 」1 『3 』3。
- ABSTRACT.txt：韩语单行 297 字节、0 换行、无 ASCII 双引号，含 `Lucerna VOL.4`、네덜란드어、A2–B2、150문항与真实主题（신터클라스/파크예스아본트/네이션스리그 네덜란드 대 독일/익스페디티 로빈슨）。校准：de 版摘要同样只写 `Lucerna …`（无字面 `A Lucerna`）且已通过——SOP §9 要求的是刊名、目标语名、A2–B2 分级与题数，本版齐全。
- 韩语注时间误译类（pt-ko D5「16:30」→「16일:30」）：未复现。`[0-9]일:[0-9]` 在 text.md 与全部 SVG 均为 0 命中；仅有的两处 `일:` 是日期 gloss 分隔符 `(11월 16일: 독일–네덜란드)` 与 `(12월 5일: 19일 남음)`，与核心全角冒号结构平行，非缺陷。text.md 时间 inventory：20:45×17、12:00×16、20:00×13、18:00×27、16:00×3、10:15×4、11:30×1、13:00×3、16:30×2、18:45×2、14:30×1、12:15×1。
- E 节 type 标签已本地化（번역/한국어로 번역하기/네덜란드어로 번역하기、문장 완성、객관식、빈칸 채우기、단어 짝짓기、참/거짓 판단、문장 만들기、쓰기）；无中文标签。标签计数：A2 문장완성 19、B1 32、B2 14；A2 객관식 21、B1 29、B2 7；A2 단어짝짓기 1、B2 1；B1 참/거짓 6、B2 1；B2 문장만들기 4、A2 1、B1 3；번역 A2 1、B1 2、B2 1；B1 쓰기 1。
- Q78「Zij ___ (maken)」单复数歧义为核心同文、键自洽，不计缺陷。P1 刊首日期行像素 +0.5 px、P2 `Pakjesavond에속한단어는?` span +0.1 px——均为噪声，不计。
- 8 张图片均带目标语图说 + CC0 出处（Wim van Rossem/Anefo、Anefo、W. Punt/Anefo、Spaarnestad Photo/Wikimedia Commons、Elise lovenko/Unsplash、Cristina Gottardi/Unsplash、Aaron Burden/Unsplash——P7 书图为 Cristina Gottardi/Unsplash）。

## 核实摘要
- **身份核对**：印 PDF SHA `d72e53eb31c222fb3882b5644162a8292ec1a8ba0b3481b3b6099f98f710fed8`、网 PDF SHA `a5b50f5985fa7da5dd213ece619c21004c9a4d8698a7c331e5dca64aeecac119`、text.md SHA `bbca93462db80962c14bee566395aea8f3ba8f62d9570c99335ae718cbf92d33` 与任务一致；字节数 17,281,555 / 1,884,427 / 47,383。
- **全文通读**：text.md 全文（pinned 版）+ 印 PDF 8 页逐页目视（150 dpi 自渲染）；日期/星期全部用日历核验（2026-11-01 周日、11-04 周三、11-14 周六、11-15 周日、11-16 周一、11-21 周六、11-22 周日、11-24 周二、11-29 周日、12-05 周六，全部吻合）。
- **外部事实来源**（2026-11-11 检索，5 组）：
  - **PSV 26 分**（题 63、126；亦为 D6 所缺句子的事实依据）：PitchLab「PSV Eindhoven are 1st in the 2026/27 Eredivisie with 26 points from 12 games. Latest result was a 5–2 win at Cambuur on 8 November. Next game away at Nijmegen on 21 November」；VAVEL「PSV lead the table with 26 points after 12 matches, 1 clear of Feyenoord. Matchweek 13 starts on 21 November with NEC Nijmegen v PSV」；Sports Mole 表格 PSV 12 战 8-2-2、40:15、26 分；TuringStats「1 point clear of Feyenoord」。——属实。NEC–PSV 11 月 21 日 원정 확인；16:30 개시 시간은 이번 검색 조각에 미표시（与核心文本一致）。
  - **Grave 入城**（P1/P3）：vandaagingrave.nl：Landelijke intocht 2026 in Grave，2026-11-14 周六，Maaskade，市长 Marieke Moorman，NPO Zapp (NPO 3) 直播，Merel Westrik 主持；mamaliefde.nl：约 12:00 靠岸 Maaskade，节目 12:00–16:00，NPO Zapp (NPO 3) 12:00 起直播，Merel Westrik 主持；playtix：同上 + Sinterklaasjournaal 自 11 月 9 日。——全部属实。注：vandaagingrave 另称节目 11:45 开始、船 12:15 靠岸——文中只写「rond 12:00」（约 12:00），无冲突。
  - **Amsterdam 入城**（P3；题 31、32、139）：desinterklaassite.nl、amsterdam.org、noordhollandnieuws.nl：2026-11-15 周日，船 De Omval 10:15，陆上队伍 Stopera 13:00 出发；amsterdaminside.com 与 holland-explorer.com：gemeente 登记为第 88 届（88ste editie）。——全部属实。注：uitamsterdam.com 一处散文写 10:30 靠岸 De Omval，但其自家节目表明细与所有其他来源均为 10:15（10:30 为 Berlagebrug 时刻），文中 10:15 为多数值。
  - **下期预告欧战**（P7 VOLGENDE WEEK）：UEFA.com 2026/27 Champions League 赛程：Matchday 5，Tuesday 24 November 2026，Feyenoord vs Porto、Real Madrid vs PSV Eindhoven。——属实。
  - **Feyenoord–Ajax**（P7 VOLGENDE WEEK）：FBref、FotMob、Sky Sports：Sun 29 November 2026，14:30 CET，De Kuip（Stadion Feijenoord）。——属实。
- **150 题手验**：`keycheck-150.json`，150/150 ok；算术题重算（19 天、1 天、4 小时、17 年、65、100）；配对题字母对照印刷版 a–d 列表（P2 D：a 愿望单/b 诗/c 食物/d 门口；P8 F：a 诗/b 新闻节目/c 小组头名/d 门口）；137/138 翻译键逐字核对正确（137 `Het Sinterklaasjournaal is elke dag om 18:00 uur te zien.` → 韩 `신터클라스 뉴스는 매일 18:00에 방송해요.`；138 `De nummers één en twee gaan naar de kwartfinales.` → `상위 두 팀이 8강전에 진출해요.`）；范文 81 词（逐词数过，80–100 内，与注称 81단어一致）；P7 八句金句逐字出自正文、页码标注正确（P1×2、P2、P3、P4、P5、P6×2）。
- **源文件未动**：未改动、未重建、未 commit、未 push 任何源文件；全部工作在 goals 侧 scratch。text.md 的中途重写为他人并发操作（见首节说明），非本轮所为。
