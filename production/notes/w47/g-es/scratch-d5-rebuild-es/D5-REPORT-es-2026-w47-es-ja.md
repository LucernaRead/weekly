# D5 重建报告 — 2026-w47-es-ja

日期：2026-11-12（UTC ~09:00–09:20）。构建解释器全程 `tools/venv/bin/python`。CJK 读者版（裁定 §1：按字符文字分流，不加 `_READER_LANG` 门）。

## 安装
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader ja`（mode=cjk）。
- `svglib.py` md5 `6a46ee51…` → `091da842…`（安装器同时补 port 了 fix2，CJK 索引 SC→JP，kinsoku 块自 core-zh-tw 移植）；路由断言 10/10；机制 `test_d5_routing.py` FAILURES: 0。
- 修前基线（`pre.sh` 新建，因 scratch 原无 CJK 基线目录）：印 17,294,448 B `459d570a…`、网 1,540,820 B `6c6a273d…`；D5 普查 346 violations（与裁定 §1.1 预期 346 一致）；boxtitle 0 DEFECT；occlusion 0。

## 预修（与 core-es 相同的 3 项共用版式）
P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐项修（D5 新缺陷，CJK 类）
- P1 框题 `LA SEMANA EN CIFRAS　今週の数字` +22.5px → 该框 `tsize=21`（21pt advance 389.8，余量 14.7px）。
- P5 框题 `EL PLAN DE LA SEMANA　今週の計画` +36.7px → 该框 `tsize=20`（21pt 余量仅 1.7px，取 20 求稳）。
- P7 手工题 `ERRORES TÍPICOS　よくある間違い` +8.7px → 23→22pt（余量 9.2px）。以上文字均未动。注：ink=advance（尾字为全角 CJK），框题可用宽 404.5px、手工题 400.5px。

## 门禁（最终版全绿）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；head_check PASS 0 defects；render rc=0。
- D5 普查 0；U+201C 普查 0（KR 引号不扩展，裁定 §3）。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（仅读者语译注）。
- boxtitle 0 DEFECT；creambox（tools 版）PASS 0 defects（P8 220 行、余量 36.4px 不变）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8；freeze diff vs core-es 新增 CJK 字符 2,946 个（日语读者层相对 core-es 中文读者层的正当差异）；同版 freeze diff（修前基线 vs 新版）新增 CJK 字符仅 1 个 U+3000。
- 印/网文字层 38,692 字符、6,991 词，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-ja.pdf` 8,530,855 B，SHA-256 `9a5338c3e29eefc4c42adc3c50c39f3acc1c3ab8f7326b52d6940f78beb76422`。
- 网页版 `La-Lucerna-VOL4-es-ja-web.pdf` 1,280,435 B，SHA-256 `5f496c566aa337d3604527f4fe6f13fbae9443e4025e8f2525422b6c8eb08570`。
- `text.md` 字节不变（SHA `74790778…`）。
- KIT 已更新（§1 交付行 + 尾部 D5 记录）。日志在本目录；freeze build-copy 已删。
