# W47 ja 家庭独立校对记录（PROOF-NOTE）

- **校对员**：独立校对（未参与建造，全新全量通读；SOP §8.4 重校）
- **日期**：2026-11-12
- **范围**：目标语 ja，11 版（读者母语 en de fr es it pt nl ru ko zh-cn zh-tw；core-ja = ja-zh-cn）
- **结论**：**(b) 有问题** —— 2 条缺陷（D1：11 版全有；D2：仅 ja-ko），另 5 条观察项。只记录，不修复。
- **硬约束遵守**：只在 `production/2026-w47/` 与 `hidden_files/w47/` 读/写；未 reset/stash/add/commit/push，未跑 lint，未重渲染（只用生产目录已有的 PNG/PDF；目检用 PyMuPDF 由印 PDF 现场栅格化，未写回生产目录）。磁盘开工 93G、收尾 93G（<100G 门限）。

## 1. 校对文件指纹（校对的那份文件）

每版 8 页，1462.5 × 2025 pt。印 PDF / 网 PDF / text.md 的字节数与 SHA-256 前 12 位（2026-11-12 实测；收尾重哈希 11 份印 PDF，SHA 与下表完全一致，校对期间生产文件未变）。

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-ja（zh-cn） | 25,973,499 / `e5b8a65dcf65` | 4,654,724 / `a1f1a21c267f` | 44,432 / `bcfa667da57e` |
| ja-en | 25,806,203 / `a063fff2f05e` | 4,379,969 / `9c9e2fd0d832` | 45,706 / `8374230f772c` |
| ja-de | 25,813,853 / `9c3d99f1cbb5` | 4,387,409 / `c9934cc55414` | 46,520 / `6323cd14109c` |
| ja-fr | 25,812,294 / `a49a45bc7ec7` | 4,386,310 / `261f69ffc4ec` | 46,882 / `420616e6b601` |
| ja-es | 25,813,996 / `429f2dd366ba` | 4,387,628 / `26fc381b5322` | 46,684 / `81993361c31f` |
| ja-it | 25,807,650 / `4e4788733790` | 4,381,274 / `0a97c94a09c2` | 46,678 / `71a2d7d21e57` |
| ja-pt | 25,814,744 / `ea1bf3b8aa5f` | 4,388,483 / `15614590c526` | 46,696 / `53bc548ba01c` |
| ja-nl | 25,805,475 / `dc2140959c3c` | 4,379,017 / `e17fb93ba898` | 45,627 / `f823709e214d` |
| ja-ru | 25,970,245 / `2ab6a7d2d740` | 4,540,692 / `f70444a63e48` | 53,004 / `88e3680b5d31` |
| ja-ko | 28,140,833 / `30fdf1f67dca` | 4,551,758 / `82c1c7c69a41` | 47,722 / `b20d5bc686ff` |
| ja-zh-tw | 25,988,408 / `d080e8981720` | 4,789,284 / `b8f3fdad5208` | 44,361 / `8c18a0e9fb47` |

盘点：11 版齐全（10 个 fan-out 目录 + core-ja），无缺失、无多余、无重复的 ja-zh-cn fan-out 目录。`production/2026-w47/` 共 133 项 = 119 fan-out + 12 core + `fanout-nl`、`fanout-zh-tw` 两个非版目录。

## 2. 缺陷

### D1 —— “ryuuryuu”拼写错误（11 版全有）

- **错误**：りくりゅう（三浦璃来 Riku + 木原龍一 Ryuu，简称“りくりゅう”）的正确罗马字是 **rikuryuu**；正文误作 **ryuuryuu**（丢了 riku、重复了 ryuu）。
- **位置（每版 5 处）**：P7 本周金句 gloss 行 1 处 + P8 答案 66、77、80、105 各 1 处。
- **证据**：
- 11 版 text.md grep 均为 `ryuuryuu ×5`，`rikuryuu` 0 处。
- 已证实在印制 SVG 与印 PDF 中：core-ja P7 `ryuuryuu` 位于 y=1550.2（Newsreader run）；ja-ko P7 位于 (741.8, 1475.9)，P8 4 处（(440.1,1636.6)、(437.9,1877.7)、(790.2,1042.5)、(783.2,1648.2)）；de 版 P8 答案 77 原文 “77. × — ryuuryuu ist kein Filmtitel”。
- 日文核心层本身正确写『りくりゅう』，错只在讲解层/答案注的罗马字。
- **严重度**：轻微（讲解层拼写错误，不影响答案判定与事实），但属可验证的正字法错误，11 版同错。

### D2 —— ja-ko “우미노우미”读音错误（仅 ja-ko）

- **错误**：力士名 美ノ海 的正确读音是 **ちゅらのうみ**（Chura-no-umi），ja-ko P8 答案 48 的注释误作 **우미노우미**（Umi-no-umi）。
- **位置**：ja-ko text.md 第 1246 行：`48. B — 우미노우미는 1일째에 호쇼류에게 졌어요`；印制 SVG `p8-tesuto.svg` y=1635.08（13.3pt run）；印 PDF P8 (439.1, 1214.8)，已放大目检确认印出。
- **证据**：
- 琉球新報（2026-10-26）与日刊スポーツ（2018 年）均确认读音为 ちゅらのうみ。
- 同一家 ja-ru 已有意修正同一错误（Чура-но-уми 1× 在、Уми-но-уми 0；旧形于 text.md/SVG/py 全为 0）；其余版拼写均正确：en `Churanōmi`、de `Churanoumi`、fr/es/it/pt/nl `Chura-no-umi`；zh-cn/zh-tw 用汉字『美之海』（与『义之富士』同例的汉字转写，非读音主张，无问题）。
- ja-ko 全版仅此 1 处（“미노우미 1×”为子串计数 artifact，实为 우미노우미 的一部分）；题干用汉字『美ノ海』，不受影响。
- **严重度**：轻微（1 处答案注单词，专名读音错误；与 ja-ru 已修的错误同类）。

## 3. 观察项（非缺陷）

- **O1 嵐山紅葉見頃 23 日 / 26 日双日期**：正文用 Weathernews 第 3 回予想（10 月 29 日）“見頃 11 月 23 日”；同出版社嵐山 spot 页 11 月 8 日更新为“見頃 11 月 26 日ごろ”。正文未说明是预报版本差。练习只用 23 日作見頃、12 月 12 日作落葉はじめ，无内在矛盾，不影响答案。
- **O2 读者来信 gloss 多一句邀稿**：en 版 P7 来信 gloss 比核心多一句 “Send us your letter in Japanese — selected letters will be printed in VOL.5!”；zh-tw 版同位置多一句“請把你的日語來信寄來！”。与本期各处邀稿一致，不算缺陷。
- **O3 core-ja `_D5_READER="latin"`**：core-ja/en/de/fr/es/it/pt/nl 为 `"latin"`，ja-ru 为 `"ru"`，ja-ko/ja-zh-tw 为 `"cjk"`。按 `apply_variant.py` 注释，latin/cjk 路由相同（仅 `"ru"` 分支不同），core-ja 的 `"latin"` 只是标签差异，无功能影响。
- **O4 记录 SHA 滞后于 D5 重建**：10 个 fan-out 的 `EDITION-RECORD.md` 所记印/网 PDF 尺寸与 SHA 均与现盘不符（例：en 记印 PDF 27,440,477 字节 / `c29f6f98…`，现盘 25,806,203 / `a063fff2f05e`）；core-ja 的 `ja-gates.log`（2026-11-10/11，D5 重建前）亦然（旧印 SHA `20b9d504…` vs 现盘 `e5b8a65d…`）。记录滞后，内容本身不受影响。
- **O5 目检工具链插曲**：`/tmp`（512MB tmpfs）校对中途被多家校对的渲染件占满至 100%，且 `pdftoppm` 在 3 版上 segfault；已改用 PyMuPDF 在 scratch 目录重渲 88 页（0.55×，8.9MB），不影响结论。已删 `/tmp/ja_proof/sheets/` 旧件。

## 4. 已通过的检查（证据摘要）

| 检查 | 结果 |
|---|---|
| D5 普查（`d5_census.py`，11 版） | 全部 `CENSUS PASS`：拉丁在 CJK sans 0、西里尔在 CJK 0、弯引号在 CJK 0；`curly_total=0`（11 版均无弯引号）；ja-ru `noto_sans_elements=712`（ru 读者 Noto Sans 路径真实触发） |
| svglib 结构 | 11 版均有新式 `_char_font`（7 处）+ fix2（7 处）+ kinsoku（10 处）；SVG 字体族全为 Noto Serif/Sans CJK **JP** |
| `p8.py compare`（core P8 vs 10 版，`--total 150`） | 全部 **CLEAN**，150/150；keydiff [137,138,139,140]（zh-tw [139,140]，137/138 与核心逐字节同）——预期的读者语翻译题键 |
| `occlusion_audit.py`（11 版 svg 目录） | 全部 **0 flags**，自检 OK |
| 奶油框绝对审计（`d5_creambox_audit.py` `abs_flags`） | 11 版均为 0 flags；P8 墨水底边 2517.9–2536.0，距页脚规则线 y=2596 余量 60–78px，无压页脚 |
| 禁则 kinsoku（v3，PIL 真实墨水宽度分组） | 11 版均为 **0 hits**（v2 因行分组 bug 的 20–27 条/版误报已废弃；假阳性如 P1 caption“（6面）”、P8“（___）”经 v3 证实为同一视觉行内的分 run） |
| 题号连续性（11 版 text.md 程序化检查） | Q 1–150 与 A 1–150 均齐全、无缺无重 |
| P8 最小字号（PyMuPDF 实测印 PDF 第 8 页） | 11 版均为 **9.98pt** ≥ SOP §1.1 底线 9.75pt |
| 印/网文字层（`pdftotext`） | 11 版字节数与内容全部 **IDENTICAL** |
| 数字一致性（core vs 各版 diff，150 hunks/版） | 不匹配 hunks：拉丁/西里尔版 8 处、ko 7 处、zh-tw 1 处，逐条核对均为合理解释（“二十四節気”→24、“11月”→November、“第N面”→Page N 等）；实质数字全对：P6 图表 38+24+22+16=100，Q91 差 14、Q92 和 62、Q93 合计 100；19/22/23/40/30/2/12 均一致 |
| 范文 154 字（Q150） | core 范文精确 **154 字**（去空白计数），Q150 “✓ 范文见本版 H 区（154 字）”属实；✓ 在 11 版 text.md 各 2 处、P8 SVG 各 1 处，均印出 |
| F 141–144 题干+键 | 141 熊手 c、142 解禁 a、143 金星 d、144 見頃 b，释义与原文一致；Q147 “见第 2 版”页码引用正确 |
| 事实/日期/星期（2026-11-12 当天网页核验） | 11-16 周一 … 11-22 周日；11-03 周二、11-05 周四、11-07 周六、12-01 周二；相扑九州场所初日~3 日目赛果（大の里负義ノ富士、豊昇龍负藤凌駕获金星、两横纲 2 胜 1 负、“3 场所连续休场明け”）全部属实；流行语大赏 11 月 5 日提名 30 语（含 りくりゅう、ちいかわ、酷暑日、AI暴走、NISA貧乏、ボンボンドロップシール、好きすぎて滅！），Top 10 于 12 月 1 日公布；Weathernews 红叶予想（高尾山 11 月 13 日、嵐山 11 月 23 日、宮島 11 月 21 日）与正文一致；阪神梅田本店约 40 种新酒（PR Times 2026-11-04 原文“約40種類”）；酉の市 2026 一の酉 11 月 7 日（周六）、二の酉 11 月 19 日（周四），熊手店约 150、露店约 750（鷲神社官网）；花園神社 Mozzucu 照片日期 2025 年 11 月 24 日 = 2025 年二の酉，图注正确 |
| 禁用字符 | 11 版 SVG+text.md 均无中点 `·`、无旧纸色 `#f7f1e2`、无 U+2019/U+201C |
| P1 刊头 + 配对徽章、页脚配对标注、摘要 | 11 版 P1 页脚均完整正确（en “Japanese text English explanations”、de “Japanischer Text Deutsche Erklärungen”、ru “Текст на японском Объяснения на русском”、ko “텍스트는 일본어 해설은 한국어”、zh-tw “正文日語 講解繁體中文”等）；ABSTRACT.txt 11 版均有、读者母语、单行、无 ASCII 双引号，含刊名、目标语名、A2–B2、150 题与真实主题 |
| core-ja text.md 全文通读（1356 行） | 文章、练习、P8 答案逐题核对过；P7 本周金句 8 条逐字核对与正文一致、页码引用正确 |
| ja-en diff 全文通读（1037 行） | 翻译正确（唯一注意点见 O2） |
| 目检 88 页 | 11 张 2×4 总览图逐版看过 + 放大细看（ko P8 우미노우미行、core P8 上部 Q114–132、core P1 内容页码列表）：无溢出/重叠/压页脚/豆腐块/截断句；P6 图表条形正常；P7 底部照片条、P8 寺院图均在位 |

## 5. tools/ 状态与重跑

- 开工时 tools/ git HEAD：`71f4e6f9df302d5322211cdd01437a9ac0f4fec7`，工作树脏（M `tools/README.md`、`tools/cover.mjs`、`tools/occlusion_audit.py`、`tools/p8.py`、`tools/run_build.README.md`、`tools/run_build.py`；?? `tools/d5_creambox_audit.py`、`tools/head_check.py`）。
- 校对中途上述改动被提交为 `b9ac29a6`（“tools: D5 gates + p8/occlusion/cover/run_build fixes (W47 review round)”），tools/ 现为干净状态。按任务要求，收尾用**已提交的 tools**重跑了受影响的三项检查：`p8.py compare`（10 版全 CLEAN）、`occlusion_audit.py`（11 版 0 flags）、奶油框 `abs_flags`（11 版 0 flags，P8 墨水底边/余量同前）——**结果与提交前完全一致**。
- D5 普查与 kinsoku v3 不依赖 tools/（分别为 hidden_files 脚本与自写脚本），无需重跑。

## 6. 备注

- ja-ru 两处有意修改已核实正确：Фудзирёг 5× 在、Фудзирюг 0；Чура-но-уми 1× 在、Уми-но-уми 0；旧形（единственно правильного / Прогноз Японии / Оканчивайте / 一之富士）于 text.md/SVG/py 全为 0。
- ja-ko 为 D5 版（10:22 同步），非漏版；其 `_D5_READER="cjk"`、JP 索引字体族与 kinsoku 均与裁定一致。
- 本记录只校对、不修复。D1 须 11 版同修、D2 须 ja-ko 单修，修后建议重跑 `p8.py compare` 与 occlusion 以确认无连带变化。
