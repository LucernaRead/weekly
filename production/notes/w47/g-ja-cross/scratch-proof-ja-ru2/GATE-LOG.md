# GATE-LOG — W47 ja-ru proof2 机械门与复校记录

- 2026-11-11 09:16 UTC：探针双通（`git hash-object -w` OK，9daeafb9…；笔记目录写盘 OK），
  磁盘 7.3G 可用（fix1 时 45G；本轮未遇 EDQUOT）。开始。
- 09:16 UTC：成品核对——print 25,858,387 B sha `86af0bb5…`、web 4,396,966 B sha `dd5fdc63…`，
  与任务所给一致；text.md 53,029 B / 1382 行；双 PDF 8 页；pdftotext 各 53,363 B 逐字节一致。
- 09:17 UTC：SVG sha256 建前存档（ru-sha-proof2-before.txt）；`run.py` 重跑 rc=0，零溢出，
  TOTAL 150（A2 48 / B1 73 / B2 29；按页 10/18/18/18/18/18/12/38；范文 154 字）；
  建后 sha 与建前 **8/8 相同**（ru-sha-proof2-after.txt；freeze 通过）。
- 09:18 UTC：`freeze.py diff --strict-cjk` core-ja vs ja-ru rc=1（added CJK 15 字）；
  自写补充脚本 `cjk-added-proof2.py` 逐出来源为 U+3000 分隔符 + 配对注复现的冻结词
  ノミネート/千秋楽；ja-en 校准跑出**完全相同的 15 字分布**，裁定为 fanout 系统性格式属性，
  非本版缺陷（见 PROOF-NOTE §1.1）。ru text.md / content*.py 中不在核心里的 CJK 字符皆 0。
- 09:19 UTC：`occlusion_audit.py` selftest OK（6 类 planted 全触发，clean 对照静默），**0 flags**。
- 09:19 UTC：`p8.py extract` **150/150**；`compare` vs core-ja **CLEAN**，
  missing=[] extra=0 uncertain=[]，keydiff=[137, 138, 139, 140]。
  150 键逐键比对：146 键与核心逐字节同，仅 E 组 4 键为俄译，逐条核对正确。
- 09:20 UTC：P8 最小字号 9.975pt（print/web 同，次档 10.35pt）；§1.1 grep 全过
  （纸 #fbfaf6 1×/页，旧纸 0，· 在 SVG 0，页码行 1×/页，VOL.4/VOL.5/VOL.3 分布与 proof1 一致，
  刊头 196px、头条 56px）。
- 09:20 UTC：全扫（scan-proof2.py，Python 码点扫描）——旧形 Фудзирюг/Уми-но-уми/
  единственно правильного/Прогноз Японии:/Оканчивайте/一之富士/吉伊卡哇/参考答案/
  酉之市/提名 在 py/SVG/text.md/双 PDF 文字层 **全 0**（仅 KIT/RECORD 的修复历史记录句有；
  新形 Фудзирёг 5×、Чура-но-уми 1×、D2/D3/D4 新句、#47 俄译各就位）；
  弯引号 U+201C/U+201D/U+2019 **全 0**。
- 09:21 UTC：D2/D3 跨行核实——D2 桥接句在 SVG 内跨两 `<text>`（`Письменное задание (единственного` +
  `правильного ответа нет)…`），text.md 与 print 文字层同文；D3 #86 注两行
  （`Прогноз Японской метеорологической ассоциации:` / `Арасияма с 13 нояб.`）。
- 09:21 UTC：P8/P7 几何量测——D4 两行在诊所框内（框底 1087.64，末行 1047.12）；
  P8 末行基线 2530.35、P7 末行 2546.7，皆在页脚带（2580）外；P1 gloss 末基线 1865.95
  vs 分隔线 1884；P2 词框 4 框底 1768，释义单行基线 1752.06。
- 09:21–09:35 UTC：text.md 1380+ 行全读；日期星期 `date` 全核（11/5 周四、11/7 周六、
  11/8 周日、11/9 周一、11/10 周二、11/13 周五、11/16 周一、11/19 周四、11/22 周日、
  11/23 周一、12/1 周二）；图表验算 100%（Q91 14、Q92 62、Q93 100）；150 题逐题验算通过；
  范文重数 154 字；P8 注文 prose 150 条逐条人工核对。
- 09:21 UTC：PyMuPDF 130dpi 渲染 print 8/8 + web 8/8（/tmp/proof2-ja-ru/，一次性中间件）；
  目视 16 版全过，无溢出/重叠/压页脚/豆腐块；印/网像素比对：P2/P4/P6 全同，
  其余 5 版平均绝对差 ≤0.43、差异像素 ≤2.10%（仅网页图降分辨率所致）。
  web P7/P8 逐版目视与 print 一致（D4 两行、#86 两行、H 桥接句皆就位）。
- 09:40 UTC：map-ru.json 只读复核——221 键；D1 五值、D2 meta p8_bridge、D3、D4 值皆为新形；
  含 `一之富士` 的键 0 条，含旧形的 map 值 0 条。
- 09:44 UTC：终验——双 PDF SHA 与开工时一致（print 86af0bb5…、web dd5fdc63…），
  本轮未改动任何源文件与成品。结论：**(a) 零缺陷，可定稿**。
  笔记：PROOF-NOTE.md、GATE-LOG.md、PROBE.txt、ru-sha-proof2-before/after.txt、
  build-proof2-run1.log、freeze-diff-proof2.{json,log}、freeze-diff-ja-en-calibration.log、
  cjk-added-proof2.py、scan-proof2.py、ru-occlusion-proof2-selftest.log、
  ru-occlusion-proof2.{json,log}、ru-p8-proof2.{json,log}、ru-p8compare-proof2.{json,log}、
  ru-p8core-proof2.{json,log}、print-proof2.txt、web-proof2.txt。
  （页图在 /tmp/proof2-ja-ru/print|web/，一次性中间件，未入 scratch。）
