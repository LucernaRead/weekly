# GATE-LOG — 2026-W47 nl → fr（proof1）

复校员 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-fr1/`
除注明外，全部命令均在该 scratch 下以 `TMPDIR=<scratch>/tmp` 运行；源文件未改动、未重建、未 commit、未 push。

## §0 身份核对（与任务一致）

- 探针：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0；goals 侧 hidden_files 试写 `probe.txt` 成功。
- 印 PDF `De-Lucerna-VOL4-nl-fr.pdf`：SHA `e6db69e3cb07c8050bb95a9c29bab3862a1b57c24cc60a0b6c25a861b6ffb60a`，12,704,394 字节——与任务一致。
- 网 PDF `De-Lucerna-VOL4-nl-fr-web.pdf`：SHA `d26a0b571ddb268ce34bb363bd39cbb63e8c48d7108d63063e1b1ae626fbe5a0`，1,577,894 字节——与任务一致。
- text.md `2026-w47-nl-fr.text.md`：SHA `bc9c9f0056d9c1b5556f6bdadb19cf6cf08bd3c6d83db86933aca63e0b805972`，47,536 字节——与任务一致。
- 正典 creambox.py md5 `ee7a55d8b2057cf4ad42a97bb1197383`——与任务一致。
- 工具：`~/workspace/weekly-git/tools/venv/bin/python`。
- 附记：版目录在 git 中为 untracked（`git status --porcelain` 显示 `?? production/2026-w47/fanout-nl/2026-w47-nl-fr/`）；本复校未作任何 commit/push。

## §1 occlusion 审计

- 命令：`tools/venv/bin/python tools/occlusion_audit.py <edition>/svg`
- 结果：自检 `selftest OK: planted classes fired {BOXTITLE, COVER, EDGE, FOOTER, LINEX, TEXTX}; clean controls silent`；**0 flags**，rc=0（`occlusion.log`）。
- 保留意见：审计未检出 D1（P7 框标题溢出 21 px）——BOXTITLE 类对该标题漏检；D1 由 PIL + PDF 词位 + 像素扫描三法独立证实。工具跟进见 PROOF-NOTE O3。

## §2 正典 creambox.py 全版扫描

- 命令：`tools/venv/bin/python <goals>/hidden_files/w47/tools/creambox.py <edition>/svg/*.svg`（`creambox-all.log`）。
- 结果摘要（逐盒裁决）：
  - P1：numbers 盒末行余量 +49.0（desc-clear +43.0）；agenda 盒 +164.0；IN DEZE EDITIE 盒内部末行 +16.0（desc-clear +9.7），框下 +24 px 为 `HET WOORD VAN DE WEEK` 标题（次标题，非溢出）；IN HET KORT 盒 +58.0。
  - P2：ZO ONTHOUD 盒 +52.1；Note 盒 +51.7；WIST JE DAT 盒末行 `erbij.` 余量 +13.3（desc-clear +6.9，含降部 j）；EN JIJ 盒末行 `rédaction.` 余量 +6.2（desc-clear +0.2，无降部字母）；四词盒 SCHOEN/WORTEL/LIJSTJE/GEDICHT 内部末行余量分别为 +11.4/+36.1/+36.1/+11.4。
  - P3：Note 盒 +51.7；SINTERKLAAS IN CIJFERS 盒 +16.2。
  - P4：Note 盒 +51.7；HET PROGRAMMA 盒 +14.2。
  - P5：ZO KIJK 盒 +50.6；Note 盒 +51.7；JONGEREN IN CIJFERS 盒 +37.3；EN JIJ 盒末行 `envoie-les.` 余量 +6.3（desc-clear +0.3，无降部字母）。
  - P6：Note 盒 +51.7；图表盒末行 `chaussure ? (100 jeunes)` 余量 +8.7（desc-clear +3.2，含降部 j）；VOOR OF TEGEN 盒 +15.0。
  - P7 toolbox：3 盒，PAS OP +17.4、HET WOORD +13.1、BRIEVEN +28.5；**min inside clearance +13.1，min desc-clear +7.1**。
  - P8：无奶油盒。
- 降部真墨复核（PIL，见 §6）：最紧为 P6 图表末行 +3.7 px；其余 ≥ +6.2 px。全部为正，无漫出。

## §3 p8 compare（显式 --core-p8 / --edition-p8）

- 命令：`tools/p8.py compare --core-p8 production/2026-w47/core-nl/svg/p8-toets.svg --edition-p8 <edition>/svg/p8-toets.svg --total 150 --json p8-compare.json`（`p8-compare.log`）。
- 结果：core 150 noted / edition 150 noted；**status: CLEAN，missing=[]，extra_count=0，uncertain=[]；keydiff=[137, 138]**，rc=0。
- keydiff 裁决（合法重定向，非缺陷）：
  - #137：core `圣诞老人新闻每天 18:00 播出。` → 版 `Le journal de Sinterklaas passe chaque jour à 18 h 00.`——荷→法翻译题，译文正确（正文 P3）。
  - #138：core `前两名晋级四分之一决赛。` → 版 `Les deux premiers passent en quart de finale.`——荷→法翻译题，译文正确（正文 P4）。
- extract 双方各 150/150（`p8-extract-edition.json` / `p8-extract-core.json`）。

## §4 freeze

- `freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out <scratch>/freeze-baseline`：**8/8 SVG byte-identical**，rc=0；核心完整性复核通过（运行前后 8 文件重哈希无变）（`freeze-baseline.log`）。
- `freeze.py diff --core-svg core-nl/svg --edition-svg <edition>/svg --json freeze-diff.json`：rc=0；逐页增减 +27/+44/+30/+29/+41/+36/+47/+181，均为法语讲解层替换；**新增 CJK 每页 1 字，均为 U+3000（全角空格，双语标题分隔符），版内无任何汉字**（逐页清点：P1 18、P2 17、P3 13、P4 13、P5 14、P6 15、P7 13、P8 15 个 U+3000，别无他字）。
- 方法备注：`tools/freeze.py` 仅有 `baseline` / `diff` 两个子命令，**无 `freeze_direct` 子命令**（与任务注记一致），记为方法备注，不作缺陷。

## §5 keycheck 150/150

- 文件：`keycheck-150.json`（逐题：text.md 答案、P8 印键、与核心键比较、verdict、备注）。
- 方法：逐题手验——答案对正文事实、P8 印键（`p8.py extract`）、冻结核心键三方核对；范文计词；分级与页分布清点。
- 结果：**150/150 verified，0 mismatch**。text.md 答案与 P8 印键除 #150（开放写作题，P8 印 ✓ 号）外全部一致；配对题 25–28（d/c/a/b）、141–144（b/c/d/a）一致。
- 分级：A2 46 / B1 73 / B2 31（与 KIT 一致）；页分布 10/18/18/18/18/18/12/38（P1 1–10 … P8 113–150）。
- 范文：81 词（空白分隔口径；与核心范文同数同口径；题求 80–100 词，81 在内）。
- 备注项（非缺陷）：#63/#126“PSV 榜首 26 分”事实见于 P8 #126 题干本身，未见于 P4 正文，键与冻结核心一致，属核心层构造；#137/#138 见 §3。

## §6 boxtitle / 降部 / 横线：PIL 真墨 + PDF 词位 + 像素扫描三法

- PIL 字体：按 SVG 元素实际 `font-family` 取字（框题为 Noto Sans CJK SC Bold；正文 Newsreader；`~/.local/share/fonts/` 与 fontconfig 一致）；U+3000 用 CJK 字度量。
- 框标题墨右（PIL，余量 = 框右 − 墨右；页宽 1950）：
  - 全部通过，仅两项异常 → PROOF-NOTE D1/D2：P7 `HET WOORD　LE MOT DE LA SEMAINE` **−21.6 px**；P6 `VOOR OF TEGEN?　POUR OU CONTRE ?` **−0.8 px**。
  - 其余最紧：P1 numbers 标题 +5.0 px、P6 图表标题 +10.8 px、P7 PAS OP 标题 +15.5 px、P2 ZO ONTHOUD +24.7 px、P1 IN DEZE EDITIE +59.1 px。
- 像素扫描（印 PDF 216 dpi 渲染，`pixel-scan.log` / `pixel-scan2.log`）：与 PIL 一致——P7 标题墨右 1883.1（−21.1 px）；P6 标题 1862.7（−0.7 px）；P1 numbers 标题 956.0（+5.0 px）；P6 图表标题 1850.7（+11.3 px）；P2 ZO ONTHOUD 936.4（+24.6 px）。
- 页边：8 页印 PDF span 最大 x1 = 1413.5 pt（P7），页宽 1462.5 pt，余量 ≥ 48.99 pt——**无任何页右溢出**。
- 降部真墨（PIL，`pil-ink.log`）：P6 图表末行 `chaussure ? (100 jeunes)` +3.7 px；P2/P5 EN JIJ 末行 +6.2/+6.3 px（无降部字母，真墨底 = 基线）；P2 WIST JE DAT `erbij.` +7.3 px；P2 GEDICHT `taquin` +7.4 px；P7 HET WOORD `quart de finale.` +8.1 px；P7 PAS OP +11.4 px；P3/P4 末行 +16.2/+14.2 px；P1 IN DEZE EDITIE `Pag. 8` +11.0 px。**全部为正**。
- P1 HET WOORD 法语两行 vs 行规则 y=1853（线宽 1.2，带 1852.4–1853.6）：
  - PIL：上行 `« Victoire de groupe » : première place du` 墨底 1850.2，余量 **+2.2 px**；下行 `groupe, direction les quarts de finale.` 墨顶 1857.85，余量 **+4.25 px**；
  - 像素扫描：上行末墨行 1850.2（+2.18 px），下行首墨行 1856.9（+3.29 px）。紧但不触线（存证 `p1-gloss-rule.png`）。

## §7 印/网文字层比对 + 斜体 + 最小字号 + 引号

- 印/网词层（PyMuPDF 逐词多重集）：**8 页全等**——P1 826/826、P2 836/836、P3 730/730、P4 724/724、P5 811/811、P6 755/755、P7 947/947、P8 2437/2437；仅 print/ web 的 pdftotext 行序不同（栏序），内容无差。
- 斜体（ru-en D3 类）：本版唯一斜体 span 为 P1 `«de groepswinst»`。印 PDF 字体 `Newsreader16pt-Italic` 16.12 pt；**网 PDF 同 span 为 `LucernaNewsreader-Regular`，且整份网 PDF 无任何斜体字体**——斜体丢失（→ D3）。文字层无丢空格、无闭引号脱离。
  - 机制核实：本机 `fc-match 'Newsreader:weight=100:slant=italic'` 正确解析至 `Newsreader-Italic.ttf`；用当前 `tools/webpdf.py` 在 scratch 重建网 PDF（`rebuilt-web.pdf`，1,614,231 字节）含 `LucernaNewsreader-Italic`，该 span 恢复斜体，8 页词数与印 PDF 全等——证明修复 = 重建网 PDF。
- P8 最小字号（实测，非 KIT 口径）：印 PDF P8 答案区 span 最小 **10.12 pt**，中位 10.12 pt（与 KIT 的 10.12 一致）。
- 弯引号扫描（SVG 全文 + text.md）：« » 全版成对——P1 2/2、P2 2/2、P7 30/30、P8 2/2；无 U+201C/U+201D。
  - 撇号：版内 U+0027 约 40+ 处、U+2019 仅 8 处（P7 4、P8 4，见 D4 多法语层混用）；核心 8 页 SVG 含 U+2019 共 **0 处**（KIT“与核心相同”之说不实，见 PROOF-NOTE D4 附注）。

## §8 必查项逐项裁决

- (a) P1 框标题/副标题横向溢出：**P1 未复现**（numbers 标题余量 +5.0 px；`Agenda van de week　LES RENDEZ-VOUS` 副标题余量 +36.4 px；`IN DEZE EDITIE　CE NUMÉRO` 余量 +59.1 px；页边全清）。但同类缺陷在 P7 复现（D1）及 P6 边界（D2）。
- (b) P3/P5 右栏末行降部漫出：**未复现**（最紧 P6 图表 +3.7 px、P5 EN JIJ +6.3 px、P2 相关盒 ≥ +6.2 px）。
- (c) P7 toolbox clearance：**未复现**（min desc-clear +7.1 px，min inside +13.1 px）。
- (d) text.md E 节 type 标签：**未复现**——全部 8 类标签均为法语（Compléter les phrases / Choix unique / Associer les mots / Vrai ou faux / Faire des phrases / Texte à trous / Traduction / Écriture）；E 节用 `Traduction`；text.md 唯一中文是标准 `答案：` 标记 142×，与核心同数（导出格式惯例，非本地化残留）。
- (e) 网 PDF 斜体三联症：**部分复现**——丢空格、闭引号脱离均无，斜体丢失有（→ D3）。
- (f) ABSTRACT.txt：**未复现**——含 `Journal néerlandais Lucerna VOL.4 (16–22 novembre 2026)…`，刊名 + 期号齐全。

## §9 外部事实来源

- 本复校的事实全部来自磁盘实测（上述日志 + 8 页卡片目视 + text.md 全文通读 + PyMuPDF/PIL 实测）；未引用外部网页。
- 冻结核心作为对照基准：`production/2026-w47/core-nl/`（freeze baseline 8/8 证实其未被改动；p8 compare 证实键一致）。
- 判为非缺陷的项（摘要）：§3 keydiff 137/138（合法法语重定向）；§4 新增 CJK 仅为 U+3000 分隔符；§5 #63/#126（核心层构造，键与核心一致）；§6 P1 横线间隙（紧但 clearance 为正）；§8 (a)–(f) 除 D1/D2/D3/D4 对应项外全部未复现；KIT 数值中经核实者：P8 最小字号 10.12 pt、分级 46/73/31、范文 81 词、页分布均与实测一致。
- KIT 失实两处（不作版缺陷，记入档）：① “U+2019 quirk 与核心相同”——核心含 U+2019 共 0 处；② “print/web text posdiff 0” 为词级比较，测不到 D3 的样式丢失。

## §10 交付文件（scratch 内）

- `PROOF-NOTE.md`（结论 (b) + 缺陷 D1–D4 + 未决 O1–O4 + 核实摘要）
- `GATE-LOG.md`（本文件）
- `keycheck-150.json`（150 题逐题手验，150/150 verified）
- 证据：`occlusion.log`、`creambox-all.log`、`p8-compare.log`、`p8-compare.json`、`p8-extract-edition.json`、`p8-extract-core.json`、`freeze-diff.log`、`freeze-diff.json`、`freeze-baseline.log`、`pil-ink.log`、`pil-titles.log`、`span-check.log`、`span-check2.log`、`pixel-scan.log`、`pixel-scan2.log`、`keycheck-prep.log`、`txt/print-p*.txt`、`txt/web-p*.txt`、`rebuilt-web.pdf` + `rebuilt-web.log`（D3 修复验证）、`p7-hetwoord-title.png`、`p1-gloss-rule.png`、`p6-voortegen-title.png`（像素存证裁图）、`probe.txt`
