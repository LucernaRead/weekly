# D5 重建报告 — 2026-w47-es-it

日期：2026-11-12（UTC ~07:55–08:00）。构建解释器全程 `tools/venv/bin/python`。

## 安装
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader it`（mode latin）。
- 修前 `svglib.py` md5 `6a46ee51…`（尚未移植 fix2）；安装时一并补入 fix2 块，装后 md5 `63c75f38…`；路由断言 10/10。
- 修前基线：印 3,498,553 B `12e7e081…`、网 882,083 B `e4e14eb1…`；D5 普查 491 拉丁在 CJK Sans；boxtitle 0 DEFECT；occlusion 0。

## 预修（与 core-es 相同的 3 项共用版式）
P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐项修（D5 新缺陷）
- P1 框题 `LA SEMANA EN CIFRAS　IN CIFRE` +17.5px → 该框 `tsize=21`。
- P1 手工题 `EN ESTA EDICIÓN　IL NUMERO` +3.7px → 24→23pt。
- P2 框题 `EL CALENDARIO　IL CALENDARIO` +23.4px → 该框 `tsize=21`。
- P5 框题 `EL PLAN DE LA SEMANA　IL PIANO` +32.7px → 该框 `tsize=20`。
- P7 手工题 `ERRORES TÍPICOS　ERRORI TIPICI` +26.7px → 23→20pt。以上文字均未动。

## 门禁（最终版全绿）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；render rc=0。
- D5 普查 0；弯引号在 CJK Sans 0。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（仅读者语译注）。
- boxtitle 0 DEFECT；creambox PASS 0 defects（P8 239 行、余量 38.9px 不变）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 6 个（全为 U+3000）。
- 印/网文字层 44,422 字符、8,319 词，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-it.pdf` 2,913,383 B，SHA-256 `fab568413ff316b99129db7d02e4f40cefed6efdae99eb5ac72830eeb6c15c2c`。
- 网页版 `La-Lucerna-VOL4-es-it-web.pdf` 803,850 B，SHA-256 `437c65b44ca5adc3ce2d6833e36358fa6684feec6e5737b8f46aa883d030f927`。
- `text.md` 字节不变（SHA `434e8df8…`）。
- KIT 已更新（PDF 行 + 尾部 D5 记录）。日志在本目录；freeze build-copy 已删。
