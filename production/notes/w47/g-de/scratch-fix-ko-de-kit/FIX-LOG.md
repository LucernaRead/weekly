# FIX LOG — W47 ko-de KIT-only 修复（K1–K4，不重建、不重渲）

- 对象：`~/workspace/weekly-git/production/2026-w47/2026-w47-ko-de/WEEKLY-KIT.md`（仅此一文件）
- 时间：2026-11-11。未改任何源文件，未重建、未重渲，未 commit、未 push。
- 探针（开工前通过）：`ls /dev/null` 存在；`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` 返回 `9daeafb9864cf43055ae93beb0afd6c7d144bfa4`；goals 侧工作区真实写文件成功（`.probe`，事后已删）。
- 工作区：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-ko-de-kit/`

## 三件交付物修前后复核（均未变）

| 交付物 | 修前 | 修后 |
|---|---|---|
| 印版 Lucerna-VOL4-KO-DE.pdf | 45,682,430 B，SHA `28dbc2e775883e64e4a6b482c9da37932d3c803264ba2d9e0ef76d4052cf7cc5` | 相同（SHA 与字节数逐字一致） |
| 网版 Lucerna-VOL4-KO-DE-web.pdf | 4,035,158 B，SHA `0b309527f4beb78272a969d153c285af77e5d65c27e520c28a5959fe4a8a45c7` | 相同（SHA 与字节数逐字一致） |
| 文版 2026-w47-ko-de.text.md | 35,162 B，SHA `a192156f3c49576611f4392b9c7883c8408dfa3da8519a811cbcbec0eb87917c` | 相同（SHA 与字节数逐字一致） |

另：8 张 SVG 修前后哈希逐个一致（P2 仍为 `cfab7ef1…`，其余不变）；`git status` 只显示该目录整体为未追踪（`??`，与修前一致），无任何提交。

## K1 — KIT:23 P8 E 组干/键方向写反一半

旧文（:23）：
> E 翻译 4 (stems 137/138 in German, keys stay Korean; stems 139/140 in German, keys stay Korean)

新文（:23）：
> E 翻译 4 (stems 137/138 in Korean, keys in German; stems 139/140 in German, keys stay Korean — verified from the P8 SVG key nodes + content8.py:70/72; now agrees with :60)

盘面核对依据（亲手核实）：
- P8 SVG 键节点（`svg/p8-siheom.svg`）：`137. Der 22. Nov. ist der Kimchi-Tag. — Siehe Seite 2`、`138. Samsung gewann den Titel nach 12 Jahren. — Siehe Seite 4` 为德语键；`139. 11월 18일은 예비소집이에요.`、`140. 일요일에는 가족과 김치를 나눠 먹어요.` 为韩语键。
- P8 SVG 题干：137 `11월 22일은 김치의 날이에요. → ___`、138 `삼성이 12년 만에 우승했어요. → ___` 为韩语；139 `Der 18. Nov. ist die Vorversammlung. → ___`、140 `Am Sonntag teile ich Kimchi mit der Familie. → ___` 为德语。
- 源文件 `content8.py:69–76`：137/138 的键（第 1 串）为德语、题干（:70/:72 行）为韩语；139/140 的键为韩语、题干为德语。
- 结论：137/138 干韩键德、139/140 干德键韩；:23 改后与 :60（"keys 137/138 translated to German; stems 139/140 translated, keys stay Korean"）不再矛盾。

## K2 — KIT:105 "only P1/P4/P7 changed vs #2 run 2" 基线错误

旧文（:105）：
> SVG hashes `de/sha-de-run1.txt` (only P1/P4/P7 changed vs #2 run 2 — the core D2/D3/D4 fixes; P2/P3/P5/P6/P8 byte-identical to #2 run 2).

新文（:105）：
> SVG hashes `de/sha-de-run1.txt` (vs #2 run 2, P1/P2/P4/P7 changed — P2 is the fix1 D5 change, content12.py:174, P2 SVG 92390ad4…→cfab7ef1…; P3/P5/P6/P8 byte-identical to #2 run 2. "Only P1/P4/P7 changed" holds only vs the fix1-after SVGs baseline, where the P1/P4/P7 deltas are the core D2/D3/D4 fixes).

盘面核对依据（亲手核实）：
- 现 P2 SVG 哈希：`cfab7ef105e3eee5e7ed3ef787bb9b750246d11bc84b0c253f58c4b5f9df920b`（与 `de/sha-de-run1.txt` 一致）。
- fix1 FIX-LOG:43：仅 P2（`92390ad4…→cfab7ef1…`）与 P7 变化，其余 6 张逐字节一致；`sha-svg-pre.txt`（=#2 run 2）P2 为 `92390ad44e50ea3975b4fd61b1f778dbd90d98dac8b85b36c9f046c6f8834990`。故 P2 相对 #2 run 2 必然已变——fix1 改了 `content12.py:174`（`작황 = die Ernte` → `Ernteaussichten`，盘上已见该行现为 `Ernteaussichten`）。
- 全量逐页对照（#2 run 2 `sha-svg-pre.txt` vs 现 SVG）：变：P1（`dd673d06…→f31477cb…`）、P2（`92390ad4…→cfab7ef1…`）、P4（`5f13bc4f…→06a27b96…`）、P7（`50e68b61…→f258c06b…`）；不变：P3、P5、P6、P8。
- 另一基线核对（fix1 后 `sha-svg-fix1.txt` vs 现 SVG）：变：仅 P1/P4/P7；不变：P2（`cfab7ef1…` 两边相同，fix1 D5 被原样重施）、P3/P5/P6/P8。故"仅 P1/P4/P7 变"只对 fix1 后 SVGs 基线成立。

## K3 — KIT History（:70）补 fix1 网版与文版（数值取 FIX-LOG 原文）

旧文（:70 尾句）：
> The old fix1 print (45,682,367 B, SHA `c19fe6c1…`) is superseded.

新文（:70 尾句）：
> The old fix1 print (45,682,367 B, SHA `c19fe6c1…`), web (4,035,061 B, SHA `375f0cf79e6c4592edc504cdafcca469aff402ee79393aa694a5cb4cc3dd0878`), and text.md (26,603 B, SHA `a76413749471ee248e5f6bf4c83d1047a63e3134104f9fd63098c148196ca0d1`) are superseded (web/text values from fix1 FIX-LOG :41/:42, verified by grep).

盘面核对依据（亲手 grep `scratch-fix-ko-de1/FIX-LOG.md`）：
- FIX-LOG:41：网版 `Lucerna-VOL4-KO-DE-web.pdf：4,035,061 B，SHA 375f0cf79e6c4592edc504cdafcca469aff402ee79393aa694a5cb4cc3dd0878`——grep 命中 1 行。
- FIX-LOG:42：`text.md：26,603 B（+6），SHA a76413749471ee248e5f6bf4c83d1047a63e3134104f9fd63098c148196ca0d1`——grep 命中 1 行。
- 复核员 proof2 交接里 K3 给出的数值经核实为编造：其网版前缀 `375f0cf7a179` 与文版前缀 `a7641374d6f3` 在 FIX-LOG 中 grep 均为 0 命中；写入时未使用这两个数值，只用 FIX-LOG :41/:42 原文。

## K4 — fix1 FIX-LOG 的 brief 路径注记收入 KIT（:70 末追加）

新文（:70 末追加句）：
> Fix1 provenance note (from its FIX-LOG): the brief path given in the fix1 task (`~/workspace/weekly-git/hidden_files/w47/briefs/brief-coordinator.md`) does not exist on disk; the brief actually read was the goals-side copy at `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`.

盘面核对依据（亲手核实，取 FIX-LOG 原文表述）：
- FIX-LOG:12–13 原文：任务书写的 brief 路径 `~/workspace/weekly-git/hidden_files/w47/briefs/brief-coordinator.md` 在盘上不存在；该文件实际在 `~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/briefs/brief-coordinator.md`，已读该处副本。
- 盘上验证：前一路径 `ls` 报 No such file or directory；后一路径存在（11,277 B，2026-11-09）。
- 另：改前 KIT 全文 grep `brief` 为 0 命中——FIX-LOG 所称"已记入 KIT fix1 节"在现 KIT 中并无对应文字，本次 K4 即为补记。
- **出入提醒（供协调员注意）**：本次任务书称"实际 brief 在 goals 侧 `hidden_files/w47/scratch-briefs/`"，但盘上并无 `scratch-briefs/` 这一目录（`ls` 报 No such file or directory）；实际 brief 所在是 `hidden_files/w47/briefs/brief-coordinator.md`，与 FIX-LOG 原文一致。故 KIT 写入采用 FIX-LOG 原文路径，未采用任务书的 `scratch-briefs/` 表述。

## 未碰项

- 只改了 `WEEKLY-KIT.md` 四处文字；未碰源文件（content*.py、render.py、run.py、svg/、textmd.py 等）、未重建、未重渲、未改三件交付物、未跑 insert.py / lint、未做任何 git 写操作（无 commit、无 push）。
