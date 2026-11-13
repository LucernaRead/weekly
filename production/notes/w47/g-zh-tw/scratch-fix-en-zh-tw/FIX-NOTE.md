# FIX-NOTE — 2026-W47 en-zh-tw proof1 D1 修复（ABSTRACT.txt 一字 fix）

- 版：`production/2026-w47/2026-w47-en-zh-tw/`
- 缺陷来源：`hidden_files/w47/scratch-proof-en-zh-tw/PROOF-NOTE.md` D1（轻微）+ `GATE-LOG.md` §1.12/§5.1
- 修复 agent：fix-en-zh-tw，2026-11-11；只改以下两文件，未碰其他版、未碰 core-en、未碰 tools/、未重建任何 PDF
- Commit：`c0382fa7f6c0915057611d714f75949d81a29956`（一次 commit，两文件；未 push，推循环负责）
- 探针：`ls /dev/null` 存在；`echo test | git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；scratch 真实写文件成功（`probe.txt`）

## 1. 修复内容（仅两处）

### 1.1 ABSTRACT.txt 一字改
- `已宣布結果` → `已宣佈結果`（布→佈，第 1 行唯一一处）。
- 其他任何字、行尾/换行均未动；全文仍为单行（206 字符）、无 ASCII 双引号、以换行结尾。
- 修复前：498 B，SHA-256 `9daba5e8061d7c76dae599beff94431637802d9621b57ca183c96bc7120b0902`
- 修复后：498 B（布与佈皆为 3 字节 UTF-8，字节数不变），SHA-256 `47750881038ea49c33d1a562346d13a23bb0b058f6e487e3dd35a985ecc80f16`
- 修复后全文首句：“11月3日週二美國期中選舉已宣佈結果——……”；`宣布` 0×，`宣佈` 1×。

### 1.2 WEEKLY-KIT.md 修正注（§5 item 4 末尾新增一段，历史叙述未重写）
- 位置：§5 item 4 段落末（原 "…`OpenCC('s2t')`.)" 之后）、item 5 之前；新增 7 行。
- 内容：“**Correction (2026-11-11, proof1 D1):** the "0× anywhere" claim above missed one place —
  ABSTRACT.txt was outside that self-check's scope (§3 script gate lists registry.json +
  text.md + 8 SVGs only) and still carried one 已宣布結果. It has since been changed to
  已宣佈結果 (one character, 布→佈) and re-checked with the same OpenCC s2t method:
  ABSTRACT.txt now converts to itself with 0 differences. The §5 item 4 history above is
  unchanged; this note is the only addition.”
- KIT 内其余“宣布”出现处（§5 item 2/4 历史叙述、§10 note 等）均为例证历史讨论，一字未动。
  新增注本身含“宣布”1×（引述旧文“已宣布結果”），属修正注必要内容。

## 2. 验证门禁（全部通过）

### 2.1 OpenCC s2t 自查（repo venv python，`OpenCC('s2t')`；`opencc` 二进制本机未装）
- 方法：`check_s2t.py`（本 scratch 内），整文件转换后先判字符串相等，差异文件才逐字定位。
- 修复前（`s2t-pre.log`，TOTAL diffs 1）：
  - ABSTRACT.txt：len 206，diffs 1 `[(38, '布', '佈')]`
  - registry.json：0；2026-w47-en-zh-tw.text.md：0；8 个 SVG：全部 0
- 修复后（`s2t-post.log`，TOTAL diffs 0）：
  - ABSTRACT.txt：len 206，diffs 0
  - registry.json：len 16988，diffs 0；2026-w47-en-zh-tw.text.md：len 44489，diffs 0
  - svg/p1-front.svg 0、p2-life.svg 0、p3-culture.svg 0、p4-sport.svg 0、p5-youth.svg 0、
    p6-deep.svg 0、p7-lang.svg 0、p8-test.svg 0
- 注：首次跑 check 时逐字 zip 循环在数 MB 的 SVG 上极慢（CPU 争用下 >3 分钟无输出），已改写为
  相等快判，改后单次全跑约 3 分钟。旧版慢脚本未保留（同一文件已覆盖为快版）。

### 2.2 三 SHA 不变验证（修复后重算，与任务书逐字节一致；绝未重建 PDF、绝未重渲网 PDF）
| 文件 | 字节 | SHA-256 |
|---|---|---|
| `The-Lucerna-VOL4-en-zh-tw.pdf` | 38,152,350 | `7641031186c77653ac1263056a968ba7ce2ffb9383716c5a35cfad798e0fc334` |
| `The-Lucerna-VOL4-en-zh-tw.web.pdf` | 2,965,191 | `e07e5dd048dad9ab1ed42daa6d33c2e9f0dea129538b957c06afe25627e0d177` |
| `2026-w47-en-zh-tw.text.md` | 51,147 | `57cb886738e8e23d79abe531e1f03ee7372560c5020ff02d4d6997ea117651b3` |

### 2.3 ABSTRACT.txt 形式复核（修复后）
- 498 B、206 字符、单行（换行符 1 个，仅行尾）、无 ASCII 双引号、以换行结尾。
- 全版 grep：`宣布` 仅存于 WEEKLY-KIT.md（历史讨论 + 本修正注）；`*.py`、`registry.json`、
  `text.md`、`ABSTRACT.txt`、`svg/*.svg` 均已 0×。

## 3. 源头背景 —— 给即将到来的 core-en fix2 delta 重建 agent 的提示（必读）

- **版内仅 ABSTRACT.txt 与 WEEKLY-KIT.md 含“宣布”**（已核查：`registry.json`、全部 `*.py`、
  `text.md` 干净；`run.py` 无 ABSTRACT 生成逻辑）。本次修复前 grep 命中仅此二文件。
- **ABSTRACT.txt 是手工文件，不由构建生成**：它不在 `run.py` 的构建链里（`run.py` 只跑
  content12/34/56/7/8），没有任何脚本会从 registry/text.md/SVG 重新生成它。
- 因此，即将到来的 **core-en fix2（Q73 speak→up）delta 重建不会覆盖 ABSTRACT.txt**——
  但 delta agent 仍须**保留此修复**：重建/重插时不要用旧版 ABSTRACT 覆盖本文件；若重建流程
  涉及 ABSTRACT，请以本 commit（`c0382fa7`）的版本为准（SHA `47750881…f16`，498 B），
  并在重建后复核 OpenCC s2t 仍为 0 diffs、三 SHA 仍与上表一致。
- 同理，WEEKLY-KIT.md 的 §5 item 4 修正注是修复记录，重建时不要抹掉；若 KIT 被重写，
  请把此注（proof1 D1、ABSTRACT 一字 fix、0 diffs 复核）带回新版 KIT。
- core-en fix2 由另一 agent 并行处理中（本 agent 未读未改 core-en 任何文件）；本修复与之无交集。

## 4. 产物清单（本 scratch：`hidden_files/w47/scratch-fix-en-zh-tw/`）

- `FIX-NOTE.md`（本文件）、`probe.txt`
- `check_s2t.py`（OpenCC s2t 自查脚本）、`s2t-pre.log`（修复前 TOTAL 1）、`s2t-post.log`（修复后 TOTAL 0）
- `fix_abstract.py`（一字替换脚本，含断言）、`fix-abstract.log`（修复前后 SHA/字节数）
- 未写 repo 侧 hidden_files；未写 /tmp。
