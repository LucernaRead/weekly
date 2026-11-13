# FIX-LOG-2 — W47 fr 家庭第二轮重校 3 项修复

- 日期：2026-11-12（EST；驱动 18:04–18:40 UTC）。
- 任务：修复第二轮独立重校（PROOF-NOTE-2.md）发现的 3 项 low（R2-1/R2-2/R2-3），重渲受影响的 5 版并复核门禁，更新 KIT。
- **未动版：core-fr（fr-zh-cn）、fr-en、fr-de、fr-es、fr-it、fr-pt 共 6 版只字未改。**收尾核实：6 版印/网 PDF + text.md 的 SHA-256 前 12 位与 PROOF-NOTE-2 所列全部一致（core `f36c32f020e4`/`ff08e74903d6`/`52024e024d32`、en `0503cff0885d`/`11e5babac345`/`82f53a7aa6af`、de `234a877ebbbb`/`68c62c41b596`/`de37011a23a0`、es `57d86cd14c5a`/`0f89bcd285da`/`d348eda26a40`、it `179461e905ff`/`be09601e1dcf`/`0ca8ff5439bf`、pt `4a76ddaca94d`/`302da684a631`/`c7a3f3244476`）。
- 依据：`hidden_files/w47/scratch-reproof2-w47-fr/PROOF-NOTE-2.md`（3 项）；`hidden_files/w47/scratch-fix-fr/FIX-LOG.md`（第一轮流程：run_gates.sh + export_lang.py，照抄）；`~/workspace/weekly-git/SOP.md` §8。
- 约束遵守：**未 commit、未 push、未跑 lint**；未碰其他家庭、其他周；未改 SOP；只改 fr 家庭 5 版的生产源（各版 `expl.py` + 重建的印/网 PDF + 重导出的 text.md + WEEKLY-KIT.md）。
- 工具链：`~/workspace/weekly-git/tools/venv/bin/python`；门禁脚本 `hidden_files/w47/scratch-d5-rebuild-fr/run_gates.sh`（tag `r2`）；驱动 `scratch-fix2-w47-fr/run_r2.sh`（日志 `driver-r2.log`，rc=0）。
- 磁盘：开工 95G/150G（63%），收尾 95G/150G，未触 100G 门限。

## §1 3 项逐项修后状态（全部已修）

修法均为改讲解层源码 `expl.py`（第一轮同一做法），再重导出 text.md、重渲印/网 PDF；不是只改 text.md。

| # | 版 | 位置 | 修复（文件:行） | 修后核实 |
|---|---|---|---|---|
| R2-1 | fr-ja | P7 文法点题头 `gp4` + P8 答案 100 简析 `n_gp4` | `expl.py:175` `文法 \| en beauté：美しく締めくくる。` → `文法 \| se terminer en beauté：美しく締めくくる。`；`expl.py:292` `en beauté = 美しく締めくくる` → `se terminer en beauté = 美しく締めくくる`（对照 de `se terminer en beauté: schön enden` / en `se terminer en beauté: to end in style`） | text.md L893、L1079；印 PDF 文字层含 `se terminer en beauté：美しく締めくくる` 与 `100. beauté（se terminer en beauté = 美しく締めくくる）`；P7 目视题头完整（见 §5） |
| R2-1 | fr-ko | 同上 | `expl.py:175` `문법 \| en beauté: 아름답게 마무리하다.` → `문법 \| se terminer en beauté: 아름답게 마무리하다.`；`expl.py:292` `en beauté = 아름답게 마무리하다` → `se terminer en beauté = 아름답게 마무리하다` | text.md L893、L1079；印 PDF 文字层在位；P7 目视题头完整 |
| R2-1 | fr-nl | 同上 | `expl.py:175` `Grammatica \| en beauté: mooi eindigen.` → `Grammatica \| se terminer en beauté: mooi eindigen.`；`expl.py:292` `en beauté = mooi eindigen` → `se terminer en beauté = mooi eindigen` | text.md L893、L1079；印 PDF 文字层在位；P7 目视题头完整 |
| R2-1 | fr-ru | 同上 | `expl.py:175` `Грамматика \| en beauté: красивый финал.` → `Грамматика \| se terminer en beauté: красивый финал.`；`expl.py:292` `en beauté = красиво` → `se terminer en beauté = красиво` | text.md L893、L1079；印 PDF 文字层在位；P7 目视题头完整 |
| R2-2 | fr-nl | P4 NOTE `g4` | `expl.py:41` `un vainqueur winnaar` → `un vainqueur een winnaar`（同版 P1 NOTE L45 `un vainqueur een winnaar` 为对照） | text.md L465；印 PDF 文字层含 `un vainqueur een winnaar`（P1、P4 各 1 处，共 2 处） |
| R2-3 | fr-zh-tw | P8 答案 93 简析 `n_micro6b` | `expl.py:285` `眾議員否決收入部分` → `議員否決收入部分`（先核对 core-fr：`core-fr/expl.py:301` 为 `议员否决收入部分`，一致；答案键 `ont rejeté` 不动） | text.md L1075；印 PDF 文字层含 `93. ont rejeté（議員否決收入部分）` |

改前旧形式全家 grep 零残留：`en beauté` 题头（`gp4`/`n_gp4`）、`眾議員否決`、`un vainqueur winnaar`（P4 语境）在 5 版 `expl.py` 中已无一处。

## §2 每版改前 / 改后（尺寸 + SHA-256 前 12；全 SHA 见 §6 与各版 WEEKLY-KIT.md）

改前值来源：`scratch-fix2-w47-fr/pre-shas.txt` + `pre-textmd/`（5 版修前 text.md），与 PROOF-NOTE-2 所列逐项一致；改后值为盘上最终实测（`sha256sum` + `stat` 全 5 版三件，2026-11-12）。网 PDF SHA 每次重建都会变，以上为最后一次落盘实测。

| 版 | 印 PDF 改前 → 改后 | 网 PDF 改前 → 改后 | text.md 改前 → 改后 | text.md diff（vs 修前） |
|---|---|---|---|---|
| ja | 20,149,418 `3121d66228dd` → **20,149,490 `f3f9d526f158`** | 2,019,912 `8c52331f7ce6` → **2,019,995 `a1951960b852`** | 47,524 `354f6b094247` → **47,548 `d243033462d4`** | 2 行（L893 gp4、L1079 ans 100） |
| ko | 20,086,243 `bfeb8970f59f` → **20,086,280 `acb99672c246`** | 1,923,201 `d972b7cbc104` → **1,923,242 `f7341f1a0a4f`** | 47,332 `fd2dfe488c05` → **47,356 `4929e183f280`** | 2 行（L893、L1079） |
| nl | 17,030,024 `45c0b11e87a7` → **17,030,093 `c7e99156a889`** | 1,621,399 `fb98be3aa292` → **1,621,462 `d846793366f5`** | 46,281 `ad506a852519` → **46,309 `a5f5c7ebbfc8`** | 3 行（L465 g4、L893、L1079） |
| ru | 17,332,080 `038ee398d117` → **17,332,158 `387991e60727`** | 1,882,292 `f0e9d27b3934` → **1,882,380 `5fdfbf439848`** | 50,513 `3b6f2cf61934` → **50,537 `1985e95d9be2`** | 2 行（L893、L1079） |
| zh-tw | 18,532,970 `3f4f58df81c3` → **18,532,749 `e6ef33ce2f62`** | 2,076,083 `6972666e0e72` → **2,075,855 `0d6b19e48c69`** | 46,011 `e257f1023046` → **46,008 `3dc051e14be0`** | 1 行（L1075 ans 93） |

印/网 PDF 均为 8 页（pdfinfo 核实，10 个文件全 8 页）。

## §3 门禁复核结果（逐版；日志在 `scratch-d5-rebuild-fr/<版>/logs-r2/`，驱动日志 `scratch-fix2-w47-fr/logs-<版>-gates-r2.log`）

注：`run_gates.sh` 的 FAILFLAG 只反映 run/render/webpdf 返回码，不代表门禁——以下结论以各工具日志为准。

- **ja r2 — 全绿，零警告**：run 0 FLOW OVERFLOW / 0 HEAD TOO WIDE；render rc=0；webpdf rc=0；occlusion 0 flags；p8 CLEAN（121/121，vs 核心 keydiff=`[150]`，vs 修前基线 keydiff=`[]`）；boxtitle 0 DEFECT（41 titles）；spill 0/104；edge 0 TOUCH / 0 NEAR；census PASS（0/0/0/0）；creambox PASS 0 defects（n=495）；印/网文字层逐字节一致（93,507 字符，print.txt 101,036 B）；freeze baseline 8/8，freeze diff vs core added CJK 2325 / Latin 116。
- **ko r2 — 全绿，零警告**：同上结构；boxtitle 0 DEFECT（47 titles）；spill 0/136；creambox PASS 0 defects（n=493）；文字层 95,023 字符（print.txt 101,830 B）；freeze diff vs core added CJK 2563 / Latin 94。
- **nl r2 — 全绿，1 条已接受残留警告**：boxtitle 0 DEFECT（38 titles）；spill 0/101；edge 0/0；census PASS；creambox PASS 0 defects（n=520）；p8 CLEAN keydiff=`[150]`；文字层 98,218 字符（print.txt 99,461 B）；freeze diff vs core added CJK 10 / Latin 521。残留：run.log 1 HEAD TOO WIDE `[P7-clinic] CLINIQUE DES ERREURS　FOUTEN`——与 fix2 日志逐字相同、第一轮 FIX-LOG §8 已接受项（432.6px，伸入空白边距，无碰撞），非本轮改动引起。
- **ru r2 — 全绿，creambox 3 缺陷为已裁定误报**：boxtitle 0 DEFECT（43 titles）；spill 0/107；edge 0/0；census PASS（拉丁/西里尔入 CJK=0、弯引号=0；`noto_sans_elements=1014` 为 PROOF-NOTE-2 已注明不重报的跨家 D5 已知问题）；p8 CLEAN keydiff=`[150]`；文字层 97,242 字符（print.txt 104,255 B）；freeze diff vs core added CJK 9 / Latin 225。creambox rc=1，FAIL 3 defects——与 r1/fix2 逐字相同（P5 `debat5_note` 三行被匹配到其第二处复现，见 ru KIT D5 条目已裁定：误报；独立 spill_sweep 0 SPILL；P5 原文完整在框内）。
- **zh-tw r2 — 全绿，零警告**：boxtitle 0 DEFECT（40 titles）；spill 0/104；edge 0/0；census PASS；creambox PASS 0 defects（n=486）；p8 CLEAN keydiff=`[150]`；文字层 93,502 字符（print.txt 99,911 B）；freeze diff vs core added CJK 972 / Latin 46。

附加门（任务单列，`run_gates.sh` 之外逐项实测）：

| 门 | 5 版结果 |
|---|---|
| `tools/p8.py compare --core-dir production/2026-w47/core-fr --edition-dir <版> --target fr --total 150` | 5 版全部 **CLEAN，121/121 noted，missing=[]，extra_count=0**，keydiff=`[150]`（Q150 开放题读者语标签差异，已知非失败）。注：任务所写 `--core-dir production/2026-w47/2026-w47-fr-zh-cn` 该目录不存在，core 实际在 `production/2026-w47/core-fr/`（其内 text.md 名为 `2026-w47-fr-zh-cn.text.md`）；与 `run_gates.sh` 用法一致，改用 core-fr 实测。 |
| 印/网 PDF 页数 | 10 个文件全 8 页（pdfinfo） |
| 印/网提取文本逐字节一致 | 5 版全部 `cmp` 一致（print.txt == web.txt，multiset diff 0） |
| P8 答案 1–150（印 PDF 提取文本） | 5 版 **missing=[]**（初版正则漏写 `150` 致伪报 missing=[150]，已修正正则重测；`150. Open vraag` 等确在文字层） |
| U+201C/U+201D 普查（text.md + 印 PDF 文字层） | 5 版 **U+201C=0、U+201D=0**（U+2018/U+2019/直引号 `"` 亦为 0；法语用 « »） |
| D5 census | 5 版 **PASS**：拉丁入 CJK=0、西里尔入 CJK=0、弯引号入 CJK=0、弯引号总数=0（见 §3 各版） |

## §4 导出器陷阱干跑核查（本轮执行结果）

按任务要求：每版先干跑导出到 `/tmp/fix2-dryrun/<版>/`（仅复制 `*.py` + `assets`，不碰生产目录），与修前 text.md diff；再正式导出，对比干跑结果。

- 5 版干跑 diff **只含意改行、无丢行**：ja 2 行、ko 2 行、nl 3 行、ru 2 行、zh-tw 1 行，与 §2 的正式导出 diff 逐行一致；干跑 text.md 与正式导出 text.md `cmp` **逐字节相同**（5/5）。
- **无需回补**：无任何标题行丢失（fr 家导出器无尺寸阈值，第一轮 FIX-LOG §5 同结论；本轮 gp4 变长后仍无丢失）。
- 内容复核：印 PDF 文字层（fix1 基线 vs r2）去空白字符后差量恰为意改内容——ja/ko/ru +20 字符（`se terminer`×2）、nl +21（`se terminer`×2 + `een`，另含 fix1→fix2 已知的 `GEREEDSCHAPSKIST`→`GEREEDSCHAP` 基线差）、zh-tw −1 字符（去 `眾`）；其余 0 增删。

## §5 P7 渲染目视（裁图在 `/tmp/fix2-p7/<版>-gp4.png`，临时件；题头行全幅裁切）

5 版 P7 文法点题头行逐版目视：

- ja：`文法| se terminer en beauté：美しく締めくくる。` 完整，折为 2 行（`る。` 在第 2 行），无溢出、无截断、无碰撞。
- ko：`문법| se terminer en beauté: 아름답게 마무리하다.` 完整，折为 2 行（末尾句号 `.` 独占折行行首），无溢出、无截断、无碰撞。
- nl：`Grammatica | se terminer en beauté: mooi eindigen.` 完整，折为 2 行，无溢出、无截断、无碰撞。
- ru：`Грамматика | se terminer en beauté: красивый финал.` 完整，折为 2 行，无溢出、无截断、无碰撞。
- zh-tw（R2-1 未动版，对照）：`文法｜se terminer en beauté：圓滿收尾。` 单行完整，与其余 4 版修复后一致。

说明：gp4 加长后 ja/ko/nl/ru 四版题头由 1 行折为 2 行，属栏内正常折行（其余文法点同为折行体例），下方 100. 题干位置不受影响；ja/ko KIT 的 Visual QA 句 `(gpN all 1 line)` 已同步改为 `(gp4 wraps to 2 lines after the R2-1 fix, all fit)`，zh-tw 单行未变、不改。

## §6 KIT 更新记录

5 版 WEEKLY-KIT.md 均已更新（只改 Files 现值行 + Fix log 追加 r2 条目，不动带日期的历史条目；ja/ko 另改 Visual QA 一句，见 §5）：

| 版 | 印 PDF（新） | 网 PDF（新） | text.md（新） | 文字层（新） |
|---|---|---|---|---|
| ja | 20,149,490 B `f3f9d526f158111e90611ecec90592b047451bcc5202a802b6a24a821107f44a` | 2,019,995 B `a1951960b852759375f1c94bc30177869c034a63b0ad154a7c5914ce4fd7436f` | 47,548 B `d243033462d46cdda5c87128fba36a70b9f0903b10057c90222faa1f18636683` | 93,507 字符 |
| ko | 20,086,280 B `acb99672c2468b2649bf0bfc8bd303c18cf4712a3477a8259231b3cec4e50cc3` | 1,923,242 B `f7341f1a0a4f5781d2a5b4ae295678fdced3de2b51cb70294eda539bfb0c7e4b` | 47,356 B `4929e183f280c71951d30f84e4234aa3ee28c4345720406039a22534e8cc4b8a` | 95,023 字符 |
| nl | 17,030,093 B `c7e99156a889019993fe6fc66b74e000e7232c7d5408be3a5cf4e79152cdb212` | 1,621,462 B `d846793366f5faf26da2faf9bc848b7adc8aa4fee73086d28060a319107957a4` | 46,309 B `a5f5c7ebbfc80d6351bed6fc8738222ea6a05777a111ae64b62d3a859be52820` | 99,461 B |
| ru | 17,332,158 B `387991e607272a4b546f6e3ff2c855dcce004ba5e67d41aaf0127cf45b4d0192` | 1,882,380 B `5fdfbf439848981d842ce9d4a73e2aaadfc35df6404fdaefade393dd42e65aeb` | 50,537 B `1985e95d9be2482a94b0ef2b58f14640f8f82ed8ede3c091a9e274830140fa6a` | 97,242 字符 |
| zh-tw | 18,532,749 B `e6ef33ce2f62f085001da0320fb5e0684d1d5aff22b735c3521da959517c23e1` | 2,075,855 B `0d6b19e48c6908be32dd08555254073afe62fe66b0d6f42a554f8d5255bdc1fe` | 46,008 B `3dc051e14be04dd404c2f3af0d227e22eef7b7212e608ed1e775ac9dbd5b92fd` | 93,502 字符（不变） |

三点核对通过：5 版 × 3 件的完整 SHA-256 与字节数均与 KIT 所载逐项一致（全 SHA + 去逗号后尺寸逐项 grep 核对；text.md 的 KIT 行不含文件名，以 `.text.md` 行首匹配核对）。

未改：各 KIT 的 text.md「字符」数（nl 44135）——口径不明（第一轮 FIX-LOG §7 同注），字节 + SHA 为准。

## §7 残留问题

- **无新增缺陷。** 残留仅以下两项既往已裁定项，均与本轮改动无关：
  - nl：1 HEAD TOO WIDE `[P7-clinic] CLINIQUE DES ERREURS　FOUTEN`（第一轮 §8 已接受，栏外伸入空白边距，无碰撞）。
  - ru：creambox FAIL 3 defects（r1 已裁定为测量误报：P5 `debat5_note` 复现匹配错位；独立 spill_sweep 0 SPILL）。
- 观察项（非缺陷）：ko 版 gp4 释义末尾句号 `.` 独占折行行首（释义过长折行所致，句号在位、无丢失）；ja 版同位置折为 `る。` 两字一行。均不处理。

## §8 备注

- 驱动日志：`scratch-fix2-w47-fr/` 下 `driver-r2.log`、`run_r2.sh`、`logs-<版>-gates-r2.log`、`logs-<版>-export-r2.log`、`logs-<版>-export-dryrun.log`、`diffs/`（各版 `*-dryrun.diff` + `*.diff`）、`pre-shas.txt`、`pre-textmd/`；门禁明细 `scratch-d5-rebuild-fr/<版>/logs-r2/`（`run.log`、`render.log`、`webpdf.log`、`shas.txt`、`print.txt`/`web.txt`、`textlayer.txt`、`occlusion.log`、`p8-*.log`/`*.json`、`freeze-*.log`、`boxtitle.log`、`creambox.log`、`spill.log`、`edge.log`、`census.log`/`census.json`）。
- 注意：`scratch-d5-rebuild-fr/<版>/logs-r2/textlayer.txt` 内含两组字符数——首组为此前 D5 r2 轮次残留（`tee -a` 追加所致），末组为本轮实测；§3/§6 所引字符数均以本轮末组 + 直接 `len()` 实测为准（print==web 逐字节一致）。
- 未做：commit / push / lint（按任务约束）；core-fr 与 en/de/es/it/pt 未动（SHA 已核对，见页首）。
