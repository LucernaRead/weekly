# ru — 2026-w47-zh-tw-ru（完成，2026-11-11 ~03:55 UTC，第 7 棒）

**结论：完成，全量自查零问题。**

- 印刷 PDF `Lucerna-VOL4-RU.pdf` 12,896,270 字节，SHA-256 `e1f3c46a9e22a3b03c9b8a6c9fc450b86bb254ccbec223169b682c2447c2ff76`；网页 PDF `Lucerna-VOL4-RU-web.pdf` 1,993,092 字节（< 7 MB），SHA-256 `385e4b265347bb5d87442934b60f9b2c1bac88b48bfc20ca98033bc54d6a0719`；text.md SHA-256 `41da5432e31c1f9819a6508d8fc91933a64ac6cd8b0a0794e32f0d10e0319f09`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；全版泄漏扫描 0；P8 徽章 38/38，Q113–150 各带徽章，F 写作标题在。
- 详见本版 `WEEKLY-KIT.md`。

## 本版修过的五处（均只改本版目录内文件）

1. **6 条 P8 答案注记预补译**：与 de/fr/es/it/pt/nl 同一 tables.py 缺口，首轮构建前已在 content56.py/content8.py 译成俄语（Церемония — в Тайбэйском музыкальном центре. / Сяосюэ — 22 ноября. / Четыре больших события приходятся на одно воскресенье. / Накапливать баллы — это 集點。），答案键不动。
2. **4 处栏头超宽**：首轮 4× HEAD TOO WIDE（P4 看图 426.2px、P6 看图 484.1px、P6 深读测验 461.0px、P8 D 头 450.7px），均缩为 "Чтение …" 式短头（370.8 / 311.8 / 320.3 / 382.3px）。
3. **P7 第 3 栏溢出为全家最重**：首轮 col3 终点 1968.0、预告条终点 2722.0；俄语披露 10 行、句型注 3 行；修 content7.py（披露 10→7 行、句式例 5→4 行、句型注 3→2 行），终点 1823.3 / 2577.3。
4. **P8 答案区标题与右侧注记重叠**：occlusion 1× TEXTX（8.5×20.5px），标题由 1171px 缩为 830px（"Ответы — по страницам, с примечанием к каждому пункту"），复审 0 flags，终版为 build 3。
5. 删 copytree 带入的核心旧件 3 个。

## 过程事故（已处理，无遗留）

- 首贴补脚本在第一步即失败：P4 栏头在 content34.py 而非 content4.py，版内文件未改，但 tables.py 镜像已先写，造成短暂表/版不一致；用正确文件名重贴后一致，build 2 验证通过。
- 首次 render 被运行时中断（"aborted"：卡片已出、PDF 未生成），第二次在分发层超时；第三次前台执行 rc=0。无 exit 120 / 内存错误。

## 已裁定的非缺陷

- P3 金马小档栏头贴右框边（框内，occlusion 0）；P4 "Слова бейсбола" 栏头折两行（栏内，无溢出）；P5 首篇末行跨栏续排；P8 题干 10.35pt 按核心裁定；text.md 页标题英文为导出器固定格式；印刷 PDF 12.9MB 小于他版约 20MB——卡片尺寸相同、文字层完整，仅为图片嵌入差异。

## 日志

- `transform-ru.log`（244 行）、`build-ru-run.log`（4 HEAD TOO WIDE，P7 2722.0）/ `build-ru-run2.log`（0 警告）/ `build-ru-run3.log`（0 警告）、`render-ru.log`（中断，空）/ `render-ru2.log`（rc=0）、`webpdf-ru.log` / `webpdf-ru2.log`、`checks-ru.log` / `checks-ru2.log`、`occlusion-ru.log`（1 TEXTX）/ `occlusion-ru2.log`（0 flags）、`p8-extract-ru.log` / `p8-extract-ru2.log`、`p8-compare-ru.log` / `p8-compare-ru2.log`（CLEAN）、`leak-scan-ru.log`（0）、`freeze-ru.log`（8/8）、`export-ru.log` / `export-ru2.log`。
