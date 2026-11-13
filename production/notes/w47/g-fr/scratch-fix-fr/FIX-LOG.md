# FIX-LOG — W47 fr 家庭独立重校 16 项补译注修复

- 日期：2026-11-12（UTC）
- 任务：修复独立重校发现的 16 项 minor 缺失（全是讲解层缺译注），重渲染受影响的 8 版并复核门禁。
- 范围：只动 `production/2026-w47/` 下 fr 家 8 版（`2026-w47-fr-es/it/ja/ko/nl/pt/ru/zh-tw`）；en、de、core-fr（= fr-zh-cn）0 项，未动。
- 依据：`~/workspace/weekly-git/SOP.md` §8；`hidden_files/w47/scratch-reproof-w47-fr/PROOF-NOTE.md`（16 项位置/证据/对照版）。
- 约束遵守：**未 commit、未 push、未跑 lint**；未碰其他家庭、其他周；未 reset/stash/git add。
- 工具链：`~/workspace/weekly-git/tools/venv/bin/python`；门禁脚本 `hidden_files/w47/scratch-d5-rebuild-fr/run_gates.sh`（run.py + render.py + webpdf.py + textlayer / occlusion / p8 / freeze / boxtitle / creambox / spill / edge / census 全套）。
- 仓库 HEAD：`b9ac29a6`（8 版目录在 clone 中为 untracked，故无 git diff，修改以 grep + text.md diff 核实）。
- 中途事件：驱动跑剩余 7 版时 VM/运行时重启，中断后台会话（ja 跑到一半，creambox.log 为 0 字节被杀；ko/nl/pt/ru/zh-tw 未开始）。已用 `run_resume.sh`（ja→zh-tw）续跑完成；**ja 重跑后印 PDF SHA 与重启前半程重建完全一致（`3121d66228dd`），确定性已证实**。

## §1 16 项逐项修后状态（全部已修）

源头均为各版 `expl.py`（栏目标题/译注的唯一源头；`content*.py`/`svglib.py` 中无重复定义）。译注文字均取自**该版自有译法**，未编造。

| # | 版 | 位置 | 修复 | 修后核实 |
|---|---|---|---|---|
| D1 | fr-ja | P1 NOTE `g1` | `un vin primeur` → `un vin primeur 新酒`（同版 P2 g2 已有该译注；对照 fr-en `a new wine`、core `新酒`） | 印 PDF 目视：P1 NOTE 行含 `primeur 新酒`；文字层含该行 |
| D2 | fr-zh-tw | P2 注释行 `bridge_valise` | `virgule 逗號` → `une virgule 逗號`（其余 10 版均有 `une`；virgule 阴性） | 印 PDF 目视：P2 含 `une virgule 逗號` |
| D3-1 | fr-es | P7 `head_clinic` | `CLINIQUE DES ERREURS` 补 `ERRORES` | 目视 P7 `CLINIQUE DES ERREURS　ERRORES` |
| D3-2 | fr-it | P7 `head_clinic` | 补 `ERRORI` | 目视 P7 `CLINIQUE DES ERREURS　ERRORI` |
| D3-3 | fr-ja | P7 `head_clinic` | 补 `誤り` | 目视 P7 `CLINIQUE DES ERREURS　誤り` |
| D3-4 | fr-ko | P7 `head_clinic` | 补 `오류` | 目视 P7 `CLINIQUE DES ERREURS　오류` |
| D3-5 | fr-nl | P7 `head_clinic` | 补 `FOUTEN` | 目视 fix2 P7 `CLINIQUE DES ERREURS　FOUTEN` |
| D3-6 | fr-pt | P7 `head_clinic` | 补 `ERROS` | 目视 P7 `CLINIQUE DES ERREURS　ERROS` |
| D3-7 | fr-ru | P7 `head_clinic` | 补 `ОШИБКИ` | 目视 fix2 P7 `CLINIQUE DES ERREURS　ОШИБКИ` |
| D3-8 | fr-zh-tw | P7 `head_clinic` | 补 `易錯診所`（core `易错诊所` 的繁体写法） | 目视 P7 `CLINIQUE DES ERREURS　易錯診所` |
| D3-9 | fr-nl | `head_cine` | `LE CINÉMA DU MERCREDI` 补 `FILMS`（en FILMS / de FILME 复数先例） | text.md L655；门禁全绿 |
| D3-10 | fr-ru | `head_cine` | 补 `КИНО`（取自该版 `head_mots_photo`） | text.md L655；门禁全绿 |
| D3-11 | fr-ru | `head_lire` | `LIRE LE CALENDRIER` 补 `КАЛЕНДАРЬ`（取自该版 `head_chart`） | text.md L723；门禁全绿 |
| D3-12 | fr-nl | `head_outils` | `BOÎTE À OUTILS` 补 `GEREEDSCHAPSKIST` → fix2 改为 `GEREEDSCHAP`（见 §4） | 目视 fix2 P7 `BOÎTE À OUTILS　GEREEDSCHAP` |
| D3-13 | fr-ru | `head_outils` | 补 `ИНСТРУМЕНТЫ`（取自该版 `bridge_outils`） | 目视 fix2 P7 `BOÎTE À OUTILS　ИНСТРУМЕНТЫ` |
| D3-14 | fr-ru | `sommaire_title` | `DANS CE NUMÉRO` 补 `СОДЕРЖАНИЕ`（对 de INHALT / nl INHOUD / ja 目次 / core 本期目录的标准俄语对应词） | 目视 fix2 P1 `DANS CE NUMÉRO　СОДЕРЖАНИЕ`；pdftotext -bbox 核实 x=1261.4–1379.7，页宽 1462.5pt，在页内 |

## §2 每版改前 / 改后（尺寸 + SHA-256 前 12；全 SHA 见各版 WEEKLY-KIT.md）

| 版 | 印 PDF 改前 → 改后 | 网 PDF 改前 → 改后 | text.md 改前 → 改后 | text.md diff（vs 修前） |
|---|---|---|---|---|
| es (fix1) | 17,031,451 `d732ed21b8be` → **17,031,455 `57d86cd14c5a`** | 1,622,812 `aa1b3076782d` → **1,622,809 `0f89bcd285da`** | 46,645 `7c340f2d9ede` → **46,655 `d348eda26a40`** | 1 行（L921 clinic） |
| it (fix1) | 17,027,791 `5d31cbc41f0a` → **17,027,797 `179461e905ff`** | 1,619,122 `20b66275d46c` → **1,619,126 `be09601e1dcf`** | 46,528 `ac5c096d167c` → **46,537 `0ca8ff5439bf`** | 1 行（L921） |
| ja (fix1) | 20,148,505 `a62d3c89d9a9` → **20,149,418 `3121d66228dd`** | 2,019,098 `bc8eb6e62d2b` → **2,019,912 `8c52331f7ce6`** | 47,508 `df028d09d5db` → **47,524 `354f6b094247`** | 2 行（L45 g1 新酒、L921） |
| ko (fix1) | 20,086,049 `9aeba6cc400e` → **20,086,243 `bfeb8970f59f`** | 1,923,039 `98170fbd21ae` → **1,923,201 `d972b7cbc104`** | 47,323 `f5474d61eead` → **47,332 `fd2dfe488c05`** | 1 行（L921） |
| nl (fix2) | 17,029,995 `c0c12aea4176` → **17,030,024 `45c0b11e87a7`** | 1,621,369 `36493cef193a` → **1,621,399 `fb98be3aa292`** | 46,250 `4a4a9fcc9bb5` → **46,281 `ad506a852519`** | 3 行（L655 cine、L855 outils、L921；fix2 相对 fix1 仅 L855 `GEREEDSCHAPSKIST`→`GEREEDSCHAP` 1 行） |
| pt (fix1) | 17,031,944 `8c01de5f3691` → **17,031,948 `4a76ddaca94d`** | 1,623,290 `a62233ec10cd` → **1,623,288 `302da684a631`** | 46,486 `12a860a9b4e1` → **46,494 `c7a3f3244476`** | 1 行（L921） |
| ru (fix2) | 17,331,940 `3459a9b9d3ed` → **17,332,080 `038ee398d117`** | 1,882,129 `ccfba10759e7` → **1,882,292 `f0e9d27b3934`** | 50,418 `9aa919b7c647` → **50,513 `3b6f2cf61934`** | 5 行（L109 sommaire、L655、L723、L855、L921；fix2 相对 fix1 0 行） |
| zh-tw (fix1) | 18,531,943 `de24f2a08c9b` → **18,532,970 `3f4f58df81c3`** | 2,074,668 `f54db205afbd` → **2,076,083 `6972666e0e72`** | 45,992 `e5c8c1cd50f0` → **46,011 `e257f1023046`** | 2 行（L229 une virgule、L921） |

改前值来源：`scratch-fix-fr/pre-shas.txt` + `pre-textmd/`（8 版修前 text.md；nl/ru 另有 `.fix1` 副本）；改后值为盘上最终实测（`sha256sum` + `stat` 全 8 版三件，2026-11-12）。网 PDF SHA 每次重建都会变，以上为最后一次落盘实测。

## §3 门禁复核结果（逐版；日志在 `scratch-d5-rebuild-fr/<版>/logs-fix1/` 或 `logs-fix2/`）

注：`run_gates.sh` 的 FAILFLAG 只反映 run/render/webpdf 返回码，不代表门禁——以下结论以各工具日志为准。

- **es fix1 — 全绿**：occlusion 0 flags；p8 CLEAN（121/121，keydiff=`[150]`，vs 修前基线 keydiff=`[]`）；boxtitle 0 DEFECT（38 titles）；spill 0；edge 0 TOUCH / 0 NEAR；D5 census PASS（0/0/0）；印/网文字层逐字节一致（99,397 字符，print.txt 100,842 B）；freeze baseline 8/8。残留警告：clinic ERRORES 445.2px（见 §8）。
- **it fix1 — 全绿**：occlusion 0；p8 CLEAN；boxtitle 0 DEFECT（38 titles）；spill 0/107；edge 0/0；census PASS；文字层 101,605 字符（print.txt 102,893 B）。残留警告：clinic ERRORI 423.4px（仅 0.9px，见 §8）。
- **ja fix1 — 全绿，零警告**：occlusion 0；p8 CLEAN；boxtitle 0 DEFECT（41 titles）；spill 0/104；edge 0/0；census PASS；文字层 93,346 字符（print.txt 100,875 B）。
- **ko fix1 — 全绿，零警告**：occlusion 0；p8 CLEAN；boxtitle 0 DEFECT（47 titles）；spill 0/136；edge 0/0；census PASS；文字层 94,860 字符（print.txt 101,667 B）。
- **nl fix1 — 不合格**：occlusion 1 EDGE（`GEREEDSCHAPSKIST` 墨迹 x 至 2014.1，超出 1950 宽页面）、edge 1 TOUCH。**fix2 — 全绿**：occlusion 0；boxtitle 0 DEFECT；spill 0/101；edge 0/0；census PASS；p8 CLEAN keydiff=`[150]`；文字层 97,995 字符（print.txt 99,238 B）。残留警告：clinic FOUTEN 432.6px（见 §8）。
- **pt fix1 — 全绿，零警告**：occlusion 0；p8 CLEAN；boxtitle 0 DEFECT（36 titles）；spill 0/103；edge 0/0；census PASS；文字层 99,282 字符（print.txt 100,788 B）。
- **ru fix1 — 不合格**：occlusion 0；p8 CLEAN；**boxtitle 1 DEFECT**（P1 `СОДЕРЖАНИЕ` 右溢 +10.9px）+ 3 处 HEAD TOO WIDE 警告；spill 0/107；edge 0/0（P7 右缘最小 46.8pt）；census PASS。**fix2 — 全绿，零警告**：boxtitle 0 DEFECT；edge 0/0；census PASS；p8 vs 核心 CLEAN，vs 修前基线 CLEAN keydiff=`[]`；文字层 multiset diff 0（97,022 字符，print.txt 104,035 B）。
- **zh-tw fix1 — 全绿，零警告**：occlusion 0；p8 CLEAN；boxtitle 0 DEFECT（40 titles）；spill 0/104；edge 0/0；census PASS；文字层 93,502 字符（print.txt 99,913 B）。

p8 vs 核心 keydiff=`[150]` 是已知非失败（Q150 开放题读者语标签差异，见 PROOF-NOTE）。

## §4 字号修正（fix2；D5 逐版降字号先例：de/pt 的 head_outils 已是 25，es 的 head_lire/head_clinic 已降过）

栏宽 CW = 422.5。实测宽度（tools/venv 的 `svglib.text_w`）：

- **nl**：`BOÎTE À OUTILS　GEREEDSCHAPSKIST` @27 = 574.6px，出页。改为译注 `GEREEDSCHAP` + `content7.py:58` 字号 27→23（415.0 ≤ 422.5，无警告；23 号与同版 P7 诊所头同号）。
- **ru（4 处）**：`content12.py:93` sommaire 24→22（原 +10.9px boxtitle DEFECT）；`content56.py:135` head_lire 25→23（431.1→396.7）；`content7.py:58` head_outils 27→25（450.6→417.2）；`content7.py:99` head_clinic 25→23（约 437.8→402.8）。fix2 后 0 HEAD TOO WIDE。

## §5 导出器陷阱干跑核查（ru 家补充指令的执行结果）

ru 家发现：text.md 重导出会悄悄丢标题行（导出器只收 sans 粗体 ≥24pt 的标题，D5 后缩到 22/23pt 的框题会被丢；处置口径：重导出前先干跑到 /tmp 再与修前文件 diff，落盘时原位置逐字回补被丢标题行；不改导出器、不动源码字号；最终 diff 只含意改行）。

fr 家核查结论：**无此陷阱，无需回补**。

- 代码检查：fr 家导出器（`scratch-fanout-fr/export_lang.py` + `stub_svg`/`stub_bslib`）**无尺寸阈值**——stub 无条件记录所有 head/title/boxtitle/shead/text。
- 干跑核查：8 版逐版干跑导出到 `/tmp/fix-fr-dryrun/<lang>/`，与修前文件 diff **只含意改行、无丢行**；干跑与盘上文件 7/8 字节一致（nl 差 1 行即意改的 GEREEDSCHAP 行，fix2 落盘后已用 `cmp` 核实与干跑一致；ru fix2 text.md 与干跑一致）。
- 详见 ru 家 FIX-LOG §7（ru 家因此回补了 de 2 行、es 1 行、fr 2 行、nl 1 行、pt 2 行、en 1 行标题）——fr 家不适用。

## §6 目视复核（裁图在 `/tmp/fix-fr-*.png`，临时件；每版至少一处）

- es P7 `CLINIQUE DES ERREURS　ERRORES`；it P7 `ERRORI`；ja P1 `primeur 新酒` + P7 `誤り`；ko P7 `오류`；pt P7 `ERROS`；nl fix2 P7 `GEREEDSCHAP` + `FOUTEN`；zh-tw P2 `une virgule 逗號` + P7 `易錯診所`；ru fix2 P1 `СОДЕРЖАНИЕ` + P7 `ИНСТРУМЕНТЫ` + `ОШИБКИ`。**全部干净、无溢出。**
- 另用 `pdftotext -bbox` 核实各译注在印 PDF 文字层中的位置（ru P1 СОДЕРЖАНИЕ x=1261.4–1379.7，页宽 1462.5pt，在页内）。

## §7 KIT 更新记录

8 版 WEEKLY-KIT.md 均已更新（只改 §四/Files 的现值行，不动带日期的历史条目）：

- es：L41–42 印/网字节+SHA、pdftotext 100,880→100,842 B；L62 text.md 46,655 B + 新 SHA；§五追加 fix1 条目。
- it：L41–42 印/网字节+SHA（pdftotext 102,893 B 不变）；L63 text.md 46,537 B + 新 SHA；§五追加 fix1 条目。
- ja：L68–69 印/网字节+SHA；L70 text.md 47,524 B + 新 SHA；L71 文字层 93,208→93,346 字符；Fix log 追加 fix1 条目。
- ko：L69–70 印/网字节+SHA；L71 text.md 47,332 B + 新 SHA；L72 文字层 94,860 字符不变；Fix log 追加 fix1 条目。
- nl：L13–14 印/网字节+SHA；L15 text.md 46,281 B + 新 SHA；L16 文字层 99,546→99,238 B；Fix log 追加 fix1→fix2 两轮条目。
- pt：L41–42 印/网字节+SHA（pdftotext 100,788 B 不变）；L62 text.md 46,494 B + 新 SHA；§五追加 fix1 条目。
- ru：L13–14 印/网字节+SHA；L15 text.md 50,513 B + 新 SHA；L16 文字层 97,297→97,022 字符；Fix log 追加 fix1→fix2 两轮条目。
- zh-tw：L92–93 印/网字节+SHA；L94 text.md 46,011 B + 新 SHA；L95 文字层 93,337→93,502 字符；Fix log 追加 fix1 条目。

未改：各 KIT 的 text.md「字符」数（es 44362、it 44361、nl 44135、pt 44145）——口径不明，实测 `len()` 与 KIT 既有值对不上（es 修前实测 44,413 ≠ 44,362），无法按同一口径更新；**字节 + SHA 为准**，全 SHA 已写入 KIT。

## §8 残留警告说明（门禁全绿、栏外伸入空白边距、无碰撞，接受）

- es clinic ERRORES 445.2px、it clinic ERRORI 423.4px（仅 0.9px）、nl clinic FOUTEN 432.6px：栏目标题超栏宽 ~10px，伸入空白边距，与 en D5 已发版 clinic ERRORS 428.6 同类。不再缩字号（再缩会破坏栏目标题层级一致性）。
- ja/ko/pt/zh-tw fix1 零警告；ru fix2 零警告。

## §9 备注

- **D1 历史**：ja P1 的 `新酒` 译注在 D5 rebuild #2 时曾被**有意删掉**（修孤儿日文句号 。独行；见 ja KIT Fix log）。本次按独立重校结论重新补回，NOTE 行重排后门禁全绿、目视无孤儿再现。供协调员知悉。
- es 试点发现：`run.py` 不重出 text.md，须用 `export_lang.py` 重出（在版目录内运行，cwd 即版目录；头行按该版读者语，HEADERS 已与 8 版现头逐版核对一致）。
- 驱动日志：`scratch-fix-fr/` 下 `driver-remaining.log`、`driver-fix2.log`、`logs-<版>-gates.log`、`logs-<版>-export.log`、`diffs/`（各版 diff + `nl-fix2.diff`、`ru-fix2.diff`）、`pre-shas.txt`、`pre-textmd/`。
- 未做：commit / push / lint（按任务约束）；core-fr 未动；其他家庭未动。
