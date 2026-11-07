# W45 RU×EN 独立校对报告（proofread, not builder）

- 待校版：`files/weekly-report-w45-ru-en/`（8 SVG + 8 PNG + print/web PDF + WEEKLY-KIT.md + ABSTRACT.txt）
- 核心对照：`files/weekly-report-w45-ru-core/svg/`（W45 俄语核心，zh-cn 版）
- 本报告目录：`hidden_files/w45/ru-en-proof/`（本文件 + 全部审计日志/脚本/裁图）
- 纪律：只读校对。未发 Discord、未往主聊天发卡片/PDF、未建 cron、未碰 weekly-git；核心构建目录与核心已发 SVG 全程未改动（校对前后核心哈希见 `core-hashes-after-baseline.txt` / `core-hashes-final.txt`，8/8 一致）。

## 结论先行

**除待裁定项（P7 读者园地盒底线，见 §9）外：ZERO PROBLEMS。** 构建者自述的每一项可验证主张均经独立重跑/重算证实；另发现两处“自述措辞需修正但不影响通过”的记录（见 §10），均不是版面缺陷。

**待裁定项 §9 不单独判不通过**（按任务书）：P7 盒底线擦碰确为核心原样几何、本版零位移、文字全程可读、审计 0 flags；是否采纳 lh+20 修复由协调员裁定（参照 es-en/es-de P6 擦碰先例的处理方式：冻结核心几何 + 文字可读 + 审计 0 flags）。

## 1. 基线 freeze（§2）

- 构建者自述基线哈希 8/8：p1 `8bfcb7e289dc383e`、p2 `5b35f1d7c000759f`、p3 `8be9ba7f8d32ad9b`、p4 `9d699050f467482a`、p5 `f49d0ed8b09b4ec7`、p6 `8559d61d890820e0`、p7 `961119d6a19e617b`、p8 `2738ae046bda8030`——与实测核心 SVG sha256 前 16 位逐一相符。
- 独立重跑 `tools/freeze.py baseline`：
  - 对**未改动的核心构建** `hidden_files/weekly-report-w45-ru-build/`：**8/8 byte-identical**（`freeze-core-baseline.log` / `.json`）。
  - 对当前（已改后）的 ru-en 构建目录重跑：0/8 vs 核心——这是必然结果（该目录已是英文改后源码），但其产物与**已发英文版 8/8 byte-identical**（`freeze-baseline.log`），即英文版可由构建目录确定性复现。
  - 构建者保留的基线产物 `tools/scratch/baseline-w45-ru-en/svg/` 哈希 = 核心哈希 8/8（`builder-preserved-baseline-hashes.txt`），与“改前基线 8/8”自述一致。
  - 校对前后核心 SVG 重哈希无变化。

## 2. freeze diff 与西里尔词元（§2）

- `tools/freeze.py diff`（`freeze-diff.log` / `.json`）：8 页 added CJK 均为 0，英文版 SVG 内 CJK 字符总数 0（独立正则复核 8 页均为 0）。
- 西里尔词元多重集（独立脚本 `cyr-diff.py` / `cyr-diff.json`）：
  - P2–P8 与核心**完全相等**：443 / 338 / 306 / 316 / 354 / 397 / 641，与自述一致。
  - P1 差异仅副标题行：only_core 10 个词元各 −1（ЕЖЕНЕДЕЛЬНАЯ、ДЛЯ、ИЗУЧАЮЩИХ、РУССКИЙ、ЯЗЫК、НАСТОЯЩАЯ、РОССИЯ、ГАЗЕТА、ПО、РУССКИ），only_ed 为空——即除 y=372 副标题被徽章替换外，俄语正文词元确无增删。注：ГАЗЕТА/ПО/РУССКИ 在 P1 别处仍有出现，故净差 −1，与构建者“2→1 / 3→2 / 2→1”分述一致。
  - 目录表 Стр. 8 行 `все` 标签：核心与本版一致保留（`Стр. 8 / Тест и все ответы / все`）。

## 3. 注册表与范文（§2 补充）

- 构建目录重跑 `run.py`（`rerun-build.log`，产物 `rerun-svg/`，8/8 等同已发版）自带注册表输出：**TOTAL 150；by level A2 51 / B1 75 / B2 24；by page 10/18/18/18/18/18/12/38；by type fill-in 54 / multiple choice 42 / matching 20 / sentence building 12 / transformation 4 / cloze 13 / translation 4 / writing 1**——与 KIT 一致。
- 页码范围独立复核（SVG 题号区间）：P1 1–10、P2 11–28、P3 29–46、P4 47–64、P5 65–82、P6 83–100、P7 101–112、P8 题干 113–150 + 全部 150 键。
- P8 §H 范文：核心与本版拼接文本逐字节相同；除 `Пример:` 标签外正文 **84 词**（split 计数），在 80–100 任务范围内。

## 4. P8 答案（§3）

- `tools/p8.py compare`（`p8-compare.log` / `.json`）：**CLEAN，150 noted = 150 noted，missing = []，extra = []，uncertain = []，keydiff = [83, 137, 138, 148]**，与自述一致。
- 独立 dash-parse（`dash-parse.py` / `.log`：取 p8.py lines 解析的印出段，按首个 ` — ` 切键，逐字节比对）：
  - **键差异仅 [137, 138]**（RU→EN 重瞄准，见 §5）。
  - **83 / 148 确为 p8.py 括号提取 artifact**：印出键两版相同（83. `B`、148. `A`）；p8.py 的 paren 分支把尾部括号注记内的 ` — ` 当成键分隔，导致其“key”串不同（83 核心 key 串含中文注记前半、148 同理）。其余全部键逐字节相同，差异均为 note-only。
- 137 / 138 按 W43 同配对 KIT §5 先 precedent 核对：137 英文键 `Wednesday, 4 November is a day off.`（note `Compare page 3`）、138 `A promo code is a discount code.`（note `Compare page 5`），俄语题干保留、指令为 `Translate into English`，属已备案的重瞄准。
- 139 / 140 反向键与核心**逐字节相同**（`В субботу «Краснодар» играет с ЦСКА.` / `Поздравляю с Днём народного единства!`），note 仅把“工具格”译为 `instrumental`。
- 150 为 `✓` 范文题，note-only（英文 `Model text in section H of this page (84 words)`）。
- P8 分隔符 8 页均为俄语 `— СТРАНИЦА N —`（1–8 全）。

## 5. Occlusion 与几何扫描（§4）

- `occlusion_audit.py --selftest`：OK（6 类 planted 全部触发，clean 对照静默）。
- 本版 8 页：**0 flags**；核心对照：**0 flags**；`--core` 对比：**NEW flags = 0**（`occlusion-ed/core/vs-core.log`）。
- 同基线 advance-width 外框扫描（自写 `advance-scan.py`，按 PIL getlength/getmetrics ÷ SCALE）：8 页同基线重叠 0、<5px 紧贴 0，核心与本版一致；P1 顶栏与徽章行无碰撞。
- P6 图表逐元素检查（`p6-check.py` / `.log`）：later-rect 覆盖正文墨迹 0 处；4 条 bar 标签与数值卡片上全部可见（34% / 28% / 22% / 16%，bar 宽 600/494/388/282 与 34/28/22/16 成比例）；图表注记双语一行，含 `Practice data` / “非真实统计”声明；目视裁图 `p6-chart-crop.png` 确认。
- P8 最大非页脚基线核心与本版同为 2532.59，页脚规则 2580 未越；构建重跑日志零 `FLOW OVERFLOW` / `HEAD TOO WIDE`（`rerun-build.log` 中该串出现 0 次）。

## 6. Gloss、图片、金句（§4）

- Gloss 按 `·` 本身拆分（源码 `gloss()` 串独立计数）：**9 次调用共 26 项**，逐 call 与核心相等（content12: 3/3/3；content34: 3/3/3；content56: 3/2/3）。渲染后 gloss 前缀均为 `Note — `（P2–P6 有载页实测）。
- 图片：P1 / P4 / P5 各 1 张，`<image>` 元素字符串核心与本版**逐字节相同**（其余 5 页均无内嵌图）；元素相同即载荷相同。
- P7 金句 8 句：裸句（无引号）在全刊拼接文本中核心与本版均为**各恰 2 次**（正文 1 次 + P7 `ФРАЗЫ НЕДЕЛИ` 引文 1 次）；俄语原文逐字节相同，仅英译为新；页签保留俄语 `Страница N`。

## 7. 家具三方实测（§5，徽章为重点）

| 版本 | P1 徽章/副标题 y=372 | 字体/颜色 | 实测 advance 跨度（x=975 居中） |
|---|---|---|---|
| W45 ru-en（本版） | `TEXT IN RUSSIAN · EXPLANATIONS IN ENGLISH — THE EDITION FOR ENGLISH-SPEAKING READERS` | 20pt 粗体 olive `#3e4c2a` | 495.2–1454.8（宽 959.7） |
| W43 ru-en 已发版 | 同上，逐字相同 | 20pt 粗体 olive `#3e4c2a` | 495.2–1454.8（宽 959.7） |
| W43 ru-de 已发版 | `RUSSISCHER TEXT · DEUTSCHE ERKLÄRUNGEN — DIE AUSGABE FÜR DEUTSCHSPRACHIGE LESER` | 20pt 粗体 BRICK `#a4553a` | 499.7–1450.3（宽 950.7） |
| W45 ru-de（对照） | y=372 俄语副标题**保留**；徽章另插 y=574 | 22pt 粗体 BRICK `#a4553a` | 452.2–1497.8（宽 1045.7） |

- 结论：**英语栏以 W43 ru-en 已发版实测（原位替换）为准的自述成立**——本版徽章与 W43 ru-en 在位置、字号、粗细、颜色、跨度上完全相同。
- 措辞修正（§10 详述）：`(975,574) 22pt BRICK 插入位`是 **W45 ru-de** 的做法，**不是 W43 ru-de 已发版**的做法——W43 ru-de 同样是 y=372 原位替换（仅颜色为德语栏 BRICK）。本版未采用 W45 ru-de 插入位是正确的（任务书亦明令英语栏以 W43 ru-en 为准）。
- 顶栏：本版 `КАЖДУЮ НЕДЕЛЮ ПО-РУССКИ · ONE ISSUE A WEEK · THE RUSSIAN RUSSIANS READ`，跨度 548.9–1401.1（与 KIT 一致），左项止于 371.5、日期起于 1464.7，无碰撞。
- 页脚 8 页全部：左 `Lucerna · RUSSIAN WEEKLY VOL.2 · Russian text · English explanations`，右 `Page N of 8`。
- 双语栏头、P8 分隔符（俄语形）、目录 `все` 均按 W43 ru-en 式样。

## 8. ABSTRACT 与读者园地（§6）

- `ABSTRACT.txt`：英语单行（277 字符，0 换行），无 ASCII 双引号；含真实主题关键词（Wednesday holiday 4 November、one-hour-shorter Tuesday 3 November、11.11 sale、RPL round 14 on 6–8 November）+ 学习者检索短语（`for English speakers learning Russian with real Russian news`）+ `A2 to B2` + `150 exercises`。
- 读者园地：P7 俄语示例信全文与核心逐行同坐标（`— М. (пример от редакции)` 结尾），俄语披露 5 行同坐标保留；英文披露行 2 行（`No real letters or best texts yet — editor's / example; promise for VOL.3.`），与核心中文披露行同为 2 行同基线（1709.88 / 1738.28）。**未编造新读者/信件/引文**。

## 9. 待裁定项：P7 读者园地盒底线擦碰（只报告证据与建议，不因此单独判不通过）

**实测几何（核心与本版像素级相同）：**
- 读者园地盒：`<rect x=1451 y=1254.58 width=434 height=473.0 stroke=#d8cfb4 stroke-width=1.4>`，盒底 = **1727.58**（含半线宽外缘 1728.28）；该 rect 在 SVG 绘制顺序中为 idx 135，**先于**披露语文字（idx 147/148）绘制，故文字墨迹压在线上。
- 披露语第 2 行基线两版同为 **1738.28**；真墨盒（PIL/FreeType ink box）：
  - 核心中文第 2 行：1721.28–1741.78（盒底外缘 1728.28 切入墨顶下方 **7.0px**）；
  - 本版英文第 2 行：1722.28–1742.78（切入 **6.0px**）。
  - 第 1 行墨盒两版均完全在盒底之上（核心止于 1712.38、本版止于 1714.63，距外缘 ≥13.6px）。
- 修正措辞：线穿过的不是“第二行中部”，而是**第二行墨迹的上约 1/3（大写/升部区域）**；线粗仅 1.4px、颜色为浅色 `#d8cfb4`。
- **文字全程可读**：目视裁图 `p7-box-ed-crop.png`（本版）与 `p7-box-core-crop.png`（核心）显示，`example; promise for VOL.3.` 全部字母完整可辨，浅线仅在字间空隙与行尾右侧（英文第 2 行墨迹止于 x=1733.5，盒右缘 1885.7，故有一段无字底线横贯）可见；核心中文行同理。
- **审计 0 flags 的原因（结构性盲区，需如实说明）**：`occlusion_audit.py` 的 LINEX 只统计**后绘**图形压先绘文字（此处盒先绘、字后绘，不触发）；BOXTITLE 的归属判定用文字锚点/中心是否落在盒内——第 2 行锚点 y=1738.28 与中心 y≈1732 均已低于盒底 1728.28，故不被判定为“盒内文字”，也不触发。因此 **0 flags ≠ 无几何接触**；接触本身是真实的，但属核心原样。
- **本版零位移**：盒 rect、披露语两行基线、P7 col3 全部坐标与核心逐值相同；P7 金句规则在 y=1756，第 2 行墨底 1742.78 距其 13.2px。
- **若修（KIT §7a 的 lh+20 方案）的影响评估**：盒底 1727.58 → 1747.58，距金句规则 1756 仅余 **8.4px** 空隙；盒内其余文字不动，仅盒体下扩 20px，不触及其他栏（col3 其余两盒底分别为 1008.08 / 1242.58，与本盒顶 1254.58 无交叠；扩后盒底仍在规则之上）。风险是 8.4px 的余量较薄，但不产生新碰撞；且该修只改英文版盒高，不动核心、不动任何俄语文字坐标。另一种“缩披露为 1 行”方案 KIT 已明令不用（披露四要素必须齐全）。
- **建议**：沿 es-en/es-de P6 擦碰先例的处理方式——**冻结核心几何、接受本版原样**，理由：(1) 缺陷为核心固有、非本版引入；(2) 文字全程可读、无遮挡致误读；(3) 修复余量仅 8.4px 且改动盒高会使本版偏离核心几何、为后续 fan-out 立一个与核心不一致的特例。若协调员倾向“版面零擦碰优先”，则 lh+20 是收敛的 contained fix，可接受。**本校对员不以此项单独判不通过。**

## 10. 自述措辞修正（非缺陷，不影响通过）

1. **基线重跑的口径**：任务书“重跑 freeze.py baseline 复核”若字面理解为对当前 ru-en 构建目录跑 baseline，结果是 0/8 vs 核心（必然，因源码已改后）。正确的独立复核是三条腿（§1）：未改动核心构建 8/8 + 构建者保留基线产物 8/8 + 当前构建目录产物 8/8 等同已发英文版。三者合起来才完整证实“改前基线 8/8 且英文版可复现”。
2. **ru-de 插入位先例的归属**：`(975,574) 22pt BRICK` 是 W45 ru-de 的做法，不是 W43 ru-de 已发版的做法（W43 ru-de 为 y=372 原位替换，见 §7 表）。构建者 KIT §3 称“ru-de 栏先例”时未区分 W43/W45，易误读；但本版实际采用的 W43 ru-en 原位替换经实测正确，不受此措辞影响。
3. **P7 col3“ ends at 1727.58”**：该值是盒底，不是 col3 最后基线（披露语第 2 行基线 1738.28、墨底 1742.78，仍在金句规则 1756 之上）。数值本身无误，仅表述需与“盒底”绑定理解（本报告 §9 已按此口径重述）。

## 11. 文件与交付物核对

- SVG 8 张、PNG 卡片 8 张（均为 1950×2700）齐全。
- `Lucerna-VOL2-EN.pdf` print 版 **13,515,528 字节、8 页**；`Lucerna-VOL2-EN-web.pdf` **3,137,814 字节、8 页**（<10 MB），与 KIT 一致（print 版页尺寸 1462.5×2025 pts，web 版 1400×1938 pts，pdfinfo 实测）。
- WEEKLY-KIT.md 与 ABSTRACT.txt 齐全。未发现 PDF 页数/尺寸异常。
- 本次校对未改动待校版、核心版、构建目录的任何文件；全部工作产物仅在 `hidden_files/w45/ru-en-proof/` 内。

## 审计输出路径（本报告目录内）

- `REPORT.md`（本文件）
- `freeze-core-baseline.log` / `.json`（核心构建 8/8）、`freeze-baseline.log` / `.json`（英文构建复现 8/8）、`builder-preserved-baseline-hashes.txt`、`core-hashes-after-baseline.txt`、`core-hashes-final.txt`
- `freeze-diff.log` / `.json`、`cyr-diff.log` / `.json` / `.py`
- `p8-compare.log` / `.json`、`dash-parse.log` / `.json` / `.py`
- `occlusion-selftest.log`、`occlusion-ed.log` / `.json`、`occlusion-core.log` / `.json`、`occlusion-vs-core.log` / `.json`
- `advance-scan.log` / `.py`、`p6-check.log` / `.py`、`checks3.log` / `.py`、`images.json`
- `rerun-build.log`（注册表 + 零 FLOW OVERFLOW / HEAD TOO WIDE）、`rerun-svg/`（重跑产物，8/8 等同已发版）
- 裁图：`p7-box-ed-crop.png`、`p7-box-core-crop.png`、`p7-col3-ed.png`、`p7-col3-core.png`、`p6-chart-crop.png`、`p6-chart-view.png`、`p1-top-crop.png`
