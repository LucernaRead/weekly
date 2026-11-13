# FIX-LOG — W47 fr-ru fix1 (D1, build fix1)

**任务**：修 proof1（96b9fdf8）结论 (b) 的唯一缺陷 D1。只改 `production/2026-w47/2026-w47-fr-ru/` 这一版，不碰核心与其他版；**不 commit、不 push**（定稿另派独立 re-proof）。
**工作区**：`hidden_files/w47/scratch-fix-fr-ru1/`（新建独占；脚本、日志、渲染件全在此；TMPDIR 指向其内 `tmp/`，全程未写 /tmp）。
**生产零写入**：本次作业的生产目录文件一律未动（开工/收工 SHA 快照逐项比对，见 §5）。修复只做在 scratch 内的构建副本 `build/` 里；新件在 `render/`，由协调员在 re-proof 通过后落地。本日志不改生产 `WEEKLY-KIT.md`，§6 给出待贴入 KIT 的文字。

## 0. 开工核对与探针

- **三 SHA 与 brief 一致**（开工实测）：
  - 印 PDF `La-Lucerna-VOL4-fr-ru.pdf` 17,477,429 B — `c2976921db3531b69adc9d0a37ab8c5fb59dde8678d6892d6d2a9d72de040229`
  - 网 PDF `La-Lucerna-VOL4-fr-ru-web.pdf` 1,760,007 B — `a6d94e5f0d54f78d5cd822040b17bff37c04a7a6852ad25fce5388dcdca9a15a`
  - 文 `2026-w47-fr-ru.text.md` 50,453 B — `a3449fa7e9d90576241371a33fd8f1c25d17a7c723ceee019de9e29d11ccd8f9`
- **探针**：`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4` 成功；scratch 真实写文件成功（`.probe`）。
- **前置阅读**：repo 根 `SOP.md` §1.1、§8.4（+附则一/二）、`AGENTS.md`；`hidden_files/w47/briefs/brief-coordinator.md` **不存在**（`hidden_files/w47/briefs/` 目录无此路径，brief 要点以任务书为准，已记录）。核心对照 `production/2026-w47/core-fr/`（fix4 已定稿）。
- **基线复现（freeze pre）**：`freeze.py baseline --build <版目录> --core-svg <版目录>/svg` → **8/8 逐字节相同**（`freeze-baseline-pre.log`）。本栈（tools/venv，Pillow 13.0.0 / FreeType 2.14.3）精确复现盘上版，可动手。

## 1. 缺陷 D1（修前，双方法复现）

P3「DATES À RETENIR」奶油盒：SVG 实测 rect `x=1439.5 y=1639.6 w=422.5 h=330` → **盒底 1969.6 svg px**（= 1477.2 pt；brief 写的 1970.0 为 dy3=1640 的取整，差 0.4px，下述余量按实测 1969.6 计；结论不变）。
源码 `expl.py:121` `dates3_note`（俄语注折 3 行；核心同注中文 2 行，末基线 1938.9）。

| 方法 | 修前实测 | 结论 |
|---|---|---|
| PIL 真墨（`ink_check.py`，Noto Sans CJK SC 19.5pt，`getbbox(anchor="ls")` 逐行实测墨降部） | 3 行基线 1911.6 / 1938.9 / **1966.2**；末行墨降部 5.00 → **墨底 1971.2**；余量 **−1.6px**（brief −1.2px 是按盒底 1970.0 计，同一墨底） | 越边；盒内全部文本扫描仅此一处越边（见 §4 门 6） |
| 交付 PDF 600dpi 像素（`pdf_pixel_check.py`，fitz 渲染 P3 裁切） | 盒底 1477.20pt；注 x 范围内盒底下暗墨至 **1478.00pt**，越边 **+0.80pt = +1.07 svg px**（brief 区间 1477.92–1478.04pt 内）；盒底下首 5 行暗像素 60/58/39/38/37 | 越边；р/у 下行笔画伸出盒底 |

## 2. 修法（改动最小：缩短注文 1 行）

只改 1 行——scratch 副本 `build/expl.py:121`：

- 旧：`Внимание: нуво выходит в четверг 19-го; праздник начинается уже вечером в среду 18-го.`
- 新：`Нуво выходит в четверг 19-го; праздник — уже вечером в среду 18-го.`

改动说明：删去旗标词 `Внимание:` 与动词 `начинается`，第二分句以破折号承接；两项事实全保留（нуво周四 19 日上市；庆祝周三 18 日晚已开始），与核心注（中文：19 日周四上市，18 日晚已有庆祝活动）事实一致。未选“盒内容上移”：上移只挪基线不减行数，3 行结构仍贴底；缩短到 2 行后末基线与核心同为 1938.9，余量 +25.7px，一步到位且零连带位移。
候选实测（`ink-candidates.log`，同字号/行距/宽 378.5px）：另两候选亦 2 行（`Нуво в продаже с четверга 19-го; …` 与 `Внимание: нуво — в четверг 19-го, …`，同为 +25.7px），取本版因它保留原文动词 `выходит`、改动最贴近原句；仅删 `уже` 的候选仍 3 行（末行 `18-го.` 墨降部 0，余量仅 +3.4px，不足 5px 要求，弃用）。

**重建**（OUT 断言先行：5 个 content 模块的 OUT 全部落在 scratch 内，`build-fix1.log` 首段）：`run.py` rc=0，FLOW OVERFLOW 0，HEAD TOO WIDE 0，TOTAL 150（A2 53 / B1 75 / B2 22；分版 10/15/18/18/17/18/12/42）。
**SVG 差异**（修前盘上 SVG vs 新 SVG）：7/8 逐字节相同，仅 p3 不同；p3 内仅 3 行注文换成 2 行（同 x=1461.5，基线 1911.6 / 1938.9 不变，1966.2 行删除），其余 199 个 `<text>` 元素全同（`svg-diff-summary.txt`）。
**text.md**：同串替换 1 处（第 439 行），其余逐行相同（`render/2026-w47-fr-ru.text.md`）。

## 3. 修后实测（D1 双方法 + 目视）

| 方法 | 修后实测 | 结论 |
|---|---|---|
| PIL 真墨（`ink-after.log`） | 2 行基线 1911.6 / **1938.9**；末行墨降部 5.00 → **墨底 1943.9**；余量 **+25.7px**（要求 ≥5px） | 通过；与核心末基线 1938.9 同值 |
| 交付 PDF 600dpi 像素（`pdf-pixel-post.log`） | 注 x 范围内盒底下 **0 暗像素**；盒内最深暗墨 1457.48pt（= 1943.3 svg px，与 PIL 1943.9 一致，抗锯齿取整差） | 通过 |
| 目视（`crop-p3-dates-fix.png`，300dpi 裁切） | 注 2 行全在奶油盒内，末行下有完整一段盒底留白；其下 `POUR OU CONTRE ?` 位置未动 | 通过 |

## 4. 新件（scratch/render/，待 re-proof 后落地）

- 印 PDF `La-Lucerna-VOL4-fr-ru.pdf` 17,477,392 B — `0f89cf1590a0ee04bdb75baa73c512c5d6f9b7f0671199a1b8935c8cdfae39f2`
- 网 PDF `La-Lucerna-VOL4-fr-ru-web.pdf` 1,759,960 B（<7MB）— `9373b750bc266644cf634f2d65bfc9d9930a9df658486409544775d8e62931e3`
- 文 `2026-w47-fr-ru.text.md` 50,418 B — `9aa919b7c64738b412484c7d491fedb1d314024779e835584ef13b6c48cf978d`
- 渲染卡片 `render/cards/*.png`（8 页，1950×2700）

## 5. 生产零写入核对（收工）

- 版目录快照：开工 47 文件 SHA vs 收工 47 文件 SHA，**逐项相同，零写入**（`snapshot-edition-pre/post.txt`）。
- 核心 `core-fr/`：开工 50 文件 SHA vs 收工，**逐项相同，零写入**（`snapshot-corefr-pre/post.txt`）。
- `git status`：tracked 修改 123 项，收工与开工逐项相同（均为开工前已有的 W43 脏状态，与本次无关）；新增 untracked 仅 `production/2026-w47/2026-w47-nl-it/` 与 `2026-w47-nl-ja/` 两个目录——为作业期间其他并行 agent 所建，非本次。
- 未 commit、未 push；未覆盖任何生产 PDF（生产网 PDF SHA 未动）。

## 6. 待贴入 KIT 的文字（生产 KIT 本次未动，协调员落地时贴）

> fix1（D1）：`expl.py:121 dates3_note` 缩短为 2 行——`Нуво выходит в четверг 19-го; праздник — уже вечером в среду 18-го.`（删 `Внимание:`/`начинается`，事实与核心一致）。P3 注末基线 1966.2→1938.9，PIL 真墨底 1971.2→1943.9，余量 −1.6px→+25.7px；交付 PDF 600dpi 盒底下暗墨 1478.00pt→0。重建 TOTAL 150，7/8 SVG 与修前逐字节相同（仅 p3 注行）。新 SHA：印 `0f89cf15…`（17,477,392 B）、网 `9373b750…`（1,759,960 B）、文 `9aa919b7…`（50,418 B）。16 门全绿（见 GATE-LOG.md）；存活项逐项复测无回退（P7 披露 2233.3/2238.3、Q148 `devant le`、Q130 (989.0, 843.0)、Q36/Q37 +29.7、孤儿 0 新增、p8 CLEAN keydiff [150]、印/网文字层逐字节一致、P8 最小字号 11.625pt）。

## 7. 范围确认与备注

- 只动了 scratch 副本内 `build/expl.py` 1 行 + `render/2026-w47-fr-ru.text.md` 同串 1 行；`tools/`、核心、其他版、SOP 均未动。
- 备注 a：`hidden_files/w47/briefs/brief-coordinator.md` 不存在（目录缺失），本次以任务书为准。
- 备注 b：盒底实测 1969.6 vs brief 1970.0 为 dy3 取整差 0.4px；墨底 1971.2 与 brief 完全一致，结论不受影响。
- 备注 c：盒内文本计数本方法为 380（修前）/379（修后），与 proof1 的 517 口径不同（入盒判定规则不同）；两种口径一致结论：修前唯一越边即 D1，修后 0 越边。
- 备注 d：`keycheck` 149/150，唯一不精确为 Q150（抽取截断，P8 印有全键，见 GATE-LOG 门 10）。
- 遗留文件（本 scratch 内）：见本目录清单；`freeze-pre/`、`freeze-post/` 为 freeze 工具的构建副本，`build/` 为修复构建源，`render/` 为新件。
