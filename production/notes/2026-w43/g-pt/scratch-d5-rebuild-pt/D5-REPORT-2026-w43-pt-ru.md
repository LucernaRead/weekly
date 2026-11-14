# D5 重建报告 — 2026-w43-pt-ru（俄语读者版）
W43 pt 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader）。施工 2026-11-13–14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-pt/logs/2026-w43-pt-ru/`
（`GATES-SUMMARY.txt` 为 run2 门禁总表；`*-gates-run1.log` / `*-rebuild.log` 为 run1 记录）。
## 一、装机
- Core 落盘（全家共用一次）：`apply_variant.py --patch-core pt --week 2026-w43`
  → `production/2026-w43/core-pt/svglib.py`，`_D5_READER = "latin"`（core 模板；与 es 家 core 同型）。
- 本版安装：`apply_variant.py --svglib patched/2026-w43-pt-ru/svglib.py --target pt
  --reader ru --week 2026-w43`（先 `--check` dry-run 全净，RC 0）。装后 `_D5_READER = "ru"`；装后 svglib `_D5_READER = "ru"`，字体索引为 `_sc_index`（SC 字体）；与 core-pt 模板差 `_D5_READER` 与读者字体索引（读者相关，预期内）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py`。text.md 无导出器（pt 家已证实；
  `ru_textmd.py` 试跑差 757 行），已发 `issues/2026-w43/2026-w43-pt-ru/2026-w43-pt-ru.text.md` 原样 carry-over
  **BYTE-IDENTICAL**（SHA-256 `a6f97d1180377b6f6953afca12781bd21991730090bd73d6850400d62053a9d9`），验证用 `verify_textmd.py` carry-over + 门 15。
## 二、基线（修前生产版，全部干净才装机）
- `run.py` RC=0，**TOTAL 150**，0 警告。
- 文字层：印 / 网 / 已发三方字符数均为 43,357 = 43,357 = 43,357，多重集差 **0**；自建网 PDF 769,137 B。
- 印 PDF 5,862,783 B（SHA-256 `3371066e62693ed4aa6897587af3727f8b8479e513e7fc2345cee54791b2e5b1`，前 8 位 `3371066e`）；D5 前 KIT 记值 6,380,386 B（D1 旧值，已过期；工具链漂移，见 §六）。
- 修前普查 `d5_census.py`：D5 拉丁 **346**（>0，符合装机前提）、西里尔 256、弯引号在 CJK 0。
- 基线 P8 口径：noted **150/150**。
## 三、缺陷与修法（run1 → run2）
run1 **0 项缺陷**：本版无二次修复（ru 讲解层较窄，Noto Sans 下两头已通过；D5 安装器改动已落盘，
文字零改动）。

P8 变化：215→**215** 行，距页脚线余量 40.7→**40.7 px**（正，无溢出）。
## 四、门禁（run2，全套 16 门）
| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0 （curly_total=0） |
| 4 render | RC=0，印 PDF 5,626,667 B |
| 5 webpdf | RC=0，网 PDF 894,153 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（keydiff=[137, 138]——与 KIT 记载的读者语答案键一致） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 170，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（57 OBSERVE） |
| 12 boxtitle | 0 DEFECT（30 titles，300 body lines） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 215→215，slack 40.7→40.7） |
| 15 文字层 print=web | 字符多重集差 **0**；textmd carryover **PASS 0/0**（svg 5144 = md 5144 tokens） |
| 15b 刊头 gap（D18） | 88.4 px PASS |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | pt 家无 gates.py |

**OVERALL: ALL-GREEN.**
## 五、新交付物
（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）
- 印 PDF：`A-Lucerna-VOL1-pt-ru.pdf`，**5,626,667 字节**，
  SHA-256 `e2830aeb4ea28d2bb5ecd9deed1e588f2038e7978c967f35d35f66401973a6ad`
  （D5 前 KIT 记值 6,380,386 字节——D1 旧值，已过期，以此为准）。
- render-web PDF：`A-Lucerna-VOL1-pt-ru-web.pdf`，**3,331,472 字节**，
  SHA-256 `9053be6a3f27cd94033097a18a23a891ebf7f43be4aed25d2d7edde406a46318`
  （D5 前 KIT 记值 3,729,701 字节，见 §六）。
- 网 PDF（issues 型）：`2026-w43-pt-ru.web.pdf`，**894,153 字节**，
  SHA-256 `0511cef1e6dbe15e09b2be9bbc02b1936305ead22a15660aec5f6b49e1dd856b`
  （D5 前 issues 已发版 732,214 字节，`2b2b09fb…`）。
- text.md：已发版原样 carry-over **BYTE-IDENTICAL**（SHA-256 `a6f97d1180377b6f6953afca12781bd21991730090bd73d6850400d62053a9d9`）。
- 练习总量仍为 **150 题**，答案键仅 #137/#138 与 core 不同（KIT 已登记）。
## 六、KIT
- `patched/2026-w43-pt-ru/WEEKLY-KIT.md`（closer 同步入 `production/2026-w43/2026-w43-pt-ru/WEEKLY-KIT.md`）：pin 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-13–14）** 节
  （装机、基线、缺陷与修法、门禁、新交付物、导出器缺失说明）。
- 工具冻结合规（家族报告 §5.0b）：`tools/verify_textmd.py` 仅加法式 pt 表校准（ja +4 条、ko 新表），
  通用规则未动；fr/de/zh-tw 残留改前改后均为 0/0。
- KIT SHA 漂移：重建印 PDF 系统性小于 KIT 记值（`tools/webpdf.py` commit `40963281` 把 Bold/Italic
  拆成独立子集，工具链漂移、内容相同），KIT 更新以实测发运值为准纠正。
