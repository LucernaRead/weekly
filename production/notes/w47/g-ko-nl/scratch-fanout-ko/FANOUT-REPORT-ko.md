# FANOUT REPORT — W47 ko family (core-ko run 10 → 10 reader editions)

- Core: `production/2026-w47/core-ko/` (reader zh-cn, run 10). Family count verified against W46: 11 ko editions in `issues/2026-w46/` → core zh-cn + 10 fan-outs.
- Order: en, de, fr, es, it, pt, nl, ru, ja, zh-tw — one edition at a time.
- Build interpreter (whole family): **/usr/bin/python3** (system PIL 10.2.0) for run.py / freeze / checks / textmd; render.py + webpdf.py on `tools/venv/bin/python`. svglib.py byte-identical to core in every edition (md5 `1c94d836d46fcf6fc67e88b0f0febd34`).
- Shared tools (in this scratch dir): `inventory.py`, `gen-map-<lang>.py` → `map-<lang>.json` (216 keys + 8 instr), `apply-ko.py`, `probe-p8keys.py`, `boxtitle-ko.py`, `check-edition.py`, `keycheck-ko.py`, `gen-record-<lang>.py`.
- Per-edition record: `<lang>/EDITION-RECORD.md` (gate logs + 150-key table); edition KIT in the edition dir.

## Editions

- **ko-en 完成（rebuild 2，2026-11-11 07:58 UTC）**：ALL GATES PASS。印版 45,262,664 B，sha256 `571699d675bd31f2cc656698df05908e6843517b8cc28b5e0b849a0f6f48cc18`；网版 4,013,441 B（< 7 MB），sha256 `02203d2490905b9d863c935ede7b378eb87bd00ce9bf5069ab8bbc2f109d4323`。150 键 150/150（#150 ✓ 预期内，与 core 相同）；芯片 138（P8 35）；P8 最小字号 9.975pt；U+2019 全扫 0；freeze baseline 8/8（/usr/bin/python3）；freeze diff 新增 CJK 7（全为 U+3000 页脚空格）；occlusion 0 flags；print/web 文字层 50,698 字节一致；text.md 332 项。修复 1 类缺陷：4 个盒标题超 386.5px 内宽（run 1 遮挡审计 2 TEXTX）→ 缩短重建 run 2，新增 `boxtitle-ko.py` 门。独立复校待协调员另派。

- **ko-de 完成（rebuild 2，2026-11-11 08:15 UTC）**：ALL GATES PASS。印版 45,682,479 B，sha256 `bcf8f141b015d01d32eff843ce0970751fce996d99ea5ddeaca9ffb913c4fda6`；网版 4,037,656 B（< 7 MB），sha256 `101073970b4eb50c514a105741f262ae98d6cc681427221e3527c0771be9b604`。150 键 150/150（#150 ✓ 预期内，与 core 相同）；芯片 138（P8 35）；P8 最小字号 9.975pt；U+2019 全扫 0；freeze baseline 8/8（/usr/bin/python3）；freeze diff 新增 CJK 7（全为 U+3000 页脚空格）；occlusion 0 flags；print/web 文字层 52,009 字节一致；text.md 332 项。修复 2 类缺陷：(1) run 1 P2-feature FLOW OVERFLOW + 遮挡 7 flags——봉사활동 注释德语 3 行（`ehrenamtliche Arbeit`，+29.7px），购物单盒被压到日历条上 → 缩短为 `Ehrenamt`（2 行）重建 run 2，P2-feature 归位 1531；教训：注释换行必须连读者语前缀 `Hinweis — ` 一起实测，前缀本身就能多占一行；(2) 盒标题 P3 389.4px、P5 396.8px 超内宽 → `Wichtig`（319.6px）、`Jugendzahlen`（345.7px）。P7 teaser 余量仅 40.8px，勿加长 P7 disclosure。独立复校待协调员另派。

- **ko-fr 完成（run 1，2026-11-11 08:36 UTC）**：ALL GATES PASS。印版 45,468,290 B，sha256 `ef8429557ec75f1473cd594185df8275056caf6338feeb6499872dfa314c2f7b`；网版 4,024,760 B（< 7 MB），sha256 `adcaba49b643ed26f4b3b1b22461ac0f1cf1275ae9f6177f64280678e77b1245`。150 键 150/150（#150 ✓ 预期内，与 core 相同）；芯片 138（P8 35）；P8 最小字号 9.975pt；U+2019 全扫 0；freeze baseline 8/8（/usr/bin/python3，README 形式 `--build core-ko`）；freeze diff 新增 CJK 7（全为 U+3000 页脚空格）；occlusion 0 flags；print/web 文字层 52,232 字节一致；text.md 332 项。修复 1 类缺陷：P7 frame 盒标题 `Structure de la semaine` 406.8px 超内宽 → `La structure`（275.9px），apply 前修、无重建。另：freeze 首跑 EDQUOT rc=120（df 45G 空闲、配额封顶），停手、只删自家笔记目录内可复现的 freeze 重建件 43M（fr/en/de 三个 freeze-*/，日志与 JSON 全留）后重试一次通过；p8 compare 须带 `--total 150` 否则报 arg 错。独立复校待协调员另派。

## 核查发现（#2，2026-11-11）

- **#1 的 en/de freeze-baseline 口径与 README 不符**：`en/freeze-en.log` 与 `de/freeze-de.log` 均显示 `repointed files: none`，且 8 个 hash 全为当版自己的 hash（en p1 `b7143ff…` = `sha-en-run2.txt` p1；de p1 `dd673d06…` = `sha-de-run2.txt` p1）；而实测 shipped core-ko p1 sha256 为 `c47bc434…`。结论：#1 的两次 baseline 实际是对版目录的重建（`--build` 指向了版目录），其 8/8 不能证明 core 可复现。fr 版已按 README 形式（`--build core-ko --core-svg core-ko/svg`）重跑：8 个 repointed 文件、hash 全为 core hash、8/8。建议协调员安排 en/de 各重跑一次 freeze baseline（core 形式），再认 8/8。
- **mk 机制已泛化**：`mk-lang.py`（`mk-de.py` 的通用版）+ 每语 `<lang>-replace.json` / `<lang>-meta.json`；`gen-record.py`（通用版记录生成器）+ 每语 `<lang>-record.json`；`style11-ko.py`（§1.1 审计，复现 #1 的 log 格式）。后续 7 语复用。

## 停止指令（#2，2026-11-11 09:01 UTC / 04:01 EST 收悉）

- #2 接协调员停止指令即刻停工，不再开始任何新版构建，等协调员消息，不自行判断继续。已写笔记与脚本全部保留，不删除。
- **指令原文称“fr 未开始”，与实际不符，特此纠正**：fr 实际已于 2026-11-11 08:36 UTC 建成并全部落盘（基于 08:40 前的旧核心 run 10）；es 亦已于 08:55 UTC 建成（基于 08:40 后的新核心），印版已落盘，网版与 text.md 因配额未落盘（见 /tmp/es-gates/）。指令提到 10 版须从修复后的核心重建——08:40 的核心改动（content12/34/7）即疑似 D2/D3/D4 修复；若核心仍在继续修，es 也可能过期。fr/en/de 是否重扩、es 是否需重建，由协调员定；待核心修好后由协调员重派 #3。
- 注：指令所称时间“~10:20 UTC”与收悉时间 09:01 UTC 不符，以收悉时间为准。

## Pending

- es、it、pt、nl、ru、ja、zh-tw：未开始。
