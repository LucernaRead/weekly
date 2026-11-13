# EDITION-RECORD — 2026-w47-ja-en

- Slug: `2026-w47-ja-en` · Target: Japanese · Reader: English · VOL.4
- Status (stick 8, 2026-11-11): **完成，已核实** — 交付物齐全，门禁全绿。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-en/`

## Deliverables (measured 2026-11-11, stick 8)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-EN.pdf` | 27,440,477 | `c29f6f987ba709082145c4ca71b7a656eb0b6bcc5f5f49d89f22b35a6161bbeb` |
| Web PDF `Lucerna-VOL4-JA-EN-web.pdf` | 4,428,571 | `9d10efc5fdc72c1c46194eea25cb5ff7b59f52c316a13fb5564395439396beb1` |
| `2026-w47-ja-en.text.md` | 45,706 | — |
| `ABSTRACT.txt` | 275 | — |
| `WEEKLY-KIT.md` | 10,759 | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。

## Gates (stick 8 re-run)

- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- P8 extract (`tools/p8.py extract --total 150`): **150/150**
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成英语，预期值）
- 文字层：print/web pdftotext **逐字节一致**，46,044 B
- P8 最小字号（PyMuPDF）：**9.975pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- 待办：无。
