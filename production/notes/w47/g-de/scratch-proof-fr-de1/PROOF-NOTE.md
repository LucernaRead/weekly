# PROOF-NOTE — W47 fr-de (法语核心 × 读者德语) 独立复校 proof1

- 复校员：独立复校（与构建者不同人），2026-11-11 12:32–13:00 EST
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-fr-de1/`
- 结论：**(b) 有缺陷，不定稿** — 1 项 de 版缺陷（P7 盒底溢出），见下。另 2 项记录（不计入本版缺陷）：1 项核心继承缺陷（Q148，需 core 轨道修）、1 项全周级已知待定项（D5 字体）。
- 生产文件只读：复校期间未改任何生产文件，未 commit、未 push。确定性重建在沙盒副本中进行（副本已删，哈希记录在 GATE-LOG）。`git status` 上该版目录为未提交新目录（builder 工作状态，复校未动）。

## 身份核对（开工前实测，与任务书一致）

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `La-Lucerna-VOL4-fr-de.pdf`（印刷） | 17,424,274 | `6fff7a4f688fbc4724e0b307d1db71716244a871f2a0dcb4be3d59098fd8864f` |
| `La-Lucerna-VOL4-fr-de-web.pdf`（网页） | 1,704,484 | `751125ef971d6aa2d08219a884ba4bcd5e8eb4dc684f33218ecf9fb5ddf7cbde` |
| `2026-w47-fr-de.text.md` | 46,694 | `f1c60667110623744690217646de50240c7a74170dea3b9050dad926adff88f3` |

核心 core-fr 已定稿（fix3 build，proof4 (a)）。Builder 本版 run4，门禁 15/15。

## 缺陷清单（1 项，de 版引入）

### D1 — P7 LESERBRIEFE 奶油盒底部溢出（须修后重校）

- 位置：P7 右下 `LE COURRIER DES LECTEURS　LESERBRIEFE` 奶油盒（`p7-langue.svg`：`x=989.0 y=1878 w=873.0 h=380`，盒底 `y=2258.0`）。
- 内容：`courrier_disclosure`（`expl.py:182`）德文段 "Anmerkung der Redaktion: Bis Redaktionsschluss war kein VOL.4-Text eingegangen; diese Ausgabe druckt ein gekennzeichnetes Redaktionsbeispiel. VOL.5 löst das Versprechen ein, echte Einsendungen zu kommentieren."（199 字符）在 849px 宽、19.5pt 下排成 **3 行**（基线 2206.0 / 2233.3 / 2260.6），核心中文版仅 2 行（末基线 2233.3）。
- 实测（PIL 真墨测量，印刷 PDF 300 dpi 渲染）：
  - 第 3 行基线 2260.6，盒底 2258.0，基线溢出 **+2.6px**；creambox 规范扫描记为 `clearance -2.6`。
  - 奶油底边实测 svg y≈2257.5；该行真墨最末行 svg y≈2265（字色 `#6f675d`），即 **约 7.5px 真墨落在奶油盒之外**（白纸上），含 "Einsendungen" 中 `g` 的下行部 + 主字形底部约 3px；其下约 4px 白纸，再接 `LA SEMAINE PROCHAINE` 深绿带（起于 svg y≈2270）。
  - 目视：300 dpi 裁切（`png/p7-box-crop.png`）可见末行字形被奶油边切过；150 dpi 全页亦可辨。
- 定性：同流续行溢出（非 +24/+37 下一标题误报，见 GATE-LOG creambox 判定）。核心与 en/ja/ko/zh-tw 均为 2 行（末基线 2233.3，清除 +24.7）；同类溢出亦见于 es/it/pt/nl/ru（同盒同为 -2.6），属本轮 fan-out 共性缺陷类，但本报告只判定 de 版，兄弟版由其复校员各自判定、修复建议同式。
- 修复方向（供 builder，不由复校改）：缩短 `courrier_disclosure` 至 2 行（如删 "diese Ausgabe druckt ein gekennzeichnetes Redaktionsbeispiel." 或等效缩写，目标末基线 ≤2233.3、清除 ≥+24）；仅改该键值，P7 哈希变，其余页不变；修后重跑 gates 全套 + 本复校重验 P7。

## 记录项（不计入本版 (b) 判定）

### R1 — Q148 错法语（核心继承，10 版共有，需 core 轨道修）

- 印法：P8 对话 "— On se retrouve (148)___ du cinéma ? — Oui, à 19 h 30."，答案键 `devant`（`p8-proof1.json` / 核心 `final-fr-p8.json` 均为 `devant`）。
- 问题：填入后成 "On se retrouve **devant du cinéma** ?"——介词 `devant` 后不接 `du`，正确应为 "devant **le** cinéma"。
- 定性：核心冻结源 `core-fr/content8.py:176` 与 de 版 `content8.py:176` 字节相同，核心键亦为 `devant`；属核心原文缺陷，非 de fan-out 引入，fan-out 按 freeze 规则不得擅自偏离核心。故不计入 de 版缺陷，报请转 core 轨道修复（修核心后 10 版同受影响，须重验）。

### R2 — D5 字体（全周级已知待定项，如实记录，不判 (b)、不擅自修）

- 实测：8 页 SVG 字体普查——`Newsreader` 946 段、`Noto Sans CJK SC` 696 段、`Noto Serif CJK SC` 74 段（全为结构分隔符 U+3000，不可见）、`DejaVu Sans` 4 段（P7 ✗ 标记，合理）、`UnifrakturMaguntia` 1 段（刊头黑体）。
- 其中 770 段 CJK 字体中 **423 段为纯拉丁文**（无 CJK 字符、含德文词），即德语讲解层落在 Noto Sans CJK SC——与任务书所述 fr 家庭 D5 问题一致（核心对照：776 段 CJK 字体中纯拉丁 100 段）。按任务书指示：仅记录，待用户定夺 scope。

## 其余手验（150 题逐题核对，无问题）

- `.text.md` 全文 1,089 行通读：150 题题干/选项/答案/注记逐题核对题干事实与文章内容，德语注记逐条核对语法与译义。结论：除 R1 外，150 键全部正确（Q64 "Lukas Dhont" 拼写已在 P5 目视核对无误；run4 修复的 `Dont`→`Dhont` 已落实）。
- 抽查示例：Q26 注记 "Vrai (Frühverkauf seit 1951)" 与 P3 ZOOM "Erstverkauf 1951" 同事实、不同 E 键（与 pt/nl/ru 同处理，非缺陷）；Q53 "plus vite" 为比较级语法练习答案；Q113 "propose"（主语 Le cinéma 单数）、Q114 "aimé"（avoir 无配合）注记正确；Q135–139 德→法翻译答案与注记正确；Q148 除外。
- 细项（非缺陷，仅备查）："DATES À RETENIR" 注记 "Miabend" 为 Mittwochabend 的紧缩写法，可读；P3 头 "BEAUJOLAIS　BEAUJOLAIS-QUIZ" 宽度门已过；P1 "sam. 21　Turin : demies　SERD" 中 SERD 为欧洲减废周（源文件即如此）。
- 8 页逐页目视（印刷 PDF 150 dpi；另抽查网页 PDF P1/P7）：除 D1 外零问题——P1 band_r1（"ALCARAZ SIEGT　SENAT STIMMT MI." 起 1337.5，法文标题止 1236.9，净空 100.6）无重叠；各页无溢出、无遮挡、无截断；Hiroshige 图注完整；P8 42 题答案流完整。
- 徽章 134（10/12/18/15/14/15/12/38），与 builder 一致；P8 最小字号 11.625pt；U+2019=0、U+00B7=0；印/网文字层逐字节一致（104,794 B）；卷号 VOL.4 各处一致。

## 参考

- 构建报告：`hidden_files/w47/scratch-fanout-fr/FANOUT-REPORT-fr.md`（de 版 run4）
- 门禁明细：同目录 `GATE-LOG.md`、`gates-proof1.json`
- 证据图：同目录 `png/`（p1–p8 印刷版、`p7-box-crop.png` 3× 盒底裁切、`web-p1.png`、`web-p7.png`）
