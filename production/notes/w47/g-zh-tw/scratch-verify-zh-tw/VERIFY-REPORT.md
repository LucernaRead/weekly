# W47 zh-tw 家 §8.4 状态核对报告（VERIFY-REPORT）

- 核对员：§8.4 zh-tw 核对员（全新校对员，与建造者、第一/二轮校对员、修复者均不同；只读核对，未改任何生产文件，未 commit/push/lint --write/reset/stash）
- 核对时间：2026-11-13 ~05:00–05:30 UTC（任务时戳 2026-11-12 23:56 EST）
- 范围：目标语 zh-tw × 读者母语 en de es fr it ja ko nl pt ru，共 10 版；无 zh-cn 读者版；core-zh-tw 即 zh-tw-en，无独立 `2026-w47-zh-tw-en` 目录
- 磁盘：开工 96G 已用，收尾 96G（< 100G 停手线，未触发）
- 先读：SOP.md 全文（重点 §8）+ run-log.md 全文 + ledger.md + 第二轮 `scratch-reproof2-w47-zh-tw/PROOF-NOTE-2.md` 全文

## 结论总览：10/10 CLEAN

| 版 | 最后重校记录 | 结论 |
|---|---|---|
| core-zh-tw（zh-tw-en） | 第二轮 fad16b47，2026-11-12 18:20 UTC，(a) | VERIFIED CLEAN（SHA 一致） |
| zh-tw-de | 第二轮 fad16b47，18:20 UTC，(a) | VERIFIED CLEAN（SHA 一致） |
| zh-tw-es | 第二轮 fad16b47，18:20 UTC，(a) | VERIFIED CLEAN（SHA 一致） |
| zh-tw-fr | 第二轮 fad16b47，18:20 UTC，(a) | VERIFIED CLEAN（SHA 一致） |
| zh-tw-it | 第二轮 fad16b47，18:20 UTC，(a) | VERIFIED CLEAN（SHA 一致） |
| zh-tw-ja | 第二轮 fad16b47，18:20 UTC，(a) | VERIFIED CLEAN（SHA 一致） |
| zh-tw-ko | 第二轮 fad16b47，18:20 UTC，(a) | VERIFIED CLEAN（SHA 一致） |
| zh-tw-nl | 第二轮 fad16b47，18:20 UTC，(a) | VERIFIED CLEAN（SHA 一致） |
| zh-tw-pt | 第二轮 fad16b47，18:20 UTC，(a) | VERIFIED CLEAN（SHA 一致） |
| zh-tw-ru | **本轮全新全量重校（SHA 变过），(a) 干净，0 新发现** | **RE-PROOFED CLEAN** |

- 9 版：最后重校 (a) + 磁盘三 SHA 与重校记录逐字一致 → VERIFIED CLEAN，无需重校。
- 1 版（zh-tw-ru）：印/网 PDF 在最后重校后被 *-ru 重建工人 C（4b908b8c，2026-11-12 23:52 UTC）重建，SHA 变过 → 本人按 SOP §8 做全新全量重校，结论 (a) 干净，0 新发现。
- 待修清单：**无阻塞缺陷**。仅 2 项观察（O-1、O-2，见 zh-tw-ru 节）+ 1 处 KIT 文字笔误（wave-2 清单），均不阻塞插仓。

## SHA-12 表（磁盘实测 2026-11-13 ~05:05 UTC）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） | 与最后重校比对 |
|---|---|---|---|---|
| core-zh-tw | 11,195,126 / 27afa3281b1d | 1,898,131 / 45d076003801 | 49,804 / 9b8b5295ddd8 | 一致（reproof2） |
| zh-tw-de | 11,196,101 / 2a22bcdaa8ca | 1,903,630 / a67ffad91835 | 51,820 / 8187f6196326 | 一致（reproof2） |
| zh-tw-es | 11,194,154 / 25216239cbf9 | 1,902,298 / f8c0086a1a66 | 52,252 / e8a36b7996f6 | 一致（reproof2） |
| zh-tw-fr | 11,191,659 / 47320e77d6f1 | 1,899,287 / 233658513953 | 52,476 / a2df8892d632 | 一致（reproof2） |
| zh-tw-it | 11,187,826 / 0cdf05fef852 | 1,895,728 / 3ed32974c27d | 51,691 / 788ed6f6600c | 一致（reproof2） |
| zh-tw-ja | 16,365,954 / dbbe03ab27b3 | 2,447,388 / 660f93940fe8 | 53,759 / 6e5b4b81e131 | 一致（reproof2） |
| zh-tw-ko | 12,719,179 / e49ab5fee582 | 2,134,244 / 7419fee9eedf | 53,922 / 0215bc2cf6a6 | 一致（reproof2） |
| zh-tw-nl | 11,189,718 / 20ad418b233c | 1,898,763 / d28897aea142 | 50,602 / 487127dd7d72 | 一致（reproof2） |
| zh-tw-pt | 11,198,017 / 7c59676c6ef0 | 1,907,201 / 90caf45fab41 | 51,498 / 542bfae121e5 | 一致（reproof2） |
| zh-tw-ru | 11,291,943 / 8c3aca16ea41 | 1,997,666 / 04606730a740 | 62,498 / ea9c1514df96 | **印/网变过**（reproof2：11,366,471 / eb3fd9aae5e2、2,070,994 / 16a6d20a755e）；text.md 未变 |

完整 SHA-256 见各版生产目录实测（本报告 SHA-12 均为实测值前 12 位）。

## 最后重校记录逐版（run-log + PROOF-NOTE 核查）

- **第二轮全家重校（9 版的最后记录）**：工人 fad16b47，`scratch-reproof2-w47-zh-tw/PROOF-NOTE-2.md`，2026-11-12 ~18:20 UTC，结论 (a) 干净，0 新发现；第一轮 P7 金句缺「香港」已在 10 版全部修复并逐版核实；门禁 9 版 ALL-GREEN（ja 版仅已书面定性的 SIMP_ONLY 人为产物）；P8 最小字号 9.75pt。run-log L4616/L4648 记为二轮干净 4 家之一。
- **其余 9 版在 18:20 UTC 之后无任何重建**：逐一核查 run-log 18:20 UTC 至 05:00 UTC 全部条目——es/it/nl/fr/ko/ja/ru 各家二轮修复、*-ru 重建、三轮及以后重校、扫查、门禁复核均只动本家他版或他家版本；触及 zh-tw 目标语家的只有 *-ru 重建的 zh-tw-ru 一版（下述）。de/fr/it 三轮重校覆盖的是 de-zh-tw / fr-zh-tw / it-zh-tw（目标语 de/fr/it），不是本家 zh-tw-de / zh-tw-fr / zh-tw-it，特此区分。
- **zh-tw-ru 的后续史**：18:20 UTC reproof2 (a) → 23:52 UTC *-ru 重建工人 C 重建印/网 PDF（`scratch-fix-xru-w47/summary-zh-tw.txt`：run.py rc=0、probe LAT@NotoSans 518→0、TEXT-LAYER MULTISET IDENTICAL pre/post 57,457 chars、text.md 未变）→ 01:13 UTC 扫查工人 f595a087 只扫 occlusion+boxtitle（全 PASS），**不是全量重校**。因此 zh-tw-ru 无重建后的全量重校记录，本轮补做。

## zh-tw-ru 全新全量重校（本轮，SOP §8）

- 校对对象（磁盘实测）：印 `Lucerna-VOL4-RU.pdf` 11,291,943 B / 8c3aca16ea41…；网 `Lucerna-VOL4-RU-web.pdf` 1,997,666 B / 04606730a740…；文 `2026-w47-zh-tw-ru.text.md` 62,498 B / ea9c1514df96…（与 reproof2 一致，未变）。
- **结论：(a) 干净 —— 0 条新发现**（MAJOR 0 / MEDIUM 0 / low 0）。

### 1. text.md 全量通读（与 core-zh-tw 全量 diff，2,514 行逐行读完）
- 俄语讲解层 934 行新增逐行核对：翻译准确；全部事实/数字/日期与 core 一致；无 core 以外的新事实。
- 算术全验：1200+800=2000、2000−1200=800；11月6–22日=17天；17:00→18:30=1.5小时；14:00→19:00=5小时；11月17日–1月3日=48天（14+31+3）；11月17–22日=6天；5×10=50、7×10=70、距100差30；17:30→23:00每半小时=12场；587部、267处、5米、142字范文——全部与 core 一致。
- 日期/星期：11月22日周日、11月13日周五、11月15日周日、11月17日周二、11月19日周四、11月21日周六、12月27日周日、2027年1月3日周日——俄语译文星期表述全部正确。
- P7 8 条金句：俄译与核心一致，页码 (с. 1–5) 正确；第 8 条中文引文含「香港」，印 PDF 文字层核实 `香港迪士尼聖誕，從11月17日開始` 在位（P5 原句 + P7 引文）。
- CJK 字符集对照：ru 版去重 CJK 699 字与 core 完全相同，仅一换一：多 `俄`（俄語講解）、少 `英`（英語講解）；简体字扫描 0 命中。
- ABSTRACT（俄语读者版，621 B，单行，无 ASCII 双引号）：主题/刊期/分级/题数均与本期一致（见 O-2）。

### 2. P8 150 题（SOP §8.2）
- `tools/p8.py compare` vs core-zh-tw：**CLEAN**，150 noted，missing=[]、extra=0、keydiff=[]。
- 150 条答案简析逐条读完（diff 全量）：键与 core 逐条一致，数字/日期与题面/原文一致；150. ✓ 开放题，范文 142 字。
- P8 最小字号实测 9.75pt（PyMuPDF，§1.1 现行众数，符合）。

### 3. 印/网文本层
- pdftotext 各 58,542 / 58,543 字节，均 > 0；字符多重集差 0（仅 1 个换行符差），词元 4,435 = 4,435。
- 唯一字节级差异是提取顺序：P1 kicker `香港` 一词在 web 层排在第 3 词元、在印层排在第 11 词元；PyMuPDF 核实两版 P1 该词坐标逐字相同（653.3, 54.2 与 1185.7, 963.3），全书各 12 处——纯 pdftotext 读取顺序 artifact，非内容差异。记为观察 O-1，不列缺陷（与 reproof2 textcheck-adapted 多重集口径及 fix-xru 工人「TEXT-LAYER MULTISET IDENTICAL」口径一致）。

### 4. 8 页逐页看图（print PDF，100 dpi 渲染，`pages/p-1.png` … `p-8.png`）
- P1–P8 逐页目视：无溢出、无重叠、无压页脚、无豆腐块、无截断；页脚 `Страница N из 8` 齐全；VOL.4、刊期 2026年11月16日至11月22日齐全。
- *-ru 重建专项（拉丁文改走 Newsreader 后变宽风险）：P1 头条与俄语 gloss 无重叠；occlusion 0 flags（下述）；P1 kicker `台灣 香港 ТАЙВАНЬ И ГОНКОНГ` 与刊头净空干净。
- 图注–图片对照（fr 家 A1 同类，新增覆盖）：6 张图逐张核对——P2 雨滴图 ↔「冷空氣一波波，雨天出門記得帶傘」✓；P3《月球之旅》1902 剧照 ↔「電影從黑白默片走到今天的金馬獎」✓；P4 棒球旧照（Bain News Service）↔「棒球舊照」✓；P5 百年前維多利亞港 ↔「一百多年前的維多利亞港」✓；P7 旧书 ↔「舊書，越讀越有味道」✓；P8 铅笔写字 ↔「寫下來，才記得住」✓。**6/6 相符，无 fr A1 类错配。**
- 6 张图与 core-zh-tw 印 PDF 逐字节相同（PyMuPDF 图像哈希比对，P2/P3/P4/P5/P7/P8 各 1 张）——图注–图片结论适用于全家 10 版（中文图注与图片均为共享核心内容，仅读者语出处行 `Photo:/Фото:` 措辞不同）。

### 5. 机械门禁（共享工具，`tools/venv/bin/python`，日志 `gates/zh-tw-ru/`）
| 门 | 结论 |
|---|---|
| checks.py（图表点位等） | RC=0 PASS |
| occlusion_audit.py | RC=0，0 flags（自检 6 类全触发） |
| p8.py compare | CLEAN，150/150，keydiff=[] |
| spill_sweep.py | 0 SPILL（219 OBSERVE） |
| boxtitle_check.py | 72 titles，0 DEFECT，0 marginal |
| pdf_edge_scan.py | 8 页，0 TOUCH，0 NEAR（最小边距 bottom 53.6pt） |
| d5_census.py | PASS（LAT@CJK 0、CYR@CJK 0、curly 5 全在 Newsreader、Noto Sans 元素 1790 = 俄文） |
| census_quotes.py | 0 defective（U+201C ×5 全在 Newsreader） |
| head_check.py（对 fix-xru 重建 run log） | PASS，0 defects（首轮误传版目录 RC=2 系调用错误，已纠正重跑） |
| freeze | 未跑（无重建前 SVG 快照；印/网/text.md SHA + 多重集 + 门禁已覆盖；fix-xru 工人已做 pre/post 多重集 IDENTICAL） |

### 观察项（不列缺陷，不阻塞）
- **O-1**：印/网 pdftotext 非逐字节相同（见 §3：仅 `香港` 一词提取顺序 + 1 个换行符差；内容多重集一致）。若协调员要求逐字节口径，须重建 web PDF 再验——但 webpdf 构建本身非确定性（run-log 04:08 已记同一内容三次构建三次 SHA），逐字节口径对此版不稳定，不建议追。
- **O-2**：ABSTRACT 俄语版「150 упражнений」出现两次（句首 `A2–B2, 150 упражнений:` 与句末 `— 150 упражнений на темы недели`）——措辞重复，非事实错误；系 core 英文摘要同款模板句式继承，非俄语层引入，不修。

## KIT §7 SHA 核对（wave-2 清单）
- 10 版 KIT 均含磁盘现行印/网/text.md SHA（每版各 SHA 至少命中 2 处；zh-tw-ru 含 fix-xru 节，新 SHA 全文在位）→ **KIT §7 与磁盘一致，wave-2 无 SHA 待补**。
- 1 处 KIT 文字笔误（不阻塞，记入 wave-2 文字清单）：zh-tw-ru KIT L35 称印 PDF「比其他版（~20 MB）小」——同家他版实为 ~11.2 MB，`~20 MB` 数字有误；同行引用的 web 2,070,745 B 为重建前旧值（现行 1,997,666 B 另有 fix-xru 节正确记录）。建议 wave-2 改写该行，其余不动。

## 交付物
- 本报告：`hidden_files/w47/scratch-verify-zh-tw/VERIFY-REPORT.md`
- 机械门禁日志：`hidden_files/w47/scratch-verify-zh-tw/gates/zh-tw-ru/`（GATES-SUMMARY.txt + 各门 log/json + print.txt/web.txt）
- core–ru 全量 diff：`hidden_files/w47/scratch-verify-zh-tw/diff-core-vs-ru.txt`（2,514 行）
- 门禁脚本：`hidden_files/w47/scratch-verify-zh-tw/run_gates_ru.sh`
- 8 页渲染图：`hidden_files/w47/scratch-verify-zh-tw/pages/p-1.png` … `p-8.png`（100 dpi，仅供本轮目视核对）
- 未改动生产目录任何文件；未 commit/push；未跑 lint。
