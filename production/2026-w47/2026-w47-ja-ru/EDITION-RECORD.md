# EDITION-RECORD — 2026-w47-ja-ru

- Slug: `2026-w47-ja-ru` · Target: Japanese · Reader: Russian · VOL.4
- Status (stick 8, 2026-11-11): **完成，已核实** — 交付物齐全，门禁全绿。
- Status (fix1, 2026-11-11): proof1 (b) 缺陷 D1–D4 已修，整期重渲染，全套门禁重验全绿，见 KIT §11 F3。待第二轮全量复校（协调员另派）。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-ru/`

## Deliverables (measured 2026-11-11, fix1)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-RU.pdf` | 25,858,387 | `86af0bb5bd5fb3e2a521cb92cd355185b9e3a1bd297511121b11d30e2f2a1592` |
| Web PDF `Lucerna-VOL4-JA-RU-web.pdf` | 4,396,966 | `dd5fdc63020f5365c714937ac5835c057cd5b42a56005011ce35c6e8db86ef57` |
| `2026-w47-ja-ru.text.md` | 53,029 | — |
| `ABSTRACT.txt` | 464 | — |
| `WEEKLY-KIT.md` | 14,389 | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。修前值（stick 8）：print 25,858,425 / `abc44c9c695ddac9df434e93cf51e6eae5604c7f78b663331603dacc425a525f`，web 4,396,999 / `e2fc538241a3d1446ab78dab0acfa411b0f95f126a7c926a82f69fe7d350e94e`。

## Gates (fix1 re-run)

- run.py exit 0，零 FLOW OVERFLOW / HEAD TOO WIDE；TOTAL 150（A2 48 / B1 73 / B2 29）
- Freeze：两次连续构建 8 SVG sha256 **8/8 相同**
- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- P8 extract (`tools/p8.py extract --total 150`): **150/150**
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成俄语，预期值；逐键比对 146/150 与核心逐字节同）
- 文字层：print/web pdftotext **逐字节一致**，53,363 B
- P8 最小字号（PyMuPDF）：**9.975pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×
- 旧形残留：`Фудзирюг` / `Уми-но-уми` / `единственно правильного` / `Прогноз Японии` / `Оканчивайте` / `一之富士` 在 py/SVG/text.md/双 PDF 文字层 **全 0**；新形 `Фудзирёг` 5×、`Чура-но-уми` 1× 已就位
- 目视：print 8/8 + web P7/P8 全过，无溢出/重叠/压页脚/豆腐块

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- ちいかわ按读者语译名 `Чикава`（KIT 记录；未用中文名）。
- fix1（2026-11-11）：proof1 D1–D4 已修；重 apply 时发现 core-ja 随后把 `一之富士` 改成 `义之富士`，map 键已同步更新（值不变），见 KIT §11 F3。
- 待办：第二轮全量复校（协调员另派）。
