# W47 de fan-out #2 — 范围界定说明（SCOPE-NOTE）

- 界定员：只读审计，未重建、未改生产文件、未 commit、未 push。
- 开工探针：`git -C ~/workspace/weekly-git hash-object -w /dev/null` 通过；scratch 真实写文件通过；磁盘 150G 总、91G 已用、59G 空闲（探针时 df）。
- 盘验时间：2026-11-11 ~14:30 EST（SHA/字节均为本次实测；run-log 引用行号为核验时的行号）。
- 依据：`scratch-fanout-de/FANOUT-REPORT-de.md` 全文、`scratch-fanout-de/README-BLOCKED.md`、
  协调员 `run-log.md` 相关条目（grep "de #2"、"gen_tr"、"680e7dee"、"40bf2905"）、
  `scratch-fix-gen-tr/FIX-LOG.md`、盘上 10 版生产目录 + 各版 `WEEKLY-KIT.md`。

## 结论先行

**de #2 已被后续工作全部覆盖，建议关闭。**

原始待办两项（① 建 10 版；② de-en build-1 的 8 门禁失败修复落盘）均已被 #3/#4/#5 棒、
重建-A/B、fix 轮与 proof2/proof3 (a) 实质覆盖；de 家庭 fan-out 10/10 已定稿
（run-log L1621、L1633："de 家庭 fan-out 10/10 已定稿确认完成"）。
8 门禁失败的逐项清单本身不可恢复（见 §1.2），但无剩余动作——没有任何一门仍停留在失败态。

§4 另列两项新发现的非 #2 剩余范围（KIT 交付节过期 6 版；core-de svglib 路由并入仍在排队），
只列范围、不开工，供协调员另派；它们不属于 de #2 的原始待办，不影响关闭建议。

---

## §1 de #2 原始待办还原（40bf2905）

### §1.1 派单原文（run-log L654，2026-11-10 21:15–21:50 EST 段）

> **de fan-out（8769fb60）拦停**：记录 scratch-fanout-de/README-BLOCKED.md。0/10；en transform
> 已验证（TRANSFORM OK，2 处宽度缺陷已修）；不完整 2026-w47-de-en/ 须删掉重拷（仅 assets/、
> cards/、render.py、run.py、svg/ 在位）。**已派接替（40bf2905，scratch-fanout-de/）**：
> 删残目录、从 core-de 新拷（先核源 SVG 141 枚）、en 起逐版做；de 核心收尾并行，
> 若 content8.py 变动须重拷重跑该版。

即待办 ①：删残缺版目录 → 从 core-de 新拷（先核源 SVG 141 枚）→ en 起逐版做 10 版
（de-en / de-fr / de-es / de-it / de-pt / de-nl / de-ru / de-ja / de-ko / de-zh-tw），
每版 transform → measure → build → 目视 → 150 键 → KIT。

### §1.2 #2 棒实际进展与未落盘项（run-log L724，2026-11-10 20:29 EST 交接补记）

> de #2（40bf2905）是例外、做了实活：de-en transform 成功、measure 24/24、build 跑完
> 但 8 门禁失败，根因与修复方案已定、只差落盘（/tmp 备份已失，盘上有
> scratch-fanout-de/FANOUT-REPORT-de.md）。

即待办 ②：de-en build-1 的 8 门禁失败修复落盘。

**⚠️ 8 门的逐项清单不可恢复（已尽力查证）：**

- `scratch-fanout-de/en/` 只有 rebuild 2 的日志（build.log、rebuild2.log）；build.log 全文
  无 FAIL/OVERFLOW/TOO WIDE 行，尾部为 run.py 正常输出（"P8 saved, TOTAL exercises: 150 / ALL DONE"）。
- `FANOUT-REPORT-de.md` 全文（grep "门失败"、"Build 1"）没有任何 de-en build-1 失败枚举；
  报告中的 de-en 记录直接从 rebuild 2（2026-11-11 02:53 UTC，ALL GATES PASS）写起。
- run-log L724 原话已说明 /tmp 备份已失，根因与修复方案的落盘记录不存在。
- 因此只能还原"8 门禁失败、根因与方案已定、未落盘"这一事实本身，不能还原 8 门各是哪一门、
  各的根因与修复值。此缺口无剩余动作价值（见 §3 第 2 项）。

### §1.3 区分：#1 棒遗留的 2 处 measure 缺陷不属于 #2 待办

README-BLOCKED.md（#1 棒 8769fb60 的记录）称：首轮 en transform 通过，measure 发现 2 处宽度缺陷
（masthead edition-line 间距 11.3→7.0；P7 工具盒 D4 条目缩短至 3 行），均已在 tr_en.py 修好，
第二轮 transform 死于配额。这 2 处是 #1 棒已修的内容，#2 棒接替时 transform/measure 已重新验证通过，
不计入 #2 的待办。

---

## §2 de 家庭终态审计（盘上实测，10/10 目录在位）

生产目录：`~/workspace/weekly-git/production/2026-w47/2026-w47-de-{en,es,fr,it,ja,ko,nl,pt,ru,zh-tw}/`
10 个全在；每版 8 张 SVG 全在；印/网/文三件 + ABSTRACT.txt + WEEKLY-KIT.md 全在。
下表 SHA256 与字节均为本次 `sha256sum` + `stat` 实测；与 run-log 协调员盘验的最新值逐一一致
（de-en fix2 L1520；de-es fix1 L1319；de-fr proof2 L1539/L1568；de-it L1569/L1578；
de-ja L1552/L1616；de-ko L1558/L1621/L1633；de-nl L1540/L1609；de-pt proof3 L1503；
de-ru L1546/L1598；de-zh-tw L1388/L1452）。

| 版 | 印版 B (sha256 前 8) | 网版 B (sha256 前 8) | text.md B (sha256 前 8) | ABSTRACT B | 复校结论 |
|---|---|---|---|---|---|
| de-en | 10,966,410 (c8904dea) | 1,597,904 (2c190c75) | 49,665 (f3f0c084) | 356 | proof3 (a) 定稿 |
| de-es | 10,968,798 (6e8bde3f) | 1,601,888 (f43d561a) | 50,124 (5f5ea69b) | 426 | proof2 (a) 定稿 |
| de-fr | 10,932,565 (0df35360) | 1,600,197 (5262bfae) | 50,042 (3ef1934a) | 414 | proof2 (a) 定稿 |
| de-it | 10,965,087 (ca802fb8) | 1,596,994 (09fb2470) | 49,712 (1594ba08) | 393 | proof2 (b,仅KIT)→KIT修→定稿 |
| de-ja | 23,901,741 (2638a6e6) | 2,155,095 (161f2dd0) | 51,913 (a59f7847) | 426 | proof2 (a) 定稿 |
| de-ko | 15,907,006 (1ee2229f) | 1,909,587 (9a069942) | 51,498 (fd2dbd04) | 388 | proof2 (a) 定稿 |
| de-nl | 10,964,697 (c8a5f5e2) | 1,596,830 (4ed5b46e) | 49,403 (e904fb3d) | 362 | proof2 (a) 定稿 |
| de-pt | 10,968,902 (c0019075) | 1,602,472 (e48265d3) | 49,812 (e2ee96eb) | 400 | proof3 (a) 定稿 |
| de-ru | 10,954,759 (d8f84e05) | 1,647,527 (462f516d) | 56,231 (dee6697b) | 688 | proof2 (a) 定稿 |
| de-zh-tw | 23,048,426 (74faeb9d) | 2,343,141 (352ead22) | 49,092 (fe62ddb5) | 294 | proof2 (a) 定稿 |

完整 SHA256（实测）：

- de-en 印 `c8904dea16d2474afdd6629789af266eabfa5d5b9ea06813d9b0fd95e38722cd` / 网
  `2c190c75c61f9dbc75db62b251cb07ba965f98866425bcd287cab08f423d9f3a` / 文
  `f3f0c08455b647c9b8f2844fbf16c33008e2717f30c584d7a3b835f98cb8a53e`
- de-es 印 `6e8bde3f30a6dcb415321051d0a9f1a19f3a5c033d0167b80215a969aa69077e` / 网
  `f43d561a2e54de16ffd194ea5f05b1ad9c6c44ef6d60809324cc73e2dfd28d7e` / 文
  `5f5ea69b69a578dd42865a4b6065ba1dc55e347e6802bd9b3eb3683a8b0027b3`
- de-fr 印 `0df35360ac599e8af590f990ae302dfe17f8daf23904bbc4e5aac6d641ecc413` / 网
  `5262bfaea8f8947874171b558e704e36bc7f138e3c9419afce5809a76836b167` / 文
  `3ef1934af59e6ba8f6cf59d1cd24fcfdd30f1a25e5b8c1a4f544446bd7ff0db6`
- de-it 印 `ca802fb853eb3f18c61cddd5da406c72c9c0471cabd84c76731478f4cdf6f2c0` / 网
  `09fb247059a96c37c0fa1fe0178b7dacf35cd1e5500fe6f089b929c722c82300` / 文
  `1594ba080bece8b9a947cf011a64a355125b8869f82413ccdb03ae31a269f255`
- de-ja 印 `2638a6e62c00da39933a3e921bb74d0d81d6cc00ddf2eff50000c182554f98e1` / 网
  `161f2dd0bdfefecffe06944ded2d22f22410daeb321e7bc387c745da9cbcce16` / 文
  `a59f784705bec4329b7dfa19321256c2469ab7680212302481876fc96f957f69`
- de-ko 印 `1ee2229f5e0d9803d9b32e9c048027a1bced2783bacac9ed72a83499cd866bcc` / 网
  `9a0699420966ff7354c3e11d078a2e46ecde8ff35badab03f2be7f8722fe6776` / 文
  `fd2dbd047e23bcd0fffc5245ee8d529b9e848adc11133ff46f490b304b8a66a2`
- de-nl 印 `c8a5f5e2ea2affc15df0aef472ce08f74e3ae5cc826d2ef49d636c866c083521` / 网
  `4ed5b46e385815a4358cb01407e0a476f69cdc9885801756998410fd5e336d8a` / 文
  `e904fb3d7ee18a72c1316f8693f39436ff9390648261d6fbad18afcfb7fc848e`
- de-pt 印 `c0019075c98389d84c3b71076d8828b9079de2e737332ff76d0fcd998a7ac4e0` / 网
  `e48265d346544f278cf25a5a040a0a5656dd7ef639480bb7ed07ad988a64282a` / 文
  `e2ee96ebd9dca775598431f87c511f53ed04dec2547896586d46a2c57a800928`
- de-ru 印 `d8f84e0500e23c19aed45e5eda095a37c8c55ca71c8e94aa43fdd0f0b5d4bf1e` / 网
  `462f516d1087dc7d997f9b7be66ccd842b7225fed37601ffcbf7c54ee9407c41` / 文
  `dee6697b0ec3ff279ad4508dcc7d7402952d40fcc8670b1208a2de9158074958`
- de-zh-tw 印 `74faeb9d898e254cd3f27a675063739701a9e40e387bde4b3622be5b7f240545` / 网
  `352ead22cee3fc77c56aa5d036015ba3e309679848cbf722a5e11d22ceb296b9` / 文
  `fe62ddb59ac6ee2b2c474c7d11019295652e95e3c6bbd22b138fb4c7e798b0f9`

注意：盘上三件与 FANOUT-REPORT 顶部的重建-A/B 表不相同——重建-A/B 之后各版又经历了
fix 轮重建（09:29–10:12 UTC），印版仅差 ±2–8 B、网版 +3,040~+43,280 B（webpdf 补丁定稿后的
字体子集，见 §3 第 5 项），text.md 除 de-pt（fix1 改 pers.→pess. 后重导）外与重建-A/B 一致。
盘上值即现行终态，以上表为准。

---

## §3 逐项覆盖证据（de #2 原始待办 → 后续工作）

| # | de #2 原始待办项 | 覆盖证据（哪一棒、哪次复校结论） | 状态 |
|---|---|---|---|
| 1 | 删残缺 de-en、从 core-de 新拷、en 起逐版建 10 版 | #3 棒 de-en rebuild 2（2026-11-11 02:53 UTC，ALL GATES PASS，FANOUT-REPORT "de-en 交付（rebuild 2）"）；#4 棒 de-fr rebuild 3（04:38 UTC，ALL GATES PASS）；#5 棒其余 8 版（es rebuild 3 06:14、it rebuild 2 06:29、pt rebuild 2 06:40、nl build 1 06:46、ru rebuild 2 06:57、ja rebuild 3 07:15、ko rebuild 2 07:23、zh-tw build 1 07:28，全部 ALL GATES PASS，报告顶部"结论：完成 — 10/10 建成"）。其后重建-A/B（08:05–09:11）10/10 从新 core 再次重建，全部 ALL GATES PASS。 | ✅ 已覆盖 |
| 2 | de-en build-1 的 8 门禁失败修复落盘 | 实质覆盖，清单不可恢复（§1.2）：de-en 自 build-1 之后从 core 全新重建 3 次——rebuild 2（02:53，ALL GATES PASS）、重建-A rebuild 3（08:15，ALL GATES PASS）、fix1（09:34，D1/D2/D3 全修，ALL GATES PASS，run-log L1322）+ fix2（10:38，只换渲染字体，D1/D2 治愈，ALL GATES PASS，run-log L1520）；最终 proof3 (a) 零缺陷定稿（run-log L1588）。build-1 可能失败的每一门都在后续全门禁 + 独立复校中被重验通过；没有任何一门仍停留在失败态。 | ✅ 已覆盖（清单不可恢复，但无剩余动作） |
| 3 | Q34 单数 vs 复数（#2 时代遗留的协调员待定项，FANOUT-REPORT"核心改动"节：10 版建版后核心 content34.py L105 由复数改为单数，待协调员定是否 10 版全部重 transform） | 重建-A/B 以 core-de build15（proof5 (a) 零问题，Q34 已为单数）重建全部 10 版。本次盘验：10 版 `content34.py` grep 均为单数句 `Am Montag öffnet in Köln der erste ___.`（10/10，复数句 0 处）。 | ✅ 已覆盖 |
| 4 | 网页 PDF 命名（FANOUT-REPORT"重建-A"节：简报称 en 版 `.web.pdf`、其余 `-web.pdf`，与磁盘实证不符，待协调员裁定） | run-log L1202 已裁定：de 家庭一律 `Die-Lucerna-VOL4-de-XX-web.pdf`（连字符，含 de-en）；en 家庭一律 `.web.pdf`；不改名。盘上 10 版一律 `-web.pdf`，proof2/proof3 均按此名核验。 | ✅ 已覆盖（已裁定） |
| 5 | 网页 PDF 工具版本分裂（FANOUT-REPORT 重建-A/B 两节：部分网版嵌 Newsreader-Bold 子集、部分未嵌，补丁定稿后协调员可决定是否以定稿工具重建） | webpdf.py 40963281 已合入（de-zh-tw fix1 记录，run-log L1388）；10 版网版均在 fix 轮以定稿工具重建（09:29–10:12 UTC）：en/es/fr/it/ja/nl/ru 网版 +42,071~+43,280 B（Bold 子集；本次 pdffonts 实测 de-en 网版含 `LucernaNewsreader-Bold` 子集 3 处），ko/pt/zh-tw +3,040~+3,050 B（Italic 子集）。proof2/proof3 逐版核验通过。家庭一致性问题已不存在。 | ✅ 已覆盖 |
| 6 | CJK 读者版 freeze `--strict-cjk` 字面无法通过（FANOUT-REPORT"第 5 棒待办"：待 parent 决定） | 按 en 家庭先例处理并在终报明说：记录新增 CJK 总量 + 零残留简体中文 + freeze_direct 8/8 作严格证明。ja 新增 2,994 / ko 3,096 / zh-tw 1,328，残留审计皆 0；ja/ko/zh-tw proof2 (a) 逐版确认（run-log L1452、L1616、L1621）。 | ✅ 已覆盖 |

---

## §4 gen_tr.py 修（680e7dee）核实——已完成，线程关闭

| 核实项 | 盘上实测 | 结论 |
|---|---|---|
| TB_NEW 是否已是 110 | `scratch-fanout-de/gen_tr.py` L116–117 实测：TB_OLD `+ 110`；TB_NEW `+ 110` | ✅ 已是 110 |
| 假注是否已订正 | TB_NEW 附注已改写为真实依据："pad 110 restores the core-de value. The formula still underestimates ink advance (it misses the +20.5/entry para offset, 6 entries = +123, only partly offset by the 29.5 vs 29.11 line-height gap), so 110 is a compensating value, not a formula fix. Verified by 6 hand-fixed editions (creambox-measured clearance +19.2..+20.0). Occlusion 0 flags cannot prove box-bottom clearance: the audit is blind to text spilling past its own box."；"90 validated by en/fr occlusion 0 flags" 假注在 gen_tr.py 已无 | ✅ 已订正 |
| 8 语 tr 重生成 diff 是否已报 | `scratch-fix-gen-tr/FIX-LOG.md` §3：8 语 × 1 行 = 8 处 diff，全部属于 pad 行（live L337），0 处其他；`scratch-fix-gen-tr/regen/` 在盘，含 8 份重生成 tr + 8 份 vals；run-log L1516 协调员盘验一致 | ✅ 已报 |
| live tr 是否被覆写 | 实测 `tr_es.py` / `tr_nl.py` / `tr_pt.py` / `tr_ru.py` L337 仍为 `+ 90` + 旧假注（与 FIX-LOG 一致：本次未覆写，下次重生成即带 pad 修） | ✅ 未覆写（按任务书） |
| nl/ru/pt rail-up 是否仍只是设计 | `gen_tr.py` 内 `RTOP`/`rail` 命中 0；`vals_nl.json` / `vals_ru.json` / `vals_pt.json` 内 `RTOP` 命中 0；设计只在 FIX-LOG §4（nl/ru/pt 平铺 pad 110 会把 NOCH EIN WORT 推到 1567.5 越 1548 线，须整条 rail 上移 20，顶 330→310） | ✅ 仍只是设计，未上线 |

补充：run-log L1516、L1621 载明 gen_tr 线程已关闭；FIX-LOG §5.4 另记 `tr_fr.py` 仍 stale
（与 rebuild-A 差 22 行，皆为盒标题缩短类翻译值，与 pad 无关），以及未决项
（en/fr pad 行旧注、公式未根治、live tr 是否同步 8 份行 337、rail-up 上线、tr_fr stale）
留待后续裁定——这些是 gen_tr 线程的遗留未决项，不属于 de #2 的待办。

---

## §5 新发现的非 #2 剩余范围（只列范围，不开工）

### §5.1 KIT 交付节登记过期——6 版（与 de-it proof2 D1 同类缺陷）

**现象（盘上实测）：** 6 版 KIT 的现行交付节仍登记重建前（rebuild 3 / rebuild-B）的印/网 SHA
与字节数，与盘上 fix 后成品不符；新 SHA 只写在各 KIT 后部的 fix-history 段落里，
交付节未同步。de-it 同类缺陷已由 proof2 (b) 发现、由 KIT-only 棒 ca1fc66c 修好
（run-log L1569/L1578：只改 KIT §5/§6 共 8 行，不动交付件、不重建、不重校，修后定稿）。

**精确范围（只改 KIT 文字，不动交付件；不 commit、不 push；修后无需重校内容，de-it 先例）：**

| 版 | 交付节位置（现行登记） | 旧值 → 盘上实测新值（只改交付节 + 门禁字节行） |
|---|---|---|
| de-es | §5 "Deliverables (rebuild 3, final)" L82–88 | 印 10,968,797 B `2c535a10…` → **10,968,798 B `6e8bde3f…`**；网 1,558,812 B `b20ceebf…` → **1,601,888 B `f43d561a…`**；文 50,125 B `b36e21f4…` → **50,124 B `5f5ea69b…`**；§6 门值亦为 rebuild 3 口径，同步改 |
| de-fr | §5 "Deliverables (rebuild 3, final)" L80–88 | 印 10,932,758 B `acfdfb0d…` → **10,932,565 B `0df35360…`**；网 1,557,331 B `2b13edd1…` → **1,600,197 B `5262bfae…`**；文 50,116 B `effbd257…` → **50,042 B `3ef1934a…`** |
| de-ja | §2 "Deliverables (rebuild-B build 1)" L18–22 | 印 23,901,736 B `f412f930…` → **23,901,741 B `2638a6e6…`**；网 2,113,024 B `29f65fec…` → **2,155,095 B `161f2dd0…`**；文不变 `a59f7847…` |
| de-ko | §2 "Deliverables (rebuild-B build 1)" L18–22 | 印 15,907,001 B `d0cb457c…` → **15,907,006 B `1ee2229f…`**；网 1,906,546 B `fe4b835a…` → **1,909,587 B `9a069942…`**；文不变 `fd2dbd04…` |
| de-nl | §5 "Deliverables (rebuild-B build 1, final)" L84–92 | 印 10,964,699 B `8f47eea8…` → **10,964,697 B `c8a5f5e2…`**；网 1,553,854 B `be22a1b5…` → **1,596,830 B `4ed5b46e…`**；文不变 `e904fb3d…` |
| de-ru | §5 "Deliverables (rebuild-B build 1, final)" L84–93 | 印 10,954,761 B `17f33460…` → **10,954,759 B `d8f84e05…`**；网 1,605,337 B `76f1aba7…` → **1,647,527 B `462f516d…`**；文不变 `dee6697b…` |

**不属此项的 4 版（交付节已与盘上一致，无需动）：** de-en（fix2 已同步，L84–90 与盘上一致）、
de-it（ca1fc66c 已修）、de-pt（L83–89 与盘上一致）、de-zh-tw（L17–19 与盘上一致）。

**定性：** 这是 fix 轮（重建-A/B 之后）产生的 KIT 同步缺口，不属于 de #2 的原始待办；
6 版交付件本身已由 proof2/proof3 (a) 定稿，KIT 文字过期不影响成品。是否派 KIT-only 棒修，
由协调员定。

### §5.2 core-de svglib.py 路由并入——仍在排队（core-de 范围，不属 de #2）

de-en fix2（76cf5c2c）的回退风险跟进：修复活在版内 svglib.py（U+201C 经 serif 分支路由到
Newsreader），transform 重复制 core-de 时会掉；根治须把同一路由并入 core-de/svglib.py。
run-log L1522/L1524/L1535/L1540/L1552/L1558 均列在排队，截至 run-log 末（L2889）未见完成记录。
范围：先核 core-de 现状，再并入路由；属 core-de 线。本棒只报状态，未核 core-de、未开工。

### §5.3 说明：core-de 本体仍未定稿（不属 de #2）

run-log L1621："de 家庭 fan-out 10/10 已定稿；11 项中的最后一项 core-de 本体仍未定稿
（web/KIT/门禁被堵，收尾 24ac4b65 未查）"。此为 core-de 线待办，不计入 de #2。

---

## 附：未验过的事项（本棒未报）

- 未重跑任何门禁（build/measure/verify/occlusion/p8/freeze/keycheck 均未重跑）；门禁结论全部引用
  各棒记录 + run-log 协调员盘验，不代表本棒独立重验。
- 未核对 10 版 text.md 全文内容与 150 键；未目视任何一页。成品内容正确性以各版 proof2/proof3 (a) 为准。
- 未核查 git 状态、未查远端入仓情况（insert/push 不在本棒范围）。
