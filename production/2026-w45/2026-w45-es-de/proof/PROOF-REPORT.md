# W45 ES×DE（2026-w45-es-de）独立校对报告

**结论先行：除徽章槽位一项待协调员裁定外，本版 ZERO PROBLEMS。**
P6 Inmigración 擦碰经实测确为冻结核心几何，按协调员 2026-10-27 裁定登记为非阻塞已知缺陷，**不构成不通过理由**。
徽章槽位一项（第 §9）只呈三方实测证据，不自行判通过/不通过，待协调员裁定。

- 待校版本：`files/weekly-report-w45-es-de/`（8 SVG + 8 张 1950×2700 PNG + print PDF 7,162,280 B / 8 页 + web PDF 3,748,613 B / 8 页 + WEEKLY-KIT.md + ABSTRACT.txt）
- 构建副本：`hidden_files/weekly-report-w45-es-de-build/`（transform.py）
- 本报告与全部审计输出：`hidden_files/w45/es-de-proof/`（见文末路径）
- 纪律：只读校对。未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git；核心构建目录与核心已发 SVG 全程未改动（校对结束时核心 SVG 重哈希，与基线哈希逐字节一致）。

## 1. 基线 freeze —— 通过（附一条方法说明）

- 核心已发 SVG 实测 sha256（前 16 位，与构建者自述逐项一致）：
  p1 `a1b3010296ad129e` · p2 `10e78c2e6cb29519` · p3 `5986ba9e318c985e` · p4 `1894836e06be824b` ·
  p5 `cd15c68b5f8db752` · p6 `fcfccf8267e10cc7` · p7 `b1774024b6a17353` · p8 `d1c46fa439ac505d`
- `freeze.py baseline` 对**未改动的核心构建目录**（`hidden_files/weekly-report-w45-es-build/`）重跑：**8/8 逐字节相同**，核心 SVG 事后重哈希无变化。
- 对**已转换的 DE 构建目录**直接重跑 baseline 得 0/8 ——这是预期结果，不是缺陷：该目录的源码已是德语化后的状态，重建出来理应是德语版而非核心版；构建者“8/8”指的是转换前副本的状态。
  为闭合此环，另用同一工具以已发德语版 SVG 为参照重跑 DE 构建目录：**8/8 逐字节相同**（p1 `4e91d8d8c778f457` … p8 `c24125b7c435d3e2`，与已发版一致）。即：核心构建可复现核心，DE 构建可复现已发德语版，链条完整。
- transform.py 幂等（在 proof 副本中重跑，未碰原构建目录）：exit 0，**0 处替换**，7 个源码文件哈希全部不变；SKIP 行实测 285 行（构建者自述 278 行，计数口径差 7，不影响结论：替换数为 0）。

## 2. 冻结 diff 与西班牙语正文零增删 —— 通过

- `freeze.py diff`：各页 added CJK = 0，全刊 added CJK = 0；各页 CJK 核心→本版：170→0、280→0、161→0、169→0、247→0、80→0、388→0、981→0。
- SVG 文本层非 CJK 移除串全刊仅 3 条，逐条裁定如下，其余移除串全部含 CJK（中文讲解层被德语替换）：
  1. P5 `la NFL.`——换行碎片。核心 #72 题干 `El Bernabéu ___ (原形 acoger) un partido de / la NFL.`，本版 `El Bernabéu ___ (Infinitiv: acoger) un / partido de la NFL.`，西班牙语词逐字保留，仅 instr 改德语致换行点移动。
  2. P6 `indecisos · margen de error`——换行碎片。本版仍为 `Setze ein: sondeo · muestra · indecisos · / margen de error`，词逐字保留。
  3. P8 `102. uno — el 1 = el uno`——注-only 翻译。本版 `102. uno — der 1. heißt el uno`，键 `uno` 逐字节不变。
- 源码层拉丁词元核查（核心构建 vs DE 构建全部 7 个 .py 文件逐 hunk 比对）：除以下装置性丢失外，正文词元无增删——
  (a) 页脚英文行 `LUCERNA SPANISH WEEKLY` → 德语页脚（bslib4.py，构建者所称第 1 处）；
  (b) OUT 路径 `es-core` → `es-de`（每文件各 1 处，构建者所称第 2 处）；
  (c) #117 注缩短：`acoger = 承办（伯纳乌承办 NFL）` → `acoger = beherbergen`，括号事实（Bernabéu 承办 NFL）在题干中已在版（构建者所称第 3 处）。
  其余“丢失”计数均为分词器假象：德语复合词中的同一词元（如 `DANA-Gedenken`、`NFL-Spiel` 中的 DANA/NFL）及大小写/连字符切分所致；逐 hunk 目视确认西班牙语题干、键、文章句全部逐字保留。
- 全刊 SVG 汉字 = 0，全角括号 = 0（文本层与原始层双查）；P8 注括号均为半角，0 违规。
- 图片：P3（烤栗子）、P5（南瓜）嵌入 data URI 与核心版**全 sha256 相同**（P3 627,079 字符、P5 461,691 字符）；P1 房屋插图为程序绘制路径，未动。

## 3. P8 答案 —— 通过（CLEAN，keydiff 23 项逐项裁定）

- `p8.py compare`：**CLEAN，150 = 150，missing = []，extra = 0**，keydiff = [25, 26, 27, 28, 52, 53, 54, 55, 83, 85, 95, 96, 98, 107, 117, 118, 137, 138, 141, 142, 143, 144, 148]，与构建者自述完全一致。
- 逐项裁定（以 P8 原始答案行 + content8.py 注册行为准；p8.py extract 对括号注有截断假象，如 #117 提取为 `A`，原始行实为 `117. A — acoger = beherbergen`，已据原始行裁定）：
  - 注-only、键逐字节相同（21 项）：#25–28、#52–55（配对题，键字母不变，附加德语 gloss 注，格式 `wort = deutsche Glosse (Buchstabe)` 与 W43 ES×DE 已发版式一致，如 `141. c — sondeo = Umfrage (c)`）、#83、#85、#95、#96、#98、#107、#117（注德语化 + 删冗余括号，见 §2c）、#118、#141–144、#148。另 #102 未进 keydiff，原始行键 `uno` 同样逐字节不变、仅注中译。
  - 重瞄准键（2 项）：#137 `#138`，与 W43 ES×DE KIT §5 先例同款（W43 #137/#138 同为 ES→DE 键德语化）：
    #137 `Am Montag ist in neun Regionen Feiertag.` 注 `Übersetzung`；#138 `Am Sonntag sehen wir die NFL und Atlético–Barça.` 注 `Übersetzung`（注跨行，原始行 + 续行 `Übersetzung`）。
  - #139/#140：题干改为德语句（#139 `Das Bernabéu ist Gastgeber eines NFL-Spiels. → ___`，与 W43 #140 德语句 `Jede Grafik muss ihre Quelle angeben. → ___` 同款；#140 题干与 W43 #140 德语句逐字相同），西班牙语 key 逐字节不变（`El Bernabéu acoge un partido de la NFL.` / `Cada gráfico tiene que llevar su fuente.`），注德语化（`acoger = beherbergen` / `tener que = müssen`）。
  - #150：注册行改为德语装置句 `Offene Aufgabe — Mustertext unten auf dieser Seite`，注 `Mustertext in Abschnitt H auf dieser Seite (84 Wörter)`；范文西班牙语 84 词**逐字节不变**（渲染行与核心版逐行相同；空白切分实数 84 词，`Vivo … ¡Qué mes!`）。
  - 答案代码：P8 分隔符 8 页均为 `— PÁGINA N —`，与 W43 ES×DE 已发版式逐字相同（未用 tables.json 的 DE 通用 `— SEITE N —`）；破折号体 `N. key — note` 未动。
- 答案流几何：答案行 150 条；末号答案 #150 基线 2410.9；最长栏末行 #76 基线 2548.7、墨底 2552.2，距页脚线 2580 有 27.8px 净空；occlusion 0 flags（见 §4）。构建者“流末 y=2427”应指末栏游标（2410.9 + 行高），与实测无实质出入，无溢出。

## 4. 几何遮挡 —— 通过

- `occlusion_audit.py --selftest`：6 类 planted 全部触发、clean 对照静默，**selftest OK**。
- 本版审计：**0 flags**；`--core` 对比：核心 0 flags，**NEW flags = 0**。
- 同基线墨迹扫描（家具带）：P1 顶栏/刊头带/黑带/页脚带相邻墨迹间隙除冻结目录外全部 ≥8px；全页同基线扫描最小间隙：P1 4.00px（目录行，见 §8）、P2–P5 34.00px、P6 19.75px、P7 19.75px、P8 18.25px，**无同基线重叠**。
- 构建者自述的实测值逐项复现：P1 刊行行 45pt 墨迹 56.5→1893.5（内框线 1910，净空 16.5px）；P7 诊所框标题 20pt 墨止 1857.2（框右界 1885，净空 27.8px）；P7 预告框底 2558.08（构建者称 2558.1），距页脚线 2580 有 21.9px。
- P6 图表逐元素：左图 PSOE/PP/Vox/Sumar/Podemos 标签与条形起点间隙 30.5–100px；右图 Vivienda 间隙 34.5px、Economía 间隙 21.0px、数值均在框内；唯一重叠为 §8 的冻结 Inmigración 行。
- 无占位符：TODO/FIXME/Lorem/`??` 全刊 0；XXX/TBD 命中仅见于图片 base64 载荷内，正文层 0。

## 5. Gloss、金句、注册表 —— 通过

- Gloss（按 `·` 本身拆分，源码层 + 渲染层双验）：P2 5=5（festivo / el puente / la comunidad / anochecer / el horario de invierno）、P3 5=5、P4 5=5、P5 4=4，**合计 19=19**；西班牙语词头与核心版逐字相同，德语释义逐项对应。
- P7 金句：8 句西班牙语原文每句在全刊中**各恰 2 次**（原文所在页 1 次 + P7 1 次，按去引号句体归一化计数；P7 的 «» 形式与文章无引号形式为同一句体）。
- 注册表（安全副本重跑，非核心目录内导入）：总量 **150**；A2 50 / B1 72 / B2 28；分页 10/18/18/18/18/18/12/38；题型 完成句子 48 / 单选 47 / 词汇配对 12 / 判断对错 8 / 造句 7 / 句型转换 10 / 完形单选 13 / 翻译 4 / 写作 1；**page/level/type 差异 = 0**；key 差异仅 3 项（#137、#138、#150 装置句，见 §3）；本版注册表注/键中 CJK = 0。

## 6. 家具（对 W43 ES×DE 已发版 `files/weekly-report-es-de/` 逐项比对）—— 通过

- 徽章串逐字相同（位置/字号见 §9 待裁定项）：`SPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER`。
- 每页页脚：`La Lucerna · SPANISCHE WOCHENZEITUNG VOL.2 · TEXT AUF SPANISCH · ERKLÄRUNGEN AUF DEUTSCH` + `Seite N von 8`（8/8 页齐全，仅 VOL.1→VOL.2）。
- 栏目后缀：VIDA · LEBEN、CULTURA · KULTUR、DEPORTE · SPORT、JUVENTUD · JUGEND、A FONDO · HINTERGRUND、LENGUA · SPRACHE、EJERCICIOS · ÜBUNGEN；gloss 前缀 `HINWEIS · `、桥句前缀 `Hinweis · `、答案行 `Antworten auf Seite 8 · Aufgaben gemischt, nach Nummer suchen`，与 W43 注册表逐字一致。
- instr 映射齐全：Ausfüllen、Richtig oder falsch、Sätze bilden、Umformen、Übersetzen、Schreiben、Zuordnen。
- P1 顶栏、刊行行、黑带右侧文案与 KIT §3 一致；刊头仍为 `La Lucerna`（西班牙语冠词，未动）。

## 7. ABSTRACT 与读者园地 —— 通过

- ABSTRACT.txt：德语**单行**（409 字符，末尾换行），**ASCII 双引号 0 个**，CJK 0 个；内容含本周实题关键词（29 日大选倒计时、住房议题、11 月 2 日周一九区连休、NFL 马德里站、11 月 8 日周日 Atlético–Barça）+ A2–B2 / 150  Übungen + 读者母语/目标语说明。
- 读者园地：Ana 示例信西班牙语行与核心版**逐字相同**，仅署名行括号由全角改为半角（`(ejemplo, escrito por la redacción)`，与 W43 ES×DE KIT §5 的字形规范化先例同款，词句未动）；西班牙语披露 `Nota de la redacción: al cierre no había cartas reales…` 原文保留，德语 `Anmerkung der Redaktion: Keine echten Briefe eingegangen…` 作为讲解层附加，事实一致（未收到真实来信、示例信、承诺顺延至 VOL.3）；**未编造新读者/信件**。
- 日期星期实测（Europe/Madrid）：2026-11-02 周一、2026-11-08 周日、2026-11-29 周日、2026-10-29 周四、2026-11-13 周五、2026-11-01 周日、2026-11-06 周五、2026-10-05 周一、2026-10-02 周五、2025-11-16 周日——与版内全部星期表述一致。

## 8. 冻结核心轻擦（非本版问题）

- **P1 目录 `Pág. N` 与标题间距**：真墨测量 7 行均为 **4.00px**（构建者称 3.9px，方法舍入差），核心版与本版**逐行完全相同**，间隙为正、无重叠。另渲染卡片裁图（1440,1380,1900,1650）核心 vs 本版**逐像素相同**。结论：冻结版式，非缺陷。
- **P6 Inmigración 标签擦碰**（协调员已裁定项）：见 §9(2)。

## 9. 两项待裁定事项 —— 只报告证据

### (1) 徽章槽位（待协调员裁定，本校对不判）

三方实测（P1 SVG 文本元素实测值，`x=975` 居中）：

| 版本 | 徽章串 | y（基线） | 字号 | 粗体 | 颜色 | y=372 元素 |
| --- | --- | --- | --- | --- | --- | --- |
| **本版 W45 ES×DE** | `SPANISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER` | **574** | **22pt** | 是 | BRICK `#a4553a` | 西语 strapline `EL PERIÓDICO SEMANAL PARA APRENDER — LA VIDA REAL, EN ESPAÑOL, DESDE ESPAÑA`（19pt，**保留**） |
| W43 ES×DE 已发版 | 同上串，逐字相同 | **574** | **22pt** | 是 | BRICK `#a4553a` | 同上西语 strapline（19pt，**保留**） |
| W43 ES×EN 已发版 | `TEXT IN SPANISH · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS` | **372** | **19pt**（实测；简报引 README #20 称 19.5pt，实测为 19pt） | 是 | OLIVE `#3e4c2a` | 该 y=372 元素本身就是徽章，**无独立 strapline** |

证据要点：本版与 W43 ES×DE 已发版在徽章位置、字号、颜色、串文本、strapline 保留与否上**全部一致**；W43 ES×EN 属于另一实例（372 槽位、徽章替换 strapline）。构建者“从已发 ES×DE 先例”的说法与实测相符；简报所引 README #20 的 372/19.5pt 描述对应的是 EN 核心实例而非 ES×DE 已发先例。几何本身不由本校对定罪，**请协调员据此裁定**：若维持 574/22pt，本版无需改动；若改 372/19.5pt，需移徽章 + 删 strapline 一行（构建者称可低成本返工）。

### (2) P6 Inmigración 擦碰（协调员已裁定：登记为非阻塞已知缺陷）

实测（真墨度量，SVG 元素序号/坐标/填色三方一致）：
- 核心版与本版**完全相同**：标签元素均为 paint-order idx=109，`Inmigración`，x=1011、y=1717、21pt 粗体，墨盒 (1011.0, 1699.0, **1144.2**, 1722.5)；
- 其后条形均为 x=1139、y=1699、宽 156.75、高 22、填色 `#a4553a`，条形起点比标签墨右界早 **5.2px**，压住词尾 n 右缘约 3–5px；
- 渲染卡片裁图（1000,1680,1330,1745）核心 vs 本版**逐像素相同**（sha 前 16 位均为 `57782044be3fa4e0`）；字母完整可读，语境中词义无歧义；规范遮挡审计 0 flags（该类亚阈值覆盖不在审计类内）。
- 结论：确为**冻结目标语元素继承**，与协调员裁定（es-en 版实测 + 目视裁图确认、修复须重发核心 + 重建全部 ES 分版、不成比例）一致。**本校对仅登记其存在以确认身份，不列为本版问题，不影响通过结论。**

## 10. 问题清单

除 §9(1) 徽章槽位待协调员裁定外，**无问题**。§9(2) P6 擦碰为协调员已裁定的非阻塞已知缺陷，不计入问题。

## 附：审计输出路径

- `hidden_files/w45/es-de-proof/freeze-baseline/`（DE 构建目录 vs 核心 SVG：0/8，预期内，见 §1）
- `hidden_files/w45/es-de-proof/freeze-corebuild/`（核心构建 8/8 + 核心注册表 `reg-core.json`）
- `hidden_files/w45/es-de-proof/freeze-debuild/`（DE 构建复现已发版 8/8 + 本版注册表 `reg-ed.json`）
- `hidden_files/w45/es-de-proof/freeze-diff.json`（冻结 diff 全量）
- `hidden_files/w45/es-de-proof/occlusion.json`（本版 0 flags）、`hidden_files/w45/es-de-proof/occlusion-vs-core.json`（NEW flags = 0）
- `hidden_files/w45/es-de-proof/p8-compare.json`（CLEAN 150=150）、`hidden_files/w45/es-de-proof/p8-core.json`、`hidden_files/w45/es-de-proof/p8-ed.json`
- `hidden_files/w45/es-de-proof/reg-diff.json`（page/level/type 差异 []，key 差异 3 项）
- `hidden_files/w45/es-de-proof/transform-rerun/` + `hidden_files/w45/es-de-proof/transform-rerun.log`（幂等重跑：0 替换，285 SKIP）
