# FIX-LOG — W47 zh-tw 记忆法 ja 值补时间（tables.py L2181）

**时间：** 2026-11-11 ~05:05 EST；**执行：** ja 值补时员。
**对象：** `hidden_files/w47/scratch-fanout-zh-tw/tables.py` 唯一一处：记忆法条目（源键 `Memory trick: learn 入圍 first, then 星光大道 (the red carpet at 17:00, before the ceremony), then the ceremony （頒獎） at 18:30.`）的 ja 值，L2181。
**前情：** 按 `hidden_files/w47/scratch-rekey-zh-tw-memory/FIX-LOG.md` §5 遗留 1——ja 值按 ja fix1 提案原文取用，不含 17:00/18:30，与其余 8 语不一致；本轮只补 ja 这一处。
**范围纪律：** 只改 tables.py 这一值；core、transform.py、其余条目、其余 8 语值均未动；不 commit、不 push；真实版目录未动（见 §5）。

## 探针

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0（一次通过，未硬锤）。
- scratch 真实写：`scratch-fix-zh-tw-ja-time/tmp/probe.txt` 写入并读回成功。
- 全程 `TMPDIR=<scratch>/tmp/`，未写 /tmp。

## 1. 改前 / 改后（仅 L2181 一行）

改前（原值，无时间）：
> `覚え方のコツ：まず入圍、次に星光大道（式典の前のレッドカーペット）、そして式典（頒獎）の順に覚えよう。`

改后（新值）：
> `覚え方のコツ：まず入圍、次に星光大道（式典の前のレッドカーペット、17:00）、そして式典（頒獎、18:30）の順に覚えよう。`

改动说明：只在两处括号内各插一个时间注——红地毯括号内加 `、17:00`，式典括号内加 `、18:30`；其余一字不动。顺序不变（入圍 → 星光大道 → 式典）；“式典の前のレッドカーペット”的括号说明保留；时间位置与源句一致：17:00 属红地毯（颁奖之前），18:30 属式典（頒獎）。

## 2. 备份与 diff

- 本次改前备份：`scratch-fix-zh-tw-ja-time/tables.py.bak-pre-ja-time`（SHA256 与改前 tables.py 一致：`1230d4a1a3d41fd7491b2770cb028aa54c719be7ce6018e834db638866f0341e`；同目录既有 `tables.py.bak-pre-rekey` 未动）。
- `diff tables.py.bak-pre-ja-time tables.py`：**仅 L2181 一行值变**（diff rc=1 为“有差异”的正常返回值）。
- `ast.parse` 通过。
- 替换用 Python 精确匹配执行，旧值计数 =1、新值改前计数 =0，确认只命中一处。

## 3. 禁词复查

记忆法条目 L2173–2183 grep `Ort|lugar|luogo|plek|plaats|место|場所|lieu|장소`：**0 命中**（改前基线亦为 0）。
注：全文件 grep 同组词有 18 命中，分属其他条目（其他语种正文用词），与本条目无关，不作处理。

## 4. 验证：transform 9/9（沙箱跑法）

transform.py 为 one-shot（目标版目录已存在即拒跑），真实 `production/2026-w47/2026-w47-zh-tw-<lang>` 9 个版目录已存在，故未在真实 production 目录跑。
改用沙箱（沿用 rekey 轮做法）：`HOME=<scratch>/tmp/fakehome`，其 `workspace/weekly-git/production/2026-w47/core-zh-tw` 为指向真实 core 的符号链接；跑 `~/workspace/weekly-git/tools/venv/bin/python transform.py <lang>`；各语日志存 `<scratch>/transform-<lang>.log`（transform.py 自身也在 scratch-fanout-zh-tw 内写同名日志，为工具固有行为）。

- **结果：de / fr / es / it / pt / nl / ru / ja / ko 9/9 OK**（`TRANSFORM OK`，无 AssertionError、无拒跑）。
- **逐语核查生成文件：** 9 版 `content7.py:52` 记忆法行与 tables.py 条目值逐字一致（`MATCH`，以 `tables.ENTRIES` 按源键取值为准绳核对；ko 亦 MATCH）。
- **ja 生成文件 L52：**
  > `b.para("覚え方のコツ：まず入圍、次に星光大道（式典の前のレッドカーペット、17:00）、そして式典（頒獎、18:30）の順に覚えよう。", 22)`
  程序校验通过：与新值逐字一致；17:00 在 18:30 之前；入圍 < 星光大道 < 頒獎；17:00 位于星光大道括号内、18:30 位于式典括号内（`そして式典` 在 17:00 之后、18:30 之前）；“式典の前のレッドカーペット”保留。
- 9 版 L52 均含 17:00 与 18:30（ja 此前为唯一缺失者，现已补齐）。

## 5. 真实版目录未动

沙箱生成物只在 `<scratch>/tmp/fakehome/` 内。真实 `production/2026-w47/2026-w47-zh-tw-ja/content7.py:52` 仍为重 key 前旧值（`次に式典（頒獎）、そして行われる場所（星光大道）…`），即真实 9 版未重建——与 rekey 轮 FIX-LOG §5 遗留 2 相同：已发版 9 版的 content7.py 仍含旧记忆法行，需协调员定重扩/重建时机（transform one-shot 限制 + 各版 P7 已调栏，径直重跑会丢版内手工修正）。

## 6. 未做事项

未 commit、未 push。沙箱运行产物在 `<scratch>/tmp/`（fakehome + 9 版生成目录），transform 日志 9 份在 `<scratch>/transform-<lang>.log`。
