# GATE-LOG — 2026-W47 ko-de proof2

版：`production/2026-w47/2026-w47-ko-de/`（#3 重建版，未提交）。核心：`production/2026-w47/core-ko`（只读）。
解释器铁律：freeze baseline/diff、run.py、check_core/check_gloss、textmd 用系统 `/usr/bin/python3`（Pillow 10.2.0）；render/webpdf 可走 venv。工作区 `$S = hidden_files/w47/scratch-proof-ko-de2/`。TMPDIR 为 goals 侧 scratch。开工探针：`git hash-object -w`（自 `~/workspace/weekly-git`，`9daeafb9…`）+ scratch 真实写文件 OK（`probe.txt`）；`/dev/null` 缺失时已 `sudo touch /dev/null` 垫回。

## 0. SHA 复核（开工前）

| 文件 | 尺寸 | SHA-256 | 任务单 |
|---|---|---|---|
| 印 `Lucerna-VOL4-KO-DE.pdf` | 45,682,430 B | `28dbc2e775883e64e4a6b482c9da37932d3c803264ba2d9e0ef76d4052cf7cc5` | ✓ |
| 网 `Lucerna-VOL4-KO-DE-web.pdf` | 4,035,158 B | `0b309527f4beb78272a969d153c285af77e5d65c27e520c28a5959fe4a8a45c7` | ✓ |
| `2026-w47-ko-de.text.md` | 35,162 B / 449 项 | `a192156f3c49576611f4392b9c7883c8408dfa3da8519a811cbcbec0eb87917c` | ✓ |
| `ABSTRACT.txt` | 350 B | `2d7ba827b0d051ff1647668c108883dfca05deb7fd5e7f51174a5135a3f9a7c6` | ✓（KIT）|

核心只读核查：印 46,232,227 B `53bf14ed…`、网 4,232,878 B `9592945a…`、text.md 34,606 B `da1d3a32…`，与 proof5 / fix-core2 记录完全一致；8 页 SVG 哈希与 proof5 逐页一致（`sha-svg-core-now.txt`）。

## 1. run.py — PASS

- 命令：系统 python3，在 `$S/rebuild/` 内复制源文件后 `run.py`。
- rc=0；0 FLOW OVERFLOW / HEAD TOO WIDE；TOTAL 150（A2 51 / B1 72 / B2 27；每页 10/18/18/18/18/18/12/38；类型：Satz ergänzen 48、Auswahl 52、Paare zuordnen 16、Umformen 4、Sätze bilden 8、Richtig oder falsch 4、Lückentext 13、Übersetzen 4、Schreiben 1）。
- P2-feature 末 1531（限 1540）；P8-keys 末 2457；P7 teaser 末 2539.22（页脚 2580，余 40.8px）；模型字数 169。
- 重建 8 页 SVG 与生产版字节一致（`sha-svg-rebuild.txt` = `sha-svg-prod.txt`）。
- 日志：`rebuild.log`（重建中间件已按存储规矩删除，日志与 SHA 记录保留）。

## 2. freeze baseline — PASS

- 命令：系统 python3，`tools/freeze.py --build $E --core-svg $E/svg --out $S/freeze`。
- rc=0，**8/8 字节一致**。日志：`freeze-baseline.log`。

## 3. freeze diff — PASS（7 个新增 CJK，全部 U+3000）

- 逐页：P1: 0、P2–P8: 各 1。原始 U+3000 计数：核→版 P1 19→19、P2 17→18、P3 14→15、P4 13→14、P5 14→15、P6 13→14、P7 13→14、P8 14→15。载体为页脚（版 3× vs 核 2×；P1 一处抵消净 0）。新增/删除串全部是德语解释层，无新增韩语内容。
- 日志：`freeze-diff.log`；数据：`freeze-diff.json`。

## 4. p8 extract — PASS

- venv python，`tools/p8.py`：已注 **150/150**。日志：`p8-extract.log`。

## 5. p8 compare vs 核心 — PASS

- **CLEAN**；missing=[]、extra=0；keydiff=[137, 138]（E 组重定向，W46 ko-de 前例）。日志：`p8-compare.log`。

## 6. 独立 keycheck（REG vs P8 SVG）— PASS

- 自写脚本 `proof-keycheck.py`（REG 从源导出 vs P8 SVG 答案行；列向 (x,y) 排序处理跨栏续行；排除 `— 제N면 —` 分隔符/页脚/图例/页行）。
- **149 exact + #150 `✓`（预期，核心一致）= 150/150，BAD 0**。日志：`proof-keycheck.log`；REG：`reg-dump.json`。

## 7. PDF 文字层 keycheck（第三源）— PASS

- 印版 `pdftotext` plain 文字层 vs REG：**149 exact + #150 `✓` = 150/150，BAD 0**。初版 2 处 BAD 均为 checker 伪影（页脚换行被误并入 #16 注；#150 未特殊处理），修 checker 后通过。日志：`pdf-keycheck.log`。

## 8. check_core / check_gloss — PASS

- builder 检查的复制本（`check_core.py`、`check_gloss.py`），系统 python3。
- gloss fails 0，orphan issues 0；P7 句 8/8 逐字（含新句 #7 (1면)）；日期全对。日志：`check-core.log`、`check-gloss.log`。

## 9. textmd 重导出 — PASS

- 系统 python3，与 builder 同命令重导出：与发货 text.md **字节一致**，449 项。日志：`textmd.log`；副本：`textmd-reexport.md`。

## 10. 印/网文字层一致 — PASS

- plain `pdftotext`：印/网各 **52,078 B、字节一致**（`cmp` 干净）。`-layout`：各 107,221 B、字节一致。文件：`print-plain.txt`、`web-plain.txt`、`print.txt`、`web.txt`。

## 11. P8 最小字号 — PASS

- PyMuPDF，印版 PDF：答案区（y≥1302/2700）最小 **9.975pt**（173 spans，168 个在 9.975pt）≥ 9.75pt 阈值；P8 整体最小亦 9.975pt（361 spans）。

## 12. boxtitle — PASS

- `/usr/bin/python3 boxtitle-ko.py $E`：**8/8 ≤ 386.5px**（最大 345.7px P5 Jugendzahlen；P3 Wichtig 319.6、P7 Muster der Woche 341.3）。日志：`boxtitle.log`。

## 13. occlusion audit — PASS

- venv python，`tools/occlusion_audit.py`：**0 flags**；selftest 正常（6 类触发，干净对照静默）。日志：`occlusion.log`。

## 14. census — PASS

- ex/match 166 项，0 缺失；D6 0 缺失。日志：`census.log`。

## 15. §1.1 grep audit — PASS

- 纸 `#fbfaf6`、VOL.4、`·` 计数与核心逐页一致；P7 VOL.5 3→2 系设计（去 `lko`/`lcn2`）；`<text>` 内汉字 0；U+2019 0；颜色集逐页一致。注：原始文件汉字计数 de P1 = 3，均为蛾标 SVG `<title>` 内的 `三色蛾`（嵌入资产元数据，核心相同），非面向读者的文字。日志：`style11.log`。

## 16. 孤儿标点全扫 — PASS

- 8 页 SVG `<text>` 内：U+2019=0、U+201C=0、U+201D=0；独行 `。`/`”`/`：`/`–`/`—` 均为 0；残留汉字 0。

## 17. creambox 逐盒裁定 — PASS

- 规范版 `creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，取自 `hidden_files/w47/tools/creambox.py`）。
- 全部盒子已裁定；所有负数汇总间隙均为已记录的假阳性模式（BELOW-WINDOW 下一区块标题 +26…+44，盒内间隙为正）。P7 工具箱：3 盒，盒内最小 +12.5，desc 余 +6.5。三处紧 Und-du 盒（P2 +5.7/desc −0.3；P3/P5 +5.1/desc −0.9）比核心同类盒更宽松（核心 +4.5/desc −1.5）——继承几何、亚像素降部区，非缺陷。P2 购物清单盒末 1473.9（底 1518.9，盒内 +45.0），全在 D-day 条（y=1618）之上；D-day 条格内 +15.9、desc +10.2。
- 日志：`creambox.log`；核心对照：`creambox-core.log`。

## 18. 150 题手验（三源一致）— PASS

- REG（源导出）= P8 SVG 答案行（#6）= 印版文字层（#7）：150/150。

## 19. 逐页目视 — PASS

- 印版 8 页（`pages/p-1.png` … `p-8.png`，100dpi）+ 网版 P1/P2/P7/P8（`webpages/w-1/2/7/8.png`）：零问题。详见 PROOF-NOTE 目视记录。

## 20. text.md 全文通读 — PASS

- 917 行全读；日期/星期、百分比、比分、计数均与 proof1 核实事实及 KIT 一致；无新事实问题。

## 21. KIT 完整性核查 — 4 项缺陷（见 PROOF-NOTE K1–K4）

- 核实无误：门禁表、SHA/尺寸、修复记录 #1–#6、已裁定项、occlusion、输出文件、未决核查债；数字核实：等级徽章 138 个（P8 35 个）、svglib.py md5 与核心一致（`1c94d836…`）、textmd.py md5 `bc6394a387…` 与核心一致、P7 teaser 余量 40.8px、H 模型 169 字；text.md 449 vs 452 三处扣除核实（`Alle` + `lko`/`lcn2`）。
- 缺陷：K1（P8 行 E 组 137/138 方向写反）、K2（SVG 足迹基线混写）、K3（fix1 网版/text.md SHA 缺失）、K4（fix1 brief 路径注记缺失）。

## 22. 承接项重验 — 全部 PASS

- D1：`content7.py:81` 精确值在场；P7 SVG ×1、text.md 第 761 行 ×1；弯引号形 0。
- D5：`content12.py:174` 精确值在场；`Ernteaussichten` 在 P2 SVG 与 text.md 各 ×1；`die Ernte` 0。D5 字体：只记录、不计入判定（生产级待定项）。
- 核心 D2/D3/D4 流过：ex 10 / ex 47 同句；ex 48 无重复 `시리즈`；P7 句 #7 新句 + (1면)。
- text.md D6 修复：P7 读者来信文本（第 765 行）、德语披露、框架例句 + `Rahmen:` 行（第 761 行）均在场。
- SVG 足迹：vs #2 run 2 变化 P1/P2/P4/P7（P2 = fix1 D5）；vs fix1 后 SVGs 仅 P1/P4/P7。
- `___` 23 处；等级徽章 138 个；ASCII 双空格 0。

## 判定

**结论 (b) 不定稿**。产品文件（印/网 PDF、text.md）全门禁通过，无产品缺陷；缺陷全部在 `WEEKLY-KIT.md`（K1–K4），修复为纯文字修改，不需重建/重渲，修后 KIT-only 复核即可翻 (a)。
