# PROOF-NOTE — W47 fr-ko (法语核心 × 读者韩语) 独立复校 proof1（re-fanout #2 版）

- 复校员：独立复校（与构建者不同人），2026-11-11 17:40–18:10 EST
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-ko1/`
- 结论：**(a) 零缺陷，定稿** — 本版无缺陷。另 2 项记录（不计入本版缺陷）：1 项核心继承观察（Q130/Q36/Q37 孤儿填空行，首轮已存在，不修）、1 项全周级已知待定项（D5 字体，只记录）。
- 本轮是 re-fanout #2 版的 proof1。上一轮（#1 版，12:48–13:10）的结论与文件已封存于同目录 `prev-round-#1/`，本次全部数字均为针对 #2 新版的独立重测，不采信上一轮或构建方数字。
- 生产文件只读：复校期间未改任何生产文件，未 commit、未 push。确定性重建在 scratch 副本中进行（副本已删，哈希记录在 GATE-LOG 与 `rebuild/shipped-svg.sha256`、`rebuild/rebuilt-svg.sha256`）。`git status` 上该版目录与 core-fr 均为未提交新目录（builder 工作状态，复校未动）；复校前后生产 SVG 哈希复测一致。

## 身份核对（开工前实测，与任务书完全一致；复校结束再次复测，未变）

| 文件 | 字节 | SHA-256（开工前 = 结束后） |
|---|---|---|
| `La-Lucerna-VOL4-fr-ko.pdf`（印刷） | 23,103,425 | `a315cced01b3725d57e17ca5b57015372b4bf2555392033cae618dd38faf3c82` |
| `La-Lucerna-VOL4-fr-ko-web.pdf`（网页） | 2,048,869 | `0862b544eb337d4061cf762a9f40932ae40fc5d0107cfd9bac2bb31e4349ebd5` |
| `2026-w47-fr-ko.text.md` | 47,323 | `f5474d61eeadf9fdb2fe6a5fb3e2e15ff9088201aa8989e986ed064f46ba5c37` |

核心 core-fr fix4 对照（盘上实测，复核前后各测一次，未变）：

| 文件 | 字节 | SHA-256（复核前 = 复核后） |
|---|---|---|
| `La-Lucerna-VOL4.pdf`（印刷） | 30,446,975 | `a30af667b25929984c34cf2af621c0b15a3072f4db55a14e507d3682ace25a9d` |
| `La-Lucerna-VOL4-web.pdf`（网页） | 2,241,835 | `56f50ca8ab7ec912408bb4eda77c5a1a36eb7cc2639f09400584a6166d58e141` |
| `2026-w47-fr-zh-cn.text.md` | 46,471 | `52024e024d32ca22c32287c7954d05e2bae9480dd75448b65169bb4899d063df` |

与 FANOUT-REPORT-fr2.md §1 / §4 一致：本版 P8 SVG 哈希 `fc7999be…`（#1 的 `b533645f` → #2 的 `fc7999be`），P1–P7 哈希与 #1 相同（重建 8/8 字节一致，见 GATE-LOG）。

## 缺陷清单

**零项。** 本版无 ko 引入缺陷。

## re-fanout #2 复核点（逐项独立重测，全部存活）

- **P7 披露框 2 行**：P7 右下 `LE COURRIER DES LECTEURS　독자 편지` 奶油盒（`p7-langue.svg`：`x=989.0 y=1878.0 w=873.0 h=380`，盒底 `y=2258.0`）。内容 `courier_disclosure` 韩文段 2 行（基线 2206.0 / 2233.3）：“편집부 알림: 마감 시점에 VOL.4 투고가 도착하지 않아, 명시한 편집부 예문을 싣는다. VOL.5에서 실제 투고 평론 약속을 지킨다.”
  - 自测（非采信构建方/上一轮数字）：
    - creambox PIL 真墨扫描（`boxtitle_creambox.py` → `boxtitle-creambox-proof2.log`）：该盒末基线 2233.3，真墨底 2235.1，清除 **+22.9**。
    - 交付印刷 PDF 300 dpi 渲染像素（`p7_measure2.py`）：末行真墨最后一行 svg y **2234.4**（x 1021.3..1202.1）；2234.4 至 2269.6 之间零墨（35.2px 干净白纸）；深绿带绘图实测起于 svg y=2270.0（`get_drawings` fill (0.216, 0.251, 0.184)，x 989.0..1862.0）。真墨清除 **+23.6px**。300 dpi 裁切（`png/p7-box-crop.png`）目视：两行韩文完整在奶油内，盒底奶油边干净，字形无一触边，绿带未被侵入。
    - 附注：`p7_measure.py` 旧版写法用 `yb±80px` 窗口取“末墨行”，会把 2270 起的绿带顶行误算为 2283.1（清除 −25.1）——这是测量窗口 artifact，不是版面问题；以 `p7_measure2.py` 的逐行扫描（2234.4 末墨行 + 35.2px 零墨间隙 + 绿带 2270.0 起）为准。结论：**干净，无溢出。**
- **Q148**：三重验证全部通过——`content8.py:170` 键 `"devant le"`；`:176` 题干 `On se retrouve ({gnums[3]})___ cinéma ?`（无 `du`）；P8 SVG 文本层含 `On se retrouve` + `cinéma ?` 且不含 `du cinéma`；`p8.py extract` 提取键 148 = `devant le`，与核心 `final-fr-p8.json` 148 = `devant le` 一致。P8 目视（`png/p8.png`）：对话区 `(148)___ cinéma ?`、答案区 `148. devant le（영화관 앞）` 均正确。填入后 “On se retrouve devant le cinéma ?” 语法正确——#1 的 R1 缺陷已由核心 fix4 修复落地。
- **Q130**：P8 填空线 `(989.0, 843.0)`，与核心分毫不差（`check_extra2.py`：core 与 ko 的 blank lines 完全相同）。
- **Q36/Q37**：P3 x=538.5，y=1864.7 / 1997.4，与核心分毫不差，属 **+0 档**（ja/ko/zh-tw 档），与任务书预期一致。
- **keydiff**：实测 `[150]`（`p8compare-proof2.json`，CLEAN）。Q137–139 翻译键与核心逐字相同（`q150-handcheck.txt`：Q137 `Nous suivons le vote du Sénat depuis lundi.`、Q138 `Ce soir, nous allons préparer nos affaires.`、Q139 `On ne connaît pas encore les résultats.`，core 键相同）；仅 Q150 写作键为读者语（`자유 작문` vs 核心 `开放题`，设计内差异）。
- **孤儿扫描**：`check_extra2.py`（同基线判定版，已在 ru/ja 旧版上验证过检出能力）：15 个标点元素，**新增 0**；核心继承 2（P4 y=623.13 与 P6 y=653.69 的行首 `—`，x=1007.0）；同基线 13（字体分拆的行末标点 `.` / `——` / `）`，均与同行实词共享基线 |Δy|<1.5，非视觉孤儿）；记录残留 0。逐项清单见 `ko/extra-proof2.json`。
- **P8 哈希封闭性**：仅 P8 相对 #1 变化（`fc7999be`），改动 = Q148 键/题干两处，无多余改动（与 FANOUT-REPORT-fr2.md §4 一致）。

## 韩语读者版特别核查（逐项手验）

- **expl.py 全文通读**（318 条，`expl.py`）：韩文拼写正确；指示语一律用敬语 `-(으)세요`（`완성하세요`、`고쳐 쓰세요`、`채우세요`、`읽고 정답을 고르세요`、`보내세요` 等）；无片假名/平假名混用——SVG 全量扫描：假名 0 个；新增汉字 0 个（freeze diff + `cjk_inventory.py`：新增 CJK 2,564 字 = 谚文音节 2,538 + U+3000 结构空格 17 + 『』4 对，**未入账 0**）；无中文残留——版内全部汉字仅品牌三色蛾 `三色蛾` 3 字（刊头蛾标，与核心同一字节来源，非中文讲解残留）。
- **“next Sunday”**：`Sunday` 在 fr-ko 全目录（py/md/svg）0 命中，不触发。
- 未使用的 E 键（观察，非缺陷）：`m_gerbe` / `m_flamme` / `m_musee` / `m_vernissage` / `m_tirage` / `m_galerie` / `m_vernissage2` / `m_legende2` 在 content*.py 中无任何引用（仅 `m_tirage3` 被 `content34.py:143` 引用），不印出版面；核心 expl.py 亦有同样 8 条（`tirage=印制` 与 ko 的 `tirage=인화` 义同），属核心继承的未使用键，不动。

## 150 题逐题手验（题干 vs 核心 0 差异，键 vs 键 0 差异，键-题干契合手验）

- 机制：`content12/34/56/7/8.py`、`bslib4.py`、`svglib.py`、`run.py` 与核心**字节相同**（source_freeze 门），故全部法语题干即核心题干；string_freeze 门逐页验证全部非 CJK 核心串在版内逐字存活（0 缺失、0 核心 E 残留、0 未入账 CJK）。手验表 `q150-handcheck.txt`（题干取自 `.text.md` 阅读顺序导出 + P8 提取键 + 核心登记键三列）。
- 逐题读完 Q1–Q150：键-题干契合全部成立。抽样关键项：Q5 `12,7`（正文 21,8→12,7）；Q42 `13` août（正文 dès le 13 août）；Q48 `vendredi 20`（Ligue 1 20–22 日复出）；Q60 Bordeaux / Q61 Milan（与正文城市一致）；Q113 `propose`（主语 Le cinéma 单数）；Q114 `aimé`（avoir + 过去分词无配合）；Q120 `irais`（si + 未完成过去时 → 条件式）；Q130–139 完成句全部与题干提示的语法点一致；配对题 5 组（Q22–25、Q49–52、Q73–76、Q85–88、Q140–144）逐组核对词与释义的对应全部正确；对话 Q145–149（`des billets` / `deux` / `quelle heure` / `devant le` / `film`）填入后对话通顺；Q150 为设计内写作键差异（见上）。
- P8 印出键 vs 登记键：三重交叉（`triple_check.py` → `triple-check.json`）——text.md 答案 150/150 解析、0 缺失；仅 Q150 一处差异（设计内）。其余 149 题印出键 = 登记键 = 核心键。

## 全页目视（P1–P8 印刷 PDF 110 dpi，`png/p1.png`–`p8.png`；网 P1/P7 另验）

- P1：刊头、头条、Atget 照片+图注、QUIZ ÉCLAIR、页脚全部干净。照片内小白方块与核心 P1 嵌入图逐字节相同（base64 SHA 前 12 位 `ff20bc2bd265` 两边一致）——是 Atget 原片里的店招，非本版缺陷。
- P2：ET VOUS 盒最末韩文行在盒内（紧点见下）；DIRE LA DATE 表、Q11–25 均正常。
- P3：Q36/Q37 孤儿填空线可见（核心继承观察项，不修）；其余正常。
- P4：Q44–61、配对、MICRO-DRILLS 均正常；P4 `—` 孤儿元素 2 处均为行内标点，非视觉孤儿。
- P5：Q62–78、Méliès 图、词表均正常；Q64 选项 B `Lukas Dhont` 与正文一致。
- P6：日历表、Q79–96 均正常；`comparatif` 练习与括号提示一致。
- P7：奶油盒 2 行披露完整在内（见上）；Doré 插图+出处、CLINIQUE Q105–108、绿带 `LA SEMAINE PROCHAINE` 均正常。
- P8：Q109–150、答案区、Hiroshige 图均正常；Q148 对话与答案、`148. devant le` 正确；Q130 孤儿填空线为核心继承观察。
- 网 PDF：P1/P7 渲染（`png/web-p1.png`、`web-p7.png`）与印刷版同一版式、无豆腐块；文字层与印刷版逐字节一致（102,735 B，见 GATE-LOG）。

## 最紧的两处（均已用交付 PDF 渲染像素复核，非仅卡片测量）

- **P2 ET VOUS 盒**（`p2-vie.svg` 盒 y=973.6，底 1308.6，x 1439.5..1862.0）：SVG PIL 真墨底 1306.2，清除 +2.4px；交付 PDF 300 dpi 行扫描：末墨行 svg y 1305.5，其后至 1320 零墨，渲染清除 **+3.1px**；裁切目视（`png/p2-tightbox-crop.png`）末行 `어로 두 문장을 써서 보내세요.` 完整在奶油内。注：span em 框底为 1309.9（略超盒底 1.3px）——那是字框度量，不是墨；真墨在内，故不判溢出。**通过，偏紧但干净。**
- **P7 披露盒**：见上，清除 +23.6px（渲染像素），通过，余量充足。

## 记录项（不计入本版 (a) 判定）

### R1 — Q130 / Q36 / Q37 孤儿填空线（核心继承观察类，首轮已存在，不修版、不动核心）

- Q130：P8 `(989.0, 843.0)`，`Futur proche : « Le Sénat vote mercredi. » →` 后填空线独行；Q36/Q37：P3 x=538.5，y=1864.7 / 1997.4，`(pas)` 改写句的填空线独行。三处与核心坐标分毫不差（ko 为 +0 档），属核心版式继承，按任务书列为观察类，不修。

### R2 — D5 字体（全周级已知待定项，如实记录，不判 (b)、不擅自修）

- ET 全量普查（8 页全部 1,804 个 `<text>` 元素，精确分类；分类口径：含 CJK 字母或 U+3000–303F/全角符号者计“含 CJK”——与上一轮口径一致，数字可对上）：
  - ko 版：`Newsreader` 983 段、`Noto Sans CJK SC` 661 段、`Noto Serif CJK SC` 155 段、`DejaVu Sans` 4 段（P7 ✗ 标记，合理）、`UnifrakturMaguntia` 1 段（刊头黑体）。
  - CJK 字体段共 816：含 CJK 452 段、纯拉丁字母 222 段、纯数字/标点 125 段、纯标点/空格 17 段（其中仅含 CJK 字母者 366 段，其余 86 段为 U+3000 结构空格/全角符号）。
  - 核心对照：CJK 字体段共 775（414 / 219 / 125 / 17）。ko 版仅比核心多 41 段（+38 含 CJK、+3 纯拉丁）——即 D5 现象基本是核心继承的常量，ko 讲解层新增极小。（注：上一轮记核心为 776/415，本次 ET 全量重数为 775/414，差 1 段为计数口径所致；本文以本次实测为准。）
- 按任务书指示：仅记录实测段数，待用户定夺 scope。

### R3 — 任务书所称冻结英文 “next Sunday”（核查说明，非缺陷）

- 盘上实测：fr-ko 全目录 `Sunday` 出现 0 次；`content12.py:37/:113`、`content34.py:127` 现为法文头条与词条行，不含该英文串。结论：本版内不存在该英文串，无可裁定的内容；行号与盘上现状不符，已如实记录（可能为旧版行号）。不影响 (a) 判定。
