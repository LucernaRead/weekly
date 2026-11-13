# FIX-LOG — W47 de vals_pt.json 单值修补（`ist`：`pers.` → `pess.`，以 live tr_pt.py 为准）

日期：2026-11-11（EST 05:03 起）
操作员：de vals-pt 单值修员（subagent）
目录：`hidden_files/w47/scratch-fanout-de/`（8 份 vals_*.json）
Scratch：`hidden_files/w47/scratch-fix-de-vals3/`（备份 `backup/`、验证 `verify/`、临时 `tmp/`、md5 记录 `md5-before.txt` / `md5-after.txt`、live tr md5 `live-tr-md5-before.txt` / `live-tr-md5-after.txt`）
路径说明：任务所称 `hidden_files/w47/scratch-fanout-de/` 在本机实际位于
`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fanout-de/`
（与 vals1/vals2 两棒一致；`~/workspace/weekly-git/hidden_files/w47/` 下无此目录）。
未改任何版文件、未重建、未 commit、不 push、未写盘任何 tr 文件。

## 0. 探针（开工前，均通过）

- `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`，rc=0
- scratch 目录新建并真实写文件 `tmp/probe-write.txt`（内容 `probe-write 2026-11-11T10:03:36Z`）
- TMPDIR 全程指向 scratch 内 `tmp/`，未写 /tmp（注：执行时 /tmp 实际仅用 3%，任务所称满未复现，但仍全程遵守）
- 备注：中途一次 `md5sum` 命令因路径拼接笔误（`$SRC/vals_pt.json` 中 `$SRC` 本已是文件路径）返回 rc=1，
  仅为命令笔误、未触文件；随后正确重跑 md5 全部 clean。

## 1. 改动（仅 1 处：vals_pt.json 第 277 行，值内 `pers.` → `pess.`，其余一字不动）

裁决依据（vals2 FIX-LOG §3/§4 + 任务裁决）：以 live 为准，改 vals 以匹配 live。
vals_pt.json 内 EN 键 `ist (3rd pers. sg.)` 的值原为 `ist (3.ª pers. sg.)`，
而其余 7 条同类值（bastelt/beginnt/denkt … nach/liest/schaut/schreibt/sieht + `(3rd pers. sg.)`）
均为 `(3.ª pess. sg.)`；现行 live tr_pt.py:243 记的是 `ist (3.ª pess. sg.)`
（版内 pess. 12 处、pers. 0 处）。按原 vals 重生成会把修正打回 `pers.`，故改 vals。

| 文件 | 改动 | 改前 md5 | 改后 md5 |
|---|---|---|---|
| vals_pt.json | `"ist (3rd pers. sg.)": "ist (3.ª pers. sg.)"` → `"ist (3rd pers. sg.)": "ist (3.ª pess. sg.)"`（第 277 行，仅值内一词） | 49f7d8f3aaf43df711986cab818c6fcc | 589390c26739cc85f9fc2e16b887c756 |

- 其余 7 份 vals md5 改前改后完全一致（见 `md5-before.txt` vs `md5-after.txt`；es 4a770f40…、it 8991fb55…、ja df81844b…、ko 311e7f41…、nl 3ac51839…、ru b99b7001…、zh-tw d500076f…）。
- 改前 vals_pt.json 已备份至 scratch `backup/`（`vals_pt.json` + `vals_pt.json.orig`，md5 与改前一致 49f7d8f3…）。
- 改法：原始文本精确替换（脚本内 assert：改前旧串恰 1 处、新串 0 处；改后旧串 0 处、新串 1 处；
  解析后 dict 除该值外与改前完全一致；values 总数保持 275 条）。
- `diff backup/ → 改后`：恰 1 行差异（`277c277`），无其他任何行差异。

## 2. 验证（步骤 2，全部通过）

- `python -m json.tool`：8 份全部可解析（OK）。
- 值级核对（python 解析后按值断言，非 grep 键名——键名本身含 `pers.`，grep 会误计）：
  8 条第三人称值（bastelt/beginnt/denkt … nach/ist/liest/schaut/schreibt/sieht）**全部**为 `(3.ª pess. sg.)`；
  含 `pers. sg.)` 的值 **0 条**；含 `pess. sg.)` 的值 12 条（8 条第三人称 + lese/machst/schaue/öffne 第一/第二人称）；
  values 总数 275 条不变。

## 3. 决定性验证（只在 scratch verify/ 内做）—— 全部通过

- 在 scratch `verify/` 内复制 gen_tr.py + tr_en.py + 改后 8 份 vals + 现行 tr_&lt;lang&gt;.py（另存 `verify/orig/` 作比对基准）。
- `python3 gen_tr.py <lang>` 全 8 语：**RC=0**，每语 `wrote …: 278 TR keys, typemap 10, instrmap 5, E 4`。
- 生成物与 live tr_&lt;lang&gt;.py 逐字节比对（`cmp`）：

| 语 | 结果 |
|---|---|
| es / it / ja / ko / nl / pt / ru / zh-tw（8 语） | **IDENTICAL，0 差异** |

- **8/8 零差异**：vals2 §4 的 pt 唯一 1 处漂移（`ist`：live `pess.` vs 生成 `pers.`）至此闭合；
  verify 内生成的 tr_pt.py:243 为 `'ist（第三人称单数）': 'ist (3.ª pess. sg.)'`，与 live 一致。
- live tr_&lt;lang&gt;.py 生成前后 md5 逐一比对完全一致（`live-tr-md5-before.txt` vs `live-tr-md5-after.txt`，diff 空）——
  验证过程未触动现行 tr 文件（live tr_pt.py mtime 仍为 09:35，未变）。

## 4. 状态总结

- ✅ 单值已改：vals_pt.json 仅第 277 行值内 `pers.` → `pess.`，其余一字不动（备份 + 改前/改后 md5 在上）。
- ✅ 步骤 2 验证全部通过（json.tool 8/8、8 条第三人称值全为 `pess.`、含 `pers.` 的值 0 条、diff 恰 1 行）。
- ✅ 决定性验证全部通过：gen_tr.py 全 8 语 RC=0（278 TR keys/语）；逐字节比对 **8/8 零差异**；live tr 文件 md5 前后一致。
- ⛔ 只改 vals_pt.json 一个文件；未写盘任何 tr 文件、未 commit、未 push。
