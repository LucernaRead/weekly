# FIX-LOG — W47 zh-tw-ru fix1（N1/N2/N6/N7 + D1俄语，機制層修復）

- **Builder**：fix1（葉子，未再派 subagent）
- **範圍**：只修 `hidden_files/w47/scratch-fanout-zh-tw/tables.py`（238 → 242 條）。**未重建任何版、未改任何版目錄文件、未碰 core-zh-tw（re-proof 在跑）、未碰其他家庭、tools/、issues/，未 commit、未 push。**本輪不產生新成品；重擴後統一重建 9 版時帶走。
- **復校對象**：`production/2026-w47/2026-w47-zh-tw-ru/`，印刷 `Lucerna-VOL4-RU.pdf`（SHA 前 16 位 `e1f3c46a9e22a3b0`）、網頁 `Lucerna-VOL4-RU-web.pdf`（`385e4b265347bb5d`），與 PROOF-NOTE 核對一致，僅核對、未動。
- **先讀**：`~/workspace/weekly-git/SOP.md` §8、§1.1 全文；`~/workspace/weekly-git/AGENTS.md`；`hidden_files/w47/briefs/brief-coordinator.md`；`hidden_files/w47/scratch-proof-zh-tw-ru1/PROOF-NOTE.md` 全文；另參照 `scratch-fix-zh-tw-it1/FIX-LOG.md`、`GATE-LOG.md` 的機制層做法（只改 tables.py 對應語值 + scratch 副本重跑 transform 驗證）。

## 探針（開工與每次寫盤前重探）

- 開工 2026-11-11 ~09:30 UTC：`echo test | git -C ~/workspace/weekly-git hash-object -w --stdin` rc=0；筆記目錄 `scratch-fix-zh-tw-ru1/probe.txt` 真實寫盤 rc=0。
- 編輯 tables.py 前重探 rc=0（備份 `tables.py.bak-pre-fix1` 同步寫盤）；scratch 驗證寫盤前重探 rc=0；寫本日誌前重探 rc=0。
- 全程無 EDQUOT；`df`：/home/hatch 150G 總，73G 已用，77G 可用。/tmp 未用（中間件一律放本筆記目錄）。

## 核心 fix1/fix2 落地核查（動手前已核，見「不動項」）

- D1 中文：盤上 core-zh-tw `下週日` 0 處、`本週日` 11 處 —— core fix1 已落地。
- N3：盤上 core `content56.py` 無 BABYMONSTER 行，`by4 = by3 + 436  # fix2: HK box shrank 480->418` —— core fix2 已落地。
- 兩者隨重擴自然帶上，本輪未改版文件，見下「不動項」。

## 改動一覽（只改 tables.py；行號為改前行號，新插條目致其後行號 +44）

| 項 | 位置 | 改前 → 改後 |
|---|---|---|
| N1（中） | tables.py:2070（ENTRIES[196] ru） | `Выучите их раз — …` → `Выучите их один раз — и любой парад станет понятен。`（全文見下） |
| D1-俄語 #1 | tables.py:252（P1 首條注） | `назначен на следующее воскресенье` → `назначен на это воскресенье` |
| D1-俄語 #2 | tables.py:274（P2 小雪注） | `В следующее воскресенье, 22 нояб., — Сяосюэ` → `В это воскресенье, 22 нояб., — Сяосюэ` |
| D1-俄語 #3 | tables.py:329（P4 注） | `назначен на следующее воскресенье` → `назначен на это воскресенье` |
| N6（低） | tables.py:373（ENTRIES[31] ru）+ :1541（[148] ru） | `гигантский шар-Пикачу` / `Гигантский шар-Пикачу` → `гигантский надувной Пикачу` / `Гигантский надувной Пикачу` |
| N7（低） | tables.py:1431（[138] ru）+ :1728（[165] ru） | `Рождество в Диснее` → `Рождество в Диснейленде`（兩處） |
| N2（中） | 新插 4 條 ENTRIES（舊 :1655 後，練習注區） | 見下「N2 新條目」 |
| N5（低） | 隨 N2 第 4 條入表（修正版） | `Накапливать баллы — это 集點。` → `Накапливать баллы — это 集點.` |

### N1 改前 → 改後（全文）

- **源鍵**：`Parades give you four useful words: 遊行 (parade), 封王 (clinching the title), 夜間 (night-time) and 終點 (finish line). Learn them once, and every parade makes sense.`
- **版內定位**：`2026-w47-zh-tw-ru/content7.py:18`（`a.para`，與表值逐字一致）。
- **改前**：`Парады дают четыре полезных слова: 遊行 (парад), 封王 (завоевание титула), 夜間 (ночной) и 終點 (финиш). Выучите их раз — и любой парад станет понятен.`
- **改後**：`Парады дают четыре полезных слова: 遊行 (парад), 封王 (завоевание титула), 夜間 (ночной) и 終點 (финиш). Выучите их один раз — и любой парад станет понятен.`
- **溯源**：表源。核心 `core-zh-tw/content7.py:18` 為英文源串，版內俄語由 transform 依表值生成；只改表，不改版文件。

### D1-俄語 改前 → 改後（逐條讀句定格，按 PROOF-NOTE §1b）

1. tables.py:252（P1 游行注）：`…назначен на следующее воскресенье, 22 нояб., в 14:00…` → `…назначен на это воскресенье, 22 нояб., в 14:00…`（`назначен на` + 賓格，`это воскресенье`）。
2. tables.py:274（P2 小雪注）：`В следующее воскресенье, 22 нояб., — Сяосюэ…` → `В это воскресенье, 22 нояб., — Сяосюэ…`（`в` + 賓格表「在本週日」）。
3. tables.py:329（P4 游行 + U 幣注）：與 #1 同句 → `назначен на это воскресенье`（其餘 U-Sport 句不動）。
- 中文 11 處隨核心 fix1、重擴帶上，本輪不碰（見「不動項」）。

### N6 改前 → 改後

- [31] tables.py:373（P5 注，源串 `a giant Pikachu balloon …`）：`…гигантский шар-Пикачу, 10-метровая световая инсталляция «Покебол»…` → `…гигантский надувной Пикачу, 10-метровая световая инсталляция «Покебол»…`
- [148] tables.py:1541（P8 key 75，源串 `A giant Pikachu balloon marks the Pokémon event.`）：`Гигантский шар-Пикачу — знак события Покемона.` → `Гигантский надувной Пикачу — знак события Покемона.`

### N7 改前 → 改後

- [138] tables.py:1431（P8 key 65）：`Рождество в Диснее — 17 нояб. — 3 янв.` → `Рождество в Диснейленде — 17 нояб. — 3 янв.`
- [165] tables.py:1728（P8 key 115）：`Рождество в Диснее начинается 17 нояб.` → `Рождество в Диснейленде начинается 17 нояб.`
- 未動：[29]/[194] 原已是 `Рождество в Диснейленде`（:167、:2047）；[167] 欄頭與 [351] P5 注亦為全稱，現全表統一。

### N2 新條目（4 條不同源串，keys 92/98/100/117/134/138）

插在練習注區 `"Xiaoxue is Nov 22, the same day."` 條（ENTRIES[158]）之後、`"The steel festival closes at 20:00."` 之前。英文源鍵取自核心 `content56.py:177/:190/:194`、`content8.py:26/:62/:70`（各源串在核心中出現次數：`The ceremony…` 1×、`Xiaoxue is Nov 22.` 3×、`Four big events…` 1×、`Collecting points…` 1×；`Xiaoxue is Nov 22, the same day.` 另有 1 處，由長源優先先替換，不衝突）。

**重要說明——為何新條目帶 9 語而不只 ru：** `transform.py` 對每條 ENTRIES 執行 `tr[LANG]`，238 條舊條目**全部** 9 語齊全（已程式核實，缺語條目 0 條）；只帶 ru 的條目會使另 8 語重擴時 `KeyError` 崩潰，適得其反。其餘 8 語值**不是新譯**，是把各版已發版內的手寫預補譯逐字搬回表內（來源行位：各版 `content56.py:178/:191/:195`、`content8.py:26/:62/:70`），已用程式逐條核對已發版原文——**36/36 逐字相符**（唯一例外見 N5）。此舉同時修掉其餘 8 語重擴時的同一回落缺口；各語既有值一字未動。

| 源串（核心英文） | de / fr / es / it / pt / nl / ru / ja / ko（逐字照搬已發版） |
|---|---|
| `The ceremony is at the Taipei Music Center.`（key 92） | Die Zeremonie ist im Taipei Music Center. / La cérémonie a lieu au Taipei Music Center. / La ceremonia es en el Taipei Music Center. / La cerimonia è al Taipei Music Center. / A cerimônia é no Taipei Music Center. / De ceremonie is in het Taipei Music Center. / **Церемония — в Тайбэйском музыкальном центре.** / 式典は台北音楽センターです。 / 시상식은 타이베이 음악 센터입니다. |
| `Xiaoxue is Nov 22.`（keys 98/117/138） | Xiaoxue ist am 22. Nov. / Xiaoxue est le 22 nov. / Xiaoxue es el 22 nov. / Xiaoxue è il 22 nov. / Xiaoxue é 22 de nov. / Xiaoxue is op 22 nov. / **Сяосюэ — 22 ноября.** / 小雪は11月22日です。 / 샤오쉐는 11월 22일입니다. |
| `Four big events fall on the same Sunday.`（key 100） | Vier große Ereignisse fallen auf denselben Sonntag. / Quatre grands événements tombent le même dimanche. / Cuatro grandes eventos caen el mismo domingo. / Quattro grandi eventi cadono la stessa domenica. / Quatro grandes eventos caem no mesmo domingo. / Vier grote evenementen vallen op dezelfde zondag. / **Четыре больших события приходятся на одно воскресенье.** / 4つの大きなイベントが同じ日曜日に重なります。 / 네 가지 큰 행사가 같은 일요일에 열립니다. |
| `Collecting points is 集點.`（key 134） | Punkte sammeln heißt 集點. / Collectionner des points se dit 集點. / Acumular puntos es 集點. / Raccogliere punti è 集點. / Acumular pontos é 集點. / Punten sparen is 集點. / **Накапливать баллы — это 集點.**（見 N5） / ポイントを集めることは集點です。 / 포인트를 모으는 것은 集點입니다. |

- KIT 所稱「5 條源串」經核為 4 條不同串（98/117/138 同串），以本次 grep 為準，與 PROOF-NOTE §2 N2 一致。

## N5 溯源結論（表源，已隨 N2 修掉）

- **位置**：P8 key 134，`2026-w47-zh-tw-ru/content8.py:62`：`f.ex("B1", "完成句子", "集點", "Накапливать баллы — это 集點。",`。
- **來源**：核心 `content8.py:62` 英文源串正是 N2 第 4 條 `"Collecting points is 集點."`；表缺此條，fan-out 時 builder 在版內手寫補譯，句尾誤用中文 `。`。**缺陷在俄語譯文層，不在核心**（核心英文以 `.` 結尾，`集點` 是術語非標點）。
- **修法**：新條目 ru 值直接用修正版 `Накапливать баллы — это 集點.`（同頁同類句一律 `.`，如 key 129/133），即 PROOF-NOTE N5 所囑「補表時一併用修正版」。36/36 核對中此條為唯一預期差異（已發版 `。` vs 入表 `.`）。重擴後版內即為修正版；**未改版文件**。

## N4 溯源結論（核心級，待裁定——只報不修）

- **位置**：P1「本週大事」末條，`2026-w47-zh-tw-ru/content12.py:68`，text.md L259–265：`"下週日 11/22 遊行、金馬獎、鋼雕閉幕、小雪"`。
- **證據（核心源，非表源）**：
  1. `tables.py` 全文 grep `鋼雕閉幕、小雪` / `11/22 遊行` 均 0 命中——該行不是任何表條目。
  2. 盤上核心（已帶 fix1）`core-zh-tw/content12.py:68` 仍為 `"本週日 11/22 遊行、金馬獎、鋼雕閉幕、小雪"`——中文原文如此，僅 D1 日期詞已改。
  3. 其餘 8 個已 proof 的 zh-tw 版同病：de/fr/es/it/pt/nl/ja/ko 的 `content12.py:68` 逐字同為 `"下週日 11/22 遊行、金馬獎、鋼雕閉幕、小雪"`（建自修復前核心）。
  4. P6 規範在核心：`core-zh-tw/content56.py:204` `"四件大事：遊行、金馬獎、鋼雕閉幕、夜間遊行"`；P6 正文 `:130` 與時間軸 `:153` 同此定義；Q100 答案 4 亦同。
- **結論**：**疑似核心級缺陷**，未改核心、未改版文件。Scratch-ru diff 中該行只見 D1 的 `下週日→本週日`，`小雪` 原封不動（見 GATE-LOG）。請協調員裁定是否開 core fix3（改為 `本週日 11/22 遊行、金馬獎、鋼雕閉幕、夜間遊行`；小雪已在 P2 與 P6 另列，不丟信息）。
- **附帶觀察（非本輪，報備）**：盤上核心 `content56.py:131` 在 fan-out 後新增一句 `——四件事只能取捨`（9 版已發版皆無此句；核心目錄未入 git，無提交記錄可查出處）。此句反向佐證「四件」為操作定義，與 N4 同屬核心側，留協調員核查其出處；重擴時它會隨核心帶入 9 版。

## 不動項（已核核心 fix1/fix2 落地，無需版內修）

- **N3**（P5 香港表 BABYMONSTER 行）：核心 fix2 已刪——盤上核心 `content56.py` 無 BABYMONSTER 行，`by4 = by3 + 436 # fix2: HK box shrank 480->418`。Scratch diff 顯示重擴即帶上（HK box 480→418、刪 1 行、by4 498→436）。本輪未改版文件。
- **D1 中文 11 處**：核心 fix1 已改——盤上核心 `下週日` 0 處、`本週日` 11 處。Scratch diff 顯示 11 處全數帶上（見 GATE-LOG §4）。本輪未改版文件。
- **其餘 8 語既有值**：一字未動（備份 diff 證明：除 8 處 ru 單行改動 + 4 條新插條目外，全表無其他差異）。

## Scratch 驗證結果（見 GATE-LOG.md）

- 筆記目錄 `work/` 內複製盤上核心（已帶 core fix1/fix2）+ 改後 tables.py + transform.py（僅 PROD 指針改向 scratch），9 語重跑 transform：**9/9 TRANSFORM OK**（各 248 行日誌，ENTRIES = 242）。
- scratch-ru：N1/N2（6 處）/N6（2 處）/N7（2 處）/D1-俄語（3 處）新值全部流入對應 content 文件，舊串全版歸零；`Xiaoxue is Nov 22, the same day.` 長源優先無衝突（content56.py:171 原句完整）。
- scratch-ru vs 已發版 diff：16 hunks，**全部分類，無剩餘**——D1 ×8 hunks（含中文 11 處 + 俄語 3 處）+ N1 ×1 + N2/N5 ×1（key 134 標點）+ N6/N7 ×3 hunks（-25 混合 + -52 + -19）+ N3 ×2 hunks（core fix2 平行帶入）+ 核心側 `四件事只能取捨` ×1（平行帶入，非本輪）。
- 其餘 8 語 scratch vs 已發版 diff：94 hunks，**全部分類，無剩餘**——D1中文 ×11/語 + N3 ×2 組/語 + `四件事只能取捨` ×1/語（以上皆平行帶入）+ it D3 ×5（it-fix1 平行帶入）+ fr Astuce mémoire ×1（fr-fix1 平行帶入）+ de P7 預告條 118↔104 ×2 行（fan-out 手工修正，見下「重擴注意」）。
- **其餘 8 語零波及證據**：8 語 diff 的 ± 行逐條清點（120 刪 / 120 增），除上述前存/平行三類外無任何其他差異；N2 的 6 處 P8 注在 8 語 diff 中**零出現**，即回填值與各版已發手寫譯文逐字一致；`bslib4.py` / `render.py` / `ABSTRACT.txt` 9 語 diff 全空。
- 驗證用副本（core 拷貝 33M + 9 版產出）已刪，僅留日誌與 diff 檔（`transform-*.log`、`diff-ru.txt`、`diff-other8.txt`）；修前備份 `tables.py.bak-pre-fix1`（207KB）留存備查。

## 重擴注意（協調員，兩項均非本輪所致、非本輪可修）

1. **de P7 預告條會回落**：de 已發版的 P7 預告條是 fan-out 時手工由 118px 壓到 104px（`p.rect` + `print("P7 teaser ends", py + 104)`），核心仍為 118；重擴後 scratch-de 為 118——de 的 P7 欄 3 壓頁腳手工修正**只活在版文件裡，不在核心**。重建輪次須重驗 de 的 P7 幾何（it-fix1 GATE-LOG §5 已記一筆，此處再報一次）。
2. **N4 待裁定**：見上。未裁定前重擴仍帶 `小雪` 版 P1 日程條；若開 core fix3，須在重擴前落地。

## 未做

- 未改核心、未改本版成品、未重建、未跑 insert.py / lint --write、無任何 git 寫操作（僅探針 `git hash-object -w`）。
- N4 未修（待裁定）。N3、D1中文未碰版文件。P7 欄高與 occlusion 終驗留待重建輪次。
