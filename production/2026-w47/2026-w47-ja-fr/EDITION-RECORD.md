# EDITION-RECORD — 2026-w47-ja-fr

- Slug: `2026-w47-ja-fr` · Target: Japanese · Reader: French · VOL.4
- Status (fix round 1, 2026-11-11): **已返修，门禁全绿，待第二轮全量复校** — D1/D2 六处罗马字已改，整期重渲染，机械门全绿；按 SOP §8 须再做一轮全量复校至零问题方可定稿。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-fr/`

## Deliverables (measured 2026-11-11, fix round 1; pre-fix values in KIT §8)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-FR.pdf` | 28,348,000 | `1f3b28f4eae5b23c57bf6dac67b976d8e167efd09825ebdcdc10fa9bb9f2fdcb` |
| Web PDF `Lucerna-VOL4-JA-FR-web.pdf` | 4,458,587 | `4f02e8c8f9dec50844906ec8c43e0e13520aa98897a49a14685468c6f6dd2b8b` |
| `2026-w47-ja-fr.text.md` | 46,882 | — |
| `ABSTRACT.txt` | 330 | — |
| `WEEKLY-KIT.md` | 15,154 | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。仅 p8 SVG 相对修前变化（p1–p7 字节一致）。

## Gates (fix round 1 re-run)

- run.py exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE；登记表 TOTAL 150（A2 48 / B1 73 / B2 29）
- Freeze：runA vs runB 两轮构建，8 SVG **8/8 字节一致**
- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- P8 extract (`tools/p8.py extract --total 150`): **150/150**
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成法语，预期值）；150 键值与第一轮复校 extract 逐键比对，0 差异
- 文字层：print/web pdftotext **逐字节一致**，47,210 B
- P8 最小字号（PyMuPDF）：**9.98pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py + KIT 全扫 **0**
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×；VOL.4 ×10 / VOL.3 ×1 / VOL.5 ×4 / VOL.2 0×；徽章 141 枚（A2 45 / B1 70 / B2 26）
- 目视：印刷版 8 页（110 dpi）+ 网页 P1/P8 全读，P8 答案区放大核实 6 处改动；无溢出、无重叠、无截断、无压页脚

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- 第一轮返修（2026-11-11）：修 D1（`Fujiryūga` → `Fujiryōga`，keys 49/54/63/111/116）与 D2（`Umi-no-umi` → `Chura-no-umi`，key 48），只改 6 条答案注释；`export-textmd-fr.py` 缺失已重建（SVG 文本导出，修前源上验证字节一致）；门禁证据在 goals scratch `hidden_files/w47/scratch-ja-fr-fix1/`。
- 待办：第二轮全量复校（协调员派）。
