# W47 en 家庭修复 FIX-LOG（接替工人 c042f65c，2026-11-12）

- 范围：目标语 en，读者母语 de / es / fr / it / ja / ko / nl / pt / ru / zh-cn / zh-tw，共 11 版（目录 `2026-w47-en-*` 10 个 + `core-en` = en-zh-cn 版）。
- 缺陷来源：独立重校 PROOF-NOTE（`hidden_files/w47/scratch-reproof-w47-en/PROOF-NOTE.md`），3 条低严重度：F1（11 版，Georgia 决胜轮写成待定）、F2（en-fr，:775 `le passé simple`）、F3（en-zh-tw，:1031 答案 `決勝輪`）。
- 上一任：118ea848，运行时重启中断，无 FIX-LOG；本日志从头写完整记录。
- 约束：只在 `production/2026-w47/` 内工作，只动 en 家 11 版目录；不 commit、不 push、不跑 lint；解释器一律 `tools/venv/bin/python`；`svglib.py` 字体路由一律不动；磁盘门限已用 ≥100G 立即停手。
- 复用上一任工具（已核实可用）：`scratch-fix-en/fix_build.sh`、`make_textmd_fix.py`、`pre-reg/`、`pre-svg/`、`tmp/`（pre-fix text.md / print 层快照）、`logs/`（各版门禁日志）、`scratch-fanout-en/backup/`（creambox 基线）。

## 接手核实（2026-11-12 13:xx UTC 开工，上一任中断时状态）

方法：逐版指纹（印/网 PDF + text.md 尺寸 + SHA-256，与 PROOF-NOTE §1 表逐版对照）；每版分别查 F1 旧句（精确句式，非短语）在印 PDF 文字层与 text.md 是否仍在；F2（en-fr）、F3（en-zh-tw）同法。旧句精确式：P2 `If no candidate wins a majority in Georgia's Senate race, there is a runoff on December 1.`；P6 `…goes to a runoff on December 1. Mississippi…`（无 `— but this time` 从句者为旧句）。注意：新措辞仍含 `runoff on December 1` 短语 2 处，故只查该短语会误判——协调员“en-fr 与 core-en 的 text.md 仍各含 2 处”即为此误读，实测两版旧句均为 0。

### 指纹对照（PROOF-NOTE §1 → 接手时盘上值；✓=与校对值相同，✗=已变）

| 版 | 印 PDF | 网 PDF | text.md | 结论 |
|---|---|---|---|---|
| core-en（en-zh-cn） | 99dad9f2ed37 → 5e9789d5f873（30,110,194→30,110,585）✗ | 801597efe2c8 → 9283d6e6baab（2,605,120→2,605,509）✗ | 23855d4bd60a → e271f6cbfc44（51,402→51,573）✗ | 已重建 |
| en-de | c7b8f20d9b5a → 80e0746afc89（28,845,194→28,845,594）✗ | e18adeb766be → 86438c44ceb8（2,334,418→2,334,821）✗ | c16f0e473f80 → 2b2af27cc59b（52,565→52,736）✗ | 已重建 |
| en-es | 78a9edee2ea3 → 81e1cfb9f3b0（28,847,427→28,847,830）✗ | 0b1c2088a6be → 452a9d0f891a（2,336,646→2,337,042）✗ | 314b32a3c3f2 → cb334ba784ac（54,385→54,556）✗ | 已重建 |
| en-fr | abb14dde411a → f18c64ee8913（28,846,712→28,847,125）✗ | bae85a681966 → 18523f7b6177（2,335,922→2,336,319）✗ | ed8fd9ec8b70 → cbe3b588d970（53,806→53,974）✗ | 已重建 |
| en-it | 7efa726326ac → 0062f3d9b875（28,841,334→28,841,732）✗ | 681f6184d35e → 24ad7443e932（2,330,533→2,330,932）✗ | a83306257076 → 3d6c872ff631（53,944→54,115）✗ | 已重建 |
| en-ja | 2da138556847 → 068e2d9da3e5（35,187,539→35,187,926）✗ | e880d0c9370a → e0ead68adf7a（2,712,817→2,713,215）✗ | 2d498e4e9b99 → 2ccd31bee63d（53,585→53,756）✗ | 已重建 |
| en-ko | aef89be3f6bb → dacad9cca89b（30,158,892→30,159,302）✗ | e5ca78436649 → 7c486f7d60aa（2,534,848→2,535,257）✗ | 08d87476b499 → b5592fecb7af（53,587→53,758）✗ | 已重建 |
| en-nl | ac22842fe938 → eb6be63a6686（28,841,767→28,842,162）✗ | ec2c820e7326 → ec2c820e7326（2,330,974）✓ | 30bfb6f93860 → cbd9a008c530（53,565→53,736）✗ | **半截**：run/head/textmd/render 已做（13:25–13:28），webpdf 中断（log 仅 16 行、停在字体清单，网 PDF 文件 mtime 仍为 09:16 旧件）；门禁只跑到 render，未跑 webpdf 及之后 |
| en-pt | 4ecc163c3c66 ✓（28,850,005） | dbc0fefb64ab ✓（2,339,191） | f85c55cef1cf ✓（54,120） | 未动 |
| en-ru | e8c2cc4ef238 ✓（29,097,398） | f50ae8fc638c ✓（2,572,948） | 78c1b137e665 ✓（62,381） | 未动 |
| en-zh-tw | 44dcb76d240a ✓（30,215,246） | 6353e4506947 ✓（2,701,246） | cf12ebfe88d7 ✓（51,144） | 未动 |

### 缺陷逐版核实（接手时）

- F1（P2+P6 旧句，text.md / 印 PDF 文字层）：
  - core-en、en-de、en-es、en-fr、en-it、en-ja、en-ko、en-nl：text.md 旧句 0/0，新措辞 `Ossoff won reelection` 2 处（P2+P6）、`so there was no runoff` 1 处；印 PDF 文字层旧句 0/0（归一化单行文本核查；pdftotext 栏间交错会拆散 `won reelection`，以 `Ossoff` 计数 2 处为准，两新句均在层内）。**F1 已修。**
  - en-pt、en-ru、en-zh-tw：text.md 旧句各 1/1，新措辞 0；印 PDF 仍为校对件（SHA 未变），旧句仍在（en-pt 印层 P2 旧句因栏间交错拆散，但 `runoff on December 1` 与 `Georgia's Senate race` 均在层内；en-zh-tw 印层 P2/P6 旧句均可直接匹配）。**F1 仍开。**
- F2（en-fr）：源头 `content7.py:34` 已是 `le prétérit`；text.md :775 `past simple = le prétérit …`，:407/:511 一致；印 PDF 文字层 `passé simple` 0 处、`prétérit` 3 处。**F2 已修**（源头+重建+重导出均已落地）。
- F3（en-zh-tw）：源头 `content12.py:257` 已是 `第二輪投票 12 月 1 日`；但 text.md :1031 仍为 `13. [A2] 完成句子 — 1 (決勝輪 12 月 1 日)`，印 PDF 仍为校对件；印层 P8 答案 13 只印 `13. 1`（注语不进 P8 印出 key），故 F3 仅存于 text.md 附录答案行 + registry 注语。**F3 仍开（只差重渲染+重导出）。**
- 源头核查：F1 新措辞已在 11 版全部 `content12.py:171`（P2）与 `content56.py:103`（P6）到位（含未重建的 en-pt/en-ru/en-zh-tw）；F2 源头（en-fr `content7.py:34`）、F3 源头（en-zh-tw `content12.py:257`）均已到位。上一任已把全部源头改完，只差 4 版的重建。
- 已完成 7 版的门禁（上一任日志 `logs/<slug>/GATES-SUMMARY.txt` 尾行）：core-en、en-de、en-es、en-fr、en-it、en-ja、en-ko 均为 `OVERALL: ALL-GREEN`（core-en 注：creambox 首跑因 harness 备份缺 `assets/` symlink 失败，重跑 PASS，其余门全绿）。
- KIT 未更新：11 版 KIT §2/§7 仍记校对值（如 en-de KIT mtime 仍为 07:52，印 `c7b8f20d…`、网 `e18adeb7…`、text `c16f0e47…`）。待全部重建完成后统一按盘上实际 SHA 更新。
- Q13/Q142 不受影响（已核实 core-en text.md）：答案 13 仍为 `1 (决胜轮 12 月 1 日)`、142 仍为 `c (runoff=决胜轮 c)`；text.md diff 仅 :185 与 :651 两行正文改动，答案附录零改动。
- 磁盘：接手时已用 93G/150G（< 100G 门限），可开工。

### 待补工作（只补仍开着的口子）
1. en-nl：整套 `fix_build.sh` 重跑一遍（幂等；run/textmd/render 会重做，webpdf + 全部门禁补齐）。
2. en-pt、en-ru、en-zh-tw：整套 `fix_build.sh` 各跑一遍（F1；en-zh-tw 另含 F3）。
3. 11 版 KIT 按盘上实际 SHA 更新（§2/§7 印/网 PDF 字节+SHA、text.md 字节+SHA、文字层字符数）+ 各记一条修复 bullet。
4. 终验：11 版指纹重测 + F1/F2/F3 旧句全版清零核查 + 门禁汇总。

## 修复实施（第二接替工人 e718edf9，2026-11-12）

**接手时盘上实况与任务前提的出入**：FIX-LOG「接手核实」写于 13:55（mtime 13:55:47），其后 c042f65c 在被重启中断前已把 4 版补做全部跑完——`logs/` 下 4 份 `*-driver-takeover.log`（en-nl 14:10:35、en-pt 14:30:05、en-ru 14:49:49、en-zh-tw 15:13:48）均为 `OVERALL: ALL-GREEN`，4 版印/网 PDF 与 text.md 指纹均已变（见下表）。本工人未重复跑 fix_build.sh（已绿的重跑只耗磁盘/时间）；工作为：逐版复核门禁日志与 text.md diff（确认只含意改行、无标题丢失）、补 2 版未更新的 KIT（en-ru、en-zh-tw；其余 9 版 KIT 已由 c042f65c 于 15:23–15:29 更新并逐版验过 SHA+字节）、终验（11 版指纹重测 + F1/F2/F3 旧句清零 + 门禁汇总）。

### 逐版 fix_build.sh 运行记录（c042f65c 执行，driver-takeover 日志）

| 版 | 运行窗口（UTC） | RC | 门禁结果 |
|---|---|---|---|
| en-nl | 13:56:10–14:10:35 | 0 | run TOTAL 150 MODEL 82, 0 overflow；head_check PASS；text.md diff 4 行（:185/:651，仅 F1）；registry diff 0；render RC=0；webpdf RC=0（2,331,372 B，49,209 text bytes）；occlusion 0 flags（selftest OK）；p8 extract 60/150，compare CLEAN，keydiff=[137,138,139,140,150]；freeze baseline 8/8，diff added CJK 9 / Latin 361；spill 0（149 OBSERVE）；boxtitle 0（32 titles，183 body lines）；edge 0 TOUCH 0 NEAR；creambox PASS（P8 178 lines，slack 35.9）；census PASS（curly 168 全在 Newsreader）；print/web 文字层 byte-identical。**OVERALL: ALL-GREEN** |
| en-pt | 14:10:36–14:30:05 | 0 | 同上结构：TOTAL 150，head_check PASS，text.md diff 4 行（:185/:651，仅 F1），registry diff 0，webpdf RC=0（2,339,582 B）；occlusion 0；p8 CLEAN keydiff=[137,138,139,140,150]；freeze 8/8，added CJK 9 / Latin 363；spill 0（148 OBSERVE）；boxtitle 0（32 titles，185 body lines）；edge 0；creambox PASS（P8 192 lines，slack 37.8）；census PASS（curly 164）；print/web byte-identical。**OVERALL: ALL-GREEN** |
| en-ru | 14:30:06–14:49:49 | 0 | TOTAL 150，head_check PASS，text.md diff 4 行（:185/:651，仅 F1），registry diff 0，webpdf RC=0（2,573,323 B）；occlusion 0；p8 CLEAN keydiff=[137,138,139,140,150]；freeze 8/8，added CJK 9 / Latin 135；spill 0（152 OBSERVE）；boxtitle 0（34 titles，238 body lines）；edge 0；creambox PASS（P8 203 lines，slack 36.3）；census PASS（curly 164，Noto Sans elements 817——俄语讲解层，预期）；print/web byte-identical。**OVERALL: ALL-GREEN**。`svglib.py` 未动。 |
| en-zh-tw | 14:49:49–15:13:48 | 0 | TOTAL 150，head_check PASS，text.md diff 6 行（:185/:651 F1 + :1031 F3），registry diff 0，webpdf RC=0（2,701,637 B）；occlusion 0；p8 CLEAN keydiff=[137,138,139,150]（缺 140 为本版固有——见 KIT §3 注，pre-fix 亦同）；freeze 8/8，added CJK 775（繁體層）/ Latin 132；spill 0（138 OBSERVE）；boxtitle 0（30 titles，251 body lines）；edge 0；creambox PASS（P8 182 lines，slack 35.6）；census PASS（curly 164，Noto Sans 0）；print/web byte-identical。**OVERALL: ALL-GREEN**。F3 :1031 已为 `第二輪投票 12 月 1 日`。 |

### KIT 更新（本工人）

- 已更新 9 版（c042f65c，15:23–15:29）：core-en、en-de、en-es、en-fr、en-it、en-ja、en-ko、en-nl、en-pt——本工人逐版复核：印/网 PDF 全 SHA + 逗号格式字节数 + text.md 全 SHA + 字节数全部与 KIT 一致（脚本 `/tmp/kit_verify.py` 输出 9/9 OK；文字层字符数口径为去空白字符数，与各 KIT 记录值一致）。
- 本工人补更新 2 版：en-ru（§2 三行指纹 + §3 F1 bullet；印 29,097,780 B `9e503c05…`、网 2,573,323 B `8875c559…`、text 62,552 B `13e0e75c…`、文字层 38,129 字符（原 37,997））、en-zh-tw（§2 三行指纹 + §3 F1+F3 bullet；印 30,215,637 B `58112dca…`、网 2,701,637 B `cd585a52…`、text 51,321 B `63c7651e…`、文字层 47,885（该版口径为 pdftotext 字节数，原 47,680））。11 版 KIT 全部与盘上实际 SHA 一致（终验脚本复核 11/11 OK）。
- en-fr KIT 的修复 bullet 为 `**F1+F2 fix`（grep `**F[123] fix` 会漏计，已核实存在）；en-zh-tw keydiff 缺 140 为本版固有（pre-fix 校对 p8-en-zh-tw.json 亦为 [137,138,139,150]），非回归。

### 终验（本工人，2026-11-12，脚本 /tmp/final_verify.py）

- **11 版指纹重测**：印/网 PDF + text.md 字节 + SHA-256 全 11 版与 KIT 一致（见本工人汇报附表；网 PDF SHA 每次重建都变，均以盘上值为准）。
- **F1 旧句清零**：精确旧句 P2 `If no candidate wins a majority in Georgia's Senate race, there is a runoff on December 1.` 与 P6 `…goes to a runoff on December 1. Mississippi…` 在 11 版 text.md 与印 PDF 文字层（归一化单行）均为 0/0；新措辞 `Ossoff won reelection` 在 text.md 各 2 处、印层 `Ossoff` 各 2 处（印层 `won reelection` 因栏间交错只直配 1 处，以 `Ossoff` 计数为准，见接手核实方法注）。源头 11 版 `content12.py:171` 与 `content56.py:103` 全含新措辞。
- **F2**：en-fr text.md 与印层 `passé simple` 0 处、`prétérit` 各 3 处；源头 `content7.py:34` 为 `le prétérit`。
- **F3**：en-zh-tw text.md `決勝輪` 0 处、`第二輪投票 12 月 1 日` 1 处（:1031）。
- **门禁汇总**：11 版 GATES-SUMMARY 尾行全部 `OVERALL: ALL-GREEN`（core-en 注 creambox 重跑 PASS）。
- **Q13/Q142**：4 版 text.md diff 仅含意改行（en-nl/en-pt/en-ru 各 4 行，en-zh-tw 6 行），答案附录零改动；导出器丢标题陷阱未触发（diff 无标题行丢失）。
- 磁盘：终验时已用 94G/150G（< 100G 门限）。
