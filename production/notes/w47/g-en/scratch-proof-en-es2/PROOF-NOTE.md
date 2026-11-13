# PROOF-NOTE — Lucerna Weekly 2026-W47 en-es · proof2 (independent, Q73 delta rebuild)

- Edition: `production/2026-w47/2026-w47-en-es/` (VOL.4, issue week Mon 2026-11-16–Sun 2026-11-22)
- Proofreader: proof2 (independent; not the delta builder, not proof1). No production file was modified, rebuilt, committed or pushed. All build/tool runs happened in scratch copies; the three production objects re-hashed identical at the end of the round.
- Build under review: Q73 delta rebuild (key `speak` → `up`, core-en fix2 sync). Proof1 on the pre-delta build was (a) with zero defects; the delta claims a single-key change only.
- Probes first: `/dev/null` present (`crw-rw-rw-`, 1,3); `git hash-object -w --stdin` OK (`ce013625…`); scratch write OK (`probe.txt` in this dir). `TMPDIR` pointed at this scratch dir's `tmp/`; `/tmp` never written.

## Conclusion: (a) — 定稿，零缺陷

No defect found. The delta is exactly what it claims — one key, one line in the registry, one line in text.md, one SVG (p8) — and every gate re-run independently passes. All 150 exercises hand-verified; all 8 pages visually inspected; Q73 consistent across all four sources and with fixed core-en.

## Identity / SHA (PASS — match task values exactly, re-verified at start AND end)

| Object | Size | SHA-256 |
|---|---|---|
| Print `The-Lucerna-VOL4-en-es.pdf` | 29,331,230 B | `6a249cc98f0dea9aa24d6b0af1db9480d9b030164f6ad083e4ff4f01249a70cb` |
| Web `The-Lucerna-VOL4-en-es.web.pdf` | 2,414,439 B | `2bc163a375007387e0e09c0ef2395459688dd2d19aea2f6946ced68c5c1eb79c` |
| `2026-w47-en-es.text.md` | 54,385 B | `314b32a3c3f236bec94ad6f1426664eb180cc8f96053cc886beed3eaacf217ca` |

Pre-delta values from the delta note re-confirmed against its stored `registry-pre.json` / `text-pre.md` (print `6341e239…` / 29,331,231 B; web `73356781…` / 2,414,448 B; text `25391799…` / 54,388 B). Both PDFs 8 pages, 1462.5×2025 pts. Interpreter: `tools/venv/bin/python` (Pillow 13.0.0 / FreeType 2.14.3) for every tool run.

## Delta scope verification (PASS — exactly one key, nothing else moved)

| Check | Result |
|---|---|
| Registry diff vs `registry-pre.json` | exactly 1 line: `583c583` `"key": "speak"` → `"key": "up"` (diff output 4 lines = 1 change) |
| text.md diff vs `text-pre.md` | exactly 1 line: `1151c1151` `73. … — speak (speak up = hablar sin miedo)` → `… — up (speak up = hablar sin miedo)` |
| SVG scope (pre vs post sha256) | ONLY `p8-test.svg` changed (`e565acaf…` → `1c7f8051…`); other 7 SVGs byte-identical, incl. `p5-youth.svg` `5aab5f16…` — correct and expected: the key appears only on the P8 answers page, not on the P5 stem page |
| Source change | `content56.py:49` = `f.ex("A2", "Completar frases", "up", "speak up = hablar sin miedo",` |
| Core-en untouched | `git status --porcelain` shows `core-en/` and `2026-w47-en-es/` both as untracked `??`, no `M` items under either; core Q73 key = `up` (matches edition now) |

## Q73 four-source consistency (PASS — all `up`)

| Source | Evidence |
|---|---|
| registry.json[72] | `{'n': 73, 'page': 5, 'level': 'A2', 'type': 'Completar frases', 'key': 'up', 'note': 'speak up = hablar sin miedo'}` |
| text.md answer line 1151 | `73. [A2] Completar frases — up (speak up = hablar sin miedo)` |
| P8 printed key | print PDF p8 text: `73. up` (in `72. rights … · 73. up · 74. d`); web PDF p8 identical; `p8-extract.json` `"73": "up"`; P8 render shows `73. up` in ANSWERS — Página 5 — |
| P5 stem + gloss | P5 SVG: stem `Speak ___: tell a teacher.` (Q73, A2 Completa); Nota box `to speak up = hablar sin miedo`; box title `SPEAK UP　Alza la voz`; match term `75. to speak up`; Q79 `Children (speak) up this week.` — all coherent with key `up` |
| Cross-check vs core-en | registry keys vs core-en registry differ ONLY in the 5 known reader-language keys (137–140, 150); Q73 `up` = core `up` |

## 全量门禁逐项结果（详见 GATE-LOG.md；全部独立重跑）

| 门禁 | 结果 |
|---|---|
| run.py（scratch 拷贝 `runcopy/` 内重跑） | rc=0；OVERFLOW 0；TOO WIDE 0；TOTAL 150；MODEL 82；ALL DONE；all flows end within bottom (P8-keys y=2443/bottom 2560) |
| freeze baseline（edition rebuild in copy） | 8/8 SVGs byte-identical (incl. p8 `1c7f8051…`); core integrity: shipped SVGs unchanged |
| freeze baseline（core-en rebuild in copy, read-only 对照） | 8/8 SVGs byte-identical; core integrity unchanged |
| freeze diff vs core-en | TOTAL added CJK 9，全部 U+3000；`freeze-diff.json` byte-identical to delta's file |
| occlusion audit（REAL audit, NOT `--selftest`） | rc=0, **0 flags** (edition 0, core 0, NEW vs core 0); `occlusion.json` identical to delta's (`flag_count: 0, core_flag_count: 0, new_flag_count: 0`) — the `selftest OK` line in the log is printed by the tool itself on the real-audit run |
| p8 extract | 150/150 both; noted set 60/150 each, identical sets (parse: joined) |
| p8 compare（`p8-compare.json` 本体直读） | **CLEAN**, missing=[] extra=[] uncertain=[]; keydiff=[137, 138, 139, 140, 150] (expected reader-language keys); file byte-identical to delta's |
| keycheck（p8 extract vs registry） | extract 150, registry 150, missing none; only mismatch #150 short-label exception (known, same as core); text.md 150 answer lines, 1–150 continuous, **0 mismatches** |
| 印/网文字层逐页一致 | 各 48,255 字符；token-multiset diff 0/0；逐页 8/8 byte-identical (P1 4956B … P8 9916B)；网 PDF 只在 scratch 副本里重渲对比，未覆盖交付文件 |
| check_s11（§1.1 + P8） | **ALL PASS**; P8 min SVG font-size 13.5; colour set core 19 / edition 19, extra none, missing none |
| P8 最小字号 | SVG 13.5 pt；PDF 实测 **10.12 pt ≥ 10 pt** (verify_ed PASS) |
| boxtitle（source 12 + SVG 18） | 0 超框；source 最紧 P1 +20.4；SVG 最紧 P2 SENATE +33.6、P6 HOW LONG +142.3 |
| creambox（canonical, PIL 真墨） | **NO OVERFLOW**; 32 cream boxes; inside clearance +5.0 至 +92.4 px; 最紧 P2 box y=1211 (+5.0, 仍为正) |
| verify_ed | **VERIFY ALL PASS** (Q39/Q40、Q46/Q52/Q55/Q125 fix1 checks still pass; text.md 150 answers; P8 min PDF font 10.12 pt; SVG zero real CJK) |
| 孤儿标点全扫 | SVG 全 8 页 `<text>` 行首孤儿闭标点、行尾孤儿开标点均为 0；text.md 全 1305 行同为 0；curly “ ” 81/81 平衡（见观察 O7）；SOP/proofread/TODO/PLACEHOLDER/Lorem/XXX/estadio/stadio = 0 |
| 日期/星期 | 全部核实（`date`, America/Toronto）：Nov 3 2026 Tue、Nov 8 Sun、Nov 9 Mon、Nov 16 Mon、Nov 20 Fri、Nov 26 Thu、Nov 27 Fri、Nov 21 2025 Fri、Jan 8 2026 Thu |
| 模型文 | "My Monday, November 16" = 82 词（alphanumeric-token 计，与 run.py 一致） |
| ABSTRACT.txt | 一行西班牙语，807 B，含真实主题 + A2–B2 + 150 ejercicios |
| P7 golden sentences | 8/8 逐字见于正文，页码归属正确（P2/P1/P4/P6/P6/P3/P5/P1） |
| IN THIS ISSUE / 交叉引用 | p.2–p.8 与各版栏目一致；"Read page 6" → P6 地图；P2 "Page 3 has the story / page 4 the sport" 正确 |

## 150 题逐题手验（PASS，150/150）

- 全文 text.md 1305 行通读（P1–P8 正文 + 全部答案行）；registry 150 题编号连续，分页 10/17/18/18/18/18/12/39，级别 A2 62 / B1 66 / B2 22。
- 每题键对照题干语义手验；配对题另对印版 SVG 字母顺序核对（定义字母的 SVG 实测顺序）：
  - P2 D 24–27：a=the bird (turkey), b=a second vote (runoff), c=to confirm officially (certify), d=the American family holiday (Thanksgiving) → 24→b, 25→c, 26→a, 27→d ✓；SVG 术语编号 24. a runoff / 25. to certify / 26. a turkey / 27. Thanksgiving ✓
  - P3 C 38–41：a=teaches and guides (mentor), b=chosen to take part (tribute), c=lives with you in camp (campmate), d=place where Games fought (arena) → 38→b, 39→a, 40→d, 41→c ✓
  - P4 C 56–59：a=a pause (break), b=a five-day cricket match (Test), c=a series of games away (tour), d=damage to the body (injury) → 56→b, 57→c, 58→d, 59→a ✓
  - P5 C 74–77：a=saying what you think (speak up), b=something every child has by law (right), c=saying nothing at all (silence), d=hurting/frightening (bullying) → 74→d, 75→a, 76→b, 77→c ✓
  - P8 F 141–144：a=election in the middle of a term (midterm), b=news organisation's judgement (call), c=a second vote (runoff), d=to confirm officially (certify) → 141→b, 142→c, 143→d, 144→a ✓
  - P8 ANSWERS 块亦印有 `24. b · 25. c · 26. a · 27. d` 与 `38. b · 39. a · 40. d · 41. c`，与 registry 一致。
- Q73 专项：`Speak ___: tell a teacher.` → `up`（speak up 为固定短语动词，题干 Nota 框与 P5 正文 "to speak up, to listen" 均佐证）；Q70 `silence`（Break the ___）与 Q79 `are speaking`（Children (speak) up → "Children are speaking up this week."）亦复核无误。
- 图表题算术：254+162+19=435（Q87→C）；254−218=36（P7 "36 more than the majority"）；参议院 33/35 已宣布（Q84→A）。
- 对话 145–149（row / film / popcorn / show / Friday）与翻译 137–140（西语译文准确）逐一核对。
- Q108/Q109 诊所题已审定接受（proof1 O5）：Q108 "The Democrats win the House in 2026." → "The Democrats won the House."；Q109 "The count continue after the vote." → "The count continued after the vote."；过去时修正与诊所 "wrong tense" 定性及本期过去时框架一致，句子本身合乎语法，不计缺陷。
- Q116/Q117 cloze 细核：116 `writes`（Maya 三单，选项 writes/write/is wrote）；117 `will certify`（"states ___ their counts by December 18"，将来语境，与 core 键一致，keydiff 不含 117）。

## 8 页逐页目视（PASS，网版 100 dpi 渲染 `visual/web-p-*.png`，2032×2813）

- P1：masthead、VOL.4、日期、头条、数字盒、搜索榜、目录、简讯、Capitol 图 + 图注、快问——干净。
- P2：SENATE 标题收进奶油盒；SAY IT 三盒、火鸡图 + 图注、练习 A–D、页脚 "Página 2 de 8"——干净（见 O4）。
- P3：配对块 C（38–41 题干与 a–d 定义顺序正确）、gloss "the arena = la arena"、Rousseau 虎图 + 图注、HAYMITCH'S GAMES 盒、FIVE SENTENCES——干净。
- P4：Ashes 回顾正文、WHY PERTH 盒、SATURDAY 盒（标题收进框内）、W. G. Grace 照 + 图注、"Arsenal are winning!"、练习 A–D——干净。
- P5：Lawrence 1912 儿童图 + 图注、ODD SOCKS 盒、SPEAK UP 盒（标题收进框内）、FRIDAY'S WORDS、桥接行、练习 A–D——干净；Q73 题干 `Speak ___: tell a teacher.` 目视确认，Nota 框 `to speak up = hablar sin miedo` 目视确认。
- P6：HOW LONG? 标题收进框内、图表数字、投票亭图 + 图注、FIFTY ELECTIONS——干净。
- P7：8 句 golden sentences 及页码归属、drills 100–107、error clinic 108–111、toolbox、Samuel Johnson 肖像 + 图注、读者来信、示例信、NEXT WEEK——干净。
- P8：cloze A、选择 B、阅读 C、句子 D、翻译 E、配对 F、对话 G、写作 H、MODEL 82 词、Library of Congress 图 + 图注、ANSWERS 块（目视可见 `73. up`、"38. b · 39. a · 40. d · 41. c"）——干净。

## 观察项（非缺陷，不阻塞定稿；与 proof1 相同项沿用其裁定）

- O1 — P5 桥接行 "Cada niño tiene derechos | Every child has rights = Cada niño tiene derechos." 西班牙语出现两次，读感冗余；与 core 同构（freeze-diff 证实 core 同句式），属 frozen core 写法。
- O2 — P7 golden sentence "A "call" is not the official result." 内层直引号；core-en P7 SVG 同字节 renders，属 frozen core 排版惯例。
- O3 — P5 "D PRESENT CONTINUOUS" 小节头在第 2 栏底、题目在第 3 栏顶；模板分流，freeze-diff 证实 P5 英文正文与 core 一致。
- O4 — P2 SAY IT 第 3 盒 Feliz 行贴边：目视渲染中 "¡Feliz Día de Acción de Gracias!" 的 "¡" 贴奶油盒左沿；proof1 已像素实测墨迹在盒边之内、无溢出，沿用其裁定（clean）。
- O5 — Q108/Q109 诊所修正（见 150 题节）已审定接受。
- O6 — 旧版 proof1 唯一未 source-verified 微断言（ATP 决赛 "not before 6 p.m. local time"）仍未核实源——未断言为假，仅未核实；不在本次 delta 范围内，不阻塞。
- O7 — curly 引号计数 81/81：proof1 记为 82/82；本轮在修前 `text-pre.md` 与修后 text.md 中均实测 81/81（平衡），delta 未改动引号——proof1 的 82 应为计数口径差，非内容变化；平衡即无孤儿引号，不计缺陷。

## D5 字体（只记录、不计入判定）

按任务要求只记录：印 PDF `pdffonts` = 43 行输出（41 个字体行 + 2 行表头）/ **35 distinct font names**（`pdffonts-print.txt`、`pdffonts-distinct.txt`），与 delta 记录的 41 行 / 35 名一致。未找到 "D5 字体" 的定义文本；不判、不修。

## 交付

工作目录 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-proof-en-es2/`：
`PROOF-NOTE.md`（本文件）、`GATE-LOG.md`、门禁日志（`gates-run1.log`、`run.log`、`occlusion*.log/json`、`p8-*.log/json`、`freeze*.log/json`、`check_s11.log`、`boxtitle*.log`、`creambox-check.log`、`verify.log`、`printweb.log`、`keycheck.log`、`orphan.log`、`pdffonts-print.txt`、`pdffonts-distinct.txt`、`svg-now.sha256`）、复现产物（`freeze-final/`、`freeze-core/`、`runcopy/`）、渲染（`visual/web-p-1.png` … `visual/web-p-8.png`）。

## 生产文件零改动确认

收尾复核三件 SHA 与任务值完全一致（见上表）；`git status` 显示 en-es 与 core-en 仍为未跟踪新目录、无 M 项。网 PDF 未被覆盖（只在 scratch 副本里重渲对比）。
