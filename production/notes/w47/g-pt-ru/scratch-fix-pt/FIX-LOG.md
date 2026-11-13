# W47 pt 家庭修复日志 — F1 + F2（2026-11-12）

- **修复工人**：pt 家庭修复工人（独立重校 F1/F2 的修复，不含 F3）。
- **依据**：`~/workspace/weekly-git/SOP.md` §8（修复流程）与 §9（摘要须含刊名）；`scratch-reproof-w47-pt/PROOF-NOTE.md` §6（F1/F2 位置与证据）；各版 D5-REPORT（`scratch-d5-rebuild-pt/`，构建结构与渲染命令）。
- **范围**：只动 `production/2026-w47/` 下 pt 家 8 版目录（`2026-w47-pt-en/fr/es/nl/it/ja/ko/ru`）。**不 commit、不 push、不跑 lint、不 reset、不 stash、不 git add。F3（P2「D AS PALAVRAS」分栏）未动。**
- **解释器**：一律 `~/workspace/weekly-git/tools/venv/bin/python`（未用系统 python3）。
- **磁盘**：开工 93G/150G 已用，收尾 93G/150G（57G 空闲），未触 ≥100G 门限。

## F2 摘要流向结论（先查清再动手）

- `tools/insert.py` `render_md()`（约 L165–180）：入仓时读各版目录的 `ABSTRACT.txt`（单行、无 ASCII 双引号、VOL 号须等于台账 VOL.4），写入 issues md 的 frontmatter `abstract` 字段**和**正文摘要节（`body_template` 的 `ABSTRACT` + `ABSTRACT_HEADING`）。无 ABSTRACT.txt 即中止。
- **摘要不进 PDF、不进 text.md**（实测）：5 版摘要的特征尾句在各版 text.md 与印 PDF 中均为 0 命中——it "con le risposte a pagina 8"、ja "8ページにあります"、ko "정답은 8면에"、nl "antwoorden op pagina 8"、ru "ответы — на странице 8"；en 对照 "for English speakers learning Portuguese" 同样 0 命中。pt-it text.md:402 的 "Il 20 novembre" 是 P7 练习讲解句，非摘要。
- **结论：F2 只改 ABSTRACT.txt，不重渲染。**改后摘要由 insert.py 在入仓时读入 frontmatter 与 md 正文；生产 PDF/text.md 不受影响（5 版印/网 PDF 与 text.md SHA 与 PROOF-NOTE §1 完全一致，见下）。

## F1 源头定位

- F1 句在两处源头，二者须同步改（只改一处会留下一个旧版）：
  1. **印/网 PDF 源头**：各版 `content7.py:52` 的 `c.bridge("quando, se, quem …")` 全句（由 transform.py 从 core + tables 生成，run.py 读它出 SVG）。
  2. **text.md 源头**：各版 `tables_<lang>.py` SEG 表 `"后用虚拟式将来："` → 动词碎片（`textmd.py` 从 core text.md + SEG/OVR 生成 fan-out text.md；`textmd.py` 从 `scratch-fanout-pt/` 导入 tables，故**版内副本与机制副本两份都要改**，已核实两份此前完全一致）。
- 改后复核：每版 `svg/` 其余 7 页与改前逐字节一致，仅 `p7-lingua.svg` 变，且只变了动词一词（坐标/行高未动，无重排）；text.md diff 每版仅 line 393 一行。
- de/it/ru 的单数形式（`steht danach…` / `vuole…` / `требует…`）校对员已裁定可辩，**未动**（已 grep 确认仍在原处）。

## F1 修复（4 版：pt-en / pt-fr / pt-es / pt-nl）

每版流程：改前快照（`scratch-fix-pt/<版>/baseline/`，不含 cards/）→ 改 `content7.py:52` + 两份 tables SEG → `run.py` → `render.py` → `textmd.py`（core text.md + 版目录 + 语种）→ `webpdf.py` → `gates.py` → `gates.sh` 全套（以改前快照为 creambox 基线）→ 更新 KIT §6 + 文末 fix 节。

### pt-en：takes → take

| 文件 | 改前（尺寸 / SHA-256 前 12） | 改后（尺寸 / SHA-256 前 12） |
|---|---|---|
| 印 PDF `A-Lucerna-VOL4.pdf` | 12,421,287 B / `91fa99c4ed0b` | 12,421,286 B / `7221c0d7009c` |
| 网 PDF `A-Lucerna-VOL4-web.pdf` | 1,058,717 B / `b100c5765c5f` | 1,058,709 B / `71ebd11901ed` |
| text.md（md5） | 37,333 B / `1d0567bb2493` | 37,332 B / `ed59cccd8eab` |

- 改后 P7 印 PDF："quando, se, quem take the future subjunctive…"；旧形式 svg + 印 PDF 均为 0 命中；text.md diff 仅 line 393。
- 门禁（`gates-fix1/`，ALL-GREEN）：run TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE；gates.py 16/16 FAILURES: none；occlusion 0 flags；p8 extract 150/150，compare CLEAN（keydiff=[137, 138]）；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH, 0 NEAR；creambox PASS 0 defects；D5 census PASS；印/网文字层逐字节相同（45,957 B 各，`-layout` 103,755 字符，字符多重集差 0）。
- KIT：§6 已更新为改后印/网 SHA + 尺寸；文末已加 "F1 fix" 节。

### pt-fr：prend → prennent

| 文件 | 改前（尺寸 / SHA-256 前 12） | 改后（尺寸 / SHA-256 前 12） |
|---|---|---|
| 印 PDF `A-Lucerna-VOL4.pdf` | 12,422,440 B / `90f78551a5eb` | 12,422,441 B / `8e7a24d96c3b` |
| 网 PDF `A-Lucerna-VOL4-web.pdf` | 1,059,873 B / `83f63d47ace7` | 1,059,870 B / `0b41560bc4b8` |
| text.md（md5） | 37,699 B / `98bdb7a249d9` | 37,702 B / `596207ea7baa` |

- 改后 P7 印 PDF："quando, se, quem prennent le futur du subjonctif…"；旧形式 svg + 印 PDF 均为 0 命中；text.md diff 仅 line 393。
- 门禁（`gates-fix1/`，ALL-GREEN）：run TOTAL 150，0 警告；gates.py 16/16 FAILURES: none；occlusion 0 flags；p8 extract 150/150，compare CLEAN（keydiff=[137, 138]）；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH, 0 NEAR；creambox PASS 0 defects；D5 census PASS；印/网文字层逐字节相同（47,433 B 各，104,943 字符，差 0）。
- KIT：§6 已更新；文末已加 "F1 fix" 节。

### pt-es：lleva → llevan

| 文件 | 改前（尺寸 / SHA-256 前 12） | 改后（尺寸 / SHA-256 前 12） |
|---|---|---|
| 印 PDF `A-Lucerna-VOL4.pdf` | 12,421,396 B / `9e80ddac1389` | 12,421,397 B / `cf8dcb1f5bbb` |
| 网 PDF `A-Lucerna-VOL4-web.pdf` | 1,058,824 B / `4f918ab38188` | 1,058,816 B / `f60aee6774f2` |
| text.md（md5） | 37,467 B / `9bdf14009d81` | 37,468 B / `8f4657d0e9fb` |

- 改后 P7 印 PDF："quando, se, quem llevan el futuro de subjuntivo…"；旧形式 svg + 印 PDF 均为 0 命中；text.md diff 仅 line 393。
- 门禁（`gates-fix1/`，ALL-GREEN）：run TOTAL 150，0 警告；gates.py 16/16 FAILURES: none；occlusion 0 flags；p8 extract 150/150，compare CLEAN（keydiff=[137, 138]）；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH, 0 NEAR；creambox PASS 0 defects；D5 census PASS；印/网文字层逐字节相同（47,061 B 各，103,524 字符，差 0）。
- KIT：§6 已更新；文末已加 "F1 fix" 节。

### pt-nl：krijgt → krijgen（另含 F2）

| 文件 | 改前（尺寸 / SHA-256 前 12） | 改后（尺寸 / SHA-256 前 12） |
|---|---|---|
| 印 PDF `A-Lucerna-VOL4.pdf` | 12,422,999 B / `7fbf77a5d9da` | 12,422,999 B / `390ac2d5faf5` |
| 网 PDF `A-Lucerna-VOL4-web.pdf` | 1,060,452 B / `0fc3730b1fb5` | 1,060,451 B / `a6e383aaab91` |
| text.md（md5） | 37,559 B / `40b63423459e` | 37,560 B / `6592eca08f2d` |

- 注：印 PDF 尺寸未变（12,422,999 B），SHA 已变——一词之改在压缩文字流内，尺寸巧合；SVG 与印 PDF 文本已核实为新形式。
- 改后 P7 印 PDF："quando, se, quem krijgen de toekomende tijd van de aanvoegende wijs…"；旧形式 svg + 印 PDF 均为 0 命中；text.md diff 仅 line 393。
- 门禁（`gates-fix1/`，ALL-GREEN）：run TOTAL 150，0 警告；gates.py 16/16 FAILURES: none；occlusion 0 flags；p8 extract 150/150，compare CLEAN（keydiff=[137, 138]）；spill 0 SPILL；boxtitle 0 DEFECT；edge 0 TOUCH, 0 NEAR；creambox PASS 0 defects；D5 census PASS；印/网文字层逐字节相同（47,101 B 各，105,718 字符，差 0）。
- KIT：§6 已更新；文末已加 "F1 fix" 节（含 F2 说明）。

## F2 修复（5 版：pt-it / pt-ja / pt-ko / pt-nl / pt-ru）

只改各版 `ABSTRACT.txt`（在摘要开头相应位置加入 "A Lucerna"，并按其余 6 版的开头模式补 VOL.4；措辞贴合各版首句；单行、无 ASCII 双引号、VOL 号唯一且为 4）。**未重渲染，未改 KIT**（KIT 不动，见本日志注明）。改前原件存 `scratch-fix-pt/<版>-ABSTRACT.pre-fix.txt`。

| 版 | 改前开头 | 改后开头 | grep `lucerna`（不区分大小写） |
|---|---|---|---|
| pt-it | `Il 20 novembre è festa nazionale, …` | `Il Settimanale portoghese di A Lucerna VOL.4: il 20 novembre è festa nazionale, …` | 0 → 1 |
| pt-ja | `11月20日は全国の祝日、…` | `A Lucerna ポルトガル語週報 VOL.4：11月20日は全国の祝日、…` | 0 → 1 |
| pt-ko | `11월 20일은 전국 공휴일, …` | `A Lucerna 포르투갈어 주간지 VOL.4: 11월 20일은 전국 공휴일, …` | 0 → 1 |
| pt-nl | `Op 20 november is het een nationale feestdag, …` | `Het Portugese Weekblad van A Lucerna VOL.4: op 20 november is het een nationale feestdag, …` | 0 → 1 |
| pt-ru | `20 ноября — национальный праздник, …` | `Португальский еженедельник A Lucerna VOL.4: 20 ноября — национальный праздник, …` | 0 → 1 |

- 其余 6 版摘要（en/de/fr/es/zh-cn/zh-tw）未动，计数仍为 1；改后 11 版摘要计数全部为 1。
- F2-only 四版（it/ja/ko/ru）印/网 PDF 与 text.md SHA 与 PROOF-NOTE §1 完全一致，未被重建：
  - it：印 `56f388e7ce3a`（12,418,794 B）、网 `ab8305b734dc`（1,056,196 B）、text.md md5 `39b09bea2a4f`；
  - ja：印 `9208d231d66c`（15,449,291 B）、网 `a9b4a30929c1`（1,433,879 B）、text.md md5 `83035b2da702`；
  - ko：印 `f3104fecd528`（14,231,397 B）、网 `797ad196553e`（1,307,288 B）、text.md md5 `2cfbfa663d5e`；
  - ru：印 `6208be63e917`（12,694,224 B）、网 `c3b7eae275d7`（1,311,813 B）、text.md md5 `0db690a29850`。
- pt-nl 的 F2 与 F1 同轮完成（一次重渲染覆盖 F1；F2 本身不需重渲染），见上节与 KIT 文末 fix 节。

## F3 未动

- 未碰任何版的 `content12.py`（P2 源头）；四版重建的 `svg/` 中除 `p7-lingua.svg` 外其余 7 页与改前快照逐字节一致（含 `p2-vida.svg`），P2 未重排。
- de/pt-zh-tw/core-pt 未动；其余家庭未动。

## 文件改动清单（本任务所改，全部未提交）

- F1 源头（4 版 × 3 处）：`2026-w47-pt-{en,fr,es,nl}/content7.py:52`、`2026-w47-pt-{en,fr,es,nl}/tables_<lang>.py` SEG 项、`scratch-fanout-pt/tables_<lang>.py` SEG 项（机制副本，textmd.py 的实际读入）。
- F1 重建产物（4 版）：`svg/p7-lingua.svg`、`cards/`（8 张重渲染）、`A-Lucerna-VOL4.pdf`、`A-Lucerna-VOL4-web.pdf`、`2026-w47-pt-<lang>.text.md`、`WEEKLY-KIT.md`（§6 + 文末 fix 节）。
- F2（5 版）：`2026-w47-pt-{it,ja,ko,nl,ru}/ABSTRACT.txt` 仅此一文件。
- 日志与快照：本目录 `scratch-fix-pt/`（各版 `baseline/`、`run/render/textmd/webpdf.log`、`gates.log`、`gates-fix1/`；F2 改前摘要副本 `<版>-ABSTRACT.pre-fix.txt`）。
- 注意：`scratch-fanout-pt/tables_<lang>.py` 是机制表副本（不在 weekly 仓内），与版内副本同步改动；`scratch-fanout-pt/en-textmd-diff.json` 由 textmd.py 每次运行覆写（仅为 diff 报告，无内容影响）。

## 结论

- **F1：4/4 已修**（pt-en/fr/es/nl），印+网+text.md 均已重渲染，门禁全绿（p8 compare CLEAN、occlusion 0、boxtitle/spill/edge 全过、D5 普查 PASS），KIT 已同步为盘上实际 SHA。
- **F2：5/5 已修**（pt-it/ja/ko/nl/ru），仅改 ABSTRACT.txt，11 版摘要 `lucerna` 计数现全部为 1；未重渲染、未改 KIT（依据：摘要流向见上，insert.py 入仓时读 ABSTRACT.txt）。
- **F3：未动。**
