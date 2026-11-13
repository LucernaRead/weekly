# D5 重建报告 — 2026-w47-es-en

日期：2026-11-12（UTC ~07:30–07:40）。构建解释器全程 `tools/venv/bin/python`。

## 安装
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader en`（mode latin）。
- `svglib.py` md5 `48c31801…` → `da6d8aa3…`（与 core-es D5 后一致）；路由断言 10/10；fix2 保留。
- 修前基线（`pre-record.txt`）：印 3,500,997 B `b7f7931f…`、网 886,824 B `f1221df3…`；D5 普查 494 拉丁在 CJK Sans；boxtitle 0 DEFECT；occlusion 0。

## 预修（与 core-es 相同的 3 项共用版式）
P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐项修（D5 新缺陷）
- P1 框题 `LA SEMANA EN CIFRAS　Numbers` +10.5px → 该框 `tsize=21`（文字未动）。
- P5 框题 `EL PLAN DE LA SEMANA　The plan` +20.7px → 该框 `tsize=21`（文字未动）。

## 门禁（最终版全绿）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；render rc=0。
- D5 普查 0；弯引号在 CJK Sans 0（6 个全在 Newsreader）。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（仅读者语译注：同义答案中文→英文）。
- boxtitle 0 DEFECT；creambox PASS 0 defects（P8 197 行、余量 39.9px 不变；P1 120→122 行系 D5 重排）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 0。
- 印/网文字层 44,302 字符、8,430 词，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-en.pdf` 2,915,634 B，SHA-256 `3ece32511f03d5483b2a8fb20cc1bca664513dc9af2d95b60ff847024848e11e`。
- 网页版 `La-Lucerna-VOL4-es-en-web.pdf` 806,132 B，SHA-256 `23a06fabd738cc15d052d17a9302903200389da9376a5db3be197109a7bf9033`。
- `text.md` 字节不变（SHA `6080c94c…`）。
- KIT 已更新（PDF 行 + 尾部 D5 记录）。日志在本目录（run-d5b/render-d5b/census-d5b/occlusion-d5b/p8-*-d5b/boxtitle-d5b/creambox-d5/spill-d5b/edge-d5b/textlayer-d5b/freeze-baseline-d5b/freeze-diff-d5b）；freeze build-copy 已删。
