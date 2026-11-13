# EDITION-RECORD — 2026-w47-ja-nl

- Slug: `2026-w47-ja-nl` · Target: Japanese · Reader: Dutch · VOL.4
- Status (fix round 1, 2026-11-11): **返修完成，门禁全绿，待第二轮全量复校**（协调员另派；本轮不做复校）。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-nl/`

## Deliverables (measured 2026-11-11, fix round 1)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-NL.pdf` | 29,099,141 | `c8b82a8491a0d4c54a01214806cede29188e8f4bf6c81c6cf8a1b3bd5ceafa56` |
| Web PDF `Lucerna-VOL4-JA-NL-web.pdf` | 4,476,527 | `7a7f5fc96730e82ba8c6697a9accd10387d6aa84a731f81fe3083310df0f97b8` |
| `2026-w47-ja-nl.text.md` | 45,627 | — |
| `ABSTRACT.txt` | 301 | — |
| `WEEKLY-KIT.md` | 16,317 | — |

Pre-fix values: print PDF 29,099,171 bytes
`c18c551af2249561000dd50821d4e9646597c5a2cdccf316b02ee38128d40a19`;
web PDF 4,476,557 bytes
`e0678a4b892ff07080d48a51b2f8b7c9ee109916752df537849000370ad9cb81`;
text.md 45,685 bytes. SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。

## Gates (fix round 1 re-run, 2026-11-11)

- run.py exit 0, zero FLOW OVERFLOW / HEAD TOO WIDE; TOTAL 150 （A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38）
- Freeze: 两轮构建 8 SVG **8/8 字节一致**；相对修前仅 p2/p8 变化
- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- P8 extract (`tools/p8.py extract --total 150`): **150/150**；150 键与复校一轮 extract 逐键一致
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成荷兰语，预期值，未变）
- 文字层：print/web pdftotext **逐字节一致**，45,931 B
- P8 最小字号（PyMuPDF）：**9.98pt**（修前 9.975pt，同值仅舍入不同），次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**
- 旧拼全扫：`Fujiryūga` / `Umi-no-umi` 在 content*.py + svg/ + text.md 均为 **0**；P8 SVG 新拼 `Fujiryōga` ×5、`Chura-no-umi` ×1；双 PDF 文字层旧拼 0
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×
- 目视：P2 词条区 200 dpi 放大——四格释义均单行在框内；P8 答案区 200 dpi 放大——注 48/49/54/63/111/116 已改，47 Yoshinofuji 未动；P2/P8 全页已读

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- Fix round 1（2026-11-11）：修 proof1 (b) D1/D2/D3——D1 P2 两条荷兰语释义缩短至一行（`een bamboe hark voor voorspoed` / `wanneer er een beetje sneeuw valt`，词框高未动；P8 答案注同释义同步缩短）；D2 注 49/54/63/111/116 `Fujiryūga`→`Fujiryōga`；D3 注 48 `Umi-no-umi`→`Chura-no-umi`。详情见 KIT §11 F3 与 `scratch-fix-ja-nl1/FIX-LOG.md`。
- 待办：第二轮全量复校（协调员另派）。
