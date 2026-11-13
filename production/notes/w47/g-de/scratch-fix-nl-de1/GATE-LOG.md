# GATE-LOG — W47 nl-de fix1 (D12) 自验门禁

- 版：`production/2026-w47/2026-w47-nl-de/`；对照核心：`production/2026-w47/core-nl/`（fix5）。
- 工具：仓库 `tools/venv/bin/python` + 共享工具 `occlusion_audit.py` / `p8.py` / `freeze.py` /
  `webpdf.py`；门禁脚本为 proof-delta 版 `gates.py` 的拷贝（输出 JSON 落在本 scratch，
  `gates-de.json`），另加三源比对 `p8compare_fix.py`（proof-delta `p8compare.py` 改路径版）。
- 全部日志、JSON、裁图均在本 scratch（`scratch-fix-nl-de1/`）。

## 门禁逐项实测值

| # | 门 | 命令 / 来源 | 实测值 | 结论 |
|---|---|---|---|---|
| 1 | `run.py` 重建 | `run.py` → `run.log` | rc=0；TOTAL 150；A2 46 / B1 73 / B2 31；分页 10/18/18/18/18/18/12/38；0 FLOW OVERFLOW / HEAD TOO WIDE | PASS |
| 2 | 几何遮挡真实审计 | `tools/occlusion_audit.py svg/`（gates.py 门 1） | rc=0，0 flags（自检通过，见 `gates.log`） | PASS |
| 3 | P8 extract | `tools/p8.py extract --p8 svg/p8-toets.svg --total 150`（gates 门 2 + `p8-extract.log`） | noted=150/150 | PASS |
| 4 | P8 compare（core vs 本版） | `tools/p8.py compare --core-p8 core-nl/svg/p8-toets.svg --edition-p8 … --total 150`（`p8-compare.log`） | rc=0，verdict=CLEAN，missing=[]，extra_count=0，uncertain=[]，**keydiff=[137,138]** | PASS |
| 5 | freeze baseline（核心） | `tools/freeze.py baseline --build <core-nl> --core-svg <core-nl>/svg --out <scratch>/freeze-baseline`（`freeze-baseline.log`） | rc=0，**8/8 SVGs byte-identical**；shipped core SVGs unchanged（8 files re-hashed） | PASS |
| 6 | 版内自比对 | gates 门 4（clean repro 重跑 run.py，逐页 sha256 比对） | run rc=0，match=**8/8** | PASS |
| 7 | 印/网文字层逐页一致 | gates 门 5（PyMuPDF 位置排序逐页） | 8/8 页，posdiff=0，msdiff=0；P1 832/832，P2 813/813，P3 719/719，P4 720/720，P5 795/795，P6 729/729，P7 890/890，**P8 2257/2257** | PASS |
| 8 | pdftotext 非空且一致 | gates 门 6 | print=46,746 B，web=46,746 B，web_size=1,617,817 | PASS |
| 9 | P8 最小字号（SOP §1.1 下限 9.75pt） | gates 门 7（PyMuPDF 答案区） | min=**10.12pt**，median=10.12pt，spans=187 | PASS |
| 10 | P8 级别徽章 vs 核心 | gates 门 8 | core={A2:8, B1:24, B2:3}，edition 相同 | PASS |
| 11 | §1.1 SVG 审计 | gates 门 9 | off-palette={}，gold/old=False，stroked_rects=0，VOL.5=5（core 5），paper_fills=8 | PASS |
| 12 | 150 键三源复核 | `p8compare_fix.py`（registry-new.json + text.md + p8-extract.json）→ `p8-compare-3way.json` / `p8compare-3way.log` | **3-way MATCH 149/149**（Q150 开放写作例外）；DIFF=[]，MISSING=[]；Q140 三源逐字一致；配对键 25–28 / 141–144 未动 | PASS |
| 13 | D12 专项：题干含 kurzen | p8 SVG（stem y=528.04，label 140. y=505.24）+ 印/网 P8 pdftotext 136 行 + text.md:415 | 三处均含 `Ich mache eine Surprise mit einem kurzen Gedicht.`；旧句 `einem Gedicht`（无 kurzen）全文 0 处 | PASS |
| 14 | D12 专项：key 不动 | registry Q140（`dump_reg.log`） | `key = "Ik maak een surprise met een kort gedicht."`，note 不变 | PASS |
| 15 | SVG 变化清单 | `svg-sha-delivered.txt` vs `svg-sha-rebuilt.txt`（diff 仅 p8 一行） | 仅 p8 变化（`c065d94787d2…` → `83c3cc7aa0a5…`）；p1–p7 字节不变 | PASS |
| 16 | 文字层 P8 渲染目检 | `render-p8.png`（975×1350）裁图 `crop-p8-q140-stem.png` / `crop-p8-q140-key.png` | 题干 `…mit einem kurzen Gedicht. → ___` 单行在栏内、无溢出；答案区 `140. Ik maak een surprise met een kort gedicht. — surprise ist eine feste Wendung` 清晰 | PASS |

`s11` 门（gates 门 9 映射）与 proof1 一致。`gates.py` 总体：`OVERALL: ALL PASS`，rc=0
（见 `gates.log`；JSON `gates-de.json`）。

## 回归确认（未动项）

- D11（p4）：p4 SVG 字节与交付一致，盒内余量 +20.11px 未动。
- D6/D7/D8/D10（p3/p6/p7）：对应 SVG 字节与交付一致，w 机制与值均在位。
- 其余文字/图/版式：仅 p8 一个 SVG 有变化，其余 7 页 sha256 全同。
- 核心对照未碰：freeze baseline 8/8 且 core SVG 完整性复核通过（run 前后重哈希无变化）。

## 交付物

- 本 scratch：`FIX-LOG.md`（本文件之外的修法与 SHA 记录）、`GATE-LOG.md`（本文件）、
  `run.log` / `render.log` / `webpdf.log` / `export.log` / `gates.log` / `gates-de.json` /
  `freeze-baseline.log` / `p8-compare.log` / `p8-compare-3way.json` / `p8-extract.json` /
  `registry-new.json` / `svg-sha-delivered.txt` / `svg-sha-rebuilt.txt` /
  `textmd-delivered.md` / `new-sha.txt` / `render-p8.png` / `crop-p8-q140-stem.png` /
  `crop-p8-q140-key.png`。
- 版目录内改动（未 commit）：`content8.py`（1 行）、`svg/p8-toets.svg`、
  `De-Lucerna-VOL4-nl-de.pdf`、`De-Lucerna-VOL4-nl-de-web.pdf`、
  `2026-w47-nl-de.text.md`（仅 415 行一词）、`cards/*.png`（render 缓存）。
