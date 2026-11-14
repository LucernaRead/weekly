# D5 重建报告 — 2026-w43-pt-it（意大利语读者版）
W43 pt 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13–14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-pt/logs/2026-w43-pt-it/`
（`GATES-SUMMARY.txt` 为 run2 门禁总表；`*-gates-run1.log` / `*-rebuild.log` 为 run1 记录）。
## 一、装机
- Core 落盘（全家共用一次）：`apply_variant.py --patch-core pt --week 2026-w43`
  → `production/2026-w43/core-pt/svglib.py`，`_D5_READER = "latin"`（core 模板；与 es 家 core 同型）。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-pt-it/svglib.py --target pt
  --reader it --week 2026-w43`（先 `--check` dry-run 全净，RC 0）。装后 `_D5_READER = "latin"`；装后 svglib 与生产 core-pt 装后版**逐字节相同**（md5 `8f4599b1…`）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py`。text.md 无导出器（pt 家已证实；
  `ru_textmd.py` 试跑差 757 行），已发 `issues/2026-w43/2026-w43-pt-it/2026-w43-pt-it.text.md` 原样 carry-over
  **BYTE-IDENTICAL**（SHA-256 `461229b03ab46da844298519467425b9dd2ebb3e2d42c24266dc21aa3f0c0fcb`），验证用 `verify_textmd.py` carry-over + 门 15。
## 二、基线（修前生产版，全部干净才装机）
- `run.py` RC=0，**TOTAL 150**，0 警告。
- 文字层：印 / 网 / 已发三方字符数均为 43,886 = 43,886 = 43,886，多重集差 **0**；自建网 PDF 716,765 B。
- 印 PDF 5,854,607 B（SHA-256 `aed50f1130194cbc46c2c3bb8db2c2fc3d5b7af55ed804ab1ea5669c23785f8d`，前 8 位 `aed50f11`）；D5 前 KIT 记值 6,450,106 B（D1 旧值，已过期；工具链漂移，见 §六）。
- 修前普查 `d5_census.py`：D5 拉丁 **494**（>0，符合装机前提）、西里尔 0、弯引号在 CJK 0。
- 基线 P8 口径：noted **150/150**。
## 三、缺陷与修法（run1 → run2）
run1 共 5 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比
Noto Sans CJK 宽）。修法只动字号，**未动任何文字内容**。
| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P2-ex 头 `C　COMPLETE COM OS NÚMEROS` | 25pt advance 460.0px，超栏 37.5（栏宽 422.5） | content12.py:256 `e.head` 25→**22**（404.7 ✓；23pt 423.2 仍超 0.7） |
| 2 | head_check | P3-main 头 `DOIS INSTRUMENTOS, UM PAÍS` | 25pt advance 425.7px，超栏 3.2 | content34.py:21 `f.head` 25→**24**（408.5 ✓） |
| 3 | creambox / boxtitle | P1 `CIFRE` 盒标题 | 23pt advance 415.9px，溢出 +11.5px | content12.py:47 `f.box` close 加 `tsize=22`（397.8 ✓） |
| 4 | creambox / boxtitle | P1 `IN BREVE` | 24pt advance 450.3px，溢出 +49.4px | content12.py:132 `p.text` 24→**21**（394.0 ✓） |
| 5 | creambox / boxtitle | P2 `DA RICORDARE` 盒标题 | 23pt advance 436.4px，溢出 +32.5px | content12.py:179 `f.box` close 加 `tsize=21`（398.4 ✓） |

P8 变化：220→**220** 行，距页脚线余量 41.7→**41.7 px**（正，无溢出）。
## 四、门禁（run2，全套 16 门）
| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 （curly_total=0） |
| 4 render | RC=0，印 PDF 5,353,932 B |
| 5 webpdf | RC=0，网 PDF 641,287 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（keydiff=[137, 138]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 250，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（56 OBSERVE） |
| 12 boxtitle | 0 DEFECT（26 titles，254 body lines） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 220→220，slack 41.7→41.7） |
| 15 文字层 print=web | 字符多重集差 **0**；textmd carryover **PASS 0/0**（svg 5246 = md 5246 tokens） |
| 15b 刊头 gap（D18） | 36.2 px PASS |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | pt 家无 gates.py |

**OVERALL: ALL-GREEN.**
## 五、新交付物
（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）
- 印 PDF：`A-Lucerna-VOL1-pt-it.pdf`，**5,353,932 字节**，
  SHA-256 `df3abee80c67989a9278df44782d12a4b8d612901055bd1d5aaa934719912f74`
  （D5 前 KIT 记值 6,450,106 字节——D1 旧值，已过期，以此为准）。
- render-web PDF：`A-Lucerna-VOL1-pt-it-web.pdf`，**3,299,664 字节**，
  SHA-256 `02bb6131eaab67dd6d879a50b49324eba6ba5bd01d9c77ebad9dcf8434fc40d1`
  （D5 前 KIT 记值 3,685,048 字节，见 §六）。
- 网 PDF（issues 型）：`2026-w43-pt-it.web.pdf`，**641,287 字节**，
  SHA-256 `e82569ff705c059cc6cf32488d4eacf64a3ff019ac1b9339300cb59bb9a50c07`
  （D5 前 issues 已发版 679,477 字节，`55daade4…`）。
- text.md：已发版原样 carry-over **BYTE-IDENTICAL**（SHA-256 `461229b03ab46da844298519467425b9dd2ebb3e2d42c24266dc21aa3f0c0fcb`）。
- 练习总量仍为 **150 题**，答案键仅 #137/#138 与 core 不同（KIT 已登记）。
## 六、KIT
- `patched/2026-w43-pt-it/WEEKLY-KIT.md`（closer 同步入 `production/2026-w43/2026-w43-pt-it/WEEKLY-KIT.md`）：pin 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-13–14）** 节
  （装机、基线、缺陷与修法、门禁、新交付物、导出器缺失说明）。
- 工具冻结合规（家族报告 §5.0b）：`tools/verify_textmd.py` 仅加法式 pt 表校准（ja +4 条、ko 新表），
  通用规则未动；fr/de/zh-tw 残留改前改后均为 0/0。
- KIT SHA 漂移：重建印 PDF 系统性小于 KIT 记值（`tools/webpdf.py` commit `40963281` 把 Bold/Italic
  拆成独立子集，工具链漂移、内容相同），KIT 更新以实测发运值为准纠正。
