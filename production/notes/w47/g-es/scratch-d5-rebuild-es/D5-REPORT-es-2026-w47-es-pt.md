# D5 重建报告 — 2026-w47-es-pt

日期：2026-11-12（UTC ~08:00–08:12）。构建解释器全程 `tools/venv/bin/python`。

## 安装
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader pt`（mode latin）。
- 修前 `svglib.py` md5 `6a46ee51…`（尚未移植 fix2）；安装时一并补入 fix2 块，装后 md5 `63c75f38…`；路由断言 10/10。
- 修前基线：印 3,500,936 B `0c8dd285…`、网 885,043 B `c4d420b7…`；D5 普查 493 拉丁在 CJK Sans；boxtitle 0 DEFECT；occlusion 0。

## 预修（与 core-es 相同的 3 项共用版式）
P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐项修（D5 新缺陷）
- P1 框题 `LA SEMANA EN CIFRAS　Números` +9.5px → 该框 `tsize=21`。
- P5 框题 `EL PLAN DE LA SEMANA　O plano` +9.7px → 该框 `tsize=21`。
- P7 手工题 `ERRORES TÍPICOS　Erros comuns` +2.7px → 23→22pt。
- P7 手工题 `LA PALABRA　A palavra da semana` +11.5px → 23→21pt。以上文字均未动。

## 门禁（最终版全绿）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；head_check PASS 0 defects；render rc=0。
- D5 普查 0；U+201C 普查 0。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（仅读者语译注）。
- boxtitle 0 DEFECT；creambox（tools 版）PASS 0 defects（P8 248 行、余量 36.4px 不变）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 0。
- 印/网文字层 44,640 字符、8,448 词，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-pt.pdf` 2,914,545 B，SHA-256 `8da2a440916ec28cc052b3c6b8f8329f3e14c540823e2c9c375fb04263f14e3e`。
- 网页版 `La-Lucerna-VOL4-es-pt-web.pdf` 805,014 B，SHA-256 `0a23b7d32fcc6c3ecf7b9cabaed9b28bf0e0add0684a9855d0dc7b75d41c6644`。
- `text.md` 字节不变（SHA `9df4d30c…`）。
- KIT 已更新（PDF 行 + 尾部 D5 记录）。日志在本目录；freeze build-copy 已删。
