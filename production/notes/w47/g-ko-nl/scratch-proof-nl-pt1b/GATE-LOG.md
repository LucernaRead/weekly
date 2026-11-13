# GATE-LOG — 2026-W47 · nl → pt · proof1 机械门实跑证据（delta build 4）

复校员独立实跑，不信 KIT，只信自己跑的结果。全部命令用 `tools/venv/bin/python`；
TMPDIR 全程指向本 scratch 下 `tmp/`（系统 /tmp 512M 未用）。
工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-nl-pt1b/`。
源码见 `occlusion.json`、`p8-extract.json`、`p8-compare.json`、`freeze-diff.json`、`freeze-baseline/`、
`creambox-all.log`、`boxtitle2.log`、`raster-checks.log`、`strip-probe.log`、`p7-adjudicate.log`、
`p7-staging-compare.log`、`textlayer.log`、`p1-posdiff.log`、`keycheck.log`、`reg-dump.json`、
`orphan.log`、`style11.log`、`content-verify.log`、`print.txt`、`web.txt`、`render-p1.png`…`render-p8.png`、
`crop-p7-title.png`、`crop-p4-d11.png`、`crop-p8-ahead.png`。
自写脚本：`boxtitle_scan.py`（本版盒坐标重推导；HEAD 带区按 `bslib4.py:72` 下划线几何排除下划线、
P8 刊头带底 182 px 排除刊头带）、`keycheck.py`（三源键比对）。

## §0 身份核对（磁盘为准）

- 探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` → `e69de29bb2d1d6434b8b29ae775ad8c2e48c5391`，RC=0；
  scratch 写入探针文件成功（`probe.txt`）。磁盘 59G 可用。
- 印 PDF `De-Lucerna-VOL4-nl-pt.pdf`：SHA `dd74de0a45556e96fdfcc216a9d249bbae577ace249bfbc256dd564ef6e5113e`，
  12,672,019 字节——**与任务一致**。
- 网 PDF `De-Lucerna-VOL4-nl-pt-web.pdf`：SHA `4e795b31f65273524128656f1a0a6064ba0f18efa93a29c191f15a2f58bf5e6b`，
  1,618,464 字节——**与任务一致**。
- text.md `2026-w47-nl-pt.text.md`：SHA `7e6b0c54dcb2f0025b90bd6074407d32ec24c8f6d78a018e4b49ae9d621f7d8f`，
  47,209 字节——**与任务一致**。
- 任务数字与磁盘无出入，本节无 §0 差异。
- 补充：与 build-3 staging（`production/2026-w47/fanout-nl/2026-w47-nl-pt/`）的 diff —
  text.md 仅 415 行不同（D9 `kort`）；SVG 仅 `p4-sport.svg`（D11）与 `p8-toets.svg`（D9）不同，
  其余 6 页字节一致。

## §1 run.py 复现（clean-copy 重跑，非生产目录内运行）

- 方法：`cp -a` 整版到本 scratch `work/ed/`（仅去 `__pycache__`/`cards/`），在副本内跑
  `tools/venv/bin/python run.py`，逐文件 sha256 比对交付 SVG。生产目录内未执行 run.py。
- 结果：**exit 0，TOTAL 150**，by page 10/18/18/18/18/18/12/38，A2 46 / B1 73 / B2 31，范文 81 词；
  **0 FLOW OVERFLOW / TOO WIDE 警告**（`repro-run.log` 全文 grep 0 命中）；
  `flow[P1-headline] ended col 2/2 y=1465`、`flow[P8-keys] ended col 3/3 y=2550 (bottom 2560)`、
  `P4 col3 ends 1229.6`（旧 1202.6）。
- SVG 比对：**8/8 字节一致**（`repro-compare.txt`，逐文件名比对，diff 行数每页均为 0）。
  诚实记录：第一版比对脚本因排序粘贴错位曾报 8/8 DIFF，已废弃；逐文件 `diff` + 逐文件名 sha256
  两法复核均为 8/8 SAME，上面为准。

## §2 几何遮挡审计（tools/occlusion_audit.py）

- 命令：`./tools/venv/bin/python tools/occlusion_audit.py production/2026-w47/2026-w47-nl-pt/svg --core production/2026-w47/core-nl/svg --json occlusion.json`
- 结果：**0 flags**（edition 与 core 均为 0，NEW vs core 0）；合成自检通过
  （6 类 planted flags 全触发，clean 对照静默）。RC=0（`occlusion.log` / `occlusion.json`）。
- 局限（任务已提示）：该工具只核查带边框盒的 BOXTITLE 类；无边框奶油盒标题横向溢出不在其覆盖内——
  由 §3–§4 的独立实测检出/排除，不得以 occlusion 0 为放过理由。
  本轮 0 flags，故无 OVERLAP 须裁切图 adjudicate；P7 标题的 ±1 px 边缘见 §3（O1）与裁切图证据。

## §3 框标题 / 版心右缘实测（交付 PDF 光栅像素为准 + PIL 交叉）

- 自写脚本 `boxtitle_scan.py`：标题来源 = 本版源码 `Flow.head` 调用的 38 个字符串（`content12.py:7` +
  `content34.py:10` + `content56.py:10` + `content7.py:3` + `content8.py:8`）+ SVG 内 cream rect
  （fill `#f0eee5`）含 700-weight 标题的 21 个盒；盒坐标与语言标记均按本版重推导，未用任何他版硬编码坐标。
  测量面 = 交付印 PDF 150 dpi 光栅（scale 1.5625 raster-px / SVG-px）；HEAD 带区按 `bslib4.py:70–73`
  （`shead` 下划线在基线 +13 px，线宽 2）封顶至基线 +11 px，P8 A-head 带顶另按刊头带底 182 px 夹住，
  下划线与刊头带均不计入墨迹。
- 结果：**共 59 个标题（38 Flow.head + 21 奶油盒标题），外缘 OVER 1 处**（见下），其余 58 个外缘余量 ≥ +9.8 px。
  最紧的 8 个：P7 BOX「HET WOORD　PALAVRA DA SEMANA」−1.0；P6 BOX「VOOR OF TEGEN?　A FAVOR / CONTRA」+9.8；
  P2 BOX「ZO ONTHOUD JE HET　LEMBRA-TE」+14.4；P6 BOX「DE GRAFIEK　DADOS DE TREINO」+22.0；
  P2 HEAD「DRIE DINGEN VOOR 5 DECEMBER」+24.0；P1 BOX「IN DEZE EDITIE　NESTA EDIÇÃO」+29.7；
  P1 BOX「DE WEEK IN CIJFERS　NÚMEROS」+37.5；P2 BOX「GEDICHT」+41.8。
- **唯一 OVER-OUTER：P7「HET WOORD　PALAVRA DA SEMANA」−1.0 px（150 dpi，阈值 <200）**——裁决为观察项 O1，
  非缺陷（PROOF-NOTE 末节）：(a) PIL `getbbox`（Noto Sans CJK SC Bold 23 pt，4× 采样）墨右 1861.25 px，
  余量 **+0.75 px**，advance 右缘 1861.08 px——字形度量法判在内；(b) 300 dpi 双法复测 solid 墨（<128，
  最暗 min-channel 31）最右 1862.96 px，与 150 dpi 一致，确为抗锯齿边缘口径差异，非测量错误；
  (c) build-3 staging 的 P7 在 300 dpi 下与本版光栅**逐像素相同**（`p7-staging-compare.log`），
  几何与上一轮 proof1 已裁定的 O3 完全相同，**无回归**；(d) 末字 “A” 完整未裁切（`crop-p7-title.png` 目视），
  盒为无边框 fill-only，墨迹未与任何元素或可见边框重叠。
- **P8「A　VUL DE KRONIEK IN」**：墨迹 x 87.7–320.6 px，外缘余量 **+189.9 px**（栏边 510.5）；
  下划线 y=214 按设计止于栏边；刊头带底 182 与字顶无交叠（`crop-p8-ahead.png` 目视）。
  nl-ko 版同标题 −26.5 px 的情形在本版未复现。第一版扫描曾因带区误触刊头带报假 OVER，已按上述几何修正带区后消除。
- **D1 回归**：P6「VOOR OF TEGEN?　A FAVOR / CONTRA」外缘余量 **+9.8 px**，在内。
- **D2 回归**：P2 选项 c「c. eten voor Sinterklaas' paard」（`p2-leven.svg` x=1473.5, y=2233, 23 pt）
  真墨右缘 1793.92 px，余量 **+68.08 px**（`raster-checks.log`）。
- **D11 回归**：P4 盒底 1229.6，末行「18:45 uur.」最低墨迹 y=1209.60，**墨迹余量 +20.00 px**；
  盒底下 7 px 条带 0 非纸像素（`raster-checks.log`，裁切图 `crop-p4-d11.png`）。

## §4 正典 creambox.py 全版扫描 + 盒底像素复核

- 命令：`./tools/venv/bin/python <goals>/hidden_files/w47/tools/creambox.py production/2026-w47/2026-w47-nl-pt/svg/*.svg`
  → `creambox-all.log`（312 行）。RC=0。
- 结果：仅 2 处「last baseline」负值，均为盒下相邻标题的已知假阳性：
  - P1 IN DEZE EDITIE 盒（bottom 1652）：盒内末行 baseline 1636，clearance +16.0，desc-clear +9.7；
    窗内下一行「HET WOORD VAN DE WEEK」baseline 1676（+24.0）。
  - P2 四词盒组（bottom 1768）：盒内末行 baseline 1756.6，clearance +11.4，desc-clear +5.7；
    窗内下一行「Let op: schrijf je gedicht…」baseline 1800（+32.0）。
- **P7 toolbox 实测**：3 个盒，min inside clearance **+13.1**，min desc-clear **+7.1**
  （末行「de final.」baseline 1327.4，盒底 1340.5）。
- 盒底像素复核（交付 PDF 150 dpi 光栅，`strip-probe.log`）：

  | 位置 | 盒底 | 最低墨点 | 墨底余量 | 盒底下 7 px 条带 |
  |---|---|---|---|---|
  | P2 EN JIJ 末行 | 1447.8 px | 1444.48 px | **+3.32 px** | 0 非纸像素 |
  | P5 EN JIJ 末行 | 994.5 px | 988.80 px | **+5.70 px** | 0 非纸像素 |
  | P3 SINTERKLAAS 盒 | 1106.6 px | 1090.56 px | **+16.04 px** | — |
  | P7 toolbox 盒 1 | 1011.5 px | 998.40 px | **+13.10 px** | 0 非纸像素 |
  | P7 toolbox 盒 2 | 1340.5 px | 1327.36 px | **+13.14 px** | 0 非纸像素 |
  | P7 toolbox 盒 3 | 1927.0 px | 1902.08 px | **+24.92 px** | 0 非纸像素 |
  | P4 HET PROGRAMMA 盒（D11） | 1229.6 px | 1209.60 px | **+20.00 px** | 0 非纸像素 |

  P2 EN JIJ 墨底余量由 build-3 的 +0.9 px 升至 +3.32 px（re-fanout fix15 +2 px 底垫见效）；
  P5 desc-clear −0.3 为估计值，像素实测 +5.70 px 在内。

## §5 p8 compare（显式 --core-p8/--edition-p8；--total 150）

- 命令：`p8.py compare --core-p8 <core-nl>/svg/p8-toets.svg --edition-p8 <edition>/svg/p8-toets.svg --total 150`
- 结果：**CLEAN**，core 150 noted / edition 150 noted，missing=[]，extra=0，uncertain=[]，**keydiff=[137, 138]**。RC=0。
- keydiff 裁决：137、138 为 E 节翻译题（NL→PT），键合法重定向到读者语；键本身正确（137「As notícias do
  Sinterklaas passam todos os dias às 18:00.」；138「Os dois primeiros passam aos quartos de final.」）。
  139、140（PT→NL）键与核心一致。非缺陷。
- `p8.py extract --p8 <edition>/svg/p8-toets.svg --total 150`：**noted set = 150 of 150**。RC=0。
- P8 chips：edition {A2: 8, B1: 24, B2: 3} = core {A2: 8, B1: 24, B2: 3}（`content-verify.log`）。

## §6 freeze / freeze diff 8/8

- `freeze.py baseline --build production/2026-w47/core-nl --core-svg production/2026-w47/core-nl/svg --out <scratch>/freeze-baseline`：
  **8/8 SVG byte-identical**，核心 8 文件重哈希确认未被改动（"core integrity: shipped core SVGs unchanged"）。
  `--core-svg` 指向 `core-nl/svg` 子目录；`freeze-baseline/build-copy/` 经核实确为核心版
  （含核心 `2026-w47-nl-zh-cn.text.md`、`FIX-LOG.md`、`De-Lucerna-VOL4.pdf`；其 `content8.py` 含 3 处「答案」、
  1 处「kort gedicht」——核心 fix4 后的中文版特征，非本版自比）。RC=0（`freeze-baseline.log`）。
- `freeze.py diff --core-svg <core-nl>/svg --edition-svg <edition>/svg`：p1 +27/−48 … p8 +183/−676；
  **新增 CJK 仅 7 个 U+3000**（p1 为 0，其余每页 1 个）。U+3000 是 SOP §1.1 规定的全角空格分隔符
  （「不用·做分隔，用全角空格」），非中文文本。RC=0（`freeze-diff.log` / `freeze-diff.json`）。
- 移除串核查：全部含拉丁字母的移除串，其词元均在同页新增串中重现；惟二例外已裁定：（a）刊头
  「LUCERNA DUTCH WEEKLY」→ 葡语刊头副标（fan-out 设计）；（b）「perfectum」→ 葡语「perfeito」
  （P8 答案注 40/42），讲解层合法翻译，非核心丢失。

## §7 三源 keycheck 150/150（逐题手验 + 程序比对）

- 方法：registry（clean-copy 重跑 `work/ed/` 导出，`reg-dump.json`，150 条）× P8 印刷键
  （`p8-extract.json` 的 `keys`）× text.md 答案（`keycheck.py` 解析 `— Resposta:` / `(Resposta x`）。
- 结果：**149/149 MATCH，DIFF=[]，MISSING=[]**（`keycheck.log`）；仅 Q150 不同（开放写作例外：
  P8 键 `✓`，text.md 载 81 词 Tekstmodel，registry 为开放题占位）。
  配对键 25–28 = d/c/a/b，141–144 = b/c/d/a，三源一致。
  **Q140 三源 MATCH**：`Ik maak een surprise met een kort gedicht.`（registry / P8 / text.md:415）。
  （注：首版脚本漏配对题行曾报 8 处“差异”，系解析器要求行首 `[` 所致；修正后重跑 0 差异，修正只动了
  scratch 脚本，未动任何版内文件。）
- 语义逐题手验见 PROOF-NOTE：算术重算、范文计词 81、编号连续性、分布与级别计数均与 `run.py` 一致。

## §8 印/网文字层比对（只比文字层，不比 SHA/字节）

- `pdftotext -layout` 印版 104,925 B / 网版 104,925 B（字节数相等；raw diff rc=0，**逐字节相同**）。
- PyMuPDF 位置排序提取：两版各 **7,985 token**，8 页逐页 msdiff 0；
  posdiff 0（P3–P8），P1 posdiff 2——仅刊头 “De / Lucerna” 两词 x 坐标 0.2 pt 舍入差
  （print (394.0, 81.3) vs web (393.8, 81.3)；词与词序相同，`p1-posdiff.log`），属字体子集化提取舍入，
  非内容差异。逐页 tokens：P1 822/822、P2 826/826、P3 729/729、P4 739/739、P5 805/805、
  P6 756/756、P7 915/915、P8 2393/2393。
- 斜体：印版 1 处 / 网版 1 处（P1 «de groepswinst»，16.12 pt），D5 已修好。

## §9 P8 最小字号实测

- PyMuPDF 逐 span（P8，387 个 span）：**最小 10.12 pt**（175 个 span），中位 10.35 pt；
  全书最小亦为 10.12 pt。SOP §1.1 让步阶梯允许降至 9.75 pt，10.12 合规，非缺陷（`textlayer.log`）。

## §10 孤儿标点 + E 节 type 标签本地化 + text.md 残留中文 + ABSTRACT.txt + §1.1

- 孤儿标点横扫（重建 SVG，1618 个 `<text>` 节点）：独行标点 **0**，行首标点 **0**（`orphan.log`）。
- text.md 答案标记未本地化：CJK「答案」**0 处**；「— Resposta:」142 处 + 「(Resposta」8 处 = 150 处（D3 已修好）。
- E 节 type 标签本地化：text.md 内联标签全葡语（complete→`Completa a frase` 65、choice→`Escolha múltipla` 44、
  cloze choice→`Cloze` 13、make sentences→`Forma frases` 8、true or false→`Verdadeiro ou falso` 7、
  translate→`Traduzir` 4、matching→`Relaciona as palavras` 2、writing→`Escrita` 1）；
  印刷版 SVG `Complete` ×59 为葡语命令式（D4 已修好，见 PROOF-NOTE）。
- ABSTRACT.txt：葡语单行 320 字节，含「Lucerna」「VOL.4」、目标语名、A2–B2、150 题；0 处 ASCII 双引号。
- §1.1 SVG 审计（`style11.log`）：纸色 `#fbfaf6` 全页底 8/8；VOL.5 = 5 = 核心；“VOL. 4” 0 次；
  fill 调色板仅 §1.1 调色板 + 刊头蛾标品牌色（#34483A、#4D72B4、#7898CD、#D7B257 等），无 #b3a06a；
  stroked rect 0；最深背景 #37402f；字体 Newsreader 971 / Noto Sans CJK SC 646 / Noto Serif CJK SC 25 /
  UnifrakturMaguntia 1（刊头）。
- 弯引号：SVG 全版 « » 成对（P1 2/2、P2 2/2、P7 30/30、P8 2/2）；text.md 直引号全为荷兰语 `'s` 属格，
  与核心一致。无误用。
- gloss 核查：6 条 gloss 行共 29 个注释词，全部真实出现在正文里（`content-verify.log`，缺失 0；
  脚本另对 8 条金句行计 37 个 “>” 条目一并核查通过）。
  范文 81 词（80–100 内）。P1 目录 7 行与各版真实标题对应，页码正确。
