# D5 重建报告 — 2026-w45-pt-nl（荷兰语读者版）
W45 pt 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走 Newsreader）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-pt/logs/2026-w45-pt-nl/`
（`GATES-SUMMARY.txt` 现为 F-A fix 门禁总表；run2 总表存于 `hidden_files/d5-redo/scratch-2026-w45-pt/fix/logs/run2-summaries/`；`*-gates-run1.log` / `*-rebuild.log` 为 run1 记录）。
## 一、装机
- Core 落盘（全家共用一次）：`apply_variant.py --patch-core pt --week 2026-w45`
  → `production/2026-w45/core-pt/svglib.py`，`_D5_READER = "latin"`（core 模板；D24 常驻值，按 patched 原样同步，不特殊处理）。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-pt-nl/svglib.py --target pt --reader nl --week 2026-w45`（先 `--check` dry-run 全净，RC 0）。装后 `_D5_READER = "latin"`；
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py`。text.md 无导出器（pt 家已证实：生产目录无 textmd/export/derive 文件；pt-de/pt-fr 的 `transform.py` 是内容分发变换，不是 textmd 导出器），已发 `issues/2026-w45/2026-w45-pt-nl/2026-w45-pt-nl.text.md` 原样 carry-over（F-A fix 后：与已发版差恰好 1 行，见 §七；新 text.md SHA-256 `f701243be24b20039981ba255edd6d4393d09b576a9a6d4861c26bb605e7dabe`，32119 字节；run2 值为 BYTE-IDENTICAL，9a198ec213310744…），验证用 `verify_textmd.py` carry-over + 门 15。
## 二、基线（修前生产版，全部干净才装机）
- `run.py` RC=0，**TOTAL 150**，0 警告。
- 文字层：印 / 网 / 已发三方字符数均为 33289 = 33289 = 33289，多重集差 **0**；自建网 PDF 841760 B。
- 印 PDF 2792783 B（SHA-256 `a584534a0bc88f8fac5a68735cce37e7a408a2418647b670b0f72abd180cb9c0`）；D5 前 KIT 记值 3,510,712 B（D1 旧值，已过期；工具链漂移，见 §六）。
- 修前普查 `d5_census.py`：D5 拉丁 **503**（>0，符合装机前提）、西里尔 0、弯引号在 CJK 0。
- 基线 P8 口径：noted **150/150**。
## 三、缺陷与修法（run1 → run2）
run1 共 6 项缺陷，全部为 D5 字体加宽引起（拉丁粗体在 Newsreader SemiBold 下比 Noto Sans CJK 宽；CJK 版同理为 D5 分流后拉丁段加宽）。修法只动字号，**未动任何文字内容**。
| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | head_check | P1-tv 头 `A SEMANA EM DOIS DOMINGOS` | 25pt ink 434.0px，超限 | content12.py:124 `f2.head` 25→**22**（381.9 ✓） |
| 2 | head_check | P2-ex 头 `C　COMPLETE COM OS NÚMEROS` | 25pt ink 417.5px，超限 | content12.py:255 `e.head` 25→**22**（367.4 ✓） |
| 3 | creambox / boxtitle | P1 `CIJFERS` 盒标题 | 23pt ink 443.2px，溢出 +38.5px | content12.py:48 `f.box` close 加 `tsize=20`（385.4 ✓） |
| 4 | creambox / boxtitle | P1 `IN DEZE EDITIE` | 24pt ink 421.9px，溢出 +21.1px | content12.py:89 `p.text` 24→**22**（386.7 ✓） |
| 5 | creambox / boxtitle | P1 `KORTOM` | 24pt ink 447.0px，溢出 +44.4px | content12.py:131 `p.text` 24→**21**（391.1 ✓） |
| 6 | creambox / boxtitle | P7 `WOORD VAN DE WEEK` | 23pt ink 449.8px，溢出 +45.1px | content7.py:84 `p.text` 23→**20**（391.1 ✓） |

P8 变化：256→**256** 行，距页脚线余量 47.4→**47.4 px**（正，无溢出）。
## 四、门禁（run2，全套 17 门）
| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、弯引号在 CJK 0（curly_total=2，全部在 Newsreader） |
| 4 render | RC=0，印 PDF 2281094 B（run2 2281090 B） |
| 5 webpdf | RC=0，网 PDF 762459 B（run2 762454 B；< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**（keydiff=[137, 138]（与 KIT 记载的读者语答案键一致）） |
| 9 freeze baseline | 8/8（core SVG 未被重建改动） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 245（run2 243；+2 为新 F-A 词 sair/cair/saíram/caíram 的新增 run strings，预期内），run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 SPILL（57 OBSERVE） |
| 12 boxtitle | 0 DEFECT（25 titles，258 body lines） |
| 13 edge | 0 TOUCH，0 NEAR（8 页） |
| 14 creambox | PASS，0 defects（P8 256→256，slack 47.4→47.4） |
| 15 文字层 print=web | 字符多重集差 **0**（print=web 33285 字符）；print 与已发版多重集差 **22** = 恰好 F-A 字符差（对照为修前已发版）（9 新 vs 13 旧，`pdftotext` 计数核实）；text.md 与已发版 diff = 2 行（F-A line 352 + D34 line 34，落仓时修正），其余逐字节相同；修正后 carryover 0/0 |
| 15b 刊头 gap（D18） | 31.6 px PASS |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | 家族 gates.py 经 runner 跑通：footer_ok=False ×8 两版相同；same-baseline 紧邻 flag 15 vs 13（同类，全部正间隙；G6 为准 0 flag）。 |

**OVERALL: ALL-GREEN.**

**F-A fix（2026-11-14，D36）门禁**：fix 重跑与 run2 一致（见 §七）；fix verdict 天生带 15a 红（对照是已发版），验收以 diff 内容为准——text.md 与已发版 diff = 2 行（F-A line 352 + D34 line 34，落仓时修正），其余逐字节相同；修正后 carryover 0/0；print-vs-issued 多重集差 22（对照为修前已发版）恰好为 F-A 字符差。

**G17（家族 gates.py，runner 重跑，修复后与修复前一致）**：家族 gates.py 经 runner 跑通：footer_ok=False ×8 两版相同；same-baseline 紧邻 flag 15 vs 13（同类，全部正间隙；G6 为准 0 flag）。
## 五、新交付物
（scratch 内，closer 拷入 issues 时网 PDF 改名 `<slug>.pdf`）
- 印 PDF：`A-Lucerna-VOL2-pt-nl.pdf`，**2281094 字节**，
  SHA-256 `5d8acc05552efd78f0c9ff94861db95d32b13fbedf7ec8ea8343045273731264`
  （D5 前 KIT 记值 3,510,712 字节——D1 旧值，已过期，以此为准）。
- render-web PDF：`A-Lucerna-VOL2-pt-nl-web.pdf`，**3124714 字节**，
  SHA-256 `2b76d2e60aa843f7ae92f1f6e3a17a36b29687d1ac372eed90841e27fbaec8cc`
  （D5 前 KIT 记值 3,500,683 字节，见 §六）。
- 网 PDF（issues 型）：`2026-w45-pt-nl.web.pdf`，**762459 字节**，
  SHA-256 `26e41b05538092f8c4cfbe4c704f97e11211257aa2752cfb7b52e39fef8f20ce`
  （D5 前 issues 已发版 841760 字节）。
- text.md：与已发版差 2 行（F-A line 352 + D34 line 34，落仓时修正，见 §七；交付文件 `issues/2026-w45/2026-w45-pt-nl/2026-w45-pt-nl.text.md`，SHA-256 `296610dc98660ec5c5ffef035348e4630a8009e9073f55254c7a5316561262b9`，32118 字节；fix 新文件 `fix/2026-w45-pt-nl/2026-w45-pt-nl.text.md.new` 为叠加前值，SHA-256 `f701243be24b20039981ba255edd6d4393d09b576a9a6d4861c26bb605e7dabe`，32119 字节；run2 值为 BYTE-IDENTICAL `9a198ec213310744628a427449e8cbe1c67c71c49ca7c83ff1f67fcbd3ed7589`）。。
- 练习总量仍为 **150 题**，答案键仅 #137/#138 与 core 不同（KIT 已登记）。
## 六、KIT
- `patched/2026-w45-pt-nl/WEEKLY-KIT.md`（closer 同步入 `production/2026-w45/2026-w45-pt-nl/WEEKLY-KIT.md`）：pin 节追加 D5 交付物行
  （新 SHA + 字节数，注明 D5 前值）；文末追加 **D5 rebuild（2026-11-14）** 节
  （装机、基线、缺陷与修法、门禁、新交付物、导出器缺失说明）。
- F-A fix（2026-11-14，D36）：KIT pin 行与 New deliverables 行已更新为 fix 值（印/网 PDF 字节+SHA、新 text.md SHA，不再写 BYTE-IDENTICAL）；文末追加 **F-A fix（2026-11-14，D36）** 节。已修复 `content7.py` 已同步进 `production/2026-w45/2026-w45-pt-nl/content7.py` 与 `patched/2026-w45-pt-nl/content7.py`（`diff -q` 三边一致）。
- 工具校准（家族报告 §0）：`tools/verify_textmd.py` 经 W45 基线 + patched 两轮校准后落地，
  live md5 `6dc093c207b0d72b6d387c04e46066f2`；本版 carryover 修正后 0/0（D34 已修）。
- KIT SHA 漂移：重建印 PDF 系统性小于 KIT 记值（工具链漂移、内容相同），KIT 更新以实测发运值为准纠正。

## 七、F-A 修复（2026-11-14，D36）
重校结论 NOT PASSED，finding F-A：P7 B1 桥句称 chegar/dormir（chegou, dormiu）带重音——两词均无重音。修复：`content7.py:35`（nl 为 `b.expl`）最小改动，重音归属改到 sair/cair（saíram, caíram），句式与余词不动；PT 原文行 34 不动；其余 5 版不动。
- 改前/改后见 `FAMILY-W45-PT-FIX.md` §2（逐字对照）。
- 重渲（run → render → webpdf）+ 全部门禁重跑：run TOTAL 150，0 警告；其余门与 run2 一致，惟门 10 新增拉丁 strings 245（run2 243）与门 15 print-vs-issued 差 22（见 §四）为 F-A 内容差本身。G17 runner（fix）：与 builder patched 侧 runner 日志逐字节一致（路径归一化后）。
- P7 目检（印 PDF 100 dpi 渲染）：新桥句完整呈现，无溢出/碰撞；p8 150/150 CLEAN。
- 交付物见 §五（fix 值）；新 text.md 为已发版 text.md 的 2 行替换（line 352 F-A + line 34 D34），pt 无 text.md 导出器（见 KIT Exporter note），不得从 PDF 反向抽取。
- F-B（D34 typo，11 份已发 `.text.md` line 34 `domingo 15` → `8`）已由 closer 落仓时在交付文件上叠加修正并重 pin（交付 SHA 见 §五与 KIT D5-pin 行；fix 新文件 SHA 为叠加前的值）。
