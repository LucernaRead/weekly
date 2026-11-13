# GATE-LOG — W47 core-zh-tw fix4：三處源句修后全套机械门重跑记录

- **复校对象**：`~/workspace/weekly-git/production/2026-w47/core-zh-tw/`（修后）
- **工具**：`~/workspace/weekly-git/tools/venv/bin/python`（共享工具，永不去 /tmp）；`webpdf.py` 为 commit `40963281` 定稿版
- **日志目录（绝对路径）**：
  `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-core-zh-tw4/`
- **时间**：2026-11-11 09:43–09:54 UTC

## 0. 探针与交付物（见 FIX-LOG §0、§4）

- `git hash-object -w` RC=0；笔记目录写盘 RC=0；全程 `TMPDIR=<scratch>/tmp`，无 `Disk quota exceeded`。
- 改后 print `Lucerna-VOL4.pdf` 19,420,551 B / SHA `97e896947fba550a0e4dd496e093a2cbafef88ed5cd0398052a3508aa77f11b0`；
  web `Lucerna-VOL4-web.pdf` 2,324,051 B（< 7 MB）/ SHA `121cba14278ef1af117eff324b4ac9c2ec6837e0564186c3d91bd98148cd8d62`；
  text.md 49,798 B / SHA `09e083e10da2784cea4f636399b11e822e526ccdda3b2d94a3db68744e02f02b`；
  双 PDF 各 8 页、1462.5×2025 pt。
- 印刷 PDF 两跑 SHA 相同（render2.log 再跑一次仍为 `97e89694…77f11b0`）。

## 1. 构建门（build.log / render.log / render2.log / webpdf.log / export.log）

- `run.py` RC=0；`render.py` RC=0（两次）；`webpdf.py` RC=0；`export_zhtw_textmd.py` RC=0。
- 无 FLOW OVERFLOW、无 HEAD TOO WIDE 警告。
- Registry：TOTAL 150（A2 44 / B1 74 / B2 32；分頁 10/18/18/18/18/18/12/38）——与修前一致。
- `flow[P7-b1] ended col 0/0 y=1535 (bottom 1560)`——新记忆句比修前长（修前 y=1501），仍留 25px 余量，无断行溢出；`flow[P1-lead] y=1659 (bottom 1935)` 不变。

## 2. 文字层一致（print.txt / web.txt，pdftotext -layout）

- print 101,461 B；web 101,461 B（均 > 0，有文字层；修前各 101,442 B，+19 B）。逐页字符数双版完全相同
  （P1 7909 / P2 9239 / P3 10806 / P4 7612 / P5 11268 / P6 8525 / P7 11477 / P8 18211；
  修前 P1 7907 / P7 11460，其余 6 页不变；P1 +2 字符恰为修 3「小雪」→「夜間遊行」，
  P7 +17 字符恰为修 1（+19）与修 2（−2）之和——其余增量差为 -layout 空格填充随断行重排而变，
  内容以 §2 的 diff 为准）。
- 字符多重集差：print-only **0**；web-only **0**（本次双版逐字节同长且多重集全等，优于 fix3 的 1 换行差）。
- `本週日` print/web 各 11×；`下週日` 各 0；`BABYMONSTER` 各 0；`取捨` 各 2×（正文 1 + P8 鍵 1）；
  `小雪` 各 36×（修前 37，僅減 P1 框內 1 次）；`夜間遊行` 各 25×（修前 24）；
  `finish line` 各 0；`end point` 各 1×；`the red carpet at 17:00` 各 1×；`18:30` 各 12×。
- `print.txt` vs fix3 `print.txt` diff **仅 3 处**（P1 L57、P7 L640、P7 L688–691），三处新句完整在层。
- 一处提取说明：新记忆句 `ceremony （頒獎）` 的空格在 SVG 内存在（节点 161 尾端空格，节点 162 起于 x=849.6；目视有空格），
  `pdftotext -layout` 拼接相邻 span 时略去，印出 `ceremony（頒獎）`。双版一致、多重集差 0，属提取拼接 artifact，视觉与 SVG 均正确。
- **结论：文字层完整一致，PASS。**

## 3. occlusion_audit.py（occlusion-selftest.log / occlusion.log / occlusion.json）

- `--selftest` rc=0：6 类皆触发（BOXTITLE/COVER/EDGE/FOOTER/LINEX/TEXTX 各 1），干净对照沉默。
- 本版审计 rc=0：**0 flags**（`flag_count: 0`）。
- **结论：PASS。**

## 4. p8.py（p8-extract.log/.json / p8-compare.log/.json）

- `extract --p8 svg/p8-test.svg --total 150` rc=0：noted set = **150/150**。
- `compare`（本核心 P8 vs `../2026-w47-zh-tw-de/svg/p8-test.svg`，fan-out 德语读者版）rc=0：
  **CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]。
  （三处修复未动任何题/键，keydiff 为零符合预期。）
- **结论：PASS。**

## 5. checks.py（checks.log）— rc=0 PASS

- 本週金句 8 句各 2 次（文章＋P7）。
- SIMP_ONLY_HITS []（无简体字）。
- P4 bars [90.0, 450.0, 900.0]；P6 dots [188.0, 695.21, 948.82, 1033.36, 1202.43]——与预期一致。

## 6. freeze.py（freeze-base.log）

- `baseline --build . --core-svg svg --out <scratch>/freeze-base` rc=0：
  **8/8 SVGs byte-identical**（重建产物与已交 SVG 逐字节相同；core integrity：
  运行前后 8 个已交 SVG 哈希不变）。
- 与修前逐页比对，**仅 p1-front.svg 与 p7-lang.svg 变化**
 （p1 `0a362c6e…`→`cc70b39c…`，p7 `292a5110…`→`839a8093…`），
  其余 6 页哈希与 fix3 完全相同——本次修复只动 P1、P7，无其他页回归。
- **结论：PASS。**

## 7. 弯撇／弯引号全扫（U+2019/U+201C/U+201D/U+2018，Python 按码点计数）

- SVG 8 页＋text.md 全扫：**0 命中**。PASS。

## 8. P8 最小字号与 §1.1 颜色（PyMuPDF／fitz）

- P8 最小字号：print 与 web 双 PDF 皆 **9.75pt**（= §1.1 下限）；P8 最大 34.5pt（栏目题）。
- 双 PDF 各 8 页、1462.5×2025 pt。
- 纸色 #fbfaf6：8 页各 1 处；金色系 fill（#b8860b/#d4af37/#c9a227/#8b4513）：**0**。
- **结论：PASS。**

## 9. 54 个填空键答案词出自正文复核（fillin-check.log，check_fillin_keys.py，fix3 方法重跑）

- 方法：源 `.py` 解析全部 `"完成句子"` 调用得 54 键，逐键查是否出现于 text.md keys 区之前。
- 结果：**54/54**，缺失 []。其中「取捨」正文出现 1 次（D3 未回归；「小雪」正文 32 次）。
- **结论：PASS。**

## 10. 目视（p1-crop.png / p7-crop.png / p7-m1-crop.png，本目录）

- P1 本週日框：「本週日 11/22 遊行、金馬獎、鋼雕閉幕、夜間遊行」两行完整，框体无破损。
- P7 记忆句：「Memory trick: learn 入圍 first, then 星光大道 (the red carpet at 17:00, before the ceremony), then the ceremony （頒獎） at 18:30.」四行完整，`ceremony （頒獎）` 间有空格，无溢出、无重叠。
- P7 M1 句：「Parades give you four useful words: 遊行 (parade), 封王 (clinching the title), 夜間 (night-time) and 終點 (end point). Learn them once, and every parade makes sense.」完整，无溢出。
- 其余 6 页 SVG 与 fix3 字节相同，无需重看；见 §6。
- **结论：目视通过。**

## 11. 防回退项

- D1：text.md / 双 PDF 文字层 `本週日` 各 11、`下週日` 0——无回归。
- D2：`BABYMONSTER` 0（源 .py、text.md、双 PDF 文字层）——无回归。
- D3：`取捨` 源 .py 2 处（文章 L131 + 題目定義 L184，未变，`content56.py` SHA 与修前相同）；text.md 2 处（正文 + keys 區鍵）；双 PDF 文字层各 2 次——无回归。
- Q34：《月球之旅》是哪一年拍的？鍵 `34. C — A Trip to the Moon was made in 1902.` 在 text.md keys 區仍为 L5772，与修前同行同文；题面与选项未动——无回归。
- 禁动项：`content56.py:131` SHA 修后与修前相同；`scratch-fanout-zh-tw/tables.py` 未动。

## 总结：全套机械门全绿

| 门 | 结果 |
|---|---|
| 构建（run/render×2/webpdf/export） | RC 皆 0，无 overflow 警告，150 题分布不变；印刷 PDF 两跑 SHA 相同 |
| occlusion_audit.py（自检先过） | 0 flags |
| p8.py extract --total 150 | 150/150 |
| p8.py compare（新核心 vs zh-tw-de） | CLEAN，keydiff=[] |
| freeze.py baseline | 8/8 byte-identical（仅 P1、P7 变，其余 6 页与 fix3 相同） |
| checks.py | PASS（金句 8×2、简体 0、图表几何一致） |
| print/web 文字层多重集差 | print-only 0 / web-only 0（-layout 模式）；逐页字符数双版相等 |
| U+2019/U+201C/U+201D 全扫 | 0 |
| P8 最小字号（双 PDF） | 9.75pt（= §1.1 下限） |
| §1.1 颜色 | 纸 #fbfaf6 ×8 页；金／红褐 0 |
| 54 填空键复核 | **54/54，缺失 []** |
| 目视（P1 框、P7 记忆句、P7 M1 句） | 通过（新句完整上版、无溢出） |
| D1/D2/D3/Q34 回归 | 本週日 11/11、下週日 0、BABYMONSTER 0、取捨 2/2、Q34 同行同文（无回归） |
| text.md 字节变化 | +32 B，opcode 求和与文件增量一致，仅三处源句所致 |

## 未做事项（按任务范围）

- 未跑 insert.py、lint --write；未做任何 git 写操作（除任务要求的 hash-object 探针外；
  core-zh-tw/ 目录目前未入 git 追踪，属 W47 生产中状态）。
- 未碰 fan-out 各版、tools/、其他目标语。WEEKLY-KIT.md 已按任务更新为本次交付 SHA（仅 L53、L129 两行）。
- 下一步（协调员另派）：修后全量复校；本修复员不派复校。
