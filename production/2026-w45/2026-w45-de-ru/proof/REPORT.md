# W45 DE×RU 独立校对报告 — ZERO PROBLEMS（可定稿）

- 校对对象：`files/weekly-report-w45-de-ru/`（SVG×8、卡片×8、印刷 PDF、网页 PDF、WEEKLY-KIT.md、ABSTRACT.txt）
- 对照核心：`files/weekly-report-w45-de-core/`（Die Lucerna VOL.2，150 题）
- 对照同胞：`files/weekly-report-w45-de-en/`（P7 词框、P7 栏终点）、`files/weekly-report-de-ru/`（W43 已发同配对，家具实测）
- 工具：`tools/`（freeze.py、p8.py、occlusion_audit.py，全部经自测/实测；构建员自述一律未采信，全部数值均为本校对独立重测）
- 开工查重：files 与 hidden_files/de-ru-build 在 90 秒复查内零新写盘（末次写盘 21:03 UTC，当时 21:06 UTC）；运行中的进程属 de-ja 分版，与本版无关。正常开工。
- 本校对行为：只读校对。未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未改核心与 W43 目录（核心前后哈希一致，见门 1）。未派生任何下级代理。
- 上架：本报告不宣称上架，上架由协调员串行执行。

## 结论：ZERO PROBLEMS — 可定稿

9 个必查门全部通过，无编号问题。以下为逐门实测值。

## 门 1 Freeze — 通过

- 核心基线：`freeze.py baseline`（构建树 `hidden_files/weekly-report-w45-de-build/`，即 W45 DE 核心的真实构建目录）**8/8 字节复现**，与 KIT 所列哈希逐字节一致：
  - p1 `6cbd4802…fade3e`、p2 `9362256d…b6d22`、p3 `3e8a8d16…6b6d22`（全值见 KIT §2，本校对实测全同）、p4 `b787f592…5cb0199d`、p5 `4dcbeb97…3decb77c`、p6 `01b75ad4…79e2233090b`、p7 `fbaf8cdd…aa162f278c`、p8 `299524bd…1e3c13891`。
- 核心前后哈希一致：基线重跑前后 8 个核心 SVG sha256 全同（CORE-UNCHANGED），核心未被触动。
- `freeze.py diff`（核心→分版）：P1 +24/−23、P2 +36/−32、P3 +42/−40、P4 +26/−22、P5 +44/−39、P6 +36/−33、P7 +61/−53、P8 +161/−141；**新增 CJK 字符 0（8 页全 0；分版全文 CJK 字符 0、中文标点 0、全角括号 0）**；全文无“桥接”（中英两形在 SVG 文本层均为 0 命中）。
- 删除串逐项裁定（不含 CJK 的移除串，全量）：
  - P1 仅 1 串：`DIE WOCHENZEITUNG FÜR LERNENDE — DAS ECHTE LEBEN, AUF DEUTSCH, AUS DEUTSCHLAND`——任务规定的副标题槽位被配对徽章替换（见门 8），属家具，非正文。
  - P2、P5：不含 CJK 的移除串 0。
  - P3、P4、P6：各仅 1 串 `。`——中文 gloss 末尾孤悬句号元素；俄文版以 `.` 结尾故无此元素，属讲解层标点伪影。
  - P7：3 串，均为讲解层——`Ein Beispiel der Redaktion!`（编辑部示例标签改俄文 `Пример редакции!`）；`«der Tankrabatt»（Seite 2）: die`（全角括号→半角括号致换行切分差异，德语词本身存续，见门 2）；`……`（工具箱中文省略号随俄译消失）。
  - P8：6 串，均为答案行换行切分伪影（核心全角括号→分版半角括号，键行重切分；德语键本身经 p8.py 核对无损，见门 3）。其余移除串全部含 CJK，属中文讲解层替换。
- P1–P7 德语正文冻结成立：除上述裁定项外，无德语正文删除。

## 门 2 核心层冻结专项（NOCH EIN WORT 框）— 通过

- 核心原文（P7）：`«der Tankrabatt»（Seite 2）: die` + `gesenkte Steuer auf Benzin und Diesel.` + 中文 gloss `油价减税。`
- 本版实测（P7）：`«der Tankrabatt» (Seite 2): die` + `gesenkte Steuer auf Benzin und Diesel.` + 俄文 gloss `Скидка на топливо.`
- 裁定：**德语定义句逐字保留**，仅 gloss 本地化（中文→俄文）与括号全角→半角（DE 家族已发分版的统一式样，README #14；非删改译成俄语）。**无阻塞问题。**
- DE×EN 同胞版对照（`weekly-report-w45-de-en` P7）：同一框为 `«der Tankrabatt» (Seite 2): die` + `gesenkte Steuer auf Benzin und Diesel.` + `Fuel discount.`——与本版结构逐项一致（德语句同文、半角括号同式、仅 gloss 语言不同）。W43 DE×RU 同框亦为半角括号式（`«der Klassiker» (Seite 4): das größte …` + 俄文 gloss），家族先例一致。

## 门 3 P8 — 通过

- `tools/p8.py compare`：**CLEAN，150 noted = 150 noted，missing=[]，extra_count=0，uncertain=[]，keydiff=[137, 138, 139, 150]**；extract 两端均为 noted set 150/150。
- keydiff 逐项核实（全部为真实重定向，无括号提取伪影；p8.py 经 2026-10-21 俄文破折号修复后，含括号注文的键均正确解析）：
  - 137：核心中文键 `油价减税持续到十二月。（laufen = 持续）` → 分版 `Скидка на топливо действует до декабря.(laufen = действовать)`——DE→RU 翻译题键重定向，属实。
  - 138：核心 `我周二看足球。（schauen = 看）` → 分版 `Во вторник я смотрю футбол.(schauen = смотреть)`——DE→RU 重定向，属实。
  - 139：核心 `学校又开学了。（wieder begonnen = 又开始）` → 分版 `Школа снова началась.(wieder begonnen = снова началась)`——DE→RU 重定向，属实。
  - 140（不在 keydiff 中，正确）：键德语 `Am Sonntag schlafe ich eine Stunde länger.` 两端同文；分版提示为俄文 `В воскресенье я сплю на час дольше.`，指令 `Переведите на немецкий`——反向题键已核实无损。
  - 150：写作登记行改为俄文 apparatus（`открытое задание — пункты в рамке задания; образец — в рамке на этой странице(оценка по пунктам)`），范文德语正文未动。
- 括号/破折号类伪影：分版 P8 全角括号 0；键行 `.(…)` 紧贴式与核心中文键行式样一致（核心亦为紧贴），非缺陷。P8 分隔符 `— СТРАНИЦА N —` ×8（N=1..8），符合 ×RU 家具定式（核心为中文式 `— 第 N 版 —`，分版本地化正确）。

## 门 4 几何遮挡审计 — 通过

- `tools/occlusion_audit.py`（自测 6 类全触发、干净对照静默）：**分版 0 flags、核心 0 flags、NEW 0 flags**（`--core` 对照）。
- 同基线墨迹碰撞扫描（独立重测，ink_box 真墨迹，阈值 <5px）：分版 0 项、核心 0 项——P1 目录行 `Ferienwechsel & Herbst` 与级别标签 `A2→B1`（y=1436）无同基线邻接 <5px 情形（构建员 KIT 所称的 advance 宽度伪影在本校对的真墨迹扫描中不出现；无论如何不构成缺陷）。
- 全页 graze 扫描（文本墨迹 vs 后绘不透明矩形/图片，任意 >0% 重叠）：**全 8 页零重叠**——优于审计 30% COVER 阈值，含次阈值擦碰亦无。
- P6 图表标签与条形逐项实测（x=425，20pt sans regular；柱条起点 x=535）：
  - `родные` 墨迹右缘 **500.0**，净空 35.0px；`служба` 墨迹右缘 **495.8**，净空 39.2px；`пансионат` 墨迹右缘 **530.0**，净空 **5.0px**——与构建员宣称逐值一致（500/496/530，柱条 535）。
  - 标签墨迹盒与对应柱条矩形 x 方向无交集，重叠 **0%**；P6 卡面目视确认：`пансионат` 与柱条间有可见空隙，无接触、无截断。5px 净空虽小但为确定性渲染，属可接受（非阻塞）。
- P3-ex 流终点裁定：构建员所称 y=2582 为排版流盒终点（非墨迹）；本校对真墨迹实测 P3 末行 `Advent · Nebel`（基线 2563.17）墨迹底 **2563.4**，距页脚线 y=2580 净空 **16.6px**，审计 FOOTER 0 旗。**benign**——墨迹实际比宣称情形更宽松。另注：分版 P3 左栏末行基线较核心下移 29.7px（多一行所致），仍在页脚线之上，不构成缺陷。
- P7 栏终点与金句规则线（见门 6 末段）：墨迹底 1494.2，距规则线 1508 净空 13.8px，通过。
- P1 末行墨迹底 2515.8，与核心逐值相同，benign（核心同款）。

## 门 5 Gloss — 通过

- 按渲染后 gloss() 调用字符串本身以 `·` 拆分计数（构建树 content12/34/56.py，核心构建树对照）：
  - content12.py：核心 5 项 → 分版 5 项；content34.py：核心 5+5=10 项 → 分版 10 项；content56.py：核心 5+5=10 项 → 分版 10 项。**总计 25 项，逐项 1:1**。
- 25 项德语词头在分版渲染中全部存续（24 个唯一词头，`der Angehörige` 在 content12 与 content56 各出现 1 次，计 2 项，与核心一致）。
- gloss 前缀 `Пояснение — ` 在渲染中 6 处（5 个 gloss 框 + P1 bridge 注），与 W43 de-ru 定式一致。

## 门 6 P7 金句 — 通过

- 8 句德语原文在分版全刊 SVG 文本中**各恰 2×**（源文章 + P7 表），与核心逐条相等；源页与页码标签一一对应：
  1. `Vier Nächte Fußball hintereinander, dann ein ganzes Wochenende Liga.`——p4，`Seite 4 · B1`
  2. `Die Energiesteuer auf Benzin und Diesel sinkt um 14,04 Cent pro Liter.`——p2，`Seite 2 · A2`
  3. `Wer 50 Liter tankt, spart rund 8,35 Euro.`——p2，`Seite 2 · A2`
  4. `Die Schule hat nach den Herbstferien wieder begonnen.`——p5，`Seite 5 · B1`
  5. `Die Tage sind kurz, die Abende lang.`——p3，`Seite 3 · A2`
  6. `Zwei schwere Auswärtsspiele für die deutschen Teams.`——p4，`Seite 4 · B1`
  7. `Die deutsche Wirtschaft kommt langsam aus der Stagnation heraus, doch der Aufschwung trägt sich nicht selbst.`——p6，`Seite 6 · B2`
  8. `Es geht langsam aufwärts — aber von allein geht es nicht.`——p6，`Seite 6 · B2`
- 页码标签分布与核心逐值一致：`Seite 4 · B1`、`Seite 2 · A2`×2、`Seite 5 · B1`、`Seite 3 · A2`、`Seite 4 · B1`、`Seite 6 · B2`×2；P7 表上 8 句德语引文 + 俄译 + 标签齐全。
- P7 栏终点：右栏（x=1473）末行 gloss `Скидка на топливо.`（基线 1490.72）墨迹底 **1494.2**，距金句区规则线 y=1508 净空 **13.8px**；DE×EN 同胞版同位置末行 `Fuel discount.` 墨迹底 1491.0，净空 17.0px。构建员所称 1504.5（流盒终点，净空 3.5px）与墨迹实测均指向同一结论：**不越线，通过**；墨迹口径下余量实际大于宣称。
- P7 卡面目视：金句表与规则线分离清晰，词框完整，无越框。

## 门 7 读者园地 — 通过（绝不编造）

- 页上三事实齐全（P7 右栏 LESERBRIEFE 框内）：
  1. 无真实来信：俄文注 `Настоящих писем … не поступило` + 德语冻结句 `Bis Redaktionsschluss keine Briefe oder Texte — sie erscheinen in VOL.3.`；
  2. 无最佳 P8 作文：同注 `… и лучших сочинений не поступило`；
  3. 示例 + VOL.3 承诺：标签 `Пример редакции!` + 德语示例（冻结，署名 `die Redaktion`）+ 注文 `продолжение — в VOL.3.` 及德语冻结 invite `Die besten echten Briefe drucken wir in VOL.3.`。
- 德语 defer、示例、invite 三段与核心逐字相同（仅行切分与核心一致），未编造任何读者、来信、姓名、引言。
- 显性俄语公开征集句（P7 页上，独立成句）：`Присылайте настоящие письма — напечатаем лучшие в VOL.3.`——**判定：构成显性邀请**（祈使动词 Присылайте + 明确对象 настоящие письма + 刊登承诺 напечатаем лучшие в VOL.3.）。内容预告栏（P7 底部 `IN DER NÄCHSTEN AUSGABE` 内的 `Ihre Briefe: Schreiben Sie uns! …`）与他页练习提示均未计入；征集句独立存在，不依赖它们。

## 门 8 家具三方对照 — 通过（W43 实测胜出）

- 配对徽章（P1）：本版元素与 W43 已发同配对版 `files/weekly-report-de-ru/svg/p1-front.svg` **逐字节一致**：
  - `<text x="975" y="372" font-family="Noto Sans CJK SC" font-size="20" font-weight="700" fill="#a4553a" text-anchor="middle">ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ</text>`
  - 即 x=975 居中、y=372（替代核心副标题行原位）、20pt、sans 粗体、BRICK #a4553a。README #20 的泛写（插入式/他家族实例）不适用于 DE×RU 槽位，本校对以 W43 实测为准。
- 页脚 8/8：`Die Lucerna · НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК VOL.2 · ТЕКСТЫ НА НЕМЕЦКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ`；与 W43 页脚除 VOL.1→VOL.2 外逐字一致。
- 页码行 8/8：`Страница N из 8`（N=1..8）；P1 另有版头行 `НЕМЕЦКИЙ ЕЖЕНЕДЕЛЬНИК · VOL.2 · ФУТБОЛ · ТОПЛИВО · УХОД`。
- masthead：`Die Lucerna`（目标语德语用 Die；俄语无冠词适用问题），P1 元素与核心、W43 逐字节一致（x=975 y=262，168pt UnifrakturMaguntia）。
- P1 顶条、栏目俄文短式、题型/指令词汇与 W43 de-ru 定式一致（抽查：LEBEN · Жизнь、KULTUR · Культура、SPORT · Спорт、JUGEND · Молодёжь、VERTIEFUNG · Углублённо、SPRACHE · Язык、LESERBRIEFE · Письма читателей、NOCH EIN WORT · Ещё одно слово、SÄTZE DER WOCHE · Фразы недели、FEHLERKLINIK · Клиника ошибок；题型 Выбор ответа / Дополните предложение / Переведите / Письмо 等）。

## 门 9 PDF/卡片 — 通过

- 印刷 PDF `Die-Lucerna-VOL2-RU.pdf`：**4,069,552 B，8 页，1462.5×2025 pt**，sha256 `bfad19255f9ff8bdf9a96b7da7b0b9dad639fa85bc94931ec368a34ae5e090e6`——与 KIT §11 一致。
- 网页 PDF `Die-Lucerna-VOL2-RU-web.pdf`：**4,139,732 B，8 页，1400×1938 pt**，sha256 `08887763797799412e42084822510b189d89a7c34b005a09ecaea46b87a86894`（<10 MB）——与 KIT §11 一致。
- 卡片：8 PNG @1950×2700，**全部目视**：P1（徽章/刊头/照片署名/quiz）、P2（gloss 框）、P3（栏底与页脚分离）、P4（赛程表/照片署名）、P5（周计划表）、P6（图表标签与柱条）、P7（读者园地/词框/金句表）、P8（练习与答案流）——**无重叠、无截断、无越框**。
- 150 题分页与等级分布：登记表 10/18/18/18/18/18/12/38，A2 66 / B1 70 / B2 14，与核心一致；每页级别标签多重集与核心逐页相同；题号 1–150 连续。
- ABSTRACT.txt：俄语单行（仅尾换行），**无 ASCII 双引号**；含真实主题关键词（9-й тур Бундеслиги、скидка на топливо до 31 декабря、уход за родными、налог на электричество、смена каникул、возвращение в школу）+ 学习者搜索短语（`как учить немецкий по новостям Германии`、`читать Бундеслигу по-немецки`）+ 刊头 VOL.2 + 级别 A2–B2 + 150 упражнений。
- 图片署名行与核心一致且确已排版：P1 `Foto: Staff Sgt. Stephanie Jacobs, U.S. Air Force — public domain`；P4 `Foto: DVIDS (Armed Forces Soccer Championship, Destin, Florida, 2010) — public domain`；两图 base64 数据哈希与核心逐值相同；其余各页无署名图片，与核心一致。

## 非阻塞备注（不计入问题，不影响定稿）

- 构建员 KIT §5 散文中有 “P1 bridge” 一词（内部记录用语）；**分版 SVG 文本层中 bridge/桥接均为 0 命中**，出版物本身符合“讲解”用语要求。协调员如愿可顺手 scrub KIT 措辞，非定稿条件。
- P6 `пансионат` 距柱条墨迹净空仅 5.0px（0% 覆盖、卡面目视无接触）：余量小但确定性渲染已验证，属可接受，不列为问题。
- B2 仅 14/150：核心同款分布，未重定级，非问题。

## 问题清单

无。结论：ZERO PROBLEMS，可定稿（上架由协调员串行执行）。
