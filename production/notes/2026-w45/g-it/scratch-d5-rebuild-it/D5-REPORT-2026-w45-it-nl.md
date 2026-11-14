# D5 重建报告 — 2026-w45-it-nl（荷兰语读者版）

W45 it 家 D5-only 重建（SOP §1.1 字体修复：讲解层拉丁/西里尔字母由 Newsreader 改为 Noto Sans CJK）。施工 2026-11-14；**不 commit、不 push**（入仓由独立重校后的 closer 做）。
施工分工：builder v1 完成第 0–5 步、run1 全部门禁、全部字号修复与 run2 前 6 版（zh-cn/de/en/es/fr/ja）；builder v2（接替 v1，v1 被 restart drain 杀死）完成 run2 余下 5 版（ko/nl/pt/ru/zh-tw）、KIT 更新与本报告。
工作日志：`hidden_files/d5-redo/scratch-2026-w45-it/logs/2026-w45-it-nl/`（`GATES-SUMMARY.txt` 为 run2 门禁总表，`run1/GATES-SUMMARY.txt` 为修前总表）。门禁总表复本（D29）：`production/notes/2026-w45/g-it/scratch-d5-rebuild-it/logs/2026-w45-it-nl/GATES-SUMMARY.txt`（与 scratch run2 总表逐字节一致，`cmp` 已验）。

## 一、装机

- Core 落盘（全家共用一次）：`apply_variant.py --patch-core it --week 2026-w45` → `production/2026-w45/core-it/svglib.py` +95/−3 行，`_D5_READER = "latin"`。
- 本版安装：`apply_variant.py --svglib patched/2026-w45-it-nl/svglib.py --target it --reader nl --week 2026-w45`（先 `--check` dry-run，mode=latin 正确）。装后 `_D5_READER = "latin"`。
- 路由单元测试 `test_d5_routing.py`：**FAILURES: 0**；fix2 块保留（5 处）。
- 重建：`run.py` → `render.py` → `webpdf.py` → text.md 由 `hidden_files/style-port-it/export_it.py` 导出（第 0 步已核实：scratch 试跑 vs issues 已发版 BYTE-IDENTICAL，11/11）。

## 二、基线（修前生产版，全部干净才装机）

- `run.py` RC=0，**TOTAL 150**，0 FLOW OVERFLOW / 0 HEAD TOO WIDE。
- 印 PDF 6,600,111 字节（sha256 `5783b8e7f45b…`），与 fanout 原件逐字节一致；网 PDF 630,600 字节。
- 文字层：印 PDF vs 自建网 PDF 字符多重集差 **0**；自建网 PDF vs issues 已发 web PDF 差 **0**。
- 修前普查 `d5_census.py`：D5 违规 **487**（>0，符合装机前提）。
- 基线 P8 口径：noted **150/150**。

## 三、缺陷与修法（run1 → run2）

run1 共 4 项，全部为 D5 字体加宽引起（讲解层粗体在 Noto Sans CJK 下比 Newsreader 宽，框标题右溢；P1 溢出的标题同时造成 occlusion 墨迹重叠）。修法只动字号，**未动任何文字内容**。

| # | 门 | 位置 / 内容 | 实测 | 修法 |
|---|---|---|---|---|
| 1 | 12 boxtitle / 14 creambox | P1 框标题 `IN CIJFERS` | 右溢 +3.2px | `content12.py:49` 框标题 tsize 20→**19** |
| 2 | 12 boxtitle / 14 creambox | P1 `IN QUESTO NUMERO　INHOUD`（`INHOUD` 框） | 右溢 +4.2px | `content12.py:90` 24→**23**pt |
| 3 | 12 boxtitle / 14 creambox | P2 框标题 `EZELSBRUG` | 右溢 +35.0px | `content12.py:181` tsize 20→**18** |
| 4 | 12 boxtitle / 14 creambox | P7 `LA PAROLA　WOORD VAN DE WEEK` | 右溢 +44.5px | `content7.py:84` 23→**20**pt |

P8 变化：243->243 行，距页脚线余量 45.4 → 45.4 px（正，无溢出）。

- 刊头间隙特记：D18 实测 gap **9.4px**（正值，PASS；D18 只以 ≤0 为缺陷，无需修复）。

## 四、门禁（run2，全套 17 门 + D18）

| 门 | 结果 |
|---|---|
| 1 run | RC=0，TOTAL 150，0 FLOW OVERFLOW，0 HEAD TOO WIDE |
| 2 head_check | PASS，0 defects |
| 3 d5 census | PASS：D5 拉丁 0、西里尔 0、花括号 CJK 0 |
| 4 render | RC=0，印 PDF 6,089,380 B（fix1；run2 为 6,089,382 B） |
| 5 webpdf | RC=0，网 PDF 559,703 B（fix1；run2 为 559,705 B；< 7 MB） |
| 6 occlusion | 0 flags（selftest 6 类全触发） |
| 7 p8 extract | noted 150/150 |
| 8 p8 compare | **CLEAN**，keydiff=[137, 138, 139]，missing=[]，extra=[] |
| 9 freeze baseline | 8/8（patched 重建复现自身 SVG） |
| 10 freeze diff vs base | 新增 CJK 字符 **0**（新增拉丁 strings 250（fix1；run2 为 247），run 拆分所致；对照是 base 修前生产版，不是 core） |
| 11 spill | 0 spills |
| 12 boxtitle | 0 defects |
| 13 edge | 0 touches，0 nears |
| 14 creambox | 0 defects；P8 行数 243->243，页脚余量 45.4 px |
| 15 text layer | print=web=issues，字符多重集差 0 |
| 15a text.md | 导出 RC=0，diff = 2 行（E139 提示/答案互换，F2 修复，D33），其余逐字节相同 |
| 16 census_quotes | 0 defective |
| 18 masthead（D18） | slogan–date 间隙 9.4px，PASS（>0） |

**结论：run2 ALL-GREEN；fix1 除 15a 外全绿（见 §六）。**

## 五、新交付物 / KIT

- 印 PDF：`scratch-2026-w45-it/fix/2026-w45-it-nl/The-Lucerna-VOL3.pdf`（fix1 原件）— 6,089,380 字节，sha256 `6eb4fbbef0d898a022f07d53ea427d100ec81b9bd77cc5725ef8b7a1636374db`（文件名 VOL3 为 render.py 既有命名，基线同名，刊头 VOL.2 无误；run2 为 6,089,382 B，`546074620699…`）。
- 网 PDF：`scratch-2026-w45-it/fix/2026-w45-it-nl/2026-w45-it-nl.web.pdf`（fix1 原件）— 559,703 字节，sha256 `4d0e9bdaedfe91eeddc3a894a3acfa2e2ed6d4edbb7395c527ec3acf8e275bda`。网 PDF 跨次运行字节不确定，**closer 须拷 fix 原件，绝不重跑 webpdf**；KIT 记录的 fix SHA 即交付值（run2 为 559,705 B，`72c01b1a3235…`）。
- text.md：`scratch-2026-w45-it/fix/2026-w45-it-nl/2026-w45-it-nl.text.md.new`（fix1 导出）— 54,424 字节，sha256 `971d573c818be184c6326ecf5963b6d1375abe3140221d5b9c5d33511974ebaa`，与 issues 已发版 diff = 2 行（E139 提示/答案互换，F2 修复，D33），其余逐字节相同。
- KIT：`production/2026-w45/2026-w45-it-nl/WEEKLY-KIT.md` 针脚行已更新为上述新值 + 文末 D5 节（§11）。

## 六、F1–F4 修复（fix1，2026-11-14，D33）

- F2：`production/2026-w45/2026-w45-it-nl/content8.py:73–74`，E139 提示/答案互换——key 由意大利语 "Domenica sera si gioca Fiorentina–Juventus." 改为荷兰语 "Op zondagavond speelt Fiorentina tegen Juventus."，body 由荷兰语提示改为意大利语提示 "Domenica sera si gioca Fiorentina–Juventus. → ___"；note（"si gioca = er wordt gespeeld"）与 instr（"Vertaal"）不动。基线核实：已发版 text.md E139 行即为荷兰语提示 → 意大利语答案，先存缺陷、非 D5 回归。改后核对 nl E137–140 方向全部符合设计（137–139 意大利语提示 → 荷兰语答案、140 荷兰语提示 → 意大利语答案）。
- 修复后在 `scratch-2026-w45-it/fix/2026-w45-it-nl/` 全量重建 + 全部门禁重跑（`gates_fix.py`，tag fix1）：TOTAL 150、p8 150/150 CLEAN keydiff=[137, 138, 139]；P8 行数 243->243，页脚余量 45.4px；freeze-diff 新增拉丁 strings 250（run2 为 247）；文字层 print=web=issues 差 0（互换为多重集不变）；刊头间隙 9.4px PASS。
- fix1 门禁 verdict：FAILURES: ['15a-textmd']——仅 15a 一门红，属预期内：text.md 与已发版差恰好为 2 行（E139 练习行 + P8 答案 139 行，均为提示/答案互换），其余逐字节相同。
- 新交付物（fix1 原件，§五已更新，KIT pin 已更新）：印 PDF 6,089,380 B，sha256 `6eb4fbbef0d898a022f07d53ea427d100ec81b9bd77cc5725ef8b7a1636374db`；网 PDF 559,703 B，sha256 `4d0e9bdaedfe91eeddc3a894a3acfa2e2ed6d4edbb7395c527ec3acf8e275bda`；text.md 54,424 B，sha256 `971d573c818be184c6326ecf5963b6d1375abe3140221d5b9c5d33511974ebaa`。门禁总表复本（D29）：`production/notes/2026-w45/g-it/scratch-d5-rebuild-it/logs/2026-w45-it-nl/GATES-SUMMARY.txt` 已换为 fix1 总表。
