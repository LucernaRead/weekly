# FANOUT-REPORT-zh-tw — W47 繁體中文家庭 fan-out（9 版：de fr es it pt nl ru ja ko）

**Builder：** 第 7 棒（2026-11-11 接棒）。上一棒 4d120f93（01-BLOCKED）与第一棒（00-BLOCKED）均因 Disk quota exceeded 停手；第三棒（02-BLOCKED）transform.py de 成功、run.py 在 content56.py 阶段 exit 120 后停手。
**进度：9/9 完成（de、fr、es、it、pt、nl、ru、ja、ko 全部完成，全量自查零问题）。**
**核心版 SHA（开工核对，与任务一致）：** print `f2764750d3872fc07adc034ef3c1e80cad60d543067f6a96a710b16bd8f89fba`、web `9191ef790de862fd1defc7e51ea661e8de71b1438e1d55068a393eb211dc54a2`、text `4a99110975bb0c4b684de82a8a9ed7fa11bddb59562bb75398327cb4446207a5`。
**写探针（第 7 棒，2026-11-11 ~01:30 UTC）：** git hash-object -w（rc=0）+ 真实文件写 probe-write-7a.txt（rc=0），均通过。df：/home/hatch 150G 总，97G 已用，53G 可用。内存 available ~1.7G。动手。
**工具：** scratch-fanout-zh-tw/tables.py（238 条 × 9 语）与 transform.py（前两棒已就绪，直接续跑）。顺序：de → fr → es → it → pt → nl → ru → ja → ko，一版一版做，每版自查零问题才算完成。

## de — 2026-w47-zh-tw-de

**完成（第 7 棒，2026-11-11 ~02:10 UTC），全量自查零问题。** 详见 [de.md](de.md)。
- 印刷 PDF `Lucerna-VOL4-DE.pdf` 21,717,574 字节，SHA-256 `28af6ac44b607d5a2e7518e45a422ae23859fe10bc0142ba6c81f0dc9edaa77c`；网页 PDF 2,436,311 字节，SHA-256 `18f1ed9d6f978b5c5e29eb080498dbc9c4b5120e2c4e899fc1e288c2894619f8`；text.md 51,842 字节。
- 门禁：run exit 0（0 FLOW OVERFLOW；1 HEAD TOO WIDE 已裁定）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；P8 徽章 38/38。
- 修过两处：(1) P7 第 3 栏德语过长压页脚（occlusion 2 flags → 缩短披露/诊所注/句式例 + 预告条 118→104px，终点 2589.8，occlusion 0）；(2) 6 条 P8 答案注记英文残留（tables.py 缺 5 条源串所致，见共享缺口）。
- 共享缺口（其余 8 语都会遇到）：tables.py 缺 `Xiaoxue is Nov 22.` / `The ceremony is at the Taipei Music Center.` / `Four big events fall on the same Sunday.` / `Collecting points is 集點.` 5 条源串，各版须在自家 content56.py/content8.py 译成本语；P7 第 3 栏长讲解语普遍会超，须实测 col3 终点；每版 transform 后须删 copytree 带入的核心旧件 3 个（本版已删）。

## fr — 2026-w47-zh-tw-fr

**完成（第 7 棒，2026-11-11 ~02:30 UTC），全量自查零问题。** 详见 [fr.md](fr.md)。
- 印刷 PDF `Lucerna-VOL4-FR.pdf` 20,191,919 字节，SHA-256 `beeebce2531fcadd076f3999d8965ee425df76efe47c1e8f1584365fe74930b3`；网页 PDF 2,350,191 字节，SHA-256 `61537f8dde6b5c04b63adebdd5835275d41108588c426688a0bf1cc4c1ce04df`；text.md 52,507 字节。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；泄漏扫描 0；P8 徽章 38/38。
- 修过三处：(1) 6 条 P8 答案注记预补译（tables.py 同一缺口）；(2) P6 栏头超宽 2 处（446.3/467.1px → "Lire la frise" / "Quiz de lecture"）；(3) P7 第 3 栏溢出（col3 1908.7→1823.3，预告条 2662.7→2577.3）。
- 非缺陷：P4 "Mots du baseball" 栏头折两行（栏内，无溢出）。

## es — 2026-w47-zh-tw-es

**完成（第 7 棒，2026-11-11 ~02:45 UTC），全量自查零问题。** 详见 [es.md](es.md)。
- 印刷 PDF `Lucerna-VOL4-ES.pdf` 23,256,393 字节，SHA-256 `5f77b922a5f954fbe84b59ea6a1bcce7a21f663dd27d69e4067f34d655dea9cf`；网页 PDF 2,513,310 字节，SHA-256 `c625ae1d85f220af088c6f3c95189b31442cbb970079067e5f3364310060b7b8`；text.md SHA-256 `4e7bd1ae9b864a43b65b3edb882b82de9be9535e3d930035176fce902c47aa08`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；泄漏扫描 0；P8 徽章 38/38。
- 修过两处：(1) 6 条 P8 答案注记预补译（tables.py 同一缺口）；(2) P7 第 3 栏溢出（col3 1908.7→1823.3，预告条 2662.7→2577.3）。
- 非缺陷：P4 "Palabras de béisbol" 栏头折两行（栏内，无溢出）。

## it — 2026-w47-zh-tw-it

**完成（第 7 棒，2026-11-11 ~02:55 UTC），全量自查零问题。** 详见 [it.md](it.md)。
- 印刷 PDF `Lucerna-VOL4-IT.pdf` 19,420,291 字节，SHA-256 `ec9d0624d91abb2ae8875f5f51cb2064d7927d4f1a4a8e4f2454b1fb11894bce`；网页 PDF 2,306,683 字节，SHA-256 `34c4ff2c9e3f1fe0e3714c773b5ead11306e542c4a60e52b2c815684ba986988`；text.md SHA-256 `5e0ada652cf39269b96cac9c25f675deab93ab239f00ee8d2ea891a657ded507`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；泄漏扫描 0；P8 徽章 38/38。
- 修过三处：(1) 6 条 P8 答案注记预补译（tables.py 同一缺口）；(2) P6 栏头超宽 1 处（466.9px → "Quiz di lettura"）；(3) P7 第 3 栏溢出（col3 1908.7→1823.3，预告条 2662.7→2577.3）。
- 非缺陷：P4 "Parole del baseball" 栏头折两行（栏内，无溢出）。

## pt — 2026-w47-zh-tw-pt

**完成（第 7 棒，2026-11-11 ~03:10 UTC），全量自查零问题。** 详见 [pt.md](pt.md)。
- 印刷 PDF `Lucerna-VOL4-PT.pdf` 20,944,927 字节，SHA-256 `3673d36cb0890418be4e1699fdda2e0df0525516227a7cd0dc8b35bf414e8d47`；网页 PDF 2,396,718 字节，SHA-256 `da2dd497b7fca416acba2751f4e7c4cc6321418d71efc7fe1f4ffa16c345db14`；text.md SHA-256 `1f1738742785e806b65e63afb44fc92854e04fc79de12ba11676c42404857f37`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；泄漏扫描 0；P8 徽章 38/38。
- 修过三处：(1) 6 条 P8 答案注记预补译（tables.py 同一缺口）；(2) P6 栏头超宽 1 处（469.6px → "Quiz de leitura"）；(3) P7 第 3 栏溢出（col3 1908.7→1823.3，预告条 2662.7→2577.3）。
- 非缺陷：P4 "Palavras do beisebol" 栏头折两行（栏内，无溢出）。

## nl — 2026-w47-zh-tw-nl

**完成（第 7 棒，2026-11-11 ~03:30 UTC），全量自查零问题。** 详见 [nl.md](nl.md)。
- 印刷 PDF `Lucerna-VOL4-NL.pdf` 20,939,118 字节，SHA-256 `254751618af573d563bf11632fb2487ee01e1b2ea15b54c609a08fb129e34e32`；网页 PDF 2,393,503 字节，SHA-256 `3c308d062aeda055039936558b1a608eee30229092e79a56fe3b2f153dbf081d`；text.md SHA-256 `dcfc16818510b3229b1611607de403ea93219f75f3c24a4a0fa6dfd681410051`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；泄漏扫描 0；P8 徽章 38/38。
- 修过三处：(1) 6 条 P8 答案注记预补译（tables.py 同一缺口）；(2) P7 第 3 栏溢出——荷兰语第 3 条诊所注已是 2 行，省行改从披露 8→7、诊所第 2 条注 2→1、句式例 5→4（col3 1908.7→1823.3，预告条 2662.7→2577.3）；(3) text.md H1 按 W46 nl 前例更正为 "Teksten in het Chinees (traditioneel)"。
- 非缺陷：P4 "Honkbalwoorden" 栏头折两行（栏内，无溢出）；freeze 首跑 exit 127 仅是工作目录错误，重跑 8/8。

## ru — 2026-w47-zh-tw-ru

**完成（第 7 棒，2026-11-11 ~03:55 UTC），全量自查零问题。** 详见 [ru.md](ru.md)。
- 印刷 PDF `Lucerna-VOL4-RU.pdf` 12,896,270 字节，SHA-256 `e1f3c46a9e22a3b03c9b8a6c9fc450b86bb254ccbec223169b682c2447c2ff76`；网页 PDF 1,993,092 字节，SHA-256 `385e4b265347bb5d87442934b60f9b2c1bac88b48bfc20ca98033bc54d6a0719`；text.md SHA-256 `41da5432e31c1f9819a6508d8fc91933a64ac6cd8b0a0794e32f0d10e0319f09`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags（首审 1× P8 TEXTX 已修）；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；泄漏扫描 0；P8 徽章 38/38。
- 修过五处：(1) 6 条 P8 答案注记预补译（tables.py 同一缺口）；(2) 4 处栏头超宽（P4/P6/P8-D）；(3) P7 第 3 栏溢出为全家最重（col3 1968.0→1823.3，预告条 2722.0→2577.3；披露 10→7 行）；(4) P8 答案区标题与右侧注记重叠（1171px→830px），终版为 build 3；(5) 删核心旧件 3 个。
- 事故：首贴补脚本文件名写错（content4.py 应为 content34.py）致短暂表/版不一致，已重贴验证；首次 render 被运行时中断、第二次分发超时，第三次前台 rc=0，无 exit 120。
- 非缺陷：P3 金马小档栏头贴右框边（框内）；P4 "Слова бейсбола" 栏头折两行（栏内）；印刷 PDF 12.9MB 小于他版——卡片相同、文字层完整，仅图片嵌入差异。

## ja — 2026-w47-zh-tw-ja

**完成（第 7 棒，2026-11-11 ~04:10 UTC），全量自查零问题。** 详见 [ja.md](ja.md)。
- 印刷 PDF `Lucerna-VOL4-JA.pdf` 18,090,244 字节，SHA-256 `35fb9b00d5e9c33f4d1ef9fdcecaff5f83b3139e264b39182a420f2fb90b3d95`；网页 PDF 2,548,035 字节，SHA-256 `5c3be54673d3e1d65b14df730b48a1de908ca30d6a354ea651cd1811dc9f912f`；text.md SHA-256 `47162db4c1020a498e429df6336dbc3f7d83137a0ecfbb8d0ac0832f31b08918`。
- 门禁：run exit 0（首轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；泄漏扫描 0；P8 徽章 38/38。
- 九版中唯一首轮零修改的版（日语讲解紧凑，P7 终点 1827.28/2581.28，无需修正）；6 条 P8 答案注记预补译（tables.py 同一缺口）；删核心旧件 3 个。
- checks.py 报 SIMP_ONLY_HITS ['国','学']——已逐处核实为日语汉字误报（中国語 / 国際 / 学べる 三处日语讲解串，繁体正文内无此二字），非缺陷；短语与图表检查均通过。

## ko — 2026-w47-zh-tw-ko

**完成（第 7 棒，2026-11-11 ~04:25 UTC），全量自查零问题。** 详见 [ko.md](ko.md)。
- 印刷 PDF `Lucerna-VOL4-KO.pdf` 16,839,317 字节，SHA-256 `e1e1b6a2056728809b5e9ccbdbb9988c0205396dac94f46eb2523d3a8ed7cd56`；网页 PDF 2,310,716 字节，SHA-256 `3150f83e128f75b6614ef3149c645e596de867dd92f4454feaeeaf888124175f`；text.md SHA-256 `f5b1943de93a838bcd5fcfdd16cce0cafbcdc89eff5e6176604ae6061e81ea99`。
- 门禁：run exit 0（首轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；泄漏扫描 0；P8 徽章 38/38。
- 与 ja 同为首轮零修改的版（韩语讲解紧凑，P7 终点 1821.42/2575.42）；6 条 P8 答案注记预补译（tables.py 同一缺口）；删核心旧件 3 个。
- 非缺陷：P4 "야구 단어" 栏头单行；P5 跨栏续排；P8 题干 10.35pt；text.md 页标题英文为导出器固定格式。

## 9/9 完成（第 7 棒最终状态，2026-11-11 ~04:25 UTC）

de、fr、es、it、pt、nl、ru、ja、ko 全部完成，全量自查零问题。每版一份记录（de.md / fr.md / es.md / it.md / pt.md / nl.md / ru.md / ja.md / ko.md）+ 各版 WEEKLY-KIT.md + 门禁日志均在 scratch-fanout-zh-tw/。未跑 insert.py / lint --write / git push / git add / reset / stash，未提交；core-zh-tw/ 与 W43/W45/W46、其他目标语、core-zh-cn 未动。待协调员另派独立复校员逐版复校。
