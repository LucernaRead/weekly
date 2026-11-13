# W47 en 家 §8.4 统一核对报告（VERIFY-REPORT）

- 核对员：全新核对员（与建造者、第一轮/第二轮校对员、F1/F2/F3 与 boxtitle-fix2 修复者均不同）
- 时间：2026-11-13 04:56–05:10 UTC
- 范围：目标语 en，11 版：core-en（= 2026-w47-en-zh-cn）+ 2026-w47-en-{de,es,fr,it,ja,ko,nl,pt,ru,zh-tw}
- 方式：只读核对。未改任何生产文件（事后核查：04:50 UTC 后 en 家 11 个目录内无任何文件 mtime 变动）；未 commit/push，未跑 lint --write/reset/stash/add -A；未碰 en 以外任何版。
- 磁盘：开工 96G/150G，收尾 96G/150G，未触 100G 停手线。
- 工作目录：`hidden_files/w47/scratch-verify-en/`（本报告 + `run_gates_enru.sh` + `tool-out/` + 8 张 100dpi 渲染页 `page-{1..8}.png`）

## 结论总览

**en 家 11/11 VERIFIED CLEAN，可定稿。**

- 10 版（core-en/en-zh-cn、de、es、fr、it、ja、ko、nl、pt、zh-tw）：最后重校（二轮，工人 2f96abe3，2026-11-12 ~18:30 UTC）结论 (a) CLEAN，且印/网/text.md 三 SHA 与磁盘实测逐版一致 → VERIFIED CLEAN，无需重校。
- 1 版（en-ru）：二轮重校后因 *-ru 扫查回归做过 boxtitle fix2 重建，印/网 SHA 变过 → 本人按 SOP §8 做了全新全量重校（下文 §en-ru），结论 (a) CLEAN，0 新发现 → VERIFIED CLEAN。
- KIT SHA 核对：11 版 KIT 内记录的印/网/text.md 完整 SHA-256 均与磁盘一致（11/11），wave-2 清单无待修项。
- 待修清单：无阻塞项、无须修复项。仅 1 项非缺陷观察（Q109，见 §en-ru 末节），交协调员裁定，不拦定稿。

说明：任务书提到的“16:07 UTC 中间态三门禁 130/130”只是上一任协调员线的中间态，已被 18:30 UTC 的二轮全量重校结论取代，不作为最终状态依据。

## 最后重校记录（10 版共用）

- 工人：2f96abe3；轮次：第二轮独立重校（SOP §8/§8.4，全新工人）；报告：`hidden_files/w47/scratch-reproof2-w47-en/PROOF-NOTE-2.md`
- 结论：(a) 干净——零问题。第一轮 3 条低严重度（F1 Georgia 决胜轮、F2 en-fr `le passé simple`→`le prétérit`、F3 en-zh-tw 答案 13 `決勝輪`→`第二輪投票 12 月 1 日`）已核实修复到位；本轮从头全量重校未发现任何新问题。
- 机械门（tools/venv 解释器，tools HEAD `b9ac29a6`）：occlusion 0、p8 CLEAN ×10（keydiff [137–140,150]；en-zh-tw [137–139,150]）、spill 0、boxtitle 0、edge 0、creambox PASS、D5 census PASS、印/网文字层一致、KIT 33/33 一致。
- 注：二轮报告 §2.4/§7 已载明 en-ru 拉丁标题字体问题为已知跨家 D5 系统性问题（另有跨家工人统一修 svglib.py），不计入本轮发现；该问题随后由 fix-xru 修好（见 en-ru 节）。

## SHA-12 对照表（最后重校记录值 vs 当前磁盘实测）

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） | 对照 |
|---|---|---|---|---|
| en-zh-cn（core-en） | 30,110,585 / `5e9789d5f873` | 2,605,509 / `9283d6e6baab` | 51,573 / `e271f6cbfc44` | 一致 |
| en-de | 28,845,594 / `80e0746afc89` | 2,334,821 / `86438c44ceb8` | 52,736 / `2b2af27cc59b` | 一致 |
| en-es | 28,847,830 / `81e1cfb9f3b0` | 2,337,042 / `452a9d0f891a` | 54,556 / `cb334ba784ac` | 一致 |
| en-fr | 28,847,125 / `f18c64ee8913` | 2,336,319 / `18523f7b6177` | 53,974 / `cbe3b588d970` | 一致 |
| en-it | 28,841,732 / `0062f3d9b875` | 2,330,932 / `24ad7443e932` | 54,115 / `3d6c872ff631` | 一致 |
| en-ja | 35,187,926 / `068e2d9da3e5` | 2,713,215 / `e0ead68adf7a` | 53,756 / `2ccd31bee63d` | 一致 |
| en-ko | 30,159,302 / `dacad9cca89b` | 2,535,257 / `7c486f7d60aa` | 53,758 / `b5592fecb7af` | 一致 |
| en-nl | 28,842,162 / `eb6be63a6686` | 2,331,372 / `32e8baa51bf9` | 53,736 / `cbd9a008c530` | 一致 |
| en-pt | 28,850,391 / `eb347a545c8e` | 2,339,582 / `adc0a7e864db` | 54,291 / `1b3ee4558a75` | 一致 |
| en-ru | 28,991,765 / `7336fdd65c17` | 2,468,694 / `8ded0e80780b` | 62,552 / `13e0e75ce382` | **印/网变过**（见下） |
| en-zh-tw | 30,215,637 / `58112dca9caf` | 2,701,637 / `cd585a52bc57` | 51,321 / `63c7651e06e9` | 一致 |

（上表“最后重校记录值”取 PROOF-NOTE-2 §1；磁盘值由本次实测 `sha256sum` + `stat` 得出。10 版三件全一致；en-ru 仅印/网变过，text.md 未变。）

## 逐版结论

| 版 | 最后重校 | 磁盘对照 | 结论 |
|---|---|---|---|
| en-zh-cn（core-en） | 二轮 (a) CLEAN（2f96abe3） | 三 SHA 一致 | VERIFIED CLEAN |
| en-de | 二轮 (a) CLEAN | 三 SHA 一致 | VERIFIED CLEAN |
| en-es | 二轮 (a) CLEAN | 三 SHA 一致 | VERIFIED CLEAN |
| en-fr | 二轮 (a) CLEAN | 三 SHA 一致 | VERIFIED CLEAN |
| en-it | 二轮 (a) CLEAN | 三 SHA 一致 | VERIFIED CLEAN |
| en-ja | 二轮 (a) CLEAN | 三 SHA 一致 | VERIFIED CLEAN |
| en-ko | 二轮 (a) CLEAN | 三 SHA 一致 | VERIFIED CLEAN |
| en-nl | 二轮 (a) CLEAN | 三 SHA 一致 | VERIFIED CLEAN |
| en-pt | 二轮 (a) CLEAN | 三 SHA 一致 | VERIFIED CLEAN |
| en-ru | 二轮 (a) CLEAN，但随后重建 | 印/网 SHA 变过，text.md 一致 | 本人全新全量重校 → (a) CLEAN（见下） |
| en-zh-tw | 二轮 (a) CLEAN | 三 SHA 一致 | VERIFIED CLEAN |

## en-ru 全新全量重校（SOP §8，本人执行）

### 为什么重校

二轮重校（18:30 UTC）之后，*-ru 扫查（工人 09cda9c4，`scratch-sweep-xru-occl-1/SWEEP-LOG.md`，2026-11-13 ~01:15 UTC）在 en-ru 查出 boxtitle 3 处回归（P1 `Цифры` +8.5px、P5 `Цифры` +24.3px、P6 `Бюллетень` +11.4px；根因：fix-xru 把拉丁标题改走 Newsreader 后变宽）。修复工人 ff34ff71（`scratch-fix-en-ru2/FIX-LOG-boxtitle2.md`）只降三处标题字号（P1 23→22pt、P5 23→21pt、P6 23→22pt），措辞未动，仅 `svg/p1-front.svg`、`p5-youth.svg`、`p6-deep.svg` 三份变过，其余 5 份逐字节相同；text.md 重导出 diff 0 行。协调员已独立核实新 SHA 与门禁（run-log 2026-11-13 ~01:32 UTC）。因印/网 PDF 已重建，二轮 CLEAN 结论不再覆盖当前磁盘态，故按任务要求由本人做全新全量重校。

### 当前指纹（本次实测）

| 件 | 字节 | SHA-256（前 12） | 与 FIX-LOG-boxtitle2 / KIT §2 |
|---|---|---|---|
| 印 PDF `The-Lucerna-VOL4-en-ru.pdf` | 28,991,765 | `7336fdd65c17` | 一致 |
| 网 PDF `The-Lucerna-VOL4-en-ru.web.pdf` | 2,468,694 | `8ded0e80780b` | 一致 |
| text.md `2026-w47-en-ru.text.md` | 62,552 | `13e0e75ce382` | 一致（未变） |

### 机械门（只读重跑，`tools/venv/bin/python`，脚本 `run_gates_enru.sh`，输出 `tool-out/GATES-SUMMARY.txt`）

- occlusion_audit.py：selftest 通过（RC=0）；**0 flags**。
- p8.py extract：60/150（= core 集）；compare vs core-en：**CLEAN**，missing=[]，extra=0，keydiff=[137, 138, 139, 140, 150]（预期：翻译题 + 开放写作题按读者语不同）。
- spill_sweep.py：32 boxes，176 candidates，**0 SPILL**。
- boxtitle_check.py：42 titles / 397 body lines，**0 DEFECT，0 OBSERVE，0 marginal**——3 处回归全清。
- pdf_edge_scan.py：8 页，**0 TOUCH，0 NEAR**。
- d5_creambox_audit.py：P8 203 行，页脚空隙 36.3，**PASS 0 defects**。
- d5_census.py：**CENSUS PASS**（164 弯引号全在 Newsreader 内；拉丁/西里尔入 CJK 均为 0）。
- 印/网 PDF 文字层：**逐字节一致**（54,750 字节）。
- freeze baseline 未在本轮重跑：重建会重渲染整版；修复工人在此构建上已跑 freeze 8/8（FIX-LOG-boxtitle2.md），协调员已核实；本轮其余门禁全部重跑且全绿。head_check 未单列：修复工人记录两处已裁定接受的 HEAD TOO WIDE（P7 AN EXAMPLE LETTER、P8 `Понимание текста`，位于未动的 P7/P8 页，任务明令不动），本次未动它们。
- 22 个 PDF（全家）未重验页数；en-ru 两 PDF 均为 8 页（pdftoppm 渲染 8 页 + edge 扫描 8 页；KIT §2 亦记 8 页）。

### 文本通读（text.md 全文 1305 行，逐行读完）

- P1–P8 正文、练习与全部 150 个答案逐题核对题面/原文/图表/算术，**全部正确**。配对题复核：P2 D（24 b / 25 c / 26 a / 27 d）、P3 D（38 b / 39 a / 40 d / 41 c）、P4 D（56 b / 57 c / 58 d / 59 a）、P5 D（74 d / 75 a / 76 b / 77 c）、P8 F（141 b / 142 c / 143 d / 144 a），均与题面定义顺序一致。
- 算术复核：254+162+19=435；254−218=36；20+13=33；254/162/19、20/13/2 全家一致。
- 答案编号：150 条，1–150 连续无断号（`## Answers` 段后精确计数与全文扫描一致）。
- P7 金句 8 句逐字核对均出自本期正文（P1×2、P2、P3、P4、P5、P6×2），页码标注正确。
- P1 目录与 P2–P8 标题/级别一致（A2、A2→B1、B1、B1、B2、A2→B2）。
- 讲解层（俄语 gloss/译文/答案注释）逐项对照正文，无错译、无孤儿注释；翻译题 137–140 俄译正确。
- ABSTRACT.txt：单行、俄语，含真实主题事实 + 刊名 + 目标语 + A2–B2 + 150 练习，无模板套话。
- 日历（America/Toronto，`date` 核查）：Tue 2026-11-03、Sun 2026-11-08、Mon 2026-11-09、Thu 2026-11-26（感恩节，第 4 个周四）、Fri 2026-11-27、Mon 2026-11-16、Fri 2026-11-20、Sat 2026-11-21、Sun 2026-11-22、Tue 2026-12-01。纸面星期全部吻合。

### 修复核实（F1/F2/F3 + boxtitle fix2 + fix-xru）

- F1（Georgia 决胜轮，11 版级，本版亦然）：text.md P2/P6 新措辞在位（`Ossoff won reelection` 2 处；P2 `so there is no runoff`、P6 `so there was no runoff`）；旧句（`If no candidate wins a majority in Georgia's Senate race, there is a runoff on December 1` 及 P6 旧句）在 text.md 与印 PDF 文字层均为 0。印 PDF P2/P6 目视亦为新措辞。Q13/Q142 规则题答案未受影响。
- fix1 D1（P1 SEARCHES 框 gloss）：`Относительный интерес, не точные.` 在位。
- boxtitle fix2 三处：P1 `THE WEEK IN NUMBERS　Цифры`、P5 `ODD SOCKS, IN NUMBERS　Цифры`、P6 `A PRACTICE BALLOT　Бюллетень`——boxtitle 工具 0 DEFECT；P1/P5/P6 整页目视标题均在奶油框内，无溢出。
- fix-xru（拉丁标题走 Newsreader）：D5 census PASS（LAT@NotoSans=0）；印 PDF P1 头条 `DEMOCRATS WIN BOTH HOUSES!` 目视正常。

### 8 页逐页看图（100dpi 全页渲染，`page-{1..8}.png`）

P1–P8 逐页目视：刊头、页脚（`Страница N из 8`）、图片与图注（国会大厦、火鸡 Audubon、Rousseau 虎、W. G. Grace、Lawrence 童工 1912、投票亭、Samuel Johnson、Library of Congress 阅览室）均完整，无溢出/重叠/压页脚/豆腐块/截断句。P5 D 节标题跨栏断行（栏尾 `D PRESENT CONTINUOUS` + 次栏顶续行）为模板流式行为，D78–81 全在版，非缺陷。P8 答案区 150 键全在版，范文框完整。

### 结论：(a) CLEAN——零问题

本轮从头全量重校（text.md 全文 1305 行 + 150 答案逐题 + 事实/日期复核 + 机械门 8 门全绿 + 印/网文字层逐字节一致 + 8 页逐页目视）未发现任何 MAJOR / MEDIUM / low 问题。en-ru 当前磁盘态 **VERIFIED CLEAN**。

### 观察项（非缺陷，记入报告、不修）

- **O1（Q109，Error Clinic）**：题干 `"The count continue after the vote." (wrong tense)`，答案键为 `The count continued after the vote.`。该改法语法成立；但本期正文多处写计数仍在继续（P2 `The counting continues`、P6 `the counting goes on`），按正文口径更自然的改法是 `continues`。两轮前序全量重校均未列为问题；本次重校亦不将其定为缺陷（语法正确、非重建引入）。交协调员裁定是否记为 polish 项；**不拦定稿，不修**。
- 范文 MODEL 词数：按破折号计词为 84 词（80–100 要求内），不计破折号约 82 词，两种口径均在要求内；与 de 家 M1 同类计数口径问题（已知工具债），非缺陷。

## KIT §7 SHA 核对（wave-2 清单）

逐版核对 KIT 内记录的印/网/text.md 完整 SHA-256（64 位）与磁盘实测：

| 版 | KIT 印 SHA | KIT 网 SHA | KIT 文 SHA | 备注 |
|---|---|---|---|---|
| en-zh-cn | OK | OK | OK | SHA 在 §7 Build/repro（F1 bullet） |
| en-de | OK | OK | OK | SHA 在 §7 Build/repro |
| en-es | OK | OK | OK | SHA 在 §7 Build/repro |
| en-fr | OK | OK | OK | SHA 在 §7 Build/repro |
| en-it | OK | OK | OK | SHA 在 §2 Files delivered |
| en-ja | OK | OK | OK | SHA 在 §2 Files delivered |
| en-ko | OK | OK | OK | SHA 在 §2 Files delivered |
| en-nl | OK | OK | OK | SHA 在 §2 Files delivered |
| en-pt | OK | OK | OK | SHA 在 §2 Files delivered |
| en-ru | OK | OK | OK | SHA 在 §2 Files delivered（已更新为 fix2 新值 `7336fdd6…`/`8ded0e80…`/`13e0e75c…`） |
| en-zh-tw | OK | OK | OK | SHA 在 §2 Files delivered |

（各版 KIT 章节编号不统一：core-en/de/es/fr 的 SHA 表在 §7，余版在 §2；均已逐版定位核对。）

**wave-2 清单：无待修项。** 11 版 KIT SHA 全部与磁盘一致，无过期 SHA。

## 待修清单

无。无阻塞项、无须修复项。仅上述 O1 观察项 1 条（非缺陷，交协调员裁定）。
