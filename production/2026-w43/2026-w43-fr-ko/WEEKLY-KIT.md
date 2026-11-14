# Le Lucerna VOL.2 · FR×KO（프랑스어 텍스트 · 한국어 해설）— WEEKLY-KIT

**状态：PASS（独立校对一轮零问题，见 §8）**
**配对：法语正文 VOL.2 + 韩语讲解（해요체）· W43（2026-10-19–25）**
**核心：法语核心 VOL.2「深秋与节日」（files/weekly-report-vol4/，145 题 = A2 55 · B1 65 · B2 25）**

## 交付物与实测针脚

| 文件 | 字节 | sha256 |
|---|---|---|
| svg ×8（svg/） | — | 见 §2 freeze 门 |
| cards ×8（cards/，1950×2700 PNG） | — | — |
| Le-Lucerna-VOL2-KO.pdf（印刷） | 16,642,695 | e4e5b0e627e7d13ff7d5ed6111030997342be6dbb5b04b6ddc87fdbee5eb8c77 |
| Le-Lucerna-VOL2-KO-web.pdf（网页，JPEG q85） | 5,782,068（<10 MB ✓） | 780fc874c22df11132ebbd07326087db788b663da69248297f3a6c3e11dff2e6 |
- D5 重建（2026-11-13，见文末 D5 节）：印 `The-Lucerna-VOL1-fr-ko.pdf` **12,023,580 字节**（SHA-256 `57bdc389e06e9e610f14e5455aa8844470e70e805b476635ccd96afde1b71f31`）；网 `2026-w43-fr-ko.web.pdf` **2,071,490 字节**（SHA-256 `93121c7ee6b69f47f39a5843d7e6461e7e0d92435ab612bac782143fce15b2e5`，< 7 MB）；text.md 与已发版 BYTE-IDENTICAL（SHA-256 `b075a5cc9ac05fe361b1b203e3bb1c17ae151d2daacf281bf24c723ca45c9bad`）。D5 前值：印 16,642,695 B（SHA-256 `e4e5b0e627e7d13ff7d5ed6111030997342be6dbb5b04b6ddc87fdbee5eb8c77`）、网 2,168,416 字节（`5d3de9d1…`，issues 已发版）。


建造目录：hidden_files/weekly-report-fr-ko-build/（核心 build 的改道副本，OUT 指向 files/weekly-report-fr-ko/；scratch/ 内含 mapping_ko.py 331 条映射、transform_ko.py、build.py 单进程驱动、render.py、linescan.py、注册表 dump 两份）。

## §1 来源与方法

- 动工前 `tools/freeze.py baseline` 在核心 build 上 8/8 逐字节复现；完工复核核心出货 SVG sha256 前缀与基线记录逐一（p1 5f1dc8a12056a93e · p2 b99e94bea2216ee9 · p3 cb4dc01ed3479e8d · p4 14b128b78c179cde · p5 f2d679f3a006d66c · p6 82021a2baf6cbbd3 · p7 cb2bfc1c15d36d8e · p8 5ac98ee139a1b479）——核心未动 8/8。
- 变换：抽取全部含汉字字符串常量 331 条（bslib4 5 · content12 62 · content34 87 · content56 84 · content7 30 · content8 63；出现 430 次），逐条译韩后以 AST 切片回填（f-string 内常量以原文替换、普通常量以 repr 替换），断言：每条须命中抽取计数、映射键与抽取集互为全覆盖。法语正文一字未动。
- 结构编辑仅三项：① bslib4 `bridge()` 改名 `expl()`（定义 1 处 + 调用 27 处，逐文件与核心同数）；② P1 徽章行插入（见 §3）；③ content8 印刷注释改显式 PRINT_NOTES + 半角括号式（见 §4）。
- 字体口径与核心同：svglib.py 未改（Noto CJK TTC，tables.json 字体面索引 KR=1 经核心 SC 面渲染管线出货，EN×KO 同管线先例）；8 页 cards 肉眼核韩文字形无缺字/方框。

## §2 机械门结果（终版产物实测）

| 门 | 结果 |
|---|---|
| freeze.py baseline（动工前，核心 build） | 8/8 逐字节复现 |
| freeze.py diff（终版） | 新增 CJK 字 2,725 个，**全部为韩字音节**（汉字新增 = 0；含汉字的新增字符串 = 0）；移除字符串中无汉字/韩字者 = **0**（移除侧全为讲解层）；法语正文文本多重集与核心全等 |
| p8.py compare | **CLEAN 67 = 67**，missing=[]、extra=0、uncertain=[]，keydiff=[71, 72, 73, 132, 145]（见 §4） |
| occlusion_audit.py（自检先行通过） | 本版 **0 旗**，核心 0 旗，NEW vs core = **0** |
| 同行墨迹扫描（README #10，scratch/linescan.py） | 8 页同基线墨迹碰撞 = **0** |
| 图表标签元素检查（README #12） | P6 图表 6 个百分值标签（28/24/17/11/9/11 %）元素齐全，后绘不透明形覆盖 = 0；练习图免责行韩语完整呈现 |
| 孤行标点扫描 | 终版 = **0**（初版 2 处，已修，见 §6） |
| 注册表逐项比对（145 题） | 页码全等；难度 A2 55 · B1 65 · B2 25 两边同；type 145 条全译；note 121 条译韩、24 条语言中立注逐字未动（含 #117）；与核心同文且含汉字的 note = 0 |
| 残留扫描 | 成品 SVG 含汉字字符串 = **0**（中文讲解残留 0）；西里尔字符 = 0；荷/俄家具串 = 0；禁用术语：paper SVG = 0、operative code（build *.py）= 0、scratch = 0〔独立校对更正：本 KIT 另有 3 处该词的反引号代码标识符（§1 改名记录、§3 家具表、§5 点数核对），与已入仓 EN×RU/FR×RU/JA×RU KIT 的改名记录先例同形，属披露范围、非版面缺陷；原行「本 KIT = 0」表述不确，特此订正〕 |
| 日历核验（Europe/Paris） | 2026-10-25 周日冬令时 03:00→02:00、10-31 周六 Halloween、11-01 周日 Toussaint、11-02 周一开学——与 W43 日期表（10-19 周一 … 10-25 周日）算术一致，核心口径未动；VOL.3 预告韩语行三项承诺全保留（见 §6 注） |

## §3 家具登记（FR 目标 · KO 列；式样照 EN×KO KIT §3 定式，目标名换 프랑스어、VOL.2）

| 部位 | 本版式样 |
|---|---|
| P1 徽章 | 法语核心 y=372 副题行为冻结法语（FR×RU/FR×JA 先例），徽章另行**插入**于倒计时带下 y=574，22pt sans 粗体 BRICK 居中：`프랑스어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`（与 EN×KO §3 对法语版的预登记式样逐字一致） |
| P1 顶带左 | `VOL. 2 · 제2호` |
| P1 顶带中（strapline） | `HEBDOMADAIRE EN FRANÇAIS · 매주 발행 · 프랑스가 읽는 프랑스어` |
| P1 衬线行（y=330） | `프랑스어 주간지 · VOL.2 · 깊은 가을 · 명절` |
| P1 倒计时带右行 | `이번 주 일요일 · 프랑스 겨울 시간` / `시계를 한 시간 뒤로 돌려요 · 2면 참조` |
| P1 头条 kicker | `POLITIQUE · LA UNE · 프랑스 국내 정치` |
| 页脚（每页） | `Le Lucerna · 프랑스어 주간지 VOL.2 · 텍스트는 프랑스어 · 해설은 한국어` |
| 页码（每页右） | `제 {n} 면 / 총 {total} 면` |
| 章节带（P2–P8 左） | 法语原题 · 短韩语后缀，如 `VIE QUOTIDIENNE · 생활`、`POLITIQUE & CHIFFRES · 시사`、`EXERCICES & RÉPONSES · 연습 문제와 정답`（栏宽受限取短式，EN×KO §8-① 教训） |
| 章节带右行 | 如 `NIVEAU A2 · Changement d'heure · 겨울 시간`（法语题名保留，末段韩语） |
| gloss 前缀 | `해설 — `（单前缀；字符串内不自带前缀，核心自带的「译注｜/讲解｜」已在映射中剥除） |
| 讲解行方法 | `expl()`（由 bridge() 改名） |
| P8 页分隔 | `— 제 {pg} 면 —` |
| P8 注释式样 | 半角括号、键后空一格 ` ({note})`，显式 PRINT_NOTES 强制核心同集（§4） |
| P7 页标签 | 逐字保留核心法语 `(page N)`，不本地化（短语条目 §5 核） |
| 题型/指令标签 | 문장 완성 · 객관식 · 문장 바꾸기 · 단어 짝짓기 · 읽기 판단 · 따라 연습 · 빈칸 채우기 · 도표 읽기 · 대화 완성 · 오류 고치기 · 읽기 이해 · 번역 · 쓰기；指令标签 빈칸 채우기 · 바꿔 쓰기 · 고치기 · 단어와 뜻 짝짓기 · 짝짓기 |
| 导师人格 | 小墨 → `샤오모`（P7 독자 마당评论以 `샤오모의 한마디 — ` 起） |

## §4 键差异全表（仅 5 项，与 FR 家族已入仓扇出合法集逐字吻合）

核心印刷集先以 `p8.py extract` 出货核心 P8 独立复证 = 67 条 {1, 4, 17, 22, 26, 33, 35, 41, 44, 46, 47, 55, 56, 65, 71–74, 80–85, 92, 97, 105–145}，并以注册表按核心规则复算同集。本版 content8 以显式 `PRINT_NOTES` 同集强制（核心按注长阈值的规则对韩语长注必漏印，禁用阈值路径），compare CLEAN 67=67。

| # | 核心键 | 本版键 | 类别 |
|---|---|---|---|
| 71 | ex. : amusant, parce que les enfants adorent se déguiser（参考答案） | ex. : amusant, parce que les enfants adorent se déguiser (예시 답안) | P5 开放题键尾装置（法语键体逐字） |
| 72 | ex. : j'aime les histoires et les mots nouveaux（参考答案） | ex. : j'aime les histoires et les mots nouveaux (예시 답안) | 同上 |
| 73 | ex. : ce ne sont pas les résultats（参考答案） | ex. : ce ne sont pas les résultats (예시 답안) | 同上 |
| 132 | 读一份民调，本身就是在参与政治。 | 여론조사를 읽는 것 자체가 이미 정치에 참여하는 거예요. | 翻译题键（目标句译韩；题干法语源句冻结） |
| 145 | 开放题 — 要点见写作框，范文在第 8 版写作框内 | 열린 문제 — 기준은 쓰기 칸에, 모범 답안은 8면 쓰기 칸 안에 | 写作题装置键 |

- #117 数学注 `7 h 30 = et demie` 语言中立，注册表逐项比对证其逐字节未动（核心自身印刷口径）。
- 翻译题题干侧（#133–135 的读者语源句）随读者语呈现：核心中文源句 → 本版韩语源句，键（法语）不动；与 FR×RU 同题处理一致。
- 任务书预估的 {137, 138} 经注册表实测为 짝짓기 题（键 b/c 不变、仅注译韩），不入键差异——以实测为准，与 FR×NL/FR×RU 先例表 [71, 72, 73, 132, 145] 全合。

## §5 gloss 与 P7 逐条点数

- `expl()` 调用点逐文件与核心 `bridge()` 全等：content12 4 · content34 10 · content56 9 · content7 3 · content8 1（合计 27），gloss 词条逐条保留、一项不少；各页 gloss 串在 freeze diff 中一一对应（移除侧全为含汉字讲解串）。
- 词表盒条目（P3 축제 단어장 10 条、P4 스포츠 단어장 8 条、P5 화면 단어장 10 条、P6 선거 단어장 8 条）逐条与核心同数同序，仅释义译韩。
- P7 短语 7 条：法语原句、`(page N)` 页标签、题干、答案、法语提示逐字节 = 核心；仅语法点讲解（元素 [1]）译韩，前缀式样 `문법 포인트 — `。content7 内 `(page N)` 出现次数 9 = 9。
- P7 短语为核心自身凝练形，逐字继承，未回改原文摘录。

## §6 自校缺陷与修复（全量自校一轮，8 页 cards 肉眼 + 机械门）

初版机械门共 5 处缺陷，全为韩语讲解层文字过长/折行（README #15：讲解层自有文字越界必改短，不以核心同旗豁免），逐一改短后整轮复跑全绿：

1. **P1 GT 盒副题出界**（BOXTITLE：墨迹右 1898.2 > 盒边 1885）→ `이번 주 프랑스 인기 검색어 · Google Trends 프랑스` 改 `이번 주 프랑스 인기 검색 · Google Trends 프랑스`（去「어」，与 EN×KO 同盒同修法）。
2. **P1 GT 盒末行出页**（EDGE：墨迹至 x=2043）→ `이번 주 프랑스에서 가장 많이 검색된 것은 바로 2027 대선 여론조사예요.` 改 `이번 주 프랑스 검색 1위는 2027 대선 여론조사예요.`（实测 406.7 ≤ 412 可用宽）。
3. **P2 ET VOUS 盒高溢出**（LINEX：盒底 1577.9 压 1557 分节线；韩语答句 3 行比核心中文 2 行高一线）→ 答句压缩至 2 行 `나라에도 서머타임이 있나요? 일요일엔 몇 시에 일어나요? 프랑스어 두 문장 써서 보내 주세요.`，盒底回到 1548.9（与 EN×KO §8-② 同缺陷同修法）。
4. **P7 clinic 头过宽**（HEAD TOO WIDE）→ `CLINIQUE DES ERREURS · 실수 클리닉`（453.7 > 434）改 `CLINIQUE DES ERREURS · 실수`（377.7）。
5. **孤行标点 2 处**（P2 gloss 末句号、P8 #134 题干末句号被折行甩至单独一行）→ P2 gloss `la reprise 개학, 다시 시작` 改 `개학·재개`；P8 #134 题干 `방학 중이에요` 改 `방학이에요`（单行收齐）。终版孤行扫描 = 0。

另：映射阶段自查改一处误译（P3 词表 `un saint — 성인`，初稿误作他词，已正）。

## §7 给独立校对的裁定项（非缺陷，勿误报）

- **P4 头 `REGARDER UN MATCH EN FRANÇAIS` 的 HEAD TOO WIDE 警告**：冻结法语串，前进宽 523 为该串的纯函数，核心构建同警；审计 TEXTX/COVER 对核心与本版同为 0 旗，成品卡肉眼无碰撞——继承核心几何，不动。
- **P5 « Lire en français, c'est chic. » 引文折行**（» 单独成行）：法语冻结串 + 固定盒宽，核心同形。
- **P7 署名竖排条与 P8 引言头**：冻结法语，继承范围以出货核心为准。
- **VOL.3 预告**：法语段冻结；韩语行 `다음 주 토요일은 Halloween, 일요일은 모든 성인의 날이에요. 겨울 시간 첫 주, 밤이 점점 일찍 찾아와요.` 完整保留三项承诺（10-31 万圣节、11-01 诸圣节、冬令时第一周）。
- 内容红线：讲解层未引入国际政治；法国国内政治为核心既有口径，不增不删。P6 练习图免责行保留诚实披露口径（연습용 자료, 실제 여론조사 기관이나 후보자와 관계없어요）。

## §8 独立校对记录（2026-10-22）— **PASS（一轮零缺陷、零修复、无重渲染）**

全部结论为校对者独立复跑/复测，未采信建造者自报。Scratch：hidden_files/proof-fr-ko/scratch/。

- **工具门（独立复跑全过）**：freeze.py baseline 核心 8/8 逐字节复现，开局/收尾核心 8 SVG sha256 两度全等（5f1dc8a1…5ac98ee1），核心零触碰；freeze.py diff 分账独立成立——新增 CJK 2,725 字全为韩字音节、汉字新增 = 0、纯拉丁增删串 = 0（法语正文多重集与核心全等）、移除侧含韩字串 = 0；occlusion_audit.py（自检先行通过）本版 0 旗、核心 0 旗、NEW vs core = 0。
- **注册表复验（自备导出器，双 build 改道副本一进程导出）**：两版复渲出货 SVG 各 8/8 逐字节（复现性自证）；REG 145 = 145，page/level 分布全等（A2 55 · B1 65 · B2 25，逐页 10/16/18/18/17/18/11/37）；**键差异恰 {71, 72, 73, 132, 145}**，与 §4 表逐字合（71–73 键尾 «（参考答案）»→«(예시 답안)»、键体法语逐字；132 翻译题键译韩；145 装置键）；题型标签 145 条全译韩（同形 0）；注差异 121 条、未变 24 条逐条裁定为法语注/语法箭头/算式类语言中立（含 #117 «7 h 30 = et demie» 逐字节未动，仅 type 标签译韩）；本版 REG 全部字符串字段汉字 = 0。**全部 145 键已从法语正文逐题手工重推导，零分歧**（含 P6 图表 28/24/17/11/9/11 合计 100、#81 28−24=4、#84 B+3=27>A−2=26、#85 52%、五组配对映射、P8 完形与对话链）；121 条韩注逐条对照核心注，忠实、해요체 一致。
- **p8.py**：extract 出货核心独立复证印刷集 = 67 条，与任务书集合逐项全等；compare **CLEAN 67 = 67**（missing=[]、extra=0、keydiff=[71, 72, 73, 132, 145]）；content8.py 第 143 行显式 PRINT_NOTES 同集在位；渲染式样半角括号 + 注前空格实证（P8 全角括号仅 2 处，为 #119 注文自身 «（à+les）» 内容、与核心逐字节同，非包裹式）。
- **KO 列定式核**：徽章实测 y=574、x=975 居中（anchor=middle）、22pt、字重 700、填色 #a4553a（BRICK），文 «프랑스어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판» 与 EN×KO §3 对法语版预登记式逐字一致，位于倒计时带与头条 kicker 之间，P1 配对显著达标；页脚 ×8 逐字同 §3 登记串、VOL.2 全册一致；页码 «제 N 면 / 총 8 면» 逐页对位；P8 分隔 «— 제 1–8 면 —» 各一；gloss 盒渲染 9 = 核心 9、逐页分布全等、前缀 «해설 — » 单层（双前缀 = 0）；expl() 调用点逐文件 4/10/9/3/1 = 核心 bridge() 同数（合计 27），改名属实（operative code 中该旧名 = 0）。**列内差异注记**：DE×KO 无插入徽章（配对由顶带/副题/时钟带/页脚承载，其 §3 登记式），本版按 EN×KO §3 预登记另行插入徽章行——两式并存，均满足 P1 显著标注，以各自 KIT 登记为准。
- **几何兜底（自写扫描，复用审计真墨迹盒）**：同行墨迹扫描（README 第 10 条）本版与核心 gap<12 的对子均 0、无碰撞（P1 顶带三簇含 FR 核心 strapline 前科位，实测干净）；P6 元素级任意覆盖率检查（第 12 条）：文字被后绘不透明图形覆盖 >0.05% 者 = 0，六个百分值标签（28/24/17/11/9/11 %）齐全、练习图免责行韩语完整；建造者 5 项自校修复逐项复核落点——P1 GT 副题/末行改短形在版、P2 ET VOUS 盒底实测与核心逐值全等（1549.6 含线宽展开 = 自报 1548.9 口径）、P7 clinic 头 «· 실수» 在版、P8 #134 题干单行在版；孤行标点节点本版 2 处（P1 «?»、P5 «»»）与核心同位同串，属冻结法语（P5 引文折行为 §7 既裁项），非讲解层缺陷；P4 宽头 «REGARDER UN MATCH EN FRANÇAIS» 与 P7 竖排署名、P8 引言头均为冻结法语、与出货核心同几何（freeze 纯拉丁增删 = 0 + 审计双零互证），继承裁定成立（第 15 条界内）。
- **P7 / gloss 点数**：7 条金句 + (page N) 页签逐字 = 核心（标签节点 9 = 9 逐条全等）；四个词表盒数据层条数同序（P3 10 · P4 8 · P5 10 · P6 8=4+4），法语词头序列逐条全等、仅释义译韩；导师人格 小墨 → 샤오모 在版；VOL.3 预告韩语行三项承诺（10-31 Halloween、11-01 诸圣节、冬令时第一周）完整保留。
- **日历 / 红线 / 残留**：`date`（Europe/Paris）实测 10-19 一至 10-25 日、10-25 03:00→02:00 回拨、10-31 六、11-01 日、11-02 一开学，与纸面全合（#109/#140 的星期键亦合：11-01 日、10-24 六）；讲解层无国际政治新增（法国国内政治为核心冻结口径）；残留独立复扫：成品 SVG 汉字 = 0、西里尔 = 0、荷/俄家具串 = 0、禁用术语 paper/code/scratch = 0（KIT 3 处反引号改名记录已于 §2 更正注中披露）。
- **最终针脚（磁盘实测，与建造者自报逐字全合）**：网页版 Le-Lucerna-VOL2-KO-web.pdf **5,782,068 B**、sha256 `780fc874c22df11132ebbd07326087db788b663da69248297f3a6c3e11dff2e6`（<10 MB）、8 页；印刷版 Le-Lucerna-VOL2-KO.pdf **16,642,695 B**、sha256 `e4e5b0e627e7d13ff7d5ed6111030997342be6dbb5b04b6ddc87fdbee5eb8c77`、8 页；cards ×8。

**结论：PASS，可由主线以 slug `2026-w43-fr-ko` 经 tools/insert.py 入仓。**

## §9 D5 重建记录（2026-11-13，D5-only）

SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader（SemiBold）。
施工不 commit、不 push；入仓由独立重校后的 closer 做。工作日志：
`hidden_files/d5-redo/scratch-2026-w43-fr/logs/2026-w43-fr-ko/`；
逐版报告：`production/notes/2026-w43/g-fr/scratch-d5-rebuild-fr/D5-REPORT-2026-w43-fr-ko.md`。

**装机**：core 落盘 `apply_variant.py --patch-core fr --week 2026-w43`（core-fr
`svglib.py` +95/−3 行，`_D5_READER = "latin"`）；本版 `--svglib patched/…/svglib.py
--target fr --reader ko --week 2026-w43`，装后 `_D5_READER = "cjk"`；路由单元测试 FAILURES: 0；fix2 块保留。
D1 组装先于安装：patched svglib 取本地 fanout D1 版，组装后与生产版 svglib 的 diff 恰为 D1 hunk 一处（28 行）。

**基线**（修前生产版）：run TOTAL 145，0 警告；印 PDF 与 `d1-fix/work/2026-w43-fr-ko/RESULT.txt`
的 shipped SHA/字节逐字节一致；印/网文字层差 0；自建网 vs issues 已发 web 非空字符差 0（仅空格差）；
修前普查 D5 拉丁 419、西里尔 0、弯引号在 CJK 0；基线 P8 noted 67/145。

**缺陷与修法**（run1 → run2 → run3；修法只动字号、盒高与间距，未动文字）：
head 5 项（共用 5）；箱标题 5 处（COMMENTATEUR 20、TROIS DATES 21、scrutin 21、sport 22、écrans 21）；spill ×2；run2 P2 LINEX ×5 → run3 消除。

P8：200→198 行，距页脚线余量 32.7→32.7 px。

**门禁 run3（全套 16 门 ALL-GREEN）**：run TOTAL 145、0 警告；head_check 0；
d5 census 0/0/0；render RC=0；webpdf RC=0（2,071,490 B < 7 MB）；occlusion 0 flags；
p8 extract noted 67/145；p8 compare **CLEAN**（keydiff=[71, 72, 73, 132, 145]）；freeze baseline 8/8；
freeze diff 新增 CJK 字符 0；spill 0；boxtitle 0 DEFECT（54 titles）；
edge 0/0；creambox PASS 0 defects；文字层 print=web 差 0（各 102,633 字符）；census_quotes
0 defective；fr 家无 gates.py。

**新交付物**：印 `The-Lucerna-VOL1-fr-ko.pdf` 12,023,580 字节（`57bdc389…`）；
网 `2026-w43-fr-ko.web.pdf` 2,071,490 字节（`93121c7e…`）；text.md BYTE-IDENTICAL
（`b075a5cc…`）。练习仍为 145 题。
