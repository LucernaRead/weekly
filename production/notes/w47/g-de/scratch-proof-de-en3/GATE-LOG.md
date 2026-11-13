# GATE-LOG — proof3，Lucerna Weekly 2026-W47 de-en（rebuild 6，fix2 后）

- 复校员：proof3；时间 2026-11-11（EST 上午，任务 05:29 EST 到达；fix2 06:23–10:30 UTC 提交 `4ff1cf7f` 在前）
- 对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-de-en/`
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`；`TMPDIR=<scratch>/tmp`，绝未写 /tmp；中间件一律在本 scratch 目录。
- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…` rc=0；本目录 `probe.txt` 真实写成功。

## 对象核对（开工 + 收尾两次）

| 文件 | 大小 | SHA-256 | 与任务值 |
|---|---|---|---|
| Die-Lucerna-VOL4-de-en.pdf（印刷） | 10,966,410 B | `c8904dea16d2474afdd6629789af266eabfa5d5b9ea06813d9b0fd95e38722cd` | 一致 |
| Die-Lucerna-VOL4-de-en-web.pdf（网页） | 1,597,904 B | `2c190c75c61f9dbc75db62b251cb07ba965f98866425bcd287cab08f423d9f3a` | 一致 |
| 2026-w47-de-en.text.md | 49,665 B | `f3f0c08455b647c9b8f2844fbf16c33008e2717f30c584d7a3b835f98cb8a53e` | 一致（与 fix1 相同） |

收尾 re-check：同一 SHA；未改动版目录任何文件；`git status` 见 PROOF-NOTE 末尾。

## 闭引号 D1/D2 像素重测（定稿）

方法：400 dpi 印刷 PDF 墨列法——以引号自身 y 带为窗口，取「“」字形的第一墨列（两个逗点团的第一团左缘）与前一字母墨列右缘之差，减 1 px 量化（0.18pt/px）；另以 PDF rawdict 字符 advance 框交叉验证字形归属；200 dpi / 400 dpi 裁切目视。

| 实例 | 字体/字号 | 前空隙（实测） | fix2 宣称 | 目视 |
|---|---|---|---|---|
| D1 P8 H 框 „My week in November" | Newsreader 15.00pt（独立 `<text>“</text>`） | **0.18pt = 0.012em**（r 墨止 450.90 → 引号第一团墨起 451.26，1 像素空） | 0.18pt / 0.01em | 贴紧，无白洞，无触碰 |
| D2 P8 键 67 „Im Lande des Christkinds" | Newsreader 9.94pt（独立 `<text>“</text>`） | **0.72pt = 0.072em**（s 墨止 455.76 → 引号第一团墨起 456.66，4 像素空） | 0.72pt / 0.07em | 贴紧，无白洞，无触碰 |
| 对照 P8 对话 „Eine stille, schöne Woche", | Newsreader 14.62pt | 前空隙 **1.44pt = 0.098em**（e 墨止 500.58 → 第一团 502.20）；后空隙 1.26pt | fix2 引「1.26pt = 0.09em」为对照 | 同型，贴紧 |

字形结构（rawdict 字符框确认）：`“`（Newsreader）在 x 投影上恒为两个逗点团——D1 (451.26–453.42)+(454.14–456.12)，D2 (456.66–457.92)+(458.46–459.90)，对照 (502.20–504.36)+(504.90–507.06)。D1 第二团 (454.14–456.12) 位于引号 span advance [450.52, 457.14] 内、句点 advance 起点 457.14 之前，确为引号第二逗点，非句点；本轮初测 `quote_pixel3c.py` 曾误取第二团为“引号墨起”报 0.36pt（D2），系脚本取团 bug，profile 数据已推翻，不作证据。

**fix2 对照引用注记（非缺陷）**：fix2 报告的对照值 1.26pt 是对照组 `Woche“,` 的**后**空隙（引号→逗号），不是前空隙；对照组真前空隙为 1.44pt = 0.098em。结论不变（D1 0.012em 仍偏紧于对照带、但为正且无触碰；D2 0.072em 落在带内），仅 fix2 日志的引用口径需纠正。已废弃测量：`quote_pixel3.py`（D2 未找到、D1 取团错）、`quote_pixel3b.py`（以 span advance 框为墨起、吞并前字母墨迹、报前空隙 0px）。

## 机械门

| # | 门 | 命令 / 方法 | 结果 | 日志 |
|---|---|---|---|---|
| 1 | occlusion 正式审计 | `occlusion_audit.py`（内建自检 6 类植入均触发） | **0 flags，rc=0** | `gates/occlusion.log` |
| 2 | p8 extract | `p8.py extract --total 150` | 本版 150/150，core 150/150 | `gates/p8extract-ed.json`、`gates/p8extract-core.json` |
| 3 | p8 compare | `p8.py compare --total 150` | **CLEAN**；missing=[]、extra=0；keydiff=[137,138,139,150] 均预期（Q137–139 E 组翻译键为英文；Q150 开放题标签） | `gates/p8compare.json` |
| 4 | freeze.py diff | `freeze.py diff --core-svg core-de/svg --edition-svg de-en/svg` | rc=0；新增 CJK 共 7 个，均为 U+3000（P2–P8 各 1，P1 为 0）；P8 +152/−137（proof2 +148：+4 为 fix2 拆出的独立引号 `<text>` 串） | `gates/freeze-diff3.log` |
| 5 | freeze 直接层（渲染） | `scans3.py` 冻结交集 | **8/8**：P1 147 `083e2a2a`、P2 163 `689045ad`、P3 195 `fc88f676`、P4 166 `df1bebf7`、P5 173 `86fa4421`、P6 175 `2bbe05f9`、P7 150 `b7aa0771`、P8 186 `57e118e7`；计数与 SHA 与宣称完全相同 | `gates/scans3.log` |
| 6 | freeze 源层级 | `freeze_source_reg.py`（AST 字面量 + REG 复现） | **PASS**：core 字面量 2389 / 版 2397；core 无 CJK 字面量缺于版 = 5，皆预期（刊头副标、（、）、` · `、`Die-Lucerna-VOL4-de.pdf`）；版新增无 CJK 字面量 449，61 个含非 ASCII，抽样均为德词+英文释义串（含 D2 串 `The 1903 calendar: „Im Lande des Christkinds"`）；REG 150 题复现、编号 1–150 连续、copy SVG 与版 SVG 8/8 字节相同 | `gates/freeze-source-reg.log`、`gates/freeze-source.json`、`gates/reg-mine.json` |
| 7 | measure.py en | `scratch-fanout-de/measure.py en <版>` | **24/24 PASS，0 FAIL** | `gates/measure3.log` |
| 8 | creambox（canonical 全版） | `hidden_files/w47/tools/creambox.py <版>/svg/*.svg` | **NO OVERFLOW**：全部 27 个奶油盒 inside-only 清除量为正（最小 +10.4 P7 LESERBRIEFE；P7 工具盒 +16.0，desc-clear +9.9，未回退）；BELOW-WINDOW 行 10 条，偏移均为 +24.0～+44.9（已知误报带：下一标题/练习编号），无 +12～+18 整行溢出；P7-TOOLBOX 汇总：6 盒，最小 inside +10.4、最小 desc-clear +4.5 | `gates/creambox-canonical.log` |
| 9 | P8 最小字号 | PyMuPDF 逐页（render_extract3） | **9.94pt ≥ 9.75pt**；各页最小值 11.62/12.75/11.62/11.62/11.62/12.75/11.62/9.94 | `gates/p8font.json` |
| 10 | 印/网文字层一致 | pdftotext 默认 + raw，逐页词 multiset | 默认 50,433B = 50,433B；raw 均为 49,277B，归一化相同；逐页 P1–P8 词 multiset 全部相同 | `gates/print.txt`、`gates/web.txt`、`gates/scans3.log` |
| 11 | abutting | 逐页词 multiset + span 坐标位移（abutting3.py） | **PASS**：8 页词 multiset 相同，最大位移 **0.20pt**（P1 'Die Lucerna'），无计数不符；P6 图表 strip 像素差 max 0、mean 0.0（像素全同） | `gates/abutting3.log` |
| 12 | chips | rx="2.7" 计数 | 10/15/18/15/18/18/12/35，总计 **141**；P8 A2 22 / B1 13 | `gates/scans3.log` |
| 13 | 弯标点 | 全版字符计数（8 幅 SVG、text.md、两版 PDF 文字层） | U+201D = **0**；U+2019 = **0**；U+201C = U+201E = **35**（P1 5/5、P5 6/6、P7 21/21、P8 3/3）；core-de U+201C=33（P8 1），多出的 2 个恰为 D1/D2；其余 33 对与 core 一致 | `gates/q34-quotes.log`、`gates/scans3.log` |
| 14 | Q34 防回退 | 五处计数 | 新单数 `"Am Montag öffnet in Köln der erste ___."` 各 1×、旧复数 0×：content34.py、text.md、P3 SVG、印刷 PDF、网页 PDF 全过；core 亦新 1×/旧 0× | `gates/q34-quotes.log`、`gates/scans3.log` |
| 15 | D1/D2 键 | keycheck3 | Q67 键 B 三方一致；Q8 键 A 三方一致；Q56 键 mehr 三方一致 | `gates/keycheck3.log` |
| 16 | 盒标题 7/7（SVG 实测） | `boxtitle3.py`（`svglib.text_w(..., kind="sans")`） | **7/7**：394.6 / 359.9 / 262.5 / 397.9 / 382.9 / 352.8 / 366.1（预算 400.5px）；最紧 P5 ADVENTSWÖRTER 余 2.6px | `gates/boxtitle3.log` |
| 17 | 盒标题 7/7（共享 tr_en.py） | `boxtitle.py en` | **7/7 fit**，数值与 SVG 实测逐项相同 | `gates/boxtitle-shared3.log` |
| 18 | 150 题键核对 | `keycheck3.py`：自建 REG vs builder `en/keycheck-150.json` | **0 差异**（n/page/level/type/key 逐项） | `gates/keycheck3.log` |
| 19 | 150 题键核对 | REG vs P8 提取 | **149/150** 完全一致（仅 Q150 开放写作题被提取器截为 "Open task"，预期） | `gates/keycheck3.log` |
| 20 | verify_repro | 逐字/样式/页脚/标题/条形 | 逐字 8×2 通过；样式色 PAPER #fbfaf6 / INK #302c28 / OLIVE #46581f / CLOTH #37402f，无旧金/近黑色值；MUSTER 84 词（标签 84 一致）；页脚/页码行 8/8；头条 40 字符（≤56）；P6 条 748/561/391；星期已验（16.11 周一、13.11 周五、18.11 周三、20.11 周五、22.11 周日、27.11 周五、29.11 周日）；日期算术 18+11=29、15+7=22、16+6=22 | `gates/verify-repro3.log`、`gates/verify-repro.json` |
| 21 | text.md vs core | diff + token 检查 | 均 1185 行；39 组差异、235 行改动；core 非 CJK 行 952，仅 2 行缺于本版（slug 头行；刊头副标——已知 freeze 缺失项）；德语 token 检查仅标记 2 处（刊头副标、NOCH EIN WORT 释义行——解释层，预期） | `gates/textmd-core-diff.txt`、`gates/textmd-core-diff-summary.log` |
| 22 | 字体嵌入 | `pdffonts` 两版 PDF | 印刷版：Newsreader16pt-Regular/Italic、NotoSansCJKsc、NotoSerifCJKsc、UnifrakturMaguntia 全部 embedded+subset；网页版：LucernaNewsreader-Bold 与 LucernaNewsreader-Italic 均已嵌入（proof1 T1 已解决，rebuild 6 仍在） | 本轮命令输出 |
| 23 | 渲染提取 | 印刷版 8 页 100 dpi + 网页版 P1/P8 + 200/400 dpi 裁切 | 全部生成并目视（见 PROOF-NOTE）；P3 盒标题裁切坐标错位（取到词表体而非标题），未作证据——全页目视已覆盖 7 标题 | `render/`、`gates/render-extract.log` |

## 结论

**（a）零问题，可定稿。**proof2 的 D1/D2 已由 fix2 治愈（0.18pt / 0.72pt，实测与宣称逐项一致）；其余全部通过，无新发现缺陷。
