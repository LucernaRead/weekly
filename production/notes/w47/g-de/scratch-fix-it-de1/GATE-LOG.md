# GATE-LOG — 2026-W47 it-de fix1 (proof2 D1/D2)

- 对象：`production/2026-w47/2026-w47-it-de/`（修后交付件；修前三 SHA 见 FIX-LOG.md §0）
- 日期：2026-11-11；修复员：fix-it-de1（先 stage 副本改+重建+验门，全部通过后拷回生产；未 commit、未 push）
- 探针：`git hash-object -w /dev/null` → rc=0，`e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`；goals-side scratch 真实写盘通过（`probe.txt`）。`PYTHONDONTWRITEBYTECODE=1` 全程，TMPDIR=`$SCRATCH/tmp/`。
- 结论：20/20 门禁通过（stage 与生产各一次），两处缺陷以交付 PDF 渲染像素三重实测修复。

## 逐门结果（stage / 生产，两次均为 20/20）

### G1 探针与 SHA 核对 — PASS
- 探针通过（上）。
- 修前：印 14,037,260 B `ee5a962f…` / 网 1,297,292 B `e6d3df84…` / 文本 56,699 B `8660fc02…`，与任务简报逐字节一致。
- 修后：印 `La-Lucerna-VOL4-DE.pdf` 14,037,237 B，SHA `527b38ce33f20765b211d7191623d76c6fbb3a56f3a19aa5167d7a0f32211457`；网 `La-Lucerna-VOL4-DE-web.pdf` 1,297,272 B，SHA `f9f4343bdcec894854e3362a9f46b6c17d3b992076096c9970b13e1cc27a4d3a`；文本 `2026-w47-it-de.text.md` 56,683 B，1317 行，SHA `36a11a8f2b58452374b7211434b78e4526c2f584f21764f98a4c2ca9fc302ed4`。8 页，1462.5×2025 pt；网 PDF < 7 MB。

### G2 run.py（stage 副本 `$SCRATCH/stage/...`）— PASS
- RC=0；TOTAL 150；级别 A2 47 / B1 70 / B2 33；页数 10/18/18/18/18/18/12/38；范文 99 词。
- FLOW OVERFLOW / HEAD TOO WIDE / NOSPACE = **0**（日志中无此类行；`rebuild-run.log`）。
- 流末端与 KIT 一致：P4 col3 1140.45、P7 col3 1673.0、P8-ex col3 y=870、P8-keys col3 y=2514（底 2552）。
- 生产副本重跑（`rebuild-prod/`）：run.py rc=0 TOTAL 150，0 溢出；重渲印 PDF SHA 与交付件逐字节相同（`527b38ce…`）。

### G3 SVG 重建与差异 — PASS
- Stage 重建 8 个 SVG：p1/p2 仅标题字符串不同（旧标题替换为新标题后与修前逐字节相同），p3–p8 字节一致。
- 交付后：生产 svg/ 8/8 与 stage 相同（`deliver_stage.py` 校验）。

### G4 重渲印 PDF 与交付逐字节相同 — PASS
- 生产副本重渲（`rebuild-prod/`，OUT/BASE 重定向到 scratch）：RC=0；重渲件 14,037,237 B，SHA = `527b38ce…`，与交付 `La-Lucerna-VOL4-DE.pdf` 逐字节相同。
- web PDF 未重渲染（字节不可复现，只比文字层，见 G8）。

### G5 freeze 核心 baseline 8/8 — PASS（stage + 生产）
- `tools/freeze.py baseline`：stage **8/8 字节一致**（`freeze-baseline.log`、`freeze-baseline.json`）；生产 **8/8 字节一致**（`freeze-baseline-prod.log`、`freeze-baseline-prod.json`）。Core 完整性复核通过（两次）。

### G6 freeze diff vs core — PASS
- 0 unexplained fragments（P1–P7）；新增 CJK 仅 U+3000 ×13（家具分隔符，豁免）；其余新增全为德语讲解层/家具，删除全为 core 中文讲解层；意大利目标语零改动（`gates-stage.log` / `gates-prod.log`，gates.py freeze-diff 段）。

### G7 occlusion audit — PASS（盲区声明不变）
- `tools/occlusion_audit.py`：交付 svg 扫出 **0 flags**（stage 与生产各一次）。
- 盲区：occlusion 对无边框奶油盒横向溢出是盲的——本轮 D1/D2 的修后验收以奶油盒扫描 + 交付 PDF 渲染像素三重实测为准（见 G11/G21），不以 0 flags 背书。

### G8 印/网文字层一致 — PASS
- pdftotext 多重集相同：各 7,784 词，字符集相等（7787 → 7784：D1 标题 `DIE WOCHE IN ZAHLEN` 4 词 → `ZAHLEN` 1 词，−3）；网 PDF 1,297,272 B < 7 MB。

### G9 P8 最小字号 — PASS
- SVG 最小字号 13.0 px = **9.75 pt**（SOP §1.1 下限）。

### G10 §1.1 视觉规格 — PASS
- 纸色 #fbfaf6 在；无金/砖/近黑；VOL.4 ×9；VOL.5 仅 3 处合法节点（预告/LETTERE 说明/P2 交叉引用）；徽章色 A2/B1/B2 在；无双层外框（0 全页 rect）。

### G11 奶油盒 PIL 真墨扫 — 0 处溢出（缺陷已修）
- 自写 `scan_box_titles.py`：29 个 #f0eee5 盒全扫（每盒首行标题 PIL 真墨 vs 盒右缘）。
- 修前：D1 1099.8（−138.8）、D2 991.5（−30.5）两处溢出；其余最紧 P7 `ERRORI TIPICI　TYPISCHE FEHLER` +13.8。
- 修后（stage 与生产）：**0 flags**。D1 `LA SETTIMANA IN CIFRE　ZAHLEN` 墨迹右缘 936.0（+25.0）；D2 `LA FRASE PER RICORDARE　MERKE` 951.5（+9.5）。
- 候选否决记录（PIL 真墨，盒右缘 961，下限 +5）：D1 `IN ZAHLEN` −5.0、`IN ZIFFERN` −9.8、`DIE WOCHE` −12.8、`DIE ZAHLEN` −18.2、`WOCHENZAHLEN` −77.5、`WOCHE IN ZAHLEN` −95.5、`ZAHLEN DER WOCHE` −117.0；D2 `LEITSATZ` −14.2、`MERKE DIR` −35.2、`ZUM MERKEN` −63.5。另实测未选：D2 `LERNE` +14.5（lernen 不如 merken 贴切）、`SATZ` +34.5（丢 "remember" 义）。见 `measure_candidates.log`。

### G12 横向 spill 扫 — 未重跑（proof2 结论沿用；本轮改动不涉及页边文本）
- 本轮只改两处盒标题（墨迹右缘均在盒内 961 以内，远离页边 1862）；proof2 的横向 spill 扫（1617 节点，实墨越线仅 P8 两处非缺陷项）不受影响。P8 家具行/范文行越线量（+2.4/+1.4 px）为 proof2 已裁定的非缺陷，本轮未改动相关行。

### G13 P8 家具行与范文行 — 未变（proof2 裁定沿用）
- 两行均未改动（本轮只改 P1/P2 盒标题）；数值与 proof2 §6 一致，非缺陷。

### G14 孤儿扫 — 未重跑（proof2 结论沿用）
- 本轮改动只缩短两处盒标题（盒内文字量不变、不断行），不产生新孤儿；proof2 孤儿扫 0 结论不受影响。

### G15 p8 extract — PASS
- 150/150 noted，RC=0（stage `de/p8-extract.json`；生产 `de-prod/p8-extract.json`）。

### G16 p8 compare vs core — PASS
- 状态 **CLEAN**，missing=[]，keydiff = **[137, 138, 139]**（预期：重定向的读者句键；Q140 意语句键，core 与本版相同、无 diff，正确）（stage / 生产各一次）。

### G17 text.md validate — PASS
- forward-miss 0 / reverse-miss 0（gates.py textmd 段；stage 与生产各一次）。

### G18 150 键复核 — PASS
- 键 1–150 与 core 一致（除 137–139 重定向与写作项）；notes 与 translations.py 一致（除 137–140 + 写作项）；table_gaps=[]。

### G19 日期/星期 — 未重跑（proof2 结论沿用）
- 本轮未改动任何日期/星期表述；proof2 全验结论不受影响。

### G20 8 页逐版目视 — PASS（两处修后裁图已目视）
- 交付印 PDF 200 dpi 渲染 P1/P2 标注裁图（红线=盒右缘 961，蓝线=墨迹右缘）已目视：D1 `…ZAHLEN` 全在奶油盒内，盒缘余量清晰；D2 `…MERKE` 末字母 E 止于蓝线，奶油延续至红线。裁图：`pages/crop-p1-cifre-fixed-prod.png`、`pages/crop-p2-frase-fixed-prod.png`（stage 版裁图与生产版字节相同，因两版 PDF 字节相同）。

### G21 交付 PDF 渲染像素三重实测（本轮新增验收门，occlusion 的盲区补位）— PASS
- 方法：① PIL 真墨（SVG 源，`OA.ink_box`）；② 96 dpi 渲染最暗像素（渲染坐标 = SVG 坐标 1:1）；③ 文字层 bbox（`pdftotext -bbox`，页码+基线过滤，pt ×4/3 → SVG px）。三者中最紧者为准，下限 +5 px。
- D-1 `LA SETTIMANA IN CIFRE　ZAHLEN`：+25.0 / +29 / +24.9（印+网一致）→ 最紧 **+24.9**。
- D-2 `LA FRASE PER RICORDARE　MERKE`：+9.5 / +11 / +8.1（印+网一致）→ 最紧 **+8.1**。
- Stage 与生产两次实测值完全一致（`verify-triple-stage.log` / `verify-triple-prod.log`）。

## 附加机械核对（非门禁，但已实测）

| 项 | 结果 |
|---|---|
| Q150 范文词数 | 99 词（与 KIT/题面一致，未变） |
| 文本行数 | 1317 行（未变） |
| 印/网词数 | 各 7,784 词（修前 7,787，−3 = D1 标题缩短） |
| 旧标题残留 | `DIE WOCHE IN ZAHLEN` / `MERKSATZ` 在生产目录 + translations.py 中 0× |
| 生产 __pycache__ | 未新增（仅修前 12:15 的 2 个 .pyc） |
| 变更文件（按 hash） | 恰好 8 个：content12.py、svg/p1、svg/p2、印/网 PDF、.text.md、cards/p1、cards/p2；另 KIT §12 追加；其余 6 张 cards 重生成字节相同 |
| 修后三 SHA | 见 FIX-LOG.md 首行与 KIT §12 |

## 备注（门禁过程记录）
- 首轮 stage gates 出现 3 项工具性 FAIL（p8 extract / p8 compare / freeze-diff report），原因是 `de/` 输出目录不存在——p8.py / freeze.py 在 `--json` 父目录缺失时 exit 1。工具本身直接运行时均通过（p8 extract 150/150，freeze diff rc=0）。`mkdir de/` 后重跑即 20/20。生产 gates 用 `de-prod/` 目录，一次通过。
- freeze strict-CJK 门的 `rc=1` 是 freeze.py 的预期行为（有新增 CJK 即 exit 1）；门禁接受，因非 U+3000 新增为空集（仅 13× U+3000 豁免项），与修前一致。

## 证据文件索引（均在 scratch 内）
- `gates-stage.log`、`gates-prod.log` — 20/20（stage / 生产）
- `de/p8-extract.json`、`de/p8-compare.json`、`de/freeze-diff.json`（stage）；`de-prod/*`（生产）
- `freeze-baseline.log`、`freeze-baseline.json`（stage 8/8）；`freeze-baseline-prod.log`、`freeze-baseline-prod.json`（生产 8/8）
- `rebuild-run.log`、`rebuild-render.log`、`rebuild-webpdf.log`（stage 重建）；`rebuild-prod-run.log`、`rebuild-prod-render.log`（生产副本重渲，印 PDF SHA 与交付一致）
- `scan_box_titles.log`（修前：2 flags）、`scan_box_titles_stage.log`（修后 stage：0 flags）
- `measure_candidates.log`、`verify-triple-stage.log`、`verify-triple-prod.log`
- `pages/stage-p1.png`、`pages/stage-p2.png`、`pages/prod-p1.png`、`pages/prod-p2.png`（96 dpi 渲染）、`pages/stage200-p1.png`、`pages/stage200-p2.png`、`pages/prod200-p1.png`、`pages/prod200-p2.png`（200 dpi 渲染）、`pages/crop-p1-cifre-fixed-prod.png`、`pages/crop-p2-frase-fixed-prod.png`（2× 标注裁图，已目视）
- `prod-before.sha256`、`prod-after.sha256`、`svg-sha-before.txt`、`deliver_stage.log`
