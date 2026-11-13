# FIX-LOG — boxtitle fix2, 2026-w47-en-ru (2026-11-13 ~01:20–01:45 UTC)

只修 2026-w47-en-ru 上的 3 处 boxtitle 右溢（扫查 `scratch-sweep-xru-occl-1/SWEEP-LOG.md`）。
不碰其他版；两处已裁定接受的 HEAD TOO WIDE（P7 AN EXAMPLE LETTER、P8 Понимание текста）未动。

## 修法：只降标题字号，不改措辞（循 nl 25→23pt 先例；逐版最小改动）

先用 PIL（Newsreader-SemiBold + NotoSans-Bold，与 boxtitle_check 同一量法；
23pt 实测 ink_r 与扫查值吻合 ±0.5px）量算：标题行 x 起点固定，字号缩放整行宽度。
- P1 `THE WEEK IN NUMBERS　Цифры`（+8.5px）：tsize 23→**22**，新余量 +9.1px
- P5 `ODD SOCKS, IN NUMBERS　Цифры`（+24.3px）：22pt 仍溢 −6.0px，tsize 23→**21**，新余量 +12.7px
- P6 `A PRACTICE BALLOT　Бюллетень`（+11.4px）：tsize 23→**22**，新余量 +7.1px

改动：`content12.py:43`（P1 box 加 `tsize=22`）、`content56.py:22`（P5 box 加 `tsize=21`）、
`content56.py:106`（P6 box 加 `tsize=22`）。`svglib.py` 未动；措辞未动。

## 重建 + 门禁（改编已验证的 `scratch-fix-en/fix_build.sh` → 本目录 `fix_build2.sh`；
日志 `gates2/`，修前快照 `textmd-pre-boxtitle2.md` / `registry-pre-boxtitle2.json` /
`print-pre-boxtitle2.txt` / `web-pre-boxtitle2.txt` / `svg-before-boxtitle2.sha256`）

- run.py RC=0，TOTAL 150，MODEL 82，0 FLOW OVERFLOW；HEAD TOO WIDE = 2（仅上述两处已接受，
  位于未动的 P7/P8 页；head_check RC=1 仅此两处）
- occlusion 0 flags（selftest OK）
- p8 extract 60/150（= core 集），compare CLEAN，keydiff=[137, 138, 139, 140, 150]（预期）
- freeze baseline 8/8；freeze diff added CJK 9（全 U+3000），added Latin 145
  （F1 时 135，+10 为 fix-xru 分行所致、修前已然，非本次改动）
- spill 0 SPILL（176 OBSERVE）
- **boxtitle 0 DEFECT / 0 OBSERVE / 0 marginal（42 titles，397 body lines）**——3 处全清
- edge 0 TOUCH，0 NEAR
- creambox PASS 0 defects（P8 203 lines，slack 36.3）
- D5 census PASS：D5 Latin 0，Cyrillic 0，curly in CJK 0，164 curly 全在 Newsreader
- text.md byte-identical（`13e0e75c…`，62,552 B，diff 0 行），registry diff 0
- print/web 文字层 byte-identical；print 文字层 vs 修前 token-multiset diff 0/0，
  非空字符 multiset diff 0（27 行 pdftotext diff 仅为空白换行重排，源于盒高缩 1–2px）
- SVG 变化范围：仅 p1-front / p5-youth / p6-deep 三份，其余 5 份 byte-identical
- harness 总 RC=1，唯一原因是上述两处已接受 HEAD TOO WIDE（fix_build.sh 要求 HTW=0）；
  任务所列门禁全部绿灯

## 新旧指纹

| | 修前 | 修后 |
|---|---|---|
| 印 PDF | `dde756cbb1a1…` / 28,991,750 B | `7336fdd65c17baa107ecb7ef3871c696499c52176d131573214c08ec7195bbc3` / 28,991,765 B |
| 网 PDF | `21d126378f87…` / 2,468,667 B | `8ded0e80780b33981cb31bf438c9ceb1ac804cc226f6aa985ae94507dbcca0ad` / 2,468,694 B |
| text.md | `13e0e75ce382…` / 62,552 B | 不变 |

KIT 已更新（§2 新 SHA + §3 boxtitle fix2 bullet）。未 commit、未 push、未动其他版。
