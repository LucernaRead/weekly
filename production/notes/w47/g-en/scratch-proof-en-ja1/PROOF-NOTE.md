# PROOF-NOTE — 2026-W47 en-ja · proof1（独立复校，en re-fanout #2 重建版）

- **版**：2026-W47，英语目标语 × 日语读者版（en-ja），VOL.4，刊期 2026-11-16..22
- **复校员**：独立复校（与建版者/fan-out agent 不是同一人），SOP §8.4 proof1
- **复校日期**：2026-11-11
- **对象目录**：`production/2026-w47/2026-w47-en-ja/`
- **重建来源**：en re-fanout #2（`hidden_files/w47/scratch-fanout-en2/FANOUT-REPORT.md`）；核心 core-en 已定稿
- **结论：(a) 定稿零缺陷** —— 全部机械门通过，150 题逐题三源一致，8 页逐页目视干净；旧 proof1 的 D1–D6 与 fanout 轮新发现的两项标题溢出均已修复并实测验证；无新缺陷。

## 对象核对（SHA 全量匹配，复核前后各测一次）

| 文件 | 大小 | SHA-256 | 结果 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ja.pdf`（印刷） | 41,509,391 B | `9f9faaea18807551394977ef536d142da65cfda78b73aa91d807063c0c4b0428` | MATCH（复核前＝复核后） |
| `The-Lucerna-VOL4-en-ja.web.pdf`（网页） | 2,883,877 B | `25645767641d06f1bfdc25f9437eb5c7f3ce0c319612eaabc9e912353f756f49` | MATCH（复核前＝复核后） |
| `2026-w47-en-ja.text.md` | 53,588 B | `219ce22d549887f0ca6895a928206ac18b255686e8f50f07296c54cd33d48aa9` | MATCH（复核前＝复核后） |
| core-en 印（对照） | 41,407,278 B | `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566` | 复核前＝复核后，未变 |
| core-en 网（对照） | 2,804,271 B | `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8` | 复核前＝复核后，未变 |
| core-en text（对照） | 51,405 B | `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b` | 复核前＝复核后，未变 |

三者均与任务简报及 KIT §2 一致。两 PDF 各 8 页，页尺寸 1462.5 × 2025 pts。复校全程只读生产目录（freeze/web 重渲染只在工作区 scratch 副本里做；`git status` 仅显示两目录为未跟踪状态——fanout 轮未 commit 的既有状态，本轮未改动 repo 内任何文件）。

## 旧缺陷复验（旧 proof1 D1–D6，全部已修）

| 编号 | 旧缺陷 | 复验结果 |
|---|---|---|
| D1 MAJOR | P3 Q39/Q40 答案键互换（39 应为 a、40 应为 d） | **已修，四方一致**：P3 SVG 题干 a=teaches/guides（mentor）、b=chosen（tribute）、c=lives with（campmate）、d=place（arena），词 38 tribute / 39 mentor / 40 arena / 41 campmate；registry 38=b、39=a、40=d、41=c；text.md 39→a（mentor = 指導者 a）、40→d（arena = 競技場 d）；P8 抽取键 39=a、40=d；印刷 P8 答案行 "38. b · 39. a · 40. d · 41. c" |
| D2 | P2 DID YOU KNOW 末行溢出盒底 12.7 px | **已修**：盒底 1185.4，末行 "November 3." 基线 1171.1，**余量 +14.3**（core-en 同值）；P2 渲染目视确认行在奶油盒内 |
| D3 | P1 SEARCHES 注脚溢出盒底 18.0 px | **已修**：盒底 1256.0，注 "人気の目安で、正確な検索数ではありません。" 基线 1244.0，**余量 +12.0**（core-en 同值）；P1 渲染目视确认 |
| D4 | ABSTRACT 短式，缺 Lucerna / A2–B2 / 150 | **已修**：现为完整式 666 B，含 Lucerna、VOL.4、150、A2、B2（各 1× 核实），0 个 ASCII 双引号；内容覆盖 11 月 3 日选举発表结果、11 月 16 日反いじめ週間/奇抜な靴下の日、11 月 20 日世界子どもの日/ハンガー・ゲーム、11 月 21 日プレミアリーグ/ATP、アッシュズ 4–1 回顾 |
| D5 | P3 盒标题 "HAYMITCH'S GAMES　ヘイミッチの大会" 溢出盒右缘 26.9 px | **已修**：现为 "HAYMITCH'S GAMES　ヘイミッチ戦"，实测 385.4 px，**余量 +19.1**（advance 与 PIL 真墨一致）；P3 渲染目视确认标题在奶油盒内 |
| D6 | P5 D 节说明跨栏断裂（"と）。" 孤悬栏 3 顶） | **已修**：说明现为单行 "現在進行形で書きかえよう。"，节头 y=2497.45、说明基线 y=2543.95（页脚线 y=2596 之上 52 px）；栏 3 顶部为 Q78–80 本题，无孤字；P5 渲染目视确认 |

## 本版 carry-forward 专项复验（fanout #2 构建记录）

- **ja P5 ODD SOCKS 标题**：现为 "ODD SOCKS, IN NUMBERS　数字で"，源 sweep 380.9 px / **advance 余量 +23.6**；独立 PIL 真墨重测：真墨终点 487.0，**真墨余量 +23.5**（旧 −22.4 已消除）。P5 渲染目视确认。
- **ja P6 A PRACTICE BALLOT 标题**：现为 "A PRACTICE BALLOT　投票用紙"，源 sweep 338.9 px / **advance 余量 +65.6**；独立 PIL 真墨重测：真墨终点 895.5，**真墨余量 +65.5**（旧 −3.4 / 真墨 −3.5 实溢出已消除）。P6 渲染目视确认。
- **Q39→a / Q40→d**：见 D1 四方一致（SVG 题干/选项、registry 键、text.md 注记、P8 提取键）。
- **其余核心 fix1 carry-over**：Q46 新题干 "The 2025–26 Ashes began on... A. Friday, November 21, 2025, in Perth · B. Saturday, November 21, 2026, in Perth · C. Thursday, November 19, in Houston" → A ✓（正文：2025 年 11 月 21 日周五珀斯首战；`date -d` 核实 2025-11-21 = Friday，2026-11-21 = Saturday）；Q52 "Perth Stadium ___ its first Ashes Test in November 2025." → hosted ✓（正文原句）；Q55 "Australia ___ the first Test by eight wickets." → won ✓（正文 "won in two days, by eight wickets"）；Q125 "Australia won the 2025–26 Ashes by... A. 4–1 · B. 1–4 · C. 2–2" → A ✓（正文 "The final score was 4–1"）；Q7 "The Democrats won the House with... A. 218 · B. 254 · C. 162" → B ✓；Q82 "In the House, as called on November 8, the Democrats won... A. 218 · B. 254 · C. 162" → B ✓；Q83 "races still uncalled: A. 2 · B. 13 · C. 19" → C ✓；Q84 "In the Senate, races called: A. 33 of 35 · B. 20 of 35 · C. 35 of 35" → A ✓；Q47 Cummins 背伤 → C ✓；Q48 Smith 代主将 → B ✓；Q49 英格兰上次在澳赢系列赛 2010–11 → A ✓；Q50 Man City–Fulham 12:30 → C ✓；Q51 Sinner 膝伤 → B ✓。Ashes 残留措辞 "Ashes begin" / "second week in Perth" / "Perth is winning" / "Ashes will begin" 在 SVG + text.md + registry 中均为 0 命中；"Arsenal are winning" 1×、"June 2027" 2× 在位。P7 NEXT WEEK 已重写："Thanksgiving in America. The Ashes: England's rematch waits until June 2027. More certified results of the midterm election. And your letters — the first real ones." P1 strip "中間選挙 · 発表された結果 · 6ページ参照"；已確認 0 命中，発表 8×（日语表达，无中文残留）。
- **SAY IT**：三格 label/sub 全 fit（最小余量 +45.3，中间格 w=380）；panel 3 右缘 1340，glossary lx=1370，**间隙 30 px** 完好。

## 已核实无缺陷的项目

- **150 题答案键**：text.md 答案 1–150 对 registry.json 逐项一致（键、级别、题型；编号连续；**0 差异**）；registry 对 P8 抽取键 149/150（唯一不符 Q150 见观察项工具 bug）；每页 10/17/18/18/18/18/12/39；级别 A2 62 / B1 66 / B2 22。其余四组匹配题对印刷定义逐组语义核对无误：P2 Q24–27（24=b runoff、25=c certify、26=a turkey、27=d Thanksgiving）、P4 Q56–59（56=b Test、57=c tour、58=d injury、59=a break）、P5 Q74–77（74=d bullying、75=a speak up、76=b right、77=c silence）、P8 Q141–144（141=b call、142=c runoff、143=d certify、144=a midterm）。
- **外部事实**：旧 proof1 已逐项联网核实（选举数字、饥饿游戏、丛林节目、灰烬杯、反欺凌周、儿童日、ATP、英超、NFL）；本次重建只改了已核实的 Ashes 回顾表述与题键，未引入新事实主张；Q46 的 2025-11-21 周五已用 `date -d` 核实。未独立确认的两处微观说法（"Day one is already sold out"、"more than 80% of schools"）仍记为未证实、无矛盾（与旧 proof1 相同）。
- **弯引号**：text.md “ 81 / ” 81 成对，0 处贴 CJK，0 个 ‘/’；8 页 SVG “ 82 / ” 82 成对，0 处贴 CJK（多出的一对是 Rousseau 图注 "Surprised!"，SVG 有、text.md 无）；孤标点行首扫查 0 命中。
- **禁词 / 残留简体中文**：中期选举/众议院/民主党赢下/参议院/星期五/金句/范文/桥接/占位/TODO/FIXME/Lorem/已确认 在 text.md 中 0 命中；SVGs + registry 同上 0 命中；宣布/宣佈 0 命中（日语用 発表）。
- **印/网文字层**：词多重集相同（差 0），逐页字节一致 8/8（各 43,475 字符）；工作区 scratch 重渲染网 PDF：SHA 不同（符合铁律——fontTools 子集 head.modified 墙钟 + cairo CreationDate），文字层与已发网/印两版均差 0；已发网 PDF 未动（SHA 仍为 `25645767…`）。
- **家具**：masthead "The Lucerna"、"英語週刊 VOL.4"、"WEEK OF NOVEMBER 16 TO 22, 2026"、8 页页脚 "The Lucerna　英語週刊 VOL.4　本文は英語　解説は日本語" + "{n} ページ（全8 ページ）"、徽章 "英語テキスト　日本語の解説 — 日本語読者のための版" 全部齐全一致。Readers' Corner 正确说明无来信、示例信标为编辑所写，无虚构读者来信。P7 金句 8 条页码标注与旧 proof1 核实结果一致（P2、P1、P4、P6、P6、P3、P5、P1）。
- **MODEL 散文**：82 词，在 80–100 要求内。P8 最小字号 SVG 13.5 pt；PDF 最小 span 10.12 pt（≥ 9.75 下限，印/网一致）。
- **星期**：沿用旧 proof1 的 `date -d` 核对（Nov 3 周二、Nov 8 周日、Nov 9 周一、Nov 10 周二、Nov 15 周日、Nov 16 周一、Nov 18 周三、Nov 19 周四、Nov 20 周五、Nov 21 周六、Nov 22 周日、Nov 26 周四感恩节、Nov 27 周五、Dec 1 周二）；本次新增核实 2025-11-21 周五（Q46 选项 A）与印刷一致。
- **P7 工具盒**：7 盒 inside-only 最小余量 +47.7，desc-clear 最小 +41.6，干净。
- **盒标题**：源 sweep 12/12 全过；SVG sweep 18/18 全过，0 溢出。最紧为 THE WEEK IN NUMBERS，advance +1.5 / 真墨 +1.5（实测，见下）。
- **creambox**：inside-only 全版扫 0 真溢出；每页最差盒内余量 P1 +12.0、P2 +5.0、P3 +47.7、P4 +47.7、P5 +47.7、P6 +47.7、P7 +47.7、P8 +92.4。全部 −35.5/−36/−37 负值均为 +45 px 窗口抓到的盒下节头伪影（core-en 同盒同值佐证）。
- **读者面扫查**：SOP / proofread / cover / TODO / FIXME / Lorem / 占位 在 text.md 中 0 命中；"VOL.5予告" 1× 为 NEXT WEEK 栏头本身（正文内容，SVG 同 1×）。
- **"next Sunday" 冻结规则**：core-en 源码、en-ja 源码/registry/SVG、`tools/tables.py`、text.md 中 "next Sunday"（大小写不敏感）全部 **0 命中**——无适用对象，规则不适用，未硬套旧行号。
- **旧版逐页对比**（备份旧版 print PDF 像素对比，100 dpi）：P1 0.98%、P2 0.82%、P3 0.02%、P4 11.48%（Ashes 全文重写，预期内）、P5 0.87%、P6 0.05%、P7 2.90%（NEXT WEEK 重写）、P8 0.65%——差异分布与已知修复一一对应，无意外改动。印/网像素差集中在 P1 国会大厦照片与 P8 图书馆全景照片区，双版裁切目视内容同一（网版照片下采样所致，非内容差）。

## 紧但通过（实测在内，不修）

- **THE WEEK IN NUMBERS 标题**（P1）：403.0 px，advance 余量 **+1.5**，PIL 真墨余量 **+1.5**——确实紧，但真墨在内，无修复。
- **P2 AND YOU? 盒**：末行 "ださい。" 基线余量 +5.0；0.30×size 拉丁下行 heuristic 得 desc-clear −1.0——该行是假名，无拉丁下行字母，heuristic 不适用；core-en 同盒同 heuristic 为 −1.5（中文末行），同为 heuristic 伪报；P2 渲染目视确认末行完整在奶油盒内。

## 观察项（非本版缺陷）

- **P4 "B SENTENCES" 节头孤悬**：节头在栏 2 底部，题目 Q52–55 在栏 3 顶部——core-en 结构相同（继承的核心版式特征，与旧 proof1 观察项一致）。
- **keycheck 149/150 唯一不符 Q150**：抽取截断 + p8.py FOOTER_RE 已知工具 bug（混合大小写页脚漏进第 150 键），keycheck rc=1 仅因此；版面内容无误（text.md 与 registry 的 Q150 键一致）。
- **p8 extract 不是 150/150**：工具对本版返回 **60/150 noted**（P8 版式下仅 60 个键带印刷注记）；有意义的门是与 core-en 抽取集完全相同——该门通过（CLEAN，keydiff=[137, 138, 139, 140, 150] 为预期的 4 个读者语翻译键 + 写作键）。不得谎称 150/150。
- **D5 字体数量（只记录，不判）**：SVG font-family 统计：Newsreader 1037、Noto Sans CJK JP 633、Noto Serif CJK JP 55、DejaVu Sans 4、UnifrakturMaguntia 1，共 5 种。
- **fanout freeze.log 的标签说明**：fanout 轮各语的 freeze.log 所印 "core" 哈希互不相同，且 ja 的 freeze-final/build-copy 与已发 ja 版 SVG 字节一致（`bdd374b7…`）——其实是各版自重建的自洽校验，不是核心冻结；本次独立重跑了真正的核心冻结（`--build core-en --core-svg core-en/svg`，8/8 字节一致），且 freeze-diff 数值与 fanout 轮逐页一致（TOTAL 2,084），故不影响结论。见 GATE-LOG 诚实说明。
- **text.md 缺 7 处图注**（Capitol、Audubon 火鸡、Rousseau "Surprised!"、W. G. Grace、Lawrence 姐弟、投票亭、Samuel Johnson）——core-en 的 text.md 同样缺这 7 处，属导出的既定行为，非本版缺陷（与旧 proof1 相同）。

## 复校方法

全文通读 text.md；150 题逐题三源核对（registry / text.md / P8 抽取）+ 改动题语义核对 + 四组匹配题对印刷定义核对；8 页印刷卡片全部目视 + 网页 PDF P1/P8 渲染目视 + P1/P8 印网差异区裁切目视；机械门全跑（见 GATE-LOG.md）；核心对照 core-en（freeze 8/8、p8 抽取集相同、creambox 对照相同、SHA 复核前后不变）；旧版逐页像素对比。
**未做**：未改任何源文件、未重建生产文件、未 commit、未 push、未动 tools/。旧 proof1 目录原样保留在 `old-proof1-pre-rebuild/` 子目录内。
