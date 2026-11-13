# PROOF-NOTE — 2026-W47 pt-ru（葡萄牙语目标 · 俄语读者版）· re-proof 独立复校

- 复校员：独立复校（re-proof），与制作/重建/修复分开；proof1（0fcfc679）之后的重建版复核
- 日期：2026-11-11（UTC 17:16–18:00 前后）
- 版目录：`production/2026-w47/2026-w47-pt-ru/`（规范路径）
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-reproof-pt-ru1/`

## 结论：(a) 零缺陷，可定稿

proof1 的 5 项缺陷 D1–D5 在本次重建中**全部修净**，逐项经 PIL 真墨迹 + 交付印 PDF 200dpi 渲染像素双法独立量测，并有裁剪目视证据。KIT §9（Re-fanout）所载改动逐项复核属实；SÁB 21 改动正确；P1 顶栏标语俄语主客正确；全部框标题逐一 PIL 量测均在框内；150 题逐题手验通过；全部机械门独立重跑通过。**未发现新缺陷。**（两处 KIT 数值出入与一项工具状态出入见 §5，均非版面缺陷。）

## §0 身份核对（磁盘为准，三 SHA 先验值）

| 文件 | 任务给定 SHA | 磁盘 SHA（开工 + 完工两次实测一致） | 字节 | 结论 |
|---|---|---|---|---|
| `A-Lucerna-VOL4.pdf`（印） | `86447421…4a0d2f2` | `86447421b5a5abff48690ed8ab8e4cd51ce9808e5adcaf24f0d8e30004a0d2f2` | 12,916,388 | 一致 |
| `A-Lucerna-VOL4-web.pdf`（网） | `acd86e86…53b779` | `acd86e86bc20562c2080952bec2c89071c85c1733d2cb5183f4dc6d90253b779` | 1,188,615 | 一致 |
| `2026-w47-pt-ru.text.md` | `87871659…88184c8` | `87871659c0101a9d8c2f7bc415946653ea80257032332cda8b1208e6288184c8` | 39,736（535 行） | 一致 |

- 探针通过（`git hash-object -w` 回 `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；本 scratch 可写）。
- 生产目录零写入：开工前 47 个文件 sha256 快照（`presnap.sha256`），完工复核 **0 个非 OK**；run.py 三次重跑（含 keycheck/REG 导出）后 SVG 与 PDF 字节均不变（构建确定性已验）。
- creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383` 与 proof1 所用正典一致。全部命令用 `tools/venv/bin/python`（Python 3.12.3，Pillow 13.0.0），`TMPDIR=<scratch>/tmp`。

## §1 D1–D5 逐项复核（双法 + 目视）

### D1（本版）P7 框标题溢出 —— 修净 ✓
- 现标题（`svg/p7-lingua.svg`，基线 y=242.0）：`ERROS COMUNS　Ошибки`（原 `Типичные ошибки` 已换为 `Ошибки`）。
- 源码行：`content7.py:82`（classify 记录 KEEP）——`p.text(bx + 22, yy3 + 26, "ERROS COMUNS　Ошибки", …)`。
- PIL 真墨：墨右缘 **1764.5**，框右缘 1862.0，**clear +97.5**（与 KIT 称 +97.5 完全一致）；页右边界 1884，余量 +119.5。
- 交付 PDF 渲染像素（200dpi，`pdfrender/print-7.png`）：标题行墨右 **1762.8**，clear **+99.2**；与 PIL 差 1.7px（已知渲染差）。
- 目视：`crops/crop-p7-boxtitle.png`，末字 `Ошибки` 稳在奶油内，右侧大片余量。**修净。**

### D2（本版）P1 数字框标题溢出 —— 修净 ✓
- 现标题（`svg/p1-capa.svg`，基线 y=823.2）：`A SEMANA EM NÚMEROS　Цифры`（原 `В цифрах` 已换为 `Цифры`）。
- 源码行：`content12.py:43`（classify 记录 KEEP）——`f.box("A SEMANA EM NÚMEROS　Цифры", …)`。
- PIL 真墨：墨右缘 **1391.0**，框右缘 1411.5，**clear +20.5**（KIT 称 +20.2，差 0.3px 为量测口径舍入，不影响结论）。
- 交付 PDF 渲染像素：墨右 **1388.0**，clear **+23.5**；与 PIL 差 3.0px（已知卡片/PDF 渲染差，前科约 3px）。
- 目视：`crops/crop-p1-numtitle.png`，末字 `Цифры` 在框内。**修净。**

### D3（核心携带）P1 末行 `em Brasília. (Página 4)` 整行漫出 —— 修净 ✓
- 机制：core fix1 将 EM POUCAS 框高 436→474，框底 **2310.0→2348.0**；quiz 规则线随之由 y≈2311 下移至 **y=2350.0**（绿线 x 88–1862，框底之下 2.0px）；quiz 区整体下移（chip y=2404，flow 末 y=2559）。
- 现版：该行基线 2327.6，PIL 真墨 (1461.5, **2311.6–2332.6**)，框底 2348.0 → **clear +15.4**。
- 交付 PDF 渲染像素：奶油底 2347.7，墨顶 2313.1，墨底 2331.8 → **clear +16.2**。
- 旧 0.2px LINEX 擦过已不存在：规则线现处 y=2350，墨顶 2313.1，相距 36.9px（见 §5 出入 1）。
- 目视：`crops/crop-p1-em-poucas.png`，该行在奶油上，绿规则线在其下，quiz 标题 `QUIZ RELÂMPAGO` 在线下，分隔干净。**修净。**本版几何与 core-pt 完全一致（core creambox 同窗末行基线 2327.6、框底 2348.0）。

### D4（核心携带）P3 末行 `16h30.` 整行漫出 —— 修净 ✓
- 机制：core fix1 将 P3 周框底 **525.0→551.0**（+26px）。
- 现版：该行基线 540.6，PIL 真墨 (1461.5, 524.6–540.6)，框底 551.0 → **clear +10.4**。
- 交付 PDF 渲染像素：奶油底 550.6，墨底 540.5 → **clear +10.5**。
- 目视：`crops/crop-p3-weekbox.png`，`16h30.` 全在奶油内。**修净。**core-pt 同值（框底 551.0、末行 540.6）。

### D5（核心携带）P6 末行降部漫出 —— 修净 ✓
- 机制：core fix1 将 P6 时间线框底 **840.0→854.0**（+14px）。
- 现版：`Página do Participante.` 基线 840.8，PIL 真墨 (1603.5, 825.8–**845.8**)，框底 854.0 → **clear +8.2**。
- 交付 PDF 渲染像素：奶油底 853.4，墨底 845.3 → **clear +8.7**。
- 目视：`crops/crop-p6-timeline.png`，`p` 的降部全在奶油上。**修净。**core-pt 同值（框底 854.0、末行 840.8）。

## §2 KIT §9（Re-fanout，行 141 后）逐项复核

KIT §9 全文读完，逐项独立复核结果：

| §9 载项 | 独立实测 | 结论 |
|---|---|---|
| 三 SHA/字节（印 12,916,388 / 网 1,188,615 / 文 39,736） | 与 §0 磁盘实测完全一致 | 属实 |
| gates 16/16 | 重跑 rc=0，16 PASS，FAILURES: none（`gates.log`） | 属实 |
| occlusion 0 flags（venv） | 重跑 0 flags；core-pt 同跑亦 0 flags（见 §5 出入 1） | 属实（§6 称 1 flag 已过期） |
| p8 extract 150/150, compare CLEAN，keydiff [137,138] | 重跑 150/150，CLEAN，keydiff=[137,138]（`ru-p8-compare.json` 本体已读） | 属实 |
| freeze baseline 8/8 | 重跑 8/8 byte-identical，repointed none | 属实 |
| creambox 0 spill | 全版扫描 438 行，无负 inside clearance；仅三处 desc-clear 负值，均像素裁决为非缺陷（§4） | 属实 |
| boxtitle true-ink clear on all boxes | 33 框逐一 PIL 量测，最小余量 **+8.5**（P1 EM POUCAS）；D1 +97.5、D2 +20.5 | 属实 |
| sweep 0 bridge widows | 重跑 sweep：box-vs-hline 0、bridge orphans 0（20 bridges）、bridge widows 0 | 属实 |
| italic spans print 1 = web 1 | fitz 全文档计数：印 1（P1 `« consciência »`，Newsreader-Italic 16.12pt）= 网 1 | 属实 |
| P8 min font 9.75pt | SVG 答案区最小 13.0 单位 = 9.75pt（1327 spans）；fitz 印/网 P8 答案区最小均为 9.75pt | 属实 |
| check_final word multiset diff 0 | fitz 印/网各 8,093 词，diff 0；pdftotext -layout 印/网各 8,170 词，diff 0（见 §5 出入 2：KIT 正文写 8,095，与其自家 JSON 8,093 不符） | 结论属实，数字一处笔误 |
| Keycheck 148/150，exit 1 by design | 独立重跑 `keycheck_ptru.py`：**148/150，rc=1**，mismatch 仅 Q137（提取截断）与 Q150（✓），与 KIT 所述完全一致（`keycheck-150.json`） | 属实 |
| print/web `pdftotext -layout` 仅 P8 差 40 行单空格列移 | 重跑 diff：40 行，全部在 P8，单空格列移；词多重集差 0 | 属实（已知非缺陷） |
| D5 gloss（core fix2）：ru `титул` | text.md L215 `o título титул`；P4 gloss 框 PIL：4 行，末行右余 +99.5、底余 +42.7（creambox：末基线 398.2，clearance +47.7）；渲染 `o título титул` | 属实 |
| Proof1 fixes D1/D2（本体重建携带） | 见 §1：D1 +97.5、D2 +20.5（PIL），PDF 渲染 +99.2/+23.5 | 属实 |
| SÁB 21（proof1 miss）：fragment key `周六 16` 删除，整句 key 新增，渲染 `суббота, 16:30, дерби Палмейрас–Фламенго` | SVG P2 SÁB 21 格：`16h30`（y=1687.2）、`суббота, 16:30, дерби`（y=1736.5）、`Палмейрас–Фламенго`（y=1761.2）；PIL 末行墨底 1766.2（框底 1768，clear +1.8）；PDF 渲染墨底 1765.0（**clear +3.0**）；text.md L118 一致；`crops/crop-p2-sab21.png` 目视干净。旧版 `Суббота, 16-е:30 дерби` 已无。 | 属实，修净（余量 +3.0px 偏紧但在框内） |
| O3（P7 A PALAVRA 末行 0.5px 零余量）未动 | 几何与 proof1 相同（末基线 1427.0，框底 1431.5）；见 §4 裁决 | 属实，非缺陷如前 |
| text.md 改动 2 行：L215 D5 gloss、L433 逐字行 | L215 `o título чемпион` → `o título титул` ✓；L433 `### Frases da semana (дословно из этого номера)` ✓ | 属实 |
| Hand-patch inventory：27 diffs ALL KEEP，0 REVERT | 读 `ru-classify.json` 本体：KEEP 27、REVERT 0；抽查条目含 D1/D2 标题改动与盒高改动 | 属实 |
| core-fix1 注释 `墨底` SEG key（`нижний край чернил`） | 存在（tables_ru.py 内含该 key；构建无 CJK-0 断言失败，run.py rc=0） | 属实 |

## §3 另核项

### P1 顶栏标语：主客正确 ✓
- 中文原文（core）：「读巴西人正在读的葡萄牙语」；俄译（`tables_ru.py:201`，P1 顶栏 y=92 渲染）：「Португальский, который читает Бразилия」。
- 独立语法判定：关系代词 `который` 为阳性单数；作宾语时，无生命阳性名词的宾格形与主格形相同（`который`），故 `который` 在此为**宾格**（被读的对象 = 葡萄牙语）；`Бразилия` 为主格阴性单数，作 `читает` 的**主语**（巴西）。动词后主语（VS 语序）在俄语中合法。整句解析为“巴西所读的葡萄牙语”——与中文“巴西人正在读的葡萄牙语”一致，无主客颠倒。**无缺陷。**（注：若 `который` 作主格主语，句意将成“读巴西的葡语”，荒谬；母语者按语义与格形自然取宾格读法。）

### 全部框标题逐一 PIL 真墨量测
- 33 个奶油框首行标题全部在框内，最小余量 **+8.5**（P1 EM POUCAS PALAVRAS）；次紧为 D2 +20.5、P2 SÁB 格 +22.5、P6 gloss +27.5、P1 NESTA EDIÇÃO +28.5。无一超框右缘；全版无一墨迹超页右边界 1884（§A 扫描零命中）。最紧三处（D2 +20.5、SÁB21 末行 +1.8~+3.0、O3 +0.6）均经交付 PDF 渲染像素交叉验证。完整表见 GATE-LOG §7（`boxtitles.json`）。

### O3（P7 A PALAVRA 框末行墨距框底仅 0.5px）复核确认
- 末行 `память о борьбе и культуре.` 基线 1427.0，框底 1431.5；PIL 真墨底 1432.0（超框 0.5px，亚像素级）；**交付 PDF 渲染像素：墨底 1430.9，框内 +0.6px**。按任务规则（边缘裁决以交付 PDF 渲染为准），**非缺陷**，与 proof1 裁决一致。`crops/crop-p7-wordbox.png` 目视：末行贴底但在奶油上。

### 其余非缺陷项（像素复核）
- P2/P3/P4/P5 E VOCÊ 框 desc-clear −1.0/−0.9/−0.9/−0.3：PDF 渲染墨底均在框底内 1.3–1.9px（P2 907.7<909、P3 878.4<880、P4 903.4<905、P5 838.6<840.5）。非缺陷（0.30 降部 allowance 高估，如 proof1）。
- P5 数字框 `2027.` desc-clear −1.1：渲染墨底 507.4 < 框底 513（无降部字母）。非缺陷。
- 四处 BELOW-WINDOW（P1 AGORA VOCÊ +37、P2 Atenção +32、P3 UM DIA +37、P6 EXERCÍCIOS +42）：框下另起标题/正文，假阳性如前。

## §4 全文通读 + 150 题手验

- **text.md 全文 535 行逐行读完**：讲解层为俄语，无中文残留（CJK 0）、无内部标签（`cover`/`SOP`/`proofread`/`TODO`/`lint` 均为 0；`VOL.3`×2 与 `VOL.5`×3 均在 P7 读者来信披露/下期预告内，属允许引用；`VOL.4`×2 在页眉）。
- **150 题逐题手验**（`keycheck-150-table.txt`：题干源自 text.md 练习区，key 源自 SVG 答案区 p8-extract，core key 对照；另 REG key 全量比对）：**150/150 通过**。要点逐一核实：Q58 `16h30 é mais cedo do que 17h` → mais ✓；Q73 `Depois da prova, começa a ___. (espera)`，题干与 key 配对正确（P5 正文“Depois da prova, começa a espera”）✓；Q83–86 工作日 10+5=15（16–19 日 4 天 + 23–27 日 5 天 + 30 日 1 天 = 10；周末 21/22/28/29 4 天 + 20 日假日 = 5）✓；Q108 `saíram` ✓；Q109 `sair`、Q110 `for`、Q111 `tiver`（未来虚拟式）✓；Q112 `sair` ✓；Q120 13h30–18h30 = 5 小时 → B ✓；Q124 选项重排后 B=Norris ✓；Q125 周六赛属第 36 轮 → A ✓；Q131 A ✓；Q133–136 造句 ✓；Q137/138 俄译正确（见下）；Q141–144 配对 c/d/b/a ✓；Q145–149 全 A（146 sexto / 147 quinto 与 P4 正文 L211 一致）✓；Q150 开放题 + 样文实测 **88 词** ✓。
- **Q137/Q150（keycheck 两项）独立复核**：Q137——SVG 答案区 y=2118.4 行直读：`137. Пятница, 20 ноября, — национальный праздник. — Смотри заголовок на странице 1`，全文在印，正确俄译；提取器在首个 ` — ` 处截断为工具 artifact，**非缺陷**。Q138——`Палмейрас выиграл 5–4 по пенальти.`，正确俄译，**非缺陷**。Q150——REG key `(открытое задание — образец ниже)`，提取器作 `✓`，为开放题既定标记，**非缺陷**。
- **事实核验**（`date -d`，America/Toronto）：2026-11-15 周日、16 周一、17 周二、20 周五、21 周六、22 周日、27 周五、12-06 周日、11-07 周六、11-08 周日、11-30 周一——与版内星期全部一致。Enem 次日 15 日周日 13h30–18h30 = 5 小时；首日 8 日 13h30–19h。
- **P8 最小字号**：答案区最小 13.0 SVG 单位 = **9.75pt**（1327 spans），恰为 SOP §1.1 下限，不低于下限；fitz 印/网 P8 答案区最小均为 9.75pt，625 spans。
- **弯引号**：P1–P7 内容中直引号 `"` 为 0；P8 U+201C×2、U+201D×2（E139/E140 俄语句源，正确用法）、U+2019×0。P7 语法释义中直单引号 `'выпадать на день'` ×2——与 pt-en 版 `'to fall on a day'` 同一跨版释义引用惯例，**非缺陷**。
- **CJK**：SVG 中除 U+3000 分隔符 ×9 外仅 P1 moth logo `<title>` 内 `三色蛾`（非读者面）；text.md CJK 0。
- **印/网文字层**：均为 8 页 1462.5×2025pt；fitz 印/网各 8,093 词，多重集差 0；pdftotext -layout 印/网各 8,170 词，多重集差 0，行 diff 仅 40 行 P8 单空格列移；自 scratch 重渲染网 PDF（`web-rerender.pdf`，未覆盖生产网 PDF）：文字层与生产网 PDF 多重集差 0，italic 1=1（字节差 2 字节为已知 fontTools wall-clock 不可复现，永不以字节论证）。

## §5 KIT 数值出入（非版面缺陷，记入档）

1. **Occlusion “1 flag”已过期**：KIT §6 称现态工具报 1 flag（P1 LINEX graze，核心自带 0.2px 擦过）。我实跑 `tools/occlusion_audit.py`（自测 planted 六类全触发）对**本版与 core-pt 均为 0 flags**；几何上该擦过在新版已不存在（规则线由 y≈2311 移至 2350，D3 行墨顶 2313.1，相距 36.9px）。KIT 的 1-flag 说法来自 core fix1 之前的旧几何（proof1 当时实跑亦为 0 flags）。**结论：无 flag，无缺陷；KIT 须更新。**
2. **check_final 词数笔误**：KIT §9 称“8,095 words each”；我 fitz 实测印/网各 **8,093** 词，且重建方自家 `ru-textdiff.json` 亦为 8,093。diff=0 的结论正确，绝对数字差 2。**非缺陷。**
3. **D2 clear 口径差**：KIT 称 +20.2；我 PIL 实测 +20.5、PDF 渲染 +23.5。均远在框内，**非缺陷**。

## §6 未决事项

- 无。本版 (a) 零缺陷，可定稿；无需再修。建议协调员在 KIT §6/§9 中更正上述两处过期数字（occlusion 1 flag → 0；8,095 → 8,093），属文档更正，不涉及版面。

## 文件清单（本 scratch）

`PROOF-NOTE.md` / `GATE-LOG.md` / `keycheck-150.json` / `keycheck-150-table.txt` / `stems.json` / `registry.json` /
`run.log` / `gates.log` / `occlusion.log` / `ru-occlusion.json` / `occlusion-core.log` / `core-occlusion.json` /
`p8-extract.log` / `ru-p8-extract.json` / `p8-compare.log` / `ru-p8-compare.json` / `core-p8-extract.json` / `core-p8-extract.log` /
`freeze-baseline.log` / `freeze-diff.log` / `ru-freeze-diff.json` /
`creambox-all.log` / `creambox-core.log` / `inkprobe.py` / `inkprobe.log` / `boxtitles.json` /
`pixelprobe.py` / `pixelprobe.log` / `print.txt` / `web.txt` / `web-rerender.pdf` / `web-rerender.txt` / `webpdf-rerender.log` /
`check_s11_ptru.py` / `check_s11.log` / `check_final_ptru.py` / `check_final.log` / `ru-textdiff-fitz.json` / `italic-check.log` /
`keycheck_ptru.py` / `keycheck.log` / `sweep_ptru.py` / `sweep.log` / `presnap.sha256` /
`pdfrender/print-{1..8}.png` / `crops/crop-p*.png`（7 张）/ `backup-edition/`（开工前全版备份，仅作可逆保障）
