# FIX-LOG — W47 de 家庭 KIT-only 交付节修复（6 版）

- 日期：2026-11-11（UTC 19:35–19:40）
- 范围：只改 6 版 `WEEKLY-KIT.md` 的交付节（de-es 另含 §6 门值同步，任务明确授权）。
  不动源码、SVG、PDF、text.md；不重建、不重校内容；不 commit、不 push。
- 缺陷类：与 de-it 同类——KIT 交付节仍登记重建前（rebuild 3 / rebuild-B）的印/网 SHA 与字节数，
  与盘上 fix 后成品不符；新 SHA 只写在各 KIT 后部 fix-history 段落里，交付节未同步。
- 标头改法沿用 de-it KIT-only 修复先例（`2026-w47-de-it/WEEKLY-KIT.md` L80/L126）：
  交付节标头改称最终 rebuild，web 行的 "text bytes" 同步为实测 web PDF 的 `pdftotext` 默认模式字节数。
- 工作目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-de-*/`
- Scratch：`~/workspace/goals/lucernaread-social-media-operations/hidden_files/w47/scratch-fix-de-kit1/`
  （探针、`snapshot-before.txt`、`snapshot-after.txt`、`apply_kit_fix.py`、`de-*-print/web[-raw].txt` 均在此）

## 探针

- `git -C ~/workspace/weekly-git hash-object -w /dev/null` 成功（返回 `e69de29b…`），
  scratch 真实文件 `probe.txt` 写入成功。磁盘可写，正常开工。

## 改前实测（逐版核对，18/18 与任务表新值一致才改）

| 版 | 印 PDF（B / sha256 前 8） | 网 PDF（B / sha256 前 8） | text.md（B / sha256 前 8） |
|---|---|---|---|
| de-es | 10,968,798 / `6e8bde3f…` | 1,601,888 / `f43d561a…` | 50,124 / `5f5ea69b…` |
| de-fr | 10,932,565 / `0df35360…` | 1,600,197 / `5262bfae…` | 50,042 / `3ef1934a…` |
| de-ja | 23,901,741 / `2638a6e6…` | 2,155,095 / `161f2dd0…` | 51,913 / `a59f7847…`（不变） |
| de-ko | 15,907,006 / `1ee2229f…` | 1,909,587 / `9a069942…` | 51,498 / `fd2dbd04…`（不变） |
| de-nl | 10,964,697 / `c8a5f5e2…` | 1,596,830 / `4ed5b46e…` | 49,403 / `e904fb3d…`（不变） |
| de-ru | 10,954,759 / `d8f84e05…` | 1,647,527 / `462f516d…` | 56,231 / `dee6697b…`（不变） |

完整 SHA 与任务表逐字核对一致（见各版小节）。`pdftotext` 实测（默认模式，印/网；`-raw` 模式）：

| 版 | 默认印 B | 默认网 B | -raw（印/网同） | word multiset |
|---|---|---|---|---|
| de-es | 51,011 | 51,011 | 49,812 | identical |
| de-fr | 50,879 | 50,879 | 49,698 | identical |
| de-ja | 52,873 | 52,873 | 51,709 | （§3 只记字节，未重验 multiset） |
| de-ko | 52,318 | 52,318 | 51,151 | （同上） |
| de-nl | 50,192 | 50,192 | 49,003 | identical |
| de-ru | 57,607 | 57,607 | 56,407 | identical |

字符数校准：`wc -m` 与 KIT 既有值在 4 份未变 text.md 上逐字吻合
（ja 42,950；ko 43,394；nl 47,761；ru 47,594），故改后字符数取同法实测值。

## de-es — `2026-w47-de-es/WEEKLY-KIT.md`（§5 L80–88 + §6 L98、L126）

| 行 | 字段 | 旧值（rebuild 3） | 新值（rebuild 5 / fix1，盘上实测） |
|---|---|---|---|
| L80 | 标头 | `Deliverables (rebuild 3, 2026-11-11, final; builds 1–2 superseded)` | `Deliverables (rebuild 5, 2026-11-11, final; rebuilds 3–4 superseded)` |
| L81 | 印字节 | 10,968,797 B | 10,968,798 B |
| L82 | 印 SHA | `2c535a10f81516a749c56fa43290bc54c5bd268ba36469caa10367bc944395ed` | `6e8bde3f30a6dcb415321051d0a9f1a19f3a5c033d0167b80215a969aa69077e` |
| L83 | 网字节 | 1,558,812 B | 1,601,888 B |
| L84 | 网 text bytes | 51,014 | 51,011（实测 web 默认模式） |
| L85 | 网 SHA | `b20ceebfeba6c5e7ad2be9d2123b8406755bceff0174f34c6ca4158e03716228` | `f43d561a2e54de16ffd194ea5f05b1ad9c6c44ef6d60809324cc73e2dfd28d7e` |
| L86 | 文字节/字符 | 50,125 B，48,287 chars | 50,124 B，48,286 chars（实测 `wc -m`；−1 为 Q34 "ersten"→"erste"） |
| L88 | 文 SHA | `b36e21f45810821a28855186fe67739927e18f2aff30ef56672e3fda44753d48` | `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3` |

### de-es §6 改了哪几行（任务授权同步）

- L98 标头：`## §6 Gates (rebuild 3, 2026-11-11 — final)` →
  `## §6 Gates (rebuild 5, 2026-11-11 — final)`。
- L126 pdftotext 行：`print 51,012B / web 51,013B` → `print 51,011B / web 51,011B`；
  `-raw` 49,812B 两边未变，保留。§6 其余门值（flow ends、chips 141、P8 9.94pt、
  keycheck 149/150、freeze 各页 sha）与 fix1 无关——fix1 只动 P7 盒几何、不改文字，
  rebuild 4/5 历史段已记 "flow ends otherwise identical to rebuild 3"，故只改此一行。
- 注：旧 §5 的 "51,014 text bytes" 与旧 §6 的 web 51,013B 在 rebuild 3 口径下本身就不一致
  （差 1B）；改后两者同为实测值 51,011，收敛。

## de-fr — `2026-w47-de-fr/WEEKLY-KIT.md`（§5 L80–88）

| 行 | 字段 | 旧值（rebuild 3） | 新值（rebuild 5 / fix1，盘上实测） |
|---|---|---|---|
| L80 | 标头 | `Deliverables (rebuild 3, 2026-11-11, final; builds 1–2 superseded)` | `Deliverables (rebuild 5, 2026-11-11, final; rebuilds 3–4 superseded)` |
| L81 | 印字节 | 10,932,758 B | 10,932,565 B |
| L82 | 印 SHA | `acfdfb0d914b097d7a6cabb34f19c32068273a52242ec19155b5a697ac3a05f8` | `0df35360ac599e8af590f990ae302dfe17f8daf23904bbc4e5aac6d641ecc413` |
| L83 | 网字节 | 1,557,331 B | 1,600,197 B |
| L84 | 网 text bytes | 50,957 | 50,879（实测 web 默认模式；旧值与旧 §6 的 50,883B 亦不一致，疑为 build 2 遗留数） |
| L85 | 网 SHA | `2b13edd197ecd80559ef65329e7e4e2aef5bc5051cc8d04dca030235fb8791e4` | `5262bfaea8f8947874171b558e704e36bc7f138e3c9419afce5809a76836b167` |
| L86 | 文字节/字符 | 50,116 B，48,235 chars | 50,042 B，48,164 chars（实测 `wc -m`；−74B/−71 字符为 rebuild 4 六处 box-title 缩短 + Q34，见 §7） |
| L88 | 文 SHA | `effbd257252256566ba2af9caee79bbeecc54d01f39813e51ac0c617553b2a8b` | `3ef1934af59e6ba8f6cf59d1cd24fcfdd30f1a25e5b8c1a4f544446bd7ff0db6` |

§6 未动（不在本次授权范围，见末节“超范围发现”）。

## de-ja — `2026-w47-de-ja/WEEKLY-KIT.md`（§2 L18–22）

| 行 | 字段 | 旧值（rebuild-B build 1） | 新值（fix1 rebuild，盘上实测） |
|---|---|---|---|
| L18 | 标头 | `## §2 Deliverables (rebuild-B build 1, 2026-11-11)` | `## §2 Deliverables (fix1 rebuild, 2026-11-11)` |
| L20 | 印 | 23,901,736 B，`f412f930242d16c87a7fb783506f6e92e5020a40e323edfdb1243dfd82db459d` | 23,901,741 B，`2638a6e62c00da39933a3e921bb74d0d81d6cc00ddf2eff50000c182554f98e1` |
| L21 | 网 | 2,113,024 B，`29f65fec5681e46f5b927171163c5d66559e61ed275d998583653574d8e8294a` | 2,155,095 B，`161f2dd0bdfefecffe06944ded2d22f22410daeb321e7bc387c745da9cbcce16` |
| L21 | 网 text bytes | 52,873 | 未改——实测 web 默认模式仍为 52,873B，本来就是现行值 |
| L22 | 文 | 51,913 B，`a59f784705bec4329b7dfa19321256c2469ab7680212302481876fc96f957f69` | 未改——实测一致（只确认不改） |

## de-ko — `2026-w47-de-ko/WEEKLY-KIT.md`（§2 L18–22）

| 行 | 字段 | 旧值（rebuild-B build 1） | 新值（fix1 rebuild，盘上实测） |
|---|---|---|---|
| L18 | 标头 | `## §2 Deliverables (rebuild-B build 1, 2026-11-11)` | `## §2 Deliverables (fix1 rebuild, 2026-11-11)` |
| L20 | 印 | 15,907,001 B，`d0cb457ce4d856726b279f792156a005f376441a7f2353c75f7c50346235dc67` | 15,907,006 B，`1ee2229f5e0d9803d9b32e9c048027a1bced2783bacac9ed72a83499cd866bcc` |
| L21 | 网 | 1,906,546 B，`fe4b835a037d93c33240292af4300f5e487ac33861df66c0f33e60c374fd29d0` | 1,909,587 B，`9a0699420966ff7354c3e11d078a2e46ecde8ff35badab03f2be7f8722fe6776` |
| L21 | 网 text bytes | 52,316 | 52,318（实测 web 默认模式） |
| L22 | 文 | 51,498 B，`fd2dbd047e23bcd0fffc5245ee8d529b9e848adc11133ff46f490b304b8a66a2` | 未改——实测一致（只确认不改） |

## de-nl — `2026-w47-de-nl/WEEKLY-KIT.md`（§5 L84–92）

| 行 | 字段 | 旧值（rebuild-B build 1） | 新值（rebuild fix1，盘上实测） |
|---|---|---|---|
| L84 | 标头 | `Deliverables (rebuild-B build 1, 2026-11-11, final)` | `Deliverables (rebuild fix1, 2026-11-11, final)` |
| L85 | 印字节 | 10,964,699 B | 10,964,697 B |
| L86 | 印 SHA | `8f47eea85f54067532cad3e21ba74d3ed98133a3eabc5605dcb34ca3cca8d6d6` | `c8a5f5e2ea2affc15df0aef472ce08f74e3ae5cc826d2ef49d636c866c083521` |
| L87 | 网字节 | 1,553,854 B | 1,596,830 B |
| L88 | 网 text bytes | 50,194 | 50,192（实测 web 默认模式） |
| L89 | 网 SHA | `be22a1b5beda4dcaaeccbcffcb7a122e01bb3f92a488d896fd261808ffc34551` | `4ed5b46e385815a4358cb01407e0a476f69cdc9885801756998410fd5e336d8a` |
| L90–92 | 文 | 49,403 B / 47,761 chars，`e904fb3d7ee18a72c1316f8693f39436ff9390648261d6fbad18afcfb7fc848e` | 未改——实测一致（只确认不改） |

## de-ru — `2026-w47-de-ru/WEEKLY-KIT.md`（§5 L84–93）

| 行 | 字段 | 旧值（rebuild-B build 1） | 新值（rebuild fix1，盘上实测） |
|---|---|---|---|
| L84 | 标头 | `Deliverables (rebuild-B build 1, 2026-11-11, final)` | `Deliverables (rebuild fix1, 2026-11-11, final)` |
| L85 | 印字节 | 10,954,761 B | 10,954,759 B |
| L86 | 印 SHA | `17f334608c1dfe2cf00ce8b955e8968fce23e53b6322dfd53986845ed995c40a` | `d8f84e0500e23c19aed45e5eda095a37c8c55ca71c8e94aa43fdd0f0b5d4bf1e` |
| L87 | 网字节 | 1,605,337 B | 1,647,527 B |
| L88 | 网 text bytes | 57,613 | 57,607（实测 web 默认模式） |
| L89 | 网 SHA | `76f1aba78b60027a74a365bb2d189c62300dac49b5a25a476a499546531cb02a` | `462f516d1087dc7d997f9b7be66ccd842b7225fed37601ffcbf7c54ee9407c41` |
| L91–93 | 文 | 56,231 B / 47,594 chars，`dee6697b0ec3ff279ad4508dcc7d7402952d40fcc8670b1208a2de9158074958` | 未改——实测一致（只确认不改） |

## 改后验证（逐版，缺一不可）

1. **改前实测**：6 版 × 3 交付件 SHA256 + 字节，18/18 与任务表新值逐字一致后才改。
2. **交付节旧号 grep 0 命中**：每版交付节行范围（es L80–97、fr L80–97、ja L18–22、
   ko L18–22、nl L84–95、ru L84–96）内，旧 SHA 前缀 + 旧字节数（含 es 的 51,014 / 51,012 / 51,013）
   全部 0 命中。
3. **新值在 KIT 内出现**：6 版交付节新 SHA/字节全部就位（另与后部 fix-history 段的
   "New deliverables" 一致——新值原本就写在那里）。
4. **全生产目录快照 diff**：改前/改后两份快照各 234 个文件（6 版目录内除 `__pycache__` 外全部文件），
   仅 6 份 `WEEKLY-KIT.md` 变化，其余 228 个文件字节一致。
   前后 KIT sha256：es `0d6b3dc3…`→`b7ce61c3…`；fr `3baba1e4…`→`54099882…`；
   ja `b52723b6…`→`89d7bd97…`；ko `85ea7afb…`→`9fdbdc5f…`；nl `222acdf0…`→`a83a94f5…`；
   ru `7a030323…`→`6603835b…`。
5. **交付件 SHA 改后复算不变**：18 个交付件改后重算 sha256，与改前实测值逐字相同
   （印/网/text.md 均未被触碰）。
6. **未碰的 4 版**：de-en、de-it、de-pt、de-zh-tw 的 `WEEKLY-KIT.md` mtime 仍为改前
   （10:15 / 10:47 / 09:55 / 09:53），6 版改后 mtime 均为 2026-11-11 19:38:39。
   未 commit、未 push。

## 保留的历史引用（旧值仍在 KIT 内，但不在交付节，是历史记录）

- **de-es**：全文件旧值 0 命中——无保留历史引用（rebuild 4 历史段 L163–164 记的是
  rebuild 4 中间值 10,968,803 B / 1,558,821 B，不在本次旧值之列）。
- **de-fr L250**（§7 Round 2 历史）："Rebuild 3 re-rendered cleanly: print PDF 10,932,758 bytes,
  multiset identical."——rebuild 3 当时的印字节，历史记录，保留。
  （同段 L164–165 的 rebuild 4 中间值 10,932,570 B / 1,556,917 B 亦为历史，保留。）
- **de-ja L68**（§6 Rebuild-B 历史）："print 23,901,730 → 23,901,736 B, web 2,113,005 →
  2,113,024 B, text 51,914 → 51,913 B"——rebuild-B 前后增量，历史记录，保留。
- **de-ko L65**（§6 Rebuild-B 历史）："print 15,906,995 → 15,907,001 B, text 51,499 →
  51,498 B" 及 "Web PDF grew 1,867,491 → 1,906,546 B"——历史记录，保留。
- **de-nl / de-ru**：交付节旧值在全文件 0 命中（除下节 §6 门值的 web 旧数外，无历史引用残留）。

## 超范围发现（未改，报协调员定夺）

其余 5 版的 §6/§3 pdftotext 门值同样是重建前口径，与本次实测不符，但不在本次授权范围内，
故未动。实测现行值如下（`-raw` 各版均与 KIT 一致，未变）：

| 版 | 位置 | KIT 旧值 | 实测现行值 |
|---|---|---|---|
| de-fr | §6 L126–127 | print 50,881B / web 50,883B | print 50,879B / web 50,879B |
| de-ja | §3 L37 | print 52,872 B / web 52,873 B | print 52,873 B / web 52,873 B |
| de-ko | §3 L37 | print 52,316 B / web 52,316 B | print 52,318 B / web 52,318 B |
| de-nl | §6 L130–131 | print 50,192B / web 50,194B | print 50,192B / web 50,192B（仅 web 旧） |
| de-ru | §6 L138–139 | print 57,610B / web 57,613B | print 57,607B / web 57,607B |

（de-es 的同类门值已按授权在 L126 同步。de-fr §6 标头 L98 仍为 rebuild 3，亦未动。）
