# D5 重建报告 — 2026-w47-es-de

日期：2026-11-12（UTC ~07:39–07:45）。构建解释器全程 `tools/venv/bin/python`。

## 安装
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader de`（mode latin）。
- `svglib.py` md5 `48c31801…` → `da6d8aa3…`；路由断言 10/10；fix2 保留。
- 修前基线：印 3,503,173 B `f47f4ea9…`、网 889,964 B `31d479c8…`；D5 普查 496 拉丁在 CJK Sans；boxtitle 0 DEFECT；occlusion 0。

## 预修（与 core-es 相同的 3 项共用版式）
P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐项修（D5 新缺陷）
- P1 框题 `LA SEMANA EN CIFRAS　ZAHLEN` +13.5px → 该框 `tsize=21`。
- P5 框题 `EL PLAN DE LA SEMANA　Der Plan` +19.7px → 该框 `tsize=21`。
- P7 手工题 `LA PALABRA　WORT DER WOCHE` +19.5px → 字号 23→21pt。以上文字均未动。

## 门禁（最终版全绿）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；render rc=0。
- D5 普查 0；弯引号在 CJK Sans 0。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（仅读者语译注）。
- boxtitle 0 DEFECT（1 marginal，容差内）；creambox PASS 0 defects（P8 247 行、余量 36.4px 不变）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 1 个（仅 U+3000，run 拆分 artifact）。
- 印/网文字层 44,553 字符、8,178 词，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-de.pdf` 2,916,396 B，SHA-256 `86db55fa894be629e93ae1415c02ad85508efdbaa5b8f8805a51d7a25e25facb`。
- 网页版 `La-Lucerna-VOL4-es-de-web.pdf` 806,903 B，SHA-256 `052cf044d65a10ff92aed5ab625f3c80dd664540e45c66c805975bbf6721cbf2`。
- `text.md` 字节不变（SHA `81ff0656…`）。
- KIT 已更新（PDF 行 + 尾部 D5 记录）。日志在本目录；freeze build-copy 已删。
