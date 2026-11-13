# W47 ja 家庭最终重校核对报告（VERIFY-REPORT）

- **核对员**：ja 家 §8.4 状态核对员（全新校对员，与建造者及第一至四轮校对员/修复工人均不同）
- **日期**：2026-11-13（UTC 约 05:00；磁盘核对时点 04:57 UTC）
- **范围**：ja 家 11 版（core-ja = ja-zh-cn + 10 个 fan-out：ja-de/ja-en/ja-es/ja-fr/ja-it/ja-ko/ja-nl/ja-pt/ja-ru/ja-zh-tw）
- **工作目录**：`hidden_files/w47/scratch-verify-ja/`（本报告、门禁日志 `gates.log`、逐版 JSON `gates/`、core 对照 diff `diff-core-vs-jaru.txt`、8 页渲染图 `pages/p1–p8.png`、门禁脚本 `run_gates_ja_ru.sh`）
- **约束遵守**：只读核对，未改任何生产文件，未 commit/push，未跑 lint（无 `--write`、无 reset/stash/add），未碰 ja 以外任何版。解释器一律 `tools/venv/bin/python`，只用仓内共享工具。磁盘 96G 已用（<100G 门限）。

## 结论总览

| 版 | 最后重校记录 | 磁盘 SHA 是否一致 | 结论 |
|---|---|---|---|
| core-ja（zh-cn） | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |
| ja-de | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |
| ja-en | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |
| ja-es | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |
| ja-fr | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |
| ja-it | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |
| ja-ko | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |
| ja-nl | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |
| ja-pt | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |
| ja-ru | 第四轮 aa94c0d9，(a) CLEAN，但**重校后印/网 PDF 已重建** | 否（印/网变，text.md 未变） | **本轮全新全量重校（第五轮），(a) CLEAN** |
| ja-zh-tw | 第四轮 aa94c0d9，(a) CLEAN | 是（3/3） | **VERIFIED CLEAN** |

**ja 家 11/11 最终状态成立：10 版 VERIFIED CLEAN + ja-ru 第五轮重校 CLEAN。待修内容清单：无。**仅 1 项 KIT 文字同步记入 wave-2 清单（见 §5，非内容缺陷）。

## 1. 最后重校记录（10 版的依据）

- 最后一次全量重校：**第四轮**，校对员 aa94c0d9，`scratch-reproof4-w47-ja/PROOF-NOTE-4.md`，2026-11-12，结论 **(a) 干净——一整轮全量校对零问题**（run-log L4824–4826，协调员已读并接受，ja 家庭定稿第 7 家）。
- 该轮指纹表（§1）与磁盘实测对照：10 版 30/30 一致（印/网/text.md 尺寸 + SHA-12 全合）；ja-ru 仅 text.md 一致，印/网不一致（见 §3）。
- mtime 核查：除 ja-ru 外，10 版全部文件在第四轮重校完成时刻（2026-11-12 ~22:40 UTC）之后**零改动**（`find -newermt "2026-11-12 22:40 UTC"` 在 10 版目录下无结果，`__pycache__` 除外）。

## 2. 当前磁盘 SHA-12 表（2026-11-13 04:57 UTC 实测）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| core-ja（zh-cn） | 25,973,509 / `0ce5e4b872ae` | 4,654,731 / `0f9098ff3bf0` | 44,432 / `55c570f1bd0e` |
| ja-de | 25,813,856 / `4283e8a74ff9` | 4,387,416 / `c24dfb09d7d0` | 46,520 / `0d8d1de78a06` |
| ja-en | 25,806,211 / `c6a15edb8a6c` | 4,379,966 / `0560f0e4ea85` | 45,706 / `fb5a4700d3c9` |
| ja-es | 25,814,013 / `74066b869920` | 4,387,651 / `43a26e56278f` | 46,702 / `d8e0c3018361` |
| ja-fr | 25,812,296 / `9d4c6114fb31` | 4,386,312 / `ef073db3df37` | 46,882 / `badb0a6e7d00` |
| ja-it | 25,807,665 / `e44a8fcba1ba` | 4,381,291 / `3cb1e9559b3a` | 46,692 / `91224d88a55d` |
| ja-ko | 28,141,037 / `b78a3f6d5a39` | 4,552,025 / `bdf5074b3698` | 47,722 / `b1736ccf46f8` |
| ja-nl | 25,805,479 / `d6f14754f22c` | 4,379,026 / `97ee26ba1616` | 45,627 / `7f8f6638e635` |
| ja-pt | 25,814,751 / `3cca426dcbec` | 4,388,490 / `a573debf0755` | 46,696 / `9c9609378189` |
| ja-ru | 25,898,158 / `44d884ac6b54` | 4,469,712 / `d130ae325fed` | 53,004 / `f934bcf1d9f4` |
| ja-zh-tw | 25,988,418 / `4b09db1088b8` | 4,789,292 / `649ac196e81a` | 44,361 / `77fb0f36c75b` |

全量 SHA-256 见附录 A。第四轮指纹对照：10 版 30/30 与上表一致；ja-ru 第四轮值为印 `04b2f315e267` / 25,970,343 B、网 `0726eda64903` / 4,540,808 B，已被重建取代。

## 3. ja-ru 为何重校：重校后重建

- 第四轮重校完成后，跨家 *-ru 修复（Latin 标题误入 Noto Sans）重建了 ja-ru：工人 fec69813，2026-11-12 23:50–23:51 UTC，印 PDF `44d884ac…` / 25,898,158 B、网 PDF `d130ae325fed…` / 4,469,712 B（run-log L4886，协调员已逐项核实与汇报一致）。
- 改动范围（`scratch-fix-xru-w47/summary-ja.txt` + KIT §12）：仅 `svglib.py` 的 `_D5_READER == "ru"` 分支（拉丁文改走 Newsreader），8 张 SVG + 印/网 PDF 重渲染；**内容、text.md 均未动**（text.md SHA 仍为 `f934bcf1d9f4`，与第四轮一致；印层文字多重集重建前后 IDENTICAL，21,342 非空白字符）。
- 但 SOP §8 循环规则：重渲染即须从头再做一轮全量校对。另有扫查工人 09cda9c4（2026-11-13 ~01:15 UTC）报 ja-ru occlusion + boxtitle 双门 PASS——仅两门，非全量重校，不能替代。
- 故本轮对 ja-ru 做**全新全量重校（第五轮）**，其余 10 版按任务书第 2 条直接 VERIFIED CLEAN。

## 4. ja-ru 第五轮全量重校（本轮新做）

### 4.1 text.md 全文通读（1382 行）

- 全文 1382 行逐行读完：P1–P8 文章、练习、P8 答案逐题核对；俄语讲解层逐项对照日文正文（译注词均真实出现在正文里）。
- 与 core-ja 的 diff 全量核对（core-only 359 行 / ru-only 385 行，`diff-core-vs-jaru.txt`）：家具、译注、题干说明、P7 金句 gloss、读者园地、P8 全部答案简析、137–140 翻译题俄译均已读。
- 俄语拼写/变格复核：Фудзирёга（主格 2 处）/ Фудзирёги（属格，答案 54/111）/ Фудзирёге（与格，答案 116）变格正确；Ёсинофудзи、Чура-но-уми、Хосёрю、Оносато 均正确；旧拼 `Фудзирюг`、`Уми-но-уми`、`ryuuryuu` 全版 0 处；`rikuryuu` 5 处在位。
- P7 本周金句 8 条逐字核对与正文一致、页码引用正确（(с. 1)×3、(с. 2)×2、(с. 3)、(с. 4)、(с. 7)）；137–140 页码引用正确（стр. 2/3/5/6）。
- ABSTRACT.txt：俄语、单行、无 ASCII 双引号，含刊名、目标语名、A2–B2、150 题与真实主题。

### 4.2 P8 150 题逐题复核

- 题号 Q 1–150 与答案 A 1–150 均齐全、无缺无重（程序计数）。
- 逐题验算（题面 ↔ 原文 ↔ 答案）：Q1–Q112（P1–P7 即学即练）与 Q113–Q150（P8 综合卷）全部与答案一致；其中 Q91（38−24=14）、Q92（38+24=62）、Q93（38+24+22+16=100）算术全对；Q137–140 为预期的俄语翻译题键。
- 范文 154 字（去空白精确计数 154，与 Q150 指引句一致）。

### 4.3 日期/星期与事实（`date -d`，Asia/Tokyo）

- 11-03 周二、11-05 周四、11-07 周六、11-08 周日、11-13 周五、11-16 周一、11-19 周四、11-21 周六、11-22 周日、11-23 周一、12-01 周二——与正文所称星期全部一致；刊期 11-16 周一～11-22 周日正确。
- 事实复核：酉の市二の酉 11 月 19 日（第 3 木曜日）与ボジョレー解禁同日；相扑九州场所 8 日开幕、3 日目两横纲 2 胜 1 败、千秋乐 22 日；流行语提名 30 语 11 月 5 日、Top 10 为 12 月 1 日；嵐山見頃两说（23 日/26 日）正文已同时交代预报版本差，练习只用 23 日/12 月 12 日，无内在矛盾（第四轮 O1，本轮复核后不重报）。
- 图片出处 5 处在位（P1 Poliphilo CC0、P3 Alainauzas 公有领域、P5/P8 lumoplank CC0、P7 Mozzucu CC0，P7 照片日期 2025-11-24 已披露）。

### 4.4 印/网/text.md 一致性

- 印/网 PDF 各 8 页；pdftotext 文字层**逐字节相同**（各 52,013 字节）；非空白多重集相同。
- text.md 全部有效行（1355 行，去空白归一化）均在印 PDF 文字层中逐字找到，**缺失 0 行**。
- P8 最小字号（PyMuPDF 实测印 PDF 第 8 页）：**9.98pt** ≥ SOP §1.1 底线 9.75pt。

### 4.5 xru 修复本身复核（探针重跑）

- 在当前 SVG 上重跑与 `scratch-fix-xru-w47/probe_xru.py` 同口径的 ja-ru 单版探针：runs=4556，LAT@Newsreader=897、**LAT@NotoSans=0**、CYR@NotoSans=3925、CYR@Newsreader=0、CJK+LAT=0、CJK+CYR=732——与重建记录（summary-ja.txt）逐项一致，修复在位。
- CJK+CYR=732 为 ru 读者模式的已知属性（D5 census PASS，见 4.6），非缺陷。

### 4.6 机械门禁（共享工具，`tools/venv/bin/python`，日志 `gates.log`，逐版 JSON 在 `gates/`）

| 门 | 结果 |
|---|---|
| `p8.py compare --total 150`（vs core-ja） | **CLEAN**，150/150，keydiff=[137, 138, 139, 140]（预期翻译题键） |
| `occlusion_audit.py`（自检 OK，6 类全触发） | **0 flags** |
| D5 census（`d5_census.py`） | **PASS**（D5_lat=0，D5_cyr=0，curly_total=0；noto_sans_elements=666，ru 模式预期） |
| 引号普查（`census_quotes.py`） | defective **0** |
| `boxtitle_check.py` | **0 DEFECT，0 marginal**（第四轮的 1 marginal 已裁定 pre-existing；本轮重建后为 0） |
| `spill_sweep.py` | **0 SPILL**（151 OBSERVE） |
| `pdf_edge_scan.py` | **0 TOUCH，0 NEAR**（P8 最小边距：上 54.0pt、下 53.6pt、左 65.9pt、右 58.0pt） |

7 门 RC 全部为 0。未重跑项：freeze baseline 与 creambox（第四轮记录：修复轮已跑 8/8 与 PASS；本次重建仅改字体路由，印层文字多重集重建前后 IDENTICAL，text.md 未变，结论仍成立；本轮任务门禁清单未含此项）。

### 4.7 8 页逐页看图

- 印 PDF 8 页 72dpi 全页渲染（`pages/p1–p8.png`）逐页看过：无溢出、重叠、压页脚、豆腐块、截断句；5 张图片与出处均在位；P6 图表柱长与 38/24/22/16% 一致；P8 答案区 1–150 三栏完整、范文与寺院图在位。
- 栏间续句（如 P2 栏顶“す。”、P4 栏顶“5）でお知らせします。”）为正常栏间续排，非截断。

### 4.8 发现表

**无发现。结论：(a) 干净——一整轮全量校对零问题。**

未重报项（按任务要求，已裁定/已知）：第四轮 O1（嵐山 23 日/26 日双日期，正文已交代版本差）、O2（读者来信 gloss 多一句邀稿）、O3（`_D5_READER="latin"` 标签差异）、O4（EDITION-RECORD.md 历史 SHA 滞后）；ja-ru boxtitle 旧 1 marginal（本轮已为 0）；P8 答案简析末尾的字母回显（如 `25. b — … b`）为全家既有格式，非缺陷。

## 5. KIT §7/SHA 核对（wave-2 清单）

逐版核对 KIT 内当前印/网/text.md SHA 与磁盘是否一致：

- **10 版一致**：core-ja、ja-de、ja-en、ja-es、ja-fr、ja-it、ja-ko、ja-nl、ja-pt、ja-zh-tw 的 KIT 均含当前磁盘 SHA（印/网各至少 1 处，text.md 亦在位）。
- **ja-ru（wave-2 清单 1 项）**：KIT §12 fix-xru 含当前值（印 `44d884ac…`/25,898,158 B、网 `d130ae325fed…`/4,469,712 B、text 未变），与磁盘一致；但 **KIT §8 主段落仍以重建前的值为交付值**（印 25,970,343 B `04b2f315e267…`、网 4,540,808 B `0726eda64903…`），未同步到 fix-xru 后的现值。建议 wave-2 将 §8 主段落的印/网字节数与 SHA 更新为 §12 的现值（或加注指向 §12）。**只记录，不改 KIT。**
- 其余 KIT 内的旧 SHA 均为有标注的历史构建记录（fix1/D5 各轮），不列入清单。

## 附录 A：全量 SHA-256（磁盘实测）

```
core-ja/Lucerna-VOL4.pdf 0ce5e4b872ae4d53fc639bff0ae2df3cf2bfd91149bd08b04400920e21adc214
core-ja/Lucerna-VOL4-web.pdf 0f9098ff3bf0836c279960beffdb1ff619c1cdb01fceef699046c0a77be1e9ef
core-ja/2026-w47-ja-zh-cn.text.md 55c570f1bd0e9ea4d907960fe0fc472fe69440bacf67a83af40d0d48b977e1aa
2026-w47-ja-de/Lucerna-VOL4-JA-DE.pdf 4283e8a74ff969a5d6d565e5cc03cd0618648ed827e6cd8843ce5ec85326c7a5
2026-w47-ja-de/Lucerna-VOL4-JA-DE-web.pdf c24dfb09d7d0c54333c6f43aafdf697a08e99a178c5be5b762bc571c90086d4c
2026-w47-ja-de/2026-w47-ja-de.text.md 0d8d1de78a06d4df371b88425cb66f330222e6ca1a200632fdcdc48c8c95bd22
2026-w47-ja-en/Lucerna-VOL4-JA-EN.pdf c6a15edb8a6c9e2954cb844b38b36a27f19d404ede7ad5084c3d3389db3410cf
2026-w47-ja-en/Lucerna-VOL4-JA-EN-web.pdf 0560f0e4ea8520899c0b7054ded812d2a16fba6cec0f9e55cfc3bec8b99c1d8d
2026-w47-ja-en/2026-w47-ja-en.text.md fb5a4700d3c94cd17039d8b69d2626e35ed115812fdcb5ca34f17294f8860c3f
2026-w47-ja-es/Lucerna-VOL4-JA-ES.pdf 74066b86992080d5de346594ec437f0686932daa2b68d2acc176925d1933bd53
2026-w47-ja-es/Lucerna-VOL4-JA-ES-web.pdf 43a26e56278f7b7cca4219c18ce508bdc2fe1662e99e2f91584e4ebcb71f09f2
2026-w47-ja-es/2026-w47-ja-es.text.md d8e0c3018361cdce75084706e6857e642822992ecab8ac55f5865b861091ebb0
2026-w47-ja-fr/Lucerna-VOL4-JA-FR.pdf 9d4c6114fb31cca2a912c2313f756667277748f048b4c0041aba10bc051e4507
2026-w47-ja-fr/Lucerna-VOL4-JA-FR-web.pdf ef073db3df3789ef4326440df33cea387675e0ed1b5dacc17161220bf0622c5a
2026-w47-ja-fr/2026-w47-ja-fr.text.md badb0a6e7d00858afda9e6d1e158a915e93bd1ee41478e23bf3857cf23c72563
2026-w47-ja-it/Lucerna-VOL4-JA-IT.pdf e44a8fcba1ba429a2ad6c463cca8f4e33559d1a65139e46fa27d367f4242cf6c
2026-w47-ja-it/Lucerna-VOL4-JA-IT-web.pdf 3cb1e9559b3a6e7763858cbaeae56eee9a61e54a083e8ade9c5c950e513a62fb
2026-w47-ja-it/2026-w47-ja-it.text.md 91224d88a55d5dc7ae8c3411e62d4199fe32d4028293223ba5373bd3a21125aa
2026-w47-ja-ko/Lucerna-VOL4-JA-KO.pdf b78a3f6d5a39da219b61d8ae179c397622259484dfe3a4804f2027a7be51d0d2
2026-w47-ja-ko/Lucerna-VOL4-JA-KO-web.pdf bdf5074b36981cf6bcf913a8d732a604dd37d4be9a65398c6c6a43b79f4c3f73
2026-w47-ja-ko/2026-w47-ja-ko.text.md b1736ccf46f8cd2cc7646038c5163849e306210884d4b15fbb3f388a82535517
2026-w47-ja-nl/Lucerna-VOL4-JA-NL.pdf d6f14754f22c8ee43d343a59d77e6cf0df271465d9dfcbe3b094a5368da2246d
2026-w47-ja-nl/Lucerna-VOL4-JA-NL-web.pdf 97ee26ba16163696bd9a1ff30968bd71e8eab18af4cc75fcf9f2e04ded95f338
2026-w47-ja-nl/2026-w47-ja-nl.text.md 7f8f6638e6352eb8ba9c1a2b3283f0e2436ea65613cf15c109ae3f067f69af4d
2026-w47-ja-pt/Lucerna-VOL4-JA-PT.pdf 3cca426dcbec961b4a1ddb54248e05f1d1771f9661fd9df5ed70d10773749dbf
2026-w47-ja-pt/Lucerna-VOL4-JA-PT-web.pdf a573debf07556431b5d8b20d95f088d9f8f098c84935380f9a7fb3635ab5a81e
2026-w47-ja-pt/2026-w47-ja-pt.text.md 9c9609378189a5b32b894b5c26adbdf4e8e1b23bbbe7b923f7a6198c4c62564a
2026-w47-ja-ru/Lucerna-VOL4-JA-RU.pdf 44d884ac6b543a6be3f4186ffe8ce22899a5ba90bc1f951539e0a3176af822a4
2026-w47-ja-ru/Lucerna-VOL4-JA-RU-web.pdf d130ae325fedb8325a724aef3ee3889b1db01c9ee0d5091b74644a9ab388dbd5
2026-w47-ja-ru/2026-w47-ja-ru.text.md f934bcf1d9f4611d094ed6f55a1f76fc8da74663cfe647c9fed17025af3d4eec
2026-w47-ja-zh-tw/Lucerna-VOL4-JA-ZH-TW.pdf 4b09db1088b81f4a56bfd5ee7126088cb2762e2348279f402032c1749bd76c8c
2026-w47-ja-zh-tw/Lucerna-VOL4-JA-ZH-TW-web.pdf 649ac196e81abf1a99524847e89ca4d5104080f12b644aa234aee0b94819b5cc
2026-w47-ja-zh-tw/2026-w47-ja-zh-tw.text.md 77fb0f36c75bb4713873b33793d63fc243f27fee3d4450c1d1e8f5da94ed416f
```

## 附录 B：工作产物

- 本报告：`scratch-verify-ja/VERIFY-REPORT.md`
- 门禁：`scratch-verify-ja/run_gates_ja_ru.sh`、`gates.log`、`gates/ja-ru-{p8,occlusion,census,boxtitle,spill,edge}.json`
- core 对照 diff：`scratch-verify-ja/diff-core-vs-jaru.txt`（core-only 359 行 / ru-only 385 行）
- 8 页渲染图：`scratch-verify-ja/pages/p1–p8.png`（72dpi，读完保留备查）
