# FIX-LOG — 2026-W47 ru-en KIT 记录修正（proof3 §6 两点）

- Edition: `2026-w47-ru-en` (Russian target × English reader), VOL.4
- Executor: kit-fix (ru-en proof3 后的 KIT 记录修理工); 2026-11-11
- Scope: **只改 `production/2026-w47/2026-w47-ru-en/WEEKLY-KIT.md` 的两处记录**。
  不碰任何内容、PDF、SVG、text.md；不重建、不 commit、不 push、不派 subagent。
- Backup: `WEEKLY-KIT.md.before`（本目录，改前 SHA-256
  `1d730f135444a87def06d13c7475bc63c3dd9a29655d6512d6e6fffa93f65afb`）。
- Probes: `echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` → rc=0
  （`9daeafb9864cf43055ae93beb0afd6c7d144bfa4`）；scratch 写文件成功（`probe.txt`）。
  全程 `TMPDIR=<本目录>/tmp`，未写 /tmp。
- 依据：proof3 `PROOF-NOTE.md` §6（`scratch-proof-ru-en3/`）；proof2 与 italic 补丁的
  freeze 调用见 `scratch-ru-en-proof2/freeze-diff.json` 与
  `scratch-webpdf-italic-fix1/freeze-diff.json`（`core_svg` 均为
  `…/production/2026-w47/core-ru`，即空心调用的实证）。
  注：任务简报提到的 `hidden_files/w47/scratch-fix-ru-en-italic/` 不存在；
  italic 补丁的日志在 `scratch-webpdf-italic-fix1/`（PATCH-LOG.md + GATE-LOG.md），已读。

## 1. freeze diff 实测（正确路径重跑，与 proof3 交叉核对）

命令（repo 内工具实际用法，cwd `production/2026-w47`）：

```
tools/venv/bin/python tools/freeze.py diff --core-svg core-ru/svg --edition-svg 2026-w47-ru-en/svg --json <本目录>/freeze-diff.json
```

rc=0。逐页 removed/added（strings）：

| Page | Removed | Added | Removed Cyrillic-bearing | Added Cyrillic |
|---|---|---|---|---|
| P1 | −21 | +20 | 0 | 0 |
| P2 | −36 | +39 | 0 | 0 |
| P3 | −28 | +26 | 0 | 0 |
| P4 | −28 | +28 | 0 | 0 |
| P5 | −27 | +29 | 0 | 0 |
| P6 | −54 | +34 | 11 | 0 |
| P7 | −59 | +49 | 4 | 0 |
| P8 | −637 | +173 | 20 | 0 |
| **合计** | | | **35** | **0** |

Added CJK：U+3000 ×6（P1、P2、P3、P4、P5、P8 各 1；P6、P7 为 0），与 proof3 一致。

**与 proof3 的记录逐项一致，无出入**：逐页 removed（21/36/28/28/27/54/59/637）、
removed Cyrillic-bearing 35 条（P6 11、P7 4、P8 20）、added Cyrillic 0、
added CJK 仅 U+3000 ×6。四舍五入无差异；本实测以 `freeze-diff.json`（本目录）为准。
35 条被删俄语串逐条与 proof3 的裁定一致（P6 `УЧЕБНЫЕ ДАННЫЕ` + 图注词 → 英文；
P7 `Три уровня, три темы` → `Three levels, three topics`；P8 15 词为 Morozko 图注+credit，
`тест/недели/все/ответы` 为 P8 副标题 → 英文副标题，`можно` 为 key 46 注解）——
**无俄语核心内容丢失**。

## 2. 改动对照（全文 diff 仅此两处）

### 改动 A — KIT §1.1 spot-checks 行（第 81 行）

改前：

> `… print + web PDFs 8 pages each; web 3,367,620 bytes < 7 MB.`

改后：

> `… print + web PDFs 8 pages each; web 3,375,060 bytes < 7 MB.`

注：3,367,620 是 italic 补丁前的旧网页 PDF（weight-patch 重建值）；现值 3,375,060 与 §5
一致。另：KIT 第 85 行（weight-patch 历史记录）中的 3,367,620 是该次重建的真实历史值，
**未动**，不是过期记录。

### 改动 B — KIT §7 italic-patch 段落内的 freeze diff 句（第 86 行）

改前：

> `… freeze baseline 8/8 byte-identical RC=0, freeze diff −0 removed on all 8 pages, check_core.py golden BAD 0. …`

改后：

> `… freeze baseline 8/8 byte-identical RC=0, freeze diff (correct paths --core-svg core-ru/svg --edition-svg <edition>/svg, re-run 2026-11-11 by proof 3 and re-verified in hidden_files/w47/scratch-fix-ru-en-kit/freeze-diff.json): removed P1 −21 / P2 −36 / P3 −28 / P4 −28 / P5 −27 / P6 −54 / P7 −59 / P8 −637 strings — all the Chinese explanation layer; the 35 removed Cyrillic-bearing strings (P6 11, P7 4, P8 20) each have an English equivalent or are skipped by the shared build condition (P8 Morozko image), so no Russian core content is lost; added CJK is only U+3000 ×6 (furniture separators); added Cyrillic 0. Correction (2026-11-11, proof 3): the earlier "freeze diff −0 removed on all 8 pages" was vacuous — it ran --core-svg <core-ru> (the edition dir, which contains no .svg files directly), so the core side was empty and 0 was the empty-set result, check_core.py golden BAD 0. …`

## 3. 验证

- `diff WEEKLY-KIT.md.before WEEKLY-KIT.md`：仅 2 行改动（2 `<` + 2 `>`），其余一字不动。
- `git status --porcelain` 改前改后逐行比对：**完全一致**（267 行；ru-en 目录仍为
  `?? production/2026-w47/2026-w47-ru-en/`，未提交状态不变；除 KIT 外零改动）。
  改前基线存 `git-status-before.txt`，改后存 `git-status-after.txt`。
- 数字一致性：改后 §1.1 的 3,375,060 B 与 §5 一致；磁盘实测
  `Lucerna-VOL4-ru-en-web.pdf` = 3,375,060 bytes，SHA-256 前 16 位 `6419f7ad188d0e6a`，
  与 §5 的 `6419f7ad188d0e6aca09ae76abc739e954d0d6e1d5249171c34376e6b61360b6` 一致；
  print PDF 21,245,374 bytes 未动。
- 未 commit、未 push。无其他文件被改动。
