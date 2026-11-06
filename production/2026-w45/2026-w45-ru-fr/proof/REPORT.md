# W45 RU×FR 独立校对报告（proofread, read-only）

**结论：ZERO PROBLEMS，可定稿。** 下述 9 项 SOP §8 检查全部独立重跑通过，KIT 数字逐项核对一致（仅金句计数表述有一处口径说明，见 §5 注，不构成问题）。
未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git、未写入任何源目录（W43、核心、本版 files/ 均只读；校对结束复哈希：本版 8 SVG 与开工时一致）。

**开工查重：** 2026-10-27 18:55 UTC 首次见本版文件时间戳距当时 <2 分钟，但无任何渲染进程；75 秒后复查零新写盘（最后写盘仍为 18:55:07 WEEKLY-KIT.md），按协调员裁定正常开工。

## 1. 基线与核心完整性 — 通过
- `tools/freeze.py baseline`（以原始核心构建树 `hidden_files/weekly-report-w45-ru-build` 全新重跑，非 builder 的 baseline 副本）：**8/8 逐字节相同**，核心哈希与任务基线前缀全对（p1 8bfcb7e2…、p2 5b35f1d7…、p3 8be9ba7f…、p4 9d699050…、p5 f49d0ed8…、p6 8559d61d…、p7 961119d6…、p8 2738ae04…）。
- 事后核心重哈希无变化；`freeze.py` 自身亦报告 shipped core SVGs unchanged。
- 本版构建独立重跑（`freeze.py baseline` 以 ru-fr 构建树对本版 SVG）：**8/8 逐字节相同**（p1 d513d03e…、p2 48003025…、p3 d3d1a8ef…、p4 28f872c0…、p5 df751ed5…、p6 697b64a8…、p7 c5f43b47…、p8 66e4d713…，与 KIT §12 全对）。

## 2. freeze diff — 通过
- `freeze.py diff`：8 页 added CJK 均为 0；渲染 SVG 原文件 CJK 字符总数 = 0（核心为 128/208/133/129/115/146/284/844，全部清零）。
- 西里尔词元多重集（按连续西里尔串拆分，即任务口径）：P2–P8 与核心**完全相等**，总数 443/338/306/316/354/397/641，与任务数字逐项一致；新增词元 0。
- P1 差异只含备案的两处，逐项核实：(a) y=372 徽章替换行移除 ЕЖЕНЕДЕЛЬНАЯ/ГАЗЕТА/ДЛЯ/ИЗУЧАЮЩИХ/РУССКИЙ/ЯЗЫК/НАСТОЯЩАЯ/РОССИЯ/ПО/РУССКИ（ПО-РУССКИ 拆分计 2）；(b) y=330 版头首段法语化移除 РУССКАЯ/ГАЗЕТА（P1 的第 2 个 ГАЗЕТА）。合计移除 12 词元、新增俄语词元 0、主题词 ПРАЗДНИК/СКИДКИ/ФУТБОЛ 保留。无未备案俄语丢失。
- svglib 源码 docstring 的「重阳」在核心构建树与本版构建树 line 120 逐字相同，属源码注释，不进入渲染 SVG（上条原文件 CJK=0 已证）。

## 3. P8 — 通过（CLEAN，真改动仅 137/138）
- `tools/p8.py compare`：**CLEAN，150=150，missing=[]，extra=0，uncertain=[]，keydiff=[83,137,138,148]**。
- 独立 dash-parse（答案区文本按首个 " — " 切键，不用 p8.py 的括号分支）：**key diffs = [137,138] 仅此两项**，150 项齐全无缺漏。
  - 83：印出键两版均为 `B`；p8.py 之差是括号提取 artifact——核心键后括号注为全角（周三、周六、周日），法语版为半角 (mercredi, samedi, dimanche)，工具把注前文本并入键。非真改动。
  - 148：印出键两版均为 `A`；同理，核心注（阳性）/法语注 (masculin) 造成工具键差。非真改动。
  - 137：俄→法重瞄准。习题区指令 `Traduire en français`，俄语题干 `В среду, 4 ноября, — выходной.` → 键 `Mercredi 4 novembre, c'est un jour férié.`，忠实翻译。
  - 138：俄→法重瞄准。题干 `Промокод — это код со скидкой.` → 键 `Un code promo est un code de réduction.`，忠实翻译。
  - 139/140：反向（法→俄，`Traduire en russe`），键逐字节相同（`В субботу «Краснодар» играет с ЦСКА.` / `Поздравляю с Днём народного единства!`）。
  - 150：键 `✓` 两版相同；范文体为俄语原文，源码 MODELO 两版逐字相同（484 字符），`split()` 计 **84 词**，与 P8 注（84 mots）一致；"80–100 слов" 题面范围未动。
- 该模式与 W43 已发同配对版先例逐项对应：W43 KIT 记载 137/138 俄→法、139/140 反向键相同；本版 W43 实测 P8 习题区亦为 137/138 `Traduire en français`、139/140 `Traduire en russe`。
- 括号形式：本版 P8 全角括号字符数 = 0（核心 12 字符 = 6 对全角注），法语注全为半角括号；分隔符 `— СТРАНИЦА N —`（N=1..8）三版（核心/本版/W43）逐字相同。
- P8 keys flow（独立重跑日志）：ends y=2375（bottom 2540），规则线 2580 之前，余量充足。

## 4. 几何审计 — 通过
- `occlusion_audit.py --selftest`：6 类 planted 全触发、clean 对照静默；本版运行 **0 flags，核心对照 0 flags，NEW vs core = 0**。
- 自写同基线 advance-width 间隙扫描（<5px）：核心与本版 8 页均为 0 flags。
- P6 图表逐元素检查：4 条 bar 标签（Дома с семьёй / Короткая поездка / Ярмарка или концерт / Просто выспятся）与数值 34%/28%/22%/16% 在核心相同坐标（基线 1634/1680/1726/1772），**后绘 rect 重叠 = 0**；RU 的 P6 无 ES 式冻结压字，0 重叠为正常正确结果。

## 5. 计数与结构 — 通过
- 独立重跑日志：**150 题；A2 51 / B1 75 / B2 24；分页 10/18/18/18/18/18/12/38；范文 84 词；P7 col3 ends 1727.58；FLOW OVERFLOW / HEAD TOO WIDE 出现 0 次。**
- gloss：按 `·` 本身拆分源码调用，9 次调用、共 **26 项**，逐 call 与核心相等（content12 3/3/3、content34 3/3/3、content56 3/2/3）；俄语词头顺序未动，只译讲解层；渲染后 gloss 盒 9 个（P2×3、P3×2、P4×1、P5×2、P6×1），前缀 `Note — ` 与 W43 已发版一致。
- 图片载荷：P1/P4/P5 各 1 张，data-URI sha16 与核心逐字节相同（P1 299e7e477ee35be9、P4 db6982729417df21、P5 75b89f36224f4ee3）；其余 5 页两版均无内嵌图。
- 金句：8 句俄语原文在核心与本版中出现位置/次数**完全相同**。注（口径说明，非问题）：单看 P7 页内每句为 1 次（引号形式）；全刊计每句恰 2 次（源页 P1–P6 各 1 次 + P7 金句栏 1 次）。KIT §4「2×」按全刊口径成立；冻结判据（核心=本版、无增删）成立。
- 图片说明与核心逐字相同（P1 Toxer427 CC0、P4 作者未知 1912 公有领域、P5 Престон Керес USDA 公有领域）。

## 6. 家具三方比对（本版 vs W43 已发版 vs 核心）— 通过
除 VOL.1→VOL.2 与当期主题词外，全部与 W43 已发版逐字一致：
- 徽章：`TEXTES EN RUSSE · EXPLICATIONS EN FRANÇAIS — L'ÉDITION POUR LES LECTEURS FRANCOPHONES`；顶条：`КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · CHAQUE SEMAINE · LE RUSSE QUE LIT LA RUSSIE`；页脚（8 页全）：左 `Lucerna · HEBDOMADAIRE RUSSE VOL.2 · TEXTE EN RUSSE · EXPLICATIONS EN FRANÇAIS`（单数 TEXTE），右 `Page N sur 8`。
- 栏目名：ГЛАВНАЯ ТЕМА · Le thème principal、НЕДЕЛЯ В ЦИФРАХ · En chiffres、В ЭТОМ НОМЕРЕ · Sommaire、СЛОВО НЕДЕЛИ · Mot de la semaine、УПРАЖНЕНИЯ · Exercices de la page N、ФРАЗЫ НЕДЕЛИ · Phrases de la semaine (mot pour mot, de cette édition)、СЛЕДУЮЩАЯ НЕДЕЛЯ · La semaine prochaine (VOL.3)、ТЕСТ И ОТВЕТЫ · Test et réponses、ОТВЕТЫ · Réponses — classées par page ; cherchez votre numéro。
- P6 免责句：俄语行后接法语句 `Un sondage d'exercice de la rédaction, pour s'entraîner — pas de vraies statistiques.`，与 W43 逐字相同；目录表 Стр. 8 行级别标签 `все` 保留未译，与核心/W43 一致。

## 7. P7 读者园地 — 通过（按协调员裁定不重报）
- 沿用核心示例（俄语，`— М. (пример от редакции)`）+ 俄语披露全文未动，只译讲解层：法语披露 `Aucune lettre réelle reçue — exemple de la rédaction ; promesse pour VOL.3.` 2 行；无新读者/来信/姓名/引言编造；VOL.3 征信预告与核心一致。
- 盒几何与核心逐值相同：三盒 200–1008.08 / 1020.08–1242.58 / 1254.58–1727.58（含 letters 盒 x=1451, w=434, h=473, 盒底 1727.58）；披露第 2 行基线 1738.28 两版相同；目视文字可读，遮挡审计 0 flags。按 ru-en 先例的协调员裁定，此核心固有接触为非阻塞，几何一致 + 可读即通过。

## 8. 三处法语缩短 — 通过（保义 + 无压线）
1. P7 诊所注 #1：`« с » + instrumental : с Днём единства.` 单行（y=417），语法点（с + 工具格）与完整例句保留。
2. P7 词盒注：`промокод = code promo à la caisse.` 单行（y=1230.67，实测宽 334.3px < 390 内宽），结账含义保留。
3. P1 本周单词行：`сокращённый день = une journée raccourcie.` 单行（y=1830.30）；1844 横线在该行基线下方，无第二行可压，目视与遮挡审计（0 flags）均确认**现已无压线**（修复了本版自身 NEW LINEX）。
- 完整形式保留：P2 单词条 `journée de travail raccourcie`、P7 bridge `сокращённый день journée de travail raccourcie`、P7 习题键同形；三处缩短均未造成信息丢失。

## 9. ABSTRACT / PDF / 卡片 — 通过
- ABSTRACT.txt：法语单行（348 字节，1 个换行结尾），无 ASCII 双引号；含真实主题关键词（4 novembre jour férié、3 novembre journée plus courte、soldes 11.11、14e journée du championnat 6–8 novembre）+ 学习者搜索短语（francophones qui apprennent le russe / vraies actualités russes）+ A2–B2 / 150 exercices。
- 两 PDF 均为 8 页：print `Lucerna-VOL2-FR.pdf` 13,518,341 字节，sha256 `3bfa593e86e2a2479e46943e0b7aecdacb5b5f843755918b169ce01fd4cb0d0f`，页尺寸 1462.5×2025 pts；web `Lucerna-VOL2-FR-web.pdf` 3,197,163 字节（<10 MB），sha256 `df56e15e4fb717a1e827456ada2e62bcec1d8bb9bb70a9eacb785867c940d71e`，页尺寸 1400×1938 pts；尺寸与 SHA 与 KIT §12 全对。
- PDF–SVG 一致性（针对中途服务重启后仅重跑 render.py 的情形）：print PDF 逐页文本提取与 SVG 对比，>4 字文本元素 8 页均为 **100% 对应**（含徽章、8×页脚、P8 137/138 法语键、P7 法语披露、CJK 0）；web PDF 按 render.py 设计为 JPEG 图片页（无文本层，属预期，非缺陷）。PDF 时间戳 18:50 晚于 SVG 18:48、与卡片 18:50 一致，无半成品。
- 8 卡全部目视（P1–P8，含 builder 未看的 P2/P3/P4/P5/P8）：1950×2700 PNG；无溢出、无遮挡、无页脚碰撞；P1 徽章/版头/顶条、P6 图表、P7 读者园地、P8 答案区（止于页脚上方 ample 余量）均清晰可读。

## 待裁定项（单列，不因此判不通过）
**徽章槽位：实测支持 builder（遵循 W43 已发版），而非 README #20 的泛化描述。**
- 三方实测：本版与 W43 已发版 P1 徽章**逐字、逐位、逐样式相同**——x=975, y=372（在位替换原副标题行），20pt 粗体，fill #a4553a，居中；版头行 y=330 亦同位（本版 VOL.2 + 当期主题词，W43 VOL.1 + 当期主题词）。
- 三版 P1 均**不存在 y=574 的文本元素**，即 README #20 的 (975,574) 22pt 插入槽位在本版与 W43 已发版中均无实例；该描述对应的是法语作目标语的情形，不适用俄语目标 × 法语读者本版。
- 按协调员家具规则（已发同配对版为准），与 W43 已发版一致即不列为问题；请协调员确认 README #20 的适用范围说明是否需加注「FR 作目标语」限定。

## 审计输出路径
- `hidden_files/w45/ru-fr-proof/REPORT.md`（本文件）
- `hidden_files/w45/ru-fr-proof/baseline.json`（核心基线 8/8）、`edition-repro.json` + `edition-rerun.log`（本版重跑 8/8、计数、零溢出）
- `hidden_files/w45/ru-fr-proof/diff.json`（freeze diff）、`p8.json` / `p8-core.json` / `p8-ed.json`（p8 compare/extract）、`occlusion.json`（0 flags / NEW 0）
- `hidden_files/w45/ru-fr-proof/check1.py`、`check1b.py`、`check_furn.py`、`check_p8.py`、`check_p8dash.py`、`check_rest.py`（独立复核脚本）、`pdftext/print.txt`、`pdftext/web.txt`（PDF 文本提取）
