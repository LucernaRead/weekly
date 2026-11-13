# GATE-LOG — W47 core-zh-tw fix3：D3 修后全套机械门重跑记录

- **复校对象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（修后）
- **工具**：`~/workspace/weekly-git/tools/venv/bin/python`（共享工具，永不去 /tmp）
- **日志目录（绝对路径）**：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-zh-tw3/`
- **时间**：2026-11-11 09:31–09:4x UTC

## 0. 探针与交付物（见 FIX-LOG §0、§4）

- `git hash-object -w` 每次 RC=0；笔记目录写盘 RC=0；全程无 `Disk quota exceeded`。
- 改后 print `Lucerna-VOL4.pdf` 19,420,533 B / SHA `11dae5e73bdcea590bcb54523bafd09c8d39d56b704ee0c747de6ed7a023a78f`；
  web `Lucerna-VOL4-web.pdf` 2,324,030 B（< 7 MB）/ SHA `624685e427ee1800bbdc6955ab2c1edb2217b2ff3c96bdcbcf0baa408db0afd4`；
  text.md 49,766 B / SHA `80ed153b66f899e54d991e8ba8828d1995a6830012817b730941046bb62a0560`；
  双 PDF 各 8 页、1462.5×2025 pt。
- 印刷 PDF 两跑 SHA 相同（render2.log 再跑一次仍为 `11dae5e7…23a78f`）。

## 1. 构建门（build.log / render.log / webpdf.log / export.log / render2.log）

- `run.py` RC=0；`render.py` RC=0（两次）；`webpdf.py` RC=0；`export_zhtw_textmd.py` RC=0。
- 无 FLOW OVERFLOW、无 HEAD TOO WIDE 警告。
- Registry：TOTAL 150（A2 44 / B1 74 / B2 32；分頁 10/18/18/18/18/18/12/38）——与修前一致。
- `flow[P6-main] ended col 1/2 y=483 (bottom 860)`——新句无断行溢出。

## 2. 文字层一致（print.txt / web.txt，pdftotext -layout）

- print 101,442 B；web 101,442 B（均 > 0，有文字层）。逐页字符数双版完全相同
  （P1 7907 / P2 9239 / P3 10806 / P4 7612 / P5 11268 / P6 8525 / P7 11460 / P8 18211，
  含页间分隔符计数；双版逐页相等）。
- 字符多重集差：print-only **0**；web-only **0**。
- `本週日` print/web 各 11×；`下週日` 各 0；`BABYMONSTER` 各 0；`取捨` 各 2×（正文 1 + P8 鍵 1）。
- **结论：文字层完整一致，PASS。**

## 3. occlusion_audit.py（occlusion-selftest.log / occlusion.log / occlusion.json）

- `--selftest` rc=0：6 类皆触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），干净对照沉默。
- 本版审计 rc=0：**0 flags**（`flag_count: 0`）。
- **结论：PASS。**

## 4. p8.py（p8-extract.log/.json / p8-compare.log/.json）

- `extract --p8 svg/p8-test.svg --total 150` rc=0：noted set = **150/150**。
- `compare`（本核心 P8 vs `../2026-w47-zh-tw-de/svg/p8-test.svg`，fan-out 德语读者版）rc=0：
  **CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]。
  （D3 未动任何题/键，keydiff 为零符合预期。）
- **结论：PASS。**

## 5. checks.py（checks.log）— rc=0 PASS

- 本週金句 8 句各 2 次（文章＋P7）。
- SIMP_ONLY_HITS []（无简体字）。
- P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]——与预期一致。

## 6. freeze.py（freeze-base.log）

- `baseline --build . --core-svg svg --out <scratch>/freeze-base` rc=0：
  **8/8 SVGs byte-identical**（重建产物与已交 SVG 逐字节相同；core integrity：
  运行前后 8 个已交 SVG 哈希不变）。
- 与修前逐页比对，**仅 p6-deep.svg 变化**（`906ddb0d…`→`51dafd84…`），
  其余 7 页哈希与 fix2 完全相同——本次修复只动了 P6，无其他页回归。
- **结论：PASS。**

## 7. 弯撇／弯引号全扫（U+2019/U+201C/U+201D/U+2018，Python 按码点计数）

- SVG 8 页＋text.md 全扫：**0 命中**。PASS。

## 8. P8 最小字号与 §1.1 颜色（PyMuPDF／grep）

- P8 最小字号：print 与 web 双 PDF 皆 **9.75pt**（= §1.1 下限）；P8 最大 34.5pt（栏目题）。
- 双 PDF 各 8 页、1462.5×2025 pt。
- 纸色 #fbfaf6：8 页各 1 处；金色系 hex（#b8860b/#d4af37/#c9a227/#8b4513）：**0**。
- **结论：PASS。**

## 9. 54 个填空键答案词出自正文复核（fillin-check.log，check_fillin_keys.py）

- 方法：源 `.py` 解析全部 `"完成句子"` 调用得 54 键，逐键查是否出现于 text.md keys 区之前。
- 结果：**54/54**，缺失 []。其中「取捨」正文出现 1 次（P6 文章新句；修前为 53/54）。
- **结论：PASS，D3 闭合。**

## 10. P6 目视（cards/p6-deep.png）

- 新句「怎麼辦？先選一件，再看轉播——四件事只能取捨。」完整上版，段落不断行溢出；
  時間軸、數字一覽、看活動三問、Q83–Q100 皆与修前一致，无溢出、无重叠、无压页脚。
- Q95 题面「四件大事同一天，要學會___。」未动。
- **结论：P6 目视通过。**（其余 7 页 SVG 与 fix2 字节相同，无需重看；见 §6。）

## 11. D1/D2 回归

- D1：text.md / 双 PDF 文字层 `本週日` 各 11、`下週日` 0——无回归。
- D2：`BABYMONSTER` 0（源 .py、text.md、双 PDF 文字层）——无回归。

## 总结：全套机械门全绿

| 门 | 结果 |
|---|---|
| 构建（run/render×2/webpdf/export） | RC 皆 0，无 overflow 警告，150 题分布不变；印刷 PDF 两跑 SHA 相同 |
| occlusion_audit.py（自检先过） | 0 flags |
| p8.py extract --total 150 | 150/150 |
| p8.py compare（新核心 vs zh-tw-de） | CLEAN，keydiff=[] |
| freeze.py baseline | 8/8 byte-identical（仅 P6 变，其余 7 页与 fix2 相同） |
| checks.py | PASS（金句 8×2、简体 0、图表几何一致） |
| print/web 文字层多重集差 | print-only 0 / web-only 0（-layout 模式） |
| U+2019/U+201C/U+201D 全扫 | 0 |
| P8 最小字号（双 PDF） | 9.75pt（= §1.1 下限） |
| §1.1 颜色 | 纸 #fbfaf6 ×8 页；金／红褐 0 |
| 54 填空键复核 | **54/54（修前 53/54），D3 闭合** |
| P6 目视 | 通过（新句上版、无溢出） |
| D1/D2 回归 | 本週日 11/11、下週日 0、BABYMONSTER 0（无回归） |

## 未做事项（按任务范围）

- 未跑 insert.py、lint --write；未做任何 git 写操作（除任务要求的 hash-object 探针外；
  core-zh-tw/ 目录目前未入 git 追踪，属 W47 生产中状态）。
- 未碰 fan-out 各版、tools/、其他目标语。WEEKLY-KIT.md 未更新（留待协调员／re-proof #2 后统一更新）。
- 下一步（协调员另派）：re-proof #2 从头全量复校；本修复员不派复校。
