# PROOF-NOTE — 2026-W47 en-ja · proof2（独立复校，Q73 delta 重建版）

- **版**：2026-W47，英语目标语 × 日语读者版（en-ja），VOL.4，刊期 2026-11-16..22
- **复校员**：独立复校（与建版者/delta 执行者不是同一人），SOP §8.4 proof2
- **复校日期**：2026-11-11
- **对象目录**：`production/2026-w47/2026-w47-en-ja/`
- **复校对象**：Q73 delta 重建版（delta 记录 `hidden_files/w47/scratch-delta-en-ja/DELTA-NOTE.md`）；proof1 为 (a) PROVISIONAL（`hidden_files/w47/scratch-proof-en-ja1/PROOF-NOTE.md`）
- **工作区**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-ja2/`（全部日志与证据在此；绝未写 repo 侧 hidden_files，绝未改生产目录任何文件）
- **结论：(a) 定稿零缺陷** —— Q73 四源一致为 up，delta 改动范围恰好 1 键，全部机械门通过，150 题逐题手验无误，8 页逐页目视干净；proof1 的 D1–D6 复验仍为已修。**确认 en-ja 可定稿。**

## 对象核对（SHA 全量匹配，复核前后各测一次）

| 文件 | 大小 | SHA-256（复核前＝复核后） | 结果 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ja.pdf`（印刷） | 41,509,391 B | `e91ed980047959177588a26c72fff55bc2710c7ce476d631d87d1bcd20c19542` | MATCH |
| `The-Lucerna-VOL4-en-ja.web.pdf`（网页） | 2,883,888 B | `fb903b2b1da9be8abc04ad40e6387cb6050eaa41bc4c3c63b0eddb07150f48f0` | MATCH |
| `2026-w47-en-ja.text.md` | 53,585 B | `2d498e4e9b997c85b00671aef294d197b5be420d1eeb9bbf0efcac6d50c3b96e` | MATCH |

三者均与任务简报一致（与修前比：印大小不变 SHA 变；网 +11 B；文 −3 B）。两 PDF 各 8 页。复校全程只读生产目录（run.py / render 全部在工作区 scratch 副本里做；网 PDF 重渲只在 scratch 里做，已发网 PDF SHA 复核后仍为 `fb903b2b…`，未动）。`git status` 仅显示本版目录为未跟踪状态——fanout 轮未 commit 的既有状态，本轮未改动 repo 内任何文件。

## Delta 范围复核（实测，非复述 delta 报告）

- **registry diff（pre 备份 vs 现盘）**：恰好 1 行——`583c583 < "key": "speak" --- > "key": "up"`（`registry-diff.log`）。
- **text.md diff（pre 备份 vs 现盘）**：恰好 1 行——`1151c1151 < 73. [A2] 文の完成 — speak (speak up = 声を上げる) --- > 73. [A2] 文の完成 — up (speak up = 声を上げる)`（`textmd-diff.log`）；文件 53,588 → 53,585 B（−3），registry 21,314 → 21,311 B（−3）。
- **SVG 变化范围（pre-svg 备份 vs 现盘 SVG，逐字节前缀/后缀定位 + 后缀恒等复测）**：P1–P7 **字节一致**；P8 仅一处差异，字节 1228700 起 `73. speak`（5 B）→ `73. up`（2 B），总长 1,237,869 → 1,237,866（−3 B），差异点之后后缀逐字节恒等（`svg-byte-diff.log`）。P5 哈希 `cacd38b4…` = 修前哈希——正确且预期：键只出现在 P8 答案页，不出现在 P5 题干页。
- **残留 `speak` 扫查**：registry `"key": "speak"` 0 命中。
- **源头**：`content56.py:49` 现为 `f.ex("A2", "文の完成", "up", "speak up = 声を上げる",`（只改 key 一处）。

## Q73 四源一致（均为 up，全部实测）

| 源 | 实测值 |
|---|---|
| registry（Q73） | `{'n': 73, 'page': 5, 'level': 'A2', 'type': '文の完成', 'key': 'up', 'note': 'speak up = 声を上げる'}` |
| text.md:1151 | `73. [A2] 文の完成 — up (speak up = 声を上げる)` |
| P8 印刷键（文字层 + 目视放大） | `73. up`（P8 答案行 `73. up · 74. d · 75. a · 76. b (right = 権利 b) · 77. c · 78. Schools`；`render/p8-answers-zoom.png` 目视确认） |
| P5 题干 + 注记 | `Speak ___: tell a teacher.`（P5 印刷文字层 + 渲染目视，`render/p-5.png` / `p5-q73-zoom.png`）；注记 `speak up = 声を上げる`；填入后 "Speak up: tell a teacher." 合理 |

## 旧缺陷复验（proof1 D1–D6，全部仍为已修）

| 编号 | 复验结果 |
|---|---|
| D1 | Q39=a、Q40=d 四方一致（registry 38=b、39=a、40=d、41=c；keycheck Q38–41 = b/a/d/c；P8 抽取键一致；P3 匹配定义逐组核对无误） |
| D2 | P2 DID YOU KNOW 末行 "November 3." 基线余量 **+14.3**（creambox inside-only） |
| D3 | P1 SEARCHES 注脚基线余量 **+12.0**；P1 渲染目视确认行在奶油盒内 |
| D4 | ABSTRACT 完整式 666 B，含 Lucerna、VOL.4、150、A2、B2 各 1×，0 个 ASCII 双引号 |
| D5 | "HAYMITCH'S GAMES　ヘイミッチ戦" 385.4 px，余量 **+19.1**（advance 与 PIL 真墨一致）；P3 渲染目视确认标题在奶油盒内 |
| D6 | P5 D 节说明单行 "現在進行形で書きかえよう。"（SVG y=2543.95，页脚线上 52 px）；栏 3 顶部为 Q78–81 本题，无孤字；P5 渲染目视确认 |
| carry-forward | P5 ODD SOCKS 标题真墨余量 **+23.5**；P6 A PRACTICE BALLOT 标题真墨余量 **+65.5**；THE WEEK IN NUMBERS 最紧 **+1.5**（advance 与真墨一致）；SAY IT 三格全 fit（proof1 实测，本轮目视确认版式未变） |

## 150 题逐题手验（全文通读 text.md 1305 行 + 三源机械核对）

- **text.md 答案 1–150 对 registry.json 逐项一致**（键、级别、题型；编号连续；**0 差异**，`answers-150.log`）。
- **registry 对 P8 抽取键 149/150**（唯一不符 Q150，见观察项工具 bug；`keycheck.log`）。registry 对 core-en 145/150，diff 仅 5 个读者语键 137–140、150（预期）。
- **填空/改写键适配**：AST 抽取全部 `___`/`→` 题 53 项逐项审读，**53/53 键合理**（含 Q73 "Speak up"）；与 registry 1:1 映射 53 项，unmapped/multi 均为 0（`fill-rewrite.log`、`fill-rewrite-map.log`）。说明：fill 日志内的题号为 ex 调用序号（非 registry n），Q73 在该日志中为第 61 个 ex 调用，键 'up'——编号差异是脚本计数口径，不是内容差异。
- **四组匹配题对印刷定义逐组语义核对无误**：P2 Q24–27（24=b runoff、25=c certify、26=a turkey、27=d Thanksgiving）、P3 Q38–41（见 D1）、P4 Q56–59（56=b Test、57=c tour、58=d injury、59=a break）、P5 Q74–77（74=d bullying、75=a speak up、76=b right、77=c silence）、P8 Q141–144（141=b call、142=c runoff、143=d certify、144=a midterm）。
- **改动题语义核对**（proof1 已核，本轮逐题重读确认未变）：Q46 A（2025-11-21 周五珀斯首战）、Q52 hosted、Q55 won、Q125 A（4–1）、Q7 B、Q82 B、Q83 C、Q84 A、Q47 C、Q48 B、Q49 A、Q50 C、Q51 B；Q107 win（见标题现在时）；Q108–111 纠错句（won / continued / more than / whether）正确；Q112–119 完形（Tuesday / call / continues / will meet / writes / will certify / wears / will watch）正确；Q145–149 对话（row / film / popcorn / show / Friday）正确；Q137–140 翻译正确。
- **复用题**：Q2/Q79 同题干同键 call、Q5/Q80 同题干同键 changed、Q6/Q12 同题干同键 January——三组均为既有复用（P1 试做 + 后页正文），两处一致，无矛盾。
- **每页题数**：10/17/18/18/18/18/12/39；级别 A2 62 / B1 66 / B2 22。
- **金句 8 条页码标注**与正文一致（P2、P1、P4、P6、P6、P3、P5、P1），引文均与原文逐字一致。
- **未证实微观说法**（与 proof1 相同，记为未证实、无矛盾）："Day one is already sold out"、"more than 80% of schools"。

## 已核实无缺陷的项目

- **弯引号**：text.md “ 81 / ” 81 成对，0 处贴 CJK，0 个 ‘/’；8 页 SVG “ 82 / ” 82 成对，0 处贴 CJK（多出的一对是 Rousseau 图注 "Surprised!"，SVG 有、text.md 无）；CJK 孤儿标点行首扫查 **0 命中**（text.md 与 SVG 文本元均 0；24 个以 — 开头的 SVG 文本元均为有意的破折号开头——"—— From page N of this issue." 归属行、"— he painted…" 续行、P2 匹配分隔符——非孤儿标点）。
- **禁词 / 残留简体中文**：中期选举/众议院/民主党赢下/参议院/星期五/金句/范文/桥接/占位/FIXME/Lorem/已确认/宣布/宣佈 在 text.md 与 SVG 文本中 **0 命中**；TODO 在 SVG 文本中 0 命中（朴素子串计数在 p3-culture.svg 有 1 命中，实为 base64 图片数据内的偶然子串，非文本内容）；日语用 発表 8×。
- **印/网文字层**：`-layout` 提取两版全文逐字节相同（各 101,065 字符）；词多重集差 **0**；逐页字节一致 **8/8**。工作区 scratch 重渲染网 PDF：SHA 不同（`1d86b217…` vs 已发 `fb903b2b…`，符合铁律——fontTools 子集 head.modified 墙钟 + cairo CreationDate；文件 2,883,892 B vs 已发 2,883,888 B），文字层与已发网/印两版均差 **0**；已发网 PDF 未动（SHA 仍为 `fb903b2b…`）。
- **家具**：masthead "The Lucerna"、"英語週刊 VOL.4"、"WEEK OF NOVEMBER 16 TO 22, 2026"、8 页页脚 "The Lucerna　英語週刊 VOL.4　本文は英語　解説は日本語" + "{n} ページ（全8 ページ）"、徽章 "英語テキスト　日本語の解説 — 日本語読者のための版" 全部齐全一致。Readers' Corner 正确说明无来信、示例信标为编辑所写，无虚构读者来信。
- **MODEL 散文**：82 词，在 80–100 要求内。P8 最小字号 SVG 13.5 pt；PDF 最小 span 10.12 pt（≥ 10 pt 下限，印/网一致）。
- **盒标题**：源 sweep 12/12 全过；SVG sweep 18/18 全过，0 溢出。最紧为 THE WEEK IN NUMBERS，advance +1.5 / 真墨 +1.5。
- **creambox**：inside-only 全版扫 0 真溢出；每页最差盒内余量 P1 +12.0、P2 +5.0、P3–P7 +47.7、P8 +92.4。全部 −35.5/−36/−37 负值均为 +45 px 窗口抓到的盒下节头伪影（core-en 同盒同值佐证）。P2 AND YOU? 盒 desc-clear −1.0 为假名行 heuristic 伪报（末行 "ださい。" 无拉丁下行字母；core-en 同盒同 heuristic 为 −1.5；P2 渲染目视确认末行完整在奶油盒内）。
- **"next Sunday" 冻结规则**：core-en 源码、en-ja 源码/registry/SVG、text.md 中 "next Sunday"（大小写不敏感）全部 **0 命中**——无适用对象，规则不适用。
- **残留措辞**："Ashes begin" / "second week in Perth" / "Perth is winning" / "Ashes will begin" 在 SVG + text.md + registry 中均为 0 命中；"Arsenal are winning" 1×、"June 2027" 2× 在位。
- **读者面扫查**：SOP / proofread / cover / TODO（文本）/ FIXME / Lorem / 占位 在 text.md 中 0 命中；"VOL.5予告" 1× 为 NEXT WEEK 栏头本身（正文内容，SVG 同 1×）。

## 紧但通过（实测在内，不修）

- **THE WEEK IN NUMBERS 标题**（P1）：403.0 px，advance 余量 **+1.5**，PIL 真墨余量 **+1.5**——确实紧，但真墨在内，无修复。
- **P2 AND YOU? 盒**：末行 "ださい。" 基线余量 +5.0；0.30×size 拉丁下行 heuristic 得 desc-clear −1.0——该行是假名，无拉丁下行字母，heuristic 不适用；core-en 同盒同 heuristic 为 −1.5（中文末行），同为 heuristic 伪报；P2 渲染目视确认末行完整在奶油盒内。

## 观察项（非本版缺陷）

- **P4 "B SENTENCES" 节头孤悬**：节头在栏 2 底部、题目 Q52–55 在栏 3 顶部——core-en 结构相同（继承的核心版式特征，与 proof1 观察项一致）。
- **keycheck 149/150 唯一不符 Q150**：抽取截断 + p8.py FOOTER_RE 已知工具 bug（混合大小写页脚漏进第 150 键），与 proof1/delta 相同，非版面缺陷。本轮 keycheck_ed.py 的 rc=0（脚本本身不以 mismatch 退出），结果与 proof1 一致。
- **p8 extract 不是 150/150**：工具对本版返回 **60/150 noted**（P8 版式下仅 60 个键带印刷注记）；有意义的门是与 core-en 抽取集完全相同——该门通过（CLEAN，keydiff=[137, 138, 139, 140, 150] 为预期的 4 个读者语翻译键 + 写作键）。不得谎称 150/150。
- **D5 字体数量（只记录，不判）**：SVG font-family 统计：Newsreader 1037、Noto Sans CJK JP 633、Noto Serif CJK JP 55、DejaVu Sans 4、UnifrakturMaguntia 1，共 5 种（与 proof1/delta 计数完全一致）。
- **text.md 缺 7 处图注**（Capitol、Audubon 火鸡、Rousseau "Surprised!"、W. G. Grace、Lawrence 姐弟、投票亭、Samuel Johnson）——core-en 的 text.md 同样缺这 7 处，属导出的既定行为，非本版缺陷（与 proof1 相同）。

## 复校方法

delta 记录 + proof1 记录通读；三 SHA 复核前后各测一次；registry/text.md/SVG 与 delta pre 备份逐项 diff；Q73 四源实测；run.py 与 freeze 在工作区 scratch 副本里重跑；registry/text.md 自源重建比对；机械门全跑（见 GATE-LOG.md）；核心对照 core-en（freeze 8/8、p8 抽取集相同、creambox 对照相同）；text.md 全文通读 + 150 题逐题手验；8 页印刷卡片全部目视（含 P8 答案区放大、P5 Q73 放大）+ 网页 PDF P1/P8 渲染目视。
**未做**：未改任何源文件、未重建生产文件、未 commit、未 push、未动 tools/、未动核心与其他版。

## 缺陷汇总

**零缺陷。结论：(a) 定稿。确认 en-ja 可定稿。**
