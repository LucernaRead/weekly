# GATE-LOG — 2026-w47-pt-ko fix1

返修员：fix1。解释器（全部步骤）：`~/workspace/weekly-git/tools/venv/bin/python`
（Python 3.12.3 / Pillow 13.0.0 / FreeType 2.14.3）。
scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-pt-ko1/`。
两轮验证：(A) scratch 构建副本 `build/2026-w47-pt-ko`（修复迭代 + 全部门禁）；
(B) 生产重建后，生产件直接复验 + 全新生产副本 `build2/2026-w47-pt-ko`
（keycheck / check_final 等会写目标目录的步骤）。
生产件与 scratch 验证版：SVG 8/8、印 PDF SHA、text.md、修复页卡片全部逐字节一致，
故 (A) 的目视结论直接适用于生产件。

## 0. 探针与 SHA

| 项 | 结果 |
|---|---|
| `ls /dev/null` | 存在 |
| `git hash-object -w` 探针文件 | 能通（`c4b82938…`） |
| scratch 写文件 | 成功（`probe.txt`） |
| SHA（修前，与任务书先验一致） | 印 `ac839d22…` / 17,185,806 B；网 `f505a301…` / 1,431,508 B；文 `fe14281f…` / 37,823 B |
| SHA（修后，生产件） | 印 `cdff9fe46e350a0d2889fcc99e51dfb36547eb158eb4aabfda021a2ad6f069a4` / 17,184,511 B；网 `3046541c903ea95e4f74aa7124c790a290448bd01fc4d30f04a1c9a42e64c3ad` / 1,431,219 B；文 `3eb35dfb9070565c1b168d3e79b8319c4867434b53e0819e8f77cd8ca467cb4c` / 37,804 B，534 行 |

## 1. run.py —— rc=0，TOTAL 150，0 溢出

- scratch：`logs/run.log`；生产：`logs/prod-run.log`。
- rc=0。`TOTAL 150`；by level `{'A2': 48, 'B1': 71, 'B2': 31}`；
  by page `{1: 10, 2: 18, 3: 18, 4: 18, 5: 18, 6: 18, 7: 12, 8: 38}`；model words 88。
- `grep -c OVERFLOW` = 0。
- SVG 变化页：仅 p1/p5/p7/p8（与修复页一致）；p2/p3/p4/p6 与生产旧版逐字节一致。

## 2. gates.py —— 16/16，rc=0

- scratch：`logs/gates.log`；生产：`logs/prod-gates.log`。16 行 `[PASS]`，`FAILURES: none`，rc=0。

## 3. occlusion_audit（真实审计，未传 --selftest）—— 0 flags，rc=0

- scratch：`logs/occlusion.log`；生产：`logs/prod-occlusion.log`。
- 输出：`<svg 目录>： 0 flags`（rc=0）。工具首行的 `selftest OK: planted classes fired {...}`
  为工具每次运行的固有自检输出，并非传入 `--selftest`（同 proof1 注）。

## 4. p8 extract / compare —— 150/150，CLEAN，rc=0

- extract：`logs/p8-extract.log`（scratch）/ `logs/prod-p8-extract.log`（生产）：
  `noted set = 150 of 150 (parse: lines)`，rc=0。
- compare：`logs/p8-compare.log` / `logs/prod-p8-compare.log`：
  `status: CLEAN  missing=[] extra_count=0 uncertain=[] keydiff=[137, 138]`，rc=0（137/138 预期）。

## 5. freeze baseline —— 核心对照 8/8 + 版内自洽基线 8/8，rc=0

- 核心对照（任务书标准口径）：`freeze.py baseline --build <core-pt> --core-svg <core-pt>/svg`
  → `logs/freeze-core.log`：`baseline: 8/8 SVGs byte-identical`，rc=0；
  `core integrity: shipped core SVGs unchanged by the run`。
- 版内自洽基线（补充）：`--build <版目录> --core-svg <版 svg>`：scratch `logs/freeze-ed.log`
  与生产 `logs/prod-freeze-ed.log` 均为 8/8，rc=0。

## 6. freeze diff（核心对照）—— rc=0

- scratch `logs/freeze-diff.log` / 生产 `logs/prod-freeze-diff.log`。
- 每页增减：p1 +49/-29、p2 +35/-33、p3 +29/-29、p4 +28/-26、p5 +85/-40、p6 +21/-21、
  p7 +48/-46、p8 +923/-481。
- TOTAL added CJK characters: **3,397**（重建版 3,403；−6 = F1 −2、F2 −3、F3b −1；
  均为韩语解释层 + 每页 1 个 U+3000，目标语文本无新增）。

## 7. creambox / creambox_diag（PIL 真墨）—— 0 溢出

- creambox.py（naive 扫描）：scratch `logs/creambox.log` / 生产 `logs/prod-creambox.log`，rc=0；
  6 处负 clearance（与 proof1 相同的 6 处：P1 y=786 −37.0、P1 y=1874 −38.0、P2 y=1618 −32.0、
  P3 y=200 −37.0、P6 y=1594 −42.0 ×2）。
- creambox_diag.py（真墨裁决）：`logs/creambox-diag.log` / `logs/prod-creambox-diag.log`，rc=0；
  **0 处负 ink-clearance**；6 处负值全部是框外行（owner-rect=NONE）；
  各框 OWN 末行真墨余量最小 +2.4px。**真墨 0 溢出。**

## 8. boxtitle（PIL 真墨）—— 31 框全清

- scratch `logs/boxtitle.log` / 生产 `logs/prod-boxtitle.log`，rc=0。
- 31 个框标题全部 `clear=+`，最小 clearance +18.2px（P3 gloss 标题），其次 +22.2、+26.3。无负值。

## 9. keycheck —— 149/150（唯一不符 Q150，预期），rc=0

- 方法：复制 `keycheck_core.py` 到本 scratch（`keycheck-mine.py`，输出写本 scratch 的
  `keycheck-150.json`），对构建副本运行（该工具会在目标目录内重跑 run.py，故只在副本跑）。
  生产重建后在全新生产副本 `build2/` 上重跑（`logs/prod-keycheck.log`，registry 重导）。
- `REG entries: 150; p8extract keys: 150`；`exact match: 149/150`；rc=0。
- 唯一 MISMATCH：`n=150 page=8 type=작문: key='（자유 과제 — 모범 글은 아래에 있어요）' extracted='✓'`（预期）。

## 10. sweep（桥孤儿 / 框-线 / 桥寡行）—— 0 / 0 / 0

- scratch `logs/sweep.log` / 生产 `logs/prod-sweep.log`，rc=0。
- box-vs-hline flags: 0；bridges found: 20；bridge orphans: 0；**bridge widows: 0**（重建版为 1，F1 已修）。

## 11. 印/网文字层 —— 逐字节一致（105,211 B）

- scratch：`pdftotext -layout` 印 PDF（`logs/print.txt`）与 scratch 重渲网 PDF（`logs/webtest.txt`），
  `cmp` 无输出，**PRINT/WEB TEXT BYTE-IDENTICAL**，各 105,211 字节。
- 生产：`logs/prod-print.txt` vs `logs/prod-web.txt`（生产印 PDF vs 生产网 PDF），同样逐字节一致，105,211 字节。
- scratch 网 PDF 重渲 1,431,223 B；生产网 PDF 1,431,219 B——字节数浮动属已知逐次浮动，文字层一致。
- italic span：生产印 1 = 生产网 1（同文 `« conscience »`）。

## 12. minfont（印 PDF P8）—— 最小 10.125pt，0 项低于 9.75pt

- scratch `logs/minfont.log` / 生产 `logs/prod-minfont.log`，rc=0。
- `P8 min effective font size = 10.125 pt (n=805)`；`below 9.75pt: 0`。

## 13. check_final（词 multiset + P8 字号）—— diff 0，7049/7049，rc=0

- scratch `logs/check-final.log` / 生产副本 `logs/prod-check-final.log`，rc=0。
- `pages print=8 web=8`；`words print=7049 web=7049 multiset-diff=0`；`diff sample: []`；
  P8 answer-region span sizes `[10.125, 10.5, 14.625, 18.75]`，count 610，min 10.125；
  `word bbox height: min 10.125 median 10.125 max 27.15`。
- 注：首次 scratch 运行因副本内网 PDF 仍是旧版，曾报 diff 15（恰为 4 处修复的 token 差异）；
  换入 scratch 重渲网 PDF 后 diff 0——该 15 是 stale-web 伪差，非缺陷。

## 14. render.py —— rc=0

- scratch `logs/render.log` / 生产 `logs/prod-render.log`，rc=0。
- 印 PDF 17,184,511 B；生产与 scratch 的印 PDF SHA 一致
  （`cdff9fe4…`）。
- 卡片：`build/2026-w47-pt-ko/cards/*.png`（1950×2700，8 页）为目视依据；生产卡片与 scratch 卡片
  修复页（p1/p5/p7/p8）逐字节一致。

## 15. webpdf.py —— rc=0

- scratch `logs/webpdf.log`：重渲 `webtest/A-Lucerna-VOL4-web.pdf` 1,431,223 B，47423 text bytes。
- 生产 `logs/prod-webpdf.log`：`WROTE …/A-Lucerna-VOL4-web.pdf: 1431219 bytes, 47423 text bytes`。

## 16. textmd.py —— rc=0，534 行，diff 恰 3 行

- scratch `logs/textmd.log` / 生产 `logs/prod-textmd.log`，rc=0；`question numbers present: 150 missing: []`。
- 新 text.md 37,804 B，`wc -l` = 534，`splitlines` = 534，以换行结尾。
- 与重建前 text.md 的 `diff` 恰 3 行：L38（F2）、L280（F3b）、L393（F1）。F4 在 text.md 中无出现处。

## 17. 孤儿标点 / 行首冒号 / 逗号缺空格 全版重扫 —— 0 处

- 逐栏重建扫描 `tmp/scan_lines2.py`（按栏 x 分组，跨栏同 y 不混淆）：
  - 旧生产版：5 处——ORPHAN P1 `）` y=990.2、ORPHAN P7 `.` y=654.4、
    LEAD-COLON P5 y=664.2、LEAD-COLON P7 y=624.7、COMMA-NOSPACE P8 Q68 `,TRI`。
  - 修复版（scratch 与生产 SVG 均测）：**ISSUES: 0**。
  - 修复行实测：P7B2 y=594.9 `quando、se、quem 뒤엔 접속법 미래가 와요:` / y=624.7
    `sair、for、tiver（공식 정답 기다리는 문법）.`；P1 y=963.2 `Palmares（1695년에 돌아가셨어요）`；
    P5 y=635.6 `TRI decide（맞힌 수가 점수가 아니에요:`；P8 y=2313.1
    `68. B — 맞힌 개수가 점수가 아니에요, TRI 성적을 정해요`。
- 核心 P5 孤儿 `）`（y=718.7）不在本版扫描结果中（韩语版该项不断行），且核心未动。

## 18. check_s11（pt-ko 改编版）—— rc=0，ALL PASS

- `check_s11_ptko.py`（据 en-ko2 版改编通用 §1.1 部分；现存 check_s11.py 均为 en 家族专用，
  无 pt-ko 版）：`logs/check-s11.log`（scratch）/ `logs/prod-check-s11.log`（生产）。
- colour set core 21 = edition 21，extra/missing 均为 none；P8 min font-size 13.5
  （该脚本正则口径；门禁以 minfont.py 的 10.125pt 为准）；
  P8 `AVALIAÇÃO E RESPOSTAS` / `113.` / `120.` / `145.` / `작문` 均 present；
  P8 Q68 行（`, TRI `）与 Q65 整句行均 present。

## 19. verify_ed（pt-ko 专用版）—— rc=0，ALL FIX1 VERIFICATIONS PASS

- `verify_ed_ptko.py`（en 版 verify_ed.py 为 Ashes 内容专用，不适用 pt-ko；本版为 pt-ko 新写）：
  `logs/verify-ed.log`（scratch）/ `logs/prod-verify-ed.log`（生产）。
- 18 项全 PASS：Q68 键 B、Q65 键 B、P8 Q68/Q65 整句行、Q137/Q138 键、4 处源文行、
  content12:266 答案未动、text.md 534 行 + L38/L280/L393 + 无 `,TRI`、
  core-pt 三重未动核验（无文件新于开工、git diff 为空、freeze-core 完整性行）。

## 20. 目视（8 页全页 + 4 处特写）

- 依据：scratch 重建卡片（与生产卡片修复页逐字节一致）及 `render/crop-*.png`（2× 特写）。
- P1：干净；1695 项 2 行，`）` 落行末（特写 `crop-p1-numbers1695.png`）。
- P2：干净（SVG 与旧版一致）。P3：干净（同前）。P4：干净（同前；D5 gloss 框未动）。
- P5：干净；计划框第 4 项 3 行，`:` 落行 2 末（特写 `crop-p5-note.png`）。
- P6：干净（SVG 与旧版一致）。
- P7：干净；B2 桥 2 行，`:` 落行 1 末、`.` 落行 2 末（特写 `crop-p7-b2bridge.png`）；引言与读者来信未动。
- P8：干净；Q68 行 `, TRI` 有空格（特写 `crop-p8-q68.png`）；答案区其余未动。

## 21. 机制耐久验证（transform 复现）

- `tmp/transform-test/`（core-pt 拷贝 + 更新后机制）跑 `transform.py ko`，rc=0
  （`logs/transform-test.log`）；4 处产出与手改版逐字相同（F1/F2/F3b/F4 transform==handfix）。
