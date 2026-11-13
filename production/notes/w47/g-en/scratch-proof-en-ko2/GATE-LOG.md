# GATE-LOG — W47 en-ko · proof2（独立复校，Q73 delta 后）

- 版：`production/2026-w47/2026-w47-en-ko/`，刊期 2026-11-16–22，VOL.4
- 复校员：独立 proof2（与 delta 执行者非同一人）；本轮会话 `a6718c59-84f2-461c-bc42-0ac1904beb1f`
- 工具解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0；除注明外；本版构建栈为 venv，见“栈口径说明”）；scratch：`hidden_files/w47/scratch-proof-en-ko2/`；`TMPDIR=<scratch>/tmp`，未写 `/tmp`
- 只读核查生产目录：构建类门禁在 scratch 副本里重跑；网 PDF 只重渲到 scratch，未覆盖生产目录网 PDF；未改任何生产文件，未 commit、未 push、未碰 core-en、未动 `tools/`
- 探针：`ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 式探针（`git hash-object -w <scratch>/tmp/probe.txt` → `f30b2a09c52cea680bce7e1ad7f0f138b90e0f5d`）；scratch 内真实写入 `probe.txt`。通过。
- 复校结束时三件 SHA 与任务给定值逐符一致（见下表），生产目录未动（结束核对：三件 + registry SHA 均与开工时一致）。

## SHA 核对（任务给定值 + 盘上 sha256sum，全符）

| 文件 | 字节 | SHA-256 | 核对 |
|---|---|---|---|
| `The-Lucerna-VOL4-en-ko.pdf`（印刷） | 32,386,301 | `c892247fe96290e8cc563ff72bdf2bfaa59ef9f73fd0ea0956391e4b4e696158` | ✓ |
| `The-Lucerna-VOL4-en-ko.web.pdf`（网页） | 2,629,430 | `e8f6f94a8ed493cbd4d0016ae6cbf0294a392af17d1337749b0897e6d3544a31` | ✓ |
| `2026-w47-en-ko.text.md` | 53,587 | `08d87476b499421c564a0931ab48bf7669463ea5f0a8a8ac9ac2a4545cab81f3` | ✓ |
| `registry.json`（另核） | — | `56f6620b5741bce7b6c8474e4f691ccb3bd909d3809f6bdc5b0848ac54cf732a` | ✓ 与 DELTA-NOTE §3 一致 |

两 PDF 各 8 页（PyMuPDF 验证：print 8 页，web 8 页；版面 1462.5×2025pt）。

## 栈口径说明（重要：任务“ko 家庭铁律”与本版的实际适用）

任务要求 freeze baseline/diff + run.py/check_core/check_gloss/textmd 用系统 python3，并称 venv 下 freeze ABORT rc=2 是预期的。本版实测与该描述**方向相反**，原因在 `tools/freeze.py` 的 guard 本身（`is_ko_family_path`：路径段须为 `core-ko` 或匹配 `^\d{4}-w\d+-ko-`，即韩语**目标**版 `2026-w47-ko-*`）：

- 本版路径 `2026-w47-en-ko`（英语目标 × 韩语读者）与 `core-en` 均不匹配 ko 家族，guard 要求 Pillow **13**（venv）。
- 系统 python3 跑 freeze baseline/diff 均 **ABORT rc=2**（guard 原文：`canonical stack is tools/venv Pillow 13.x (got Pillow 10.2.0 ...); re-run with tools/venv/bin/python`），见 `freeze-baseline-core-sys.log` / `freeze-diff-sys.log`——这是 guard 按设计工作，不是门禁失败。
- venv 跑 freeze baseline（core-en 标准口径）：**8/8 byte-identical**；版内自洽基线亦 8/8（见下表）。
- 为不留歧义，两栈都跑了、都记录在案；本结论以 guard 要求的 venv 栈为准。另：仓库内不存在 `check_core.py` / `check_gloss.py` 独立脚本（全仓 grep 仅命中无关文件：onnxruntime 内置码、W45 旧 proof、W46 KIT 提及；SOP.md 的 `gloss` 仅见于 cover.json 字段说明）——其指代的核心对照/注释核对由 keycheck、p8 compare、freeze diff、stemfit 覆盖，均已跑。

## delta 范围独立核实（逐项，与 DELTA-NOTE §4 对照）

| 声称 | 独立核实结果 |
|---|---|
| registry 恰好 1 条差异 | ✓ `registry-pre.json` vs 现 registry：恰好 1 条（n=73 speak→up）；现 registry == `registry-delta.json`（逐字节内容相等） |
| text.md 恰好 1 行差异 | ✓ `text-pre.md` vs 现 text.md：恰好 1 行（1151 行 `speak`→`up`）；题干 589 行未动 |
| 仅 p8 SVG 变化 | ✓ 8 页 SHA：p1–p7 与修前逐个一致；p8 `c50c2edd…` → `007698e2…`；与 `svg-post.sha` 逐值一致 |
| p5 不变是正确预期 | ✓ p5 SHA 与修前一致；P5 内 7 处小写 `speak` 均为题干/正文/注释（`Speak ___`、`to speak up`、`Break the ___: speak up about bullying.`、`75. to speak up`、`Children (speak) up this week.`），无一处是 Q73 键 |
| Q73 四源一致 | ✓ registry / text.md 答案区 / P8 印出键 / P5 题干+注释（见 PROOF-NOTE §1）；core-en Q73 亦为 `up` |

## 逐门结果

| 门 | 结果 | 证据/日志 |
|---|---|---|
| 构建重跑（scratch 副本，venv） | **通过** | 新副本 `build-copy-en-ko/`（仅 `*.py` + `assets/`）：venv 重跑 rc=0，`TOTAL exercises: 150`，`OVERFLOW`/`TOO WIDE` 命中 0（run.log 流末值与 delta 一致：P8-keys 2205/2560、P2-ex 2532/2560），`MODEL words: 82`，重生成的 8 个 SVG 与生产 SVG SHA-256 逐个一致（`MATCH` 8/8）；重跑 registry 与生产 `registry.json` 内容相等（150 条）。`rerun-venv.log`、`registry-rerun.json`。注：同一副本用系统 python3 重跑为 7/8 DIFF（仅 p4 MATCH），属栈 artifact：生产 SVG 由 venv（Pillow 13.0.0 / FreeType 2.14.3）构建；系统栈重跑 TOTAL/流末值相同，仅 x 坐标微差。`rerun-sys.log` |
| run rc=0 / TOTAL 150 | **通过** | 同上；分版 10/17/18/18/18/18/12/39（P8 112–150 共 39 题） |
| ABSTRACT 全文形式 | **通过** | `ABSTRACT.txt` 624 字节，SHA `927505ce05ef9c169d89d7d797530c9d2148fd6652963b44276483d3735bc81a`，与 fanout-en2 `abstracts/ko.txt` `cmp` 字节一致；未动 |
| Q73 四源一致 | **通过** | registry n=73 `up`；text.md:589 题干 + :1151 答案 `up`；P8 SVG 含 `73. up`、`73. speak` 0 次；P8 抽取键 73 = `up`；core-en Q73 = `up`，core P8 SVG 含 `73. up`；P5 题干 `Speak ___` + 注释 `to speak up = 목소리를 내다` 一致（见 PROOF-NOTE §1） |
| D1 Ashes 无回归 | **通过** | P4 标题 `Perth, One Year On: How Australia Kept the Ashes`（SVG 两节点拼合证实）；`Perth is winning` / `Ashes begin` / `second week in Perth` 全版 0 处（含 text.md）；首场 2025-11-21 周五珀斯、4–1、Cummins 背伤 / Smith 代任 / Boland / Doggett 首秀 / Hazlewood 腿筋伤一律过去时（proof1 已外部复核，本轮未改动） |
| D2 Q39/Q40 无回归 | **通过** | registry 38=b、39=a、40=d、41=c；text.md 答案区 39 a、40 d；P8 抽取键 38–41 = b/a/d/c |
| D3 ODD SOCKS 无回归 | **通过** | P5 框题短标题 `ODD SOCKS, IN NUMBERS　숫자로`；源级 375.4px、PIL 真墨余量 +29.5px、SVG advance 余量 +29.1px；全页目视在框内 |
| occlusion 审计 | **0 flags（通过）** | 真实命令（未用 `--selftest`）：`flag_count: 0`。工具自检 6 类阳性对照全部触发、干净对照静默（另跑 `--selftest` 仅作工具验证，见 `occlusion-selftest.log`）。`occlusion.log/json`；core-en 对照亦 0 flags（`occlusion-core.log/json`）。已知盲区同 proof1（BOXTITLE 只覆盖有描边或填色 `#2c2822` 的矩形）——本版由 boxtitle 门 + PIL 真墨 + 目视覆盖 |
| spill sweep（盒外行） | **0 真溢出（通过）** | 24 处“盒外基线”逐项核对：全部为下一区块的首行（栏目标题/下段首行，如 TRY IT NOW / WHAT IS ON THIS WEEK? / FIVE SENTENCES / READERS' CORNER / MODEL 框上方的图片说明），间距均匀 35.5–37px（一倍行距的正常块间距），无一处是盒内内容的溢出；另 2 处 ABOVE-BOX 为框上方的题头/图注。`mech-checks.log` |
| p8 extract + compare | **CLEAN（通过）** | core 与 edition 各 60/150 带印刷注释，同一集合；compare CLEAN，无缺失、无多余；keydiff = [137, 138, 139, 140, 150]，逐项说明：137–140 为 E 翻译题键（核心中文译文 vs ko 版韩文译文，读者语改向，预期内）；150 为开放写作题键（核心中文措辞 vs ko 版韩文措辞，预期内）。`p8-extract.log/json`、`p8-extract-core.log/json`、`p8-compare.log/json` |
| keycheck（p8 抽取键 × registry；registry × core；registry × 重跑） | **通过** | registry 150 条，重跑 registry 150 条，二者内容相等；registry-vs-p8extract exact **149/150** + exc=[150]（抽取器截断长开放题键为 “열린 문제”，既定预期），mismatch=[]；registry-keys-vs-core **145/150**，diffs 仅 137–140、150（读者语改向，预期内）；Q38–41 = b/a/d/c；Q125 A、Q46 A、Q52 hosted、Q55 won；Q82/83/84 = B/C/A；noted set == core noted: True；extract keys 150，无缺失。`keycheck.log` |
| freeze baseline（标准口径 core-en） | **通过（venv）** | venv：**8/8 SVGs byte-identical**（`--build core-en --core-svg core-en/svg`）；`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。`freeze-baseline-core.log`。系统 python3：ABORT rc=2（guard 要求 Pillow 13，见“栈口径说明”）。`freeze-baseline-core-sys.log` |
| freeze baseline（版内自洽，补充） | **通过（venv）** | `--build <scratch>build-copy-en-ko --core-svg <edition>/svg`：**8/8 SVGs byte-identical**（p8 `007698e2…` 与 delta 修后值一致）。`freeze-baseline-edition.log` |
| freeze diff | **通过** | venv：TOTAL 新增 CJK **2323**：Hangul 2309、U+3000 9、CJK 标点 5；新增汉字（U+4E00–U+9FFF）**0**。分版：p1 213 / p2 316 / p3 162 / p4 170 / p5 166 / p6 183 / p7 471 / p8 642——与 delta 逐项一致。`freeze-diff.log/json`。系统 python3：ABORT rc=2（同上）。`freeze-diff-sys.log`。独立 CJK 扫描（`cjk_scan.log`）：逐页 added 与 freeze 逐页值完全一致；全局 multiset 差为 2322，仅因 1 字跨页净抵（聚合口径差异，以逐页 freeze 值为准）；added Han 0。SVG 内唯一汉字为核心继承的 P1 刊头三色蛾装饰 `三色蛾`（§1.1 规定元素） |
| 印/网文字层同一 | **通过** | `pdftotext -layout` 两版各 **107,720 字节**，`cmp` 字节一致；token multiset diff **0/0**；PyMuPDF 逐页 span 数一致（P1 227 / P2 259 / P3 216 / P4 229 / P5 197 / P6 218 / P7 242 / P8 273，两版相同）。`print.txt`、`web.txt` |
| 网版重渲（仅 scratch） | **通过** | `tools/webpdf.py svg/ <scratch>/web-rerender.pdf` rc=0：2,629,443 字节（vs 生产网版 2,629,430，+13 字节为字体子集化非确定性，预期；SHA/字节数本身不可复现）；重渲版文字层与生产网版 `cmp` 字节一致、token multiset diff 0/0。生产网 PDF 未被覆盖（SHA 始终 `e8f6f94a…`）。`webpdf-rerender.log`、`web-rerender.pdf/txt` |
| P8 最小字号 | **通过** | PyMuPDF 实测印版：P8 最小 **10.125pt**（答案行，SVG 13.5px），≥ 9.75pt 底线；其余各页最小 11.625pt；网版同值。`printweb.log`；`verify_ed.py` 亦测得 P8 最小 10.12pt |
| creambox（canonical 全版扫描） | **通过** | canonical `hidden_files/w47/tools/creambox.py`（系统 python3，8 个 SVG 作参数）：rc=0，输出与 proof1 `creambox-canon.log` **逐字一致**；全部 inside-only 清除量为正，最小 **+5.0px**（P2 AND YOU? 框）；所报负清除量（-35.5/-36/-37.0）皆为 +45px 窗口的已知假阳性（所报“末行”皆为框下方下一区块的首行/标题，清一色一倍行距，工具已标注 BELOW-WINDOW）；P7 工具盒最小 inside 清除量 +47.7、最小 desc-clear +41.6；P8 MODEL 框清除量 +92.4。`creambox-canon.log`（注：首次调用误传版目录致 IsADirectoryError，已纠正为传 8 个 SVG 文件，见该日志首版错误；正确调用 rc=0。另 venv 交叉跑结果相同，见 `creambox-canon-venv.log`） |
| boxtitle 宽度 | **通过（1 处观察 O1）** | 源级 `boxtitle-ko.py`（系统 python3）：12 项中 11 项在 386.5px 通用预算内，HAYMITCH 400.7px 标 OVER（venv 口径 401.9px，见 PROOF-NOTE O1）；ODD SOCKS 375.4px。SVG 扫 `sweep_svg_titles.py ko`：18/18，**overflows: 0，PASS**，HAYMITCH advance 余量 +2.6px / 真墨余量 +2.5px。`boxtitle.log`、`sweep_svg_titles.log`、`ink_ko.log`（`ink_ko.log` 与 proof1 逐字一致） |
| P2 AND YOU? 真墨复算 | **通过（观察 O2）** | 独立复算（anchor=`ls` 帧）：`요.` 墨水在基线处止（ink_below_baseline=0），真墨余量 **+5.05px**；`ink_ko.py` 所报 −19.0 是该脚本量测口径错误（`getbbox` 默认 `la` 帧 y1 被直接加到基线上）。放大裁切 `render/crop-p2-andyou.png` 目视确认末行完整在框内 |
| 孤儿标点全版扫 | **0 真孤儿（通过）** | text.md 行首孤儿 0；8 个 SVG 逐节点扫查：8 处“纯标点节点”全部为同基线折分 artifact（P2 5 处 “—” 为日历分隔符、与同行韩文/数字同基线；P7 3 处 “.” 为句末句号、与所属句同基线 y=754.03/841.59/959.68），非孤儿。另：全版独立 `___` 节点 19 处（P2 4 / P3 5 / P4 4 / P5 4 / P8 2；P1/P6/P7 0），edition 与 core-en 逐页位置完全一致，属核心既有排版形态，记观察 O3。`mech-checks.log` |
| 150 题三源逐题手验 + stemfit | **0 flags（通过）** | text.md 全 1305 行逐行通读；答案区 150 条编号连续；text.md 答案区 vs registry **150/150**；5 组配对题释义顺序逐组对 SVG 核对无误；stub 逐项复核（`stemfit2-proof.py`，REG_PATH 指向生产 registry.json，与 delta scratch 无关）：ex 项 121 个，含 `___` 题干 **57 个**，机械 flags **0**；完形段落（Q112–119）与对话段落（Q145–149）代入键后全文通顺；Q73 现为 `Speak up: tell a teacher.`。`stemfit2.log` |
| check_s11.py ko | **ALL PASS** | colour set core 19 = edition 19，无多无缺；badge 色 A2/B1/B2 均在版；P8 最小字号 13.5px；P8 Q113–120 options 行 `[A2]` 标签、Levels 145–149 [A2]、Q120 [A2] chip、WRITING head 均在。`check_s11.log` |
| verify_ed.py ko | **ALL PASS** | Q39 a、Q40 d、Q46 A、Q52 hosted、Q55 won、Q125 A、registry 无陈旧 Ashes 措辞、text.md 150 答案、P8 最小 PDF 字号 10.12pt ≥ 9.75pt 等全部 PASS。`verify_ed.log` |
| 日期/星期 | **通过** | `date` 核验：2025-11-21 周五、2026-01-08 周四、11 月 3 日周二、8 日周日、9 日周一、10 日周二、15 日周日、16 日周一、18 日周三、19 日周四、20 日周五、21 日周六、22 日周日、26 日周四、27 日周五、12 月 1 日周二、12 月 18 日周五、2027-01-03 周日 |
| 残留简体中文 | **通过** | text.md 汉字（U+4E00–U+9FFF）0 个；SVG 汉字仅 P1 刊头三色蛾装饰 `三色蛾`（§1.1 规定元素，属意）；新增汉字 0 |
| 禁词 | **通过** | `SOP`、`proofread`、`cover`、`lint`、`github`、`TODO`、`placeholder`、`占位`、`bridge` 在 text.md 中均为 0 |
| 弯引号/撇号 | **通过** | text.md 中 “ 81 个 / ” 81 个，成对；U+2019 为 0 个；ASCII 撇号 40 个；P3 框题撇号为 ASCII U+0027 |
| 金句逐字 | **通过** | P7 金句 8 条与原文页面逐字一致（8/8，见 proof1；本轮未改动） |
| MODEL 范文词数 | **通过** | P8 MODEL 82 词（构建计数；连独立 em-dash 计为词符则为 84），在 80–100 词范围内 |
| 目视 | **通过** | 印刷 P1–P8 全页 + 网页 P1/P8 全页已目视（`render/print-p1.png`…`print-p8.png`、`web-p1.png`、`web-p8.png`，96dpi，PyMuPDF）；无溢出/重叠/压页脚；印/网逐页目视一致。放大裁切：`crop-p8-answers.png`（`73. up` 清晰）、`crop-p5-q73b.png`（B 组 73. `Speak __: tell a teacher.`）、`crop-p5-oddsocks*.png`（D3 在框内）、`crop-p2-andyou.png`（O2 末行在框内）、`crop-p7-bottom.png`（工具盒干净）。注：驱动初版 `render_pages.py` 的 sed 换址把 OUT 写重导致 16 张 PNG 落入错位嵌套目录（`hidden_files/w47/home/...`），已全部移回本 scratch `render/` 并删除错位目录树；delta 的 render 目录未被触碰（其文件 mtime 15:34–15:36，早于本轮驱动 15:56+） |

## D5 字体（只记录，不判定）

- 印版 PDF：43 个字体对象，全部已嵌入 + 子集化；字体族：NotoSansCJKsc（Bold/Regular）、NotoSerifCJKsc（Bold/Regular）、Newsreader16pt（Regular/Italic）、UnifrakturMaguntia、DejaVuSans；无未嵌入字体
- 网版 PDF：43 个字体对象，全部已嵌入 + 子集化；同一字体族，子集重命名为 Lucerna*
- 8 页目视中韩文字形完整、无缺字（tofu）；P6 练习选票 ☐ 正常渲染
- 拉丁读者解释层在 Noto Sans CJK SC 是已知待用户裁定的全线问题，不作本版缺陷（任务门 9）

## 结论

- **(a) 零缺陷，可定稿**：proof1 唯一缺陷 D4（Q73）已修，四源一致；ko1 D1/D2/D3 无回归；全部机械门通过；无新缺陷。
- 本复校未改任何生产文件、未碰 core-en、未动 `tools/`。
