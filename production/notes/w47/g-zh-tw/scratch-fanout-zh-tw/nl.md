# nl — 2026-w47-zh-tw-nl（完成，2026-11-11 ~03:30 UTC，第 7 棒）

**结论：完成，全量自查零问题。**

- 印刷 PDF `Lucerna-VOL4-NL.pdf` 20,939,118 字节，SHA-256 `254751618af573d563bf11632fb2487ee01e1b2ea15b54c609a08fb129e34e32`；网页 PDF `Lucerna-VOL4-NL-web.pdf` 2,393,503 字节（< 7 MB），SHA-256 `3c308d062aeda055039936558b1a608eee30229092e79a56fe3b2f153dbf081d`；text.md SHA-256 `dcfc16818510b3229b1611607de403ea93219f75f3c24a4a0fa6dfd681410051`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；全版泄漏扫描 0；P8 徽章 38/38，Q113–150 各带徽章，F 写作标题在。
- 详见本版 `WEEKLY-KIT.md`。

## 本版修过的三处（均只改本版目录内文件）

1. **6 条 P8 答案注记预补译**：与 de/fr/es/it/pt 同一 tables.py 缺口，首轮构建前已在 content56.py/content8.py 译成荷兰语（De ceremonie is in het Taipei Music Center. / Xiaoxue is op 22 nov. / Vier grote evenementen vallen op dezelfde zondag. / Punten sparen is 集點。），答案键不动。
2. **P7 第 3 栏溢出压页脚**：首轮 col3 终点 1908.7、预告条终点 2662.7；荷兰语与 fr/es/it/pt 不同——其第 3 条诊所注已是 2 行，省行改从别处来：披露 8→7 行、诊所第 2 条注 2→1 行（"De parade vertrekt om 14:00 (niet 02:00)."）、句式例 5→4 行；终点 1823.3 / 2577.3，occlusion 0。
3. **text.md H1 按 W46 nl 前例更正**：首导出用了 "Teksten in traditioneel Chinees"，W46 nl 是 "Teksten in het Chinees (traditioneel)"，已重导出。
4. 删 copytree 带入的核心旧件 3 个；freeze 首跑 exit 127 仅因在版目录内用了相对路径 `tools/venv/bin/python`，从仓根重跑 rc=0，8/8。

## 已裁定的非缺陷

- P4 "Honkbalwoorden" 栏头折两行（栏内，无溢出）；P5 首篇末行跨栏续排；P8 题干 10.35pt 按核心裁定；text.md 页标题英文为导出器固定格式。

## 日志

- `transform-nl.log`（244 行）、`build-nl-run.log`（0 警告，P7 2662.7）/ `build-nl-run2.log`（0 警告）、`render-nl.log`、`webpdf-nl.log`、`checks-nl.log`、`occlusion-nl.log`（0 flags）、`p8-extract-nl.log`、`p8-compare-nl.log`（CLEAN）、`leak-scan-nl.log`（0）、`freeze-nl.log`（8/8）、`export-nl.log` / `export-nl2.log`（H1 更正）。
