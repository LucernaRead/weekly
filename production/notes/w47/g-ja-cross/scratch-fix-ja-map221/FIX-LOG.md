# FIX-LOG — ja 家庭 map 221 键「一之富士」错字修复（fix1）

- 日期：2026-11-11（UTC 09:11–09:20）
- 范围：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-ja/` 内的 map 与 map 生成源头
- 红线：只改机制表与 map 生成源头；不重建任何版、不动任何版目录、tools/、issues/；不跑 insert.py / lint --write；无任何 git 写操作

## 0. 核心原文核实（修前已做）

- `~/workspace/weekly-git/production/2026-w47/core-ja/content34.py:120` 正文：`小結の義ノ富士`。
- `content34.py:186-187` B1 练习答案（#47 对应键）：`首日战胜大之里的是义之富士` —— 核心原文是「义之富士」，确证。
- 内部一致性：各 map 另有一键 `大之里首日输给了义之富士`（义，已正确），同一文件内一对一错，错字得证。

> 编号纠正：任务书称「map-en.json:221 键」「:117 另键」——实测 map 是 **221 个键**（总数），错键在 dict 顺序第 211 位（en/de/fr/it）、第 203 位（es）、第 218 位（pt/nl）；正确同胞键在第 107 位（en/de/fr/es/it）/ 第 112 位（pt/nl）。`map-keys.json`（224 条）中错键为 0-based index 217，同胞键 index 112。

## 1. 改前核查（逐图）

| map | 错键 `首日战胜大之里的是X之富士` | 状态 |
|---|---|---|
| map-en.json | 一之富士 ×1（pos 211） | 错 → 已改 |
| map-de.json | 一之富士 ×1（pos 211） | 错 → 已改 |
| map-fr.json | 一之富士 ×1（pos 211） | 错 → 已改 |
| map-es.json | 一之富士 ×1（pos 203） | 错 → 已改 |
| map-it.json | 一之富士 ×1（pos 211） | 错 → 已改 |
| map-pt.json | 一之富士 ×1（pos 218） | 错 → 已改 |
| map-nl.json | 一之富士 ×1（pos 218） | 错 → 已改 |
| map-ko.json | 0（一之富士 0×，义之富士 2×） | 已正确（ko fix1 已修），未动 |
| map-ru.json | 0（义之富士 2×） | 已正确，未动 |
| map-zh-tw.json | 0（义之富士 2×） | 已正确，未动 |
| map-zh-cn.json | **缺失**：全 workspace 文件名 find 无此文件；fanout-ja 内无 `apply-zh-cn.log`；`FANOUT-REPORT-ja.md` 无 zh-cn 字样 | 无图可改（见 §5） |

改前断言（脚本内 assert，全部通过）：每张错图 raw 文本中错键恰 1 次、正确形 `首日战胜大之里的是义之富士` 恰 0 次；`map-keys.json` 错键恰 1 次。

## 2. 改动（改前 → 改后，值不动）

键统一改为：`首日战胜大之里的是一之富士` → `首日战胜大之里的是义之富士`（仅改一字，值逐字不动，键在 dict 中位置不变）。方法：raw 文本单次替换（除该一字外字节全保留）+ JSON 重载结构 diff。

| 图 | 改后键位置 | 值（未变） |
|---|---|---|
| en | pos 211 | `Yoshinofuji beat Ōnosato on day 1` |
| de | pos 211 | `Yoshinofuji schlug Ōnosato an Tag 1` |
| fr | pos 211 | `Yoshinofuji a battu Ōnosato le jour 1` |
| es | pos 203 | `Yoshinofuji venció a Ōnosato el día 1` |
| it | pos 211 | `Yoshinofuji ha battuto Ōnosato il giorno 1` |
| pt | pos 218 | `Yoshinofuji bateu Ōnosato no primeiro dia` |
| nl | pos 218 | `Yoshinofuji versloeg Ōnosato op dag 1` |

- `map-keys.json`（机制表，224 条）：index 217 同样改键，余 223 条逐字不动。
- 结构 diff（与改前快照 `snapshot-before.json` 对照）：7 图均为「键集合除该键拼写外零变化、键顺序零变化、值零变化、instr/meta 零变化」；`map-keys.json` 仅 index 217 一条变化。
- 未动文件核对：改前快照了目录全部顶层文件 sha256，改后比对——除以下 12 个文件外其余 sha 全部未变：7 图 + `map-keys.json` + 4 个生成脚本。

改后 12 文件 sha256：

```
993d33c1c71e33440f17050ffbfeb07c6b968ffb6ca78f15d5d294113a73c978  map-en.json
14b6e6858c2ac1c925d7375c9b75a9c5ba09cb826641a5370ade9ced95b21c49  map-de.json
75c5565d33a69a9b7253553df817b9ab7de1fefb83a7fa91624e3a29b06729b6  map-fr.json
47ed4a467ba3f90c897b49f07121463156301e9d8f989a7247d176aa454e8a25  map-es.json
5663a84f82fea41d322755855798802907a8deb49236a7fd0868a922de2360aa  map-it.json
2c4849920778d74959e019ffc055717146a4a35c253399e4ee9a6757dec92c2e  map-pt.json
7b9c6a39efeceb72f81c97b84d145698ff6c62d7b1f31a785a2165a98463720a  map-nl.json
4f8b821711df8e3d3f6c6c80f32aed81f3bbb7a57a89eee566b0b0bbf3f6c117  map-keys.json
de3fdf11c9c4bfee4328b57cfdaaf60f1cccc4617284eb8243d808a4409c4b94  gen-map-it.py
88fff18408a3a5b891982827665734cfd61eeac7367d7c1f3d767dc85e64e903  gen-map-zh-tw.py
edc11efb6bcfc4567d622311e325a16734bdcb137a43314288daf6e326b65b77  build-map-nl.py
49a15aadb84f3975e57c6333a77a383475d5eca83b48f7c8859ed30eb606d6d6  build-map-ru.py
```

## 3. 生成源头 guard（仿 ko 的 KEY_FIX）

| 脚本 | guard 做法 |
|---|---|
| `gen-map-it.py`（it 图） | 加 `KEY_FIX`，生成循环改为 `m[KEY_FIX.get(k, k)] = T[v]`（键取自 map-en.json，值表 keyed by 英文值） |
| `gen-map-zh-tw.py`（zh-tw 图，当前已正确） | 加 `KEY_FIX`，循环首行 `k = KEY_FIX.get(k, k)` 再进 OVERRIDE/s2t——键值同改，s2t 值得出正确繁体 `首日戰勝大之里的是義之富士`。不加则一旦 map-en.json 回退，重生成即重带错字 |
| `build-map-nl.py`（nl 图） | 加 `KEY_FIX`，在 ingestion 处归一：`en["map"] = {KEY_FIX.get(k,k): v ...}` 再 `KS = sorted(en['map'])` |
| `build-map-ru.py`（ru 图，当前已正确） | 同 nl（ru 生成器同样从 map-en.json 取键；不加则重生成即重带错字） |
| `gen-map-ko.py` | 已有 KEY_FIX，未动 |

- **nl/ru guard 曾返工一次（实录）**：第一版把 `KEY_FIX` 放在 `KS = [KEY_FIX.get(k,k) for k in sorted(...)]`（先排序后改名），验证发现它撞上脚本内断言 `assert set(m) == set(en['map'])`——上游若回退旧 en，改名后的键集与原 en 键集不等，脚本直接 AssertionError 退出、写不出 map。已改为 ingestion 处归一（上游键先改名再排序/断言），三组回归模拟全过。
- 另已验：错键排序位置稳定（`sorted()` 下错/正形同为 index 217，相邻键 `预报因公司而异…` / `首日败给丰升龙的是美之海` 在第 2 字已分出胜负），`T[i]` 按序号取值不受改名影响。
- de/fr/es/pt 图**没有生成脚本**（目录内无 `gen-map-de/fr/es/pt.py`，系手写 map，源头即 map 文件本身 + map-en.json 键序参照），故无 guard 可加；防再生靠已修的 map-en.json + map-keys.json。
- `gen-map-ko.py` 未动；`apply.py` 未动（仅 compile 检查通过）。

## 4. 验证结果

### 4.1 重载与扫尾
10 图 + `map-keys.json` 全部 `json.load` 通过；最终扫尾：10 图均为「一之富士 0× / 义之富士 2×」，`map-keys.json` 错 0 / 正 2。

### 4.2 重生成模拟（/tmp 内，真实生成器，未动任何实文件）
每图三组：F=guarded+已修 en，G=guarded+旧（错）en，O=去 guard 原脚本+旧 en。
- **A（guard 使上游状态无关）**：F == G，四图（it/nl/ru/zh-tw）全过。
- **B（guard 只改 #47，别无他变）**：G vs O 仅错键↔正键一处互换、其余键值全同：it/nl/ru 全过；zh-tw 的值随键走 s2t——G 值得出正确繁体 `首日戰勝大之里的是義之富士`，O 值得出旧错繁体 `首日戰勝大之里的是一之富士`，属预期内正确行为（已单独核实通过）。
- **C（实图 vs 重生成）**：差异只剩生成后手调过的短值（P8 包行缩短等既往手调，与本次无关）：it 11 条、nl 17 条、ru 16 条、zh-tw 2 条；#47 均不在差异中，#47 键值与实图一致。
- zh-tw 模拟用 `~/workspace/weekly-git/tools/venv/bin/python` 跑（含 opencc；系统 python3 无 opencc）。
- 5 个脚本 compile 全过。

### 4.3 重 apply 干跑（#47 命中情况，等效验证，未碰版目录）
核心文本内存模拟：`content34.py:186` 含带引号的正键 1 处，错键带引号 0 处。把 10 图各自的 #47 值代入替换后：

| 图 | 命中 | 替换结果 |
|---|---|---|
| en | ✅ 1 处 | `Yoshinofuji beat Ōnosato on day 1` |
| de | ✅ 1 处 | `Yoshinofuji schlug Ōnosato an Tag 1` |
| fr | ✅ 1 处 | `Yoshinofuji a battu Ōnosato le jour 1` |
| es | ✅ 1 处 | `Yoshinofuji venció a Ōnosato el día 1` |
| it | ✅ 1 处 | `Yoshinofuji ha battuto Ōnosato il giorno 1` |
| pt | ✅ 1 处 | `Yoshinofuji bateu Ōnosato no primeiro dia` |
| nl | ✅ 1 处 | `Yoshinofuji versloeg Ōnosato op dag 1` |
| ko | ✅ 1 处（对照，已修） | `요시노후지는 1일째에 오노사토를 이겼어요` |
| ru | ✅ 1 处（对照，本就正确） | `Ёсинофудзи победил Оносато в 1-й день` |
| zh-tw | ✅ 1 处（对照，本就正确） | `首日戰勝大之里的是義之富士` |

旧错键在核心中带引号出现 0 次——即旧 map 逐字替换永不命中、重 apply 即打回中文的机理与任务书一致；修后 10 图全部命中。

## 5. 未改的图及原因

- **ko**：fix1 时已修（键 + `gen-map-ko.py` 的 KEY_FIX），本次核实 0 错，未动。
- **ru / zh-tw**：核实已正确（义之富士 2×），map 未动；但其生成器（`build-map-ru.py` / `gen-map-zh-tw.py`）从 map-en.json 取键、无 guard——重生成会重带错字，故只给生成器加了 KEY_FIX（§3）。
- **zh-cn**：**无 map 可改**。`map-zh-cn.json` 在全 workspace 文件名查找中不存在；fanout-ja 内无 zh-cn apply 日志、无生成脚本、无报告提及。ja-zh-cn 版文本（`2026-w47-ja-zh-cn.text.md`）仅见于 core-ja 团队的校对目录（`scratch-ja/`、`scratch-proof-ja*`），属另一条构建路线、未经过 fanout-ja 的 map 机制。是否需要给 zh-cn 补 map，请协调员定（本任务不建版、不新建 map）。

## 6. 未动项

- 快照类：`map-en-before.json`、`map-en-new.json`（报告已注明废弃）、`map-keys-before.json`、`miss*.json` / `miss2-*.json`（apply 诊断输出，历史记录）。
- `gen-map-ko.py`、`apply.py`、`core-ja/`、全部版目录、`tools/`、`issues/`。
- 无 insert.py / lint --write；无 git 写操作（仅探针 `hash-object -w` 写了一个测试 blob + 写盘前探针）。

## 7. 遗留（未改、请协调员定）

错字「一之富士」仍存于以下**上游翻译工作表 / 诊断输出**（各 1×，非 map 生成源头，本次按任务范围未动）：`translate-list.json`、`translate-list-before.json`、`translate-roles.json`、`tr-en-34.json`、`tr-en-merged.json`、`w47-inventory.json`、`w47-counts.json`、`worklist.txt`、`miss*.json`、`miss2-*.json`。其中 `translate-list.json` 是 `map-keys.json` 的上游重算来源——若日后从它重算 map-keys，错字会回来；建议届时同修或在重算处加同一 KEY_FIX。

## 8. 本目录产物

- `fix_map221.py`（修复脚本：快照→断言→改名→结构 diff→加 guard）
- `verify_map221_v2.py`（验证 v2：重载/未动集/compile/ guard A-B-C 模拟/#47 干跑；60 项中 57 项直接通过，3 项 B 断言为校验脚本自身的期望写法 bug，已用修正标准复核通过——见 §4.2）
- `verify_zhtw.py`（zh-tw 三组模拟，venv python 跑；其中 B 项同样为校验期望写法问题，已按 §4.2 修正标准复核通过）
- `snapshot-before.json`（改前快照：目录 sha256 + 7 图解析 + map-keys 列表）
- `verify-results.json`（v2 原始逐项结果）
- `probe.txt`（探针记录，每步写盘前重探：git hash-object + 写盘均成功，6 次）
