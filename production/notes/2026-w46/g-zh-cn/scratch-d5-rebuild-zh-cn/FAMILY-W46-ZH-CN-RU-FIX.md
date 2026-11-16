# FAMILY-W46-ZH-CN-RU-FIX.md — W46 zh-cn-ru D65 fix（P1 读者行 D37 侵入）

- 版：`2026-w46-zh-cn-ru`（W46 zh-cn 家，VOL.3）
- 缺陷：D65（协调员已裁定，真缺陷，不接受）——P1 读者行（y=612）末字 Й 侵入右栏奶油框左缘
- 修复：读者行字号 16 → 15.5pt，仅此一处
- 工作区：`hidden_files/d5-redo/scratch-2026-w46-zh-cn-ru-fix/`（`patched/` + `core/` + `gates-fix/`）
- 仓库 HEAD（开工/收工一致）：`b124ab6d3aa5d1ce5d1f7ab5577d2150058bb077`
- 磁盘：150G 盘已用 80G、可用 70G（< 100G 门限，收工复核一致）
- 未做的事：未 commit/push；未跑 `lint --write`；未跑 `insert.py`；未改 `production/`、`issues/`（只读）；未重跑 webpdf 覆盖 builder 原件；其余 129 版未动

## §0 结论

- **bbox 法（主验收）：修复后余量 +8.6 SVG 单位 ≥ +8，PASS。** 行仍居中（中心 976.8 SVG，~975）。
- **目检：PASS。** 修复后 Й 完整落在白底上，与奶油框左缘有可见间隙；终轮对照图 Й 被框缘切掉右部。
- **门禁：19/21 PASS，1 FAIL（G6 caron，已裁定 D62），1 RECORD（G15b）。** 与任务书预期 18/21 有一处出入：**G15a 由 FAIL 翻为 PASS**——issues 参照现为 run1 build（见 §5 末），pdfdiff 8/8 页 identical，— 差已不存在于本次对照中。非测量误差，证据见 §5。
- **text.md：与已落仓件逐字节一致**（51,516 B，SHA 同值），closer 无需动 text.md。

## §1 修复行

| 文件 | 行 | 旧 → 新 | 内容 |
|---|---|---|---|
| `patched/content12.py`（= production `2026-w46-zh-cn-ru/content12.py`） | 23 | **16 → 15.5** | P1 读者行 `p.text(975, 612, "ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ)　ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ", 15.5, "sans", False, GREY, anchor="middle")` |

- 核对：复制 production 源进 `patched/` 后 `diff -rq` 一致；修复前后 diff 仅此 1 行；文案、盒高、其他行均未动；`15.5` 在 `patched/content12.py` 全文件仅出现 1 处（即第 23 行）。
- 图文件补充（builder 同款做法，D20/D58：production `assets/` 仅 `CREDITS.md`，图不入仓）：`frost.jpg`、`lanparty.jpg`、`locker.jpg`、`popcorn.jpg`、`valley.jpg`、`lucerna-moth.svg`（SHA `42487693…`，D6 试点蛾）自 `style-port-zh-cn/fanout-2026-w46/ru/assets/` 复制进 `patched/assets/`，仅供构建，不随同步。

## §2 重建与 SHA 全值表

流程（builder 同款）：`run.py` → `render.py`（内调 `tools/webpdf.py`）→ `textexp_zh_cn.py` → `<slug>.text.md.new`；解释器 `~/workspace/weekly-git/tools/venv/bin/python`；全部只进工作区。

| 交付物 | 字节 | SHA-256（全值） |
|---|---|---|
| 印 PDF `Lucerna-VOL3-RU.pdf` | 29,054,076 | `f5ba3a64a50a66494b8e4ccb8394d86c0223098d465ffb72879323fcec349a43` |
| 网 PDF `Lucerna-VOL3-RU-web.pdf` | 2,321,118 | `68b66ddafb12f050b70e548776c4d945ac1c4af9570c245efc1aa9556e2a297a` |
| text.md.new `2026-w46-zh-cn-ru.text.md.new` | 51,516 | `dbfeee6c30645a9f5278fa60fcdaf4e8522be900e4a8f87abeda4cc5e7bb7fde` |

- 构建 rc：run 0（TOTAL 150：A2 56 / B1 69 / B2 25）、render 0、webpdf 0（render 内）、textexp 0（1,886 行）。
- text.md.new 与已落仓 production `2026-w46-zh-cn-ru.text.md` **逐字节一致**（`cmp` 通过，同 51,516 B，同 SHA `dbfeee6c…`）。

## §3 bbox 法验收（主，三值对照）

方法：fitz 读网 PDF 文本层 P1，取 y=612 SVG 行（基线 459pt 附近）的 span bbox x1；SVG 单位 = pt ÷ 0.75；余量 = 1439.5 − 行末。框缘 1439.5 SVG 由 P1 奶油 rect x0=1079.62pt ÷ 0.75 得出，**基线/终轮/修复后三版实测同值**（rect y 441.0–966.0pt 覆盖读者行）。

| 轮次 | 行末 bbox | 行末（SVG） | 余量 | 字体 | 行中心（SVG） |
|---|---|---|---|---|---|
| 基线 fanout（pre-D5） | 1077.23pt | 1436.3 | **+3.2** | 12.00pt（Noto Sans CJK SC） | 977.4 |
| 终轮 run1（已发 issues PDF） | 1084.19pt | 1445.6 | **−6.1** | 12.00pt（Noto Sans） | 977.0 |
| **修复后（本轮重建网 PDF）** | **1073.14pt** | **1430.9** | **+8.6 ✓** | **11.62pt（= 15.5 × 0.75，Noto Sans）** | **976.8** |

- 三值与协调员 D65 核实值逐位一致（基线 +3.2 / 终轮 −6.1），方法复现可信。
- 修复后余量 **+8.6 ≥ +8，PASS**；行中心 976.8，仍居中 ~975（终轮 977.0、基线 977.4，同量级偏移，系该行固有排版，非修复引入）。
- 0.5pt 降号效果与线性预测一致：行宽 937.2 → 908.2 SVG（×15.5/16 = 0.96875），行末 −14.7 SVG（−6.1 → +8.6）。

## §4 目检

渲染：fitz 自网 PDF P1 切片（pt x 950–1120、y 420–480，3×）+ 全幅带图（pt x 0–1462.5、y 380–520，1.5×），已真打开看。

- **修复后（`p1-crop-fix.png`）**：`ЧИТАТЕЛЕЙ` 的 Й（含上标短音符）完整落在白底上，Й 与右侧奶油框左缘之间有清晰可见的白间隙，无相贴、无越线。
- **终轮对照（`p1-crop-final.png`）**：同一位置 Й 的右部被奶油框切掉、短音符剩半截——缺陷复现，确认修复针对真问题。
- **带图（`p1-band-fix.png`）**：读者行居中完整，右栏 `本周日历` 奶油盒无侵入，其余 P1 元素（头条、波段）无变化。

## §5 终轮门禁表（21 verdict）

`gates_zhcn46.py` 原件已随家族 scratch 清理而失；本轮用同一批底层工具按 builder 口径重跑（`run_gates.py`，日志 `gates-fix/`；D18/D37 用 phase2 `measure_d18_d37.py`，见 §8）。结果：**PASS 19 FAIL 1 of 21**（另 G15b 仅记录）。

```
GATES-SUMMARY 2026-w46-zh-cn-ru round=fix
  G1: PASS  TOTAL=150 FLOW=0 HEAD=0
  G2: PASS  head_check rc=0 findings=0
  G3: PASS  D5_lat=0 D5_cyr=0 curly_cjk=0 noto_sans=798
  G4: PASS  render rc=0 print=yes 29054076 B
  G5: PASS  web 2321118 B
  G6: FAIL  flags=1 [[TEXTX] p1-touiban.svg 'ǒ' — ink overlaps 'bāogu' by 3.2x15.8px]
  G7: PASS  p8 extract 150/150
  G8: PASS  CLEAN keydiff=[]
  G9: PASS  freeze 8/8 rc=0
  G10: PASS  cjk_added=0 latin_added=111 latin_unexpected=111
  G11: PASS  spill=0 observe=105 set==baseline:True (baseline spill=0 observe=79)
  G12: PASS  defect=0 observe=0 marginal=0
  G13: PASS  touch=0 near=0
  G14: PASS  defects=0 P8 p8-ceyan.svg: lines 242->242 slack_footer 43.0->43.0
  G15a: PASS  print/web multiset diff=0; text.md.new==fanout .new: True; pdfdiff vs issues: verdict: IDENTICAL [page 1: identical (2417 chars)]
  G15b: RECORD  rc=1   8x 'ты' |   7x '周' | CARRYOVER: FAIL
  G15c: PASS  ADOPT: 2026-w46-zh-cn-ru.text.md.new: 934 entries vs ref 933; ADOPT furniture 98, ADOPT word-split 1, UNEXPECTED 0
  G16: PASS  defective quotes=0
  D18: PASS  gap=253.5px date_x=1511.2 slogan_end=1257.7 clusters=3
  D37: PASS  end=1427.0 margin=12.5 (band, y=612) text='ТЕКСТЫ НА КИТАЙСКОМ (УПРОЩЁННОМ)　ОБЪЯСНЕНИЯ НА РУССКОМ — ВЫПУСК ДЛЯ РУССКОЯЗЫЧНЫХ ЧИТАТЕЛЕЙ'
  D37-sub: PASS  end=1209.6 margin=229.9 text='给学中文的人的周报 — Читай настоящий Китай по-китайски'
ALL-GREEN: False (PASS 19 FAIL 1 of 21)
textexp rc=0
```

与终轮 run1（18/21，FAIL G6 + G15a）逐值对照：

| 门 | 终轮 run1 | 本轮 fix | 说明 |
|---|---|---|---|
| G1–G5、G7–G9、G11–G14、G16 | PASS | PASS，同值 | G5 网 PDF 字节 2,321,088 → 2,321,118（+30 B）；G11 observe 105 不变；其余数值逐值一致 |
| G6 | FAIL 1 旗 caron | FAIL 1 旗 caron，同文 | 已裁定 D62，残留 |
| G10 | cjk 0 / latin 111 / unexp 111 | 同值 | 字号改动不改文字，run-split 数不变 |
| G15a | FAIL（pdfdiff 1 页差，1 个 `—`） | **PASS** | 见下 |
| G15b | RECORD rc=1 | RECORD rc=1，同值 | `8x 'ты' \| 7x '周' \| CARRYOVER: FAIL` |
| G15c | ADOPT 934/933，家具 98，word-split 1，UNEX 0 | 同值 | |
| D18 | gap 330.7 | gap 253.5 | 工具口径差，见 §8； verdict 同为 PASS |
| D37 | margin +10.0 | margin +12.5 | 工具口径差，见 §8； verdict 同为 PASS |
| D37-sub | margin +240.9 | margin +229.9 | 工具口径差，见 §8； verdict 同为 PASS |

**G15a 翻为 PASS 的原因（与任务书预期 18/21 的出入，需协调员确认）：** builder 终轮 G15a 的 pdfdiff 参照是当时的 issues PDF（发前旧版，含 `—`）；closer 落仓后，issues 现存 PDF 已是 run1 build——2,321,088 B，与 run1 GATES-SUMMARY G5 同值，frontmatter `pdfBytes: 2321088` / `pdfSha256: f82d449b…e0dec8` 与实测 SHA 一致，且其 P1 读者行 bbox 1084.19pt 即终轮值。本轮 pdfdiff（issues PDF vs 修复后网 PDF）8/8 页 identical（每页字符数两边逐页相等：2417/2548/1907/2133/1907/2274/2966/7469），因两边皆无 `—`、且字号改动不改抽取文本。**`—` 丢失（D61）作为 §1.1 移植已知差仍真实存在于 run1 与发前旧版之间，但 fix 轮次的 G15a 对照（新件 vs 现存 issues 件）已不再包含它。** 若协调员要求 G15a 仍以发前旧版 PDF 为参照，请明示，本轮可补测。

## §6 D19（引用复核，D48 修正逻辑）

- 本报告唯一修复引用 `content12.py:23` **指向修复行本身**：patched 该行即读者行 `p.text(975, 612, …)`，行内含新字号字面量 `15.5`；production 同行旧值 `16` 已核对（§1 diff）；`15.5` 全文件唯一。
- 无 `f.box` 引用；无其他修复引用。
- production KIT（`WEEKLY-KIT.md`）目前尚无 ru 版 `content12.py:23` 引用（grep 0 命中）——closer 补 fix 条目后，由 reproof v2 对改后 KIT 全量重核 D19（BUILD §4 例：47 引用 0 坏）。

## §7 与已落仓值的差异说明（closer 交接）

**会变的文件（closer amend 一笔）：**

| 文件 | 旧值（已落仓） | 新值（本轮） |
|---|---|---|
| production `2026-w46-zh-cn-ru/content12.py:23` | 字号 16 | 字号 15.5（仅此 1 行） |
| 印 PDF（仓库外交付，BUILD §9 惯例） | 29,054,061 B，SHA 仅 BUILD §9 截断值 `160e613d…93ddd6`（全值未留存） | 29,054,076 B（+15 B），`f5ba3a64…349a43`（§2 全值） |
| issues `2026-w46-zh-cn-ru/2026-w46-zh-cn-ru.pdf`（= 网 PDF 改名） | 2,321,088 B，`f82d449b5b581b0b442962ea8741b58b4d4fdd72f5b0f53dd4cb6229b9e0dec8` | 2,321,118 B（+30 B），`68b66ddafb12f050b70e548776c4d945ac1c4af9570c245efc1aa9556e2a297a`（§2 全值） |
| issues `2026-w46-zh-cn-ru/2026-w46-zh-cn-ru.md` frontmatter | `pdfBytes: 2321088` / `pdfSha256: f82d449b…` | `pdfBytes: 2321118` / `pdfSha256: 68b66dda…` |
| production `2026-w46-zh-cn-ru/WEEKLY-KIT.md` D5 节 | “修复 0 处：run1 即 ALL-GREEN”（REPROOF §4 F2 已指为假） | + fix 条目：`content12.py:23` 16 → 15.5，D37 bbox +8.6 / 门禁 +12.5；并按 F2 修正“ALL-GREEN”文案；终轮门禁记为 fix 轮 19/21（残留仅 G6） |

**不变的文件：**

- text.md：production 与 issues 两处 text.md 皆 51,516 B、SHA `dbfeee6c…7bb7fde`，与本轮 `.text.md.new` 逐字节一致，**不动**。
- 其余 129 版、index.json、`svg/`/`cards/`（构建输出，不同步）、图文件（不入仓，D20/D58）。

注：REPROOF §9 所列 ru 网 PDF 2,321,094 B 为 reproof 自建件（webpdf 字体子集非确定性 ±6B），非 builder 件；builder 件为 2,321,088 B（run1 GATES-SUMMARY G5 + issues 实测 + frontmatter 三方一致）。

## §8 方法与口径说明

- **G15a/G15b/G15c/G10/G11/G14 所用工具**与 builder 同款（`tools/`：`head_check.py`、`occlusion_audit.py`、`p8.py`、`freeze.py`、`spill_sweep.py`、`boxtitle_check.py`、`pdf_edge_scan.py`、`d5_creambox_audit.py`、`census_quotes.py`；`style-port-zh-cn/`：`pdf_text_diff_zh_cn.py`、`verify_textexp_zh_cn.py`、`textexp_zh_cn.py`；`d5-redo/tools/`：`d5_census.py`、`verify_textmd.py`）。G8 的 core P8 参照为本轮自 production `core-zh-cn` 源现建（`core/`，run.py rc=0，TOTAL 150），非 fanout 旧件。
- **D18/D37/D37-sub 量测器**：builder 的 `remeasure_p1.py` 亦随 scratch 失传；本轮用 phase2 `measure_d18_d37.py`（同款逻辑：SVG runs + `svglib.text_w` + 奶油左缘 1439.5；ru 用 band 法）。其在 fanout 基线上的 D37 为 +8.4（builder gates 工具 +8.0，差 0.4），可比。
- **D37 工具值 vs bbox 值（以 bbox 为准，D65）：** 本轮工具值 +12.5 vs bbox +8.6，工具高估 +3.9；基线 +8.4 vs +3.2，高估 +5.2；终轮 builder 工具 +10.0 vs bbox −6.1，高估 +16.1（D5 换字体后工具低估墨宽加剧，D65 已记入机制 todo）。三法对修复的**增量**一致：工具 +14.6（−2.1→+12.5，按 text_w 模型推算的终轮值）、bbox +14.7（−6.1→+8.6）。
- **D18 工具值差异：** 本轮 253.5 vs builder 终轮 330.7，差 −77.2。原因：builder 的 D18 工具未计 y=92 标语行的 `letter-spacing=1.7`（两段标语 run 共 46 字 × 1.7 ≈ 78.2px）；date 起点 1511.2 两边逐位一致。修复未动 y=92 行，D18 实质与终轮同值；gap 远大于 0，PASS 不受口径影响。
- **D37-sub 工具值差异：** 本轮 229.9 vs builder 终轮 240.9，差 −11.0。同为 y=372 标语行（3 runs，CJK + `—` + 西里尔），字体量测差约 0.3px/字；余量仍 >200，PASS 不受影响。

## 附录：工作区文件

- `scratch-2026-w46-zh-cn-ru-fix/patched/`：修复后源 + 重建件（svg/、cards/、印/网 PDF、`.text.md.new`）
- `scratch-2026-w46-zh-cn-ru-fix/core/`：D5 core 现建参照（仅 G8 用）
- `scratch-2026-w46-zh-cn-ru-fix/GATES-SUMMARY-fix.txt`：终轮门禁表（§5 全文）
- `scratch-2026-w46-zh-cn-ru-fix/gates-fix/`：各门日志（g2/g3/g6/g7/g8/g9/g10/g11/g12/g13/g14/g15a/g15b/g15c/g16/gD18D37）+ `p8-compare.json`、`g9.json`、`g10.json`、`g14.json`
- `scratch-2026-w46-zh-cn-ru-fix/run_gates.py`：门禁 runner（21 verdict）
- `scratch-2026-w46-zh-cn-ru-fix/measure_bbox.py` + `measure_bbox.log`：bbox 三值量测
- `scratch-2026-w46-zh-cn-ru-fix/measure-baseline.json`、`measure-fix.json`：D18/D37 量测 JSON
- `scratch-2026-w46-zh-cn-ru-fix/p1-crop-fix.png`、`p1-crop-final.png`、`p1-band-fix.png`：目检图
- `scratch-2026-w46-zh-cn-ru-fix/logs-run.log`、`logs-render.log`、`logs-textexp.log`、`logs-core-run.log`、`gates-fix-run.log`：构建日志
