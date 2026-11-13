# GATE-LOG — W47 zh-tw-fr proof1 机械门独立重跑记录（重建后新版）

- 复校对象：`production/2026-w47/2026-w47-zh-tw-fr/`（印 SHA `acd1d85b2af07310…` / 网 SHA `6026be3ed418a8bd…` / text SHA `673943a0de31811e…`，见 PROOF-NOTE.md）
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`（正典栈，绝无系统 python3）；TMPDIR 为 scratch 内 `tmp/`
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0，goals 侧真实写文件成功后开工
- 本目录内 `work/` 与 `PROOF-NOTE-old-build-0841.md` / `GATE-LOG-old-build-0841.md` 为 08:41 上一轮（旧版成品）的记录，原样保留；以下为本轮新版实测
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-zh-tw-fr1/`（下称 `$S`），版目录 `$ED=~/workspace/weekly-git/production/2026-w47/2026-w47-zh-tw-fr`，核心 `$CORE=~/workspace/weekly-git/production/2026-w47/core-zh-tw`

## 1. 成品指纹（开工实测，sha256sum + wc -c）

- print `Lucerna-VOL4-FR.pdf` 20,191,919 B，SHA-256 `acd1d85b2af073100140a8bfd5936faeecc8a050f42226a424066aefce1aaf33` ✓
- web `Lucerna-VOL4-FR-web.pdf` 2,366,339 B，SHA-256 `6026be3ed418a8bd9574bfea2fd154ec7bc727d600b0eded0cff2b91a4070246` ✓
- text.md `2026-w47-zh-tw-fr.text.md` 52,470 B，SHA-256 `673943a0de31811ee43d899390a40fdde1c564ae7176f61878f77e1c687fa613` ✓
- 核心对照：印 `5ec35fe2a95142463eccc737bd51e4b2eaf3f2f0394a286cded23ea91e570d9a` 19,420,552 B；网 `1c0799ac37662736fc27d4bf9cd1f220bf038089e75e159433da18cd8ee6d240` 2,324,042 B；text `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b` 49,798 B ✓

## 2. freeze baseline（第一步，8/8 才继续）

命令：`tools/venv/bin/python tools/freeze.py baseline --build $ED --core-svg $ED/svg`（输出至 `$S/freeze-base/`，日志 `$S/freeze.log`）

- **8/8 SVGs byte-identical**：p1 `b11d4028…`、p2 `f8f7c994…`、p3 `7c9e4576…`、p4 `7bda50af…`、p5 `f2de5e8e…`、p6 `08e0227d…`、p7 `6b3fd466…`、p8 `f7421f50…`（core 与 produced 逐对一致）
- core integrity：shipped core SVGs 重哈希未变
- runtime：venv python | Pillow 13.0.0 | FreeType 2.14.3

## 3. freeze diff --strict-cjk

命令（逐字）：`tools/venv/bin/python ~/workspace/weekly-git/tools/freeze.py diff --core-svg ~/workspace/weekly-git/production/2026-w47/core-zh-tw/svg --edition-svg $ED/svg --strict-cjk` → 日志 `$S/gates/freeze-diff.log`，rc=1

- `STRICT-CJK FAIL: edition adds CJK characters the core does not have`
- 分页：p1 +25/-25 strings，CJK core 892 → edition 879，added {'法': 2}；p2 +43/-39，1111→1106，{'法': 1}；p3 +48/-46，1198→1193，{'法': 1}；p4 +40/-37，810→805，{'法': 1}；p5 +50/-45，1220→1215，{'法': 1}；p6 +35/-33，884→879，{'法': 1}；p7 +114/-106，822→817，{'法': 1}；p8 +189/-179，1114→1109，{'法': 1}
- TOTAL added CJK = 9，全部是家具「法語講解」中的「法」（P1 ×2 徽章行+页脚，其余每页 ×1 页脚）；正文 CJK 无新增。裁定：门禁工具对 fan-out 家具（读者语名必然更换）的结构性误报，非缺陷（与上一轮同一裁定；上一轮核心 CJK 计数 p1 890、p5 1236、p6 877，本轮核心侧计数有变化，与核心层为修 D1 所作编辑一致）

## 4. checks.py

命令：`tools/venv/bin/python $ED/checks.py` → `$S/gates/checks.log`

- **CHECKS PASS**：8 phrases ×2；SIMP_ONLY_HITS []；P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]

## 5. occlusion 审计

命令：`tools/venv/bin/python tools/occlusion_audit.py $ED/svg/` → `$S/gates/occlusion.log`、`occlusion.json`；另 selftest → `$S/gates/occlusion-selftest.log`

- selftest OK：6 类 planted（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX）全触发，clean 对照静默
- 全版 **0 flags**

## 6. p8 extract + compare

命令：`tools/venv/bin/python tools/p8.py extract --p8 $ED/svg/p8-test.svg --total 150` → `$S/gates/p8-extract.log`、`p8-extract.json`；
`tools/venv/bin/python tools/p8.py compare --edition $ED/svg/p8-test.svg --core $CORE/svg/p8-test.svg` → `$S/gates/p8-compare.log`、`p8-compare.json`

- extract：noted set = **150/150**（1–150 连续）
- compare vs core：**CLEAN**，missing=[]、extra_count=0、keydiff=[]

## 7. canonical creambox 全版扫描

命令：`tools/venv/bin/python ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py $ED/svg/` → `$S/gates/creambox.log`、`creambox.json`

- **36 盒**；inside-only 最小清除：P1 18.8 / P2 15.8 / P3 15.8 / P4 9.8 / P5 6.4 / P6 19.9 / P7 12.5；负 inside-only 清除 0
- P7-TOOLBOX 三盒清除 +40.5 / +12.5 / +14.0（desc-clear +34.7 / +6.5 / +8.0）
- 注意：日志中 11 条 `clearance -44/-37` 行为 naive box 行，其 "last baseline" 含一行 BELOW-WINDOW 行（盒底之外下一元素的首行，如 P1 y=1215.8 在盒底 1171.8 之下 44px），非盒内溢出；正典 inside-only 度量全部为正

## 8. boxtitle（新版 + 备份旧版）

命令：`tools/venv/bin/python <builder gtools>/boxtitle.py $ED/svg/` → `$S/gates/boxtitle.log`、`boxtitle.json`；
同工具对 `scratch-refanout-zh-tw/backup/2026-w47-zh-tw-fr/svg/` → `$S/gates/boxtitle-old.log`

- 新版：**36 盒，overruns 0**；最小标题右余 **-0.2px**（P2「耶誕城小檔 Fiche Christmasland」，盒 [1439.5, 1430.0, 1862.0, 1890.0]）；最小左余 18.0px
- 旧版：同样 36 盒、overruns 0、最小右余 **-0.2px**（同一标题，完全相同）
- 新旧逐盒右余差：仅 2 处——P1 Notes 盒 77.2→44.8px、P2 Notes 盒 57.8→42.8px（法语 Notes 首行重排，仍为大幅正值）；其余 34 盒完全相同

## 9. creambox-pil STRADDLE / CREAM-COVER（新版 + 备份旧版）

命令：`tools/venv/bin/python <builder gtools>/creambox-pil.py $ED/svg/` → `$S/gates/creambox-pil.log`；
同工具对备份旧版 SVG → `$S/gates/creambox-pil-old.log`

- 新版：**STRADDLE 0，CREAM-COVER 0**
- 旧版：**STRADDLE 1**——P4「你呢？」盒，法语译文末行独占 "?"（x=1461.5，基线 y=1362.2，墨底 1362.4），旧米色盒底 1358.0，伸出 4.4px；新版米色盒高 230→244（盒底 1358→1372），"?" 位置未变，现距盒底 +9.6px 在内
- 结论：重建修好 1 处旧超框，引入 0 处。builder §7「fr 0 = 舊 0」不实（其 `gates/old-fr-check/` 内仅有 boxtitle.json，无旧版 creambox-pil.log；其余 8 版均有旧 PIL 日志）

## 10. 印/网文字层多重集 + 位置差分

命令：`pdftotext -layout $ED/Lucerna-VOL4-FR.pdf $S/gates/print.txt`；`pdftotext -layout $ED/Lucerna-VOL4-FR-web.pdf $S/gates/web.txt`；`pdftotext $ED/Lucerna-VOL4-FR.pdf $S/gates/print-plain.txt`；`pdftotext $ED/Lucerna-VOL4-FR-web.pdf $S/gates/web-plain.txt`；多重集比对（venv python）

- -layout 字节：110,315 / 110,315（字节全等，即文字与位置一致）；字符多重集差 **0**
- plain 差恰 1 字节（仅一个 `\n`）
- 计数（印/网一致）：本週日 11/11，下週日 0/0，BABYMONSTER 0，取捨 2/2，小雪 36/36，end point 0，next Sunday 0
- VOL 计数（印文字层）：VOL.4 ×10、VOL.3 ×2、VOL.5 ×1

## 11. PDF 度量（PyMuPDF，venv python）

- 8 页，1462.5×2025 pt；P8 字号 9.75–34.5pt（最小恰 SOP §1.1 下限 9.75）；P1 顶部字号 [147.0, 45.0, 27.0, 24.0]；印 20,191,919 B / 网 2,366,339 B

## 12. 填空键 + 答案键连续性

命令：venv python 填空键抽查 → `$S/gates/fillin-check.log`

- 填空键 **54/54** 出自正文；答案键 1–150 连续

## 13. leak 扫描

- deny 命中 {}（含 "next Sunday"/"Next Sunday" 0 处）；唯一与核心共有的长 ASCII 串为选项行 `A. 12:00 · B. 14:00 · C. 19:00`（构造共享）

## 14. abutting P6（18:30/19:00）

- 18:30「頒獎典禮」墨右缘 990.8；19:00「夜間遊行」墨左缘 991.4；墨缝 **0.6px**；与核心先例一致；P6 渲染目视无碰撞

## 15. 150 题逐题手验（三源交叉）

命令：`tools/venv/bin/python $S/keycheck150.py` → `$S/keycheck-150.json`、`$S/keycheck-150-dump.txt`（150 题干+选项+答案键逐题 dump，450 行）

- 三源（版 text.md 答案区 / 版 P8 SVG 答案区 / 核心 P8 SVG 答案区）答案值 **150/150 一致**；mismatches []
- 唯一名义差异：#150 注释语言——核心英文 "Open task … (142 characters)"、版与 text.md 法文 "Tâche ouverte … (142 caractères)"，内容相同，记 OK
- 150 题题干+选项+答案逐题手验无误；F 范文实测 **142 字**（120–180 内）；Q114 答案 B（SVG 原文核实，初看渲染曾误读为 A）
- 补充：`$S/p8-svg-flow.txt`（150 题 P8 流程抽出）、`$S/textmd-prose.txt`（text.md 349 行 prose 抽出）

## 16. text.md 全文通读 + text.md ↔ 印 PDF 文字层

- text.md 全文读过（8 页节 + 5740 行起答案键）；与印 PDF 文字层比对：非空白字符多重集差 153/约 25,800，**CJK 字符差 0**；残差全为 Markdown 标题记号（`#`×17、"Page N — …" 标题字母）与 PDF 独有的装饰性 "Lucerna" 页眉词标（text.md 8 处页脚 vs PDF 16 处）
- E 节 type 标签：A 判斷對錯 / B 本週大測驗 / C 完成句子 / D 讀一讀，答一答 / E 情景說話 / F 寫一寫，配法语 gloss，全繁体 ✓
- 弯引号：直引号 `"` 0；「」21/21 成对（与核心一致）；“”/«» 0；… ×6 全在「越…越…」内；法语省音 `'` ×86（核心 ×28，同一家 ASCII 风格），无中文邻接撇号
- 简体字：checks.py SIMP_ONLY_HITS []；text.md 同集扫查 []
- 风格杂扫：`grep Gold` 仅 "Golden Horse"；`stroke-width="3"` 0 处；「·」×59（选项分隔/时间轴图例/人名中点，与上一轮核实一致）；弯引号 “” 0

## 17. 旧缺陷修复核实（本轮新增查证，逐位置）

命令：venv python 剥 SVG 标签后按关键词取上下文；`grep -o 本週日 $ED/svg/*.svg | wc -l` 等

- **D1**：SVG「本週日」11 处（P1×3、P2×1、P3×2、P4×3、P7×1、P8×1，与旧版 11 处「下週日」位置逐一对应），「下週日」0 处；法语 "dimanche prochain" 0 处，P1/P4 Notes 为 "ce dimanche, 22 nov."（P1 另有 "le dimanche 22 nov."）✓
- **D2**：P7 SVG 原文：`Astuce mémoire : apprenez d'abord 入圍, puis 星光大道 (le tapis rouge à 17:00, avant la cérémonie), puis la cérémonie （頒獎） à 18:30.` — 顺序与时间均已改正 ✓
- ABSTRACT.txt（423 B）全文读过：法语单行，VOL.4、A2 à B2、150 exercices，本周真实主题，无 ASCII 双引号 ✓

## 18. 目视（自行渲染，100dpi，PyMuPDF）

- 印 PDF P1–P8：`$S/render/p1.png`–`p8.png`，逐版看过，无溢出/重叠/页脚碰撞
- 网 PDF 抽查：`$S/render/web-p1.png`、`web-p4.png`，与印版视觉一致
- 渲染所用 PDF 为印/网成品本身；未采信 builder 的图

## 19. 只读复核

- `git status --porcelain -- production/2026-w47/2026-w47-zh-tw-fr/`：版目录为 untracked（`??`，与 builder 交付状态一致），无本人改动；成品 mtime 仍为 builder 的 11:06–11:08
- 未改任何生产文件，未 commit，未 push；全部写盘只在 goals 侧 scratch（`$S`）
