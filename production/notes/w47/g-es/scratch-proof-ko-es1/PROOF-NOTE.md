# PROOF-NOTE — 2026-W47 ko-es (proof1)

- 版：`2026-w47-ko-es`（target ko，reader es），ko fan-out #3 重建版（run 1）
- 复校员：独立 proof1（与 #3 构建者分离）；全部门禁自跑，生产文件只读
- 结论：**(a) 定稿** —— 缺陷 0；承接项逐项重验全部通过；门禁逐项见 GATE-LOG.md
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-ko-es1/`
- 日期：2026-11-11（UTC）

## 1. SHA 复核（开工先核对，全部对上才开工）

| 文件 | 字节 | SHA-256 | 结果 |
|---|---|---|---|
| 印 `Lucerna-VOL4-KO-ES.pdf` | 45,679,580 | `20c7f485832a5ff7e13e0a2687c728a27db818350f6d9654f08f94ec4a79c426` | ✓ 与任务一致 |
| 网 `Lucerna-VOL4-KO-ES-web.pdf` | 4,032,263 | `624c1933067d8f0f102971ed79d27eeb335526fa9fc0f330032bfdbb2d399d3f` | ✓ 与任务一致 |
| `2026-w47-ko-es.text.md`（任务称 text.md） | 35,207 | `8c5396b8d0a342d6ffc4cc8d537138d94680bbf1586282f7a336d6e4c0252e89` | ✓ 与任务一致 |
| `ABSTRACT.txt` | 384 | `383ccd7f7751d1701585eb271d507b5dd626173dca241d74c7bc8c81fb2c8cdf` | ✓ 与 #3 记录一致 |

核心 ko 未变（只读核查，未重建）：印 `Lucerna-VOL4.pdf` 46,232,227 B
`53bf14edeca05f9db56e699b5d826f50c320eebcce200c4b876b394de21a2f27`；
网 4,232,878 B `9592945ae188dc8e50394fcab1ded155baaff63161bcf0b5f7ecbc6898c43bc7`；
text.md 34,606 B / 452 项 `da1d3a323f7c83eb95fe989e59f56ca6a706282c443f20cc5792c3f73468181a`——
三件与 ko #3 报告 §1 基线逐字节一致。开工探针：`git hash-object -w` 成功，
goals 侧 scratch 真实写文件成功，`/dev/null` 存在。

生产目录状态：`git status` 中 `2026-w47-ko-es/` 与 `core-ko/` 始终仅为 `??`
（未跟踪，与开工时一致）；本轮无任何改动、commit、push。

## 2. 缺陷清单

**无。0 项。**

## 3. 承接项逐项重验（ko #3）

### (1) P7 Frame 「」修复 —— 通过
- 重建 8 张 SVG 与生产 SVG 逐字节一致；与 #2 run 3 哈希
  （`scratch-fanout-ko/es/sha-es-run3.txt`）逐项比对：**仅 P7 变**
  （`eb377a55…` → `f73e0a06…`），其余 7 页字节一致。
- `content7.py:81` 为 `Marco: 「después de ~」. Pregunta: 「〜 후에 뭐 해요?」`；
  P7 SVG 与 text.md L761 同形；弯引号全扫 U+201C/U+201D/U+2019 在 8 SVG +
  text.md 均为 0。
- 印 PDF −122 B（45,679,702 → 45,679,580）与“仅 P7 Frame 修”一致：
  scratch 重渲染印 PDF 字节一致（SHA `20c7f485…`，见 §4）。

### (2) text.md 332→449 项重导出 —— 通过
- `textmd.py` 重导出字节一致（SHA `8c5396b8…`），449 项；
  分页非空行 72+72+54+49+42+55+52+53 = 449。
- 三处扣减逐一核实，无缺失、无多余：`Todo` 在 P1 SVG（y=1600.0）
  渲染、text.md 中 0 次（`is_prose`  quirk，见 §5）；`lcn2`/`lko`
  在 text.md 中 0 次（按设计剔除）；其余与核心 452 项的差额仅此 3 项。
- census：ex/match 166 项 0 缺失，D6 0 缺失。
- P8 答案列表不入 text.md 导出集——与核心 text.md 同设计
  （核心 text.md 同样止于 `答 参考答案` 标题行，无编号答案行）。

### (3) 记录项：P2 instr EDGE、P8 F-header TEXTX 修复 —— 通过
- P2 instr 现为 `Relacionar palabras y notas`（`content12.py:299`，
  P2 SVG 单行完整），旧串 `Relacionar las palabras con las notas` 全版 0 次。
- P8 F 组 instr 现为 `Palabra y significado`（`content8.py:86`），旧串
  （`Relacionar la palabra con su significado` / `Relacionar palabra y
  significado`）全版 0 次；P8 目视 F 标题单行，与 a/b/c/d 选项行无重叠。
- occlusion audit 0 flags（见 §4）为几何学复核。

### (4) `Todo` is_prose quirk —— 说明（非缺陷）
- `textmd.py` 的 `is_prose` 拒收裸 3 字母拉丁词 `Todo`（P1 目录 8면 行的级别词），
  故 text.md 449 而非 452；SVG/PDF 正常渲染 `Todo`（P1 目视已确认）。
  与 en/de 同模式；内容无缺口。

## 4. 150 题逐题手验（三源一致）

- 源 1（REG，版源文件）：`keycheck-mine.py`（共享 `keycheck-ko.py`，
  输入改为本次 scratch 副本源文件 + 本次新鲜 P8 提取）——REG 150，
  SVG keys 150，exact 149，trunc-ok 1（#150 `✓`，与核心一致），BAD 0，
  rc=0；分页面 10/18/18/18/18/18/12/38 全对。
- 源 2（P8 SVG 提取）：本次新鲜 `p8.py extract` 150/150，与 ko3 的
  `p8-es.json` 键逐一相同；`p8.py compare` vs 核心 CLEAN，keydiff
  `[137, 138]`——E 组按设计重定向：137 核心 `11月22日是泡菜日。` →
  es `El 22 nov. es el Día del Kimchi.`；138 核心 `三星时隔12年夺冠。` →
  es `Samsung ganó el título después de 12 años.`；139/140 键仍为韩文，
  其余 146 键与核心完全相同。
- 源 3（印 PDF 文字层）：全部多字键 0 缺失；记录表 150 行逐行比对
  （页/类型/键）0 差异（`verify150.py`，REG 表落盘 `logs/reg150.json`）。
- 6 条答案注（#79/#81/#91/#125/#133/#136）在 pdftotext 扁平串中未整串命中，
  已逐条核实为提取 artifact，非内容缺失：注文本在 P8 SVG 中完整存在，
  只是折为两行（如 #79 `…sujeto +` / `adverbio + verbo`），pdftotext
  -layout 按栏序交错所致；P8 目视 6 条均完整。

## 5. 8 页逐页目视（scratch 重渲染卡片，1950×2700）

P1–P8 全部干净，0 问题：页眉/页脚（西语 `SEMANARIO COREANO VOL.4 …
Explicaciones en español`，`Página n de 8`）、8 张配图及图注、
奶油盒、对照表（P6 三行交替底色正常）、P7 工具箱/读者来信/8 短语、
P8 全部练习 A–H 与 1–150 答案（含 H 范文 169 字去空格计数与印文一致）
均无溢出、重叠、截断。`Todo` 在 P1 目录 8면 行正常显示。

## 6. 逐盒裁定（creambox 正典工具，md5 `ee7a55d8b2057cf4ad42a97bb1197383`）

- 49 个奶油盒（P1 5、P2 12、P3 7、P4 5、P5 6、P6 11、P7 3、P8 0），
  全部 inside-only；PIL 真墨 clearance 最小 **+0.4px**（三处 ¿Y tú? 盒，
  P2/P3/P5，末行 `frases en coreano y envíanoslas.` / `coreano y envíanoslas.`），
  其余 ≥ +8.7px。
- 19 条 below-window 行全部 owner-rect NONE（下一标题/图注，+26..+44px，
  非 +12..+18px 的同流溢出），逐条已裁定为假阳性；P6 表格行标签
  （`단풍`/`예보 날짜`/`예보 날짜 지났어요`，+35.0）目视确认为下一表行，
  非溢出；P6 表源注（+30.0）为表下注文。
- +0.4px 三处为**紧配合、非缺陷**：occlusion（PIL 真墨几何）0 flags；
  符合 es3 先例标准（真墨 ≥ +0.1 在盒内）；目视三盒末行均在盒内、
  盒下留有奶油空隙；同类先例 P2 购物标题 +0.7px 已在 KIT 中“实测、保留”。
  未来该盒文案加长须重测（已记为观察项，非缺陷）。

## 7. 观察项（非缺陷，不计入判定）

1. **D5 字体（生产级待定项，仅记录）**：ledger 2026-11-11 记
   “D5 字体范围待用户定（A 78 版 / B 390 版）”。本版未发现 ko-es
   特有的 D5 字体缺陷；范围待定，不计入本次判定。
2. **韩文正文双句号 `..`**（P2 `11월 11일까지예요..`、P3 `않았어요..`、
   P4 `끝났어요..`、P7/P8 各一处）：逐串核实与已定稿核心 ko 的 SVG
   完全相同，为核心原文继承，非本版引入；freeze diff 亦证韩文串无新增。
3. **P8 #79/#133 答案注折两行**：在 2540 界内（P8-keys 终点 2457），
   compare CLEAN；排版固有，非缺陷。
4. **配对题注末尾重复选项字母**（如 `25. d — … 199 456 wones d`）：
   核心原文惯例（源注字面自带字母），非缺陷。
5. **P2 购物标题 `Lista de la compra` 385.8px**，距 386.5px 内宽仅
   0.7px——KIT 已“实测、保留”；未来核心改动该盒须重测。

## 8. 门禁汇总（全绿）

| 门禁 | 结果 |
|---|---|
| run.py（系统 python3） | rc=0，TOTAL 150（A2 51/B1 72/B2 27；页 10/18/18/18/18/18/12/38），0 FLOW OVERFLOW / HEAD TOO WIDE；P2-feature 1531，P8-keys 2457，P7 teaser 2483.7 |
| 重建 SVG vs 生产 | 8/8 字节一致 |
| 印 PDF 重渲染（venv，仅 scratch） | 字节一致，SHA `20c7f485…` |
| 网 PDF | 只核落盘 SHA（`624c1933…`），**未重渲染**（webpdf 字节不可复现，铁律遵守） |
| freeze baseline（系统 python3，Pillow 10.2.0） | **8/8** |
| freeze diff vs 核心 | 新增 CJK 7，全为 U+3000（页脚） |
| occlusion audit | **0 flags**；selftest 六类全触发，干净对照静默 |
| p8 extract / compare | 150/150；CLEAN，keydiff [137, 138]（设计） |
| keycheck（独立重跑） | 150/150（149 exact + #150 `✓`） |
| boxtitle | 8/8 ≤ 386.5px |
| check_core / check_gloss | rc=0；gloss fails 0；短语 8/8 原文；orphan 0；日期全对 |
| census | ex/match 166 项 0 缺失；D6 0 缺失 |
| 印/网文字层 | 字节一致（PyMuPDF 48,446 B；pdftotext 107,850 B） |
| P8 最小字号 | **9.975pt**（172 spans，167 在最小值）≥ 9.75pt |
| §1.1 grep audit | paper/VOL.4/`·`/颜色与核心逐页一致；汉字 0；U+2019 0；P7 VOL.5 3→2 按设计 |
| creambox 逐盒 | 49 盒全 inside-only，真墨最小 +0.4；19 条窗下行全假阳性 |
| 孤儿标点全扫 | 独行 。/独行右引号/独行 ：/– 均为 0（SVG + text.md） |
| 弯引号全扫 | U+201C/U+201D/U+2019 全版 0 |
| 目视 8 页 | 0 问题 |
| text.md | 重导出字节一致，449 项 |
| ABSTRACT.txt | 384 B，SHA 与记录一致 |

**结论重申：(a) 定稿。** 缺陷 0；三件 SHA 已复核；生产文件未动。
