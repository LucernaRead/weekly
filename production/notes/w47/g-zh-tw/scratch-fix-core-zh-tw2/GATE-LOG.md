# GATE-LOG — W47 core-zh-tw fix2：D2 修后全套机械门重跑记录

- **复校对象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（修后）
- **工具**：`~/workspace/weekly-git/tools/venv/bin/python`（共享工具，永不去 /tmp）
- **日志目录（绝对路径）**：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-zh-tw2/`
- **时间**：2026-11-11 09:06–09:2x UTC

## 0. 探针与交付物（见 FIX-LOG §0、§5）

- `git hash-object -w` 每次 RC=0；笔记目录写盘 RC=0；df 78G 可用，无 EDQUOT。
- 改后 print `Lucerna-VOL4.pdf` 19,419,829 B / SHA `3ab3f758…3474e`；
  web `Lucerna-VOL4-web.pdf` 2,323,405 B（< 7 MB）/ SHA `582c4aa7…46938e`；
  text.md 49,735 B / SHA `7e1a4516…0791c`；双 PDF 各 8 页、1462.5×2025pt。

## 1. 构建门（build.log / render.log / webpdf.log / export.log）

- `run.py` RC=0；`render.py` RC=0；`webpdf.py` RC=0；`export_zhtw_textmd.py` RC=0。
- 无 FLOW OVERFLOW、无 HEAD TOO WIDE 警告。
- Registry：TOTAL 150（A2 44 · B1 74 · B2 32；分頁 10/18/18/18/18/18/12/38）——与修前一致。
- run.py 重跑一次：8 个 SVG 哈希不变（svg-hashes-before/after-run.txt diff 空）。

## 2. 文字层一致（print.txt / web.txt，pdftotext）

- print 46,151 B；web 46,152 B（均 > 0，有文字层）。较 fix1（46,224 / 46,225）各少 73 B，恰为移出行的文字量。
- 字符多重集差：print-only **0**；web-only **1** = 1 个换行（行界空白 artifact；本跑 `電影小課：1902年的月球之` 双版完全相同，Build-14 的空格 artifact 未再现）。
- `本週日` print/web 各 11×（fix1 无回归）；`下週日` 各 0；`BABYMONSTER` 各 0；`台北演唱會` 各 0；`香港11月節目` 各 1。
- **结论：文字层完整一致，PASS。**

## 3. occlusion_audit.py（occlusion-selftest.log / occlusion.log / occlusion.json）

- `--selftest` rc=0：6 类皆触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），干净对照沉默。
- 本版审计 rc=0：**0 flags**（`flag_count: 0`）。
- **结论：PASS。**

## 4. p8.py（p8-extract.log/.json / p8-compare.log/.json）

- `extract --p8 svg/p8-test.svg --total 150` rc=0：noted set = **150/150**。
- `compare`（新核心 P8 vs zh-tw-de 版 P8）rc=0：
  **CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]。
  150 题键值与修前一致——预期：D2 未动任何题/键，keydiff 变化为零（无须说明的变化量即为零）。
- **结论：PASS。**

## 5. checks.py（checks.log）— rc=0 PASS

- 本週金句 8 句各 2 次（文章＋P7）。
- SIMP_ONLY_HITS []（无简体字）。
- P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]——与预期一致。

## 6. freeze.py（freeze-base.log）

- `baseline --build . --core-svg svg --out <scratch>/freeze-base` rc=0：
  **8/8 SVGs byte-identical**（重建产物与已交 SVG 逐字节相同；core integrity：
  运行前后 8 个已交 SVG 哈希不变）。
- 关键回归证据：与 fix1 freeze 记录逐页比对，**仅 p5-youth.svg 变化**（`3b257230…`→`183e0bc4…`），
  其余 7 页哈希与 fix1 完全相同——本次修复只动了 P5，无其他页回归。
- **结论：PASS。**

## 7. 弯撇／弯引号全扫（U+2019/U+201C/U+201D/U+2018，Python 按码点计数）

- SVG 8 页＋text.md 全扫：**0 命中**。注：中途一次 `grep -c` 误报（SVG 为单行文件，按行计数 + 字节类匹配失真），
  以 Python 码点计数为准复核为 0，与 fix1 记录一致。PASS。

## 8. P8 最小字号与 §1.1 颜色（PyMuPDF／grep 抽查）

- P8 最小字号：print 与 web 双 PDF 皆 **9.75pt**（= §1.1 下限）；双 PDF 各 8 页、1462.5×2025 pt。
- 纸色 #fbfaf6：8 页各 1 处；金色系 hex（#b8860b/#d4af37/#c9a227/#8b4513）：**0**；
  GOLD 常数：0（仅正文词 "Golden Horse"）。
- **结论：PASS。**

## 9. P5 几何核查（SVG 实测）+ 目视（cards/p5-youth.png）

- 香港表框：y=1405.6、h=418→底 1823.6；5 行基线 1503.6 / 1565.3 / 1656.7 / 1718.4 / 1780.1，
  末行底距 43.5px（改前 43.8px），无多余留白。
- 爵士表框：y=1841.6（改前 1903.6），框间距 18px 不变；底 2271.6，页脚线 2596 之前留白 324px。
- `BABYMONSTER` 在 p5-youth.svg 中 0 命中。
- 目视：香港表 5 行收尾「迪士尼聖誕音樂會：11月21、22日」，框底距均匀；
  爵士表 5 行完整，无碰撞、无溢出、无页脚碰撞；其余栏目（标题、正文、迪士尼小档、「你呢？」、练习题）与改前一致。
- **结论：P5 目视通过。**（其余 7 页 SVG 与 fix1 字节相同，无需重看；见 §6。）

## 总结：全套机械门全绿

| 门 | 结果 |
|---|---|
| 构建（run/render/webpdf/export） | RC 皆 0，无 overflow 警告，150 题分布不变 |
| occlusion_audit.py（自检先过） | 0 flags |
| p8.py extract --total 150 | 150/150 |
| p8.py compare（新核心 vs zh-tw-de） | CLEAN，keydiff=[]（零变化，符合预期） |
| freeze.py baseline | 8/8 byte-identical（仅 P5 变，其余 7 页与 fix1 相同） |
| checks.py | PASS（金句 8×2、简体 0、图表几何一致） |
| print/web 文字层多重集差 | print-only 0（web 仅多 1 换行 artifact） |
| U+2019/U+201C/U+201D 全扫 | 0 |
| P8 最小字号（双 PDF） | 9.75pt（= §1.1 下限） |
| §1.1 颜色 | 纸 #fbfaf6 ×8 页；金／红褐 0 |
| P5 几何＋目视 | 通过（5 行表框底距正常、爵士表无碰撞） |
| D1 回归 | 本週日 11/11、下週日 0（无回归） |

## 未做事项（按任务范围）

- 未跑 insert.py、lint --write；未做任何 git 写操作（除任务要求的 hash-object 探针外；
  core-zh-tw/ 目录目前未入 git 追踪，属 W47 生产中状态）。
- 未碰 fan-out 各版、tools/、其他目标语。WEEKLY-KIT.md 已按任务更新（新双 PDF 尺寸+SHA + fix2 记录）。
- 下一步（协调员另派）：核心重校一次派发、覆盖 fix1+fix2；本修复员不派复校。
