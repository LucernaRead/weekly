# PROOF-NOTE — 2026-W47 it-ko 独立复校（re-proof，重扩散 2 后全量重校）

**结论：(a) 零缺陷，可定稿。满轮全量校对零问题；下列 11 项为观察项，不计缺陷。**

- 版：`2026-w47-it-ko`（目标语 Italiano × 读者母语 한국어，VOL.4；core D-2 fix 后重扩散 2 的新版）
- 复校员：reproof（独立于重扩散员与 proof2，从头全量，不抄前人结论；每项均独立重测）
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-ko/`
- 日期：2026-11-11（America/Toronto）
- 已读：`~/workspace/weekly-git/SOP.md` §8、§1.1 全文；`scratch-refanout-it2/FANOUT-REPORT-it2.md` 全文；`scratch-proof2-it-ko1/PROOF-NOTE.md`；`scratch-fix-core-it-d2/FIX-LOG.md`。
- 生产文件：未改任何生产文件，未 commit、未 push；KIT 未碰。

## 1. 开工盘核（三 SHA 与任务值逐字节一致；收工复核仍一致）

| 文件 | 大小 (B) | SHA-256（盘上实测，开工与收工两次一致） | 任务值 |
|---|---|---|---|
| 印 PDF `La-Lucerna-VOL4-KO.pdf` | 19,296,892 | `3125d4f36667155d5f10eb3522364513ba31bee72a4445f1e5ac90d74b28f87f` | 一致 |
| 网 PDF `La-Lucerna-VOL4-KO-web.pdf` | 1,607,467 | `67bda0ac5dfd57c6dce140bc021e420044888d11c63dcb25426bb2e95becfef8` | 一致 |
| `2026-w47-it-ko.text.md` | 57,326 | `d4d0c6c1a0048b9f2fa3248c0b5868058a3599bf75d253188301f3ad0a5a8fa1` | 一致 |

开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；scratch 真实写文件通过（`probe.txt`）。TMPDIR 全程指向 scratch 下 `tmp/`，未写系统 /tmp。解释器全程 `~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0）。

## 2. 回归项 A — D-2 修正逐项独立重测（全部通过）

| 检查 | 实测 |
|---|---|
| 新串在 text.md:775/:777 | 两行逐字在位（:775 `…Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`；:777 `…Il verbo è leggere, regolare al futuro: leggerò.`） |
| 新串在 content7.py:17/:18 | 两行逐字在位 |
| 新串在 p7 SVG | 换行碎片在位：`'Atalanta–Inter. Le forme sono regolari:'`、`'assaggerò, guardare '`、`'verbo è leggere, regolare al futuro: leggerò.'`（整句被换行拆成节点，故整串 grep 为 0 是换行所致，非缺失） |
| 新串在印/网 PDF P7 文字层 | 各 ×1（PyMuPDF 自然词序 + 箭头归一化 `\s*→\s*`→`→`；直接 `get_text()` 换行断句查不到是提取口径问题，词序拼接后 ×1） |
| 旧串 `Le forme sono regolari: andare` | content7.py / text.md / p7 SVG / 两 PDF P7 文字层 均为 0；全版 live 文件 grep 仅 `WEEKLY-KIT.md:98` 一处引用——为 KIT 历史披露行（引述旧串作变更记录），非正文 |
| 旧串 `irregolare al futuro: leggerò` | 同上，全版 live 文件 0（KIT:98 同行引用除外，同上） |
| 与重扩散前生产版 diff（`scratch-refanout-it2/backup/2026-w47-it-ko/`） | text.md diff 恰为 :775/:777 两行 replace，57,347 → 57,326 B（恰 −21）；SVG 仅 p7 不同（p1–p6/p8 逐字节一致）；cards 仅 p7 不同；content*.py 仅 content7.py:17/:18 两行；两 PDF 均变（P7 重建所致）；WEEKLY-KIT.md 亦变（§7/§8/新节文档更新，非内容）。另：备份两 PDF SHA 与修前历史值 `d5698327…` / `85722a84…` 逐字一致 |
| 词数旁证 | pdftotext 词数 7,411，proof2 旧版实测 7,414，差恰 −3（删去的 `andare`、`→`、`andrò,` 三词） |

## 3. 回归项 B — P7 教学段语义逐句事实核查（D-2 教训：读教学句本身）

- L17 新句：`Le forme sono regolari: assaggiare → assaggerò, guardare → guarderò.`——正确。assaggiare / guardare 均为规则 -are 动词，未来时 assaggerò / guarderò 恰为规则构形（不定式去尾 -e + -ò；assaggiare 的 -i- 脱落为规则音变）。andare 已不再被举为规则例。
- L18 新句：`Il verbo è leggere, regolare al futuro: leggerò.`——正确。leggere 未来时规则（leggerò = 规则构形）；其不规则处在远过去时 lessi 与过去分词 letto，不在未来时。
- 全版 `regolar` 仅出现在这两处（text.md grep = :775/:777 两行；content*.py grep = content7.py:17/:18 两行），无其他同类规则性断言。
- Q101–104 不受影响：Q101 题干 `(andare)` 为原形提示、键 andremo 无规则性断言；Q101–103 键 andremo / assaggeremo / guarderemo、Q104 键 B（leggerò）与三源核对一致（§5）。
- 桥接句 `미래형으로 계획을 말하기: andremo, assaggeremo, guarderemo, leggeremo.` 无规则性断言，四形拼写正确。

## 4. 缺陷

**无（0 项）。**

## 5. 门禁汇总（全部独立重跑，19/19 通过；详见 GATE-LOG.md）

| 门禁 | 实测 |
|---|---|
| run.py（scratch 副本，OUT 重定向） | RC=0，TOTAL 150，A2 47 / B1 70 / B2 33，页 10/18/18/18/18/18/12/38，0 FLOW OVERFLOW / 0 HEAD TOO WIDE / 0 NOSPACE；P7-a2 flow 末端 y=1124（改前 1157，短一行，底 1560——与 fix-core-it 一致）；P7 col3 末端 1673.0；P8-keys 流末 2499（底 2552）；P8-ex 流末 col 3 y=870 |
| SVG 重建 vs 生产 | 8/8 逐字节一致 |
| 印 PDF 重渲 vs 交付 | 逐字节相同，SHA `3125d4f3…` |
| 网 PDF 重建 | RC=0，1,607,467 B（与交付同字节），46,935 文字字节；文字层逐字节相同；二进制差异仅在字体子集流内（见观察 O6） |
| freeze baseline（核心 it 自身） | 8/8 逐字节一致；build-copy 核实确为核心版（与 core-it 仅 OUT 行不同；core content8/12/34 md5 与 KIT §11 一致：`629b5b0a…` / `91cdfbb9…` / `18926942…`；核心 p7 SHA `a7e6afa4…` = D-2 定稿值；核心 SVG 跑前后未变） |
| freeze diff（核心 → 本版） | P1–P7 0 未解释片段；P8 由 p8 compare + 150 键审计覆盖 |
| occlusion 几何遮挡审计 | 0 flags |
| p8 extract | noted 150/150 |
| p8 compare vs core | CLEAN，keydiff `[137, 138, 139]`（与 it 家预期一致） |
| 印/网文字层逐页比对 | 词多重集 8 页全同（pdftotext 7,411 词；PyMuPDF 6,651 词——两种分词口径，印网均一致）；词框位置比对（PyMuPDF，0.1pt 取整）P2–P8 0 差异；P1 仅刊头 “La Lucerna” 两词 x 差 0.4–0.5pt（见观察 O7） |
| P8 最小字号 | SVG 最小 13.0px；印 PDF 实测最小 9.75pt（520 spans）= SOP §1.1 下限 |
| §1.1 干净 | 纸 `#fbfaf6` 有；无金/红褐/近黑；VOL.4 ×9；VOL.5 仅 3 处合法节点（下周预告头、LETTERE 披露、P2 交叉引用，与核心同）；徽章色 A2/B1/B2 齐全；双线外框 0 个；字体 Newsreader / Noto Serif CJK KR / Noto Sans CJK KR / UnifrakturMaguntia；`·` 151 处全部在选项串或术语表内 |
| creambox（canonical） | 9 处 desc-clear 负值全部经交付 PDF 像素实测澄清（见 §6） |
| 横向溢出 PIL 真墨扫描 | 2,213 节点，3 处 +0.4~+0.5px 旗标，全部经交付 PDF 像素实测澄清（见 §6） |
| 盒标题横向溢出专项（STRADDLE） | 新旧 sweep 逐字相同；2 处越盒（见观察 O10），字形完整、无重叠、与备份像素一致——按 STRADDLE 规则为观察项 |
| text.md 校验 | forward-miss 0 / reverse-miss 0 |
| 150 键审计 vs 核心 text.md | 150/150，键一致（137–139 重定向、写作题除外）；notes 与 translations.py 一致（137–140 + 写作题除外）；9 条无表 notes 为冻结意大利语动词变位（16–20、60–61）与算术（85–86），逐字节照搬、无 CJK |
| 150 题三源逐题手验（登记 REG vs text.md 正文键 vs Risposte vs P8 印出键） | 150/150，0 差异（脚本 `threeway.py`；含键、note、级别、页码） |
| 8 金句 | 每句在本版与核心中各恰好出现 2 次（正文 + P7），逐字一致（见 §7）；第 9 个 «» 串 `Il governo propone` 计 3 次，系 P6 框 + Q88 + Q127 题干，非金句 |
| 日期/星期（`date -d`，Europe/Rome） | 20 个日期全验：11月16日周一…11月22日周日、11月23日周一、11月24日周二、12月2日周三、12月6日周日、12月31日周四、10月15日周四、10月28日周三、11月9日周一、11月12日周四、11月6–8日周五–周日、11月13–14日周五–周六，全部与正文星期表述一致（另验：VEN 20 周五、GIO 19 周四、MAR 17 周二均一致） |
| 算术 | 13−11=2（Q85）、6+7=13（Q86）、10 场比分逐场复加 = 24 球（与“ventiquattro gol in dieci partite”一致）、积分榜 29/28/27/24/23/5、TFF 11月24日–12月2日=9天、BookCity 11月23–29日=7天、Torrone 11月7–22日=16天·3个周末、BookCity 数字 1,360/2,487/1,164/443 与 Q70/73/80 一致，全部复算通过 |
| 全文通读（text.md 1,317 行）+ 8 页逐页目视交付印 PDF | 无拼写/语法/截断/事实错误；无溢出、重叠、压页脚、豆腐块；韩语讲解层无他语残留（可视 `<text>` 节点汉字/假名/西里尔 0 命中；仅有的 3 个汉字在 P1 兽蛾 logo 的非渲染 `<title>Lucerna 三色蛾</title>` 内，核心同款冻结家具，不可见） |
| 范文词数 | Testo modello 实测 99 词，与“99단어”标注一致 |
| ABSTRACT.txt | 一行韩语，421 B，无 ASCII 双引号 |
| 禁词扫描 | Ucraina/Russia/Putin 0 命中（正文+讲解层） |

## 6. 盒边与页边裁决（全部以交付 PDF 渲染像素为准，200 dpi，SCALE=2.0833）

### 6.1 奶油盒 desc-clear 负值（9 处）——全部澄清，非缺陷

canonical creambox 报 9 处 desc-clear 为负（−0.9~−1.5px，0.30em 保守系数），末行真墨逐盒像素实测（盒内 x 范围、末行基线至盒底+8px 窗口）：

| 盒 | 末行 | 盒底 | 末行真墨底 | 余量 |
|---|---|---|---|---|
| P2 LO SAPEVI? | della musica e dei musicisti. | 960.6 | 955.20 | +5.40 |
| P2 E TU? | 에 보내세요. | 1350.6 | 1346.40 | +4.20 |
| P3 IL WEEKEND DOLCE | continua fino al 6 dicembre. | 1021.1 | 1015.68 | +5.42 |
| P3 E TU? | 문장을 써서 보내세요. | 1290.6 | 1287.36 | +3.24 |
| P4 E TU? | 아어로 두 문장을 써서 보내세요. | 1140.4 | 1137.12 | +3.28 |
| P5 I GIOVANI IN NUMERI | domenica 22 novembre. | 1010.7 | 1005.60 | +5.10 |
| P5 E TU? | 장을 써서 보내세요. | 1249.8 | 1246.56 | +3.24 |
| P7 LA PAROLA | 치오가 29점으로 선두. | 1344.0 | 1340.64 | +3.36 |
| P7 LETTERE | 습니다. 약속은 VOL.5로 이어집니다. | 1673.0 | 1669.44 | +3.56 |

（单位：SVG px；真墨阈值灰度<200。）负 desc-clear 只是 0.30em 系数对无下行字母行（韩语无下行笔，意大利末行均无 p/q/g/y/j 下行字形）的保守高估；真墨全部留在盒内，最小余量 +3.24px。P7 工具盒汇总：3 盒，最小盒内 clearance +4.5，最小 desc-clear −1.5（上表 LA PAROLA，真墨余量 +3.36）。

其余 creambox 负 clearance 全部是 +45px 窗口的假阳性，inside-only 行自证清白：P1 三处（ADESSO TU +37.0、LA PAROLA DELLA SETTIMANA +24.0、QUIZ LAMPO 说明 +44.0，均为盒下块标题）、P3 一处（IL TORRAZZO +37.0，下块标题）、P4 三处（斑马表素行）、P6 两处（ESERCIZI 6면 연습 +42.0，下块标题）。各盒 inside-only clearance 均为正（+4.5~+90.0）。

### 6.2 横向页边（3 处 PIL 旗标 + 全页像素扫描）

- PIL 旗标 3 处（+0.4~+0.5px）：P1 “SETTIMANA DAL 16 AL 22 NOVEMBRE 2026”、P1 QUIZ LAMPO 说明、P8 “각 정답에 한국어 한 줄 설명 ✓ = 모범 답안 과제”。行级像素实测（行带窗口，不伸进 gutter）：真墨右缘分别为 1860.96（−1.04）、1856.16（−5.84）、1851.84（−10.16），全部在 1862 页边内——PIL advance 与渲染真墨之差，非溢出。
- 全页像素扫描：P1/P3/P4/P6/P7 最右真墨 1861.44（−0.56）；P2、P5 各有 11/7 行真墨越过 1862，均为 +0.88px、0 个实色像素（灰度<100 为 0，最浅 104），即抗锯齿毛边，非实墨（P2：副标 “Una festa, una giornata verde” 行顶；P5：Corot 图注行）。旧版与新版 P2/P5 整页渲染逐像素相同（差异像素 0），故非回归——与 proof2 的 +0.40px 之差为行带/阈值口径所致，0 实色像素的结论一致。最左真墨 87.36px 系 x=88 处 band 矩形/照片/徽章边缘的抗锯齿，非文本溢出。
- **P8 模型文两行独立行级实测**：‘Testo modello: Domenica 22 novembre metto la sciarpa e’（基线 635.56）与 ‘vado a Cremona: è l’ultimo giorno della Festa del Torrone’（基线 656.36）真墨右缘均为 1863.36，即越过 1862 内容边 **+1.36 SVG px（≈1.02pt）**。按两行各自基线对齐与核心重测：**核心同两行逐行相同**（右缘同为 1863.44 列、暗像素 34、实色像素 22；两行字符串、字号 12.0pt、x0=1079.62、x1=1398.34/1398.43 与核心逐字相同；仅基线 y 不同——ko y=635.56/656.36，核心 y=605.84/626.64，因 P8 上方练习流不同）。即该行为冻结核心固有、且核心已通过零问题复校；越边处为空白纸面，无裁切、无重叠、无碰撞，肉眼不可辨（边线本身不印刷）。故记**观察 O2，不计缺陷**。裁图：`out/crops/p8-model-right-edge.png`。（注：若用 ko 行带直接套核心页会得出 68 vs 9 的假差异——系行带 y 未对齐所致，已用各自基线对齐纠正。）

### 6.3 盒标题横向溢出专项（STRADDLE 规则）

判定标准（任务给定）：缺陷当且仅当字形被裁 / 墨水与另一元素或可见边框重叠 / 与备份旧版不同即回归；否则观察项。判定前已跑备份旧版对照。

- PIL 真墨 sweep（`sweep_box_titles.py`，复用 h-overflow 的 `node_ink`，覆盖全部奶油盒内各行）：新版 2 处旗标，旧版（备份）**逐字相同**（diff 空）：P1 cifre 标题 `LA SETTIMANA IN CIFRE　숫자로 보는 이번 주` inkR=1033.5，越盒右缘 961.0 计 +72.5px；P2 `LA FRASE PER RICORDARE　기억해 두세요` inkR=1005.5，越盒 +44.5px。另 1 处紧线：P1 `이번 주 일정　Cosa succede, giorno per giorno` inkR=1861.5，距页边 0.5px，盒内。
- 交付 PDF 像素实测：P1 cifre 标题真墨 x=558.7..1028.6，越盒 **+67.6px**，实色像素 12,313 个；P2 标题真墨 x=558.7..1004.2，越盒 **+43.2px**，实色 12,790 个；旧版备份 PDF 同区像素**逐值相同**（暗像素 15,310 / 15,090 一致）。越墨区 x=961..1030、y=1336..1362 内无任何 `<text>`、`<rect>`、`<image>`（SVG 全扫 0 命中），即溢出落在空白纸面（栏间白地），非重叠。
- 200 dpi 裁图目视：两标题末字（`주` / `요`）字形完整，无裁切（`out/crops/p1-cifre-title.png`、`p2-frase-title.png`）。
- 结论：两处均**非回归**（与 proof2 (a) 版像素一致）、**字形未裁**、**无元素/可见边框重叠**（奶油盒无边框）——按 STRADDLE 规则记**观察 O10，不计缺陷**。成因：韩语 gloss 比繁中版长（P1 `숫자로 보는 이번 주` 9 字 vs zh-tw `數字看本週` 5 字；zh-tw 同标题余量仅 +1.0px，ko 则越出 67.6px），为 it-ko 版固有版式特征。

## 7. 其他核实

- **keydiff**：实测 `[137, 138, 139]`，p8 compare verdict CLEAN，与 it 家预期一致。Q140 的键在核心与本版都是意大利语（“Ogni cifra deve essere chiara.”，韩→意翻译题），无差异是正确行为，不是遗漏。Q137–139 为 E 节重定向的读者句键（韩语句），符合 KIT §9。
- **标题数（实测，不用 “56 titles”）**：定义 = 字号 ≥26.5 SVG px（≈19.9pt）的非空标题文本节点。**原始节点 48、不同（页，基线）35**——与 proof2 的同口径实测逐字相同（48 / 35；proof2 另用 band 分列口径得 43）。三个口径均不复现 “56”——该数为幻数。
- **P4 斑马表**：10 场结果分 5 行，cream/none 交替，日标签每行重复；与核心 P4 同区一致——为核心冻结设计，非本版缺陷，渲染观感为规整斑马表。
- **P5 词表**：第二行以 ‘·’ 开头（“· indipendente · lettrice”），与 KIT §10 披露一致，核心同断点模式；视觉无重叠。
- **P1 无首字下沉、P3/P5 中段留白**：均为核心既有格局（KIT §10 已披露），本版与核心一致。
- **Q32 引号**：P8 答案 32. “Fate dolci” 用直引号，而正文（P3）与题干用 «Fate dolci»——translations.py ko 原值逐字如此，与 nl 版同源（KIT §10 已披露）。内容正确，仅引号样式与他版不同。
- **意大利语事实抽查**（核心冻结内容，复核一致）：Madonna della Salute 1630 年许愿、圣殿 1631–1687 年 Longhena 设计、植树节 1898 年起源/2013 年立法、Torrone 1441 年 10 月 25 日 Sforza–Visconti 婚礼、Eurochocolate 第 32 届、TFF 第 44 届（1982 创办，2026 年为第 44 届）、BookCity 第 15 届、Colson Whitehead 两届普利策、Sinner 为 2025 年 ATP 总决赛冠军；“Gattuso 执教 Lazio / Zverev 世界第一”为本期设定前提，核心已定稿。总分榜 29/28/27/24/23/5 与 10 场比分（24 球）自洽：那不勒斯–拉齐奥 1–1、国际–科莫 2–0、罗马–萨索洛 3–0 的比分在头条、P4 正文、积分榜、结果表、Q2/3/4/48/60/61 中六处一致。P2 25–28 匹配题 b/d 为已修复措辞（“il ponte di barche per la festa in novembre”、“la piccola luce di cera accesa in chiesa”），PIL 实测在页边内。
- **P7 金句页码**：8 句的 (Pagina N) 标注与正文所在页逐一核对：P1×2、P2、P3、P4、P5、P6×2，全部正确；金句本身逐字出自本期正文（各 ×2，见 §5）。
- **P8 评估卷复测属性**：Q113–149 多数为 P1–P7 内容的复测（如 Q113≈Q7、Q121≈Q47、Q134 与 Q44 同句），属 P8 综合评估的既定设计，非重复出题缺陷。
- **禁词扫描**：Ucraina/Russia/Putin 0 命中（正文+讲解层；继承核心）。

## 8. 观察项（不计缺陷，共 11 项）

| # | 位置 | 现象（源码行 + 实测值 + 证据） | 判定理由 |
|---|---|---|---|
| O1 | P5 IL PIANO DELLA SETTIMANA 第 2、3 条（content56.py 词条；SVG p5 y≈611/751） | 韩语括注收尾 “)” 独占一行（proof2 已记；本轮 P5 渲染目视复核相同） | 换行 artifact，与 KIT 已接受的 ‘·’ 行首同类；可读，无硬门违规 |
| O2 | P8 模型文第 1–2 行（content8.py 模型文；p8 y 635.56/656.36） | 真墨右缘 1863.36，越 1862 边 +1.36px（≈1.02pt），实墨 22 像素/行；与核心逐行对齐重测逐值相同（§6.2） | 冻结核心固有行为，空白纸面，无裁切/重叠 |
| O3 | P2 副标行（y 1594）、P5 图注行（y 602.95） | 真墨右缘 1862.88（+0.88px），越边像素 17/10 个、实色 0 个、最浅灰度 104；旧版新版整页渲染逐像素相同 | 抗锯齿毛边，非实墨；非回归 |
| O4 | P8 答案 32（content8.py 键表；p8 y 2394.8） | note 用 “Fate dolci” 直引号，正文/题干用 «Fate dolci»；translations.py ko 原值，与 nl 版同 | 内容正确；KIT §10 已披露 |
| O5 | P5 底部词表（content56.py；p5 y≈1885） | 第二行以 ‘·’ 开头 | KIT §10 已披露，核心同断点 |
| O6 | 网 PDF 重建 | 重建与交付同为 1,607,467 B，文字层逐字节相同；二进制差异仅在字体子集流内（obj 20 FontFile2 /Length 1975 vs 1976，及 CIDFontType0C 流；差异字节 878,484 个，均在子集流区段） | fontTools 子集化跨进程非字节稳定；非内容差异（proof2 同类现象：旧版重建差 5 B） |
| O7 | 印/网 P1 刊头 | “La/ Lucerna” 两词 x 差 0.4–0.5pt（印 404.8/599.5 vs 网 404.3/599.1；另同一行 “La/Lucerna” 第二组 556.5/1058.0 vs 556.0/1057.6），其余 7 页词框 0 差异 | 子集字体重测；0.5pt 不可见 |
| O8 | P4 结果表 | SAB 7.11、DOM 8.11 日标签各出现两次（每行自带） | 核心冻结设计，与核心相同 |
| O9 | P1 / P3 / P5 | P1 头条无首字下沉；P3 第二栏、P5 第三栏中段留白（P3-main col1 止于 y≈1249、P5 col1 止于 y≈1217 量级，核心同） | 核心既有格局，KIT §10 已披露 |
| O10 | P1 cifre 标题、P2 LA FRASE 标题（svg p1 y=1358.8、p2 y=1280.8） | 标题真墨越出奶油盒右缘 +67.6px / +43.2px（PIL +72.5/+44.5px），末字完整；与备份旧版像素逐值相同；越墨区无任何元素 | STRADDLE 规则：无裁切、无重叠、非回归 → 观察项（见 §6.3） |
| O11 | 9 盒末行真墨余量（§6.1） | 本轮实测 +3.24~+5.42px；P7 两盒比 proof2 旧版值低 0.48~0.96px（P7 重建所致，1~2 渲染行），其余盒低 0~0.48px（阈值边缘行）；最小余量仍 +3.24px | 全部在盒内；差值属渲染阈值边缘，非内容变化 |

## 9. 方法与证据文件

- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-it2-ko/`
- `logs/run.log`（run.py RC=0，TOTAL 150）、`logs/render.log`（印 PDF 逐字节同）、`logs/webpdf.log`（网 PDF 重建）、`logs/freeze-baseline.log`（8/8）、`logs/gates-ko.log`（19 门全过）、`logs/h-overflow.log`（2,213 节点，3 旗标）、`logs/creambox.log`（canonical 工具全版扫描）、`logs/pixel-check.log`（交付 PDF 像素：9 盒 + 全页边）、`logs/rowlevel.log`（P2/P5/P8 行级真墨实测）、`logs/threeway.log`（150 题三源 0 差异）、`logs/dump_reg.log`（REG 导出）、`logs/sweep-box-new.log` / `logs/sweep-box-old.log`（盒标题 sweep，新旧逐字相同）
- `ko/p8-extract.json`（150/150）、`ko/p8-compare.json`（CLEAN，[137,138,139]）、`ko/freeze-diff.json`（0 未解释片段）
- `out/reg.json`（REG 150 条）、`out/crops/`（P7 A2 D-2 句、P8 模型文右缘、P1 cifre 标题、P2 frase 标题）
- `rebuild/`（重建用源码副本 + 重建 SVG 8/8 + 重建印/网 PDF）、`freeze-baseline/build-copy/`（核心版复现副本，仅 OUT 行不同）、`pages/`（交付印 PDF 200 dpi 渲染 8 页）
- 工具链：repo `tools/venv/bin/python`（Pillow 13.0.0；it-ko 为 it 家，用 venv 栈）；共享工具 `tools/freeze.py`、`tools/p8.py`、`tools/occlusion_audit.py`、`tools/webpdf.py`；奶油盒 canonical `creambox.py`（与 proof2 同算法）；横向溢出、逐题核对、盒标题 sweep 脚本为本 scratch 自写/复用 proof2 拷本（`h-overflow-proof2.py`、`threeway.py`、`pixel-check.py`、`rowlevel.py`、`sweep_box_titles.py` 新写）。
- 工具局限：无。freeze.py diff 与 p8 compare 对纯拉丁文本漂移不可见——本次 D-2 回归另做了文字层检查（§2）与导出 diff 覆盖；web PDF 重建的字体子集流跨进程非字节稳定（O6），以文字层逐字节相同为准。
