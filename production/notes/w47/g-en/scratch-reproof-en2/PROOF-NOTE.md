# PROOF-NOTE — W47 core-en fix2 独立 re-proof（2026-11-11）

复校员：独立 re-proof agent（与 fix2 修复者不是同一人）。
对象：`production/2026-w47/core-en/`（只读核查；未 commit、未 push、未改生产目录任何文件）。
修复内容（唯一改动）：`content56.py:49` Q73 键 `"speak"` → `"up"`，注记与题干不动。

## 结论：(a) 通过

fix2 可进入 en delta 重建。未发现缺陷；缺陷清单为空（见 §5）。
10 个 en-* 读者版各自携带同一旧键（fix2 报告 §8），须按各版自己的 fix 流程同步——不在本次复校范围内。

## 1. SHA 实测（动手前与结束时各测一次，两次一致）

| 产物 | sha256（实测） | 字节 | 与 fix2 报告 |
|---|---|---|---|
| 印 `The-Lucerna-VOL4-en-zh-cn.pdf` | `08cbc1e53f2d02d6c64266d1f64ac2422eaa2f8f71e1829f877e94a5627b3213` | 41,407,287 | 一致 |
| 网 `The-Lucerna-VOL4-en-zh-cn.web.pdf` | `d7927eaad14531a9aee71331d4e27abbf951a296f6b6ee5fb1c770f8c7f7e444` | 2,804,281 | 一致 |
| `2026-w47-en-zh-cn.text.md` | `23855d4bd60abe4a7fb4db42050cb9343202e85789ffd434634808d299215c69` | 51,402 | 一致 |

基线核对：fix2 暂存的修前 text.md 快照 `scratch-fix-en2/tmp/text-prefixed.md`
实测 SHA `e368828a3fd5bb5a90de0d506a94fc03b22453e1d3d5ff139792f2b42e0ff70b`
与任务给定的修前基线完全一致——该快照可作修前真凭。

## 2. 改动范围实测（恰好 1 条 / 恰好 1 行）

- `diff text-prefixed.md 2026-w47-en-zh-cn.text.md`：**恰好 1 行**——
  `:1151` `73. [A2] 完成句子 — speak (speak up = 大声说出来)`
  → `73. [A2] 完成句子 — up (speak up = 大声说出来)`。
- `diff registry-prefixed.json registry.json`（json.tool 规范化后）：**恰好 1 处**——
  n=73 `"key": "speak"` → `"key": "up"`（note 不变）。
- `content56.py:49` 实测：`f.ex("A2", "完成句子", "up", "speak up = 大声说出来", "Speak ___: tell a teacher.", instr="填空")`。

## 3. Q73 四源一致（实测）

| 源 | 实测值 |
|---|---|
| registry n=73 | `{key: 'up', note: 'speak up = 大声说出来', page: 5, level: 'A2', type: '完成句子'}` |
| text.md:1151 | `73. [A2] 完成句子 — up (speak up = 大声说出来)` |
| P8 印出键（p8 extract keys['73'] + 印 PDF P8 文字层 `73. up` + 目视 P8 第 5 版答案区 `73. up`） | `up` |
| P5 题干 + 注释（印/网 P5 文字层 + 目视 P5） | `Speak ___: tell a teacher.`；同页译注 `to speak up 大声说出来`、配对 75. `to speak up` |

读成句为 "Speak up: tell a teacher."——语法正确，与注记一致。
未受影响对照（实测）：Q70 `silence`（Break the ___）、Q71 `socks`、Q72 `rights`、
Q79 `Children are speaking up this week.` 均与修前一致；P5 配对 74–77
（bullying→d / to speak up→a / a right→b / silence→c）全部正确。

## 4. 150 题逐题手验键与题干适配（key-vs-stem fit，我的独立对照表）

方法：我自己的脚本 `dump_keyverify_reproof.py` 在 scratch 副本里重跑
content12/34/56/7/8，wrap `Flow.ex` / `Flow.match_set` / `Flow.para` 逐条捕获
stem+key+note（完形/对话的题干取自带 `(N)___` 标记的原段落上下文），与
registry.json 逐条断言 key/note 相等；150 行对照表
`keyverify-reproof.txt`（116 ex + 20 match + 13 cloze/dlg + 1 writing）由我逐行读完。

**结果：150/150 PASS，无键错。** 逐题要点：
- 完成句子/句型转换（Q1–6, 11–19, 34–37, 42–45, 52–55, 60–63, 70–73, 78–81,
  94–99, 133–136）：键填入空白后句子语法与语义均成立；
  Q73 `up` 是唯一使 "Speak ___" 成立的键（旧键 speak 读作 "Speak speak"，不成立）。
- 单选 41 题、多选图表读数 6 题：键字母与选项内容一致（如 Q7 B=254 seats、
  Q82 B=254、Q87 C=435=254+162+19）。
- 词汇配对 5 组 ×4（n=24–27, 38–41, 56–59, 74–77, 141–144）：字母与释义一一对应，
  无错位；fix1 的 Q39 mentor→a / Q40 arena→d 仍在。
- 完形 112–119：键在各自 A/B/C 选项中唯一且合语境
  （Tuesday / call / continues / will meet / writes / will certify / wears / will watch）。
- 对话 145–149（row / film / popcorn / show / Friday）合语境。
- 纠错 108–111：改正句正确（Q111 "Nobody knows whether it will change."）。
- Q150 写作：开放题已知例外（键为全文说明，非可比键）。
- 分布：P1 10 / P2 17 / P3 18 / P4 18 / P5 18 / P6 18 / P7 12 / P8 39；
  A2 62 / B1 66 / B2 22，与 fix2 报告一致。

## 5. 缺陷清单

**无。** 本轮复校未发现任何须修的缺陷（键错、溢出、遮挡、字号、文字层、SAY IT
均通过；D5 字体只记录，不判）。

## 6. 门禁总表（全部由我独立重跑，详见 GATE-LOG.md）

| 门禁 | 结果 |
|---|---|
| run.py（scratch 副本） | rc=0，TOTAL 150，0 × FLOW OVERFLOW / HEAD TOO WIDE，MODEL words 82，P8 keys y=2548 / bottom 2560 |
| freeze baseline | 8/8 SVGs byte-identical，rc=0；p5 `a6a515cd…`、p8 `1066c475…` 与 fix2 一致；核心 SVG 跑前后重哈希未变 |
| occlusion（真实命令，无 --selftest） | 0 flags，rc=0（自检 6 类 planted 均触发为工具自带输出） |
| p8 extract | 150/150，noted set 60/150，与 fix1/fix2 基线集合完全相同 |
| p8 compare（读 p8-compare-reproof.json 本体） | CLEAN：missing=[] extra_count=0 uncertain=[] keydiff=[] |
| keycheck（registry vs P8 印出键，我的脚本） | 149/150 exact，#150 已知例外，0 mismatches — PASS |
| 印/网文字层逐页一致（交付件，pdftotext 同参） | 8/8 页字节一致（P1 4868 B … P8 9728 B） |
| 网 PDF scratch 重渲对比 | 重渲 2,804,279 B、48,135 文字字节；8 页文字层与交付印 PDF 全一致（交付网 PDF 本体未覆盖，SHA 终验不变） |
| 印 PDF 字节可复现 | scratch 重渲 SHA = 交付 SHA `08cbc1e5…`，41,407,287 B |
| P8 最小字号 | 15.5 pt（255 spans，0 < 10 pt） |
| creambox / box-title 真墨扫描（PIL 真墨） | 0 OVERFLOW；最紧 box 底 +2.9 px（P2 AND YOU?，修前已存在）、最紧标题边 +5.5 px（P1 THE WEEK IN NUMBERS） |
| SAY IT 在框内 | 3 面板全在框内（中 label −11.0 px/侧）；vocab ≤ −25.0 px；note 第 3 行墨至 1861 vs RIGHT 1862（−1.0 px，与基线同） |
| 8 页逐页目视（交付印 PDF 100 dpi 渲染） | 8/8 无溢出、无遮挡、无错字；P5 Q73 题干、P8 `73. up` 目视确认 |
| D5 字体（只记录） | Newsreader / Noto Sans CJK SC / Noto Serif CJK SC / UnifrakturMaguntia 全页；DejaVu Sans 仅 P6（4 个 ☐ 选票框，object 175）；全部 embedded + subset；与 fix1 一致 |

## 7. 工作卫生

- 所有工作在 `hidden_files/w47/scratch-reproof-en2/` 内；生产目录只读。
  终验三 SHA 与动手前一致；freeze 跑前后核心 SVG 重哈希未变；
  `git status production/2026-w47/` 下的 M 项均为其他并行 agent 的工作（it-es / core-nl / fanout-nl），
  与 core-en 无关。
- 网 PDF 只在 scratch 副本里重渲对比，未覆盖交付件。
- 未碰任何 en-* 读者版、未碰其他核心、未碰其他周。
