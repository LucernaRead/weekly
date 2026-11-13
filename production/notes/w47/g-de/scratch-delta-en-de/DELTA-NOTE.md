# DELTA-NOTE — 2026-W47 en-de Q73 键同步 delta（core-en fix2）

- 版：`2026-w47-en-de`（英语目标语 × 德语读者版），VOL.4，8 版，150 题
- 日期：2026-11-11（UTC 约 14:55–16:05）
- 任务：core-en fix2 把 Q73 键 `speak` → `up`；只在本版内同步该键并重建 + 全部门禁。不碰核心、其他版、tools/。不 commit、不 push（由协调员统一做）。
- 工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-en-de/`（日志、门禁证据、重建副本均在此；未写 repo 侧 hidden_files）
- 解释器：`~/workspace/weekly-git/tools/venv/bin/python`（未用系统 python3）

## 0. 开工探针（通过）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`
- scratch 目录真实写盘成功；`df -h`：`/home/hatch` 可用 64G，无配额问题；`/dev/null` 正常（字符设备）

## 1. 修前身份核对（三件 SHA，实测 = KIT 登记）

| 文件 | 字节 | SHA-256（修前，实测） | 来源 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-de.pdf` | 29,331,212 | `fe02ab1d9ba41e7a22651be02bda3612b66b54f2c521e12ab0ab5ca6797be5e1` | KIT §7 + proof2 PROOF-NOTE（proof2 后 re-fanout #2 重建，proof2 的 `6f82363a…` 已是旧版） |
| `The-Lucerna-VOL4-en-de.web.pdf` | 2,414,462 | `19e166e03f28e813a8418189f20c1ddd31635f6621fbb182268e552c5302e6e5` | 同上 |
| `2026-w47-en-de.text.md` | 52,568 | `0aad0d2c8118bd6dab2f08170425f8ada595b5a397ba0d77511cffdd12c1e5e1` | 同上 |

修前 SVG 8 个 SHA 存 `pre/svg-sha-pre.txt`（快照于 `pre/`，含修前 registry.json、text.md、8 个 SVG 原样备份）。

## 2. 修前三源核对（预期：三源同错 `speak`）

- 核心对照（只读）：`production/2026-w47/core-en/content56.py:49` 已为 `f.ex("A2", "完成句子", "up", "speak up = 大声说出来", …`——核心已修好，未动。
- 本版 `content56.py:49`（修前）：`f.ex("A2", "Satzergänzung", "speak", "speak up = laut sagen", "Speak ___: tell a teacher.", instr="Ergänze")`——键 `speak`，注记与题干与核心同形。
- registry Q73：`{"n": 73, "page": 5, "level": "A2", "type": "Satzergänzung", "key": "speak", "note": "speak up = laut sagen"}`。
- text.md L589：`EXERCISE: Speak ___: tell a teacher.`；L1151：`73. [A2] Satzergänzung — speak (speak up = laut sagen)`。
- P8 印出键（`svg/p8-test.svg`）：`rights (right = Recht) · 73. speak · 74. d · 75. a · 76. b (right = Recht …`。
- 三源同错确认后动手；三者任一不符即停——实际三者全符，继续。

## 3. 唯一改动

- 只改 `content56.py:49`：键 `"speak"` → `"up"`；note（`speak up = laut sagen`）与 stem（`Speak ___: tell a teacher.`）一字不动。未改其他任何源行，未碰 map/翻译文件、ABSTRACT.txt、KIT 以外文件。
- 重导 registry（`dump_reg_new.py`，与 `dump_reg.py` 同逻辑，输出到本 scratch 再装入版内）、重导 text.md（`make_textmd_delta.py`，`make_textmd_w47.py` 的副本，REG_PATH 指新 registry，不碰 fanout 共享区）、重建 `run.py` / `render.py` / `tools/webpdf.py`。

## 4. 修后三件 SHA

| 文件 | 字节 | SHA-256（修后，实测） |
|---|---|---|
| `The-Lucerna-VOL4-en-de.pdf` | 29,331,209 | `ae3b2e371d0dc8344853c106a697d958496dffb0170d3f6cb8599618209f1751` |
| `The-Lucerna-VOL4-en-de.web.pdf` | 2,414,471 | `7117abe47962468fbf93068665f10da4cafaa2116ad368a907971bc9a94fa655` |
| `2026-w47-en-de.text.md` | 52,565 | `c16f0e473f8017605fe8822a6d711134ad55b1708a0f22346ef2b4dd1f01d589` |

- 两 PDF 均为 8 页、1462.5 × 2025 pt（`pdfinfo`）；web PDF 2,414,471 B < 7 MB。
- SVG：仅 `p8-test.svg` 变化（修前 `6b69156023d24b46c193baf697c05719b5319628fca14d65e2b810aa892de5a1` → 修后 `b04d052dd7d4b0eb35702e9766f681e2d6d318642d7da773aa18b14559d6f623`）；其余 7 个 SVG（含 P5，题干不带键）与修前字节一致。**此为正确预期**：Q73 键只出现在 P8 答案区，P5 只印 `Speak ___` 空白与 `speak up` 注记，键本身从不上 P5——p5 不变不是异常（en-es delta 同样证实：p8 含 `73. up`，p5 不变）。

## 5. diff 证据（恰好 1 条 / 恰好 1 行）

registry diff（修前 vs 新导）：
```
583c583
<   "key": "speak",
---
>   "key": "up",
```
registry 仍 150 条；分版 P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；分级 A2 62 / B1 66 / B2 22——与 proof 记录一致。

text.md diff（修前 vs 新导）：
```
1151c1151
< 73. [A2] Satzergänzung — speak (speak up = laut sagen)
---
> 73. [A2] Satzergänzung — up (speak up = laut sagen)
```
52,568 → 52,565 字节（`speak`→`up` 少 3 字节）。

## 6. Q73 四源证据（修后，全为 `up`）

| 源 | 证据 |
|---|---|
| registry | `{"n": 73, "page": 5, "level": "A2", "type": "Satzergänzung", "key": "up", "note": "speak up = laut sagen"}` |
| text.md | L589 题干 `EXERCISE: Speak ___: tell a teacher.`；L1151 答案 `73. [A2] Satzergänzung — up (speak up = laut sagen)` |
| P8 印出键 | `svg/p8-test.svg`：`rights (right = Recht) · 73. up · 74. d · 75. a · 76. b (right = Recht …`；印刷 PDF P8 提取文本含 `73. up` |
| P5 题干 + 注释 | `svg/p5-youth.svg`：题干 `Speak ___: tell a teacher.`；注释框 `Mobbing · to speak up = laut sagen · a …`；印刷/网页 PDF P5 提取文本均含该题干 |

旧键全域扫描：`73. speak` / 旧键 `"speak", "speak up` 在 registry、content56.py、svg/ 中 0 命中（`speak up` 短语本身是正确的注记/正文用词，保留）。

## 7. 150 题键与题干适配抽查（Q73 教训：三源一致不够）

- 方法：`pair_stems.py` 用 recording-stub 直跑 content 文件，逐题配对（键、注记、题干、选项），再人工复核全部填空（Satzergänzung 34）与改写（Umformung 16）共 50 题的键填空合理性。结果文件 `gates/fill-rewrite.log` + `fill-rewrite.json`。
- 50/50 合理，无异常。抽例：Q73 `up` / `Speak ___: tell a teacher.`（speak up 为固定短语动词，正确）；Q70 `silence` / `Break the ___: speak up about bullying.`；Q79 `Children are speaking up this week.` / `Children (speak) up this week.`；Q13 `1` / `December ___`（12 月 1 日）；Q14 `Thursday` / `Thanksgiving is on ___, November 26`（2026-11-26 为周四，proof 已用 `date -d` 核验）；Q107 `win` / `“Democrats ___ the House” is a headline`（复数主语 + 标题现在时）。
- 已知重复：Q2/Q95、Q5/Q96、Q6/Q12 为跨版有意重复（同题干同键，P1→P6 难度复现），proof1 已留档，非缺陷。
- 其余题型（选择/匹配/翻译等）未改动，proof1/proof2 的三源核对 + 本轮 `verify3.py` 0 不一致覆盖。

## 8. D5 字体（只记录数量，不判、不修）

8 个 SVG 的 `<text>` 元素按 font-family 计数：Newsreader 1022 / Noto Sans CJK SC 655 / Noto Serif CJK SC 27 / DejaVu Sans 4 / UnifrakturMaguntia 1；合计 1709。与 proof1 数字完全一致（本次改动不涉及字体）。

## 9. 全部门禁表（全部独立重跑，均通过）

| 门 | 命令 / 依据 | 结果 |
|---|---|---|
| run.py | 版目录内 `tools/venv/bin/python run.py`（`run.log`） | rc=0；OVERFLOW / TOO WIDE 0 次；TOTAL 150；MODEL 82 |
| occlusion | `tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-en-de/svg`（`gates/occlusion.log`，真实审计，未用 --selftest） | 0 flags；selftest OK（6 类 planted 全触发，clean 对照静默） |
| p8 extract | `tools/p8.py extract` core + edition（`gates/p8-extract*.json/log`） | noted set 60/150，两版集合相同 |
| p8 compare | `tools/p8.py compare`（`gates/p8-compare.json` 本体已读） | CLEAN；missing=[]、extra_count=0、uncertain=[]；keydiff=[137, 138, 139, 140, 150]（预期：德语翻译键 + Q150 短标签） |
| keycheck | `keycheck_ed.py de`（`gates/keycheck.log`） | registry-vs-P8 149/150 exact，唯一例外 Q150；registry-vs-core 145/150（差异仅 137–140、150）；Q38–41=[b,a,d,c]；Q125=A；Q46=A；Q52=hosted；Q55=won；Q82/83/84=B/C/A；extract keys 150 条齐全 |
| freeze baseline | `tools/freeze.py baseline --build production/2026-w47/2026-w47-en-de --core-svg production/2026-w47/2026-w47-en-de/svg --out scratch-delta-en-de/freeze-final`（`gates/freeze-baseline.log/json`；--build 为版自己的构建目录，core 对照另用 core-svg 路径的 freeze diff） | **8/8 SVGs byte-identical**（p1–p8 全 OK，含新 p8 `b04d052d…`；shipped SVG 完整性复核通过，运行未改动送审 SVG）。另：瘦复制 `rebuild/` 重跑 + 直接 sha256 比对亦为 8/8 MATCH（交叉验证；build-copy 已清，只留 `freeze-final/svg` 空目录 + 日志/JSON 证据） |
| freeze diff | `tools/freeze.py diff --core-svg …/core-en/svg --edition-svg …/en-de/svg`（`gates/freeze-diff.json/log`）| 8 页逐页对照 core-en（只读）：P1 +32/−34、P2 +42/−54、P3 +25/−23、P4 +24/−22、P5 +24/−22、P6 +25/−21、P7 +64/−55、P8 +99/−99；新增 CJK 合计 9 个，全部 U+3000（与 proof1 逐页一致） |
| 印/网文字层 | `printweb.py`（`gates/printweb.log`）：pdftotext 逐页 | 各 47,403 字符 / 48,638 字节；逐页 byte-identical 8/8（4855 / 5881 / 5395 / 5841 / 4764 / 5674 / 6320 / 9908 B）；token 多重集差 0/0；全文逐字节相同。注：KIT 原登记 47,416 字符是本轮重建第一版的数字（HAYMITCH 标题修复 −10 字符在后）；47,416 − 10 − 3 = 47,403，账对得上 |
| check_s11 | `check_s11.py de`（`gates/check_s11.log`） | ALL §1.1/P8 CHECKS PASS；色集 core 19 = edition 19；徽章色 A2/B1/B2 全在；P8 最小字号 13.5 pt |
| verify_ed | `verify_ed.py de`（`gates/verify.log`） | VERIFY ALL PASS；P8 最小 PDF 字号 10.12 pt ≥ 9.75 pt；SVG 零真实 CJK |
| verify3 | `verify3.py`（`gates/verify3.log/json`） | 三源键 0 不一致（Q150 短标签例外）；孤儿标点 0（SVG 8 页 + 印刷文本行）；D1 回归 fixed（8 条出处行全部 x=538.5，末行 y=2545.12 紧跟金句末行；第 3 栏顶为 THE DRILLS）；fix1 两串新在旧无；金句 8/8 逐字命中；禁词 0；VOL.4 ×12 / VOL.5 ×8 / VOL.3 ×3；徽章逐页与 core 一致（16/15/16/16/16/19/13/23）；U+2019 总数 0；真实 CJK 仅非可见 moth `<title>` 三色蛾；Q38–41 四方一致 |
| boxtitle | `sweep_boxes.py` 源扫 + SVG 扫（`gates/boxtitle-creambox.log`） | 源扫 12/12 fit（最紧 ODD SOCKS +15.2）；SVG 扫 21/21 fit（最紧 P2 `The new Congress meets in January.` +8.8，加粗首行；18 个真标题全部 fit，最紧仍为 ODD SOCKS +15.2） |
| creambox PIL 真墨 | `sweep_boxes.py`（32 盒 × 新 render 的 cards PNG，1:1 坐标）+ `ink_check2.py`（`gates/ink_check2.log`，裁图 `render/crop-*.png`） | 32 盒盒底下方 0 暗像素溢出；最紧盒内基线 clearance +5.0（P2 AND YOU?）；ink_check2 重测：P2 AND YOU? 深色真墨最低行 y=1543，距盒底像素缘 1545 为 +1 px（启发式 −1.0 px 为假警报，与 proof1 一致）；P3 HAYMITCH 标题右 clearance +90.0 px、顶 +19.0 px |
| 8 页逐页目视 | 印刷 PDF 110 dpi 全新渲染（`render/p--*.png`）；网页 P5/P8 同标准渲染（`render/w--5.png`、`w--8.png`） | P1–P8 印刷版逐页读完：无溢出、重叠、压页脚、截断、豆腐块；P7 D1 修复状态目视确认（8 条出处行均在第 2 栏，金句后紧跟；第 3 栏顶为 THE DRILLS）；P5 Q73 题干正常显示；P8 答案区 `73. up` 正常落版；网页 P5/P8 与印刷版逐页一致 |
| SVG 变化范围 | 修前快照 `pre/svg-sha-pre.txt` vs 修后 | **仅 `p8-test.svg` 变化；其余 7 页字节一致——此为正确且预期的结果**：Q73 键只出现在 P8 答案区，P5 只印 `Speak ___` 空白与 `speak up` 注记，键本身从不上 P5；p5 未变不是异常，不得为此返工（en-es delta 同样证实：p8 含 `73. up`，p5 不变） |

## 10. KIT 更新

- `WEEKLY-KIT.md` §7 三件 SHA/字节数已更新为修后值；§8 末新增 Delta Q73 条目；§9 末新增 Delta Q73 门禁重跑条目。只此一改，无其他 KIT 变动。

## 11. 结论

- 改动：仅 Q73 键 `speak` → `up` 一处；registry diff 恰 1 条、text.md diff 恰 1 行；Q73 四源一致为 `up`；SVG 仅 p8 变化、p5 未变（正确预期，见 §4/§9）。
- 门禁：上表全部通过；50 题填空/改写键适配全部合理；D5 字体仅记录（与 proof1 一致）。
- **可进 proof2**：是。本版已达 proof2 送审状态（proof2 只需针对本次 delta 做独立复核；其余内容与 proof2 已通过的版面字节一致——除 P8 外 7 页 SVG 与修前完全相同）。
- 未做：不 commit、不 push（协调员统一做）；未碰核心、其他版、tools/、map/翻译文件、ABSTRACT.txt。
