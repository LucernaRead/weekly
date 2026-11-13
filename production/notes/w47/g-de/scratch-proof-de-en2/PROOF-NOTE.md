# 校对笔记 — 2026-W47 de-en（重建后第二轮独立复校，全量）

- 对象：`production/2026-w47/2026-w47-de-en/`（德文目标语 × 英文读者语；重建 3，core build15）
- 校对员：本轮独立复校员（与重建者、core builder、第一轮复校员不同人；第一轮 proof1 (a) 已因旧 Q34 题干作废，本轮为重建后全新全量复校）
- 时间：2026-11-11 04:05–05:30 UTC（以 UTC 计；任务下发 04:04 EST）
- 只检查、不改成品：未改源、未重建、未跑 insert.py / lint --write，未 git add/commit/push/reset/stash，未碰 core-de、其他版、其他周、tools/。verify.py 未在原版目录跑（它会重写 SVG），其检查项用只读脚本在副本/原版只读复现；run.py / render.py / webpdf / export 未重跑。REG 复现在副本目录完成。
- 笔记目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-de-en2/`
  （PROOF-NOTE.md / GATE-LOG.md / scans.py / render_extract.py / verify_repro.py /
  keycheck_probe.py / freeze_source_reg.py / render/ / text/ / gates/ / copy/）

## 结论：(b) 有缺陷，共 2 处（D1、D2）—— 同一缺陷类，均在 P8，须修后重走复校

两处均为英文值里的英文弯双引号 U+201C/U+201D（任务专项规则：英语值里应为 0，德语引号 „" 保留）。
在 Noto Sans CJK SC 中这两个字形渲染为宽体全角字形（250 dpi 放大裁切可见引号前后留出明显空隙），
与重建 2 已修复的 U+2019 宽撇号是同一缺陷类。除 D1/D2 外，本轮全量复校其余全部通过，
含重建的两项改动（Q34 新题干、P3 box-title 修复）。

## 0. 开工探针与身份核对

- 探针 1（开工前）：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…`，成功。
  每道写盘/命令批前重探一次，全部通过；全程未遇 `Disk quota exceeded`（df：150G 总，72G 已用，78G 可用）。
- 探针 2：在 `hidden_files/w47/scratch-proof-de-en2/` 真实写文件成功。
- 印刷 PDF：`Die-Lucerna-VOL4-de-en.pdf` 10,966,409 字节，
  SHA-256 `47aae035c9531818bce832e25b2aed6ed2557c18229c514bf32443fb6becd429` ✓ 与任务一致。
- 网页 PDF：`Die-Lucerna-VOL4-de-en-web.pdf` 1,555,605 字节，
  SHA-256 `37ba00d4fcf83f7dd78fe6427d5b0c1ae70c9035fbe8dd345dfde8de13d12875` ✓ 与任务一致。
  （注：本版网页文件确为 `-web.pdf` 连字符，与任务简报一致；en 家庭 `.web.pdf` 的说法不适用于本版，
  磁盘实证与 build_edition.py 均为 `-web.pdf`。）
- text.md：`2026-w47-de-en.text.md` 49,665 字节，
  SHA-256 `2eb0363202b8c9eacc8aaaf5008eedab614b8ddb0301082e92eb80cd25d6b7f5` ✓ 与任务一致。
- 收尾复核：复校前后双 PDF 与 text.md 的 SHA/字节/mtime 均未变（印版 08:14:08、网页 08:15:10、
  text.md 08:15:52 UTC；SVG 08:15:21–08:15:40 UTC）；`git status` 只显示该版目录为未追踪（`??`），我未改动。

## 缺陷清单

### D1 — P8 H 写作框英文说明：英文弯双引号 “ ”（U+201C/U+201D），宽体渲染
- 页码：P8，H SCHREIBEN 框英文说明第 1 行。
- 原文（`content8.py:201`、`.text.md:1147`、P8 SVG、双 PDF 文字层均同）：
  `Write in German, 80–100 words: “My week in November”. Say what you make, which games you watch and with whom — and add one sentence about the Buß- und Bettag or Totensonntag.`
- 应改：改为本版惯例的德式引号 `„My week in November“`（与同版 P5 标题 `„Im Lande des Christkinds“`、
  P7 金句英文译文的 `„…"` 惯例一致；或改直引号 ASCII `"`，须全版统一）。
- 证据：
  1. 规则：任务专项要求 U+201C/U+201D/U+2019 在英语值里为 0（德语引号 „" 保留）；此处引号在英文句子里，
     框住的是英文标题，不是德文。
  2. 计数：全版 U+201D 共 2 处（D1、D2），core-de 为 0，其余 9 个 de-* 版（fr/es/it/pt/nl/ru/ja/ko/zh-tw）全版均为 0，
     本版是唯一引入英文弯双引号的版。
  3. 目视：250 dpi 放大裁切 `render/crop-p8-hbox2.png` 显示 `words: “My week in November” .`——
     开引号前、闭引号后各留出一个宽体字形空隙（`November”` 与句号 `.` 之间明显断开），与重建 2 已修的
     U+2019（`Let' s`）同一成因：Noto Sans CJK SC 把 U+201C/U+201D 画成全角宽字形。
     同裁切内德式 guillemet `«Leserbriefe»`（核心冻结原文）渲染紧贴，可作对照。
  4. 来源：核心中文用书名号 `《我的十一月的一周》`，译者转写为英文弯引号；核心德文同句用 `«Meine Novemberwoche»`。

### D2 — P8 答案键 Q67 注：英文弯双引号 “ ”（U+201C/U+201D），宽体渲染
- 页码：P8，ANTWORTEN — Page 5 — 键 67。
- 原文（`.text.md:1173`、P8 SVG、双 PDF 文字层均同）：
  `67. B (The 1903 calendar: “Im Lande des Christkinds”)`
- 应改：改为德式引号 `„Im Lande des Christkinds“`（与 P5 同标题的写法 `„Im Lande des Christkinds“`、
  P5 Q67 选项 B 的 `„Im Lande des Christkinds“` 完全一致；或改直引号 ASCII `"`，须全版统一）。
- 证据：
  1. 规则：同 D1，英语值（英文答案简析）里的 U+201C/U+201D 应为 0。
  2. 计数：同上，全版 U+201D 仅此 2 处；core-de 与其余 9 版均为 0。
  3. 目视：250 dpi 放大裁切 `render/crop-p8-key67.png` 显示 `calendar: “Im Lande des Christkinds”)`——
     冒号后、闭引号与右括号间各留宽体空隙。
  4. 同一标题三种写法：P5 正文/选项用德式 `„…"`，P8 键注用英文 `“…"，全版引号不统一；
     核心中文用 `《圣婴之国》`，无弯引号先例。

## 1. 重建两项改动逐一复核（全部通过）

### Q34 新题干
- 新题干 `"Am Montag öffnet in Köln der erste ___."`：源码 `content34.py` 1×、`.text.md` 1×、
  P3 SVG 1×、印刷 PDF 文字层 1×、网页 PDF 文字层 1×；旧题干 `"Am Montag öffnen in Köln die ersten ___."` 五处均为 0×。
  core-de 同样新 1× / 旧 0×（`content34.py:105`）。
- P3 目视：Q34 渲染为 `Am Montag öffnet in Köln der erste ___.`（见 P3 全页 `render/print-p3.png`），键 `Weihnachtsmarkt` 不变，
  与词框 `Weihnachtsmarkt · Glühwein · Lebkuchen · Advent · Weihnachtsbaum` 一致（单数阳性主格）。
- 冻结指纹：P3 冻结交集仍为 195 串，sha 由上一轮 `093cf378` 变为 `fc88f676`（仅题干字符串本身改了），
  其余 7 页 sha 与上一轮逐字节一致（见 §7）。

### P3 box-title 修复
- `WEIHNACHTSWÖRTER　Words`：从已发货 SVG 独立实测（`text_w`，bold，24pt）359.9px，预算 400.5px，
  墨水止于 x=1821.4，盒右缘 1862.0，余 40.6px；200 dpi 放大裁切 `render/crop-p3-boxtitle.png`
  可见标题完整收进奶油盒内，右侧留白清晰。
- 7 个 col3 框标题独立实测（从已发货 SVG 取串、按各自字号量墨水宽）7/7：
  P2 `DIE STILLE WOCHE　A quiet week` 394.6px、P3 `WEIHNACHTSWÖRTER　Words` 359.9px、
  P3 `DER TIPP　Editor's tip` 262.5px、P5 `ADVENTSWÖRTER　Advent words` 397.9px、
  P7 `DER WERKZEUGKASTEN　Toolbox` 382.9px、P7 `LESERBRIEFE　Readers' letters` 352.8px、
  P7 `NOCH EIN WORT　One more word` 366.1px——与 builder 的 boxtitle-en.log 逐一吻合。
  （注：任务所称“P3 box-title 7/7”实为横跨 P2/P3/P5/P7 的 7 个 col3 框标题；P3 本页占 2 个。）

## 2. 印刷 PDF 逐页目视 + 内容复校（除 D1/D2 外干净）

100 dpi 全页渲染逐页目视（`render/print-p1.png` … `print-p8.png`），并逐题验算 150 键（见 §4）。

- P1：干净。头条去空白 40 字符（≤56）。日期/星期全对：13.11 周五、16.11 周一（20.45 荷兰）、
  18.11 周三 Buß- und Bettag、22.11 周日 Totensonntag、29.11 周日首个将临期、17.11 周二 19:00 Dom 开幕。
  ZAHLEN 盒在栏内；FRAGEN 栏 5 问；Q1–Q10 键与正文一致（Q1 Bundesliga、Q2 Niederlande、Q3 Sachsen、
  Q4 Totensonntag、Q5 fünf、Q6 29. November、Q7 B、Q8 A、Q9 B、Q10 B）。
  **纠正第一轮笔记一处笔误**：第一轮 PROOF-NOTE 写“Q8 B 20.30”有误——Q8 选项实为
  `A. 20.30 Uhr · B. 15.30 Uhr · C. 18.30 Uhr`（core text.md:171 与本版 p1.txt:165 一致），正确键为 A，
  答案 20.30 本身无误。本轮 REG 键 Q8=A 已核对。
  "Germany's" 直撇号紧贴（对照）。
- P2：干净。日期算术 18+11=29、15+7=22、16+6=22 全对；"Elf Tage vor dem ersten Advent: immer ein Mittwoch" 对
  （29.11 周日往前 11 天为周三）。Perfekt 键 Q16–Q20 全对；配对 Q25–Q28（d/c/a/b）对；Q21–Q24（B/B/A/B）对。
  "Let's calculate"、"This week's dates" 撇号紧贴。
- P3：干净（除 box-title 已修项外）。市场日期全对（16.11 开、22.11 关、23.12 止、13.11 港口市场已开、
  17.11 19:00 正式开幕、20.11 亚琛开）；"fast zwei Wochen früher"（16→29 日 = 13 天）对；
  1930 画 "vor fast 100 Jahren"（96 年）对。Q29–Q46 逐题验算全对；"Editor's tip" 紧贴；配图在横线之上，图注无重叠。
- P4：干净。德甲第 9 轮 9 场进球逐场加总 4+3+3+7+4+1+3+2+3 = 30 ✓ 与正文 "30 Tore" 一致；
  最高比分 Leipzig–Augsburg 5:2 ✓；MD10 赛程（周五 20.30、周六 5 场 15.30 + Schalke 18.30、
  周日 Augsburg–Mainz 15.30、Bremen–Hamburg 17.30）与表注一致；24/25.11 欧冠、26.11 欧联星期（周二/周三/周四）对。
  Q47–Q64 逐题验算全对（Q51 B "8 und 5"、Q56–59 mehr/später/früher/mehr 均与比分/时间/积分吻合）。
  UND SIE? 盒与结果表边缘相接、无重叠（与核心一致）。"the league's return" 紧贴。见观察项 O1。
- P5：干净。周计划日期/星期全对（16.11 周一、17.11 周二、18.11 周三、19.11 周四、20.11 周五）；
  1903 日历 „Im Lande des Christkinds"、"über 120 Jahre"（123 年）对。Q65–Q82 逐题验算全对。
  1903 图在位，图注与横线无重叠（11px 间隙）。"The editors' week"、"What's" 紧贴。
- P6：干净。图表 44+33+23=100 ✓；Q83–Q100 逐题验算全对（Q85 44+33=77、Q88 100%、Q91 2,05 Cent、
  Q92 27. November（周五）、Q93 wird、Q94 ob、Q95 geht、Q96 beginnt、Q98 Kirchenjahr）。
  图表标签与条形无交叠，条形宽度 748/561/391 与数值成比例；ÜBUNGSDATEN 单行。"editors' practice example" 紧贴。
- P7：干净。金句 8 条逐字比对正文见 §3；三课 Q101–Q112 逐题验算全对（Q102 werden、Q103 wird、
  Q110 fraglich、Q111 dass 句动词居末）。工具箱 6 条末条在盒内；读者来信含 3 行披露（Editor's example）；
  VOL.5 预告与 P4 欧战日期（24.–26.11）及第 11 轮一致。"Readers' letters"、"Learners'…"、"Editor's example" 均紧贴。
- P8：干净（除 D1/D2 两处英文弯引号外）。A 完形 113–120、B 121–128、C 129–132、D 133–136、E 137–140、
  F 141–144、G 145–149、H 写作逐题验算全对；MUSTER 84 词逐词数过（84，与标签一致），要点齐全；
  答案末端在页脚之上（keys 末端 2481，底边 2560，余 79px）；Q133 "Die Bundesliga kehrt…" 无粘连。
  德文 H 指令用 `«Meine Novemberwoche»`（核心冻结原文，guillemet 渲染紧贴）。

## 3. P7 金句 8 条（逐字比对正文，全部 2 次）

8 句在全刊正文连接文本中各出现恰好 2 次（正文 1 次 + P7 引用 1 次），出处页/级别均正确：
1. "Nach zwei Wochen Pause spielt am Freitagabend der FC Bayern gegen den 1. FC Köln."（P1·A2）
2. "Es geht ums Viertelfinale der Nations League."（P1·A2）
3. "Nur in Sachsen ist der Buß- und Bettag ein gesetzlicher Feiertag."（P2·A2）
4. "Die Märkte beginnen fast zwei Wochen früher."（P3·A2）
5. "Hinter jedem Türchen wartet eine kleine Überraschung."（P5·B1）
6. "Der FC Bayern gewann in Mainz mit 2:1."（P4·B1）
7. "Die stille Woche ist der Übergang: vom November in den Advent."（P6·B2）
8. "Am Sonntag ist es still im Land."（P6·B2）
英文译文逐句核对，均忠实（BrE "Bayern play" 等无误）。金句的英文译文不带引号；
P7 的 U+201C 均为德文句的德式引号 `„…"`（21 处，与 U+201E 配对），不在缺陷之列。

## 4. 150 题逐题验算（独立复现，不采信 builder 的 keycheck 文件）

- 方法：把版目录复制到我方 scratch（`copy/`），在副本里 runpy 五个 content 模块重建 REG，
  再用 `tools/p8.py extract`（自跑）抽取 P8 印刷键，逐题比对；同时把我方 REG 与 builder 的
  `en/keycheck-150.json` 逐项比对。
- 副本重跑：REG 总数 150，编号连续 1–150；分版 10/18/18/18/18/18/12/38；
  级别 A2 69 / B1 67 / B2 14；题型 MC 52 / fill-in 41 / transformation 11 / true-false 8 /
  cloze 8 / sentence building 8 / matching 12 / translation 4 / dialogue 5 / writing 1——
  与 KIT 完全一致。副本 8 个 SVG 与原版 SVG 字节相同（8/8，构建确定性独立证实）。
  流向末端与 builder 记录一致（P1-headline 1554、P3 col3 1643.19、P8 keys 2481 等）。
- 我方 REG 与 builder keycheck-150.json：150/150 逐项一致（n/page/level/type/key），差异 0。
- REG 键 vs 我方 P8 抽取键：149/150 精确；唯一非精确为 Q150：抽取器把 REG 键
  "Open task — follow the points in the writing box" 截断为 "Open task"。
  该截断与 builder 所述一致，且 Q150 已在 keydiff 集合中；开放写作题无固定键，属预期内。
- 全部 150 个 REG 键另经人工逐题对照题面/原文/图表验算（见 §2 各版记录），无一错误。
  （D1/D2 不涉键值：D2 所在 Q67 键 `B` 正确，只是键注里的德文标题引号用了英文弯引号。）

## 5. p8 compare keydiff 逐条核实（自跑：CLEAN，keydiff [137, 138, 139, 150]）

- Q137：核心键 '德甲周五回归。' → 本版 'The Bundesliga returns on Friday.'——
  E 组正向翻译题答案键译成英文，预期内。
- Q138：核心 '市场周日关闭。' → 'The markets are shut on Sunday.'——同上，预期内。
- Q139：核心 '我做一个降临节日历。' → 'I am making an Advent calendar.'——同上，预期内。
- Q140：核心与本版键完全相同（德语句 "Am Montag schaue ich zu Hause Deutschland gegen die Niederlande."）——
  反向题（英译德），键本就是德文目标语句，正确地不在 keydiff 中。
- Q150：核心 '开放题' → 'Open task'——开放写作题标签译成英文；抽取器截断见 §4。预期内。
- 结论：4 条 keydiff 无一为真缺陷。missing=[]，extra_count=0。

## 6. 禁词 / VOL / 徽章 / 字号 / 翻译层

- 禁词：verify.py 全部 18 项（桥接、Le Lucerna、The Lucerna、VOL.3、VOL.2、Geisterspiel、
  Karneval、Volkstrauertag、NFL、American Football、11.11、Tankrabatt、14,04、Hart aber fair、
  Klassiker、Allerheiligen、8,35、ZEW）8 个 SVG 全无。
- VOL：VOL.4 出现 9 次（8 个页脚 + P1 刊别行），VOL.3/VOL.2 为 0；VOL.5 出现 6 次，
  均为下期预告/读者来信 VOL.5 引用，预期内；刊头 "Die Lucerna"、周头
  "WOCHE VOM 16. BIS 22. NOVEMBER 2026"、副标题 "TEXT IN GERMAN · EXPLANATIONS IN ENGLISH" 在位；
  页脚逐页 1 枚、页码行 Page 1–8 of 8 逐页在位；头条去空白 40 字符（≤56）。
- 徽章（rx="2.7" 矩形，自数）：逐页 10/15/18/15/18/18/12/35，全刊 141 ✓；
  P8 按级别 A2 22 / B1 13 / B2 0 ✓。
- 字号：P8 最小字号 9.94pt（PyMuPDF 实测印刷 PDF + SVG 13.25 单位 ×0.75 双重确认），
  ≥9.75pt 底线 ✓（低于 11.25pt 目标，属 SOP §1.1 让步第 4 步，KIT 已写明）；其余各版最小 11.62–12.75pt。
- 样式：PAPER #fbfaf6 / INK #302c28 / OLIVE #46581f / CLOTH #37402f，旧式金色/近黑底色值全无。
- 翻译层：讲解/界面语言确为英文；8 个 SVG 的 `<text>` 中唯一 CJK 字符是全角空格 U+3000
  （家具分隔符，每版 12–16 处）；text.md 汉字/假名/韩字 0 个（U+3000 计 122 处）。
  冻结源码级：核心无 CJK 常量在版内缺失的仅 5 处，均为预期 transform 产物
  （masthead 副标题、全角括号 '（' '）'、间隔符 ' · '、PDF 文件名 'Die-Lucerna-VOL4-de.pdf'）；
  版内新增无 CJK 常量 449 处，含非 ASCII 者 61 条，抽查均为德语词+英文释义串，无新增德文正文句。
- text.md 与 core text.md 全量 diff（235 组改动行，见 `gates/textmd-core-diff.txt`）逐组读过：
  全部为讲解层中文→英文，德文正文行逐行未动；core 非 CJK 行 327 行中仅上述 2 行预期项未入本版
  （版头 slug 行、masthead 副标题——后者为已知冻结缺失项）。

## 7. 弯标点专项（U+201C/U+201D/U+2019）

- U+2019：8 个 SVG 全扫总数 0 ✓（逐页 0/0/0/0/0/0/0/0）；text.md 0。直撇号 U+0027 逐页 1/2/1/1/2/1/3/0，共 11 处，
  与 KIT 所述 9 处修复 + P1 对照 1 处 + P5 "What's" 1 处一致；目视均紧贴，无宽字形断裂。
- U+201C：全版 35 处——P1 5、P5 6、P7 21、P8 3。其中 33 处为德式引号 `„…"` 的闭引号
  （P1 德文提问 5、P5 德文标题 6、P7 德文句/金句 21、P8 德文对话 1），与 U+201E 开引号逐一配对，保留 ✓；
  其余 2 处为 D1、D2 的英文弯引号开引号（见缺陷清单）。
- U+201D：全版 2 处，即 D1、D2 的闭引号；core-de 0，其余 9 个 de-* 版 0。**不通过。**
- 德式 guillemet «»（U+00AB/U+00BB）：P1 `« der Adventskalender »`、P5 `SÄTZE MIT «WEIL»`、
  P7 `«der Adventskalender»`、P8 `«Meine Novemberwoche»` / `«Leserbriefe»`——
  全部为核心冻结原文（core P7/P8 SVG 同串），渲染紧贴，不在任务所列三码点之列，不计缺陷。

## 8. 机械门（全部自跑，与构建相同的解释器）

构建解释器确认：`~/workspace/weekly-git/tools/venv/bin/python`，Pillow 13.0.0。
详见 GATE-LOG.md。

| 门 | 自跑结果 |
|---|---|
| occlusion_audit.py（自检通过：6 类 planted 全触发，clean 对照静默） | 0 flags ✓ |
| p8.py extract | 150/150（版 + 核心各一） ✓ |
| p8.py compare vs core | CLEAN，missing=[]，extra=0，keydiff=[137,138,139,150]（§5 已逐条核实为预期内）✓ |
| freeze.py diff | exit 0；新增 CJK 7 个，全为 U+3000（P2–P8 各 1，P1 0）✓ |
| freeze 直接 sha256（渲染级冻结交集，sorted + "\n" 连接） | 8/8：逐页 147/163/195/166/173/175/150/186，sha 前 8 位 083e2a2a / 689045ad / fc88f676 / df1bebf7 / 86fa4421 / 2bbe05f9 / b7aa0771 / 57e118e7，P3 为新 Q34 指纹 ✓ |
| print/web 文字层（pdftotext） | default：print 50,434B / web 50,435B，词多重集相同；raw：均为 49,277B，归一化后完全相同；web 有真实文字层 ✓ |
| measure.py | 24/24 PASS，0 FAIL ✓ |
| verify.py 全部检查项（只读复现，未在原版目录跑） | verbatim 8 句各 2 次 ✓；样式审计 ✓；MUSTER 84 词 ✓；页脚/页码逐页 ✓；头条 40 字符 ✓；P8 底线 9.94pt ✓；图表 44+33+23=100 ✓；日期算术 3 组 ✓；星期全对 ✓；P6 条形 748/561/391 ✓；禁词全无 ✓ |
| chips | 141 枚（见 §6）✓ |
| P8 最小字号 | 9.94pt ✓ |
| boxtitle（从已发货 SVG 独立实测） | 7/7（见 §1）✓ |

## 9. 网页 PDF 逐页校对

- 8 页齐全（pdfinfo：8 页，1462.5×2025pt，1,555,605 B < 7 MB）；P1、P8 全页 100 dpi 目视与印刷版一致，
  无缺字、无豆腐块；逐页词多重集印刷/网页完全相同（P1–P8 各页均相同）。
- 文本层完整：default 50,435B、raw 归一化 49,277B 与印刷版一致（见 §8）。
- abutting：SOP.md 与 tools/ 均无 "abutting" 一词的既有检查定义。本轮以逐页词多重集 +
  逐 span 坐标比对代行：P6 图表区印刷/网页的全部标签与数值 span 坐标逐一相同至 0.1pt
  （44 % (991.5, 1108.9)、33 % (851.2, 1147.9)、23 % (723.8, 1186.9) 等），
  无 >0.5pt 的位移或缺口。pdftotext 逐页读出顺序在 P6 图表区有一处换行归属差异
  （"33 %" 的归属行），纯属抽取顺序 artifact，词多重集相同、渲染像素相同（`render/chart-p6-web.png`），
  不计缺陷。
- 工具层观察项 T1（单列，不与内容缺陷混同）：本版网页 PDF 用 D2 补丁落地前（`:style=Bold`）的旧 webpdf.py 建成，
  pdffonts 显示无 `LucernaNewsreader-Bold` 与 Italic 子集（只有 Regular；印刷版含 Newsreader-Italic）。
  网页版标题/粗体以 Regular 字重渲染，100 dpi 目视与印刷版几无可辨差异，内容与几何均不受影响；
  按任务说明，pre-insert 会以定稿工具全部重建，此项不计入内容缺陷。

## 10. 观察项（不计缺陷）

- O1（继承自核心，core-de P4 同样如此；第一轮已裁定、builder 报告亦裁定不是缺陷）：
  P4 正文提到 "der VfB Stuttgart verlor in Istanbul bei Galatasaray mit 0:2"（欧冠第 4 轮），
  但 "DIE ERGEBNISSE & DER SPIELPLAN" 表未列该场。核实：核心 core-de 的 P4 SVG 同样只有正文句、表内无此场；
  freeze P4 removed 串仅为中文讲解层，fan-out 未删任何德文赛果行。表内德甲 9 场齐全（30 球已验算），
  无任何练习题依赖该场赛果。本版不因此阻断。
- O2（措辞，可斟酌；第一轮已记，源自核心中文注直译）：P8 答案 Q56 注 "(5–2 more goals than 2–1)" 表述压缩生硬，
  宜读作 "5:2 一场进 5 球，多于 2:1 一场的 2 球"。键 "mehr" 正确，含义可还原；非事实错误，不计缺陷。
- O3（核心既有、KIT §8 已列为 honest shortfall）：P1 头条首段无首字下沉（与已接受的 W46-FR 版相同情形）。
  fan-out 未引入，不计缺陷。
- 另：工具箱 "Es ist fraglich, ob … = Whether … is open" 与答案键注 "(fraglich: whether … is still doubtful)"
  措辞不完全一致，但两者同义（未定/存疑），均忠实，非事实错误，不计缺陷。

## 附：已覆盖核查点

8 版印刷目视 + 网页 P1/P8 目视 + 网页逐页文字层、150 题逐题验算、金句 8 条、禁词、VOL.4、
徽章 141 枚、P8 字号、翻译层 360 字面量、U+2019/U+201C/U+201D 专项、Q34 五处 1×/0×、
box-title 7/7（独立实测 + 放大裁切）、机械门全套、text.md 全量 diff 审读。
未核查项：无。
