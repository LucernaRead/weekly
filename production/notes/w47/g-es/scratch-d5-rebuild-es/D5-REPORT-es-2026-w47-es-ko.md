# D5 重建报告 — 2026-w47-es-ko

日期：2026-11-12（UTC ~09:21–09:44）。构建解释器全程 `tools/venv/bin/python`（freeze 亦 venv，未用系统 python3 例外）。CJK 读者版（裁定 §1：按字符文字分流，不加 `_READER_LANG` 门）。

## 安装
- `mechanism/apply_variant.py --svglib <版>/svglib.py --target es --reader ko`（mode=cjk）。
- `svglib.py` md5 `6a46ee51…` → `4010cae9…`（安装器同时补 port 了 fix2，CJK 索引 SC→KR）；路由断言 10/10；机制 `test_d5_routing.py` FAILURES: 0。
- 修前基线（`pre.sh` 新建，因 scratch 原无 CJK 基线目录）：印 8,873,692 B `2c98a0f8…`、网 1,236,854 B `39f6a7e9…`；D5 普查 347 violations（与裁定 §1.1 预期 347 一致）；boxtitle 0 DEFECT；occlusion 0。

## 预修（与 core-es 相同的 3 项共用版式）
P1 栏头 `UNA SEMANA, TRES ESCENARIOS` 25→23pt；P3 栏头 `LO QUE QUEDA DE NOVIEMBRE` 25→24pt；P3 手工题 `EL FLAMENCO, EN TRES DATOS` 24→23pt。

## 逐项修（D5 新缺陷，CJK 类）
- P1 框题 `LA SEMANA EN CIFRAS　이번 주 숫자` +23.7px → 该框 `tsize=21`（余量 13.3px）。
- P5 框题 `EL PLAN DE LA SEMANA　이번 주 계획` +37.9px → 该框 `tsize=20`（21pt 余量仅 0.3px，取 20 求稳）。以上文字均未动。注：ink=advance（尾字为全角 CJK），框题可用宽 404.5px。
- 另：首建 run.py 在服务重启中完成（TOTAL 150，日志核实无溢出），render.py 重启后补跑；产物均为原地重建，生产文件已核实。

## 门禁（最终版全绿）
- run TOTAL 150，0 FLOW OVERFLOW，HEAD TOO WIDE 0；head_check PASS 0 defects；render rc=0。
- D5 普查 0（弯引号 4 个全在 Newsreader 内，合规）；U+201C 普查 0（KR 引号不扩展，裁定 §3）。
- occlusion 0 flags；p8 extract 150/150；p8 compare vs 新 core-es CLEAN，keydiff=[137, 138]（仅读者语译注）。
- boxtitle 0 DEFECT；creambox（tools 版）PASS 0 defects（P8 191 行、余量 52.0px 不变）。
- spill 0；edge 0 TOUCH/0 NEAR；freeze baseline 8/8（venv 下通过，未触发 ko Pillow 10 例外；系统 python3 已核实有 Pillow 10.2.0 备用）；freeze diff vs core-es 新增 CJK 字符 3,458 个（韩语读者层相对 core-es 中文读者层的正当差异）；同版 freeze diff（修前基线 vs 新版）新增 CJK 字符仅 1 个 U+3000。
- 印/网文字层 39,805 字符、7,949 词，逐字一致。

## 交付
- 印刷版 `La-Lucerna-VOL4-es-ko.pdf` 5,229,280 B，SHA-256 `f059db4ed89c374128875f5b2c1c8b76ea4b402f40c8cc40f863c9b53a9b2040`。
- 网页版 `La-Lucerna-VOL4-es-ko-web.pdf` 1,097,508 B，SHA-256 `a555f282aceb71772ca483664537cb4eab85c9321be9fccdbcda2f616219a33f`。
- `text.md` 字节不变（SHA `a24b79b0…`）。
- KIT 已更新（§1 交付行 + 尾部 D5 记录）。日志在本目录；freeze build-copy 已删。
