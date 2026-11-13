# W47 en 家庭独立重校 PROOF-NOTE（第二轮，SOP §8/§8.4）

- 校对员：独立重校第二轮（全新工人，与建造者、第一轮校对员、修复者均不同，满足“另派”要求），2026-11-12
- 范围：目标语 en，读者母语 de / es / fr / it / ja / ko / nl / pt / ru / zh-cn / zh-tw，共 11 版
- 刊期：2026 年 11 月 16–22 日，VOL.4
- 结论：**(a) 干净——零问题。** 第一轮 3 条低严重度（F1/F2/F3）已核实修复到位；本轮从头全量重校未发现任何新问题（无 MAJOR、无 MEDIUM、无 low）。详见 §6。
- 本文件只记录校对结论，不做任何修复。未改动任何生产文件，未 commit/push，未跑 lint。

## §0 枚举与目录核对

盘上目录 11 个，与任务范围一致，无多无少：

- `production/2026-w47/core-en/` = en-zh-cn 版（`2026-w47-en-zh-cn.text.md` + 印/网 PDF）；无单独的 `2026-w47-en-zh-cn` fan-out 目录，无重复 slug。
- fan-out 10 个：`2026-w47-en-de/es/fr/it/ja/ko/nl/pt/ru/zh-tw`。
- 每版含：`<slug>.text.md`、`ABSTRACT.txt`、印 PDF（`The-Lucerna-VOL4-en-<native>.pdf`）、网 PDF（`.web.pdf`）、`WEEKLY-KIT.md`、`svg/`（p1–p8）、`cards/`（8 张整页 PNG）。
- 22 个 PDF 均为 8 页（PyMuPDF 核查，见 §2.8）。
- 磁盘门：开工 94G/150G，收尾 95G/150G，均低于 100G 门限，未停手。

## §1 校对文件清单（尺寸 + SHA-256 前 12 位，即本次校对的那份文件）

全部 11 版指纹与 FIX-LOG 终验值逐版一致（修复后文件未再变动），且与各版 WEEKLY-KIT §2 记录一致（11/11，见 §2.9）。

| 版 | 印 PDF（字节 / SHA-12） | 网 PDF（字节 / SHA-12） | text.md（字节 / SHA-12） |
|---|---|---|---|
| en-zh-cn（core-en） | 30,110,585 / `5e9789d5f873` | 2,605,509 / `9283d6e6baab` | 51,573 / `e271f6cbfc44` |
| en-de | 28,845,594 / `80e0746afc89` | 2,334,821 / `86438c44ceb8` | 52,736 / `2b2af27cc59b` |
| en-es | 28,847,830 / `81e1cfb9f3b0` | 2,337,042 / `452a9d0f891a` | 54,556 / `cb334ba784ac` |
| en-fr | 28,847,125 / `f18c64ee8913` | 2,336,319 / `18523f7b6177` | 53,974 / `cbe3b588d970` |
| en-it | 28,841,732 / `0062f3d9b875` | 2,330,932 / `24ad7443e932` | 54,115 / `3d6c872ff631` |
| en-ja | 35,187,926 / `068e2d9da3e5` | 2,713,215 / `e0ead68adf7a` | 53,756 / `2ccd31bee63d` |
| en-ko | 30,159,302 / `dacad9cca89b` | 2,535,257 / `7c486f7d60aa` | 53,758 / `b5592fecb7af` |
| en-nl | 28,842,162 / `eb6be63a6686` | 2,331,372 / `32e8baa51bf9` | 53,736 / `cbd9a008c530` |
| en-pt | 28,850,391 / `eb347a545c8e` | 2,339,582 / `adc0a7e864db` | 54,291 / `1b3ee4558a75` |
| en-ru | 29,097,780 / `9e503c053878` | 2,573,323 / `8875c5599472` | 62,552 / `13e0e75ce382` |
| en-zh-tw | 30,215,637 / `58112dca9caf` | 2,701,637 / `cd585a52bc57` | 51,321 / `63c7651e06e9` |

## §2 机械门（tools/ HEAD `b9ac29a6`，工作树干净；解释器一律 `tools/venv/bin/python`）

本轮全部只读重跑（未重建、未改动生产文件）。`occlusion_audit.py --selftest` 先行通过（6 类 planted 缺陷全部触发，clean 对照静默）。逐版汇总见下表；完整输出在 `tool-out/`（`GATES-SUMMARY.txt` + 各门日志/JSON）。

### 2.1 几何遮挡审计 `tools/occlusion_audit.py`（每版，含 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX）

- **0 flags，全部 11 版。**

### 2.2 P8 比对 `tools/p8.py compare --total 150`（core vs 10 fan-out）

- **CLEAN × 10**：core 60 noted / edition 60 noted，missing=[]，extra=0，uncertain=[]。
- keydiff=[137, 138, 139, 140, 150]（每版皆同）：翻译题（137–140）与开放写作题（150）的印出 key 按读者语言不同，属设计如此，非缺陷。en-zh-tw 为 [137, 138, 139, 150]（缺 140 为本版固有，pre-fix 校对亦同，非回归）。

### 2.3 spill / boxtitle / edge 三门

- spill_sweep：**0 SPILL，全部 11 版**（OBSERVE 138–175/版）。
- boxtitle_check：**0 DEFECT，全部 11 版**（28–45 titles/版）。
- pdf_edge_scan：**0 TOUCH，0 NEAR，全部 11 版**（8 页/版）。

### 2.4 D5 普查（SOP §1.1 字体表；`d5_census.py` + `d5_creambox_audit.py`）

- 弯引号（U+201C/U+201D；U+2019 在本家三层均为 0，见 §7 注）：core-en 166 个、en-nl 168 个、其余 9 版各 164 个，**全部位于 Newsreader 元素内，0 个位于 Noto Sans CJK 内**。
- `d5_creambox_audit.py`（pre-fix 基线差分）：**PASS，全部 11 版**（P8 行数与页脚空隙与基线一致，0 defects）。
- 全量 `<text>` 均带显式 font-family；字体集与第一轮一致（Newsreader / Noto Sans CJK SC·TC·JP / Noto Serif CJK SC·TC·JP / UnifrakturMaguntia / DejaVu Sans 仅 P6 四个 ☐ 选票框 / Noto Sans 仅 en-ru 讲解层）。
- en-ru 版拉丁标题用 Noto Sans 而非 Newsreader：**已知跨家 D5 系统性问题，另有跨家工人统一修 svglib.py，按任务要求不计入本轮发现**（本版内容照常校对，无其他问题）。

### 2.7 逐版门禁汇总表

| 版 | occlusion | p8 compare | spill (OBSERVE) | boxtitle (titles/body) | edge (TOUCH/NEAR) | creambox (P8 行/页脚空隙) | census 弯引号 (Newsreader 内) | 印/网文字层 |
|---|---|---|---|---|---|---|---|---|
| en-zh-cn（core-en） | 0 flags | —（core 本身） | 0 SPILL (140) | 0 DEFECT (30/250) | 0/0 | PASS (191/41.1) | 166/166 | 一致 (48,166 B) |
| en-de | 0 flags | CLEAN [137–140, 150] | 0 SPILL (146) | 0 DEFECT (30/185) | 0/0 | PASS (189/35.9) | 164/164 | 一致 (48,677 B) |
| en-es | 0 flags | CLEAN [137–140, 150] | 0 SPILL (150) | 0 DEFECT (32/184) | 0/0 | PASS (202/37.3) | 164/164 | 一致 (49,599 B) |
| en-fr | 0 flags | CLEAN [137–140, 150] | 0 SPILL (145) | 0 DEFECT (28/189) | 0/0 | PASS (191/35.9) | 164/164 | 一致 (49,463 B) |
| en-it | 0 flags | CLEAN [137–140, 150] | 0 SPILL (147) | 0 DEFECT (34/181) | 0/0 | PASS (192/37.8) | 164/164 | 一致 (49,187 B) |
| en-ja | 0 flags | CLEAN [137–140, 150] | 0 SPILL (147) | 0 DEFECT (30/269) | 0/0 | PASS (185/34.6) | 164/164 | 一致 (49,871 B) |
| en-ko | 0 flags | CLEAN [137–140, 150] | 0 SPILL (175) | 0 DEFECT (45/379) | 0/0 | PASS (184/37.6) | 164/164 | 一致 (49,760 B) |
| en-nl | 0 flags | CLEAN [137–140, 150] | 0 SPILL (149) | 0 DEFECT (32/183) | 0/0 | PASS (178/35.9) | 168/168 | 一致 (49,209 B) |
| en-pt | 0 flags | CLEAN [137–140, 150] | 0 SPILL (148) | 0 DEFECT (32/185) | 0/0 | PASS (192/37.8) | 164/164 | 一致 (49,338 B) |
| en-ru | 0 flags | CLEAN [137–140, 150] | 0 SPILL (152) | 0 DEFECT (34/238) | 0/0 | PASS (203/36.3) | 164/164 | 一致 (54,799 B) |
| en-zh-tw | 0 flags | CLEAN [137–139, 150] | 0 SPILL (138) | 0 DEFECT (30/251) | 0/0 | PASS (182/35.6) | 164/164 | 一致 (47,885 B) |

### 2.8 编号、页数与文本层

- 每版 text.md 答案段：150 条，1–150 连续无断号（`## Answers` 段后精确计数；全文 `^\d+\. \[` 158 行 = 答案 150 + P8 完形选项行 112–119 的 8 行）。
- 22 个 PDF 均为 8 页；印/网 PDF 文本层每版字节完全相同（47,885–54,799 字节/版）；text.md 与印/网 PDF 均 0 行 U+FFFD。
- 范文 MODEL：84 词（80–100 要求内），覆盖全部四个提示点（奇袜、电视丛林、选举阅读、周五电影）。

### 2.9 KIT 指纹核对

- 11 版 ×（印 PDF / 网 PDF / text.md）SHA-256 前 12 位 + 字节数，**全部与各版 WEEKLY-KIT §2 记录一致（33/33）**。

## §3 文本通读

- core-en `text.md` 全文通读（1–1305 行）：P1–P8 正文、练习与全部 150 个答案逐题核对题面/原文/图表/算术。**全部正确**（题型分布与第一轮一致：P1 TRY IT NOW 1–6、Lightning Quiz 7–10；P2 A 11–15、B 16–19、C 20–23、D 配对 24–27；P3 A 28–33、B 34–37、C 38–41、D 42–45；P4 A 46–51、B 52–55、C 56–59、D 60–63；P5 A 64–69、B 70–73、C 74–77、D 78–81；P6 A 图表 82–87、B 88–93、C 94–99；P7 drills 100–107、error clinic 108–111；P8 完形 112–119、MC 120–128、阅读 129–132、句型 133–136、翻译 137–140、配对 141–144、对话 145–149、写作 150 开放题）。
  - 算术复核：254+162+19=435；254−218=36；33/35 参议院席位已宣布（20 D + 13 R + 2 未宣布）；20+13=33。
  - P7 金句与所引页逐字核对无误（8 句，P1/P2/P3/P4/P5/P6 各有出处）。
  - P1 "IN THIS ISSUE" 目录与 P2–P8 标题/级别一致（A2、A2→B1、B1、B1、B2、A2→B2）。
  - 配对题答案复核：P2 D（24 b / 25 c / 26 a / 27 d）、P3 D（38 b / 39 a / 40 d / 41 c）、P4 D（56 b / 57 c / 58 d / 59 a）、P5 D（74 d / 75 a / 76 b / 77 c）、P8 F（141 b / 142 c / 143 d / 144 a）——均与题面定义顺序一致。
- 讲解层：10 个 fan-out 与 core 的 diff（每版 267 行改动；zh-tw 251 行，余 16 行因简繁脚本相同）**全文通读**。全部 gloss、译文、答案注释、日期与星期核对无误；答案 key（字母/数字/词形）在各版与 core 完全一致，改动仅限括号内注释与题型标签的读者语翻译。翻译题 137–140 各版译文正确（de/fr/es/it/pt/nl/ru/ja/ko/zh-tw 全读）。
- ABSTRACT.txt：11 版全读，均为单行、读者母语，含主题事实 + 刊名 + 目标语 + A2–B2 + 150 练习，无模板套话。

## §4 事实核验（复核第一轮 §4 的网上核查结论 + 本轮独立抽查）

第一轮已逐项网上核实为真的事实，本轮通读中未发现任何与之矛盾的改动（核心文本除 F1 两行外与校对件相同，见 §5；F1 新措辞本身即为事实修正）。本轮独立复核要点：

- 日历（America/Toronto，`date` 核查）：Tue 2026-11-03、Sun 2026-11-08、Mon 2026-11-09、Tue 2026-11-10、Fri 2026-11-13、Sun 2026-11-15、Mon 2026-11-16、Wed 2026-11-18、Thu 2026-11-19、Fri 2026-11-20、Sat 2026-11-21、Sun 2026-11-22、Thu 2026-11-26（感恩节，第 4 个周四）、Fri 2026-11-27、Tue 2026-12-01、Fri 2026-12-18。纸面星期全部吻合。
- Georgia 新措辞事实：AP 于 2026-11-03 晚宣布 Ossoff 连任，约 59% 对 41%（Collins），已过半数，无需决胜轮——与 P2/P6 新措辞一致。
- 选举数字：众议院 254 D / 162 R / 19 未宣布（11 月 8 日快照，纸面明确标注并提示数字会变）；参议院 20 D / 13 R / 2 未宣布（阿拉斯加、密西西比）；7 席翻转（Iowa、Kansas、Maine、North Carolina、Ohio、South Carolina、Texas）；5 位州长翻转（Georgia、Iowa、Nevada、Ohio、Texas）；选前众议院 218 R / 214 D；参议院 53–47；36 场州长选举；35 个参议院席位；新国会 2027 年 1 月 3 日就职（纸面写“一月”，未写具体日，无误）。
- 其余事实（Ashes、ATP Finals、I'm a Celebrity、Hunger Games、Anti-Bullying Week、Premier League、NFL、认证窗口、Mike Johnson）与第一轮核查结论一致，通读中无矛盾处。

## §5 修复核实（逐版，FIX-LOG 所称修复确实在版）

### F1（Georgia 决胜轮，11 版）——已修 ✓

- 精确旧句核查（非短语，避免误读）：P2 旧句 `If no candidate wins a majority in Georgia's Senate race, there is a runoff on December 1.` 与 P6 旧句（含 `…goes to a runoff on December 1. Mississippi…`）在 **11 版 text.md 与 11 版印 PDF 文字层（归一化单行）均为 0/0**。
- 新措辞在版：text.md 每版 `Ossoff won reelection` 2 处（P2+P6）、`so there was no runoff` 1 处（P2）、`so there is no runoff` 1 处（P2 另一句）；印 PDF 文字层每版 `Ossoff` 2 处。
- 新措辞原文（P2）：“Georgia law calls for a runoff on December 1 only if no candidate wins a majority — but Jon Ossoff won reelection with about 59% of the vote, so there is no runoff.”（P6）：“In Georgia, a Senate race with no majority winner goes to a runoff on December 1 — but this time Jon Ossoff won reelection with about 59% of the vote, so there was no runoff.”
- 练习不受影响：Q13 答案仍为 `1 (决胜轮 12 月 1 日)`、Q142 配对仍为 runoff，均为规则题，答案正确。

### F2（en-fr P7 `le passé simple`→`le prétérit`）——已修 ✓

- en-fr text.md：`passé simple` 0 处、`prétérit` 3 处（P7 注释 :775 + P3/P4 练习指令 :407/:511 一致）；印 PDF 文字层同为 `passé simple` 0 处、`prétérit` 3 处。

### F3（en-zh-tw 答案 13 `決勝輪`→`第二輪投票 12 月 1 日`）——已修 ✓

- en-zh-tw text.md：`決勝輪` 0 处；:1031 已为 `13. [A2] 完成句子 — 1 (第二輪投票 12 月 1 日)`，与本版 P2/P6 gloss 及答案 21/24/142 的 `第二輪投票` 一致。

## §6 发现的问题

**零条。本轮从头全量重校未发现任何 MAJOR / MEDIUM / low 问题。**

## §7 曾核查、判定为非缺陷的项（不计入问题）

- FIX-LOG 末节已裁定不修的项：无新增（FIX-LOG 未列不修项；本轮亦无需要裁定的项）。
- en-ru 版拉丁标题字体问题（拉丁文用 Noto Sans 而非 Newsreader）：已知跨家 D5 系统性问题，另有跨家工人统一修 svglib.py，按任务要求不作为本轮发现；en-ru 版内容照常校对，无其他问题。
- de 版 «…» 法式引号（瑞士式，全版一致）；it 版答案 2 "proclamare" 对 P1 "annunciare"（同义变体）；pt 版 "ODD SOCKS, IN NUMBERS · N.º" 简略与 "coisas a acontecer agora" 欧葡进行时简写；fr 版 "Thanksgiving = Thanksgiving d" gloss；es 版 "Misisipi"（RAE 拼法）；nl 版 "bekrachtigen" 译 certify；ru 版 "Эшес"、"Поиски недели"、"a seat = мандат"；ja/ko 音译均标准（レイフ・ファインズ、레이프 파인스、ヘイミッチ、애시스、ジョゼフ・ザダ、조지프 자다 等）。以上与第一轮 §7 一致，本轮复核仍接受。
- 纸面 "ITV has not confirmed the campmates yet" 在 11 月 9 日截稿日时为真（名单 11 月 11–12 日才确认），不算缺陷。
- en-nl P8 版式为另一合法重排（Q121 落在第 1 栏底部、Q122 起第 2 栏顶部，137/138 在第 3 栏底部），内容齐全有序，非缺陷。
- P3/P4/P5/P6 栏尾留白为模板流式行为（与 W46 相同），KIT 已注明接受。
- it/nl/pt 三版印 PDF 文字层刊期行提取为字母间空格（`W E E K O F N O V E M B E R 1 6 TO 2 2 , 20 2 6`）：pdftotext 对字距拉宽行的提取伪影；目视 en-it P1 卡片，刊期行正常显示为 "WEEK OF NOVEMBER 16 TO 22, 2026"，非缺陷。
- 撇号：text.md、SVG、印 PDF 三层一致使用直撇号（`president's`、`I'm a Celebrity` 等），弯撇号 U+2019 三层均为 0；弯引号仅为双引号 “ ”（text.md 每版 81–85 对，SVG 普查 164–166 个全在 Newsreader 内）。三层一致，非缺陷。
- 占位词扫描：`TODO|FIXME|XXX|lorem|placeholder|占位|待写|TBD` 全版 0 真命中（es/pt 的 "todo/sobretudo" 为子串误报）。
- P8 完形 Q117 key 为 "will certify"：题干 "states ___ their counts by December 18" 亦可接受现在时，但出题意图为将来时，key 明确且与 P2 练习 Q17 一致；第一轮亦通过，非缺陷。
- P4 "ONE SCREEN, TWO SCREENS" 侧栏在各版译作足球/比赛英语（如 it "Inglese del calcio"、de "Fußball-Englisch"）：侧栏例句确为足球短句，标签合理，非缺陷。

## §8 版式目视（抽查）

- en-it P1、en-fr P8、en-zh-tw P1 三张整页卡片全页目视：刊头 + 配对徽章、页脚配对标注、D5 盒标题、P8 答案流与 MODEL 框、图片与图注均完整，无溢出/重叠/压页脚/豆腐块/截断句。
- 其余 85 页由机械门覆盖：occlusion 0 flags + spill 0 + boxtitle 0 + edge 0 + creambox PASS（§2），与第一轮全量 88 页目视结论一致（第一轮已全量看图零缺陷；本轮重建后机械门全部重跑绿）。

## §9 结论

- **(a) 干净：零问题。** 第一轮 3 条低严重度（F1/F2/F3）已核实全部修复到位（§5）；本轮从头全量重校（核心全文 + 10 版讲解层 diff 全文 + 150 答案逐题 + 事实复核 + 机械门 11 版全绿 + text.md/PDF 一致性抽查 + 版式抽查）未发现任何新问题。
- 无中/高严重度问题；无事实硬伤；无版式缺陷；P8 答案 150/150 逐题复核正确；D5 字体缺陷已清除（§2.4，en-ru 拉丁标题字体除外，另案处理）。
- 本校对未修复任何内容，未改动任何生产文件，未 commit/push，未跑 lint；除本文件与 `tool-out/` 内审计输出外，未在 production/2026-w47/ 内写入任何内容。
- 支撑文件：`tool-out/GATES-SUMMARY.txt`、`tool-out/occlusion-*.json`、`tool-out/p8-*.json`、`tool-out/p8-extract-*.json`、`tool-out/spill-*.log`、`tool-out/boxtitle-*.log`、`tool-out/edge-*.log`、`tool-out/creambox-*.json`、`tool-out/census-*.json`、`tool-out/print-*.txt` / `web-*.txt`（印/网 PDF 文字层）、`tool-out/diff-en-*.txt`（10 份讲解层 diff）、`tool-out/diff-new-en-*.txt`（10 份讲解层新侧全文）、`run_gates.sh`（只读门禁脚本）。
