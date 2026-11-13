# GATE-LOG — Lucerna Weekly 2026-W47 · nl-es fix1（机械门自跑结果）

版：`production/2026-w47/2026-w47-nl-es/`。全部命令用 `tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3），输出均在 `hidden_files/w47/scratch-fix-nl-es1/`。
修后产物只在 `scratch-fix-nl-es1/rebuild/`（印 PDF + 网 PDF + svg/ + cards/）；生产 PDF/SVG 未覆盖。

## 1. 开工三 SHA（生产，核对通过）

| 文件 | SHA-256 | 字节 |
|---|---|---|
| De-Lucerna-VOL4-nl-es.pdf（印） | 45a4c25ea7780d378dbc41c8b95290d4c12121b99e11634611383cb9593697a8 | 12,669,539 |
| De-Lucerna-VOL4-nl-es-web.pdf（网） | 47d4a6c6c0e8e3b150ced86ceb830ca9bc41b3d72a6d67b7523d7c499fed59eb | 1,616,177 |
| 2026-w47-nl-es.text.md | 44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb | 47,649 |

## 2. 修后三 SHA（scratch rebuild/）

| 文件 | SHA-256 | 字节 |
|---|---|---|
| De-Lucerna-VOL4-nl-es.pdf（印） | e6c285668e99e80a4651d2377ee3dd3ccce6c5ea54a288963aa07012e233a8e5 | 12,669,546 |
| De-Lucerna-VOL4-nl-es-web.pdf（网） | 48b35efc1b858a143bed01075ca22038123770f31e064e2818caf2db99ba812f | 1,616,171 |
| 2026-w47-nl-es.text.md | 44fc3d5c42875e56cad0dcaaf5c0b977f6346ec06324c6b2b4d9d321b19d00eb（未变） | 47,649 |

## 3. 缺陷光栅量测（edge_raster.py，600 dpi，限 1862 SVG px）

| 带 | 修前 | 修后 | 余量 | 结论 |
|---|---|---|---|---|
| D1 P6 图标题 | 1866.24 | 1849.44 | +12.56 | PASS |
| D2 P1 桥接行 | 1866.24 | 1856.16 | +5.84 | PASS |
| D2 P2 栏目标题 | 1865.76 | 1855.68 | +6.32 | PASS |
| D3 P2 家具行 | 1864.00 | 1853.92 | +8.08 | PASS |
| D3 P3 家具行 | 1864.00 | 1853.92 | +8.08 | PASS |
| D3 P4 家具行 | 1864.00 | 1853.92 | +8.08 | PASS |
| D3 P5 家具行 | 1864.00 | 1853.92 | +8.08 | PASS |
| D3 P6 家具行 | 1864.00 | 1853.92 | +8.08 | PASS |
| D3 P8 答案头行 | 1864.00 | 1854.08 | +7.92 | PASS |

整页墨右（不含页脚带 y>2550）：修后 P1 1862.24（刊头日期 + hline 端点 x2=1862.0 + 满栏照片边，见 FIX-LOG §4）、P2–P8 1861.92。修前 P7 1861.92、修后 P7 1861.92（无变化）。
原始输出：`edge-before.json` / `edge-before.log`、`edge-after.json` / `edge-after.log`。

## 4. 机械门

| 门 | 命令 / 证据 | 结果 |
|---|---|---|
| freeze diff | `freeze.py diff --core-svg production/2026-w47/core-nl/svg --edition-svg rebuild/svg` → `freeze-diff-after.json/log` | rc=0；新增 CJK 仅 U+3000 ×7（P2–P8 各 1） |
| freeze baseline（核心） | `freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out scratch-fix-nl-es1/freeze-core` | **8/8 SVG 字节一致**；核心 SVG 完整性复核无变化 |
| p8 compare | `p8.py compare --core-p8 core-nl/svg/p8-toets.svg --edition-p8 rebuild/svg/p8-toets.svg --total 150` → `p8-compare.json/log` | **CLEAN**；150/150 noted；keydiff [137, 138]（与修前一致） |
| occlusion audit | `occlusion_audit.py --selftest`（6 类全触发，干净对照静默）+ `occlusion_audit.py rebuild/svg` → `occlusion-after.json/log` | **0 flags** |
| P8 最小字号 | PyMuPDF 取重建印 PDF P8 全部 span 字号 | **10.12pt**（≥ 9.75pt 底线；与修前一致） |
| 题量 | `run.py`（rebuild/）→ `build-fix1.log` | TOTAL **150**；by page 10/18/18/18/18/18/12/38 |
| 文字层一致 | `webpdf.py rebuild/svg → rebuild web PDF`（46,815 text bytes）；pdftotext 三方比对 | 网 vs 印（修后）：**0 行差异**；修前 vs 修后（印/网）：多重集一致，仅 1 空行 + 137–139 读序抖动 |
| SVG 元素级比对 | `svg_diff.py`（生产 svg vs 重建 svg，逐元素） | 元素数一致；**仅 9 处不同**，恰为本次修复；P7 0 处不同 |
| 视觉裁切 | `crop-D1-before/after.png`、`crop-D2P1-before/after.png`（4× 放大） | D1 末字母 A 修前越盒缘、修后留白；D2 文字无损 |

## 5. 生产零写入核对

- `snapshot-before.sha256` vs `snapshot-after.sha256`（44 文件）：仅 5 个 .py 变化（bslib4.py、content12.py、content34.py、content56.py、content8.py）；PDF/SVG/.text.md/assets/cards 全数一致。
- 未 commit、未 push。定稿须另派独立 re-proof。

## 6. 已知事项 / 提醒协调员

- `hidden_files/w47/briefs/brief-coordinator.md` 不存在（开工即无）；本次按任务正文 + SOP + ru-pt fix1 已验做法执行。
- core-nl 的 `git status` M 项（.text.md / FIX-LOG.md / WEEKLY-KIT.md）mtime 15:58–16:28 UTC，早于本次开工，非本次写入。
- P1 整页墨右修后 1862.24：成分为设计边（刊头日期行、hline 端点、满栏照片），非缺陷文本；缺陷带本身修后 1856.16，余量 5.84px。
- 网 PDF SHA 不可重现：修后网 PDF 仅在 scratch 内重建、比文字层通过；入仓时由 insert 流程重新生成。
