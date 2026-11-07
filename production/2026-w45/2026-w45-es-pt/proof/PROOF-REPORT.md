# W45 ES×PT 独立校对报告（SOP §8）

**结论先行：纸面零问题，但 KIT 有 1 项表述不实 → 在 KIT 修正前不判定稿。**
纸面本身（SVG/PDF/卡面）无需改动；定稿条件见文末“问题清单 P1”——接受
`A notícia`（有 W45 IT 兄弟版 `LA NOTIZIA` 先例）则只需改 KIT 一行文字，
无需重建；若协调员要求与 W43 已发版逐字一致，则改串为 `A manchete`
后重建并重校。

- 待校版本：`files/weekly-report-w45-es-pt/`（svg ×8、cards ×8、print/web PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照：W45 ES 核心 `files/weekly-report-w45-es-core/`；家具对照 W43 已发版 `files/weekly-report-es-pt/`（只读，未写入；其 mtime 仍为 2026-10-22）
- 本校对未改源码、未派生下级代理、未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git；全部输出只写本目录。
- 开工查重：交付写盘最后时间为 19:00:37 UTC，90 秒复查 + 后续全程零新写盘；`ps` 所见渲染进程仅为本会话自身的 exec 噪声，无并发写盘者，可正常开工。校对结束时核心重哈希与开工前一致，待校版 mtime 未变。

## 问题清单（阻塞，1 项）

### P1 — KIT §3 “(all W43 verbatim)”表述不实（纸面词本身可接受，KIT 须修正）
- 实测：P1 `LA NOTICIA` 槽（x=65 y=606 22pt bold 砖红，三版同槽同几何）：
  W43 已发版 `LA NOTICIA · A manchete`；W45 核心 `LA NOTICIA · 头条`；
  本版 `LA NOTICIA · A notícia`。且本版同页 kicker 行（[9]）把“本期头条”译为
  `A manchete desta edição`，即同一核心词在本页出现两种葡语译法。
- 定性：`A notícia` 不是错译（W45 ES×IT 兄弟版同槽亦作 `LA NOTIZIA`；
  DE `SCHLAGZEILE`、EN `Top story`、FR `À LA UNE`、NL `Hoofdverhaal` 各有译法，
  属译者 latitude），且任务第 10 项逐字清单（徽章、页脚、Nota 前缀、band、
  练习头、指令 chips）中不含此槽——故不列为纸面缺陷。
- 但 KIT §3 P1 家具 bullet 称“(all W43 verbatim)”与实测不符；同理 §3 总起
  “verbatim from W43”亦涵盖了核心驱动的 P8 右文（见下），措辞须修正：
  要么接受本版译法并把 §3 改为如实记录（`A notícia` 为 W45 译法，W43 作
  `A manchete`；P8 右文为 W45 核心译文），要么把串改回 `A manchete`。
- 附带核实：P8 右文 `Cada resposta traz uma breve nota · ✓ marca a questão de redação`
  是 W45 核心中文右文（每题附一句中文简析 · 带 ✓ 的为范文题）的译文，
  W43 已发版右文 `Uma nota curta em português por exercício · ✓ = exercício de escrita`
  对应的是 W43 核心的不同中文措辞——属核心驱动差异，非家具模板偏离。
  W45 IT 兄弟版右文亦为各自译文（`Una nota in italiano per ogni risposta…`），佐证此槽非 W43 模板。

## 非阻塞观察（冻结核心几何，presence only，不计入本版缺陷）

- **O1 — P7 cartas 框末行压框线（新增观察，需协调员裁定记录）：**
  cartas 框 rect y=1299.58 h=520.5 → 底 1820.08（与核心分毫不差），
  但末行披露基线 y=1832.69，字墨骑在框底线上、框外一行（卡面目视确认）。
  核心卡面同一位置同一现象（核心末行中文披露亦在框线之下），几何逐字节相同，
  故非本版引入；建议沿用 Inmigración 式裁定记录为冻结核心 artifact，
  或留待未来核心修订，勿由分版擅自改几何。
- **O2 — P6 `Inmigración` 约 5px 条形压字（已裁定非阻塞，presence only）：**
  文本 x=1011 y=1717 21pt bold，后随条 rect x=1139 y=1699 w=156.75，
  实测墨右 1144.2 vs 条左 1139（卡面目视：末字母 `n` 触条边），与核心逐项相同，
  KIT §6 已记录。本版未改几何，符合任务第 5 项。

## 逐项验证结果（全部独立实测，不采信 builder 自述）

1. **基线**：`freeze.py baseline`（核心构建 `weekly-report-w45-es-build`）8/8 逐字节相同，
   哈希与 KIT 基线表逐位一致；事后核心重哈希无变化（`core-hashes-before/final.txt`）。
2. **freeze diff（--strict-cjk）**：各页增减串求和与 KIT §5 表完全一致
   （P1 +26/-25，P2 +49/-43，P3 +33/-30，P4 +30/-27，P5 +47/-40，P6 +17/-17，
   P7 +43/-42，P8 +163/-160）；added CJK = 0 全 8 页；全版 CJK 仅 P7 的 `（` `）` 各 1 个。
   西语删串：无 CJK 字符（freeze 定义，含全角区）的核心删串恰为 KIT 所列 6 项
   之 5 项正文（P1 刊头副标题槽、P5 `la NFL.`、P6 `indecisos · margen de error`、
   P8 #1 两行）+ P7 `mejor。`（`。`属 CJK 标点区）；另 2 个全角括号碎片
   （P2 `AEK）`、P5 `viaje, si tu comunidad hace puente（`）的西语词元均在新增串中
   逐字存活；全量无 CJK 核心文本元素逐项核对，缺失的仅上述备案项——**西语零未备案丢失**。
   长文本（≥40 字）缺失项全部为讲解层中译葡、家具 VOL 换版或 P5 题干重排，
   西语原文均在新增串/他处存活。
3. **P8**：`p8.py compare` CLEAN（150=150，missing=[]，extra=0），
   keydiff 18 项与 KIT 一致。独立 dash-parse（答案区按首个 ` — ` 切分）逐项复核：
   16 项括号分支 artifact（34, 57, 83, 85, 93, 94, 95, 96, 98, 101, 107, 109, 110, 111, 117, 148）
   键全部逐字节相同；真改动仅 137（`Na segunda-feira é feriado em nove comunidades.`）
   与 138（`No domingo vemos a NFL e o Atlético–Barça.`）；139/140 反向键逐字节相同
   （`El Bernabéu acoge un partido de la NFL.` / `Cada gráfico tiene que llevar su fuente.`）；
   150 两版均为 `✓ + 指针注释`，✓ 标记相同，注释为已备案的 apparatus 改动
   （dash-parse 原始输出另标 150 仅因该条无 ` — ` 分隔符、整段即注释，非键改动）。
   范文：西语范文逐字节等同核心，实测 84 词，与印出 `(84 palavras)` 一致。
   P8 括号形式：答案区半角括号，与该家族分版构建代码一致。
4. **几何审计**：`occlusion_audit.py --selftest` 通过（6 类各 1 次，干净对照静默）；
   本版 0 flags，核心 0 flags，NEW = 0；同基线行扫描本版 7 项 = 核心 7 项，
   同一批 P1 目录行（`Pág. n` + 标题，4.0px 正间隙，无重叠），P1 顶带/刊头/页脚行两版皆静默；
   P6 图表区 34 元素（23 文本 + 8 条形 + 2 框 + 1 规则线，y 1580–1950 窗口）与核心逐项相同。
5. **P6 压字**：见 O2，几何与核心相同、KIT 已记录，非新增讲解层重叠。
6. **内容计数**：gloss 按 `·` 本身拆分，P2 5=5、P3 5=5、P4 5=5、P5 4=4，
   词头顺序与核心一致；图片载荷：P3 `<image>` 元素与核心逐字节相同
   （payload MD5 ad9f8753… = 构建资产 castanas.jpg），P5 同理（0b1992b1… = kuerbis.jpg），
   印出 credit 两版逐字相同（P3 Wikimedia Commons CC0；P5 美国农业部 dominio público）；
   P7 金句 8 句西语原文各恰 2 次（文章页 + P7，页签 1/2/3/4/5/6/6/1 与 KIT 一致）；
   150 题，级别：配对章计数 A2 46/B1 68/B2 24 + 三组共用级别章配对题
   （P2 25–28 A2、P4 52–55 B1、P8 141–144 B2，各 4 题）= **A2 50 / B1 72 / B2 28**；
   答案区按分隔符分组：**10/18/18/18/18/18/12/38**；最终构建日志零 FLOW OVERFLOW /
   零 HEAD TOO WIDE（首版日志 13 次溢出 = P6 3 + P8 10，与 KIT §8 一致，已修复）。
7. **W43 三核对点**：
   (a) P7 示例信署名括号：W43 已发版为全角 `Mei （carta de ejemplo, escrita por la redacción）`
   （全 P7 仅此一对全角括号）；本版全角 `Ana （ejemplo, escrito por la redacción）`
   与已发版一致、与核心逐字节相同——**不列为问题**（es-en/es-de/es-fr 的半角归一化
   不跨配对套用）。
   (b) P8 分隔符：W43、核心、本版均为 `— PÁGINA {n} —` 全大写形，逐字一致；
   tables.json 通用形 `— Página {n} —` 未被采用，符合“已发版为准”。
   (c) 渲染面指令/类型标签：指令 chips 两版集合完全相同
   （Complete / Verdadeiro ou falso / Forme a frase / Reescreva / Traduza / Escreva / Associe
   + `Escolha a resposta certa.`）；P8 章节头 A–F/H 相同（G 章名随当周内容不同，
   TIENDA vs INMOBILIARIA，属内容非标签）；葡语类型名（Completar frases 等不定式形）
   在渲染面零出现，确属元数据（构建代码 `== "Escrita"` token 已核）；其余渲染标签
   （`¿Y TÚ? · E você?`、`¿SABÍAS QUE…?`、FOCO 行、预告行除 VOL 号外）均一致。
   gloss 词条内标点（W43 逗号式 vs W45 括号式）与 FRASES 括号说明（W43 `(tiradas desta edição)`
   vs 本版 `(retiradas dos textos desta edição)`）均为核心中文措辞驱动的讲解层译法，
   不在任务第 10 项逐字清单内，不列为问题（已如实记录于此）。
8. **版式余量**：P5 练习流终点 y=2577（终版日志 `flow[P5-ex] ended col 2/3 y=2577 (bottom 2580)`，
   3px 余量），卡面目视末题与页脚规则无碰撞、审计 0 flags；
   P7 cartas 框底 1820.08、预告框 rect y=2440.08（底 2558.08，距 2580 规则线 22px）、
   预告标题基线 2484.08 均与核心分毫不差（右栏三框 rect 亦逐项相同）；
   P8 #137/#138 各 2 行（基线 1994.02/2009.68、2039.34/2055.00），卡面目视无压线、
   与 #139 间距正常。
9. **读者园地**：西语披露 ld（[123]–[126]）与核心逐字节相同；葡语 ldcn
   `Nota da redação: ao fecho, sem cartas reais nem textos da pág. 8; sai este exemplo. Promessa: VOL.3.`
   保留三事实（无真实来信、无最佳作文、登示例信 + 承诺顺延 VOL.3）；
   Ana 示例信正文 + Shanghái + 全角括号署名与核心逐字节相同，无编造；
   “欢迎来信”邀请的省略 KIT §7 已如实披露（行数对齐，ES×EN 先例），不在任务三事实内。
10. **家具三方比对**：徽章（19.5pt sans bold 砖红 #a4553a，x=975 中线 y=372，
    与 W43 逐字同串同属性）、页脚（除 VOL.1→VOL.2 外逐字相同）、Nota — 前缀、
    band（7 条全同）、练习头 + 右文（全同）、指令 chips（全同）均与 W43 已发版逐字一致；
    盒标题实测尺寸：CIFRAS 20pt（墨宽 370.2，23pt 将为 425.9 超 416 槽）、
    CALENDARIO 19pt（399.5；20pt 将为 420.6 超槽）、PLAN 20pt（405.5；23pt 将为 466.5 超槽）、
    ERRORES 20pt（339.8）、PALABRA 22pt（384.5），卡面目视均无超框；
    F1 顶带实测：带墨止 1406.22、日期墨起 1420.70，间隙 14.5px（KIT 1406.3/1420.7，舍入差 0.1）；
    F3：P1 CIFRAS 框 3 处、P2 日历框 7 处、P5 PLAN 框 5 处括号前均有空格，
    全页括号无无空格前置；F4：P1 词注 `«Pré-campanha»: semanas antes da campanha.`
    墨宽 419.8 < 434，基线 1816.2 距 1844 规则线 27.8px，干净。
11. **ABSTRACT 与 PDF**：ABSTRACT.txt 葡萄牙语单行（末尾换行符 1 个）、
    无 ASCII 双引号，含 habitação / 29 de novembro / ponte / NFL / Bernabéu /
    Atlético–Barça / `aprender espanhol` 学习者短语 / A2–B2 / 150 题；
    两 PDF 均为 8 页（Count=8），print 7,162,060 字节 sha256 a6459268…（与 KIT 全串一致，
    见 edition-hashes.txt），web 3,735,347 字节 < 10 MB sha256 754cd83c…（与 KIT 全串一致）；
    8 卡全部目视（P1–P8 全卡 + P1 顶带、P6 压字区、P7 cartas 框、P5 底、P8 #137/#138 裁切），
    除 O1/O2 两处冻结核心几何外，无溢出/遮挡/页脚碰撞；版 SVG 哈希与 KIT §10 表逐位一致。

## 定稿条件
1. 协调员裁定 P1：接受 `A notícia` → 仅修正 KIT §3 措辞（删除“(all W43 verbatim)”
   的绝对化表述，如实注明 W43 作 `A manchete`、P8 右文为核心译文），纸面不动，
   修正后可定稿；或要求与 W43 逐字一致 → 改串为 `A manchete` 后重建并重校
   （该串 22pt 下 `manchete` 比 `notícia` 长约 1 字宽，槽位无溢出风险，但仍须重校）。
2. 建议将 O1（P7 cartas 框末行压框线）与 O2 同样记为冻结核心已知 artifact，
   不由分版修几何。

## 审计输出路径（本目录）
- `freeze-baseline.log`、`freeze-diff.json/.log`、`p8-compare.json/.log`、`dashparse.txt/.json`、
  `occlusion.log/.json`、`occlusion-core.log/.json`、`occlusion-selftest.log`、
  `rowcheck-edition.txt`、`rowcheck-core.txt`、`frozen-audit.txt`、`spanish-removal-audit.txt`、
  `p6chart.txt`、`p6-audit.txt`、`gloss-core.txt`、`misc-audit2.txt`、`image-payload.txt`、
  `counts.txt`、`matchsets.txt`、`modeltext.txt`、`model-ed.txt`、`model-core.txt`、
  `geom.txt`、`geom2.txt`、`furniture.txt`、`furniture2.txt`、`furniture3.txt`、
  `w43-audit.txt`、`w43-letter.txt`、`w43-righttext.txt`、`noticia.txt`、
  `edition-hashes.txt`、`core-hashes-before/after/final.txt`、`crops/`（卡面裁切）、
  `baseline/`（基线重跑 scratch）。
