# PROOF-NOTE — 2026-W47 en-zh-tw 独立复校 proof1（en re-fanout #2 重建版，2026-11-11）

- 版：`production/2026-w47/2026-w47-en-zh-tw/`，印刷 `The-Lucerna-VOL4-en-zh-tw.pdf`（38,152,350 B，SHA-256 `7641031186c77653ac1263056a968ba7ce2ffb9383716c5a35cfad798e0fc334`）、网页 `The-Lucerna-VOL4-en-zh-tw.web.pdf`（2,965,191 B，SHA-256 `e07e5dd048dad9ab1ed42daa6d33c2e9f0dea129538b957c06afe25627e0d177`）、`2026-w47-en-zh-tw.text.md`（51,147 B，SHA-256 `57cb886738e8e23d79abe531e1f03ee7372560c5020ff02d4d6997ea117651b3`）。三者与任务书逐字节一致；两 PDF 各 8 页，1462.5 × 2025 pt。
- 复校员：独立 proof1（重建版），与建版者/fan-out 不是同一人。只复校，未改任何生产文件、未重建生产件、未 commit、未 push、未动 tools/、未碰 core-en。中间件全在 `hidden_files/w47/scratch-proof-en-zh-tw/`（`TMPDIR=<scratch>/tmp`），未写 /tmp；网 PDF 未重渲（只从交付件本身渲染 PNG 目视）。
- 探针：`ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）；scratch 真实写文件成功。

## 结论：(b) 有缺陷，不可定稿

共 **1 项**（轻微），在 ABSTRACT.txt，不在印版/网版正文。proof1（旧版）的 9 项缺陷已全部关闭（见“已关闭”）。

## 缺陷清单

### D1（轻微，本版级）— ABSTRACT.txt 含简体字“宣布”×1，与本版“宣佈”惯例冲突

- 定位：`ABSTRACT.txt` 第 1 行（全文唯一一行）：“11月3日週二美國期中選舉**已宣布結果**——……”。
- 实测（repo venv Python，`OpenCC('s2t')`，与任务书指定方法一致）：
  - `ABSTRACT.txt`：206 字符，s2t diffs **1**：`(38, '布', '佈')`，即“宣布”→“宣佈”。
  - 对照：`registry.json` 0 diffs；`2026-w47-en-zh-tw.text.md` 0 diffs；8 个 SVG 可见文本全部 0 diffs。
  - 全版 grep：`宣布` 仅此 1 处（除 KIT 自述文字外）；`宣佈` 在 text.md ×13、registry ×9、SVG ×9、`宣布` 在三者均为 0。
- 为什么算缺陷（按本版自己的标准，不是按台湾通用习惯）：
  - 本版 KIT §5 item 4 自述：6 处新“已宣布”在本轮自查中被发现并已逐一改成“宣佈”，“Re-check after the rebuild: registry.json, text.md and all 8 SVGs convert to themselves with 0 differences；宣佈 13× in text.md, 9× in registry.json；**宣布 0× anywhere**”。但 ABSTRACT 不在那次自查范围内（§3 script gate 只列 registry + text.md + 8 SVG），其“已宣布結果”漏网——KIT 的“0× anywhere”断言对交付件全集不成立。
  - 同一词在同一交付件集里两种写法（宣佈 31 处 vs 宣布 1 处），内部不一致；且 proof1（旧版）时 ABSTRACT.txt 的 OpenCC 自查是 0 diffs，本轮重写为全文形式后 regress 到 1。
  - 本轮任务书明令“简体泄漏重验残留 0”；按任务书指定的 OpenCC s2t 方法，残留 = 1，不是 0。
  - 说明：布本身不是“严格意义的简体泄漏”（KIT §5 item 4 同款承认：宣布在繁体中也是标准写法）；缺陷的性质是**违反本版自定的 0-diff 门 + 内部不一致**，不是错字。严重度因此定为轻微。
- 修复：ABSTRACT.txt 一字之改——“已宣布結果”→“已宣佈結果”。不涉及 PDF/text.md（其 SHA 不变）；ABSTRACT 只在 insert 时读入 frontmatter，版面未入仓前改无任何连带成本。改后须重跑 OpenCC 自查（ABSTRACT 0 diffs）并复核 ABSTRACT SHA。
- 证据：`measure3.log`（`ABSTRACT.txt: len 206 s2t diffs 1 [(38, '布', '佈')]`）、`measure3b.log` 同；`GATE-LOG §1.12/§5.1`。

## 已关闭（proof1 旧版 9 项 → 本轮逐项复验全部关闭）

| 旧项 | 本轮复验 |
|---|---|
| D1（严重）Q39/Q40 键互换 | registry 39→a、40→d；text.md 39→a、40→d；P8 印出键 38→b、39→a、40→d、41→c；P3 SVG 释义顺序 a=mentor、b=tribute、c=campmate、d=arena——**四源一致**，关闭 |
| D2 P1 SEARCHES 盒末行漫出盒底 18.0 px | 盒内末基线 1244.0，盒底 1256.0，余 **+12.0**；裁图目视行在盒内，关闭 |
| D3 P2 DID YOU KNOW 末行漫出 12.7 px | 盒内末基线 1171.1，盒底 1185.4，余 **+14.3**；裁图目视行在盒内，关闭 |
| D4 “已確認”混淆 call/certified | Q7/Q82/Q83/Q84 注一律改“已宣佈”；Q90 “尚未確認”系核心原文直转（见观察 O1），关闭 |
| D5（严重）P4 Ashes 整版错一年 | 全版改写为 2025–26 回顾；全部事实逐项网上核实通过（见 GATE-LOG §8），关闭 |
| D6 P2 SENATE 框题漫出 25 px | 标题改为 “SENATE IN NUMBERS　參議院數字”，advance 余 +30.5、真墨 558..929 余 **+32.0**；裁图目视框内，关闭 |
| D7 P2 SAY IT 第 2 盒英文行横向漫出 | 中盒由 280 加宽至 380（x=560..940），英文行 574.0..926.1，左右余 +14.0/+13.9；裁图目视框内，关闭 |
| D8 P4 框题真墨出框 3 px | 标题改为 “SATURDAY, NOV 21　週六賽程”，advance 余 +79.9、真墨 1458..1785 余 **+77.0**；裁图目视框内，关闭 |
| D9 P7 NEXT WEEK 承诺无法兑现 | 改写为 “Thanksgiving in America. The Ashes: England's rematch waits until June 2027. More certified results of the midterm election. And your letters — the first real ones.”（条件式 + 下届灰燼盃 2027 年 6 月 18 日英格兰开打已核实），关闭 |

## 已核对无问题（要点）

- 150 题：编号 1–150 连续（registry 逐项核对）；每页题数 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；级别 A2 62 / B1 66 / B2 22；与 KIT 一致。除 ABSTRACT 一字外，答案键逐题核对题面、原文、图表、算术（254+162+19=435；254−218=36；P8 模型文 82 词）全部正确（5 组配对 P2 D 24–27、P3 C 38–41、P4 C 56–59、P5 C 74–77、P8 F 141–144 均按印版 SVG 节点顺序逐题手验）。
- 机械门全过：occlusion 审计 0 flags（自检通过）；p8 extract 60/150 noted，compare CLEAN（keydiff [137, 138, 139, 150] = 翻译题 + 開放題，预期内；140 因简繁同形而不列入 keydiff）；freeze baseline 8/8 byte-identical；freeze diff vs 核心：新增 CJK 775 字（与 KIT 一致），180 个不同字全数 s2t 自恒（繁体合法新增，全数追踪）；印/网文字层逐页 token-multiset diff 0/0（pdftotext 字符数各 42,852，与 KIT 一致）；keycheck registry vs text.md 0 不符；印版 P8 键 vs registry 149/150 仅 #150 短标例外（预期）；印版 P8 键 139 现与 registry 逐字一致（旧版空格断行差异已无）。
- zh-tw 特有：text.md 宣佈 ×13 / 宣布 ×0；registry 宣佈 ×9 / 宣布 ×0；SVG 宣佈 ×9 / 宣布 ×0；OpenCC s2t：registry + text.md + 8 SVG 全部 0 diffs。Q140 `打破沉默。`简繁同形，registry 与核心键逐字相同，不在 keydiff 内，非错误。ABSTRACT 全文形式（498 B、206 字符、单行、无 ASCII 双引号），内容点与本期一致——除 D1 一字外合格。
- 奶油框：32 盒逐盒实测，盒内末基线余 +4.5 至 +92.4 px（最紧为 P2 AND YOU? 盒 +4.5，末行中文、无降部，框内，裁图已目视）；45 px 带内行全部裁定为下块栏头（FP），无真墨溢出。
- 框题：全部奶油框题逐个 advance + 真墨实测——全部合框（最紧 P1 NUMBERS：advance 余 +1.5 px，真墨 1007..1407 余 +5.0 px，框内，裁图已目视）；无双语小标题漫出奶油框右缘，STRADDLE 裁定无适用项。
- §1.1：字体 Newsreader 1025、Noto Sans CJK TC 619、Noto Serif CJK TC 48、UnifrakturMaguntia 1（刊头）、DejaVu Sans 4（符号），合规；用色集合与 core-en **完全一致**（fill/stroke 集合逐项比对，edition-only 与 core-only 均为空）；家具分隔符 U+3000 141（核心 132，+9 为繁体家具多用全角空格）；· 计数 282 与核心完全一致；VOL.4 ×12、VOL.5 ×8、VOL.3 ×3，与核心一致。
- P8 最小字号 10.12 pt ≥ 任务书 10 pt 下限（亦 ≥ §1.1 的 9.75 pt），通过。
- 金句：P7 8 句全部逐字出自本期正文，页码标注正确（含嵌套引号句 “A ‘call’ is not the official result.”，正文逐字核对无误）。
- 引号：弯引号 “ 82 / ” 82 成对；U+2019 0；弯引号全在 Newsreader（拉丁）节点，CJK 字运行 0；唯一斜体对是 P1 每周一词 “midterm”（Newsreader 斜体，§1.1 本周词斜体）；P7 无斜体引号。SVG 比 text.md 多一对是 P3 图注 “Surprised!”（text.md 按惯例跳过图注）。
- 8 页目视：印版 8 页逐页看图 + 网版 P1/P8 看图，无溢出、重叠、压页脚、图片与出处问题；网版与印版视觉一致。
- 外部事实：Ashes 回顾逐项核实（珀斯首战 2025-11-21–22、8 wicket、两天、847 球自 1888 年最短；系列 2025-11-21–2026-01-08、4–1；墨尔本英格兰 4 wicket 两天取胜、近十五年首胜；悉尼澳大利亚 5 wicket；Cummins 背伤、Hazlewood 腿筋伤、Smith 代队长、Boland、Doggett 首秀；2024 年珀斯印度 295 分胜；珀斯不在 2021–22 巡回赛；下届 2027 年 6 月 18 日英格兰开打）；其余本期事实与 proof1 已核实集一致（内容未改）。

## 观察（非缺陷）

- O1 — Q90 注“兩個參議院選區尚未確認：阿拉斯加與密西西比”仍用“確認”。该注是 core-en 原文直转（简繁同形），核心本轮修 D4 时有意未动 90（只改了 7/82/83/84）；且此处说的是未定选区“尚未确认”，不构成把 call 说成 certified 的 D4 式误述。记观察，不算缺陷。
- O2 — KIT §5 “registry keys vs core 145/150（diff only the 5 reader-language keys 137–140, 150）”与实测不符：实测差异仅 [137, 138, 139, 150]（146/150 相同），140 因简繁同形与核心键逐字相同。KIT 口径问题，非本版缺陷；p8 compare 的 keydiff [137, 138, 139, 150] 与此一致。
- O3 — KIT §3 “P8 min font 13.5 pt”写的是 SVG 属性 px 数而非渲染 pt；实测印版 P8 最小 10.12 pt（答案键块在 0.75 缩放组内），仍 ≥ 任务书 10 pt 下限；仅 KIT 口径问题，非本版缺陷（与 proof1 O3 同款）。
- O4 — P1 NUMBERS 框题极紧：advance 余 +1.5 px，真墨余 +5.0 px，框内，裁图目视未碰线。
- O5 — P2 AND YOU? 盒盒内余 +4.5 px，末行中文、无降部，框内，裁图已目视。
- O6 — P2 A 组说明“根據日期與時間”偏宽（本周 5 题全是日期、无钟点题），系核心模板通用措辞，非本版新错（与 proof1 O5 同款）。
- O7 — P5 D 节栏头落在第 2 栏底部、其 78–81 题在第 3 栏顶部：按三栏自上而下、自左至右的阅读流，栏头在先、题在后，顺序正确，只是视觉上跨栏分离；属版式流常态，非缺陷。
- O8 — D5 字体问题：按任务书只记录、不判 (b)。本轮未发现字体问题（字体清单与核心一致，无缺字/错体迹象）。

## 未独立再核实（低风险、已列出）

- Mike Johnson“不竞选新一届众议院共和党领袖”原话出处、众院两党领袖选举日期（11 月 10 日/11 月 18–19 日）；“How to Survive the Jungle”一次特别节目 11 月 15 日；ATP 决赛“不早于 18:00”；W. G. Grace 照片“late 1880s”与 Samuel Johnson 肖像“1772”；Lawrence 儿童照片日期 1912 年 2 月 19 日（罢工背景已核实：1912 年 1–3 月 Lawrence 纺织罢工、儿童 2 月送往纽约，照片本身的 LOC 编目日期未直接查到）；选举场景本身为本期工作假设（AP 口径数字与 proof1 已核实集一致）。

## 建议下一步

1. ABSTRACT.txt 一字改“已宣布結果”→“已宣佈結果”（本版级，零连带成本；PDF/text.md SHA 不变）。
2. 改后重跑 OpenCC s2t 自查（registry + text.md + ABSTRACT.txt + 8 SVG 全 0 diffs），复核 ABSTRACT 新 SHA，记入 KIT §5 item 4 的“宣布 0× anywhere”使之属实。
3. 其余无需重出：本轮 1 项缺陷只在 ABSTRACT，不触及版面；改后无需整版重渲染、无需 proof 全轮重做（仅 ABSTRACT 自查 + 本轮结论更新）。
