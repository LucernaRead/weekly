# GATE-LOG — 2026-W47 pt-ko 独立复校 re-proof（fix1 重建版）机械门实跑证据

- 复校：re-proof，2026-11-11；工具：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3）。
- 原则：只信自己跑的结果。全部命令在本人 scratch（`.../scratch-reproof-pt-ko1/`，TMPDIR 指到其下 `tmp/`）内执行；生产目录零写入（交付件 mtime 仍为 16:19–16:26 UTC，源文件 16:18:57，KIT 16:31:40，均早于本次开工 16:35 UTC；git diff 为空）。
- 说明：fix1 的脚本/日志仅作路径参考，全部结论均为本轮独立重跑所得；pt 系无 registry.json（en 系才有），不判缺文件；pt 系无现成 check_s11.py/verify_ed.py，本轮用 fix1 的 pt-ko 改编版（自家 scratch 内副本，en 原版未动）。

## §0 身份核对与三 SHA

- 印 PDF `A-Lucerna-VOL4.pdf`：SHA `cdff9fe46e350a0d2889fcc99e51dfb36547eb158eb4aabfda021a2ad6f069a4`，17,184,511 字节 ✔（与任务一致）
- 网 PDF `A-Lucerna-VOL4-web.pdf`：SHA `3046541c903ea95e4f74aa7124c790a290448bd01fc4d30f04a1c9a42e64c3ad`，1,431,219 字节 ✔（与任务一致）
- text.md `2026-w47-pt-ko.text.md`：SHA `3eb35dfb9070565c1b168d3e79b8319c4867434b53e0819e8f77cd8ca467cb4c`，37,804 字节，534 行 ✔（与任务一致）
- 探针：`git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9…`；`/dev/null` 存在；scratch 写探针 OK。
- **重建可复现性（proof1 O1 已闭合）**：本轮 scratch `run.py` 重建 SVG 与交付 SVG 8/8 字节一致（见 §1），freeze 核心对照 8/8（见 §5），render 重渲印 PDF SHA 与交付件一致（见 §14）。当前 venv 栈下无字体度量漂移。

## §1 run.py —— rc=0，TOTAL 150，0 溢出，重建 SVG 8/8 一致（`logs/run.log`）

- scratch 构建副本 `build/2026-w47-pt-ko` 内运行。rc=0。`TOTAL 150`；by level `{'A2': 48, 'B1': 71, 'B2': 31}`；by page `{1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；model words 88。
- `grep -c OVERFLOW` = 0。
- 重建 SVG 与生产 SVG 逐字节一致 8/8（sha256 前 16 位：p1 `c18f1017bc40dc70`、p2 `9e2484f6edd1ecc4`、p3 `fe431a453a4af44b`、p4 `6de55aebaca75651`、p5 `0ac8aaad1b06e0b4`、p6 `483a16616741f467`、p7 `aa577faf340ef9e1`、p8 `cf1097c6bb46d03e`，两边相同）。

## §2 gates.py —— 16/16，rc=0（`logs/gates.log`）

- scratch 构建副本内运行。16 行 `[PASS]`，`FAILURES: none`，rc=0。关键项：P7 末引基线 2292.17（距预告盒顶 2404 约 107px）；P1  headline 41 字符 ≤56；P8 答案流止于 y=2458。

## §3 occlusion_audit.py —— 真实审计 0 flags，rc=0（`logs/occlusion.log`）

- 对 scratch 构建副本 `svg/` 目录实跑，**未传 `--selftest`**。输出首行 `selftest OK: planted classes fired {...}` 为工具每次运行的固有自检输出；实跑行：`…/svg: 0 flags`，rc=0。

## §4 p8 extract / compare —— 150/150，CLEAN，keydiff [137, 138]（`logs/p8-extract.log` / `logs/p8-compare.log` / `p8-extract.json` / `p8-compare.json`）

- extract：`noted set = 150 of 150 (parse: lines)`，rc=0。
- compare（core-pt P8 vs 本版 P8）：`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`，rc=0。**直接读了 `p8-compare.json` 本体**：`"status": "CLEAN"`，`"missing": []`，`"extra": []`，`"uncertain": []`，`"keydiff": [137, 138]`——无 "?" extra 误读。137/138 为韩语译文，逐字核对均正确（Q137 `11월 20일 금요일은 전국 공휴일이에요.`；Q138 `파우메이라스는 승부차기에서 5–4로 이겼어요.`）。

## §5 freeze baseline —— 核心对照 8/8 + 版内自比对 8/8，rc=0（`logs/freeze-core.log` / `logs/freeze-ed.log`）

- 核心对照（任务书标准口径）：`freeze.py baseline --build <core-pt> --core-svg <core-pt>/svg` → `logs/freeze-core.log`：`baseline: 8/8 SVGs byte-identical`，rc=0；`core integrity: shipped core SVGs unchanged by the run`（8 文件重哈希）。
- 版内自洽基线（补充）：`--build <scratch 构建副本> --core-svg <副本 svg>` → `logs/freeze-ed.log`：`baseline: 8/8 SVGs byte-identical`，rc=0。**注**：本轮该口径用的是版内自比对作补充；核心对照证据以前一款为准，两者均为 8/8。
- core-pt 只读：全程无写入；verify_ed 三重核验亦 PASS（见 §18）。

## §6 freeze diff（核心对照）—— rc=0，TOTAL added CJK 3,397（`logs/freeze-diff.log` / `freeze-diff.json`）

- 每页增减：p1 +49/-29、p2 +35/-33、p3 +29/-29、p4 +28/-26、p5 +85/-40、p6 +21/-21、p7 +48/-46、p8 +923/-481。
- TOTAL added CJK characters: **3,397**（与 fix1 数字一致；相对重建前 3,403 的 −6 = F1 −2、F2 −3、F3b −1；均为韩语解释层 + 每页 1 个 U+3000，目标语文本无新增）。

## §7 creambox / creambox_diag（PIL 真墨）—— 真墨 0 溢出（`logs/creambox.log` / `logs/creambox-diag.log`）

- creambox.py（naive 扫描）：rc=0；6 处负 clearance（与 fix1 相同 6 处：P1 y=786 −37.0、P1 y=1874 −38.0、P2 y=1618 −32.0、P3 y=200 −37.0、P6 y=1594 −42.0 ×2）。
- creambox_diag.py（真墨裁决）：rc=0；**0 处负 ink-clearance**；6 处负值全部是框外行（owner-rect=NONE：下一节标题/页注）；各框 OWN 末行真墨余量最小 **+2.4px**（P2 E-VOCÊ 盒）。**真墨 0 溢出。**
- D2/D3/D4 OWN 行实测：P1 快讯盒底 2348.0，`em Brasília. (Página 4)` 墨底 2332.6，余 **+15.4**；P3 周历盒底 551.0，`16h30.` 墨底 540.9，余 **+10.1**；P6 时间线盒底 854.0，`Página do Participante.` 墨底 846.0，余 **+8.0**。

## §8 boxtitle（PIL advance 宽度）—— 31 框全清（`logs/boxtitle.log`）

- rc=0。31 个框标题全部 `clear=+`，最小 clearance **+18.2px**（P3 gloss 标题），其次 +22.2、+26.3。无负值，无 OVERFLOW。
- P1 数字框标题：`A SEMANA EM NÚMEROS　숫자`，title_w=340.3，right=1347.3，clear=+64.2。

## §9 ink_measure（PIL 真墨，全版逐盒）—— 标题 31/31 清，页缘 0，盒顶 0（`logs/ink-measure.log` / `ink-measure.json`；core 对照 `logs/ink-measure-core.log` / `ink-measure-core.json`）

- 本版：8 页，31 盒；框标题真墨右缘距盒右缘全部为负（即在盒内），最小 **−18.2px**（P3 gloss），P1 数字框标题 **−64.2px**（D1 已修）；页缘违规 0；盒顶溢出 0。
- “ink-bottom spills” 6 处均为基线在盒底之下 37–44px 的框外行（下一节标题/页注），core-pt 同法复测**基线相同、墨底相差 ≤0.8px**（P1 `AGORA VOCÊ…` 1205.7 同值；P1 quiz 注 2388.0 vs core 2388.5；P2 `Atenção…` 1805.2 同值；P3 `UM DIA, DOIS SENTIDOS` 417.6 同值；P6 `EXERCÍCIOS…` 1960.2 vs core 1961.0；P6 quiz 注 1960.0 vs core 1960.5——差异来自中韩 gloss 字形）。
- “right spills” 1 处：P2 `Atenção: o feriado é nacional, mas cada cidade tem as suas regras para…` over_box +1172.8——该行为横跨整页宽的页注（墨右缘 1683.3 < 页宽 1950），误关联进 SEX 20 格的 +45px 窗口；creambox_diag 判其 owner-rect=NONE；core-pt 同值。非缺陷。
- D2/D3/D4 的 core-pt 对照值与本版相同（盒已加高后数值一致），确认修在核心层且本版继承。

## §10 sweep（桥孤儿 / 框-线 / 桥寡行）—— 0 / 0 / 0（`logs/sweep.log`）

- `sweep_de.py` 对 scratch 构建副本运行，rc=0。box-vs-hline flags: 0；bridges found: 20；bridge orphans: 0；**bridge widows: 0**。

## §11 keycheck —— 149/150（唯一不符 Q150，预期），rc=0（`logs/keycheck.log` / `keycheck-150.json`）

- 方法：fix1 的 `keycheck-mine.py` 副本（输出写本人 scratch 的 `keycheck-150.json`），对 scratch 构建副本运行（该工具会在目标目录内重跑 run.py，故只在副本跑）。
- `REG entries: 150; p8extract keys: 150`；`exact match: 149/150`；rc=0。
- 唯一 MISMATCH：`n=150 page=8 type=작문: key='（자유 과제 — 모범 글은 아래에 있어요）' extracted='✓'`（预期）。

## §12 150 题三源交叉（`logs/xcheck150.log` / `keys-table.txt`）

- 本轮自写 `xcheck150.py`：REG 键 × text.md 行内答案（解析 108 项）× text.md Respostas 汇总（解析 **150/150**）× P8 印出版面键（150/150）。
- 不一致 **0 项**（Q150 除外，见 §11——写作题，REG 键为任务说明，P8/Respostas 为 `✓` + 模范文提示）。
- 行内未解析的 42 题均为填空/组句/翻译等非 "(X)" 格式题，均由 Respostas 150/150 与 P8 150/150 覆盖。

## §13 印/网文字层 —— 逐字节一致（105,211 B）（`logs/print.txt` / `logs/webtest.txt` / `logs/web-prod.txt`）

- 生产印 PDF vs 生产网 PDF：`pdftotext -layout` 各 105,211 字节，`cmp` 无输出，**PRINT/WEB TEXT BYTE-IDENTICAL**。
- scratch 重渲网 PDF（见 §15）文字层与生产印 PDF 同样逐字节一致（105,211 B）。
- 斜体 span：生产印 1 = 生产网 1（P1 `« consciência »`，Newsreader-Italic 16.12pt；网 PDF 为 LucernaNewsreader-Italic 同位）。

## §14 render.py —— rc=0，印 PDF SHA 与交付件一致（`logs/render.log`）

- scratch 构建副本内运行，rc=0。重渲印 PDF 17,184,511 B，SHA `cdff9fe46e350a0d2889fcc99e51dfb36547eb158eb4aabfda021a2ad6f069a4`，与生产印 PDF 一致。
- 卡片：`build/2026-w47-pt-ko/cards/*.png`（1950×2700，8 页）为目视依据；因 SHA 一致，scratch 卡片即交付件卡片。

## §15 webpdf.py —— rc=0，scratch 重渲只在 scratch（`logs/webpdf.log` / `webtest/`）

- `webpdf.py <scratch 构建副本 svg> webtest/A-Lucerna-VOL4-web.pdf`，rc=0：`WROTE …/webtest/A-Lucerna-VOL4-web.pdf: 1431219 bytes, 47423 text bytes`。
- scratch 网 PDF 与生产网 PDF **同为 1,431,219 B**，文字层逐字节一致（见 §13）；SHA 不同（scratch `b0b40d96…` vs 生产 `3046541c…`）——fontTools 嵌时间戳所致已知逐次浮动，非缺陷。**绝未覆盖生产网 PDF。**

## §16 textmd.py —— rc=0，534 行，重生成文件与交付件逐字节一致（`logs/textmd.log` / `ko-textmd-diff.json`）

- 本轮用自家 scratch 副本 `textmd-mine.py`（原工具会把 diff json 写进机制目录，副本改写进本人 scratch），在 `textmd-copy/`（构建副本的复件）上运行，PYTHONPATH 指复件目录。rc=0。
- 重生成 text.md SHA `3eb35dfb9070565c1b168d3e79b8319c4867434b53e0819e8f77cd8ca467cb4c`，与生产 text.md **逐字节一致**；`wc -l` = 534，`splitlines` = 534，以换行结尾；`question numbers present: 150 missing: []`；remaining CJK chars: 0。
- 注：工具自报 "(535 lines)" 是 `split('\n')` 对末尾换行多计 1 的口径；实际 534 行。此即旧 "535 行" 误记的来源。
- text.md diff 相对修前（SHA `fe14281f…`，`scratch-refanout-pt/freeze-pt-ko/build-copy/` 的副本）：**恰 3 行**——L38（F2）、L280（F3b）、L393（F1）；F4 在 text.md 中无出现处。

## §17 孤儿标点 / 行首冒号 / 逗号缺空格 全版重扫 —— 0 处（`logs/scan.log` / `logs/scan-punct.log`）

- `scan_lines2.py`（逐栏重建，跨栏同 y 不混淆）对生产 SVG 运行：**ISSUES: 0**。P7B2 y=594.9 `quando、se、quem 뒤엔 접속법 미래가 와요:` / y=624.7 `sair、for、tiver（공식 정답 기다리는 문법）.`。
- 同工具对 core-pt 运行：**ISSUES: 1**——ORPHAN p5-jovens.svg y=718.7 `）`（核心 P5 孤儿，本版无，核心未动，观察项）。
- 本轮自写 `scan_punct.py`（冒号粘连 / 全角逗号 / 全角句号 / `数字+일:` / `일까지`）：3 处旗标，逐项裁决均为非缺陷——P7 `22일 일요일까지예요`（延至 22 日周日，正确日期用法）；P8 Q85 `주말에 공휴일까지 5일`（对 core `周末加假日 5 天`，语义正确）；P8 Q59 `2일 < 7일: menos`（对 core `2 天 < 7 天：menos`，冒号后有空格）。真·冒号粘连 0 处，全角 `，` 0 处，`16일:30` / `18일까지:30` 0 处；时刻 `HH:MM` 5 处正常，冒号+空格 162 处。
- text.md 标点：全角 `，` 0 处，全角 `。` 0 处，U+3001 `、` 4 处（著者列举写法），冒号粘连 0 处。

## §18 F1–F4 独立重测（wrap 重算 + 渲染真墨，`probe_wrap.py`）

- F1 wrap（sans 20.5 / 422.5）：2 行——407.8（余 14.7）/ 398.3（余 24.2）；渲染真墨 y=594.9 宽 408.0、y=624.7 宽 398.2。`:` 落行 1 末，`.` 落行 2 末。
- F2 wrap（serif 20 / 386.5）：2 行——340.0 / 331.7（余 54.8）；渲染真墨 y=936.2 墨 1007.0–1347.0、y=963.2 行末 `）` 墨止于 1338.8（盒右缘 1411.5）。`）` 落行末。
- F3b wrap（serif 21 / 386.5）：3 行——350.1 / 370.8（余 15.7，行末 `:`）/ 149.7；渲染行 2 末 `:` 元素 x=921.6（盒右缘 961），行 3 `TRI 가 정해요）` y=664.2。
- F4：全版 `,(\S)` 0 处；P8 y=2313.1 行 `, TRI ` 有空格（见 §17）。
- `content12.py:266` 仍为 `e.ex("A2", "문장을 완성하기", "1695", "줌비는 1695년에 돌아가셨어요",`——答案原文未动；`content56.py:74` 仍为 Q68 键 `맞힌 개수가 점수가 아니에요, TRI 성적을 정해요`。

## §19 minfont（印 PDF P8）—— 最小 10.125pt，0 项低于 9.75pt（`logs/minfont.log`）

- rc=0。`P8 min effective font size = 10.125 pt (n=805)`；`below 9.75pt: 0`；distinct sizes 10.125–34.5。

## §20 check_final（词 multiset + P8 字号）—— diff 0，7049/7049，rc=0（`logs/check-final.log`）

- 生产印/网 PDF：`pages print=8 web=8`；`words print=7049 web=7049 multiset-diff=0`；`diff sample: []`；P8 answer-region span sizes `[10.125, 10.5, 14.625, 18.75]`，count 610，min 10.125；`word bbox height: min 10.125 median 10.125 max 27.15`。

## §21 check_s11（pt-ko 改编版）—— rc=0，ALL PASS（`logs/check-s11.log`）

- `check_s11_ptko.py`（本人 scratch 副本；现存 check_s11.py 均为 en 家族专用，无 pt-ko 版）：colour set core 21 = edition 21，extra/missing 均为 none；P8 min font-size 13.5（该脚本正则口径；门禁以 minfont.py 的 10.125pt 为准）；P8 `AVALIAÇÃO E RESPOSTAS` / `113.` / `120.` / `145.` / `작문` 均 present；P8 Q68 行（`, TRI `）与 Q65 整句行均 present。

## §22 verify_ed（pt-ko 专用版）—— rc=0，18/18 PASS（`logs/verify-ed.log`）

- `verify_ed_ptko.py`（本人 scratch 副本；en 版 verify_ed.py 为 Ashes 内容专用，不适用 pt-ko）：Q68 键 B、Q65 键 B、P8 Q68/Q65 整句行、Q137/Q138 键、4 处源文行、content12:266 答案未动、text.md 534 行 + L38/L280/L393 + 无 `,TRI`、core-pt 三重未动核验（无文件新于开工、git diff 为空、freeze-core 完整性行）全部 PASS。

## §23 目视（8 页全页 + 4 处特写）

- 依据：scratch 重建卡片（印 PDF SHA 与生产件一致，故卡片即交付件卡片）及 `render/crop-*.png`（2× 特写）。
- P1：干净；数字框标题 `숫자` 在盒内；1695 项 2 行，`）` 落行末（特写 `crop-p1-numbers1695.png`）；快讯盒末行在盒内，quiz 行为盒下独立栏目标题。
- P2：干净；SÁB 21 格 `토요일 16:30, 파우메이라스 대 플라멩구`（2 行，在格内）；`Atenção…` 全宽页注干净。
- P3：干净；周历盒末行 `16h30.` 在盒内；Zumbi 画像 + 说明干净。
- P4：干净；决赛表与练习区无溢出。
- P5：干净；计划框第 4 项 3 行，`:` 落行 2 末（特写 `crop-p5-note.png`）。
- P6：干净；时间线盒末行 `Página do Participante.` 在盒内；条形图 10 天 / 5 天与正文一致。
- P7：干净；B2 桥 2 行，`:` 落行 1 末、`.` 落行 2 末（特写 `crop-p7-b2bridge.png`）；引言与读者来信未动。
- P8：干净；Q65 行 `13:30–18:30`、Q68 行 `, TRI ` 有空格（特写 `crop-p8-q68.png`）；答案区其余未动；模范文 + 体育场图干净。

## §24 手验事实核对

- 日期/星期（`date -d`，America/Toronto）：11-07 六、11-08 日、11-14 六、11-15 日、11-16 一、11-17 二、11-18 三、11-19 四、11-20 五、11-21 六、11-22 日、11-23 一、11-27 五、12-06 日，全部与正文吻合。
- Enem 算术复算：16–30 日共 15 天；工作日 10 天（16,17,18,19,23,24,25,26,27,30）；周末/假日 5 天（20,21,22,28,29）。
- 模范文实测 88 词；半决赛比分算术（Grêmio 总 3–1；Palmeiras 总 2–2、点球 5–4）与正文一致。

## §25 KIT §9 更正核对（D6 24 处 / text.md 534 行）

- D6 实为 24 处：KIT L150 已写 "(24 instances"、FANOUT-REPORT-pt.md L135 已写 "D6 colons (24 spots"；全文 grep 无 "(22 instances" / "(22 spots" / "22 处" 残留。
- text.md 实为 534 行：KIT L127 已写 "37,823 bytes, 534 lines (the '535' originally written here was a miscount; proof1 §5c)"；本轮 `wc -l` = `splitlines` = 534。

## §26 D5 字体问题（只记录，不判）

- proof1 O1（字体度量漂移）：本轮在当前 venv 栈下，scratch `run.py` 重建 SVG 8/8 与交付件一致、freeze 核心对照 8/8、版内自比对 8/8、render 重渲印 PDF SHA 与交付件一致。本轮未观察到字体度量漂移。按任务书要求只记录，不作缺陷判定。
