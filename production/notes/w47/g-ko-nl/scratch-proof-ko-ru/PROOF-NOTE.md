# PROOF-NOTE — W47 ko-ru (2026-w47-ko-ru), proof1 独立复校

- **结论：(a) 定稿零缺陷。** 全部机械门禁独立重跑通过；150 题三源手验全过；8 页逐页渲染目视零问题；#137 已裁决属实（提取器 artefact，非内容错误）；无新缺陷。
- 复校员与构建者/fan-out agent 不同人；全部工作在 goals 侧工作区完成，未动生产目录，未 commit、未 push。
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-ru/`
- 门禁产物与日志：同目录 `GATE-LOG.md`；本文件为结论文件。

## 1. SHA 复核（复核前 / 复核后各测一次，全部未变）

| 文件 | 字节 | SHA-256（复核前 = 复核后） |
|---|---|---|
| 印 `Lucerna-VOL4-KO-RU.pdf` | 44,014,545 | `bcc7eedf64d6d4ac4056e32eb86c40059b20f162dfaa0bd39346df8fa580ffaa` ✓ 与任务给定一致 |
| 网 `Lucerna-VOL4-KO-RU-web.pdf` | 3,985,120 | `2d553d300fe83f71f3f0cf262cce371754f0b2844b1bf18a0603dced99c062f9` ✓ |
| text `2026-w47-ko-ru.text.md` | 37,195 | `956b6fccf1d67c0c67159c5525004bda504bf4e56a3e90488bd580a3aed19771` ✓ |
| `ABSTRACT.txt` | 500 | `c0d5fa6ffcc91fde62ef5fc376fa1a8e80eb1e984492339f6df46f732ae7b214` ✓ |
| core-ko 印 `Lucerna-VOL4.pdf` | 46,232,227 | `53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27`（复核前后未变） |
| core-ko 网 `Lucerna-VOL4-web.pdf` | 4,232,878 | `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7`（未变） |
| core-ko text | 34,606 | `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a`（未变） |

## 2. Carry-forward #137 —— 已裁决属实，不计缺陷

任务要求的核实项逐一独立复现，全部属实：

- keycheck 独立重跑（自写 `keycheck-proof.py`，REG 取自本版源码、SVG keys 取自自提的 `p8-ru.json`）：**REG 150、SVG keys 150、exact 148、trunc-ok 1（#150 `✓`）、BAD 1（#137）**，与 FANOUT-REPORT-ko3.md 完全一致。
- #137 三源一致（内容完整）：
  1. **源码** `edition/content8.py:69`：`f.ex("A2", "перевод", "22 ноября — День кимчхи.", "См. страницу 2", …)`；
  2. **P8 SVG** `svg/p8-siheom.svg` 文本元素（x=1439.5, y=2059.8）：`137. 22 ноября — День кимчхи. — См. страницу 2`；
  3. **交付印 PDF 文字层**（`pdftotext` 实测）：同句逐字出现；网 PDF 文字层与印 PDF 逐字节一致，故网面亦完整。
  - P8 渲染目视亦确认该行完整无缺。
- 机制已核对源码：`tools/p8.py` `detect_note`（约 line 149–150）对含 ` — ` 的段按**第一个** ` — ` 切分，`137. 22 ноября — День кимчхи. — См. страницу 2` 的 key 被读作 `22 ноября`——因为俄语 key 本身含 em-dash 系词。俄语标点正确，**不改**。内容层面 keycheck 为 150/150。
- 记录为**已裁决、不计缺陷**。

## 3. 门禁汇总（全部独立重跑，见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| run.py（系统 python3，scratch 副本） | rc=0，0 FLOW OVERFLOW / HEAD TOO WIDE，TOTAL 150（A2 51 / B1 72 / B2 27；每页 10/18/18/18/18/18/12/38） |
| freeze baseline（系统 python3，Pillow 10.2.0） | **8/8 字节一致**，rc=0 |
| freeze diff vs core | added CJK **7，全部 U+3000**（footer 分隔符），rc=0 |
| occlusion audit（含 selftest） | selftest 6 类全触发、干净对照静默；本版 **0 flags** |
| p8.py extract | **150/150 noted** |
| p8.py compare vs core | **CLEAN**，missing=[]，keydiff=[137, 138]（E 组重定向，预期） |
| keycheck | 148 exact + #150 `✓` + #137 已裁决 = 内容 150/150 |
| 印/网文字层 | `pdftotext` 各 **59,120 字节，逐字节一致**（`cmp` rc 0；`-layout` 抽取亦各 112,373 字节一致） |
| P8 最小字号（PyMuPDF，交付印 PDF） | **9.975pt**（173 spans，168 at-min），≥ 9.75pt，PASS |
| boxtitle | **8/8 ≤ 386.5px**（最宽 366.1px，P3 `김치의 날에 알아 둘 것　Надо знать`） |
| U+2019 / U+201C / U+201D 扫查（8 SVG + text.md） | **0 / 0 / 0** |
| 孤标点 sweep（SVG 文本元素首尾） | **0** |
| check_core（自 patch 副本） | rc=0，gloss fails 0，orphan 0，phrases **8/8 verbatim**，日期全对 |
| check_gloss（自 patch 副本） | rc=0，gloss fails 0 |
| census（ex/match + D6） | ex/match 166 项 0 missing；D6 0 missing |
| itemgap（text.md 450 vs core 452） | core accepted 484（unique 452），ed accepted 482（unique 450），rejected 40 both；差 2 = `lcn2` + `lko` 按设计移除 |
| §1.1 grep audit | OK：paper / VOL.4 / `·` / 颜色逐页与 core 一致；hanzi 0；U+2019 0；P7 VOL.5 3→2 按设计 |
| textmd 重导出 | 用交付件标题行重跑后与交付 text.md **逐字节一致**，SHA `956b6fcc…`（首次重跑仅标题行参数是我猜错所致，见 §6 注记） |
| creambox 真墨复核 | v2：250 段奶油底文字，**0 问题**（v1 的 16 个旗标经核查全为检查器伪像，见 §6） |
| 印 PDF 重渲染（scratch 副本，venv） | **字节级一致**，SHA `bcc7eedf…` 与交付相同 |
| 网 PDF 重渲染（scratch 副本，venv） | 大小同为 3,985,120 B；文字层与交付网 PDF **逐字节一致**；8 页（SHA 本就每次不同，不作数） |

## 4. 150 题三源手验

- **源 1 REG**（本版 `content*.py` AST 提取，150 条）↔ **源 2 P8 SVG keys**（`p8.py extract`）：keycheck 148 exact + #150 `✓` + #137 已裁决（§2）。
- **源 3 交付印 PDF P8 文字层**（自写 `print-p8-check.py`，PyMuPDF 取第 8 页、空白归一化后逐题比对 `N. key`）：**150/150 出现，BAD 0**；#137、#138 全句逐字命中。
- P8 答案区逐行与 EDITION-RECORD 的 150 行表核对：页码、类型、key、俄语 note 均一致；#43/#123/#124 的 Weatheri / Лесная служба 表述为 core 自带 rendering，非错字（与 record 的 adjudication 一致）。

## 5. 8 页逐页渲染目视（交付印 PDF，100dpi，`pages/p-1.png` … `p-8.png`）

- P1：masthead、头条、数字盒、日历、目录（含 `Всё`）、quiz 7–10、俄语 footer 均干净；目录 level 徽章右对齐在盒内，无溢出。
- P2：feature、`Покупки` 盒完整在位、D-day 条、练习 11–28，无溢出。
- P3：`김치의 날에 알아 둘 것　Надо знать` 盒标题 fit；栏顶 `않았어요。` 为跨栏续句（`확인되지 / 않았어요` 在栏界断开），属正常流排版，非缺陷；练习 29–46。
- P4：季后赛梯形图、照片+图注、练习 47–64；右栏盒下空白为版式设计（与 core 一致）。
- P5：练习 65–82；`시험 전날의 하루`、`당신은? А вы?` 正常。
- P6：对照表深底浅字表头（`구분` / `지난주` / `이번 주`）渲染正确，练习 83–100。
- P7：Frame `Рамка: 「после ~」. Спросите: 「〜 후에 뭐 해요?」` 用 「」 正确；clinic 4 条、读者来信单俄语 disclosure + VOL.5 承诺、8 句 phrase 全带页码引注（含新句 #7 `수능이 끝나면 일요일 11월 22일에는 김치의 날이 와요` + (1면)）；练习 101–112。
- P8：38 题齐全；答案区 1–150 完整，#137 全句在列；H 作文范文 169 字 + 照片；F 表头 `Слово и значение` 正确。
- **目视结论：8/8 零问题。**

## 6. 观察项（非缺陷，已核实，记录在案）

- **P8 #138 答案行折行收尾为孤字 `4`**：`138. «Самсунг» выиграл титул спустя 12 лет. — См. страницу 4` 在栏内折为两行，`4` 独占第二行。全文完整、无截断、无重叠；同类折行亦见于 #136（`используйте 「에서」` 折行）、#140（`странице 8` 折行），属长答案正常折行，非缺陷。不改。
- **creambox v1 伪像**：首版检查器因未处理 `text-anchor="end"`（P1 目录 level 徽章实为右对齐，墨在盒内）、锚点纵向窗口过宽（把盒上方标题误判为盒内文字）、未区分顶层矩形（P6 表头浅字 `#f4efe1` 坐在深底 `#37402f` 上，属有意设计），报了 16 个旗标。修正后 v2（锚点三态 + 顶层矩形判定）：250 段奶油底文字 0 问题；P1 淡黄标题 `#f6e08e` 亦经核实坐在深底 `#37402f` 横幅上。另 canonical occlusion audit（真墨）0 flags 佐证。
- **textmd 首次重跑差异**：第一次我猜的 title_line（`Lucerna Korean Weekly VOL.4`）与交付件第一行不符，仅此一行不同；改用交付件准确标题行（`… — Korean text, Russian explanations (2026-W47)`）重跑后逐字节一致。非版本缺陷。
- **D5 字体（只记录数量，不判 (b)）**：`Noto Sans CJK SC` 段数 **0**（8 页全为 0）。讲解层（俄语/西里尔）实际用 `Noto Sans CJK KR`：P1 67、P2 81、P3 79、P4 71、P5 85、P6 70、P7 68、P8 105，**合计 626 段**；衬线体 `Noto Serif CJK KR` 合计 883 段。
- **“next Sunday”冻结规则**：在 core-ko 全部源码、ko-ru 全部源码、`tools/tables.py` 中 `grep -ri "next sunday"` **0 命中**，无适用对象，不套用。
- **旧版逐页对比**：W46 ko-ru（`issues/2026-w46/2026-w46-ko-ru/2026-w46-ko-ru.pdf`）为旧版式 VOL.3（米色纸底、红字俄语副标题行、旧 footer）；W47 为新版标准样式 §1.1（VOL.4、书绿+近白新闻纸），与 core-ko 一致。P1、P8 逐页比对：差异均为有意的版式迁移，无 W46 家具被误带入；P8 结构（A–H 组 + 答案区）与 W46 同构，答案注记措辞为当周 core 内容。无缺陷。

## 7. 继承/按设计项（非缺陷，归属已核对）

- text.md 450 vs core 452：`lcn2` + `lko` 按设计移除；俄语 `Всё` 保留（Cyrillic 通过 `is_prose`），故比拉丁版（449）多 1 项。itemgap 复现一致。
- P7 VOL.5 计数 3→2：core 的 `lko` 韩语 disclosure 行按设计移除。
- P8 #150 key 渲染为 `✓`：core 与本版一致。
- 事实债继承自 core-ko（见 core KIT）：截至 11 月 10 日截稿未见内藏山/月出山实测 절정公布；HanNeungGeom 细节（日期/时间/费用外）来自二手来源；K 联赛 35 轮比分未核实——未引用；WiKim Festival 2026 时间/主题/场次无独立来源（按计划刊登）。本版未引入新事实，只做俄语 rendering。
- #43/#123/#124 的 “прогноз Лесной службы / Weatheri” 为 core 自带表述。

## 8. 缺陷清单

**零缺陷。** 无 (b) 项，无需修复路由。

---
*复校：proof1（独立复校员），2026-11-11。未 commit、未 push；未改动生产目录任何文件。*
