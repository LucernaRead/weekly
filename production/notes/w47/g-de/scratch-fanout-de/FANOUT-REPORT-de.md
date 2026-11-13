# W47 de fan-out — FANOUT REPORT (builder, 3rd shift)

## 结论：完成 — 10/10 建成（de-en、de-fr、de-es、de-it、de-pt、de-nl、de-ru、de-ja、de-ko、de-zh-tw 全部完成，全量自查零问题），第 5 棒任务完成
## 重建-A（2026-11-11 08:05–08:41 UTC，builder A：de-en / de-fr / de-es / de-it / de-pt）

core-de 重新定稿 build15（proof5 (a) 零问题，2026-11-11 08:02 UTC；印版 22,965,197 B
sha 49beffc4…、网页 2,044,855 B sha 9b63b413…、text.md 49,798 B sha 0952bc51…），唯一内容变化是
Q34 题干 `content34.py:105` 由复数 `"Am Montag öffnen in Köln die ersten ___."` 改为单数
`"Am Montag öffnet in Köln der erste ___."`（键 `Weihnachtsmarkt` 不变）。本波次 5 版全部从新
core 删除重建，**5/5 建成，全部 ALL GATES PASS，8 版目视零问题**。builder B 的 5 版
（de-nl、de-ru、de-ja、de-ko、de-zh-tw）由 B 另行重建，本节不涉及其数字。de-en 的 proof1 (a)
已因旧题干作废——重建后须另派全量复校（本棒不做复校）。各版记录在
`scratch-fanout-de-rebuild-A/<lang>/EDITION-RECORD.md`，工具与日志同目录。

| 版 | 重建 | 完成 UTC | 印版 B (sha256 前 8) | 网页 B (sha256 前 8) | text.md B (sha256 前 8) |
|---|---|---|---|---|---|
| de-en | 3 | 08:15:54 | 10,966,409 (47aae035) | 1,555,605 (37ba00d4) | 49,665 (2eb03632) |
| de-fr | 4 | 08:18:59 | 10,932,570 (126e9522) | 1,556,917 (727c8b8a) | 50,042 (3ef1934a) |
| de-es | 4 | 08:24:15 | 10,968,803 (7bc39e1f) | 1,558,821 (cd453143) | 50,124 (5f5ea69b) |
| de-it | 3 | 08:29:28 | 10,965,095 (0d7be581) | 1,553,872 (dbbe5880) | 49,712 (1594ba08) |
| de-pt | 3 | 08:41:14 | 10,968,908 (33e2dc7d) | 1,599,432 (a251196e) | 49,812 (42579207) |

完整 sha256：en 印 `47aae035c9531818bce832e25b2aed6ed2557c18229c514bf32443fb6becd429` /
网页 `37ba00d4fcf83f7dd78fe6427d5b0c1ae70c9035fbe8dd345dfde8de13d12875` /
text `2eb0363202b8c9eacc8aaaf5008eedab614b8ddb0301082e92eb80cd25d6b7f5`；
fr 印 `126e9522eb9980012692bf84e7ed5e420032fd2574ea355ac62466529c0e0700` /
网页 `727c8b8a4f7ee27d0687b4503f0cf47c3e766f081538aa9ce1cf06da55f842f5` /
text `3ef1934af59e6ba8f6cf59d1cd24fcfdd30f1a25e5b8c1a4f544446bd7ff0db6`；
es 印 `7bc39e1f58b9bb447caf4f69b397eb39723ab2fef1c2bc4cf99d1be4a6e580ed` /
网页 `cd453143111bfad4f7f8a6ada98190f1790d2feccdaf3fd7c762a3a683043b90` /
text `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3`；
it 印 `0d7be5816da194742ed4b25e10e15b3a35353e243535c4361e12722c300bbb93` /
网页 `dbbe5880e1b8b1309e981f021c8e41e2f862fe62629816c2be8c9e90a3290f46` /
text `1594ba080bece8b9a947cf011a64a355125b8869f82413ccdb03ae31a269f255`；
pt 印 `33e2dc7d5fe62549c605a622d61d59ade0dd5fa4e54aa3a7901dbbc486d260aa` /
网页 `a251196e6d411c09f3b4ccef54876da6fcacd96fd899198154b9836118b877bb` /
text `4257920750577d5ad5f0e58ca8959dcb8ef4779cafd1a932a170405c24790dbf`。

- **每版通用门禁（全部绿）**：run.py RC=0、0 溢出；measure 24/24；occlusion 0 flags；
  p8 抽取 150/150、compare CLEAN、keydiff [137, 138, 139, 150]（预期内）；
  freeze 8/8（渲染冻结 147/163/195/166/173/175/150/186，
  sha `083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 /
  57e118e7`——仅 P3 sha 由上一轮的 `093cf378` 变为 `fc88f676`，因 Q34 题干字符串本身改了，
  冻结数仍为 195；其余 7 页与上一轮逐字节一致）；print/web 文字层多重集一致
  （en 50,434/50,435B、fr 50,881/50,883B、es 51,012/51,013B、it 50,593/50,597B、
  pt 50,684/50,684B；-raw 归一化 en 49,277B、fr 49,698B、es 49,812B、it 49,392B、
  pt 49,500B，各版双份一致）；chips 10/15/18/15/18/18/12/35 = 141，
  P8 A2 22 / B1 13 / B2 0；P8 最小字号 9.94pt；U+2019 全扫 0；150 键复核 149/150
  （仅 Q150 抽取器截断，预期内；en 48,034 字符、fr 48,164、es 48,286、it 48,032、
  pt 47,947；ABSTRACT en 356B、fr 414B、es 426B、it 393B、pt 400B）。
- **Q34 核查（每版 5 处各 1× 新题干、0× 旧题干）**：源码 `content34.py`、`.text.md`、
  P3 SVG、印版文字层、网页文字层，5 版全部通过；P3 目视可见新单数题干。
  de-en 观察项 O1（P4 Stuttgart 0:2 Galatasaray 为欧冠 prose、结果表只列德甲）已裁定不是缺陷，
  重建未动它。
- **box-title 真缺陷修复（本棒唯一有意的"除 Q34 外"内容改动）**：上一轮报告称 en/fr
  "值干净未动"只是断言未实测（上一轮 sweep 只覆盖了 es/it/pt/nl/ru/ja/ko/zh-tw）。
  本棒实测 en `WEIHNACHTSWÖRTER　Christmas words` 483.5px 超 400.5px 预算 83px，
  fr 6 个标题超 10–53px；旧版 P3 裁切目视确认墨水跑出奶油盒落到新闻纸上（"words" /
  "Noël" 在纸面）。只改读者语 gloss、德语头不动：en → `WEIHNACHTSWÖRTER　Words`
  （359.9px）；fr → `La semaine`、`Noël`、`Conseil`、`Avent`、`Outils`、`Courrier`
  （219.5–376.9px）。修复后 boxtitle en/fr 均为 7/7，重建页目视确认标题全部收进盒内。
  diff 存 `scratch-fanout-de-rebuild-A/tr-fixes.diff`；共享的 `scratch-fanout-de/tr_*.py` 未动。
  es/it/pt 本轮 boxtitle 7/7 无需改动。
- **de-pt 首建失败后重试**：首跑（08:31–08:32）run.py 完成但渲染中进程被杀（RC 120，
  仅 p1–p3 卡片写出、无 PDF、日志 0 字节；当时机器多 agent 并行、空闲内存约 184MB）。
  以 `python -u` 重跑（08:37–08:41）：ALL GATES PASS。旧轮 P7 col3 1547.5（1548 线前 0.5px，
  内容与上一轮相同、冻结数一致，目视工具盒末行收进盒内，无重叠）与 rebuild-2 一致。
- **de-pt 网页 PDF +40,050 B（工具中途改版所致，非内容）**：上一轮网页 1,559,382 B →
  本轮 1,599,432 B，而印版仅 +6 B、text.md −1 B。原因是 `tools/webpdf.py` 在工作树有未提交改动
  （另一 agent 的 scratch-webpdf-patch1 在本棒 de-it 08:29 与 de-pt 08:31 之间落地）：
  `fc_match` 由 `:style=Bold` 改为 `:weight=200`，使 `fc-match 'Newsreader:weight=200'`
  解析到 `Newsreader-SemiBold.ttf`（与 Regular 不同文件），`build_subsets` 不再跳过 Bold 子集，
  pt 网页 PDF 8 页均嵌入 Newsreader-Bold 子集（日志 `font LucernaNewsreader-Bold: 24868 bytes`）；
  en/fr/es/it 网页 PDF（08:15–08:29 用旧代码建成）则完全没有 Newsreader-Bold
  （已用 pdffonts 逐一核实 5 版）。各语 SVG 的字体用量完全相同，故纯属构建时工具版本差异。
  pt 网页 PDF 有效（8 页、真实文字层、与印版多重集一致、< 7 MB），未用旧代码重建，
  其余四版也未用新代码重建（补丁仍在另一 agent 手中、未提交，现在重建会反复折腾）。
  协调员可在补丁定稿后决定是否以定稿工具重建其余四版网页 PDF 以求家庭一致。
- **网页 PDF 命名差异（任务简报与磁盘实证不符，待协调员裁定）**：任务简报称 en 版为
  `.web.pdf`（带点）、其余为 `-web.pdf`，"按上一轮文件名"。但磁盘实证：上一轮 de-en
  的网页文件是 `Die-Lucerna-VOL4-de-en-web.pdf`（连字符，与其余各版相同），且
  `build_edition.py` 写的就是 `-web.pdf`。本棒按磁盘上一轮文件名 + driver（`-web.pdf`）
  建成 5 版；若协调员确认简报的 `.web.pdf` 为准，en 版需改名。
- 探针：开工前及每版构建前 `git hash-object -w` + 真实写文件均通过；构建解释器
  tools/venv/bin/python（PIL 13.0.0）。工作仅限 `production/2026-w47/2026-w47-de-*/`
  与本棒笔记目录；未碰 core-de、其他家庭、tools/、issues/；未跑 insert.py / lint --write；
  未做任何 git 写操作。


- **de-en 完成（rebuild 3，重建-A，2026-11-11 08:15:54 UTC）**：ALL GATES PASS，8 版目视零问题
  （重建后撇号修复已复核），150 键复核 149/150 精确（Q150 为抽取器截断，预期内），
  P8 chip 35 / 全刊 141，KIT + text.md + ABSTRACT 已交付。独立复校待协调员另派。
- **de-fr 完成（rebuild 4，重建-A，2026-11-11 08:18:59 UTC）**：ALL GATES PASS，8 版目视
  零问题，150 键复核 149/150 精确（Q150 截断，预期内），P8 chip 35 / 全刊 141，
  KIT + text.md + ABSTRACT 已交付。独立复校待协调员另派。另补两件可复用脚本
  keycheck.py / freeze_direct.py（第 3 棒手工做的两项检查，今后 8 版直接跑）。
- **de-es 完成（rebuild 4，重建-A，2026-11-11 08:24:15 UTC）**：ALL GATES PASS，8 版目视
  零问题，150 键复核 149/150 精确（Q150 截断，预期内），P8 chip 35 / 全刊 141，
  KIT + text.md + ABSTRACT 已交付。独立复校待协调员另派。本棒新增缺陷类
  col3 box-title overflow（遮挡审计看不见，21 个标题横跨 5 语），新脚本 boxtitle.py
  （400.5px 预算）+ transform.py step-12 CJK allowlist 补丁（ja/zh-tw 用）。
- **de-it 完成（rebuild 3，重建-A，2026-11-11 08:29:28 UTC）**：ALL GATES PASS，8 版目视
  零问题，150 键复核 149/150 精确（Q150 截断，预期内），P8 chip 35 / 全刊 141，
  KIT + text.md + ABSTRACT 已交付。独立复校待协调员另派。Build 1 单一根因：
  P1 ZAHLEN 盒 362px（es 334px）跳栏致 headline 溢出 + Q6 越线，一值修复。
- **de-pt 完成（rebuild 3，重建-A，2026-11-11 08:41:14 UTC）**：ALL GATES PASS，8 版目视
  零问题，150 键复核 149/150 精确（Q150 截断，预期内），P8 chip 35 / 全刊 141，
  KIT + text.md + ABSTRACT 已交付。独立复校待协调员另派。Build 1 仅 1 门失败：
  P8 电池 A 头 "Texto com lacunas" 434.6px 超 CW 422.5，一值修复为
  "Preenchimento"（400.4px）。
- **de-nl 完成（build 1，2026-11-11 06:46 UTC，第 5 棒）**：一次通过，ALL GATES
  PASS，8 版目视零问题，150 键复核 149/150 精确（Q150 截断，预期内），P8 chip
  35 / 全刊 141，KIT + text.md + ABSTRACT 已交付。独立复校待协调员另派。无返工。
- **de-ru 完成（rebuild 2，2026-11-11 06:57 UTC，第 5 棒）**：ALL GATES PASS，8 版目视
  零问题，150 键复核 149/150 精确（Q150 截断，预期内），P8 chip 35 / 全刊 141，
  KIT + text.md + ABSTRACT 已交付。独立复校待协调员另派。Build 1 失败 3 门：
  P5-ex 溢出 122px + P5 图注压练习标题 + Q82 越页脚，两根因（P5 A 组说明折 2 行、
  2 条词条折 2 行），3 值修复。另新增缺陷类：值含 ASCII `"`（ko 写作题）致
  transform 语法错，已修为 『』；vals_*.json 为嵌套结构（values/overrides 等
  16 顶级键），直接按扁平 dict 读写会读空——已记入机制。
- **de-ja 完成（rebuild 3，2026-11-11 07:15 UTC，第 5 棒）**：ALL GATES PASS，8 版目视
  零问题，150 键复核 149/150 精确（Q150 截断，预期内），P8 chip 35 / 全刊 141，
  KIT + text.md + ABSTRACT 已交付。独立复校待协调员另派。Build 1 失败 5 门
  （P1 ZAHLEN 跳栏 2 flag + p8 compare 缺 Q150）；Build 2 遮挡修好、p8 仍缺 Q150：
  wrap 模拟 14 变体证实 kinsoku 级联固定断在 Q150 破折号后、只缩键无效；Build 3
  删 Q150 注（『Marked against the points listed』→ 空，tr diff 恰 1 行）通过——
  删注三选一：Q150 程序性评分注（H 节 + MUSTER 已含该指示）优于 Q145–149
  对话动词形态注（答案内容）。ja 为唯一无 Q150 注的版，REG 键未动。
  印版 23,901,730 B（JP CJK 字体子集，41 字体，与 ru 印版同数）；新增 CJK
  2,994（日语层），SVG 4,005 CJK 字 0 个不在 tr_ja 值内（零残留简体中文）；
  freeze_direct 渲染 8/8，源层仅 4 未计入串、皆为 transform JP 字体切换
  （ documented，transform.py 198–202 行）。
- **de-ko 完成（rebuild 2，2026-11-11 07:23 UTC，第 5 棒）**：ALL GATES PASS，8 版目视
  零问题，150 键复核 148/150（Q150 截断 + Q139 空格拼接，均为抽取器 join 伪影，
  SVG 已核实渲染正确，预期内），P8 chip 35 / 全刊 141，KIT + text.md + ABSTRACT
  已交付。独立复校待协调员另派。Build 1 仅遮挡 1 真 flag（P1 ZAHLEN 头 464.6px
  压 Q6），一值修复为 `숫자`（334.1px）；Q150 注保留完整渲染（与 ja 不同）。
  印版 15,906,995 B（韩语 CJK 字体子集）；新增 CJK 3,096（韩语层）；
  freeze_direct 源层 PASS（0 未计入）。
- **de-zh-tw 完成（build 1，2026-11-11 07:28 UTC，第 5 棒）**：一次通过，ALL GATES
  PASS，8 版目视零问题，150 键复核 149/150 精确（Q150 截断，预期内），P8 chip
  35 / 全刊 141，KIT + text.md + ABSTRACT 已交付。独立复校待协调员另派。无返工。
  印版 23,048,415 B（繁體 CJK 字体子集）；新增 CJK 1,328（繁體層）；
  freeze_direct 渲染 8/8，源层仅 4 未计入串：TC 字体切换 3 + 核心在
  07:28:39 UTC 改动的一句德文（见下「核心改动」——10 版皆为改前复数句，
  zh-tw 无缺陷）。

## 重建-B（2026-11-11 08:11–09:11 UTC，builder B：de-nl / de-ru / de-ja / de-ko / de-zh-tw）

与重建-A 同源（core-de build15，proof5 (a) 零问题，2026-11-11 08:02 UTC；唯一内容变化是
Q34 题干由复数改为单数，键 `Weihnachtsmarkt` 不变）。本波次 5 版全部从新 core 删除重建，
**5/5 建成，全部 ALL GATES PASS**。de-zh-tw 分两棒：B 棒 08:50–08:57 两次死于磁盘配额
（EDQUOT），配额清理后由续跑棒 09:05–09:11 从 webpdf 步续跑完（见下）。各版记录在
`scratch-fanout-de-rebuild-B/<lang>/EDITION-RECORD.md`，日志同目录
（nl/ru/ja/ko 为 `<lang>-rebuild-B.log`；zh-tw 为 `zh-tw-rebuild-B.log`）。

| 版 | 重建 | 完成 UTC | 印版 B (sha256 前 8) | 网页 B (sha256 前 8) | text.md B (sha256 前 8) |
|---|---|---|---|---|---|
| de-nl | 2 | 08:13:14 | 10,964,699 (8f47eea8) | 1,553,854 (be22a1b5) | 49,403 (e904fb3d) |
| de-ru | 3 | 08:20:38 | 10,954,761 (17f33460) | 1,605,337 (76f1aba7) | 56,231 (dee6697b) |
| de-ja | 4 | 08:31:53 | 23,901,736 (f412f930) | 2,113,024 (29f65fec) | 51,913 (a59f7847) |
| de-ko | 3 | 08:43:52 | 15,907,001 (d0cb457c) | 1,906,546 (fe4b835a) | 51,498 (fd2dbd04) |
| de-zh-tw | 2 | 09:11:44 | 23,048,423 (7cb79dc3) | 2,340,091 (8bfc56bd) | 49,092 (fe62ddb5) |

完整 sha256：nl 印 `8f47eea85f54067532cad3e21ba74d3ed98133a3eabc5605dcb34ca3cca8d6d6` /
网页 `be22a1b5beda4dcaaeccbcffcb7a122e01bb3f92a488d896fd261808ffc34551` /
text `e904fb3d7ee18a72c1316f8693f39436ff9390648261d6fbad18afcfb7fc848e`；
ru 印 `17f334608c1dfe2cf00ce8b955e8968fce23e53b6322dfd53986845ed995c40a` /
网页 `76f1aba78b60027a74a365bb2d189c62300dac49b5a25a476a499546531cb02a` /
text `dee6697b0ec3ff279ad4508dcc7d7402952d40fcc8670b1208a2de9158074958`；
ja 印 `f412f930242d16c87a7fb783506f6e92e5020a40e323edfdb1243dfd82db459d` /
网页 `29f65fec5681e46f5b927171163c5d66559e61ed275d998583653574d8e8294a` /
text `a59f784705bec4329b7dfa19321256c2469ab7680212302481876fc96f957f69`；
ko 印 `d0cb457ce4d856726b279f792156a005f376441a7f2353c75f7c50346235dc67` /
网页 `fe4b835a037d93c33240292af4300f5e487ac33861df66c0f33e60c374fd29d0` /
text `fd2dbd047e23bcd0fffc5245ee8d529b9e848adc11133ff46f490b304b8a66a2`；
zh-tw 印 `7cb79dc34363d7cb5456c10a5c1f63b95604fe96b4d65c7c8c339a28df5ad6de` /
网页 `8bfc56bdad2b69de907d576650903b54292d33ab99f0551370f80327cc2b0da7` /
text `fe62ddb59ac6ee2b2c474c7d11019295652e95e3c6bbd22b138fb4c7e798b0f9`。
以上数字全部与盘上实测一致（2026-11-11 09:14 UTC `sha256sum` 五版双 PDF 全量复核，
与各版 EDITION-RECORD.md 记录逐一相符；zh-tw 的记录为本次续跑后新写）。

- **每版通用门禁（全部绿）**：run.py RC=0、0 溢出；measure 24/24；precheck 0 FAIL；
  boxtitle 7/7；occlusion 0 flags；p8 抽取 150/150、compare CLEAN、keydiff [137, 138, 139, 150]
  （预期内）；freeze 8/8（渲染冻结 nl 147/163/195/166/173/175/150/186、
  ru 149/163/198/166/179/175/160/187、ja 144/164/200/166/179/173/163/183、
  ko 149/163/201/166/179/175/160/185、zh-tw 151/164/206/166/182/176/170/191——仅 P3 sha
  各版都动了，因 Q34 题干字符串本身改了，其余 7 页与上一轮逐字节一致；新增 CJK
  nl 7、ru 7、ja 2,994、ko 3,096、zh-tw 1,328）；print/web 文字层多重集一致
  （nl 50,192/50,194B、ru 57,610/57,613B、ja 52,872/52,873B、ko 52,316/52,316B、
  zh-tw 49,905/49,905B；-raw 归一化 nl 49,003B、ru 56,407B、ja 51,709B、ko 51,151B、
  zh-tw 48,777B，各版双份一致）；chips 10/15/18/15/18/18/12/35 = 141，
  P8 A2 22 / B1 13 / B2 0；P8 最小字号 9.94pt；U+2019 全扫 0；150 键复核 nl/ru/ja/zh-tw
  149/150、ko 148/150（Q139 抽取器 join 伪影 + Q150 截断，均为预期内，SVG 已核实渲染正确）。
- **Q34 核查（每版 5 处各 1× 新题干、0× 旧题干）**：源码 `content34.py`、`.text.md`、
  P3 SVG、印版文字层、网页文字层，5 版全部通过；P3 目视可见新单数题干。nl/ru/ja/ko 为
  8 版 100 dpi 全看零问题；zh-tw 因与 build 1 相比文字层只差 1 行（Q34 题干本身），只渲染了
  新网页 PDF 的 P3+P8 目视（零问题），余 6 页沿用 build 1 的 8 版目视。
- **de-zh-tw 配额中断与续跑**：B 棒 run.py + render.py 完成（印版 23,048,423 B、
  SHA `7cb79dc3…` 已核对）后，08:51 与 08:57 两次在 webpdf 步前/步中死于 EDQUOT
  （进程死、日志 0 字节）。配额清理至 78G 空闲后，续跑棒先双探针
  （`git hash-object -w` + 真实写文件）通过、每步写盘前重探，09:05–09:11 从 webpdf 续跑
  （未重跑 run.py/render.py，印版 SHA 续跑前后一致），ALL GATES PASS。
  另：zh-tw 的 WEEKLY-KIT.md 在重建开始时是 core 拷贝（重变换把 core 文件拷回了版目录），
  续跑棒已按 build-1 版 + 重建-B 新数重写回版专用 KIT。
- **网页 PDF 工具版本分裂（非内容，协调员可定夺）**：nl/ru/ja 网页 PDF（08:11–08:31）
  未嵌 Newsreader-Bold 子集；ko（08:42）与 zh-tw（09:10）嵌了额外的
  `LucernaNewsreader-Bold` 子集（各 21,596 B + PDF 对象），故网页分别比上一轮 +39,055 B
  （ko）/+39,047 B（zh-tw），而印版仅 +6 B/+8 B、text.md −1 B。ko 记录的解释是
  fontconfig 缓存再生导致 `:weight=200` 解析在 Regular 与 SemiBold 间翻转；另，
  zh-tw 构建时工作树 `tools/webpdf.py` 带有另一 agent 未提交的 fc_match 改动
  （`:style=Bold` → `:weight=200`/`:weight=100`，斜体修复进行中，09:04 UTC 测得
  `git diff --stat` 5 增 1 删）——且该文件在 zh-tw 的 webpdf 步进行中又被保存了一次
  （mtime 09:10:13 UTC），diff 此后又扩大到 90 增 17 删。两种说法指向同一机制，尚无定论
  是哪一次落地导致翻转，确切的内存中版本也无法再精确钉死——网页 PDF 均有效（8 页、
  真实文字层、与印版多重集一致、< 7 MB），未为求一致重建任何一版；补丁定稿后协调员
  可决定是否以定稿工具重建 5 版网页 PDF。另 zh-tw webpdf 日志有一条 fontTools cosmetic
  警告（Newsreader-Bold 的 fsSelection/macStyle bold 位），exit 0，文字层已验一致。
  其余共享工具（freeze.py / occlusion_audit.py / p8.py）虽也在工作树有未提交改动，但
  mtime 均在重建波次之前（11-10 22:59 / 11-11 05:01 / 11-10 21:37），5 版用的是同一版本，
  无版本分裂。
- 探针：开工前及每版构建前 `git hash-object -w` + 真实写文件均通过；续跑棒每步写盘前重探。
  构建解释器 tools/venv/bin/python（PIL 13.0.0）。工作仅限
  `production/2026-w47/2026-w47-de-*/` 与本棒笔记目录；未碰 core-de（只读）、其他家庭、
  tools/（未改）、issues/；未跑 insert.py / lint --write；未做任何 git 写操作。

## de-zh-tw 交付（build 1，最终，2026-11-11 07:28 UTC，第 5 棒）

- Print PDF: `Die-Lucerna-VOL4-de-zh-tw.pdf` — 23,048,415 bytes,
  sha256 `71693e9c011ffc4b589a3fdaba8d339cad7e9f3ebaac35ea33ea34e1d2fa8537`
- Web PDF: `Die-Lucerna-VOL4-de-zh-tw-web.pdf` — 2,301,044 bytes (< 7 MB),
  sha256 `11f58493f60fe6dce06b8f3c47095e7b5fbec5a2cb300a8d4a9074b478189cc1`
- Text: `2026-w47-de-zh-tw.text.md` — 49,093 B (42,126 chars, 591 entries, 150 exercises),
  sha256 `f82141d6224f6870f1218b1f0aa58e2f4dd7b6baa81515fc1d4239b6b3261b5f`
- ABSTRACT.txt: 294 B（繁體中文）
- Gates：run.py exit 0 零溢出、measure 24/24、verify TOTAL 150、occlusion 0 flags、
  p8 抽取 150/150 且 compare CLEAN（keydiff [137, 138, 139, 150]，预期内）、
  freeze exit 0（新增 CJK 1,328，繁體層）、freeze_direct 渲染 8/8
  （frozen 151/164/206/166/182/176/170/191；sha8 54c9b51e / 2db0dd83 / 56a81b7d /
  df1bebf7 / b42a8c3d / babfe417 / 9dc31873 / 961dd98a）；源层仅 4 未计入串：
  TC 字体切换 3（`TC`、`Noto Sans CJK TC`、`Noto Serif CJK TC`，transform.py
  的 TC 切换已备案）+ 核心改动句 1（见下）、print/web 文字层一致
  （默认 multiset 49,906 B / 49,907 B；-raw 归一化 48,778 B 双方）、
  P8 最小字号 9.94pt、U+2019 全扫 0、盒标题 8 实例全 ≤ 1862.0（最大 1825.1）
- Chips：10/15/18/15/18/18/12/35 = 141，P8 A2 22 / B1 13 / B2 0
- keycheck 149/150：仅 Q150 PREFIX（extracted `開放任務`，REG 键
  `開放任務 — 依寫作框中的要點進行`），与拉丁版一致；Q150 破折号在 wrap 中
  存活（与 ja 不同），注 `（依列出的要點評分）` 保留且完整渲染
- 目视：8 版 100 dpi 全看，零问题（renders /tmp/zhtw-proof-*.png）
- CJK 残留审计：8 个 SVG 共 2,978 个 CJK 字；唯一不在 tr_zh-tw.py 值内的
  是 `／` U+FF0F（PAGELINE_ZH_TW 的頁碼分隔符，合法家具）——零残留简体中文
- 记录：`zh-tw/EDITION-RECORD.md`（192 行，含 150 键表）、本版 WEEKLY-KIT.md（已写版内）
- Flow ends：P1-headline 1503、P1-fussball 2264、P1-quiz 2523、P2-feature 964、P2-ex 2332、
  P3-main 886、P3-ex 2333、P4-main 647、P4-ex 2315、P5-main 996、P5-ex 2441（= core）、
  P6-main 747、P6-ex 2523、P7-A2 1278 / B1 1310 / B2 1306、P8-battery 1409、P8-keys 2379
  （bottom 2560，余 181px）
- Transform 1 通过（step-12 identical-key 补丁覆盖 zh-tw 的 15 处 CJK 相同键；
  `TR_ZH_TW` 连字符 bug 已提前修复），measure1 24/24，一次通过，无返工

## 核心改动（2026-11-11 07:28:39 UTC，协调员决定——本棒不擅自定）

- 核心 `core-de/content34.py` 第 105 行在 07:28:39 UTC 被改动：冻结德文练习
  句由复数 `Am Montag öffnen in Köln die ersten ___.` 改为单数
  `Am Montag öffnet in Köln der erste ___.`。该时间在 zh-tw transform
  （07:06:31）与 zh-tw 双 PDF 生成（07:27:08 / 07:27:51）之后。
- 全部 10 版（en、fr、es、it、pt、nl、ru、ja、ko、zh-tw）均为复数句，
  与建版时核心一致；zh-tw 无缺陷，freeze_direct 源层 4 未计入串中
  除 TC 切换 3 串外即此句。
- 证实为核心侧改动（非 zh-tw 缺陷）：ja 的 freeze_direct 在建版时
  （07:15）源层仅 4 串（JP 切换），07:30 诊断重跑后变为 2 删 / 4 增，
  恰好多出此句一对；ja 渲染层 frozen 数/sha8 不变。
- 本棒不改 core-de、不替协调员决定：请协调员定——单数是否为须 10 版
  全部重 transform 的修正，或各版按建版状态交付。ja 的 WEEKLY-KIT §5 与
  EDITION-RECORD 已加注（ja/freeze-direct.json 为 07:30 诊断重跑版）。

## de-ko 交付（rebuild 2，最终，2026-11-11 07:23 UTC，第 5 棒）

- Print PDF: `Die-Lucerna-VOL4-de-ko.pdf` — 15,906,995 bytes,
  sha256 `2232d232f6b156e4c0242e5883a4f31821ded5faaa72dbcdc15a43bacc48aec1`
- Web PDF: `Die-Lucerna-VOL4-de-ko-web.pdf` — 1,867,491 bytes (< 7 MB),
  sha256 `3070faf0c58e07ef056b7deed582036f09143d031417457da84ba84655b7563d`
- Text: `2026-w47-de-ko.text.md` — 51,499 B (43,395 chars, 591 entries, 150 exercises),
  sha256 `7de85c889534ea93d96d47fea65ed869dcba578d538bb242a70761c4b334057f`
- ABSTRACT.txt: 388 B（韩语）
- Gates：run.py exit 0 零溢出、measure 24/24、verify TOTAL 150、occlusion 0 flags、
  p8 抽取 150/150 且 compare CLEAN（keydiff [137, 138, 139, 150]，预期内）、
  freeze exit 0（新增 CJK 3,096，韩语层）、freeze_direct 源层 PASS
  （0 未计入；渲染 8/8，frozen 149/163/201/166/179/175/160/185；sha8 73347f49 /
  689045ad / 14aaccaf / df1bebf7 / e7b235f9 / 2bbe05f9 / 591dc064 / f6dd4a15）、
  print/web 文字层一致（默认 multiset 52,317 B / 52,320 B；-raw 归一化 51,152 B 双方）、
  P8 最小字号 9.94pt、U+2019 全扫 0、盒标题 8 实例全 ≤ 1862.0（最大 1857.3）
- Chips：10/15/18/15/18/18/12/35 = 141，P8 A2 22 / B1 13 / B2 0
- keycheck 148/150：Q150 PREFIX（预期内）+ Q139 空格拼接伪影——两者皆已在
  P8 SVG 核实为正确渲染（见下），非内容缺陷
- 目视：8 版 100 dpi 全看，零问题（renders /tmp/ko2-proof-*.png）
- 印版 15.9 MB 为真：韩语 CJK 字体子集（字形数介于日语与西里尔之间）；网版 < 7 MB 通过
- 记录：`ko/EDITION-RECORD.md`（197 行，含 150 键表）、本版 WEEKLY-KIT.md（已写版内）
- Flow ends：P1-headline 1503、P1-fussball 2264、P1-quiz 2523、P2-feature 993、P2-ex 2332、
  P3-main 886、P3-ex 2333、P4-main 647、P4-ex 2315、P5-main 996、P5-ex 2441（= core）、
  P6-main 747、P6-ex 2523、P7-A2 1278 / B1 1310 / B2 1306、P8-battery 1409、P8-keys 2395
  （bottom 2560，余 165px）

## de-ko 两轮构建

- Build 1（07:17–07:21 UTC）：仅 2 门失败——occlusion，唯一真 flag 为 [TEXTX]
  p1-front.svg：Q6 `Der erste Advent ist am ___.` 压 ZAHLEN 头
  `DIE WOCHE IN ZAHLEN　숫자로 보는 한 주` 12.8x5.6px（日志中另 4 类 flag 为
  selftest 植入类，非真 flag）。根因：ZAHLEN 头 464.6px（盒内宽 378.5px）。
  修复 → `DIE WOCHE IN ZAHLEN　숫자`（334.1px，与 ja 的 `数字` 337.9px 同为
  裸名词模式）。word-of-week `대림절 달력(24개의 작은 문). 5쪽 참조。` 已为
  1 行（316.5px），未动。Build 1 时 p8 compare 已 CLEAN（ko 的 Q150 破折号
  在 wrap 中存活——韩语度量与日语不同，未触发 ja 的断裂）。
- Build 2（07:22–07:23 UTC）：ALL GATES PASS。一值修复（vals_ko.json 嵌套
  v['values'] 寻址；gen_tr diff 恰 1 行；boxtitle 7/7；transform-ko3.log RC 0；
  measure3 24/24）。
- keycheck 148/150 详解（皆为抽取器 join2() 跨行黏连伪影，SVG 已核实）：
  Q139 `대림절 달력을만들고 있습니다.`——SVG 第 1 行尾 `대림절 달력을`
  （y=2250.14），第 2 行首 `만들고 있습니다.`（y=2265.775），行断处空格被
  join 吞掉；Q150 `자유과제`——`자유` 行尾（y=2359.585）、`과제 — …` 行首
  （y=2375.22），同理 + 预期内 PREFIX 截断。Q150 注
  `（나열된 항목으로 채점）` 保留且完整渲染（与 ja 删注不同）。
- Transform 1 曾因 ASCII `"` 语法错失败（写作题标题引号终止双引号字符串）
  ——修复为韩式书名号 `『11월의 나의 한 주』`；8 语 vals 全扫确认仅此一处
  含 ASCII `"`（其余皆为 p8sep/pageline 结构性 f-string 包装）。

## de-ja 交付（rebuild 3，最终，2026-11-11 07:15 UTC，第 5 棒）

- Print PDF: `Die-Lucerna-VOL4-de-ja.pdf` — 23,901,730 bytes,
  sha256 `19d5a14a2966e6865a8bfb28bd74fd0c05b10594a37670fe7db4d84596e5605a`
- Web PDF: `Die-Lucerna-VOL4-de-ja-web.pdf` — 2,113,005 bytes (< 7 MB),
  sha256 `8dc87c2363a02cb2b098f55614e3866b31f5796c91ea6e8d3d393fbfbb66236d`
- Text: `2026-w47-de-ja.text.md` — 51,914 B (42,951 chars, 591 entries, 150 exercises),
  sha256 `c780542f0835bdaef6cfd52939346ecec6daa06d6b0edb4e348201942b2a3951`
- ABSTRACT.txt: 426 B（日语）
- Gates：run.py exit 0 零溢出、measure 24/24、verify TOTAL 150、occlusion 0 flags、
  p8 抽取 150/150 且 compare CLEAN（keydiff [137, 138, 139, 150]，预期内：
  137–139 为译成日语题，150 为 Q150 PREFIX）、freeze exit 0（新增 CJK 2,994，日语层）、
  freeze_direct 渲染 8/8（frozen 144/164/200/166/179/173/163/183；源层仅 4 未计入串，
  皆为 transform JP 字体切换，见 KIT §5）、print/web 文字层一致
  （默认 multiset 52,873 B / 52,874 B；-raw 归一化 51,710 B 双方）、P8 最小字号 9.94pt、
  U+2019 全扫 0、盒标题 8 实例全 ≤ 1862.0（最大 1849.1）
- Chips：10/15/18/15/18/18/12/35 = 141，P8 A2 22 / B1 13 / B2 0
- keycheck 149/150：仅 Q150 PREFIX（extracted `自由課題`，REG 键
  `自由課題 — 枠のポイントに従おう`），与拉丁版一致
- 目视：8 版 100 dpi 全看，零问题（renders /tmp/ja3-proof-*.png）
- 印版 23.9 MB 为真：JP CJK 字体子集多（print 41 字体，web 34 字体；ru 印版同为 43 字体行）；
  无门禁查印版大小，网版 < 7 MB 通过
- CJK 残留审计：8 个 SVG 共 4,005 个 CJK 字，0 个不在 tr_ja.py 值内——零残留简体中文
- 记录：`ja/EDITION-RECORD.md`（194 行，含 150 键表）、本版 WEEKLY-KIT.md（已写版内）
- Flow ends：P1-headline 1503、P1-fussball 2264、P1-quiz 2523、P2-feature 993、P2-ex 2332、
  P3-main 916、P3-ex 2333、P4-main 677、P4-ex 2315、P5-main 996、P5-ex 2441（= core）、
  P6-main 747、P6-ex 2496、P7-A2 1278 / B1 1342 / B2 1306、P8-battery 1409、P8-keys 2473
  （bottom 2560，余 87px）

## de-ja 三轮构建

- Build 1（06:58–07:01 UTC）：失败 5 门——occlusion 2 flags（P1 ZAHLEN 盒跳栏：
  word-of-week 折 2 行越 hline；ZAHLEN 头 457.9px 压 Q6）+ p8 compare SHORT 缺 [150]。
  修复：ZAHLEN 头 → `DIE WOCHE IN ZAHLEN　数字`（337.9px）；word-of-week →
  `アドベントカレンダー（24の小窓）。5ページ。`（410.5px，1 行）；Q150 键缩短为
  `自由課題 — 枠のポイントに従おう`。
- Build 2（07:06–07:08 UTC）：occlusion 修好，p8 compare 仍缺 [150]。wrap 模拟证实：
  P8 keys 段 kinsoku 级联固定断在 Q150 破折号后（行尾 `—`），与键尾长度无关——
  破折号在 CJK 行首断裂时丢后空格，join2() 黏连，抽取器 `" — " in seg` 失效；
  且页脚（`Die Lucerna　ドイツ語週刊…` + `8 / 8 ページ`）不合 FOOTER_RE，注后括号
  不是末尾。14 个模拟变体：只删整条注（Q147/Q148/Q149 对话注或 Q150 注）能移断点，
  所有只缩短的变体（Q150 注缩短、Q149 注缩短、Q150 键改写等 8 个）全失败。
- Build 3（07:11–07:15 UTC）：ALL GATES PASS。修复：Q150 注删空
  （vals_ja.json 嵌套 v['values']['Marked against the points listed'] → ''；
  gen_tr diff 恰 1 行；transform-ja4.log RC 0；measure4 24/24）。决策理由：
  Q150 注为程序性评分说明（H 节 + MUSTER 框已含该指示），Q145–149 注为
  变位练习的答案内容（动词形态 + 人称），后者不可丢；ja 因此成为唯一无 Q150 注
  的版，REG 键未动，keycheck 仍 149/150（Q150 PREFIX）。
- 教训（07:05 UTC）：绝不裸 import 版内 content*.py——直接 import content8.py
  执行了模块级建页，把 `svg/p8-uebungen.svg` 覆盖为独立变体（38 题）；
  rebuild 2 重建后恢复。检查用 AST 解析或 keycheck.py 的 stub 机制（stub_svg /
  stub_bslib + W46_BUILD_DIR），不用裸 import。
- Transform 1 曾因 step-12 相同键 CJK 误报失败（`LEBEN　生活` 等 3 处）——
  transform.py identical-key 补丁已修（键值相同时为合法读者语串）；zh-tw
  同类 15 处已由该补丁覆盖。

## de-nl 交付（build 1，最终，2026-11-11 06:46 UTC，第 5 棒）

- Print PDF: `Die-Lucerna-VOL4-de-nl.pdf` — 10,964,692 bytes,
  sha256 `bb54120a55d5de272c17061f84a363ac14f1820b2353e1490e9dcb75d8444e53`
- Web PDF: `Die-Lucerna-VOL4-de-nl-web.pdf` — 1,553,848 bytes (< 7 MB),
  sha256 `74a0ecddea5427ea4d724760cc1e46733745b188683d3184dac771e12c65a9bb`,
  50,195 text bytes
- Text export: `2026-w47-de-nl.text.md` — 49,404 bytes, 47,762 chars, 591 entries,
  150 exercises, sha256 `d02aa27e21e8f1d8f2338a97e3d05a42cab6a105d95fbb4debfa80fb3d5613a7`
- ABSTRACT.txt（荷兰语，一行，无 ASCII `"`）；WEEKLY-KIT.md（build 1 值）已写。
- 门禁（build 1 一次通过）：run.py exit 0 零溢出 TOTAL 150；measure 24/24；
  verify TOTAL 150；occlusion 0 flags；p8 抽取 150/150，compare CLEAN，
  keydiff [137, 138, 139, 150]（预期内：137–139 正向翻译、150 开放写作题；
  Q140 反向题键即德语句子，不 diff）；freeze diff exit 0（新增 CJK 7 个，全为
  U+3000，P2–P8 各 1）；freeze_direct 8/8（源码 0 未入账；渲染冻结
  147/163/195/166/173/175/150/186，sha 与 en/fr/es/it/pt 相同）；print/web 文字层：
  默认多重集一致（50,193B / 50,195B），-raw 归一化完全一致（49,004B）；chips
  10/15/18/15/18/18/12/35 = 141，P8 A2 22 / B1 13 / B2 0；P8 最小字号 9.94pt
  （≥ 9.75pt）；U+2019 全扫 0；150 键 149/150 精确（Q150 "Open opdracht — volg
  de punten in het schrijfblok" 被抽取器截断为 "Open opdracht"，预期内）。
- 目视：build 1 印版 100 dpi 渲染 P1–P8 逐版看过，零问题；另 SVG 级扫描 7 个
  col3 盒标题（8 处，含 P6 全宽盒），全部收进盒内（最大 1857.0，盒边 1862.0，
  DER WERKZEUGKASTEN "Werktuig" 余 5.0px，确定性通过）。
- 记录：`nl/EDITION-RECORD.md`（门禁日志 + 150 键表）；日志 `nl/rebuild1.log`、
  `nl/build.log`、`nl/measure1.log`、`nl/keycheck-150.json`、`nl/freeze-direct.json`。
- 本版无返工：build 1 即全部通过。验证期两处值修复（gloss 前缀 "Opgelet — " →
  "Uitleg — "；键拼写 "beginnen → begint" → "beginnen → beginnt"）均在 build 1
  之前完成；盒标题 4 处缩短（STILLE → "Stille week"、WEIHN → "Kerst"、ADVENTS →
  "Advent"、TOOLBOX → "Werktuig"）亦在 build 1 之前。

## de-ru 交付（rebuild 2，最终，2026-11-11 06:57 UTC，第 5 棒）

- Print PDF: `Die-Lucerna-VOL4-de-ru.pdf` — 10,954,755 bytes,
  sha256 `74fac6aa22cf181614ff3fb40f267547f54859bcd072bc3dc17f78cc0ca9144e`
- Web PDF: `Die-Lucerna-VOL4-de-ru-web.pdf` — 1,605,334 bytes (< 7 MB)，
  57,614 text bytes，
  sha256 `8f9b83e799ed2afafb96e94e862e434f487803203143f7cc7f1fafd3b1a664cf`
  （大于拉丁版约 1.55MB——西里尔字体子集）
- Text export: `2026-w47-de-ru.text.md` — 56,232 bytes，47,595 chars，591 entries，
  150 exercises，sha256 `e5d6bd0ba28ec910f83155c2cda4b38423a2000419c142ddd36d42e2bafcde16`
- ABSTRACT.txt（俄语，一行，无 ASCII `"`）；WEEKLY-KIT.md（rebuild 2 值，15,097 B）已写。
- 门禁（rebuild 2 全部通过）：run.py exit 0 零溢出 TOTAL 150；measure 24/24；
  verify TOTAL 150；occlusion 0 flags；p8 抽取 150/150，compare CLEAN，
  keydiff [137, 138, 139, 150]（预期内：137–139 正向翻译、150 开放写作题；
  Q140 反向题键即德语句子，不 diff）；freeze diff exit 0（新增 CJK 7 个，全为
  U+3000，P2–P8 各 1）；freeze_direct 8/8（源码 0 未入账；渲染冻结
  149/163/198/166/179/175/160/187，P2/P4/P6 的 sha8 与拉丁版相同，P1/P3/P5/P7/P8
  的冻结数更高——俄版 SVG 渲染文本元素更多（P1 207 对 178），多出的纯德语行与
  核心行重合，交集变大，是分行差异不是内容差异）；print/web 文字层：
  默认多重集一致（57,611B / 57,614B），-raw 归一化完全一致（56,408B）；chips
  10/15/18/15/18/18/12/35 = 141，P8 A2 22 / B1 13 / B2 0；P8 最小字号 9.94pt
  （≥ 9.75pt）；U+2019 全扫 0；150 键 149/150 精确（Q150 "Свободное задание —
  следуйте пунктам из рамки письма" 被抽取器截断为 "Свободное задание"，预期内）。
  另：P8-keys 落点 2545（底 2560，仅余 15px）——通过但最紧，俄版 P8 增量须盯。
- 目视：rebuild 2 印版 100 dpi 渲染 P1–P8 逐版看过，零问题；另 SVG 级扫描 7 个
  col3 盒标题（8 处，含 P6 全宽盒），全部收进盒内（最大 1853.4，盒边 1862.0，
  LESERBRIEFE "Письма читателей" 余 8.6px）。P5 重点复核：1903 日历图 + 图注已
  远离 ÜBUNGEN 标题，Q68 回到第 1 栏，Q82 远离页脚。
- 记录：`ru/EDITION-RECORD.md`（门禁日志 + 150 键表，236 行）；日志
  `ru/rebuild2.log`、`ru/build.log`、`ru/measure2.log`、`ru/keycheck-150.json`、
  `ru/freeze-direct.json`。
- Build 1 失败 3 门（2026-11-11 06:48–06:52 UTC）：FLOW OVERFLOW [P5-ex]
  （flow 落点 y=2682，超 122px）+ occlusion 3 flags（全在 p5-jugend.svg：图注
  第 2 行压 ÜBUNGEN 标题——TEXTX；Q82 行越页脚横线——LINEX）。两根因均在 SVG
  中量出：（1）P5 A 组说明 "Прочитайте стр. 5 и выберите правильный ответ."
  折 2 行，每道 A 题 +30px，Q68 被挤出第 1 栏（P5-ex +241px）；（2）P5 词条框
  2 条在 377.5px 盒宽、serif 21.5pt 下折 2 行（"der Wunschzettel — список
  желаний" 380.6px、"das Christkind — Младенец Христос" 382.3px），col3 叠高
  +61px，图顶进标题。3 值修复（diff 恰 3 行）：说明 → "Прочитайте стр. 5 и
  выберите ответ."（1 行）；"das Christkind — Младенец Христос" → "Младенец"；
  "der Wunschzettel — список желаний" → "желания"。重建后词条框落点 979.36
  （= it）、图落点 1732.93（= it）、P5-ex 落点 2441（= core）。未动：第 96 行
  独立键 "Младенец Христос" 与 P8 键 "Wunschzettel=список желаний"。同轮亦
  修盒标题 4 处（Тишина / Слова / Адвент / Справка）。
- 本棒新增教训（ko transform 失败，见下）：**值里不得含 ASCII `"`**——ko
  写作题 "11월의 나의 한 주" 的 ASCII 引号使 transform 吐出的 content8.py
  双引号字符串提前闭合，SyntaxError；已改为 『』（tr diff 恰 1 行，transform
  2 + measure 24/24 已过）。**vals_*.json 是嵌套结构**（values/overrides/
  p8sep/pageline/ed_spacing 等 16 个顶级键，values 内 273 条）：直接对顶层
  dict 按扁平键读写会读空（本次误判为"值已消失"并用 json.dump 原样重写了一
  次，所幸 round-trip 无损，273 值完好、gen_tr 仍出 278 键）；以后改值一律
  先确认层级（v['values'][key]），并用 gen_tr diff 行数验。

## de-pt 交付（rebuild 2，2026-11-11 06:40 UTC，第 5 棒；上一轮记录，已被重建-A supersede，见报告顶部「重建-A」一节）

- Print PDF: `Die-Lucerna-VOL4-de-pt.pdf` — 10,968,902 bytes,
  sha256 `d946e0184638857c6e7800faa54570815245496e0c48316af75bd4d4582c0c5a`
- Web PDF: `Die-Lucerna-VOL4-de-pt-web.pdf` — 1,559,382 bytes (< 7 MB),
  sha256 `a86ce50df519bee26a5fa4858ac17079306b9f15929fc5e88f5c6c1a7d1c081d`,
  50,688 text bytes
- Text export: `2026-w47-de-pt.text.md` — 49,813 bytes, 47,948 chars, 591 entries,
  150 exercises, sha256 `496e931a201ea78df436ef5a25a9404d773e898cbd66e0da4e5abe719cca6462`
- ABSTRACT.txt（葡萄牙语，一行，无 ASCII `"`）；WEEKLY-KIT.md（rebuild 2 值）已写。
- 门禁：run.py exit 0 零溢出 TOTAL 150；measure 24/24；verify TOTAL 150；
  occlusion 0 flags；p8 抽取 150/150，compare CLEAN，keydiff [137, 138, 139, 150]
  （预期内：137–139 正向翻译、150 开放写作题；Q140 反向题键即德语句子，不 diff）；
  freeze diff exit 0（新增 CJK 7 个，全为 U+3000，P2–P8 各 1）；freeze_direct 8/8
  （源码 0 未入账；渲染冻结 147/163/195/166/173/175/150/186，sha 与 en/fr/es/it
  相同）；print/web 文字层：默认多重集一致（50,685B / 50,688B），-raw 归一化完全
  一致（49,501B）；chips 10/15/18/15/18/18/12/35 = 141，P8 A2 22 / B1 13 / B2 0；
  P8 最小字号 9.94pt（≥ 9.75pt）；U+2019 全扫 0；150 键 149/150 精确
  （Q150 "Tarefa livre — segue os pontos do quadro de escrita" 被抽取器
  截断为 "Tarefa livre"，预期内）。
- 目视：rebuild 2 印版 100 dpi 渲染 P1–P8 逐版看过，零问题；另 SVG 级扫描 7 个
  col3 盒标题（8 处，含 P6 全宽盒），全部收进盒内（最大 1849.6，盒边 1862.0，
  NOCH EIN WORT 余 12.4px）。
- 记录：`pt/EDITION-RECORD.md`（门禁日志 + 150 键表）；日志 `pt/rebuild2.log`、
  `pt/build.log`、`pt/measure2.log`、`pt/keycheck-150.json`、`pt/freeze-direct.json`。

## de-pt 两轮构建

- Build 1（06:32–06:35 UTC）：仅 1 门失败 — 'no HEAD TOO WIDE'：P8 电池 A 头
  "A　LÜCKENTEXT　Texto com lacunas" 24pt 下 434.6px，超 CW 422.5（超 12.1px）。
  其余全过（occlusion 0 flags，chips 141，p8 CLEAN，freeze exit 0，P8 最小字号
  9.94pt，P8-battery 止 1409，P8-keys 止 2457），无跳栏、无级联溢出。本家庭新缺陷
  类：P8 电池头超栏宽（es build 1 的 F 头 525.6px 同类；pt 仅超 12.1px）。
- 流程教训（记入本报告，勿再犯）：第一次 build 1 启动后 10 秒即被我停掉——因为
  measure 命令漏写 $S/ 路径（在 /home/hatch 下跑 `measure.py`，文件不存在，RC 2），
  却先启动了构建。重跑正确 measure（24/24）后才重启动。顺序永远是 measure 先、
  build 后，不可倒置。
- 修复（`vals_pt.json`，重生成 tr_pt.py，diff 恰 1 行）：P8 A 头
  "Texto com lacunas" → "Preenchimento"（400.4px，通过，余 22px；葡语完形填空
  标准词；另测 "Lacunas" 315.9、"Texto lacunar" 377.7）。版目录删除重 transform，
  measure 24/24。
- Rebuild 2（06:36–06:40 UTC）：ALL GATES PASS；目视零问题。

## de-it 交付（rebuild 2，2026-11-11 06:29 UTC，第 5 棒；上一轮记录，已被重建-A supersede，见报告顶部「重建-A」一节）

- Print PDF: `Die-Lucerna-VOL4-de-it.pdf` — 10,965,089 bytes,
  sha256 `8c9c1d4fb3ce889530ef1e424a9eba9d7a4c5e758667607852ea8ac4b1e8482c`
- Web PDF: `Die-Lucerna-VOL4-de-it-web.pdf` — 1,553,866 bytes (< 7 MB),
  sha256 `9c01c2f3123ed38f332882c68c1fc0c8a9e876cd2bf8b6d2fbf50c063bc1d571`,
  50,598 text bytes
- Text export: `2026-w47-de-it.text.md` — 49,713 bytes, 48,033 chars, 591 entries,
  150 exercises, sha256 `5f3332f13de35e9206c397eac37eacc1fbca8a973b00231bfa3b6029b0835da7`
- ABSTRACT.txt（意大利语，一行，无 ASCII `"`）；WEEKLY-KIT.md（rebuild 2 值）已写。
- 门禁：run.py exit 0 零溢出 TOTAL 150；measure 24/24；verify TOTAL 150；
  occlusion 0 flags；p8 抽取 150/150，compare CLEAN，keydiff [137, 138, 139, 150]
  （预期内：137–139 正向翻译、150 开放写作题；Q140 反向题键即德语句子，不 diff）；
  freeze diff exit 0（新增 CJK 7 个，全为 U+3000，P2–P8 各 1）；freeze_direct 8/8
  （源码 0 未入账；渲染冻结 147/163/195/166/173/175/150/186，sha 与 en/fr/es 相同）；
  print/web 文字层：默认多重集一致（50,594B / 50,598B），-raw 归一化完全一致
  （49,393B）；chips 10/15/18/15/18/18/12/35 = 141，P8 A2 22 / B1 13 / B2 0；
  P8 最小字号 9.94pt（≥ 9.75pt）；U+2019 全扫 0；150 键 149/150 精确
  （Q150 "Esercizio libero — segui i punti del riquadro di scrittura" 被抽取器
  截断为 "Esercizio libero"，预期内）。
- 目视：rebuild 2 印版 100 dpi 渲染 P1–P8 逐版看过，零问题；另 SVG 级扫描 7 个
  col3 盒标题（8 处，含 P6 全宽盒），全部收进盒内（最大 1856.5，盒边 1862.0，
  NOCH EIN WORT 余 5.5px，确定性通过）。
- 记录：`it/EDITION-RECORD.md`（门禁日志 + 150 键表）；日志 `it/rebuild2.log`、
  `it/build.log`、`it/measure2.log`、`it/keycheck-150.json`、`it/freeze-direct.json`。

## de-it 两轮构建

- Build 1（06:18–06:23 UTC）：3 门失败，单一根因在 P1 — FLOW OVERFLOW
  [P1-headline]（流止 1921，底 1828）+ occlusion LINEX ×2（Q6 的 B1 芯片与
  "6." 越过 row-B 横线 y=1844）。SVG 度量定位：ZAHLEN 盒高 362px（es 334px），
  其第 2 项在 378.5px 内宽下绕成 3 行（"(Bayern-Colonia, ore / 20.30)"），盒子
  装不进第 1 栏 gloss 后的余量而跳到第 2 栏，把 JETZT ÜBEN 下推 362px 压进图区
  （与 fr build 1 的 ZAHLEN 跳栏同类）。Build-1 P1 渲染目视证实：ZAHLEN 在第 2
  栏顶，Q6 "Der erste Advent ist am" 压住 "EINE WOCHE, ZWEI STIMMUNGEN" 标题。
- 修复（`vals_it.json`，重生成 tr_it.py，diff 恰 1 行）：ZAHLEN 第 2 项
  "(Bayern-Colonia, ore 20.30)" → "(Bayern-Colonia 20.30)"（去 ", ore"；
  378.5px 内宽下 2 行）。版目录删除重 transform，measure 24/24。
- Rebuild 2（06:25–06:29 UTC）：ALL GATES PASS；P1-headline 止 1554 = 核心版。
  目视零问题。

## de-es 交付（rebuild 3，2026-11-11 06:14 UTC，第 5 棒；上一轮记录，已被重建-A supersede，见报告顶部「重建-A」一节）

- Print PDF: `Die-Lucerna-VOL4-de-es.pdf` — 10,968,797 bytes,
  sha256 `2c535a10f81516a749c56fa43290bc54c5bd268ba36469caa10367bc944395ed`
- Web PDF: `Die-Lucerna-VOL4-de-es-web.pdf` — 1,558,812 bytes (< 7 MB),
  sha256 `b20ceebfeba6c5e7ad2be9d2123b8406755bceff0174f34c6ca4158e03716228`,
  51,014 text bytes
- Text export: `2026-w47-de-es.text.md` — 50,125 bytes, 48,287 chars, 591 entries,
  150 exercises, sha256 `b36e21f45810821a28855186fe67739927e18f2aff30ef56672e3fda44753d48`
- ABSTRACT.txt（西班牙语，一行，无 ASCII `"`）；WEEKLY-KIT.md（rebuild 3 值）已写。
- 门禁：run.py exit 0 零溢出 TOTAL 150；measure 24/24；verify TOTAL 150；
  occlusion 0 flags；p8 抽取 150/150，compare CLEAN，keydiff [137, 138, 139, 150]
  （预期内：137–139 正向翻译、150 开放写作题；Q140 反向题键即德语句子，不 diff）；
  freeze diff exit 0（新增 CJK 7 个，全为 U+3000，P2–P8 各 1）；freeze_direct 8/8
  （源码 0 未入账；渲染冻结 147/163/195/166/173/175/150/186，sha 与 en/fr 相同）；
  print/web 文字层：默认多重集一致（51,013B / 51,014B），-raw 归一化完全一致
  （49,813B）；chips 10/15/18/15/18/18/12/35 = 141，P8 A2 22 / B1 13 / B2 0；
  P8 最小字号 9.94pt（≥ 9.75pt）；U+2019 全扫 0；150 键 149/150 精确
  （Q150 "Tarea libre — sigue los puntos del recuadro de escritura" 被抽取器
  截断为 "Tarea libre"，预期内）。
- 目视：rebuild 3 印版 100 dpi 渲染 P1–P8 逐版看过，零问题；另 SVG 级扫描 7 个
  col3 盒标题（8 处，含 P6 全宽盒），全部收进盒内（最大 1849.1，盒边 1862.0）。
- 记录：`es/EDITION-RECORD.md`（门禁日志 + 150 键表）；日志 `es/rebuild3.log`、
  `es/build.log`、`es/measure3.log`、`es/keycheck-150.json`、`es/freeze-direct.json`。

## de-es 三轮构建

- Build 1（05:42–05:47 UTC）：3 门失败 — P8 电池 F 头过宽（"F　WÖRTER PAAREN
  Palabras emparejadas" 525.6px > CW 422.5）+ occlusion 4 flags（P3 标题墨
  1987.75；P7 工具箱标题 1994.75；P8 同 F 头 1965.0；P3 LINEX 提示第 3 行基线
  1623.66 越过练习规则线 1608）。其余全过（chips 141、p8 CLEAN、freeze 0）。
- Build 2（05:55 UTC）：ALL GATES PASS，但目视发现**新缺陷类 col3 box-title
  overflow**（遮挡审计只看 1950 页边，看不见）：5 个标题长于 400.5px 盒预算，
  墨水漫出米色盒底印到新闻纸上（STILLE 超 84.0、TIPP 超 10.1、ADVENTSWÖRTER
  超 83.4、WERKZEUGKASTEN 超 47.5、LESERBRIEFE 超 15.0）。en 对照干净、fr 贴盒边，
  是真缺陷不是设计。
- Rebuild 3（06:08–06:14 UTC）：5 标题缩短（Tranquila / Consejo / Adviento /
  Útiles / Cartas），新脚本 `boxtitle.py`（7/7）。ALL GATES PASS + 目视零问题。
- 同类横扫：boxtitle.py 对 8 语全跑，21 个标题横跨 5 语（it 4、pt 3、nl 4、
  ru 4、ja 1，es 5）已在 transform 前改短并复核 7/7；ko、zh-tw 0 超。en/fr
  自身值干净，不动。

## 第 5 棒机制修补（scratch-fanout-de/，core 只读未动）

- `gen_tr.py`：由 tr_en.py 键序 + vals_<lang>.json 生成 tr_<lang>.py（278 键；
  EN 值碰撞 2 处用中文键 override；INSTRMAP 新值自动包 `instr="..."`；
  单引号内 `'` 写 `\u0027`，U+3000 写 `\u3000`；断言无 U+2019、无 ASCII `"`
  在 ABSTRACT 内、键集 == TR_EN）。es/it/pt/nl/ru/ja/ko/zh-tw 8 份已生成并校验
  （273/273 值全覆盖）。首版漏包 instr 致 transform 语法错，已修。
- `precheck.py`：transform 前镜像 measure 1–12 项 + 建议 ED_SPACING 上限；
  8 语 0 FAIL。
- `boxtitle.py <lang>`：7 个 col3 盒标题按 400.5px 预算度量（标题 x=1461.5，
  盒右 1862.0；P2 STILLE / P3 WEIHNACHTSWÖRTER / P3 DER TIPP / P5
  ADVENTSWÖRTER 24pt，P7 WERKZEUGKASTEN / LESERBRIEFE 23pt，P7 NOCH EIN WORT
  22pt），7/7 才过。transform 前必跑。
- `transform.py` step-12 CJK allowlist 补丁（2026-11-11）：拉丁/西里尔读者保持
  严格扫描（任一 CJK 即失败）；ja/zh-tw 改 allowlist 模式 — 含 CJK 的字面量
  仅当等于或是 tr_<lang>.py 字面量（含 f-string 片段）的子串才通过（子串须 ≥2
  字），且 TR 键本身永不入 allowlist；另加独立断言：无 CJK TR 键残留在任何
  字面量内（自查已证：tr 值中不含 CJK 键；核心 CJK 字面量除 TR 键外只有
  TYPEMAP/分页片段/「桥接」探针，均由 transform 替换或不在扫描集内）。
  it transform 已用补丁版跑过，step-12 干净，拉丁行为不变。
- `TR_ZH_TW` 连字符 bug 修：`UP = LANG.upper()` 产生非法标识符 `TR_ZH-TW`；
  8 个脚本统一 `UP = LANG.upper().replace("-", "_")`，tr_zh-tw.py 已重生成，
  boxtitle 7/7 + precheck 0 FAIL 已确认。
- LAYOUT ey 1620 → 1680 已写入 8 语的 layout_extra（es 证实 3 行 undsie 提示
  需此下移；en 前例同）。

## 第 5 棒待办（全部完成 — 10/10）

- 8 版全部完成：es（rebuild 3）、it（rebuild 2）、pt（rebuild 2）、nl（build 1）、
  ru（rebuild 2）、ja（rebuild 3）、ko（rebuild 2）、zh-tw（build 1）。
  每版 EDITION-RECORD.md + WEEKLY-KIT.md 已写，报告结论已更新为 10/10。
- 待 parent（协调员）决定（不擅自定）：
  1. CJK 读者版 freeze `--strict-cjk` 字面无法通过（读者语解释层本身加 CJK；
     en 家庭前例：记录新增 CJK 总量 + 核查零残留简体中文串，freeze_direct 8/8
     作严格证明）。本棒按此处理：ja 2,994 / ko 3,096 / zh-tw 1,328，残留审计皆为 0
     （zh-tw 唯一例外为 PAGELINE 分隔符 ／，合法家具）。
  2. **核心改动（2026-11-11 07:28:39 UTC）**：core-de/content34.py 第 105 行德文
     练习句由复数改为单数（`Am Montag öffnen in Köln die ersten ___.` →
     `Am Montag öffnet in Köln der erste ___.`），在全部 10 版建版之后。
     10 版皆为复数句。需协调员定：单数是否为须 10 版全部重 transform 的修正，
     或各版按建版状态交付。本棒未改 core-de，未重 transform 任何版。
- zh-tw：tr + precheck + boxtitle 已齐，待 transform（step-12 identical-key
  补丁已就位；`TR_ZH_TW` 命名）。
- 待 parent 决定（不擅自定）：CJK 读者版 freeze `--strict-cjk` 字面无法通过
  （读者语解释层本身加 CJK；en 家庭前例：记录新增 CJK 总量 + 核查零残留简体中文
  串，freeze_direct 8/8 作严格证明）。本棒按此处理并在终报明说。

## de-en 交付（rebuild 2，2026-11-11 02:53 UTC；上一轮记录，已被重建-A supersede，见报告顶部「重建-A」一节）

- Print PDF: `Die-Lucerna-VOL4-de-en.pdf` — 10,966,416 bytes,
  sha256 `a997c6cefe8467bdd37a71158e0f61ceff16d653039f50159b1608305b3a4b87`
- Web PDF: `Die-Lucerna-VOL4-de-en-web.pdf` — 1,555,614 bytes (< 7 MB),
  sha256 `62623cb5996644004ba48a6ed7246cdd0584bec3a2549123174db318384a3a90`
- Text: `2026-w47-de-en.text.md` — 49,676 bytes, 48,045 chars, 591 entries, 150 exercises,
  sha256 `0749ad78f536883f8f3a484d7c93f026d0f7d7f433891861333f7a9a8fbf3830`
  （源稿导出，绝不从 PDF 倒抽）
- ABSTRACT.txt：一行英文，356 字节，无 ASCII 双引号。
- WEEKLY-KIT.md：已写（en 版完整记录，见版内文件）。
- 门禁（build_edition.py en，rebuild2.log）：run.py exit 0、零 FLOW OVERFLOW /
  HEAD TOO WIDE；measure 24/24；verify TOTAL 150、编号连续、SVG 字节一致、§1.1
  审计 True、verbatim OK、P8 floor True、17 项禁词全无；occlusion 0 flags；p8
  extract 150/150、compare CLEAN、keydiff [137, 138, 139, 150]（预期内）；
  freeze diff exit 0（新增 CJK 仅 7 个 U+3000）；print/web 文字层多重集一致、
  raw 归一化一致；chips 10/15/18/15/18/18/12/35 = 141，P8 A2 22 / B1 13；
  P8 最小字号 9.94pt ≥ 9.75pt；export exit 0。
- Freeze 直接比对 8/8（工具 baseline 自报 0/8 是已知重定向局限，以直接 sha256 为准）：
  (a) 源码级：核心全部 2033 个无 CJK 字符串常量在 en 版中同数存在，仅 8 处缺失均为
  预期 transform 产物（masthead 副标题、全角括号、间隔符、PDF 名、verify 文档/路径）；
  新增无 CJK 字符串全为英文（TR/TYPEMAP/INSTRMAP 值或格式片段）；
  (b) 渲染级：核心与 en 版 SVG 交集（冻结字符串）逐页 P1 147 / P2 163 / P3 195 /
  P4 166 / P5 173 / P6 175 / P7 150 / P8 186，sha256 083e2a2a / 689045ad / 093cf378 /
  df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7。
- 150 键复核（`en/keycheck-150.json`）：P8 SVG 抽取键 vs 版内源 REG 逐题比对，
  **149/150 精确**；唯一非精确项为 Q150（开放写作题，抽取器把 REG 键
  "Open task — follow the points in the writing box" 截断为 "Open task"，预期内，
  Q150 已在 keydiff 集合中）。REG 分页 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12,
  8:38}，级别 A2 69 / B1 67 / B2 14。
- 目视：8 版自 print PDF 100 dpi 渲染逐版目视 + 5 处放大裁切复核，零问题
  （P1–P8 逐版记录见 `en/` 下的 gate logs 与本报告"de-en 目视"一节）。
  唯一发现并修复的缺陷：英文弯撇号 U+2019 在 Noto Sans CJK SC 中渲染为宽字形
  （"Let' s calculate"），9 处已改为直撇号 U+0027（`\u0027` 转义），rebuild 2
  复核通过，8 SVG 中 U+2019 总数 0。教训已写入 tr_en.py 注释与 KIT §7：
  其余 9 版一律用直撇号，并把 U+2019 扫描加入每版自查。
- 核心源未变：content8.py sha256 仍为
  `9b690738c88bdc42f118948aab86fca030d3eb598dd4a52cfe69205d942279b4`
  （与本棒开工时一致）；transform 前已核对。
- 开工探针（本棒 2026-11-11 01:30 UTC）：`git hash-object -w` 通过、
  scratch 真实写文件通过；磁盘 150G 总、97G 已用、53G 空闲——配额已恢复，
  未再遇 Errno 122。

## de-en 目视（8 版，上一版渲染 + 重建后撇号复核）

- P1：头版、桥接、数字盒、JETZT ÜBEN、FRAGEN 侧栏、IN DIESER AUSGABE、
  DAS WORT DER WOCHE、足球图+图注、KURZ & GUT、BLITZQUIZ、页脚均干净。
  "Germany's five hot questions"（直撇号）渲染紧贴，为对照。
- P2：文章、Note  gloss 盒、四侧栏（DER BUß- UND BETTAG / WUSSTEN SIE DAS? /
  UND SIE? / DIE STILLE WOCHE）、RECHNEN 表、练习 A–D 干净。缺陷仅 "Let' s
  calculate" / "This week' s dates" 弯撇号——重建后裁切复核已紧贴。
- P3：文章、Note 盒、1930 圣诞市场图+图注、WEIHNACHTSWÖRTER、UND SIE?、
  DER TIPP、练习 A–D 干净；图在横线之上。缺陷仅 "Editor' s tip"——已修复复核。
- P4：文章、Note 盒、头球图+图注、UND SIE? 盒与结果表边缘相接无重叠、
  9 行结果表、练习 A–D 干净。缺陷仅 "league' s return"——已修复复核。
- P5：文章、Note 盒、ADVENTSKALENDER/ADVENTSWÖRTER、UND SIE?（2 行提示）、
  1903 日历图+图注（图注与横线无重叠）、编辑部周计划表、练习 A–D 干净。
  缺陷仅 "editors' week"——已修复复核。"What's"（直撇号）渲染正常。
- P6：文章、Note 盒、DIE ZAHLEN、DIE STILLE WOCHE、DIE DEBATTE、民调条
  （44/33/23）、练习 A–D 干净。缺陷仅图表注 "editors' practice"——已修复复核。
- P7：三课（A2/B1/B2）、工具箱（6 条，末条在盒内）、LESERBRIEFE（含 3 行
  披露）、NOCH EIN WORT、阅览室图+图注、Sätze der Woche 8 条、FEHLERKLINIK
  4 组、VOL.5 预告带均干净，无重叠。缺陷仅 "Readers' / Editor's / Learners'"
  三处弯撇号——已修复复核（"Learners'" 以 SVG 文本 U+2019=0 为证）。
- P8：A 完形（113–120 选项 8 枚徽章）/ B Quiz（121–123）/ C 阅读（124–132）/
  D 造句（133–136）/ E 翻译（137–140）/ F 配对（141–144）/ G 对话（145–149
  徽章 5 枚）/ H 写作（MUSTER 84 词）/ ANTWORTEN 8 组答案均完整，图在位，
  答案末端在页脚之上。关键 "133. Die Bundesliga kehrt…" 无粘连（sweep 已验）。

## 剩余工作（8 版未建成）

- es / it / pt / nl / ru / ja / ko / zh-tw：翻译表 tr_<lang>.py 均未写；
  盘点基数 360 unique CJK literals（`cjk_inventory.json`）。每版顺序
  transform → measure → build → 目视 → 150 键 → KIT，一版一版做。
  机制修复（transform.py / build_edition.py / export_text_lang.py / sweep）
  已全部落盘、可复用；新增 keycheck.py / freeze_direct.py（见第 4 棒章节），
  每版主要调校为长字符串缩短（measure 预检 + build.log 溢出定位）。注意：
  tr_<lang>.py 里各语种撇号一律用直撇号 U+0027（单引号字符串内写 `\u0027` 转义），
  并在每版自查中加 U+2019 扫描。
- 预计占地：每版约 40MB × 8，另加构建日志。

## 需要 parent / user 决定

- 无。de-fr 已完成；其余 8 版按既定顺序继续，不需决定。

---

# 第 4 棒记录（2026-11-11，fr 版；本棒进行中）

## de-fr 交付（rebuild 3，2026-11-11 04:38 UTC；上一轮记录，已被重建-A supersede，见报告顶部「重建-A」一节）

- Print PDF: `Die-Lucerna-VOL4-de-fr.pdf` — 10,932,758 bytes,
  sha256 `acfdfb0d914b097d7a6cabb34f19c32068273a52242ec19155b5a697ac3a05f8`
- Web PDF: `Die-Lucerna-VOL4-de-fr-web.pdf` — 1,557,331 bytes (< 7 MB),
  sha256 `2b13edd197ecd80559ef65329e7e4e2aef5bc5051cc8d04dca030235fb8791e4`
- Text: `2026-w47-de-fr.text.md` — 50,116 bytes, 48,235 chars, 591 entries, 150 exercises,
  sha256 `effbd257252256566ba2af9caee79bbeecc54d01f39813e51ac0c617553b2a8b`
  （源稿导出，绝不从 PDF 倒抽）
- ABSTRACT.txt：一行法文，414 字节，无 ASCII 双引号。
- WEEKLY-KIT.md：已写（fr 版完整记录，见版内文件）。
- 门禁（build_edition.py fr，rebuild3.log）：run.py exit 0、零 FLOW OVERFLOW /
  HEAD TOO WIDE；measure 24/24；verify TOTAL 150、编号连续、SVG 字节一致、§1.1
  审计 True、verbatim OK、P8 floor True、17 项禁词全无；occlusion 0 flags；p8
  extract 150/150、compare CLEAN、keydiff [137, 138, 139, 150]（预期内）；
  freeze diff exit 0（新增 CJK 仅 7 个 U+3000）；print/web 文字层多重集一致
  （50,955B / 50,957B）、raw 归一化一致；chips 10/15/18/15/18/18/12/35 = 141，
  P8 A2 22 / B1 13；P8 最小字号 9.94pt ≥ 9.75pt；export exit 0。
- Freeze 直接比对 8/8（`fr/freeze-direct.json`，脚本 `freeze_direct.py`）：
  (a) 源码级 AST 字面量差：0 未入账移除、0 未入账新增（移除 520 / 新增 528，
  逐一由 tr_fr.py、CJK 盘点或已记录的 transform 产物入账）；
  (b) 渲染级冻结交集逐页 P1 147 / P2 163 / P3 195 / P4 166 / P5 173 / P6 175 /
  P7 150 / P8 186，sha256 083e2a2a / 689045ad / 093cf378 / df1bebf7 / 86fa4421 /
  2bbe05f9 / b7aa0771 / 57e118e7——与 de-en 完全一致（冻结内容是共用的德语正文）。
- 150 键复核（`fr/keycheck-150.json`，脚本 `keycheck.py`）：P8 SVG 抽取键 vs 版内源
  REG 逐题比对，**149/150 精确**；唯一非精确项为 Q150（开放写作题，抽取器把 REG 键
  "Exercice libre — suivez les points de l'encadré d'écriture" 截断为 "Exercice libre"，
  预期内，Q150 已在 keydiff 集合中）。REG 分页 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18,
  7:12, 8:38}，级别 A2 69 / B1 67 / B2 14。
- 目视：8 版自 print PDF 100 dpi 渲染逐版目视 + P1 词条行与 P4 Und-Sie 盒放大裁切，
  零问题。U+2019 全扫 8 SVG 总数 0（tr_fr.py 从一开始即用直撇号 U+0027）。
- 核心源未变：content8.py sha256 仍为
  `9b690738c88bdc42f118948aab86fca030d3eb598dd4a52cfe69205d942279b4`
  （与本棒开工时一致）；transform 前已核对。
- 开工探针（本棒 2026-11-11 03:57 UTC）：`git hash-object -w` 通过、
  scratch 真实写文件通过；磁盘 150G 总、101G 已用、49G 空闲。构建解释器
  tools/venv/bin/python（PIL 13.0.0）；freeze 用同一解释器重跑。

## de-fr 三轮构建

- Build 1：de-fr 4 门失败——P1-headline FLOW OVERFLOW（ZAHLEN 盒跳栏）、
  P5-ex 溢出、P8-battery HEAD TOO WIDE（"C LESEVERSTEHEN Compréhension"）、
  occlusion 28 flags。诊断后修 tr_fr.py（fix_tr_fr.py：88 处取值缩短 +
  LAYOUT 工具箱 pad 110→90；P8 keys 注释共削 ~820 字符，114→100 行）。
  失败日志存 fr-build1/；版目录已删重建。
- Build 2：de-fr 3 门失败——occlusion 1 LINEX（P1 词条法文段落 2 行，第 2 行
  "page 5." 墨迹压住 1844 横线）；print/web 默认多重集不一致（3 个 topband
  token：print 侧 "LISENT" 完整、web 侧拆成 "LISE NT"）。根因：本轮 render.py
  写出 69,605,037 字节的 print PDF（335 个字体子集，正常 35 个），并行家庭
  CPU 争用下的瞬时渲染异常；同批 SVG 隔离重渲均为 ~10.9MB / 35 字体。
  topband_test.py（print 管线 vs webpdf 子集字体管线，单页 P1）证明当前
  topband 文案双侧抽取一致，故 topband 文案不动；只修词条段落
  （fix_tr_fr2.py：删 "petites"，394.6px → 1 行）。版目录已删重建。
- Rebuild 3：ALL GATES PASS。print PDF 10,932,758 字节。
- 构建耗时说明：build 2 约 22 分钟、rebuild 3 约 20 分钟，主因多家庭并行
  渲染争 CPU（同期 zh-tw-ja webpdf、ru-it webpdf、nl-it render 在跑），
  非本版问题；render.py 单独跑 16 分钟亦属同一原因。

## de-fr 目视（8 版，rebuild 3 渲染）

- P1：头版、ZAHLEN 盒（3 项收进栏内）、FRAGEN 侧栏（末行 "Les cinq questions
  de la semaine." 收进页内）、IN DIESER AUSGABE、词条 "Calendrier de l'Avent
  (24 portes). Voir page 5." 单行且与横线有空隙、足球图+图注、KURZ & GUT、
  BLITZQUIZ、页脚均干净。放大裁切复核词条行：横线在行下无交叉。
- P2：文章、Note 盒、四侧栏、RECHNEN 表（Note 1 行）、练习 A–D 干净。
- P3：文章、Note 盒、1930 圣诞市场图+图注、WEIHNACHTSWÖRTER、UND SIE?、
  DER TIPP、练习 A–D 干净；图在横线之上。
- P4：文章、Note 盒、头球图+图注、UND SIE? 盒（德 2 行 + 法 2 行收进盒内，
  与结果表无重叠）、9 行结果表、练习 A–D 干净。放大裁切复核 Und-Sie 盒。
- P5：文章、Note 盒、ADVENTSKALENDER/ADVENTSWÖRTER、UND SIE?（2 行提示）、
  1903 日历图（图底 1732.93，横线 1744，11px 空隙）、周计划表、
  桥接 A/C 各 1 行、练习 A–D 干净。
- P6：文章、Note 盒、DIE ZAHLEN、DIE STILLE WOCHE、DIE DEBATTE、民调条
  （44/33/23，标签 football/marchés/calme 不压条形）、ÜBUNGSDATEN 单行收进
  页内、练习 A–D 干净。
- P7：三课（A2/B1/B2）、工具箱（末条 "Es ist fraglich, ob ... = encore ouvert"
  1 行，栏底 1518.0，距 1548 横线 30px）、LESERBRIEFE（含法文披露）、
  NOCH EIN WORT 2 行收进横线以上、阅览室图+图注、Sätze der Woche 8 条、
  FEHLERKLINIK 4 组、VOL.5 预告带均干净，无重叠。
- P8：A 完形 / B Quiz / C 阅读（"C LESEVERSTEHEN Lecture" 标题收进框内）/
  D 造句 / E 翻译（137–140）/ F 配对 / G 对话（徽章 5 枚）/ H 写作
  （MUSTER 84 词）/ ANTWORTEN 8 组答案均完整，图在位，keys 末端 2426
  （距底 2560 余 134px），答案在页脚之上。

## 本棒新增可复用脚本（scratch-fanout-de/，第 3 棒手工做的两项检查）

- `keycheck.py <lang> <edition-dir> <log-dir>`：P8 SVG 抽取键 vs 版内源 REG
  逐题比对，写 keycheck-150.json；Q150 截断（抽取值是 REG 键的前缀）为预期内，
  其余不匹配即失败。在 de-en 上验证：149/150 精确，仅 Q150 截断，exit 0。
- `freeze_direct.py <lang> <edition-dir> <log-dir>`：(a) 源码级 AST 字符串字面量
  多重集差（核心 vs 版），未入账项为 0 才通过（入账规则：tr 模块字面量及其子串、
  CJK 盘点值、transform 注入片段、已记录的核心家具形态）；
  (b) 渲染级冻结交集逐页计数 + sha256（文本不 strip，与第 3 棒口径一致）。
  在 de-en 上验证：源码 PASS + 渲染 8/8，8 页计数与 sha 与第 3 棒参考值逐一
  相同（147/163/195/166/173/175/150/186）。写 freeze-direct.json。
- `topband_test.py`（一次性诊断工具）：单页 P1 的 print 管线 vs webpdf 子集字体
  管线抽取对比，用于定位 print/web 多重集差异是否来自 topband 文案本身。
  结论：fr 当前 topband 文案双侧一致，差异来自异常的 print PDF。
- `keys_measure.py`：按页组度量 P8 keys 流的行数（fr 重建后 100 行，en 为 105 行）。
- `fix_tr_fr.py` / `fix_tr_fr2.py`：两轮 tr_fr.py 修复脚本（断言式旧→新替换）。

## 下一步（本棒继续）

- es：写 tr_es.py（278 键，与 tr_en.py 集合一致；先拿 core svglib 预检
  masthead/topband/chart/phrases，再 transform → measure → build → 目视 →
  150 键 → KIT）。同类缺陷盯防：ZAHLEN 盒跳栏、桥接行数、Und-Sie 提示行数、
  ÜBUNGSDATEN 宽度、P7 栏高、P8 keys 长度；撇号一律直撇号并扫 U+2019。

---

# 完成记录（更正：尾部过期章节，2026-11-11 07:35 UTC 核实）

本章原写于 2026-11-11 ~01:00 UTC：第 3 棒开工时磁盘配额耗尽（Errno 122），
build 在写 build.log 时失败，当时无一版建成。配额释放后重建恢复：第 3 棒
建成 de-en（rebuild 2，02:53 UTC），第 4 棒建成 de-fr（rebuild 3，04:38 UTC），
第 5 棒建成其余 8 版。原章标题与“剩余工作”节均已过期，以下为终版 10/10 记录
（逐版一行：状态、双 PDF 字节+SHA、门禁结果；SHA/字节取自各版 WEEKLY-KIT.md，
已与落盘文件逐一核对一致）。

- **de-en 完成（rebuild 2，2026-11-11 02:53 UTC）**：ALL GATES PASS。印版 10,966,416 B，sha256 `a997c6cefe8467bdd37a71158e0f61ceff16d653039f50159b1608305b3a4b87`；网版 1,555,614 B（< 7 MB），sha256 `62623cb5996644004ba48a6ed7246cdd0584bec3a2549123174db318384a3a90`。150 键 149/150（Q150 PREFIX，预期内）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 8/8。
- **de-fr 完成（rebuild 3，2026-11-11 04:38 UTC）**：ALL GATES PASS。印版 10,932,758 B，sha256 `acfdfb0d914b097d7a6cabb34f19c32068273a52242ec19155b5a697ac3a05f8`；网版 1,557,331 B（< 7 MB），sha256 `2b13edd197ecd80559ef65329e7e4e2aef5bc5051cc8d04dca030235fb8791e4`。150 键 149/150（Q150 PREFIX）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 8/8。
- **de-es 完成（rebuild 3，2026-11-11 06:14 UTC）**：ALL GATES PASS。印版 10,968,797 B，sha256 `2c535a10f81516a749c56fa43290bc54c5bd268ba36469caa10367bc944395ed`；网版 1,558,812 B（< 7 MB），sha256 `b20ceebfeba6c5e7ad2be9d2123b8406755bceff0174f34c6ca4158e03716228`。150 键 149/150（Q150 PREFIX）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 8/8。
- **de-it 完成（rebuild 2，2026-11-11 06:29 UTC）**：ALL GATES PASS。印版 10,965,089 B，sha256 `8c9c1d4fb3ce889530ef1e424a9eba9d7a4c5e758667607852ea8ac4b1e8482c`；网版 1,553,866 B（< 7 MB），sha256 `9c01c2f3123ed38f332882c68c1fc0c8a9e876cd2bf8b6d2fbf50c063bc1d571`。150 键 149/150（Q150 PREFIX）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 8/8。
- **de-pt 完成（rebuild 2，2026-11-11 06:40 UTC）**：ALL GATES PASS。印版 10,968,902 B，sha256 `d946e0184638857c6e7800faa54570815245496e0c48316af75bd4d4582c0c5a`；网版 1,559,382 B（< 7 MB），sha256 `a86ce50df519bee26a5fa4858ac17079306b9f15929fc5e88f5c6c1a7d1c081d`。150 键 149/150（Q150 PREFIX）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 8/8。
- **de-nl 完成（build 1，2026-11-11 06:46 UTC）**：一次通过，ALL GATES PASS。印版 10,964,692 B，sha256 `bb54120a55d5de272c17061f84a363ac14f1820b2353e1490e9dcb75d8444e53`；网版 1,553,848 B（< 7 MB），sha256 `74a0ecddea5427ea4d724760cc1e46733745b188683d3184dac771e12c65a9bb`。150 键 149/150（Q150 PREFIX）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 8/8。
- **de-ru 完成（rebuild 2，2026-11-11 06:57 UTC）**：ALL GATES PASS。印版 10,954,755 B，sha256 `74fac6aa22cf181614ff3fb40f267547f54859bcd072bc3dc17f78cc0ca9144e`；网版 1,605,334 B（< 7 MB），sha256 `8f9b83e799ed2afafb96e94e862e434f487803203143f7cc7f1fafd3b1a664cf`。150 键 149/150（Q150 PREFIX）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 8/8。
- **de-ja 完成（rebuild 3，2026-11-11 07:15 UTC）**：ALL GATES PASS。印版 23,901,730 B，sha256 `19d5a14a2966e6865a8bfb28bd74fd0c05b10594a37670fe7db4d84596e5605a`；网版 2,113,005 B（< 7 MB），sha256 `8dc87c2363a02cb2b098f55614e3866b31f5796c91ea6e8d3d393fbfbb66236d`。150 键 149/150（Q150 PREFIX）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 渲染 8/8（源层仅 JP 字体切换 4 串）；新增 CJK 2,994（日语层），残留审计 0。
- **de-ko 完成（rebuild 2，2026-11-11 07:23 UTC）**：ALL GATES PASS。印版 15,906,995 B，sha256 `2232d232f6b156e4c0242e5883a4f31821ded5faaa72dbcdc15a43bacc48aec1`；网版 1,867,491 B（< 7 MB），sha256 `3070faf0c58e07ef056b7deed582036f09143d031417457da84ba84655b7563d`。150 键 148/150（Q150 PREFIX + Q139 空格拼接，皆为抽取器 join 伪影，SVG 已核实渲染正确）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 源层 PASS（0 未计入）+ 渲染 8/8；新增 CJK 3,096（韩语层），残留审计 0。
- **de-zh-tw 完成（build 1，2026-11-11 07:28 UTC）**：一次通过，ALL GATES PASS。印版 23,048,415 B，sha256 `71693e9c011ffc4b589a3fdaba8d339cad7e9f3ebaac35ea33ea34e1d2fa8537`；网版 2,301,044 B（< 7 MB），sha256 `11f58493f60fe6dce06b8f3c47095e7b5fbec5a2cb300a8d4a9074b478189cc1`。150 键 149/150（Q150 PREFIX）；芯片 141；P8 最小字号 9.94pt；U+2019 全扫 0；freeze_direct 渲染 8/8（源层仅 TC 字体切换 3 串 + 核心改动句 1）；新增 CJK 1,328（繁體層），残留审计 0。

## 核实说明（2026-11-11 07:35 UTC）

- 交付物逐版核实：10 版各 8 SVG + 双 PDF + .text.md + ABSTRACT.txt + WEEKLY-KIT.md + EDITION-RECORD.md 齐全；各版 scratch 门禁日志（build.log、rebuild<N>.log、measure<N>.log、keycheck-150.json、freeze-direct.json、occlusion/p8/verify/export 日志）齐全，无缺失，无需补记。
- Q34 题干状态：10 版 content34.py 均带旧题干 `Am Montag öffnen in Köln die ersten ___.`（每版 1 处，已逐版 grep 核实）。核心 `core-de/content34.py` L105 现已是修后句 `Am Montag öffnet in Köln der erste ___.`（已 grep 核实）；核心重建进行中，核心重定稿后协调员另派 10 版重建波次。本次核实未重建任何版。
