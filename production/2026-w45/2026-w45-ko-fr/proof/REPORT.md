# 独立校对报告 — Lucerna Weekly W45 KO×FR（韩语目标 × 法语读者）

**结论：ZERO PROBLEMS**

校对员：独立校对（只校对，不改源码，不宣布上架，不派生下级代理）。本次为全新完整校对，不沿用任何前人结论；上一位校对员未留下报告与证据目录，本报告与证据全部由本次重测产生。
未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心/W43 目录（只读对照）、未清理共享 scratch 目录。构建树脚本一律未在原地运行：基线复现用 `tools/freeze.py baseline`（其 `--out` 指向本科对 scratch）、登记展开与 wrap-spy 均在本科对 scratch 内拷树并重定向 OUT 后重跑；交付目录与核心目录在校对中零写入（见 §11 哈希 diff）。

## 0. 开工查重

- 在途进程逐进程查 cwd：仅 2 个在途进程，分别为 fr-en 构建（cwd `/tmp/fr-en-webfix` 相关）与 ko-es 构建（cwd `hidden_files/weekly-report-w45-ko-es-build`），均与 ko-fr 树无关，**不构成 stand down**。无任何 cwd 属于 ko-fr 树的在途写盘。
- ko-fr 交付物最后 mtime 2026-10-28 03:50:19 UTC（WEEKLY-KIT.md），开工复查时（03:52:37 UTC）已静默 138 秒（>120 秒），安全开工。
- 交付物与构建员声称值逐一核对一致（独立实测，非采信）：印刷 PDF `Lucerna-VOL2-FR.pdf` 32,587,981 B，sha256 `2fc4e410d120eba3563e9a7809343a87e0610da5b9d9774a44d9754976ccacaa`，8 页；网页 PDF `Lucerna-VOL2-FR-web.pdf` 3,565,743 B，sha256 `4773a934add411954d54dfe0e48cad54a5dba88cd984d1037d9982611594687a`，8 页；SVG×8、卡片×8（均为 1950×2700 RGB）齐全。

## 1. 冻结门禁

- **核心基线 8/8 逐字节**：`tools/freeze.py baseline`（核心构建树 `hidden_files/weekly-report-w45-ko-build`，输出重定向至本科对 scratch）复现核心 SVG 8/8 byte-identical；运行前后核心重哈希无变化；构建树内 `core-baseline-sha256.txt` 与本科对实测核心哈希逐一相符。
- **韩语正文零删失**：`tools/freeze.py diff`（核心 SVG vs 分版 SVG，逐页文本多重集 + CJK 多重集）：
  - 新增 CJK 字符：P1–P7 均为 0；**P8 仅 2 字：`절` +1、`기` +1**，与构建员声称一致。
  - 逐页增/删串：P1 +21/−20、P2 +39/−36、P3 +29/−28、P4 +23/−21、P5 +33/−31、P6 +17/−15、P7 +40/−36、P8 +175/−167。
  - 逐字核实该 2 字：分版 P8 第 104 条印刷行（x=989, y=2222.77）为 `104. A — 절기 = les 24 divisions de l'année`；`절기` 一词在分版 P7 与核心 P7 各出现 2 次（P7 A2 词框第 104 题题干 `절기는 무슨 뜻이에요?` 的词头），即该 2 字是 **P7 习题自身韩语词头的引用**，与 ko-pt 先例同类，不是未本地化残留、不是新增目标语正文。裁定：冻结成立。
  - 纯韩语删串（删串含 Hangul 但不含 Han 表意字）全量核查：仅 3 类——各页页码行 `제 N 면 / 총 8 면`（家具，改为 `Page N sur 8`）、P1 版次行 `한국어판 · VOL.2 · 입동 · 단풍 · 김장`（改为法语版次行，主题词 `입동 · 단풍 · 김장` 原样保留）、P7 句式片段 `〜까지예요?」`（改为 `〜까지예요? »`，引号样式本地化，韩语本身保留）。其余删串均含中文讲解层（被法语讲解层替换）。**无韩语正文删失。**
- **P7 词框定义句逐字冻结**：P7 删串中含韩语者逐条核查，全部是中文讲解行、法语化后的栏目标题/披露句、或句式说明的中文部分；A2/B1/B2 三栏韩语定义散文无一被删；glossline 仅本地化（`남다 = rester · 바로 = exactement.`、`본격적 = vraiment, pleinement · 나다 = passer,` 等，韩语词头冻结、法语释义）。P7 定义句冻结成立。
- **中间层术语 0**：该术语在交付 SVG 全文、构建代码（`hidden_files/weekly-report-w45-ko-fr-build/*.py`）、KIT、ABSTRACT 中均为 0 命中。交付 SVG 全版 Han 表意字（U+4E00–U+9FFF）= 0（核心为 2136，全系中文讲解层，已清零）。
- **刊头无冠词**：三方实测刊头均为 `Lucerna` 裸词（168pt, y=262），无冠词；SVG 全文 `Le Lucerna` 0 命中（KIT 内 1 处仅为否定句自述，见 §10 非阻塞观察）。

## 2. P8 比较（显式双路径，`--total 150`）

工具版本（实测 SHA，须注明）：当前 `tools/p8.py` = 新版 `96fc2cfe51d3dcfa44cc87ec63052b98b2f9b27462703d8226815046eccc0ca9`（破折号分支已验证 TRUSTED）。本次校对全部使用该当前版本；KIT 中“任务开始时为旧版、新版未采纳”的段落已滞后于当前 canonical 工具状态，纸面结论不受影响（见 §10）。

| 检查 | 实测 |
|---|---|
| `compare --core-p8 … --edition-p8 … --total 150` | **CLEAN**，核心 150 noted / 分版 150 noted，missing []、extra_count 0、uncertain []、keydiff **[137, 138]** |
| 登记 keydiff（本科对 scratch 重跑，见 §8） | **[137, 138, 150]**，与任务描述一致 |
| 键流编号行 | 1–150 各出现恰好一次（键流区编号起始行 150 条，唯一 150 个，重复 0、缺失 0） |

- **#137 真 E 区改向（印刷行直查）**：核心 `137. 11月7日是立冬。 — 对照第 1 版`（x=1451, y=1955.09）→ 分版 `137. Le 7 novembre, c'est l'Ipdong. — Voir page 1`（x=1451, y=2044.40）。登记键：核心 `11月7日是立冬。` → 分版 `Le 7 novembre, c'est l'Ipdong.`，注释 `Voir page 1`。习题干为韩语 `11월 7일은 입동이에요.`（分版 P8  exercise 区可查），法语键为合法重定向，非伪影。
- **#138 真 E 区改向（印刷行直查）**：核心 `138. 离高考还剩 12 天。 — 对照第 5 版` → 分版 `138. Il reste 12 jours avant le Suneung. — Voir page 5`（x=1451, y=2073.63）。登记键：核心 `离高考还剩 12 天。` → 分版 `Il reste 12 jours avant le Suneung.`。习题干韩语 `수능까지 12일이 남았어요.` 可查。
- **#139/#140 键逐字节相同**：核心与分版印刷行键均为 `특별 조치는 11월 19일에만 적용돼요.`（#139，注释 `Voir page 6`）与 `저는 토요일에 내장산에 단풍을 보러 가요.`（#140，注释 `Voir page 3`），无 keydiff。
- **#109 无伪影（印刷行直查）**：核心 `109. 기준 — 日期不同因标准不同（3版）`（x=989, y=2308.82）→ 分版 `109. 기준 — Les dates diffèrent car les critères diffèrent (page 3)`（x=989, y=2368.91）。破折号式 `N. key — note` 下两版键均为 `기준`，逐字节相同；工具 keydiff 不含 109，新版正确。
- **#150 排除正确（印刷键 = 核心）**：两版印刷键均为 `✓`（核心 `150. ✓ 范文见本版 H 区（157 字）`，分版 `150. ✓ Modèle dans la section H de cette page (157 caractères)`，x=1451）。登记键差异（核心 `(开放题，范文如下)` vs 分版 `(question ouverte — modèle ci-dessous)`）属于 H 装置行本身，p8 工具正确排除 150，工具 keydiff [137, 138] 与登记 keydiff [137, 138, 150] 的差值恰为该装置行。排除成立。
- **P8 注释语言纯度**：登记注释 150/150 已变更（相同编号段 key+note 全相同 = 0 条），无未译注释残留；注释中 Han 表意字 = 0；含 Hangul 的注释 25 条，逐条核查均为**目标语词头 + 法语释义**的既定格式（如 #25 `김장=le kimchi de l'hiver a`、#57 `Passé de 이기다 : 이겼어요`、#104 `절기 = les 24 divisions de l'année`、#141 `입동=le début de l'hiver a`），且全部词头均在核心渲染中存活（§1 冻结词头引用类），不是跨族残留；注释中无德语/西班牙语/中文等他族残留（`Voir page` 仅见于 #137–#140 与 #109/#150 的法语注释内）。P8 注释纯法语（讲解层）裁定成立。
- P8 组分隔符 8 个（`— 제1면 —` … `— 제8면 —`）齐全、韩语冻结；P8 带副行韩语-only（`제8면 · 이번 주의 큰 시험 + 모든 답`）；P8 头 `답 · Réponses — classées par page, cherchez le numéro` 与右线 `Chaque réponse avec une courte note en français · ✓ = exercice à texte modèle` 在位。

## 3. Gloss（渲染 · 切分逐项重测 — 口径明示）

**口径问题与裁定**：三组数字口径不同，不可直接混比——构建员 `24/26/28/6/0` 是**按内容文件**（content12/content34/content56/content7/content8）；ko-de 校对 `5/19/16/10/16/12/6` 是**按渲染页**（P1–P7，P8 为 0 未列出）；ko-fr 构建员 `24/26/28/6/0` 同样是按文件。本校对两种口径均独立重测，**两版在两种口径下均等于核心**：

- **口径 A（按文件，AST 常量串法）**：仅统计 `gloss()`/`glossline()` 常量字符串参数，按 `·` 切分。核心 = 分版 = content12 24、content34 26、content56 28、content7 6、content8 0，**合计 84**。content8 的 1 处 `glossline` 为 f-string 写作题指令行（`쓰기 문제예요 …`，不含 `·`，非 gloss 词条），AST 法正确排除为 0；本科对初版行扫描曾误计该行为 P8 1 项得 85，已用 AST 法纠正并说明原因。
- **口径 B（按渲染页，p.save 分段法）**：同一组调用按 `p.save` 分段映射到渲染页。核心 = 分版 = **P1 5、P2 19、P3 16、P4 10、P5 16、P6 12、P7 6、P8 0，合计 84**（content12 24 = P1 5 + P2 19；content34 26 = P3 16 + P4 10；content56 28 = P5 16 + P6 12；content7 6 = P7 6）。逐项词头渲染存活核查：两版 8 页缺失均为 0（含 P4 `하나가 되다` 类跨行断词头在去空白拼接后存活）。
- gloss 前缀 `Note — ` 全版在位；法语 gloss 形为 `词头 = 法语释义`，与 W43 ko-fr 一致。

## 4. 金句（8 句全版频次，SVG 全文去空白拼接重测）

P7 金句行为韩法双行（韩语原句行 + 法语译句行 + 页签 `(N면)`），韩语原句仍在 P7，频次与核心逐页一致：

| 句 | 频次 | 分页（核心 = 分版） |
|---|---|---|
| 11월 7일은 입동이에요 | 5 | P1×3、P7×1、P8×1 |
| 절정에 가까운 주말이라고만 말할 수 있어요 | 2 | P1、P7 |
| 김장은 겨울 내내 먹는 김치를 담그는 일이에요 | 4 | P1、P2×2、P7 |
| 수능까지 17일 남았어요. 오늘이 D-17예요 | 2 | P2、P7 |
| 낮은 길은 더 늦게 물들어요 | 2 | P3、P7 |
| KIA 타이거즈가 LG 트윈스를 3연승으로 이겼어요 | 2 | P4、P7 |
| 온 나라가 수험생을 응원해요 | 2 | P5、P7 |
| 날짜를 먼저 보세요 | 2 | P6、P7 |

频次 = 核心（5/2/4/2/2/2/2/2），每句均在其页签页出现（P7 法语译句行如 `Le 7 novembre, c'est l'Ipdong. (1면)` 等 8 行齐全）。

## 5. 几何门禁（输出全文存于证据文件，未截断）

- **Canonical `tools/occlusion_audit.py`**（自检 6 类全触发，`{'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}`，干净对照静默）：分版 0 flags、核心 0 flags、**NEW vs 核心 0**。
- **ADVANCE 全页右缘扫描**（内框 x=1910，锚点修正版：`text-anchor=end/middle` 按锚点计 advance 终点；初版忽略锚点的扫描曾误报 37 旗，已纠正）：分版与核心最差 advance 终点均为 **1885.0**（P1 日期行），flags 0。
- **全页框线扫描**（锚点修正真墨迹 vs 全部 stroked rect 边框/横线，页脚规则 y=2580 豁免）：分版 0、核心 0。
- **同基线墨迹碰撞**（0.6px 容差，锚点修正版）：分版 0、核心 0。
- **P6 图表标签基线锚定墨迹覆盖**（getmetrics 基线锚定法：`getmetrics` ascent/descent 定框、仅计文本之后绘制的 rect；本科对初版误计单元格底色得 100%，已纠正为仅后绘 rect；解析用非贪婪属性正则，12 标签全部命中，规避构建员所述贪婪正则 bug 类）：12 标签全部 **0.0%**（门禁 <30%），分版 = 核心。标签：`구분`、`이번 주 (11월 2~8일)`、`시험 날 (11월 19일)`、`날짜 세기`、`D-17 ~ D-12`、`D-데이`、`분위기`、`카운트다운`、`시험 당일`、`특별 조치`、`없어요 (평상시)`、`있어요 (10시 출근 등)`，基线 y=1303/1355/1407/1459。
- **韩语孤儿扫描**（本科对 scratch 内 wrap-spy 重跑：943 条记录、535 条去重，与构建员 `orphan-wrap.log` 逐条相同；且 scratch 渲染 SVG 与交付 SVG 8/8 逐字节相同，日志与交付渲染对应）：
  - 句中切分（上一行尾与下一行首拼成同一韩语词节）：0；其中尾 ≥3 音节：**0**；尾 1–2 音节：0。
  - 行首禁则（kinsoku 收束标点 。、，．！？；：）」』》】 开头）：wrap 日志 0；渲染行窗口扫描（同列相邻行 dy 10–45，分版 655 对、核心 632 对）：**0**。
  - `·` 引导续行 8 条（分版）vs 4 条（核心）：均为 gloss/选项分隔符引导的续行（如 `· 식탁 = table à manger.`、`· C. 11월 28일`），分隔符类续行，非 kinsoku 违规；分版多 4 条源于法语 gloss 更长致换行更多。不构成缺陷。
  - 孤立末行残片（≤3 字）**5 个**，逐个核实确为核心冻结文本（分版与核心坐标逐一相同）：P4 标题末行 `소식`（x=65, y=327.28）、P4 选项词 `대구`（x=65, y=2041.225）、P6 判断选项 `틀리다`×3（x=989, y=1807.225/2012.225/2129.225）。另 3 条单字整串（`물`、`간식`、`카메라`）为独立词条整串，非残片，已排除。
- **31 个框下溢出候选**：去重后恰 31 条，逐条核查（交付 SVG 坐标 + 文档顺序邻元 + 核心同坐标对照）：全部为后续元素——栏目标题（25pt，如 `산불조심기간이 시작됐어요`、`겨울 밥상`）、图片说明（19pt，如 `가을 산골짜기의 단풍. …`）、表格次行标签（P6 表 y=1355/1407/1459 各行）、表下资料注、 quiz 页脚行；无一为某框自身内容落于框外。框线扫描 0 穿框与此结论互证。P2 框标题等因法语 gloss 变长致 y 位移者，仍为后续栏目标题，非溢出。
- **P8 答案流末端**：键流区 165 行（不含 2 行页脚），最大基线 2528.85，墨底 **2532.60 < 2540**；末行 `76. 1,312 — Centres d'examen dans tout le pays : 1 312`（y=2528.85）。
- **P7 预告末端**：预告带 rect (65, 2401.94, 1820×118) → 末端 **2519.94 < 2540**（核心预告末端 2512.94）。
- **未决观察 1 核实（核心侧几何属实，只报告、不擅自重开核心）**：
  - 核心 P7 读者框 rect (1451, 1230.44, 434×508.5)，框底 **1738.94**；核心末行披露句（y=1764.73）墨底 **1766.73**，整行落于框外（框底之下 27.79px），核心公式欠计数约 25–29px 属实（框内末行 y=1736.33 墨底 1738.83 恰贴框底，下一行即出框）。
  - 本版 +40 slack 后：框 rect (1451, 1230.44, 434×635.5)，新框底 **1865.94**；末行征集句（y=1849.93）墨底 **1854.93**，框内留 **~11px**（1865.94 − 1854.93 = 11.01px）；金句栏头 y=1933.94，框底与栏头间有空隙。实测核实通过。
  - P7 金句 pitch：核心 132（1869.94→2001.94）→ 本版 **102**（1996.94→2098.94，2046.61→2148.61），行内容 ~76px，pitch 102 仍留 ~26px 行间空气，与 KIT 所述一致。

## 6. 家具三方对照（W45 核心 / W43 同配对 / 本版，SVG 实测；W43 同配对优先于 README #20）

| 槽位 | W45 核心 | W43 ko-fr（实测） | 本版（实测） |
|---|---|---|---|
| 刊头冠词 | 无 | 无 | 无（`Lucerna` 裸词） |
| 配对 badge | n/a（核心无 badge） | `TEXTES EN CORÉEN · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`，20pt 粗体 BRICK `#a4553a`，y=394 | 同串、20pt 粗体 `#a4553a`、y=394 ✓ |
| 副标题 y | 372 | 366 | 366 ✓ |
| 规则线 y | 392 / 401 | 412 / 421 | 412 / 421 ✓ |
| 暗带 y | 424 | 433 | 433 ✓ |
| 带内文字 y | 478 / 522 | 487 / 531 | 487 / 531 ✓ |
| 版次行 | `한국어판 · VOL.2 · 입동 · 단풍 · 김장`，40pt，y=330 | `HEBDOMADAIRE CORÉEN · VOL.1 · 태풍 참피 · 가을야구 · 단풍`，40pt | `HEBDOMADAIRE CORÉEN · VOL.2 · 입동 · 단풍 · 김장`，40pt，y=330 ✓ |
| 页脚 | 核心原生形 | `Lucerna · HEBDOMADAIRE CORÉEN VOL.1 · TEXTE EN CORÉEN · EXPLICATIONS EN FRANÇAIS`，20pt，y=2624 | 同形改 VOL.2，20pt，y=2624 ✓ |
| 页码行 | 核心原生形 | `Page {n} sur 8` | `Page {n} sur 8`（8 页逐页核实）✓ |
| 顶条中段 | 核心原生形 | `매주 한국어로 · Chaque semaine · 한국 사람이 읽는 한국어를 읽어요` | 同串 ✓ |
| P1 带右 | 核心原生形 | W43 主题不同 | `IPDONG` / `L'Ipdong, le samedi 7 novembre · Début du kimjang`（W45 主题，合理差异） |
| 带标题 | — | — | 생활 · Vie quotidienne；문화 · Culture；스포츠 · Sports；청년 · Jeunesse；깊이 읽기 · Lecture approfondie；말 공부 · Langue；시험과 답 · Test et réponses ✓ |
| 练习头 / 指令标签 | — | — | `연습 · Exercices page N`；指令标签 Complétez 42、Réécrire 4、Former une phrase 8、Traduire 4、Écrire 1、Associer 4（登记题型名 Compléter 等为登记标签，渲染形为祈使指令标签，见 §8 注） |
| gloss 前缀 / P8 分隔符 / P8 带副行 | — | `Note — ` / 韩语 `— 제N면 —` / 韩语-only | 同上 ✓ |
| 目录 P8 级 | 全部（核心） | Tous（W43） | `Tous` ✓ |

- W43 偏差清单逐项核实：P7 金句 pitch 132→102（§5）、读者框 lh +40 slack（§5，新框底 1865.94）、P2 框标题缩短为 `한능검 접수 · Inscriptions`（y=513.95，核心原题 y=446.225，位移源于法语 gloss 变长，框内无穿框）、P3 框标题缩短为 `단풍 구경 준비물 · À emporter`（y=990.90，与核心同 y）。缩短均不影响可读性（卡面目视无截断，canonical 0 旗）。

## 7. 读者来信角（逐字摘录，范围裁定）

- **韩语例信逐字冻结**（与核心同串、同 y 1319.44–1441.56，仅披露区 y 因法语短注而位移）：`「안녕하세요. 저는 대학생이에요. / 토요일에는 내장산에 단풍을 보러 가요. / 일요일에는 집에서 김장을 도와요. 겨울이 / 와도 따뜻하게 지내고 싶어요.」 — 독자 / 편지의 예`。无编造人名、信件、引文。
- **韩语延期披露逐字冻结**：`알려요: 이 편지는 편집부가 쓴 예예요. 마감 / 때까지 진짜 독자 편지와 8면 쓰기 우수작이 / 도착하지 않았어요. 그래서 예가 실렸고, / 지난 호의 약속은 VOL.3으로 이어져요.`（分版 y=1589.89–1677.22）。
- **法语短注**：`Exemple de la rédaction, pas une vraie lettre.`（y=1502.09–1530.49）。
- **法语延期披露（含 3 事实 + VOL.3 承诺）**：`Aucune vraie lettre ni meilleur texte de / page 8 à la mise sous presse : l'exemple / reste, la promesse passe au VOL.3.`（y=1736.33–1793.13）。事实：① 截稿时止；② 无真实来信；③ 无 P8 最佳文本；示例刊登；上期承诺顺延至 VOL.3。
- **征集句（明确祈使，框内）**：`Envoyez-nous votre lettre et votre texte / de page 8 !`（y=1821.53–1849.93，框底 1865.94 之内，距金句栏头 y=1933.94 有空隙）。字面同时覆盖来信与最佳 P8 文本，裁定为充分。
- **范围裁定**：预告行（`다음 주 · La semaine prochaine (VOL.3)` + 韩语预告体，内含 `여러분의 편지와 8면 쓰기 우수작도 실어요`）**不计作征集**，仅作预告；征集成立的依据是框内祈使句本身，不依赖预告行。

## 8. 计数 / 范文 / 图片 / 摘要

- **登记展开（本科对 scratch 重跑，登记源为两构建树，OUT 重定向至本科对 scratch）**：150 题连续（1–150）；级别 A2 51 / B1 72 / B2 27；页分布 10/18/18/18/18/18/12/38；题型（法语登记名，计数 = 核心）：Compléter 48、Choix multiple 52、Appariement 16、Texte à trous 13、Former une phrase 8、Transformation 4、Vrai ou faux 4、Traduction 4、Rédaction 1。n/page/level 不一致 0；注释变更 150/150。注：KIT 所列题型名为登记标签；渲染面出现的是祈使指令标签（Complétez 等，见 §6），两者映射一致，非不一致。
- **P8 分组**：P8 本页题 113–150 共 38 项，组头与题号段对应：A `이번 주 연표` 113–120（8）、B `일반 문제` 121–128（8）、C `읽고 답하기` 129–132（4）、D `문장 만들기` 133–136（4）、E `번역` 137–140（4）、F `이번 주의 말` 141–144（4）、G `도서관에서` 145–149（5）、H `써 보기` 150（1）。组标题韩语冻结。
- **范文逐字 = 核心**：MODELO 源串两构建树逐字节相同；渲染 6 行分版与核心逐行相同（`예: 나의 겨울 준비는 김장부터 시작해요. … 겨울 준비가 끝나면 마음이 든든해져요.`）；去空格 **157 字**（两版渲染体去空格同为 157；P8 印刷注 `157 caractères` 相符；指令 150–200자 区间内）。渲染行拼接与源串的字符差异仅为换行处空格脱落，去空格计数不受影响。
- **图片 payload 逐页 = 核心（两种哈希口径）**：base64 文本 sha256 前缀 / 解码 JPEG sha256 前缀——P1 1（`535fff46b7ce` / `6f7f33ed8f40`）、P2 1（`e66d2b455ec6` / `96a6a19b612a`）、P3 2（`e266b6ee1a87` / `158ea3a0e81f` 与 `5bea45d1f81e` / `214cc390ac7c`）、P4 1（`1a7e7d6d5ffc` / `18ad8ae06fac`）、P5 1（`6a1bab177d54` / `35e7dc69d417`）、P6/P7/P8 0。credit 均在页、取 Commons API Artist 字段原文：P1 `사진: lumoplank — CC0 (Wikimedia Commons) · 자료 사진`、P2 `사진: wizdata — CC0 …`、P3 `사진: Udonhan1992 — CC0 …` + `그림: Paul Cézanne — Public domain (Wikimedia Commons)`、P4 `사진: Bain News Service — Public domain …`、P5 `사진: Gary Todd — CC0 …`；资料照片注记在位。
- **ABSTRACT**：法语单行（1 行）、ASCII 双引号 0 个；真实主题关键词（Ipdong 周 11 月 2–8 日、深秋末叶、kimjang 季开始、Suneung 倒计时、韩国史考试报名）+ 学习者检索短语（`apprendre le coréen en lisant de vrais articles`）+ Lucerna coréen VOL.2、A2–B2、150 exercices。全文：`Lucerna coréen VOL.2 : la semaine de l'Ipdong du 2 au 8 novembre 2026 — derniers feuillages d'automne, ouverture de la saison du kimjang, compte à rebours du Suneung et inscriptions à l'examen d'histoire de Corée ; 150 exercices de coréen du niveau A2 au niveau B2 pour apprendre le coréen en lisant de vrais articles.`

## 9. 目视（全 8 卡，非抽查）

p1–p8 全部整幅目视：无重叠、无截断、无错位框。P1 badge/暗带/日历/图片 credit 干净；P2 `Inscriptions` 框标题框内完整；P3 `À emporter` 框标题框内完整、Cézanne 图与 credit 在位；P4 标题末行 `소식` 为冻结换行、流程图干净；P5 图片与 Gary Todd credit 在位；P6 对照表 12 标签清晰无遮盖；P7 读者框末行 `de page 8 !` 框内留白、金句双行与预告带干净；P8 四列答案流至页脚规则线、150 行与 H 范文在位。

## 10. KIT 文字观察（非阻塞；纸面正确）

1. **p8 工具版本段落滞后**：KIT 称任务开始时 `tools/p8.py` 为旧版（`67df05f1…`）、新版（`96fc2cfe…`）“未采纳、仅交叉核对”。当前 canonical `tools/p8.py` 实测即新版 `96fc2cfe…`，且本校对全部使用当前版本重测得 CLEAN、keydiff [137, 138]，与 KIT 记载的两版一致结论相同。KIT 段落是构建时快照滞后，非纸面错误；本报告按当前版本注明（见 §2）。
2. **`Le Lucerna` 否定句自述**：KIT 称“No occurrence of `Le Lucerna` anywhere”，但该否定句本身含有该字符串；SVG 全文实测为 0 命中，刊头确无冠词。属 KIT 行文自指，非纸面错误。
3. **Gloss 口径**：KIT 仅列按文件分布（24/26/28/6/0）；按渲染页分布（5/19/16/10/16/12/6/0）由本报告 §3 补测，两版均等于核心，非 KIT 错误。

## 11. 校对前后哈希

- 交付物：`delivery-before.sha256 = delivery-after.sha256`（diff 为空）。
- 核心：`core-before.sha256 = core-after.sha256`（diff 为空）。
- W43 同配对：`w43-before.sha256 = w43-after.sha256`（diff 为空）。
- 交付物与核心在校对中均未被改动。

## 证据文件

- 本报告：`hidden_files/w45/ko-fr-proof/REPORT.md`
- 校对前/后哈希：`hidden_files/w45/ko-fr-proof/delivery-before.sha256`、`delivery-after.sha256`、`core-before.sha256`、`core-after.sha256`、`w43-before.sha256`、`w43-after.sha256`
- 冻结重测：`hidden_files/w45/ko-fr-proof/scratch/freeze-diff.txt`、`.json`、`freeze-adjudication.txt`；基线：`scratch/baseline/`（8/8 复现）
- P8：`hidden_files/w45/ko-fr-proof/scratch/p8-compare.txt`、`.json`、`p8-core.json`、`p8-ed.json`
- 登记：`hidden_files/w45/ko-fr-proof/scratch/reg-run.txt`、`reg-core.json`、`reg-ed.json`（`reg_rerun.py`、`reg-core/`、`reg-ed/` 为本科对 scratch 重跑）
- Gloss：`hidden_files/w45/ko-fr-proof/scratch/gloss.txt`（渲染页分段法）、`gloss-ast.txt`（AST 常量串法）、`gloss_rerun.py`、`gloss_ast.py`
- 几何：`hidden_files/w45/ko-fr-proof/scratch/occlusion-ed.txt`、`.json`、`geom.txt`（初版锚点误报已纠正，见报告说明）、`geom2.txt`（锚点修正版）、`geom3.txt`、`geom4.txt`、`spill-check.txt`
- 孤儿：`hidden_files/w45/ko-fr-proof/scratch/orphan-wrap.log`（本科对 scratch 重跑，与构建员日志逐条相同）、`orphan-wrap-core.log`、`orphan-scan.txt`、`orphan_scan.py`、`orphan-svg.sha256`（scratch 渲染 8/8 = 交付）
- 家具/分析：`hidden_files/w45/ko-fr-proof/scratch/furn.txt`、`analyze1.txt`

**不宣布上架。** 是否入库由父线定夺。
