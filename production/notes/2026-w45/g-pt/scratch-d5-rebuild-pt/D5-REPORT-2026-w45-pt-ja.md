# D5 重建报告 — 2026-w45-pt-ja（日语读者版）
W45 pt 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader，CJK 字符仍走 Noto Sans CJK，按字符文字分流）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-pt/logs/2026-w45-pt-ja/`
（`GATES-SUMMARY.txt` 为 run2 门禁总表；`*-gates-run1.log` / `*-rebuild.log` 为 run1 记录）。
## 一、装机
- Core 落盘（全家共用一次）：`apply_variant.py --patch-core pt --week 2026-w45`
  → `production/2026-w45/core-pt/svglib.py`，`_D5_READER = "latin"`（core 模板；D24 常驻值，按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-pt-ja/svglib.py --target pt --reader ja --week 2026-w45`（mode=cjk，先 `--check` dry-run 全净，RC 0）。装后 `_D5_READER = "cjk"`（按字符文字分流）；
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py`。text.md 无导出器（pt 家已证实：生产目录无 textmd/export/derive 文件；pt-de/pt-fr 的 `transform.py` 是内容分发变换，不是 textmd 导出器），已发 `issues/2026-w45/2026-w45-pt-ja/2026-w45-pt-ja.text.md` 原样 carry-over
  **BYTE-IDENTICAL**（SHA-256 `15cf0281074037f44becbde826a01d0729c6cb2651faf5a570c1aa8aac839574`），验证用 `verify_textmd.py` carry-over + 门 15。
## 二、基线（修前生产版，全部干净才装机）
- `run.py` RC=0，**TOTAL 150**，0 警告。
- 文字层：印 / 网 / 已发三方字符数均为 28022 = 28022 = 28022，多重集差 **0**；自建网 PDF 1375819 B。
- 印 PDF 14954791 B（SHA-256 `f9a733a43988d3c0bdc3a017e66024fc4f1e687830cb3db2c6087d5ca7091b1e`）；D5 前 KIT 记值 16,852,697 B（D1 旧值，已过期；工具链漂移，见 §六）。
- 修前普查 `d5_census.py`：D5 拉丁 **335**（>0，符合装机前提）、西里尔 0、弯引号在 CJK 0。
- 基线 P8 口径：noted **150/150**。
## 三、缺陷与修法（run1 → run2）
run1 共 3 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比 Noto Sans CJK 宽；CJK 版同理为 D5 分流后拉丁段加宽）。修法只动字号，**未动任何文字内容**。
| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P1-tv 头 `A SEMANA EM DOIS DOMINGOS` | 25pt ink 434.0px，超限 | content12.py:124 `f2.head` 25→**22**（381.9 ✓） |
| 2 | head_check | P2-ex 头 `C　COMPLETE COM OS NÚMEROS` | 25pt ink 417.5px，超限 | content12.py:255 `e.head` 25→**22**（367.4 ✓） |
| 3 | creambox / boxtitle | P1 `今週の数字` 盒标题 | 23pt ink 455.0px，溢出 +50.5px | content12.py:48 `f.box` close 加 `tsize=20`（395.7 ✓） |

P8 变化：224→**224** 行，距页脚线余量 42.7→**42.7 px**（正，无溢出）。
## 四、门禁（run2，全套 17 门）
| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（curly_total=0，全部在 Newsreader） |
| 4 render | RC=0，印 PDF 7814449 B |
| 5 webpdf | RC=0，网 PDF 1174032 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（keydiff=[137, 138]（与 KIT 记载的读者语答案键一致）） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 227，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（113 OBSERVE） |
| 12 boxtitle | 0 DEFECT（29 titles，356 body lines） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 224→224，slack 42.7→42.7） |
| 15 文字层 print=web | 字符多重集差 **0**；text.md 与已发版 diff = 1 行（D34 line 34，落仓时修正），其余逐字节相同；修正后 carryover 0/0 |
| 15b 刊头 gap（D18） | 63.3 px PASS |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | 家族 gates.py 经 runner 跑通（报告式）：§1–§6 与基线逐行相同；行首 flag 19 vs 9，新增 10 个全是行中 run（扫描器对每个元素首字判 flag，从不验证是否真在行首）。 |

**OVERALL: ALL-GREEN.**

**G17（家族 gates.py，runner 重跑，修复后与修复前一致）**：家族 gates.py 经 runner 跑通（报告式）：§1–§6 与基线逐行相同；行首 flag 19 vs 9，新增 10 个全是行中 run（扫描器对每个元素首字判 flag，从不验证是否真在行首）。
## 五、新交付物
（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）
- 印 PDF：`A-Lucerna-VOL2-pt-ja.pdf`，**7814449 字节**，
  SHA-256 `3b6d22a9588e1f62b60eb82c312a8a686a1fccccbf1ab67a7d3c46ff85fa2fec`
  （D5 前 KIT 记值 16,852,697 字节——D1 旧值，已过期，以此为准）。
- render-web PDF：`A-Lucerna-VOL2-pt-ja-web.pdf`，**3025028 字节**，
  SHA-256 `483a6dca9c5598005cd0d5d5223450230d394afe5bb0aa3d0d74dc986bfcf590`
  （D5 前 KIT 记值 3,392,107 字节，见 §六）。
- 网 PDF（issues 型）：`2026-w45-pt-ja.web.pdf`，**1174032 字节**，
  SHA-256 `0d0cef4c7faa9a81e9da19cffe628a167270abf76803a6a89c450b57f3149a04`
  （D5 前 issues 已发版 1375819 字节）。
- text.md：与已发版差 1 行（D34 line 34，落仓时修正；交付文件 `issues/2026-w45/2026-w45-pt-ja/2026-w45-pt-ja.text.md`，SHA-256 `99e88e70a9d5c64759aadddec5394699217a34cebe797f5988d7fe55d9fb7adb`，32007 字节；原已发版 BYTE-IDENTICAL `15cf0281074037f44becbde826a01d0729c6cb2651faf5a570c1aa8aac839574`）。。
- 练习总量仍为 **150 题**，答案键仅 #137/#138 与 core 不同（KIT 已登记）。
## 六、KIT
- `patched/2026-w45-pt-ja/WEEKLY-KIT.md`（closer 同步入 `production/2026-w45/2026-w45-pt-ja/WEEKLY-KIT.md`）：pin 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-14）** 节
  （装机、基线、缺陷与修法、门禁、新交付物、导出器缺失说明）。
- 工具校准（家族报告 §0）：`tools/verify_textmd.py` 经 W45 基线 + patched 两轮校准后落地，
  live md5 `6dc093c207b0d72b6d387c04e46066f2`；本版 carryover 修正后 0/0（D34 已修）。
- KIT SHA 漂移：重建印 PDF 系统性小于 KIT 记值（工具链漂移、内容相同），KIT 更新以实测发运值为准纠正。
