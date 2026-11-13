# DELTA-NOTE — 2026-W47 en-pt · Q73 speak→up (core-en fix2 sync)

- 版：`2026-w47-en-pt`（目标语 English，读者母语 Portuguese）
- 任务：只对本版做 Q73 键同步 delta；core-en fix2 已定稿，re-proof (a) 通过。
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-delta-en-pt/`
- 日期：2026-11-11。未 commit、未 push（由协调员统一 git 操作）。
- 核心未动：`core-en/content56.py:49` 仍为 `"up"`（`speak up = 大声说出来`）；core-en SVG 8 个哈希与 freeze baseline 一致，未变。

## 唯一改动

`production/2026-w47/2026-w47-en-pt/content56.py:49`，仅 key 一词：

```diff
-f.ex("A2", "Completar frases", "speak", "speak up = falar sem medo",
+f.ex("A2", "Completar frases", "up", "speak up = falar sem medo",
      "Speak ___: tell a teacher.", instr="Complete")
```

note 与 stem 一字未动；未改其他任何源行、map、翻译文件、ABSTRACT.txt。

## 修前 → 修后（三件）

| 件 | 修前（proof1 (a) 核对一致） | 修后 | 字节 |
|---|---|---|---|
| 印 `The-Lucerna-VOL4-en-pt.pdf` | `3f6b415fa35195ca49605414b5a756a01f0457032cc5c6acc75075e49c221dad` | `52452731bc5988209215cb8f83548b14a7d1a933953dac09688e7f8d82a3b700` | 29,345,708 → 29,345,708（同大小，内容变） |
| 网 `The-Lucerna-VOL4-en-pt.web.pdf` | `0252edc42a4981413c25067e8ed60bb5069994f86c10a4d25a0b8483e0846629` | `467068e289700e570c5e2c55a9f6c372dc618a0fb4e8d49ccf277429151b7128` | 2,418,233 → 2,418,222 |
| `2026-w47-en-pt.text.md` | `12b04ff13b12db5232d3114816f287c2d72a69df164e0273269409ef3148d545` | `f85c55cef1cf7fe824fe59f3c9ff97bad8f4938d423bcc737a9afe60fbab7422` | 54,123 → 54,120（−3 = speak→up） |

修前三 SHA/字节与本版 proof1 PROOF-NOTE（`scratch-proof-en-pt1/`）逐字一致后才动手；
修前三源同错已核：registry Q73 `speak`、text.md l.1151 `speak`、P8 提取键 `"73": "speak"`。

## diff 证据（见 `diffs.txt`）

- registry diff：恰好 1 行 — `"key": "speak"` → `"key": "up"`（第 583 行）。
- text.md diff：恰好 1 行 — l.1151 `73. [A2] Completar frases — speak (speak up = falar sem medo)` → `… — up (…)`。
- SVG 变化范围：仅 `svg/p8-test.svg` 变（`1365ad54…` → `d9ce301c…`）；其余 7 页与修前字节一致。P5 未变是预期的——题干字符串 `Speak ___: tell a teacher.` 未改，键只印在 P8。

## Q73 四源一致（见 `q73-evidence.txt`）

| 源 | 修后值 |
|---|---|
| registry Q73 | `{"n": 73, "page": 5, "level": "A2", "type": "Completar frases", "key": "up", "note": "speak up = falar sem medo"}` |
| text.md l.1151 | `73. [A2] Completar frases — up (speak up = falar sem medo)` |
| P8 印出键（SVG + p8 extract + 150dpi 裁片目视） | `73. up`（裁片 `render/p8-answers-73.png`） |
| P5 题干 + 注释 | `Speak ___: tell a teacher.` + `speak up = falar sem medo`（未动） |

另：核心 P8 提取键 Q73 亦为 `up`，与本版一致。

## 全部门禁表（全部独立重跑，日志均在本目录）

| 门 | 结果 | 证据 |
|---|---|---|
| run.py | rc=0，TOTAL 150，ALL DONE，0 溢出（各 flow 终点 ≤ bottom；P8-keys 2443/2560） | `run.log` |
| registry 重导 | 150 条，per page 10/17/18/18/18/18/12/39；A2 62 / B1 66 / B2 22 | `dump_reg.log` |
| text.md 重导 | rc=0，stub registry 150 = real registry 150，54,120 B | `textmd.log` |
| render.py | rc=0，8 卡 + 印 PDF | `render.log` |
| webpdf.py | rc=0，2,418,222 B，49,268 text bytes | `webpdf.log` |
| occlusion（真实审计，未用 --selftest） | 0 flags（本版 0，core 0，NEW vs core 0） | `occlusion.log` / `occlusion.json` |
| p8 extract | core 60/150，edition 60/150，同一 noted set | `p8-extract(-core).log/json` |
| p8 compare | CLEAN，missing=[]，extra=0，keydiff=[137, 138, 139, 140, 150]（预期读者语键） | `p8-compare.log/json` |
| freeze baseline（--build 指真核心 core-en） | 8/8 byte-identical；core integrity：shipped core SVG 未变 | `freeze.log`，`freeze-baseline/` |
| freeze baseline（更正口径，见下文补记） | 版 baseline 8/8（--build 指版自己的构建目录，--core-svg 指版 svg 目录）；core 只读对照 8/8（直接 sha256，不重建核心） | `freeze-edition.log`，`freeze-baseline-edition/`，`core-readonly-check.txt` |
| freeze diff | p1 +34/−33、p2 +43/−54、p3 +27/−23、p4 +25/−22、p5 +25/−22、p6 +25/−21、p7 +65/−55、p8 +106/−100（proof1 为 +105/−99，+1/−1 恰为改动的 1 个键字符串）；新增 CJK 合计 9，全部 U+3000 | `freeze-diff.log/json` |
| 印/网文字层 | token multiset diff 0/0（各 47,923 chars，2,515 distinct）；逐页 layout 提取 8/8 字节一致（p1 12,540、p2 13,634、p3 11,212、p4 12,542、p5 10,715、p6 11,128、p7 14,182、p8 23,483；仅 p8 比修前少 6 B，为答案区重排） | `printweb.log`，`layout/` |
| keycheck（150 题） | 150/150，registry-key 0 不符、level 0 不符、type 0 不符 | `keycheck-out.txt` |
| P8 最小字号 | 印/网均为 10.12pt；其余各页 11.62pt（≥10pt 门通过；SOP 下限 9.75pt） | `p8-font.txt` |
| creambox 全版扫查 | 日志与 proof1 逐字节相同（32 盒；24 条 SVG-OVERFLOW 启发式旗标均为下一栏头，P1 406px 带为下一栏头字顶——proof1 已查明处置；唯一真墨紧余量 P2 AND YOU +0.9px 未变） | `creambox.log`，`creambox2.log` |
| boxtitle 源扫查 | 12/12 fit，PASS（最紧 HOW LONG? 395.6，+8.9） | `boxtitle-src.log` |
| boxtitle SVG 扫查 | 18/18 fit，0 溢出（最紧 HOW LONG? advance +8.9 / 真墨 +8.5） | `boxtitle-svg.log` |
| check_s11 | ALL §1.1/P8 CHECKS PASS | `check_s11.log` |
| 家具 tables.py | badge / footer / `Página {n} de 8` / `Nota — ` / `— Página {n} —` 与 SVG 逐字一致，VOL.4 | `furniture.log` |
| D5 字体（只记录数量，不判） | 印 41 个字体对象、网 41 个；族：NotoSansCJKsc（R/B）、NotoSerifCJKsc R、Newsreader（R/Italic）、UnifrakturMaguntia、DejaVuSans；全部 embedded + subset | `d5-print.txt`，`d5-web.txt` |
| 逐页像素对比（vs proof1 渲染） | p1–p7 0px 全同；p8 4,509px（0.15%），bbox x 404–719 / y 1699–1757，仅答案块重排区 | `render/p-*.png` |
| 8 页逐页目视（印版） | 全部干净，无溢出/重叠/压页脚；P5 Q73 题干在位，P8 答案块 `73. up` 在位、收尾在页脚之上 | `render/p-1.png` ~ `p-8.png` |
| 网版 P1/P8 目视 | 与印版一致，无豆腐块、无缺字 | `render/web-p1-1.png`，`render/web-p8-8.png` |

## 150 题键与题干适配抽查（Q73 教训：三源一致不够）

- 全量复核填空/改写类共 65 题（`fill-audit2.txt`，以 monkeypatch 记录真题号，0 映射偏差）：
  34 Completar frases + 16 Transformação + 8 Completar o texto（cloze）+ 7 P7 drills
  （Frases de ouro / Comparativos / Passado / Futuro / Tempos verbais / Subordinadas）。
- 结论：65/65 键填空合理。抽查要点：
  - Q73 `Speak [up]: tell a teacher.`——`speak up` 为固定搭配，正确。
  - Q79 `Children are speaking up this week.`——(speak) → are speaking，含 up 不动，正确。
  - Q133–Q136（P8 D 组单形式键）：`will meet` / `won` / `more` / `whether` 各与题干动词/比较/从句一致。
  - Cloze Q112–Q119：Tuesday / call / continues / will meet / writes / will certify / wears / will watch，
    逐项对选项组验算，均为唯一适配项（如 Q112 Nov 3 为周二，选项 Mon/Tue/Fri → Tuesday）。
- 既存重复（proof1 (a) 已带、非本次引入）：Q6=Q12（January 同题干同键）、Q2=Q95（call）、Q5=Q96（changed）。
  为跨页/跨级别复用，非本次 delta 缺陷。

## 观察（不构成阻碍）

1. P2 AND YOU 盒真墨余量 +0.9px 与 HOW LONG? 标题真墨 +8.5px 为 proof1 已记录的紧余量，本次未变。
2. 本次并行期间其余 en-* 版（en-de/fr/es/it/nl/ru/ja/ko/zh-tw 等）亦在同步改动，盘上 mtime 有交叉，均非本 agent 所动；本 agent 只写了 `2026-w47-en-pt/` 内文件与本 scratch 目录。
3. KIT §6 旧标题行（P2 栏头旧文案）与 KIT §3 “P8 min font 13.5 pt”单位口径两处 proof1 观察 2/3 仍在，属 KIT 文字问题，本次未动 KIT 该两行（任务只要求新 SHA + delta 条目）。
4. WEEKLY-KIT.md 已更新：§2 三件新 SHA/字节 + §5 item 6 delta 条目。

## 补记（2026-11-11，简报更正后追加）

1. **SVG 变化范围**：Q73 键只出现在 P8 答案页，不出现在 P5 题干页（P5 只印 `Speak ___` 空白 + `speak up` 注记，键本身从不上 P5）。因此**只有 p8 变化、p5 与修前字节一致是正确且预期的**，非异常，无返工（en-es delta 同证：p8 含 `73. up`，p5 不变）。本 delta 原记录已按此定性，无改动。
2. **freeze 口径更正**：`freeze.py baseline` 的 `--build` 指版自己的构建目录（含 run.py），core 对照另用 core-svg 路径。已按更正口径重跑：
   - 版 baseline：`freeze.py baseline --build production/2026-w47/2026-w47-en-pt --core-svg production/2026-w47/2026-w47-en-pt/svg --out <scratch>/freeze-baseline-edition` → **8/8 byte-identical**，哈希与修后 svg 快照逐个一致（p1 `16be1b38…`、p2 `23d1d7c4…`、p3 `22aa9881…`、p4 `8151afbf…`、p5 `cbecfa6c…`、p6 `48167a62…`、p7 `61007a0d…`、p8 `d9ce301c…`），另附 `core integrity: shipped core SVGs unchanged`。见 `freeze-edition.log`。
   - core 只读对照：直接 `sha256sum` 盘上 core-en/svg 8 页，前 16 位与 freeze.log 所载 core 哈希逐个一致（p1 `a9a8deaf…`、p2 `97974716…`、p3 `efb83ce7…`、p4 `aa6f395e…`、p5 `a6a515cd…`、p6 `76922564…`、p7 `da908af6…`、p8 `1066c475…`）→ **8/8**。见 `core-readonly-check.txt`。
   - 此前 `--build core-en` 的 8/8 仍保留为补充证据（`freeze.log`）：核心可自我复现且未被本次改动。

## 结论

**Delta 完成，全部门禁通过，可进 proof2。** 唯一改动 Q73 speak→up；registry/text 各恰 1 行 diff；Q73 四源一致为 up；SVG 仅 P8 变；65 题填空适配全过；8 页目视干净。
