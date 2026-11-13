# GATE-LOG — 2026-W47 ru-es proof2 机械门实跑证据（重建版）

版目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-ru-es/`
核心：`~/workspace/weekly-git/production/2026-w47/core-ru/`（fix1 `f11854bf`）
工具：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；正典 creambox `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py`（md5 `ee7a55d8b2057cf4ad42a97bb1197383`，与 proof1 验过的同一版本）。
本目录下证据文件：`svg-before.sha256` / `svg-after.sha256`、`p8-extract-core.json/.log`、`p8-extract.json/.log`、`p8-compare.json/.log`、`occlusion.json/.log`、`adjudicate/sheet1–7.png`、`adjudicate.py`、`freeze-baseline-core.log` / `freeze-baseline-ed.log`、`freeze-core-copy.sha256` / `freeze-core-shipped.sha256` / `freeze-ed-copy.sha256` / `freeze-ed-shipped.sha256`、`freeze-diff.json/.log`、`freeze-core/` / `freeze-ed/`（build-copy）、`s11.log`、`check_core.log`、`creambox-all.log` / `creambox-backup.log`、`d1d2d6.log` / `d1d2d6.py`、`ink_measure.log` / `ink_measure.py`、`spill.log` / `spill.py`、`kicker-pixel.log`、`p1-kicker.png`、`p1-wowword.png` / `p1-wowword-web.png`、`pages/p1–8.png` + `web-p1–8.png`、`regression.log` / `regression-content.diff`、`keycheck.py` / `keycheck-mechanical.json` / `keycheck-150.json`、`run-gates.sh`、`probe.txt`。

## §0 身份（磁盘实测，开工与收工两次）

- `Lucerna-VOL4-ru-es.pdf` SHA `64cb48f90dea70553a76e70c8cb9bc75ffa571c1ceaa8318c8655b47b80cf7c3`，21,278,615 字节 ✓
- `Lucerna-VOL4-ru-es-web.pdf` SHA `7af50086c326e1d5bcd78afa746663e3a0d1c5b5b35735a719a17006b694b051`，3,387,465 字节 ✓
- `2026-w47-ru-es.text.md` SHA `a4044bf0b7570abb58eaf7c0e53c71870f7182c3b375991bdb6eac721502ef1b`，64,215 字节 ✓
- core-ru：印 `d60fbd6c503f2442ae5a49bf475518034563816af27a05f8bbba2dc1383cab81` / 31,429,147 B；网 `2f995f1deb75fce116b33a10b9da816fb415a7bac79a258d817c4f99731e4197` / 4,025,834 B；文 `348511e061c28019b56d81bcd6e006ff1d7ddae3e49c7b599668216a6b90f8cc` / 60,953 B ✓
- 三 SHA 与任务先验完全一致，复校前后不变。`git status`：版目录与 core-ru 未入仓（`??`），无 tracked 修改；freeze 运行前后 shipped SVG SHA 未变（`svg-before.sha256` vs `svg-after.sha256`，diff 空）。

## 1. Occlusion 审计（`tools/occlusion_audit.py`，真实命令，未加 --selftest）

- 全版运行：`42 flags {'TEXTX': 42}`，COVER 0 / LINEX 0 / FOOTER 0 / EDGE 0 / BOXTITLE 0，rc=1（仅 TEXTX 有标记）。（注：日志首行 `selftest OK …` 为工具自身每次运行打印的内部自检行，非本次附加 `--selftest`。）
- 逐个像素裁定（`adjudicate.py`：按 JSON 坐标从 1950×2700 卡片裁图、2× 放大、红框标墨迹盒，7 张 contact sheet 逐张目视）：
  - P1 #1–#10、P2 #11–#16、P3 #17–#19、P4 #20–#26、P5 #27–#28、P6 #29–#32、P7 #33–#40、P8 #41–#42。
  - 全部 42 项均为 3–8px 的墨迹盒侧边距重叠（相邻标点/词间、引号、全角空格分隔段），渲染字形均未相触。**42/42 CLEAR，0 真缺陷**。与 KIT 自查数（42 TEXTX）一致；与 proof1 旗标集仅差 1 项——同一 P6 旗标因 D1 标题拆分改 run（`?　DATOS DE PRÁCTICA` → `?　`），位置与重叠量（3.3×19.5px）相同。

## 2. 正典 creambox.py 全版扫描（+45px 窗口 + 逐行 clearance + P7 toolbox）

- 32 个奶油框（P1 4、P2 8、P3 4、P4 2、P5 3、P6 8、P7 3、P8 0）；全部为纯填充无描边（stroke=False），已覆盖在扫查内。
- 负窗口余量（inside-only）：0。BELOW-WINDOW 95 行（+28.0 ×25、+32.0 ×41、+34.0 ×4、+37.0 ×25），全部为下一标题假阳性，属已分类的既有项。
- **P7-TOOLBOX：3 框，最小框内余量 +11.9px，最小降部余量 +5.9px**（通过）。
- 与 #1 备份扫描逐行相同（路径归一化后 diff 0 行）。
- 唯一临界：P2 `А ВЫ?` 框（y=795，底 1159.0）末行 `para Ded Moroz.` 启发式 desc-clear −1.0；PIL 真墨迹：降部最末墨行 ink_bottom = 1159.0，框底 1159.0——**0px 贴边、0 漫出**（见 PROOF-NOTE O3）。

## 3. p8 compare（显式 `--core-p8` / `--edition-p8`，core `core-ru/svg/p8-test.svg`）

- `core 150 noted / edition 150 noted / status: CLEAN / missing=[] extra_count=0 uncertain=[] / keydiff=[137, 138, 139, 140]`，rc=0。
- 直接比对 core `ru-p8.json`（150 键）：差异亦恰为 [137, 138, 139, 140]——E 节 RU→西语翻译题，印键为西语译文（设计如此）；其余 146 键与 core 字节一致。
- `p8.py extract`：`noted set = 150 of 150`（core 与 edition 各 150）。
- Q137 em-dash 提取截断为已知非缺陷：SVG 原行 `137. Martes 17 de noviembre, Día del Estudiante. — Ver página 2` 完整；仅解析器在 em-dash 处截断键。

## 4. freeze / freeze diff

- **标准口径（core）**：`freeze.py baseline --build <core-ru> --core-svg <core-ru>/svg --out scratch/freeze-core`：rc=0，`baseline: 8/8 SVGs byte-identical`；**直接 SHA-256 比对 `build-copy/svg/` vs shipped core `svg/`：8/8 MATCH**（逐页哈希见 `freeze-baseline-core.log`）；工具复核 shipped core SVG 运行前后未变。
- **补充（edition-internal 自洽基线，非标准口径）**：`freeze.py baseline --build <edition> --core-svg <edition>/svg --out scratch/freeze-ed`：rc=0，`8/8 SVGs byte-identical`；直接 SHA 比对亦 8/8 MATCH。
- `freeze.py diff --core-svg core-ru/svg --edition-svg ru-es/svg`：removed total 848 / distinct 484；CJK：edition 每页仅 U+3000（新增 CJK 字符共 8 个，全部为 U+3000）；**西里尔删除恰为 15 项**：`Билибин、Билибина、Зимняя、Иван、Ивана、Иллюстрация、Морозко、год、достояние、иллюстрация、к、можно、ноябрю、общественное、сказка`（各 ×1，全部 P8）= Q46 `можно` ×1（已知合法）+ 14 个 Morozko 图注词（图按设计跳过）；unexplained 0。text.md CJK 0。

## 5. keycheck 150/150（`keycheck-150.json` + `keycheck-mechanical.json`）

- 机械比对：text.md Answers 1–150 逐题解析（无缺号）vs P8 extract 键：**149/150**，唯一差异 Q150（text.md 为 `(Pregunta abierta, texto modelo abajo)`，印刷键为 `✓`，开放写作，属设计）；P8 extract vs core `ru-p8.json`：差异恰 [137–140]。
- 逐题手核：text.md 838 行全文通读 + 8 页渲染逐页目视；每题题干对正文/表/图表逐项核实；**150/150 PASS，0 失败**。
- 重点项：Q20 `желании`（D6，`о своём ___` 前置格，中性 -ие → -и；题干与注释未变）；Q25 选项 `День студента`（D2，键 b 不变，全称仍存于 P2 正文 + Q11 题干）；Q73 `заказов`（直接对正文句「сделали больше 14,4 миллиона заказов」核实）；Q137–140 西语译键（与 core 中文键差异属设计）；Q150 范文实测 97 词（brief 80–100）。
- 表内题：Q54（Крылья—Оренбург 2:0）、Q59（Спартак胜 Акрон 2:1）已对 P4 渲染表逐行核实（与 proof1 一致，P4 SVG 0 变化）。

## 6. boxtitle 逐个实测（PIL 真墨迹，不只 advance）+ spill sweep

- 全版 32 框标题墨迹右缘 vs 框右缘/页右缘（1862）：全部为正余量；全版最紧 P6 `ЗА И ПРОТИВ　PROS Y CONTRAS` **+8.6px**；次紧 P3 `Nota — экранизация adaptación al cine` +26.3px、P7 `ОШИБКИ　CLÍNICA DE ERRORES` +27.4px；P1 最紧为 `В ЭТОМ НОМЕРЕ　SUMARIO` +65.1px（与 proof1 一致）。
- 全部奶油框末行降部真墨迹：除 O3（+0.0）外，余量 ≥ +6.9px（P7 词框 `распродажа = gran venta.`）。
- spill sweep（修正版：仅基线在盒内的行计入归属）：**0 溢出**。首版 naive 扫查（基线窗 +45px）的 69 项均为 BELOW-WINDOW 下一行误报；其中唯一 RIGHT 项 `снег` +8.6px 经核为盒下 32px 的下一行（y=1800，盒底 1768），非盒内溢出。

## 7. 印/网文字层比对（#1 D1 回归）

- PyMuPDF 非空白字符多重集：整体一致且逐页一致，30,838 字符；总字符（含空白）印/网均为 37,321。
- **#1 D1 已修复**：印版 P1 恰 3 个斜体 span；**网版斜体 span 亦为 3 个**（`LucernaNotoSerif-Italic` `чёрная пятница` bbox `(1088.0, 1266.8, 1222.8, 1288.7)` 与印版逐值一致 + `LucernaNewsreader-Italic` `«` / `»` 各 1）；span 文本 `чёрная пятница`（无丢空格）；`«чёрная пятница»` 印版 8 次 / 网版 8 次；目视对照 `p1-wowword.png` vs `p1-wowword-web.png` 像素相同（md5 `893da63dd70a85b47711cfceb770c727`）。
- P8 最小字号实测（PyMuPDF，印 PDF）：**9.75pt**（SOP §1.1 下限，符合）；全书最小字号亦为 9.75pt（P8）。

## 8. D1 / D2 / D6 / kicker（`d1d2d6.py`，Python 解析 `<text>` 元素）

- D1：text.md L459 `УЧЕБНЫЕ ДАННЫЕ`、L504 `Три уровня, три темы`、L596 `Большой тест недели + все ответы`；免责声明（`Это учебный опрос редакции для упражнений — не настоящая статистика.`）**不在** text.md；4 串全部在 SVG（P6 s1+s2、P7 s3、P8 s4）；免责声明未出现在其他页。
- D2：全称 `Международный день студента` text.md ×2 = core ×2；Q25 选项为 `День студента`（P2 SVG 短式 ×4、全称 ×2，分别为正文/题干）。
- D6：`желании` text.md ×2；P2 SVG ×0（仅键）；P8 extract key 20 = `желании` = core `ru-p8.json:177`。
- Kicker：P1 y=372 串含 9 处双空格；PIL 真墨间隙 `[7.2, 5.9, 6.8, 6.3, 7.1, 7.4, 7.4, 6.8, 7.6]`，最小 5.9px ≥ 4（与 INVEST-NOTE 表 1 逐值一致）；行居中 975.0。#1 O1 两处 0–1px 词距已消除（`p1-kicker.png` 目视确认）。
- `___` 字面：text.md 恰 87 处（模板缺口，已裁定，不作缺陷）。

## 9. §1.1 与读者面扫查（`s11_check.py` + 自跑）

- `s11_check.py <edition>`：**FAILURES: none**。8 SVG；纸色 `#fbfaf6`；禁用色 `#f7f1e2` / `#c9a227` / `#8b4513` / `#000000` 均为 0；徽章 A2 `#5c6e30` / B1 `#46581f` / B2 `#37402f` 俱在；页脚 `VOL.4` + 全角空格；VOL.3 仅 P4 更正句 1 次；P1/P8 带无 VOL.5；刊头 196px、带标题 46px；左缘 ≥87（实测 88.0）；可见 SVG CJK 0；印/网各 8 页；网 <7MB（3,387,465 B）；P8 最小字号 9.75pt。
- `check_core.py`（版内验证器，rc=0）：`GOLDEN: 8 / golden BAD: 0 / gloss fails: 0`；P8 svg 文本字符 11,108；孤儿行首 1（P7 y553 `”».`，已知 benign）；同基线碰撞 1（P1 y1712 `чёрная`，与 core 同类）。
- 弯引号 U+201C/U+201D/U+2019 全版扫描（SVG 可见文本 + text.md）：text.md 各 1/1/0、SVG 仅 P7 一对（故意保留）；其余引号均为 « »（U+00AB/U+00BB）。
- D5 字体（只记录不判定，见 `d1d2d6.log`）：Newsreader 13–53pt、Noto Sans / Noto Sans CJK SC 13.3–46pt、Noto Serif / Noto Serif CJK SC 13–53pt、UnifrakturMaguntia 196pt（刊头 1 处）。

## 10. 回归对照（#1 备份 `backup-old/2026-w47-ru-es/`）

- text.md diff：恰为 6 行对（12 行 diff），即 L173 D6 键、L187 D2 选项、L459/L504/L596 D1、L694 D6 键表；别无其他。
- content*.py：content12.py（kicker :18、D6 :257、D2 :276）、content56.py（D1 s1+s2）、content7.py（D1 s3）、content8.py（D1 s4）有差异，逐行均为已记录的修复；content34.py、run.py、render.py、ru_textmd.py、svglib.py、bslib4.py、check_core.py 完全相同。ABSTRACT.txt 相同。
- SVG `<text>` 多重集差分：P1 仅 kicker 双空格（`  ` ×7、`—  `、`，  `），P2 仅 D2，P6 仅 D1，P7 仅 D1，P8 仅 D1+D6；P3/P4/P5 为 0。
- **KEEP/REVERT 盘点：无 hand patch 丢失。** #1 无内容手补（仅网 PDF 机制缺陷 D1，已由重建修复）；es 旧 map 无独占手 fix（重建报告：surgical map 与再生 map 逐字节一致）。
- creambox 扫描新旧逐行相同（0 diff 行）；occlusion 旗标集仅差 1 项 run 标签（见 §1）。

## 11. 工具出入说明

- 任务所列「`verify_ed.py` es」不存在：全树检索，`verify_ed.py` 仅见于 en 系（`2026-w47-en-<lang>` 专用）；ru 系无此脚本。本次以版内 `check_core.py`（§9，rc=0）+ `p8.py` + 150 键手核覆盖其职能。
- `check_s11.py` 一项对应正典 `scratch-fanout-ru/s11_check.py`，对本版实跑通过（§9）。

## 外部事实来源

- 沿用 proof1 已核来源（本版未改核心事实；P3/P4/P5 SVG 0 变化）：俄超 14 轮 Forbes / Спорт-Экспресс / Sports.ru / Sportradar；第 15 轮赛程 Спорт-Экспресс；星期/日期 `date -d`（Europe/Moscow）。其余事实以 core-ru KIT §3 的已核查来源为准。
- 本次新增实测不依赖外部事实：全部数字均为本轮磁盘实测。

## 判为非缺陷的项（证据在上）

- 42 TEXTX 全部为测量伪报（像素裁定）；creambox 下标题假阳性 95 行；P2 末行降部 0px 贴边（O3）；P1 标语窄词距已消除（O1）；`— СТРАНИЦА ? —`（O2，导出器共有格式）；Q140 译法（O4）；Q150 印刷键 `✓`（设计）；Q137 em-dash 截断（解析器行为，SVG 原行完整）；check_core 孤儿行首/同基线碰撞（与 core 同类）；Nota 词头/释义窄空格为缩图错觉（PIL 真墨 5.1–9.3px，O6）；byline `редакции | Lucerna` 3.9px（与 core 逐值相同，O6）；`___` ×87（模板缺口，O7）；P7 弯引号一对（O8）；P8 最小字号 9.75pt（SOP 下限内）；P8 «Морозко» 图跳过（设计）；D5 字体只记录。
- **KIT 记录核对**：occlusion 42 TEXTX、p8 CLEAN/keydiff [137–140]、freeze 8/8、P8 9.75pt、非空白字符 30,838、kicker 间隙、95 BELOW-WINDOW 分布——本次独立实测全部复现；KIT §5 字节数/SHA 与磁盘一致。
