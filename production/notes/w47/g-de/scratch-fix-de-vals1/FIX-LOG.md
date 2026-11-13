# FIX-LOG — W47 de 家庭机制表 vals 键名修补（只改 8 个键名）

日期：2026-11-11（EST 04:53 起）
操作员：de-vals 修补员（subagent）
目录：`hidden_files/w47/scratch-fanout-de/`（8 份 vals_*.json）
Scratch：`hidden_files/w47/scratch-fix-de-vals1/`（备份 `backup/`、验证 `verify/`、临时 `tmp/`）
未改任何版文件、未重建、未 commit、不 push。

## 0. 探针（开工前，均通过）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0
- scratch 目录新建并真实写文件 `PROBE.txt`（内容 `probe ok 2026-11-11`）
- TMPDIR 全程指向 scratch 内 `tmp/`，未写 /tmp（注：执行时 /tmp 实际仅用 2%，任务所称 100% 满未复现，但仍全程遵守）

## 1. 改动（每份恰 1 条键名，值一字不动，其余一字不动）

旧键：`WEIHNACHTSWÖRTER␣Christmas words` → 新键：`WEIHNACHTSWÖRTER␣Words`
（␣ = U+3000。关键发现：文件内 U+3000 是原始 UTF-8 字符（字节 E3 80 80），不是 `\u3000` 转义——
前两次替换脚本因按反斜杠转义匹配而计数 0、未写盘；改用 chr(0x3000) 构造后成功。后续脚本须按原始字符匹配。）

| 文件 | 值（改前 = 改后，一字不动） | 改前 md5 | 改后 md5 |
|---|---|---|---|
| vals_es.json | WEIHNACHTSWÖRTER␣Palabras | a902a3946a7049dc22680eb8af0aa7f2 | e27428380afeb2d3166e6345062d27a8 |
| vals_it.json | WEIHNACHTSWÖRTER␣Parole | 1e235ba6c0d3464de34d7739365b99ed | 41fe091f1a0c34c34d73717eadb8a92f |
| vals_ja.json | WEIHNACHTSWÖRTER␣聖誕 | 274e0ea9234cd8738e5405bc72a8c106 | b05fae68171f89023000ac699c264a71 |
| vals_ko.json | WEIHNACHTSWÖRTER␣크리스마스 | 2799bf19365df22880edce742481cb2f | ce4e93e334953524beacedb44099f55c |
| vals_nl.json | WEIHNACHTSWÖRTER␣Kerst | 124bf31ccabdf0432bbc970df4a6b5a9 | 53a59e8f00b48c8b8623e3b1d00e227d |
| vals_pt.json | WEIHNACHTSWÖRTER␣Palavras | 470d97d3b4135af0b3073e7a598e575c | a91d66a977e7411edcf10215377954c9 |
| vals_ru.json | WEIHNACHTSWÖRTER␣Слова | 9461d1981cf79696a0549deff841d14f | 4e08943449bf159d2fc030bf6762f4f7 |
| vals_zh-tw.json | WEIHNACHTSWÖRTER␣聖誕 | aaec7a5d17f8141ca99918067c1d6369 | 6f8d605d97ada44b8c009006dae6a2c8 |

- 改前 8 份原文件已备份至 scratch `backup/`（md5 与上表“改前”逐一核对一致）。
- 改法：原始文本精确替换（改前断言旧键恰 1 处、新键 0 处；改后断言旧键 0 处、新键 1 处；
  文件字节数恰减 10 = len("Christmas words") − len("Words")）。
- 改后逐一断言（脚本内 assert，全部通过）：解析后 dict 除该键外与改前完全一致；
  该键的值与改前相等；其余全部 272 个 values 键及所有非 values 字段一字不动。
- tr_en.py:76 已核实为 `WEIHNACHTSWÖRTER␣Words`（与任务背景一致）。

## 2. 验证（步骤 2，全部通过）

- `python -m json.tool`：8 份全部可解析（OK）。
- 旧键 `WEIHNACHTSWÖRTER␣Christmas words`：8 份合计 0 处（python 计数 + grep -F 双重核对）。
- 新键 `WEIHNACHTSWÖRTER␣Words`：8 份合计 8 处（每份 1 处）。
- 现行 tr_*.py 内 `Christmas words` 仍为 0 处（改前改后均 0，未动）。

## 3. 决定性验证（步骤 3）——未通过，因任务范围外的既有漂移，已按指令停下

- 在 scratch `verify/` 内复制 gen_tr.py + tr_en.py + 8 份 vals（改后）+ 现行 tr_<lang>.py（另存 `verify/orig/` 作比对基准）。
- `python3 gen_tr.py <lang>` 全 8 语：**RC=1，全部断言失败，未生成任何文件**。
  失败点（8 语相同，gen_tr.py:35）：
  `AssertionError: missing EN value: 'The 1903 calendar: „Im Lande des Christkinds“' (key '1903 年的日历叫《圣婴之国》')`
- 逐字节比对因此无法进行（verify/ 内无生成物）；现行 tr_<lang>.py 未被覆盖——
  生成前后 live `tr_*.py` md5 逐一比对完全一致（`live-tr-md5-before.txt` vs `live-tr-md5-after.txt`，diff 空）。

### 缺口分析（只读诊断，未做任何修复——超出“只改 8 个键名”范围）

以现行 tr_en.py（TR_EN 共 278 条）为准，逐语统计 vals["values"] 缺失的 EN 值：

| 语 | 缺失（改后 vals） | 缺失（备份=改前 vals） | 本次修复的 |
|---|---|---|---|
| es / it / ja / ko / nl / pt / ru / zh-tw（8 语完全相同） | 2 | 3 | 1（WEIHNACHTSWÖRTER␣Words） |

改后仍缺失的 2 条（8 语相同，均为 tr_en.py 的 EN 值在 vals 里不存在）：

1. key `'1903 年的日历叫《圣婴之国》'` → EN `'The 1903 calendar: „Im Lande des Christkinds“'`
2. key `'用德语写 80–100 词：《我的十一月的一周》。写清做什么手工、看哪几场比赛、和谁一起，并写一句关于忏悔祈祷日或亡灵主日的话。'` → EN `'Write in German, 80–100 words: „My week in November“. Say what you make, which games you watch and with whom — and add one sentence about the Buß- und Bettag or Totensonntag.'`

结论：这两条缺失在改前备份里同样存在（改前缺 3 条 = 上述 2 条 + WEIHNACHTSWÖRTER 旧键），
是 tr_en.py 在 vals 生成之后又改了至少 2 处 EN 值造成的既有漂移，与本次改动无关。
佐证：现行 tr_es.py:143 仍有 `'1903 年的日历叫《圣婴之国》': '«Im Lande des Christkinds» (1903)'`，
即现行 tr 文件是按更旧的 tr_en 生成的——即使补齐 vals，gen_tr.py 再生成也未必与现行逐字节一致，
须协调员另行判定（补 vals 的 2×8 条译文，或以现行 tr_en 为准重生成并接受差异）。

## 4. 状态总结

- ✅ 8 份 vals 键名已改、值未动、其余未动（备份 + 改前/改后 md5 在上）。
- ✅ 步骤 2 验证全部通过（json.tool、旧键 0 处、新键 8 处）。
- ❌ 步骤 3 决定性验证未通过：gen_tr.py 全 8 语 RC=1，断言缺 EN 值（1903 日历条，先于 WEIHNACHTSWÖRTER 条触发）。
- ⛔ 已按任务指令停下：未自行补 vals、未写盘任何 tr 文件、未动现行 tr_<lang>.py（md5 证实未动）。
- 待协调员决定：2 条缺失 EN 值 × 8 语的译文补齐方案，及补齐后是否重跑 gen_tr.py 做逐字节比对。
