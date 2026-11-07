# W45 EN×JA 独立校对报告

**校对对象**：`files/weekly-report-w45-en-ja/`（SVG×8、卡片×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
**核心对照**：`files/weekly-report-w45-en-core/`（VOL.2，刊头 The Lucerna）
**构建树**：`hidden_files/weekly-report-w45-en-ja-build/`（只读使用，未修改）
**结论：ZERO PROBLEMS**（阻塞项 0；非阻塞观察 5 项，见末节，均不影响内容与几何正确性）
**未做事项**：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录、未派生下级代理。

## 0. 开工查重与哈希锁定

- 开工前 `files/weekly-report-w45-en-ja/` 与构建树无进行中写盘（唯一运行进程属于 EN×IT 分版，与本版无关）；120 秒复查零新写盘后开工。
- 校对前记录交付物与核心全部 sha256（`pre-delivery.sha256`、`pre-core.sha256`）；校对后复核：**交付物与核心 sha256 前后全等，无一变动**（`post-*.sha256`，`sha256sum -c` 全 OK）。
- 交付物实测：印刷 PDF 31,114,365 B，sha256 `943448ee5aff62bb8250546164afe0e606b1a2b92675fdc3e7f1cade55a99cac`；网页 PDF 3,943,144 B，sha256 `995de98a686023da7dcbb1e5704e5f2ae8c3dd461522f84a7850e0c63bae5478`；与任务单/KIT 一致。双 PDF 各 8 页（印刷页框 1462.5×2025 pt，网页页框 1400×1938）；8 卡片均为 1950×2700 RGB。

## 1. 冻结（通过）

- `freeze.py baseline`（核心构建树 `hidden_files/weekly-report-w45-en-build`）：**8/8 SVG 逐字节复现**，且工具自检核心在运行前后未动（`check1-freeze.log`、`freeze-baseline.json`）。
- `freeze.py diff`：新增 CJK 逐页 = P1 211 / P2 243 / P3 145 / P4 171 / P5 159 / P6 172 / P7 440 / P8 741，合计 **2,282**，与 KIT 一致；新增字符全部落在日语讲解层（见 `freeze-diff.json`、`char-multiset-diff.txt`）。
- 字符多重集残差逐项闭合，移除侧非讲解项 = 0：
  - 移除的全部拉丁大写字母 = P1 strapline `THE LEARNERS' WEEKLY — REAL LIFE, IN ENGLISH, FROM AMERICA`（1 次，含撇号/逗号）+ 页脚英文尾 `LUCERNA ENGLISH WEEKLY`（8 页）；保留的 `The Lucerna · VOL.2` 部分恰好解释反向差额；`/` ×8 = 8 页旧页码行 `第 N 版 / 共 8 版`（家具替换）。
  - P1 徽章替换（W43 同配对先例，见 §8）、P8 半角括号式（`(` / `)` 各 +78，见 §3）、日语串内 ASCII 数字与分隔符、答案区换行重排（P3 `A2 →` / `B1`、P8 答案行重断行，词面本身未变）、P7 独立 `。` ×3 为中文讲解句重断行 artifact（字符层面 `。` 净 +6，无日语 `。` 丢失）。
  - 移除侧纯英文串除上述家具外无一例外；P8 纯英文移除串均有词面相同的重断行对应串。
- 违禁词全量：SVG 文本 + KIT + ABSTRACT 中 `桥接`、`讲解`、`译注` 均为 **0**；讲解层全部日语（`check-cjk.py`：未映射 CJK 常量 0）。

## 2. 日语专项（通过）

- 行首禁则独立扫描：本版 **6 处**，核心同口径 **12 处**，均复现（`check3-geometry-gloss.log`、`linestart-coords.txt`）。
  - 其中 5 处与核心**同页同坐标同串**（P2 `: costumes…`、P5 `: what…` 与 `: MLS…`、P8 `? — Yes…` 与 `, in the results…`），确为冻结英文换行继承。
  - 第 6 处（P8 `) · 147. ballot…`，y=1875.5）见非阻塞观察 O2：同页同栏同类注括号换行，非日语行。
  - **日语行 0**：6 处行首行无一为日语句（5 处纯英文，1 处为英文答案流 + 日语注）。
- 中文残留词级复查（`chinese-residual.txt`、`chinese-w43.txt`）：
  - 简体专属字（语/说/这/让/为/电话/车门/见/观/龙/汉/仅/发/对/马/风/云/买卖/读 等）**0**；真中文专属词（但是/因为/所以/如果/已经/正在/可以/需要/觉得/知道/这个/那个/我们/你们/他们/什么/怎么/为什么/时候/地方/东西/问题 等）**0**。
  - 仅有的中文功能字形均在日语复合词内（現在、終了、有権者、不規則、都合、要点、会話、比較），非中文用法。
  - 共享汉字词逐词裁定为正明日语：生活/文化/体育/青年（栏目标题）、怪物（`a monster 怪物`）、原文（`原文に戻って読む`、`原文：a teacher from Ohio`）、原形（`動詞の原形` 及 P8 多处注）、投票率（`turnout = 投票率`）、地図（`（選挙の）地図`、`一枚の地図`）、得点（`誰が得点したか`）。
- svglib 规范：构建树 `svglib.py` 与 W43 EN×JA 规范文件 md5 均为 **`d73e23b365676c3618d7e060b835eb4d`**，实测一致，规范文件未编辑。

## 3. P8（通过）

- 独立确立计数口径：`p8.py extract` 直接对**核心 P8 SVG**实测 = **78 项**（非采信固化值），与 `transform.py` 的 PRINT_NOTES 78 项一致；本版实测亦 78 项，集合逐项相等。
- `p8.py compare`（显式双路径形式）：**CLEAN 78=78，missing=[]、extra=0，keydiff=[137, 138, 139, 140, 150]**（`check2-p8-occlusion.log`、`p8-compare.json`）。
- keydiff 逐项印刷行对照（`p8-stems.txt`）：
  - 137：题面 `Translate : « Patience is part of the system, not a failure of it. »` 英文冻结，键中→日（忍耐は制度の一部であり、制度の失敗ではない。）——EN→JA 翻译题，合法。
  - 138：题面英文句与核心**逐字节相同**（`Tuesday, November 3, is Election Day in the United States.`），仅指令词由 `翻译：` 本地化为 `翻訳：`，键为日语译文（11月3日火曜日はアメリカの選挙日です。）——合法（措辞澄清见 O3）。
  - 139：同 138 机制（`On Sunday, the NFL plays in Madrid.` 英文冻结，键：今週の日曜日、NFLはマドリードで試合をします。）——合法。
  - 140：题面 `Translate : « Not every place changes. »` 英文冻结，键日语译文（すべての場所が時計を戻すわけではない。）——合法。
  - 150：写作装置项，键日语化（自由記述 — 要点は作文の枠内、模範文は8ページの作文枠の中），注“要点ごとに採点”——合法。
  - 其余 145 键与核心逐字节全等。
- P8 注释：注内日语化完成，无中文（P8 单独扫描简体专属字 0、`桥接`/`讲解` 0）；注中英文 token 均为答案本身的键/锚词（如 Election Day、on Tuesday），与核心注的英文锚词模式一致（见 O5）。P8 印刷笔记集合相等， verdict 为 CLEAN（非 EXTRA_ONLY）。

## 4. 几何（通过）

- `occlusion_audit.py` 自检先行通过（6 类 planted flags 全触发，clean 对照静默）；本版 **0 / 核心 0 / NEW 0**（`occlusion-edition.json`、`occlusion-core.json`）。
- 同行墨迹扫描（`rowcheck.py`）：本版 **0 碰撞**，核心对照亦 0。
- P6 图表标签覆盖（`chartcheck.py`，PIL getmetrics、anchor ls 基线锚定）：4 标签墨迹盒全部实测，最大覆盖 **0.0%**（门限 <30%）。
- 框线压框：全 8 页 occlusion 0 旗（含 BOXTITLE/LINEX/COVER 类），即压框 0。
- 右缘扫描（ADVANCE 法）：本版仅剩 **2 处**，与核心**同页同坐标同串**（P8 y=806.4 edge=1899.4 `b. an election in the middle of a term`；P8 y=882.4 edge=1903.8 `d. the paper you mark your choice on`），均在 1950 页内，墨迹审计 0 旗——核心继承，非本版缺陷。
- 首轮消除验证：首轮 `occlusion-round1.json` 的 5 NEW 旗（P1 热搜副题出页 + 压框、P3 在家框题出框 + 连带 TEXTX、P4 周日框题出框）在终态全部消除；首轮右缘新增 P1 相对热度注 1946.7 在终轮右缘输出中**不存在**。
- 第二轮变化范围验证：首轮基线（`baseline-round1-edition.sha256`、`baseline-round1-cards-pdfs.sha256`）与终态对照——SVG 变化仅 p1/p3/p4，其余五页 SVG 全等；卡片变化仅 p1/p3/p4，其余五页卡片 sha256 与首轮全等。PDF 字节变化属合并重建所致：从终态 SVG 用 `render.py` 在 scratch 复现，印刷 PDF **逐字节相同**（sha256 一致）；网页 PDF 8 页内嵌 JPEG 字节逐页全等、总字节相同，仅 CreationDate/ModDate 时间戳不同（内容等价）。

## 5. gloss（通过，独立实测）

- 不照搬构建员数字：独立解析核心构建树与分版构建树的 `gloss()` 调用串，按 `·` 拆分逐项计数（`gloss_count.py` 实测 + AST 按文件复核）：
  - 核心：content12（P2）3、content34（P3）4 +（P4）4、content56（P5）3 +（P6）4，合计 18。
  - 本版：同分布 3 / 4 / 4 / 3 / 4，合计 **18 = 18，1:1**。
- P1 bridge 串另计（非 gloss 门）：核心与本版均为 4 项（midterm / ballot / race / to call a race），前缀由 `讲解｜` 换为 `解説 —`，内容对应。

## 6. P7（通过）

- 定义句逐字保留：P7 去 CJK 后的英文 token 流对照，全部差异仅为讲解层标点/分隔符/日语内数字（`｜`→`—`、`，`→`、`、`……`→`〜`、工具箱日语句内 `3`/`1` 等）与家具（页脚/页码），**无任何英文定义词改动**，定义句本地化 **0 处**；B2 例句框 gloss 片段 `part of = 一部` 的本地化不改动英语原句（核心为 `一部分`，属讲解层）。
- 金句 8 句：原文逐字 + `(page N)` 标签与核心全等（page 1/2/3/4/5/6/2/4）；全文归一化裸句计数核心 = 本版：**3 / 2 / 2 / 2 / 2 / 4 / 3 / 2**（`p7_check.py`、`p7-check.log`）。
- P7 结构语言归属与核心一致：三级专栏（英语定义句/例句 + 日语栏目标题 基礎/中級/上級）、金句区（英语原文 + 日语 `文法ポイント —` + 日语题型 `音読ドリル`）、易错诊所（英语错句 + 日语指令 `誤り直し`）、读者园地（英语信件 + 日语披露句，见 §7）、VOL.3 预告（英语预告句 + 日语预告行）。

## 7. 读者园地（通过，含一处计数订正，见 O1）

- 英语信件逐字冻结：`« On Sunday, I slept one hour more — and I still woke up late ! » — M. L., a reader in Chicago (editor's example : no real reader letters had arrived when this issue went to press, so the example stays, honestly labeled)`，核心与本版同坐标逐字节相同；标注与 VOL.3 预告英语句亦逐字相同；**零编造**（无新增读者/来信/姓名/引言），**未新写核心没有的英语披露句**。
- 日语披露句逐字摘录（P7 园地框 x=989..1885，框底 y=2178，`readers-corner.txt`）：
  > 編集部より｜VOL.1ではVOL.2に本物の読者の手紙を載せると約束しましたが、締め切りまでに本物の手紙も、VOL.1の作文投稿の最優秀作も届きませんでした。そこで本号は見本を見本と明示して載せ、約束はVOL.3へ先送りします。あなたの手紙と作文を送ってください。VOL.3に届いた本物の手紙を載せます。
- 逐项核实：事实 1 无真实来信 ✓、事实 2 无 VOL.1 作文投稿最優秀作 ✓、事实 3 示例 + 承诺顺延 VOL.3 ✓；显性日语征集邀请：祈使句 `送ってください` + VOL.3 刊登承诺 `VOL.3に届いた本物の手紙を載せます`，邀请句独立在披露句内（内容预告行 y=2420 不算邀请，未计入）✓。
- 框内无溢出实测：披露句渲染为 **4 行**（y=2076 / 2104 / 2132 / 2160），末行墨迹底（occlusion 口径：2160 − 上升 23.25 + 下延 25.5 = **2162.3**）< 框底 **2178**，余量约 15.7；且 occlusion 全版 0 旗。行数与末行数值的订正见 O1，内容与几何均通过。
- 最佳 P8 作文覆盖范围裁定：披露句的 `VOL.1の作文投稿の最優秀作` 指 **VOL.1 那一期的 P8 写作投稿中的最优秀作**（与核心中文 `VOL.1 写作投稿` 同范围）；VOL.2 为当期，其作文尚未评出，故“无最佳作”陈述与事实范围一致，无编造。

## 8. 家具与 W43 偏差清单（通过）

- 印刷笔记集 78 vs W43 62：口径已实测——W45 核心 P8 实测 78（本版 CLEAN 对应），W43 EN×JA P8 用 total=149（VOL.1 总题 149，非 150）实测 **62**，两数各为当期核心实测值，非照搬；差异源于两期总题与注规则不同。
- keydiff 5 vs 3：W45 的 5 项 = 翻译题 4 项（137–140）+ 写作装置项 150（§3 逐项合法）；W43 的 3 项为其当期翻译 2 项 + 写作 1 项（机制同类，数量随当期翻译题数而异）。
- 园地披露句文案差异：W45 核心情境为 VOL.1 承诺落空（无来信 + 无最佳作文，顺延 VOL.3），与核心中文披露句逐句对应；W43 为 VOL.2 承诺情境，两期事实不同，文案不同属实。
- 4 处缩短日语标题（KIT §10 误写“三处”，见 O4）：P1 热搜副题 `今週の急上昇 · Google Trends`、P1 相对热度注 `人気の目安で、正確な検索数ではありません。`、P3 在家框题 `AT HOME THIS WEEK · おうち時間`、P4 周日赛程框题 `SUNDAY, NOVEMBER 8 · 日曜の試合`——4 项均在终态 SVG 内且 occlusion 0 旗（在框验证：P1 卡片目视副题与注均在搜索框内，P3/P4 卡片目视框题均在框内）；4 项均在 `transform.py` 值映射中（行 45、46、67、71），非仅改 content 文件（W43 同类缩短先例成立）。
- 行首继承 6 vs W43 0：两期核心英文换行位置不同所致——W45 核心同口径 12 处（§2），本版继承其中 6 处（含 P8 注括号类），日语行两版皆 0。
- 其余家具与 W43 EN×JA 逐字一致（实测）：徽章 `英語テキスト · 日本語の解説 — 日本語読者のための版`（各 1 次）、页脚（除 VOL.1→VOL.2 期号外逐字同）、页码行 `N ページ（全 8 ページ）`、gloss 前缀 `解説 — `（各 7 次）、语法前缀 `文法ポイント — `（各 8 次）、P8 分隔行 `— N ページ —`、P8 半角括号式（W43 样例与本版同式）、题型/指令映射标签（空所補充/書きかえ/選択肢/組み合わせ/会話補完/翻訳/誤り直し 等映射关系一致；出现次数差异属两期题目构成不同，非家具漂移）、svglib 规范版 md5 同（§2）。

## 9. 图片、题量、卡片目视（通过）

- 图片载荷逐页相等：每页 `<image>` 数与 href sha256 核心 = 本版（P1/P2/P3/P4/P6 各 1 张，P5/P7/P8 无图，`images-compare.txt`）；署名在版且与核心逐字相同（P1 Kenneth C. Zirkel — CC0、P2 Public domain、P3 Édouard Manet — CC0、P4 Frank R. Snyder — public domain、P6 Public domain，均 via Wikimedia Commons）。
- ABSTRACT.txt：日语**单行**、无 ASCII 双引号；含刊名 The Lucerna、目标语名 英語、A2–B2、150問；真实主题关键词（11月3日の中間選挙の投票日、11月1日の時計を戻す日、ハロウィーン、The Cat in the Hat、Godzilla Minus Zero、NFLマドリード戦）与学习者搜索短语（英語の記事で読み、日本語の解説で学ぶ、英語学習者向け週刊紙）。
- 8 卡片全部逐页目视通过（P1–P8）：无溢出、无重叠、无压页脚、无图片与出处问题；P6 图表标签无覆盖（§4）；P1 搜索框、P3 在家框、P4 周日框、P7 园地框目视均在框内。
- 题量独立展开计数：分版构建树在 scratch 复现构建，SVG **8/8 逐字节复现** shipped SVG，注册表实测 **150 题，A2 60 / B1 69 / B2 21，页分布 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39**；题型分布与 KIT 一致（文の完成 33、選択 41、文型変換 16、語彙マッチング 20、グラフ読み取り 6、音読ドリル 8、誤り直し 4、穴埋め 8、読解 4、翻訳 4、会話補完 5、作文 1）；编号由 `len(REG)+1` 顺序追加，1–150 连续无缺重。
- 范文：`« My Tuesday, November 3 »` 模型文与核心逐字相同，空白分词 **85 词**（与核心一致；按词形计为 81 + 标点 token 4）。
- 构建日志：两轮均 **0 警告**，无 FLOW OVERFLOW / HEAD TOO WIDE。
- 解释器：`run.py` 与 `render.py` 均用 `tools/venv/bin/python`（实测 Python 3.12.3、PIL 13.0.0、cairosvg 2.9.1、pypdf 6.21.2）。

## 非阻塞观察（不构成阻塞项）

- **O1 — 披露句行数订正**：构建员/KIT 称披露句“3 行、末行 2132”，实测本版为 **4 行、末行基线 2160**（2132 为核心中文披露句的末行，核心披露句确为 3 行且末行含独立 `。`）。本版第 4 行 `届いた本物の手紙を載せます。` 为披露句末句的延续，内容完整；墨迹底 2162.3 < 框底 2178，几何通过。仅为文档计数 stale，不改结论。
- **O2 — 行首第 6 处坐标说明**：5/6 处为核心同坐标继承；第 6 处（P8 y=1875.5 `) · 147.…`）不在核心任一 `）` 行首行的坐标上（核心 P8 括号行首行在 y=2022.36 / 2344.76 / 2385.06 / 2465.66），而是 P8 答案区因半角括号式 + 日语注变长重排后、同栏（x=1451）同类注括号换行的新位置。类别与核心一致，非日语行，非新缺陷类；构建员“同位置”表述对该处不精确。
- **O3 — 138/139“改向”措辞澄清**：题面英文句与核心逐字节相同，并非题面改写；实际机制仅为指令词 `翻译：`→`翻訳：` 本地化 + 键本地化为日语译文。机制合法，KIT §7“题面改向”一词易误读，建议后续改述为“指令词本地化”。
- **O4 — KIT §10 数字笔误**：§10 第 4 项写“三处日语标题”，但同项列出 4 项、§11 正确写“4 处缩短”；以 4 项实测为准（§8 已列）。
- **O5 — “P8 注释纯日语”的口径**：P8 注中含英文键/锚词（如 `Election Day`、`on Tuesday`），属答案内容本身，与核心注模式一致；注的讲解部分为日语、无中文。口径上应理解为“注的讲解层纯日语”，而非“注内无任何英文 token”。

## 证据文件（本报告目录 `hidden_files/w45/en-ja-proof/`）

`REPORT.md`（本文件）、`pre-delivery.sha256`、`pre-core.sha256`、`post-delivery.sha256`、`post-core.sha256`、`check1-freeze.log`、`freeze-baseline.json`、`freeze-diff.json`、`char-multiset-diff.txt`、`freeze-removed-noncjk.txt`、`freeze-added-noncjk.txt`、`check2-p8-occlusion.log`、`p8-core.json`、`p8-edition.json`、`p8-compare.json`、`p8-w43.json`、`p8-w43.log`、`p8-stems.txt`、`occlusion-edition.json`、`occlusion-core.json`、`check3-geometry-gloss.log`、`linestart-coords.txt`、`linestart_coords.py`、`p7-check.log`、`p7_check.py`、`p7-core-lines.txt`、`p7-ed-lines.txt`、`readers-corner.txt`、`chinese-residual.txt`、`chinese-w43.txt`、`w43-types.txt`、`images-compare.txt`、`repro.log`、`repro/`（复现 SVG 8/8 字节等同）、`pdfrepro/`（印刷 PDF 逐字节复现；网页 PDF 内容等同仅时间戳异）、`freeze-baseline-scratch/`。

**结论重申：ZERO PROBLEMS。未宣布上架（上架由主线串行执行）。**
