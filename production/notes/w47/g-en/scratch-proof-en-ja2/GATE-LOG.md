# GATE-LOG — 2026-W47 en-ja · proof2 机械门（Q73 delta 重建版）

- **版**：2026-W47 en-ja，VOL.4
- **复校日期**：2026-11-11
- **对象目录**：`production/2026-w47/2026-w47-en-ja/`；核心对照 `production/2026-w47/core-en/`
- **工作区**：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-ja2/`（全部中间件与日志在此；TMPDIR 未写 /tmp；delta/proof1 的脚本拷入本目录后改写路径重跑——`dump_reg_delta.py`、`make_textmd_w47.py`、`keycheck_ed.py` 内的 `scratch-delta-en-ja` 路径已改指本目录，且 `make_textmd_w47.py` 的 OUT_PATH 已改写为本目录内 `textmd-regen.md`，绝不写生产目录）

## SHA 核对（任务简报 + 盘上 sha256sum，复核前后各测一次）

| 文件 | 大小 | SHA-256 | 结果 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ja.pdf` | 41,509,391 B | `e91ed980047959177588a26c72fff55bc2710c7ce476d631d87d1bcd20c19542` | MATCH（复核前＝复核后） |
| `The-Lucerna-VOL4-en-ja.web.pdf` | 2,883,888 B | `fb903b2b1da9be8abc04ad40e6387cb6050eaa41bc4c3c63b0eddb07150f48f0` | MATCH（复核前＝复核后） |
| `2026-w47-en-ja.text.md` | 53,585 B | `2d498e4e9b997c85b00671aef294d197b5be420d1eeb9bbf0efcac6d50c3b96e` | MATCH（复核前＝复核后） |

修前（proof1 (a)）对照：印 `9f9faaea…` / 41,509,391 B；网 `25645767…` / 2,883,877 B；文 `219ce22d…` / 53,588 B。

## 逐门结果

| 门 | 命令 / 方法 | 结果 | 证据 |
|---|---|---|---|
| 探针 | `ls /dev/null` 存在；`echo test \| git hash-object -w --stdin` 通（`9daeafb9…`）；工作区真实写文件成功 | **PASS** | `.probe` |
| delta registry diff | `diff` delta `pre/registry.json` vs 现盘 registry.json | **恰好 1 行**：583 `speak` → `up` | `registry-diff.log` |
| delta text.md diff | `diff` delta `pre/2026-w47-en-ja.text.md` vs 现盘 text.md | **恰好 1 行**：1151 `speak` → `up`；−3 B | `textmd-diff.log` |
| delta SVG 范围 | `svg_byte_diff2.py`：delta `pre-svg/` vs 现盘 `svg/`（逐字节前缀/后缀定位 + 后缀恒等复测） | **P1–P7 字节一致；P8 仅字节 1228700 一处** `73. speak`→`73. up`（−3 B） | `svg-byte-diff.log` |
| SVG 现盘哈希 | `sha256sum svg/*.svg` | 与 delta `post-svg-sha.txt` 全 8 页一致；p5 `cacd38b4…` = 修前，p8 `b86fb714…` = 修后 | `svg-sha-now.txt` |
| Q73 四源 | registry / text.md:1151 / P8 印文字层 / P5 题干 + 注记 | **四源一致为 up**；残留 `"key": "speak"` 0 命中 | PROOF-NOTE |
| run.py | scratch 副本 `run-copy/` 内 `run.py`（venv python） | **rc=0，TOTAL 150，MODEL 82，0 OVERFLOW / TOO WIDE**（build.log 全文 grep 无 overflow/warn/error）；P8-keys y=2205/2560 | `build.log` |
| run.py 重建 SVG | `run-copy/svg` vs 现盘 `svg/` 逐文件 sha256 | **8/8 字节一致** | `run-copy-sha.txt` |
| freeze baseline（真核心） | `tools/freeze.py baseline --build production/2026-w47/core-en --core-svg production/2026-w47/core-en/svg --out freeze-base-core` | **PASS — 8/8 SVG 字节一致**；核心完整性未变（8 文件复哈希） | `freeze-base-core.log`、`.json`、`freeze-base-core/` |
| freeze baseline（版内） | `tools/freeze.py baseline --build production/2026-w47/2026-w47-en-ja --core-svg production/2026-w47/2026-w47-en-ja/svg --out freeze-base-edition` | **PASS — 8/8 SVG 字节一致**（p5 `cacd38b4…` = 修前哈希，p8 `b86fb714…` = 修后已发哈希） | `freeze-base-edition.log`、`.json`、`freeze-base-edition/` |
| freeze diff | `tools/freeze.py diff --core-svg core-en/svg --edition-svg svg` | rc=0，新增 CJK 总计 **2,084**（逐页：182/273/159/168/145/156/435/566，与 proof1 完全一致） | `freeze-diff.json/.log` |
| registry 自源重建 | `dump_reg_delta.py`（路径改指本目录）自 content*.py 重建 registry | **rc=0，150 条；与现盘 registry.json 字节一致**；每页 10/17/18/18/18/18/12/39；A2 62 / B1 66 / B2 22 | `dump_reg.log`、`registry.json` |
| text.md 自源重建 | `make_textmd_w47.py`（OUT 改指本目录 `textmd-regen.md`） | **rc=0，53,585 B；与现盘 text.md 字节一致**；stub registry 150 = 真 registry 150 | `textmd.log`、`textmd-regen.md` |
| occlusion 审计 | `tools/occlusion_audit.py <svg dir> --json occlusion.json`（真实审计，非 --selftest） | **PASS — 0 flags**，rc=0，selftest OK（6 类 planted 全触发，clean 对照静默） | `occlusion.json/.log` |
| p8 extract | `tools/p8.py extract`（本版 + core-en 对照） | **60/150 noted，两版抽取集完全相同**（set `[3, 14, 36, 43, 54, 57, 66, 71, 72, 76, 82–87, 89, 108–150]`） | `p8-extract.json/.log`、`p8-extract-core.json/.log` |
| p8 compare | `tools/p8.py compare`（读本体） | **CLEAN**，missing=[]，extra_count=0，keydiff=**[137, 138, 139, 140, 150]**（预期内：4 个读者语翻译键 + 写作键） | `p8-compare.json/.log` |
| keycheck | `keycheck_ed.py ja`（路径改指本目录） | **registry vs P8 抽取 149/150 exact**，唯一不符 Q150 = 已知抽取截断 + 页脚泄漏（见诚实说明 2）；registry vs core 145/150，diff 仅 137–140、150（预期）；Q38–41 = b/a/d/c；noted set == core | `keycheck.log`、`keycheck_ed.py` |
| text.md 答案 150 | 答案行正则抽取 vs registry.json 逐项比对（键/级别/题型） | **150/150，0 差异**；Q73 = up | `answers-150.log`、`answers150.py` |
| check_s11 | `check_s11.py ja` | **ALL §1.1/P8 CHECKS PASS**；色集 core 19 = 本版 19；徽章 A2 #5c6e30 / B1 #46581f / B2 #37402f 在位；P8 最小字号 13.5；"Levels: 145–149 [A2]"；Q120 [A2] chip；"H　WRITING　作文 [B1]" | `check_s11.log` |
| creambox 全版扫 | `creambox.py`（+45 px 窗口版，8 页 SVG 作参数） | 真溢出 **0**；D2 +14.3、D3 +12.0；其余负值均为盒下节头伪影（−35.5/−36/−37，core-en 同盒同值） | `creambox.log`、`creambox.py` |
| creambox inside-only | `creambox_inside.py`（仅计盒内基线） | **0 真溢出**；每页最差 P1 +12.0、P2 +5.0、P3–P7 +47.7、P8 +92.4；P2 desc-clear −1.0 为假名行 heuristic 伪报（同 proof1） | `creambox-inside.log`、`creambox_inside.py` |
| boxtitle 宽度（源） | `sweep_titles.py ja` | **12/12 全过**；最紧 THE WEEK IN NUMBERS +1.5；HAYMITCH +19.1；ODD SOCKS +23.6；A PRACTICE BALLOT +65.6 | `boxtitle.log` |
| boxtitle 宽度（SVG） | `sweep_svg_titles.py ja` | **18/18 全过，0 溢出**；THE WEEK IN NUMBERS 真墨 +1.5 | `boxtitle-svg.log` |
| PIL 真墨重测 | `ink_titles.py` | P5 ODD SOCKS **真墨 +23.5**；P6 A PRACTICE BALLOT **真墨 +65.5**；THE WEEK IN NUMBERS 真墨 +1.5 | `ink_titles.log` |
| P8 最小 PDF 字号 | fitz 逐 span（印 + 网） | **10.12 pt**（两版一致，≥ 10 pt 下限）；全文档最小亦 10.12 pt | `p8font.log` |
| 印/网文字层 | `pdftotext -layout` 两版 + 词多重集 + 逐页字节比对 | print 101,065 字符 = web 101,065 字符；**全文逐字节相同；词多重集差 0；逐页字节一致 8/8** | `printweb.log`、`txt/print.txt`、`txt/web.txt` |
| 网 PDF 重渲染（仅 scratch） | 复制 svg 到 `webrerender/`，`webpdf.py` 重渲染 | RC=0，2,883,892 B，49,784 text bytes；SHA 与已发版不同（`1d86b217…`，符合铁律）；文字层与已发网/印两版**均差 0**（101,065 字符，逐页 9/9 含尾空分段）；已发网 PDF 未动（复核后仍 `fb903b2b…`） | `web-rerender.log`、`web-rerender-compare.log`、`webrerender/out.web.pdf` |
| 填空/改写键适配 | AST 抽取全部 `___`/`→` 题（53 项）逐项审键填空合理性 + 与 registry 1:1 映射 | **53/53 键合理**（含 Q73 "Speak up"）；映射 1:1 53 项，unmapped/multi 均为 0；Q2/Q79、Q5/Q80、Q6/Q12 同题干同键为既有复用，两处一致 | `fill-rewrite.log`、`fill-rewrite-map.log` |
| 弯引号扫描 | text.md + 8 页 SVG 全扫 | text.md “ 81 / ” 81 成对，0 贴 CJK，0 个 ‘/’；SVG “ 82 / ” 82 成对，0 贴 CJK（+1 对为 Rousseau 图注 "Surprised!"） | `quotes.log`、`quotes_scan.py` |
| 孤儿标点扫查 | CJK 孤儿集（、。）」』…）行首/元素首扫查 | text.md **0**；SVG 文本元 **0**；24 个以 — 开头的 SVG 文本元均为有意破折号开头（归属行/续行/分隔符），非孤儿标点 | `orphan.log`、`orphan2.log`、`orphan_scan.py` |
| 禁词 / 残留简体中文 | text.md + SVG 文本 + registry grep | 中期选举/众议院/民主党赢下/参议院/星期五/金句/范文/桥接/占位/FIXME/Lorem/已确认/宣布/宣佈 **0 命中**；TODO 文本 0 命中（朴素子串在 p3 base64 图片数据内有 1 偶然命中，非文本）；日语用 発表 8× | `quotes.log`、`orphan.log` |
| ABSTRACT | 全文核对 | **完整式**：Lucerna、VOL.4、150、A2、B2 俱在；0 ASCII 双引号；666 B | （见 PROOF-NOTE） |
| 家具 | masthead / 刊期 / 页脚 / 徽章 grep + 目视 | 8 页齐全一致；"WEEK OF NOVEMBER 16 TO 22, 2026" 在 P1；页脚每页 1× | （见 PROOF-NOTE） |
| Q39/Q40 四方一致 | SVG 题干/选项、registry 键、text.md 注记、P8 提取键 | **四方一致**：a=mentor、b=tribute、c=campmate、d=arena；39=a、40=d | `keycheck.log` |
| P5 D 节（旧 D6） | SVG 文本行位置核对 + 目视 | 说明单行 "現在進行形で書きかえよう。" y=2543.95（页脚线上 52 px），栏 3 顶为 Q78–81 本题，无孤字 | （见 PROOF-NOTE） |
| 残留措辞 | "Ashes begin" 等 grep | SVG + text.md + registry **0 命中**；"Arsenal are winning" 1×、"June 2027" 2× | （见 PROOF-NOTE） |
| "next Sunday" 冻结规则 | core-en / en-ja 源码+registry+SVG / text.md | **0 命中**——无适用对象，规则不适用 | （见 PROOF-NOTE） |
| D5 字体（只记录，不判） | SVG font-family 统计 | 5 种：Newsreader 1037、Noto Sans CJK JP 633、Noto Serif CJK JP 55、DejaVu Sans 4、UnifrakturMaguntia 1（与 proof1/delta 完全一致） | `fonts.log` |
| 目视 | 印刷卡片 p1–p8 全 8 页（100 dpi 渲染）+ 网页 PDF P1/P8 + P8 答案区放大 + P5 Q73 放大 | **全部看过，干净**；P5 Q73 题干在位、D 节单行说明、ODD SOCKS 标题在盒内；P8 答案区 `73. up` 放大目视确认；网 P1/P8 与印版版式一致（P1 国会大厦照片网版下采样，内容同一） | `render/p-1.png` … `render/p-8.png`、`render/p8-answers-zoom.png`、`render/p5-q73-zoom.png`、`render-web/web-p1-1.png`、`render-web/web-p8-8.png` |
| 全文通读 | text.md 1305 行全读 | 150 题逐题手验：题干与键逐项适配，四组匹配题逐组核对，金句 8 条逐字核对；全部正确 | PROOF-NOTE |

## 诚实说明（与任务简报 / delta 报告的出入）

1. **p8 extract 不是 150/150**：工具对本版返回 **60/150 noted**，因为本版 P8 版式下仅 60 个键带印刷注记。有意义的门是与 core-en 抽取集相同——该门通过。不得谎称 150/150。
2. **keycheck 149/150 唯一不符 Q150**：抽取截断 + p8.py FOOTER_RE 已知 bug（混合大小写页脚漏进第 150 键），非版面缺陷。本轮所用 keycheck_ed.py 的 rc=0（脚本本身不以 mismatch 退出）；proof1 的 keycheck.py 同一 mismatch 下 rc=1——rc 差异是脚本口径，不是结果差异。
3. **文字层字符数口径**：本轮 `-layout` 提取印/网各 101,065 字符、全文逐字节相同；delta 报告的 "43,472 字符" 是另一计数口径（非 `-layout`），不构成出入——逐页字节一致 8/8 是更强的同一性证据。网重渲文件 2,883,892 B（vs 已发 2,883,888 B，+4 B）亦为铁律内浮动，文字层差 0。
4. **fill 日志题号口径**：`fill_rewrite.py` 以 ex 调用序号编号（Q73 在该日志中为第 61 个 ex 调用），不是 registry n；`fill_rewrite_map.py` 已验证与 registry 1:1 映射 53 项。编号差异不是内容差异。
5. **TODO 朴素子串 1 命中是假阳性**：`svgs.count("TODO")` 在 p3-culture.svg 有 1 命中，位于 base64 图片数据内；剥离 data URI 后 SVG 文本/markup 中 TODO 为 0。proof1 的 "0 命中" 是文本口径，本轮复测一致。
6. **孤儿标点初版脚本的两个计数 bug 已纠正**：第一版把空 `<text>` 元素（`'' in 集合` 为 True）和行首 —（有意破折号）计入孤儿，分别报 29/53；修正后（非空守卫 + CJK 孤儿集）text.md 0、SVG 文本元 0，24 个 — 开头元均为有意破折号。最终数字以修正版为准。
7. **creambox.py / creambox_inside.py 首次调用漏传参数**：第一轮未传 SVG 路径，creambox.log 为空、inside 脚本 IndexError；已按脚本用法（路径参数 / glob 参数）重跑，两份日志均为完整实测值。
8. **webpdf.py 首次调用用了不存在的 --out 参数**（rc=2）：已按 `webpdf.py svg_dir out_pdf` 位置参数重跑，rc=0。重渲只在 scratch 副本里做，已发网 PDF 的 SHA 复核后仍为 `fb903b2b…`，未动。
9. **网 PDF SHA 必然不同**：重渲 `1d86b217…` vs 已发 `fb903b2b…`，符合铁律（fontTools 子集 head.modified 墙钟 + cairo CreationDate）；内容以文字层为准（差 0）。

## 缺陷汇总

**零缺陷。结论：(a) 定稿。确认 en-ja 可定稿。**
