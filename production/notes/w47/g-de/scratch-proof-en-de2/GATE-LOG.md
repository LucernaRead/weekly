# GATE-LOG — 2026-W47 en-de 第二轮独立复校（delta 后，proof2）机械门记录

- 版：`2026-w47-en-de`；解释器：`~/workspace/weekly-git/tools/venv/bin/python`（未用系统 python3；freeze 日志所印 Pillow 13.0.0 / FreeType 2.14.3）
- 日期：2026-11-11；命令均在 `~/workspace/weekly-git` 仓根或本笔记目录下执行；输出存本目录 `gates/`，渲染图存 `render/`（p--1..p--8、w--1..w--8，pdftoppm 110 dpi 全新渲染），freeze 运行产物存 `freeze-core/`、`freeze-ed/`
- 对照基准：proof1（`scratch-proof-en-de1/`，结论 (a) PROVISIONAL，待 delta 后复校）与 delta（`scratch-delta-en-de/DELTA-NOTE.md`）；本次全部门在 delta 重建后的新成品上独立重跑（只读，不改源码/成品；开工探针 `git hash-object -w` 除外无任何 git 写操作）
- 本目录 `pre-delta/` 为今晨旧一轮 proof2 原样归档，与本轮无关

## 0. 开工探针（双通）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- 在 `hidden_files/w47/scratch-proof-en-de2/` 真实写小文件成功（probe.txt，完工后已删）；`TMPDIR` 全程指向本目录 `tmp/`；`df -h`：`/home/hatch` 可用 61G，无配额问题；`/dev/null` 为字符设备；全程未遇 EDQUOT。
- 读到 `~/workspace/weekly-git/AGENTS.md`（runtime 提示后补读）：仅复校、不改生产文件、不 commit——与任务一致。

## 1. 身份核对（送审成品；复校结束时复核，SHA 未变）

- `sha256sum` + `stat`（开工与完工各一次，两次一致）：
  - `The-Lucerna-VOL4-en-de.pdf`：29,331,209 字节，`ae3b2e371d0dc8344853c106a697d958496dffb0170d3f6cb8599618209f1751`
  - `The-Lucerna-VOL4-en-de.web.pdf`：2,414,471 字节，`7117abe47962468fbf93068665f10da4cafaa2116ad368a907971bc9a94fa655`
  - `2026-w47-en-de.text.md`：52,565 字节，`c16f0e473f8017605fe8822a6d711134ad55b1708a0f22346ef2b4dd1f01d589`
- `pdfinfo`：两 PDF 均为 8 页、1462.5 × 2025 pt；网页版 < 7 MB。
- 生产文件 mtime 复核：SVG 15:13:21–15:14:12、text.md/registry 15:12、print PDF 15:20:13、web PDF 15:23:40——复校前后未变；`git status` 仅 `?? production/2026-w47/2026-w47-en-de/` 与 `?? production/2026-w47/core-en/`（未跟踪目录），无修改。

## 2. Delta 范围核实（独立重核，与 delta 声称逐项相符）

- registry diff（delta `pre/registry.json` vs 现状）：恰 1 行——第 583 行 `"key": "speak"` → `"key": "up"`（`diff` rc=1 仅因此行）。
- text.md diff（delta `pre/2026-w47-en-de.text.md` vs 现状）：恰 1 行——第 1151 行 `73. [A2] Satzergänzung — speak (speak up = laut sagen)` → `… — up (…)`；52,568 → 52,565 B。
- SVG SHA（delta `pre/svg-sha-pre.txt` vs 现状）：仅 `p8-test.svg` 变化（`6b69156023d24b46c193baf697c05719b5319628fca14d65e2b810aa892de5a1` → `b04d052dd7d4b0eb35702e9766f681e2d6d318642d7da773aa18b14559d6f623`）；p1–p7 字节一致，P5 未变（正确预期，见 PROOF-NOTE）。
- Q73 四源：content56.py:49 键 `up`（core-en 同为 `up`）；registry Q73 键 `up`；text.md L589 题干 `Speak ___: tell a teacher.`、L1151 答案 `73. [A2] Satzergänzung — up (speak up = laut sagen)`；`svg/p8-test.svg` 含 `73. up`（grep 1 命中）、`73. speak` 0 命中；印刷 P8 提取文本含 `73. up`；`svg/p5-youth.svg` 含题干 `Speak ___: tell a teacher.` 与注释 `to speak up = laut sagen`。旧键 `73. speak` 在 registry、content56.py、text.md、8 个 SVG 中 0 命中。

## 3. occlusion_audit.py（真实审计，未用 --selftest）

- 命令：`tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-en-de/svg`
- 结果：`selftest OK: planted classes fired {'BOXTITLE': 1, 'COVER': 1, 'EDGE': 1, 'FOOTER': 1, 'LINEX': 1, 'TEXTX': 1}; clean controls silent`；`production/2026-w47/2026-w47-en-de/svg: 0 flags`。**PASS**（`gates/occlusion.log`）

## 4. p8.py extract + compare

- 命令：`tools/p8.py extract --p8 <edition>/svg/p8-test.svg --total 150 --json gates/p8-extract.json`；core 同命令 → `gates/p8-extract-core.json`
- 结果：两版 noted set 均为 60/150，同一集合 `[3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82, 83, 84, 85, 86, 87, 89, 108–150]`（parse: joined）。**PASS**
- 命令：`tools/p8.py compare --core-p8 <core>/svg/p8-test.svg --edition-p8 <edition>/svg/p8-test.svg --total 150 --json gates/p8-compare.json`
- 结果：`status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138, 139, 140, 150]`。与任务预期恰相符（读者语答案键）。**PASS**

## 5. keycheck（registry vs P8 extract / vs core）

- 命令：`tools/venv/bin/python gates/keycheck_ed.py de`（本目录副本；仅把 p8-extract.json 读路径由 delta scratch 改指本目录 `gates/`，核查逻辑未改）
- 结果（`gates/keycheck.log`）：
  - `registry-vs-p8extract exact 149/150 exc=[150] mismatch=[]`
  - `registry-keys-vs-core: 145/150 match; diff=[(137, …), (138, …), (139, …), (140, …), (150, …)]`（德语翻译键 + Q150 短标签）
  - `Q38-41: ['b', 'a', 'd', 'c']`；`Q125=A; Q46=A; Q52=hosted; Q55=won; Q82/83/84=B/C/A`；`extract keys count: 150 missing vs registry: none`。**PASS**（与任务预期 149/150、145/150 恰相符）

## 6. freeze

### 6a. 标准口径 baseline（--build = core-en 构建目录，--core-svg = core-en svg 目录）

- 命令：`tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/core-en --core-svg production/2026-w47/core-en/svg --out <scratch>/freeze-core`
- 结果：rc=0；`baseline: 8/8 SVGs byte-identical`——p1 `a9a8deaf76e61cb2`、p2 `979747160de01d67`、p3 `efb83ce76688554b`、p4 `aa6f395e4932ef8b`、p5 `a6a515cd5f734d0d`、p6 `7692256484f26289`、p7 `da908af644651793`、p8 `1066c475da8afe7e`（p8 为 fix2 后值，proof1 登记的修前 `2f9a0334…` 已被 fix2 改变，预期内）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。**PASS**（`gates/freeze-baseline-core.log`；产物 `freeze-core/`）
- 补充核对：core-en 8 个 SVG SHA 与 proof1 登记逐个一致（除 fix2 所改 p8）；core-en 即 en-zh-cn 核心版（目录内成品名为 en-zh-cn，无独立 `2026-w47-en-zh-cn` 版目录），其 `render.py` 输出 `The-Lucerna-VOL4-en-zh-cn.pdf`——与任务所指核心对照一致。

### 6b. edition-internal 自洽基线（补充证据，不冒充 6a）

- 命令：`tools/venv/bin/python tools/freeze.py baseline --build production/2026-w47/2026-w47-en-de --core-svg production/2026-w47/2026-w47-en-de/svg --out <scratch>/freeze-ed`
- 结果：rc=0；`baseline: 8/8 SVGs byte-identical`——p1 `b2be6b6ec3976a8d`、p2 `66f3fd31b48b34a5`、p3 `3679e16b396bd69c`、p4 `8fb26bf7c3cf75cf`、p5 `25045251378009ab`（与修前一致）、p6 `074ed84857a0acf2`、p7 `a78d6cb197fd87e2`、p8 `b04d052dd7d4b0eb`（新 p8）；`core integrity: shipped core SVGs unchanged by the run`。**PASS**（`gates/freeze-baseline-ed.log`；产物 `freeze-ed/`）
- 注意：6b 的 `--core-svg` 参数实为本版自己的 svg 目录（freeze.py 的参数名使然），其 8/8 只证明"本版源码重建与送审 SVG 自洽"；6a 才是任务要求的标准口径（core-en 对 core-en）。两者均已跑，无冒充。

### 6c. freeze.py diff（core-en svg vs edition svg，只读）

- 命令：`tools/venv/bin/python tools/freeze.py diff --core-svg production/2026-w47/core-en/svg --edition-svg production/2026-w47/2026-w47-en-de/svg --json gates/freeze-diff.json`
- 结果：P1 +32/−34、P2 +42/−54、P3 +25/−23、P4 +24/−22、P5 +24/−22、P6 +25/−21、P7 +64/−55、P8 +99/−99；TOTAL 新增 CJK 9 个，全部 U+3000（每页各 1 个，P1 为 2 个）。与 proof1/delta 逐页一致。**PASS**

## 7. creambox + 盒标题 + 真墨（gate 6 余部）

### 7a. canonical creambox.py

- 命令：`tools/venv/bin/python ~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/tools/creambox.py production/2026-w47/2026-w47-en-de/svg/*.svg`
- 结果（`gates/creambox-all.log`）：32 盒全部 inside-only clearance 为正；最紧 P2 AND YOU? +5.0（desc-clear −1.0，见 7c 裁定）；次紧 P1 SEARCHES +12.0（desc +6.3）、P2 DID YOU KNOW +14.3；P7-TOOLBOX：7 盒，min inside clearance +47.7，min desc-clear +41.6。
- Spill sweep（BELOW-WINDOW 行，盒底外 +45px 窗口）：共 23 行，偏移全部 +24.0…+37.0——均为下一下一级标题/正文首行（false positive 区间，见 creambox README）；**+12…+18px 整行溢出区间 0 行**。无整行溢出。**PASS**

### 7b. sweep_boxes.py（源标题 + SVG 标题 + PIL 真墨盒底）

- 命令：`tools/venv/bin/python gates/sweep_boxes.py`（卡片 PNG 为 delta 重建后 `cards/`，15:15–15:17，晚于 SVG 重建 15:13–15:14；只读）
- 结果（`gates/sweep-boxes.log`）：源扫 12/12 fit（最紧 ODD SOCKS +15.2）；SVG 扫 21/21 fit（最紧 P2 `The new Congress meets in January.` +8.8，加粗首行）；32 盒盒底下方 0 暗像素溢出（逐页 0）；最紧盒内基线 clearance +5.0（P2 `Englisch an die Redaktion.` y=1539.85）；`FAILS: none`，rc=0。**PASS**
- `boxtitle.py` 未跑：其 TITLES 硬编码为 de 目标语版的 7 个德语盒标题、CORE 指 core-de，不适用于 en-de；sweep_boxes.py 的 (a)(b) 两节已覆盖本版盒标题源扫 + SVG 扫。

### 7c. ink_check2.py（PIL 真墨重测，最紧两处）

- 命令：`tools/venv/bin/python gates/ink_check2.py`（本目录副本；仅把裁图写出路径改指本目录 `render/`）
- 结果（`gates/ink_check2.log`）：P2 AND YOU? 深色真墨（lum<120）最低行 y=1543（x=1488–1493，`Englisch` 的 `g` 降部）；米色实测底缘在 y=1544（占比 0.98）与 y=1545（0.00）之间——深色墨距像素底缘 +1 px，抗锯齿尾（|lum 差|>25）最低行 y=1544、触及最后一行米色未出盒。**启发式 −1.0px 为假警报，通过**；裁图 `render/crop-p2-andyou.png` 目视确认。P3 HAYMITCH 标题：最右真墨 x=1772，盒右缘 1862，clearance +90.0 px；带顶真墨 y=875，盒顶 856，+19.0 px；裁图 `render/crop-p3-haymitch.png`。rc=0。**PASS**

## 8. print/web 文本层比对（web PDF 未重渲染，只在 scratch 里比对）

- 命令：`tools/venv/bin/python gates/printweb.py`（逐页 pdftotext）
- 结果（`gates/printweb.log`）：print chars 47,403 = web chars 47,403；token 多重集差 0/0；逐页 byte-identical 8/8（4855 / 5881 / 5395 / 5841 / 4764 / 5674 / 6320 / 9908 B）；`print==web full: True`。**PASS**
- 注：47,403 与 delta 注记一致（KIT 原登记 47,416 为 HAYMITCH 标题修复前数字，47,416 − 10 − 3 = 47,403，账对得上）；与 proof1 的 47,406 差 3——恰为 Q73 键 `speak`→`up` 少的 3 字符。

## 9. check_s11.py de

- 命令：`tools/venv/bin/python gates/check_s11.py de`
- 结果（`gates/check_s11.log`）：`colour set: core 19 edition 19 extra: none missing: none`；徽章色 A2 #5c6e30 / B1 #46581f / B2 #37402f 全在；`P8 min font-size: 13.5`；P8 Q113–120 选项行 [A2]、Q120 [A2] chip、`Levels: 145-149 [A2]`、WRITING 头 `H　WRITING　Schreiben [B1]` 均在；`ALL §1.1/P8 CHECKS PASS`，rc=0。**PASS**

## 10. verify_ed.py de

- 命令：`tools/venv/bin/python gates/verify_ed.py de`
- 结果（`gates/verify.log`）：Q39=a、Q40=d（含 note `mentor = Mentor a` / `arena = Arena d`、无 estadio/stadio）、Q46=A、Q52=hosted、Q55=won、Q125=A（含 4–1 注）、text.md 150 答案、Q39/Q40/Q125 text.md 一致、无 `Perth is winning` / `second week in Perth` / `Ashes begin`、有 `Arsenal are winning!` 与 Ashes 回顾表述；`P8 min PDF font >= 9.75pt — min 10.12pt`；`SVG: zero real CJK (only U+3000 allowed) — []`；`VERIFY ALL PASS`，rc=0。**PASS**

## 11. verify3.py（三源键 / 孤儿标点 / D1 / fix1 / 金句 / 禁词 / VOL / 徽章 / U+2019 / Q38–41）

- 命令：`tools/venv/bin/python gates/verify3.py`（本目录副本；仅把 WD 写出路径改指本目录）
- 结果（`gates/verify3.log` + `gates/verify3.json`），rc=0：
  - §1 三源键：text.md 答案 150 条；Q150 p8-extract `Offene Aufgabe` vs registry 长标签——短标签例外（预期）；mismatches: 0；分版 {1: 10, 2: 17, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 39}；分级 {A2: 62, B1: 66, B2: 22}
  - §2 孤儿标点：SVG 8 页各 0，TOTAL 0；印刷文本行独行标点 0
  - §3 D1 回归：8 条出处行全部 x=538.5，y=1432.76 / 1539.23 / 1679.07 / 1818.91 / 1958.75 / 2131.96 / 2305.17 / 2545.12；col3 流式首项 `THE DRILLS　Übungen` (989.0, 228.0)；col2 y 2400–2560 末两行 `Senate, and for governor in 36 states.”` (2490.75) → 出处行 (2545.12)；`D1 fixed: YES`
  - §4 fix1 两串：新串 text.md=True / svg=True；旧串 `(gewinnt immer wieder)` / `für Geschehenes` text.md=False / svg=False / print-text=False
  - §5 金句 8/8 逐字命中（P1×2、P2、P3、P4、P5、P6×2）
  - §6 禁词 0 命中；§7 VOL.4: 12 / VOL.5: 8 / VOL.3: 3 / `VOL. 4`: 1
  - §8 徽章：60×30 芯片 10/14/15/15/15/18/12/22，LV 填充矩形 16/15/16/16/16/19/13/23，均与 core 逐页一致
  - §9 U+2019 总数 0；CJK 字符 {U+3000: 141, 三: 1, 色: 1, 蛾: 1}（后三者为非可见 `<title>`）
  - §10 Q38–41 四方一致：38=b / 39=a / 40=d / 41=c（registry / text.md / p8 / 语义四方）

## 12. 150 键逐项手核（pair_stems.py 新跑 + 全文手读）

- 命令：`tools/venv/bin/python gates/pair_stems.py`（本目录副本 `make_textmd_delta.py`；仅把写出路径改指本目录；recording-stub 运行，事后核查 SVG mtime 未变：仍为 15:13:21–15:14:12，无生产写操作）
- 结果（`gates/fill-rewrite.log` + `gates/fill-rewrite.json`）：pairs 150，reg 150；`key mismatches vs registry.json: []`；fill/rewrite 50 项全部输出。50 题逐题手验 key 填入 stem 成句（详见 PROOF-NOTE §全量复校结果 3，含 Q73 `up` / `Speak ___: tell a teacher.`）；其余 100 题逐题对照题面/原文/图表手验（选择/匹配/翻译/对话/填空/阅读各题，映射见 PROOF-NOTE）。**PASS，150/150 适配**
- MODEL 字数：H 写作范文 82 词（不含独立破折号；按 `[A-Za-z0-9’']+` 计数），在 80–100 词任务范围内。
- 日期/星期：`date -d`（America/Toronto）核验 2026-11-03 周二、11-08 周日、11-09 周一、11-10 周二、11-16 周一、11-18 周三、11-19 周四、11-20 周五、11-21 周六、11-22 周日、11-26 周四、11-27 周五、12-01 周二，全部与正文一致；2025-11-21 周五亦一致。
- ABSTRACT.txt：699 字节，德文单行，ASCII 双引号 0 个。

## 13. D5 字体（只记录，不判定）

- 命令：8 个 SVG 的 `<text>` 元素按 font-family 计数（python3 + re）
- 结果：Newsreader 1022 / Noto Sans CJK SC 655 / Noto Serif CJK SC 27 / DejaVu Sans 4 / UnifrakturMaguntia 1；合计 1709。与 proof1/delta 数字完全一致。**仅记录**

## 14. 8 页逐页目视（印刷 + 网页，全新渲染）

- 渲染：`pdftoppm -png -r 110` 印刷版 → `render/p--1.png`～`p--8.png`；网页版 → `render/w--1.png`～`w--8.png`（16 张均在本轮全新渲染；web PDF 本身未重渲染、未覆盖生产文件）
- 印刷 P1–P8 逐页读完：无溢出、重叠、压页脚、截断、豆腐块、孤行；P5 Q73 题干 `Speak ___: tell a teacher.` 正常落版；P7 D1 修复状态目视确认；P8 答案区 `73. up` 正常落版。
- 网页 P1–P8 逐页读完：与印刷版逐页一致，无差异。**PASS**

## 门总汇

| 门 | 结果 |
|---|---|
| 身份（3 件 SHA/字节） | 与任务先验一致；复校结束时复核未变 |
| delta 范围 | registry 恰 1 行、text.md 恰 1 行、仅 p8 SVG 变化、P5 不变（正确预期） |
| occlusion_audit（真实审计） | 0 flags，selftest OK |
| p8 extract | core 与本版 noted set 均为 60/150，同一集合 |
| p8 compare | CLEAN，keydiff 仅 [137, 138, 139, 140, 150]（预期） |
| keycheck | registry-vs-P8 149/150（仅 [150] 除外）；vs core 145/150（仅上 5 项） |
| freeze baseline 标准口径（core-en） | 8/8 byte-identical |
| freeze baseline 版内自洽（补充） | 8/8 byte-identical（含新 p8 `b04d052d…`） |
| freeze diff vs core | P1 +32/−34 … P8 +99/−99；新增 CJK 9 个，全部 U+3000 |
| creambox 典范扫 | 32 盒，0 溢出；最紧 +5.0（P2 AND YOU?，真墨重测为假警报） |
| spill sweep（BELOW-WINDOW） | 23 行全部 +24…+37 标题区间；+12…+18 整行溢出区间 0 行 |
| sweep_boxes（标题+PIL 盒底） | 源 12/12、SVG 21/21 fit；盒底下方 0 暗像素；FAILS: none |
| ink_check2 真墨 | P2 AND YOU? 深色墨 +1 px 在盒内；P3 HAYMITCH +90.0/+19.0 px |
| print/web 文本层 | 逐页 byte-identical 8/8；token 多重集差 0/0 |
| check_s11.py de | ALL §1.1/P8 CHECKS PASS；P8 最小字号 13.5pt |
| verify_ed.py de | VERIFY ALL PASS；P8 最小 PDF 字号 10.12pt；SVG 零真实 CJK |
| verify3.py | 三源键 0 不一致；孤儿标点 0；D1 fixed；金句 8/8；禁词 0；VOL 12/8/3；徽章与 core 一致；U+2019 0 |
| 150 键手核 | 填空/改写 50/50 成句；其余 100 逐题验算全部正确 |
| 8 页目视（印刷+网页） | 16/16 读完，无版式缺陷 |
| D5 字体 | 仅记录：1022/655/27/4/1，合计 1709 |
