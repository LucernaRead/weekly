# GATE-LOG — 2026-W47 es-de 独立复校（重建版，proof2）

复校员：独立复校员（与 es-de builder / es 核心 builder / 首轮复校员不同人）
工作目录：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-es-de2/`
日期：2026-11-11
解释器：`~/workspace/weekly-git/tools/venv/bin/python`（Pillow 13.0.0 / FreeType 2.14.3）；TMPDIR 用本目录下 `tmp/`（未写 /tmp）。
探针：`/dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 通；goals 侧真实写文件成功后开工。

## 0. 身份核对（自算 SHA-256；复核前后各测一次，均一致）

| 产物 | 字节 | SHA-256 |
|---|---|---|
| 印 `La-Lucerna-VOL4-es-de.pdf` | 3,503,120 | `65ebf6b7df8b07013d809427259a8b3504ac33e318bb9e0b61f72d7c9498fbca` |
| 网 `La-Lucerna-VOL4-es-de-web.pdf` | 889,914 | `2e39306ddd4424e8309aed9efe9e580920c75a826e5821c5e67f401f91c7ec9b` |
| text.md `2026-w47-es-de.text.md` | 45,311（1,802 行） | `81ff06563dd9332ab6af2b4d826f2dda6d7157d82983df01e484fa462c310a67` |
| core-es 印 | 17,212,955 | `2723a283d30b4114aa7946611126e05c1df08e2cd6e2019f120f1cc411e138b5`（复核前后未变） |
| core-es 网 | 1,410,471 | `c2473211d3fb4b930dceb3668237138dd24a2be363fc026b08251ac22185e235`（复核前后未变） |
| core-es text.md | — | `509c95fac1943b2bc380c85564cd467918648403175bc7bc80d58f4eb3948ddb`（复核前后未变） |

## 1. 机械门（全部自跑；rc 均为最终重跑值）

| 门 | 工具 / 日志 | rc | 结果 |
|---|---|---|---|
| run 重跑 | `run.py`（keycheck 内联，`de-keycheck.log`） | 0 | TOTAL 150；A2 50 / B1 72 / B2 28；分版 10/18/18/18/18/18/12/38；FLOW OVERFLOW 0；HEAD TOO WIDE 0 |
| render 重渲染 | `render.py`（`de-render.log`） | 0 | 印 PDF 字节复现（SHA `65ebf6b7…`）；网 PDF 见 O2 注记 |
| freeze 首检 | `tools/freeze.py baseline`（`de-freeze.log`） | 0 | **8/8 SVGs byte-identical**；shipped SVG 未变 |
| freeze diff / CJK | `tools/freeze.py diff`（`de-freeze-diff.json/.log`） | 0 | P1 +27/−38、P2 +50/−51、P3 +33/−30、P4 +34/−27、P5 +44/−47、P6 +19/−17、P7 +46/−46、P8 +162/−626；新增 CJK 合计 1 个 = U+3000（P1 刊头结构空格） |
| 遮挡审计 | `tools/occlusion_audit.py`（`de-occlusion.json/.log`） | 0 | 自检六类全触发；本版 **0 flags** |
| p8 extract | `tools/p8.py extract`（`de-p8-extract.json/.log`） | 0 | **150/150** |
| p8 compare | `tools/p8.py compare`（`de-p8-compare.json/.log`） | 0 | **CLEAN**；missing=[]；extra=0；keydiff=**[137, 138]**（已裁决 E 组德译） |
| creambox 全版扫描 | canonical `hidden_files/w47/tools/creambox.py`（`de-creambox.log`） | 0 | 末行基线全在盒内；below-window 均为下一节标题（+24..+44px 预期假阳性）；P7-TOOLBOX 3 盒 min inside +5.7 / min desc-clear −0.0 |
| creambox 真墨复测 | `creambox_diag.py` + `ink_all_runs.py`（`de-creambox-diag.log`、`de-ink-all-runs.log`） | 0 | 全部盒末行真墨 clearance 为正；最紧 P2 `ley.` +0.1、P5 `compara…pagar.` +0.1（3 倍放大裁图核实未出盒） |
| boxtitle 真墨 | `boxtitle_core.py`（`de-boxtitle.log`） | 0 | **0 OVERFLOW**；25 盒题全正，最小 +20.9；必查 2 处：`Der Plan` **+23.4**（旧 −21.4）、`Fehler` **+102.0**（旧 −30.8） |
| keycheck 150 | `keycheck_core.py`（`de-keycheck.log`、`keycheck-150.json`） | 0 | REG==提取键 149/150（仅 Q150 预期 `✓`）；P8-keys 终 y=**2506**（底 2560） |
| sweep | `sweep_de.py`（`de-sweep.log`） | 0 | box-vs-hline 0；bridge 20 条，orphans 0，widows 0 |
| 文字层 | pdftotext（`de-print.txt`、`de-web.txt`） | 0/0 | 印 == 网，逐字节一致，**111,448 字节**；网 PDF < 7 MB |
| P8 最小字号 | `minfont.py`（`de-minfont.log`） | 0 | P8 最小 **10.125pt**（≥9.75）；低于下限 0 处；376 个 Tm 条目 |
| P8 答案区逐行 | `check_p8keys.py`（`de-p8keys-check.log`） | 0 | 142 行，134 答案起首，多行答案 6 条（#1、#36、#44、#84、#139、#141），无碰撞 |

注：首轮 `gates.py` 驱动中 boxtitle/keycheck/sweep/minfont 4 项初次 rc=2 系路径错误（helper 拷在 `gates/` 子目录而驱动在根目录找），属我方搭建失误；修正后 4 项重跑 rc 均为 0，结果如上。`de-gates.json` 已修正为最终值。

## 2. 内容核查摘要（150 题 × 8 页，详见 PROOF-NOTE.md）

- 150 题逐题验算：三源交叉 REG==提取键 149/150（仅 Q150 预期 `✓`）、REG==核心键 147/150（仅已裁决 137/138 + Q150）；内容全部通过。
- 金句 8 条各出现 2 次；徽章计数与 REG 之差恰为 3 个区间徽章组；VOL.4 9 处 / VOL.5 3 处 / VOL.3 0 处；禁词全 0；§8.1 讲解词计数与 KIT 逐项一致；MODELO 手工计数 97 词。
- text.md 全文通读 1,802 行：`hasta el jueves` ×7、`antes del jueves` ×0、`sábado veo el derbi` ×1；CJK 表意字 0、U+3000 99 个。
- 目视：印版 P1–P8 + 网版 P1/P8 逐页目视（`render/`）；P2/P5 最紧盒 3 倍放大裁图核实（`zoom-p2-sabias.png`、`zoom-p5-votar.png`）。除观察项外无问题。
- ABSTRACT.txt：德文一行、无 ASCII 双引号、事实与本期一致。KIT 第 109 行 SHA 登记与实测逐字一致。

## 3. 结论

- 缺陷 **0 条**。结论 **(a)**。
- 观察项 4 条（PROOF-NOTE.md §7，不计缺陷）：O1 两处奶油盒真墨余量 +0.1px（在盒内）；O2 网 PDF 字节不可重现（工具链属性，已恢复交付件并 SHA 复核）；O3 D5 字体实测 537/636 纯拉丁 run（全周级已知待定项，只记录）；O4 「next Sunday」冻结指针过期（core-es/es-de 均为 0 次）。
- 未改任何生产文件，未 commit，未 push。唯一写操作为门禁重渲染改写网 PDF，已用 `backup-shipped/` 备份原样恢复并 SHA 复核；印 PDF 重渲染字节一致，8 枚 SVG 重渲染前后 SHA 一致。
