# EDITION-RECORD — 2026-w47-ja-ru

- Slug: `2026-w47-ja-ru` · Target: Japanese · Reader: Russian · VOL.4
- Status (stick 8, 2026-11-11): **完成，已核实** — 交付物齐全，门禁全绿。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-ru/`

## Deliverables (measured 2026-11-11, stick 8)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-RU.pdf` | 25,858,425 | `abc44c9c695ddac9df434e93cf51e6eae5604c7f78b663331603dacc425a525f` |
| Web PDF `Lucerna-VOL4-JA-RU-web.pdf` | 4,396,999 | `e2fc538241a3d1446ab78dab0acfa411b0f95f126a7c926a82f69fe7d350e94e` |
| `2026-w47-ja-ru.text.md` | 52,948 | — |
| `ABSTRACT.txt` | 464 | — |
| `WEEKLY-KIT.md` | 11,514 | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。

## Gates (stick 8 re-run)

- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- P8 extract (`tools/p8.py extract --total 150`): **150/150**
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成俄语，预期值）
- 文字层：print/web pdftotext **逐字节一致**，53,247 B
- P8 最小字号（PyMuPDF）：**9.975pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- ちいかわ按读者语译名 `Чикава`（KIT 记录；未用中文名）。
- 待办：无。
