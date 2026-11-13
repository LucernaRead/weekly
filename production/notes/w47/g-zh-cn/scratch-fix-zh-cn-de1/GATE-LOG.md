# GATE-LOG — 2026-W47 zh-cn × de fix1（修复员自验）

修复员，2026-11-11 17:30–18:00 UTC。解释器：`~/workspace/weekly-git/tools/venv/bin/python`
（Pillow 13.0.0 / FreeType 2.14.3）。全部命令与原始日志均在本 scratch 目录：
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-zh-cn-de1/`

## 0. 开工前 SHA（与任务预期一致）

- 印 `e6ed50ab8eedb82c249aee9a9ce5e6ed61d0b06bc2060c79c9cdb94957ac424b` / 44,829,975 B ✓
- 网 `7fb396f13ece42b771beb722811e4ab8df8bb2f9971cf2380e3f06d7e83535e5` / 2,732,464 B ✓
- 文 `8940ba88e92d70eb6d54e4759657d187b451e259b1633bb92f9d475e97075b0a` / 50,637 B ✓
- 磁盘：57G 可用。SVG 基线 SHA 存 `svg-before.sha256`。

## 1. 缺陷复现（改前，`gate67-before.log` / `gate8b-before.log`）

- gate67：cream boxes 35；G6 1（P2 `本周生活小日历　Kalender der Woche` 1418.0 vs 1411.5，
  −6.5px）；G7a 1（同行）；G7b 0；edge 0。
- gate8b：孤儿标点 31 处；其中 `1 START '》' y=1366.3 '》startet'` 为唯一 `》` 行首。

## 2. 修前测算（`measure-candidates.py` → `measure-candidates.log`）

- D1 新标题 `本周生活小日历　Wochenkalender`：advance 375.2（旧 411.2），
  ink_right 1383.0，clearance **+28.5px**（旧 −6.5px）。
- D2 新行 `21. Nov., Samstag — der Film 《试探》 startet`：
  wrap → `21. Nov., Samstag — der Film 《试探》`（348.8）/ `startet`（60.6），
  orphan-》=False，split-《试探》=False（旧行 orphan=True，split=True）。

## 3. 改动

仅 `content12.py` 两行：`:50` 去 `neue`；`:187` `Kalender der Woche` → `Wochenkalender`。
其余源码一字不动（grep 核对：`neue Film` 0 次、`Kalender der Woche` 0 次已无残留）。

## 4. 重建（`run-fix1.log` / `render-fix1.log` / `webpdf-fix1.log` / `export-fix1.log`）

- run.py rc=0，TOTAL 150（A2 56 / B1 69 / B2 25；页 10/18/18/18/18/18/12/38；
  类型 完成句子 68 / 单选 50 / 词汇配对 20 / 完形单选 11 / 写作 1）；
  overflow/warn/error/traceback 0 命中；P8 keys 尾 y=2521.9（<2560）。
- render.py rc=0，印 PDF 44,829,877 B。
- webpdf.py rc=0，WROTE 2,732,386 B，44,729 text bytes。
- export_de.py rc=0，text.md 50,628 B。
- 新三 SHA：印 `b38ffe40ae07b2502766d553d33e50d414d6210288c852ed961259cc2ee97279`；
  网 `ecd253809c7c4c331a3093dd808fd06337307fb170dc0c0d8a2ab39f79aeaa81`；
  文 `51d6dab11f8b9d857790b8e1c1aba6c5e34259f3eb4b77a19ad77d24106e0a1e`。
- SVG 变化：仅 p1（`eb00af5d…`→`418ad8a2…`）、p2（`d129d1b4…`→`cc90a57e…`）；
  p3–p8 字节不变（`svg-after-run.sha256` diff 为证）。

## 5. gates-zhcn.py — 11/11 ALL PASS（`gates-fix1.log`，rc=0；JSON `gates-de.json`）

```
[PASS] occlusion: rc=0 flags=0 svg/: 0 flags
[PASS] img_overlap: hits=0
[PASS] p8_extract: rc=0 noted=150/150
[PASS] p8_compare: rc=0 verdict=CLEAN keydiffs=0
[PASS] freeze_sha256: run rc=0 match=8/8
[PASS] print_web_text: pages 8/8 posdiff=0 msdiff=0 P1:355/355:pos0:ms0 P2:350/350:pos0:ms0 P3:263/263:pos0:ms0 P4:333/333:pos0:ms0 P5:267/267:pos0:ms0 P6:327/327:pos0:ms0 P7:502/502:pos0:ms0 P8:1706/1706:pos0:ms0
[PASS] pdftotext_nonempty: print=44729B web=44729B web_size=2732386
[PASS] p8_fontsize: answer-zone min=9.98pt median=9.98pt spans=370
[PASS] p8_chips: core={'A2': 11, 'B1': 24, 'B2': 3} edition={'A2': 11, 'B1': 24, 'B2': 3}
[PASS] u2019: files_with_U+2019=[]
[PASS] s11_svg: off-palette={} gold/old=False stroked_rects=0 VOL.5=1(core 1) paper_fills=8
OVERALL: ALL PASS
```

注：P1/P2 token 数较 proof 各少 1/2（355 vs 356；350 vs 352），正是删 `neue`（1 token）
与标题 3 词→1 词（2 tokens）所致，属预期变化；其余各页与 proof 相同，posdiff/msdiff 均为 0。
P8 字号 9.98pt ≥ 9.75pt（SOP §1.1 下限），与核心同值。

## 6. freeze（`freeze-baseline-fix1.log` / `freeze-diff-fix1.log` / `freeze-diff-fix1.json`）

- baseline：rc=0，**8/8** SVGs byte-identical（repointed 6 文件）；
  `core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。
- diff `--strict-cjk`：rc=0，**TOTAL added CJK characters: 0**；
  P1 886→870 / P2 1065→1060 / P3 864→859 / P4 772→767 / P5 969→964 /
  P6 912→907 / P7 753→748 / P8 1125→1120，各页新增 CJK 均为 0。

## 7. gate67 + gate8b（修后，`gate67-after.log` / `gate8b-after.log`；JSON `gate67.json` / `gate8b.json`）

- gate67：cream boxes 35；**G6 0、G7a 0、G7b 0、edge 0**。
  P2 日历标题 `本周生活小日历　Wochenkalender`：ink_right 1383.0，box_right 1411.5，
  **clearance +28.5px**（修后标准 ≥ +5px，通过）。35 盒最小余量现为 P1 数字盒 14.5px。
- gate8b：孤儿标点 31→**30 处**；`》` 行首 **0 处**（grep `》` 无命中）；
  其余 30 处与改前一致、均为核心同款已接受形态。

## 8. 150dpi 渲染像素验证（`verify-pixels.py` → `verify-pixels.log`，裁图见 §9）

- D1（印 PDF P2，150dpi）：校准——奶油盒右缘实测 svg x=1410.6（标称 1411.5，量化差 0.9px）。
  标题行带（svg y 210–245）内、盒边右侧条带 (1411.5, 1439.5] 的暗像素 26 个，
  **全部位于 svg x=1439.4 单列**，即山谷照片（x=1439.5 起）左缘的照片像素
  （蓝灰色值 (37,60,73) 等）；**标题真墨越盒像素 0 个**。
- D2（印 PDF P1，150dpi）：裁图目视确认（见 §9），与 SVG run 一致。

## 9. SVG run + 裁图（D2 直接证据）

- 新 `p1-touiban.svg`：
  `y=1339.265, x=556.5: '21. Nov., Samstag — der Film '`；
  `y=1339.265, x=825.3: '《试探》'`（同行闭合）；
  `y=1366.265, x=556.5: 'startet'`（无 》）。
- 新 `p2-shenghuo.svg`：`x=1007.0, y=237, 23pt bold: '本周生活小日历　Wochenkalender'`。
- 裁图：`p2-cal-title-after.png`（D1：标题完整落于奶油底，右侧留白后接山谷照）、
  `p1-numbers-box-after.png`（D2：第一行以 `《试探》` 收尾，第二行仅 `startet`）。
  两图均已目视读过。

## 10. 150 键复核（`reg-ed.json` / `reg-core.json` / `p8-extract-fix1.json` / `p8-compare-fix1.json`）

- 在 scratch 副本运行 `dump_reg.py`（`regcheck-ed/`、`regcheck-core/`，OUT 已重定向至副本，
  未在生产目录运行）：REG 各 150 条。
- REG 键（key-only）edition vs 核心：**0 差异**；edition vs proof1 版：**0 差异**；
  页/级/型：**0 差异**；德语注记 vs proof1 版：**0 差异**。
- `p8.py extract`：edition 150/150，core 150/150。
- `p8.py compare`：rc=0，**CLEAN**，missing=[] extra_count=0 uncertain=[] keydiff=[]；
  P8 印出键 edition vs 核心：**0 差异**。
- P8 印出键 vs REG 键：仅 Q150 不同（REG `(开放题，范文如下)` vs P8 `✓`），
  与核心一致，是设计（P8 表头 `✓ = die Schreibaufgabe`）。
- badge 复核：新 SVG + text.md 中 `德语讲解` 0 次。

## 11. 回归核对

- 仅 P1/P2 两页 SVG 变化（§4）；其余 6 页 SHA 与修前逐字节相同。
- 核心核对：`core-zh-cn/svg` 8 枚现 SHA 与 freeze-baseline 记录的 core 哈希逐字节相同
  （p1 `6685c71a…`、p2 `70a22dc6…`、p3 `1386ba27…`、p4 `0d9b8ed7…`、p5 `a0c0ae12…`、
  p6 `40db68d1…`、p7 `c6752fe2…`、p8 `ce8692e2…`）；freeze 自身 before/after 哈希守卫通过。
  附注：核心 SVG mtime 显示 17:53:22–17:54:10，但我本次 freeze-baseline 结束于 17:49:30，
  该触碰在 4 分钟后、系并行他线；内容哈希已证零改动（详见 FIX-LOG §8）。
- 未 commit、未 push。全部中间文件只在 本 scratch 内。
