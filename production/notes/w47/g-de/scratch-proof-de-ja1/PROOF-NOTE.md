# PROOF-NOTE — 2026-W47 de-ja · proof1（独立复校）

- 复校员：独立复校（与重建 B 棒非同一人）
- 日期：2026-11-11（UTC 上午，EST 04:05 开工）
- 版：`2026-w47-de-ja`（德语目标 · 日语读者），重建版（rebuild-B build 1）
- 结论：**(a) 零缺陷可定稿**
- 缺陷清单：无（D1/D2/… 共 0 条）
- 门禁日志：`GATE-LOG.md`（同目录；每道门禁的命令与 RC 全数记录）
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-ja1/`（txt/ 提取文本、png/ 16 张 100 dpi 渲染、freeze_repl.py / srcdiff.py / abut.py / fonts.py 自写核查脚本、occlusion.json / p8extract.json / p8compare.json / freeze.json / freeze-strict.json / freeze-direct.json / keycheck-150.json / verify-rerun.log）

## 0. SHA 核对（先核对，通过后才开工）

| 文件 | 实测 | 任务给定 | 结果 |
|---|---|---|---|
| 印刷 PDF `Die-Lucerna-VOL4-de-ja.pdf` | 23,901,736 B，`f412f930242d16c87a7fb783506f6e92e5020a40e323edfdb1243dfd82db459d` | 同左 | ✓ 符 |
| 网页 PDF `Die-Lucerna-VOL4-de-ja-web.pdf` | 2,113,024 B，`29f65fec5681e46f5b927171163c5d66559e61ed275d998583653574d8e8294a` | 同左 | ✓ 符 |
| text.md `2026-w47-de-ja.text.md` | 51,913 B，SHA-256 全文 `a59f784705bec4329b7dfa19321256c2469ab7680212302481876fc96f957f69`（前 8 位 `a59f7847`） | 前 8 位 `a59f7847` | ✓ 符 |
| ABSTRACT.txt | 426 B，日语一行，无 ASCII 双引号 | KIT §2 | ✓ 符 |

探针：开工前 `git hash-object -w --stdin` 成功（`9daeafb…`，RC=0），并在本科目录真实写盘；每次写盘前重探均通过。磁盘未报 EDQUOT（`df` 时已用 72G/150G）。

## 1. Q34 专项（重建改动，逐一复核）

- 新题干 `"Am Montag öffnet in Köln der erste ___."`：源码 `content34.py` 1×、`.text.md` 1×（Q34）、P3 SVG `p3-kultur.svg` 1×、印刷 PDF 文字层 1×、网页 PDF 文字层 1×、核心 `core-de/content34.py` 1×、核心 text.md 1×。
- 旧题干 `"Am Montag öffnen in Köln die ersten ___."`：上述各处均为 0×。旧题干仅见于重建前快照 `ja-prev/freeze-direct.json` 的 unaccounted_removed（即本次重建所替换的对象）。
- P3 目视确认：100 dpi 全页 + 200 dpi 特写（`png/p3-q34-crop.png`）——`A2 34. 入れよう / Am Montag öffnet in Köln der erste ___.` 单数形式、单行、无遮挡、无溢出。
- 一致性：题干单数 `der erste ___` 与答案键 Q34 `Weihnachtsmarkt`（单数）吻合；P3 正文 `"Am Montag, dem 16. November, öffnen in Köln die ersten Weihnachtsmärkte"` 为复数叙述句，与填空题单数形式不冲突（题干问的是词框中的 `Weihnachtsmarkt` 一词）。

## 2. 内容复校（从头完整校，逐页）

- `.text.md` 全文 1,187 行逐行读完；练习 1–150 连续编号、题题有键（P8 答案区 1–150 齐全，见 §5）。
- 德文正文与核心对照：`.text.md` 纯拉丁行多重集 diff（edition 326 行 vs core 327 行）——仅 2 行差异：(1) 版头 slug 行（`de-ja` vs `de-zh-cn`，必然）；(2) 核心 P1 标语 `DIE WOCHENZEITUNG FÜR LERNENDE — …` 在 ja 版被读者语版名行 `ドイツ語テキスト・日本語解説 — 日本語話者向けエディション` 替换——transform 日志 1× 记录，10 个 de-* fan-out 版全部如此（`WOCHENZEITUNG` 计数均为 0），为统一 fan-out 模式，非缺陷。
- 数字/日期逐项核对：P2 三道日期算术 18+11=29、15+7=22、16+6=22 均正确；`date` 核实 2026-11-03（二）、11-04（三）、11-05（四）、11-13（五）、11-16（一）、11-17（二）、11-18（三）、11-20（五）、11-22（日）、11-23（一）、11-27（五）、11-29（日）——文中所有"星期×+日期"搭配正确；比分/时间（Bayern 2:0、Dortmund 2:1、Leipzig 2:3、Stuttgart 0:2、Leverkusen 0:1、Hoffenheim 1:1、Freiburg 1:0、9. Spieltag 30 Tore、20.30/15.30/18.30/17.30/20.45）与 P4 日程表、练习题、答案键三方一致；图表 44+33+23=100。
- 答案键逐题人工验算（抽查全部关键题型）：配对题 25–28（d/c/a/b）、52–55（d/b/c/a）、141–144（c/a/d/b）与词框顺序一致；比较级 56–59（mehr/später/früher/mehr）与比分/时间/积分一致；被动/将来 101–103（wird/werden/wird）、weil/dass/ob 107/109–111、113–120 动词变位、121–128 选择、129–136 阅读/造句、137–140 翻译（日译 3 题 + 德译 1 题，译文与原文对应）、145–149 对话变位（öffne/machst/schaue/schaue/lese）全部正确；Q150 键 `自由課題 — 枠のポイントに従おう`。
- P7 金句 8/8 逐字核对正文：① P1 "Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln." ② P1 "Es geht ums Viertelfinale der Nations League." ③ P2 "Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag." ④ P3 "Die Märkte beginnen fast zwei Wochen früher." ⑤ P5 "Hinter jedem Türchen wartet eine kleine Überraschung." ⑥ P4 "Der FC Bayern gewann in Mainz mit 2:1." ⑦ P6 "Die stille Woche ist der Übergang: vom November in den Advent." ⑧ P6 "Am Sonntag ist es still im Land."——逐字一致，页码标注（Seite 1/1/2/3/5/4/6/6，按级别 A2→B2 排列）正确；日语译文与德文对应。
- MUSTER 84 词：实测空白切分 84 词，与标注 `模範文（84語）` 相符；H 作文题 80–100 词要求与模范文字数自洽（模范文本身 84 词在区间内）。
- P8 练习 113–150（A 穴埋め 113–120、B クイズ 121–128、C 読解 129–132、D 文作り 133–136、E 翻訳 137–140、F 組み合わせ 141–144、G 会話 145–149、H 作文 150）与答案键齐全；Q150 的评分注已按重建 3 决议移除（H 节 + MUSTER 已含指示，REG 键不变）。

## 3. 网页 PDF（逐页校对 + 文字层 + abutting）

- 文字层完整：`pdftotext` 印刷 112,509 B / 网页 112,510 B；词级多重集完全相同（6,871 词，两边互差 0）；逐页 diff 仅 3 行空白间距差，无内容差。
- abutting（自写核查 `abut.py`，PyMuPDF 词级位置比对）：同行同词的词间距变化最大值 0.5pt——**不大于 0.5pt**，无缺口缺陷。注：两端对齐行内词的绝对 x 位置存在累计漂移（最大约 44pt，P1 标题行），系新旧 webpdf 字体度量差异所致（见 §7 工具层单列），词与词之间的相对间距变化 ≤0.5pt，视觉上无错位、无断词。
- P8 最小字号：印刷/网页均为 9.94pt（≥9.75pt 门槛）。
- 网页 8 页 100 dpi 逐页目视：与印刷页逐页一致，无内容/几何差异（仅 §7 的两项字重/斜体差异）。

## 4. 几何与冻结门禁（独立重跑，见 GATE-LOG.md）

| 门禁 | 命令 | RC | 结果 |
|---|---|---|---|
| occlusion | `tools/venv/bin/python tools/occlusion_audit.py <edition>/svg --json occlusion.json` | 0 | 0 flags，selftest 6 类 planted 全触发、clean 对照静默 |
| p8 extract | `tools/p8.py extract --p8 …/p8-uebungen.svg --total 150` | 0 | noted 150/150（joined） |
| p8 compare | `tools/p8.py compare --core-p8 … --edition-p8 … --total 150` | 0 | **CLEAN**，missing=[]，extra=0，keydiff=[137, 138, 139, 150]（预期：137–139 日译题 + 150 Q150 PREFIX） |
| freeze diff | `tools/freeze.py diff --core-svg … --edition-svg …` | 0 | TOTAL added CJK 2,994（P1 243 / P2 229 / P3 312 / P4 180 / P5 269 / P6 237 / P7 412 / P8 1,112），与 builder 一致 |
| freeze_direct（真实工具） | `scratch-fanout-de/freeze_direct.py ja <edition> <scratch>` | 1* | rendered **8/8**：frozen 144/164/200/166/179/173/163/183，sha8 `b01ba1b1/2db0dd83/2dd3b3f2/df1bebf7/e7b235f9/89156519/b854370f/1c855c30` 全部命中（含 P3 新值 2dd3b3f2）；source 层 removed 516 / added 524，unaccounted 仅 JP 字体开关（removed 1：`Noto Serif CJK SC`；added 3：`JP`、`Noto Sans CJK JP`、`Noto Serif CJK JP`） |
| boxtitle | `scratch-fanout-de/boxtitle.py ja` | 0 | **7/7 fit**（387.6/333.4/300.7/379.4/361.9/290.3/286.5 ≤ 400.5） |
| keycheck | `scratch-fanout-de/keycheck.py ja <edition> <scratch>` | 0 | **149/150**，唯一 mismatch 为 Q150 PREFIX（key `自由課題 — 枠のポイントに従おう` vs extracted `自由課題`），与拉丁版一致的预期结果 |
| verify.py（版内） | `<edition>/verify.py` | 0 | TOTAL 150、编号连续、§1.1 audit True、verbatim OK、P8 floor True、17 禁用词全无、chart 748/561/391 |
| freeze --strict-cjk | `tools/freeze.py diff … --strict-cjk` | 1* | *见注 |

\* 注：`freeze_direct` RC=1 与 `freeze --strict-cjk` RC=1 均为日语版**按设计**的结果（KIT §5 已载明）：读者语解说层本身新增 CJK 2,994 字，`--strict-cjk` 要求新增 CJK=0 对 ja 版不适用；freeze_direct 的 source_level_pass 亦因子 JP 字体开关（4 个字符串，transform.py 198–202 行的 SC→JP 切换）而不通过——builder 重建记录的同一状态（`ja/freeze-direct.json` 逐值相同，本次独立重跑逐值复现）。两者都不是缺陷。

## 5. 弯标点专项

- 8 个 SVG 中含 CJK 的 `<text>` 元素逐个扫描：U+201C / U+201D / U+2019 出现 **0 次**。
- 全 SVG 原始计数：U+201D = 0，U+2019 = 0，U+201C = 33——33 处全部是德文引号 `„…"` 的闭引号（配对的 U+201E 开引号），附着于纯德文串，无一混入日语值。日语一律用「」。
- 附带：Q108 逻辑串 `„Stiller als sonst" heißt... A. いつもより静か…` 的弯引号属于德文原句的德式引号，SVG 中德文干与日语选项分属不同 `<text>` 元素，规范正确。`tr_ja.py` 中另有一条 Q108 的中文选项旧变体（`比平时更安静…`），**不在本版任何文件里**（仅 builder 侧对照表残留），不构成缺陷，见 §8 观察。

## 6. 目视复校（印刷 8 页 + 网页 8 页，100 dpi 全页）

- 印刷 P1–P8、`web-p1`–`web-p8` 逐页看完，**零发现**：版式、标题、图片、图注、盒子、练习题、页脚（`n / 8 ページ`）、图表均无遮挡、无溢出、无错字（以文字层核对为准）。P1 ZAHLEN 盒与 word-of-week 均为单行盒内；P6 图表标签与柱条无接触（verify 亦确认）；P8 MUSTER 标签 `MUSTER　模範文（84語）` 清晰在位。
- Q34 特写（200 dpi）见 §1。

## 7. 工具层问题——单列，不与内容缺陷混同（网页 PDF 系 D2 补丁落地前的旧 webpdf.py 所建，pre-insert 将以定稿工具全部重建）

- **T1**：P1 版名行 `ドイツ語週刊　VOL.4　ブンデスリーガ復帰　静かな一週間`：SVG 注明 `font-weight="700"`，印刷 PDF 为 Bold，网页 PDF 降为 Regular（3 个 span：`ドイツ語週刊` / `ブンデスリーガ復帰` / `静かな一週間`）。其余各页 Bold span 数印刷/网页一致（P2–P8 均为 50/57/55/62/67/67/99）。
- **T2**：P1 `« der Adventskalender »`：SVG 注明 `font-style="italic"`，印刷 PDF 为 Newsreader Italic（全版唯一 1 个斜体 span），网页 PDF 为 Regular（网页 PDF 无任何 Italic 字体）。
- **T3**：网页 PDF 字体度量与印刷不同（Lucerna* 系列 vs Newsreader16pt 系列），两端对齐行内词 x 位置累计漂移最大约 44pt；但词间距相对变化 ≤0.5pt（§3），视觉无错位。以上三项均为旧 webpdf.py 的字体处理差异，不涉及内容、数字、答案与几何；定稿重建后应复核 T1/T2 是否消失。

## 8. 观察（非缺陷，不影响定稿）

- O1：版内 `verify.py` 打印 `MUSTER label: MISSING`，但 P8 页面上 `MUSTER　模範文（84語）` 标签实际存在——脚本按独立 `MUSTER` 元素精确匹配，而本版标签为合并元素；verify RC=0，builder 日志亦同此输出。属脚本匹配口径问题，非版面问题。
- O2：P6 Q87 选项 `C. 44 %` 的 `%` 折到下一行——正常换行，无溢出，核心版同式。
- O3：`tr_ja.py`（builder 侧对照表）含 Q108 中文选项旧变体 1 条，未进入本版；建议下次 fan-out 时清理对照表残留（不影响本版）。
- O4：CJK 残留审计：宽口径 CJK 字符 4,008 个（KIT 称 4,005，差 3 字为统计口径：本次含 U+31F0–U+31FF 小假名与 U+FF61–U+FF9F 半角片假名），**0 字**不在 `tr_ja.py` 值集与核心 SVG 之外；汉字单扫 1,358 字，与 KIT 一致，值集外仅 色/蛾（核心自带 `<title>Lucerna 三色蛾</title>`，与核心字节一致）——零简体中文残留。
- O5：源码层 diff 独立复算 removed 516 / added 524，与 builder 的 freeze_direct 源码层总数一致；本次粗分表的其余未归类项（TYPEMAP 类型标签、页码行骨架、输出路径/文件名、校验 docstring、版头标语替换）均有据可查，无新增德文内容串。

## 9. 未做事项

- 未改源、未重建、未 commit、未 push（按任务要求）。
- `freeze.py baseline`（核心重建 8/8）未重跑：freeze_direct 的 rendered 8/8（逐页 frozen 计数 + sha8 与 builder 逐值复现）已覆盖冻结核对；baseline 属于构建者门禁，非 proof1 必须项。
- 本版不含网站封面块（cover.json / lint 规则 14 属整周门禁，非单版 proof 范围）。

## 结论

**(a) 零缺陷可定稿。** 内容缺陷 0 条；工具层差异 3 项（T1–T3）单列于 §7，按任务要求不计入内容缺陷，待 pre-insert 定稿 webpdf 重建后复核。
