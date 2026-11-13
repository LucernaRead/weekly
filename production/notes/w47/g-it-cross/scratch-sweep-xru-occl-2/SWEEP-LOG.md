# SWEEP-LOG — *-ru occlusion + boxtitle 扫查（只读，未改源）
- 时间：2026-11-12 ~20:20 EST（2026-11-13 ~01:20 UTC）；扫查员：门禁工人（协调员 #4 派）
- 对象：~/workspace/weekly-git/production/2026-w47/2026-w47-{nl,es,zh-cn,zh-tw}-ru/（改道后重建态，PDF mtime 2026-11-12 23:43–23:52 UTC）
- 工具：tools/venv/bin/python tools/occlusion_audit.py svg/ --json …（自带 selftest 通过）；tools/boxtitle_check.py <edition-dir> --json-dir …/boxtitle
- 日志与证据：本目录（selftest.log、occlusion-<ed>.log/json、boxtitle-<ed>.log、boxtitle/2026-w47-<ed>.json）

## 逐版结果

### 2026-w47-nl-ru — FAIL（boxtitle 4 DEFECT；occlusion 0）
- occlusion：PASS，0 flags，RC=0。
- boxtitle：FAIL，4 DEFECT（34 titles / 483 body lines），RC=1：
  - P1 [TITLE] 'ЦИФРАХ' over +1.5px right，core -7.8；ink_r 962.5，box 右界 961.0（box=[538.5,1440.3,422.5,384.0]），overlap=None，clip=False
  - P2 [TITLE] 'ЗАПОМНИ' over +8.5px right，core -18.0；ink_r 969.5，box 右界 961.0，overlap=None，clip=False
  - P6 [TITLE] 'ДАННЫЕ' over +14.1px right，core -22.0；ink_r 1876.1，box 右界 1862.0，overlap=None，clip=False
  - P6 [BODY] '?' over +9.7px right，core -22.0；ink_r 1871.7，box 右界 1862.0，overlap=None，clip=False
- PDF：印 De-Lucerna-VOL4-nl-ru.pdf sha12 5541fc59de37 / 12,260,999 B；网 De-Lucerna-VOL4-nl-ru-web.pdf sha12 5df8b0d6af5b / 1,674,515 B

### 2026-w47-es-ru — FAIL（boxtitle 1 DEFECT；occlusion 0）
- occlusion：PASS，0 flags，RC=0。
- boxtitle：FAIL，1 DEFECT（41 titles / 581 body lines），RC=1：
  - P1 [TITLE] 'цифрах' over +22.3px right，core -18.0；ink_r 983.3，box 右界 961.0（box=[538.5,1287.7,422.5,417.2]），overlap=None，clip=False
- PDF：印 La-Lucerna-VOL4-es-ru.pdf sha12 277b2d2695f8 / 3,100,942 B；网 La-Lucerna-VOL4-es-ru-web.pdf sha12 985368280784 / 950,829 B

### 2026-w47-zh-cn-ru — PASS
- occlusion：PASS，0 flags，RC=0。
- boxtitle：PASS，0 DEFECT（78 titles / 928 body lines），RC=0。
- PDF：印 Lucerna-VOL4-RU.pdf sha12 52aa381ae7dd / 33,644,459 B；网 Lucerna-VOL4-RU-web.pdf sha12 3e47f038c53b / 2,557,060 B

### 2026-w47-zh-tw-ru — PASS
- occlusion：PASS，0 flags，RC=0。
- boxtitle：PASS，0 DEFECT（72 titles / 1493 body lines），RC=0。
- PDF：印 Lucerna-VOL4-RU.pdf sha12 8c3aca16ea41 / 11,291,943 B；网 Lucerna-VOL4-RU-web.pdf sha12 04606730a740 / 1,997,666 B

## 结论
- occlusion：4/4 版 0 flags，全绿——fr-ru 的 P1 头条撞 gloss 回归未在四版复现。
- boxtitle：2/4 版 FAIL——nl-ru 4 处、es-ru 1 处，均为右溢回归（core 对照值皆为负，即 core 同框不溢）；两中文版 0 DEFECT。
- 未修：按任务只读扫查，未动任何源。nl-ru 的 P1 'ЦИФРАХ' +1.5px 仅略高于 1.0px marginal 阈值，工具仍判 DEFECT（回归 vs core -7.8），如实上报。
