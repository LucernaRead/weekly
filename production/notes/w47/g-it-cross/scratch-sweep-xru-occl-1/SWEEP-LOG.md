# SWEEP-LOG — W47 *-ru occlusion + boxtitle 扫查（只读，未改源）
- 时间：2026-11-13 ~01:10–01:20 UTC；扫查员：扫查工人（协调员 #4 派）
- 对象：2026-w47-en-ru、2026-w47-it-ru、2026-w47-ja-ru、2026-w47-ko-ru（~/workspace/weekly-git/production/2026-w47/）
- 工具（与 fr-ru 门禁同一命令）：tools/venv/bin/python tools/occlusion_audit.py <edition-dir> [--core <core>] [--json]；tools/venv/bin/python tools/boxtitle_check.py <edition-dir> --json-dir <scratch>/boxtitle
- 日志与证据：本目录 scratch-sweep-xru-occl-1/（occlusion-<e>.log/json、occlusion-it-ru-vs-core.log/json、occlusion-core-it.log/json、boxtitle-<e>.log、boxtitle/<slug>.json）
- 范围说明：en-ru 与 it-ru 的 HEAD TOO WIDE 已裁定接受处不在本次扫查范围内，未重复报；只报 occlusion 与 boxtitle 新发现。

## PDF SHA-12 与大小（扫查时磁盘态）
- en-ru：印 The-Lucerna-VOL4-en-ru.pdf dde756cbb1a1 / 28,991,750 B / 2026-11-12 21:46 UTC；网 The-Lucerna-VOL4-en-ru.web.pdf 21d126378f87 / 2,468,667 B / 2026-11-12 23:43 UTC
- it-ru：印 La-Lucerna-VOL4-RU.pdf 97095d301dc1 / 13,644,353 B / 2026-11-12 23:44 UTC；网 La-Lucerna-VOL4-RU-web.pdf 55368ada2028 / 1,361,680 B / 2026-11-12 23:44 UTC
- ja-ru：印 Lucerna-VOL4-JA-RU.pdf 44d884ac6b54 / 25,898,158 B / 2026-11-12 23:50 UTC；网 Lucerna-VOL4-JA-RU-web.pdf d130ae325fed / 4,469,712 B / 2026-11-12 23:51 UTC
- ko-ru：印 Lucerna-VOL4-KO-RU.pdf 9bf5c43082b6 / 43,846,114 B / 2026-11-12 23:53 UTC；网 Lucerna-VOL4-KO-RU-web.pdf 5fc509995df1 / 4,047,903 B / 2026-11-12 23:53 UTC
- git status：四版目录均为 untracked（??），插仓前正常态。

## 逐版结果

### 2026-w47-en-ru — FAIL（occlusion 0 / boxtitle 3 DEFECT）
- occlusion：PASS — 0 flags（selftest OK）。
- boxtitle：FAIL — 3 DEFECT（44 titles / 395 body lines，0 OBSERVE，0 marginal；core=core-en）。
  - P1 [TITLE] 'Цифры' over=+8.5px (right)，core=-11.4。整行：'THE WEEK IN NUMBERS　Цифры'（23pt，gloss 起 x=1333.0，ink_r=1420.0，栏右=1411.5）。overlap=None，clip=False。
  - P5 [TITLE] 'Цифры' over=+24.3px (right)，core=-11.6。整行：'ODD SOCKS, IN NUMBERS　Цифры'（23pt，gloss 起 x=447.8，ink_r=534.8，栏右=510.5）。
  - P6 [TITLE] 'Бюллетень' over=+11.4px (right)，core=-18.0。整行：'A PRACTICE BALLOT　Бюллетень'（23pt，gloss 起 x=838.4，ink_r=972.4，栏右=961.0）。
  - 机制与 fr-ru 同：拉丁标题改走较宽 Newsreader 后把俄文 gloss 向右顶出盒外。

### 2026-w47-it-ru — FAIL（occlusion 1 / boxtitle 4 DEFECT）
- occlusion：FAIL — 1 flag {'LINEX': 1}（selftest OK）。
  - [LINEX] p7-lingua.svg 'VOL.5.' — later line box [87.0, 1685.0, 1863.0, 1687.0] crosses ink。ink box [1461.5, 1682.1, 1526.5, 1697.1]。
  - 实测复核（真墨，非误报）：'VOL.5.' 基线 y=1696.32，20pt；分隔线 y=1686、stroke-width 2，绘于该文本之后，横穿字形上部（ink 顶 1682.1 < 线 1685–1687 < ink 底 1697.1），即横线划过 'VOL.5.' 字墨。
  - vs core-it：core-it 0 flags，NEW vs core = 1。core-it 的 'VOL.5' 在 y=1639.52（线之上）；it-ru 的俄文 gloss 行（y=1667.92 'нет; обещание переносится на'）把 'VOL.5.' 顶到下一行，恰落在分隔线上。
- boxtitle：FAIL — 4 DEFECT（37 titles / 498 body lines，0 OBSERVE，0 marginal；core=core-it）。
  - P1 [TITLE] 'ЦИФРАХ' over=+31.8px (right)，core=-18.0。整行：'LA SETTIMANA IN CIFRE　В ЦИФРАХ'（22pt，gloss 起 x=895.8，ink_r=992.8，栏右=961.0）。
  - P1 [TITLE] '.' over=+4.8px (right)，core=-9.8。整行：'IN QUESTO NUMERO　СОДЕРЖ.'（24pt，句点 ink 1860.8–1866.8，栏右=1862.0）——gloss 词尾句点微溢。
  - P2 [BODY] 'ЗАПОМНИТЕ' over=+26.5px (right)，core=-8.3。整行：'LA FRASE PER RICORDARE　ЗАПОМНИТЕ'（19.5pt，gloss 起 x=859.5，ink_r=987.5，栏右=961.0）。
  - P4 [BODY] 'DOPO 11 GIORNATE' over=+18.1px (right)，core=-22.0。整行：'LA CLASSIFICA　DOPO 11 GIORNATE'（21pt，起 x=1656.1，ink_r=1880.1，栏右=1862.0）——此处溢出段本身即拉丁文（Newsreader 加宽直接致溢）。

### 2026-w47-ja-ru — PASS（occlusion 0 / boxtitle 0）
- occlusion：PASS — 0 flags（selftest OK）。
- boxtitle：PASS — 0 DEFECT（49 titles / 658 body lines，0 OBSERVE，0 marginal；core=core-ja）。

### 2026-w47-ko-ru — PASS（occlusion 0 / boxtitle 0）
- occlusion：PASS — 0 flags（selftest OK）。
- boxtitle：PASS — 0 DEFECT（85 titles / 1209 body lines，0 OBSERVE，0 marginal；core=core-ko）。

## 结论
- PASS：ja-ru、ko-ru（两门禁全绿）。
- FAIL：en-ru（boxtitle 3 处）、it-ru（occlusion 1 处 + boxtitle 4 处）。7 处 boxtitle 缺陷均为右溢、均为 vs core 回归（core 值全部为负，即 core 态不溢），与 fr-ru 的 4 处同一机制（拉丁改走较宽 Newsreader 顶宽标题行）；it-ru 的 occlusion 1 处为分隔线划过被顶到下一行的 'VOL.5.'，vs core 为 NEW。
- 未修：按任务只读扫查，未动任何源。
