# EDITION-RECORD — 2026-w47-ja-zh-tw

- Slug: `2026-w47-ja-zh-tw` · Target: Japanese · Reader: Traditional Chinese · VOL.4
- Status (stick 8, 2026-11-11): **完成，第 8 棒独立审计通过** — 全套门禁逐项重跑，零问题。
- Build dir: `production/2026-w47/fanout-ja/2026-w47-ja-zh-tw/`

## Deliverables (measured 2026-11-11, stick 8)

| Item | Bytes | SHA-256 |
|---|---|---|
| 8 SVG (`svg/`, p1–p8) | — | — |
| 8 cards (`cards/`, PNG) | — | — |
| Print PDF `Lucerna-VOL4-JA-ZH-TW.pdf` | 26,034,639 (fix2) | `a2640e158bf5c13eeea572de1898d7faf7311d98fa92fc27e681fccc7abac4db` |
| Web PDF `Lucerna-VOL4-JA-ZH-TW-web.pdf` | 4,788,063 (fix2) | `00575aa2683794a11b6a274c091383cf89fcb12af649b8e731a9ae024712b27a` |
| `2026-w47-ja-zh-tw.text.md` | 44,361 | `8c18a0e9fb47b145108a23b1144cd58bd9f7e3fc20e7ec5575d1cb55bb3d5db0` |
| `ABSTRACT.txt` | 235 | — |
| `WEEKLY-KIT.md` | 16,697 | — |

SHA 与 KIT 记录一致，无漂移。双 PDF 均为 8 页。**Fix1（2026-11-11）：key 47 `一之富士`→`義之富士`一字修复后重建；新 SHA 见上（旧 print `7b23a2c4…ff83e6` / web `cafe8303…9f1b9c1` 作废）。Fix2（2026-11-11）：proof1 缺陷 D1/D2（P3 注文 `出來栄え`→`出来栄え`、P4 注文 `波亂`→`波乱`）两字修复后重建；新 SHA 见上（fix1 的 print `7f05fd50…edb27b` / web `cee0a8b5…afa93e` 作废）。**

## Gates (stick 8 full re-run, evidence in hidden_files/w47/scratch-fanout-ja/, *-stick8.*)

- run.py (`tools/venv/bin/python`，与构建同一解释器）：exit 0，**TOTAL 150**，**0 FLOW OVERFLOW / HEAD TOO WIDE**（`build-zh-tw-stick8-run1.log`）
- Freeze：run.py 连跑两遍，8 SVG sha256 **8/8 逐字节一致**，且与重跑前交付的 SVG 指纹一致（`zh-tw-sha-stick8-pre/run1/run2.txt`）——交付 PDF 仍由同一批 SVG 渲染，无需重渲
- Occlusion audit (`tools/occlusion_audit.py`, selftest OK，6 类全触发阳性对照）：**0 flags**（`zh-tw-occlusion-stick8.json`）
- P8 extract (`tools/p8.py extract --total 150`): **150/150**（`zh-tw-p8-stick8.json`）
- P8 compare vs core P8 SVG: **CLEAN**，missing=[] extra=0 uncertain=[]，keydiff=**[139, 140]**——恰为预期（137/138 无简体特有字，与核心逐字节一致，故不进入 keydiff；KIT §11 F3 已裁定，不得当缺陷“修”）（`zh-tw-p8compare-stick8.json`）
- 文字层：print/web pdftotext **逐字节一致**，44,661 B
- P8 最小字号（PyMuPDF）：**9.975pt**，次档 10.35pt（题干，冻结值不动）
- U+2019 弯撇号：text.md + SVG + content*.py 全扫 **0**；简体残留：`参考答案` 0×，`參考答案` 1×，`吉伊卡哇` 4×（读者语正确译名）；`售`×5/`呢`×3 为简繁同形字，KIT §11 F4 已裁定为误报
- §1.1 grep：纸色 `#fbfaf6` 1×/页，旧纸 `#f7f1e2` 0×，`·` 0×，页行 `第 N 版 / 共 8 版` 8×
- 8 版目视（cards/ p1–p8）：干净，无溢出/重叠/压页脚/豆腐块。P7 披露 3 行繁体、teaser 未压页脚；P7 B1 桥接「りくりゅう 雙人滑 ちいかわ 吉伊卡哇」；P8 E 组 137–140 繁体答案无误；P4 栏顶「5) でお知らせします。」是核心冻结正文的正常跨栏续接，非 fan-out 缺陷

## Fix1 gates (2026-11-11，证据 in hidden_files/w47/scratch-ja-zh-tw-fix1/, *-fix1.*)

- 一字修复：`content34.py:186` key 47 `一之富士`→`義之富士`；`map-zh-tw.json` 同词条键（`一`→`义`，贴合现行核心）与值（`一`→`義`，防重引入）。
- run.py run3/run4 exit 0，TOTAL 150，0 溢出；freeze 8/8；相对修前仅 p8 SVG 变化；render/webpdf/export 全 rc 0。
- Occlusion 0 flags（selftest OK）；P8 extract 150/150；P8 compare CLEAN，keydiff=[139, 140]（预期，KIT §11 F3）；print/web 文字层逐字节一致 44,661 B；P8 最小字号 9.975pt；U+2019 全扫 0；`一之富士` 全版 0（源码、text.md、SVG、双 PDF 文字层）；150 键复核 1–150 连续、text.md 与 P8 SVG 0 差异；8 版目视干净（P8 答案区重点复核：47 题已印 `義之富士`）。
- 中途磁盘配额 EDQUOT 致 run2 中断：按规程删已合入干净的旧 worktree `weekly-es46-post`（约 1.2G）后重跑，余 12 个 dirty worktree 未动。
- 详见 `FIX-LOG.md`、`GATE-LOG.md`（本目录对应 scratch）。修后待第一轮全量复校。

## Fix2 gates (2026-11-11，证据 in hidden_files/w47/scratch-fix-ja-zh-tw2/, *-fix2.*)

- 两字修复：`content34.py:20` P3 注文 `出來栄え`→`出来栄え`（D1）；`content34.py:124` P4 注文 `波亂`→`波乱`（D2）；`map-zh-tw.json` 同两词条值同步改回日文原形（键不动，已与现行核心逐字一致，防重引入）。
- run.py run1/run2 exit 0，TOTAL 150，0 溢出；freeze 8/8；相对修前仅 p3/p4 SVG 变化；render/webpdf/export 全 rc 0。
- Occlusion 0 flags（selftest OK）；P8 extract 150/150；P8 compare CLEAN，keydiff=[139, 140]（预期，KIT §11 F3）；print/web 文字层逐字节一致 44,661 B；P8 最小字号 9.975pt；U+2019 全扫 0；`出來栄え`/`波亂` 全版 0（源码、text.md、SVG、双 PDF 文字层）；150 键复核 1–150 连续、text.md 与 P8 SVG 实质差异 0（key 150 仅为已知 ✓ 标记提取形式差异）；8 版目视干净（P3/P4 注文区重点复核：headword 已与正文同形）。
- 一次瞬时磁盘配额 EDQUOT（写笔记时报 Errno 122，`df` 仍 45G 空闲）：探针显示写盘随即恢复，无需删文件（本轮笔记目录仅 72K），按任务规则重试一次成功；此前 key-review 的 heredoc 追加失败即同一事件，已用文件脚本重跑补全。
- 详见 `FIX-LOG.md`、`GATE-LOG.md`（本目录对应 scratch）。修后待第二轮全量复校（proof2），不定稿。

## Notes

- 任务交代称 zh-tw“状态未知”——盘上实际已全套完成（KIT 05:08，PDF 05:01），第 8 棒逐项重跑门禁，全部复现，无需续做。
- KIT 所记 P7 teaser ends 2442 / P8 keys ends y=2351 未用原测量脚本重测（该脚本随旧 scratch 目录丢失）；几何审计 0 旗 + 8 版目视为证。
- 待办：无。
