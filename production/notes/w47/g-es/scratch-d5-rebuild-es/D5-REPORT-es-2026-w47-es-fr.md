# D5 重建报告 — 2026-w47-es-fr

日期：2026-11-12（UTC ~07:45–07:55）。构建解释器全程 `tools/venv/bin/python`。

## 安装
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader fr`（mode latin）。
- 修前 `svglib.py` md5 `6a46ee51…`（尚未移植 fix2——本版修前普查 curly_total=0，无弯引号字形）；安装时一并补入 fix2 块，装后 md5 `63c75f38…`；路由断言 10/10。
- 修前基线：印 3,500,186 B `688152c7…`、网 884,215 B `9d4bca4a…`；D5 普查 497 拉丁在 CJK Sans；boxtitle 0 DEFECT；occlusion 0。

## 预修（与 core-es 相同的 3 项共用版式）
P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐项修（D5 新缺陷）
- P1 手工题 `EN ESTA EDICIÓN　SOMMAIRE` +2.7px → 24→23pt。
- P2 框题 `EL CALENDARIO　LE CALENDRIER` +28.4px → 该框 `tsize=21`。
- P5 框题 `EL PLAN DE LA SEMANA　LE PLAN` +28.7px → 该框 `tsize=21`。
- P7 手工题 `LA PALABRA　MOT DE LA SEMAINE` +46.5px → 23→19pt。以上文字均未动。

## 门禁（最终版全绿）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；render rc=0。
- D5 普查 0；弯引号在 CJK Sans 0（本版无弯引号）。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（仅读者语译注）。
- boxtitle 0 DEFECT；creambox PASS 0 defects（P8 243 行、余量 38.9px 不变）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 1 个（仅 U+3000）。
- 印/网文字层 44,873 字符、8,471 词，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-fr.pdf` 2,914,976 B，SHA-256 `671c8c129839aef684ae57c0fba19aecc3794e316ca71eb20e881f3ed484addc`。
- 网页版 `La-Lucerna-VOL4-es-fr-web.pdf` 805,449 B，SHA-256 `a7a0b7025d03599d48152f423854513ebc9972cb50c3f097529c971e454ece14`。
- `text.md` 字节不变（SHA `ae1c3f3b…`）。
- KIT 已更新（PDF 行 + 尾部 D5 记录）。日志在本目录；freeze build-copy 已删。
