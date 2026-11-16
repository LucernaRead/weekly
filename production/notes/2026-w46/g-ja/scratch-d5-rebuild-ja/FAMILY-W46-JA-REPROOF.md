# W46 日语目标家族 D5 重校报告（独立重校）

- 家族：W46 ja（目标语 ja，读者 de/en/es/fr/it/ko/nl/pt/ru/zh-cn/zh-tw；无 ja 读者）+ core-ja
- 重校工作目录：`hidden_files/d5-redo/scratch-2026-w46-ja-reproof/`（`reproof/patched/` 为 builder `patched/` 源文件的独立副本，`reproof/logs/` 为全部重校输出；builder 文件、production、issues 均只读，未改动——`find scratch-2026-w46-ja -newermt '2026-11-16 01:35 UTC'` 为空）
- Builder 报告：`FAMILY-W46-JA-BUILD.md`（全文通读，以它为准绳逐项复核）
- 结论：**PASS**（0 内容/门禁 finding；D19 文本类 finding 0 条；残留项均为记录类，见 §8）
- 磁盘：开工 74G 已用，收尾 74G 已用（<100G 门）

## §0 方法

- 独立重建：`rsync` builder `patched/` 源文件（不含 PDF/text.md.new/svg/`__pycache__`，`diff -rq` 核对 SOURCES-IDENTICAL）→ `reproof/patched/`，用 builder 同款流程（`bin/build-one.sh` 只读调用，日志写我方 `reproof/logs/build/`）重渲印 PDF + 网 PDF + `textexp_ja.py` 导出 text.md。11/11 `rc=0/0/0`。
- 全部门禁：builder `bin/gates_ja46.py` 只读调用（输出写我方 `reproof/logs/gates/<slug>/`，基线对照读 builder `baseline/` 只读），19 verdict/版。
- D19：我方改写版 `reproof/bin/d19_check_reproof.py`（D48 修正逻辑 + 括号容忍正则；KIT/content 取我方副本，`fixes-applied.jsonl`/基线只读；输出写我方 `reproof/logs/d19-check.txt`）。
- D41：我方 `reproof/bin/d41_check_reproof.py`（`occlusion_audit.ink_box` 墨量测 + 三方 SVG 对照）。
- D37-sub：`measure_ja46.py` 只读调用（输出写我方 `reproof/logs/d37/`）+ PDF 字符原点/像素双重复核。

## §1 逐版门禁复核表（重校独立跑，run2）

门禁循环 `reproof/logs/gates-all-reproof.log`，11/11 ALL-GREEN（G15b 除外，D27 记录项）。G1–G10、G12–G14 全版 PASS，值与 builder 终轮逐值一致（归一化 diff 见 §2）：G1 TOTAL 150/FLOW 0/HEAD 0；G2 defects 0；G7 150/150；G8 CLEAN keydiff [137,138]（zh-tw [138]，zh-cn []）；G9 8/8；G12 DEFECT 0；G13 0 TOUCH/0 NEAR；G14 defects 0/observes 0；G16 defective 0；P8 max_y 2624.0、余量 76.0px。关键值下表（括号内为 builder 终轮值，全部一致）：

| 版 | G3 | G6 | G11 SPILL / OBSERVE | G15a pw / pi / pdfdiff | G15b rc | G15c | D18 gap | D37 y612 / sub | P8 元素 |
|---|---|---|---|---|---|---|---|---|---|
| de | latin 0, curly 0 | flags [] | 1 / 94，同基线集 | 0 / 125, IDENTICAL | 1 | ADOPT | 297.9px | −1111.5 / −55.4pt | 867 |
| en | latin 0, curly 0 | flags [] | 1 / 97，同基线集 | 0 / 125, IDENTICAL | 1 | ADOPT | 318.4px | −1136.6 / −50.7pt | 862 |
| es | latin 0, curly 0 | flags [] | 1 / 89，同基线集 | 0 / 125, IDENTICAL | 1 | ADOPT | 291.3px | −1076.4 / −8.0pt | 875 |
| fr | latin 0, curly 0 | flags [] | 1 / 92，同基线集 | 0 / 125, IDENTICAL | 1 | ADOPT | 276.3px | −1149.5 / −33.2pt | 868 |
| it | latin 0, curly 0 | flags [] | 1 / 91，同基线集 | 0 / 125, IDENTICAL | 1 | ADOPT | 280.5px | −1067.3 / −98.1pt | 870 |
| ko | latin 0, curly 0 | flags [] | 1 / 152，同基线集 | 0 / 125, IDENTICAL | 1 | ADOPT | 335.5px | −1165.4 / −290.1pt | 2353 |
| nl | latin 0, curly 0 | flags [] | 1 / 90，同基线集 | 0 / 125, IDENTICAL | 1 | ADOPT | 305.6px | −1105.4 / −27.9pt | 872 |
| pt | latin 0, curly 0 | flags [] | 1 / 92，同基线集 | 0 / 125, IDENTICAL | 2 | ADOPT | 291.8px | −1132.8 / −0.9pt | 874 |
| ru | latin 0, cyr 0, Noto Sans 711 | flags [] | 1 / 93，同基线集 | 0 / 125, IDENTICAL | 1 | ADOPT | 277.4px | −1068.3 / −69.2pt | 2405 |
| zh-tw | curly_total 2, curly_in_CJK 0 | flags [] | 1 / 98，同基线集 | 0 / 141, IDENTICAL | 2 | ADOPT | 315.3px | −1182.3 / −287.0pt | 1298 |
| zh-cn | curly_total 2, curly_in_CJK 0 | flags [] | 1 / 98，同基线集 | 0 / 132, IDENTICAL | 1 | ADOPT | 315.3px | −1182.3 / sub N/A | 1299 |

- G10 latin_added：de 208、en 214、es 207、fr 210、it 212、ko 92、nl 208、pt 210、ru 81、zh-tw 80、zh-cn 88；cjk_added 全 0（与 builder 一致）。
- G14 p8rows：de 840→859、en 835→854、es 848→867、fr 842→860、it 843→862、ko 2213→2332、nl 845→864、pt 847→866、ru 2378→2397、zh-tw/zh-cn 1225→1288；页脚余量不变（与 builder 一致）。注：BUILD §4 ru 表的“P8 2397”为 G14 p8rows 值，重校 P8 元素数 2405 与 builder `run2-summary.json` 的 p8 值一致，无出入。
- G11 spill 集：11 版均为 P5 BELOW 17.74px 同一行 `の回答）によるものです。`（框底 762.0，行 y=779.7），与基线 spill 集逐项相同（`same set`），先存几何成立，D5 零引入。

## §2 归一化 diff：0 行

我方 `GATES-SUMMARY.txt` vs builder `logs/run2-gates/*/GATES-SUMMARY.txt`：归一化（剥离 G4/G5 字节数与短 SHA、印/网 PDF 摘要行）后 **11 版 diff 0 行**（`reproof/logs/run2-summary.json` 为我方汇总）。G15a/G15c 行未归约——逐值一致（含 vs_issues 多重集差分解 `·`124 + `—`1；zh-tw 141 = `·`124 + `／`8 + `/`8 + `—`1；zh-cn 132 = `·`115 + `／`8 + `/`8 + `—`1）。

## §3 交付物 SHA 核对表

| 版 | 印 PDF（字节 / SHA-256） | text.md.new（字节 / SHA-256） | 网 PDF（字节 / 与 builder 差） |
|---|---|---|---|
| de | 24,212,672 / ``861832c2…3ad7` MATCH | 46,228 / ``8481f9bb…6d69` MATCH | 2,165,894 / +15B |
| en | 24,205,030 / ``c8491232…8217` MATCH | 45,421 / ``08bded92…8e95` MATCH | 2,158,345 / +9B |
| es | 24,213,421 / ``6e90549c…206c` MATCH | 46,996 / ``7bd9da14…8a68` MATCH | 2,166,704 / −1B |
| fr | 24,211,949 / ``ac61b957…16ec` MATCH | 46,910 / ``cfb09507…5712` MATCH | 2,165,547 / +3B |
| it | 24,204,487 / ``a60532e7…60a8` MATCH | 46,769 / ``f4c570de…ff52` MATCH | 2,157,693 / +11B |
| ko | 26,157,353 / ``1192bd9e…857e` MATCH | 47,808 / ``2ba8a376…b3dd` MATCH | 2,324,071 / +15B |
| nl | 24,207,002 / ``411cc7d7…1b21` MATCH | 46,030 / ``473f9969…5eca` MATCH | 2,160,245 / +7B |
| pt | 24,214,993 / ``3a877c06…2d09` MATCH | 46,819 / ``b21c91fc…8834` MATCH | 2,168,460 / +5B |
| ru | 24,375,615 / ``236107cf…8c2f` MATCH | 53,505 / ``ca05c834…bd87` MATCH | 2,326,339 / +43B |
| zh-tw | 24,387,005 / ``a6881fa8…f134` MATCH | 44,018 / ``09f7d430…c4a5` MATCH | 2,534,480 / +8B |
| zh-cn | 24,369,825 / ``0630eb38…6875` MATCH | 44,048 / ``b35f8fbd…452a` MATCH | 2,418,537 / −2B |

- **印 PDF 11/11、text.md 11/11 与 BUILD §9 全值逐字节一致**（SHA-256 全值核对，非仅前缀）。
- 网 PDF 11/11 字节漂移 −2…+43B，属 webpdf 非确定性（时间戳/ID），内容等价由 G15a 证实（印=网多重集差 0 + pdfdiff IDENTICAL，11/11）。
- 内容抽查：§7 探针 33/33 双向在位（重建 text.md.new vs 已发 text.md，空白归一）。

## §4 D19 引用重核（D48 修正逻辑）

工具：`reproof/bin/d19_check_reproof.py`（rc=0，`reproof/logs/d19-check.txt`）。结果：

- **引用在位：46/46**（11 份 KIT 内全部 `content*.py:NNN` 引用 + BUILD 报告内全部引用，逐行核对我方副本；与 builder 所称 46/46 一致）。
- **D5 修复严格+引用：15/15**（F1 ×11、F2/F3/F4/F5 各 1）。p.text 引用行本身含新字号字面且基线同行含旧值；f.box（it `content12.py:51`）引用行即收尾行 `], tsize=22)`，基线同行 `])` 无 `tsize=`（`tsize added` 形通过）；15 处均在其版 KIT D5 节与 BUILD 修复表中有引用。
- **报告修复表旧/新字号值：15/15**（含散文体 `18.5→18.0` 6 处与表列 `tsize 23（默认）→ tsize 22` 1 处——括号容忍正则 `(?:\uff08[^）]*\uff09)?` 生效；W46 ru 先例的同类适配）。
- **Finding：0 条**（无文本类 finding，无内容/门禁类 finding）。

## §5 D55 / D53 字体面核实

- **zh-tw（D55，已裁定接受，独立证实）**：重建印 PDF `pdffonts`：Newsreader 17 + NotoSansCJKjp Bold/Regular ×8 + NotoSerifCJKjp Bold ×7/Regular ×8 + Unifraktur 1，**TC 0 处、JP 面**；网 PDF 同样 JP-only（Newsreader 17 + JP Sans/Serif + Unifraktur 1）。已发版核实为 JP+TC 双面：Sans JP Bold/Regular ×8、Sans TC Bold/Regular ×8、Serif JP Bold/Regular ×8、Serif TC-Regular ×1、Unifraktur ×1，与 BUILD §0.3 逐数一致。文字层与已发版一致（G15a pdfdiff IDENTICAL + G15c ADOPT，11/11 含 zh-tw）；剥离 face 未改文案（G15a/G15c + 内容抽查 3/3）。**JP 面不是缺陷，不列为 finding。**
- **ko（D53）**：重建 ko 印 PDF 面 = builder patched = 已发版，三方一致：Newsreader 16 + NotoSansCJKjp ×16 + NotoSerifCJKjp ×15 + Unifraktur 1，**无 KR 面嵌入**；`_D5_READER="cjk"`，CJK 子字体为模板安装的 JP（`_jp_index`，`svglib-ja-d5.py` 模板）；韩文读者文本（매주、포키）以 Noto Sans CJK JP 渲染，与已发版一致。D53 所述 SC→KR 为机制规定，接受、不质疑；本家实测与已发一致即通过。
- **ja 面**：SC→JP 与已发 JP 面一致（de/ko 等版印 PDF 均为 JP 面，无 SC 面残留）。

## §6 D47 核实：不适用，11 版全 0

| 版 | 已发 text.md `###` 行数 | `##` 行数 | 总行数 |
|---|---|---|---|
| de/en/es/fr/it/ko/nl/pt/ru/zh-tw/zh-cn | 0（11 版全 0） | 8 | 1357/1348/1363/1353/1360/1332/1361/1363/1364/1326/1329 |

与 BUILD D47 节逐值一致。`textexp_ja.py`：grep `###` 0 命中、grep `24` 0 命中，无 `###` 逻辑、无 24pt 阈值。无丢失行可补，无补行任务。

## §7 D41 ru F5 核实：run1 真缺陷，F5 已修

- **基线同位对照（实测）**：基线 ru P8 眉题行（Noto Sans CJK JP 25px，x=88）墨右缘 **1020.2**，`Короткое…` 行 x=1032.3、墨左缘 1032.3，余量 **+12.0px**；基线 occlusion flags []。基线干净，与 BUILD 所称一致。
- **run1 真缺陷重建（实测）**：run1 布局中 `答え`（3 字 × 25px）使 `Ответы` 元素 x=163；墨探针（`occlusion_audit.ink_box`，逐元素模型）：25px Noto Sans 时墨右缘 **1048.5**，`Короткое…` 墨左缘 1010.7，实隙 **−37.8px**——与 builder run1 门禁日志的 G6 旗标逐值一致（box [163.0, 1282.2, 1048.5, 1308.0]，`ink overlaps … by 37.8x18.8px`）。另有独立证据：run1 G15c HOLD（词元合并 `номерКороткое`）。定性：**真缺陷**，非量测 artifact。
- **F5 修复后（实测）**：`content8.py:114` 25→23.5；重建 ru P8：`Ответы` 元素 x=158.5、墨右缘 990.8，`Короткое…` x=1010.7，余量 **+20.0px**；builder patched 与我方重建逐值相同；三方 occlusion 均为 flags []（基线 / builder patched / 重建）。run2 G6 flags []、G15c ADOPT。
- 探针口径注记（非 finding）：builder 报告的 24px −2.3 / 23.5px +15.5 是按 run1 固定 x=163 的保守探针；真实几何下（`答え` 字宽随字号收缩，`Ответы` x 随之左移）余量为 24px **+0.7**、23.5px **+20.0**。23.5 仍是正确选择（24px 仅 +0.7 过于边缘）；修复本身与门禁结论不受影响。
- 其余 10 版 run2 G6 均为 flags []，无 D41 事项。

## §8 §6 core-ja / §8 同步清单 / KIT pin 核实

- **§6 core-ja**：production `2026-w46/` 内无 `2026-w46-ja-zh-cn` 目录；`core-ja/` 含 `2026-w46-ja-zh-cn.text.md` + WEEKLY-KIT.md；已发 zh-cn PDF（8 页）fitz 实测：P1 标语含 `每周一期`（`毎週、日本語で· 每周一期· 日本人が読んでいる日本語を読む`），无读者徽章行（`日語正文` 0 命中），页脚 `Lucerna · 日语周报VOL.3 · LUCERNA JAPANESE WEEKLY`。core-ja 构建 (ja, zh-cn) 成立；zh-cn D37-sub N/A（无副刊头行）与 builder 一致。
- **§8 同步清单**：`diff -rq patched/ vs production/2026-w46/`（排除 `__pycache__`/svg/cards/PDF/`.text.md`/assets/JPG；逐文件统一 diff 存我方 `reproof/logs/diff-full/`）。每版差异文件恰为 9 件（KIT、svglib、bslib4、content12/34/56/7/8、render.py）；`transform.py`/`run.py` 与生产版逐字节相同（zh-tw 与 core-ja 两侧均无 `transform.py`，与 builder 所称一致）；ABSTRACT.txt、JPG 不同步；生产侧独有文件（各版 `ja-*-freeze.json`/`ja-*-occlusion.json`/`ja-*-p8compare.json`、core-ja 的 `fix/`、`fix-round3/`、`proofread-gates*` 等）不动。
  - 行差：统一 diff（不含 KIT）de/en/es/fr/ko/nl/pt/ru 691 行、it 693 行、zh-tw 789 行、core-ja 689 行；builder 报告为 697/699/803/695。**差额纯属 diff 对齐口径**：builder 的 diff 把空行与一行移位行计为变更，我方 diff 将其配为上下文/同行。证据：非空 `+`/`-` 行集合 10/11 版与 builder `logs/diff-full/` 逐项相同（symdiff 0）；zh-tw 仅差 2 行，即 bslib4.py 中 `return self.y` 一行——两文件各含 5 处、仅行号平移，builder 的 diff 将其计为一对 `-/+`，我方配为上下文，内容无差。KIT 为纯追加 40–41 行（D5 节），剥离 D5 节后旧章节与生产版逐字节相同（11/11）。
  - 行差主体为 D1 移植；D5 修复本身每版仅 1–2 行（it content12 +58/−57 中多出的 1 行为 F4 `tsize=22`；es/fr/ru 的 content7/content8 多行对应 F2/F3/F5）。
  - `render.py` 按 D54 同步：生产版 BASE 为仓外死路径，patched 版为 ED-相对 + 内调 webpdf（11 版同）。
- **KIT pin**：11 份 KIT 与 builder patched 侧 SHA-256 前 16 位逐份一致；KIT 内 D5 节在位（`## 补记：D5 字体重建（2026-11-15）` + 交付物 pin 块 + 各版修复引用，含旧引用 `content34.py:95`）；KIT pin 的印 PDF 全 SHA 与 text.md 全 SHA 与我方重建值 11/11 一致（网 PDF pin 为 builder run2 值，我方重建漂移 −2…+43B，见 §3）。

## §9 pt D37-sub 复核

- 门禁口径（`measure_ja46.py`，advance 模型）：我方重建 pt **−0.9pt（end 1438.6，限 1439.5）PASS**、es **−8.0pt（end 1431.5）**，与 builder 终轮逐值一致；其余版 sub 余量 −27.9…−290.1pt。
- 像素/实墨复核（PDF 字符原点 + 300dpi 列投影 + 刊头带目视）：pt 副刊头行末 span（`PORTUGUESA`）实墨右缘 SVG **1446.9**，即名义线 1439.5 外 **+7.4** 单位；es 实墨右缘 **1439.49**（线内 0.01）。成因：`text_w` 对 Newsreader 全大写行的 advance 模型比 PDF 实际字宽窄约 1.1%（该行模型 732.8 vs 实际 741.1）；基线 pt 实墨右缘 1393.5（advance 口径 −50.0），D5 加宽所致与 builder 所称一致。
- **无遮挡**：y≈356、x 1439–1470 带内无任何元素（无盒、无字、无规则线；规则线在 y=420）；刊头带渲染目视：副刊头行完整、无截断、无重叠，G6 flags []、G13 0 TOUCH/0 NEAR。**门禁口径 PASS 且无遮挡，结论成立。**
- 残留观察（非门禁 finding）：D37-sub 的 advance 口径在 pt/es 两版上低估实墨约 8 单位；pt 实墨已越名义线（空白处，无可见缺陷）。建议后续 D37-sub 改用实墨/实际 advance 量测；本次无需重建。

## §10 残留项（仅记录类）

1. **G15b（D27，已知工具缺口，不阻塞）**：重校复核 9 版 rc=1（de/en/es/fr/it/ko/nl/ru/zh-cn）、2 版 rc=2（pt/zh-tw，无读者表），与 builder 一致。验收以 G15a + G15c + 全读为准。
2. **G11 spill 1/版**：P5 `の回答）によるものです。` BELOW 17.74px，先存几何；重建集 == 基线集，D5 零引入。
3. **zh-tw/zh-cn G3 curly_total=2**：已归 Newsreader 的弯引号（fix2 既定态），curly_in_CJK=0，G16=0，非违规。
4. **P2 中页空白**：基线 de 83.3px = 重建 83.3px = builder patched 83.3px（`p2gap_ja.py` 实测；ru 53.6px 系内容流差异）；29.2px 为 D1 前生产值，D5 零变化。已 reopen 待 redesign，非 D5 发现。
5. **zh-tw TC 面（上报协调员，BUILD §0.3）**：已发 TC+JP 双面、D5 模板 JP-only，本家按 W45 先例剥离 face；重校独立证实重建为 JP-only、文字层一致。若协调员裁定须复现 TC 面，需机制侧 TC 分支模板后重做 zh-tw 一版。
6. **pt D37-sub（见 §9）**：门禁口径 PASS（−0.9pt），实墨越名义线 +7.4 单位（空白处，无遮挡、无可见缺陷）；建议后续改实墨量测。
7. **印/网 PDF 字节非确定性**：网 PDF 漂移 −2…+43B；§3 以重建实测为准；closer 复制 builder 原件，绝不重跑 webpdf。

## §11 Finding 清单

| 编号 | 版/门 | 缺陷 | 证据 | 修复建议 |
|---|---|---|---|---|
| — | — | **无** | — | — |

## §12 事故记录

1. **服务重启杀死重建循环**（约 02:00 UTC，11-16）：重建进行到 pt 版 render 步骤时进程消失（pt 无 PDF 落盘，其余 7 版已完成 rc=0）。处置：按 builder run2 事故同类先例单独续跑未完成版（`reproof/bin/build-resume-reproof.sh`：pt、ru、zh-tw、zh-cn），4 版全部 rc=0/0/0；pt 重建后印/text SHA 与 builder 全值一致。另有一次同源的等待命令被重启打断（仅 sleep，无副作用）。
2. **D19 表值解析初版误判**：初版只认箭头形 `NN→MM`，BUILD 报告修复表为分列旧/新字号（+ 散文体 `F1 同 de（…，18.5→18.0）`），初跑 0/15；修正为表列解析 + 箭头形回退（含括号容忍）后 15/15，rc=0。属重校脚本自身修正，不影响 builder 交付物。
3. **zh-tw `transform.py` 误报**：初版 `cmp` 因两侧均无此文件报 DIFFERS；核实两侧均无文件，与 builder 所称一致，非问题。

## §13 交付物核对表

| 交付物 | 位置 | 状态 |
|---|---|---|
| 本报告 | `hidden_files/d5-redo/FAMILY-W46-JA-REPROOF.md`（§0–§13） | ✅ 完成 |
| 重校脚本 | `scratch-2026-w46-ja-reproof/reproof/bin/build-all-reproof.sh`、`build-resume-reproof.sh`、`gates-all-reproof.sh`、`collect_reproof.py`、`d19_check_reproof.py`、`d41_check_reproof.py`（全部写盘只在 `reproof/`） | ✅ 完成 |
| 重建源 + 产物 | `scratch-2026-w46-ja-reproof/reproof/patched/`（11 版 SVG、印/网 PDF、text.md.new） | ✅ 完成（印 11/11、text.md 11/11 与 BUILD §9 逐字节一致；网 PDF −2…+43B） |
| 重建/门禁总日志 | `reproof/logs/build-all-reproof.log`（7 版一次完成 + 4 版重启后续跑）、`reproof/logs/build-resume-reproof.log`、`reproof/logs/gates-all-reproof.log`（11/11 ALL-GREEN） | ✅ 完成 |
| 门禁日志 | `reproof/logs/gates/<slug>/GATES-SUMMARY.txt` + `gates.json` + 各门日志 | ✅ 完成（11/11 ALL-GREEN，G15b 除外） |
| 专项核查 | `reproof/logs/d19-check.txt`（46/46、15/15、15/15）、`reproof/logs/d41/d41-ru.json` + `occlusion-*.json`（基线 +12.0 / run1 −37.8 / run2 +20.0）、`reproof/logs/d37/*.json`（pt −0.9 / es −8.0）、`reproof/logs/diff-patched-vs-production.txt` + `reproof/logs/diff-full/*.diff` | ✅ 完成 |
