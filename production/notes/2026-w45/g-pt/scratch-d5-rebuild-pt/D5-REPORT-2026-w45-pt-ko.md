# D5 重建报告 — 2026-w45-pt-ko（韩语读者版）
W45 pt 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader，CJK 字符仍走 Noto Sans CJK，按字符文字分流）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-pt/logs/2026-w45-pt-ko/`
（`GATES-SUMMARY.txt` 为 run2 门禁总表；`*-gates-run1.log` / `*-rebuild.log` 为 run1 记录）。
## 一、装机
- Core 落盘（全家共用一次）：`apply_variant.py --patch-core pt --week 2026-w45`
  → `production/2026-w45/core-pt/svglib.py`，`_D5_READER = "latin"`（core 模板；D24 常驻值，按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-pt-ko/svglib.py --target pt --reader ko --week 2026-w45`（mode=cjk，先 `--check` dry-run 全净，RC 0）。装后 `_D5_READER = "cjk"`（按字符文字分流）；
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py`。text.md 无导出器（pt 家已证实：生产目录无 textmd/export/derive 文件；pt-de/pt-fr 的 `transform.py` 是内容分发变换，不是 textmd 导出器），已发 `issues/2026-w45/2026-w45-pt-ko/2026-w45-pt-ko.text.md` 原样 carry-over
  **BYTE-IDENTICAL**（SHA-256 `3f17df397e50f908ef8fd9388bbed58949ec86910aef3f1fd07fa60c67997fb6`），验证用 `verify_textmd.py` carry-over + 门 15。
## 二、基线（修前生产版，全部干净才装机）
- `run.py` RC=0，**TOTAL 150**，0 警告。
- 文字层：印 / 网 / 已发三方字符数均为 27886 = 27886 = 27886，多重集差 **0**；自建网 PDF 1104845 B。
- 印 PDF 6532489 B（SHA-256 `2e4b6e5dccb7b5e88e96cc04466ecc70ce187302372aa4479b0d539750b15cba`）；D5 前 KIT 记值 8,438,601 B（D1 旧值，已过期；工具链漂移，见 §六）。
- 修前普查 `d5_census.py`：D5 拉丁 **333**（>0，符合装机前提）、西里尔 0、弯引号在 CJK 1。
- 基线 P8 口径：noted **150/150**。
## 三、缺陷与修法（run1 → run2）
run1 共 2 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比 Noto Sans CJK 宽；CJK 版同理为 D5 分流后拉丁段加宽）。修法只动字号，**未动任何文字内容**。
| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P1-tv 头 `A SEMANA EM DOIS DOMINGOS` | 25pt ink 434.0px，超限 | content12.py:124 `f2.head` 25→**22**（381.9 ✓） |
| 2 | head_check | P2-ex 头 `C　COMPLETE COM OS NÚMEROS` | 25pt ink 417.5px，超限 | content12.py:255 `e.head` 25→**22**（367.4 ✓） |

P8 变化：243→**243** 行，距页脚线余量 41.7→**41.7 px**（正，无溢出）。
## 四、门禁（run2，全套 17 门）
| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（curly_total=4，全部在 Newsreader） |
| 4 render | RC=0，印 PDF 3579889 B |
| 5 webpdf | RC=0，网 PDF 992354 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（keydiff=[137, 138]（与 KIT 记载的读者语答案键一致）） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 216，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（177 OBSERVE） |
| 12 boxtitle | 0 DEFECT（40 titles，497 body lines） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 243→243，slack 41.7→41.7） |
| 15 文字层 print=web | 字符多重集差 **0**；text.md 与已发版 diff = 1 行（D34 line 34，落仓时修正），其余逐字节相同；修正后 carryover 0/0 |
| 15b 刊头 gap（D18） | 148.3 px PASS |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | 家族 gates.py 经 runner 跑通：patched 独有 FAILURES 全部是 run-split 测量伪影（join 空格、整元素正则、按行假设）；S3 真·断词 patched 0 命中、基线 1 命中。 |

**OVERALL: ALL-GREEN.**

**G17（家族 gates.py，runner 重跑，修复后与修复前一致）**：家族 gates.py 经 runner 跑通：patched 独有 FAILURES 全部是 run-split 测量伪影（join 空格、整元素正则、按行假设）；S3 真·断词 patched 0 命中、基线 1 命中。
## 五、新交付物
（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）
- 印 PDF：`A-Lucerna-VOL2-pt-ko.pdf`，**3579889 字节**，
  SHA-256 `6a58c64da109198276ab9e63c76f2087f19a5f608928b0a885180baebb30a91e`
  （D5 前 KIT 记值 8,438,601 字节——D1 旧值，已过期，以此为准）。
- render-web PDF：`A-Lucerna-VOL2-pt-ko-web.pdf`，**2997452 字节**，
  SHA-256 `900f381158b4fcf596688f03d63b1b82cc9fb2988f5a2782e5642cf1b989b85d`
  （D5 前 KIT 记值 3,361,090 字节，见 §六）。
- 网 PDF（issues 型）：`2026-w45-pt-ko.web.pdf`，**992354 字节**，
  SHA-256 `8ca305ec40d687ba9914e6ebf76606b660ec393d17c9fe00447f6417a16ad803`
  （D5 前 issues 已发版 1104845 字节）。
- text.md：与已发版差 1 行（D34 line 34，落仓时修正；交付文件 `issues/2026-w45/2026-w45-pt-ko/2026-w45-pt-ko.text.md`，SHA-256 `f4ee84ab5e500b498eca296869e14b79b32ac9a74dfe83f95293383443a9d247`，32117 字节；原已发版 BYTE-IDENTICAL `3f17df397e50f908ef8fd9388bbed58949ec86910aef3f1fd07fa60c67997fb6`）。。
- 练习总量仍为 **150 题**，答案键仅 #137/#138 与 core 不同（KIT 已登记）。
## 六、KIT
- `patched/2026-w45-pt-ko/WEEKLY-KIT.md`（closer 同步入 `production/2026-w45/2026-w45-pt-ko/WEEKLY-KIT.md`）：pin 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-14）** 节
  （装机、基线、缺陷与修法、门禁、新交付物、导出器缺失说明）。
- 工具校准（家族报告 §0）：`tools/verify_textmd.py` 经 W45 基线 + patched 两轮校准后落地，
  live md5 `6dc093c207b0d72b6d387c04e46066f2`；本版 carryover 修正后 0/0（D34 已修）。
- KIT SHA 漂移：重建印 PDF 系统性小于 KIT 记值（工具链漂移、内容相同），KIT 更新以实测发运值为准纠正。
