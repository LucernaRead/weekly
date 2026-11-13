# W47 ja 家庭第三轮修复记录（FIX-LOG-3）

> **范围声明**：本轮只修 ja 家庭的 **ja-es、ja-it** 两版。core-ja 及 ja-de、ja-en、ja-fr、ja-ko、ja-nl、ja-pt、ja-ru、ja-zh-tw 共 9 版**未动任何文件**——修复后逐版核对印/网 PDF 与 text.md 尺寸+SHA-12，与 PROOF-NOTE-3 §1 的 pre-fix 值逐项一致（见 §5）。未 commit、未 push、未跑 lint、未改 SOP。
> 磁盘：修复全程 `df` 已用 95G，未触及 100G 停手门限。两版串行渲染（RAM 紧张，8G 总量、可用 <1G）；render 均一次成功，无需重试。

来源：第三轮独立重校 `scratch-reproof3-w47-ja/PROOF-NOTE-3.md`（2026-11-12；0 MAJOR/MEDIUM，2 项 low）。方法照第二轮 `scratch-fix2-w47-ja/FIX-LOG-2.md`（讲解层源码改动 → 基线重建对照 → 补丁重建 → 重导出 text.md（dry-run + verify/restore）→ 全部门禁 → 同步生产 → 更新 KIT）。工具解释器一律 `tools/venv/bin/python`。本轮脚本：`scratch-fix3-w47-ja/fix3_edition.sh`、`verify_reexport3.py`、`update_kit3.py`、`svg_text_count.py`（由 fix2 版改编，见 §6）。

## §1 逐项修复前后对照

### L3（ja-es，PROOF-NOTE-3 低项）—— P8 答案 60 把休場写成落败

- **问题**：3 場所連続休場（缺席）写成「输掉三场 tournament」。
- **位置**：`production/2026-w47/2026-w47-ja-es/content34.py:216`（text.md L1276）。
- **改前**：`60. B — Hōshōryū vuelve tras tres torneos perdidos`
- **改后**：`60. B — Hōshōryū vuelve tras tres torneos de ausencia`
- **依据**：取任务书建议的 `tras tres torneos de ausencia`，与 pt `três torneios de ausência` / it `tre tornei di assenza` / en `missing three` / de `drei verpassten Turnieren` / fr `trois tournois manqués` 一致。答案字母 B 与数字 3 不变。
- **未动**：同版 Q132 `Día de Acción de Gracias por el Trabajo`（`content8.py:57`，第二轮已修全称）未碰，核对仍为 1 处。

### L4（ja-it，PROOF-NOTE-3 低项）—— P8 答案 132 以美国感恩节专名指日本劳动感谢日

- **问题**：`Festa del ringraziamento` 是意大利语里美国感恩节的专名，与第二轮 L2（ja-es 答案 20）同一类问题。
- **位置**：`production/2026-w47/2026-w47-ja-it/content8.py:57`（text.md L1355）。
- **改前**：`132. A — Lunedì niente scuola: Festa del ringraziamento`
- **改后**：`132. A — Lunedì niente scuola: Festa del ringraziamento per il lavoro`
- **依据**：取任务书建议的直译全称，与同版答案 20（L1231）`23 nov. (lun.): ringraziamento per il lavoro` 体例一致。答案字母 A 不变。
- **未动**：答案 20（`content12.py:263`）未碰，核对仍为 1 处；KIT §11 F1 引用的旧 #132 note（`Lunedì niente scuola: Festa del ringraziamento`）按 F4 的 Fujiryōga 旧引文先例，**原文照录作历史，不改**，Fix round 3 小节已注明。

## §2 重渲记录

| 版 | 完成运行 | 失败运行 |
|---|---|---|
| ja-es | 第 1 次（2026-11-12T19:46:40Z–19:56:06Z） | 无 |
| ja-it | 第 1 次（2026-11-12T19:56:10Z–20:07:43Z） | 无 |

每版流程（`scratch-fix3-w47-ja/fix3_edition.sh <slug>`）：备份 pre-fix 快照（`pre-src/` + `pre/fingerprints.txt`）→ 改讲解层源码（幂等写法）→ 基线重建（pre-fix 对照，8/8 SVG 与已交付版字节一致）→ 补丁重建（`run.py` TOTAL 150，`render.py` RC=0，`webpdf.py` RC=0）→ 重导出 text.md（dry-run 到 /tmp 校验，见 §6.1）→ 全部门禁 → 同步生产（印/网 PDF、SVG、卡片、text.md、WEEKLY-KIT.md）→ 清理 scratch 构建副本。

重建真实性逐项验（rebuild 脚本无 `set -e`，总返回码 0 不作数）：

| 版 | run.py RC / TOTAL | render.py RC | 印 PDF mtime（UTC）/ 尺寸 | 印 PDF SHA（与同步后盘上值一致） |
|---|---|---|---|---|
| ja-es | 0 / TOTAL 150 | 0 | 2026-11-12 19:50 / 25,814,013 字节 | `74066b86992080d5de346594ec437f0686932daa2b68d2acc176925d1933bd53` |
| ja-it | 0 / TOTAL 150 | 0 | 2026-11-12 20:00 / 25,807,665 字节 | `e44a8fcba1ba429a2ad6c463cca8f4e33559d1a65139e46fa27d367f4242cf6c` |

SVG 变化（与 pre-fix 对比）：两版均仅 `p8-tesuto.svg`；其余 7 个 SVG 字节不变。

text.md diff（与 pre-fix 对比）：两版均恰 1 行，仅改动修复替换——ja-es L1276、ja-it L1355。

## §3 门禁结果（两版全绿）

### ja-es

| 门禁 | 结果 |
|---|---|
| `p8.py compare`（core-ja 对照，total 150） | CLEAN；keydiff `[137, 138, 139, 140]`（预期读者语翻译题键） |
| P8 答案 1–150 | 全有，无缺口、无重复 |
| 印/网 PDF 页数 | 各 8 页 |
| 印/网提取文本 | multiset 完全一致；pdftotext 逐字节一致（46,938 字节） |
| 补丁 vs 已交付 multiset 差 | +6/−4——恰为本次替换（`perdidos`→`de ausencia` 去空白净 +2 字符；多重集净差 +6/−4 含字母重叠抵消） |
| P8 最小字号 | 9.975pt（≥9.75pt） |
| U+201C/U+201D 普查 | 0 |
| D5 census | PASS（拉丁/西里尔入 CJK=0，弯引号=0） |
| 弯引号 census | 0 defective |
| 几何遮挡 `occlusion_audit.py` | 0 flags |
| `boxtitle_check.py` | 37 titles，503 body lines，0 DEFECT，0 OBSERVE，0 marginal |
| `spill_sweep.py` | 35 boxes，82 candidates，0 SPILL，82 OBSERVE |
| `pdf_edge_scan.py` | 8 页，0 TOUCH，0 NEAR |
| `d5_creambox_audit.py` | PASS，0 defects（P8 行数 248→248，页脚余量 64.2→64.2） |
| `head_check.py` | PASS，0 defects |
| `freeze.py`（与基线对比） | p7 +0/−0 串；p8 +1/−1 串，新增 CJK 字符 0，新增拉丁串 1 |
| 重导出校验 `verify_reexport3.py` | ALL OK（见 §6.1：dry-run 归一化长度 22,219→22,221，+2 字符恰为修复；590 行碎片逐行原样恢复；PDF 回归 64/64 缺失行，新增缺失 0；补丁 PDF 中新措辞 1 处现、旧措辞 0 处） |
| 修复后核对 | text.md `tres torneos perdidos` 0×、`tres torneos de ausencia` 1×（L1276）；PDF 文本（去空白计数）每版新措辞 1、旧措辞 0 |

### ja-it

| 门禁 | 结果 |
|---|---|
| `p8.py compare`（core-ja 对照，total 150） | CLEAN；keydiff `[137, 138, 139, 140]`（预期读者语翻译题键） |
| P8 答案 1–150 | 全有，无缺口、无重复 |
| 印/网 PDF 页数 | 各 8 页 |
| 印/网提取文本 | multiset 完全一致；pdftotext 逐字节一致（46,936 字节） |
| 补丁 vs 已交付 multiset 差 | +11/−0——恰为扩展 ` per il lavoro`（11 个非空白字符） |
| P8 最小字号 | 9.975pt（≥9.75pt） |
| U+201C/U+201D 普查 | 0 |
| D5 census | PASS（拉丁/西里尔入 CJK=0，弯引号=0） |
| 弯引号 census | 0 defective |
| 几何遮挡 `occlusion_audit.py` | 0 flags |
| `boxtitle_check.py` | 36 titles，502 body lines，0 DEFECT，0 OBSERVE，0 marginal |
| `spill_sweep.py` | 35 boxes，83 candidates，0 SPILL，83 OBSERVE |
| `pdf_edge_scan.py` | 8 页，0 TOUCH，0 NEAR |
| `d5_creambox_audit.py` | PASS，0 defects（P8 行数 242→242，页脚余量 60.0→60.0） |
| `head_check.py` | PASS，0 defects |
| `freeze.py`（与基线对比） | p7 +0/−0 串；p8 +1/−1 串，新增 CJK 字符 0，新增拉丁串 1 |
| 重导出校验 `verify_reexport3.py` | ALL OK（见 §6.1：dry-run 归一化长度 22,414→22,425，+11 字符恰为修复；595 行碎片逐行原样恢复；PDF 回归 65/65 缺失行，新增缺失 0；补丁 PDF 短语计数 short=1、full=1） |
| 修复后核对 | text.md `Festa del ringraziamento` 仅作全称 1×（L1355），裸简称 0；`ringraziamento per il lavoro` 2×（答案 20 L1231 + Q132 L1355）；PDF 文本（去空白计数）每版全称 1、简称 1（均在全称内）、裸简称 0 |

## §4 KIT 更新后 SHA 表（盘上实测值）

| 版 | 文件 | 尺寸（字节） | sha256（前 12 位；KIT 内为完整值） |
|---|---|---|---|
| ja-es | 印 PDF `Lucerna-VOL4-JA-ES.pdf` | 25,814,013 | `74066b869920` |
| ja-es | 网 PDF `Lucerna-VOL4-JA-ES-web.pdf` | 4,387,651 | `43a26e56278f` |
| ja-es | text.md `2026-w47-ja-es.text.md` | 46,702 | `d8e0c3018361` |
| ja-it | 印 PDF `Lucerna-VOL4-JA-IT.pdf` | 25,807,665 | `e44a8fcba1ba` |
| ja-it | 网 PDF `Lucerna-VOL4-JA-IT-web.pdf` | 4,381,291 | `3cb1e9559b3a` |
| ja-it | text.md `2026-w47-ja-it.text.md` | 46,692 | `91224d88a55d` |

两版 KIT 均已更新：§8 头部印/网 PDF 尺寸+SHA 与 Text 字节数（盘上实时值；网 PDF SHA 每次重建会变，以本次实时值为准）；各新增 “Fix round 3” 小节（§8 内，含修复前后、门禁与 SHA）与 §11 条目。KIT 内 SHA 与盘上实测逐项核对一致。ja-it KIT §1 未动（不含被修字符串）；§11 F1 的旧 #132 引文按历史原文保留（见 §1 L4）。

## §5 未动 9 版核实

修复后逐版核对 core-ja、ja-de、ja-en、ja-fr、ja-ko、ja-nl、ja-pt、ja-ru、ja-zh-tw 的印/网 PDF 与 text.md 尺寸+SHA-12，与 PROOF-NOTE-3 §1 的 pre-fix 值全部一致，零差异（核对时按 web/印/text 顺序：core-ja `0f9098ff3bf0`/`0ce5e4b872ae`/`55c570f1bd0e`；ja-de `c24dfb09d7d0`/`4283e8a74ff9`/`0d8d1de78a06`；ja-en `0560f0e4ea85`/`c6a15edb8a6c`/`fb5a4700d3c9`；ja-fr `ef073db3df37`/`9d4c6114fb31`/`badb0a6e7d00`；ja-ko `bdf5074b3698`/`b78a3f6d5a39`/`b1736ccf46f8`；ja-nl `97ee26ba1616`/`d6f14754f22c`/`7f8f6638e635`；ja-pt `a573debf0755`/`3cca426dcbec`/`9c9609378189`；ja-ru `0726eda64903`/`04b2f315e267`/`f934bcf1d9f4`；ja-zh-tw `649ac196e81a`/`4b09db1088b8`/`77fb0f36c75b`）。

另核对生产源码 diff：与各版 `pre-src/` 快照比对，除被修的 1 个 content 文件外无任何 .py 差异——ja-es 仅 `content34.py:216` 一行，ja-it 仅 `content8.py:57` 一行。

注：共享 clone 内另有其他家庭的在途修改，那是其他工人的活，本轮未碰；本轮写入仅限 `production/2026-w47/2026-w47-ja-es/` 与 `production/2026-w47/2026-w47-ja-it/` 两个目录。

## §6 探针教训（本轮新发现，写给下一轮）

### 6.1 Exporter 碎片化如前两轮，流程复用有效

D5 后朴素导出器仍无法复现 text.md：ja-es dry-run 3,404 行（原 1,376 行，diff 3,783 行）、ja-it 3,401 行（原 1,378 行，diff 3,790 行）。沿用 fix2 流程（dry-run 到 /tmp → 去空白归一化比对只含修复 → 碎片行逐行原样恢复 → `verify_reexport3.py` 全检）一次通过，两版均无重跑。ja-es 为替换型修复（新旧措辞无包含关系，PDF 检查用“旧行不在场”）；ja-it 为扩展型修复（新全称含旧简称作子串，PDF 检查改用 short==full 计数，与 fix2 的 ja-es L2 同法）。

### 6.2 两处编辑均已幂等

- ja-es 用 Python `str.replace`（新串不含旧串，重跑即 0 次替换）。
- ja-it 用带否定前瞻的 Python 正则（`Festa del ringraziamento(?! per il lavoro)`，已修复时 0 次替换）——复用 fix2 的 L2 教训，不再用 plain sed。
- 两版均一次跑通，无失败运行；基线重建 8/8 SVG 字节一致，证明重建链本身稳定。

### 6.3 数字自洽备忘（供重校员复核）

- ja-es：text.md 46,699 → 46,702（+3 字节：`perdidos` 8 字符 → `de ausencia` 11 字符）；去空白归一化 +2（`trestorneosperdidos` 19 → `trestorneosdeausencia` 21）；PDF 多重集 +6/−4（字母重叠抵消后净 +2）。
- ja-it：text.md 46,678 → 46,692（+14 字节：` per il lavoro` 含 3 空格）；去空白归一化 +11（`perillavoro`）；PDF 多重集 +11/−0；网 PDF 4,381,297 → 4,381,291（压缩后反而 −6 字节，SHA 照常更新，以实时值为准）。

## §7 残留问题

无。2 项 low 全部修复；2 版门禁全部通过；2 版 KIT 全部更新；其余 9 版未动；磁盘 95G，未触及门限。按 SOP §8，修复后是否再走一轮全量重校，由父线裁定。

## 附：工作产物

- 本日志：`scratch-fix3-w47-ja/FIX-LOG-3.md`
- 修复脚本与探针：`scratch-fix3-w47-ja/fix3_edition.sh`、`update_kit3.py`、`verify_reexport3.py`、`svg_text_count.py`
- 每版日志：`scratch-fix3-w47-ja/ja-es-fix3.log`、`ja-it-fix3.log` 及各版目录内 `p8-compare.log`、`textlayer.log`、`pdf-text-counts.txt`、`census*.log`、`kit-update.log` 等；pre-fix 快照在各版 `pre-src/` 与 `pre/fingerprints.txt`。
