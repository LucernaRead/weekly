# GATE-LOG — W47 ja-ru proof1 机械门重跑记录

- 2026-11-11 08:22 UTC：探针双通（git hash-object -w OK；笔记目录写盘 OK），磁盘 46G 可用。开始。
- 08:23 UTC：成品核对——print 25,858,425 B sha abc44c9c…（任务所给两 SHA 互换，以盘上实测为准，
  与 FANOUT 报告一致）；web 4,396,999 B sha e2fc5382…；双 PDF 8 页；pdftotext 各 53,247 B 逐字节一致。
- 08:24 UTC：旧拼/弯引号/中文残留/· 全扫——拉丁旧拼 0、弯引号 0、中文残留 0、· 0；
  但西里尔转写 Фудзирюга 5 处、Уми-но-уми 1 处（见 PROOF-NOTE D1）。
- 08:25 UTC：P2 词框几何——4 框底 1768，释义单行基线 1752.06，宽 ≤340.1px，无溢出。
- 08:26 UTC：run.py 重跑 exit 0，零溢出，150 题；SVG sha256 重建前后 8/8 相同（freeze 通过）。
- 08:27 UTC：occlusion_audit 0 flags（selftest OK）；p8 extract 150/150。
- 08:28 UTC：p8 compare vs core-ja CLEAN，keydiff=[137,138,139,140]；150 键值逐键比对：146 同，仅 E 组 4 键俄译。
- 08:29–08:40 UTC：text.md 1380 行全读；日期星期全核（date 命令）；相扑事实 web 核对（琉球新報/デイリー/報知）；
  图表验算 100%；P8 注文 prose 逐条人工核对。
- 08:28–08:35 UTC：print 8 版 pdftoppm 渲染目视全过；web 版 pdftoppm 在 p-6/p-7 写盘时 segfault
  （libpng Write Error，磁盘 45G 可用，与成品无关），换 PyMuPDF 重渲 web 8/8 成功，目视全过。
- 08:32 UTC：P8 最小字号 9.975pt（print/web 同）；§1.1 grep 全过；刊头 196px、头条 56px。
- 08:50 UTC：收尾。结论：非零问题——D1 严重（人名转写错 6 处）+ D2/D3/D4 轻微（俄语 3 处）。
  笔记：PROOF-NOTE.md、GATE-LOG.md、audit-*.log/json/txt、print.txt/web.txt、pages/、webpages/、scan1.py。
