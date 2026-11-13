# EDITION-RECORD — 2026-w47-ja-it

- Slug: `2026-w47-ja-it` · Target: Japanese · Reader: Italian · VOL.4
- Status (stick 8, 2026-11-11): **完成，已核实** — 交付物齐全，门禁全绿。
- Status (fix-1, 2026-11-11): **返修完成，待第二轮全量复校** — 第一轮 (a) 因 P8 注文罗马字拼错作废（见 KIT §11 F4）；本版未入仓，仍为本地件。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-it/`

## Deliverables (measured 2026-11-11, fix-1 rebuild)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-IT.pdf` | 29,099,163 | `8ed65a83d1795577f7ca83f47009f917af18c23adcd7cb1b0b335d86d690f15c` |
| Web PDF `Lucerna-VOL4-JA-IT-web.pdf` | 4,476,985 | `d8af211a19b8a216d4bdba9048ca47a56d4fd628346b4c5dd63741306825805a` |
| `2026-w47-ja-it.text.md` | 46,678 | — |
| `ABSTRACT.txt` | 299 | — |
| `WEEKLY-KIT.md` | — | — |

Pre-fix (stick 8): print 29,099,162 / `75986cd7e7b0acc6e3d4887ccb023c577f3612c9a242c3093060cb7f2af200fd`, web 4,476,984 / `b3ea6d183dea6a1c5b64f5ff1a42807462a0f259fc37fea3668f7a239fc353f0`, text.md 46,676. SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。

## Gates (fix-1 re-run, 2026-11-11)

- Build (`tools/venv/bin/python run.py` ×2): **rc 0, 0 overflow**；freeze runA vs runB **8/8 SVG 相同**；与修前比仅 `p8-tesuto.svg` 变化
- Render (`render.py` ×1): **rc 0**，print PDF 29,099,163 B；webpdf **rc 0**（首跑 rc=120 失败见 FIX-LOG，系磁盘配额，清空后重跑通过），web PDF 4,476,985 B
- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- P8 extract (`tools/p8.py extract --total 150`): **150/150**；keys 与修前逐字节相同（答案键未动）
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成意大利语，预期值）
- 文字层：print/web pdftotext **逐字节一致**，47,002 B
- P8 最小字号（PyMuPDF）：**9.975pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×
- 150 键逐题复核：全读新版 text.md P8 答案区，键全对；6 处改动只改注文罗马字，键值未变；其余人名罗马字逐一复核全对
- 8 版目视：cards 全看，重点 P8 答案区 6 处新拼写均已印出，无溢出/重叠/压页脚；web PDF P8 渲染与 print 卡一致

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- Fix-1（2026-11-11）：修 P8 注文力士名罗马字 6 处——`Fujiryūga`→`Fujiryōga`（keys 49/54/63/111/116）、`Umi-no-umi`→`Chura-no-umi`（key 48）。详见 KIT §11 F4 与 `hidden_files/w47/scratch-ja-it-fix1/` 下 FIX-LOG.md / GATE-LOG.md。
- 待办：第二轮全量复校（协调员派）。
