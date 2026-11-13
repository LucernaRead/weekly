# W47 D5 重建 — ko 家庭工作日志

- 工人：ko 家庭重建工人；开工 2026-11-12 ~03:10 EST
- 家庭：core-ko（ko-zh-cn）+ 9 fan-out：ko-en、ko-es、ko-fr、ko-de、ko-it、ko-pt、ko-nl、ko-ru、ko-zh-tw
- 不在本次任务内：2026-w47-ko-ja（任务清单无此版，不碰）
- 模板：mechanism/svglib-ko-d5.py；解释器：tools/venv/bin/python（Pillow 13），freeze 一步用 /usr/bin/python3（Pillow 10.2.0，协调员已批一次性例外）
- 磁盘开工时：df 91G 已用（任务称 94.7G；门限 ≥100G 停手）
- **接替记录（2026-11-12 ~04:31 EST，第二任工人）**：上一任 9ab2f774 在 04:28 EST 被第二次运行时重启打断。接替时核实：前 7 版（core-ko、ko-en、ko-es、ko-fr、ko-ru、ko-de、ko-it）生产印/网 PDF 的 SHA 与本日志所记逐版一致，全部落地在生产目录，无需重做；ko-pt、ko-nl、ko-zh-tw 三版的重建已在生产目录完成（生产 SHA 与 `logs/pdf-patched.sha256` 一致、与 pre-D5 不同），门禁做到一半被打断——ko-pt 缺 edge/creambox/textlayer，ko-nl 缺 creambox/textlayer，ko-zh-tw 缺 boxtitle/edge/creambox/textlayer，三版均未同步 KIT。第二任只补跑缺失门禁（`finish_gates.sh`，venv；freeze 未重跑，已有结论沿用）+ KIT 同步 + 清 build 副本，未重建任何一版。接替时 df 92G 已用，收尾时 92G。

## core-ko（ko-zh-cn）

### core-ko（ko-zh-cn）— DONE 2026-11-12 ~08:45 UTC
- 安装：`--patch-core ko` 按设计拒绝（old-style svglib，无 `_char_font`）；模板 `svglib-ko-d5.py` 落盘，`_D5_READER="cjk"`，与模板仅差该行。旧 svglib 存 `svglib.pre-d5`。
- 基线：base-venv（旧 svglib + venv）8/8 SVG 与交付字节一致；TOTAL 150（P2 FLOW OVERFLOW 警告 1 处，不改任何输出字节）。
- 重建：venv，TOTAL 150，0 警告。印 PDF `Lucerna-VOL4.pdf` 45,167,884 B sha256 `fa67a1af9d6d…`；网 PDF `Lucerna-VOL4-web.pdf` 4,210,506 B sha256 `5b596e5fe459…`。
- 门禁：census PASS（0/0/0）；quotes 0；head_check PASS；occlusion 0 flags；p8 150/150 compare CLEAN；spill 0；boxtitle 0 DEFECT（63 titles）；edge 0/0；creambox PASS 0 defects（n=381 median 1.008，P8 206→205 行，余量 78.1→78.1）；textlayer multiset 差 0（18,127=18,127）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0；baseline 7/8——P1 一处显示数字 "1" 185 vs 183pt（解释器量度 artefact，文本 0 差），已裁定非缺陷。
- 内容缺陷：0 处。KIT 已同步（输出 SHA/尺寸 + D5 节）。build 副本（base/、freeze/）已清。

### 2026-w47-ko-en — DONE 2026-11-12
- 安装：模板 + `_D5_READER="latin"`，与模板 0 行差。基线 base-venv TOTAL 150（P2 FLOW OVERFLOW 警告 1 处，core 内容，pre-D5 已有）。
- 重建：venv，TOTAL 150，0 警告。印 PDF 43,747,373 B sha256 `eb62691270b7…`；网 PDF 3,948,079 B sha256 `4c9091c06423…`。
- 门禁：census PASS；quotes 0；head_check PASS；occlusion 0；p8 150/150 compare CLEAN（keydiff=[137,138]）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox 绝对缺陷 0（P8 218→238 行，余量 75.5→62.7）；textlayer 差 0（22,483=22,483）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0；baseline 7/8——P1 同 core-ko artefact（文本 0 差）。
- P6 creambox "spill" 已裁定为工具误报（盒子随栏下移，行在新盒内；渲染裁图证实），未改内容。KIT 已同步；build 副本已清。
- 注：KIT 原 web PDF SHA（8fe16cdd…）在我开工前已 stale，在盘 pre-D5 web PDF 为 d4caa904…；已在 KIT 注明。

### 2026-w47-ko-es — DONE 2026-11-12
- 安装：模板 + `_D5_READER="latin"`，与模板 0 行差。重建 venv，TOTAL 150，0 警告。印 PDF 43,751,757 B sha256 `8672ef924611…`；网 PDF 3,952,529 B sha256 `105856e3608c…`。
- 门禁：census PASS；quotes 0；head_check PASS；occlusion 0；p8 150/150 compare CLEAN（keydiff=[137,138]）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox 绝对缺陷 0（n=396 median 1.007，P8 218→217 行，余量 60.0→75.5）；textlayer 差 0（23,556=23,556）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0；baseline 7/8——P1 同 core-ko artefact（文本 0 差）。
- P6 creambox "spill" 同 ko-en 误报（盒子随栏下移，行在新盒内；SVG 几何核实），未改内容。KIT 已同步；build 副本已清。
- 注：KIT 原 web PDF SHA（624c1933…）开工前已 stale，在盘 pre-D5 web PDF 为 8e9b6c00…；已在 KIT 注明。

### 2026-w47-ko-fr — DONE 2026-11-12
- 安装：模板 + `_D5_READER="latin"`，与模板 0 行差。重建 venv，TOTAL 150，0 警告。印 PDF 43,750,452 B sha256 `dedad96d3ee2…`；网 PDF 3,951,154 B sha256 `eea62fb6f68e…`。
- 门禁：census PASS；quotes 0；head_check PASS；occlusion 0；p8 150/150 compare CLEAN（keydiff=[137,138]）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox 绝对缺陷 0（n=398 median 1.007，P8 234→217 行，余量 60.0→75.5）；textlayer 差 0（23,641=23,641）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0；baseline 7/8——P1 同 core-ko artefact（文本 0 差）。
- P6 creambox "spill" 同 ko-en 误报（盒子随栏下移，行在新盒内；SVG 几何核实），未改内容。KIT 已同步；build 副本已清。
- 注：KIT 原 web PDF SHA（a5f712d2…）开工前已 stale，在盘 pre-D5 web PDF 为 d69239d3…；已在 KIT 注明。

### 2026-w47-ko-ru — DONE 2026-11-12
- 安装：模板 + `_D5_READER="ru"`，与模板仅差该行。重建 venv，TOTAL 150，0 警告。印 PDF 43,925,173 B sha256 `8bbaf7979737…`；网 PDF 4,123,689 B sha256 `cfec8232a249…`。
- 真缺陷修 1 处：P2 `кимчхи` 掉出固定高 D-day 框底 8.76px——俄语行 `22 ноября — день, когда делятся кимчхи` → `22 ноября — делятся кимчхи`（389.2px→276.0px，2 行→1 行）；韩语原文不动；text.md 用 textmd.py 重导出（仅该行变）。修后 spill 0，P2 143→142 行。
- 试点 P6 "掉框" 重裁定为工具误报：creambox spill 检查拿 patched 行 y 对 BASELINE 盒底，盒子本身随栏下移 +73px（底 502.9→575.95），行在新盒内有余量，渲染裁图证实；未改内容。试点 2 处 TEXTX 亦为已知误报，修后 occlusion 0 flags。
- 门禁：census PASS（Noto Sans 元素 1108）；quotes 0；head_check PASS；occlusion 0；p8 150/150 compare CLEAN（keydiff=[137,138]）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox 绝对缺陷 0（n=404 median 0.998，P8 236→244 行，余量 60.0→60.0）；textlayer 差 0（23,451=23,451）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0；baseline 7/8——P1 同 core-ko artefact（文本 0 差，显示数字 "1" 185 vs 183pt）。
- KIT 已同步；build 副本已清。注：KIT 原 web PDF SHA（2d553d30…）开工前已 stale，在盘 pre-D5 web PDF 为 80878c29…；已在 KIT 注明。

### 2026-w47-ko-de — DONE 2026-11-12
- 安装：模板 + `_D5_READER="latin"`，与模板 0 行差。重建 venv，TOTAL 150，0 警告。印 PDF 43,753,274 B sha256 `01c8a283684b…`；网 PDF 3,953,949 B sha256 `b0ee1af9d6ed…`。
- 门禁：census PASS；quotes 0；head_check PASS；occlusion 0；p8 150/150 compare CLEAN（keydiff=[137,138]）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox 绝对缺陷 0（n=402 median 1.009，P8 231→215 行，余量 60.0→61.0）；textlayer 差 0（23,803=23,803）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0；baseline 7/8——P1 同 core-ko artefact（文本 0 差）。
- P6 creambox "spill" 同 ko-en 误报（盒子随栏下移，行在新盒内；SVG 几何核实），未改内容。KIT 已同步；build 副本已清。
- 注：KIT 原 web PDF SHA（0b309527…）开工前已 stale，在盘 pre-D5 web PDF 为 a2ad1d6d…；已在 KIT 注明。

### 2026-w47-ko-it — DONE 2026-11-12
- 安装：模板 + `_D5_READER="latin"`，与模板 0 行差。重建 venv，TOTAL 150，0 警告。印 PDF 43,745,554 B sha256 `3a83150347fb…`；网 PDF 3,945,989 B sha256 `58e4b864e4f1…`。
- 门禁：census PASS；quotes 0；head_check PASS；occlusion 0；p8 150/150 compare CLEAN（keydiff=[137,138]）；spill 0；boxtitle 0 DEFECT（73 titles）；edge 0/0；creambox 绝对缺陷 0（n=398 median 1.009，P8 243→217 行，余量 60.0→76.5）；textlayer 差 0（23,615=23,615）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0；baseline 7/8——P1 同 core-ko artefact（文本 0 差）。
- P6 creambox "spill" 同 ko-en 误报（盒子随栏下移，行在新盒内；SVG 几何核实），未改内容。KIT 已同步；build 副本已清。
- 注：KIT 原印/网 PDF SHA 均开工前已 stale（印 54e35033…→在盘 3c48b6f4…；网 f6135c50…→在盘 4d15cd38…）；已在 KIT 注明。

### 2026-w47-ko-pt — DONE 2026-11-12（第二任工人补齐门禁 + KIT 同步）
- 重建（上一任，生产目录原地 venv）：安装模板 + `_D5_READER="latin"`，与模板 0 行差。基线 base-venv TOTAL 150（P2 FLOW OVERFLOW 警告 1 处，core 内容，pre-D5 已有）。重建 venv，TOTAL 150，0 警告。印 PDF 43,752,879 B sha256 `41217c9397cc…`；网 PDF 3,953,672 B sha256 `1a973dc82d43…`（生产 SHA 与 `logs/pdf-patched.sha256` 一致，第二任复核）。
- 门禁：census PASS（生产基线 406 拉丁 → 0/0/0）；quotes 0；head_check PASS；occlusion 0；p8 150/150 compare CLEAN（keydiff=[137,138]）；spill 0（359 OBSERVE）；boxtitle 0 DEFECT（73 titles，964 body lines）；edge 0/0；creambox 1 旗标裁定为工具误报（见下；n=397 median 1.007，P8 218→217 行，余量 75.5→76.5）；textlayer 差 0（23,203=23,203；pdftotext 51,663 字节印/网一致）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0（拉丁 +590）；baseline 7/8——P1 同 core-ko artefact，第二任直接比对生产 P1 SVG 与 freeze 重建 P1 SVG 核实：文本多重集差 0（1113 runs 各），仅大字 "1" 185 vs 183pt + 31 处 x 位移，0 文本内容差。
- P6 creambox "spill" 裁定为工具误报（第二任复核，与 ko-en/ko-es/ko-fr/ko-de/ko-it/ko-ru 同一类）：creambox 拿 patched 行 y 对 BASELINE 盒底，盒子本身随栏下移 +73px（底 502.9→575.95），行 `confirmado · 믿다 = acreditar`（y 528.2）在新盒内（x=989 y=460 h=115.95），SVG 几何 + 渲染裁图（`2026-w47-ko-pt-p6-gloss-crop.png`）证实；spill_sweep 0 SPILL。未改内容。
- KIT 已同步（输出 SHA/尺寸 + D5 节）；build 副本（base/、freeze/）已清，留 pre/、delivered/、logs/、JSON。

### 2026-w47-ko-nl — DONE 2026-11-12（第二任工人补齐门禁 + KIT 同步）
- 重建（上一任，生产目录原地 venv）：安装模板 + `_D5_READER="latin"`，与模板 0 行差。基线 base-venv TOTAL 150（P2 FLOW OVERFLOW 警告 1 处，core 内容，pre-D5 已有）。重建 venv，TOTAL 150，0 警告。印 PDF 43,747,058 B sha256 `770e3c23dce4…`；网 PDF 3,947,564 B sha256 `f0b06c75ca26…`（生产 SHA 与 `logs/pdf-patched.sha256` 一致，第二任复核）。
- 门禁：census PASS（生产基线 408 拉丁 → 0/0/0）；quotes 0；head_check PASS；occlusion 0；p8 150/150 compare CLEAN（keydiff=[137,138]）；spill 0（357 OBSERVE）；boxtitle 0 DEFECT（73 titles，965 body lines）；edge 0/0；creambox 绝对缺陷 0（n=398 median 1.007，P8 245→233 行，余量 73.8→74.8）；textlayer 差 0（23,503=23,503；pdftotext 51,471 字节印/网一致）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0（拉丁 +592）；baseline 7/8——P1 同 core-ko artefact，第二任直接比对核实：文本多重集差 0（1115 runs 各），仅大字 "1" 185 vs 183pt + 31 处 x 位移，0 文本内容差。
- KIT 已同步；build 副本（base/、freeze/）已清。注：KIT 原 web PDF SHA（c4ad9cc6…）开工前已 stale，在盘 pre-D5 web PDF 为 ab4c077d…；已在 KIT 注明。

### 2026-w47-ko-zh-tw — DONE 2026-11-12（第二任工人补齐门禁 + KIT 同步）
- 重建（上一任，生产目录原地 venv）：安装模板 + `_D5_READER="cjk"`，与模板仅差该行。基线 base-venv TOTAL 150（P2 FLOW OVERFLOW 警告 1 处，core 内容，pre-D5 已有）。重建 venv，TOTAL 150，0 警告。印 PDF 45,215,288 B sha256 `17c39f4f4887…`；网 PDF 4,314,413 B sha256 `fe0220266520…`（生产 SHA 与 `logs/pdf-patched.sha256` 一致，第二任复核）。
- 门禁：census PASS（生产基线 210 拉丁 → 0/0/0）；quotes 0；head_check PASS；occlusion 0；p8 150/150 compare CLEAN（keydiff=[138]，预期读者语键）；spill 0（335 OBSERVE）；boxtitle 0 DEFECT（63 titles，1030 body lines）；edge 0/0；creambox 绝对缺陷 0（n=385 median 1.007，P8 206→205 行，余量 78.1→78.1）；textlayer 差 0（18,114=18,114；pdftotext 49,577 字节印/网一致）。
- freeze（syspy 例外）：diff vs base-venv RC=0，新增 CJK 0（拉丁 +450）；baseline 7/8——P1 同 core-ko artefact，第二任直接比对核实：文本多重集差 0（1126 runs 各），仅大字 "1" 185 vs 183pt + 31 处 x 位移，0 文本内容差。
- KIT 已同步（输出 SHA/尺寸 + D5 节；KIT 原 "Freeze baseline blocked" 债务条已标注为已解决）；build 副本（base/、freeze/）已清。注：KIT 原 web PDF SHA（cfe20ece…）开工前已 stale，在盘 pre-D5 web PDF 为 30365149…；已在 KIT 注明。

## 家庭完成状态（10/10，2026-11-12）

- core-ko、ko-en、ko-es、ko-fr、ko-ru、ko-de、ko-it（上一任 DONE，本日志上文）+ ko-pt、ko-nl、ko-zh-tw（本节 DONE）——全部 10 版生产印/网 PDF 均为 D5 重建后版本，全套门禁绿（含已裁定的 P1 freeze artefact 与 P6 误报类），KIT 全部同步。
- 未完成项：无。独立重校（SOP §8.4）由协调员另派。2026-w47-ko-ja 不在任务内，未碰。

### 2026-w47-ko-ja — DONE 2026-11-12（补做单版，ko 家庭漏版；任务清单外）

- 背景：ko 家庭 10/10 报完后协调员盘点发现 ko 目标读者版应为 11 版，ko-ja 不在任务清单、仍是修前版（生产印 PDF 51,357,740 B，2026-11-11 12:01；svglib 无 _D5_READER；KIT 无 D5 节）。本版只做 ko-ja 一版。
- 安装：模板 `mechanism/svglib-ko-d5.py` + `_D5_READER="cjk"`，与模板仅差该行。旧 svglib 存 `svglib.pre-d5`（版内 + `pre/`）。基线：base-venv（旧 svglib + venv）TOTAL 150（P2 FLOW OVERFLOW 警告 1 处，core 内容，pre-D5 已有）；生产交付 SVG 与 base-venv 重建 8/8 均不同——预期内 PIL 漂移（交付建于系统 python3/Pillow 10，venv Pillow 13 量韩文宽 ~1.1%，见 core-ko KIT fix #15），D5 对照以 base-venv 为准。
- 重建：venv，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE（base 的 P2 警告在 D5 重排后消失，无内容改动）。印 PDF 50,274,489 B sha256 `387b3922ce85…`；网 PDF 4,361,673 B sha256 `eddc96d9fe6d…`（生产 SHA 与 `logs/pdf-patched.sha256` 一致，终验复核一致）。
- 门禁：census PASS（生产基线 210 拉丁 → 0/0/0；弯引号 0）；quotes 0；head_check PASS 0 defects；occlusion 0 flags（自检 6 类全触发）；p8 150/150 compare CLEAN（keydiff=[137,138]，预期读者语键）；spill 0（49 boxes，348 OBSERVE）；boxtitle 0 DEFECT（63 titles，1089 body lines，真实 backup）；edge 0/0；creambox 绝对缺陷 0（n=390 median 1.006，boldT 1.040，boldF 1.000；P8 206→205 行，余量 78.1→78.1）；textlayer 差 0（19,284=19,284；pdftotext 53,150 字节印/网一致）。
- freeze（syspy 例外，协调员已批）：diff vs base-venv RC=0，新增 CJK 0（拉丁 +447，run 拆分所致，预期内）；baseline 7/8——P1 同 core-ko artefact（直接比对：文本多重集差 0，1128 runs 各；仅大字 "1" 185 vs 183pt + 31 处 x 位移，0 文本内容差），已裁定非缺陷。
- 内容缺陷：0 处（无一标题/框体需修；ko-zh-tw 同款 cjk 流程，本版零新增缺陷）。text.md 未动（SHA `635ec8af…` 与修前一致）。KIT 已同步（输出 SHA/尺寸 + D5 节；KIT 原 web PDF SHA `9f0567aa…` 开工前已 stale，在盘 pre-D5 web PDF 为 `7c84456b…`，已注明；"Freeze baseline blocked" 债务条已标注为已解决）。
- build 副本（base/、freeze/）已清，留 pre/、delivered/、logs/、JSON。收尾时 df 93G 已用（门限 100G，未触发）。
- 未完成项：无。独立重校（SOP §8.4）由协调员另派。ko 家庭至此 11/11 齐。
