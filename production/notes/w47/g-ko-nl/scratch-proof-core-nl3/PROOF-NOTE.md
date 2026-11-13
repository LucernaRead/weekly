# PROOF-NOTE — W47 core-nl 独立复校（fix3 后，proof3）

- 复校员：独立复校（与构建者 / fix3 agent 不同人）
- 对象：`production/2026-w47/core-nl/`，fix3 本地 commit `f567bcea`（未 push）
- 日期：2026-11-11
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-core-nl3/`
- 工具栈：`tools/venv/bin/python`（正典栈；全程未用系统 python3）

## 结论：(a) 无缺陷 —— 可定稿

fix3 的两项改动（D6/D7）**全部回归通过**，且逐元素级实测证明两页除目标
断行外零位移；fix2 的三项改动（D3/D4/D5）全部回归通过；150 题、全部机械门、
全部外部事实均通过；全版孤儿标点扫查为 0。本轮**零新缺陷**，proof2 的 5 项
nits 原样携带（无一升级为缺陷）。

## 0. 环境探针与红线遵守

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin`
  一次通过（返回 `9daeafb9…`）；goals 侧写文件探针通过
 （`hidden_files/w47/probe-proof-core-nl3.txt`）。`/dev/null` 现为 0 字节
  普通垫文件（proof2 留下），终验仍为 0 字节，未增长。
- TMPDIR 全程用 goals 侧 `scratch-proof-core-nl3/tmp`，未用 /tmp 做工具输出。
- 只读生产文件：未改任何成品、未 commit、未 push。终验：`git log` 仍为
  `f567bcea`；`git status --porcelain -- production/2026-w47/core-nl/`
  仅有 fix3 已记的未追踪项（render cache 与未入仓源码），无任何 `M`；
  freeze baseline 亦验“shipped core SVGs unchanged”。
  （工作树另有 W43 旧改动与 fan-out 重建中的未提交改动，均与本轮无关、未动。）

## 1. 身份核对（逐字通过）

| 文件 | 尺寸 | SHA-256（实测） | 任务给定 | 结果 |
|---|---|---|---|---|
| `De-Lucerna-VOL4.pdf`（印） | 25,955,581 B | `82427d3f80af23588726311dd415ff9caefe0cc153dc3b3637444babd4bc9eb7` | 同 | ✓ |
| `De-Lucerna-VOL4-web.pdf`（网） | 2,103,999 B | `44553e5c77d3fbf796939fc35bc43721292e44f1669253cd23fc76c47bcd5a39` | 同 | ✓ |
| `2026-w47-nl-zh-cn.text.md` | 44,088 B | `2f2a650b54989e7b4b656f21cc2ae613e9dc42425a56106f03e00dff6b25d92e` | 同 | ✓ |

HEAD 即 `f567bcea`（`W47 core-nl fix3: D6/D7 orphan 。 (proof2 rounds)`），
为 core-nl 最新提交；复校期间无新的 core-nl 提交出现。
三项 SHA 在开工与收工两次实测一致。

## 2. fix3 回归复测（D6/D7）—— 全部通过

工具：`step0_d6d7_orphan.py`（本轮自写）。对照基线为 proof2 的
freeze build-copy 中的 fix2 SVG（哈希与 fix3 `svg-hashes-before.txt`
逐字节一致，是真实的 fix2 产物，不是重建）。

### D6 — P3 C 节 bridge 句末 `。` ✓ 通过

- 当前 `svg/p3-cultuur.svg`（x=538.5）：两行确为 fix3 所称：
  `用现在完成时补全，注意助动词`（y=2250.5）与 `hebben/zijn。`（y=2280.225）；
  句末 `。` 已回上一行，桥区独行 `。` 为 0。
- 逐元素级 diff（fix2 → fix3，172 个 `<text>`）：**仅 2 个元素变化**，
  且 (x, y) 坐标对完全相同——旧行 `…助动词 hebben/zijn` + 独行 `。`
  换成新两行；P3 的 y 值集合 fix2 与 fix3 **完全相同，无任何位移**。
  印 PDF P3 目视：该句两行干净，无孤儿 `。`。
- 机制核对：`bslib4.py:119` `Flow.para(..., w=None)`、`154` `bridge(..., w=None)`，
  `w=None` 时取栏宽，默认行为不变；`content34.py:78` 传 `w=CW - 40`，
  CW=422.5 故 382.5px，与 FIX-LOG 一致。

### D7 — P7 A2 gloss bridge 句末 `。` ✓ 通过

- 当前 `svg/p7-taal.svg`（x=88.0）：三行确为 fix3 所称：
  `de wedstrijd 比赛；de groepswinst 小组`（y=725.66）、
  `头名；de kwartfinale 四分之一决赛；`（y=755.385）、
  `scoren 进球。`（y=785.11）；句末 `。` 已回上一行，桥区独行 `。` 为 0。
- 逐元素级 diff（fix2 → fix3，175 个 `<text>`）：**仅 3 个元素变化**，
  (x, y) 坐标对完全相同；P7 的 y 值集合 fix2 与 fix3 **完全相同，无任何位移**。
  印 PDF P7 目视：该 gloss 三行干净，无孤儿 `。`。
- 机制核对：`content7.py:19` 传 `w=CW - 35`，即 387.5px，与 FIX-LOG 一致。

### 机制未使其他页面回归 ✓

- 当前 8 页 SVG 哈希与 fix3 `svg-hashes-after.txt` 逐字节一致；
  before → after 仅 p3、p7 两页变化，其余 6 页与 fix2 字节一致。
- 全版 freeze baseline 8/8（见 §5 G12），`w` 默认路径行为不变得到独立验证。

## 3. 孤儿标点全版扫查 —— 0

8 版 SVG 按基线 y 分组；基线拼接后仅含单个字符且该字符属于
{`。` `»` `”` `’` `）` `」` `》` `：` `–`} 才计为真孤儿：

| 页 | 真孤儿 `。` | 真孤儿闭引号 | 真孤儿 `：`/`–` |
|---|---|---|---|
| P1–P8 | 0 | 0 | 0 |

P8 的 7 个单字元 `）`逐一核对，均与同基线 4–6 个 sibling 共行，
为答案区行内定位符（`愿望单（het）`等），不是孤儿：

| 基线 y | siblings | 内容 |
|---|---|---|
| 1818.64 | 6 | `54. ongeslagen — … / 未尝败绩 / 93. verlanglijstje — … / 愿望单（/ het / ）` |
| 1848.3 | 6 | `55. stand … / 94. surprise … / 伪装礼物（/ de / ）` |
| 1877.96 | 6 | `56. interland … / 95. gedicht … / 诗（/ het / ）` |
| 2325.44 | 4 | `70. surprise … / 伪装礼物（/ de / ）` |
| 2355.1 | 4 | `71. verslaggever … / 记者（/ de / ）` |
| 2384.76 | 4 | `72. proef … / 比赛项目、考验（/ de / ）` |
| 2414.42 | 4 | `73. gedicht … / 诗（/ het / ）` |

## 4. fix2 回归复测（D3/D4/D5）—— 全部通过

### D3 — P2 D 选项 c 溢出修复 ✓ 通过（与 proof2 逐数一致）

| 行 | advance 右缘 / clearance | 真墨右缘 / clearance |
|---|---|---|
| a. een lijst met wensen voor（＋折行 Sinterklaas） | 1764.2 / +97.8；折行 +269.4 | 1764.5 / +97.5 |
| b. een klein versje bij een cadeau | 1816.5 / +45.5 | 1817.5 / +44.5 |
| c. eten voor Sinterklaas' paard | 1790.1 / **+71.9** | 1790.5 / **+71.5** |
| d. die staat 's avonds bij de deur | 1806.5 / +55.5 | 1806.5 / +55.5 |
| 25. de schoen | 1589.7 / +272.3 | 1583.5 / +278.5 |
| 26. de wortel | 1582.3 / +279.7 | 1576.5 / +285.5 |
| 27. het verlanglijstje | 1662.9 / +199.1 | 1653.5 / +208.5 |
| 28. het gedicht | 1603.2 / +258.8 | 1596.5 / +265.5 |

版心右缘 1862，门限 ≥+5px。c 项真墨 clearance **+71.5px**，
与任务书允许的 ±2px 方法差内与声称值一致（实为逐数一致）。
旧串 P2 渲染行残留 0；印/网双 PDF 文字层含新串、旧串 0；P2 目视 c 行居栏内。

### D4 — 答案标记本地化 ✓ 通过（9 版 text.md 全验，实质不变）

| 版 | 新标记 | 新配对裸词 | 「答案」残留 | 他语标记串入 |
|---|---|---|---|---|
| nl-de `— Antwort:` | 142 | 8 | 0 | 无 |
| nl-en `— Correct:` | 142 | 8 | 0 | 无 |
| nl-es `— Respuesta:` | 142 | 8 | 0 | 无 |
| nl-fr `— Réponse:` | 142 | 8 | 0 | 无 |
| nl-it `— Risposta:` | 142 | 8 | 0 | 无 |
| nl-ja `— 答え：` | 142 | 8 | 0 | 无 |
| nl-ko `— 정답：` | 142 | 8 | 0 | 无 |
| nl-pt `— Resposta:` | 142 | 8 | 0 | 无 |
| nl-ru `— Ответ：` | 142 | 8 | 0 | 无 |

- 对照组未动：core-nl（zh-cn）432 行、162 行含「答案」、`— 答案：`142 处；
  nl-zh-tw 430 行、162 行含「答案」、`— 答案：`142 处。
- 行数说明（非缺陷）：本轮实测 de/en/es/fr/it 为 431 行、ja/ko/pt/ru 为 430 行，
  proof2 表记全为 430 行。原因是并行重 fan-out 正在进行中：工作树 5 版
  已按 fix2 核心重生成（新增 D5 积分行 +1 行，即 431 行；另含重 fan-out
  自己的德语标题微调，如 `IN DIESER AUSGABE`→`AUSGABE`、`MERK ES DIR`→`MERK DIR`），
  其余 4 版尚未重写。D4 实质（142/8/0/无串入）在两种状态下完全一致；
  fan-out 文件不在 core-nl 复校范围，其重建归协调员。
  （中途一次 `wc` 读到 it 版 430 行、数分钟后变 431 行，正是并行重写进行中的活证据。）

### D5 — P4 积分行与 Q126 一致性 ✓ 通过

- 四处均存在：`svg/p4-sport.svg`（两行：y=1054.37
  `Stand Eredivisie na 12 ronden: PSV` / y=1084.90
  `26, Feyenoord 25, Ajax 25 punten.`）、印 PDF 文字层、网 PDF 文字层、
  text.md 第 188 行。
- P4 目视：新行在 HET PROGRAMMA 框内（框 x=1439.5 y=591.6 w=422.5 h=611，
  底缘 1202.6；末行基线 1084.9，余量 ~118px）；框 0 旗标。
- Q63 注（text.md 第 216 行“PSV 26 分领跑荷甲”）与 Q126 题干/注（第 398 行，
  答案 B·26 分）均与该行一致；Q126 选项 A.25 / B.26 / C.8 中 25 为
  Feyenoord 实际分数（活干扰项），8 为 Nations League 分数。
- 积分事实独立公开核实（本轮新检索，12 源一致，见 §6）：第 12 轮
  （11 月 8 日）后 PSV 26 分第 1、Feyenoord 25 分第 2、Ajax 25 分第 3。

### D5 字体（拉丁讲解层落在 Noto Sans CJK SC）—— 全周级已知待定项，只记录

- 全版 `<text>` 字体普查：Noto Sans CJK SC 619 段、Newsreader 1215 段、
  Noto Serif CJK SC 304 段、UnifrakturMaguntia 1 段。
- 其中 CJK 字体段含拉丁字母者 335 段；纯拉丁字母（无任何 CJK 字符）却落在
  CJK 字体者 **245 段**（分版 38/23/30/29/29/26/18/52）。
  此为全周级已知待定项，本轮只记录实测段数，不以此判 (b)。

## 5. 全量独立复校（核心层）

- text.md 432 行全文通读；印 PDF 8 页逐页目视（PyMuPDF 自渲染 1.5×，
  `render/p1–p8.png`，即本轮自渲染的已交付印 PDF）。
- 150 题逐题手验（见 `keycheck-150.json`）：三源交叉——
  (1) text.md 答案（全文通读时逐题对文章核对）、(2) P8 印出键
  （`p8.py extract` 机械对照 0 不符，配对项 25–28 d/c/a/b 与 141–144
  b/c/d/a 逐项一致）、(3) 各版 SVG 渲染题干（8 页目视）。
  **PASS 150、MISMATCH 0**；Q150 为开放写作题（范文 81 词，P8 印 `✓`）。
- 题量分布：按版 10/18/18/18/18/18/12/38＝150；级别 A2 46 / B1 73 / B2 31
  （`run.py` 注册表；text.md 正则计数为 A2 43/B1 73/B2 28＝144，
  系配对项走范围标题行的计数口径差，注册表为准——proof2 同款口径差）。
- 金句 8 条逐字出自正文（已机验）；Q150 范文空白分隔计 81 词
  （除独立 `–` token 计 80 词），均在 80–100 要求内。
- 验算抽查（手算复核）：Q22/Q45 16 Nov→5 Dec＝19 天 ✓；
  Q43 14→15 Nov＝1 天 ✓；Q44 12:00–16:00＝4 小时 ✓；
  Q46 2009→2026＝17 年 ✓；Q83–87 图表 35/30/65/15/100 ✓
  （35+30+20+15=100）；Q39–42 完成时助动词 ✓；Q57–60 过去时 ✓；
  Q76–79 gaan＋不定式 ✓（Q78 zij 单数用 gaat、Q79 复数用 gaan）；
  Q97–100/Q133–136 造句 ✓；Q137–140 翻译 ✓；Q150 范文星期三
  （11 月 18 日）与“Op woensdag”一致 ✓。
- D 配对交叉核对：P2 右栏 a/b/c/d 与 text.md 25–28 键（d/c/a/b）一致；
  P8 F 右栏 a/b/c/d（含 b 项折行 `televisie`）与 text.md 141–144 键
  （b/c/d/a）一致。
- 弯引号全扫：8 版 SVG `<text>`＋text.md：ASCII 双引号 0 处、反引号 0 处；
  `« »` 成对（P1 1对、P2 2对、P7 30对、P8 2对；text.md 35/35）；
  `“ ”` 仅 P1 一对（本周词中文释义，与 text.md 第 46 行一致）。
  直引号 `'` 11 处全部为荷兰语合法省音/所有格（`'s avonds`、`'s nachts`、
  `Sinterklaas'`），已逐条列出（`step3b-p8compare.txt`），无直引号误用。
- 构建重放（干净拷贝）：`run.py` TOTAL 150，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；
  重建 8 页 SVG 与已交付逐字节一致；重建印 PDF 与已交付
  **逐字节一致**（25,955,581 B，SHA `82427d3f…b4bc9eb7`）。

### 缺陷清单

**零缺陷。** 本轮未发现任何新缺陷；D6/D7 已修且回归通过；proof2 的
5 项 nits 原样携带（见 §7），无一升级。

## 6. 外部事实独立核查（全部通过）

| 事实 | 刊登内容 | 核实结果 |
|---|---|---|
| Eredivisie 第 12 轮后积分 | PSV 26、Feyenoord 25、Ajax 25 | ✓ 本轮新检索 12 源一致（Sportradar / PitchLab / Sports Mole×2 / VAVEL×2 / elFutbolero / Road2Sushi / Sports Oracle / TuringStats / Pitchside Lab / BankoZeka；PSV 12 场 8-2-2，Feyenoord/Ajax 7-4-1） |
| Eredivisie 第 12 轮比分 | Heerenveen–Feyenoord 5–3；Cambuur–PSV 2–5；Twente–Ajax 2–2 | ✓ 与刊登一致（elFutbolero：Feyenoord 2–0 领先被 5–3 翻盘、PSV 随后 5–2 取胜登顶） |
| Eredivisie 第 13 轮 | 21–22 Nov；NEC–PSV 周六 16:30、Feyenoord–Excelsior 周六 18:45、Ajax–ADO 周日 14:30、Twente–Willem II 周日 12:15 | ✓ UTC 开球 15:30/17:45/13:30/11:15（Sportradar / VAVEL / SportSignals / TheStatsAPI / SmartCalendars），→CET 换算一致 |
| Nations League A2 积分 | NED 8、GRE 8、GER 5、SRB 0；NED 居首因进球 7–5 | ✓ proof2 已验多源一致，本轮刊登内容与 P1/P4 两处一致，未变 |
| 日期星期（`date -d` 核） | 11 Nov 周三、14 Nov 周六、15 Nov 周日、16 Nov 周一、21 Nov 周六、22 Nov 周日、24 Nov 周二、29 Nov 周日、5 Dec 周六 | ✓ 逐项一致 |
| 日数验算 | 16 Nov→5 Dec 19 天；22 Nov→5 Dec 13 天；14→15 Nov 1 天；2009→2026 17 年 | ✓ 手算一致 |

其余外部事实（Sinterklaas 两场入城式、Heel Nederland Leest、Expeditie
Robinson、欧冠 24 Nov、Feyenoord–Ajax 29 Nov 等）proof2 已逐项核实，
本轮刊登文本与 fix2 字节一致（text.md SHA 未变），未重验——无变化即无新风险。

## 7. 非阻塞观察（nits，proof2 原样携带，不入缺陷）

- N1：Q85 题干「Wortel en verlanglijstje samen」——图表 35 人行实为
  「Een wortel en een tekening」；题干略去「en een tekening」，答案唯一
  （35＋30＝65），可理解。
- N2：Q81「Expeditie Robinson speelt in Spanje」——表示地点宜用
  「speelt zich af in」；答案不受影响。
- N3：P7 末尾 VOLGENDE WEEK 深色带：末行基线 2551.56，带底 2557.0，
  墨底约 2556.6，0px 溢出（与 proof2 实测完全一致——P7 y 值集合未变），
  但视觉上贴底，建议带高＋6px 或减一行。
- N4：Q18/Q93「Op het ___ staan drie wensen」——「三愿」未见于正文
  （正文只说「lijst met wensen」），属练习句合理发挥，答案不受影响。
- N5：Q150 范文词数计法差异（81 含独立 `–` token / 80 不含），
  均在 80–100 区间内，无影响。

## 8. 复核工具手记（非缺陷，供下轮参考）

- proof2 的 `step3_gates.py` 金句小节确会因 `md` 为 list 而崩溃——本轮
  已在自用拷贝中改成 `"\n".join(md)` 再 `findall`，金句 8/8 一次跑通。
  其内嵌 p8 小节未传 `--json` 报 noted set 0 是已知口径问题，
  以独立跑的 `p8.py extract --json`（150/150）为准。
- proof2 的 `step4b_inkprobe.py` 首个正则只有 2 个分组（x 与文本），
  P6 的 y 值恰好精确匹配时 `group(2)` 取到文本而 `float()` 崩溃；
  本轮已在自用拷贝中把 y 捕获为 group(2)，P5/P6 均一次跑通。
  `step4_inkprobe.py` 的 P5 段会因左右两栏框在 y 上重叠而取错候选框
  致 crop 崩溃，P5 改由 step4b（按文本 x 选框）裁定，与 proof2 做法一致。
- proof2 的 P6 全宽带扫描得墨底 664.44（疑似框底边），本轮紧贴文本
  x 跨度的窄带扫描得 661.0、step4b 带得 661.4（余量 +3.6~+4.0px）；
  决定性判据（框底以下 7px 带）三轮均为 0 墨点，结论一致：假阳性。
- `step3b` 的“level counts incl. match items: A2=47/B1=73/B2=32”与注册表
  46/73/31 相差 1+1，系该脚本把范围标题行与单项重复计数，
  注册表（`run.py`）为准，非内容问题。
