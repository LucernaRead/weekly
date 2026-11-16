# FAMILY-W46-ZH-TW-REPROOF.md

**家**：W46 zh-tw（VOL.3），10 版：de/en/es/fr/it/ja/ko/nl/pt/ru（core-zh-tw 兼 en 读者版）
**Reproof**：独立重校 v1 · **Verdict: PASS**（1 项 D19 文本类 finding，见 §10 F1；D43：closer 落仓时原地修 + 针对性复验，不需整轮重校）
**日期**：2026-11-16（UTC）· 仓库 HEAD `6753a650`（开工/收工一致）· 磁盘 75G/150G（51%）

报告只写、不 commit、不 push、不动 production/issues、不跑 lint --write。Builder `patched/` / `baseline/` / `logs/` 只读，未写；全部输出在 reproof 工作区 `scratch-2026-w46-zh-tw-reproof/`。

## §0 方法

- 通读 BUILD 报告全文；rsync builder `patched/` 源文件（不含 PDF/text.md.new/svg/cards/`__pycache__`）到 reproof `patched/`，`diff -rq` 核对 **10/10 SOURCES-IDENTICAL**；baseline（svg + 源文件，不含 PDF/cards）与 `trial/*.fanout.text.md` 同样 rsync 核对（抽查 5 版 BASELINE-IDENTICAL）。
- 同款流程独立重建：run.py → render.py → 显式 webpdf.py → naive textexp → D5 joiner（`--base-svglib baseline/<slug>/svglib.py`）。解释器 `~/workspace/weekly-git/tools/venv/bin/python`；`fc-cache -s` 已暖。
- 门禁脚本为 builder `gates_zhtw.py` 的复制件，仅改硬编码 SCRATCH 路径指向 reproof 目录（diff 仅此 1 行）；输出写 reproof `logs/`。d19_check.py 同样仅改 S 路径复制运行。
- **中断与恢复**：运行体重启杀死首轮重建循环（做到 pt 一半、ru 未开始；8 版已落 rc 行）。用 `rebuild_all.sh patched reproof --resume` 续跑：8 版跳过，pt + ru 全量重建 rc=0。最终 10/10 rc=0、TOTAL=150。
- 事故对照：pt 基线 120MB 印 PDF 偶发已解决——本轮重建 pt 印 PDF 字节 = §9 pin（见 §3），无残留。

## §1 逐版门禁复核表（我的独立重跑 vs builder 终轮）

分母 19/版（G1–G14 + G15a + G15c + G16 + D18 + D37；G15b 仅记录）。

| 版 | 我的终轮 | builder 终轮 | G3 | G10 lat_added | G11 | G15a difflines | G15b | G15c | G16 | D18 | D37 内容边 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| de | **18/19** | 18/19 run1 | 0/0/0 | 263 | 0 SPILL (132 OBS) | 108 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| en | **17/19** | 17/19 run1 | 0/0/0 | 253 | **2 SPILL**¹ (132 OBS) | 32 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| es | **18/19** | 18/19 run1 | 0/0/0 | 242 | 0 SPILL (132 OBS) | 302 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| fr | **18/19** | 18/19 run1 | 0/0/0 | 246 | 0 SPILL (131 OBS) | 132 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| it | **18/19** | 18/19 run1 | 0/0/0 | 222 | 0 SPILL (128 OBS) | 50 | rc=1 | ADOPT | 0 | 21.0px | **3.5px**² |
| ja | **18/19** | 18/19 run2 | 0/0/0 | 157 | 0 SPILL (132 OBS) | 500 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| ko | **18/19** | 18/19 run1 | 0/0/0 | 157 | 0 SPILL (**178 OBS**) | 100 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| nl | **18/19** | 18/19 run1 | 0/0/0 | 229 | 0 SPILL (133 OBS) | 42 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |
| pt | **18/19** | 18/19 run1 | 0/0/0 | 237 | 0 SPILL (129 OBS) | 82 | rc=**2** | ADOPT | 0 | 21.0px | 20.6px |
| ru | **18/19** | 18/19 run2 | 0/0/0 (noto_sans=1013) | 70 | 0 SPILL (137 OBS) | 510 | rc=1 | ADOPT | 0 | 21.0px | 20.6px |

全版共通（我的重跑 = builder）：G1 TOTAL 150、G2 head 0、G4 render、G5 webpdf < 7 MB、G6 遮挡自检 OK + 0 旗标、G7 p8 150/150、G8 CLEAN、G9 freeze 8/8、G10 cjk_added=0、G12 0 DEFECT（backup ok）、G13 0 TOUCH/0 NEAR、G14 0 defects、G16 defective=0、D37 最小边距 31.5pt。唯一 FAIL 全版均为 G15a REFLOW（D30 接受，见 §6）。

¹ en 2 SPILL 为基线先存残留，接受（见 §5）。² it D37 内容边最紧 3.5px，仍 PASS（> 0，见 §9）。

## §2 归一化 diff（builder 终轮 GATES-SUMMARY vs 我的 GATES-SUMMARY-reproof）

归一化：剥离 round tag（run1/run2/reproof）、G5 网 PDF 字节数、绝对路径。**10/10 均为 0 行**：

| 版 | 归一化 diff 行数 | | 版 | 归一化 diff 行数 |
|---|---|---|---|---|
| de | 0 | | ko | 0 |
| en | 0 | | nl | 0 |
| es | 0 | | pt | 0 |
| fr | 0 | | ru | 0 |
| it | 0 | | ja | 0 |

## §3 交付物 SHA 核对表（vs BUILD §9；§9 全值由解析 BUILD §9 表格取值，非手抄）

| 版 | 印 PDF 字节 | 印 SHA-256 前 16（我的 = §9） | text.md.new 字节 | text SHA-256 前 16（我的 = §9） | 网 PDF 字节（我的 vs §9） | 网文本层 diff |
|---|---|---|---|---|---|---|
| de | 5,459,405 | `76a33a5d1bee41c3` ✓ | 50,151 | `90ea2c2ac0b0e446` ✓ | 1,502,042 vs 1,502,046 (−4) | 0 |
| en | 5,487,327 | `4d5b8a5bd8790246` ✓ | 47,637 | `94a69e96bc439185` ✓ | 1,524,377 vs 1,524,374 (+3) | 0 |
| es | 5,458,175 | `6e829430088dd708` ✓ | 50,498 | `0b725f273c5a99bf` ✓ | 1,500,668 vs 1,500,683 (−15) | 0 |
| fr | 5,457,617 | `2bfbe2ffae514531` ✓ | 51,149 | `1b4f4dff528f1c84` ✓ | 1,500,238 vs 1,500,234 (+4) | 0 |
| it | 5,450,370 | `a6eddb2de4d67565` ✓ | 49,786 | `1adece96780fb62c` ✓ | 1,492,981 vs 1,492,979 (+2) | 0 |
| ja | 10,357,989 | `e58162ee734b63ac` ✓ | 54,698 | `a02ae6e46ddf3051` ✓ | 2,059,911 vs 2,059,919 (−8) | 0 |
| ko | 6,598,426 | `c50a994489749dc8` ✓ | 52,890 | `141a571cd9198e29` ✓ | 1,713,008 vs 1,713,006 (+2) | 0 |
| nl | 5,451,565 | `b08643e57063edd5` ✓ | 49,282 | `9b17f0577f3016d5` ✓ | 1,494,128 vs 1,494,129 (−1) | 0 |
| pt | 5,460,061 | `08492b6502ffda21` ✓ | 49,762 | `a3336a63f91c057c` ✓ | 1,502,568 vs 1,502,560 (+8) | 0 |
| ru | 5,638,728 | `92ad4ec2d045577c` ✓ | 62,036 | `be4f1ecfa424ec9c` ✓ | 1,678,638 vs 1,678,623 (+15) | 0 |

- **印 PDF：10/10 字节 + SHA 全值一致。text.md.new：10/10 字节 + SHA 全值一致。**
- 网 PDF：字节漂移 −15…+8 B（已知 webpdf 非确定性）；`pdftotext` 文本层 vs builder 原件 **10/10 diff 0 行**——漂移仅为元数据/排序。

## §4 D19（我的 D48 逻辑重核，不照抄 builder 结论）

同款 `d19_check.py`（仅改 S 路径）在当前 BUILD + KIT 上跑出 **TOTAL 16 PASS 10 FINDING 6**，与 builder 存档 `logs/d19-check.txt`（TOTAL 7 PASS 7 FINDING 0）不一致。查明原因如下：

- 引用总数：实际共 **16 处** = KIT 2 处（ja:71、ru:73）+ BUILD 14 处（§3 表 L105/L106、机制说明 L108、§4 表 L118–L124 共 7 行、§4 总结句 L126 ×2、§8 表 L181/L185）。
- Builder 的 "共 7 处" 是**实质引用**计数：2 KIT + §3 3 处 + §8 2 处 = 7，§4 表本身是核查记录，不计入——该计数正确；`logs/d19-check.txt` 是写 §4 表之前跑的（BUILD.md mtime 10:31:53 晚于 d19-check.txt 10:31:16），故 TOTAL 7 与当时文件一致，**不是造假，是陈旧**。
- 6 处 FINDING 全为检查器自指局限，实质均 PASS：
  - 5 处 "cannot infer reader"（§4 表 L120–L124）：表行不含 `\bja\b`/`\bru\b` 词符，检查器无法从行内推断读者；但所指内容行（content56.py:21、content34.py:200）均为真修复行。
  - 1 处 L126 总结句（双读者同句）："ja 的 `size=19.5` …；ru 的 `20 → 19.5` …"——检查器按行首读者码 ja 去核 ru 的 `20→19.5`，误判；句中两处引用实质均正确。
- **实质核查 16/16 PASS**：ja `content56.py:21` patched 行含 `size=19.5`、基线同行无 `size=`、行不同且在 fixlines 内（kwarg-added）；ru `content34.py:200` patched 19.5、基线 20、行不同（NN→MM）；其余提及行均指向实际修改行。修复行本身已逐行读过确认（见 §0 方法与 §1 run1→run2 前后对比）。

### F1 — D19 文本类 finding：BUILD §4 表第 6–7 行的位置号写错

| 行 | 表中写法 | 实际位置 | 结论 |
|---|---|---|---|
| §4 表第 6 行（L123） | "本报告 §8 表 L165"（content56.py:21） | §8 表 ja 行为 **L181**；L165 是 §7 每周词计数行，无此引用 | 位置号错 |
| §4 表第 7 行（L124） | "本报告 §8 表 L169"（content34.py:200） | §8 表 ru 行为 **L185**；L169 为空行 | 位置号错 |

表中第 3–5 行的位置号核对无误（§3 表 L105/L106、机制说明 L108 均与实际一致）。内容引用本身（content56.py:21、content34.py:200）全部正确，错的只是 §4 记录表的两个 BUILD 内部行号。按 D43：closer 落仓时原地修正（L165→L181、L169→L185）+ 针对性复验（重跑 d19_check；注意检查器会继续把 §4 表自指行计为 FINDING，属已知局限，复验以实质引用为准），不需整轮重校。

## §5 en 2 SPILL 基线核实（关键项：证实为基线先存残留，接受）

我独立在 builder 基线 en 版上跑 `spill_sweep.py`（只读输入，输出写我的 logs）：

| 处 | 盒 | 基线 | 我的重建 patched |
|---|---|---|---|
| P4 "exercise?" | 盒底 1358.0 | BELOW **+4.20px** x=1461.5 **y=1362.2 [SPILL]** | 同盒、同偏移、同文本：+4.20px y=1362.2 [SPILL] |
| P7 "the invitation stays open." | 盒底 1803.7 | BELOW **+6.30px** x=1461.5 **y=1810.0 [SPILL]** | 同盒、同偏移、同文本：+6.30px y=1810.0 [SPILL] |

- 基线 en 全量：2 SPILL / 115 OBSERVE；我的 patched en：2 SPILL / 132 OBSERVE（OBSERVE 差为 D5 新增拉丁元素，预期内）。两处 SPILL 在基线与 patched 中**逐元素同位**：SVG `<text>` 元素 x、y、font-size（20）、fill、文本逐字节相同，仅 font-family 由基线 `Noto Sans CJK TC` 变为 patched `Newsreader`（D5 机制本身，未移动元素）。
- **结论：两处 SPILL 均为基线先存残留，D5 未引入，接受。** 与 W45 前例同类处理一致。

附带核实（同法）：
- **ru run1 SPILL 确为 D5 引入**：我跑基线 ru spill_sweep = **0 SPILL**（122 OBSERVE）；builder run1 ru 日志：1 SPILL `'спортом?'` +4.20px y=1362.2（同盒底 1358.0）；修复后 run2 及我的重跑均为 **0 SPILL**（137 OBSERVE）。ru `content34.py:200` 19.5pt 渲染确认：我的 ru P4 SVG 中 "в неделю вы занимаетесь спортом?" 元素 y=1335.55、font-size=19.5、距盒底约 17.6px，两行。
- **ja P6 gloss +4.5px 确为基线原样**：基线 ja P6 元素 "キャッシュバックは割引ではありません。実" x=556.5、y=611.525、size=20.5；patched 同元素坐标/字号/文本逐字节相同，仅 font-family TC→JP。未动，正确。
- ja run1→run2 前后对比（builder run1 摘要 + 我的重跑）：run1 TOTAL 16/19，G12 FAIL defects=2（P5 +5.5px、P6 +4.5px）、G14 FAIL defects=1；修复后 run2 及我的重跑 G12/G14 均为 0 defects、TOTAL 18/19。修复有效。

## §6 D30 REFLOW（三件套，我的重跑逐版核实）

| 版 | print/web 字符多重集差 | pdfdiff（vs 已发网 PDF，trim 后） | joiner text.md 多重集差 | difflines |
|---|---|---|---|---|
| de | 0 | IDENTICAL | 0 | 108 |
| en | 0 | IDENTICAL | 0 | 32 |
| es | 0 | IDENTICAL | 0 | 302 |
| fr | 0 | IDENTICAL | 0 | 132 |
| it | 0 | IDENTICAL | 0 | 50 |
| ja | 0 | IDENTICAL | 0 | 500 |
| ko | 0 | IDENTICAL | 0 | 100 |
| nl | 0 | IDENTICAL | 0 | 42 |
| pt | 0 | IDENTICAL | 0 | 82 |
| ru | 0 | IDENTICAL | 0 | 510 |

**10/10 三件套齐全**：差异纯为 D5 换行（Newsreader 更窄）。G15a 记为 FAIL 是脚本按设计，D30 接受成立；G15c native verifier 10/10 ADOPT（rc=0）。

## §7 D52 字面（我重建的印 PDF + 网 PDF，逐版 pdffonts；svglib 源级计数）

| 版 | 印 PDF 面 | 网 PDF 面 | svglib index | 结论 |
|---|---|---|---|---|
| de/en/es/fr/it/nl/pt | NotoSans/SerifCJK**tc** + Newsreader16pt + CairoFont-0-0 | Newsreader + NotoSans/SerifCJK**TC** + Unifraktur | tc=2, sc/jp/kr=0 | ✓ TC 复现 |
| ja | NotoSans/SerifCJK**jp** + Newsreader16pt + CairoFont-0-0 | Newsreader + NotoSans/SerifCJK**JP** + Unifraktur | jp=2, tc/sc/kr=0 | ✓ JP 面（机制指定） |
| ko | NotoSans/SerifCJK**kr** + Newsreader16pt + CairoFont-0-0 | Newsreader + NotoSans/SerifCJK**KR** + Unifraktur | kr=2, tc/sc/jp=0 | ✓ KR 面（机制指定） |
| ru | NotoSans/SerifCJK**tc** + **NotoSans** (Bold/Medium) + Newsreader16pt + CairoFont-0-0 | Newsreader + NotoSans + NotoSans/SerifCJK**TC** + Unifraktur | tc=2, sc/jp/kr=0 | ✓ TC 复现 + 西里尔 Noto Sans |

**结论：10/10 字面符合，无缺陷。SC 面全家 0 处。** 新增面均为 D5 机制行为（Newsreader 拉丁、Noto Sans 西里尔、Unifraktur 仅网 PDF），不改变任何 CJK 文本字面。与 BUILD §5 一致；builder patched 原件 pdffonts 抽查（de/ja/ko/ru/en）结果相同。

## §8 §6 / §8 / KIT（含 census 修正核实）

- **§6 core 关系**：`style-port-zh-tw/MANIFEST-W46.md:15` 原文 "## zh-tw-en (CORE) — `core-zh-tw` doubles as the en-reader edition"；production 下无 `2026-w46-zh-tw-en/` 目录（9 个读者目录 + core-zh-tw）；core 内含 `2026-w46-zh-tw-en.text.md`；issues 下 10 个目录齐全。**证实 core-zh-tw 兼 en 读者版。** en 版源取 core（我的 en 重建即 2026-w46-zh-tw-en 目录，与 core 同源构建，SHA 见 §3）。
- **§8 同步表**：逐版 `diff -rq` patched vs production（9 源文件，KIT/text 另计）：**10/10 均为 8/9 不同**，不同者恰为 bslib4、content12/34/56/7/8、render、svglib，相同者均为 run.py。与 BUILD §8 一致。KIT 10/10 不同（D5 节追加）；text 导出字节与 BUILD §8 表一致（de 50,151 vs 47,681 … ru 62,036 vs 59,161）。
- **KIT census 修正核实**：10 份 patched KIT 的 "Baseline D5 census" 行逐份读过，与 BUILD §1 完全一致——de 602/0/1、en 577/0/0、es 603/0/0、fr 603/0/0、it 590/0/0、ja **283**/0/0、ko 282/0/0、nl 602/0/0、pt 596/0/0、ru **297/480**/0。**无一版误写 Latin 0，census bug 已修。** KIT 门禁行亦一致（de run1 18/19、en run1 17/19、ja/ru run2 18/19）。
- **§9 SHA 为修正后交付物的值**：§3 核对的即修正后交付物——印 PDF 与 text.md.new 10/10 全值一致（KIT census 修正后重建的 deliverables），pt 亦然。

## §9 D18 / D37 复测

- **D18**：我的重跑全版最小间隙 **21.0px**，gaps [42.0, 42.0, 42.0, 21.0]；en 为 6 值 [42.0×3, 21.0×3]（副标题含 3 个 U+3000 段，y=378 分隔符已计入——strip bug 修正后的行为已复现）。全版 PASS。
- **D37**：全版最小边距 31.5pt（同一中文行，y≈1423–1453，盒 y=1128）；内容边最小 20.6px（9 版），**it 例外 3.5px**。it 元素 "Parola della settimana" 在我的 it P1 SVG 中 y=1750.0、x=1586.5、size=25，与 BUILD 所述一致；我的 measure.json：`content_edge_min_margin=3.5`，D37 PASS；G6 遮挡 0 旗标。**确认 > 0 且无遮挡，PASS。**
- **残留**：G15b 仅记录（pt rc=2，我的重跑复现——共享 verifier 无 pt 读者表，D27）；ko G11 OBSERVE 178、SPILL 0（我的重跑复现，全家最多，SPILL 0）；pt 交付物 SHA = §9（§3），基线事故无残留。

## §10 结论 + finding 清单

**结论：PASS。**

- 独立重建 10/10（rc=0、TOTAL=150）；印 PDF 10/10 字节+SHA 全值一致；text.md.new 10/10 字节+SHA 全值一致；网 PDF 文本层 10/10 diff 0。
- 全门禁重跑 10/10：归一化 diff 0 行；终轮 9×18/19、en 17/19，与 builder 终轮逐值一致；唯一 FAIL 全版为 G15a REFLOW（D30 三件套齐全，接受），en 另 2 SPILL 为基线先存（§5 证实）。
- D19 实质 16/16 PASS；D52 10/10 符合；§6/§8/KIT（含 census 修正）10/10 证实；D18/D37 复测通过。

**Finding 清单（1 项，D19 文本类；D43 处理，不需整轮重校）：**

- **F1**：BUILD §4 D19 表第 6–7 行的位置号错误——"§8 表 L165" 应为 **L181**（ja 行），"§8 表 L169" 应为 **L185**（ru 行）。内容引用本身全部正确。Closer 落仓时原地修正这两处行号 + 针对性复验（重跑 d19_check；§4 表自指行仍会被检查器计为 FINDING，属已知局限，以实质引用为准）。另注：`logs/d19-check.txt`（TOTAL 7）是写 §4 表之前的跑批，陈旧但与当时文件一致；修正后建议重跑刷新。

**未核实**：无。全部核查项均有实测证据。

**运行记录**：重建循环一次被运行体重启中断（pt 中途），`--resume` 续跑完成；磁盘 75G/150G，终盘未超 100G 门；builder 文件未动；无 commit/push。
