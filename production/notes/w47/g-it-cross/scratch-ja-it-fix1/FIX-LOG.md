# FIX-LOG — 2026-W47 ja-it, 第一轮返修 (fix-1, 2026-11-11)

- 对象：`production/2026-w47/fanout-ja/2026-w47-ja-it/`（未入仓本地件）
- 修者：叶子（第一轮返修 builder；与 ja-it builder、ja 核心 builder、ja 各轮复校员、第一轮复校员不同人；未再派 subagent）
- 依据：SOP.md §8 与 §1.1、AGENTS.md、WEEKLY-KIT.md（本版）、第一轮复校 PROOF-NOTE.md（(a) 笔记）
- 结论：第一轮 (a) 作废——修后须另派第二轮全量复校（协调员派）。

## 0. 开工硬门禁（双通才动手）

- `echo probe | git -C ~/workspace/weekly-git hash-object -w --stdin` 成功（`da0c4eb8…`）。
- 在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-ja-it-fix1/` 真实写文件成功（`probe.txt`）。
- 红线遵守：只改 `production/2026-w47/fanout-ja/2026-w47-ja-it/` 内必要文件；未改 core-ja、未碰 W43–W46、其他目标语家庭、tools/；未跑 insert.py、未跑 lint --write、未 git add/commit/push/reset/stash、未提交。

## 1. 缺陷核实（动手前 grep + 公开来源，不只采信简报）

### D1：`Fujiryūga` → `Fujiryōga`（预期 5 处，实测 5 处，0 残留）

- 读法核实：藤凌駕 = ふじりょうが。
  - ozumo.jp（引日本相撲協会公式 profile）：「藤凌駕は『ふじりょうが まさはる』と読む」——https://ozumo.jp/fujiryoga/
  - Nikkan Sports 2025-10-01：「五島改め藤凌駕（ふじりょうが、22＝藤島）」——https://www.nikkansports.com/battle/sumo/news/202510010000733.html
  - 另：スポーツ報知 2026-11-11（九州場所 3 日目）：藤凌駕初金星、初土俵から 11 場所目——与本版 key 54「11° torneo dal debutto」事实一致。
- 形式：りょう = ryō，长音 ō 用 macron，与本版既有 `Hōshōryū` / `Ōnosato` / `Shōsetsu` 体例完全一致。

### D2：`Umi-no-umi` → `Chura-no-umi`（预期 1 处，实测 1 处，0 残留）

- 读法核实：美ノ海 = ちゅらのうみ。
  - Nikkan Sports 2018-05-30：「美ノ海（ちゅらのうみ）」「木崎改め美ノ海（ちゅらのうみ、25＝木瀬）」——https://www.nikkansports.com/battle/sumo/news/201805300000522.html
  - 日刊スポーツ 2018-06-24 同：「美ノ海（ちゅらのうみ）」。
- 形式：取与 fr/es/pt 版一致的连字符式 `Chura-no-umi`（fr/es/pt 已同此式；en 用 `Churanōmi`、de 用 `Churanoumi`，各版自定，不采）。

### 修前 grep 证据（.py 源码层，svg/cards/PDF 除外，均 1 次/处）

| Key | 位置 | 原文 |
|---|---|---|
| 48 | `content34.py:188` | `Umi-no-umi ha perso contro Hōshōryū il giorno 1` |
| 49 | `content34.py:190` | `Fujiryūga ha battuto Hōshōryū il giorno 3` |
| 54 | `content34.py:202` | `Kinboshi di Fujiryūga: 11° torneo dal debutto` |
| 63 | `content34.py:224` | `Fujiryūga ha vinto un kinboshi il giorno 3` |
| 111 | `content7.py:57` | `Kinboshi di Fujiryūga: 11° torneo dal debutto` |
| 116 | `content8.py:22` | `Hōshōryū ha perso contro Fujiryūga il giorno 3` |

以上 6 串均为练习的答案注文串（`e.ex` / `c.ex` / `f.ex` 的第 4 参数）：P4/P7 练习页不印注文，注文只在 P8 答案区印出；因此 6 处修后只有 `p8-tesuto.svg` 变化（见 §3）。题干（汉字 藤凌駕 / 美ノ海，冻结日语）未动；答案键（B/A/11/○）未动。

### 同类残留全版扫查（无新增改动）

- 全版 `.py` + `text.md` + SVG 文本层 grep：`Fujiryūga` / `Umi-no-umi` 修后 0 处（仅 KIT §11 F1/F4 引文保留旧形作历史，附旧→新对照）。
- 其余人名罗马字逐一复核全对，无同类残留：Ōnosato（大の里）、Hōshōryū（豊昇龍）、Yoshinofuji（義ノ富士）、Shōsetsu（小雪）、Miura Riku / Kihara Ryuichi（りくりゅう）、Miyajima、Arashiyama、Tori-no-ichi、Ni-no-tori、ryuuryuu、Chiikawa。
- 无共用罗马字表：`hidden_files/w47/scratch-fanout-ja/` 内无任何 `map-*.json`（O1 缺口依旧）；缺陷只住在各版自己的注文串里。上游同源在 `production/2026-w47/core-ja/WEEKLY-KIT.md` §3 83–88 行（`Umi-no-umi` 1×、`Fujiryūga` 4×，纯叙述文字）——按红线未碰，只报告。其他版状态（只报告，未碰）：de/en/es/fr/pt 已修；ja-nl 仍带 `Fujiryūga` 5× + `Umi-no-umi` 1×；ko/ru/zh-tw 无罗马字，不受影响。

### 第一轮复校漏了什么（对照 PROOF-NOTE.md）

- 第一轮逐字精读 + 150 题验算 + 全部机械门均未查人名罗马字读法：其「翻译层专项」只核对了 `Chiikawa` / `ryuuryuu` 与 E 组键，未列出任何相扑力士罗马字；P8 答案键本身全对（键值 B/A/11/○ 均正确），错只在注文串的拼写，p8.py compare 只比键值不比注文——机械门也拦不住这一类。教训已记入 KIT §7a：人名罗马字须逐个对公开来源核读法。

## 2. 改动清单（共 6 处，只改源码串）

- `content34.py:188`：`Umi-no-umi` → `Chura-no-umi`（key 48）
- `content34.py:190`：`Fujiryūga` → `Fujiryōga`（key 49）
- `content34.py:202`：`Kinboshi di Fujiryūga:` → `Kinboshi di Fujiryōga:`（key 54）
- `content34.py:224`：`Fujiryūga` → `Fujiryōga`（key 63）
- `content7.py:57`：`Kinboshi di Fujiryūga:` → `Kinboshi di Fujiryōga:`（key 111）
- `content8.py:22`：`contro Fujiryūga` → `contro Fujiryōga`（key 116）
- 每处替换均断言原串计数恰为 1；修后 `.py` 层 `Fujiryūga` / `Umi-no-umi` 皆 0，`Fujiryōga` 5×、`Chura-no-umi` 1×。
- 另：删除含旧字节的 `__pycache__/*.pyc`（en fix-1 同款教训；构建经 runpy 读源码，本不受影响）。
- 另：新建 `export-textmd-it.py`（仿 en 版；原脚本缺失）。修前验证：由修前 SVG 导出与修前 text.md **逐字节相同**（1379 行），才用于修后导出。

## 3. 重建（全 rc 0，零溢出）

- `tools/venv/bin/python run.py` runA：rc 0，`FLOW OVERFLOW` / `HEAD TOO WIDE` 0；登记 150 题（A2 48 / B1 73 / B2 29；分版 10/18/18/18/18/18/12/38；范文 154 字）；P8-keys 流止 col 3 y=2442（与修前相同）。
- `run.py` runB（同解释器，freeze）：rc 0，0 溢出；runA vs runB SVG sha256 **8/8 相同**；修前 vs 修后 SVG diff = 仅 `p8-tesuto.svg`（`9509da3e…` → `ed9116cd…`）。
- `render.py`（单次，事前 `ps` 确认无并行 render/run 抢写）：rc 0，print PDF 29,099,163 B（修前 29,099,162，+1 B）。
- `tools/webpdf.py svg Lucerna-VOL4-JA-IT-web.pdf`：首跑 rc=120（中途停在字体子集化，无 traceback；同刻 text.md 导出报磁盘配额超限 EDQUOT，df 显 45 GB 空闲——多 agent 并行渲染期配额被顶满）；处置：删除本 scratch 目录里我自己的 33 MB 修前 PDF 快照（其字节/SHA 已记入 KIT 与本日志），`TMPDIR=/tmp/webpdf-it-fix1` 隔离重跑：**rc 0**，web PDF 4,476,985 B（修前 4,476,984，+1 B），47,002 text bytes（修前 47,000，+2 B = `Chura-no-umi` 比 `Umi-no-umi` 多 2 字符；`ū`→`ō` 同为 2 字节）。
- `export-textmd-it.py`：text.md 46,678 B（修前 46,676，+2 B），1378 行；新旧全文 diff = 恰好 6 行（keys 48/49/54/63/111/116）。

## 4. 新双 PDF（最终）

| PDF | 字节 | SHA-256 | 页数 |
|---|---|---|---|
| Print `Lucerna-VOL4-JA-IT.pdf` | 29,099,163 | `8ed65a83d1795577f7ca83f47009f917af18c23adcd7cb1b0b335d86d690f15c` | 8 |
| Web `Lucerna-VOL4-JA-IT-web.pdf` | 4,476,985 | `d8af211a19b8a216d4bdba9048ca47a56d4fd628346b4c5dd63741306825805a` | 8 |

修前：print 29,099,162 / `75986cd7e7b0acc6e3d4887ccb023c577f3612c9a242c3093060cb7f2af200fd`；web 4,476,984 / `b3ea6d183dea6a1c5b64f5ff1a42807462a0f259fc37fea3668f7a239fc353f0`。

## 5. KIT / 记录更新

- `WEEKLY-KIT.md`：§8 双 PDF 字节/SHA 与 text.md 字节更新；freeze 改为 fix-1 runA/runB；新增 §7a（150 键复核 + 人名罗马字逐项 + macron/连字符体例依据）；§11 F1 引文加注（旧形保留作历史）；新增 §11a F4 完整修记录。
- `EDITION-RECORD.md`：交付物表与门禁更新为 fix-1 实测值；状态改为「返修完成，待第二轮全量复校」。
- 本目录文件：`FIX-LOG.md`（本文件）、`GATE-LOG.md`、构建/渲染/webpdf 日志、门 JSON、`pre-sha.txt` / `sha-runA.txt` / `sha-runB.txt`、`textmd-pre.txt`、`p8-notes-old.txt`、`p8-section-new.txt`、`print.txt` / `web.txt`（双 PDF pdftotext 提取）。

## 6. 待办（不由修者做）

- 第二轮全量复校（协调员另派）：第一轮 (a) 已作废，本修只担保 6 处改动 + 全套机械门；须从头再做一轮全量校对，零问题才算定稿。
