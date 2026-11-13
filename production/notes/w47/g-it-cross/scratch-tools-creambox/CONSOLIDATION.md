# creambox 工具收敛记录（W47）

收敛员：scratch-tools-creambox。2026-11-11。只读收敛 + 复制，不改任何版与 repo，不 commit、不 push。

## 探针

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0。
- scratch 真实写文件：`scratch-tools-creambox/tmp/probe.txt` 写入并读回成功。
- 全程 `TMPDIR` 指向 `scratch-tools-creambox/tmp/`，未写 `/tmp`。
- repo `tools/` 核查：`~/workspace/weekly-git/tools/` 下无任何 creambox* 文件（任务背景属实）。

## 清单快照（2026-11-11 10:14 UTC）

`find hidden_files/w47 -name 'creambox*.py'` 共 **37 个文件**。注意：W47 并行生产进行中，快照期间仍有新 scratch 出现——10:10 初查为 24 份 `creambox.py` / 4 份 `creambox_check.py`，10:14 复查新增 `scratch-fix-de-en2/creambox.py`（13 行版第 23 份）与 `scratch-fix-core-zh-tw5/creambox.py`（墨迹盒版第 2 份）。新增份均为已有家族的原样复制，未改变下述结论；表中数量以 10:14 快照为准。

### A 组 — 13 行全版扫描版（md5 `a5dbea586836c950f1fdfb6bdc6569c0`，859 字节，13 行）× 23 份

| 副本位置 | 备注 |
|---|---|
| scratch-proof-de-es1/creambox.py | **最老（2026-11-11 09:20），本家族起源；canonical 来源** |
| scratch-fix-de-en1/creambox.py | |
| scratch-fix-de-en2/creambox.py | 快照期间新增 |
| scratch-fix-de-es1/creambox.py | |
| scratch-fix-de-pt-toolbox/creambox.py | |
| scratch-fix-de-toolbox-family/creambox.py | |
| scratch-fix-de-zh-tw-toolbox/creambox.py | |
| scratch-proof-de-en3/creambox.py | |
| scratch-proof-de-es2/creambox.py | 产出 `creambox-p7.log` / `creambox-all.log`（验证基准） |
| scratch-proof-de-pt3/creambox.py | |
| scratch-proof-de-zh-tw2/creambox.py | |
| scratch-proof-en-fr1/creambox.py | GATE-LOG 记为“引自 scratch-proof-de-es1/ 原样复制” |
| scratch-proof-en-it1/creambox.py | |
| scratch-proof-en-ja1/creambox.py | |
| scratch-proof-en-ko1/creambox.py | |
| scratch-proof-en-nl1/creambox.py | |
| scratch-proof-en-ru1/creambox.py | |
| scratch-proof-es-fr1/creambox.py | |
| scratch-proof-es-it1/creambox.py | |
| scratch-proof-es-ja1/creambox.py | |
| scratch-proof-es-ko1/creambox.py | |
| scratch-proof-es-pt1/creambox.py | |
| scratch-proof-es-ru1/creambox.py | |

行为：`+45px` 全版窗口（基线 `[y-5, bottom+45]`、x `[x-1, x+w+1]`）；输出每盒 `box y / bottom / last baseline / clearance / 末行文字`。无逐行表、无 P7 专项、无 descender 修正、无假阳性标注、无 exit 码。

### B 组 — 墨迹盒版（ink-box，依赖 repo `tools/occlusion_audit.py`）× 2 份

| 副本 | md5 | 行数 | 与另一份的差异 |
|---|---|---|---|
| scratch-reproof-core-zh-tw2/creambox.py | `1c7f245ec9d14bb06738f43f0dc5565c` | 83 | 写 `creambox.json` 到本 scratch |
| scratch-fix-core-zh-tw5/creambox.py | `824111415c7310da111f21d82e3e82f2` | 83 | 仅 `S = Path(...)` 输出路径一行不同（diff 唯一 1 行） |

行为：用真实墨迹盒（非基线）判 STRADDLE / 四边 CLEARANCE（墨迹到盒边）/ CREAM-COVER（后画奶油 rect 盖住先画文字 ≥30%）；P7 盒单列打印 + 每页最小底边清除量；写 JSON。硬编码单一 core 路径（core-zh-tw），无 `+45px` 窗口、无逐行基线清除量、无 argv。口径与 A 组不同（墨迹 vs 基线），不能互换。

### C 组 — en-pt1 等价版 × 2 份（同属 scratch-proof-en-pt1/）

| 副本 | md5 | 行数 | 行为 |
|---|---|---|---|
| creambox.py | `514960b1b027f91a5a0c2c96b833da6f` | 34 | SVG + PNG 双重：(a) 基线在盒底下 `(bottom, bottom+40]` 的文本（> +40 视为下块，排除）；(b) PNG 灰度条 `(bottom, bottom+10]` 内深色像素。硬编码 en-pt 路径，无 argv、无逐行表、无 P7 专项 |
| creambox2.py | `b5010af33842a0520c03bdd4ecce72ad` | 23 | 每盒末行 descender 清除量 `bottom - (末基线 + 0.30 × 字号)` + `DESCENDER CROSSES` 旗标；列出 `(bottom, bottom+45]` 内各行及盒内前一行（供断句判断）。硬编码 en-pt 路径，无 argv、无 P7 专项。**0.30 系数被 canonical 采纳** |

### D 组 — 窄带版 creambox_check.py（md5 `ea1a2ff7ae54d575b6085fc7dec7bc38`，2233 字节，40 行）× 5 份

4 份原件（scratch-fix-de-en1、scratch-fix-de-en2、scratch-proof-de-en3、scratch-proof-en-fr1）+ 1 份本次抄入 `tools/` 的副本，md5 全同。

行为：0–8px 窄带——盒内清除量（严格盒内末基线）+ 基线落在 `(bottom, bottom+8]` 即 OVERFLOW，exit 1，否则 `NO OVERFLOW` exit 0。文件头已自述假阳性机制：+45px 窗口会把下块标题（P1 `DAS WORT DER WOCHE` 在盒底下 24px）与 P7 练习题号（35px 下）误报为溢出——窄带即为绕开该问题而设，但代价是漏整行漫出（见验证）。

### E 组 — 诊断版 creambox_diag.py × 4 份

| md5 | 行数 | 副本 |
|---|---|---|
| `e7a9556b13dd931e8557c63883944e8f` | 18 | scratch-proof-es-fr1、scratch-proof-es-pt1 |
| `daefec0bed9f993c1889580636a07918` | 17 | scratch-proof-es-ja1、scratch-proof-es-ko1 |

行为：只列盒底附近（`[bottom-70, bottom+50]` 或 `[bottom-70, bottom+60]`）各行基线/x/字号/文字，供人工判断该行是否属本盒栏流。诊断用，非扫描；未收入 `tools/`（canonical 的 `BELOW-WINDOW` 行已覆盖其用途）。

## 选定理由

**没有任何一份同时满足“+45px 窗口 + 逐行清除量 + P7 工具盒测量”三项。**

| 候选 | +45px 窗口 | 逐行清除量 | P7 工具盒测量 | 通用（argv） | 结论 |
|---|---|---|---|---|---|
| A 组 13 行版 | ✅ | ❌（仅末行） | ❌ | ✅ | 最接近 + 事实标准 |
| B 组墨迹盒版 | ❌（盒内墨迹 + 跨边） | ❌（每盒四边最小值） | ✅（单列 + 每页最小值） | ❌（硬编码 core-zh-tw） | 口径不同，不可作 canonical |
| C 组 en-pt1 | ⚠️ +40px | ❌ | ❌ | ❌（硬编码 en-pt） | 窗口口径不同 |
| C 组 creambox2 | ✅ | ⚠️（仅末行 desc-clear） | ❌ | ❌（硬编码 en-pt） | 贡献了 0.30 系数 |
| D 组窄带版 | ❌（0–8px） | ❌ | ❌ | ✅ | 漏整行漫出，另存 |

因此取 **A 组（scratch-proof-de-es1/creambox.py，md5 a5dbea…，23 份全同、de-facto 标准、en-fr1 GATE-LOG 注明的复制源头）**为 canonical 底本，补最小缺口，不改算法口径。

### 补了什么（共 3 项，均只加输出行）

1. **inside-only 行**：严格盒内末行（基线 `[y-5, bottom]`）的基线、清除量，另加 `desc-clear = bottom - (末基线 + 0.30 × 字号)`（0.30 系数原样取自 C 组 creambox2.py）。作用：把盒子自有末行与窗内下块文字分开。
2. **逐行表**：盒内每一行（基线升序）的 `clearance = bottom - 基线`，随后列出全部 `BELOW-WINDOW` 行（`(bottom, bottom+45]`，带 `+N.N` 超出量）。作用：整行漫出与下块标题假阳性可逐行裁定。
3. **P7-TOOLBOX 测量**：文件名以 `p7-` 开头时，盒子打 `[P7-TOOLBOX]` 标记，文件末出汇总行（盒数、最小盒内清除量、最小 desc-clear）。

未改动的：正则、x `±1`、y `-5`、窗口 `+45`、`last = max(inside)`、原摘要行格式（字节不变）。另加 usage（无参数时 exit 2）与文件头说明。canonical md5：`ee7a55d8b2057cf4ad42a97bb1197383`。

## 交付

- `hidden_files/w47/tools/creambox.py`（canonical，见上）
- `hidden_files/w47/tools/creambox_check.py`（D 组窄带版原样复制，md5 `ea1a2ff7ae54d575b6085fc7dec7bc38` 与 4 份原件全同）
- `hidden_files/w47/tools/creambox-README.md`（用法、字段、假阳性类、与窄带版的区别、适用版本）
- 本文件 `hidden_files/w47/scratch-tools-creambox/CONSOLIDATION.md`
- 验证日志 `hidden_files/w47/scratch-tools-creambox/verification-de-es-p7.log`、`verification-en-fr.log`、`verification-en-fr-check-narrow.log`

## 验证复现值（2026-11-11，当前 repo 状态，只读运行）

### 1. de-es P7（目标值 +19.6）——复现 ✅

命令：`python3 tools/creambox.py production/2026-w47/2026-w47-de-es/svg/p7-sprache.svg`

- 摘要行与 `scratch-proof-de-es2/creambox-p7.log` **逐行一致**（`grep '^  box '` diff 为空），其中：
  - `box y=330 bottom=803.5 last baseline 783.9 clearance +19.6 | 'Es ist fraglich, ob ... = aún dudoso'` —— **+19.6 精确复现**。
- canonical 补行（同盒）：`inside-only [P7-TOOLBOX]: last baseline 783.9 clearance +19.6 desc-clear +13.5`（字号 20.5，0.30×20.5=6.15；19.6−6.15≈+13.5）。
- 三处旧假阳性盒现已自证清白：y=633 两盒与 y=596 一盒的摘要行仍为 `-35.0`（`'101.'`/`'105.'`/`'109.'`），但 inside-only 行均为 **+47.4**（desc-clear +41.1），BELOW-WINDOW 行显示 `'A2'/'B1'/'B2' +34.0`、`'Completa' +35.0`、`'101.'/'105.'/'109.' +35.0`——题号与级别标确为盒下注文。
- P7 汇总：`P7-TOOLBOX summary: 6 boxes, min inside clearance +10.4, min desc-clear +4.5`（最小盒为 y=820 读者来信盒，末行 `'tus textos para el VOL.5!'` +10.4 / desc-clear +4.5）。
- 附注：fix-de-es1 的修前日志同盒曾为 `bottom=783.5 / clearance -0.4`；当前 repo 已是修后状态（盒底 803.5），故复现 +19.6 而非 -0.4。

### 2. en-fr 8 页（目标：SEARCHES / DID YOU KNOW 两处溢出须检出）——复现 ✅

命令：`python3 tools/creambox.py production/2026-w47/2026-w47-en-fr/svg/*.svg`

- 摘要行与 `scratch-proof-en-fr1/creambox-all.log` **逐行一致**（diff 为空）。
- D2 检出：`box y=588 bottom=1256.0 last baseline 1274.0 clearance -18.0 | 'Intérêt relatif, pas des volumes exacts.'`；BELOW-WINDOW 行 `+18.0`；inside-only 行 `+16.0`（盒内末行本身未出）。
- D3 检出：`box y=833 bottom=1158.4 last baseline 1171.1 clearance -12.7 | 'November 3.'`；BELOW-WINDOW 行 `+12.7`；inside-only 行 `+17.9`。
- 两处与 PROOF-NOTE.md D2/D3（200 dpi 裁图证实）一致。
- BELOW-WINDOW 全版共 25 行：22 行在 +35.5~+37.0（下块标题/流文，假阳性）、1 行 +24.0（`THE WORD OF THE WEEK`，下块标题，假阳性）、仅 2 行在 +12.7/+18.0（真漫出 D3/D2）——分界干净。
- P7 汇总：`P7-TOOLBOX summary: 7 boxes, min inside clearance +47.7, min desc-clear +41.6`（与 GATE-LOG 记的 P7 盒内间隙 +47.7…+48.5 一致）。

### 3. 窄带版漏检铁证（同批 en-fr 8 页）

命令：`python3 tools/creambox_check.py production/2026-w47/2026-w47-en-fr/svg/*.svg` → 尾行 `NO OVERFLOW`，**exit 0**，而 D2（18.0px）与 D3（12.7px）两处真漫出均在其 8px 带之外。故窄带版不得再作“无溢出”证据（README 已写明）。

## 未做事项

- 未碰 repo `tools/`、未改任何版文件、未 commit、未 push。
- E 组诊断版与 C 组 en-pt1 双版未抄入 `tools/`：其功能已被 canonical 的逐行表 / BELOW-WINDOW 行覆盖；B 组墨迹盒版口径不同（墨迹 vs 基线），留待其作者决定是否另行收敛。
- 原各 scratch 副本未动（去留由生产方定）。
