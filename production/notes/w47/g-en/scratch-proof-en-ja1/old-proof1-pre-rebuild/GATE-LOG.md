# GATE-LOG — 2026-W47 en-ja · proof1 机械门

- **版**：2026-W47 en-ja，VOL.4
- **复校日期**：2026-11-11
- **对象目录**：`production/2026-w47/2026-w47-en-ja/`；核心对照 `production/2026-w47/core-en/`
- ** scratch**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-ja1/`（全部中间件与日志在此；TMPDIR 指向其下 `tmp/`，未写 /tmp）

## SHA 核对（KIT §7 + 盘上 sha256sum）

| 文件 | 大小 | SHA-256 | 结果 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ja.pdf` | 41,509,526 B | `5cfb282caa800c343435639ee1b54a325f7d902e4fa6a3c53f2bc4e1374aa63c` | MATCH |
| `The-Lucerna-VOL4-en-ja.web.pdf` | 2,843,624 B | `f20c1affd5a53ab23dd8619715dfa86f72c3c6322c0faf5f8daf4c0b4cc7eabb` | MATCH |
| `2026-w47-en-ja.text.md` | 52,982 B | `1fcc919c1d72958cba7d8039a031eab12444aa066ad5a947f50e637061151f79` | MATCH |

两 PDF 各 8 页，页尺寸 1462.5 × 2025 pts（`pdfinfo`）。

## 逐门结果

| 门 | 命令 / 方法 | 结果 | 证据 |
|---|---|---|---|
| occlusion 审计 | `tools/venv/bin/python tools/occlusion_audit.py <svg dir> --json occlusion.json`（无 `--selftest`） | **PASS — 0 flags**，rc=0，selftest OK | `occlusion.json/.log` |
| p8 extract | `tools/p8.py` 抽取（本版 + core-en 对照） | **60/150 noted，两版抽取集完全相同** `[3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82–87, 89, 108–150]` | `p8extract.json/.log`、`p8extract-core.json/.log` |
| p8 compare | `tools/p8.py compare` | **CLEAN**，missing=[]，extra_count=0，keydiff=**[137, 138, 139, 140, 150]**（4 个读者语翻译键 + 写作键，预期内） | `p8compare.json/.log` |
| freeze baseline | `tools/freeze.py baseline --build core-en --core-svg core-en/svg --out freeze-base` | **PASS — 8/8 SVG 字节一致**，核心完整性未变 | `freeze-base.log`、`freeze-base/` |
| freeze diff | `tools/freeze.py diff --core-svg core-en/svg --edition-svg svg` | rc=0，新增 CJK 总计 **2,092**（全为日语讲解层，以平假名为主），移除 = 核心中文层 | `freeze.json/.log` |
| creambox 全版扫 | `creambox.py`（自兄弟 proof `scratch-proof-de-es1` 复制）本版 + core-en 对照 | 真溢出仅 **D2（P2，−12.7 px）、D3（P1，−18.0 px）**，两版相同；**P7 工具盒清除量 +48.2，干净**；其余负值为下标题伪影（core-en 相同负值佐证） | `creambox.log`、`creambox-core.log`、`creambox.py` |
| keycheck | `keycheck.py`（自 `scratch-fanout-de-rebuild-A`，配 `tr_ja.py`、`stub_svg.py`、`stub_bslib.py`） | **149/150 exact**；唯一不匹配 Q150 = 预期内的抽取截断 + 页脚泄漏（p8.py FOOTER_RE 已知 bug）。每页累计数与 KIT 一致（P1 10、P2 27、P3 45、P4 63、P5 81、P6 99、P7 111、P8 150）。rc=1 仅因 Q150 | `keycheck.log`、`keycheck-150.json` |
| check_s11 | `check_s11.py` ja（自 `scratch-fanout-en`） | **全部 §1.1 / P8 检查 PASS**：色集 core 19 = 本版 19；徽章 A2 #5c6e30 / B1 #46581f / B2 #37402f 在位；P8 最小字号 13.5；Q113–120 [A2] 选项标签；"Levels: 145–149 [A2]"；Q120 [A2] chip；"H　WRITING　作文 [B1]" | `check_s11.log` |
| boxtitle 宽度 | 以 core-en `svglib.text_w` 直接量取 SVG（40 个栏 3 粗体橄榄标题） | **39 PASS，1 FAIL = D5**（P3 "HAYMITCH'S GAMES　ヘイミッチの大会"，右缘 +26.9 px） | `boxtitle.log`、`boxtitle.py` |
| 印/网文字层 | `pdftotext -layout` 两版 | print 106,202 B，web 106,207 B；**词多重集相同**；5 字符差纯为空白（diff 10 行，均为单空格排版差，行 112/207/209/211/214）。内容同一 | `txt/print.txt`、`txt/web.txt` |
| 弯引号扫描 | text.md + 8 页 SVG 全扫 | text.md " 81 / ” 81 成对，0 贴 CJK；SVG " 82 / ” 82 成对，0 贴 CJK（+1 对为 Rousseau 图注 "Surprised!"，SVG 有、text.md 无）；无 ‘/’ | （扫描输出见 PROOF-NOTE） |
| 禁词 / 残留简体中文 | text.md grep | 中期选举/众议院/民主党赢下/参议院/星期五/金句/范文/桥接/占位/TODO/FIXME/Lorem **0 命中** | — |
| 目视 | 印刷卡片 p1–p8 全 8 页 + 网页 PDF P1/P8（`pdftoppm -r 100` 渲染） | 全部看过；D2/D3/D5/D6 均经裁切目视确认（`crop-p2-didyouknow.png`、`crop-p1-searches.png`、`crop-p3-haymitch.png`、`crop-p3-haymitch2.png`、`crop-p7-col3.png`、`crop-p7-bottom.png`） | `web-p1-1.png`、`web-p8-8.png`、各 crop |
| 答案键逐题核对 | text.md 答案 1–150 对 registry.json + 逐题语义核对题干 | 键/级别/题型一致，编号连续；**除 D1（Q39/Q40 互换）外全部正确**；另 4 组匹配题对印刷字母复核无误 | — |
| 星期核对 | `date -d` | Nov 3 周二、Nov 8 周日、Nov 9 周一、Nov 10 周二、Nov 15 周日、Nov 16 周一、Nov 18 周三、Nov 19 周四、Nov 20 周五、Nov 21 周六、Nov 22 周日、Nov 26 周四（感恩节）、Nov 27 周五、Dec 1 周二 —— 与印刷一致 | — |
| 外部事实 | 联网检索逐项核实 | 全部核实，见 PROOF-NOTE；仅 2 处微观说法未独立确认、无矛盾（"Day one is already sold out"、"more than 80% of schools"）；众院 254–162 存在另一 Nov 8 快照 252–161，记为快照口径差异 | — |

## 诚实说明（与任务简报的出入）

1. **p8 extract 不是 150/150**：工具对本版返回 **60/150 noted**，因为本版 P8 版式下仅 60 个键带印刷注记。 meaningful 的门是与 core-en 抽取集相同——该门通过。不得谎称 150/150。
2. **KIT §3 的 freeze 数字过时**：KIT 称新增 CJK 2,096，本次重跑 2,092，差值恰为 P4 gloss 修正删去的 4 个全宽冒号；KIT 数字早于该修正。P4 SVG 现 0× U+FF1A，修正已验证。
3. **keycheck rc=1 仅因 Q150**：抽取截断 + p8.py FOOTER_RE 已知 bug（混合大小写页脚漏进第 150 键），非版面缺陷。

## 缺陷汇总（详见 PROOF-NOTE.md）

| 编号 | 严重度 | 位置 | 归属 |
|---|---|---|---|
| D1 | MAJOR | P3 Q39/Q40 答案键互换（39 应为 a、40 应为 d） | 核心级候选（根在 core-en registry） |
| D2 | MINOR | P2 DID YOU KNOW 末行溢出盒底 12.7 px | 核心级候选 |
| D3 | MINOR | P1 SEARCHES 注脚溢出盒底 18.0 px | 核心级候选 |
| D4 | MINOR | ABSTRACT.txt 缺 Lucerna / A2–B2 / 150 | 本版特有 |
| D5 | MINOR | P3 盒标题溢出盒右缘 26.9 px | 本版特有 |
| D6 | MINOR | P5 D 节说明跨栏断裂（"と）。" 孤悬栏 3 顶） | 本版特有 |

**结论：(b) 缺陷清单，不可直接定稿。**
