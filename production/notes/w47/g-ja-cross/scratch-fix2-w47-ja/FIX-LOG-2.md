# W47 ja 家庭第二轮修复记录（FIX-LOG-2）

> **范围声明**：本轮只修 ja 家庭的 **ja-ko、ja-es** 两版。core-ja 及 ja-de、ja-en、ja-fr、ja-it、ja-nl、ja-pt、ja-ru、ja-zh-tw 共 9 版**未动任何文件**——修复后逐版核对指纹，与 PROOF-NOTE-2 §1 的 pre-fix 值逐字节一致（见 §5）。未 commit、未 push、未跑 lint、未改 SOP。
> 磁盘：修复全程 `df` 已用 95G，未触及 100G 停手门限。

来源：第二轮独立重校 `scratch-reproof2-w47-ja/PROOF-NOTE-2.md`（2026-11-12；0 MAJOR/MEDIUM，2 项 low）。方法照第一轮 `scratch-fix-ja/FIX-LOG.md`（讲解层源码改动 → 重导出 text.md → 重渲印/网 PDF → 全部门禁 → 同步生产 → 更新 KIT）。工具解释器一律 `tools/venv/bin/python`。

## §1 逐项修复前后对照

### L1（ja-ko，PROOF-NOTE-2 低项）—— P7 本周金句 gloss 用词不当

- **问题**：見頃（最佳观赏期）误译为 절기（二十四節氣）。
- **位置**：`production/2026-w47/2026-w47-ja-ko/content7.py:120`（text.md L1022）。
- **改前**：`단풍 절기는 교토로 이동하고 있어요.`
- **改后**：`단풍 절정은 교토로 이동하고 있어요.`
- **依据**：同版其余各处均译对（L44 `가장 보기 좋은 시기`；答案 144 `가장 보기 좋은 시기`；答案 94/95/96/69/73 均用 `절정`），故取 `절정`，与同版惯用译法一致。

### L1 追加（协调员追加发现，重校员漏报）—— P8 答案 98 同一误译

- **问题**：同版答案 98 亦用 절기 译見頃。
- **位置**：`production/2026-w47/2026-w47-ja-ko/content56.py:222`（text.md L1299；core-ja L1300：`98. ○ — 红叶见赏期从北向南移动`）。
- **改前**：`98. ○ — 단풍 절기는 북쪽에서 남쪽으로 이동해요`
- **改后**：`98. ○ — 단풍 절정은 북쪽에서 남쪽으로 이동해요`
- **未动**：L188 `二十四節気 24절기`（`content12.py:177`）是正确的節氣用法，绝不动。修复模式带 `단풍` 前缀，物理上碰不到它；修复后核对 text.md 中 `절기` 仅剩 L188 一处。

### L2（ja-es，PROOF-NOTE-2 低项）—— P8 答案 20 勤労感謝の日简写易混淆

- **问题**：`Día de Acción de Gracias` 是美国感恩节通用西语名，易与勤労感謝の日混淆。
- **位置**：`production/2026-w47/2026-w47-ja-es/content12.py:263`（text.md L1233）。
- **改前**：`20. 勤労感謝の日 — Lun. 23 nov.: Día de Acción de Gracias`
- **改后**：`20. 勤労感謝の日 — Lun. 23 nov.: Día de Acción de Gracias por el Trabajo`
- **依据**：同版 L1354 Q132 已用全称 `Día de Acción de Gracias por el Trabajo`，改为全称与之统一；Q132 本身未动。

## §2 重渲记录

| 版 | 完成运行 | 失败运行与原因（均为探针/脚本问题，成片本身无误） |
|---|---|---|
| ja-ko | 第 3 次（2026-11-12T18:50:07Z） | 第 1 次：PDF 文本层检查用绝对零缺失标准误报（见 §6.2）；第 2 次：原始 SVG grep 对 D5 后多词短语无效（见 §6.3） |
| ja-es | 第 5 次（2026-11-12T19:23:57Z） | 第 1 次：旧措辞子串断言对“扩展型”修复不成立（新全称含旧简称作子串）；第 2 次：`sed` 非幂等，短称是其替换结果的前缀，重跑把 `content12.py:263` 写成双倍后缀（见 §6.4，已手工修复并换幂等写法）；第 3 次：SVG 交叉核对按文档顺序拼接，答案 20 换行导致全称不连续（见 §6.3）；第 4 次：PDF 文本计数按行 grep，同一换行问题导致全称少计（见 §6.3） |

每版流程（`scratch-fix2-w47-ja/fix2_edition.sh <slug>`）：备份 pre-fix 快照（`pre-src/` + `pre/fingerprints.txt`）→ 改讲解层源码 → 基线重建 → 补丁重建 → 重导出 text.md（dry-run 到 /tmp 校验，见 §6.1）→ 全部门禁 → 同步生产（印/网 PDF、SVG、卡片、text.md、WEEKLY-KIT.md）→ 清理 scratch 构建副本。

SVG 变化（与 pre-fix 对比）：ja-ko 仅 `p7-kotoba.svg`、`p8-tesuto.svg`；ja-es 仅 `p8-tesuto.svg`。core SVG 完整性：两版 freeze 基线均 8/8 文件哈希与 shipped core 一致。

text.md diff（与 pre-fix 对比）：ja-ko 恰 2 行（L1022、L1299），每行仅改动修复替换；ja-es 恰 1 行（L1233），仅改动修复替换。

## §3 门禁结果（两版全绿）

### ja-ko

| 门禁 | 结果 |
|---|---|
| `p8.py compare`（core-ja 对照，total 150） | CLEAN；keydiff `[137, 138, 139, 140]`（预期读者语翻译题键） |
| P8 答案 1–150 | 全有，无缺口、无重复 |
| 印/网 PDF 页数 | 各 8 页 |
| 印/网提取文本 | multiset 完全一致；pdftotext 逐字节一致（47,947 字节） |
| 补丁 vs 已交付 multiset 差 | +4/−4，`{'은': 2, '정': 2}`——恰为两次修复 |
| P8 最小字号 | 9.975pt（≥9.75pt） |
| U+201C/U+201D 普查 | 0 |
| D5 census | PASS（拉丁/西里尔入 CJK=0，弯引号=0） |
| 弯引号 census | 0 defective |
| 几何遮挡 `occlusion_audit.py` | 0 flags |
| `boxtitle_check.py` | 48 titles，601 body lines，0 DEFECT，0 OBSERVE，0 marginal |
| `spill_sweep.py` | 35 boxes，141 candidates，0 SPILL，141 OBSERVE |
| `pdf_edge_scan.py` | 8 页，0 TOUCH，0 NEAR |
| `d5_creambox_audit.py` | PASS，0 defects |
| `head_check.py` | PASS，0 defects |
| `freeze.py`（与基线对比） | p7 +1/−1 串，p8 +1/−1 串；新增 CJK 字符共 4（`은`×2、`정`×2），新增拉丁串 0 |
| 重导出校验 `verify_reexport.py` | ALL OK（见 §6.1：dry-run 归一化长度 17,140→17,140；787 行碎片逐行原样恢复；PDF 回归 83/83 缺失行，新增缺失 0；补丁 PDF 中新措辞 2 处现、旧措辞 2 处无） |
| 修复后核对 | text.md `절기` 仅 L188；`단풍 절정은` 在 L1022、L1299；PDF 文本 `절정` 2 行、`절기` 0 行、`24절기` 1 行 |

### ja-es

| 门禁 | 结果 |
|---|---|
| `p8.py compare`（core-ja 对照，total 150） | CLEAN；keydiff `[137, 138, 139, 140]`（预期读者语翻译题键） |
| P8 答案 1–150 | 全有，无缺口、无重复 |
| 印/网 PDF 页数 | 各 8 页 |
| 印/网提取文本 | multiset 完全一致；pdftotext 逐字节一致（46,935 字节） |
| 补丁 vs 已交付 multiset 差 | +12/−0（` por el Trabajo` 的 12 个非空白字符） |
| P8 最小字号 | 9.975pt（≥9.75pt） |
| U+201C/U+201D 普查 | 0 |
| D5 census | PASS（拉丁/西里尔入 CJK=0，弯引号=0） |
| 弯引号 census | 0 defective |
| 几何遮挡 `occlusion_audit.py` | 0 flags |
| `boxtitle_check.py` | 37 titles，503 body lines，0 DEFECT，0 OBSERVE，0 marginal |
| `spill_sweep.py` | 35 boxes，82 candidates，0 SPILL，82 OBSERVE |
| `pdf_edge_scan.py` | 8 页，0 TOUCH，0 NEAR |
| `d5_creambox_audit.py` | PASS，0 defects（P8 行数 245→248，页脚余量 62.7→64.2——答案 20 变长换行所致，属预期） |
| `head_check.py` | PASS，0 defects |
| `freeze.py`（与基线对比） | p7 +0/−0 串；p8 +2/−1 串，新增拉丁串 2（答案 20 全称多出的换行片段），新增 CJK 字符 0 |
| 重导出校验 `verify_reexport.py` | ALL OK（dry-run 归一化长度 22,207→22,219，+12 字符恰为修复；589 行碎片逐行原样恢复；PDF 回归 64/64 缺失行，新增缺失 0；补丁 PDF 短语计数 short=2、full=2） |
| 修复后核对 | text.md 全称仅 L1233（答案 20）与 L1354（Q132）两处；裸简称出现 0 次；PDF 文本（去空白计数）每版全称 2、简称 2、裸简称 0 |

## §4 KIT 更新后 SHA 表（盘上实测值）

| 版 | 文件 | 尺寸（字节） | sha256（前 12 位；KIT 内为完整值） |
|---|---|---|---|
| ja-ko | 印 PDF `Lucerna-VOL4-JA-KO.pdf` | 28,141,037 | `b78a3f6d5a39` |
| ja-ko | 网 PDF `Lucerna-VOL4-JA-KO-web.pdf` | 4,552,025 | `bdf5074b3698` |
| ja-ko | text.md `2026-w47-ja-ko.text.md` | 47,722 | `b1736ccf46f8` |
| ja-es | 印 PDF `Lucerna-VOL4-JA-ES.pdf` | 25,814,012 | `b65f033d7c6f` |
| ja-es | 网 PDF `Lucerna-VOL4-JA-ES-web.pdf` | 4,387,650 | `a2a294d10d62` |
| ja-es | text.md `2026-w47-ja-es.text.md` | 46,699 | `014add82a97a` |

两版 KIT 均已更新：§8 头部印/网 PDF 尺寸+SHA 与 Text 字节数（ja-es 顺带修正了第一轮遗留的 §8 头部 Text 字节数旧值 46,682 → 实际 46,684；本轮新值为 46,699 = 46,684 + 15 字符 ` por el Trabajo`）；各新增 “Fix round 2” 小节（§8 内，含修复前后、门禁与 SHA）与 §11 条目。KIT 内 SHA 与盘上实测一致，已逐项核对。

## §5 未动 9 版核实

修复后逐版核对 core-ja、ja-de、ja-en、ja-fr、ja-it、ja-nl、ja-pt、ja-ru、ja-zh-tw 的印/网 PDF 与 text.md 尺寸+SHA-12，与 PROOF-NOTE-2 §1 的 pre-fix 值全部一致，零差异。

注：共享 clone 内另有其他家庭（de-en、it-es、core-it、core-nl 等）的在途修改，那是其他工人的活，本轮未碰；本轮写入仅限 `production/2026-w47/2026-w47-ja-ko/` 与 `production/2026-w47/2026-w47-ja-es/` 两个目录。

## §6 探针教训（本轮新发现，写给下一轮）

### 6.1 Exporter 碎片化比任务书说的更严重

任务书只提“丢标题/丢 `### ` 前缀”。实测：D5 后文本被拆成逐字体 run，朴素的“一 `<text>` 一行”导出器无法复现 text.md——ja-ko dry-run 导出 5,628 行 vs 原 1,356 行（diff 6,401 行），ja-es 3,404 行 vs 1,376 行（diff 3,779 行）。本轮 text.md 均无 `### ` 行，故 creambox 前缀陷阱不适用。采用的流程：dry-run 到 /tmp，以去空白归一化长度证明除修复外一致（ja-ko 17,140→17,140；ja-es 22,207→22,219），再把每一条碎片行逐行从 pre-fix 文件原样恢复，只施加修复替换；最终 text.md diff 必须只含本轮改动（ja-ko 2 行、ja-es 1 行）。`verify_reexport.py` 强制执行以上全部检查。

### 6.2 PDF 文本层检查是回归检查，不是绝对零缺失

严格的全文档子串测试在 pre-fix 版上已有 83 行（ja-ko）/ 64 行（ja-es）“缺失”（pdftotext 把 masthead/双语标题 run 按交错顺序输出）。PROOF-NOTE-2 §3 的“0 缺失”用的是更宽松的方法。`verify_reexport.py` 第 4 步改为：修复后缺失集必须等于修复前缺失集（新增缺失 0），且新修复行现于补丁 PDF；ja-es 这类扩展型修复用短语计数而非子串断言（short 计数必须等于 full 计数 == 2）。

### 6.3 原始 grep / 按行 grep 对 D5 后 SVG 与 PDF 均无效——多词短语必须用拼接计数

- **SVG**：D5 后多词短语被拆成逐词 `<text>` run，原始 grep 永远找不到；答案 20 还跨两行换行（`…por el` / `Trabajo`），文档顺序与全局 (y,x) 排序都会在片段间插入其他栏的行。`svg_text_count.py` 现改为：对拼接后的 `<text>` 内容做**去空白**计数，并在两种线性化下各计一次——文档顺序与分栏顺序（650px x 带，带内按 (y,x) 排序，带间从左到右）——输出 `"<doc-count> <col-count>"`；`fix2_edition.sh` 取第 2 个数（分栏计数）为准。4 组验证全过：ja-es pre-fix 全称 1/1、简称 2/2；ja-es 补丁版全称 2/2、简称 2/2；ja-ko pre-fix `단풍 절정은` 0、`단풍 절기는` 2；ja-ko 修复后 `단풍 절정은` 2、`단풍 절기는` 0、`절기` 1。
- **PDF**：同一换行使按行 `grep -o` 把 ja-es 全称每版计成 1 而非 2（第 4 次失败）。`fix2_edition.sh` 的 PDF 文本计数现改为去空白全文计数（与 `verify_reexport.py` 的短语检查同法），每版全称 2、简称 2。
- 附：`grep -P '\x{201c}'` 在此环境报错（PCRE `\x{}` 过大），`$'\u201c'` 亦不展开；弯引号普查改用字面 `“`/`”`。

### 6.4 ja-es `sed` 非幂等导致双倍后缀（已修复，无残留）

`fix2_edition.sh` 第 2 次运行的 `sed 's/<简称>/<全称>/'` 不是幂等的——简称是其替换结果的前缀，重跑时把已修复的 `content12.py:263` 写成 `…por el Trabajo por el Trabajo`。已手工把生产文件该行恢复为单次全称，并核对与 `pre-src` 的 diff 恰为 1 行（全称出现 1 次、双倍 0 次、裸简称 0 次），其余生产文件与 `pre-src` 零差异。脚本已改用带否定前瞻的 Python 正则（`Día de Acción de Gracias(?! por el Trabajo)`；0 次替换 = 已修复）。ja-ko 的 `sed` 是幂等的（`단풍 절기는` 修复后即消失），不受影响。

## §7 残留问题

无。2 项（+协调员追加 1 处）全部修复；2 版门禁全部通过；2 版 KIT 全部更新；其余 9 版未动；磁盘 95G，未触及门限。

## 附：工作产物

- 本日志：`scratch-fix2-w47-ja/FIX-LOG-2.md`
- 修复脚本与探针：`scratch-fix2-w47-ja/fix2_edition.sh`、`update_kit2.py`、`verify_reexport.py`、`svg_text_count.py`
- 每版日志：`scratch-fix2-w47-ja/ja-ko-fix2.log`、`ja-es-fix2.log` 及各版目录内 `p8-compare.log`、`textlayer.log`、`pdf-text-counts.txt`、`census*.log`、`kit-update.log` 等；pre-fix 快照在各版 `pre-src/` 与 `pre/fingerprints.txt`。
