# FIX-LOG — W47 pt-ja fix1 · D6（P1 顶栏标语主语错误）

- 版：`production/2026-w47/2026-w47-pt-ja/`（读者母语 ja，目标语 pt）
- 核心对照：`production/2026-w47/core-pt/`（fix2，未动）
- 修复员 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-ja1/`
- 工具栈：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3，见 ja-freeze.log）
- 日期：2026-11-11（UTC 17:52–18:07 执行）

## 0. 开工前三 SHA 核对（与任务书一致，全部相符才开工）

| 文件 | SHA-256（开工前） | 大小 |
|---|---|---|
| 印 `A-Lucerna-VOL4.pdf` | `e45f4a9471d59a78e615cfd010679b7aff4dd963f092ab7457f6d8214fda8a08` | 24,991,049 B |
| 网 `A-Lucerna-VOL4-web.pdf` | `ff67441e1c61e58b002b0a9c40711732512d089bde84aeadc57ff774778281e8` | 1,680,796 B |
| 文 `2026-w47-pt-ja.text.md` | `90dcdcca7821049a9af8735653d7059e4a111eeaae6dfebf1ea1467941ec9830` | 37,915 B |

## 1. D6 修法（只加一字「人」，其余一字不动）

缺陷：P1 顶栏标语日语层主语错误。中文源文「读巴西人正在读的葡萄牙语」明确主语为巴西人；
日语「ブラジルが読む」中ブラジル为 が 主语，国家换喻对 読む 有歧义。

| 位置 | 改前 | 改后 |
|---|---|---|
| `tables_ja.py:202` | `"读巴西人正在读的葡萄牙语": "ブラジルが読むポルトガル語"` | `"读巴西人正在读的葡萄牙语": "ブラジル人が読むポルトガル語"` |
| `content12.py:15` | `p.text(975, 92, "TODA SEMANA EM PORTUGUÊS　毎週　ブラジルが読むポルトガル語", 17, "sans", False, GREY, anchor="middle", spacing=1.7)` | `p.text(975, 92, "TODA SEMANA EM PORTUGUÊS　毎週　ブラジル人が読むポルトガル語", 17, "sans", False, GREY, anchor="middle", spacing=1.7)` |

- 全版 grep「ブラジルが読む」（`*.py`/`*.md`/`*.txt`/`*.json`，不含已渲染的 svg/）：修前恰 2 处（上表两处），修后 **0 处**。
- 全版 grep「ブラジル人が読む」：修后恰 2 处（上表两处），无其他出现。
- 机制说明：`content12.py:15` 是已 transform 的渲染源（核心 `core-pt/content12.py:15` 为
  `…每周一期　读巴西人正在读的葡萄牙语`，transform 按 `tables_ja.py` 替换为日语值）；
  两处必须同步改——`content12.py` 决定本次渲染，`tables_ja.py` 是该版的事实源（将来重 transform 的依据）。
- 未动：D1–D5 与 Q65、标语以外的任何文字、其他版、核心。`WEEKLY-KIT.md` 未引用该标语，无需改动。
  `git status`：本版目录此前即为 untracked（未入仓）；本次只改了上述两个源码文件（mtime 17:54）。

## 2. 重建（版目录正常流程，全套）

全部日志重定向均为绝对路径、目标预先核对在 fix1 scratch 内（铁律①）：

1. `tools/venv/bin/python -u run.py` → `ja-run.log`，rc=0（见 GATE-LOG）
2. `tools/venv/bin/python -u render.py` → `ja-render.log`，rc=0，8 cards + print PDF
3. `tools/venv/bin/python -u gates.py` → `ja-gates.log`，16/16 PASS
4. `tools/venv/bin/python <MECH>/textmd.py <core-pt zh-cn text.md> <edition> ja` → `ja-textmd.log`，rc=0
5. `tools/venv/bin/python -u tools/webpdf.py <edition>/svg <edition>/A-Lucerna-VOL4-web.pdf` → `ja-webpdf.log`，rc=0，8 页，48,026 text bytes

（副作用说明：`textmd.py` 按其自身设计把 diff 报告 `ja-textmd-diff.json` 写到了它的
所在目录 `scratch-fanout-pt/`（MECH 共享区），已原样复制一份到本 scratch；
输入（MECH 表 + 核心 text.md）均未变，报告内容与上一轮一致。未改 MECH 的任何源码。）

## 3. 新三 SHA（本次交付为准）

| 文件 | SHA-256（新） | 大小 | 变化 |
|---|---|---|---|
| 印 `A-Lucerna-VOL4.pdf` | `568eb36b19a0d285dfbb9058933659e3dd97afae0d5de535a5b47bb7906b6ea5` | 24,991,052 B | +3 B（「人」UTF-8 恰 3 字节） |
| 网 `A-Lucerna-VOL4-web.pdf` | `7079b9af534836635228e9d5982210dacbecc2257438c9d1d98afbf7761c5444` | 1,680,802 B | +6 B |
| 文 `2026-w47-pt-ja.text.md` | `90dcdcca7821049a9af8735653d7059e4a111eeaae6dfebf1ea1467941ec9830` | 37,915 B | **不变（预期）** |

**text.md 不变的原因（已核对）**：标语行不在 text.md 中。`grep "TODA SEMANA|ブラジル" 2026-w47-pt-ja.text.md`
修前即为 0 行；核心 `core-pt/2026-w47-pt-zh-cn.text.md` 亦不含该标语（grep 0 行），
`textmd.py` 由核心 text.md 派生，故重生成后字节相同（sha 不变，见 §0/§3 同值）。

## 4. SVG 变化清单（只应有 p1 变化）

修前快照 `svg-before.sha256` vs 修后 `svg-after.sha256`：

| SVG | 修前 | 修后 | 变化 |
|---|---|---|---|
| `svg/p1-capa.svg` | `289748dd…` | `fc51c47e6a0bc0d26b05892896369c50aedfe1aa05d972a25cbc01bae8e2474f` | **唯一变化** |
| `svg/p2-vida.svg` | `f5b85a70…` | 相同 | 无 |
| `svg/p3-cultura.svg` | `e70be859…` | 相同 | 无 |
| `svg/p4-esporte.svg` | `c4e8842a…` | 相同 | 无 |
| `svg/p5-jovens.svg` | `70024d94…` | 相同 | 无 |
| `svg/p6-aprofundamento.svg` | `db450c45…` | 相同 | 无 |
| `svg/p7-lingua.svg` | `7ed1338f…` | 相同 | 无 |
| `svg/p8-avaliacao.svg` | `612bfcea…` | 相同 | 无 |

p1 内含「ブラジル」的 `<text>` 元素恰 1 个（修后 `x="663.9" y="92"`，即标语行）；
含旧串「ブラジルが読む」的元素 0 个（`measure_topstrip.py` 实测，见 `ja-topstrip-after.log`）。

## 5. 标语行右缘实测（无碰撞）

方法见本 scratch `measure_topstrip.py`。A）advance 度量（与 re-proof 同口径：SVG 元素 x + `svglib.text_w`，
即字形 advance 之和，不含 letter-spacing）；B）真实渲染墨迹（新 `cards/p1-capa.png` y70–105 带，
灰度 <128 的墨点游程）。

| 度量 | 修前 | 修后 | 日期行 |
|---|---|---|---|
| A) 标语 advance 右缘 | 1208.7（≈ re-proof 称 1209） | **1216.4** | 日期行 x=1459.5（不变），advance 间隙 243.1px |
| B) 标语真实墨迹右缘 | 1276（墨迹 674–1276） | **1285**（墨迹 665–1285） | 日期行墨迹左缘 1461（不变），**墨迹间隙 176px**（修前 185px） |

- 注：re-proof 称「加人后约 1226」是未计重居中的估算（1208.7+17）；实际 anchor=middle 重居中，
  右缘只增 (17+1.7)/2 ≈ 9.35px（advance 1208.7→1216.4，墨迹 1276→1285），比估算更安全。
- 视觉证据：`ja-p1-topstrip.png`（P1 顶栏裁切，2× 放大）——标语居中、左右均有大段空白，
  与日期行无任何接触；`gates.py`「same-baseline ink collisions = 0」亦通过。

## 6. 待协调员注意（非本次范围，未动手）

- MECH 主表 `scratch-fanout-pt/tables_ja.py:202` 仍为旧串「ブラジルが読むポルトガル語」
  （与本次修前版内表完全相同）。本任务范围只限 pt-ja 版目录，故未改。
  **若将来从 MECH 重 fan-out ja 版，D6 会重现**——建议协调员在适当时机同步 MECH 主表。
- 未 commit、未 push（按任务书，协调员统一处理）。

## 7. 结论

**a = 修完自验全过。** D6 两处源码已改、全版无残留、整版重建、SVG 仅 p1 变化、
text.md 预期不变、全部机械门禁通过（逐项实测见 GATE-LOG.md）。
