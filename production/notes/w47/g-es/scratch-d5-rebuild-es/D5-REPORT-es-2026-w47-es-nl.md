# D5 重建报告 — 2026-w47-es-nl

日期：2026-11-12（UTC ~08:14–08:26）。构建解释器全程 `tools/venv/bin/python`。

## 安装
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader nl`（mode latin）。
- `svglib.py` md5 `48c31801…` → `da6d8aa3…`；路由断言 10/10；fix2 保留。
- 修前基线：印 3,502,211 B `67656a0d…`、网 888,054 B `c70a310a…`；D5 普查 497 拉丁在 CJK Sans；boxtitle 0 DEFECT；occlusion 0。

## 预修（与 core-es 相同的 3 项共用版式）
P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐项修（D5 新缺陷）
- P1 框题 `LA SEMANA EN CIFRAS　De cijfers` +13.5px → 该框 `tsize=21`。
- P1 手工题 `EN ESTA EDICIÓN　In dit nummer` +21.7px → 24→22pt。
- P5 框题 `EL PLAN DE LA SEMANA　Weekplan` +34.7px → 该框 `tsize=20`。以上文字均未动。

## 门禁（最终版全绿）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；head_check PASS 0 defects；render rc=0。
- D5 普查 0；U+201C 普查 0。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（仅读者语译注）。
- boxtitle 0 DEFECT；creambox（tools 版）PASS 0 defects（P8 249 行、余量 36.4px 不变）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 1 个（仅 U+3000）。
- 印/网文字层 44,571 字符、8,373 词，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-nl.pdf` 2,915,319 B，SHA-256 `7f7e902290987298f091ea9231eb7327b9ba980cfcf867c07e932e3a0c86ec10`。
- 网页版 `La-Lucerna-VOL4-es-nl-web.pdf` 805,821 B，SHA-256 `7d69a9df24051300dedbc69eee44595495c7bea0eefec50b9277e20fd337bef1`。
- `text.md` 字节不变（SHA `d8d8e007…`）。
- KIT 已更新（§8 交付行 + 尾部 D5 记录）。日志在本目录；freeze build-copy 已删。
