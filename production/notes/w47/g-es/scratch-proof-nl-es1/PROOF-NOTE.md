# PROOF-NOTE — 2026-W47 nl-es（独立校对 proof1，delta build-4）

**结论：(b) 有缺陷，不可定稿。**
缺陷 3 项（D1–D3），同一根因：西班牙语（拉丁）字符串以 `Noto Sans CJK SC` 排版，Cairo 实际排宽比 PIL/svglib 单字体实测宽 1.4–4.1px，印墨越过内容右缘 1862。须缩短 5 个西班牙字符串（7 处调用点），重渲染后以交付 PDF 光栅边缘扫描复验。
Delta 六处 D6–D11 全部复核通过；旧版 7 项缺陷已修/证伪；150 题三源 150/150；其余全部门禁通过。生产目录未动（见末节）。

**版本：** 2026-W47 `2026-w47-nl-es`（荷兰语目标 × 西班牙语读者），VOL.4，8 页，150 题。
**校对范围：** 仅 `production/2026-w47/2026-w47-nl-es/`，对照 `production/2026-w47/core-nl/`（fix5 定稿）与 pre-delta staging `production/2026-w47/fanout-nl/2026-w47-nl-es/`。未碰核心与其他版；未提交、未推送。

## 1. 三 SHA 实测（与任务给定值逐字节一致）

| 成品 | SHA-256（实测） | 大小 |
|---|---|---|
| 印 `De-Lucerna-VOL4-nl-es.pdf` | `45a4c25ea7780d378dbc41c8b95290d4c12121b99e11634611383cb9593697a8` | 12,669,539 B |
| 网 `De-Lucerna-VOL4-nl-es-web.pdf` | `47d4a6c6c0e8e3b150ced86ceb830ca9bc41b3d72a6d67b7523d7c499fed59eb` | 1,616,177 B |
| 文 `2026-w47-nl-es.text.md` | `44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb` | 47,649 B |

核心对照实测：印 `b7d4a9cd…`/25,955,578 B、网 `5a47449c…`/2,104,000 B、文 `0b97a48d…`/44,093 B，与给定值一致。
Pre-delta 比对：除 p4 外 7 页 SVG 与 staging 逐字节相同；p4 唯一不同（`e90c156c…` vs staging `278c621a…`），与 D11 预期一致。
KIT 已更新为 build-4 三 SHA（`WEEKLY-KIT.md` L19/L21/L122–127 实测一致）。

## 2. 缺陷清单（3 项，同一根因）

裁定标准（任务定）：以**交付 PDF 渲染像素**为准，卡片测量不能单独作证。内容右缘 1862（左缘 88），页 1950×2700。

**根因（实测机制）**：PIL/svglib 单字体测度低估了 CJK 字体中拉丁串的 Cairo 排宽。例 P6 标题：PIL getlength = 400.88，svglib `text_w` = 401.0，但 Cairo 排进 PDF 的 span 宽 404.8（x1 = 1866.3）。Occlusion 审计（PIL 计度）对此类越框盲区；1:1 卡片 + 严格阈值 `<128` 的像素扫描也漏测（我自己的 1:1 卡片扫描对 P6/P2/P8 均返回 0），因为越框墨是边缘抗锯齿斜线、非满黑；2× CairoSVG 渲染与 300/600dpi PDF 光栅均可测。
**对照组**：同一方法扫描核心印 PDF（200dpi，严格 `<128`），8 页右缘全部 0 像素越 1862——核心的对应行 PIL 余量同样只有 +0.1/+0.2px，但中文串渲染与 PIL 一致，未越框；左缘核心与本版均有 x=87.8（0.2px）系统性墨，属系统误差、非缺陷。
**KIT 判定已证伪**：KIT（L41、L103）称 P6 标题“真墨探针到卡片最右黑像素 x=1861”“0 真溢出”——与交付 PDF 实测（墨至 1866.08）矛盾。同期 staging build-3 印 PDF 同样在 P6 测得 1865.9：缺陷自 build-3/W46 起已存在，**非 delta 引入**。

### D1 — P6 统计图盒标题越框 +4.08px
- 源码：`content56.py:150`，`p.text(ix + 22, yy3 + 26, ..., 24, "sans", True, OLIVE)`；x=1461.5，基线 y=242；串 `DE GRAFIEK　DATOS DE PRÁCTICA`；盒 x=1440–1862，y=200–717。
- 实测：PIL 真墨右 1862.5（−0.5px）；交付印 PDF 300dpi 墨带 y231–241 至 1865.9，600dpi 至 **1866.08（+4.08px）**；交付网 PDF 300dpi 同带至 1865.9；2× CairoSVG 重渲染墨至 1866.0–1866.5；PDF span x1=1866.3（vs PIL 排宽 400.9，Cairo 404.8）。
- 渲染证据：`crops/p6-title-de-grafiek.png`（放大裁切，末字母 "A" 的右斜边跨过奶油盒右缘落到白纸上）。
- 修法建议：缩短西语 gloss（例如 `DATOS DE PRÁCTICA` → 更短，如 build-3 修旧 D1/D2 的做法）或降字号，至 Cairo 渲染墨右 ≤1862（建议留 ≥1px 余量，即墨右 ≤1861）。

### D2 — P1 桥接行与 P2 栏目标题越框（+3.8px / +3.4px）
- P1 桥接行：`content12.py:147`，`p.text(RIGHT, qy + 36, "Lee la primera página y elige la respuesta correcta　Respuestas en la página 8", 20, "sans", False, GREY, anchor="end")`，基线 2348。PIL 真墨右 1861.7（+0.3px）；交付印 PDF 300dpi 墨带 y2334–2348 至 **1865.8（+3.8px）**。证据：`crops/p1-bridge-row.png`。
- P2 栏目标题：`content12.py:214`，`p.text(RIGHT, dy + 28, "Wat hoort bij pakjesavond?　¿Qué palabras pertenecen a Pakjesavond?", 20, "sans", False, GREY, anchor="end")`，基线 1594。PIL 真墨右 1861.8（+0.2px）；交付印 PDF 300dpi 墨带 y1579–1587 至 **1865.4（+3.4px）**。证据：`crops/p2-head-row.png`。
- 修法建议：同上，缩短西语部分或降字号。

### D3 — 共享练习头家具行（P2–P6 五页）与 P8 答案头行越框（+1.8px）
- 家具行（同一串，五页）：`content12.py:235`（P2）、`content34.py:50`（P3）、`content34.py:147`（P4）、`content56.py:65`（P5）、`content56.py:180`（P6）：`p.text(RIGHT, ey + 28, "Respuestas en la página 8　Los niveles están mezclados; busca tu número", 20, "sans", False, GREY, anchor="end")`。PIL 真墨右 1861.8（+0.2px）；交付印 PDF 光栅：P2 墨带 y1867–1874、P3–P6 墨带 y1639–1646，均至 **1863.8（+1.8px）**（200dpi 1863.4）。一处修串即修五页。
- P8 答案头行：`content8.py:133`，`p.text(RIGHT, 1302, "Cada respuesta tiene una nota breve en español　✓ marca el ejercicio de escritura", 19.5, "sans", False, GREY, anchor="end")`。PIL 真墨右 1862.0（0.0px）；交付印 PDF 300dpi 墨带 y1292–1302 至 **1863.8（+1.8px）**；核心对应 P8 行最大 1861.0（干净）。
- 全页光栅边缘扫描（200dpi，严格 `<128`，x1850–1950 与 x0–100 两带，8 页）：仅上述 R 带，余无；P7 R 干净。
- 修法建议：缩短两串（家具行可删「busca tu número」等；P8 行可缩短），重渲染后以 PDF 光栅边缘扫描复验。

**影响范围说明**：其余盒标题 PIL 余量 +19.5px 至 +267px，PIL–Cairo 差距（≤4.1px）无法翻转其中任何一项。P7 HET WOORD 标题 PIL +21.8px、P6 VOOR OF TEGEN 标题 PIL +103.5px，渲染卡像素行确认最右黑像素 1840.0（P7）与 1758.0（P6），在内。

## 3. Delta 六处复核（全部通过）

- **D6（P3 桥接 w=377.5）**：以本版自有 `svglib.wrap`、0.5px 步长实测区间 329.5–425.5，连续，中点 377.5，shipped w 在区间内，重现两目标行（`Completa en perfecto. Fíjate en los` y=2303.5 / `auxiliares hebben/zijn.` y=2333.225）；p3 SVG 与 pre-delta 逐字节相同。✓
- **D7（P7 gloss 桥接 w=419.5）**：实测区间 414.5–424.5，连续，中点 419.5，重现三行（y=725.66 / … / 785.11）；p7 无孤儿、无回归。✓
- **D8（P6 标题 capcn_w=370.75）**：实测区间 349.5–392.0，连续，中点 370.75，重现四行（基线 635.02/659.44/683.86/708.28）；`P6 chart ends 717` 不变；p6 无行首标点。✓
- **D9（Q140 键已修）**：三源一致——登记 `content8.py:75`、text.md:415、P8 节点（y=2189.3/2205.0）均为「Ik maak een surprise met een kort gedicht.」，附注「surprise: expresión fija; corto = kort」。手验：键 `kort` 与题干西语「Hago una sorpresa con un poema corto.」（corto = kort）契合，且与 P2 正文「schrijf een gedicht — kort is ook goed」一致（en Q73 链教训：三源一致错也查不出，故加此手验）。p8 keydiff = [137, 138]（仅翻译题按设计对西语重定向）。✓
- **D10（P7 致读者信 dt_zh_w=362.5）**：实测区间 319.5–405.5，连续，中点 362.5，重现两行（`Sin cartas reales ni mejores textos:` y=1783.27 / `ejemplo; la promesa pasa a VOL.5.` y=1811.67）；`P7 col3 ends 1927.0` 不变；p7 无行首标点。✓
- **D11（P4 HET PROGRAMMA 盒，62→89）**：源码 `content34.py:130-134`，`sh = 89 + sum(...) + 32 + 30`；盒 rect x=1439.5, y=591.6, w=422.5, h=638.0，底 1229.6；末行「18:45 uur.」基线 y=1209.49（SVG 实测），基线余量 **+20.11px ≥ +20px 标准** ✓。PIL 真墨末行 x=[1461.5,1563.0], y=[1194.2,1209.7]，墨余量 +19.86px（delta 称 +20.60px，两者均 ≥ 盒边，差值来自测量方法，小差异、如实记录）；盒下 7px 带（y1229.6–1240）渲染像素扫描：我重渲染的卡片与交付印 PDF（150dpi）均为 0 黑像素。事实行换行数重算：serif 21.5、CW−44=378.5 时 3/3/3/2/3 = 14 行，sh 旧 611.0 → 新 638.0 ✓。p4 为唯一改动 SVG。✓

## 4. 旧版缺陷状态（上一轮 7 项，逐项独立重验）

| 旧项 | 状态 |
|---|---|
| D1 P6 VOOR OF TEGEN 标题 +47.8px | 已修：build-3 重 fanout 缩短 gloss 为 `¿SÍ O NO?`，现 PIL 余量 +103.5px |
| D2 P7 HET WOORD 标题 +34px | 已修：gloss 缩短为 `PALABRA SEMANAL`，现 PIL 余量 +21.8px |
| D3 P2 c 项 +8.5px | **未重现**：旧报告误引题为 "eten voor het paard van Sinterklaas"；实际题为 `c. eten voor Sinterklaas' paard`（P2 y=2233，x=1473.5，size 23），PIL 真墨右 1790.0，余量 +72.0px，与核心一致 |
| D4 text.md 150 个答案全标 `答案：` | 已修：`答案：` 出现 0 次，标签现为 `Respuesta:`；CJK 总数 0，U+3000 59 个（分隔符） |
| D5 Q63/Q126「PSV 26 分无来源」 | **误报**：事实在版内——text.md:187 与 P4 HET PROGRAMMA 盒（SVG y=1054.37 `Stand Eredivisie na 12 ronden: PSV` / y=1084.90 `26, Feyenoord 25, Ajax 25 punten.`），核心同款在 text.md:188 亦有。外部复核：独立检索确认 12 轮后 PSV 26 / Feyenoord 25 / Ajax 25（doelpunten.nl、FR12、1908.nl、VAVEL、sportradar、soccerstats 等 6+ 源一致），Heerenveen–Feyenoord 5–3 亦确认 |
| D6 Q140 键丢 `corto` | 已修（见 §3 D9） |
| D7 网 PDF 丢唯一斜体 | 已修：网 PDF 含 `LucernaNewsreader-Italic`；P1 `«de groepswinst»` 在印/网中均为斜体（16.12pt） |

旧 O2（P2/P5 EN JIJ 盒 +0.9px）现测 +2.8px（P2）/+2.9px（P5）真墨余量——通过，偏薄（见 §6）。
旧 O3（P6 DE GRAFIEK 标题 +0.5px）已升格为本次 D1：旧判定依据 PIL +0.5px 与 1:1 卡片扫描，两法均对本类越框不敏感。

## 5. 150 题手验（题干 vs 核心 0 差异，键 vs 键 0 差异，P8 印出键 vs 登记键仅设计内差异）

三源比对 150/150 MATCH（登记 vs text.md 答案 vs P8 印出键；Q150 为开放写作题例外）。
- 荷兰语题干与核心 text.md 逐一比对：仅 Q139/Q140 差异，按设计（翻译题对西语重定向）；Q1/Q25/Q141 的三源“差异”经核实为我方解析器跨栏位产物，可见差异仅为 gloss 语言西语 vs 中文。配对题键经 P2/P8 选项表逐一核对：Q25–28 = d/c/a/b（a. 愿望清单 / b. 小诗 / c. 马食 / d. 门边之鞋），Q141–144 = b/c/d/a。
- 算术重算：Q22/Q45 11月16日→12月5日 = 19 天 ✓；Q43 14→15日 = 1 天 ✓；Q44 12:00–16:00 = 4 小时 ✓；Q46 2009→2026 = 17 年 ✓；Q85 35+30=65 ✓；Q87 35+30+20+15=100 ✓。小组积分 NL/GR 8、DE 5、SRB 0 与四场比分内部一致（NL 1–1、2–1、2–2、2–1 = 8；DE 0–1、2–0、0–0、1–1 = 5）。
- 日期/星期经 `date` 核对：2026-11-01 周日、11-11 周三、11-14 周六、11-15 周日、11-16 周一、11-21 周六、11-22 周日、11-24 周二、11-29 周日、12-05 周六，全部与版内一致；intocht Grave 11月14日周六、Amsterdam 11月15日周日、第 88 届；VOL.5 预告（11月24日周二 Real Madrid–PSV、Feyenoord–Porto；11月29日周日 Feyenoord–Ajax）。
- Q150 模型文 81 词（80–100 范围内），内容与版内事实一致（Oranje 周一 20:45 柏林 NPO 3、journaal 18:00、NEC–PSV 周六、schoen+wortel+verlanglijstje、Robinson 周日晚、pakjesavond 12月5日）。
- Q78 键 `gaat maken`（Zij 单数）：与 Q79「De kinderen → gaan schrijven」（复数）构成单/复数对比设计，有设计依据，列观察 O1、不列缺陷。

## 6. 观察类（不列缺陷）

- **O1** Q78 `Zij` 单数读法：见 §5。属练习设计，协调员定夺。
- **O2** 盒底偏薄 3 处（通过）：P2 EN JIJ 真墨余量 +2.8px、P5 EN JIJ +2.9px、P6 统计图 +4.2px；7px 盒下带 0 黑像素。
- **O3** 左缘系统性墨 x=87.8（0.2px）：8 页均有，核心亦同，属渲染系统误差。
- **O4** 核心继承、无孤儿：孤儿横扫 1452 行（PIL + svglib + 暴力行首标点），a 类 0、b 类 0；spill 横扫 6 处 BELOW 候选均为下一栏自有标题/注脚，非溢出，真溢出 0。
- **O5 D5 字体（只记录、不修，待用户定范围）**：本版字体统计 Noto Sans CJK SC 645 / Newsreader 967 / Noto Serif CJK SC 25 / UnifrakturMaguntia 1；纯拉丁-CJK 段每页 58/66/59/58/61/62/63/70 = **497**（核心 245，38/23/30/29/29/26/18/52）。西语解释层全部以 CJK 字体排拉丁文——此为 §2 越框根因的合理机制解释，但仅作记录；修法在版面字符串，不在字体。
- **O6** P6 中栏、P4 中栏存在大片留白（核心版式继承，非缺陷）。

## 7. 目视 P1–P8（重建渲染卡，8/8 与生产 SVG 逐字节一致之 SVG 重渲染）

P1–P8 逐页目视：版式干净，无重叠、无压页脚、无截断；图片均有来源标注（Wim van Rossem/Anefo、国立档案馆 CC0；Spaarnestad/Wikimedia 公有领域；Elise Iovenko/Unsplash CC0；Cristina Gottardi/Unsplash CC0；Aaron Burden/Unsplash CC0）。P4 HET PROGRAMMA 盒目视确认末行下方留白充足（D11 实修）。约 2–4px 的右缘越框在整页尺度下不可见，仅在放大/光栅扫描中可测——这正是它被 PIL 与 1:1 卡片漏过的原因。
P1 斜体 `«de groepswinst»` 正确；P8 F 节配对选项表与答案区一致；页脚「Página N de 8」完整。

## 8. 生产未动证明

- 校对全程只在 scratch 内重建/重渲染；生产 SVG 哈希在重建前后两次核对一致（`prod-svg-sha.txt`）。
- 生产三成品 SHA 与 §1 一致；核心三成品 SHA 与给定值一致；freeze baseline 后核心 8 SVG 逐字节一致。
- 工作树状态说明：`git status` 中 core-nl 的 M 项（content34.py、content7.py、FIX-LOG.md、KIT、text.md）与 `2026-w47-nl-es/` 未跟踪目录均为校对开始前核心 fix5 与 delta 工作留下的状态，非本人写入——本人未在生产目录写任何文件，未 commit、未 push。

## 9. 待办（供协调员）

1. 按 §2 修 5 串（7 处调用点），重渲染，重验三 SHA。
2. **程序级建议**：PIL/svglib 计度对 CJK 字体拉丁串低估 1.4–4.1px，且 1:1 卡片 `<128` 扫描漏测边缘抗锯齿墨——门禁应加一道**交付 PDF 光栅边缘扫描**（本 proof 的 `edge_raster.py`：200dpi 严格阈值，x1850–1950/x0–100 两带），并作为盒标题越框的裁定法；KIT 的“0 真溢出”式判定须以该法为准，不以卡片为准。
3. D5 字体问题待用户定范围（只记录）。
