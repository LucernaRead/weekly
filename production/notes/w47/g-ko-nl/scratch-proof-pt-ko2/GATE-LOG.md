# GATE-LOG — 2026-w47-pt-ko proof1（独立重跑，2026-11-11）

复校员：独立复校（proof1）。对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-pt-ko/`（重建版）。
解释器（全部步骤）：`~/workspace/weekly-git/tools/venv/bin/python`（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3）。
 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-pt-ko2/`。
生产目录只读：所有会写的步骤（run/gates/render/webpdf/keycheck）均在 `scratch-proof-pt-ko2/build/2026-w47-pt-ko`
副本里跑；只读门禁直接读生产文件。交付文件 SHA 复校前后一致（见文末）。

注：freeze baseline 的调用按 KIT §7 与 `gates_pt.py` 的既定用法：
`freeze.py baseline --build <版目录> --core-svg <版本身 svg 目录>`（--build 是构建该版 SVG 的源码目录，
--core-svg 是待比对的已交付 SVG 目录；与重建者 `ko-freeze.log` 的命令与哈希逐项相同）。
任务书括号"（--build 指真核心 svg 目录，不要指版目录）"与此既定用法字面不合——按既定用法执行并记录在案。

## 0. 探针与 SHA

| 项 | 结果 |
|---|---|
| `ls /dev/null` | 存在 |
| `git hash-object -w` 探针文件 | 能通（`9daeafb9…`） |
| scratch 写文件 | 成功（`probe.txt`） |
| SHA（复校前） | 印 `ac839d227acb506f71ccfd05a1b63915a22cca91c6bcb0cec0cecd025c2de6e1` / 17,185,806 B；网 `f505a301e3cb22645aba7131fb61d2f6f445d41ff670bfb3aa63dcebb071c38f` / 1,431,508 B；文 `fe14281fdd24abcfc527d359d707aef97b6d92bc9d602cd38ce1a4fbf6c791c4` / 37,823 B——与 FANOUT-REPORT-pt.md §1 全值一致 |
| SHA（复校后，全部工作结束时） | 三者逐字节相同（见文末复核命令输出） |

## 1. run.py（scratch 副本）—— rc=0，TOTAL 150，0 溢出

命令：`cd scratch-proof-pt-ko2/build/2026-w47-pt-ko && venv/bin/python -u run.py` → `logs/run.log`。
- rc=0。`TOTAL 150`；by level `{'A2': 48, 'B1': 71, 'B2': 31}`；
  by page `{1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；model words 88。
- 溢出：`grep -c OVERFLOW logs/run.log` = 0；`grep -i overflow` 无行。
- 副产物：scratch 副本重建的 SVG 与交付 SVG 8/8 字节一致（`logs/svg-copy.sha` vs `logs/svg-prod.sha`，`diff` 无输出）。

## 2. gates.py（scratch 副本）—— 16/16，rc=0

命令：同目录 `venv/bin/python -u gates.py` → `logs/gates.log`。16 行 `[PASS]`，`FAILURES: none`，rc=0。
逐项：P1 VOL.4+日期；P1 副题；页脚+页码 8/8；无 VOL.3 残留；截稿注+决赛命名；P1 masthead ≤1820；
同基线墨碰撞 0；页框墨穿越 0（边距 L/R/T/B = 47.0/47.5/35.0/33.0）；P6 图表标签覆盖 0%；
gloss 29 项枚举；gloss 词干 0 缺失；P7 引言 8 条 2×+页码+韩语；读者角 5/5；图片+注 5/5；
P7 引言清于预览框（max 基线 2292.17）；P1 标题 41 字符（≤56）。

## 3. occlusion_audit（真实审计，未传 --selftest）—— 0 flags，rc=0

命令：`venv/bin/python tools/occlusion_audit.py <生产版 svg 目录> --json logs/occlusion.json` → `logs/occlusion.log`。
- 输出：`<生产版 svg>： 0 flags`（rc=0）。注：工具自身输出首行含其内置 selftest 自检行（`selftest OK: planted
  classes fired {...}; clean controls silent`），该行是工具每次运行的固有输出，并非我传入 `--selftest`。

## 4. p8 extract / compare —— 150/150，CLEAN，rc=0

- extract：`venv/bin/python tools/p8.py extract --p8 <生产版 svg>/p8-avaliacao.svg --total 150 --json logs/p8-extract.json`
  → `logs/p8-extract.log`：`noted set = 150 of 150 (parse: lines)`，rc=0。
- compare：`... tools/p8.py compare --core-p8 <core-pt>/svg/p8-avaliacao.svg --edition-p8 <生产版 svg>/p8-avaliacao.svg
  --total 150 --json logs/p8-compare.json` → `logs/p8-compare.log`：
  `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`，rc=0。
  137/138 为预期：两题翻译答案指向韩语（137 `11월 20일 금요일은 전국 공휴일이에요.`；
  138 `파우메이라스는 승부차기에서 5–4로 이겼어요.`），已逐题手验正确（PROOF-NOTE §4）。

## 5. freeze baseline —— 8/8，rc=0

命令：`venv/bin/python tools/freeze.py baseline --build <生产版目录> --core-svg <生产版 svg 目录>
--out scratch-proof-pt-ko2/freeze-pt-ko` → `logs/freeze.log`。
- `runtime: ... Pillow 13.0.0 | FreeType 2.14.3`；`baseline: 8/8 SVGs byte-identical`；
  8 项 OK（p1 `8172493e…`、p2 `9e2484f6…`、p3 `fe431a45…`、p4 `6de55aeb…`、p5 `16c98abd…`、
  p6 `483a1661…`、p7 `5ead6512…`、p8 `4f16f090…`，与重建者 `ko-freeze.log` 逐项相同）；
  `core integrity: shipped core SVGs unchanged by the run`。rc=0。

## 6. freeze diff（核心对照）—— rc=0

命令：`venv/bin/python tools/freeze.py diff --core-svg <core-pt>/svg --edition-svg <生产版 svg>
--json logs/freeze-diff.json` → `logs/freeze-diff.log`。
- 每页增减字符串：p1 +52/-30、p2 +35/-33、p3 +29/-29、p4 +28/-26、p5 +85/-41、p6 +21/-21、p7 +49/-46、p8 +923/-481。
- TOTAL added CJK characters: 3403（均为韩语解释层字符 + 每页 1 个 U+3000 家具分隔符；目标语文本无新增）。
  ko 豁免说明：Hangul 计入该工具的 CJK 计数器，属预期；首轮为 3408，本轮 3403（差 5 来自 D5 gloss 换行与 D6 间隔）。

## 7. creambox / creambox_diag（PIL 真墨）—— 0 溢出

- creambox.py（naive 扫描）：`logs/creambox.log`，rc=0；6 处负 clearance：
  P1 y=786（-37.0）、P1 y=1874（-38.0）、P2 y=1618（-32.0）、P3 y=200（-37.0）、P6 y=1594（-42.0 ×2）。
- creambox_diag.py（真墨裁决）：`logs/creambox-diag.log`，rc=0；**0 处负 ink-clearance**。
  6 处负值全部是 +45px 窗口捕到的框外行（section head / 下一栏标题，owner-rect=NONE），各框 OWN 末行真墨余量
  最小 +2.4px（P2 y=545 `휴일이 있나요? …`，ink-clearance +2.4；其余 +2.5 起）。**真墨 0 溢出。**

## 8. boxtitle（PIL 真墨）—— 31 框全清

命令：`venv/bin/python scratch-refanout-pt/boxtitle_core.py <生产版 svg 目录>` → `logs/boxtitle.log`，rc=0。
- 31 个框标题全部 `clear=+`，最小 clearance +18.2px（P3 gloss 标题 `해설 — o quilombo …`），
  其次 +22.2（P2 SÁB 21 栏目标题）、+26.3。无负值。

## 9. keycheck —— 149/150（唯一不符 Q150，预期），rc=0（推导）

方法：复制 `keycheck_core.py` 到本 scratch（`keycheck-mine.py`，输出写本 scratch 的 `keycheck-150.json`，
不覆盖重建者文件），对 **scratch 构建副本**运行（该工具会在目标目录内重跑 run.py，故绝不在生产目录跑）。
- `logs/keycheck.log`：`REG entries: 150; p8extract keys: 150`；`exact match: 149/150`；
  唯一 MISMATCH：`n=150 page=8 type=작문: key='（자유 과제 — 모범 글은 아래에 있어요）' extracted='✓'`。
- `keycheck-150.json` 核验：150 行，不符项仅此 1 项且为 n=150、extracted=`✓`——符合工具的
  expected_only 规则，故 rc=0（该次运行的 rc 因服务重启未落盘，以日志 + json 逐项推导；见下注）。
- 注：本次 keycheck 运行时值一次服务重启，`logs/keycheck.log` 完整落盘（末行 `wrote .../keycheck-150.json`），
  故以日志与 json 为准推导 rc。

## 10. sweep（桥孤儿 / 框-线 / 桥寡行）—— box-vs-hline 0，orphans 0，widows 1

命令：`venv/bin/python scratch-refanout-pt/sweep_de.py <生产版目录>`（只读）→ `logs/sweep.log`，rc=0（该工具恒 exit 0，
rc 不代表 0 发现——以计数为准）。
- box-vs-hline flags: 0；bridges found: 20；bridge orphans: 0；
- **bridge widows: 1**：`WIDOW content7.py: 'quando、se、quem 뒤에는 접속법 미래가 와요: sair、for、tiver（공식 정답을 기다리는 문법' -> line '.'`
  （即 PROOF-NOTE F1；重建者 `ko-sweep.log` 同为 1，与其报告"0"矛盾。）

## 11. 印/网文字层 —— 逐字节一致（105,505 B）

命令：`pdftotext -layout` 各印/网 PDF → `logs/print.txt` / `logs/web.txt`，rc 均为 0；
`cmp` 无输出：**PRINT/WEB TEXT BYTE-IDENTICAL**，各 105,505 字节。
独立 fitz 计数：italic span 印 1 = 网 1（同文 `« consciência »`）。

## 12. minfont（印 PDF P8）—— 最小 10.125pt，0 项低于 9.75pt

命令：`venv/bin/python scratch-refanout-pt/minfont.py <生产版印 PDF>` → `logs/minfont.log`，rc=0。
- `P8 min effective font size = 10.125 pt (n=805)`；`below 9.75pt: 0`。

## 13. check_final（词 multiset + P8 字号）—— diff 0，7052/7052，rc=0

命令：cwd=本 scratch，`venv/bin/python scratch-refanout-pt/check_final.py <生产版目录>`
→ `logs/check-final.log`，rc=0（输出写本 scratch 的 `ko-textdiff.json` / `ko-p8size.json`）。
- `pages print=8 web=8`；`words print=7052 web=7052 multiset-diff=0`；`diff sample: []`；
  P8 answer-region span sizes `[10.125, 10.5, 14.625, 18.75]`，count 610，min 10.125；
  `word bbox height: min 10.125 median 10.125 max 27.15`。

## 14. render.py（scratch 副本）—— rc=0；重渲印 PDF 与交付逐字节相同

命令：`cd scratch-proof-pt-ko2/build/2026-w47-pt-ko && venv/bin/python -u render.py` → `logs/render.log`，rc=0。
- 注：首次运行被服务重启打断（停在 p7 卡片）；重跑完成，`print PDF: .../A-Lucerna-VOL4.pdf 17185806`。
- SHA：重渲印 PDF `ac839d227acb506f71ccfd05a1b63915a22cca91c6bcb0cec0cecd025c2de6e1` =
  交付印 PDF SHA，**逐字节相同**；字节数 17,185,806。
- 卡片：`build/2026-w47-pt-ko/cards/*.png`（1950×2700，8 页）为目视依据。

## 15. webpdf.py（scratch 副本，只重渲对比）—— rc=0；文字层与交付网 PDF 逐字节一致

命令：`venv/bin/python tools/webpdf.py <scratch 副本 svg> scratch-proof-pt-ko2/webtest/A-Lucerna-VOL4-web.pdf`
→ `logs/webpdf.log`，rc=0；`WROTE ...: 1431506 bytes, 47443 text bytes`。
- 重渲网 PDF：1,431,506 字节，SHA `6dee364566e805f550cae5718170f8c068ce8d9b30cae1a26cfc46d368c1b3ea`——
  与交付网 PDF（1,431,508 字节，`f505a301…`）SHA/字节数不等，**属已知逐次浮动，非缺陷**（任务书已明示）。
- 文字层：`pdftotext -layout` 重渲网 PDF → `logs/webtest.txt`，`cmp` 对交付网 PDF 的 `logs/web.txt` 无输出，
  **105,505 字节逐字节一致**。

## 16. D5 gloss PIL 实测 —— 4 行，末行右余 +280.5、底余 +42.7，无溢出

命令：`venv/bin/python scratch-refanout-pt/gloss_probe.py <生产版目录>` → `logs/gloss-probe.log`，rc=0。
- 框 rect#0 x=989.0 y=270.48 w=422.5 h=175.4，bottom=445.88，right=1411.5，lines=4。
- 各行：309.0 右余 +94.5；338.7 右余 +43.5；368.4 右余 +31.5（`título 우승/타이틀 · a pausa 쉬는 기간 ·`）；
  398.2 末行右余 +280.5、底余 +42.7（`a taça 트로피.`）。
- `GLOSS VERDICT: lines=4 last-line right clear +280.5 last-line bottom clear +42.7 overflow=no`。
- 字体（仅记录）：框内 4 个 `<text>` 全为 `Noto Sans CJK SC 20.5`（1 种字体）。

## 17. 声称点专项实测

| 项 | 命令/方法 | 实测值 |
|---|---|---|
| SÁB 21 | SVG 文本提取（P2）+ 特写 `render/crop-p2-sab21.png` | `토요일 16:30, 파우메이라스 대` / `플라멩구`（y=1736.5/1761.2） |
| Q65 | P8 答案区行重建 + `logs/p8-extract.json`（key `B`） | `65. B — 2일 차는 자연과학과 수학, 13:30–18:30`（y=2224.1） |
| D6 冒号 | 机制文件与 MECH 逐字节同 + 同一 core-pt，复跑 transform 步骤 5 改计数（`d6/`） | **24 处**（content34 5、content56 11、content7 8）；新 SVG 韩语冒号无空格仅剩时间表达式 |
| D8 逗号 | 全版 SVG + text.md 全角扫描 | `，`=0、`：`=0；首轮唯一 `，`（P8 Q68）已改拉丁逗号；但留 `,TRI` 无空格 1 处（F4） |
| text.md 5 行差异 | `diff <首轮备份 text.md> <本版 text.md>` | 恰 5 行：L215、L280、L363、L393、L433 |
| 词数 7,052 | §13 check_final | 7052 / 7052，diff 0 |
| P7 桥 / P1 数字框孤儿行 | SVG 行重建 + 特写 + 全页目视 | P7 `.`（y=654.4）、P1 `）`（y=990.2）——见 PROOF-NOTE F1/F2 |
| 行首 `:` | 逐栏逐行扫描 | P7 y=624.7、P5 y=664.2（F3） |
| 150 题手验 | `qtable.md`（题干 text.md + 键 REG + 提取值）逐题核对 | 150/150 键正确；唯一键/提取不符为 Q150（预期 `✓`） |
| hand patch 盘点 | `ko-classify.json` 读数 + 标记分布 + content7/8 抽查 | 52 KEEP / 0 REVERT / 0 丢失；25 处 D6/D8 机制 + 21 处 fix1 系 + 6 处证明修复标记 |
| KIT §6 item 6 扫描重跑 | 新 SVG 文本元素扫描 | `?두` 0、`?Write` 0、`..`（除 `...` 外）0、`( (` 0、` :` 0、CJK（除 U+3000）3 字（三/色/蛾，logo）、`。`0、`！`0 |

## 18. 目视（8 页全页 + 6 处特写）

依据：`build/2026-w47-pt-ko/cards/*.png`（与交付 SVG 字节一致的 scratch 重建渲染）及 `render/crop-*.png`（2× 特写）。
- P1：除 F2 外干净。P2：干净。P3：干净（E VOCÊ `있나`/`요?` 为音节断行，合法）。
  P4：干净（gloss 框无溢出）。P5：除 F3(b) 外干净。P6：干净。
  P7：除 F1+F3(a) 外干净；引言末行基线 2292.17 < 2404 预览框顶。
  P8：除 F4 外干净；答案区末行 y=2458（底 2560）；模范 88 词（run.log `model words: 88`）。

## 19. 交付文件复核（工作结束后，生产目录未动）

```
$ cd <生产版目录> && sha256sum A-Lucerna-VOL4.pdf A-Lucerna-VOL4-web.pdf 2026-w47-pt-ko.text.md
ac839d227acb506f71ccfd05a1b63915a22cca91c6bcb0cec0cecd025c2de6e1  A-Lucerna-VOL4.pdf
f505a301e3cb22645aba7131fb61d2f6f445d41ff670bfb3aa63dcebb071c38f  A-Lucerna-VOL4-web.pdf
fe14281fdd24abcfc527d359d707aef97b6d92bc9d602cd38ce1a4fbf6c791c4  2026-w47-pt-ko.text.md
A-Lucerna-VOL4.pdf 17185806
A-Lucerna-VOL4-web.pdf 1431508
2026-w47-pt-ko.text.md 37823
```
与 §0 复校前逐字节一致。生产目录无任何写入。
