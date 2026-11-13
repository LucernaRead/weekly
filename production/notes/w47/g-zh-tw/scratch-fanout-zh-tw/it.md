# it — 2026-w47-zh-tw-it（完成，2026-11-11 ~02:55 UTC，第 7 棒）

**结论：完成，全量自查零问题。**

- 印刷 PDF `Lucerna-VOL4-IT.pdf` 19,420,291 字节，SHA-256 `ec9d0624d91abb2ae8875f5f51cb2064d7927d4f1a4a8e4f2454b1fb11894bce`；网页 PDF `Lucerna-VOL4-IT-web.pdf` 2,306,683 字节（< 7 MB），SHA-256 `34c4ff2c9e3f1fe0e3714c773b5ead11306e542c4a60e52b2c815684ba986988`；text.md SHA-256 `5e0ada652cf39269b96cac9c25f675deab93ab239f00ee8d2ea891a657ded507`。
- 门禁：run exit 0（最终轮 0 溢出、0 超宽）；occlusion 0 flags；p8 extract 150/150、compare CLEAN；freeze 直接 sha256 8/8；checks PASS；print/web 文字层多重集差 0；P8 最小字号 9.75pt；§1.1 实测通过；8 版目视通过；150 题复核通过；全版泄漏扫描 0；P8 徽章 38/38，Q113–150 各带徽章，F 写作标题在。
- 详见本版 `WEEKLY-KIT.md`。

## 本版修过的三处（均只改本版目录内文件）

1. **6 条 P8 答案注记预补译**：与 de/fr/es 同一 tables.py 缺口，首轮构建前已在 content56.py/content8.py 译成意大利语（La cerimonia è al Taipei Music Center. / Xiaoxue è il 22 nov. / Quattro grandi eventi cadono la stessa domenica. / Raccogliere punti è 集點。），答案键不动。
2. **P6 栏头超宽**：首轮 1× HEAD TOO WIDE（466.9px vs 栏宽 422.5px），content56.py 缩为 "Quiz di lettura"（299.0px）。另一栏头 "Leggi la linea del tempo"（415.5px）本已合格——未按表中 "Leggere la linea del tempo" 误改。
3. **P7 第 3 栏溢出压页脚**：首轮 col3 终点 1908.7、预告条终点 2662.7；修 content7.py（披露 8→7 行、诊所第 3 条注 3→2 行、句式例 5→4 行），终点 1823.3 / 2577.3，occlusion 0。
4. 删 copytree 带入的核心旧件 3 个；tables.py 镜像时 P6 栏头条目按实际形式补镜像（初次替换因措辞不符计数 0，已按行 563 原串补正）。

## 已裁定的非缺陷

- P4 "Parole del baseball" 栏头折两行（栏内，无溢出）；P5 首篇末行跨栏续排；P8 题干 10.35pt 按核心裁定；text.md 页标题英文为导出器固定格式。

## 日志

- `transform-it.log`（244 行）、`build-it-run.log`（1 HEAD TOO WIDE，P7 2662.7）/ `build-it-run2.log`（0 警告）、`render-it.log`、`webpdf-it.log`、`checks-it.log`、`occlusion-it.log`（0 flags）、`p8-extract-it.log`、`p8-compare-it.log`（CLEAN）、`leak-scan-it.log`（0）、`freeze-it.log`（8/8）、`export-it.log`。
