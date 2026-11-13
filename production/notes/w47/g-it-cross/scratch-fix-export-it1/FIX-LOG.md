# FIX-LOG — 2026-W47 it 家庭 export_it「翻譯」标签机制修复（fix-export-it1）

**修理工**：fix-export-it1（只修 fan-out 机制，不碰版文件、不碰 core-it、不碰 PDF、不 commit、不 push）
**日期**：2026-11-11
**工作目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-export-it1/`
**机制目录**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-it/`
（注意：机制在 goals 侧；仓库侧 `~/workspace/weekly-git/hidden_files/w47/` 下没有 `scratch-fanout-it/`，W47 实际的出口商是 W46 的 `production/2026-w46/core-it/finish/export_it_textmd.py`，由 `build_edition.py` 导入复用。）

## 0. 探针（开工前）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → rc=0（`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）
- scratch 写入正常（`probe.txt`）
- 全程 `TMPDIR=<scratch>/tmp`，未写系统 /tmp

## 1. 根因（已验证的三环节链条，与 it-es fix1 的 FIX-LOG 一致）

1. **源头**：core-it `content8.py:69–76`，E 节 4 道题 `f.ex()` 的 type 与 instr 均为中文「翻譯」。
2. **放行**：`scratch-fanout-it/translations.py` 头注释第 6–8 行写明 type「翻譯」deliberately NOT in this table（"W46 precedent: kept as-is"），于是 type 字符串未经翻译进入各版 `content8.py`。
3. **导出**：W46 `export_it_textmd.py:297` 逐字照印 type（`s = f"{self.exn}. [{level} · {typ}] …"`），无本地化步骤。

补充核实（本轮新查）：
- `Flow.ex`（core-it `bslib4.py:196`）**不渲染 typ**：PDF 上只画 level chip、题号、instr、正文；typ 只进 `REG` 登记 + `run.py:17` 的 by-type 日志。P8 答案循环比对的是 `e_["type"] == "写作"`（各版已本地化为 Escritura 等），与「翻譯」无关。**因此本修复只影响 .text.md，不影响 PDF 版式。**
- it-en 的 text.md 第 969/971/973/975 行已是 `[A2 · Translate]`（自读记录称当时仍是「翻譯」，说明之后有人手改或重导过 text.md；其 content8.py 仍含「翻譯」，未入仓、无 git 历史可查）——本地化标签是已确立的行为。
- 其余 8 版（de/fr/ja/ko/nl/pt/ru/zh-tw）的 text.md 第 969/971/973/975 行仍是 `[A · 翻译]`；zh-tw 版也是简体「翻译」，应为繁体「翻譯」。

## 2. 方案选择

二选一，取 **(i) translations.py 补映射**，弃 (ii) 出口商加本地化步骤：

| | (i) 翻译表补「翻譯」 | (ii) 出口商本地化 |
|---|---|---|
| 改动 | 1 个表条目 + 1 个计数 + 门收紧 | 需给出口商加读者语言参数与映射表 |
| 覆盖 | 10 版全家，一次生效；源头 content8.py 即干净 | 只修 .text.md，content8.py 仍残留中文 |
| 风险 | 计数断言兜底（错了 build 即死） | W46 出口商是已发版周的共享文件，改它越界；且出口商本不知道读者语言 |
| 判定 | ✅ 采纳 | ❌ 放弃：改动更大、覆盖更窄、碰 W46 文件 |

## 3. 改动对照表（共 2 个文件，均在 goals 侧机制目录）

### 3.1 `scratch-fanout-it/translations.py`

| 处 | 改前 | 改后 | 为什么 |
|---|---|---|---|
| 头注释 L6–8 | `Type '翻译' is deliberately NOT in this table (W46 precedent: kept as-is; only its instr is re-aimed per item via full-line replacement)` | `Type '翻译' IS in this table (fix 2026-11-11): the W46 precedent … was overturned by W47 it-en/it-es proof1 — the label must read in the reader's language. Its instr is still re-aimed per item via full-line replacement in build_edition.py; the type itself goes through this table.` | W46 前例已被 proof1 否定；注释必须与行为一致，否则下一轮还会照旧放行 |
| 练习类型区，新增条目（在 `"写作"` 块后，L276–279） | （无） | `"翻译": { "en": "Translate", "de": "Übersetzen", "fr": "Traduire", "es": "Traducir", "pt": "Traduzir", "nl": "Vertalen", "ru": "Переведите", "ja": "翻訳", "ko": "번역하기", "zh-tw": "翻譯" }` | E 节 4 个 type 标签的读者语言映射。取值依据：en "Translate"（it-en 磁盘 text.md 已确立）、es "Traducir"（it-es fix1 手修确立）、其余取与同区 sibling 类型标签一致的词形——de/nl 不定式（"Einsetzen"/"Schreiben" 同式）、fr/pt 不定式（与 instr "Traduire en français"/"Traduzir para português" 同头）、ru 祈使（"Вставьте"/"Дополните предложение" 占多数 + instr "Переведите на русский" 同动词）、ja 名词 "翻訳"（"作文"/"穴埋め" 同式）、ko "번역하기"（"빈칸 채우기"/"쓰기" 同式）、zh-tw 繁体 "翻譯"（任务指定）。表共 239 → 240 条 |

### 3.2 `scratch-fanout-it/build_edition.py`

| 处 | 改前 | 改后 | 为什么 |
|---|---|---|---|
| `consumed` 字典 L186–189 | …`"写作": 1}` | …`"写作": 1, "翻译": 4}` | E 节重定向（full-call re-aim）消耗掉 4 处 `instr="翻译"`，剩下 4 处 type 待表处理；库存 `inv["翻译"]`=8，期望值 = 8−4 = 4，与 "写作": 1 同一模式（其 instr 也被预消耗） |
| 残留 CJK 检查注释 L211、L217 | `(except frozen '翻译' type …)` / `is either a table key or '翻译'` | `(type '翻译' is now a table key, so no exemption: a non-CJK build must have zero CJK left in these files)` / `is a table key` | 豁免已无依据；注释必须与新门一致 |
| 残留 CJK 检查逻辑 L228–232 | `bad = [ln for ln in left if "翻译" not in ln]; if bad: die(...)` + `print("table pass OK; residual CJK only in kept '翻译' type strings")` | `if left: die(f"residual CJK in {fn}: {left[:3]}")` + `print("table pass OK; no residual CJK (type '翻译' localized via table)")` | **收紧为零容忍**：过去含「翻譯」的行会被豁免放行（漏网的静默通过）；修后任何残留 CJK 都会让 build 当场死掉。零 CJK 是可保证的（核实：core 各源文件的全部 CJK 串都是表键；ja/ko/zh-tw 分支本就走另一条"无残留表键"检查，不受影响） |

**未改**：W46 出口商 `export_it_textmd.py`（无须改、且是他周文件）；`validate_edition_textmd.py`、`gates.py`（均不含「翻譯」断言；validator 解析时跳过 `[...]` 标签内容，标签值不影响校验）；`cjk-inventory.json`（库存不变）；各版 `WEEKLY-KIT.md`（任务明确不改）；core-it 全部内容。

### 3.3 机制侧 KIT 记录

`scratch-fanout-it/STATUS.md` 末尾追加一节 "Mechanism fix — type '翻译' localized (2026-11-11, fix-export-it1)"：根因、改动、验证结论、重 fan-out 前置条件、以及已知既存 drift 提示。core-it 的 `WEEKLY-KIT.md` 未碰（任务禁碰 core-it 内容）；各版 KIT 未碰。

## 4. 验证（实跑，harness：`scratch-fix-export-it1/harness.py`，日志 `harness.log`）

harness 两阶段，均只写本 scratch，不写 production、不覆盖任何版文件：

- **Phase 1（机制，源自 core-it，10 语全跑）**：逐字复用 `build_edition.py` 的 E 重定向 + 表处理循环（含 `consumed` 与计数断言）与收紧后的残留检查，对 core-it 的 6 个源文件跑表。结果：**10/10 通过**——每语「翻譯」恰好替换 4 处，标签 4/4 正确，计数断言全绿；非 CJK 语零残留 CJK，ja/ko/zh-tw 零残留表键。
- **Phase 2（导出，源自已提交版源文件，用真实 W46 出口商，control 对照）**：每语两份——control（版源文件原样，type 仍「翻譯」）、fixed（仅 content8.py 的 4 处 type 换为标签；已验证「翻譯」在该版全部源文件中恰好只出现这 4 处，故 fixed 等价于修后机制对该版源文件的净效果）。control 证明基线，fixed 证明修复增量。

### 4.1 验证全表 — Phase 1（10 语 type 标签，content8.py L69/71/73/75）

| 读者语 | 替换处数 | Q137 (A2) | Q138 (B1) | Q139 (B1) | Q140 (B2) | 计数断言 | 残留检查 |
|---|---|---|---|---|---|---|---|
| en | 4 | Translate | Translate | Translate | Translate | 绿 | 零 CJK |
| de | 4 | Übersetzen | Übersetzen | Übersetzen | Übersetzen | 绿 | 零 CJK |
| fr | 4 | Traduire | Traduire | Traduire | Traduire | 绿 | 零 CJK |
| es | 4 | Traducir | Traducir | Traducir | Traducir | 绿 | 零 CJK |
| pt | 4 | Traduzir | Traduzir | Traduzir | Traduzir | 绿 | 零 CJK |
| nl | 4 | Vertalen | Vertalen | Vertalen | Vertalen | 绿 | 零 CJK |
| ru | 4 | Переведите | Переведите | Переведите | Переведите | 绿 | 零 CJK |
| ja | 4 | 翻訳 | 翻訳 | 翻訳 | 翻訳 | 绿 | 零残留表键 |
| ko | 4 | 번역하기 | 번역하기 | 번역하기 | 번역하기 | 绿 | 零残留表键 |
| zh-tw | 4 | 翻譯 | 翻譯 | 翻譯 | 翻譯 | 绿 | 零残留表键 |

### 4.2 验证全表 — Phase 2（重导出 .text.md，es/de/ru）

| 版 | control（未修机制的重导出）vs 已提交 text.md | fixed（修后机制的重导出）vs 已提交 text.md | 结论 |
|---|---|---|---|
| it-es | 56,259 B；仅 4 行不同（969/971/973/975：control「翻譯」vs 已提交 Traducir） | **56,267 B；0 行不同，字节全等**；SHA-256 `ebd13d454e258a29fe414c04fb56ce53214308b84b2befe400a072fd3415cabf`，与 fix1 FIX-LOG 所记新 text.md SHA **完全一致** | 修后机制逐字节复现 fix1 手修结果 |
| it-es vs fix1 前 `.prefixed` | — | 仅 4 行不同（969/971/973/975：fixed Traducir vs 修前「翻譯」） | 交叉验证：相对修前，恰好只改 4 行 |
| it-de | 56,734 B；**0 行不同**（版源文件与 text.md 同步，基线干净） | 56,754 B；仅 4 行不同（969/971/973/975：`[A·Übersetzen]`，其余 0 行） | 抽查通过 |
| it-ru | 67,722 B；**0 行不同**（基线干净） | 67,778 B；仅 4 行不同（969/971/973/975：`[A·Переведите]`，其余 0 行） | 抽查通过 |

独立复核：三份 fixed 重导出全文 grep「翻譯」= **0 命中**；三份 P8 答案区、instr 尾标（`[Traducir al español]` / `[Ins Deutsche übersetzen]` 等）与全部其他行逐行一致。

### 4.3 既存 drift（验证中发现、与本修复无关、已如实记录）

harness 从 core-it 跑出的 content8.py 与已提交的 10 版 content8.py 相比，除 4 处 type 标签外另有 3 行不同（L80–82：`match_set` 的 deficit/copertura/scaglione 释义，10 版相同、core-it 是旧文案）。另有其他 proof 补丁只存在于各版源文件（如 it-es content12 L35 "Domenica 22 novembre"、Q26/27 释义等，core-it 是旧文案）。**含义：core-it 并未同步各版 fan-out 后的 proof 补丁；重 fan-out 会从 core-it 重建，丢掉这些补丁。** 这是重 fan-out 前协调员须另行处理的事项（补丁重打或先合回 core-it），不在本次机制修复 scope 内；本修复对此既无帮助也无损害。Phase 2 特意用"已提交版源文件"而非 core-it 做重导出基线，正是为了把这层 drift 隔离在外。

## 5. 未动清单

- 未 commit、未 push（机制修完由协调员统一审 commit）。
- 未改动 production 下任何版文件（`git status` 核查：`production/2026-w47` 下 0 个 M；全部 M 项都在 `issues/2026-w43` 与 `production/2026-w43`，是他人 pre-existing 的工作，与 fix1 FIX-LOG §7 所述一致）。
- 未改动 core-it 任何内容、未改动 W46 出口商与任何他周文件、未改动各版 KIT、未改动 `cjk-inventory.json`。
- 未跑 `run.py`/`render.py`/`webpdf.py`（验证只需重导出 .text.md；全量重建是重 fan-out 时的事）。
- 未写系统 /tmp（全程 `TMPDIR=<scratch>/tmp`）。

## 6. 工作产物（本 scratch 内）

- `FIX-LOG.md`（本文件）、`MECHANISM-FIX-REPORT.md`（给协调员的简报）
- `harness.py`（验证脚本，两阶段）、`harness.log`（完整实跑日志）
- `harness/<lang>/`（Phase 1：10 语修后 fan-out 源文件）
- `export-src/<lang>/{control,fixed}/`（Phase 2 输入：版源文件副本）
- `export/<lang>/2026-w47-it-<lang>.text.md.{control,fixed}`（Phase 2 输出：重导出的 text.md）
- `probe.txt`（开工探针）
