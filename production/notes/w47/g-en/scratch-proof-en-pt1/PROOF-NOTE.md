# PROOF-NOTE — 2026-W47 en-pt（独立复校 proof1 · re-fanout #2 重建版）

- 版：`2026-w47-en-pt`（目标语 English，读者母语 Portuguese）
- 复校员：独立复校员（与建版者/fan-out agent 非同一人），2026-11-11
- 对象（`production/2026-w47/2026-w47-en-pt/`，开工前盘上 `sha256sum`+`stat` 核对，与任务单逐字一致）：
  - 印刷 `The-Lucerna-VOL4-en-pt.pdf` — 29,345,708 B，SHA-256 `3f6b415fa35195ca49605414b5a756a01f0457032cc5c6acc75075e49c221dad`
  - 网页 `The-Lucerna-VOL4-en-pt.web.pdf` — 2,418,233 B，SHA-256 `0252edc42a4981413c25067e8ed60bb5069994f86c10a4d25a0b8483e0846629`
  - `2026-w47-en-pt.text.md` — 54,123 B，SHA-256 `12b04ff13b12db5232d3114816f287c2d72a69df164e0273269409ef3148d545`
- 核心：`core-en`（盘上实为 en-zh-cn 命名文件）复核前后各测一次，未变：
  - 印 `b484e007e6e0e29a78ea3f81c412e9c27c45a7c2b317a9a6081a2f63eb416566`（41,407,278 B）
  - 网 `7277e32a96f26974efd68d5e27978e0f1570dd15222f29a060ecdf7dbd89d3f8`（2,804,271 B）
  - text `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b`（51,405 B）
  - 与 FANOUT-REPORT 所载一致。
- 本版来自 en re-fanout #2（`hidden_files/w47/scratch-fanout-en2/`）；第一轮 proof1 的文件已归档至本工作区 `proof1-first-build/`，本次结论与门禁为全新重跑，不复用旧结论。
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-pt1/`（`TMPDIR=<scratch>/tmp`；只在 goals 侧写；不 commit、不 push；未覆盖生产目录下任何文件）。

## 结论：(a) 定稿零缺陷

本版讲解层与核心继承层均无缺陷。第一轮 proof1 的两项核心级缺陷已由重建解决（见下），本次复校的全部机械门与人工核对均通过；三处“紧但装得下”的余量已逐项真墨实测并目视确认在内（见“紧余量记录”）。

### 第一轮缺陷的复验（均已解决，实测值在案）

**D1（原：Q39/Q40 答案互换，严重 · 核心级）——已解决，四方一致：**
- SVG 题面（`svg/p3-culture.svg`）：38. a tribute / 39. a mentor / 40. the arena / 41. a campmate；选项 a. a person who teaches and guides you（= mentor）/ b. a person chosen to take part in the Games（= tribute）/ c. a person who lives with you in the jungle camp（= campmate）/ d. the place where the Games are fought（= arena）。
- `registry.json`：39→a（`mentor = um mentor a`）、40→d（`arena = a arena d`），38→b、41→c；与 core-en registry 键逐字相同（`mentor=导师 a` / `arena=竞技场 d`）。
- `text.md` 答案：39→a、40→d；P8 提取键：38–41 = b/a/d/c。四方一致，正确答案 39→a、40→d。
- 配对题其余四组亦以 SVG 印刷字母逐组复核，全部正确：P2（24→b，25→c，26→a，27→d）、P4（56→b，57→c，58→d，59→a）、P5（74→d，75→a，76→b，77→c）、P8（141→b，142→c，143→d，144→a）。

**D2（原：P2 “DID YOU KNOW?” 盒末行出盒，轻微 · 核心级）——已解决：**
- 盒已加深：`y=833, h=325.5→352.5`，底边 `1185.4`；末行 `November 3.` 基线 `y=1171.1`，0.30em 下行余量 **+7.9px**；渲染卡像素实测末行墨水最末行 `y=1170`，距盒底 **15.4px**；裁片 `crops/p2-didyouknow-bottom.png` 目视该行完整在盒内，盒底线之下为下一栏头 `AND YOU?`。
- 同类旧观察（P1 SEARCHES 盒说明行在盒外）亦已解决：葡语行 `Interesse relativo, não números exatos.` 基线 `y=1244.0`，盒底 `1256.0`，下行余量 **+6.3px**，像素实测墨水最末行 `y=1246`（+10px）；裁片 `crops/p1-searches-bottom.png` 目视三行全在盒内。

### 本版 carry-forward 项复验（任务单点名三项，全部落地）

- **P5 ODD SOCKS 标题修复**：SVG 题头现为 `ODD SOCKS, IN NUMBERS　N.º`（`svg/p5-youth.svg`，x=106.0，y=2070.86，23pt bold）；源扫查 346.2px（预算 404.5，+58.2）；渲染卡真墨实测墨宽至 x=449，盒右界 510.5，**真墨余量 +61.5px**；裁片 `crops/p5-odd-title.png` 目视标题居盒内、余量宽裕。旧式 `Números` 在 text.md / SVG / registry 中均为 0 命中。
- **ABSTRACT 完整式**：一行葡语，753 字符，无 ASCII 双引号；含 Lucerna、VOL.4、150、A2–B2 全部命中；另含“resultados anunciados”“certificação 10 de novembro a 18 de dezembro”“16 de novembro”“20 de novembro”“21 de novembro”“4–1”全部命中；旧短式已不在盘上（`diff` 旧 ABSTRACT 仅一行整行替换）。
- **Q39→a / Q40→d Ashes 措辞**：见 D1 四方一致；另 Q46→A（`O primeiro Test das Ashes 2025–26: sexta-feira, 21 de novembro de 2025, em Perth`）、Q52→hosted、Q55→won、Q125→A（`A Austrália venceu as Ashes 2025–26 por 4–1`），registry / text.md / P8 提取三处一致。
- **Ashes 改写外核**（新回顾体事实，逐项网核，来源见 GATE-LOG §9）：系列 2025-11-21–2026-01-08、澳大利亚 4–1、首三 Test 珀斯/布里斯班/阿德莱德胜出后已保 Ashes、第四 Test 墨尔本英格兰 4 wickets 胜（近十五年首胜）、第五 Test 悉尼澳大利亚 5 wickets 胜、首 Test 珀斯两日完赛且为 1888 年以来按球数最短、珀斯体育场首办 Ashes Test、2021–22 未排珀斯——全部与 Wikipedia 2025–26 Ashes 词条 / Sky Sports 一致。星期核验：2025-11-21 周五、2026-11-21 周六、2026-11-22 周日、2026-11-19 周四、2026-11-16 周一、2026-11-20 周五、2026-11-03 周二、2026-11-26 周四，全部正确。
- **其余改动项**：Q82→B（254）、Q83→C（19）、Q84→A（33/35）、Q85→B（7 席）、Q86→A（5 州长）、Q87→C（254+162+19=435）均对 P6 图表题面逐项验算正确；Q46–Q51、Q60–Q63、Q100–Q111、Q112–Q119、Q120–Q132、Q133–Q136、Q137–Q140、Q145–Q149 均对题面/正文核对正确（详见 GATE-LOG §5）。
- **陈旧措辞清零**：`Ashes begin`、`Perth is winning!`、`second week in Perth`、已确认、`Confirmado em`、`foram decididos`、旧标题 `THE SENATE, IN NUMBERS` / `SATURDAY, NOVEMBER 21` 在 text.md / 全部 SVG / registry 中均为 0 命中；`anunciad*` 3 处，`verificados/confirmados` 0 处。

### 紧余量记录（紧但装得下，不构成缺陷，均已真墨实测+目视）

- P2 AND YOU? 盒：末行 `para a redação.` 基线 1539.85，0.30em 启发式报 −1.0px（与 de 同款假警报）；渲染卡真墨最末行 y=1544，盒底 1544.9，**真墨余量 +0.9px**；裁片 `crops/p2-andyou-bottom.png` 目视 `p` 下行笔完整在奶油盒内，分隔线在其下。这是全版最紧的一处。
- P6 HOW LONG? 标题：源 advance +8.9px，真墨 +8.5px（墨至 x=1854，盒右界 1862.5）；裁片目视标题未碰右界。
- P1 THE WEEK IN NUMBERS 标题：源 advance +13.6px，真墨 +13.5px。
- P1 SEARCHES 盒末行 +6.3px（0.30em 口径；真墨 +10px）；P2 DID YOU KNOW 末行 +7.9px（真墨 +15.4px）。

## 观察（不构成定稿阻碍，报协调员）

### 观察 1：构建方 freeze baseline 证据指向错误（流程问题，非本版缺陷）
- 构建方 `scratch-fanout-en2/fanout/pt/freeze-final/build-copy/` 内是 **en-pt 版目录**（含 `The-Lucerna-VOL4-en-pt.pdf`、葡语 content），不是 core-en；其 `freeze.log` 所载 8 个“core”哈希（p1 `16be1b38…` 等）实为重渲染的 **en-pt SVG** 哈希，与盘上 core-en SVG 的实测哈希（p1 `a9a8deaf…` 等）逐个不符。也就是说构建方那轮 freeze 证明的是“en-pt 版可自我复现”，并非“核心可复现”，KIT §3 “direct sha256 re-render vs shipped core SVGs: 8/8 MATCH”所引的证据不可作此证明。
- **我方已用正确路径独立重跑**：`freeze.py baseline --build core-en --core-svg core-en/svg`，8/8 逐字节一致，并以 `sha256sum` 直接复核盘上 core-en SVG（见 GATE-LOG §3）。freeze 门本身真实通过；请构建方修正其 freeze 调用路径（`--build` 须指 core-en），不要只改 KIT 文字。

### 观察 2：KIT §6 自查行沿用旧标题（KIT 文字问题，非版式缺陷）
- KIT §6 写 P2 栏头为 `"THE SENATE, IN NUMBERS · O Senado"`；SVG 实测与渲染均为新标题 `"SENATE IN NUMBERS　O Senado"`（源扫查 367.2px，+37.3）。§4 的框题表已是新标题，唯 §6 这一行是旧文案残留。建议构建方把 §6 该行改写为新标题；不影响版面，不须重渲染。

### 观察 3：KIT §3 “P8 min font 13.5 pt”仍是 SVG 单位（沿用第一轮观察 3）
- PyMuPDF 实测印/网两版 P8 最小字号均为 **10.12pt**（SVG 13.5 单位 ×0.75），SOP §1.1 下限 9.75pt（PyMuPDF 口径），10.12 ≥ 9.75，门通过；其余各页最小 11.62pt。KIT 所写 “13.5 pt”未注明是 SVG 单位，建议补写单位口径。

### 观察 4：两处跨栏断行（核心同款结构，文字完整，第一轮观察 4 继续沿用）
- P5 “D PRESENT CONTINUOUS”栏头 + instruction 前半在中栏底部，后半与 78–81 题在右栏顶部；P7 不规则动词句在左栏底部断开、尾行在中栏顶部。文字完整，无丢失；是否改排版由核心定。

### 观察 5：“next Sunday”冻结规则无适用对象
- 在 core-en、`2026-w47-en-pt`、`tools/tables.py` 中 grep `next Sunday` 均为 0 命中，本版无适用对象，不套用旧行号。

### 观察 6：D5 字体（只记录数量，不判）
- `pdffonts`：印版 41 个字体对象、网版 41 个字体对象，全部 embedded + subset；字体族：NotoSansCJKsc（Regular/Bold）、UnifrakturMaguntia、Newsreader（Regular/Italic/Bold）、NotoSerifCJKsc Regular、DejaVuSans。数量已记录（见 GATE-LOG §11），不作定稿判断。

## 150 题手验方法（说明口径，非抽查）

- 三源一致性：text.md 答案 150/150 行（无缺号、无重号）与 `registry.json` 逐题比对 key / level / type **0 不符**；registry 键与 P8 提取键 149/150 精确一致 + Q150 短标签例外（预期）；registry 键与 core-en 145/150，仅 137–140、150 五个读者语键不同（预期）。
- 变动项全量手验：与第一轮 proof1 已验备份逐字节 `diff`，变动只发生在 registry 8 条（Q39/40/46/52/55/82/84/125）、text.md 31 处、SVG 文本（P1/P2/P4/P5/P6/P7/P8，仅预期字符串；P3 SVG 逐字节相同）——变动的每一题均对 SVG 题面 + 正文 + 答案键逐项验算（Q39/40 四方、Q46/52/55/125、Q82–87 图表读数、Q47–Q51、Q60–Q63、Q100–Q111、Q112–Q119、Q120–Q132、Q133–Q136、配对五组），并对外核 Ashes 新事实。
- 未变动项：与已验备份逐字节相同（registry 其余 142 条、text.md 其余行、P3 SVG 全文），一致性门全过；另抽查配对五组 SVG 字母与 P8 答案块关键行（Q60 “England lost 4–0 in 2021–22.” 以 SVG 原文复核，非凭渲染小图判读）。

## 已核实无问题的项（全量核对，见 GATE-LOG.md）

- **机械门全绿**：occlusion 0 flags（自检 6 类 planted 各命中 1 次，clean 对照静默；core 0，NEW vs core 0）；p8 extract 60/150（与核心同集合），compare CLEAN，keydiff [137, 138, 139, 140, 150]（预期）；freeze baseline 8/8（正确路径重跑），diff 新增 CJK 仅 9×U+3000；印/网 token 多重集差分 0/0（各 8,862 token、2,532 distinct；无 layout 提取 49,271 字符；逐页字节一致 8/8）；网 PDF 在 scratch 副本重渲染，文字层逐字节一致（2,418,228 B vs 发货 2,418,233 B，差 5 字节为 fontTools 时间戳，符合铁律）；keycheck 150/150；P8 最小字号 10.12pt；框题源扫查 12/12、SVG 扫查 18/18 全 fit；creambox 全版 32 盒：除紧余量记录外全部 inside-only 余量为正；check_s11 ALL PASS；家具 `tables.py furniture pt --target en --week 2026-W47` 与本版 badge / footer / `Página {n} de 8` / `Nota — ` 逐字一致，VOL.4。
- **引号/撇号/禁词**：弯双引号 “ ” SVG 82/82、text.md 81/81，各自成对；« » text.md 4/4、SVG 2/2，成对；无直引号；撇号 ASCII（构建归一化，SVG 43 处、text.md 40 处）；U+2019 0 处；孤标点 0；禁词（SOP / proofread / geometry audit / cover / lint / placeholder / TODO / XXX / Lorem）可见文本 0；CJK 仅 U+3000 分隔符 141 处（SVG 可见文本），text.md 0 处 CJK。
- **家具与 ABSTRACT**：见上；ABSTRACT 完整式已核（见 carry-forward 项）。
- **目视**：印版 8 页逐页渲染目视 + 网版 P1/P8 渲染目视；除紧余量记录的三处外，无溢出、重叠、压页脚、图片与出处问题；8 张图片均有 PD/CC0 授权记录（`assets/CREDITS.md`）；旧版逐页像素对比：P3 0px 全同，其余各页变化区域恰为预期改动（P1 1.0%、P2 0.8%、P4 11.3% Ashes 重写、P5 0.2% 仅标题与 THE JUNGLE, TOO 两处、P6 812px 仅桥接词、P7 6.2%（Try-it +1 行、下游统一下移 35.7px；NEXT WEEK 原位改写）、P8 1.4% 答案块重排）。
