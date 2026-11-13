# FIX-LOG — 2026-W47 en-de fix1（D1 修復）

- 版：`2026-w47-en-de`（英语目标语 × 德语读者版），VOL.4，8 版，150 题
- 修复员：fix1 builder；日期：2026-11-11（UTC 08:02–08:20 左右）
- 依据：SOP §8 / §1.1、`~/workspace/weekly-git/SOP.md` 全文已读；`hidden_files/w47/briefs/brief-coordinator.md` 已读；第一轮复校笔记 `scratch-proof-en-de1/PROOF-NOTE.md`、`GATE-LOG.md` 只作参考，改动前已自行核实。
- 工作范围：只改 `production/2026-w47/2026-w47-en-de/` 内文件与本笔记目录；未碰 core-en、其他家庭、tools/、issues/；未跑 insert.py、lint --write；无任何 git 写操作（不 commit、不 push、不 reset、不 stash）。

## 0. 开工探针（双通）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` → `da0c4eb8d9a48d171a33574b380752e183286751`，成功。
- 在 `hidden_files/w47/` 真实写小文件成功（`.probe-fix-en-de1`，完工后已删）。
- `df -h`：`/home/hatch` 可用 46G，无配额问题。

## 1. D1 在盘上核实属实

`svg/p7-lang.svg` 坐标实测（修前）：

| 行 | x | y |
|---|---|---|
| 第 8 条金句末行 `Senate, and for governor in 36 states.”` | 538.5（第 2 栏） | 2526.47 |
| 第 8 条出处行 `—— From page 1 of this issue.` | 989.0（第 3 栏顶部） | 219.0 |
| `THE DRILLS　Übungen` | 989.0 | 275.6 |

其余 7 条出处行全部在第 2 栏内（y=1468.48 / 1574.95 / 1714.79 / 1854.63 / 1994.47 / 2167.68 / 2340.89）。

成因（实测确认，非推断）：`bslib4.py` `Flow.para` 按 `maxk = int((bottom − y − size) // (size·lh)) + 1` 决定一栏能放几行。金句末行后 flow y=2561.8，已超底线 2560（只差 1.8），出处行（19pt、行高 26.6）maxk=0，被推到下一栏顶部 y=219。德语讲解层较长是总高度来源，但直接触发点就是这 1.8pt。

## 2. 改动（只改 `content7.py` 两行）

修法：缩短 P7 德语讲解文字，每处各省 1 行（框内行高 29.725pt），合计省 59.45pt；不改金句英文原文、不改出处文字、不改题意、不动行距/栏距、不动其他页。

| 位置 | 改前（行数） | 改后（行数） | 删了什么、为什么不改题意 |
|---|---|---|---|
| `content7.py:17` WORDS A2 win/won gloss | `Erklärung \| Win ist Gegenwart (gewinnt immer wieder); won ist Vergangenheit (hat schon gewonnen) — in dieser Woche steht meist die Vergangenheit.`（5 行） | `Erklärung \| Win ist Gegenwart; won ist Vergangenheit (hat schon gewonnen) — in dieser Woche steht meist die Vergangenheit.`（4 行） | 删冗余括号 `(gewinnt immer wieder)`：win=现在时已由 “Win ist Gegenwart” 说清；完成时说明 `(hat schon gewonnen)` 保留。 |
| `content7.py:41` GRAMMAR B1 past simple gloss | `Erklärung \| past simple = einfache Vergangenheit: für Geschehenes; unregelmäßige Verben muss man lernen.`（4 行） | `Erklärung \| past simple = einfache Vergangenheit; unregelmäßige Verben muss man lernen.`（3 行） | 删 `für Geschehenes`：“einfache Vergangenheit” 本身即指过去发生的事，且紧接的正文段即 “Use the past for the past: …”，题意无损。 |

行数用 `bslib4.wrap(..., 框内宽 386.5)` 实测确认（另试过 headline-present gloss 亦可省 1 行，未用——两处已够）。

模型预演（scratch 瘦复制 + monkeypatch 打点）：改后金句末行后 y=2490.4，出处行回第 2 栏，基线 2509.4；THE DRILLS 仍在第 3 栏顶。

## 3. 重建（真版，全量）

```bash
cd production/2026-w47/2026-w47-en-de
tools/venv/bin/python run.py      # exit 0，零 OVERFLOW / TOO WIDE；TOTAL exercises 150；MODEL words 82
tools/venv/bin/python render.py   # cards + print PDF
tools/venv/bin/python tools/webpdf.py production/2026-w47/2026-w47-en-de/svg production/2026-w47/2026-w47-en-de/The-Lucerna-VOL4-en-de.web.pdf
tools/venv/bin/python hidden_files/w47/scratch-fanout-en/de/make_textmd_w47.py   # .text.md 重导（见 §5）
```

- SVG 逐字节比对（修前快照）：**仅 `p7-lang.svg` 变，其余 7 个 byte-identical**。
- 新版 P7 实际 flow：`flow[P7-main] ended col 2/2 y=1786 (bottom 2560)`（修前 1833——DRILLS 段自第 3 栏顶起，位置不变，结束点提前 47pt 是因为栏顶不再有孤行占位）。

## 4. 新交付物

| 文件 | 字节 | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-de.pdf` | 29,330,766（修前 29,330,795） | `6f82363a63477603b9de4b7ad14967bc01d6bc68e7cbd1b961b8530b52d2d5c2` |
| `The-Lucerna-VOL4-en-de.web.pdf` | 2,377,894（修前 2,377,924，< 7 MB） | `b2b686e4f9064ef4babdf02697671e5aaf73d1a87382015546d483d09b86181a` |

两 PDF 均为 8 页、1462.5 × 2025 pt。文件名注意：网页版是点式 `.web.pdf`，未写错。

## 5. 附带同步：`.text.md`

`.text.md` 由源码导出，内含两句旧 gloss（第 747、775 行），与新 PDF 不一致。用原 exporter（`scratch-fanout-en/de/make_textmd_w47.py`）从修后源码重导：diff 仅两行 gloss，51,989 → 51,948 字节；stub/real registry 均为 150 条。`ABSTRACT.txt` 未动（628 字节，不含 gloss）。

## 6. P7 目视结果（从新双 PDF 用 pdftoppm 全新渲染 110 dpi，非 card 图）

- 印刷 P7：第 2 栏底部——第 8 条金句以 `Senate, and for governor in 36 states.”` 结束，其下紧接 `—— From page 1 of this issue.`；第 3 栏顶部为 `THE DRILLS　Übungen`，其上无孤行。裁图：`render/p7new-col2-bottom.png`、`render/p7new-col3-top.png`。
- 网页 P7：同位置一致。裁图：`render/wp7new-col2-bottom.png`、`render/wp7new-col3-top.png`。
- SVG 坐标：8 条出处行全部 x=538.5（第 2 栏），y=1397.04 / 1503.51 / 1643.35 / 1783.19 / 1923.03 / 2096.24 / 2269.45 / **2509.40**；金句末行 y=2455.03，出处行紧跟其后（间隔 54.37 = 19pt 字 + 行高 + gap，正常）。

## 7. 观察项

- 观察项一律未动（proof1 的 8 条观察项：P2 A 组说明、ABSTRACT 两处措辞、引号 «»、双前缀、P8 注节选、版面留白、P1-countries 余量、freeze baseline 配额注——均未碰）。
- 修后 "Irregular verbs…" 段由原来整段在第 2 栏改为前 2 行留在第 1 栏、余行进第 2 栏（flow 正常分栏，无断句、无溢出，run.py 零警告）。
- EDITION-RECORD.md：en 系列各版目录下均无此文件（只存在于 `fanout-ja/` 等 fanout 工作目录），故只更新了 `WEEKLY-KIT.md`（§7 交付物 SHA、§8 增加 fix1 记录、§9 增加 fix1 门禁记录）；未新建文件。

## 8. 未做事项

- 未做第二轮复校（按任务，由协调员另派）。
- 未跑 insert.py、lint --write；未 commit、未 push。
