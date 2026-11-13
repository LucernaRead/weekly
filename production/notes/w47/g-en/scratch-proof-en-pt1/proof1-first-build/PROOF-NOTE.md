# PROOF-NOTE — 2026-W47 en-pt（独立复校 proof1）

- 版：`2026-w47-en-pt`（目标语 English，读者母语 Portuguese）
- 复校员：独立复校员（与建版者非同一人），2026-11-11
- 对象（`production/2026-w47/2026-w47-en-pt/`）：
  - 印刷 `The-Lucerna-VOL4-en-pt.pdf` — 29,345,286 B，
    SHA-256 `50484ca9c0ef23231977066164281455491180ef7843efc8d266805cdcc5ce0e`
  - 网页 `The-Lucerna-VOL4-en-pt.web.pdf` — 2,381,728 B，
    SHA-256 `c150c65509fa722ef17d54f0c823878c7f958fcca6aaaae879e10c36e7430071`
  - `2026-w47-en-pt.text.md` — 53,549 B，
    SHA-256 `329a027375eda3fe73abf2ed27819456abb8a57ad4849ec3e342db6632d004ba`
  - 开工前已以盘上 `sha256sum` 核对完整 SHA 与字节数，与任务单一致（见 GATE-LOG.md）。
- 核心：`core-en` 已定稿；本复校只复校、不改任何源文件、不重建、不 commit、不 push、不动 `tools/`。

## 结论：(b) 缺陷清单 — 本版不能直接定稿

**en-pt 讲解层本身没有发现缺陷。两项真实缺陷的根都在 core-en（几何与答案键与核心逐字节一致），按规则记为核心级候选报协调员，绝不碰核心。** 在核心修好并重渲染、fan-out 重新跑通全量校对之前，本版不应定稿。

### 缺陷 1（严重 · 内容错 · 核心级）：P3 配对题答案 Q39 / Q40 互换

- 位置：P3 “C · THE WORDS”（38–41 题）；印刷答案见 P8 ANSWERS “— Página 3 —”行：`38. b · 39. d · 40. a · 41. c`。
- 印刷题面（P3 SVG 与渲染卡均已核对）：
  - 词：38. a tribute　39. a mentor　40. the arena　41. a campmate
  - 释义：a. a person who teaches and guides you（= mentor）　b. a person chosen to take part in the Games（= tribute）　c. a person who lives with you in the jungle camp（= campmate）　d. the place where the Games are fought（= arena）
- 正确答案应为：38→b，**39→a，40→d**，41→c。
- 印刷答案为：38→b ✓，**39→d ✗，40→a ✗**，41→c ✓。Q39 与 Q40 正好互换。
- 核实路径：`p3-culture.svg` 原文顺序 + 渲染卡 P3 目视 + `registry.json`（39=d，40=a）三方一致，错误不在导出环节。
- 根在核心：`core-en/registry.json`（39=d，40=a）与 `core-en` text.md 答案（39. d，40. a）完全相同，核心 P3 SVG 释义顺序亦与本版一致。**修法在核心**：改核心 registry 39→a、40→d，改核心 text.md 答案，重渲染核心，各 fan-out 重新跑 P8 门与全量校对。本版不动。
- 其余四组配对题已逐组以 SVG 印刷字母核对，全部正确：P2（24→b，25→c，26→a，27→d）、P4（56→b，57→c，58→d，59→a）、P5（74→d，75→a，76→b，77→c）、P8（141→b，142→c，143→d，144→a）。

### 缺陷 2（轻微 · 版式 · 核心级）：P2 “DID YOU KNOW?” 盒末行溢出盒底

- 位置：P2 右栏奶油盒（`x=1439.5, y=832.9, w=422.5, h=325.5`，底边 `y=1158.4`）。
- 盒内第三条末句分三行：`The House has 435 seats — and every`（y=1110.02）／`one of them was on the ballot on`（y=1140.55）／**`November 3.`（基线 y=1171.08，底边之下 12.7px）**。
- 实测：渲染卡 P2 目视可见 `November 3.` 落在盒外白地上，与盒内前两行断开；像素核查：该行字形顶约 y=1156，盒底 1158.4——字顶 2px 压盒底线，其余全部在盒外。这是 occlusion 审计的盲区类缺陷（文字未被遮盖，只是出了盒），与任务单点名的 de 家庭工具盒漫出同类。
- 根在核心：`core-en/svg/p2-life.svg` 的盒矩形与三行文字坐标与本版逐值相同。**修法在核心**：盒高 325.5→约 340，或重排末句；重渲染核心后各 fan-out 复验。
- 同类全版扫查（32 个奶油盒，见 GATE-LOG.md “creambox”）：仅此一处盒内句子跨过盒底。**P7 工具盒干净**：末行基线 y=959.68，距盒底 1008.21 有 42px 以上余量，盒底像素带无墨水（见裁片 `crop-p7-toolbox-bottom.png`）。
- 相近项（已裁定不是本版缺陷，见“观察 1”）：P1 SEARCHES 盒葡语说明行亦在盒外，但核心亦然，见下。

## 观察（不构成定稿阻碍，报协调员裁定）

### 观察 1：P1 SEARCHES 盒说明行在盒外（核心同款，妆容性）
- 葡语行 `Interesse relativo, não números exatos.`（基线 y=1274）在 SEARCHES 盒底边 1256 之下 18px，落在盒外白地上；核心同位置是中文行 `相对热度示意，非精确搜索量。`（同 y=1274，同盒底）。渲染图上读作盒下 caption，可读、无遮挡、无断句。本版只是忠实复现核心几何，**不算 en-pt 缺陷**；是否要把该行收进盒内，由协调员在核心定。

### 观察 2：KIT §4 框题宽度数字无法用 `svglib.text_w` 复现（KIT 计量口径问题，非版式缺陷）
- KIT 称 10 个框题“measured at 23pt with svglib.text_w, CW 422.5”，如 THE SENATE 408.4、SATURDAY 379.4、HOW LONG? 379.6。
- 我方复测（`svglib.text_w(t, kind, True, 23)`）：serif 得 462.5 / 432.5 / 408.3，sans 得 425.8 / 397.0 / 395.6，均与 KIT 数不符；且 ERROR CLINIC / READERS' CORNER / AN EXAMPLE LETTER 在 SVG 里实际是 28pt / 25pt / 25pt，并非 KIT 所称的 23pt。
- **真墨实测（渲染 PNG，框题墨 vs 自身框界）全部装得下**：THE SENATE 墨宽 403px、余 1.0px；ODD SOCKS 402px、余 1.5px；SATURDAY 401px、余 3.0px；HOW LONG? 395px、余 8.0px；其余余 17–175px；P7 各栏头余 38–139px。occlusion 审计 BOXTITLE 0 flags 亦证实无出框。三个最紧的（1.0 / 1.5 / 3.0px）已目视，字未碰框线。
- 结论：版式无缺陷；建议 KIT 补写计量所用的 kind/字重/字号，否则该表不可复核。

### 观察 3：KIT “P8 最小字号 13.5pt” 是 SVG 单位，PDF 实测 10.12pt（门仍过）
- PyMuPDF 实测印版 P8 最小字号 **10.12pt**（SVG 13.5 单位 × 0.75 px→pt；印/网两版同值）。SOP §1.1 的 9.75pt 下限是 PyMuPDF 口径（W46 实测分布 9.0–10.9pt、众数 9.75pt），10.12 ≥ 9.75，**门通过**。建议 KIT 写明单位，避免把 SVG 单位当 PDF 字号。

### 观察 4：两处跨栏断行（核心同款结构，文字完整，无丢失）
- P5 “D PRESENT CONTINUOUS” 栏头 +  instruction 前半 `Reescreva no presente contínuo (coisas a` 在中栏底部，`acontecer agora).` 与 78–81 题在右栏顶部；核心同栏头亦在中栏底部（y=2438），结构相同。
- P7 不规则动词句 `Irregular verbs in this issue: win → won, lose → lost, beat → beat, choose` 在左栏底部，尾行 `→ chose, run → ran.` 在中栏顶部；文字完整。
- 均为断行生硬、无文字丢失；是否改排版由核心定。

## 已核实无问题的项（抽样之外的全量核对，见 GATE-LOG.md）

- **150 题答案键全量核对**：text.md 答案 150/150 行，题号连续无缺重；与 `registry.json` 逐题比对 key / level / type **0 不符**；各页题数 10/17/18/18/18/18/12/39；A2 62 / B1 66 / B2 22；与 KIT 一致。
- **单选题**：41 道 MC + 6 道图表读数 + P1 4 道快问，键控选项逐项对题面与正文核对，全部正确（Q82–87 算术：254+162+19=435；Senate 20+13=33/35；7 翻转；5 州长）。
- **填空/转换/完形/对话/翻译**：Q1–6、11–19、34–37、42–45、52–55、60–63、70–73、78–81、94–99、100–111、112–119、133–136、145–149 逐题验算，全部正确（Q108 订正 “won”、Q109 “continued”、Q110 “more than”、Q111 “whether” 均合语法与正文）。
- **外部事实**（逐项网核，来源见 GATE-LOG.md）：
  - I'm a Celebrity 2026：11 月 16 日周一 21:00 ITV1/ITVX，Ant & Dec，Murwillumbah，Unpacked 在 ITV2；因 11 月 15 日周日 ITV 转播欧国联西班牙–英格兰而比惯常周日档晚一天——与正文逐字相符。
  - Anti-Bullying Week 2026：11 月 16–20 日，主题 “Break the Silence”，Odd Socks Day 11 月 16 日、十周年（2017 年始），ABA 组织（英格兰/威尔士/北爱尔兰），约 800 万儿童、逾 80% 学校参与，主题由 200 多名青少年参与选定——与正文逐字相符。
  - Hunger Games《Sunrise on the Reaping》：2026 年 11 月 20 日周五上映，Joseph Zada 演 16 岁 Haymitch，McKenna Grace 演 Maysilee Donner，Ralph Fiennes 演年轻 Snow，Francis Lawrence 执导，原著 Suzanne Collins 2025 年 3 月 18 日出版，第 50 届、第二次四分之一大赛、 tributos 翻倍，Woody Harrelson 演年长 Haymitch，专辑 11 月 13 日——全部相符。
  - Ashes：首 Test 11 月 21 日珀斯；Cummins 背伤缺阵、Hazlewood 腿筋伤缺阵、Steve Smith 代队长、Scott Boland 顶替——全部相符；英格兰上次在澳赢系列 2010–11、2017–18 与 2021–22 均 0–4 落败、2023 在英格兰打平——相符；印度 2024 年 11 月在珀斯首 Test 赢 295 分——相符。
  - ATP Finals 2026：11 月 15–22 日都灵，Sinner 膝伤缺阵、2024–2025 两届冠军，八人名单 Zverev / Alcaraz / Shelton / Medvedev / Cobolli / Fils / Tiafoe / Jodar 与官方一致（含 Jodar 以第九名递补），两组各四人——相符。
  - 英超：11 月 21 日周六 Man City–Fulham 12:30、Newcastle–Arsenal 17:30；11 月 22 日周日 Liverpool–Man Utd 16:30；国际比赛日后复赛——相符。
  - World Children's Day：11 月 20 日周五，主题 “My day. My rights. My future.”，UNICEF 主导，1989 年 11 月 20 日通过《儿童权利公约》——相符。
  - 星期核验：11 月 3 日周二、11 月 8 日周日、11 月 9 日周一、11 月 16 日周一、11 月 20 日周五、11 月 21 日周六、11 月 22 日周日、11 月 26 日周四（11 月第四个周四感恩节）、12 月 1 日周二（佐治亚次轮，投票后四周）——全部正确。
  - 选举数字为本期情景设定（以 11 月 8 日美联社 call 为口径、注明待认证、VOL.5 报认证结果），内部自洽：435=254+162+19，多数 218，参议院 20+13=33/35，7 席翻转（Iowa、Kansas、Maine、North Carolina、Ohio、South Carolina、Texas），5 州长翻转（Georgia、Iowa、Nevada、Ohio、Texas），选前众议院 218–214、参议院 53–47。真实性无法对尚未发生的选举外核，已按 SOP 要求标注口径。
  - 其余：Rousseau《Surprised!》（1891）未出法国画丛林；W. G. Grace 照（Herbert Rose Barraud，1880 年代末）；Lawrence 童工 1912 年 2 月 19 日纽约游行（Bain News Service，LoC）；Samuel Johnson 肖像（Reynolds，1772）；国会图书馆主阅览室（Carol M. Highsmith）——与图注一致。图片 8 张均有 PD/CC0 授权记录（`assets/CREDITS.md`）。
- **引号/撇号**：弯双引号 “ ” 各 81，成对；每页各自成对；« » 各 4，成对；无直引号；撇号为 ASCII `'`（构建归一化，与核心一致，核心 42 处、本版 40 处）。
- **禁词**：可见文本中 SOP / proofread / geometry audit / cover / lint / placeholder / TODO / XXX / Lorem / 桥接 均为 0（SVG base64 与葡语词 `todo` 的误报已排除）；CJK 仅 U+3000 分隔符 141 处 + 刊头蛾标「三色蛾」1 处（核心亦同）。
- **印/网同一**：两 PDF 各 8 页；pdftotext token 多重集差分 0/0（各 8,753 token、2,513 distinct）；P1、P8 网版渲染与印版卡目视一致。
- **家具**：`tables.py furniture pt --target en --week 2026-W47` 输出与本版 badge / footer / 页码行 / gloss 前缀逐字一致，VOL.4；报头冠词 The Lucerna；刊别 “SEMANÁRIO EM INGLÊS VOL.4 ELEIÇÕES SELVA CINEMA”；页脚 “Página {n} de 8” 八页齐全；栏头分隔用全角空格（SVG 内 `THE BIG STORY　Manchete`），`·` 只出现在 gloss 行与选项分隔（与核心一致）。
- **ABSTRACT.txt**：一行、葡萄牙语、无 ASCII 双引号，含目标语、真实主题与题数。
- **目视**：印版 8 页卡（cards/p1–p8）逐页看过 + 网版 P1/P8 渲染看过；除缺陷 2（P2 盒外行）与观察 1（P1 盒下说明行）外，无溢出、重叠、压页脚、图片与出处问题；P7 栏头、工具盒、读者园地、示例信、NEXT WEEK 均干净。

## 需协调员裁定的事

1. 缺陷 1、2 的修复**必须在 core-en 做**（改核心 registry/text.md 与盒高，重渲染核心），再由各 en fan-out 重新跑 P8 门与全量 proof1。本版不改。
2. 观察 1 是否收入盒内，由核心定；观察 2、3 的 KIT 口径请建版者在 KIT 补写计量方法。
3. 本版 en-pt 讲解层零缺陷：核心修好重渲染后，本版只需重跑 fan-out + 本复校员再做一轮全量 proof1（SOP §8.4 循环规则），即可定稿。
