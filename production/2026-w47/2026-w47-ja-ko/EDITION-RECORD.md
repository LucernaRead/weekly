# EDITION-RECORD — 2026-w47-ja-ko

- Slug: `2026-w47-ja-ko` · Target: Japanese · Reader: Korean · VOL.4
- Status (fix1, 2026-11-11): **返修完成，待第二轮全量复校（proof2）** — proof1 的 3 条缺陷
  （D1/D2/D3）已修，另附带修好 map 第 221 键错字致 #47 漏译；全套门禁逐项重跑，零问题。
  （此前状态 stick 8, 2026-11-11：完成，第 8 棒独立审计通过。）
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-ko/`

## Deliverables (measured 2026-11-11, fix1)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-KO.pdf` | 28,189,450 | `8c6b7566e6efe7d94beae5bf10b6382970a93b3b71708688d3d27dbb7f39f177` |
| Web PDF `Lucerna-VOL4-JA-KO-web.pdf` | 4,550,444 | `133f57264a824575af7336c6e1198c4992211fa45bf8c82d96dfd89e840f3368` |
| `2026-w47-ja-ko.text.md` | 47,722 | — |
| `ABSTRACT.txt` | 296 | — |
| `WEEKLY-KIT.md` | 12,408 | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。
（旧值 proof1：print 28,189,461 B `fbcfe840…`、web 4,550,459 B `d52edd4e…`、text.md 47,721 B。）

## Gates (fix1 full re-run, evidence in hidden_files/w47/scratch-fix-ja-ko1/, *fix1.*)

- run.py (`tools/venv/bin/python`，与构建同一解释器）：exit 0，**TOTAL 150**（A2 48 / B1 73 / B2 29；按页 10/18/18/18/18/18/12/38），**0 FLOW OVERFLOW / HEAD TOO WIDE**（`build-ko-fix1-run1.log`；run2 为冻结重跑，`build-ko-fix1-run2.log`）
- Freeze：run.py 连跑两遍，8 SVG sha256 **8/8 逐字节一致**（`ko-sha-fix1-run1.txt` vs `ko-sha-fix1-run2.txt`）；与 proof1 交付 SVG 比，仅 p5（D3）与 p8（D1/D2/#47）两页变化，其余六页逐字节一致
- Occlusion audit (`tools/occlusion_audit.py`, selftest OK，6 类全触发阳性对照）：**0 flags**（`ko-occlusion-fix1.json`）
- P8 extract (`tools/p8.py extract --total 150`): **150/150**（`ko-p8-fix1.json`）
- P8 compare vs core P8 SVG: **CLEAN**，missing=[] extra=0 uncertain=[]，keydiff=**[137, 138, 139, 140]**——恰为预期（E 组 4 个中文句答案键译成韩语；其余 146 键与核心逐字节一致）（`ko-p8compare-fix1.json`）
- 文字层：print/web pdftotext **逐字节一致**，47,998 B（plain）；layout 91,550 B 逐字节一致
- P8 最小字号（PyMuPDF）：**9.975pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**；简体残留：`吉伊卡哇` 0×、`参考答案` 0×、`酉之市` 0×、`提名` 0×；`치이카와` / `ryuuryuu` 如裁定；`후지류가` 0×（`후지료가` P8 SVG 5 处 + text.md 5 处）、`기하라 류치` 0×（`기하라 류이치` 1 处）、#47 中文原文 0×
- §1.1 grep：纸色 `#fbfaf6` 1×/页，旧纸 `#f7f1e2` 0×，`·` 0×，页脚 `제 N 면 / 총 8 면` 8×
- 8 版目视（cards/ p1–p8）：干净，无溢出/重叠/压页脚/豆腐块。P7 披露 4 行韩语、teaser 未压页脚；P8 E 组题干与答案 137–140 韩语无误；P1 趋势盒第 1 条末尾单字「敗」换行是核心冻结正文的原有换行，非 fan-out 缺陷；P2/P4 栏中空白为短专栏留白（W46 已披露模式）。P5「あなたは？」框韩语提示已为 2 行、句号贴回行尾（D3 已修，目视确认）；P8 #47/#49/#54/#63/#80/#111/#116 皆为修正后韩文（目视确认）

## Notes

- 任务交代称“第 6 棒是否做了全套自查未知”——盘上 KIT §7–§8 已记全套自查，第 8 棒又逐项重跑，全部复现，无需补做。
- KIT 所记 P7 teaser ends 2443.58 / P8 keys ends y=2366 未用原测量脚本重测（该脚本随旧 scratch 目录丢失）；几何审计 0 旗 + 8 版目视为证。
- fix1 说明：apply.py 会清空版目录重拷，本文件与 WEEKLY-KIT.md 在 fix1 重 apply 时被清，已按开工时读到的原文逐字重建（只更新本节数值与状态）；proof2/协调员复核时请以 `hidden_files/w47/scratch-fix-ja-ko1/FIX-LOG.md` 为据再验。KIT 文件字节数由 10,695 变为 12,408，系 §8 更新 + §11 追加 F2 记录所致。
- 待办：第二轮全量复校（proof2），零问题方可定稿。
