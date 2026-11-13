# PROOF-NOTE — 2026-W47 ja-it, 第一轮独立复校（叶子）

- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-it/`（未入仓本地件）
- 校对员：叶子（第一轮独立复校，与 builder / 核心 builder / 其他轮复校员不同人）
- 日期：2026-11-11（UTC 05:30–06:05 左右）
- 依据：SOP.md §8、§1.1；`AGENTS.md`；`WEEKLY-KIT.md`（本版）；`core-ja` 只读对照。
- 方法：全文逐字精读（`2026-w47-ja-it.text.md` 1378 行全读）＋ 8 版印刷 PDF 逐版目视
  （由印刷 PDF 重新渲染，不用 builder 的卡片图）＋ 网页 P1/P8 目视 ＋ 150 题逐题验算
  ＋ 全部机械门自跑（见 GATE-LOG.md）。

## 结论：(a) 零问题，可定稿

本版未发现缺陷。以下为已核实事实；观察项单列，不计缺陷。

## 身份复核（自算）

- 印刷 PDF `Lucerna-VOL4-JA-IT.pdf`：29,099,162 字节，8 页，1462.5×2025 pt，
  SHA-256 `75986cd7e7b0acc6e3d4887ccb023c577f3612c9a242c3093060cb7f2af200fd` —— 与 KIT 一致。
- 网页 PDF `Lucerna-VOL4-JA-IT-web.pdf`：4,476,984 字节，8 页，
  SHA-256 `b3ea6d183dea6a1c5b64f5ff1a42807462a0f259fc37fea3668f7a239fc353f0` —— 与 KIT 一致。

## 全量复校结果

- 150 题：编号 1–150 连续无缺重；分版 10/18/18/18/18/18/12/38；级别 A2 48 / B1 73 / B2 29；
  题型 completamento 50 / scelta multipla 51 / abbinamento 12（3 组×4）/ costruzione di frasi 8 /
  vero o falso 11 / cloze 13 / traduzione 4 / Scrittura 1；范文 154 字（自数 154，含句号）。
  150 条答案逐题对照题面与正文验算，全部正确；图表合计 38+24+22+16=100、38−24=14、38+24=62 均对。
- 金句 8 条：逐字与正文一致，且与核心版正文逐字节相同（8/8 在核心文本中原样出现）。
- 日期/星期全验：11月16日（月）～22日（日）、19日（木）、22日（日）、23日（月）、5日（木）、
  7日（土）、8日（日）、12月1日（火）等全部与 2026 年日历相符；P8 阅读短文木→金→日→月
  与 19→20→22→23 日一致。
- VOL：VOL.4 为期号（页脚每页 1 次；P1 另有「VOL.4　第4号」与刊名行 VOL.4）；
  VOL.3 出现 1 次（P4 前号注）；VOL.5 实际出现 4 次（见观察项 O4），无误印。
- 徽章：每题级别徽章与登记一致；颜色 A2 #5c6e30 / B1 #46581f / B2 #37402f；
  P1  contents 栏级别标注（2面 A2、3面 A2→B1、4面 B1、5面 B1、6面 B2、7面 A2→B2、8面 Tutti i livelli）与各版一致。
- P8：最小字号 9.98pt（≥9.75pt）；题干 10.35pt 未动（79 个 10.35pt 跨度，均为日语题干）；
  答案流在页脚之上收束（末行 150 在约 2/3 处），无压页脚。
- §1.1：纸色 #fbfaf6 每页 1 次；旧 #f7f1e2 0 次；禁用金/砖红 0 次；「·」0 次；
  刊头 196px；页码行 `Pagina N di 8` 每页 1 次；页脚意大利文。
- 禁词扫描：`吉伊卡哇` / `参考答案` / `酉之市` / `提名` / `简体` / `中文` / `中国` /
  `快讯` / `头条` / `本周` / `练习` 在 8 个 SVG 与 text.md 中均为 0 次。
- 目视 8 版＋网页 P1/P8：无溢出、无重叠、无压页脚、无 tofu；图片 5 张与图注/出处齐全；
  P6 图表有「練習用データ — 实际的调查并不是」标注，柱长与 38/24/22/16 成比例。
- ABSTRACT.txt：意大利文单行，无 ASCII 双引号，含真实主题（Tori-no-ichi、Beaujolais、sumo、
  30 nomination、Arashiyama）、A2–B2、150 esercizi。

## 翻译层专项（fan-out）

- 讲解/界面语言确为意大利文（页脚、栏头、Nota、题型标签、答案简析、P7 诊所/披露/预告、P8 说明）。
- 练习小节头冻结为日语：A 理解、B ことば、C 数字と日付、C 文を作りましょう、
  D ペアにしましょう、D 正しい・正しくない、B グラフ、C 数字と事実、D 文を完成しましょう、
  B 一般問題；`match_set` 指令为 `Abbinare`（25–28、43–46、141–144）。
- ちいかわ：`Chiikawa`（P7  gloss、P8 106/128 注）；`吉伊卡哇` 0 次。
- りくりゅう：gloss 用 romaji `ryuuryuu`（P7 金句 gloss、P8 66/77/80/105 注）。
- E 组翻译答案键已译成意大利文，p8 compare keydiff 恰为 [137,138,139,140]，status CLEAN：
  137 `Ni-no-tori è il 19 novembre.`（核心：二之酉在11月19日。）、
  138 `Il vino nuovo esce il 19 novembre.`（核心：新酒在11月19日解禁。）、
  139 `Le nomination delle parole di moda sono state annunciate il 5 novembre.`
  （核心：流行语提名在11月5日发表。）、
  140 `Chi vuole vedere le foglie deve controllare sia le date previste sia la situazione attuale.`
  （核心：去看红叶的人应该同时确认预报日期和现在的状况。）
  四条均为对日语题干的忠实意译，原因均为 E 组答案由中文译成意大利文；其余 146 键与核心一致。
- 转写完整性（map 文件缺失，见 O1）：改用端到端核实——freeze diff 字符级核算：
  本版 SVG 的 CJK 字符集整体是核心 CJK 字符集的子集（无任何本版独有 CJK 字符），
  且全部被替换的串均为中文家具/译注→意大利文；无中文残留（除有意保留者外——
  本版无有意保留的中文原文引用；全部中文均已译出）。

## U+2019 回归

- 8 个 SVG 中 U+2019 总数 0；U+0027 撇号共 29 处（P1 2、P2 3、P3 4、P4 1、P5 2、P6 0、P7 2、P8 15），
  目视抽查含撇号的行（P1 `l'inizio`、P3 `dell'uscita` / `quest'anno`、P4 `l'ultimo`、
  P7 `d'acquisto`、P8 `L'8 novembre`）均为窄字形，无宽字形断裂。

## 观察项（不计缺陷）

- O1. Builder 审计件缺失：任务与 KIT 引用的 `hidden_files/w47/scratch-fanout-ja/FANOUT-REPORT-ja.md`、
  `map-it.json`、builder 的 `it-*.json` 门结果与 `build-it-run*.log` 在工作树中均不存在
  （全仓 depth 4/5 搜索无果；该目录现仅有 ko stick8 的 3 个文件；本版目录与该 scratch 目录
  在 git status 中均为 untracked）。本次全部机械门均为我独立重跑（见 GATE-LOG.md），
  结论不依赖缺失文件；「221 个 map 键」的计数亦无法从 map 本身核实，已改用 freeze diff
  端到端核实转写完整性（上节）。
- O2. `tools/freeze.py diff --strict-cjk` 对本版报 FAIL（净增 CJK 15 字），经逐字裁定为工具误报实质：
  9× U+3000（全角空格分隔符，SOP §1.1 规定分隔符，核心家具中同样使用；净残差来自中→意家具串重切分，
  每页仅 1–2 字）；ノミネート 5 字（P8 注 107 回显题目自身的日语词；核心该注用中文「提名」）；
  楽 1 字（P8 注 58 回显 `千秋楽`；核心该注用简体「千秋乐」）。无新增目标语文本；本版用的
  均是正确的日语形。建议：strict-CJK 门的核算口径需备注此裁定，否则每个回显题干词的 fan-out 都会误报。
- O3. KIT §7 误引 P8 键 140：KIT 写 `Chi va a vedere le foglie dovrebbe controllare le date previste
  e la situazione attuale.`，实际印出（SVG＋PDF＋text.md 三处一致）为
  `Chi vuole vedere le foglie deve controllare sia le date previste sia la situazione attuale.`。
  印出文本是对日语题干的忠实翻译，无误；仅 KIT 记录过期/有误（137–139 与 KIT 引文一致）。
- O4. KIT §1「VOL.5 appears 3×」有误：实际印出 4 次（P4 正文句、P4 底条、P7 披露、P7 预告）。
  P4 正文句的 `VOL.5` 被切在两个 text 节点（`VOL.` 与 `5）…`），朴素 grep 只数到 3 次，
  是 KIT 计数方法的漏数；无规则限制 VOL.5 提及次数，仅 KIT 记录需更正。
- O5. 继承自已定稿核心版的外观项（已与核心版渲染图逐页对照，完全相同，不属本版缺陷，
  本版内无动作）：P2/P3/P5/P6/P7 中部空白带；选择题选项跨行断词（P3 Q29 フラ|ンス、Q30 `B.`|
  `11月の第3木曜日`；P4 Q47–49；P5 Q67 漫|画；P7 Q101 商|売繁盛；P8 Q125 緑のお菓|子）；
  P4 正文末句 `(VOL.` 与 `5）…` 分跨两栏。均为冻结日语正文＋同一版式，核心版已定稿时即如此。
- O6. 意大利语 gloss 的轻微软化（答案字母与事实均不受影响，仅备录）：P7 诊所
  `Il verbo finisce in forma ます.`（措辞略生硬）；P8 注 84 `aveva già cambiato colore`
  （题干为「色づき始めた」，「已开始变色」译成「已变色」稍强）；P8 注 86
  `Previsione meteo giapponese: Arashiyama 13 nov.`（未点名日本気象協会，题目问的正是该协会预报）；
  P8 注 103 `gli applausi quando compri`（较 Q17 同义注略短，缺宾语）。
