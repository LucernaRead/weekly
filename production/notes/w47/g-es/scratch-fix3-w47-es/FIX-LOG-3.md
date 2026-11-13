# FIX-LOG-3 — W47 es 家庭第三轮修复（H1，es-ru 称呼混用，低）

**任务**：修第三轮独立重校 PROOF-NOTE-3.md（2026-11-12，`scratch-reproof3-w47-es/PROOF-NOTE-3.md`）的 H1：es-ru P1 栏目头 `AHORA TÚ　Теперь ты` 用 ты 体，全版其余称呼通篇 вы 体。只修 es-ru 一处，其余 10 版未动；不 commit、不 push、不跑 lint、不改 SOP、不碰其他家庭/其他周。解释器全程 `tools/venv/bin/python`。SOP §8：改源头 → 整版重渲染 → 门禁 → KIT → FIX-LOG。

**磁盘**：开工 95G 已用（150G 盘），门限 100G；收尾 95G 已用 / 55G 空闲，未触发停手。RAM：渲染串行一次通过，无 RC=143/-15 中断，无需重试。

## 改前实测（与 PROOF-NOTE-3 §1 逐一核对，一致）

| 文件 | 字节 | SHA-256（完整） |
|---|---|---|
| 印 `La-Lucerna-VOL4-es-ru.pdf` | 3,213,296 | `0ca1beca6d7498103b7d36fc27c4946cfdc0276606935ad8b80c0ae9c796e32c` |
| 网 `La-Lucerna-VOL4-es-ru-web.pdf` | 1,061,817 | `2febbe24084bff7e022d937e506df8b1866d211a752936a268194623b09997ae` |
| `2026-w47-es-ru.text.md` | 52,347（1888 行） | `8a57918fc0f9baf0de43b0f920f7ff25272b74e90b94a0c60aeea435673db701` |

- text.md L147：`AHORA TÚ　Теперь ты`（全角空格 U+3000 分隔）。
- 词边界独立词 `ты`（Python `re.findall(r'\bты\b')`，逐行核对）：改前恰 1 处，即 L147。其余 `ты` 命中均为 `дебаты`/`debates` 等词内子串。注意：`grep -P '(?<![\p{L}])ты(?![\p{L}])'` 在此环境计得 15，均为假阳性（命中行全是 дебаты 词内串）；以 Python 词边界为准。
- `А вы?` ×4（text.md 与印/网 PDF 文字层一致）；`Теперь вы` 0 处。

## 源头改动（唯一一处）

- 位置：`production/2026-w47/2026-w47-es-ru/content12.py:51`（P1 栏目头，`f.head(...)`；与第二轮 G2 的 es-pt 同一位置、同一改法）。
- 改前：`f.head("AHORA TÚ　Теперь ты", 25)`
- 改后：`f.head("AHORA TÚ　Теперь вы", 25)`
- 定位依据：`Теперь ты` 在源码（`.py`）中全版仅此 1 处（`content12.py:51`）；SVG `svg/p1-portada.svg` 中同串为生成物，非源头。
- 改后源码 grep `Теперь ты` 0 命中；`Теперь вы` 恰 1 处。

## 重建记录（逐项验 rc 与 SHA；无 set -e 脚本，总返回码 0 不作证据）

| 步骤 | 命令 | 返回码 | 结果 |
|---|---|---|---|
| run | `tools/venv/bin/python run.py`（日志 `run-es-ru.log`） | rc=0 | TOTAL 150，ALL DONE；`svg/p1-portada.svg` 含 `Теперь вы` ×1、`Теперь ты` 0；8 个 SVG 19:00 全新写入 |
| render | `tools/venv/bin/python render.py`（日志 `render-es-ru.log`） | rc=0，一次通过，无中断 | 印 3,213,297 B（19:01:53 UTC）、网 1,061,847 B（19:02:51 UTC）；各 8 页 |

- 印/网 SHA 均为重建后盘上实时值（见下「改后 SHA」），非抄旧报告；网 PDF SHA 每次重建会变，已以实时值为准。
- 改后 SHA 复核（写日志前再次 `sha256sum`，与渲染后即时值一致，无漂移）。

## text.md 更新（手术替换，非整版重导出——有实测依据）

- 干跑：D5 导出器 `scratch-text-reexport-es/extract_text2_d5.py` 干跑到本目录 `text-dryrun.md`（rc=0），1866 行 vs 已装 1888 行，`diff` 200 行——全是重分段（行断点移动）+ 首行 slug 误标（与 FIX-LOG-2 三版实测同一陷阱）；意改在干跑 L138 在场（`AHORA TÚ　Теперь вы`）。
- 结论：整版落盘会引入约 200 行非意改，违反“不要改任何别的词”；故沿用 FIX-LOG-2 的手术式替换：先断言 L147 原文 `AHORA TÚ　Теперь ты` 再替换为 `AHORA TÚ　Теперь вы`，落盘。
- 落盘后 diff（vs `text-pre.md`）：恰 1 行，`147c147`，无一非意改行；行数 1888 不变，字节 52,347 不变（ты→вы 同为 4 字节）。

## 改后 SHA（2026-11-12 19:03 UTC，盘上实测）

| 文件 | 字节 | SHA-256（完整） | 变化 |
|---|---|---|---|
| 印 `La-Lucerna-VOL4-es-ru.pdf` | 3,213,297 | `538ca756749a2bd57760b6bf9c5cc370aefeef11f4ba1e9f409073ba60a33d2d` | +1 B（PDF 元数据/时间戳差；文字层仅一词之变） |
| 网 `La-Lucerna-VOL4-es-ru-web.pdf` | 1,061,847 | `8d440e9b52cf9a157755ec223b5cd160b86d8a7a62a5ff3eca1ac9f8aac61a3d` | +30 B |
| `2026-w47-es-ru.text.md` | 52,347（1888 行） | `ee9b53f788c85e8b28dd87ae99066552c04807bf8a6f04aa5124e582f1faa5b4` | 0 B，仅 L147 一词 |

印/网各 8 页；印/网 pdftotext 53,420 字节逐字节一致（与改前字节数相同）。

## 核对（修后，全部通过）

- text.md：词边界 `\bты\b` 0 处；`Теперь ты` 0；`Теперь вы` 恰 1 处（L147）；`А вы?` 仍 ×4；U+201C/U+201D 各 0 次。
- 印/网 PDF 文字层（pdftotext）：`Теперь вы` 各 1 处、`Теперь ты` 0、`А вы?` 各 4 处。注：PyMuPDF 抽取将全角空格省去，P1 呈 `AHORA TÚТеперьвы`（`Теперь` ×1、`Теперьты` 0），与 pdftotext 结论一致，仅为空格抽取差异。
- SVG：`Теперь вы` ×1、`Теперь ты` 0。

## 门禁（`gates3.sh`，`gates-all.log`，GATES DONE 19:04:30 UTC，全部 rc=0）

说明：任务书列的 `gates.py` 为 `tools/gates.py`，其内硬编码 core-nl / nl slug，不适用于 es-ru；本轮沿用 es 家三轮重校同一门禁集（reproof-3 `gates_all3.sh` 逻辑，单版）：freeze、occlusion、p8 抽取/比对、boxtitle、spill、edge、D5 census。

| 门 | 结果 | rc |
|---|---|---|
| freeze baseline | 8/8 SVGs byte-identical（repointed files: none） | 0 |
| occlusion | 0 flags | 0 |
| p8 extract | 150/150（1–150 全有） | 0 |
| p8 compare vs core-es | CLEAN（keydiff=[137, 138]，读者语翻译题应有差异，已裁定） | 0 |
| boxtitle | 30 titles, 372 body lines，0 DEFECT，0 OBSERVE，0 marginal | 0 |
| spill | 0 SPILL（27 盒，72 candidates，72 OBSERVE） | 0 |
| edge | 8 页，0 TOUCH / 0 NEAR（edge JSON 实测；日志行 "1 touch/near-lines" 为汇总行本身含关键词的计数假象，与 PROOF-NOTE-3 §5 同） | 0 |
| D5 census | PASS（弯引号 U+201C/U+201D 全版 0；curly_total=0；noto_sans_elements=768） | 0 |

附加核查：印/网 PDF 各 8 页、均 < 7 MB；P8 答案 1–150 全有。

## KIT 更新

`2026-w47-es-ru/WEEKLY-KIT.md` 末尾追加一节「第三轮独立重校修复 H1（2026-11-12，PROOF-NOTE-3 (b) 返修）」（沿用第一/二轮惯例：历史节保留旧 SHA，新节载盘上实时新 SHA）：改动摘要、重建方式、新印/网/text.md 尺寸与完整 SHA-256、门禁全绿摘要、日志路径。已核对新 SHA 在 KIT 内各出现 1 次，与盘上实测一致。

## 范围核查（只动 es-ru）

- 本轮 19:00–19:04 UTC 内 es 家改动的文件（mtime 核查）：仅 `2026-w47-es-ru/` 内 20 个文件——`content12.py`、8 个 SVG（`run.py` 全量重生成；freeze 8/8 证实重建确定性）、8 个 cards PNG（`render.py` 生成）、印/网 PDF、`2026-w47-es-ru.text.md`；其余 10 版（core-es、es-de、es-en、es-fr、es-it、es-ja、es-ko、es-nl、es-pt、es-zh-tw）无任何文件在此窗口改动。`WEEKLY-KIT.md` 仅追加 H1 一节。
- 未 commit、未 push、未跑 lint、未改 SOP、未碰其他家庭/其他周。`~/workspace/weekly-git/` 的 git status 另有大量他家工人未提交改动，与本轮无关。
- 日志：本目录（`FIX-LOG-3.md`、`gates3.sh`、`gates-all.log`、`run-es-ru.log`、`render-es-ru.log`、`text-pre.md`、`text-dryrun.md`、`text-dryrun.log`、`content12-pre.py` 及各门禁日志/JSON）。
