# FIX-LOG — W47 nl-de fix1 (D12)

- 版：`production/2026-w47/2026-w47-nl-de/`（2026-w47-nl-de），仅此一版；核心与其他版未碰。
- 核心对照：`production/2026-w47/core-nl/`（fix5 已定稿）。
- 修复员 scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-nl-de1/`
- 未 commit、未 push（协调员统一处理）。

## 开工核对（2026-11-11 17:42 UTC proof1 盘验三 SHA，一致才开工）

| 文件 | 旧 SHA-256 | 旧字节 |
|---|---|---|
| `De-Lucerna-VOL4-nl-de.pdf`（印） | `26faddf46acd8db2ec36999d5734ccff88835a554447b57526db5062f2c244ef` | 12,669,889 |
| `De-Lucerna-VOL4-nl-de-web.pdf`（网） | `74f10eefe797397b8e3e5eacc636208ebba2a73919848a1ad7c698043de97aa0` | 1,617,811 |
| `2026-w47-nl-de.text.md`（文） | `ac56f6f91c644dc0d9a86c9d6d8748bca2721c507c255efd47ff612f2170117c` | 46,219 |

三 SHA 与任务书一致，`sha256sum` + `stat` 实测，开工。

## 缺陷 D12 — Q140 题干与 key 不一致（fanout 翻译层漏译）

- key 正确，不动：registry Q140 `key = "Ik maak een surprise met een kort gedicht."`
  （`content8.py:75`，note `surprise ist eine feste Wendung`）。
- 证据链（key 要求题干含"小"）：
  - 核心中文题干 `core-nl/2026-w47-nl-zh-cn.text.md:416`：`我做一个带小诗的伪装礼物。`
  - 正文 `text.md:73`：`Twee: schrijf een gedicht — kort is ook goed.`
  - 旧德语题干 `content8.py:76`（修前）：`Ich mache eine Surprise mit einem Gedicht.`
    —— 丢了"小"，忠实译出得 `met een gedicht`，按 key 会判错。
- 生成源头定位：题干是 `content8.py:76` 的字面量，无翻译表/map 生成（grep 全版
  `Surprise mit einem Gedicht` 仅此一处；registry 键本身已是 kort，不动）。
  因此无复活路径，不存在需同步改的表。

## 修法（一词）

`content8.py:76`：

```diff
-     "Ich mache eine Surprise mit einem Gedicht. → ___", instr="Ins Niederländische übersetzen", size=13.8, gap=0)
+     "Ich mache eine Surprise mit einem kurzen Gedicht. → ___", instr="Ins Niederländische übersetzen", size=13.8, gap=0)
```

只改这一行。key（`content8.py:75`）、D11、D6/D7/D8/D10、其余文字/图/版式一律未动。

## 重建（全套在版目录正常流程内做；日志重定向一律绝对路径，目标均在本人 scratch 内）

1. `tools/venv/bin/python run.py` → `run.log`，rc=0，TOTAL 150（A2 46 / B1 73 / B2 31；
   分页 10/18/18/18/18/18/12/38），0 FLOW OVERFLOW / HEAD TOO WIDE。
   注：`flow[P8-keys] ended col 3/3 y=2565 (bottom 2560)` 与 proof1 重建逐字相同，修前即有，非新引入。
2. `tools/venv/bin/python render.py` → `render.log`，rc=0，印 PDF 12,669,892 B。
3. `tools/venv/bin/python tools/webpdf.py svg/ De-Lucerna-VOL4-nl-de-web.pdf` → `webpdf.log`，
   rc=0，网 PDF 1,617,817 B，46,746 text bytes（修前 46,739，+7 = `kurzen ` 一词）。
4. `tools/venv/bin/python scratch-fanout-nl/export_fanout.py <版目录> de` → `export.log`，rc=0，
   471 events / registry 150 / 142 单题 + 2 配对头 + 8 配对项 = 150 / 金句 8 / gloss 6。
   text.md 重导后与交付版 diff 仅一行（`diff` rc=1 仅因此行）：
   `2026-w47-nl-de.text.md:415` 题干加 `kurzen`，46,219 → 46,226 B（+7）。

## 新三 SHA + 大小（本次交付为准）

| 文件 | 新 SHA-256 | 新字节 |
|---|---|---|
| `De-Lucerna-VOL4-nl-de.pdf`（印） | `4eacaa18f98f4e8ebdba3608da8e0ec0441f70d94533fdf8efa9234daf0188bb` | 12,669,892 |
| `De-Lucerna-VOL4-nl-de-web.pdf`（网） | `aba38eecd9e18499438a5f32e6f6469c3aa590ef9ed5420061f5b6bd76730953` | 1,617,817 |
| `2026-w47-nl-de.text.md`（文） | `c1342c3fe20d7a26df33d604285a9a1fc746ea8ae1c62ef1c66e6211dd908aeb` | 46,226 |

## SVG 变化清单（交付版 vs 重建版，`svg-sha-delivered.txt` vs `svg-sha-rebuilt.txt`）

只 p8 变化，其余 7 页字节不变：

| 页 | 交付 SHA（前 12） | 重建 SHA（前 12） | 变化 |
|---|---|---|---|
| p1–p7 | 与交付一致 | 与交付一致 | 无 |
| p8-toets.svg | `c065d94787d2…` | `83c3cc7aa0a5…` | 仅 Q140 题干 +`kurzen` |

- p4（D11 盒内余量 +20.11px）字节不变，D11 完好。
- p3（D6）、p6（D7/D8）、p7（D10）字节不变，w 机制与值均在位。
- 旧题干残留核查：新 p8 SVG 与新印 PDF 全文 grep `einem Gedicht`（无 kurzen）= 0；
  `kurzen Gedicht` 在 p8 SVG（y=528.04）、印 P8（pdftotext 136 行）、网 P8（136 行）均在位。

## 验证结论（详见 GATE-LOG.md）

- 题干与 key 一致：题干现含 `kurzen`（`Ich mache eine Surprise mit einem kurzen Gedicht.`），
  可推出 key `kort`；三源（registry = text.md:415 = P8 节点 y=2236.28）Q140 全为
  `Ik maak een surprise met een kort gedicht.`，三源比对 149/149 MATCH，DIFF=[]，MISSING=[]。
- p8 compare（core-nl vs 本版）：CLEAN，keydiff=[137,138]（与 proof1 修后状态一致；140 已不在 diff 中）。
- 门禁逐项见 GATE-LOG.md，全部 PASS。
