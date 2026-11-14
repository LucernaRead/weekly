# WEEKLY-KIT — De Lucerna VOL.2 · NL×KO（荷兰语正文 × 韩语讲解）

- **配对**：네덜란드어 텍스트 · 한국어 해설（目标语 = 荷兰语，讲解 = 韩语 해요체）
- **期次**：W45 · 2026-11-02–08（VOL.2，核心 VOL.2 的扇出）
- **状态**：**builder-complete（未定稿）**——全部硬性门禁实测通过，见 §2；定稿须独立校对。
- **出货目录**：`files/weekly-report-w45-nl-ko/`（svg ×8、cards ×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- **建造树**：`hidden_files/weekly-report-w45-nl-ko-build/`（核心 build 的完整拷贝 + transform.py + koscan.py + rowcheck.py + chartcheck.py + 各轮日志/门禁原始输出/基线）
- **未做之事**：未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录（核心 build 目录只读对照，freeze 基线证明核心 8/8 未动）。

## 1. 建造溯源

- 核心：W45 荷兰语核心 VOL.2（`files/weekly-report-w45-nl-core/`，build `hidden_files/weekly-report-w45-nl-build/`；核心 WEEKLY-KIT.md 实测值：150 题，页数 10/18/18/18/18/18/12/38，A2 47/B1 72/B2 31，题型 complete 65 / choice 44 / matching 8 / true-false 7 / make-sentences 8 / cloze-choice 13 / translate 4 / writing 1，范文 87 词）。
- 开工前查重：本版 files/build 目录均不存在；同期运行中的渲染进程经查属于 NL×RU 分版（cwd 为其 build 目录），与本版无关，未受干扰；60–120 秒复查零本版写盘后安全开工。
- 开工前 `freeze.py baseline`：核心 8/8 逐字节复现（p1 5424557b · p2 78e6fcd2 · p3 5b9854e3 · p4 cc227fd9 · p5 e58064c9 · p6 6583fe28 · p7 65cfe2b3 · p8 fe22a151）；收尾复哈希仍 8/8 全等，核心未动。
- 变换：`transform.py` 行/串字面替换（长串优先，逐项断言），共 257 处映射（含 2 条补漏 + fix1–fix3 的 17 处改动，全部同步进 transform.py；从核心 build 全新拷贝 + 跑 transform.py 可复现本版源码）。
  - 覆盖断言：变换后 build 源码汉字残留 = 0（bslib4/content12/34/56/7/8/render/run 全量扫描；中途曾漏 2 条 P2 代码注「黄色代码：当心」「橙色代码：危险」，已补进 transform 并同步改 content 文件，复扫为 0）。
  - OUT 改道：5 个 content 模块 OUT → `files/weekly-report-w45-nl-ko/svg`；render BASE → `files/weekly-report-w45-nl-ko`；PDF 名 `De-Lucerna-VOL2-KO.pdf` / `De-Lucerna-VOL2-KO-web.pdf`。改道后 grep 验证：build 代码中无任何指向核心目录的生产输出路径。
  - 单进程驱动 `run.py` 一次构建：注册表 **TOTAL 150 = A2 47 · B1 72 · B2 31**；分版 {1:10, 2:18, 3:18, 4:18, 5:18, 6:18, 7:12, 8:38}，与核心全等；题型韩语标签计数 65/44/8/7/8/13/4/1 与核心全等；范文词数 87（核心同值，MODELO 荷语冻结）。
  - 全程未在核心 build 目录内 import/运行任何模块（README #11）。
- 字体：与 W43 NL×KO 完全一致，沿用核心 svglib 的 Noto CJK SC 面（serif/sans），未改动 svglib.py；韩文以 SC 面渲染，8 页卡片目视无缺字/方框。

## 2. 机械门结果（全部实测，终轮 fix3 渲染）

| 门 | 结果 |
|---|---|
| freeze.py baseline（核心） | 开工 8/8、收尾复哈希 8/8 逐字节全等，核心未变 |
| freeze.py diff | 新增 CJK 3,600 字**全为 Hangul 音节**；汉字（Hanja）= **0**；全文 桥接 = **0**；移除侧非 CJK 串 15 条逐项裁定（见 §2.1） |
| p8.py compare | **CLEAN 150 = 150**，missing=[]、extra=0；keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148] 全裁定（见 §4） |
| occlusion_audit.py（自检先行 OK） | 本版 **0 旗**，核心 **0 旗**，**NEW vs core = 0** |
| 同行墨迹碰撞扫描（README #10，rowcheck.py） | 1 处 P1 内容行碰撞 2.0px，与核心**同旗同值**（冻结荷语标题 + 冻结级别串，见 §2.2）；卡面目视该行字与级别间有间隙，属测量口径边际，非新缺陷 |
| P6 图表标签覆盖（基线锚定墨迹法，chartcheck.py） | 8 个标签（4 行名 + 4 数值）最大覆盖率 **0.0%**（<30% 通过）；首版 getbbox 法 78.3% 虚高读数为已知口径错误，已弃用，改用 PIL getmetrics ascent/descent + anchor ls/rs 基线锚定法重测 |
| 韩语中词分裂扫描（阻塞门，koscan.py，窗口 10–45） | 真切分总数 **16**，**S3（尾 ≥3 音节）= 0**；孤行末行（≤1 音节）= **0**；行首孤标点 = **0**（见 §5） |
| gloss 计数（渲染后 gloss() 串拆 ·） | P2 **6**、P3–P6 各 **5**，与核心 1:1 |
| P7 金句 | 8 句荷语逐字各出现 **2×**（并行计数：源文章页 + P7），页码标签与核心一致且每句在其标注页上实测存在；P7 短语逐字取自本期文章 |
| P7 词框冻结（阻塞门） | 定义句逐字保留（«meedoen» betekent: deelnemen, erbij zijn. In de Klimaatweek doet heel Nederland mee.），仅 gloss 本地化为韩语 |
| 读者园地（零编造） | 页上三事实 + 显性韩语邀请齐全，示例标注为编辑部示例（见 §6） |
| 图片/署名 | 仅公有领域/CC0 图片 4 张，署名行取自 Commons API Artist 字段（核心 KIT §5），每张均核实排版在版（见 §7） |
| 残留扫描 | 成品 SVG 汉字 = 0、西里尔 = 0、假名 = 0；他族家具（Note |、EXPLANATIONS IN ENGLISH）= 0；P8 注文拉丁词全为荷语引词/专名（museum/musea、perfectum、KNMI、ADE/PAN/RAI/NEC），无英语/德语残留 |
| 构建警告 | 终轮 build/render 日志 **FLOW OVERFLOW / HEAD TOO WIDE = 0** |
| 卡片目视 | 8 张 1950×2700 PNG 逐页目视：无重叠、无截断；页数 8（4 的倍数）、页脚 8/8 标 VOL.2、配对徽章/页眉页脚齐全 |

### 2.1 freeze diff 移除侧非 CJK 串 15 条裁定

- P1 徽章行 1 条：荷语家具行被韩语徽章替换（槽位裁定，见 §3），设计内。
- P8 分隔行 8 条：`— PAGINA N —` → `— 제 N 면 —`（KO 列家具定式），设计内。
- P5 贴士 2 条 + P6 括号 1 条 + P7 PAS OP 注 3 条：讲解括号/注文长度变化引起的**折行伪影**——新增侧对应行荷语词逐字不变（并行文本核查 `Kijk zondag om 20:00 uur op RTL 4`、`een boom`、`blijf ik thuis`、`zij zette vast` 均在版），源串荷语前缀逐字节冻结。

### 2.2 同行碰撞 1 处裁定（继承，非新缺陷）

- P1 内容目录行 `Musea bij nacht en boeken`（冻结荷语标题）与右端级别 `A2→B1`（冻结串）：rowcheck 测得重叠 2.0px；**核心同页同行测得完全相同的 2.0px**（rowcheck 对核心 SVG 的复跑结果），几何逐值相同；卡面目视标题与级别间有间隙，属 getbbox 边标口径边际。两元素均为冻结内容，不可为消旗而移动——裁定为冻结继承，不修复。

## 3. 家具逐项（KO 列定式，W43 NL×KO 实测 SVG 为准）

| 部件 | 本版落地 |
|---|---|
| P1 徽章 | 核心 y=372 荷语副题行即徽章槽：替换为 `네덜란드어 텍스트 · 한국어 해설 — 한국어 독자를 위한 판`，(975, 372）居中、19.5pt sans **bold BRICK**（#a4553a），与 W43 串/槽位/字号/颜色逐字全等 |
| P1 顶栏中段（y=92) | `ELKE WEEK IN HET NEDERLANDS · 매주 발행 · 네덜란드인이 읽는 네덜란드어`（与 W43 逐字全等） |
| P1 主标下题花（y=330, 40pt) | `네덜란드어 주간지 · VOL.2 · 기후 주간 · 박물관의 밤 · 12라운드`（W43 式：目标名 + VOL + 韩语主题词；主题词随本期内容变，VOL.1 → VOL.2） |
| P1 头条黑带右行 | 行1（24pt bold #b3a06a)`기후 주간`；行2（21pt)`온 나라가 함께하는 기후 주간 · 2면 참조`（W43 式为时钟主题两行；本期核心黑带右行是气候周主题，故韩语镜像核心语义，非 W43 时钟串） |
| 页脚左（每页） | `De Lucerna · 네덜란드어 주간지 VOL.2 · 텍스트는 네덜란드어 · 해설은 한국어`（W43 式，VOL.1 → VOL.2） |
| 页脚右（每页） | `제 {n} 면 / 총 8 면`（W43 式） |
| gloss 前缀 | `해설 — `（核心 `译注｜` 全量替换；P1 bridge 行首前缀同步改为 `해설 — `） |
| P8 答案分隔 | `— 제 {pg} 면 —` ×8（W43 式） |
| P8 答案头 | `ANTWOORDEN · 정답 — 면별로 정리했어요, 번호로 찾으세요`；右注 `문제마다 짧은 해설이 있어요 · ✓ 표시는 모범 답안 문제예요`（W43 式） |
| 栏目头 | 目标语原名 · 韩语短译：`HET NIEUWS · 헤드라인`、`LEVEN · 생활`、`CULTUUR · 문화`、`SPORT · 스포츠`、`JONGEREN · 청소년`、`VERDIEPING · 심층`、`TAAL · 언어`、`TOETS EN ANTWOORDEN · 시험과 정답`（W43 式） |
| 盒标题韩语后缀（短式） | `DE WEEK IN CIJFERS · 숫자로 보기`（W43 同盒式）、`ZO ONTHOUD JE HET · 외우는 방법`、`DE GRAFIEK · 그래프(연습용 데이터)`、`VOOR OF TEGEN? · 찬반 토론`、`PAS OP! · 실수 클리닉`、`HET WOORD · 이번 주 단어` 等——全部经遮挡审计 BOXTITLE 零新旗实测 |
| 题型标签 | 完成句子→`문장 완성` · 单选→`객관식` · 完形单选→`빈칸 채우기` · 造句→`문장 만들기` · 判断对错→`참/거짓 판단` · 词汇配对→`단어 짝짓기` · 翻译→`번역` · 写作→`쓰기`（W43 §3 全等） |
| instr 行 | 填空→`빈칸 채우기` · 判断→`참 / 거짓` · 造句→`문장 만들기` · 写作→`쓰기` · 把词和释义配对→`단어와 뜻 짝짓기`；P8 翻译题方向：137/138 `한국어로 번역`（荷→韩）、139/140 `네덜란드어로 번역`（韩→荷）；其余指示句全韩 해요체 |
| 盒内括号注 | 半角 `(韩语）`（核心全角（）全量转半角，W43 式） |
| bridge() 函数 | **未改名为 expl()**：W45 核心用 `bridge()` + `讲解｜` 前缀；仅把前缀串替换为 `해설 — `，渲染出的家具形式与 W43 的 expl 行逐字同式；改名无渲染收益，故不改（与 W43 的差异仅为函数名，成品串全等） |

## 4. 键差异全表（p8.py compare keydiff [7, 17, 70, 71, 76, 96, 137, 138, 148]，逐条以渲染答案行核对）

**裁定总览**：键本体 148 条与核心逐字相同；7 条为「注文差异」——p8.py 行级比对含注文，键（` — ` 前段）逐字相同，按 README #13 证伪为提取口径伪影；2 条为许可的翻译题键变更（#137、#138）。

| # | 键（核心 = 本版，逐字相同） | 差异所在 |
|---|---|---|
| 7 | B | 注文韩译 |
| 17 | wortelen | 注文韩译 |
| 70 | eiland | 注文韩译 |
| 71 | proef | 注文韩译 |
| 76 | gaat winnen | 注文韩译 |
| 96 | advies | 注文韩译 |
| 148 | B | 注文韩译 |
| **137** | **键变更（翻译题）**：核心键 = 中文句「气候周持续七天。」→ 本版键 = 韩语句 `기후 주간은 7일 동안 이어져요.`；注文韩译 | |
| **138** | **键变更（翻译题）**：核心键 = 中文句「橙色预警意味着：做好准备。」→ 本版键 = 韩语句 `주황색 경보는 대비하라는 뜻이에요.`；注文韩译 | |

其余许可类（未被 keydiff 标记、印刷行直查一致）:

- **#139 / #140 题干改向**：题干（荷语）冻结、作答正文由中文源句改为韩语源句（#139 `박물관의 밤은 저녁 7시부터 새벽 2시까지예요. → ___`、#140 `저는 기후 주간에 참여해요. → ___`），键（荷语）不变：139 `Museumnacht duurt van 19:00 uur tot 02:00 uur.`、140 `Ik doe mee aan de Klimaatweek.` 逐字同核心。
- **#150 装置项**：写作题，键 = 韩语注 `（열린 문제, 모범 답안은 아래에）`；答案行 `150. ✓ 모범 답안은 이 면 H 구역에 있어요(87단어）`，词数 87 与核心同值（MODELO 荷语冻结）。

## 5. 韩语中词分裂扫描（koscan.py，窗口 10–45，P8 答案流在内）

- 方法：解析渲染后 SVG 的 <text> 元素，同 x（±1px）、10 ≤ 行距 ≤ 45 的连续行配对；行末韩文 + 下行行首韩文为候选；以 build 源码空格对照裁定——无空格连写为真切分、有空格为干净断词；尾 = 下行首 token 的音节数。窗口下界 10 的意义：P8 答案行行距约 14.7px，15–45 窗口会结构性漏掉 P8（DE×KO 教训）。
- 终轮（fix3）：候选 30 对，**真切分总数 16，S3（尾 ≥3 音节）= 0**，孤行末行（≤1 音节）= 0，行首孤标点 = 0。
- 16 处真切分全为尾 ≤2 音节（주|는、박|물관,、문|장、실|내에、지역|을、비기|다、빅|매치、점수|는、활동|하는、조|사가、거예|요?、치우|다:、같|아요.、대문|자로、와|요:、여러|분의），均在 S3 门以下；另有 2 对 UNRESOLVED，均为家具/段落边界伪配对（P1 题花行→徽章行、P1 黑带两行分属不同元素，非折行切分，源码空格对照双否）。
- 修复史：首轮 S3 = 5（P1 쿠|포르던이 尾4、P6 여|러분은 尾3、P7 네덜|란드가 尾3、P8 헤이렌베|인-페예노르트예요 尾8、P3 주의|하세요. 尾3）+ 孤行 2 处（P4 요.、P8 요）+ 行首孤标点 1 处（P7 `: zij zette vast.`），经 fix1–fix3 逐项改短注文/桥接句消除；每次注文改动后 koscan + p8 + occlusion 全部重跑（P8 注文改动引起下游重排时亦然）。

## 6. 读者园地 — 诚实注（零编造）

- 页上三事实齐全：荷兰语披露句原文保留（`Ter perse: nog geen echte brieven of beste pagina-8-teksten binnen — daarom dit voorbeeld; belofte naar VOL.3.`）+ 韩语披露句同义（`마감 때까지 실제 독자 편지나 8면 최고 작문이 들어오지 않아서, 이 예시를 싣고 약속은 VOL.3으로 이어져요.`）+ 示例标注（荷语 `Li (voorbeeldbrief van de redactie)` + 韩语 `편집부 예시예요(실제 편지가 아니에요)`）。
- 显性韩语邀请（祈使句 + 刊登承诺，内容预告行、他页练习提示均不计入）：`여러분의 실제 편지와 8면 최고 작문을 보내 주세요. VOL.3에 실어 드릴게요!`（与披露句同段、BRIEVEN 盒内，卡面目视在盒内）。
- 未编造任何读者/来信/人名/引言；唯一信件为标注的编辑部示例（署名 Li 为示例的一部分，非真实读者）。W43 的 VOL.2 承诺顺延为 VOL.3，系核心 fix-1 的既定披露，非本版自改。

## 7. 图片与署名（核心 KIT §5，W43 Commons API Artist 字段）

- P1 herfstbos — Vovogov90，CC0；版面 <image> 1 个，署名行 `Foto: Vovogov90 — CC0` 在版。
- P2 kinderdijk — Nationaal Archief，CC0；版面 <image> 1 个，署名行在版。
- P3 gracht — W. Punt / Anefo, Nationaal Archief，CC0；版面 <image> 1 个，署名行在版。
- P4 elftal1912 — Spaarnestad Photo / Wikimedia Commons，public domain；版面 <image> 1 个，署名行 `Foto: Spaarnestad Photo / Wikimedia Commons — publiek domein` 在版。
- P5/P6/P7/P8 无照片，与核心一致；图片资产与核心 build assets 逐字节同源（未新下载）。

## 8. 工具链

- **run.py 解释器**：tools/venv/bin/python — Python 3.12.3，Pillow 13.0.0（同一 venv 复现核心基线 8/8 逐字节；系统 python3 亦为 3.12.3 但 Pillow 10.2.0 且无 cairosvg，故未使用）。
- **render.py（CairoSVG）解释器**：tools/venv/bin/python — Python 3.12.3，Pillow 13.0.0，cairosvg 2.9.1。
- **管线**：单进程 run.py（content12 → 34 → 56 → 7 → 8，注册表累积——绝不单跑模块，绝不在核心 build 目录内 import，README #11）→ render.py（SVG → 1950×2700 PNG 卡片 → cairosvg+pypdf 印刷 PDF → JPEG q85 @1400px 网页 PDF）。
- **行宽口径**：一律以渲染后 SVG 实测为准（occlusion_audit 的 PIL 真实墨迹 + koscan 的渲染行配对），不以源码估算为准。
- **修复轮基线**：每轮重渲染前，现版 SVG/card/PDF 完整 sha256 已写入构建日志（fix1/fix2/fix3-baseline-sha256.txt）；全部修复改动均同步进 transform.py（无只改 content 文件的改动）。

## 9. 构建轮次

1. **首轮渲染**：计数全合（150；级别/分版/题型如 §1），但遮挡审计 NEW 2 旗（P1 数字盒题超宽 996.2 > 961.0、P6 正反盒题超宽 1886.2 > 1885.0）+ koscan S3 = 5 + 孤行 2 + 行首孤标点 1。
2. **Fix 1**：盒题改短（`숫자로 보기`、`찬반 토론`）+ 5 处 S3 注文改短 + 2 处孤行桥接/注文改短 + 3 处 head ≥3 切分改短尝试 → 遮挡 0/0/0、p8 CLEAN 不变、koscan S3 = 0、孤行 0、行首孤标点 1（P7 冒号孤行未除）。
3. **Fix 2**：P7 桥接补 Dutch 例句成分（`wij hebben de tuin opgeruimd`）消除冒号孤行 + 邀请句/数字盒括号/图表注改短尝试 → S3 = 0、行首孤标点 0，但图表注改短新造孤行末行 `명)` 1 处。
4. **Fix 3**：图表注 revert 回 fix1措辞（孤行消除，S3 仍 0）→ 终轮全部门禁复跑通过（koscan S3 = 0、孤行 0、行首孤标点 0、遮挡 0/0/0、p8 CLEAN、freeze diff Hanja 0）。

## 10. 交付针脚（终轮 fix3 渲染）

- `De-Lucerna-VOL2-KO.pdf`（印刷）— 8,707,242 字节，sha256 `9690c3b9b57e66f1597a32e86962658d9b05b0229a766e58cc75005dd02aca56`
- `De-Lucerna-VOL2-KO-web.pdf`（网页，< 10 MB ✓）— 1,276,949 字节，sha256 `2fce7472a39398f310f297c20f42069e1df0772dfdb861da4415d240fdd24ef8`
- SVG（sha256）：p1-voorpagina `ebf439180c8ee57dfdbefb044d26dfb1cd004714b88cb8d1c4c8b4960615551f`；p2-leven `de3bc93eb3914aa4462107a15f84b0afecbef99a51b5f717bd024b80a85481c5`；p3-cultuur `57960853c8d22974d12fc231b49efe393d528b02922f3ea7497b659cccec9dbb`；p4-sport `b72ea4532f27faffdcd2253bcd039b42c3151ab998ec5e154f28e87e458c1915`；p5-jongeren `4da63c2c6f82499d0dc215435a1b6df1cb89b15e9970f7ddd6ec1f7b5facbe0a`；p6-verdieping `52f67855a60afb5fafedd159a04558471e231b835d9e2acf053865d123d7e3e4`；p7-taal `18ad5731b07765d955b70826088c16934e98e7d9cbb6bfdbb92e2010c9ca1e95`；p8-toets `a0a2a111d7ed2ce787e7388f6c8b81f744c4e72bf8d771f95278826efea0e55f`
- Cards（sha256）：p1 `64c3cfde8635a1268344790f63dd4f97e73ed4e2d712eedd85d79fdd4387b555`；p2 `ea7ea64e0902d09198fbd81095a6cc5b4696220552bb69260c9e0a0d8b54b8ab`；p3 `39be3b9102fa9101a4ba5d9faf981db8244ae778deb197e58f201d3ea0379582`；p4 `6fe09baa131d4680200e2a82a8cc8250ed26234f5efb50b7c6bd9b54bffe5387`；p5 `dd880e4bb7811a6a48da8fa6cbf32ac631d0a610ef5708dfc5e0bbb0d9535483`；p6 `a928e43f6ad6e7d011f5a60aab6d4185f844e40f7470c6276195d51f7779d693`；p7 `0b36dc4a2c2e3d6f767272740b032d3aa49e73a60f23d3abc3b686da7433d818`；p8 `9c1abf3cc526883dc7a9763f4c84f3d228320cddadb4cb79037fbc98a88cd176`

## 11. 交付说明

- 本版仅以文件交付（builder-complete，**未定稿**——定稿须独立校对门）。未推送 git、未发 Discord、未发主聊天。
- 文件：`files/weekly-report-w45-nl-ko/` — `svg/`（8 个 SVG）、`cards/`（8 张 PNG，1950×2700）、`De-Lucerna-VOL2-KO.pdf`（印刷 PDF，8 页）、`De-Lucerna-VOL2-KO-web.pdf`（网页 PDF，8 页，< 10 MB）、`WEEKLY-KIT.md`、`ABSTRACT.txt`。
- 构建树：`hidden_files/weekly-report-w45-nl-ko-build/` — 构建代码（bslib4/content*/svglib/run/render）、transform.py + transform-log.txt、koscan.py + koscan-fix3.txt、rowcheck.py + rowcheck-fix1.txt、chartcheck.py、构建日志（build-log.txt、build-log-fix1/2/3.txt、render-log-fix3.txt）、freeze-diff-fix3.txt/json、p8-compare-fix3.txt、occlusion-new-fix3.txt、core-sha256-before.txt、fix1/2/3-baseline-sha256.txt、final-sha256.txt。

## 12. D5 rebuild (2026-11-14, builder run; not a proofread round)

D5: 讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK（SOP §1.1 字体修复）。D5-only 家族：新样式已在仓，单版施工只装 D5、重渲一次。

- Core 落盘（全家共用一次，v1 执行）：`apply_variant.py --patch-core nl --week 2026-w45 --i-understand-this-writes-production` → `production/2026-w45/core-nl/svglib.py` +95/−3 行，`_D5_READER = "latin"`（D24：按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-nl-ko/svglib.py --target nl --reader ko --week 2026-w45`（先 `--check` dry-run，mode=cjk）。装后 `_D5_READER = "cjk"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（svglib.py 含 fix2 标记 13 处，安装器日志 "added fix2 block"）。
- 基线（修前生产版，venv 重建）：`run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE；印 PDF 11,938,148 字节；印/网文字层 vs issues 已发 web PDF 字符多重集差 **0**；修前普查 D5 违规 **拉丁 324**（>0，符合装机前提）。旧 pin 与基线实测不符（de 例：KIT 印 7,918,211 B，基线实测 7,526,971 B）——KIT SHA 滞后（PLAN 修正案：基线永不以 KIT SHA 为准），本节 pin 以实测发运值订正，旧 §10 pin 已同步更新为本次值。
- 导出器（第 0 步自验）：`scratch-2026-w45-nl/export_text_w45nl.py`（AST 导出，源自 content*.py 字面量，绝不从 PDF 反提；无 hardcode，标题由参数传入）。基线试跑 vs issues 已发 `.text.md` **11/11 BYTE-IDENTICAL**；patched 导出同样 BYTE-IDENTICAL（门 15）。
- 修复（run1 → run2）：共 **4 处**，只动字号，零文字改动。run1 缺陷：栏头超宽 3 处（ru 除外，ru 栏头未超）、occlusion TEXTX 1 处（P7 B1 栏头 'SCHEIDBARE WERKWOORDEN' 与 'B2' 重叠 5.2×17.8px；ru 除外）、boxtitle/creambox 1 处（ru/zh-cn/zh-tw 为 0），ru 另有 spill 1 处（codes 行注 'внимательны' 框底溢出 BELOW +13.34px）。
  - `content56.py:142` p.text DE GRAFIEK　그래프(연습용 데이터)：24 → **23**（宽 406.1px，超 5.7px；修后 389.1px，余量 9.2px）。
  - `content12.py:175` 栏头 DRIE ACTIES VOOR DEZE WEEK：25 → **24**（宽 425.0px；修后 408.0px）。
  - `content34.py:21` 栏头 TWEEDEHANDS IS OOK CULTUUR：25 → **23**（宽 456.7px；修后 420.1px）。
  - `content7.py:32` 栏头 B1　SCHEIDBARE WERKWOORDEN：24 → **22**（宽 455.7px；修后 417.8px）。
- 门禁（run2，全套 16 门 + D18）：**ALL-GREEN**。run TOTAL 150 / head_check 0 defects / d5 census 拉丁 0、西里尔 0、CJK 内花括号 0 / render RC=0 / webpdf RC=0（网 PDF 1,276,949 B < 7 MB）/ occlusion 0 flags（selftest 6 类全触发）/ p8 extract 150/150 / p8 compare CLEAN（missing=[] extra=0，keydiff=[137, 138]，137/138 为读者语重定向真重 aim，已裁定，非缺陷) / freeze baseline 8/8 / freeze diff vs base 新增 CJK 字符 **0**（新增拉丁 strings 424，D5 run 拆分所致；对照是 base 修前生产版，不是 core）/ spill 0（1 OBSERVE）/ boxtitle 0 / edge 0 TOUCH 0 NEAR / creambox 0 defects（P8 223 → 223 行，距页脚线余量 43.3px）/ 文字层 print=web 字符多重集差 **0**（29,768 字符），text.md BYTE-IDENTICAL / census_quotes 0 defective / D18 刊头 gap **89.1px** > 0。
- 补充校验 G15b（carryover，诊断性，不计入 verdict）：共享 `verify_textmd.py` 对 nl 目标家族未标定（表按 pt 目标语格式标定），patched 与基线同态 FAIL（de 例：SVG-only 711 / MD-only 1119，基线 711 / 1121；ru、zh-cn 基线与 patched 残差完全相同）——D27 类已知工具口径差，非 D5 回归；内容不变的证据以门 15（AST 导出器 BYTE-IDENTICAL + print=web 差 0）为准。
- 最终 pin（builder 原件；网 PDF 跨次字节不确定，closer 须拷 builder 原件，绝不重跑 webpdf）：印 PDF `De-Lucerna-VOL2-KO.pdf` 8,707,242 B，SHA-256 `9690c3b9b57e66f1597a32e86962658d9b05b0229a766e58cc75005dd02aca56`；网 PDF `2026-w45-nl-ko.web.pdf` 1,276,949 B，SHA-256 `2fce7472a39398f310f297c20f42069e1df0772dfdb861da4415d240fdd24ef8`；text.md 40,944 B，SHA-256 `cf94e576cf0f76a5889d809a050261ed999a98ae370ca37e2551a1309787b905`（与 issues 已发版 BYTE-IDENTICAL）。
- Builder scratch：`hidden_files/d5-redo/scratch-2026-w45-nl/patched/2026-w45-nl-ko/`；门禁总表复本（D29）：`production/notes/2026-w45/g-nl/scratch-d5-rebuild-nl/logs/2026-w45-nl-ko/GATES-SUMMARY.txt`。
