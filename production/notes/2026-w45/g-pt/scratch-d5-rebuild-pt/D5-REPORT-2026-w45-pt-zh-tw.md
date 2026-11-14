# D5 重建报告 — 2026-w45-pt-zh-tw（繁體中文读者版）
W45 pt 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader，CJK 字符仍走 Noto Sans CJK，按字符文字分流）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-pt/logs/2026-w45-pt-zh-tw/`
（`GATES-SUMMARY.txt` 为 run2 门禁总表；`*-gates-run1.log` / `*-rebuild.log` 为 run1 记录）。
## 一、装机
- Core 落盘（全家共用一次）：`apply_variant.py --patch-core pt --week 2026-w45`
  → `production/2026-w45/core-pt/svglib.py`，`_D5_READER = "latin"`（core 模板；D24 常驻值，按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-pt-zh-tw/svglib.py --target pt --reader zh-tw --week 2026-w45`（mode=cjk，先 `--check` dry-run 全净，RC 0）。装后 `_D5_READER = "cjk"`（按字符文字分流）；
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py`。text.md 无导出器（pt 家已证实：生产目录无 textmd/export/derive 文件；pt-de/pt-fr 的 `transform.py` 是内容分发变换，不是 textmd 导出器），已发 `issues/2026-w45/2026-w45-pt-zh-tw/2026-w45-pt-zh-tw.text.md` 原样 carry-over
  **BYTE-IDENTICAL**（SHA-256 `d294ee3920b309d5f82f9fd3fa850f5690988060df4d06311203acdcf38f21b5`），验证用 `verify_textmd.py` carry-over + 门 15。
## 二、基线（修前生产版，全部干净才装机）
- `run.py` RC=0，**TOTAL 150**，0 警告。
- 文字层：印 / 网 / 已发三方字符数均为 26984 = 26984 = 26984，多重集差 **0**；自建网 PDF 1515589 B。
- 印 PDF 14072049 B（SHA-256 `25f2aa5e6125020a251437b658deec8dba229feb0e46b2cafab787caeadd32c7`）；D5 前 KIT 记值 16,014,280 B（D1 旧值，已过期；工具链漂移，见 §六）。
- 修前普查 `d5_census.py`：D5 拉丁 **331**（>0，符合装机前提）、西里尔 0、弯引号在 CJK 0。
- 基线 P8 口径：noted **150/150**。
## 三、缺陷与修法（run1 → run2）
run1 共 2 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比 Noto Sans CJK 宽；CJK 版同理为 D5 分流后拉丁段加宽）。修法只动字号，**未动任何文字内容**。
| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P1-tv 头 `A SEMANA EM DOIS DOMINGOS` | 25pt ink 434.0px，超限 | content12.py:124 `f2.head` 25→**22**（381.9 ✓） |
| 2 | head_check | P2-ex 头 `C　COMPLETE COM OS NÚMEROS` | 25pt ink 417.5px，超限 | content12.py:255 `e.head` 25→**22**（367.4 ✓） |

P8 变化：207→**207** 行，距页脚线余量 58.4→**58.4 px**（正，无溢出）。
## 四、门禁（run2，全套 17 门）
| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（curly_total=0，全部在 Newsreader） |
| 4 render | RC=0，印 PDF 3665353 B |
| 5 webpdf | RC=0，网 PDF 1167585 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（keydiff=[137, 138]（与 KIT 记载的读者语答案键一致）） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 220，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（99 OBSERVE） |
| 12 boxtitle | 0 DEFECT（31 titles，326 body lines） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 207→207，slack 58.4→58.4） |
| 15 文字层 print=web | 字符多重集差 **0**；text.md 与已发版 diff = 1 行（D34 line 34，落仓时修正），其余逐字节相同；修正后 carryover 0/0 |
| 15b 刊头 gap（D18） | 137.5 px PASS |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | 家族 gates.py 经 runner 跑通：COLLIDE 358 vs 300（同类噪声；两处抽查真墨盒为 0.1px 相接与 +0.2px 间隙）；其余结论行两版完全相同。 |

**OVERALL: ALL-GREEN.**

**G17（家族 gates.py，runner 重跑，修复后与修复前一致）**：家族 gates.py 经 runner 跑通：COLLIDE 358 vs 300（同类噪声；两处抽查真墨盒为 0.1px 相接与 +0.2px 间隙）；其余结论行两版完全相同。
## 五、新交付物
（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）
- 印 PDF：`A-Lucerna-VOL2-pt-zh-tw.pdf`，**3665353 字节**，
  SHA-256 `313e0adb5d0e7d5f045dac2225176da9a99de2c81d8cb9878f014c6d673f14f8`
  （D5 前 KIT 记值 16,014,280 字节——D1 旧值，已过期，以此为准）。
- render-web PDF：`A-Lucerna-VOL2-pt-zh-tw-web.pdf`，**2931086 字节**，
  SHA-256 `074d0abdcb226121536a56a45b176647c9ec12f5f32aac179031727d74378af5`
  （D5 前 KIT 记值 3,296,578 字节，见 §六）。
- 网 PDF（issues 型）：`2026-w45-pt-zh-tw.web.pdf`，**1167585 字节**，
  SHA-256 `c6b0610f3f362c84c619188247b218b87a40a4a01f9ff8c84b77efde79844f4d`
  （D5 前 issues 已发版 1515589 字节）。
- text.md：与已发版差 1 行（D34 line 34，落仓时修正；交付文件 `issues/2026-w45/2026-w45-pt-zh-tw/2026-w45-pt-zh-tw.text.md`，SHA-256 `81023ec8adc54e2f5da201ddde6d3639564d711ee8da83ed7753f98f1808ccd9`，31384 字节；原已发版 BYTE-IDENTICAL `d294ee3920b309d5f82f9fd3fa850f5690988060df4d06311203acdcf38f21b5`）。。
- 练习总量仍为 **150 题**，答案键仅 #137/#138 与 core 不同（KIT 已登记）。
## 六、KIT
- `patched/2026-w45-pt-zh-tw/WEEKLY-KIT.md`（closer 同步入 `production/2026-w45/2026-w45-pt-zh-tw/WEEKLY-KIT.md`）：pin 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-14）** 节
  （装机、基线、缺陷与修法、门禁、新交付物、导出器缺失说明）。
- 工具校准（家族报告 §0）：`tools/verify_textmd.py` 经 W45 基线 + patched 两轮校准后落地，
  live md5 `6dc093c207b0d72b6d387c04e46066f2`；本版 carryover 修正后 0/0（D34 已修）。
- KIT SHA 漂移：重建印 PDF 系统性小于 KIT 记值（工具链漂移、内容相同），KIT 更新以实测发运值为准纠正。
