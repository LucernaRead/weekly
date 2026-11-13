# PROOF-NOTE — 2026-W47 es-de 独立复校（重建版，proof2）

复校员：独立复校员（与 es-de builder / es 核心 builder / 首轮复校员不同人）
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-de2/`
日期：2026-11-11（13:00 UTC 前后）
对象：`production/2026-w47/2026-w47-es-de/`（西语核心 × 德语读者版，es 全族重建版，未 commit 未 push）
方法：全部项目从头独立重跑、重测、重验；**不采信首轮任何结论**。只读生产文件，未改任何生产文件，未 commit，未 push。
唯一一次对生产文件的写操作：门禁重渲染（`render.py`）改写了网 PDF（见 O2），已用备份原样恢复并 SHA 复核。

## 结论：(a) 零缺陷

缺陷清单：**无**。观察项 O1–O4（见下），均不计缺陷。

## 0. 身份核对（自算 SHA-256，与任务书逐字一致；复核前后各测一次）

| 产物 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| 印 PDF `La-Lucerna-VOL4-es-de.pdf` | 3,503,120 | `65ebf6b7df8b07013d809427259a8b3504ac33e318bb9e0b61f72d7c9498fbca` | ✓ 始末一致 |
| 网 PDF `La-Lucerna-VOL4-es-de-web.pdf` | 889,914 | `2e39306ddd4424e8309aed9efe9e580920c75a826e5821c5e67f401f91c7ec9b` | ✓ 恢复后复核一致 |
| text.md `2026-w47-es-de.text.md` | 45,311 | `81ff06563dd9332ab6af2b4d826f2dda6d7157d82983df01e484fa462c310a67` | ✓ 1,802 行，始末一致 |
| core-es 印 PDF | 17,212,955 | `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5` | ✓ 复核前后未变 |
| core-es 网 PDF | 1,410,471 | `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235` | ✓ 复核前后未变 |
| core-es text.md | — | `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb` | ✓ 复核前后未变 |

SVG 8 枚：重渲染前后逐枚 SHA 一致（8/8 SAME，`svg-sha256-final.txt`）。
WEEKLY-KIT.md 第 109 行登记的 SHA/字节/行数与上表逐字一致。
说明：本目录下另有 08:31–08:37 的旧版 proof2 残留文件（针对重建前旧版，已过期），已原样移入 `stale-0831-pre-rebuild/`，本次未采用。

## 1. 必查项：首轮漏检的 2 处盒题溢出（重建修复）——逐处独立实测，均已归零

| # | 盒题（重建后 gloss） | 位置 | 实测（boxtitle 真墨，PIL 4x） | 旧值 | 结论 |
|---|---|---|---|---|---|
| A | `EL PLAN DE LA SEMANA　Der Plan` | P5 盒 x=538..961 y=200，标题基线 y=237.0，fs=23 | 标题宽 381.1px，右缘 937.6，**clear +23.4px** | −21.4px | ✓ 归零 |
| B | `ERRORES TÍPICOS　Fehler` | P7 盒 x=1440..1862 y=441，标题基线 y=483.4，fs=23 | 标题宽 298.5px，右缘 1760.0，**clear +102.0px** | −30.8px | ✓ 归零 |

boxtitle 全版：0 处 OVERFLOW；全部 25 个盒题 clearance 均为正，最小 +20.9px（P2 HINWEIS 行）。
渲染目视亦核实：P5「Der Plan」标题居盒内留白充足；P7「Fehler」标题留白大。

## 2. P8-keys 与运行门

- `run.py` 重跑（keycheck 内联）：TOTAL 150；A2 50 / B1 72 / B2 28；分版 P1 10 / P2 18 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 38；题型与 KIT 一致；**FLOW OVERFLOW 0 次，HEAD TOO WIDE 0 次**（bslib4 的 `!! FLOW OVERFLOW` / `!! HEAD TOO WIDE` 行在输出中出现 0 次）。
- P8-keys 终 y=**2506**（底 2560，余 54px），0 OVERFLOW。
- P8 最小有效字号 10.125pt（≥9.75pt 下限），低于下限 0 处；P8 共 376 个 Tm 条目。
- p8 extract 150/150；p8 compare **CLEAN**，missing=[]，extra=0，keydiff=**[137, 138]**（已裁决：E 组中文句答案键译成德语，137 `Montag ist der Internationale Flamencotag.` / 138 `Am Samstag sehen wir das Derby von Sevilla.`，与核心中文键逐项核对，译法正确；不得据此判 (b)）。
- keycheck（REG vs P8 提取键）：149/150 精确一致，唯一差异为 Q150 预期项（开放写作题，提取器渲染为 `✓`），与工具设计一致。
- P8 答案区逐行检查（`check_p8keys.py`）：142 行，134 个答案起首；多行答案 6 条（#1、#36、#44、#84、#139、#141），均为正常折行，目视无碰撞；#139（C2 新措辞）3 行，整体仍收于 y=2506。

## 3. freeze 首检 8/8 与 CJK 逐个分类

- freeze baseline：**8/8 SVGs byte-identical**（rc=0）；shipped SVG 跑后未变。
- freeze diff（core-es vs es-de）：P1 +27/−38、P2 +50/−51、P3 +33/−30、P4 +34/−27、P5 +44/−47、P6 +19/−17、P7 +46/−46、P8 +162/−626。
- 新增 CJK **合计 1 个 = U+3000 全角空格**，在 P1，其余 7 页 0 个。分类：P1 刊头行 `CADA SEMANA EN ESPAÑOL　JEDE WOCHE　SPANISCH, WIE SPANIEN ES LIEST` 含 2 个 U+3000 分隔符（核心对应行 `CADA SEMANA EN ESPAÑOL　每周一期…` 含 1 个），净增 1 个结构空格——只允许的 U+3000 结构空格，无表意字、无全角标点。
- 全量扫描：`.py` 源码 CJK 表意字 0（U+3000 共 106 个：content12 33 / content34 24 / content56 25 / content7 10 / content8 12 / bslib4 2）；8 页 SVG `<text>` CJK 表意字 0（U+3000：P1 21 / P2 16 / P3 13 / P4 15 / P5 14 / P6 14 / P7 12 / P8 14）；text.md CJK 表意字 0（U+3000 共 99 个）。
- 新增字符串含真 CJK 表意字：8 页均为 0。
- 被删拉丁片段核查（词级）：P1–P7 被删无 CJK 字符串全部以子串存在于当页（缺失 0 项）；P7 唯一缺失片段为 `mejor。`（中文句号 。的附着，词本身以西式句号存在）；P8 被删 18 个非子串片段全为答案注德文改写（键经 p8 compare + keycheck 核实一致，无一失词）。西语正文无丢失。

## 4. 150 题逐题手验（三源交叉）

三源：版 P8 keys（`de-p8-extract.json`）/ text.md 答案区（RESPUESTAS，1,802 行全文通读）/ 核心 P8 keys（`core-p8-extract.json`）。
逐题核对题干—键—正文/图表一致性（`de-150-compare.txt` 全表 + `keycheck-150.json`）：

- REG 键 == P8 提取键：149/150（仅 Q150 预期 `✓`）。
- REG 键 == 核心键：147/150（仅 137、138 已裁决德译 + Q150 提取器 `✓`）。
- 内容验算全部通过，抽样要点：配对 25–28（debate=c / mitin=b / cartel=d / escaño=a）、52–55（jornada=c / derbi=b / liderato=a / fase liga=d）、141–144（sondeo=c / muestra=d / margen de error=b / junta electoral=a）；P3 词框 5 词（cante·baile·guitarra·palmas·compás）各用一次；RTVE 合计 45+45+30+30+15+10+10+10=195；45−30=15；禁发民调 24–28 为 5 天；135 题：`La campaña dura quince días.`；Q35 `baile` / Q36 `guitarra` / Q37 `palmas` 均与正文一致。
- 金句 8 条：每条在 8 页 SVG 合并文本中恰好出现 2 次（原文 + P7 引用）；德文译注与页码注（Página 1/2/3/4/5/6）均准确。
- 徽章逐页计数（精确匹配 run）：P1 16（10 练习徽章 + 6 个 EN ESTA EDICIÓN 级别标）/ P2 15（25–28 共用 1 个区间徽章）/ P3 18 / P4 15（52–55 共用 1 个）/ P5 18 / P6 18 / P7 12 / P8 35（141–144 共用 1 个）；与 REG 题数之差恰为 3 个区间徽章组。
- VOL：SVG 中 VOL.4 9 处、VOL.5 3 处（下期预告正当引用）、VOL.3 0 处。
- 禁词：`12 de noviembre` / Ucrania / Rusia / guerra / Trump / Putin / OTAN / Israel / Gaza / Palestina 各 0 次（text.md 与 SVG 双查）。
- §8.1 讲解词计数与 KIT 逐项一致：P1 reflexión 2；P2 mitin/cartel/escaño 各 2；P3 cante 5 / toque 6 / baile 9 / compás 4 / duende 6；P4 parón 2 / liderato 3；P5 papeleta 2 / censo 3 / plazo 3。
- MODELO（Q150 范文）：手工逐词计数 97 词，与 KIT 及正文标注一致；`✓ = Schreibaufgabe` 注明。
- ABSTRACT.txt：德文一行、无 ASCII 双引号；所列事实（laSexta 辩论 13 日、大选 29 日、邮寄投票截止 19 日、弗拉门戈日 16 日、Cecilia 22 日、Liga 第 13 轮、欧冠、A2–B2、150 题）均与本期一致。
- 练习小节头一律冻结为西语：P8 `A　COMPLETA LA CRÓNICA / B　PREGUNTAS GENERALES / C　LEE Y RESPONDE / D　CONSTRUYE FRASES / E　TRADUCE / F　LAS PALABRAS DEL 29N / G　DIÁLOGO EN EL COLEGIO / H　ESCRIBE TÚ`；P2–P6 各节头（`A　LAS FECHAS / B　EL PRESENTE / C　COMPRENSIÓN / D　LAS PALABRAS` 等）亦为西语，德文仅为副说明。
- 核心冻结英文 `next Sunday`：在 core-es 与 es-de 的 .py、SVG、text.md 中出现 **0 次**（任务书所引 core content12.py:37/:113、content34.py:127 在现盘 core-es 中并非该句；该句实际只存在于 core-zh-tw 的同名文件——指针过期，与本版无关）。本版无任何英文 gloss 残留，无缺陷可判。
- text.md 核查：`hasta el jueves` ×7、`antes del jueves` ×0、`sábado veo el derbi` ×1；P7 金句德译、P8 答案区与版面逐项一致。

## 5. 几何门（全部自跑，tools/venv 解释器 Pillow 13.0.0 / FreeType 2.14.3）

- 遮挡审计：自检六类全触发（selftest PASS）；本版 **0 flags**。
- creambox（canonical `hidden_files/w47/tools/creambox.py` 全版扫描）：全部奶油盒末行基线均在盒内；below-window 行均为下一节标题/说明（+24..+44px，预期假阳性），无整行漫出。
- creambox 真墨复测（`creambox_diag.py` + 全行复核 `ink_all_runs.py`）：全部盒末行真墨 clearance 为正；最紧 2 处见 O1。P7-TOOLBOX 3 盒：min inside clearance +5.7，min desc-clear −0.0（见 O1）。
- sweep：box-vs-hline 0 旗；bridge 20 条，orphans 0，widows 0。
- 文字层：pdftotext 印 == 网，逐字节一致，111,448 字节；网 PDF 889,914 B（< 7 MB）。

## 6. 8 页逐页渲染目视（印版 P1–P8 + 网版 P1/P8，120 dpi）

- P1：刊头、头条、五要点盒、数字盒、目录、AHORA TÚ（与题 1 紧贴，无孤悬）、BREVES、闪电问答 7–10 题齐全，无重叠。
- P2：日历盒、HINWEIS、¿SABÍAS QUE…?（末行 `ley.` 在盒内）、¿Y TÚ?、DECIR LA HORA、日期表、练习 A–D（11–28）齐全。
- P3：Sargent 油画 + 署名/PD 出处、HINWEIS、LO QUE QUEDA、EL FLAMENCO EN TRES DATOS（末行 `música.` 在盒内）、¿Y TÚ?、练习 29–46 齐全；中栏下半留白与核心版式一致。
- P4：六场表、LA CHAMPIONS VUELVE、HINWEIS、¿Y TÚ?、练习 47–64 齐全。
- P5：投票箱照片 + CC0 出处、EL PLAN DE LA SEMANA（见 §1）、HINWEIS、VOTAR POR PRIMERA VEZ、¿Y TÚ?、练习 65–82 齐全。
- P6：EL CAMINO AL 29N 时间轴、LEER UN DEBATE、RTVE 条形图（45/45/30/30/15 + 195 总数注）、民调禁令图（5/15/1）、练习 83–100 齐全。
- P7：三级语法栏（LA HORA / COMPARATIVOS / EL SUBJUNTIVO）、ERRORES TÍPICOS（见 §1）、LA PALABRA、读者来信（末行 `Versprechen gilt für VOL.5.` 在盒内）、8 金句 + 德译 + 页码、VOL.5 横幅位于页脚线上方（未越线）、中世纪祈祷书图 + PD 出处、练习 101–112 齐全。
- P8：练习 113–150、RESPUESTAS 1–150 收尾距页脚留白充足、范文 97 词、天鹅羽毛笔图 + PD 出处。网版 P1/P8 与印版视觉一致。

## 7. 观察项（不计缺陷）

- **O1 — 两处奶油盒末行真墨余量仅 +0.1px**：P2 ¿SABÍAS QUE…? 盒（底 543.5，末行 `ley.` 墨底 543.4）与 P5 VOTAR POR PRIMERA VEZ 盒（底 1251.5，末行 `compara precios antes de pagar.` 墨底 1251.4）。真墨实测在盒内，3 倍放大裁图（`zoom-p2-sabias.png` / `zoom-p5-votar.png`）目视墨未出白区；0.1px ≈ 0.007mm，低于任何印刷/光栅阈值。另 P7 读者来信盒末行真墨余量 +0.9px、P3/P5 ¿Y TÚ? 盒 +1.7px、P1 目录盒 +4.2px，均在盒内。按「墨在盒内即过」计为通过，记为观察（不改版；若协调员要求加高盒体亦可，但非必需）。
- **O2 — 网 PDF 字节不可重现（工具链属性，非本版缺陷）**：`render.py` 重渲染印 PDF 字节一致（SHA `65ebf6b7…` 复现），但网 PDF 变为 889,905 B / SHA `774b5a3e…`；另两次隔离 `webpdf.py` 运行互不相同（889,909 B / `5813af06…` 与 889,908 B / `91c37492…`，间隔 3 秒），证实 `webpdf.py` 每次输出均不同（内嵌时间戳/ID 所致，压缩流逐字节皆变）。已交付的网 PDF 已用备份原样恢复，SHA 复核与任务书一致。结论：网 PDF 的 SHA 只能核对交付件本身，不可用重渲染复现；文字层印==网（111,448 字节）是有效核对。建议协调员勿将「网 PDF 重渲染 SHA 一致」列为门禁。
- **O3 — D5 字体（全周级已知待定项，只记录）**：`Noto Sans CJK SC` 文本 run 共 636 个，其中纯拉丁 run 537 个（拉丁讲解层落在该字体，含德文译注、双语标题、西语 HINWEIS 等）。只记录实测段数，不以此判 (b)。
- **O4 — 「next Sunday」冻结指针过期（记录）**：见 §4 末。该句在 core-es 与 es-de 中均为 0 次，任务书行号对应的是 core-zh-tw 的文件；本版无相关内容，无缺陷可判。建议协调员更新该条指针。

## 8. 交付文件（本目录）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`（门禁表）
- 门禁产物：`de-gates.json`（已修正为恢复后交付件值 + 重渲染注记）、`de-render.log`、`de-occlusion.json/.log`、`de-p8-extract.json/.log`、`de-p8-compare.json/.log`、`de-freeze.log`、`de-freeze-diff.json/.log`、`de-creambox.log`（canonical）、`de-creambox-diag.log`、`de-ink-all-runs.log`、`de-boxtitle.log`、`de-keycheck.log`、`keycheck-150.json`、`de-sweep.log`、`de-minfont.log`、`de-print.txt`、`de-web.txt`、`de-p8keys-check.log`、`de-150-compare.txt`、`de-content-checks.log`、`de-frag-check.log`、`de-frag2.log`、`core-p8-extract.json`
- 渲染与放大：`render/print-1..8.png`、`render/web-1.png`、`render/web8-8.png`、`zoom-p2-sabias.png`、`zoom-p5-votar.png`、`web-rerun1/2.pdf`（网 PDF 非重现性证据）
- 备份：`backup-shipped/`（已交付 SVG/PDF 原样备份 + `svg-sha256-before.txt`）
- 工具副本：`gates/gates.py`、`boxtitle_core.py`、`creambox_diag.py`、`check_p8keys.py`、`keycheck_core.py`、`minfont.py`、`sweep_de.py`、`ink_all_runs.py`
- 旧版残留：`stale-0831-pre-rebuild/`（08:31–08:37 旧版 proof2 文件，未采用）
