# W47 ja 机制表罗马字扫尾 NOTE

- 日期：2026-11-11（UTC 08:11 开工）
- 范围：仅 `hidden_files/w47/scratch-fanout-ja/` 内机制文件；未碰 production/、core-ja、其他家庭、tools/、issues/；未跑 insert.py / lint --write / 任何 apply/transform；无任何 git 写操作（不 commit、不 push）。
- 探针：开工前通过。`git hash-object -w` 返回 `796c2b4c26cd09e79967b1039c792aa39af765bc`；探针文件已真实写入 `hidden_files/w47/probe-ja-tables-sweep.txt`。
- 旧拼写：`Fujiryūga`、`Umi-no-umi`。正确形（与各版已交付 fix1 一致）：en `Churanōmi` / `Fujiryōga`；de `Churanoumi` / `Fujiryōga`；fr/es/it/pt/nl `Chura-no-umi` / `Fujiryōga`。
- 替换方式：纯文本字面替换（不重序列化 JSON），文件其余字节不变。脚本：`/tmp/ja-tables-sweep.py`（已按文件逐项断言替换前计数）。

## 改了的 24 个文件（共 71 处）

| 文件 | Fujiryūga→Fujiryōga | Umi-no-umi→正确形 | 备注 |
|---|---|---|---|
| tm-en.json | 0 | 1 → Churanōmi | 现行翻译值 |
| tm-de.json | 0 | 1 → Churanoumi | 现行翻译值 |
| tm-fr.json | 0 | 1 → Chura-no-umi | 现行翻译值 |
| tm-es.json | 0 | 1 → Chura-no-umi | 现行翻译值 |
| tm-it.json | 0 | 1 → Chura-no-umi | 现行翻译值 |
| tm-nl.json | 0 | 1 → Chura-no-umi | 现行翻译值 |
| tm2-en.json | 0 | 1 → Churanōmi | 现行翻译值 |
| tm2-de.json | 0 | 1 → Churanoumi | 现行翻译值 |
| tm2-fr.json | 0 | 1 → Chura-no-umi | 现行翻译值 |
| tm2-es.json | 0 | 1 → Chura-no-umi | 现行翻译值 |
| tm2-it.json | 0 | 1 → Chura-no-umi | 现行翻译值 |
| tm2-nl.json | 0 | 1 → Chura-no-umi | 现行翻译值 |
| tr-en-34.json | 3 | 1 → Churanōmi | 现行翻译值（单行文件） |
| tr-en-merged.json | 3 | 1 → Churanōmi | 现行翻译值 |
| map-en.json | 4 | 1 → Churanōmi | 现行机制表 |
| map-en-new.json | 1 | 0 | 现行机制表 |
| map-de.json | 4 | 1 → Churanoumi | 现行机制表 |
| map-fr.json | 4 | 1 → Chura-no-umi | 现行机制表 |
| map-es.json | 4 | 1 → Chura-no-umi | 现行机制表 |
| map-it.json | 4 | 1 → Chura-no-umi | 现行机制表（单行文件） |
| map-nl.json | 4 | 1 → Chura-no-umi | 现行机制表（单行文件） |
| gen-map-it.py | 8（键+值） | 2（en 键→Churanōmi 1；it 值→Chura-no-umi 1） | 生成器：en 源串键与 it 生成值分开改，键用 en 形、值用 it 形 |
| gen-map-ko.py | 4（en 键） | 1（en 键→Churanōmi） | 生成器：只改 en 源串键；ko 值（후지류가×4、우미노우미×1）为韩文转写，未动 |
| build-map-nl.py | 4 | 1 → Chura-no-umi | 生成器 nl 生成值 |
| **合计** | **47** | **24** | **71 处** |

## 未动的 5 个文件（有意保留，共 20 处）

| 文件 | 残留 | 不动原因 |
|---|---|---|
| map-en-before.json | Fujiryūga 4、Umi-no-umi 1 | “改前”历史快照，快照必须保持改前原样 |
| probe-p8short.py | Fujiryūga 4 | 一次性诊断探针：冻结的原注输入串（"orig"）与当时实测的候选缩短串（"new A"）；与 probe-pt 同类，改动会改变已记录的 wrap 实测 |
| probe-it-p8short.py | Fujiryūga 4 | 同上（it 版一次性诊断探针，冻结原注/候选串） |
| probe-pt-p8short.py | Fujiryūga 4 | ja-pt fix1 已明确为有意保留（冻结原注输入串）；本次只复核，未动 |
| FANOUT-REPORT-ja.md | Fujiryūga 3 | 审计报告引文：引用当时实测的缩短候选串原文（`Kinboshi van/de/di Fujiryūga…`），修复记录引文不动 |

注：probe-p8short.py / probe-it-p8short.py 与 probe-pt-p8short.py 为同一类探针（"orig" 原注 + "new A" 候选串冻结）；pt 已由 fix1 定为保留，en/it 按同一规则处理。如协调员认为两探针的 "new A" 候选串（非 "orig" 输入）应随表改，可再派单——本次按“拿不准先不动”处理，未动。

## pt 三表复核（未动）

- map-pt.json / tm-pt.json / tm2-pt.json：旧拼写 0 处；正确形已在位（map-pt.json：Fujiryōga 4、Chura-no-umi 1；tm-pt.json：Chura-no-umi 1；tm2-pt.json：Chura-no-umi 1）。三表 JSON 均可解析。

## 改后验证

- 21 个改动过的 JSON 全部可解析（`json.load` 全过）。全目录 114 个 `*.json` 扫一遍另有 3 个“非法”——均为改前已坏、与本次无关、未碰：
  - `ko-occlusion.json`、`ko-occlusion-run3.json`：实为纯文本日志却以 .json 命名（内容为 occlusion 自检输出），mtime 2026-11-11 04:35/04:46 UTC，早于本次开工；
  - `tr-en.json`：截断片段（缺外层花括号），mtime 2026-11-11 00:27 UTC，旧拼写 0 处，不在本次 29 文件之列。
- 3 个生成器 `py_compile` 全过（gen-map-it.py、gen-map-ko.py、build-map-nl.py）。
- 改后全目录递归 grep 两旧拼写：仅剩上述 5 个有意保留文件（20 处）；**现行机制值 0 处**。
- 改后各文件新形计数已逐项核对（en 版 Churanōmi、de 版 Churanoumi、fr/es/it/nl 版 Chura-no-umi、Fujiryōga 处数与改前旧形处数一一对应；gen-map-it.py 键 1 处 Churanōmi + 值 1 处 Chura-no-umi；gen-map-ko.py 键 1 处 Churanōmi）。
