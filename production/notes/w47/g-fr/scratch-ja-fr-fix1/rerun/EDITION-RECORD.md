# EDITION-RECORD — 2026-w47-ja-fr

- Slug: `2026-w47-ja-fr` · Target: Japanese · Reader: French · VOL.4
- Status (stick 8, 2026-11-11): **完成，已核实** — 交付物齐全，门禁全绿。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-fr/`

## Deliverables (measured 2026-11-11, stick 8)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-FR.pdf` | 28,347,993 | `5903a36b47668d91c04dafb047f94022299f8f5308647696fe7cff9c47244517` |
| Web PDF `Lucerna-VOL4-JA-FR-web.pdf` | 4,458,579 | `99fd99aff8f1a8289ae58435efc0a85e04b36e79d1a09ce7d700493e3658c47c` |
| `2026-w47-ja-fr.text.md` | 46,880 | — |
| `ABSTRACT.txt` | 330 | — |
| `WEEKLY-KIT.md` | 10,560 | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。

## Gates (stick 8 re-run)

- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- P8 extract (`tools/p8.py extract --total 150`): **150/150**
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成法语，预期值）
- 文字层：print/web pdftotext **逐字节一致**，47,208 B
- P8 最小字号（PyMuPDF）：**9.975pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- 待办：无。
