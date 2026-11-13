# W47 pt 家庭独立重校 — PROOF-NOTE

- **校对员**：独立校对员（未参与建造这 11 版）。只校对、不修复、不重建、不 commit、不 push、不跑 lint。
- **校对日期**：2026-11-12
- **范围**：11 版，目标语 pt，读者母语 en / de / fr / es / it / ja / ko / nl / ru / zh-cn / zh-tw。版目录：`production/2026-w47/2026-w47-pt-<母语>/`（10 个 fan-out）+ `core-pt/`（即 pt-zh-cn 版；盘上无单独的 `2026-w47-pt-zh-cn` 目录，无需去重）。开工枚举：10 fan-out + core-pt = 11 版，与任务一致，无多无少。
- **结论：(b) 有问题** —— 共 3 条，均为低严重度（见 §2）。其余逐项检查全部通过（见 §3）。

## §1 校对的文件（尺寸 + SHA-256 前 12 位，即本次校对的那份文件）

| 版 | 印 PDF `A-Lucerna-VOL4.pdf` 字节 / SHA12 | 网 PDF `A-Lucerna-VOL4-web.pdf` 字节 / SHA12 | text.md 字节 / SHA12 |
|---|---|---|---|
| pt-en | 12421287 / 91fa99c4ed0b | 1058717 / b100c5765c5f | 37333 / 513326ffa497 |
| pt-de | 12426508 / a8c54d0c9b42 | 1063964 / d76c126f2788 | 37907 / 519ab0dedbae |
| pt-fr | 12422440 / 90f78551a5eb | 1059873 / 83f63d47ace7 | 37699 / 39d06879d21b |
| pt-es | 12421396 / 9e80ddac1389 | 1058824 / 4f918ab38188 | 37467 / 96d6f11a5616 |
| pt-it | 12418794 / 56f388e7ce3a | 1056196 / ab8305b734dc | 37419 / 37c1980caacc |
| pt-ja | 15449291 / 9208d231d66c | 1433879 / a9b4a30929c1 | 37915 / 90dcdcca7821 |
| pt-ko | 14231397 / f3104fecd528 | 1307288 / 797ad196553e | 37804 / 3eb35dfb9070 |
| pt-nl | 12422999 / 7fbf77a5d9da | 1060452 / 0fc3730b1fb5 | 37559 / 6f8d4d596032 |
| pt-ru | 12694224 / 6208be63e917 | 1311813 / c3b7eae275d7 | 39736 / 87871659c010 |
| pt-zh-tw | 13804538 / 2bbf46445f9e | 1463493 / 2d0e80af74d7 | 36875 / 5cd5c7270e6a |
| pt-zh-cn（core-pt） | 14137984 / edcb8d3d6920 | 1389823 / ca9f7722ecb2 | 36882 / 3cd3793f198a |

收尾时复核：上述 33 个文件的尺寸与 SHA 与开工记录完全一致，校对期间未被改动。11 版印 PDF 均为 8 页（pdfinfo）。

## §2 发现的问题（3 条，均为低严重度）

### 2.1 P7 B2 讲解句主谓不一致 —— pt-en / pt-fr / pt-es / pt-nl（低）

- **位置**：P7 第三栏「B2 O FUTURO DO SUBJUNTIVO」讲解段第二句；text.md 与印 PDF P7 均可验证（印 PDF 已逐页目检确认）。
- **证据**（text.md 原文，grep 实测）：
  - pt-en：`quando, se, quem takes the future subjunctive: sair, for, tiver (the grammar of waiting for the official key)` —— 主语 quando/se/quem 三项并列，动词应为复数 **take**。
  - pt-fr：`quando, se, quem prend le futur du subjonctif : sair, for, tiver …` —— 应为 **prennent**。
  - pt-es：`quando, se, quem lleva el futuro de subjuntivo: sair, for, tiver …` —— 应为 **llevan**。
  - pt-nl：`quando, se, quem krijgt de toekomende tijd van de aanvoegende wijs: sair, for, tiver …` —— 应为 **krijgen**。
- **不记问题的同模板三版**：pt-de（`… steht danach im Futur des Subjunktivs`）、pt-it（`… vuole il futuro del congiuntivo`）、pt-ru（`… требует будущего времени сослагательного наклонения`）——单数动词在这些语言中可理解为将枚举视作一个整体，语法可辩；ja/ko/zh-cn/zh-tw 的表述方式不同，无一致问题。
- **严重度**：低。讲解层单句语法错误，不影响题意与答案。

### 2.2 ABSTRACT.txt 缺刊名 —— pt-it / pt-ja / pt-ko / pt-nl / pt-ru（低）

- **位置**：各版 `ABSTRACT.txt` 全文。
- **证据**：grep `lucerna`（不区分大小写）计数：pt-en/de/fr/es/zh-cn/zh-tw 各含 1 次（均以 "A Lucerna … VOL.4" 开头）；pt-it、pt-ja、pt-ko、pt-nl、pt-ru 均为 **0 次**，直接以话题开头。SOP §9 要求摘要包含刊名、目标语名、A2–B2 分级与题数——目标语、A2–B2、150 题在五版中齐全，仅缺刊名。
- **严重度**：低。SEO 完整性缺口，不影响正文。

### 2.3 P2「D AS PALAVRAS」小节标题与其内容分离 —— 全部 11 版，系统性（低）

- **位置**：P2 练习区底部。
- **证据**（印 PDF P2 逐版目检）：「D AS PALAVRAS」绿色小节标题落在中间栏（C 栏）最底部、24 题之后，而其内容（25–28 配对题及选项 a–d）在右侧栏、标头为「A2 25.-28.」+ 各版配对说明。11 版版式完全一致，属模板分栏行为，非单版缺陷；内容无缺失、无溢出，读者可凭题号对应。
- **严重度**：低。版式观感问题，建议模板层面处理，不必逐版修。

## §3 已验证无问题（逐项）

### 内容与事实（core text.md 全文通读 + 10 版 fan-out 全量 diff vs core）

- core-pt text.md 全文通读：150 题、8 页。日期/星期逐项核验无误（11 月 20 日周五假期；11 月 15 日周日 Enem 第二天；11 月 7 日周六 / 11 月 8 日周日半决赛；11 月 1 日周日首回合；11 月 16–30 日 = 15 天 = 10 工作日 + 5 周末/假日，10+5=15；Q83–86 一致）。事实核验无误（Zumbi 卒于 1695 年 11 月 20 日；Lei 12.519/2011 设纪念日；Lei 14.759/2023 定为全国假日；Enem 第二天 13h30–18h30、90 题、5 小时；杯赛决赛 12 月 6 日 Mané Garrincha；Grêmio 总比分 3–1、Palmeiras 点球 5–4；P4 赛程表；F1 圣保罗站 11 月 8 日 Norris/Verstappen/Hadjar；Black Friday 11 月 27 日周五）。全部题键与题干/原文/图表交叉核对无误（P1 1–10、P2 11–28、P3 29–46、P4 47–64、P5 65–82、P6 83–100、P7 101–112、P8 113–150）；动词变位正确；P2（25–28）、P4（52–55）、P8 F（141–144）配对正确；「Frases da semana」8 句与正文逐字一致；P7 读者来信说明披露 VOL.3 承诺未兑现、顺延至 VOL.5；Q125「rodada 36 … sábado 21」与 P1（第 35 轮 18–19 日周三/周四结束）一致。
- 10 版 fan-out text.md 与 core 全量 diff（`toolout/textmd-diff-vs-core.txt`，1656 行，逐行读完）：葡语核心层逐字节相同；仅讲解层行有差异，全部为正确读者母语，无跨语言残留。E 节翻译 137–140 十版均准确。zh-tw 为规范繁体（連假/週五/十二碼/價籤/獎盃），无简体残留。
- 模型文：core text.md 实测 **88 词**，与 P8「88 字/88 words」标注一致。

### 机械检查

- `tools/p8.py compare --total 150`（core P8 SVG vs 各 fan-out P8 SVG）：10 版全部 **CLEAN**，150/150，keydiff 仅 [137, 138]。137/138 已逐项核查：core 键为中文，fan-out 键为读者语翻译（例 en "Friday 20 November is a national holiday." / "Palmeiras won 5–4 in the shoot-out."；ru 俄语；zh-tw 繁体）——属合法的翻译重定向，仅作信息记录。
- `tools/occlusion_audit.py`（11 版 `svg/` 目录）：**0 标记**，每版均如此。
- P8 印出答案 vs text.md「Respostas」逐题比对（`toolout/p8-vs-textmd.txt`）：每版 150/150。残余表面差异为比对脚本切分伪影（值内含 "N." 如 #134 "1 a 1."、德语日期 "20. November" 如 pt-de #137/#138、#1/#150 边界处理），已逐项 grep 核实，无真实不符。
- 文本层：每版网 PDF 的 `pdftotext` 字节数与印 PDF 逐版相等（zh-cn 44343；en 45958；de 47966；fr 47430；es 47060；it 46710；ja 47917；ko 47284；nl 47100；ru 54970；zh-tw 44534）——文本层完整且一致。
- 弯引号普查（D5）：每版 curly_total 4–6，**全部在 Newsreader 内，0 在 Noto Sans CJK**——core-pt 6、pt-fr 5、pt-it 5，其余 8 版各 4。符合任务 PASS 标准。core-pt P7 两处已知 fix2 点在 Newsreader 内（20.5pt）。
- 摘要（除 §2.2 外）：11 版摘要均为正确读者语，事实与正文一致。
- 刊头/页脚（pdftotext P1+P8 逐版核对）：P1 均有 VOL.4 + "QUARTA EDIÇÃO"；P8 页脚均为读者语（"Page 8 of 8" / "Seite 8 von 8" / "Page 8 sur 8" / "Página 8 de 8" / "Pagina 8 di 8" / "8ページ（全8ページ）" / "제8면/총8면" / "Pagina 8 van 8" / "Страница 8 из 8" / "第8版／共8版" ×2）。提取中字母间距拆分（如 "TODA SEM ANA EM PORTUGUÊS"）为 pdftotext 伪影，非印刷缺陷。

### 逐页目检（印 PDF 8 页 × 11 版 = 88 页，72 dpi 渲染图全部看过）

- **无溢出、无重叠、无压页脚、无豆腐块、无截断句**。粗体盒标题在 Newsreader 下无顶出盒；P8 答案流单页容纳完整（113–150 全部可见，含 Mané Garrincha 球场图及图注）。
- **pt-ko P2 已知项已核**：电池头「SEX 20 / SÁB 21 / DOM 22 / SEG 23」（25→22pt 修后）无溢出，韩语说明文字完整在框内。
- 逐页要点：P1 刊头、配对徽章、头条条、数字盒、练习 1–10、图片+图注、页脚均完整；P2 生活版+电池日程+练习 11–28；P3 Zumbi/Parreiras 画作+图注+练习 29–46；P4 体育版+「A SEMANA DO FUTEBOL」赛程表+练习 47–64；P5 Enem 等待+图书馆照片+练习 65–82；P6 深读+「O FIM DE NOVEMBRO EM NÚMEROS」条形图（工作日 10 天 / 周末假日 5 天）+练习 83–100；P7 语言版+《Os Lusíadas》1572 首版图+「FRASES DA SEMANA」8 句+「A PRÓXIMA SEMANA (VOL.5)」；P8 测试 113–150 + 全部答案 + 88 词模型文。
-  minor 观察（非缺陷）：zh-cn P1「A SEMANA EM NÚMEROS」2023 行末全角「（」换行，属正常换行；ja/ko P1 同类括号跨行亦同。

## §4 方法与工具状态

- 依据：`SOP.md` §8（校对循环）+ §1.1（字体表）；`scratch-d5-plan/D5-PLAN.md` §1（D5 缺陷类）。
- 工具：`~/workspace/weekly-git/tools/venv/bin/python` 跑仓内工具；`pdftoppm`/`pdftotext`/`pdfinfo` 辅助。未跑 lint，未动任何文件。
- **tools/ HEAD 变化与重跑**：开工时仓库 HEAD 为 `71f4e6f9df302d5322211cdd01437a9ac0f4fec7`；收尾时为 `b9ac29a6f3c640f408965572823e5a1ccebfd1e5`（其间新增 commit `b9ac29a6 tools: D5 gates + p8/occlusion/cover/run_build fixes (W47 review round)` 与 `eb6be533 W47 covers`）。`tools/p8.py` 与 `tools/occlusion_audit.py` 在此期间有改动（p8 解析补 CJK 破折号空格恢复；occlusion 字体度量改 bare family 名一律走非 CJK 面）。按任务要求，收尾用新版工具重跑两项受影响检查：**p8 compare 10 版仍全 CLEAN（150/150，keydiff 仅 [137, 138]）；occlusion 11 版仍 0 标记**——与旧版工具结果一致。另：工作树中有他人未提交的 de 家庭改动（`2026-w47-de-en/`），与本任务无关，未触碰。
- 磁盘：收尾时 `/home/hatch` 93G/150G（63%），未触 ≥100G 门限。`/tmp/pt-proof/` 下 88 张渲染图为可复现中间件，校对后已清理（见下）。
- 机械检查日志：`toolout/` 下 `p8-compare150.log`、`p8-compare-rerun.log`、`occlusion.log`、`occlusion-rerun.log`、`p8-vs-textmd.txt`、`textmd-diff-vs-core.txt`、`mech-checks.txt`、`curly-census.txt`、`abstract-textlayer.txt`、`masthead-footer.txt`。
- 清理：`/tmp/pt-proof/png/` 与 `/tmp/pt-proof/small/`（88+88 张渲染图）已删除；均为可复现的渲染中间件，非交付物。
