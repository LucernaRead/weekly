# de 版状态 — 磁盘配额阻塞（2026-11-11）

## 阻塞点

- 时间：约 2026-11-11 07:52 UTC，跑 `p8sim.py`（第 3 次调用，复现 P8 keys
  模拟）时 `content12.py` 写 `svg/p1-touiban.svg` 报
  `OSError: [Errno 122] Disk quota exceeded`。
- `df`：/home/hatch 150G 总、105G 已用、**45G 可用**——不是磁盘满，是配额
  （EDQUOT），与 2026-11-10 的教训一致。
- 按红线：已立即停手，未重试构建，未再写盘（除本记录文件一次探针写）。

## 本版已完成（de，9 版之第 1 版）

- `transform.py de` 通过：289 行日志，276 ENTRIES + 4 FSTRINGS 全应用，
  版目录 `production/2026-w47/2026-w47-zh-cn-de/` 已建。
- 徽章：532.4px，止于 x=620.4（≤888 ✓）；页脚间隙 961px ✓；
  U+2019 全扫 0 ✓（.py 层）。
- `run.py` RC=0，TOTAL 150（A2 56 / B1 69 / B2 25；按版
  10/18/18/18/18/18/12/38），其余 flow 全部在底线内。
- 唯一溢出：P8-keys，col 3 末端 y=2604.2 vs 底 2560，超 44px；
  总高 4817.3 vs 容量 4704，需省 ≥113.3px。
- `p8sim.py` 已写好，模拟与实测完全一致（2604.2，5 处溢出）。
  缩短方案已定并已验证：`de/p8short-de.json`（11 条注记串 → 13 题
  2 行变 1 行），**已真实落进版内 content 文件**（13 处替换，
  content12.py 7 处、content56.py 5 处、content8.py 1 处），
  零写盘模式重验：**0 溢出，末端 y=2521.9（余量 38.1px）**，
  仅余 4 条 2 行键（Q109/Q120/Q148/Q150，均在容量内）。

## 恢复后待办（de 版，按顺序）

1. （配额恢复后）重跑 `run.py`（须 0 溢出；盘上 SVG 仍是缩短前的旧件，
   07:51 版，须重生成）→ `render.py` → `tools/webpdf.py` →
   改编 `export_core.py` 出 `.text.md` → 全部机械门
   （verify 150、occlusion、p8 抽取/compare、freeze 8/8、文字层一致、
   P8 字号、U+2019 扫、目视）→ `WEEKLY-KIT.md` + `EDITION-RECORD.md`。
2. 再按 fr、es、it、pt、nl、ru、ja、ko 顺序逐版。

## 共享进展（不受阻塞影响，均已落地）

- `tables.py`：276 ENTRIES + 4 FSTRINGS，覆盖断言 276/276，
  最长优先消费模拟 0 未消费（`gen_tables.py`）。
- `fresh.py`：227 条原始（含 12 处跨文件重复，值全一致，已去重）+ 213 唯一。
- `transform.py`：已验证可用（de 通过）。
- `p8sim.py`：P8 keys 精确模拟器（与实测一致）。
