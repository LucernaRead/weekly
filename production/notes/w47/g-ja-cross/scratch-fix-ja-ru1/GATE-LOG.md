# GATE-LOG — W47 ja-ru fix1 门禁重验记录

- 2026-11-11 08:37 UTC：开工探针双通（git hash-object -w OK；笔记目录写盘 OK），磁盘 45G 可用。
  成品身份盘上核实：print 25,858,425 B sha abc44c9c…、web 4,396,999 B sha e2fc5382…
  （任务简报两 SHA 写反，以实测为准，与 FANOUT 报告一致）。
- 08:38 UTC：修前核对——text.md Уми-но-уми 1×、Фудзирюг 5×、Фудзирёг 0×；
  KIT/RECORD/text.md/ABSTRACT 已备份入本目录。
- 08:39 UTC：map-ru.json 改 8 值（D1 5 值 + D2 meta + D3 + D4），逐字断言各出现恰 1 次，
  JSON 校验通过，221 键完整；旧形 grep 0，新形齐全。
- 08:40 UTC：apply ru 第 1 轮 rc=1——MAP key `首日战胜大之里的是一之富士` 在 core 中不存在。
  查明 core-ja 事后把 `一之富士→义之富士`（content34.py:186），map 键过期致 #47 注文残留中文；
  第 1 次改键漏“是”字，第 2 轮仍 rc=1；纠正为仅 `一→义` 后第 3 轮 rc=0，`APPLY ru: OK`
  （221 keys + 6 instr）。日志：apply-fix1-ru.log / -ru2.log / -ru3.log。
- 08:41 UTC：恢复 KIT/RECORD；run.py run1 rc=0，零溢出，TOTAL 150（A2 48 / B1 73 / B2 29；
  按页 10/18/18/18/18/18/12/38；范文 154 字）。render.py 单进程 rc=0，print 25,858,387 B。
- 08:44 UTC：webpdf rc=0，4,396,966 B，53,363 text bytes；export-textmd rc=0，53,029 B / 1382 行。
  新 SHA：print 86af0bb5…、web dd5fdc63…。新旧 text.md diff 恰 9 处（D1 6 + D2/D3/D4），别无差异。
- 08:45 UTC：freeze——run.py run2 rc=0，8 SVG sha256 两次构建 8/8 相同（ru-sha-fix1-run1/2.txt）。
- 08:45 UTC：occlusion_audit selftest OK（6 类 planted 全触发，clean 对照静默），**0 flags**
  （ru-occlusion-fix1.json/log）。
- 08:45 UTC：p8 extract 150/150（ru-p8-fix1.json）；p8 compare vs core-ja **CLEAN**，
  missing=[] extra=0 uncertain=[]，keydiff=[137, 138, 139, 140]（ru-p8compare-fix1.json）。
  逐键比对：146 键与核心逐字节同，仅 E 组 4 键为俄译（值与 proof1 核过的逐字一致）。
- 08:46 UTC：双 PDF pdftotext 各 53,363 B，**逐字节一致**（cmp 通过；print-fix1.txt / web-fix1.txt）。
  P8 最小字号 9.975pt（print/web 同，次档 10.35pt）。P8 键流最末基线 2530.35（#115，底线 2540 内）；
  P7 披露末行基线 2546.70（页脚带 2580 外，余 33px；D4 注文现为两行，诊所框内，无压线）。
- 08:46 UTC：§1.1 grep（8 SVG）：纸 `#fbfaf6` 1×/页；旧纸 `#f7f1e2` 0；`·` 0；页码行
  `Страница N из 8` 1×/页；VOL.4 10×（含刊头等）、VOL.5 3×（P4 次号预告、P7 披露、P7 下期栏，
  与修前同）；弯引号 U+201C/U+201D/U+2019 经 Python 码点全扫为 **0**（py/SVG/text.md/双 PDF 文字层）；
  刊头 196px、头条 56px。注：bash grep 曾误报 3422——$'…' 模式被多字节截断所致，已用 Python 重扫纠正为 0。
- 08:46 UTC：残留扫描——旧形 `Фудзирюг` / `Уми-но-уми` / `единственно правильного` /
  `Прогноз Японии` / `Оканчивайте` / `一之富士` / `吉伊卡哇` / `参考答案` / `酉之市` / `提名` 在
  content*.py / SVG / text.md / 双 PDF 文字层 **全 0**；新形 `Фудзирёг` 5×、`Чура-но-уми` 1×、
  `единственного правильного` / `Японской метеорологической ассоциации` /
  `Глагол должен оканчиваться` / `Ёсинофудзи победил` 各就位。
- 08:47 UTC：页图渲染首次 mkdir 报 EDQUOT（共享配额瞬时峰值，兄弟线并行渲染中；df 45G 可用）。
  停手核查：本目录仅 260K，无可清大中间件，未删任何文件；小写盘恢复后重试一次，
  16 张页图改写 /tmp/fix-ja-ru1/ 成功。
- 08:48–09:10 UTC：目视——print 8/8 全过；web P7/P8 全过（与 print 同版式、无豆腐块）。
  P8：#48 Чура-но-уми、#49/#63 Фудзирёга、#54/#111 Фудзирёги、#86 两行机构全名、
  #116 Фудзирёге、H 栏头 единственного 皆就位，无溢出/重叠/压页脚；
  P7：诊所第 4 条 `Глагол должен оканчиваться формой ます.` 两行居框内，披露栏距页脚充足。
  P1–P6：刊头/图片/图注/页脚齐全，无异常。web P1–P6 未逐页目视——与 print 同源 SVG、
  文字层逐字节一致（已在日志注明口径）。
- 09:12 UTC：KIT §7/§8/§11 + EDITION-RECORD.md 更新为 fix1 数值与 F3 记录；终验 SHA 复核无变。
- 09:15 UTC：收尾。结论：D1–D4 已修，全套门禁重验全绿，待第二轮全量复校。
  笔记：FIX-LOG.md、GATE-LOG.md、PROBE.txt、apply-fix1-ru{,2,3}.log、build-fix1-run{1,2}.log、
  render-fix1.log、webpdf-fix1.log、export-textmd-fix1.log、textmd-fix1.diff、
  ru-sha-fix1-run{1,2}.txt、ru-occlusion-fix1.{json,log}、ru-p8-fix1.{json,log}、
  ru-p8compare-fix1.{json,log}、ru-p8core-fix1.json、print-fix1.txt、web-fix1.txt、
  map-ru.json.pre-fix1、修前 KIT/RECORD/text.md/ABSTRACT 备份。
