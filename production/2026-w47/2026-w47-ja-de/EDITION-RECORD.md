# EDITION-RECORD — 2026-w47-ja-de

- Slug: `2026-w47-ja-de` · Target: Japanese · Reader: German · VOL.4
- Status (fix round 1, 2026-11-11): **第一轮返修完成，待第二轮全量复校** — D1/D2/D3 已修，整期重渲染，全套机械门全绿，8 版目视通过。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-de/`

## Deliverables (measured 2026-11-11, fix round 1 — re-measured, supersedes stick 8)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | p7 `3493886b3c75364682e2b630b821399750d12344b8e40989654757fa6c4bc505`, p8 `021ed40fe1098cc68805757cdd4bac08445771a84b731c34f04c4df382003cb5` (p1–p6 unchanged) |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-DE.pdf` | 29,102,625 | `2047035bdaa9f9ba82d4f2a6d2b5d7c4461e1442070ed5abacbe86d930001f39` |
| Web PDF `Lucerna-VOL4-JA-DE-web.pdf` | 4,483,728 | `8db59bf122c73d895e9fe0d58da7e9f283f11ed1e76bc45aeb2be9a268a98f26` |
| `2026-w47-ja-de.text.md` | 46,520 | — |
| `ABSTRACT.txt` | 311 | — |
| `WEEKLY-KIT.md` | — | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。旧版（stick 8）：印刷 29,102,629 / `b5d66e17…a239`，网页 4,483,732 / `c55dd68c…f26a`，text.md 46,516。

## Gates (fix round 1 re-run, 2026-11-11 — all green)

- run.py ×2 (`tools/venv/bin/python`, Pillow 13.0.0): exit 0，零溢出；freeze 8/8 字节一致；TOTAL 150（A2 48 / B1 73 / B2 29）
- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- P8 extract (`tools/p8.py extract --total 150`): **150/150**
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成德语，预期值）
- 150 键逐题复核：仅 keys 48/49/54/63/111/116 简析变化，键值零差异
- 文字层：print/web pdftotext **逐字节一致**，105,192 B
- P8 最小字号（PyMuPDF）：**9.98pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG 全扫 **0**
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×
- 8 版目视（新印刷 PDF 100 dpi 重渲染）：全部干净，P7 诊所第 4 条与 P8 六处已放大确认

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- 第一轮返修（D1/D2/D3，2026-11-11）：`content34.py` ×4、`content7.py` ×2、`content8.py` ×1，text.md 同步 7 行；详见 WEEKLY-KIT §11 F4 与 FIX-LOG.md。
- 待办：第二轮全量复校（协调员另派）。
