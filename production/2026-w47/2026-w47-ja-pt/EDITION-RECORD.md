# EDITION-RECORD — 2026-w47-ja-pt

- Slug: `2026-w47-ja-pt` · Target: Japanese · Reader: Portuguese · VOL.4
- Status (fix1, 2026-11-11): **完成，已核实** — 交付物齐全，门禁全绿。
  第一轮复校 D1 + 力士罗马字 + 2 处框题溢出已修（见 WEEKLY-KIT §12），
  全套门禁重跑通过，待第二轮全量复校（协调员派）。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-pt/`

## Deliverables (measured 2026-11-11, fix1)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-PT.pdf` | 29,103,009 | `9591f16cb82a2e2534f141febc1232632ee6cf02eefa64e84e9b74cb3601b8be` |
| Web PDF `Lucerna-VOL4-JA-PT-web.pdf` | 4,485,030 | `f0cdce302756b0bf118dfaa432af9dfcaf9d66b9d17056adbeb688f26258645f` |
| `2026-w47-ja-pt.text.md` | 46,696 | — |
| `ABSTRACT.txt` | 307 | — |
| `WEEKLY-KIT.md` | — | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。前版（已作废）：
印版 29,103,006 / `5e7542bc…`，网版 4,485,027 / `49914939…`。

## Gates (fix1 re-run)

- run.py (`tools/venv/bin/python`, run3/run4): exit 0, TOTAL 150,
  0 FLOW OVERFLOW / HEAD TOO WIDE；freeze 8/8 SVG sha256 相同
- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- Light-box overflow re-scan (`box-overflow-scan.py`): **0 true overflows**
  （8 页全扫；仅剩 3 处 0.29–0.92px 量测噪声，首轮已裁定）
- P8 extract (`tools/p8.py extract --total 150`): **150/150**
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成葡萄牙语，预期值）
- 150 键逐题复核：noted set 150/150 一致，键差异仅 [137, 138, 139, 140]
- 文字层：print/web pdftotext **逐字节一致**，46,969 B
- P8 最小字号（PyMuPDF）：**9.975pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×
- 8 版目视：从印刷 PDF 重渲逐版看过；P1 数字框标题、P2 词框、P7 框架框
  标题三处修复均 2× 裁图确认入框；P8 答案区干净

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- 待办：无。
