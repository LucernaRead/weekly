# W46 韩语目标家族 D5 重建独立重校报告

- 家族：W46 ko（目标语 ko，读者 de/en/es/fr/it/ja/nl/pt/ru/zh-tw；无 ko 读者）+ core-ko
- 重校工作目录：`hidden_files/d5-redo/scratch-2026-w46-ko-reproof/`（`rebuild/`、`logs/`、`bin/`）
- Builder 报告：`hidden_files/d5-redo/FAMILY-W46-KO-BUILD.md`（全文通读，以之为准绳逐项复核）
- 结论：**PASS** —— 0 内容/门禁 finding；D19 0 finding；D56–D59 四项裁定的事实依据全部独立证实（D57 附两项证据备注，见 §D57，不构成内容/门禁 finding）。

## 结论摘要

| 项 | 重校结果 |
|---|---|
| 独立重建 | 印 PDF 11/11 SHA 全等、text.md 11/11 SHA 全等；双网 PDF 文字层 4 项对比 ×11 版皆差 0（字节差仅 fontTools 跨次元数据漂移，−13…+22 B） |
| 门禁全套重跑（run2） | 10/11 18/19（仅 G15a FAIL），fr 17/19（G15a + G2）；与 builder 终轮归一化 diff **0 行**；gates.json 内 G15b/P8/D18/D37 细节 11/11 全等 |
| D18 独立重测 | 11/11 与 builder 终轮逐值一致，含三处回填值 de 263.1 / en 297.5 / core 370.4 |
| D19 | 0 finding：KIT D5 节引用 13/13 命中 fixes.json 修复行；BUILD 报告行号集与 fixes.json 全等；zh-tw `content56.py:125` 为 Round-1 修复行本身 |
| D56 | 证实：重建 zh-tw KR 面（印/网 KR 31、TC 0）；已发 TC-only；W47/W45 ko-zh-tw 皆 KR 面 |
| D57 | 证实（附备注）：`_` 0/231/0/0；BLANK 代码在位；text.md 69 `_` ×11；pdfdiff 仅 `_`（逐页 18/27/27/27/39/12/18/63 = 231）；填空墨线视觉 2 版在位。备注：NBSP“632”未复现（见 §D57-备注）；nl p7 另有 1 个 `-` 差实为 pdftotext 提取 artifact，字形在 PDF 内在位（见 §D57-备注2） |
| D58 | 证实：已落仓各家 production `assets/` 仅 `CREDITS.md`；§8 的 7 个图文件不同步 |
| D59 | 证实：run2 fr 交付侧干净（TOTAL 150、FLOW 0、HEAD 0），唯一 finding 在冻结基线日志 `logs/baseline-2026-w46-ko-fr-run.log:2` |
| D41 | 证实：run1 G6 9 版 ×7 旗标为真缺陷（基线同位 0 旗标），run2 全版 0 旗标；D37-sub 实墨 es/pt 修复后过关，nl 最紧仍过关 |
| R1 | 证实：逐版缺口恰为 BUILD §0.1 所列，无其他遗漏 |
| §6/§8/KIT | 证实：production 无 `2026-w46-ko-zh-cn`；core-ko 构建成立；§8 总量 11/11 与 BUILD 全等；`transform.py`/`run.py`/`ABSTRACT.txt` 不动；KIT 11/11 各恰 1 个 D5 节且 pin 与 §9 全值一致；D1+D5 安装等价 |
| 残留（仅记录类） | G15b rc=1 ×10、pt rc=2（D27，已知工具缺口）；P2 空白加宽（已 reopen 待 redesign）；nl D37-sub 实墨最紧（+6.8px builder 值，我方 PDF 渲染复测 +10.1px）；G15a pdfdiff DIFF（D57 模板行为，已裁定接受） |

## §1 独立重建与 SHA 核对

- 方法：builder `patched/` 11 版 + core-ko 源文件复制进我方 `rebuild/`（复制时 builder 原件 SHA 已先验 44/44 全等），用 builder 同款 `bin/build-one.sh`（run.py → render.py → webpdf.py → `textmd_ko.py`）逐版重渲。11/11 四步 rc=0。
- 印 PDF：11/11 逐字节 + SHA 与 BUILD §9 全等。text.md（`.text.md.new`）：11/11 逐字节 + SHA 与 §9 全等。
- 网 PDF：render-网与 builder-网皆与 §9 字节差数 B（−13…+22 B），SHA 皆不符——为已知的 fontTools 跨次元数据漂移（D40 类），非内容差。文字层等价性（`pdftotext` 空白剥离多重集差，8 页）：

| 对比 | 11 版结果 |
|---|---|
| 我方 builder-网 vs builder builder-网 | 0（字符数亦逐版相等，如 de 32486/32486） |
| 我方 render-网 vs builder render-网 | 0 |
| 我方 render-网 vs 我方 builder-网 | 0 |
| 我方印 PDF vs 我方 builder-网 | 0（即 G15a 印=网分量） |

- G15a 比较用网 PDF：`gates.py` 用的是 builder-网（`<slug>.web.pdf`），与现行规则一致。发货取舍：**取 builder 的 `<slug>.web.pdf`**（门禁所验原件；我方重建件文字层与之逐字相同但字节不同，绝不重跑 webpdf 产生第三种变体）。

## §2 逐版门禁表（run2，我方重跑值）

| 版 | 计分 | 未过项 | G1 | G2 | G3 | G6 | G11 SPILL/OBSERVE | G12 | G15a | G15b(rc) | G15c | D18 | D37 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| core-ko | 18/19 | G15a | PASS 150/0/0 | PASS 0 | PASS | PASS [] | 0/399 ✓ | PASS 0 | FAIL pdfdiff DIFF | 1 | ADOPT 60/1 | 370.4 | 255.6 |
| de | 18/19 | G15a | PASS | PASS 0 | PASS | PASS [] | 0/439 ✓ | PASS 0 | FAIL | 1 | ADOPT 61/1 | 263.1 | 46.8 |
| en | 18/19 | G15a | PASS | PASS 0 | PASS | PASS [] | 0/434 ✓ | PASS 0 | FAIL | 1 | ADOPT 61/1 | 297.5 | 57.5 |
| es | 18/19 | G15a | PASS | PASS 0 | PASS | PASS [] | 0/436 ✓ | PASS 0 | FAIL | 1 | ADOPT 61/1 | 346.4 | 32.3 |
| fr | 17/19 | G15a+G2 | PASS | FAIL 1（patched 0，baseline-side 1） | PASS | PASS [] | 0/425 ✓ | PASS 0 | FAIL | 1 | ADOPT 60/1 | 331.3 | 39.2 |
| it | 18/19 | G15a | PASS | PASS 0 | PASS | PASS [] | 0/438 ✓ | PASS 0 | FAIL | 1 | ADOPT 61/1 | 335.6 | 110.1 |
| ja | 18/19 | G15a | PASS | PASS 0 | PASS | PASS [] | 0/417 ✓ | PASS 0 | FAIL | 1 | ADOPT 61/1 | 370.4 | 263.3 |
| nl | 18/19 | G15a | PASS | PASS 0 | PASS | PASS [] | 0/431 ✓ | PASS 0 | FAIL | 1 | ADOPT 61/1 | 360.6 | 12.9 |
| pt | 18/19 | G15a | PASS | PASS 0 | PASS | PASS [] | 0/436 ✓ | PASS 0 | FAIL | 2 | ADOPT 61/1 | 346.8 | 25.6 |
| ru | 18/19 | G15a | PASS | PASS 0 | PASS（noto_sans 1050） | PASS [] | 0/447 ✓ | PASS 0 | FAIL | 1 | ADOPT 61/1 | 330.1 | 65.7 |
| zh-tw | 18/19 | G15a | PASS | PASS 0 | PASS | PASS [] | 0/399 ✓ | PASS 0 | FAIL | 1 | ADOPT 61/1 | 370.4 | 255.6 |

- 其余门（G4/G5/G7/G8/G9/G10/G13/G14/G16）11/11 PASS。G15a 其余分量全版通过（印=网多重集差 0、text.md 与 fanout `.new` 逐字节相同）；G15a web-vs-issues 分解：10 版 `·`×127 + `—`×1，fr `·`×126 + `—`×1，zh-tw `／`×8 + `·`×127 + `—`×1 + `/`×8，core `·`×118 + `—`×1。
- P8：11 版 max_y 皆 2624.0、页脚余量 76.0px；元素数 core 1854、de 1364、en 1376、es 1362、fr 1376、it 1356、ja 1812、nl 1325、pt 1362、ru 2642、zh-tw 1847（与 BUILD 全等）。

## §3 归一化 diff

- 我方 run2 `GATES-SUMMARY.txt` vs builder run2 `GATES-SUMMARY.txt`，归一化（G4/G5 字节数置换）后：**11/11 IDENTICAL，总 diff 0 行**（脚本 `bin/normdiff.py`）。
- `gates.json` 逐项核对：G15b rc 11/11 一致（10×1、pt 2）；P8 元素数/max_y/余量 11/11 一致；D18/D37 detail 串 11/11 一致。
- 残留接受项逐项复核：
  - G11 SPILL 0 全版，重建集 == 基线集（`== baseline set: True`）11/11；基线 OBSERVE 值与 BUILD §0.4 全等（core 274、de 293、en 286、es 289、fr 286、it 291、ja 287、nl 291、pt 286、ru 300、zh-tw 287）；我方对基线 de/en/core 重跑 `spill_sweep.py` 得 SPILL 0、OBSERVE 293/286/274，与 builder 基线集一致。
  - G15b（D27 记录项）：rc=1 ×10、pt rc=2（无 pt 读者表），与 builder 一致，仅记录。
  - zh-tw/zh-cn curly（fix2 既定态）：G3 curly_cjk 0 全版；curly_total：de 2、en 4、其余 0。
  - P2 空白加宽：已 reopen 的结构性缺陷类（NO-GO），非 D5 发现，不修，未重测（与 BUILD 一致）。
  - D39(4) teaser 带底缘：本家不存在。实测基线 p7 teaser 带底缘 de 2497.2、en 2512.7、core 2518.7（与 BUILD 值全等），皆在页脚线 2596 之上（余 67–99px）；基线 G11 SPILL 0 全版。
  - P7 读者来信盒溢出：本家不存在。基线 + run2 G11 SPILL 0 全版。
  - G9 zh-tw fanout p2 SVG 0 字节：证实。`fanout-2026-w46/zh-tw/svg/p2-saenghwal.svg` 为 0 字节（2026-11-10 09:16），整棵 fanout 唯一 0 字节 SVG（其余 0 字节文件皆为 `probe-*` 临时文件）；基线 p2 完好（pdfdiff IDENTICAL、text.md 逐字节相同）——fanout 参照损坏，非基线缺陷。

## §4 D18 全部独立重测

- 方法：`measure_d18_d37.py` 复制进我方 `bin/`（与 builder 版逐字节相同，已验其 letter-spacing 修正 + 按簇分组逻辑在位），在我方重建 SVG 上独立重测全部 11 版，**不采信回填值**。

| 版 | 我方 D18 | BUILD 终轮 | 我方 D37 | BUILD 终轮 |
|---|---|---|---|---|
| core-ko | 370.4 | 370.4（回填） | 255.6（y=372，end=1183.9） | 255.6 |
| de | 263.1 | 263.1（回填） | 46.8（y=394，end=1392.7） | 46.8 |
| en | 297.5 | 297.5（回填） | 57.5（y=394，end=1382.0） | 57.5 |
| es | 346.4 | 346.4 | 32.3（y=394，end=1407.2） | 32.3 |
| fr | 331.3 | 331.3 | 39.2（y=394，end=1400.3） | 39.2 |
| it | 335.6 | 335.6 | 110.1（y=394，end=1329.4） | 110.1 |
| ja | 370.4 | 370.4 | 263.3（y=372，end=1176.2） | 263.3 |
| nl | 360.6 | 360.6 | 12.9（y=394，end=1426.6） | 12.9 |
| pt | 346.8 | 346.8 | 25.6（y=394，end=1413.9） | 25.6 |
| ru | 330.1 | 330.1 | 65.7（y=394，end=1373.8） | 65.7 |
| zh-tw | 370.4 | 370.4 | 255.6（y=366，end=1183.9） | 255.6 |

- 结论：11/11 逐值一致，回填值 de/en/core 得证（y=92 行不受 run1→run2 修复影响，run1 == run2）。

## §5 D19（D48 修正逻辑）

- 方法：D48 修正逻辑（`f.box` 引用指向 `tsize=` 收尾行；zh-cn→core 映射不适用本家——core-ko 即 zh-cn 构建；括号写法容忍）。
- `fixes.json`：121 处（de/fr/it/ja/nl 各 13；en/es/pt/ru 各 14），与 BUILD 一致。
- KIT D5 节引用 13 处逐核：de/en/es/fr/it/nl/pt/ru 的 `content12.py:40`、en `:202`、es/pt `:20`、ru `:53`、ja `:39`——**13/13 皆在 fixes.json 对应版的修复行集合内**。实地核对收尾行：en `content12.py:202` 为 `], tsize=21)`、ru `:53` 为 `], tsize=20)`；es/pt `:20` 为 y=394、size 15 的 `p.text` 行。
- BUILD 报告内全部 `content*.py:NNN` 引用：para 40–45（ja 39–44）、ex 56–66 偶数（ja 55–65 奇数）、head 54（ja 53）、box 收尾行 en 202 / ru 53、y394 行 20——与 fixes.json 行号集**逐版全等**（de `{40–45,54,56,58,60,62,64,66}`；ja 偏 −1；ru 含 53；es/pt 含 20；en 含 202）。R1 引用（`content12.py:28/101/102`、`content56.py:141`、`content8.py:61`）为缺口位置引用，非修复引用，不适用 D19。
- 生产 KIT 唯一引用：zh-tw `content56.py:125`（`WEEKLY-KIT.md:108`，Round-1 D1 节）。patched 与 production 该行皆为 `f.gloss("재다 衡量 · 규모 規模 · 섞다 混淆。")`，`規`（U+898F）在位——恰为修复行本身。
- **D19：PASS，0 finding。**

## §6 D56 面核实（zh-tw KR 面）

- 重建 zh-tw：印 PDF `pdffonts` 为 NotoSans/SerifCJKkr ×31、TC 0；网 PDF CJKKR ×31、TC 0。**KR 面证实。**
- 已发版：TC-only（CJKTC ×32、KR 0）——与 BUILD 一致。
- W47 ko-zh-tw：KR 31、TC 0；W45 已落仓 ko-zh-tw：KR 31、TC 0；W46 其余 10 版已发皆 KR-only（×32）。**与 W45/W47 一致。**
- 文字层：重建 zh-tw 网 PDF vs 已发版多重集差 376 = `／`×8 + `·`×127 + `—`×1 + `의`×1（TRIM 已知丢字）+ `_`×231（D57）+ `/`×8——除已知三类外无其他字符差；G15c ADOPT + 内容抽查（§7 探针 3/3）通过。
- Fanout 面与模板面：fanout zh-tw 默认 `face="TC"`（`_char_font(..., face="TC")`），D5 模板 KR-only；重建按模板装机为 KR 面，与 D56 裁定一致。**KR 面不是缺陷，不列为 finding。**

## §7 D57 BLANK 核实（G15a pdfdiff DIFF）

| 检查 | 结果 |
|---|---|
| `_` 计数四方 | 重建印/网 PDF 0 个；已发版 231 个（11 版皆 231）；W47 ko-de 0 个；W45 已落仓 ko-de 0 个（`pdftotext` 实测） |
| pdfdiff 逐页 | builder run2 11 版 ×8 页：87 页仅 `_`（逐页 18/27/27/27/39/12/18/63，合计 231 = 已发 `_` 数），only-new 皆 []；我方门禁 pdfdiff 同型（core/de/en 已验全等，余版 builder 日志同上） |
| text.md `_` | 11 版皆 69 个 |
| 模板 BLANK 代码 | `svglib-ko-d5.py` L223–256 在位（`BLANK = "\u00a0"`、`_blank_run`、`_blanks`）；W47 production `core-ko/svglib.py` 同样含 BLANK，与机制拷贝除 `_D5_READER` 行外 diff 0 行；ja 模板 `svglib-ja-d5.py` 含 BLANK 0 处（故 ja 得 IDENTICAL 而 ko 不得） |
| 填空墨线视觉 | 2 版渲染抽查在位：nl p7（`11월 9일은 D-___예요`、`미리 소금에 절인 배추를 ___라고 해요`、`한국시리즈 ___는` 三处墨线清晰可见）、de p7（同型三处） |
| SVG 层 NBSP run | de 77 个 blank run、1001 个 NBSP 字符；基线/fanout SVG NBSP 0（旧引擎无此机制） |

- **§D57-备注1（NBSP“632”未复现）**：D57/BUILD 称“NBSP 字节数重建与已发版相同（皆 632）”。我方以 6 种口径实测皆未复现该数字：`pdftotext`（默认/`-raw`/`-layout`）、fitz `get_text`、pypdf、pdftohtml-xml——重建与已发**皆为 0**；内容流 `00A0` 计数亦为 0；全流计数则为已发 102 / 重建网 138（该口径含字体 ToUnicode 数据，非正文 NBSP，不可作数）。**实质结论**：NBSP 在正文提取层的“相同”成立（0=0），且 SVG 层 blank run + 视觉墨线证实机制在位；但“632”这一具体数字无从复现（方法未知）。记为证据备注，不构成内容/门禁 finding（裁定的承重依据是 BLANK 机制本身，6 项皆已证实）。
- **§D57-备注2（nl p7 另有 1 个 `-` 差）**：builder run2 pdfdiff 88 页中 1 页例外——nl p7 `only-old=[('-', 1), ('_', 18)]`。fitz span 级核查证实 `-` 字形**在重建 PDF 内在位**：重建 span `'D-'` bbox [483.6, 664.0, 501.6, 679.3]，与基线 span `'D-___'` 同位同起；fitz 全页计数重建/基线/已发皆为 `-` 15 个、全书 66 个。丢失仅发生在 `pdftotext` 的行重组（`'D-'` + NBSP run + 后续 `B1` 标签被拼成 `DB1`），与 `_` 丢失同属提取 artifact，非内容丢失。我方门禁 nl pdfdiff 复现同一 `-` 1，证实其为稳定的 D5 输出提取特性。**不列为 finding。**另：D57 文本“BLANK 机制（7 处）”措辞不精确——实测 `'BLANK'` 字面出现 5 处、`'_blank'` 4 处；机制本身在两文件内逐行一致，不影响结论。

## §8 D58 核实

- `git ls-files 'production/2026-w46/2026-w46-ko-de/assets/*'` 与 `2026-w46-ko-zh-tw` 皆仅 `CREDITS.md` 一件；已落仓 ja-de `assets/` 同样仅 `CREDITS.md`。
- §8 的 7 个图文件（`apples.jpg`、`autumn.jpg`、`baseball.jpg`、`bukhansan-ui.jpg`、`lucerna-moth.svg`、`ssam.jpg`、`study.jpg`）仅存于 patched/fanout `assets/`，不在 production 同步清单内（production `assets/` 仅 `CREDITS.md`）。**D58 证实：7 图不同步，§8 该项作废。**

## §9 D59 fr G2 核实

- run2 交付侧日志干净：`run2-2026-w46-ko-fr-run.log` TOTAL 150、FLOW 0、HEAD 0（`HEAD TOO WIDE` 0 命中）；我方门禁 G1 同值。
- 唯一 finding 仅在冻结基线日志：`logs/baseline-2026-w46-ko-fr-run.log:2`，修前 `HEAD TOO WIDE [P1-headline]: 지금 바로 연습　Exercices immédiats`；run2 `head-check.json` 的唯一 finding 即该条（patched 0、baseline-side 1）；run1 为 defects 2（patched 1 + baseline-side 1），run2 为 defects 1（仅 baseline-side）。
- A 修复 head 25→24 已修掉该缺陷：run2 HEAD 0；fr head 行 `content12.py:54` 已为 24。**D59 证实：D25 类门禁计数 artifact，17/19 接受。**

## §10 D41 核实

- G6：run1 9 版同型 7 旗标（LINEX ×2：line box [87.4, 1843.4, 1862.6, 1844.6] 跨 `A2`/`6.`；TEXTX ×5：`한능검`叠`바쁜` 46.0×4.0、`한능검`叠`한` 4.7×4.0、`정기`叠`한` 13.5×4.0、`바쁜`叠`닫혀요` 46.0×10.7、`한`叠`닫혀요` 4.7×10.2；ru 变体 4.0/14.2）——与 BUILD 逐值一致；基线 11 版 G6 皆 PASS flags []（D5 回归）；与 G1 FLOW OVERFLOW 同根；流修复后 run2 全版 0 旗标（我方门禁 G6 11/11 `flags []`）。**真缺陷已修，非 artifact。**
- D37-sub 实墨复核（副刊头行行末墨 vs 右栏左缘 1439.5）：
  - 我方 PDF 300dpi 渲染复测：es **+26.4px**、pt **+18.8px**、nl **+10.1px**（builder 值 +23.5/+17.2/+6.8，方法阈值差约 3px，结论一致）；SVG 3× 渲染复测：es +33.5、pt +25.8、nl +14.2、de +47.5、fr +40.5（builder 对照值 de +42.2、fr +32.8）。三法皆判：es/pt 修复 D 后过关，**nl 最紧但过关**。
  - run1 实墨（builder 值，我方 SVG 法复核方向一致）：pt −14.5、es −5.8（皆真越线——es 名义 D37 曾 PASS +3.5，正是实墨复核的原因）。

## §11 R1 缺口逐版复核（D39(3)）

- 方法：`r1_scan3.py` 复制进我方 `bin/`（仅改路径指向我方 rebuild，不写 builder `logs/`），在我方重建 SVG + text.md 上重跑。
- 结果 11/11：拉丁读者（de/en/es/fr/it/nl/pt）恰 4 项——caption 词 `KIMJANG`（en `KIMCHI-MAKING`，`content12.py:28`）、`A2→B2`（`:101`）、读者词 `:102`（`Alle`/`All`/`Todos`/`Tous`/`Tutti`）、`D-10 ~ D-4`（`content56.py:141`）；CJK/ru 读者（ja/ru/zh-tw/core）恰 2 项——`A2→B2`、`D-10 ~ D-4`。**与 BUILD §0.1 全等，无其他遗漏。**
- 4 句斜杠提示句（`content8.py:61/63/65/67`）在我方扫描中归入 not_rendered 而非 gap——因 D5 分行使整句在拼接 SVG 串中不再连续；词本身在渲染层在位（如 de p8 `가래떡을`×6、`수요일에`×6），且与 builder gap 集的并集逐版全等。分类漂移，非新缺口。

## §12 §6 core-ko / §8 同步清单 / KIT pin 核实

- §6：production 无 `2026-w46-ko-zh-cn` 目录；fanout `zh-cn/` 即 core 构建目录；已发 (ko, zh-cn) P1 字符串（标语 `매주한국어로…`、徽章 `한국어판`、副标 `한국어를배우는사람을위한주간신문—…`、页脚 `Lucerna　韩语周报 VOL.3　LUCERNA KOREAN WEEKLY`）在我方 core 重建 P1 全数在位；core 基线 P1 SVG 含徽章 `한국어판` 与页脚行。**core-ko 构建成立；closer 同步 patched core-ko → production/core-ko，绝不新建读者目录。**
- §8：`diff -rq patched/ vs production/2026-w46/` 确认每版 8 源文件 + KIT（+ text.md 替换说明）；`diff | wc -l` 总量 11/11 与 BUILD 全等——core 1058、de 1100、en 1100、es 1096、fr 1094、it 1100、ja 1098、nl 1096、pt 1100、ru 1098、zh-tw 1070（de 分文件 svglib 431、bslib4 111、content12 215、content34 102、content56 106、content7 62、content8 52、render 21）；行差主体为 D1 移植（svglib 431 + bslib4 111 占大头）+ 121 处修复。`transform-w45.py`/`run.py`/`ABSTRACT.txt` 不动（core-ko 两侧皆无 `transform-w45.py`，同缺）。
- KIT：11/11 各恰 1 个 `## 补记：D5 字体重建` 节；pin（印 + render-网 + builder-网 + text.md）与 §9 全值 11/11 一致。
- D1+D5 安装等价性：patched svglib vs 机制拷贝 `svglib-ko-d5.py`——latin 版 0 行差；ru/cjk 版恰 2 行（即 `_D5_READER` 一行，两侧各 1 行）；patched svglib vs W47 production `core-ko/svglib.py`——core/zh-tw 0 行差，de 2 行（`_D5_READER` 一行）。

## §13 残留项（仅记录类）

- G15b rc=1 ×10、pt rc=2（D27：共享校验器对 ko 格式未校准；与 W45 ko 一致的已知工具缺口）。
- G15a pdfdiff DIFF（D57 模板 BLANK 机制行为，已裁定接受；见 §7 及两项备注）。
- fr G2 FAIL（D59 门禁计数 artifact，已裁定接受；见 §9）。
- P2 中页空白加宽（已 reopen 待 redesign，非 D5 发现）。
- nl D37-sub 实墨最紧（builder +6.8px；我方 PDF 渲染复测 +10.1px）：过关，无动作，记在案。
- 报告笔误（非交付物问题，builder 原始日志与我方一致）：BUILD §2 fr 表 REWRAP 写 61，实为 60；§3 ja 表 REWRAP 写 60，实为 61（11 版实测：60 者为 fr 与 core，余 9 版 61）。D57 文本“BLANK 机制（7 处）”措辞不精确（实测 `'BLANK'` 5 处）。

## §14 事故记录

- **重校事故 1（已完全恢复）**：重校中途一条 `pdftotext` 命令误用未加引号的 glob（`Lucerna-VOL3-*.pdf` 展开为两文件，第二个被当作输出文件），将 builder `patched/` 内 de 与 zh-tw 两份印 PDF 覆写为提取文本（52,875 B / 约同量）。发现后立即从重校复制时已存的副本恢复——副本为事故前复制、SHA 与 §9 全等；恢复后两文件重验为 PDF 1.7、8 页、SHA 与 §9 全等；收尾再扫 builder `patched/` 44/44 SHA 全等。教训：`pdftotext` 一律用显式单文件路径，禁用 glob；重校复制先行的做法救回了原件。
- **§0.8 事故 2（builder）**：`measure_d18_d37.py` 在 run1 门禁循环跑着时被改，run1 D18 的 de/en/core 由 run2 值回填——本次已用我方脚本独立重测全部 11 版 D18，回填值逐值证实（见 §4）。
- 磁盘：开工 74G/150G，收尾 75G/150G（50%），门内（≥100G 才停手）。
- 未改动：builder `patched/`（除事故 1 的恢复外无任何写操作，收尾 44/44 SHA 全等）、builder `logs/`、production/、issues/；未跑 `lint --write`；未 commit/push。
