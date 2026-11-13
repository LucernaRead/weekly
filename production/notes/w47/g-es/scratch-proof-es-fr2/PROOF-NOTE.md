# W47 es-fr proof2 — 独立复校笔记（重建版）

- 版：`production/2026-w47/2026-w47-es-fr/`（西语核心 × 法语读者版，es 全族重建版）
- 复校员：独立复校（与构建者 / fan-out agent 不同人）
- 日期：2026-11-11
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-fr2/`（下称 **S2**）
- 运行环境：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR = S2/tmp；未用系统 python3、未写 /tmp
- 状态：未 commit、未 push；**未改任何生产文件**（复核前后全目录哈希比对一致，见 §7）

## 结论：(a) 零缺陷，通过

独立重跑全部机械门 + 150 题三源手验 + text.md 全文通读（1,815 行）+ 8 页逐页渲染目视，
**缺陷 0 项**。必查项 C1 与全部回归项逐处实测归零（见 §4、§5）。

## 缺陷清单

无。观察项（非缺陷）见 §6。

## 1. 身份核对（三件 SHA，复核前与复核后两次实测一致）

| 产物 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| 印 PDF `La-Lucerna-VOL4-es-fr.pdf` | 3,500,186 | `688152c7a055a25414e9c72b33f9e6d074b8137c2a9e2c9ea365b4d541e14894` | ✓ 与任务给定一致 |
| 网 PDF `La-Lucerna-VOL4-es-fr-web.pdf` | 884,225 | `3c2d60696561278323150dafabe922bc77df682946e3266e89adfb9180a3016c` | ✓ 与任务给定一致（见 §7 还原说明） |
| text.md `2026-w47-es-fr.text.md` | 45,794 / 1,815 行 | `ae1c3f3ba234a0b3f5ce2128770e4e4983d509822fdd520d03da4e98a76fad43` | ✓ 与任务给定一致 |

核心 core-es 前后对照（复核前后各测一次，未变；印 SHA 前缀 2723a283…与任务一致）：

| core-es 产物 | SHA-256（前 = 后） |
|---|---|
| 印 `La-Lucerna-VOL4.pdf`（17,212,955 B） | `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5` |
| 网 `La-Lucerna-VOL4-web.pdf`（1,410,471 B） | `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235` |
| text.md `2026-w47-es-zh-cn.text.md` | `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb` |

## 2. freeze 首检 8/8；新增 CJK 分类

- freeze baseline：**8/8 SVG 逐字节一致**（重建产物哈希 =  shipped 哈希；repointed files: none；core 完整性：shipped core SVG 未被改动）。
- freeze-diff 新增 CJK 总计：**1 个字符，仅 U+3000**（p1）。其余 7 页新增 0。
  - 该 1 个 U+3000 是 P1 刊头带（y=330）的独立结构空格文本元（`font-size 36 / letter-spacing 4` 的刊头分隔符，
    与 core 同位置同类元素并存；core 该类元素 6 个、本版 4 个；diff 多重集净增 1）。
  - 分类：**结构空格，允许**。无其他新增 CJK 字符，无需逐一说明项。

## 3. 门禁汇总（全部独立重跑）

| 门 | 工具 / 方法 | 结果 |
|---|---|---|
| run | `run.py`（内容脚本重建 SVG） | rc=0，TOTAL 150（A2 50 / B1 72 / B2 28；按页 10/18/18/18/18/18/12/38）；8 个 SVG 哈希与 shipped 完全一致 |
| render | `render.py` | rc=0；印 PDF 复现**逐字节一致**（SHA 688152c7…）；网 PDF 内容一致、字节差 1（见 §7 注） |
| occlusion | `tools/occlusion_audit.py` | 0 flags（自检 planted 6 类全触发、干净对照静默） |
| p8 extract | `tools/p8.py extract --total 150` | **150/150** |
| p8 compare | `tools/p8.py compare`（vs core-es P8） | **CLEAN**，keydiff **[137, 138]**（已裁决项：E 组中文句答案键译成法语，见 §3.1）；missing/extra/uncertain 全空 |
| freeze baseline | `tools/freeze.py baseline` | **8/8** |
| freeze-diff | `tools/freeze.py diff` | 新增 CJK 1 × U+3000（§2） |
| creambox（canonical） | `hidden_files/w47/tools/creambox.py` 全版扫描 | **inside-only 负 clearance 0**；原始扫描 6 条负值全为盒下标题/注文（与 core 同类假阳性）；P7-TOOLBOX：3 盒，min inside +5.7，min desc-clear +0.0 |
| creambox 真墨 | `creambox_diag.py`（PIL 真墨） | 全部自有末行墨 clearance **≥ 0**（最小值见 §4） |
| boxtitle 真墨 | `boxtitle_core.py` | **0 溢出**；最小 clear +14.8 |
| keycheck | `keycheck_core.py`（REG vs P8 抽取） | **149/150**，唯一 mismatch 为 #150 开放写作题（抽取 `✓`，已知例外） |
| sweep | `sweep_de.py`（box-vs-hline / bridge） | box-vs-hline 0；bridges 20，orphans 0，widows 0 |
| text_layer | `pdftotext -layout` 印 vs 网 | 逐字节一致，109,748 B；且与 builder 的印/网文本层逐字节一致 |
| p8_font（minfont） | `minfont.py`（P8 印 PDF） | 最小有效字号 **10.125pt**（n=376），< 9.75pt 者 0 |
| widths / band_spans / scans / chips | 随 gates 驱动内含（keycheck / sweep / minfont） | 均 rc=0，无告警 |
| string_freeze / source_freeze | freeze baseline + diff 覆盖 | 8/8；源冻结一致（run 重建 SVG 逐字节一致） |

### 3.1 p8_compare 的 keydiff [137, 138]（已裁决，不判 (b)）

逐字符串比对版 P8 keys vs 核心 P8 keys：仅 137、138 两处不同，且恰为裁决情形——

- #137 核心：`周一是国际弗拉门戈日。` → 本版：`Lundi, c'est la Journée internationale du flamenco.`
- #138 核心：`周六我们看塞维利亚德比。` → 本版：`Samedi, nous regardons le derby de Séville.`

E 组中文句答案键须译成读者语（法语），status CLEAN。另：gates.json 的 p8 extra 若显示 "?" 是驱动误读键名——
已直接读 `fr-p8-compare.json`：`"extra": []`，无 extra。

### 3.2 150 题三源交叉手验

- 版 P8 keys（`fr-p8-extract.json`）vs text.md 答案区（RESPUESTAS）：149/150 解析比对，**0 不符**；
  唯一未解析为 #150（开放写作，键为 `✓`，已知例外）。
- 版 P8 keys vs 核心 P8 keys（`core-p8-extract.json`，独立抽取 150/150）：仅 [137, 138] 不同（§3.1）。
- REG vs P8 抽取（keycheck）：149/150，仅 #150 例外。
- text.md 全文 1,815 行逐行通读：全部 150 题的题干、选项与答案键逐题核对无误（含算术核验：
  RTVE 45+45+30+30+15+3×10=195 分钟；PSOE−Vox=45−30=15；禁发民调 24–28 日共 5 天；
  Q57 muchísimos、Q58 peor、Q59 mejor、Q60–64 过去时 ganó/recibió/perdió/volvió/cerró、
  Q93 tenga / Q94 sea / Q95 para que / Q96 Aunque、Q109 baje / Q110 sea / Q111 es / Q112 B、
  Q141–144 c/d/b/a、Q145–149 全 A 均与原文一致）。
- 注：text.md 中 Q96 的 “En la ___” 是分栏交错的导出假象；渲染版实为
  “___ los debates difieren, ninguno miente.”，键 Aunque——无缺陷。

## 4. 必查项：P1 CINCO CLAVES 盒 C1（独立重测）

| 测量项 | Builder 值 | **我方独立重测值** |
|---|---|---|
| 盒底（box bottom） | 1308.0 | **1308.0** |
| 末行基线（last baseline） | 1300.0 | **1300.0** |
| 末行真墨底（ink bottom） | 1304.2 | **1304.2** |
| 真墨 clearance | +3.8px | **+3.8px** |
| desc-clear（含下行字母余量） | — | +2.3px |

裁定：**薄但在内为正，不是缺陷**（字形未被切、墨未出盒；裁图 `visual/p1-c1.png` 目视确认末行
`Cinq clés, sans chiffres inventés.` 完整在盒内，盒底边在其下方清晰可见）。
core 原测 +5.8px，法语末行墨位略高，差值来源为法语译文行高，与盒高无关。

P1 全部盒题真墨重测（boxtitle，全部为正）：

| 盒题 | clear |
|---|---|
| CINCO（C1 盒题） | +316.2 |
| LA SEMANA EN CIFRAS　Chiffres | +43.1 |
| EN ESTA EDICIÓN　SOMMAIRE | +45.6 |
| BREVES　EN BREF | +184.7 |

全版真墨最小值另记：P4 ¿Y TÚ? 盒 +1.3px、P7 CARTAS 盒 +1.5px、C1 +3.8px、P3/P5 ¿Y TÚ? 各 +6.7px、
P2/P5 O1 各 +10.1px——**全部 ≥ 0**；P4、P7 两处裁图（`visual/p4-thin.png`、`visual/p7-toolbox.png`）
目视确认末行墨完整在盒内、无切割。P7 CARTAS 的 desc-clear 为 +0.0（5.7 − 0.30×19，恰好归零不为负），
真墨 +1.5px，仍为正。

## 5. 回归核查（本重建声称已修，逐处实测）

| 项 | 声称修复 | **独立实测** | 结论 |
|---|---|---|---|
| fr D1：P3 ¿Y TÚ? 盒 +9px | 真墨 clearance +6.7px | P3 盒 y=1298、底 1603.8，末行墨底 1597.1，**+6.7px**；裁图 `visual/p3-d1.png` 墨在盒内 | ✓ 已归零 |
| fr D1：P5 ¿Y TÚ? 盒 +9px | 真墨 clearance +6.7px | P5 盒 y=1288、底 1593.5，末行墨底 1586.9，**+6.7px**；裁图 `visual/p5-d1.png` 墨在盒内 | ✓ 已归零 |
| fr O1：P2 ¿SABÍAS QUE…? 盒 +5px | 真墨 clearance +10.1px | P2 盒 y=200、底 553.5，末行墨底 543.4，**+10.1px**；裁图 `visual/p2-o1.png` 墨在盒内 | ✓ 已归零 |
| fr O1：P5 VOTAR POR PRIMERA VEZ 盒 +5px | 真墨 clearance +10.1px | P5 盒 y=939、底 1261.5，末行墨底 1251.4，**+10.1px**；裁图 `visual/p5-o1.png` 墨在盒内 | ✓ 已归零 |
| LA SEMANA 盒题溢出（首轮漏检，pt proof1 曾指出） | `… EN CHIFFRES` → `… Chiffres` | boxtitle：`LA SEMANA EN CIFRAS　Chiffres` right=917.9，**clear +43.1**；裁图 `visual/p1-lasemana.png` 标题在盒内 | ✓ 已归零 |
| 同批：ERRORES TÍPICOS 盒题溢出 | `… ERREURS TYPES` → `… Erreurs` | boxtitle：`ERRORES TÍPICOS　Erreurs` right=1771.5，**clear +90.5**；裁图 `visual/p7-errores.png` 标题在盒内 | ✓ 已归零 |

## 6. D5 字体（全周级已知待定项，只记录，不判 (b)）

实测：SVG 文本元共 1,658 个，其中 font-family 为 `Noto Sans CJK SC` 者 638 个、
`Newsreader` 976 个、`Noto Serif CJK SC` 43 个、`UnifrakturMaguntia` 1 个。
**拉丁-only 文本落在 `Noto Sans CJK SC` 上：398 段**（分頁：p1 47、p2 50、p3 52、p4 49、p5 50、p6 40、p7 53、p8 57）。
落在 `Noto Serif CJK SC` 上的拉丁-only 文本：0 段。
（注：该族字体同时承载全部无衬线拉丁文本——标题、标签、法语讲解层皆然；此为全周级待定项，本版只记录段数。）

## 7. 网 PDF 字节复现性注记与还原（重要过程记录，非缺陷）

- 我方独立重跑 `render.py` 时，印 PDF 复现**逐字节一致**（SHA 688152c7…不变），
  但网 PDF 复现为 884,226 B、SHA `6e0c2ab7…`，与交付的 884,225 B / `3c2d6069…` 差 1 字节。
- 逐层比对证明差异纯属字体子集化内部排序噪声，**内容完全一致**：
  - `pdftotext -layout`：我方印/网文本层与 builder 的印/网文本层**逐字节一致**（109,748 B）；webpdf 文本字节数同为 46,790。
  - pypdf 逐对象比对：34 个条目中仅 18 处不同，**全部是 /FontFile2 子集字体程序**，
    且每处解压后长度完全相同（如 3096 = 3096、6744 = 6744），仅字节序不同；
    全部内容流与全部 8 页抽取文本**零差异**。
  - 两版网 PDF 各页 72dpi 渲染像素比对：**8/8 页差异像素 0**。
  - 无 CreationDate/ModDate 等时间戳字段（仅 `/Producer (pypdf)`）。
  - 结论：webpdf.py 的字体子集化在不同进程间不具字节稳定性（疑似 hash 种子相关的字形排序），
    印 PDF 的 cairosvg 路径则逐字节稳定。**交付后请勿重渲染网 PDF；以交付字节为准。**
- **还原**：我方已用 builder freeze 时的 build-copy（`scratch-refanout-es/freeze-es-fr/build-copy/`，
  SHA 验为 `3c2d6069…` 的原始字节）把网 PDF 恢复原样；复核后三件 SHA 与复核前完全一致，
  生产目录全文件哈希与复核前快照（`before-hashes.txt`，35 文件）**逐项一致、diff 为空**。
  另：`fr-gates.json` 是重渲染当时写入的快照，其中 web_sha 记为重渲染值 `6e0c2ab7…`，
  不代表最终交付状态；最终交付网 PDF SHA 仍为 `3c2d6069…`（已还原并复验）。

## 8. 观察项（非缺陷，不影响结论）

1. C1 真墨 clearance +3.8px（§4）：薄但为正，按已定规则不判缺陷。
2. 全版最薄两处：P4 ¿Y TÚ? 盒 +1.3px、P7 CARTAS 盒 +1.5px（desc-clear +0.0）：均为正，裁图确认墨在盒内。
3. #88 法语注释略宽松：题面 C 为 “solo datos oficiales, con fuente”，答案区法语注为
   “Seulement les temps gratuits, avec la source”（指 RTVE 免费分钟图表本身即官方数据+来源）——
   键字母 C 正确，注释事实不假；仅措辞可更贴切，不判缺陷。
4. P1 urna 图注 “En la página 5, titular.” 与 core-es 一字不差，属冻结核心文案，不议。
5. 网 PDF 字节复现性：见 §7——交付字节已还原，建议后续流程勿重渲染网 PDF。
6. “next Sunday” 冻结英文：在 core-es 与本版全部 .py/.svg/.md 中**零出现**，本版无此项可核。

## 9. 目视记录

- 8 页逐页渲染目视（cards/*.png，由我方 render.py 复现，哈希与交付前一致；缩略图见 `visual/p1.png`–`p8.png`）：
  P1–P8 版式、图片、图表、练习区、答案区均干净，无溢出、无重叠、无缺字。
- 关键部位裁图（`visual/`）：p1-c1、C1；p3-d1、p5-d1（D1）；p2-o1、p5-o1（O1）；p1-lasemana、p7-errores（盒题）；
  p7-toolbox（最薄盒）、p4-thin（最薄盒）——全部确认墨在盒内。

## 10. 交付物（S2 内）

- `PROOF-NOTE.md`（本文件）、`GATE-LOG.md`
- `fr-run.log`、`fr-render.log`、`fr-gates.json`、`fr-gates-run.log`
- `fr-occlusion.log`、`fr-occlusion.json`、`fr-p8-extract.log`、`fr-p8-extract.json`、
  `fr-p8-compare.log`、`fr-p8-compare.json`、`core-p8-extract.log`、`core-p8-extract.json`
- `fr-freeze.log`、`fr-freeze-diff.log`、`fr-freeze-diff.json`、`freeze-es-fr/`（baseline build-copy）
- `fr-creambox.log`（canonical creambox）、`fr-creambox-diag.log`（真墨）、`fr-boxtitle.log`、
  `fr-keycheck.log`、`keycheck-150.json`、`fr-sweep.log`、`fr-minfont.log`、
  `fr-print.txt`、`fr-web.txt`（印/网文本层）
- `before-hashes.txt`、`after-hashes.txt`、`final-hashes.txt`（生产目录复核前/中/后哈希）
- `visual/`（8 页缩略图 + 9 张关键部位裁图）、`tmp/webcmp-o/`、`tmp/webcmp-m/`（两版网 PDF 渲染像素比对）
- `gates.py`、`creambox_diag.py`、`boxtitle_core.py`、`keycheck_core.py`、`minfont.py`、`sweep_de.py`、
  `check_p8keys.py`（门禁驱动与复核脚本副本；creambox 用 canonical 版，未复制）
