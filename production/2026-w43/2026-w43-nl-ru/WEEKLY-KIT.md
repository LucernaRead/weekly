# WEEKLY-KIT — De Lucerna VOL.1 · NL×RU（荷兰语正文 + 俄语讲解）

状态：**PASS**（独立校对 2026-10-22 一轮完成：版面零缺陷；仅 KIT 文档层
3 处登记更正，见 §4/§5 校对更正注与 §8）
期次：VOL.1 · 2026年第43周 · 2026-10-19（周一）–10-25（周日）
配对：目标语 = 荷兰语（Nederlands），讲解语 = 俄语（Русский）
交付目录：`files/weekly-report-nl-ru/`（svg ×8、cards ×8、印刷 PDF、网页 PDF、本 KIT）
建造目录：`hidden_files/weekly-report-nl-ru-build/`（荷兰语核心 build 的副本）

## 0. 交付物与实测针脚（落盘实测）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| De-Lucerna-VOL1-RU.pdf（印刷） | 9,966,645 | fa92236d04aa207cb6767c6c154800bb630ed898a2dcc306bed869d955cfeaeb |
| De-Lucerna-VOL1-RU-web.pdf（网页） | 3,391,548（<10 MB ✓） | c374f1f5bea5ef7022ce349b2a5486e7b645485c0a72f528b71854a7f3dc9f4c |

总量：**150 题 = A2 42 · B1 76 · B2 32**（与核心逐项一致，注册表 page/level 差异 = 0）。
分版题数：10 / 18 / 18 / 18 / 18 / 18 / 12 / 38（与核心一致）。

## 1. 基线证据（freeze.py baseline）

- 副本在未改一字时经 `tools/freeze.py baseline` 复现核心出货 SVG **8/8 逐字节一致**；
  核心 SVG sha256 前缀：p1 a8a2cc5d · p2 ea3f2a18 · p3 b61fbb1b · p4 eff31458 ·
  p5 1098c657 · p6 c941eb44 · p7 097fcfa7 · p8 feba8026。
- 交付前复核：核心文件哈希未变（建造全程未触碰核心目录）。
- 核心构建遵守 one-process 规则（tools/README 第 7 条）：全部内容模块只经单一
  driver `run.py` 在一个进程内运行；副本中从未单独运行任何内容模块（第 11 条）。
- 核心 P1 规则线 1844→1853 的既往几何修正属冻结现状，基线以当前出货 SVG 为准，已复现。

## 2. 变换方法

- 讲解层替换经 `scratch/transform.py` 完成：Python AST 解析各内容模块，只替换
  字符串常量的 value（258 个不同串，含核心全部中文讲解串与 P7 的 «Pagina 1–6»
  引文页标签），逐串计数断言（每串出现次数与映射表期望值相等才落盘）；结构性
  编辑（OUT 改道、PDF 名、P8 分隔符、#150 装置串、页脚 «Страница N из 8»、
  badge、答案字号）逐项计数断言后应用。
- 核心 gloss 版面方法已改名 `expl()`（1 处定义 + 22 处调用，与核心一致计数；
  原方法名按 RU 列先例不在此引述）。
- 禁用术语：终局纸面、KIT、本文件所述 operative 代码中中英两形均为 0；
  `scratch/transform.py` 为一次性变换脚本（值映射本身不含该词），按建造惯例 confined 于
  scratch/ 并在此披露。
- 目标语正文逐字节冻结：freeze.py diff 终局 added CJK = 0（全 8 页），图片数据
  载荷逐页与核心 sha 一致（P1×1、P2×1、P3×2、P4×1、P5×1）。

## 3. 家具逐项（RU 列定式，源：FR×RU KIT §3 + EN×RU KIT §3 先例）

- P1 badge（标题线槽位，19.5pt 粗体砖红居中，EN×RU 槽位先例）：
  «ТЕКСТЫ НА ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ»
- 页脚左（8 页逐页验证 ×1）：«De Lucerna · ГОЛЛАНДСКИЙ ЕЖЕНЕДЕЛЬНИК VOL.1 ·
  ТЕКСТЫ НА ГОЛЛАНДСКОМ · ОБЪЯСНЕНИЯ НА РУССКОМ»
- 页脚右：«Страница N из 8»（N=1..8，各恰 1 页）
- gloss 前缀：«Пояснение — »（SVG 中出现 9 处 = P1 桥注 1 + P2–P6 gloss 框 5 +
  P7 三栏注 3，与结构一致）
- P8 分隔符：«— СТРАНИЦА 1 —» … «— СТРАНИЦА 8 —» 各 1；«— PAGINA» = 0
- P7 引文页标签：«(Страница N)》，序列 1,2,2,3,4,5,6,6，与核心 «(Pagina N)» 计数
  逐条相等（1×1、2×2、3×1、4×1、5×1、6×2）
- 双语章节头（荷语原题 · 俄语短式）：ГЛАВНОЕ / ТЕПЕРЬ ВЫ / БЛИЦ-ВИКТОРИНА /
  ЖИЗНЬ / КОТОРЫЙ ЧАС? / УПРАЖНЕНИЯ СТРАНИЦЫ N / КУЛЬТУРА / СПОРТ / МОЛОДЁЖЬ /
  РАЗБОР / ЯЗЫК / КЛИНИКА ОШИБОК / СЛОВО НЕДЕЛИ / ФРАЗЫ НЕДЕЛИ（+ «дословно из статей
  этого номера») / ТЕСТ И ОТВЕТЫ / ОТВЕТЫ；栏宽受限短式：В ЦИФРАХ（P1 数字框）、
  ПАМЯТКА（P2 记忆框）、ОТМЕНЯТЬ?（P6 框）、А ВЫ?、КОРОТКО。
- P6 图表来源行：荷语冻结行 + 俄语 «Источник: исследование Wristler, опубликовано
  20 октября 2026 года; данные — запросы за октябрь прошлого года»。
- ⚠️ **名称分歧登记（待主线裁定）**：本版按任务简报用 «ГОЛЛАНДСКИЙ /
  НА ГОЛЛАНДСКОМ»；EN×RU KIT §3 的 12 语俄语目标名表作 «НИДЕРЛАНДСКИЙ /
  НА НИДЕРЛАНДСКОМ»。两种形式俄语均成立；本版全册统一 ГОЛЛАНДСКИЙ 系，
  与 EN×RU 的名表不一致，特此登记。

## 4. 键纪律与差异登记（注册表逐字节比对为权威）

核心 P8 经核心代码 + 出货 SVG 实证为 **dash 式且印全部 150 条注**
（content8.py：`N. key — note`、写作题 `N. ✓ note`，无长度阈值删注规则）。
本版沿核心式样印同一 150 集：**p8.py compare = CLEAN 150 = 150**（missing=[],
extra=0）。

注册表（核心 vs 本版，逐项比对）：
- **键（key）差异恰 3 项**，均为翻译题答案改指俄语：
  - #137: 核心键 «周日时钟拨回：多睡一小时！» →
    «В воскресенье часы переводят назад: спим на час дольше!»
  - #138: 核心键 «你的手机和电脑会自动更改时间。」 →
    «Твой телефон и компьютер сами меняют время.»
  - #150（装置项）: 核心键 «（开放题，范文如下）»、注 «范文见本版 H 区（87 词）» →
    键 «(открытый вопрос — образец ниже)»、注 «Образец — в разделе H этой страницы (87 слов)»
    （MODELO 词数两版同为 87，建造日志实测）
  - （校对更正 2026-10-22：本节初稿曾以荷语转述句充作核心键引文，与注册表及
    核心 P8 印刷键不符，已按注册表逐字节原文更正；版面本体未受影响。）
- **题干改向 2 项**（#139、#140 题干译俄，答案键荷兰语不变，P8 SVG 实证题干在位）：
  - #139 题干 «Неделя дизайна (Dutch Design Week) проходит в Эйндховене. → ___»
    （括号内保留英文原名）；键 «De Dutch Design Week is in Eindhoven.» 不变
  - #140 题干 «В воскресенье я спал на час дольше. → ___»；
    键 «Zondag heb ik een uur langer geslapen.» 不变
- 注文（note）差异 141 项（全部为中→俄翻译）；**未变 9 项全为语言中立**
  （时刻/算式/荷兰语时间短语）：#12（03:00 → 02:00）、#16（kwart over twee = 2:15）、
  #18（kwart voor drie = 2:45）、#46（71,50 = 19,50 + 19,50 + 32,50）、
  #79（hij → gaat kijken）、#84（301.000 + 246.000 = 547.000）、
  #101（kwart over drie = 3:15）、#102（half vier = 3:30）、#120（half drie = 2:30）。
- 题型（type）差异 150 项（注册表语言标记 zh→ru，属讲解层翻译，非内容变更）；
  page/level 差异 0。
- p8.py 行级 keydiff 列出 22 号 [2, 5, 11, 19, 20, 24, 35, 66, 70, 71, 73, 74, 78,
  82, 83, 94, 109, 127, 137, 138, 146, 147]：除 #137/#138 外均为 13.0pt 重排 +
  注文译文进入同行造成的行级伪影（tools/README 第 13 条口径）——注册表逐字节
  比对证明这些号码的键与核心全等，伪影据此证伪。

## 5. 字号调整登记（P8 答案段）

- 现象：俄语注文总量 3,967 字（核心中文 2,636 字），核心字号 13.5/1.16 下答案段
  溢出（流尾 2553/2582 > 答案区底 2552）。
- 处理：**答案段字号 13.5 → 13.0（行高 1.16 不变）**，不删任何注。先例：
  DE×RU 同因将答案段定为 13.0/1.16（DE×NL 实测值，tools/README 已录）；本版
  沿用同一落点。调整后答案段流尾 y=2478 < 2552 ✓，卡面留白充足。
- （校对复核 2026-10-22：字号裁定成立。注册表实测注文总量为俄 4,775 字 /
  核心 2,491 字——本节初稿的 3,967 / 2,636 口径未能复现，以注册表数为准；
  方向与量级无误。实测墨迹底：本版答案段 2530.4 < 核心自身 2539.4，
  距页脚线 2580 约 50；且 13.0 为 NL 目标家族主流（已入仓扇出 5/6 版为
  13.0）。）

## 6. 自校缺陷与修复（建造者全量自校一轮）

机械门初跑：occlusion_audit（自检先行通过）报 12 旗，其中 10 旗为新增、全部经
像素/墨迹复核为真缺陷（俄语串偏宽），2 旗为核心自有（见下）。修复全部为讲解层
串长压缩，不动版式与目标语：

- A. P1 衬线行 EDGE（墨迹宽 2044.6 超页）：压缩为 «…· ЧАСЫ НАЗАД · КАНИКУЛЫ ·
  ADE 30 ЛЕТ»（墨迹 1770.1，三话题俱全）。
- B. P1 顶带 TEXTX（中串压右日期串 98.4px）：先删 «КАЖДУЮ НЕДЕЛЮ ·» 段；看图复核
  仍几乎贴死（墨迹间隙 ≈0)，再删 «ELKE WEEK» → 终局墨迹间隙实测 63px。
- C. P1 数字框题 BOXTITLE：«НЕДЕЛЯ В ЦИФРАХ» → «В ЦИФРАХ»。
- D. P1 趋势框：副题 «Что Нидерланды ищут в Google» → «Что ищут в Google»；
  快照行整行溢出（墨迹右 2247.8）→ «Снимок 20 октября: цифры — оценки»。
- E. P2 记忆框题 BOXTITLE：«ЗАПОМИНАЛКА» → «ПАМЯТКА»。
- F. P6 框题 BOXTITLE+EDGE：«ОТМЕНЯТЬ ИЛИ НЕТ?» → «ОТМЕНЯТЬ?»。
- G. P8/P2 配对题指令 TEXTX（«Сопоставьте слово и значение» 侵入邻栏正文）：
  两处同源串改 «Сопоставьте пары слов»。
- H. P7 第三栏溢出（俄语注使栏底 1854.5 越过短语带横线 1698；核心栏底 1678.5）：
  诊所/词条/读者信六条注电报式压缩至栏底 = 1678.5，与核心逐点相同。
- I. P1 本周词俄注视觉缺陷（审计口径外）：俄注 2 行时，1853 横线恰穿两行之间
  （行1 墨迹止 1850、行2 起 1856、线 1853–54)，且行2 墨迹止 1872 距快讯框顶
  1874 仅 2px——注文压回 1 行 ««De klok verzetten» — менять время на часах.»
  （墨迹 412.4；“本周后退一小时”义已在正上方荷兰语原行 «deze week één uur
  achteruit» 中，释义完整）。像素复核：注文墨迹单带 1831–1850，线在其下 ✓。

继承旗（非本版缺陷，勿动）：P2 «adviesdata: scholen mogen afwijken.» 底墨迹
993.8 > 框边 993.1（0.7px）、P3 «Kaartjes: € 32,50; studenten € 19,50.» 底墨迹
1235.7 > 1235.0（0.7px）——与核心同坐标同值，系冻结荷兰正文的次像素擦碰。

终局机械门（修复后重跑全套）：
- occlusion_audit：2 旗（即上述继承旗），**NEW vs core = 0**
- 同行墨迹扫描（README 第 10 条，scratch/rowcheck.py）：本版 0 碰撞（核心亦 0）
- p8.py compare：CLEAN 150 = 150
- freeze.py diff：added CJK = 0（8 页）
- P6 图表元素级检查（README 第 12 条）：条形坐标/宽度与核心逐条同
  （250/204/50/5)，标签在条形上方、审计 COVER = 0
- 日历对照真实 2026（Europe/Amsterdam)：10-17 周六（假期/DDW 起）、10-18 周日、
  10-19 周一（Noord 复课）、10-20 周二、10-21 周三、10-22 周四、10-24 周六、
  10-25 周日 wintertijd 03:00→02:00、11-01 周日 Robinson 开播——程序校验 9 项全合
- 残留扫描：讲解层荷兰语家具串 = 0（«— PAGINA» 0、P7 «(Pagina N)» 0；
  正文冻结荷语不计）；CJK 全册 = 0；讲解无国际政治内容
- 8 张卡逐张目检通过

## 7. 图片与授权（与核心同一批，载荷逐字节同核心）

- P1：Westertoren, Amsterdam — Wim van Rossem / Anefo, Nationaal Archief — CC0
- P2：怀表 — photo-nic.co.uk / Wikimedia Commons — CC0
- P3a: Kinderdijk 风车 — Nationaal Archief / Wikimedia Commons — CC0
- P3b：秋林 — Vovogov90 / Wikimedia Commons — CC0
- P4: 1912 荷兰国家队 — Spaarnestad Photo / Wikimedia Commons — 公有领域
- P5：运河船 — W. Punt / Anefo, Nationaal Archief — CC0

## 8. 独立校对记录（2026-10-22，校对员独立复跑/复测）

- freeze.py baseline：8/8 逐字节复现核心；校对收尾核心 8 SVG 哈希与开局快照全同。
- freeze.py diff：全 8 页 added CJK = 0，本版 CJK 总量 = 0；图片载荷 6 个逐页与核心 sha 全同、位置全同、署名逐页全同。
- p8.py compare：CLEAN 150 = 150（missing=[]、extra=0）；行级 keydiff 22 号经注册表逐字节比对证伪为伪影（注册表键差异恰 {137, 138, 150}）。
- 注册表双导出比对：总量 150 = A2 42 · B1 76 · B2 32、逐页 10/18/18/18/18/18/12/38 两版全同；page/level 差异 0；注差异 141、未变 9 项 {#12,16,18,46,79,84,101,102,120} 全语言中立；题干改向 {139,140} 在 P8 实印核实；范文两版同为 87 词。
- 150 键全部由校对员自荷语正文/题干手工重推导，零分歧（含两组配对题字母映射、算术题 #46/#84/#85、对话完形 #145–149、翻译题 #137–140 忠实度）。
- occlusion_audit（自检先行）：2 旗均为核心自有 0.7px BOXTITLE（P2 adviesdata 行、P3 Kaartjes 行），与核心同坐标同字号逐字节同元素，属冻结正文继承，NEW vs core = 0。
- 同行墨迹扫描（自写，审计墨迹盒）：0 真碰撞（唯 P1 目录 Pag. 标签与题名 4.0 设计间隙，与核心逐行同值）；P1 顶带中串↔日期墨迹间隙实测 69.3（建造者报 63，口径差，结论同）。
- P6 图表元素级：条形 (250/204/50/5 × h18) 与核心逐条全同；任意覆盖率口径下文字被后绘图形覆盖 = 0。
- P7：短语荷语串多重集与核心全等（diff 增删全在讲解层）；页标签序列 (1,2,2,3,4,5,6,6) 与核心逐条相等；第三栏末行基线与核心同位（1660.0），墨迹底距 1698 横线约 33。
- P1 本周词（缺陷 I）：俄注单行墨迹带 1831.0–1850.5，1853 横线在其下；卡面像素复核：1851–1852 行与 1855–1873 行（x 1451–1885）暗像素 = 0，原 2px 贴框问题消失，释义完整。
- 字号裁定（§5）：成立，复核数据见 §5 校对注。
- 家具：徽章/页脚 ×8/«Страница N из 8»/gloss 前缀 9 处/P8 分隔 ×8/P7 俄式标签/双语章节头全表逐项在版；目标名全册统一 «ГОЛЛАНДСКИЙ» 系（主线裁定），«НИДЕРЛАНДСКИЙ» = 0；残留荷兰家具串 = 0；禁用术语纸面/KIT/operative code = 0（改名实证 def expl 1 + 调用 22；scratch 无例外项）。
- 日历（Europe/Amsterdam 程序校验）：10-17 六、10-18 日、10-19 一、10-20 二、10-21 三、10-22 四、10-24 六、10-25 日（wintertijd 03:00→02:00）、11-01 日，9 项与版面全合。
- 文档更正（不动版面）：§2 改名披露改为不引原词式；§4 三处核心键引文按注册表原文更正；§5 注文总量按注册表实测更正。
- 最终针脚（校对员落盘实测，与建造者自报全合）：印刷 10,592,220 B / 3d2baf87…；网页 3,784,239 B / 394a6a72…；各 8 页。

## D5 rebuild (13 Nov 2026; this build supersedes all earlier deliverable figures in this KIT)

- Install: `hidden_files/d5-redo/tools/mechanism-w47/apply_variant.py --svglib 2026-w43-nl-ru/svglib.py --target nl --reader ru --week 2026-w43` (`--check` dry-run first, RC=0). `_D5_READER = "ru"`. Routing unit test `test_d5_routing.py`: FAILURES: 0. D1 fix2 retained.
- Pre-rebuild census (`d5_census.py`, D5 elements in the pre-D5 SVGs): 590 (328 Latin-in-CJK-sans + 262 Cyrillic-in-CJK-sans).
- Baseline (pre-D5 rebuild, venv, disk-measured): run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; print `De-Lucerna-VOL1-RU.pdf` 10,329,408 B (sha256 `93a883a26fa18fcce9c26efe2675aa3b0a1d6750c0472e517a0ecb76cc922624` — pre-D5 build, superseded); web `De-Lucerna-VOL1-RU-web.pdf` 1,039,668 B (sha256 `a4120a88620dbcc2b2cf0bd185d71307aec76e9fe17fed16f25f7c4cbad95792`). Text layer print vs shipped web PDF multiset diff 0 (Python `len()` chars). The KIT-recorded print/web figures predate the §1.1 style port and the D1 re-render and are superseded by the disk-measured baselines above.
- Defects found by the 17 gates (run 1) and fixed by size only — text unchanged throughout:
  - Feature heads `ETEN BESTELLEN WORDT HELDER` / `EROPUIT IN DE HERFSTVAKANTIE` already fit at 25 pt (Noto Sans routing; advance 406.7/407.7 px vs column 422.5 px) — no change; head_check passed in run 1.
  - P1 p.text `IN DEZE EDITIE　В ЭТОМ НОМЕРЕ` over +1.6 px (right) → size 24 → 23 (`content12.py:91`).
  - Exporter note: the `IN DEZE EDITIE …` panel heading shrank 24 → 23 pt, crossing the exporter's ≥24 pt heading heuristic, so the scratch exporter (`export_text_w43nl.py`) gained an explicit heading rule for it (same pattern as the P3b italic-serif fix). The re-export is still byte-identical to the shipped `.text.md`.
- P8: 244 → 244 lines, slack to footer rule 36.5 → 36.5 px (unchanged by §4; `content8.py` untouched).
- Gates (full re-run after fixes, run 2): **ALL-GREEN** — run.py TOTAL 150, 0 FLOW OVERFLOW, 0 HEAD TOO WIDE; head_check 0; d5 census 0; render RC=0; webpdf RC=0, web < 7 MB; occlusion 0 flags; p8 extract 150/150; p8 compare CLEAN; freeze baseline 8/8 byte-identical; freeze diff vs baseline added CJK 0; spill 0 SPILL; boxtitle 0 DEFECT; edge 0 TOUCH 0 NEAR; creambox PASS 0 defects; text layer print=web multiset 0, text.md BYTE-IDENTICAL; census_quotes 0 defective. Logs: `hidden_files/d5-redo/scratch-2026-w43-nl/gates/2026-w43-nl-ru/` (`GATES-SUMMARY.txt` master). Full record: `production/notes/2026-w43/g-nl/scratch-d5-rebuild-nl/D5-REPORT-2026-w43-nl-ru.md`.
- New deliverables (rebuilt 13 Nov 2026): print `De-Lucerna-VOL1-RU.pdf` 9,966,645 B, sha256 `fa92236d04aa207cb6767c6c154800bb630ed898a2dcc306bed869d955cfeaeb`; web `De-Lucerna-VOL1-RU-web.pdf` 3,391,548 B, sha256 `c374f1f5bea5ef7022ce349b2a5486e7b645485c0a72f528b71854a7f3dc9f4c` (< 10 MB); text-layer web `2026-w43-nl-ru.web.pdf` 1,157,010 B, sha256 `8474f4cf780a53330734fee99fc7d058763a6a2f600b9ce0a91127e1a3816a4f` (< 7 MB); `2026-w43-nl-ru.text.md` 49,288 B, sha256 `9e8a4e6e30210abffdf5137a69084e32ca895b8c3981935f86df4789130a7096`, **BYTE-IDENTICAL** to the shipped `issues/2026-w43/2026-w43-nl-ru/2026-w43-nl-ru.text.md` (exported from the build source with the scratch exporter `hidden_files/d5-redo/scratch-2026-w43-nl/export_text_w43nl.py`, W46 generic AST exporter + W43-nl italic-serif fix + `IN DEZE EDITIE` heading fix).
- Status: builder DONE, all gates green. Independent re-proof (SOP §8) is the coordinator's separate step; no commit, no push by the builder.
