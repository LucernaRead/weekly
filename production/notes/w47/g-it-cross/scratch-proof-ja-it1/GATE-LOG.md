# GATE-LOG — 2026-W47 ja-it 第一轮独立复校（叶子）

全部机械门均为本轮独立重跑（tools/venv/bin/python：Python 3.12.3，Pillow 13.0.0），
输出存本目录。构建解释器确认：共享 venv 重建与 shipped SVG 8/8 字节一致，
与构建所用解释器一致（ko 家庭 Pillow 版本差问题不适用；系统 python3 的 Pillow 为 10.2.0，未采用）。

## 1. 身份

- print `Lucerna-VOL4-JA-IT.pdf`：29,099,162 字节；SHA-256
  `75986cd7e7b0acc6e3d4887ccb023c577f3612c9a242c3093060cb7f2af200fd`；8 页；1462.5×2025 pt。
- web `Lucerna-VOL4-JA-IT-web.pdf`：4,476,984 字节；SHA-256
  `b3ea6d183dea6a1c5b64f5ff1a42807462a0f259fc37fea3668f7a239fc353f0`；8 页。
- 与 KIT 登记的字节数与 SHA（全串）逐字一致。

## 2. run.py 重跑（scratch 副本，不碰成品目录）

- `run.py` exit 0；`FLOW OVERFLOW` 0 行；`HEAD TOO WIDE` 0 行。
- TOTAL 150；by level {A2: 48, B1: 73, B2: 29}；
  by page {1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}；
  by type {completamento: 50, scelta multipla: 51, abbinamento: 12,
  costruzione di frasi: 8, vero o falso: 11, cloze: 13, traduzione: 4, Scrittura: 1}；
  model chars: 154。日志：`it-runpy.log`。

## 3. Freeze（直接 sha256，8/8）

- `tools/freeze.py baseline`：8/8 SVGs byte-identical，exit 0；
  shipped SVG 建前/建后重哈希，未被改动。日志：`it-freeze.log`。
  shipped SHA：见 `shipped-sha.txt`（p1 654e03c4…、p2 4a29d9f1…、p3 6bdb2aae…、p4 d1d67c5c…、
  p5 0ea9121e…、p6 9f565406…、p7 aab13386…、p8 9509da3e…，全串在文件中）。
- 独立第二次重跑（`rerun/`）：8/8 MATCH。
- `tools/freeze.py diff --core-svg core-ja/svg --strict-cjk`：exit 1，
  净增 CJK 15 字（U+3000 9、ト/ー/ノ/ミ/ネ/楽 各 1）。已逐字裁定为误报实质，
  见 PROOF-NOTE O2；非严格模式下增/减串均为中→意家具替换。日志：`it-freediff.log`，
  明细：`it-freediff.json`，裁定脚本：`show_diff.py`、`cjknet.py`、`textnodes.py`、`simp_scan.py`。

## 4. Occlusion 几何审计

- `tools/occlusion_audit.py`：selftest OK（6 类 BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX
  阳性对照全触发，干净对照静默）；本版 0 flags，exit 0。
  输出：`it-occlusion.json`，日志：`it-occlusion.log`。

## 5. P8

- `tools/p8.py extract --total 150`：noted set 150/150。输出：`it-p8.json`。
- `tools/p8.py compare`（core-ja/svg/p8-tesuto.svg 对照）：status CLEAN，
  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140]，exit 0。
  四条 keydiff 已逐条核对原文（core 中文键 vs 本版意大利文键，均为 E 组翻译答案的意译）。
  输出：`it-p8compare.json`，日志：`it-p8compare.log`。

## 6. U+2019 回归

- 8 个 SVG 中 U+2019 总数 0（逐文件 grep 均为 0）；U+0027 撇号 29 处，目视窄字形无断裂。

## 7. 文字层一致

- `pdftotext`（无 layout）：print 与 web 各 47,000 字节，字节全同。
- `pdftotext -layout`：各 106,304 字节，`cmp` 通过（TEXT_IDENTICAL）。

## 8. P8 字号（PyMuPDF，print PDF p.8）

- 最小字号 9.98pt（≥9.75pt）；次档 10.35pt（79 个跨度，日语题干）；其余 10.88/11.25/11.62/12.75/13.5/14.25/14.62/15.38/15.75/17.25/18.0/18.75/34.5pt。

## 9. §1.1 grep 审计（shipped SVG）

- 纸色 #fbfaf6 每页 1 次；旧 #f7f1e2 0 次；禁用金/砖红 0 次；「·」0 次；
  刊头 font-size 196（P1）1 次；`Pagina N di 8` 每页 1 次；
  徽章色 A2 #5c6e30 / B1 #46581f / B2 #37402f 均在。

## 10. 目视

- 印刷 PDF 重新渲染（pdftoppm 90dpi，`render/print-p-{1..8}.png`）逐版目视；
  网页 PDF P1/P8（`render/web-p1-1.png`、`render/web-p8-8.png`）目视；
  与核心版对照渲染（`render/core-p-*.png`，P2/P3/P4/P5/P7/P8）核对继承项。
  结论：无溢出/重叠/压页脚/tofu；网页版与印刷版视觉一致。

## 备注

- 任务引用的 builder 审计件（FANOUT-REPORT-ja.md、map-it.json、builder 版 it-*.json、
  build-it-run*.log）在工作树中不存在（见 PROOF-NOTE O1），故本轮全部机械门独立重跑，
  未采信 builder 的门结果。
- 本轮未改动任何源码/成品；未跑 insert.py、lint --write；无 git add/commit/push/reset/stash；
  未碰 core-ja、W43–W46、其他目标语家庭、tools/（tools 仅作只读调用）。
