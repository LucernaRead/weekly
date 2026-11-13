# EDITION-RECORD — 2026-w47-ja-es

- Slug: `2026-w47-ja-es` · Target: Japanese · Reader: Spanish · VOL.4
- Status (stick 8, 2026-11-11): **完成，已核实** — 交付物齐全，门禁全绿。
- Status (fix-1, 2026-11-11): **D1 已修并重验** — 第一轮复校缺陷 D1（P8 注文 6 处相扑力士罗马字）已改源码并整期重渲染，全套机械门重跑全绿，150 键逐题复核仅 6 处注文变化。待第二轮全量复校（协调员派）。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-es/`

## Deliverables (measured 2026-11-11, stick 8)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-ES.pdf` | 29,102,102 | `9947b70c00a378c912ad7cffd198fd19a234ca3d6a3598589f647c3eaff0fce7` |
| Web PDF `Lucerna-VOL4-JA-ES-web.pdf` | 4,482,721 | `49665374de81dd2a2ee7dad1b91396b22b69b2e64f5a038d55f03b5246a99550` |
| `2026-w47-ja-es.text.md` | 46,684 | — |
| `ABSTRACT.txt` | 308 | — |
| `WEEKLY-KIT.md` | 11,760 | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。

## Gates (stick 8 re-run)

- Occlusion audit (`tools/occlusion_audit.py`, selftest OK): **0 flags**
- P8 extract (`tools/p8.py extract --total 150`): **150/150**
- P8 compare vs core P8 SVG: **CLEAN**, missing=[] extra=0 uncertain=[], keydiff=[137, 138, 139, 140]（E 组 4 个中文句答案键译成西班牙语，预期值）
- 文字层：print/web pdftotext **逐字节一致**，47,036 B（fix-1 重测；原 47,034 B）
- P8 最小字号（PyMuPDF）：**9.975pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**
- §1.1 grep：纸色 `#fbfaf6` 8×（1×/页），旧纸 `#f7f1e2` 0×，`·` 0×

## Fix-1 (D1, 2026-11-11)

- 改动：`content34.py:188/190/202/224`、`content7.py:57`、`content8.py:22` 共 6 条 P8 答案注文：
  `Umi-no-umi` → `Chura-no-umi`（key 48）、`Fujiryūga` → `Fujiryōga`（keys 49/54/63/111/116）。
  键值与题面汉字未动。整期重渲染（runA/runB 8/8 freeze）+ web PDF + text.md 重导；
  机械门全绿（occlusion 0、p8 extract 150/150、compare CLEAN keydiff=[137,138,139,140]）；
  新旧 P8 注文逐行 diff 仅此 6 行；8 版目视通过（重点 P8 答案区，另见 FIX-LOG.md）。
- 上游提示：同错见于 core-ja KIT §3（L83–88）及 de/en/fr/it/nl/pt 六个同家拉丁版，ko/ru/zh-tw 不受影响；
  本任务只修 ja-es，其余只报告、不碰。

## Notes

- 前棒（第 7 棒）审计已通过；第 8 棒独立重跑上述机械门，全部复现。
- 待办：无。
