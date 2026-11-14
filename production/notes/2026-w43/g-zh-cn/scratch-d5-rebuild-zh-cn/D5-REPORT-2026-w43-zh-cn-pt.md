# D5 重建报告 — 2026-w43-zh-cn-pt（葡萄牙语读者版）

W43 zh-cn 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁字母由 Noto Sans CJK 改走
Newsreader；ru 读者版 Latin AND Cyrillic → Noto Sans，D26 旧分支）。施工 2026-11-14；
**不 commit、不 push**（入仓由独立重校后的 closer 做）。
工作日志：`hidden_files/d5-redo/scratch-2026-w43-zh-cn/logs/2026-w43-zh-cn-pt/`
（`GATES-SUMMARY.txt` 为门禁总表，`gates-run1.log` 为修前门禁日志）。

## 一、装机

- 本版手 port：installer 无法在 face= 引擎上运行（`cmap: pattern found 0x, expected 1`），
  改由 `scripts/d5_port_zhcn.py`（经 `scripts/install_zhcn.sh`，`logs/install.log`，
  `INSTALL DONE fail=0`）；本版 port RC=0。
- 装后 `_D5_READER = "latin"`（mode=latin variant=SC）；svglib.py 与基线差 99 行。
- 路由单元测试 `scripts/test_d5_routing_zhcn.py`：**FAILURES: 0**（66 PASS）；fix2 块保留（5 处）+ `_QUOTE_CLS` 4 处。
- 重建：`run.py` → `render.py` → `webpdf.py`（`scripts/rebuild_zhcn.sh`）→ text.md 由 textexp 导出（与 fanout `.text.md.new` BYTE-IDENTICAL）。

## 二、基线（修前生产版）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 144,208,249 字节（SHA-MISMATCH（冷缓存膨胀；fanout 64,569,287））；网 PDF 3,158,934 字节。
- 文字层：印 PDF vs 网 PDF 字符多重集差 **0**（24,560 字符）；残差 {·:164, —:1}。
- 修前普查：D5 拉丁 **466**、西里尔 0、弯引号在 CJK **0**。
- 基线 P8 口径：noted **150/150**（core 重测亦为 150/150；port 期 149/150 是 `p8.py is_header()` 误判，已 adjudicated）。

## 三、缺陷与修法（run1 → run2）

run1 共 1 项缺陷。修法只动字号/内容侧几何常数，**未动任何文字内容**（diff vs 基线源仅改动字号/常数行）；每处修复后全量重渲 + 全部门禁重跑。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | G6 occlusion | P1 版行 `TEXTOS EM CHINÊS SIMPLIFICADO　EXPLICAÇÕES EM PORTUGUÊS — A EDIÇÃO PARA OS LEITORES DE LÍNGUA PORTUGUESA`（content12.py:23，16pt sans，anchor middle x=975，y=612） | Newsreader 葡语 run x=763.6，墨水右缘 1496.6；`本周热搜`标题墨水起于 1461.5 → 重叠 35.1×9.5px。基线（单 CJK run）总宽 926.1px，右缘 1438.0，occlusion 0 flags——D5 引起（整行 926.1→1044.1px）。PIL 实测：15pt → 右缘 1464.4（仍盖 −2.9px）；**14.5pt → 右缘 1448.1，余量 13.4px**；14pt → 1431.8（29.7px） | `content12.py:23` 16→**14.5**（15pt 不够——实测，非假设） |

P8 变化：856 节点（修前修后同值），距页脚线余量 34.22px（正，无溢出）。

## 四、门禁（run2，全套 17 门 + D18，ALL-GREEN）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 警告 |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：lat 0 / cyr 0 / curly_cjk 0 / noto 0 |
| 4 render | RC=0，印 PDF 55,564,053 B |
| 5 webpdf | RC=0，网 PDF 2,908,240 B（< 7 MB） |
| 6 occlusion | 0 flags（selftest 全过） |
| 7 p8 extract | noted 150/150（含 [108]） |
| 8 p8 compare | **CLEAN**：core 150 noted vs 本版 150 noted，missing=[] extra_count=0 keydiff=[]（[108] 两边都在，无 EXTRA_ONLY、无 SHORT；不切 canonical） |
| 9 freeze（基线 8/8 + diff vs base） | 基线 8/8；新增 CJK 字符 **0**（新增拉丁 strings 278，run 拆分所致；对照是 base 修前生产版，不是 core） |
| 10 spill | 0 SPILL（33 boxes，94 candidates） |
| 11 boxtitle | 0 DEFECT（41 titles，457 body lines，1 marginal） |
| 12 edge | 0 TOUCH，0 NEAR（8 页） |
| 13 creambox | PASS，0 defects |
| 14 文字层 print=web | 字符多重集差 **0**（各 24,560 字符） |
| 15a text.md | 与 fanout **BYTE-IDENTICAL**（43,589 B） |
| 15b 共享 verify_textmd | **N/A**：共享工具 `verify_textmd.py` 的 READER_TABLES 无 `pt` 表（rc=2），工具缺口，非本版缺陷；基线对照亦无法跑。按 D27 口径验收：15a BYTE-IDENTICAL + 15c 915/915 UNEXPECTED 0 + 全文通读（复校）。pt 表标定是工具工作，已记入家族报告 §8 待协调员/工具方处理。 |
| 15c native verifier | PASS：915 entries vs ref 915，ADOPT 0，UNEXPECTED 0 |
| 16 census_quotes | 0 defective |
| 17 家族 gates.py | 本家无 gates.py（N/A） |
| D18 刊头 | gap 298.2px PASS |

**OVERALL: ALL-GREEN.**

## 五、新交付物

（scratch 内，closer 拷入 issues 时网 PDF 改名 `2026-w43-zh-cn-pt.pdf`；production 内印 PDF 沿用 KIT 登记名 `Lucerna-VOL1-PT.pdf`）

- 印 PDF：`Lucerna-VOL1-PT.pdf`，**55,564,053 字节**，
  SHA-256 `eecb50bce0fdda297aa91564473495d66232cc5cedb8867aaddf8464bfcbff6f`
  （D5 前 KIT 值印 67,307,684 字节、网 3,263,463 字节（`3fb977b1…`））。
- 网 PDF：`Lucerna-VOL1-PT-web.pdf`，**2,908,240 字节**，
  SHA-256 `2a00a18ead9082f8574d70d77aa9d9546d1076d4bb85e9fef389f33e7473d032`
  （< 7 MB）。
- text.md：导出与 fanout **BYTE-IDENTICAL**
  （SHA-256 `05e8604af2aa0eb555f3b3ca31cb3d57a5fc0576a041d1214d3f52c60e0e2326`，43,589 B）。
- 练习总量仍为 **150 题**。

## 六、KIT

- `production/2026-w43/2026-w43-zh-cn-pt/WEEKLY-KIT.md`：交付物/针脚行更新为 D5 值（新 SHA + 字节数）；
  文末追加 **D5 重建记录（2026-11-14）**（装机、基线、缺陷与修法、门禁 ALL-GREEN、新交付物）。
