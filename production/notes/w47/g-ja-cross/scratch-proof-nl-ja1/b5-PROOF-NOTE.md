# PROOF-NOTE — 2026-W47 nl → ja（日语读者版）· proof1（独立复校）

- 版目录：`production/2026-w47/fanout-nl/2026-w47-nl-ja/`
- 复校员：独立复校（proof1）· 2026-11-11（America/Toronto）
- 机械门完整证据见同目录 `GATE-LOG.md`；150 题逐题手验见 `keycheck-150.json`
- 源文件未改动、未重建、未 commit、未 push

## §0 身份核对（磁盘为准）

| 文件 | 磁盘 SHA-256 | 磁盘字节 | 与任务一致 |
|---|---|---|---|
| `De-Lucerna-VOL4-nl-ja.pdf`（印） | `af010c1f2d2f0d39a61417aa3ace0bc02e9e20fcece5e4181314721a5361c1b1` | 26,049,268 | ✓ |
| `De-Lucerna-VOL4-nl-ja-web.pdf`（网） | `07243a6bc87aee40eeb1b03b4967e7917db835d709a0245e86678fac2dbd1d2f` | 2,119,188 | ✓ |
| `2026-w47-nl-ja.text.md` | `6685d681c585eca265e63de70bf0a77e78efb46aadedcaf2c747a4855c46d789` | 47,592 | ✓ |

三文件 SHA 与字节数与任务消息完全一致，无需停下。探针：`git hash-object -w` 通过（`9daeafb9…`）；goals 侧 scratch 可写（`probe.txt` 已写）。

## 结论：(b) 有缺陷，不能定稿

共 **2 项缺陷**（D1 中、D2 低），均可修复；修复后须重跑受影响的门（D1 重建 web PDF 后重验斜体与印/网文字层；D2 改 ABSTRACT 后重核摘要）并再做一轮零问题复校。

| # | 严重度 | 页 | 缺陷 | 归属 |
|---|---|---|---|---|
| D1 | 中 | P1（网 PDF） | 网 PDF 丢失本周词斜体：`«de groepswinst»` 在印 PDF 为 Newsreader Italic，在网 PDF 为 Regular 全文 0 个斜体 span | 机制 `tools/webpdf.py`（斜体面子集化丢失；核心网 PDF 同症） |
| D2 | 低 | ABSTRACT.txt | 摘要缺完整刊名 `De Lucerna`，只写了裸 `Lucerna VOL.4`，违反 SOP §9（含刊名） | 本版（全 nl 家庭 9 版共性；核心 ABSTRACT 有 `De Lucerna`） |

## 缺陷清单

### D1 — 网 PDF 丢失 P1 斜体（ru-en D3 同类，第 3 症状复现）
- **页码/定位**：网 PDF `De-Lucerna-VOL4-nl-ja-web.pdf` P1，`HET WOORD VAN DE WEEK` 栏，`«de groepswinst»`。
- **实测证据**（PyMuPDF span 实测，`fonts-italic.log` / `italic-deep.log`）：
- 印 PDF：P1 斜体 span 1 个 — `Newsreader16pt-Italic 16.12pt '«de groepswinst»'`；P1 内嵌字体含 `Newsreader16pt-Italic`。
- 网 PDF：全文 8 页斜体 span **0 个**；`«de groepswinst»` 所在 span 字体为 `LucernaNewsreader-Regula`（Regular）；P1 内嵌字体无 Italic 面（仅 `LucernaNewsreader-Regular`）。
- SVG 源头正确：`p1-voorpagina.svg` 该文本带 `font-style="italic"`。
- 同类三联症其余两项**未复现**：印/网文字层逐字一致（`«de groepswinst»` 前后空格完整、闭引号 `»` 未脱离；全卷 pdftotext 仅 2 处纯空格差异，见 GATE-LOG §印/网比对）。
- 机制性：核心 `core-nl` 自身网 PDF 同样 0 斜体 span（同工具 `webpdf.py` 子集化时把斜体面并入 Regular）。KIT 的印/网门只比文字不比字形，故漏检。
- **归属**：机制（`tools/webpdf.py`），非本版排版错；但本版交付的网 PDF 确有与印 PDF 的可见差异（本周词失去斜体标记）。
- **修复建议**：修 `webpdf.py`，使 italic/bold-italic 面独立子集、不并入 Regular（系统有 `Newsreader-Italic.ttf`，印 PDF 即用它）；修后重建本版网 PDF（SHA 将变，需更新 KIT 与后续 insert 记录），重验：网 PDF P1 须有 1 个 Italic span 且文字层与印版一致。

### D2 — ABSTRACT.txt 缺完整刊名 `De Lucerna`（pt-zh-tw D4 同类）
- **定位**：`ABSTRACT.txt` 全文：`オランダ語週刊 Lucerna VOL.4（2026年11月16日〜22日）：…`。
- **实测证据**：摘要含 `Lucerna`、`VOL.4`、目标语名（オランダ語）、A2〜B2、150 题、真实主题词，唯独缺冠词 `De`——完整刊名（报头）是 `De Lucerna`（SOP §1：荷兰语报头冠词用本语 `De`；text.md 标题、核心 ABSTRACT 均为 `De Lucerna`）。核心 ABSTRACT：`De Lucerna 荷兰语周报 VOL.4：…`。对照：nl 家庭 9 个 fan-out 版摘要全部只写裸 `Lucerna VOL.4`（模板共性），核心除外。
- **归属**：本版（摘要层）；修复须全家庭统改才彻底，单修本版即可过本版门。
- **修复建议**：改为 `オランダ語週刊 De Lucerna VOL.4（2026年11月16日〜22日）：…`（只加 `De ` 两字符，其余不动）；同步检查其余 8 个 nl 摘要与 md frontmatter 的 `abstract` 字段（insert 时）。

## 未决事项

- **O1（观察，非缺陷）**：Q78 `Zij ___ (maken)` 的 `Zij` 单复数歧义（单数 she → `gaat maken`，复数 they → `gaan maken`）。本版 P8 答案注已消歧（78 无标记=单数；79 注 `（複数）`=复数），且与核心逐字一致（核心 Q78 同文同键，属冻结核心）。建议以后各周避免裸 `Zij` 作题干，或题干内注明单复数；本版不动。
- **O2（方法备注，非缺陷）**：`tools/freeze.py` 无 `freeze_direct` 子命令，仅 `baseline`/`diff`（已按任务要求记为方法备注）。本次以 `freeze.py baseline`（核心重建 8/8）+ `freeze.py diff` 代替 direct 核验。

## 核实摘要（全部通过，详见 GATE-LOG）

- **全文通读**：印 PDF 8 页已逐页渲染目视（`render-p1.png`～`render-p8.png`）+ `text.md` 430 行全文通读；无溢出、无遮挡、无错字、无内部标签。
- **150 题手验**：150/150 通过（`keycheck-150.json`）。P8 印出键 = text.md 答案（149 道；150 作文题印 `✓`，模范文实数 **81 词**，在 80–100 范围内）。分级 A2 46 / B1 73 / B2 31（与 KIT 一致）；按页 10/18/18/18/18/18/12/38；题号 1–150 无缺无重。
- **机械门**：occlusion 0 flags；creambox 全版扫描 26 盒——P7 toolbox 3 盒最小内边 +12.5 / desc +6.5，P2/P5 `EN JIJ?` 末行 desc-clear −1.0/−0.9 经 PIL 真墨迹复核实为框内 −3.0/−3.1px（误报）；P6 图表头真墨迹在框内（KIT 称 advance 宽超 2.5px 属 advance 法假阳性）；全卷真墨迹溢出 0 旗；P8 compare CLEAN（150/150，keydiff 仅 137/138，已裁决为翻译重定向）；freeze baseline 8/8；freeze diff 仅讲解层中→日替换，无荷兰语目标句改动；P8 最小字号实测 **10.12pt**（≥ SOP §1.1 下限 9.75pt，与 KIT 一致）；印/网文字层基本一致（仅 2 处空格差异）。
- **本版必查 (a)–(g)**：(a) P1 标题/副标题横向溢出——无（真墨迹最宽 1873.8 < 1950；36pt 副标题合乎 1818 限）；(b) P3/P5 右栏末行降部漫出——无（上条已覆）；(c) P7 toolbox——通过；(d) E 节 type 标签——全日语（`翻訳` 等），无中文残留（`判断` 命中均为日语 `正誤判断` 内）；(e) 网 PDF 斜体——第 3 症状复现（D1），前两症状无；(f) ABSTRACT 刊名——缺 `De`（D2）；(g) 日语时间误写——无（`16:30` 等完整，`日:` 零命中，`11月16日：` 为正常日期+全角冒号分隔）。
- **外部事实核验**：PSV 26 分领跑荷甲（Q63/Q126，VAVEL/PitchLab 等 8 源一致：12 战 26 分）；阿姆斯特丹到着第 88 届、10:15 De Omval 出发、11:30 到敞篷船博物馆、13:00 Stopera 骑行出发（Q32/Q123/Q139，多源一致）；Cambuur–PSV 2–5、NEC–PSV 11 月 21 日（Q51/Q64/Q126）；全部日期星期核验无误（11/14 六、11/15 日、11/16 一、11/21 六、11/22 日、11/24 二、11/29 日、12/5 六）。
- **KIT 声明复核**：基本属实。两处说明：① KIT 称印/网 `posdiff 0 msdiff 0`，本次 `pdftotext -layout` 比对见 2 处纯空格差异（P1 `MA 16` 间距、P6 `DE GRAFIEK` 间距），文字无差，不属缺陷；② KIT 称 P6 图表头 advance 宽超框边 2.5px「渲染不可见」，本次真墨迹证实确在框内。
