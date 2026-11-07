# 独立校对报告 — Lucerna Weekly W45 EN×IT（英语×意大利语分版）

**结论：ZERO PROBLEMS**（阻塞项 0；非阻塞观察见末节）。本报告不宣布上架；上架由主线串行执行。
校对员仅校对，未改源码、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、
未改核心/W43 目录（只读对照）、未清理共享 scratch 目录、未派生任何下级代理。

## 0. 开工查重与哈希

- 开工时 `files/weekly-report-w45-en-it/` 与 `hidden_files/weekly-report-w45-en-it-build/` 无进行中渲染进程；
  交付物最新 mtime 为 00:45–00:50（已完成交付），90 秒复查 SVG/卡片/PDF 零新写盘后开工，未 stand down。
- 校对前记录全部交付物与核心 sha256（`before.sha256`）；校对后复核（`after.sha256`）：
  `diff` 无差异，**HASHES_UNCHANGED_PROOFREAD**。
- 交付物核实（与 KIT 一致）：
  - print PDF `The-Lucerna-VOL2-IT.pdf` 17,290,297 B，sha256
    `9f7d94ad572374ed5a1b8f82316c152c8ac516166b4a5eb99563ae174ac6efdb`
  - web PDF `The-Lucerna-VOL2-IT-web.pdf` 3,999,180 B，sha256
    `d3607b57c36bb7f1705c107b8073c936d7a8e103508bc22da52d730bc6c8eec4`
  - 两 PDF 均为 8 页（`/Count 8`）；SVG 8 张 sha 与 KIT 所列逐项一致（见 `before.sha256`）。
  - 卡片 8 张均为 1950×2700 RGB PNG。

## 1. 冻结（freeze）

- `tools/freeze.py baseline --build hidden_files/weekly-report-w45-en-build`（核心原构建树）：
  **8/8 逐字节复现**，核心 SVG 校对前后哈希不变（`freeze-core-baseline.log`）。
  - 说明：若误以分版构建树跑 baseline 会得 0/8，那是“已变换的树”而非核心基线失败；
    正确口径是核心原树，本项以核心原树为准。
- `freeze.py diff` 核心→分版：新增 CJK **每页均为 0**（核心 CJK 总量 P1 183 / P2 197 / P3 119 /
  P4 139 / P5 134 / P6 136 / P7 347 / P8 776 → 分版全部 0）；分版 8 页 CJK 字符总数 0。
- 违禁扫描（分版全部 8 页 SVG + KIT + ABSTRACT）：**“桥接”0 次、德语字符（ä/ö/ü/ß）0、
  德语功能词（und/mit/für/von/zu/ist/nicht/eine/der/die/das 等整词）0**（`scans.log`）。
- Token 级 adjudication（本人独立词表差分，`token-diff.txt`，非照搬构建员结论）：
  - P2–P6 丢失词仅 3 个/页：`ENGLISH / LUCERNA / WEEKLY` —— 全部来自页脚槽位
    （核心页脚 `The Lucerna · 英语周报 VOL.2 · LUCERNA ENGLISH WEEKLY` → 意大利页脚），正文无丢失。
  - P1 另丢失：`THE / LEARNERS / WEEKLY / REAL / LIFE / FROM / AMERICA` —— 全部来自刊头副标题槽位
    （核心 `THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA` → 意大利副标题）；
    `midterm` 小写丢失 1 次对应 `Midterm` 增加 1 次（R3 WORD 单行化后的首字母大写），非丢失。
  - P7 另丢失 `VOL` 1 次：核心页脚 VOL.2 槽位所致（分版 P7 仍有 VOL.3 预告，见读者园地节）。
  - P8 另丢失 `change` 1 次：仅为 140 题注释措辞 `change 变化` → `changes = cambiano`，
    对应新增 `changes`；键本身为合法重定向（见 §2）。
  - 串级 removed 清单复核（`removed-strings-check.txt`）：所有含英文的 removed 串均为
    (a) 中英双语标题中英文部分在分版中保留（如 `TELLING THE TIME · …`）、
    (b) 换行切分碎片（如 `seats in the House, all on the ballot（众…`，完整句在分版中仍在）、
    (c) gloss 碎片。**无英语正文丢失。**

## 2. P8（独立重跑 + 78 口径独立确立）

- `tools/p8.py compare` 独立重跑：**CLEAN，核心 78 noted = 分版 78 noted，
  missing=[]、extra=0（extra_count=0）、uncertain=[]、keydiff=[137,138,139,140,150]**
  （`p8-compare.log/.json`；双向 extract 集合逐项相同）。
- **78 口径的独立确立（不依赖 p8.py 解析器）**：从核心源码规则重算——核心 content8 印刷规则为
  `note 非空 且（页==8 或 len(note)<=10 或 类型∈{改错，图表读数}）`；在隔离复本中运行核心构建树
  的 REG，算得印刷集合恰为 78 项，与 p8.py 渲染解析集合逐项相同
  （`regdump/dump.log`，集合见该日志）。分版按其规则（同规则 + NOTE_EXTRA 27 项）同样算得 78 项
  （`regdump-ed/dump.log`）。NOTE_EXTRA 集合与 KIT 所列 27 项逐项一致。
- keydiff 逐项印刷行对照（渲染 SVG 原文，`scans` 段 + §2 证据）：
  - **137 EN→IT 合法**：核心 `137. 耐心是制度的一部分，而不是制度的失败。（part of 一部分；not a failure 不是失败）`
    → 分版 `137. La pazienza fa parte del sistema, non è un fallimento del sistema. (part of = una parte di; not a failure = non un fallimento)`；
    题干保留 `Translate: « Patience is part of the system, not a failure of it. »`，重定向成立。
  - **138 IT→EN 合法**：分版 `138. Tuesday, November 3, is Election Day in the United States. (giorno delle elezioni = Election Day; di martedì = on Tuesday)`；
    题干 `Traduci: Martedì 3 novembre è il giorno delle elezioni negli Stati Uniti.`，重定向成立。
  - **139 IT→EN 合法**：分版 `139. On Sunday, the NFL plays in Madrid. (questa domenica = on Sunday; a Madrid = in Madrid)`；
    题干 `Traduci: Questa domenica la NFL gioca a Madrid.`，重定向成立。
  - **140 EN→IT 合法**：核心 `140. 并非每处都拨回时钟。（not every 并非每处；change 变化）`
    → 分版 `140. Non tutti i luoghi cambiano. (not every = non tutti; changes = cambiano)`；
    题干保留 `Translate: « Not every place changes. »`，重定向成立。
  - **150 写作登记转意大利语合法**：核心 `150. 开放题 — 要点见写作框，范文在第 8 版写作框内（按要点给分）`
    → 分版 `150. Compito aperto — punti chiave nel riquadro di scrittura; testo modello nel riquadro a pagina 8 (Valutazione per punti chiave)`。
  - 无括号解析伪影：137–140、150 的键均为完整句/完整登记语；P8 键区 15.5pt 条件印刷
    （`kf.para(..., 15.5, ...)`）与核心一致，未用德语版 13.5pt 全印形式。
- P8 注释语言：78 条注释全部为意大利语（`regdump-ed` 注释全表已摘录核查）；
  其中英语仅见于任务本身的键/体或被讲解的英语词本身（如 `still = ancora`、`I VOTED` 贴纸原文、
  `a teacher from Ohio` 阅读原文引用、`Election Day / on Tuesday` 对译项），符合“纯意大利语”口径。
  注释尾随的选项字母（41 c、58 a、74 c、141 b、142 c、143 d、144 a）为核心原有格式，逐字对译，非缺陷。

## 3. P1 头条流 R1→R2 的 424px 差值专项

- 事实复核：R1 日志 `flow[P1-headline] ended col 2/2 y=1921 (bottom 1828)`；
  R2/R3/R4 日志均为 `ended col 2/2 y=1497 (bottom 1828)`，差值 424px 属实；终版无 `!!` 溢出警告。
- **完整性独立验证（全部成立）**：
  - P1 全部 10 个栏目头在分版中均在：AMERICA VOTES ON TUESDAY、THE BIG STORY、TRY IT NOW、
    THE WEEK IN NUMBERS、SEARCHES OF THE WEEK、IN THIS ISSUE、THE WORD OF THE WEEK、
    FALL, THE SEASON OF VOTES、IN BRIEF、LIGHTNING QUIZ。
  - 头条 5 段全部句子头（共 17 句）在核心与分版渲染文本中均命中（逐句核查，含
    `All 435 seats in the House…`、`Some races are called on Tuesday night ; others take days.` 等）。
  - 题量：P1 练习 1–10 全部在位（REG：1–6 TRY IT NOW、7–10 LIGHTNING QUIZ；级别 A2 8 / B1 2，
    与核心一致）；numbers 框、gloss 桥、IN THIS ISSUE 均在卡片目视中完整。
  - **结论：完整性成立，机理未证明记为非阻塞过程记录缺口**（与任务指令一致）；
    未发现任何内容缺失，故不构成阻塞项。

## 4. 几何

- `occlusion_audit.py`（自检先行）：6 类 planted 各命中 1 次、干净对照静默；
  **分版 0 / 核心 0 / NEW vs 核心 0**（`occlusion-ed/core/new.log`）。
- 框线压框扫描（builder `scratch-checks.py` 重跑）：**0**（分版与核心均为 0）。
- 同基线家具间距（解码后测量，分版，`scratch-ed.log` §4）：全部为正——
  P1 顶带 y=92 gaps **[401.0, 113.0]**、P1 黑带 y=478 **[49.0]**、y=522 **[153.0]**、
  每页页脚 y=2624 **[827.0]**、P8 黑带 y=478 **[30.0, 18.0]**。与 KIT 一致。
  （对照：核心同基线为顶带 564/277、黑带 288/213、页脚 1118——差异来自意大利页脚/刊头措辞长度，
  均为正间距，无重叠。）
- P6 图表覆盖（基线锚定墨迹法，PIL textbbox anchor `ls`，门限 <30%）：4 标签均为 **0.0%**
  （`No lines : 38%`、`Work on Tuesday : 29%`、`Travel plans : 21%`、`Habit : 12%`）。
  无条形确为核心原样：核心 content56 源码注释明言“chart bars … is complex; use text bars in flow”，
  循环体仅输出 `f.para(f"{lab} : {pct}%", …)` 文本标签，`bw`（280/214/155/88）从未用于绘制矩形；
  核心与分版 P6 在标签区域均无矩形（各 26 个 rect，总数相同），且分版图表标签墨迹与核心同款。
- 右缘 ADVANCE 扫描（终轮，分版 9 项，`rightedge.txt`；墨迹全部 ≤1904，在内框 1910 以内）：
  - 核心同款节点 5 项（文本与 advance/ink 值与核心逐项相同）：P4 图注 1888.6/1889；
    P8 F 选项 1903.8/1904、1899.4/1899；P8 对话行 1891.3/1891、1890.3/1890。
  - 分版新增 P8 键区满栏换行 4 项：150 区 1896.8/1897、148–149 区 1892.3/1893、
    139–140 区 1890.5/1890、139 行 1890.3/1890——均为冻结键 + 意大利注释的 svglib 换行量度差所致，
    不可缩短（缩短即动冻结键），模式与核心自有的 1904 行相同，全部在框内。
  - P1 搜索说明行 R4 缩短后终值：`Popolarità relativa, non numeri esatti.`（x=1473, y=1266）
    advance-right **1806.6**、ink-right **1807.0**，远在 1885 栏缘以内（R3 旧值 1891.8/1892.0 已消除）。
- R3 的 P1 WORD 段单行化终态：分版 P1 仅 1 个 WORD 节点
  `<text x="1451" y="1820" font-size="19">Midterm election = elezioni di medio termine.</text>`；
  行 B 分隔线为 `<line y1="1844" stroke-width="1.2">`（上缘 1843.4），19pt 单行墨迹底远在其上，无压线。
- R4 变化范围验证（`baseline-round4-pre.sha256` 对终版）：**仅 P1 SVG + P1 卡片 + 两 PDF 变化**；
  P2–P8 SVG 与卡片逐字节不变（8 项 SAME，4 项 DIFF 恰为 P1 SVG/P1 PNG/两 PDF）。

## 5. gloss

- 本人直接从核心源码测得（非照搬构建员数字）：`gloss()` 调用分布
  P2 **3** / P3 **4** / P4 **4** / P5 **3** / P6 **4**，合计 **18**（`gloss-p7-readers.txt` 前段）。
- 词头 1:1（核心→分版）：P2 to fall back / a costume / trick or treat；P3 to open / a monster /
  a catchphrase / a series；P4 a fixture / a title / to defend / a fan；P5 a map / too close to call /
  a second screen；P6 to register / a governor / to shape laws / patience——渲染后 SVG 中每词头在两版均命中，
  分版每页均有 `Nota — ` 前缀。P1 gloss 为 `bridge()` 调用（`Spiegazione | a midterm = medio termine · …`，
  4 项），与 KIT 口径一致，不计入 18 项。

## 6. P7

- 定义句逐字保留：P7 全部 11 个英文定义段（FALLING BACK、GOING TO + VERB、COMPARATIVES、
  THE PAST SIMPLE、HEADLINE PRESENT、WHETHER = IF ?、TOOLBOX 三句及报纸反射句）在核心与分版源码中
  逐字相同（diff 仅改标题中的中文→意大利文及 B2 例句注释 `part of = 一部分` → `part of = una parte di`）。
- 金句 8 句原文逐字：渲染后（空白归一化）8 句在核心与分版中全部命中；
  级别序列（源码 phrases 表 + REG 100–107 级别）为 **A2, A2, B1, B1, B2, B2, A2, B1**，与任务所给序列一致。
- 片段计数（渲染全文计数）：P7 **[1,1,1,1,1,2,1,1]**、全刊 **[3,2,2,2,2,4,3,2]**，
  核心 = 分版逐项相同（Patience 句在 P7 出现 2 次：金句表 + B2 例句框）。
- P7 结构与核心一致：A2/B1/B2 三栏 + TOOLBOX + PHRASES OF THE WEEK 100–107 + ERROR CLINIC 108–111 +
  READERS' CORNER + NEXT WEEK · VOL.3。
- 注：任务提及的“与 EN×ES/EN×FR 校对实测一致、可作 EN×PT 差异旁证”一句，本次校对未重测 ES/FR/PT 分版，
  仅记录为构建员转述，不作为本报告的独立结论。

## 7. 读者园地

- 英语元素逐字冻结：例句
  `« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)`
  在分版渲染与源码中与核心逐字相同（无新编读者、姓名、引言）。
- 意大利语披露句逐字摘录（分版 P7 渲染 + 源码一致）：
  `Nota della redazione | Alla chiusura di questo numero non sono arrivate vere lettere dei lettori e non ci sono testi di scrittura del VOL.1 da premiare come migliori. L'esempio qui sopra resta quindi indicato onestamente come esempio; le vere lettere usciranno dal VOL.3. Mandaci la tua lettera e il tuo testo: li pubblicheremo nel VOL.3!`
- 逐项核实：(1) 截至截稿未收到真实来信 ✓；(2) 无 VOL.1 写作投稿可评为最佳 ✓；
  (3) 例句仍诚实标注为例句、真实来信自 VOL.3 起 ✓；显性祈使邀请
  `Mandaci la tua lettera e il tuo testo:` ✓ + VOL.3 刊登承诺 `li pubblicheremo nel VOL.3!` ✓；
  VOL.3 预告行（NEXT WEEK 框）未计入邀请。
- 最佳 P8 作文覆盖范围显式裁定：P8 写作题英文说明保留“最佳文本将登于 VOL.3（第 7 页读者园地）”；
  披露句中的“VOL.1 写作投稿”即指可供 VOL.2 评选的那批投稿池——披露“无此投稿可评为最佳”，
  故本期无最佳作文颁布、无凭空获奖者，覆盖成立。无凭空新写英语披露句（披露句为意大利语）。

## 8. 家具（W43 同配对偏差清单逐项核实）

- 页脚 VOL.2 形式：8 页均为 `The Lucerna · SETTIMANALE INGLESE VOL.2 · TESTI IN INGLESE · SPIEGAZIONI IN ITALIANO · Pagina N di 8`，
  与 W43 同配对页脚范式一致（仅 VOL.1→VOL.2）。
- 徽章 BRICK **#a4553a**：分版 P1 出现 12 次、P8 出现 4 次，与 W43 同配对 SVG 次数相同；
  徽章节点（x=975, y=372, middle 锚点，`TESTI IN INGLESE · SPIEGAZIONI IN ITALIANO — …`）与 W43 同位。
- P8 键区：核心 15.5pt 条件印刷 + NOTE_EXTRA（源码 `kf.para(..., 15.5, ...)` 与 NOTE_EXTRA 27 项集），
  未用德语版 13.5pt 全印形式。
- P1 意大利措辞缩短：transform.py R2 记录（黑带行、趋势副标题、数字行、gloss 桥 gap 12→6/9→5、
  TRY head gap 13→8）+ R4 搜索说明行缩短，终版卡片无溢出。
- P2 框行高 29→30px：源码 `eh` 公式中意大利块系数确为 `* 30`（`content12.py:201`），英语块为 `* 30.5`；
  AND YOU 框卡片目视无压框（框线压框扫描亦为 0）。
- P8 电池 gap 11→8：transform.py R2-6 将 B/C/D 三组 `bf.ex(..., size=20.5)` 改为 `gap=8`；
  终版 P8 电池 flow 止于 y=1390（底线 1485），键区止于 col 3/3 y=2187（底线 2545），与 KIT 一致。
- TOO CLOSE 标题量宽复核（见非阻塞观察 2）：`In bilico` 墨迹右缘 432，框内缘 481，余量 49px， fits；
  构建员“`Troppo incerto` 仅余约 2px”之说未能复现（实测溢出），但换用 `In bilico` 的决定本身正确，
  且 gloss 中仍保留直译 `troppo incerto per decidere`，语义无损。

## 9. 图片、ABSTRACT、卡片、题量、范文、PDF

- 图片载荷与核心逐页相等：P1/P2/P3/P4/P6 各 1 图，P5/P7/P8 0 图，位置尺寸与核心相同；
  5 张图片 data-URI sha256 核心 = 分版逐项相同（P1 `58010598…`、P2 `960958ec…`、P3 `989526b0…`、
  P4 `86b34e8f…`、P6 `85b54b4f…`，前缀见证据）；署名在版：P1 Kenneth C. Zirkel — CC0、
  P2/P6 Public domain、P3 Édouard Manet — CC0、P4 Frank R. Snyder — public domain，均 via Wikimedia Commons，
  与核心逐字相同。无新增/替换/重署名图片。
- ABSTRACT.txt：意大利语单行（464 字节，无换行符）、无 ASCII 双引号；
  含刊名 The Lucerna、A2–B2、150 esercizi、本周全部真实主题关键词
  （11 月 3 日中期选举日、11 月 1 日 25 小时拨钟夜、Halloween、11 月 6 日两部电影全名、
  11 月 8 日 NFL 马德里赛、美国投票制度深读）及学习者搜索短语
  `impara l'inglese leggendo le notizie americane`。
- 8 卡片全部逐页目视：P1（R4 终版）至 P8 逐页看完，无重叠、无出框、无缺题；
  P4 底部“On Saturday, November 7, the”后接中栏“warm-up is already on…”为分栏续接，核心同款，非截断。
- 题量与级别（隔离区 REG 独立展开，核心与分版 REG 各自重跑）：
  **150 题连续 1–150；A2 60 / B1 69 / B2 21；页分布 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39**，
  两版 n/级别/页码逐项相同。
- 范文：P8 MODEL `My Tuesday, November 3` 源码与渲染在两版中逐字相同；
  空白切分计词 **85 词**，与核心一致。
- transform.py 替换数：R4 日志 `transform done, replacements: 309`，与任务所给一致。

## 非阻塞观察（均不构成阻塞项）

1. **P1 头条流 424px 差值机理未从 Flow 代码层面证明**（构建员已如实记录，KIT 亦载明）：
   完整性已由卡片、题量、栏目头、全部句子头四重证据证实，故记为过程记录缺口，非阻塞。
2. **TOO CLOSE “`Troppo incerto` 仅余约 2px”之说未能复现**：以 builder 同款量法（NotoSansCJK Bold 23pt，
   anchor `ls`）量得 `TOO CLOSE TO CALL · Troppo incerto` 墨迹右缘 510，框内缘 481（溢出 29px）、
   框外缘 499（溢出 11px）；`In bilico` 墨迹右缘 432，余量 49px。结论方向不变——`In bilico`
   不仅 fits 且余量充裕，直译则根本放不下；仅构建员的过程数字不准确，不影响交付。
3. **freeze baseline 的口径说明**：对分版构建树跑 baseline 得 0/8 属预期（该树已变换）；
   本报告以核心原树 8/8 为准，特此记录以防误读。
4. **P8 注释尾随选项字母**（如 41 c、141 b）为核心原有格式，分版逐字对译，非缺陷。
5. **跨分版级别序列旁证**（ES/FR/PT）本次未重测，仅记录为转述，不作独立结论。

## 证据文件（本目录）

- `before.sha256` / `after.sha256`（校对前后哈希，diff 为空）
- `freeze-core-baseline.log`、`freeze-diff.json`（全量串级差分；`freeze-diff-detail.txt` 仅为 P1 局部摘录）、`token-diff.txt`、`removed-strings-check.txt`
- `p8-compare.log/.json`、`p8-core-extract.log/.json`、`p8-ed-extract.log/.json`
- `regdump/dump.log` + `core-REG.json`、`regdump-ed/dump.log` + `ed-REG.json`（隔离 REG 展开）
- `occlusion-ed.log/.json`、`occlusion-core.log/.json`、`occlusion-new.log/.json`
- `scratch-ed.log`、`scratch-core.log`、`rightedge.txt`、`scans.log`、`gloss-p7-readers.txt`
- `freeze-baseline.log`（误用分版树跑 baseline 的 0/8 记录，仅作口径说明）
