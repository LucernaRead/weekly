# PROOF-NOTE — 2026-W47 en-zh-tw 独立复校 proof1（2026-11-11）

- 版：`production/2026-w47/2026-w47-en-zh-tw/`，印刷 `The-Lucerna-VOL4-en-zh-tw.pdf`（38,152,082 B，SHA-256 `d2e919473d70463a00b3be10129bfecbd3c1a9137b0ae4ab0cf8ca2bdea78e07`）、网页 `The-Lucerna-VOL4-en-zh-tw.web.pdf`（2,927,283 B，SHA-256 `df41f1fc1a6786b839c63fdd53ecec1fdecba57a19ddf7c274a679762f421545`）、`2026-w47-en-zh-tw.text.md`（50,505 B，SHA-256 `6ecf354e4e614c77d747604aab6ef888ac794305869e997bc4d9049b31324dbc`）。三者与 KIT §7 及任务书一致；两 PDF 各 8 页，1462.5 × 2025 pt。
- 复校员：独立 proof1，与建版者不是同一人。只复校，未改任何源文件、未重建、未 commit、未 push、未动 tools/、未碰 core-en。中间件全在 `hidden_files/w47/scratch-proof-en-zh-tw1/`（`TMPDIR=<scratch>/tmp`），未写 /tmp。
- 探针：`git hash-object -w --stdin` 成功（`9daeafb9…`）；scratch 真实写文件成功。

## 结论：(b) 有缺陷，不可定稿

共 **9 项**，全部根在 core-en（核心盘上同错同形），记为**核心级**，本版无法单修，须核心修 + 全版重出 + 从头再复校。本版繁体中文层未发现独有缺陷。

## 缺陷清单

### D1（严重，核心级）— P3 配对题答案键 Q39/Q40 互换
- 定位：P3 `C · THE WORDS`（38–41 题）+ P8 答案页 + `registry.json` 39/40 条 + `text.md` 39/40 行。印/网两 PDF 文字层均含错键。
- 事实（印版 P3 SVG 节点顺序实测）：
  - a. a person who teaches and guides you（= mentor，39 题）
  - b. a person chosen to take part in the Games（= tribute，38 题）
  - c. a person who lives with you in the jungle camp（= campmate，41 题）
  - d. the place where the Games are fought（= arena，40 题）
  - 正确键：38→b、**39→a、40→d**、41→c。印出键：38→b ✓、**39→d ✗、40→a ✗**、41→c ✓（P8 印 `38. b · 39. d · 40. a · 41. c`）。
- 根在核心：`core-en/registry.json` 39 条 `key='d'`、40 条 `key='a'`，与本版完全一致。`p8.py compare` 判 CLEAN 是因为两边同错——该门只核对版与核心一致，不核对键与题面。
- 影响：按题面做对的学生在答案页被判错。须改核心 registry + 核心 P8 键 → 核心重渲染 → 本版重出 → 从头再复校一轮。

### D2（中等，核心级）— P1 SEARCHES 盒末行漫出盒底
- 定位：P1 右栏 SEARCHES 盒，rect `x=1439.5 y=588.0 w=422.5 h=668.0`，盒底 1256.0；盒内末行 `相對熱度示意，非精確搜尋量。` 基线 1274.0，**超出盒底 18.0 px**（盒内末基线 1240.0，余 +16.0；该行是盒内 gloss 内容，x0=1461.5、19pt，非下块标题）。裁图 `render/crop-p1-searches-bottom.png` 目视证实：该行落在盒外白纸上。
- 根在核心：core-en 同盒同几何，核心末行同样 -18.0（核心行 `相对热度示意，非精确搜索量。`）。盒高是核心模板几何问题。
- 工具盲区：occlusion 审计 0 flags（此类缺陷盲区）；须逐行裁定（本版全部 32 奶油盒已逐行裁定，其余带下 35–37 px 的行全是下块栏头，见 GATE-LOG）。

### D3（中等，核心级）— P2 DID YOU KNOW 盒末行漫出盒底
- 定位：P2 右栏 DID YOU KNOW 盒，rect `x=1439.5 y=832.9 w=422.5 h=325.5`，盒底 1158.4；盒内末行 `November 3.` 基线 1171.1，**超出盒底 12.7 px**（盒内末基线 1140.5，余 +17.9）。裁图 `render/crop-p2-didyouknow-bottom.png` 目视证实：`November 3.` 在盒底白边之下。
- 根在核心：core-en 同盒同几何（-12.7），且漫出的行是英文核心正文。同属核心模板盒高问题。

### D4（轻微，核心级）— “已確認”一词模糊了 call 与 certified 的区分
- 定位：Q7 答案注 `眾議院民主黨獲254席（11月8日已確認數）`；Q82 `11月8日已確認：眾議院民主黨254席`；Q83 `眾議院19個選區尚未確認`；Q84 `參議院35席中33席已確認`；Q90 `兩個參議院選區尚未確認：阿拉斯加與密西西比`。其中 82/83/84 的注印在 P8 答案页（SVG 可见）。
- 事实：正文 P1/P6 反复强调 “A ‘call’ is not the official result”，11 月 8 日的数只是 AP 的 call、不是 certified 结果；答案注却称其为“已確認”。根在核心 `registry.json`（同款措辞 5 处），繁体层是忠实翻译。建议核心与各版统一改“11月8日 AP 已公佈/已宣佈”一类表述。

### D5（严重，核心级）— P4 Ashes 整版内容错了一年
- 事实（网上核实：Wikipedia “2025–26 Ashes series”、Flashscore、Sky Sports）：
  - 2025–26 Ashes 已于 **2025-11-21 至 2026-01-08** 打完，澳大利亚 **4–1** 获胜；首场 2025-11-21–22 珀斯，澳大利亚 8 个 wicket **两天**取胜。
  - “Perth Stadium 从未办过 Ashes Test”自 2025 年 11 月起已不成立（首场即在珀斯举行）。
  - “英格兰上两次访澳 2017–18 与 2021–22 均 0–4 失利”——至 2026 年 11 月最近一次访澳是 2025–26（1–4 失利）。
  - “上一届系列赛是 2023 年英格兰打平”——至 2026 年 11 月上一届是 2025–26。
  - 2026 年 11 月并无 Ashes，下一届在 2027 年英格兰。
- 波及：P1 简讯（IN BRIEF “ASHES Sat, Nov 21…”）、P1 搜索榜第 2 位 “ashes”、P1 导语（“…the Ashes to Perth”）、P2 “WHAT IS ON THIS WEEK?”（“On Saturday, November 21, the Ashes begin in Perth”）、P4 整版主文 + “WHY PERTH?” 框 + “SATURDAY, NOVEMBER 21” 框 + 练习 Q46–51 / 52–55 / 60–63、P5 “THE JUNGLE, TOO”（“the Ashes begin on Saturday morning in Perth”）、P7 金句（“The Ashes are not a sport for early nights.”——引文逐字无误，但所引文章本身失实）、P7 “NEXT WEEK”（“The Ashes, second week in Perth”）、P8 Q125（“The first Ashes Test starts on… C. Sat, Nov 21”，答案键与失实文章内部一致）。
- 附带：纸面首球时间 “10:20 a.m. local — 2:20 a.m. in London”与 2025 年赛程 listing（10:30 local / 02:30 GMT，crictotal）相差 10 分钟，次要，待修方复核。“Day one is already sold out”未独立核实。
- 根在 **core-en**（核心文本与本版一致），须报协调员、由核心层修正并联动全部 12 个读者语版；本版单独无法修。严重度：重大——整版主故事 + 跨 7 页的连锁引用全部失实。

### D6（中等，核心级）— P2 SENATE 框题跑出奶油框
- 定位：P2 “THE SENATE, IN NUMBERS　參議院數字”（Noto Sans CJK TC 700，23pt），奶油框 x=538.5–961.0，标题基线 y=562.84。
- 实测（本版 `svglib.text_w` + 卡片真墨）：advance 起于 556.5、止于 989.1 → **超出框右缘 28.1 px**；真墨 557..986 → **超出 25 px**。裁图 `render/crop-p2-senate-title.png` 目视证实：末二字“數字”落在框外白纸上，框边从字间切过。
- 根在核心：core-en 同题同数（真墨亦 557..986，-25 px）。KIT §4 “Box titles … all fit, no collision”与此相悖——KIT 框题表不可信。

### D7（中等，核心级）— P2 SAY IT 第 2 盒英文行横向漫出
- 定位：P2 SAY IT strip，第 2 个奶油盒（x=610–890，y=1636，h=132），英文行居中。
- 实测：`The new Congress meets in January.` span 574.0..926.1 → **左超 36.0 px、右超 36.1 px**，整句横跨盒外白纸。裁图 `render/crop-p2-sayit-box2.png` 目视证实：句首 “The” 与句末 “January.” 均在奶油框之外。盒 1（`The counting continues.` 181..417.1）与盒 3（`Happy Thanksgiving!` 1094.9..1305.1）的英文行合框，三盒中文行均合框。
- 根在核心：英文行是核心正文，核心同盒同行同样漫出（盒宽 280 px，英文行宽 352.1 px）。

### D8（轻微，核心级）— P4 栏 3 框题真墨部分出框
- 定位：P4 “SATURDAY, NOVEMBER 21　週六賽程”（23pt 粗体），奶油框 x=1440–1862，标题基线 y=893.0。
- 实测：advance 1457.5..1861.3（框右缘 1862，advance 口径内 +0.7 px，看似合框）；**真墨 1458..1865 → 超出 3 px**。裁图 `render/crop-p4-saturday-title.png` 目视证实：框边从末字“程”中间切过，该字半在框内半在框外。
- 根在核心：core-en 同题同数（真墨亦 1865，-3 px）。教训：advance 口径会漏检此类缺陷，须以真墨为准。

### D9（中等，核心级）— P7 NEXT WEEK 承诺无法兑现
- 定位：P7 “NEXT WEEK · VOL.5預告”——“The certified results of the midterm election.”
- 事实：各州认证窗口为 **11 月 10 日–12 月 18 日**（Ballotpedia/NCSL；佐治亚决选若需则 12 月 1 日、州认证 12 月 18 日；密西西比 12 月 3 日宣布、阿拉斯加目标 11 月 25 日）。VOL.5 刊期 11 月 23–29 日，认证结果不可能齐全。P6 的条件式写法正确（“When the certified results are in, VOL.5 will report them”），P7 是 flat promise。
- 同句第二错（纸面内部亦不成立）：“The Ashes, second week in Perth”——按纸面自家赛程首场 11 月 21–25 日，珀斯并无“第二周”；第二场在布里斯班。即便不计 D5 的年份错，此句在纸面内部亦不成立。

## 已核对无问题（要点）

- 150 题：编号 1–150 连续（registry 逐项核对）；每页题数 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；级别 A2 62 / B1 66 / B2 22；与 KIT 一致。除 D1 外，答案键逐题核对题面、原文、图表、算术（254+162+19=435；254−218=36；P8 模型文 82 词）全部正确（另 4 组配对 P2 D 24–27、P4 C 56–59、P5 C 74–77、P8 F 141–144 均已按印版释义顺序逐题手验）。
- 机械门全过：occlusion 审计 0 flags（自检通过）；p8 extract 60/150 noted，compare CLEAN（keydiff [137, 138, 139, 150] = 翻译题 + 開放題，预期内；140 因简繁同形而不列入）；freeze baseline 8/8 byte-identical；freeze diff vs 核心：新增 CJK 776 字（与 KIT 一致）；印/网文字层逐页 token-multiset diff 0/0；keycheck registry vs text.md 0 不符；印版 P8 键 vs registry 仅 2 处 benign（139 空格断行差异、150 开放题截断显示）；OpenCC s2t 0 差异（registry + text.md + ABSTRACT.txt，全繁体）；MODEL 82 词。
- 外部事实逐项核实（见 GATE-LOG §事实核对）：选举数（众院 254/162/19、参院 20/13、2 未定 AK/MS、7 翻转州、5 州长翻转、选前 218–214/53–47、第 120 届国会 2027-01-03 就职、认证窗口 11 月 10 日–12 月 18 日、佐治亚决选日 12 月 1 日、密西西比常规大选无决选）与 AP 口径复核一致；Hunger Games（11 月 20 日上映、Zada/Fiennes/McKenna Grace、Lawrence 导演、2025 小说、50 届 2 倍 tribut、原声专辑 11 月 13 日）核对；I'm a Celebrity S26（11 月 16 日 21:00、Ant & Dec、Murwillumbah、因英格兰–西班牙国家联赛晚一天、Unpacked 在 ITV2、营员截稿未公布）核对；ATP 总决赛（11 月 15–22 日都灵、8 人名单 Zverev/Alcaraz/Shelton/Medvedev/Cobolli/Fils/Tiafoe/Jodar 与 Sinner 膝伤缺席完全一致）核对；英超第 11 轮（曼城–富勒姆 12:30、纽卡–阿森纳 17:30、利物浦–曼联周日 16:30）核对；NFL 第 11 周（小马–德州人 11 月 19 日 20:15 ET、维京人–49 人墨西哥城 11 月 22 日 20:20 ET、爱国者慕尼黑赛后轮空）核对；反欺凌周（11 月 16–20 日、主题 Break the Silence、Odd Socks Day 11 月 16 日十周年、约 800 万儿童、80%+ 学校、200+ 儿童定主题、ABA 主办、英格兰/威尔士/北爱）核对；世界儿童日（11 月 20 日、主题 “My day. My rights. My future.”、1989 年《儿童权利公约》）核对；日期/星期 18 项日历全对。
- 8 页目视：印版 8 页总览 + 网版 P1/P8 均已看图，除 D2/D3/D6/D7/D8 外无溢出、重叠、压页脚、图片与出处问题；网版与印版视觉一致。
- 引号：弯引号 “ 82 / ” 82 成对；U+2019 0；弯引号全在 Newsreader（拉丁）节点，CJK 字运行 0；唯一斜体对是 P1 每周一词 “midterm”（Newsreader 斜体，§1.1 本周词斜体）；P7 无斜体引号。SVG 比 text.md 多一对是 P3 图注 “Surprised!”（text.md 按惯例跳过图注）。
- 奶油框：32 盒逐盒实测，盒内末基线余 +4.5 至 +92.4 px（最紧为 P2 AND YOU? 盒 +4.5，末行中文、无降部，框内）；P7 工具盒盒内余 +48.5 px（墨水最低行 961，盒底 1008.2，余 +47.2 px，B2 句末行降部字母干净），B2 句翻译准确，无他版多词问题。
- 框题：全部 11 个奶油框题逐个 text_w + 真墨实测——除 D6/D8 外全部合框（最紧 P1 NUMBERS：advance 余 +1.5 px，真墨 1007..1407 余 +5.0 px，框内）；HAYMITCH'S GAMES 真墨余 +21、ODD SOCKS +28、HOW LONG? +136、TOOLBOX +107。
- §1.1：字体 Newsreader / Noto Sans CJK TC / Noto Serif CJK TC / UnifrakturMaguntia（刊头）/ DejaVu Sans（符号），合规；用色集合与核心完全一致（§1.1 外的色均为图表/地图内容色，核心共有）；P8 实测最小字号 10.12 pt ≥ 9.75 下限（见观察 O3）；家具分隔符全角空格（U+3000 141，核心 132）；· 计数 282 与核心完全一致；VOL.4 ×12、VOL.5 ×8、VOL.3 ×3，与核心一致。
- 金句：P7 8 句全部逐字出自本期正文，页码标注正确。
- ABSTRACT.txt：一行、繁体中文、无 ASCII 双引号（151 B）。

## 观察（非缺陷）

- O1 — P1 NUMBERS 框题极紧：advance 余 +1.5 px，真墨余 +5.0 px，框内，目视未碰线。
- O2 — P2 AND YOU? 盒盒内余 +4.5 px，末行中文、无降部，框内。
- O3 — KIT §3 “P8 min font 13.5 pt”写的是 SVG 属性 px 数而非渲染 pt；实测印版 P8 最小 10.12 pt（答案键块在 0.75 缩放组内），仍 ≥ §1.1 下限 9.75 pt，通过；仅 KIT 口径问题，非本版缺陷。
- O4 — P7 工具盒干净（见上）；B2 句翻译准确。
- O5 — P2 A 组说明“根據日期與時間”偏宽（本周 5 题全是日期、无钟点题），系核心模板通用措辞，非本版新错。
- O6 — 纸面内部张力（非缺陷）：35 席中 33 席已定、仅 AK/MS 未定，暗含佐治亚已定；P2/P6 的佐治亚决选句为条件式（“If no candidate wins…”），无直接矛盾；且实测 Ossoff 得票 59.0% 已过半，决选本不会发生。
- O7 — Q139 印出键“新國會將於2027 年 1 月開會。”与 registry“將於 2027 年”差一空格，属排版断行差异，义同；且印出版式合 §1.1“中文里的数字不加空格”。
- O8 — P7 “VOL.3 promised real letters from VOL.4”经核与 W46（VOL.3）P7 读者园地“VOL.4 起刊登收到的真實來信”一致，表述准确，非夸大。
- O9 — 印版 P8 键 vs registry 仅 2 处 benign 差异（见上）；p8 extract noted 集 60/150 与核心同集。

## 未独立再核实（低风险、已列出）

- Mike Johnson“不竞选新一届众议院共和党领袖”原话出处、众院两党领袖选举日期（11 月 10 日/11 月 18–19 日）；“How to Survive the Jungle”一次特别节目 11 月 15 日；ATP 决赛“不早于 18:00”；Lawrence 儿童照片日期 1912 年 2 月 19 日；P4“Day one is already sold out”。
- P6 图表“Governors flipped: 5”与正文一致；州长翻转 5 州（Georgia, Iowa, Nevada, Ohio, Texas）已与 AP 口径复核一致。

## 建议下一步（报协调员定）

1. 核心修 D1（registry 39/40 键互换 + 核心 P8 键）、D4 措辞、D5 Ashes 整版重写（年份）、D9 NEXT WEEK 改写，核心模板修 D2/D3 盒高、D6/D8 框题（缩短标题或放宽盒）、D7 SAY IT 英文行（缩短/换行/缩小字号或放宽盒）；本版随核心重出。
2. 重出后整版重渲染，本版从头再做一轮全量复校（proof2），直至一整轮零问题。
3. 工具缺口：occlusion 审计不覆盖奶油框题（BOXTITLE 只查有描边/填色框）与盒内末行漫出（D2/D3/D6/D7/D8 均由此漏检）；`creambox.py` 的 +45 px 窗口会把下块栏头当作盒内行，须逐行裁定——建议把“盒内末基线超出盒底”（x0≈盒内 inset 的行）本身判为溢出，并把框题真墨 vs 框界做进审计。
