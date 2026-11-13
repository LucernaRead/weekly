# DELTA-NOTE — W47 en-ko · Q73 键同步 delta（core-en fix2）

- 版：`production/2026-w47/2026-w47-en-ko/`，刊期 2026-11-16–22，VOL.4
- 任务：只对本版做 Q73 键同步 delta（core-en fix2 已定稿；本版 proof1 结论 (b)，唯一未决项 D4 = Q73）
- 唯一改动：`content56.py:49`，Q73 f.ex 键 `"speak"` → `"up"`；note（`speak up = 목소리를 내다`）与题干（`Speak ___: tell a teacher.`）一字不动；其余源行、map/翻译文件、ABSTRACT.txt、KIT 以外文件均未碰
- 未 commit、未 push（10 版并行，git 操作由协调员统一做）；未碰核心、其他版、`tools/`
- 证据目录：`hidden_files/w47/scratch-delta-en-ko/`（本文件 + 全部日志/json/渲染图）

## 1. 修前核对（动手前，全部通过才动手）

- 修前三 SHA 与 proof1 (b) 记录（`scratch-proof-en-ko/GATE-LOG.md` SHA 核对表）逐符一致，生产目录未动：

| 文件 | 字节 | SHA-256（修前） |
|---|---|---|
| `The-Lucerna-VOL4-en-ko.pdf`（印刷） | 32,386,301 | `ecad215eb3f5ab98e6d50a7fd5ea5b383902c8f1ea0aadd3bff1fb28822072cd` |
| `The-Lucerna-VOL4-en-ko.web.pdf`（网页） | 2,629,426 | `5115ad3f586bbb94226ad841bbfeedd31fa80eecc7ee6cf4a9296d43ccc9ca9e` |
| `2026-w47-en-ko.text.md` | 53,590 | `e5633ac3569d216ce5e7f0578af3ab0c920fa964c77636fd2c7954a3a05484ac` |

- 核心已修好（只读对照）：`core-en/content56.py:49–50` 为 `"up"`、`"speak up = 大声说出来"`、`"Speak ___: tell a teacher."`；core-en registry Q73 = `up`，core-en P8 SVG 已印 `73. up`
- 三源同错（预期状态，全部核实）：
  - registry n=73：`key: 'speak'`，`note: 'speak up = 목소리를 내다'`
  - text.md:589 题干 `EXERCISE: Speak ___: tell a teacher.`；答案区 1151 行 `73. [A2] 문장 완성 — speak (speak up = 목소리를 내다)`
  - P8 SVG（`svg/p8-test.svg`）：印出键 `73. speak`
- D1/D2/D3 修前状态（与 proof1 (b) 记录对照，已修）：
  - D1：P4 标题 `Perth, One Year On: How Australia Kept the Ashes`；`Perth is winning` / `Ashes begin` / `second week in Perth` 全版 0 处
  - D2：registry 38=b、39=a、40=d、41=c
  - D3：P5 框题 `ODD SOCKS, IN NUMBERS　숫자로`（短标题）

## 2. 改动与重建

- 改动（`content56.py:49`，仅此一行）：
  - 前：`f.ex("A2", "문장 완성", "speak", "speak up = 목소리를 내다",`
  - 后：`f.ex("A2", "문장 완성", "up", "speak up = 목소리를 내다",`
- 重建（全部用 `tools/venv/bin/python`，标准 venv 栈）：
  - `run.py` → `run.log`；`render.py` → `render.log`（cards + 印版 PDF）
  - registry 重导：`dump_reg_delta.py`（proof 版 `dump_reg.py` 的改址副本，输出本 scratch `registry-delta.json`）→ 拷回版内 `registry.json`；`dump_reg.log`
  - text.md 重导：`make_textmd_delta.py`（fanout 版 `make_textmd_w47.py` 的改址副本，REG_PATH 指本 scratch）→ `textmd.log`
  - 网版 PDF：`tools/webpdf.py svg/ The-Lucerna-VOL4-en-ko.web.pdf` → `webpdf.log`
- KIT 已更新：`WEEKLY-KIT.md` §2 新 SHA + §5 新增第 6 条 delta 条目（Q73 speak→up，只此一改）

## 3. 修后 SHA

| 文件 | 字节 | SHA-256（修后） |
|---|---|---|
| `The-Lucerna-VOL4-en-ko.pdf`（印刷） | 32,386,301 | `c892247fe96290e8cc563ff72bdf2bfaa59ef9f73fd0ea0956391e4b4e696158` |
| `The-Lucerna-VOL4-en-ko.web.pdf`（网页） | 2,629,430 | `e8f6f94a8ed493cbd4d0016ae6cbf0294a392af17d1337749b0897e6d3544a31` |
| `2026-w47-en-ko.text.md` | 53,587 | `08d87476b499421c564a0931ab48bf7669463ea5f0a8a8ac9ac2a4545cab81f3` |
| `registry.json` | — | `56f6620b5741bce7b6c8474e4f691ccb3bd909d3809f6bdc5b0848ac54cf732a` |

（印版 PDF 字节数与修前相同纯属巧合——SHA 已变；网版 +4 字节；text.md −3 字节 = `speak`→`up` 的 3 字符差。）

## 4. Diff 证据（恰好 1 条 / 恰好 1 行）

- registry diff（`registry-pre.json` vs `registry-delta.json`，逐项比对）：**恰好 1 条**——
  - 前：`{'n': 73, 'page': 5, 'level': 'A2', 'type': '문장 완성', 'key': 'speak', 'note': 'speak up = 목소리를 내다'}`
  - 后：`{'n': 73, 'page': 5, 'level': 'A2', 'type': '문장 완성', 'key': 'up', 'note': 'speak up = 목소리를 내다'}`
  - 其余 149 条逐项相等；`registry == rerun registry: True`（见 `keycheck.log`）
- text.md diff（`text-pre.md` vs 新 text.md）：**恰好 1 行**（1151 行）——
  - 前：`73. [A2] 문장 완성 — speak (speak up = 목소리를 내다)`
  - 后：`73. [A2] 문장 완성 — up (speak up = 목소리를 내다)`
  - 题干行（589 行）`EXERCISE: Speak ___: tell a teacher.` 未动
- SVG 变化范围（`svg-pre.sha` vs `svg-post.sha`）：**仅 `p8-test.svg` 变化**（`c50c2edd…` → `007698e2…`），其余 7 页 SHA 与修前逐个一致。**此为正确且预期的范围**：Q73 键只出现在 P8 答案页，从不上 P5——P5 只印题干 `Speak ___` 空白 + `speak up` 注记，键本身从不印在 P5 上。因此 p5 与修前字节一致是预期状态，不是异常，无需返工（en-es delta 已证实同点：p8 含 `73. up`，p5 不变）。已 grep 核实 `p5-youth.svg` 内全部 `speak` 命中均为题干/正文/注释文字（`Speak ___`、`to speak up`、`Break the ___: speak up about bullying.`、`75. to speak up`、`Children (speak) up this week.`），无一处是 Q73 键。

## 5. Q73 四源一致（均为 `up`）

| 源 | 证据 |
|---|---|
| registry | n=73 `key: 'up'`，`note: 'speak up = 목소리를 내다'` 不变 |
| text.md | 答案区 1151 行 `73. [A2] 문장 완성 — up (speak up = 목소리를 내다)` |
| P8 印出键 | `svg/p8-test.svg` 含 `73. up`，`73. speak` 出现 0 次；`p8-extract.json` 抽取键 73 = `'up'`；印版 P8 答案块放大裁切 `render/crop-p8-answers.png` 目视可见 `73. up`（`72. rights … · 73. up · 74. d …`） |
| P5 题干 + 注释 | P5 印版目视：B 组 `73. Speak __: tell a teacher.`；页首注释 `해설 — bullying = 왕따 · to speak up = 목소리를 내다 · …`；同页 C 组 `75. to speak up`、D 组 Q79 `Children (speak) up this week.` 一致 |

完成句现为 **“Speak up: tell a teacher.”**——合语法，D4 已修。

## 6. D1/D2/D3 未退化（修后复核）

- D1：P4 标题 `Perth, One Year On: How Australia Kept the Ashes` 仍在；`Perth is winning` / `Ashes begin` / `second week in Perth` 在 P4 SVG 与 text.md 中仍为 0 处
- D2：registry 38=b、39=a、40=d、41=c；text.md 答案区与 P8 抽取键一致（见 keycheck）
- D3：P5 框题仍为短标题 `ODD SOCKS, IN NUMBERS　숫자로`；PIL 真墨余量 +29.5px（见 `ink_ko.log`，与 proof 逐字一致）

## 7. 全部门禁表

| 门 | 结果 | 证据 |
|---|---|---|
| run.py | **通过** | rc=0；`TOTAL exercises: 150`；`MODEL words: 82`；`OVERFLOW`/`TOO WIDE` 命中 0；全部 flow end y ≤ bottom（P8-keys 2205/2560；P2-ex 2532/2560）——与修前流末值逐项相同。`run.log` |
| render.py（印版 PDF） | **通过** | rc=0；8 张 cards + 印版 PDF 32,386,301 字节；SHA 见 §3。`render.log` |
| webpdf.py（网版 PDF） | **通过** | rc=0；2,629,430 字节，49,708 text bytes；SHA 见 §3；< 7 MB。`webpdf.log` |
| freeze baseline（版内构建目录） | **通过** | `freeze.py baseline --build <本版构建目录，含 run.py> --core-svg <本版/svg>`：**8/8 SVGs byte-identical**（我重建的 SVG 可复现）；工具完整性校验确认本版 shipped SVG 未被该轮改动。`freeze-baseline-edition.log` |
| freeze baseline（core 只读对照） | **通过** | core-en 构建目录只读对照：**8/8 SVGs byte-identical**，`core integrity: shipped core SVGs unchanged by the run (8 files re-hashed)`。`freeze-baseline-core.log` |
| freeze diff | **通过** | TOTAL 新增 CJK **2323**，与 proof 逐项一致（p1 213 / p2 316 / p3 162 / p4 170 / p5 166 / p6 183 / p7 471 / p8 642；Hangul 2309 + U+3000 9 + CJK 标点 5；新增汉字 0）。`freeze-diff.log/json` |
| occlusion 审计（真实命令，未用 --selftest） | **0 flags，通过** | `occlusion_audit.py <svg dir>`：`flag_count: 0`；工具自带自检 6 类阳性对照全部触发、干净对照静默。`occlusion.log/json` |
| p8 extract | **通过** | core 与本版各 60/150 带印刷注释，同一集合；抽取键 150 个，无缺失。`p8-extract.log/json`、`p8-extract-core.log/json` |
| p8 compare | **CLEAN，通过** | status CLEAN，missing=[]，extra_count=0，uncertain=[]；keydiff=[137, 138, 139, 140, 150]（读者语翻译键 + 开放题键，预期内，与 proof 一致）。`p8-compare.log/json`（已读 json 本体） |
| keycheck | **通过** | registry 150 条 = 重跑 registry；registry-vs-p8extract exact **149/150** + exc=[150]（抽取器截断长开放题键为 “열린 문제”，既定预期），mismatch=[]；registry-keys-vs-core **145/150**，diffs 仅 137–140、150（读者语改向）；Q38–41 = b/a/d/c；Q125 A、Q46 A、Q52 hosted、Q55 won；Q82/83/84 = B/C/A；noted set == core noted: True。`keycheck.log` |
| 印/网文字层逐页一致 | **通过** | `pdftotext -layout` 两版各 **107,720 字节**（修前 107,723，−3 = speak→up），`cmp` 字节一致；PyMuPDF 逐页 span 数一致（P1 227 / P2 259 / P3 216 / P4 229 / P5 197 / P6 218 / P7 242 / P8 273，两版相同）。`print.txt`、`web.txt`、`printweb.log` |
| P8 最小字号 | **通过** | PyMuPDF 实测印版 P8 最小 **10.125pt**（答案行，SVG 13.5px）≥ 10pt 任务线，亦 ≥ 9.75pt 底线；其余各页最小 11.625pt；网版同值。`printweb.log` |
| creambox（PIL 真墨） | **通过** | `creambox.py` 全版输出与 proof `creambox2.log` **逐字一致**（0 真溢出；所报负清除量 −37/−36/−24 皆为 +45px 窗口的已知假阳性，与 proof 同值）；`ink_ko.py` 输出与 proof `ink_ko.log` **逐字一致**：HAYMITCH 真墨余量 +2.5px、ODD SOCKS +29.5px。`creambox.log`、`ink_ko.log` |
| boxtitle（源级 + SVG） | **通过** | 源级 `boxtitle-ko.py` 输出与 proof `boxtitle2.log` **逐字一致**（12 项，11 项在 386.5px 预算内，HAYMITCH 401.9px 标 OVER——proof 已裁定为观察 O1，框实宽 404.5px，见下行）；SVG 扫 `sweep_svg_titles.py`：18/18，**overflows: 0，PASS**，HAYMITCH advance 余量 +2.6px / 真墨余量 +2.5px。`boxtitle.log`、`sweep_svg_titles.log`（注：源级脚本对 HAYMITCH 标 OVER 时 rc=1，属已知 O1 状态，与 proof 相同；PIL 真墨 0 溢出） |
| 8 页逐页目视 | **通过** | 印版 P1–P8 全页 + 网版 P1/P8 全页已目视（`render/print-p1.png`…`print-p8.png`、`web-p1.png`、`web-p8.png`，96dpi，PyMuPDF）；无溢出/重叠/压页脚；P8 答案块完整、未压页脚；P5 框题在框内；P3 HAYMITCH 末字 “기” 完整在框内。放大裁切 `render/crop-p8-answers.png`：`73. up` 清晰 |
| 150 题键与题干适配抽查 | **通过，0 flags** | 见 §8 |
| D5 字体 | **只记录，不判、不修** | 见 §9 |
| ABSTRACT | 未动 | 624 字节，SHA `927505ce05ef9c169d89d7d797530c9d2148fd6652963b44276483d3735bc81a`，与 proof 记录一致 |

## 8. 150 题键与题干适配抽查（Q73 教训：三源一致不够）

方法：用记录桩（stub bslib4，与 text.md 导出同一机制）执行全部 5 个 content 文件，逐项记录 (n, type, key, body)，再对每个含 `___` 的题干代入键做机械检查（键与空格前一词重复 = Speak/speak 类；填后出现相邻重词 = 双词类）+ 全部逐行人工复核。`stemfit2.py` / `stemfit2.log`（另有初版 `stemfit.py`，其重词检测有子串假阳性，已废弃，以 stemfit2 为准）。

- 覆盖：stub registry 150 条与真实 registry 键逐项相等；ex 项 121 个（含循环生成的 MCQ/阅读/句型/翻译/配对题）；含 `___` 的题干 **57 个**，机械 flags **0**；完形段落（Q112–119）与对话段落（Q145–149）各 1 个，代入键后全文通顺。
- 逐行复核（57 个填空题干 + 2 段）：全部键填入后合语法、合题意；Q73 现为 `Speak up: tell a teacher.`。其余示例：Q70 `Break the silence`、Q71 `wear odd socks`、Q72 `Every child has rights`、Q100 `The Democrats won the House.`、Q107 `“Democrats win the House” is a headline.`（标题现在时，正确）、完形 `On Tuesday morning… a call is… the counting continues… will meet… writes… will certify… wears… will watch`、对话 `Which row? … film about Haymitch … popcorn … show … Friday, November 20`。
- 仅作观察（不改，核心继承，与 proof1 O7 同类）：改写题 Q18/Q63 的公布键省去了题干末尾的状语（Q18 `Families will travel home.`，题干 `Families (travel) home for Thanksgiving.`；Q63 `India beat Australia by 295 runs.`，题干 `… in November 2024.`）。键本身合语法、时态转换正确，属可接受的简化改写；proof1 已对全部非 D4 题逐题核对无误，本 delta 不动。

## 9. D5 字体（只记录数量，不判、不修）

- 印版 PDF：43 个字体对象，全部已嵌入 + 子集化；字体族：NotoSansCJKsc（Bold/Regular）、NotoSerifCJKsc（Bold/Regular）、Newsreader16pt（Regular/Italic）、UnifrakturMaguntia、DejaVuSans；无未嵌入字体。`pdffonts-print.log`
- 网版 PDF：43 个字体对象，全部已嵌入 + 子集化；同一字体族，子集重命名为 Lucerna*。`pdffonts-web.log`
- 8 页目视中韩文字形完整、无缺字（tofu）；P6 练习选票 ☐ 正常渲染。
- freeze diff 新增 CJK 2323 = Hangul 2309 + U+3000 9 + CJK 标点 5，新增汉字 0。

## 10. 本轮改动文件清单（版内）

- 改动 1 行：`content56.py:49`（Q73 键 speak→up）
- 重建生成：`svg/p8-test.svg`（仅此 1 个 SVG 变化；其余 7 个 SVG 字节不变）、`cards/*.png`（render.py 重渲 8 张）、`The-Lucerna-VOL4-en-ko.pdf`、`The-Lucerna-VOL4-en-ko.web.pdf`、`registry.json`、`2026-w47-en-ko.text.md`、`WEEKLY-KIT.md`（§2 新 SHA + §5 第 6 条）
- 未动：`content12.py`、`content34.py`、`content7.py`、`content8.py`、`bslib4.py`、`svglib.py`、`run.py`、`render.py`、`dump_reg.py`、`ABSTRACT.txt`、`assets/`、其他所有版、核心、`tools/`

## 11. 结论

- **Delta 完成，全部 12 项门禁通过，D4（Q73）已修，可进 proof2。**
- 修前（proof1 (b) 状态）→ 修后三 SHA：
  - 印版：`ecad215e…22072cd` → `c892247f…e4b4e696158`
  - 网版：`5115ad3f…ca9e` → `e8f6f94a…544a31`
  - text.md：`e5633ac3…484ac` → `08d87476…cab81f3`
- 唯一残留观察：§7 boxtitle 源级口径的 HAYMITCH OVER（proof O1，PIL 真墨余量 +2.5px，框内，沿用）；§8 Q18/Q63 改写键省状语（proof1 O7 同类，不改）。
