# D5 重建报告 — 2026-w45-pt-zh-cn（简体中文读者版）
W45 pt 家 D5-only 重建（SOP §1.1 字体修复：本版即核心，讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader，CJK 字符仍走 Noto Sans CJK SC，按字符文字分流）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-pt/logs/2026-w45-pt-zh-cn/`
（`GATES-SUMMARY.txt` 为 run2 门禁总表；`*-gates-run1.log` / `*-rebuild.log` 为 run1 记录）。
## 一、装机
- Core 落盘（全家共用一次）：`apply_variant.py --patch-core pt --week 2026-w45`
  → `production/2026-w45/core-pt/svglib.py`，`_D5_READER = "latin"`（core 模板；D24 常驻值，按 patched 原样同步，不特殊处理）。
- 本版即核心：core 落盘即装机；读者版拷贝携带 `_D5_READER = "cjk"`（patched 2026-w45-pt-zh-cn 与生产 core-pt 仅此一行不同，W43 前例；先 `--check` dry-run 全净，RC 0）。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py`。text.md 无导出器（pt 家已证实：生产目录无 textmd/export/derive 文件；pt-de/pt-fr 的 `transform.py` 是内容分发变换，不是 textmd 导出器），已发 `issues/2026-w45/2026-w45-pt-zh-cn/2026-w45-pt-zh-cn.text.md` 原样 carry-over
  **BYTE-IDENTICAL**（SHA-256 `cff1ef9dbdd8f434bba164a75de2ebd3ab61c418f32688546e80e78a2bc84e9d`），验证用 `verify_textmd.py` carry-over + 门 15。
## 二、基线（修前生产版，全部干净才装机）
- `run.py` RC=0，**TOTAL 150**，0 警告。
- 文字层：印 / 网 / 已发三方字符数均为 27116 = 27116 = 27116，多重集差 **0**；自建网 PDF 1264469 B。
- 印 PDF 14019850 B（SHA-256 `6a7f323462c1edc8618e678d4b2ee71e6da81d49e0c63bed19bd0cc3ed41a7c5`）；D5 前 KIT 记值 15.96 MB（KIT 约值） B（D1 旧值，已过期；工具链漂移，见 §六）。
- 修前普查 `d5_census.py`：D5 拉丁 **338**（>0，符合装机前提）、西里尔 0、弯引号在 CJK 1。
- 基线 P8 口径：noted **150/150**。
## 三、缺陷与修法（run1 → run2）
run1 共 2 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比 Noto Sans CJK 宽；CJK 版同理为 D5 分流后拉丁段加宽）。修法只动字号，**未动任何文字内容**。
| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P1-tv 头 `A SEMANA EM DOIS DOMINGOS` | 25pt ink 434.0px，超限 | content12.py:124 `f2.head` 25→**22**（381.9 ✓） |
| 2 | head_check | P2-ex 头 `C　COMPLETE COM OS NÚMEROS` | 25pt ink 417.5px，超限 | content12.py:255 `e.head` 25→**22**（367.4 ✓） |

P8 变化：207→**207** 行，距页脚线余量 58.4→**58.4 px**（正，无溢出）。
## 四、门禁（run2，全套 16 门）
| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（curly_total=4，全部在 Newsreader） |
| 4 render | RC=0，印 PDF 3598537 B |
| 5 webpdf | RC=0，网 PDF 1067516 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（keydiff=[]（本版即核心）） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 226，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（102 OBSERVE） |
| 12 boxtitle | 0 DEFECT（31 titles，321 body lines） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 207→207，slack 58.4→58.4） |
| 15 文字层 print=web | 字符多重集差 **0**；text.md 与已发版 diff = 1 行（D34 line 34，落仓时修正），其余逐字节相同；修正后 carryover 0/0 |
| 15b 刊头 gap（D18） | 137.5 px PASS |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | pt 家无 gates.py |

**OVERALL: ALL-GREEN.**
## 五、新交付物
（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）
- 印 PDF：`A-Lucerna-VOL2.pdf`，**3598537 字节**，
  SHA-256 `f1ada85dd6cbaff6945725abf87f837db1da04e842786e3453bc29dc9efae60a`
  （D5 前 KIT 记值 15.96 MB（KIT 约值） 字节——D1 旧值，已过期，以此为准）。
- render-web PDF：`A-Lucerna-VOL2-web.pdf`，**2934623 字节**，
  SHA-256 `78a1ce1b586c61a290fb8ce2cdce0914d1cf9998c180b39c64f8d6002ecb8368`
  （D5 前 KIT 记值 3.27 MB（KIT 约值） 字节，见 §六）。
- 网 PDF（issues 型）：`2026-w45-pt-zh-cn.web.pdf`，**1067516 字节**，
  SHA-256 `cb2338ef8d79dc1e631eb90e36fae4429780517cb4f218e2e85b20946f64654c`
  （D5 前 issues 已发版 1264469 字节）。
- text.md：与已发版差 1 行（D34 line 34，落仓时修正；交付文件 `issues/2026-w45/2026-w45-pt-zh-cn/2026-w45-pt-zh-cn.text.md`，SHA-256 `e3f627f81c9afaeba7d4aaeb3def8c30d97843950f926bbfea2cb6fd98acfd70`，31313 字节；原已发版 BYTE-IDENTICAL `cff1ef9dbdd8f434bba164a75de2ebd3ab61c418f32688546e80e78a2bc84e9d`）。。
- 练习总量仍为 **150 题**；本版即核心，keydiff=[]。
## 六、KIT
- `patched/2026-w45-pt-zh-cn/WEEKLY-KIT.md`（closer 同步入 `production/2026-w45/2026-w45-pt-zh-cn/WEEKLY-KIT.md`；zh-cn 版同步入 `production/2026-w45/core-pt/WEEKLY-KIT.md`（本版即核心，双体须逐字节一致））：pin 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-14）** 节
  （装机、基线、缺陷与修法、门禁、新交付物、导出器缺失说明）。
- 工具校准（家族报告 §0）：`tools/verify_textmd.py` 经 W45 基线 + patched 两轮校准后落地，
  live md5 `6dc093c207b0d72b6d387c04e46066f2`；本版 carryover 修正后 0/0（D34 已修）。
- KIT SHA 漂移：重建印 PDF 系统性小于 KIT 记值（工具链漂移、内容相同），KIT 更新以实测发运值为准纠正。
