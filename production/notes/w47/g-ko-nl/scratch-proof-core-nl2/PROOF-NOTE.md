# PROOF-NOTE — W47 core-nl 独立复校（fix2 后，proof2）

- 复校员：独立复校（与构建者 / fix2 agent 不同人）
- 对象：`production/2026-w47/core-nl/`，fix2 本地 commit `5de7492f`（未 push）
- 日期：2026-11-11
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-nl2/`
- 工具栈：`tools/venv/bin/python`（正典栈；全程未用系统 python3）

## 结论：(b) 有缺陷 —— D6、D7 两项同类轻微排版缺陷，须 fix3 后重校

fix2 的三项改动（D3/D4/D5）**全部回归通过**，150 题、全部机械门、全部外部事实均通过。
但全量独立复校发现 **2 项新缺陷**（均非 fix2 引入，是 fix-round 遗留、proof1 漏检）：
句末中文句号 `。` 被断行器单独甩到下一行独占一行，P3、P7 各一处，印 PDF 实渲染可见。
**不可定稿**；修后须重校这两处（+ 全量门禁重跑）。

## 0. 环境探针与红线遵守

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 初次失败，
原因是本机 `/dev/null` 缺失（`ls /dev` 无 null 设备；`mknod` 被拒 Operation not permitted）。
以普通文件 `touch /dev/null` 垫上后 git 恢复，hash-object 返回 `9daeafb9…`，探针通过才开工。
注意：该垫文件目前仅 46 字节；若后续有进程向 /dev/null 大量写出会累积，需留意。
- goals 侧写文件探针通过（`scratch-proof-core-nl2/probe.txt`）。
- TMPDIR 全程用 goals 侧 `scratch-proof-core-nl2/tmp`，未用 /tmp 做工具输出。
- 只读生产文件：未改任何成品、未 commit、未 push；活动范围仅 `production/2026-w47/`（读）
与 `hidden_files/w47/`（写 scratch）。`git status` 与开工时一致（仅 W43 旧改动，与本轮无关，未动）。

## 1. 身份核对（逐字通过）

| 文件 | 尺寸 | SHA-256（实测） | 任务给定 | 结果 |
|---|---|---|---|---|
| `De-Lucerna-VOL4.pdf`（印） | 25,955,593 B | `5308f4a3…bd361f8` | 同 | ✓ |
| `De-Lucerna-VOL4-web.pdf`（网） | 2,104,002 B | `a5f7ecba…6a1cfd3` | 同 | ✓ |
| `2026-w47-nl-zh-cn.text.md` | 44,088 B | `2f2a650b…b25d92e` | 同 | ✓ |

HEAD 即 `5de7492f`（`W47 core-nl fix2: D3 match overflow + D4 answer-marker localization + D5 Eredivisie standings`）。

## 2. fix2 回归复测

### D3 — P2 D 选项 c 溢出修复 ✓ 通过

- SVG 实测（`svg/p2-leven.svg` 渲染行，x=1473.5，版心右缘 1862）：
- advance 宽度（builder `text_w`，Newsreader 23px）：c 右缘 1790.1，clearance **+71.9px**（与 fix2 声称一致，门限 ≥+5px）
- PIL 真墨（FreeType `getbbox`，同字体同字号）：c 墨右缘 1790.5，clearance **+71.5px**
- 同页其余 D 选项（真墨）：a 两行 +97.5 / +269.4（第二行 "Sinterklaas"）、b +44.5、d +55.5；左列 25–28 真墨 +278.5 / +285.5 / +208.5 / +265.5 —— 全部 ≥+5px，无新溢出
- 旧串 `eten voor het paard van Sinterklaas` 在 P2 渲染行中残留 0 处（正文第 68 行与 Q21 题干中的同串为正确用法，未动）
- P2 目视（自渲染印 PDF）：c 行 `c. eten voor Sinterklaas' paard` 居栏内，D 组四行整齐，无溢出、无遮挡
- text.md 第 124 行已同步为新串；P2 双 PDF 文字层均含新串、旧串 0 处

### D4 — 答案标记本地化 ✓ 通过（9 版 text.md 全验）

| 版 | 行数 | 新标记 | 新配对裸词 | 「答案」残留 | 他语标记串入 |
|---|---|---|---|---|---|
| nl-de `— Antwort:` | 430 | 142 | 8 | 0 | 无 |
| nl-en `— Correct:` | 430 | 142 | 8 | 0 | 无 |
| nl-es `— Respuesta:` | 430 | 142 | 8 | 0 | 无 |
| nl-fr `— Réponse:` | 430 | 142 | 8 | 0 | 无 |
| nl-it `— Risposta:` | 430 | 142 | 8 | 0 | 无 |
| nl-ja `— 答え：` | 430 | 142 | 8 | 0 | 无 |
| nl-ko `— 정답：` | 430 | 142 | 8 | 0 | 无 |
| nl-pt `— Resposta:` | 430 | 142 | 8 | 0 | 无 |
| nl-ru `— Ответ：` | 430 | 142 | 8 | 0 | 无 |

- 对照组未动：core-nl（zh-cn）432 行、162 行含「答案」、`— 答案：`142 处；nl-zh-tw 430 行、162 行含「答案」、`— 答案：`142 处 —— 与 fix 前声称一致
- 9 版 PDF 尚未重建（待重 fan-out），本轮只核 text.md + core PDF（与任务范围一致）

### D5 — P4 HET PROGRAMMA 框增积分行 ✓ 通过

- 四处均存在：`svg/p4-sport.svg`（两行：y=1054.37 `Stand Eredivisie na 12 ronden: PSV` / y=1084.90 `26, Feyenoord 25, Ajax 25 punten.`）、印 PDF 文字层、网 PDF 文字层（空白归一化后整句匹配）、text.md 第 188 行
- P4 目视：新行在 HET PROGRAMMA 框内（框 x=1439.5 y=591.6 w=422.5 h=611，底缘 1202.6；末行基线 1084.9，距框底 ~118px）；框 0 旗标（creambox 全版 0 真溢出，见 §4）
- Q63 注（text.md 第 216 行）与 Q126 题干/注（第 398 行）原文未动，现均可从正文直接验证（26 可读；25 为 Feyenoord 实际分数，是活干扰项；8 为 Nations League 分数）
- 积分事实独立公开核实（11 源一致，见 §5）：第 12 轮（11 月 8 日）后 PSV 26 分第 1、Feyenoord 25 分第 2、Ajax 25 分第 3 —— 与刊登句逐字相符，顺序与积分榜一致

## 3. 全量独立复校（核心层）

- text.md 432 行全文通读；印 PDF 8 页逐页目视（PyMuPDF 自渲染 1.5×，`render/p1–p8.png`）
- 150 题逐题手验（见 `keycheck-150.json`）：149 题答案与正文/题干核对通过，Q150 为开放写作题（范文 81 词，见下）；p8 印出键与 text.md 答案对照 0 不符
- 题量分布：按版 10/18/18/18/18/18/12/38＝150；级别 A2 46 / B1 73 / B2 31（与 FIX-LOG 声称一致）
- 金句 8 条逐字出自正文（已机验）；Q150 范文空白分隔计 81 词（除独立 `–` token 计 80 词），均在 80–100 要求内
- 验算抽查：Q22/Q45 16 Nov→5 Dec＝19 天 ✓；Q43 14→15 Nov＝1 天 ✓；Q44 12:00–16:00＝4 小时 ✓；Q46 2009→2026＝17 年 ✓；Q83–87 图表 35/30/65/15/100 ✓；Q39–42 完成时助动词 ✓；Q57–60 过去时 ✓；Q76–79 gaan＋不定式 ✓；Q97–100/Q133–136 造句 ✓；Q137–140 翻译 ✓
- D 配对交叉核对：P2 右栏 a/b/c/d 与 text.md 25–28 键（d/c/a/b）一致；P8 F 右栏 a/b/c/d（含 b 项折行 `televisie`）与 text.md 141–144 键（b/c/d/a）一致

## 4. 新缺陷（须 fix3）

### D6 — P3 句末 `。` 独占一行（C 节说明句）

- 位置：第 3 版，中栏 C `HET PERFECTUM` 节说明句
- 实测：SVG `p3-cultuur.svg`：说明句 `用现在完成时补全，注意助动词 hebben/zijn`（x=538.5, y=2250.5, 20.5px）后，句号 `。` 单独成一 `<text>`（x=538.5, y=2280.225, 20.5px）—— 行内仅此一字
- 证据：自渲染印 PDF P3 裁图 `render/crop-p3-orphan.png` 可见独行 `。`；text.md 中该句为一行带句号（断行器在 SVG 层将其甩出）
- 严重度：轻微——可见的排版瑕疵，不影响理解与答案；但 proof-until-zero 下不可留
- 建议修法：重排该说明句使 `。` 回上一行（缩短行宽预算或提前断行）

### D7 — P7 句末 `。` 独占一行（A2 词汇 gloss）

- 位置：第 7 版，左栏 A2 `VOETBALWOORDEN` 词汇行
- 实测：SVG `p7-taal.svg`：`；de kwartfinale 四分之一决赛；scoren 进球`（x=88.0, y=755.385, 20.5px）后，句号 `。` 单独成一 `<text>`（x=88.0, y=785.11, 20.5px）—— 行内仅此一字
- 证据：自渲染印 PDF P7 裁图 `render/crop-p7-orphan.png` 可见独行 `。`；text.md 中该 gloss 为一行带句号
- 严重度：轻微——同 D6
- 建议修法：同 D6；修后应全版重扫此类孤儿标点（本轮扫查：8 版仅此 2 处真孤儿 `。`；P8 的 `：`/`）`/`–` 单字元为答案区行内定位符，非独行，已排除；补充扫查独行闭引号 `»”’ ） 」 》` 0 处）

## 5. 外部事实独立核查（全部通过）

| 事实 | 刊登内容 | 核实结果 |
|---|---|---|
| Nations League A2 四轮后积分 | NED 8、GRE 8、GER 5、SRB 0；NED 居首因进球 7–5 | ✓ 5 源以上一致（Sports Mole / TuringStats / NBC / TNT / bundesliga.com；UEFA 口径） |
| NL 四场比分 | 1–1 GER（主）、2–1 SRB（客）、2–2 GRE（客）、2–1 SRB（主） | ✓ 与 MD1–MD4 官方赛果逐场一致 |
| GER 三场比分 | 0–1 GRE（主）、2–0 SRB、0–0 GRE（客） | ✓ 一致 |
| MD5 周五 | Oranje 主场对希腊（Johan Cruijff ArenA）、德国客场在贝尔格莱德对塞尔维亚 | ✓ 13 Nov 赛程一致（比分未刊登——已知 §4 未决项，不作缺陷） |
| MD6 周一 | 柏林 Olympiastadion、20:45、NPO 3、小组最后一场、前二进 2027-03 四分之一决赛 | ✓ 一致 |
| Eredivisie 第 12 轮 | Heerenveen–Feyenoord 5–3；Cambuur–PSV 2–5；Twente–Ajax 2–2 | ✓ 8 Nov 赛果一致（多源） |
| Eredivisie 12 轮后积分 | PSV 26、Feyenoord 25、Ajax 25 | ✓ 11 源一致（见 D5） |
| Eredivisie 第 13 轮 | 21–22 Nov；NEC–PSV 周六 16:30、Feyenoord–Excelsior 周六 18:45、Ajax–ADO 周日 14:30、Twente–Willem II 周日 12:15 | ✓ 四场开球时间经 UTC→CET 换算一致（15:30/17:45/13:30/11:15 UTC） |
| Sinterklaas 全国入城式 | 14 Nov 周六 Grave、Maaskade 约 12:00、Marieke Moorman 迎接、12:00–16:00、NPO 3 直播、Merel Westrik、Sinterklaasjournaal 9 Nov 起每日 18:00 | ✓ 多源一致（市政府/NTR/地方媒体；一源称靠岸 12:15，刊登用「约 12:00」在容差内） |
| 阿姆斯特丹入城式 | 15 Nov 周日、第 88 届、船 10:15 De Omval、11:30 Scheepvaartmuseum（市钥匙）、13:00 Stopera 起步、经 Rembrandtplein/Utrechtsestraat 至 Leidseplein | ✓ 组织方时刻表逐项一致 |
| Sinterklaas 的马 | Ozosnel | ✓ 传统马名一致 |
| Heel Nederland Leest 2026 | 《Het diner》Herman Koch，2009，11 月图书馆免费领（非会员亦可），大字版/简易版/电子书/有声书、读书会 | ✓ 多源一致（Wikipedia 2009 年出版；各图书馆公告） |
| Expeditie Robinson 2026 | 19 人（荷兰＋佛拉芒）、马来西亚、34 天、Nicolette Kluijver＋Edson da Graça 主持、Camille Vanuxem 记者、11 月 1 日周日 20:00 RTL 4 首播、每周日 | ✓ Wikipedia/RTL/多家媒体一致（10 荷兰＋9 佛拉芒） |
| 下期预告 | 24 Nov 周二 Real Madrid–PSV、Feyenoord–FC Porto（欧冠）；29 Nov 周日 Feyenoord–Ajax | ✓ UEFA/多源一致（欧冠 MD5 周二 24 Nov；Feyenoord–Ajax 29 Nov 第 14 轮） |
| 日期验算 | pakjesavond 5 Dec 为周六；Sint-Maarten 11 Nov 为周三；16 Nov→5 Dec 为 19 天；22 Nov→5 Dec 为 13 天 | ✓ 日历一致 |

## 6. 非阻塞观察（nits，不入缺陷）

- N1：Q85 题干「Wortel en verlanglijstje samen」——图表 35 人行实为「Een wortel en een tekening」；题干略去「en een tekening」，答案唯一（35＋30＝65），可理解；建议改为「Wortel-en-tekening en verlanglijstje samen」。
- N2：Q81「Expeditie Robinson speelt in Spanje」——表示地点宜用「speelt zich af in」；答案不受影响。
- N3：P7 末尾 VOLGENDE WEEK 深色带：末行基线距带底仅 5.4px，下伸笔画墨底约 2556.6（带底 2557），0px 溢出（框底以下 7px 带像素探针 0 墨点），但视觉上贴底，建议带高＋6px 或减一行。
- N4：Q18/Q93「Op het ___ staan drie wensen」——「三愿」未见于正文（正文只说「lijst met wensen」），属练习句合理发挥，答案不受影响。
- N5：Q150 范文词数计法差异（81 含独立 `–` token / 80 不含），均在 80–100 区间内，无影响。

## 7. 机械门结果摘要（详见 GATE-LOG.md）

16 项门禁中 16 项通过，2 处排版缺陷（D6/D7）由目视＋孤儿标点扫查发现（非门禁数值项）。
gates_core 16/16（本轮自定的 16 项核对清单——仓内无名 `gates_core` 的脚本；见 GATE-LOG.md 说明）。
